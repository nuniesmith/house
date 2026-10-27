#!/usr/bin/env python3
"""
generate_scad.py — generate OpenSCAD 3D models from config/floorplan.yaml.

Reads the same YAML the 2D floor-plan generator uses and emits one .scad
file per level (main floor + basement): floor plates in the plan's
colours, walls extruded to ceiling height, door/window openings cut,
stairs, fireplace, pool, hot tub and theater seating as simple solids.

Units are FEET (1 OpenSCAD unit = 1 ft), matching the YAML. To print the
model, scale in your slicer (e.g. 1:87) or set model_scale below.

Assumptions (the YAML does not carry these):
  - main-floor ceiling 9 ft (basement is 12 ft, from the YAML note)
  - door leaf height 7 ft, window sill 2.5 ft, window height 4 ft
  - exterior walls 0.5 ft, interior 0.34 ft (rooms are drawn with a wall
    frame on each room edge, so shared walls appear doubled — this is a
    visualisation model, not construction documents)

Usage:  python3 src/generate_scad.py [floorplan.yaml] [out_dir]
Defaults resolve relative to the repo root (config/floorplan.yaml -> output/).
"""

import sys
import yaml

MAIN_CEILING_FT = 9.0
BASEMENT_CEILING_FT = 12.0  # "12' Ceilings Throughout" in the YAML
DOOR_H = 7.0
WIN_SILL = 2.5
WIN_H = 4.0
EXT_T = 0.5
INT_T = 0.34


def hex_rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def label_of(room):
    return (room.get("label") or "").replace("\n", " ").strip()


