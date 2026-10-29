#!/usr/bin/env python3
"""Layout checker for the house models (needs `openscad` on PATH).

Runs each level file with -D audit=true, reads the room / door / window /
fixture tables it echoes, and checks that:
  * every door or opening lies on a room's wall line and has the same
    room on each side along its whole width (no doors into voids or
    outside, except garage doors, and no cuts into a neighbouring room);
  * every door leaf swings clear of walls, fixtures and other leaves;
  * every room is reachable from the foyer (main floor) or the rec room
    (basement) without going outside;
  * no door overlaps a window, and every window has walls on one side only;
  * rooms don't overlap and leave no thin voids between them.
The main floor is checked with the changes on and off.

    python3 tools/check_layout.py             # both levels
    python3 tools/check_layout.py basement.scad
"""
import ast
import math
import re
import subprocess
import sys
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = {
    "main_floor.scad": [[], ["-D", "changes=false"]],
    "basement.scad": [[]],
}
# rooms deliberately drawn inside another room (own floor level or no plate)
NESTED_OK = {("GARAGE", "STORAGE"), ("GARAGE", "STAIR DN"), ("REC ROOM / LIBRARY", "STAIR UP"), ("", "STAIR UP")}


def tables(scad, extra):
    out = subprocess.run(
        ["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", *extra, str(scad)],
        capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$",
                  out.stdout + out.stderr, re.M)
    if not m:
        sys.exit(f"{scad}: no audit output\n{out.stderr}")
    lit = lambda s: ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))
    return [lit(g) for g in m.groups()]


def label(r):
    return " ".join(r[0]) if isinstance(r[0], list) else r[0]


def name(r):
    return f"{label(r) or '(unlabelled)'} @ {r[1]:g},{r[2]:g}"


def rooms_at(rooms, x, y):
    """Rooms containing (x, y), innermost (smallest) first."""
    hits = [r for r in rooms if r[1] < x < r[3] and r[2] < y < r[4]]
    return sorted(hits, key=lambda r: (r[3] - r[1]) * (r[4] - r[2]))


def sides(rooms, x, y, axis, w):
    """Innermost room on each side of an opening's midpoint."""
    if axis == "x":
        cx, cy = x + w / 2, y
        a, b = rooms_at(rooms, cx, cy - 0.8), rooms_at(rooms, cx, cy + 0.8)
    else:
        cx, cy = x, y + w / 2
        a, b = rooms_at(rooms, cx - 0.8, cy), rooms_at(rooms, cx + 0.8, cy)
    return (a[0] if a else None), (b[0] if b else None)


def side_pairs(rooms, x, y, axis, w):
    """The (innermost) rooms either side of an opening, sampled along its width."""
    pairs = set()
    for i in range(int(w / 0.1) + 1):
        s = 0.05 + (w - 0.1) * i / max(1, int(w / 0.1))
        if axis == "x":
            a, b = rooms_at(rooms, x + s, y - 0.3), rooms_at(rooms, x + s, y + 0.3)
        else:
            a, b = rooms_at(rooms, x - 0.3, y + s), rooms_at(rooms, x + 0.3, y + s)
        pairs.add((name(a[0]) if a else None, name(b[0]) if b else None))
    return pairs


def leaf_sweep(d, step=0.15):
    """Points swept by a door's leaf (both leaves of a double door) as it opens."""
    x, y, axis, w, kind = d[:5]
    s = d[5] if len(d) > 5 else 1
    u, n = ((1, 0), (0, s)) if axis == "x" else ((0, 1), (s, 0))
    leaves = {"door": [((x, y), u, w)],
              "double": [((x, y), u, w / 2), ((x + w * u[0], y + w * u[1]), (-u[0], -u[1]), w / 2)]}
    pts = []
    for (hx, hy), (ux, uy), lw in leaves.get(kind, []):
        for i in range(1, int(lw / step) + 1):
            for j in range(11):
                c, sn = math.cos(math.pi / 20 * j), math.sin(math.pi / 20 * j)
                px, py = hx + i * step * (c * ux + sn * n[0]), hy + i * step * (c * uy + sn * n[1])
                if (abs(py - y) if axis == "x" else abs(px - x)) > 0.25:   # clear of its own wall
                    pts.append((px, py))
    return pts


def wall_at(rooms, doors, px, py):
    """The room whose wall (0.4 ft thick, centred on its edge) is at (px, py), unless cut open there."""
    for r in rooms:
        if r[5] <= 0:
            continue
        for axis, line, a, b in (("x", r[2], r[1], r[3]), ("x", r[4], r[1], r[3]),
                                 ("y", r[1], r[2], r[4]), ("y", r[3], r[2], r[4])):
            along, across = (px, py) if axis == "x" else (py, px)
            if abs(across - line) < 0.2 and a - 0.2 <= along <= b + 0.2 and not any(
                    d[2] == axis and abs(d[1 if axis == "x" else 0] - line) < 0.05
                    and d[0 if axis == "x" else 1] <= along <= d[0 if axis == "x" else 1] + d[3]
                    for d in doors):
                return name(r)
    return None


