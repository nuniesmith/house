// Basement, Option E "Linear ranch" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// Same outline as the main-floor bar (x 24..100.5, y 0..39 less the kitchen/pantry
// notch on the north and the bedroom 2 notch on the east), 10 ft ceiling
// (floor_to_floor 11.75 ft). No pool, spa, theatre tiers, exit stair or light
// wells. The straight stair arrives from the main floor at x 59.3 (top nosing)
// and its foot is at x 43.55 (y 20.4..24.6) at a landing hall; the future
// elevator is stacked at x 47.8..53.8, y 32.4..39 as on the main floor.
// Utility on the west wall at y 26.8..36.8, north of the garage (x 0..24,
// y 0..30), so its louvres face open yard, not the garage.
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
    ["STORAGE",         24,   0,    34.4, 26.8, basement_ceiling(), "closet", 0, "", [29.2, 13, 1.4, 90]],
    ["UTILITY",         24,   26.8, 34.4, 36.8, basement_ceiling(), "utility", 0, "", [29.2, 31.5, 1.3]],
    ["",                34.4, 20.4, 43.55,30,   basement_ceiling(), "hall"],
    ["",                34.4, 30,   38.6, 36.8, basement_ceiling(), "hall"],              // landing at the stair foot
    ["OFFICE",          38.6, 30,   47.8, 36.8, basement_ceiling(), "office", 0, "", [41, 33.5, 1.3]],
    ["STAIR UP",        43.55,20.4, 59.5, 24.6, basement_ceiling(), "stair", 0, "", [51.5, 22.5, 0.8]],
    ["",                43.55,24.6, 64.7, 30,   basement_ceiling(), "hall"],              // hall under the gallery
    ["",                47.8, 30,   53.8, 32.4, basement_ceiling(), "hall"],
    [["ELEVATOR", "(FUTURE)"], 47.8, 32.4, 53.8, 39, basement_ceiling(), "closet", 0, "", [50.8, 35.7, 0.7]],
    ["STORAGE",         53.8, 30,   64.7, 39,   basement_ceiling(), "closet", 0, "", [59.2, 34.5, 1.2]],
    // south row (south wall = exterior, egress windows)
    ["BEDROOM 3",       34.4, 0,    46.8, 14,   basement_ceiling(), "bed", 0, "", [40.6, 11, 1.2]],
    [["JACK &", "JILL BATH"], 46.8, 0, 55.2, 14, basement_ceiling(), "bath", 0, "", [51, 11, 0.9]],
    ["BEDROOM 4",       55.2, 0,    67.6, 14,   basement_ceiling(), "bed", 0, "", [61.4, 11, 1.2]],
    [["FLEX /", "CRAFT"], 67.6, 0,  79.6, 14,   basement_ceiling(), "office", 0, "", [73.6, 11, 1.0]],
    ["LIVING ROOM",     79.6, 0,    98.9, 19.6, basement_ceiling(), "living", 0, "", [89, 15, 1.7]],
    ["",                34.4, 14,   79.6, 20.4, basement_ceiling(), "hall"],              // basement hall
    ["",                64.7, 20.4, 79.6, 24.6, basement_ceiling(), "hall"],
    ["THEATRE",         64.7, 24.6, 79.6, 39,   basement_ceiling(), "rec", 0, "", [72, 33, 1.3]],
    [["GYM /", "MUSIC"], 79.6, 19.6, 100.5, 39, basement_ceiling(), "rec", 0, "", [90, 33, 1.3]],
    // window wells (outside the bar, clear of the porches)
    [["WINDOW", "WELL"], 38.5, -3.5, 45,  0,    0, "porch", 0, "", [41.7, -1.8, 0.5]],
    [["WINDOW", "WELL"], 58,   -3.5, 64.5, 0,   0, "porch", 0, "", [61.2, -1.8, 0.5]],
    [["WINDOW", "WELL"], 75.4, -3.5, 81.9, 0,   0, "porch", 0, "", [78.6, -1.8, 0.5]],
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [34.4,  22,   "y", 3.0, "door",  1],      // storage (landing side)
    [34.8,  30,   "x", 3.6, "full"],
    [34.4,  32,   "y", 3.0, "door",  1],      // utility
    [38.6,  32,   "y", 3.0, "door",  1],      // office
    [34.4,  15,   "y", 3.0, "full"],          // hall opening west
    [43.55, 20.8, "y", 3.6, "full"],          // landing / stair foot
    [43.55, 25,   "y", 4.5, "full"],          // landing / hall
    [38,    20.4, "x", 5.0, "full"],          // landing / hall (north side of the basement hall)
    [48.2,  30,   "x", 5.2, "full"],
    [49.5,  32.4, "x", 3.0, "door", -1],      // elevator (future)
    [55,    30,   "x", 3.0, "door", -1],      // storage
    [64.7,  26,   "y", 3.0, "door",  1],      // theatre
    [65,    20.4, "x", 5.0, "full"],
    [65,    24.6, "x", 3.0, "door", -1],      // theatre from the east hall
    [36,    14,   "x", 3.0, "door", -1],      // bedroom 3
    [48.8,  14,   "x", 3.0, "door", -1],      // bath
    [46.8,  5,    "y", 3.0, "door",  1],      // bath to bedroom 3
    [55.2,  5,    "y", 3.0, "door",  1],      // bath to bedroom 4
    [57,    14,   "x", 3.0, "door", -1],      // bedroom 4
    [69,    14,   "x", 3.0, "door", -1],      // flex
    [79.6,  15,   "y", 4.0, "full"],          // hall / living room
    [85,    19.6, "x", 3.0, "door",  1],      // living room to gym
];

