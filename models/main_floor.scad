// Main floor - OpenSCAD model of the main level.
// Units: feet. Visualisation only - NOT construction documents.
//
// Traced from docs/house/main_floor.jpg (the November 2026 redesign) at
// 15.2 px per ft: rooms are wall-centre-line rectangles, read to about
// +/- 0.3 ft. x = east, y = north; x = 0 is the garage's west wall and
// y = 0 the front wall of the den and the breakfast bay. The basement
// (basement.scad) uses the same coordinates.
//
// One change from the drawing (docs/house/Redesign-and-Spec-2026-11-02.md
// has the details): the two plans had the
// stair entered from the south on both levels, which no straight stair
// can do, and it was too short for any basement. The stair now starts
// in the upper hall (north end) and runs 15 3/4 ft south, under the
// main hall, to the basement hallway; the opening reaches 1.6 ft into
// the upper hall for headroom, and its south end is walled off.

use <house_lib.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
show_furniture = true;
audit = false;         // echo the tables for the layout checker

// no section cut when this file is opened on its own ($cut is a special
// variable, so house_combined.scad's value reaches these modules)
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
table    = [0.66, 0.50, 0.34];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    // ---- garage and the service side
    ["GARAGE",          0,     1.25,  24.34, 35.46, 10, "garage", -1.5],
    [["SIDE", "ENTRY"], 24.34, 13.39, 35.6,  20.82, 0,  "porch", 0, "", [30, 17.3, 1.3]],
    ["SCULLERY",        24.34, 20.82, 35.6,  29.51, 12, "utility", 0, "", [30, 25.3, 1.3]],
    ["MUDROOM",         22.1,  35.46, 37.3,  40.56, 10, "utility", 0, "", [32.4, 36.2, 1.0]],
    ["LAUNDRY",         22.1,  40.56, 37.3,  49.64, 10, "utility", 0, "", [28.6, 45.3, 1.3]],
    // ---- bedroom 2 suite and the bunk room
    ["BEDROOM 2",       7.27,  35.46, 22.1,  48.13, 10, "bed", 0, "", [14.7, 46.4, 1.5]],
    ["",                13.78, 48.13, 22.1,  53.75, 10, "hall"],   // suite entry
    ["",                13.78, 53.75, 17.5,  55.3,  0,  "hall"],
    ["WIC",             7.27,  48.13, 13.78, 51.15, 10, "closet", 0, "", [10.5, 48.9, 0.8]],
    ["WC",              7.27,  51.15, 13.78, 55.3,  10, "bath", 0, "", [11.6, 54.4, 0.8]],
    ["BATH 2",          7.27,  55.3,  17.5,  62.04, 10, "bath", 0, "", [13.2, 57.3, 1.1]],
    ["BUNK ROOM",       17.5,  53.75, 32.6,  66.64, 10, "bed", 0, "", [25.6, 59.5, 1.4]],
    ["STUDY",           32.6,  53.75, 42.65, 63.42, 10, "office", 0, "", [38.2, 61.6, 1.3]],
    // ---- halls and the stair
    ["HALL",            22.1,  49.64, 42.65, 53.75, 10, "hall", 0, "", [33, 51.7, 1.1]],
    ["",                37.3,  35.46, 42.65, 49.64, 10, "hall"],
    ["STAIR DN",        42.65, 35.46, 47.27, stair_top_y(), 0, "stairwell", 0, "", [44.95, 39.0, 0.8, 90]],
    ["",                42.65, stair_top_y(), 47.27, 50.69, 0, "hall"],   // landing at the stair top
    ["",                47.27, 45.39, 53.95, 50.69, 10, "hall"],   // upper hall, west of its door
    ["HALL",            53.95, 45.39, 69.14, 50.69, 10, "hall", 0, "", [64.6, 48.1, 1.1]],
    ["BATH",            47.27, 35.46, 53.95, 45.39, 10, "bath", 0, "", [50.2, 42.5, 1.0]],
    [["FLEX", "ROOM"],  53.95, 35.46, 69.14, 45.39, 10, "office"],
    ["SITTING ROOM",    42.65, 50.69, 53.95, 63.42, 10, "living", 0, "", [49.75, 54.55, 0.8]],
    [["BREAKFAST", "NOOK"], 53.95, 50.69, 69.14, 63.42, 10, "dining", 0, "", [61.3, 54.2, 1.3]],
    ["HALL",            24.34, 29.51, 105.2, 35.46, 10, "hall", 0, "", [61, 33.2, 1.3]],
    // ---- great room, kitchen, front rooms
    ["GREAT ROOM",      69.14, 35.46, 95.63, 52.53, 12, "living", 0, "", [83, 48.6, 2]],
    [["KITCHEN /", "DINING"], 35.6, 6.28, 69.14, 29.51, 12, "kitchen", 0, "", [52.5, 25.4, 1.6]],
    ["BREAKFAST",       54.1,  0,     69.14, 6.28,  10, "dining", 0, "", [64.7, 3.9, 1.0]],
    ["FOYER",           69.14, 3.72,  81.12, 29.51, 12, "hall", 0, "", [76.3, 21, 1.6]],
    ["DEN",             81.12, 0,     95.95, 29.51, 12, "living", 0, "", [88.5, 21.5, 2]],
    ["",                95.95, 9.31,  99.7,  20.56, 10, "living"],          // den alcove
    // ---- office and the master suite
    ["OFFICE",          95.63, 35.46, 108.62, 48.16, 10, "office", 0, "", [102.1, 46.3, 1.3]],
    [["MASTER", "BEDROOM"], 108.62, 29.51, 126.97, 52.86, 10, "bed", 0, "", [117.8, 48.2, 1.6]],
    ["",                105.2, 29.51, 108.62, 35.46, 10, "hall"],          // master entry
    ["WIC",             95.95, 20.56, 106.51, 29.51, 10, "closet", 0, "", [101.2, 25.1, 1.2]],
    ["",                106.51, 20.56, 111.41, 29.51, 10, "hall"],         // closet passage
    ["WIC",             111.41, 20.56, 121.94, 29.51, 10, "closet", 0, "", [116.7, 25.1, 1.2]],
    ["LINEN",           121.94, 20.56, 128.13, 29.51, 10, "closet", 0, "", [123.9, 25.1, 0.8, 90]],
    [["MASTER", "BATH"], 106.51, 9.31, 128.13, 20.56, 10, "bath", 0, "", [117, 16, 1.3]],
    ["WC",              99.7,  16.71, 106.51, 20.56, 10, "bath", 0, "", [104.9, 19.6, 0.7]],
    ["",                99.7,  13.09, 106.51, 16.71, 10, "closet"],         // linen between the WCs
    ["WC",              99.7,  9.31,  106.51, 13.09, 10, "bath", 0, "", [104.9, 12.3, 0.7]],
    // ---- porches (no walls)
    ["FRONT PORCH",     49.24, -15.26, 101.41, 0,    0, "porch", 0, "", [61, -9, 1.8]],
    ["",                49.24, 0,      54.1,   6.28, 0, "porch"],
    ["",                95.95, 0,      101.41, 9.31, 0, "porch"],
    ["",                69.14, 0,      81.12,  3.72, 0, "porch"],          // covered entry
    ["DECK",            69.14, 52.53,  95.63,  64.7, 0, "porch", 0, "", [82.4, 58.6, 2]],
    [["OFFICE", "PORCH"], 95.63, 48.16, 108.62, 59.47, 0, "porch", 0, "", [102.1, 54.3, 1.3]],
    [["MASTER", "PORCH"], 108.62, 52.86, 126.97, 62.4, 0, "porch", 0, "", [117.8, 57.6, 1.4]],
    [["SIDE", "PORCH"], 126.97, 29.51, 137.66, 59.47, 0, "porch", 0, "", [132.3, 44.4, 1.4]],
    ["",                128.13, 26.84, 137.66, 29.51, 0, "porch"],
    ["",                36.6,  63.42,  41.2,   66.6, 0, "porch"],           // study stoop
    ["",                1.7,   35.46,  7.27,   38.6, 0, "porch", -2],       // garage side-door pad
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    // ---- exterior
    [72.0,   3.72,  "x", 6.2,  "double",  1],      // front door
    [69.6,   3.72,  "x", 2.0,  "glass"],           //   sidelights
    [78.6,   3.72,  "x", 2.0,  "glass"],
    [63.8,   0,     "x", 5.0,  "double",  1],      // breakfast bay to the front porch
    [37.0,   63.42, "x", 3.75, "double",  1],      // study to its stoop
    [99.0,   48.16, "x", 6.5,  "double",  1],      // office to the office porch
    [114.1,  52.86, "x", 6.05, "double",  1],      // master bedroom to the master porch
    [0,      4.97,  "y", 16,   "garage"],          // side-load garage doors
    [0,      22.86, "y", 9,    "garage"],
    [2.43,   35.46, "x", 2.8,  "door",    1],      // garage side door
    [24.34,  16.1,  "y", 3.0,  "door",   -1],      // garage to the side entry
    // ---- service side
    [24.34,  31.9,  "y", 3.0,  "door",    1],      // garage to the hall (mud entry)
    [35.6,   23.3,  "y", 3.0,  "door",   -1],      // kitchen to the scullery
    [24.6,   35.46, "x", 12.4, "full"],            // mudroom / hall
    [24.8,   40.56, "x", 2.8,  "door",   -1],      // laundry to the mudroom
    [25.0,   49.64, "x", 2.7,  "door",   -1],      // laundry from the bedroom hall
    // ---- bedroom wing
    [22.1,   50.0,  "y", 2.8,  "door",   -1],      // bedroom 2 suite
    [14.0,   48.13, "x", 7.9,  "full"],            //   suite entry / bedroom
    [13.9,   53.75, "x", 3.5,  "full"],            //   the entry's two pieces
    [14.3,   55.3,  "x", 2.6,  "door",   -1],      //   bath 2
    [13.78,  51.35, "y", 2.35, "door",   -1],      //   WC
    [7.6,    48.13, "x", 5.9,  "open"],            //   closet (sliding doors)
    [17.5,   56.2,  "y", 2.4,  "door",   -1],      // bunk room to bath 2 (shared bath)
    [29.4,   53.75, "x", 2.8,  "door",    1],      // bunk room
    [33.0,   53.75, "x", 2.7,  "door",    1],      // study
    [37.5,   49.64, "x", 5.0,  "full"],            // bedroom hall / north-south hall
    [37.6,   35.46, "x", 4.8,  "full"],            // north-south hall / main hall
    // ---- stair and the upper hall
    [42.65,  47.15, "y", 2.4,  "door",    1],      // north-south hall to the stair landing
    [42.9,   stair_top_y(), "x", 4.1, "full"],     // top of the stair
    [47.27,  47.3,  "y", 3.2,  "full"],            // stair landing / upper hall
    [53.95,  45.75, "y", 2.7,  "door",   -1],      // upper hall door (sitting room / nook line)
    [69.14,  45.6,  "y", 4.9,  "full"],            // upper hall / great room
    [47.8,   45.39, "x", 2.9,  "door",   -1],      // hall bath
    [58.3,   45.39, "x", 6.5,  "slider"],          // flex room (glass sliders)
    [47.5,   50.69, "x", 5.9,  "double",  1],      // sitting room
    [53.95,  53.9,  "y", 4.9,  "double",  1],      // sitting room / nook
    [58.55,  50.69, "x", 6.0,  "double", -1],      // nook
    // ---- main hall, kitchen, front rooms
    [38.2,   29.51, "x", 4.0,  "full"],            // hall / kitchen
    [48.9,   29.51, "x", 5.9,  "full"],
    [54.4,   6.28,  "x", 14.5, "full"],            // kitchen / breakfast bay
    [71.4,   29.51, "x", 7.9,  "full"],            // hall / foyer
    [69.4,   35.46, "x", 26.0, "full"],            // hall / great room
    [81.12,  12.66, "y", 5.0,  "double",  1],      // foyer / den
    [95.95,  9.6,   "y", 10.7, "full"],            // den / alcove
    // ---- office and the master suite
    [99.3,   35.46, "x", 4.7,  "double",  1],      // office
    [105.2,  29.95, "y", 4.6,  "double",  1],      // master suite
    [108.62, 29.8,  "y", 5.4,  "full"],            //   entry / bedroom
    [108.9,  29.51, "x", 2.3,  "open"],            //   bedroom / closet passage
    [106.51, 23.6,  "y", 2.9,  "door",   -1],      //   west closet
    [111.41, 23.6,  "y", 2.9,  "door",    1],      //   east closet
    [107.1,  20.56, "x", 2.7,  "door",   -1],      //   master bath
    [122.6,  20.56, "x", 3.0,  "door",    1],      //   linen
    [106.51, 17.0,  "y", 2.6,  "door",   -1],      //   WC
    [106.51, 13.4,  "y", 2.4,  "door",   -1],      //   linen between the WCs
    [106.51, 9.8,   "y", 2.6,  "door",   -1],      //   WC
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [21.45,  66.64, "x", 3.5, 2.5,  5],      // bunk room
    [7.27,   36.3,  "y", 5.4, 2.75, 5],      // bedroom 2
    [7.27,   42.3,  "y", 5.4, 2.75, 5],
    [69.14,  53.6,  "y", 9.4, 1.5,  6.5],    // nook: glass wall to the deck
    [70.2,   52.53, "x", 6.9, 2,    6],      // great room
    [77.8,   52.53, "x", 3.6, 2,    6],
    [89.4,   52.53, "x", 4.3, 2,    6],
    [110.0,  52.86, "x", 2.5, 2.5,  5],      // master bedroom
    [126.97, 46.0,  "y", 4.7, 2.5,  5],
    [126.97, 31.0,  "y", 4.0, 2.5,  5],
    [128.13, 9.8,   "y", 4.6, 3.5,  4],      // master bath, by the tub
    [128.13, 21.3,  "y", 3.6, 4,    3],      // linen
    [84.0,   0,     "x", 8.0, 2.5,  5.5],    // den
    [95.95,  1.8,   "y", 5.8, 2.5,  5.5],
    [54.1,   0.7,   "y", 4.8, 2,    6],      // breakfast bay
    [54.6,   0,     "x", 5.6, 2,    6],
    [37.7,   6.28,  "x", 7.5, 3.5,  4],      // kitchen, over the sink
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: range wall west, sink under the south window, double island
    [35.8,   6.48,  38.29,  22.6,  0, 3,    counter],
    [35.9,   14.7,  38.2,   17.66, 3, 3.05, dark],      // range
    [38.29,  6.48,  54.41,  8.45,  0, 3,    counter],
    [39.93,  6.68,  42.57,  8.26,  3, 3.05, basin],     // sink
    [35.8,   25.89, 38.29,  29.11, 0, 7,    steel],     // fridge
    [42.24,  27.2,  49.14,  29.11, 0, 7,    wood],      // tall pantry cabinets
    [42.24,  12.4,  49.14,  22.27, 0, 3,    wood],      // double island
    [43.22,  16.68, 44.87,  18.65, 3, 3.05, basin],     // prep sink
    [56.38,  27.2,  68.22,  29.11, 0, 3,    wood],      // buffet
    // scullery, laundry, mudroom
    [24.74,  27.2,  34.8,   29.11, 0, 3,    counter],
    [28.09,  27.34, 31.71,  28.91, 3, 3.05, basin],
    [24.74,  21.28, 34.8,   22.93, 0, 3,    counter],
    [28.09,  47.07, 34.01,  49.05, 0, 3.2,  steel],     // washer + dryer
    [28.42,  41.02, 33.22,  43.32, 0, 3,    counter],
    [33.22,  41.02, 35.1,   43.52, 0, 3,    basin],     // laundry sink
    [22.63,  41.15, 24.41,  49.05, 0, 6,    shelf],     // drying rack
    [35.2,   41.15, 36.9,   49.05, 0, 7,    wood],
    [22.63,  35.66, 24.14,  39.97, 0, 7,    wood],      // lockers
    [28.09,  36.94, 36.64,  39.97, 0, 3,    wood],      // bench + cabinets
    [24.8,   30.49, 35.33,  31.81, 0, 1.5,  wood],      // mud bench in the hall
    // baths
    [7.7,    55.55, 10.33,  61.41, 0, 2,    white],     // bath 2: tub
    [10.99,  60.1,  17.3,   61.68, 0, 3,    counter],   //   double vanity
    [8.03,   51.55, 10.33,  53.85, 0, 1.4,  white],     // WC
    [51.78,  42.34, 53.42,  44.31, 0, 3,    counter],   // hall bath
    [51.12,  39.7,  53.09,  41.35, 0, 1.4,  white],
    [47.83,  35.89, 53.42,  38.39, 0, 0.15, tile],      //   shower
    [111.64, 17.86, 121.51, 19.64, 0, 3,    counter],   // master bath: double vanity
    [111.97, 9.55,  120.2,  14.05, 0, 0.15, tile],      //   shower
    [123.16, 9.55,  127.63, 15.03, 0, 2,    white],     //   tub
    [100.79, 17.01, 103.42, 19.31, 0, 1.4,  white],     // WCs
    [100.79, 9.77,  103.42, 12.07, 0, 1.4,  white],
    // closets and storage
    [7.7,    49.57, 13.36,  50.69, 0, 7,    shelf],
    [96.51,  27.2,  106.05, 28.91, 0, 7,    shelf],
    [96.51,  22.93, 98.16,  27.2,  0, 7,    shelf],
    [96.51,  21.15, 106.05, 22.93, 0, 7,    shelf],
    [111.97, 27.2,  121.38, 28.91, 0, 7,    shelf],
    [111.97, 21.15, 121.38, 22.93, 0, 7,    shelf],
    [125.99, 21.15, 127.63, 28.91, 0, 7,    shelf],
    [69.67,  18.65, 71.38,  29.11, 0, 7,    shelf],     // foyer wine racks
    [69.67,  12.07, 71.38,  18.65, 0, 1.5,  wood],      //   and bench
    // great room fireplace
    [81.58,  51.41, 89.61,  52.14, 0, 4,    hearth],
];

