// Site - OpenSCAD model of the whole property: house, shop and the
// utility tunnel between them. Units: feet. Visualisation only -
// NOT construction documents.
//
// Coordinates are the house model's (x = east, y = north; main floor
// at z = 0, grade 2 ft below it at z = -2, basement floor 13 ft below
// the main floor). Land is not yet chosen: positions are RELATIVE to
// the house, not a survey.
//
// Shop v2 (Jordan, 2026-10-29): the shop is rotated 90 degrees from
// the first sketch - bays run north-south, front faces SOUTH, and
// Bay 1 (utilities) is the easternmost bay, closest to the house.
// The tunnel leaves the SIDE (east wall) of Bay 1 at its portal room
// and runs due east on the centreline of the basement UTILITIES room
// (basement coords y = 45..60, the north side of the basement), into a
// proposed utility receiving room carved from the west end of the
// theater; services continue along the theater's north wall in a
// ceiling bulkhead into UTILITIES itself. See
// docs/shop/Shop-Base-Plan.md for the full plan and decisions.

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>
use <shop.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue (house)
show_ground = true;
show_tunnel = true;

/* [Hidden] */
off = basement_offset();
grade_z = -2;

// Shop placement: 100 ft clear between the garage's west wall (x = 0)
// and the shop's east wall; the shop's local (0,0) is its south-west
// corner, so it sits at x -200..-100, y 2.5..102.5.
function shop_origin() = [-200, 2.5];
// Tunnel centreline: Bay 1's portal room is at shop-local y 42..58
// (centre 50) -> site y = 2.5 + 50 = 52.5, which is also the centre
// of the basement UTILITIES room (45..60). One straight line.
function tunnel_y() = 52.5;

module flat_text(s, at, size = 4, col = [0.2, 0.2, 0.2]) {
    color(col) translate([at[0], at[1], grade_z + 0.25])
        linear_extrude(0.1) text(s, size = size, halign = "center", valign = "center");
}

module drives() {
    color([0.78, 0.78, 0.74]) {
        translate([-200, -57.5, grade_z + 0.06]) cube([100, 60, 0.12]);   // shop apron (south)
        translate([-200, -15, grade_z + 0.05]) cube([220, 17.5, 0.12]);   // south spine: house -> shop
        translate([-100, 2.5, grade_z + 0.05]) cube([100, 42, 0.12]);     // court between shop and garage
    }
}

module tunnel() {
    // Floor at basement level (z = -13), 8 ft wide, 7.5 ft clear.
    // Shop east wall x = -100 to the basement west wall (site x = off[0]).
    color([0.62, 0.62, 0.60])
        translate([-100, tunnel_y() - 4, -13]) cube([100 + off[0], 8, 7.5]);
    // Portal frame at the shop end
    color([0.45, 0.45, 0.45])
        translate([-101, tunnel_y() - 5, -13]) cube([2, 10, 9]);
}

module proposed_basement_link() {
    // Proposed utility receiving room carved from the theater's west
    // end (basement coords (0,44)-(12,60) -> site via off), drawn
    // translucent orange: it is a CHANGE to the basement, not built.
    color([1.0, 0.55, 0.15, 0.45])
        translate([off[0], off[1] + 44, -13]) cube([12, 16, 12]);
    // Services bulkhead along the theater's north wall at ceiling
    // level, receiving room -> UTILITIES west wall (basement x = 30)
    color([1.0, 0.55, 0.15, 0.6])
        translate([off[0] + 12, off[1] + 58.4, -3.4]) cube([18, 1.4, 1.2]);
}

module ground() {
    ex = exit_areaway();
    color([0.56, 0.68, 0.45]) difference() {
        translate([-320, -95, grade_z - 0.1]) cube([500, 290, 0.1]);
        // exit-stair areaway stays open (as in house_combined)
        translate([ex[0] + off[0], ex[1] + off[1], grade_z - 1]) cube([ex[2] - ex[0], ex[3] - ex[1], 2]);
        // a slot over the tunnel so the tunnel reads from above
        if (show_tunnel) translate([-102, tunnel_y() - 5.5, grade_z - 1]) cube([104 + off[0], 11, 2]);
    }
}

module well_and_septic() {
    color([0.39, 0.70, 0.93]) translate([-228, -38, grade_z]) cylinder(r = 2, h = 1.2, $fn = 24);
    flat_text("WELL", [-228, -47], 4, [0.1, 0.35, 0.7]);
    color([0.50, 0.55, 0.48]) translate([-248, 118, grade_z]) cube([34, 18, 1]);
    flat_text("SEPTIC TANK", [-231, 109], 4, [0.2, 0.4, 0.2]);
    color([0.70, 0.82, 0.62]) translate([-255, 142, grade_z + 0.02]) cube([70, 30, 0.08]);
    flat_text("FIELD", [-220, 157], 4, [0.2, 0.4, 0.2]);
}

if (show_ground) ground();
drives();
well_and_septic();
translate([off[0], off[1], -floor_to_floor()]) basement_level();
translate([0, 0, 0]) main_level(true, show_roof, roof_color, roof_opacity);
translate([shop_origin()[0], shop_origin()[1], grade_z]) shop_level(show_roof);
if (show_tunnel) {
    tunnel();
    proposed_basement_link();
    flat_text("UTILITY TUNNEL", [-35, tunnel_y() + 9], 4, [0.75, 0.15, 0.15]);
}
