#!/usr/bin/env python3
"""Drawing set for engineering review and permit preparation.

Reads the model through models/export.scad (tools/model_data.py) and
writes, in docs/permit/:

  House-Drawing-Set.pdf    24 x 36 in (ARCH D) sheets; plans at 3/16" = 1'-0"
  cad/*.dxf                the plans as CAD files (inches, layered)
  schedules/*.csv          door, window and room schedules

Elevations, sections, the roof plan and the site plan are OpenSCAD
renders. They are made here and cached in build/renders/ until a model
file changes (delete the folder to force new ones).

    python3 tools/make_drawings.py       # needs openscad (+ xvfb-run when
                                         # headless), matplotlib, shapely, ezdxf

Everything is drawn from the model's tables, so the set stays in step
with the model. NOT FOR CONSTRUCTION: structure, reinforcement and
connections are for the engineer to design.
"""
import csv
import datetime
import hashlib
import math
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from math import gcd
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                   # noqa: E402
from matplotlib.backends.backend_pdf import PdfPages             # noqa: E402
from matplotlib.patches import Arc, Circle, PathPatch, Polygon as MPoly, Rectangle  # noqa: E402
from matplotlib.path import Path as MPath                        # noqa: E402
import ezdxf                                                     # noqa: E402
from shapely.geometry import box, Polygon, LineString           # noqa: E402
from shapely.ops import unary_union                              # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model_data import load                                      # noqa: E402

matplotlib.rcParams["hatch.linewidth"] = 0.3
matplotlib.rcParams["pdf.fonttype"] = 42

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "permit"
CACHE = ROOT / "build" / "renders"
SHEET_W, SHEET_H = 36.0, 24.0            # inches, ARCH D landscape
TB_W = 4.6                               # title block strip
DRAW = (0.6, 0.6, SHEET_W - 0.5 - TB_W - 0.7, SHEET_H - 1.2)   # drawing area x, y, w, h
PROJECT = "NEW SINGLE-FAMILY DWELLING"
PROJECT_2 = "Attached garage, full ICF basement, indoor pool + spa"
SITE_TXT = "Rural Alberta - legal land description: TBD"
DATE = datetime.date.today().isoformat()
INK = "#1a1a1a"
GREY = "#8c8c8c"
LIGHT = "#bdbdbd"
RED = "#b00000"
BLUE = "#1f4e9e"
GREEN = "#2e6b2e"
POCHE = "#a6a6a6"

# scales, as feet of model per inch of sheet
S316, S18, S14, S38, S12, S34 = 16 / 3, 8.0, 4.0, 8 / 3, 2.0, 4 / 3
S_SITE = 20.0
SCALE_TXT = {S316: '3/16" = 1\'-0"', S18: '1/8" = 1\'-0"', S14: '1/4" = 1\'-0"',
             S38: '3/8" = 1\'-0"', S12: '1/2" = 1\'-0"', S34: '3/4" = 1\'-0"', S_SITE: '1" = 20\'-0"'}


# ============================================================ small helpers

def ftin(v, frac=8):
    """Feet as feet-inches, rounded to 1/8"."""
    neg = v < -1e-9
    t = round(abs(v) * 12 * frac) / frac
    f = int(t // 12)
    i = t - 12 * f
    w = int(i)
    n = round((i - w) * frac)
    s = f"{f}'-{w}"
    if n:
        g = gcd(n, frac)
        s += f" {n // g}/{frac // g}"
    return ("-" if neg else "") + s + '"'


def el(z):
    return "EL. " + ("+" if z > 1e-9 else "") + ftin(z)


def label_of(r):
    return " ".join(r[0]) if isinstance(r[0], list) else r[0]


def rbox(r):
    return box(r[1], r[2], r[3], r[4])


def opening_box(o, depth=1.0):
    x, y, a, w = o[0], o[1], o[2], o[3]
    return box(x, y - depth, x + w, y + depth) if a == "x" else box(x - depth, y, x + depth, y + w)


def opening_mid(o):
    x, y, a, w = o[:4]
    return (x + w / 2, y) if a == "x" else (x, y + w / 2)


def strip(s, w):
    """A strip w wide along the axis-aligned segment s = [x0, y0, x1, y1, ...] (as foundation.scad)."""
    return box(min(s[0], s[2]) - w / 2, min(s[1], s[3]) - w / 2, max(s[0], s[2]) + w / 2, max(s[1], s[3]) + w / 2)


def polys(g):
    if g is None or g.is_empty:
        return []
    if g.geom_type == "Polygon":
        return [g]
    return [p for p in getattr(g, "geoms", []) if p.geom_type == "Polygon"]


def reading_order(n, xy, row=12.0):
    """Indices 0..n-1 in reading order: rows from the north, west to east within a row."""
    return sorted(range(n), key=lambda i: (-math.floor(xy(i)[1] / row), xy(i)[0]))


def m2(ft2):
    return ft2 * 0.09290304


def wrap(text, n):
    lines, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)
    return lines


def chars_for(width_in, fs):
    return int(width_in / (fs * 0.56 / 72) * 0.95)


def bullets(items, n):
    out = []
    for it in items:
        if it.startswith("**"):
            out.append(it)
            continue
        ws = wrap(it, n - 2)
        out.append("- " + ws[0])
        out += ["  " + w for w in ws[1:]]
    return out


# ============================================================ canvases
# Plans are drawn once against a small canvas API with two back ends:
# matplotlib (the PDF sheets) and ezdxf (the CAD files).

class Mpl:
    def __init__(self, ax, fpi):
        self.ax, self.fpi = ax, fpi

    def geom(self, g, layer, fc="none", ec=INK, lw=0.5, ls="-", hatch=None, z=3, alpha=1.0):
        for p in polys(g):
            verts, codes = [], []
            for ring in [p.exterior] + list(p.interiors):
                c = list(ring.coords)
                verts += c
                codes += [MPath.MOVETO] + [MPath.LINETO] * (len(c) - 2) + [MPath.CLOSEPOLY]
            self.ax.add_patch(PathPatch(MPath(verts, codes), fc=fc, ec=ec, lw=lw, ls=ls, hatch=hatch,
                                        zorder=z, alpha=alpha))

    def line(self, pts, layer, color=INK, lw=0.5, ls="-", z=4):
        xs, ys = zip(*pts)
        self.ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="butt")

    def arc(self, c, r, t1, t2, layer, color=INK, lw=0.3, ls="-", z=5):
        self.ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, color=color, lw=lw, ls=ls, zorder=z))

    def circle(self, c, r, layer, fc="none", ec=INK, lw=0.4, ls="-", z=4):
        self.ax.add_patch(Circle(c, r, fc=fc, ec=ec, lw=lw, ls=ls, zorder=z))

    def text(self, x, y, s, layer, size=6, ha="center", va="center", rot=0, weight="normal",
             color=INK, boxed=None, z=7, bg=False):
        kw = {}
        if boxed:
            kw["bbox"] = dict(fc="white", ec=boxed, lw=0.35, boxstyle="round,pad=0.15")
        elif bg:
            kw["bbox"] = dict(fc="white", ec="none", alpha=0.85, pad=0.4)
        self.ax.text(x, y, s, fontsize=size, ha=ha, va=va, rotation=rot, weight=weight, color=color,
                     zorder=z, linespacing=1.15, rotation_mode="anchor", **kw)

    def leader(self, p, t, s, layer, size=5.6, ha="left", color=INK):
        self.ax.annotate(s, xy=p, xytext=t, fontsize=size, ha=ha, va="center", color=color, zorder=8,
                         linespacing=1.15,
                         arrowprops=dict(arrowstyle="-", lw=0.35, color=color, shrinkA=1, shrinkB=0),
                         bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.5))
        self.ax.add_patch(Circle(p, 0.035 * self.fpi, fc=color, ec="none", zorder=8))

    def dim(self, p1, p2, off, layer, text=None, size=5.5, color=INK, z=6, ext=True):
        """Aligned dimension p1 -> p2, its line `off` ft to the left of the direction p1 -> p2."""
        (x1, y1), (x2, y2) = p1, p2
        L = math.hypot(x2 - x1, y2 - y1)
        if L < 1e-6:
            return
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        nx, ny = -uy, ux
        s = 1 if off >= 0 else -1
        a = (x1 + nx * off, y1 + ny * off)
        b = (x2 + nx * off, y2 + ny * off)
        gap, over = 0.03 * self.fpi, 0.05 * self.fpi
        if ext:
            for (px, py), (qx, qy) in (((x1, y1), a), ((x2, y2), b)):
                if abs(off) > gap:
                    self.ax.plot([px + nx * gap * s, qx + nx * over * s], [py + ny * gap * s, qy + ny * over * s],
                                 color=color, lw=0.2, zorder=z)
        self.ax.plot([a[0] - ux * over, b[0] + ux * over], [a[1] - uy * over, b[1] + uy * over],
                     color=color, lw=0.3, zorder=z)
        tk = 0.06 * self.fpi
        for (qx, qy) in (a, b):
            self.ax.plot([qx - (ux + nx) * tk / 2, qx + (ux + nx) * tk / 2],
                         [qy - (uy + ny) * tk / 2, qy + (uy + ny) * tk / 2], color=color, lw=0.8, zorder=z)
        ang = math.degrees(math.atan2(uy, ux))
        flip = ang > 90.1 or ang < -89.9
        if flip:
            ang += 180
        up = (nx, ny) if not flip else (-nx, -ny)
        g = 0.025 * self.fpi
        mx, my = (a[0] + b[0]) / 2 + up[0] * g, (a[1] + b[1]) / 2 + up[1] * g
        self.ax.text(mx, my, text or ftin(L), fontsize=size, rotation=ang, ha="center", va="bottom",
                     color=color, zorder=z, rotation_mode="anchor")

    def chain_dim(self, pa, pb, axis, at, layer, size=5.0, ext_from=None, text=None):
        """A dimension along `axis` between pa and pb, its line at coordinate `at`, with
        extension lines from the points (or from the coordinate ext_from)."""
        k = 0 if axis == "x" else 1
        lo, hi = sorted([pa, pb], key=lambda p: p[k])
        for p in (lo, hi):
            start = p[1 - k] if ext_from is None else ext_from
            sgn = 1 if at > start else -1
            g, o = 0.03 * self.fpi, 0.05 * self.fpi
            if axis == "x":
                self.line([(p[0], start + sgn * g), (p[0], at + sgn * o)], layer, color=GREY, lw=0.18, z=6)
            else:
                self.line([(start + sgn * g, p[1]), (at + sgn * o, p[1])], layer, color=GREY, lw=0.18, z=6)
        if axis == "x":
            self.dim((lo[0], at), (hi[0], at), 0, layer, text=text, size=size, ext=False)
        else:
            self.dim((at, lo[1]), (at, hi[1]), 0, layer, text=text, size=size, ext=False)


class Dxf:
    """The same calls into a DXF modelspace, in inches (1 ft = 12)."""
    LAYERS = {
        "A-WALL": (7, "Continuous"), "A-WALL-PATT": (8, "Continuous"), "A-DOOR": (3, "Continuous"),
        "A-GLAZ": (5, "Continuous"), "A-AREA": (9, "Continuous"), "A-ANNO-TEXT": (7, "Continuous"),
        "A-ANNO-DIMS": (1, "Continuous"), "A-ANNO-MARK": (6, "Continuous"), "A-FLOR-FIXT": (8, "Continuous"),
        "A-FLOR-STRS": (2, "Continuous"), "A-FLOR-OVHD": (8, "DASHED"), "S-FNDN": (7, "Continuous"),
        "S-FNDN-PATT": (8, "Continuous"), "S-FTNG": (4, "DASHED"), "S-POOL": (5, "Continuous"),
        "S-SLAB": (8, "Continuous"), "S-PIER": (4, "Continuous"), "S-BEAM": (1, "DASHED"),
        "S-ANNO": (7, "Continuous"),
    }

    def __init__(self, fpi):
        self.doc = ezdxf.new("R2010", setup=True)
        self.doc.units = ezdxf.units.IN
        for name, (color, lt) in self.LAYERS.items():
            self.doc.layers.add(name, color=color, linetype=lt)
        self.msp = self.doc.modelspace()
        self.fpi = fpi
        ds = self.doc.dimstyles.new("ARCH")
        ds.dxf.dimtxt = self.pt(5.5)
        ds.dxf.dimtsz = self.pt(4)
        ds.dxf.dimexo = self.pt(3)
        ds.dxf.dimexe = self.pt(3)
        ds.dxf.dimgap = self.pt(1.5)
        ds.dxf.dimtad = 1
        ds.dxf.dimtih = 0
        ds.dxf.dimtoh = 0

    def pt(self, size):          # a text size in points at the plot scale -> model inches
        return size / 72 * self.fpi * 12

    @staticmethod
    def P(p):
        return (p[0] * 12, p[1] * 12)

    @staticmethod
    def _lt(ls):
        return {} if ls in ("-", "solid") else {"linetype": "DASHED"}

    def geom(self, g, layer, fc="none", ec=INK, lw=0.5, ls="-", hatch=None, z=3, alpha=1.0):
        for p in polys(g):
            for ring in [p.exterior] + list(p.interiors):
                self.msp.add_lwpolyline([self.P(c) for c in ring.coords], close=True,
                                        dxfattribs={"layer": layer, **self._lt(ls)})
            if fc not in ("none", None, "white") and layer in ("A-WALL", "S-FNDN"):
                h = self.msp.add_hatch(color=8, dxfattribs={"layer": layer + "-PATT"})
                h.paths.add_polyline_path([self.P(c) for c in p.exterior.coords], is_closed=True, flags=1)
                for hole in p.interiors:
                    h.paths.add_polyline_path([self.P(c) for c in hole.coords], is_closed=True, flags=0)

    def line(self, pts, layer, color=INK, lw=0.5, ls="-", z=4):
        self.msp.add_lwpolyline([self.P(c) for c in pts], dxfattribs={"layer": layer, **self._lt(ls)})

    def arc(self, c, r, t1, t2, layer, color=INK, lw=0.3, ls="-", z=5):
        self.msp.add_arc(self.P(c), r * 12, t1, t2, dxfattribs={"layer": layer})

    def circle(self, c, r, layer, fc="none", ec=INK, lw=0.4, ls="-", z=4):
        self.msp.add_circle(self.P(c), r * 12, dxfattribs={"layer": layer, **self._lt(ls)})

    def text(self, x, y, s, layer, size=6, ha="center", va="center", rot=0, weight="normal",
             color=INK, boxed=None, z=7, bg=False):
        hv = {"left": "LEFT", "center": "CENTER", "right": "RIGHT"}[ha]
        vv = {"center": "MIDDLE", "bottom": "BOTTOM", "top": "TOP", "baseline": "BOTTOM"}[va]
        align = ezdxf.enums.TextEntityAlignment[f"{vv}_{hv}"]
        lines = s.split("\n")
        h = self.pt(size)
        n = len(lines)
        ang = math.radians(rot)
        for i, ln in enumerate(lines):
            if va == "center":
                dy = ((n - 1) / 2 - i) * h * 1.45
            elif va == "top":
                dy = -i * h * 1.45
            else:
                dy = (n - 1 - i) * h * 1.45
            px, py = x * 12 - math.sin(ang) * dy, y * 12 + math.cos(ang) * dy
            t = self.msp.add_text(ln.replace("²", "2"), height=h, rotation=rot, dxfattribs={"layer": layer})
            t.set_placement((px, py), align=align)

    def leader(self, p, t, s, layer, size=5.6, ha="left", color=INK):
        self.line([p, t], layer)
        self.text(t[0], t[1], s, layer, size=size, ha=ha)

    def dim(self, p1, p2, off, layer, text=None, size=5.5, color=INK, z=6, ext=True):
        L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        if L < 1e-6:
            return
        d = self.msp.add_aligned_dim(p1=self.P(p1), p2=self.P(p2), distance=off * 12, dimstyle="ARCH",
                                     text=text or ftin(L), dxfattribs={"layer": layer})
        d.render()

    def chain_dim(self, pa, pb, axis, at, layer, size=5.0, ext_from=None, text=None):
        if axis == "x":
            p1 = (pa[0], pa[1] if ext_from is None else ext_from)
            p2 = (pb[0], pb[1] if ext_from is None else ext_from)
            base, angle, L = (pa[0], at), 0, abs(pb[0] - pa[0])
        else:
            p1 = (pa[0] if ext_from is None else ext_from, pa[1])
            p2 = (pb[0] if ext_from is None else ext_from, pb[1])
            base, angle, L = (at, pa[1]), 90, abs(pb[1] - pa[1])
        if L < 1e-6:
            return
        d = self.msp.add_linear_dim(base=self.P(base), p1=self.P(p1), p2=self.P(p2), angle=angle, dimstyle="ARCH",
                                    text=text or ftin(L), dxfattribs={"layer": layer})
        d.render()

    def save(self, path):
        self.doc.saveas(path)


# ============================================================ the model

M = load()
LV = M["levels"]
WALL_T = LV["wall_t"]
ICF = LV["icf_wall_t"]
SLAB = LV["slab_top"]
GRADE = LV["grade"]
SILL = LV["sill"]
FTG_TOP, FTG_T, FTG_W = LV["footing_top"], LV["footing_t"], LV["footing_w"]
SLAB_T, BASE_T = LV["slab_t"], LV["base_t"]
FROST_BOT = LV["frost_bottom"]
F2F = LV["floor_to_floor"]
STAIR = M["stair"]
POOL, SPA, THEA, EXIT = M["pool"], M["spa"], M["theatre"], M["exit_stair"]
BOUT = Polygon(M["basement_outline"])
DOOR_H, OPEN_H, GARAGE_DOOR_H = 7.0, 8.0, 8.0      # house_lib.scad: door_h, open_h; the garage leaves
CORE = 8 / 12


def main_exterior():
    enclosed = unary_union([rbox(r) for r in M["main_rooms"] if r[6] != "porch"])
    return enclosed.buffer(0.5, join_style=2).difference(enclosed.buffer(-0.2, join_style=2))


def icf_ring(half=None):
    half = ICF / 2 if half is None else half
    return BOUT.buffer(half, join_style=2).difference(BOUT.buffer(-half, join_style=2))


def exit_walls():
    """The exit stair areaway's 8" concrete walls, in plan."""
    a, t = EXIT["areaway"], EXIT["wall_t"]
    return unary_union([
        box(a[0] - t, a[3], a[2], a[3] + t),                 # north (outer) wall
        box(a[0] - t, a[1], a[0], a[3]),                     # west wall
        box(54.14, 63.09, a[2], 63.09 + 2 / 3),              # the patio's frost wall, carried down
    ])


def exit_footings():
    a, t = EXIT["areaway"], EXIT["wall_t"]
    return unary_union([box(a[0] - t - 0.5, a[3] + t / 2 - 0.835, a[2], a[3] + t / 2 + 0.835),
                        box(a[0] - t / 2 - 0.835, a[1], a[0] - t / 2 + 0.835, a[3])])


def well_walls():
    t = EXIT["wall_t"]
    out = []
    for w in M["base_windows"]:
        c = w[6]
        ya = c[3] if c[1] > 30 else c[1] - t
        out += [box(c[0] - t, ya, c[2] + t, ya + t), box(c[0] - t, c[1], c[0], c[3]), box(c[2], c[1], c[2] + t, c[3])]
    return unary_union(out)


def well_footings():
    t = EXIT["wall_t"]
    out = []
    for w in M["base_windows"]:
        c = w[6]
        ya = c[3] if c[1] > 30 else c[1] - t
        out += [box(c[0] - t - 0.5, ya + t / 2 - 0.835, c[2] + t + 0.5, ya + t / 2 + 0.835)]
        out += [box(x - 0.835, c[1], x + 0.835, c[3]) for x in (c[0] - t / 2, c[2] + t / 2)]
    return unary_union(out)


def well_floor(w):
    return SLAB + w[4] - 0.5


