// export.scad - echoes every table of the house model, one "name = value"
// line each, for tools/model_data.py (the drawing set and the checks read
// the model through it, so there is still one copy of each table).
// Run: openscad -o model.echo export.scad

use <house_lib.scad>
use <main_floor.scad>
use <basement.scad>
use <foundation.scad>

$cut = undef;

echo(levels = [["floor_to_floor", floor_to_floor()], ["main_floor_depth", main_floor_depth()],
               ["grade", grade()], ["basement_ceiling", basement_ceiling()], ["slab_top", slab_top()],
               ["slab_t", slab_t()], ["base_t", base_t()], ["footing_top", footing_top()],
               ["footing_t", footing_t()], ["footing_w", footing_w()], ["sill", sill()],
               ["frost_bottom", frost_bottom()], ["icf_wall_t", icf_wall_t()], ["wall_t", wall_t()]]);
echo(stair = [["x", stair_x()], ["risers", stair_risers()], ["rise", stair_rise()], ["run", stair_run()],
              ["top_y", stair_top_y()], ["foot_y", stair_foot_y()]]);
echo(main_rooms = main_rooms());
echo(main_doors = main_doors());
echo(main_windows = main_windows());
echo(main_fixtures = main_fixtures());
echo(main_furniture = main_furniture());
echo(main_posts = main_posts());
echo(main_roof = main_roof());
echo(main_porch_steps = main_porch_steps());
echo(garage_steps = garage_steps());
echo(base_rooms = base_rooms());
echo(base_doors = base_doors());
echo(base_windows = basement_windows());
echo(base_fixtures = base_fixtures());
echo(base_furniture = base_furniture());
echo(theatre_seats = theatre_seats());
echo(basement_outline = basement_outline());
echo(bearing_lines = bearing_lines());
echo(deep_footings = deep_footings());
echo(pool = [["xy", pool_xy()], ["shell_t", shell_t()], ["shell_floor", shell_floor()], ["water", pool_water()],
             ["depth", pool_depth()], ["bottom", pool_bottom()], ["insul", pit_insul()]]);
echo(spa = [["xy", spa_xy()], ["rim", spa_rim()], ["water", spa_water()], ["depth", spa_depth()],
            ["bottom", spa_bottom()], ["spill_x", spill_x()]]);
echo(theatre = [["xy", theatre_xy()], ["pit_x", theatre_pit_x()], ["stage", theatre_stage()],
                ["tiers", theatre_tiers()], ["pit_bottom", theatre_pit_bottom()]]);
echo(frost_walls = frost_walls());
echo(piers = piers());
echo(exit_stair = [["door", exit_door()], ["rise", exit_rise()], ["risers", exit_risers()], ["run", exit_run()],
                   ["landing_x", exit_landing_x()], ["areaway", exit_areaway()], ["wall_t", exit_wall_t()],
                   ["top_pad", exit_top_pad()], ["footprint", exit_footprint()]]);
