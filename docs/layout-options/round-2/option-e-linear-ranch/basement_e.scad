// Basement, Option E "Linear ranch" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// Same outline as the main-floor bar (x 24..96.5, y 0..39, wall centre lines),
// 10 ft ceiling (floor_to_floor 11.75 ft). No pool, spa, theatre tiers, exit
// stair or light wells from foundation.scad. The straight stair comes down
// the north wall from x 53.3 (top nosing) to x 37.55 (foot) into a landing
// hall; the future elevator is stacked at x 42..48, y 27..34.4 as on the main
// floor. Utility room on the west wall. Basement bedrooms and the flex room
// have egress windows into window wells (porch-kind rooms, outside the bar).

use <house_lib_e.scad>

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
    // ---- west block: utility on the west wall, storage, stair landing
    ["STORAGE",         24,   0,    37.5, 19.5, basement_ceiling(), "closet", 0, "", [30.7, 10, 1.4]],
    ["UTILITY",         24,   19.5, 32,   39,   basement_ceiling(), "utility", 0, "", [28.2, 29, 1.3, 90]],
    ["",                32,   19.5, 37.5, 39,   basement_ceiling(), "hall"],              // landing at the stair foot
    // ---- hub
    ["",                37.5, 19.5, 53.5, 27,   basement_ceiling(), "hall"],              // hall, elevator approach
    ["STORAGE",         37.5, 27,   42,   34.4, basement_ceiling(), "closet", 0, "", [39.75, 30.7, 0.55, 90]],
    [["ELEVATOR", "(FUTURE)"], 42, 27, 48, 34.4, basement_ceiling(), "closet", 0, "", [45, 30.7, 0.7]],
    ["STORAGE",         48,   27,   53.5, 34.4, basement_ceiling(), "closet", 0, "", [50.75, 30.7, 0.55, 90]],
    ["STAIR UP",        37.5, 34.4, 53.5, 39,   basement_ceiling(), "stair", 0, "", [45.5, 36.7, 0.8]],
    ["",                53.5, 19.5, 96.5, 25,   basement_ceiling(), "hall"],              // east hall
    // ---- north row (north wall = exterior, egress windows)
    ["BEDROOM 3",       53.5, 25,   65.5, 39,   basement_ceiling(), "bed", 0, "", [59.5, 36, 1.2]],
    [["JACK &", "JILL BATH"], 65.5, 25, 73.5, 39, basement_ceiling(), "bath", 0, "", [69.5, 36, 0.9]],
    ["BEDROOM 4",       73.5, 25,   85.5, 39,   basement_ceiling(), "bed", 0, "", [79.5, 36, 1.2]],
    [["FLEX /", "CRAFT"], 85.5, 25, 96.5, 39,   basement_ceiling(), "office", 0, "", [91, 36, 1.0]],
    // ---- south row
    ["OFFICE",          37.5, 0,    49.5, 19.5, basement_ceiling(), "office", 0, "", [43.5, 15, 1.3]],
    ["LIVING ROOM",     49.5, 0,    69.5, 19.5, basement_ceiling(), "living", 0, "", [59.5, 15, 1.7]],
    ["THEATRE",         69.5, 0,    83.5, 19.5, basement_ceiling(), "rec", 0, "", [76.5, 15, 1.3]],
    [["GYM /", "MUSIC"], 83.5, 0,   96.5, 19.5, basement_ceiling(), "rec", 0, "", [90, 15, 1.2]],
    // ---- window wells (outside the bar)
    [["WINDOW", "WELL"], 55,  39,   61.5, 42.5, 0, "porch", 0, "", [58.2, 40.7, 0.5]],
    [["WINDOW", "WELL"], 75,  39,   81.5, 42.5, 0, "porch", 0, "", [78.2, 40.7, 0.5]],
    [["WINDOW", "WELL"], 88,  39,   94.5, 42.5, 0, "porch", 0, "", [91.2, 40.7, 0.5]],
    [["WINDOW", "WELL"], 40,  -3.5, 46.5, 0,    0, "porch", 0, "", [43.2, -1.8, 0.5]],
    [["WINDOW", "WELL"], 54,  -3.5, 64.5, 0,    0, "porch", 0, "", [59.2, -1.8, 0.5]],
];

