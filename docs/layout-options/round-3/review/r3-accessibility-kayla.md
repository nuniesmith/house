# R3-ACC: accessibility, flow and Kayla's notes, Option H (knuckle hub)

**Specialist:** R3-ACC (prefix ACC). **Date:** 2026-11-12. **Status:** complete. Read-only review.

**Inputs read:** `briefs/REVIEW-R3.md`, `ROUND3-BRIEF.md`, `COMMON-RULES.md`; H's `PROS-CONS.md`, `matrix_h.md`, `routes_h.md`, `main_floor_h.scad`, `basement_h.scad`, `plan_h.png`, `basement_plan_h.png`; the 164-item PLAN list (`findings/01-architecture-flow.md`); round-1 rulings (`kayla-rescore.md`); round-2 `r2-accessibility-kayla.md` and `kayla-rescore-r2.md` (D and F numbers reused, not re-reviewed).

**Re-measured:**
- `plan_facts.py` on H reproduces `matrix_h.md` (no diff).
- `check_layout.py` prints OK on both levels.
- `routes.py --extended` on H, D and F reproduces the designer's table (H 524 ft, D 653, F 850).
- Scratch scripts are in `work/R3-ACC/`: `routes_x.py`, `circ.py`, `maxc.py`, `los.py`, `doorfx.py`.

**Elevator wording (household note):** the lift is a planned future option. The stacked space is built now, the lift is installed later, and the stair stays as the backup. I assess the space as a future install (ACC-13).

## 0. Daily routes (the reason for round 3)

`routes.py` start point for "front door" is the **FOYER centre**, not the door. H's front door is in the vestibule, 11 to 14 ft further out. I therefore report two conventions. D has a vestibule too; F has none.

| Route | H (script, foyer centre) | H (from the vestibule, real door) | D (script) | F (script) |
|---|---|---|---|---|
| garage → kitchen | 31 | 31 (35 with the Costco door blocked, ACC-02) | 30 | 34 |
| garage → primary | 67 | 67 | 125 (KITCHEN, DINING, LIVING) | 144 (KITCHEN, DINING, LIVING) |
| front door → primary | 55 | 66 | 48 | 60 |
| front door → kitchen | 23 | 33 | 50 (LIVING, DINING) | 53 (LIVING, DINING) |
| front door → library | 33 | 43 | not on this floor | 80 (LIVING, DINING, KITCHEN) |
| primary → kitchen | 58 | 58 | 97 (LIVING, DINING) | 112 (LIVING, DINING) |
| bedroom 2 → kitchen | 49 | 49 | 73 (LIVING, DINING) | 101 (LIVING, DINING) |
| primary → laundry | 28 | 28 | 23 | 30 |
| lift → kitchen | 34 | 34 | 63 (LIVING, DINING) | 78 (LIVING, DINING) |
| lift → primary | 32 | 32 | 43 | 46 |
| front door → living | 19 | 20 | 14 | 19 |
| front door → dining | 18 | 28 | 32 (LIVING) | 38 (LIVING) |
| kitchen → living | 40 | 40 | 36 (DINING) | 34 (DINING) |
| dining → living | 37 | 37 | 19 | 20 |
| **First 10 (target ≤ 420)** | **409** (designer 410) | **441 (fails by 21 ft; 445 with the Costco door blocked)** | 552 | 738 |
| **All 14 (target ≤ 560)** | **524** | **567 (fails by 7 ft; 571 with the Costco door blocked)** | 653 | 850 |
| **Pass-throughs (14 trips)** | **0** | **0** | 13 | 16 |

Today's model (brief): 0 pass-throughs, 597 ft on 8 routes.

