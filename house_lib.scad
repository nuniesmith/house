// house_lib.scad - shared drawing modules for the house models.
// Units: feet. x = east, y = north, z = up; the main floor is z = 0.
// Visualisation only - NOT construction documents.
//
// The level files (main_floor.scad, basement.scad) describe each floor
// as tables and call draw_level() below, so one table row drives a
// room's floor plate, label and walls, and one door row drives both
// the wall cut and the door leaf.
//
// room   = [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
//   (x0, y0)-(x1, y1) are wall centre lines. ceiling = wall height
//   above the room's floor; 0 = no walls (porches and open-plan zones,
//   which are bounded by their neighbours' walls). kind picks the
//   colour; "stairwell" also leaves out the floor plate. z0 (optional)
//   is the floor elevation, e.g. a garage slab below the house floor.
//   tag (optional) - see keep() below. label "" = no label; a list of
//   strings is a multi-line label. label_at (optional) = [x, y, size]
//   moves the label off the room centre, e.g. clear of an island.
// door   = [x, y, axis, width, type, swing, tag]
//   axis "x": the opening sits in a horizontal wall at y and spans
//   x .. x+width; axis "y": vertical wall at x, spans y .. y+width.
//   type: "door" (single leaf), "double", "open" (cased opening with a
//   header), "full" (no wall at all - open-plan edge), "slider" and
//   "glass" (glazed), "garage" (overhead door).
//   swing: +1 / -1 = the leaf opens toward +y / -y (axis "x") or
//   +x / -x (axis "y"); the hinge is at the x / y start of the opening.
// window = [x, y, axis, width, sill, height]
//
// Tags let one table carry alternatives: a row tagged "new" is drawn
// only with the proposed changes on, "old" only with them off; the
// stair options use "stair_new" / "stair_old" the same way.

wall_t = 0.4;   // wall thickness
door_h = 7.0;   // single-door height
open_h = 8.0;   // double doors, cased openings, sliders

wall_color  = [0.93, 0.91, 0.87];
glass_color = [0.55, 0.78, 0.92, 0.45];
leaf_color  = [0.55, 0.35, 0.20];
new_color   = [0.10, 0.60, 0.25];  // leaves of doors added by the changes
label_color = [0.15, 0.15, 0.15];
post_color  = [0.96, 0.95, 0.92];
step_color  = [0.80, 0.80, 0.78];
stair_color = [0.75, 0.72, 0.68];
icf_color   = [0.45, 0.45, 0.45];

// ---- basement alignment (shared by basement.scad and house_combined.scad)
// basement (x, y) + basement_offset() = main-floor (x, y). The basement's
// south wall sits under the front wall line (y = 0) and its east wall
// under the master bath's east wall, which keeps the sketch's exit stair
// outside the house body.
function basement_offset() = [30.1, 0];
// basement floor to main floor: 12 ft basement ceiling + 1 ft floor
function floor_to_floor() = 13;

function kind_color(k) =
    k == "bed"       ? [0.86, 0.91, 0.98] :
    k == "bath"      ? [0.82, 0.93, 0.95] :
    k == "shower"    ? [0.62, 0.82, 0.93] :
    k == "closet"    ? [0.88, 0.88, 0.86] :
    k == "hall"      ? [0.97, 0.95, 0.90] :
    k == "living"    ? [0.98, 0.95, 0.86] :
    k == "kitchen"   ? [1.00, 0.92, 0.80] :
    k == "dining"    ? [0.99, 0.93, 0.84] :
    k == "office"    ? [0.92, 0.90, 0.97] :
    k == "utility"   ? [0.94, 0.89, 0.80] :
    k == "garage"    ? [0.82, 0.82, 0.82] :
    k == "stair"     ? [0.90, 0.88, 0.84] :
    k == "pool"      ? [0.80, 0.92, 0.96] :
    k == "rec"       ? [0.96, 0.96, 0.92] :
    k == "porch"     ? [0.88, 0.94, 0.88] :
                       [0.95, 0.95, 0.95];

function room_z0(r) = len(r) > 7 ? r[7] : 0;
function door_swing(d) = len(d) > 5 ? d[5] : 1;
function door_is_new(d) = len(d) > 6 && d[6] == "new";

