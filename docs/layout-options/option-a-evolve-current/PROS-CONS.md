# Option A: Evolve the current model

Files in this folder: `main_floor_a.scad`, `basement_a.scad`, `plan_a.png`, `3d_a.png`, `stair_a.png` (the new stair), `basement_plan_a.png`, `matrix_a.md`, `plan_facts_a.md`, `check_layout.txt` (both files print OK).

## 1. Matrix numbers

| Row | Option A | Current model |
|---|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED (of 164) | 78 / 77 / 9 | 62 / 89 / 13 |
| Deal-breakers met (of 12 in ARC's list) | 10 (open: wide halls K-060, no-threshold shower K-055) | 5 |
| Review Blockers fixed / open (of 6: CODE-01, STR-04, STR-01, STR-02, STR-03, PLB-01) | 2 fixed (CODE-01, STR-04) / 4 open | 0 / 6 |
| Circulation % (strict / with foyer) | 16.6% / 22.2% | 16.2% / 21.9% |
| Drain-run index (ft), wet-wall groups (main), groups stacked over the basement | 1,019 ft (alt exit 866); 15; 1 of 15 | 879 ft; 14; 1 of 14 |
| Single doors under 32 in / 32-35 in / 36 in+ (main); min hall clear width | 0 / 0 / 23; 4.71 ft | 7 / 11 / 4; 3.71 ft |
| No-threshold shower | N | N |
| Bedrooms sharing a wall with the living/great room | 0 | 0 |
| A bedroom next to the foyer | N | N |
| Master bed to laundry path (ft) | 42.9 (MASTER LAUNDRY); 102.6 to the old LAUNDRY, kept | 103.1 |
| Master suite's side | east (north-east block, x 95-128) | same |
| Bedrooms with east light | 1 (master) | 1 |
| Living spaces facing south | 2 rows (DEN, den alcove) | same |
| Living spaces with windows on 2+ walls | 4 rooms in all (SUN ROOM, MASTER BEDROOM, DEN, BREAKFAST); 0 living spaces added | 4 |
| Building area, outside face (m2) against 600 | 584.5 (15.5 under; centre lines 564.4) | 608.0 |
| Basement / shop / site changes | basement: stair foot room and hall rows redrawn (basement_a.scad); shop: none; site: garage doors face south, west drive replaced by a south drive (not drawn in site.scad) | |
| Cost vs the current model | $ down (net saving: 243 sf of garage leaves; a stair landing, a second W/D hookup and a new south drive come back) | |

## 2. What it is

Same footprint, basement shell, shop, septic (west) and well (east) as `models/main_floor.scad`, with the smallest moves that answer the Blockers and the deal-breakers. The model is a copy of the current file; the 56 doors, 52 rooms and 17 windows tables keep their format. Changes:

1. **Stair (CODE-01).** The single 22-riser flight (4,191 mm) is now 18 risers (3,429 mm) south from the unchanged top nosing, a 4.4 ft long x 4.22 ft clear landing at 11.25 ft below the main floor, a 90-degree turn east, and 4 risers (762 mm). The main-floor opening and headroom line are unchanged, so STR-08's 43 mm margin is unchanged (still an engineer item). The foot moves to the basement east hall (x 49.7, y 27.6-32.2).
2. **Garage (STR-04, K-005/K-335).** South wall moved from y 1.25 to y 11.25 (10 ft, 243 sf). The two west doors (16 ft + 9 ft) become one 16 ft door on the south wall.
3. **Costco door (K-037).** 3 ft door at x 24.34, y 23.6-26.6, with a third garage step run (y 22.2-27.6).
4. **LINEN becomes MASTER LAUNDRY (K-036).** W/D along the east (exterior) wall, door M53 from the master bath, the old east window above the dryer.
5. **BEDROOM 2 closet (K-070).** The west-wall WIC is gone. A 3.6 ft deep walk-in runs along the east wall (the laundry/mudroom side). The old WIC area joins the WC, now 6.5 x 7.2 ft. Bed moved to the north wall. BEDROOM 2 is 142 sf (was 188).
6. **Doors (K-003/K-061, CODE-02).** Every swing door under 3 ft is 3 ft, including M28 (stair landing) and the M49 closet opening (the closet passage grew 0.4 ft to hold it).
7. **Bedroom hall.** North wall moved 1 ft (4.71 ft clear, was 3.71); LAUNDRY 1 ft shorter (123 sf, was 138); the N-S hall and the bedroom hall's east end are one room so M28 sits wholly in one room (the checker requires that).

Not done on purpose: powder room, vestibule, foyer/spine trimming, kitchen, bunk/study closets, windows, shower pans.

## 3. Pros

- **Under the Part 9 line with margin.** 584.5 m2 against 600 (matrix_a.md, same 0.5 ft method as the 608 m2 figure). Fixes STR-04 and CODE-03's margin ask (15.5 m2 vs 15). The trim is garage area only: no heated room shrinks for it.
- **The stair now passes the flight limit.** 18 risers x 190.5 mm = 3,429 mm and 4 x 190.5 = 762 mm, both under 3.7 m (ABC 9.8.3.3.(1), abc_2023 p.852, as quoted in REVIEW-SUMMARY section 5). The landing is 4.4 ft long against a 4.22 ft (1,286 mm) stair width (CODE-07, mid-landing). Rise 7.5 in and run 10.5 in are unchanged.
- **Master laundry.** Bed-to-laundry 103.1 ft to 42.9 ft; K-036, K-158, K-203, K-228, K-329 move to IN (ARC-02, PLB-09). Zero added area; the wall at y 20.56 is the bath's wet wall.
- **Costco door.** K-037/K-115/K-315/K-116 IN. Garage to scullery centre 17.9 ft; garage to the tall pantry 34.2 ft (was 41.3).
- **Doors.** 23 of 23 single doors at 36 in (was 4 of 22); 0 passage openings under 36 in. CODE-02 (M28, 732 mm against 810 mm in Table 9.5.5.1, abc_2023 p.842) is fixed at 36 in. K-003, K-061 IN.
- **Closets off exterior walls.** 0 of 4 closets touch a yard or porch wall (was 2 of 5). K-070 and the K-331 deal-breaker move to IN, with the garage-wall caveat in Cons.
- **Drive moves off the bedroom wing.** With the doors south, the nearest bedroom to the apron is 24.2 ft (was 9.3 ft). K-005/K-335 IN, and SITE-04's snow-pile dead end at y 42 beside the meters goes away (needs the site work in Cons).
- **Smallest change.** 52 rooms and 56 doors stay; no shop, basement shell, septic or well change; the checker passes on both files.

## 4. Cons

- **K-005/K-335 are only fixed by a site departure.** The south drive is not drawn in `site.scad`: the tool still prints 9.3 ft (matrix_a.md) because it reads the west drive. The 24.2 ft figure is a hand measurement. The south drive, its apron and a new road cut are unmodelled, and the road side is itself an assumption (site.scad:8).
- **The garage drops from 3 bays to 2.** One 16 ft door (66% of the 24.34 ft south wall, was 73% of the west wall, STR-06) and 24.2 ft of depth (23.8 ft inside). The 9 ft third door is gone. STR-06's 16 ft header and wall bracing remain an engineer item.
- **The drain run gets longer.** Index 879 ft to 1,019 ft and one more wet group (15) because the master laundry is at the far east end (K-006 stays MISSING; PLB-03, PLB-11 untouched). One group in 15 is over a basement group (unchanged).
- **BEDROOM 2 shrinks to 142 sf (from 188),** and its two west windows (11.4 of 12.67 ft of wall) are unchanged (K-307, K-081 MISSING). The walk-in's south wall (3.6 ft) is the garage wall, so K-070 holds only by the tool's rule.
- **Circulation rose 891 to 909 sf (16.6%).** The 481 sf spine, the 309 sf foyer and the 80 ft master-to-front-door run are untouched (ARC-07, K-316 CONTRADICTED, K-075 CONTRADICTED).
- **Basement stair foot moves.** The old 1.1 ft hallway strip is gone; the foot (x 49.7) now exits east. Foot to UTILITY is 26.4 ft (was 25.6), by the same Dijkstra method through the living room. The west hall is reached only through the living room or the HALL at x 37.4. Flight 2 sits under the main hall spine at x 47-49.7 (basement ceiling clear, 9.5 ft above the landing).
- **CODE-07 at the stair top stays open.** The top landing is 3.39 ft in the direction of travel (0.83 ft or 253 mm short of 4.22 ft) because the sun room wall at y 50.69 and the 11.64 ft opening length (headroom) are both fixed. It is open to the W and E (M28, M30) rather than a dead end; the designer must confirm the code reading. A fix is moving the sun-room wall about 0.9 ft north (a 10 sf loss), not done.
- **The garage steps get busier.** Three step runs along x 19.4-24.14 (y 15.6-19.6, 22.2-27.6, 30.5-35.2), with a landing 2.34 ft wide at the Costco door (CODE-11: landing and door arc to be confirmed). The 6 ft side aisle of the garage holds them all.
- **Still MISSING or CONTRADICTED:** powder room (K-033, K-145, K-157, K-298), vestibule (K-041), library (K-032), kitchen triangle 41.4 ft (K-261) and island sink (K-108), windowless rooms (K-007), K-055 curbless shower, K-060 walker-wide halls (master entry still 3.0 ft clear), K-074 tubs on exterior walls, K-306 bunk bed under the window.
- **Exterior-wall closets for BUNK ROOM and STUDY:** none added (ARC-04, K-071).
- **Doors only partly widened in the basement:** 7 of 14 basement doors are still 32-35 in.

## 5. Kayla compliance (all 164 PLAN items)

Verdict key as ARC used (partial presence is MISSING). Counts: **IN 78, MISSING 77, CONTRADICTED 9** (current model 62 / 89 / 13). 16 items moved to IN (K-003, K-061, K-005, K-335, K-036, K-158, K-203, K-228, K-329, K-037, K-115, K-315, K-116, K-070, K-331, K-103) and none got worse in verdict; K-006 and K-316 got worse in numbers only.

Deal-breakers (12): met 10 (K-328, K-329, K-330, K-331, K-332, K-333, K-334, K-335, K-036, K-037). Not met: wide doors and halls (K-003 and K-061 IN, K-060 MISSING) and the no-threshold shower (K-055).

**Contradictions left (9):** K-074, K-075, K-096, K-104, K-108, K-144, K-292, K-306, K-316.

**Misses (77), by theme:** noise and adjacency K-008, K-009, K-325, K-326; daylight and windows K-007, K-014, K-064, K-078, K-080, K-081, K-099, K-100, K-185, K-297, K-307, K-323; kitchen K-030, K-117, K-123, K-127, K-129, K-134, K-257, K-261, K-270, K-273, K-274, K-282, K-288, K-290; entry and mud K-041, K-043, K-044, K-141 to K-143, K-153, K-155, K-157, K-249, K-320; bath and access K-004, K-055, K-060, K-211, K-220, K-227; rooms K-032, K-033, K-145, K-237, K-240, K-242, K-245, K-298, K-302; other K-012, K-023, K-102, K-105, K-189; layout K-006, K-010, K-069, K-071, K-083, K-095, K-117, K-254, K-317; storage and utility K-038, K-040, K-058, K-059, K-166, K-170, K-172, K-210.

| K-ID | Verdict | Evidence | Change vs current |
|---|---|---|---|
| K-001 | IN | (unchanged) All essential rooms (kitchen, laundry, master suite, 2 bedrooms, hall BATH) are on the main level (PF §3.1); basement holds gym/theatre/pool/music... | none |
| K-002 | IN | (unchanged) Basement 3,475 sf (PF §1.1) with gym, theatre, music room, pool (PF §3.2). | none |
| K-003 | IN | 0 single doors under 36 in (matrix_a: 0 / 0 / 23); passage openings 38 of 38 at 36 in or more; bedroom hall 4.71 ft clear | MISSING to IN |
| K-004 | MISSING | Master bath 230 sf clear is generous (PF §3.1) but WC rooms are 3.4 ft clear wide (PF §3.1 rows :57, :90, :92), hall BATH 60 sf, BATH 2 62 sf; no... | BATH 2 WC room is now 6.5 x 7.2 ft (turning space), but master WCs stay 3.4 ft clear and the hall BATH is unchanged |
| K-005 | IN | Garage door now on the SOUTH wall (y 11.25); no west drive; BEDROOM 2 (y 35.46) is 24.2 ft north of the apron end, with the 24.2 ft garage between (hand figure). Needs the site departure: site.scad still draws the west drive, so plan_facts still prints 9.3 ft | CONTRADICTED to IN (depends on the site departure) |
| K-006 | MISSING | 15 wet-wall groups on the main floor, 1 within 5 ft of a basement group, drain-run index 1,019 ft (plan_facts_a.md section 9) | worse: 14 to 15 groups, 879 to 1,019 ft |
| K-007 | MISSING | (unchanged) Windowless: STUDY 97, FLEX ROOM 151, OFFICE 165, laundry, mudroom, scullery, FOYER 309 (PF §5.1 list of 27 rooms with no window row). | none |
| K-008 | MISSING | BEDROOM 2 east wall (12.7 ft) is shared with LAUNDRY (7.6 ft) and MUDROOM (5.1 ft), south wall (14.8 ft) with the garage (PF §2.2, §3.1). Master... | partly better, still MISSING: east wall is now the WIC (12.7 ft buffer); south wall still 11.2 ft of garage |
| K-009 | MISSING | The bedroom hall (x 22.1-42.65, y 49.64-53.75) also serves STUDY, laundry and the stair landing, and the hall BATH/sun room/flex are reached past... | unchanged: the hall still serves study, laundry and the stair landing |
| K-010 | MISSING | Room sizes are off a 2 ft module: 14.83 x 12.67, 11.26 x 8.69, 15.19 x 9.93 (PF §3.1). | unchanged |
| K-012 | MISSING | Kitchen, breakfast, den, foyer face south (PF §2.2) but the main living room (GREAT ROOM) and the deck face north (PF §2.2); garage drive is on... | drive now south; great room still north-facing |
| K-013 | IN | (unchanged) Master bedroom is in the north-east block (y 29.5-52.9) with north and east exterior walls (PF §2.2); bath and WICs sit south of it (PF §3.1). | none |
| K-014 | MISSING | (unchanged) Master has east windows 43.5 sf (PF §5.1). BEDROOM 2 windows are west, BUNK ROOM north (PF §5.1); the SUN ROOM faces north and east, not... | none |
| K-021 | IN | (unchanged) BREAKFAST bay 94 sf opens 14.5 ft to the kitchen (M41, PF §4.1) with banquette and round table (main_floor.scad furniture :54.41-60.33). | none |
| K-023 | MISSING | (unchanged) No door from KITCHEN / DINING to a covered outdoor area; the nearest covered outdoor is the front porch via BREAKFAST door M4 (5 ft), the back... | none |
| K-030 | MISSING | (unchanged) No pantry room; SCULLERY 90 sf clear carries a sink and two counters only (main_floor.scad:207-209) and tall pantry cabinets in the kitchen are... | none |
| K-031 | IN | (unchanged) STUDY 97 sf at the end of the bedroom hall, shares walls with bunk room, sun room, hall only (PF §3.1, §7.1); it has no window row (see K-007). | none |
| K-032 | MISSING | (unchanged) No library room on the main floor (PF §8.1 note: living-type rooms are GREAT ROOM, DEN, SUN ROOM). Basement LIVING ROOM 412 sf exists (PF §3.2). | none |
| K-033 | MISSING | (unchanged) No powder room (PF §15.14). Hall BATH is 65.8 ft from the foyer (PF §7.3). See ARC-09. | none |
| K-034 | IN | (unchanged) SUN ROOM 144 sf, enclosed, N window 48.1 sf, E window 23.4 sf, double door M37 to PATIO (PF §5.1, §4.1). | none |
| K-035 | IN | (unchanged) Kitchen and dining are one room (779 sf), dining table at x 59.3-63, y 12.7-21.9 with no hall or pantry between (PF §3.1; main_floor.scad furniture). | none |
| K-036 | IN | MASTER LAUNDRY (ex linen, 55 sf) opens off the master bath by a 36 in door; W/D on the east wall; bed to laundry 42.9 ft (was 103.1) | MISSING to IN |
| K-037 | IN | 3 ft door in the scullery/garage wall at x 24.34, y 23.6-26.6 (between the counter runs); 3 added garage steps (y 22.2-27.6); SCULLERY 1 door to the garage | MISSING to IN |
| K-038 | MISSING | (unchanged) No broom/vacuum closet in the room table (PF §3.1 closet rows: 3 WICs, LINEN, linen between WCs). | none |
| K-040 | MISSING | (unchanged) Both linen rooms (LINEN 55 sf, linen between WCs 25 sf) are in the master bath; none near BEDROOM 2, BUNK ROOM or the hall BATH (PF §3.1). | none |
| K-041 | MISSING | (unchanged) No vestibule: front door M1 opens straight into the 12 x 25.8 ft FOYER (PF §3.1, §4.1); opening M42 to the hall has no door. | none |
| K-043 | MISSING | (unchanged) Foyer fixtures are a bench and 'wine racks' only (main_floor.scad:238-239 rows at x 69.67-71.38); no mail/command centre drawn. | none |
| K-044 | MISSING | (unchanged) No key/purse landing drawn at the front entrance (same foyer rows). | none |
| K-047 | IN | (unchanged) Foyer bench 1.7 x 6.6 ft (69.67-71.38 x 12.07-18.65) and mud lockers/bench (main_floor.scad:215-217). | none |
| K-053 | IN | (unchanged) Master bed drawn floating with 4.8 ft east and 7.6 ft south of it to walls (main_floor.scad:267, x 116.25-122.17, y 37.07-43.65). Bed symbol 5.92... | none |
| K-055 | MISSING | Showers are drawn as 0.15 ft (1.8 in) raised tile boxes (main_floor.scad:224, 226); no depressed floor or curbless detail. Master shower 8.23 x... | unchanged: pans still 0.15 ft raised; curbless needs a recessed floor (engineer) |
| K-058 | MISSING | (unchanged) No stacked closet/shaft footprint reserved; stair is fixed 4.62 x 11.64 ft (PF §10.1). | none |
| K-059 | MISSING | (unchanged) No dumbwaiter shaft; basement LAUNDRY (x 67.4-81.7, y 5.8-13.4) is not under any main-floor laundry (PF §3.1, §3.2). | none |
| K-060 | MISSING | Clear hall widths: HALL @22.1 3.7 ft (45 in), master entry 3.0 ft (36 in), suite entry 5.2 ft, spine 5.5 ft (67 in), N-S hall 5.0 ft (PF §6.1). No... | hall 3.71 to 4.71 ft clear, but master entry stays 3.0 ft and no 60 in turning space |
| K-061 | IN | Same: all 23 swing doors, M28 and M49 at 36 in (main_floor_a.scad doors table) | MISSING to IN |
| K-062 | IN | (unchanged) Zones are separated by 15 full openings (4-26 ft) and 12 double doors rather than a single space (PF §4.3); great room and kitchen are split by... | none |
| K-064 | MISSING | (unchanged) Windows on 2 walls only in SUN ROOM, MASTER BEDROOM, DEN, BREAKFAST (PF §5.1); GREAT ROOM has north windows only, KITCHEN / DINING south only. | none |
| K-069 | MISSING | (unchanged) 17 outside and 13 inside corners, 395.5 ft heated perimeter (PF §1.2). | none |
| K-070 | IN | 0 of 4 closets touch a yard or porch wall (matrix_a). Caveat: the BEDROOM 2 walk-in has 3.6 ft of its south wall on the unheated garage, which the tool does not count as exterior | CONTRADICTED to IN (caveat) |
| K-071 | MISSING | 2 of 3 WICs fully interior (PF §8.3); BUNK ROOM and STUDY have no closet row. | WIC now touches the garage wall; BUNK and STUDY still have no closet |
| K-072 | IN | (unchanged) Hall BATH: shower y 35.9-38.4, toilet y 39.7-41.35, door y 45.39 (main_floor.scad:222-224, M34); master WCs are separate rooms. | none |
| K-074 | CONTRADICTED | (unchanged) Master tub x 123.16-127.63 sits on the east wall (gap 0.24 ft) and Bath 2 tub x 7.7-10.33 on the west wall x=7.27 (gap 0.43 ft) (PF §9.1, §2.2). | none |
| K-075 | CONTRADICTED | (unchanged) Bedroom wing (x 7.3-42.7) and master wing (x 95-128) are separated by foyer, kitchen, great room and den over 80 ft of hall (PF §3.1, §6.1). | none |
| K-077 | IN | (unchanged) No room has windows on opposite walls: pairs are E/N, S/W, E/S (PF §5.1). | none |
| K-078 | MISSING | (unchanged) 4 of the 9 windowed rooms have corner-adjacent windows (PF §5.1); GREAT ROOM and KITCHEN have one wall of glass. | none |
| K-080 | MISSING | (unchanged) Centred windows: DEN south (x 84-92 in room 81.1-96), SUN ROOM north (44.3-51.7 in room 42.65-53.95) (PF §5.1, §3.1). | none |
| K-081 | MISSING | (unchanged) BEDROOM 2 has 54 sf of west glass with no porch or overhang on that side (PF §5.1, §2.2: W 9.6 ft yard/soil). | none |
| K-083 | MISSING | (unchanged) Long:short ratios 1.4-1.6 only for GREAT ROOM 1.55, KITCHEN 1.44, FLEX 1.53, hall BATH 1.49; MASTER 1.27, BEDROOM 2 1.17, BUNK 1.17, SUN 1.13,... | none |
| K-095 | MISSING | (unchanged) FRONT PORCH 15.26 ft (4.65 m) deep in front of den and breakfast windows; PATIO 12.73 ft deep east of the sun room (PF §3.1). | none |
| K-096 | CONTRADICTED | (unchanged) Kitchen range run is on the west wall (faces SIDE ENTRY porch/yard, PF §2.2) and the sink run on the south wall (exterior); only the tall pantry... | none |
| K-099 | MISSING | (unchanged) Kitchen, den, breakfast are south (IN) but the main living room GREAT ROOM faces north only (PF §2.2). | none |
| K-100 | MISSING | (unchanged) Master east windows only; BEDROOM 2 west, BUNK ROOM north (PF §5.1). | none |
| K-102 | MISSING | (unchanged) Hall BATH toilet (x 51.12-53.09, y 39.7-41.35) is 4.0 ft inside the door line (door y 45.39); master WCs are enclosed in their own rooms (PF §9.1,... | none |
| K-103 | IN | BEDROOM 2 bed moved to the north wall at x 9-14; the old line through M18/M19 to the BATH 2 door (x 14.3-17.3) no longer starts at the bed; the north wall is solid at x 7.27-14.1 | MISSING to IN |
| K-104 | CONTRADICTED | (unchanged) Looking east along the 80.5 ft spine, double door M47 (55 in) and 64.8 in opening M48 put the master bedroom directly in line (PF §4.1, §3.1). | none |
| K-105 | MISSING | (unchanged) MUDROOM is open 12.4 ft to the hall (M14) and laundry door M15 is in its north wall (PF §4.1). | none |
| K-106 | IN | (unchanged) Island 6.9 x 9.87 ft (x 42.24-49.14, y 12.4-22.27), no stools drawn (main_floor.scad:203). | none |
| K-107 | IN | (unchanged) BREAKFAST banquette on two walls plus round table 5.1 ft (main_floor.scad furniture). | none |
| K-108 | CONTRADICTED | (unchanged) Prep sink at island x 43.22-44.87, y 16.68-18.65 (main_floor.scad:204). | none |
| K-114 | IN | (unchanged) SCULLERY 98 sf with sink and two counter runs, entered from kitchen M13 (PF §3.1, §4.1). | none |
| K-115 | IN | Same as K-037 | MISSING to IN |
| K-116 | IN | Garage to SCULLERY centre 17.9 ft; to the tall pantry cabinets 34.2 ft via the scullery (was 41.3); kitchen centre 41.7 ft (was 52.5) | MISSING to IN |
| K-117 | MISSING | (unchanged) No coffee bar near BREAKFAST; nearest counter is the south run (y 6.48-8.45) and buffet at y 27.2-29.1 (main_floor.scad:197-205). | none |
| K-123 | MISSING | (unchanged) Island faces the dining table and breakfast, not a living area; great room is across the hall via a 5.9 ft opening (PF §4.1 M40). | none |
| K-124 | IN | (unchanged) Sink x 39.93-42.57 on south wall under window x 37.7-45.2 (main_floor.scad:200, :191). | none |
| K-127 | MISSING | (unchanged) No outdoor door from KITCHEN / DINING; BREAKFAST M4 opens to the front porch (PF §4.1). | none |
| K-128 | IN | (unchanged) Dining table 3.62 x 9.21 ft with 6.2 ft to the foyer wall and 10.2 ft to the island (main_floor.scad furniture :59.34-62.96 x 12.73-21.94). | none |
| K-129 | MISSING | (unchanged) Dining/breakfast exterior door M4 is a 5 ft double (PF §4.1); no wide folding or sliding wall. | none |
| K-132 | IN | (unchanged) GREAT ROOM 435 sf clear holds three sofa boxes and a table in the drawn furniture (main_floor.scad furniture :70.53-79.74). | none |
| K-133 | IN | (unchanged) GREAT ROOM double door M33 (72 in) to DECK; SUN ROOM beside it (PF §4.1). | none |
| K-134 | MISSING | (unchanged) M33 is a 6 ft double door, M6 6.5 ft, M7 6.05 ft; no multi-panel wall (PF §4.1). | none |
| K-140 | IN | (unchanged) Foyer bench (main_floor.scad:239). | none |
| K-141 | MISSING | (unchanged) Foyer storage is 'wine racks' 7 ft high at x 69.67-71.38, y 18.65-29.11, not coat storage (main_floor.scad:238). | none |
| K-142 | MISSING | (unchanged) No closed coat/shoe storage in the foyer (same rows). | none |
| K-143 | MISSING | (unchanged) No foyer drop surface or shelf. | none |
| K-144 | CONTRADICTED | (unchanged) Front door (x 72-78.2), M42 (71.4-79.3), M43 (69.4-95.4) and deck doors M33 (70.65-76.65) line up: great room is seen from the door; kitchen is... | none |
| K-145 | MISSING | (unchanged) No powder room (PF §15.14). | none |
| K-146 | IN | (unchanged) Mud bench + cabinets 8.55 x 3.0 ft (x 28.09-36.64, y 36.94-39.97) and hall bench (main_floor.scad:216-217). | none |
| K-147 | IN | (unchanged) Lockers and cabinets drawn (main_floor.scad:215-216). | none |
| K-149 | IN | (unchanged) Lockers x 22.63-24.14, y 35.66-39.97, 7 ft high (main_floor.scad:215). | none |
| K-151 | IN | (unchanged) Mud bench/cabinet top 3 ft high near garage door (main_floor.scad:216). | none |
| K-153 | MISSING | (unchanged) No mail/command area drawn. | none |
| K-155 | MISSING | (unchanged) MUDROOM has no exterior door; its only openings are M14 and M15 (PF §4.1, §7.1). | none |
| K-156 | IN | (unchanged) Garage door M12 into the hall, mudroom open to the hall (PF §4.1). | none |
| K-157 | MISSING | (unchanged) No bath off the mudroom (PF §15.14). | none |
| K-158 | IN | Same as K-036 | MISSING to IN |
| K-163 | IN | (unchanged) Laundry sink x 33.22-35.1, y 41.02-43.52 (main_floor.scad:212). | none |
| K-166 | MISSING | Master to LAUNDRY 103.1 ft (PF §7.3); no pass-through. | no pass-through between closet and laundry; the laundry is a door away |
| K-170 | MISSING | (unchanged) Dog wash is in the basement PET ROOM (x 65.5-69, y 26.5-28.9, basement.scad:134), none near the garage entry. | none |
| K-172 | MISSING | (unchanged) No litter area; PET ROOM has no door to the garage (PF §7.2). | none |
| K-179 | IN | (unchanged) Hall BATH off the upper hall (M34); master bath off master suite; BATH 2 off bedroom lobby (PF §7.1). | none |
| K-183 | IN | (unchanged) OFFICE door M6 (78 in) to OFFICE PORCH 147 sf (PF §4.1). | none |
| K-185 | MISSING | (unchanged) SUN ROOM north wall 11.3 ft has a 7.4 ft window, east wall 12.7 ft has a 3.6 ft window plus 4.9 ft door (PF §5.1, §4.1). | none |
| K-186 | IN | (unchanged) Double door M37 (58.8 in) SUN ROOM to PATIO (PF §4.1). | none |
| K-188 | IN | (unchanged) SUN ROOM 134 sf clear with two sofa boxes (main_floor.scad furniture :43.09-51.78). | none |
| K-189 | MISSING | (unchanged) Drawn table is 2.6 x 3.6 ft and leaves 2.3 ft to the west sofa (main_floor.scad furniture :43.09-45.53 vs :47.83). | none |
| K-191 | IN | (unchanged) Master double door M7 (72.6 in) to MASTER PORCH 175 sf (PF §4.1). | none |
| K-192 | IN | (unchanged) The only fireplace box is in the great room (main_floor.scad:241). | none |
| K-195 | IN | (unchanged) Master bedroom 412 sf clear, bed 4.8 ft from east wall, 7.6 ft from south wall (PF §3.1). | none |
| K-200 | IN | (unchanged) Two separate WICs 95 and 94 sf (PF §3.1). | none |
| K-201 | IN | (unchanged) Closets open from the master bedroom through M49 (27.6 in, 'open') and from the bath through M52 (32.4 in) (PF §4.4). Opening M49 is narrow. | none |
| K-202 | IN | (unchanged) Bath reaches closets via M52 (PF §4.4); bedroom access exists (K-201). | none |
| K-203 | IN | Laundry reached through the master bath from the closet passage (M52) in 42.9 ft | MISSING to IN |
| K-210 | MISSING | No laundry in master suite (see K-036). | no pass-through basket; laundry door is off the bath |
| K-211 | MISSING | Master shower 8.23 x 4.5 ft is large (main_floor.scad:226) but drawn 1.8 in above floor. | unchanged |
| K-220 | MISSING | (unchanged) Tub 4.47 x 5.48 ft drawn as a 2 ft raised box, not sunken (main_floor.scad:227). | none |
| K-224 | IN | (unchanged) Double vanity 9.87 x 1.78 ft (main_floor.scad:225). | none |
| K-226 | IN | (unchanged) LINEN 55 sf and linen between WCs 25 sf off the master bath (PF §3.1). | none |
| K-227 | MISSING | Two WC rooms (IN) but 3.4 ft clear wide with 31.2 in doors (PF §3.1, §4.4). | doors now 36 in; rooms still 3.4 ft clear wide |
| K-228 | IN | MASTER LAUNDRY door M53 opens straight off the master bath | MISSING to IN |
| K-229 | IN | (unchanged) Closet passage door M52 to the bath (PF §4.4). | none |
| K-237 | MISSING | (unchanged) FLEX ROOM 14.8 x 9.5 ft clear has space for a bed but no window row (PF §3.1, §5.1) and a 6.5 ft slider to the hall. | none |
| K-238 | IN | Queen (5.0 x 6.67 ft) drawn head-on-north-wall in BEDROOM 2 (11.2 x 12.7 ft clear); 1.5 ft west and 4.2 ft east side clearance | IN (changed layout) |
| K-239 | IN | (unchanged) BATH 2 via lobby (M18, M19, M20), 19.4 ft path from bed (PF §7.3); also opens to BUNK ROOM (M23). | none |
| K-240 | MISSING | BEDROOM 2 has no exterior door; it shares 14.8 ft with the garage but has no door (PF §2.2). | unchanged |
| K-242 | MISSING | (unchanged) Two non-master bedrooms (BEDROOM 2, BUNK ROOM); no fourth bedroom (PF §3.1). | none |
| K-244 | IN | (unchanged) BATH 2 reaches BEDROOM 2 (via lobby) and BUNK ROOM (M23) (PF §7.1). | none |
| K-245 | MISSING | (unchanged) No small bedroom beside the master: OFFICE (165 sf) shares wall x=108.62 with the master bedroom but is an office (PF §3.1). | none |
| K-248 | IN | (unchanged) FRONT PORCH 796 sf with posts and roof blocks (main_floor.scad:94, posts :main_posts). | none |
| K-249 | MISSING | (unchanged) Mudroom has no outside door; garage side door M10 has a 17.5 sf uncovered pad (PF §3.1). | none |
| K-252 | IN | (unchanged) DECK 322 sf (26.5 x 12.2 ft) under porch roof posts (main_floor.scad:98, posts). | none |
| K-253 | IN | (unchanged) DECK and PATIO 193 sf adjoin (PF §3.1). | none |
| K-254 | MISSING | (unchanged) 7 porch roof blocks over 13 porch rows (PF §1.2); no unroofed sun area identified. | none |
| K-255 | IN | (unchanged) OFFICE PORCH 147 sf off the office (PF §3.1). | none |
| K-256 | IN | (unchanged) Range run has 4.9 ft north and 8.2 ft south of the range; sink has 1.6 ft west and 11.8 ft east (main_floor.scad:197-198, :200). | none |
| K-257 | MISSING | (unchanged) Scullery door M13 (y 23.3-26.3) sits between the range run end (y 22.6) and the fridge (y 25.89-29.11); no counter beside the fridge. | none |
| K-261 | MISSING | (unchanged) Legs: fridge-sink 20.4, sink-range 9.7, range-fridge 11.3 ft = 41.4 ft total (centres, computed from PF §9.1). With island prep sink: 12.0 + 7.2 +... | none |
| K-262 | IN | (unchanged) Foyer shares 23.2 ft with kitchen with no opening (PF §8.2); kitchen is first seen from the hall. | none |
| K-270 | MISSING | (unchanged) Fridge to sink 20.4 ft; at 2.5 ft per step that is about 8 steps (assumption). | none |
| K-273 | MISSING | (unchanged) Fridge door side faces the 4 ft M39 entry (fridge x 35.8-38.29, M39 x 38.2-42.2) (PF §4.1, main_floor.scad:201). | none |
| K-274 | MISSING | (unchanged) No dishwasher drawn (PF §8.4); aisle between range run and island is 3.95 ft (47 in), under 54 in. | none |
| K-277 | IN | (unchanged) Sink under the south window (K-124). | none |
| K-279 | IN | (unchanged) Island north end is 4.9 ft from the tall pantry cabinets (y 22.27 vs 27.2) (main_floor.scad:202-203). | none |
| K-281 | IN | (unchanged) Island 68 sf with no cooktop (main_floor.scad:203). | none |
| K-282 | MISSING | (unchanged) Island centre is 8.8 ft from the range but 13.4 ft from the fridge (computed). | none |
| K-283 | IN | (unchanged) Counter beside the range: 4.9 ft north, 8.2 ft south (main_floor.scad:197-198). | none |
| K-288 | MISSING | (unchanged) No dishwasher in main_fixtures (PF §8.4). | none |
| K-290 | MISSING | (unchanged) Fridge is nearer the range (11.3 ft) than the sink (20.4 ft); it is at a run end, 4.3 ft from the pantry, away from the cooking wall... | none |
| K-292 | CONTRADICTED | (unchanged) Tall pantry cabinets form a separate unit on the north wall (x 42.24-49.14), interrupted by openings M39 and M40 (main_floor.scad:202, PF §4.1). | none |
| K-297 | MISSING | (unchanged) FOYER has no window row (PF §5.1); only 2 glass sidelights of 24 in (M2, M3). | none |
| K-298 | MISSING | (unchanged) No powder room (PF §15.14). | none |
| K-299 | IN | (unchanged) Front door, M42, M43 and deck doors M33 overlap on x 72-76.65, so the view runs to the deck (PF §4.1). | none |
| K-300 | IN | (unchanged) Same line ends at the deck doors M33 (double, 72 in). | none |
| K-302 | MISSING | (unchanged) OFFICE has no bathroom adjacent (PF §7.1, §8). | none |
| K-304 | IN | (unchanged) Same as K-201; closets are reached from the bedroom (M49). | none |
| K-306 | CONTRADICTED | (unchanged) BUNK ROOM bed box x 23.16-29.74, y 63.91-66.15, 5 ft high overlaps north window x 21.45-24.95 (main_floor.scad:175; furniture). | none |
| K-307 | MISSING | BEDROOM 2 west windows 5.4 ft x 2 cover 11.4 of 12.67 ft of wall (PF §5.1); master east windows are at the corners (IN). | unchanged: BEDROOM 2 west windows still 11.4 of 12.67 ft |
| K-315 | IN | Same as K-037 | MISSING to IN |
| K-316 | CONTRADICTED | Halls total 891 sf = 16.2% of 5,486 sf; with foyer, mudroom and stair 24.3% (PF §6.1). One 80.5 x 5.5 ft hall is 481 sf (54% of the total). | worse by 18 sf: strict circulation 891 to 909 sf (16.6%) |
| K-317 | MISSING | (unchanged) Room access unchanged: every room opens to the spine or a wing hall (PF §7.1). | none |
| K-318 | IN | (unchanged) Bypass lane x 49.14-59.3 (10 ft) east of the island from M40 to BREAKFAST (computed); master/laundry/stair paths do not enter the kitchen (PF §7.3). | none |
| K-320 | MISSING | (unchanged) Mail and groceries landing missing (K-043, K-116). | none |
| K-323 | MISSING | (unchanged) GREAT ROOM west wall is a 26 ft opening, north wall has 21.9 ft of openings in 26.5 ft (PF §4.1, §5.1). | none |
| K-324 | IN | (unchanged) Zones are separated (see K-062). | none |
| K-325 | MISSING | BEDROOM 2 shares 12.7 ft with laundry/mudroom and 14.8 ft with the garage (PF §2.2). | partly better: laundry/mudroom wall now behind the closet; garage wall remains (11.2 ft) |
| K-326 | MISSING | BEDROOM 2 east and south walls are utility and garage (not buffers); master has closets south and office west. | partly better: closet buffer east, WC north; south is still the garage wall |
| K-328 | IN | (unchanged) No bedroom touches the foyer; nearest is the master 27 ft away (PF §8.2). | none |
| K-329 | IN | Master 42.9 ft (was 103.1) via the bath; BEDROOM 2 24.3 ft and BUNK 20.6 ft to the old LAUNDRY (kept, so both groups are near a washer) | MISSING to IN |
| K-330 | IN | (unchanged) Master-to-laundry route uses the spine and mudroom, not the kitchen (PF §7.3). | none |
| K-331 | IN | Same as K-070 (deal-breaker; the garage-wall caveat stands) | CONTRADICTED to IN (caveat) |
| K-332 | IN | (unchanged) Kitchen/dining and great room are separated by the hall with three openings (4, 5.9, 26 ft) (PF §4.1). | none |
| K-333 | IN | (unchanged) Master closets open from the bedroom (M49) as well as the bath. | none |
| K-334 | IN | (unchanged) No bedroom wall is shared with a living-type room (PF §8.1, §7.1). | none |
| K-335 | IN | Same as K-005: no drive passes BEDROOM 2 or the master wing; garage is at the front-west, not the rear | CONTRADICTED to IN (depends on the site departure) |

## 6. Review Blockers

| ID | Status | Evidence |
|---|---|---|
| CODE-01 stair flight over 3.7 m | **Fixed on the drawing** | Two flights, 18 risers (3,429 mm) and 4 risers (762 mm), 4.4 ft landing (`stair_a.png`, `basement_plan_a.png`, `main_floor_a.scad` `main_stair_a`). Opening and headroom unchanged. Stair, landing framing, foundation and the opening header are for the licensed Alberta engineer. Basement change listed under Departures. |
| STR-04 over 600 m2 | **Fixed** | 584.5 m2 outside face by the matrix method (0.5 ft offset). CODE-03's other offsets were not re-run; at the 0.35 ft offset where CODE-03 puts the 600 line, this plan has more margin than 15.5 m2. Garage trimmed 10 ft. |
| STR-01 basement ICF wall height | **Open** | Basement shell unchanged. |
| STR-02 pool pit under the footings | **Open** | Unchanged. |
| STR-03 pool-room floor span | **Open** | Unchanged; no main-floor bearing wall added. |
| PLB-01 pool drain-down | **Open** | Unchanged (CODE-04 supports it). |

Other code items touched: CODE-02 **fixed** (M28 36 in); CODE-07 mid-landing **fixed**, stair-top landing **open**; CODE-05 patio guard (1,067 mm) **open**, not touched; CODE-11 garage steps/landing **to confirm**.

## 7. Cost drivers

**$ down vs the current model** (relative; the repo has no $/sf figure, so no dollars here).
1. **Less garage:** 243 sf of slab, roof and 2 side-wall runs of 10 ft each are gone; COST-02 calls garage square feet the cheapest to cut, so the saving is the smallest of the three but real.
2. **Costs that come back:** a landing and a turn in the stair (extra stringer, a 4.4 x 4.2 ft platform, redrawn basement foot; engineer), a second W/D hookup with a dryer vent at the far east wall (K-036), and 36 in door frames (23 doors).
3. **Site:** a south drive and apron (a new road cut, grading) replaces the west drive of 4,260 sf (SITE-04); the west-drive cost goes away, the south one comes in. Unpriced; the heated-apron question (COST-05) moves to the south. Net site cost unknown.

## 8. What you give up

A third garage bay and 46 sf of Bedroom 2, to buy a legal stair, a margin under 600 m2 and two deal-breakers, while leaving the 481 sf spine, the foyer, the kitchen and the daylight problems exactly as they are.

## 9. Departures

| Item | Departure | Drawn / costed |
|---|---|---|
| Basement | Stair foot moved east; HALLWAY strip replaced by a west hall piece and an east STAIR FOOT hall; living room opens by two 'open' doors (36-42.4 and 50-54, y 27.6) | `basement_a.scad`, `basement_plan_a.png`; cost: a few partitions plus the stair; included in the stair line above |
| Site | Garage doors face south; the drive comes from the south; the west drive (x -32..-2, y to 42) is no longer needed. Services, septic (-3..3, 52-64) and meters stay where they are but lose the plow pile | Arrow and note on `plan_a.png`; **not** in `site.scad` (read-only); unpriced |
| Shop | None | none |
| Septic (west), well (east) | None | none |
| Envelope | Garage 10 ft shorter at the south; no heated wall moves except the 1 ft bedroom hall move (interior) and the 0.4 ft closet passage (interior) | `main_floor_a.scad` |
| Structure (engineer) | 16 ft garage header on the south wall; stair landing; walk-in closet partition; the bedroom hall wall moved 1 ft (check whether it carries roof trusses: no main-floor wall is marked bearing, STR-13) | flagged, not claimed |
