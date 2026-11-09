# Plan facts: house design, rural Alberta (Phase 0)

Facts only. No judgements, recommendations or severities. Every number carries a source: `file:line` (repo `/home/user/house`), "computed" with the formula (all computed tables are produced by `scripts/plan_facts.py` and pasted below), or a render measurement.

## 0. Header

- **Commit:** `d20a2fa` on `main` (repo read-only; `tools/make_drawings.py` not run). **OpenSCAD:** 2021.01. `python3 tools/check_layout.py`: main_floor.scad 52 rooms / 56 doors / 17 windows OK; basement.scad 20 rooms / 20 doors / 2 windows OK.
- **Method:** room, door, window and fixture tables come from `openscad -D audit=true` on `models/main_floor.scad` and `models/basement.scad` (same tables check_layout.py reads); other values from `models/export.scad` via `tools/model_data.py` (saved as `model.json`) and from reading the SCAD and docs. Source line numbers are mapped from each table row. Geometry (areas, unions, distances, routes) is computed with shapely/numpy in `scripts/plan_facts.py`; renders by `scripts/plot_plan.py`.
- **Coordinates:** feet; x = east, y = north; x = 0 is the garage's west wall; y = 0 is the front wall of the den and breakfast bay (main_floor.scad:5-8, house_lib.scad:1-5). Both levels share the frame.
- **Definitions used.**
  - *Room rectangle* = wall centre lines (house_lib.scad:19-24). "W x D c/l" = centre-line size; "clear" = c/l minus half of each bounding wall's thickness. Main floor: every wall is `wall_t` = 0.4 ft (house_lib.scad:40), exterior and interior alike (the model draws no thicker exterior wall). Basement outside walls: ICF 13.25 in = 1.104 ft (foundation.scad:37).
  - *Conditioned main floor* = main_rooms rows whose kind is not `porch` or `garage` (includes ceiling-0 hall zones and the STAIR DN stairwell footprint). *Basement* = all base_rooms rows except the EXIT STAIR areaway.
  - *Opening width* = the `width` field of a door row; the model draws the leaf at that full width (house_lib.scad:leaf()). "Approx clear" for a single swing door = opening - 1.5 in (a convention, not in the model).
  - *Exterior wall* = a room edge whose point 0.55 ft outside lies in no heated room; the outside is classed yard/soil, porch/patio (open, unconditioned), garage, or areaway.
  - *Circulation* = rooms of kind `hall` (halls, corridors, vestibules, landings), foyer excluded; foyer, mudroom and the stair are separate lines (§6).
  - *Outside corner* = convex vertex of the heated-envelope polygon; inside corner = reflex vertex.
- **Source caveat:** the audit tables carry no fixture-type field; wet fixtures and appliances are identified by hand from box coordinates and the source-line comments (boxes are listed in §9 so the mapping can be checked).

## 1. Envelope and areas

{{sec1}}

## 2. Orientation

### 2.1 Compass, road and driveway

- **North = +y.** main_floor.scad:5-8 ("x = east, y = north"); house_lib.scad:1. The front porch is at y < 0 (south): FRONT PORCH y -15.26..0 (main_floor.scad:94); the great-room deck and office/master porches are at y > 52 (north) (main_floor.scad:98-100); the side porch is on the east (main_floor.scad:101).
- **Road: south.** "The road is assumed along the south side" (site.scad:8); road north edge y = -100 (site.scad:74). Land is not chosen; positions are relative to the house (site.scad:6-8).
- **Driveway: west side.** Drive from the road up the west side to the garage's west-facing doors (site.scad:11-12; rectangle x -32..-2, y -100..42, site.scad:111) plus a front loop south of the house (x 25..130, y -72..-14, site.scad:113-117). Garage doors: west facade, axis y at x = 0 (main_floor.scad:117-118). Services corridor on the west side of the drive (site.scad:14-17, 162-164). Septic tank and field west; well east (site.scad:63, 70-73). Shop (later) north at x 0..100, y 130..230 (site.scad:56-60).
- **Facade summary:** garage W (doors), front porch/foyer/den/breakfast/kitchen S, great room/deck/sun room/office/master N, master suite and side porch E (computed in §2.2 and §5).

{{sec2}}

## 3. Room tables

{{sec3}}

