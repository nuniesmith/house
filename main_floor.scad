// Main floor - OpenSCAD model of the main level.
// Units: feet. Visualisation only - NOT construction documents.
//
// Geometry is measured off the architect's plan image (about 11.55 px
// per ft, +/- 0.3 ft): rooms are wall-centre-line rectangles, so they
// run larger than the printed clear sizes, which also leave out the
// walkways (e.g. the family room's printed 16'-6" x 15'-2" is its
// seating area). x = east, y = north; y = 0 is the front wall of the
// dining room / lounge and x = 0 the garage's west wall.
//
// changes = true applies the proposed changes (Kayla's review): direct
// bedroom -> closet doors (green leaves), a hall to bedrooms 2 + 3 that
// doesn't pass through the laundry, a master laundry by the closet, a
// hall from the kitchen to the dining room beside the butler's pantry,
// a kitchen work zone with no through traffic (fridge included), a
// wider nook-to-kitchen opening, a linen-closet door off the new hall
// and a larger master shower.
// It also puts the basement stair in the former bar (a U-stair that lands
// in the basement rec room), wraps the front porch round both front
// corners so the whole basement sits under the house or a porch, and
// widens bath 2.
// changes = false shows the plan as drawn, with the bar and the short
// stair in the garage corner (it doesn't meet the basement - REVIEW.md).

use <house_lib.scad>

changes = true;
show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.20, 0.38, 0.62];  // blue
audit = false;         // echo the tables for the layout checker

main_level(changes, show_roof, roof_color, roof_opacity, audit);

