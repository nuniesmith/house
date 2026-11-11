# R2-ACC: accessibility, flow and Kayla's notes (round 2, options D and E)

**Specialist:** R2-ACC (prefix ACC). **Status:** D and E complete; **F pending** (option F is being redrawn; its column, findings and the three-way verdict will be added when it lands). **Date:** 2026-11-11.

**Inputs read:** REVIEW-R2.md, ROUND2-BRIEF.md, COMMON-RULES.md, `01-architecture-flow.md` (164 PLAN items), round-1 `kayla-rescore.md` rulings, `r2-code-structure.md` (not duplicated: stair headroom, egress wells and structure are R2-CODE's), both options' scad files, PNGs, matrix, plan_facts and PROS-CONS.

**Method.** Re-ran `plan_facts.py` and `check_layout.py` (both options, both levels: OK). Parsed the scad tables (`work/R2-ACC/parse.py`) and measured on plan geometry: largest inscribed circle after fixtures and door leaves (`circ.py`), line of sight with closed doors and open cased openings (`los.py`), door and hall widths (`misc.py`). Clear size = centre line - 0.4 ft. A turning circle counts only if clear of fixtures and of door leaves swung 90 degrees. Round-1 rulings applied exactly (garage-wall closet = exterior; undrawn drive does not count; kitchen crossing needs a clear lane; flush shower with stated recess counts); partial = MISSING.

## 1. Findings

| # | Severity | Option | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| ACC-01 | Should fix | D | Main floor, closets (linen, BR 2 closet, WIC @96.4) | Three of five closets touch exterior walls: K-070/K-331 (a deal-breaker) CONTRADICTED, K-071 MISSING. Moving them inboard grows a footprint that is at 2,934 of 3,000 sq ft. | matrix_d.md "Closets touching an exterior wall: 3 of 5"; main_floor_d.scad rooms LINEN, BR 2 CLOSET, WIC | - | $ |
| ACC-02 | Should fix | E | Open living zone | K-332 (deal-breaker) CONTRADICTED: dining/living 15 ft opening at x=47 (y 2-17) of a 19.5 ft wall (77 pct), kitchen/dining 8 ft opening, no door anywhere between the three rooms. K-062, K-324 MISSING. | main_floor_e.scad doors `[47,2,y,15,full]`, `[34,19.5,x,8,full]` | - | $ |
| ACC-03 | Should fix | D | Basement BATH @92.8,41.2 | Basement bath 2 is 7.6 x 8.0 ft clear and its largest clear circle is 5.40 ft (1,646 mm), under 1,700 mm; the designer's matrix says "2 of 2 basement baths". The drawn "circle" is a 4.4 x 3.4 ft disc. | circ.py: 5.40 ft (arc 4.20); basement_d.scad fixture `[93.6,46,98,49.4]`; brief hard target 6 | ABC 3.8.4.3.(4) | $ |
| ACC-04 | Should fix | E | Powder, J&J bath, WC | Powder 4.1 x 7.6 ft clear: largest circle 3.0 ft. Basement J&J bath: the drawn circle (66.7-72.3, 26.2-31.8) sits in the swing of three doors; 4.8 ft clear with leaves open. Ensuite WC room 3.7 ft with its leaf. Main floor 5 of 6 rooms pass (kitchen 7.2, foyer 6.9, laundry 6.6, shared bath 6.0, ensuite 8.4 ft). | circ.py; main_floor_e.scad POWDER row; basement_e.scad doors (65.5,28), (73.5,28), (67,25) | ABC 3.8.4.3.(4) | $ |
| ACC-05 | Should fix | D | Doors | Hard target 6 says every swing door is 36 in. D has three at 2.8 ft (34 in): main WC (75.5,62), basement (77.8,44) and (101,49.6). K-061 MISSING, so the "wide doors and halls" deal-breaker is not met. Each is a 0.2 ft change. | parse of door rows; matrix_d.md counts main floor only | - | $ |
| ACC-06 | Should fix | D | Vestibule | Vestibule-to-foyer is a 4.8 ft cased opening with no door: not an air lock (K-041). Largest circle in the vestibule 4.3 ft. | main_floor_d.scad doors `[83.2,8.0,x,4.8,open]`; round-1 B and C drew inner doors | - | $ |
| ACC-07 | Should fix | E | Foyer to kitchen sight line | From the foyer west edge (66,10) the line runs through the living room, the 15 ft opening and the 8 ft opening to the island and range. 245/266 sf of dining and 223/342 sf of living are visible from the foyer centre. K-144 and K-262 CONTRADICTED (round-1 C ruling). | los.py; main_floor_e.scad island `[31,27,40.8,31.5]` | - | $ |
| ACC-08 | Should fix | E | Basement noise | GYM / MUSIC (x 83.5-96.5, y 0-19.5) is directly under main BEDROOM 2 (x 82-96.5, y 0-11.5); basement bedrooms 3 and 4 face the theatre and gym across a 5.1 ft hall. D has no theatre and its gym (x 51-64) is under the dining room, not a bedroom. | basement_e.scad and main_floor_e.scad room rows | - | $$ (sound assemblies; no repo price) |
| ACC-09 | Should fix | E | Kitchen orientation | Kitchen is the north-west block (windows north and west only): K-099 and K-012 MISSING; K-114 MISSING (74 sf pantry, no counter, 1 ft shelf bank). | main_floor_e.scad windows y=39 and x=24; pantry fixtures | - | $ |
| ACC-10 | Consider | D | Front sight lines | From the foyer, 339/420 sf of the living room and 110/294 sf of the dining room are visible; the bedroom 2 door and the suite-hall door are visible from the front door. K-104 CONTRADICTED, K-144 MISSING. Kitchen not visible (0/315 sf), K-262 IN. | los.py | - | $ |
| ACC-11 | Consider | D | Pantry, fridge, laundry | Pantry 77 sf clear (target 80-96): K-030 MISSING. Fridge and tall cabinets are a separate 5.5 ft tall unit: K-292 MISSING. Laundry is off the ensuite/suite hall, not the walk-ins: K-166, K-210 MISSING. | main_floor_d.scad fixtures and doors | - | $ |
| ACC-12 | Consider | D, E | Basement bedroom light | D basement bedroom 4 (west/north windows) and E basement bedrooms 3 and 4 (north windows) get no east light: K-100 MISSING under the round-1 C ruling. | window rows | - | none |
| ACC-13 | Consider | D, E | Step-free routes | Both put the garage slab at house level, so house to garage is step-free through a 3 ft door (D (24.4,3); E (24,3) and Costco door (24,12.5)). The exterior drive rise is 2 ft over the 16 ft drawn (12.5 pct, the designers' own figure): drive length is a site item. Decks and patios are at house level with steps to the yard; neither draws a ramp. | PROS-CONS D s.6, E s.6 | ABC 3.8.4.3.(3) | $$ (drive grading; no repo price) |
| ACC-14 | Consider | D | Foyer circle | Foyer is 5.6 ft clear: circle 5.60 ft = 1,707 mm, a 7 mm margin. E foyer 6.9 ft. | circ.py | ABC 3.8.4.3.(4) | none |
| ACC-15 | Consider | D, E | Entry storage depth | Entry coat cabinets: D 1.4 ft (17 in) deep, E 0.9 ft (11 in); mudroom lockers 1.4-1.5 ft. Hanging coats usually want about 2 ft (planning rule, not a code item). Verdicts unchanged. | fixtures rows | - | none |
| ACC-16 | Consider | D | Primary bedroom | Designer says 3 ft from bed foot to bench; the bench (y 59.6-61.0) is 1.0 ft from the bed foot (y 62.0). Side clearances 7.6-7.8 ft, so K-053 stays IN. | main_floor_d.scad fixtures | - | none |
| ACC-17 | Consider | E | Basement gym window | PROS-CONS lists the gym as windowed; basement windows are at the office, living room, utility and three north bedroom/flex wells only. Gym/music and theatre have none. | basement_e.scad windows | - | none |
| ACC-18 | Consider | D, E | Halls | D hall 5.6 ft clear, E 5.1 ft; both meet the 5 ft target and 860 mm. E's stair/elevator hub is 50 ft by door path from the primary bed. | misc.py | ABC 9.5.4.1. | none |

(Stair headroom, window wells and egress, structure, the 39 ft span and the drive grade: see R2-CODE `r2-code-structure.md`; not repeated.)

## 2. Kayla re-score (164 PLAN items)

| | Today | D (mine) | E (mine) | F |
|---|---|---|---|---|
| IN / MISSING / CONTRADICTED | 62 / 89 / 13 | 101 / 60 / 3 | 99 / 62 / 3 | pending |
| Designer's own score | - | 109 / 52 / 3 | 103 / 60 / 1 | pending |
| Deal-breakers met (of 12) | 5 | 10 | 11 | pending |
| Designer's deal-breaker score | - | 11 | 11 | pending |


| Deal-breaker | D | E | F |
|---|---|---|---|
| K-328 | met | met | pending |
| K-329 | met | met | pending |
| K-330 | met | met | pending |
| K-331/K-070 | NOT met | met | pending |
| K-332 | met | NOT met | pending |
| K-333/K-201/K-304 | met | met | pending |
| K-334 | met | met | pending |
| K-335/K-005 | met | met | pending |
| K-036+K-329 | met | met | pending |
| K-037+K-115 | met | met | pending |
| wide K-003/060/061 | NOT met | met | pending |
| K-055 | met | met | pending |

D misses: K-331/K-070 (ACC-01) and wide doors (K-061, ACC-05). E miss: K-332 (ACC-02). Designers claimed 11 each.

### Items where my verdict differs from the designer's

**Option D** (designer 109 / 52 / 3; mine 101 / 60 / 3)

| K-ID | Designer | Mine | Evidence |
|---|---|---|---|
| K-004 | IN | MISSING | Basement BATH @92.8,41.2 (7.6x8.0 clear): largest clear circle 5.40 ft (1,646 mm) <5.58; its drawn "circle" is a 4.4x3.4 ft disc (basement_d.scad fixture [93.6,46,98,49.4]). Partial = MISSING (round-1 standard). 5 of 5 main-floor circles do measure clear. |
| K-030 | IN | MISSING | PANTRY 8.0x9.6 = 77 sf clear (84 sf CL), 1 shelf bank + 6.4 ft counter + freezer; smaller than round-1 option B pantry (90 sf) that was ruled MISSING; basement storage is 2 floors from the Costco door. |
| K-041 | IN | MISSING | Vestibule->foyer is door row [83.2,8.0,x,4.8,"open"]: a cased opening, no inner door, so no air lock (round-1 B and C drew inner doors). |
| K-061 | IN | MISSING | Hard target 6 = all swing doors 36 in. Three single doors are 2.8 ft (34 in): main WC [75.5,62.0], basement [77.8,44.0] and [101.0,49.6] (parse of main_floor_d.scad / basement_d.scad). |
| K-100 | IN | MISSING | Round-1 ruling on C (a bedroom with no east light = MISSING): basement BEDROOM 4 has west (x74) and north windows only. |
| K-144 | IN | MISSING | Line of sight (shapely, closed doors, cased openings open): from the foyer centre 339 of 420 sf of LIVING ROOM and 110 of 294 sf of DINING are visible through the 6 ft opening; kitchen 0 of 315. One of two messy areas in view = partial. |
| K-210 | IN | MISSING | Same ground as K-166: laundry opens off the ensuite and the suite hall, not the walk-ins (round-1 IN needed the laundry door off the WIC). Walk-ins are 6 ft of hall away on the other side of the suite hall. |
| K-292 | IN | MISSING | North "run" is fridge + tall cabinets only (x 33.2-38.7, y 18.4-21.4): a separate 5.5 ft tall-unit wall with no counter beside it, which is what K-292 asks to avoid. |

**Option E** (designer 103 / 60 / 1; mine 99 / 62 / 3)

| K-ID | Designer | Mine | Evidence |
|---|---|---|---|
| K-002 | MISSING | IN | The note asks for a basement; it does not ask for a pool. E has a 2,940 sf basement with rec room 374 sf, theatre 273 sf, gym/music 254 sf. Round 1 scored IN with these rooms. |
| K-004 | IN | MISSING | POWDER 4.1x7.6 ft clear: largest circle 3.0 ft; the J&J bath circle (66.7-72.3, 26.2-31.8) is crossed by the swung leaves of three doors, 4.8 ft clear with leaves at 90 deg; WC room 3.7 ft with its leaf. Designer concedes the powder has no circle. |
| K-008 | IN | MISSING | Basement GYM / MUSIC (x 83.5-96.5, y 0-19.5) sits under main BEDROOM 2 (x 82-96.5, y 0-11.5), 13 x 11.5 ft overlap; basement bedrooms 3 and 4 face the theatre and gym across a 5.1 ft hall. |
| K-012 | IN | MISSING | Round-1 ruling on C: living spaces south but no south backyard = MISSING. E kitchen faces north (windows N and W only); the south side is the road side (drive, front porch); the private deck is east. |
| K-099 | IN | MISSING | Kitchen is on the north wall (windows x 28-40, y 39; west x=24): one of the three named active spaces gets no south or east light. Designer evidence says "the kitchen is north" yet scores IN. |
| K-100 | IN | MISSING | Round-1 ruling on C: BEDROOM 3 with a north window only = MISSING. E basement bedrooms 3 and 4 have north windows only (y 39). |
| K-114 | IN | MISSING | Pantry 74 sf has a 1 ft shelf bank (x 31.8-32.8) and a freezer, no counter; designer's own K-030 says "no room for small-appliance counters". |
| K-144 | IN | CONTRADICTED | Sight line from the foyer west edge (66,10) through the 6 ft foyer/living opening, the 15 ft living/dining opening and the 8 ft dining/kitchen opening reaches the island (31-40.8, 27-31.5) and west counter run. 223 of 342 sf of living and 245 of 266 sf of dining are visible from the foyer centre. Same call as round-1 C. |
| K-166 | MISSING | IN | Round-1 ruling: laundry door off the WIC = basket never leaves the suite. E laundry opens off WIC B (door [61.5,22,y]). |
| K-210 | MISSING | IN | Same ruling as K-166. |
| K-255 | MISSING | IN | Round 1 scored K-255 IN for a roofed front porch/deck of 10+ ft depth (C, B). E has a 420 sf roofed front porch, a 168 sf patio and a 184 sf deck. |
| K-262 | IN | CONTRADICTED | Same sight line as K-144: the kitchen island and range are in view from the foyer through the living and dining openings. |

Every other item matches the designer's verdict after a check against the plan. Full per-item verdicts: `$RUN/work/R2-ACC/rescore.json` (keys D, E; F = "pending").

## 3. Accessibility audit

| Criterion | Today | D | E | F |
|---|---|---|---|---|
| 1,700 mm circle, main floor, clear of fixtures and open door leaves | 0 shown | kitchen 10.6, foyer 5.60, guest bath 6.8, master bath 6.6, laundry 6.2 ft: 5 of 5 | kitchen 7.2, foyer 6.9, laundry 6.6, shared bath 6.0, ensuite 8.4 pass; powder 3.0 fails: 5 of 6 | pending |
| Basement baths | - | bath 1 6.8 ft pass; bath 2 5.40 ft fail: 1 of 2 | J&J 4.8 ft with leaves open: 0 of 1 | pending |
| Step-free house to garage | 3 steps | Y (slab at house level; drive rise 12.5 pct as drawn) | Y (same) | pending |
| House to deck | - | Y at house level; steps to yard | Y; steps to yard | pending |
| Single doors <32 in / 32-35 in / 36 in+ | 7 / 11 / 4 (main) | main 0 / 1 / 12; basement 0 / 2 / 13 | main 0 / 0 / 19; basement 0 / 0 / 14 | pending |
| Minimum hall clear (ft) | 3.71 | 5.60 (4.2 stair-top landing) | 5.10 (4.2-4.6 landings) | pending |
| Elevator stack | none | Y: x 88.4-94.4, y 21.6-29.0, offset 0.0 | Y: x 42-48, y 27-34.4, offset 0.0 | pending |
| 5 x 5 ft approach | - | both levels: hall 5.6 ft wide, door swings into the closet | main hall 5.1 ft wide, door leaf swings into it; basement hall 7.5 ft deep | pending |
| Stair | 22 risers | straight, 19 risers, 4.2 ft (50 in) clear, landings 4.2 x 5.0 / 4.2 x 6.5 ft | straight east-west, 19 risers, 4.2 ft clear, landings 4.6 x 5.0 / 5.1 ft hall | pending |
| Curbless showers | N | master, guest, basement 1 flush, recess flagged | ensuite, shared, basement flush, recess flagged | pending |

ABC 3.8.4.3.(4) and (3), abc_2023 p.318; ABC 9.5.4.1.(1), p.841. The dwelling-unit rules are a yardstick, not a requirement for a house.

## 4. Flow, daylight, noise

| Criterion | D | E | F |
|---|---|---|---|
| Garage to kitchen with groceries | mudroom door (24.4,3) then 4 ft opening to the kitchen lane, about 30 ft; or Costco door to pantry | Costco door to pantry then kitchen door, 18 ft to the fridge; mudroom has no kitchen door | pending |
| Primary bed to toilet at night | ensuite then WC door, about 20 ft | ensuite then WC door, about 15 ft | pending |
| Primary bed to laundry | 23.5 ft | 30.0 ft through two walk-ins | pending |
| Entry to powder | guest bath off the foyer, 15.4 ft | powder beside the vestibule, 8 ft; door visible from the foyer | pending |
| Kitchen to dining | 9 ft opening | 8 ft opening | pending |
| Bedrooms and living rooms with exterior wall and window | all | all; living has windows on one wall | pending |
| Dark interior living rooms | none | none (theatre has no window) | pending |
| Depth at living rooms | 21.6 ft public wing; private wing 31 ft wide | 39 ft CL, 40 ft outside: at the limit | pending |
| Bedroom vs living / theatre noise | 0 shared walls; no theatre; gym under dining | 0 shared walls; gym under bedroom 2; theatre and gym 5.1 ft across a hall from basement bedrooms | pending |

## 5. Program check (clear sf vs target, from PROS-CONS s.2 spot-checked against plan_facts)

| Room | Target | D | E | F |
|---|---|---|---|---|
| Kitchen | 330 | 318 | 336 | pending |
| Dining + nook | 308-352 | 293 under | 260 under | pending |
| Pantry | 80-96 | 77 under | 74 under | pending |
| Living | 400-480 | 416 | 346 under | pending |
| Primary bedroom | 440-528 | 421 under | 374 under | pending |
| Ensuite | 170-228 | 161 under | 165 under | pending |
| Walk-ins (each 7 x 8) | 56 | 61 / 66 | 65 / 65 | pending |
| Laundry | 8 x 9 | 8.0 x 8.0 under | 7.6 x 9.1 under | pending |
| Bedroom 2 | 12 x 12 | 11.4 x 11.8 | 14.1 x 11.1 | pending |
| Powder | 5 x 7 | none (guest bath doubles) | 4.1 x 7.6 under | pending |
| Basement theatre / gym | optional | theatre dropped; gym 162 | theatre 260; gym 241 | pending |
| Dropped | | theatre, tub, powder, sun room, library | library, sun room, tub | pending |

## 6. Verdict (D and E; F pending)

1. D leads on Kayla items (101 vs 99 IN) and on flow and daylight: kitchen faces south, the kitchen is hidden from the foyer, no gym sits under a bedroom.
2. D's misses are small edits (three 34 in doors, one basement bath circle, an open vestibule) plus the exterior closets; E's are layout-level (powder, J&J circle, open living zone, kitchen sight line, gym under a bedroom).
3. Strongest of D and E on my criteria: D. The final ranking needs F.

## 7. Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| ACC-03, ACC-04, ACC-14 | `search.py --page abc_2023 318` | abc_2023 | 318 | 3.8.4.3. | designed with an unobstructed turning diameter of not less than 1 700 mm |
| ACC-13 | `search.py --page abc_2023 318` | abc_2023 | 318 | 3.8.4.3. | A barrier-free path of travel shall be provided between the interior living space of the dwelling unit and any ancillary space |
| ACC-18 | `search.py --doc abc_2023 '"9.5.4.1"'` | abc_2023 | 841 | 9.5.4.1. | width of a hallway within a dwelling unit shall be not less than 860 mm |
