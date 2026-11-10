# Layout options, round 2: a main floor under 3,000 sq ft (binding for options D, E, F)

`RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`

## Why round 2

Round 1's options A/B/C all kept the ~5,400–5,500 sq ft heated main floor. Jordan and Kayla's direction (2026-11-10):
- Those are **too big**. Option C's deep rectangle would also be **dark in the centre**.
- **Keep the heated main-floor footprint, excluding the garage, under 3,000 sq ft.**
- Keep the **primary suite and one more bedroom upstairs**. Move the other bedrooms and the flex rooms to the **basement**.
- Plan for **accessibility**: a stacked space for a future **residential elevator**, and a **straight stair** that can take a heavy-duty stair lift in the meantime.
- **No pool in the basement.** A covered, seasonal outdoor pool and a hot-tub sunroom are being considered instead.

Every number in your work is measured the same way as rounds 0–1: `python3 $RUN/scripts/plan_facts.py --main <main scad> --basement <basement scad> --out <dir>`. It now also reports **"Heated main-floor footprint excl. garage, outside face"** (the target row) and **"Basement footprint, outside face"**. For reference, today's model is 5,685 sq ft and 3,617 sq ft.

## Hard targets (every option)

1. **Heated main-floor footprint, outside face, excluding the garage: ≤ 3,000 sq ft.** Aim for 2,700–2,950, so there's margin for real wall thicknesses.
2. **Building depth ≤ 40 ft wherever there are living rooms.** Every bedroom, living room, kitchen, dining room and office has an exterior wall with a window (Kayla K-097/K-098: deep, square plans are dark). Living spaces get windows on 2 walls where possible (K-064).
3. **The basement sits under the heated main floor.** Same outline or smaller. It doesn't extend under the garage or the porches.
4. **Stair: one straight flight with no landing**, which is legal only if floor-to-floor ≤ 3.7 m (ABC 9.8.3.3.(1), abc_2023 p.852).
   - Use **floor_to_floor = 11.75 ft**, which gives a 10 ft basement ceiling. `models/house_lib.scad:102-106` documents this: 19 risers of 7.42", 3.58 m.
   - Clear width **≥ 42 in** (room for a stair-lift rail).
   - A level landing at the top and at the bottom.
5. **Elevator (future):** a **6 × 7 ft** space, including the shaft walls, stacked on both floors.
   - The same x/y on both levels (within 0.1 ft), ideally near the garage/mudroom entry and the primary suite.
   - Framed for now as a **closet with a door** (kind `closet`, label `ELEVATOR (FUTURE)`), so the layout checker sees it as reachable.
   - In front of it on each floor, a clear 5 × 5 ft approach (that can overlap a hall).