/* [Hidden] */
counter  = [0.97, 0.97, 0.95];
wood     = [0.55, 0.38, 0.22];
steel    = [0.70, 0.72, 0.74];
dark     = [0.12, 0.12, 0.12];
basin    = [0.62, 0.78, 0.86];
hearth   = [0.35, 0.33, 0.32];
brick    = [0.55, 0.27, 0.20];
white    = [0.97, 0.97, 0.97];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    // ---- garage, mud room, bedroom 4
    ["GARAGE",          0,     7.9,  25.2,  39.7, 9.67, "garage", -1.5],
    ["STORAGE",         19.5,  35.5, 25.2,  39.7, 8,    "closet", 0, "new", [22.1, 38.7, 0.65]],
    ["STAIR DN",        19.5,  35.5, 25.2,  39.7, 8,    "stairwell", 0, "old"],
    ["MUD ROOM",        25.2,  23.5, 36.9,  31.1, 12,   "utility"],
    ["HALL",            25.2,  31.1, 55.2,  35.5, 12,   "hall"],
    ["",                25.2,  35.5, 29.9,  39.7, 12,   "hall"],
    ["BATH 4",          36.9,  25.9, 45.5,  31.1, 12,   "bath", 0, "", [40.5, 29.4, 1.2]],
    ["WIC",             45.5,  25.9, 50.7,  31.1, 12,   "closet", 0, "", [48.1, 29.6, 1.1]],
    ["",                50.7,  25.9, 55.2,  31.1, 12,   "hall"],
    ["BEDROOM 4",       36.9,  11.6, 55.2,  25.9, 12,   "bed"],
    // ---- north bedroom wing
    ["BEDROOM 3",       12.1,  39.7, 29.9,  53.1, 12,   "bed"],
    ["",                12.1,  53.1, 16.1,  58.7, 12,   "hall"],
    ["WIC",             16.1,  53.1, 21.4,  58.7, 12,   "closet", 0, "", [19.6, 54.2, 1]],
    ["BATH 3",          12.1,  58.7, 21.4,  64.3, 12,   "bath", 0, "", [17.3, 62.2, 1.3]],
    ["BEDROOM 2",       21.4,  53.1, 35.25, 68.1, 12,   "bed", 0, "new"],
    ["WIC",             35.25, 51.3, 41.4,  56.1, 12,   "closet", 0, "new", [39.2, 52.4, 1.1]],
    ["BATH 2",          35.25, 56.1, 41.4,  66.1, 12,   "bath", 0, "new", [38.3, 62, 1.4, 90]],    // 1 ft wider
    ["BEDROOM 2",       21.4,  53.1, 36.25, 68.1, 12,   "bed", 0, "old"],
    ["WIC",             36.25, 51.3, 41.4,  56.1, 12,   "closet", 0, "old"],
    ["BATH 2",          36.25, 56.1, 41.4,  66.1, 12,   "bath", 0, "old"],
    ["HALL",            29.9,  47,   41.4,  51.3, 12,   "hall"],
    ["",                29.9,  51.3, 35.25, 53.1, 12,   "hall", 0, "new"],
    ["",                29.9,  51.3, 36.25, 53.1, 12,   "hall", 0, "old"],
    ["LAUNDRY",         29.9,  35.5, 37.4,  47,   12,   "utility", 0, "new", [33.4, 38.3, 1.1]],
    ["HALL",            37.4,  35.5, 41.4,  47,   12,   "hall", 0, "new"],   // to bedrooms 2 + 3, in line with the bedroom hall
    ["LAUNDRY",         29.9,  35.5, 43.1,  47,   12,   "utility", 0, "old"],
    ["PWDR",            41.4,  35.5, 48.7,  41.8, 12,   "bath", 0, "new", [44.6, 39.6, 1.3]],
    ["LINEN",           41.4,  41.8, 48.7,  47,   12,   "closet", 0, "new", [46.2, 44.4, 1]],
    ["PWDR",            43.1,  35.5, 48.7,  41.8, 12,   "bath", 0, "old"],
    ["LINEN",           43.1,  41.8, 48.7,  47,   12,   "closet", 0, "old"],
    ["PANTRY",          48.7,  35.5, 55.2,  47,   12,   "utility", 0, "", [52, 41.25, 1.4, 90]],
    [["BREAKFAST", "NOOK"], 41.4, 47, 55.2, 66.2, 14, "dining", 0, "", [47.5, 57.5, 1.4]],
    // ---- kitchen, family room, front rooms
    ["KITCHEN",         55.2,  29.5, 71.3,  52.6, 14,   "kitchen", 0, "", [63.25, 33.3, 1.8]],
    ["FAMILY ROOM",     71.3,  31.4, 97.2,  52.6, 14,   "living", 0, "", [83.5, 47.6, 2]],
    ["DINING ROOM",     55.2,  0,    71.3,  19.6, 14,   "dining", 0, "", [64, 14.5, 1.5]],
    [["BUTLER'S", "PANTRY"], 55.2, 19.6, 67.3, 29.5, 14, "utility", 0, "new"],
    ["HALL",            67.3,  19.6, 71.3,  29.5, 14,   "hall", 0, "new"],   // kitchen to dining
    [["BUTLER'S", "PANTRY"], 55.2, 19.6, 71.3, 29.5, 14, "utility", 0, "old"],
    ["FOYER",           71.3,  2.9,  82.3,  17.7, 14,   "hall"],
    [["FRONT", "HALL"], 71.3, 17.7, 82.3, 31.4, 14,   "hall"],
    ["LOUNGE",          82.3,  0,    97.2,  21,   14,   "living", 0, "", [88.8, 14.2, 2]],
    ["STAIR DN",        82.3,  21,   97.2,  31.4, 14,   "stairwell", 0, "new", [90, 23.3, 1.5]],
    ["BAR",             82.3,  21,   97.2,  31.4, 14,   "dining", 0, "old"],
    // ---- master wing
    ["GALLERY",         97.2,  30.6, 109.7, 36.5, 14,   "hall"],
    ["OFFICE",          97.2,  36.5, 109.7, 49.1, 14,   "office"],
    [["MASTER", "SUITE"], 109.7, 30.6, 127.9, 53.5, 14, "bed"],
    ["W / D",           97.2,  21.5, 102.2, 30.6, 12,   "utility", 0, "new", [99.7, 25.3, 0.9]],  // master laundry
    ["WIC",             102.2, 21.5, 108.7, 30.6, 12,   "closet", 0, "new"],
    ["WIC",             97.2,  21.5, 108.7, 30.6, 12,   "closet", 0, "old"],
    ["WIC",             108.7, 21.5, 117.1, 30.6, 12,   "closet"],
    ["DRESSING",        97.2,  17.3, 117.1, 21.5, 12,   "hall"],
    ["WC",              97.2,  11.6, 105.4, 17.3, 12,   "bath", 0, "", [100.2, 13.6, 1.6]],
    ["SHOWER",          105.4, 11.6, 117.1, 17.3, 12,   "shower", 0, "new", [110.5, 14.45, 1.5]],
    ["VANITY",          105.4, 11.6, 110.2, 17.3, 12,   "bath", 0, "old"],
    ["SHOWER",          110.2, 11.6, 117.1, 17.3, 12,   "shower", 0, "old"],
    [["MASTER", "BATH"], 117.1, 11.6, 130.1, 30.6, 12, "bath"],
    // ---- porches (no walls)
    ["FRONT PORCH",     48.1, -12.3, 105.7, 0,    0,    "porch"],
    ["",                48.1,  0,    55.2,  11.6, 0,    "porch"],
    ["",                97.2,  0,    105.7, 11.6, 0,    "porch", 0, "old"],
    ["",                97.2,  0,    130.1, 11.6, 0,    "porch", 0, "new"],   // over the music room
    ["",                25.2,  0,    48.1,  11.6, 0,    "porch", 0, "new"],   // over the pool room
    ["",                25.2,  11.6, 36.9,  17.8, 0,    "porch", 0, "new"],
    ["",                71.3,  0,    82.3,  2.9,  0,    "porch"],
    ["STOOP",           25.2,  17.8, 36.9,  23.5, 0,    "porch", 0, "", [33, 19.7, 1.5]],
    [["BREAKFAST", "PORCH"], 55.2, 52.6, 69.3, 66.2, 0, "porch"],
    ["OUTDOOR LIVING",  69.3,  52.6, 97.2,  67.6, 0,    "porch"],
    [["OFFICE", "PORCH"], 97.2, 49.1, 109.7, 59.5, 0,  "porch"],
    ["MASTER PORCH",    109.7, 53.5, 127.9, 63.5, 0,    "porch"],
    [["SIDE", "PORCH"], 127.9, 30.6, 137.7, 59.8, 0,   "porch"],
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    // ---- exterior
    [73.8,  2.9,  "x", 6,    "double",  1],            // front door
    [56.8,  0,    "x", 4.8,  "double",  1],            // dining French doors
    [64.7,  0,    "x", 4.8,  "double",  1],
    [84.2,  0,    "x", 4.4,  "double",  1],            // lounge French doors
    [92.1,  0,    "x", 4.4,  "double",  1],
    [51.1,  11.6, "x", 3,    "door",    1],            // bedroom 4 to the porch
    [26.5,  23.5, "x", 3,    "door",   -1],            // mud room to the stoop
    [0,     10.5, "y", 9,    "garage"],                // side-load garage doors
    [0,     22.5, "y", 9,    "garage"],
    [25.2,  32.4, "y", 2.8,  "door",   -1],            // garage to the hall
    [55.2,  57.4, "y", 5.2,  "double", -1],            // nook to the breakfast porch
    [72.5,  52.6, "x", 20.5, "slider"],                // family room pocket slider
    [115.6, 53.5, "x", 6,    "double", -1],            // master suite to the master porch
    [127.9, 32.4, "y", 5,    "double", -1],            // master suite to the side porch
    [127.9, 46.8, "y", 5,    "double", -1],
    // ---- front rooms, kitchen, family room
    [71.3,  6,    "y", 8.5,  "open"],                  // foyer / dining
    [82.3,  6,    "y", 8.5,  "open"],                  // foyer / lounge
    [72.3,  17.7, "x", 9,    "open"],                  // foyer / front hall
    [71.6,  31.4, "x", 10.4, "full"],                  // front hall / family room
    [71.3,  31.7, "y", 20.6, "full"],                  // kitchen / family room
    [82.6,  31.4, "x", 14.3, "full"],                  // stair (or bar) / family room
    [58,    19.6, "x", 3,    "door",    1],            // dining / butler's pantry
    [56.5,  29.5, "x", 3.5,  "open"],                  // butler's pantry / kitchen
    [55.2,  31.4, "y", 3.8,  "full"],                  // hall into the kitchen
    [55.2,  47.3, "y", 5,    "open",    1, "new"],     // nook / kitchen, widened
    [55.2,  47.3, "y", 3.9,  "open",    1, "old"],     // nook / kitchen (as drawn)
    [67.6,  29.5, "x", 3.4,  "full",    1, "new"],     // kitchen / dining hall
    [67.6,  19.6, "x", 3.4,  "full",    1, "new"],     // dining hall / dining room
    // ---- bedroom wing
    [41.4,  47.3, "y", 3.7,  "open"],                  // nook / bedroom hall
    [30.2,  51.3, "x", 4.75, "full",    1, "new"],     // bedroom hall alcove
    [30.2,  51.3, "x", 5.75, "full",    1, "old"],
    [31.9,  53.1, "x", 3,    "door",    1, "new"],     // bedroom 2
    [32.7,  53.1, "x", 3,    "door",    1, "old"],
    [29.9,  47.9, "y", 2.8,  "door",   -1],            // bedroom 3
    [36.2,  35.5, "x", 3,    "door",    1, "old"],     // laundry (as drawn)
    [37.4,  40,   "y", 2.8,  "door",   -1, "new"],     // laundry off the bedroom hall
    [37.7,  35.5, "x", 3.4,  "full",    1, "new"],     // bedroom hall from the garage hall
    [37.7,  47,   "x", 3.4,  "full",    1, "new"],     // bedroom hall to bedrooms 2 + 3
    [45.4,  35.5, "x", 2.6,  "door",    1],            // powder room
    [41.4,  43,   "y", 2.4,  "door",    1, "new"],     // linen, off the new hall
    [45,    47,   "x", 2.4,  "door",    1, "old"],     // linen, into the nook (as drawn)
    [49.6,  47,   "x", 2.6,  "door",   -1],            // pantry, nook side
    [49.6,  35.5, "x", 2.6,  "door",    1],            // pantry, hall side
    [25.5,  31.1, "x", 8.2,  "full"],                  // mud room / hall
    [25.5,  35.5, "x", 4.1,  "full"],                  // hall alcove by the garage door
    [25.2,  36,   "y", 2.5,  "door",   -1, "new"],        // storage in the old stair bay
    [25.2,  35.8, "y", 3.6,  "full",    1, "old"],        // top of the drawn stair
    [51.0,  31.1, "x", 3.9,  "full"],                  // hall to bedroom 4
    [51.4,  25.9, "x", 3,    "door",   -1],            // bedroom 4
    [42.4,  25.9, "x", 2.6,  "door",    1],            // bath 4
    [46.6,  25.9, "x", 2.6,  "door",    1, "new"],     // bedroom 4 -> WIC
    [45.5,  27.5, "y", 2.4,  "open",    1, "old"],     // bath 4 -> WIC (as drawn)
    [12.6,  53.1, "x", 3,    "open"],                  // bedroom 3 / closet vestibule
    [12.4,  58.7, "x", 2.6,  "door",    1],            // bath 3
    [16.1,  55.5, "y", 2.6,  "door",    1],            // bedroom 3 WIC
    [35.25, 56.6, "y", 2.6,  "door",    1, "new"],     // bath 2
    [36.25, 56.6, "y", 2.6,  "door",    1, "old"],
    [35.25, 53.3, "y", 2.5,  "door",    1, "new"],     // bedroom 2 -> WIC
    [36.6,  56.1, "x", 2.4,  "open",    1, "old"],     // bath 2 -> WIC (as drawn)
    // ---- master wing
    [97.2,  31.5, "y", 4.5,  "open"],                  // family room / gallery
    [101.8, 36.5, "x", 3.6,  "open"],                  // gallery / office
    [109.7, 31.2, "y", 5,    "double",  1],            // gallery / master suite
    [111,   30.6, "x", 2.6,  "door",   -1, "new"],     // master suite -> WIC
    [120.8, 30.6, "x", 5,    "double", -1],            // master suite / bath
    [103.8, 21.5, "x", 2.5,  "open"],                  // WIC / dressing
    [98.3,  21.5, "x", 2.6,  "door",    1, "new"],     // master laundry
    [111.3, 21.5, "x", 2.5,  "open"],                  // WIC / dressing
    [117.1, 17.6, "y", 3.6,  "open"],                  // dressing / master bath
    [101.8, 17.3, "x", 2.5,  "door",   -1],            // WC
    [105.8, 17.3, "x", 3,    "open",    1, "new"],     // bigger shower: entry
    [109,   17.3, "x", 7.8,  "glass",   1, "new"],     //   and glass front
    [105.8, 17.3, "x", 4,    "open",    1, "old"],     // vanity niche (as drawn)
    [110.6, 17.3, "x", 2.6,  "open",    1, "old"],     // shower (as drawn)
    [113.4, 17.3, "x", 3.4,  "glass",   1, "old"],
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [6,     7.9,  "x", 3.5, 3,   4],      // garage
    [15.5,  7.9,  "x", 3.5, 3,   4],
    [40.3,  11.6, "x", 4.3, 2.5, 5],      // bedroom 4
    [31.7,  23.5, "x", 3.2, 3,   4],      // mud room
    [12.1,  41.5, "y", 3.5, 2.5, 5],      // bedroom 3
    [12.1,  47.5, "y", 3.5, 2.5, 5],
    [12.1,  54.5, "y", 2.5, 3,   4],      // closet vestibule
    [14,    64.3, "x", 2.5, 4,   3],      // bath 3
    [23.5,  68.1, "x", 3.5, 2.5, 5],      // bedroom 2
    [30,    68.1, "x", 3.5, 2.5, 5],
    [37.5,  66.1, "x", 2.5, 5,   2.5],    // bath 2
    [43,    66.2, "x", 4,   2.5, 6],      // nook
    [49.5,  66.2, "x", 4,   2.5, 6],
    [62.5,  52.6, "x", 5,   3.5, 4],      // kitchen, over the counter
    [55.2,  2,    "y", 4,   2.5, 6],      // dining
    [97.2,  3,    "y", 3.3, 2.5, 6],      // lounge
    [101,   49.1, "x", 5,   2.5, 6],      // office
    [112.2, 53.5, "x", 3.2, 2.5, 6],      // master suite
    [122.3, 53.5, "x", 3.2, 2.5, 6],
    [127.9, 39.5, "y", 5,   2.5, 6],
    [130.1, 21.9, "y", 6,   3.5, 4],      // master bath
    [121,   11.6, "x", 5,   3.5, 4],
    [99.5,  11.6, "x", 2,   5,   2.5],    // WC
];