class Level:
    """Walls, openings and marks of one floor, from the model's tables."""

    def __init__(self, key, rooms, doors, windows, exterior, extra_walls=None, room_prefix="1", mark="1"):
        self.key, self.rooms, self.doors, self.windows = key, rooms, doors, windows
        rings = []
        for r in rooms:
            if r[5] and r[5] > 0:
                b = rbox(r)
                rings.append(b.buffer(WALL_T / 2, join_style=2).difference(b.buffer(-WALL_T / 2, join_style=2)))
        self.exterior = exterior
        allw = unary_union(rings + [exterior] + ([extra_walls] if extra_walls is not None else []))
        cuts = unary_union([opening_box(o) for o in doors + windows])
        self.walls = allw.difference(cuts)
        # marks in reading order; "full" openings are not doors
        di = [i for i in reading_order(len(doors), lambda i: opening_mid(doors[i])) if doors[i][4] != "full"]
        self.door_mark = {i: f"D{mark}{n + 1:02d}" for n, i in enumerate(di)}
        wi = reading_order(len(windows), lambda i: opening_mid(windows[i]))
        self.window_mark = {i: f"W{mark}{n + 1:02d}" for n, i in enumerate(wi)}
        named = [i for i, r in enumerate(rooms) if label_of(r)]
        ri = reading_order(len(named), lambda k: self.label_xy(rooms[named[k]]))
        self.room_no = {named[k]: f"{room_prefix}{n + 1:02d}" for n, k in enumerate(ri)}

    @staticmethod
    def label_xy(r):
        at = r[9] if len(r) > 9 and r[9] else None
        return (at[0], at[1]) if at else ((r[1] + r[3]) / 2, (r[2] + r[4]) / 2)

    def room_name(self, i):
        r = self.rooms[i]
        return label_of(r) or r[6].upper()

    def rooms_at(self, x, y):
        hits = [i for i, r in enumerate(self.rooms) if r[1] < x < r[3] and r[2] < y < r[4]]
        return sorted(hits, key=lambda i: (self.rooms[i][3] - self.rooms[i][1]) * (self.rooms[i][4] - self.rooms[i][2]))

    def sides(self, o):
        mx, my = opening_mid(o)
        pts = ((mx, my - 0.8), (mx, my + 0.8)) if o[2] == "x" else ((mx - 0.8, my), (mx + 0.8, my))
        out = []
        for pt in pts:
            hits = self.rooms_at(*pt)
            out.append(hits[0] if hits else None)
        return out

    def side_names(self, o):
        return [self.room_name(i) if i is not None else "OUTSIDE" for i in self.sides(o)]

    def is_exterior(self, o):
        return any(i is None or self.rooms[i][6] in ("porch", "stairwell") and self.key == "base"
                   or i is not None and self.rooms[i][6] == "porch" for i in self.sides(o))


MAIN = Level("main", M["main_rooms"], M["main_doors"], M["main_windows"], main_exterior(), room_prefix="1", mark="1")
BASE = Level("base", M["base_rooms"], M["base_doors"], [w[:6] for w in M["base_windows"]], icf_ring(),
             extra_walls=unary_union([exit_walls(), well_walls()]), room_prefix="B", mark="B")

ENCLOSED = unary_union([rbox(r) for r in M["main_rooms"] if r[6] != "porch"])
HEATED = unary_union([rbox(r) for r in M["main_rooms"] if r[6] not in ("porch", "garage")])
GARAGE = unary_union([rbox(r) for r in M["main_rooms"] if r[6] == "garage"])
PORCHES = unary_union([rbox(r) for r in M["main_rooms"] if r[6] == "porch"]).difference(ENCLOSED)
AREAS = {
    "main_heated": HEATED.area,                                       # to wall centre lines
    "garage": GARAGE.area,
    "porches": PORCHES.area,
    "basement": BOUT.buffer(-ICF / 2, join_style=2).area,             # inside the ICF
    "footprint_cl": ENCLOSED.area,
    "footprint_out": ENCLOSED.buffer(0.5, join_style=2).area,         # outside face of the walls
    "house_only_out": HEATED.buffer(0.5, join_style=2).area,
    "garage_out": GARAGE.buffer(0.5, join_style=2).area,
}
PART9_LIMIT_M2 = 600.0


# ============================================================ plan drawing

def visible_points(g, side):
    """Vertices of polygon(s) g with nothing of g between them and the far side."""
    pts = []
    x0, y0, x1, y1 = g.bounds
    shrunk = g.buffer(-0.05, join_style=2)
    for p in polys(g):
        for (x, y) in list(p.exterior.coords)[:-1]:
            far = {"S": (x, y0 - 10), "N": (x, y1 + 10), "W": (x0 - 10, y), "E": (x1 + 10, y)}[side]
            if not LineString([(x, y), far]).intersects(shrunk):
                pts.append((x, y))
    return pts


def chains(cv, g, limit, off_near=4.0, off_far=7.5, sides="SNWE", size=5.0, merge=0.5):
    """Exterior dimension chains of polygon g: the wall jogs, then the overall.
    The dimension lines sit off_near / off_far beyond `limit` (bounds clear of porches)."""
    x0, y0, x1, y1 = g.bounds
    lx0, ly0, lx1, ly1 = limit
    for side in sides:
        pts = visible_points(g, side)
        k = 0 if side in "SN" else 1          # coordinate along the chain
        cs = sorted(set(round(p[k], 3) for p in pts))
        keep = [cs[0]]
        for c in cs[1:]:
            if c - keep[-1] >= merge:
                keep.append(c)
        keep[-1] = cs[-1]
        pick = {"S": min, "N": max, "W": min, "E": max}[side]
        near_pt = {}
        for c in keep:
            cands = [p for p in pts if abs(p[k] - c) < 0.01]
            near_pt[c] = pick(cands, key=lambda p: p[1 - k]) if cands else None
        sgn = -1 if side in "SW" else 1
        fixed = {"S": ly0, "N": ly1, "W": lx0, "E": lx1}[side]
        axis = "x" if side in "SN" else "y"
        for c0, c1 in zip(keep, keep[1:]):
            cv.chain_dim(near_pt[c0], near_pt[c1], axis, fixed + sgn * off_near, "A-ANNO-DIMS", size=size)
        if side in "SN":
            pa, pb = (x0, fixed), (x1, fixed)
        else:
            pa, pb = (fixed, y0), (fixed, y1)
        cv.chain_dim(pa, pb, axis, fixed + sgn * off_far, "A-ANNO-DIMS", size=size + 0.8,
                     ext_from=fixed + sgn * (off_near + 0.4))


def draw_openings(cv, lv, marks=True):
    for i, w in enumerate(lv.windows):
        x, y, a, wd = w[:4]
        for d in (-0.2, 0.0, 0.2):
            pts = [(x, y + d), (x + wd, y + d)] if a == "x" else [(x + d, y), (x + d, y + wd)]
            cv.line(pts, "A-GLAZ", lw=0.35, z=4)
        if marks:
            mx, my = opening_mid(w)
            s = lv.sides(w)
            sgn = 1 if s[1] is None or lv.rooms[s[1]][6] in ("porch",) else -1
            tx, ty = (mx, my + sgn * 1.4) if a == "x" else (mx + sgn * 1.6, my)
            cv.text(tx, ty, lv.window_mark[i], "A-ANNO-MARK", size=4.2, color=BLUE, boxed=BLUE)
    for i, d in enumerate(lv.doors):
        x, y, a, wd, kind = d[:5]
        sw = d[5] if len(d) > 5 and d[5] in (1, -1) else 1
        u = (1, 0) if a == "x" else (0, 1)
        n = (0, sw) if a == "x" else (sw, 0)
        leaves = []
        if kind == "door":
            leaves = [((x, y), u, wd)]
        elif kind == "double":
            leaves = [((x, y), u, wd / 2), ((x + wd * u[0], y + wd * u[1]), (-u[0], -u[1]), wd / 2)]
        for (hx, hy), (ux, uy), lw_ in leaves:
            cv.line([(hx, hy), (hx + n[0] * lw_, hy + n[1] * lw_)], "A-DOOR", lw=0.55, z=5)
            a0 = math.degrees(math.atan2(uy, ux))
            a1 = math.degrees(math.atan2(n[1], n[0]))
            dd = (a1 - a0 + 540) % 360 - 180
            t1, t2 = (a0, a0 + dd) if dd > 0 else (a0 + dd, a0)
            cv.arc((hx, hy), lw_, t1, t2, "A-DOOR", lw=0.25, z=5)
        if kind in ("slider", "glass"):
            for dd in (-0.07, 0.07):
                pts = [(x, y + dd), (x + wd, y + dd)] if a == "x" else [(x + dd, y), (x + dd, y + wd)]
                cv.line(pts, "A-DOOR", lw=0.4, z=5)
        if kind == "garage":
            pts = [(x, y), (x, y + wd)] if a == "y" else [(x, y), (x + wd, y)]
            cv.line(pts, "A-DOOR", lw=0.6, ls="--", z=5)
        if kind == "open":
            pts = [(x, y), (x + wd, y)] if a == "x" else [(x, y), (x, y + wd)]
            cv.line(pts, "A-FLOR-OVHD", color=GREY, lw=0.35, ls="--", z=5)
        if marks and i in lv.door_mark:
            mx, my = opening_mid(d)
            off = 1.6 if kind == "garage" else 0.0         # in the opening, on the wall line
            tx, ty = (mx, my + off) if a == "x" else (mx + off, my)
            cv.text(tx, ty, lv.door_mark[i], "A-ANNO-MARK", size=4.2, color=RED, boxed=RED)


def draw_rooms(cv, lv, tags=True):
    for r in lv.rooms:
        if r[6] == "porch":
            cv.geom(rbox(r), "A-AREA", fc="#eef3ee", ec="#9aa79a", lw=0.3, ls=":", z=1)
        elif r[6] == "garage":
            cv.geom(rbox(r), "A-AREA", fc="#f2f2f2", ec="none", lw=0, z=1)
    if not tags:
        return
    for i, r in enumerate(lv.rooms):
        lab = label_of(r)
        if not lab:
            continue
        at = r[9] if len(r) > 9 and r[9] else None
        cx, cy = lv.label_xy(r)
        rot = at[3] if at and len(at) > 3 else 0
        w_, d_ = r[3] - r[1], r[4] - r[2]
        name = "\n".join(r[0]) if isinstance(r[0], list) else lab
        if r[6] == "porch":
            cv.text(cx, cy, f"{lab}\n{ftin(w_)} x {ftin(d_)}", "A-ANNO-TEXT", size=5.5, color=GREEN, rot=rot)
            continue
        if r[6] in ("stair", "stairwell"):
            txt = name
        else:
            txt = f"{name}\n{lv.room_no[i]}\n{ftin(w_)} x {ftin(d_)}"
        small = min(w_, d_) < 6.5
        cv.text(cx, cy, txt, "A-ANNO-TEXT", size=4.8 if small else 6.0, weight="bold", rot=rot, bg=True)


def draw_fixtures(cv, items, layer="A-FLOR-FIXT", color="#9a9a9a"):
    for f in items:
        if f[5] - f[4] < 0.1 or f[4] > 6:
            continue
        g = box(f[0], f[1], f[2], f[3])
        if len(f) > 8 and f[8] == "round":
            cx, cy = (f[0] + f[2]) / 2, (f[1] + f[3]) / 2
            t = np.linspace(0, 2 * np.pi, 40)
            g = Polygon(list(zip(cx + (f[2] - f[0]) / 2 * np.cos(t), cy + (f[3] - f[1]) / 2 * np.sin(t))))
        cv.geom(g, layer, ec=color, lw=0.25, z=2, ls="--" if f[4] > 3.5 else "-")


def draw_stair(cv, x, top, foot, run, arrow_up=False):
    """Treads from `top` (the main floor end) down to `foot`, with the direction arrow."""
    x0, x1 = x
    y = top
    while y >= foot - 1e-6:
        cv.line([(x0 + 0.2, y), (x1 - 0.2, y)], "A-FLOR-STRS", color=GREY, lw=0.3, z=2)
        y -= run
    xm = (x0 + x1) / 2
    cv.line([(xm, top - 0.5), (xm, foot + 0.6)], "A-FLOR-STRS", lw=0.45, z=6)
    tip, tail = (foot + 0.6, foot + 1.4) if not arrow_up else (top - 0.5, top - 1.3)
    cv.line([(xm - 0.45, tail), (xm, tip), (xm + 0.45, tail)], "A-FLOR-STRS", lw=0.45, z=6)


def porch_step_geoms():
    out = []
    for (x, y, d, w) in M["main_porch_steps"]:
        for i in range(4):
            out.append(box(x, y - (i + 1), x + w, y - i) if d == "-y" else box(x, y + i, x + w, y + i + 1))
    return out


def plan_main(cv, marks=True):
    draw_rooms(cv, MAIN)
    draw_fixtures(cv, M["main_fixtures"])
    for g in porch_step_geoms():
        cv.geom(g, "A-FLOR-STRS", ec=GREY, lw=0.3, z=2)
    for ys in M["garage_steps"]:
        for x0 in (19.4, 20.6):
            cv.geom(box(x0, ys[0], x0 + 1.2, ys[1]), "A-FLOR-STRS", ec=GREY, lw=0.3, z=2)
    for p in M["main_posts"]:
        cv.geom(box(p[0] - 0.25, p[1] - 0.25, p[0] + 0.25, p[1] + 0.25), "A-WALL", fc=POCHE, ec=INK, lw=0.3, z=3)
    cv.geom(MAIN.walls, "A-WALL", fc=POCHE, ec=INK, lw=0.4, z=3)
    draw_openings(cv, MAIN, marks)
    # from the main floor only the flight inside the floor opening shows; the
    # rest runs on under the main hall
    draw_stair(cv, STAIR["x"], STAIR["top_y"], 35.46 + WALL_T / 2 + 0.1, STAIR["run"])


def plan_base(cv, marks=True, overlay_main=True):
    draw_rooms(cv, BASE)
    draw_fixtures(cv, M["base_fixtures"])
    draw_fixtures(cv, M["theatre_seats"])
    tx = THEA["pit_x"]
    for t in THEA["tiers"][1:]:
        cv.geom(box(tx[0], t[0], tx[1], t[1]), "S-SLAB", ec=GREY, lw=0.35, ls="--", z=2)
    p, s = POOL["xy"], SPA["xy"]
    sh = POOL["shell_t"]
    cv.geom(box(*p), "S-POOL", fc="#d6ecf5", ec=INK, lw=0.4, z=2)
    cv.geom(box(*s), "S-POOL", fc="#d6ecf5", ec=INK, lw=0.4, z=2)
    cv.geom(box(p[0] - sh, p[1] - sh, p[2] + sh, p[3] + sh).union(box(s[0] - sh, s[1] - sh, s[2] + sh, s[3] + sh))
            .difference(box(*p)).difference(box(*s)), "S-POOL", fc="#d9d9d9", ec=INK, lw=0.35, z=2)
    for i in range(1, 4):
        cv.line([(p[0], p[3] - i), (p[0] + 4, p[3] - i)], "S-POOL", color=GREY, lw=0.3, z=3)
    cv.line([(p[0] + 4, p[3] - 4), (p[0] + 4, p[3])], "S-POOL", color=GREY, lw=0.3, z=3)
    cv.text((p[0] + p[2]) / 2 + 1, (p[1] + p[3]) / 2, f"POOL\n{ftin(p[2] - p[0])} x {ftin(p[3] - p[1])}\n"
            f"{ftin(POOL['depth'])} WATER", "A-ANNO-TEXT", size=5.5, color=BLUE)
    cv.text((s[0] + s[2]) / 2, (s[1] + s[3]) / 2, f"SPA\n{ftin(s[2] - s[0])} x {ftin(s[3] - s[1])}", "A-ANNO-TEXT",
            size=5.0, color=BLUE)
    if overlay_main:
        cv.geom(ENCLOSED, "A-FLOR-OVHD", ec=LIGHT, lw=0.45, ls=(0, (4, 3)), z=1)
    cv.geom(BASE.walls, "A-WALL", fc=POCHE, ec=INK, lw=0.4, z=3)
    draw_openings(cv, BASE, marks)
    draw_stair(cv, STAIR["x"], STAIR["top_y"], STAIR["foot_y"], STAIR["run"], arrow_up=True)
    a = EXIT["areaway"]
    x = EXIT["landing_x"][1]
    while x <= a[2] + 1e-6:
        cv.line([(x, a[1] + 0.1), (x, a[3] - 0.1)], "A-FLOR-STRS", color=GREY, lw=0.3, z=2)
        x += EXIT["run"]
    ym = (a[1] + a[3]) / 2
    cv.line([(EXIT["landing_x"][1] + 0.4, ym), (a[2] - 0.6, ym)], "A-FLOR-STRS", lw=0.45, z=6)
    cv.line([(a[2] - 1.4, ym + 0.45), (a[2] - 0.6, ym), (a[2] - 1.4, ym - 0.45)], "A-FLOR-STRS", lw=0.45, z=6)
    cv.text((EXIT["landing_x"][1] + a[2]) / 2, ym + 0.3, f"UP {EXIT['risers']}R TO GRADE", "A-ANNO-TEXT",
            size=4.5, va="bottom")


# ------------------------------------------------------------ foundation plan

def frost_geoms():
    keep_out = unary_union([BOUT.buffer(ICF / 2, join_style=2), exit_walls().buffer(0.01),
                            box(*EXIT["areaway"]), well_walls().buffer(0.01)]
                           + [box(*w[6]) for w in M["base_windows"]])
    walls = unary_union([strip(f, 8 / 12) for f in M["frost_walls"]]).difference(keep_out)
    ftgs = unary_union([strip(f, 20 / 12) for f in M["frost_walls"]]).difference(BOUT.buffer(ICF / 2, join_style=2))
    # the overhead doors: no curb across the opening
    for d in M["main_doors"]:
        if d[4] == "garage":
            walls = walls.difference(opening_box(d))
    return walls, ftgs


def crawlspace():
    return HEATED.difference(BOUT.buffer(ICF / 2 + 0.3, join_style=2)).difference(unary_union(
        [box(*EXIT["footprint"])] + [box(*w[6]).buffer(0.7, join_style=2) for w in M["base_windows"]]))


def plan_foundation(cv, notes=True):
    p, s = POOL["xy"], SPA["xy"]
    sh = POOL["shell_t"]
    crawl = crawlspace()
    cv.geom(crawl, "S-SLAB", fc="#f4f1e8", ec="none", lw=0, z=0.5, hatch="\\\\\\\\" if isinstance(cv, Mpl) else None)
    cv.geom(GARAGE, "S-SLAB", fc="#ececec", ec="none", lw=0, z=0.5, hatch="...." if isinstance(cv, Mpl) else None)
    cv.geom(ENCLOSED, "A-FLOR-OVHD", ec=LIGHT, lw=0.4, ls=(0, (4, 3)), z=1)
    cv.geom(PORCHES, "A-FLOR-OVHD", ec="#9aa79a", lw=0.3, ls=":", z=1)
    # footings (dashed), then walls on top
    cv.geom(BOUT.buffer(FTG_W / 2, join_style=2).difference(BOUT.buffer(-FTG_W / 2, join_style=2)), "S-FTNG",
            ec=INK, lw=0.35, ls=(0, (5, 3)), z=2)
    for b in M["bearing_lines"]:
        cv.geom(strip(b, 1.67), "S-FTNG", fc="#e9e9e9", ec=INK, lw=0.4, ls=(0, (5, 3)), z=2)
        cv.line([(b[0], b[1]), (b[2], b[3])], "S-ANNO", color=RED, lw=0.5, ls=(0, (12, 3, 2, 3)), z=2.5)
    deep = unary_union([strip(d, 1.0) for d in M["deep_footings"]])
    cv.geom(deep, "S-FTNG", fc="none", ec=BLUE, lw=0.5, ls=(0, (2, 2)), z=2.6)
    fw, ff = frost_geoms()
    cv.geom(ff, "S-FTNG", ec=INK, lw=0.35, ls=(0, (5, 3)), z=2)
    cv.geom(exit_footings(), "S-FTNG", ec=INK, lw=0.35, ls=(0, (5, 3)), z=2)
    cv.geom(well_footings(), "S-FTNG", ec=INK, lw=0.35, ls=(0, (5, 3)), z=2)
    # pool + spa shells
    cv.geom(box(*p), "S-POOL", fc="#d6ecf5", ec=INK, lw=0.4, z=2)
    cv.geom(box(*s), "S-POOL", fc="#d6ecf5", ec=INK, lw=0.4, z=2)
    shells = box(p[0] - sh, p[1] - sh, p[2] + sh, p[3] + sh).union(box(s[0] - sh, s[1] - sh, s[2] + sh, s[3] + sh))
    cv.geom(shells.difference(box(*p)).difference(box(*s)), "S-POOL", fc="#b9b9b9", ec=INK, lw=0.4, z=3)
    cv.geom(shells.buffer(POOL["insul"], join_style=2).difference(shells), "S-POOL", fc="#fbf3c8", ec=GREY,
            lw=0.2, z=3)
    for i in range(1, 4):
        cv.line([(p[0], p[3] - i), (p[0] + 4, p[3] - i)], "S-POOL", color=GREY, lw=0.3, z=3)
    cv.line([(p[0] + 4, p[3] - 4), (p[0] + 4, p[3])], "S-POOL", color=GREY, lw=0.3, z=3)
    sx = SPA["spill_x"]
    cv.line([(sx[0], s[3] + sh / 2), (sx[1], s[3] + sh / 2)], "S-POOL", color=BLUE, lw=1.4, z=4)
    # theatre lowered area
    tx = THEA["pit_x"]
    for t in THEA["tiers"][1:]:
        cv.geom(box(tx[0], t[0], tx[1], t[1]), "S-SLAB", fc="#efefef", ec=INK, lw=0.4, z=2)
    # ICF walls: concrete core dark, foam faces light
    cuts = unary_union([box(EXIT["door"][0], 63.16 - 1, EXIT["door"][0] + EXIT["door"][1], 63.16 + 1)]
                       + [opening_box(w) for w in M["base_windows"]])
    cv.geom(icf_ring().difference(cuts), "S-FNDN", fc="#f6f0d0", ec=INK, lw=0.35, z=3)
    cv.geom(icf_ring(CORE / 2).difference(cuts), "S-FNDN", fc="#7d7d7d", ec="none", lw=0, z=3.1)
    cv.geom(fw, "S-FNDN", fc="#7d7d7d", ec=INK, lw=0.3, z=3)
    cv.geom(exit_walls().difference(BOUT.buffer(ICF / 2, join_style=2)), "S-FNDN", fc="#7d7d7d", ec=INK, lw=0.3, z=3)
    cv.geom(well_walls(), "S-FNDN", fc="#7d7d7d", ec=INK, lw=0.3, z=3)
    a = EXIT["areaway"]
    x = EXIT["landing_x"][1]
    while x <= a[2] + 1e-6:
        cv.line([(x, a[1]), (x, a[3])], "S-SLAB", color=GREY, lw=0.3, z=2)
        x += EXIT["run"]
    cv.geom(box(a[2], a[1], a[2] + EXIT["top_pad"], a[3] + EXIT["wall_t"]), "S-SLAB", fc="#e9e9e9", ec=INK, lw=0.3, z=2)
    for (x, y) in M["piers"]:
        cv.circle((x, y), 1.0, "S-PIER", ec=INK, lw=0.35, ls=(0, (3, 2)), z=3)
        cv.circle((x, y), 0.5, "S-PIER", fc="#7d7d7d", ec=INK, lw=0.4, z=3)
    if notes:
        foundation_notes(cv)


