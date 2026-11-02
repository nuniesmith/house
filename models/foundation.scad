// foundation.scad - the concrete: basement walls and footings, the slab
// with the stepped theatre floor, the pool + spa shell, frost walls
// under the parts of the main floor that have no basement, porch piers,
// and the earth around it all (for section views).
// Units: feet, house coordinates (see house_lib.scad); z = 0 is the
// main floor, so everything here sits at its real elevation.
// Visualisation only - the sizes follow the spec in
// docs/house/Redesign-and-Spec-2026-11-02.md and need an engineer's
// design before they are built.

use <house_lib.scad>

part = "all";          // [all, basement, frost]
show_earth = false;

// no section cut when this file is opened on its own ($cut is a special
// variable, so house_combined.scad's value reaches these modules)
let ($cut = undef) foundation(part, show_earth);

/* [Hidden] */
concrete = [0.62, 0.62, 0.60];
eps      = [0.93, 0.90, 0.76];   // ICF foam faces, rigid insulation
stone    = [0.52, 0.50, 0.47];
earth_c  = [0.55, 0.42, 0.30];
lawn     = [0.48, 0.66, 0.40];
liner    = [0.55, 0.80, 0.88];   // pool / spa interior finish

// ---- elevations (z, feet; main floor = 0) ----------------------------------
function slab_top()     = -floor_to_floor();             // basement floor
function slab_t()       = 4 / 12;
function base_t()       = 6 / 12;                        // clear stone + radon layer
function footing_top()  = slab_top() - slab_t() - base_t();
function footing_t()    = 10 / 12;
function footing_w()    = 2.0;                           // 24" under the 13 1/4" ICF wall
function sill()         = -main_floor_depth();           // top of the foundation walls
function frost_bottom() = grade() - 4;                   // frost wall footings: 4 ft below grade
function icf_wall_t()   = (8 + 2 * 2.625) / 12;          // 8" core + two 2 5/8" EPS faces = 13 1/4"

// basement outline: wall centre lines, counter-clockwise
function basement_outline() = [
    [22.16, 63.16], [22.16, 35.08], [35.27, 35.08], [35.27, 5.79], [81.68, 5.79],
    [81.68, 13.43], [103.04, 13.43], [103.04, 41.94], [96.33, 41.94], [96.33, 52.76],
    [69.38, 52.76], [69.38, 50.35], [54.14, 50.35], [54.14, 63.16],
];

// interior bearing lines (under the main floor's bearing walls) with
// thickened-slab strip footings [x0, y0, x1, y1]
function bearing_lines() = [
    [54.14, 5.79,  54.14, 50.35],
    [69.38, 18.15, 69.38, 50.35],
    [96.33, 13.43, 96.33, 41.94],
    [54.14, 18.15, 103.04, 18.15],
];

// ---- pool + spa ------------------------------------------------------------
// Water areas (inside face of the shell), as drawn on docs/house/basement.jpg.
function pool_xy()    = [75.07, 32.66, 90.04, 47.70];    // 15 x 15
function spa_xy()     = [82.07, 23.77, 90.04, 31.91];    // 8 x 8'-2", shares the pool's south wall
function shell_t()    = 0.75;                            // 9" walls
function shell_floor()= 10 / 12;
function pool_water() = slab_top() - 0.5;                // 6" below the deck
function pool_depth() = 4.5;                             // water depth, uniform
function spa_rim()    = slab_top() + 1.5;                // raised 18" above the deck
function spa_water()  = spa_rim() - 2 / 12;
function spa_depth()  = 3.5;
function spill_x()    = [85.0, 87.0];                    // spillway, spa -> pool
function pit_insul()  = 2 / 12;                          // rigid insulation under the shells
function pool_bottom()= pool_water() - pool_depth() - shell_floor();
function spa_bottom() = spa_water() - spa_depth() - shell_floor();

