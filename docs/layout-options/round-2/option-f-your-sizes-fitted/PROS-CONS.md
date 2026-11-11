# Option F: Kayla's list (Nov 11), compact

**Drawn footprint: 3,910 sq ft** heated, outside face, excluding the garage (matrix row, `plan_facts.py`, `matrix_f.md`); basement 3,917 sq ft. No cap on this drawing. A compact L: the sunny wing (kitchen, dining, living in a row), the junction at the inner corner (foyer, stair top, elevator, powder), and the quiet wing turning north from it. There is no gallery and no hall along the sunny wing. Circulation is 10.7% strict (396 sq ft).

Earlier versions, kept as records: the Nov 10 sizes drawn at 3,032 (`*_nov10.*`); an L with a long link hall drew at 4,439 (19.5% circulation), moved out of the repo.

Files: `main_floor_f.scad`, `basement_f.scad`, `house_lib_f.scad` (floor-to-floor 11.75 ft; stair runs north to south, opening 11.6 ft from the top nosing, 12.0 ft wall to wall), `plan_f.png`, `basement_plan_f.png`, `3d_f.png`, `matrix_f.md`, `plan_facts_f.md`, `check_layout.txt` (both levels print OK).

## 1. Matrix numbers and the footprint arithmetic

**(a) Her list, clear:** about 2,923 sq ft. **(b) Drawn:** 3,910 sq ft at the outside face. The 987 sq ft between them:

| Step | sq ft |
|---|---|
| Her list, clear (a) | 2,923 |
| Added by the program (stair opening, elevator approach, bedroom 2 closet, linen) | +130 |
| Walls: clear to centre line, about 20 rooms at 0.4 ft | +183 |
| Halls (strict circulation, matrix row) | +396 |
| Rooms above her sizes and extras (foyer 11.8 x 8.4, ensuite 10.4 x 18.8, junction closet, pantry/mudroom turned, notches) | +72 |
| Heated main floor, centre lines | 3,704 |
| Outside-face offset (0.5 ft each wall, 412 ft of perimeter) | +206 |
| **Heated footprint, outside face** | **3,910** |

(c) The Nov 10 sizes drawn: 3,032 sq ft (`matrix_f_nov10.md`).

The drawn plan is about 210 sq ft above the 3,550 to 3,700 expected: the L's perimeter costs about 60 sq ft over a bar, the quiet wing's two-step hall (J + bedroom hall + short hall + primary entry) 130, and the ensuite turned to 10.4 x 18.8 about 25.

**(d) To reach 3,000 from F** (centre-line sq ft, about 5.5% more at the outside face), ranked:

| Move | Saves (outside face) |
|---|---|
| Office/library to the basement | 253 (about 267) |
| Primary 27 x 22 to 22 x 22 | 112 (about 118) |
| Living 24 x 20 to 20 x 20 | 82 (about 86) |
| Powder merged into the shared bath | 47 (about 50) |
| Ensuite 16 x 10 to 13 x 10 and laundry 9 x 10 to 8 x 9 | 48 (about 50) |
| Bedroom 2 12 x 14 to 12 x 12 | 28 (about 30) |
| Short hall to the primary and primary entry removed (door straight from the bedroom hall) | 100 (about 105) |

All seven together save about 706 and bring F to about 3,200. Closing the last 200 needs the L to become a 39 ft bar with halls near 7% (about 130 more) and the junction closet and stair-side passage folded into the foyer (about 70 more). Her list does not reach 3,000 without losing the office/library, a 22 x 22 primary and the 20 x 20 living together.

**Matrix numbers, F as drawn**

