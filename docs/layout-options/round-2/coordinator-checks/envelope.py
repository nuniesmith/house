#!/usr/bin/env python3
"""Coordinator check: heated envelope perimeter and corners, outside face.
Usage: envelope.py MAIN.scad [BASE.scad]  (same audit + 0.5 ft offset as plan_facts.py)"""
import ast, re, subprocess, sys
from shapely.geometry import box
from shapely.ops import unary_union
OFFSET = 0.5
def lit(s):
    return ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))
def audit(scad):
    r = subprocess.run(["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", str(scad)],
                       capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$", r.stdout + r.stderr, re.M)
    return [lit(g) for g in m.groups()]
def rect(r):
    return min(r[1], r[3]), min(r[2], r[4]), max(r[1], r[3]), max(r[2], r[4])
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
    return cx, rx
def union(rooms, keep):
    u = unary_union([box(*rect(r)).buffer(0.01, join_style=2) for r in rooms if keep(r)]).buffer(-0.01, join_style=2)
    return u
def report(tag, u):
    o = u.buffer(OFFSET, join_style=2)
    polys = list(o.geoms) if o.geom_type == "MultiPolygon" else [o]
    big = max(polys, key=lambda p: p.area)
    cx, rx = corners(big)
    minx, miny, maxx, maxy = big.bounds
    print(f"{tag}: area {o.area:,.0f} sq ft; perimeter {big.exterior.length:.1f} ft; corners {cx + rx} ({cx} out, {rx} in); "
          f"bbox {maxx-minx:.1f} x {maxy-miny:.1f} ft; pieces {len(polys)}; holes {sum(len(p.interiors) for p in polys)}")
rooms = audit(sys.argv[1])[0]
report("main heated (excl. garage, porch)", union(rooms, lambda r: r[6] not in ("porch", "garage")))
gar = [r for r in rooms if r[6] == "garage"]
if gar:
    report("garage", union(rooms, lambda r: r[6] == "garage"))
if len(sys.argv) > 2:
    b = audit(sys.argv[2])[0]
    report("basement (excl. porch, EXIT STAIR)", union(b, lambda r: r[6] != "porch" and (" ".join(r[0]) if isinstance(r[0], list) else r[0]) != "EXIT STAIR"))
