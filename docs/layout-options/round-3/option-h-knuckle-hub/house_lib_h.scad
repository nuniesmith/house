// house_lib.scad - shared drawing modules for the house models.
// Units: feet. x = east, y = north, z = up; the main floor is z = 0.
// Both levels use the same plan coordinates: x = 0 is the garage's west
// wall, y = 0 the front wall line of the den and breakfast bay.
// Visualisation only - NOT construction documents.
//
// The level files (main_floor.scad, basement.scad) describe each floor
// as tables and call draw_level() below, so one table row drives a
// room's floor plate, label and walls, and one door row drives both
// the wall cut and the door leaf. foundation.scad does the same for
// the concrete.
//
// room   = [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
//   (x0, y0)-(x1, y1) are wall centre lines. ceiling = wall height
//   above the room's floor; 0 = no walls (porches and open-plan zones,
//   which are bounded by their neighbours' walls). kind picks the
//   colour; "stairwell", "tiered" and "pit" leave out the floor plate
//   (stair opening, theatre tiers, pool deck - drawn separately).
//   z0 (optional) is the floor elevation, e.g. a garage slab below the
//   house floor. tag (optional) - see keep() below. label "" = no
//   label; a list of strings is a multi-line label. label_at
//   (optional) = [x, y, size] or [x, y, size, angle] moves the label
//   off the room centre, e.g. clear of an island or a door swing.
// door   = [x, y, axis, width, type, swing, tag]
//   axis "x": the opening sits in a horizontal wall at y and spans
//   x .. x+width; axis "y": vertical wall at x, spans y .. y+width.
//   type: "door" (single leaf), "double", "open" (cased opening with a
//   header), "full" (no wall at all - open-plan edge), "slider" and
//   "glass" (glazed), "garage" (overhead door).
//   swing: +1 / -1 = the leaf opens toward +y / -y (axis "x") or
//   +x / -x (axis "y"); the hinge is at the x / y start of the opening.
// window = [x, y, axis, width, sill, height]
// fixture = [x0, y0, x1, y1, z0, z1, colour, tag, shape]
//   a box (counters, appliances, furniture); shape "round" draws the
//   cylinder that fits the box instead (round tables, tanks).
//
// Tags let one table carry alternatives: a row is drawn only when its
// tag (if any) is among the active tags.

wall_t = 0.4;   // wall thickness
door_h = 7.0;   // single-door height
open_h = 8.0;   // double doors, cased openings, sliders

wall_color  = [0.93, 0.91, 0.87];
glass_color = [0.55, 0.78, 0.92, 0.45];
leaf_color  = [0.55, 0.35, 0.20];
new_color   = [0.10, 0.60, 0.25];  // door leaves that the review added
label_color = [0.15, 0.15, 0.15];
post_color  = [0.96, 0.95, 0.92];
step_color  = [0.80, 0.80, 0.78];
stair_color = [0.75, 0.72, 0.68];
icf_color   = [0.45, 0.45, 0.45];
floor_frame = [0.80, 0.68, 0.50];   // main-floor trusses / subfloor

// `use <house_lib.scad>` brings in functions and modules but not
// variables, so the level files read these through functions
function wall_t()      = wall_t;
function stair_color() = stair_color;
function floor_frame() = floor_frame;

// Colour a part. When a section cut is active ($cut = [axis, at], set by
// house_combined.scad) the part is also cut, with a cutting box of the
// same colour, so each material keeps its colour on the cut face.
// The level files call their top module inside let ($cut = undef); a
// top-level $cut assignment in a used file would hide the caller's.
module paint(c) {
    if (is_undef($cut)) color(c) children();
    else {
        intersection() { color(c) children(); color(c) keep_side($cut); }
        color(cut_shade(c)) cut_face($cut) children();
    }
}
// cut faces are drawn darker than the faces seen beyond the cut
function cut_shade(c) = [c[0] * 0.72, c[1] * 0.72, c[2] * 0.72, len(c) > 3 ? c[3] : 1];
module keep_side(cut) {        // the half kept by a section: x >= at or y >= at
    if (cut[0] == "x") translate([cut[1], -150, -100]) cube([300, 300, 200]);
    else               translate([-150, cut[1], -100]) cube([300, 300, 200]);
}
// The cut face as a thin slab just in front of the cut. OpenSCAD's preview
// gives every face that lies in the cut plane the colour of the last part
// drawn, so each part's outline in the plane is drawn again as its own
// object: projection(cut = true) with the plane moved to z = 0. A marker
// cube far off the model keeps an empty cut from failing.
module cut_face(cut) {
    a = cut[1];
    module outline() {
        difference() {
            projection(cut = true) { children(); translate([4000, 4000, -0.5]) cube(1); }
            translate([3999, 3999]) square(3);
        }
    }
    if (cut[0] == "x")
        rotate([0, 90, 0]) translate([0, 0, a - 0.03]) linear_extrude(0.02)
            outline() translate([0, 0, -a]) rotate([0, -90, 0]) children();
    else
        rotate([-90, 0, 0]) translate([0, 0, a - 0.03]) linear_extrude(0.02)
            outline() translate([0, 0, -a]) rotate([90, 0, 0]) children();
}

