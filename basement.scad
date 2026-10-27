// Basement - OpenSCAD model of the lower level.
// Units: feet. Dollhouse view (no roof). NOT construction documents.
wall_h = 12.0;
$fn = 24;

// ---- floor plates
color([0.6823529411764706, 0.9333333333333333, 0.9333333333333333]) translate([0, 0, -0.15]) cube([25, 35, 0.15]);
color([0.15,0.15,0.15]) translate([12.5, 17.5, 0.01]) linear_extrude(0.05) text("POOL / HOT TUB", size=2.30, halign="center", valign="center");
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([25, 0, -0.15]) cube([21, 20, 0.15]);
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([25, 20, -0.15]) cube([5, 15, 0.15]);
color([0.4392156862745098, 0.5019607843137255, 0.5647058823529412]) translate([0, 35, -0.15]) cube([30, 25, 0.15]);
color([0.15,0.15,0.15]) translate([15.0, 47.5, 0.01]) linear_extrude(0.05) text("HOME THEATER", size=2.30, halign="center", valign="center");
color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([30, 45, -0.15]) cube([40, 15, 0.15]);
color([0.15,0.15,0.15]) translate([50.0, 52.5, 0.01]) linear_extrude(0.05) text("UTILITIES", size=2.30, halign="center", valign="center");
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([30, 20, -0.15]) cube([70, 25, 0.15]);
color([0.15,0.15,0.15]) translate([65.0, 32.5, 0.01]) linear_extrude(0.05) text("OPEN REC AREA", size=2.30, halign="center", valign="center");
color([0.9607843137254902, 0.9607843137254902, 0.8627450980392157]) translate([46, 0, -0.15]) cube([54, 20, 0.15]);
color([0.15,0.15,0.15]) translate([73.0, 10.0, 0.01]) linear_extrude(0.05) text("STORAGE / REC", size=2.30, halign="center", valign="center");
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([70, 45, -0.15]) cube([30, 15, 0.15]);
color([1.0, 0.984313725490196, 0.9215686274509803]) translate([100, 20, -0.15]) cube([10, 40, 0.15]);
color([0.15,0.15,0.15]) translate([105.0, 40.0, 0.01]) linear_extrude(0.05) text("EXIT STAIRS", size=1.18, halign="center", valign="center");

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
    translate([69.83, 44.83, 0]) cube([0.34, 15.34, 12.0]);
    translate([99.75, 19.75, 0]) cube([10.50, 0.50, 12.0]);
    translate([99.75, 59.75, 0]) cube([10.50, 0.50, 12.0]);
    translate([99.83, 19.83, 0]) cube([0.34, 40.34, 12.0]);
    translate([109.75, 19.75, 0]) cube([0.50, 40.50, 12.0]);
  }
  translate([26, 34.2, -0.1]) cube([3, 1.6, 7.1]);
  translate([24.2, 29, -0.1]) cube([1.6, 3, 7.1]);
  translate([63, 44.2, -0.1]) cube([3, 1.6, 7.1]);
  translate([99.2, 52, -0.1]) cube([1.6, 3, 7.1]);
}

// ---- door leaves (ajar 30 deg)
color([0.55, 0.35, 0.2]) {
  translate([26, 35, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([25, 29, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([63, 45, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([100, 52, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
}

// ---- furniture
color([0.5450980392156862, 0.27058823529411763, 0.07450980392156863]) translate([62, 28, 0]) cube([4, 10, 3.5]);

// stairs: UP
color([0.75, 0.72, 0.68]) {
  translate([52.00, 35, 0]) cube([1.67, 10, 1.00]);
  translate([53.67, 35, 0]) cube([1.67, 10, 2.00]);
  translate([55.33, 35, 0]) cube([1.67, 10, 3.00]);
  translate([57.00, 35, 0]) cube([1.67, 10, 4.00]);
  translate([58.67, 35, 0]) cube([1.67, 10, 5.00]);
  translate([60.33, 35, 0]) cube([1.67, 10, 6.00]);
  translate([62.00, 35, 0]) cube([1.67, 10, 7.00]);
  translate([63.67, 35, 0]) cube([1.67, 10, 8.00]);
  translate([65.33, 35, 0]) cube([1.67, 10, 9.00]);
  translate([67.00, 35, 0]) cube([1.67, 10, 10.00]);
  translate([68.67, 35, 0]) cube([1.67, 10, 11.00]);
  translate([70.33, 35, 0]) cube([1.67, 10, 12.00]);
}

// stairs: EXIT STAIRS
color([0.75, 0.72, 0.68]) {
  translate([100, 20.00, 0]) cube([10, 1.48, 0.44]);
  translate([100, 21.48, 0]) cube([10, 1.48, 0.89]);
  translate([100, 22.96, 0]) cube([10, 1.48, 1.33]);
  translate([100, 24.44, 0]) cube([10, 1.48, 1.78]);
  translate([100, 25.93, 0]) cube([10, 1.48, 2.22]);
  translate([100, 27.41, 0]) cube([10, 1.48, 2.67]);
  translate([100, 28.89, 0]) cube([10, 1.48, 3.11]);
  translate([100, 30.37, 0]) cube([10, 1.48, 3.56]);
  translate([100, 31.85, 0]) cube([10, 1.48, 4.00]);
  translate([100, 33.33, 0]) cube([10, 1.48, 4.44]);
  translate([100, 34.81, 0]) cube([10, 1.48, 4.89]);
  translate([100, 36.30, 0]) cube([10, 1.48, 5.33]);
  translate([100, 37.78, 0]) cube([10, 1.48, 5.78]);
  translate([100, 39.26, 0]) cube([10, 1.48, 6.22]);
  translate([100, 40.74, 0]) cube([10, 1.48, 6.67]);
  translate([100, 42.22, 0]) cube([10, 1.48, 7.11]);
  translate([100, 43.70, 0]) cube([10, 1.48, 7.56]);
  translate([100, 45.19, 0]) cube([10, 1.48, 8.00]);
  translate([100, 46.67, 0]) cube([10, 1.48, 8.44]);
  translate([100, 48.15, 0]) cube([10, 1.48, 8.89]);
  translate([100, 49.63, 0]) cube([10, 1.48, 9.33]);
  translate([100, 51.11, 0]) cube([10, 1.48, 9.78]);
  translate([100, 52.59, 0]) cube([10, 1.48, 10.22]);
  translate([100, 54.07, 0]) cube([10, 1.48, 10.67]);
  translate([100, 55.56, 0]) cube([10, 1.48, 11.11]);
  translate([100, 57.04, 0]) cube([10, 1.48, 11.56]);
  translate([100, 58.52, 0]) cube([10, 1.48, 12.00]);
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
color([0.6, 0.1, 0.1]) translate([0, 34.75, 0]) cube([30, 0.5, 11]);  // false wall, 1 ft below the 12 ft ceiling
