// Main floor, Option H "Knuckle hub" (round 3, revision 2).
// Units: feet. Visualisation only - NOT construction documents.
//
// Two wings meet at a daylit hub. South wing: living (SW) | hub | dining (SE). The dining room and the
// kitchen are STACKED on the hub's east side: dining south (patio on its east), kitchen north of it,
// each with its own opening onto the hub, joined to each other by an 8 ft opening. Hub (FOYER):
// vestibule with an inner door, powder, stair (west wall), lift, library and living doors on the west.
// The mudroom opens off the hub's north-east corner and sits between the hub and the garage; the pantry
// sits between the kitchen and the garage. The quiet wing runs north off the hub through one 15 ft hall
// (shared bath, linen, laundry, bedroom 2 and the primary door). Hub light: glazed front door + sidelight
// and a clerestory on the raised hub roof (last block of the roof table).

use <house_lib_h.scad>

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
    // ---- south wing: living | hub | dining; kitchen stacked north of the dining room
    ["LIVING",          28,    0,     50,    20.4,  10, "living", 0, "", [39, 10, 1.8]],
    ["VESTIBULE",       50,    0,     59.6,  7.4,   10, "hall", 0, "", [54.8, 3.7, 0.8]],
    ["POWDER",          59.6,  0,     66,    7.4,   10, "bath", 0, "", [62.8, 3.7, 0.7]],
    [["DINING /", "NOOK"], 66, 0,     85,    14,    10, "dining", 0, "", [75.5, 7, 1.4]],
    ["KITCHEN",         66,    14,    88,    29,    10, "kitchen", 0, "", [77, 21.5, 1.6]],
    // ---- the hub (FOYER): stair on the west wall, lift on the east, openings to every side
    ["FOYER",           50,    7.4,   66,    14.4,  10, "hall", 0, "", [58, 10.9, 1.2]],
    [["STAIR DN"],      50,    14.4,  55.4,  26.4,  0,  "stairwell", 0, "", [52.7, 20.4, 0.8]],
    ["",                55.4,  14.4,  66,    22.4,  10, "hall"],
    ["",                55.4,  22.4,  60,    26.4,  10, "hall"],
    ["",                50,    26.4,  60,    33,    10, "hall"],              // stair-top landing
    ["",                60,    22.4,  66,    33,    10, "hall"],
    ["OFFICE / LIBRARY", 35,   20.4,  50,    36.4,  10, "office", 0, "", [42.5, 28.4, 1.3]],
    // ---- garage side: mudroom (off the hub), pantry (off the kitchen), garage beyond both
    ["MUDROOM",         66,    29,    79,    40.5,  10, "utility", 0, "", [72.5, 34.7, 1.0]],
    ["PANTRY",          79,    29,    91,    37,    10, "utility", 0, "", [85, 33, 1.0]],
    ["GARAGE",          79,    37,    103,   61,    10, "garage", 0],
    // ---- quiet wing: one 15 ft hall off the hub's north side
    ["",                59,    33,    66,    48.4,  10, "hall"],              // the bedroom hall
    [["ELEVATOR", "(FUTURE)"], 53, 33, 59, 40,      10, "closet", 0, "", [56, 36.5, 0.7]],      // opens onto the bedroom hall
    ["LINEN",           50,    33,    53,    40,    10, "closet", 0, "", [51.5, 36.5, 0.5, 90]],
    ["SHARED BATH",     50,    40,    59,    48.4,  10, "bath", 0, "", [54.5, 44.2, 0.8]],
    ["WIC",             44,    36.4,  50,    48.4,  10, "closet", 0, "", [47, 42.4, 0.7]],
    ["WIC",             38,    36.4,  44,    48.4,  10, "closet", 0, "", [41, 42.4, 0.7]],
    ["ENSUITE",         26,    36.4,  38,    48.4,  10, "bath", 0, "", [32, 42.4, 1.0]],
    ["LAUNDRY",         66,    40.5,  75.5,  48.4,  10, "utility", 0, "", [70, 44.7, 0.9]],
    ["BEDROOM 2",       62.5,  48.4,  74.5,  60.4,  10, "bed", 0, "", [67.5, 54.4, 1.3]],
    [["MASTER", "BEDROOM"], 34.5, 48.4, 62.5, 70.4, 10, "bed", 0, "", [48, 59.4, 1.7]],
    // ---- porches and the drive (no walls)
    [["DRIVE (LEVEL TO", "GARAGE DOORS)"], 103, -16, 127, 61, 0, "porch", 0, "", [115, 22, 1.2, 90]],
    ["PATIO",           85,    1,     97,    11,    0,  "porch", 0, "", [91, 7, 1.2]],
    ["FRONT PORCH",     50,    -8,    60,    0,     0,  "porch", 0, "", [55, -4, 1.0]],
    ["DECK",            28.5,  54,    34.5,  66,    0,  "porch", 0, "", [31.5, 60, 0.8, 90]],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    [103,   40,   "y", 9,   "garage"],
    [103,   50,   "y", 9,   "garage"],
    [54.5,  0,    "x", 3.5, "door",    1],     // front door (42 in), glazed, into the vestibule
    [85,    3,    "y", 6.0, "double",  1],     // dining to the covered patio
    [34.5,  55,   "y", 6.0, "double", -1],     // primary to its deck
    // hub
    [51,    7.4,  "x", 3.0, "door",    1],     // vestibule inner door (offset west of the front door)
    [62,    7.4,  "x", 3.0, "door",   -1],     // powder from the hub
    [50,    8.5,  "y", 5.0, "full"],           // living / hub
    [66,    8,    "y", 4.0, "full"],           // dining / hub
    [66,    17,   "y", 4.0, "full"],           // kitchen / hub
    [57,    14.4, "x", 6.0, "full"],           // hub / hub east piece
    [56,    22.4, "x", 3.5, "full"],
    [56,    26.4, "x", 4.0, "full"],
    [61,    22.4, "x", 4.0, "full"],
    [60,    28,   "y", 4.0, "full"],
    [50.2,  26.4, "x", 5.2, "full"],           // stair top
    [50,    28,   "y", 4.0, "full"],           // library / hub
    [60,    33,   "x", 4.0, "full"],           // hub / bedroom hall
    // dining / kitchen, garage side
    [77,    14,   "x", 8.0, "full"],           // kitchen / dining
    [66,    30,   "y", 3.0, "door",    1],     // hub to mudroom
    [79,    37.3, "y", 3.0, "door",    1],     // mudroom to garage (direct, step-free)
    [79,    30,   "y", 3.0, "door",    1],     // mudroom to pantry
    [80,    29,   "x", 3.0, "door",   -1],     // pantry to kitchen (its own door)
    [83,    37,   "x", 3.0, "door",    1],     // pantry to garage (Costco door, step-free)
    // bedroom hall
    [59,    34,   "y", 3.0, "door",   -1],     // elevator (future), 7 x 7 ft approach in the hall
    [59,    43,   "y", 3.0, "door",   -1],     // shared bath
    [50,    40,   "x", 3.0, "full"],           // linen: cased opening from the bath, shelves behind
    [66,    43,   "y", 3.0, "door",    1],     // laundry
    [59,    48.4, "x", 3.0, "door",    1],     // primary
    [63,    48.4, "x", 3.0, "door",    1],     // bedroom 2
    // primary suite
    [39,    48.4, "x", 3.0, "door",   -1],     // walk-in
    [45,    48.4, "x", 3.0, "door",   -1],     // walk-in
    [35,    48.4, "x", 3.0, "door",    1],     // ensuite
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [50.8,  0,    "x", 3.0, 0.5, 6.5],     // vestibule sidelight (hub daylight)
    [34,    0,    "x", 12,  2,   6],       // living, south
    [28,    6,    "y", 5.0, 2.5, 5],       // living, west
    [29,    20.4, "x", 4.0, 3,   4],       // living, north
    [70,    0,    "x", 8.0, 3,   4.5],     // dining, south
    [85,    10,   "y", 3.0, 2.5, 5],       // dining, east
    [88,    17,   "y", 6.0, 3.5, 4],       // kitchen over the sink, east
    [35,    22,   "y", 3.5, 2.5, 5],       // library, west: desks half
    [35,    29,   "y", 3.5, 2.5, 5],       // reading half
    [91,    31,   "y", 3.0, 4,   3],       // pantry
    [65.5,  60.4, "x", 6.0, 2.5, 5],       // bedroom 2, north
    [74.5,  52,   "y", 4.0, 2.5, 5],       // bedroom 2, east
    [75.5,  43,   "y", 3.0, 3.5, 3.5],     // laundry (dryer vent wall)
    [34.5,  50,   "y", 3.5, 2.5, 5],       // primary
    [34.5,  62.5, "y", 4.5, 2.5, 5],
    [38,    70.4, "x", 4.0, 2.5, 5],       // pulled to the corners: none behind the bed
    [57.5,  70.4, "x", 4.0, 2.5, 5],
    [26,    40,   "y", 3.0, 4,   3],       // ensuite
    [28,    36.4, "x", 3.0, 4,   3],
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: range + tall units on the west (inside) wall, sink run on the east wall under the window,
    // island with no seating, fridge beside the pantry door
    [66.2,  22.6, 68.4,  28.8,  0, 3,    counter],    // range run, west wall
    [66.2,  23.6, 68.2,  26.2,  3, 3.05, dark],       // cooktop
    [70,    26.8, 72.6,  28.8,  0, 7,    steel],      // tall oven column
    [74,    26.6, 76.8,  28.8,  0, 7,    steel],      // fridge, by the pantry door, end of a run
    [72.6,  26.8, 74,    28.8,  0, 3,    counter],
    [85.8,  15,   87.8,  28.8,  0, 3,    counter],    // sink run, east wall
    [86.2,  18.4, 87.6,  22.4,  3, 3.05, basin],      // sink under the east window
    [85.8,  23.4, 87.8,  26,    0, 3,    steel],      // dishwasher
    [72,    17.6, 75.4,  25.6,  0, 3,    counter],    // island: 10 ft aisle to the dishwasher
    // dining: coffee station by the nook
    [83.4,  8,    84.8,  13.6,  0, 3,    counter],
    // pantry
    [79.2,  33,   79.8,  36.4,  0, 7,    shelf],
    [80.4,  36.2, 90.8,  36.8,  0, 7,    shelf],
    [89.4,  29.2, 90.8,  32,    0, 6.5,  steel],      // upright freezer
    // mudroom: lockers, bench, drop shelf
    [66.2,  38.2, 67.4,  40.8,  0, 7,    wood],
    [66.2,  33.6, 67.2,  37.8,  0, 1.5,  wood],
    [68.4,  39.7, 77.6,  40.3,  0, 7,    wood],
    // vestibule: closed coats, bench, drop shelf
    [50.2,  2,    50.8,  6.6,   0, 7,    shelf],
    [58.2,  1.2,  59.4,  6.4,   0, 1.5,  wood],
    [58.9,  1.2,  59.5,  6.4,   3.5, 3.55, wood],
    // powder
    [59.8,  0.4,  61.4,  2,     0, 1.4,  white],
    [64,    0.4,  65.8,  3,     0, 3,    counter],
    // shared bath
    [56.6,  40.4, 58.2,  42,    0, 1.4,  white],
    [50.4,  44,   52,    48,    0, 3,    counter],
    [53.4,  44.6, 58.2,  48,    0, 0.02, tile],       // curbless shower
    // laundry
    [73.9,  41.4, 75.3,  47.8,  0, 3.2,  steel],
    [66.4,  46.2, 72,    47.8,  0, 3,    counter],
    [68,    46.4, 70,    47.5,  3, 3.05, basin],      // laundry sink
    // ensuite: curbless wet zone + vanity + WC
    [26.4,  36.8, 33.4,  40.6,  0, 0.02, tile],
    [26.4,  37,   31,    39.6,  0, 1.6,  white],
    [31.6,  37,   33.2,  40.2,  0, 0.03, tile],
    [26.4,  45.4, 32.4,  47,    0, 3,    counter],
    [36.2,  42,   37.8,  43.6,  0, 1.4,  white],
    // walk-in shelving
    [38.2,  36.6, 38.8,  47.8,  0, 7,    shelf],
    [49.2,  36.6, 49.8,  47.8,  0, 7,    shelf],
    // 1,700 mm turning circles: kitchen, hub, powder, shared bath, laundry, ensuite
    [76,    17.6, 81.6,  23.2,  0, 0.03, circle_c, "", "round"],
    [57,    8,    62.6,  13.6,  0, 0.03, circle_c, "", "round"],
    [60,    0.8,  65.6,  6.4,   0, 0.03, circle_c, "", "round"],
    [52.6,  40.6, 58.2,  46.2,  0, 0.03, circle_c, "", "round"],
    [66.6,  41.8, 72.2,  47.4,  0, 0.03, circle_c, "", "round"],
    [30.4,  41,   36,    46.6,  0, 0.03, circle_c, "", "round"],
    // living: gas fireplace on the north wall (shared with the library)
    [36,    18.6, 42,    20.2,  0, 4,    hearth],
];