// [x0, y0, x1, y1, z0, z1, colour, tag]
function main_fixtures() = [
    // kitchen as proposed: one work aisle - wall ovens, range and fridge
    // on the west wall facing the island sink - closed at the south by a
    // counter return. Nothing sits on the north wall, so the nook <->
    // family room path and the garage hall <-> family room path both pass
    // outside the work zone and never between the fridge and the cook.
    [55.2, 37.5, 57.2, 43.4, 0, 3,    counter, "new"],   // range wall
    [55.2, 37.5, 57.2, 39.8, 0, 7,    steel,   "new"],   // wall ovens
    [55.4, 40.4, 57.1, 43.2, 3, 3.05, dark,    "new"],   // range
    [55.2, 43.5, 57.5, 46.5, 0, 7,    steel,   "new"],   // fridge, facing the aisle
    [55.2, 35.5, 61.2, 37.5, 0, 3,    counter, "new"],   // counter return
    [61.2, 37.5, 65.2, 46.0, 0, 3,    wood,    "new"],   // island
    [61.4, 40.5, 62.8, 43.5, 3, 3.05, basin,   "new"],   // island sink
    // kitchen as drawn: cooktop wall, island across both entries, sink
    // under the north window, fridge by the butler's pantry
    [55.2, 35.5, 57.6, 47.0, 0, 3,    counter, "old"],
    [55.4, 39.5, 57.4, 43.0, 3, 3.05, dark,    "old"],
    [60.7, 35.2, 65.2, 47.3, 0, 3,    wood,    "old"],
    [60.9, 40.0, 62.3, 43.0, 3, 3.05, basin,   "old"],
    [56.5, 50.6, 69.0, 52.6, 0, 3,    counter, "old"],
    [63.3, 50.9, 66.7, 52.3, 3, 3.05, basin,   "old"],
    [60.4, 29.7, 63.6, 32.1, 0, 7,    steel,   "old"],
    // laundry: washer + dryer; master laundry beside the closet
    [97.5, 28.1, 99.8, 30.3, 0, 3.2,  steel, "new"],
    [99.8, 28.1, 102.0, 30.3, 0, 3.2, steel, "new"],
    [30.4, 44.6, 32.9, 46.8, 0, 3.2,  steel],
    [33.1, 44.6, 35.6, 46.8, 0, 3.2,  steel],
    // fireplaces: dining (west wall), family room (east wall), lounge gas
    [55.2, 8.0,  57.2, 11.5, 0, 4.5,  hearth],
    [95.2, 39.5, 97.2, 43.5, 0, 4.5,  hearth],
    [95.6, 8.2,  97.2, 11.8, 0, 3.5,  hearth],
    [56.9, 8.6,  57.25, 10.9, 0.5, 2.6, dark],
    [94.85, 40.1, 95.2, 42.9, 0.5, 2.6, dark],
    [95.25, 8.8, 95.6, 11.2, 0.5, 2.2, dark],
    // master bath tub, shower bench
    [121.2, 12.4, 126.6, 15.6, 0, 2,  white],
    [116.0, 11.9, 116.9, 17.0, 0, 1.5, white, "new"],
    // garage: dog wash, steps up to the house
    [0.6,  35.6, 5.0,  39.2, -1.5, 0.5,  white],
    [19.5, 32.4, 20.5, 35.3, -1.5, -1.0, [0.80, 0.80, 0.78]],
    [20.5, 32.4, 21.5, 35.3, -1.5, -0.5, [0.80, 0.80, 0.78]],
    [21.5, 32.4, 25.0, 35.3, -1.5, 0,    [0.80, 0.80, 0.78]],
];

