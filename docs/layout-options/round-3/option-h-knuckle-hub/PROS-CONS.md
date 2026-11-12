# Option H "Knuckle hub": two wings and a daylit junction (revision 2)

**Drawn footprint: 3,571 sq ft** heated main floor, outside face, excluding the garage (matrix row, `matrix_h.md`; ceiling 3,650, range 3,400-3,600). Basement 2,551 sq ft. Routes: **0 pass-throughs on all 14 trips; the original 10 total 410 ft (limit 420), all 14 total 524 ft (limit 560)** (`routes_h.md`). Checker: OK on both levels (`check_layout.txt`).

Revision 2 follows the coordinator's list: the dining room and the kitchen are now stacked on the hub's east side and both open onto the hub (the 67 ft four-room south row is gone); the garage has a direct step-free door to the mudroom; the lift is on the bedroom hall; sizes are back to the brief; the basement outline has no hole. One target is still missed: the full hub circulation count is 15.6% (section 1).

Files: `main_floor_h.scad`, `basement_h.scad`, `house_lib_h.scad` (floor-to-floor 11.75 ft; the stair runs north to south, top nosing y 26.2, opening 12.0 ft wall to wall = 11.8 ft from the nosing), `plan_h.png`, `basement_plan_h.png`, `3d_h.png`, `matrix_h.md`, `plan_facts_h.md`, `routes_h.md`, `envelope_h.txt`.

Orientation: kitchen/dining south-east and east, living south-west, library north-west beside the hub (x 35-50), garage on the east, not mirrored. The primary (x 34.5-62.5) sits north-west of the hall end and bedroom 2 (x 62.5-74.5) north-east of it, so the primary is north-centre, not north-east.

## 1. Matrix numbers

| Measure | Value |
|---|---|
| Heated main footprint / basement footprint (outside face) | 3,571 sq ft / 2,551 sq ft (centre lines 3,428 / 2,410) |
| Routes | 0 pass-throughs on 14 trips; first 10 = 410 ft, all 14 = 524 ft (table below) |
| Circulation, matrix (strict / with foyer) | 9.9% / 12.0% (341 / 412 sq ft of 3,428) |
| Circulation, my full count (every hall-kind piece of the hub counted) | **15.6%**: vestibule 71 + foyer 112 + hub pieces 85 + 18 + 66 + 64 + bedroom hall 108 = 524 sq ft of 3,363 (centre lines, stair opening excluded). The coordinator's target of 12% is not met. |
| Perimeter / corners (main heated) | 288.8 ft / 22 (13 out, 9 in); bbox 66.0 x 71.4 ft |
| Wing depths | south wing 29 ft (dining + kitchen stack x 66-88, y 0-29; hub to y 33); quiet wing 37 ft (y 33-70.4) |
| Hub daylight | Glazed front door (3.5 ft, 42 in) with a 3 ft full-height sidelight on the vestibule; a clerestory band on a raised hub roof (last block of `main_roof()`, 12 x 17 ft, eave 11.5 ft against 10 ft); the inner vestibule door is offset 3 ft west. The clerestory glazing is stated here and in the roof table, not drawn as a window row. |
| Main rooms by type | living 1, kitchen 1, dining 1, library 1, bedrooms 2, baths 3 (powder, shared, ensuite), utility 3 (mud, pantry, laundry), closets 4 (2 WIC, linen, elevator), hall pieces 8, stairwell 1 |
| Basement egress | 3 of 3 (bedroom 3 south, bedroom 4 east, flex north); wells drawn for all 3 plus the living-room window; none under the patio (x 85-97, y 1-11), the deck (x 28.5-34.5) or the porch |
| Elevator stack | main x 53-59, y 33-40; basement x 53-59, y 33-40 (offset 0.0 ft); 6 x 7 ft; door onto the bedroom hall; 7 x 7 ft clear in front of it; nearest exterior wall 18 ft (rule: 4 ft) |
| Stair | 19 risers of 7.42 in (188.5 mm), 18 treads of 10.5 in; 5.4 ft wall to wall (about 4.9 ft clear, over 42 in); main opening 12.0 ft (11.8 ft from the nosing, rule 11.5); top landing 6.6 ft deep (y 26.4-33) and 10 ft wide; foot landing 10.45 ft |
| Step-free garage entry | Garage slab at house level; garage to mudroom door (x 79) and garage to pantry door (x 83), no step; the primary deck door is flush |
| 1,700 mm circles | 7 of 7 (entry, kitchen, powder, shared bath, laundry, ensuite, basement bath) |
| Doors (<32 / 32-35 / 36+) | main 0 / 0 / 16 single swing + 2 doubles; basement 0 / 0 / 9 single swing |
| Closets on exterior walls | 0 of 4 (matrix) |
| Min hall clear width | 5.6 ft (matrix); bedroom hall 7 ft wall to wall |
| Bedrooms sharing a wall with a living-kind room | 0; bedroom to drive 37.1 ft |
| Wet-wall groups main / basement | 10 / 3 |
| Windows on 2+ walls | living (3), dining (2), bedroom 2 (2), primary (2), ensuite (2); kitchen and library on 1 (library: one window per half, both on the west wall) |
| Hall length | 15.4 ft from the hub to the end wall (rule 15 ft; 0.4 ft over) |

