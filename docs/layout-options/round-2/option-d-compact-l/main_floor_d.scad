// OPTION D - COMPACT L (round 2), main floor.
// Kayla's K-088 ranch pattern: "L shaped, one wing public, one private, private back patio".
// Units: feet, x = east, y = north, rooms are wall-centre-line rectangles,
// door/window x,y = the LOW end of the opening. Road south (site.scad:8).
// Visualisation only - NOT construction documents.
//
// THE PLAN IN ONE PARAGRAPH
//   PUBLIC WING (south, y 0-21.6, x 24.4-88.4): garage (west end, doors face the
//   road, slab at house level so the garage entry is step-free) -> mudroom and
//   pantry (Costco door to the garage) -> kitchen -> dining + nook -> living room
//   -> vestibule/foyer. PRIVATE WING (north, x 74-105, y 21.6-70): it rises from
//   the foyer along a 6 ft hall. The hub on that hall holds the straight stair
//   (top landing at y 27), the stacked 6 x 7 ft elevator space (x 88.4-94.4,
//   y 21.6-29) and the bath/linen closets; bedroom 2 is on the east wall;
//   the primary suite (bedroom NE, ensuite, two walk-ins, laundry) is at the
//   north end, entered through a short suite hall. The BACK PATIO sits in the L's
//   elbow (north of kitchen/dining/living, west of the stair). Guests' bath is
//   off the foyer (it doubles as the powder room).
// Stair: one straight flight, NO landing, runs NORTH from the top nosing at y 27.0
//   (19 risers, 18 treads of 10.5 in, floor-to-floor 11.75 ft); stairwell
//   x 77.8-82.4 = 4.2 ft = 50 in clear, a "straight stair-lift-ready flight".
// Hard target: heated footprint excl. garage <= 3,000 sq ft (outside face).

use <house_lib_d.scad>

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
circ     = [0.80, 0.88, 1.00];   // a 1,700 mm (5.58 ft) turning circle, drawn as a thin disc

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function main_rooms() = [
    // ---- public wing (south): garage, service strip, kitchen, dining, living, entry
    ["GARAGE",          0,     0,     24.4,  24.4, 10, "garage", 0, "", [12, 12, 2]],
    ["MUDROOM",         24.4,  0,     32.8,  11.6, 10, "utility", 0, "", [28.6, 6.0, 1.0]],
    ["PANTRY",          24.4,  11.6,  32.8,  21.6, 10, "utility", 0, "", [28.6, 16.6, 1.1]],
    ["KITCHEN",         32.8,  0,     48.2,  21.6, 12, "kitchen", 0, "", [40.5, 15.5, 1.7]],
    [["DINING +", "NOOK"], 48.2, 0,   62.4,  21.6, 12, "dining", 0, "", [55.3, 8.0, 1.4]],
    ["LIVING ROOM",     62.4,  0,     82.4,  21.6, 12, "living", 0, "", [72.4, 11.0, 1.8]],
    ["VESTIBULE",       82.4,  0,     88.4,  8.0,  10, "hall", 0, "", [85.4, 6.2, 0.7]],
    ["FOYER",           82.4,  8.0,   88.4,  21.6, 12, "hall", 0, "", [85.4, 15.0, 1.4]],
    ["BATH",            88.4,  11.6,  96.4,  21.6, 10, "bath", 0, "", [92.4, 14.4, 1.1]],
    // ---- the hub and the hall of the private wing
    ["HALL",            82.4,  21.6,  88.4,  41.2, 10, "hall", 0, "", [85.4, 33.0, 1.2, 90]],
    ["",                77.8,  21.6,  82.4,  27.0, 10, "hall"],                 // stair top landing
    ["STAIR DN",        77.8,  27.0,  82.4,  38.5, 0,  "stairwell", 0, "", [80.1, 32.7, 0.8, 90]],
    ["LINEN",           77.8,  38.5,  82.4,  41.2, 10, "closet", 0, "", [80.1, 39.85, 0.6]],
    [["ELEVATOR", "(FUTURE)"], 88.4, 21.6, 94.4, 29.0, 10, "closet", 0, "", [91.4, 25.3, 0.8]],
    // ---- bedroom 2 and its closet
    [["BEDROOM", "2"],  88.4,  29.0,  100.2, 41.2, 10, "bed", 0, "", [94.3, 36.0, 1.3]],
    [["BR 2", "CLOSET"], 94.4, 21.6,  100.2, 29.0, 10, "closet", 0, "", [97.3, 25.3, 0.7]],
    // ---- primary suite
    ["LAUNDRY",         74.0,  41.2,  82.4,  49.6, 10, "utility", 0, "", [78.2, 47.6, 1.0]],
    ["",                82.4,  41.2,  88.4,  49.6, 10, "hall"],                 // suite hall
    ["WIC",             88.4,  41.2,  96.4,  49.6, 10, "closet", 0, "", [92.4, 45.4, 1.0]],
    ["WIC",             96.4,  41.2,  105.0, 49.6, 10, "closet", 0, "", [100.7, 45.4, 1.0]],
    [["MASTER", "BATH"], 74.0, 49.6,  83.0,  62.0, 10, "bath", 0, "", [78.5, 53.0, 1.0]],
    ["WC",              74.0,  62.0,  78.6,  69.5, 10, "bath", 0, "", [76.3, 64.5, 0.8]],
    ["SHOWER",          78.6,  62.0,  83.0,  69.5, 10, "bath", 0, "", [80.8, 64.5, 0.7]],
    [["MASTER", "BEDROOM"], 83.0, 49.6, 105.0, 69.5, 10, "bed", 0, "", [94.0, 55.0, 1.6]],
    // ---- porches and the drive (no walls)
    ["DRIVE",           0,     -16,   24.4,  0,    0, "porch", 0, "", [12, -8, 1.6]],
    [["MUD", "STOOP"],  28.0,  -5.0,  32.8,  0,    0, "porch", 0, "", [30.4, -2.4, 0.6]],
    ["FRONT PORCH",     79.0,  -8.0,  91.8,  0,    0, "porch", 0, "", [85.4, -4.2, 1.0]],
    ["PATIO",           36.0,  21.6,  77.8,  34.0, 0, "porch", 0, "", [57, 27.8, 1.8]],     // the back patio in the L's elbow
    ["DECK",            105.0, 54.0,  113.0, 68.0, 0, "porch", 0, "", [109, 61, 1.2]],     // the primary suite's private deck
];