def foundation_notes(cv):
    p, s = POOL["xy"], SPA["xy"]
    L = "S-ANNO"
    f = 5.4
    cv.leader((35.27, 20.0), (25.5, 11.0), "13 1/4\" ICF (8\" CORE)\nON 24\" x 10\" FTG\n"
              f"T/O WALL {el(SILL)}\nU/S FTG {el(FTG_TOP - FTG_T)}", L, size=f, ha="right")
    cv.text(44.7, 16.5, f"BASEMENT SLAB\n{el(SLAB)}\n4\" ON 6\" CLEAR STONE\n(RADON LAYER)", L, size=f)
    cv.leader((p[0] + 3.0, p[1] + 2.5), (77.0, 49.6), f"POOL WATER {el(POOL['water'])}\nFLOOR {el(POOL['water'] - POOL['depth'])}"
              f"\nU/S SHELL {el(POOL['bottom'])}", L, size=f, ha="left")
    cv.leader((s[0] + 1.5, s[1] + 1.5), (73.3, 21.6), f"SPA RIM {el(SPA['rim'])}\nWATER {el(SPA['water'])}\n"
              f"U/S SHELL {el(SPA['bottom'])}", L, size=f, ha="left")
    cv.leader((86.0, s[3] + 0.4), (91.5, 33.0), "SPILLWAY\nSPA TO POOL", L, size=f, ha="left")
    dz = THEA["tiers"]
    cv.leader((60.0, 33.0), (57.0, 27.0), f"THEATER REAR TIER {el(SLAB)}", L, size=f, ha="left")
    cv.leader((60.0, 37.05), (59.0, 25.9), f"STEP {el(SLAB - dz[1][2])}", L, size=f, ha="left")
    cv.text((THEA["pit_x"][0] + THEA["pit_x"][1]) / 2, 42.4, f"FRONT TIER\n{el(SLAB - dz[2][2])}\n"
            "DEPRESSED SLAB,\nTHICKENED EDGES", L, size=f)
    cv.leader((69.38, 21.0), (79.0, 20.6) if False else (60.5, 21.0), "", L, size=1)
    cv.text(61.8, 22.5, "BEARING LINE\n20\" STRIP FTG\nU/S " + el(FTG_TOP - FTG_T).replace("EL. ", ""), L, size=f)
    cv.leader((96.33, 47.0), (100.5, 47.0), f"DEEPENED FTG\nROUND POOL ROOM\nU/S {el(M['deep_footings'][0][4])}\n"
              "(OR SHELL DESIGNED\nTO RETAIN - ENG.)", L, size=f, ha="left", color=BLUE)
    a = EXIT["areaway"]
    cv.leader((58.0, (a[1] + a[3]) / 2), (58.0, 71.0), f"EXIT STAIR AREAWAY {ftin(a[3] - a[1])} CLEAR, FLOOR {el(SLAB)}\n"
              f"8\" CONC. WALLS ON 20\" FTGS, {EXIT['risers']}R UP TO GRADE, A5.1", L, size=f, ha="center")
    w0 = M["base_windows"][0]
    cv.leader(((w0[6][0] + w0[6][2]) / 2, 2.0), (44.0, -6.0), f"LIGHT WELL, FLOOR {el(well_floor(w0))}\n"
              "8\" CONC. WALLS ON 20\" FTGS, A5.1", L, size=f, ha="center")
    w1 = M["base_windows"][1]
    cv.leader((34.6, 67.0), (27.0, 71.5), f"LIGHT WELL, FLOOR {el(well_floor(w1))}", L, size=f, ha="right")
    cv.text(12.0, 18.0, f"GARAGE SLAB\n4\" ON 6\" STONE\nT/O {el(-1.5)}\nSLOPE TO DOORS", L, size=f)
    cv.text(14.7, 50.5, "CRAWLSPACE\n18\" CLEAR\nCONDITIONED,\nSEALED GROUND\nCOVER", L, size=f)
    cv.text(115.5, 32.0, "CRAWLSPACE\n18\" CLEAR, CONDITIONED,\nSEALED GROUND COVER\nTIED TO RADON LAYER", L, size=f)
    cv.leader((126.97, 45.0), (118.0, 45.0), f"8\" FROST WALL ON 20\" x 8\" FTG\nU/S {el(FROST_BOT)} "
              "(4'-0\" BELOW GRADE)", L, size=f, ha="center")
    cv.leader((81.1, -14.81), (75.5, -10.0), "12\" PIER ON 24\" BELL\nU/S 4'-6\" BELOW GRADE\n(OR HELICAL PILE)", L,
              size=f, ha="center")
    cv.text(30.0, 39.0, "SUMP + RADON\nROUGH-IN (SUGG.)", L, size=4.8, color=RED)
    cv.circle((30.0, 41.4), 0.9, L, ec=RED, lw=0.6)
    cv.text(99.7, 38.6, "SUMP (POOL\nDRAIN LOOP)", L, size=4.8, color=RED)
    cv.circle((99.7, 40.4), 0.9, L, ec=RED, lw=0.6)


# ------------------------------------------------------------ framing concept

# Floor-framing zones: [label, x0, y0, x1, y1, span axis, what is below]. The
# spans are between the supports the foundation gives (ICF walls, bearing
# lines, frost walls); the truss designer and the engineer set the layout.
FRAMING = [
    ("F1", 35.27, 5.79, 54.14, 35.08, "x", "living room, hallway"),
    ("F2", 22.16, 35.08, 42.65, 63.16, "x", "utility, storage, music room - with NEW bearing line x = 42.65"),
    ("F3", 42.65, 35.08, 54.14, 63.16, "x", "stair, bath, gym - stair opening framed in"),
    ("F4", 54.14, 18.15, 69.38, 50.35, "x", "pet room, theater"),
    ("F5", 69.38, 18.15, 96.33, 52.76, "x", "pool room - longest clear span, humid room below"),
    ("F6", 96.33, 13.43, 103.04, 41.94, "x", "pool equipment, pool bath"),
    ("F7", 54.14, 5.79, 81.68, 18.15, "y", "bath, laundry, hall"),
    ("F8", 81.68, 13.43, 103.04, 18.15, "y", "hall"),
    ("C1", 7.27, 35.46, 22.16, 62.04, "x", "bedroom wing, crawlspace"),
    ("C2", 24.34, 20.82, 35.27, 35.46, "x", "scullery, side entry, crawlspace"),
    ("C3", 54.14, 50.35, 69.14, 63.42, "y", "patio floor (exterior), on the frost walls"),
    ("C4", 103.04, 9.31, 126.97, 48.16, "x", "office, master wing - NEW crawlspace beam line x = 103.04 north of y 41.94"),
    ("C5", 108.62, 48.16, 126.97, 52.86, "x", "master bedroom north, crawlspace"),
    ("C6", 81.68, 0.0, 95.95, 13.43, "y", "den front, crawlspace"),
]
NEW_BEARING = [
    ("NEW BEARING WALL ON 20\" STRIP FTG (PHASE 1)", (42.65, 35.08, 42.65, 63.16)),
    ("NEW BEAM ON PIERS / FROST WALL IN CRAWLSPACE", (103.04, 41.94, 103.04, 48.16)),
]


def plan_framing(cv):
    cv.geom(ENCLOSED, "A-FLOR-OVHD", ec=LIGHT, lw=0.4, z=1)
    cv.geom(MAIN.walls, "A-WALL", fc="#e3e3e3", ec="#b5b5b5", lw=0.2, z=1.5)
    cv.geom(icf_ring(), "S-FNDN", fc="#5a5a5a", ec=INK, lw=0.4, z=3)
    fw, _ = frost_geoms()
    cv.geom(fw, "S-FNDN", fc="#5a5a5a", ec=INK, lw=0.3, z=3)
    for b in M["bearing_lines"]:
        cv.geom(strip(b, 0.6), "S-BEAM", fc="#5a5a5a", ec=INK, lw=0.3, z=3)
    for lab, s in NEW_BEARING:
        cv.geom(strip(s, 0.6), "S-BEAM", fc=RED, ec=RED, lw=0.3, z=3.2)
    for (lab, x0, y0, x1, y1, ax_, what) in FRAMING:
        cv.geom(box(x0, y0, x1, y1).buffer(-0.6, join_style=2), "S-ANNO", ec=BLUE, lw=0.4, ls=(0, (1, 2)), z=2)
        if ax_ == "x":
            ym = (y0 + y1) / 2
            cv.dim((x0, ym), (x1, ym), 0, "S-ANNO", text=f"{lab}  {ftin(x1 - x0)}", size=6.5, color=BLUE)
        else:
            xm = (x0 + x1) / 2
            cv.dim((xm, y0), (xm, y1), 0, "S-ANNO", text=f"{lab}  {ftin(y1 - y0)}", size=6.5, color=BLUE)
    sx = STAIR["x"]
    cv.geom(box(sx[0], 35.46, sx[1], STAIR["top_y"]), "S-ANNO", fc="white", ec=INK, lw=0.5, z=2.5)
    cv.line([(sx[0], 35.46), (sx[1], STAIR["top_y"])], "S-ANNO", lw=0.3, z=2.6)
    cv.line([(sx[1], 35.46), (sx[0], STAIR["top_y"])], "S-ANNO", lw=0.3, z=2.6)
    cv.text(sum(sx) / 2, 41.2, "STAIR\nOPENING", "S-ANNO", size=4.5, bg=True)


# ============================================================ sheets

SHEETS = []
INDEX = [
    ("A0.0", "COVER, PROJECT DATA, DRAWING INDEX"),
    ("A0.1", "SITE PLAN (SCHEMATIC)"),
    ("S0.1", "STRUCTURAL DESIGN BRIEF"),
    ("S1.0", "FOUNDATION PLAN"),
    ("S1.1", "MAIN FLOOR FRAMING CONCEPT"),
    ("A1.1", "BASEMENT PLAN"),
    ("A1.2", "MAIN FLOOR PLAN"),
    ("A1.3", "ROOF PLAN"),
    ("A3.0", "ELEVATIONS"),
    ("A4.0", "BUILDING SECTIONS A AND B"),
    ("A4.1", "BUILDING SECTIONS C, D AND E"),
    ("A5.0", "DETAILS - FOUNDATION"),
    ("A5.1", "DETAILS - POOL, THEATER, STAIRS, LIGHT WELL"),
    ("A6.0", "SCHEDULES - DOORS, WINDOWS, ROOMS"),
]


def new_sheet(number, scale=""):
    title = dict(INDEX)[number]
    fig = plt.figure(figsize=(SHEET_W, SHEET_H))
    fig.patch.set_facecolor("white")
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_xlim(0, SHEET_W)
    bg.set_ylim(0, SHEET_H)
    bg.axis("off")
    bg.add_patch(Rectangle((0.5, 0.5), SHEET_W - 1.0, SHEET_H - 1.0, fill=False, lw=1.4, ec=INK))
    x0 = SHEET_W - 0.5 - TB_W
    bg.plot([x0, x0], [0.5, SHEET_H - 0.5], color=INK, lw=1.4)

    def tb(y, text, fs=8, weight="normal", color=INK):
        bg.text(x0 + 0.2, y, text, fontsize=fs, weight=weight, color=color, va="top")

    tb(SHEET_H - 0.75, PROJECT, 12, "bold")
    tb(SHEET_H - 1.2, PROJECT_2, 7.5)
    tb(SHEET_H - 1.48, SITE_TXT, 7.5)
    tb(SHEET_H - 1.76, "Owner / applicant: ______________________", 7.5)
    bg.add_patch(Rectangle((x0 + 0.15, SHEET_H - 4.25), TB_W - 0.3, 2.1, fill=False, lw=1.6, ec=RED))
    bg.text(x0 + TB_W / 2, SHEET_H - 3.2, "NOT FOR CONSTRUCTION\n\nFOR ENGINEERING REVIEW\nAND PERMIT PREPARATION",
            fontsize=10.5, weight="bold", color=RED, ha="center", va="center", linespacing=1.3)
    notes = [
        "Drawn from the OpenSCAD model in",
        "github.com/nuniesmith/house (models/)",
        "by tools/make_drawings.py.",
        "",
        "Dimensions are to wall centre lines",
        "unless noted. Walls are drawn 4 3/4\"",
        "interior, 8 3/8\" exterior (2x6 + sheathing",
        "+ cladding assumed) and 13 1/4\" ICF.",
        "",
        "Elevations are relative to the main",
        "floor = 0'-0\". Finished grade is taken",
        "at -2'-0\" all round until a site survey",
        "and grading plan fix it.",
        "",
        "Structure, reinforcement, connections",
        "and member sizes are by the engineer",
        "of record and the truss designer.",
        "Verify every dimension before building.",
    ]
    for i, n in enumerate(notes):
        tb(SHEET_H - 4.6 - i * 0.235, n, 7, color="#333333")
    bg.add_patch(Rectangle((x0 + 0.15, 4.0), TB_W - 0.3, 2.9, fill=False, lw=0.6, ec=INK))
    bg.text(x0 + 0.3, 6.75, "ENGINEER'S REVIEW / SEAL", fontsize=6.5, va="top", color="#555555")
    bg.plot([x0, SHEET_W - 0.5], [3.55, 3.55], color=INK, lw=0.9)
    bg.plot([x0, SHEET_W - 0.5], [2.0, 2.0], color=INK, lw=0.9)
    bg.text(x0 + 0.2, 3.42, "SHEET TITLE", fontsize=6, va="top", color="#555555")
    bg.text(x0 + 0.2, 3.18, "\n".join(wrap(title, 30)), fontsize=10.5, weight="bold", va="top", linespacing=1.2)
    if scale:
        bg.text(x0 + 0.2, 2.12, f"SCALE: {scale}", fontsize=7, va="bottom")
    bg.text(x0 + 0.2, 1.85, "SHEET", fontsize=6, va="top", color="#555555")
    bg.text(x0 + 0.2, 1.6, number, fontsize=24, weight="bold", va="top")
    bg.text(SHEET_W - 0.7, 1.85, f"{[n for n, _ in INDEX].index(number) + 1} of {len(INDEX)}", fontsize=7,
            va="top", ha="right")
    bg.text(SHEET_W - 0.7, 1.05, f"DATE {DATE}", fontsize=6.5, va="top", ha="right")
    bg.text(SHEET_W - 0.7, 0.8, "REV. 0 - issued for review", fontsize=6.5, va="top", ha="right")
    SHEETS.append((number, title))
    return fig, bg


def sheet_axes(fig, rect, center, fpi):
    """Axes over `rect` (sheet inches x, y, w, h) at 1 in = fpi ft, centred on the model point `center`."""
    x, y, w, h = rect
    ax = fig.add_axes([x / SHEET_W, y / SHEET_H, w / SHEET_W, h / SHEET_H])
    cx, cy = center
    ax.set_xlim(cx - w * fpi / 2, cx + w * fpi / 2)
    ax.set_ylim(cy - h * fpi / 2, cy + h * fpi / 2)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax


def view_title(bg, x, y, n, text, scale, sheet=None):
    bg.add_patch(Circle((x + 0.3, y), 0.28, fill=False, lw=0.9, ec=INK))
    bg.plot([x + 0.02, x + 0.58], [y, y], color=INK, lw=0.6)
    bg.text(x + 0.3, y + 0.04, str(n), fontsize=9, weight="bold", ha="center", va="bottom")
    bg.text(x + 0.3, y - 0.04, sheet or "", fontsize=5.5, ha="center", va="top")
    bg.text(x + 0.72, y + 0.04, text, fontsize=11, weight="bold", va="bottom")
    bg.plot([x + 0.72, x + 0.72 + 0.112 * len(text) + 0.2], [y, y], color=INK, lw=1.0)
    bg.text(x + 0.72, y - 0.07, f"SCALE: {scale}", fontsize=7, va="top")


def north_arrow(bg, x, y, size=0.42):
    bg.add_patch(Circle((x, y), size * 0.78, fill=False, lw=0.6, ec=INK))
    bg.add_patch(MPoly([(x, y + size), (x - size * 0.32, y - size * 0.5), (x, y - size * 0.22)],
                       closed=True, fc=INK, ec=INK, lw=0.5))
    bg.add_patch(MPoly([(x, y + size), (x + size * 0.32, y - size * 0.5), (x, y - size * 0.22)],
                       closed=True, fc="white", ec=INK, lw=0.5))
    bg.text(x, y + size * 1.05, "N", ha="center", va="bottom", fontsize=10, weight="bold")


def scale_bar(bg, x, y, fpi, feet=(0, 4, 8, 16, 32)):
    for k, (a, b) in enumerate(zip(feet, feet[1:])):
        bg.add_patch(Rectangle((x + a / fpi, y), (b - a) / fpi, 0.07, fc=INK if k % 2 == 0 else "white",
                               ec=INK, lw=0.4))
    for f in feet:
        bg.text(x + f / fpi, y - 0.05, f"{f}'", fontsize=5.5, ha="center", va="top")


def notes_column(bg, x, y, title, items, width, fs=6.4, lh=None):
    """A titled column of bullet notes; returns the y below it."""
    lh = lh or fs / 72 * 1.42
    ts = max(8.5, fs + 1.0)
    bg.text(x, y, title, fontsize=ts, weight="bold", va="top")
    bg.plot([x, x + width], [y - ts / 72 * 1.6, y - ts / 72 * 1.6], color=INK, lw=0.5)
    yy = y - ts / 72 * 2.6
    for ln in bullets(items, chars_for(width, fs)):
        bold = ln.startswith("**")
        bg.text(x, yy, ln.strip("*"), fontsize=fs, va="top", weight="bold" if bold else "normal")
        yy -= lh * (1.25 if bold else 1.0)
    return yy - 0.1


def section_marker(ax, label, sheet, axis, at, ends, look=1):
    """Section cut on a plan: axis 'y' = the cut line y = at, bubbles at x = ends; arrows look +y (look=1)."""
    style = dict(color=INK, lw=0.9, ls=(0, (10, 3, 2, 3)), zorder=9)
    for k, e in enumerate(ends):
        inward = 1 if k == 0 else -1
        if axis == "y":
            ax.plot([e, e + inward * 5], [at, at], **style)
            c = (e, at)
            arrow = [(e - 0.9, at + look * 1.5), (e + 0.9, at + look * 1.5), (e, at + look * 3.0)]
        else:
            ax.plot([at, at], [e, e + inward * 5], **style)
            c = (at, e)
            arrow = [(at + look * 1.5, e - 0.9), (at + look * 1.5, e + 0.9), (at + look * 3.0, e)]
        ax.add_patch(MPoly(arrow, closed=True, fc=INK, ec=INK, zorder=10))
        ax.add_patch(Circle(c, 1.5, fc="white", ec=INK, lw=0.8, zorder=10))
        ax.plot([c[0] - 1.5, c[0] + 1.5], [c[1], c[1]], color=INK, lw=0.4, zorder=11)
        ax.text(c[0], c[1] + 0.15, label, fontsize=7, weight="bold", ha="center", va="bottom", zorder=11)
        ax.text(c[0], c[1] - 0.2, sheet, fontsize=4.2, ha="center", va="top", zorder=11)