Sliver fragments, so per-row statistics mislead: "(suite entry, 2nd piece)" 3.72 x 1.55 ft (main_floor.scad:55); basement "HALLWAY" row 18.87 x 1.125 ft (basement.scad:61), which is the south strip of a 3-row hallway (rows basement.scad:61-63, x 35.27..54.14, y 27.6..35.08, with the STAIR UP flight room between its two arms).

## 4. Door schedule

{{sec4}}

## 5. Window schedule

{{sec5}}

## 6. Circulation

{{sec6}}

Merged basement hallway zone (rows basement.scad:61-63, plus the stair foot between): the zone is 18.87 ft wide (x 35.27..54.14) by 7.48 ft (y 27.6..35.08); its two arms on either side of the stair foot are about 6 ft wide.

## 7. Door-graph facts for flow

{{sec7}}

## 8. Adjacency facts

{{sec8}}

## 9. Plumbing

{{sec9}}

## 10. Stairs

{{sec10}}

## 11. Electrical and mechanical facts

| Item | As stated | Source |
|---|---|---|
| Electric service entrance | Underground from the road to a meter on the **west wall**; the house's own service (not fed from the shop) | permit README:152-153; make_drawings.py:1488-1491; site.scad:10-17 |
| Service route in the model | three dashed lines (fibre y=44, power y=46, gas y=48) run east from x = -41/-44/-47 to x = 7.27 (the bedroom wing's west wall, a crawl-space wing) | site.scad:162-164 |
| Meters | two boxes on the west wall at x = 6.6, y = 45 and 47.5, 3 ft above grade (not labelled which is which) | site.scad:175 |
| Panel | in the basement UTILITY room (x 22.16..37.37, y 35.08..42.77); no position or box in the fixture tables | permit README:144-145, 153; make_drawings.py:1491, 2254 |
| Panel size / service amperage | **not in model** for the house as built-first. "200 A panel fed from the shop" appears only in the Shop-Base-Plan (lines 84, 234, 323, 364), whose Nov 3 update says the house has its own services from the road (Shop-Base-Plan:9-11) | Shop-Base-Plan.md |
| Generator, batteries, switchgear | in the model only in the shop (Bay 1: shop.scad:145-151); none in the house model | shop.scad |
| Heating plant | basement UTILITY room: five boxes listed in the order of the comment "air handler, boiler, water heater, well-water treatment, HRV" (basement.scad:135): air handler (22.8..25.8, 35.7..38.7, 6 ft high, basement.scad:136), boiler (26.3..28.5 x 35.7..37.7, 3.5 ft, :137), water heater (round 29.0..31.2 x 35.7..37.9, 5.5 ft, :138), well-water treatment (33.8..36.6 x 35.7..37.7, :139), HRV (22.8..25.8 x 40.4..42.3, z 5.5-7, :140). The mapping is by comment order. Permit README says "furnace or boiler" (make_drawings.py:2254) and "heating, HRV, water heater, water treatment, the electrical panel and the sump pump" (permit README:144-145) | basement.scad:135-140 |
| Boiler / heat output, fuel, heat-loss calc | **not in model**; Oct 28 decision #21 (a/b/c) is open (House-Review-and-Research:1043-1047) | |
| Water heater | one, in the UTILITY room (above); no recirculation, no second heater modelled | basement.scad:138 |
| Gas / propane | Natural gas from the road if served, else 1 000 US gal propane tank at (-60, -45) (pad 16 x 6 ft) with a line east along y = -45 to x = -47, then north along the gas line (x = -47) to the house (y = 48) | site.scad:64, 164, 170-173; permit README:154-156 |
| Gas appliances | range (fuel not stated, main_floor.scad:198); great-room fireplace box (gas or wood undecided, main_floor.scad:241; permit README:108-109) | |
| Internet | fibre (x = -41 line) or a Starlink dish at (12, 80) with a drop to (12, 62.04) | site.scad:65, 162, 181-183; permit README:168-172 |
| Pool plant | pool equipment room x 96.33..103.04, y 29.12..41.94: filter (round), pump, heater, dehumidifier, chemicals (basement.scad:141-146); pool dehumidifier row at basement.scad:145 (comment order); pool/spa water: foundation.scad:57-58, 63-65 | basement.scad |
| Sump, floor drains, radon | Redesign/permit text only (sump "utility room is suggested", permit README:476-477; Redesign:224, 345, 497); no location or box in the models | |
| Well water | well (150, 75), line to (150, 45) then (126.97, 45); water treatment in UTILITY (basement.scad:139) | site.scad:63, 167 |

## 12. Site distances

{{sec12}}

## 13. Run-document premises vs the model on main

Status key: PRESENT = in the model/docs on main as the run brief states; ABSENT = not in the models or docs; CHANGED = exists in a different form.

| # | Premise | Status | Evidence |
|---|---|---|---|
| a | ~70 ft heated, walkable utility tunnel house-shop, floor at basement level | **ABSENT (dropped)** | "No tunnel": site.scad:33-35; Redesign:22-23, 39-40, 559-566; permit README:121-124, 520; Shop-Base-Plan.md:15-19 (its §5, §6 and the tunnel drawing are kept "for reference only"). No tunnel geometry in site.scad. Leftovers: shop.scad:19-23 comment, "TUNNEL PORTAL" room (shop.scad:62) and its stair well (shop.scad:158-161) are still drawn in the shop. The old landing room (UTILITIES x 60.1..100.1, Shop-Base-Plan:96) is not in the basement: UTILITY is x 22.16..37.37 (basement.scad:57). Shop to house gap in the model is 63 ft of yard (§12) and a 210 ft buried-service route (site.scad:197) |
| b | Shop is the electrical service point; house has a 200 A panel fed from the shop | **CHANGED** | Described in Shop-Base-Plan.md:81-86, 226-236, 323; replaced by the Nov 3 update at :9-11 (house has its own services from the road) and permit README:152-153 (power from the road to a west-wall meter, panel in the basement UTILITY room); site.scad:10-17, 162-175. No panel size for the house anywhere except the superseded 200 A |
| c | Heating plant (boiler for pool + DHW + snow melt + house heat; geothermal backup) in shop Bay 1 | **CHANGED** | Shop boiler drawn in Bay 1 "WATER + HEAT" (shop.scad:152, room shop.scad:61) and described as the hub (Shop-Base-Plan.md:101, 289-298); but the house also has its own boiler and water heater in the basement UTILITY room (basement.scad:135-138) and the Nov 3 update retires the hub idea (Shop-Base-Plan.md:12-13). Geothermal: see (d) |
| d | Geothermal loop field | **ABSENT** from models and from the house/permit docs. Only: research (House-Review-and-Research §2, lines 757-855; decision #21 at 1043-1047, "GSHP" option) and one phrase "a future ground-source unit fits beside" the shop boiler (Shop-Base-Plan.md:296-298). No loop-field rectangle in site.scad |
| e | Heated driveway / walkways (snow melt) | **ABSENT** from models and Redesign/permit docs. Documented only as research (House-Review-and-Research §3 lines 855-925, decision #23 at 1050-1054) and as a shop-boiler load (Shop-Base-Plan.md:101, 289-295). Exit-stair treads "heated or heat-traced... worth considering" (Redesign:500). Drives in site.scad:108-132 are plain slabs |
| f | "U-stair in the former bar area" of the basement | **CHANGED** | Oct 28/29: option A decided (House-Review-and-Research:979-982, 1085-1086, 1131, 1171). Nov redesign model: one straight 22-riser stair, x 42.65..47.27, top y 47.1, foot y 28.725 (house_lib.scad:120-125; basement.scad:59; Redesign:117-121, 150-170); no "bar" room or U-stair anywhere in basement.scad |
| g | 80 ft truck apron; turning room for a Volvo VNL with trailer | **CHANGED / ABSENT** | Apron is **70 ft** deep in both docs and model: Shop-Base-Plan.md:112 (x -72..0) and site.scad:125 (x -72..-2, y 130..230), plus a 60 ft deep east apron (site.scad:130; Shop-Base-Plan.md:59) and a 32 ft north leg (site.scad:129). No 80 ft dimension and no "VNL" in models or docs. Only "tractor-trailer's ~50 ft outside turning radius" (Shop-Base-Plan.md:71; site.scad:127-128 comment). All of this exists only with `phase = "full"` |
| h | Shared drive | **PRESENT** | "A shared driveway runs up the west side" (Shop-Base-Plan.md:42, 113-116); site.scad:111 (house drive) and 124 (continues north at x -38..-8 in full phase). In the house phase the drive ends at y = 42 (site.scad:111) |
| i | Parents' house (no basement, crawl space, floor 2'-4" up, porch roof posts, 500 lb egg-chair hook) | **ABSENT from the SCAD models; PRESENT as drawings only** | Not in any `.scad`. Plan images `docs/small_house/IMG_0415..0420.PNG` (read by me): "PARENTS' HOUSE - FLOOR PLAN v1", 32' x 21' = 672 SF, 1 bed / 1 bath, "CRAWL SPACE (NO BASEMENT) - SERVICES: FROM MAIN HOUSE (TBD)", 7'-0" x 32'-0" porch, mech closet, W/D, an "EGG CHAIR HOOK: doubled joist + blocking, rated eye-bolt (500 lb design)" on the plan, porch posts in the elevations. The 2'-4" floor height is not readable in the images (an unmeasured base band is drawn). Text mentions: permit README:212-215 ("a future house for the parents is planned"); make_drawings.py:1503. Position on the lot, distance to the main house and foundation type in a model: **not in model** |
| j | 100 x 100 ft shop, 4 bays with wash bay, Bay 1 bathroom draining west by gravity | **PRESENT / CHANGED** | 100 x 100 (site.scad:218; shop.scad:46), four bays Bay 1 utilities / Bay 2 truck / Bay 3 truck + pit / Bay 4 wash (shop.scad:47-52; roof 100 x 100 at shop.scad:165); "NETWORK + BATH" room in Bay 1 (shop.scad:60). Gravity west then north: Shop-Base-Plan.md:300-306, 416-417; the Nov 3 update says instead the shop bathroom "pumps to the house tank through a small lift station in Bay 1" (Shop-Base-Plan.md:28-29). Also Shop-Base-Plan.md:404-412 has the house pumping to a shop tank. Drain direction is not in shop.scad |
| k | Septic on the west by the utility room; well on the east | **PRESENT, with a note** | Tank [-3,52,3,64], field [-120,45,-65,100], reserve [-120,-15,-65,40], well (150,75) (site.scad:63, 70-73); permit README:157-166. The tank sits at y 52..64, beside the bedroom wing and MUSIC ROOM; the UTILITY room is y 35.08..42.77 (9-17 ft south of the tank's south edge (y 52); §12). Shop-Base-Plan.md:9-11 header bullets state the reverse (well west, septic east), contradicted at :20-21 |
| l | Basement pool and spa | **PRESENT** | POOL ROOM row (basement.scad:67), pool 15 x 15 ft and spa 8 x 8.2 ft (foundation.scad:57-58), water depth 4.5 ft / 3.5 ft (foundation.scad:61-65), equipment room and pool bath (basement.scad:68-69); Redesign §4 |
| m | Main-floor baseline: model traced from `main_floor.jpg` (Nov redesign); run doc says `floor_plan.JPEG` "geometry matches the current model" | **CHANGED** (matches `main_floor.jpg`; `floor_plan.JPEG` matches in footprint only) | main_floor.scad:4-8; Redesign:3-5 calls floor_plan.JPEG "the version before them" |

**(m) image comparison (viewed at a glance, both sheets: front porch at the bottom, garage at the left).** Shared: the same overall footprint and wing pattern: garage on the west edge, a bedroom wing at the north-west, a large central block, two side wings with a covered porch/deck on the north and the master wing on the east, a front porch along the south. Different: in `floor_plan.JPEG` the big central room with the island and sink is in the upper middle (where `main_floor.jpg` has the GREAT ROOM), the south-centre holds two dining/study rooms, hallways and a patio, there is a stair/utility cluster at the garage corner and a row of pantries and storage rooms in the middle-east; in `main_floor.jpg` (and the model) the KITCHEN / DINING (35.6..69.14, y 6.28..29.51), BREAKFAST bay, FOYER and DEN are at the south-centre, the GREAT ROOM is north-centre, and the garage-side cluster is mudroom/laundry/scullery with a single stair at x 42.65..47.27. The two sheets agree on the footprint and the position of the garage and master wing, not on where the kitchen, great room and stair sit. The model's room layout matches `main_floor.jpg` (main_floor.scad:4-8), so the run document's claim that `floor_plan.JPEG`'s "geometry matches the current model" holds for the footprint only; Redesign:3-5 calls `floor_plan.JPEG` the earlier version.

## 14. Oct 28 decision list status (23 items, House-Review-and-Research-2026-10-28.md:977-1054)

| # | Item (doc lines) | Status | Evidence |
|---|---|---|---|
| 1 | Basement stair A/B/C (979-982) | superseded | Decided A (U-stair in the bar) Oct 29, lines 1085-1086, 1131; replaced by the Nov redesign's straight stair (Redesign:117-121, 150-170; basement.scad:1-21) |
| 2 | One interior stair or two (983-984) | decided | No second stair (1132); main stair + exit stair only (Redesign:140) |
| 3 | Basement bathroom by the pool (985-986) | decided | Pool bath added (1124, 1132); basement has POOL BATH + 2 BATH rows (basement.scad:60, 69, 71); under-slab rough-in listed (permit README:466-475) |
| 4 | Basement outline (987-989) | superseded | Oct 29 kept a 100 x 60 rectangle (1133); Nov outline is a 14-vertex 3,475 sq ft polygon with crawl space/frost walls elsewhere (foundation.scad:40-45, 90-105; Redesign:238-252) |
| 5 | Theater sound/vibration package (990-992) | decided (spec) | "Still open" Oct 29 (1136-1137); room-within-a-room spec in Redesign:434-436 |
| 6 | Exit stair vs side porch (993-994) | superseded | Moved Oct 29 (1134), then redone: areaway off the gym's north wall, patio guard (Redesign:446-480; foundation.scad:134-145; main_floor.scad:345-354) |
| 7 | Ask architect: garage-corner stair, side-load garage doors (995-997) | open | No later doc records an answer; model draws side-load (west) garage doors (main_floor.scad:117-118) and no garage-corner stair |
| 8 | Gas service (1001-1002) | open | Propane fallback in the model (site.scad:64, 170-173; permit README:154-156); land not chosen |
| 9 | Well prospects (1003-1005) | open | Land not chosen (site.scad:6-8); well drawn at (150,75) |
| 10 | Climate zone (1006-1008) | open | "7A or 7B... from the location" (permit README:77, 295 blank) |
| 11 | Geotechnical report (1009-1010) | open | Redesign:559-575 open questions ("Geotech first") |
| 12 | ICF core 8 in (1014) | decided | 13 1/4 in wall (foundation.scad:37; House-Review:1125) |
| 13 | Waterproofing in writing (1016-1017) | open (spec'd) | Waterproofing spec in Redesign:218-228; contract-scope wording not in repo |
| 14 | ICF above grade? (1018) | decided | Basement-only ICF; main floor on frost walls/crawl space (foundation.scad:90-105; Redesign:238-252) |
| 15 | Wall assembly (1019-1020) | open | No wall assembly in Redesign/permit docs; models draw 0.4 ft walls |
| 16 | Window spec (1021-1024) | open | No window spec in the later docs; window rows are geometry only (main_floor.scad:174-192) |
| 17 | Pool room = natatorium spec (1025-1028) | decided (input) | Dehumidification and the room around the pool in Redesign:358-373; pool dehumidifier in the model (basement.scad:145); permit README:395, 460 |
| 18 | Roof package (1029-1031) | open | Roof "product parked until land"; model has 16 hip blocks, 6/12 (main_floor.scad:305-322) |
| 19 | Before-the-pour checklist (1032-1034) | decided (listed) | Phase 1 rough-ins checklist, permit README:466-480 (under-slab drains, sump, radon, pool); well/septic/service entries in README:149-172 |
| 20 | Well contract (1038-1042) | open | No contract terms in repo; land not chosen |
| 21 | Heating plant architecture (1043-1047) | open | House has air handler + boiler + water heater boxes (basement.scad:135-138), fuel and type not chosen; the shop-hub version is superseded (Shop-Base-Plan.md:12-13) |
| 22 | Distribution: radiant (1048-1049) | open | Only "essential if the slab carries in-floor heat" (Redesign:211); no distribution in models |
| 23 | Snow-melt scope (1050-1054) | open | Not in models; shop-boiler tie superseded (Shop-Base-Plan.md:101) |

Count: decided 7 (2, 3, 12, 14, 17, 19 and 5 as spec), superseded 3 (1, 4, 6), open 13 (7-11, 13, 15, 16, 18, 20-23).

## 15. Model inconsistencies noticed (facts only)

1. **Stair length, comments vs table.** main_floor.scad:13-14 and basement.scad:12 say the stair "runs 15 3/4 ft"; the table gives 21 treads x 10.5 in = 18.375 ft (house_lib.scad:121-125), and Redesign:120, 155 say 18'-4 1/2".
2. **Basement door count.** Redesign:125 says 19 doors were added; basement.scad:79-98 has 20 door rows (14 swing doors, 2 "open", 4 "full").
3. **"By the UTILITY room" vs the drawn sewer and tank.** site.scad:22, 185-186, permit README:157, Redesign:564 place the septic tank / sewer at the UTILITY room (y 35.08..42.77); the model draws the tank at y 52..64 (site.scad:70) and the building sewer leaving at (22.16, 58) (site.scad:188), which is the MUSIC ROOM's west wall (y 50.35..63.16, basement.scad:54).
4. **Service lines stop at the crawl-space wing.** Power/gas/fibre end at x = 7.27 (site.scad:162-164, 175), the bedroom wing's west wall; the UTILITY room and panel are at x 22.16..37.37 (basement.scad:57), 14.9 ft further east, and the lines are at y 44..48, i.e. beside STORAGE (y 42.77..50.35), not UTILITY (y 35.08..42.77).
5. **Well water line stops at the master bedroom.** site.scad:167 ends at (126.97, 45); the docs say it enters at the pool equipment room (permit README:164-166), whose east wall is x = 103.04 (basement.scad:68), 24 ft west.
6. **Shop-Base-Plan contradicts itself and the model.** Header bullets at lines 9-11 (well west, septic east) vs lines 20-21, permit README:157-166 and site.scad:63, 70 (septic west, well east); body: well at (140, 110) (lines 72, 126) vs site.scad:63 (150, 75); septic zone around (-89, 212) (line 131) vs site.scad:70; "tunnel ~70 ft" and 200 A feeder through it (lines 96, 234) vs lines 15-19; title line 1 "utility hub + tunnel to house".
7. **Shop still draws the tunnel.** shop.scad:19-23, 62, 158-160 (portal room and stair well) while site.scad:33-35 says the tunnel is gone.
8. **Shop bathroom drainage.** Gravity west (Shop-Base-Plan.md:300-306, 416-417) vs pumped to the house tank (Shop-Base-Plan.md:28-29) vs house pumps to a shop tank (lines 404-412).
9. **Basement size across docs.** Oct 28 doc: 6,000 sq ft, 100 x 60 ft (House-Review:28, 275, 638-639); Redesign:523 "3,000 ft2 basement"; model polygon 3,475 sq ft, bbox 80.9 x 57.4 ft (foundation.scad:40-45; §1).
10. **Building area vs the Part 9 limit.** Redesign:574 says about 626 m2 to the outside face of the walls (house with attached garage); model heated + garage footprint = 6,319 sq ft = 587 m2 at wall centre lines, 595 m2 with 0.2 ft added each side (house_lib wall_t/2), 604 m2 with 0.4 ft; porches excluded in all three (computed from main_floor.scad:47-104 rows, kind not porch). The 626 m2 is not reproduced.
11. **Gym exit door.** Redesign:543 says a "full-glass 3'-6" exit door"; basement.scad:98 draws type "door" (opaque leaf), width 3.5 ft.
12. **Unnamed rows.** 9 main-floor and 2 basement hall/closet rows have an empty label and are identified here only from source-line comments (main_floor.scad:54-55, 63, 65-66, 80, 84, 86, 91; basement.scad:62-63).
13. **Pantry.** No PANTRY room exists in the main-floor table; floor_plan.JPEG labels several pantries, and main_floor.scad:202 has "tall pantry cabinets" inside the kitchen; SCULLERY is the nearest room (§8.3).
14. **Powder room.** No half bath on the main floor; the only toilets are in the bedroom-2 suite WC, the hall BATH and the master WCs (§9).
