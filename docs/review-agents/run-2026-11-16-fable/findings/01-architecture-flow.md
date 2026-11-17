# 01 Architecture / Flow findings (ARC)

- Specialist: Architecture/flow (Sonnet 5.5), prefix ARC, date 2026-11-16.
- Inputs read: COMMON-RULES, SPECIALIST-FORMAT, brief 01; PF-V12 §0-§12, PF-V2 §0-§12, PF-V3 §0-§12, PF-ALT §0-§12, PF-COMPARE §1-§10; kayla_checklist.md (all 164 PLAN rows, K-001..K-335); household brief docs/review-agents/agents/architecture-flow.md. Sheets looked at: v12 p.3, v2 p.3, v3 p.3, alt p.2 (Rooms) to confirm room positions and which room touches which. Code pages opened with `search.py --page`: abc_2023 PDF p.841 and p.842.
- Scope notes. No plan prints a north arrow, drive, roof/cover, or basement sheet; K items that need those are N/S, not MISSING. Beds are judged against a king 76 x 80 in (stated assumption). Structural and gas items are for a licensed Alberta engineer; not reviewed here. Verdicts are conservative: partial = MISSING.

## 1. Kayla cross-check (164 PLAN items)

### 1a. Counts (of 164)

| Plan | IN | MISSING | CONTRADICTED | N/S | Total |
|---|---|---|---|---|---|
| V1-2 | 59 | 59 | 14 | 32 | 164 |
| V2 | 62 | 56 | 14 | 32 | 164 |
| V3 | 55 | 62 | 15 | 32 | 164 |
| ALT | 57 | 68 | 7 | 32 | 164 |

### 1b. Deal-breaker table (12 groups)

| # | Deal-breaker (K-IDs) | V1-2 | V2 | V3 | ALT | Evidence |
|---|---|---|---|---|---|---|
| 1 | Bedroom directly adjacent to foyer (K-328) | IN | IN | IN | IN | V1-2/V2/V3 bedroom doors are 36 in doors on the hall about 18-20 ft from the vestibule (PF-V12 §10, PF-COMPARE §6b R8/R9); ALT has no bedroom on the foyer, but Bathroom 2 shares the foyer north wall and hall 16 opens to the foyer by a 39.9 in passage (PF-ALT §11). |
| 2 | Laundry far from bedrooms / not tied to master suite (K-329, K-036) | IN | IN | IN | IN | Laundry about 20 ft from the master door, 36 in door into the master vanity zone (V1-2 room 19, V2 room 18, V3 room 17) (PF-V12 §11). ALT: direct 36 in door from the master bedroom, about 6 ft (PF-ALT §10, §11); intent met, though not "through bath or closet" as written. |
| 3 | Major path only through the kitchen zone (K-330) | IN | CONTRADICTED | CONTRADICTED | IN | V2: garage entry room 7 has doors to garage, toilet room, pantry, kitchen and terrace only; no hall door, so garage to laundry/master/hall runs through room 2 (PF-V2 §3). V3: mudroom 8 same (PF-V3 §3); V3 also has no hall-kitchen door. V1-2: mudroom has a 36 in open to the hall (PF-V12 §3). ALT: mudroom to utility (66 in open) to hall 10 door 42 in (PF-ALT §3 rows 6, 9). |
| 4 | Closets on exterior walls (K-331, K-070) | CONTRADICTED | CONTRADICTED | CONTRADICTED | CONTRADICTED | V1-2 closets 17 and 20 on master-wing exterior walls (PF-V12 §11); V2 closets 16, 19 plus room 8 wardrobes (PF-V2 §11); V3 closets 15, 18 plus room 7 wardrobes (PF-V3 §11); ALT WIC 23 north wall, Closet 29 east wall (PF-ALT §11). |
| 5 | Full open concept, linear living-dining-kitchen (K-332) | CONTRADICTED (partial) | IN | IN | IN | V1-2: kitchen and dining are one 616.78 ft² room (v12 p.1), living beyond a 48 in opening, in a row (PF-V12 §7); the living room is walled, hence partial. V2/V3: every space is a walled room with doors (PF-V2 §7, PF-V3 §7). ALT: separate rooms, 60 in sliding runs (PF-ALT §7). |
| 6 | Master closet only through the master bath (K-333, K-201, K-304) | CONTRADICTED | CONTRADICTED | CONTRADICTED | IN | V1-2/V2/V3 closets open off the vanity zone only; read from p.1 door positions, flagged "inferred" in PF-V12 §11, PF-V2 §11, PF-V3 §11. ALT both WICs open off the bedroom (31.5 and 36 in) (PF-ALT §3 rows 39-40). |
| 7 | Bedrooms sharing a wall with the living room (K-334) | IN | IN | IN | IN | "no" in all four PF §11. V3 living room's west wall is the garage (PF-V3 §11), not a bedroom. |
| 8 | Garage at rear / drive past bedrooms (K-335, K-005) | IN (position only) | IN (position only) | IN (position only) | IN (position only) | Garage bottom-left, doors on the left sheet edge, bedrooms at the top in all four (PF-COMPARE §9). The drive itself is N/S (no site plan). |
| 9 | Costco door pantry to garage (K-037, K-115, K-315) | IN | MISSING | MISSING | MISSING | V1-2 pantry 36 in door to garage, 36 in double door to kitchen (PF-V12 §7). V2/V3 pantry shares the garage wall but no door (PF-V2 §7, PF-V3 §7). ALT pantry does not touch the garage (PF-ALT §7). |
| 10 | Wide doors and halls (K-003, K-060, K-061) | MISSING | MISSING | MISSING | MISSING | Narrowest door 31.5 in x about 4 in V1-2/V2/V3 (PF §3); ALT 31.5 x 2 plus Bedroom 2 door 34.4 in on alt p.28 (36.0 on p.26) (PF-ALT §3). Narrowest hall: V1-2/V2/V3 corridor about 48 in measured +/- 6 (PF §5; the 96.0 in west zone is wider); ALT Hall 16 47.9 in, Hall 10 48.1 in printed (PF-ALT §5). Most doors are 36 in. |
| 11 | No-threshold shower (K-055) | N/S | N/S | N/S | N/S | No sheet shows a curbless tray (PF §6). |
| 12 | Bathroom reachable from every living zone and both entries (K-033) | IN | IN | IN | CONTRADICTED | V1-2: powder room about 24 ft from front door, about 40 ft from living via the hall (PF-V12 §11). V2/V3 add a WC off the garage entry (V2 room 27, V3 room 25) (PF-V2 §11, PF-V3 §11). ALT: no bath on the kitchen/living side, living centre to powder room about 76 ft (PF-ALT §11). |

Deal-breakers met (IN): V1-2 7, V2 6, V3 6, ALT 7 (of 12; group 11 is N/S in all four, so 11 are scoreable).

### 1c. Item-by-item table (164 PLAN items, K order)

Verdict letters: IN / MISSING / CONTRA = CONTRADICTED / N/S. "PF" refs are to the plan's own fact sheet; where they differ the evidence names each plan.