**By eye on `plan_h.png`:**
- **Would a person walk the script's routes?** Yes. Every route runs mudroom or pantry (utility), hub pieces and the 7 ft hall. Nobody crosses the living, dining, kitchen or library. 0 pass-throughs holds for the 14 trips. It also holds for 22 extra trips I added (`routes_H_x2.md`):
  - front door, garage, kitchen, library and primary to the powder room;
  - laundry, ensuite, bedroom 2 to shared bath;
  - lift → garage 42 ft;
  - garage → library 55 ft.
- **Does any daily trip cross a living room the script misses?**
  - The script's shortest path for garage → powder, garage → living, garage → dining and mudroom → dining goes through the kitchen via the pantry door. That is a shortcut, not a forced crossing. Without the pantry and Costco doors the hub route is 60 / 70 / 66 / 43 ft: same for powder and living, +20 ft for dining, +8 ft for mudroom → dining. So 0 forced pass-throughs.
  - Any route that uses the Costco door at (83, 37) is physically blocked by a shelf bank (ACC-02). The script ignores fixtures. Real garage → kitchen goes through the mudroom: 35 ft, not 31.
- **Linear check:**
  - The south face is living, hub and dining over 57 ft (x 28 to 85). That is not three living rooms in a row: the kitchen is stacked north of the dining room, the library north of the living room, and each opens to the hub by a 4 to 8 ft cased opening.
  - The hub itself is a 41 ft north-south spine of 8 hall-kind pieces (x 50 to 66, y 7.4 to 48.4). It works as a connector, but it is a long gallery rather than a compact room. The designer's own full count is 15.6% circulation against the 12% target.

## 1. Kayla re-score (164 PLAN items), independent

| | Today | D (indep.) | F (indep.) | **H designer** | **H mine** |
|---|---|---|---|---|---|
| IN | 62 | 101 | 84 | 95 | **80** |
| MISSING | 89 | 60 | 73 | 67 | **82** |
| CONTRADICTED | 13 | 3 | 7 | 2 | **2** |
| Deal-breakers met (of 12) | 5 | 10 | 8 | 11 | **10** |

Mine: 80 IN, 82 MISSING, 2 CONTRADICTED. The two CONTRADICTED are K-074 (ensuite tub on a W/S exterior corner) and K-104 (hall sight line ends at the primary and bedroom 2 doors).

Deal-breakers where I differ: **K-037 and K-115** (Costco door), IN → MISSING on the drawing only (ACC-02). It flips back to IN if the shelf is shortened, which gives 11 of 12. K-036 stays MISSING, as the designer says.

Per-item verdicts are in `work/R3-ACC/rescore.json` (`{"H": {"K-001": ...}}`, all 164).

### Items where I differ from the designer (21)