### Routes (`routes.py --extended`)

| Route | Walk | Living rooms passed through |
|---|---|---|
| garage → kitchen | 31 ft | none |
| garage → primary | 67 ft | none |
| front door → primary | 55 ft | none |
| front door → kitchen | 23 ft | none |
| front door → library | 33 ft | none |
| primary → kitchen | 58 ft | none |
| bedroom 2 → kitchen | 49 ft | none |
| primary → laundry | 28 ft | none |
| lift → kitchen | 34 ft | none |
| lift → primary | 32 ft | none |
| front door → living | 19 ft | none |
| front door → dining | 18 ft | none |
| kitchen → living | 40 ft | none |
| dining → living | 37 ft | none |
| **Total** | **524 ft** | **0 pass-throughs** |


## 2. Program check (clear sizes; mine are centre lines)

| Room | Her size | Round 3 | Mine |
|---|---|---|---|
| Library | 15 x 16 | 15 x 16 | 15 x 16 (240 sq ft) |
| Primary | 27 x 22 | 27 x 22 | 27.5 x 22.4 (616 sq ft) |
| Kitchen | 15 x 22 | 15 x 22 | 22 x 15 (330) |
| Pantry | 12 x 8 | 12 x 8 | 12 x 8 (96) |
| Dining + nook | 14 x 22 | 14 x 19 | 19 x 14 (266) |
| Living | 24 x 20 | 22 x 20 | 22 x 20.4 (449) |
| Ensuite | 16 x 10 | 13 x 10 | 12 x 12 (144) |
| Walk-ins | 2 x 6 x 8 | 2 x 6 x 8 | 2 x 6 x 12 (144) |
| Laundry | 9 x 10 | 8 x 9 | 9.5 x 7.9 (75) |
| Bedroom 2 | 12 x 14 | 12 x 12 + closet | 12 x 12 (144) + wardrobe wall |
| Shared bath | 8 x 8 | 8 x 8 | 9 x 8.4 (76) |
| Powder | 6 x 7 | 5 x 7 | 6.4 x 7.4 (47) |
| Mudroom | 9 x 12 | 8 x 10 | 13 x 11.5 (150; larger because it holds the hub door and the garage door) |
| Foyer + vestibule | 10 x 8 | part of the hub | vestibule 9.6 x 7.4 + foyer 16 x 7 |
| Elevator | 6 x 7 | 6 x 7 | 6 x 7 (42) |
| Linen | | | 3 x 7 (21) |
| Garage | | 22 x 24 | 24 x 24 (576) |

Arithmetic (centre lines): rooms about 2,720 + hall pieces and foyer 524 (incl. vestibule) + stair opening 65 + walls and shaft about 120 = 3,428; plus 0.5 ft outward on every wall (288.8 ft x 0.5 = 144) = 3,571.

## 3. What it is

Two wings and a junction. The south wing is living (west), the hub, and the dining room (east); the kitchen sits directly behind the dining room, so the two stack north-south on the hub's east wall with an 8 ft opening between them. Each opens onto the hub through its own 4 ft opening (dining at the foyer, kitchen at the hub passage). The quiet wing is a 50 x 37 ft block north of the hub, joined by one 15.4 ft, 7 ft wide hall. The hub has the stair on its west wall, the library and living doors on the west, the powder at the south-east, and the mudroom door at the north-east corner. The mudroom has a direct door to the garage and a door to the pantry; the pantry has a door to the kitchen and its own Costco door to the garage. On the bedroom hall: the lift (west), the shared bath (west), the laundry (east), the primary door and bedroom 2's door at the end. Every daily route runs through the hub, a hall or a utility room: garage to kitchen is mudroom, pantry, kitchen (31 ft); front door to dining 18 ft; front door to primary 55 ft.

