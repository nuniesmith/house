// OPTION D - COMPACT L (round 2), basement.
// Units: feet, same plan coordinates as main_floor_d.scad. Visualisation only - NOT
// construction documents. z = 0 is the basement floor; ceiling 10 ft (floor_to_floor
// 11.75 ft, house_lib_d.scad).
//
// Under the heated main floor, same outline (no room outside the main-floor union and no
// room under the garage or porches). No pool, no spa, no theatre tiers, no light wells or
// exit stair from foundation.scad (so that file is not used). Stair foot, elevator stop and
// utility room are drawn where the brief asks:
//   - the straight flight (stair_x 77.8-82.4) meets the main floor at y 27.0 and lands at
//     y 42.75 in STAIR FOOT; the ELEVATOR stop is at x 88.4-94.4, y 21.6-29.0, the same
//     x/y as the main floor's ELEVATOR (FUTURE); both open onto the basement hall.
//   - UTILITY (x 24.4-35, y 9.6-21.6) is on the west end of the wing; its north wall is an
//     exterior wall for flue / combustion-air / intake; the sewage ejector pit is in it.
//   - bedrooms 3 and 4 and the flex room each have an exterior wall, an egress window
//     (rough opening 2.5 wide x 4.0 high, sill 3.0) and a WINDOW WELL room 3.5 ft deep.
// Dropped from the program: theatre (optional) - the footprint left no interior room that
// is not also the stair, hall or bedrooms; nothing else.

use <house_lib_d.scad>

show_stair = true;     // false when the main floor draws it (combined model)
audit = false;         // echo the tables for the layout checker

// no section cut when this file is opened on its own ($cut is a special
// variable, so house_combined.scad's value reaches these modules)
let ($cut = undef) basement_level(show_stair, audit);

