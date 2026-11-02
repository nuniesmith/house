// Site - OpenSCAD model of the whole property: house, shop and the
// utility tunnel between them. Units: feet. Visualisation only -
// NOT construction documents.
//
// Coordinates are the house model's (x = east, y = north; main floor
// at z = 0, grade 2 ft below it at z = -2, basement floor
// floor_to_floor() = 11.75 ft below the main floor). Land is not yet
// chosen: positions are RELATIVE to the house, not a survey.
//
// Shop v3 (Jordan, 2026-10-29): the shop moves BEHIND the house, to
// the north side, rotated 90 degrees right from v2 - front faces
// WEST again, bays run east-west, Bay 1 (utilities) southernmost,
// closest to the house. A shared driveway runs up the WEST side of
// the house (past the garage's west doors) to the shop's west apron.
// At the front (south) of the house a loop driveway circles a GARDEN
// island. Trees belt the shop on its north, east and south edges
// (the west edge is the working front). The tunnel leaves the south
// side of Bay 1 and runs due SOUTH into the basement UTILITIES room
// through its north foundation wall - UTILITIES is on the north side
// of the basement, so the landing is direct: no other basement room
// is touched. See docs/shop/Shop-Base-Plan.md.
//
// NOTE - house redesign of November 2026: the new basement has no
// UTILITIES room on its north side. Its UTILITY room (14'6" x 7') is on
// the west side, behind the storage room, and on x = 80 the basement's
// north wall is now the POOL ROOM's. The tunnel below is drawn to that
// wall so the conflict shows; its landing needs re-planning (see
// docs/house/Redesign-and-Spec-2026-11-02.md).

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>
use <foundation.scad>
use <shop.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue (house)
show_ground = true;
show_tunnel = true;

/* [Hidden] */
grade_z = -2;

// Shop placement: behind the house. Its west wall aligns with the
// garage's west wall (x = 0); its south wall is at y = 130, so the
// shop sits at x 0..100, y 130..230, with ~62 ft of back yard between
// the house's north porches and the shop.
function shop_origin() = [0, 130];
// Tunnel centreline: x = 80, the centre of Bay 1's portal room
// (shop-local x 72..88, centred 80 - the shop sits at x 0..100, so
// local and site x agree); it was also the centre of the old basement's
// UTILITIES room. It ends at the basement's north wall on that line
// (the outside face of the pool room's ICF wall, y = 52.76 + 0.55).
function tunnel_x() = 80;
function tunnel_end_y() = 52.76 + icf_wall_t() / 2;

module flat_text(s, at, size = 4, col = [0.2, 0.2, 0.2]) {
    color(col) translate([at[0], at[1], grade_z + 0.25])
        linear_extrude(0.1) text(s, size = size, halign = "center", valign = "center");
}

module drives() {
    color([0.78, 0.78, 0.74]) {
        // shared driveway up the west side: front loop -> garage -> shop
        translate([-32, -70, grade_z + 0.05]) cube([30, 300, 0.12]);
        // shop apron (west front)
        translate([-72, 130, grade_z + 0.06]) cube([70, 100, 0.12]);
        // front loop driveway (ring) south of the house
        translate([25, -72, grade_z + 0.05]) cube([105, 14, 0.12]);    // south leg
        translate([25, -28, grade_z + 0.05]) cube([105, 14, 0.12]);    // north leg
        translate([25, -72, grade_z + 0.05]) cube([14, 58, 0.12]);     // west leg
        translate([116, -72, grade_z + 0.05]) cube([14, 58, 0.12]);    // east leg
        // connector from the west drive into the loop
        translate([-2, -50, grade_z + 0.05]) cube([27, 14, 0.12]);
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

module tree_belt() {
    for (x = [8, 26, 44, 62, 80, 98]) tree(x, 244);              // north edge
    for (y = [140, 158, 176, 194, 212, 228]) tree(114, y);       // east edge
    for (x = [8, 26, 44, 62, 98]) tree(x, 116);                  // south edge (gap at the tunnel, x 72..88)
    flat_text("TREE BELT - 3 SIDES", [53, 258], 4, [0.2, 0.4, 0.2]);
}

module tunnel() {
    // Floor at basement level, 8 ft wide, 7.5 ft clear, from Bay 1's
    // south wall (y = 130) to the basement's north wall (~77 ft).
    zf = -floor_to_floor();
    color([0.62, 0.62, 0.60])
        translate([tunnel_x() - 4, tunnel_end_y(), zf]) cube([8, 130 - tunnel_end_y(), 7.5]);
    // Entry frame where it meets the basement wall
    color([1.0, 0.55, 0.15, 0.55])
        translate([tunnel_x() - 4.5, tunnel_end_y() - 1.5, zf]) cube([9, 3, 9]);
}

module ground() {
    color([0.56, 0.68, 0.45]) difference() {
        translate([-175, -100, grade_z - 0.1]) cube([370, 370, 0.1]);
        // a slot over the tunnel so the tunnel reads from above
        if (show_tunnel) translate([tunnel_x() - 5.5, tunnel_end_y() - 2, grade_z - 1]) cube([11, 134 - tunnel_end_y(), 2]);
    }
}

module well_and_septic() {
    color([0.39, 0.70, 0.93]) translate([140, 110, grade_z]) cylinder(r = 2, h = 1.2, $fn = 24);
    flat_text("WELL", [140, 101], 4, [0.1, 0.35, 0.7]);
    color([0.50, 0.55, 0.48]) translate([-100, 205, grade_z]) cube([22, 15, 1]);
    flat_text("SEPTIC TANK", [-89, 197], 4, [0.2, 0.4, 0.2]);
    color([0.70, 0.82, 0.62]) translate([-165, 150, grade_z + 0.02]) cube([60, 55, 0.08]);
    flat_text("FIELD", [-135, 177], 4, [0.2, 0.4, 0.2]);
}

// ($cut: no section cut - house_lib's paint() reads it)
let ($cut = undef) {
    if (show_ground) ground();
    drives();
    garden();
    tree_belt();
    well_and_septic();
    translate([0, 0, -floor_to_floor()]) basement_level(show_stair = false);
    main_level(show_roof, roof_color, roof_opacity);
    translate([shop_origin()[0], shop_origin()[1], grade_z]) shop_level(show_roof);
    if (show_tunnel) {
        tunnel();
        flat_text("UTILITY TUNNEL", [57, 95], 4, [0.75, 0.15, 0.15]);
    }
}
