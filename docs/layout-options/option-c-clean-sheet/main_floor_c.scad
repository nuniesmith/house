// OPTION C - CLEAN SHEET INSIDE THE SAME ENVELOPE (main floor variant).
// Re-planned from Kayla's notes outward; NOT a trace of models/main_floor.scad.
// Units: feet, x = east, y = north, rooms are wall-centre-line rectangles,
// door/window x,y = the LOW end of the opening. Same coordinates, basement
// (x 22.16-103.04, y 5.79-63.16), stair box (x 42.65-47.27) and house_lib as
// the current model. Visualisation only - NOT construction documents.
//
// THE PLAN IN ONE PARAGRAPH
//   South band (road side): garage (x 0-22.16, ONE 16 ft door facing SOUTH),
//   mudroom + pantry (Costco door to the garage), kitchen, dining, vestibule +
//   foyer, living room, sun room (SE). North-west quiet zone over the basement:
//   den, library, office, reached by a short gallery that also carries the
//   stair landing. Private wing north-east: hall H1 (N-S) from the foyer, hall
//   H4 (E-W), bedroom 2 (east light) with its own bath, bedroom 3, hall bath,
//   and the master suite on the north wall (WIC + laundry + bath back to back).
// CHANGES vs the current model: see PROS-CONS.md section 2 / 9. In short:
//   - footprint x 0-108 x y 0-63.42 (was 0-128 x 1.25-66.64); garage 22.16 x 26
//   - STAIR (CODE-01): 18 + 4 risers, landing 4.4 ft at the basement (as Option
//     A, basement_c.scad); main-floor top landing 4.62 x 5.0 ft (CODE-07)
//   - the west drive is not used: garage door faces south (site departure)
//   - no basement shell change; crawl wings W and E are not needed (departure)

use <../../../models/house_lib.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
show_furniture = true;
audit = false;         // echo the tables for the layout checker

