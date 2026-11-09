# Option B: the as-drawn sheet, with Kayla's notes applied

1. Takes the room arrangement from the architect's sheet `docs/house/floor_plan.JPEG` (kitchen and island in the north-centre, dining/foyer/study across the front, service cluster beside the garage), read from geometry and fixtures, not from the sheet's printed labels.
2. Applies Kayla's notes: garage doors south, Costco door, master laundry, no closets on exterior walls, 36 in doors, curbless showers, vestibule, powder room, library, broken (not open) concept.
3. Fixes CODE-01 with a two-flight stair (11 + landing + 11), same x, same basement foot; fixes STR-04 with a 585.7 m2 building area (14.3 m2 margin).
4. Result: Kayla PLAN items 109 IN / 52 MISSING / 3 CONTRADICTED (of 164); drain-run index worse (1,162 ft vs 879 ft); kitchen is the route between the two wings.
5. Start with `PROS-CONS.md`, then `plan_b.png` (phone-readable plan), `3d_b.png`, `stair_b.png`, `basement_plan_b.png`.

**Status: complete.** `check_layout.txt` shows OK for `main_floor_b.scad` and `basement_b.scad`. Facts are in `plan_facts_b.md` / `matrix_b.md` (variant mode, same method as Phase 0). Not done: `site.scad` is not edited, so the south apron and the meter move are described but not drawn. The matrix row "Min distance bedroom -> drive" still shows the current 9.3 ft for that reason (hand figure: at least 27.6 ft).

## How the sheet was read and calibrated

- Sheet: 8,736 x 5,891 px. Walls were detected on a 4x downsample (2,184 px wide) and checked against zoomed crops with a feet grid; rooms were identified by fixtures (island, sinks, tubs, toilets, stair, garage), not labels. The sheet's "Bedroom 60'4" x 43'8"" is the open kitchen + great room + lobe; its big "Patio" on the north is the great room's walled covered patio/deck; its "Dining Room" at the front is a front room beside the foyer.
- Fit (image to model feet, y flipped), from the shared envelope. A least-squares line per axis through 8 x-edges and 6 y-edges:
  - x: 15.23 px/ft (60.9 px/ft on the full image); x = 0.06568 px - 2.762; residual rms 0.41 ft, max 1.04 ft (great room west wall).
  - y: 15.10 px/ft (60.4 px/ft on the full image); y = 78.19 - 0.06623 px; residual rms 0.95 ft, max 1.37 ft (north deck wall).
- Control points (px at 2,184 wide -> model feet, residual): garage west wall 44 -> 0 (+0.13); master bath east wall 1993 -> 128.13 (+0.01); master bedroom east wall 1976 -> 126.97 (+0.05); front-porch west and east edges 794 / 1588 -> 49.24 / 101.41 (+0.15 / +0.13); great room east wall 1505 -> 95.63 (+0.45); great room west wall 1079 -> 69.14 (-1.04); garage south / north walls 1157 / 659 -> 1.25 / 35.46 (+0.31 / -0.92); master bath south wall 1056 -> 9.31 (-1.06); master bedroom north wall 393 -> 52.86 (-0.70); front-porch south edge 1396 -> -15.26 (+0.99); deck north wall 183 -> 64.7 (+1.37).
- The x fit is tight. The y residuals up to 1.4 ft are real differences between the sheet and the model envelope, not fit error: the sheet's garage is 32.8 ft deep to the model's 34.2 ft, and its front porch is deeper. Rooms were read from the sheet, then snapped to the model's wall lines (the shared envelope); the sheet's printed numbers were not used.
- Scratch work (tiles, wall masks, scripts): `$RUN/work/OPT-B/`.
