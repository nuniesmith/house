// Main floor - OpenSCAD model of the main level.
// Units: feet. Visualisation only - NOT construction documents.
//
// CONVERTED 2026-10-29 (Jordan) from Architectural Designs plan
// 818030JSS, "New American Ranch Plan with Private Primary Suite -
// 3564 Sq Ft" (4 bd, 4.5 ba, 1 storey, 3-car garage; overall
// 89'-10" wide x 87'-6" deep, 10 ft ceilings, ridge 26'-10").
// See docs/ranch-plan-818030.md. This file REPLACES the previous
// main-floor design on its branch; the previous design remains on
// main / in git history.
//
// Geometry is fitted from the plan's marketing floor-plan image plus
// its printed room dimensions: rooms are wall-centre-line rectangles,
// so they run larger than the printed clear sizes. The marketing
// image is not perfectly to scale, so a few printed dimensions could
// not all be satisfied at once - overall envelope and the labelled
// bedroom/living sizes were given priority. x = east, y = north;
// y = 0 is the garage's south wall, x = 0 the west wall of the
// bedroom wing. Front (entry) faces SOUTH, as drawn.
//
// The plan is drawn slab-on-grade; basement.scad is NOT part of this
// conversion - it still belongs to the previous design and does not
// align with this footprint (docs/ranch-plan-818030.md).
//
// main_level() keeps the old signature so house_combined.scad and
// site.scad still call it; `changes` is accepted and ignored (this
// plan has no as-drawn/proposed variants).

use <house_lib.scad>

changes = true;
show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
audit = false;         // echo the tables for the layout checker

main_level(changes, show_roof, roof_color, roof_opacity, audit);

