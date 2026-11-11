#!/usr/bin/env python3
"""Regenerates every computed table of plan_facts.md (sections 1-12 computed parts).

    python3 plan_facts.py [out_dir]                              Phase 0 run on /home/user/house/models
    python3 plan_facts.py --main <main_floor variant.scad> [--basement <basement variant.scad>] --out <dir>
                                                                  VARIANT MODE (layout options A/B/C)

Reads /home/user/house read-only: runs openscad on the level files with
-D audit=true, parses the SCAD tables for source line numbers, and writes
  <out>/computed/secN.md   (markdown fragments)       <out>/computed/facts.json
  <out>/computed/matrix.md (the comparison block; also written in default mode)
Variant mode also writes <out>/plan_facts.md (the computed sections concatenated) and <out>/matrix.md.
Site (models/site.scad numbers) and, unless --basement is given, the basement stay the current ones.

Room classification (nothing depends on the current model's exact labels; kind = the row's 7th field):
  bedroom          kind bed.  Master bedroom = kind bed with MASTER in the label (else the largest bed row).
  full bath        kind bath with BATH in the label (WC / POWDER rooms are toilet rooms, not full baths).
  closet / WIC     kind closet (linen closets included). "WIC" label = walk-in closet.
  foyer            label containing FOYER or VESTIBULE.      mudroom: label MUDROOM.
  laundry          label LAUNDRY (main level); a W/D fixture (steel box, 3.2 ft high) inside a master-suite room also counts.
  scullery/pantry  label SCULLERY or PANTRY.                 powder room: label POWDER.
  living-kind      kind living with walls (ceiling > 0): GREAT ROOM, LIVING, DEN, SUN ROOM ...
  kitchen          kind kitchen.  garage: kind garage.  stairwell: kind stairwell (main stair opening).
  circulation      kind hall, foyer excluded (strict); "with foyer" adds the foyer rows.
  hall (min width) circulation rooms whose longer clear side is >= 6 ft (so entries and sliver rows are not 'halls').
  master suite     master bedroom + every bath/closet/hall room reached from it through doors without crossing a
                   hall room larger than 100 sq ft.
Wet fixtures (variant mode; the audit table has no type field) are recognised by colour, which the level
files define once: basin = sink, tile = shower, white = toilet/tub (in a bath room, or in a PET/DOG/LAUNDRY/MUD
utility room), counter = vanity (in a bath room), steel 3.2 ft high in a LAUNDRY room = washer/dryer.
Water heater = the round fixture in the room labelled UTILITY, boiler = steel 3.5 ft box there. Validated against
the hand lists used for the default Phase 0 run (see README-variant.md).
Paths: Dijkstra over door midpoints, as in Phase 0.
"""
import ast, json, math, re, subprocess, sys
from collections import defaultdict
from pathlib import Path
import heapq
from shapely.geometry import box, Polygon, LineString, Point
from shapely.ops import unary_union

REPO = Path("/home/user/house")
M = REPO / "models"
import argparse
_ap = argparse.ArgumentParser()
_ap.add_argument("outdir", nargs="?")
_ap.add_argument("--main"); _ap.add_argument("--basement"); _ap.add_argument("--out")
ARGS = _ap.parse_args()
VARIANT = ARGS.main is not None or ARGS.basement is not None
RUNDIR = Path(__file__).resolve().parent.parent
OUT = Path(ARGS.out or ARGS.outdir) if (ARGS.out or ARGS.outdir) else RUNDIR
CMP = OUT / "computed"
CMP.mkdir(parents=True, exist_ok=True)
model = json.load(open(RUNDIR / "model.json"))
MAIN_FILE = Path(ARGS.main).resolve() if ARGS.main else M / "main_floor.scad"
BASE_FILE = Path(ARGS.basement).resolve() if ARGS.basement else M / "basement.scad"
def _lbl(p, default):
    return default if p.parent == M else f"{p.parent.name}/{p.name}"
MAIN_LBL, BASE_LBL = _lbl(MAIN_FILE, "main_floor.scad"), _lbl(BASE_FILE, "basement.scad")

WALL_T = 0.4                       # house_lib.scad:40 wall_t (every wall, main floor)
ICF_T = model["levels"]["icf_wall_t"]   # 13.25 in, foundation.scad:37
WET_GAP = 8.0                      # along-wall chaining limit for wet groups (assumption, stated in doc)
DRAIN_EXIT = (22.16, 58.0)         # site.scad:188 building sewer leaves the basement west wall here
out = {}

# ---------------------------------------------------------------- parsing
def lit(s):
    return ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))