// ---- home theatre: stadium tiers (z offsets below the basement floor) -----
// The rear tier is the basement floor (the entrance level); one 7 1/2"
// step, then the front tier 15" down. The lowered "pit" stops short of
// the walls - a 1 ft ledge each side and the 2 1/2 ft screen stage at the
// north end stay at floor level - so it is clear of the footings' 1:1
// bearing zones and they need no stepping down. The spec in docs/house/
// has the sightline check.
function theatre_xy()    = [54.34, 29.32, 69.18, 49.80];  // inside faces (north: the ICF wall)
function theatre_pit_x() = [55.5, 68.0];                   // the lowered tiers' x range
function theatre_stage() = [47.3, 49.80];                  // y range, at floor level
function theatre_tiers() = [    // [y0, y1, drop]
    [29.32, 36.6,  0],
    [36.6,  37.5,  0.625],
    [37.5,  47.3,  1.25],
];
function theatre_pit_bottom() = slab_top() - theatre_tiers()[2][2] - slab_t() - base_t();

// ---- frost walls: main-floor walls that have no basement under them ------
// [x0, y0, x1, y1, top]: 8" concrete on a 20" x 8" footing 4 ft below grade
function frost_walls() = [
    [0, 1.25, 24.34, 1.25, -1.25], [0, 1.25, 0, 35.46, -1.25],        // garage (curb above the slab)
    [0, 35.46, 24.34, 35.46, -1.25], [24.34, 1.25, 24.34, 35.46, -1.25],
    [7.27, 35.46, 7.27, 62.04, sill()], [7.27, 62.04, 17.5, 62.04, sill()],   // bedroom wing
    [17.5, 62.04, 17.5, 66.64, sill()], [17.5, 66.64, 32.6, 66.64, sill()],
    [32.6, 63.42, 32.6, 66.64, sill()],
    [24.34, 20.82, 35.27, 20.82, sill()],                              // scullery
    [54.14, 63.42, 69.14, 63.42, sill()], [69.14, 52.76, 69.14, 63.42, sill()],   // nook
    [96.33, 48.16, 108.62, 48.16, sill()], [108.62, 48.16, 108.62, 52.86, sill()],  // office, master wing
    [108.62, 52.86, 126.97, 52.86, sill()], [126.97, 29.51, 126.97, 52.86, sill()],
    [126.97, 29.51, 128.13, 29.51, sill()], [128.13, 9.31, 128.13, 29.51, sill()],
    [95.95, 9.31, 128.13, 9.31, sill()],
    [81.12, 0, 95.95, 0, sill()], [95.95, 0, 95.95, 9.31, sill()],     // den, entry, breakfast bay
    [81.12, 0, 81.12, 3.72, sill()], [69.14, 3.72, 81.12, 3.72, sill()],
    [69.14, 0, 69.14, 3.72, sill()], [54.1, 0, 69.14, 0, sill()], [54.1, 0, 54.1, 6.28, sill()],
];

// Footings deepened below a dug-out area beside them [x0, y0, x1, y1,
// bottom]: round the pool room, the pool and spa pits are dug below the
// footings' 1:1 bearing zone, so those footings go down to the pit depth
// (or the shell is designed to retain them - the engineer's call).
function deep_footings() = [
    for (s = [[69.38, 18.15, 96.33, 18.15], [69.38, 52.76, 96.33, 52.76],
              [69.38, 18.15, 69.38, 52.76], [96.33, 18.15, 96.33, 52.76]])
        concat(s, [pool_bottom() - base_t()])
];

// porch piers under the posts (main_floor.scad's main_posts) [x, y]
function porch_piers() = [
    [49.69, -14.81], [57.4, -14.81], [65.1, -14.81], [69.2, -14.81], [81.1, -14.81],
    [88.6, -14.81], [96.3, -14.81], [100.96, -14.81], [49.69, -7.0], [49.69, 5.83],
    [100.96, -7.0], [100.96, 8.86], [69.59, 64.25], [95.18, 64.25], [108.17, 59.02],
    [109.07, 61.95], [126.52, 61.95], [127.42, 59.02], [137.21, 59.02], [137.21, 51.1],
    [137.21, 43.2], [137.21, 35.2], [137.21, 27.29],
];