| Row | Option F (Nov 11, compact) |
|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED | 108 / 56 / 0 (of 164) (designer's own scoring; 28 rows re-scored on F, the rest carried from E, section 5) |
| Deal-breakers met (of 12) | 11 (K-331 closets on yard faces) |
| Review Blockers fixed / open (of 6) | 5 fixed / 1 open (STR-01) |
| Circulation % (strict / with foyer) | 10.7% / 13.4% (396 sq ft strict) |
| Drain-run index (ft), wet-wall groups (main), groups stacked over the basement | 1,017 ft (alt exit 848); 9; 0 of 9 |
| Single doors under 32 in / 32-35 in / 36 in+; minimum hall clear width | 0 / 0 / 19; 5.0 ft |
| No-threshold shower | Y (0.02 ft; recess flagged for the engineer) |
| Bedrooms sharing a wall with the living room | 0 |
| A bedroom next to the foyer | N |
| Master bed to laundry path | 29.6 ft |
| Master suite's side | north end of the east wing (x 99.6-127, y 44.6-67) |
| Bedrooms with east light | 2 of 2 on this floor |
| Living spaces facing south | LIVING (24.4 ft) plus the dining room |
| Living spaces with windows on 2+ walls | 5 (kitchen N/S, living N/S, office N/W, bedroom 2 E/S, primary E/N/W) |
| Building area, outside face, house + garage (m2) against 600 | 417.8 |
| **Heated main-floor footprint, outside face, excl. garage** | **3,910 sq ft** (centre lines 3,704) |
| **Basement footprint, outside face** | **3,917 sq ft** |
| Main-floor rooms by type | bedrooms 2; baths 3 (powder, shared, ensuite); kitchen, dining, living, office/library 1 each; utility 3; closets 6 (2 walk-ins, bedroom 2 closet, linen, junction closet, elevator); hall pieces 6; stairwell 1; garage 1 |
| Basement bedrooms with compliant egress windows | 2 of 2 (bedrooms 3 and 4), plus the flex room |
| Elevator stacked (Y/N, x/y) | Y: x 92-98.4, y 25.8-33.2 on both floors (6.4 x 7.4 ft centre lines) |
| Stair | 19 risers of 7.42 in; 3,581 mm; 5.4 ft wall to wall; opening 11.6 ft from the top nosing |
| Step-free garage entry | Y: garage slab at house level, drive slopes up |
| 1,700 mm circles shown | kitchen, foyer, powder, laundry, shared bath, ensuite, basement bath: 7 of 7 |
| Basement/shop/site changes | Basement under the L, no pool, no office; site: garage doors south, drive drawn as a strip; `site.scad` not edited |
| Cost vs the current model | $$ down (section 7) |

## 2. Program check (clear sizes)

| Room | Her size | F | Note |
|---|---|---|---|
| Primary bedroom | 27 x 22 | 27 x 22 | north end of the east wing; north windows; furniture with 36 in walkways |
| Ensuite | 16 x 10 | 10 x 18.4 (184 sf) | wet zone (tub + shower, screened, curbless) at the south end; vanity and WC outside; bench; turned 90 degrees to fit the wing; +2.4 ft in one dimension |
| Walk-ins | 2 x 6 x 8 | 2 x 6 x 8 | both off the primary bedroom |
| Laundry | 9 x 10 | 9 x 10 | W/D side by side on the east wall; opens to the bedroom hall and a walk-in |
| Living | 24 x 20 | 24 x 20 | kitchen, dining, living in a row |
| Kitchen | 15 x 22 | 15 x 22 | sink on the north wall under a window; range and fridge on the west run; island 2.8 ft wide |
| Dining + nook | 14 x 22 | 14 x 22 | round table for 8, nook table by the coffee station |
| Pantry | 12 x 8 | 9 x 12 | Costco door to the garage; its own kitchen entrance; not a through route |
| Office/library | 15 x 16 | 15 x 16 | north-west, off the mudroom; each half windowed; bay seat as a note |
| Bedroom 2 | 12 x 14 + closet | 12 x 14 + closet 7 x 8 | off the bedroom hall |
| Shared bath | 8 x 8 | 8 x 8 | off the bedroom hall |
| Mudroom | 9 x 12 | 9 x 12 | house door into the kitchen and the office |
| Foyer | 10 x 8 | 11.4 x 8 | vestibule folded in; front door opens into it |
| Powder | 6 x 7 | 6 x 7 | off the junction passage |
| Elevator | 6 x 7 + 5 x 5 | 6.4 x 7.4 + the junction hall | stacked |

Basement (no office): bedrooms 3 and 4 (12 x 14, egress), jack-and-jill bath, flex/craft 10 x 13 (egress), `LIVING ROOM` 21 x 20, gym/music, future theatre, utility on the west wall, storage.

## 3. What it is

A compact L, road south, garage west. The sunny wing runs west to east: garage, pantry and mudroom on the garage wall, kitchen, dining, living, joined by two 14 ft openings with 8 ft of wall left on each. At its east end is the junction: the foyer (front door opens into it), then north of it the stair (top nosing at the junction hall, the flight runs south to a foot under the foyer), the elevator off the junction hall, and a passage to the powder room. The quiet wing turns north from the junction: one 28 ft bedroom hall serves bedroom 2, the shared bath, the laundry and a short hall to the primary; walk-ins and the ensuite sit between that hall and the primary bedroom at the north end. The office/library is at the north-west corner, off the mudroom. The kitchen, dining, living sequence is the public route; the mudroom reaches the junction through the kitchen, along the edge of the seating, as in option D.

## 4. Pros, then cons

**Pros**
- **Every room at her size** except the pantry and ensuite, which are turned to fit (section 2).
- **Compact and daylit**: 10.7% circulation (against 19.5% for the first L); kitchen, living and office each have windows on two walls (K-064, K-097).
- **Quiet wing away from the living room**: 0 bedrooms share a wall with the living room; the foyer is 11 ft from the bedroom hall (K-328, K-334).
- **Junction as asked**: foyer, stair top, elevator approach and powder meet at one point, reachable from the garage side through the kitchen and from the front without crossing the bedroom wing.
- **Costco door** and its own kitchen entrance (K-037, K-115); **laundry** opens to the bedroom hall and a walk-in (K-036).
- **Code and access**: one straight 19-riser stair, elevator stacked, 19 of 19 doors 36 in, curbless showers, step-free garage.
- **Mechanical room on the west wall** under the office, north of the garage, so its louvres face open yard (CS-18).

**Cons**
- **3,910 sq ft**, 910 over a 3,000 cap (section 1d).
- **Circulation 10.7%**, 66 sq ft over the 330 limit; the bedroom hall is 28 ft, not 25.
- **The mudroom reaches the front of the house through the kitchen** (K-330 is met only because the kitchen has a clear lane outside the work zone).
- **Closets on exterior faces**: 4 of 6 (K-331 MISSING).
- **Stair foot under the foyer**: basement landing 4 ft; the flight and the foyer floor depth are for the engineer (CS-02, CS-04).
- **L plan**: 4 re-entrant corners and a 412 ft perimeter; long roof valleys (COST-08).
- **Long wing**: the primary is 70 ft from the kitchen.

| Deal-breaker | Verdict |
|---|---|
| Bedroom directly adjacent to foyer (K-328) | IN |
| Laundry far from bedrooms (K-329) | IN (29.6 ft) |
| Major path only through kitchen zone (K-330) | IN |
| Closets on exterior walls (K-331/K-070) | MISSING |
| Full open concept (K-332) | IN (broken open) |
| Through master bath to reach closet (K-333) | IN |
| Bedrooms sharing a wall with the living room (K-334) | IN |
| Garage at rear, drive past bedrooms (K-335/K-005) | IN |
| Laundry tied to master suite | IN |
| Costco door pantry to garage | IN |
| Wide doors and halls (K-003 + K-060 + K-061) | IN |
| No-threshold shower (K-055) | IN |

11 of 12 met.

## 5. Kayla compliance (every item ARC classed PLAN)

Rulings: a garage-wall closet counts as exterior; a drive that is only noted does not count (mine is drawn); a kitchen crossing needs a clear lane outside the work zone; a flush shower with a stated recess counts. Self-scored. 28 rows re-scored on F; the rest carry E's verdict ("Same basis as E", not re-measured on F), so treat them as provisional.

| K-ID | Verdict | Evidence | Basis |
|---|---|---|---|
| K-001 | IN | Same basis as E (not re-measured on F): Kitchen, laundry, primary suite, bedroom 2 and a bath are all on the main floor; no stairs to reach them | carried from E |
| K-002 | MISSING | Same basis as E (not re-measured on F): Basement 2,940 sf has theatre and gym/music, but no pool (removed by the round-2 direction) | carried from E |
| K-003 | IN | 0 single doors under 36 in (19 main swing doors, all 36 in) | re-scored on F |
| K-004 | IN | 5.6 ft circles drawn in kitchen, foyer, powder, laundry, shared bath, ensuite, basement bath | re-scored on F |
| K-005 | IN | Garage doors south; drive drawn as a strip x 0-23; the quiet wing is 100 ft east of it | re-scored on F |
| K-006 | MISSING | 9 wet-wall groups on main, 0 of 9 stacked over basement groups; drain-run index 1,017 ft | re-scored on F |
| K-007 | IN | Kitchen, dining, living, office/library, both bedrooms, ensuite have windows; foyer, mudroom, laundry, closets do not | re-scored on F |
| K-008 | IN | Matrix: 0 bedrooms share a wall with a living-kind room | re-scored on F |
| K-009 | IN | Guests reach kitchen, dining, living, powder and the stair without entering the bedroom hall | re-scored on F |
| K-010 | MISSING | Same basis as E (not re-measured on F): Bar is 72.5 x 39 ft (centre lines), not a 2 ft multiple; the 4.6 ft stair width and 5.5 ft hall are not either | carried from E |
| K-012 | IN | Living (24.4 ft), dining and the front door face south; garage doors face south | re-scored on F |
| K-013 | IN | Primary bedroom is the north end of the east wing, north wall 27.4 ft | re-scored on F |
| K-014 | MISSING | Same basis as E (not re-measured on F): Bedroom 2 and the primary bedroom both have east windows, but there is no sunroom (south-east) | carried from E |
| K-021 | IN | Dining/nook opens 14 ft to the kitchen; nook table by the coffee station | re-scored on F |
| K-023 | IN | Dining has a 6 ft double door to a 12 x 10 ft covered patio | re-scored on F |
| K-030 | IN | Pantry 9 x 12 ft clear (108 sf; her 12 x 8 turned to fit the garage wall) | re-scored on F |
| K-031 | IN | Office/library is off the mudroom, public side, not through the bedroom wing; basement has no office | re-scored on F |
| K-032 | IN | Office/library 15 x 16 ft on the main floor, desks end south, reading end north, closable partition (note) | re-scored on F |
| K-033 | IN | Powder (6 x 7 ft) is off the junction passage, 12 ft from the front door | re-scored on F |
| K-034 | MISSING | Same basis as E (not re-measured on F): No sunroom or screened porch drawn | carried from E |
| K-035 | IN | Kitchen and dining share a 14 ft opening | re-scored on F |
| K-036 | IN | Laundry opens to the bedroom hall and to a walk-in; 29.6 ft from the primary bed; W/D on the east wall, away from the bed | re-scored on F |
| K-037 | IN | Pantry shares 12.4 ft with the garage and has a 36 in door to it, level with the slab | re-scored on F |
| K-038 | MISSING | Same basis as E (not re-measured on F): No broom or vacuum closet is drawn on either level | carried from E |
| K-040 | MISSING | Same basis as E (not re-measured on F): No linen closet near bedroom 2 or the shared bath (the shared bath has no linen unit) | carried from E |
| K-041 | IN | Same basis as E (not re-measured on F): Vestibule 6.1 x 7.6 ft (46 sf) with an inner 36 in door | carried from E |
| K-043 | IN | Same basis as E (not re-measured on F): Foyer drop shelf (4.7 ft) on the north wall; mudroom drop counter 3.5 ft | carried from E |
| K-044 | IN | Same basis as E (not re-measured on F): Same foyer drop shelf, 3 ft high | carried from E |
| K-047 | IN | Same basis as E (not re-measured on F): Mudroom bench 5.3 ft by lockers; foyer bench 4.2 ft | carried from E |
| K-053 | IN | Same basis as E (not re-measured on F): King bed 6.5 ft wide: 7.8 ft to the west, 5.3 ft to the east, 3.4 ft at the foot (room 19.6 x 19.1 ft clear) | carried from E |
| K-055 | IN | Curbless wet zone (tub + shower) in the ensuite, shared bath shower, basement bath; recess flagged for the engineer | re-scored on F |
| K-058 | IN | Same basis as E (not re-measured on F): Elevator space 6.0 x 7.4 ft incl. walls at x 42-48, y 27-34.4 on both floors, with a 5.5 x 7.4 ft approach | carried from E |
| K-059 | MISSING | Same basis as E (not re-measured on F): No dumbwaiter shaft | carried from E |
| K-060 | IN | Smallest hall is 5.0 ft clear (short hall to the primary); passage 6.4 ft, bedroom hall 5.4 ft | re-scored on F |
| K-061 | IN | All 19 main-floor swing doors are 36 in | re-scored on F |
| K-062 | MISSING | Same basis as E (not re-measured on F): Kitchen, dining and living are joined by an 8 ft and a 15 ft full opening with no door: only the service rooms and bedrooms are closed off | carried from E |
| K-064 | MISSING | Same basis as E (not re-measured on F): Living has windows on one wall (south); kitchen (N/W), bedroom 2 (E/S) and primary (E/N) have two | carried from E |
| K-069 | IN | Same basis as E (not re-measured on F): Heated bar has 4 outside corners and 0 inside (was 17 + 13); perimeter 223 ft (was 395.5); with the garage 5 + 1 | carried from E |
| K-070 | IN | Same basis as E (not re-measured on F): 0 of 3 closet-kind rooms (2 WICs, elevator) touch a yard or porch wall | carried from E |
| K-071 | IN | Same basis as E (not re-measured on F): Both WICs are fully interior (north: laundry/ensuite; south: living/foyer) | carried from E |
| K-072 | MISSING | Same basis as E (not re-measured on F): Ensuite WC is its own room; the shared bath has the shower at the far end, not toilet between shower and door | carried from E |
| K-074 | IN | Same basis as E (not re-measured on F): No tub drawn: no tub on an exterior wall | carried from E |
| K-075 | MISSING | Same basis as E (not re-measured on F): West service/kitchen zone and east bedroom zone are joined on the north side by a 19.5 ft band (hub, laundry, closets), but the living room and foyer sit between them on the south | carried from E |
| K-077 | IN | Same basis as E (not re-measured on F): No room has windows on opposite walls | carried from E |
| K-078 | MISSING | Same basis as E (not re-measured on F): Not designed for cross-breeze diagonals | carried from E |
| K-080 | MISSING | Same basis as E (not re-measured on F): Living window (12 ft) is centred on its 18.5 ft wall | carried from E |
| K-081 | MISSING | Same basis as E (not re-measured on F): Kitchen west window (5 ft) has no overhang; the garage is beside it | carried from E |
| K-083 | MISSING | Same basis as E (not re-measured on F): Living 1.06, kitchen 1.09, primary 1.02; none inside 1.4-1.6 | carried from E |
| K-095 | IN | Same basis as E (not re-measured on F): Patio 12 ft (3.7 m) and front porch 12 ft deep: inside the 4-5 m limit | carried from E |
| K-096 | MISSING | Same basis as E (not re-measured on F): Sink run is on the north (outside) wall under the window (K-124), range on the west (outside) wall | carried from E |
| K-099 | IN | Same basis as E (not re-measured on F): Dining, living and front rooms face south; the kitchen is north | carried from E |
| K-100 | IN | Same basis as E (not re-measured on F): Primary bedroom (E+N) and bedroom 2 (E+S) get morning light | carried from E |
| K-102 | MISSING | Same basis as E (not re-measured on F): Powder door opens straight to a toilet 7 ft away; the ensuite WC door is off the bathing room | carried from E |
| K-103 | MISSING | Same basis as E (not re-measured on F): Powder door (x 72.8-75.8) is visible from the foyer | carried from E |
| K-104 | IN | Same basis as E (not re-measured on F): From the foyer opening (y 9-14) the east line hits the hall wall between the bedroom 2 door (y 3-6) and the bath door (y 14-17) | carried from E |
| K-105 | IN | Same basis as E (not re-measured on F): Laundry door (x 54.5-57.5) is off the line of the living-room opening (x 48.2-53.3) | carried from E |
| K-106 | IN | Island 2.8 x 9.4 ft, no seating, nothing in it | re-scored on F |
| K-107 | IN | Same basis as E (not re-measured on F): Banquette plus 3 ft round table in the dining room | carried from E |
| K-108 | IN | No sink or cooktop in the island | re-scored on F |
| K-114 | IN | Same basis as E (not re-measured on F): Walk-in pantry 74 sf off the kitchen, with a freezer | carried from E |
| K-115 | IN | Same basis as E (not re-measured on F): Same as K-037 | carried from E |
| K-116 | IN | Same basis as E (not re-measured on F): Garage to pantry to kitchen: two 36 in doors, 18 ft to the fridge | carried from E |
| K-117 | IN | Same basis as E (not re-measured on F): Coffee counter 3.8 ft at the dining room's north wall beside the nook (no pot filler drawn) | carried from E |
| K-123 | MISSING | Same basis as E (not re-measured on F): Island faces the dining room; the living room is 20 ft further east | carried from E |
| K-124 | IN | Kitchen sink on the north wall under an 8 ft window | re-scored on F |
| K-127 | IN | Same basis as E (not re-measured on F): 6 ft double door from the dining room to the covered patio | carried from E |
| K-128 | IN | Same basis as E (not re-measured on F): 72 in round table with 3.8 ft of clear floor each side | carried from E |
| K-129 | MISSING | Same basis as E (not re-measured on F): 6 ft double door only; no multi-panel wall | carried from E |
| K-132 | IN | Same basis as E (not re-measured on F): Living 18.1 x 19.1 ft (346 sf) holds the sectional and two chairs | carried from E |
| K-133 | MISSING | Same basis as E (not re-measured on F): Living has windows to the porch, not a door; the dining room has the door | carried from E |
| K-134 | MISSING | Same basis as E (not re-measured on F): Same as K-129 | carried from E |
| K-140 | IN | Same basis as E (not re-measured on F): Foyer bench 4.2 ft and mudroom bench | carried from E |
| K-141 | IN | Same basis as E (not re-measured on F): Closed 7 ft coat cabinet 4.5 ft wide in the foyer | carried from E |
| K-142 | IN | Same basis as E (not re-measured on F): Same closed cabinet | carried from E |
| K-143 | IN | Same basis as E (not re-measured on F): Foyer drop shelf and mudroom counter | carried from E |
| K-144 | IN | Same basis as E (not re-measured on F): Front door looks north across the foyer to the coat wall; the kitchen is 50 ft away with no opening to the foyer | carried from E |
| K-145 | IN | Same basis as E (not re-measured on F): Powder 4.5 x 8 ft beside the vestibule, 8 ft from the front door | carried from E |
| K-146 | IN | Same basis as E (not re-measured on F): Mudroom bench 5.3 ft | carried from E |
| K-147 | IN | Same basis as E (not re-measured on F): Lockers 5.3 ft on the south wall | carried from E |
| K-149 | IN | Same basis as E (not re-measured on F): Lockers 7 ft high | carried from E |
| K-151 | IN | Same basis as E (not re-measured on F): Mudroom counter 3.5 ft at the garage door | carried from E |
| K-153 | IN | Same basis as E (not re-measured on F): Foyer drop shelf; mudroom counter | carried from E |
| K-155 | MISSING | Same basis as E (not re-measured on F): Mudroom has no outside door; its only exit is the garage door and the dining door | carried from E |
| K-156 | IN | Same basis as E (not re-measured on F): Garage door into the mudroom, step-free (garage slab at house level) | carried from E |
| K-157 | MISSING | Same basis as E (not re-measured on F): Powder is about 40 ft from the mudroom | carried from E |
| K-158 | IN | Same basis as E (not re-measured on F): Laundry through the primary closet, 30.0 ft from the bed | carried from E |
| K-163 | IN | Same basis as E (not re-measured on F): Laundry sink 2.9 ft counter drawn | carried from E |
| K-166 | MISSING | Same basis as E (not re-measured on F): No pass-through basket or chute between the closet and the laundry | carried from E |
| K-170 | MISSING | Same basis as E (not re-measured on F): No dog wash drawn | carried from E |
| K-172 | MISSING | Same basis as E (not re-measured on F): No litter spot drawn | carried from E |
| K-179 | IN | Same basis as E (not re-measured on F): Shared bath off the private hall; ensuite off the primary bedroom | carried from E |
| K-183 | MISSING | Same basis as E (not re-measured on F): No main-floor office; the office is in the basement | carried from E |
| K-185 | MISSING | Same basis as E (not re-measured on F): No sunroom | carried from E |
| K-186 | MISSING | Same basis as E (not re-measured on F): No sunroom | carried from E |
| K-188 | MISSING | Same basis as E (not re-measured on F): No sunroom | carried from E |
| K-189 | MISSING | Same basis as E (not re-measured on F): No sunroom | carried from E |
| K-191 | IN | Same basis as E (not re-measured on F): 6 ft double door from the primary bedroom to a 16 x 11.5 ft deck | carried from E |
| K-192 | IN | Same basis as E (not re-measured on F): The only fireplace is in the living room | carried from E |
| K-195 | IN | Same basis as E (not re-measured on F): Primary bedroom 19.6 x 19.1 ft clear; bed 3+ ft clear on three sides | carried from E |
| K-200 | IN | Same basis as E (not re-measured on F): Two separate WICs, 65 sf each (7.1 x 9.1 ft) | carried from E |
| K-201 | IN | Same basis as E (not re-measured on F): WIC A opens from the bedroom; WIC B opens from WIC A, the laundry and the ensuite | carried from E |
| K-202 | IN | Same basis as E (not re-measured on F): WIC B also opens to the ensuite | carried from E |
| K-203 | IN | Same basis as E (not re-measured on F): WIC B opens to the laundry | carried from E |
| K-210 | MISSING | Same basis as E (not re-measured on F): Laundry is through the closet, but no pass-through basket | carried from E |
| K-211 | IN | Same basis as E (not re-measured on F): Shower 5.0 x 4.3 ft, flush (0.02 ft); recess flagged for the engineer | carried from E |
| K-220 | MISSING | Same basis as E (not re-measured on F): No tub drawn | carried from E |
| K-224 | IN | Same basis as E (not re-measured on F): Double vanity 6.3 ft | carried from E |
| K-226 | MISSING | Same basis as E (not re-measured on F): No towel storage drawn in the ensuite | carried from E |
| K-227 | IN | Same basis as E (not re-measured on F): WC room 5.1 x 9.6 ft clear, 36 in door | carried from E |
| K-228 | IN | Same basis as E (not re-measured on F): Ensuite to WIC B to laundry, 3 doors | carried from E |
| K-229 | IN | Same basis as E (not re-measured on F): Door from the ensuite to WIC B | carried from E |
| K-237 | IN | Same basis as E (not re-measured on F): Basement flex 10.6 x 13.6 ft clear, egress window 4 x 3 ft | carried from E |
| K-238 | IN | Same basis as E (not re-measured on F): Bedroom 2 14.1 x 11.1 ft clear holds a queen; basement bedrooms 11.6 x 13.6 ft | carried from E |
| K-239 | MISSING | Same basis as E (not re-measured on F): Bedroom 2 uses the shared bath off the hall; basement bedrooms share a J&J bath | carried from E |
| K-240 | MISSING | Same basis as E (not re-measured on F): Bedroom 2 has no exterior door; it faces the south wall and the east wall only | carried from E |
| K-242 | IN | Same basis as E (not re-measured on F): Bedroom 2 plus basement bedrooms 3 and 4 and a flex room | carried from E |
| K-244 | IN | Same basis as E (not re-measured on F): Basement J&J bath between bedrooms 3 and 4 (112 sf) | carried from E |
| K-245 | IN | Same basis as E (not re-measured on F): Bedroom 2 is 8 ft from the primary bedroom (the bath between), east light | carried from E |
| K-248 | IN | Same basis as E (not re-measured on F): Front porch 35 x 12 ft under a roof | carried from E |
| K-249 | MISSING | Same basis as E (not re-measured on F): Mudroom has no outside door, so no covered entry | carried from E |
| K-252 | IN | Same basis as E (not re-measured on F): Patio 14 x 12 ft (168 sf) under a roof beside the dining room | carried from E |
| K-253 | IN | Same basis as E (not re-measured on F): Front porch 35 x 12 ft (420 sf) adjoins the patio | carried from E |
| K-254 | MISSING | Same basis as E (not re-measured on F): Every porch is roofed; no sun-only area | carried from E |
| K-255 | MISSING | Same basis as E (not re-measured on F): No desk or work spot drawn on a porch | carried from E |
| K-256 | IN | Same basis as E (not re-measured on F): 3.0 ft of counter on each side of the range and the sink | carried from E |
| K-257 | MISSING | Same basis as E (not re-measured on F): No counter beside the fridge: the pantry door is on its east side | carried from E |
| K-261 | MISSING | Same basis as E (not re-measured on F): Fridge to sink 17.9 ft, sink to range 12.7 ft, range to fridge 11.3 ft = 41.9 ft (26 ft limit) | carried from E |
| K-262 | IN | Same basis as E (not re-measured on F): No opening from the foyer to the kitchen; the kitchen is first seen from the dining room | carried from E |
| K-270 | MISSING | Same basis as E (not re-measured on F): Fridge to sink 17.9 ft is about 7 steps | carried from E |
| K-273 | MISSING | Same basis as E (not re-measured on F): Fridge door swings toward the pantry door's landing | carried from E |
| K-274 | IN | Island to the sink/dishwasher run 5.0 ft (60 in); island to the range run 4.0 ft | re-scored on F |
| K-277 | IN | Same basis as E (not re-measured on F): Sink under the north window | carried from E |
| K-279 | IN | Same basis as E (not re-measured on F): Island is 4.6 ft from the fridge as a landing zone | carried from E |
| K-281 | IN | Same basis as E (not re-measured on F): Island 44 sf clear of fixtures | carried from E |
| K-282 | MISSING | Same basis as E (not re-measured on F): Island centre is 12.4 ft from the fridge and 9.8 ft from the sink | carried from E |
| K-283 | IN | Same basis as E (not re-measured on F): 3.0 ft of counter each side of the range | carried from E |
| K-288 | IN | Same basis as E (not re-measured on F): Dishwasher drawn next to the sink | carried from E |
| K-290 | IN | Range and fridge share the west run, 4 ft apart; the sketch groups them | re-scored on F |
| K-292 | MISSING | Same basis as E (not re-measured on F): Fridge stands alone 5 ft from the first counter run | carried from E |
| K-297 | MISSING | Same basis as E (not re-measured on F): No glass partition in the vestibule or foyer | carried from E |
| K-298 | MISSING | Same basis as E (not re-measured on F): Powder door opens directly into the foyer, not off a hall after storage | carried from E |
| K-299 | MISSING | Same basis as E (not re-measured on F): Looking north from the front door ends at the coat wall 11 ft away | carried from E |
| K-300 | MISSING | Same basis as E (not re-measured on F): Same as K-299 | carried from E |
| K-302 | MISSING | Same basis as E (not re-measured on F): Office is in the basement; the J&J bath is 40 ft away | carried from E |
| K-304 | IN | Same basis as E (not re-measured on F): WIC A opens from the bedroom | carried from E |
| K-306 | IN | Same basis as E (not re-measured on F): Primary bed head on the north wall between windows (x 79-83.5 and 92-96); basement beds on the west wall | carried from E |
| K-307 | MISSING | Same basis as E (not re-measured on F): Primary north windows are 4 ft from the corners, not in them | carried from E |
| K-315 | IN | Same basis as E (not re-measured on F): Same as K-037 | carried from E |
| K-316 | IN | Same basis as E (not re-measured on F): Circulation 284 sf = 10.1% strict (11.9% with the foyer), was 16.2% (21.9%) | carried from E |
| K-317 | IN | Same basis as E (not re-measured on F): Rooms open off the living zone or the 5.5 ft hub; the only hall is the 107 sf private hall | carried from E |
| K-318 | IN | Same basis as E (not re-measured on F): Kitchen is a dead end; garage to primary and laundry to bedroom paths use the dining, living and hub | carried from E |
| K-320 | IN | Same basis as E (not re-measured on F): Foyer drop shelf and bench, mudroom counter and lockers, pantry beside the garage | carried from E |
| K-323 | MISSING | Same basis as E (not re-measured on F): Living south wall is 12 ft of glass in 18.5 ft | carried from E |
| K-324 | MISSING | Same basis as E (not re-measured on F): Dining and living share a 15 ft opening: one zone, no door | carried from E |
| K-325 | IN | Same basis as E (not re-measured on F): No bedroom shares a wall with a living room, kitchen or garage | carried from E |
| K-326 | IN | Same basis as E (not re-measured on F): Bedroom 2 is buffered by the hall and bath; the primary by closets, ensuite and hall | carried from E |
| K-328 | IN | Same basis as E (not re-measured on F): No bedroom touches the foyer; the private hall is between | carried from E |
| K-329 | IN | Same basis as E (not re-measured on F): Laundry 30 ft from the primary bed by door path | carried from E |
| K-330 | IN | Same basis as E (not re-measured on F): Primary to laundry goes through the closets, not the kitchen zone | carried from E |
| K-331 | MISSING | Walk-in (98.4, 36.2) has a yard wall 1.2 ft, the bedroom 2 closet and two junction closets are on yard faces (4 of 6 closets touch an exterior wall) | re-scored on F |
| K-332 | IN | Kitchen to dining 14 ft and dining to living 14 ft openings with 8 ft of wall left on each; the foyer opens 6.5 ft | re-scored on F |
| K-333 | IN | Same basis as E (not re-measured on F): Closet A opens from the bedroom | carried from E |
| K-334 | IN | Same basis as E (not re-measured on F): 0 bedrooms share a wall with the living room | carried from E |
| K-335 | IN | Same basis as E (not re-measured on F): Garage doors south; the drive is drawn at x 0-24; nearest bedroom is 58 ft away | carried from E |

## 6. Egress and accessibility table

**Basement egress** (ABC 9.9.10.1.(2), abc_2023 p.873: 0.35 m2 or more, no dimension under 380 mm; (3): 760 mm clear in front of a well window)

| Window | Rough opening, sill | Estimated clear opening | Well |
|---|---|---|---|
| Bedroom 3, x 35-39, y 0 | 4.0 x 3.0 ft, sill 3.5 ft | about 3.4 x 2.5 ft = 8.5 sf = 0.79 m2; smallest side 762 mm | x 33.5-40, 3.5 ft out; clear of the patio (x 49-61) |
| Bedroom 4, x 62-65.6, y 0 | 3.6 x 3.0 ft | about 3.0 x 2.5 ft = 0.70 m2 | x 61.5-67; clear of the patio (ends x 61) |
| Flex room, x 106-110, y 12.4 | 4.0 x 3.0 ft | about 3.4 x 2.5 ft = 0.79 m2 | x 104.8-111.5, y 8.4-12.4; no porch or deck on that side |

Estimates for one casement; confirm against the manufacturer's rating. A cover, if any, must open from inside. Wells are about 6.7 ft deep.

**Turning circles (1,700 mm):** kitchen, foyer, powder (6 x 7 ft), laundry, shared bath, ensuite, basement bath: all drawn.

**Doors and halls:** 19 of 19 main swing doors 36 in. Halls: junction passage 6.4 ft, junction hall 5.4 ft, bedroom hall 5.4 ft, short hall to the primary 5.0 ft.

**Elevator stack:** x 92-98.4, y 25.8-33.2 on both floors. Main: door on the south face onto the junction hall (11.8 x 5.4 ft). Basement: door onto the hall under it. Labelled ELEVATOR (FUTURE).

**Stair:** straight, 19 risers of 7.42 in, 18 treads of 10.5 in, flight height 3,581 mm, 5.4 ft wall to wall; opening 11.6 ft from the top nosing (12.0 ft wall to wall); top landing is the junction hall (11.8 x 5.4 ft); foot at y 4.45 under the foyer onto a 4 ft landing.

**Step-free route:** garage slab at house level; the patio door level; the front porch level with steps down (a ramp is a site item).

## 7. Cost drivers vs today's model

**$$ down.** Repo research gives no whole-house $/sq ft (07-cost-ve.md header), so these are ranked.
1. **Basement and pool removed ($$$ down)**: COST-01; the pool, spa, theatre tiers and exit stair go; 10 ft ceiling (COST-12).
2. **Heated footprint 3,910 against 5,685 sq ft ($$ down)** with an L of 4 re-entrant corners (COST-08).
3. **Added items ($ up)**: elevator shaft, 3 egress windows and wells (window range $850-$1,600 each, HR:434 as quoted in COST-09), the office wing beside the garage.

## 8. What you give up

Her list drawn at her sizes needs 3,910 sq ft, about 910 over a 3,000 cap, and its primary suite is 70 ft from the kitchen.

## 9. Departures

- **Site, septic, well, services:** none. The house stays inside x 16.6-130 and y -16 to 70 (primary north wall at y 67); `site.scad` not edited.
- **Garage doors** turn from the west face to the south face; the drive is a strip (x 0-23, y -16 to 0).
- **Utility room** moves to the basement west wall at x 16.6-26.6, y 24.8-41.2 (under the office, north of the garage). GAS-01 needs a B149.1 check (not in the library).
- **Office/library** is heated floor north of the garage (x 16.6-23); its south wall is shared with the garage.
- **Basement ICF wall height** (STR-01) unchanged and still open.