| K-ID | Designer | Mine | Evidence |
|---|---|---|---|
| K-004 | IN | MISSING | Largest clear circle (walls and fixtures only): powder 4.81 ft (1,466 mm); laundry 5.40 ft (1,646 mm) against 5.58 ft. Designer says 7 of 7; I measure 5 of 7 (see ACC-03). Same standard as round 2 (D basement bath 5.40 ft and F powder were MISSING). |
| K-008 | IN | MISSING | LAUNDRY (x 66 to 75.5) shares an 8.5 ft wall with BEDROOM 2 (x 62.5 to 74.5) at y 48.4. Round 1 scored the current model's laundry-against-bedroom-2 wall MISSING. |
| K-012 | IN | MISSING | Round-1 ruling on C and round-2 on D, E and F: living spaces south but no south backyard = MISSING. H's south side is the road side: front porch, 12 x 10 patio on the east, drive on the east. |
| K-014 | IN | MISSING | Primary has N and W windows only. Bedroom 2's east window (x 74.5, y 52 to 56) looks at the garage west wall 4.1 ft away (outside faces x 74.7 and 78.8). No sunroom. |
| K-031 | IN | MISSING | The library opens to the hub by a 4 ft cased opening `[50,28,y,4,"full"]`: no door and no partition. The brief asks for a closable partition. |
| K-037 | IN | MISSING | Costco door `[83,37,x,3]` is blocked: the 7 ft tall shelf `[80.4,36.2,90.8,36.8]` spans the whole door width (x 83 to 86) (ACC-02). |
| K-100 | IN | MISSING | Designer cites a "primary east door": none is drawn (deck door is west). Primary N/W only; basement bedroom 3 south only. Same ruling as round 2's basement bedroom with no east light. |
| K-114 | IN | MISSING | Pantry fixtures are shelves on 3 walls plus a freezer; no counter for small appliances. Same call as round-2 E and F. |
| K-115 | IN | MISSING | Same blocked door as K-037. |
| K-128 | IN | MISSING | 72 in table `[68,3,74,9]` has its west edge 1.8 ft from the hub wall (x 66.2). Round 2 used about 3 ft push-back clearance (F: 0.5 ft = MISSING). |
| K-141 | IN | MISSING | The only guest coat storage is `[50.2,2,50.8,6.6]`: 0.6 ft (7 in) deep. That is shelving, not a hanging closet. |
| K-142 | IN | MISSING | Same unit. |
| K-144 | IN | MISSING | Offset inner door hides the living room only from the vestibule (41 of 440 sf of living seen from the door). From the foyer centre, 260 of 440 sf of living (59%) and 164 of 266 sf of dining are in view; from just inside the inner door, 212 of 440 sf of living. Round 2 called 81% of D's living in view MISSING. |
| K-151 | IN | MISSING | Mudroom has lockers `[68.4,39.7,77.6,40.3]` and a bench only; no shelf or counter drop surface. Same as round-2 F. |
| K-211 | IN | MISSING | Ensuite wet zone 7.0 x 3.8 ft holds a 4.6 x 2.6 ft tub, leaving a shower floor of about 2.4 x 3.8 ft (29 x 46 in). Not a "large" shower (ACC-07). |
| K-262 | IN | MISSING | Fridge visible from the foyer; island visible from x 54.5 inward; 72 of 330 sf of kitchen in view from the foyer centre. Partial = MISSING. |
| K-298 | IN | MISSING | Powder door `[62,7.4,x,3]` opens straight into the foyer (the entryway), 8 ft from the inner door, with no storage between. Same ruling as round-2 D and F. |
| K-315 | IN | MISSING | Same blocked Costco door as K-037. |
| K-077 | MISSING | IN | Designer says living S and N windows are partly opposite. Coordinates: S x 34 to 46, N x 29 to 33: no overlap. No other room has windows on opposite walls. |
| K-106 | MISSING | IN | Island 3.4 x 8 ft = 27 sf, the same size as D (8 x 3.5) and F (3 x 9.4), both scored IN. |
| K-288 | MISSING | IN | Dishwasher `[85.8,23.4,87.8,26]` is 1.0 ft from the sink basin (y 18.4 to 22.4), on one continuous counter run. Designer says 2 ft. D and F scored IN. |

### Designer evidence that does not match the drawing (verdict unchanged unless listed above)

| K-ID | Designer's text | Measured |
|---|---|---|
| K-002 | basement 2,728 sf | 2,551 sf (matrix) |
| K-003 | 15 of 15 single doors, hall 6 ft | 16 single swing and 2 doubles (matrix); bedroom hall 7 ft wall to wall |
| K-006 | 9 wet-wall groups in 4 clusters | 10 groups (matrix) |
| K-069 | 18 corners (11 out, 7 in) | 22 corners (13 out, 9 in) |
| K-013 | primary y 46 to 68 | y 48.4 to 70.4 |
| K-261 | sink to range 15 ft | about 19 ft, centre to centre |
| K-274 | 54 in aisle on the dishwasher side | 10.4 ft between island and dishwasher (fine, but not a 4.5 ft aisle) |
| K-238 | bedroom 2 is 12 x 14 | 12 x 12 centre line (11.6 x 11.6 clear) |
| K-200 | walk-ins 6 x 12 | 2 x (6 x 12) = 144 sf, 48 sf over her 6 x 8 |