// ---- basement exit stair ----------------------------------------------------
// An areaway outside the gym's north wall, in the back yard and clear of
// every porch: a 3'-6" door in the gym's north wall opening in (so snow
// can't block it), a landing at the basement floor, and a straight
// flight rising east along the house to grade, just west of the deck.
// East of the gym its house side is the nook's frost wall, carried down
// to the areaway floor. exit_areaway() = [x0, y0, x1, y1], the clear
// inside; the flight runs from exit_landing_x()[1] to x1.
function exit_door()      = [46.2, 3.5];                    // [x, width] in the gym's north wall, y = 63.16
function exit_rise()      = floor_to_floor() + grade();      // basement floor up to grade
function exit_risers()    = ceil(exit_rise() * 12 / 7.5);    // 19 of 7.42" for a 12 ft basement
function exit_run()       = 11 / 12;                         // 11" treads outdoors
function exit_landing_x() = [45.6, 50.3];
function exit_areaway()   = [45.6, 63.75, exit_landing_x()[1] + (exit_risers() - 1) * exit_run(), 67.75];
function exit_wall_t()    = 8 / 12;
function exit_top_pad()   = 2.2;                             // landing at grade past the top step, up to the deck
// its footprint with the walls and the top landing, from the house face
// out [x0, y0, x1, y1]
function exit_footprint(g = 0) = let(a = exit_areaway(), t = exit_wall_t())
    [a[0] - t - g, 63.09 - g, a[2] + exit_top_pad() + g, a[3] + t + g];

// ---- 2D helpers -------------------------------------------------------------
module outline2d(d = 0) { offset(delta = d) polygon(basement_outline()); }
module ring2d(d_out, d_in) { difference() { outline2d(d_out); outline2d(d_in); } }
module rect2d(r, grow = 0) { translate([r[0] - grow, r[1] - grow]) square([r[2] - r[0] + 2 * grow, r[3] - r[1] + 2 * grow]); }
function shell_out(r) = [r[0] - shell_t(), r[1] - shell_t(), r[2] + shell_t(), r[3] + shell_t()];
// convexity: the preview needs it for non-convex outlines (the wall ring) once they are cut
module zslab(z0, z1) { translate([0, 0, z0]) linear_extrude(z1 - z0, convexity = 10) children(); }
module strip(s, w, z0, z1) {      // a straight strip w wide along segment s = [x0, y0, x1, y1, ...]
    translate([min(s[0], s[2]) - w / 2, min(s[1], s[3]) - w / 2, z0])
        cube([abs(s[2] - s[0]) + w, abs(s[3] - s[1]) + w, z1 - z0]);
}
// the theatre's lowered area (step + front tier)
module theatre_low2d(grow = 0) {
    x = theatre_pit_x(); y = [theatre_tiers()[1][0], theatre_tiers()[2][1]];
    translate([x[0] - grow, y[0] - grow]) square([x[1] - x[0] + 2 * grow, y[1] - y[0] + 2 * grow]);
}

// ---- basement: ICF walls, footings, slab, pool + spa, theatre tiers ------
module basement_concrete() {
    w = icf_wall_t();
    core = 8 / 12;
    // ICF walls: concrete core between two foam faces, with the exit door
    paint(concrete) difference() { zslab(footing_top(), sill()) ring2d(core / 2, -core / 2); exit_door_cut(); }
    paint(eps) difference() {
        zslab(footing_top(), sill()) difference() { ring2d(w / 2, -w / 2); ring2d(core / 2, -core / 2); }
        exit_door_cut();
    }
    // perimeter footings and the interior bearing-line footings
    paint(concrete) zslab(footing_top() - footing_t(), footing_top()) ring2d(footing_w() / 2, -footing_w() / 2);
    paint(concrete) for (s = bearing_lines()) strip(s, 1.67, footing_top() - footing_t(), footing_top());
    // deepened footings round the pool room (deep_footings())
    paint(concrete) for (s = deep_footings()) strip(s, 1.0, s[4], footing_top() - footing_t());