6. **Accessibility benchmark.** The code's accessible-dwelling rules aren't required for a house, but they're the right yardstick:
   - a **1,700 mm (5'-7") clear turning circle** in the entry, kitchen, every bathroom and the laundry (ABC 3.8.4.3.(4), abc_2023 p.318);
   - a **step-free route** from the house to the garage and the deck (3.8.4.3.(3), p.318). Today's garage is 1.5 ft lower behind 3 steps: fix that, e.g. a garage slab at house level with the drive sloping up, or a ramp drawn in the garage. Say which.
   - **Halls ≥ 5 ft clear** (K-060). **All swing doors 36 in** (K-061).
   - **Curbless showers** (K-055), with the recessed floor flagged for the engineer.
7. **Basement bedrooms need an egress window** on an exterior wall (ABC 9.9.10.1, abc_2023 p.873):
   - an unobstructed opening ≥ **0.35 m²**, with no dimension < **380 mm**;
   - where it opens into a **window well**, ≥ **760 mm clear** in front of the window;
   - a well cover, if any, openable from inside.
   - Draw each bedroom window. Window rows are `[x, y, axis, width, sill, height]`; size the rough opening so a casement's clear opening comfortably beats 0.35 m², e.g. 2.5 × 4 ft. Draw the window wells as rooms of kind `porch`, labelled `WINDOW WELL`, or describe them in a table.
8. **The mechanical/utility room is on an exterior wall** (west, the services side). Round 1's GAS-01: a boiler, water heater and HRV need routes outdoors, and combustion air may not come from a crawl space.
9. **The checker passes on both levels:** `python3 /home/user/house-review/tools/check_layout.py <your main scad> <your basement scad>` prints OK. The reachability start is a room labelled `FOYER` (main) and one labelled `LIVING ROOM` (basement: use that label for the rec/family room).

## The program

Clear (inside) sizes from Kayla and Jordan's sketches and notes (2026-11-10), with the ranges the round-1 review suggested to make 3,000 fit.

**Main floor**

| Room | Target clear size | Must do |
|---|---|---|
| Kitchen | 15 × 22 (330) | Island with no seating and nothing in it (K-106, K-108). **54 in aisle on the dishwasher side** (K-274), 48 in elsewhere. Sink on an exterior wall under a window (K-124). Fridge near the pantry, **not beside the oven** (K-290). 1,700 mm turning circle. |
| Dining + breakfast nook | 14–16 × 22 (308–352) | 72 in round table for 8 + a 4-seat nook. Coffee station by the nook (K-117). Direct from the kitchen (K-035). |
| Pantry / scullery | 8 × 10–12 (80–96) | **Costco door to the garage** (K-037, K-115). Shallow shelves, upright freezer. |
| Living | 20 × 20 to 24 × 20 (400–480) | Sectional + 2 swivel chairs, 75 in TV, gas fireplace. Windows on 2 walls, none behind or facing the TV (K-066). |
| Primary bedroom | 22 × 20 to 22 × 24 (440–528) | King bed with 36 in+ around it (K-195), bench, armchair, dresser, vanity. Private porch access (K-191). North or north-east (K-013). |
| Primary ensuite | 170–228 | Curbless shower ≥ 60 × 48 with a bench, 72 in double vanity, WC room ≥ 48 × 72. Tub optional. 1,700 mm circle. |
| Primary closets | 2 walk-ins, each ≥ 7 × 8 | Reached from the bedroom, not only through the bath (K-201). On interior walls; the garage wall counts as exterior (K-070, K-331). |
| Primary laundry | ≥ 8 × 9 | Next to and connected to the suite, through the closet or bath (K-036). 1,700 mm circle. The house's only laundry. |
| Bedroom 2 | ~12 × 12 + closet | Near the primary (nursery/guest, K-245). East light if possible (K-014). |
| Shared full bath | ~8 × 10 | Not through a bedroom (K-179). |
| Powder room | ~5 × 7 | Near the mudroom/front door, off a hall, after storage (K-298). May be the shared bath if placed for both. |
| Mudroom | ~8 × 12 | Garage entry, step-free. Bench, lockers, drop zone, mail centre (K-148 to K-155). |
| Foyer + vestibule | vestibule ~6 × 8 + foyer | Coat closet. No direct view of the kitchen mess, a bedroom door or a toilet (K-104, K-262). |
| Office / library | ~240 (optional) | Only if the footprint stays ≤ 3,000; otherwise basement. |
| Elevator (future) | 6 × 7 incl. walls | See hard target 5. |
| Stair | straight, 19 risers, ≥ 42 in clear | See hard target 4. |
| Garage | 2 cars, ≥ 22 × 24 clear | Attached; not counted in the 3,000. Doors not facing the bedrooms (K-005, K-335). If its doors face south, draw the drive on your plan as a porch-kind strip, or a note. |
| Porches | not counted | Covered BBQ / outdoor dining reachable from the kitchen or dining room (K-023). A hot-tub sunroom is optional: only inside the 3,000, or drawn as a future addition outside it. |

**Basement** (10 ft ceiling, under the main floor)

| Room | Target | Must do |
|---|---|---|
| Bedroom 3 (guest) | ~12 × 13 + closet | Egress window (hard target 7). Near a bath. |
| Bedroom 4 | ~12 × 12 + closet | Egress window. |
| Bath(s) | Jack & Jill ~8 × 10, or 2 baths | Basement fixtures drain to a sewage ejector (round 1 PLB-04): draw a small ejector/sump spot in the mechanical room. |
| Flex / craft room | ~12 × 14 | Murphy-bed ready (K-237), so give it an egress window too. |
| Office / library | ~240 | If not upstairs. Quiet, away from the theatre. |
| Rec / family room | ~16 × 20 | Label `LIVING ROOM`. |
| Theatre | ~14 × 18 (optional) | Interior room; a flat floor at a 10 ft ceiling (no stadium tiers). |
| Gym / music | one room ~12 × 16 (optional) | |
| Mechanical / utility | ~10 × 12 | On the west exterior wall (hard target 8). |
| Storage | as space allows | |
| Elevator stop + stair foot | | Aligned with the main floor. |

If everything doesn't fit, drop the optional rooms first (theatre, gym/music, office/library downstairs) and say what was dropped. **Never exceed the footprint target.**

## The site (keep it)

- Road south (`site.scad:8`); septic tank at x −3..3, y 52–64, keep ≥ 3.3 ft from any wall; field further west; well at (150, 75) east; services enter on the west.
- Keep the house inside today's footprint box (x 0–130, y −16–70), with the front wall at y ≈ 0, so the site and the drain-exit point (22.16, 58) used by `plan_facts.py` still apply.
- The garage may stay at the west end.

## How to build (files)

- **Your folder:** `/home/user/house-review/docs/layout-options/round-2/option-<x>-<slug>/`. Write ONLY there and in `$RUN/work/OPT-<X>2/`.
  - Don't commit or switch branches.
  - Don't edit `models/`, `tools/` or other options' folders.
  - Don't run `tools/make_drawings.py`.
- **`house_lib_<x>.scad`:** copy `models/house_lib.scad` into your folder and change only what your option needs: `floor_to_floor()` = 11.75, and the stair functions (`stair_x`, `stair_top_y`, and the foot) for your stair position.
- **`main_floor_<x>.scad`:** start from a copy of `models/main_floor.scad`, with `use <house_lib_<x>.scad>`, and keep its table formats and the audit echo exactly. Replace the tables with your plan: rooms, doors, windows, fixtures, furniture, porch steps, posts, roof.
- **`basement_<x>.scad`:** start from `models/basement.scad`. Drop everything that comes from `foundation.scad` (pool, spa, theatre tiers, exit-stair areaway, light wells), remove that `use` line, and keep the table formats and the audit echo.
- **Check:** `python3 /home/user/house-review/tools/check_layout.py <main> <basement>` → `check_layout.txt`. It must say OK for both.
- **Measure:** `python3 $RUN/scripts/plan_facts.py --main <main> --basement <basement> --out $RUN/work/OPT-<X>2/facts`. Copy `matrix.md` → `matrix_<x>.md` and `plan_facts.md` → `plan_facts_<x>.md`. Re-run after every change.
- **Render:**
  - `python3 $RUN/scripts/plot_plan.py <main> <folder>/plan_<x>.png --title "Option <X> — <name> (main floor)"`;
  - the same for the basement → `basement_plan_<x>.png`;
  - one 3D view: `xvfb-run -a openscad -o <folder>/3d_<x>.png --imgsize=1800,1300 -D show_roof=false --viewall --autocenter <main>`, with the camera adjusted so the rooms read.
  - Open every PNG and check it's legible on a phone.

## `PROS-CONS.md` (sections in this order)

1. **Matrix numbers:** the round-1 rows (see `$RUN/briefs/LAYOUT-COMMON.md`) **plus**:
   - heated footprint (outside face) and basement footprint;
   - main-floor room count by type;
   - basement bedrooms with compliant egress windows (n of n);
   - elevator stacked (Y/N, with x/y);
   - stair (risers, flight height in mm, clear width);
   - step-free garage entry (Y/N, how);
   - 1,700 mm circles shown in the kitchen, baths and laundry (n of n).
2. **Program check:** every room in the two program tables, with its target size, your size and its area. Then the totals for the main floor and basement, and what was dropped.
3. **What it is:** one paragraph, and the shape.
4. **Pros, then cons:** each tied to evidence (a number, a K-item, a review finding, a code item).
5. **Kayla compliance:** re-score EVERY item ARC classed PLAN in `$RUN/findings/01-architecture-flow.md`, with the round-1 rulings:
   - a garage-wall closet = exterior;
   - a drive that's only noted, not drawn, doesn't count;
   - a kitchen crossing needs a clear lane outside the work zone;
   - a flush shower with a stated recess counts.
   - A table: K-ID | verdict | evidence. Then the counts and the 12 deal-breakers.
6. **Egress and accessibility table:** each basement bedroom's window (size, sill, estimated clear opening, well); the turning circles; door and hall widths; the elevator stack; the stair.
7. **Cost drivers vs today's model:** $ / $$ / $$$, naming the 2–3 that move the price. Repo research ranges only, cited.
8. **What you give up:** one honest line.
9. **Departures** from the site, septic, well and services: drawn, listed, costed, or "none".

`README.md`: 5 lines + status (complete, or exactly where you stopped).

**Privacy (binding):** the repo is PUBLIC. Never write a lift's weight rating, or anything about anyone's health, mobility, body or age. Keep accessibility wording generic.

**Rules:**
- No adjectives without numbers.
- Code citations only from the library (`python3 ~/code-library/search.py`, per `$RUN/briefs/COMMON-RULES.md`).
- No stamped-engineer claims: structural moves are flagged for the licensed Alberta engineer.
- If the session limit hits, write your status into README.md first.
- **Final message (300 words or fewer):** the matrix numbers block, top 3 pros and cons, the "what you give up" line, the checker result, and your folder.
