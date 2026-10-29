// Shop - OpenSCAD model of the 100' x 100' 4-bay shop.
// Units: feet. Visualisation only - NOT construction documents.
//
// Orientation v2 (Jordan, 2026-10-29): the shop is rotated 90 degrees
// from the first sketch. The bays now run north-south and the front
// (overhead doors) faces SOUTH. The bays stack west -> east:
//
//   Bay 4 wash | Bay 3 truck work + pit | Bay 2 truck work | Bay 1 utilities
//
// Bay 1 (utilities) is the EASTERNMOST bay, closest to the house. The
// utility tunnel leaves the SIDE (east wall) of Bay 1 at its portal
// room, on the centreline of the house basement's UTILITIES room
// (which sits on the north side of the basement) - see site.scad.
//
// Local coordinates: x = east, y = north, floor at z = 0. The front
// wall is y = 0. site.scad places the shop west of the house with its
// south-east corner toward the house's north-west.

use <house_lib.scad>

show_roof = true;
roof_opacity = 1.0;    // [0.1:0.1:1]
roof_color = [0.55, 0.58, 0.62];  // steel grey

shop_level(show_roof, roof_color, roof_opacity);

/* [Hidden] */
wall_h = 20;           // eave height (14 ft doors + truck stacks / lifts)
wall_t = 0.5;
steel  = [0.70, 0.72, 0.74];
dark   = [0.12, 0.12, 0.12];
waterc = [0.39, 0.70, 0.93];
pit_c  = [0.25, 0.25, 0.25];

// bays: [label, x0, x1, kind, label_at] - each bay is 25 ft wide,
// 100 ft deep (y 0..100). Bay 1 carries no bay label: its rooms label it.
function shop_bays() = [
    [["WASH", "BAY"],       0,  25, "pool",   [12.5, 92, 1.8]],
    [["TRUCK WORK", "+ PIT"], 25, 50, "living", [37.5, 88, 1.6]],
    [["TRUCK", "WORK"],     50, 75, "living", [62.5, 50, 1.9]],
    ["",                    75, 100, "utility", undef],
];

// Bay 1 subdivisions, south -> north: [label, y0, y1, kind, label_at]
// The tunnel portal room is centred on y = 50, the centreline the
// tunnel takes to the house basement's UTILITIES room (site.scad).
// Label positions are picked to sit clear of the fixtures.
function util_rooms() = [
    ["GENERATOR",    0,  18, "garage",  [87.5, 15, 1.25]],
    ["ELECTRICAL",   18, 42, "utility", [89, 39, 1.1]],
    ["TUNNEL PORTAL", 42, 58, "stair",  [81.5, 50, 1.05]],
    [["WATER +", "HEAT"], 58, 82, "utility", [86, 78, 1.15]],
    [["NETWORK +", "BATH"], 82, 100, "office", [85, 95, 1.1]],
];

// overhead doors on the south wall: [x, width, height]
function shop_doors() = [
    [5.5,  14, 14],    // wash bay
    [30.5, 14, 14],    // truck work + pit
    [55.5, 14, 14],    // truck work
    [80,   10, 12],    // utilities (equipment only, no trucks)
];

module txt(lines, at, size = 1.6, rot = 0) {
    color([0.15, 0.15, 0.15])
        translate([at[0], at[1], 0.06]) rotate([0, 0, rot])
            for (i = [0 : len(lines) - 1])
                translate([0, (len(lines) - 1) / 2 * 1.4 * size - i * 1.4 * size, 0])
                    linear_extrude(0.05)
                        text(lines[i], size = size, halign = "center", valign = "center");
}

module room_box(r) {   // r = [label, x0, y0, x1, y1, ceil, kind]
    floor_plate(r);
    room_label(r);
}

