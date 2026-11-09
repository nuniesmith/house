// Main floor - OPTION B: the as-drawn sheet (docs/house/floor_plan.JPEG, Oct 30)
// with Kayla's notes applied. Units: feet, x = east, y = north; x = 0 is the
// garage's west wall, y = 0 the front wall line. Visualisation only - NOT
// construction documents.
//
// What this option is: the sheet's room ARRANGEMENT (read from geometry and
// fixtures, not from its printed labels) - dining room, foyer and a study/den
// across the front; kitchen + great room in the north-centre with the island
// and the sink wall; the garage-side service cluster; the sun room and covered
// patio - with Kayla's notes applied on top. Changes vs the current model
// (main_floor.scad on main):
//  * the 80 ft spine is gone: a 30 ft service hall west of the kitchen and a
//    36 ft gallery east of it; the kitchen sits between them
//  * garage trimmed 6.65 ft at the south end (y 1.25 -> 7.9) and its doors
//    turned to face south (drive no longer passes BEDROOM 2; building area
//    falls under 600 m2); front walls moved 2 ft north (den alcove deleted)
//  * pantry <-> garage "Costco door"; pantry opens to the side-entry porch
//  * master laundry (W/D in the ex-LINEN room), closet opening widened to 3 ft
//  * BEDROOM 2's closet moved off the exterior wall; tubs off exterior walls
//  * every single door is 36 in; halls 4.6 ft clear or wider; curbless showers
//  * vestibule + powder room at the front entry
//  * the stair is TWO flights with a landing (CODE-01): same x, same foot in the
//    basement (y 28.725), top nosing moved north to y 50.825. The basement
//    variant (basement_b.scad) frees the gym's SW corner for the longer stair.

use <../../../models/house_lib.scad>

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
table    = [0.66, 0.50, 0.34];

// ---- the two-flight stair (CODE-01) ------------------------------------
// 22 risers of 7.5 in = 11 + landing + 11. Same x as before (42.65-47.27).
// Top nosing y 50.825; flight 1 runs south 10 treads to the landing
// (y 42.075-37.475, 6.875 ft below the main floor); flight 2 runs on south
// to the foot at y 28.725, where the basement expects it.
function stairb_top_y()   = 50.825;
function stairb_land()    = [37.475, 42.075];       // landing y0, y1
function stairb_foot_y()  = stairb_land()[0] - 10 * stair_run();   // 28.725