# every plan sheet shares this frame (scale and centre), so the plans overlay
PLAN_RECT = (DRAW[0], 2.85, DRAW[2], DRAW[3] - 2.25)
PLAN_CENTER = (68.6, 25.6)
MAIN_LIMIT = (0.0, -19.3, 137.66, 70.7)
BASE_LIMIT = (BOUT.bounds[0] - ICF / 2, -0.5, BOUT.bounds[2] + ICF / 2, 69.7)
SEC_BUBBLES_MAIN = {"A": (-2.1, 139.2), "B": (-21.4, 72.7), "C": (-21.4, 72.7), "D": (-21.4, 72.7)}
SEC_BUBBLES_BASE = {"A": (19.5, 105.6), "B": (-2.6, 71.8), "C": (-2.6, 71.8), "D": (-2.6, 71.8), "E": (43.05, 71.3)}
SECTIONS = {   # label: (cut-line axis, at, plan sheet the section is on)
    "A": ("y", 40.0, "A4.0"), "B": ("x", 45.0, "A4.0"), "C": ("x", 62.0, "A4.1"), "D": ("x", 86.0, "A4.1"),
    "E": ("y", (EXIT["areaway"][1] + EXIT["areaway"][3]) / 2, "A4.1"),
}


def plan_sheet(number, title, draw, chain_geom, limit, bubbles, extra=None, notes=(), notes_w=6.3):
    fig, bg = new_sheet(number, SCALE_TXT[S316])
    ax = sheet_axes(fig, PLAN_RECT, PLAN_CENTER, S316)
    cv = Mpl(ax, S316)
    draw(cv)
    chains(cv, chain_geom, limit)
    for lab, ends in bubbles.items():
        axis, at, sh = SECTIONS[lab]
        section_marker(ax, lab, sh, axis, at, ends)
    if extra:
        extra(ax, cv, fig, bg)
    view_title(bg, DRAW[0] + 0.2, 2.5, 1, title, SCALE_TXT[S316], number)
    north_arrow(bg, DRAW[0] + 0.75, 1.15)
    scale_bar(bg, DRAW[0] + 1.6, 1.2, S316)
    x = DRAW[0] + 8.2
    for t, items in notes:
        notes_column(bg, x, 2.62, t, items, notes_w - 0.3, fs=6.0)
        x += notes_w + 0.15
    return fig, bg, ax


def sheet_main_floor(pdf):
    notes = [
        ("PLAN NOTES", [
            "Room tags: name, number (A6.0), size between wall centre lines.",
            "Door marks D1xx, window marks W1xx: see the schedules on A6.0.",
            "Porch floors are 2'-0\" (610 mm) above grade: guards (NBC 9.8.8) unless the finished grade "
            "is raised to within 600 mm of the porch floor.",
        ]),
        ("LIFE SAFETY", [
            "Smoke alarms in every bedroom, the hall outside them and on each storey: hard-wired, "
            "interconnected (NBC 9.10.19).",
            "CO alarms near the sleeping areas: the garage is attached (NBC 9.32.3.9).",
            "Garage door to the house: self-closing, weatherstripped; garage walls and ceiling gas-proofed "
            "(NBC 9.10.13.15, 9.10.9.16).",
        ]),
        ("STAIRS AND STEPS", [
            f"Main stair: {STAIR['risers']} risers x 7 1/2\", treads 10 1/2\", headroom 1 993 mm min. (A5.1).",
            "Porch steps (4 risers of 6\") and garage steps (3 risers): handrails per NBC 9.8.7; "
            "check the garage door landing (9.8.6).",
        ]),
    ]
    fig, bg, ax = plan_sheet("A1.2", "MAIN FLOOR PLAN", plan_main, ENCLOSED, MAIN_LIMIT, SEC_BUBBLES_MAIN,
                             notes=notes, notes_w=7.2)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_basement(pdf):
    def extra(ax, cv, fig, bg):
        ax.text(1.0, 63.5, "MAIN FLOOR OUTLINE\nABOVE SHOWN DASHED", fontsize=5.5, color=GREY, ha="left", va="top")
        ax.text(110.0, 37.0, "PHASE 2 - after the house is occupied:\n"
                "framing, drywall, ceilings, bathrooms,\nthe theater and music room build-out and\n"
                "the finishes. It needs its own building,\nelectrical and plumbing permits.\n\n"
                "PHASE 1 - with the house:\nall the concrete on S1.0, the stair,\n"
                "bearing walls and posts (S1.1), the\nunder-slab plumbing, the pool and spa,\n"
                "the mechanical room, and a thermal\nbarrier (1/2\" gypsum) over all the\n"
                "ICF foam (NBC 9.10.17.10).", fontsize=6.2, ha="left", va="top", color=INK, linespacing=1.25,
                bbox=dict(fc="#fff7e0", ec="#c9a227", lw=0.6, pad=5))
    notes = [
        ("PLAN NOTES", [
            f"Basement floor {el(SLAB)}; 12'-0\" ceilings to the underside of the main floor framing.",
            "Theater: rear tier at floor level, one 7 1/2\" step, front tier 1'-3\" down (A5.1).",
            "Pool 15'-0\" x 15'-0\", 4'-6\" water; spa raised 18\" (A5.1).",
        ]),
        ("EXITS AND LIGHT", [
            "No bedrooms in the basement, so no egress windows are needed (NBC 9.9.10).",
            "Exits: the main stair and the exterior exit stair from the gym (A5.1).",
            "Windows WB01-WB02 sit in light wells with 42\" guards (A5.1).",
        ]),
        ("BEFORE THE SLAB (PHASE 1)", [
            "Under-slab drains for every future basement fixture, floor drains, the sump, the radon "
            "pipe, the pool and spa piping and the hydrostatic relief valve.",
        ]),
    ]
    fig, bg, ax = plan_sheet("A1.1", "BASEMENT PLAN", plan_base, BOUT, BASE_LIMIT, SEC_BUBBLES_BASE, extra=extra,
                             notes=notes, notes_w=7.2)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_foundation(pdf):
    def extra(ax, cv, fig, bg):
        # legend, in the open ground south of the garage
        lx, ly = 1.0, -4.0
        items = [("#7d7d7d", INK, "-", "CONCRETE WALL (ICF CORE, FROST WALL, AREAWAY)"),
                 ("#f6f0d0", INK, "-", "ICF FOAM FACES"),
                 ("none", INK, (0, (5, 3)), "FOOTING BELOW"),
                 ("#e9e9e9", INK, (0, (5, 3)), "BEARING-LINE STRIP FOOTING"),
                 ("none", BLUE, (0, (2, 2)), "DEEPENED FOOTING"),
                 ("#f4f1e8", "none", "-", "CRAWLSPACE")]
        for k, (fc, ec, ls, t) in enumerate(items):
            yy = ly - k * 1.9
            ax.add_patch(Rectangle((lx, yy - 0.6), 3.0, 1.2, fc=fc, ec=ec, ls=ls, lw=0.5, zorder=9,
                                   hatch="\\\\\\\\" if t == "CRAWLSPACE" else None))
            ax.text(lx + 3.6, yy, t, fontsize=5.2, va="center", zorder=9)
    notes = [
        ("FOUNDATION NOTES", [
            "Dimensions to the ICF wall centre line (= the main floor wall centre lines). The form's outside "
            "face is 6 5/8\" outside it.",
            f"Footings bear on undisturbed soil at {el(FTG_TOP - FTG_T)}, about 13'-5\" below grade: "
            "bearing capacity, sulphate class and groundwater from the geotechnical report.",
            "Reinforcement, dowels, lintels over openings and the wall-top connection: by the engineer (S0.1).",
        ]),
        ("SLAB AND DRAINAGE", [
            "4\" slab on 10 mil sealed poly on 6\" clear stone (gas-permeable layer, NBC 9.13.4); "
            "2\" rigid insulation under it recommended.",
            "Weeping tile round the footings to the sump; the pool pit gets its own drain loop (A5.1).",
            "Dampproofing / waterproofing and drainage board on the ICF, free-draining backfill.",
        ]),
        ("CONCRETE (CSA A23.1, verify)", [
            "Footings, walls: S-class per the geotech, else N.  Slab: N, 25-32 MPa.",
            "Garage slab: C-2, 32 MPa, air-entrained.  Pool/spa shell: 35 MPa, w/cm 0.40 (A5.1).",
        ]),
    ]
    # the basement's dimension chains go outside everything, clear of the frost walls
    fig, bg, ax = plan_sheet("S1.0", "FOUNDATION PLAN", plan_foundation, BOUT, MAIN_LIMIT,
                             {**SEC_BUBBLES_MAIN, "E": SEC_BUBBLES_BASE["E"]}, extra=extra, notes=notes, notes_w=7.2)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_framing(pdf):
    def extra(ax, cv, fig, bg):
        for lab, s in NEW_BEARING:
            ax.annotate(lab, xy=((s[0] + s[2]) / 2, (s[1] + s[3]) / 2 + 3), xytext=(s[0] - 14, s[3] + 5.5)
                        if s[0] < 60 else (s[0] + 6, s[3] + 9), fontsize=5.6, color=RED, weight="bold",
                        arrowprops=dict(arrowstyle="-", lw=0.4, color=RED), zorder=10,
                        bbox=dict(fc="white", ec="none", pad=0.5))
    notes = [
        ("FRAMING CONCEPT - FOR THE ENGINEER", [
            "Main floor: floor trusses spanning between the supports shown dark: ICF walls, interior bearing "
            "lines on strip footings, frost walls. Blue: indicative clear spans (F = over the basement, "
            "C = over crawlspace). Depth allowed: 1'-7 1/2\" from T/O ICF to T/O subfloor.",
            "Two supports are added (red): a bearing wall on x = 42.65 so the west zone is not a 32 ft span, "
            "and a crawlspace beam line on x = 103.04 under the office.",
        ]),
        ("CHECK", [
            "F5 pool room: 26'-11\" clear over a humid room - deep or closely spaced trusses, and protect them "
            "from the pool air (vapour control in the ceiling).",
            "Stair opening 4'-7 1/2\" x 11'-7 5/8\": headers and trimmers.  Garage door headers 16'-0\" and 9'-0\".",
            "Roof: hip trusses by the truss designer. Girder trusses where the hips meet put point loads on "
            "interior walls - trace them to the footings.",
        ]),
        ("BEARING WALLS ARE PHASE 1", [
            "Everything that carries the main floor (bearing walls, beams, posts and their footings) is built "
            "with the house, even where the basement stays unfinished until Phase 2.",
        ]),
    ]
    fig, bg, ax = plan_sheet("S1.1", "MAIN FLOOR FRAMING CONCEPT", plan_framing, ENCLOSED, MAIN_LIMIT, {}, extra=extra,
                             notes=notes, notes_w=7.2)
    pdf.savefig(fig)
    plt.close(fig)


# ============================================================ renders (OpenSCAD)

HC = "house_combined.scad"
NOFURN = ("show_furniture=false",)
SECT = NOFURN + ("section_roof=true", 'mode="section"')
VIEWS = {
    # name: (scad, look, (u0, u1), (z0, z1) or (y0, y1) for "D", depth, fpi, dpi, defines)
    # look: N/S/E/W = the direction looked in; D = down (plan). u = the model axis to screen-right.
    "elev_s": (HC, "N", (-3.0, 141.0), (-2.6, 22.0), 0.0, S316, 150, NOFURN),
    "elev_n": (HC, "S", (-141.0, 3.0), (-2.6, 22.0), 60.0, S316, 150, NOFURN),
    "elev_e": (HC, "W", (-21.0, 71.0), (-2.6, 22.0), 120.0, S316, 150, NOFURN),
    "elev_w": (HC, "E", (-71.0, 21.0), (-2.6, 22.0), 0.0, S316, 150, NOFURN),
    "sec_a": (HC, "N", (-4.0, 142.0), (-21.5, 22.0), 40.0, S316, 150, SECT + ('section="A"',)),
    "sec_b": (HC, "E", (-71.0, 21.0), (-21.5, 22.0), 45.0, S316, 150, SECT + ('section="B"',)),
    "sec_c": (HC, "E", (-71.0, 21.0), (-21.5, 22.0), 62.0, S316, 150, SECT + ('section="C"',)),
    "sec_d": (HC, "E", (-71.0, 21.0), (-21.5, 22.0), 86.0, S316, 150, SECT + ('section="D"',)),
    "sec_e": (HC, "N", (41.5, 72.5), (-17.0, 3.0), EXIT["areaway"][1] + 2, S38, 160,
              SECT + ('section="E"',)),
    "roof": ("main_floor.scad", "D", (PLAN_CENTER[0] - PLAN_RECT[2] * S316 / 2, PLAN_CENTER[0] + PLAN_RECT[2] * S316 / 2),
             (PLAN_CENTER[1] - PLAN_RECT[3] * S316 / 2, PLAN_CENTER[1] + PLAN_RECT[3] * S316 / 2), 0.0, S316, 150,
             NOFURN),
    "site": ("site.scad", "D", (-112.0, 262.0), (-127.0, 240.0), 0.0, S_SITE, 150, ('phase="house"',)),
}


def camera(name):
    scad, look, ur, vr, depth, fpi, dpi, defs = VIEWS[name]
    uc, vc = (ur[0] + ur[1]) / 2, (vr[0] + vr[1]) / 2
    d = (vr[1] - vr[0]) / 0.39782
    size = (int(round((ur[1] - ur[0]) / fpi * dpi)), int(round((vr[1] - vr[0]) / fpi * dpi)))
    c = {"N": (uc, depth, vc, 90, 0, 0), "S": (-uc, depth, vc, 90, 0, 180), "W": (depth, uc, vc, 90, 0, 90),
         "E": (depth, -uc, vc, 90, 0, 270), "D": (uc, vc, depth, 0, 0, 0)}[look]
    return ",".join(f"{v:.4f}" for v in c) + f",{d:.4f}", size


def render_all(names):
    CACHE.mkdir(parents=True, exist_ok=True)
    stamp = max(p.stat().st_mtime for p in (ROOT / "models").glob("*.scad"))
    paths, todo = {}, []
    for k, name in enumerate(names):
        scad, look, ur, vr, depth, fpi, dpi, defs = VIEWS[name]
        cam, size = camera(name)
        key = hashlib.sha1(repr((scad, cam, size, defs)).encode()).hexdigest()[:10]
        png = CACHE / f"{name}-{key}.png"
        paths[name] = png
        if not (png.exists() and png.stat().st_mtime > stamp):
            cmd = (["xvfb-run", "-a", "-n", str(90 + k)] if shutil.which("xvfb-run") else []) + [
                "openscad", "-o", str(png), f"--imgsize={size[0]},{size[1]}", f"--camera={cam}",
                "--projection=o", "--colorscheme=Tomorrow"]
            for d in defs:
                cmd += ["-D", d]
            todo.append((name, cmd + [str(ROOT / "models" / scad)]))

    def run(job):
        name, cmd = job
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(f"  rendered {name}" if r.returncode == 0 else f"  FAILED {name}: {r.stderr[-400:]}", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(run, todo))
    return paths


def load_render(path):
    img = plt.imread(path)[:, :, :3].copy()
    bgc = img[2, 2].copy()
    mask = np.all(np.abs(img - bgc) < 0.004, axis=2)
    img[mask] = 1.0
    return img


def place_render(fig, name, paths, x, y):
    """The render on the sheet with its lower-left corner at (x, y) inches, at its own scale.
    Returns the axes; its data coordinates are the view's (u, z) in feet."""
    scad, look, ur, vr, depth, fpi, dpi, defs = VIEWS[name]
    img = load_render(paths[name])
    h_px, w_px = img.shape[:2]
    h_ft = vr[1] - vr[0]
    w_ft = h_ft * w_px / h_px
    uc = (ur[0] + ur[1]) / 2
    ext = (uc - w_ft / 2, uc + w_ft / 2, vr[0], vr[1])
    ax = fig.add_axes([x / SHEET_W, y / SHEET_H, w_ft / fpi / SHEET_W, h_ft / fpi / SHEET_H])
    ax.imshow(img, extent=ext, interpolation="antialiased", zorder=0)
    ax.set_xlim(ext[0], ext[1])
    ax.set_ylim(vr[0], vr[1])
    ax.axis("off")
    return ax


def level_line(ax, z, label, u0, u1, color=RED, side="right", fs=5.6, ls=(0, (8, 3)), text_u=None, below=False):
    ax.plot([u0, u1], [z, z], color=color, lw=0.3, ls=ls, zorder=5, alpha=0.55)
    ax.plot([u1 - 12, u1] if side == "right" else [u0, u0 + 12], [z, z], color=color, lw=0.6, zorder=5)
    tu = text_u if text_u is not None else (u1 if side == "right" else u0)
    ax.text(tu, z - 0.18 if below else z + 0.18, label, fontsize=fs, color=color,
            ha="right" if side == "right" else "left", va="top" if below else "bottom", zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.3))


def grade_mask(ax, u0, u1, z0):
    ax.add_patch(Rectangle((u0, z0 - 1), u1 - u0, GRADE - z0 + 1, fc="white", ec="none", zorder=3))
    ax.add_patch(Rectangle((u0, GRADE - 0.45), u1 - u0, 0.45, fc="#efe4d3", ec="none", hatch="////", zorder=3.1))
    ax.plot([u0, u1], [GRADE, GRADE], color=INK, lw=1.2, zorder=4)


# ------------------------------------------------------------ roof, elevations, sections, site

def sheet_roof(pdf, paths):
    fig, bg = new_sheet("A1.3", SCALE_TXT[S316])
    scad, look, ur, vr, depth, fpi, dpi, defs = VIEWS["roof"]
    ax = place_render(fig, "roof", paths, PLAN_RECT[0], PLAN_RECT[1])
    for b in M["main_roof"]:
        x0, y0, x1, y1, eave, pitch, ov = b
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        p12 = round(pitch * 12)
        small = min(x1 - x0, y1 - y0) < 12
        ax.text(cx, cy - (1.4 if not small else 0), f"{p12}/12" + ("" if small else f"\nPLATE {el(eave)}"),
                fontsize=5.5 if not small else 4.8, ha="center", va="center", color="white", weight="bold", zorder=6,
                bbox=dict(fc="#203f66", ec="none", alpha=0.85, pad=0.8))
    view_title(bg, DRAW[0] + 0.2, 2.5, 1, "ROOF PLAN", SCALE_TXT[S316], "A1.3")
    north_arrow(bg, DRAW[0] + 0.75, 1.15)
    scale_bar(bg, DRAW[0] + 1.6, 1.2, S316)
    notes = [
        ("ROOF NOTES", [
            "Hip roofs: 6/12 over the house, 4/12 over the porches; 1'-6\" overhangs on the house, 1'-0\" on "
            "the porches. Plate heights as tagged (main floor = 0'-0\").",
            "Engineered roof trusses by the truss supplier, designed for the site's snow and wind loads "
            "(S0.1). Raised-heel (energy-heel) trusses for full attic insulation at the walls.",
        ]),
        ("FOR THE ENGINEER", [
            "Where the hip blocks meet, valleys and girder trusses bring point loads onto interior walls and "
            "headers: take them down through the main floor framing to the footings (S1.1).",
            "Snow drifting at the lower porch roofs against the higher house roofs (NBC 4.1.6 / 9.4.2).",
        ]),
        ("ENVELOPE (NBC 9.36, verify zone 7A/7B)", [
            "Attic insulation, ventilation (1/300) and an air barrier per 9.36 and 9.19; the energy "
            "advisor's model sets the final values (performance path).",
        ]),
    ]
    x = DRAW[0] + 8.2
    for t, items in notes:
        notes_column(bg, x, 2.62, t, items, 6.9, fs=6.0)
        x += 7.35
    pdf.savefig(fig)
    plt.close(fig)


def roof_heights():
    """Ridge height of each hip block (the roof's top at the block's centre line)."""
    out = []
    for x0, y0, x1, y1, eave, pitch, ov in M["main_roof"]:
        out.append(eave + (min(x1 - x0, y1 - y0) + 2 * ov) / 2 * pitch)      # as hip_roof() in house_lib.scad
    return out


