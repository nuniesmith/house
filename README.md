# house

OpenSCAD models of the house, the shop and the site. Units are feet;
visualisation only, not construction documents.

The house was redesigned in November 2026. The new plans are
[`docs/house/main_floor.jpg`](docs/house/main_floor.jpg) and
[`docs/house/basement.jpg`](docs/house/basement.jpg). See
[`docs/house/Redesign-and-Spec-2026-11-02.md`](docs/house/Redesign-and-Spec-2026-11-02.md)
for:

- how the plans became the model, and what changed;
- the stair between the floors;
- the foundation;
- the concrete for the indoor pool and its hot tub;
- the stadium-tiered theater floor;
- the open questions.

![Both levels, cut east-west](docs/house/cutaway.png)

| File | What |
|---|---|
| `models/main_floor.scad` | Main level from `main_floor.jpg`: rooms, doors, windows, kitchen and bath fixtures, furniture, porches, hipped roof, the floor framing |
| `models/basement.scad` | Lower level from `basement.jpg`: music room, gym, theater, pool + spa + pool bath, pet room, living room, utility, laundry |
| `models/foundation.scad` | The concrete: ICF basement walls and footings, slab, theater tiers, pool + spa shells, frost walls, garage slab, porch piers, and the earth for sections |
| `models/house_combined.scad` | Everything together (it `use`s the files above): assembled, exploded, foundation and section views |
| `models/house_lib.scad` | Shared modules, the floor-to-floor height and the stair |
| `models/shop.scad` | The 100 × 100 ft 4-bay shop (v3: behind the house, front faces west, Bay 1 utilities southernmost) with pit, wash-bay drain and the Bay 1 utility rooms |
| `models/site.scad` | The whole property: house, shop, west shared driveway, front loop + garden, shop tree belt, well and septic zones. It also has the utility tunnel from Bay 1 to the basement; its landing needs re-planning for the new basement (spec §6) |
| `tools/check_layout.py` | Layout checker (needs `openscad` on `PATH`) |

Research and planning documents live in `docs/`:

- `docs/house/` has the plans, the redesign notes and spec, and the renders.
- `docs/House-Review-and-Research-2026-10-28.md` is the earlier house review
  and build research for Alberta.
- `docs/shop/` has the shop base plan (utility hub, tunnel, septic, build
  order, decision list) with its drawn plans and renders.

| | |
|---|---|
| ![Main floor](docs/house/main_floor_plan.png) | ![Basement](docs/house/basement_plan.png) |
| ![Section A](docs/house/section_a.png) | ![Section D: pool and spa](docs/house/section_d.png) |

## Options

Set them in the OpenSCAD Customizer or with `-D name=value`.

`house_combined.scad`:

- **`mode`**:
  - `assembled`: the house on its lot.
  - `exploded`: the main floor lifted off the basement; `explode_gap` sets
    the distance.
  - `basement_only`, `main_only`.
  - `foundation`: the concrete alone.
  - `section`: a vertical cut through everything, earth included.
- **`section`** (with `mode="section"`):
  - `A`: east-west through the stair, theater and pool.
  - `B`: along the stair.
  - `C`: through the theater.
  - `D`: through the pool and spa.
  - `custom`: set `cut_axis` (`x`/`y`) and `cut_at` yourself.

  Cut faces are drawn darker than the surfaces beyond them.
- **`show_roof`, `roof_opacity`, `roof_color`**: the roof (blue by
  default). `show_furniture`, and `show_ground` (the lawn in the assembled
  view).

`foundation.scad`:

- **`part`**: `all`, `basement` or `frost`.
- **`show_earth`**: draw the earth around it.

## Editing

Each floor is a set of tables at the top of its file. In
`models/main_floor.scad`:

- `main_rooms()`: `[label, x0, y0, x1, y1, ceiling, kind, ...]`
- `main_doors()`: `[x, y, axis, width, type, swing, ...]`
- `main_windows()`, `main_fixtures()`, `main_furniture()`

The coordinates:

- Both floors use the same frame, in feet. x runs east and y north; x = 0
  is the garage's west wall and y = 0 the front wall of the den and the
  breakfast bay.
- z = 0 is the main floor. The basement floor is `floor_to_floor()`
  (11.75 ft) below it.
- Every table format is described at the top of `models/house_lib.scad`.

After editing, run the checker:

```bash
python3 tools/check_layout.py
```

It checks:

- every door joins the rooms it should;
- every leaf swings clear of walls, fixtures and other leaves;
- every room is reachable;
- rooms neither overlap nor leave slivers between them.

Rendering from the command line (from `models/`), e.g. the main-floor plan
and section A:

```bash
openscad -o plan.png --imgsize=3600,2300 --projection=o \
  --camera=69,25.7,0,0,0,0,235 -D show_roof=false main_floor.scad
openscad -o section_a.png --imgsize=3000,1000 --projection=o \
  --camera=69,40,-3,90,0,0,190 -D 'mode="section"' -D 'section="A"' house_combined.scad
```

For sections B–D, look east with `--camera=<x>,25,-3,90,0,270,150`.
Sections take a minute or two each: every cut face is computed exactly.