module main_stair_b(z_main = 0, rail = true) {
    x0 = stair_x()[0] + wall_t() / 2;
    x1 = stair_x()[1] - wall_t() / 2;
    zl = z_main - 11 * stair_rise();
    zb = z_main - floor_to_floor();
    flight(x0, stairb_land()[1], x1, stairb_top_y(), "-y", z_main, zl, 11, zb);
    landing(x0, stairb_land()[0], x1, stairb_land()[1], zb, zl);
    flight(x0, stairb_foot_y(), x1, stairb_land()[0], "-y", zl, zb, 11, zb);
    if (rail)
        paint([0.40, 0.28, 0.18])
            for (x = [x0 + 0.1, x1 - 0.2]) {
                hull() { translate([x, stairb_top_y(), z_main + 2.8]) cube([0.1, 0.1, 0.12]);
                         translate([x, stairb_land()[1], zl + 2.8]) cube([0.1, 0.1, 0.12]); }
                hull() { translate([x, stairb_land()[0], zl + 2.8]) cube([0.1, 0.1, 0.12]);
                         translate([x, stairb_foot_y(), zb + 2.8]) cube([0.1, 0.1, 0.12]); }
            }
}

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    // ---- garage (trimmed to y 7.9) and the service side
    ["GARAGE",          0,     7.9,   24.34, 35.46, 10, "garage", -1.5],
    [["SIDE", "ENTRY"], 24.34, 13.39, 35.6,  20.82, 0,  "porch", 0, "", [30, 17.3, 1.3]],
    [["PANTRY /", "SCULLERY"], 24.34, 20.82, 35.6, 29.51, 12, "utility", 0, "", [30, 25.3, 1.1]],
    ["MUDROOM",         28.0,  35.46, 37.3,  40.56, 10, "utility", 0, "", [32.6, 36.2, 1.0]],
    ["WIC",             22.1,  35.46, 28.0,  40.56, 10, "closet", 0, "", [25.0, 36.3, 0.7]],
    ["LAUNDRY",         22.1,  40.56, 37.3,  49.64, 10, "utility", 0, "", [28.6, 45.3, 1.3]],
    // ---- bedroom 2 suite and the bunk room
    ["BEDROOM 2",       7.27,  35.46, 22.1,  48.13, 10, "bed", 0, "", [14.7, 46.4, 1.5]],
    ["",                13.78, 48.13, 22.1,  53.75, 10, "hall"],   // suite entry
    ["",                13.78, 53.75, 17.5,  55.3,  0,  "hall"],
    ["WC",              7.27,  48.13, 13.78, 55.3,  10, "bath", 0, "", [10.5, 53.5, 0.8]],   // ensuite WC + wardrobe wall
    ["BATH 2",          7.27,  55.3,  17.5,  62.04, 10, "bath", 0, "", [13.2, 57.3, 1.1]],
    ["BUNK ROOM",       17.5,  53.75, 22.1,  66.64, 10, "bed", 0, "", [19.8, 63.5, 0.8]],
    ["",                22.1,  55.6,  32.6,  66.64, 10, "bed"],
    ["STUDY",           32.6,  55.6,  42.65, 63.42, 10, "office", 0, "", [38.2, 61.6, 1.3]],
    // ---- halls and the stair
    ["HALL",            22.1,  49.64, 42.65, 55.6,  10, "hall", 0, "", [33, 52.2, 1.1]],
    ["",                37.3,  35.46, 42.65, 49.64, 10, "hall"],
    ["STAIR DN",        42.65, 35.46, 47.27, stairb_top_y(), 0, "stairwell", 0, "", [44.95, 41.0, 0.8, 90]],
    ["",                42.65, stairb_top_y(), 47.27, 55.6, 10, "hall"],   // landing at the stair top
    ["HALL",            24.34, 29.51, 54.6,  35.46, 10, "hall", 0, "", [38, 32.6, 1.3]],
    ["BATH",            47.27, 35.46, 54.6,  45.39, 10, "bath", 0, "", [50.9, 42.5, 1.0]],
    [["BROOM /", "LINEN"], 47.27, 45.39, 54.6, 50.69, 10, "closet", 0, "", [50.9, 47.8, 0.8]],
    // sun room (two pieces) and the covered patio (no walls)
    ["SUN ROOM",        47.27, 50.69, 54.6,  63.42, 10, "living", 0, "", [51.0, 56.0, 0.9]],
    ["",                42.65, 55.6,  47.27, 63.42, 10, "living"],
    ["PATIO",           54.6,  50.69, 69.14, 63.42, 0,  "porch", 0, "", [61.8, 58.0, 1.3]],
    // ---- front band, west to east: library, breakfast, dining + butler, foyer, den, media
    ["LIBRARY",         35.6,  6.28,  54.6,  18.0,  10, "living", 0, "", [45, 12.3, 1.5]],
    ["BREAKFAST",       35.6,  18.0,  54.6,  29.51, 10, "dining", 0, "", [45, 24.5, 1.3]],
    ["DINING ROOM",     54.6,  2.0,   69.14, 22.0,  12, "dining", 0, "", [61.8, 12.5, 1.5]],
    ["",                60.5,  22.0,  69.14, 29.51, 12, "dining"],                 // dining room, north end (direct to the kitchen)
    ["BUTLER",          54.6,  22.0,  60.5,  29.51, 10, "utility", 0, "", [57.5, 25.7, 0.8]],
    ["VESTIBULE",       69.14, 5.0,   81.12, 10.5,  10, "hall", 0, "", [75.1, 7.4, 1.0]],
    ["FOYER",           69.14, 10.5,  81.12, 22.0,  12, "hall", 0, "", [75.1, 16.0, 1.6]],
    ["FOYER",           69.14, 22.0,  76.0,  29.51, 12, "hall", 0, "", [72.6, 25.0, 0.8]],
    ["POWDER",          76.0,  22.0,  81.12, 29.51, 10, "bath", 0, "", [78.5, 26.0, 0.7]],
    ["DEN",             81.12, 2.0,   95.95, 17.5,  12, "living", 0, "", [88.5, 9.8, 1.8]],
    ["MEDIA",           81.12, 17.5,  95.95, 29.51, 12, "living", 0, "", [88.5, 23.5, 1.5]],
    // ---- kitchen, great room, gallery
    [["KITCHEN"],       54.6,  29.51, 69.14, 50.69, 12, "kitchen", 0, "", [61.8, 47.0, 1.6]],
    ["GREAT ROOM",      69.14, 35.46, 95.63, 52.53, 12, "living", 0, "", [83, 48.6, 2]],
    ["HALL",            69.14, 29.51, 105.2, 35.46, 10, "hall", 0, "", [87, 32.5, 1.3]],
    // ---- office and the master suite
    ["OFFICE",          95.63, 35.46, 108.62, 48.16, 10, "office", 0, "", [102.1, 46.3, 1.3]],
    [["MASTER", "BEDROOM"], 108.62, 29.51, 126.97, 52.86, 10, "bed", 0, "", [117.8, 48.2, 1.6]],
    ["",                105.2, 29.51, 108.62, 35.46, 10, "hall"],          // master entry
    ["WIC",             95.95, 20.56, 106.51, 29.51, 10, "closet", 0, "", [101.2, 25.1, 1.2]],
    ["",                106.51, 20.56, 112.0, 29.51, 10, "hall"],          // closet passage (3 ft opening)
    ["WIC",             112.0, 20.56, 121.94, 29.51, 10, "closet", 0, "", [117.0, 25.1, 1.2]],
    [["MASTER", "LAUNDRY"], 121.94, 20.56, 128.13, 29.51, 10, "utility", 0, "", [123.9, 25.1, 0.8, 90]],
    [["MASTER", "BATH"], 106.51, 9.31, 128.13, 20.56, 10, "bath", 0, "", [117, 16, 1.3]],
    ["MECH",            95.95, 9.31,  99.7,  20.56, 10, "utility", 0, "", [96.9, 14.5, 0.6, 90]],   // heating/ventilation closet for the east side
    ["WC",              99.7,  16.71, 106.51, 20.56, 10, "bath", 0, "", [104.9, 19.6, 0.7]],
    ["",                99.7,  13.09, 106.51, 16.71, 10, "closet"],         // linen between the WCs
    ["WC",              99.7,  9.31,  106.51, 13.09, 10, "bath", 0, "", [104.9, 12.3, 0.7]],
    // ---- porches (no walls)
    ["FRONT PORCH",     49.24, -13.26, 101.41, 2.0,  0, "porch", 0, "", [61, -7, 1.8]],
    ["",                49.24, 2.0,    54.6,   6.28, 0, "porch"],
    ["",                95.95, 2.0,    101.41, 9.31, 0, "porch"],
    ["",                69.14, 2.0,    81.12,  5.0,  0, "porch"],           // covered entry
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
    [72.0,   5.0,   "x", 6.2,  "double",  1],      // front door (into the vestibule)
    [69.6,   5.0,   "x", 2.0,  "glass"],           //   sidelights
    [78.6,   5.0,   "x", 2.0,  "glass"],
    [58.5,   2.0,   "x", 6.0,  "double",  1],      // dining room to the front porch
    [37.0,   63.42, "x", 3.75, "double",  1],      // study to its stoop
    [99.0,   48.16, "x", 6.5,  "double",  1],      // office to the office porch
    [114.1,  52.86, "x", 6.05, "double",  1],      // master bedroom to the master porch
    [2.0,    7.9,   "x", 9,    "garage"],          // garage doors now face south
    [12.5,   7.9,   "x", 9,    "garage"],
    [2.43,   35.46, "x", 3.0,  "door",    1],      // garage side door
    [24.34,  16.1,  "y", 3.0,  "door",   -1],      // garage to the side entry
    // ---- service side
    [24.34,  22.3,  "y", 3.0,  "door",    1],      // garage to the pantry: the Costco door (3 steps up)
    [28.5,   20.82, "x", 3.0,  "door",   -1],      // pantry to the side-entry porch
    [30.5,   29.51, "x", 3.0,  "door",    1],      // pantry to the hall
    [35.6,   22.3,  "y", 3.0,  "door",    1],      // pantry to the breakfast room
    [24.34,  31.9,  "y", 3.0,  "door",    1],      // garage to the hall (mud entry)
    [28.2,   35.46, "x", 8.8,  "full"],            // hall / mudroom
    [31.0,   40.56, "x", 3.0,  "door",   -1],      // mudroom to laundry
    [25.0,   49.64, "x", 3.0,  "door",   -1],      // laundry from the bedroom hall
    [22.1,   36.6,  "y", 3.0,  "door",   -1],      // BEDROOM 2 to its WIC
    // ---- bedroom wing
    [22.1,   50.0,  "y", 3.0,  "door",   -1],      // bedroom 2 suite
    [14.0,   48.13, "x", 7.9,  "full"],            //   suite entry / bedroom
    [13.9,   53.75, "x", 3.5,  "full"],            //   the entry's two pieces
    [14.2,   55.3,  "x", 3.0,  "door",    1],      //   bath 2
    [8.0,    55.3,  "x", 3.0,  "door",   -1],      //   WC, off bath 2
    [8.0,    48.13, "x", 3.0,  "door",   -1],      //   BEDROOM 2 to its ensuite WC
    [17.5,   56.8,  "y", 3.0,  "door",    1],      // bunk room to bath 2 (opens into the bunk room)
    [22.1,   57.2,  "y", 6.0,  "full"],            // bunk room, its two pieces
    [29.4,   55.6,  "x", 3.0,  "door",    1],      // bunk room
    [33.0,   55.6,  "x", 3.0,  "door",    1],      // study
    [37.5,   49.64, "x", 5.0,  "full"],            // bedroom hall / north-south hall
    [37.6,   35.46, "x", 4.8,  "full"],            // north-south hall / service hall
    // ---- stair and the sun room
    [42.9,   stairb_top_y(), "x", 4.1, "full"],    // top of the stair
    [42.65,  51.2,  "y", 4.0,  "full"],            // bedroom hall / stair landing
    [47.27,  51.2,  "y", 4.0,  "double",  1],      // stair landing / sun room
    [47.27,  56.2,  "y", 5.5,  "full"],            // sun room, its two pieces
    [54.6,   53.9,  "y", 4.9,  "double",  1],      // sun room -> patio
    [48.4,   50.69, "x", 3.0,  "door",   -1],      // sun room to the broom/linen closet
    [48.4,   35.46, "x", 3.0,  "door",    1],      // hall bath, off the service hall
    // ---- front band, kitchen, great room
    [54.6,   29.8,  "y", 5.4,  "full"],            // service hall / kitchen
    [55.4,   29.51, "x", 4.0,  "full"],            // kitchen / butler
    [61.0,   29.51, "x", 6.0,  "full"],            // kitchen / dining room (direct)
    [55.4,   22.0,  "x", 4.0,  "full"],            // butler / dining
    [54.6,   23.5,  "y", 5.0,  "full"],            // butler / breakfast
    [69.14,  24.0,  "y", 3.0,  "door",   -1],      // dining room to the foyer (bypass of the kitchen)
    [54.6,   8.0,   "y", 5.0,  "double",  1],      // dining / library (French doors)
    [38.5,   18.0,  "x", 6.0,  "full"],            // library / breakfast
    [64.0,   50.69, "x", 4.6,  "double", -1],      // kitchen to the covered patio
    [69.14,  38.0,  "y", 6.0,  "full"],            // kitchen / great room
    [69.14,  29.8,  "y", 5.4,  "full"],            // kitchen / gallery
    [71.0,   10.5,  "x", 5.0,  "double",  1],      // vestibule / foyer
    [69.4,   22.0,  "x", 6.5,  "full"],            // foyer / foyer passage
    [77.4,   22.0,  "x", 3.0,  "door",   -1],      // foyer to the powder room
    [69.4,   29.51, "x", 6.5,  "full"],            // foyer passage / gallery
    [69.4,   35.46, "x", 26.0, "full"],            // gallery / great room
    [81.12,  11.8,  "y", 5.0,  "double",  1],      // foyer / den
    [84.0,   17.5,  "x", 8.0,  "full"],            // den / media
    [83.0,   29.51, "x", 8.0,  "full"],            // media / gallery
    [70.65,  52.53, "x", 6.0,  "double", -1],      // great room to the deck
    // ---- office and the master suite
    [99.3,   35.46, "x", 4.7,  "double",  1],      // office
    [105.2,  29.95, "y", 4.6,  "double",  1],      // master suite
    [108.62, 29.8,  "y", 5.4,  "full"],            //   entry / bedroom
    [108.9,  29.51, "x", 3.0,  "open"],            //   bedroom / closet passage (3 ft)
    [106.51, 23.6,  "y", 3.0,  "door",   -1],      //   west closet
    [112.0,  23.6,  "y", 3.0,  "door",    1],      //   east closet
    [107.1,  20.56, "x", 3.0,  "door",   -1],      //   master bath
    [122.6,  20.56, "x", 3.0,  "door",    1],      //   master laundry, from the bath
    [121.94, 23.6,  "y", 3.0,  "door",   -1],      //   master laundry, from the east closet
    [106.51, 17.0,  "y", 3.0,  "door",   -1],      //   WC
    [106.51, 13.4,  "y", 3.0,  "door",   -1],      //   linen between the WCs
    [106.51, 9.8,   "y", 3.0,  "door",   -1],      //   WC
    [95.95,  12.0,  "y", 3.0,  "door",   -1],      // den to the east-side mechanical closet
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [33.0,   63.42, "x", 3.0, 2.5,  5],      // study, in its corner
    [96.4,   48.16, "x", 2.6, 2.5,  5],      // office, in its corner
    [17.5,   63.0,  "y", 3.0, 2.5,  5],      // bunk room, west corner
    [25.0,   66.64, "x", 3.5, 2.5,  5],      //   and north
    [7.27,   36.3,  "y", 4.0, 2.75, 5],      // bedroom 2, windows pulled to the corners
    [7.27,   43.6,  "y", 4.0, 2.75, 5],
    [43.0,   63.42, "x", 3.5, 1.5,  6.5],    // sun room
    [48.5,   63.42, "x", 5.0, 1.5,  6.5],
    [54.6,   59.3,  "y", 3.6, 1.5,  6.5],    //   and beside its doors to the patio
    [77.8,   52.53, "x", 3.6, 2,    6],      // great room
    [89.4,   52.53, "x", 4.3, 2,    6],
    [110.0,  52.86, "x", 2.5, 2.5,  5],      // master bedroom
    [126.97, 46.0,  "y", 4.7, 2.5,  5],
    [126.97, 31.0,  "y", 4.0, 2.5,  5],
    [128.13, 9.8,   "y", 4.6, 3.5,  4],      // master bath
    [128.13, 21.3,  "y", 3.6, 4,    3],      // master laundry (dryer vent wall)
    [82.5,   2.0,   "x", 5.0, 2.5,  5.5],    // den
    [95.95,  3.0,   "y", 5.0, 2.5,  5.5],
    [54.6,   3.0,   "y", 3.0, 2.5,  5.5],    // dining room, west
    [55.8,   2.0,   "x", 2.5, 2.5,  5.5],    //   and south, by the French doors
    [37.7,   6.28,  "x", 5.0, 2.5,  5.5],    // library
    [46.0,   6.28,  "x", 5.0, 2.5,  5.5],
    [35.6,   8.0,   "y", 5.0, 2.5,  5.5],
    [35.6,   18.5,  "y", 2.2, 3.0,  4],      // breakfast room, to the side porch
    [57.0,   50.69, "x", 4.5, 3.0,  3.5],    // kitchen, over the sink
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: west run on the inside wall (tall pantry cabinet, range, fridge at the
    // end of the run), north sink run under the window, island (no seating, no sink)
    [54.8,   35.9,  57.3,   38.0,  0, 7,    wood],      // tall pantry cabinet, end of the run
    [54.8,   38.0,  57.3,   45.6,  0, 3,    counter],
    [54.9,   41.0,  57.2,   44.0,  3, 3.05, dark],      // range
    [54.8,   46.0,  57.3,   49.2,  0, 7,    steel],     // fridge
    [57.3,   48.6,  63.5,   50.5,  0, 3,    counter],
    [57.4,   48.7,  59.4,   50.4,  0, 3,    steel],     // dishwasher
    [59.6,   48.8,  62.0,   50.3,  3, 3.05, basin],     // sink
    [61.8,   36.8,  65.8,   44.0,  0, 3,    wood],      // island
    // butler's pantry: coffee bar and prep sink on the east wall
    [58.6,   23.0,  60.3,   29.2,  0, 3,    counter],   // coffee bar
    [54.8,   26.4,  56.4,   29.2,  0, 7,    shelf],
    // pantry (Costco store), laundry, mudroom
    [24.74,  27.6,  30.0,   29.3,  0, 7,    shelf],
    [33.2,   27.6,  35.4,   29.3,  0, 7,    shelf],
    [24.74,  20.98, 27.8,   22.1,  0, 7,    shelf],
    [32.0,   20.98, 35.4,   22.5,  0, 3,    counter],
    [32.8,   21.1,  34.6,   22.4,  3, 3.05, basin],     // scullery sink
    [28.09,  47.07, 34.01,  49.05, 0, 3.2,  steel],     // washer + dryer
    [28.42,  41.02, 33.22,  43.32, 0, 3,    counter],
    [33.22,  41.02, 35.1,   43.52, 0, 3,    basin],     // laundry sink
    [22.63,  41.15, 24.41,  49.05, 0, 6,    shelf],     // drying rack
    [35.2,   41.15, 36.9,   49.05, 0, 7,    wood],
    [28.2,   35.66, 29.8,   39.97, 0, 7,    wood],      // lockers
    [34.2,   37.0,  36.9,   39.97, 0, 3,    wood],      // bench + cabinets
    // baths
    [8.3,    55.6,  14.1,   58.23, 0, 2,    white],     // bath 2: tub, off the exterior wall
    [10.99,  60.1,  16.9,   61.68, 0, 3,    counter],   //   double vanity
    [11.2,   52.0,  13.5,   54.3,  0, 1.4,  white],     // WC
    [52.0,   36.0,  54.3,   38.0,  0, 3,    counter],   // hall bath: vanity by the door
    [52.3,   39.5,  54.1,   41.1,  0, 1.4,  white],     //   toilet between door and shower
    [49.6,   41.9,  54.3,   45.1,  0, 0.02, tile],      //   curbless shower, far end
    [111.64, 17.86, 121.51, 19.64, 0, 3,    counter],   // master bath: double vanity
    [111.97, 9.55,  120.2,  14.05, 0, 0.02, tile],      //   curbless shower
    [121.2,  12.6,  125.7,  18.0,  0, 2,    white],     //   freestanding tub, off the walls
    [100.79, 17.01, 103.42, 19.31, 0, 1.4,  white],     // WCs
    [100.79, 9.77,  103.42, 12.07, 0, 1.4,  white],
    [78.9,   26.9,  80.8,   28.9,  0, 1.4,  white],     // powder room
    [79.6,   23.1,  80.9,   25.4,  0, 3,    counter],
    // master laundry
    [122.4,  26.0,  127.5,  29.0,  0, 3.2,  steel],     // washer + dryer
    [122.4,  23.9,  127.5,  25.7,  0, 3,    counter],
    // closets and storage
    [96.51,  27.2,  106.05, 28.91, 0, 7,    shelf],
    [96.51,  22.93, 98.16,  27.2,  0, 7,    shelf],
    [96.51,  21.15, 106.05, 22.93, 0, 7,    shelf],
    [112.5,  27.2,  121.38, 28.91, 0, 7,    shelf],
    [112.5,  21.15, 121.38, 22.93, 0, 7,    shelf],
    [47.5,   46.0,  54.3,   47.4,  0, 7,    shelf],     // broom / linen
    [69.67,  14.0,  71.38,  21.4,  0, 7,    wood],      // foyer coat storage
    [69.67,  22.9,  71.0,   29.1,  0, 3,    wood],      //   drop shelf + mail
    [69.4,   6.0,   70.9,   9.8,   0, 1.5,  wood],      // vestibule bench
    [81.58,  51.41, 89.61,  52.14, 0, 4,    hearth],    // great room fireplace
];

