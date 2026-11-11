// Main floor, Option F "Your sizes, fitted" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// One plain bar x 24..100.5, y 0..39 (wall centre lines), garage at the west end
// (x 0..24, y 0..28, slab at house level, drive slopes up). Kitchen, dining
// turned east-west, living, foyer hub south; stair, elevator, laundry, ensuite
// north; primary north-east; bedroom 2 south-east. Stair runs west->east beside
// the living room's north wall; opening 11.5 ft from the top nosing.
// Same table formats and audit echo as models/main_floor.scad.

use <house_lib_f.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
show_furniture = true;
audit = false;         // echo the tables for the layout checker

let ($cut = undef) main_level(show_roof, roof_color, roof_opacity, show_furniture, audit);

/* [Hidden] */
counter  = [0.97, 0.97, 0.95];
wood     = [0.55, 0.38, 0.22];
steel    = [0.70, 0.72, 0.74];
dark     = [0.12, 0.12, 0.12];
basin    = [0.62, 0.78, 0.86];
hearth   = [0.35, 0.33, 0.32];
white    = [0.97, 0.97, 0.97];
shelf    = [0.62, 0.50, 0.36];
tile     = [0.55, 0.75, 0.85];
sofa     = [0.45, 0.50, 0.60];
bed      = [0.92, 0.88, 0.80];
circle_c = [0.95, 0.75, 0.75];   // 1,700 mm (5.6 ft) turning circle, floor marker
table    = [0.66, 0.50, 0.34];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    ["GARAGE",          0,     0,     24,    30,    10, "garage", 0],
    // ---- south band
    [["DINING /", "NOOK"], 24, 0,     47.8,  14.4,  10, "dining", 0, "", [36, 12.4, 1.4]],
    ["LIVING",          47.8,  0,     68.2,  20.4,  10, "living", 0, "", [58, 15, 1.8]],
    ["VESTIBULE",       68.2,  0,     78.1,  8.4,   10, "hall", 0, "", [73.1, 4, 0.8]],
    ["FOYER",           68.2,  8.4,   78.1,  18.6,  10, "hall", 0, "", [73.1, 13.5, 1.3]],
    [["SHARED BATH", "/ POWDER"], 78.1, 0, 86.5, 12.4, 10, "bath", 0, "", [82.3, 10.6, 0.8]],
    ["BEDROOM 2",       86.5,  0,     98.9,  12.4,  10, "bed", 0, "", [92.7, 10, 1.3]],
    ["",                78.1,  12.4,  91.5,  18.6,  10, "hall"],              // bedroom hall
    ["WIC",             91.5,  12.4,  100.5, 18.6,  10, "closet", 0, "", [96, 14, 0.9]],
    // ---- west column on the garage wall, kitchen
    ["MUDROOM",         24,    14.4,  32.4,  24.8,  10, "utility", 0, "", [28.2, 22.5, 1.0]],
    ["PANTRY",          24,    24.8,  32.4,  37.2,  10, "utility", 0, "", [28.2, 34.5, 1.0]],
    ["KITCHEN",         32.4,  14.4,  47.8,  36.8,  10, "kitchen", 0, "", [40, 33, 1.6]],
    // ---- hub
    [["STAIR DN"],      47.8,  20.4,  59.5,  24.6,  0,  "stairwell", 0, "", [53.6, 22.5, 0.8]],
    ["",                59.5,  20.4,  68.2,  24.6,  10, "hall"],              // stair-top landing
    ["",                47.8,  24.6,  64.7,  30,    10, "hall"],              // gallery
    ["",                47.8,  30,    53.8,  32.4,  10, "hall"],              // elevator approach
    [["ELEVATOR", "(FUTURE)"], 47.8, 32.4, 53.8, 39, 10, "closet", 0, "", [50.8, 35.7, 0.7]],
    ["LAUNDRY",         53.8,  30,    64.7,  39,    10, "utility", 0, "", [59.2, 36.5, 1.0]],
    // ---- primary suite
    [["MASTER", "BATH"], 64.7, 24.6,  78.1,  39,    10, "bath", 0, "", [71.4, 26.8, 1.1]],
    ["WIC",             68.2,  18.6,  78.1,  24.6,  10, "closet", 0, "", [73.1, 20.6, 0.9]],
    [["MASTER", "BEDROOM"], 78.1, 18.6, 100.5, 39,  10, "bed", 0, "", [89.3, 23.5, 1.6]],
    // ---- porches and the drive (no walls)
    ["PATIO", 24, -10, 36, 0, 0, "porch", 0, "", [30.5, -5, 1.2]],
    ["FRONT PORCH",     68.4,  -8,    74.4,  0,     0,  "porch", 0, "", [71.4, -4, 1.0]],
    [["DRIVE (SLOPES", "UP TO GARAGE)"], 0, -16, 24, 0, 0, "porch", 0, "", [12, -8, 1.2]],
    ["DECK",            100.5, 21,    112,   37,    0,  "porch", 0, "", [106.2, 29, 1.0]],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    [1.5,   0,    "x", 9,   "garage"],
    [12.5,  0,    "x", 9,   "garage"],
    [70.0,  0,    "x", 3.5, "door",    1],     // front door (42 in)
    [27.0,  0,    "x", 6.0, "double", -1],     // dining to the patio
    [100.5, 27,   "y", 6.0, "double",  1],     // primary to its deck
    // service side
    [24,    17,   "y", 3.0, "door",    1],     // garage to mudroom (step-free)
    [24,    26.0, "y", 3.0, "door",   -1],     // garage to pantry (Costco door)
    [26,    24.8, "x", 3.0, "door",   -1],     // mudroom to pantry
    [26,    14.4, "x", 3.0, "door",    1],     // mudroom to dining
    [32.4,  28,   "y", 3.0, "door",    1],     // pantry to kitchen
    [33,    14.4, "x", 12,  "full"],           // dining / kitchen
    [47.8,  2,    "y", 6.0, "double",  1],     // dining / living
    [47.8,  24.8, "y", 4.5, "full"],           // kitchen / gallery
    // hub
    [60.5,  20.4, "x", 6.0, "full"],           // living / landing
    [59.5,  20.7, "y", 3.6, "full"],           // landing / stair top
    [60,    24.6, "x", 4.5, "full"],           // landing / gallery
    [48.2,  30,   "x", 5.2, "full"],           // gallery / elevator approach
    [49.5,  32.4, "x", 3.0, "door",   -1],     // elevator (future) door
    [55,    30,   "x", 3.0, "door",   -1],     // laundry
    [64.7,  33,   "y", 3.0, "door",    1],     // laundry to ensuite
    // entry
    [71.5,  8.4,  "x", 3.0, "door",    1],     // vestibule to foyer
    [68.2,  10,   "y", 8.0, "full"],           // living / foyer
    [78.1,  13,   "y", 5.0, "full"],           // foyer / bedroom hall
    // private zone
    [80.5,  12.4, "x", 3.0, "door",   -1],     // shared bath from the hall
    [88.5,  12.4, "x", 3.0, "door",   -1],     // bedroom 2
    [80,    18.6, "x", 3.0, "door",    1],     // hall to primary
    [93.5,  18.6, "x", 3.0, "door",    1],     // primary to walk-in
    [78.1,  20,   "y", 3.0, "door",   -1],     // primary to walk-in (west)
    [78.1,  32,   "y", 3.0, "door",   -1],     // primary to ensuite
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [37,    0,    "x", 5.5, 2.5, 5.5],     // dining
    [43,    0,    "x", 3.5, 2.5, 5.5],
    [52,    0,    "x", 12,  2,   6],       // living
    [80,    0,    "x", 2.5, 4,   2],       // bath
    [91,    0,    "x", 6.0, 2.5, 5],       // bedroom 2
    [98.9,  3,    "y", 5.0, 2.5, 5],
    [36,    36.8, "x", 6.0, 3.5, 4],       // kitchen over the sink
    [43,    36.8, "x", 3.0, 3.5, 4],
    [26,    37.2, "x", 2.5, 4,   2],       // pantry
    [57,    39,   "x", 3.0, 3.5, 3],       // laundry
    [68,    39,   "x", 4.0, 4,   3],       // ensuite
    [82,    39,   "x", 4.5, 2.5, 5],       // primary, north
    [92,    39,   "x", 5.0, 2.5, 5],
    [100.5, 21,   "y", 4.0, 2.5, 5],       // primary, east
    [100.5, 34,   "y", 3.5, 2.5, 5],
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: sink run on the north wall under the window, range wall west, island with nothing in it
    [33,    35.3, 46.8,  36.6,  0, 3,    counter],
    [37.5,  35.5, 40.5,  36.4,  3, 3.05, basin],      // sink
    [41,    35.3, 43.5,  36.6,  0, 3,    steel],      // dishwasher
    [32.6,  16,   35,    22.5,  0, 3,    counter],
    [32.8,  18.2, 34.8,  20.4,  3, 3.05, dark],       // cooktop
    [32.6,  25.4, 35.2,  28,    0, 7,    steel],      // fridge, by the pantry door
    [39.6,  22,   44,    29,    0, 3,    counter],    // island, no seating, nothing in it
    // pantry
    [31.6,  25,   32.2,  36.8,  0, 7,    shelf],
    [24.4,  35,   27,    37,    0, 6.5,  steel],      // upright freezer
    // mudroom lockers and bench
    [24.2,  20.2, 25.4,  24.2,  0, 7,    wood],
    [30.8,  15,   32.2,  24,    0, 1.5,  wood],
    // dining: coffee station by the nook
    [46.2,  7,    47.6,  13.5,  0, 3,    counter],
    // foyer storage
    [68.4,  16.8, 72,    18.4,  0, 7,    shelf],
    [72,    17,   77.8,  18.4,  0, 3,    counter],
    // bedroom 2 wardrobe
    [86.7,  9,    88.5,  12.2,  0, 7,    shelf],
    // shared bath / powder: toilet, vanity, curbless shower (recess flagged for the engineer)
    [79,    0.6,  81,    2.4,   0, 1.4,  white],
    [81.8,  0.5,  86.2,  2.0,   0, 3,    counter],
    [80.6,  8.2,  85.8,  12.0,  0, 0.02, tile],
    // laundry
    [54,    35.0, 58.5,  38.8,  0, 3.2,  steel],
    [59,    37.6, 64.5,  38.8,  0, 3,    counter],
    [60,    37.8, 62,    38.6,  3, 3.05, basin],
    // closets
    [68.4,  18.8, 77.9,  19.9,  0, 7,    shelf],
    [91.7,  12.6, 100.3, 14,    0, 7,    shelf],
    // ensuite: curbless shower with bench, double vanity, toilet
    [72.6,  33.5, 77.8,  38.8,  0, 0.02, tile],
    [65,    37.4, 71.4,  38.8,  0, 3,    counter],
    [65,    30.5, 66.8,  32.3,  0, 1.4,  white],
    // 1,700 mm turning circles: kitchen, entry, laundry, shared bath, ensuite
    [35.8,  29.4, 41.4,  35,    0, 0.03, circle_c, "", "round"],
    [70.4,  10.6, 76,    16.2,  0, 0.03, circle_c, "", "round"],
    [58,    30.4, 63.6,  36,    0, 0.03, circle_c, "", "round"],
    [78.6,  2.6,  84.2,  8.2,   0, 0.03, circle_c, "", "round"],
    [66.6,  27.2, 72.2,  32.8,  0, 0.03, circle_c, "", "round"],
    // living: gas fireplace on the east wall
    [66.6,  3,    68,    8,     0, 4,    hearth],
];

