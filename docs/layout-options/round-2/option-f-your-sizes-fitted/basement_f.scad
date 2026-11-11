// Basement, Option E "Linear ranch" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// Same outline as the main-floor compact L, 10 ft ceiling (floor_to_floor 11.75 ft).
// No pool, spa, theatre tiers, exit stair or light wells. The straight stair comes
// down from the junction hall (top nosing y 20.2) running south to its foot at
// y 4.45 under the foyer, landing at x 86.6..92; the future elevator is stacked at
// x 92..98.4, y 25.8..33.2 as on the main floor. Utility room on the west wall
// (x 16.6) under the office, north of the garage (x 0..23, y 0..24.8), so its louvres
// face open yard. The office is upstairs.
use <house_lib_f.scad>

show_stair = true;     // false when the main floor draws it (combined model)
audit = false;         // echo the tables for the layout checker

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
seat   = [0.25, 0.25, 0.28];
screen = [0.96, 0.96, 0.96];
carpet = [0.66, 0.36, 0.36];
circle_c = [0.95, 0.75, 0.75];   // 1,700 mm turning circle

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function base_rooms() = [
    // west block: utility on the west wall under the office, storage
    ["UTILITY",         16.6, 24.8, 26.6, 41.2, basement_ceiling(), "utility", 0, "", [21.6, 33, 1.3]],
    ["STORAGE",         26.6, 24.8, 32,   41.2, basement_ceiling(), "closet", 0, "", [29.3, 33, 0.9, 90]],
    ["",                23,   14.4, 32.4, 24.8, basement_ceiling(), "hall"],
    ["STORAGE",         23,   0,    32.4, 14.4, basement_ceiling(), "closet", 0, "", [27.7, 7, 1.0]],
    // south row (south wall = exterior, egress windows)
    ["BEDROOM 3",       32.4, 0,    44.8, 14.4, basement_ceiling(), "bed", 0, "", [38.6, 11, 1.2]],
    [["JACK &", "JILL BATH"], 44.8, 0, 53.2, 14.4, basement_ceiling(), "bath", 0, "", [49, 11, 0.9]],
    ["BEDROOM 4",       53.2, 0,    65.6, 14.4, basement_ceiling(), "bed", 0, "", [59.4, 11, 1.2]],
    ["LIVING ROOM",     65.6, 0,    86.6, 20.4, basement_ceiling(), "living", 0, "", [76, 15, 1.7]],
    ["",                32.4, 14.4, 65.6, 22.4, basement_ceiling(), "hall"],              // basement hall
    // junction: stair foot, elevator
    ["",                86.6, 0,    92,   4.45, basement_ceiling(), "hall"],              // landing at the stair foot
    ["STAIR UP",        86.6, 4.45, 92,   20.4, basement_ceiling(), "stair", 0, "", [89.3, 12, 0.8]],
    ["",                92,   0,    98.4, 20.4, basement_ceiling(), "hall"],
    ["",                86.6, 20.4, 98.4, 25.8, basement_ceiling(), "hall"],
    ["CLOSET",          86.6, 25.8, 92,   33.2, basement_ceiling(), "closet", 0, "", [89.3, 29.5, 0.7]],
    [["ELEVATOR", "(FUTURE)"], 92, 25.8, 98.4, 33.2, basement_ceiling(), "closet", 0, "", [95.2, 29.5, 0.7]],
    // quiet wing: flex, gym, future theatre
    ["",                98.4, 5,    104.8,25.8, basement_ceiling(), "hall"],
    [["FLEX /", "CRAFT"], 104.8, 12.4, 114.6, 25.8, basement_ceiling(), "office", 0, "", [109.7, 19, 1.0]],
    [["GYM /", "MUSIC"], 114.6, 6,  127,  25.8, basement_ceiling(), "rec", 0, "", [120.8, 16, 1.2]],
    [["THEATRE", "(FUTURE)"], 98.4, 25.8, 127, 44.6, basement_ceiling(), "rec", 0, "", [112.7, 35, 1.3]],
    [["FUTURE", "ROOM"], 99.6,  44.6, 127, 67,   basement_ceiling(), "rec", 0, "", [113.3, 56, 1.3]],
    // window wells (outside the building, clear of the porches)
    [["WINDOW", "WELL"], 33.5, -3.5, 40,   0,  0, "porch", 0, "", [36.7, -1.8, 0.5]],
    [["WINDOW", "WELL"], 61.5, -3.5, 67,   0,  0, "porch", 0, "", [64.2, -1.8, 0.5]],
    [["WINDOW", "WELL"], 104.8, 8.4, 111.5, 12.4, 0, "porch", 0, "", [108.2, 10.4, 0.5]],
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [32.4,  16,   "y", 4.0, "full"],
    [23.8,  24.8, "x", 2.8, "door", -1],      // utility
    [28,    24.8, "x", 3.0, "door",  1],      // storage
    [24,    14.4, "x", 3.0, "door", -1],      // storage (south)
    [34,    14.4, "x", 3.0, "door", -1],      // bedroom 3
    [45.5,  14.4, "x", 3.0, "door", -1],      // bath
    [44.8,  5,    "y", 3.0, "door",  1],      // bath to bedroom 3
    [53.2,  5,    "y", 3.0, "door",  1],      // bath to bedroom 4
    [55,    14.4, "x", 3.0, "door", -1],      // bedroom 4
    [65.6,  16,   "y", 4.0, "full"],          // hall / living room
    [86.6,  0.6,  "y", 3.0, "door", -1],      // living room to the stair-foot landing
    [92,    1,    "y", 3.0, "full"],          // landing / hall
    [92,    6,    "y", 3.6, "full"],          // stair foot side opening
    [93,    20.4, "x", 4.5, "full"],
    [94,    25.8, "x", 3.0, "door", -1],      // elevator (future)
    [87.5,  25.8, "x", 3.0, "door",  1],      // closet
    [98.4,  8,    "y", 4.0, "full"],
    [98.4,  21,   "y", 4.0, "full"],
    [104.8, 17,   "y", 3.0, "door",  1],      // flex
    [114.6, 16,   "y", 3.0, "door",  1],      // gym
    [100,   25.8, "x", 3.0, "door", -1],      // theatre
    [105,   44.6, "x", 3.0, "door", -1],      // future room
];