/* [Hidden] */
counter  = [0.97, 0.97, 0.95];
wood     = [0.55, 0.38, 0.22];
steel    = [0.70, 0.72, 0.74];
dark     = [0.12, 0.12, 0.12];
basin    = [0.62, 0.78, 0.86];
hearth   = [0.35, 0.33, 0.32];
brick    = [0.55, 0.27, 0.20];
white    = [0.97, 0.97, 0.97];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
// Printed sizes in comments are the plan's labelled clear dimensions.
function main_rooms() = [
    // ---- west wing (bedrooms + game room), north -> south
    ["GAME ROOM",       0,     69.5, 17.3,  87.5, 10, "living", 0, "", [8.6, 78.5, 1.6]],   // 16'-3" x 18'-0", vault
    ["BEDROOM 3",       0,     57.5, 12.5,  69.5, 10, "bed"],                 // 12'-0" x 12'-0"
    ["BATH 3",          0,     50.5, 12.5,  57.5, 10, "bath", 0, "", [6.2, 54, 1.2]],
    ["LINEN",           0,     49,   12.5,  50.5, 10, "closet", 0, "", [6.2, 49.7, 0.8]],
    ["",                12.5,  43,   17.3,  69.5, 10, "hall"],                // west corridor
    ["BEDROOM 2",       0,     37,   12.5,  49,   10, "bed"],                 // 12'-0" x 11'-10"
    ["CLOSET",          17.3,  43,   23.5,  49,   10, "closet", 0, "", [20.4, 46, 1]],
    ["BATH 2",          12.5,  37,   19,    43,   10, "bath", 0, "", [15.7, 40, 1.1]],
    ["WC",              19,    37,   23.5,  43,   10, "bath", 0, "", [21.2, 40, 0.9]],     // 6'-0" x 5'-0"
    ["BATH 4",          0,     29,   13,    37,   10, "bath", 0, "", [8, 35.8, 1.2]],      // tub bath + 7'-0" x 5'-7" pwdr end
    ["",                13,    29,   19,    37,   10, "hall"],                // west passage
    ["",                19,    29,   23.6,  37,   10, "living"],              // family west strip (fireplace)
    ["",                17.3,  49,   23.6,  57.5, 10, "hall"],                // landing
    ["",                17.3,  57.5, 23.6,  62,   0,  "porch"],               // back porch west strip
    ["",                10.6,  26.6, 23.6,  29,   10, "hall"],
    ["BEDROOM 4",       10.6,  14.1, 23.6,  26.6, 10, "bed"],                 // 12'-6" x 12'-0"
    // ---- centre: family, entry, kitchen, dining
    ["FAMILY",          23.6,  26,   45,    62,   13, "living"],              // 20'-0" x 22'-0", vault off 18'
    ["ENTRY HALL",      23.6,  18.9, 43.5,  26,   12, "hall", 0, "", [34.5, 22.4, 1.3]],   // 18'-7" x 7'-6"
    ["",                43.5,  14.1, 47.5,  26,   10, "hall"],                // entry alcove
    ["DINING",          45,    47,   58.7,  62,   10, "dining"],              // 12'-1" x 15'-0"
    ["KITCHEN",         45,    29,   56.5,  47,   10, "kitchen", 0, "", [52, 31.8, 1.5]],   // 12'-9" x 18'-0"
    ["",                56.5,  43,   58.7,  47,   10, "kitchen"],
    ["HALL",            45,    26.1, 60,    29,   10, "hall"],
    ["PANTRY",          56.5,  33,   63.5,  43,   10, "utility", 0, "", [60, 38, 1.2]],    // 7'-0" x 10'-0"
    ["",                56.5,  29,   63.5,  33,   10, "hall"],                // pantry passage
    ["OFFICE",          47.5,  14.1, 60,    26.1, 10, "office", 0, "", [55.5, 20, 1.5]],   // 12'-6" x 12'-0"
    // ---- east wing: mud, primary suite
    ["",                60,    26.1, 63.5,  29,   10, "hall"],                // garage vestibule
    ["MUD ROOM",        63.5,  29,   70.7,  43,   10, "utility", 0, "", [67.1, 36, 1.1]],  // 7'-2" x 14'-3"
    ["HALL",            58.7,  43,   70.7,  49,   10, "hall", 0, "", [64, 46, 1]],         // primary entry hall
    ["",                70.7,  34.5, 73.6,  49,   10, "hall"],                // primary hall
    ["PRIMARY SUITE",   58.7,  49,   73.6,  67,   10, "bed"],                 // 14'-6" x 18'-0", vault
    [["PRIMARY", "BATH"], 73.6, 52,  89.83, 72,   10, "bath", 0, "", [81, 55.8, 1.5]],
    ["CLOSET",          73.6,  41.5, 89.83, 52,   10, "closet"],              // 15'-4" x 10'-6", pass-through
    ["UTILITY",         73.6,  34.5, 89.83, 41.5, 10, "utility", 0, "", [79, 38, 1.3]],   // 15'-4" x 7'-0" laundry
    // ---- garage (three plates so the mud room / vestibule sit over its NW)
    ["3 CAR GARAGE",    60,    0,    83,    26.1, 10, "garage", 0, "", [71.5, 12, 1.8]],   // 23'-0" x 33'-3"
    ["",                70.7,  26.1, 83,    34.5, 10, "garage"],
    ["",                63.5,  26.1, 70.7,  29,   10, "garage"],
    // ---- porches (no walls)
    ["FRONT PORCH",     23.6,  10.4, 43.5,  18.9, 0,  "porch", 0, "", [33.5, 14.6, 1.3]],  // 18'-9" x 8'-6"
    ["BACK PORCH",      17.3,  62,   58.7,  79.2, 0,  "porch"],               // 40'-4" x 17'-1"
    [["OUTDOOR", "KITCHEN"], 17.3, 79.2, 26.5, 86.8, 0, "porch", 0, "", [21.9, 83, 1]],
];