let ($cut = undef) main_level(show_roof, roof_color, roof_opacity, show_furniture, audit, false);

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
table    = [0.66, 0.50, 0.34];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    // ---- south band: garage, service strip, kitchen, dining, entry, living
    ["GARAGE",          0,      0,     22.16, 26,    10, "garage", -1.5],
    ["MUDROOM",         22.16,  0,     34,    13,    10, "utility", 0, "", [27.5, 6, 1.1]],
    [["SCULLERY /", "PANTRY"], 22.16, 13, 34, 26,    10, "utility", 0, "", [27.6, 19.5, 1.0]],
    ["KITCHEN",         34,     0,     54,    26,    12, "kitchen", 0, "", [44, 13, 1.7]],
    ["DINING",          54,     0,     66,    26,    12, "dining", 0, "", [60, 13, 1.4]],
    ["VESTIBULE",       66,     0,     78,    7,     10, "hall", 0, "", [72, 3.5, 0.8]],
    ["FOYER",           66,     7,     78,    28,    12, "hall", 0, "", [72, 17, 1.5]],
    ["LIVING ROOM",     78,     0,     94,    28,    12, "living", 0, "", [86, 14, 1.8]],
    ["SUN ROOM",        94,     0,     108,   22,    10, "living", 0, "", [101, 11, 1.3]],
    // ---- north-west quiet zone (over the basement's west half)
    ["DEN",             22.16,  26,    42.65, 47.1,  10, "living", 0, "", [32.4, 36.5, 1.6]],
    ["BUTLER",          42.65,  26,    60,    35.46, 10, "utility", 0, "", [51.3, 30.5, 1.0]],
    ["STAIR DN",        42.65,  35.46, 47.27, stair_top_y(), 0, "stairwell", 0, "", [44.95, 39.0, 0.8, 90]],
    ["STORAGE",         47.27,  35.46, 60,    stair_top_y(), 10, "closet", 0, "", [53.6, 41.3, 1.0]],
    ["POWDER",          60,     26,    66,    33,    10, "bath", 0, "", [63, 29.5, 0.7]],
    ["COATS",           60,     33,    66,    40,    10, "closet", 0, "", [63, 36.5, 0.7]],
    ["BROOM",           60,     40,    66,    stair_top_y(), 10, "closet", 0, "", [63, 43.5, 0.7]],
    // ---- halls
    ["H1",              66,     28,    72,    52.1,  10, "hall", 0, "", [69, 40, 0.9, 90]],
    ["",                22.16,  stair_top_y(), 42.65, 52.1, 10, "hall"],              // gallery, west
    ["",                42.65,  stair_top_y(), 47.27, 52.1, 10, "hall"],              // stair-top landing
    ["GALLERY",         47.27,  stair_top_y(), 66, 52.1, 10, "hall", 0, "", [56.6, 49.6, 1.0]],
    ["H4",              72,     37,    94,    42,    10, "hall", 0, "", [83, 39.5, 1.0]],
    // ---- quiet rooms on the north wall
    ["LIBRARY",         22.16,  52.1,  42.65, 63.42, 10, "office", 0, "", [32.4, 57.8, 1.4]],
    ["OFFICE",          42.65,  52.1,  60,    63.42, 10, "office", 0, "", [51.3, 57.8, 1.2]],
    // ---- private wing
    ["BEDROOM 3",       60,     52.1,  72,    63.42, 10, "bed", 0, "", [66, 57.8, 1.0]],
    ["LINEN",           72,     28,    78,    37,    10, "closet", 0, "", [75, 32.5, 0.7]],
    ["BATH",            78,     28,    88,    37,    10, "bath", 0, "", [83, 32.5, 0.9]],
    ["CLOSET",          88,     28,    94,    37,    10, "closet", 0, "", [91, 32.5, 0.7]],
    ["BEDROOM 2",       94,     28,    108,   42,    10, "bed", 0, "", [101, 35, 1.3]],
    ["BATH 2",          94,     22,    108,   28,    10, "bath", 0, "", [101, 25, 0.9]],
    [["MASTER", "BEDROOM"], 88, 42,    108,   63.42, 10, "bed", 0, "", [98, 56, 1.6]],
    [["MASTER", "LAUNDRY"], 72, 42,    80,    52,    10, "utility", 0, "", [76, 47, 0.7]],
    ["WIC",             80,     42,    88,    52,    10, "closet", 0, "", [84, 47, 0.9]],
    [["MASTER", "BATH"], 72,    52,    88,    63.42, 10, "bath", 0, "", [80, 57.7, 1.2]],
    // ---- porches (no walls)
    ["FRONT PORCH",     34,    -10,    108,   0,     0, "porch", 0, "", [70, -5, 1.8]],
    [["MUD", "STOOP"],  22.16, -6,     34,    0,     0, "porch", 0, "", [28, -3, 0.8]],
    ["PATIO",           108,    0,     120,   22,    0, "porch", 0, "", [114, 11, 1.1]],
    [["MASTER", "PORCH"], 108,  44,    118,   56,    0, "porch", 0, "", [113, 50, 1.0]],
    ["DECK",            108,    22,    118,   44,    0, "porch", 0, "", [113, 33, 1.0, 90]],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    // ---- exterior
    [4,      0,     "x", 16,  "garage"],           // ONE 16 ft garage door, south wall
    [27,     0,     "x", 3.0, "door",    1],       // mudroom to its stoop
    [70.5,   0,     "x", 3.0, "door",    1],       // front door (vestibule)
    [68.3,   0,     "x", 2.0, "glass"],            //   sidelights
    [73.5,   0,     "x", 2.0, "glass"],
    [57,     0,     "x", 6.0, "double",  1],       // dining to the porch (outdoor dining)
    [49,     0,     "x", 3.0, "door",    1],       // kitchen to the porch (BBQ)
    [82,     0,     "x", 6.0, "double",  1],       // living room to the porch
    [108,    8,     "y", 5.0, "double",  1],       // sun room to the patio
    [108,    47,    "y", 5.0, "double",  1],       // master bedroom to its porch
    [108,    38,    "y", 3.0, "door",    1],       // bedroom 2 to the east deck (private access, K-240)
    // ---- garage, mudroom, pantry, kitchen
    [22.16,  4,     "y", 3.0, "door",    1],       // garage to the mudroom
    [22.16,  17,    "y", 3.0, "door",    1],       // COSTCO DOOR: garage to the pantry
    [29,     13,    "x", 3.0, "door",   -1],       // mudroom to the pantry
    [34,     2,     "y", 3.0, "door",    1],       // mudroom to the kitchen
    [34,     16,    "y", 3.0, "door",    1],       // pantry to the kitchen
    [27,     26,    "x", 3.0, "door",    1],       // pantry to the den: a route from the garage that skips the kitchen (K-330)
    [54,     6,     "y", 14,  "full"],             // kitchen / dining (broken open)
    [36,     26,    "x", 6.0, "full"],             // kitchen / den
    [44,     26,    "x", 3.0, "door",    1],       // kitchen to the butler's pantry
    [66,     10,    "y", 8.0, "full"],             // dining / foyer
    [69,     7,     "x", 6.0, "double",  1],       // vestibule to foyer
    [78,     10,    "y", 10,  "full"],             // foyer / living room
    [94,     6,     "y", 12,  "full"],             // living room / sun room (glass partition)
    // ---- halls, powder room, coats, stair
    [66,     28,    "x", 6.0, "full"],             // foyer / H1
    [66,     28.5,  "y", 3.0, "door",   -1],       // H1 to the powder room
    [66,     34,    "y", 3.0, "door",   -1],       // H1 to the coat closet
    [66,     41,    "y", 3.0, "door",   -1],       // H1 to the broom closet
    [66,     47.6,  "y", 4.0, "full"],             // H1 / gallery
    [47.27,  47.4,  "y", 4.4, "full"],             // gallery / stair landing
    [42.65,  47.4,  "y", 4.4, "full"],             // stair landing / west gallery
    [42.9,   stair_top_y(), "x", 4.1, "full"],     // top of the stair
    [49,     stair_top_y(), "x", 3.0, "door",   -1],  // gallery to the storage room
    [30,     stair_top_y(), "x", 3.0, "door",   -1],  // west gallery to the den
    [30,     52.1,  "x", 3.0, "door",    1],       // west gallery to the library
    [50,     52.1,  "x", 3.0, "door",    1],       // gallery to the office
    [61,     52.1,  "x", 3.0, "door",    1],       // gallery to bedroom 3
    // ---- private wing
    [72,     37.5,  "y", 4.0, "full"],             // H1 / H4
    [79,     37,    "x", 3.0, "door",   -1],       // H4 to the bath
    [73,     37,    "x", 3.0, "door",   -1],       // H4 to the linen closet
    [89,     37,    "x", 3.0, "door",   -1],       // H4 to the closet
    [94,     38.5,  "y", 3.0, "door",    1],       // H4 to bedroom 2
    [97,     28,    "x", 3.0, "door",   -1],       // bedroom 2 to its bath
    [73,     42,    "x", 3.0, "door",    1],       // H4 to the master laundry
    [89.5,   42,    "x", 3.0, "door",    1],       // H4 to the master bedroom
    [80,     44,    "y", 3.0, "door",   -1],       // WIC to the laundry (K-036: through the closet)
    [88,     43.5,  "y", 3.0, "door",   -1],       // master bedroom to the WIC
    [81,     52,    "x", 3.0, "door",    1],       // WIC to the master bath
    [88,     55,    "y", 3.0, "door",   -1],       // master bedroom to the master bath
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [38.5,   0,     "x", 7.0, 3.5, 4],       // kitchen, over the sink
    [89.5,   0,     "x", 3.9, 2,   6],       // living room
    [95.5,   0,     "x", 5.0, 1.5, 6.5],     // sun room
    [102.5,  0,     "x", 4.5, 1.5, 6.5],
    [108,    1.5,   "y", 5.0, 1.5, 6.5],
    [108,    15,    "y", 5.0, 1.5, 6.5],
    [22.16,  29,    "y", 6.0, 2.5, 5],       // den
    [22.16,  55,    "y", 5.0, 2.5, 5],       // library
    [28,     63.42, "x", 6.0, 2.5, 5],
    [46,     63.42, "x", 6.0, 2.5, 5],       // office
    [67.4,   63.42, "x", 3.6, 2.5, 5],       // bedroom 3
    [74,     63.42, "x", 3.5, 4,   3],       // master bath
    [92,     63.42, "x", 5.0, 2.5, 5],       // master bedroom
    [101,    63.42, "x", 5.0, 2.5, 5],
    [108,    58,    "y", 4.0, 2.5, 5],
    [108,    29,    "y", 4.5, 2.5, 5],       // bedroom 2, east light
    [108,    33.8,  "y", 3.0, 2.5, 5],
    [108,    23.5,  "y", 3.0, 4,   3],       // bath 2
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: sink run under the south window, range wall west, island, fridge by the pantry
    [37.5,   0.4,   47.5,  2.4,   0, 3,    counter],
    [40,     0.6,   43,    2.2,   3, 3.05, basin],      // sink
    [45,     0.6,   47,    2.4,   0, 3,    steel],      // dishwasher beside the sink
    [34.4,   6,     36.4,  14.5,  0, 3,    counter],
    [34.5,   8.5,   36.2,  11.5,  3, 3.05, dark],       // range
    [34.4,   20.6,  36.9,  24,    0, 7,    steel],      // fridge (at a run end, by the pantry)
    [38,     23.4,  54,    25.6,  0, 3,    counter],    // north run, tall cabinets at the ends
    [40,     10,    50,    15.5,  0, 3,    wood],       // island
    [34.4,   24.1,  36.9,  25.6,  0, 7,    wood],
    // pantry
    [22.5,   13.4,  24.6,  16.6,  0, 7,    shelf],
    [22.5,   20.4,  24.6,  25.6,  0, 7,    shelf],
    [31.5,   20.5,  33.6,  23.5,  0, 6,    steel],      // upright freezer
    [30.2,   23.8,  33.6,  25.6,  0, 3,    counter],
    // mudroom: lockers, bench
    [22.5,   9,     24.1,  12.6,  0, 7,    wood],
    [24.4,   11.2,  28.6,  12.6,  0, 3,    wood],
    [31.5,   0.4,   33.6,  4,     0, 7,    shelf],
    // butler's pantry
    [43,     34,    59.6,  35.1,  0, 3,    counter],
    [47.6,   27,    59.6,  28.6,  0, 7,    shelf],
    // powder room
    [60.5,   29.5,  62.3,  31.5,  0, 1.4,  white],
    [60.4,   26.4,  62.4,  28.0,  0, 3,    counter],
    // coats, broom
    [60.3,   33.3,  62,    39.7,  0, 7,    shelf],
    [60.3,   40.3,  62,    46.8,  0, 7,    shelf],
    // storage
    [47.6,   35.8,  49,    46.8,  0, 7,    shelf],
    [58.4,   35.8,  59.7,  46.8,  0, 7,    shelf],
    // foyer: bench and closed storage; vestibule: coat wall
    [66.4,   8,     67.8,  17,    0, 1.5,  wood],
    [66.4,   17,    68.4,  26.5,  0, 7,    shelf],
    [66.4,   0.4,   67.8,  6.6,   0, 7,    shelf],
    [76.4,   0.4,   77.6,  6.6,   0, 3,    wood],       // vestibule drop shelf
    [76.4,   22,    77.7,  27.5,  0, 3,    wood],       // foyer: mail / key drop
    // living room hearth
    [87,     26.6,  92,    27.6,  0, 4,    hearth],
    // hall bath, bath 2
    [86,     30,    87.8,  32,    0, 1.4,  white],
    [78.4,   28.4,  83,    30.4,  0, 0.02, tile],       // curbless shower (recessed pan)
    [84,     35,    87.6,  36.6,  0, 3,    counter],
    [94.4,   23,    96.4,  25,    0, 1.4,  white],
    [97.4,   22.4,  101,   24,    0, 3,    counter],
    [102,    22.4,  107.6,  26,   0, 0.02, tile],
    // linen, closet
    [72.4,   28.4,  73.8,  33.6,  0, 7,    shelf],
    [88.4,   28.4,  89.8,  33.6,  0, 7,    shelf],
    // bedroom 2 wardrobe on the interior wall, bedroom 3 wardrobe
    [94.4,   29,    95.8,  37.4,  0, 7,    shelf],
    [71,     52.5,  71.6,  62,    0, 7,    shelf],
    // master laundry: washer + dryer raised, sink, counter
    [74.6,   49.6,  79.6,  51.6,  0, 3.2,  steel],
    [72.4,   46.2,  74.2,  49,    0, 3,    counter],
    [72.5,   47,    74.1,  48.6,  3, 3.05, basin],
    // master WIC
    [80.4,   42.4,  81.6,  51.6,  0, 7,    shelf],
    [86.4,   47,    87.6,  51.6,  0, 7,    shelf],
    [82,     50.2,  86,    51.6,  0, 7,    shelf],
    // master bath: curbless shower, tub on the interior wall, vanity, two WCs
    [72.4,   53,    78.4,  58,    0, 0.02, tile],       // shower pan (curbless)
    [72.4,   59,    78,    63,    0, 2,    white],      // tub
    [80,     61.6,  86.8,  63.1,  0, 3,    counter],    // double vanity
    [86.6,   53.2,  87.6,  55,    0, 1.4,  white],
    // great room, den, library, office: shelving and hearth
    [31,     26.5,  35.5,  27.8,  0, 3,    wood],
    [22.6,   52.5,  24.2,  62.6,  0, 7,    shelf],
    [24.2,   62,    41.8,  63.1,  0, 7,    shelf],
];