def sheet_elevations(pdf, paths):
    fig, bg = new_sheet("A3.0", SCALE_TXT[S316])
    ridge = max(roof_heights())
    rows = [("elev_s", "SOUTH (FRONT) ELEVATION", 1, 17.25), ("elev_n", "NORTH (REAR) ELEVATION", 2, 11.75),
            ("elev_e", "EAST ELEVATION", 3, 6.25), ("elev_w", "WEST ELEVATION", 4, 0.75)]
    for name, title, n, y in rows:
        scad, look, ur, vr, depth, fpi, dpi, defs = VIEWS[name]
        x = DRAW[0] + 0.3
        ax = place_render(fig, name, paths, x, y + 0.55)
        u0, u1 = ax.get_xlim()
        grade_mask(ax, u0, u1, vr[0])
        for z, lab, below in [(0.0, "MAIN FLOOR " + el(0), False), (10.0, "PLATE " + el(10), False),
                              (12.0, "PLATE " + el(12), False), (ridge, "HIGHEST RIDGE " + el(ridge), False),
                              (GRADE, "GRADE " + el(GRADE), True)]:
            level_line(ax, z, lab, u0, u1, side="right", fs=5.4, below=below)
        view_title(bg, x, y + 0.3, n, title, SCALE_TXT[S316], "A3.0")
    tx = DRAW[0] + 18.6
    notes_column(bg, tx, 10.6, "ELEVATION NOTES", [
        "Views are orthographic renders of the model, at scale. Finished grade is drawn at -2'-0\"; "
        "the grading plan sets the real grades (slope away from the house).",
        "Cladding, roofing and trim materials are not selected yet; the envelope must meet NBC 9.36 "
        "(energy) and 9.27 (cladding) and suit the site's hail exposure.",
        "Window and door sizes: A6.0. Glazing area per wall face counts toward the spatial "
        "separation limits (NBC 9.10.15) if the house is near a property line - not expected on a rural lot.",
        f"Highest ridge about {ftin(ridge)} above the main floor ({ftin(ridge - GRADE)} above grade): "
        "check the land-use bylaw height limit.",
        "Porch floors 2'-0\" above grade: guards or raised grade (A1.2).",
        "The model draws door leaves open, so some doorways show as openings.",
    ], 11.0, fs=6.3)
    pdf.savefig(fig)
    plt.close(fig)


def section_overlay(ax, name, u_note):
    u0, u1 = ax.get_xlim()
    for z, lab, below in [(0.0, "MAIN FLOOR " + el(0), False), (GRADE, "GRADE " + el(GRADE), True),
                          (SLAB, "BASEMENT FLOOR " + el(SLAB), False),
                          (FTG_TOP - FTG_T, "U/S FOOTING " + el(FTG_TOP - FTG_T), True),
                          (10.0, "PLATE " + el(10), False), (12.0, "PLATE " + el(12), False)]:
        level_line(ax, z, lab, u0, u1, side="right", fs=5.2, text_u=u1 - 0.5, below=below)
    cv = Mpl(ax, VIEWS[name][5])
    cv.dim((u_note, SLAB), (u_note, 0.0), 2.0, "", text=f"{ftin(F2F)} FLOOR TO FLOOR", size=5.2)
    cv.dim((u_note, SLAB), (u_note, LV["basement_ceiling"] + SLAB), -1.2, "", text=f"{ftin(LV['basement_ceiling'])} CLG",
           size=5.2)


def sheet_sections_ab(pdf, paths):
    fig, bg = new_sheet("A4.0", SCALE_TXT[S316])
    ax = place_render(fig, "sec_a", paths, DRAW[0] + 0.4, 13.6)
    section_overlay(ax, "sec_a", 30.0)
    view_title(bg, DRAW[0] + 0.4, 13.3, "A", "SECTION A - EAST-WEST THROUGH THE STAIR, THEATER AND POOL",
               SCALE_TXT[S316], "A4.0")
    ax = place_render(fig, "sec_b", paths, DRAW[0] + 0.4, 3.2)
    section_overlay(ax, "sec_b", -60.0)
    view_title(bg, DRAW[0] + 0.4, 2.9, "B", "SECTION B - NORTH-SOUTH ALONG THE MAIN STAIR (LOOKING EAST)",
               SCALE_TXT[S316], "A4.0")
    notes_column(bg, DRAW[0] + 18.4, 11.6, "SECTION NOTES", [
        "Sections are cut through the model and drawn at scale; cut faces are darker than what is seen "
        "beyond. Earth is drawn round the foundation; grade at -2'-0\".",
        f"Main floor 0'-0\"; basement floor {el(SLAB)}; floor to floor {ftin(F2F)}; 12'-0\" basement ceilings.",
        f"ICF walls stand about {ftin(SILL - FTG_TOP)} from the footing to the sill, with "
        f"{ftin(GRADE - SLAB)} of backfill above the basement floor: beyond prescriptive ICF tables, "
        "engineered design required (S0.1).",
        "The ICF wall tops are held by the main floor: its diaphragm and the sill connection must take "
        "the soil load at the top of the wall (engineer).",
        "Plate heights 10'-0\" and 12'-0\" (8'-6\" garage); hip roofs at 6/12.",
        "Section A passes the stair opening: the headroom check is on A5.1.",
    ], 11.6, fs=6.3)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_sections_cde(pdf, paths):
    fig, bg = new_sheet("A4.1", SCALE_TXT[S316] + " U.N.O.")
    ax = place_render(fig, "sec_c", paths, DRAW[0] + 0.4, 13.6)
    section_overlay(ax, "sec_c", -60.0)
    view_title(bg, DRAW[0] + 0.4, 13.3, "C", "SECTION C - THROUGH THE THEATER (LOOKING EAST)", SCALE_TXT[S316], "A4.1")
    ax = place_render(fig, "sec_d", paths, DRAW[0] + 0.4, 3.2)
    section_overlay(ax, "sec_d", -60.0)
    view_title(bg, DRAW[0] + 0.4, 2.9, "D", "SECTION D - THROUGH THE POOL AND SPA (LOOKING EAST)", SCALE_TXT[S316],
               "A4.1")
    ax = place_render(fig, "sec_e", paths, DRAW[0] + 18.6, 13.6)
    u0, u1 = ax.get_xlim()
    for z, lab in [(GRADE, "GRADE " + el(GRADE)), (SLAB, "BASEMENT FLOOR " + el(SLAB))]:
        level_line(ax, z, lab, u0, u1, side="right", fs=5.4)
    view_title(bg, DRAW[0] + 18.6, 13.3, "E", "SECTION E - BASEMENT EXIT STAIR", SCALE_TXT[S38], "A4.1")
    notes_column(bg, DRAW[0] + 18.6, 10.9, "NOTES", [
        "C: the stepped theater floor - rear tier at the basement floor, one 7 1/2\" step, front tier "
        "15\" down; the lowered area stops 1'-0\" short of the side walls and 2'-6\" short of the screen wall, "
        "outside the footings' 1:1 bearing zones (A5.1).",
        "D: pool and spa shells, the deepened footings round the pool room and the pit's insulation and "
        "stone (A5.1).",
        f"E: the exit stair, {EXIT['risers']} risers up to grade along the gym's north wall, in an areaway "
        "with 8\" concrete walls and a 42\" guard (A5.1).",
    ], 11.3, fs=6.3)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_site(pdf, paths):
    fig, bg = new_sheet("A0.1", SCALE_TXT[S_SITE])
    ax = place_render(fig, "site", paths, DRAW[0] + 0.2, 2.75)
    view_title(bg, DRAW[0] + 0.2, 2.35, 1, "SITE PLAN - SCHEMATIC, NOT A SURVEY", SCALE_TXT[S_SITE], "A0.1")
    north_arrow(bg, DRAW[0] + 13.5, 1.6)
    scale_bar(bg, DRAW[0] + 15.0, 1.6, S_SITE, feet=(0, 20, 40, 80, 160))
    ax.text(69, 25, "HOUSE", fontsize=8, weight="bold", ha="center", va="center", color="white", zorder=6,
            bbox=dict(fc="#203f66", ec="none", pad=1.0, alpha=0.85))
    y = notes_column(bg, DRAW[0] + 20.0, 22.6, "THE HOUSE FIRST - ITS SITE AND SERVICES", [
        "The house is built first, on its own; the shop is a separate project with its own permits, later "
        "(its spot is kept clear, dashed).",
        "Driveway from the road (assumed on the south) up the west side to the garage's west-facing doors, "
        "plus the front loop round the garden. A road approach permit from the municipality.",
        "Power: underground from the road (the utility or REA sets the transformer and route) to a meter on "
        "the west wall; the panel is in the basement UTILITY room on that side.",
        "Gas: natural gas from the road if a gas utility or co-op serves it; otherwise a propane tank "
        "(1 000 US gal shown) on the west side, placed to the supplier's and CSA B149 clearances.",
        "Internet: fibre from an ISP on Alberta SuperNet if it reaches the road (in the same corridor), "
        "or Starlink (a dish with a clear view of the northern sky); either can back up the other.",
        "Water: a drilled well on the west side, near the UTILITY room, uphill of and at least 30 m "
        "(100 ft) from every septic part (our planning rule; the Standard of Practice minimums are smaller).",
        "Septic: tank east of the master wing, treatment field (where the treated water soaks into the "
        "soil) further east; a certified installer sizes both after the site evaluation.",
        "No utility tunnel: the shop will get buried service lines from the house's west side.",
    ], 9.6, fs=7.6)
    notes_column(bg, DRAW[0] + 20.0, y - 0.15, "THIS IS NOT THE PERMIT SITE PLAN", [
        "Land is not chosen yet: positions are relative to the house (models/site.scad, phase = house).",
        "For the development and building permits, replace this sheet with a plot plan by an Alberta Land "
        "Surveyor on the real parcel: property lines and setbacks; easements and pipelines; the buildings; "
        "the well and septic with their separation distances; the driveway and road approach; existing "
        "and finished grades with the main floor's geodetic elevation; drainage; any watercourse or slope.",
    ], 9.6, fs=7.6)
    pdf.savefig(fig)
    plt.close(fig)


# ============================================================ details (drawn)

MAT = {   # fill, hatch, hatch colour
    "concrete": ("#dcdcdc", "..", "#707070"),
    "eps": ("#fbf3c8", "xx", "#c9b56a"),
    "stone": ("#ece6d6", "oo", "#a89a78"),
    "earth": ("#f1e7d6", "////", "#b39b78"),
    "wood": ("#f1dcb2", None, None),
    "water": ("#d6ecf5", None, None),
    "gyp": ("#ffffff", None, None),
    "insul": ("#fdf0a6", "\\\\\\\\", "#d9b84a"),
}


def mat(ax, x0, z0, x1, z1, kind, lw=0.5, z=2):
    matp(ax, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], kind, lw, z)


def matp(ax, pts, kind, lw=0.5, z=2):
    fc, hatch, hc = MAT[kind]
    if hatch:
        ax.add_patch(MPoly(pts, closed=True, fc=fc, ec=hc, lw=0, hatch=hatch, zorder=z))
        ax.add_patch(MPoly(pts, closed=True, fc="none", ec=INK, lw=lw, zorder=z + 0.1))
    else:
        ax.add_patch(MPoly(pts, closed=True, fc=fc, ec=INK, lw=lw, zorder=z))


def detail_axes(fig, x, y, w, h, u0, z0, fpi):
    """Axes with the lower-left sheet corner (x, y) inches showing model (u0, z0) upward at fpi."""
    ax = fig.add_axes([x / SHEET_W, y / SHEET_H, w / SHEET_W, h / SHEET_H])
    ax.set_xlim(u0, u0 + w * fpi)
    ax.set_ylim(z0, z0 + h * fpi)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax


def note(ax, p, t, s, fs=5.8, ha="left"):
    ax.annotate(s, xy=p, xytext=t, fontsize=fs, ha=ha, va="center", zorder=9, linespacing=1.15,
                arrowprops=dict(arrowstyle="-", lw=0.35, color=INK, shrinkA=1, shrinkB=0),
                bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.6))
    ax.plot([p[0]], [p[1]], marker="o", ms=1.6, color=INK, zorder=9)


def tag(ax, u, z, s, fpi, fs=5.6, side="right", color=RED):
    k = 0.06 * fpi
    ax.add_patch(MPoly([(u - k, z + 1.4 * k), (u + k, z + 1.4 * k), (u, z)], closed=True, fc=color, ec=color, zorder=9))
    ax.text(u + (1.6 * k if side == "right" else -1.6 * k), z + 0.8 * k, s, fontsize=fs, color=color,
            ha="left" if side == "right" else "right", va="center", zorder=9)


def detail_title(bg, x, y, n, title, scale, sheet):
    view_title(bg, x, y, n, title, scale, sheet)


def det_icf(fig, bg, x, y):
    """Typical basement wall, from the footing to the main floor wall."""
    fpi = S34
    u0, u1, z0, z1 = -6.2, 7.2, -16.6, 2.3
    ax = detail_axes(fig, x, y, (u1 - u0) / fpi, (z1 - z0) / fpi, u0, z0, fpi)
    cv = Mpl(ax, fpi)
    h, c = ICF / 2, CORE / 2
    ftb = FTG_TOP - FTG_T
    # ground: subgrade under everything, backfill outside up to the sloped grade
    mat(ax, u0, ftb - 0.9, u1, FTG_TOP, "earth", z=1)
    matp(ax, [(u0, FTG_TOP), (-h, FTG_TOP), (-h, GRADE), (u0, GRADE - 0.35)], "earth", z=1)
    ax.plot([u0, -h], [GRADE - 0.35, GRADE], color=INK, lw=1.0, zorder=4)
    # drainage stone + weeping tile beside the footing
    matp(ax, [(-2.15, ftb), (-1.0, ftb), (-1.0, FTG_TOP), (-h, FTG_TOP), (-h, FTG_TOP + 0.75),
              (-2.15, FTG_TOP + 0.75)], "stone", z=2.4)
    ax.add_patch(Circle((-1.6, FTG_TOP + 0.2), 0.17, fc="white", ec=INK, lw=0.7, zorder=3))
    # footing, ICF wall, membrane, slab
    mat(ax, -FTG_W / 2, ftb, FTG_W / 2, FTG_TOP, "concrete", z=3)
    mat(ax, -h, FTG_TOP, -c, SILL, "eps", z=3)
    mat(ax, c, FTG_TOP, h, SILL, "eps", z=3)
    mat(ax, -c, FTG_TOP, c, SILL, "concrete", z=3)
    ax.plot([-h - 0.03] * 2, [FTG_TOP, GRADE + 0.5], color=INK, lw=1.6, zorder=4)
    for zz in np.arange(FTG_TOP + 0.6, SILL - 0.3, 1.33):
        ax.plot([-0.1], [zz], marker="o", ms=1.4, color="#333333", zorder=4)
    ax.plot([0.1, 0.1], [FTG_TOP - 0.55, SILL - 0.1], color="#333333", lw=0.7, zorder=4)
    ax.plot([0.1, 0.55], [FTG_TOP - 0.55, FTG_TOP - 0.55], color="#333333", lw=0.7, zorder=4)
    mat(ax, h, SLAB, h + 0.045, SILL - 0.3, "gyp", lw=0.5, z=3.2)
    mat(ax, h, FTG_TOP, u1, SLAB - SLAB_T, "stone", z=2.4)
    mat(ax, h, SLAB - SLAB_T, u1, SLAB, "concrete", z=3)
    ax.plot([h, u1], [SLAB - SLAB_T, SLAB - SLAB_T], color=INK, lw=1.0, ls=(0, (3, 1.5)), zorder=4)
    # main floor: sill plate, rim, trusses, subfloor, and the 2x6 wall above
    sw = 0.229
    mat(ax, -sw, SILL, sw, SILL + 0.125, "wood", z=3)
    mat(ax, -sw, SILL + 0.125, -sw + 0.125, -0.0625, "wood", z=3)
    ax.add_patch(Rectangle((-sw + 0.125, SILL + 0.125), u1 - (-sw + 0.125), -0.0625 - SILL - 0.125, fc="#fbf4e4",
                           ec=INK, lw=0.4, zorder=2.9))
    for uu in np.arange(0.3, u1, 1.2):
        ax.plot([uu, uu + 0.6, uu + 1.2], [SILL + 0.2, -0.14, SILL + 0.2], color=GREY, lw=0.4, zorder=3)
    mat(ax, -sw, -0.0625, u1, 0.0, "wood", z=3)
    mat(ax, -sw, 0.0, sw, z1, "insul", z=3)
    mat(ax, -sw, 0.0, sw, 0.125, "wood", z=3.1)
    mat(ax, sw, 0.0, sw + 0.045, z1, "gyp", lw=0.4, z=3)
    mat(ax, -sw - 0.036, -0.4, -sw, z1, "wood", lw=0.4, z=3)
    ax.plot([-0.42, -0.42], [-0.5, z1], color=INK, lw=0.9, zorder=4)
    ax.plot([-0.5, -0.25, -0.25], [-0.62, -0.45, -0.4], color=INK, lw=0.8, zorder=4)
    f = 6.4
    note(ax, (-0.42, 1.2), (-5.3, 1.5), "2x6 WALL: CLADDING ON A RAINSCREEN,\nSHEATHING; FLASHING OVER THE ICF", fs=f)
    note(ax, (-3.5, GRADE - 0.17), (-5.3, -0.9), "FINISHED GRADE, SLOPED AWAY\nFROM THE HOUSE", fs=f)
    note(ax, (-h - 0.03, -4.5), (-5.3, -4.2), "WATERPROOFING MEMBRANE +\nDRAINAGE BOARD, TO GRADE", fs=f)
    note(ax, (-3.0, -7.5), (-5.3, -7.0), "FREE-DRAINING BACKFILL\n(PER GEOTECH)", fs=f)
    note(ax, (-0.1, FTG_TOP + 0.6 + 1.33 * 5), (-5.3, -9.6), "REINFORCEMENT BY ENGINEER\n(EXPECT 15M VERT. + HORIZ.\n"
         "@ ABOUT 400 O.C.); DOWELS\nFROM THE FOOTING", fs=f)
    note(ax, (-1.6, FTG_TOP + 0.2), (-5.3, -12.6), "4\" WEEPING TILE IN CLEAR\nSTONE, FILTER CLOTH, TO\nTHE SUMP",
         fs=f)
    note(ax, (-0.5, ftb + 0.3), (-5.3, -16.1), "24\" x 10\" FOOTING ON UNDISTURBED\nSOIL; BEARING PER GEOTECH",
         fs=f)
    note(ax, (0.0, SILL + 0.06), (2.4, -2.6), "P.T. SILL PLATE ON A GASKET; ANCHORS\nAND WALL-TOP BRACING BY "
         "ENGINEER", fs=f)
    note(ax, (3.5, (SILL - 0.0625) / 2), (2.4, 1.3), "FLOOR TRUSSES BY THE TRUSS DESIGNER,\nRIM BOARD, 3/4\" "
         "SUBFLOOR", fs=f)
    note(ax, (c + 0.1, -5.5), (2.4, -5.5), "13 1/4\" ICF: 8\" CONCRETE CORE,\n2 5/8\" EPS EACH FACE", fs=f)
    note(ax, (h + 0.03, -8.0), (2.4, -8.0), "1/2\" GYPSUM THERMAL BARRIER\nOVER THE FOAM (NBC 9.10.17.10):\n"
         "PHASE 1, BEFORE OCCUPANCY", fs=f)
    note(ax, (4.0, SLAB - 0.15), (2.4, -11.6), "4\" SLAB ON 10 MIL POLY (SEALED, TAPED\nTO THE WALL) ON 6\" CLEAR "
         "STONE =\nRADON LAYER (NBC 9.13.4); 2\" RIGID\nINSULATION UNDER IT RECOMMENDED", fs=f)
    t = 6.0
    tag(ax, 5.2, 0.0, "MAIN FLOOR " + el(0), fpi, fs=t)
    tag(ax, -0.7, SILL, "T/O ICF " + el(SILL), fpi, fs=t, side="left")
    tag(ax, 5.2, SLAB, "BSMT FLOOR " + el(SLAB), fpi, fs=t)
    tag(ax, 1.0, ftb, "U/S FTG " + el(ftb), fpi, fs=t)
    cv.dim((-1.5, GRADE), (-1.5, 0.0), 0.0, "", size=5.6)
    cv.dim((-5.85, ftb), (-5.85, GRADE), 0.0, "", size=5.6)
    cv.dim((6.6, SLAB), (6.6, 0.0), 0.0, "", size=5.6)
    cv.dim((5.4, SLAB), (5.4, SLAB + LV["basement_ceiling"]), 0.0, "", text=ftin(LV["basement_ceiling"]) + " CEILING",
           size=5.6)
    cv.dim((-FTG_W / 2, ftb - 0.45), (FTG_W / 2, ftb - 0.45), 0.0, "", size=5.6)
    detail_title(bg, x, y - 0.25, 1, "TYPICAL ICF BASEMENT WALL", SCALE_TXT[S34], "A5.0")


