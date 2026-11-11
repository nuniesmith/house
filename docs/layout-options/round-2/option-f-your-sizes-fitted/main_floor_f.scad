// Main floor, Option F "Your sizes, fitted" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// Kayla's list (Nov 11), compact L. South wing (x 23..98.4): garage-side block
// (pantry, mudroom), kitchen -> dining -> living in a row with 14 ft openings, then
// the junction at the inner corner: foyer, stair (top nosing at the junction hall),
// elevator, powder off the foyer passage. Quiet wing turns north from the east end
// (x 98.4..127): one bedroom hall, bedroom 2, shared bath, laundry, walk-ins, ensuite,
// primary at the north end. Office/library at the north-west corner, off the mudroom.
// Garage slab at house level. No gallery, no hall along the south wing.
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
    ["GARAGE",          0,     0,     23,    24.8,  10, "garage", 0],
    // ---- garage-side block
    ["PANTRY",          23,    0,     32.4,  12.4,  10, "utility", 0, "", [27.7, 6, 1.0]],
    ["MUDROOM",         23,    12.4,  32.4,  24.8,  10, "utility", 0, "", [27.7, 18.5, 1.0]],
    ["OFFICE / LIBRARY", 16.6, 24.8,  32,    41.2,  10, "office", 0, "", [24.3, 33, 1.2]],
    // ---- sunny wing: kitchen -> dining -> living
    ["KITCHEN",         32.4,  0,     47.8,  22.4,  10, "kitchen", 0, "", [40, 17, 1.6]],
    [["DINING /", "NOOK"], 47.8, 0,   62.2,  22.4,  10, "dining", 0, "", [55, 17, 1.4]],
    ["LIVING",          62.2,  0,     86.6,  20.4,  10, "living", 0, "", [74.4, 15, 1.8]],
    // ---- junction: foyer, stair, elevator, powder
    ["FOYER",           86.6,  0,     98.4,  8.4,   10, "hall", 0, "", [92.5, 4.2, 1.1]],
    [["STAIR DN"],      86.6,  8.4,   92,    20.4,  0,  "stairwell", 0, "", [89.3, 14.4, 0.8]],
    ["",                92,    8.4,   98.4,  20.4,  10, "hall"],              // junction passage
    ["",                86.6,  20.4,  98.4,  25.8,  10, "hall"],              // junction hall (stair top)
    ["CLOSET",          86.6,  25.8,  92,    33.2,  10, "closet", 0, "", [89.3, 29.5, 0.7]],
    [["ELEVATOR", "(FUTURE)"], 92, 25.8, 98.4, 33.2, 10, "closet", 0, "", [95.2, 29.5, 0.7]],
    // ---- quiet wing
    ["POWDER",          98.4,  5,     104.8, 12.4,  10, "bath", 0, "", [101.6, 8.7, 0.7]],
    ["",                98.4,  20.4,  127,   25.8,  10, "hall"],              // bedroom hall
    ["SHARED BATH",     98.4,  12.4,  106.8, 20.4,  10, "bath", 0, "", [102.6, 16.4, 0.8]],
    ["CLOSET",          106.8, 12.4,  114.6, 20.4,  10, "closet", 0, "", [110.7, 16.4, 0.7]],
    ["BEDROOM 2",       114.6, 6,     127,   20.4,  10, "bed", 0, "", [120.8, 15, 1.3]],
    ["LAUNDRY",         98.4,  25.8,  107.8, 36.2,  10, "utility", 0, "", [103.1, 31, 1.0]],
    ["LINEN",           107.8, 25.8,  111.2, 36.2,  10, "closet", 0, "", [109.5, 31, 0.5, 90]],
    ["",                111.2, 25.8,  116.6, 36.2,  10, "hall"],              // short hall to the primary
    ["WIC",             98.4,  36.2,  104.8, 44.6,  10, "closet", 0, "", [101.6, 40.4, 0.8]],
    ["WIC",             104.8, 36.2,  111.2, 44.6,  10, "closet", 0, "", [108, 40.4, 0.8]],
    ["",                111.2, 36.2,  116.6, 44.6,  10, "hall"],              // primary entry
    [["MASTER", "BATH"], 116.6, 25.8, 127,   44.6,  10, "bath", 0, "", [121.8, 35, 1.0]],
    [["MASTER", "BEDROOM"], 99.6, 44.6, 127, 67,    10, "bed", 0, "", [113.3, 56, 1.6]],
    // ---- porches and the drive (no walls)
    [["DRIVE (SLOPES", "UP TO GARAGE)"], 0, -16, 23, 0, 0, "porch", 0, "", [11.5, -8, 1.2]],
    ["PATIO",           49,    -10,   61,    0,     0,  "porch", 0, "", [55, -5, 1.2]],
    ["FRONT PORCH",     89,    -8,    96,    0,     0,  "porch", 0, "", [92.5, -4, 1.0]],
    ["DECK",            127,   48,    130,   64,    0,  "porch", 0, "", [128.5, 56, 0.5, 90]],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    [1.5,   0,    "x", 9,   "garage"],
    [12.5,  0,    "x", 9,   "garage"],
    [91.0,  0,    "x", 3.5, "door",    1],     // front door (42 in) into the foyer
    [51.0,  0,    "x", 6.0, "double", -1],     // dining to the patio
    [127,   52,   "y", 3.0, "double",  1],     // primary to its deck
    // garage-side block
    [23,    2,    "y", 3.0, "door",    1],     // garage to pantry (Costco door)
    [23,    15,   "y", 3.0, "door",    1],     // garage to mudroom (step-free)
    [32.4,  3,    "y", 3.0, "door",    1],     // pantry to kitchen (its own entrance)
    [32.4,  18.9, "y", 3.0, "door",   -1],     // mudroom to kitchen
    [24.5,  24.8, "x", 3.0, "door",    1],     // mudroom to the office / library
    // sunny wing
    [47.8,  3,    "y", 14,  "full"],           // kitchen / dining
    [62.2,  3,    "y", 14,  "full"],           // dining / living
    [86.6,  1.5,  "y", 6.5, "full"],           // living / foyer
    // junction
    [93.5,  8.4,  "x", 4.5, "full"],           // foyer / junction passage
    [93.5,  20.4, "x", 4.5, "full"],           // passage / junction hall
    [87,    20.4, "x", 4.8, "full"],           // junction hall / stair top
    [87.5,  25.8, "x", 3.0, "door",    1],     // closet from the junction hall
    [94,    25.8, "x", 3.0, "door",   -1],     // elevator (future) door
    [98.4,  9,    "y", 3.0, "door",    1],     // powder from the junction passage
    [98.4,  21.2, "y", 4.5, "full"],           // junction hall / bedroom hall
    // quiet wing
    [100,   20.4, "x", 3.0, "door",   -1],     // shared bath
    [117,   20.4, "x", 3.0, "door",   -1],     // bedroom 2
    [114.6, 15,   "y", 3.0, "door",    1],     // bedroom 2 closet
    [100,   25.8, "x", 3.0, "door",    1],     // laundry from the bedroom hall
    [108.1, 25.8, "x", 3.0, "door",   -1],     // linen
    [101.5, 36.2, "x", 3.0, "door",    1],     // laundry to walk-in
    [112,   25.8, "x", 4.0, "full"],           // bedroom hall / short hall
    [112,   36.2, "x", 4.0, "full"],
    [113,   44.6, "x", 3.0, "door",    1],     // primary entry
    [100.5, 44.6, "x", 3.0, "door",   -1],     // primary to walk-in
    [106,   44.6, "x", 3.0, "door",   -1],     // primary to walk-in
    [120,   44.6, "x", 3.0, "door",   -1],     // primary to ensuite
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [36,    0,    "x", 6.0, 3.5, 4],       // kitchen, south
    [35,    22.4, "x", 8.0, 3.5, 4],       // kitchen over the sink, north
    [48.2,  0,    "x", 2.5, 2.5, 5.5],     // dining
    [58,    0,    "x", 3.5, 2.5, 5.5],
    [68,    0,    "x", 12,  2,   6],       // living, south
    [66,    20.4, "x", 8,   3,   4],       // living, north
    [16.6,  26,   "y", 3.5, 2.5, 5],       // office / library, south half
    [16.6,  35,   "y", 3.5, 2.5, 5],       // north half
    [20,    41.2, "x", 4.0, 2.5, 5],
    [26,    41.2, "x", 4.0, 2.5, 5],
    [116,   6,    "x", 6.0, 2.5, 5],       // bedroom 2
    [127,   10,   "y", 5.0, 2.5, 5],
    [127,   30,   "y", 3.0, 4,   3],       // ensuite
    [103,   67,   "x", 5.0, 2.5, 5],       // primary
    [114,   67,   "x", 6.0, 2.5, 5],
    [99.6,  52,   "y", 5.0, 2.5, 5],
    [127,   60,   "y", 4.0, 2.5, 5],
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: 22 ft range wall (west), sink run on the north wall under the window, island with 4 ft aisles
    [32.6,  7,    34.6,  16,    0, 3,    counter],    // west run: oven column, range, fridge
    [32.8,  9,    34.4,  12,    3, 3.05, dark],       // cooktop
    [32.6,  16,   34.8,  18.6,  0, 7,    steel],      // fridge beside the range wall
    [34.6,  20.4, 46.8,  22.2,  0, 3,    counter],    // north run
    [38,    20.6, 41,    21.8,  3, 3.05, basin],      // sink under the north window
    [42,    20.4, 44.5,  22.2,  0, 3,    steel],      // dishwasher
    [38.6,  6,    41.6,  15.4,  0, 3,    counter],    // island, no seating, nothing in it
    // pantry
    [31.6,  0.4,  32.2,  12,    0, 7,    shelf],
    [23.4,  8,    26,    11.6,  0, 6.5,  steel],      // upright freezer
    // mudroom lockers and bench
    [23.2,  18,   24.4,  24.4,  0, 7,    wood],
    [30.8,  12.8, 32.2,  17.5,  0, 1.5,  wood],
    // dining: coffee station by the nook
    [60.4,  15,   62,    21.4,  0, 3,    counter],
    // foyer: closed coats
    [86.8,  7,    92,    8.2,   0, 7,    shelf],
    // powder
    [98.8,  5.4,  100.4, 7,     0, 1.4,  white],
    [102.4, 5.4,  104.6, 8,     0, 3,    counter],
    // shared bath
    [98.8,  13,   100.4, 14.6,  0, 1.4,  white],
    [98.7,  15.2, 100,   19,    0, 3,    counter],
    [102,   12.6, 106.6, 16.2,  0, 0.02, tile],       // curbless shower
    // bedroom 2 closet
    [107,   12.6, 114.4, 13.6,  0, 7,    shelf],
    // laundry: 10 ft appliance wall (W/D side by side) on the east wall; sink
    [106.2, 26.2, 107.7, 36,    0, 3.2,  steel],
    [98.6,  34.6, 105.6, 36,    0, 3,    counter],
    [100,   34.8, 102,   35.8,  3, 3.05, basin],
    // walk-ins
    [98.6,  36.4, 99.8,  44.4,  0, 7,    shelf],
    [106.4, 36.4, 110.6, 37.4,  0, 7,    shelf],
    // ensuite: curbless wet zone (tub + shower, screened) at the north end; vanity and WC outside it
    [117,   26.2, 126.6, 33.4,  0, 0.02, tile],       // wet zone floor (recess flagged for the engineer)
    [117.4, 26.4, 123,   29.4,  0, 1.6,  white],      // soaking tub
    [123.6, 26.4, 126.4, 32.6,  0, 0.03, tile],       // shower with bench
    [117,   37,   118.4, 43.4,  0, 3,    counter],    // vanity
    [124.8, 38,   126.4, 39.6,  0, 1.4,  white],      // WC
    // 1,700 mm turning circles: kitchen, foyer, powder, laundry, shared bath, ensuite
    [34.8,  17.6, 40.4,  21.2,  0, 0.03, circle_c, "", "round"],
    [88.6,  1.8,  94.2,  7.4,   0, 0.03, circle_c, "", "round"],
    [98.7,  6.6,  104.3, 12,    0, 0.03, circle_c, "", "round"],
    [99.8,  28.4, 105.4, 34,    0, 0.03, circle_c, "", "round"],
    [99,    13.2, 104.6, 18.8,  0, 0.03, circle_c, "", "round"],
    [119,   35.2, 124.6, 40.8,  0, 0.03, circle_c, "", "round"],
    // living: gas fireplace on the east wall
    [84.8,  3,    86.2,  8,     0, 4,    hearth],
];

