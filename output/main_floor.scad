// Main floor — generated from config/floorplan.yaml by generate_scad.py
// Units: feet. Dollhouse view (no roof). NOT construction documents.
wall_h = 9.0;
$fn = 24;

// ---- floor plates
color([0.9607843137254902, 0.9607843137254902, 0.9607843137254902]) translate([0, 10, -0.15]) cube([25, 32, 0.15]);
color([0.15,0.15,0.15]) translate([12.5, 26.0, 0.01]) linear_extrude(0.05) text("GARAGE", size=2.30, halign="center", valign="center");
color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([25, 10, -0.15]) cube([15, 12, 0.15]);
color([0.15,0.15,0.15]) translate([32.5, 16.0, 0.01]) linear_extrude(0.05) text("MUD ROOM", size=2.30, halign="center", valign="center");
color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([25, 22, -0.15]) cube([15, 14, 0.15]);
color([0.15,0.15,0.15]) translate([32.5, 29.0, 0.01]) linear_extrude(0.05) text("BEDROOM 4", size=2.17, halign="center", valign="center");
color([0.8784313725490196, 1.0, 1.0]) translate([25, 36, -0.15]) cube([7, 8, 0.15]);
color([0.15,0.15,0.15]) translate([28.5, 40.0, 0.01]) linear_extrude(0.05) text("BATH 4", size=1.52, halign="center", valign="center");
color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([32, 36, -0.15]) cube([8, 8, 0.15]);
color([0.15,0.15,0.15]) translate([36.0, 40.0, 0.01]) linear_extrude(0.05) text("LAUNDRY", size=1.49, halign="center", valign="center");
color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([25, 44, -0.15]) cube([15, 14, 0.15]);
color([0.15,0.15,0.15]) translate([32.5, 51.0, 0.01]) linear_extrude(0.05) text("BEDROOM 3", size=2.17, halign="center", valign="center");
color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([25, 58, -0.15]) cube([15, 14, 0.15]);
color([0.15,0.15,0.15]) translate([32.5, 65.0, 0.01]) linear_extrude(0.05) text("BEDROOM 2", size=2.17, halign="center", valign="center");
color([1.0, 0.984313725490196, 0.9215686274509803]) translate([40, 10, -0.15]) cube([3, 62, 0.15]);
color([0.15,0.15,0.15]) translate([41.5, 41.0, 0.01]) linear_extrude(0.05) text("HALL", size=0.98, halign="center", valign="center");
color([1.0, 0.9725490196078431, 0.8627450980392157]) translate([43, 0, -0.15]) cube([18, 15, 0.15]);
color([0.15,0.15,0.15]) translate([52.0, 7.5, 0.01]) linear_extrude(0.05) text("DINING ROOM", size=2.13, halign="center", valign="center");
color([1.0, 0.984313725490196, 0.9215686274509803]) translate([61, 0, -0.15]) cube([12, 15, 0.15]);
color([0.15,0.15,0.15]) translate([67.0, 7.5, 0.01]) linear_extrude(0.05) text("FOYER", size=2.30, halign="center", valign="center");
color([1.0, 0.9725490196078431, 0.8627450980392157]) translate([73, 0, -0.15]) cube([14, 15, 0.15]);
color([0.15,0.15,0.15]) translate([80.0, 7.5, 0.01]) linear_extrude(0.05) text("LOUNGE", size=2.30, halign="center", valign="center");
color([1.0, 0.8745098039215686, 0.7294117647058823]) translate([43, 15, -0.15]) cube([14, 10, 0.15]);
color([0.15,0.15,0.15]) translate([50.0, 20.0, 0.01]) linear_extrude(0.05) text("BUTLER'S PANTRY", size=1.21, halign="center", valign="center");
color([1.0, 0.984313725490196, 0.9215686274509803]) translate([57, 15, -0.15]) cube([4, 10, 0.15]);
color([0.15,0.15,0.15]) translate([59.0, 20.0, 0.01]) linear_extrude(0.05) text("STAIR", size=1.04, halign="center", valign="center");
color([1.0, 0.9333333333333333, 0.7333333333333333]) translate([43, 25, -0.15]) cube([20, 18, 0.15]);
color([0.15,0.15,0.15]) translate([53.0, 34.0, 0.01]) linear_extrude(0.05) text("KITCHEN", size=2.30, halign="center", valign="center");
color([0.9803921568627451, 0.9803921568627451, 0.9803921568627451]) translate([63, 25, -0.15]) cube([24, 18, 0.15]);
color([0.15,0.15,0.15]) translate([75.0, 34.0, 0.01]) linear_extrude(0.05) text("FAMILY ROOM", size=2.30, halign="center", valign="center");
color([0.9607843137254902, 0.9607843137254902, 0.9607843137254902]) translate([87, 25, -0.15]) cube([14, 14, 0.15]);
color([0.15,0.15,0.15]) translate([94.0, 32.0, 0.01]) linear_extrude(0.05) text("OFFICE", size=2.30, halign="center", valign="center");
color([1.0, 0.9921568627450981, 0.9058823529411765]) translate([87, 0, -0.15]) cube([20, 25, 0.15]);
color([0.15,0.15,0.15]) translate([97.0, 12.5, 0.01]) linear_extrude(0.05) text("MASTER SUITE", size=2.17, halign="center", valign="center");
color([0.8784313725490196, 1.0, 1.0]) translate([107, 0, -0.15]) cube([14, 15, 0.15]);
color([0.15,0.15,0.15]) translate([114.0, 7.5, 0.01]) linear_extrude(0.05) text("MASTER BATH", size=1.65, halign="center", valign="center");
color([0.9411764705882353, 0.9411764705882353, 0.9411764705882353]) translate([107, 15, -0.15]) cube([14, 10, 0.15]);
color([0.15,0.15,0.15]) translate([114.0, 20.0, 0.01]) linear_extrude(0.05) text("WIC", size=2.30, halign="center", valign="center");
color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([40, -10, -0.15]) cube([50, 10, 0.15]);
color([0.15,0.15,0.15]) translate([65.0, -5.0, 0.01]) linear_extrude(0.05) text("FRONT PORCH", size=2.30, halign="center", valign="center");
color([0.9411764705882353, 1.0, 0.9411764705882353]) translate([43, 43, -0.15]) cube([44, 15, 0.15]);
color([0.15,0.15,0.15]) translate([65.0, 50.5, 0.01]) linear_extrude(0.05) text("OUTDOOR LIVING", size=2.30, halign="center", valign="center");

