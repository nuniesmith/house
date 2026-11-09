# Option B: the as-drawn sheet, with Kayla's notes applied

Files in this folder: `main_floor_b.scad`, `basement_b.scad`, `plan_b.png` (the decision plan), `3d_b.png`, `basement_plan_b.png`, `stair_b.png`, `plan_facts_b.md`, `matrix_b.md`, `check_layout.txt`. "PF-B" below means `plan_facts_b.md`. "Current" means the model on `main` (`$RUN/computed/matrix.md`).

## 1. Matrix numbers

| Row | Option B | Current (for reference) |
|---|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED (of 164) | 109 / 52 / 3 | 62 / 89 / 13 |
| Deal-breakers met (of the 12 in ARC's list) | 12 of 12 (K-055 on paper; the recessed pan is an engineer item) | 5 of 12 |
| Review Blockers fixed / open (of 6) | 2 fixed (CODE-01, STR-04) / 4 open (STR-01, STR-02, STR-03, PLB-01) | 0 / 6 |
| Circulation % (strict / with foyer) | 13.6% / 14.8% (737 sf of 5,417) | 16.2% / 21.9% |
| Drain-run index (ft), wet-wall groups, groups stacked over the basement | 1,162 ft (1,014 ft to the alternate exit); 16 groups; 1 of 16 within 5 ft | 879 ft; 14; 1 of 14 |
| Single doors under 32 in / 32-35 in / 36 in+; minimum hall clear width | 0 / 0 / 30; 4.95 ft (raw sliver 1.15 ft) | 7 / 11 / 4; 3.71 ft |
| No-threshold shower | Y (both showers drawn flush; structure item) | N |
| Bedrooms sharing a wall with the living/great room | 0 | 0 |
| A bedroom next to the foyer | N | N |
| Master bed to laundry path | 31.5 ft (MASTER LAUNDRY); 99.3 ft to the family LAUNDRY | 103.1 ft |
| Master suite side | East (N + E exposure) | East |
| Bedrooms with east light | 1 of 3 (master; BEDROOM 2 west, bunk north/west) | 1 of 3 |
| Living spaces facing south | 2 living-kind rooms (LIBRARY 19.0 ft, DEN 14.8 ft) plus the DINING ROOM; GREAT ROOM and KITCHEN face north | 1 (DEN) |
| Living spaces with windows on 2+ walls | 3 living-kind (SUN ROOM, DEN, LIBRARY); 5 rooms in all (+ MASTER BEDROOM, DINING ROOM) | 4 rooms in all |
| Building area, outside face (m2) against 600 | 585.7 (centre lines 565.6); margin 14.3 | 608.0 |
| Basement / shop / site changes | Basement: stair room +25 sf, gym corner and gym door move. Shop: none. Site: garage doors south, new south apron, west drive dropped, meters move to the garage west wall. Envelope: garage trimmed 6.65 ft, front walls 2 ft north. Details in section 9. | - |
| Cost vs the current model | $ down (net, small) | - |

## 2. What it is

The option takes the room arrangement from the architect's sheet `docs/house/floor_plan.JPEG` (Oct 30), read from geometry and fixtures only. On that sheet the front band is, west to east: a blank lobe, a 14.5 x 18.3 ft room, a 12 ft foyer that is open to the back, and a 14.8 ft study with a pantry cell behind it. The kitchen sits in the north-centre: counter and sink on the north wall, an island, and a 6 x 10 ft galley with the range. It is one open room with the great room, and a 28 ft glass wall opens to a walled covered patio. There is no 80 ft spine. The sheet's garage-side stair is not used, so the basement stair stays where the basement expects it.

Option B keeps that arrangement and applies Kayla's notes to it:

- **Front band.** LIBRARY and BREAKFAST (the sheet's lobe), DINING ROOM with a BUTLER, VESTIBULE + FOYER + POWDER, DEN + MEDIA.
- **Kitchen.** KITCHEN (308 sf) between a 30 ft service hall and a 36 ft gallery. It is divided from the great room and the dining room by 5-6 ft openings instead of being one open space (K-332). The range run is on the inside wall, the sink sits under a north window, the island has no sink and no seating, and a 4.6 ft door goes to the covered patio.
- **Garage.** Trimmed from 34.2 to 27.6 ft deep (6.65 ft off the south end), doors turned to face south, and a 3 ft Costco door added between the garage and the pantry.
- **Master suite.** MASTER LAUNDRY in the ex-LINEN room, a 3 ft closet opening from the bedroom, 36 in doors everywhere, a freestanding tub off the exterior wall, curbless showers.
- **Bedroom wing.** BEDROOM 2's closet moved to the interior (x 22.1-28), halls widened to 5.4 ft clear, bunk room split into two pieces, and the stair rebuilt as two flights.

**Stair (CODE-01).** The stair is 11 risers, a 4.6 ft landing, then 11 risers, all straight. It uses the same x (42.65-47.27) and keeps the basement foot at y 28.725. The top nosing moves 3.7 ft north, from y 47.1 to y 50.825, and the main-floor opening is 15.4 ft long (71 sf, was 54 sf). The mid landing is 4.6 ft against the 4.2 ft stair width (CODE-07). The top landing is the hall, 4.57 ft clear. Headroom at the south end of the opening is 6.55 ft (1,996 mm), a 46 mm margin on the same 1,950 mm basis as STR-08 (computed from the stair table; engineer to confirm). See `stair_b.png`.

**Changes vs the current model:**

- 16 wet groups instead of 14.
- Spine 481 sf -> gallery 215 sf + service hall 180 sf.
- Foyer 309 sf -> vestibule 66 + foyer 138 + passage 52 sf.
- FLEX ROOM, upper hall and the den alcove are gone.
- The sun room is 130 sf (was 144).
- Study 79 sf (was 97).
- Bunk room 175 sf in two pieces (was 195).

## 3. Pros

| # | Pro | Evidence |
|---|---|---|
| P1 | Every deal-breaker is met on paper: 12 of 12 (was 5). | Section 5: K-328, K-329, K-330, K-331, K-332, K-333, K-334, K-335, K-036, K-037, K-003/060/061, K-055. |
| P2 | Under the Part 9 size limit with margin: 585.7 m2 against 600 (was 608.0), a 14.3 m2 margin. Fixes STR-04 and CODE-03 without detaching the garage, so the Costco door survives. | Matrix row (0.5 ft offset method); garage 833 -> 671 sf, conditioned 5,486 -> 5,417 sf (PF-B §1). |
| P3 | Laundry tied to the master suite: 31.5 ft from the master bed (was 103.1 ft), through the closet or the bath. BEDROOM 2 and the bunk room keep a laundry 22.8 and 25.0 ft away. | PF-B §7.3; K-036, K-329, K-166, K-203, K-210, K-228 move to IN. Fixes ARC-02. |
| P4 | Costco door: pantry and garage share 8.7 ft of wall with a 3 ft door; about 37 ft from that door to the fridge (was 41.3 ft with no door). | PF-B §8.3; K-037, K-115, K-315 move to IN. Fixes ARC-03. |
| P5 | The drive no longer passes the bedrooms: garage doors on the south wall, nearest drive piece 27.6 ft from BEDROOM 2 (was 9.3 ft). Frees the west side for the septic and services, and removes the snow pile at the dead end. | K-005, K-335 move to IN. Fixes ARC-01, SITE-03, SITE-04; the site change is in section 9. |
| P6 | Circulation: halls 737 sf = 13.6% (was 891 sf, 16.2%); with the foyer 14.8% (was 21.9%). The 481 sf spine is gone. | PF-B §6.1; ARC-07 / COST-07. |
| P7 | Wide doors and halls: 30 of 30 single doors are 36 in, 0 under 36 in; passage openings 45 of 45 are 36 in or wider; minimum hall 4.95 ft clear (was 3.71). | PF-B §4.3, §6.1; K-003, K-060, K-061 move to IN. Fixes ARC-05, CODE-02 (M28 no longer exists). |
| P8 | No closets on exterior walls: 0 of 5 (was 2 of 5). | Matrix row; K-070, K-071, K-331 move to IN. Fixes ARC-04 (for the closets that exist). |
| P9 | Kitchen triangle 18.7 ft with every leg under 9 ft (was 41.4 ft); dishwasher beside the sink; 54 in aisles; fridge ends a run; no island sink. | Fixture rows in `main_floor_b.scad`; K-261, K-274, K-288, K-292, K-108, K-273 move to IN. Fixes ARC-10, ARC-11. |
| P10 | Front entry: vestibule (K-041), powder room 19.7 ft from the front door (K-145), closed coat storage 7.4 ft and a drop shelf. | PF-B §7.3; fixes ARC-09, ARC-14. Moves K-041, K-043, K-044, K-141-K-145, K-298, K-320 to IN. |
| P11 | A real LIBRARY (223 sf, 2 walls of glass) and the covered patio reached from the kitchen. | K-032, K-023, K-127 move to IN. Fixes ARC-15 (library only). |
| P12 | CODE-01 fixed with no basement relocation: the foot stays at y 28.725. The basement gives up 25 sf of gym. | PF-B §10; `basement_b.scad` passes the checker. |

## 4. Cons

| # | Con | Evidence |
|---|---|---|
| C1 | Plumbing is more scattered: drain-run index 1,162 ft against 879 ft (+32%), 16 groups against 14, and only 1 of 16 within 5 ft of a basement group. The master laundry (+133 ft) and powder room (+90 ft) are far from the drain exit at (22.16, 58). | PF-B §9.3-§9.5; K-006 stays MISSING; PLB-03 / PLB-11 get worse. |
| C2 | The kitchen is the thoroughfare between the two wings. With no spine, the west-wing-to-foyer route runs through its 6 ft south lane. The front door to the stair top is 80.7 ft by that route. K-318 and K-330 are scored IN only because the lane is clear of the work zones and the butler/dining route bypasses it. | PF-B §7.3, §8.4. |
| C3 | The active rooms still face north: KITCHEN and GREAT ROOM have north glass only; only LIBRARY, DEN and DINING face south. K-012 and K-099 stay MISSING. | PF-B §2.2, §5.1; ARC-16. |
| C4 | Daylight: the windowless rows include MEDIA 178 sf, FOYER 190 sf, MUDROOM, LAUNDRY, BUTLER and the pantry. K-007 stays MISSING. | PF-B §5.1; ARC-19 (study and office gained a corner window). |
| C5 | Several rooms shrink: study 79 sf (was 97), sun room 130 sf (was 144), bunk room 175 sf in two pieces (was 195), BEDROOM 2's closet 30 sf, mudroom nook 47 sf (was 78), LINEN 55 sf given to the laundry. Bunk room and study still have no closet. | PF-B §3.1; ARC-04 stays open for those two rooms. |
| C6 | BEDROOM 2 still shares walls with the laundry (7.6 ft) and the garage (14.8 ft); the closet buffers only 5.1 ft. K-008, K-325 and K-326 stay MISSING. | PF-B §2.2; ARC-08. |
| C7 | Basement departure: the stair room grows from y 45.34 to y 50.825 (25 sf of gym), and the gym is entered from the music room instead of the basement hall. | `basement_b.scad`; section 9. |
| C8 | Site departure: new south apron and a garage 27.6 ft deep (was 33.5 ft). Whether a crew-cab pickup fits with the Costco steps is not checked here. The west drive and its dead end go away. | Section 9. |
| C9 | Still contradicted: K-075 (two wings, about 53 ft of kitchen, great room and foyer between), K-104 (the master double door is in line with the 36 ft gallery) and K-144 (the front-door line runs up to the great room). | Section 5. |
| C10 | Two laundries (family + master) and a powder room add plumbing, a dryer vent and appliances; the master laundry and powder are the two groups that raise the drain-run index most. | PF-B §9.3; section 7. |
| C11 | Longer stair opening: 71 sf (was 54 sf). The headroom margin is 46 mm (same thin basis as STR-08). The stair's upper end takes the gym's SW corner. A 15.4 ft framed opening is a structural item. | Section 2 stair paragraph; STR-08. |
| C12 | The tool row "Min distance bedroom -> drive" still reads 9.3 ft because `site.scad` is unchanged. The 27.6 ft is hand-measured against the new apron, which is not drawn in `site.scad`. | Matrix row note. |

## 5. Kayla compliance (all 164 PLAN items re-scored)

Counts: **IN 109, MISSING 52, CONTRADICTED 3** of 164 (current: 62 / 89 / 13). 47 items move to IN, none moves down.

Same verdict convention as ARC: partial presence is MISSING.

**Contradicted (3):**

- K-075: two wings separated by the central rooms.
- K-104: the master door is in line with the gallery.
- K-144: the front-door line runs up to the great room.

**Missing (52):**

- Kitchen and entry: K-116, K-153, K-155, K-157, K-257, K-282, K-290, K-297.
- Daylight and orientation: K-007, K-012, K-014, K-064, K-078, K-081, K-099, K-100, K-185.
- Noise and views: K-008, K-009, K-102, K-103, K-105, K-325, K-326.
- Rooms and storage: K-033, K-038, K-040, K-237, K-242, K-245, K-302.
- Wet and shape: K-004, K-006, K-010, K-058, K-059, K-069, K-083, K-220, K-227.
- Outdoors: K-095, K-129, K-134, K-249, K-254.
- Pets and sun room: K-170, K-172, K-189.
- Circulation and walls: K-316, K-317, K-323.
- Bedroom access: K-240.

| K-ID | Verdict | Evidence | Change vs the current model |
|---|---|---|---|
| K-001 | IN | Kitchen, laundry (x2), master suite, BEDROOM 2, bunk room and hall BATH are all on the one main level; basement holds gym/theatre/pool/music only. Unchanged. | same |
| K-002 | IN | Basement stays 3,475 sf (PF-B §1); only its stair room grows 25 sf (basement_b.scad). | same |
| K-003 | IN | All 45 passage openings (doors, doubles, open) are 36 in or wider; 0 under 36 in (PF-B §4.3). Was 8 under 32 in. | MISSING -> IN |
| K-004 | MISSING | Master bath 230 sf and hall BATH 66 sf clear are generous, ensuite WC 6.1 x 6.8 ft, but the two master WCs are still 3.4 ft clear wide (22 sf each); no 60 in turning circle drawn in BATH 2 (62 sf). | same |
| K-005 | IN | Garage doors now face south (y 7.9); the west drive is not used. Nearest drive piece is the apron at y <= 7.9, 27.6 ft from BEDROOM 2 (y 35.46). Needs the site change listed in Departures. Matrix tool still quotes 9.3 ft because it reads the unchanged site.scad. | CONTRADICTED -> IN |
| K-006 | MISSING | 16 wet-wall groups, drain-run index 1,160 ft (PF-B §9.3, §9.5); worse than 14 / 879 ft. Master laundry and powder are two new far groups. | same |
| K-007 | MISSING | No window row: MEDIA 178 sf, FOYER 190, MUDROOM, LAUNDRY, PANTRY, BUTLER (PF-B §5.1). STUDY and OFFICE now have a corner window each. | same |
| K-008 | MISSING | BEDROOM 2 east wall: WIC 5.1 ft (buffer) + LAUNDRY 7.6 ft; south wall 14.8 ft garage. Closet buffer only on 5.1 ft. Master WCs no longer share a wall with a living room (alcove deleted). | same |
| K-009 | MISSING | The bedroom hall still carries the stair landing and the sun-room door, so reaching the sun room means walking the private hall (PF-B §7.1); hall BATH and powder are public-side. | same |
| K-010 | MISSING | Rooms are not on a 2 ft module: 14.54 x 20.0, 19.0 x 11.72, 14.83 x 15.5 (PF-B §3.1). | same |
| K-012 | MISSING | LIBRARY (S, 19 ft), DEN (S, 14.8 ft), DINING (S) and the drive face south; the GREAT ROOM, KITCHEN and DECK still face north. | same |
| K-013 | IN | Master bedroom in the north-east block with north and east exterior walls. Unchanged. | same |
| K-014 | MISSING | Master has 43.5 sf of east glass; BEDROOM 2 west, bunk north/west; SUN ROOM north + east. | same |
| K-021 | IN | Kitchen opens 6 ft to the GREAT ROOM (sofas, 435 sf clear) and the island faces it; BREAKFAST room 219 sf with banquette and table beside the butler. | same |
| K-023 | IN | KITCHEN has a 4.6 ft double door straight to the covered PATIO (185 sf); the DINING ROOM has 6 ft doors to the covered front porch. | MISSING -> IN |
| K-030 | IN | PANTRY / SCULLERY 90 sf clear, 7 ft shelving on 3 walls, door to the garage, plus the 44 sf BUTLER. (Bulk-storage depth is for Kayla to judge.) | MISSING -> IN |
| K-031 | IN | STUDY 81 sf (now with a window) off the bedroom hall; OFFICE 165 sf with a porch door and a corner window. | same |
| K-032 | IN | LIBRARY 223 sf, south + west glass, 7 ft shelving on two walls, seating; shares walls with BREAKFAST and DINING only. | MISSING -> IN |
| K-033 | MISSING | POWDER off the foyer (19.7 ft from the front door) and hall BATH 21 ft from the mud entry, but the OFFICE and master-side rooms are 50+ ft from any bath except the master suite. | same |
| K-034 | IN | SUN ROOM 130 sf (two pieces), N glass 55 sf, E glass 23 sf, double door to the PATIO. | same |
| K-035 | IN | KITCHEN to DINING ROOM through a 6 ft opening (61.0-67.0 at y 29.51), no hall or pantry between; second route through the butler. | same |
| K-036 | IN | MASTER LAUNDRY 55 sf (W/D, ex-LINEN) reached from the east WIC and from the master bath; 31.5 ft from the master bed (was 103.1). | MISSING -> IN |
| K-037 | IN | 3 ft door in the garage/pantry wall x = 24.34 (y 22.3-25.3), 8.7 ft shared wall, three 6 in risers in the garage (garage slab is 1.5 ft lower). | MISSING -> IN |
| K-038 | MISSING | One BROOM / LINEN closet (39 sf, off the sun room); no second broom closet. | same |
| K-040 | MISSING | Only 25 sf linen between the master WCs and BROOM / LINEN beside the hall BATH; none near BEDROOM 2 or the bunk room. | same |
| K-041 | IN | VESTIBULE 66 sf: 6.2 ft front double door, 5 ft interior double door into the FOYER. | MISSING -> IN |
| K-043 | IN | 3 ft drop shelf / mail counter, 6.2 ft long, on the foyer wall beside the powder room. | MISSING -> IN |
| K-044 | IN | Same foyer drop shelf (keys, purse) 5 ft from the front door. | MISSING -> IN |
| K-047 | IN | Vestibule bench 1.5 x 3.8 ft at the front door; mud bench and lockers by the garage entry. | same |
| K-053 | IN | Master bed floats: 4.8 ft east and 7.6 ft south clear. Unchanged. | same |
| K-055 | IN | Master shower (8.2 x 4.5 ft) and hall-bath shower drawn flush (0.02 ft). A curbless pan needs a recessed floor: structural item for the engineer (ARC-06). | MISSING -> IN |
| K-058 | MISSING | No shaft reserved; the stair is longer (4.62 x 15.4 ft opening). | same |
| K-059 | MISSING | No dumbwaiter shaft; basement LAUNDRY is not under either main laundry. | same |
| K-060 | IN | Clear halls: HALL @22.1 5.4 ft (64 in), service hall 5.5 ft, gallery 5.5 ft, N-S hall 5.0 ft, stair landing 4.2 ft; min hall 4.95 ft (PF-B §6.1). Was 3.71 ft. | MISSING -> IN |
| K-061 | IN | 29 of 29 single doors are 36 in; 14 doubles 60 in or more. | MISSING -> IN |
| K-062 | IN | Zones divided by 22 full openings (4-26 ft) and 14 doubles; kitchen / great room 6 ft, kitchen / dining 6 ft. | same |
| K-064 | MISSING | 5 rooms have windows on 2 walls (SUN ROOM, MASTER BEDROOM, DEN, DINING ROOM, LIBRARY; was 4); GREAT ROOM, KITCHEN, BREAKFAST one wall; MEDIA none. | same |
| K-069 | MISSING | 18 outside + 14 inside corners, 412.6 ft heated perimeter (PF-B §1.2) vs 17 + 13 and 395.5 ft: the garage jog adds corners. | same |
| K-070 | IN | 0 of 5 closet rooms touch an exterior wall (garage excluded): BEDROOM 2 WIC moved to the interior (x 22.1-28), LINEN became a laundry, MECH fills the old alcove. | CONTRADICTED -> IN |
| K-071 | IN | All 5 closet rooms entirely on interior walls (matrix row). Bunk room and study still have no closet (ARC-04 stays open). | MISSING -> IN |
| K-072 | IN | Hall BATH: vanity by the door, toilet between door and shower, shower at the far end; fan over the shower is a spec item. | same |
| K-074 | IN | Master tub freestanding 2.4 ft off the east wall; BATH 2 tub on an interior wall, 1.0 ft off the west wall (marginal). | CONTRADICTED -> IN |
| K-075 | CONTRADICTED | Bedroom wing (x 7-43) and master wing (x 96-128) are still two wings with kitchen, great room and foyer between (about 53 ft). | same |
| K-077 | IN | No room has windows directly opposite; window pairs are N/E, S/W, S/E (PF-B §5.1). | same |
| K-078 | MISSING | Windows pulled to corners in BEDROOM 2, bunk, study, office, den; GREAT ROOM and KITCHEN still one wall of glass, so no diagonal cross-breeze. | same |
| K-080 | IN | No window centred on its wall: DEN 81-95.95 window at 82.5-87.5; LIBRARY two windows at 37.7 and 46; GREAT ROOM at 77.8 and 89.4. | MISSING -> IN |
| K-081 | MISSING | BEDROOM 2 has 40 sf of west glass (was 54 sf) with no porch or overhang. | same |
| K-083 | MISSING | Ratios 1.4-1.6 only for GREAT ROOM 1.55, KITCHEN 1.46, LIBRARY 1.62, BREAKFAST 1.65; DEN 1.05, BEDROOM 2 1.17, MASTER 1.27. | same |
| K-095 | MISSING | FRONT PORCH still 15.26 ft (4.65 m) deep in front of dining and library glass; PATIO 12.73 ft. | same |
| K-096 | IN | Range run and tall pantry cabinet on the inside west wall (x 54.6); only the sink run (base cabinets under a 4.5 ft window, no overheads) is on the exterior north wall. | CONTRADICTED -> IN |
| K-099 | MISSING | DINING and LIBRARY face south; KITCHEN and GREAT ROOM face north. | same |
| K-100 | MISSING | Master east windows only; BEDROOM 2 west; bunk north and west. | same |
| K-102 | MISSING | Hall BATH toilet is 4.1 ft inside the door line; POWDER toilet 4.8 ft inside its door. | same |
| K-103 | MISSING | The POWDER door faces the foyer; BEDROOM 2 bed still sees BATH 2 door through the 7.9 ft suite-entry opening. | same |
| K-104 | CONTRADICTED | The 36 ft gallery (x 69-105) ends at the 4.6 ft master double door, so the master bedroom is in line from the great room. | same |
| K-105 | MISSING | MUDROOM is open 8.8 ft to the service hall and the laundry door is in its north wall. | same |
| K-106 | IN | Island 4.0 x 7.2 ft (29 sf), no stools, no cooktop. | same |
| K-107 | IN | BREAKFAST room: 7 ft banquette on one side, round table 4.5 ft, chairs on the rest. | same |
| K-108 | IN | No sink in the island; the only kitchen sink is on the north run. | CONTRADICTED -> IN |
| K-114 | IN | PANTRY / SCULLERY (sink, shelving, 90 sf clear) plus a BUTLER with coffee counter, both on the garage-to-kitchen route. | same |
| K-115 | IN | Same as K-037: 1 door, 8.7 ft shared wall. | MISSING -> IN |
| K-116 | MISSING | Garage Costco door to the fridge is about 37 ft by the pantry and service hall (was 41.3 ft); not "near". | same |
| K-117 | IN | 6 ft coffee counter in the BUTLER, open 5 ft to the BREAKFAST room; pot filler is a spec item. | MISSING -> IN |
| K-123 | IN | Island long side faces the GREAT ROOM across the 6 ft opening. | MISSING -> IN |
| K-124 | IN | Sink centred 3.5 ft from the west end of a 4.5 ft window on the north wall. | same |
| K-127 | IN | KITCHEN door to the covered PATIO (4.6 ft); DINING ROOM doors to the covered front porch. | MISSING -> IN |
| K-128 | IN | Dining table 3.8 x 8.5 ft seats 8; 5+ ft clear to the walls. | same |
| K-129 | MISSING | Largest exterior door on the dining side is a 6 ft double; no folding or sliding wall. | same |
| K-132 | IN | GREAT ROOM 435 sf clear with three sofa boxes and a table. Unchanged. | same |
| K-133 | IN | GREAT ROOM 6 ft double door to the DECK; SUN ROOM / PATIO beside the kitchen. | same |
| K-134 | MISSING | Exterior doors are 6 ft doubles (great room, dining) and 6.5 ft (office). | same |
| K-140 | IN | Vestibule bench and mud bench. | same |
| K-141 | IN | 7 ft closed coat storage, 7.4 ft run on the foyer west wall; lockers in the mudroom. | MISSING -> IN |
| K-142 | IN | Same closed storage (hidden coat/shoe); no wine racks. | MISSING -> IN |
| K-143 | IN | Foyer drop shelf (K-043). | MISSING -> IN |
| K-144 | CONTRADICTED | Front door line (x 72-78) runs up the foyer passage to the GREAT ROOM (deck doors in line); the kitchen is behind the west wall. | same |
| K-145 | IN | POWDER 38 sf off the foyer. | MISSING -> IN |
| K-146 | IN | Mud bench and cabinets 2.7 x 3 ft in the mudroom nook (smaller than before). | same |
| K-147 | IN | Lockers 1.6 x 4.3 ft, 7 ft high, in the mudroom. | same |
| K-149 | IN | Lockers in the mudroom. | same |
| K-151 | IN | Bench and lockers 6-10 ft from the garage mud-entry door. | same |
| K-153 | MISSING | No mail/command area in the mudroom (it is in the foyer). | same |
| K-155 | MISSING | The MUDROOM nook has no exterior door; the side-entry door goes into the pantry, not the mudroom. | same |
| K-156 | IN | Garage door (x 24.34, y 31.9) into the service hall; mudroom open 8.8 ft to it. | same |
| K-157 | MISSING | Hall BATH is 21 ft from the mud entry on the same hall, not off the mudroom. | same |
| K-158 | IN | See K-036. | MISSING -> IN |
| K-163 | IN | Laundry sink 1.9 x 2.5 ft in LAUNDRY. | same |
| K-166 | IN | MASTER LAUNDRY opens off the east WIC (door x 121.94) and the bath: laundry basket does not leave the suite. | MISSING -> IN |
| K-170 | MISSING | Dog wash stays in the basement PET ROOM (basement.scad:134). | same |
| K-172 | MISSING | No litter area; PET ROOM has no door to the garage. | same |
| K-179 | IN | Hall BATH off the service hall; master bath; BATH 2 reached from the suite entry. | same |
| K-183 | IN | OFFICE 6.5 ft door to OFFICE PORCH 147 sf. | same |
| K-185 | MISSING | SUN ROOM north wall 5 + 3.5 ft of window in 11.3 ft; east wall 3.6 ft window + 4.9 ft door. | same |
| K-186 | IN | SUN ROOM 4.9 ft double door to the PATIO. | same |
| K-188 | IN | SUN ROOM 117 sf clear with two sofas. | same |
| K-189 | MISSING | No dining set drawn in the sun room. | same |
| K-191 | IN | Master 6.05 ft double door to MASTER PORCH 175 sf. | same |
| K-192 | IN | Only fireplace is in the GREAT ROOM. | same |
| K-195 | IN | Master 412 sf clear, bed 4.8 ft from the east wall. Unchanged. | same |
| K-200 | IN | Two WICs: 95 sf and 89 sf. | same |
| K-201 | IN | Closets open from the bedroom through a 3 ft opening (was 27.6 in) and from the bath through a 3 ft door. | same |
| K-202 | IN | Bath reaches the closets through the passage (door 3 ft). | same |
| K-203 | IN | East WIC has a 3 ft door into the MASTER LAUNDRY. | MISSING -> IN |
| K-210 | IN | MASTER LAUNDRY in the suite. | MISSING -> IN |
| K-211 | IN | Master shower 8.2 x 4.5 ft drawn flush; recessed floor to be confirmed by the engineer. | MISSING -> IN |
| K-220 | MISSING | Tub 4.5 x 5.4 ft is a raised freestanding box, not sunken. | same |
| K-224 | IN | Double vanity 9.9 x 1.8 ft. Unchanged. | same |
| K-226 | IN | 25 sf linen between the WCs plus laundry shelving; the old 55 sf LINEN is now the laundry, so linen is smaller than before. | same |
| K-227 | MISSING | Master WCs are still 3.4 ft clear wide; their doors are now 36 in. | same |
| K-228 | IN | MASTER LAUNDRY door off the master bath (x 122.6, 3 ft). | MISSING -> IN |
| K-229 | IN | Closet passage door to the bath (3 ft). | same |
| K-237 | MISSING | No flex room; MEDIA (178 sf) and STUDY (81 sf) have no window or too small for a bed. | same |
| K-238 | IN | BEDROOM 2 14.4 x 12.3 ft clear; queen fits on the east wall (8.5 ft free beside the WIC door). | same |
| K-239 | IN | BATH 2 19.5 ft from the BEDROOM 2 centre, plus an ensuite WC through a 3 ft door. | same |
| K-240 | MISSING | BEDROOM 2 has no exterior door; shares 14.8 ft with the garage, no door. | same |
| K-242 | MISSING | Two non-master bedrooms (BEDROOM 2, bunk room); no fourth. | same |
| K-244 | IN | BATH 2 opens to the suite entry and the bunk room. | same |
| K-245 | MISSING | OFFICE beside the master is an office, not a bedroom. | same |
| K-248 | IN | FRONT PORCH 796 sf with posts and roof, 2 ft further north. | same |
| K-249 | MISSING | Side-entry porch (84 sf, under the main roof) leads to the pantry, not to a mudroom. | same |
| K-252 | IN | DECK 322 sf under the porch roof. | same |
| K-253 | IN | DECK and PATIO adjoin. | same |
| K-254 | MISSING | No unroofed sun area identified; 7 porch roof blocks. | same |
| K-255 | IN | OFFICE PORCH 147 sf. | same |
| K-256 | IN | Range: 3.0 ft and 1.4 ft of counter either side; sink: dishwasher (2 ft) west, 1.5 ft of counter east (>= 15 in). | same |
| K-257 | MISSING | Fridge is at the north end of the west run beside the dishwasher; only 0.4 ft of counter touches it. | same |
| K-261 | IN | Fridge-sink 5.1 ft, sink-range 8.5 ft, range-fridge 5.1 ft = 18.7 ft total, every leg under 9 ft (centres, from fixture rows). | MISSING -> IN |
| K-262 | IN | Kitchen opens west of the foyer passage; the island and range are out of the front-door line; only the lane end shows from the passage. | same |
| K-270 | IN | Legs of 5.1, 8.5 and 5.1 ft = 2 to 4 steps at 2.5 ft per step (assumption). | MISSING -> IN |
| K-273 | IN | Fridge door opens into the 4.5 ft island aisle, with no entry through that aisle (entries are at the south end). | MISSING -> IN |
| K-274 | IN | Dishwasher on the north run with 4.6 ft (55 in) of aisle to the island; west aisle 4.5 ft (54 in). | MISSING -> IN |
| K-277 | IN | Sink under the north window. | same |
| K-279 | IN | Island 4.6 ft from the north run and 4.5 ft from the west run is the landing; tall pantry cabinet at the south end of the west run. | same |
| K-281 | IN | Island 29 sf, no cooktop. | same |
| K-282 | MISSING | Island centre is 8.0 ft from the range but 10.6 ft from the fridge, not between them. | same |
| K-283 | IN | 3.0 ft and 1.4 ft of counter either side of the range. | same |
| K-288 | IN | Dishwasher drawn next to the sink (x 57.4-59.4). | MISSING -> IN |
| K-290 | MISSING | Fridge ends a run and is clear of the range, but it is 5.1 ft from both the sink and the range (not nearer the sink) and 22 ft from the pantry. | same |
| K-292 | IN | Tall pantry cabinet ends the west run; fridge ends it at the north; no separate tall wall. | CONTRADICTED -> IN |
| K-297 | MISSING | FOYER has no window row; only 2 sidelights of 24 in in the vestibule. | same |
| K-298 | IN | POWDER 38 sf. | MISSING -> IN |
| K-299 | IN | Front door line ends at the great room deck doors (x 70.65-76.65), as before. | same |
| K-300 | IN | Same line, double door to the deck. | same |
| K-302 | MISSING | OFFICE has no bathroom adjacent. | same |
| K-304 | IN | Closets are reached from the bedroom (3 ft opening). | same |
| K-306 | IN | Bunk beds moved off the north window: bed boxes at y 56-62.5 and 58.8-65.3, window at x 25-28.5; west window at the corner. | CONTRADICTED -> IN |
| K-307 | IN | BEDROOM 2 west windows are two 4 ft units at the corners (0.8 and 0.5 ft from them); master east windows at the corners. | MISSING -> IN |
| K-315 | IN | Same as K-037. | MISSING -> IN |
| K-316 | MISSING | Halls 737 sf = 13.6% (was 891 sf, 16.2%); 14.8% with the foyer (was 21.9%). No single 481 sf spine, but the gallery (215 sf) and service hall (180 sf) are still 54% of it. | CONTRADICTED -> MISSING |
| K-317 | MISSING | Most rooms still open to a hall; the spine is gone but the gallery and service hall remain. | same |
| K-318 | IN | The kitchen is the route between the wings, but the lane is its 6 ft south edge, clear of the island and runs, and a second route runs through the butler and dining room (door at x 69.14, y 24). | same |
| K-320 | IN | Landings at the entry: bench 3.8 ft, coat storage 7.4 ft, drop shelf 6.2 ft; groceries through the garage-pantry door. | MISSING -> IN |
| K-323 | MISSING | GREAT ROOM south side is a 26 ft opening, west 6 ft, north wall 13.9 ft of glass and doors in 26.5 ft. | same |
| K-324 | IN | Zones separated (see K-062). | same |
| K-325 | MISSING | BEDROOM 2 shares 7.6 ft with the laundry, 5.1 ft with the WIC and 14.8 ft with the garage. | same |
| K-326 | MISSING | WIC buffers 5.1 ft only; laundry and garage walls remain. | same |
| K-328 | IN | No bedroom touches the foyer or vestibule; nearest bedroom is the master, 27.5 ft away. | same |
| K-329 | IN | Family LAUNDRY 22.8 ft from BEDROOM 2 and 25.0 ft from the bunk room; MASTER LAUNDRY 31.5 ft from the master bed. | MISSING -> IN |
| K-330 | IN | Wing-to-wing traffic uses the 6 ft lane south of the island (no range or dishwasher on it) or the butler/dining bypass; master laundry removes the laundry route. | same |
| K-331 | IN | See K-070: 0 of 5 closets on exterior walls. | CONTRADICTED -> IN |
| K-332 | IN | Not one open space: kitchen, dining, great room and library are divided by walls with 5-6 ft openings. | same |
| K-333 | IN | Closets open from the bedroom (3 ft) as well as the bath. | same |
| K-334 | IN | No bedroom shares a wall with a living-kind room (matrix row = 0). | same |
| K-335 | IN | See K-005. | CONTRADICTED -> IN |

**Deal-breakers (ARC's 12 rows):** K-328 IN, K-329 IN, K-330 IN, K-331 IN, K-332 IN, K-333 IN, K-334 IN, K-335 IN, K-036 IN, K-037 IN, wide doors and halls (K-003/060/061) IN, K-055 IN. K-055 is "IN on paper": the shower is drawn flush, and a curbless pan in a wood-framed floor needs a recessed floor that the engineer must confirm.

## 6. Review Blockers

| ID | Status | Evidence |
|---|---|---|
| CODE-01 (stair 4,191 mm in one flight) | **Fixed** | Two flights of 11 risers (2.1 m each), 4.6 ft landing, same x, foot unchanged at y 28.725; basement variant passes the checker. Headroom margin 46 mm and the 15.4 ft opening go to the engineer. |
| STR-04 (over 600 m2) | **Fixed** | 585.7 m2 by the matrix method (centre lines 565.6). 14.3 m2 margin. The garage is kept, attached. |
| STR-01 (ICF wall height 3.70 m) | Open | Basement height unchanged. |
| STR-02 (pool pit below footings) | Open | Not a main-floor item. |
| STR-03 (pool floor span 26.95 ft) | Open | No bearing wall is claimed over the pool-room support line; the engineer decides. |
| PLB-01 (pool drain-down and backwash) | Open | Basement item. |

Should-fix code items this layout answers:

- CODE-02: no door into the stair landing; the top is a 4.1 ft opening plus a 4.0 ft opening, both 36 in or wider.
- CODE-03: see STR-04.
- CODE-05: the patio guard is drawn at 44 in (3.67 ft).
- CODE-07: mid landing 4.6 ft and top landing 4.57 ft against a 4.22 ft (1,286 mm) stair width.
- CODE-11: porch floors unchanged; the Costco steps need a landing and a guard check (the garage steps are drawn at 6 in risers).

## 7. Cost drivers ($/$$/$$$ vs the current model: **$ down, net, small**)

1. **Less enclosed area.** The garage goes from 833 to 671 sf (-162 sf, the cheapest square feet per COST-02) and conditioned area from 5,486 to 5,417 sf (-69 sf). The repo's only dollar handle is plant capacity of about $550-$2,900 per 100 sf (`findings/07-cost-ve.md:75`, a computed upper bound), so about -$380 to -$2,000 of plant, plus the build cost of the area. Relative terms otherwise.
2. **More plumbing and appliances.** The second laundry and the powder room add 2 wet groups, a dryer vent and a W/D set (PF-B §9.3). Drain-run index +32%. Cost up, $.
3. **Stair, doors and shower floors.** A 15.4 ft framed floor opening with a landing; 30 single doors at 36 in; two recessed (curbless) shower floors (ARC-06, $$); Costco steps. Cost up, $ to $$.
4. **Site.** A new south apron replaces the west drive (cost-neutral to $ up depending on the lot). The meters and services move to the garage west wall.

The net is "$ down" because the area saving is large (-231 sf of enclosed area) against modest additions. This is a relative statement; the repo has no $/sf for floor area.

## 8. What you give up

Plumbing compactness and daylight on the active side: the drain-run index rises 32% (879 -> 1,162 ft), the kitchen and great room still face north, and the kitchen becomes the route between the two wings.

## 9. Departures

| Item | Change | Drawn | Cost |
|---|---|---|---|
| Envelope | Garage trimmed from y 1.25 to y 7.9. Dining room and den front walls moved from y 0 to y 2.0; foyer from 3.72 to 5.0. Front porch moved 2 ft north (depth unchanged, 15.26 ft). Den alcove (x 95.95-99.7) is now a MECH closet. | `plan_b.png`, `main_floor_b.scad` | $ down (-231 sf enclosed) |
| Basement | STAIR UP room y 28.725-45.34 -> y 28.725-50.825 (+25 sf); GYM split in two (corner x 42.65-47.27 lost); gym door moves from x 42.65 (y 46.2) to the music room wall (y 52.0). Foot unchanged. | `basement_b.scad`, `basement_plan_b.png`, `stair_b.png` | $ (framing for a longer opening; one wall moved) |
| Site: drive | The west drive (x -32..-2, to y 42) is not used. The garage doors face south, so a new apron x -2..24.5, y about -20..7.9 joins the front loop. Nothing in `site.scad` is edited. Drive-to-BEDROOM 2 distance becomes at least 27.6 ft. | text only (no site plan drawn) | $ to $$, lot dependent |
| Site: services | The meters under BEDROOM 2's west window move to the garage west wall (x 0, y 10-30, no window). The septic (x -3..3, y 52-64), well (150, 75) and shop are unchanged; the septic loses the snow pile that drained onto it (SITE-03/04). | text only | $ |
| Shop, septic, well, tunnel | None. | - | - |

The coordinator did not run `make_drawings.py` or touch `site.scad`; the south apron must be drawn if Option B is chosen.

## Sheet calibration (how the sheet was read)

See `README.md` for the fit and residuals.