function main_furniture() = [
    // dining: 72 in round table for 8, nook table + banquette by the coffee station
    [48.5,  4,    54.5,  10,    0, 2.5,  table, "", "round"],
    [56,    14,   59.5,  17.5,  0, 2.5,  table],
    [55.6,  17.5, 59.9,  18.2,  0, 1.5,  sofa],
    // living: sectional + two swivel chairs, 75 in TV on the north wall
    [65,    8,    73,    11,    0, 2.6,  sofa],
    [65,    11,   68,    16,    0, 2.6,  sofa],
    [76,    6,    78.8,  8.8,   0, 2.6,  sofa],
    [76,    11,   78.8,  13.8,  0, 2.6,  sofa],
    [70,    4.5,  73.5,  7.2,   0, 1.5,  table],
    [76,    18.6, 82,    19.9,  0, 2,    wood],
    // office / library: desks end (south half), reading end (north half)
    [17,    26,   23,    28,    0, 2.5,  wood],
    [17,    39,   19,    41,    0, 6,    shelf],
    [21,    37,   25,    40,    0, 2.6,  sofa],
    // bedroom 2
    [120,   11,   126,   15.3,  0, 2,    bed],
    // primary: king bed with 3 ft+ around it
    [110,   62,   116.3, 66.6,  0, 2,    bed],
    [107.5, 65,   109.5, 66.8,  0, 2,    wood],
    [117,   65,   119,   66.8,  0, 2,    wood],
    [112,   50,   116,   51.5,  0, 1.5,  wood],
    [101,   56,   104.5, 59.5,  0, 2.5,  sofa],
    [106,   45,   112,   46.5,  0, 2.5,  wood],
    [124.5, 60,   126.8, 65.5,  0, 2.5,  table],
];

// steps from the porches down to grade [x, y, direction, width]: four 6 in risers
function main_porch_steps() = [
    [92,    -8,   "-y", 4.0],
    [55,    -10,  "-y", 5.0],
];

// porch posts [x, y, height]
function main_posts() = [
    [89.4, -7.6, 9.5], [95.6, -7.6, 9.5],
    [49.4, -9.6, 9.5], [60.6, -9.6, 9.5],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [32.4,  0,    86.6,  22.4, 10,  0.333, 1.5],   // sunny wing
    [86.6,  0,    98.4,  33.2, 10,  0.333, 1.5],   // junction
    [16.6,  24.8, 32.4,  41.2, 10,  0.333, 1.5],   // office / garage-side block
    [98.4,  5,    127,   67,   10,  0.333, 1.5],   // quiet wing
    [0,     0,    23,    24.8, 8.5, 0.333, 1.0],   // garage
    [89,    -8,   96,    0,    9.5, 0.25,  0.5],
    [49,    -10,  61,    0,    9.5, 0.25,  0.5],
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
