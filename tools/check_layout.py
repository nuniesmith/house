#!/usr/bin/env python3
"""Layout checker for the house models (needs `openscad` on PATH).

Runs each level file with -D audit=true, reads the room / door / window
tables it echoes, and checks that:
  * every door or opening lies on a room's wall line and has a room on
    both sides (no doors into voids or outside, except garage doors);
  * every room is reachable from the foyer (main floor) or the rec room
    (basement) without going outside;
  * no door overlaps a window, and every window has walls on one side only;
  * rooms don't overlap and leave no thin voids between them.
Each level is checked in every stair / changes variant.

    python3 tools/check_layout.py             # both levels
    python3 tools/check_layout.py basement.scad
"""
import ast
import re
import subprocess
import sys
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = {
    "main_floor.scad": [[], ["-D", "changes=false"], ["-D", 'stair="as_drawn"']],
    "basement.scad": [[], ["-D", 'stair="as_drawn"']],
}
# rooms deliberately drawn inside another room (own floor level or no plate)
NESTED_OK = {("GARAGE", "STORAGE"), ("GARAGE", "STAIR DN"), ("REC ROOM", "STAIR UP"), ("", "STAIR UP")}


def tables(scad, extra):
    out = subprocess.run(
        ["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", *extra, str(scad)],
        capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*)$", out.stdout + out.stderr, re.M)
    if not m:
        sys.exit(f"{scad}: no audit output\n{out.stderr}")
    lit = lambda s: ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))
    return lit(m.group(1)), lit(m.group(2)), lit(m.group(3))


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


def on_wall_line(rooms, x, y, axis, w):
    for r in rooms:
        if axis == "x" and min(abs(y - r[2]), abs(y - r[4])) < 0.05 and r[1] - 0.05 <= x and x + w <= r[3] + 0.05:
            return True
        if axis == "y" and min(abs(x - r[1]), abs(x - r[3])) < 0.05 and r[2] - 0.05 <= y and y + w <= r[4] + 0.05:
            return True
    return False


def check(scad, extra):
    rooms, doors, windows = tables(scad, extra)
    problems = []
    graph = defaultdict(set)
    for d in doors:
        x, y, axis, w, kind = d[:5]
        a, b = sides(rooms, x, y, axis, w)
        if not on_wall_line(rooms, x, y, axis, w):
            problems.append(f"door {d} is not on a wall line")
        if kind != "garage" and (a is None or b is None):
            problems.append(f"door {d} opens to nothing ({a and name(a)} | {b and name(b)})")
        elif a is b and a is not None:
            problems.append(f"door {d} has the same room on both sides")
        if a and b:
            graph[name(a)].add(name(b))
            graph[name(b)].add(name(a))
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
    start = next((name(r) for r in rooms if label(r) in ("FOYER", "REC ROOM")), name(rooms[0]))
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