def on_wall_line(rooms, x, y, axis, w):
    for r in rooms:
        if axis == "x" and min(abs(y - r[2]), abs(y - r[4])) < 0.05 and r[1] - 0.05 <= x and x + w <= r[3] + 0.05:
            return True
        if axis == "y" and min(abs(x - r[1]), abs(x - r[3])) < 0.05 and r[2] - 0.05 <= y and y + w <= r[4] + 0.05:
            return True
    return False


def check(scad, extra):
    rooms, doors, windows, fixtures = tables(scad, extra)
    problems = []
    graph = defaultdict(set)
    sweeps = {}
    for d in doors:
        x, y, axis, w, kind = d[:5]
        a, b = sides(rooms, x, y, axis, w)
        if not on_wall_line(rooms, x, y, axis, w):
            problems.append(f"door {d} is not on a wall line")
        if kind != "garage" and (a is None or b is None):
            problems.append(f"door {d} opens to nothing ({a and name(a)} | {b and name(b)})")
        elif a is b and a is not None:
            problems.append(f"door {d} has the same room on both sides")
        pairs = side_pairs(rooms, x, y, axis, w)
        if len(pairs) > 1:
            problems.append(f"door {d} runs past the rooms it joins: {sorted(pairs, key=str)}")
        if a and b:
            graph[name(a)].add(name(b))
            graph[name(b)].add(name(a))
        # the leaf's swing: walls, fixtures (anything standing above the floor), other leaves
        pts = leaf_sweep(d)
        walls = {wall_at(rooms, doors, px, py) for px, py in pts} - {None}
        hits = {tuple(f[:6]) for f in fixtures for px, py in pts
                if f[5] > 0.1 and f[4] < 7 and f[0] < px < f[2] and f[1] < py < f[3]}
        problems += [f"door {d} swings into the wall of {r}" for r in sorted(walls)]
        problems += [f"door {d} swings into fixture {list(f)}" for f in sorted(hits)]
        sweeps[str(d)] = {(round(px * 4), round(py * 4)) for px, py in pts}
    for (da, sa), (db, sb) in combinations(sweeps.items(), 2):
        if len(sa & sb) > 5:
            problems.append(f"doors {da} and {db} swing into each other")
    for d in doors:
        for win in windows:
            line_d = d[1] if d[2] == "x" else d[0]
            line_w = win[1] if win[2] == "x" else win[0]
            span = lambda o: (o[0], o[0] + o[3]) if o[2] == "x" else (o[1], o[1] + o[3])
            (s0, s1), (t0, t1) = span(d), span(win)
            if d[2] == win[2] and abs(line_d - line_w) < 0.05 and s0 < t1 and t0 < s1:
                problems.append(f"door {d} overlaps window {win}")
    for win in windows:
        a, b = sides(rooms, *win[:4])
        walled = [r for r in (a, b) if r and r[5] > 0]
        if not walled:
            problems.append(f"window {win} has no wall")
        elif len(walled) == 2:
            problems.append(f"window {win} is between {name(a)} and {name(b)}")
    # reachability without going outside (porches excluded)
    inside = {name(r) for r in rooms if r[6] != "porch"}
    start = next((name(r) for r in rooms if label(r) == "FOYER" or label(r).startswith("REC ROOM")),
                 name(rooms[0]))
    seen, todo = {start}, deque([start])
    while todo:
        for nxt in graph[todo.popleft()]:
            if nxt in inside and nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    lost = sorted(inside - seen)
    if lost:
        problems.append(f"not reachable from {start} without going outside: {lost}")
    # overlaps and thin voids, sampled on a 0.25 ft grid
    x0, x1 = min(r[1] for r in rooms), max(r[3] for r in rooms)
    y0, y1 = min(r[2] for r in rooms), max(r[4] for r in rooms)
    overlaps, voids = set(), set()
    for i in range(int((x1 - x0) / 0.25)):
        for j in range(int((y1 - y0) / 0.25)):
            x, y = x0 + 0.125 + i * 0.25, y0 + 0.125 + j * 0.25
            hits = rooms_at(rooms, x, y)
            if len(hits) > 1:
                pair = (label(hits[-1]), label(hits[0]))
                if pair not in NESTED_OK:
                    overlaps.add(" / ".join(name(h) for h in hits))
            elif not hits and ((rooms_at(rooms, x - 1.6, y) and rooms_at(rooms, x + 1.6, y))
                               or (rooms_at(rooms, x, y - 1.6) and rooms_at(rooms, x, y + 1.6))):
                voids.add((round(x), round(y)))
    problems += [f"rooms overlap: {o}" for o in sorted(overlaps)]
    if voids:
        problems.append(f"thin voids between rooms near {sorted(voids)[:12]}")
    tag = " ".join(extra) or "(defaults)"
    print(f"{scad.name} {tag}: {len(rooms)} rooms, {len(doors)} doors, {len(windows)} windows - "
          f"{'OK' if not problems else f'{len(problems)} problem(s)'}")
    for p in problems:
        print("   ", p)
    return len(problems)


def main():
    files = sys.argv[1:] or list(VARIANTS)
    total = 0
    for f in files:
        scad = (ROOT / f) if not Path(f).is_absolute() else Path(f)
        for extra in VARIANTS.get(scad.name, [[]]):
            total += check(scad, extra)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