    // stone (radon) layer and the slab, with the pool pit and the
    // theatre's lowered area left out; the theatre tiers step down
    module slab2d() {
        difference() {
            outline2d(-w / 2);
            rect2d(shell_out(pool_xy()));
            rect2d(shell_out(spa_xy()));
            theatre_low2d();
        }
    }
    paint(stone) zslab(footing_top(), slab_top() - slab_t()) slab2d();
    paint(concrete) zslab(slab_top() - slab_t(), slab_top()) slab2d();
    x = theatre_pit_x();
    for (tier = [theatre_tiers()[1], theatre_tiers()[2]]) {
        z = slab_top() - tier[2];
        paint(stone) translate([x[0], tier[0], z - slab_t() - base_t()]) cube([x[1] - x[0], tier[1] - tier[0], base_t()]);
        paint(concrete) translate([x[0], tier[0], z - slab_t()]) cube([x[1] - x[0], tier[1] - tier[0], slab_t()]);
    }
    pool_shell();
    exit_areaway_concrete();
}

module exit_door_cut() {
    d = exit_door();
    translate([d[0], 63.16 - 1, slab_top()]) cube([d[1], 2, 7]);
}

// the exit stair's areaway: slab, the outer (north) and west retaining
// walls on 20" footings, up to a 6" curb above grade, the nook's frost
// wall carried down to the areaway floor, and a landing slab at grade
// past the top step (the steps themselves: basement.scad)
module exit_areaway_concrete() {
    a = exit_areaway(); t = exit_wall_t();
    zf = slab_top() - slab_t();
    ft = zf - footing_t();
    top = grade() + 0.5;
    paint(stone) translate([a[0], a[1], zf - base_t()]) cube([a[2] - a[0], a[3] - a[1], base_t()]);
    paint(concrete) {
        translate([a[0], a[1], zf]) cube([a[2] - a[0], a[3] - a[1], slab_t()]);
        translate([a[0] - t, a[3], zf]) cube([a[2] - a[0] + t, t, top - zf]);              // north wall
        translate([a[0] - t, a[1], zf]) cube([t, a[3] - a[1], top - zf]);                    // west wall
        translate([a[0] - t - 0.5, a[3] + t / 2 - 0.835, ft]) cube([a[2] - a[0] + t + 0.5, 1.67, footing_t()]);
        translate([a[0] - t / 2 - 0.835, a[1], ft]) cube([1.67, a[3] - a[1], footing_t()]);
        translate([54.14, 63.09, ft]) cube([a[2] - 54.14, 2 / 3, frost_bottom() - ft]);    // nook frost wall, deepened
        translate([a[2], a[1], grade() - 0.33]) cube([exit_top_pad(), a[3] + t - a[1], 0.33]);   // top landing
    }
}

// pool + spa: 9" shotcrete walls and 10" floors on 2" rigid insulation and
// 6" stone; the spa is raised 18" above the deck and spills into the pool
module pool_shell() {
    p = pool_xy(); s = spa_xy();
    // under-shell insulation and stone
    for (b = [[p, pool_bottom()], [s, spa_bottom()]]) {
        paint(eps) zslab(b[1] - pit_insul(), b[1]) rect2d(shell_out(b[0]), pit_insul());
        paint(stone) zslab(b[1] - pit_insul() - base_t(), b[1] - pit_insul()) rect2d(shell_out(b[0]), pit_insul());
        // insulation round the outside of the shell walls, below the slab
        paint(eps) zslab(b[1], slab_top() - slab_t())
            difference() { rect2d(shell_out(b[0]), pit_insul()); rect2d(shell_out(b[0])); }
    }
    paint(concrete) {
        // pool: floor + walls up to the deck
        zslab(pool_bottom(), pool_bottom() + shell_floor()) rect2d(shell_out(p));
        zslab(pool_bottom(), slab_top()) difference() { rect2d(shell_out(p)); rect2d(p); }
        // entry steps in the north-west corner, 12" risers down to the floor
        for (i = [1 : 4])
            translate([p[0], p[3] - i, pool_bottom()]) cube([4, 1, slab_top() - i - pool_bottom()]);
        // spa: floor, raised walls (the north one is the shared wall), bench
        zslab(spa_bottom(), spa_bottom() + shell_floor()) rect2d(shell_out(s));
        difference() {
            zslab(spa_bottom(), spa_rim()) difference() { rect2d(shell_out(s)); rect2d(s); }
            translate([spill_x()[0], s[3] - 0.1, spa_water()]) cube([spill_x()[1] - spill_x()[0], shell_t() + 0.2, 5]);
        }
        bench = spa_water() - 1.75;
        zslab(spa_bottom(), bench) difference() { rect2d(s); translate([s[0] + 1.5, s[1] + 1.5]) square([s[2] - s[0] - 3, s[3] - s[1] - 1.5]); }
    }
    // interior finish (plaster / tile) as a thin skin
    paint(liner) {
        translate([p[0], p[1], pool_bottom() + shell_floor()]) cube([p[2] - p[0], p[3] - p[1], 0.04]);
        translate([s[0], s[1], spa_bottom() + shell_floor()]) cube([s[2] - s[0], s[3] - s[1], 0.04]);
    }
}