// [x, y, axis, width, type, swing, tag]
function main_doors() = [
    // ---- exterior
    [82.8,   0,     "x", 5.0,  "double",  1],      // front door
    [4.0,    0,     "x", 16,   "garage"],          // garage door (faces the road)
    [29.4,   0,     "x", 3.0,  "door",    1],      // mudroom to its covered stoop
    [53.0,   21.6,  "x", 6.0,  "double",  1],      // dining to the back patio
    [69.5,   21.6,  "x", 6.0,  "double",  1],      // living to the back patio
    [105.0,  56.0,  "y", 6.0,  "double",  1],      // primary bedroom to its porch
    // ---- garage, mudroom, pantry, kitchen
    [24.4,   3.0,   "y", 3.0,  "door",    1],      // garage to mudroom (step-free, slab at house level)
    [24.4,   14.0,  "y", 3.0,  "door",    1],      // Costco door: garage to pantry
    [32.8,   7.6,   "y", 4.0,  "open"],            // mudroom to kitchen (opens onto the clear lane)
    [32.8,   14.0,  "y", 3.0,  "door",    1],      // pantry to kitchen
    [48.2,   11.0,  "y", 9.0,  "full"],            // kitchen / dining (the lane runs straight through)
    [62.4,   4.0,   "y", 6.0,  "open"],            // dining / living
    // ---- entry
    [83.2,   8.0,   "x", 4.8,  "open"],            // vestibule to foyer
    [82.4,   10.0,  "y", 6.0,  "open"],            // foyer to living room
    [88.4,   12.4,  "y", 3.0,  "door",    1],      // foyer to guest bath
    [82.6,   21.6,  "x", 5.6,  "full"],            // foyer to hall
    // ---- hub, stair, elevator, bedroom 2
    [82.4,   22.0,  "y", 4.8,  "open"],            // hall to the stair landing
    [78.0,   27.0,  "x", 4.2,  "full"],            // top of the stair
    [88.4,   22.4,  "y", 3.0,  "door",    1],      // elevator door (framed as a closet door)
    [88.4,   30.5,  "y", 3.0,  "door",    1],      // bedroom 2
    [95.0,   29.0,  "x", 3.0,  "open"],            // bedroom 2 closet
    [82.4,   38.7,  "y", 2.4,  "open"],            // linen
    // ---- primary suite
    [84.4,   41.2,  "x", 3.0,  "door",    1],      // hall to suite hall
    [82.4,   43.0,  "y", 3.0,  "door",   -1],      // suite hall to laundry
    [83.4,   49.6,  "x", 3.0,  "door",    1],      // suite hall to primary bedroom
    [89.4,   49.6,  "x", 4.0,  "open"],            // walk-in 1
    [98.4,   49.6,  "x", 4.0,  "open"],            // walk-in 2
    [75.5,   49.6,  "x", 3.0,  "door",   -1],      // laundry to ensuite
    [83.0,   56.0,  "y", 3.0,  "door",    1],      // ensuite to bedroom
    [75.5,   62.0,  "x", 2.8,  "door",    1],      // WC
    [79.4,   62.0,  "x", 3.0,  "open"],            // curbless shower
];