// [x, y, axis, width, type, swing, tag] - x,y is the LOW end of the opening
function main_doors() = [
    // ---- exterior
    [32,    18.9, "x", 5,    "double",  1],            // front door
    [28,    62,   "x", 16,   "slider"],                // family -> back porch
    [48,    62,   "x", 6,    "slider"],                // dining -> back porch
    [61,    0,    "x", 7,    "garage"],                // 3-car garage, side entry (south)
    [68,    0,    "x", 7,    "garage"],
    [75.25, 0,    "x", 6.5,  "garage"],
    // ---- centre
    [28.5,  26,   "x", 12,   "full"],                  // entry hall / family
    [43.5,  20,   "y", 4,    "open"],                  // entry hall / alcove
    [47.5,  18.5, "y", 3,    "door",    1],            // alcove -> office
    [48.5,  26.1, "x", 3,    "door",   -1],            // hall -> office
    [45,    50,   "y", 8,    "full"],                  // family / dining
    [45,    32,   "y", 12,   "full"],                  // family / kitchen
    [46,    47,   "x", 8,    "full"],                  // kitchen / dining
    [45,    26.1, "y", 2.8,  "open"],                  // family -> east hall
    [56.5,  36.7, "y", 2.6,  "door",   -1],            // kitchen -> pantry
    [58.7,  33,   "x", 2.6,  "door",    1],            // pantry passage -> pantry
    [57.5,  29,   "x", 2.4,  "full"],                  // east hall / pantry passage
    [60.1,  29,   "x", 2.4,  "full"],                  // vestibule / pantry passage
    [63.5,  29.7, "y", 2.6,  "door",   -1],            // pantry passage -> mud room
    [60,    26.2, "y", 2.6,  "open"],                  // east hall / vestibule
    [60.2,  26.1, "x", 3,    "door",    1],            // vestibule -> garage
    [64.5,  26.1, "x", 5,    "full"],                  // garage plates join
    [72,    26.1, "x", 8,    "full"],
    [65.5,  29,   "x", 3,    "door",    1],            // mud room -> garage
    // ---- primary wing
    [64.25, 43,   "x", 3.5,  "open"],                  // mud room -> primary entry hall
    [58.7,  43.7, "y", 2.6,  "open"],                  // kitchen strip -> primary entry hall
    [70.7,  44.5, "y", 3,    "open"],                  // entry hall / primary hall
    [70.7,  49,   "x", 2.8,  "door",    1],            // primary hall -> primary suite
    [73.6,  56,   "y", 4,    "double", -1],            // primary suite -> primary bath
    [73.6,  44.5, "y", 3,    "open"],                  // primary hall -> closet (pass-through)
    [79.5,  52,   "x", 3,    "door",    1],            // closet -> primary bath
    [73.6,  36.6, "y", 2.8,  "door",    1],            // primary hall -> utility / laundry
    // ---- west wing
    [13.4,  69.5, "x", 3,    "door",    1],            // game room -> west corridor
    [17.3,  58,   "y", 3,    "door",    1],            // corridor -> back porch west strip
    [18,    62,   "x", 4,    "full"],                  // porch strip / back porch
    [12.5,  61.6, "y", 2.8,  "door",    1],            // corridor -> bedroom 3
    [12.5,  51.7, "y", 2.6,  "door",   -1],            // corridor -> bath 3
    [5,     50.5, "x", 2,    "door",    1],            // bath 3 -> linen
    [12.5,  44.6, "y", 2.8,  "door",   -1],            // corridor -> bedroom 2
    [17.3,  44.7, "y", 2.6,  "door",    1],            // corridor -> bedroom 2 closet
    [13.7,  43,   "x", 2.6,  "door",   -1],            // corridor -> bath 2
    [12.5,  38.7, "y", 2.6,  "door",    1],            // bedroom 2 -> bath 2
    [19,    38.4, "y", 2.2,  "door",    1],            // bath 2 -> WC
    [14.2,  37,   "x", 2.6,  "door",   -1],            // west passage -> bath 2
    [13,    31.7, "y", 2.6,  "door",    1],            // west passage -> bath 4
    [16,    29,   "x", 3,    "open"],                  // west hall / west passage
    [19,    31.5, "y", 3,    "open"],                  // west passage / family strip
    [23.6,  31,   "y", 4,    "full"],                  // family strip / family
    [17.3,  50.5, "y", 3,    "open"],                  // corridor / landing
    [23.6,  50.25,"y", 3.5,  "open"],                  // landing / family
    [18.6,  26.6, "x", 2.8,  "door",   -1],            // west hall -> bedroom 4
];