// keep a row unless its tag (at index i) is not among the active tags
function keep(row, i, tags) =
    len(row) <= i || row[i] == "" || len([for (t = tags) if (t == row[i]) 1]) > 0;
function active(rows, i, tags) = [for (r = rows) if (keep(r, i, tags)) r];

// ---- rooms -------------------------------------------------------------

module floor_plate(r) {
    color(kind_color(r[6]))
        translate([r[1], r[2], room_z0(r) - 0.15])
            cube([r[3] - r[1], r[4] - r[2], 0.15]);
}

module room_label(r) {
    lines = is_list(r[0]) ? r[0] : [r[0]];
    at = len(r) > 9 ? r[9] : undef;
    w = r[3] - r[1];
    d = r[4] - r[2];
    n = max(concat([for (s = lines) len(s)], [3]));
    k = len(lines);
    // largest text that fits across the room, or along it (turned 90 deg)
    sh = min(2.2, (w - 1.6) / (0.85 * n), (d - 0.6) / (1.5 * k));
    sv = min(2.2, (d - 1.6) / (0.85 * n), (w - 0.6) / (1.5 * k));
    turn = is_undef(at) && sh < 1.0 && sv > 1.3 * sh;
    size = max(is_undef(at) ? (turn ? sv : sh) : at[2], 0.5);
    if (lines[0] != "")
        color(label_color)
            translate([is_undef(at) ? (r[1] + r[3]) / 2 : at[0],
                       is_undef(at) ? (r[2] + r[4]) / 2 : at[1], room_z0(r) + 0.01])
                rotate([0, 0, turn ? 90 : 0])
                    for (i = [0 : k - 1])
                        translate([0, ((k - 1) / 2 - i) * 1.4 * size, 0])
                            linear_extrude(0.05)
                                text(lines[i], size = size, halign = "center", valign = "center");
}

module room_walls(r) {
    x0 = r[1]; y0 = r[2]; x1 = r[3]; y1 = r[4];
    h = r[5]; z0 = room_z0(r); t = wall_t;
    translate([x0 - t / 2, y0 - t / 2, z0]) cube([x1 - x0 + t, t, h]);
    translate([x0 - t / 2, y1 - t / 2, z0]) cube([x1 - x0 + t, t, h]);
    translate([x0 - t / 2, y0 - t / 2, z0]) cube([t, y1 - y0 + t, h]);
    translate([x1 - t / 2, y0 - t / 2, z0]) cube([t, y1 - y0 + t, h]);
}

// ---- openings ----------------------------------------------------------

module door_cut(d) {
    t = d[4];
    zb = t == "garage" ? -1.6 : -0.5;
    zt = t == "full" ? 60 : t == "door" ? door_h : t == "garage" ? 6.5 : open_h;
    if (d[2] == "x") translate([d[0], d[1] - 0.75, zb]) cube([d[3], 1.5, zt - zb]);
    else             translate([d[0] - 0.75, d[1], zb]) cube([1.5, d[3], zt - zb]);
}

module window_cut(w) {
    if (w[2] == "x") translate([w[0], w[1] - 0.75, w[4]]) cube([w[3], 1.5, w[5]]);
    else             translate([w[0] - 0.75, w[1], w[4]]) cube([1.5, w[3], w[5]]);
}

module pane(x, y, axis, width, z, h) {
    color(glass_color)
        if (axis == "x") translate([x, y - 0.05, z]) cube([width, 0.1, h]);
        else             translate([x - 0.05, y, z]) cube([0.1, width, h]);
}

// Door leaf of width lw, hinged at the start (end = 0) or the far end
// (end = 1) of door d, drawn swung 90 degrees open with its floor arc.
module leaf(d, end, lw) {
    u = d[2] == "x" ? [1, 0] : [0, 1];                 // along the wall
    n = d[2] == "x" ? [0, door_swing(d)] : [door_swing(d), 0];
    du = end == 0 ? u : -u;                            // hinge -> closed leaf
    hinge = [d[0], d[1]] + (end == 0 ? [0, 0] : d[3] * u);
    color(door_is_new(d) ? new_color : leaf_color)
        multmatrix([[du[0], n[0], 0, hinge[0]],
                    [du[1], n[1], 0, hinge[1]],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]) {
            translate([-0.08, 0, 0]) cube([0.16, lw, door_h]);
            translate([0, 0, 0.02]) linear_extrude(0.04)
                intersection() {
                    difference() { circle(lw, $fn = 64); circle(lw - 0.12, $fn = 64); }
                    square([lw, lw]);
                }
        }
}

