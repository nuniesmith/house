# 3D models

OpenSCAD models of the house, generated from `../config/floorplan.yaml`
by `../src/generate_scad.py` — edit the YAML, never these files.

| File | What |
|---|---|
| `main_floor.scad` / `.stl` | Main level only |
| `basement.scad` / `.stl` | Basement only (incl. the exit-stair tower) |
| `house_combined.scad` / `.stl` | Both levels stacked |
| `house_combined_exploded.stl` | Both levels, vertically separated |

Units are feet (1 unit = 1 ft). The models are dollhouse-style (no
roof) visualisation aids, **not** construction documents: shared walls
are doubled, and open-plan zones are fitted rectangles (see
`../docs/original-plan-data.md`).

## Combined model parameters

`house_combined.scad` takes a `mode` (OpenSCAD customizer / `-D`):

- `assembled` — basement under the main floor at its real position
- `exploded` — levels separated by `explode_gap` for inspection
- `basement_only`, `main_only`

The basement is modelled open-plan the way Jordan's sketch draws it
(only the theater, pool room and utilities are walled), and on the
main floor the kitchen, family room and bar are open to each other
(`open_edges` / `open_plan` in the YAML).

Floor-to-floor alignment is an assumption, recorded in the file header:
the foundation's south edge sits on the main floor's south wall line
and its east edge on the master suite's east wall, which puts the
exit-stair tower under the side porch. Under this alignment the
basement's UP flight lands under the family room, **not** under the
main floor's mud-room flight — the two source drawings disagree on the
stair, and which one governs is an open design question.

## Regenerating

```bash
python3 src/generate_scad.py          # SCAD files into models/
python3 src/generate_scad.py --stl    # plus binary STLs (needs openscad)
```

Renders of all levels live in `../output/` (`*_3d.png`).