class Level:
    def __init__(self, cfg, colors, ceiling, name):
        self.cfg = cfg
        self.colors = colors
        self.ceiling = ceiling
        self.name = name
        self.rooms = cfg.get("rooms", [])
        self.bounds = self._bounds()

    def _bounds(self):
        xs = [r["x"] for r in self.rooms] + [r["x"] + r["width"] for r in self.rooms]
        ys = [r["y"] for r in self.rooms] + [r["y"] + r["height"] for r in self.rooms]
        return min(xs), min(ys), max(xs), max(ys)

    def is_exterior(self, room, side):
        """A room edge is exterior if no other room shares it."""
        x, y, w, h = room["x"], room["y"], room["width"], room["height"]
        for o in self.rooms:
            if o is room:
                continue
            ox, oy, ow, oh = o["x"], o["y"], o["width"], o["height"]
            overlap_x = min(x + w, ox + ow) - max(x, ox) > 0.01
            overlap_y = min(y + h, oy + oh) - max(y, oy) > 0.01
            if side == "S" and abs(oy + oh - y) < 0.01 and overlap_x:
                return False
            if side == "N" and abs(oy - (y + h)) < 0.01 and overlap_x:
                return False
            if side == "W" and abs(ox + ow - x) < 0.01 and overlap_y:
                return False
            if side == "E" and abs(ox - (x + w)) < 0.01 and overlap_y:
                return False
        return True

    def wall_lines(self):
        """Yield (cx, cy, len, t, horizontal, height) per room edge wall.
        Porches get a 3 ft railing instead of a full-height wall."""
        out = []
        for r in self.rooms:
            x, y, w, h = r["x"], r["y"], r["width"], r["height"]
            wh = 3.0 if r.get("color") == "porch" else self.ceiling
            for side in "SNWE":
                ext = self.is_exterior(r, side)
                t = EXT_T if ext else INT_T
                if side == "S":
                    out.append((x + w / 2, y, w + t, t, True, wh))
                elif side == "N":
                    out.append((x + w / 2, y + h, w + t, t, True, wh))
                elif side == "W":
                    out.append((x, y + h / 2, h + t, t, False, wh))
                else:
                    out.append((x + w, y + h / 2, h + t, t, False, wh))
        return out

    def render(self):
        L = []
        A = L.append
        A(f"// {self.name} — generated from config/floorplan.yaml by generate_scad.py")
        A("// Units: feet. Dollhouse view (no roof). NOT construction documents.")
        A(f"wall_h = {self.ceiling};")
        A("$fn = 24;")
        A("")
        # ---- floor plates + labels
        A("// ---- floor plates")
        for r in self.rooms:
            col = hex_rgb(self.colors.get(r.get("color", "living"), "#eeeeee"))
            A(f"color({col}) translate([{r['x']}, {r['y']}, -0.15]) "
              f"cube([{r['width']}, {r['height']}, 0.15]);")
            lab = label_of(r)
            if lab:
                size = min(2.3, r["width"] / max(len(lab), 1) * 1.3, r["height"] / 2.2)
                if size > 0.7:
                    A(f"color([0.15,0.15,0.15]) translate([{r['x'] + r['width']/2}, "
                      f"{r['y'] + r['height']/2}, 0.01]) "
                      f"linear_extrude(0.05) text(\"{lab}\", size={size:.2f}, "
                      f"halign=\"center\", valign=\"center\");")
        A("")
        # ---- walls with openings cut
        A("// ---- walls (openings cut)")
        A("color([0.93, 0.91, 0.87]) difference() {")
        A("  union() {")
        for cx, cy, ln, t, horiz, wh in self.wall_lines():
            if horiz:
                A(f"    translate([{cx - ln/2:.2f}, {cy - t/2:.2f}, 0]) cube([{ln:.2f}, {t:.2f}, {wh}]);")
            else:
                A(f"    translate([{cx - t/2:.2f}, {cy - ln/2:.2f}, 0]) cube([{t:.2f}, {ln:.2f}, {wh}]);")
        A("  }")
        for d in self.cfg.get("doors", []):
            x, y, w = d["x"], d["y"], d["width"]
            if d["direction"] in ("up", "down"):  # opening in a horizontal wall
                A(f"  translate([{x}, {y - 0.8}, -0.1]) cube([{w}, 1.6, {DOOR_H + 0.1}]);")
            else:  # vertical wall
                A(f"  translate([{x - 0.8}, {y}, -0.1]) cube([1.6, {w}, {DOOR_H + 0.1}]);")
        for wn in self.cfg.get("windows", []):
            x, y, w = wn["x"], wn["y"], wn["width"]
            if wn["orientation"] == "horizontal":
                A(f"  translate([{x}, {y - 0.8}, {WIN_SILL}]) cube([{w}, 1.6, {WIN_H}]);")
            else:
                A(f"  translate([{x - 0.8}, {y}, {WIN_SILL}]) cube([1.6, {w}, {WIN_H}]);")
        A("}")
        A("")
        # ---- window panes
        panes = self.cfg.get("windows", [])
        if panes:
            A("// ---- window panes")
            A("color([0.53, 0.81, 0.92, 0.55]) {")
            for wn in panes:
                x, y, w = wn["x"], wn["y"], wn["width"]
                if wn["orientation"] == "horizontal":
                    A(f"  translate([{x}, {y - 0.06}, {WIN_SILL}]) cube([{w}, 0.12, {WIN_H}]);")
                else:
                    A(f"  translate([{x - 0.06}, {y}, {WIN_SILL}]) cube([0.12, {w}, {WIN_H}]);")
            A("}")
            A("")
        # ---- door leaves (ajar)
        doors = self.cfg.get("doors", [])
        if doors:
            A("// ---- door leaves (ajar 30 deg)")
            A("color([0.55, 0.35, 0.2]) {")
            for d in doors:
                x, y, w = d["x"], d["y"], d["width"]
                ang = {"up": 30, "down": -150, "right": 120, "left": 60}[d["direction"]]
                A(f"  translate([{x}, {y}, 0]) rotate([0,0,{ang}]) "
                  f"translate([0, -0.09, 0]) cube([{w}, 0.18, {DOOR_H}]);")
            A("}")
            A("")
        # ---- fireplaces
        for f in self.cfg.get("fireplaces", []):
            A(f"// fireplace: {f.get('label', '')}")
            A(f"color([0.3,0.3,0.3]) translate([{f['x']}, {f['y']}, 0]) "
              f"cube([{f['width']}, {f['height']}, {min(5.0, self.ceiling - 1)}]);")
            A(f"color([0.05,0.05,0.05]) translate([{f['x'] + 0.7}, {f['y'] - 0.05}, 0.6]) "
              f"cube([{f['width'] - 1.4}, 0.3, 1.8]);")
            A("")
        # ---- stairs
        for s in self.cfg.get("stairs", []):
            A(f"// stairs: {(s.get('label') or '').replace(chr(10), ' ')}")
            A("color([0.75, 0.72, 0.68]) {")
            n = s["num_steps"]
            if s["orientation"] == "vertical":
                run = s["height"] / n
                for i in range(n):
                    A(f"  translate([{s['x']}, {s['y'] + i * run:.2f}, 0]) "
                      f"cube([{s['width']}, {run:.2f}, {(i + 1) * self.ceiling / n:.2f}]);")
            else:
                run = s["width"] / n
                for i in range(n):
                    A(f"  translate([{s['x'] + i * run:.2f}, {s['y']}, 0]) "
                      f"cube([{run:.2f}, {s['height']}, {(i + 1) * self.ceiling / n:.2f}]);")
            A("}")
            A("")
        return "\n".join(L) + "\n"


