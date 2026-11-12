# Layout options, round 3: a central-hub main floor near 3,500 sq ft (binding for options G and H)

## Why round 3

Kayla's verdict on round 2 (11 November):
- **"too much walking through all the living rooms, I don't like them linear like that."** D, E and F each line the kitchen, dining and living up in a row, so daily trips pass through them.
- **The library is on the main floor, not optional.**
- **3,000 sq ft was a target, not a rule.**

Asked to choose, the household picked:
- the **central hub** shape: foyer, stair and lift in the middle, with the kitchen/dining, living, library and bedroom wing each opening off it;
- a main floor **held near 3,500 sq ft**, keeping her key rooms (library, primary, kitchen) and trimming the others.

**The measured problem.** `$RUN/scripts/routes.py` walks 10 daily routes through each plan's doors and lists the living rooms each route passes through:

| Plan | Pass-throughs on the 10 routes | Total walk |
|---|---|---|
| D | 11 | 552 ft |
| E | 3 | 419 ft |
| F | 14 | 738 ft |
| Today | 0 (16% of the floor is hall) | 597 ft (8 routes) |

The 10 routes:
- garage → kitchen;
- garage → primary;
- front door → primary;
- front door → kitchen;
- front door → library;
- primary → kitchen;
- bedroom 2 → kitchen;
- primary → laundry;
- lift → kitchen;
- lift → primary.

Living rooms are kitchen, dining, living and library/office. Round 3 has to reach **0 pass-throughs with short walks and tight halls**: the hub is the only connector, not a long hall.

## Hard targets (every option)

1. **Heated main-floor footprint, outside face, excluding the garage: 3,400–3,600 sq ft. Hard ceiling 3,650** (the matrix row in `plan_facts.py`). The basement sits under the main floor, same outline or smaller.
2. **Routes:** `routes.py --extended` reports **0 pass-throughs on all 14 routes**. That's the 10 above plus four living-room trips added on 11 Nov after the first H drawing: front door → living, front door → dining, kitchen → living, dining → living.
   - Garage → kitchen may pass through the mudroom or pantry; those are utility rooms, not living rooms.
   - **Total walk ≤ 420 ft for the 10 and ≤ 560 ft for all 14.**
   - Round-2 baseline on the 14: D 13 pass-throughs (653 ft), E 4 (514 ft), F 16 (850 ft).
3. **Not linear:** the kitchen/dining, the living and the library each open onto the hub. No three living rooms in a row along one axis. Kitchen → dining stays direct (K-035). Dining ↔ living may connect through a wide opening, as long as no route needs it.
4. **Halls:** strict circulation ≤ 12% (matrix row). The hub counts as circulation, so keep it a compact room, not a gallery. Halls ≥ 5 ft clear (K-060).
5. **Daylight:** building depth ≤ 40 ft wherever there are living rooms (outside face). Every bedroom, living room, kitchen, dining room and library has an exterior wall with a window, and a window on 2 walls where possible (K-064).
   - **The hub itself must get daylight:** a glazed front entry, a clerestory or a skylight, stated on the plan.
   - Round 1's C was rejected for a dark centre; don't repeat it.
6. **Stair:** one straight flight, 19 risers at floor_to_floor = 11.75 ft (3.58 m, ABC 9.8.3.3, abc_2023 p.852), ≥ 42 in clear.
   - **The floor opening runs ≥ 11.5 ft from the top nosing,** for headroom (round 2 CS-02/CS-04).
   - Level landings top and bottom, each at least as long as the stair is wide (CS-19).
   - The top of the stair opens off the hub.
7. **Elevator (future):** 6 × 7 ft including shaft walls, stacked on both floors within 0.1 ft, `ELEVATOR (FUTURE)`, kind `closet`, with a door.
   - It opens off the hub with a 5 × 5 ft clear approach.
   - Keep the shaft ≥ 4 ft from the perimeter ICF wall (round 2 CS-11, PMC-19: the pit).