// ---- frost walls, garage slab, porch piers --------------------------------
// Frost walls and the garage slab stop at the basement walls' outside
// face (where they meet, the basement wall carries the floor), and a
// porch post that stands on a basement wall needs no pier.
module frost_foundation() {
    paint(concrete)
        difference() {
            union() {
                for (f = frost_walls()) {
                    strip(f, 8 / 12, frost_bottom() + 8 / 12, f[4]);
                    strip(f, 20 / 12, frost_bottom(), frost_bottom() + 8 / 12);
                }
                translate([0.33, 1.58, -1.5 - slab_t()]) cube([23.68, 33.55, slab_t()]);   // garage slab
            }
            basement_footprint();
            let(a = exit_areaway()) translate([a[0], a[1], slab_top()]) cube([a[2] - a[0], a[3] - a[1], 20]);
        }
    paint(stone)
        difference() {
            translate([0.33, 1.58, -1.5 - slab_t() - base_t()]) cube([23.68, 33.55, base_t()]);
            basement_footprint();
        }
    paint(concrete)
        for (p = piers()) {
            translate([p[0], p[1], frost_bottom() - 0.5]) cylinder(d = 2.0, h = 0.67, $fn = 24);   // bell
            translate([p[0], p[1], frost_bottom()]) cylinder(d = 1.0, h = grade() - frost_bottom() + 1.5, $fn = 24);
        }
}
module basement_footprint() { zslab(frost_bottom() - 2, 2) outline2d(icf_wall_t() / 2); }

// the porch piers that are not on (or within 6" of) a basement wall
function piers() = [for (p = porch_piers()) if (!near_outline(p, icf_wall_t() / 2 + 0.5)) p];
function near_outline(p, d) = let(o = basement_outline(), n = len(o))
    inside(p, o) || min([for (i = [0 : n - 1]) seg_dist(p, o[i], o[(i + 1) % n])]) < d;
// point in polygon (even-odd rule) and point-to-segment distance
function inside(p, poly) = len([for (i = [0 : len(poly) - 1])
    let(a = poly[i], b = poly[(i + 1) % len(poly)])
    if ((a[1] > p[1]) != (b[1] > p[1]) && p[0] < a[0] + (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1])) 1]) % 2 == 1;
function seg_dist(p, a, b) = let(ab = b - a, t = max(0, min(1, ((p - a) * ab) / (ab * ab)))) norm(p - (a + t * ab));