// [x, y, axis, width, sill, height] - x,y is the LOW end of the opening
function main_windows() = [
    [3,     87.5, "x", 4,   2.5, 5],      // game room, north
    [10,    87.5, "x", 4,   2.5, 5],
    [0,     75.5, "y", 5,   2.5, 5],      // game room, west
    [0,     61,   "y", 4,   2.5, 5],      // bedroom 3
    [0,     53,   "y", 2,   4.5, 2.5],    // bath 3
    [0,     40.75,"y", 4.5, 2.5, 5],      // bedroom 2
    [0,     31.75,"y", 2.5, 4.5, 2.5],    // bath 4
    [14.5,  14.1, "x", 5,   2.5, 5],      // bedroom 4, south
    [10.6,  18.25,"y", 3.5, 2.5, 5],      // bedroom 4, west (notch side)
    [26.25, 18.9, "x", 3.5, 2.5, 5],      // entry / family glass, south
    [39.25, 18.9, "x", 3.5, 2.5, 5],
    [51.5,  14.1, "x", 5,   2.5, 5],      // office, south
    [58.7,  60,   "y", 4,   2.5, 5],      // primary suite, west to back porch
    [60,    67,   "x", 4,   2.5, 5],      // primary suite, north
    [68,    67,   "x", 4,   2.5, 5],
    [78.5,  72,   "x", 3,   4.5, 2.5],    // primary bath, north
    [89.83, 59.5, "y", 5,   3.5, 4],      // primary bath, east
    [89.83, 46,   "y", 2,   5,   2],      // closet, east
    [89.83, 36.5, "y", 3,   3.5, 3.5],    // utility, east
    [83,    15.5, "y", 3,   3.5, 3],      // garage, east
];

// porch posts: [x, y, height, tag]
function main_posts() = [
    [23.6, 10.4, 10], [33, 10.4, 10], [43.5, 10.4, 10],          // front porch
    [20, 79.2, 10], [32, 79.2, 10], [44, 79.2, 10], [56, 79.2, 10],  // back porch
    [18.3, 86.3, 10],                                            // outdoor kitchen corner
];

// roof blocks: [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,    14.1, 24,   87.5, 13, 0.45, 1.5],   // west wing
    [23.6, 18.9, 47.5, 62,   15, 0.55, 1.5],   // family (vaulted, tallest)
    [45,   14.1, 63.5, 62,   13, 0.45, 1.5],   // kitchen / dining / office
    [58.7, 29,   89.83, 72,  13, 0.45, 1.5],   // primary wing
    [60,   0,    83,   34.5, 11, 0.40, 1.5],   // garage
    [23.6, 10.4, 43.5, 18.9, 10, 0.25, 1],     // front porch
    [17.3, 62,   58.7, 86.8, 10.5, 0.25, 1],   // back porch + outdoor kitchen
];

module main_level(changes = true, show_roof = true,
                  roof_color = [0.20, 0.38, 0.62], roof_opacity = 1, audit = false) {
    rooms = main_rooms();
    doors = main_doors();
    if (audit) echo(rooms = rooms, doors = doors, windows = main_windows(),
                    fixtures = []);

    draw_level(rooms, doors, main_windows());

    // ---- fixtures (simple blocks, as in the previous model)
    color(counter) {
        translate([49.5, 35, 0]) cube([4, 6, 3]);              // kitchen island
        translate([45.2, 30, 0]) cube([2.3, 15, 3]);           // kitchen west counters
        translate([47.5, 45, 0]) cube([8, 2, 3]);              // kitchen north counter
        translate([74, 52.2, 0]) cube([7, 2, 3]);              // primary bath vanity
        translate([0.2, 30, 0]) cube([5, 2, 3]);               // bath 4 vanity
        translate([13, 37.2, 0]) cube([5.5, 2, 3]);            // bath 2 vanity
    }
    color(basin) {
        translate([86.3, 57.5, 0]) cube([3.2, 6.5, 2]);        // primary soaking tub
        translate([7.5, 30.5, 0]) cube([5, 2.5, 1.8]);         // bath 4 tub
        translate([74, 64, 0]) cube([7.5, 7.5, 0.4]);          // primary shower tray
    }
    color(steel) {
        translate([84.5, 35, 0]) cube([2.2, 2.5, 3.5]);        // washer
        translate([87, 35, 0]) cube([2.2, 2.5, 3.5]);          // dryer
    }
    // fireplaces: family room west wall + back porch west end
    color(hearth) translate([23.6, 40, 0]) cube([1.5, 6, 5]);
    color(hearth) translate([17.3, 57, 0]) cube([2, 5.5, 5]);

    for (p = main_posts()) post(p[0], p[1], p[2]);
    porch_steps(34.5, 10.4, "-y", 8.4);    // front entry
    porch_steps(40,   79.2, "+y", 16);     // back porch to the yard

    if (show_roof) {
        roofs(main_roof(), roof_color, roof_opacity);
        color(brick) translate([23.9, 42.5, 0]) cube([2.2, 2.6, 22]);  // family chimney
    }
}