// furniture
function main_furniture() = [
    [48.5,   18.5,  52.5,  24,    0, 2.6,  sofa],       // breakfast banquette
    [46,     16.5,  52,    20,    0, 2.5,  table],
    [58,     8,     64,    18,    0, 2.5,  table],      // dining table (seats 8)
    [80,     3,     92,    9,     0, 2.6,  sofa],       // living room sectional
    [80,     9,     84,    18,    0, 2.6,  sofa],
    [86,     13,    90,    17,    0, 1.5,  table],
    [82,     21,    86,    25,    0, 2.6,  sofa],
    [96,     4,     105,   9,     0, 2.6,  sofa],       // sun room
    [100,    12,    106,   17,    0, 2.5,  table],
    [24,     30,    32,    35,    0, 2.6,  sofa],       // den
    [34,     40,    40,    44,    0, 2.6,  sofa],
    [25,     56,    35,    59,    0, 2.5,  table],      // library reading
    [44,     55.5,  55,    58.5,  0, 2.5,  wood],       // office desk
    [96,     43,    102.5, 49.5,  0, 2.0,  bed],        // master bed (head on the south wall, no window behind it, K-306)
    [96,     60,    104,   63,    0, 2.5,  wood],
    [98,     29,    104.5, 35.5,  0, 2,    bed],        // bedroom 2 (head on the south wall)
    [60.5,   56,    66.5,  62,    0, 2,    bed],        // bedroom 3 (head on the west wall)
];