| K-ID | Item (short) | V1-2 | V2 | V3 | ALT | Evidence |
|---|---|---|---|---|---|---|
| K-001 | one story | IN | IN | IN | IN | One floor drawn in all four; stair to basement only (PF-V12 §9, PF-ALT §9) |
| K-002 | basement | IN | IN | IN | MISSING | V12/V2/V3 print 'Open to Basement' + stair 53.8 in (PF-V12 §9); ALT stair drawn but unlabelled, no basement sheet in any set (PF-ALT §9) |
| K-003 | wider doors/halls | MISSING | MISSING | MISSING | MISSING | Narrowest door 31.5 in (V12/V2/V3 x~4, ALT x2 + Bed 2 34.4); halls ~48 in (V12-3 corridor meas.; ALT 47.9/48.1); typical door 36 (PF §3, §5) |
| K-004 | more space bath/shower/furniture | MISSING | MISSING | MISSING | MISSING | Master wet rooms: V12-3 shower base 78.8x78.3 + tub 78.8x27.6, hall bath 68.57 ft2; ALT shower 104.3x56, Bath 3 55.43 ft2 (PF §6). No plan is clearly roomier |
| K-005 | driveway not past bedrooms | N/S | N/S | N/S | N/S | No drive/site plan in any set (COMMON-RULES); garage position only, see K-335 |
| K-006 | group wet walls | IN | MISSING | MISSING | MISSING | Largest listed wet-group gap: V12 ~30 ft, V2 ~40, V3 ~55, ALT ~80+ (PF-COMPARE §7) |
| K-007 | daylight where needed | IN | IN | CONTRA | CONTRA | V3 living 3 (571 ft2) has no window (PF-V3 §4); ALT dining 240 ft2 and breakfast 144 ft2 no window (PF-ALT §4); V12/V2 all main rooms glazed |
| K-008 | noise separation | IN | IN | IN | MISSING | Bedroom wing at top, no bedroom shares a wall with living/kitchen/garage (PF §11). ALT: Bathroom 2 shares foyer north wall, hall 16 opens to foyer (PF-ALT §11) |
| K-009 | public/private | IN | IN | IN | IN | No public room is reached through a bedroom in any set. Note ALT Bedroom 2 -> Bath 2 passes Bedroom 3 (PF-ALT §10) - private-to-private |
| K-010 | 2 ft increments | N/S | N/S | N/S | N/S | No stock-size or framing grid printed; sheets cannot show it |
| K-012 | south living/backyard | N/S | N/S | N/S | N/S | No north arrow (COMMON-RULES) |
| K-013 | north master | N/S | N/S | N/S | N/S | No north arrow |
| K-014 | east bedrooms/sunroom | N/S | N/S | N/S | N/S | No north arrow |
| K-021 | sit near cook | IN | IN | IN | MISSING | V12 dining table 72 dia in kitchen room; V2 nook table 35.4+banquette 78.7; V3 table 35.4 + 4 chairs in kitchen (PF §8). ALT kitchen has no seat; breakfast room beyond 60 in opening (PF-ALT §7) |
| K-023 | covered outdoor cooking | N/S | N/S | N/S | N/S | No roof/cover on any terrace (PF-COMPARE §2); V2 grill-type symbols on open terrace (PF-V2 §8) |
| K-030 | lots of food storage | MISSING | IN | IN | MISSING | Pantry V12 95.91, V2 132.83, V3 117.87, ALT 85.47 ft2 (PF-COMPARE §3). Rule used: IN if >=100 ft2 |
| K-031 | home office, privacy | IN | IN | IN | IN | Office V12/V2/V3 144.02 ft2, 48 in double door onto hall (PF §3); ALT 237.99 ft2, off foyer + hall-10 nook (two doors) |
| K-032 | library | MISSING | MISSING | MISSING | IN | No library in V12/V2/V3 (PF §11); ALT Library 239.28 ft2 (PF-ALT §2) |
| K-033 | bath from all living zones/entries | IN | IN | IN | CONTRA | Powder room ~24 ft from front door, ~40 ft from living (V12), V2/V3 add a WC off the mudroom entry (PF-V2 §11, PF-V3 §11). ALT: no bath on kitchen/living side, living-to-powder ~76 ft (PF-ALT §11) |
| K-034 | bug-free sit-out | IN | MISSING | MISSING | IN | Sunroom V12 147.04 ft2, ALT 269.42 ft2 (glazed). V2/V3: no room named sunroom, position now dressing/sitting room (inferred) (PF-V2 §2, PF-V3 §2); screened porch not shown in any set |
| K-035 | kitchen-dining direct | IN | IN | IN | IN | V12 same room; V2/V3 48 in double door direct; ALT 60 in opening direct (PF-COMPARE §8) |
| K-036 | laundry by master, via bath/closet | IN | IN | IN | IN | V12/V2/V3 laundry 36 in door to vanity zone (room 19/18/17) of master wet group (PF §11); ALT direct 36 in door from master bedroom (not via bath/closet, intent met) (PF-ALT §11) |
| K-037 | pantry adjacent garage + Costco door | IN | MISSING | MISSING | MISSING | V12 pantry 36 in door to garage (PF-V12 §7). V2/V3 pantry shares garage wall, NO door (PF-V2 §7, PF-V3 §7). ALT pantry shares no wall with garage (PF-ALT §7) |
| K-038 | broom/vacuum closets | MISSING | MISSING | MISSING | MISSING | Closets 13.35/6.89 ft2 etc. exist but none labelled broom/vacuum (PF §2); ALT closets 28/29 unlabelled |
| K-040 | linen closets near bedrooms | IN | IN | IN | MISSING | p5 prints 'Floor-standing linen cabinet' x3, 'Corner linen cabinet' (PF-V12 §6; wing unchanged in V2/V3). ALT: only 'Mini cabinet for bathroom' x2 in master bath (PF-ALT §6) |
| K-041 | vestibule | IN | IN | IN | MISSING | Vestibule 39.18/39.29/39.18 ft2 (PF-COMPARE §3); ALT none, 60 in double front door opens into foyer (PF-ALT §5) |
| K-043 | mail drop zone | MISSING | MISSING | MISSING | MISSING | No mail/command-centre item labelled on any Furniture sheet |
| K-044 | purse/keys drop | MISSING | MISSING | MISSING | MISSING | Not labelled on any sheet |
| K-047 | shoes at doorway | MISSING | MISSING | MISSING | MISSING | No shoe storage labelled at front entry; V2 room 7 shoe units are at the garage entry (PF-V2 §8) |
| K-053 | clearance around bed | IN | IN | IN | IN | Beds with 19.7 in nightstands each side: master 76x84 in 326 in wide room (V12-3); secondary 63x84 in 144 in rooms; ALT 63x78.7 in 144 in rooms, master bed 82x86 (PF §8) |
| K-055 | no-threshold shower | N/S | N/S | N/S | N/S | No curbless tray identifiable on any sheet |
| K-058 | elevator space | IN | IN | IN | IN | Future Elevator/Closet 45.21 (V12) /44.24 (V2,V3), ALT Elevator Closet 34.12 ft2 (PF-COMPARE §4) |
| K-059 | dumb waiter | MISSING | MISSING | MISSING | MISSING | Not drawn in any set |
| K-060 | wide walkways | MISSING | MISSING | MISSING | MISSING | Hall V12-3 corridor ~48 in meas. +/-6 (PF §5); ALT 47.9/48.1 printed, foyer openings 39.9/40.1 (PF-ALT §5). A 36 in walker/wheelchair want is not confirmed |
| K-061 | wide doorframes | MISSING | MISSING | MISSING | MISSING | Most doors 36 in; 31.5 in x~4 (V12-3), x2 + 34.4 (ALT) (PF §3) |
| K-062 | broken open | MISSING | IN | MISSING | IN | V12 kitchen+dining one 617 ft2 room (living walled, 48 in opening); V2 nook + dining/living in separate rooms with 48 in doubles and a glazed dining/living wall; V3 all closed rooms with doors; ALT 60 in sliding panel runs + foyer open to hall 10 |
| K-064 | windows on 2 walls (living spaces) | MISSING | MISSING | CONTRA | MISSING | V12 living bay 2-3 walls but kitchen/dining 1 wall; V2 living 1 exterior wall (2nd is glazing into dining, PF-V2 §4); V3 living none; ALT living 2 walls, dining/breakfast none |
| K-069 | simple forms | CONTRA | CONTRA | MISSING | IN | Outside corners: V12 ~28, V2 ~32 (inferred counts), V3 not counted (upper half as V12, lower block plain rectangle), ALT ~10-12 T/L (PF-COMPARE §2) |
| K-070 | closets off exterior walls | CONTRA | CONTRA | CONTRA | CONTRA | V12-3 master closets 17/20 (15/18) on east/west exterior walls (PF §11); ALT WIC 23 north, Closet 29 east (PF-ALT §11) |
| K-071 | closets entirely interior | CONTRA | CONTRA | CONTRA | CONTRA | as K-070; V2/V3 also room 8/7 wardrobes on the east exterior wall |
| K-072 | toilet between shower and door | N/S | N/S | N/S | N/S | Exhaust fan not shown; fixture order inside each bath not extracted in PF |
| K-074 | tubs off exterior walls | IN | IN | IN | CONTRA | V12-3 tub in interior wet room (PF §11); ALT master, Bath 2 on west wall, Bath 3 east wall (PF-ALT §11) |
| K-075 | no 2 wings split by great room | IN | IN | IN | IN | V12/V2/V3 master and bedroom wings split by an unheated 390.52 ft2 terrace notch, hall band between, not a great room; ALT one wing + one block (PF §1) |
| K-077 | windows not directly across | CONTRA | CONTRA | CONTRA | IN | Master east and west walls each 48 in pair, directly opposite (PF-V12 §4; unchanged in V2/V3). ALT: wing windows not on one axis; garage N/S windows opposite (PF-ALT §4) |
| K-078 | windows on a diagonal | MISSING | MISSING | MISSING | MISSING | Master windows opposite, not diagonal (V12-3); ALT bedrooms 1 window each (PF §4) |
| K-080 | windows to corners | MISSING | MISSING | MISSING | MISSING | V12-3 master windows in corners flanking 205.9 in solid wall (PF-V12 §4) but other rooms not read; ALT window widths/positions not printed (PF-ALT §4) |
| K-081 | overhangs on west windows | N/S | N/S | N/S | N/S | No roof or elevations, no orientation |
| K-083 | golden-ratio rooms | MISSING | MISSING | MISSING | MISSING | Mixed: V3 kitchen 294x306.1 = 1.04, dining 230.3x221.4 = 1.04, living 357.3x230.3 = 1.55; ALT dining/library 240x144 = 1.67, breakfast 1.0; V12 master ~1.9 (PF §1/§2) |
| K-095 | covered patio depth | N/S | N/S | N/S | N/S | No cover/roof drawn |
| K-096 | kitchen counters on inside walls | MISSING | MISSING | MISSING | MISSING | Sink runs on exterior walls in all four (V12 S, V2 W, V3 S, ALT S) per K-124; range walls interior (PF §7) |
| K-099 | active spaces to sun | N/S | N/S | N/S | N/S | No orientation |
| K-100 | bedrooms for morning light | N/S | N/S | N/S | N/S | No orientation |
| K-102 | bathroom not open to toilet | N/S | N/S | N/S | N/S | Not determinable (PF §11) |
| K-103 | no view of baths | N/S | N/S | N/S | N/S | Not determinable from PF (door swing/line of sight not extracted) |
| K-104 | no view into bedroom doors | CONTRA | CONTRA | CONTRA | MISSING | V12/V2/V3 bedroom doors 36 in on the public hall (PF-V12 §3 p14 wall 8); ALT hall 16 ends at master double 47.9 in, 39.9 in open passage from foyer (PF-ALT §3) |
| K-105 | no view of laundry from public | CONTRA | CONTRA | CONTRA | IN | V12-3 laundry 48 in double door opens on the main hall (PF-V12 §3); ALT laundry on private hall 16 (PF-ALT §3) |
| K-106 | large island no seating | IN | IN | IN | IN | Island 120x60 in all four, no stools drawn (PF §7) |
| K-107 | breakfast nook | MISSING | IN | IN | IN | V12 none (dining only); V2 nook 35.4 + banquette 78.7; V3 round 35.4 + 4 chairs; ALT Breakfast Room 143.91 ft2 |
| K-108 | nothing in island | IN | IN | IN | IN | Island drawn plain; sink on exterior wall, range on a wall (PF §7) |
| K-114 | walk-in pantry w/ appliances | IN | IN | IN | IN | Enclosed pantry in all four; small-appliance counter space not identifiable (PF §7) |
| K-115 | Costco door in pantry, garage wall | IN | MISSING | MISSING | MISSING | as K-037 |
| K-116 | kitchen near rear entry | IN | IN | IN | MISSING | Garage door -> kitchen: V12 13 ft, V2 18/26, V3 13, ALT 19 ft to threshold via 2 rooms (PF-COMPARE §6b) |
| K-117 | coffee bar + pot filler | MISSING | MISSING | MISSING | MISSING | V2 coffee bar is on the living-room wall (PF-V2 §7); no pot filler or bar by a nook in any set |
| K-123 | face living areas from island | IN | CONTRA | CONTRA | CONTRA | V12 island in the open room facing dining/living; V2/V3 kitchen is an enclosed room, living behind a 48 in double door; ALT living behind a 36 in single door (PF-COMPARE §8) |
| K-124 | sink under window | IN | IN | IN | IN | V12 S wall, V2 W wall under 3x36 windows, V3 S under 144.4, ALT S under 2 windows (PF-COMPARE §8) |
| K-127 | dining access to outdoor dining | MISSING | IN | IN | MISSING | V12 dining has no exterior door (terrace via sunroom) (PF-V12 §3); V2 72 in slider; V3 94.5 in slider + 8-seat table; ALT dining no exterior opening (PF-ALT §7) |
| K-128 | dining seats 8 | IN | IN | IN | IN | V12 72 dia + 8; V2 96x42 + 8; V3 72 dia + 8; ALT 96x42 + 8 (PF §8) |
| K-129 | openable doors, dining | MISSING | MISSING | MISSING | MISSING | V12 none; V2 72 in 2-panel slider; V3 94.5 in 3-panel slider (not fully openable); ALT none |
| K-132 | sectional + chairs | IN | IN | IN | IN | Sectional + 2-3 armchairs + coffee table drawn in all four (PF §8) |
| K-133 | living to patio/sunroom | MISSING | IN | MISSING | IN | V12 via hall to sunroom 22 ft, no door; V2 72 in slider to terrace; V3 living has no exterior wall; ALT 203.2 in glazed opening to Terrace D |
| K-134 | openable doors, living | MISSING | MISSING | MISSING | IN | V12/V3 none; V2 72 in 2-panel slider; ALT 203.2 in glazed opening |
| K-140 | sit to put on shoes at entry | MISSING | MISSING | MISSING | MISSING | No bench labelled at front entry; V2 bench 72 is at the garage entry (PF-V2 §8) |
| K-141 | coat storage for guests | IN | IN | IN | MISSING | Hall coat wall 142.0 in (PF-V3 §5; unchanged V12-V3); ALT foyer cabinet run unlabelled |
| K-142 | hidden coat/shoe storage | MISSING | MISSING | MISSING | MISSING | Hall slat screen 49.3+7.0+49.3 is a screen, not a closed closet (PF-V3 §5) |
| K-143 | drop zone at entry | MISSING | MISSING | MISSING | MISSING | Not labelled in any set |
| K-144 | no line of sight to kitchen/living | IN | IN | IN | IN | No direct line from front door (PF-COMPARE §9) |
| K-145 | powder near front door | IN | IN | IN | IN | 24 / 22-24 / 22-24 / 28 ft (PF-COMPARE §9) |
| K-146 | mudroom seating | MISSING | IN | MISSING | MISSING | V2 entry room 7 bench 72.0 (PF-V2 §8); other mudroom contents not itemised in PF |
| K-147 | mudroom shoe storage | MISSING | IN | MISSING | MISSING | V2 room 7 shoe/coat units (PF-V2 §8); V3 'cabinets, coat units' (PF-V3 §2) unspecific |
| K-149 | mudroom hidden coat | MISSING | IN | IN | MISSING | V2 coat units; V3 coat units (PF-V3 §2) |
| K-151 | mudroom drop zone | MISSING | IN | MISSING | MISSING | V2 bench + hooks + shoe units; others not itemised |
| K-153 | mudroom mail area | MISSING | MISSING | MISSING | MISSING | Not labelled |
| K-155 | mudroom outdoor entrance | MISSING | IN | MISSING | IN | V2 room 7 36 in door to south terrace; ALT mudroom 42 in exterior door; V12/V3 mudroom has none (PF §3) |
| K-156 | garage entrance at mudroom | IN | IN | IN | IN | V12 42 in, V2 36, V3 36, ALT 36 (PF-COMPARE §5) |
| K-157 | bath off mudroom | MISSING | IN | IN | MISSING | V2 room 27 (21.21 ft2) off room 7; V3 room 25 (30.03 ft2) inside mudroom; V12/ALT none |
| K-158 | laundry near master | IN | IN | IN | IN | as K-036 |
| K-163 | laundry sink | IN | IN | IN | MISSING | V12 sink p20; ALT not drawn (PF-ALT §6) |
| K-166 | pass-through basket | N/S | N/S | N/S | N/S | Hatch/chute not drawn or drawable; ALT has a direct door instead |
| K-170 | dog bath at rear entry | MISSING | MISSING | MISSING | MISSING | Not drawn; ALT mudroom has sink + unlabelled grate 47.2x31.5 (PF-ALT §6) |
| K-172 | cat litter area | MISSING | MISSING | MISSING | MISSING | Not drawn (cat tree only) |
| K-179 | full bath not through a bedroom | IN | IN | IN | MISSING | V12-3 hall bath off the hall (PF §6); ALT Bath 2/3 reached only via bedrooms; powder room draws a tub/shower-type fixture (PF-ALT §6) |
| K-183 | office to porch | MISSING | MISSING | MISSING | MISSING | Office has no exterior door in any set (PF §3) |
| K-185 | sunroom full glass walls | IN | MISSING | MISSING | MISSING | V12 south wall 3 glazed units 132 of 134 in + east; ALT 126 of 202 / 192 in; V2/V3 no sunroom |
| K-186 | sunroom open to patio | IN | MISSING | MISSING | IN | V12 south glazed units to terrace; ALT two 126 in glazed doors (PF §3) |
| K-188 | sunroom lounge furniture | IN | MISSING | MISSING | IN | V12 sofa 68.1; ALT two sofas + armchair (PF §8) |
| K-189 | sunroom dining for 4 | MISSING | MISSING | MISSING | MISSING | V12 2-seat bistro only; ALT none |
| K-191 | master private porch | IN | IN | IN | MISSING | V12/V2/V3 48 in door master -> north terrace (PF-V12 §3); ALT Terrace A above wing, no door listed |
| K-192 | no fireplace in master | IN | IN | IN | IN | None drawn |
| K-195 | room to walk around bed | IN | IN | IN | IN | Master 458.12 ft2 (V12-3), 300.64 ft2 (ALT) (PF §2) |
| K-200 | separate walk-in closets | IN | IN | IN | IN | V12-3 closets 72.01 + 63.94 ft2; ALT WIC 53.39 + 52.85 ft2 |
| K-201 | closet access not just via bath | CONTRA | CONTRA | CONTRA | IN | V12-3 closets open off the vanity zone only (inferred p1) (PF-V12 §11); ALT both WICs off the bedroom, 31.5 + 36 in doors |
| K-202 | via bath ok if not only way | CONTRA | CONTRA | CONTRA | IN | as K-201 |
| K-203 | closet to laundry or via bath | IN | IN | IN | MISSING | V12-3 closet - vanity zone - laundry; ALT closets to laundry through bedroom only |
| K-210 | floor/kick laundry | N/S | N/S | N/S | N/S | Not drawable |
| K-211 | large walk-in shower, no step | MISSING | MISSING | MISSING | MISSING | Size only: V12-3 base 78.8x78.3, ALT 104.3x56; no-step not shown |
| K-220 | sunken tub for 1-2 | MISSING | MISSING | MISSING | MISSING | Tub 78.8x27.6 (V12-3), ALT 84.3x40.2; 'sunken' not shown (PF §6) |
| K-224 | double vanity | IN | IN | IN | IN | V12-3 room 19 two lavs 31.5 on 125 in; ALT 90.7 in double vanity |
| K-226 | closed towel storage | IN | IN | IN | IN | Linen cabinets (V12-3, PF-V12 §6); ALT 2 mini cabinets (PF-ALT §6) |
| K-227 | water closet, 2, spacious | MISSING | MISSING | MISSING | MISSING | V12-3 one 47.8x72 toilet room in the master group; ALT one WC 79.4x43 |
| K-228 | master bath to laundry | IN | IN | IN | MISSING | V12-3 laundry door onto vanity zone; ALT laundry opens to bedroom/hall, not the bath |
| K-229 | master bath to closets | IN | IN | IN | MISSING | V12-3 closets off vanity zone; ALT WICs off bedroom (PF-ALT §2 notes 11/23/24/27/28 partly open: unresolved) |
| K-237 | flex room w/ bed option | MISSING | MISSING | MISSING | MISSING | No craft/flex room; offices 144 ft2 (V12-3), 237.99 (ALT) |
| K-238 | guest bedroom with queen | IN | IN | IN | IN | Queen beds 59.4x79.9 / 63x84 (V12-3); 63x78.7 (ALT) |
| K-239 | guest ensuite | MISSING | MISSING | MISSING | IN | V12-3 none; ALT Bedroom 3 -> Bath 2, Bedroom 4 -> Bath 3 (36 in doors) |
| K-240 | guest private access | MISSING | MISSING | MISSING | MISSING | No porch/garage door to a bedroom in any set |
| K-242 | bedrooms 3 and 4 | MISSING | MISSING | MISSING | IN | V12-3: 2 + master = 3 bedrooms; ALT 4 (PF-COMPARE §10) |
| K-244 | Jack and Jill bath | MISSING | MISSING | MISSING | MISSING | Not drawn; ALT baths are ensuites to one bedroom each |
| K-245 | nursery near master | MISSING | MISSING | MISSING | MISSING | V12 room 14 113.67 ft2 lounge (inferred use) beside master; no designated small bedroom; ALT Bedroom 4 142.62 is 3rd along the wing |
| K-248 | covered front porch | N/S | N/S | N/S | N/S | No cover drawn |
| K-249 | covered mudroom entry | N/S | N/S | N/S | N/S | No cover drawn |
| K-252 | covered patio dining | N/S | N/S | N/S | N/S | No cover drawn; V12/V3 8-seat outdoor table on open terrace, V2 72 dia |
| K-253 | covered patio lounge | N/S | N/S | N/S | N/S | No cover drawn; sofas on open terrace (V12/V2/V3) |
| K-254 | open sunny area | IN | IN | IN | IN | Open terraces 1575 / 3419 / 2049 / 2709 ft2 (PF-COMPARE §2) |
| K-255 | outdoor desk spot | MISSING | MISSING | MISSING | MISSING | Not drawn |
| K-256 | 15 in landing each side cooktop/sink | N/S | N/S | N/S | N/S | Counter clear lengths not derivable from PF |
| K-257 | fridge landing 30-60 in | N/S | N/S | N/S | N/S | Not derivable |
| K-261 | work triangle 9 ft/26 ft | N/S | N/S | N/S | N/S | Leg lengths not in PF; fixture centres not extracted |
| K-262 | no line of sight to kitchen from entry | IN | IN | IN | IN | as K-144 |
| K-270 | 3-5 steps between zones | N/S | N/S | N/S | N/S | Not derivable |
| K-273 | appliance doors into walkway | N/S | N/S | N/S | N/S | Door swings of appliances not extracted |
| K-274 | 54 in dishwasher walkway | MISSING | MISSING | MISSING | MISSING | Dishwasher not labelled in any set; island aisles: V3 red clearances 36.8/49.5/56.6 unlabelled, V2 ~4-5 ft W, V12 ~8 ft, ALT ~6.5 ft (PF §7) |
| K-277 | sink not facing wall | IN | IN | IN | IN | as K-124 |
| K-279 | landing from pantry/fridge | N/S | N/S | N/S | N/S | Not derivable |
| K-281 | prep counter space | N/S | N/S | N/S | N/S | Not derivable |
| K-282 | prep between fridge and range | N/S | N/S | N/S | N/S | Appliance positions not itemised |
| K-283 | landing both sides range | N/S | N/S | N/S | N/S | Not derivable |
| K-288 | dishwasher next to sink | MISSING | MISSING | MISSING | MISSING | Dishwasher not labelled (PF §6) |
| K-290 | fridge placement | N/S | N/S | N/S | N/S | Not itemised; V12 fridge lower-left, V2 on pantry wall, V3 east run, ALT not labelled |
| K-292 | tall units end of runs | N/S | N/S | N/S | N/S | Not derivable |
| K-297 | glass partitions at entry | MISSING | MISSING | MISSING | MISSING | V12-3 hall slat screen (wood); ALT foyer glass panel behind stair + 30.7 glazed sidelight (PF-ALT §4); no glass partition between entry and rest |
| K-298 | powder off a hall, past storage | IN | IN | IN | IN | V12-3 powder 36 in slider off hall; ALT 31.5 in door off hall 16 (PF §3). 'After storage' not verified |
| K-299 | focal point across from front door | MISSING | MISSING | MISSING | MISSING | Sight line runs down corridor (V12-3) or to office double door (ALT) (PF §11) |
| K-300 | large window/glass doors opposite | MISSING | MISSING | MISSING | MISSING | as K-299 |
| K-302 | office door to bathroom | MISSING | MISSING | MISSING | MISSING | No office-bath door in any set |
| K-304 | closet not via bathroom | CONTRA | CONTRA | CONTRA | IN | as K-201 |
| K-306 | no window behind bed | MISSING | MISSING | MISSING | MISSING | Master bed head at partition (V12-3) OK; Bedroom 12 east-wall window ws36 may sit behind headboard; ALT unresolved |
| K-307 | windows in corners for bed options | MISSING | MISSING | MISSING | MISSING | Master corner windows V12-3; others not |
| K-315 | Costco door to pantry | IN | MISSING | MISSING | MISSING | as K-037 |
| K-316 | too much circulation | CONTRA | MISSING | MISSING | IN | Hall % of net heated: V12 10.1, V2 9.0, V3 8.9, ALT 7.6 (foyer+halls 15.5). Rule used: <=8 IN, 8-10 MISSING, >10 CONTRADICTED |
| K-317 | minimise circulation | CONTRA | MISSING | MISSING | IN | as K-316 |
| K-318 | kitchen not a highway | MISSING | CONTRA | CONTRA | MISSING | V2/V3: garage entry connects to the house only through the kitchen (PF-V2 §3, PF-V3 §3); V12/ALT kitchen has opposite doors but a hall/utility alternative (PF §7) |
| K-320 | landing zones | MISSING | MISSING | MISSING | MISSING | Not labelled at front or garage entry (except V2 room 7 units) |
| K-323 | uninterrupted wall space | N/S | N/S | N/S | N/S | Not assessed |
| K-324 | not too open | MISSING | IN | IN | IN | V12 kitchen+dining one room with no zone break (PF-V12 §7) |
| K-325 | bedrooms away from noisy rooms | IN | IN | IN | IN | No bedroom shares a wall with living/kitchen/dining/garage (PF §11) |
| K-326 | baths/closets as buffers | MISSING | MISSING | MISSING | IN | V12-3 master closets buffer; bedrooms 7/12 face hall and office; ALT baths sit between bedrooms and foyer |
| K-328 | bedroom adjacent foyer | IN | IN | IN | IN | V12-3 bedroom doors on hall strip ~18-20 ft from vestibule; ALT none (PF §11) |
| K-329 | laundry far from bedrooms | IN | IN | IN | IN | Laundry ~20 ft from master (V12-3), ~6 ft (ALT) |
| K-330 | major path only via kitchen | IN | CONTRA | CONTRA | IN | V2 entry room 7 and V3 mudroom 8 have no hall door: garage -> hall/laundry/master only through kitchen (PF-V2 §3, PF-V3 §3). V12 mudroom has a 36 in hall opening; ALT mudroom -> utility -> hall 10 |
| K-331 | closets on exterior walls | CONTRA | CONTRA | CONTRA | CONTRA | as K-070 |
| K-332 | full open concept, linear | CONTRA | IN | IN | IN | V12 kitchen + dining one 616.78 ft2 room, then living via 48 in pair, in a row (partial; living walled) |
| K-333 | through master bath to closet | CONTRA | CONTRA | CONTRA | IN | as K-201 |
| K-334 | bedroom sharing wall w/ living | IN | IN | IN | IN | No (PF §11) |
| K-335 | garage at rear / past bedrooms | IN | IN | IN | IN | Garage bottom-left, doors face left edge, bedrooms at top; drive not shown (PF §11) so only the garage position is scored |

