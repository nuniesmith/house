// Basement - OpenSCAD model of the lower level.
// Units: feet. Visualisation only - NOT construction documents.
//
// Follows the hand-drawn 100' x 60' sketch: home theater (NW), pool +
// hot tub (SW), utilities (N), open rec room with the bar / coffee /
// sink counter, a 10' x 30' room (NE) and a 40' x 20' room (SE), both
// unlabelled in the sketch, and the exit stair outside the east wall.
// Positions come from the photo with its perspective corrected; the
// labelled dimensions win where the drawing disagrees with them.
// x = east, y = north in basement coordinates; house_lib's
// basement_offset() maps them onto the main floor.
//
// stair = "proposed": the stair comes down from the main floor's
// former bar into the rec room (it lines up with main_floor.scad).
// "as_drawn": the sketch's straight stair beside the utilities, which
// lands under the office / master suite upstairs (see REVIEW.md).

use <house_lib.scad>

stair = "proposed";    // [proposed, as_drawn]
audit = false;         // echo the tables for the layout checker

basement_level(stair, audit);

/* [Hidden] */
water  = [0.39, 0.70, 0.93];
spa    = [0.51, 0.90, 0.85];
seat   = [0.29, 0.29, 0.29];
riser  = [0.40, 0.33, 0.30];
fabric = [0.45, 0.10, 0.12];
screen = [0.96, 0.96, 0.96];
wood   = [0.55, 0.38, 0.22];

// exit stair areaway outside the east foundation wall [x0, y0, x1, y1]
function exit_areaway() = [100, 12, 105, 50];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function base_rooms() = [
    [["HOME", "THEATER"], 0,  35, 30,  60, 12, "living", 0, "", [15, 53.6, 1.6]],
    [["POOL /", "HOT TUB"], 0, 0, 25,  35, 12, "pool",   0, "", [20.5, 29, 1.1]],
    [["POOL", "EQUIP."],  25, 0,  30,  31, 12, "utility"],
    ["",                  25, 31, 30,  35, 0,  "rec"],      // vestibule at the theater / pool doors
    ["UTILITIES",         30, 45, 70,  60, 12, "utility"],
    ["STORAGE",           70, 50, 100, 60, 12, "closet"],   // unlabelled in the sketch
    ["FLEX ROOM",         60, 0,  100, 20, 12, "living"],   // unlabelled in the sketch
    ["REC ROOM",          30, 20, 100, 45, 0,  "rec",    0, "", [42, 38, 2.2]],
    ["",                  30, 0,  60,  20, 0,  "rec"],
    ["",                  70, 45, 100, 50, 0,  "rec"],
    ["STAIR UP",          52.2, 21, 67.1, 31.4, 12, "stairwell", 0, "stair_new", [59.6, 33.3, 1.4]],
    ["STAIR UP",          70, 45, 90.7, 50, 12, "stairwell", 0, "stair_old", [80.3, 42.6, 1.4]],
    concat([["EXIT", "STAIR"]], exit_areaway(), [11, "stair"]),   // areaway outside the foundation
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [26,   35,   "x", 3,   "door",  1],                 // theater
    [25,   31.5, "y", 3,   "door", -1],                 // pool room
    [26,   31,   "x", 3,   "door", -1],                 // pool equipment
    [30,   31.3, "y", 3.4, "full"],                     // vestibule / rec room
    [30.3, 20,   "x", 29.4, "full"],                    // rec room is one open floor:
    [70.3, 45,   "x", 29.4, "full", 1, "stair_new"],    //   its three plates join here
    [91,   45,   "x", 8.7, "full", 1, "stair_old"],
    [64,   45,   "x", 3,   "door",  1],                 // utilities
    [95,   50,   "x", 3,   "door",  1],                 // storage
    [88,   20,   "x", 3,   "door", -1],                 // flex room (no door in the sketch)
    [100,  22,   "y", 3,   "door",  1],                 // exit door, opens outward
    [52.2, 21.2, "y", 4.4, "full",  1, "stair_new"],    // foot of the stair
    [90.7, 45.3, "y", 4.4, "full",  1, "stair_old"],
];

// [x0, y0, x1, y1, z0, z1, colour]
function base_fixtures() = [
    [5,    3,    17,   23,   -0.3, 0.02, water],        // pool
    [1.5,  36,   28.5, 40.5, 0,    1.33, riser],        // theater risers, rows 2 + 3
    [1.5,  41,   28.5, 45.5, 0,    0.67, riser],
    [0.4,  57.6, 29.6, 58.2, 0,    11,   fabric],       // false wall at the screen end
    [3,    57.4, 27,   57.6, 2,    10.5, screen],
    [77.2, 29,   81.7, 39,   0,    3.5,  wood],         // bar / coffee / sink
];

module basement_level(stair = "proposed", audit = false) {
    tags = [stair == "proposed" ? "stair_new" : "stair_old"];
    rooms = active(base_rooms(), 8, tags);
    doors = active(base_doors(), 6, tags);
    if (audit) echo(rooms = rooms, doors = doors, windows = []);

    // ICF foundation walls up to the main floor; passed into draw_level
    // so the exit door is cut through them too
    draw_level(rooms, doors, []) foundation_walls(0, 0, 100, 60, floor_to_floor());
    foundation_slab(0, 0, 100, 60);

    fixtures(base_fixtures());
    color(spa) translate([11, 28.5, 0]) cylinder(r = 3.5, h = 1.5, $fn = 48);   // hot tub
    // theater seating: three rows of four facing the screen (north),
    // the back rows on the risers
    color(seat)
        for (row = [[47, 0], [42, 0.67], [37, 1.33]], x = [6, 11, 16, 21])
            translate([x, row[0], row[1]]) cube([3, 2.5, 2.6]);

    // stairs: up to the main floor, and the exit stair up to grade
    // (2 ft below the main floor) along the outside of the east wall
    off = basement_offset();
    if (stair == "proposed")
        translate([-off[0], -off[1], 0]) bar_stair(floor_to_floor(), upper = false);
    else
        flight(70.5, 45.5, 90.7, 49.5, "+x", floor_to_floor(), 0, 21, 0);
    flight(100.5, 27, 104.5, 44, "-y", floor_to_floor() - 2, 0, 18, 0);
    landing(100.5, 44, 104.5, 50, 0, floor_to_floor() - 2);
}
