// Main floor, Option E "Linear ranch" (round 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// One straight bar, x 24..96.5 and y 0..39 (wall centre lines; 73 x 40 ft
// outside, about 2,940 sq ft), with the garage on the west end (x 0..24).
// South row y 0..19.5: mudroom, dining, living, foyer, private hall, bedroom 2.
// North row y 19.5..39: kitchen, stair + future elevator hub, laundry,
// closets, ensuite, primary bedroom (north-east). Stair: one straight flight
// running west along the north wall (house_lib_e.scad). The garage slab is at
// house level (z0 = 0) and the drive slopes up to it: no steps.
// Same table formats and audit echo as models/main_floor.scad.

use <house_lib_e.scad>

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
    // ---- garage (slab at house level), west end
    ["GARAGE",          0,     0,     24,    27,    10, "garage", 0],
    // ---- south row
    ["MUDROOM",         24,    0,     33,    10.5,  10, "utility", 0, "", [28.5, 8.5, 1.0]],
    ["PANTRY",          24,    10.5,  33,    19.5,  10, "utility", 0, "", [28.5, 16.5, 1.0]],
    [["DINING /", "NOOK"], 33, 0,     47,    19.5,  10, "dining", 0, "", [40, 14.5, 1.2]],
    ["LIVING",          47,    0,     65.5,  19.5,  10, "living", 0, "", [56, 14, 1.8]],
    ["VESTIBULE",       65.5,  0,     72,    8,     10, "hall", 0, "", [68.7, 4, 0.8, 90]],
    ["POWDER",          72,    0,     76.5,  8,     10, "bath", 0, "", [74.3, 4, 0.7, 90]],
    ["FOYER",           65.5,  8,     76.5,  19.5,  10, "hall", 0, "", [71, 12, 1.3]],
    ["",                76.5,  0,     82,    19.5,  10, "hall"],              // private hall
    ["BEDROOM 2",       82,    0,     96.5,  11.5,  10, "bed", 0, "", [89.2, 9.2, 1.3]],
    ["BATH",            82,    11.5,  96.5,  19.5,  10, "bath", 0, "", [89.2, 17.4, 1.1]],
    // ---- north row
    ["KITCHEN",         24,    19.5,  42,    39,    10, "kitchen", 0, "", [33, 23.5, 1.6]],
    ["",                42,    19.5,  48,    27,    10, "hall"],              // kitchen to hub passage
    [["ELEVATOR", "(FUTURE)"], 42, 27, 48,   34.4,  10, "closet", 0, "", [45, 30.7, 0.7]],
    ["STAIR DN",        42,    34.4,  53.5,  39,    0,  "stairwell", 0, "", [47.7, 36.7, 0.8]],
    ["",                48,    19.5,  53.5,  34.4,  10, "hall"],              // gallery
    ["",                53.5,  29,    58.5,  34.4,  10, "hall"],              // gallery, east
    ["",                53.5,  34.4,  58.5,  39,    10, "hall"],              // stair-top landing
    ["LAUNDRY",         53.5,  19.5,  61.5,  29,    10, "utility", 0, "", [57.5, 22, 1.0]],
    ["WIC",             61.5,  19.5,  69,    29,    10, "closet", 0, "", [65.2, 22, 1.0]],
    ["WIC",             69,    19.5,  76.5,  29,    10, "closet", 0, "", [72.7, 22, 1.0]],
    ["WC",              58.5,  29,    64,    39,    10, "bath", 0, "", [61.2, 34, 0.9, 90]],
    [["MASTER", "BATH"], 64,   29,    76.5,  39,    10, "bath", 0, "", [70, 31.2, 1.1]],
    [["MASTER", "BEDROOM"], 76.5, 19.5, 96.5, 39,   10, "bed", 0, "", [87, 24, 1.6]],
    // ---- porches and the drive (no walls)
    ["PATIO", 33, -12, 47, 0, 0, "porch", 0, "", [40, -6, 1.2]],
    ["FRONT PORCH",     47,    -12,   82,    0,     0,  "porch", 0, "", [64.5, -6, 1.6]],
    [["DRIVE (SLOPES", "UP TO GARAGE)"], 0, -16, 24, 0, 0, "porch", 0, "", [12, -8, 1.2]],
    ["DECK",             96.5, 21,  108,   37,    0,  "porch", 0, "", [102.2, 29, 1.0]],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    // ---- exterior
    [1.5,   0,    "x", 9,   "garage"],
    [12.5,  0,    "x", 9,   "garage"],
    [67.0,  0,    "x", 3.5, "door",    1],     // front door (42 in)
    [40.5,  0,    "x", 6.0, "double", -1],     // dining to the south porch (BBQ / outdoor dining)
    [96.5,  27,   "y", 6.0, "double",  1],     // primary bedroom to its porch
    // ---- service side
    [24,    3,    "y", 3.0, "door",    1],     // garage to mudroom (step-free)
    [24,    12.5, "y", 3.0, "door",    1],     // garage to pantry (Costco door)
    [26,    10.5, "x", 3.0, "door",   -1],     // mudroom to pantry
    [29,    19.5, "x", 3.0, "door",    1],     // pantry to kitchen
    [33,    3,    "y", 3.0, "door",    1],     // mudroom to dining
    // ---- open zone
    [34,    19.5, "x", 8.0, "full"],           // dining / kitchen
    [47,    2,    "y", 15,  "full"],           // dining / living
    [42,    20.5, "y", 5.5, "full"],           // kitchen / passage
    [48,    19.8, "y", 6.5, "full"],           // passage / gallery
    [48.2,  19.5, "x", 5.1, "full"],           // living / gallery
    // ---- hub
    [48,    28.2, "y", 3.0, "door",    1],     // elevator (future) door
    [53.5,  34.7, "y", 4.3, "full"],           // stair top
    [53.5,  29.3, "y", 4.8, "full"],           // gallery / gallery east
    [53.5,  34.4, "x", 5.0, "full"],           // gallery east / stair landing
    [54.5,  29,   "x", 3.0, "door",   -1],     // laundry from the hub
    // ---- entry
    [67.5,  8,    "x", 3.0, "door",    1],     // vestibule to foyer
    [72.8,  8,    "x", 3.0, "door",    1],     // powder from the foyer
    [65.5,  10,   "y", 6.0, "full"],           // living / foyer
    [76.5,  9,    "y", 5.0, "full"],           // foyer / private hall
    // ---- private zone
    [82,    3,    "y", 3.0, "door",    1],     // bedroom 2
    [82,    14,   "y", 3.0, "door",    1],     // bath
    [78.5,  19.5, "x", 3.0, "door",    1],     // private hall to primary bedroom
    // ---- primary suite
    [61.5,  22,   "y", 3.0, "door",   -1],     // laundry to closet
    [69,    22,   "y", 3.0, "door",    1],     // closet to closet
    [76.5,  24,   "y", 3.0, "door",    1],     // closet to bedroom
    [64.5,  29,   "x", 3.0, "door",   -1],     // closet to ensuite
    [64,    33,   "y", 3.0, "door",   -1],     // ensuite to WC
    [76.5,  31,   "y", 3.0, "door",    1],     // ensuite to bedroom
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [34,    0,    "x", 5.5, 2.5, 5.5],     // dining
    [50,    0,    "x", 12,  2,   6],       // living
    [73.2,  0,    "x", 2.0, 4,   2],       // powder
    [78,    0,    "x", 3.5, 2,   5],       // private hall end
    [86,    0,    "x", 6.0, 2.5, 5],       // bedroom 2
    [96.5,  3,    "y", 5.0, 2.5, 5],
    [96.5,  14,   "y", 3.0, 4,   3],       // bath
    [24,    29,   "y", 5.0, 3.5, 4],       // kitchen, west
    [28,    39,   "x", 8.0, 3.5, 4],       // kitchen, over the sink
    [36,    39,   "x", 4.0, 3.5, 4],
    [59.5,  39,   "x", 2.5, 4,   3],       // WC
    [71,    39,   "x", 4.0, 4,   3],       // ensuite
    [79,    39,   "x", 4.5, 2.5, 5],       // primary bedroom, north
    [92,    39,   "x", 4.0, 2.5, 5],
    [96.5,  21,   "y", 4.0, 2.5, 5],       // primary bedroom, east
    [96.5,  34.5, "y", 3.5, 2.5, 5],
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: sink run on the north wall under the window, range wall west, island with nothing in it
    [27,    37.3, 41.5,  38.8,  0, 3,    counter],
    [30,    37.5, 33,    38.5,  3, 3.05, basin],      // sink
    [24.2,  27.5, 26.7,  36.5,  0, 3,    counter],
    [24.4,  30.5, 26.5,  33,    3, 3.05, dark],       // range
    [24.2,  20,   28.7,  22.4,  0, 7,    steel],      // fridge, by the pantry door
    [31,    27,   40.8,  31.5,  0, 3,    counter],    // island, no seating, nothing in it
    [33.4,  37.3, 35.9,  38.8,  0, 3,    steel],      // dishwasher (54 in aisle to the island)
    // pantry
    [31.8,  11,   32.8,  18.5,  0, 7,    shelf],
    [24.4,  17,   27,    19.2,  0, 6.5,  steel],      // upright freezer
    // mudroom: lockers, bench, drop zone
    [27.5,  0.2,  32.8,  1.7,   0, 7,    wood],
    [27.5,  1.8,  32.8,  3.0,   0, 1.5,  wood],
    [31.8,  6.5,  32.8,  10,    0, 3,    counter],
    // dining: coffee station by the nook
    [43,    18.2, 46.8,  19.2,  0, 3,    counter],
    // powder
    [73.4,  0.8,  75.4,  2.4,   0, 1.4,  white],
    [72.3,  3.4,  73.3,  6.2,   0, 3,    counter],
    // foyer: closed coat storage and a drop shelf
    [66,    18.4, 70.5,  19.3,  0, 7,    shelf],
    [70.5,  18.4, 75.2,  19.3,  0, 3,    counter],    // mail / key drop shelf
    [66.2,  16.9, 70.4,  18.3,  0, 1.5,  wood],       // bench for shoes
    // bedroom 2: wardrobe
    [82.2,  7,    84,    11.3,  0, 7,    shelf],
    // shared bath: curbless shower (recess flagged for the engineer), double vanity, WC
    [91.2,  11.9, 96.3,  15.6,  0, 0.02, tile],
    [86,    17.8, 93,    19.3,  0, 3,    counter],
    [94,    17.4, 95.8,  19.1,  0, 1.4,  white],
    // laundry: washer + dryer on the south wall
    
    [53.7,  19.7, 58,    22.2,  0, 3.2,  steel],
    [58.4,  19.8, 61.3,  21.8,  0, 3,    counter],    // laundry sink
    [59,    20.2, 60.7,  21.4,  3, 3.05, basin],
    // closets
    [62,    19.7, 68.8,  21.2,  0, 7,    shelf],
    [69.2,  27.2, 76.3,  28.8,  0, 7,    shelf],
    // ensuite: curbless shower, double vanity
    [64.4,  34.5, 69.4,  38.8,  0, 0.02, tile],
    [70,    37.4, 76.3,  38.8,  0, 3,    counter],
    // WC room
    [59,    36.5, 61,    38.2,  0, 1.4,  white],
    // 1,700 mm turning circles (floor markers): kitchen, entry, laundry, shared bath, ensuite
    [32.7,  31.6, 38.3,  37.2,  0, 0.03, circle_c, "", "round"],
    [68.2,  10.4, 73.8,  16,    0, 0.03, circle_c, "", "round"],
    [54.7,  22.6, 60.3,  28.2,  0, 0.03, circle_c, "", "round"],
    [85.7,  12.2, 91.3,  17.8,  0, 0.03, circle_c, "", "round"],
    [67.8,  30,   73.4,  35.6,  0, 0.03, circle_c, "", "round"],
    // living room: gas fireplace on the east wall
    [63.8,  4,    65.2,  12,    0, 4,    hearth],
];