## 2. Findings

| # | Severity | Option | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| ACC-01 | Should fix | H | Routes | Measured from the real front door (vestibule), H misses both route ceilings: 441 ft on the first 10 (limit 420) and 567 ft on all 14 (limit 560). The script and PROS-CONS (410 / 524) start at the foyer centre, 11 to 14 ft inside the house. 0 pass-throughs is unaffected. D is 569 / 683 and F 738 / 850 on the same basis, so H is still far the shortest. | `routes_x.py` with front door = VESTIBULE: front door → primary 66, kitchen 33, library 43, living 20, dining 28 (foyer-centre values 55 / 23 / 33 / 19 / 18). Trimming ~25 ft needs the library or kitchen door nearer the vestibule, or a shorter spine (bedroom hall is 15.4 ft against ≤ 15). | brief hard target 2 | $ (door/wall moves) |
| ACC-02 | Should fix | H | Pantry, Costco door (83, 37) | The door is drawn but a 7 ft tall shelf bank `[80.4,36.2,90.8,36.8,0,7]` runs the full width of the opening (x 83 to 86). On the drawing there is no usable Costco door, so K-037 / K-115 / K-315 (a deal-breaker pair) are MISSING. The garage → pantry → kitchen walk that the PROS-CONS quotes as 31 ft actually goes through the mudroom (35 ft). Fix: shorten the shelf to x 80.4 to 82.8 and move the freezer east. | `doorfx.py` door/fixture overlap check; `main_floor_h.scad` pantry fixtures. Restoring it gives 11 of 12 deal-breakers. | — | $ (drawing only) |
| ACC-03 | Should fix | H | Powder, laundry | Two of the seven required 1,700 mm turning circles do not exist. Powder (6.0 x 7.0 ft clear): largest clear circle 4.81 ft (1,466 mm); the drawn circle overlaps the toilet and the vanity. Laundry (9.1 x 7.5 ft clear): 5.40 ft (1,646 mm), 0.18 ft short, and the door leaf swings into it. The shared-bath circle is drawn over the toilet but a clear 6.4 ft circle exists; kitchen 10.4 ft, ensuite 6.4 ft, foyer 6.6 ft, vestibule 7.0 ft, basement bath 5.8 ft all pass. Fix: merge the powder into the shared bath (the brief allows it) or rework it to one fixture wall; cut the laundry counter depth or widen the room 0.2 ft and swing the door out. | `maxc.py` (walls and fixtures over 0.1 ft tall as obstacles, door leaves excluded); `main_floor_h.scad` powder and laundry fixtures. Round 2 held the same line for D's basement bath (5.40 ft) and F's powder. | ABC 2023 3.8.4.2.(4), p.318 | $ |
| ACC-04 | Should fix | H | Hub daylight | The hub is lit by a glazed 42 in front door and a 3 ft sidelight, both in the vestibule. The clerestory is a roof-table block only: raised roof `[52,9,64,26]` eave 11.5 ft, but every hub room is drawn with a 10 ft ceiling and there is no window row for it. The foyer and hub pieces (112 + 85 + 66 + 64 + 18 sf) and the 108 sf bedroom hall have 0 window rows. The hub centre is at least 22 ft from any exterior wall (south wall, living north wall, library west wall). The clerestory also stops at y 26, so the stair-top landing and bedroom hall get none. As drawn, the spine reads dark. | `main_windows()` (only `[50.8,0]` serves the entry); `main_roof()` last row; matrix hub-daylight cell ("stated here and in the roof table, not drawn"). Brief target 5: "stated on the plan". | — | $$ (raised roof, vaulted ceiling, glazing: unknown, needs a quote) |
| ACC-05 | Should fix | H | Entry sight lines | The offset inner door hides the living room from the vestibule only. One step inside, the foyer opens to the living room (5 ft opening), dining (4 ft) and kitchen (4 ft). From the foyer centre: living 260 / 440 sf, dining 164 / 266, kitchen 72 / 330 (fridge in view; island from x ≤ 54.5). The powder door opens into the same foyer. This is the round-1 C / round-2 D standard (K-144 and K-262 MISSING). The hall sight line ends at the primary and bedroom 2 doors (K-104 CONTRADICTED). | `los.py` (closed doors, cased openings open). | — | $ (swing doors or glazed screens at the openings) |
| ACC-06 | Should fix | H | East light | Primary has N and W windows only; basement bedroom 3 has a south window only; bedroom 2's "east light" window looks at the garage wall 4.1 ft away (garage roof overhang 1.0 ft, quiet-wing overhang 1.5 ft). Brief asks for the primary north or north-east and bedroom 2 east light (K-013 / K-014 / K-100). | windows `[34.5,50]`, `[34.5,62.5]`, `[38,70.4]`, `[57.5,70.4]`; `[74.5,52]`; basement `[71,0]`. | — | $ |
| ACC-07 | Should fix | H | Ensuite and basement bath | Ensuite: the 7.0 x 3.8 ft curbless wet zone holds a 4.6 x 2.6 ft tub; the free shower floor is about 2.4 x 3.8 ft. The brief asks for a screened curbless tub plus shower zone or a shower ≥ 60 x 48 in with a bench; no WC room is drawn (the WC stands open at x 36.2 to 37.8 against a ≥ 48 x 72 in room). Basement bath: the shower pad `[68.4,24,73.6,26]` is 5.2 x 2.0 ft (24 in deep). Shared bath pad 4.8 x 3.4 ft is adequate. | fixture rows in both scad files; K-211, K-226, K-227 MISSING. | — | $ |
| ACC-08 | Should fix | H | Library | No closable partition between the desk and reading halves and no door to the hub. Both windows are on the west wall (y 22 to 25.5 and 29 to 32.5), where the brief asks for a window per half. K-031 MISSING. Clear size 14.6 x 15.6 ft (228 sf) against her 15 x 16 (240 sf). | `main_doors()` `[50,28,y,4,"full"]`; `main_windows()`; room row `[35,20.4,50,36.4]`. | — | $ |
| ACC-09 | Should fix | H | Step-free routes | Garage entry: the garage slab is "at house level" but the front porch has four 6 in risers, so the finished floor sits about 2 ft above front grade, while the drive is drawn "level to garage doors". The plan does not say where the 2 ft is taken up. The front door has 4 steps and no ramp, so the only step-free entry is through the garage. The primary deck and patio doors are flush with the floor, but no steps or ramp to grade are drawn. Needs a stated grade or fill and a ramp or walk to grade (CS item 5 covers the garage slab). | `main_porch_steps()` `[55,-8,"-y",4]`; `main_floor_depth()` 1.625 ft; drive row z 0. | ABC 2023 3.8.4.2.(3), p.318 (benchmark for a dwelling unit, not a stated requirement for this house) | $$ |
| ACC-10 | Consider | H | Program sizes | Clear sizes (centre lines minus 0.4 ft): library 14.6 x 15.6 (228 sf, her 240), kitchen 21.6 x 14.6 (315 sf, her 330), bedroom 2 11.6 x 11.6 (135 sf, brief 144), laundry 9.1 x 7.5 (68 sf, brief 72), dining 18.6 x 13.6 (253 sf, brief 266). The kept rooms (library, kitchen) are 5% under her sizes. Over: walk-ins 2 x (6 x 12) = 144 sf against 96, mudroom 150 sf against 80, ensuite 144 sf centre-line against 130. | §3 table; `main_rooms()`. | — | $ (about 0.4 ft added to each kept room) |
| ACC-11 | Consider | H | Storage details | Pantry has no counter (K-114). Mudroom has no drop surface (K-151). Vestibule coat unit is 0.6 ft (7 in) deep and the long mudroom locker wall is also 0.6 ft deep; only the 1.2 ft block is a closet depth (K-141 / K-142 MISSING). | fixture rows `[50.2,2,50.8,6.6]`, `[68.4,39.7,77.6,40.3]`. | — | $ |
| ACC-12 | Consider | H | Dining | Round table's west edge is 1.8 ft from the hub wall; the coffee counter `[83.4,8,84.8,13.6]` reaches 1 ft into the swing of the 6 ft patio double door (door y 3 to 9). | fixtures; `main_doors()` `[85,3,y,6]`. | — | $ |
| ACC-13 | Consider | H | Elevator, future install | **Space is ready for a later lift.** Main and basement stops are both x 53 to 59, y 33 to 40 (offset 0.0 ft), 6 x 7 ft, 18 ft from the nearest exterior wall (rule 4 ft), with a 3 ft door onto the bedroom hall and a 7 x 7 ft clear approach on both levels (hall x 59 to 66). The stair is straight, 19 risers, 5.4 ft wall to wall, with a 6.6 ft top landing and a 10.45 ft foot landing, so it works as the backup. **Gaps:** (1) the brief puts the lift off the hub; H puts it on the bedroom hall, 11 ft north of the hub opening (the hub-to-hall opening is 4 ft wide). (2) The main-floor 6 x 7 ft space is a closet today, so the floor framing under it has to be laid out so the shaft opening can be cut later (no bearing line through it), and the pit needs a dig in the basement slab: both are items for a licensed Alberta engineer. (3) The basement lift door and the bedroom hall are lined up for the stack, but nothing on the plan marks the basement slab recess. Routes: lift → kitchen 34 ft, lift → garage 42 ft, lift → primary 32 ft, with 0 pass-throughs. | `matrix_h.md`; `main_floor_h.scad` `[53,33,59,40]`; `basement_h.scad` `[53,33,59,40]`; `main_doors()` `[59,34,y,3]`; `routes_x.py`. | — | $$ now (framing), lift itself: no repo price, needs a quote |
| ACC-14 | Consider | H | Door clear width | All swing doors are 3.0 ft (36 in) nominal; none are under 36 in on either level, which meets the brief. The benchmark asks for 850 mm clear with the door open; a 36 in leaf normally gives less than that unless swing-clear hinges are specified. | `main_doors()`, `base_doors()` widths. | ABC 2023 3.8.4.2.(8), p.318 (benchmark) | $ |
| ACC-15 | Consider | H | Quiet wing | Bedroom hall 15.4 ft (brief 15 ft or less). Primary and bedroom 2 doors are 1 ft apart at the hall end. Laundry shares an 8.5 ft wall with bedroom 2 and is 28 ft from the primary bed, with no link to a walk-in (K-036, K-158, K-166, K-203 MISSING). Night walk bed → ensuite WC is about 27 ft through one door. | `main_doors()` `[59,48.4]`, `[63,48.4]`; matrix "Master bed → laundry 27.8 ft". | — | $ |
| ACC-16 | Consider | H | Basement bedrooms | Bedrooms 3 (12 x 13) and 4 (14 x 10.6) have no closet drawn; the brief asks for "+ closet". Basement bedrooms do not share walls with the rec room, and there is no theatre or gym. East hall to the bedrooms is 14 x 5.4 ft (5.0 ft clear, exactly at the target). | `base_rooms()`; no closet-kind rows. | — | $ |
| ACC-17 | Consider | H | Stair opening | The stair opening's east edge (x 55.4, y 14.4 to 26.4) adjoins an open hub piece. No guard or screen is drawn. Refer to R3-CODE for the guard rule. | `main_rooms()` stairwell row. | — | $ |

