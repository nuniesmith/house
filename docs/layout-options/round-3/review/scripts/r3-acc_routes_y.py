#!/usr/bin/env python3
"""Coordinator check (round 3): daily routes and the living rooms they pass through.

Usage: routes.py MAIN.scad [--md] [--extended]

--extended adds four living-room trips: front door -> living, front door -> dining,
kitchen -> living, dining -> living (the "linear row" test).

Loads the main floor through OpenSCAD's audit echo (same as plan_facts.py), links rooms through
their doors and openings, and finds the shortest walk between room centres via door midpoints
(Dijkstra, straight lines inside each room). For each daily route it reports the walk in feet and
the living rooms it passes THROUGH (start and end rooms excluded). Living rooms = room kinds
living, kitchen, dining, office, plus any label with DINING / NOOK / LIBRARY.
"""
import ast, heapq, math, re, subprocess, sys
from collections import defaultdict

def lit(s):
    return ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))

def audit(scad):
    r = subprocess.run(["openscad", "-o", "/dev/stdout", "--export-format", "echo", "-D", "audit=true", str(scad)],
                       capture_output=True, text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$", r.stdout + r.stderr, re.M)
    return [lit(g) for g in m.groups()]

def label(r):
    return (" ".join(r[0]) if isinstance(r[0], list) else r[0]).strip()

def rect(r):
    return min(r[1], r[3]), min(r[2], r[4]), max(r[1], r[3]), max(r[2], r[4])

LIVING_KINDS = {"living", "kitchen", "dining", "office"}
def is_living(r):
    return r[6] in LIVING_KINDS or re.search(r"DINING|NOOK|LIBRARY", label(r), re.I) is not None

def main(path, md=False, extended=False):
    rooms, doors = audit(path)[:2]
    import os
    if os.environ.get("NODOOR"): doors=[d for d in doors if (d[0],d[1])!=(83,37)]
    R = [r for r in rooms if r[6] not in ("porch",)]
    def room_at(px, py):
        best = None
        for i, r in enumerate(R):
            x0, y0, x1, y1 = rect(r)
            if x0 < px < x1 and y0 < py < y1:
                a = (x1 - x0) * (y1 - y0)
                if best is None or a < best[0]:
                    best = (a, i)
        return None if best is None else best[1]
    # graph nodes: ("c", i) room centre, ("d", k) door midpoint
    pos, adj = {}, defaultdict(list)
    room_doors = defaultdict(list)
    for i, r in enumerate(R):
        x0, y0, x1, y1 = rect(r)
        pos[("c", i)] = ((x0 + x1) / 2, (y0 + y1) / 2)
    for k, d in enumerate(doors):
        x, y, ax, w = d[0], d[1], d[2], d[3]
        if ax == "x":
            mx, my = x + w / 2, y
            a, b = room_at(mx, y - 0.25), room_at(mx, y + 0.25)
        else:
            mx, my = x, y + w / 2
            a, b = room_at(x - 0.25, my), room_at(x + 0.25, my)
        pos[("d", k)] = (mx, my)
        for i in (a, b):
            if i is not None:
                room_doors[i].append(k)
    dist = lambda p, q: math.hypot(pos[p][0] - pos[q][0], pos[p][1] - pos[q][1])
    for i, ks in room_doors.items():
        nodes = [("c", i)] + [("d", k) for k in ks]
        for u in nodes:
            for v in nodes:
                if u != v:
                    adj[u].append((v, dist(u, v), i))
    def route(i, j):
        start, goal = ("c", i), ("c", j)
        best = {start: 0.0}; prev = {}
        pq = [(0.0, start)]
        while pq:
            d0, u = heapq.heappop(pq)
            if u == goal:
                break
            if d0 > best.get(u, 1e18):
                continue
            for v, w, room in adj[u]:
                # only enter a room centre if it is the goal (no shortcuts through centres)
                if v[0] == "c" and v != goal:
                    continue
                nd = d0 + w
                if nd < best.get(v, 1e18):
                    best[v] = nd; prev[v] = (u, room); heapq.heappush(pq, (nd, v))
        if goal not in best:
            return None, []
        through, u = [], goal
        while u != start:
            u, room = prev[u]
            through.append(room)
        through = list(dict.fromkeys(reversed(through)))
        mid = [R[x] for x in through if x not in (i, j)]
        return best[goal], [label(r) or r[6] for r in mid if is_living(r)]
    def find(pat, kinds=None, largest=False):
        c = [i for i, r in enumerate(R) if re.search(pat, label(r), re.I) and (kinds is None or r[6] in kinds)]
        if not c:
            return None
        if largest:
            c.sort(key=lambda i: -(rect(R[i])[2] - rect(R[i])[0]) * (rect(R[i])[3] - rect(R[i])[1]))
        return c[0]
    pts = {
        "garage": find(r"GARAGE"),
        "kitchen": find(r"KITCHEN"),
        "primary": find(r"MASTER|PRIMARY", {"bed"}, True) if find(r"MASTER|PRIMARY", {"bed"}) is not None else find(r"BED", {"bed"}, True),
        "bedroom 2": find(r"BEDROOM 2|BR ?2|BED ?2"),
        "front door": find(r"VESTIBULE") if find(r"VESTIBULE") is not None else find(r"FOYER"),
        "foyer": find(r"FOYER"),
        "powder": find(r"POWDER"),
        "shared bath": find(r"SHARED BATH"),
        "ensuite": find(r"ENSUITE"),
        "mudroom": find(r"MUDROOM"),
        "library": find(r"LIBRARY|OFFICE|STUDY"),
        "laundry": find(r"LAUNDRY|LDRY"),
        "lift": find(r"ELEVATOR|LIFT"),
        "living": find(r"LIVING|GREAT ROOM", {"living"}, True),
        "dining": find(r"DINING|NOOK|BREAKFAST"),
    }
    routes = [("garage", "kitchen"), ("garage", "primary"), ("front door", "primary"), ("front door", "kitchen"),
              ("front door", "library"), ("primary", "kitchen"), ("bedroom 2", "kitchen"), ("primary", "laundry"),
              ("lift", "kitchen"), ("lift", "primary")]
    if "--x2" in sys.argv:
        routes = [("front door","primary"),("front door","kitchen"),("front door","library"),("front door","living"),("front door","dining"),("front door","powder"),("garage","powder"),("library","powder"),("kitchen","powder"),("garage","living"),("garage","dining"),("garage","laundry"),("laundry","primary"),("primary","ensuite"),("bedroom 2","shared bath"),("primary","library"),("primary","powder"),("lift","garage"),("mudroom","dining"),("kitchen","dining"),("primary","front door"),("garage","library")]
    elif extended:
        routes += [("front door", "living"), ("front door", "dining"), ("kitchen", "living"), ("dining", "living")]
    rows, total_d, total_t = [], 0.0, 0
    for a, b in routes:
        if pts.get(a) is None or pts.get(b) is None:
            rows.append((f"{a} → {b}", "—", "not on this floor")); continue
        d, thr = route(pts[a], pts[b])
        if d is None:
            rows.append((f"{a} → {b}", "—", "no route")); continue
        total_d += d; total_t += len(thr)
        rows.append((f"{a} → {b}", f"{d:.0f} ft", ", ".join(thr) if thr else "none"))
    if md:
        print("| Route | Walk | Living rooms passed through |\n|---|---|---|")
        for r in rows:
            print(f"| {r[0]} | {r[1]} | {r[2]} |")
        print(f"| **Total** | **{total_d:.0f} ft** | **{total_t} pass-throughs** |")
    else:
        for r in rows:
            print(f"{r[0]:<24} {r[1]:>7}   {r[2]}")
        print(f"{'TOTAL':<24} {total_d:>4.0f} ft   {total_t} pass-throughs")

if __name__ == "__main__":
    main(sys.argv[1], "--md" in sys.argv, "--extended" in sys.argv or "--x2" in sys.argv)