module door_parts(d) {
    t = d[4];
    if (t == "door") leaf(d, 0, d[3]);
    if (t == "double") { leaf(d, 0, d[3] / 2); leaf(d, 1, d[3] / 2); }
    if (t == "slider") pane(d[0], d[1], d[2], d[3], 0, open_h);
    if (t == "glass")  pane(d[0], d[1], d[2], d[3], 0, door_h);
    if (t == "garage")
        color([0.92, 0.92, 0.90])
            if (d[2] == "x") translate([d[0], d[1] - 0.1, -1.5]) cube([d[3], 0.2, 8]);
            else             translate([d[0] - 0.1, d[1], -1.5]) cube([0.2, d[3], 8]);
}

// Draw one level: floor plates, labels, walls with every door and window
// cut, door leaves and glass. Children are extra wall solids (e.g. the
// basement's foundation) that the door cuts must also go through.
module draw_level(rooms, doors, windows) {
    for (r = rooms) if (r[6] != "stairwell") floor_plate(r);
    for (r = rooms) room_label(r);
    color(wall_color) difference() {
        union() {
            for (r = rooms) if (r[5] > 0) room_walls(r);
            children();
        }
        for (d = doors) door_cut(d);
        for (w = windows) window_cut(w);
    }
    for (d = doors) door_parts(d);
    for (w = windows) pane(w[0], w[1], w[2], w[3], w[4], w[5]);
}

// ---- fixtures ----------------------------------------------------------

// fixture = [x0, y0, x1, y1, z0, z1, colour, tag] (a box: counters, appliances...)
module fixtures(list) {
    for (f = list)
        color(f[6]) translate([f[0], f[1], f[4]]) cube([f[2] - f[0], f[3] - f[1], f[5] - f[4]]);
}

module post(x, y, h, s = 0.75) {
    color(post_color) translate([x - s / 2, y - s / 2, 0]) cube([s, s, h]);
}

// Steps from a porch edge down to grade: n risers, starting at the edge
// point (x, y), `width` wide along the edge, leading away toward dir.
module porch_steps(x, y, dir, width, n = 4, rise = 0.5, run = 1.0) {
    color(step_color)
        for (i = [1 : n]) {
            z = -i * rise - 0.5;
            a = (i - 1) * run;
            if (dir == "-y") translate([x, y - a - run, z]) cube([width, run, 0.5]);
            if (dir == "+y") translate([x, y + a, z]) cube([width, run, 0.5]);
            if (dir == "-x") translate([x - a - run, y, z]) cube([run, width, 0.5]);
            if (dir == "+x") translate([x + a, y, z]) cube([run, width, 0.5]);
        }
}

// ICF foundation wall: 8 in concrete core + two 2 5/8 in EPS faces
function icf_wall_t() = (8 + 2 * 2.625) / 12;

// Foundation walls (ICF, t thick) centred on the outline [x0,y0]-[x1,y1].
module foundation_walls(x0, y0, x1, y1, h, t = icf_wall_t()) {
    color(icf_color) {
        translate([x0 - t / 2, y0 - t / 2, 0]) cube([x1 - x0 + t, t, h]);
        translate([x0 - t / 2, y1 - t / 2, 0]) cube([x1 - x0 + t, t, h]);
        translate([x0 - t / 2, y0 - t / 2, 0]) cube([t, y1 - y0 + t, h]);
        translate([x1 - t / 2, y0 - t / 2, 0]) cube([t, y1 - y0 + t, h]);
    }
}

module foundation_slab(x0, y0, x1, y1, t = 1) {
    w = icf_wall_t();
    color(icf_color) translate([x0 - w / 2, y0 - w / 2, -t - 0.15]) cube([x1 - x0 + w, y1 - y0 + w, t]);
}

module landing(x0, y0, x1, y1, z0, z1) {
    color(stair_color) translate([x0, y0, z0]) cube([x1 - x0, y1 - y0, z1 - z0]);
}