// furniture, as drawn on the plan
function main_furniture() = [
    [14.8,   40.03, 19.21,  44.64, 0, 2,    bed],       // bedroom 2
    [7.7,    40.6,  10.0,   43.5,  0, 2.6,  sofa],
    [10.66,  35.76, 14.93,  37.4,  0, 2.5,  wood],
    [29.2,   58.8,  32.4,   65.3,  0, 5,    bed],       // bunk beds, clear of the windows
    [23.0,   56.0,  26.2,   62.5,  0, 5,    bed],
    [35.99,  58.68, 39.93,  61.76, 0, 2.5,  wood],      // study
    [36.64,  56.05, 41.91,  57.5,  0, 3,    wood],
    [48.0,   60.76, 52.78,  62.99, 0, 2.6,  sofa],      // sitting room
    [43.09,  57.0,  45.53,  62.0,  0, 2.6,  sofa],
    [58.68,  56.48, 62.96,  60.76, 0, 2.5,  table, "", "round"],   // patio table
    [60.0,   8.0,   63.8,   16.5,  0, 2.5,  table],     // dining table, 8 seats
    [40.0,   8.0,   46.0,   9.4,   0, 2.6,  sofa],      // library
    [38.0,   12.0,  39.2,   17.0,  0, 7,    shelf],     //   bookshelves
    [38.0,   6.7,   52.0,   7.6,   0, 7,    shelf],
    [43.5,   21.5,  48.0,   25.5,  0, 2.5,  table, "", "round"],   // breakfast table
    [43.0,   27.9,  50.0,   29.3,  0, 1.5,  sofa],      //   banquette (one side), chairs on the rest
    [70.53,  40.03, 73.82,  46.61, 0, 2.6,  sofa],      // great room
    [74.14,  39.05, 79.74,  41.55, 0, 2.6,  sofa],
    [75.79,  42.34, 79.74,  46.28, 0, 1.5,  table],
    [96.64,  38.39, 99.8,   44.97, 0, 2.5,  wood],      // office desks
    [105.07, 38.39, 108.22, 44.97, 0, 2.5,  wood],
    [116.25, 37.07, 122.17, 43.65, 0, 2,    bed],       // master bedroom
    [109.34, 39.05, 111.32, 44.64, 0, 3,    wood],
    [84.8,   12.5,  89.8,   14.8,  0, 2.6,  sofa],      // den
    [83.5,   4.5,   90.0,   6.0,   0, 1.5,  wood],
    [84.0,   20.0,  90.0,   22.2,  0, 2.6,  sofa],      // media room
    [96.84,  13.39, 98.82,  16.02, 0, 3,    wood],
];