// furniture, as drawn on the plan
function main_furniture() = [
    [14.8,   40.03, 19.21,  44.64, 0, 2,    bed],       // bedroom 2
    [7.7,    39.05, 10.33,  44.97, 0, 2.6,  sofa],
    [10.66,  35.76, 14.93,  37.4,  0, 2.5,  wood],
    [18.09,  60.76, 21.05,  66.02, 0, 5,    bed],       // bunk beds
    [23.16,  63.91, 29.74,  66.15, 0, 5,    bed],
    [22.17,  54.05, 26.12,  56.15, 0, 2.5,  wood],
    [35.99,  56.68, 39.93,  60.76, 0, 2.5,  wood],      // study
    [36.64,  54.05, 41.91,  56.02, 0, 3,    wood],
    [46.84,  60.76, 51.78,  62.99, 0, 2.6,  sofa],      // sitting room
    [43.09,  53.85, 45.53,  59.77, 0, 2.6,  sofa],
    [47.83,  55.49, 50.46,  59.11, 0, 1.5,  table, "", "round"],
    [58.68,  56.48, 62.96,  60.76, 0, 2.5,  table, "", "round"],   // nook table
    [59.34,  12.73, 62.96,  21.94, 0, 2.5,  table],     // dining table
    [54.41,  0.56,  55.39,  5.49,  0, 1.5,  sofa],      // breakfast banquette
    [55.39,  0.36,  60.33,  1.88,  0, 1.5,  sofa],
    [55.07,  1.9,   60.2,   6.0,   0, 2.5,  table, "", "round"],
    [70.53,  40.03, 73.82,  46.61, 0, 2.6,  sofa],      // great room
    [74.14,  39.05, 79.74,  41.55, 0, 2.6,  sofa],
    [75.79,  42.34, 79.74,  46.28, 0, 1.5,  table],
    [96.64,  38.39, 99.8,   44.97, 0, 2.5,  wood],      // office desks
    [105.07, 38.39, 108.22, 44.97, 0, 2.5,  wood],
    [116.25, 37.07, 122.17, 43.65, 0, 2,    bed],       // master bedroom
    [109.34, 39.05, 111.32, 44.64, 0, 3,    wood],
    [82.04,  25.23, 94.54,  28.85, 0, 2.6,  sofa],      // den
    [84.01,  16.68, 90.59,  18.65, 0, 2.6,  sofa],
    [84.01,  10.1,  90.59,  12.07, 0, 2.6,  sofa],
    [86.64,  12.73, 89.93,  16.02, 0, 1.5,  table, "", "round"],
    [88.95,  3.52,  92.57,  7.14,  0, 2.5,  table, "", "round"],
    [83.36,  0.36,  91.91,  2.86,  0, 1.5,  sofa],
    [82.04,  18.65, 84.67,  25.23, 0, 2.5,  wood],
    [96.84,  13.39, 98.82,  16.02, 0, 3,    wood],
];