function main_furniture() = [
    // dining: 72 in round table for 8, nook table + banquette by the coffee station
    [29.5,  4.5,  35.5,  10.5,  0, 2.5,  table, "", "round"],
    [41.5,  7,    44.5,  10,    0, 2.5,  table],
    [41.2,  6.6,  44.8,  7.2,   0, 1.5,  sofa],
    // living: sectional + two swivel chairs, 75 in TV on the north wall
    [50,    8,    58,    11,    0, 2.6,  sofa],
    [50,    11,   53,    15,    0, 2.6,  sofa],
    [60,    6,    62.8,  8.8,   0, 2.6,  sofa],
    [60,    11,   62.8,  13.8,  0, 2.6,  sofa],
    [54,    4.5,  57.5,  7.2,   0, 1.5,  table],
    [51,    18.8, 57.3,  20,    0, 2,    wood],
    // bedroom 2
    [91,    4,    97,    8.3,   0, 2,    bed],
    // primary: king bed with 3 ft+ around it, nightstands, bench, armchair, dresser, vanity
    [86,    32.2, 92.3,  38.6,  0, 2,    bed],
    [83.5,  37.2, 85.5,  38.8,  0, 2,    wood],
    [93,    37.2, 95,    38.8,  0, 2,    wood],
    [87,    29.5, 91.2,  31,    0, 1.5,  wood],
    [96.5,  22,   100,   25.5,  0, 2.5,  sofa],
    [86,    19,   92,    20.5,  0, 2.5,  wood],
    [97.5,  31,   99.8,  36,    0, 2.5,  table],
];

