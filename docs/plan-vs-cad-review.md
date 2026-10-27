# Original plans vs the YAML / OpenSCAD model — review (2026-10-26)

The OpenSCAD models are generated from `config/floorplan.yaml`, so every
difference below is a difference between the original plans (the
architectural main-floor plan and the hand-drawn basement sketch, both in
`assets/`) and the YAML data — the CAD renders the YAML faithfully.
Fixing the YAML and re-running the generators fixes both the 2D plans
and the 3D models.

## Main floor

### Missing from the YAML entirely
- **Breakfast Nook** (14'-1" × 14'-9", 14' clg) and **Breakfast Porch**
  (13'-4" × 12'-4") — the whole breakfast area between Bedroom 2 and the
  kitchen is absent; the YAML kitchen absorbs the space.
- **Bar** (14'-6" × 9'-0", 14' clg) between Front Hall and Lounge.
- **Front Hall** (10'-2" × 12'-5", 14' clg) as a distinct room — the YAML
  only has the 3 ft bedroom corridor as "HALL".
- **Powder room (PWDR)** by the pantry.
- **Bath 3** and **Bath 2**, plus their walk-in closets (Bedroom 2's WIC
  and the Bath 2 WIC). The YAML has a single "BATH 4" for the whole wing.
- **Master Porch** (19'-2" × 10'-0", vaulted), **Office Porch**
  (11'-4" × 10'-8"), **Side Porch** (10'-0" × 32'-0") — of the original's
  six porch areas the YAML keeps only Front Porch and Outdoor Living.
- The **second master WIC** — the original has two (both 12' clg); the
  YAML has one.
- The **dining-room fireplace** — the original has two fireplaces
  (Dining Room west wall, Family Room east wall); the YAML has one, on
  the Family Room's south wall.

### Present but different
- **Mud Room**: YAML 15×12 vs original 11'-1" × 7'-5" (nearly double
  the area).
- **Laundry**: YAML puts it beside Bath 4; the original puts it up by
  Bedroom 2/3, next to Bath 2.
- **Family Room**: YAML 24×18 vs original 16'-6" × 15'-2".
- **Outdoor Living**: YAML 44 ft wide vs original 28'-2" × 15'-4".
- **Master Suite**: YAML 20×25 vs original 17'-8" × 22'-8".
- **Bedroom 4**: YAML 15×14 vs original 18'-1" × 13'-11".
- **Front Porch**: YAML 50×10 vs original 56'-8" × 12'-4".
- **Stairs**: the original's basement stairs sit in the left wing by the
  Mud Room; the YAML has a 4×10 "STAIR" alcove mid-plan at (57, 15).
- Close enough: Garage (25×32 vs 25'-2" × 31'-9"), Bedroom 2, Dining,
  Foyer, Lounge, Office.

### Ceiling heights (model assumption gap)
The original specifies ceilings throughout: 12' in the bedroom wing,
14' in the front rooms / office / bar / nook, and vaulted in the Family
Room, Master Suite, Outdoor Living and Master Porch. The YAML carries
no ceiling data, so the SCAD model uses a flat 9' everywhere. A
per-room `ceiling_ft` in the YAML (plus a `vaulted` flag) would let the
generator match.

## Basement (sketch vs YAML)

Matches: overall 100' × 60'; Home Theater 30×25 top-left; Pool/Hot Tub
25×35 bottom-left; Utilities 40×15 top-center; 12' ceilings.

- **Doors: the sketch shows five** (theater, pool, utilities, and two
  into the open area / exit side). The YAML basement has `doors: []` —
  so in the model every basement room is a sealed box.
- **Exit stairs**: the sketch draws a ~30' run attached at the top-right
  ("Stairs Exit outside", with a 20' lower segment). The YAML stretches
  a 10×60 container down the full right side with 40 steps.
- **Stairs UP**: sketch ~20×10 at the top, around x 52–77, with a door
  from Utilities. YAML has 20×15 at (70, 45) — shifted right and deeper.
- **Bar / Coffee / Sink**: a freestanding counter in the sketch's open
  area; the YAML makes it a walled 10×6 room inside the rec area.
- **Bottom band**: the sketch segments it 25 (pool) + 5 (strip) + 30
  (open) + 40 (block). The YAML merges the last two into one 60×20
  "STORAGE / REC", and leaves the 5 ft strip right of the pool
  unassigned (no room covers x 25–30, y 0–20).
- The sketch's big open area is one space; the YAML splits it into
  "OPEN REC AREA" + "STORAGE / REC" with a wall between — worth
  confirming which is intended.

## Suggested follow-up

A data-only PR that brings `config/floorplan.yaml` in line with the
originals: add the missing rooms/porches/baths, correct the sizes above,
add the basement doors, per-room ceiling heights, and the second
fireplace. Both generators (2D PNG and 3D SCAD) then re-render from the
same corrected data.