// ---- levels ---------------------------------------------------------------
// main floor (finished) at z = 0; grade 2 ft below it; basement slab
// (top) floor_to_floor() below it. The main floor assembly is 18" open-web
// floor trusses + subfloor + finish, so 13.75 ft gives the basement a
// 12 ft ceiling. For 10 ft set floor_to_floor() = 11.75: the stair drops
// to 19 risers of 7.42" and its foot moves 2.6 ft north; the rooms, the
// foundation and the exit stair follow.
function floor_to_floor()   = 11.75;
function main_floor_depth() = 1.625;
function grade()            = -2;
function basement_ceiling() = floor_to_floor() - main_floor_depth() - 0.125;

// ---- main stair (Option H) --------------------------------------------------
// One straight flight between the floors, running north -> south: top nosing on
// the main floor at y = stair_top_y() at the junction hall, foot in the basement
// at y = stair_foot_y() under the foyer. 19 risers of 7.42 in (3.58 m floor to
// floor), 18 treads of 10.5 in, no landing in the flight (ABC 9.8.3.3.(1)); a
// level landing at the top and the bottom; wall to wall 5.4 ft (about 4.9 ft
// clear), so a stair lift can be added later.
function stair_x()      = [50, 55.4];           // main-floor opening, wall centre lines
function stair_y()      = [14.4, 26.4];         // wall centre lines; opening 11.8 ft from the nosing
function stair_risers() = ceil(floor_to_floor() * 12 / 7.5);   // 19
function stair_rise()   = floor_to_floor() / stair_risers();
function stair_run()    = 10.5 / 12;
function stair_top_y()  = 26.2;                   // top nosing
function stair_foot_y() = stair_top_y() - (stair_risers() - 1) * stair_run();
function stair_top_x()  = stair_x()[0];
function stair_foot_x() = stair_x()[0];

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

