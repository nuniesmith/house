#!/usr/bin/env python3
"""Draw a level file's audit tables as a phone-readable plan.

    python3 plot_plan.py <level.scad> <out.png> [--title "..."] [--width-px 2400] [--no-fixtures]

Works on any level SCAD that supports `-D audit=true` and echoes
`rooms = ..., doors = ..., windows = ..., fixtures = ...` (main_floor.scad,
basement.scad and variants of them). Output is ~2400 px wide.

Drawing: room outlines (kind-tinted fill; dashed for ceiling-0 open zones),
name + centre-line area in sq ft in each room, door openings as gaps in the
wall with swing arcs, windows as heavy blue lines on the wall, fixtures as
light grey boxes, 10 ft grid with feet on the axes, north arrow (y = north).
Labels shrink / abbreviate / rotate to fit; the ones that cannot reach
MIN_PT are numbered and keyed in the margin.
"""
import argparse, ast, math, re, subprocess, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle, FancyArrow

MIN_PT = 9.0
MAX_PT = 16.0
KIND = {"bed": "#dbe8fa", "bath": "#d1edf2", "shower": "#9fd1ee", "closet": "#e2e2dc", "hall": "#f8f3e6", "living": "#faf2da",
        "kitchen": "#ffecd1", "dining": "#fdeed6", "office": "#ebe6f7", "utility": "#f0e3cc", "garage": "#d1d1d1", "stair": "#e6e1d6",
        "pool": "#cdeaf2", "rec": "#f4f4ea", "porch": "#e1f0e1"}
ABBR = [("BEDROOM", "BR"), ("MASTER", "MSTR"), ("KITCHEN", "KIT"), ("LAUNDRY", "LDRY"), ("CLOSET", "CL"), ("STORAGE", "STOR"),
        ("EQUIP.", "EQ"), ("EQUIPMENT", "EQ"), ("THEATER", "THTR"), ("LIVING", "LIV"), ("BREAKFAST", "BKFST"), ("MUDROOM", "MUD"),
        ("SCULLERY", "SCUL"), ("ROOM", "RM"), ("PORCH", "PCH"), ("GARAGE", "GAR"), ("UTILITY", "UTIL"), ("OFFICE", "OFC")]


def get_tables(scad):
    r = subprocess.run(["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", str(scad)],
                       capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$", r.stdout + r.stderr, re.M)
    if not m:
        sys.exit(f"{scad}: no audit output\n{r.stderr[-800:]}")
    lit = lambda s: ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))
    return [lit(g) for g in m.groups()]


def label_lines(r):
    return list(r[0]) if isinstance(r[0], list) else ([r[0]] if r[0] else [])


def abbreviate(line):
    for a, b in ABBR:
        line = line.replace(a, b)
    return line


def leaf_line(hx, hy, u, n, w, steps=1):
    return [(hx, hy), (hx + w * n[0], hy + w * n[1])]