/* [Hidden] */
steel  = [0.70, 0.72, 0.74];
counter= [0.97, 0.97, 0.95];
white  = [0.97, 0.97, 0.97];
tile   = [0.55, 0.75, 0.85];
shelf  = [0.62, 0.50, 0.36];
wood   = [0.55, 0.38, 0.22];
dark   = [0.12, 0.12, 0.12];
sofa   = [0.45, 0.50, 0.60];
table  = [0.66, 0.50, 0.34];
bed    = [0.92, 0.88, 0.80];
basin  = [0.62, 0.78, 0.86];
circ   = [0.80, 1.00, 0.90];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function base_rooms() = [
    // ---- west end of the wing: utility and storage
    ["STORAGE",         24.4,  0,     35.0,  9.6,  basement_ceiling(), "closet", 0, "", [29.7, 4.8, 1.0]],
    ["UTILITY",         24.4,  9.6,   35.0,  21.6, basement_ceiling(), "utility", 0, "", [29.7, 15.6, 1.2]],
    // ---- office, gym / music, storage, family room (under kitchen, dining, living)
    [["OFFICE /", "LIBRARY"], 35.0, 0, 51.0, 13.6, basement_ceiling(), "office", 0, "", [43, 6.8, 1.3]],
    ["STORAGE",         35.0,  13.6,  51.0,  21.6, basement_ceiling(), "closet", 0, "", [43, 17.6, 1.1]],
    [["GYM /", "MUSIC"], 51.0, 0,     64.0,  13.6, basement_ceiling(), "rec", 0, "", [57.5, 6.8, 1.2]],
    ["STORAGE",         51.0,  13.6,  64.0,  21.6, basement_ceiling(), "closet", 0, "", [57.5, 17.6, 1.0]],
    ["LIVING ROOM",     64.0,  0,     82.4,  21.6, basement_ceiling(), "living", 0, "", [73.2, 10.8, 1.8]],
    ["HALL",            82.4,  0,     88.4,  21.6, basement_ceiling(), "hall", 0, "", [85.4, 11, 1.2, 90]],
    ["BATH",            88.4,  11.6,  96.4,  21.6, basement_ceiling(), "bath", 0, "", [92.4, 14.4, 1.1]],
    // ---- the hub: hall, stair, elevator stop
    ["HALL",            82.4,  21.6,  88.4,  41.2, basement_ceiling(), "hall", 0, "", [85.4, 31.5, 1.2, 90]],
    ["UNDER STAIR",     77.8,  21.6,  82.4,  27.0, basement_ceiling(), "closet", 0, "", [80.1, 24.3, 0.6]],
    ["STAIR UP",        77.8,  27.0,  82.4,  42.75, basement_ceiling(), "stair", 0, "", [80.1, 34.8, 0.8, 90]],
    ["STAIR FOOT",      77.8,  42.75, 82.4,  49.6, basement_ceiling(), "hall", 0, "", [80.1, 46.2, 0.55]],
    ["HALL",            82.4,  41.2,  92.8,  49.6, basement_ceiling(), "hall", 0, "", [87.6, 45.4, 1.1]],
    [["ELEVATOR", "(FUTURE)"], 88.4, 21.6, 94.4, 29.0, basement_ceiling(), "closet", 0, "", [91.4, 25.3, 0.8]],
    // ---- flex room under bedroom 2, bedrooms 3 and 4, baths
    [["FLEX /", "CRAFT"], 88.4, 29.0, 100.2, 41.2, basement_ceiling(), "bed", 0, "", [94.3, 36.0, 1.2]],
    ["CLOSET",          94.4,  21.6,  100.2, 29.0, basement_ceiling(), "closet", 0, "", [97.3, 25.3, 0.7]],
    ["STORAGE",         74.0,  41.2,  77.8,  49.6, basement_ceiling(), "closet", 0, "", [75.9, 45.4, 0.55, 90]],
    ["BATH",            92.8,  41.2,  100.8, 49.6, basement_ceiling(), "bath", 0, "", [96.8, 45.4, 1.0]],
    ["STORAGE",         100.8, 41.2,  105.0, 49.6, basement_ceiling(), "closet", 0, "", [102.9, 45.4, 0.55, 90]],
    ["",                86.2,  49.6,  92.8,  69.5, basement_ceiling(), "hall"],
    [["BEDROOM", "4"],  74.0,  57.0,  86.2,  69.5, basement_ceiling(), "bed", 0, "", [80.1, 63.2, 1.3]],
    ["CLOSET",          74.0,  49.6,  86.2,  57.0, basement_ceiling(), "closet", 0, "", [80.1, 53.3, 0.8]],
    [["BEDROOM", "3"],  92.8,  57.0,  105.0, 69.5, basement_ceiling(), "bed", 0, "", [98.9, 63.2, 1.3]],
    ["CLOSET",          92.8,  49.6,  105.0, 57.0, basement_ceiling(), "closet", 0, "", [98.9, 53.3, 0.8]],
    // ---- window wells (no walls), 3.5 ft deep in front of each egress window
    [["WINDOW", "WELL"], 70.5, 59.5,  74.0,  65.0, 0, "porch", 0, "", [72.2, 62.2, 0.5, 90]],
    [["WINDOW", "WELL"], 105.0, 59.5, 108.5, 65.0, 0, "porch", 0, "", [106.8, 62.2, 0.5, 90]],
    [["WINDOW", "WELL"], 100.2, 31.5, 103.7, 36.5, 0, "porch", 0, "", [102, 34, 0.5, 90]],
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [82.4,   8.0,   "y", 6.0,  "open"],            // hall to family room
    [82.6,   21.6,  "x", 5.6,  "full"],            // hall to hub hall
    [82.6,   41.2,  "x", 5.6,  "full"],            // hub hall to hall at the stair foot
    [88.4,   12.4,  "y", 3.0,  "door",    1],      // bath
    [88.4,   22.4,  "y", 3.0,  "door",    1],      // elevator stop
    [88.4,   30.5,  "y", 3.0,  "door",    1],      // flex room
    [95.0,   29.0,  "x", 3.0,  "open"],            // flex closet
    [82.4,   22.0,  "y", 3.0,  "door",   -1],      // under-stair storage
    [78.0,   42.75, "x", 4.2,  "full"],            // foot of the stair
    [82.4,   43.5,  "y", 4.0,  "full"],            // stair foot to hall
    [77.8,   44.0,  "y", 2.8,  "door",   -1],      // storage
    [92.8,   43.5,  "y", 3.0,  "door",    1],      // bath to hall
    [101.0,  49.6,  "x", 2.8,  "door",   -1],      // storage off bedroom 3's closet
    [86.7,   49.6,  "x", 5.6,  "full"],            // hall to the bedroom hall
    [86.2,   60.0,  "y", 3.0,  "door",   -1],      // bedroom 4
    [92.8,   60.0,  "y", 3.0,  "door",    1],      // bedroom 3
    [77.0,   57.0,  "x", 4.0,  "open"],            // bedroom 4 closet
    [96.0,   57.0,  "x", 4.0,  "open"],            // bedroom 3 closet
    [64.0,   4.0,   "y", 3.0,  "door",   -1],      // family room to gym / music
    [51.0,   4.0,   "y", 3.0,  "door",   -1],      // gym / music to office
    [57.0,   13.6,  "x", 3.0,  "door",    1],      // gym storage
    [41.0,   13.6,  "x", 3.0,  "door",    1],      // office storage
    [35.0,   14.0,  "y", 3.0,  "door",   -1],      // storage to utility
    [35.0,   3.0,   "y", 3.0,  "door",   -1],      // office to storage
];

