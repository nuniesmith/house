# Option E: Linear ranch

Files: `main_floor_e.scad`, `basement_e.scad`, `house_lib_e.scad` (forked: floor-to-floor 11.75 ft, east-west stair), `plan_e.png`, `basement_plan_e.png`, `3d_e.png`, `matrix_e.md`, `plan_facts_e.md`, `check_layout.txt` (both levels print OK).

## 1. Matrix numbers

| Row | Option E | Current model |
|---|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED (of 164) | 103 / 60 / 1 (designer's own scoring, section 5) | 62 / 89 / 13 |
| Deal-breakers met (of 12) | 11 (K-332 full open concept is contradicted) | 5 |
| Review Blockers fixed / open (of 6) | 5 fixed (CODE-01, STR-04, STR-02, STR-03, PLB-01) / 1 open (STR-01) | 0 / 6 |
| Circulation % (strict / with foyer) | 10.1% / 11.9% (284 sf of 2,828) | 16.2% / 21.9% |
| Drain-run index (ft), wet-wall groups (main), groups stacked over the basement | 667 ft (alt exit 514); 8; 1 of 8 | 879 ft; 14; 1 of 14 |
| Single doors under 32 in / 32-35 in / 36 in+; minimum hall clear width | 0 / 0 / 19; 5.10 ft (raw 4.20 ft at the stair-top landing, which opens onto the 10 ft hub) | 7 / 11 / 4; 3.71 ft |
| No-threshold shower | Y (0.02 ft; recess flagged for the engineer) | N |
| Bedrooms sharing a wall with the living room | 0 | 0 |
| A bedroom next to the foyer | N | N |
| Master bed to laundry path | 30.0 ft (through WIC A and WIC B) | 103.1 ft |
| Master suite's side | north-east (x 58.5-96.5, y 19.5-39) | north-east block |
| Bedrooms with east light | 2 of 2 on this floor (bedroom 2, primary) | 1 |
| Living spaces facing south | 1 living-kind (LIVING, 18.5 ft of south wall) plus the dining room (14 ft) | 1 (DEN) |
| Living spaces with windows on 2+ walls | 3 rooms (kitchen N/W, bedroom 2 E/S, primary E/N); 0 living-kind | 4 rooms |
| Building area, outside face, house + garage (m2) against 600 | 335.6 (centre lines 322.9) | 608.0 |
| **Heated main-floor footprint, outside face, excl. garage** | **2,940 sq ft** (73.5 x 40 ft; centre lines 2,828) | 5,685 |
| **Basement footprint, outside face** | **2,940 sq ft** (same outline) | 3,617 |
| Main-floor rooms by type | bedrooms 2; baths 4 (powder, shared bath, WC room, ensuite); kitchen 1; dining 1; living 1; utility 3 (mudroom, pantry, laundry); closets 3 (2 WICs + elevator); hall rows 7 (vestibule, foyer, 5 hall pieces); stairwell 1; garage 1 | |
| Basement bedrooms with compliant egress windows | 2 of 2 (bedrooms 3 and 4), plus the flex room | |
| Elevator stacked (Y/N, x/y) | Y: x 42-48, y 27-34.4 on both floors (6.0 x 7.4 ft incl. walls) | N |
| Stair (risers, flight height, clear width) | 19 risers of 7.42 in; 3,581 mm; 4.2 ft (1,280 mm) | 22 risers; 4,191 mm; 4.2 ft |
| Step-free garage entry (Y/N, how) | Y: garage slab at house level (z0 = 0), the drive slopes up to it | N (3 steps) |
| 1,700 mm circles shown | kitchen 1 of 1; entry 1 of 1; laundry 1 of 1; baths 3 of 5 (shared, ensuite, basement J&J; the powder and the WC room are under 5.6 ft wide) | 0 |
| Basement/shop/site changes | Basement: new level under the bar, no pool. Shop: none. Site: garage doors turn to the south, drive drawn as a strip (x 0-24, y -16 to 0); `site.scad` not edited | none |
| Cost vs the current model | $$$ down (see section 7) | |

The tool's "bedroom to drive 14.0 ft" row reads `site.scad`'s old west drive. With the drive drawn at x 0-24 on the south face, bedroom 2 (x 82) is 58 ft from it.

## 2. Program check

Clear sizes are centre-line size minus 0.4 ft per dimension.

**Main floor**

| Room | Target | Mine (clear) | Area (sf) |
|---|---|---|---|
| Kitchen | 15 x 22 (330) | 17.6 x 19.1 | 336 |
| Dining + nook | 14-16 x 22 (308-352) | 13.6 x 19.1 | 260 (48 under) |
| Pantry | 8 x 10-12 (80-96) | 8.6 x 8.6 | 74 (6 under) |
| Living | 20 x 20 to 24 x 20 (400-480) | 18.1 x 19.1 | 346 (54 under) |
| Primary bedroom | 22 x 20 to 22 x 24 (440-528) | 19.6 x 19.1 | 374 (66 under) |
| Primary ensuite | 170-228 | 12.1 x 9.6 + WC room 5.1 x 9.6 | 116 + 49 = 165 |
| Primary closets | 2 walk-ins, each 7 x 8 or more | 7.1 x 9.1 each | 65 + 65 |
| Primary laundry | 8 x 9 or more | 7.6 x 9.1 | 69 (3 under) |
| Bedroom 2 | 12 x 12 + closet | 14.1 x 11.1 (2 x 8 ft wardrobe built in) | 157 |
| Shared full bath | 8 x 10 | 14.1 x 7.6 | 107 |
| Powder | 5 x 7 | 4.1 x 7.6 | 31 |
| Mudroom | 8 x 12 | 8.6 x 10.1 | 87 |
| Vestibule + foyer | 6 x 8 + foyer | 6.1 x 7.6 + 10.6 x 11.1 | 46 + 118 |
| Office / library | 240, only if footprint allows | not on this floor (the footprint is 2,940, and the plan is full) | basement 222 |
| Elevator (future) | 6 x 7 incl. walls | 6.0 x 7.4 (centre lines) | 44 |
| Stair | straight, 19 risers, 42 in clear or more | 1 flight, 4.2 ft clear | 47 opening |
| Garage | 2 cars, 22 x 24 clear or more | 23.6 x 26.6 | 628 (not counted) |
| Porches | not counted | patio 14 x 12 (168), front porch 35 x 12 (420), deck 16 x 11.5 (184) | |

Main-floor total: 2,828 sf at centre lines, 2,940 sf at the outside face. Circulation rows: 284 sf.

**Basement**

| Room | Target | Mine (clear) | Area (sf) |
|---|---|---|---|
| Bedroom 3 | 12 x 13 + closet | 11.6 x 13.6 | 158 |
| Bedroom 4 | 12 x 12 + closet | 11.6 x 13.6 | 158 |
| Bath | J&J 8 x 10 | 7.6 x 13.6 | 103 |
| Flex / craft | 12 x 14 | 10.6 x 13.6 | 144 (24 under) |
| Office | 240 | 11.6 x 19.1 | 222 |
| Rec room (LIVING ROOM) | 16 x 20 | 19.6 x 19.1 | 374 |
| Theatre | 14 x 18 | 13.6 x 19.1 (has two outside walls, no windows) | 260 |
| Gym / music | 12 x 16 | 12.6 x 19.1 | 241 |
| Mechanical / utility | 10 x 12, west wall | 7.6 x 19.1 | 145 |
| Storage | as space allows | 263 (west) + 3 small rooms (29-36 each) | |
| Elevator stop + stair foot | aligned | x 42-48, y 27-34.4; stair room x 37.5-53.5 | 39 + 66 |

Basement total: 2,828 sf at centre lines.

**Dropped or short:** a library and a sunroom / hot-tub sunroom (not drawn); the powder has no 1,700 mm circle; the ensuite WC room is a separate 49 sf room. Short against target: dining, living, primary bedroom, pantry, flex. Nothing optional in the basement was dropped.

## 3. What it is

A single straight bar, 73.5 x 40 ft outside (2,940 sq ft heated, one hip roof ridge, 4 outside corners), with the 2-car garage (23.6 x 26.6 ft clear, slab at house level, doors on the south face) on the west end. Walking west to east on the south side: mudroom and pantry beside the garage, dining with its covered patio, living, a vestibule and foyer on the front porch, a short private hall, bedroom 2 and a shared bath. On the north side: the kitchen (north-west, sink under the north window), a stair and future-elevator hub, the laundry, two walk-in closets, the ensuite and the primary bedroom (north-east, with a deck). The stair is one straight flight along the north wall. The basement is the same outline, with a hub, 2 bedrooms with egress windows, a flex room and a J&J bath on the north wall, and the office, rec room, theatre and gym on the south.


## 4. Pros, then cons

**Pros**

- **Under 3,000 with margin.** Heated footprint 2,940 sq ft (60 sq ft under); building area 335.6 m2 against 600 m2, fixes STR-04 (ABC Div. A 1.3.3.3 as cited in the review).
- **Simplest envelope.** Heated bar: 4 outside corners, 0 inside, 223 ft of centre-line perimeter, against 17 + 13 corners and 395.5 ft today (COST-08, K-069). One roof ridge against 16 hip blocks.
- **Daylight everywhere that matters.** Depth is 40 ft outside; kitchen, dining, living, both bedrooms, flex, office, and the gym have an outside wall with glass (K-007, K-097/098). Round 1's centre-dark rectangle (85.8 x 63.4 ft) is gone.
- **Laundry next to the suite.** 30.0 ft from the primary bed, through WIC B (was 103.1 ft; K-036, K-329).
- **Costco door.** The pantry shares 9.0 ft with the garage and has a 36 in door, level with the garage slab (K-037, K-115).
- **Circulation 10.1% strict** (was 16.2%); the open dining-living zone is the route west to east, and the private hall is 107 sf (K-316, ARC-07).
- **Code Blockers from the pool and basement cluster go away.** No pool: STR-02, STR-03, PLB-01 do not apply. CODE-01 is fixed: one flight, 19 risers, 3,581 mm against the 3.7 m maximum (ABC 9.8.3.3.(1), abc_2023 p.852).
- **Accessibility built in.** Elevator space stacked on both floors; all swing doors 36 in; halls 5.1 ft clear; flush showers; a stair 4.2 ft (1,280 mm) clear that can take a heavy-duty stair lift later.
- **Mechanical room on the west wall**, 35 ft from the septic side: two louvre windows on the wall for vents and combustion air (round 1 GAS-01).
- **Bedrooms are quiet.** No bedroom touches the living room, kitchen, garage or foyer; the nearest bedroom is 58 ft from the drive (K-005, K-325, K-328, K-335).

**Cons**

- **Several rooms are under the target sizes.** Primary bedroom 374 sf (66 under), living 346 (54 under), dining 260 (48 under), flex 144 (24 under), pantry 74 (6 under). The program does not fit 2,940 sq ft at full size.
- **Open concept.** Kitchen, dining and living are joined by an 8 ft and a 15 ft opening and no door: K-332 is CONTRADICTED, K-062 and K-324 are MISSING.
- **Living has windows on one wall** (south, 12 ft of glass in 18.5 ft). K-064 MISSING.
- **No library, no sunroom, no hot-tub sunroom.** K-032, K-034, K-185 to K-189 MISSING. The office is in the basement and shares a 19.5 ft wall with the rec room (K-031).
- **60 of 164 Kayla items MISSING**, including kitchen work triangle 41.9 ft against 26 (K-261), no dog wash (K-170), no broom closets (K-038), no sunken tub (K-220).
- **Long bar.** 73.5 ft east-west: the elevator and stair hub is about 50 ft by door path from the primary bed, and the west and east zones are joined on the south only by the living room and foyer (K-075 MISSING). Duct runs along the 73.5 ft length are for the HVAC designer.
- **Stair headroom is tight.** The main-floor opening is 11.5 ft long from the top nosing; clearance under the floor reaches 6.4 ft (about 1,950 mm) at 13 risers, so the opening and the floor depth are flagged for the licensed Alberta engineer and the designer. Not a stamped claim.
- **39 ft clear span.** The bar is 39 ft deep with no bearing line drawn: roof trusses and 18 in floor trusses need an interior bearing wall or a long-span design. For the engineer (STR-13 stays open).
- **The drive moves.** Garage doors face south, so the drive needs 2.0 ft of rise to the house-level slab: 12.5% over the 16 ft drawn. A longer drive (about 25 ft or more) is a site item. `site.scad` still shows the west drive.
- **Theatre has two outside walls** (not an interior room) and no windows.
- **STR-01 stays open:** basement walls are about 12 ft high (floor to floor 11.75 ft) with about 10 ft of backfill, against the Part 9 table limit of 3.0 m (review STR-01).

## 5. Kayla compliance (every item ARC classed PLAN)

Rulings used: a garage-wall closet counts as exterior; a drive that is only noted does not count (mine is drawn); a kitchen crossing needs a clear lane outside the work zone; a flush shower with a stated recess counts.

| K-ID | Verdict | Evidence | Change vs the current model |
|---|---|---|---|
| K-001 | IN | Kitchen, laundry, primary suite, bedroom 2 and a bath are all on the main floor; no stairs to reach them | same |
| K-002 | MISSING | Basement 2,940 sf has theatre and gym/music, but no pool (removed by the round-2 direction) | IN -> MISSING |
| K-003 | IN | 0 single doors under 36 in on either level (19 main, 14 basement, all 36 in); halls 5.1 ft clear or more | MISSING -> IN |
| K-004 | IN | Turning circles (5.6 ft) drawn in kitchen, foyer, laundry, shared bath, ensuite, basement bath; the powder (4.1 x 7.6 ft) has none | MISSING -> IN |
| K-005 | IN | Garage doors on the south wall; drive drawn as a porch strip at x 0-24; nearest bedroom (bedroom 2, x 82) is 58 ft east of it. The tool still reads the old west drive (14 ft) | CONTRADICTED -> IN |
| K-006 | MISSING | 8 wet-wall groups in 4 clusters (was 14); drain-run index 665 ft (was 879); kitchen, laundry and baths are not back to back | same |
| K-007 | IN | Kitchen, dining, living, bedrooms, flex, office and gym have windows; foyer, vestibule, pantry, mudroom, laundry and closets have none | MISSING -> IN |
| K-008 | IN | Bedrooms touch only halls, baths, closets, the ensuite; no kitchen, living or garage wall (matrix: 0 bedrooms share a wall with a living room) | MISSING -> IN |
| K-009 | IN | Guests reach kitchen, dining, living and powder without crossing the private hall; the primary suite and bedroom 2 hang off the foyer hall | MISSING -> IN |
| K-010 | MISSING | Bar is 72.5 x 39 ft (centre lines), not a 2 ft multiple; the 4.6 ft stair width and 5.5 ft hall are not either | same |
| K-012 | IN | Living (18.5 ft), dining (14 ft) and the front door face south; garage doors and the drive face south (drawn) | MISSING -> IN |
| K-013 | IN | Primary bedroom is the north-east block: north wall 20 ft, east wall 16 ft + 3.5 ft | same |
| K-014 | MISSING | Bedroom 2 and the primary bedroom both have east windows, but there is no sunroom (south-east) | same |
| K-021 | IN | Dining/nook opens 8 ft to the kitchen; nook table and banquette sit in the dining room | same |
| K-023 | IN | Dining has a 6 ft double door to a 14 x 12 ft covered patio (168 sf) for the BBQ; the dining opens 8 ft to the kitchen | MISSING -> IN |
| K-030 | MISSING | Pantry is 74 sf clear (target 80-96): shelves and an upright freezer, no room for small-appliance counters | same |
| K-031 | MISSING | Basement office 234 sf shares a 19.5 ft wall with the rec room (LIVING ROOM); no separate quiet wall | IN -> MISSING |
| K-032 | MISSING | No library: the office is the only study room, in the basement | same |
| K-033 | MISSING | Powder is at the front door; the mudroom entry is about 40 ft from it, the kitchen about 35 ft, the basement rooms use the J&J bath | same |
| K-034 | MISSING | No sunroom or screened porch drawn | IN -> MISSING |
| K-035 | IN | Kitchen and dining share an 8 ft full opening; no pantry or hall between | same |
| K-036 | IN | Laundry connects to primary closet B by a 3 ft door; 30.0 ft from the primary bed | MISSING -> IN |
| K-037 | IN | Pantry shares 9.0 ft with the garage and has a 36 in door to it, level with the garage slab | MISSING -> IN |
| K-038 | MISSING | No broom or vacuum closet is drawn on either level | same |
| K-040 | MISSING | No linen closet near bedroom 2 or the shared bath (the shared bath has no linen unit) | same |
| K-041 | IN | Vestibule 6.1 x 7.6 ft (46 sf) with an inner 36 in door | MISSING -> IN |
| K-043 | IN | Foyer drop shelf (4.7 ft) on the north wall; mudroom drop counter 3.5 ft | MISSING -> IN |
| K-044 | IN | Same foyer drop shelf, 3 ft high | MISSING -> IN |
| K-047 | IN | Mudroom bench 5.3 ft by lockers; foyer bench 4.2 ft | same |
| K-053 | IN | King bed 6.5 ft wide: 7.8 ft to the west, 5.3 ft to the east, 3.4 ft at the foot (room 19.6 x 19.1 ft clear) | same |
| K-055 | IN | Showers drawn flush (0.02 ft) in the ensuite, shared bath and basement bath; recessed floor flagged for the engineer | MISSING -> IN |
| K-058 | IN | Elevator space 6.0 x 7.4 ft incl. walls at x 42-48, y 27-34.4 on both floors, with a 5.5 x 7.4 ft approach | MISSING -> IN |
| K-059 | MISSING | No dumbwaiter shaft | same |
| K-060 | IN | Narrowest hall 5.1 ft clear (private hall and gallery) | MISSING -> IN |
| K-061 | IN | All swing doors are 36 in (19 main, 14 basement) | MISSING -> IN |
| K-062 | MISSING | Kitchen, dining and living are joined by an 8 ft and a 15 ft full opening with no door: only the service rooms and bedrooms are closed off | IN -> MISSING |
| K-064 | MISSING | Living has windows on one wall (south); kitchen (N/W), bedroom 2 (E/S) and primary (E/N) have two | same |
| K-069 | IN | Heated bar has 4 outside corners and 0 inside (was 17 + 13); perimeter 223 ft (was 395.5); with the garage 5 + 1 | MISSING -> IN |
| K-070 | IN | 0 of 3 closet-kind rooms (2 WICs, elevator) touch a yard or porch wall | CONTRADICTED -> IN |
| K-071 | IN | Both WICs are fully interior (north: laundry/ensuite; south: living/foyer) | MISSING -> IN |
| K-072 | MISSING | Ensuite WC is its own room; the shared bath has the shower at the far end, not toilet between shower and door | IN -> MISSING |
| K-074 | IN | No tub drawn: no tub on an exterior wall | CONTRADICTED -> IN |
| K-075 | MISSING | West service/kitchen zone and east bedroom zone are joined on the north side by a 19.5 ft band (hub, laundry, closets), but the living room and foyer sit between them on the south | CONTRADICTED -> MISSING |
| K-077 | IN | No room has windows on opposite walls | same |
| K-078 | MISSING | Not designed for cross-breeze diagonals | same |
| K-080 | MISSING | Living window (12 ft) is centred on its 18.5 ft wall | same |
| K-081 | MISSING | Kitchen west window (5 ft) has no overhang; the garage is beside it | same |
| K-083 | MISSING | Living 1.06, kitchen 1.09, primary 1.02; none inside 1.4-1.6 | same |
| K-095 | IN | Patio 12 ft (3.7 m) and front porch 12 ft deep: inside the 4-5 m limit | MISSING -> IN |
| K-096 | MISSING | Sink run is on the north (outside) wall under the window (K-124), range on the west (outside) wall | CONTRADICTED -> MISSING |
| K-099 | IN | Dining, living and front rooms face south; the kitchen is north | MISSING -> IN |
| K-100 | IN | Primary bedroom (E+N) and bedroom 2 (E+S) get morning light | MISSING -> IN |
| K-102 | MISSING | Powder door opens straight to a toilet 7 ft away; the ensuite WC door is off the bathing room | same |
| K-103 | MISSING | Powder door (x 72.8-75.8) is visible from the foyer | same |
| K-104 | IN | From the foyer opening (y 9-14) the east line hits the hall wall between the bedroom 2 door (y 3-6) and the bath door (y 14-17) | CONTRADICTED -> IN |
| K-105 | IN | Laundry door (x 54.5-57.5) is off the line of the living-room opening (x 48.2-53.3) | MISSING -> IN |
| K-106 | IN | Island 9.8 x 4.5 ft, no seating | same |
| K-107 | IN | Banquette plus 3 ft round table in the dining room | same |
| K-108 | IN | Island has no sink or cooktop | CONTRADICTED -> IN |
| K-114 | IN | Walk-in pantry 74 sf off the kitchen, with a freezer | same |
| K-115 | IN | Same as K-037 | MISSING -> IN |
| K-116 | IN | Garage to pantry to kitchen: two 36 in doors, 18 ft to the fridge | MISSING -> IN |
| K-117 | IN | Coffee counter 3.8 ft at the dining room's north wall beside the nook (no pot filler drawn) | MISSING -> IN |
| K-123 | MISSING | Island faces the dining room; the living room is 20 ft further east | same |
| K-124 | IN | Sink x 30-33 under the north window x 28-36 | same |
| K-127 | IN | 6 ft double door from the dining room to the covered patio | MISSING -> IN |
| K-128 | IN | 72 in round table with 3.8 ft of clear floor each side | same |
| K-129 | MISSING | 6 ft double door only; no multi-panel wall | same |
| K-132 | IN | Living 18.1 x 19.1 ft (346 sf) holds the sectional and two chairs | same |
| K-133 | MISSING | Living has windows to the porch, not a door; the dining room has the door | IN -> MISSING |
| K-134 | MISSING | Same as K-129 | same |
| K-140 | IN | Foyer bench 4.2 ft and mudroom bench | same |
| K-141 | IN | Closed 7 ft coat cabinet 4.5 ft wide in the foyer | MISSING -> IN |
| K-142 | IN | Same closed cabinet | MISSING -> IN |
| K-143 | IN | Foyer drop shelf and mudroom counter | MISSING -> IN |
| K-144 | IN | Front door looks north across the foyer to the coat wall; the kitchen is 50 ft away with no opening to the foyer | CONTRADICTED -> IN |
| K-145 | IN | Powder 4.5 x 8 ft beside the vestibule, 8 ft from the front door | MISSING -> IN |
| K-146 | IN | Mudroom bench 5.3 ft | same |
| K-147 | IN | Lockers 5.3 ft on the south wall | same |
| K-149 | IN | Lockers 7 ft high | same |
| K-151 | IN | Mudroom counter 3.5 ft at the garage door | same |
| K-153 | IN | Foyer drop shelf; mudroom counter | MISSING -> IN |
| K-155 | MISSING | Mudroom has no outside door; its only exit is the garage door and the dining door | same |
| K-156 | IN | Garage door into the mudroom, step-free (garage slab at house level) | same |
| K-157 | MISSING | Powder is about 40 ft from the mudroom | same |
| K-158 | IN | Laundry through the primary closet, 30.0 ft from the bed | MISSING -> IN |
| K-163 | IN | Laundry sink 2.9 ft counter drawn | same |
| K-166 | MISSING | No pass-through basket or chute between the closet and the laundry | same |
| K-170 | MISSING | No dog wash drawn | same |
| K-172 | MISSING | No litter spot drawn | same |
| K-179 | IN | Shared bath off the private hall; ensuite off the primary bedroom | same |
| K-183 | MISSING | No main-floor office; the office is in the basement | IN -> MISSING |
| K-185 | MISSING | No sunroom | same |
| K-186 | MISSING | No sunroom | IN -> MISSING |
| K-188 | MISSING | No sunroom | IN -> MISSING |
| K-189 | MISSING | No sunroom | same |
| K-191 | IN | 6 ft double door from the primary bedroom to a 16 x 11.5 ft deck | same |
| K-192 | IN | The only fireplace is in the living room | same |
| K-195 | IN | Primary bedroom 19.6 x 19.1 ft clear; bed 3+ ft clear on three sides | same |
| K-200 | IN | Two separate WICs, 65 sf each (7.1 x 9.1 ft) | same |
| K-201 | IN | WIC A opens from the bedroom; WIC B opens from WIC A, the laundry and the ensuite | same |
| K-202 | IN | WIC B also opens to the ensuite | same |
| K-203 | IN | WIC B opens to the laundry | MISSING -> IN |
| K-210 | MISSING | Laundry is through the closet, but no pass-through basket | same |
| K-211 | IN | Shower 5.0 x 4.3 ft, flush (0.02 ft); recess flagged for the engineer | MISSING -> IN |
| K-220 | MISSING | No tub drawn | same |
| K-224 | IN | Double vanity 6.3 ft | same |
| K-226 | MISSING | No towel storage drawn in the ensuite | IN -> MISSING |
| K-227 | IN | WC room 5.1 x 9.6 ft clear, 36 in door | MISSING -> IN |
| K-228 | IN | Ensuite to WIC B to laundry, 3 doors | MISSING -> IN |
| K-229 | IN | Door from the ensuite to WIC B | same |
| K-237 | IN | Basement flex 10.6 x 13.6 ft clear, egress window 4 x 3 ft | MISSING -> IN |
| K-238 | IN | Bedroom 2 14.1 x 11.1 ft clear holds a queen; basement bedrooms 11.6 x 13.6 ft | same |
| K-239 | MISSING | Bedroom 2 uses the shared bath off the hall; basement bedrooms share a J&J bath | IN -> MISSING |
| K-240 | MISSING | Bedroom 2 has no exterior door; it faces the south wall and the east wall only | same |
| K-242 | IN | Bedroom 2 plus basement bedrooms 3 and 4 and a flex room | MISSING -> IN |
| K-244 | IN | Basement J&J bath between bedrooms 3 and 4 (112 sf) | same |
| K-245 | IN | Bedroom 2 is 8 ft from the primary bedroom (the bath between), east light | MISSING -> IN |
| K-248 | IN | Front porch 35 x 12 ft under a roof | same |
| K-249 | MISSING | Mudroom has no outside door, so no covered entry | same |
| K-252 | IN | Patio 14 x 12 ft (168 sf) under a roof beside the dining room | same |
| K-253 | IN | Front porch 35 x 12 ft (420 sf) adjoins the patio | same |
| K-254 | MISSING | Every porch is roofed; no sun-only area | same |
| K-255 | MISSING | No desk or work spot drawn on a porch | IN -> MISSING |
| K-256 | IN | 3.0 ft of counter on each side of the range and the sink | same |
| K-257 | MISSING | No counter beside the fridge: the pantry door is on its east side | same |
| K-261 | MISSING | Fridge to sink 17.9 ft, sink to range 12.7 ft, range to fridge 11.3 ft = 41.9 ft (26 ft limit) | same |
| K-262 | IN | No opening from the foyer to the kitchen; the kitchen is first seen from the dining room | same |
| K-270 | MISSING | Fridge to sink 17.9 ft is about 7 steps | same |
| K-273 | MISSING | Fridge door swings toward the pantry door's landing | same |
| K-274 | IN | Dishwasher beside the sink; 5.8 ft (70 in) aisle to the island; west aisle 4.3 ft | MISSING -> IN |
| K-277 | IN | Sink under the north window | same |
| K-279 | IN | Island is 4.6 ft from the fridge as a landing zone | same |
| K-281 | IN | Island 44 sf clear of fixtures | same |
| K-282 | MISSING | Island centre is 12.4 ft from the fridge and 9.8 ft from the sink | same |
| K-283 | IN | 3.0 ft of counter each side of the range | same |
| K-288 | IN | Dishwasher drawn next to the sink | MISSING -> IN |
| K-290 | MISSING | Fridge is 11.3 ft from the range and 17.9 ft from the sink; it is at the pantry end of the kitchen, not at a counter run end | same |
| K-292 | MISSING | Fridge stands alone 5 ft from the first counter run | CONTRADICTED -> MISSING |
| K-297 | MISSING | No glass partition in the vestibule or foyer | same |
| K-298 | MISSING | Powder door opens directly into the foyer, not off a hall after storage | same |
| K-299 | MISSING | Looking north from the front door ends at the coat wall 11 ft away | IN -> MISSING |
| K-300 | MISSING | Same as K-299 | IN -> MISSING |
| K-302 | MISSING | Office is in the basement; the J&J bath is 40 ft away | same |
| K-304 | IN | WIC A opens from the bedroom | same |
| K-306 | IN | Primary bed head on the north wall between windows (x 79-83.5 and 92-96); basement beds on the west wall | CONTRADICTED -> IN |
| K-307 | MISSING | Primary north windows are 4 ft from the corners, not in them | same |
| K-315 | IN | Same as K-037 | MISSING -> IN |
| K-316 | IN | Circulation 284 sf = 10.1% strict (11.9% with the foyer), was 16.2% (21.9%) | CONTRADICTED -> IN |
| K-317 | IN | Rooms open off the living zone or the 5.5 ft hub; the only hall is the 107 sf private hall | MISSING -> IN |
| K-318 | IN | Kitchen is a dead end; garage to primary and laundry to bedroom paths use the dining, living and hub | same |
| K-320 | IN | Foyer drop shelf and bench, mudroom counter and lockers, pantry beside the garage | MISSING -> IN |
| K-323 | MISSING | Living south wall is 12 ft of glass in 18.5 ft | same |
| K-324 | MISSING | Dining and living share a 15 ft opening: one zone, no door | IN -> MISSING |
| K-325 | IN | No bedroom shares a wall with a living room, kitchen or garage | MISSING -> IN |
| K-326 | IN | Bedroom 2 is buffered by the hall and bath; the primary by closets, ensuite and hall | MISSING -> IN |
| K-328 | IN | No bedroom touches the foyer; the private hall is between | same |
| K-329 | IN | Laundry 30 ft from the primary bed by door path | MISSING -> IN |
| K-330 | IN | Primary to laundry goes through the closets, not the kitchen zone | same |
| K-331 | IN | Same as K-070 | CONTRADICTED -> IN |
| K-332 | CONTRADICTED | Kitchen, dining and living are all open to one another (8 ft and 15 ft openings, no doors) | IN -> CONTRADICTED |
| K-333 | IN | Closet A opens from the bedroom | same |
| K-334 | IN | 0 bedrooms share a wall with the living room | same |
| K-335 | IN | Garage doors south; the drive is drawn at x 0-24; nearest bedroom is 58 ft away | CONTRADICTED -> IN |

**Counts:** IN 103 / MISSING 60 / CONTRADICTED 1 (of 164). Current model: 62 / 89 / 13.

**Deal-breakers (12):**

| Deal-breaker | Verdict |
|---|---|
| Bedroom directly adjacent to foyer (K-328) | IN |
| Laundry far from bedrooms (K-329) | IN (30 ft) |
| Major path only through kitchen zone (K-330) | IN |
| Closets on exterior walls (K-331/K-070) | IN (0 of 3) |
| Full open concept (K-332) | **CONTRADICTED** |
| Through master bath to reach closet (K-333) | IN |
| Bedrooms sharing a wall with the living room (K-334) | IN |
| Garage at rear, drive past bedrooms (K-335/K-005) | IN |
| Laundry tied to master suite (K-036 + K-329) | IN |
| Costco door pantry to garage (K-037 + K-115) | IN |
| Wide doors and halls (K-003 + K-060 + K-061) | IN |
| No-threshold shower (K-055) | IN |

11 of 12 met.

## 6. Egress and accessibility table

**Basement egress** (ABC 9.9.10.1.(2), abc_2023 p.873: opening 0.35 m2 or more, no dimension under 380 mm; (3): 760 mm clear in front of a well window)

| Window | Rough opening, sill | Estimated clear opening | Well |
|---|---|---|---|
| Bedroom 3, x 56.5-60.5, y 39 | 4.0 x 3.0 ft, sill 3.5 ft | about 3.4 x 2.5 ft = 8.5 sf = 0.79 m2; smallest side 2.5 ft (762 mm) | 6.5 x 3.5 ft well, 1.07 m clear in front; about 6.7 ft deep, needs steps or a ladder, and any cover must open from inside (9.9.10.1.(5)) |
| Bedroom 4, x 76.5-80.5, y 39 | same | same | same, x 75-81.5 |
| Flex room, x 89.5-93.5, y 39 | same | same | same, x 88-94.5 |

The clear opening is the designer's estimate for one casement; confirm against the manufacturer's rated clear opening. Office and rec-room windows also have 3.5 ft wells (not egress).

**Turning circles (1,700 mm):** kitchen, foyer, laundry, shared bath, ensuite, basement J&J bath drawn; powder and WC room too narrow.

**Doors and halls:** 19 of 19 main-floor swing doors and 14 of 14 basement swing doors are 36 in; narrowest hall 5.1 ft clear (main), 5.1 ft (basement landing and east hall). Doubles: dining to patio 6 ft, primary to deck 6 ft; front door 3.5 ft.

**Elevator stack:** x 42-48, y 27-34.4 on both floors (same coordinates). Main floor: door on the east face into a 5.5 ft wide hall. Basement: door on the south face into a 7.1 ft hall. Framed as a closet with a door, labelled ELEVATOR (FUTURE).

**Stair:** straight, 19 risers of 7.42 in, 18 treads of 10.5 in, flight height 3,581 mm, clear width 4.2 ft (1,280 mm), top landing 4.6 x 4.2 ft opening onto a 10 ft wide hub, bottom landing 5.1 ft wide hall; handrails both sides in the 3D model; room for a heavy-duty stair lift later.

**Step-free route:** garage slab at house level (the old 1.5 ft drop and 3 steps are gone); the dining door opens level onto the patio; front porch at floor level with 4 steps down to grade (a ramp is a site item).

## 7. Cost drivers vs today's model

**$$$ down.** Repo research gives no whole-house $/sq ft (07-cost-ve.md header), so these are ranked.

1. **Basement and pool removed ($$$ down).** COST-01: the basement and pool cluster is the largest cost driver and the source of every structural Blocker. The basement shrinks from 3,617 to 2,940 sq ft and loses the pool, spa, theatre tiers and exit stair. Basement ceiling 10 ft instead of 12 ft also cuts ICF (COST-12: 1 ft of slab depth saves $9.8K-$14.1K).
2. **Heated footprint 2,940 against 5,685 sq ft ($$$ down):** 48% less floor; with one roof ridge and 4 corners against 30 (COST-08).
3. **Added items ($ up):** an elevator shaft framed now (no repo price, needs a quote), a 39 ft clear span (engineer), 5 window wells and 3 egress windows (no repo price; the window range is $850-$1,600 each, HR:434 as quoted in COST-09).

## 8. What you give up

The primary bedroom, living room and dining room all land 48-66 sq ft under your sizes, and there is no library, sunroom or hot-tub sunroom, to fit a 2,940 sq ft bar.

## 9. Departures

- **Site, septic, well, services:** none. The house stays inside x 0-130, y -16 to 70; the septic (x -3 to 3, y 52-64) is 25 ft or more from the garage and the bar's west wall (3.3 ft needed); the well (150, 75) and the west services entry are untouched.
- **Garage doors** turn from the west face to the south face; the drive is drawn as a strip (x 0-24, y -16 to 0) and `site.scad` is not edited. Cost: a new 384 sf apron; no repo price.
- **Utility room** moves to the basement west wall at y 19.5-39 (x 24-32), 35 ft from the drain-exit point (22.16, 58). Combustion air and vents go out through louvres on the west wall (GAS-01 needs a B149.1 check; not in the library).
- **Basement ICF wall height** (STR-01) is unchanged and still open.