module floor_plate(r) {     // its top 0.005 ft proud, so it shows over a slab at the floor level
    paint(kind_color(r[6]))
        translate([r[1], r[2], room_z0(r) - 0.145])
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
        paint(label_color)
            translate([is_undef(at) ? (r[1] + r[3]) / 2 : at[0],
                       is_undef(at) ? (r[2] + r[4]) / 2 : at[1], room_z0(r) + 0.01])
                rotate([0, 0, is_undef(at) ? (turn ? 90 : 0) : (len(at) > 3 ? at[3] : 0)])
                    for (i = [0 : k - 1])
                        translate([0, ((k - 1) / 2 - i) * 1.4 * size, 0])
                            linear_extrude(0.05, convexity = 10)
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
    paint(glass_color)
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
    paint(door_is_new(d) ? new_color : leaf_color)
        multmatrix([[du[0], n[0], 0, hinge[0]],
                    [du[1], n[1], 0, hinge[1]],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]) {
            translate([-0.08, 0, 0]) cube([0.16, lw, door_h]);
            translate([0, 0, 0.02]) linear_extrude(0.04, convexity = 4)
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
        paint([0.92, 0.92, 0.90])
            if (d[2] == "x") translate([d[0], d[1] - 0.1, -1.5]) cube([d[3], 0.2, 8]);
            else             translate([d[0] - 0.1, d[1], -1.5]) cube([0.2, d[3], 8]);
}

// Draw one level: floor plates, labels, walls with every door and window
// cut, door leaves and glass. Children are extra wall solids that the
// door and window cuts must also go through.
module draw_level(rooms, doors, windows) {
    for (r = rooms) if (r[6] != "stairwell" && r[6] != "tiered" && r[6] != "pit") floor_plate(r);
    for (r = rooms) room_label(r);
    paint(wall_color) difference() {
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

module fixtures(list) {
    for (f = list)
        paint(f[6])
            if (len(f) > 8 && f[8] == "round")
                translate([(f[0] + f[2]) / 2, (f[1] + f[3]) / 2, f[4]])
                    resize([f[2] - f[0], f[3] - f[1], f[5] - f[4]])
                        cylinder(d = 1, h = 1, $fn = 48);
            else
                translate([f[0], f[1], f[4]]) cube([f[2] - f[0], f[3] - f[1], f[5] - f[4]]);
}

module post(x, y, h, s = 0.75) {
    paint(post_color) translate([x - s / 2, y - s / 2, 0]) cube([s, s, h]);
}

// Steps from a porch edge down to grade: n risers, starting at the edge
// point (x, y), `width` wide along the edge, leading away toward dir.
module porch_steps(x, y, dir, width, n = 4, rise = 0.5, run = 1.0) {
    paint(step_color)
        for (i = [1 : n]) {
            z = -i * rise - 0.5;
            a = (i - 1) * run;
            if (dir == "-y") translate([x, y - a - run, z]) cube([width, run, 0.5]);
            if (dir == "+y") translate([x, y + a, z]) cube([width, run, 0.5]);
            if (dir == "-x") translate([x - a - run, y, z]) cube([run, width, 0.5]);
            if (dir == "+x") translate([x + a, y, z]) cube([run, width, 0.5]);
        }
}

module landing(x0, y0, x1, y1, z0, z1) {
    paint(stair_color) translate([x0, y0, z0]) cube([x1 - x0, y1 - y0, z1 - z0]);
}

// A straight stair flight drawn as solid steps. Footprint [x0,y0]-[x1,y1];
// it descends toward dir ("+x", "-x", "+y", "-y") from z_top at its high
// edge to z_bottom at its low edge in n risers (n - 1 treads). Each step
// is a block down to z_floor, so the flight reads as solid from the side.
module flight(x0, y0, x1, y1, dir, z_top, z_bottom, n, z_floor) {
    rise = (z_top - z_bottom) / n;
    run = ((dir == "+x" || dir == "-x") ? x1 - x0 : y1 - y0) / (n - 1);
    paint(stair_color)
        for (i = [1 : n - 1]) {
            z = z_top - i * rise;
            a = (i - 1) * run;
            if (dir == "+x") translate([x0 + a, y0, z_floor]) cube([run, y1 - y0, z - z_floor]);
            if (dir == "-x") translate([x1 - a - run, y0, z_floor]) cube([run, y1 - y0, z - z_floor]);
            if (dir == "+y") translate([x0, y0 + a, z_floor]) cube([x1 - x0, run, z - z_floor]);
            if (dir == "-y") translate([x0, y1 - a - run, z_floor]) cube([x1 - x0, run, z - z_floor]);
        }
}

// The main stair in house coordinates (main floor at z_main). Treads run
// south from the top nosing; each is a solid block down to the basement floor,
// except under the main-floor opening's neighbours, where it stops at the
// basement ceiling.
module main_stair(z_main = 0, y_open = 14.4, rail = true) {
    x0 = stair_x()[0] + wall_t / 2;
    x1 = stair_x()[1] - wall_t / 2;
    zb = z_main - floor_to_floor();
    paint(stair_color)
        for (i = [1 : stair_risers() - 1]) {
            ya = stair_top_y() - i * stair_run();           // south edge of tread i
            z = z_main - i * stair_rise();
            zf = ya + stair_run() / 2 < y_open ? z_main - main_floor_depth() - 0.125 : zb;
            translate([x0, ya, zf]) cube([x1 - x0, stair_run() + 0.08, z - zf]);
        }
    if (rail)
        paint([0.40, 0.28, 0.18])
            for (x = [x0 + 0.1, x1 - 0.2])
                hull() {
                    translate([x, stair_top_y(), z_main + 2.8]) cube([0.1, 0.1, 0.12]);
                    translate([x, stair_foot_y(), zb + 2.8]) cube([0.1, 0.1, 0.12]);
                }
}

// ---- roof --------------------------------------------------------------

// Hip roof over [x0,y0]-[x1,y1] plus an overhang, eave at z = eave,
// pitch = rise / run (6/12 = 0.5). Ridge runs along the longer side.
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
    paint(concat(roof_color, [opacity]))
        for (b = blocks) hip_roof(b[0], b[1], b[2], b[3], b[4], b[5], b[6]);
}