8. **Accessibility benchmark** (ABC 3.8.4.3, abc_2023 p.318):
   - a 1,700 mm clear turning circle in the entry, kitchen, **every** bathroom including the powder room and the basement baths, and the laundry;
   - a step-free house → garage and → deck route (say how);
   - **all** swing doors 36 in, including storage and basement doors (round 2 ACC-05);
   - curbless showers, with the recess flagged for the engineer.
9. **Kitchen:**
   - the sink on an exterior wall under a window (K-124);
   - 54 in aisle on the dishwasher side (K-274);
   - the kitchen not visible from the front door: a vestibule with an inner door, or an offset (K-104, K-262, K-144).
10. **Closets** (walk-ins, linen, coat, bedroom closets) touch **no** exterior wall and no garage wall (K-070, K-331: a deal-breaker all three round-2 options missed in some form).
11. **Basement:**
    - bedrooms 3 and 4 and the murphy-ready flex room each get an egress window on an exterior wall (ABC 9.9.10.1, abc_2023 p.873: ≥ 0.35 m² unobstructed, no dimension < 380 mm, well ≥ 760 mm clear);
    - **no well under a deck or porch** (CS-03, CS-05);
    - **a well drawn for every below-grade window** (CS-06, CS-21);
    - **no bedroom shares a wall with the rec room, theatre or gym, and no gym or theatre under a main-floor bedroom** (K-334, ACC-08);
    - a sewage-ejector spot in the mechanical room.
12. **Mechanical room** on the west exterior wall (services enter west). Its intake and exhaust are drawn above grade and away from the garage (PMC-01/02/14, CS-18). The dryer is on an exterior wall or within 6 ft of one (PMC-06).
13. **Roof:** every heated room is under a roof block in the roof table (CS-20).
14. **The checker passes on both levels:** `python3 /home/user/house-review/tools/check_layout.py <main> <basement>`. The start rooms are `FOYER` (main) and `LIVING ROOM` (basement).

## The program (clear inside sizes; Kayla's Nov 11 list, held near 3,500)

**Main floor.** Keep: the library, the primary and the kitchen at her sizes. The others are trimmed as shown; a trim is the least you may go to, and you may give back size if the footprint allows.

| Room | Her size | Round 3 | Must do |
|---|---|---|---|
| **Library / shared office** | 15 × 16 | **15 × 16, keep** | Main floor, non-negotiable. Desks at one end, reading area at the other, a closable partition between. Each half with its own window. Opens off the hub, near the front door, not through the bedroom wing. Optional bay seat as a note. |
| **Primary bedroom** | 27 × 22 | **27 × 22, keep** | King bed with 36 in+ around it, bench, armchair, dresser, vanity. North or north-east (K-013). Private porch/deck access (K-191). Its door opens off the hub or a ≤ 15 ft bedroom hall; no separate entry hall. |
| **Kitchen** | 15 × 22 | **15 × 22, keep** | Island with no seating (K-106, K-108). Range + fridge on one long wall; tall freezer/oven column, sink, DW and coffee station on the other. Fridge near the pantry, not beside the oven (K-290). |
| Pantry | 12 × 8 | 12 × 8 (or 8 × 12) | Costco door to the garage (K-037, K-115), its own door to the kitchen; not a through-route. |
| Dining + breakfast nook | 14 × 22 | 14 × 19 | 72 in round table for 8, plus a 4-seat nook by the coffee station (K-117). Direct from the kitchen. |
| Living | 24 × 20 | 22 × 20 | Sectional, 2 swivel chairs, 75 in TV, gas fireplace; windows on 2 walls, none behind or facing the TV (K-066). South or south-west. |
| Ensuite | 16 × 10 | 13 × 10 | A screened, curbless tub + shower wet zone, or a shower ≥ 60 × 48 with a bench. Double vanity. WC room ≥ 48 × 72. Turning circle. |
| Walk-ins | 2 × (6 × 8) | 2 × (6 × 8) | Reached from the bedroom, not only through the bath (K-201). On interior walls. |
| Laundry | 9 × 10 | 8 × 9 | Opens to the bedroom hall or hub, optionally to a walk-in. W/D off the bed's headboard wall. Dryer vent ≤ 6 ft to an exterior wall. |
| Bedroom 2 | 12 × 14 | 12 × 12 + closet | Near the primary entrance (K-245); east light (K-014). |
| Shared bath | 8 × 8 | 8 × 8 | Not through a bedroom (K-179). |
| Powder | 6 × 7 | 5 × 7 off the hub, **or** merged into the shared bath if it opens off the hub | Turning circle. Door not facing the front door. |
| Mudroom | 9 × 12 | 8 × 10 | Garage entry, step-free. Bench, lockers, drop zone (K-148 to K-155). Leads to the hub without crossing the kitchen. |
| Foyer + vestibule | 10 × 8 | part of the hub | Vestibule with an inner door; coat closet on an interior wall. |
| Elevator (future) | 6 × 7 | 6 × 7 | See hard target 7. |
| Stair | — | straight, 19 risers | See hard target 6. |
| Garage | — | 2 cars, ≥ 22 × 24 clear | Not counted. Doors not facing the bedrooms (K-005, K-335). Draw its drive on the plan as a porch-kind strip. |
| Porches | — | not counted | Covered BBQ / outdoor dining off the kitchen or dining room (K-023). Hot-tub sunroom optional, as a note only. |

