# Option C: Clean sheet inside the same envelope

Files: `main_floor_c.scad`, `basement_c.scad`, `plan_c.png` (decision plan), `3d_c.png`, `stair_c.scad` + `stair_c.png`, `basement_plan_c.png`, `matrix_c.md`, `plan_facts_c.md`, `check_layout.txt` (both files print OK).

## 1. Matrix numbers

| Row | Option C | Current model |
|---|---|---|
| Kayla PLAN items IN / MISSING / CONTRADICTED (of 164) | 120 / 44 / 0 (designer's own scoring, section 5) | 62 / 89 / 13 |
| Deal-breakers met (of 12 in ARC's list) | 12 (two carry a condition: K-005/K-335 needs the south drive, K-055 needs the engineer's recessed floor) | 5 |
| Review Blockers fixed / open (of 6) | 2 fixed (CODE-01, STR-04) / 4 open (STR-01, STR-02, STR-03, PLB-01) | 0 / 6 |
| Circulation % (strict / with foyer) | 8.7% / 10.2% (474 sf of 5,444) | 16.2% / 21.9% |
| Drain-run index (ft), wet-wall groups (main), groups stacked over the basement | 951 ft (alt exit 846); 12; 1 of 12 | 879 ft; 14; 1 of 14 |
| Single doors under 32 in / 32-35 in / 36 in+; minimum hall clear width | 0 / 0 / 30; 4.60 ft (raw 4.22 ft at the stair-top landing) | 7 / 11 / 4; 3.71 ft |
| No-threshold shower | Y (drawn flush, 0.02 ft; recessed floor is an engineer item) | N |
| Bedrooms sharing a wall with the living/great room | 0 | 0 |
| A bedroom next to the foyer | N | N |
| Master bed to laundry path | 24.9 ft (MASTER LAUNDRY, through the WIC) | 103.1 ft |
| Master suite's side | north (y 42-63.42), north-east block (x 72-108) | north-east block (x 95-128) |
| Bedrooms with east light | 2 of 3 (master E+N, bedroom 2 E); bedroom 3 faces N | 1 |
| Living spaces facing south | 2 (LIVING ROOM 16 ft, SUN ROOM 14 ft of south wall) | 1 (DEN) |
| Living spaces with windows on 2+ walls | 3 rooms in all (SUN ROOM E/S, LIBRARY N/W, MASTER BEDROOM E/N); only 1 is living-kind (SUN ROOM) | 4 rooms (SUN ROOM, MASTER BEDROOM, DEN, BREAKFAST) |
| Building area, outside face (m2) against 600 | 575.3 (24.7 under; centre lines 559.3) | 608.0 |
| Basement/shop/site changes | basement: stair foot only (basement_c.scad, same as Option A). Shop: none. Site: garage door faces south so the west drive is replaced by a south drive (NOT drawn in site.scad); meters must move. Foundation: crawl wings W and E mostly not needed | none |
| Cost vs the current model | $ down (about 97 ft less wall, 4 corners instead of 30, 257 sf less garage; offset by new drive, a second stair run, redesign and re-permit effort) | |

## 2. What it is

The main floor re-planned from Kayla's notes outward, not traced from the current rooms. The heated floor is one 85.8 x 63.4 ft rectangle (x 22.16-108, y 0-63.42) sitting directly on the basement's ICF outline, with the garage (22.16 x 26 ft, one 16 ft door on the SOUTH wall) on its south-west corner. The south band, in order west to east, is: mudroom, pantry (Costco door to the garage), kitchen, dining, vestibule + foyer, living room, sun room (south-east). A north-west quiet zone (den, library, office) is reached by a short gallery that also carries the 5.0 ft stair-top landing. A north-east private wing hangs off hall H1 (north from the foyer) and H4 (east): bedroom 2 with its own bath and an east deck, bedroom 3, a hall bath, and the master suite on the north wall with the WIC, laundry and bath back to back.

Changes vs the current model:
- **Footprint.** Heated 5,444 sf (was 5,486), 4 outside corners and 0 inside (was 17 + 13), 298.5 ft of perimeter (was 395.5). The old 128 ft east end and the west bedroom wing are gone. The garage is 576 sf (was 833).
- **Stair (CODE-01).** 18 risers (3,429 mm) south from the unchanged nosing, a 4.4 ft landing at the basement, a 90-degree turn east and 4 risers (762 mm); same geometry as Option A's tested stair (`basement_c.scad`). The main-floor opening and headroom line are unchanged.
- **Rooms new to the plan:** powder, vestibule, library, den, butler's pantry, master laundry, broom/coat/linen closets, an east deck.
- **Rooms gone:** bunk room, study, flex room, sun room's old position, 2 of the 3 WICs, the 80 ft spine and the 309 sf foyer (now 252 sf + 84 sf vestibule).

## 3. Pros

- **Under the Part 9 line with margin.** 575.3 m2 against 600, 24.7 m2 under (matrix_c.md, same 0.5 ft method as the 608 m2 figure). Fixes STR-04 and exceeds CODE-03's 15 m2 margin ask, with the garage cut 30.8% by area (257 sf) and 8 ft less depth and no heated room trimmed to get there.
- **Every deal-breaker has an answer on the plan** (12 of 12; two conditional, see Cons). Laundry 24.9 ft from the master bed (was 103.1), 28.7 ft from bedroom 2 and 31.5 ft from bedroom 3 (K-036, K-329). Costco door: the pantry shares 13.0 ft with the garage and has a 36 in door (K-037).
- **Circulation roughly halved.** 474 sf strict (8.7%), 10.2% with the foyer, against 891 sf (16.2%) and 21.9% (ARC-07, K-316). The 481 sf spine is gone.
- **Doors and halls.** 30 of 30 single doors are 36 in (was 4 of 22); the narrowest hall is 4.60 ft clear (was 3.71). CODE-02 (stair-landing doors under 810 mm) is gone: the landing is reached through two wall-free openings 4.1 and 4.4 ft wide.
- **Simple envelope.** 4 corners against 30 and 298.5 ft of perimeter against 395.5 (COST-08, K-069); the heated block is a rectangle.
- **No closet on an outside wall.** 0 of 6 closet/WIC rooms touch yard or porch (was 2 of 5): K-070/K-331 IN.
- **Bedrooms are away from noise and the drive.** No bedroom shares a wall with a living-kind room, the foyer, the kitchen or the garage (PF 8.1, 8.2). Bedrooms are 42 ft or more from the old west drive by the tool; with the south drive, the nearest bedroom (bedroom 3) is more than 60 ft from the apron (hand measurement, K-005/K-335, ARC-01).
- **Stair-top landing fits CODE-07 on the main floor.** 4.62 x 5.00 ft against the 4.22 ft stair width; Option A could only reach 3.39 ft.
- **Master laundry gets a wet wall.** Laundry (G10) and master bath (G9) are back to back on y = 52 and x = 72; water heater to the furthest fixture is 87.3 ft (was 119.8).
- **Daylight follows use.** Kitchen, dining, living, sun room, library, office, den and all three bedrooms have windows or glass doors; the foyer, baths, laundry and closets do not. The old windowless STUDY, FLEX and OFFICE are gone (ARC-19, ARC-20).
- **Basement stays whole.** The ICF outline is untouched; the main floor now bears on it (west wall x = 22.16 is the basement wall). The UTILITY room (x 22-37, y 35-43) has the den above it and no wet room, so a vent chase can ride the den's west wall (GAS-01).

## 4. Cons

- **K-005/K-335 depend on a site departure that is not drawn.** `site.scad` still has the west drive, so the tool prints 42.0 ft (not the 60+ ft by hand). The new south drive, apron and road cut are unmodelled; the road side is itself assumed (site.scad:8). The west drive's dead end, snow pile and meters (SITE-03, SITE-04, ELE-05) go away only if the services move: the meters were under old bedroom 2's west window, and now the DEN's west wall (x 22.16, y 26-47) is where they would land. Coordinator: say where they go.
- **The drain run gets longer, not shorter.** Index 951 ft (alt exit 846) against 879 (747): the wet rooms moved east, 55-114 ft from the drain exit at (22.16, 58) (PF 9.5). 12 groups in 5 clusters; only 1 of 12 is within 5 ft of a basement group (4 within 10 ft). K-006 stays MISSING: only the master bath and laundry are back to back (PLB-03, PLB-11 are not fixed).
- **Master suite is smaller.** Master bath 183 sf (was 243), one WIC of 80 sf (was 95 + 94): K-200 is MISSING; no separate WC rooms (K-227), no linen on the bath (K-226), tub drawn raised (K-220).
- **Lost vs the current model.** Jack-and-Jill bath (K-244), a second non-master bedroom with its own study (STUDY/BUNK ROOM) and the great-room-with-deck: living room has windows on 1 wall only (K-064); the sunroom/living glass partition is the only borrowed light. DECK-facing views are gone: the old front-door-to-deck sightline (K-299, K-300) has no replacement, the front door looks up H1 at a blank wall.
- **Windows on 2+ walls: 3 rooms (was 4).** LIVING ROOM and DEN each have one exterior wall.
- **Bedroom 3 is 136 sf (12 x 11.3 ft)** and its north window sits at x 67.4-71, east of the exit areaway (x 45.6-66.8); the OFFICE and LIBRARY windows look at the areaway wall and its 42 in guard (CODE-05 stays open: 1,067 mm against 1,070 mm).
- **No bath off the mudroom, no dog wash, no litter spot** (K-157, K-170, K-172, K-033 for the mudroom entry, about 60 ft from the powder).
- **Kitchen triangle 45 ft** (was 41.4; K-261 against 26), fridge 22 ft from the sink (K-290). The kitchen is 520 sf with no outside wall except the south.
- **Redesign cost.** Everything on the main floor is new: new permit drawings, new engineering. Structural moves to flag for the licensed Alberta engineer: the 16 ft garage door on the south wall (STR-06), the stair opening (unchanged, STR-08), curbless showers (recessed joist bays in two baths), the 14 ft kitchen/dining and 12 ft living/sun room openings, and the gallery over the stair-top (bearing line along y 47.1-52.1 on the basement's x 42.65 stair wall). No main-floor wall is marked bearing (STR-13 stays open).
- **Garage is 22.16 ft wide inside**, 1.1 ft narrower than the old interior and 26 ft deep (was 34.2): two cars, almost no shop space (K-309 to K-314 are SPEC items, not scored).
- **Self-scored.** The 120 / 44 / 0 count is the designer's own re-score of ARC's list; kitchen-zone and sightline items (K-104, K-144, K-262, K-117, K-279) rest on fixture rows and door positions, not on a drawn kitchen layout. Re-run ARC before relying on it.

## 5. Kayla compliance (every item ARC classed PLAN)

| K-ID | Verdict | Evidence | Change vs the current model |
|---|---|---|---|
| K-001 | IN | All essential rooms on one level; basement unchanged | same |
| K-002 | IN | Basement untouched (3,475 sf); stair foot only | same |
| K-003 | IN | 0 single doors under 32 in, 30 at 36 in; vestibule/dining/living doubles 72 in; halls 4.6 ft+ clear | MISSING -> IN |
| K-004 | MISSING | Hall bath 90 sf, powder 42 sf; master bath shrank to 183 sf and has no separate 4.5 ft WC room | same |
| K-005 | IN | Garage door faces south; no drive on the west or past any bedroom (needs the site departure, not drawn in site.scad; tool still reads the west drive: 42 ft) | CONTRADICTED -> IN |
| K-006 | MISSING | 12 groups (was 14) in 5 clusters; only master bath + laundry are back to back; drain-run index 951 ft is worse than 879 | same |
| K-007 | IN | Every kitchen/dining/living/sun/den/library/office/bedroom has a window or glass door; foyer, baths, laundry, closets do not | MISSING -> IN |
| K-008 | IN | Bedrooms touch only halls, baths, closets, library/office; no kitchen/living wall (PF 8.1) | MISSING -> IN |
| K-009 | IN | Public rooms south, private wing reached from the foyer by H1; nobody crosses a bedroom to reach a public room | MISSING -> IN |
| K-010 | MISSING | Garage 22.16 ft, kitchen 20 x 26 on 2 ft module but 22.16, 63.42, 4.62 stair box are not | same |
| K-012 | IN | Kitchen, dining, living, sun room, foyer, porch on y 0; south drive (departure) | MISSING -> IN |
| K-013 | IN | Master bedroom y 42-63.42, north wall | same |
| K-014 | IN | Bedroom 2 and master have east walls with windows; sun room SE; bedroom 3 faces north | MISSING -> IN |
| K-021 | IN | Den opens 6 ft to the kitchen; banquette in the kitchen | same |
| K-023 | IN | Kitchen door (M, x 49) to the 10 ft covered front porch; BBQ at its west end | MISSING -> IN |
| K-030 | IN | Pantry 154 sf (garage side, freezer, shallow shelves) + butler's pantry 164 sf | MISSING -> IN |
| K-031 | IN | OFFICE 196 sf on the north wall, shares walls with library, bedroom 3 and gallery only | same |
| K-032 | IN | LIBRARY 232 sf, N + W windows, shelving on 2 walls | MISSING -> IN |
| K-033 | MISSING | Powder 31 ft from the foyer, ~25 ft from library/office; the mudroom entry is ~60 ft away and has no bath | same |
| K-034 | IN | SUN ROOM 308 sf, S + E glass, double door to the patio | same |
| K-035 | IN | Kitchen/dining open 14 ft, no hall or pantry between | same |
| K-036 | IN | MASTER LAUNDRY through the WIC, 24.9 ft from the bed (was 103.1) | MISSING -> IN |
| K-037 | IN | Pantry shares 13.0 ft with the garage, 1 door (Costco door, 36 in, 3 garage steps) | MISSING -> IN |
| K-038 | IN | BROOM, CLOSET, LINEN, COATS: 4 closets spread over foyer, H1, H4 | MISSING -> IN |
| K-040 | IN | LINEN 54 sf off H4, between bedrooms 2/3 and the hall bath | MISSING -> IN |
| K-041 | IN | VESTIBULE 84 sf, double inner doors | MISSING -> IN |
| K-043 | IN | Foyer and vestibule drop shelves (fixture rows at x 76.4) | MISSING -> IN |
| K-044 | IN | Same drop shelves | MISSING -> IN |
| K-047 | IN | Foyer bench, mudroom bench + lockers | same |
| K-053 | IN | Master bed on the south wall, 20 x 21 ft room, 3+ ft each side | same |
| K-055 | IN | Showers drawn flush (0.02 ft) in master bath and bath 2; recessed floor is an engineer item | MISSING -> IN |
| K-058 | MISSING | STORAGE 148 sf is a candidate, but the basement below it is a bath; no shaft reserved | same |
| K-059 | MISSING | No dumbwaiter shaft | same |
| K-060 | IN | Halls 5-6 ft (4.6 ft min clear); H1 5.6 ft | MISSING -> IN |
| K-061 | IN | Same as K-003 | MISSING -> IN |
| K-062 | IN | 11 full openings (4-14 ft) and 5 doubles between zones; no open concept | same |
| K-064 | MISSING | Windows on 2 walls: sun room, library, master only; living room has one wall of glass | same |
| K-069 | IN | Heated union has 4 outside corners, 0 inside (was 17 + 13); perimeter 298.5 ft (was 395.5) | MISSING -> IN |
| K-070 | IN | 0 of 6 closets/WICs touch an outside wall (PF 8.3) | CONTRADICTED -> IN |
| K-071 | IN | Same; no WIC on an exterior wall | MISSING -> IN |
| K-072 | MISSING | Not designed for: hall bath toilet is not between the shower and the door | IN -> MISSING |
| K-074 | IN | Master tub on the x=72 interior wall; bath 2 has a shower only | CONTRADICTED -> IN |
| K-075 | IN | Private wing NE, quiet zone NW, living S: no wing is split by the great room | CONTRADICTED -> IN |
| K-077 | IN | No room has windows on opposite walls | same |
| K-078 | MISSING | Not designed for cross-breeze diagonals | same |
| K-080 | MISSING | Not designed for; sun room windows are centred on the wall | same |
| K-081 | MISSING | Den 6 ft and library 5 ft west windows have no overhang | same |
| K-083 | MISSING | Living 1.75, dining 2.17, master 1.07: mostly outside 1.4-1.6 | same |
| K-095 | IN | Front porch 10 ft (3.0 m), patio 12 ft (3.7 m): inside the 4-5 m limit | MISSING -> IN |
| K-096 | MISSING | Range and sink-island runs OK, but the sink run is on the south (outside) wall for K-124 | CONTRADICTED -> MISSING |
| K-099 | IN | Kitchen, dining, living and sun room all south | MISSING -> IN |
| K-100 | IN | Master (E+N) and bedroom 2 (E) get morning light; bedroom 3 north | MISSING -> IN |
| K-102 | MISSING | Hall bath and powder toilets are visible from their doors | same |
| K-103 | MISSING | Master bed sees the bath door (M, x 88, y 55) | same |
| K-104 | IN | No straight line from foyer, living or dining to a bedroom door; H4 is off H1's axis | CONTRADICTED -> IN |
| K-105 | IN | Laundry door is on H4, behind H1 | MISSING -> IN |
| K-106 | IN | Island 10 x 5.5 ft, no stools | same |
| K-107 | IN | Banquette + table in the kitchen | same |
| K-108 | IN | Island has no sink or cooktop (sink under the south window) | CONTRADICTED -> IN |
| K-114 | IN | Butler's pantry 164 sf off the kitchen | same |
| K-115 | IN | Same as K-037 | MISSING -> IN |
| K-116 | IN | Mudroom door to the kitchen 3 ft; garage to kitchen 35 ft | MISSING -> IN |
| K-117 | IN | North counter run beside the banquette (coffee bar spot) | MISSING -> IN |
| K-123 | MISSING | Island faces the dining table; den opening is only 6 ft | same |
| K-124 | IN | Sink x 40-43 under the window x 38.5-45.5 | same |
| K-127 | IN | Dining double door (6 ft) to the covered porch | MISSING -> IN |
| K-128 | IN | Dining table 6 x 10 ft, 4+ ft clear | same |
| K-129 | MISSING | Doors are 6 ft doubles, no multi-panel wall | same |
| K-132 | IN | Living room 448 sf holds the sectional and chairs | same |
| K-133 | IN | Living room opens 12 ft to the sun room and has a double door to the porch | same |
| K-134 | MISSING | Same as K-129 | same |
| K-140 | IN | Foyer bench | same |
| K-141 | IN | COATS closet 42 sf + foyer closed storage (7 ft) | MISSING -> IN |
| K-142 | IN | Same, closed | MISSING -> IN |
| K-143 | IN | Foyer and vestibule drop shelves | MISSING -> IN |
| K-144 | IN | Front door axis runs north up H1; dining and living are seen sideways through 8 and 10 ft openings | CONTRADICTED -> IN |
| K-145 | IN | Powder 31 ft from the foyer, off H1 (was 65.8 ft) | MISSING -> IN |
| K-146 | IN | Mudroom bench 4.2 ft + lockers | same |
| K-147 | IN | Lockers and a shelf wall in the mudroom | same |
| K-149 | IN | Lockers 7 ft high (x 22.5-24.1) | same |
| K-151 | IN | Mudroom bench 3 ft high near the garage door | same |
| K-153 | IN | Foyer mail shelf | MISSING -> IN |
| K-155 | IN | Mudroom door to the mud stoop (covered, 71 sf) | MISSING -> IN |
| K-156 | IN | Garage door into the mudroom | same |
| K-157 | MISSING | No bath off the mudroom | same |
| K-158 | IN | See K-036 | MISSING -> IN |
| K-163 | IN | Laundry sink in the master laundry | same |
| K-166 | MISSING | Closet-to-laundry door, no pass-through basket | same |
| K-170 | MISSING | No dog wash near the mudroom | same |
| K-172 | MISSING | No litter area | same |
| K-179 | IN | BATH off H4, not through a bedroom | same |
| K-183 | MISSING | OFFICE has no porch | IN -> MISSING |
| K-185 | MISSING | Sun room: about 68% glass on S and E, not full walls | same |
| K-186 | IN | Sun room double door to the patio | same |
| K-188 | IN | Sun room 308 sf, two sofa boxes | same |
| K-189 | IN | Table 6 x 5 ft with clear space | MISSING -> IN |
| K-191 | IN | Master double door to MASTER PORCH 120 sf | same |
| K-192 | IN | No fireplace in the master | same |
| K-195 | IN | Master 428 sf, bed 3+ ft from every wall | same |
| K-200 | MISSING | One WIC (80 sf); the second WIC was given up to the laundry | IN -> MISSING |
| K-201 | IN | WIC opens to the bedroom (M, x 88) as well as the bath | same |
| K-202 | IN | Same | same |
| K-203 | IN | WIC to laundry door | MISSING -> IN |
| K-210 | IN | Master laundry beside the WIC | MISSING -> IN |
| K-211 | IN | Shower 6 x 5 ft, flush | MISSING -> IN |
| K-220 | MISSING | Tub is a 2 ft raised box, not sunken | same |
| K-224 | IN | Double vanity 6.8 ft | same |
| K-226 | MISSING | No linen room off the master bath | IN -> MISSING |
| K-227 | MISSING | One open WC, no separate rooms | same |
| K-228 | IN | Bath to WIC to laundry | MISSING -> IN |
| K-229 | IN | WIC door to the bath | same |
| K-237 | MISSING | No flex room; the library/den can take a daybed | same |
| K-238 | IN | Bedroom 2 14 x 14 ft, queen fits | same |
| K-239 | IN | BATH 2 is bedroom 2's ensuite | same |
| K-240 | IN | Bedroom 2 door to the east deck | MISSING -> IN |
| K-242 | MISSING | Two non-master bedrooms (BEDROOM 2, BEDROOM 3); no fourth | same |
| K-244 | MISSING | BATH 2 serves bedroom 2 only (lost vs the current model) | IN -> MISSING |
| K-245 | MISSING | Bedroom 3 is 40 ft of walk from the master | same |
| K-248 | IN | FRONT PORCH 740 sf, covered | same |
| K-249 | IN | Mud stoop 71 sf under a roof block | MISSING -> IN |
| K-252 | IN | Front porch 10 ft deep, patio 264 sf | same |
| K-253 | IN | Patio + deck adjoin | same |
| K-254 | IN | East deck 220 sf is left unroofed | MISSING -> IN |
| K-255 | IN | Front porch and deck | same |
| K-256 | IN | Range run 8 ft either side; sink run 3 ft each side | same |
| K-257 | MISSING | Fridge to the nearest counter is a 1.1 ft gap; no designed landing | same |
| K-261 | MISSING | Sink-range 10.5, range-fridge 12.3, fridge-sink 22: 45 ft (was 41.4) | same |
| K-262 | IN | The kitchen is seen sideways through the dining opening | same |
| K-270 | MISSING | Fridge to sink 22 ft | same |
| K-273 | MISSING | Not designed for | same |
| K-274 | IN | Island to the sink run 7.6 ft, to the north run 7.9 ft; dishwasher drawn | MISSING -> IN |
| K-277 | IN | Sink under the south window | same |
| K-279 | IN | Pantry door 6 ft from the island | same |
| K-281 | IN | Island 55 sf empty | same |
| K-282 | MISSING | Island centre 10 ft from the range, 13 ft from the fridge | same |
| K-283 | IN | Range has 2.5 ft counter each side | same |
| K-288 | IN | Dishwasher beside the sink | MISSING -> IN |
| K-290 | MISSING | Fridge 22 ft from the sink, 12 ft from the range | same |
| K-292 | MISSING | Fridge run is broken by the pantry door | CONTRADICTED -> MISSING |
| K-297 | MISSING | Foyer has no window row; sidelights 2 ft | same |
| K-298 | IN | Powder door is on H1, not the entry | MISSING -> IN |
| K-299 | MISSING | Front door axis ends at the gallery wall; no window or glass door placed on it | IN -> MISSING |
| K-300 | MISSING | Same | IN -> MISSING |
| K-302 | MISSING | Office has no bath | same |
| K-304 | IN | Closet opens to the bedroom | same |
| K-306 | IN | All three beds on walls with no window behind | CONTRADICTED -> IN |
| K-307 | MISSING | Bedroom 2 east windows are 29-33.5 and 33.8-36.8: not pulled to a corner | same |
| K-315 | IN | Same as K-037 | MISSING -> IN |
| K-316 | IN | Halls 474 sf = 8.7% of 5,444 (was 16.2%); 10.2% with the foyer | CONTRADICTED -> IN |
| K-317 | IN | Rooms open on 5-6 ft halls or on each other | MISSING -> IN |
| K-318 | IN | Garage to the den through the pantry skips the kitchen | same |
| K-320 | IN | Foyer, mudroom, Costco door pantry | MISSING -> IN |
| K-323 | IN | Living room north wall is 16 ft solid | MISSING -> IN |
| K-324 | IN | Zones separated | same |
| K-325 | IN | No bedroom touches the kitchen, living, or garage | MISSING -> IN |
| K-326 | IN | Baths and closets sit on the bedroom walls | MISSING -> IN |
| K-328 | IN | No bedroom touches the foyer | same |
| K-329 | IN | Laundry 24.9 ft from the master, 28.7 from bedroom 2, 31.5 from bedroom 3 | MISSING -> IN |
| K-330 | IN | Bypass: garage > pantry > den > gallery > H1 skips the kitchen | same |
| K-331 | IN | See K-070 | CONTRADICTED -> IN |
| K-332 | IN | Not open concept | same |
| K-333 | IN | Closet opens to the bedroom | same |
| K-334 | IN | 0 bedrooms share a wall with a living-kind room | same |
| K-335 | IN | See K-005 | CONTRADICTED -> IN |

**Counts: IN 120 / MISSING 44 / CONTRADICTED 0 of 164** (current: 62 / 89 / 13). Seven items move IN to MISSING, all things the current model had and the clean sheet gave up: K-072, K-183, K-200, K-226, K-244, K-299, K-300. 54 move MISSING to IN and 11 move CONTRADICTED to IN; 90 are unchanged.

**Contradicted: none.** Named misses: K-004, K-006, K-010, K-033, K-058, K-059, K-064, K-072, K-078, K-080, K-081, K-083, K-096, K-102, K-103, K-123, K-129, K-134, K-157, K-166, K-170, K-172, K-183, K-185, K-200, K-220, K-226, K-227, K-237, K-242, K-244, K-245, K-257, K-261, K-270, K-273, K-282, K-290, K-292, K-297, K-299, K-300, K-302, K-307.

## 6. Review Blockers

| ID | Status | Evidence |
|---|---|---|
| CODE-01 | **Fixed** | Two flights: 18 risers (3,429 mm) + 4 risers (762 mm), both under 3.7 m (ABC 9.8.3.3.(1), abc_2023 p.852, as quoted in REVIEW-SUMMARY section 5); landing 4.4 ft at the basement; stair-top landing 4.62 x 5.00 ft (CODE-07). Basement redrawn: `basement_c.scad` (check_layout OK) |
| STR-04 | **Fixed** | 575.3 m2 to the outside face against 600 m2 (matrix_c.md), 24.7 m2 under; attached garage counted, porches not |
| STR-01 | Open | Basement ICF height (12.125 ft, 3.70 m) is unchanged; not a layout item |
| STR-02 | Open | Pool pit and footings unchanged |
| STR-03 | Open | Pool-room joists (26.95 ft span) unchanged. Under the pool room (x 69.4-96.3, y 18.2-52.8) the main floor now has interior walls on y = 28 and y = 22 (living / bath / closet row) and the H1 wall at x = 72. Not a claimed fix; the engineer decides |
| PLB-01 | Open | Pool drain-down destination is a basement/site item |

Other findings touched: CODE-02 fixed (landing openings are wall-free, 4.1 and 4.4 ft); CODE-07 fixed on the main floor; CODE-05 open (basement areaway guard 1,067 mm; the patio guard module is not used); CODE-11 unchanged (porch floors 610 mm above grade; the garage steps at the Costco door and the mudroom door need a landing, drawn at x 19.8-22.2); STR-06 open (one 16 ft door on a 26 ft garage south wall, 61%); ARC-01/SITE-03/SITE-04 fixed only with the south drive.

## 7. Cost drivers

**$ down** against the current model, in relative terms (no repo research range was used).
1. **Less wall and fewer corners.** 298.5 ft of heated perimeter and 4 corners against 395.5 ft and 30 (COST-08): about 97 ft less exterior wall, no inside corners to air-seal (K-069).
2. **Less floor and no crawl wings.** Heated 5,444 sf (was 5,486) and the garage 257 sf smaller; the east crawl wing (x 108-128) and the west crawl wing are not needed, with only a 5 ft strip at x 103-108 left.
3. **What pushes it back up:** a new south drive (site), a second stair run and landing, the redesign and re-permit effort, and the 16 ft south garage-door header. Net: $ down.

## 8. What you give up

A drain run that is 8% longer (951 ft against 879), a smaller master suite (one WIC, 183 sf bath), a living room with one wall of glass, the old front-door-to-deck sightline, and the unmodelled south drive that the three deal-breakers K-005/K-335 and the SITE findings rely on.

## 9. Departures

- **Site (drawn on the plan by the south garage door; NOT in site.scad):** garage door faces south; the west drive (x -32..-2, y road..42) is replaced by a south drive of about 24 ft x (road to y 0) in front of the garage. Septic (west), well (east) and the shop stay. Cost: a new drive and apron, offset by the shorter west drive; meters and service corridor move (see Cons). Needs the coordinator's call on the road side.
- **Foundation:** crawl-space wings are mostly not needed: the heated floor is x 22.16-108, so the west wing (x 7-22) and the east wing beyond x 108 are not built; x 103-108 stays as a crawl strip. `foundation.scad` is NOT changed here. Savings, not a cost.
- **Envelope:** the heated bounding box is 85.8 x 63.4 ft, inside the old 120.9 x 66.6 ft box; the garage is 22.16 x 26 ft at x 0-22.16, y 0-26. Porches: front porch 740 sf (x 34-108, y -10-0), patio 264 sf, deck 220 sf, master porch 120 sf, mud stoop 71 sf.
- **Basement:** `basement_c.scad` redraws only the stair foot (identical to Option A's). Shell, pool, exit stair, UTILITY room, shop: unchanged. Foot room x 42.65-47.27, y 27.6-45.34; flight 2 turns east into x 47.27-54.14, y 27.6-35.08.
- **Shop, septic, well:** none.
