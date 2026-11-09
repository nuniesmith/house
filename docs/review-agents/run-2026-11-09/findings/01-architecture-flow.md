# Architecture / Flow review (ARC)

- **Specialist:** Architecture / Flow (Wave 1), prefix `ARC`
- **Date:** 2026-11-09
- **Model reviewed:** `main` @ `d20a2fa`, main floor traced from `main_floor.jpg` (the A/B baseline call is Jordan's; no finding here presumes it).
- **Inputs read:** `plan_facts.md` in full (cited as PF §N); `renders/current_main_floor_plan.png`; `kayla_checklist.md` (K-001 to K-335); `models/main_floor.scad` (fixtures and furniture, lines 196-272); the Oct 28 review "Kayla's notes: what changed" section (lines 1080-1180); `Redesign-and-Spec-2026-11-02.md` top updates; `docs/small_house/IMG_0415.PNG` and `IMG_0416.PNG`; ABC 2023 pages 841-842 via the code library.
- **Assumptions held:** land and road side not chosen (road south, drive west per `site.scad:8, 111`); tunnel dropped on `main` (not in scope of this brief); structural and gas items are for a licensed Alberta engineer; a king bed is taken as 76 x 80 in and a queen as 60 x 80 in (stated assumption, not from the repo).
- **Tool use:** no repo edits; scratch files only in `$RUN/work/ARC/`. I did not re-run `check_layout.py`; PF §0 records it passing, and it already tests door swings against fixtures and leaves.

## Findings

No Blockers found. Nothing in the architecture review prevents a permit by itself; the one code item (ARC-05) has a compliant line of passage on paper. The Kayla deal-breakers are Should fix.

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|
| ARC-01 | Should fix | West drive vs bedroom wing; garage doors | The west drive (x -32..-2, to y=42) runs 9.3 ft from BEDROOM 2, 11.1 ft from its WIC, 13.0 ft from the suite WC and 16.2 ft from BATH 2; the garage doors face it. Kayla's deal-breakers K-005 and K-335 are both CONTRADICTED. The master suite is 23 ft or more from the front loop. Land and road side are assumptions, so a different lot orientation could remove this; as drawn it fails. | PF §8.5 (BEDROOM 2 9.3 ft); `site.scad:111`; `main_floor.scad:117-118`; PF §5.1 (two west windows, 54 sf) | — | $$ (garage doors to the south face, or the wing moved) |
| ARC-02 | Should fix | Laundry placement | LAUNDRY is 103.1 ft by door path from the master bedroom and 20.3 to 22.7 ft from BEDROOM 2 and BUNK ROOM. The master suite has no W/D (K-036, K-158, K-166, K-203, K-210, K-228 MISSING). The Oct round-2 "master laundry" did not carry into the Nov model. Zero-area fix: rename LINEN (121.94,20.56 to 128.13,29.51, 55 sf, 6.19 x 8.95 ft) to MASTER LAUNDRY. It already has a 36 in door M53 from the master bath, an east window, and sits against the bath wall y=20.56 beside the double vanity (x 111.64-121.51). Linen storage then lives only in the 25 sf closet between the WCs. | PF §7.3 (103.1 ft); PF §3.1 rows `main_floor.scad:88`; PF §4.4 (M53 36 in); PF §5.1 (LINEN east window) | needs CEC check (dryer circuit) | $ (no area change; supply, drain and vent in a wall already used by the bath) |
| ARC-03 | Should fix | SCULLERY / garage wall | No pantry-to-garage "Costco door" (K-037, K-115, K-315, K-116 MISSING). SCULLERY shares 8.7 ft of wall with the garage (x=24.34, y 20.82-29.51) with 0 doors. Garage-to-groceries route today: garage door M12 to hall, east 14 ft, through the 4 ft opening M39 beside the fridge, then door M13: 41.3 ft to the pantry cabinets, 47.9 ft to the scullery centre. The wall x=24.34 has a clear 4.27 ft between counters (y 22.93-27.2) for a 3 ft door. The garage slab is 1.5 ft below the house floor, so a door there needs 3 risers or a raised garage landing (the garage already has steps at y 15.6-19.6 and 30.5-35.2). | PF §8.3; PF §7.3; PF §1.1 (garage 1.5 ft down); `main_floor.scad:207-209`, `:290` | — | $ (one door, three risers; check with the architect, K-037 is a deal-breaker) |
| ARC-04 | Should fix | Closets on exterior walls; bunk room and study without closets | WIC @7.27,48.13 (20 sf, 6.5 x 3.0 ft) has 3.0 ft of exterior west wall; LINEN has 1.2 ft north and 9.0 ft east exterior. Only the two master WICs (95 and 94 sf) are fully interior. K-070 and K-331 (deal-breaker) are CONTRADICTED; K-071 MISSING. BUNK ROOM (195 sf) and STUDY have no closet row at all. The BEDROOM 2 closet is 2.6 ft clear deep with 1.1 ft of shelving leaving a 1.5 ft aisle: it works as a reach-in, not a walk-in (an open 5.9 ft side, M22). | PF §2.2, §8.3; PF §3.1; `main_floor.scad:56`; M22 PF §4.1; shelf row `main_floor.scad:231` | — | $ (closet rectangles move inboard, no area growth) |
| ARC-05 | Should fix | Door widths, bedroom wing and master closet | 8 of 37 passage openings are narrower than 32 in: M20 31.2, M21 28.2, M23 28.8, M28 28.8, M49 27.6, M54 31.2, M55 28.8, M56 31.2 (PF §4.3). K-003, K-061 (and K-060) are MISSING for the wide-door requirement; two of the eight are daily routes: M28 (N-S hall to the stair landing) and M49 (master bedroom to the closet passage, the K-201 access). Code: ABC lists 810 mm minimum for doors at the entrance to stairs to a finished level and for "all doors in at least one line of passage from the exterior to the basement". M28 (28.8 in = 732 mm) is on the shortest garage-to-stair route (31.6 ft). A line through M31 (32.4 in = 823 mm) from the front door via M42, M43, M32, M31, M30 is compliant on paper, but only by the 13 mm margin on M31: confirm with the designer which line is declared. Table 9.5.5.1 sets 610 mm for bathroom and WC doors, so M20, M21, M23, M54-M56 pass the code but not Kayla's note. | PF §4.1, §4.3, §4.4, §7.3 | ABC 2023 Table 9.5.5.1. - abc_2023 p.842 (see citation log) | $ (door and frame changes; widening M28 means moving the stair-landing wall edge) |
| ARC-06 | Should fix | Showers and WCs | K-055 (deal-breaker) MISSING: both showers are drawn as 0.15 ft (1.8 in) tile boxes above the floor (hall BATH 5.6 x 2.5 ft, master 8.2 x 4.5 ft). A curbless shower in a wood-framed main floor needs a recessed or lowered floor area under it; that is a structure item. Master WC rooms are 3.4 ft clear wide with 31.2 in doors (K-227 MISSING for "spacious/wide") and hall BATH is 60 sf (K-004). No bathroom shows a 60 in turning circle. | `main_floor.scad:224, :226`; PF §3.1 (rows :90, :92); PF §4.4 | — | $$ (framing recess; see structural report) |
| ARC-07 | Should fix | Circulation total and the 80-ft spine | Halls total 891 sf = 16.2% of 5,486 sf conditioned (16.4% without the stair opening). Add the foyer (309 sf), mudroom (78) and the stair opening (54) and it is 24.3%. One hall (24.34,29.51 to 105.2,35.46) is 481 sf, 80.5 x 5.5 ft clear, 54% of all hall area. About 158 sf of it is the 26.5 ft where the great room opens onto it (M43 is 26 ft): it reads as part of the great room. K-316 CONTRADICTED, K-317 MISSING. The spine is also what puts the master 80 ft from the front door and the bedroom wing (K-075). | PF §6.1; PF §3.1; M43 PF §4.1 | — | $$ (area is cost; no dollar figure in the repo) |
| ARC-08 | Should fix | Bedroom wing noise adjacency (the sore spot) | BEDROOM 2 shares 12.7 ft of its east wall with LAUNDRY (7.6 ft) and MUDROOM (5.1 ft) and 14.8 ft of its south wall with the garage: K-008, K-325, K-326 MISSING; K-081 MISSING (54 sf of west glass, no overhang or porch on that side). Its north wall is 13.8 of 14.83 ft open (M18 7.9 ft + M22 5.9 ft) and the west wall is 11.4 ft of 12.67 ft windows, so a queen (5.0 x 6.67 ft) can only go on the east (laundry) or south (garage) wall. See "The sore spot" for two alternatives. | PF §2.2, §3.1, §4.1; PF §5.1 | — | $ to $$ (see alternatives) |
| ARC-09 | Should fix | No powder room | No half bath on the main floor. Nearest toilet room from the foyer is the hall BATH, 65.8 ft away (PF §7.3). K-033, K-145, K-157, K-298 MISSING. Hall BATH (6.3 x 9.5 ft clear) opens from the upper hall. A powder room would need to come out of the MUDROOM (78 sf) or the foyer (309 sf); both sit next to the entries. | PF §15.14; PF §7.3 (65.8 ft); PF §3.1 | — | $$ (plumbing group; DRI +) |
| ARC-10 | Should fix | Kitchen layout | Work triangle (centres) fridge-sink 20.4 ft, sink-range 9.7 ft, range-fridge 11.3 ft = 41.4 ft total against Kayla's 26 ft total / 9 ft per side (K-261). Using the island prep sink as the "sink" it is 30.5 ft, but the island sink is CONTRADICTED by K-108. No dishwasher is drawn (K-288 MISSING). The aisle between the range run and the island is 3.95 ft (47 in) versus 54 in (K-274). No counter touches the fridge: the scullery door M13 (y 23.3-26.3) sits between the range run end (y 22.6) and the fridge (y 25.89), so K-257 MISSING. The kitchen sink run is on the south exterior wall and the range run on the west exterior wall (K-096 CONTRADICTED); the tall pantry forms a separate unit (K-292 CONTRADICTED). Positives: sink under the window (K-124), 15 in landing both sides of range and sink (K-256), a 10 ft bypass lane east of the island (K-318 IN). | `main_floor.scad:197-205`; PF §9.1 equipment; PF §8.4 | — | $ to $$ (cabinet layout, no area) |
| ARC-11 | Consider | Kitchen entries | The 4 ft opening M39 (x 38.2-42.2) lands in the 3.95 ft cooking aisle between the range run and the island, and the fridge door side faces it (K-273 MISSING). M40 (x 48.9-54.8) starts 0.24 ft inside the pantry cabinet end (x 49.14). The Oct kitchen note asked for 2 paths of travel; here there are two (M39 into the aisle, M40 into a 10 ft lane), but a person coming from the garage uses M39. | `main_floor.scad:201-203`; PF §4.1 M39, M40 | — | $ |
| ARC-12 | Should fix | BUNK ROOM | Bunk beds are drawn as 2.96 x 5.26 ft and 6.58 x 2.24 ft boxes, 5 ft high (not full-size beds). The second box (x 23.16-29.74, y 63.91-66.15) sits directly under the north window (x 21.45-24.95, sill 2.5 ft): K-306 CONTRADICTED. The room has no closet (ARC-04). It opens to BATH 2 by a 28.8 in door (M23). Room is 195 sf, 14.7 x 12.5 ft clear, so it fits two twins plus a closet if windows move. | `main_floor.scad:249-250`; PF §5.1 (BUNK window); PF §4.4 | — | $ |
| ARC-13 | Consider | Sight lines | (a) The 80.5 ft spine looks straight through double door M47 (55 in) and the 64.8 in opening M48 into the master bedroom (K-104 CONTRADICTED). (b) From BEDROOM 2's bed (x 14.8-19.2) a straight line runs through M18 (7.9 ft) and M19 (3.5 ft) to the BATH 2 door M20 (K-103 MISSING). (c) The front door, M42, M43 and the deck doors M33 align on x 72-76.65, so the entry sees the whole great room (K-144 CONTRADICTED) while the kitchen is hidden behind a wall with no opening (K-262 IN) and the deck doors are the focal point (K-299, K-300 IN). (d) The mudroom is open 12.4 ft to the hall, with the laundry door in its far wall (K-105 MISSING). | PF §4.1; PF §3.1 | — | $ |
| ARC-14 | Should fix | Entry sequence, drop zones | K-041 MISSING: no vestibule; the 74.4 in double door M1 opens into the 12 x 25.8 ft FOYER (309 sf). The foyer holds a 6.6 ft bench and 10.5 ft of 7 ft-high "wine racks" only (K-141, K-142, K-143, K-043, K-044 MISSING). The mudroom has no exterior door (K-155, K-249 MISSING) and no mail/command centre (K-153). Foyer glass is two 24 in sidelights and no window row (K-297). The foyer is the biggest single "circulation" room after the spine. | PF §3.1, §4.1, §5.1; `main_floor.scad:238-239` | — | $ to $$ |
| ARC-15 | Should fix | Library, flex and bedroom count | No library room on the main floor (K-032); the "Bedroom 3 and 4" and nursery-near-master items (K-242, K-245) are MISSING: two non-master bedrooms plus FLEX ROOM (151 sf, no window row, so it cannot sleep someone without a window). OFFICE (165 sf) shares wall x=108.62 with the master bedroom, a natural nursery or bedroom 3, and has an exterior door to OFFICE PORCH. | PF §3.1, §5.1 (FLEX, STUDY, OFFICE no window); PF §8.1 | — | $ |
| ARC-16 | Consider | Orientation of living space | The great room (452 sf) has north glass only (21.6 + 25.8 sf) and a 26 ft west opening; the kitchen/dining has one south window run; so K-064 is MISSING for both. The SUN ROOM faces north and east (K-014: sunroom was meant to be south-east). Kitchen counter runs are on exterior walls (K-096). The front porch is 15.26 ft (4.65 m) deep in front of den and breakfast windows (K-095 MISSING). | PF §5.1, §2.2, §3.1 | — | $ |
| ARC-17 | Consider | Bathtubs on exterior walls | K-074 CONTRADICTED: master tub (x 123.16-127.63, y 9.55-15.03) is on the east wall (gap 0.24 ft) and the south wall; BATH 2 tub (x 7.7-10.33) is on the west wall (gap 0.43 ft). Master tub is 4.47 x 5.48 ft, 2 ft raised, not sunken (K-220). | PF §9.1; `main_floor.scad:219, :227` | — | $ |
| ARC-18 | Consider | Master wing adjacency | Both master WC rooms (6.81 x 3.85 and 6.81 x 3.78 ft c/l) share wall x=99.7 with the den alcove (y 9.31-20.56): K-008 noise/privacy. M49, the closet-passage opening, is 27.6 in, narrower than K-061. M47 and M48 let the 5.5 ft master entry vestibule open the whole bedroom to the hall (ARC-13). | PF §3.1, §4.4 | — | $ |
| ARC-19 | Consider | Windowless rooms | 27 heated rows have no window row, including STUDY (97 sf), FLEX (151), OFFICE (165) and FOYER (309) (K-007 MISSING; K-031 STUDY quiet but windowless). Kayla's office wishes (K-031, K-180 to K-183) need daylight: STUDY has only a 3.75 ft double door M5 to its stoop. | PF §5.1 | — | $ |
| ARC-20 | Consider | Windows: centring, corners, across | K-078 and K-080 MISSING: DEN south window (x 84-92) and SUN ROOM north window (x 44.3-51.7) are centred on their walls; only 4 rooms have windows on 2 walls. BEDROOM 2's two west windows cover 11.4 of 12.67 ft (K-307). No room has windows on opposite walls (K-077 IN). | PF §5.1 | — | $ |
| ARC-21 | Consider | Accessibility planning | K-058 (elevator space) and K-059 (dumbwaiter) MISSING; the stair is a fixed 4.62 x 11.64 ft with 22 risers (PF §10.1). The basement holds the pool, gym and theatre (K-002 IN), reachable only by that stair or the 19-riser exit stair (PF §10.2). Hall clear widths: BEDROOM hall 3.7 ft (45 in), master entry 3.0 ft (36 in), suite entry 2nd piece a 1.1 ft sliver that is passed through only by the 3.5 ft opening M19. | PF §6.1; PF §10.1, §10.2 | ABC 2023 9.5.4.1.(1): 860 mm hallway minimum; all main halls pass (clear 36 in or more) | $$ to $$$ (shaft) |
| ARC-22 | Consider | Outdoor links to the kitchen | K-023, K-127 MISSING: no door from the kitchen/dining to a covered outdoor area. The breakfast door M4 (5 ft) opens to the front porch; the deck (K-252, K-253 IN) is about 60 ft by path through the hall and great room. K-129 and K-134 (fully openable doors) MISSING: largest doors are 6 to 6.5 ft doubles. | PF §4.1; PF §7.1 | — | $ to $$ |
| ARC-23 | Consider | Pet and utility zones | K-170, K-172 MISSING: dog wash is in the basement PET ROOM (x 65.5-69, y 26.5-28.9), no litter area, no pet door to the garage; basement PET ROOM has no door to outside (PF §7.2). | `basement.scad:134`; PF §7.2 | — | $ |
| ARC-24 | Consider | Dining and sun room furniture | Dining seats 8 at the 3.62 x 9.21 ft table (K-128 IN; 6.2 ft to the foyer wall, 10.2 ft to the island). The SUN ROOM table is 2.6 x 3.6 ft and leaves 2.3 ft to the west sofa, so K-189 (dining for 4) MISSING. | `main_floor.scad:254-258` | — | $ |
| ARC-25 | Consider | Dead and sliver spaces | "(suite entry, 2nd piece)" 3.72 x 1.55 ft (6 sf), basement HALLWAY row 18.87 x 1.125 ft, and the stair-landing hall 4.62 x 3.59 ft (17 sf) hold no furniture. (Closet passage) is 44 sf and (master entry) 20 sf, 3.0 ft clear. Together 87 sf are passage only. | PF §3.1, §3.2 | — | $ |
| ARC-26 | Consider | Furniture symbols | The drawn BEDROOM 2 bed is 4.41 x 4.61 ft and the master bed 5.92 x 6.58 ft: both smaller than a queen or king of 60 or 76 in wide (assumed). Fit was checked with real sizes (table below), so no layout failure; the plan symbols should be replaced before the layouts are scored. | `main_floor.scad:246, :267` | — | $ |
| ARC-27 | Consider | Door swing check | The model's checker already passes door swings against fixtures and leaves (PF §0). Walked by hand, no door crosses a fixture; the swing hazards are traffic ones: M31 (32.4 in) swings into the 6.7 ft upper hall in front of the sun-room doors M36 (5.9 ft); M12 opens into the 5.5 ft hall beside the mud bench (x 24.8-35.3, y 30.49-31.81). | `tools/check_layout.py`; PF §4.1 | — | $ |
| ARC-28 | Consider | Room-size code check | The library has no minimum room-floor-area rule for houses; Section 9.5 gives areas over which a minimum ceiling height must exist (bedroom 4.9 m2 / 3.5 m2, kitchen 3.2 m2). Every main-floor bedroom is above that (BEDROOM 2 177 sf, BUNK 184 sf, master 412 sf clear). Minimum hall (860 mm) and door sizes are met; see ARC-05. No finding. | PF §3.1; the cited page | ABC 2023 Table 9.5.3.1 and 9.5.4.1.(1) (see citation log) | — |

## Kayla cross-check (all 335 items)

Class is the fixed scoring list for the three layout options: PLAN = a floor or site plan can show or prevent it; SPEC = fit-out, equipment or construction detail; INFO = note or empty heading.

**Counts.** PLAN 164 / SPEC 134 / INFO 37 (total 335). PLAN verdicts: IN 62 / MISSING 89 / CONTRADICTED 13 (total 164). Verdicts are conservative: partial presence is MISSING.

**Deal-breakers (verdicts on the model on `main`)**

| Deal-breaker | K-IDs | Verdict | Model evidence |
|---|---|---|---|
| Bedroom directly adjacent to foyer | K-328 | IN | Foyer (x 69.14-81.12) touches kitchen, den, spine only; nearest bedroom is the master, 27 ft east (PF §8.2) |
| Laundry far from bedrooms | K-329 | MISSING | 20.3 to 22.7 ft from BUNK/BEDROOM 2, 103.1 ft from master (PF §7.3) |
| Major path only through kitchen zone | K-330 | IN | Master-to-laundry path runs spine then mudroom (PF §7.3); a 10 ft lane bypasses the island |
| Closets on exterior walls | K-331 / K-070 | CONTRADICTED | BR2 WIC 3.0 ft exterior west, LINEN 1.2 N + 9.0 E (PF §8.3); master WICs interior |
| Full open concept | K-332 | IN | Kitchen/dining and great room split by the hall with 4, 5.9 and 26 ft openings (PF §4.1) |
| Through master bath to reach closet | K-333 / K-201 + K-304 | IN | Closet passage opens to the bedroom (M49, 27.6 in) and to the bath (M52): not only through the bath. M49 is narrow (PF §4.4) |
| Bedrooms sharing wall with living room | K-334 | IN | No bedroom wall touches a living-type room (PF §8.1) |
| Garage at rear, drive past bedrooms | K-335 / K-005 | CONTRADICTED | Drive x -32..-2 is 9.3 ft from BEDROOM 2 (PF §8.5); garage doors face it (main_floor.scad:117-118) |
| Laundry tied to master suite | K-036 + K-329 | MISSING | No master W/D; 103.1 ft path (PF §7.3) |
| Costco door pantry to garage | K-037 + K-115 | MISSING | Scullery shares 8.7 ft with garage, 0 doors (PF §8.3) |
| Wide doors and halls | K-003 + K-060 + K-061 | MISSING | 8 of 37 passage openings under 32 in (28.2-31.2 in at M20, M21, M23, M28, M54-M56; M49 27.6 in); bedroom/bath doors 28.2-36 in (PF §4.4); halls clear 3.7 ft (HALL @22.1), 3.0 (master entry), 4.9-5.5 (rest) (PF §6.1) |
| No-threshold shower | K-055 | MISSING | Shower pans drawn 0.15 ft raised (main_floor.scad:224, 226); no curbless detail |

### Full table (K-001 to K-335)

| K-ID | Class | Verdict | Evidence |
|---|---|---|---|
| K-001 | PLAN | IN | All essential rooms (kitchen, laundry, master suite, 2 bedrooms, hall BATH) are on the main level (PF §3.1); basement holds gym/theatre/pool/music only (PF §3.2). |
| K-002 | PLAN | IN | Basement 3,475 sf (PF §1.1) with gym, theatre, music room, pool (PF §3.2). |
| K-003 | PLAN | MISSING | 8 of 37 passage openings are under 32 in (PF §4.3): M20 31.2, M21 28.2, M23 28.8, M28 28.8 (hall to stair landing), M49 27.6 (master closet passage), M54 31.2, M55 28.8, M56 31.2 (PF §4.1); 11 more at 32-35 in. Widths of 5-8 ft only at openings M14, M18, M26, M27, M32, M42, M43. See ARC-05. |
| K-004 | PLAN | MISSING | Master bath 230 sf clear is generous (PF §3.1) but WC rooms are 3.4 ft clear wide (PF §3.1 rows :57, :90, :92), hall BATH 60 sf, BATH 2 62 sf; no clear turning space is shown anywhere. |
| K-005 | PLAN | CONTRADICTED | West drive x -32..-2 ends y=42 (site.scad:111), 9.3 ft from BEDROOM 2, 11.1 ft from its WIC, 16.2 ft from BATH 2 (PF §8.5); BEDROOM 2 has two west windows (PF §5.1). Garage doors face the drive (main_floor.scad:117-118). Road side is an assumption (site.scad:8). |
| K-006 | PLAN | MISSING | 14 wet-wall groups on the main floor in 5 clusters (PF §9.3); kitchen sink (G1), island prep sink (G4) and scullery sink (G7) are three separate groups; drain-run index 879 ft (PF §9.5). |
| K-007 | PLAN | MISSING | Windowless: STUDY 97, FLEX ROOM 151, OFFICE 165, laundry, mudroom, scullery, FOYER 309 (PF §5.1 list of 27 rooms with no window row). |
| K-008 | PLAN | MISSING | BEDROOM 2 east wall (12.7 ft) is shared with LAUNDRY (7.6 ft) and MUDROOM (5.1 ft), south wall (14.8 ft) with the garage (PF §2.2, §3.1). Master WC rooms share wall x=99.7 with the den alcove (PF §3.1). |
| K-009 | PLAN | MISSING | The bedroom hall (x 22.1-42.65, y 49.64-53.75) also serves STUDY, laundry and the stair landing, and the hall BATH/sun room/flex are reached past it (PF §7.1); alternate route exists via GREAT ROOM then HALL @53.95 (PF §7.1). |
| K-010 | PLAN | MISSING | Room sizes are off a 2 ft module: 14.83 x 12.67, 11.26 x 8.69, 15.19 x 9.93 (PF §3.1). |
| K-011 | INFO | — | Statement of principle. |
| K-012 | PLAN | MISSING | Kitchen, breakfast, den, foyer face south (PF §2.2) but the main living room (GREAT ROOM) and the deck face north (PF §2.2); garage drive is on the west side, with a south loop only for the front (PF §2.1). |
| K-013 | PLAN | IN | Master bedroom is in the north-east block (y 29.5-52.9) with north and east exterior walls (PF §2.2); bath and WICs sit south of it (PF §3.1). |
| K-014 | PLAN | MISSING | Master has east windows 43.5 sf (PF §5.1). BEDROOM 2 windows are west, BUNK ROOM north (PF §5.1); the SUN ROOM faces north and east, not south-east (PF §2.2). |
| K-015 | INFO | — | Empty direction heading. |
| K-016 | SPEC | — | Wall blocking: framing detail. |
| K-017 | SPEC | — | Recess behind fridge needs a 2x6 wall: construction detail (model draws every wall 0.4 ft, PF §0). |
| K-018 | SPEC | — | Laundry exhaust fan: equipment. (Laundry has no window row, PF §5.1.) |
| K-019 | SPEC | — | In-wall acoustic insulation: construction. |
| K-020 | SPEC | — | Dutch doors: door spec. |
| K-021 | PLAN | IN | BREAKFAST bay 94 sf opens 14.5 ft to the kitchen (M41, PF §4.1) with banquette and round table (main_floor.scad furniture :54.41-60.33). |
| K-022 | SPEC | — | TV in kitchen: equipment. |
| K-023 | PLAN | MISSING | No door from KITCHEN / DINING to a covered outdoor area; the nearest covered outdoor is the front porch via BREAKFAST door M4 (5 ft), the back deck is ~60 ft away via the hall and great room (PF §7.1). |
| K-024 | SPEC | — | Appliance placement; the SCULLERY (98 sf) exists (PF §3.1). |
| K-025 | SPEC | — | Shelving/storage fit-out. |
| K-026 | SPEC | — | Baking zone fit-out. |
| K-027 | SPEC | — | Shelf depth. |
| K-028 | SPEC | — | Freezer: appliance. |
| K-029 | SPEC | — | Microwave: appliance. |
| K-030 | PLAN | MISSING | No pantry room; SCULLERY 90 sf clear carries a sink and two counters only (main_floor.scad:207-209) and tall pantry cabinets in the kitchen are 6.9 x 1.9 ft (main_floor.scad:202). Bulk storage room not shown. |
| K-031 | PLAN | IN | STUDY 97 sf at the end of the bedroom hall, shares walls with bunk room, sun room, hall only (PF §3.1, §7.1); it has no window row (see K-007). |
| K-032 | PLAN | MISSING | No library room on the main floor (PF §8.1 note: living-type rooms are GREAT ROOM, DEN, SUN ROOM). Basement LIVING ROOM 412 sf exists (PF §3.2). |
| K-033 | PLAN | MISSING | No powder room (PF §15.14). Hall BATH is 65.8 ft from the foyer (PF §7.3). See ARC-09. |
| K-034 | PLAN | IN | SUN ROOM 144 sf, enclosed, N window 48.1 sf, E window 23.4 sf, double door M37 to PATIO (PF §5.1, §4.1). |
| K-035 | PLAN | IN | Kitchen and dining are one room (779 sf), dining table at x 59.3-63, y 12.7-21.9 with no hall or pantry between (PF §3.1; main_floor.scad furniture). |
| K-036 | PLAN | MISSING | LAUNDRY is 103.1 ft from the master bedroom by door path (PF §7.3); no W/D in the master suite (LINEN is the only room at the master bath end, PF §3.1). Oct round-2 master laundry did not carry over. See ARC-02. |
| K-037 | PLAN | MISSING | SCULLERY shares 8.7 ft of wall with the garage but 0 doors between (PF §8.3); garage door M12 opens to the hall. See ARC-03. |
| K-038 | PLAN | MISSING | No broom/vacuum closet in the room table (PF §3.1 closet rows: 3 WICs, LINEN, linen between WCs). |
| K-039 | SPEC | — | Robot dock: niche detail. |
| K-040 | PLAN | MISSING | Both linen rooms (LINEN 55 sf, linen between WCs 25 sf) are in the master bath; none near BEDROOM 2, BUNK ROOM or the hall BATH (PF §3.1). |
| K-041 | PLAN | MISSING | No vestibule: front door M1 opens straight into the 12 x 25.8 ft FOYER (PF §3.1, §4.1); opening M42 to the hall has no door. |
| K-042 | INFO | — | Heading. |
| K-043 | PLAN | MISSING | Foyer fixtures are a bench and 'wine racks' only (main_floor.scad:238-239 rows at x 69.67-71.38); no mail/command centre drawn. |
| K-044 | PLAN | MISSING | No key/purse landing drawn at the front entrance (same foyer rows). |
| K-045 | SPEC | — | Blanket/pillow storage: furniture. |
| K-046 | SPEC | — | Pet food storage: fit-out. |
| K-047 | PLAN | IN | Foyer bench 1.7 x 6.6 ft (69.67-71.38 x 12.07-18.65) and mud lockers/bench (main_floor.scad:215-217). |
| K-048 | SPEC | — | Games/coolers storage: fit-out (basement STORAGE 115 sf, PF §3.2). |
| K-049 | SPEC | — | Cleaning supplies in each room: fit-out. |
| K-050 | SPEC | — | Dead-void storage: construction detail. |
| K-051 | INFO | — | Heading. |
| K-052 | SPEC | — | Hamper placement: fit-out. |
| K-053 | PLAN | IN | Master bed drawn floating with 4.8 ft east and 7.6 ft south of it to walls (main_floor.scad:267, x 116.25-122.17, y 37.07-43.65). Bed symbol 5.92 ft wide, narrower than a king (assumed 76 in). |
| K-054 | INFO | — | Heading. |
| K-055 | PLAN | MISSING | Showers are drawn as 0.15 ft (1.8 in) raised tile boxes (main_floor.scad:224, 226); no depressed floor or curbless detail. Master shower 8.23 x 4.5 ft. See ARC-06. |
| K-056 | SPEC | — | Bench/foot notch: fit-out. |
| K-057 | SPEC | — | Tub step-in: fixture spec. |
| K-058 | PLAN | MISSING | No stacked closet/shaft footprint reserved; stair is fixed 4.62 x 11.64 ft (PF §10.1). |
| K-059 | PLAN | MISSING | No dumbwaiter shaft; basement LAUNDRY (x 67.4-81.7, y 5.8-13.4) is not under any main-floor laundry (PF §3.1, §3.2). |
| K-060 | PLAN | MISSING | Clear hall widths: HALL @22.1 3.7 ft (45 in), master entry 3.0 ft (36 in), suite entry 5.2 ft, spine 5.5 ft (67 in), N-S hall 5.0 ft (PF §6.1). No 60 in turning space is shown in the bedroom wing. |
| K-061 | PLAN | MISSING | Same as K-003: 8 openings under 32 in; bedroom/bath doors 28.2-36 in (PF §4.4). |
| K-062 | PLAN | IN | Zones are separated by 15 full openings (4-26 ft) and 12 double doors rather than a single space (PF §4.3); great room and kitchen are split by the 5.95 ft hall. |
| K-063 | SPEC | — | Partition types: detail. |
| K-064 | PLAN | MISSING | Windows on 2 walls only in SUN ROOM, MASTER BEDROOM, DEN, BREAKFAST (PF §5.1); GREAT ROOM has north windows only, KITCHEN / DINING south only. |
| K-065 | SPEC | — | Skylights/mirrors: spec. |
| K-066 | SPEC | — | Glare depends on TV position not drawn. |
| K-067 | SPEC | — | Same. |
| K-068 | SPEC | — | Soft surfaces: finishes. |
| K-069 | PLAN | MISSING | 17 outside and 13 inside corners, 395.5 ft heated perimeter (PF §1.2). |
| K-070 | PLAN | CONTRADICTED | WIC @7.27,48.13 has 3.0 ft of exterior west wall; LINEN has 1.2 ft north and 9.0 ft east exterior (PF §2.2, §8.3); only the 2 master WICs are fully interior. See ARC-04. |
| K-071 | PLAN | MISSING | 2 of 3 WICs fully interior (PF §8.3); BUNK ROOM and STUDY have no closet row. |
| K-072 | PLAN | IN | Hall BATH: shower y 35.9-38.4, toilet y 39.7-41.35, door y 45.39 (main_floor.scad:222-224, M34); master WCs are separate rooms. |
| K-073 | SPEC | — | Separate fan per WC: equipment. |
| K-074 | PLAN | CONTRADICTED | Master tub x 123.16-127.63 sits on the east wall (gap 0.24 ft) and Bath 2 tub x 7.7-10.33 on the west wall x=7.27 (gap 0.43 ft) (PF §9.1, §2.2). |
| K-075 | PLAN | CONTRADICTED | Bedroom wing (x 7.3-42.7) and master wing (x 95-128) are separated by foyer, kitchen, great room and den over 80 ft of hall (PF §3.1, §6.1). |
| K-076 | SPEC | — | Focal points: finish/furniture (great room fireplace box exists, main_floor.scad:241). |
| K-077 | PLAN | IN | No room has windows on opposite walls: pairs are E/N, S/W, E/S (PF §5.1). |
| K-078 | PLAN | MISSING | 4 of the 9 windowed rooms have corner-adjacent windows (PF §5.1); GREAT ROOM and KITCHEN have one wall of glass. |
| K-079 | SPEC | — | Window heights: spec. |
| K-080 | PLAN | MISSING | Centred windows: DEN south (x 84-92 in room 81.1-96), SUN ROOM north (44.3-51.7 in room 42.65-53.95) (PF §5.1, §3.1). |
| K-081 | PLAN | MISSING | BEDROOM 2 has 54 sf of west glass with no porch or overhang on that side (PF §5.1, §2.2: W 9.6 ft yard/soil). |
| K-082 | INFO | — | Principle. |
| K-083 | PLAN | MISSING | Long:short ratios 1.4-1.6 only for GREAT ROOM 1.55, KITCHEN 1.44, FLEX 1.53, hall BATH 1.49; MASTER 1.27, BEDROOM 2 1.17, BUNK 1.17, SUN 1.13, STUDY 1.04, OFFICE 1.02 (PF §3.1). |
| K-084 | INFO | — | Principle. |
| K-085 | INFO | — | Principle. |
| K-086 | INFO | — | Principle. |
| K-087 | INFO | — | Ranch-type note. |
| K-088 | INFO | — | Ranch-type note. |
| K-089 | INFO | — | Ranch-type note. |
| K-090 | INFO | — | Ranch-type note. |
| K-091 | INFO | — | Sun-path note. |
| K-092 | INFO | — | Sun-path note. |
| K-093 | INFO | — | Fact: covered-patio light fall-off (FRONT PORCH is 15.26 ft = 4.65 m deep, PF §3.1). |
| K-094 | SPEC | — | Pergola/retractable cover: spec. |
| K-095 | PLAN | MISSING | FRONT PORCH 15.26 ft (4.65 m) deep in front of den and breakfast windows; PATIO 12.73 ft deep east of the sun room (PF §3.1). |
| K-096 | PLAN | CONTRADICTED | Kitchen range run is on the west wall (faces SIDE ENTRY porch/yard, PF §2.2) and the sink run on the south wall (exterior); only the tall pantry sits on the interior north wall (main_floor.scad:197-202). |
| K-097 | INFO | — | Observation. |
| K-098 | INFO | — | Observation. |
| K-099 | PLAN | MISSING | Kitchen, den, breakfast are south (IN) but the main living room GREAT ROOM faces north only (PF §2.2). |
| K-100 | PLAN | MISSING | Master east windows only; BEDROOM 2 west, BUNK ROOM north (PF §5.1). |
| K-101 | INFO | — | Heading. |
| K-102 | PLAN | MISSING | Hall BATH toilet (x 51.12-53.09, y 39.7-41.35) is 4.0 ft inside the door line (door y 45.39); master WCs are enclosed in their own rooms (PF §9.1, §3.1). |
| K-103 | PLAN | MISSING | From BEDROOM 2 bed (x 14.8-19.2) a straight line north runs through the 7.9 ft opening M18 and the 3.5 ft opening M19 to BATH 2 door M20 (x 14.3-16.9, y 55.3); entry/couch/dining see no bath door (PF §4.1). |
| K-104 | PLAN | CONTRADICTED | Looking east along the 80.5 ft spine, double door M47 (55 in) and 64.8 in opening M48 put the master bedroom directly in line (PF §4.1, §3.1). |
| K-105 | PLAN | MISSING | MUDROOM is open 12.4 ft to the hall (M14) and laundry door M15 is in its north wall (PF §4.1). |
| K-106 | PLAN | IN | Island 6.9 x 9.87 ft (x 42.24-49.14, y 12.4-22.27), no stools drawn (main_floor.scad:203). |
| K-107 | PLAN | IN | BREAKFAST banquette on two walls plus round table 5.1 ft (main_floor.scad furniture). |
| K-108 | PLAN | CONTRADICTED | Prep sink at island x 43.22-44.87, y 16.68-18.65 (main_floor.scad:204). |
| K-109 | SPEC | — | Cabinet spec. |
| K-110 | SPEC | — | Cabinet spec. |
| K-111 | SPEC | — | Appliance size; fridge box 2.49 x 3.22 ft (main_floor.scad:201). |
| K-112 | SPEC | — | Appliance spec. |
| K-113 | SPEC | — | Appliance spec; no dishwasher drawn (PF §8.4). |
| K-114 | PLAN | IN | SCULLERY 98 sf with sink and two counter runs, entered from kitchen M13 (PF §3.1, §4.1). |
| K-115 | PLAN | MISSING | Same as K-037: shared wall 8.7 ft, 0 doors (PF §8.3). |
| K-116 | PLAN | MISSING | Garage door M12 to kitchen fridge/pantry is 41.3 ft; to kitchen centre 52.5 ft (PF §7.3). |
| K-117 | PLAN | MISSING | No coffee bar near BREAKFAST; nearest counter is the south run (y 6.48-8.45) and buffet at y 27.2-29.1 (main_floor.scad:197-205). |
| K-118 | SPEC | — | Fixture. |
| K-119 | SPEC | — | Fixture. |
| K-120 | SPEC | — | Fixture. |
| K-121 | SPEC | — | Freezer: appliance. |
| K-122 | SPEC | — | Microwave location: fit-out. |
| K-123 | PLAN | MISSING | Island faces the dining table and breakfast, not a living area; great room is across the hall via a 5.9 ft opening (PF §4.1 M40). |
| K-124 | PLAN | IN | Sink x 39.93-42.57 on south wall under window x 37.7-45.2 (main_floor.scad:200, :191). |
| K-125 | SPEC | — | Island extension: spec. |
| K-126 | SPEC | — | Sink type: spec. |
| K-127 | PLAN | MISSING | No outdoor door from KITCHEN / DINING; BREAKFAST M4 opens to the front porch (PF §4.1). |
| K-128 | PLAN | IN | Dining table 3.62 x 9.21 ft with 6.2 ft to the foyer wall and 10.2 ft to the island (main_floor.scad furniture :59.34-62.96 x 12.73-21.94). |
| K-129 | PLAN | MISSING | Dining/breakfast exterior door M4 is a 5 ft double (PF §4.1); no wide folding or sliding wall. |
| K-130 | SPEC | — | Fireplace box drawn (main_floor.scad:241); fuel undecided (PF §11). |
| K-131 | SPEC | — | TV position not drawn. |
| K-132 | PLAN | IN | GREAT ROOM 435 sf clear holds three sofa boxes and a table in the drawn furniture (main_floor.scad furniture :70.53-79.74). |
| K-133 | PLAN | IN | GREAT ROOM double door M33 (72 in) to DECK; SUN ROOM beside it (PF §4.1). |
| K-134 | PLAN | MISSING | M33 is a 6 ft double door, M6 6.5 ft, M7 6.05 ft; no multi-panel wall (PF §4.1). |
| K-135 | SPEC | — | Furniture arrangement. |
| K-136 | SPEC | — | Built-ins: fit-out. |
| K-137 | SPEC | — | Storage fit-out. |
| K-138 | SPEC | — | Pet furniture. |
| K-139 | SPEC | — | Ceiling fan. |
| K-140 | PLAN | IN | Foyer bench (main_floor.scad:239). |
| K-141 | PLAN | MISSING | Foyer storage is 'wine racks' 7 ft high at x 69.67-71.38, y 18.65-29.11, not coat storage (main_floor.scad:238). |
| K-142 | PLAN | MISSING | No closed coat/shoe storage in the foyer (same rows). |
| K-143 | PLAN | MISSING | No foyer drop surface or shelf. |
| K-144 | PLAN | CONTRADICTED | Front door (x 72-78.2), M42 (71.4-79.3), M43 (69.4-95.4) and deck doors M33 (70.65-76.65) line up: great room is seen from the door; kitchen is not (foyer/kitchen wall has no opening, PF §8.2). |
| K-145 | PLAN | MISSING | No powder room (PF §15.14). |
| K-146 | PLAN | IN | Mud bench + cabinets 8.55 x 3.0 ft (x 28.09-36.64, y 36.94-39.97) and hall bench (main_floor.scad:216-217). |
| K-147 | PLAN | IN | Lockers and cabinets drawn (main_floor.scad:215-216). |
| K-148 | SPEC | — | Hooks: fit-out. |
| K-149 | PLAN | IN | Lockers x 22.63-24.14, y 35.66-39.97, 7 ft high (main_floor.scad:215). |
| K-150 | SPEC | — | Seasonal storage: fit-out. |
| K-151 | PLAN | IN | Mud bench/cabinet top 3 ft high near garage door (main_floor.scad:216). |
| K-152 | SPEC | — | Hooks. |
| K-153 | PLAN | MISSING | No mail/command area drawn. |
| K-154 | SPEC | — | Chutes: construction. |
| K-155 | PLAN | MISSING | MUDROOM has no exterior door; its only openings are M14 and M15 (PF §4.1, §7.1). |
| K-156 | PLAN | IN | Garage door M12 into the hall, mudroom open to the hall (PF §4.1). |
| K-157 | PLAN | MISSING | No bath off the mudroom (PF §15.14). |
| K-158 | PLAN | MISSING | See K-036. |
| K-159 | SPEC | — | Appliance height. |
| K-160 | SPEC | — | Fit-out. |
| K-161 | SPEC | — | Fit-out. |
| K-162 | SPEC | — | Fit-out. |
| K-163 | PLAN | IN | Laundry sink x 33.22-35.1, y 41.02-43.52 (main_floor.scad:212). |
| K-164 | SPEC | — | Storage fit-out. |
| K-165 | SPEC | — | Fit-out. |
| K-166 | PLAN | MISSING | Master to LAUNDRY 103.1 ft (PF §7.3); no pass-through. |
| K-167 | SPEC | — | Linen storage fit-out. |
| K-168 | SPEC | — | Fit-out. |
| K-169 | SPEC | — | Fit-out. |
| K-170 | PLAN | MISSING | Dog wash is in the basement PET ROOM (x 65.5-69, y 26.5-28.9, basement.scad:134), none near the garage entry. |
| K-171 | SPEC | — | Furniture. |
| K-172 | PLAN | MISSING | No litter area; PET ROOM has no door to the garage (PF §7.2). |
| K-173 | SPEC | — | Dog door: exterior wall detail. |
| K-174 | SPEC | — | Decor. |
| K-175 | SPEC | — | Bookshelves: fit-out (no library room, see K-032). |
| K-176 | SPEC | — | Furniture. |
| K-177 | SPEC | — | Fireplace: equipment. |
| K-178 | SPEC | — | Window seat: fit-out. |
| K-179 | PLAN | IN | Hall BATH off the upper hall (M34); master bath off master suite; BATH 2 off bedroom lobby (PF §7.1). |
| K-180 | SPEC | — | Desk size: furniture (OFFICE 165 sf, PF §3.1). |
| K-181 | SPEC | — | Fit-out. |
| K-182 | SPEC | — | Door spec (OFFICE M6 is a 6.5 ft double to porch, PF §4.1). |
| K-183 | PLAN | IN | OFFICE door M6 (78 in) to OFFICE PORCH 147 sf (PF §4.1). |
| K-184 | INFO | — | Question. |
| K-185 | PLAN | MISSING | SUN ROOM north wall 11.3 ft has a 7.4 ft window, east wall 12.7 ft has a 3.6 ft window plus 4.9 ft door (PF §5.1, §4.1). |
| K-186 | PLAN | IN | Double door M37 (58.8 in) SUN ROOM to PATIO (PF §4.1). |
| K-187 | SPEC | — | Screens: window spec. |
| K-188 | PLAN | IN | SUN ROOM 134 sf clear with two sofa boxes (main_floor.scad furniture :43.09-51.78). |
| K-189 | PLAN | MISSING | Drawn table is 2.6 x 3.6 ft and leaves 2.3 ft to the west sofa (main_floor.scad furniture :43.09-45.53 vs :47.83). |
| K-190 | SPEC | — | TV: equipment. |
| K-191 | PLAN | IN | Master double door M7 (72.6 in) to MASTER PORCH 175 sf (PF §4.1). |
| K-192 | PLAN | IN | The only fireplace box is in the great room (main_floor.scad:241). |
| K-193 | SPEC | — | Fan. |
| K-194 | SPEC | — | HVAC. |
| K-195 | PLAN | IN | Master bedroom 412 sf clear, bed 4.8 ft from east wall, 7.6 ft from south wall (PF §3.1). |
| K-196 | SPEC | — | Furniture. |
| K-197 | SPEC | — | Exterior wall detail. |
| K-198 | SPEC | — | Furniture. |
| K-199 | SPEC | — | Furniture. |
| K-200 | PLAN | IN | Two separate WICs 95 and 94 sf (PF §3.1). |
| K-201 | PLAN | IN | Closets open from the master bedroom through M49 (27.6 in, 'open') and from the bath through M52 (32.4 in) (PF §4.4). Opening M49 is narrow. |
| K-202 | PLAN | IN | Bath reaches closets via M52 (PF §4.4); bedroom access exists (K-201). |
| K-203 | PLAN | MISSING | WICs reach no laundry; LINEN (no W/D) off bath only (PF §7.1). |
| K-204 | SPEC | — | Fit-out. |
| K-205 | SPEC | — | Fit-out. |
| K-206 | SPEC | — | Fit-out. |
| K-207 | SPEC | — | Fit-out. |
| K-208 | SPEC | — | Fit-out. |
| K-209 | SPEC | — | Fit-out. |
| K-210 | PLAN | MISSING | No laundry in master suite (see K-036). |
| K-211 | PLAN | MISSING | Master shower 8.23 x 4.5 ft is large (main_floor.scad:226) but drawn 1.8 in above floor. |
| K-212 | SPEC | — | Bench: fit-out. |
| K-213 | SPEC | — | Niches. |
| K-214 | SPEC | — | Hooks. |
| K-215 | SPEC | — | Valve. |
| K-216 | SPEC | — | Hand shower. |
| K-217 | SPEC | — | Fan. |
| K-218 | SPEC | — | Notch. |
| K-219 | SPEC | — | Ledge. |
| K-220 | PLAN | MISSING | Tub 4.47 x 5.48 ft drawn as a 2 ft raised box, not sunken (main_floor.scad:227). |
| K-221 | SPEC | — | Tub steps: detail. |
| K-222 | SPEC | — | Shelf. |
| K-223 | SPEC | — | Ledge. |
| K-224 | PLAN | IN | Double vanity 9.87 x 1.78 ft (main_floor.scad:225). |
| K-225 | SPEC | — | Storage fit-out. |
| K-226 | PLAN | IN | LINEN 55 sf and linen between WCs 25 sf off the master bath (PF §3.1). |
| K-227 | PLAN | MISSING | Two WC rooms (IN) but 3.4 ft clear wide with 31.2 in doors (PF §3.1, §4.4). |
| K-228 | PLAN | MISSING | No laundry reachable from the bath (PF §7.1). |
| K-229 | PLAN | IN | Closet passage door M52 to the bath (PF §4.4). |
| K-230 | SPEC | — | Makeup vanity: fit-out. |
| K-231 | SPEC | — | Fit-out. |
| K-232 | SPEC | — | Furniture. |
| K-233 | SPEC | — | Storage fit-out. |
| K-234 | SPEC | — | Furniture. |
| K-235 | SPEC | — | Furniture. |
| K-236 | SPEC | — | Furniture. |
| K-237 | PLAN | MISSING | FLEX ROOM 14.8 x 9.5 ft clear has space for a bed but no window row (PF §3.1, §5.1) and a 6.5 ft slider to the hall. |
| K-238 | PLAN | IN | BEDROOM 2 14.4 x 12.3 ft clear; queen fits on the east wall (12.3 ft free) with 3.6 ft each side (computed). |
| K-239 | PLAN | IN | BATH 2 via lobby (M18, M19, M20), 19.4 ft path from bed (PF §7.3); also opens to BUNK ROOM (M23). |
| K-240 | PLAN | MISSING | BEDROOM 2 has no exterior door; it shares 14.8 ft with the garage but has no door (PF §2.2). |
| K-241 | INFO | — | Heading. |
| K-242 | PLAN | MISSING | Two non-master bedrooms (BEDROOM 2, BUNK ROOM); no fourth bedroom (PF §3.1). |
| K-243 | SPEC | — | Use note. |
| K-244 | PLAN | IN | BATH 2 reaches BEDROOM 2 (via lobby) and BUNK ROOM (M23) (PF §7.1). |
| K-245 | PLAN | MISSING | No small bedroom beside the master: OFFICE (165 sf) shares wall x=108.62 with the master bedroom but is an office (PF §3.1). |
| K-246 | SPEC | — | Furniture. |
| K-247 | SPEC | — | Furniture. |
| K-248 | PLAN | IN | FRONT PORCH 796 sf with posts and roof blocks (main_floor.scad:94, posts :main_posts). |
| K-249 | PLAN | MISSING | Mudroom has no outside door; garage side door M10 has a 17.5 sf uncovered pad (PF §3.1). |
| K-250 | SPEC | — | Outdoor kitchen: fit-out. |
| K-251 | SPEC | — | Equipment. |
| K-252 | PLAN | IN | DECK 322 sf (26.5 x 12.2 ft) under porch roof posts (main_floor.scad:98, posts). |
| K-253 | PLAN | IN | DECK and PATIO 193 sf adjoin (PF §3.1). |
| K-254 | PLAN | MISSING | 7 porch roof blocks over 13 porch rows (PF §1.2); no unroofed sun area identified. |
| K-255 | PLAN | IN | OFFICE PORCH 147 sf off the office (PF §3.1). |
| K-256 | PLAN | IN | Range run has 4.9 ft north and 8.2 ft south of the range; sink has 1.6 ft west and 11.8 ft east (main_floor.scad:197-198, :200). |
| K-257 | PLAN | MISSING | Scullery door M13 (y 23.3-26.3) sits between the range run end (y 22.6) and the fridge (y 25.89-29.11); no counter beside the fridge. |
| K-258 | INFO | — | Definition. |
| K-259 | INFO | — | Opinion. |
| K-260 | INFO | — | Opinion. |
| K-261 | PLAN | MISSING | Legs: fridge-sink 20.4, sink-range 9.7, range-fridge 11.3 ft = 41.4 ft total (centres, computed from PF §9.1). With island prep sink: 12.0 + 7.2 + 11.3 = 30.5 ft. |
| K-262 | PLAN | IN | Foyer shares 23.2 ft with kitchen with no opening (PF §8.2); kitchen is first seen from the hall. |
| K-263 | SPEC | — | Aesthetic. |
| K-264 | INFO | — | Concept. |
| K-265 | INFO | — | Definition. |
| K-266 | INFO | — | Definition. |
| K-267 | INFO | — | Definition. |
| K-268 | INFO | — | Definition. |
| K-269 | INFO | — | Definition. |
| K-270 | PLAN | MISSING | Fridge to sink 20.4 ft; at 2.5 ft per step that is about 8 steps (assumption). |
| K-271 | SPEC | — | Appliance depth. |
| K-272 | INFO | — | Heading. |
| K-273 | PLAN | MISSING | Fridge door side faces the 4 ft M39 entry (fridge x 35.8-38.29, M39 x 38.2-42.2) (PF §4.1, main_floor.scad:201). |
| K-274 | PLAN | MISSING | No dishwasher drawn (PF §8.4); aisle between range run and island is 3.95 ft (47 in), under 54 in. |
| K-275 | SPEC | — | Hardware. |
| K-276 | SPEC | — | Hardware. |
| K-277 | PLAN | IN | Sink under the south window (K-124). |
| K-278 | SPEC | — | Appliance height. |
| K-279 | PLAN | IN | Island north end is 4.9 ft from the tall pantry cabinets (y 22.27 vs 27.2) (main_floor.scad:202-203). |
| K-280 | INFO | — | Workflow note. |
| K-281 | PLAN | IN | Island 68 sf with no cooktop (main_floor.scad:203). |
| K-282 | PLAN | MISSING | Island centre is 8.8 ft from the range but 13.4 ft from the fridge (computed). |
| K-283 | PLAN | IN | Counter beside the range: 4.9 ft north, 8.2 ft south (main_floor.scad:197-198). |
| K-284 | SPEC | — | Hood size. |
| K-285 | INFO | — | Workflow note. |
| K-286 | INFO | — | Workflow note. |
| K-287 | SPEC | — | Trash location: fit-out. |
| K-288 | PLAN | MISSING | No dishwasher in main_fixtures (PF §8.4). |
| K-289 | SPEC | — | Storage fit-out. |
| K-290 | PLAN | MISSING | Fridge is nearer the range (11.3 ft) than the sink (20.4 ft); it is at a run end, 4.3 ft from the pantry, away from the cooking wall (main_floor.scad:197-202). |
| K-291 | SPEC | — | Slab sizing (island 6.9 x 9.87 ft). |
| K-292 | PLAN | CONTRADICTED | Tall pantry cabinets form a separate unit on the north wall (x 42.24-49.14), interrupted by openings M39 and M40 (main_floor.scad:202, PF §4.1). |
| K-293 | SPEC | — | Cabinet dimensions. |
| K-294 | SPEC | — | Cabinet dimensions. |
| K-295 | SPEC | — | Cabinet dimensions. |
| K-296 | SPEC | — | Cabinet dimensions. |
| K-297 | PLAN | MISSING | FOYER has no window row (PF §5.1); only 2 glass sidelights of 24 in (M2, M3). |
| K-298 | PLAN | MISSING | No powder room (PF §15.14). |
| K-299 | PLAN | IN | Front door, M42, M43 and deck doors M33 overlap on x 72-76.65, so the view runs to the deck (PF §4.1). |
| K-300 | PLAN | IN | Same line ends at the deck doors M33 (double, 72 in). |
| K-301 | SPEC | — | Package door: detail. |
| K-302 | PLAN | MISSING | OFFICE has no bathroom adjacent (PF §7.1, §8). |
| K-303 | SPEC | — | Screens. |
| K-304 | PLAN | IN | Same as K-201; closets are reached from the bedroom (M49). |
| K-305 | SPEC | — | Furniture strategy. |
| K-306 | PLAN | CONTRADICTED | BUNK ROOM bed box x 23.16-29.74, y 63.91-66.15, 5 ft high overlaps north window x 21.45-24.95 (main_floor.scad:175; furniture). |
| K-307 | PLAN | MISSING | BEDROOM 2 west windows 5.4 ft x 2 cover 11.4 of 12.67 ft of wall (PF §5.1); master east windows are at the corners (IN). |
| K-308 | SPEC | — | Lighting. |
| K-309 | SPEC | — | Garage fans. |
| K-310 | SPEC | — | Garage fit-out. |
| K-311 | SPEC | — | EV charger. |
| K-312 | SPEC | — | Door opener. |
| K-313 | SPEC | — | Door spec. |
| K-314 | SPEC | — | Finish. |
| K-315 | PLAN | MISSING | Same as K-037. |
| K-316 | PLAN | CONTRADICTED | Halls total 891 sf = 16.2% of 5,486 sf; with foyer, mudroom and stair 24.3% (PF §6.1). One 80.5 x 5.5 ft hall is 481 sf (54% of the total). |
| K-317 | PLAN | MISSING | Room access unchanged: every room opens to the spine or a wing hall (PF §7.1). |
| K-318 | PLAN | IN | Bypass lane x 49.14-59.3 (10 ft) east of the island from M40 to BREAKFAST (computed); master/laundry/stair paths do not enter the kitchen (PF §7.3). |
| K-319 | INFO | — | Heading. |
| K-320 | PLAN | MISSING | Mail and groceries landing missing (K-043, K-116). |
| K-321 | INFO | — | Heading. |
| K-322 | INFO | — | Heading. |
| K-323 | PLAN | MISSING | GREAT ROOM west wall is a 26 ft opening, north wall has 21.9 ft of openings in 26.5 ft (PF §4.1, §5.1). |
| K-324 | PLAN | IN | Zones are separated (see K-062). |
| K-325 | PLAN | MISSING | BEDROOM 2 shares 12.7 ft with laundry/mudroom and 14.8 ft with the garage (PF §2.2). |
| K-326 | PLAN | MISSING | BEDROOM 2 east and south walls are utility and garage (not buffers); master has closets south and office west. |
| K-327 | SPEC | — | Insulation: construction. |
| K-328 | PLAN | IN | No bedroom touches the foyer; nearest is the master 27 ft away (PF §8.2). |
| K-329 | PLAN | MISSING | LAUNDRY is 20-23 ft from BEDROOM 2 and BUNK ROOM but 103.1 ft from the master (PF §7.3). |
| K-330 | PLAN | IN | Master-to-laundry route uses the spine and mudroom, not the kitchen (PF §7.3). |
| K-331 | PLAN | CONTRADICTED | See K-070. |
| K-332 | PLAN | IN | Kitchen/dining and great room are separated by the hall with three openings (4, 5.9, 26 ft) (PF §4.1). |
| K-333 | PLAN | IN | Master closets open from the bedroom (M49) as well as the bath. |
| K-334 | PLAN | IN | No bedroom wall is shared with a living-type room (PF §8.1, §7.1). |
| K-335 | PLAN | CONTRADICTED | Garage doors face the west drive 9.3 ft from BEDROOM 2 (see K-005). |

## Daily paths traced (PF §7.3, door-to-door distances)

| Path | Distance | Observation |
|---|---|---|
| Front door to kitchen/dining centre | 60.9 ft | foyer, spine, kitchen; the entry sees the great room, not the kitchen |
| Garage to kitchen centre / pantry cabinets / scullery | 52.5 / 41.3 / 47.9 ft | all via M12 to the spine then M39 (ARC-03) |
| Garage to top of stair | 31.6 ft | via M12, N-S hall, M28 (28.8 in door, ARC-05) |
| BEDROOM 2 to BATH 2 / hall BATH | 19.4 / 47.2 ft | ensuite via lobby; hall BATH passes the stair landing |
| BUNK ROOM to BATH 2 | 13.3 ft | direct, door M23 28.8 in |
| BEDROOM 2 / BUNK to LAUNDRY | 22.7 / 20.3 ft | through the hall |
| Master bedroom to LAUNDRY | 103.1 ft | ARC-02 |
| BEDROOM 2 to MASTER BATH | 127.8 ft | the two bedroom groups are in different wings |
| Master bedroom to its WICs | 25.0 / 23.9 ft | via the closet passage, not through the bath |
| Foyer to hall BATH (no powder room) | 65.8 ft | ARC-09 |
| Basement stair foot to UTILITY | 25.6 ft | not an architecture finding |

## Carried over from the Oct 28 kitchen/laundry/closet notes (item 2 of my adjustments)

| October note (applied to the Oct model) | Present on `main`? | Evidence |
|---|---|---|
| Two paths of travel through the kitchen work zone | Partly | Two entries from the hall (M39 into the 3.95 ft aisle, M40 into a 10 ft lane); fridge no longer on a separate end but at the end of the range wall (PF §4.1; `main_floor.scad:201`). ARC-11 |
| Laundry reachable from both sides | Yes (as a pass-through) | LAUNDRY has two doors: M15 from MUDROOM (33.6 in) and M16 to the bedroom hall (32.4 in) (PF §4.1). The N-S hall (M26, M27) gives an alternative path |
| Bedroom to closet directly | Partly | BEDROOM 2 to WIC: 70.8 in open (M22); master bedroom to WICs: 27.6 in open M49 to the passage; BUNK ROOM has no closet; the old "Bedroom 3/4" closets are not in the model (PF §4.4) |
| Master laundry (round 2) | No | No W/D in master suite (ARC-02) |
| Central hall to bedrooms, not through laundry (round 2) | Yes | N-S hall x 37.3-42.65 plus the E-W hall (PF §7.1) |
| Direct kitchen-to-dining, no pantry walk-through (round 2) | Yes | KITCHEN / DINING is one room (PF §3.1) |

## Furniture fit

| Item | Test | Result |
|---|---|---|
| Primary bed, king (76 x 80 in = 6.33 x 6.67 ft, assumption), headboard on the east wall | East wall is solid from y 35 to y 46 (11.0 ft) between the two windows (y 31-35 and 46-50.7); king + two 1.5 ft tables = 9.3 ft | Fits with 1.7 ft spare; window edges 2 ft from the bed (K-306, K-307 IN for the master). Room 17.9 x 22.9 ft clear (PF §3.1). Bed symbol in the model is not on a wall |
| BEDROOM 2, queen (5.0 x 6.67 ft), headboard on east wall | East wall free 12.3 ft; 3.6 ft each side; foot space 7.7 ft | Fits; but the wall is the laundry/mudroom wall (ARC-08); window-side sofa (2.6 x 5.9 ft) leaves 7 ft clear |
| BEDROOM 2 closet | WIC 6.1 x 2.6 ft clear, shelves 1.12 ft deep | Reach-in size, 20 sf (ARC-04) |
| Master WICs | 10.2 x 8.6 ft clear, shelves 1.7 ft deep on 3 sides (y 21.15-22.93 and y 27.2-28.91, x 96.51-98.16) | Aisle between runs 4.27 ft, usable |
| Dining, 8 seats | Table 3.62 x 9.21 ft | Fits (ARC-24) |
| Kitchen island | 6.9 x 9.87 ft, aisle 3.95 ft west, 10.2 ft east | Aisle under 54 in (ARC-10) |
| Great room, sectional plus chairs | Three sofa boxes and a table in 26.1 x 16.7 ft clear | Fits (K-132 IN); window wall is 26.5 ft with 21.9 ft of openings, so no clean TV wall except the east wall (12.7 ft shared with OFFICE) |
| Sun room, dining for 4 | table 2.6 x 3.6 ft, sofas along west and north walls | Not shown (ARC-24) |
| BUNK ROOM | Two bed boxes, one under the window | ARC-12 |

## The sore spot: bedroom wing and hall

**Current wing (model coordinates, feet).**

| Room | Rect x0,y0 to x1,y1 | sq ft |
|---|---|---|
| BEDROOM 2 | 7.27,35.46 to 22.1,48.13 | 188 |
| WIC | 7.27,48.13 to 13.78,51.15 | 20 |
| WC (suite) | 7.27,51.15 to 13.78,55.3 | 27 |
| BATH 2 | 7.27,55.3 to 17.5,62.04 | 69 |
| (suite entry) + (2nd piece) | 13.78,48.13 to 22.1,53.75 and 13.78,53.75 to 17.5,55.3 | 47 + 6 |
| HALL @22.1,49.64 | 22.1,49.64 to 42.65,53.75 | 84 |
| (N-S hall) | 37.3,35.46 to 42.65,49.64 | 76 |
| BUNK ROOM | 17.5,53.75 to 32.6,66.64 | 195 |
| STUDY | 32.6,53.75 to 42.65,63.42 | 97 |
| LAUNDRY / MUDROOM | 22.1,40.56 to 37.3,49.64 / 22.1,35.46 to 37.3,40.56 | 138 / 78 |

Wing circulation (suite entry 47 + 6, E-W hall 84, N-S hall 76, landing 17) is 230 sf of the 891 sf total. The E-W hall cannot be removed without moving BEDROOM 2's entry, because LAUNDRY and MUDROOM fill the space between BEDROOM 2's lobby and the N-S hall (door-graph, PF §7.1); sending the bedrooms through the laundry is what the Oct round-2 note rejected. The only real circulation lever in this wing is the suite sliver (6 sf), so alternatives are about function, noise and width, not big area savings. The far bigger lever is the 481 sf spine (ARC-07).

**Alternative A: "Walker-wide hall" (K-060, K-003).** Widen the E-W hall from 4.11 to 5.0 ft (clear 4.6 ft = 55 in).

| Room | New rect | sq ft | change |
|---|---|---|---|
| HALL @22.1,49.64 | 22.1,49.64 to 42.65,54.64 | 102.8 | +18.3 |
| BUNK ROOM (SW notch for x 22.1-32.6) | 17.5,53.75 to 32.6,66.64 less the strip y 53.75-54.64 east of x 22.1 | 185.7 | -9.3 |
| STUDY | 32.6,54.64 to 42.65,63.42 | 88.1 | -8.9 |

Net floor area 0 (wing envelope unchanged). Circulation: 891 to 909.3 sf = 16.2% to 16.6%. Gains: clear hall 55 in versus 45 in; the three doors off the hall (M17, M24, M25) can be widened to 36 in without landing in a corner. Costs: study and bunk shrink by 18.2 sf in total. Adds nothing for noise (ARC-08).

**Alternative B: "Study next to the bedroom, laundry beside the bath group" (K-008, K-325).** Swap STUDY and LAUNDRY, and give the master wing its own laundry (ARC-02).

| Room | New rect | sq ft | change |
|---|---|---|---|
| STUDY (moved) | 22.1,40.56 to 37.3,49.64 | 138 | +41 |
| LAUNDRY (moved, door off the E-W hall at old M25) | 32.6,53.75 to 42.65,63.42 | 97 | -41 |
| MASTER LAUNDRY (ex LINEN) | 121.94,20.56 to 128.13,29.51 | 55 | 0 (rename) |
| everything else | unchanged | | |

Net floor area 0; circulation unchanged at 891 sf = 16.2%. BEDROOM 2's east wall (7.6 ft) then touches a quiet study instead of the laundry; the MUDROOM wall (5.1 ft) remains. Costs: the laundry sits against the BUNK ROOM (9.7 ft shared) and the SUN ROOM (9.7 ft shared at x 42.65), so the noise moves; the old laundry's drying rack and sink lose their wall. Honest result: B only pays if Kayla accepts the laundry beside bunk and sun room. A hybrid is the master laundry from ARC-02 alone (no moves).

## If the tunnel architecture is reinstated

Not touched by this brief: nothing in the architecture and flow checks depends on the shop or the tunnel. The basement HALLWAY and UTILITY room would see a tunnel door, a basement-side question for the Wave 1 services reviewers.


## Parents' house (second pass; `docs/small_house/IMG_0415.PNG`, `IMG_0416.PNG` only)

Plan v1: 32 x 21 ft = 672 sf, one bedroom (11'-3" x 14'-3" labelled), one bath, crawl space, 7 ft deep full-width porch, services from the main house (TBD). Dimensions below that are not labelled on the sheet are read from the 32 ft = 965 px scale (about 30 px per ft) and are approximate.

| Item | What the sheet shows | Aging-in-place note |
|---|---|---|
| Doors | No door widths are labelled. Scaled: bath door leaf about 2.5 ft; entry door about 3 ft; the living/hall gap in the bedroom wall about 3.1 ft | Cannot confirm a 32 in clear opening; the main house already uses 28 to 31 in bath doors (ARC-05) |
| Bathroom | Tub (about 4.8 ft long) along the north wall, toilet and a small fixture at the east end; the door swing arc lies in the bath/W-D hall; no walk-in shower is drawn | No turning space and no walk-in shower: K-055 equivalent MISSING |
| Laundry | W/D drawn in the strip between bath and bedroom, next to the bedroom opening | Good adjacency; sight line from bedroom to W/D |
| Closet | Opens from the bedroom wall (arc at the closet's south side) | Direct bedroom access |
| Bedroom | 11'-3" x 14'-3" (160 sf); bed box about 5.5 x 6.4 ft against the west wall | Room is large enough for a queen with walker clearance on one side only |
| Step-free | Floor is raised over the crawl space; the plan does not give the height (PF §13 row i: the 2'-4" is not readable). The 3D view shows four porch steps and no ramp | If the rise is 2'-4" (28 in, as in the brief), a ramp at 1:12 would need 28 ft of run (arithmetic only; ramp slope rule not looked up here); step-free access is not planned |
| Porch and egg chair | Porch 7.0 ft deep, 32 ft long; egg-chair hook at about 3.5 ft from the wall and 3.5 ft from the edge; the swing ticks run to about 3.3 ft radius (6.6 ft diameter) | Only about 0.2 ft spare either side in the 7 ft depth; the chair also swings in front of the bedroom window; nearest post is about 5.1 ft east; check swing against the post and window |
| Kitchen | Counter along the north wall (about 20 ft); a grey box about 6 x 2.6 ft in the living room (island or table, not labelled) | About 7 ft from the counter to the box: walker-passable |

Parents' house findings are not scored in the main table. Position, services and drainage are not in any model (PF §13 row i).

## plan_facts corrections

None found in the sections I used (§3, §4, §5, §6, §7, §8, §9). Two items to watch: PF §6.1 lists the foyer as kind hall but excludes it from the 891 sf total (stated in its own definition), so a reader comparing "hall" areas should use 891 sf with a 309 sf foyer line; PF §15.14 (no powder room) and PF §8.3 (no garage-scullery door) are consistent with my reading of `main_floor.scad:120-123`.

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| ARC-05 | `search.py --doc abc_2023 '"9.5.5.1"'` | abc_2023 | 842 | Table 9.5.5.1. | All doors in at least one line of passage from the exterior to the basement 810 1 980 |
| ARC-05 | `search.py --doc abc_2023 '"9.5.5.1"'` | abc_2023 | 842 | Table 9.5.5.1. | Bathroom, water-closet room, shower room (1) 610 1 980 |
| ARC-21 | `search.py --doc abc_2023 '"9.5.4.1"'` | abc_2023 | 841 | 9.5.4.1. | The unobstructed width of a hallway within a dwelling unit shall be not less than 860 mm |
| ARC-28 | `search.py --doc abc_2023 '"9.5.3.1"'` | abc_2023 | 841 | Table 9.5.3.1. | Master bedroom or bedroom space 2.1 Lesser of area of the space or 4.9 m2 |