function main_furniture() = [
    // dining: 72 in round table for 8, nook table + banquette by the coffee station
    [68,    3,    74,    9,     0, 2.5,  table, "", "round"],
    [78,    7,    81.5,  10.5,  0, 2.5,  table],
    [78,    10.5, 81.7,  11.2,  0, 1.5,  sofa],
    // living: sectional + two swivel chairs, 75 in TV on the north wall
    [32,    8,    40,    11,    0, 2.6,  sofa],
    [32,    11,   35,    16,    0, 2.6,  sofa],
    [43,    6,    45.8,  8.8,   0, 2.6,  sofa],
    [43,    11,   45.8,  13.8,  0, 2.6,  sofa],
    [37,    4.5,  40.5,  7.2,   0, 1.5,  table],
    [43,    19,   47,    20.2,  0, 2,    wood],
    // library: desks end (south), reading end (north)
    [36,    21,   42,    23,    0, 2.5,  wood],
    [36,    34.4, 38,    36,    0, 6,    shelf],
    [43,    32,   47,    35,    0, 2.6,  sofa],
    // bedroom 2 (queen) and its wardrobe wall
    [66.5,  49,   71.5,  55.5,  0, 2,    bed],    // headboard on the south wall
    [62.2,  54,   63.4,  59.6,  0, 7,    shelf],
    // primary: king bed with 3 ft+ around it
    [47,    66,   53.3,  70,    0, 2,    bed],
    [44.5,  67,   46.5,  69,    0, 2,    wood],
    [54,    67,   56,    69,    0, 2,    wood],
    [49,    52,   53,    53.5,  0, 1.5,  wood],
    [36,    58,   39.5,  61.5,  0, 2.5,  sofa],
    [44,    49.2, 50,    50.7,  0, 2.5,  wood],
    [56.5,  60,   61,    65.5,  0, 2.5,  table],
];

// steps from the porches down to grade [x, y, direction, width]: four 6 in risers
function main_porch_steps() = [
    [55,    -8,   "-y", 4.0],
];

// porch posts [x, y, height]
function main_posts() = [
    [50.4, -7.6, 9.5], [59.6, -7.6, 9.5],
    [96.6, 1.4, 9.5], [96.6, 10.6, 9.5],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [28,    0,    50,    20.4, 10,  0.333, 1.5],   // living
    [50,    0,    66,    33,   10,  0.333, 1.5],   // hub core
    [66,    0,    88,    29,   10,  0.333, 1.5],   // dining + kitchen
    [66,    29,   91,    40.5, 10,  0.333, 1.5],   // mudroom + pantry
    [35,    20.4, 50,    36.4, 10,  0.333, 1.5],   // library
    [26,    33,   75.5,  70.4, 10,  0.333, 1.5],   // quiet wing
    [79,    37,   103,   61,   8.5, 0.333, 1.0],   // garage
    [50,    -8,   60,    0,    9.5, 0.25,  0.5],
    [85,    1,    97,    11,   9.5, 0.25,  0.5],   // covered patio
    [52,    9,    64,    26,   11.5, 0.2,  0.3],   // raised hub roof: clerestory band
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