## 3. Accessibility audit

| Item | H (measured) | D / F (round 2) |
|---|---|---|
| 1,700 mm circles, clear of fixtures | **5 of 7**: kitchen 10.4 ft, foyer 6.6, vestibule 7.0, shared bath 6.4, ensuite 6.4, basement bath 5.8; **powder 4.81 and laundry 5.40 fail** | D 5 of 5 main, basement bath 5.40 fails; F powder fails |
| Step-free garage → house | slab at house level, 3 ft door to the mudroom (and a blocked Costco door); grade unstated (ACC-09) | not re-reviewed |
| Step-free house → deck | primary deck door flush, no steps to grade | — |
| Front entry | 4 risers, no ramp | — |
| Door widths | all swing 3.0 ft; main 16 single and 2 doubles, basement 9 single | D three 2.8 ft doors; F one 2.8 ft basement door |
| Hall clear width | min 5.6 ft (matrix); bedroom hall 7 ft; basement east hall 5.0 ft | D 5.6, F 5.0 |
| Curbless showers | ensuite (small), shared bath (4.8 x 3.4), basement bath (2 ft deep) | D and F: sound |
| Elevator (future) | stacked, offset 0.0 ft, 6 x 7, approach 7 x 7 on both levels, off the bedroom hall not the hub | F approach exactly 5.0 ft with the door leaf inside it |
| Hub daylight | sidelight and glazed door; clerestory not drawn | — |
| Stair | straight, 19 risers, 5.4 ft wall to wall (about 4.9 ft clear), landings 6.6 ft top and 10.45 ft foot | D 4.2 ft clear |
| Depth ≤ 40 ft | south wing 29 ft, quiet wing 37 ft; whole footprint 66.0 x 71.4 ft | — |
| Noise | 0 bedrooms share a wall with a living room; garage 4.1 ft from bedroom 2's east window; drive 37.1 ft from the primary; laundry against bedroom 2 | — |

