// Shop - OpenSCAD model of the 100' x 100' 4-bay shop.
// Units: feet. Visualisation only - NOT construction documents.
//
// Orientation v3 (Jordan, 2026-10-29): the shop moves BEHIND the
// house, to the north side, rotated 90 degrees right from v2. The
// bays run east-west again and the front (overhead doors) faces
// WEST, onto the shared west driveway / apron. The bays stack
// south -> north:
//
//   Bay 1 utilities | Bay 2 truck work | Bay 3 truck work + pit | Bay 4 wash
//
// Bay 1 (utilities) is the SOUTHERNMOST bay, closest to the house.
// The utility tunnel leaves the SOUTH SIDE of Bay 1 at its portal
// room (near the bay's east end) and runs due SOUTH into the house
// basement's UTILITIES room through its north foundation wall -
// UTILITIES sits on the north side of the basement, so v3 gives the
// tunnel a straight, direct landing (see site.scad).
//
// Local coordinates: x = east, y = north, floor at z = 0. The front
// wall is x = 0. site.scad places the shop north of the house.

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

// bays: [label, y0, y1, kind, label_at] - each bay is 25 ft wide,
// 100 ft deep (x 0..100). Bay 1 carries no bay label: its rooms label it.
function shop_bays() = [
    ["",                    0,  25, "utility", undef],
    [["TRUCK", "WORK"],     25, 50, "living", [50, 37.5, 1.9]],
    [["TRUCK WORK", "+ PIT"], 50, 75, "living", [50, 71, 1.6]],
    [["WASH", "BAY"],       75, 100, "pool",  [45, 93, 1.8]],
];

// Bay 1 subdivisions, west -> east: [label, x0, x1, kind, label_at]
// The tunnel portal room is centred on local x = 80, which site.scad
// aligns with the centre of the basement UTILITIES room.
function util_rooms() = [
    ["GENERATOR",    0,  18, "garage",  [9, 21.5, 1.15]],
    ["ELECTRICAL",   18, 42, "utility", [36, 20.5, 1.05]],
    [["NETWORK +", "BATH"], 42, 58, "office", [50, 8, 1.0]],
    [["WATER +", "HEAT"], 58, 72, "utility", [65, 14.5, 0.95]],
    ["TUNNEL PORTAL", 72, 88, "stair",  [80, 19, 1.05]],
    ["FUTURE",       88, 100, "closet", [94, 12.5, 0.95]],
];

// overhead doors on the west wall: [y, width, height]
function shop_doors() = [
    [80.5, 14, 14],    // wash bay
    [55.5, 14, 14],    // truck work + pit
    [30.5, 14, 14],    // truck work
    [5,    10, 12],    // utilities (equipment only, no trucks)
];

module txt(lines, at, size = 1.6, rot = 0) {
    color([0.15, 0.15, 0.15])
        translate([at[0], at[1], 0.06]) rotate([0, 0, rot])
            for (i = [0 : len(lines) - 1])
                translate([0, (len(lines) - 1) / 2 * 1.4 * size - i * 1.4 * size, 0])
                    linear_extrude(0.05)
                        text(lines[i], size = size, halign = "center", valign = "center");
}

module room_box(r) {   // r = [label, x0, y0, x1, y1, ceil, kind, z0, tag, label_at]
    floor_plate(r);
    room_label(r);
}

module perimeter_walls() {
    doors = shop_doors();
    color([0.93, 0.91, 0.87]) difference() {
        union() {
            translate([-wall_t / 2, -wall_t / 2, 0]) cube([wall_t, 100 + wall_t, wall_h]);          // west (front)
            translate([100 - wall_t / 2, -wall_t / 2, 0]) cube([wall_t, 100 + wall_t, wall_h]);      // east
            translate([-wall_t / 2, -wall_t / 2, 0]) cube([100 + wall_t, wall_t, wall_h]);           // south
            translate([-wall_t / 2, 100 - wall_t / 2, 0]) cube([100 + wall_t, wall_t, wall_h]);      // north
        }
        for (d = doors) translate([-1, d[0], -0.1]) cube([2, d[1], d[2] + 0.1]);
        translate([-1, 17, -0.1]) cube([2, 3, 7.1]);   // Bay 1 man door
    }
    for (d = doors)   // door panels, drawn closed
        color([0.88, 0.88, 0.86]) translate([-0.12, d[0], 0]) cube([0.24, d[1], d[2]]);
}