## 2. Findings

Severity key: Blocker = cannot build / will not pass; Should fix = real cost or function loss; Consider = judgement call. No Blocker was found from architecture/flow: nothing drawn fails a code item cited below. Sorted by severity, then plan.

| # | Severity | Plan | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| ARC-01 | Should fix | V2, V3 | V2 room 7 (entry, 219.69 ft²) and room 2 (kitchen, 636.15 ft²); V3 room 8 (mudroom, 179.22 ft²) and room 2 (kitchen, 625.28 ft²) | The garage door leads into a room that has no door to the hall. Everything beyond (hall, laundry, bedrooms, front of house) is reached by crossing the kitchen. This is the "kitchen as a highway" Kayla lists (K-318 CONTRADICTED, K-330 CONTRADICTED). Groceries go garage -> kitchen in 13-18 ft (good, K-116 IN), but a person coming in from the garage to reach the master walks about 60-68 ft through the kitchen and hall (primary -> kitchen routes, PF-COMPARE §6b R7). V1-2 does not have this: its mudroom has a 36 in open to the hall (PF-V12 §3). | PF-V2 §3 (room 7 connects only to garage, 27, 13, 2, terrace); PF-V3 §3 (no hall-kitchen door; mudroom 8 doors); K-318, K-330 | — | $ to $$ (one added door and a hall connection; unknown) |
| ARC-02 | Should fix | V3 | V3 room 3 (living, 571.46 ft²) | The living room has no window-type opening and no exterior wall: its walls are the hall, the kitchen, the dining room and the garage. K-064 (windows on 2 walls) is CONTRADICTED and K-007 (daylight where needed) is CONTRADICTED. It is also the through-room for the shortest front door -> kitchen route (43 ft through the vestibule, hall and living 3) and the primary -> kitchen route (68 ft), so the main sitting room is a corridor. The garage is on its west wall (noise, K-008 for a quiet living room). | PF-V3 §3 (no hall-kitchen door), §4 (living: none), §10 (R3 43 ft through living 3; R7 68 ft), §11 (garage on living room's west wall) | — | $$ (needs relocating or re-opening a wall) |
| ARC-03 | Should fix | V2, V3, ALT | V2 room 13 (pantry, 132.83 ft²); V3 room 13 (117.87 ft²); ALT room 21 (85.47 ft²) | The "Costco door" is lost. In V2 and V3 the pantry shares the garage wall but has no door to it (K-037, K-115, K-315 MISSING); the garage door leads to room 7 / mudroom 8, then a second 36-42 in door to the pantry. In ALT the pantry does not touch the garage at all (mudroom and utility lie between, garage to pantry 32 ft through three rooms). V1-2 has the door: 36 in garage -> pantry, 36 in double -> kitchen, about 13 ft. | PF-V12 §7; PF-V2 §7, §11; PF-V3 §7, §11; PF-ALT §7, §10 (R2 32 ft) | — | $ (one door, V2/V3); redesign for ALT |
| ARC-04 | Should fix | V1-2, V2, V3 | Master suite: V1-2 rooms 17 and 20; V2 rooms 16 and 19; V3 rooms 15 and 18 (walk-in closets, 72.01 and 63.94 ft²) | Both walk-in closets open off the vanity zone (V1-2 room 19) only; there is no door from the master bedroom. This is the specific layout Kayla names as a dislike (K-333, K-201, K-304 CONTRADICTED; K-202 CONTRADICTED because bath is the only way). Read from p.1 door positions; the PFs mark this "inferred". Confirm on the p.1 tile before acting. ALT has both WICs off the bedroom. | PF-V12 §11 (chain 29.2+36.0+30.8, 36.0+36.0+35.9); PF-V2 §11; PF-V3 §11; PF-ALT §11 | — | $$ |
| ARC-05 | Should fix | V1-2, V2, V3, ALT | Master wing closets | Closets sit on exterior walls (K-331, K-070, K-071 all CONTRADICTED): V1-2 closets 17, 20; V2 16, 19 + room 8 wardrobes; V3 15, 18 + room 7 wardrobes; ALT WIC 23 (north wall) and Closet 29 (east wall). Kayla wants none. The same four sets also draw tubs on exterior walls in ALT (K-074 CONTRADICTED: master, Bath 2 west wall; Bath 3 east wall). V1-2/V2/V3 tub is interior (IN). | PF-V12 §11; PF-V2 §11; PF-V3 §11; PF-ALT §11 | — | $ to $$ |
| ARC-06 | Should fix | ALT | ALT rooms 2, 3, 7, 14 versus room 25 | No bathroom on the kitchen/living side. The only half bath is the Powder Room 25 off hall 16 at the west end of the main block: about 36 ft from the kitchen threshold, about 76 ft from the living-room centre, 28 ft from the front door. K-033 (bath from every living zone) CONTRADICTED. No toilet near the garage/mudroom either (K-157 MISSING). | PF-ALT §10 (R4 28 ft), §11 (36 ft, 76 ft) | — | $$ (plumbing group beside the kitchen/mudroom) |
| ARC-07 | Should fix | ALT | ALT room 7 (dining, 240.14 ft²), room 14 (breakfast, 143.91 ft²) | Both rooms have no window-type opening (K-007 CONTRADICTED); daylight reaches them only through 60 in sliding panel runs from Hall 10 on the north and from the kitchen on the south. Dining has 8 chairs at 96 x 42 in (K-128 IN) but no exterior access (K-127 MISSING, K-129 MISSING). The sunroom, library and office each have a window or glazed doors, so the windowless rooms are the ones used every day. | PF-ALT §4 (rooms with no window-type opening), §7 (dining openings 60.0 N, 60.0 S, 36.0 E) | — | $$ |
| ARC-08 | Should fix | V2, V3 | V2 room 8 (186.11 ft²), V3 room 7 (223.14 ft²) | The sunroom of V1-2 (147.04 ft², glazed on three sides, K-034/K-185/K-186/K-188 IN for V1-2) is gone: the same position is now an unnamed room with wardrobes, a dresser, armchairs and a window bench (PF reads it as a dressing/sitting room). K-034 (bug-free sit-out) MISSING; K-185, K-186, K-188 MISSING; K-189 (dining set for 4) MISSING in all four plans (V1-2 has only a 2-seat bistro table, ALT none). Screened porch not shown in any set. | PF-V2 §2, §8; PF-V3 §2, §8; PF-V12 §8 (sofa 68.1, bistro); PF-ALT §8 | — | unknown |
| ARC-09 | Consider | All | All hall doors and halls | Kayla asks for wide doors and halls (K-003, K-060, K-061, all MISSING). Doors: V1-2/V2/V3 narrowest 31.5 in x about 4 (bath sub-room, toilet room 27/26) with 36 in as the common door; ALT 31.5 in x 2 (powder room, WIC 23) plus Bedroom 2 door printed 34.4 in on alt p.28 and 36.0 on p.26. Halls: corridor about 48 in measured (+/- 6) in V1-2/V2/V3; ALT Hall 16 47.9 in and Hall 10 48.1 in printed. All pass the code floors (860 mm = 33.9 in hall; 610 mm = 24 in bath door), so this is a household requirement, not a code issue. A 36 in door is only 3 in more than the 31.5 in ones; none of the sheets draws a 42 in clear door except the ALT utility/hall 10 doors. | PF-V12 §3, §5; PF-V2 §3; PF-V3 §3; PF-ALT §3, §5; K-003, K-060, K-061 | abc_2023 PDF p.841 9.5.4.1.(1); PDF p.842 9.5.5.1.(1) and Table 9.5.5.1.; 9.5.5.3.(1) | $ |
| ARC-10 | Consider | V1-2 | V1-2 room 4 (hall, 379.54 ft²) | Hall is 10.1% of net heated interior (379.54 / 3763.34), vestibule + hall 11.1%: the largest of the four, and the one that triggers K-316/K-317 (CONTRADICTED). It also has five openings on its south wall (two 48 in kitchen doors, 60 in living, 36 in mudroom, 60 in vestibule) and the laundry's 48 in double door opens straight onto it (K-105 CONTRADICTED: laundry visible from the hall). | PF-V12 §3, §5; PF-COMPARE §3 | — | $ |
| ARC-11 | Consider | V1-2, V2, V3, ALT | Hall % (all) | Circulation compared: V1-2 10.1%, V2 9.0% (9.2% excl. room 15), V3 8.9%, ALT halls 7.6% (367.59 / 4825.80) but foyer + halls 15.5% because the 380.29 ft² foyer includes the stair well. Rule used in the table: <= 8% IN, 8-10% MISSING, > 10% CONTRADICTED; ALT is IN on halls alone and MISSING if the foyer is counted. | PF-COMPARE §3 | — | $ |
| ARC-12 | Consider | V1-2, V2, V3 | Kitchen/dining treatment (see 3b below) | Each version trades openness for walls differently; see the kitchen table in §3b. In one line: V1-2 keeps kitchen and dining in one 616.78 ft² room (open, 3 doors through it); V2 splits it into walled kitchen+nook, scullery, dining and living with 48 in doubles; V3 pushes kitchen, mudroom and pantry behind living and dining so the kitchen is off the hall. | PF-V12 §7; PF-V2 §7; PF-V3 §7 | — | unknown |
| ARC-13 | Consider | V2 | V2 room 6 (dining, 284.71 ft²) | Dining is enclosed (242.0 x 169.4 in) and reached only from the kitchen nook by a 48 in double door; the living room and dining share a glazed wall (three H=82.0 ws=36.0 units) that you can see through but not pass. Dining -> living walks 35 ft back through the kitchen (R11). K-035 (direct kitchen-dining) IN; K-062 (broken open) IN. | PF-V2 §3, §7, §10 | — | $ |
| ARC-14 | Consider | V2 | V2 room 15 (78.04 ft², inside garage walls) | A toilet, small sink and a machine-like symbol sit in a room entered only from the garage by a 36 in door. Heated status is not printed (PF counts the area both ways: 4204.55 vs 4126.51 ft² net heated). It is a garage washroom, not a mudroom bath (that is room 27, 21.21 ft², off room 7, K-157 IN). | PF-V2 §1, §2, §6 | — | unknown |
| ARC-15 | Consider | V1-2, V2, V3 | Master wing windows | The master bedroom has a 48 in window pair on its east wall and another on its west wall, directly across each other (K-077 CONTRADICTED); ALT's wing windows are not on one axis (IN). No sheet draws the windows on a diagonal (K-078 MISSING). The same master has windows in the corners flanking 205.9 in of solid top wall, which helps bed placement (K-080/K-307 partly met; scored MISSING because other rooms were not read). | PF-V12 §4; PF-V2 §4; PF-V3 §4; PF-ALT §4 | — | $ |
| ARC-16 | Consider | V1-2, V2, V3 | Hall bedrooms 7/9 and 12; laundry | Both secondary bedroom doors (36 in) and the laundry 48 in double are on the public hall (K-104, K-105 CONTRADICTED: public hall sight line into a bedroom door and into the laundry). ALT puts bedrooms and laundry on the private hall 16 (K-105 IN) but hall 16 ends at the master double door 47.9 in and the foyer opens into it by a 39.9 in passage (K-104 MISSING). | PF-V12 §3 (p.14 wall 8); PF-ALT §3 rows 27, 32-36 | — | $ |
| ARC-17 | Consider | ALT | ALT rooms 17, 18, 20 (Bedroom 3, Bedroom 2, Bathroom 2) | Bedroom 3 has an ensuite (36 in door to Bath 2) and Bedroom 4 an ensuite to Bath 3 (K-239 IN for ALT); Bedroom 2 has no bath door and reaches Bath 2 through Bedroom 3 (18 ft, passing a bedroom) or Powder Room 25 (20 ft). K-179 (a full bath not through a bedroom) MISSING because Bath 2 and Bath 3 are entered only from bedrooms; the powder room draws a tub/shower-type fixture (PF-ALT §6), which would be the only non-bedroom bath if that is intended. | PF-ALT §3 rows 34-44, §6, §10 | — | $ |
| ARC-18 | Consider | ALT | ALT room 5 (Master Bedroom, 300.64 ft²) | Master bedroom has five door openings (hall double 47.9, laundry 36, WIC 31.5, WIC 36, bath 36) in a 300.64 ft² room with a bed labelled about 82.0 x 86.0 in and 19.7 in nightstands. Wall space for the bed and clear walking space around it (K-053, K-195) is not demonstrated; I score both IN for ALT only because the bed fits; confirm the swing arcs. V1-2/V2/V3 master is 458.12 ft² with a 76.0 x 84.0 in bed. | PF-ALT §3, §8; PF-V12 §8 | — | $ |
| ARC-19 | Consider | V1-2, V2, V3 | Lounge / sitting spaces | V1-2 room 14 (113.67 ft², armchairs, small sofa) sits beside the master as a lounge; no designated small bedroom/nursery exists in any plan (K-245 MISSING). Bedroom count 3 in V1-2/V2/V3 vs 4 in ALT (K-242). Only ALT draws a library (K-032) and a guest ensuite (K-239). No plan draws a craft/flex room (K-237), a Jack-and-Jill bath (K-244), a coffee bar with pot filler (K-117), or a dog bath/cat litter area (K-170, K-172). | PF-COMPARE §9, §10 | — | unknown |
| ARC-20 | Consider | All | Front entry and garage entry | No sheet labels a mail/command centre, key/purse drop, or shoe bench at the front entry (K-043, K-044, K-140, K-143 MISSING; K-047 MISSING). V2's room 7 has hooks, a 72 in bench and shoe/coat units at the garage entry (K-146, K-147, K-149, K-151 IN for V2); V3 mudroom 8 "cabinets, coat units" (unspecific, MISSING). A hall slat screen (49.3 + 7.0 + 49.3 in) in V1-2/V2/V3 is a screen, not hidden storage (K-142 MISSING). ALT has no vestibule (K-041 MISSING); its 60 in double front door opens straight into the 380.29 ft² foyer. | PF-V2 §8; PF-V3 §2, §5; PF-ALT §5 | — | $ |
| ARC-21 | Consider | ALT | ALT room 3 (kitchen, 395.36 ft²), living room 2 | Kitchen to living is a single 36 in door; island (120.0 x 60.0 in) cannot face the living area (K-123 CONTRADICTED vs V1-2 IN). Kitchen has doors to utility, pantry, living and two 60 in openings, so it is a through route between utility (west) and living (east) and between dining/breakfast and the pantry (K-318 MISSING). Front door -> kitchen is 44-46 ft and passes the breakfast room or utility. No seat in the kitchen (K-021 MISSING; the breakfast room is 8 ft away behind a sliding panel). | PF-ALT §3 rows 10-14, §7, §10 | — | $ |
| ARC-22 | Consider | V3 | V3 room 2 island aisles | Three red clearance numbers are printed near the island: 36.8 in, 49.5 in and 56.6 in; the sheet does not say which gap each spans, so K-274 (54 in beside the dishwasher; dishwasher not labelled) is MISSING in all four. 36.8 in is below Kayla's 54 in if it is the dishwasher aisle. V2 about 4-5 ft west and 7-8 ft north, V1-2 about 8 ft, ALT about 6.5 ft (measured, +/- 1-1.5 ft). | PF-V3 §7, §12; PF-V2 §7; PF-ALT §7 | — | $ |
| ARC-23 | Consider | V2, V3, ALT | Wet-wall spread (K-006) | Largest gap between plumbing groups: V1-2 about 30 ft (hall bath to master wet group), V2 about 40, V3 about 55 (kitchen to laundry), ALT 80+ ft (kitchen to Master Bathroom). V1-2 scores IN, the other three MISSING. Plumbing/structural cost is for the plumbing and structural reviewers. | PF-COMPARE §7 | — | $$ |
| ARC-24 | Consider | V1-2, V2, V3 | Unnamed small rooms | Dead space: V1-2/V2/V3 room 25/24/23 (38.86 ft², 116.5 x 48.0 in, a passage/linen zone with no fixture) and room 28/28/27 (19.38 ft², 58.0 x 48.0 in, three openings) are circulation; room 32 (6.89 ft², 47.8 x 20.8 in, 42.1 in slider) is a tiny closet, room 31 (13.35 ft²) a closet; room 30 is the bedroom closet (15.18 ft²). The 59.31 ft² label inside room 20 is a second area label, not a room. ALT: Closets 28 (10.98) and 29 (10.76) are open niches with no door label; Closet 29 has no elevation sheet. | PF-V12 §2, §3; PF-ALT §2, §3 | — | $ |
| ARC-25 | Consider | V1-2, V2, V3 | Stair / basement | V1-2/V2/V3 print "Open to Basement" (0.22 ft²) and a 53.8 in stair with a 45.21 / 44.24 ft² Future Elevator/Closet entered from the hall by a 46.0 / 42.7 in opening (K-002, K-058 IN). ALT draws the stair at the foyer's west end (59.9 in wide) inside the Foyer's 380.29 ft² with no label, and its 34.12 ft² Elevator Closet is entered only from the Utility, not from the foyer or hall (K-058 IN, but not on a main circulation route). | PF-V12 §9; PF-ALT §9 | — | unknown |

## 3. Extra tables

### 3a. Circulation: route x plan (ft; rooms passed through) from PF §10, +/- 2-3 ft

| Route | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Garage door -> kitchen (shortest) | 13; pantry | 18 to nook edge; room 7 | 13; mudroom 8 | 19; mudroom, utility |
| Garage door -> kitchen (second route) | 30; mudroom, hall | 26; room 7, room 13 | 22; mudroom 8, pantry 13 | not given |
| Garage door -> pantry | 3-7; none | 13; room 7 | 13; mudroom 8 | 32; mudroom, utility, kitchen |
| Front door -> kitchen | 29; vestibule, hall | 25 to door; vestibule, hall | 43; vestibule, hall, living 3 | 44; foyer, hall 10, breakfast room (or 46 via utility) |
| Front door -> powder room | 24; vestibule, hall | 22-24; vestibule, hall | 22-24; vestibule, hall | 28; foyer, hall 16 |
| Front door -> primary bedroom door | 85; vestibule, hall, laundry, 2 master rooms | 85; same | 85; same | 56; foyer, hall 16 |
| Primary bedroom -> laundry | 20; 2 rooms | 20; 2 rooms | 20; 2 rooms | 6; none |
| Primary bedroom -> kitchen | 105 (not re-derived, PF-V2 §10 note); laundry, hall | 60; laundry, hall | 68; laundry, hall, living 3 | 82; hall 16, foyer, hall 10, utility |
| Bedroom -> nearest bath | 18-20; hall | 18-20; hall | 18-20; hall | 5-6 (ensuite) or 18-20 via hall 16 (Bedroom 2) |
| Kitchen -> dining | 10; none | 25; none | 20; none | 8; none |
| Dining -> living | 25; none | 35; kitchen | 24; none | 10 to door; none |
| Living -> sunroom (V2/V3: former sunroom position) | 22; hall | 60; hall | 59; hall | 24; hall 10 |
| Sum of primary lengths (PF-COMPARE §6c) | 374-378 | 401-403 | 405-407 | 334 |
| Routes naming a living, kitchen or dining room as passed-through | 0 | 1 (R11) | 2 (R3, R7) | 1 kitchen (R2) + master bedroom (R7) |

### 3b. Kitchen / dining treatment

| Item | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Open vs walled | Kitchen 314.63 + dining 201.07 + 99.24 = one 614.94 ft² open room (616.78 on p.1); living is walled with a 48 in opening | Kitchen + nook 636.15 ft² open L; pantry/scullery, dining 284.71, living 468.77, entry 219.69 all walled | Kitchen + table 625.28 ft²; living 571.46, dining 354.03, mudroom 179.22, pantry 117.87 walled | Kitchen 395.36, breakfast 143.91, dining 240.14, pantry 85.47 walled; three 60 in sliding openings on the kitchen north wall |
| Kitchen <-> dining (K-035) | same room | 48 in double, direct | 48 in double, direct | 60 in sliding opening, direct |
| Through-route (K-318, K-330) | yes (pantry W, hall N x2, living E) | yes (hall N, living E, dining SE, entry S, scullery) and the only way from the garage to the hall | yes (pantry/mudroom W, 2 x 48 N, slider E) and the only way from the garage to the hall | yes (utility W <-> living E; pantry) but hall 10 gives an alternative |
| Island, aisles (K-106, K-274) | 120.0 x 60.0, about 8 ft to range wall | 120.0 x 60.0; about 4-5 ft W, 7-8 ft N | 120.0 x 60.0; red 36.8 / 49.5 / 56.6 in unlabelled | 120.0 x 60.0; about 6.5 ft S, 8 ft E |
| Sink under window (K-124) | S wall | W wall under three 36 in windows | S wall under 144.4 in window | S wall under two windows |
| Gives up | daylight and sight lines: none; area: no breakfast nook; living across a 48 in opening | hall-to-dining door; sunroom (K-034); dining<->living passage | hall-to-kitchen door; living window and exterior wall (571 ft², no window); sunroom; garage on the living wall | island facing living (K-123); kitchen seating; no windows in dining or breakfast; kitchen on the foyer axis |

### 3c. Furniture fit (stated assumption: king 76 x 80 in)

| Item | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Master bed drawn | 76.0 x 84.0 (king) in 458.12 ft² | same | same | about 82.0 x 86.0 in labels in 300.64 ft² |
| Secondary beds | 63.0 x 84.0 (144.1 in wide room); about 59.4 x 79.9 queen (151.0 in room) | same | same | 63.0 x 78.7 (Bed 2, 3); 59.4 x 79.9 (Bed 4) |
| Dining seats | 72.0 dia + 8 chairs | 96.0 x 42.0 + 8 | 72.0 dia + 8 | 96.0 x 42.0 + 8 |
| Sectional + chairs (K-132) | 122.5 in sectional + 2 armchairs, coffee 60 x 36 | 72 in run + 2 armchairs | 66.9 in run + 3 armchairs | L-shaped 84.0 + modules, 2 armchairs |
| Sunroom furniture (K-188/189) | sofa 68.1, 2-seat bistro | no sunroom | no sunroom | 2 sofas, armchair; no dining set |
| Closet depths | bedroom closet 84.0 x 26.0 in; master WIC 96 x 108 and 96 x 96 | same | same | WIC 86.2 x 89.3 and 85.2 x 89.3; Closet 28 60.4 x 26.2 |

### 3d. Windows (K-064, K-077, K-080, K-306)

| Item | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Living spaces with windows on 2+ walls | living bay (2-3 walls); kitchen/dining 1 | living 2; dining 2; kitchen 1 | dining 2; living none; kitchen 1 | living 2; foyer 2; kitchen 1; dining/breakfast none |
| Window behind bed (K-306) | Bedroom 12 east window ws 36 may sit behind a headboard (not confirmed) | same | same | not resolved (widths not printed, PF-ALT §4) |

## 4. Cross-plan comparison (facts used; no recommendation)

| Measure | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Net heated interior (ft², Rooms sheet sum minus garage) | 3763.34 | 4204.55 | 4278.07 | 4825.80 |
| Hall % of net heated interior | 10.1% (vestibule + hall 11.1%) | 9.0% (10.0%) | 8.9% (9.8%) | 7.6% halls (foyer + halls 15.5%) |
| Routes total, 12 primary routes (ft) | 374-378 | 401-403 | 405-407 | 334 |
| Routes passing through a living/kitchen/dining room (PF-COMPARE §6c count) | 0 | 1 | 2 | 1 (+ master bedroom) |
| Narrowest door (in) | 31.5 | 31.5 | 31.5 | 31.5 |
| Doors under 36 in | about 4 | about 4 | about 4 | 3 (31.5 x 2, 34.4 x 1) |
| Narrowest printed/measured hall (in) | about 48 meas. | about 48 meas. | about 48-55 meas. | 47.9 printed |
| Bedrooms (printed + inferred master) | 3 | 3 | 3 | 4 |
| Bathrooms, full / half (PF-COMPARE §10) | 2 / 1 powder (+ 2 WC-only rooms) | 2 / 2 (powder + room 27) | 2 / 2 (powder + room 25) | 3 / 1 powder (draws tub/shower-type fixture) |
| Major rooms with windows on 2+ walls | bedrooms 7, 12, office, master, living, vestibule (6) | bedrooms 9, 12, office, master, vestibule, living 3, dining 6, room 8 (8) | bedrooms 9, 12, office, master, vestibule, dining 6, room 7 (7) | master, living, foyer (3) |
| Major rooms (living/kitchen/dining/breakfast/bedroom/office) with no window-type opening | 0 | 0 | 1 (living 3) | 2 (dining, breakfast) |
| Kayla IN / MISSING / CONTRADICTED / N/S (of 164) | 59 / 59 / 14 / 32 | 62 / 56 / 14 / 32 | 55 / 62 / 15 / 32 | 57 / 68 / 7 / 32 |
| Deal-breaker groups IN (of 12; group 11 N/S in all) | 7 | 6 | 6 | 7 |

Derivations: "major rooms with windows on 2+ walls" counted from the per-room lines of PF-V12 §4, PF-V2 §4, PF-V3 §4, PF-ALT §4; windows are not dimensioned, so counts are by wall, not area. Routes from PF-COMPARE §6c.

## 5. plan_facts corrections

- PF-COMPARE §6c counts V1-2 "routes through a living/kitchen/dining room" as 0 because the rooms named in R5/R7 are the master vanity zone and dressing area, not a kitchen. Not wrong; note the V1-2 R7 value 105 ft is not re-derived (PF-V2 §10 says so), so the 374-378 total mixes derivations.
- PF-V12 §3 lists the hall -> living opening as "60.0 double" but also "Kitchen/dining <-> living 48.0 sliding/pocket pair" (p.1). V1-2 therefore has two living-room entries; I used both in K-062 and K-332.
- No number in the PF files was found wrong on pages I opened (Rooms sheets v12 p.3, v2 p.3, v3 p.3, alt p.2 match room numbers, areas, and relative positions quoted).
- Not done: I did not open the Furniture sheets (p.4 / alt p.3) at 300 dpi; furniture fit is from the PF §8 text. Door swings were not extracted by the PF files, so "doors opening against fixtures" (brief §2) is not assessed.

## 6. Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| ARC-09 | `search.py --doc abc_2023 '"9.5.4.1"'` | abc_2023 | 841 | 9.5.4.1.(1) | The unobstructed width of a hallway within a dwelling unit shall be not less than 860 mm |
| ARC-09 | `search.py --doc abc_2023 '"9.5.5.1"'` | abc_2023 | 842 | 9.5.5.1.(1) | doorway openings within dwelling units and within houses with a secondary suite including their common spaces |
| ARC-09 | `search.py --doc abc_2023 '"9.5.5.1"'` | abc_2023 | 842 | Table 9.5.5.1. | Bathroom, water-closet room, shower room (1) 610 1 980 |
| ARC-09 | `search.py --doc abc_2023 '"9.5.5.2"'` | abc_2023 | 842 | 9.5.5.3.(1) | This Article applies where a hallway of not less than 860 mm wide serves one or more rooms containing a bathtub, shower or water closet. |
