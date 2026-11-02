// Basement - OpenSCAD model of the lower level.
// Units: feet. Visualisation only - NOT construction documents.
//
// Traced from docs/house/basement.jpg (the November 2026 redesign) at
// 29.7 px per ft; every room comes out within 1-2" of its labelled
// size. The drawing is registered on the main floor through the stair,
// so this file uses the main floor's coordinates (house_lib.scad), and
// z = 0 here is the basement floor (the combined model lowers it by
// floor_to_floor()).
//
// Changes from the drawing (see docs/house/Redesign-and-Spec-2026-11-02.md):
// - the stair is 15 3/4 ft long, so it runs on past the drawn stair box
//   into the hallway, and the hallway is 1.7 ft deeper (the living room
//   1.7 ft shorter) to give the foot of the stair a proper landing;
// - doors added (the drawing has none);
// - the theatre floor steps down toward the screen (stadium tiers), and
//   the pool and spa are shown with their shells (foundation.scad);
// - an exit stair out of the gym's north wall up to the back yard (the
//   sketch has no way out but the main stair).

use <house_lib.scad>
use <foundation.scad>

show_stair = true;     // false when the main floor draws it (combined model)
audit = false;         // echo the tables for the layout checker

// no section cut when this file is opened on its own ($cut is a special
// variable, so house_combined.scad's value reaches these modules)
let ($cut = undef) basement_level(show_stair, audit);

/* [Hidden] */
water  = [0.39, 0.70, 0.93, 0.75];
spa_w  = [0.51, 0.90, 0.85, 0.80];
deck   = [0.86, 0.84, 0.78];
seat   = [0.25, 0.25, 0.28];
carpet = [0.66, 0.36, 0.36];
stage  = [0.36, 0.20, 0.20];
screen = [0.96, 0.96, 0.96];
steel  = [0.70, 0.72, 0.74];
rail   = [0.22, 0.22, 0.24];
counter= [0.97, 0.97, 0.95];
white  = [0.97, 0.97, 0.97];
tile   = [0.55, 0.75, 0.85];
shelf  = [0.62, 0.50, 0.36];
wood   = [0.55, 0.38, 0.22];
dark   = [0.12, 0.12, 0.12];
sofa   = [0.45, 0.50, 0.60];
table  = [0.66, 0.50, 0.34];

// [label, x0, y0, x1, y1, ceiling, kind, z0, tag, label_at]
function base_rooms() = [
    ["MUSIC ROOM",      22.16, 50.35, 42.65, 63.16, basement_ceiling(), "living", 0, "", [32.4, 61.2, 1.6]],
    ["GYM",             42.65, 45.34, 54.14, 63.16, basement_ceiling(), "rec"],
    ["STORAGE",         22.16, 42.77, 37.37, 50.35, basement_ceiling(), "closet", 0, "", [29.8, 46.6, 1.4]],
    ["UTILITY",         22.16, 35.08, 37.37, 42.77, basement_ceiling(), "utility", 0, "", [29.8, 40.3, 1.4]],
    ["HALL",            37.37, 35.08, 42.65, 50.35, basement_ceiling(), "hall", 0, "", [40, 42.7, 1.0, 90]],
    ["STAIR UP",        42.65, stair_foot_y(), 47.27, 45.34, basement_ceiling(), "stair", 0, "", [44.95, 28.1, 0.55]],  // label at the foot
    ["BATH",            47.27, 35.08, 54.14, 45.34, basement_ceiling(), "bath", 0, "", [49.4, 39.6, 1.0]],
    ["HALLWAY",         35.27, 27.6,  54.14, stair_foot_y(), 0, "hall", 0, "", [39.3, 29.4, 1.0]],
    ["",                35.27, stair_foot_y(), 42.65, 35.08, 0, "hall"],
    ["",                47.27, stair_foot_y(), 54.14, 35.08, 0, "hall"],
    ["LIVING ROOM",     35.27, 5.79,  54.14, 27.6,  10, "living", 0, "", [44.7, 9.5, 1.8]],
    [["HOME", "THEATER"], 54.14, 29.12, 69.38, 50.35, basement_ceiling() + 1.25, "tiered", -1.25, "", [61.8, 45.4, 1.5]],
    ["PET ROOM",        54.14, 18.15, 69.38, 29.12, basement_ceiling(), "utility", 0, "", [61.8, 23.3, 1.5]],
    [["POOL", "ROOM"],  69.38, 18.15, 96.33, 52.76, basement_ceiling(), "pit", 0, "", [77.4, 24.5, 1.6]],
    [["POOL", "EQUIP."], 96.33, 29.12, 103.04, 41.94, basement_ceiling(), "utility", 0, "", [98.2, 37.7, 0.7]],
    [["POOL", "BATH"],  96.33, 18.15, 103.04, 29.12, basement_ceiling(), "bath", 0, "", [98.9, 24.6, 0.75]],
    ["HALL",            54.14, 13.43, 103.04, 18.15, basement_ceiling(), "hall", 0, "", [86, 15.8, 1.2]],
    ["BATH",            54.14, 5.79,  67.4,  13.43, basement_ceiling(), "bath", 0, "", [58.6, 10.4, 1.1]],
    ["LAUNDRY",         67.4,  5.79,  81.68, 13.43, basement_ceiling(), "utility", 0, "", [74.6, 10.2, 1.3]],
    // the exit stair's areaway, outside the gym (foundation.scad)
    [["EXIT", "STAIR"], exit_areaway()[0], 63.16, exit_areaway()[2], exit_areaway()[3], 0, "stairwell", 0, "", [47.95, 65.75, 0.6]],
];