// steps from the porches down to grade [x, y, direction, width]
function main_porch_steps() = [
    [68,   -10, "-y", 8.0],     // front entry
    [24,   -6,  "-y", 8.0],     // mud stoop
    [108,  4,   "+x", 8.0],     // patio, east
    [118,  27,  "+x", 8.0],     // east deck
];
// garage steps up to the house [y0, y1]: Costco door (pantry) and the mudroom door
function garage_steps() = [[3.5, 7.5], [16.5, 20.5]];

// porch posts [x, y, height]
function main_posts() = [
    [34.5, -9.5, 9.5], [50, -9.5, 9.5], [66, -9.5, 9.5], [78, -9.5, 9.5], [92, -9.5, 9.5], [107.5, -9.5, 9.5],
    [22.7, -5.5, 9.5], [33.5, -5.5, 9.5],
    [119.5, 0.5, 10], [119.5, 21.5, 10],
    [117.5, 44.5, 10], [117.5, 55.5, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,      0,     22.16, 26,    8.5, 0.5,   1.5],   // garage
    [22.16,  0,     108,   63.42, 10,  0.5,   1.5],   // house
    [34,    -10,    108,   0,     9.5, 0.333, 1],     // front porch
    [22.16, -6,     34,    0,     9.5, 0.333, 1],     // mud stoop
    [108,    0,     120,   22,    10,  0.333, 1],     // patio
    [108,    44,    118,   56,    10,  0.333, 1],     // master porch
];