// porch posts [x, y, height]
function main_posts() = [
    [49.69, -14.81, 9.5], [57.4, -14.81, 9.5], [65.1, -14.81, 9.5], [69.2, -14.81, 9.5],
    [81.1, -14.81, 9.5], [88.6, -14.81, 9.5], [96.3, -14.81, 9.5], [100.96, -14.81, 9.5],
    [49.69, -7.0, 9.5], [49.69, 5.83, 9.5], [100.96, -7.0, 9.5], [100.96, 8.86, 9.5],
    [69.59, 64.25, 10], [95.18, 64.25, 10],
    [108.17, 59.02, 10], [109.07, 61.95, 10], [126.52, 61.95, 10],
    [127.42, 59.02, 10], [137.21, 59.02, 10], [137.21, 51.1, 10], [137.21, 43.2, 10],
    [137.21, 35.2, 10], [137.21, 27.29, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,      1.25,  24.34,  35.46, 8.5, 0.5,   1.5],   // garage
    [7.27,   35.46, 37.3,   66.64, 10,  0.5,   1.5],   // bedroom wing
    [37.3,   35.46, 69.14,  63.42, 10,  0.5,   1.5],   // study, sitting room, nook
    [69.14,  29.51, 95.63,  52.53, 12,  0.5,   1.5],   // great room
    [95.63,  29.51, 126.97, 52.86, 10,  0.5,   1.5],   // office, master bedroom
    [24.34,  6.28,  69.14,  29.51, 12,  0.5,   1.5],   // kitchen, scullery, side entry
    [54.1,   0,     69.14,  6.28,  10,  0.5,   1.5],   // breakfast bay
    [69.14,  0,     95.95,  29.51, 12,  0.5,   1.5],   // foyer, den
    [95.95,  9.31,  128.13, 29.51, 10,  0.5,   1.5],   // master closets + bath
    [49.24, -15.26, 101.41, 0,     9.5, 0.333, 1],     // front porch
    [49.24,  0,     54.1,   6.28,  9.5, 0.333, 1],
    [95.95,  0,     101.41, 9.31,  9.5, 0.333, 1],
    [69.14,  52.53, 95.63,  64.7,  10,  0.333, 1],     // deck
    [95.63,  48.16, 108.62, 59.47, 10,  0.333, 1],     // office porch
    [108.62, 52.86, 126.97, 62.4,  10,  0.333, 1],     // master porch
    [126.97, 26.84, 137.66, 59.47, 10,  0.333, 1],     // side porch
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
    if (show_stair) main_stair();
    // garage steps up to the house (hall) and to the side entry: a landing
    // at house level and two steps, from the garage slab 1.5 ft below
    for (y = [[30.5, 35.2], [15.6, 19.6]])
        paint(stair_color()) {
            translate([21.8, y[0], -1.5]) cube([2.34, y[1] - y[0], 1.5]);
            translate([20.6, y[0], -1.5]) cube([1.2, y[1] - y[0], 1.0]);
            translate([19.4, y[0], -1.5]) cube([1.2, y[1] - y[0], 0.5]);
        }

    for (p = main_posts()) post(p[0], p[1], p[2]);
    porch_steps(69.6,  -15.26, "-y", 11.0);   // front entry
    porch_steps(70.0,   64.7,  "+y", 24.8);   // deck to the yard
    porch_steps(111.0,  62.4,  "+y", 13.6);   // master porch to the yard
    porch_steps(24.8,   13.39, "-y", 10.3);   // side entry
    porch_steps(37.0,   66.6,  "+y", 3.8);    // study stoop

    if (show_roof) roofs(main_roof(), roof_color, roof_opacity);
}