// A straight stair flight drawn as solid steps. Footprint [x0,y0]-[x1,y1];
// it descends toward dir ("+x", "-x", "+y", "-y") from z_top at its high
// edge to z_bottom at its low edge in n risers (n - 1 treads). Each step
// is a block down to z_floor, so the flight reads as solid from the side.
module flight(x0, y0, x1, y1, dir, z_top, z_bottom, n, z_floor) {
    rise = (z_top - z_bottom) / n;
    run = ((dir == "+x" || dir == "-x") ? x1 - x0 : y1 - y0) / (n - 1);
    color(stair_color)
        for (i = [1 : n - 1]) {
            z = z_top - i * rise;
            a = (i - 1) * run;
            if (dir == "+x") translate([x0 + a, y0, z_floor]) cube([run, y1 - y0, z - z_floor]);
            if (dir == "-x") translate([x1 - a - run, y0, z_floor]) cube([run, y1 - y0, z - z_floor]);
            if (dir == "+y") translate([x0, y0 + a, z_floor]) cube([x1 - x0, run, z - z_floor]);
            if (dir == "-y") translate([x0, y1 - a - run, z_floor]) cube([x1 - x0, run, z - z_floor]);
        }
}

// The proposed basement stair: a U-stair in the main floor's former bar,
// in main-floor coordinates with the main floor at z_main. Main floor at
// the top, 21 risers of 7.4" down to the basement. upper = false leaves
// out the main-floor landing and guard (for the basement-only model).
module bar_stair(z_main = 0, upper = true) {
    zb = z_main - floor_to_floor();
    zl = z_main - 10 * floor_to_floor() / 21;          // landing after 10 risers
    flight(84.3, 26.9, 92.0, 30.9, "+x", z_main, zl, 10, zb);   // upper flight
    landing(92.0, 21.4, 96.8, 30.9, zb, zl);
    flight(83.5, 21.4, 92.0, 25.4, "-x", zl, zb, 11, zb);       // lower flight
    color(wall_color) translate([83.5, 25.6, zb]) cube([8.5, 1.1, z_main - zb + 3]);
    if (upper) {
        color(kind_color("stair")) translate([82.3, 21, z_main - 0.15]) cube([2, 10.4, 0.15]);
        color(wall_color) {
            translate([84.3, 31.15, z_main]) cube([12.9, 0.3, 3]);   // guard, family-room side
            translate([84.15, 21, z_main]) cube([0.3, 4.6, 3]);      // guard at the top landing
        }
    }
}

// ---- roof --------------------------------------------------------------

// Hip roof over [x0,y0]-[x1,y1] plus an overhang, eave at z = eave,
// pitch = rise / run (8/12 = 0.667). Ridge runs along the longer side.
module hip_roof(x0, y0, x1, y1, eave, pitch, overhang = 1.5) {
    a = x0 - overhang; b = y0 - overhang;
    c = x1 + overhang; e = y1 + overhang;
    r = min(c - a, e - b) / 2 * 0.999;   // run to the ridge; x 0.999 keeps a ridge on square roofs
    top = eave + pitch * r;
    if (c - a >= e - b) {
        m = (b + e) / 2;
        polyhedron(points = [[a, b, eave], [c, b, eave], [c, e, eave], [a, e, eave],
                             [a + r, m, top], [c - r, m, top]],
                   faces = [[0, 1, 2, 3], [0, 4, 5, 1], [1, 5, 2], [2, 5, 4, 3], [3, 4, 0]]);
    } else {
        m = (a + c) / 2;
        polyhedron(points = [[a, b, eave], [c, b, eave], [c, e, eave], [a, e, eave],
                             [m, b + r, top], [m, e - r, top]],
                   faces = [[0, 1, 2, 3], [0, 4, 1], [1, 4, 5, 2], [2, 5, 3], [3, 5, 4, 0]]);
    }
}

// roof block = [x0, y0, x1, y1, eave, pitch, overhang]
module roofs(blocks, roof_color, opacity = 1) {
    color(concat(roof_color, [opacity]))
        for (b = blocks) hip_roof(b[0], b[1], b[2], b[3], b[4], b[5], b[6]);
}
