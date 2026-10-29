// Basement - OpenSCAD model of the lower level.
// Units: feet. Visualisation only - NOT construction documents.
//
// Follows the hand-drawn 100' x 60' sketch: home theater (NW), pool +
// hot tub (SW) with a pool bath (WC, shower, change bench) between the
// pool and the rec room, utilities (N), an open rec room that doubles as the
// library (bookshelves on every wall, reading seats, a bar / coffee
// station with sink and dishwasher in the middle), a 10' x 30' storage
// room (NE), the 40' x 20' music room (SE) and the exit stair outside
// the east wall.
// Positions come from the photo with its perspective corrected; the
// labelled dimensions win where the drawing disagrees with them.
// x = east, y = north in basement coordinates; house_lib's
// basement_offset() maps them onto the main floor.
//
// The main stair comes down from the main floor's former bar into the
// rec room (it lines up with main_floor.scad). The exit stair climbs
// south to grade along the master bath's east wall, clear of the side
// porch.

use <house_lib.scad>

audit = false;         // echo the tables for the layout checker

basement_level(audit);

/* [Hidden] */
water  = [0.39, 0.70, 0.93];
spa    = [0.51, 0.90, 0.85];
seat   = [0.29, 0.29, 0.29];
riser  = [0.40, 0.33, 0.30];
fabric = [0.45, 0.10, 0.12];
screen = [0.96, 0.96, 0.96];
shelf  = [0.42, 0.28, 0.17];
sofa   = [0.35, 0.42, 0.55];
steel  = [0.70, 0.72, 0.74];
counter = [0.97, 0.97, 0.95];
wood   = [0.55, 0.38, 0.22];
tile   = [0.55, 0.75, 0.85];

// exit stair areaway outside the east foundation wall [x0, y0, x1, y1]
function exit_areaway() = [100, 7, 105, 30.5];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function base_rooms() = [
    [["HOME", "THEATER"], 0,  35, 30,  60, 12, "living", 0, "", [15, 53.6, 1.6]],
    [["POOL /", "HOT TUB"], 0, 0, 25,  35, 12, "pool",   0, "", [20.5, 29, 1.1]],
    [["POOL", "EQUIP."],  25, 0,  30,  19, 12, "utility"],
    [["POOL", "BATH"],    25, 19, 30,  31, 12, "bath", 0, "", [27.1, 25.4, 0.7]],  // WC, shower, change bench
    ["",                  25, 31, 30,  35, 0,  "rec"],      // vestibule at the theater / pool doors
    ["UTILITIES",         30, 45, 70,  60, 12, "utility"],
    ["STORAGE",           70, 50, 100, 60, 12, "closet"],   // unlabelled in the sketch
    ["MUSIC ROOM",        60, 0,  100, 20, 12, "living"],
    [["REC ROOM /", "LIBRARY"], 30, 20, 100, 45, 0, "rec", 0, "", [42, 38, 1.8]],
    ["",                  30, 0,  60,  20, 0,  "rec"],
    ["",                  70, 45, 100, 50, 0,  "rec"],
    ["STAIR UP",          52.2, 21, 67.1, 31.4, 12, "stairwell", 0, "", [59.6, 33.3, 1.4]],
    concat([["EXIT", "STAIR"]], exit_areaway(), [11, "stair"]),   // areaway outside the foundation
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [26,   35,   "x", 3,   "door",  1],                 // theater
    [25,   31.5, "y", 3,   "door", -1],                 // pool room
    [27.2, 31,   "x", 2.6, "door", -1],                 // pool bath, from the rec room side
    [25,   23.6, "y", 2.8, "door",  1],                 // pool bath, from the pool
    [25,   8,    "y", 3,   "door",  1],                 // pool equipment, from the pool room
    [30,   31.3, "y", 3.4, "full"],                     // vestibule / rec room
    [30.3, 20,   "x", 29.4, "full"],                    // rec room is one open floor:
    [70.3, 45,   "x", 29.4, "full"],                    //   its three plates join here
    [64,   45,   "x", 3,   "door",  1],                 // utilities
    [95,   50,   "x", 3,   "door",  1],                 // storage
    [88,   20,   "x", 3,   "door", -1],                 // music room (no door in the sketch)
    [100,  26.8, "y", 3,   "door",  1],                 // exit door, opens outward
    [52.2, 21.2, "y", 4.4, "full"],                     // foot of the stair
];

// [x0, y0, x1, y1, z0, z1, colour, tag]
function base_fixtures() = [
    [5,    3,    17,   23,   -0.3, 0.02, water],        // pool
    // pool bath: shower, sink, WC, change bench
    [25.2, 19.2, 29.8, 23.2, 0,    0.15, tile],
    [25.2, 26.8, 26.6, 28.4, 0,    2.9,  counter],
    [25.3, 29,   26.9, 30.8, 0,    1.4,  counter],
    [28.4, 23.6, 29.8, 27.6, 0,    1.5,  wood],
    [1.5,  36,   28.5, 40.5, 0,    1.33, riser],        // theater risers, rows 2 + 3
    [1.5,  41,   28.5, 45.5, 0,    0.67, riser],
    [0.4,  57.6, 29.6, 58.2, 0,    11,   fabric],       // false wall at the screen end
    [3,    57.4, 27,   57.6, 2,    10.5, screen],
    // bar / coffee station in the middle of the rec room: small sink and dishwasher
    [72,   31,   77.2, 34.4, 0,    2.95, wood],
    [77.2, 31,   79.2, 34.4, 0,    2.95, steel],        // dishwasher
    [79.2, 31,   80,   34.4, 0,    2.95, wood],
    [71.9, 30.9, 80.1, 34.5, 2.95, 3.1,  counter],
    [73.5, 32,   75,   33.4, 3.1,  3.15, water],        // sink
    // library: bookshelves on every rec-room wall, 7 ft high
    [31.4, 0.6,  58.8, 1.6,  0,    7,    shelf],        // south wall
    [58.8, 1.6,  59.8, 19.6, 0,    7,    shelf],        // music room
    [67.6, 20.2, 87.4, 21.2, 0,    7,    shelf],
    [91.6, 20.2, 99.3, 21.2, 0,    7,    shelf],
    [98.3, 30.4, 99.3, 49.6, 0,    7,    shelf],        // east wall
    [70.6, 48.8, 94.6, 49.8, 0,    7,    shelf],        // storage room wall
    [31.4, 43.8, 63.6, 44.8, 0,    7,    shelf],        // utilities
    [30.2, 35.4, 31.2, 43.8, 0,    7,    shelf],        // theater
    [30.2, 1.6,  31.2, 30.6, 0,    7,    shelf],        // pool equipment
    // reading seating
    [38,   3,    46,   6,    0,    2.6,  sofa],
    [37,   10,   40,   13,   0,    2.6,  sofa],
    [44,   10,   47,   13,   0,    2.6,  sofa],
    [86,   40.5, 94,   43.5, 0,    2.6,  sofa],
    [88,   34,   91,   37,   0,    2.6,  sofa],
];

module basement_level(audit = false) {
    rooms = base_rooms();
    doors = base_doors();
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
    // (2 ft below the main floor) along the outside of the east wall:
    // landing at the door, 18 risers climbing south, landing at grade
    off = basement_offset();
    translate([-off[0], -off[1], 0]) bar_stair(floor_to_floor(), upper = false);
    flight(100.5, 11, 104.5, 26.3, "+y", floor_to_floor() - 2, 0, 18, 0);
    landing(100.5, 7, 104.5, 11, 0, floor_to_floor() - 2);
}
