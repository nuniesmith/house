// Option C stair only (both flights, landing), for the section render.
use <../../../models/house_lib.scad>
function sc_rise() = floor_to_floor() / 22;
function sc_run()  = 10.5 / 12;
function sc_n1()   = 18;
function sc_land_y() = [27.8, stair_top_y() - (sc_n1() - 1) * sc_run()];
module main_stair_c(z_main = 0, y_box = 45.34) {
    x0 = stair_x()[0] + wall_t() / 2;
    x1 = stair_x()[1] - wall_t() / 2;
    zb = z_main - floor_to_floor();
    paint(stair_color())
        for (i = [1 : sc_n1() - 1]) {
            ya = stair_top_y() - i * sc_run();
            z = z_main - i * sc_rise();
            zf = ya + sc_run() / 2 > y_box ? z_main - main_floor_depth() - 0.125 : zb;
            translate([x0, ya, zf]) cube([x1 - x0, sc_run() + 0.08, z - zf]);
        }
    zl = z_main - sc_n1() * sc_rise();
    paint(stair_color()) translate([x0, sc_land_y()[0], zb]) cube([x1 - x0, sc_land_y()[1] - sc_land_y()[0], zl - zb]);
    paint(stair_color())
        for (j = [1 : 3])
            translate([x1 + (j - 1) * sc_run(), sc_land_y()[0], zb])
                cube([sc_run() + 0.02, sc_land_y()[1] - sc_land_y()[0], zl - j * sc_rise() - zb]);
}
color([0.6,0.6,0.6,0.5]) translate([30,15,-13.8]) cube([30,40,0.05]);
main_stair_c();
