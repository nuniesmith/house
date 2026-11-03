// Site - OpenSCAD model of the whole property: the house first, then the
// shop. Units: feet. Visualisation only - NOT construction documents.
//
// Coordinates are the house model's (x = east, y = north; main floor
// at z = 0, grade 2 ft below it at z = -2, basement floor
// floor_to_floor() below the main floor: 13.75 ft, for 12 ft ceilings).
// Land is not yet chosen: positions are RELATIVE to the house, not a
// survey. The road is assumed along the south side.
//
// Phasing (Nov 3, 2026): the house is built first, on its own, with
// the bare minimum to live in it. The shop is a separate, later project
// with its own permits.
//   phase = "house" - the house and what it needs:
//     - the driveway from the road (south) up the west side to the
//       garage's west-facing doors, and the front loop round the garden;
//     - power, natural gas (if the road has it) and fibre (if an ISP
//       on Alberta SuperNet reaches the road) in one service corridor
//       from the road along the west side of the drive, into the west
//       side of the house by the basement UTILITY room;
//     - a propane tank as the gas option if there is no natural gas,
//       and a Starlink dish as the internet option;
//     - the water well on the west side, near the UTILITY room;
//     - the septic tank and its treatment field on the east side, more
//       than 30 m (100 ft) from the well;
//     - the future shop's spot, dashed, kept clear.
//   phase = "full" - adds the shop (shop.scad) with its drives, aprons
//     and tree belt, and the buried service lines from the house to it.
//
// The utility tunnel of earlier versions is gone: the basement's utility
// room moved to the west side, so the shop will get buried service lines
// in a trench instead, dug when the shop is built.
//
// Shop v4 (2026-11-02): the two truck bays and the wash bay are
// pull-through, with a wrap-round drive (north leg and a 60 ft deep east
// apron). See docs/shop/Shop-Base-Plan.md.

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>
use <foundation.scad>
use <shop.scad>

phase = "house";       // [house, full]
show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue (house)
show_ground = true;

/* [Hidden] */
grade_z = -2;

// Shop placement (future): behind the house. Its west wall aligns with the
// garage's west wall (x = 0); its south wall is at y = 130, so the shop
// sits at x 0..100, y 130..230, with ~60 ft of back yard between the
// house's north porches and the shop.
function shop_origin() = [0, 130];

// Services, house coordinates [x, y]
function well_xy()        = [-70, 90];                  // west, near the UTILITY room
function propane_xy()     = [-61, 39];                  // tank centre, if there is no natural gas
function starlink_xy()    = [-6, 76];                   // dish on a short mast, clear sky to the north
function septic_tank()    = [146, 8, 158, 14];          // [x0, y0, x1, y1]
function septic_field()   = [175, -40, 235, 15];        // treatment field, sized by the PSDS designer
function road_y()         = -100;                       // the road's north edge

module flat_text(s, at, size = 4, col = [0.2, 0.2, 0.2], z = 0.25) {
    color(col) translate([at[0], at[1], grade_z + z])
        linear_extrude(0.1) text(s, size = size, halign = "center", valign = "center");
}

// a dashed line on the ground through points pts (axis-aligned or not)
module dashed(pts, col, w = 0.9, dash = 5, gap = 3) {
    color(col)
        for (i = [0 : len(pts) - 2]) {
            a = pts[i]; b = pts[i + 1];
            L = norm(b - a);
            n = max(1, floor(L / (dash + gap)));
            for (k = [0 : n - 1]) {
                t0 = k * (dash + gap) / L; t1 = min(1, (k * (dash + gap) + dash) / L);
                p = a + (b - a) * t0; q = a + (b - a) * t1;
                hull() {
                    translate([p[0], p[1], grade_z + 0.15]) cylinder(d = w, h = 0.1, $fn = 8);
                    translate([q[0], q[1], grade_z + 0.15]) cylinder(d = w, h = 0.1, $fn = 8);
                }
            }
        }
}

module dashed_rect(r, col, w = 1.0) {
    dashed([[r[0], r[1]], [r[2], r[1]], [r[2], r[3]], [r[0], r[3]], [r[0], r[1]]], col, w, 8, 4);
}

module road() {
    color([0.42, 0.42, 0.42]) translate([-180, road_y() - 24, grade_z + 0.04]) cube([440, 24, 0.12]);
    flat_text("ROAD (SOUTH) - TO BE CONFIRMED", [170, road_y() - 12], 4, [0.95, 0.95, 0.95]);
}