// [x, y, axis, width, sill, height]   egress rows: 4.0 x 3.0 ft rough opening, sill 3.5 ft
function base_windows() = [
    [35,    0,    "x", 4.0, 3.5, 3.0],       // bedroom 3 (egress)
    [62,    0,    "x", 3.6, 3.5, 3.0],       // bedroom 4 (egress)
    [106,   12.4, "x", 4.0, 3.5, 3.0],       // flex (egress)
    [72,    0,    "x", 8.0, 3.5, 3.0],       // living room
    [16.6,  28,   "y", 3.0, 4,   2],         // utility: louvre (combustion air), west wall, open yard
    [16.6,  32,   "y", 1.5, 4,   2],         // utility: vent chase for the water heater and HRV
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // utility (west wall): air handler, boiler, water heater, HRV, sewage ejector pit
    [17,    25.6, 20,    28.6, 0, 6,    steel],
    [20.8,  25.4, 23,    27.4, 0, 3.5,  steel],
    [17,    30.4, 19.2,  32.6, 0, 5.5,  steel, "", "round"],
    [20.4,  30.4, 23,    32.4, 0, 5,    steel],
    [23.8,  38.4, 26,    40,   0, 0.05, dark],
    // jack-and-jill bath: curbless shower (recess for the engineer), vanity, WC
    [45.2,  8.4,  51.4,  13.8, 0, 0.02, tile],
    [45.2,  0.6,  47,    2.4,  0, 1.4,  white],
    [48,    0.5,  52.4,  2.0,  0, 3,    counter],
    [45.6,  3.2,  51.2,  8.2,  0, 0.03, circle_c, "", "round"],
];

function base_furniture() = [
    [68,    4,    76,    7,    0, 2.6,  sofa],
    [68,    7,    71,    12,   0, 2.6,  sofa],
    [82,    3,    84.5,  11,   0, 2,    wood],
    [35,    3,    41.5,  8.5,  0, 2,    bed],
    [58,    3,    64.5,  8.5,  0, 2,    bed],
    [106,   14,   112,   16,   0, 2.5,  wood],
    [115,   8,    125,   10,   0, 2.5,  dark],
    [100,   36,   124,   38,   0, 6,    screen],
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