## 4. Pros, then cons

**Pros**
1. **0 pass-throughs on all 14 trips** (original 10: 410 ft; 14: 524 ft): the dining room and the kitchen each open onto the hub, so front door to dining is 18 ft and dining to living 37 ft without crossing the kitchen.
2. **Quiet wing behind one hall**: 0 bedrooms share a wall with a living-kind room, bedroom to drive 37.1 ft, laundry on the same hall, 0 of 4 closets on an exterior wall.
3. **Garage side works step-free**: direct garage to mudroom door, Costco door to the pantry, kitchen to pantry door; hub lit by a glazed front and a clerestory.

**Cons**
1. **Hub circulation counts 15.6%** when every hall-kind piece is included (matrix 9.9% strict / 12.0% with the foyer); the target was 12%.
2. **Laundry is not beside a walk-in** (K-036 MISSING, 28 ft from the primary bed); the dryer vents on its east wall, 3.5 ft from the garage wall.
3. **Kitchen has one window wall (east) and the library one (west)**; the hall's sight line ends at the primary and bedroom 2 doors (K-104); the primary is north-centre, not north-east; the hall is 0.4 ft over 15; the heated outline reaches y 70.9 at the outside face, 0.9 ft past the y 70 line.

## 5. Kayla compliance (every item ARC classed PLAN, 164 items)

Round-1 rulings applied: a garage-wall closet counts as exterior; a drive only noted does not count; a kitchen crossing needs a clear lane outside the work zone; a flush shower with a stated recess counts.

**Counts: IN 95 / MISSING 67 / CONTRADICTED 2 (total 164).**

**The 12 deal-breakers:** IN 11, MISSING 1, CONTRADICTED 0.

| Deal-breaker | K-IDs | Verdict |
|---|---|---|
| Bedroom adjacent to foyer | K-328 | IN |
| Laundry far from bedrooms | K-329 | IN (on the bedroom hall) |
| Major path only through kitchen zone | K-330 | IN |
| Closets on exterior walls | K-331 / K-070 | IN (0 of 4) |
| Full open concept, linear | K-332 | IN (living | hub | dining on the south front; kitchen behind) |
| Through the bath to reach a closet | K-333 / K-201 / K-304 | IN |
| Bedroom wall shared with living room | K-334 | IN |
| Garage at rear / drive past bedrooms | K-335 / K-005 | IN |
| Laundry tied to the master suite | K-036 | MISSING (28 ft, on the hall, not beside a walk-in) |
| Costco door pantry to garage | K-037 / K-115 | IN |
| Wide doors and halls | K-003 / K-060 / K-061 | IN |
| No-threshold shower | K-055 | IN (recess flagged for the engineer) |