// [x, y, axis, width, type, swing, tag]  (the drawing shows no doors)
function base_doors() = [
    [38.4,   50.35, "x", 2.8, "door",  1],          // music room
    [42.65,  46.2,  "y", 2.8, "door",  1],          // gym
    [37.37,  45.6,  "y", 2.8, "door", -1],          // storage
    [37.37,  38.4,  "y", 3.0, "door", -1],          // utility
    [37.6,   35.08, "x", 4.8, "full"],              // hall / hallway
    [42.9,   stair_foot_y(), "x", 4.1, "full"],     // foot of the stair
    [35.5,   stair_foot_y(), "x", 6.9, "full"],     // hallway pieces
    [47.5,   stair_foot_y(), "x", 6.4, "full"],
    [49.2,   35.08, "x", 2.8, "door",  1],          // bath
    [54.14,  31.7,  "y", 3.0, "door", -1],          // theatre, at the back (top) tier; swings out
    [40.0,   27.6,  "x", 8.0, "open"],              // living room
    [54.14,  13.8,  "y", 4.0, "open"],              // living room / east hall
    [56.5,   18.15, "x", 3.0, "door",  1],          // pet room
    [71.0,   18.15, "x", 3.0, "door",  1],          // pool room
    [96.33,  20.5,  "y", 2.8, "door",  1],          // pool room / pool bath
    [99.0,   18.15, "x", 2.8, "door",  1],          // hall / pool bath
    [96.33,  33.5,  "y", 3.0, "door",  1],          // pool equipment
    [59.0,   13.43, "x", 2.8, "door", -1],          // bath
    [73.0,   13.43, "x", 3.0, "door", -1],          // laundry
    [exit_door()[0], 63.16, "x", exit_door()[1], "door", -1],   // exit door: opens in, so snow can't block it
];

// [x0, y0, x1, y1, z0, z1, colour, tag, shape]
function base_fixtures() = [
    // pool deck finish round the pool and spa (shells: foundation.scad);
    // finishes are thin layers on the slab
    [69.58, 18.35, 74.32, 52.21, 0, 0.02, deck],
    [74.32, 48.45, 95.78, 52.21, 0, 0.02, deck],
    [90.79, 18.35, 96.13, 41.94, 0, 0.02, deck],
    [90.79, 41.94, 95.78, 48.45, 0, 0.02, deck],
    [74.32, 18.35, 81.32, 31.91, 0, 0.02, deck],
    [81.32, 18.35, 90.79, 23.02, 0, 0.02, deck],
    // theatre (foundation.scad has the tiers): carpeted rear tier, side
    // ledges and screen stage at floor level, the step and the front tier
    // lowered; the screen in front of the north (ICF) wall
    [54.34, 29.32, 69.18, 36.6,   0,      0.02,   carpet],
    [54.34, 36.6,  55.5,  47.3,   0,      0.02,   carpet],
    [68.0,  36.6,  69.18, 47.3,   0,      0.02,   carpet],
    [55.5,  36.6,  68.0,  37.5,  -0.625, -0.605,  carpet],
    [55.5,  37.5,  68.0,  47.3,  -1.25,  -1.23,   carpet],
    [54.34, 47.3,  69.18, 49.8,   0,      0.03,   stage],
    [57.39, 49.5,  66.11, 49.65,  1.5,    6.4,   screen],     // 120" 16:9: 8.7 x 4.9 ft
    // baths
    [52.0,  41.5,  53.8,  43.3,  0, 1.4,  white],      // bath by the stair
    [52.1,  38.5,  53.9,  41.0,  0, 3,    counter],
    [47.6,  42.0,  50.6,  45.0,  0, 0.15, tile],
    [100.6, 22.5,  102.4, 24.3,  0, 1.4,  white],      // pool bath
    [96.6,  25.5,  98.6,  28.8,  0, 3,    counter],
    [99.2,  25.4,  102.45, 28.9, 0, 0.15, tile],
    [54.4,  6.4,   59.4,  8.95,  0, 2,    white],      // south bath: tub
    [62.5,  6.4,   67.1,  8.25,  0, 3,    counter],
    [65.2,  9.5,   67.1,  11.3,  0, 1.4,  white],
    // laundry, pet room
    [67.8,  6.4,   72.6,  8.75,  0, 3.2,  steel],
    [77.0,  6.4,   81.1,  8.45,  0, 3,    counter],
    [65.5,  26.5,  69.0,  28.9,  0, 3,    white],      // dog wash
    // utility: air handler, boiler, water heater, well-water treatment, HRV
    [22.8,  35.7,  25.8,  38.7,  0, 6,    steel],
    [26.3,  35.7,  28.5,  37.7,  0, 3.5,  steel],
    [29.0,  35.7,  31.2,  37.9,  0, 5.5,  steel, "", "round"],
    [33.8,  35.7,  36.6,  37.7,  0, 5,    steel],
    [22.8,  40.4,  25.8,  42.3,  5.5, 7,  steel],
    // pool equipment: filter, pump, heater, dehumidifier, chemicals
    [99.9,  38.7,  102.2, 41.0,  0, 4.5,  steel, "", "round"],
    [96.8,  39.2,  99.3,  41.0,  0, 2,    steel],
    [99.7,  33.0,  102.3, 36.0,  0, 4.5,  steel],
    [99.4,  29.6,  102.3, 32.4,  0, 6.5,  steel],
    [97.0,  29.6,  98.6,  31.2,  0, 3,    white],
    // storage shelving
    [22.8,  43.0,  36.9,  44.5,  0, 7,    shelf],
    [22.8,  48.6,  36.9,  50.1,  0, 7,    shelf],
];