// ---- earth (for sections) ---------------------------------------------------
// The ground round the house from grade down, with everything that is dug
// out of it removed: the basement (walls, footings, stone), the pool and
// spa pits, the theatre's lowered area, frost walls, piers, the garage
// slab and an 18" crawlspace under the main floor where there is no
// basement (crawl_rooms: the main floor's heated rooms).
module earth(crawl_rooms = []) {
    // (each colour wraps a finished shape, so a section's cut face is right)
    paint(earth_c) difference() { translate([-25, -45, -28]) cube([190, 140, 28 + grade() - 0.1]); dug_out(crawl_rooms); }
    // the lawn is cut in 2D: a 3D cut-out's faces would take the lawn's
    // colour wherever they line up with a visible face in the preview
    paint(lawn) translate([0, 0, grade() - 0.1]) linear_extrude(0.1, convexity = 10) lawn2d(crawl_rooms);
}
module lawn2d(crawl_rooms, g = 0.02) {
    difference() {
        translate([-25, -45]) square([190, 140]);
        outline2d(icf_wall_t() / 2 + g);
        for (r = crawl_rooms) translate([r[1], r[2]]) square([r[3] - r[1], r[4] - r[2]]);
        for (f = frost_walls()) let(w = 8 / 12 + 2 * g)
            translate([min(f[0], f[2]) - w / 2, min(f[1], f[3]) - w / 2]) square([abs(f[2] - f[0]) + w, abs(f[3] - f[1]) + w]);
        for (p = piers()) translate([p[0], p[1]]) circle(d = 1.0 + 2 * g, $fn = 24);
        translate([0.33 - g, 1.58 - g]) square([23.68 + 2 * g, 33.55 + 2 * g]);   // garage slab
        rect2d(exit_footprint(g));                                               // exit stair
    }
}
// Each volume is 0.01 ft bigger than what it makes room for: in the
// preview a dug face that coincides with a visible face would paint it
// earth-coloured.
module dug_out(crawl_rooms) {
    g = 0.01;
    w = icf_wall_t();
    ft = footing_top();
    union() {
        zslab(ft - footing_t() - g, ft + g) outline2d(footing_w() / 2 + g);
        zslab(ft, 1) outline2d(w / 2 + g);
        for (s = bearing_lines()) strip(s, 1.67 + 2 * g, ft - footing_t() - g, ft + g);
        for (s = deep_footings()) strip(s, 1.0 + 2 * g, s[4] - g, ft);
        zslab(pool_bottom() - pit_insul() - base_t() - g, ft + g) rect2d(shell_out(pool_xy()), pit_insul() + g);
        zslab(spa_bottom() - pit_insul() - base_t() - g, ft + g) rect2d(shell_out(spa_xy()), pit_insul() + g);
        zslab(theatre_pit_bottom() - g, ft + g) theatre_low2d(g);
        for (f = frost_walls()) {
            strip(f, 8 / 12 + 2 * g, frost_bottom() - g, 1);
            strip(f, 20 / 12 + 2 * g, frost_bottom() - g, frost_bottom() + 8 / 12 + g);
        }
        for (p = piers()) {
            translate([p[0], p[1], frost_bottom() - 0.5 - g]) cylinder(d = 2.0 + 2 * g, h = 0.67 + 2 * g, $fn = 24);
            translate([p[0], p[1], frost_bottom()]) cylinder(d = 1.0 + 2 * g, h = 10, $fn = 24);
        }
        translate([0.33 - g, 1.58 - g, -1.5 - slab_t() - base_t() - g]) cube([23.68 + 2 * g, 33.55 + 2 * g, 3]);
        // the exit stair's areaway with its walls, footings and stone
        let(a = exit_areaway(), t = exit_wall_t(), e = exit_footprint(g), ft = slab_top() - slab_t() - footing_t()) {
            translate([e[0], e[1], slab_top() - slab_t() - base_t() - g]) cube([a[2] + g - e[0], e[3] - e[1], 20]);
            translate([a[2], e[1], grade() - 0.33 - g]) cube([e[2] - a[2], e[3] - e[1], 5]);     // top landing
            translate([a[0] - t - 0.5 - g, a[3] + t / 2 - 0.835 - g, ft - g]) cube([a[2] - a[0] + t + 0.5 + 2 * g, 1.67 + 2 * g, footing_t() + 2 * g]);
            translate([a[0] - t / 2 - 0.835 - g, a[1] - g, ft - g]) cube([1.67 + 2 * g, a[3] - a[1] + 2 * g, footing_t() + 2 * g]);
            translate([54.14 - g, 63.09 - g, ft - g]) cube([a[2] - 54.14 + 2 * g, 2 / 3 + 2 * g, frost_bottom() - ft + 2 * g]);
        }
        // crawlspace: 18" clear under the floor assembly
        zslab(sill() - 1.5, 1)
            difference() {
                union() for (r = crawl_rooms) translate([r[1], r[2]]) square([r[3] - r[1], r[4] - r[2]]);
                outline2d(w / 2 + g);
                translate([0, 1.25]) square([24.34, 34.21]);           // garage
            }
    }
}

module foundation(part = "all", show_earth = false, crawl_rooms = []) {
    if (part == "all" || part == "basement") basement_concrete();
    if (part == "all" || part == "frost") frost_foundation();
    if (show_earth) earth(crawl_rooms);
}
