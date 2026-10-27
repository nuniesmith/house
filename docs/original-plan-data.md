# Original-plan data pass — 2026-10-27

`config/floorplan.yaml` was rewritten from the two source plans in
`assets/` (the architectural main-floor plan and the hand-drawn basement
sketch), resolving the gaps listed in `docs/plan-vs-cad-review.md`.
Both generators (2D matplotlib and OpenSCAD) render from this data.

## What changed

**Main floor**
- Added: Breakfast Nook, Breakfast Porch, Bar, Front Hall, powder room,
  Bath 2, Bath 3, both bedroom-wing WICs, the Bath 4 WIC, Office Porch,
  Master Porch, Side Porch, and the second master WIC.
- Added the dining-room fireplace; the family-room fireplace moved to
  the east wall, as drawn.
- The basement stairs moved to the left wing by the mud room, where the
  original plan puts them (the old data had a mid-plan alcove that
  matched nothing below).
- Enclosed-room rectangles now use the dimensions printed on the plan
  (`dimension_text` quotes them verbatim): mud room 11'-1" × 7'-5",
  family room 16'-6" × 15'-2", outdoor living frontage 28'-2", etc.
- Every room carries `ceiling_ft` from the plan's ceiling notes (12'
  bedroom wing, 14' front rooms / office / bar / nook, 9'-8" garage),
  and `vaulted: true` where the plan says VAULTED CLG (family room,
  master suite, outdoor living, master porch). The OpenSCAD generator
  models vaulted rooms 4 ft above their eave height; porches get a 3 ft
  railing.

**Basement**
- The sketch's five doors are defined (plus a corridor door); the old
  data had `doors: []`, which sealed every room in 3D.
- The exit stairs are the sketch's attached tower **outside** the east
  foundation wall (x 100–110, y 20–60), not a full-height strip inside
  the 100' width. The new `foundation:` block records the true
  100 × 60 ICF footprint, and the OpenSCAD shell is drawn from it.
- Stairs UP moved to (52, 35), 20 × 10, below the utilities wall —
  landing under the main floor's left-wing flight.
- The bar is a freestanding counter (`furniture`), as sketched, labelled
  "BAR / COFFEE / SINK".
- The bottom band follows the sketch's segments: pool 25' + 5' hall
  strip + open floor + the ~54' storage/rec block.

## Conventions and known compromises

- Rectangles are **schematic**. Enclosed rooms match their printed
  dimensions; open-plan zones (kitchen, family room, front hall, entry
  hall) are fitted between neighbours, so a zone rectangle can differ
  slightly from its printed clear dimension. The outdoor-living
  rectangle ends where the office porch begins; its printed 28'-2"
  dimension spans the combined frontage.
- Doors use one convention everywhere: `direction: up/down` = the
  opening sits in a horizontal wall and spans x; `left/right` = a
  vertical wall, spans y. (The 2D door-swing symbols remain approximate;
  the OpenSCAD cuts are exact to this convention.)
- `Room` gained `ceiling_ft` / `vaulted` fields (defaults 0 / false, so
  old data still loads); the 2D generator ignores them, the OpenSCAD
  generator uses them.
- Still not modelled: window/door sizes beyond the plan's obvious
  openings, the kitchen island and appliances, plumbing fixtures, and
  the exact L-shapes of the master suite and laundry cluster (both are
  single rectangles here).

## Combined two-level model (2026-10-27)

`models/house_combined.scad` stacks both levels in one file (the SCAD
code and STL exports now live in `models/`; renders stay in `output/`).
Its `mode` parameter switches assembled / exploded / single-level
views. The floor-to-floor alignment is an **assumption**: foundation
south edge on the main floor's south wall line (the foundation's 60 ft
depth then lands within a foot of the main floor's north wall line),
east edge on the master suite's east wall so the exit-stair tower sits
under the side porch.

One open question the combined model makes visible: under this
alignment the basement's UP flight (from the sketch) lands under the
family room, while the main plan's DN flight is by the mud room. The
two source drawings place their stairs in different spots; resolving
which stair governs is a design decision, not a data fix.

Fidelity pass (later the same day, at Jordan's word): the basement is
now modelled the way the sketch is drawn — one open floor. Only the
theater, pool room and utilities are walled; the rec area, storage
zone and pool deck are `open_plan` floor plates, and the junction and
storage doors came out. On the main floor, the kitchen / family room /
bar are open to each other via `open_edges` (no phantom walls in 3D),
and the kitchen island is in as furniture.
