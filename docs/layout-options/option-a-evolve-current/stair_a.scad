// Option A stair only (both flights, landing), for the section render.
use <../../../models/house_lib.scad>
function sa_rise() = floor_to_floor() / 22;
function sa_run()  = 10.5 / 12;
function sa_n1()   = 18;
function sa_land_y() = [27.8, stair_top_y() - (sa_n1() - 1) * sa_run()];   // 27.8 .. 32.225
module main_stair_a(z_main = 0, y_box = 45.34) {
    x0 = stair_x()[0] + wall_t() / 2;
    x1 = stair_x()[1] - wall_t() / 2;
    zb = z_main - floor_to_floor();
    paint(stair_color())
        for (i = [1 : sa_n1() - 1]) {
            ya = stair_top_y() - i * sa_run();
            z = z_main - i * sa_rise();
            zf = ya + sa_run() / 2 > y_box ? z_main - main_floor_depth() - 0.125 : zb;
            translate([x0, ya, zf]) cube([x1 - x0, sa_run() + 0.08, z - zf]);
        }
    zl = z_main - sa_n1() * sa_rise();
    paint(stair_color()) translate([x0, sa_land_y()[0], zb]) cube([x1 - x0, sa_land_y()[1] - sa_land_y()[0], zl - zb]);
    paint(stair_color())
        for (j = [1 : 3])
            translate([x1 + (j - 1) * sa_run(), sa_land_y()[0], zb])
                cube([sa_run() + 0.02, sa_land_y()[1] - sa_land_y()[0], zl - j * sa_rise() - zb]);
    paint([0.40, 0.28, 0.18])
        for (x = [x0 + 0.1, x1 - 0.2])
            hull() {
                translate([x, stair_top_y(), z_main + 2.8]) cube([0.1, 0.1, 0.12]);
                translate([x, sa_land_y()[1], zl + 2.8]) cube([0.1, 0.1, 0.12]);
            }
}


// basement slab
color([0.6,0.6,0.6,0.5]) translate([30,15,-13.8]) cube([30,40,0.05]);
main_stair_a();