// ---- walls (openings cut)
color([0.93, 0.91, 0.87]) difference() {
  union() {
    translate([-0.25, 9.75, 0]) cube([25.50, 0.50, 9.0]);
    translate([-0.25, 41.75, 0]) cube([25.50, 0.50, 9.0]);
    translate([-0.25, 9.75, 0]) cube([0.50, 32.50, 9.0]);
    translate([24.83, 9.83, 0]) cube([0.34, 32.34, 9.0]);
    translate([24.75, 9.75, 0]) cube([15.50, 0.50, 9.0]);
    translate([24.83, 21.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.83, 9.83, 0]) cube([0.34, 12.34, 9.0]);
    translate([39.83, 9.83, 0]) cube([0.34, 12.34, 9.0]);
    translate([24.83, 21.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.83, 35.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.83, 21.83, 0]) cube([0.34, 14.34, 9.0]);
    translate([39.83, 21.83, 0]) cube([0.34, 14.34, 9.0]);
    translate([24.83, 35.83, 0]) cube([7.34, 0.34, 9.0]);
    translate([24.83, 43.83, 0]) cube([7.34, 0.34, 9.0]);
    translate([24.83, 35.83, 0]) cube([0.34, 8.34, 9.0]);
    translate([31.83, 35.83, 0]) cube([0.34, 8.34, 9.0]);
    translate([31.83, 35.83, 0]) cube([8.34, 0.34, 9.0]);
    translate([31.83, 43.83, 0]) cube([8.34, 0.34, 9.0]);
    translate([31.83, 35.83, 0]) cube([0.34, 8.34, 9.0]);
    translate([39.83, 35.83, 0]) cube([0.34, 8.34, 9.0]);
    translate([24.83, 43.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.83, 57.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.75, 43.75, 0]) cube([0.50, 14.50, 9.0]);
    translate([39.83, 43.83, 0]) cube([0.34, 14.34, 9.0]);
    translate([24.83, 57.83, 0]) cube([15.34, 0.34, 9.0]);
    translate([24.75, 71.75, 0]) cube([15.50, 0.50, 9.0]);
    translate([24.75, 57.75, 0]) cube([0.50, 14.50, 9.0]);
    translate([39.83, 57.83, 0]) cube([0.34, 14.34, 9.0]);
    translate([39.75, 9.75, 0]) cube([3.50, 0.50, 9.0]);
    translate([39.75, 71.75, 0]) cube([3.50, 0.50, 9.0]);
    translate([39.83, 9.83, 0]) cube([0.34, 62.34, 9.0]);
    translate([42.83, 9.83, 0]) cube([0.34, 62.34, 9.0]);
    translate([42.83, -0.17, 0]) cube([18.34, 0.34, 9.0]);
    translate([42.83, 14.83, 0]) cube([18.34, 0.34, 9.0]);
    translate([42.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([60.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([60.83, -0.17, 0]) cube([12.34, 0.34, 9.0]);
    translate([60.75, 14.75, 0]) cube([12.50, 0.50, 9.0]);
    translate([60.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([72.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([72.83, -0.17, 0]) cube([14.34, 0.34, 9.0]);
    translate([72.75, 14.75, 0]) cube([14.50, 0.50, 9.0]);
    translate([72.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([86.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([42.83, 14.83, 0]) cube([14.34, 0.34, 9.0]);
    translate([42.83, 24.83, 0]) cube([14.34, 0.34, 9.0]);
    translate([42.83, 14.83, 0]) cube([0.34, 10.34, 9.0]);
    translate([56.83, 14.83, 0]) cube([0.34, 10.34, 9.0]);
    translate([56.83, 14.83, 0]) cube([4.34, 0.34, 9.0]);
    translate([56.83, 24.83, 0]) cube([4.34, 0.34, 9.0]);
    translate([56.83, 14.83, 0]) cube([0.34, 10.34, 9.0]);
    translate([60.75, 14.75, 0]) cube([0.50, 10.50, 9.0]);
    translate([42.83, 24.83, 0]) cube([20.34, 0.34, 9.0]);
    translate([42.83, 42.83, 0]) cube([20.34, 0.34, 9.0]);
    translate([42.83, 24.83, 0]) cube([0.34, 18.34, 9.0]);
    translate([62.83, 24.83, 0]) cube([0.34, 18.34, 9.0]);
    translate([62.75, 24.75, 0]) cube([24.50, 0.50, 9.0]);
    translate([62.83, 42.83, 0]) cube([24.34, 0.34, 9.0]);
    translate([62.83, 24.83, 0]) cube([0.34, 18.34, 9.0]);
    translate([86.83, 24.83, 0]) cube([0.34, 18.34, 9.0]);
    translate([86.83, 24.83, 0]) cube([14.34, 0.34, 9.0]);
    translate([86.75, 38.75, 0]) cube([14.50, 0.50, 9.0]);
    translate([86.83, 24.83, 0]) cube([0.34, 14.34, 9.0]);
    translate([100.75, 24.75, 0]) cube([0.50, 14.50, 9.0]);
    translate([86.83, -0.17, 0]) cube([20.34, 0.34, 9.0]);
    translate([86.83, 24.83, 0]) cube([20.34, 0.34, 9.0]);
    translate([86.83, -0.17, 0]) cube([0.34, 25.34, 9.0]);
    translate([106.83, -0.17, 0]) cube([0.34, 25.34, 9.0]);
    translate([106.75, -0.25, 0]) cube([14.50, 0.50, 9.0]);
    translate([106.83, 14.83, 0]) cube([14.34, 0.34, 9.0]);
    translate([106.83, -0.17, 0]) cube([0.34, 15.34, 9.0]);
    translate([120.75, -0.25, 0]) cube([0.50, 15.50, 9.0]);
    translate([106.83, 14.83, 0]) cube([14.34, 0.34, 9.0]);
    translate([106.75, 24.75, 0]) cube([14.50, 0.50, 9.0]);
    translate([106.83, 14.83, 0]) cube([0.34, 10.34, 9.0]);
    translate([120.75, 14.75, 0]) cube([0.50, 10.50, 9.0]);
    translate([39.75, -10.25, 0]) cube([50.50, 0.50, 3.0]);
    translate([39.83, -0.17, 0]) cube([50.34, 0.34, 3.0]);
    translate([39.75, -10.25, 0]) cube([0.50, 10.50, 3.0]);
    translate([89.75, -10.25, 0]) cube([0.50, 10.50, 3.0]);
    translate([42.83, 42.83, 0]) cube([44.34, 0.34, 3.0]);
    translate([42.75, 57.75, 0]) cube([44.50, 0.50, 3.0]);
    translate([42.83, 42.83, 0]) cube([0.34, 15.34, 3.0]);
    translate([86.75, 42.75, 0]) cube([0.50, 15.50, 3.0]);
  }
  translate([48, -0.8, -0.1]) cube([5, 1.6, 7.1]);
  translate([24.2, 12, -0.1]) cube([1.6, 3, 7.1]);
  translate([24.2, 18, -0.1]) cube([1.6, 3, 7.1]);
  translate([86.2, 5, -0.1]) cube([1.6, 3, 7.1]);
  translate([86.2, 28, -0.1]) cube([1.6, 4, 7.1]);
  translate([39.2, 60, -0.1]) cube([1.6, 3, 7.1]);
  translate([39.2, 46, -0.1]) cube([1.6, 3, 7.1]);
  translate([39.2, 24, -0.1]) cube([1.6, 3, 7.1]);
  translate([39.2, 14, -0.1]) cube([1.6, 3, 7.1]);
  translate([39.2, 38, -0.1]) cube([1.6, 3, 7.1]);
  translate([50, 24.2, -0.1]) cube([3, 1.6, 7.1]);
  translate([62.2, 30, -0.1]) cube([1.6, 4, 7.1]);
  translate([60.2, 5, -0.1]) cube([1.6, 4, 7.1]);
  translate([72.2, 5, -0.1]) cube([1.6, 3, 7.1]);
  translate([106.2, 5, -0.1]) cube([1.6, 3, 7.1]);
  translate([106.2, 18, -0.1]) cube([1.6, 3, 7.1]);
  translate([55, 42.2, -0.1]) cube([5, 1.6, 7.1]);
  translate([65, -0.8, -0.1]) cube([4, 1.6, 7.1]);
  translate([45, -0.8, 2.5]) cube([6, 1.6, 4.0]);
  translate([75, -0.8, 2.5]) cube([6, 1.6, 4.0]);
  translate([-0.8, 20, 2.5]) cube([1.6, 6, 4.0]);
  translate([106.2, 10, 2.5]) cube([1.6, 8, 4.0]);
  translate([65, 42.2, 2.5]) cube([8, 1.6, 4.0]);
  translate([45, 42.2, 2.5]) cube([6, 1.6, 4.0]);
  translate([30, 71.2, 2.5]) cube([6, 1.6, 4.0]);
  translate([24.2, 48, 2.5]) cube([1.6, 5, 4.0]);
  translate([24.2, 28, 2.5]) cube([1.6, 5, 4.0]);
  translate([92, -0.8, 2.5]) cube([8, 1.6, 4.0]);
  translate([77, 14.2, 2.5]) cube([6, 1.6, 4.0]);
  translate([42.2, 35, 2.5]) cube([1.6, 5, 4.0]);
}

// ---- window panes
color([0.53, 0.81, 0.92, 0.55]) {
  translate([45, -0.06, 2.5]) cube([6, 0.12, 4.0]);
  translate([75, -0.06, 2.5]) cube([6, 0.12, 4.0]);
  translate([-0.06, 20, 2.5]) cube([0.12, 6, 4.0]);
  translate([106.94, 10, 2.5]) cube([0.12, 8, 4.0]);
  translate([65, 42.94, 2.5]) cube([8, 0.12, 4.0]);
  translate([45, 42.94, 2.5]) cube([6, 0.12, 4.0]);
  translate([30, 71.94, 2.5]) cube([6, 0.12, 4.0]);
  translate([24.94, 48, 2.5]) cube([0.12, 5, 4.0]);
  translate([24.94, 28, 2.5]) cube([0.12, 5, 4.0]);
  translate([92, -0.06, 2.5]) cube([8, 0.12, 4.0]);
  translate([77, 14.94, 2.5]) cube([6, 0.12, 4.0]);
  translate([42.94, 35, 2.5]) cube([0.12, 5, 4.0]);
}

// ---- door leaves (ajar 30 deg)
color([0.55, 0.35, 0.2]) {
  translate([48, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
  translate([25, 12, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([25, 18, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([87, 5, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([87, 28, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
  translate([40, 60, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([40, 46, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([40, 24, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([40, 14, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([40, 38, 0]) rotate([0,0,60]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([50, 25, 0]) rotate([0,0,-150]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([63, 30, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
  translate([61, 5, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
  translate([73, 5, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([107, 5, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([107, 18, 0]) rotate([0,0,120]) translate([0, -0.09, 0]) cube([3, 0.18, 7.0]);
  translate([55, 43, 0]) rotate([0,0,-150]) translate([0, -0.09, 0]) cube([5, 0.18, 7.0]);
  translate([65, 0, 0]) rotate([0,0,30]) translate([0, -0.09, 0]) cube([4, 0.18, 7.0]);
}

// fireplace: Gas Fireplace
color([0.3,0.3,0.3]) translate([75, 25, 0]) cube([4, 3, 5.0]);
color([0.05,0.05,0.05]) translate([75.7, 24.95, 0.6]) cube([2.6, 0.3, 1.8]);

// stairs: DN
color([0.75, 0.72, 0.68]) {
  translate([57, 15.00, 0]) cube([4, 1.00, 0.90]);
  translate([57, 16.00, 0]) cube([4, 1.00, 1.80]);
  translate([57, 17.00, 0]) cube([4, 1.00, 2.70]);
  translate([57, 18.00, 0]) cube([4, 1.00, 3.60]);
  translate([57, 19.00, 0]) cube([4, 1.00, 4.50]);
  translate([57, 20.00, 0]) cube([4, 1.00, 5.40]);
  translate([57, 21.00, 0]) cube([4, 1.00, 6.30]);
  translate([57, 22.00, 0]) cube([4, 1.00, 7.20]);
  translate([57, 23.00, 0]) cube([4, 1.00, 8.10]);
  translate([57, 24.00, 0]) cube([4, 1.00, 9.00]);
}