module perimeter_walls() {
    doors = shop_doors();
    color([0.93, 0.91, 0.87]) difference() {
        union() {
            translate([-wall_t / 2, -wall_t / 2, 0]) cube([100 + wall_t, wall_t, wall_h]);          // south (front)
            translate([-wall_t / 2, 100 - wall_t / 2, 0]) cube([100 + wall_t, wall_t, wall_h]);      // north
            translate([-wall_t / 2, -wall_t / 2, 0]) cube([wall_t, 100 + wall_t, wall_h]);           // west
            translate([100 - wall_t / 2, -wall_t / 2, 0]) cube([wall_t, 100 + wall_t, wall_h]);      // east
        }
        for (d = doors) translate([d[0], -1, -0.1]) cube([d[1], 2, d[2] + 0.1]);
        translate([93, -1, -0.1]) cube([3, 2, 7.1]);   // Bay 1 man door
    }
    for (d = doors)   // door panels, drawn closed
        color([0.88, 0.88, 0.86]) translate([d[0], -0.12, 0]) cube([d[1], 0.24, d[2]]);
}

module util_partitions() {
    // Bay 1 interior walls (10 ft) at the room boundaries, with a door gap
    color([0.93, 0.91, 0.87])
        for (y = [18, 42, 58, 82]) {
            translate([75, y - 0.2, 0]) cube([10, 0.4, 10]);
            translate([89, y - 0.2, 0]) cube([11, 0.4, 10]);
        }
}

module shop_fixtures() {
    // pit in Bay 3: 4 ft wide x 40 ft long, ~5.5 ft deep, centred in the bay
    color(pit_c) translate([35.5, 30, -5.5]) cube([4, 40, 5.5]);
    color([0.85, 0.30, 0.20]) {
        translate([35.3, 29.8, -0.05]) cube([4.4, 0.4, 0.1]);
        translate([35.3, 69.8, -0.05]) cube([4.4, 0.4, 0.1]);
        translate([35.3, 29.8, -0.05]) cube([0.4, 40.4, 0.1]);
        translate([39.3, 29.8, -0.05]) cube([0.4, 40.4, 0.1]);
    }
    txt(["PIT"], [37.5, 74], 1.6);
    // wash bay trench drain
    color(waterc) translate([11.5, 15, 0.02]) cube([2, 70, 0.06]);
    txt(["TRENCH DRAIN"], [12.5, 24], 1.2, 90);
    // benches along the north wall of Bays 2 + 3
    color(steel) {
        translate([27, 96, 0]) cube([21, 3, 3]);
        translate([52, 96, 0]) cube([21, 3, 3]);
    }
    // Bay 1: generator (1A), battery racks (1B), tanks + boiler (1C), racks (1D)
    color(dark)  translate([79, 3, 0]) cube([12, 8, 8]);                 // generator
    color(steel) for (y = [21, 28, 35]) translate([95.5, y, 0]) cube([3.5, 5, 7]);  // battery racks, east wall
    color(steel) translate([77, 20, 0]) cube([7, 12, 7.5]);              // inverters / switchgear
    color(waterc) for (y = [64, 73]) translate([95, y, 0]) cylinder(r = 2.2, h = 8, $fn = 24);  // pressure tanks
    color([0.85, 0.30, 0.20]) translate([79, 62, 0]) cube([8, 8, 7]);    // boiler
    color(dark)  for (y = [85, 91]) translate([95.5, y, 0]) cube([3.5, 4, 7]);     // server racks
}

module shop_level(show_roof = true, roof_color = [0.55, 0.58, 0.62], roof_opacity = 1) {
    for (b = shop_bays()) room_box([b[0], b[1], 0, b[2], 100, 0, b[3], 0, "", b[4]]);
    for (u = util_rooms()) room_box([u[0], 75, u[1], 100, u[2], 0, u[3], 0, "", u[4]]);
    // Bay 1 stair down to the tunnel: an open well along the east wall
    // in the portal room (the tunnel floor is at basement level, ~11 ft
    // below the shop slab - see site.scad)
    color(pit_c) translate([89, 43, -1]) cube([10.5, 14, 1.05]);
    perimeter_walls();
    util_partitions();
    shop_fixtures();
    if (show_roof) roofs([[0, 0, 100, 100, wall_h, 0.30, 2]], roof_color, roof_opacity);
}