## 4. Comparison table

| Criterion | H | D | F | Today |
|---|---|---|---|---|
| Pass-throughs, 14 trips (script) | **0** | 13 | 16 | 0 (8 routes) |
| Walk, first 10 / all 14, ft (script) | **409 / 524** | 552 / 653 | 738 / 850 | 597 (8 routes) |
| Same from the real front door | **441 / 567** | 569 / 683 | 738 / 850 | n/a |
| Kayla re-score IN / MISSING / CONTRADICTED | **80 / 82 / 2** | 101 / 60 / 3 | 84 / 73 / 7 | 62 / 89 / 13 |
| Deal-breakers met (of 12) | **10** (11 if the Costco shelf is shortened) | 10 | 8 | 5 |
| Designer self-score | 95 / 67 / 2, 11 of 12 | 109 / 52 / 3 | 108 / 56 / 0 | n/a |
| Heated main footprint, outside face, sq ft | 3,571 | 2,934 | 3,910 | 5,685 |
| 1,700 mm circles clear | 5 of 7 | 5 of 6 | powder fails | none shown |
| Hall min clear, ft | 5.6 | 5.6 | 5.0 | — |
| Closets on exterior walls | 0 of 4 | 3 of 5 | 4 of 6 | — |
| Hub daylight | sidelight only drawn | n/a | n/a | — |