// porch posts [x, y, height]
function main_posts() = [
    [48.55, -11.85, 12.67], [55.1, -11.85, 12.67], [63.1, -11.85, 12.67],
    [71.5,  -11.85, 12.67], [81.6, -11.85, 12.67], [90.7, -11.85, 12.67],
    [98.8,  -11.85, 12.67], [105.25, -11.85, 12.67],
    [48.55, 0, 12.67], [105.25, 0, 12.67], [48.55, 11.15, 12.67, "old"], [105.25, 11.15, 12.67, "old"],
    [25.65, 0.45, 12.67, "new"], [36.45, 0.45, 12.67, "new"], [117.6, 0.45, 12.67, "new"],
    [129.65, 0.45, 12.67, "new"], [129.65, 11.15, 12.67, "new"],
    [25.65, 18.25, 10, "old"], [36.45, 18.25, 10, "old"],
    [55.65, 65.75, 14], [62.4, 65.75, 14],
    [69.75, 67.15, 14], [79, 67.15, 14], [88.2, 67.15, 14], [96.75, 67.15, 14],
    [97.65, 59.05, 14], [103.45, 59.05, 14], [109.25, 59.05, 14],
    [110.15, 63.05, 14], [119, 63.05, 14], [127.45, 63.05, 14],
    [131, 31.05, 12], [137.25, 31.05, 12], [137.25, 40.6, 12],
    [137.25, 50.15, 12], [137.25, 59.35, 12],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,     7.9,   25.2,  39.7, 8.17,  0.667, 1.5],  // garage
    [25.2,  11.6,  55.2,  39.7, 12,    0.667, 1.5],  // mud room, bedroom 4
    [12.1,  35.5,  41.4,  68.1, 12,    0.667, 1.5],  // bedrooms 2 + 3, laundry
    [41.4,  35.5,  55.2,  66.2, 14,    0.667, 1.5],  // nook, pantry
    [55.2,  0,     97.2,  31.4, 14,    0.667, 1.5],  // dining, foyer, lounge
    [55.2,  29.5,  97.2,  52.6, 14,    0.667, 1.5],  // kitchen, family room
    [97.2,  11.6,  130.1, 30.6, 12,    0.667, 1.5],  // master closets + bath
    [97.2,  30.6,  127.9, 53.5, 14,    0.667, 1.5],  // office, master suite
    [48.1, -12.3,  105.7, 0,    12.67, 0.333, 1],    // front porch
    [48.1,  0,     55.2,  11.6, 12.67, 0.333, 1],
    [25.2,  0,     48.1,  11.6, 12.67, 0.333, 1, "new"],   // porch over the pool room
    [97.2,  0,     105.7, 11.6, 12.67, 0.333, 1, "old"],
    [97.2,  0,     130.1, 11.6, 12.67, 0.333, 1, "new"],   // porch over the music room
    [25.2,  15.8,  36.9,  23.5, 10,    0.333, 1, "old"],    // stoop
    [25.2,  11.6,  36.9,  23.5, 10,    0.333, 1, "new"],
    [55.2,  52.6,  97.2,  67.6, 14,    0.333, 1],    // breakfast porch + outdoor living
    [97.2,  49.1,  109.7, 59.5, 14,    0.333, 1],    // office porch
    [109.7, 53.5,  127.9, 63.5, 14,    0.333, 1],    // master porch
    [127.9, 30.6,  137.7, 59.8, 12,    0.333, 1],    // side porch
];