// steps from the porches down to grade [x, y, direction, width]: four
// 6" risers (house_lib's porch_steps)
function main_porch_steps() = [
    [69.6,  -13.26, "-y", 11.0],   // front entry
    [70.0,   64.7,  "+y", 24.8],   // deck to the yard
    [111.0,  62.4,  "+y", 13.6],   // master porch to the yard
    [24.8,   13.39, "-y", 10.3],   // side entry
    [37.0,   66.6,  "+y", 3.8],    // study stoop
];
// garage steps up to the house [y0, y1]: a landing at house level
// (x 21.8-24.14) and two 6" steps down to the garage slab; the Costco door
// (y 21.5-25.5) has its own three-step run and landing
function garage_steps() = [[30.5, 35.2], [15.6, 19.6], [21.5, 25.5]];

// porch posts [x, y, height]
function main_posts() = [
    [49.69, -12.81, 9.5], [57.4, -12.81, 9.5], [65.1, -12.81, 9.5], [69.2, -12.81, 9.5],
    [81.1, -12.81, 9.5], [88.6, -12.81, 9.5], [96.3, -12.81, 9.5], [100.96, -12.81, 9.5],
    [49.69, -5.0, 9.5], [49.69, 5.83, 9.5], [100.96, -5.0, 9.5], [100.96, 8.86, 9.5],
    [69.59, 64.25, 10], [95.18, 64.25, 10],
    [68.89, 63.17, 10], [61.55, 63.17, 10],                 // patio: open corner + north edge
    [108.17, 59.02, 10], [109.07, 61.95, 10], [126.52, 61.95, 10],
    [127.42, 59.02, 10], [137.21, 59.02, 10], [137.21, 51.1, 10], [137.21, 43.2, 10],
    [137.21, 35.2, 10], [137.21, 27.29, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,      7.9,   24.34,  35.46, 8.5, 0.5,   1.5],   // garage
    [7.27,   35.46, 37.3,   66.64, 10,  0.5,   1.5],   // bedroom wing
    [37.3,   35.46, 69.14,  63.42, 10,  0.5,   1.5],   // study, sun room, kitchen, patio
    [69.14,  29.51, 95.63,  52.53, 12,  0.5,   1.5],   // great room, gallery
    [95.63,  29.51, 126.97, 52.86, 10,  0.5,   1.5],   // office, master bedroom
    [24.34,  6.28,  69.14,  35.46, 12,  0.5,   1.5],   // library, breakfast, pantry, butler, service hall
    [54.6,   2.0,   69.14,  6.28,  10,  0.5,   1.5],   // dining room, south end
    [69.14,  5.0,   81.12,  29.51, 12,  0.5,   1.5],   // vestibule, foyer, powder
    [81.12,  2.0,   95.95,  29.51, 12,  0.5,   1.5],   // den, media
    [95.95,  9.31,  128.13, 29.51, 10,  0.5,   1.5],   // master closets + bath
    [49.24, -13.26, 101.41, 2.0,   9.5, 0.333, 1],     // front porch
    [49.24,  2.0,   54.6,   6.28,  9.5, 0.333, 1],
    [95.95,  2.0,   101.41, 9.31,  9.5, 0.333, 1],
    [69.14,  52.53, 95.63,  64.7,  10,  0.333, 1],     // deck
    [95.63,  48.16, 108.62, 59.47, 10,  0.333, 1],     // office porch
    [108.62, 52.86, 126.97, 62.4,  10,  0.333, 1],     // master porch
    [126.97, 26.84, 137.66, 59.47, 10,  0.333, 1],     // side porch
];

