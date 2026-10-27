# house

OpenSCAD models of the house. Units are feet. Dollhouse-style
visualisation (no roof), not construction documents.

- `main_floor.scad` — main level: all rooms from the architectural
  plan, open-plan kitchen / family room / bar, columned front porch
  and four columned rear porches (breakfast, outdoor living,
  office, master) with yard steps
- `basement.scad` — lower level: open-plan rec floor with a walled
  theater, pool room and utilities, plus the exit-stair tower
- `house_combined.scad` — both levels stacked; set `mode` to
  `assembled`, `exploded`, `basement_only` or `main_only`

The combined model's floor-to-floor alignment is an assumption,
documented in its header.