module drives() {
    color([0.78, 0.78, 0.74]) {
        // the driveway from the road up the west side to the garage doors
        translate([-32, road_y(), grade_z + 0.05]) cube([30, 42 - road_y(), 0.12]);
        // front loop driveway (ring) south of the house, round the garden
        translate([25, -72, grade_z + 0.05]) cube([105, 14, 0.12]);    // south leg
        translate([25, -28, grade_z + 0.05]) cube([105, 14, 0.12]);    // north leg
        translate([25, -72, grade_z + 0.05]) cube([14, 58, 0.12]);     // west leg
        translate([116, -72, grade_z + 0.05]) cube([14, 58, 0.12]);    // east leg
        translate([-2, -50, grade_z + 0.05]) cube([27, 14, 0.12]);     // connector from the drive
    }
    flat_text("DRIVEWAY", [-17, -80], 4);
}

module shop_drives() {   // phase "full": on to the shop, its aprons and the wrap-round
    color([0.78, 0.78, 0.74]) {
        translate([-32, 42, grade_z + 0.05]) cube([30, 188, 0.12]);    // the drive continues north
        translate([-72, 130, grade_z + 0.06]) cube([70, 100, 0.12]);   // shop apron (west front)
        // the wrap-round: north of the shop, then the east apron in front
        // of the pull-through doors (corners sized for a tractor-trailer's
        // ~50 ft outside turning radius when it is laid out)
        translate([-72, 230, grade_z + 0.06]) cube([232, 32, 0.12]);   // north leg
        translate([100, 126, grade_z + 0.06]) cube([60, 136, 0.12]);   // east apron
    }
}

module garden() {
    // garden island inside the front loop
    color([0.45, 0.65, 0.38]) translate([45, -52, grade_z + 0.08]) cube([65, 16, 0.1]);
    color([0.30, 0.52, 0.28])
        for (p = [[55, -44], [70, -41], [85, -45], [98, -42], [62, -47], [92, -47]])
            translate([p[0], p[1], grade_z + 2]) sphere(r = 3, $fn = 12);
    flat_text("GARDEN", [77.5, -65], 4, [0.2, 0.4, 0.2]);
}

module tree(x, y) {
    color([0.45, 0.32, 0.20]) translate([x, y, grade_z]) cylinder(r = 0.5, h = 5, $fn = 8);
    color([0.32, 0.55, 0.30]) translate([x, y, grade_z + 9]) sphere(r = 6, $fn = 12);
}

module tree_belt() {   // with the shop: outside the wrap-round drive on the north and east
    for (x = [-58, -40, -22, -4, 14, 32, 50, 68, 86, 104, 122, 140, 158]) tree(x, 276);   // north edge
    for (y = [134, 152, 170, 188, 206, 224, 242, 260]) tree(174, y);                       // east edge
    for (x = [8, 26, 44, 62, 80, 98]) tree(x, 116);                                         // south edge
    flat_text("TREE BELT - 3 SIDES", [53, 290], 4, [0.2, 0.4, 0.2]);
    flat_text("EAST APRON", [130, 180], 4);
    flat_text("WRAP-ROUND DRIVE", [50, 246], 4);
}