def arc(hx, hy, u, n, w):
    pts = []
    for k in range(0, 21):
        a = math.pi / 2 * k / 20
        pts.append((hx + w * (math.cos(a) * u[0] + math.sin(a) * n[0]), hy + w * (math.cos(a) * u[1] + math.sin(a) * n[1])))
    return pts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scad"); ap.add_argument("out")
    ap.add_argument("--title", default=None)
    ap.add_argument("--width-px", type=int, default=2400)
    ap.add_argument("--no-fixtures", action="store_true")
    a = ap.parse_args()
    rooms, doors, wins, fixes = get_tables(a.scad)

    xs = [r[1] for r in rooms] + [r[3] for r in rooms]
    ys = [r[2] for r in rooms] + [r[4] for r in rooms]
    pad = 4
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad + 8
    W_ft, H_ft = x1 - x0, y1 - y0
    dpi = 200
    fig_w = a.width_px / dpi
    left, right, top, bot = 0.7, 0.25, 0.9, 0.6          # inches
    ax_w = fig_w - left - right
    ax_h = ax_w * H_ft / W_ft
    fig_h = ax_h + top + bot
    fig = plt.figure(figsize=(fig_w, fig_h), dpi=dpi)
    ax = fig.add_axes([left / fig_w, bot / fig_h, ax_w / fig_w, ax_h / fig_h])
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect("equal")
    in_per_ft = ax_w / W_ft
    pt_per_ft = in_per_ft * 72

    # grid
    gx0, gx1 = math.floor(x0 / 10) * 10, math.ceil(x1 / 10) * 10
    gy0, gy1 = math.floor(y0 / 10) * 10, math.ceil(y1 / 10) * 10
    ax.set_xticks(range(gx0, gx1 + 1, 10)); ax.set_yticks(range(gy0, gy1 + 1, 10))
    ax.grid(True, color="#9aa4b2", lw=0.45, alpha=0.55, zorder=0)
    ax.tick_params(labelsize=9, length=3)
    ax.set_xlabel("x, feet east of the garage west wall", fontsize=9); ax.set_ylabel("y, feet north of the front wall", fontsize=9)

    # rooms: draw big first so nested ones stay visible
    for r in sorted(rooms, key=lambda r: -(r[3] - r[1]) * (r[4] - r[2])):
        w, d = r[3] - r[1], r[4] - r[2]
        open_zone = r[5] == 0
        fc = KIND.get(r[6], "#f2f2f2")
        if r[6] in ("stairwell",):
            ax.add_patch(Rectangle((r[1], r[2]), w, d, fc="#ffffff", ec="#444", lw=1.0, hatch="////", zorder=1, alpha=0.9))
        else:
            ax.add_patch(Rectangle((r[1], r[2]), w, d, fc=fc, ec="#222" if not open_zone else "#7a7a7a", lw=1.8 if not open_zone else 1.0,
                                   ls="-" if not open_zone else (0, (4, 3)), zorder=1))
    # fixtures
    if not a.no_fixtures:
        for f in fixes:
            ax.add_patch(Rectangle((f[0], f[1]), f[2] - f[0], f[3] - f[1], fc="#c9ccd1", ec="#8d9199", lw=0.5, alpha=0.75, zorder=2))
    # windows
    for wd in wins:
        x, y, axis, w = wd[:4]
        xs_, ys_ = ([x, x + w], [y, y]) if axis == "x" else ([x, x], [y, y + w])
        ax.plot(xs_, ys_, color="#0b5fd6", lw=4.2, solid_capstyle="butt", zorder=6)
    # doors: gap then leaf + arc
    for d in doors:
        x, y, axis, w, kind = d[:5]
        sw = d[5] if len(d) > 5 else 1
        u = (1, 0) if axis == "x" else (0, 1)
        n = (0, sw) if axis == "x" else (sw, 0)
        xs_, ys_ = ([x, x + w], [y, y]) if axis == "x" else ([x, x], [y, y + w])
        if kind == "garage":
            ax.plot(xs_, ys_, color="#6b6b6b", lw=4, solid_capstyle="butt", zorder=5)
            continue
        ax.plot(xs_, ys_, color="#ffffff", lw=4.2, solid_capstyle="butt", zorder=4)          # gap in the wall
        if kind in ("slider", "glass"):
            ax.plot(xs_, ys_, color="#59a5d8", lw=1.6, solid_capstyle="butt", zorder=5)
        elif kind == "open":
            ax.plot(xs_, ys_, color="#555", lw=0.8, ls=(0, (2, 2)), zorder=5)
        elif kind == "full":
            pass
        else:
            leaves = [((x, y), u, n, w)] if kind == "door" else [((x, y), u, n, w / 2), ((x + w * u[0], y + w * u[1]), (-u[0], -u[1]), n, w / 2)]
            for (hx, hy), uu, nn, lw in leaves:
                ax.plot([hx, hx + lw * nn[0]], [hy, hy + lw * nn[1]], color="#7a4a22", lw=1.4, zorder=5)
                p = arc(hx, hy, uu, nn, lw)
                ax.plot([q[0] for q in p], [q[1] for q in p], color="#7a4a22", lw=0.7, zorder=5)

    # labels
    halo = [pe.withStroke(linewidth=2.2, foreground="white")]
    keyed = []
    placed = 0
    for r in rooms:
        lines = label_lines(r)
        w, d = r[3] - r[1], r[4] - r[2]
        area = w * d
        if not lines:
            if area > 40 and r[6] not in ("porch", "stairwell"):
                lines = [f"({r[6]})"]
            else:
                continue
        txt_variants = []
        full = lines + [f"{area:.0f} sf"]
        ab = [abbreviate(l) for l in lines] + [f"{area:.0f} sf"]
        one = [" ".join(lines) + f" {area:.0f}"]
        ab1 = [abbreviate(" ".join(lines)) + f" {area:.0f}"]
        for t in (full, ab, ab1):
            for rot in (0, 90):
                txt_variants.append((t, rot))
        best = None
        for t, rot in txt_variants:
            wl, dl = (w, d) if rot == 0 else (d, w)
            n = max(len(s_) for s_ in t); k = len(t)
            fs_w = (wl * pt_per_ft - 6) / (0.76 * n)
            fs_h = (dl * pt_per_ft - 5) / (1.3 * k)
            fs = min(fs_w, fs_h, MAX_PT + 1.5 * math.log(1 + area / 300))
            if best is None or fs > best[0] + 1e-9:
                best = (fs, t, rot)
            if fs >= MIN_PT + 1 and rot == 0:
                best = (fs, t, rot); break
        fs, t, rot = best
        cx, cy = (r[1] + r[3]) / 2, (r[2] + r[4]) / 2
        if len(r) > 9 and r[9] is not None and r[9][0] is not None:
            pass  # label_at in the model is for the 3D text; the plan label is centred
        if fs >= MIN_PT:
            ax.text(cx, cy, "\n".join(t), ha="center", va="center", fontsize=min(fs, MAX_PT + 2), rotation=rot,
                    color="#111", weight="bold", zorder=9, path_effects=halo, linespacing=1.1)
            placed += 1
        else:
            keyed.append((r, lines))
            num = len(keyed)
            ax.text(cx, cy, str(num), ha="center", va="center", fontsize=MIN_PT, color="#a00", weight="bold", zorder=9, path_effects=halo)
    if keyed:
        key = "KEY (room too small to label): " + "   ".join(
            f"{i+1} = {' '.join(l)} {((r[3]-r[1])*(r[4]-r[2])):.0f} sf" for i, (r, l) in enumerate(keyed))
        fig.text(0.01, 0.012, key, fontsize=9, color="#a00", wrap=True, va="bottom")

    # north arrow + legend
    nx, ny = x1 - 3.5, y1 - 9
    ax.add_patch(FancyArrow(nx, ny - 5, 0, 7, width=1.0, head_width=3.2, head_length=2.8, fc="#222", ec="#222", zorder=10))
    ax.text(nx, ny + 4.6, "N", ha="center", va="bottom", fontsize=14, weight="bold", zorder=10)
    ly = y1 - 2.0
    f = lambda t: x0 + W_ft * t
    ax.plot([f(0.02), f(0.07)], [ly, ly], color="#0b5fd6", lw=4.2, zorder=10)
    ax.text(f(0.08), ly, "window", va="center", fontsize=9)
    ax.plot([f(0.18), f(0.23)], [ly, ly], color="#7a4a22", lw=1.4, zorder=10)
    ax.text(f(0.24), ly, "door leaf + swing", va="center", fontsize=9)
    ax.add_patch(Rectangle((f(0.42), ly - 0.8), W_ft * 0.04, 1.6, fc="#c9ccd1", ec="#8d9199", zorder=10))
    ax.text(f(0.47), ly, "fixture / furniture", va="center", fontsize=9)
    ax.text(f(0.02), ly - 3.2, "area = wall centre-line W x D; dashed outline = open zone / porch (no walls)", va="center", fontsize=9, color="#444")
    title = a.title or f"{a.scad}"
    fig.suptitle(title, fontsize=17, weight="bold", y=1 - 0.12 / fig_h * 1.0, x=0.5)
    fig.savefig(a.out, dpi=dpi)
    print(f"{a.out}: {int(fig_w*dpi)}x{int(fig_h*dpi)} px, {placed} labelled, {len(keyed)} keyed")


if __name__ == "__main__":
    main()
