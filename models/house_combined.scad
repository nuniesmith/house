// house_combined.scad - both levels and the foundation in one model.
// Units: feet. Visualisation only - NOT construction documents.
//
// The levels come from main_floor.scad, basement.scad and foundation.scad
// (use<> pulls in their modules only), so there is a single copy of each
// table. Both levels share the main floor's plan coordinates; the
// basement floor is floor_to_floor() below the main floor.
//
// mode:
//   assembled      the house on its lot, grade 2 ft below the main floor
//   exploded       the main floor lifted off the basement
//   basement_only, main_only
//   foundation     the concrete alone: basement walls and footings, slab,
//                  theatre tiers, pool + spa shell, frost walls, piers
//   section        a vertical cut through everything, earth included;
//                  `section` picks the cut (see below), or set cut_axis
//                  and cut_at directly with section = "custom"; cut faces
//                  are drawn darker than the surfaces beyond (house_lib's
//                  paint() does the cutting, so every part keeps its colour)

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>
use <foundation.scad>

mode = "assembled";    // [assembled, exploded, basement_only, main_only, foundation, section]
section = "A";         // [A, B, C, D, E, custom]
cut_axis = "y";        // [x, y] - custom section: keep x >= cut_at or y >= cut_at
cut_at = 40;
show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
show_furniture = true;
explode_gap = 16;
show_ground = true;    // the lawn at grade (assembled view)

// A: east-west through the stair, the theatre's tiers and the pool
// B: north-south along the stair
// C: north-south through the theatre
// D: north-south through the pool, the spa and its spillway
// E: east-west along the basement exit stair, looking north
function section_cut(s) =
    s == "A" ? ["y", 40] :
    s == "B" ? ["x", 45] :
    s == "C" ? ["x", 62] :
    s == "D" ? ["x", 86] :
    s == "E" ? ["y", (exit_areaway()[1] + exit_areaway()[3]) / 2] : [cut_axis, cut_at];

$cut = mode == "section" ? section_cut(section) : undef;

basement_z = mode == "exploded" ? -floor_to_floor() - explode_gap : -floor_to_floor();
main_z = mode == "exploded" ? explode_gap / 2 : 0;

// the main floor's heated rooms, for the crawlspace under them
crawl = [for (r = main_rooms()) if (r[6] != "porch" && r[6] != "garage") r];

if (mode == "foundation") {
    foundation("all");
} else {
    // the stair belongs to the main floor, except when the floors are apart
    stair_below = mode == "exploded" || mode == "basement_only";
    if (mode != "main_only")
        translate([0, 0, basement_z])
            basement_level(show_stair = stair_below, show_furniture = show_furniture);
    if (mode != "basement_only")
        translate([0, 0, main_z])
            main_level(show_roof && mode != "section", roof_color, roof_opacity, show_furniture,
                       show_stair = !stair_below);
    if (mode == "assembled" || mode == "section")
        foundation("frost", show_earth = mode == "section", crawl_rooms = crawl);
    if (mode == "assembled" && show_ground)   // the lawn, open over the exit stair and the light wells
        paint([0.56, 0.68, 0.45]) translate([0, 0, grade() - 0.1]) linear_extrude(0.1)
            difference() { translate([-25, -45]) square([190, 140]); basement_openings2d(); }
}
