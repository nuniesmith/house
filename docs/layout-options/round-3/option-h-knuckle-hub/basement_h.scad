// Basement, Option H "Knuckle hub" (round 3).
// Units: feet. Visualisation only - NOT construction documents.
//
// Under the south wing, hub, mud/pantry and the east half of the quiet wing; 10 ft ceiling
// (floor_to_floor 11.75 ft). The stair foot (y 8.45) and the elevator stop sit under the main-floor
// hub, same x/y. Bedrooms 3 and 4 and the flex room each have an egress window and a well in open
// yard. Mechanical on the west wall (x 25). The ground under the primary suite is not excavated.
use <house_lib_h.scad>

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
    ["LIVING ROOM",     28,   0,     50,   20.4, basement_ceiling(), "living", 0, "", [39, 10, 1.7]],
    // under the hub: stair foot landing, stair, lift stop
    ["",                50,   0,     66,   10.45, basement_ceiling(), "hall"],              // landing at the stair foot
    ["STAIR UP",        50,   10.45, 55.4, 26.4, basement_ceiling(), "stair", 0, "", [52.7, 18.4, 0.8]],
    ["",                55.4, 10.45, 66,   22.4, basement_ceiling(), "hall"],
    ["",                55.4, 22.4,  60,   26.4, basement_ceiling(), "hall"],
    ["",                50,   26.4,  60,   33,   basement_ceiling(), "hall"],
    ["",                50,   33,    53,   36.4, basement_ceiling(), "hall"],
    ["",                60,   22.4,  66,   33,   basement_ceiling(), "hall"],
    [["ELEVATOR", "(FUTURE)"], 53, 33, 59, 40,   basement_ceiling(), "closet", 0, "", [56, 36.5, 0.7]],
    ["STORAGE",         35,   20.4,  50,   36.4, basement_ceiling(), "utility", 0, "", [42.5, 28.4, 1.2]],
    // east: hall, two bedrooms, bath
    ["",                66,   13,    80,   18.4, basement_ceiling(), "hall"],
    ["BEDROOM 3",       66,   0,     78,   13,   basement_ceiling(), "bed", 0, "", [72, 6.5, 1.2]],
    ["BEDROOM 4",       74,   18.4,  88,   29,   basement_ceiling(), "bed", 0, "", [81, 23.7, 1.2]],
    ["BATH",            66,   18.4,  74,   26.4, basement_ceiling(), "bath", 0, "", [70, 22.4, 0.8]],
    ["STORAGE",         66,   26.4,  74,   40.5, basement_ceiling(), "utility", 0, "", [70, 33.5, 0.9]],
    // quiet wing: hall under the bedroom hall, flex, storage, mechanical on the west wall
    ["",                59,   33,    66,   48.4, basement_ceiling(), "hall"],
    [["FLEX /", "CRAFT"], 62.5, 48.4, 74.5, 60.4, basement_ceiling(), "office", 0, "", [68.5, 54.4, 1.0]],
    ["",                38,   40,    59,   46.4, basement_ceiling(), "hall"],
    ["STORAGE",         38,   36.4,  53,   40,   basement_ceiling(), "utility", 0, "", [45.5, 38.2, 0.6]],
    ["UTILITY",         26,   36.4,  38,   48.4, basement_ceiling(), "utility", 0, "", [32, 42.4, 1.1]],
    // window wells (outside the building, clear of the porches and the deck)
    [["WINDOW", "WELL"], 32.5, -3.5, 42,   0,  0, "porch", 0, "", [37, -1.8, 0.5]],
    [["WINDOW", "WELL"], 69,   -3.5, 74.5, 0,  0, "porch", 0, "", [71.8, -1.8, 0.5]],
    [["WINDOW", "WELL"], 88,   21,   91.5, 26, 0, "porch", 0, "", [89.8, 23.5, 0.5, 90]],
    [["WINDOW", "WELL"], 65,   60.4, 71,   64, 0, "porch", 0, "", [68, 62.2, 0.5]],
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [50,    2,    "y", 4.0, "full"],           // hall / living room
    [57,    10.45,"x", 6.0, "full"],           // landing / hall
    [50.2,  26.4, "x", 5.2, "full"],           // stair top side
    [56,    22.4, "x", 3.5, "full"],
    [56,    26.4, "x", 4.0, "full"],
    [61,    22.4, "x", 4.0, "full"],
    [60,    28,   "y", 4.0, "full"],
    [50.2,  33,   "x", 2.7, "full"],
    [59,    34,   "y", 3.0, "door",  1],       // elevator (future)
    [50,    27,   "y", 3.0, "door", -1],       // storage under the library
    [66,    14.5, "y", 3.5, "full"],           // hub to the east hall
    [70,    13,   "x", 3.0, "door",  1],       // bedroom 3
    [77,    18.4, "x", 3.0, "door",  1],       // bedroom 4
    [70,    18.4, "x", 3.0, "door",  1],       // bath
    [70,    26.4, "x", 3.0, "door",  1],       // storage
    [60,    33,   "x", 4.0, "full"],           // hub to the wing hall
    [63,    48.4, "x", 3.0, "door",  1],       // flex
    [59,    41,   "y", 4.0, "full"],
    [38,    42,   "y", 3.0, "door", -1],       // utility
    [45,    40,   "x", 3.0, "door", -1],       // storage
];

// [x, y, axis, width, sill, height]   egress rows: 4.0 x 3.0 ft rough opening, sill 3.5 ft
function base_windows() = [
    [71,    0,    "x", 4.0, 3.5, 3.0],         // bedroom 3 (egress)
    [88,    22,   "y", 4.0, 3.5, 3.0],         // bedroom 4 (egress)
    [66,    60.4, "x", 4.0, 3.5, 3.0],         // flex (egress)
    [34,    0,    "x", 6.0, 3.5, 3.0],         // living room
    [26,    38,   "y", 3.0, 4,   2],           // utility: louvre (combustion air), west wall, open yard
    [26,    43,   "y", 1.5, 4,   2],           // utility: vent chase for the water heater and HRV
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // utility (west wall): air handler, boiler, water heater, HRV, sewage ejector pit
    [26.4,  37,   29.4,  40,    0, 6,    steel],
    [30.2,  36.8, 32.4,  38.8,  0, 3.5,  steel],
    [26.4,  43,   28.6,  45.2,  0, 5.5,  steel, "", "round"],
    [30,    43.4, 32.6,  45.4,  0, 5,    steel],
    [35.4,  44.4, 37.6,  46,    0, 0.05, dark],
    // bath: curbless shower (recess for the engineer), vanity, WC, 1,700 mm circle
    [68.4,  24,   73.6,  26,    0, 0.02, tile],
    [66.4,  21.4, 68,    23,    0, 1.4,  white],
    [66.4,  18.8, 70,    20.2,  0, 3,    counter],
    [67.4,  20.2, 73,    25.8,  0, 0.03, circle_c, "", "round"],
];

function base_furniture() = [
    [30,    4,    38,    7,     0, 2.6,  sofa],
    [30,    7,    33,    12,    0, 2.6,  sofa],
    [45,    3,    47.5,  11,    0, 2,    wood],
    [67,    3,    73.5,  8.5,   0, 2,    bed],
    [80,    21.5, 86.5,  27,    0, 2,    bed],
    [63.5,  58.6, 73.5,  60,    0, 2.5,  wood],
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