// [x, y, axis, width, sill, height]
function main_windows() = [
    [26.0,   0,     "x", 3.0, 3.0, 3.5],      // mudroom
    [34.5,   0,     "x", 5.0, 3.5, 3.5],      // kitchen, over the sink
    [43.5,   21.6,  "x", 3.5, 3.5, 3.5],      // kitchen, over the range run (diagonal to the sink window)
    [50.0,   0,     "x", 3.0, 2.0, 5.0],      // dining
    [55.0,   0,     "x", 6.0, 2.5, 4.5],      // nook
    [70.0,   0,     "x", 10.0, 2.0, 6.0],     // living, south (diagonal to the north window)
    [63.0,   21.6,  "x", 5.0, 2.5, 5.0],      // living, north (patio)
    [96.4,   13.5,  "y", 2.5, 4.5, 2.5],      // guest bath
    [100.2,  31.5,  "y", 5.0, 2.5, 5.0],      // bedroom 2, east
    [74.0,   43.5,  "y", 3.0, 3.5, 3.5],      // laundry, west
    [74.0,   53.0,  "y", 3.0, 4.0, 3.0],      // master bath
    [75.5,   69.5,  "x", 2.0, 5.0, 2.0],      // WC
    [79.8,   69.5,  "x", 2.4, 5.0, 2.0],      // shower
    [84.4,   69.5,  "x", 5.0, 2.5, 5.5],      // primary bedroom, north: pulled to the corners, none behind the bed
    [99.0,   69.5,  "x", 5.0, 2.5, 5.5],
    [105.0,  64.0,  "y", 4.0, 2.5, 5.5],      // primary bedroom, east
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function main_fixtures() = [
    // kitchen: sink + dishwasher + range run on the south wall (sink under the window), island with
    // nothing in it, fridge by the pantry door at the north-west corner. The north half is a clear
    // 8 ft lane from the mudroom opening to the dining opening, outside the work zone.
    [33.2,   0.2,   48.0,   2.2,   0, 3,    counter],
    [35.7,   0.4,   38.7,   2.0,   3, 3.05, basin],     // sink
    [38.7,   0.4,   40.7,   2.0,   0, 3.01, dark],      // dishwasher
    [43.7,   0.4,   46.7,   2.0,   3, 3.05, dark],      // range
    [33.2,   18.4,  35.7,   21.4,  0, 7,    steel],     // fridge
    [35.7,   19.4,  38.7,   21.4,  0, 7,    wood],      // tall cabinets
    [38.0,   7.0,   46.0,   10.5,  0, 3,    counter],   // island, no seating
    [38.6,   12.6,  44.2,   18.2,  0, 0.03, circ],      // 1,700 mm circle (kitchen), in the lane
    // mudroom, pantry
    [25.0,   9.6,   30.0,   11.4,  0, 7,    wood],      // lockers
    [25.0,   0.4,   29.2,   1.9,   0, 1.5,  wood],      // bench
    [24.6,   6.6,   26.2,   9.4,   0, 3,    counter],   // mail / drop zone
    [24.6,   17.4,  26.2,   21.4,  0, 7,    shelf],
    [26.2,   19.8,  32.6,   21.4,  0, 3,    counter],   // small-appliance counter
    [30.0,   11.8,  32.6,   13.8,  0, 6.5,  steel],     // upright freezer
    // dining, nook
    [49.0,   0.4,   52.5,   2.2,   0, 3,    counter],   // coffee station
    [49.0,   19.8,  52.0,   21.4,  0, 3,    wood],      // buffet
    [60.6,   0.4,   62.2,   6.0,   0, 1.5,  sofa],      // nook banquette
    [54.6,   0.4,   60.6,   1.9,   0, 1.5,  sofa],
    // coats, foyer, guest bath
    [86.8,   3.2,   88.2,   7.6,   0, 7,    wood],      // coat wardrobe in the vestibule
    [82.6,   16.5,  84.0,   21.4,  0, 7,    wood],      // coat / shoe cabinet
    [86.8,   16.6,  88.2,   20.6,  0, 3,    wood],      // mail / key drop console
    [88.6,   19.0,  92.6,   21.2,  0, 3,    counter],   // vanity
    [89.2,   19.5,  91.0,   20.9,  3, 3.05, basin],
    [94.4,   19.0,  96.0,   21.0,  0, 1.4,  white],     // toilet
    [93.0,   12.0,  96.2,   16.5,  0, 0.02, tile],      // curbless shower
    [89.4,   15.4,  95.0,   19.0,  0, 0.03, circ],      // 1,700 mm circle (guest bath)
    [82.6,   10.0,  88.2,   15.6,  0, 0.03, circ],      // 1,700 mm circle (foyer)
    // closets, linen
    [94.6,   22.0,  99.9,   23.4,  0, 7,    shelf],
    [94.6,   23.4,  95.8,   28.0,  0, 7,    shelf],
    [88.6,   41.4,  96.2,   42.8,  0, 7,    shelf],
    [96.6,   41.4,  104.8,  42.8,  0, 7,    shelf],
    [77.9,   38.7,  79.1,   41.0,  0, 7,    shelf],
    // laundry
    [74.2,   41.6,  76.5,   44.1,  0, 6.5,  steel],     // stacked washer + dryer
    [74.2,   44.2,  76.0,   46.4,  0, 3,    counter],
    [74.4,   44.6,  75.8,   46.0,  3, 3.05, basin],
    [76.6,   43.4,  82.2,   49.0,  0, 0.03, circ],      // 1,700 mm circle (laundry)
    // master bath: double vanity, curbless shower, WC room
    [74.2,   52.0,  76.2,   58.0,  0, 3,    counter],
    [74.4,   52.6,  76.0,   54.0,  3, 3.05, basin],
    [74.4,   56.0,  76.0,   57.4,  3, 3.05, basin],
    [76.8,   54.0,  82.4,   59.6,  0, 0.03, circ],      // 1,700 mm circle (master bath)
    [76.0,   66.9,  77.8,   69.1,  0, 1.4,  white],     // toilet
    [79.0,   62.4,  82.8,   69.1,  0, 0.02, tile],      // shower, flush with the floor
    // elevator: no fixtures (framed as a closet until the lift goes in)
];

// furniture
function main_furniture() = [
    [52.0,   10.0,  58.0,   16.0,  0, 2.5,  table, "", "round"],   // 72 in round table for 8
    [56.4,   2.0,   60.2,   5.4,   0, 2.5,  table],                 // nook table
    [62.6,   12.5,  64.2,   19.5,  0, 4,    hearth],                // gas fireplace + TV wall
    [74.5,   5.5,   77.5,   16.5,  0, 2.6,  sofa],                  // sectional
    [70.5,   5.5,   74.5,   8.5,   0, 2.6,  sofa],
    [68.0,   2.5,   70.4,   4.9,   0, 2.6,  sofa],                  // swivel chairs
    [68.0,   17.0,  70.4,   19.4,  0, 2.6,  sofa],
    [92.0,   31.5,  97.0,   38.2,  0, 2,    bed],                   // bedroom 2
    [89.0,   38.8,  92.8,   40.4,  0, 3,    wood],
    [45.0,   25.8,  51.0,   31.8,  0, 2.5,  table, "", "round"],  // patio: dining table under cover
    [58.0,   26.0,  62.0,   32.0,  0, 2.6,  sofa],                // patio lounge
    [64.0,   26.5,  67.0,   31.5,  0, 2.6,  sofa],
    [70.0,   25.6,  73.6,   27.6,  0, 2.5,  wood],                // patio: small desk
    [91.0,   62.0,  97.2,   69.1,  0, 2,    bed],                   // king bed, head to the north wall
    [89.8,   67.7,  90.8,   69.1,  0, 2,    wood],
    [97.6,   67.7,  98.6,   69.1,  0, 2,    wood],
    [91.5,   59.6,  96.5,   61.0,  0, 1.5,  wood],                  // bench
    [101.0,  53.0,  103.6,  55.6,  0, 2.6,  sofa],                  // armchair
    [99.0,   67.7,  103.8,  69.1,  0, 3,    wood],                  // dresser
];

// steps from the porches down to grade [x, y, direction, width]
function main_porch_steps() = [
    [83.4,  -8.0,  "-y", 5.0],    // front entry
    [113.0, 58.0,  "+x", 6.0],    // primary porch to the yard
    [50.0,  34.0,  "+y", 8.0],    // back patio to the yard
    [29.4,  -5.0,  "-y", 3.0],    // mud stoop
];

// porch posts [x, y, height]
function main_posts() = [
    [79.4, -7.6, 9.5], [91.4, -7.6, 9.5], [28.4, -4.6, 9.5], [32.4, -4.6, 9.5],
    [36.4, 33.6, 10], [56.6, 33.6, 10], [76.8, 33.6, 10],
    [112.6, 54.4, 10], [112.6, 67.6, 10],
];

// [x0, y0, x1, y1, eave, pitch, overhang]
function main_roof() = [
    [0,      0,     24.4,  24.4, 8.5, 0.5,   1.5],   // garage
    [24.4,   0,     88.4,  21.6, 12,  0.5,   1.5],   // public wing
    [88.4,   11.6,  96.4,  21.6, 10,  0.5,   1.0],   // guest bath
    [74.0,   21.6,  100.2, 41.2, 10,  0.5,   1.0],   // hub, hall, bedroom 2
    [74.0,   41.2,  105.0, 69.5, 10,  0.5,   1.5],   // primary suite
    [79.0,   -8.0,  91.8,  0,    9.5, 0.333, 1],     // front porch
    [28.0,   -5.0,  32.8,  0,    9.5, 0.333, 1],     // mud stoop
    [36.0,   21.6,  77.8,  34.0, 10,  0.333, 1],     // back patio
    [105.0,  54.0,  113.0, 68.0, 10,  0.333, 1],     // primary porch
];

// The main floor assembly (trusses + subfloor) under the heated rooms,
// with the stair opening left out.
module floor_assembly(rooms) {
    paint(floor_frame())
        difference() {
            union()
                for (r = rooms)
                    if (r[6] != "porch" && r[6] != "garage" && r[6] != "stairwell")
                        translate([r[1] - wall_t() / 2, r[2] - wall_t() / 2, -main_floor_depth()])
                            cube([r[3] - r[1] + wall_t(), r[4] - r[2] + wall_t(), main_floor_depth() - 0.15]);
            translate([stair_x()[0] + wall_t() / 2 + 0.01, stair_top_y() + 0.01, -5])
                cube([stair_x()[1] - stair_x()[0] - wall_t() - 0.02, 11.5 - 0.02, 10]);
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

    // the stair down to the basement (runs north under the suite laundry)
    if (show_stair) main_stair();

    for (p = main_posts()) post(p[0], p[1], p[2]);
    for (p = main_porch_steps()) porch_steps(p[0], p[1], p[2], p[3]);

    if (show_roof) roofs(main_roof(), roof_color, roof_opacity);
}