def det_frost(fig, bg, x, y):
    fpi = S34
    ax = detail_axes(fig, x, y, 6.0, 5.6, -3.0, -7.0, fpi)
    cv = Mpl(ax, fpi)
    w = 8 / 12
    ft_top = FROST_BOT + 8 / 12
    crawl = SILL - 1.5
    mat(ax, -3.0, FROST_BOT - 0.4, -w / 2, GRADE, "earth")
    mat(ax, w / 2, FROST_BOT - 0.4, 4.9, crawl, "earth")
    mat(ax, -10 / 12, FROST_BOT, 10 / 12, ft_top, "concrete", z=3)
    mat(ax, -w / 2, ft_top, w / 2, SILL, "concrete", z=3)
    mat(ax, w / 2, crawl - 1.5, w / 2 + 0.25, SILL - 0.05, "insul", z=3)
    ax.plot([w / 2, 4.9], [crawl + 0.03, crawl + 0.03], color=INK, lw=1.2, zorder=4)
    mat(ax, -w / 2, SILL, w / 2 - 0.1, SILL + 0.125, "wood", z=3)
    mat(ax, -w / 2, SILL + 0.125, 4.9, -0.0625, "wood", z=2.5, lw=0.3)
    mat(ax, -w / 2, -0.0625, 4.9, 0.0, "wood", z=3)
    ax.text(2.6, SILL / 2, "FLOOR TRUSSES", fontsize=4.8, ha="center", va="center")
    mat(ax, -0.229 - 0.1, 0.0, 0.229 - 0.1, 0.9, "wood", z=3)
    note(ax, (0.0, -4.0), (-2.9, -4.6), "8\" CONCRETE\nFROST WALL", ha="left")
    note(ax, (0.6, FROST_BOT + 0.3), (1.6, -6.4), "20\" x 8\" FOOTING, U/S 4'-0\"\nBELOW GRADE (NBC-AE MIN. 1.2 m)",
         ha="left")
    note(ax, (w / 2 + 0.12, -3.6), (1.6, -4.3), "RIGID INSULATION, INSIDE FACE\n(CONDITIONED CRAWLSPACE)", ha="left")
    note(ax, (3.5, crawl + 0.03), (1.6, -2.6), "SEALED GROUND COVER ON STONE,\nTIED TO THE RADON LAYER", ha="left")
    tag(ax, 4.6, 0.0, "MAIN FLOOR " + el(0), fpi)
    tag(ax, -2.2, GRADE, "GRADE " + el(GRADE), fpi)
    cv.dim((-1.3, FROST_BOT), (-1.3, GRADE), 0.0, "", size=5)
    cv.dim((4.6, crawl), (4.6, SILL), 0.0, "", text="18\" CLEAR", size=5)
    detail_title(bg, x, y - 0.25, 2, "FROST WALL AT CRAWLSPACE", SCALE_TXT[S34], "A5.0")


def det_bearing(fig, bg, x, y):
    fpi = S34
    ax = detail_axes(fig, x, y, 5.0, 3.6, -3.3, -16.0, fpi)
    cv = Mpl(ax, fpi)
    ftb = FTG_TOP - FTG_T
    mat(ax, -3.3, ftb - 0.4, 3.3, FTG_TOP, "earth")
    mat(ax, -3.3, FTG_TOP, 3.3, SLAB - SLAB_T, "stone", z=2.5)
    mat(ax, -3.3, SLAB - SLAB_T, 3.3, SLAB, "concrete", z=3)
    matp(ax, [(-0.835, ftb), (0.835, ftb), (0.835, SLAB - SLAB_T), (-0.835, SLAB - SLAB_T)], "concrete", z=3)
    mat(ax, -0.229, SLAB, 0.229, SLAB + 0.125, "wood", z=3)
    mat(ax, -0.229, SLAB + 0.125, 0.229, -12.4, "wood", z=3)
    note(ax, (0.0, -12.8), (1.0, -12.75), "BEARING WALL (2x6 ON SILL GASKET)\nOR STEEL POSTS + BEAM - PHASE 1",
         ha="left")
    note(ax, (0.5, ftb + 0.3), (1.2, -15.6), "20\" x 10\" STRIP FOOTING, SLAB\nTHICKENED TO IT; SIZE BY ENGINEER",
         ha="left")
    cv.dim((-0.835, ftb - 0.25), (0.835, ftb - 0.25), 0.0, "", size=5)
    detail_title(bg, x, y - 0.25, 3, "INTERIOR BEARING LINE FOOTING", SCALE_TXT[S34], "A5.0")


def det_pier(fig, bg, x, y):
    fpi = S34
    ax = detail_axes(fig, x, y, 4.2, 5.2, -2.6, -7.0, fpi)
    cv = Mpl(ax, fpi)
    bot = GRADE - 4.5
    mat(ax, -2.6, bot - 0.3, 2.6, GRADE, "earth")
    matp(ax, [(-1.0, bot), (1.0, bot), (1.0, bot + 0.33), (0.5, bot + 0.67), (-0.5, bot + 0.67), (-1.0, bot + 0.33)],
         "concrete", z=3)
    mat(ax, -0.5, bot + 0.67, 0.5, GRADE + 1.5, "concrete", z=3)
    mat(ax, -0.25, GRADE + 1.5, 0.25, -0.6, "wood", z=3)
    mat(ax, -1.6, -0.6, 1.6, 0.0, "wood", z=3)
    note(ax, (0.0, GRADE + 1.55), (0.9, -0.9 + 0.0), "POST BASE, ANCHORED", ha="left")
    note(ax, (0.3, -4.0), (1.0, -3.6), "12\" SONOTUBE PIER", ha="left")
    note(ax, (0.6, bot + 0.3), (1.0, -6.8), "24\" BELL, U/S 4'-6\"\nBELOW GRADE", ha="left")
    cv.dim((-1.6, bot), (-1.6, GRADE), 0.0, "", size=5)
    tag(ax, 1.6, 0.0, "PORCH " + el(0), fpi)
    detail_title(bg, x, y - 0.25, 4, "PORCH PIER", SCALE_TXT[S34], "A5.0")


def det_garage(fig, bg, x, y):
    fpi = S34
    ax = detail_axes(fig, x, y, 5.8, 5.2, -3.0, -7.0, fpi)
    cv = Mpl(ax, fpi)
    w = 8 / 12
    ft_top = FROST_BOT + 8 / 12
    gs = -1.5
    mat(ax, -3.0, FROST_BOT - 0.4, -w / 2, GRADE, "earth")
    mat(ax, w / 2, FROST_BOT - 0.4, 4.7, gs - SLAB_T - BASE_T, "earth")
    mat(ax, w / 2, gs - SLAB_T - BASE_T, 4.7, gs - SLAB_T, "stone", z=2.5)
    mat(ax, w / 2, gs - SLAB_T, 4.7, gs, "concrete", z=3)
    mat(ax, -10 / 12, FROST_BOT, 10 / 12, ft_top, "concrete", z=3)
    mat(ax, -w / 2, ft_top, w / 2, -1.25, "concrete", z=3)
    mat(ax, w / 2, gs - 2.0, w / 2 + 0.17, gs - SLAB_T, "insul", z=3)
    mat(ax, -w / 2, -1.25, w / 2 - 0.1, -1.125, "wood", z=3)
    mat(ax, -0.229 - 0.1, -1.125, 0.229 - 0.1, 0.6, "wood", z=3)
    note(ax, (2.5, gs - 0.15), (1.2, -0.3), "4\" GARAGE SLAB (C-2, 32 MPa, AIR-ENTRAINED)\nON 6\" STONE; SLOPE TO THE "
         "DOORS", ha="left")
    note(ax, (0.0, -1.2), (-2.9, 0.2), "3\" CURB ABOVE\nTHE SLAB", ha="left")
    note(ax, (0.0, -4.5), (-2.9, -4.9), "8\" FROST WALL\nON 20\" x 8\" FTG", ha="left")
    note(ax, (w / 2 + 0.08, gs - 1.0), (1.4, -4.0), "RIGID INSULATION AT THE\nSLAB EDGE (OPTIONAL, HEATED)", ha="left")
    tag(ax, 4.4, gs, "GARAGE " + el(gs), fpi)
    tag(ax, -2.2, GRADE, "GRADE " + el(GRADE), fpi)
    cv.dim((-1.3, FROST_BOT), (-1.3, GRADE), 0.0, "", size=5)
    detail_title(bg, x, y - 0.25, 5, "GARAGE SLAB EDGE", SCALE_TXT[S34], "A5.0")


def sheet_details_foundation(pdf):
    fig, bg = new_sheet("A5.0", "AS NOTED")
    det_icf(fig, bg, DRAW[0] + 0.1, 7.9)
    det_frost(fig, bg, DRAW[0] + 10.9, 16.3)
    det_pier(fig, bg, DRAW[0] + 17.7, 16.6)
    det_garage(fig, bg, DRAW[0] + 10.9, 8.6)
    det_bearing(fig, bg, DRAW[0] + 17.4, 10.4)
    notes_column(bg, DRAW[0] + 23.6, 22.4, "FOUNDATION - FOR THE ENGINEER", [
        "**Design items (S0.1)",
        "ICF walls: about 13'-0\" tall with 11'-9\" of backfill - beyond prescriptive tables. Vertical and "
        "horizontal steel, wall-top support by the floor, lintels over the door and windows.",
        "Footings: size from the geotech's bearing capacity; steps where the pool room footings deepen.",
        "Interior bearing lines: strip footings for the line loads from the main floor and the roof's "
        "girder trusses (S1.1).",
        "Areaway and light wells: 8\" cantilevered retaining walls, 11'-9\" and 8'-0\" of soil.",
        "**Assumed until the engineer and geotech say otherwise",
        "Concrete: footings and walls S-class (sulphate) per the geotech, else N.",
        "Frost: footings 4'-0\" below grade where there is no basement (NBC-AE minimum 1.2 m).",
        "Radon: sealed 10 mil poly, 6\" clear stone, a capped pipe through the slab, NBC 9.13.4.",
        "Thermal barrier: 1/2\" gypsum over all interior foam before occupancy, even with the basement "
        "unfinished (NBC 9.10.17.10).",
        "**Inspections",
        "Footing and wall inspections by the authority having jurisdiction, and field reviews by the "
        "engineer of the reinforcement before each pour.",
    ], 6.5, fs=7.0)
    pdf.savefig(fig)
    plt.close(fig)


def det_pool(fig, bg, x, y):
    """Pool + spa, a section through x = 86 looking east (north at left: u = -y)."""
    fpi = S38
    ax = detail_axes(fig, x, y, 37.6 / S38, 16.0 / S38, -54.1, -21.5, fpi)
    cv = Mpl(ax, fpi)
    p, s = POOL["xy"], SPA["xy"]
    sh, fl, ins = POOL["shell_t"], POOL["shell_floor"], POOL["insul"]
    U = lambda yy: -yy                                                    # noqa: E731
    pb, sb = POOL["bottom"], SPA["bottom"]
    deep = M["deep_footings"][0][4]
    ftb = FTG_TOP - FTG_T
    mat(ax, U(18.15 - 0.55), deep - 0.5, U(52.76 + 0.55), FTG_TOP, "earth", z=1)
    # stone + insulation under the shells, stone under the slab
    for (xy, bot) in ((p, pb), (s, sb)):
        mat(ax, U(xy[3] + sh + ins), bot - ins - BASE_T, U(xy[1] - sh - ins), bot - ins, "stone", z=2.4)
        mat(ax, U(xy[3] + sh + ins), bot - ins, U(xy[1] - sh - ins), bot, "eps", z=2.5)
    mat(ax, U(52.76 - 0.55), FTG_TOP, U(p[3] + sh), SLAB - SLAB_T, "stone", z=2.4)
    mat(ax, U(s[1] - sh), FTG_TOP, U(18.15 + 0.55), SLAB - SLAB_T, "stone", z=2.4)
    # deck slab
    mat(ax, U(52.76 - 0.55), SLAB - SLAB_T, U(p[3] + sh), SLAB, "concrete", z=3)
    mat(ax, U(s[1] - sh), SLAB - SLAB_T, U(18.15 + 0.55), SLAB, "concrete", z=3)
    # shells
    mat(ax, U(p[3] + sh), pb, U(p[1]), pb + fl, "concrete", z=3)
    mat(ax, U(p[3] + sh), pb + fl, U(p[3]), SLAB, "concrete", z=3)
    mat(ax, U(s[3] + sh), sb, U(s[1] - sh), sb + fl, "concrete", z=3)
    mat(ax, U(p[1]), sb + fl, U(p[1] - sh), SPA["water"], "concrete", z=3)        # shared wall, at the spillway
    mat(ax, U(s[1]), sb + fl, U(s[1] - sh), SPA["rim"], "concrete", z=3)
    mat(ax, U(p[1]), pb, U(s[3]), sb + fl, "concrete", z=3)
    for xy, top in ((p, POOL["water"]), (s, SPA["water"])):
        bottom = (pb if xy is p else sb) + fl
        mat(ax, U(xy[3]), bottom, U(xy[1]), top, "water", lw=0.3, z=2.8)
    # perimeter walls and the deepened footings
    for yy in (18.15, 52.76):
        mat(ax, U(yy) - ICF / 2, FTG_TOP, U(yy) + ICF / 2, SLAB + 2.5, "concrete", z=3)
        mat(ax, U(yy) - FTG_W / 2, ftb, U(yy) + FTG_W / 2, FTG_TOP, "concrete", z=3)
        mat(ax, U(yy) - 0.5, deep, U(yy) + 0.5, ftb, "concrete", z=3)
    ax.plot([U(52.76) - ICF / 2 - 3, U(52.76) - ICF / 2], [GRADE, GRADE], color=INK, lw=0.8)
    note(ax, (U(40.0), POOL["water"] - 2.0), (U(44.0), -10.3), f"POOL {ftin(p[3] - p[1])} x {ftin(p[2] - p[0])}, "
         f"{ftin(POOL['depth'])} WATER, NO DIVING", ha="left")
    note(ax, (U(28.0), SPA["water"] - 1.5), (U(29.5), -10.3), f"SPA {ftin(s[3] - s[1])}, {ftin(SPA['depth'])} WATER,"
         " RIM 18\" ABOVE DECK", ha="left")
    note(ax, (U(p[1] - sh / 2), SPA["water"]), (U(33.2), -11.2), "SPILLWAY IN THE SHARED WALL", ha="left")
    note(ax, (U(p[3] + sh / 2), -17.0), (U(51.6), -18.4), "9\" SHOTCRETE WALLS, 10\" FLOOR,\n35 MPa, w/cm 0.40, "
         "15M @ 12\"\nE.W. (BY ENGINEER)", ha="left")
    note(ax, (U(42.0), pb - ins / 2), (U(41.0), -21.0), "2\" RIGID INSULATION ON 6\" STONE WITH A DRAIN LOOP TO THE "
         "SUMP; HYDROSTATIC RELIEF VALVE IN THE FLOOR", ha="left")
    note(ax, (U(52.76), deep + 1.0), (U(51.0), -20.6), f"DEEPENED FOOTING TO {el(deep)}", ha="left")
    note(ax, (U(18.15), deep + 1.0), (U(20.0), -20.2), "DEEPENED FOOTING (OR SHELL\nDESIGNED TO RETAIN IT)",
         ha="left")
    tag(ax, U(46.0), POOL["water"], "WATER " + el(POOL["water"]), fpi, fs=5.2)
    tag(ax, U(25.5), SPA["rim"], "RIM " + el(SPA["rim"]), fpi, fs=5.2)
    tag(ax, U(21.0), SLAB, "DECK " + el(SLAB), fpi, fs=5.2)
    cv.dim((U(46.5), POOL["water"] - POOL["depth"]), (U(46.5), POOL["water"]), 0.0, "", size=5)
    cv.dim((U(24.5), SPA["water"] - SPA["depth"]), (U(24.5), SPA["water"]), 0.0, "", size=5)
    detail_title(bg, x, y - 0.25, 1, "POOL AND SPA (SECTION D)", SCALE_TXT[S38], "A5.1")


def det_theater(fig, bg, x, y):
    """Theater tiers, a section through x = 62 looking east (north at left: u = -y), with the sightline."""
    fpi = S38
    ax = detail_axes(fig, x, y, 23.5 / S38, 16.1 / S38, -51.5, -16.6, fpi)
    cv = Mpl(ax, fpi)
    U = lambda yy: -yy                                                    # noqa: E731
    tiers = THEA["tiers"]
    ys = THEA["xy"]
    st = THEA["stage"]
    mat(ax, U(50.35 + 0.55), -16.6, U(29.12 - 0.2), FTG_TOP - 0.3, "earth", z=1)
    floor = [(tiers[0][0], tiers[0][1], 0.0), (tiers[1][0], tiers[1][1], tiers[1][2]),
             (tiers[2][0], tiers[2][1], tiers[2][2]), (st[0], st[1], 0.0)]
    for (a, b, d) in floor:
        zt = SLAB - d
        mat(ax, U(b), zt - SLAB_T - BASE_T, U(a), zt - SLAB_T, "stone", z=2.4)
        mat(ax, U(b), zt - SLAB_T, U(a), zt, "concrete", z=3)
    mat(ax, U(50.35) - ICF / 2, FTG_TOP - FTG_T, U(50.35) + ICF / 2, -1.625, "concrete", z=3)
    mat(ax, U(29.12) - 0.2, SLAB, U(29.12) + 0.2, -1.75, "wood", z=3, lw=0.3)
    mat(ax, U(50.35) + ICF / 2, -1.75 - 0.05, U(29.12) - 0.2, -1.625, "gyp", lw=0.3, z=3)
    ax.add_patch(Rectangle((U(49.8) - 0.1, SLAB + 1.5), 0.1, 4.896, fc="#333333", ec="none", zorder=4))
    eyes = [(49.8 - 18.2, SLAB + 40 / 12), (49.8 - 10.3, SLAB - 1.25 + 40 / 12)]
    seats = [(30.5, 33.7, SLAB), (38.4, 41.6, SLAB - 1.25)]
    for (a, b, z0) in seats:
        matp(ax, [(U(a), z0), (U(b), z0), (U(b), z0 + 1.6), (U(a + 0.6), z0 + 1.6), (U(a + 0.4), z0 + 3.4),
                  (U(a), z0 + 3.4)], "wood", lw=0.4, z=3)
    sb = (U(49.8), SLAB + 1.5)
    for (yy, ze) in eyes:
        ax.plot([U(yy)], [ze], marker="o", ms=2.2, color=RED, zorder=6)
    ax.plot([U(eyes[0][0]), sb[0]], [eyes[0][1], sb[1]], color=RED, lw=0.6, ls=(0, (6, 2)), zorder=6)
    ax.plot([U(eyes[1][0]), U(eyes[1][0])], [eyes[1][1], eyes[1][1] + 4.75 / 12], color=RED, lw=1.2, zorder=6)
    note(ax, (U(42.0), -12.05), (U(36.0), -6.3), "REAR SIGHTLINE TO THE SCREEN BOTTOM CLEARS THE FRONT ROW'S\nHEAD "
         "(EYE 40\" ABOVE THE TIER, HEAD +4 3/4\"): 5.4\" ABOVE THE EYE", ha="left")
    note(ax, (U(49.8), -9.0), (U(46.5), -4.0), "120\" 16:9 SCREEN,\n18\" ABOVE THE STAGE", ha="left")
    note(ax, (U(42.0), SLAB - 1.25 - 0.2), (U(44.0), -16.3), "DEPRESSED SLAB: FRONT TIER 15\" DOWN, ONE 7 1/2\" STEP; "
         "POLY + STONE CONTINUOUS", ha="left")
    tag(ax, U(30.5), SLAB, "REAR TIER " + el(SLAB), fpi, fs=5.0)
    tag(ax, U(46.5), SLAB - 1.25, "FRONT " + el(SLAB - 1.25), fpi, fs=5.0, side="left")
    cv.dim((U(36.6), SLAB - 1.25), (U(36.6), SLAB), -0.8, "", size=4.8)
    detail_title(bg, x, y - 0.25, 2, "THEATER TIERS AND SIGHTLINE (SECTION C)", SCALE_TXT[S38], "A5.1")


