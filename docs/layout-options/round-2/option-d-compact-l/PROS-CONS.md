# Option D: Compact L (round 2): pros and cons

Files: `main_floor_d.scad`, `basement_d.scad`, `house_lib_d.scad` (forked: `floor_to_floor()` = 11.75 ft; stair functions moved to this option's flight), `plan_d.png`, `basement_plan_d.png`, `3d_d.png`, `matrix_d.md`, `plan_facts_d.md`, `check_layout.txt` (both levels: OK).
Measured with `plan_facts.py --main main_floor_d.scad --basement basement_d.scad`. Road assumed south; land not chosen.

## 1. Matrix numbers

| Row | Option D |
|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED (of 164) | 109 / 52 / 3 (section 5) |
| Deal-breakers met (of 12) | 11 (missed: closets on exterior walls, K-331 / K-070) |
| Review Blockers fixed / open (of 6) | 5 / 1. Fixed: CODE-01 (one flight of 3,581 mm, under 3.7 m); STR-04 (330.4 m2 to the outside face against 600 m2, garage included); STR-02, STR-03, PLB-01 (the pool and its pit, pool-room span and drain-down are gone, not engineered). Open: STR-01 (basement wall 10.125 ft = 3.09 m against 3.0 m; was 3.70 m) |
| Circulation % (strict / with foyer) | 6.9% / 8.7% |
| Drain-run index (ft) / wet-wall groups / groups stacked over the basement | 587.2 ft (alternate exit 557.3) / 7 main, 4 basement / 3 of 7 within 5 ft of a basement group |
| Single doors under 32 in / 32-35 in / 36 in+ ; minimum hall clear width | 0 / 1 / 12 ; 5.60 ft (the 4.2 ft stair-top landing is the raw minimum) |
| No-threshold shower | Y (master and guest showers drawn flush, 0.02 ft; recessed floor flagged for the engineer) |
| Bedrooms sharing a wall with the living room | 0 |
| A bedroom next to the foyer | N |
| Master bed to laundry path | 23.5 ft |
| Master suite's side | North-east end of the private wing (north wall y 69.5, east wall x 105) |
| Bedrooms with east light | 2 of 2 main-floor bedrooms (bedroom 2 east window; primary east + north); basement bedroom 3 east, bedroom 4 west |
| Living spaces facing south | 3 of 3 (kitchen, dining + nook, living room) |
| Living spaces with windows on 2+ walls | 3: kitchen, living room, primary bedroom (dining has one) |
| Building area, outside face | 330.4 m2 against 600 m2 (house + attached garage; porches and drive excluded) |
| **Heated main-floor footprint excl. garage, outside face** | **2,934 sq ft** (centre lines 2,779) against 3,000: margin 66 sq ft (2.2%) |
| **Basement footprint, outside face** | **2,934 sq ft** (same outline; none under the garage or porches). Today: 3,617 |
| Main-floor room count by type | 23 heated rooms: kitchen 1, dining 1, living 1, bedrooms 2, bath-kind 4 (guest bath, master bath, WC, shower), closet-kind 5 (linen, elevator, bedroom 2 closet, two walk-ins), utility 3 (mudroom, pantry, laundry), hall-kind 5 (vestibule, foyer, hall, stair landing, suite hall), stairwell 1. Plus garage and 5 porch / drive rows |
| Basement bedrooms with compliant egress windows | 2 of 2 (bedrooms 3 and 4), plus the flex room (3 of 3 sleeping rooms) |
| Elevator stacked | Y: main x 88.4-94.4, y 21.6-29.0; basement x 88.4-94.4, y 21.6-29.0 (offset 0.0 ft) |
| Stair | 19 risers of 7.42 in; flight 141.0 in = 3,581 mm (limit 3,700); clear width 4.2 ft = 50 in; top landing 4.2 x 5.0 ft clear, foot landing 4.2 x 6.5 ft clear |
| Step-free garage entry | Y: garage slab at house level (z 0), the drive slopes up to it; garage to mudroom is one 3 ft door with no step |
| 1,700 mm circles shown in kitchen, baths and laundry | 5 of 5 on the main floor (kitchen, foyer, guest bath, master bath, laundry) and 2 of 2 basement baths |
| Basement / shop / site changes | Basement redrawn under the new outline (no pool, spa, theatre, light wells or exit stair); no shop change; site: drive moves from the west to the south side (departure, section 9) |
| Cost vs today's model | $$$ down (section 7) |

## 2. Program check

Clear sizes are centre-line size minus 0.4 ft (`plan_facts_d.md` section 3).

**Main floor**

| Room | Target clear | Mine (clear) | Area sf |
|---|---|---|---|
| Kitchen | 15 x 22 (330) | 15.0 x 21.2 | 318 |
| Dining + nook | 14-16 x 22 (308-352) | 13.8 x 21.2 | 293 (short of 308 by 15) |
| Pantry | 8 x 10-12 (80-96) | 8.0 x 9.6 | 77 |
| Living | 400-480 | 19.6 x 21.2 | 416 |
| Primary bedroom | 440-528 | 21.6 x 19.5 | 421 (short of 440 by 19) |
| Primary ensuite | 170-228 | master bath 8.6 x 12.0 + WC 4.2 x 7.1 + shower 4.0 x 7.1 | 103 + 30 + 28 = 161 (short of 170 by 9) |
| Primary closets | 2 walk-ins, each >= 7 x 8 | 7.6 x 8.0 and 8.2 x 8.0 | 61 and 66 |
| Primary laundry | >= 8 x 9 | 8.0 x 8.0 | 64 (one foot short in depth) |
| Bedroom 2 | ~12 x 12 + closet | 11.4 x 11.8 + closet 5.4 x 7.0 | 135 + 38 |
| Shared full bath | ~8 x 10 | 7.6 x 9.6 | 73 |
| Powder room | ~5 x 7 | none: the guest bath off the foyer doubles as the powder room | (73) |
| Mudroom | ~8 x 12 | 8.0 x 11.2 | 90 |
| Foyer + vestibule | vestibule ~6 x 8 + foyer | vestibule 5.6 x 7.6; foyer 5.6 x 13.2 | 43 + 74 |
| Office / library | optional, upstairs only if <= 3,000 | in the basement (below) | |
| Elevator (future) | 6 x 7 incl. walls | 6.0 x 7.4 centre to centre | 44 |
| Stair | straight, 19 risers, >= 42 in | 4.2 ft clear, 11.5 ft opening | 53 |
| Garage | 2 cars, >= 22 x 24 | 24.0 x 24.0 | 576 (not counted) |
| Porches (not counted) | covered BBQ / outdoor dining | back patio 41.8 x 12.4 (518 sf), front porch 102, mud stoop 24, primary deck 112 | |

Main floor totals: 23 heated rooms, 2,779 sq ft centre line (2,726 without the stair opening); 2,934 sq ft outside face. Garage 595 sq ft centre line.

**Basement** (10 ft ceiling)

| Room | Target | Mine (clear) | Area sf |
|---|---|---|---|
| Bedroom 3 | ~12 x 13 + closet | 11.4 x 11.7 + closet 11.4 x 7.0 | 134 + 80 |
| Bedroom 4 | ~12 x 12 + closet | 11.4 x 11.7 + closet 11.4 x 7.0 | 134 + 80 |
| Baths | Jack & Jill ~8 x 10, or 2 baths | 2 baths: 7.2 x 9.2 (under the guest bath) and 7.6 x 7.6 (stair foot) | 67 + 58 |
| Flex / craft | ~12 x 14 | 11.0 x 11.8 with egress window | 130 |
| Office / library | ~240 | 15.6 x 12.8 | 200 |
| Rec / family room | ~16 x 20 | 18.0 x 20.5, labelled LIVING ROOM | 369 |
| Theatre | optional | dropped | |
| Gym / music | ~12 x 16 | 12.6 x 12.8 | 162 |
| Mechanical / utility | ~10 x 12 | 9.8 x 11.2, with the sewage ejector pit | 111 |
| Storage | as space allows | 6 rooms | 87 + 113 + 91 + 21 + 26 + 19 |
| Elevator stop + stair foot | aligned | elevator 6.0 x 7.4 at the same x/y; stair foot room x 77.8-82.4, y 42.75-49.6 | 44 + 27 |

Basement totals: 28 rows (25 rooms and 3 window wells), 2,779 sq ft centre line.

**Dropped or shrunk to make 3,000 fit:** theatre (dropped); powder room (merged into the foyer bath); tub (dropped; no tub in either primary or guest bath); separate library (one office / library); sun room and hot-tub sunroom (none; a future addition outside the 3,000). Shrunk: dining nook room, primary bedroom, ensuite, laundry (by 1 ft), pantry, bedroom 2 (by 9 sq ft), shared bath. Every shortfall is under 8% of its target.

## 3. What it is

K-088's ranch pattern, drawn compact: an L with a public wing and a private wing meeting at a foyer / stair / elevator hub, and a private back patio in the elbow. The public wing runs east from the garage along the south (road) side, 21.6 ft deep: garage (doors to the road, slab at house level), mudroom and pantry (Costco door to the garage), kitchen, dining + nook, living room, then the vestibule and foyer at the east end. From the foyer a 6 ft hall runs north (the private wing, x 74-105, up to y 69.5). On it are the stair (4.2 ft clear, one straight flight of 19 risers running north under the suite laundry), the stacked 6 x 7 ft elevator closet, the linen closet, bedroom 2 on the east wall with its walk-in, and at the north end the primary suite behind a short suite hall: bedroom (north and east windows, deck), curbless ensuite with a separate WC room, two walk-ins and the laundry. The 518 sq ft covered patio sits in the elbow, north of the kitchen, dining and living room, west of the stair, with doors from the dining and living rooms. The basement is under the same outline: family room, office / library, gym / music, utility on the west end, bedrooms 3 and 4 and a flex room with egress windows, two baths, storage.

Shape: a south bar (garage at the west end, then mudroom / pantry, kitchen, dining, living room, foyer) with a 31 ft wide private wing rising from its east end, and the back patio in the notch between them (see `plan_d.png`).

Changes from today's model: heated main floor 5,486 -> 2,779 sq ft (centre line); basement 3,475 -> 2,779; garage doors and drive to the south; stair one straight flight, runs north; no pool, spa, theatre, office, study, sun room, bunk room, den.

## 4. Pros and cons

**Pros**
1. **Under the target with margin.** 2,934 sq ft outside face against 3,000 (66 sq ft), from 5,685 today (`matrix_d.md`).
2. **No room is deep.** The wings are 21.6 ft (public) and 22-31 ft (private) deep, so every bedroom, living room, kitchen and dining room has an exterior wall and a window (K-097 / K-098; K-007).
3. **Quiet bedrooms.** 0 bedrooms share a wall with the living room (K-334, K-008, K-325); bedroom 2 is buffered by two walk-ins and the primary suite is behind its own hall.
4. **Garage entry fixed.** Garage doors face the road, the drive is 70 ft from the nearest bedroom (K-005 and K-335, today CONTRADICTED); a 3 ft Costco door joins the pantry to the garage at house level (K-037 / K-115, ARC-03).
5. **Laundry in the suite:** 23.5 ft from the primary bed, through the ensuite or the suite hall (K-036; today 103.1 ft; ARC-02).
6. **Accessibility is built in.** One straight flight, 3,581 mm, no landing (ABC 9.8.3.3.(1)); a 6 x 7 ft elevator closet stacked on both levels; 0 single doors under 32 in; halls 5.6 ft; flush showers; 1,700 mm circles in the kitchen, foyer, both main baths and the laundry.
7. **Less hall:** strict circulation 6.9% (today 16.2%; K-316).
8. **Shorter plumbing:** 7 wet-wall groups (today 14), drain-run index 587 ft (today 879), the guest bath stacked over a basement bath.
9. **Basement cost falls:** 2,779 sq ft centre line, 10 ft ceiling (COST-01, COST-12 in the repo's cost findings), no pool pit.

**Cons**
1. **Three closets touch exterior walls** (K-070, K-331, a deal-breaker, CONTRADICTED): the linen closet, bedroom 2's closet and one primary walk-in (matrix_d.md). Moving them inboard grows the footprint, which is at 2,934 of 3,000.
2. **Kitchen is on the garage-to-house path.** The mudroom opens onto the kitchen, so groceries and the walk to the private wing cross the kitchen; only the clear 8 ft lane north of the island keeps it out of the cooking zone (K-318, K-330 are scored IN on that lane).
3. **Front door looks at the suite door.** The 6 ft hall puts the primary suite hall door in line with the front door, 41 ft away (K-104 CONTRADICTED; K-299 / K-300 MISSING).
4. **Patio faces north.** The elbow patio is under a roof on the north side: no unroofed sun area (K-254), and K-012 wants the backyard south.
5. **Bedroom 2 has no ensuite and no outside door** (K-239, K-240, K-244 MISSING); the shared bath is off the foyer (K-298, K-102, K-103 MISSING).
6. **Basement office shares a wall with the gym / music room** (K-031).
7. **Small rooms:** laundry 8 x 8 ft (8 x 9 asked), ensuite 161 sq ft (170), primary bedroom 421 (440), dining 293 (308).
8. **Linear public wing:** kitchen, dining and living room are in a row (K-332 scored IN on 9 ft and 6 ft openings).
9. **STR-01 still open:** the basement wall is 3.09 m high against 3.0 m.

## 5. Kayla compliance

All 164 PLAN items from `findings/01-architecture-flow.md`, scored on the round-1 rulings (a garage-wall closet is exterior; a noted but undrawn drive does not count; a kitchen crossing needs a clear lane outside the work zone; a flush shower with a stated recess counts). "Change" is against today's verdict.

| K-ID | Verdict | Evidence | Change vs today |
|---|---|---|---|
| K-001 | IN | Kitchen, laundry, primary suite, bedroom 2 and a bath are all on the main floor; the stair is optional | same |
| K-002 | IN | Basement under the same outline, 2,934 sq ft outside face | same |
| K-003 | IN | 0 single doors under 32 in, 1 at 32-35, 12 at 36+; halls 5.6 ft clear (matrix_d.md) | MISSING -> IN |
| K-004 | IN | 1,700 mm circles drawn in kitchen, foyer, guest bath, master bath, laundry; master bath 112 + WC 34 + shower 33 sf | MISSING -> IN |
| K-005 | IN | Garage doors face the road; the drive (DRIVE strip x 0-24.4, y -16..0) is drawn south, 70 ft from BEDROOM 2 (computed); the site model's west drive is not used: a site departure | CONTRADICTED -> IN |
| K-006 | IN | 7 wet-wall groups on the main floor (was 14) in 3 clusters; master bath + laundry back to back; guest bath stacked over the basement bath; 3 of 7 within 5 ft of a basement group | MISSING -> IN |
| K-007 | IN | Every bedroom, living, dining, kitchen, laundry, office has a window; windowless: foyer, vestibule, halls, closets, pantry | MISSING -> IN |
| K-008 | IN | 0 bedrooms share a wall with a living room; bedroom 2 touches hall, closets and walk-ins only | MISSING -> IN |
| K-009 | IN | Public wing is reached from the foyer; the private wing is one hall (6 ft) north of the foyer; nobody crosses a bedroom | MISSING -> IN |
| K-010 | MISSING | Rooms are 22.0, 15.4, 14.2 ft centre to centre: not on a 2 ft module | same |
| K-012 | MISSING | Kitchen, dining, living, drive south; but the back patio is in the north elbow (K-088 pattern), not south | same |
| K-013 | IN | Primary suite at the north-east end (y 49.6-69.5), north and east walls exterior | same |
| K-014 | MISSING | Bedroom 2 and the primary have east windows; no sun room (a hot-tub sunroom is a future addition outside the 3,000) | same |
| K-021 | IN | Nook with L-banquette in the dining room, open 9 ft to the kitchen | same |
| K-023 | IN | Dining double door (6 ft) and living double door to the covered 518 sf back patio; patio door is 8 ft from the kitchen opening | MISSING -> IN |
| K-030 | IN | Pantry 84 sf with counter, shelves and upright freezer, plus 328 sf of basement storage | MISSING -> IN |
| K-031 | MISSING | Basement OFFICE / LIBRARY 218 sf shares a 13.6 ft wall with GYM / MUSIC | IN -> MISSING |
| K-032 | MISSING | One combined OFFICE / LIBRARY, 218 sf, in the basement | same |
| K-033 | MISSING | Guest bath is off the foyer; the mudroom is about 60 ft from it by door path (mudroom, kitchen, dining, living, foyer); the basement office is farther | same |
| K-034 | MISSING | No sun room or screened porch; the covered patio is open to bugs | IN -> MISSING |
| K-035 | IN | 9 ft opening kitchen to dining, no hall or pantry between | same |
| K-036 | IN | LAUNDRY off the suite hall and the master bath; 23.5 ft from the bed (was 103.1) | MISSING -> IN |
| K-037 | IN | PANTRY shares 10.0 ft with the garage, 1 Costco door (3 ft), slab at house level | MISSING -> IN |
| K-038 | MISSING | One LINEN closet (12 sf) and an under-stair closet; no broom/vacuum closet in the mudroom or kitchen | same |
| K-040 | IN | LINEN at the stair on the bedroom hall, 11 ft from bedroom 2's door | MISSING -> IN |
| K-041 | IN | VESTIBULE 6 x 8 ft (48 sf) with a double outer door | MISSING -> IN |
| K-043 | IN | Foyer console (1.4 x 4 ft) and the mudroom mail/drop counter | MISSING -> IN |
| K-044 | IN | Same console by the front door | MISSING -> IN |
| K-047 | IN | Vestibule coat wardrobe and the foyer cabinet (7 ft); mudroom bench and lockers | same |
| K-053 | IN | King bed 6.2 ft wide in a 22 ft room: 7+ ft each side, head on the north wall; 3 ft to the foot bench | same |
| K-055 | IN | Master shower and guest shower drawn flush (0.02 ft); a recessed floor is an item for the licensed engineer | MISSING -> IN |
| K-058 | IN | ELEVATOR (FUTURE) closet 6.0 x 7.4 ft at x 88.4-94.4, y 21.6-29.0, stacked on both levels; 5 x 5 ft approach in the 5.6 ft hall | MISSING -> IN |
| K-059 | MISSING | No dumbwaiter shaft | same |
| K-060 | IN | Hall 5.6 ft clear (6.0 centre to centre), suite hall 5.6; the stair-top landing is 4.2 ft (a landing, not a walkway) | MISSING -> IN |
| K-061 | IN | All 13 single doors are 36 in or the one 32-35 in (wc, 2.8 ft); cased openings 4-6 ft | MISSING -> IN |
| K-062 | IN | Kitchen/dining 9 ft opening, dining/living 6 ft, living/foyer 6 ft: broken open, not one room | same |
| K-064 | MISSING | Windows on 2 walls: kitchen, living, primary bedroom only (3 rooms); dining, bedroom 2 have one | same |
| K-069 | MISSING | Heated outline has 10 outside and 6 inside corners (was 17 + 13), perimeter 318 ft: better, not simple | same |
| K-070 | CONTRADICTED | Exterior-wall closets: LINEN (2.7 ft W), BR 2 CLOSET (3.8 S + 7.4 E), WIC @96.4 (4.8 S + 8.4 E) (matrix_d.md) | same |
| K-071 | MISSING | 3 of 5 main closets touch an exterior wall; WIC @88.4 is interior | same |
| K-072 | MISSING | Not designed for: guest bath toilet is not between shower and door | IN -> MISSING |
| K-074 | IN | No bathtubs drawn (tub dropped to save area), so none on an exterior wall | CONTRADICTED -> IN |
| K-075 | IN | Private wing is joined to the public wing at the foyer hall, not separated by the living room | CONTRADICTED -> IN |
| K-077 | IN | Kitchen S window x 34.5-39.5 and N window x 43.5-47; living S x 70-80 and N x 63-68: no pair is across from each other | same |
| K-078 | IN | Kitchen and living windows are on diagonals (S west / N east; S east / N west); other rooms not designed for it | MISSING -> IN |
| K-080 | MISSING | Kitchen sink window centred on the sink run; master windows are pulled to the corners | same |
| K-081 | MISSING | West windows: laundry 3 ft, master bath 3 ft, no overhang | same |
| K-083 | MISSING | Kitchen 1.40 and dining 1.52 are in 1.4-1.6; living 1.08, master 1.11, bedroom 2 1.03 are not | same |
| K-095 | IN | Patio roof is 12.4 ft (3.8 m) deep, front porch 8 ft: inside the 4-5 m limit; south living windows have no porch in front | MISSING -> IN |
| K-096 | MISSING | Both counter runs (south sink run, north fridge/tall run) are on exterior walls; only the pantry-door wall is interior | CONTRADICTED -> MISSING |
| K-099 | IN | Kitchen, dining and living face south; they open to the north patio as well | MISSING -> IN |
| K-100 | IN | Bedroom 2 east; primary east and north | MISSING -> IN |
| K-102 | MISSING | Guest bath toilet is visible from its door (NE corner, 8 ft); master WC is its own room | same |
| K-103 | MISSING | Guest bath door opens off the foyer, in view of the front door | same |
| K-104 | CONTRADICTED | The front-door axis runs north up the 6 ft hall to the suite-hall door at y 41.2, 41 ft away: the door to the primary suite is in line | same |
| K-105 | IN | Laundry door is inside the suite hall, not visible from a public room | MISSING -> IN |
| K-106 | IN | Island 8 x 3.5 ft, no stools | same |
| K-107 | IN | L-banquette on two walls plus a table; chairs on the other sides | same |
| K-108 | IN | Island has no sink or cooktop; the sink is on the south run | CONTRADICTED -> IN |
| K-114 | IN | Pantry 84 sf with a 6.4 ft small-appliance counter, shelves, freezer | same |
| K-115 | IN | Same as K-037 | MISSING -> IN |
| K-116 | IN | Garage door to the mudroom 3 ft; mudroom opens 4 ft to the kitchen: garage to kitchen centre 30 ft | MISSING -> IN |
| K-117 | IN | Coffee counter on the dining south wall, 4 ft from the nook table | MISSING -> IN |
| K-123 | MISSING | Island faces the dining room end-on; no living-area sightline from the island | same |
| K-124 | IN | Sink x 35.7-38.7 on the south wall, window x 34.5-39.5 | same |
| K-127 | IN | Dining double door to the covered patio | MISSING -> IN |
| K-128 | IN | 72 in round table for 8 (dining 14 ft wide) plus the nook | same |
| K-129 | MISSING | 6 ft double doors, no multi-panel or folding wall | same |
| K-132 | IN | Living room 416 sf clear holds the sectional and two swivel chairs | same |
| K-133 | IN | Living double door to the covered patio (and dining beside it) | same |
| K-134 | MISSING | Same as K-129 | same |
| K-140 | MISSING | No bench in the vestibule or foyer (wardrobe takes the wall); the bench is in the mudroom | IN -> MISSING |
| K-141 | IN | Vestibule wardrobe 4.4 ft and foyer cabinet 4.9 ft, both 7 ft high and closed | MISSING -> IN |
| K-142 | IN | Same, closed | MISSING -> IN |
| K-143 | IN | Foyer console and mudroom drop counter | MISSING -> IN |
| K-144 | IN | Front-door axis runs up the hall; the kitchen is not in view; the living room is seen sideways through a 6 ft opening | CONTRADICTED -> IN |
| K-145 | IN | Guest bath is 15.4 ft from the foyer centre, doubles as the powder room | MISSING -> IN |
| K-146 | IN | Mudroom bench 4.2 ft by the garage door, lockers 5 ft | same |
| K-147 | IN | Mudroom lockers and the vestibule wardrobe | same |
| K-149 | IN | Lockers 7 ft high; vestibule wardrobe | same |
| K-151 | IN | Mudroom counter 3 ft high by the garage door | same |
| K-153 | IN | Foyer console; mudroom mail counter | MISSING -> IN |
| K-155 | IN | Mudroom door (3 ft) to the covered MUD STOOP (24 sf) | MISSING -> IN |
| K-156 | IN | Garage door into the mudroom, step-free | same |
| K-157 | MISSING | No bath off the mudroom | same |
| K-158 | IN | See K-036 | MISSING -> IN |
| K-163 | IN | Laundry sink on the west wall | same |
| K-166 | MISSING | No pass-through basket | same |
| K-170 | MISSING | No dog wash | same |
| K-172 | MISSING | No litter area | same |
| K-179 | IN | Guest bath off the foyer, not through a bedroom | same |
| K-183 | MISSING | Office is in the basement, no porch | IN -> MISSING |
| K-185 | MISSING | No sun room | same |
| K-186 | MISSING | No sun room (living and dining have 6 ft double doors to the patio) | IN -> MISSING |
| K-188 | MISSING | No sun room | IN -> MISSING |
| K-189 | MISSING | No sun room (patio table seats 6 under cover) | same |
| K-191 | IN | Primary double door (6 ft) to the 112 sf private DECK | same |
| K-192 | IN | No fireplace in the primary | same |
| K-195 | IN | Primary 438 sf; bed 7+ ft from each side wall | same |
| K-200 | IN | Two walk-ins, 67 and 72 sf, side by side | same |
| K-201 | IN | Both walk-ins open from the bedroom; the bath has no door to them | same |
| K-202 | IN | Same | same |
| K-203 | IN | Laundry reached from the ensuite and the suite hall | MISSING -> IN |
| K-210 | IN | Laundry beside the walk-in row and off the ensuite | MISSING -> IN |
| K-211 | IN | Shower 3.8 x 6.7 ft (25 sf) flush with the floor | MISSING -> IN |
| K-220 | MISSING | No tub drawn | same |
| K-224 | IN | Double vanity 6 ft | same |
| K-226 | MISSING | No closed towel storage in the master bath; the LINEN closet is on the hall | IN -> MISSING |
| K-227 | MISSING | One WC room (4.2 x 7.1 ft clear), not two | same |
| K-228 | IN | Ensuite door to the laundry | MISSING -> IN |
| K-229 | MISSING | The walk-ins open off the bedroom, not the bath | IN -> MISSING |
| K-237 | IN | FLEX / CRAFT 144 sf in the basement with an egress window, Murphy-bed ready | MISSING -> IN |
| K-238 | IN | Bedroom 2 11.4 x 11.8 ft clear, queen fits | same |
| K-239 | MISSING | Bedroom 2 has no ensuite: the shared bath is off the foyer | IN -> MISSING |
| K-240 | MISSING | Bedroom 2 has no outside door | same |
| K-242 | IN | Three non-master bedrooms: bedroom 2 plus basement BEDROOM 3 and 4 | MISSING -> IN |
| K-244 | MISSING | No Jack & Jill: basement bedrooms 3 and 4 share the BATH at the stair foot, not a J&J | IN -> MISSING |
| K-245 | IN | Bedroom 2 shares walls with the two primary walk-ins; 11 ft door to door | MISSING -> IN |
| K-248 | IN | FRONT PORCH 102 sf roofed (8 ft deep) | same |
| K-249 | IN | MUD STOOP 24 sf under a roof block | MISSING -> IN |
| K-252 | IN | Patio (518 sf, roofed) holds a 6 ft round table for 6-8 | same |
| K-253 | IN | Two sofas on the roofed patio | same |
| K-254 | MISSING | The whole patio is roofed; no open sun area | same |
| K-255 | IN | Small desk on the patio | same |
| K-256 | IN | Sink: 2.5 ft counter west, dishwasher then 3 ft counter east; range: 3 ft west, 1.3 ft east (15 in) | same |
| K-257 | MISSING | Fridge has only tall cabinets beside it; no 30-60 in counter landing next to it | same |
| K-261 | MISSING | Fridge-sink 18.9, sink-range 8.0, range-fridge 21.5 ft (centres, computed): 48 ft against 26 | same |
| K-262 | IN | Kitchen is two rooms away from the front door; no line of sight | same |
| K-270 | MISSING | Fridge to sink 18.9 ft (computed) | same |
| K-273 | MISSING | Not designed for | same |
| K-274 | IN | Island to the sink/dishwasher run 4.8 ft (58 in); island to the north run 8.9 ft | MISSING -> IN |
| K-277 | IN | Sink under the south window | same |
| K-279 | MISSING | Island is 7.5 ft from the pantry door; no counter between | IN -> MISSING |
| K-281 | IN | Island 28 sf empty | same |
| K-282 | MISSING | Island centre is 8.2 ft from the range but 13.4 ft from the fridge (computed) | same |
| K-283 | IN | Range has 3 ft of counter on its west side and 1.3 ft on its east | same |
| K-288 | IN | Dishwasher beside the sink | MISSING -> IN |
| K-290 | IN | Fridge is 1.4 ft from the pantry door, 18.9 ft from the sink and 21.5 ft from the range (closer to the sink), at the end of the north run, 20 ft from the oven | MISSING -> IN |
| K-292 | IN | Fridge and tall cabinets sit together at the north-west end of the run | CONTRADICTED -> IN |
| K-297 | MISSING | Foyer has no window; the vestibule is solid | same |
| K-298 | MISSING | Guest bath opens directly off the foyer | same |
| K-299 | MISSING | Axis ends at the suite-hall door; no window or glass door on it | IN -> MISSING |
| K-300 | MISSING | Same | IN -> MISSING |
| K-302 | MISSING | Office is in the basement, no bath near it | same |
| K-304 | IN | Walk-ins open off the bedroom | same |
| K-306 | IN | Master bed on the north wall between two windows (x 84.4-89.4 and 99-104); no window behind it | CONTRADICTED -> IN |
| K-307 | MISSING | Bedroom 2 east window (y 31.5-36.5) is mid-wall; master windows are at the corners | same |
| K-315 | IN | Same as K-037 | MISSING -> IN |
| K-316 | IN | Strict circulation 193 sf = 6.9% of 2,779 (was 16.2%); 8.7% with the foyer | CONTRADICTED -> IN |
| K-317 | IN | Rooms open on 5.6 ft halls or onto each other | MISSING -> IN |
| K-318 | IN | Garage to the rest of the house goes mudroom - clear 8 ft lane on the kitchen's north side - dining; the work zone is the south run and the island | same |
| K-320 | IN | Vestibule wardrobe, foyer console, mudroom lockers, Costco-door pantry | MISSING -> IN |
| K-323 | IN | Living room west wall is 10 ft solid (TV / fireplace); south wall 7.6 ft solid | MISSING -> IN |
| K-324 | IN | Zones separated by 6-9 ft openings | same |
| K-325 | IN | No bedroom wall touches a kitchen, living room or the garage | MISSING -> IN |
| K-326 | IN | Bedroom 2 and the suite are buffered by walk-ins, laundry, baths and halls | MISSING -> IN |
| K-328 | IN | No bedroom touches the foyer | same |
| K-329 | IN | Laundry 23.5 ft from the master bed, 25.3 ft from bedroom 2 | MISSING -> IN |
| K-330 | IN | The garage-to-house path crosses the kitchen on a clear 8 ft lane north of the island, outside the range / sink / dishwasher zone | same |
| K-331 | CONTRADICTED | Same closets as K-070: 3 of 5 on exterior walls | same |
| K-332 | IN | Linear kitchen-dining-living, but 9 ft and 6 ft openings, mudroom and pantry between; not one open room | same |
| K-333 | IN | Walk-ins open off the bedroom | same |
| K-334 | IN | 0 bedrooms share a wall with the living room (matrix_d.md) | same |
| K-335 | IN | Garage at the west end of the public wing, doors to the road, drive south, 70 ft from the nearest bedroom; no bedroom is past the garage | CONTRADICTED -> IN |

**Counts:** IN 109, MISSING 52, CONTRADICTED 3, of 164 (today 62 / 89 / 13).

**The 12 deal-breakers:** 11 met.

| Deal-breaker | K-IDs | Verdict |
|---|---|---|
| Bedroom next to the foyer | K-328 | IN |
| Laundry far from bedrooms | K-329 | IN (23.5 ft) |
| Major path only through the kitchen zone | K-330 | IN, on a clear 8 ft lane |
| Closets on exterior walls | K-331 / K-070 | **CONTRADICTED** (3 of 5 closets) |
| Full open concept | K-332 | IN |
| Closet only through the master bath | K-333 / K-201 / K-304 | IN |
| Bedroom sharing a wall with the living room | K-334 | IN |
| Garage at the rear / drive past bedrooms | K-335 / K-005 | IN |
| Laundry tied to the master suite | K-036 | IN |
| Costco door, pantry to garage | K-037 / K-115 | IN |
| Wide doors and halls | K-003 / K-060 / K-061 | IN |
| No-threshold shower | K-055 | IN (recess flagged) |

Misses and contradictions: CONTRADICTED = K-070, K-331 (exterior closets), K-104 (suite door in line with the front door). MISSING: see the table.

## 6. Egress and accessibility

Code: ABC 9.9.10.1.(2)(a), abc_2023 p.873: "provide an unobstructed opening of not less than 0.35 m2 in area with no dimension less than 380 mm". ABC 9.9.10.1.(3), p.873: "a clearance of not less than 760 mm shall be provided in front of the window". Estimates below are mine; the window supplier's NFRC / egress rating governs.

| Basement window | Wall | Rough opening (w x h), sill | Estimated clear opening | Well |
|---|---|---|---|---|
| Bedroom 3 | east x 105, y 61-63.5 | 2.5 x 4.0 ft, sill 3.0 ft | casement, (2.5 - 0.25) x (4.0 - 0.25) = 8.4 sq ft = 0.78 m2; least side 2.25 ft = 686 mm | WINDOW WELL 3.5 x 5.5 ft: 3.5 ft = 1,067 mm clear in front (>= 760); cover openable from inside |
| Bedroom 4 | west x 74, y 61-63.5 | same | same | WINDOW WELL 3.5 x 5.5 ft |
| Flex / craft room | east x 100.2, y 33-35.5 | same | same | WINDOW WELL 3.5 x 5.0 ft |

| Accessibility item | Result |
|---|---|
| 1,700 mm circle (ABC 3.8.4.3.(4), abc_2023 p.318: "unobstructed turning diameter of not less than 1 700 mm") | Drawn as thin discs: kitchen (lane, 5.6 x 5.6 ft), foyer, guest bath, master bath, laundry; basement baths 2 |
| Step-free route to garage | Garage slab at house level; the drive slopes up (2 ft over the 16 ft drawn is 12.5%: too steep; the engineer / grading plan should lengthen the drive or raise the pad) |
| Step-free route to deck | Patio and primary deck are at house level; steps to the yard are separate |
| Halls | HALL 5.6 ft clear; suite hall 5.6 ft; stair-top landing 4.2 ft |
| Doors | 0 single doors under 32 in; 12 at 36 in or more; 1 WC door at 2.8 ft (34 in); cased openings 4-6 ft |
| Elevator stack | x 88.4-94.4, y 21.6-29.0 on both levels; 5 x 5 ft approach in the 5.6 ft hall; closet with a door (`ELEVATOR (FUTURE)`) |
| Stair | straight, 19 risers of 7.42 in, flight 3,581 mm (ABC 9.8.3.3.(1), p.852: "shall not exceed 3.7 m"), clear width 4.2 ft = 50 in (>= 42 in for a heavy-duty stair lift later); level landings top and bottom; headroom opening 11.5 ft |
| Showers | master and guest curbless; framing recess flagged for the licensed Alberta engineer |

## 7. Cost drivers vs today's model

**$$$ down.** Repo research only (`findings/07-cost-ve.md`); no price for the elevator, a pool or the roof exists in the repo.
1. **Floor area.** Heated main floor 5,486 -> 2,779 sq ft centre line and basement 3,475 -> 2,779; the repo has no $/sq ft, so this is "no data, needs a quote" ($$$ down).
2. **Basement walls.** COST-01 prices the ICF at $128K-$182K for a 281.3 ft perimeter and 12.96 ft wall; this outline is 318 ft at a 10.125 ft wall, i.e. 88% of the wall area (computed: 318 x 10.125 / 281.3 x 12.96), about $113K-$161K, and COST-12 gives -$9.8K-$14.1K per foot of slab lowered.
3. **No pool, spa, theatre, pool equipment.** The repo prices none of them ("no data"), so rank $$$ down.
Costs added (no repo price, needs a quote): elevator shaft and pit framing, the curbless-shower recesses (cheap if framed before the subfloor, ARC-06), 16 corners in the heated outline instead of a rectangle's 4, and drive grading.

## 8. What you give up

The tub, the theatre, the sun room and the separate powder room, to stay under 3,000 sq ft: bedroom 2 has no ensuite, the primary laundry is 8 x 8, and one primary walk-in sits on an exterior wall.

## 9. Departures

- **Drive:** from the west side to the south (a 24.4 x 16 ft `DRIVE` strip drawn; `site.scad` still draws the west drive, which the plan-facts bedroom-to-drive row reads). Cost $$; it also moves snow off the septic and services side (SITE-03/04 in round 1).
- **Utility room:** at the west end of the wing, basement x 24.4-35, y 9.6-21.6; its west wall is against the garage, its north wall is exterior (flue, intake, combustion air to open yard, patio starts at x 36). Services from the west reach it along the garage's north side (not drawn): a longer run than today's, $.
- **Septic (x -3..3, y 52-64), field and well (150, 75):** not touched; nearest heated wall to the tank is x 74 (and the garage x 0, y <= 24.4, 28 ft away); the house stays inside x 0-113, y -16-70 (north outside face at y 70.0).
- **Drain exit:** the tool still measures to (22.16, 58); the utility room is 36 ft south of it.
- **Basement:** redrawn (no `foundation.scad`); the exit stair and light wells are gone; window wells added.
- **Shop:** none.
