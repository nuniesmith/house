// Basement — generated from config/floorplan.yaml by generate_scad.py
// Units: feet. Dollhouse view (no roof). NOT construction documents.
wall_h = 12.0;
$fn = 24;

// ---- floor plates
color([0.6823529411764706, 0.9333333333333333, 0.9333333333333333]) translate([0, 0, -0.15]) cube([25, 35, 0.15]);
color([0.15,0.15,0.15]) translate([12.5, 17.5, 0.01]) linear_extrude(0.05) text("POOL / HOT TUB", size=2.30, halign="center", valign="center");
color([0.4392156862745098, 0.5019607843137255, 0.5647058823529412]) translate([0, 35, -0.15]) cube([30, 25, 0.15]);
color([0.15,0.15,0.15]) translate([15.0, 47.5, 0.01]) linear_extrude(0.05) text("HOME THEATER", size=2.30, halign="center", valign="center");
color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([30, 45, -0.15]) cube([40, 15, 0.15]);
color([0.15,0.15,0.15]) translate([50.0, 52.5, 0.01]) linear_extrude(0.05) text("UTILITIES", size=2.30, halign="center", valign="center");
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([25, 20, -0.15]) cube([55, 25, 0.15]);
color([0.15,0.15,0.15]) translate([52.5, 32.5, 0.01]) linear_extrude(0.05) text("OPEN REC AREA", size=2.30, halign="center", valign="center");
color([0.9607843137254902, 0.9607843137254902, 0.8627450980392157]) translate([30, 0, -0.15]) cube([60, 20, 0.15]);
color([0.15,0.15,0.15]) translate([60.0, 10.0, 0.01]) linear_extrude(0.05) text("STORAGE / REC", size=2.30, halign="center", valign="center");
color([1.0, 0.984313725490196, 0.9215686274509803]) translate([90, 0, -0.15]) cube([10, 60, 0.15]);
color([0.5450980392156862, 0.27058823529411763, 0.07450980392156863]) translate([65, 25, -0.15]) cube([10, 6, 0.15]);
color([0.15,0.15,0.15]) translate([70.0, 28.0, 0.01]) linear_extrude(0.05) text("BAR", size=2.30, halign="center", valign="center");

// ---- walls (openings cut)
color([0.93, 0.91, 0.87]) difference() {
  union() {
    translate([-0.25, -0.25, 0]) cube([25.50, 0.50, 12.0]);
    translate([-0.17, 34.83, 0]) cube([25.34, 0.34, 12.0]);
    translate([-0.25, -0.25, 0]) cube([0.50, 35.50, 12.0]);
    translate([24.83, -0.17, 0]) cube([0.34, 35.34, 12.0]);
    translate([-0.17, 34.83, 0]) cube([30.34, 0.34, 12.0]);
    translate([-0.25, 59.75, 0]) cube([30.50, 0.50, 12.0]);
    translate([-0.25, 34.75, 0]) cube([0.50, 25.50, 12.0]);
    translate([29.83, 34.83, 0]) cube([0.34, 25.34, 12.0]);
    translate([29.83, 44.83, 0]) cube([40.34, 0.34, 12.0]);
    translate([29.75, 59.75, 0]) cube([40.50, 0.50, 12.0]);
    translate([29.83, 44.83, 0]) cube([0.34, 15.34, 12.0]);
    translate([69.75, 44.75, 0]) cube([0.50, 15.50, 12.0]);
    translate([24.83, 19.83, 0]) cube([55.34, 0.34, 12.0]);
    translate([24.83, 44.83, 0]) cube([55.34, 0.34, 12.0]);
    translate([24.83, 19.83, 0]) cube([0.34, 25.34, 12.0]);
    translate([79.75, 19.75, 0]) cube([0.50, 25.50, 12.0]);
    translate([29.75, -0.25, 0]) cube([60.50, 0.50, 12.0]);
    translate([29.83, 19.83, 0]) cube([60.34, 0.34, 12.0]);
    translate([29.75, -0.25, 0]) cube([0.50, 20.50, 12.0]);
    translate([89.83, -0.17, 0]) cube([0.34, 20.34, 12.0]);
    translate([89.75, -0.25, 0]) cube([10.50, 0.50, 12.0]);
    translate([89.75, 59.75, 0]) cube([10.50, 0.50, 12.0]);
    translate([89.83, -0.17, 0]) cube([0.34, 60.34, 12.0]);
    translate([99.75, -0.25, 0]) cube([0.50, 60.50, 12.0]);
    translate([64.75, 24.75, 0]) cube([10.50, 0.50, 12.0]);
    translate([64.75, 30.75, 0]) cube([10.50, 0.50, 12.0]);
    translate([64.75, 24.75, 0]) cube([0.50, 6.50, 12.0]);
    translate([74.75, 24.75, 0]) cube([0.50, 6.50, 12.0]);
  }
}

// stairs: UP
color([0.75, 0.72, 0.68]) {
  translate([70.00, 45, 0]) cube([1.67, 15, 1.00]);
  translate([71.67, 45, 0]) cube([1.67, 15, 2.00]);
  translate([73.33, 45, 0]) cube([1.67, 15, 3.00]);
  translate([75.00, 45, 0]) cube([1.67, 15, 4.00]);
  translate([76.67, 45, 0]) cube([1.67, 15, 5.00]);
  translate([78.33, 45, 0]) cube([1.67, 15, 6.00]);
  translate([80.00, 45, 0]) cube([1.67, 15, 7.00]);
  translate([81.67, 45, 0]) cube([1.67, 15, 8.00]);
  translate([83.33, 45, 0]) cube([1.67, 15, 9.00]);
  translate([85.00, 45, 0]) cube([1.67, 15, 10.00]);
  translate([86.67, 45, 0]) cube([1.67, 15, 11.00]);
  translate([88.33, 45, 0]) cube([1.67, 15, 12.00]);
}