// power, gas and fibre from the road, up the west side of the drive, then
// east into the house's west side by the UTILITY room; water from the well
module services(full = false) {
    power = [0.90, 0.45, 0.10]; gas = [0.95, 0.80, 0.10]; fibre = [0.55, 0.30, 0.75];
    water = [0.20, 0.50, 0.90]; sewer = [0.45, 0.30, 0.20];
    dashed([[-41, road_y()], [-41, 44], [7.27, 44]], fibre);
    dashed([[-44, road_y()], [-44, 46], [7.27, 46]], power);
    dashed([[-47, road_y()], [-47, 48], [7.27, 48]], gas);
    dashed([[well_xy()[0], well_xy()[1]], [well_xy()[0], 51], [7.27, 51]], water);
    // propane: a 1000 US gal tank on its pad, if there is no natural gas
    p = propane_xy();
    color([0.85, 0.85, 0.82]) translate([p[0] - 8, p[1] - 3, grade_z]) cube([16, 6, 0.3]);
    color([0.96, 0.96, 0.94]) translate([p[0] - 7, p[1], grade_z + 2.2]) rotate([0, 90, 0])
        cylinder(d = 3.4, h = 14, $fn = 24);
    dashed([[p[0] + 7, p[1]], [-47, p[1]]], gas);
    // meters on the west wall
    color([0.25, 0.25, 0.25]) for (y = [45, 47.5]) translate([6.6, y - 0.6, grade_z + 3]) cube([0.6, 1.2, 1.6]);
    // the well
    w = well_xy();
    color([0.39, 0.70, 0.93]) translate([w[0], w[1], grade_z]) cylinder(r = 2, h = 1.6, $fn = 24);
    // Starlink, as the internet option (or backup)
    s = starlink_xy();
    color([0.3, 0.3, 0.3]) translate([s[0], s[1], grade_z]) cylinder(d = 0.4, h = 8, $fn = 8);
    color([0.92, 0.92, 0.92]) translate([s[0], s[1], grade_z + 8]) rotate([-20, 0, 0]) cylinder(d = 2.0, h = 0.25, $fn = 24);
    dashed([[s[0], s[1]], [s[0], 60], [7.27, 60]], fibre, 0.6);
    // septic: building sewer out of the master wing's east side to the
    // tank, then on to the treatment field
    t = septic_tank(); f = septic_field();
    dashed([[128.13, 11], [t[0], 11]], sewer);
    color([0.50, 0.55, 0.48]) translate([t[0], t[1], grade_z]) cube([t[2] - t[0], t[3] - t[1], 1]);
    dashed([[t[2], 11], [f[0], 11]], sewer);
    color([0.70, 0.82, 0.62]) translate([f[0], f[1], grade_z + 0.02]) cube([f[2] - f[0], f[3] - f[1], 0.08]);
    color([0.62, 0.74, 0.55]) for (y = [f[1] + 8 : 10 : f[3] - 4])
        translate([f[0] + 4, y, grade_z + 0.08]) cube([f[2] - f[0] - 8, 1.2, 0.06]);   // laterals
    if (full)   // buried service lines to the shop, dug with the shop
        dashed([[-50, 53], [-50, 126], [80, 126], [80, 130]], [0.85, 0.25, 0.25]);
    // labels
    flat_text("POWER, GAS, FIBRE", [-76, -40], 3.4, power);
    flat_text("FROM THE ROAD", [-76, -45], 3.4, power);
    flat_text("WELL", [w[0], w[1] + 6], 4, [0.1, 0.35, 0.7]);
    flat_text("PROPANE TANK", [p[0] - 6, p[1] - 7], 3.4, [0.55, 0.45, 0.05]);
    flat_text("(IF NO NATURAL GAS)", [p[0] - 6, p[1] - 11.5], 3.0, [0.55, 0.45, 0.05]);
    flat_text("STARLINK", [s[0] - 12, s[1] + 4], 3.2, fibre);
    flat_text("SEPTIC TANK", [(t[0] + t[2]) / 2, t[1] - 5], 3.6, [0.2, 0.4, 0.2]);
    flat_text("SEPTIC FIELD", [(f[0] + f[2]) / 2, (f[1] + f[3]) / 2 + 3], 4, [0.2, 0.4, 0.2]);
    flat_text("(TREATMENT FIELD)", [(f[0] + f[2]) / 2, (f[1] + f[3]) / 2 - 3], 3.2, [0.2, 0.4, 0.2]);
    if (full) {
        flat_text("SERVICE LINES TO", [-82, 112], 3.4, [0.75, 0.15, 0.15]);
        flat_text("THE SHOP (BURIED)", [-82, 107.5], 3.4, [0.75, 0.15, 0.15]);
    }
}

module future_shop() {   // phase "house": keep its spot clear
    dashed_rect([shop_origin()[0], shop_origin()[1], shop_origin()[0] + 100, shop_origin()[1] + 100],
                [0.35, 0.35, 0.35], 1.2);
    flat_text("FUTURE SHOP", [50, 186], 6, [0.35, 0.35, 0.35]);
    flat_text("SEPARATE PROJECT AND PERMITS", [50, 176], 4, [0.35, 0.35, 0.35]);
}

module ground() {
    color([0.56, 0.68, 0.45]) difference() {
        translate([-180, road_y(), grade_z - 0.1]) cube([440, 400, 0.1]);
        // the basement exit stair and the light wells stay open
        translate([0, 0, grade_z - 1]) linear_extrude(2) basement_openings2d();
    }
}

// ($cut: no section cut - house_lib's paint() reads it)
let ($cut = undef) {
    full = phase == "full";
    if (show_ground) ground();
    road();
    drives();
    garden();
    services(full);
    translate([0, 0, -floor_to_floor()]) basement_level(show_stair = false);
    main_level(show_roof, roof_color, roof_opacity);
    if (full) {
        shop_drives();
        tree_belt();
        translate([shop_origin()[0], shop_origin()[1], grade_z]) shop_level(show_roof);
    } else {
        future_shop();
    }
}