function main_furniture() = [
    // dining: 72 in round table for 8, nook table + banquette
    [37,    6,    43,    12,    0, 2.5,  table, "", "round"],
    [34,    14.4, 37,    17.4,  0, 2.5,  table, "", "round"],
    [33.4,  13.8, 34,    18,    0, 1.5,  sofa],
    // living: sectional + two swivel chairs, 75 in TV on the north wall
    [49,    10,   58,    13,    0, 2.6,  sofa],
    [49,    13,   52,    17,    0, 2.6,  sofa],
    [58.5,  7,    61,    9.5,   0, 2.6,  sofa],
    [58.5,  11,   61,    13.5,  0, 2.6,  sofa],
    [53,    5,    57,    8,     0, 1.5,  table],
    // bedroom 2
    [87.5,  7,    92.5,  11.3,  0, 2,    bed],
    // primary bedroom: king bed, 3 ft+ around it
    [84.5,  31,   91,    38.6,  0, 2,    bed],
    [93,    22,   96.2,  26,    0, 2.5,  wood],
];

// steps from the porches down to grade [x, y, direction, width]: four 6 in risers
function main_porch_steps() = [
    [62,    -12,  "-y", 8.0],     // front walk
    [41,    -12,  "-y", 6.0],     // BBQ / dining porch
    [108,   26,   "+x", 6.0],     // primary porch to the yard
];

// porch posts [x, y, height]
function main_posts() = [
    [33.5, -11.6, 9.5], [47, -11.6, 9.5], [60, -11.6, 9.5], [71, -11.6, 9.5], [81.5, -11.6, 9.5],
    [107.5, 21.4, 10], [107.5, 36.6, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [24,    0,    96.5,  39,   10,  0.333, 1.5],   // the bar: one ridge
    [0,     0,    24,    27,   8.5, 0.333, 1.0],   // garage
    [33,    -12,  82,    0,    9.5, 0.25,  0.5],   // south porch
    [96.5,  21,   108,   37,   10,  0.25,  0.5],   // primary porch
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