// The main floor assembly (trusses + subfloor) under the heated rooms,
// with the (longer, two-flight) stair opening left out.
module floor_assembly(rooms) {
    paint(floor_frame())
        difference() {
            union()
                for (r = rooms)
                    if (r[6] != "porch" && r[6] != "garage" && r[6] != "stairwell")
                        translate([r[1] - wall_t() / 2, r[2] - wall_t() / 2, -main_floor_depth()])
                            cube([r[3] - r[1] + wall_t(), r[4] - r[2] + wall_t(), main_floor_depth() - 0.15]);
            translate([stair_x()[0] + wall_t() / 2 + 0.01, 35.46 + wall_t() / 2 + 0.01, -5])
                cube([stair_x()[1] - stair_x()[0] - wall_t() - 0.02, stairb_top_y() - 35.46 - wall_t() / 2 - 0.01, 10]);
        }
}

// guard along the patio's north edge (over the exit-stair areaway): 44 in (CODE-05)
module patio_guard() {
    rail = [0.22, 0.22, 0.24];
    y = 63.3; x0 = 54.6; x1 = 68.89;
    paint(rail) {
        for (x = [x0 + 0.1 : (x1 - x0 - 0.2) / 4 : x1 + 0.01])
            translate([x - 0.08, y - 0.08, 0]) cube([0.16, 0.16, 3.67]);
        translate([x0, y - 0.1, 3.52]) cube([x1 - x0, 0.2, 0.15]);
        translate([x0, y - 0.06, 1.75]) cube([x1 - x0, 0.12, 0.1]);
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

    if (show_stair) main_stair_b();
    for (y = garage_steps())
        paint(stair_color()) {
            translate([21.8, y[0], -1.5]) cube([2.34, y[1] - y[0], 1.5]);
            translate([20.6, y[0], -1.5]) cube([1.2, y[1] - y[0], 1.0]);
            translate([19.4, y[0], -1.5]) cube([1.2, y[1] - y[0], 0.5]);
        }

    for (p = main_posts()) post(p[0], p[1], p[2]);
    patio_guard();
    for (p = main_porch_steps()) porch_steps(p[0], p[1], p[2], p[3]);

    if (show_roof) roofs(main_roof(), roof_color, roof_opacity);
}
