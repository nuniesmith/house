# Option G: Pinwheel hub (round 3)

> **Coordinator decision (11 Nov 2026): G stopped after two attempts; no plan was drawn.** This is a finding about the shape, not an unfinished drawing.
> - **The bedroom suite doesn't fit a pinwheel arm.** The suite alone (27 × 22 primary, ensuite, two walk-ins, bedroom 2, bath, laundry, a short hall) needs about 1,245 sq ft at centre lines. A pinwheel near 3,500 sq ft has four arms of about 22 × 36 ft (792 sq ft) around a 14 × 14 hub.
> - **Making it fit breaks the size target.** Unbalancing the arms to fit the suite pushes the block past about 64 × 66 ft, above the 3,650 ceiling.
> - **The central-hub idea continues as Option H,** where two wings meet at the hub.

Status: INCOMPLETE. No plan drawn. No SCAD, checker run, routes table, renders or PROS-CONS.md exist for G.

What was done:
- Read the brief, the round-2 F files, `routes.py`, `plan_facts.py` and `check_layout.py`.
- Worked the packing by hand and with a CP-SAT packer (`$RUN/work/OPT-G3/pack.py`, plus `core.py`, `probe.py`).
- Added the coordinator's 14-trip rule (living, dining and kitchen must each open onto the hub); no layout was tested against it.

Why it stopped (findings, not a plan):
1. Mud-room link. The mudroom has to touch both the garage and the hub, the pantry has to touch the kitchen and the garage, and the kitchen has to touch the hub. On a 58-64 ft block every arrangement tried put the kitchen between the mudroom and the hub, or needed a hub/hall 40+ ft long (circulation above 12%).
2. Depth. Stacking kitchen (22.4) + dining (19.4) in one column, with the bedroom wing (primary 22.4 deep) above it, gives a block depth of 65-70 ft. Side-by-side kitchen and dining gives a width of 64+ ft.
3. Program area. Rooms at the round-3 trims sum to about 2,800 sq ft (centre lines); the hub, stair, lift, halls and vestibule need about 600 more. That leaves about 150 sq ft of slack inside 3,650, which exact tiling cannot absorb.
4. Packer status. CP-SAT proved the set (primary NE corner + pantry beside the kitchen + mud and pantry on the garage wall + primary clear of the garage) infeasible as modelled. The cause was not isolated.

Suggested next step: relax one of (a) pantry or mud sharing a wall with the garage, (b) primary at the NE corner, (c) 58-64 ft depth. Then redraw from F's files.

## Second attempt (after the relaxations)

Status: still INCOMPLETE; nothing drawn. One hand layout on the coordinator's skeleton (hub 14 x 14 at 22.4..36.4; living SW; kitchen SE with dining north, both on the hub; library W; bedroom wing N; mud hall to a garage on the east) did not close.

What closed:
- Living, kitchen (door off the foyer) and dining (opening off the hub) each open onto the hub or foyer, so all 14 trips look feasible.
- Library at x 6.4..22.4, y 22.4..38.8 on the hub's west face.

What is left over:
- Bedroom wing. Primary 27.4 x 22.4 + ensuite 13.4 x 10.4 + two walk-ins (6.4 x 8.4) + bedroom 2 + bath + laundry + a short hall need about 1,235 sq ft. The N arm plus the W-arm area above the library gives about 1,290 at depth 23 (block 58.4 x 59.4), but they do not tile: the primary needs a 27.4-wide strip, and the strip beside the hall is 8.6 wide, which cannot hold the walk-ins and ensuite as well. Making room needs depth 66, which puts the footprint above 3,650.
- Mud hall to the hub. It was not routed. It would add a hall of about 100 sq ft along the north edge of the kitchen/dining arm.

Next step: put the bedroom wing in an east arm of its own and move the kitchen/dining to the south arm. That breaks the coordinator's skeleton, so it needs a decision.