// steps from the porches down to grade [x, y, direction, width]: four 6 in risers
function main_porch_steps() = [
    [70,    -8,   "-y", 4.0],
    [29,    -10,  "-y", 5.0],
    [112,   26,   "+x", 6.0],
];

// porch posts [x, y, height]
function main_posts() = [
    [68.8, -7.6, 9.5], [74, -7.6, 9.5],
    [25.4, -9.6, 9.5], [35.6, -9.6, 9.5],
    [111.5, 21.4, 10], [111.5, 36.6, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [24,    0,    100.5, 39,   10,  0.333, 1.5],   // the bar: one ridge
    [0,     0,    24,    30,   8.5, 0.333, 1.0],   // garage
    [68.4,  -8,   74.4,  0,    9.5, 0.25,  0.5],
    [24,    -10,  36,    0,    9.5, 0.25,  0.5],
    [100.5, 21,   112,   37,   10,  0.25,  0.5],
];

// The main floor assembly under the heated rooms, with the stair opening left out.
module floor_assembly(rooms) {
    paint(floor_frame())
        difference() {
            union()
                for (r = rooms)
                    if (r[6] != "porch" && r[6] != "garage" && r[6] != "stairwell")
                        translate([r[1] - wall_t() / 2, r[2] - wall_t() / 2, -main_floor_depth()])
                            cube([r[3] - r[1] + wall_t(), r[4] - r[2] + wall_t(), main_floor_depth() - 0.15]);
            translate([stair_x()[0] + wall_t() / 2 + 0.01, stair_y()[0] + wall_t() / 2 + 0.01, -5])
                cube([stair_x()[1] - stair_x()[0] - wall_t() - 0.02, stair_y()[1] - stair_y()[0] - wall_t() - 0.02, 10]);
        }
}

module main_level(show_roof = true, roof_color = [0.20, 0.38, 0.62], roof_opacity = 1,
                  show_furniture = true, audit = false, show_stair = true) {
    rooms = main_rooms();
    doors = main_doors();
    if (audit) echo(rooms = rooms, doors = doors, windows = main_windows(),
                    fixtures = concat(main_fixtures(), main_furniture()));

    draw_level(rooms, doors, main_windows());
    floor_assembly(rooms);
    fixtures(main_fixtures());
    if (show_furniture) fixtures(main_furniture());
    if (show_stair) main_stair();
    for (p = main_posts()) post(p[0], p[1], p[2]);
    for (p = main_porch_steps()) porch_steps(p[0], p[1], p[2], p[3]);
    if (show_roof) roofs(main_roof(), roof_color, roof_opacity);
}