**Basement (10 ft ceiling).** As in round 2, minus the office, which is now upstairs:
- bedroom 3 (~12 × 13 + closet) and bedroom 4 (~12 × 12 + closet), egress;
- bath(s), with an ejector;
- flex/craft (~12 × 14, murphy-ready, egress);
- rec/family (`LIVING ROOM`, ~16 × 20);
- mechanical (~10 × 12, west wall);
- storage;
- theatre and gym optional;
- the stair foot and the elevator stop aligned with the main floor.

## Kayla's compass preferences (her sketch) and the site

- **Her sketch:** kitchen + dining **south-east**, living **south-west**, primary + bedroom 2 **north-east**, library **north-west** near the entry, the mudroom and pantry on the garage side next to the kitchen.
- **Mirroring:** the arrangement may be mirrored east–west if the garage works better on the east beside a south-east kitchen. Say which, and keep the garage doors and drive away from the bedrooms.
- **The site:**
  - road south (`site.scad:8`);
  - septic tank at x −3..3, y 52–64, ≥ 3.3 ft from any wall;
  - well at (150, 75);
  - services and the building drain leave on the west (drain exit (22.16, 58)).
- Keep the house inside x 0–130, y −16–70, with the front wall near y = 0.

## The two options (one designer each)

- **G — "Pinwheel hub":**
  - A compact block around a small, daylit central hub (skylight or clerestory over it, or one glazed side to the front).
  - Four room groups wrap the hub in a pinwheel, each touching the hub on one side and the outside on two:
    - kitchen/dining (+ pantry, mudroom, garage beside it);
    - living;
    - library;
    - the bedroom wing.
  - Overall about 58–64 ft each way.
- **H — "Knuckle hub":**
  - Two wings, each ≤ 40 ft deep, meet at a hub at their junction.
  - The public rooms cluster **around** the hub, not along a wing: kitchen/dining on one side of the hub, living on another, the library on a third, each opening onto it.
  - The quiet wing (primary, bedroom 2, laundry, shared bath) runs off the hub's fourth side through one short hall.
  - The garage attaches beyond the kitchen/dining group.
  - Distinct from G in plan shape: two wings and a junction, not a block.

## How to build (files)

- **Your folder:** `/home/user/house-review/docs/layout-options/round-3/option-<g|h>-<slug>/`. Write ONLY there and in `$RUN/work/OPT-<G|H>3/`.
  - Don't commit or switch branches.
  - Don't edit `models/`, `tools/` or other folders.