// furniture
function base_furniture() = [
    [24.0,  54.0,  29.0,  59.5,  0, 3.3,  dark],       // grand piano
    [50.1,  57.6,  53.5,  62.5,  0, 7.5,  steel],      // gym: power rack
    [43.0,  58.1,  45.8,  62.5,  0, 4.5,  dark],       //   treadmill
    [36.0,  20.5,  46.5,  23.5,  0, 2.6,  sofa],       // living room sectional
    [36.0,  12.5,  39.0,  20.5,  0, 2.6,  sofa],
    [40.0,  15.0,  44.0,  19.0,  0, 1.5,  table],
    [52.6,  12.0,  53.9,  22.0,  0, 2,    wood],       //   TV unit
    [70.4,  21.6,  72.9,  28.1,  0, 1.2,  white],      // pool loungers
    [70.4,  29.0,  72.9,  35.5,  0, 1.2,  white],
];

// theatre seating, as fixture rows: two rows of four recliners centred on
// the lowered tiers, the back row on the rear (entrance) tier
function theatre_seats() = [
    for (row = [[30.5, 0], [38.4, -1.25]], x = [56.55, 59.15, 61.75, 64.35])
        [x, row[0], x + 2.55, row[0] + 3.2, row[1], row[1] + 3.3, seat]
];

// water in the pool and the raised spa (shells and levels: foundation.scad,
// whose elevations are from the main floor, hence + floor_to_floor())
module pool_and_spa_water() {
    p = pool_xy(); s = spa_xy(); f = floor_to_floor();
    paint(water) translate([p[0], p[1], pool_water() + f - pool_depth()]) cube([p[2] - p[0], p[3] - p[1], pool_depth()]);
    paint(spa_w) translate([s[0], s[1], spa_water() + f - spa_depth()]) cube([s[2] - s[0], s[3] - s[1], spa_depth()]);
}

// the exit stair: the flight from the landing up to grade, east along the
// house, and a 42" guard on the areaway's curb (walls: foundation.scad)
module exit_stair() {
    a = exit_areaway(); t = exit_wall_t();
    zg = exit_rise();                      // grade, above the basement floor
    flight(exit_landing_x()[1], a[1], a[2], a[3], "-x", zg, 0, exit_risers(), 0);
    paint(rail) {
        y = a[3] + t / 2;
        for (x = [a[0] - t / 2 : (a[2] - a[0] + t / 2) / 4 : a[2] + 0.01])
            translate([x - 0.08, y - 0.08, zg + 0.5]) cube([0.16, 0.16, 3]);
        translate([a[0] - t / 2 - 0.08, y - 0.1, zg + 3.35]) cube([a[2] - a[0] + t / 2 + 0.16, 0.2, 0.15]);
        for (yy = [a[1], (a[1] + y) / 2])
            translate([a[0] - t / 2 - 0.08, yy - 0.08, zg + 0.5]) cube([0.16, 0.16, 3]);
        translate([a[0] - t / 2 - 0.1, a[1], zg + 3.35]) cube([0.2, y - a[1], 0.15]);
    }
}

module basement_level(show_stair = true, audit = false, show_furniture = true) {
    rooms = base_rooms();
    doors = base_doors();
    if (audit) echo(rooms = rooms, doors = doors, windows = [],
                    fixtures = concat(base_fixtures(), base_furniture(), theatre_seats()));

    draw_level(rooms, doors, []);
    fixtures(base_fixtures());
    if (show_furniture) fixtures(base_furniture());
    fixtures(theatre_seats());
    exit_stair();
    pool_and_spa_water();
    // the concrete (walls, footings, slab, tiers, pool + spa shells),
    // drawn at its real elevation and lifted to this level's frame
    translate([0, 0, floor_to_floor()]) foundation("basement");
    if (show_stair) main_stair(floor_to_floor());
}