module util_partitions() {
    // Bay 1 interior walls (10 ft) at the room boundaries, with a door gap
    color([0.93, 0.91, 0.87])
        for (x = [18, 42, 58, 72, 88]) {
            translate([x - 0.2, 0, 0]) cube([0.4, 10, 10]);
            translate([x - 0.2, 14, 0]) cube([0.4, 11, 10]);
        }
}

module shop_fixtures() {
    // pit in Bay 3: 4 ft wide x 40 ft long, ~5.5 ft deep, centred in the bay
    color(pit_c) translate([30, 60.5, -5.5]) cube([40, 4, 5.5]);
    color([0.85, 0.30, 0.20]) {
        translate([29.8, 60.3, -0.05]) cube([40.4, 0.4, 0.1]);
        translate([29.8, 64.3, -0.05]) cube([40.4, 0.4, 0.1]);
        translate([29.8, 60.3, -0.05]) cube([0.4, 4.4, 0.1]);
        translate([69.8, 60.3, -0.05]) cube([0.4, 4.4, 0.1]);
    }
    txt(["PIT"], [50, 57], 1.5);
    // wash bay trench drain
    color(waterc) translate([15, 86.5, 0.02]) cube([70, 2, 0.06]);
    txt(["TRENCH DRAIN"], [50, 82], 1.2);
    // wash-bay separator / pressure-washer zone at the east end
    color(steel) translate([88, 77, 0]) cube([10, 21, 3]);
    // benches along the east wall of Bays 2 + 3
    color(steel) {
        translate([96, 28, 0]) cube([3, 19, 3]);
        translate([96, 53, 0]) cube([3, 19, 3]);
    }
    // Bay 1: generator (1A), batteries + switchgear (1B), racks (1D),
    // tanks + boiler (1C)
    color(dark)  translate([2, 7, 0]) cube([12, 10, 8]);                  // generator
    color(steel) for (x = [21, 28, 35]) translate([x, 1.5, 0]) cube([5, 3.5, 7]);  // battery racks, south wall
    color(steel) translate([20, 10, 0]) cube([7, 12, 7.5]);               // inverters / switchgear
    color(dark)  for (x = [45, 51]) translate([x, 20, 0]) cube([4, 3.5, 7]);       // server racks
    color(waterc) for (x = [61, 67]) translate([x, 19, 0]) cylinder(r = 2, h = 8, $fn = 24);  // pressure tanks
    color([0.85, 0.30, 0.20]) translate([59, 3, 0]) cube([7, 7, 7]);      // boiler
}

module shop_level(show_roof = true, roof_color = [0.55, 0.58, 0.62], roof_opacity = 1) {
    for (b = shop_bays()) room_box([b[0], 0, b[1], 100, b[2], 0, b[3], 0, "", b[4]]);
    for (u = util_rooms()) room_box([u[0], u[1], 0, u[2], 25, 0, u[3], 0, "", u[4]]);
    // Bay 1 stair down to the tunnel: an open well along the south wall
    // of the portal room (the tunnel floor is at basement level, ~11 ft
    // below the shop slab - see site.scad)
    color(pit_c) translate([74, 2, -1]) cube([12, 8, 1.05]);
    perimeter_walls();
    util_partitions();
    shop_fixtures();
    if (show_roof) roofs([[0, 0, 100, 100, wall_h, 0.30, 2]], roof_color, roof_opacity);
}