## 5. Flow and daylight, daily paths

| Path | Length | Doors and notes |
|---|---|---|
| Garage → kitchen with groceries | 35 ft (31 if the Costco door is cleared) | mudroom door, pantry door, pantry-to-kitchen door; no steps; pantry lane clear beside the freezer |
| Primary bed → toilet at night | about 27 ft | one door (ensuite, x 35 to 38); WC open in the ensuite |
| Primary bed → laundry | 28 ft | bedroom door and hall; no walk-in link |
| Entry → powder | about 14 ft | inner door, 8 ft to the powder door; opens onto the foyer |
| Kitchen → dining | 17 ft | direct 8 ft opening (K-035 IN) |

- Every bedroom, living room, kitchen, dining room and library has an exterior wall with a window.
- Windows on 2 or more walls: living (3), dining (2), bedroom 2 (2), primary (2), ensuite (2). One wall only: kitchen, library.

## 6. Program check (clear sizes; brief = round-3 size, hers = Kayla's)

| Room | Hers | Brief | H clear | Status |
|---|---|---|---|---|
| Library | 15 x 16 | 15 x 16 | 14.6 x 15.6 | under 5% (kept room) |
| Primary | 27 x 22 | 27 x 22 | 27.6 x 21.6 | in range |
| Kitchen | 15 x 22 | 15 x 22 | 14.6 x 21.6 | under 5% (kept room) |
| Pantry | 12 x 8 | 12 x 8 | 11.6 x 7.6 | in range |
| Dining + nook | 14 x 22 | 14 x 19 | 13.6 x 18.6 | under 5% |
| Living | 24 x 20 | 22 x 20 | 21.6 x 20.0 | in range |
| Ensuite | 16 x 10 | 13 x 10 | 11.6 x 11.6 | in range; no WC room |
| Walk-ins | 2 x (6 x 8) | 2 x (6 x 8) | 2 x (5.6 x 12) | over |
| Laundry | 9 x 10 | 8 x 9 | 9.1 x 7.5 | under |
| Bedroom 2 | 12 x 14 | 12 x 12 + closet | 11.6 x 11.6 | under (no closet room) |
| Shared bath | 8 x 8 | 8 x 8 | 8.6 x 8.0 | in range |
| Powder | 6 x 7 | 5 x 7 | 6.0 x 7.0 | over, fails circle |
| Mudroom | 9 x 12 | 8 x 10 | 12.6 x 11.1 | over |
| Elevator | 6 x 7 | 6 x 7 | 6 x 7 | in range |