// stairs: EXIT STAIRS
color([0.75, 0.72, 0.68]) {
  translate([90, 0.00, 0]) cube([10, 1.50, 0.30]);
  translate([90, 1.50, 0]) cube([10, 1.50, 0.60]);
  translate([90, 3.00, 0]) cube([10, 1.50, 0.90]);
  translate([90, 4.50, 0]) cube([10, 1.50, 1.20]);
  translate([90, 6.00, 0]) cube([10, 1.50, 1.50]);
  translate([90, 7.50, 0]) cube([10, 1.50, 1.80]);
  translate([90, 9.00, 0]) cube([10, 1.50, 2.10]);
  translate([90, 10.50, 0]) cube([10, 1.50, 2.40]);
  translate([90, 12.00, 0]) cube([10, 1.50, 2.70]);
  translate([90, 13.50, 0]) cube([10, 1.50, 3.00]);
  translate([90, 15.00, 0]) cube([10, 1.50, 3.30]);
  translate([90, 16.50, 0]) cube([10, 1.50, 3.60]);
  translate([90, 18.00, 0]) cube([10, 1.50, 3.90]);
  translate([90, 19.50, 0]) cube([10, 1.50, 4.20]);
  translate([90, 21.00, 0]) cube([10, 1.50, 4.50]);
  translate([90, 22.50, 0]) cube([10, 1.50, 4.80]);
  translate([90, 24.00, 0]) cube([10, 1.50, 5.10]);
  translate([90, 25.50, 0]) cube([10, 1.50, 5.40]);
  translate([90, 27.00, 0]) cube([10, 1.50, 5.70]);
  translate([90, 28.50, 0]) cube([10, 1.50, 6.00]);
  translate([90, 30.00, 0]) cube([10, 1.50, 6.30]);
  translate([90, 31.50, 0]) cube([10, 1.50, 6.60]);
  translate([90, 33.00, 0]) cube([10, 1.50, 6.90]);
  translate([90, 34.50, 0]) cube([10, 1.50, 7.20]);
  translate([90, 36.00, 0]) cube([10, 1.50, 7.50]);
  translate([90, 37.50, 0]) cube([10, 1.50, 7.80]);
  translate([90, 39.00, 0]) cube([10, 1.50, 8.10]);
  translate([90, 40.50, 0]) cube([10, 1.50, 8.40]);
  translate([90, 42.00, 0]) cube([10, 1.50, 8.70]);
  translate([90, 43.50, 0]) cube([10, 1.50, 9.00]);
  translate([90, 45.00, 0]) cube([10, 1.50, 9.30]);
  translate([90, 46.50, 0]) cube([10, 1.50, 9.60]);
  translate([90, 48.00, 0]) cube([10, 1.50, 9.90]);
  translate([90, 49.50, 0]) cube([10, 1.50, 10.20]);
  translate([90, 51.00, 0]) cube([10, 1.50, 10.50]);
  translate([90, 52.50, 0]) cube([10, 1.50, 10.80]);
  translate([90, 54.00, 0]) cube([10, 1.50, 11.10]);
  translate([90, 55.50, 0]) cube([10, 1.50, 11.40]);
  translate([90, 57.00, 0]) cube([10, 1.50, 11.70]);
  translate([90, 58.50, 0]) cube([10, 1.50, 12.00]);
}

// ---- ICF foundation shell (1 ft)
difference() {
  translate([0, 0, -1.15]) cube([100, 60, 1.0]);
}
color([0.45,0.45,0.45]) {
  translate([-0.5, -0.5, 0]) cube([101, 1.0, 12.0]);
  translate([-0.5, 59.5, 0]) cube([101, 1.0, 12.0]);
  translate([-0.5, 0, 0]) cube([1.0, 60, 12.0]);
  translate([99.5, 0, 0]) cube([1.0, 60, 12.0]);
}
// ---- pool + hot tub
color([0.38823529411764707, 0.7019607843137254, 0.9294117647058824]) translate([5, 3, 0.02]) cube([12, 22, 0.35]);
color([0.5058823529411764, 0.9019607843137255, 0.8509803921568627]) translate([8, 27, 0.4]) cylinder(r=4, h=1.6);

// ---- theater seating
color([0.2901960784313726, 0.2901960784313726, 0.2901960784313726]) {
  translate([3, 38, 1.20]) cube([3, 2.5, 2.6]);
  translate([8, 38, 1.20]) cube([3, 2.5, 2.6]);
  translate([13, 38, 1.20]) cube([3, 2.5, 2.6]);
  translate([18, 38, 1.20]) cube([3, 2.5, 2.6]);
  translate([3, 43, 0.80]) cube([3, 2.5, 2.6]);
  translate([8, 43, 0.80]) cube([3, 2.5, 2.6]);
  translate([13, 43, 0.80]) cube([3, 2.5, 2.6]);
  translate([18, 43, 0.80]) cube([3, 2.5, 2.6]);
  translate([3, 48, 0.40]) cube([3, 2.5, 2.6]);
  translate([8, 48, 0.40]) cube([3, 2.5, 2.6]);
  translate([13, 48, 0.40]) cube([3, 2.5, 2.6]);
  translate([18, 48, 0.40]) cube([3, 2.5, 2.6]);
}
color([0.6, 0.1, 0.1]) translate([0, 34.75, 0]) cube([30, 0.5, 11.0]);  // false wall