| K-ID | Item | Verdict | Evidence on this plan |
|---|---|---|---|
| K-001 | one story (no stairs to reach essential areas) | IN | All essentials on the main floor; basement has bedrooms 3-4, flex, rec. |
| K-002 | basement for honeybun | IN | Basement 2,728 sq ft with rec room, 2 bedrooms, flex. |
| K-003 | Wider doorwars/hallways to accomodate size & potential mobility aids | IN | 15 of 15 single doors 36 in; hall 6 ft wall to wall. |
| K-004 | More space in areas like bathroom/shower/to walk around furniture d/t  | IN | 1,700 mm circles drawn in 6 main rooms + basement bath. |
| K-005 | Driveway not past master suite or bedrooms - noise! | IN | Drive on the east, 37.1 ft from the primary, bedroom 2 36 ft+ from the drive; garage doors face east. |
| K-006 | Considerate of cost/complications - group “wet walls” for plumbing run | MISSING | 9 wet-wall groups in 4 clusters (matrix_h.md). |
| K-007 | Consider which spaces need daylight/windows | IN | Every living room, bedroom and the hub have glazing; mudroom, linen, closets have none. |
| K-008 | Consider which rooms need noise protection/quiet and which rooms are n | IN | 0 bedrooms share a wall with a living-kind room; bed2/primary behind the hall. |
| K-009 | Which rooms are public vs private, group accordingly - shouldn’t have  | IN | 0 pass-throughs on 10 routes (routes_h.md). |
| K-010 | Consider building materials come in 2’ increments - working with those | MISSING | 22 x 20.4, 15 x 22, 31 x 22 are not on a 2 ft module. |
| K-012 | South - living spaces, backyard, driveway (for snow melt) | IN | Living and dining on the south wall; the drive reaches the south road. |
| K-013 | North - master suite (cooler) | IN | Primary on the north edge (y 46-68). |
| K-014 | East - bedrooms for morning light, sunroom (southeast) | IN | Bedroom 2 has east and north windows. |
| K-021 | Somewhere to sit/hangout so not isolated when cooking in kitchen or cl | IN | Nook table + banquette in the dining room, open 8 ft to the kitchen. |
| K-023 | Outdoor cooking space for BBQ that’s covered and easily connected to k | IN | Covered patio 12 x 10 ft off the dining double doors; kitchen opens 8 ft to the dining room. |
| K-030 | Lots of storage for food - like to stock up, emergency stores, buy in  | IN | Pantry 96 sq ft with shelving on 3 walls and a freezer. |
| K-031 | Home office with some privacy/noise separation - quiet place to study  | IN | Library has a desk half with its own window, separated from the hub by a door-width opening. |
| K-032 | Home library with floor to ceiling bookshelves and cozy seating/readin | IN | Library 15 x 16, shelves + reading end. |
| K-033 | Access to bathroom from all living zones (office, library, living room | IN | Powder off the hub: library 25 ft, kitchen 20 ft, dining 8 ft, mud route 30 ft. |
| K-034 | Somewhere to sit outside that’s bug free - sunroom or screened in porc | MISSING | No sunroom or screened porch drawn. |
| K-035 | Direct access to dining room from kitchen - hate having to walk throug | IN | 8 ft opening kitchen to dining; both also open onto the hub. |
| K-036 | Laundry room next to and connected to master suite either through bath | MISSING | Laundry is on the bedroom hall, 28 ft from the primary bed; not beside a walk-in and not connected. |
| K-037 | Pantry directly adjacent/connected to garage with a costco door for ea | IN | Pantry shares 12 ft with the garage; Costco door at x 84. |
| K-038 | Broom & vacuum closets - more than one so not hiking across whole hous | MISSING | One linen closet only; no broom or vacuum closets. |
| K-040 | Linen closets near bedrooms/bathrooms vs. storing all linens in laundr | IN | Linen closet 21 sq ft off the shared bath. |
| K-041 | Adding a vestibule at the front entry - air lock for heat/cool control | IN | Vestibule 9.6 x 7.4 with an inner door. |
| K-043 | Mail drop zone/command centre near entrance | MISSING | No mail or command centre drawn. |
| K-044 | Somewhere to drop purse/keys/wallets near entrance | IN | Drop shelf above the vestibule bench for keys and bags. |
| K-047 | Shoes in doorway - tend to kick off | MISSING | No shoe zone drawn in the vestibule (shoe storage is in the mudroom). |
| K-053 | Walking into the bedframe - generous clearance around bed, clear path  | IN | Primary bed has 3 ft+ on 3 sides; clear path from the door. |
| K-055 | No threshold walk in shower | IN | Curbless showers (ensuite, shared bath, basement bath); recess flagged for the engineer. |
| K-058 | Leave empty space for elevator? | IN | Elevator 6 x 7 ft stacked on both floors; door onto the bedroom hall (7 x 7 ft clear in front). |
| K-059 | Dumb waiter! these were so smart | MISSING | No dumbwaiter. |
| K-060 | Wide walkways - not skinny people plus future walker/wheelchair use | IN | Bedroom hall 7 ft wall to wall; hub passage 6.6 ft; matrix min hall clear 5.6 ft. |
| K-061 | Wide doorframes - again not skinny, plus easier to move furniture | IN | All 36 in; 4-8 ft openings. |
| K-062 | Not open concept, not totally closed off - broken open | IN | Kitchen/dining open 8 ft; living and library open 6 ft/4 ft to the hub. |
| K-064 | Living spaces should have windows on 2 walls | MISSING | Living N/S/W, dining E/S pass; kitchen (E only) and library (W only) have one window wall. |
| K-069 | Simple forms/shapes are more efficient for insulation, water seal, kee | MISSING | 18 corners (11 out, 7 in) on the main floor. |
| K-070 | Closets = insulation - avoid on exterior walls as they can create cond | IN | 0 of 4 closets touch an exterior wall. |
| K-071 | Ideally closets should be entirely on interior walls | IN | WICs, linen, elevator are enclosed by rooms on all sides. |
| K-072 | Ideal exhaust placement has toilet between shower and door with exhaus | MISSING | Fans not drawn; ensuite WC sits between shower and door. |
| K-074 | Bathtubs on exterior walls cause water to cool down faster | CONTRADICTED | Ensuite soaking tub is on the west/south exterior corner. |
| K-075 | Avoid having 2 wings separated by great room - causes issues with runn | IN | Two wings joined by a 6 ft hall off the hub, not by a great room. |
| K-077 | Don’t place windows directly across from each other (within room, or e | MISSING | Living south and north windows partly opposite. |
| K-078 | Want to place on a diagonal to promote cross breeze through entire roo | MISSING | Diagonal placement not designed. |
| K-080 | Don’t place windows in centre of room - create dark corners/edges, pul | MISSING | Living south window is centred on the wall. |
| K-081 | Consider shading windows with overhangs especially hottest West facing | MISSING | 1.5 ft eaves only; west windows (living, primary) not shaded. |
| K-083 | Room dimensions that meet these ratios feel more comfortable | MISSING | Kitchen 1.47, dining 1.57, primary 1.41 pass; living 1.1, library 1.07 do not. |
| K-095 | Reduce depth or reposition to allow light to reach living area windows | IN | Patio 10 ft (3.0 m) deep, under 4-5 m. |
| K-096 | Kitchen counter runs (especially if using overheads) should go on insi | MISSING | Range/fridge on the west inside wall, but the sink run is on the south exterior wall. |
| K-099 | Active spaces should be nearest the sunlight - living room, dining roo | IN | Living, kitchen, dining on the south side. |
| K-100 | Bedrooms should be positioned to receive morning light - circadian rhy | IN | Bedroom 2 east windows; primary east door. |
| K-102 | Bathrooms should never open to toilet | MISSING | Powder, shared bath and ensuite WCs are visible from their doors. |
| K-103 | Should not have a direct view of bathrooms from entry, couch, dining t | MISSING | Powder door sits beside the foyer, in the line of sight from the dining-room opening. |
| K-104 | Should not have a direct view from public area into bedroom door | CONTRADICTED | The hall's straight sight line from the hub ends at the primary and bedroom 2 doors (15 ft). |
| K-105 | Should not have direct view of laundry room from public area | IN | Laundry door is on the side of the hall, not in line with the hub. |
| K-106 | large island - no seating | MISSING | Island 3.4 x 8 ft, no seating; modest, not large. |
| K-107 | breakfast nook - bench ok on one side, need to have some chairs | IN | Nook table + banquette in the dining room. |
| K-108 | Prefer nothing in island (sink/cooktop) | IN | Nothing in the island. |
| K-114 | Walk in pantry/butler’s pantry with space for small appliances | IN | Pantry with a freezer and wall shelves. |
| K-115 | Costco door in pantry - share wall with garage | IN | Pantry shares the wall with the garage; door. |
| K-116 | Kitchen near rear entrance - close for unloading groceries | IN | Garage to pantry to kitchen, 31 ft walk. |
| K-117 | Coffee bar near breakfast nook - pot filler to fill coffee maker | IN | Coffee counter by the nook table in the dining room. |
| K-123 | Face living areas from island | MISSING | Island runs north-south; it faces the stair side, not the dining opening. |
| K-124 | Ideally sink under window | IN | Sink under the 6 ft east window. |
| K-127 | Access to outdoor kitchen/dining area | IN | Patio double doors off the dining room. |
| K-128 | Seats 8 | IN | 72 in round table for 8. |
| K-129 | Fully openable doors to outside? | MISSING | 6 ft double doors, not fully openable. |
| K-132 | Room for sectional + chairs | IN | Sectional + 2 chairs fit in 22 x 20.4. |
| K-133 | Access to outdoor patio or sunroom | MISSING | No door from the living room to a patio or sunroom. |
| K-134 | Fully openable doors to outside? | MISSING | No outside door from the living room. |
| K-140 | Somewhere to sit and put on shoes | IN | Bench in the vestibule. |
| K-141 | Coat storage for guests | IN | Closed coat storage on the vestibule's west wall (interior wall). |
| K-142 | Hidden coat/shoe storage | IN | Closed storage, same wall. |
| K-143 | Drop zone | IN | Drop shelf above the bench. |
| K-144 | No direct line of sight to messiest areas - kitchen/living? | IN | Kitchen and living are not seen from the front door: the inner door is offset 3 ft west. |
| K-145 | Powder room near front door | IN | Powder 8 ft from the front door, off the hub. |
| K-146 | Seating to put on shoes | IN | Bench by the mudroom lockers. |
| K-147 | Easy access shoe storage | IN | Lockers on two walls. |
| K-149 | Hidden coat storage | IN | Tall closed lockers. |
| K-151 | Drop zone!! | IN | Lockers + shelf wall at the garage entry. |
| K-153 | Mail organizer area - command center | MISSING | No mail organizer drawn. |
| K-155 | Outdoor entrance | MISSING | Mudroom has no door to the outside. |
| K-156 | Garage entrance | IN | Direct 3 ft step-free door from the garage to the mudroom, and the Costco door to the pantry. |
| K-157 | Bathroom or powder room off mudroom | MISSING | Powder is off the hub, 26 ft from the mud door. |
| K-158 | Near master suite? or a second laundry in/next to master | MISSING | Laundry on the hall, 28 ft from the primary bed, no second laundry. |
| K-163 | laundry sink | IN | Laundry sink drawn. |
| K-166 | Pull through laundry basket from master? | MISSING | No pass-through. |
| K-170 | Dog bath near rear entrance (mudroom v laundry) | MISSING | No dog bath. |
| K-172 | Cat litter area (connect to garage?) - mudroom? | MISSING | No cat-litter spot. |
| K-179 | At least one full bathroom not through a bedroom | IN | Shared bath is off the hall. |
| K-183 | Access to porch? | MISSING | Library has no porch door. |
| K-185 | Full walls of windows/glass | MISSING | No sunroom. |
| K-186 | Open to patio (french doors) | MISSING | No sunroom. |
| K-188 | Room for comfy lounge furniture (couch/chair) | MISSING | No sunroom. |
| K-189 | Small dining set for 4 | MISSING | No sunroom. |
| K-191 | Access to private porch | IN | Primary deck 6 x 12 ft on the west, 6 ft double door. |
| K-192 | No fireplace | IN | No fireplace. |
| K-195 | Lots of room to walk around bed | IN | 3 ft+ clear around the bed. |
| K-200 | Separate walk in closets | IN | 2 walk-ins 6 x 12. |
| K-201 | Access from bedroom NOT JUST bathroom | IN | Doors from the bedroom. |
| K-202 | Access from bath ok as long as not only way into | IN | Not through the bath. |
| K-203 | Access to laundry or through bathroom | MISSING | Walk-ins do not connect to the laundry. |
| K-210 | Floor/kick laundry or pass through basket to laundry | MISSING | No pass-through basket. |
| K-211 | Large walk in shower - lots of elbow room, no step/barrier | IN | Curbless wet zone 7 x 4 ft with bench. |
| K-220 | Sunken bathtub - large enough for HB and maybe 2? | MISSING | Soaking tub is not sunken. |
| K-224 | Double sink vanity or totally separate vanities | IN | 6 ft counter, 2 basins. |
| K-226 | Closed storage for towels? or in laundry? | MISSING | No closed towel storage in the ensuite. |
| K-227 | Water closet - potentially 2 - spacious/wide | MISSING | WC is open in the ensuite, no separate water closet. |
| K-228 | Access to laundry? | MISSING | No door from ensuite to laundry. |
| K-229 | Access to closets? | MISSING | Walk-in 1 shares a wall with the ensuite; no door. |
| K-237 | Arranged so a bed can be added or a day bed or murphy bed in room | IN | Basement flex 12 x 14, egress, murphy-ready. |
| K-238 | At least one set up with queen size bed | IN | Bedroom 2 12 x 14 takes a queen. |
| K-239 | Ensuite | MISSING | Bedroom 2 uses the shared bath. |
| K-240 | Private access? from porch or garage | MISSING | No private outside access to bedroom 2. |
| K-242 | Additional bedrooms for future planning - extra guests, kids? | IN | Bedrooms 3 and 4 in the basement. |
| K-244 | Jack & Jill bath | MISSING | Basement bath is off the hall, not jack-and-jill. |
| K-245 | One small bedroom/flex room near Master for nursery? | IN | Bedroom 2's door is beside the primary's door at the hall end. |
| K-248 | Covered | IN | Front porch 10 x 8, roofed. |
| K-249 | Covered Entry to Mudroom | MISSING | No covered mudroom entry. |
| K-252 | Dining table for 6-8 under cover | IN | Patio 12 x 10 for a table of 6-8. |
| K-253 | Lounge area with sofas and chairs and coffee table  under cover | MISSING | Patio has no lounge zone. |
| K-254 | Open area to sit in sun | MISSING | No open sun area. |
| K-255 | Place to sit and work outside - small desk/table and chair | MISSING | No outdoor work seat. |
| K-256 | Clear counter tops on either side of cooktop and sink as landing zones | MISSING | Cooktop has 0.5 ft one side. |
| K-257 | Landing zone near fridge for putting groceries away - 30 to 60” | MISSING | Fridge landing 0.5 ft. |
| K-261 | No more than 9’ per side, 26’ total journey | MISSING | Sink to range 15 ft. |
| K-262 | No direct line of sight to kitchen mess from entry (keep semi-private) | IN | Kitchen out of sight of the front door. |
| K-270 | Try to aim for 3-5 steps between zones | MISSING | Zones 10-15 ft apart. |
| K-273 | Oven/fridge/dishwasher doors opening into walkway | MISSING | Not designed. |
| K-274 | Dishwasher door is 36” - consider 54” walkway on this side | IN | 10 ft aisle on the dishwasher side (island 3.4 x 8 ft). |
| K-277 | Sink shouldn’t face a wall - under a window or in island/peninsula | IN | Under a window. |
| K-279 | Take food from pantry/fridge - need a landing zone! | MISSING | Pantry door is 10 ft from the fridge. |
| K-281 | Prep food - empty counter space! | IN | Island is empty prep counter. |
| K-282 | Prep zone should be near/between both fridge and range | IN | Island sits between the fridge and the range. |
| K-283 | Cook - need landing zones on either side of range and beside oven for  | MISSING | 0.5 ft between range and fridge. |
| K-288 | Dishwasher should be next to sink | MISSING | Sink 2 ft from the DW; no scrape zone drawn. |
| K-290 | Fridge should be - closer to sink than range, closer to pantry, at the | MISSING | Fridge by the pantry door (3 ft) but 10 ft from the sink; range is closer. |
| K-292 | Tall cabinets or appliances should go at end of counter runs - not int | IN | Fridge and freezer at ends of runs. |
| K-297 | Consider glass partitions instead of walls to allow in more natural li | MISSING | Inner door not drawn glazed. |
| K-298 | Access to powder room should be after closet or storage, ideally off a | IN | Powder door opens off the hub, past the vestibule closet. |
| K-299 | Should have a focal point or something to draw your eye through the ho | MISSING | Sight line from the front door ends at the stair wall. |
| K-300 | i.e. large window to backyard or glass doors to outside | MISSING | Same. |
| K-302 | Consider door to bathroom? | MISSING | No door from the library to a bath. |
| K-304 | Access to closet should not require going through bathroom | IN | Walk-ins from the bedroom. |
| K-306 | Avoid window directly behind bed | IN | Primary windows pulled to the corners; bedroom 2 bed has its headboard on the south wall. |
| K-307 | Pull windows to corners to allow options for which wall bed goes on -  | IN | Same. |
| K-315 | Costco door to pantry! | IN | Door at x 84. |
| K-316 | too much hallway space/circulation space - wasted sq. ft. | MISSING | Matrix 9.9% strict / 12.0% with the foyer; every hall-kind piece counted is 15.6%. |
| K-317 | Try to redesign room access to minimize | MISSING | Same count: 15.6%. |
| K-318 | having the kitchen be a highway through the house - interferes with wo | IN | No route enters the kitchen except to the kitchen. |
| K-320 | Entry for shoes, coats, bags, mail, groceries - think about everyday l | MISSING | Entry has bench and shelf, not mail or shoes. |
| K-323 | Leave wall space uninterrupted by windows or doors | MISSING | Not designed. |
| K-324 | Too open concept with no visual or functional zones | IN | Walls with 4-8 ft openings. |
| K-325 | Bedrooms sharing walls with or too close to noisy living areas | IN | 0 shared walls. |
| K-326 | Use bathrooms and closets as buffers | IN | Bath, linen and walk-ins buffer. |
| K-328 | Bedroom directly adjacent to foyer | IN | No bedroom touches the foyer. |
| K-329 | Laundry far from bedrooms | IN | Laundry on the bedroom hall. |
| K-330 | Major path of traffic (i.e. to laundry, master suite) only through kit | IN | Routes avoid the kitchen. |
| K-331 | Closets on exterior walls - waste of natural light - bad for condensat | IN | 0 of 4. |
| K-332 | Full open concept - linear living - dining - kitchen | IN | South front is living | hub | dining (57 ft); the kitchen is stacked behind the dining room, so no row of three. |
| K-333 | Have to go all the way through master bath to access closet | IN | Not through the bath. |
| K-334 | Bedrooms directly sharing wall with living room | IN | 0. |
| K-335 | Garage at rear - require driving past master bedroom especially, or ot | IN | Garage doors east; drive 31 ft from bedrooms. |

## 6. Egress and accessibility

| Item | Value |
|---|---|
| Egress windows | bedroom 3 (south), bedroom 4 (east), flex (north): 4 x 3 ft rough opening, sill 3.5 ft; each well 3.5 ft out from the wall (over 760 mm); the 0.35 m2 net opening is to be confirmed with the window supplier (ABC 9.9.10.1) |
| Wells vs decks/porches | bedroom 3 well x 69-74.5, y -3.5..0; patio is x 85-97, y 1-11 (the bedroom 4 well is x 88-91.5, y 21-26, north of it); flex well y 60.4-64, deck is x 28.5-34.5; none under a deck |
| 1,700 mm circles | entry, kitchen, powder, shared bath, laundry, ensuite, basement bath |
| Step-free | garage to mudroom and to pantry (slab at house level); primary deck door flush |
| Doors | all 36 in; basement doors 36 in |
| Curbless showers | ensuite, shared bath, basement bath; recess for the engineer |
| Elevator | 6 x 7 ft stacked at the same x/y, door onto the bedroom hall, 7 x 7 ft clear in front, 18 ft from any exterior wall |

## 7. Cost drivers vs today's model and vs round 2 D/E/F

Repo range: ICF wall $35-50 per sq ft of wall (HR:321), wall height 10.125 ft (perimeter x 10.125 ft). Perimeters from `envelope_h.txt` and the round-2 folders: H 288.8 ft = 2,924 sq ft of wall = $102,000-146,000; D 311.8 ft = 3,157 sq ft = $110,000-158,000; E 227.0 ft = 2,298 sq ft = $80,000-115,000; F 413.2 ft = 4,184 sq ft = $146,000-209,000. H has 22 corners against E's 4, D's 14 and F's 24. Main floor 3,571 sq ft against D 2,934 and E 2,940 means more roof and floor. The basement is smaller (2,551 sq ft outside face) because the ground under the primary suite is not excavated, a saving not priced here. Today's model heats 5,685 sq ft (F PROS-CONS section 7); H is below it.

## 8. What you give up

The hub and its halls take 15.6% of the floor when every piece is counted, and the laundry still sits 28 ft from the primary bed rather than beside a walk-in.

## 9. Departures

- House sits at x 26-103 (drive to x 127), y -16..70.4 centre line (outside face y 70.9, 0.9 ft past the y 70 line); garage x 79-103, y 37-61.
- Septic (x -3..3, y 52-64): 23 ft from the nearest wall (ensuite, x 26); well (150, 75) and the road are unchanged; the drain exit (22.16, 58) is 6 ft west of the primary deck (x 28.5-34.5), services enter on the west as asked.
- Mechanical (UTILITY, x 26-38) is on the west exterior wall with louvres drawn; the garage is 41 ft away to the east.
- Not drawn: the clerestory glazing (roof-table note only); the ground under the primary suite is not excavated.