def audit(scad):
    r = subprocess.run(["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", str(scad)],
                       capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$", r.stdout + r.stderr, re.M)
    return [lit(g) for g in m.groups()]

def rows_src(path, func):
    """[(line_no, comment)] for each row-start line of `function func() = [ ... ];`."""
    lines = Path(path).read_text().splitlines()
    res, on = [], False
    for i, l in enumerate(lines, 1):
        if not on:
            if re.match(rf"\s*function {func}\(\)\s*=\s*\[", l):
                on = True
            continue
        if re.match(r"^\];", l):
            break
        if re.match(r"^\s*\[", l):
            c = l.split("//", 1)[1].strip() if "//" in l else ""
            res.append((i, c))
    return res

def grep(path, pat):
    return [i for i, l in enumerate(Path(path).read_text().splitlines(), 1) if re.search(pat, l)]

mrooms, mdoors, mwins, mfix = audit(MAIN_FILE)
brooms, bdoors, bwins, bfix = audit(BASE_FILE)
src = {
    "mr": rows_src(MAIN_FILE, "main_rooms"), "md": rows_src(MAIN_FILE, "main_doors"),
    "mw": rows_src(MAIN_FILE, "main_windows"),
    "mf": rows_src(MAIN_FILE, "main_fixtures") + rows_src(MAIN_FILE, "main_furniture"),
    "br": rows_src(BASE_FILE, "base_rooms"), "bd": rows_src(BASE_FILE, "base_doors"),
    "bw": rows_src(M / "foundation.scad", "basement_windows"),
    "bf": rows_src(BASE_FILE, "base_fixtures") + rows_src(BASE_FILE, "base_furniture"),
}
for k, t in (("mr", mrooms), ("md", mdoors), ("mw", mwins), ("mf", mfix), ("br", brooms), ("bd", bdoors), ("bw", bwins)):
    if len(src[k]) != len(t):
        if not VARIANT:
            raise AssertionError((k, len(src[k]), len(t)))
        print(f"note: {k}: {len(src[k])} source rows vs {len(t)} table rows; source lines for that table are approximate", file=sys.stderr)
        src[k] = (src[k] + [(0, "")] * len(t))[:len(t)]
if len(src["mf"]) < len(mfix): src["mf"] = src["mf"] + [(0, "")] * (len(mfix) - len(src["mf"]))
src["bf"] = src["bf"] + [(168, "theatre seat (generated, basement.scad:167-170)")] * (len(bfix) - len(src["bf"]))
FILE = {"mr": MAIN_LBL, "md": MAIN_LBL, "mw": MAIN_LBL, "mf": MAIN_LBL,
        "br": BASE_LBL, "bd": BASE_LBL, "bw": "foundation.scad", "bf": BASE_LBL}
def S(k, i):
    return f"{FILE[k]}:{src[k][i][0]}"

class Level:
    pass

def mk_level(tag, rooms, doors, wins, fixes, rk, dk, wk, fk):
    L = Level()
    L.tag, L.rooms, L.doors, L.wins, L.fix = tag, rooms, doors, wins, fixes
    L.rk, L.dk, L.wk, L.fk = rk, dk, wk, fk
    L.kind = [r[6] for r in rooms]
    return L

MAIN = mk_level("main", mrooms, mdoors, mwins, mfix, "mr", "md", "mw", "mf")
BASE = mk_level("base", brooms, bdoors, bwins, bfix, "br", "bd", "bw", "bf")
ALIAS = {(37.3, 35.46): "(N-S hall, unlabelled)", (13.78, 53.75): "(suite entry, 2nd piece)"}

def label(r):
    return " ".join(r[0]) if isinstance(r[0], list) else r[0]

def build_names(L):
    names = []
    for i, r in enumerate(L.rooms):
        n = label(r)
        if not n:
            n = ALIAS.get((r[1], r[2]))
            if not n:
                c = L.src_comment(i) if hasattr(L, "src_comment") else src[L.rk][i][1]
                c = re.split(r"[;(]", c)[0].strip() if c else ""
                n = f"({c})" if c else f"(unlabelled {r[6]})"
        names.append(n)
    cnt = defaultdict(int)
    for n in names:
        cnt[n] += 1
    L.names = [n if cnt[n] == 1 else f"{n} @{L.rooms[i][1]:g},{L.rooms[i][2]:g}" for i, n in enumerate(names)]
    return L

build_names(MAIN); build_names(BASE)

def rect(r):
    return (r[1], r[2], r[3], r[4])
def area(r):
    return (r[3] - r[1]) * (r[4] - r[2])
def rooms_at(L, x, y):
    hits = [i for i, r in enumerate(L.rooms) if r[1] < x < r[3] and r[2] < y < r[4]]
    return sorted(hits, key=lambda i: area(L.rooms[i]))
def room_of(L, x, y):
    h = rooms_at(L, x, y)
    return h[0] if h else None
def door_sides(L, d):
    x, y, ax, w = d[:4]
    if ax == "x":
        cx, cy = x + w / 2, y
        a, b = rooms_at(L, cx, cy - 0.8), rooms_at(L, cx, cy + 0.8)
    else:
        cx, cy = x, y + w / 2
        a, b = rooms_at(L, cx - 0.8, cy), rooms_at(L, cx + 0.8, cy)
    return (a[0] if a else None), (b[0] if b else None)
def door_mid(d):
    x, y, ax, w = d[:4]
    return (x + w / 2, y) if ax == "x" else (x, y + w / 2)
def inch(w):
    return round(w * 12, 1)

# ---------------------------------------------------------------- heated sets, exterior edges
def heated_main(r):
    return r[6] not in ("porch", "garage")
def heated_base(r):
    return r[6] != "stairwell" or label(r) != "EXIT STAIR"   # areaway is outside

def exterior_edges(L, is_heated):
    """per room index: list of (side, length, outside_class); side = N/S/E/W of the room's own edge."""
    res = {}
    H = [i for i, r in enumerate(L.rooms) if is_heated(r)]
    for i, r in enumerate(L.rooms):
        e = defaultdict(float)
        x0, y0, x1, y1 = rect(r)
        for side, (p0, p1, fixed, horiz, off) in {
            "S": (x0, x1, y0, True, -0.55), "N": (x0, x1, y1, True, 0.55),
            "W": (y0, y1, x0, False, -0.55), "E": (y0, y1, x1, False, 0.55)}.items():
            n = int(round((p1 - p0) / 0.1))
            for k in range(n):
                t = p0 + (k + 0.5) * (p1 - p0) / n
                px, py = (t, fixed + off) if horiz else (fixed + off, t)
                if any(j != i and rect(L.rooms[j])[0] < px < rect(L.rooms[j])[2] and rect(L.rooms[j])[1] < py < rect(L.rooms[j])[3]
                       for j in H):
                    continue
                cls = "yard/soil"
                for j, q in enumerate(L.rooms):
                    if j != i and q[1] < px < q[3] and q[2] < py < q[4]:
                        cls = "garage" if q[6] == "garage" else ("porch/patio (open)" if q[6] == "porch" else ("areaway" if q[6] == "stairwell" else "other"))
                        break
                e[(side, cls)] += (p1 - p0) / n
        res[i] = {k: round(v, 2) for k, v in e.items() if v > 0.04}
    return res

MAIN.ext = exterior_edges(MAIN, heated_main)
BASE.ext = exterior_edges(BASE, heated_base)

# ---------------------------------------------------------------- classification (kind + label keywords)
def LAB(L, i):
    return label(L.rooms[i]).upper()
def idx(L, f):
    return [i for i, r in enumerate(L.rooms) if f(i, r)]
def first(L, f, key=None):
    c = idx(L, f)
    if key: c.sort(key=key)
    return c[0] if c else None
def by_area_desc(L):
    return lambda i: -area(L.rooms[i])
GAR = first(MAIN, lambda i, r: r[6] == "garage")
KIT = first(MAIN, lambda i, r: r[6] == "kitchen", by_area_desc(MAIN))
FOY = first(MAIN, lambda i, r: any(k in LAB(MAIN, i) for k in ("FOYER", "VESTIBULE")))
MUD = first(MAIN, lambda i, r: "MUDROOM" in LAB(MAIN, i))
SCULS = idx(MAIN, lambda i, r: any(k in LAB(MAIN, i) for k in ("SCULLERY", "PANTRY")) and r[6] != "porch")
LAUS = idx(MAIN, lambda i, r: "LAUNDRY" in LAB(MAIN, i))
BEDS = idx(MAIN, lambda i, r: r[6] == "bed")
MBR = first(MAIN, lambda i, r: r[6] == "bed" and "MASTER" in LAB(MAIN, i)) or (first(MAIN, lambda i, r: r[6] == "bed", by_area_desc(MAIN)))
OTHER_BEDS = [i for i in BEDS if i != MBR]
FULL_BATHS = idx(MAIN, lambda i, r: r[6] == "bath" and "BATH" in LAB(MAIN, i) and "POWDER" not in LAB(MAIN, i))
POWDERS = idx(MAIN, lambda i, r: "POWDER" in LAB(MAIN, i))
LIVINGS = idx(MAIN, lambda i, r: r[6] == "living" and r[5] > 0)
STAIRW = first(MAIN, lambda i, r: r[6] == "stairwell")
gar, kit, foy = GAR, KIT, FOY
scull = SCULS[0] if SCULS else None
NFIX_MAIN = len(rows_src(MAIN_FILE, "main_fixtures"))
def nice_bath(n):
    return "hall BATH" if n == "BATH" else n

def thick(L, i, side):
    if L.tag == "main":
        return WALL_T
    return ICF_T if any(k[0] == side for k in L.ext[i]) else WALL_T

def clear_dims(L, i):
    r = L.rooms[i]
    W, D = r[3] - r[1], r[4] - r[2]
    cw = W - (thick(L, i, "W") + thick(L, i, "E")) / 2
    cd = D - (thick(L, i, "N") + thick(L, i, "S")) / 2
    return cw, cd

# ---------------------------------------------------------------- §1 envelope
sec = {}
def table(head, rows):
    s = "| " + " | ".join(head) + " |\n|" + "|".join("---" for _ in head) + "|\n"
    for r in rows:
        s += "| " + " | ".join(str(c) for c in r) + " |\n"
    return s

Hm = [i for i, r in enumerate(MAIN.rooms) if heated_main(r)]
union = unary_union([box(*rect(MAIN.rooms[i])).buffer(0.01, join_style=2) for i in Hm]).buffer(-0.01, join_style=2)
polys = list(union.geoms) if union.geom_type == "MultiPolygon" else [union]
def corners(poly):
    ring = poly.exterior.simplify(0.02)
    pts = list(ring.coords)[:-1]
    sgn = 1 if ring.is_ccw else -1
    cx = rx = 0
    for k in range(len(pts)):
        a, b, c = pts[k - 1], pts[k], pts[(k + 1) % len(pts)]
        cr = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        if cr * sgn > 1e-6: cx += 1
        elif cr * sgn < -1e-6: rx += 1
    return cx, rx, len(pts)
cx, rx, nv = corners(max(polys, key=lambda p: p.area))
holes = sum(len(p.interiors) for p in polys)

kinds_area = defaultdict(float)
heated_sum = sum(area(MAIN.rooms[i]) for i in Hm)
stairwell_area = sum(area(r) for r in MAIN.rooms if r[6] == "stairwell")
def rsum(f, L=MAIN):
    return sum(area(r) for r in L.rooms if f(r))
garage_a = rsum(lambda r: r[6] == "garage")
porch_rows = [(MAIN.names[i], area(r), S("mr", i)) for i, r in enumerate(MAIN.rooms) if r[6] == "porch"]
ext_by_class = defaultdict(float)
for i in Hm:
    for (side, cls), v in MAIN.ext[i].items():
        ext_by_class[cls] += v
bo = model["basement_outline"]
bpoly = Polygon(bo)
bar = [r for r in BASE.rooms if heated_base(r)]
base_sum = sum(area(r) for r in bar)
bcx, brx, bnv = corners(bpoly)
allx = [r[1] for r in MAIN.rooms] + [r[3] for r in MAIN.rooms]
ally = [r[2] for r in MAIN.rooms] + [r[4] for r in MAIN.rooms]
hx = [MAIN.rooms[i][1] for i in Hm] + [MAIN.rooms[i][3] for i in Hm]
hy = [MAIN.rooms[i][2] for i in Hm] + [MAIN.rooms[i][4] for i in Hm]
def _variant_roof():
    tmp = CMP / "_roof.scad"
    tmp.write_text(f"use <{MAIN_FILE}>\necho(main_roof = main_roof());\n")
    r = subprocess.run(["openscad", "-o", "/dev/stdout", "--export-format", "echo", str(tmp)], capture_output=True, text=True)
    m = re.search(r"ECHO: main_roof = (.*)$", r.stdout + r.stderr, re.M)
    tmp.unlink()
    return lit(m.group(1)) if m else model["main_roof"]
roof = _variant_roof() if VARIANT else model["main_roof"]
out["env"] = dict(heated_sum=heated_sum, union_area=union.area, stairwell=stairwell_area, garage=garage_a,
                  perim=union.length, outside_corners=cx, inside_corners=rx, verts=nv, holes=holes,
                  base_sum=base_sum, base_poly=bpoly.area, base_perim=bpoly.length)
s = "### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)\n\n"
s += table(["Item", "sq ft", "Source / formula"], [
    ["Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint)", f"{heated_sum:.1f}", f"computed: sum (x1-x0)*(y1-y0) over {len(Hm)} rows, main_floor.scad:{src['mr'][0][0]}-{src['mr'][-1][0]}"],
    ["  of which STAIR DN stairwell footprint (opening: no floor on this level)", f"{stairwell_area:.1f}", f"{S('mr', [i for i,r in enumerate(MAIN.rooms) if r[6]=='stairwell'][0])}"],
    ["Main-floor conditioned excluding the stair opening", f"{heated_sum - stairwell_area:.1f}", "difference"],
    ["Main-floor heated union polygon (shapely check, should equal row sum)", f"{union.area:.1f}", f"unary_union of heated rects; holes={holes}"],
    ["Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair)", f"{base_sum:.1f}", f"computed over basement.scad:{src['br'][0][0]}-{src['br'][-1][0]}"],
    ["Basement outline polygon (centre lines)", f"{bpoly.area:.1f}", "foundation.scad:40-45 basement_outline(), shoelace"],
    ["Garage (GARAGE row, slab 1.5 ft below house floor)", f"{garage_a:.1f}", S("mr", 0)],
])
s += "\nUnconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):\n\n"
s += table(["Porch / patio / deck row", "sq ft", "Source"], [[n or "(unlabelled porch piece)", f"{a:.1f}", f] for n, a, f in porch_rows])
s += f"\nPorch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): {sum(a for _, a, _ in porch_rows):.1f} sq ft. PATIO alone: {area(MAIN.rooms[[i for i,r in enumerate(MAIN.rooms) if label(r)=='PATIO'][0]]):.1f}; DECK alone: {area(MAIN.rooms[[i for i,r in enumerate(MAIN.rooms) if label(r)=='DECK'][0]]):.1f}. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.\n"
s += "\n### 1.2 Envelope of the heated main floor (centre-line polygon)\n\n"
s += table(["Measure", "Value", "How"], [
    ["Perimeter of heated union, centre line", f"{union.length:.1f} ft", "shapely union of heated rects; this includes walls facing the garage and porches"],
    ["  facing yard/soil", f"{ext_by_class['yard/soil']:.1f} ft", "sum of room edges whose outside point is in no room"],
    ["  facing porch/patio (open)", f"{ext_by_class['porch/patio (open)']:.1f} ft", "same"],
    ["  facing garage", f"{ext_by_class['garage']:.1f} ft", "same (garage is unheated)"],
    ["Outside (convex) corners", cx, f"vertices of the union polygon after 0.02 ft simplify ({nv} vertices)"],
    ["Inside (reflex) corners", rx, "same polygon"],
    ["Bounding box, heated rooms", f"x {min(hx):g}..{max(hx):g} ({max(hx)-min(hx):g} ft), y {min(hy):g}..{max(hy):g} ({max(hy)-min(hy):g} ft)", "min/max of heated room rects"],
    ["Bounding box, everything on the main floor incl. garage, porches, deck", f"x {min(allx):g}..{max(allx):g} ({max(allx)-min(allx):g} ft), y {min(ally):g}..{max(ally):g} ({max(ally)-min(ally):g} ft)", "all main_rooms rows"],
    ["Basement outline", f"x {min(p[0] for p in bo):g}..{max(p[0] for p in bo):g}, y {min(p[1] for p in bo):g}..{max(p[1] for p in bo):g}; perimeter {bpoly.length:.1f} ft; {bcx} outside / {brx} inside corners ({bnv} vertices)", "foundation.scad:40-45"],
    ["Roof", f"{len(roof)} hip-roof blocks in main_roof (main_floor.scad:{(grep(MAIN_FILE, 'function main_roof') or [0])[0]}); each hip block is 4 sloped facets, so 4 x {len(roof)} = {4*len(roof)} nominal facets before overlapping blocks merge; {sum(1 for b in roof if b[5]==0.5)} blocks at 6/12 pitch, {sum(1 for b in roof if b[5]!=0.5)} porch blocks at 4/12", "house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model"],
])
s += "\n(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)\n"
sec[1] = s

# ---------------------------------------------------------------- §2 orientation + exterior sides
def ext_str(L, i):
    e = L.ext[i]
    parts = []
    for side in "NSEW":
        t = {c: v for (sd, c), v in e.items() if sd == side}
        if t:
            parts.append(f"{side} " + ", ".join(f"{v:.1f} ({c})" for c, v in sorted(t.items())))
    return "; ".join(parts) if parts else "none"
s = "### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)\n\n"
s += "Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.\n\n"
s += table(["Room", "Exterior sides touched (length ft)", "Source"], [[MAIN.names[i], ext_str(MAIN, i), S("mr", i)] for i in Hm])
sec[2] = s

# ---------------------------------------------------------------- §3 room tables
def room_table(L, subset=None):
    rows = []
    for i, r in enumerate(L.rooms):
        if subset and not subset(r):
            continue
        W, D = r[3] - r[1], r[4] - r[2]
        cw, cd = clear_dims(L, i)
        rows.append([L.names[i], r[1], r[2], r[3], r[4], f"{W:.2f} x {D:.2f}", f"{cw:.1f} x {cd:.1f}" if r[5] > 0 or r[6] in ("hall", "stairwell") else f"{W:.1f} x {D:.1f} (open)",
                     f"{W*D:.0f}", f"{cw*cd:.0f}" if r[5] > 0 or r[6] in ("hall",) else "-", f"{max(W,D)/min(W,D):.2f}", r[6], r[5], S(L.rk, i)])
    return table(["Room", "x0", "y0", "x1", "y1", "W x D (c/l)", "approx clear", "area c/l sf", "area clear sf", "long:short", "kind", "ceil", "source"], rows)
s = "Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.\n\n"
s += "### 3.1 Main floor (heated rooms, then unconditioned rows)\n\n" + room_table(MAIN, heated_main)
s += "\n#### Garage and porches (not conditioned)\n\n" + room_table(MAIN, lambda r: not heated_main(r))
s += "\n### 3.2 Basement\n\n" + room_table(BASE)
sec[3] = s

# ---------------------------------------------------------------- §4 doors
def door_rows(L):
    rows = []
    for i, d in enumerate(L.doors):
        a, b = door_sides(L, d)
        rows.append(dict(i=i, x=d[0], y=d[1], axis=d[2], w=d[3], type=d[4], swing=(d[5] if len(d) > 5 else None),
                         a=L.names[a] if a is not None else "OUTSIDE", b=L.names[b] if b is not None else "OUTSIDE",
                         ai=a, bi=b, src=S(L.dk, i), mid=door_mid(d)))
    return rows
MD, BD = door_rows(MAIN), door_rows(BASE)
def dtable(rows, pre):
    out_ = []
    for k, r in enumerate(rows):
        out_.append([f"{pre}{k+1}", f"({r['x']:g}, {r['y']:g}) {r['axis']}", f"{r['w']:g} ft = {inch(r['w']):g} in", r["type"], r["swing"] if r["swing"] is not None else "-",
                     f"{r['a']} / {r['b']}", r["src"]])
    return table(["#", "pos (x,y) axis", "opening width", "type", "swing", "joins (low-side room / high-side room)", "source"], out_)
def bucket(w):
    i = w * 12
    return "<32" if i < 31.995 else ("32-35" if i < 35.995 else ">=36")
def stats(rows):
    t = defaultdict(lambda: defaultdict(int))
    for r in rows:
        t[r["type"]][bucket(r["w"])] += 1
        t["ALL"][bucket(r["w"])] += 1
    pas = [r for r in rows if r["type"] in ("door", "double", "slider", "open")]
    for r in pas:
        t["passage (door+double+slider+open)"][bucket(r["w"])] += 1
    return t
def stat_table(L, rows):
    t = stats(rows)
    keys = ["door", "double", "open", "full", "slider", "glass", "garage", "ALL", "passage (door+double+slider+open)"]
    return table(["type", "<32 in", "32-35 in", ">=36 in", "total"], [[k, t[k]["<32"], t[k]["32-35"], t[k][">=36"], sum(t[k].values())] for k in keys if k in t])
KIND_OF = lambda L, i: None if i is None else L.rooms[i][6]
def bbw(L, rows):
    res = []
    for k, r in enumerate(rows):
        ks = [KIND_OF(L, r["ai"]), KIND_OF(L, r["bi"])]
        if any(x in ("bed", "bath", "closet") for x in ks):
            res.append([r["src"], f"{r['a']} / {r['b']}", r["type"], f"{inch(r['w']):g} in", f"{inch(r['w'] - 0.125) if r['type']=='door' else '-'}"])
    return table(["source", "joins", "type", "opening width", "approx clear (door: opening - 1.5 in)"], res)
s = "Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).\n\n"
s += "### 4.1 Main floor schedule\n\n" + dtable(MD, "M") + "\n### 4.2 Basement schedule\n\n" + dtable(BD, "B")
s += "\n### 4.3 Width statistics\n\nMain floor:\n\n" + stat_table(MAIN, MD) + "\nBasement:\n\n" + stat_table(BASE, BD)
s += "\n### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)\n\nMain:\n\n" + bbw(MAIN, MD) + "\nBasement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):\n\n" + bbw(BASE, BD)
sec[4] = s
out["doors_main"] = [{k: v for k, v in r.items() if k not in ("ai", "bi")} for r in MD]

# ---------------------------------------------------------------- §5 windows
def win_rows(L):
    rows = []
    for i, w in enumerate(L.wins):
        x, y, ax, wd = w[:4]
        a, b = door_sides(L, w)
        ca = a is not None and L.rooms[a][5] > 0 and L.rooms[a][6] != "porch"
        cb = b is not None and L.rooms[b][5] > 0 and L.rooms[b][6] != "porch"
        if ax == "x":    # horizontal wall: low side = south
            room, fac = (a, "N") if (ca and not cb) else (b, "S")
        else:
            room, fac = (a, "E") if (ca and not cb) else (b, "W")
        rows.append(dict(room=L.names[room] if room is not None else "?", ri=room, fac=fac, w=wd, sill=w[4], h=w[5], src=S(L.wk, i), pos=(x, y, ax)))
    return rows
MW, BW = win_rows(MAIN), win_rows(BASE)
def wtable(rows):
    return table(["room", "facade", "pos (x,y,axis)", "width ft", "sill ft", "height ft", "glass sf", "source"],
                 [[r["room"], r["fac"], r["pos"], r["w"], r["sill"], r["h"], f"{r['w']*r['h']:.1f}", r["src"]] for r in rows])
def multi_and_none(L, rows, heated):
    byroom = defaultdict(set)
    for r in rows:
        byroom[r["ri"]].add(r["fac"])
    multi = [(L.names[i], sorted(f)) for i, f in byroom.items() if len(f) >= 2]
    none = [(L.names[i], L.rooms[i][6], round(area(L.rooms[i]))) for i in range(len(L.rooms)) if heated(L.rooms[i]) and L.rooms[i][5] >= 0 and i not in byroom and L.rooms[i][6] not in ("stairwell",)]
    return multi, none
mm, mn = multi_and_none(MAIN, MW, heated_main)
bm, bn = multi_and_none(BASE, BW, heated_base)
glass_tot = sum(r["w"] * r["h"] for r in MW)
s = "Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).\n\n### 5.1 Main floor\n\n" + wtable(MW)
s += f"\nTotal main-floor window glass (width x height): {glass_tot:.1f} sq ft ({len(MW)} windows; sliders/French doors/glass doors in main_doors are not included).\n"
s += "\nFacade counts: " + ", ".join(f"{f}: {sum(1 for r in MW if r['fac']==f)}" for f in "NSEW") + "\n"
s += "\nRooms with windows on 2+ walls (main): " + ("; ".join(f"{n} ({'/'.join(f)})" for n, f in mm) or "none") + "\n"
s += "\nHeated main-floor rooms with NO window row (all kinds; baths, closets and halls included): \n\n" + table(["room", "kind", "area sf"], [list(x) for x in mn])
s += "\n### 5.2 Basement\n\n" + wtable(BW) + "\nRooms with windows on 2+ walls (basement): " + ("; ".join(f"{n}" for n, f in bm) or "none") + "\n\nBasement rooms with no window row: " + "; ".join(f"{n} ({k}, {a} sf)" for n, k, a in bn) + "\n"
sec[5] = s
out["win_main"] = MW

# ---------------------------------------------------------------- §6 circulation
def circ(L, heated):
    idx = [i for i, r in enumerate(L.rooms) if heated(r)]
    base = sum(area(L.rooms[i]) for i in idx)
    circ_i = [i for i in idx if L.rooms[i][6] == "hall" and "FOYER" not in L.names[i] and "VESTIBULE" not in L.names[i]]
    return base, circ_i
mb, mc = circ(MAIN, heated_main)
bb_, bc = circ(BASE, heated_base)
def circ_table(L, ids):
    rows = []
    for i in ids:
        cw, cd = clear_dims(L, i)
        rows.append([L.names[i], f"{L.rooms[i][1]:g},{L.rooms[i][2]:g} to {L.rooms[i][3]:g},{L.rooms[i][4]:g}", f"{area(L.rooms[i]):.0f}", f"{min(cw, cd):.1f} ft clear width ({min(cw,cd)*12:.0f} in), length {max(cw,cd):.1f}", S(L.rk, i)])
    return table(["Circulation room", "rect", "area c/l sf", "clear width, length", "source"], rows)
mc_a = sum(area(MAIN.rooms[i]) for i in mc)
bc_a = sum(area(BASE.rooms[i]) for i in bc)
foyer_i = FOY
mud_i = MUD
stair_main = STAIRW
stair_base = [i for i, r in enumerate(BASE.rooms) if r[6] == "stair"][0]
den_a = mb - 0  # denominators
s = "**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).\n\n"
s += "### 6.1 Main floor\n\n" + circ_table(MAIN, mc)
s += f"\n**Circulation total (halls only): {mc_a:.0f} sq ft = {100*mc_a/mb:.1f}% of {mb:.0f} sq ft conditioned** ({100*mc_a/(mb-stairwell_area):.1f}% if the stair opening is excluded from the denominator).\n\n"
_fa = area(MAIN.rooms[foyer_i]) if foyer_i is not None else 0.0
_ma = area(MAIN.rooms[mud_i]) if mud_i is not None else 0.0
_rows = []
if foyer_i is not None:
    _rows.append(["FOYER", f"{_fa:.0f}", f"{min(clear_dims(MAIN, foyer_i)):.1f} ft", f"{100*(mc_a+_fa)/mb:.1f}%", S("mr", foyer_i)])
if mud_i is not None:
    _rows.append(["MUDROOM", f"{_ma:.0f}", f"{min(clear_dims(MAIN, mud_i)):.1f} ft", f"{100*(mc_a+_fa+_ma)/mb:.1f}% (halls+foyer+mudroom)", S("mr", mud_i)])
if stair_main is not None:
    _rows.append(["STAIR DN opening (stairwell)", f"{stairwell_area:.0f}", f"{min(clear_dims(MAIN, stair_main)):.1f} ft", f"{100*(mc_a+_fa+_ma+stairwell_area)/mb:.1f}% (all four)", S("mr", stair_main)])
s += table(["Separate lines (not in total)", "area c/l sf", "clear width", "% of conditioned if added", "source"], _rows)
s += "\n### 6.2 Basement\n\n" + circ_table(BASE, bc)
s += f"\n**Circulation total (halls only): {bc_a:.0f} sq ft = {100*bc_a/bb_:.1f}% of {bb_:.0f} sq ft** (rooms sum, excl. EXIT STAIR areaway).\n\n"
s += table(["Separate line (not in total)", "area c/l sf", "clear width", "% if added", "source"], [
    ["STAIR UP (stair flight room, y 28.725..45.34)", f"{area(BASE.rooms[stair_base]):.0f}", f"{min(clear_dims(BASE, stair_base)):.1f} ft", f"{100*(bc_a+area(BASE.rooms[stair_base]))/bb_:.1f}%", S("br", stair_base)]])
s += "\nNote: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.\n"
sec[6] = s
out["circ"] = dict(main_total=mc_a, main_pct=100 * mc_a / mb, base_total=bc_a, base_pct=100 * bc_a / bb_)

# ---------------------------------------------------------------- §7 graph + paths
def build_graph(L):
    """nodes: ('d',k) door midpoints, ('c',j) connectors between abutting ceiling-0 non-porch zones."""
    pts, rooms_of = {}, {}
    for k, d in enumerate(L.drows):
        pts[("d", k)] = d["mid"]
        rooms_of[("d", k)] = [x for x in (d["ai"], d["bi"]) if x is not None]
    j = 0
    zero = [i for i, r in enumerate(L.rooms) if r[5] == 0 and r[6] != "porch"] + [i for i, r in enumerate(L.rooms) if r[5] == 0 and r[6] == "porch"]
    conns = []
    for a in range(len(zero)):
        for b in range(a + 1, len(zero)):
            A, B = L.rooms[zero[a]], L.rooms[zero[b]]
            if (A[6] == "porch") != (B[6] == "porch"):
                continue
            ov = None
            if abs(A[3] - B[1]) < 0.05 or abs(B[3] - A[1]) < 0.05:
                lo, hi = max(A[2], B[2]), min(A[4], B[4])
                if hi - lo > 0.5:
                    xx = A[3] if abs(A[3] - B[1]) < 0.05 else A[1]
                    ov = (xx, (lo + hi) / 2, hi - lo)
            if ov is None and (abs(A[4] - B[2]) < 0.05 or abs(B[4] - A[2]) < 0.05):
                lo, hi = max(A[1], B[1]), min(A[3], B[3])
                if hi - lo > 0.5:
                    yy = A[4] if abs(A[4] - B[2]) < 0.05 else A[2]
                    ov = ((lo + hi) / 2, yy, hi - lo)
            if ov:
                pts[("c", j)] = (ov[0], ov[1]); rooms_of[("c", j)] = [zero[a], zero[b]]
                conns.append((j, zero[a], zero[b], ov[2])); j += 1
    L.pts, L.rooms_of, L.conns = pts, rooms_of, conns
MAIN.drows, BASE.drows = MD, BD
build_graph(MAIN); build_graph(BASE)

def adjacency(L):
    adj = defaultdict(set)
    for n, rs in L.rooms_of.items():
        if len(rs) == 2:
            adj[rs[0]].add(rs[1]); adj[rs[1]].add(rs[0])
    return adj

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

def route(L, p0, r0, p1, r1, allow=()):
    """shortest walking route (Euclid between door midpoints) from point p0 in room r0 to p1 in room r1.
    state = (node, room we are in after passing the node)."""
    if r0 == r1:
        return dist(p0, p1), [r0], [p0, p1]
    adj_nodes = defaultdict(list)
    for n, rs in L.rooms_of.items():
        for r in rs:
            adj_nodes[r].append(n)
    def ok(r):
        return L.rooms[r][6] != "porch" or r in (r0, r1) or r in allow
    start = (("S", 0), r0)
    dd = {start: 0}; prev = {}; pq = [(0, 0, start)]
    cnt = 1; best = None
    pts = dict(L.pts); pts[("S", 0)] = p0
    done = set()
    while pq:
        c, _, st_ = heapq.heappop(pq)
        if st_ in done: continue
        done.add(st_)
        n, r = st_
        if r == r1:
            tot = c + dist(pts[n], p1)
            if best is None or tot < best[0]:
                best = (tot, st_)
        if best and c >= best[0]: break
        for m in adj_nodes[r]:
            if m == n: continue
            for ra in L.rooms_of[m]:
                if ra == r or not ok(ra): continue
                ns = (m, ra)
                nc = c + dist(pts[n], pts[m])
                if nc < dd.get(ns, 1e18):
                    dd[ns] = nc; prev[ns] = st_; cnt += 1; heapq.heappush(pq, (nc, cnt, ns))
    if best is None:
        return None, [], []
    seq, pp, st_ = [r1], [p1], best[1]
    while True:
        n, r = st_
        pp.append(pts[n]); seq.append(r)
        if n == ("S", 0): break
        st_ = prev[st_]
    # seq currently r1, r_after_lastdoor(=r1), ...; rebuild readable chain of rooms
    pp = pp[::-1]
    chain = []
    st_ = best[1]
    while True:
        chain.append(st_[1])
        if st_ == start: break
        st_ = prev[st_]
    return best[0], chain[::-1], pp

def rid(L, name):
    c = [i for i, n in enumerate(L.names) if n == name or n.startswith(name + " @")]
    return c

def centroid(L, i):
    r = L.rooms[i]
    return ((r[1] + r[3]) / 2, (r[2] + r[4]) / 2)

def seqnames(L, seq):
    out_ = []
    for r in seq:
        if not out_ or out_[-1] != L.names[r]:
            out_.append(L.names[r])
    return " > ".join(out_)

adjM, adjB = adjacency(MAIN), adjacency(BASE)
def adj_table(L, adj):
    rows = []
    for i in range(len(L.rooms)):
        nb = sorted(L.names[j] for j in adj[i])
        ext_doors = [d for d in L.drows if (d["ai"] == i and d["bi"] is None) or (d["bi"] == i and d["ai"] is None)]
        ex = ", ".join(f"{d['type']} to outside ({d['src']})" for d in ext_doors)
        rows.append([L.names[i], L.rooms[i][6] + (", ceiling 0 (open zone)" if L.rooms[i][5] == 0 else ""), "; ".join(nb) or "-", ex or "-"])
    return table(["Room", "kind", "rooms reachable through one door/opening", "exterior doors"], rows)
conn_txt = lambda L: "; ".join(f"{L.names[a]} <-> {L.names[b]} ({ln:.1f} ft shared edge)" for j, a, b, ln in L.conns) or "none"

def find1(L, key):
    c = [i for i, n in enumerate(L.names) if n == key]
    if not c:
        c = [i for i, n in enumerate(L.names) if key in n]
    assert c, key
    return c[0]
def door_by_xy(rows, x, y):
    return [r for r in rows if abs(r["x"] - x) < 1e-6 and abs(r["y"] - y) < 1e-6][0]

paths = []
def add_path(L, title, p0, r0, p1, r1, note=""):
    d, seq, pp = route(L, p0, r0, p1, r1)
    paths.append(dict(title=title, len=d, seq=seq, pts=pp, L=L.tag, note=note))
    return d, seq
COLOURS = {"wood": (0.55, 0.38, 0.22), "dark": (0.12, 0.12, 0.12), "basin": (0.62, 0.78, 0.86), "tile": (0.55, 0.75, 0.85),
           "white": (0.97, 0.97, 0.97), "counter": (0.97, 0.97, 0.95), "steel": (0.70, 0.72, 0.74), "shelf": (0.62, 0.50, 0.36),
           "sofa": (0.45, 0.50, 0.60), "bed": (0.92, 0.88, 0.80), "table": (0.66, 0.50, 0.34), "hearth": (0.35, 0.33, 0.32)}
def cname(c):
    for k, v in COLOURS.items():
        if all(abs(c[n] - v[n]) < 0.006 for n in range(3)):
            return k
    return "?"
def fix_room(L, f):
    return room_of(L, (f[0] + f[2]) / 2, (f[1] + f[3]) / 2)
def fixc(f):
    return ((f[0] + f[2]) / 2, (f[1] + f[3]) / 2)
# master suite: bath / closet / small hall rooms reached through doors from the master bedroom
def suite_rooms():
    seen, todo = {MBR}, [MBR]
    while todo:
        i = todo.pop()
        for j in adjM[i]:
            r = MAIN.rooms[j]
            if j in seen or r[6] == "porch": continue
            if r[6] in ("bath", "closet") or (r[6] == "hall" and area(r) <= 100):
                seen.add(j); todo.append(j)
    return seen
SUITE = suite_rooms() if MBR is not None else set()
fd = None
if FOY is not None:
    cand = [d for d in MD if d["type"] in ("double", "door") and {d["ai"], d["bi"]} - {FOY} and FOY in (d["ai"], d["bi"])
            and any(MAIN.rooms[x][6] == "porch" for x in (d["ai"], d["bi"]) if x is not None)]
    fd = max(cand, key=lambda d: d["w"]) if cand else None
gdc = [d for d in MD if GAR in (d["ai"], d["bi"]) and d["type"] != "garage" and any(MAIN.rooms[x][6] == "hall" for x in (d["ai"], d["bi"]) if x is not None and x != GAR)]
gd = gdc[0] if gdc else None
gd_room = [x for x in (gd["ai"], gd["bi"]) if x != GAR][0] if gd else None
range_k = next((k for k, f in enumerate(MAIN.fix) if cname(f[6]) == "dark" and abs(f[4] - 3) < 0.01 and KIT is not None and fix_room(MAIN, f) == KIT), None)
pantry_k = next((k for k, f in enumerate(MAIN.fix) if cname(f[6]) == "wood" and abs(f[5] - 7) < 0.01 and KIT is not None and fix_room(MAIN, f) == KIT), None)
mwic = [i for i in sorted(SUITE) if MAIN.rooms[i][6] == "closet" and "WIC" in LAB(MAIN, i)]
paths = []
def add_path(L, title, p0, r0, p1, r1, note=""):
    d, seq, pp = route(L, p0, r0, p1, r1)
    paths.append(dict(title=title, len=d, seq=seq, pts=pp, L=L.tag, note=note))
    return d, seq
if fd is not None and KIT is not None:
    add_path(MAIN, "front door -> kitchen/dining room centre", fd["mid"], FOY, centroid(MAIN, KIT), KIT)
    if range_k is not None:
        add_path(MAIN, f"front door -> range ({S('mf', range_k)})", fd["mid"], FOY, fixc(MAIN.fix[range_k]), KIT)
if GAR is not None and KIT is not None:
    add_path(MAIN, "garage (room centre) -> kitchen/dining room centre", centroid(MAIN, GAR), GAR, centroid(MAIN, KIT), KIT)
    if range_k is not None:
        add_path(MAIN, "garage (room centre) -> range", centroid(MAIN, GAR), GAR, fixc(MAIN.fix[range_k]), KIT)
if GAR is not None:
    _np = "" if any("PANTRY" in LAB(MAIN, i) for i in SCULS) else " (no pantry room in model)"
    for sc in SCULS:
        add_path(MAIN, f"garage (room centre) -> {MAIN.names[sc]} centre{_np}", centroid(MAIN, GAR), GAR, centroid(MAIN, sc), sc)
    if pantry_k is not None and KIT is not None:
        add_path(MAIN, f"garage (room centre) -> tall pantry cabinets in kitchen ({S('mf', pantry_k)})", centroid(MAIN, GAR), GAR, fixc(MAIN.fix[pantry_k]), KIT)
if MBR is not None:
    for w in mwic:
        add_path(MAIN, f"master bedroom centre -> {MAIN.names[w]} centre", centroid(MAIN, MBR), MBR, centroid(MAIN, w), w)
    for lau in LAUS:
        add_path(MAIN, f"master bedroom centre -> {MAIN.names[lau]} centre", centroid(MAIN, MBR), MBR, centroid(MAIN, lau), lau)
for bi in OTHER_BEDS:
    bn = MAIN.names[bi]
    for v in FULL_BATHS:
        add_path(MAIN, f"{bn} centre -> {nice_bath(MAIN.names[v])} centre", centroid(MAIN, bi), bi, centroid(MAIN, v), v)
    for lau in LAUS:
        add_path(MAIN, f"{bn} centre -> {MAIN.names[lau]} centre", centroid(MAIN, bi), bi, centroid(MAIN, lau), lau)
if FOY is not None:
    if POWDERS:
        for pw in POWDERS:
            add_path(MAIN, f"foyer centre -> {MAIN.names[pw]} centre (powder room)", centroid(MAIN, FOY), FOY, centroid(MAIN, pw), pw)
    else:
        _c = [(route(MAIN, centroid(MAIN, FOY), FOY, centroid(MAIN, v), v)[0], v) for v in FULL_BATHS]
        _c = [x for x in _c if x[0] is not None]
        if _c:
            _v = min(_c)[1]
            add_path(MAIN, f"foyer centre -> {nice_bath(MAIN.names[_v])} centre (no powder room in model; nearest toilet room reachable from the foyer side)", centroid(MAIN, FOY), FOY, centroid(MAIN, _v), _v)
top_pt = None; landing = None
if STAIRW is not None:
    _sr = MAIN.rooms[STAIRW]
    top_pt = ((_sr[1] + _sr[3]) / 2, _sr[4])
    landing = room_of(MAIN, top_pt[0], top_pt[1] + 0.5)
    if landing is None: landing = STAIRW
    _orig = {}
    if fd is not None: _orig["front door"] = (fd["mid"], FOY)
    if gd is not None: _orig["garage mud-entry door"] = (gd["mid"], gd_room)
    if MBR is not None: _orig["master bedroom centre"] = (centroid(MAIN, MBR), MBR)
    for bi in (OTHER_BEDS if VARIANT else OTHER_BEDS[:1]):
        _orig[f"{MAIN.names[bi]} centre"] = (centroid(MAIN, bi), bi)
    for nm, (p, r) in _orig.items():
        add_path(MAIN, f"{nm} -> top of main stair (top nosing, ({top_pt[0]:.2f}, {top_pt[1]:g}))", p, r, top_pt, landing)
stair_base_ = first(BASE, lambda i, r: r[6] == "stair")
util = first(BASE, lambda i, r: "UTILITY" in LAB(BASE, i))
foot_pt = None
if stair_base_ is not None and util is not None:
    _br = BASE.rooms[stair_base_]
    foot_pt = ((_br[1] + _br[3]) / 2, _br[2])
    hallway = room_of(BASE, foot_pt[0], foot_pt[1] - 0.3)
    if hallway is not None:
        add_path(BASE, f"basement stair foot ({foot_pt[0]:.2f}, {foot_pt[1]:g}) -> {BASE.names[util]} centre", foot_pt, hallway, centroid(BASE, util), util)
# stair bridge: top nosing -> foot is the stair itself
stair_len = math.hypot(0, model["stair"]["top_y"] - model["stair"]["foot_y"])
def ptable():
    rows = []
    for p in paths:
        L = MAIN if p["L"] == "main" else BASE
        rows.append([p["title"], f"{p['len']:.1f}" if p["len"] is not None else "no route", seqnames(L, p["seq"]) or "same room"])
    return table(["Path", "walk ft", "room sequence (innermost room each side of each door crossed)"], rows)
s = "Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.\n\n"
s += "Virtual connectors (open-zone abutments, main): " + conn_txt(MAIN) + "\n\nBasement: " + conn_txt(BASE) + "\n\n"
s += "### 7.1 Main-floor adjacency\n\n" + adj_table(MAIN, adjM) + "\n### 7.2 Basement adjacency\n\n" + adj_table(BASE, adjB)
s += "\n### 7.3 Daily paths\n\n**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.\n\n"
s += ptable()
s += f"\nMain stair flight itself: {stair_len:.2f} ft of plan run between top nosing y={model['stair']['top_y']} and foot y={model['stair']['foot_y']:.3f} (model.json stair).\n"
mbr_wic = [p for p in paths if p["title"].startswith("master bedroom centre -> WIC")]
s += "\nMaster bed to WIC passes through the master bath? " + "; ".join(f"{p['title'].split('-> ')[1]}: {'YES' if any('MASTER BATH' in MAIN.names[r] for r in p['seq']) else 'no'} (via {seqnames(MAIN, p['seq'])})" for p in mbr_wic) + "\n"
sec[7] = s
out["paths"] = [dict(title=p["title"], len=p["len"], seq=[(MAIN if p["L"] == "main" else BASE).names[r] for r in p["seq"]]) for p in paths]

# ---------------------------------------------------------------- §8 adjacency facts
def shared_edges(L, i, j):
    A, B = L.rooms[i], L.rooms[j]
    out_ = 0.0
    for (a0, a1, b0, b1) in ((A[3], A[1], B[1], B[3]),):
        pass
    res = []
    if abs(A[3] - B[1]) < 0.05 or abs(A[1] - B[3]) < 0.05:
        ov = min(A[4], B[4]) - max(A[2], B[2])
        if ov > 0.05: res.append(("vertical wall", ov))
    if abs(A[4] - B[2]) < 0.05 or abs(A[2] - B[4]) < 0.05:
        ov = min(A[3], B[3]) - max(A[1], B[1])
        if ov > 0.05: res.append(("horizontal wall", ov))
    return res
def neigh(L, i):
    rows = []
    for j in range(len(L.rooms)):
        if j == i: continue
        for kind, ln in shared_edges(L, i, j):
            doors = [d for d in L.drows if {d["ai"], d["bi"]} == {i, j}]
            rows.append([L.names[j], L.rooms[j][6] + (" (ceil 0)" if L.rooms[j][5] == 0 else ""), f"{ln:.1f}", ", ".join(f"{d['type']} {inch(d['w']):g} in" for d in doors) or "-"])
    return table(["shares a wall with", "kind", "shared length ft", "door/opening between"], rows)
s = ""
_liv = sorted([i for i in LIVINGS if label(MAIN.rooms[i])], key=lambda i: -area(MAIN.rooms[i]))
for i in _liv:
    nm = MAIN.names[i]
    s += f"### 8.1 {nm} (main; {S('mr', i)}) shares walls with\n\n" + neigh(MAIN, i) + "\n"
s += "The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are " + ", ".join(MAIN.names[i] for i in _liv) + ". Basement LIVING ROOM:\n\n" + neigh(BASE, first(BASE, lambda i, r: r[6] == "living" and "LIVING" in LAB(BASE, i))) + "\n"
if foy is not None:
    s += f"### 8.2 FOYER ({S('mr', foy)}) shares walls with\n\n" + neigh(MAIN, foy) + "\n"
else:
    s += "### 8.2 No foyer/vestibule row (label FOYER or VESTIBULE) in this variant\n\n"
def closet_like(L, i):
    r = L.rooms[i]; n = L.names[i]
    return r[6] == "closet" or "SCULLERY" in n or "PANTRY" in n or "STORAGE" in n
if not any("PANTRY" in LAB(MAIN, i) for i in SCULS) and pantry_k is not None:
    s += f"### 8.3 Closets, WICs, linen, scullery, storage: exterior exposure\n\nNo room is labelled PANTRY in the model. SCULLERY (kind utility) and the 'tall pantry cabinets' fixture row ({S('mf', pantry_k)}, inside {MAIN.names[KIT].replace(' / ', '/')}) are the pantry-like items.\n\n"
else:
    s += "### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure\n\nPantry-like rooms: " + (", ".join(MAIN.names[i] for i in SCULS) or "none (no SCULLERY/PANTRY label)") + ".\n\n"
rows = []
for L in (MAIN, BASE):
    for i in range(len(L.rooms)):
        if closet_like(L, i):
            ex = [(k, v) for k, v in L.ext[i].items() if True]
            rows.append([L.tag, L.names[i], S(L.rk, i), ext_str(L, i)])
s += table(["level", "room", "source", "sides touching outside/porch/garage/soil (ft)"], rows)
_pg = ""
for sc in SCULS:
    sc_garage = shared_edges(MAIN, sc, gar) if gar is not None else []
    gdoors = [d for d in MD if {d["ai"], d["bi"]} == {sc, gar}]
    _nm = MAIN.names[sc]
    _pg += f"\nPantry/garage: {_nm} shares {sum(l for _,l in sc_garage):.1f} ft of wall with the garage; doors between {_nm} and GARAGE: {len(gdoors)}. The garage's doors to the house are: " + "; ".join(f"{d['src']} ({d['a']} | {d['b']}, {inch(d['w']):g} in)" for d in MD if gar in (d['ai'], d['bi']) and d['type'] != 'garage') + "."
if pantry_k is not None and gar is not None:
    _pf = MAIN.fix[pantry_k]; _gr = MAIN.rooms[gar]
    if _pf[0] >= _gr[3] + 0.5:
        _pg += f" The tall pantry cabinets (x {_pf[0]:g}-{_pf[2]:g}) are {_pf[0]-_gr[3]:.1f} ft east of the garage wall (x {_gr[3]:g}): no shared wall."
    else:
        _pg += f" The tall pantry cabinets (x {_pf[0]:g}-{_pf[2]:g}) are {box(*_pf[:4]).distance(box(*rect(_gr))):.1f} ft from the garage rectangle."
s += _pg + "\n"
# kitchen fixtures on paths
KW = re.compile(r"range|sink|dishwash|island|fridge|washer|dryer|prep", re.I)
kfix = defaultdict(list)
for k, f in enumerate(MAIN.fix):
    c = src["mf"][k][1]
    rr = room_of(MAIN, (f[0] + f[2]) / 2, (f[1] + f[3]) / 2)
    if rr is not None and KW.search(c) and k < NFIX_MAIN:
        kfix[rr].append(f"{c} ({src['mf'][k][0]})")
extra = {"range": "main_floor.scad:198", "double island (counter row, no label 'island' in comment except line 203)": "main_floor.scad:203"}
s += "\n### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them\n\n"
rows = []
for rr, lst in kfix.items():
    on = [p["title"] for p in paths if p["L"] == "main" and rr in p["seq"]]
    rows.append([MAIN.names[rr], "; ".join(lst), "; ".join(on) or "none of the §7 paths"])
s += table(["room", "fixtures (source line)", "§7 paths passing through (as a room walked through or ending in)"], rows)
s += "\nNo dishwasher row exists in main_fixtures (not in model).\n"
# driveway proximity
drive_rects = {"west driveway (site.scad:111)": box(-32, -100, -2, 42), "front loop south leg (:113)": box(25, -72, 130, -58), "loop north leg (:114)": box(25, -28, 130, -14),
               "loop west leg (:115)": box(25, -72, 39, -14), "loop east leg (:116)": box(116, -72, 130, -14), "connector (:117)": box(-2, -50, 25, -36)}
drive_union = unary_union(list(drive_rects.values()))
rows = []
for i in Hm + ([gar] if gar is not None else []):
    r = box(*rect(MAIN.rooms[i]))
    d = r.distance(drive_union)
    if d < 40:
        near = min(drive_rects.items(), key=lambda kv: r.distance(kv[1]))
        rows.append([MAIN.names[i], f"{d:.1f}", near[0], ext_str(MAIN, i)])
rows.sort(key=lambda x: float(x[1]))
s += "\n### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)\n\n" + table(["room", "distance ft", "nearest drive piece", "exterior sides"], rows)
if not VARIANT:
    s += f"\nOther rooms are > 40 ft from any drive. Garage doors face west (axis y, x=0: main_floor.scad:117-118) onto the west driveway; the drive's east edge is x=-2, i.e. 2.0 ft off the garage's west wall.\n"
else:
    _gd = [(k, d) for k, d in enumerate(MAIN.doors) if d[4] == "garage"]
    _gr = MAIN.rooms[gar]
    def _fac(d):
        return ("W" if d[0] <= _gr[1] + 0.1 else "E") if d[2] == "y" else ("S" if d[1] <= _gr[2] + 0.1 else "N")
    s += "\nOther rooms are > 40 ft from any drive. Garage doors (rows " + ", ".join(S("md", k) for k, d in _gd) + ") face " + ", ".join(sorted({_fac(d) for k, d in _gd})) + f"; garage rectangle to the nearest drive piece: {box(*rect(_gr)).distance(drive_union):.1f} ft.\n"
sec[8] = s

# ---------------------------------------------------------------- §9 plumbing
WETDEF = {
    "main": [("kitchen sink", (39.93, 6.68, 42.57, 8.26)), ("prep sink (island)", (43.22, 16.68, 44.87, 18.65)),
             ("scullery sink", (28.09, 27.34, 31.71, 28.91)), ("washer + dryer", (28.09, 47.07, 34.01, 49.05)), ("laundry sink", (33.22, 41.02, 35.1, 43.52)),
             ("Bath 2 tub", (7.7, 55.55, 10.33, 61.41)), ("Bath 2 double vanity", (10.99, 60.1, 17.3, 61.68)), ("Bath 2 suite WC", (8.03, 51.55, 10.33, 53.85)),
             ("hall bath vanity", (51.78, 42.34, 53.42, 44.31)), ("hall bath toilet", (51.12, 39.7, 53.09, 41.35)), ("hall bath shower", (47.83, 35.89, 53.42, 38.39)),
             ("master double vanity", (111.64, 17.86, 121.51, 19.64)), ("master shower", (111.97, 9.55, 120.2, 14.05)), ("master tub", (123.16, 9.55, 127.63, 15.03)),
             ("master WC (north)", (100.79, 17.01, 103.42, 19.31)), ("master WC (south)", (100.79, 9.77, 103.42, 12.07))],
    "base": [("bath-by-stair WC", (52.0, 41.5, 53.8, 43.3)), ("bath-by-stair vanity", (52.1, 38.5, 53.9, 41.0)), ("bath-by-stair shower", (47.6, 42.0, 50.6, 45.0)),
             ("pool bath WC", (100.6, 22.5, 102.4, 24.3)), ("pool bath vanity", (96.6, 25.5, 98.6, 28.8)), ("pool bath shower", (99.2, 25.4, 102.45, 28.9)),
             ("south bath tub", (54.4, 6.4, 59.4, 8.95)), ("south bath vanity", (62.5, 6.4, 67.1, 8.25)), ("south bath WC", (65.2, 9.5, 67.1, 11.3)),
             ("laundry washer + dryer", (67.8, 6.4, 72.6, 8.75)), ("dog wash (pet room)", (65.5, 26.5, 69.0, 28.9))]}
MECH = {"main": [("range (fuel not stated)", (35.9, 14.7, 38.2, 17.66)), ("fridge (water supply not stated)", (35.8, 25.89, 38.29, 29.11))],
        "base": [("air handler", (22.8, 35.7, 25.8, 38.7)), ("boiler", (26.3, 35.7, 28.5, 37.7)), ("water heater", (29.0, 35.7, 31.2, 37.9)),
                 ("well-water treatment", (33.8, 35.7, 36.6, 37.7)), ("HRV (wall-mounted, z 5.5-7)", (22.8, 40.4, 25.8, 42.3)),
                 ("pool filter (round)", (99.9, 38.7, 102.2, 41.0)), ("pool pump", (96.8, 39.2, 99.3, 41.0)), ("pool heater", (99.7, 33.0, 102.3, 36.0)),
                 ("pool dehumidifier", (99.4, 29.6, 102.3, 32.4)), ("pool chemicals", (97.0, 29.6, 98.6, 31.2)), ("laundry counter (sink not stated)", (77.0, 6.4, 81.1, 8.45))]}
def wet_type(L, k):
    f = L.fix[k]; c = cname(f[6]); ri = fix_room(L, f)
    if ri is None: return None
    r = L.rooms[ri]; lab_ = LAB(L, ri); kind = r[6]
    if c == "basin": return "sink"
    if c == "tile": return "shower"
    if c == "white" and (kind in ("bath", "shower") or (kind == "utility" and any(w in lab_ for w in ("PET", "DOG", "LAUNDRY", "MUD")))): return "toilet/tub/wash basin"
    if c == "counter" and kind in ("bath", "shower"): return "vanity"
    if c == "steel" and abs(f[5] - 3.2) < 0.01 and "LAUNDRY" in lab_: return "washer/dryer"
    return None
def locate(L, box_):
    for k, f in enumerate(L.fix):
        if all(abs(f[n] - box_[n]) < 0.006 for n in range(4)):
            return k
    raise KeyError(box_)
def wet_fixtures(L):
    res = []
    if VARIANT:
        entries = [(f"{wet_type(L, k)} ({L.names[fix_room(L, L.fix[k])]})", k, tuple(L.fix[k][:4])) for k in range(len(L.fix)) if wet_type(L, k)]
    else:
        entries = [(nm, locate(L, b), b) for nm, b in WETDEF[L.tag]]
    for nm, k, b in entries:
        f = L.fix[k]
        cx_, cy_ = (f[0] + f[2]) / 2, (f[1] + f[3]) / 2
        ri = room_of(L, cx_, cy_)
        r = L.rooms[ri]
        gaps = {("x", r[2], "S"): f[1] - r[2], ("x", r[4], "N"): r[4] - f[3], ("y", r[1], "W"): f[0] - r[1], ("y", r[3], "E"): r[3] - f[2]}
        (ax, coord, side), g = min(gaps.items(), key=lambda kv: kv[1])
        island = g > 3.0
        res.append(dict(name=nm, k=k, box=b, c=(cx_, cy_), room=L.names[ri], axis=ax, coord=coord, side=side, gap=g, island=island,
                        ext=(f[0], f[1], f[2], f[3]), src=S(L.fk, k)))
    return res
def wet_groups(L, fx, gap_lim):
    n = len(fx); par = list(range(n))
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for a in range(n):
        for b in range(a + 1, n):
            A, B = fx[a], fx[b]
            if A["island"] or B["island"]: continue
            if A["axis"] != B["axis"] or abs(A["coord"] - B["coord"]) > 1.0: continue
            ia = (A["ext"][0], A["ext"][2]) if A["axis"] == "x" else (A["ext"][1], A["ext"][3])
            ib = (B["ext"][0], B["ext"][2]) if B["axis"] == "x" else (B["ext"][1], B["ext"][3])
            gp = max(ib[0] - ia[1], ia[0] - ib[1], 0)
            if gp <= gap_lim:
                par[find(a)] = find(b)
    groups = defaultdict(list)
    for a in range(n):
        groups[find(a)].append(a)
    return sorted(groups.values(), key=lambda g: (fx[g[0]]["c"][1], fx[g[0]]["c"][0]))
WFM, WFB = wet_fixtures(MAIN), wet_fixtures(BASE)
def gdesc(fx, groups):
    res = []
    for gi, g in enumerate(groups, 1):
        cx_ = sum(fx[a]["c"][0] for a in g) / len(g); cy_ = sum(fx[a]["c"][1] for a in g) / len(g)
        ws = [fx[a] for a in g]
        res.append(dict(n=gi, members=[w["name"] for w in ws], rooms=sorted({w["room"] for w in ws}), cen=(cx_, cy_), walls=(", ".join(sorted({(f"y={w['coord']:g} (horizontal wall)" if w['axis']=='x' else f"x={w['coord']:g} (vertical wall)") for w in ws})) if not ws[0]["island"] else "free-standing island (>3 ft from any wall)")))
    return res
GM, GB = gdesc(WFM, wet_groups(MAIN, WFM, WET_GAP)), gdesc(WFB, wet_groups(BASE, WFB, WET_GAP))
def man(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
nearest_stack = []
for g in GM:
    b = min(GB, key=lambda x: man(g["cen"], x["cen"]))
    nearest_stack.append((g, b, abs(g["cen"][0] - b["cen"][0]), abs(g["cen"][1] - b["cen"][1])))
drain = sum(man(g["cen"], DRAIN_EXIT) for g in GM)
drain_alt = sum(man(g["cen"], (22.16, 38.9)) for g in GM)
sens = {gl: (len(wet_groups(MAIN, WFM, gl)), len(wet_groups(BASE, WFB, gl))) for gl in (4, 6, 8, 12, 1e9)}
# plumbing clusters (wet rooms back-to-back)
def clusters(L, fx):
    rs = sorted({room_of(L, w["c"][0], w["c"][1]) for w in fx})
    par = {r: r for r in rs}
    def find(a):
        while par[a] != a: a = par[a]
        return a
    for a in rs:
        for b in rs:
            if a < b and any(ln > 1.0 for _, ln in shared_edges(L, a, b)):
                par[find(a)] = find(b)
    cl = defaultdict(list)
    for r in rs: cl[find(r)].append(L.names[r])
    return list(cl.values())
CLM, CLB = clusters(MAIN, WFM), clusters(BASE, WFB)
def fixtable(fx, L):
    return table(["fixture", "room", "box (x0,y0,x1,y1)", "centre", "nearest wall", "gap ft", "source"],
                 [[w["name"], w["room"], w["box"], f"({w['c'][0]:.1f}, {w['c'][1]:.1f})", ("island" if w["island"] else f"{w['side']} wall {'y' if w['axis']=='x' else 'x'}={w['coord']:g}"), f"{w['gap']:.2f}", w["src"]] for w in fx])
def mtable(L):
    if VARIANT:
        return "(equipment list omitted in variant mode)\n"
    rows = []
    for nm, b in MECH[L.tag]:
        k = locate(L, b); f = L.fix[k]
        rows.append([nm, room_of(L, (f[0] + f[2]) / 2, (f[1] + f[3]) / 2) is not None and L.names[room_of(L, (f[0] + f[2]) / 2, (f[1] + f[3]) / 2)], f"({(f[0]+f[2])/2:.1f}, {(f[1]+f[3])/2:.1f})", S(L.fk, k)])
    return table(["equipment (non-wet-wall list)", "room", "centre", "source"], rows)
_ut = [i for i in range(len(BASE.rooms)) if "UTILITY" in LAB(BASE, i)]
wh_k = next((k for k, f in enumerate(BASE.fix) if len(f) > 8 and f[8] == "round" and fix_room(BASE, f) in _ut), None)
boil_k = next((k for k, f in enumerate(BASE.fix) if cname(f[6]) == "steel" and abs(f[5] - 3.5) < 0.01 and fix_room(BASE, f) in _ut), None)
wh = list(fixc(BASE.fix[wh_k])) if wh_k is not None else list(centroid(BASE, _ut[0]))
boil = list(fixc(BASE.fix[boil_k])) if boil_k is not None else list(wh)
def far(fx, pt, add=0):
    best = max(fx, key=lambda w: man(w["c"], pt))
    return best["name"], man(best["c"], pt)
fm, fmv = far(WFM, wh); fb, fbv = far(WFB, wh)
pl = model["pool"]["xy"]; sp = model["spa"]["xy"]
s = "Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).\n\n"
s += "### 9.1 Main floor wet fixtures\n\n" + fixtable(WFM, MAIN) + "\n" + mtable(MAIN)
s += "\n### 9.2 Basement wet fixtures\n\n" + fixtable(WFB, BASE) + "\n" + mtable(BASE)
s += f"\nPool shell: x {pl[0]}-{pl[2]}, y {pl[1]}-{pl[3]} (15 x 15) and spa x {sp[0]}-{sp[2]}, y {sp[1]}-{sp[3]} (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).\n"
s += f"\n### 9.3 Wet walls (definition and result)\n\n**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= {WET_GAP:g} ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.\n\n"
def gtable(G, fx_):
    return table(["wet group", "fixtures", "rooms", "wall line(s)", "centroid (x,y)"], [[f"G{g['n']}", "; ".join(g["members"]), "; ".join(g["rooms"]), g["walls"], f"({g['cen'][0]:.1f}, {g['cen'][1]:.1f})"] for g in G])
s += "Main floor:\n\n" + gtable(GM, WFM) + f"\n**Main floor: {len(GM)} wet-wall groups** ({len(CLM)} back-to-back plumbing clusters of rooms: " + " | ".join("+".join(c) for c in CLM) + ")\n\nBasement:\n\n" + gtable(GB, WFB) + f"\n**Basement: {len(GB)} wet-wall groups** ({len(CLB)} clusters: " + " | ".join("+".join(c) for c in CLB) + ")\n"
s += "\nSensitivity of the group count to the along-wall chaining limit (main / basement): " + "; ".join(("inf: " if gl>1e8 else f"{gl:g} ft: ")+f"{a}/{b}" for gl, (a, b) in sens.items()) + "\n"
s += "\n### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group\n\nThere is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.\n\n"
s += table(["main group", "members", "centroid", "nearest basement group", "its centroid", "dx", "dy", "Manhattan ft"],
           [[f"G{g['n']}", "; ".join(g["members"][:3]) + ("..." if len(g["members"]) > 3 else ""), f"({g['cen'][0]:.1f},{g['cen'][1]:.1f})", f"B{b['n']} ({'; '.join(b['rooms'])})", f"({b['cen'][0]:.1f},{b['cen'][1]:.1f})", f"{dx:.1f}", f"{dy:.1f}", f"{dx+dy:.1f}"] for g, b, dx, dy in nearest_stack])
s += f"\nMain-floor groups with a basement group within 5 ft Manhattan: {sum(1 for _,_,dx,dy in nearest_stack if dx+dy<=5)} of {len(GM)}; within 10 ft: {sum(1 for _,_,dx,dy in nearest_stack if dx+dy<=10)}.\n"
s += f"\n### 9.5 Drain-run index (used for all layout options)\n\n**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = {DRAIN_EXIT}. (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)\n\n"
s += table(["group", "centroid", "Manhattan to E", "to alt E (22.16, 38.9) UTILITY west wall"], [[f"G{g['n']}", f"({g['cen'][0]:.1f},{g['cen'][1]:.1f})", f"{man(g['cen'], DRAIN_EXIT):.1f}", f"{man(g['cen'], (22.16,38.9)):.1f}"] for g in GM])
s += f"\n**DRI (E = (22.16, 58)) = {drain:.1f} ft over {len(GM)} groups; mean {drain/len(GM):.1f} ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is {drain_alt:.1f} ft.\n"
s += f"\n### 9.6 Water heater / boiler to the furthest fixture\n\nWater heater centre (30.1, 36.8) (basement.scad:{src['bf'][wh_k][0]}, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:{src['bf'][boil_k][0]}). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.\n\n"
bo_ = [(w, man(w['c'], wh)) for w in WFM]
s += f"- Furthest main-floor fixture from the water heater (plan Manhattan): **{fm}, {fmv:.1f} ft** (plus ~{model['levels']['floor_to_floor']:.2f} ft vertical floor-to-floor; the runs go under the main floor). From the boiler: {far(WFM, boil)[0]}, {far(WFM, boil)[1]:.1f} ft.\n- Furthest basement fixture: **{fb}, {fbv:.1f} ft** from the water heater.\n- Nearest main-floor fixture: {min(bo_, key=lambda t:t[1])[0]['name']}, {min(t[1] for t in bo_):.1f} ft.\n"
s += "\nPer fixture (Manhattan plan ft from the water heater): " + "; ".join(f"{w['name']} {man(w['c'], wh):.0f}" for w in WFM + WFB) + "\n"
sec[9] = s
out["plumbing"] = dict(groups_main=len(GM), groups_base=len(GB), dri=drain, dri_alt=drain_alt, clusters_main=len(CLM), clusters_base=len(CLB), far_main=(fm, fmv), far_base=(fb, fbv))

# ---------------------------------------------------------------- §10 stairs
st = model["stair"]; ex = model["exit_stair"]; fl = model["levels"]
sx0, sx1 = st["x"]
open_len = st["top_y"] - (35.46 + WALL_T / 2 + 0.01)
s = "### 10.1 Main to basement stair (house_lib.scad:107-125, values via model.json `stair`)\n\n"
s += table(["Item", "Value", "Source / formula"], [
    ["Wall centre lines x", f"{sx0} to {sx1}", "house_lib.scad:120 stair_x()"],
    ["Clear width between walls", f"{sx1-sx0-WALL_T:.2f} ft = {(sx1-sx0-WALL_T)*12:.1f} in", "x range minus wall_t 0.4 (Redesign doc line 157 says 4'-2 1/2\")"],
    ["Floor to floor", f"{fl['floor_to_floor']} ft", "house_lib.scad:107"],
    ["Risers / rise each", f"{st['risers']} x {st['rise']*12:.3f} in", "house_lib.scad:121-122 ceil(floor_to_floor*12/7.5)"],
    ["Treads / run each", f"{st['risers']-1} x {st['run']*12:.1f} in", "house_lib.scad:123 stair_run=10.5/12; treads = risers-1"],
    ["Total run", f"{(st['risers']-1)*st['run']:.3f} ft ({(st['risers']-1)*st['run']*12:.1f} in)", "21 x 10.5 in"],
    ["Top nosing y / foot y", f"{st['top_y']} / {st['foot_y']:.3f}", "house_lib.scad:124-125; foot = top - 21*run"],
    ["Main-floor stairwell room STAIR DN", f"x {sx0}-{sx1}, y 35.46-{st['top_y']} (ceiling 0)", f"{S('mr', stair_main)}"],
    ["Floor opening in the main floor assembly", f"{sx1-sx0-WALL_T-0.02:.2f} x {open_len:.2f} ft (11'-5\" per Redesign line 165)", "computed from main_floor.scad:337-338 floor_assembly() cut"],
    ["Basement stair room STAIR UP", f"x {sx0}-{sx1}, y {st['foot_y']:.3f}-45.34", S("br", stair_base)],
    ["Headroom", "Redesign doc: >= 1 993 mm at the tightest point vs 1 950 mm required; the floor opening was sized for it (house_lib.scad:112-119 comment)", "Redesign-and-Spec-2026-11-02.md:158, 162-167; not recomputed here"],
    ["Handrails", "both sides in the model (house_lib.scad main_stair rail=true)", "house_lib.scad:324-340 main_stair(); Redesign doc:159"],
    ["Landings", "top: the stair landing/upper hall; bottom: HALLWAY at the 8 ft archway (basement.scad:89 'open' 8 ft) into the living room", "Redesign doc:160"],
])
s += "\n### 10.2 Basement exit stair (foundation.scad:134-142, model.json `exit_stair`)\n\n"
s += table(["Item", "Value", "Source"], [
    ["Door", f"x {ex['door'][0]}, {ex['door'][1]} ft wide ({ex['door'][1]*12:.0f} in) in the gym's north wall y=63.16, opens in", f"basement.scad:98; foundation.scad:134"],
    ["Rise to grade", f"{ex['rise']} ft; {ex['risers']} risers x {ex['rise']*12/ex['risers']:.2f} in", "foundation.scad:135-136"],
    ["Run", f"{ex['run']*12:.0f} in treads; flight length {ex['areaway'][2]-ex['landing_x'][1]:.2f} ft", "foundation.scad:137, 139"],
    ["Landing x range", f"{ex['landing_x']}", "foundation.scad:138"],
    ["Areaway clear inside", f"x {ex['areaway'][0]}-{ex['areaway'][2]:.2f}, y {ex['areaway'][1]}-{ex['areaway'][3]} (4.0 ft wide)", "foundation.scad:139"],
    ["Top landing at grade", f"{ex['top_pad']} ft past the top step", "foundation.scad:141"],
    ["Footprint with walls", f"{[round(v,2) for v in ex['footprint']]}", "foundation.scad:144"],
    ["Direction", "rises east along the house's north side, ending beside the deck steps (Redesign doc:473-480)", "Redesign doc"],
])
s += f"\nThe exit stair comes up beside the PATIO, whose north edge has a guard (main_floor.scad:345-354 patio_guard). Basement windows: 2 wells (foundation.scad:159-162).\n"
sec[10] = s

# ---------------------------------------------------------------- §12 site
tank, chamber, field, reserve = [-3, 52, 3, 64], [-3, 64, 3, 68], [-120, 45, -65, 100], [-120, -15, -65, 40]
well, shop, road = (150, 75), box(0, 130, 100, 230), -100
def dr(a, b):
    return a.distance(b)
T, C, F, R = box(*tank), box(*chamber), box(*field), box(*reserve)
house_heated = box(0, 0, 1, 1)  # placeholder
HU = union.union(box(*rect(MAIN.rooms[gar]))) if gar is not None else union   # heated + garage
HU_only = union
bs_wall = box(22.16 - 0.55, 35.08, 22.16, 63.16)   # outer face of basement west wall (c/l 22.16)
basement_poly = bpoly
wellp = Point(*well)
shop_south = 130
all_main = unary_union([box(*rect(r)) for r in MAIN.rooms])
service = {"power": [(-44, -100), (-44, 46), (7.27, 46)], "gas": [(-47, -100), (-47, 48), (7.27, 48)], "fibre": [(-41, -100), (-41, 44), (7.27, 44)],
           "water (well)": [(150, 75), (150, 45), (126.97, 45)]}
sl = {k: LineString(v).length for k, v in service.items()}
ft2m = 0.3048
def D(a, b):
    d = a.distance(b)
    return f"{d:.1f} ft ({d*ft2m:.1f} m)"
s = "Read with `phase = \"house\"` (site.scad:47, the default) for everything except the shop rows, which are the `phase = \"full\"` geometry (site.scad:122-131, 196-197, 245) and the future-shop dashed rectangle (site.scad:217-221, shop_origin() = [0,130], site.scad:60). Land is not chosen: positions are relative to the house (site.scad:6-8). Road assumed on the south (site.scad:8, 74: road north edge y = -100).\n\n"
s += "### 12.1 Coordinates (site.scad)\n\n" + table(["Item", "Coordinates [x0,y0,x1,y1] or point", "Source"], [
    ["Septic tank", "[-3, 52, 3, 64]  (6 x 12 ft)", "site.scad:70"], ["Pump chamber", "[-3, 64, 3, 68]", "site.scad:71"], ["Treatment field", "[-120, 45, -65, 100]  (55 x 55 ft)", "site.scad:72"],
    ["Reserve field", "[-120, -15, -65, 40]", "site.scad:73"], ["Well", "(150, 75)", "site.scad:63"], ["Propane tank", "(-60, -45) centre; pad 16 x 6 ft", "site.scad:64, 170"], ["Starlink dish", "(12, 80)", "site.scad:65"],
    ["West driveway", "x -32..-2 (30 ft wide), y -100..42 (142 ft long)", "site.scad:111"], ["Front loop", "ring x 25..130, y -72..-14, 14 ft wide legs; connector x -2..25, y -50..-36", "site.scad:113-117"],
    ["Future shop (house phase)", "dashed [0,130]-[100,230]", "site.scad:60, 218"], ["Service lines", "fibre x=-41, power x=-44, gas x=-47, from y=-100 north to y=44/46/48 then east to x=7.27 (bedroom-wing west wall)", "site.scad:162-164"],
    ["Meters", "two boxes on x=6.6, y 45 and 47.5", "site.scad:175"], ["Water line", "well (150,75) -> (150,45) -> (126.97,45)", "site.scad:167"], ["Building sewer", "(22.16,58) -> (3,58) (tank east face); effluent line (-3,66) -> (-65,66)", "site.scad:188, 191"],
])
s += "\n### 12.2 Distances (computed with shapely from those rectangles; ft and m)\n\n"
rows = [
    ["Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27)", D(T, HU_only)],
    ["Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6)", f"{22.16-3:.2f} ft ({(22.16-3)*ft2m:.1f} m) / {21.61-3:.2f} ft"],
    ["Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner", D(T, box(22.16, 35.08, 37.37, 42.77))],
    ["Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour", D(T, box(22.16, 50.35, 22.17, 63.16))],
    ["Septic tank to well", D(T, wellp)], ["Pump chamber to well", D(C, wellp)],
    ["Treatment field to well", D(F, wellp)], ["Reserve field to well", D(R, wellp)],
    ["Treatment field to the basement (outline polygon)", D(F, basement_poly)], ["Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27)", D(F, HU_only)],
    ["Treatment field to the garage west wall (x=0, slab, no basement)", D(F, box(0, 1.25, 24.34, 35.46))],
    ["Reserve field to basement", D(R, basement_poly)], ["Reserve field to the nearest heated wall", D(R, HU_only)], ["Reserve field to the garage", D(R, box(0, 1.25, 24.34, 35.46))],
    ["Treatment field to west driveway edge (x=-32)", D(F, box(-32, -100, -2, 42))], ["Reserve field to west driveway edge", D(R, box(-32, -100, -2, 42))],
    ["Treatment field to the service-line corridor (x=-47..-41)", D(F, box(-47, -100, -41, 48))], ["Reserve field to the service-line corridor", D(R, box(-47, -100, -41, 48))],
    ["Reserve field to propane pad (-68..-52, -48..-42)", D(R, box(-68, -48, -52, -42))],
    ["Well to heated main-floor wall (nearest)", D(wellp, HU_only)], ["Well to side porch/deck edge (nearest unconditioned main-floor row)", D(wellp, all_main)],
    ["Well to basement outline", D(wellp, basement_poly)],
    ["House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130)", D(HU_only, shop)],
    ["House incl. porches/deck to future shop", D(all_main, shop)], ["Basement exit areaway (y 67.75) to shop", D(box(*ex['areaway']), shop)],
    ["Garage to shop (garage north wall 35.46)", D(box(0, 1.25, 24.34, 35.46), shop)],
]
s += table(["Pair", "Distance"], rows)
s += f"\nCorridor and drive lengths: power run road->meter wall {sl['power']:.1f} ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas {sl['gas']:.1f} ft; fibre {sl['fibre']:.1f} ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: {sl['water (well)']:.1f} ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).\n"
s += f"\nWest driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).\n"
s += "\nphase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = "
s += f"{LineString([(-50,50),(-50,126),(80,126),(80,130)]).length:.0f} ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.\n"
s += "\nPhase house: parents' house and geothermal loop field are not in site.scad (§13).\n"
sec[12] = s
out["site"] = dict(dri=drain)

# ---------------------------------------------------------------- matrix (variant comparison block)
SQFT_M2 = 0.09290304
def footprint(rooms_):
    return unary_union([box(*rect(r)).buffer(0.01, join_style=2) for r in rooms_ if r[6] != "porch"]).buffer(-0.01, join_style=2)
_cur_union = footprint(model["main_rooms"])                 # the CURRENT model (model.json), for the calibration
def _m2_at(u, t):
    return (u.buffer(t, join_style=2).area if t else u.area) * SQFT_M2
_lo, _hi = 0.0, 3.0
for _ in range(60):
    _mid = (_lo + _hi) / 2
    if _m2_at(_cur_union, _mid) < 608.0: _lo = _mid
    else: _hi = _mid
OFFSET = (_lo + _hi) / 2
bu = footprint(MAIN.rooms)
M2_CL, M2_OUT = bu.area * SQFT_M2, _m2_at(bu, OFFSET)
_hu = unary_union([box(*rect(r)).buffer(0.01, join_style=2) for r in MAIN.rooms if r[6] not in ("porch", "garage")]).buffer(-0.01, join_style=2)
HEAT_FP_CL, HEAT_FP_OUT = _hu.area, _hu.buffer(OFFSET, join_style=2).area
_bfu = unary_union([box(*rect(r)).buffer(0.01, join_style=2) for r in BASE.rooms if r[6] != "porch" and label(r) != "EXIT STAIR"]).buffer(-0.01, join_style=2)
BASE_FP_CL, BASE_FP_OUT = _bfu.area, _bfu.buffer(OFFSET, join_style=2).area
def sides_str(L, ids, skip_garage=False):
    agg = defaultdict(lambda: defaultdict(float))
    for i in ids:
        for (sd, cl), v in L.ext[i].items():
            agg[sd][cl.split(" ")[0].replace("yard/soil", "yard")] += v
    parts = []
    for sd in "NSEW":
        if sd in agg:
            parts.append(sd + "(" + ", ".join(f"{c} {v:.1f}" for c, v in sorted(agg[sd].items())) + ")")
    return " ".join(parts) or "none"
def has_outside_side(L, i):
    return any(not cl.startswith("garage") for (sd, cl) in L.ext[i])
fixed_halls = [i for i in mc if max(clear_dims(MAIN, i)) >= 6.0]
min_hall = min((min(clear_dims(MAIN, i)), i) for i in fixed_halls) if fixed_halls else (None, None)
raw_min_hall = min((min(clear_dims(MAIN, i)), i) for i in mc) if mc else (None, None)
single = {"<32": 0, "32-35": 0, ">=36": 0}
for r in MD:
    if r["type"] == "door": single[bucket(r["w"])] += 1
n_double = sum(1 for r in MD if r["type"] == "double"); n_open = sum(1 for r in MD if r["type"] == "open")
stacked5 = sum(1 for _, _, dx, dy in nearest_stack if dx + dy <= 5)
bed_living = []
for i in BEDS:
    liv = [MAIN.names[j] for j in LIVINGS if any(l > 1.0 for _, l in shared_edges(MAIN, i, j))]
    if liv: bed_living.append(f"{MAIN.names[i]} - {', '.join(liv)}")
bed_foyer = [MAIN.names[i] for i in BEDS if FOY is not None and any(l > 1.0 for _, l in shared_edges(MAIN, i, FOY))]
def _wd_in_suite():
    return [k for k, f in enumerate(MAIN.fix) if cname(f[6]) == "steel" and abs(f[5] - 3.2) < 0.01 and fix_room(MAIN, f) in SUITE]
wd_suite = _wd_in_suite()
laundry_count = len(LAUS) + len(wd_suite)
m2l = [p for p in paths if p["title"].startswith("master bedroom centre -> ") and any(MAIN.names[l] in p["title"] for l in LAUS)]
m2l_txt = ("0 (W/D inside the master suite)" if wd_suite else None) or (", ".join(f"{p['title'].split('-> ')[1].replace(' centre','')}: {p['len']:.1f} ft" for p in m2l) or "n/a (no laundry room)")
m2l_min = min((p["len"] for p in m2l if p["len"] is not None), default=None)
clos = [i for i in idx(MAIN, lambda i, r: r[6] == "closet") if has_outside_side(MAIN, i)]
clos_all = idx(MAIN, lambda i, r: r[6] == "closet")
pant_yes = []
for sc in SCULS:
    sh = sum(l for _, l in shared_edges(MAIN, sc, GAR)) if GAR is not None else 0
    dr_ = [d for d in MD if {d["ai"], d["bi"]} == {sc, GAR}]
    pant_yes.append((MAIN.names[sc], sh, len(dr_)))
pant_flag = "Y" if any(sh > 1.0 and nd > 0 for _, sh, nd in pant_yes) else "N"
liv_s = []
for i in LIVINGS:
    v = sum(l for (sd, cl), l in MAIN.ext[i].items() if sd == "S" and not cl.startswith("garage"))
    if v > 0.5: liv_s.append(f"{MAIN.names[i]} ({v:.1f} ft)")
multi_w = [f"{n} ({'/'.join(f)})" for n, f in mm]
if STAIRW is not None and stair_base_ is not None:
    _sr, _br = MAIN.rooms[STAIRW], BASE.rooms[stair_base_]
    _run = (model["stair"]["risers"] - 1) * model["stair"]["run"]
    _al = abs(_sr[1] - _br[1]) < 0.05 and abs(_sr[3] - _br[3]) < 0.05
    _len = _sr[4] - _br[2]
    stair_txt = (f"top (nosing) at x {_sr[1]:g}..{_sr[3]:g}, y {_sr[4]:g}; basement foot room x {_br[1]:g}..{_br[3]:g}, y {_br[2]:g}; "
                 + ("**same** (aligned, run %.3f ft)" % _len if _al and abs(_len - _run) < 0.05 else
                    f"**moved** (x offset {_sr[1]-_br[1]:+.2f}/{_sr[3]-_br[3]:+.2f} ft, run {_len:.3f} ft vs flight {_run:.3f} ft)")
                 + f"; vs Phase 0 stair top y {model['stair']['top_y']}, foot y {model['stair']['foot_y']:.3f}")
else:
    stair_txt = "no stairwell/stair row found"
bed_drive = sorted((box(*rect(MAIN.rooms[i])).distance(drive_union), MAIN.names[i]) for i in BEDS)
chk_args = [str(MAIN_FILE)] + ([str(BASE_FILE)] if (ARGS.basement or ARGS.main) else [])
if not VARIANT: chk_args = []
_chk = subprocess.run(["python3", "/home/user/house/tools/check_layout.py"] + chk_args, capture_output=True, text=True)
chk_txt = (_chk.stdout.strip().replace("\n", " ; ") or _chk.stderr.strip()[-300:]) + f" (exit {_chk.returncode})"
far_by_wh = fm, fmv
MX = [
    ("Main-floor conditioned sq ft", f"{heated_sum:,.0f}", f"{heated_sum:.1f}; excl. stair opening {heated_sum - stairwell_area:.1f}"),
    ("Building area, centre lines (house + attached garage)", f"{M2_CL:.1f} m2", f"{bu.area:.0f} sq ft"),
    ("Building area, outside face", f"{M2_OUT:.1f} m2", f"offset {OFFSET:.4f} ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants"),
    ("Heated main-floor footprint excl. garage, outside face", f"{HEAT_FP_OUT:,.0f} sq ft", f"centre lines {HEAT_FP_CL:,.0f} sq ft; same {OFFSET:.2f} ft outward offset; round-2 target <= 3,000 sq ft"),
    ("Basement footprint, outside face (excl. exit-stair areaway)", f"{BASE_FP_OUT:,.0f} sq ft", f"centre lines {BASE_FP_CL:,.0f} sq ft"),
    ("Circulation % (strict / with foyer)", f"{100*mc_a/mb:.1f}% / {100*(mc_a+(area(MAIN.rooms[FOY]) if FOY is not None else 0))/mb:.1f}%", f"{mc_a:.0f} sq ft strict of {mb:.0f}"),
    ("Single doors <32 in / 32-35 in / 36 in+ (main)", f"{single['<32']} / {single['32-35']} / {single['>=36']}", "type `door` rows, by opening width"),
    ("Double / open counts (main)", f"{n_double} / {n_open}", "type `double` / type `open`"),
    ("Minimum hall clear width", f"{min_hall[0]:.2f} ft ({MAIN.names[min_hall[1]]})" if min_hall[0] is not None else "n/a", f"halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers {raw_min_hall[0]:.2f} ft ({MAIN.names[raw_min_hall[1]] if raw_min_hall[1] is not None else ''})"),
    ("Wet-wall groups (main / basement)", f"{len(GM)} / {len(GB)}", "8 ft along-wall chaining, same-line within 1 ft"),
    ("Main groups within 5 ft of a basement group", f"{stacked5} of {len(GM)}", "Manhattan between centroids"),
    ("Drain-run index, E = (22.16, 58)", f"{drain:.1f} ft", f"alternate exit (22.16, 38.9): {drain_alt:.1f} ft"),
    ("Water heater -> furthest fixture (main / basement)", f"{fmv:.1f} ft ({fm}) / {fbv:.1f} ft ({fb})", f"water heater at ({wh[0]:.1f}, {wh[1]:.1f}); plan Manhattan"),
    ("Bedrooms sharing a wall with a living-kind room", f"{len(bed_living)}" + (": " + "; ".join(bed_living) if bed_living else ""), "shared length > 1 ft; living-kind rooms with walls"),
    ("A bedroom shares a wall with the foyer", ("Y: " + ", ".join(bed_foyer)) if bed_foyer else "N", "foyer/vestibule label" if FOY is not None else "no foyer row"),
    ("Master bed -> laundry path", m2l_txt, "walk ft, Dijkstra over door midpoints (Phase 0 method)"),
    ("Laundry count", f"{laundry_count}", f"{len(LAUS)} LAUNDRY room(s)" + (f" + {len(wd_suite)} W/D in the master suite" if wd_suite else "")),
    ("Closets/WICs touching an exterior wall (not garage)", f"{len(clos)} of {len(clos_all)}: " + "; ".join(f"{MAIN.names[i]} [{sides_str(MAIN, [i])}]" for i in clos), "kind closet; yard / porch faces count, garage does not"),
    ("Pantry/scullery shares a wall with the garage AND has a door to it", pant_flag, "; ".join(f"{n}: {sh:.1f} ft shared, {nd} door(s)" for n, sh, nd in pant_yes) or "no SCULLERY/PANTRY room"),
    ("Each bedroom's exterior sides", " ;; ".join(f"{MAIN.names[i]}: {sides_str(MAIN, [i])}" for i in BEDS), "N/S/E/W with the length (ft) facing yard / porch / garage"),
    ("Master suite exterior sides", sides_str(MAIN, sorted(SUITE)) if SUITE else "n/a", "suite rooms: " + ", ".join(MAIN.names[i] for i in sorted(SUITE))),
    ("Living-kind rooms with S exposure", "; ".join(liv_s) or "none", "S edge facing yard/porch"),
    ("Rooms with windows on 2+ walls", f"{len(mm)}: " + "; ".join(multi_w), "window rows, facade per Phase 0 rule"),
    ("Main stair top/foot vs the basement stair", stair_txt, ""),
    ("Min distance bedroom -> drive (house phase)", f"{bed_drive[0][0]:.1f} ft ({bed_drive[0][1]})" if bed_drive else "n/a", "centre-line rectangle to nearest drive piece, site.scad:108-118"),
    ("check_layout.py", chk_txt, "python3 tools/check_layout.py on the variant file(s)" if VARIANT else "both current level files"),
]
mx = "## Layout matrix\n\nSource files: main = `%s`; basement = `%s`.\n\n" % (MAIN_FILE, BASE_FILE)
mx += table(["Measure", "Value", "Note"], [list(r) for r in MX])
(CMP / "matrix.md").write_text(mx)
out["matrix"] = {k: v for k, v, _ in MX}

# ---------------------------------------------------------------- write
for k, v in sec.items():
    (CMP / f"sec{k}.md").write_text(v)
json.dump(out, open(CMP / "facts.json", "w"), indent=1, default=str)
print("ok", {k: (round(v, 1) if isinstance(v, float) else v) for k, v in out["env"].items()})
print(out["circ"]); print(out["plumbing"])
if VARIANT:
    head = f"# Plan facts (variant mode)\n\nmain = `{MAIN_FILE}`, basement = `{BASE_FILE}`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.\n\n"
    body = ""
    for k in sorted(sec):
        body += f"## Section {k}\n\n" + sec[k] + "\n"
    (OUT / "plan_facts.md").write_text(head + mx + "\n" + body)
    (OUT / "matrix.md").write_text(mx)
    print("variant facts ->", OUT)