// [x, y, axis, width, sill, height]
function base_windows() = [
    [74.0,   61.0,  "y", 2.5, 3.0, 4.0],      // bedroom 4 egress (west)
    [78.0,   69.5,  "x", 3.0, 4.0, 3.0],      // bedroom 4, north
    [105.0,  61.0,  "y", 2.5, 3.0, 4.0],      // bedroom 3 egress (east)
    [97.0,   69.5,  "x", 3.0, 4.0, 3.0],      // bedroom 3, north
    [100.2,  33.0,  "y", 2.5, 3.0, 4.0],      // flex room egress (east)
    [68.0,   0,     "x", 8.0, 4.0, 2.5],      // family room
    [56.0,   0,     "x", 5.0, 4.0, 2.5],      // gym / music
    [40.0,   0,     "x", 5.0, 4.0, 2.5],      // office
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // utility: air handler, boiler, water heater, HRV, water treatment, sewage ejector pit
    [25.0,   17.0,  28.0,   20.0,  0, 6,    steel],     // air handler
    [28.6,   19.4,  30.8,   21.2,  0, 3.5,  steel],     // boiler
    [31.0,   19.0,  33.0,   21.0,  0, 5.5,  steel, "", "round"],   // water heater
    [33.0,   10.5,  34.6,   12.5,  5.5, 7,  steel],     // HRV
    [25.0,   13.0,  27.5,   15.5,  0, 4,    steel],     // water treatment
    [25.0,   10.2,  27.0,   12.2,  0, 0.3,  dark],      // sewage ejector pit (lid)
    // baths: stacked under the main floor's guest bath
    [88.6,   19.0,  92.6,   21.2,  0, 3,    counter],
    [94.4,   19.0,  96.0,   21.0,  0, 1.4,  white],
    [93.0,   12.0,  96.2,   16.5,  0, 0.02, tile],
    [89.4,   15.4,  95.0,   19.0,  0, 0.03, circ],      // 1,700 mm circle
    [93.0,   42.4,  96.0,   45.4,  0, 0.02, tile],      // bath at the stair foot: shower
    [97.4,   42.0,  100.6,  44.0,  0, 3,    counter],
    [98.4,   46.2,  100.0,  48.2,  0, 1.4,  white],
    [93.6,   46.0,  98.0,   49.4,  0, 0.03, circ],
    // storage shelving
    [35.2,   19.8,  50.8,   21.4,  0, 7,    shelf],
    [51.2,   19.8,  63.8,   21.4,  0, 7,    shelf],
    [24.6,   0.2,   34.8,   1.8,   0, 7,    shelf],
];

// furniture
function base_furniture() = [
    [66.0,   5.0,   69.0,   16.0,  0, 2.6,  sofa],      // sectional
    [66.0,   16.0,  72.0,   19.0,  0, 2.6,  sofa],
    [79.4,   6.0,   81.8,   15.0,  0, 3,    wood],      // TV unit
    [52.0,   2.0,   56.0,   8.0,   0, 2.5,  dark],      // gym equipment / piano
    [36.0,   8.0,   42.0,   10.0,  0, 3,    wood],      // desk
    [92.0,   34.0,  97.0,   39.0,  0, 2,    bed],       // flex room: Murphy bed footprint
    [75.0,   60.0,  80.0,   66.7,  0, 2,    bed],       // bedroom 4
    [96.5,   60.0,  101.5,  66.7,  0, 2,    bed],       // bedroom 3
];

module basement_level(show_stair = true, audit = false, show_furniture = true) {
    rooms = base_rooms();
    doors = base_doors();
    windows = base_windows();
    if (audit) echo(rooms = rooms, doors = doors, windows = windows,
                    fixtures = concat(base_fixtures(), base_furniture()));

    draw_level(rooms, doors, windows);
    fixtures(base_fixtures());
    if (show_furniture) fixtures(base_furniture());
    if (show_stair) main_stair(floor_to_floor());
}