module main_level(changes = true, show_roof = true,
                  roof_color = [0.20, 0.38, 0.62], roof_opacity = 1, audit = false) {
    tags = [changes ? "new" : "old"];
    rooms = active(main_rooms(), 8, tags);
    doors = active(main_doors(), 6, tags);
    if (audit) echo(rooms = rooms, doors = doors, windows = main_windows(),
                    fixtures = active(main_fixtures(), 7, tags));

    draw_level(rooms, doors, main_windows());
    fixtures(active(main_fixtures(), 7, tags));

    // basement stair: the U-stair in the old bar, or the short flight
    // the plan draws in the garage corner (it stops at the wall)
    if (changes) bar_stair();
    else flight(19.6, 35.7, 25.2, 39.5, "-x", 0, -8 * floor_to_floor() / 21, 8, -6);

    for (p = active(main_posts(), 3, tags)) post(p[0], p[1], p[2]);
    porch_steps(72.6, -12.3, "-y", 8.4);    // front entry
    if (changes) porch_steps(27.5, 0, "-y", 8);   // corner porch by the garage
    else porch_steps(26.5, 17.8, "-y", 9.5);     // stoop
    porch_steps(73,    67.6, "+y", 20);     // outdoor living to the yard
    porch_steps(112.5, 63.5, "+y", 12.5);   // master porch to the yard

    if (show_roof) {
        roofs(active(main_roof(), 7, tags), roof_color, roof_opacity);
        color(brick) {                                  // chimneys
            translate([54.7, 8.3, 0]) cube([2.5, 2.9, 20]);
            translate([95.6, 40.0, 0]) cube([2.8, 3.0, 20]);
        }
    }
}