// [x, y, axis, width, type, swing, tag]
function base_doors() = [
    [33.5,  19.5, "x", 3.0, "door", -1],     // storage to landing
    [32,    22,   "y", 3.0, "door", -1],     // storage (west) to landing
    [37.5,  20,   "y", 6.5, "full"],         // landing / hall
    [37.5,  34.7, "y", 4.3, "full"],         // foot of the stair
    [38,    27,   "x", 3.0, "door", -1],     // storage
    [42.5,  27,   "x", 3.0, "door", -1],     // elevator (future)
    [49,    27,   "x", 3.0, "door", -1],     // storage
    [53.5,  19.8, "y", 5.0, "full"],         // hall / east hall
    [38.5,  19.5, "x", 3.0, "door", -1],     // office
    [56,    19.5, "x", 8.0, "open"],         // living room
    [72,    19.5, "x", 3.0, "door", -1],     // theatre
    [86,    19.5, "x", 3.0, "door", -1],     // gym / music
    [54.5,  25,   "x", 3.0, "door",  1],     // bedroom 3
    [67,    25,   "x", 3.0, "door",  1],     // bath
    [65.5,  28,   "y", 3.0, "door",  1],     // bedroom 3 to bath
    [73.5,  28,   "y", 3.0, "door", -1],     // bath to bedroom 4
    [75,    25,   "x", 3.0, "door",  1],     // bedroom 4
    [87,    25,   "x", 3.0, "door",  1],     // flex
];

// [x, y, axis, width, sill, height]   egress rows: 4.0 x 3.0 ft rough opening, sill 3.5 ft
function base_windows() = [
    [56.5,  39,   "x", 4.0, 3.5, 3.0],       // bedroom 3 (egress)
    [76.5,  39,   "x", 4.0, 3.5, 3.0],       // bedroom 4 (egress)
    [89.5,  39,   "x", 4.0, 3.5, 3.0],       // flex (egress)
    [41.5,  0,    "x", 4.0, 3.5, 3.0],       // office
    [55,    0,    "x", 8.0, 3.5, 3.0],       // living room
    [24,    22,   "y", 3.0, 4,   2],         // utility: louvre for combustion air
    [24,    27,   "y", 3.0, 4,   2],         // utility: louvre / vent chase for the water heater and HRV
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // utility (west wall): air handler, boiler, water heater, HRV, sewage ejector pit
    [24.6,  20.5, 27.6,  23.5, 0, 6,    steel],
    [24.6,  25,   26.8,  27,   0, 3.5,  steel],
    [24.6,  28.5, 26.8,  30.7, 0, 5.5,  steel, "", "round"],
    [24.6,  32,   27.2,  34,   0, 5,    steel],
    [29.5,  36.2, 31.8,  38.5, 0, 0.05, dark],
    // storage shelving
    [26,    1,    36.9,  2.5,  0, 7,    shelf],
    // jack-and-jill bath: curbless shower (recess for the engineer), double vanity, WC
    [66.8,  35.5, 72.4,  38.6, 0, 0.02, tile],
    [66.8,  32.2, 68.6,  34,   0, 1.4,  white],
    [71.4,  32,   73.1,  35.5, 0, 3,    counter],
    [66.7,  26.2, 72.3,  31.8,  0, 0.03, circle_c, "", "round"],
    // elevator hub: nothing in the approach
];

function base_furniture() = [
    [50.5,  4,    60,    7,    0, 2.6,  sofa],        // living room sectional
    [50.5,  7,    53.5,  12,   0, 2.6,  sofa],
    [58,    13,   61,    16,   0, 1.5,  table],
    [67,    1,    69.2,  9,    0, 2,    wood],        // TV unit
    [53.8,  29,   60.3,  34.1, 0, 2,    bed],         // bedroom 3 (head on the west wall, no window behind)
    [73.7,  29,   80.2,  34.1, 0, 2,    bed],         // bedroom 4
    [87,    36,   96,    38.6, 0, 2.5,  wood],        // flex: desk
    [38,    1,    48.5,  3.5,  0, 2.5,  wood],        // office desk
    [71,    14.5, 82,    15.5, 0, 6,    screen],      // theatre screen (flat floor)
    [72.5,  4,    80.5,  7,    0, 2.6,  seat],
    [72.5,  9,    80.5,  12,   0, 2.6,  seat],
    [85,    1,    95.5,  3,    0, 2.5,  dark],        // gym / piano
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