def det_exit(fig, bg, x, y):
    """Exit stair along y = mid-areaway, looking north (u = x)."""
    fpi = S14
    ax = detail_axes(fig, x, y, 7.6, 5.2, 42.0, -16.6, fpi)
    cv = Mpl(ax, fpi)
    a, t = EXIT["areaway"], EXIT["wall_t"]
    n, run = EXIT["risers"], EXIT["run"]
    rise = EXIT["rise"] / n
    lx = EXIT["landing_x"]
    zf = SLAB - SLAB_T
    mat(ax, 42.0, -16.6, a[0] - t, GRADE, "earth", z=1)
    mat(ax, a[0] - t, -16.6, 72.4, zf - BASE_T, "earth", z=1)
    mat(ax, a[0], zf - BASE_T, a[2], zf, "stone", z=2.4)
    pts = [(a[0], SLAB), (lx[1], SLAB)]
    for i in range(1, n):
        x0 = lx[1] + (i - 1) * run
        pts += [(x0, SLAB + i * rise), (x0 + run, SLAB + i * rise)]
    pts += [(a[2], GRADE), (a[2] + EXIT["top_pad"], GRADE), (a[2] + EXIT["top_pad"], GRADE - 0.33),
            (a[2], GRADE - 0.33), (a[2], zf), (a[0], zf)]
    matp(ax, pts, "concrete", z=3)
    mat(ax, a[2] + EXIT["top_pad"], GRADE - 1.0, 72.4, GRADE, "earth", z=1)
    mat(ax, a[0] - t, zf, a[0], GRADE + 0.5, "concrete", z=3)
    mat(ax, a[0] - t - 0.5 - 0.3, zf - FTG_T, a[0] + 0.5, zf, "concrete", z=3)
    ax.plot([a[0] - t / 2, a[0] - t / 2], [GRADE + 0.5, GRADE + 3.5], color=INK, lw=1.0)
    ax.plot([a[0] - t / 2 - 0.2, a[2]], [GRADE + 3.5, GRADE + 3.5], color=INK, lw=1.4)
    ax.plot([a[0] - t / 2, a[2]], [GRADE + 3.5 - 0.0, GRADE + 3.5], color=INK, lw=1.4)
    ax.plot([lx[1], a[2]], [SLAB + 2.9, GRADE + 2.9], color=INK, lw=0.8)
    note(ax, (47.5, SLAB + 0.05), (43.0, -15.6), f"LANDING {ftin(lx[1] - lx[0])} AT THE BASEMENT FLOOR; AREA DRAIN "
         "TO THE WEEPING TILE / SUMP", ha="left")
    note(ax, (58.0, SLAB + 4.0 * 1), (52.0, -6.0), f"{n} RISERS x {ftin(rise)} = {ftin(EXIT['rise'])}\n{n - 1} TREADS x "
         f"{ftin(run)} (EXTERIOR, NON-SLIP)", ha="left")
    note(ax, (56.0, -6.2), (47.0, -3.0), "HANDRAILS 34\"-38\" BOTH SIDES (4'-0\" CLEAR)", ha="left")
    note(ax, (50.0, GRADE + 3.5), (52.0, 1.8), "42\" GUARD ON THE 6\" CURB ROUND THE AREAWAY", ha="left")
    note(ax, (a[0] - t / 2, -8.0), (43.0, -11.0), "8\" CONC.\nRETAINING\nWALL", ha="left")
    tag(ax, 69.5, GRADE, "GRADE " + el(GRADE), fpi, fs=5.0)
    tag(ax, 46.4, SLAB, "LANDING " + el(SLAB), fpi, fs=5.0)
    detail_title(bg, x, y - 0.25, 3, "BASEMENT EXIT STAIR (SECTION E)", SCALE_TXT[S14], "A5.1")


def det_well(fig, bg, x, y):
    """The living room light well, a section at x = 44 looking east (north at left: u = -y)."""
    fpi = S38
    ax = detail_axes(fig, x, y, 4.6, 18.4 / S38, -9.8, -16.0, fpi)
    cv = Mpl(ax, fpi)
    U = lambda yy: -yy                                                    # noqa: E731
    w = M["base_windows"][0]
    c, t = w[6], EXIT["wall_t"]
    zf = well_floor(w)
    sill, head = SLAB + w[4], SLAB + w[4] + w[5]
    h = ICF / 2
    mat(ax, U(c[1] - t), -16.0, U(-2.4), GRADE, "earth", z=1)
    mat(ax, U(c[1] - t) - 0.0, zf - BASE_T - FTG_T, U(c[1]), zf - BASE_T, "earth", z=1)
    mat(ax, U(5.79) + h, zf - BASE_T - 3.0, U(c[1]), zf - BASE_T, "earth", z=1)
    mat(ax, U(5.79) + h, zf - BASE_T, U(c[1]), zf, "stone", z=2.4)
    mat(ax, U(c[1]), zf - BASE_T, U(c[1] - t), GRADE + 0.5, "concrete", z=3)
    mat(ax, U(c[1] - t / 2) - 0.835, zf - BASE_T - FTG_T, U(c[1] - t / 2) + 0.835, zf - BASE_T, "concrete", z=3)
    for (a0, a1) in ((FTG_TOP, sill), (head, SILL)):
        mat(ax, U(5.79) - h, a0, U(5.79) - CORE / 2, a1, "eps", z=3)
        mat(ax, U(5.79) + CORE / 2, a0, U(5.79) + h, a1, "eps", z=3)
        mat(ax, U(5.79) - CORE / 2, a0, U(5.79) + CORE / 2, a1, "concrete", z=3)
    mat(ax, U(5.79) - h, sill, U(5.79) + h, head, "water", lw=0.4, z=3)
    ax.plot([U(5.79)] * 2, [sill, head], color=INK, lw=0.5, zorder=4)
    mat(ax, U(5.79) - h - 1.5, SLAB - SLAB_T, U(5.79) - h, SLAB, "concrete", z=3)
    mat(ax, U(5.79) - FTG_W / 2, FTG_TOP - FTG_T, U(5.79) + FTG_W / 2, FTG_TOP, "concrete", z=3)
    ax.plot([U(c[1] - t / 2)] * 2, [GRADE + 0.5, GRADE + 3.5], color=INK, lw=1.0)
    ax.plot([U(c[1] - t / 2), U(c[3])], [GRADE + 3.5] * 2, color=INK, lw=1.4)
    note(ax, (U(5.79), (sill + head) / 2), (U(9.5), -7.3), f"WINDOW {ftin(w[3])} x {ftin(w[5])} IN AN ICF BUCK,\n"
         "LINTEL BY ENGINEER", ha="left")
    note(ax, (U(2.5), zf - 0.2), (U(9.5), -12.4), "WELL FLOOR 6\" BELOW THE SILL:\nSTONE, DRAIN TO THE WEEPING TILE",
         ha="left")
    note(ax, (U(c[1] - t / 2), -5.0), (U(-0.3), -3.4), "8\" CONC. WALL\nON 20\" FTG", ha="left")
    note(ax, (U(2.0), GRADE + 3.5), (U(4.5), -0.2), "42\" GUARD (OR A\nWALKABLE GRATE)", ha="left")
    tag(ax, U(1.0), zf, "WELL " + el(zf), fpi, fs=5.0)
    tag(ax, U(8.5), SLAB, "BSMT " + el(SLAB), fpi, fs=5.0, side="left")
    cv.dim((U(-1.0), zf), (U(-1.0), GRADE), 0.0, "", size=5)
    detail_title(bg, x, y - 0.25, 4, "LIGHT WELL (LIVING ROOM)", SCALE_TXT[S38], "A5.1")


def det_stair(fig, bg, x, y):
    """Main stair along x = 45 looking east (north at left: u = -y)."""
    fpi = S14
    ax = detail_axes(fig, x, y, 6.6, 4.4, -51.0, -15.2, fpi)
    cv = Mpl(ax, fpi)
    U = lambda yy: -yy                                                    # noqa: E731
    n, rise, run = STAIR["risers"], STAIR["rise"], STAIR["run"]
    top, foot = STAIR["top_y"], STAIR["foot_y"]
    pts = [(U(foot), SLAB)]
    for i in range(n - 1):
        yy = foot + i * run
        pts += [(U(yy), SLAB + (i + 1) * rise), (U(yy + run), SLAB + (i + 1) * rise)]
    pts += [(U(top), 0.0), (U(top + 0.6), 0.0), (U(top + 0.6), -1.0), (U(foot + 1.2), SLAB)]
    matp(ax, pts, "wood", lw=0.5, z=3)
    mat(ax, U(50.69), SILL, U(top), 0.0, "wood", lw=0.4, z=3)
    mat(ax, U(35.46 + 0.2), SILL, U(26.0), 0.0, "wood", lw=0.4, z=3)
    mat(ax, U(50.69), SLAB - SLAB_T, U(26.0), SLAB, "concrete", z=3)
    edge = (U(35.66), SILL)
    ax.plot([U(foot), U(top)], [SLAB + rise, 0.0 + 0.0], color=GREY, lw=0.4, ls="--")
    zn = SLAB + (35.66 - foot) / run * rise + rise
    ax.plot([edge[0], edge[0]], [zn, SILL], color=RED, lw=0.8)
    note(ax, (edge[0], (zn + SILL) / 2), (U(30.0), -6.0), "HEADROOM 1 993 mm MIN.\n(NBC: 1 950 mm)", ha="left")
    note(ax, (U(40.0), SLAB + 13 * rise), (U(47.0), -5.0), f"{n} RISERS x 7 1/2\" = {ftin(F2F)}\n{n - 1} TREADS x "
         "10 1/2\"\n4'-2 1/2\" CLEAR WIDTH", ha="left")
    note(ax, (U(42.0), -1.0), (U(49.5), -2.0), "FLOOR OPENING\n" + ftin(top - 35.46), ha="left")
    note(ax, (U(33.0), -0.8), (U(29.0), 1.2), "MAIN HALL FLOOR ABOVE THE LOWER FLIGHT", ha="left")
    tag(ax, U(48.5), 0.0, "MAIN " + el(0), fpi, fs=5.0)
    tag(ax, U(27.0), SLAB, "BSMT " + el(SLAB), fpi, fs=5.0, side="left")
    detail_title(bg, x, y - 0.25, 5, "MAIN STAIR (SECTION B)", SCALE_TXT[S14], "A5.1")


def sheet_details_other(pdf):
    fig, bg = new_sheet("A5.1", "AS NOTED")
    det_pool(fig, bg, DRAW[0] + 0.1, 15.7)
    det_theater(fig, bg, DRAW[0] + 14.65, 15.7)
    det_exit(fig, bg, DRAW[0] + 0.2, 7.9)
    det_stair(fig, bg, DRAW[0] + 8.6, 8.5)
    det_well(fig, bg, DRAW[0] + 16.2, 7.5)
    notes_column(bg, DRAW[0] + 24.0, 22.4, "POOL AND SPA - FOR THE ENGINEER", [
        "Shell: wet-mix shotcrete (ACI 506.2), 35 MPa at 28 days, w/cm 0.40, crystalline waterproofing "
        "admixture; one continuous placement for the pool, the spa and the shared wall.",
        "Design the shell for the water inside and the soil and groundwater outside, empty and full; "
        "uplift when empty (hydrostatic relief valve, drain loop).",
        "Footings round the pool room are deepened below the pit, or the shell retains them.",
        "Two main drains per pool and spa (anti-entrapment), bonding grid, GFCI: electrical permit (CEC "
        "Section 68).",
        "A dedicated pool dehumidifier; the room's envelope and the trusses above protected from the "
        "pool air.",
        "**THEATER",
        "Depressed slab poured with the basement floor (Phase 1); the seating, room-within-a-room "
        "walls and the screen are Phase 2.",
    ], 6.2, fs=7.0)
    pdf.savefig(fig)
    plt.close(fig)


# ============================================================ schedules

def door_rows():
    rows = []
    for lv, lvl in ((MAIN, "MAIN"), (BASE, "BSMT")):
        for i, d in sorted(lv.door_mark.items(), key=lambda kv: kv[1]):
            o = lv.doors[i]
            kind = o[4]
            a, b = lv.side_names(o)
            ext = lv.is_exterior(o)
            h = {"door": DOOR_H, "garage": GARAGE_DOOR_H}.get(kind, OPEN_H)
            if lvl == "BSMT" and kind == "door" and ext:
                h = DOOR_H
            typ = {"door": "SWING", "double": "DOUBLE SWING", "open": "CASED OPENING", "slider": "SLIDING (GLAZED)",
                   "glass": "SIDELIGHT (GLAZED)", "garage": "OVERHEAD"}[kind]
            notes = []
            names = {a, b}
            if "GARAGE" in names and not ext:
                notes.append("TO GARAGE: SELF-CLOSING, WEATHERSTRIPPED (9.10.13.15)")
            elif ext and kind != "garage":
                notes.append("EXTERIOR: INSULATED, WEATHERSTRIPPED" + (", SAFETY GLAZING" if kind in ("slider", "glass") else ""))
            if kind == "garage":
                notes.append("HEADER BY ENGINEER")
            if any("THEATER" in n for n in names):
                notes.append("SOLID CORE, SEALS")
            if lvl == "BSMT" and ext:
                notes.append("TO THE EXIT STAIR, OPENS IN")
            sw = ""
            if kind in ("door", "double"):
                sw = {("x", 1): "N", ("x", -1): "S", ("y", 1): "E", ("y", -1): "W"}[(o[2], o[5] if len(o) > 5 else 1)]
            rows.append([d, lvl, f"{a} / {b}", typ, ftin(o[3]), ftin(h), sw, "; ".join(notes)])
    return rows


def window_rows():
    rows = []
    for lv, lvl in ((MAIN, "MAIN"), (BASE, "BSMT")):
        for i, m in sorted(lv.window_mark.items(), key=lambda kv: kv[1]):
            w = lv.windows[i]
            names = [n for n in lv.side_names(w) if n != "OUTSIDE"]
            room = names[0] if names else ""
            rid = [k for k in lv.sides(w) if k is not None]
            notes = []
            if rid and lv.rooms[rid[0]][6] == "bed":
                notes.append("BEDROOM: EGRESS 0.35 m2 MIN., NO SIDE < 380 mm (9.9.10.1)")
            if lvl == "BSMT":
                notes.append("IN A LIGHT WELL (A5.1)")
            if rid and lv.rooms[rid[0]][6] == "bath":
                notes.append("PRIVACY / SAFETY GLAZING NEAR TUB OR SHOWER")
            area = m2(w[3] * w[5])
            rows.append([m, lvl, room, ftin(w[3]), ftin(w[5]), ftin(w[4]), ftin(w[4] + w[5]), f"{area:.2f}",
                         "; ".join(notes)])
    return rows


def room_rows():
    rows = []
    for lv, lvl in ((MAIN, "MAIN"), (BASE, "BSMT")):
        for i, no in sorted(lv.room_no.items(), key=lambda kv: kv[1]):
            r = lv.rooms[i]
            if r[6] in ("stairwell",):
                continue
            wd, dp = r[3] - r[1], r[4] - r[2]
            clg = ftin(r[5]) if r[5] else "-"
            phase = "2 (FINISH)" if lvl == "BSMT" and r[6] not in ("stair",) else "1"
            rows.append([no, lvl, label_of(r), f"{ftin(wd)} x {ftin(dp)}", f"{wd * dp:.0f}", f"{m2(wd * dp):.1f}",
                         clg, phase])
    return rows


def table(bg, x, y, title, header, rows, widths, fs=5.6, rh=0.142):
    bg.text(x, y + 0.06, title, fontsize=9, weight="bold", va="bottom")
    total = sum(widths)
    top = y
    bg.add_patch(Rectangle((x, y - rh * 1.3), total, rh * 1.3, fc="#e3e3e3", ec="none"))
    cx = x
    for h_, w in zip(header, widths):
        bg.text(cx + 0.04, y - rh * 0.65, h_, fontsize=fs, weight="bold", va="center")
        cx += w
    y -= rh * 1.3
    for k, r in enumerate(rows):
        if k % 2:
            bg.add_patch(Rectangle((x, y - rh), total, rh, fc="#f4f4f4", ec="none"))
        cx = x
        for v, w in zip(r, widths):
            bg.text(cx + 0.04, y - rh / 2, str(v), fontsize=fs, va="center")
            cx += w
        y -= rh
    bg.add_patch(Rectangle((x, y), total, top - y, fill=False, ec=INK, lw=0.6))
    cx = x
    for w in widths[:-1]:
        cx += w
        bg.plot([cx, cx], [y, top], color=INK, lw=0.25)
    return y


def sheet_schedules(pdf, drows, wrows, rrows):
    fig, bg = new_sheet("A6.0", "NONE")
    half = (len(drows) + 1) // 2
    hdr = ["MARK", "LVL", "BETWEEN", "TYPE", "WIDTH", "HEIGHT", "SW.", "NOTES"]
    wid = [0.48, 0.38, 2.75, 1.05, 0.55, 0.5, 0.3, 3.35]
    table(bg, DRAW[0] + 0.2, 22.9, "DOOR SCHEDULE (1 of 2)", hdr, drows[:half], wid)
    table(bg, DRAW[0] + 0.2, 22.9 - (half + 3) * 0.142 - 0.5, "DOOR SCHEDULE (2 of 2)", hdr, drows[half:], wid)
    wh = ["MARK", "LVL", "ROOM", "WIDTH", "HEIGHT", "SILL", "HEAD", "m2", "NOTES"]
    ww = [0.48, 0.38, 1.4, 0.55, 0.55, 0.55, 0.55, 0.42, 4.2]
    yb = table(bg, DRAW[0] + 10.0 + 0.4, 22.9, "WINDOW SCHEDULE", wh, wrows, ww)
    rh = ["NO.", "LVL", "ROOM", "SIZE (C/L)", "ft2", "m2", "CEILING", "PHASE"]
    rw = [0.42, 0.38, 1.7, 1.65, 0.45, 0.45, 0.6, 0.85]
    third = (len(rrows) + 1) // 2
    table(bg, DRAW[0] + 10.4, yb - 0.6, "ROOM SCHEDULE (1 of 2)", rh, rrows[:third], rw)
    table(bg, DRAW[0] + 17.3, yb - 0.6, "ROOM SCHEDULE (2 of 2)", rh, rrows[third:], rw)
    notes_column(bg, DRAW[0] + 10.4, 5.2, "SCHEDULE NOTES", [
        "Marks: D/W + 1xx main floor, Bxx basement, numbered in reading order (north to south, west to east).",
        "Sizes are the model's opening widths (wall centre-line plan); rough openings, frames and hardware are "
        "for the supplier. Swing: the direction the leaf opens toward.",
        "Window U-values per NBC 9.36 for the climate zone (zone 7A/7B: U <= 1.61 W/m2K prescriptive; "
        "triple glazing recommended). Safety glazing where NBC 9.6.1.4 requires it (doors, sidelights, "
        "near tubs and the pool).",
        "Room sizes between wall centre lines; areas are gross. Basement rooms are finished in Phase 2.",
    ], 11.7, fs=6.3)
    pdf.savefig(fig)
    plt.close(fig)


# ============================================================ cover and brief

def text_block(bg, x, y, lines, fs=7.2, lh=None):
    lh = lh or fs / 72 * 1.45
    for ln in lines:
        bold = ln.startswith("**")
        bg.text(x, y, ln.strip("*"), fontsize=fs, va="top", weight="bold" if bold else "normal")
        y -= lh * (1.3 if bold else 1.0)
    return y


