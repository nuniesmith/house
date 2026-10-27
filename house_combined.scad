// house_combined.scad - both levels of the house in one OpenSCAD model.
// Units: feet. Dollhouse view (no roof). NOT construction documents.
// mode: assembled | exploded | basement_only | main_only
// Alignment assumption: the basement foundation's south edge sits on
// the main floor's south wall line (y=0) and its east edge on the
// master suite's east wall, which puts the exit-stair tower under
// the side porch.
mode = "assembled";
basement_dx = 18.59;
basement_dy = 0;
explode_gap = 14;

module basement_level() {
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
}

module main_level() {
  // Main floor - OpenSCAD model of the main level.
  // Units: feet. Dollhouse view (no roof). NOT construction documents.
  wall_h = 12.0;
  $fn = 24;

  // ---- floor plates
  color([0.9607843137254902, 0.9607843137254902, 0.9607843137254902]) translate([0, 0, -0.15]) cube([25.17, 31.75, 0.15]);
  color([0.15,0.15,0.15]) translate([12.585, 15.875, 0.01]) linear_extrude(0.05) text("GARAGE", size=2.30, halign="center", valign="center");
  color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([25.17, 0, -0.15]) cube([18.08, 13.92, 0.15]);
  color([0.15,0.15,0.15]) translate([34.21, 6.96, 0.01]) linear_extrude(0.05) text("BEDROOM 4", size=2.30, halign="center", valign="center");
  color([0.8784313725490196, 1.0, 1.0]) translate([25.17, 13.92, -0.15]) cube([7.5, 6, 0.15]);
  color([0.15,0.15,0.15]) translate([28.92, 16.92, 0.01]) linear_extrude(0.05) text("BATH 4", size=1.62, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([32.67, 13.92, -0.15]) cube([10.58, 6, 0.15]);
  color([0.15,0.15,0.15]) translate([37.96, 16.92, 0.01]) linear_extrude(0.05) text("WIC", size=2.30, halign="center", valign="center");
  color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([25.17, 19.92, -0.15]) cube([11.08, 7.42, 0.15]);
  color([0.15,0.15,0.15]) translate([30.71, 23.630000000000003, 0.01]) linear_extrude(0.05) text("MUD ROOM", size=1.80, halign="center", valign="center");
  color([1.0, 0.984313725490196, 0.9215686274509803]) translate([36.25, 19.92, -0.15]) cube([7, 7.42, 0.15]);
  color([0.15,0.15,0.15]) translate([39.75, 23.630000000000003, 0.01]) linear_extrude(0.05) text("HALL", size=2.27, halign="center", valign="center");
  color([1.0, 0.984313725490196, 0.9215686274509803]) translate([25.17, 27.34, -0.15]) cube([27.25, 3.5, 0.15]);
  color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([25.17, 30.84, -0.15]) cube([17.25, 13.33, 0.15]);
  color([0.15,0.15,0.15]) translate([33.795, 37.505, 0.01]) linear_extrude(0.05) text("BEDROOM 3", size=2.30, halign="center", valign="center");
  color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([42.42, 30.84, -0.15]) cube([10, 13.33, 0.15]);
  color([0.15,0.15,0.15]) translate([47.42, 37.505, 0.01]) linear_extrude(0.05) text("LAUNDRY", size=1.86, halign="center", valign="center");
  color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([52.42, 30.84, -0.15]) cube([6, 6.5, 0.15]);
  color([0.15,0.15,0.15]) translate([55.42, 34.09, 0.01]) linear_extrude(0.05) text("PWDR", size=1.95, halign="center", valign="center");
  color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([52.42, 37.34, -0.15]) cube([6, 6.83, 0.15]);
  color([0.15,0.15,0.15]) translate([55.42, 40.755, 0.01]) linear_extrude(0.05) text("PANTRY", size=1.30, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([25.17, 44.17, -0.15]) cube([7, 7, 0.15]);
  color([0.15,0.15,0.15]) translate([28.67, 47.67, 0.01]) linear_extrude(0.05) text("WIC", size=2.30, halign="center", valign="center");
  color([0.8784313725490196, 1.0, 1.0]) translate([25.17, 51.17, -0.15]) cube([7, 7, 0.15]);
  color([0.15,0.15,0.15]) translate([28.67, 54.67, 0.01]) linear_extrude(0.05) text("BATH 3", size=1.52, halign="center", valign="center");
  color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([32.17, 44.17, -0.15]) cube([14.17, 14.42, 0.15]);
  color([0.15,0.15,0.15]) translate([39.255, 51.38, 0.01]) linear_extrude(0.05) text("BEDROOM 2", size=2.05, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([46.34, 44.17, -0.15]) cube([4, 4, 0.15]);
  color([0.15,0.15,0.15]) translate([48.34, 46.17, 0.01]) linear_extrude(0.05) text("WIC", size=1.73, halign="center", valign="center");
  color([0.8784313725490196, 1.0, 1.0]) translate([46.34, 48.17, -0.15]) cube([4, 10.42, 0.15]);
  color([0.15,0.15,0.15]) translate([48.34, 53.38, 0.01]) linear_extrude(0.05) text("BATH 2", size=0.87, halign="center", valign="center");
  color([1.0, 0.9333333333333333, 0.7333333333333333]) translate([50.34, 44.17, -0.15]) cube([14.08, 14.75, 0.15]);
  color([0.15,0.15,0.15]) translate([57.38, 51.545, 0.01]) linear_extrude(0.05) text("BREAKFAST NOOK", size=1.31, halign="center", valign="center");
  color([1.0, 0.9725490196078431, 0.8627450980392157]) translate([43.25, 0, -0.15]) cube([18.33, 14.5, 0.15]);
  color([0.15,0.15,0.15]) translate([52.415, 7.25, 0.01]) linear_extrude(0.05) text("DINING ROOM", size=2.17, halign="center", valign="center");
  color([1.0, 0.984313725490196, 0.9215686274509803]) translate([61.58, 0, -0.15]) cube([11.33, 13.33, 0.15]);
  color([0.15,0.15,0.15]) translate([67.245, 6.665, 0.01]) linear_extrude(0.05) text("FOYER", size=2.30, halign="center", valign="center");
  color([1.0, 0.9725490196078431, 0.8627450980392157]) translate([72.92, 0, -0.15]) cube([14.17, 12.17, 0.15]);
  color([0.15,0.15,0.15]) translate([80.005, 6.085, 0.01]) linear_extrude(0.05) text("LOUNGE", size=2.30, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([43.25, 14.5, -0.15]) cube([3.33, 9, 0.15]);
  color([0.15,0.15,0.15]) translate([44.915, 19.0, 0.01]) linear_extrude(0.05) text("CLOSET", size=0.72, halign="center", valign="center");
  color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([46.58, 14.5, -0.15]) cube([15, 9, 0.15]);
  color([0.15,0.15,0.15]) translate([54.08, 19.0, 0.01]) linear_extrude(0.05) text("BUTLER'S PANTRY", size=1.30, halign="center", valign="center");
  color([1.0, 0.984313725490196, 0.9215686274509803]) translate([61.58, 13.33, -0.15]) cube([10.17, 12.42, 0.15]);
  color([0.15,0.15,0.15]) translate([66.66499999999999, 19.54, 0.01]) linear_extrude(0.05) text("FRONT HALL", size=1.32, halign="center", valign="center");
  color([0.5450980392156862, 0.27058823529411763, 0.07450980392156863]) translate([71.75, 14.5, -0.15]) cube([14.5, 9, 0.15]);
  color([0.15,0.15,0.15]) translate([79.0, 19.0, 0.01]) linear_extrude(0.05) text("BAR", size=2.30, halign="center", valign="center");
  color([1.0, 0.9333333333333333, 0.7333333333333333]) translate([58.42, 25.75, -0.15]) cube([14, 15, 0.15]);
  color([0.15,0.15,0.15]) translate([65.42, 33.25, 0.01]) linear_extrude(0.05) text("KITCHEN", size=2.30, halign="center", valign="center");
  color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([72.42, 25.75, -0.15]) cube([16.5, 15.17, 0.15]);
  color([0.15,0.15,0.15]) translate([80.67, 33.335, 0.01]) linear_extrude(0.05) text("FAMILY ROOM", size=1.95, halign="center", valign="center");
  color([1.0, 0.984313725490196, 0.9215686274509803]) translate([88.92, 16.5, -0.15]) cube([12, 12.42, 0.15]);
  color([0.15,0.15,0.15]) translate([94.92, 22.71, 0.01]) linear_extrude(0.05) text("HALL", size=2.30, halign="center", valign="center");
  color([0.9607843137254902, 0.9607843137254902, 0.9607843137254902]) translate([88.92, 28.92, -0.15]) cube([12, 12, 0.15]);
  color([0.15,0.15,0.15]) translate([94.92, 34.92, 0.01]) linear_extrude(0.05) text("OFFICE", size=2.30, halign="center", valign="center");
  color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([100.92, 18.25, -0.15]) cube([17.67, 22.67, 0.15]);
  color([0.15,0.15,0.15]) translate([109.755, 29.585, 0.01]) linear_extrude(0.05) text("MASTER SUITE", size=1.91, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([87.09, 0, -0.15]) cube([8.83, 16.5, 0.15]);
  color([0.15,0.15,0.15]) translate([91.50500000000001, 8.25, 0.01]) linear_extrude(0.05) text("WIC", size=2.30, halign="center", valign="center");
  color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([95.92, 0, -0.15]) cube([8.83, 16.5, 0.15]);
  color([0.15,0.15,0.15]) translate([100.33500000000001, 8.25, 0.01]) linear_extrude(0.05) text("WIC", size=2.30, halign="center", valign="center");
  color([0.8784313725490196, 1.0, 1.0]) translate([104.75, 0, -0.15]) cube([13.84, 16.5, 0.15]);
  color([0.15,0.15,0.15]) translate([111.67, 8.25, 0.01]) linear_extrude(0.05) text("MASTER BATH", size=1.64, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([40, -12.33, -0.15]) cube([56.67, 12.33, 0.15]);
  color([0.15,0.15,0.15]) translate([68.33500000000001, -6.165, 0.01]) linear_extrude(0.05) text("FRONT PORCH", size=2.30, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([64.42, 46.67, -0.15]) cube([13.33, 12.25, 0.15]);
  color([0.15,0.15,0.15]) translate([71.08500000000001, 52.795, 0.01]) linear_extrude(0.05) text("BREAKFAST PORCH", size=1.16, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([77.75, 40.92, -0.15]) cube([24, 15.33, 0.15]);
  color([0.15,0.15,0.15]) translate([89.75, 48.585, 0.01]) linear_extrude(0.05) text("OUTDOOR LIVING", size=2.23, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([101.75, 40.92, -0.15]) cube([11.33, 10.67, 0.15]);
  color([0.15,0.15,0.15]) translate([107.415, 46.255, 0.01]) linear_extrude(0.05) text("OFFICE PORCH", size=1.23, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([113.08, 40.92, -0.15]) cube([19.17, 10, 0.15]);
  color([0.15,0.15,0.15]) translate([122.66499999999999, 45.92, 0.01]) linear_extrude(0.05) text("MASTER PORCH", size=2.08, halign="center", valign="center");
  color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([118.59, 8.92, -0.15]) cube([10, 32, 0.15]);
  color([0.15,0.15,0.15]) translate([123.59, 24.92, 0.01]) linear_extrude(0.05) text("SIDE PORCH", size=1.30, halign="center", valign="center");

  // ---- walls (openings cut)
  color([0.93, 0.91, 0.87]) difference() {
    union() {
      translate([-0.25, -0.25, 0]) cube([25.67, 0.50, 9.67]);
      translate([-0.25, 31.50, 0]) cube([25.67, 0.50, 9.67]);
      translate([-0.25, -0.25, 0]) cube([0.50, 32.25, 9.67]);
      translate([25.00, -0.17, 0]) cube([0.34, 32.09, 9.67]);
      translate([25.00, -0.17, 0]) cube([18.42, 0.34, 12.0]);
      translate([25.00, 13.75, 0]) cube([18.42, 0.34, 12.0]);
      translate([25.00, -0.17, 0]) cube([0.34, 14.26, 12.0]);
      translate([43.08, -0.17, 0]) cube([0.34, 14.26, 12.0]);
      translate([25.00, 13.75, 0]) cube([7.84, 0.34, 12.5]);
      translate([25.00, 19.75, 0]) cube([7.84, 0.34, 12.5]);
      translate([25.00, 13.75, 0]) cube([0.34, 6.34, 12.5]);
      translate([32.50, 13.75, 0]) cube([0.34, 6.34, 12.5]);
      translate([32.50, 13.75, 0]) cube([10.92, 0.34, 12.5]);
      translate([32.50, 19.75, 0]) cube([10.92, 0.34, 12.5]);
      translate([32.50, 13.75, 0]) cube([0.34, 6.34, 12.5]);
      translate([43.08, 13.75, 0]) cube([0.34, 6.34, 12.5]);
      translate([25.00, 19.75, 0]) cube([11.42, 0.34, 12.0]);
      translate([25.00, 27.17, 0]) cube([11.42, 0.34, 12.0]);
      translate([25.00, 19.75, 0]) cube([0.34, 7.76, 12.0]);
      translate([36.08, 19.75, 0]) cube([0.34, 7.76, 12.0]);
      translate([36.08, 19.75, 0]) cube([7.34, 0.34, 12.0]);
      translate([36.08, 27.17, 0]) cube([7.34, 0.34, 12.0]);
      translate([36.08, 19.75, 0]) cube([0.34, 7.76, 12.0]);
      translate([43.08, 19.75, 0]) cube([0.34, 7.76, 12.0]);
      translate([25.00, 27.17, 0]) cube([27.59, 0.34, 12.0]);
      translate([25.00, 30.67, 0]) cube([27.59, 0.34, 12.0]);
      translate([25.00, 27.17, 0]) cube([0.34, 3.84, 12.0]);
      translate([52.17, 27.09, 0]) cube([0.50, 4.00, 12.0]);
      translate([25.00, 30.67, 0]) cube([17.59, 0.34, 12.0]);
      translate([25.00, 44.00, 0]) cube([17.59, 0.34, 12.0]);
      translate([25.00, 30.67, 0]) cube([0.34, 13.67, 12.0]);
      translate([42.25, 30.67, 0]) cube([0.34, 13.67, 12.0]);
      translate([42.25, 30.67, 0]) cube([10.34, 0.34, 12.5]);
      translate([42.25, 44.00, 0]) cube([10.34, 0.34, 12.5]);
      translate([42.25, 30.67, 0]) cube([0.34, 13.67, 12.5]);
      translate([52.25, 30.67, 0]) cube([0.34, 13.67, 12.5]);
      translate([52.17, 30.59, 0]) cube([6.50, 0.50, 12.0]);
      translate([52.25, 37.17, 0]) cube([6.34, 0.34, 12.0]);
      translate([52.25, 30.67, 0]) cube([0.34, 6.84, 12.0]);
      translate([58.25, 30.67, 0]) cube([0.34, 6.84, 12.0]);
      translate([52.25, 37.17, 0]) cube([6.34, 0.34, 12.0]);
      translate([52.25, 44.00, 0]) cube([6.34, 0.34, 12.0]);
      translate([52.25, 37.17, 0]) cube([0.34, 7.17, 12.0]);
      translate([58.25, 37.17, 0]) cube([0.34, 7.17, 12.0]);
      translate([25.00, 44.00, 0]) cube([7.34, 0.34, 12.0]);
      translate([25.00, 51.00, 0]) cube([7.34, 0.34, 12.0]);
      translate([24.92, 43.92, 0]) cube([0.50, 7.50, 12.0]);
      translate([32.00, 44.00, 0]) cube([0.34, 7.34, 12.0]);
      translate([25.00, 51.00, 0]) cube([7.34, 0.34, 12.5]);
      translate([24.92, 57.92, 0]) cube([7.50, 0.50, 12.5]);
      translate([24.92, 50.92, 0]) cube([0.50, 7.50, 12.5]);
      translate([32.00, 51.00, 0]) cube([0.34, 7.34, 12.5]);
      translate([32.00, 44.00, 0]) cube([14.51, 0.34, 12.0]);
      translate([31.92, 58.34, 0]) cube([14.67, 0.50, 12.0]);
      translate([32.00, 44.00, 0]) cube([0.34, 14.76, 12.0]);
      translate([46.17, 44.00, 0]) cube([0.34, 14.76, 12.0]);
      translate([46.17, 44.00, 0]) cube([4.34, 0.34, 12.0]);
      translate([46.17, 48.00, 0]) cube([4.34, 0.34, 12.0]);
      translate([46.17, 44.00, 0]) cube([0.34, 4.34, 12.0]);
      translate([50.17, 44.00, 0]) cube([0.34, 4.34, 12.0]);
      translate([46.17, 48.00, 0]) cube([4.34, 0.34, 12.5]);
      translate([46.09, 58.34, 0]) cube([4.50, 0.50, 12.5]);
      translate([46.17, 48.00, 0]) cube([0.34, 10.76, 12.5]);
      translate([50.17, 48.00, 0]) cube([0.34, 10.76, 12.5]);
      translate([50.17, 44.00, 0]) cube([14.42, 0.34, 14.0]);
      translate([50.09, 58.67, 0]) cube([14.58, 0.50, 14.0]);
      translate([50.17, 44.00, 0]) cube([0.34, 15.09, 14.0]);
      translate([64.25, 44.00, 0]) cube([0.34, 15.09, 14.0]);
      translate([43.08, -0.17, 0]) cube([18.67, 0.34, 14.0]);
      translate([43.08, 14.33, 0]) cube([18.67, 0.34, 14.0]);
      translate([43.08, -0.17, 0]) cube([0.34, 14.84, 14.0]);
      translate([61.41, -0.17, 0]) cube([0.34, 14.84, 14.0]);
      translate([61.41, -0.17, 0]) cube([11.67, 0.34, 14.0]);
      translate([61.41, 13.16, 0]) cube([11.67, 0.34, 14.0]);
      translate([61.41, -0.17, 0]) cube([0.34, 13.67, 14.0]);
      translate([72.66, -0.25, 0]) cube([0.50, 13.83, 14.0]);
      translate([72.75, -0.17, 0]) cube([14.51, 0.34, 14.0]);
      translate([72.67, 11.92, 0]) cube([14.67, 0.50, 14.0]);
      translate([72.67, -0.25, 0]) cube([0.50, 12.67, 14.0]);
      translate([86.92, -0.17, 0]) cube([0.34, 12.51, 14.0]);
      translate([43.08, 14.33, 0]) cube([3.67, 0.34, 12.0]);
      translate([43.00, 23.25, 0]) cube([3.83, 0.50, 12.0]);
      translate([43.08, 14.33, 0]) cube([0.34, 9.34, 12.0]);
      translate([46.41, 14.33, 0]) cube([0.34, 9.34, 12.0]);
      translate([46.41, 14.33, 0]) cube([15.34, 0.34, 14.0]);
      translate([46.33, 23.25, 0]) cube([15.50, 0.50, 14.0]);
      translate([46.41, 14.33, 0]) cube([0.34, 9.34, 14.0]);
      translate([61.41, 14.33, 0]) cube([0.34, 9.34, 14.0]);
      translate([61.41, 13.16, 0]) cube([10.51, 0.34, 14.0]);
      translate([61.41, 25.58, 0]) cube([10.51, 0.34, 14.0]);
      translate([61.41, 13.16, 0]) cube([0.34, 12.76, 14.0]);
      translate([71.58, 13.16, 0]) cube([0.34, 12.76, 14.0]);
      translate([71.50, 14.25, 0]) cube([15.00, 0.50, 14.0]);
      translate([71.58, 14.33, 0]) cube([0.34, 9.34, 14.0]);
      translate([86.00, 14.25, 0]) cube([0.50, 9.50, 14.0]);
      translate([58.25, 25.58, 0]) cube([14.34, 0.34, 14.0]);
      translate([58.17, 40.50, 0]) cube([14.50, 0.50, 14.0]);
      translate([58.25, 25.58, 0]) cube([0.34, 15.34, 14.0]);
      translate([72.25, 40.75, 0]) cube([16.84, 0.34, 16.0]);
      translate([88.75, 25.58, 0]) cube([0.34, 15.51, 16.0]);
      translate([88.75, 16.33, 0]) cube([12.34, 0.34, 14.0]);
      translate([88.75, 28.75, 0]) cube([12.34, 0.34, 14.0]);
      translate([88.75, 16.33, 0]) cube([0.34, 12.76, 14.0]);
      translate([100.75, 16.33, 0]) cube([0.34, 12.76, 14.0]);
      translate([88.75, 28.75, 0]) cube([12.34, 0.34, 14.0]);
      translate([88.75, 40.75, 0]) cube([12.34, 0.34, 14.0]);
      translate([88.75, 28.75, 0]) cube([0.34, 12.34, 14.0]);
      translate([100.75, 28.75, 0]) cube([0.34, 12.34, 14.0]);
      translate([100.67, 18.00, 0]) cube([18.17, 0.50, 16.0]);
      translate([100.75, 40.75, 0]) cube([18.01, 0.34, 16.0]);
      translate([100.75, 18.08, 0]) cube([0.34, 23.01, 16.0]);
      translate([118.42, 18.08, 0]) cube([0.34, 23.01, 16.0]);
      translate([86.92, -0.17, 0]) cube([9.17, 0.34, 12.0]);
      translate([86.92, 16.33, 0]) cube([9.17, 0.34, 12.0]);
      translate([86.92, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([95.75, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([95.75, -0.17, 0]) cube([9.17, 0.34, 12.0]);
      translate([95.75, 16.33, 0]) cube([9.17, 0.34, 12.0]);
      translate([95.75, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([104.58, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([104.50, -0.25, 0]) cube([14.34, 0.50, 12.0]);
      translate([104.50, 16.25, 0]) cube([14.34, 0.50, 12.0]);
      translate([104.58, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([118.42, -0.17, 0]) cube([0.34, 16.84, 12.0]);
      translate([118.34, 8.67, 0]) cube([10.50, 0.50, 3.0]);
      translate([118.42, 8.75, 0]) cube([0.34, 32.34, 3.0]);
      translate([128.34, 8.67, 0]) cube([0.50, 32.50, 3.0]);
    }
    translate([64, -0.8, -0.1]) cube([5, 1.6, 7.1]);
    translate([46, -0.8, -0.1]) cube([4, 1.6, 7.1]);
    translate([54, -0.8, -0.1]) cube([4, 1.6, 7.1]);
    translate([76, -0.8, -0.1]) cube([4, 1.6, 7.1]);
    translate([82, -0.8, -0.1]) cube([4, 1.6, 7.1]);
    translate([24.37, 22, -0.1]) cube([1.6, 3, 7.1]);
    translate([35.45, 22, -0.1]) cube([1.6, 3, 7.1]);
    translate([27, 26.54, -0.1]) cube([3, 1.6, 7.1]);
    translate([38, 13.12, -0.1]) cube([3, 1.6, 7.1]);
    translate([28, 13.12, -0.1]) cube([2.5, 1.6, 7.1]);
    translate([38, 30.04, -0.1]) cube([3, 1.6, 7.1]);
    translate([46, 30.04, -0.1]) cube([3, 1.6, 7.1]);
    translate([55.42, 36.540000000000006, -0.1]) cube([3, 1.6, 7.1]);
    translate([38, 43.370000000000005, -0.1]) cube([3, 1.6, 7.1]);
    translate([47, 43.370000000000005, -0.1]) cube([2.5, 1.6, 7.1]);
    translate([31.37, 53, -0.1]) cube([1.6, 2.5, 7.1]);
    translate([63.620000000000005, 50, -0.1]) cube([1.6, 4, 7.1]);
    translate([50, 13.7, -0.1]) cube([3, 1.6, 7.1]);
    translate([63, 12.53, -0.1]) cube([5, 1.6, 7.1]);
    translate([63, 24.95, -0.1]) cube([5, 1.6, 7.1]);
    translate([76, 22.7, -0.1]) cube([4, 1.6, 7.1]);
    translate([71.62, 30, -0.1]) cube([1.6, 5, 7.1]);
    translate([62, 39.95, -0.1]) cube([4, 1.6, 7.1]);
    translate([78, 40.120000000000005, -0.1]) cube([6, 1.6, 7.1]);
    translate([94, 28.12, -0.1]) cube([3, 1.6, 7.1]);
    translate([95, 40.120000000000005, -0.1]) cube([3, 1.6, 7.1]);
    translate([104, 17.45, -0.1]) cube([4, 1.6, 7.1]);
    translate([108, 40.120000000000005, -0.1]) cube([5, 1.6, 7.1]);
    translate([117.79, 24, -0.1]) cube([1.6, 5, 7.1]);
    translate([117.79, 33, -0.1]) cube([1.6, 4, 7.1]);
    translate([110, 15.7, -0.1]) cube([3, 1.6, 7.1]);
    translate([90, 15.7, -0.1]) cube([3, 1.6, 7.1]);
    translate([99, 15.7, -0.1]) cube([3, 1.6, 7.1]);
    translate([46, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([53, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([75, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([82, -0.8, 2.5]) cube([5, 1.6, 4.0]);
    translate([30, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([108, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([-0.8, 10, 2.5]) cube([1.6, 6, 4.0]);
    translate([-0.8, 22, 2.5]) cube([1.6, 6, 4.0]);
    translate([8, -0.8, 2.5]) cube([6, 1.6, 4.0]);
    translate([24.37, 34, 2.5]) cube([1.6, 6, 4.0]);
    translate([24.37, 53, 2.5]) cube([1.6, 3, 4.0]);
    translate([36, 57.790000000000006, 2.5]) cube([6, 1.6, 4.0]);
    translate([54, 58.120000000000005, 2.5]) cube([6, 1.6, 4.0]);
    translate([62, 39.95, 2.5]) cube([5, 1.6, 4.0]);
    translate([76, 40.120000000000005, 2.5]) cube([8, 1.6, 4.0]);
    translate([92, 40.120000000000005, 2.5]) cube([6, 1.6, 4.0]);
    translate([106, 40.120000000000005, 2.5]) cube([6, 1.6, 4.0]);
    translate([86.29, 4, 2.5]) cube([1.6, 5, 4.0]);
  }

  // ---- window panes
  color([0.53, 0.81, 0.92, 0.55]) {
    translate([46, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([53, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([75, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([82, -0.06, 2.5]) cube([5, 0.12, 4.0]);
    translate([30, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([108, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([-0.06, 10, 2.5]) cube([0.12, 6, 4.0]);
    translate([-0.06, 22, 2.5]) cube([0.12, 6, 4.0]);
    translate([8, -0.06, 2.5]) cube([6, 0.12, 4.0]);
    translate([25.110000000000003, 34, 2.5]) cube([0.12, 6, 4.0]);
    translate([25.110000000000003, 53, 2.5]) cube([0.12, 3, 4.0]);
    translate([36, 58.53, 2.5]) cube([6, 0.12, 4.0]);
    translate([54, 58.86, 2.5]) cube([6, 0.12, 4.0]);
    translate([62, 40.69, 2.5]) cube([5, 0.12, 4.0]);
    translate([76, 40.86, 2.5]) cube([8, 0.12, 4.0]);
    translate([92, 40.86, 2.5]) cube([6, 0.12, 4.0]);
    translate([106, 40.86, 2.5]) cube([6, 0.12, 4.0]);
    translate([87.03, 4, 2.5]) cube([0.12, 5, 4.0]);
  }

  // ---- door leaves (ajar 30 deg)
  color([0.55, 0.35, 0.2]) {
    translate([64, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([46, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([54, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([76, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([82, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([25.17, 22, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([36.25, 22, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([27, 27.34, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([38, 13.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([28, 13.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([2.5, 0.18, 7.0]);
    translate([38, 30.84, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([46, 30.84, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([55.42, 37.34, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([38, 44.17, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([47, 44.17, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([2.5, 0.18, 7.0]);
    translate([32.17, 53, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([2.5, 0.18, 7.0]);
    translate([64.42, 50, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([50, 14.5, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([63, 13.33, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([63, 25.75, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([76, 23.5, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([72.42, 30, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([62, 40.75, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([78, 40.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([6, 0.18, 7.0]);
    translate([94, 28.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([95, 40.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([104, 18.25, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([108, 40.92, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([118.59, 24, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
    translate([118.59, 33, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
    translate([110, 16.5, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([90, 16.5, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
    translate([99, 16.5, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  }

  // ---- furniture
  color([0.5450980392156862, 0.27058823529411763, 0.07450980392156863]) translate([65, 30, 0]) cube([3, 8, 3.5]);

  // fireplace: Fireplace
  color([0.3,0.3,0.3]) translate([43.25, 10, 0]) cube([3, 4, 5.0]);
  color([0.05,0.05,0.05]) translate([43.95, 9.95, 0.6]) cube([1.6, 0.3, 1.8]);

  // fireplace: Fireplace
  color([0.3,0.3,0.3]) translate([86.42, 31, 0]) cube([2.5, 4, 5.0]);
  color([0.05,0.05,0.05]) translate([87.12, 30.95, 0.6]) cube([1.1, 0.3, 1.8]);

  // ---- porch columns + roof: FRONT PORCH
  color([0.96, 0.95, 0.92]) {
    translate([39.62, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([39.62, -0.38, 0]) cube([0.75, 0.75, 12.67]);
    translate([49.08, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([58.52, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([67.97, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([77.41, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([86.84, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([96.30, -12.71, 0]) cube([0.75, 0.75, 12.67]);
    translate([96.30, -0.38, 0]) cube([0.75, 0.75, 12.67]);
  }
  color([0.30, 0.30, 0.32]) {
    translate([39.00, -13.33, 12.67]) cube([58.67, 13.33, 0.75]);
  }
  color([0.80, 0.80, 0.78]) {
    translate([63.25, -13.33, -0.50]) cube([8.0, 1.0, 0.5]);
    translate([63.25, -14.33, -1.00]) cube([8.0, 1.0, 0.5]);
    translate([63.25, -15.33, -1.50]) cube([8.0, 1.0, 0.5]);
    translate([63.25, -16.33, -2.00]) cube([8.0, 1.0, 0.5]);
  }

  // stairs: DN
  color([0.75, 0.72, 0.68]) {
    translate([25.17, 27.34, 0]) cube([0.83, 3.5, 1.00]);
    translate([26.00, 27.34, 0]) cube([0.83, 3.5, 2.00]);
    translate([26.84, 27.34, 0]) cube([0.83, 3.5, 3.00]);
    translate([27.67, 27.34, 0]) cube([0.83, 3.5, 4.00]);
    translate([28.50, 27.34, 0]) cube([0.83, 3.5, 5.00]);
    translate([29.34, 27.34, 0]) cube([0.83, 3.5, 6.00]);
    translate([30.17, 27.34, 0]) cube([0.83, 3.5, 7.00]);
    translate([31.00, 27.34, 0]) cube([0.83, 3.5, 8.00]);
    translate([31.84, 27.34, 0]) cube([0.83, 3.5, 9.00]);
    translate([32.67, 27.34, 0]) cube([0.83, 3.5, 10.00]);
    translate([33.50, 27.34, 0]) cube([0.83, 3.5, 11.00]);
    translate([34.34, 27.34, 0]) cube([0.83, 3.5, 12.00]);
  }


// ---- back porch columns + roofs
color([0.96, 0.95, 0.92]) {
  translate([64.05, 46.30, 0]) cube([0.75, 0.75, 14.0]);
  translate([64.05, 58.55, 0]) cube([0.75, 0.75, 14.0]);
  translate([77.38, 40.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([77.38, 46.30, 0]) cube([0.75, 0.75, 14.0]);
  translate([77.38, 48.22, 0]) cube([0.75, 0.75, 16.0]);
  translate([77.38, 55.88, 0]) cube([0.75, 0.75, 16.0]);
  translate([77.38, 58.55, 0]) cube([0.75, 0.75, 14.0]);
  translate([85.38, 55.88, 0]) cube([0.75, 0.75, 16.0]);
  translate([93.38, 55.88, 0]) cube([0.75, 0.75, 16.0]);
  translate([101.38, 40.55, 0]) cube([0.75, 0.75, 14.0]);
  translate([101.38, 40.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([101.38, 48.22, 0]) cube([0.75, 0.75, 16.0]);
  translate([101.38, 51.22, 0]) cube([0.75, 0.75, 14.0]);
  translate([101.38, 55.88, 0]) cube([0.75, 0.75, 16.0]);
  translate([112.70, 40.55, 0]) cube([0.75, 0.75, 14.0]);
  translate([112.70, 40.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([112.70, 50.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([112.70, 51.22, 0]) cube([0.75, 0.75, 14.0]);
  translate([122.28, 50.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([131.88, 40.55, 0]) cube([0.75, 0.75, 16.0]);
  translate([131.88, 50.55, 0]) cube([0.75, 0.75, 16.0]);
}
color([0.30, 0.30, 0.32]) {
  translate([64.42, 45.67, 14.0]) cube([14.33, 14.25, 0.75]);
  translate([76.75, 40.92, 16.0]) cube([26.00, 16.33, 0.75]);
  translate([100.75, 40.92, 14.0]) cube([13.33, 11.67, 0.75]);
  translate([112.08, 40.92, 16.0]) cube([21.17, 11.00, 0.75]);
}
// ---- back porch steps to the yard
color([0.80, 0.80, 0.78]) {
  translate([68.09, 58.92, -0.50]) cube([6.0, 1.0, 0.5]);
  translate([68.09, 59.92, -1.00]) cube([6.0, 1.0, 0.5]);
  translate([68.09, 60.92, -1.50]) cube([6.0, 1.0, 0.5]);
  translate([68.09, 61.92, -2.00]) cube([6.0, 1.0, 0.5]);
  translate([85.75, 56.25, -0.50]) cube([8.0, 1.0, 0.5]);
  translate([85.75, 57.25, -1.00]) cube([8.0, 1.0, 0.5]);
  translate([85.75, 58.25, -1.50]) cube([8.0, 1.0, 0.5]);
  translate([85.75, 59.25, -2.00]) cube([8.0, 1.0, 0.5]);
}
}

basement_z = (mode == "exploded") ? -12 - explode_gap : -12;
main_z = (mode == "exploded") ? explode_gap / 2 : 0;
if (mode != "main_only")
  translate([basement_dx, basement_dy, basement_z]) basement_level();
if (mode != "basement_only")
  translate([0, 0, main_z]) main_level();