def basement_extras(cfg, colors):
    """Pool, hot tub, theater seating + false wall, from the basement YAML."""
    L = []
    A = L.append
    pool = cfg.get("pool")
    if pool:
        p = pool["pool"]
        col = hex_rgb(colors.get(p.get("color", "pool"), "#63b3ed"))
        A("// ---- pool + hot tub")
        A(f"color({col}) translate([{p['x']}, {p['y']}, 0.02]) "
          f"cube([{p['width']}, {p['height']}, 0.35]);")
        ht = pool["hot_tub"]
        col = hex_rgb(colors.get(ht.get("color", "spa"), "#81e6d9"))
        A(f"color({col}) translate([{ht['x']}, {ht['y']}, 0.4]) "
          f"cylinder(r={ht['radius']}, h=1.6);")
        A("")
    th = cfg.get("theater")
    if th:
        st = th["seating"]
        col = hex_rgb(colors.get(st.get("chair_color", "chair"), "#4a4a4a"))
        A("// ---- theater seating")
        A(f"color({col}) {{")
        for row in range(st["rows"]):
            for seat in range(st["seats_per_row"]):
                x = st["start_x"] + seat * st["seat_spacing"]
                y = st["start_y"] + row * st["row_spacing"]
                z = 0.4 * (st["rows"] - row)  # raked floor, front row lowest
                A(f"  translate([{x}, {y}, {z:.2f}]) "
                  f"cube([{st['chair_width']}, {st['chair_height']}, 2.6]);")
        A("}")
        fw = th["false_wall"]
        A(f"color([0.6, 0.1, 0.1]) translate([{fw['x1']}, {fw['y1'] - 0.25}, 0]) "
          f"cube([{fw['x2'] - fw['x1']}, 0.5, {BASEMENT_CEILING_FT - 1}]);  // false wall")
        A("")
    return "\n".join(L)


def main():
    import os
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo_root, "config", "floorplan.yaml")
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(repo_root, "output")
    with open(src) as fh:
        doc = yaml.safe_load(fh)
    colors = {k: v for k, v in doc["colors"].items() if isinstance(v, str)}

    main_lvl = Level(doc["main_floor"], colors, MAIN_CEILING_FT, "Main floor")
    with open(f"{out_dir}/main_floor.scad", "w") as fh:
        fh.write(main_lvl.render())

    bs = Level(doc["basement"], colors, BASEMENT_CEILING_FT, "Basement")
    body = bs.render()
    # ICF foundation shell around the 100x60 footprint
    x0, y0, x1, y1 = bs.bounds
    shell = ["// ---- ICF foundation shell (1 ft)",
             "difference() {"]
    shell.append(f"  translate([{x0}, {y0}, -1.15]) cube([{x1 - x0}, {y1 - y0}, 1.0]);")
    shell.append("}")
    shell.append(f"color([0.45,0.45,0.45]) {{")
    shell.append(f"  translate([{x0 - 0.5}, {y0 - 0.5}, 0]) cube([{x1 - x0 + 1}, 1.0, {BASEMENT_CEILING_FT}]);")
    shell.append(f"  translate([{x0 - 0.5}, {y1 - 0.5}, 0]) cube([{x1 - x0 + 1}, 1.0, {BASEMENT_CEILING_FT}]);")
    shell.append(f"  translate([{x0 - 0.5}, {y0}, 0]) cube([1.0, {y1 - y0}, {BASEMENT_CEILING_FT}]);")
    shell.append(f"  translate([{x1 - 0.5}, {y0}, 0]) cube([1.0, {y1 - y0}, {BASEMENT_CEILING_FT}]);")
    shell.append("}")
    body += "\n".join(shell) + "\n" + basement_extras(doc["basement"], colors)
    with open(f"{out_dir}/basement.scad", "w") as fh:
        fh.write(body)
    print("wrote main_floor.scad and basement.scad")


if __name__ == "__main__":
    main()