def sheet_cover(pdf):
    fig, bg = new_sheet("A0.0")
    X0 = DRAW[0] + 0.3
    bg.text(X0, 23.05, PROJECT, fontsize=30, weight="bold", va="top")
    bg.text(X0, 22.15, "Drawings for engineering review and building permit preparation - Alberta",
            fontsize=15, va="top")
    img = plt.imread(ROOT / "docs" / "house" / "house_front.png")[:, :, :3]
    ih, iw = img.shape[:2]
    w = 11.6
    h = w * ih / iw
    ix = DRAW[0] + DRAW[2] - w
    ax = fig.add_axes([ix / SHEET_W, (23.2 - h) / SHEET_H, w / SHEET_W, h / SHEET_H])
    ax.imshow(img)
    ax.axis("off")
    back = plt.imread(ROOT / "docs" / "house" / "house_back.png")[:, :, :3]
    bh = w * back.shape[0] / back.shape[1]
    ax = fig.add_axes([ix / SHEET_W, 0.9 / SHEET_H, w / SHEET_W, bh / SHEET_H])
    ax.imshow(back)
    ax.axis("off")
    fs = 9.6
    # ---- column 1: project data, building area, code basis
    A = AREAS
    y = 20.9
    bg.text(X0, y, "PROJECT DATA", fontsize=11.5, weight="bold", va="top")
    bg.plot([X0, X0 + 9.0], [y - 0.24, y - 0.24], color=INK, lw=0.6)
    y -= 0.38
    for t, v in (("Main floor, heated (to wall centre lines)", A["main_heated"]), ("Attached garage", A["garage"]),
                 ("Porches and deck (open)", A["porches"]), ("Basement, inside the ICF walls", A["basement"])):
        bg.text(X0, y, t, fontsize=fs, va="top")
        bg.text(X0 + 6.7, y, f"{v:,.0f} ft2", fontsize=fs, va="top", ha="right")
        bg.text(X0 + 8.6, y, f"{m2(v):,.1f} m2", fontsize=fs, va="top", ha="right")
        y -= 0.2
    y -= 0.25
    over = m2(A["footprint_out"]) > PART9_LIMIT_M2
    lines = [
        "**BUILDING AREA - THE FIRST DECISION",
        f"Building area (NBC: the greatest area above grade, to the outside face of the walls) of the house "
        f"with its attached garage: about {m2(A['footprint_cl']):,.0f} m2 at the wall centre lines and "
        f"{m2(A['footprint_out']):,.0f} m2 to the outside face.",
        "NBC(AE) 2023 Part 9 covers houses of up to 600 m2 building area (Div. A 1.3.3.3)."
        + (" This design is over the limit, so Part 3 would apply as drawn." if over else ""),
        f"Without the garage the house is about {m2(A['house_only_out']):,.0f} m2. Options: detach the garage "
        "(a breezeway); separate it with a firewall; trim about 35 m2 (375 ft2) of enclosed area; or design the "
        "house to Part 3 with a professional. Confirm with the permit office and decide before the engineer "
        "starts: it changes the code path for the whole design.",
    ]
    wrapped = []
    for ln in lines:
        if ln.startswith("**"):
            wrapped.append(ln)
        else:
            wrapped += wrap(ln, chars_for(8.7, fs)) + [""]
    hgt = 0.2 * len(wrapped) + 0.25
    bg.add_patch(Rectangle((X0 - 0.12, y - hgt + 0.12), 9.25, hgt, fc="#fdecea" if over else "#eef6ee",
                           ec=RED if over else GREEN, lw=1.4))
    yy = y - 0.02
    for ln in wrapped:
        bold = ln.startswith("**")
        bg.text(X0, yy, ln.strip("*"), fontsize=fs + (1 if bold else 0), va="top", weight="bold" if bold else "normal",
                color=RED if bold else INK)
        yy -= 0.2
    y = y - hgt - 0.25
    y = notes_column(bg, X0, y, "CODE BASIS", [
        "National Building Code - 2023 Alberta Edition, in force May 1, 2024: Part 9 if the building area "
        "is 600 m2 or less (above).",
        "Energy efficiency: NBC Section 9.36, Tier 1 minimum. The performance path (an energy advisor's "
        "HOT2000 model) suits this house best.",
        "Electrical: Canadian Electrical Code with Alberta modifications. Gas: CSA B149.1. Plumbing: "
        "National Plumbing Code. Private sewage: Alberta Private Sewage Systems Standard of Practice 2021.",
        "Builder: a licensed residential builder, or an Owner Builder Authorization from the Alberta "
        "registrar, before the building permit is issued (New Home Buyer Protection Act).",
    ], 9.0, fs=fs)
    y = notes_column(bg, X0, y - 0.1, "OCCUPANCY", [
        "Group C, one dwelling unit: one storey above grade with a full basement and an attached garage.",
        "Smoke and CO alarms, the garage separation and the foam thermal barrier: A1.1, A1.2, A5.0.",
    ], 9.0, fs=fs)
    y = notes_column(bg, X0, y - 0.1, "ABBREVIATIONS", [
        "C/L centre line;  EL. elevation (main floor = 0'-0\");  T/O top of;  U/S underside of;  FTG footing;  "
        "ICF insulated concrete form;  P.T. pressure-treated;  E.W. each way;  O.C. on centre;  U.N.O. unless "
        "noted otherwise;  AHJ authority having jurisdiction;  PSDS private sewage disposal system;  HRV heat "
        "recovery ventilator;  NBC(AE) National Building Code - 2023 Alberta Edition.",
    ], 9.0, fs=fs)
    yy = y - 0.15
    bg.text(X0, yy, "SYMBOLS", fontsize=8.5, weight="bold", va="top")
    bg.plot([X0, X0 + 9.0], [yy - 0.19, yy - 0.19], color=INK, lw=0.5)
    yy -= 0.55
    for k, (mark, color, txt) in enumerate((("D101", RED, "door mark (A6.0)"), ("W101", BLUE, "window mark (A6.0)"))):
        bx = X0 + k * 4.5
        bg.text(bx + 0.3, yy, mark, fontsize=7, color=color, ha="center", va="center",
                bbox=dict(fc="white", ec=color, lw=0.6, boxstyle="round,pad=0.2"))
        bg.text(bx + 0.8, yy, txt, fontsize=fs, va="center")
    yy -= 0.5
    bg.add_patch(Circle((X0 + 0.3, yy), 0.2, fc="white", ec=INK, lw=0.8))
    bg.plot([X0 + 0.1, X0 + 0.5], [yy, yy], color=INK, lw=0.5)
    bg.text(X0 + 0.3, yy + 0.02, "A", fontsize=7, weight="bold", ha="center", va="bottom")
    bg.text(X0 + 0.3, yy - 0.03, "A4.0", fontsize=4.5, ha="center", va="top")
    bg.text(X0 + 0.8, yy, "section: letter / sheet", fontsize=fs, va="center")
    bg.add_patch(MPoly([(X0 + 4.6, yy + 0.1), (X0 + 4.8, yy + 0.1), (X0 + 4.7, yy - 0.06)], closed=True, fc=RED,
                       ec=RED))
    bg.text(X0 + 5.3, yy, "elevation tag", fontsize=fs, va="center")
    # ---- column 2: phasing
    X1 = DRAW[0] + 10.0
    y = notes_column(bg, X1, 20.9, "PHASING", [
        "**Phase 1 - the house, and all of the basement concrete",
        "Footings, ICF walls and the basement slab.",
        "The pool and spa shells, with their piping, drains and the hydrostatic relief valve.",
        "The theater's depressed (stepped) floor.",
        "The exit stair areaway and stair, the light wells and their guards.",
        "Frost walls, the garage slab and the porch piers.",
        "Under-slab plumbing for every future basement fixture, floor drains, the sump and the radon pipe.",
        "The main stair, the basement bearing walls, beams and posts (S1.1), and the mechanical room "
        "(furnace or boiler, HRV, water heater, water treatment, panel).",
        "The main floor, roof and envelope, finished for occupancy.",
        "A thermal barrier (1/2\" gypsum) over all the ICF foam inside, smoke and CO alarms, and "
        "the basement lighting and outlets the code needs.",
        "**Phase 2 - finishing the basement, after the house is occupied",
        "Partitions, drywall, ceilings and floors; the bathrooms and laundry; the theater (room within a room, "
        "seating, screen) and the music room; the pool room finishes.",
        "Phase 2 takes its own building permit, plus electrical and plumbing permits.",
        "**Why the split works",
        "Everything structural, everything under the slab and everything in the concrete is in Phase 1, "
        "so Phase 2 is interior work only - no cutting of the slab, no new footings.",
    ], 8.1, fs=fs)
    notes_column(bg, X1, y - 0.15, "ALBERTA ROADMAP (details: README.md)", [
        "1. Land: title, land-use district and setbacks; a development permit from the municipality.",
        "2. Survey (plot plan) and a geotechnical investigation on the real site.",
        "3. Builder: a licensed builder, or an Owner Builder Authorization, plus warranty or its exemption.",
        "4. Design: this set reviewed and engineered (APEGA), truss layouts, the 9.36 energy compliance.",
        "5. Building permit (municipality or its accredited agency); electrical, gas and plumbing permits; "
        "PSDS permit by a certified installer; water well by a licensed driller; road approach.",
        "6. Utility locates before digging; inspections at the footings, foundation, framing, insulation "
        "and final; occupancy.",
        "7. Phase 2: a separate permit set for the basement finish.",
    ], 8.1, fs=fs)
    # ---- column 3: index and flags, under the picture
    X2 = ix
    y = 23.2 - h - 0.35
    bg.text(X2, y, "DRAWING INDEX", fontsize=11.5, weight="bold", va="top")
    bg.plot([X2, X2 + w], [y - 0.24, y - 0.24], color=INK, lw=0.6)
    for k, (n, t) in enumerate(INDEX):
        bg.text(X2, y - 0.4 - k * 0.215, n, fontsize=fs, va="top", weight="bold")
        bg.text(X2 + 0.75, y - 0.4 - k * 0.215, t, fontsize=fs, va="top")
    y = y - 0.4 - len(INDEX) * 0.215 - 0.25
    y = notes_column(bg, X2, y, "ALSO IN THE PACKAGE (docs/permit/)", [
        "README.md - the engineering brief and the Alberta permit roadmap and checklist, with sources.",
        "cad/ - the plans as DXF files (inches, layered).  schedules/ - door, window and room schedules (CSV).",
    ], w, fs=fs)
    notes_column(bg, X2, y - 0.05, "FLAGS TO RESOLVE BEFORE THE PERMIT", [
        "Building area over the Part 9 limit (left).",
        "Geotechnical report: bearing, groundwater, sulphates - the pool pit is 18'-3\" below grade.",
        "Porch floors 2'-0\" above grade: guards, or finished grade raised within 600 mm.",
        "Fireplace type (gas or wood) in the great room - it decides the code path for it.",
        "A surveyed plot plan on the real parcel (A0.1).",
    ], w, fs=fs)
    pdf.savefig(fig)
    plt.close(fig)


def sheet_brief(pdf):
    fig, bg = new_sheet("S0.1", "NONE")
    W = 7.0
    fs = 9.6
    cols = [DRAW[0] + 0.2, DRAW[0] + 7.75, DRAW[0] + 15.3, DRAW[0] + 22.85]
    # design criteria as a fill-in table
    x, y = cols[0], 22.7
    bg.text(x, y, "1. DESIGN CRITERIA (TO BE COMPLETED)", fontsize=10.5, weight="bold", va="top")
    bg.plot([x, x + W], [y - 0.24, y - 0.24], color=INK, lw=0.6)
    bg.text(x, y - 0.38, "From NBC(AE) 2023 Div. B Appendix C for the site, and the geotechnical report",
            fontsize=fs - 0.6, va="top", style="italic")
    rows = ["Location / nearest listed place", "Climate zone (7A / 7B) and heating degree-days",
            "Ground snow load Ss  /  rain load Sr (kPa)", "Hourly wind pressure q 1/50 (kPa)",
            "Seismic Sa(0.2)  /  site class", "Frost penetration (min. footing depth 1.2 m)",
            "Bearing capacity at the footings (kPa) and level", "Groundwater level (pool pit 18'-3\" down)",
            "Sulphate exposure class", "Lateral earth pressure of the backfill (kPa/m)"]
    yy = y - 0.75
    for r in rows:
        bg.text(x, yy, r, fontsize=fs, va="bottom")
        bg.plot([x + 4.3, x + W], [yy, yy], color=GREY, lw=0.5)
        yy -= 0.42
    notes_column(bg, x, yy - 0.15, "LOADS (NBC PART 4 / 9 - CONFIRM)", [
        "Floors 1.9 kPa (40 psf) live; garage slab 2.4 kPa.",
        "Pool: 4'-6\" of water (about 13.4 kPa) plus the shell; spa 3'-6\" of water, raised 18\".",
        "Roof: snow from Ss and Sr, with drifting at the lower porch roofs.",
        "Partitions, finishes, mechanical units, the pool dehumidifier.",
        "Radon protection per NBC 9.13.4 regardless of the site.",
    ], W, fs=fs)
    elems = [
        "E1  ICF basement walls, 13'-0\" tall, 11'-9\" backfill: reinforcement, lintels, the exit door and window "
        "bucks; check against the ICF maker's engineered tables (S1.0, A5.0).",
        "E2  Wall-top support: the main floor diaphragm and the sill connection take the soil load at the top "
        "of the ICF walls - including at the stair opening and the long pool-room wall.",
        "E3  Footings: perimeter 24\" x 10\", interior bearing lines 20\", steps; bearing per the geotech.",
        "E4  Pool and spa shells; the deepened footings round the pool room or the shell retaining them; "
        "buoyancy when empty (A5.1).",
        "E5  Theater depressed slab and its thickened edges (A5.1).",
        "E6  Exit stair areaway and light wells: 8\" retaining walls, 11'-9\" and 8'-0\" of soil (A5.1).",
        "E7  Main floor framing: truss layout and spans (S1.1), the new bearing wall at x = 42.65 and the "
        "crawlspace beam at x = 103.04, the stair opening, posts and their footings.",
        "E8  Roof: hip trusses by the supplier; girder reactions traced down; uplift and lateral design.",
        "E9  Lateral: braced wall panels / shear walls for wind (and seismic) on the main floor (NBC 9.23.13).",
        "E10 Garage: door headers 16'-0\" and 9'-0\", the slab, frost walls.",
        "E11 Porches and deck: piers, beams, guards and their anchorage.",
    ]
    notes_column(bg, cols[1], 22.7, "2. ELEMENTS FOR ENGINEERED DESIGN", elems, W, fs=fs)
    qs = [
        "Q1  Is 8\" ICF core enough for 13'-0\" walls with 11'-9\" of backfill, or 10\"? Bar size and spacing?",
        "Q2  Deepen the pool-room footings, or design the pool shell to retain them?",
        "Q3  Does the groundwater level allow a pit 18'-3\" below grade? Dewatering, drain loop, relief valve.",
        "Q4  Strip footings vs thickened slab at the interior bearing lines?",
        "Q5  Floor trusses at 18\" for the 26'-11\" pool-room span - spacing, vibration, moisture?",
        "Q6  How is the ICF wall top braced at the stair opening and the exit door?",
        "Q7  Can the exit-stair and light-well walls cantilever, or do they need ties to the house?",
        "Q8  Sulphate class and concrete mixes for the footings, walls and shells?",
        "Q9  Frost walls vs frost-protected shallow foundations for the crawlspace and garage?",
        "Q10 Field reviews: which pours need an engineer's inspection (letters of assurance)?",
        "Q11 Building area over 600 m2 (cover sheet): which path does the engineer recommend?",
    ]
    notes_column(bg, cols[2], 22.7, "3. QUESTIONS FOR THE ENGINEER", qs, W, fs=fs)
    mats = [
        "**Concrete (CSA A23.1, verify)",
        "Footings + ICF walls: S-class per geotech, else N",
        "Basement slab: N, 25-32 MPa, w/cm <= 0.55, wet cure 7 days",
        "Garage slab: C-2, 32 MPa, w/cm 0.45, air-entrained",
        "Pool + spa: 35 MPa, w/cm 0.40, crystalline admixture",
        "Frost walls, piers: as footings; air-entrained if exposed",
        "**ICF",
        "8\" core, 2 5/8\" EPS faces (13 1/4\"); brand TBD",
        "**Reinforcement",
        "CSA G30.18 400W; sizes by the engineer",
        "**Wood",
        "Floor trusses 18\" (approx.), roof trusses: by supplier",
        "Sill plates pressure-treated on a gasket",
        "**Phase 1 embeds and sleeves",
        "Plumbing under the slab, sump, radon pipe, pool and spa",
        "piping and drains, conduits, a spare sleeve in the",
        "UTILITY room's west wall for the future shop lines,",
        "window and door bucks",
    ]
    notes_column(bg, cols[3], 22.7, "4. MATERIALS ASSUMED", mats, 6.4, fs=fs)
    # key plan: where each element is
    ax = sheet_axes(fig, (7.8, 3.95, 17.6, 11.0), (69.0, 25.5), S18)
    cv = Mpl(ax, S18)
    plan_foundation(cv, notes=False)
    tags = {"E1": (22.16, 50.0), "E2": (82.0, 52.76), "E3": (54.14, 12.0), "E4": (82.5, 40.0),
            "E5": (61.7, 42.0), "E6": (57.0, 65.75), "E7": (42.65, 57.0), "E8": (118.0, 58.0),
            "E9": (116.0, 20.0), "E10": (12.0, 18.0), "E11": (75.0, -8.0)}
    for t, (tx, ty) in tags.items():
        ax.add_patch(Circle((tx, ty), 2.6, fc="white", ec=RED, lw=1.0, zorder=20))
        ax.text(tx, ty, t, fontsize=7.5, weight="bold", color=RED, ha="center", va="center", zorder=21)
    w0 = M["base_windows"][0][6]
    ax.add_patch(Circle(((w0[0] + w0[2]) / 2, 2.7), 2.6, fc="white", ec=RED, lw=1.0, zorder=20))
    ax.text((w0[0] + w0[2]) / 2, 2.7, "E6", fontsize=7.5, weight="bold", color=RED, ha="center", va="center",
            zorder=21)
    view_title(bg, 7.8, 3.7, 1, "KEY PLAN - WHERE EACH ELEMENT IS (FOUNDATION, S1.0)", SCALE_TXT[S18], "S0.1")
    bg.add_patch(Rectangle((cols[0], 0.8), 29.6, 2.2, fc="#fff7e0", ec="#c9a227", lw=0.8))
    text_block(bg, cols[0] + 0.15, 2.85, [
        "**HOW TO USE THIS SET",
        "This set describes the design the owners want; it is not engineered. The engineer of record "
        "(APEGA) designs the structure and returns stamped drawings or a design letter for the items above, "
        "with the truss supplier's layouts.",
        "The permit set is then completed with the engineer's drawings, the truss layouts, the energy (9.36) "
        "compliance report, the surveyed plot plan and the permits listed in docs/permit/README.md.",
        "Mark up the PDF or the DXF files freely; the model (models/*.scad) is the source and every sheet is "
        "regenerated from it with tools/make_drawings.py.",
    ], fs=9.0)
    pdf.savefig(fig)
    plt.close(fig)


# ============================================================ DXF + CSV

def write_dxf():
    out = OUT / "cad"
    out.mkdir(parents=True, exist_ok=True)
    for name, draw, geom, limit in (("main-floor", plan_main, ENCLOSED, MAIN_LIMIT),
                                    ("basement", lambda cv: plan_base(cv), BOUT, BASE_LIMIT),
                                    ("foundation", plan_foundation, BOUT, BASE_LIMIT)):
        cv = Dxf(S316)
        draw(cv)
        chains(cv, geom, limit)
        cv.save(out / f"{name}.dxf")


def write_csv(drows, wrows, rrows):
    out = OUT / "schedules"
    out.mkdir(parents=True, exist_ok=True)
    for name, hdr, rows in (
            ("doors", ["mark", "level", "between", "type", "width", "height", "swing", "notes"], drows),
            ("windows", ["mark", "level", "room", "width", "height", "sill", "head", "area_m2", "notes"], wrows),
            ("rooms", ["no", "level", "room", "size", "area_ft2", "area_m2", "ceiling", "phase"], rrows)):
        with open(out / f"{name}.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(hdr)
            w.writerows(rows)


# ============================================================ main

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("rendering views (cached in build/renders/) ...", file=sys.stderr)
    paths = render_all(list(VIEWS))
    missing = [n for n, p in paths.items() if not p.exists()]
    if missing:
        sys.exit(f"renders missing: {missing}")
    drows, wrows, rrows = door_rows(), window_rows(), room_rows()
    pdf_path = OUT / "House-Drawing-Set.pdf"
    with PdfPages(pdf_path, metadata={"Title": f"{PROJECT} - drawing set for engineering review",
                                      "Subject": "NOT FOR CONSTRUCTION"}) as pdf:
        sheet_cover(pdf)
        sheet_site(pdf, paths)
        sheet_brief(pdf)
        sheet_foundation(pdf)
        sheet_framing(pdf)
        sheet_basement(pdf)
        sheet_main_floor(pdf)
        sheet_roof(pdf, paths)
        sheet_elevations(pdf, paths)
        sheet_sections_ab(pdf, paths)
        sheet_sections_cde(pdf, paths)
        sheet_details_foundation(pdf)
        sheet_details_other(pdf)
        sheet_schedules(pdf, drows, wrows, rrows)
    write_dxf()
    write_csv(drows, wrows, rrows)
    A = AREAS
    print(f"wrote {pdf_path.relative_to(ROOT)} ({len(SHEETS)} sheets), cad/*.dxf, schedules/*.csv")
    print(f"building area: {m2(A['footprint_cl']):.0f} m2 at centre lines, {m2(A['footprint_out']):.0f} m2 to the "
          f"outside face (Part 9 limit {PART9_LIMIT_M2:.0f} m2); house alone {m2(A['house_only_out']):.0f} m2")


if __name__ == "__main__":
    main()