## 7. Verdict (3 lines)

1. H does what round 3 asked on routes: 0 pass-throughs on 14 trips, 524 ft by the brief's method against D's 653 and F's 850. Measured from the actual front door it is 441 / 567 ft and just misses both ceilings (ACC-01).
2. On Kayla's notes H is better than F and the same as D (80 / 82 / 2 against D 101 / 60 / 3 and F 84 / 73 / 7), with no CONTRADICTED deal-breaker. The weak points are a blocked Costco door, the powder and laundry turning circles, the undrawn clerestory and the sight lines from the foyer.
3. Fixes are mostly drawing-level: shorten one shelf, redo the powder and laundry, draw the clerestory with a vaulted ceiling, add a door or screen to the library, and state the garage grade. No change to the hub layout is needed.

## plan_facts corrections

- The brief cites the turning-diameter rule as ABC 3.8.4.3.(4). On p.318 it is printed as 3.8.4.2.(4) ("General Accessibility"); 3.8.4.3 starts further down the same page ("Bathrooms").
- `routes.py` "front door" is the FOYER room centre, not the exterior door. For H this understates the front-door routes by 10 to 11 ft each.
- H `PROS-CONS.md` quotes 1,700 mm circles as 7 of 7; I measure 5 of 7.

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| ACC-03 | `search.py --doc abc_2023 '"unobstructed turning diameter"'` | abc_2023 | 318 | 3.8.4.2.(4) | shall be designed with an unobstructed turning diameter of not less than 1 700 mm |
| ACC-09 | `search.py --doc abc_2023 '"ancillary space serving"'` | abc_2023 | 318 | 3.8.4.2.(3) | A barrier-free path of travel shall be provided between the interior living space of the dwelling unit and any ancillary space serving it |
| ACC-14 | `search.py --doc abc_2023 '"850 mm when the door is in the open"'` | abc_2023 | 318 | 3.8.4.2.(8) | Every doorway within the dwelling unit shall have a clear width not less than 850 mm when the door is in the open position |
