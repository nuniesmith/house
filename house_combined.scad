// house_combined.scad - both levels of the house in one OpenSCAD model.
// Units: feet. Visualisation only - NOT construction documents.
//
// The levels come from main_floor.scad and basement.scad (use<> pulls in
// their modules only), so there is a single copy of each floor's data.
// Alignment: house_lib's basement_offset() puts the basement's south
// wall under the front wall line (y = 0) and its east wall under the
// master bath's east wall; the basement floor is floor_to_floor()
// (13 ft) below the main floor.

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>

mode = "assembled";    // [assembled, exploded, basement_only, main_only]
stair = "proposed";    // [proposed, as_drawn]
changes = true;        // the proposed changes (Kayla's review)
show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
explode_gap = 14;
show_ground = true;    // grade, 2 ft below the main floor (assembled view)

off = basement_offset();
basement_z = (mode == "exploded") ? -floor_to_floor() - explode_gap : -floor_to_floor();
main_z = (mode == "exploded") ? explode_gap / 2 : 0;

if (mode != "main_only")
    translate([off[0], off[1], basement_z]) basement_level(stair);
if (mode != "basement_only")
    translate([0, 0, main_z]) main_level(stair, changes, show_roof, roof_color, roof_opacity);

// The sketch's 100' x 60' basement runs past the house walls in places
// (see REVIEW.md); the ground hides those parts the way the yard would,
// leaving the exit-stair areaway open.
ex = exit_areaway();
if (mode == "assembled" && show_ground)
    color([0.56, 0.68, 0.45]) difference() {
        translate([-20, -35, -2.1]) cube([180, 125, 0.1]);
        translate([ex[0] + off[0], ex[1] + off[1], -3]) cube([ex[2] - ex[0], ex[3] - ex[1], 2]);
    }
