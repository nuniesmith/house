# house

OpenSCAD models of the house. Units are feet; visualisation only, not
construction documents. See [REVIEW.md](REVIEW.md) for the plan and model
review and Kayla's notes.

![The house with its blue roof](docs/house_front.png)

| File | What |
|---|---|
| `main_floor.scad` | Main level — converted 2026-10-29 to plan 818030JSS (New American Ranch, 3,564 sq ft): rooms, doors, windows, fixtures, porches, hipped roof. See `docs/ranch-plan-818030.md` |
| `basement.scad` | Lower level from the hand-drawn sketch: theater, pool + hot tub + pool bath, utilities, rec room / library, music room, exit stair, foundation |
| `house_combined.scad` | Both levels stacked (`use`s the two files above) |
| `house_lib.scad` | Shared modules and the basement alignment |
| `shop.scad` | The 100 × 100 ft 4-bay shop (v3: behind the house, front faces west, Bay 1 utilities southernmost) with pit, wash-bay drain and the Bay 1 utility rooms |
| `site.scad` | The whole property: house + shop + the utility tunnel from Bay 1's south side into the basement UTILITIES room's north wall, west shared driveway, front loop + garden, shop tree belt, well and septic zones |
| `tools/check_layout.py` | Optional layout checker (needs `openscad` on `PATH`) |

Research and planning documents live in `docs/`: the house review and
build research in `docs/House-Review-and-Research-2026-10-28.md`, and
the shop base plan (utility hub, tunnel, septic, build order, decision
list) with its drawn plans and renders in `docs/shop/`.

## Options

Set them in the OpenSCAD Customizer or with `-D name=value`:

- `changes`: `true` shows the proposed changes from Kayla's review (new
  doors drawn green, kitchen work zone, central bedroom hall, master
  laundry, kitchen-to-dining hall, bigger shower, basement stair in the old
  bar, porches round the front corners, wider Bath 2);
  `false` shows the main floor as drawn. The basement has no as-drawn
  variant, so in `house_combined.scad` its stair rises into the as-drawn
  bar.
- `show_roof`, `roof_opacity`, `roof_color`: the roof (blue by default).
- `mode` (combined only): `assembled`, `exploded`, `basement_only` or
  `main_only`; `show_ground` draws the lawn at grade in the assembled view.

## Editing

Each floor is a set of tables at the top of its file, e.g. in
`main_floor.scad`:

- `main_rooms()`: `[label, x0, y0, x1, y1, ceiling, kind, ...]`
- `main_doors()`: `[x, y, axis, width, type, swing, ...]`
- `main_windows()`

x runs east and y north; on the main floor x = 0 is the garage's west wall
and y = 0 the front wall of the dining room and lounge. Every format is
described at the top of `house_lib.scad`. After editing, run the checker:

```bash
python3 tools/check_layout.py
```

Rendering from the command line, e.g. the main-floor plan:

```bash
openscad -o plan.png --imgsize=2000,1300 --viewall --autocenter \
  --projection=o --camera=0,0,0,0,0,0,0 -D show_roof=false main_floor.scad
```