// The main floor assembly (trusses + subfloor) under the heated rooms,
// with the stair opening left out; it shows in sections and as the rim
// above the foundation.
module floor_assembly(rooms) {
    paint(floor_frame())
        difference() {
            union()
                for (r = rooms)
                    if (r[6] != "porch" && r[6] != "garage" && r[6] != "stairwell")
                        translate([r[1] - wall_t() / 2, r[2] - wall_t() / 2, -main_floor_depth()])
                            cube([r[3] - r[1] + wall_t(), r[4] - r[2] + wall_t(), main_floor_depth() - 0.15]);
            // (0.01 inside the wall faces: a cut face that coincides with a
            // visible face takes this part's colour in the preview)
            translate([stair_x()[0] + wall_t() / 2 + 0.01, 35.46 + wall_t() / 2 + 0.01, -5])
                cube([stair_x()[1] - stair_x()[0] - wall_t() - 0.02, stair_top_y() - 35.46 - wall_t() / 2 - 0.01, 10]);
        }
}


// ---- the two-flight stair (CODE-01) -----------------------------------------
// 22 risers of 7.5 in: flight 1 = 18 risers (3,429 mm) south from the unchanged top
// nosing (y 47.1) to a 4.4 ft landing at 11.25 ft below this floor, then a 90-degree
// turn east and flight 2 = 4 risers (762 mm). Same geometry as Option A's tested
// stair (basement_c.scad draws the same module at the basement).
function sc_rise() = floor_to_floor() / 22;
function sc_run()  = 10.5 / 12;
function sc_n1()   = 18;
function sc_land_y() = [27.8, stair_top_y() - (sc_n1() - 1) * sc_run()];
module main_stair_c(z_main = 0, y_box = 45.34) {
    x0 = stair_x()[0] + wall_t() / 2;
    x1 = stair_x()[1] - wall_t() / 2;
    zb = z_main - floor_to_floor();
    paint(stair_color())
        for (i = [1 : sc_n1() - 1]) {
            ya = stair_top_y() - i * sc_run();
            z = z_main - i * sc_rise();
            zf = ya + sc_run() / 2 > y_box ? z_main - main_floor_depth() - 0.125 : zb;
            translate([x0, ya, zf]) cube([x1 - x0, sc_run() + 0.08, z - zf]);
        }
    zl = z_main - sc_n1() * sc_rise();
    paint(stair_color()) translate([x0, sc_land_y()[0], zb]) cube([x1 - x0, sc_land_y()[1] - sc_land_y()[0], zl - zb]);
    paint(stair_color())
        for (j = [1 : 3])
            translate([x1 + (j - 1) * sc_run(), sc_land_y()[0], zb])
                cube([sc_run() + 0.02, sc_land_y()[1] - sc_land_y()[0], zl - j * sc_rise() - zb]);
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

    // the stair down to the basement (its lower part runs under the hall)
    if (show_stair) main_stair_c();
    // garage steps up to the house (hall) and to the side entry: a landing
    // at house level and two steps, from the garage slab 1.5 ft below
    for (y = garage_steps())
        paint(stair_color()) {
            translate([19.82, y[0], -1.5]) cube([2.34, y[1] - y[0], 1.5]);
            translate([18.62, y[0], -1.5]) cube([1.2, y[1] - y[0], 1.0]);
            translate([17.42, y[0], -1.5]) cube([1.2, y[1] - y[0], 0.5]);
        }

    for (p = main_posts()) post(p[0], p[1], p[2]);
    for (p = main_porch_steps()) porch_steps(p[0], p[1], p[2], p[3]);

    if (show_roof) roofs(main_roof(), roof_color, roof_opacity);
}