// [x, y, axis, width, sill, height]   egress rows: 4.0 x 3.0 ft rough opening, sill 3.5 ft
function base_windows() = [
    [39.5,  0,    "x", 4.0, 3.5, 3.0],       // bedroom 3 (egress)
    [59,    0,    "x", 4.0, 3.5, 3.0],       // bedroom 4 (egress)
    [76.0,  0,    "x", 3.6, 3.5, 3.0],       // flex (egress)
    [84,    0,    "x", 8.0, 3.5, 3.0],       // living room
    [24,    32,   "y", 3.0, 4,   2],         // utility: louvre (combustion air), open yard side
    [24,    35,   "y", 1.5, 4,   2],         // utility: vent chase for the water heater and HRV
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // utility (west wall): air handler, boiler, water heater, HRV, sewage ejector pit
    [24.6,  27.6, 27.6,  30.6, 0, 6,    steel],
    [28.4,  27.4, 30.6,  29.4, 0, 3.5,  steel],
    [24.6,  31.8, 26.8,  34,   0, 5.5,  steel, "", "round"],
    [28,    31.8, 30.6,  33.8, 0, 5,    steel],
    [31.8,  34.4, 34,    36.4, 0, 0.05, dark],
    [25,    1,    26.5,  25.8, 0, 7,    shelf],
    // jack-and-jill bath: curbless shower (recess for the engineer), vanity, WC
    [47.2,  8.4,  53.4,  13.6, 0, 0.02, tile],
    [47.2,  0.6,  49,    2.4,  0, 1.4,  white],
    [50.2,  0.5,  54.6,  2.0,  0, 3,    counter],
    [47.6,  3.2,  53.2,  8.2,  0, 0.03, circle_c, "", "round"],
];

function base_furniture() = [
    [82,    4,    90,    7,    0, 2.6,  sofa],
    [82,    7,    85,    12,   0, 2.6,  sofa],
    [94,    3,    96.5,  11,   0, 2,    wood],
    [38.2,  3,    44.7,  8.5,  0, 2,    bed],
    [58.8,  3,    65.3,  8.5,  0, 2,    bed],
    [68,    1,    77,    3.6,  0, 2.5,  wood],
    [41,    34.2, 47,    36.3, 0, 2.5,  wood],
    [66,    37,   78,    38.6, 0, 6,    screen],
    [87,    37,   99,    38.6, 0, 2.5,  dark],
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