- **Start from a round-2 option's files, which already have the 11.75 ft floor-to-floor fork:** copy `docs/layout-options/round-2/option-f-your-sizes-fitted/house_lib_f.scad`, `main_floor_f.scad` and `basement_f.scad`. Rename them to `house_lib_<x>.scad`, `main_floor_<x>.scad` and `basement_<x>.scad`, fix the `use <>` lines, and set your stair functions.
  - Keep the table formats and the audit echo exactly.
  - Replace the tables with your plan: rooms, doors, windows, fixtures, furniture, porches, posts, roof.
- **Check:** `check_layout.py` → `check_layout.txt`. It must print OK for both levels.
- **Measure:**
  - `python3 $RUN/scripts/plan_facts.py --main <main> --basement <basement> --out $RUN/work/OPT-<X>3/facts`. Copy `matrix.md` → `matrix_<x>.md` and `plan_facts.md` → `plan_facts_<x>.md`.
  - `python3 $RUN/scripts/routes.py <main> --md` → `routes_<x>.md`.
  - `python3 $RUN/scripts/envelope.py <main> <basement>` → `envelope_<x>.txt`.
  - Re-run all three after every change.
- **Render:**
  - `python3 $RUN/scripts/plot_plan.py <main> <folder>/plan_<x>.png --title "Option <X> — <name> (main floor)"`;
  - the same for the basement → `basement_plan_<x>.png`;
  - one 3D view: `xvfb-run -a openscad -o <folder>/3d_<x>.png --imgsize=1800,1300 -D show_roof=false --viewall --autocenter <main>`.
  - Open every PNG and check it's legible on a phone.

## `PROS-CONS.md` (sections in this order)

1. **Matrix numbers:**
   - the heated footprint and basement footprint;
   - **the routes table** (`routes_<x>.md`) with its totals;
   - circulation %; perimeter and corners;
   - how the hub gets daylight;
   - main-floor rooms by type; basement egress (n of n); the elevator stack; the stair (risers, mm, clear width, opening length);
   - step-free garage entry; 1,700 mm circles (n of n);
   - doors (<32 / 32–35 / 36+, both levels);
   - closets on exterior walls (n);
   - the matrix's other round-1 rows.
2. **Program check:** every room, with her size, the round-3 size and your size. Then the totals and the footprint arithmetic: rooms clear → walls → halls → outside face.
3. **What it is:** one paragraph; why the hub works for her daily routes.
4. **Pros, then cons:** each with evidence.
5. **Kayla compliance:**
   - Re-score EVERY item ARC classed PLAN (`$RUN/findings/01-architecture-flow.md`, 164 items), measured on your plan. Don't carry anything over from another option.
   - Use the round-1 rulings: a garage-wall closet = exterior; a drive only noted doesn't count; a kitchen crossing needs a clear lane outside the work zone; a flush shower with a stated recess counts.
   - Give the counts and the 12 deal-breakers.
6. **Egress and accessibility table.**
7. **Cost drivers vs today's model and vs round-2 D/E/F:** repo ranges only, cited (the ICF wall at $35–50/sq ft of wall, HR:321; perimeter × 10.125 ft).
8. **What you give up:** one honest line.
9. **Departures** from the site, septic, well and services.

`README.md`: 5 lines + status (complete, or exactly where you stopped).

**Privacy (binding):** the repo is PUBLIC. Room sizes and layout intent only. Never write a lift's weight rating, or anything about anyone's health, mobility, body, age, work or hobbies. Keep accessibility wording generic.

**Rules:**
- No adjectives without numbers.
- Code citations only from the library (`python3 ~/code-library/search.py`, per `$RUN/briefs/COMMON-RULES.md`).
- No stamped-engineer claims: structural moves are flagged for the licensed Alberta engineer.
- If the session limit hits, write your status into README.md first.
- **Final message (300 words or fewer):** the footprint, the routes total and pass-throughs, circulation %, the checker result, the top 3 pros and cons, and the "what you give up" line.
