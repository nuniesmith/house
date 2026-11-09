# Electrical review (ELE), Wave 3

**Specialist:** Electrical. **Date:** 2026-11-09. **Repo:** `/home/user/house` @ `d20a2fa` (read-only).

**Inputs read:** COMMON-RULES.md; 05-electrical.md brief; `plan_facts.md` (§1.1, §3 via grep, §11, §12, §13); `models/site.scad` (header 1-45, 160-200, 214-222); `models/shop.scad:130-151`; `models/basement.scad:130-146`; `docs/permit/README.md` (§2 lines 122-172, §8 lines 460-495); `docs/permit/schedules/doors.csv`; `docs/shop/Shop-Base-Plan.md` (Nov 3 note 1-29, Bay 1 electrical 176-275); `docs/house/Redesign-and-Spec-2026-11-02.md` §4; `docs/house/House-Review-and-Research-2026-10-28.md` lines 646-647, 796-801, 855-922 (heating and snow-melt research); `kayla_checklist.md` (K-111, K-268, K-309..K-311); code library `electric_2022` and `abc_2023`. Scratch calculations: `$RUN/work/ELE/calc.py`, `vd.py`.

## Ground rules for this report

- **HARD LIMIT.** The library has no Canadian Electrical Code (CEC) and no CSA B149.1. Every wiring-level item below is marked "needs CEC check". The AEUC 2022 governs the **utility side** only (it applies to systems that deliver power "to consumers' services", Section 0 Scope, p.7). It sets no service size, no demand calculation, no conductor rule and no metering equipment rule for a house. ABC 2023 9.34 hands service capacity to "the Electrical Code Regulation" (9.34.1.1).
- **All kW, factors and resistances below are my stated planning assumptions**, not code values. The CEC demand calculation by the electrician or engineer replaces them. Conductor resistance uses a physical resistivity (Cu 1.72e-8, Al 2.82e-8 ohm·m at 20 C) and nominal cross-sections (4/0 AWG 107.2 mm2; 350 kcmil 177.3 mm2; 500 kcmil 253.4 mm2; 600 kcmil 304 mm2), with a hot-conductor multiplier 1 + 0.00393 x 60 = 1.236 (Cu) and 1 + 0.00403 x 60 = 1.242 (Al) as an assumed 80 C case. None of this is from a CEC table. **Needs CEC check.**
- **Architecture reviewed is the one on `main`:** the house is the service point (power from the road, west side, into the basement UTILITY room: `site.scad:10-17`, PF §11); the shop is a later project fed by buried lines from the house (`site.scad:197`). Tunnel material is only in the last section.
- Land is not chosen. Utility, distributor, transformer capacity, phase availability and gas availability are assumptions. Structural and gas items go to a licensed Alberta engineer / gas fitter.

## Findings

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|
| ELE-01 | Should fix | Whole house, service size | **No service amperage exists anywhere in the house model or docs.** My planning demand for the house alone is **193 A** if the heating, DHW, pool and spa are fuel-fired, and **398 A** if they are electric (load table, H-rows). So 200 A is marginal even in the best case and 400 A is the practical upper bound, and the swing is decided by the open heating-fuel decision (#21). The service entrance (meter base, service conduit, panel bus, main breaker, sleeves poured into the ICF) should be designed for the larger answer even if the first energisation is smaller. Get a formal CEC load calculation for both cases before the sleeves are sized. | PF §11 ("not in model" for panel size; only the superseded 200 A at Shop-Base-Plan:84, 234); load table totals; heating decision open: PF §11 "Boiler... Oct 28 decision #21 open"; House-Review:646-647, 801 (GSHP + aux, boiler backup) | ABC 2023 9.34.1.1 (service capacity "shall conform to the Electrical Code Regulation"); needs CEC check (demand calculation) | $$ (larger service equipment and conduit now vs a service upgrade later: unknown) |
| ELE-02 | Should fix | Service vs future loads | **Do not size the house service to also carry the shop and the parents' house without a utility conversation.** Simple sums of my planning demands: house A 193 A + parents 56 A = **249 A**; + shop 198 A = **447 A**. House B 398 A + parents 56 A = **454 A**; + shop = **652 A** (no diversity between buildings; with an assumed 0.8 inter-building factor: 358 A / 522 A). Welders, compressor and lifts may want three-phase (Shop-Base-Plan:228-231 says three-phase availability "changes everything"), which a single-phase house service cannot give. Decision to put to the distributor: (a) one 400 A single-phase service for house plus parents, with the shop on its own later service (own meter, own AEUC 2-024 connection), or (b) one large service feeding all. (a) keeps the house-first build small and leaves the shop's phase question open. Ask the distributor what the transformer at the road will carry. | Load tables (house, shop S-rows, parents P-rows); Shop-Base-Plan:227-231, 234, 238-240; PF §13 (i) parents' house "SERVICES: FROM MAIN HOUSE (TBD)" | AEUC 2-024 (utility will not connect a consumer's service unless metering equipment and location are acceptable and a valid permit has been received); sizing needs CEC check | $$$ if (b) forces a 600 A+ service or transformer upgrade; unknown |
| ELE-03 | Should fix | Future shop feeder, length | **The "210 ft" buried shop run is not the panel-to-shop length.** It starts at (-50, 50), which is 72.2 ft west of the basement west wall (x = 22.16 to x = -50) and about 11 ft north of the UTILITY room's mid-line (y 38.9 to 50), so the real run from the UTILITY room is about 72.2 + 11.1 + 210 = **293 ft** (plus risers). Voltage drop at 200 A, single-phase 240 V, using 2 x L x I x R: 293 ft = 89.3 m. Copper 4/0: R = 1.72e-8 / 107.2e-6 = 1.604e-4 ohm/m; V = 2 x 89.3 x 200 x 1.604e-4 = **5.73 V = 2.39 %** (2.95 % hot). Aluminium 4/0: **9.40 V = 3.92 %** (4.86 % hot). Copper 350 kcmil 3.47 V = 1.44 %; Al 350 kcmil 5.68 V = 2.37 %; Cu 500 kcmil 2.42 V = 1.01 %; Al 500 kcmil 3.98 V = 1.66 %. Add the service run (below) for the cumulative drop. A more direct route is possible: the closest house wall to the shop wall is 63.4 ft (PF §12.2); a direct run of about 100 ft (63.4 + about 36 ft inside the house, assumed) drops only 1.96 V = 0.82 % in Cu 4/0, 3.21 V = 1.34 % in Al 4/0. Conductor choice follows the engineer's route choice (ELE-04). | `site.scad:197` (-50,50)->(-50,126)->(80,126)->(80,130) = 76 + 130 + 4 = 210 ft; PF §12.2 (63.4 ft); basement UTILITY x 22.16..37.37, y 35.08..42.77 (PF §11); arithmetic in `$RUN/work/ELE/vd.py` | needs CEC check (conductor sizing, ampacity, voltage-drop limits, burial/protection); resistances are stated assumptions | $$ (copper vs aluminium vs size; the 293 ft vs 100 ft route difference is about 193 ft of 4 conductors: unknown $) |
| ELE-04 | Should fix | Future shop trench route, west side | **The planned shop route is pinched by the septic and crosses the effluent line.** To reach (-50, 50) from the house's west side the new trench has to run between the gas line (y = 48) and the septic tank's south edge (y = 52): a **4 ft gap** (1.22 m), with power at y = 46 only 4 ft south of the line's centre. The route then runs north along x = -50 and crosses the pressure effluent line at (-50, 66) (the line spans x -65..-3 at y = 66). The route's first point (-50, 50) is also 3 ft from the gas line at x = -47 and 7.2 ft from the power turn at (-44, 46). The spare sleeve in README §8 has no stated location. Choose the sleeve position and trench route now with the site and septic specialists; the Phase 1 spare sleeve (and a second one for a parents' feeder) should leave the basement wall away from the septic neighbourhood. Dig rules: call the cable operator before any excavation, and no excavation within 1 m of an underground utility cable unless under the operator's control. | `site.scad:162-164` (fibre y=44, power y=46, gas y=48), 188-191 (building sewer y=58, effluent y=66), `site.scad:70-71` tank [-3,52,3,64], chamber [-3,64,3,68], `site.scad:197`; README:490-491 (one spare sleeve) | AEUC 2-020(1) and 2-020(3); service-corridor separations and gas separations: needs CEC check / needs B149.1 check | $$ |
| ELE-05 | Should fix | Meter to panel, UTILITY room | **Power stops at the wrong place for the panel.** The three service lines end at the bedroom wing's west wall x = 7.27 (meters at x = 6.6, y 45 and 47.5, 3 ft above grade), which is **14.9 ft** short of the basement west wall x = 22.16 where the panel sits, and the UTILITY room is at y 35.08..42.77 (its north edge is 2.2 ft south of the nearer meter at y = 45, 45 - 42.77) and 13.75 ft lower (floor-to-floor). No conduit, route or main-disconnect location is drawn between the meter and the panel, and the meter sits on a crawl-space wing. Draw the meter-to-panel route, decide the main disconnect location, and add the conduit/sleeve through the ICF or crawl space to the Phase 1 rough-in list. Meter boxes at y = 45 and y = 47.5 are not labelled which is power and which is gas. | PF §11 and §12.2 (14.9 ft); `site.scad:175`; `site.scad` header (floor_to_floor 13.75 ft); README:152-153, 490 | AEUC 2-024(b) (metering equipment and location acceptable to the utility); length of service conductors inside the building before the disconnect: needs CEC check | $ |
| ELE-06 | Should fix | Phase 1 rough-ins (README §8) | **The slab/ICF rough-in list covers only theatre, music room, pool equipment and the service/shop sleeves.** Cheap now, costly after the pour, and not listed: (a) meter-to-panel conduit (ELE-05); (b) well-pump cable conduit from the pool equipment/UTILITY side to the well at (150, 75), about 155 ft by Manhattan route (120 + 35) (ELE-11); (c) conduit to the Starlink dish at (12, 80), 18.0 ft from (12, 62.04); (d) EV charger circuit and a garage sub-panel feed (K-311); (e) generator inlet or transfer switch location and a critical-loads panel next to the UTILITY panel (ELE-07); (f) feeder conduit(s) for the parents' house (ELE-13); (g) pool/spa underwater-light and bonding penetrations (bonding grid is listed in README §8 for the pool, but not its connection to the panel); (h) sump and pool-pit ejector circuits (README §8 lists two pumps); (i) cable sleeves for electric snow-melt on steps, walks and garage apron if chosen (House-Review:898-899); (j) spare 2-inch-class conduits for solar and battery (ELE-12). | README:460-491 (§8 list); PF §12.1 (Starlink (12,80), drop to (12,62.04): 80 - 62.04 = 17.96 ft); K-311; PF §11 (water line only, no power conduit to the well) | needs CEC check (all wiring methods, conduit fill, burial depth) | $ now vs $$$ later |
| ELE-07 | Should fix | Generator and transfer | **No generator, transfer switch, battery or switchgear exists in the house model** (only shop.scad:145-151). In the house-first plan the house depends on power for the well pump, the sumps, the effluent pump and the heating plant's blowers and circulators. Critical-load sizing (running kW): heating aux 1.5 + DHW aux 0.2 + HRV/treatment/radon 0.6 + well pump 1.1 + sump/effluent 1.75 + fridges 1.0 + critical lighting/receptacles 2.0 + network/Starlink 0.6 + garage door openers 0.8 = **9.55 kW**. Add the largest motor start step: well pump 1.1 kW x (3 - 1) = 2.2 kW (assumed 3x start) = 11.75 kW; x 1.25 margin = **14.7 kW, about a 15 kW class** (fuel-fired heat). Add pool circulation + dehumidifier (1.5 + 3.0 = 4.5 kW): (9.55 + 4.5 + 2.2) x 1.25 = **20.3 kW**. If heat is electric (bounding 29.3 kW): (9.55 - 1.5 + 29.31 + 2.2) x 1.25 = **49.5 kW, about a 50 kW class**. The Shop-Base-Plan placeholder of 50-80 kW was for house + shop + pumps. **What stays live:** heating plant aux, well pump, sump/effluent pumps, fridges, a few lights, network. **What sheds:** range, dryer, EV charger, pool/spa heaters, garage heater, theatre, snow melt, general receptacles. Transfer: a service-entrance-rated transfer switch, or a 100 A critical-loads sub-panel with a transfer switch, next to the UTILITY panel; no generator pad location is shown. A propane generator would share the 1 000 US gal tank at (-60, -45), 105 ft or more from the house. | PF §11 (generator only in shop); Shop-Base-Plan:250-261; load-table H5, H7-H10, H3; arithmetic above | needs CEC check (transfer equipment, interlock, grounding, generator circuit); needs B149.1 check (gas supply to a generator) | $$ |
| ELE-08 | Should fix | Pool and spa plant | **Pool and spa heater fuel is not stated in the model** (basement.scad:143 "heater", Redesign §4.5 silent), and it moves the service by about 18 kW. Warm-up energy: pool 28.7 m3 x 4.186 MJ/(m3 K) x 18 K (10 to 28 C, assumed) = 2 162 MJ = 600 kWh; over 48 h = **12.5 kW** (electric case). Spa 4.9 m3 x 4.186 x 30 K (10 to 40 C, assumed) = 615 MJ = 171 kWh; heater 5.5 kW assumed. Pump, blower and jets add 1.5 + 0.5 x (2.0 + 1.5) = 3.25 kW; dehumidifier 3.0 kW (assumed). The room has 28.7 + 4.9 = 33.6 m3 of water, a bonding grid in the slab and a wet equipment room (pool equipment room x 96.33..103.04, y 29.12..41.94) about 66 ft from the UTILITY panel, so it needs its own sub-panel with GFCI protection. Decide heater fuel (gas boiler per House-Review:849 option (b), or heat-pump/electric) together with decision #21. | `basement.scad:141-146`; Redesign §4.1 table (28.7 m3 and 4.9 m3); PF §11 (pool plant); README §8 | needs CEC check (pool and spa wiring, bonding, GFCI, clearances; the CEC's pool section is not in the library) | $$ |
| ELE-09 | Consider | Heating-plant electrical, decision #21 | **Heating fuel is the biggest swing in the load table (H5 vs H6: 1.5 kW vs 29.3 kW).** The 29.3 kW bounding figure is 100 000 BTU/h / 3 412 = 29.3 kW, an assumed design loss because the model has no heat-loss calculation (PF §11). Whatever is chosen, get the heat-loss number from the energy/mechanical specialist before sizing electrical gear. A ground-source system with electric aux sits between cases A and B. | PF §11 ("not in model"); House-Review:801, 849 | needs CEC check | unknown |
| ELE-10 | Consider | Garage, EV charging | **K-311 asks for an electric vehicle charger in the garage; none is drawn, and no garage panel exists.** I assumed one 40 A x 240 V = 9.6 kW charger (H18, 100 % coincidence), the largest single load after the range. A load-management device could cut the contribution to the service, but whether the code lets you size on it is a CEC question. The shop plan also assumes truck charging at 19.2 kW (80 A x 240 V) (S8). K-309/K-310 (wall fans, retractable outlet and air compressor) add a few circuits. | K-309, K-310, K-311; Shop-Base-Plan:238-240 (load management) | needs CEC check | $ |
| ELE-11 | Consider | Well pump, Starlink | **The well pump is 155 ft by route from the panel and its cable route is not drawn.** Well at (150, 75); water line well -> (150, 45) -> (126.97, 45) (`site.scad:167`). Assumed 1 hp, 240 V, 8 A, #10 Cu (5.26 mm2): R = 1.72e-8 / 5.26e-6 = 3.27e-3 ohm/m; 155 ft = 47.2 m; V = 2 x 47.2 x 8 x 3.27e-3 = **2.47 V = 1.03 %** to the wellhead. With an assumed 300 ft of well-depth cable added (455 ft = 138.7 m): V = 2 x 138.7 x 8 x 3.27e-3 = 7.26 V = **3.0 %** (1.9 % with #8, 8.37 mm2). Well depth is land-dependent. Starlink at (12, 80): the dish and its cable (18.0 ft) are well within a typical product cable length (product length not from the library). | `site.scad:63, 65, 167, 181-183`; PF §11, §12.1; House-Review:696 | needs CEC check | $ |
| ELE-12 | Consider | Solar and battery readiness | **No solar or battery readiness in the house phase** (Shop-Base-Plan:245-247 places solar at the shop). A grid-tied inverter or battery is a generating facility needing the distributor's interconnection process; the AEUC covers only the utility's side of the demarcation point. Micro-generation interconnection rules: **not found in library**. Cheap now: two spare 2-inch-class conduits from the UTILITY room to an attic/roof chase and to the west yard, and panel space for a backfed breaker. | Shop-Base-Plan:245-247; `electric_2022` p.7 (scope (b)); search "generation facilities interconnection" returned only AEUC p.7, p.21, p.57 | AEUC Section 0 Scope item (1)(b) (utility side only); needs CEC check | $ now |
| ELE-13 | Consider | Parents' house | **The parents' house is a 672 sq ft, 1-bed/1-bath crawl-space house marked "SERVICES: FROM MAIN HOUSE (TBD)"; it is not in site.scad, so no feeder length or route exists.** Planning demand 13.5 kW = **56 A** at 240 V (P-rows below), so a 100 A sub-panel feed would carry it, but it adds to the house service (ELE-02). Decide: separate utility meter and service (own AEUC 2-024 connection) or a feeder from the house. If a feeder, leave a capped conduit and a 2-pole breaker space at the UTILITY panel. Whether a second dwelling may be fed from a first dwelling's service: needs CEC check. | PF §13 (i) (plan images IMG_0415..0420); README:212-215 | AEUC 2-024; needs CEC check | $$ later, $ for a sleeve now |
| ELE-14 | Consider | Exterior doors, stairs, alarms | **Code lighting counts the model does not show:** 11 exterior entrance door sets (D101, D112, D113, D114, D115, D116, D122, D131, D137, D139, DB01; sidelights D138/D140 excluded) each need an exterior lighting outlet with a wall switch inside; the main stair (22 risers, PF §10.1) needs 3-way switching at head and foot and must be lighted; basement exit stair and light-wells need their own lighting. Smoke alarms need permanent connection to an electrical circuit. The 11 entrances and a full-house alarm layout belong in the electrical drawings. | `doors.csv` (exterior marks); PF §10.1; ABC 2023 9.34.2.1, 9.34.2.3, 9.10.19.4 | ABC 2023 9.34.2.1; 9.34.2.3.(2); 9.10.19.4.(1) | $ |
| ELE-15 | Consider | Land-dependent: is there grid power at all | ABC 9.34.1.2 requires electrical facilities "where electrical services are available". On rural land the distance from the road transformer or pole to the lot, line-extension cost, and whether the service is overhead or underground are all unknown. The model assumes 197.3 ft of customer-side underground run (road edge y = -100 up x = -44 to y = 46, then east to x = 7.27). Voltage drop on that run, 2 x 197.3 ft = 60.1 m one way, at 400 A: Cu 2 x 500 kcmil per leg (506.8 mm2): R = 1.72e-8 / 5.068e-4 = 3.39e-5 ohm/m; V = 2 x 60.1 x 400 x 3.39e-5 = **1.63 V = 0.68 %**. Al 2 x 600 kcmil (608 mm2): R = 4.64e-5; V = 2.23 V = **0.93 %**. Whether this run is owned by the utility or the customer is a distributor matter (not in library). | PF §12.2 (197.3 ft); `site.scad:162-164`; arithmetic `vd.py` | ABC 2023 9.34.1.2; AEUC 2-024 | unknown |

## Load table (planning; every number is an assumption of mine unless sourced)

Voltage 240 V single-phase, I = kW x 1000 / 240. Coincidence factor (CF) is my planning factor, **not a CEC demand factor** (needs CEC check). Case A = heating, DHW, pool and spa are fuel-fired (only electrical auxiliaries). Case B = all-electric.

### House (areas: main 5 486.2 + basement 3 475.0 = 8 961.2 sq ft, PF §1.1)

| Row | Load and arithmetic | Conn. kW A | Conn. kW B | CF | Demand kW A | Demand kW B |
|---|---|---|---|---|---|---|
| H1 | General lighting and receptacles: 8 961.2 sq ft x 2 W/sq ft = 17 922 W | 17.92 | 17.92 | 0.5 | 8.96 | 8.96 |
| H2 | Range 12 + second oven 4 (K-111, K-268) | 16.00 | 16.00 | 0.4 | 6.40 | 6.40 |
| H3 | Dishwasher 1.5 + microwave 1.5 + 2 fridge/freezers x 0.5 | 4.00 | 4.00 | 0.5 | 2.00 | 2.00 |
| H4 | Laundry: dryer 5 + washer 0.5 | 5.50 | 5.50 | 0.5 | 2.75 | 2.75 |
| H5 | Fuel-fired heat auxiliaries: air handler blower, boiler circulators | 1.50 | 1.50 | 1.0 | 1.50 | 1.50 |
| H6 | Electric heat bounding: 100 000 BTU/h / 3 412 = 29.31 kW (case B only) | 0.00 | 29.31 | 1.0 | 0.00 | 29.31 |
| H7 | DHW: electric 4.5 kW tank (B), gas aux 0.2 (A) | 0.20 | 4.50 | 0.5 | 0.10 | 2.25 |
| H8 | HRV 0.3 + water treatment 0.2 + radon fan 0.1 | 0.60 | 0.60 | 1.0 | 0.60 | 0.60 |
| H9 | Well pump 1 hp, 1.1 kW assumed | 1.10 | 1.10 | 1.0 | 1.10 | 1.10 |
| H10 | Two sumps x 0.5 + effluent pump 0.75 = 1.75 | 1.75 | 1.75 | 0.5 | 0.88 | 0.88 |
| H11 | Pool circulation 1.5 + 0.5 x (spa jets 2.0 + blower 1.5) = 3.25 | 3.25 | 3.25 | 1.0 | 3.25 | 3.25 |
| H12 | Pool dehumidifier | 3.00 | 3.00 | 1.0 | 3.00 | 3.00 |
| H13 | Pool heater: gas aux 0.3 (A); electric 12.5 kW from 600 kWh / 48 h (B) | 0.30 | 12.50 | 1.0 | 0.30 | 12.50 |
| H14 | Spa heater: gas aux 0.3 (A); electric 5.5 (B) | 0.30 | 5.50 | 0.5 | 0.15 | 2.75 |
| H15 | Pool/spa lights, salt cell, controls | 0.80 | 0.80 | 1.0 | 0.80 | 0.80 |
| H16 | Theatre/AV/music 2.0 + network 0.5 | 2.50 | 2.50 | 0.5 | 1.25 | 1.25 |
| H17 | Garage electric unit heater (hydronic alternative removes it) | 5.00 | 5.00 | 0.5 | 2.50 | 2.50 |
| H18 | EV charger 40 A x 240 V = 9.6 kW (K-311) | 9.60 | 9.60 | 1.0 | 9.60 | 9.60 |
| H19 | Exterior/porch/yard lights: 11 doors x 0.1 + 1.0 | 2.10 | 2.10 | 0.5 | 1.05 | 1.05 |
| H20 | Snow melt: hydronic aux 0.5 (A); electric 200 sq ft x 50 W = 10 kW, steps and walkway (B) (House-Review:886) | 0.50 | 10.00 | 0.3 | 0.15 | 3.00 |
| H21 | Starlink | 0.10 | 0.10 | 1.0 | 0.10 | 0.10 |
| **Total** | Sum of rows | **76.0** | **136.5** | | **46.4** | **95.5** |
| **Amps at 240 V** | Demand: 46.4 x 1 000 / 240 = **193 A** (A); 95.5 x 1 000 / 240 = **398 A** (B). Connected: 76.0 / 0.24 = 317 A; 136.5 / 0.24 = 569 A | | | | 193 A | 398 A |

Not in these totals because the model does not contain them: an electric sauna/steam shower, a second laundry, an elevator (K-058 "leave empty space for elevator?"), heat trace on water lines, and heated driveways (PF §13 (e): absent from models).

### Future shop (fed from the house, case with fuel-fired shop heat; heavy items per Shop-Base-Plan:193-194, 228-240)

| Row | Load and arithmetic | Conn. kW | CF | Demand kW |
|---|---|---|---|---|
| S1 | Lighting: 100 x 100 = 10 000 sq ft x 1 W/sq ft | 10.0 | 0.6 | 6.0 |
| S2 | Welder 10 kW | 10.0 | 0.3 | 3.0 |
| S3 | Air compressor 7.5 hp, about 7 kW | 7.0 | 0.5 | 3.5 |
| S4 | Two lifts x 2.2 | 4.4 | 0.5 | 2.2 |
| S5 | Wash plant: pumps and aux heating | 5.0 | 0.5 | 2.5 |
| S6 | Boiler, in-slab pumps, unit-heater aux | 6.0 | 1.0 | 6.0 |
| S7 | Server, network, battery inverter aux | 2.5 | 1.0 | 2.5 |
| S8 | One truck/EV charger, 80 A x 240 V = 19.2 kW | 19.2 | 1.0 | 19.2 |
| S9 | Receptacles, doors, pit vent fan, misc | 5.0 | 0.5 | 2.5 |
| **Total** | | **69.1** | | **47.4** (= **198 A**) |

### Parents' house (672 sq ft)

| Row | Load and arithmetic | Conn. kW | CF | Demand kW |
|---|---|---|---|---|
| P1 | 672 sq ft x 2 W/sq ft | 1.34 | 0.5 | 0.67 |
| P2 | Range | 8.00 | 0.4 | 3.20 |
| P3 | Dryer 5 + washer 0.5 | 5.50 | 0.5 | 2.75 |
| P4 | Electric DHW | 3.00 | 0.5 | 1.50 |
| P5 | Electric heat bounding: 672 x 25 BTU/h / 3 412 = 4.92 kW | 4.92 | 1.0 | 4.92 |
| P6 | Mechanical/HRV/misc | 0.50 | 1.0 | 0.50 |
| **Total** | | **23.3** | | **13.5** (= **56 A**) |

### Roll-up against service sizes (simple sums, no inter-building diversity)

| Scenario | Arithmetic | Amps |
|---|---|---|
| House A | 46.4 kW / 0.24 | 193 A |
| House B | 95.5 kW / 0.24 | 398 A |
| House A + parents | 193 + 56 | 249 A |
| House A + parents + shop | 193 + 56 + 198 | 447 A |
| House B + parents | 398 + 56 | 454 A |
| House B + parents + shop | 398 + 56 + 198 | 652 A |

A 400 A single-phase service at 240 V is 96 kW. It covers house A + parents, and house B alone; it does not cover house B + parents or anything that includes the shop. **Flag: the full build needs more than 400 A if the shop and parents are on the same service.** Needs CEC check and the distributor's capacity answer.

## Voltage-drop table (single-phase 240 V, V = 2 x L x I x R; assumed resistivities; needs CEC check)

| Run | L | I | Conductor | Cold V (%) | Hot, assumed 80 C V (%) |
|---|---|---|---|---|---|
| Panel to shop (as modelled) | 210 ft = 64.0 m | 200 A | Cu 4/0 | 4.11 V (1.71 %) | 5.08 V (2.12 %) |
| | | | Al 4/0 | 6.74 V (2.81 %) | 8.36 V (3.48 %) |
| | | | Cu 350 kcmil | 2.48 V (1.03 %) | 3.07 V (1.28 %) |
| | | | Al 350 kcmil | 4.07 V (1.70 %) | 5.06 V (2.11 %) |
| Panel to shop (real, ELE-03) | 293 ft = 89.3 m | 200 A | Cu 4/0 | 5.73 V (2.39 %) | 7.08 V (2.95 %) |
| | | | Al 4/0 | 9.40 V (3.92 %) | 11.67 V (4.86 %) |
| | | | Cu 350 kcmil | 3.47 V (1.44 %) | 4.28 V (1.78 %) |
| | | | Al 350 kcmil | 5.68 V (2.37 %) | 7.06 V (2.94 %) |
| | | | Cu 500 kcmil | 2.42 V (1.01 %) | 3.00 V (1.25 %) |
| | | | Al 500 kcmil | 3.98 V (1.66 %) | 4.94 V (2.06 %) |
| Direct route (assumed ~100 ft) | 100 ft = 30.5 m | 200 A | Cu 4/0 | 1.96 V (0.82 %) | 2.42 V (1.01 %) |
| | | | Al 4/0 | 3.21 V (1.34 %) | 3.98 V (1.66 %) |
| Road to meter | 197.3 ft = 60.1 m | 400 A | 2 x 500 kcmil Cu | 1.63 V (0.68 %) | not computed |
| | | | 2 x 600 kcmil Al | 2.23 V (0.93 %) | not computed |

Reading it: in aluminium 4/0 the 293 ft run alone reaches about 3.9 % cold and 4.9 % hot at the full 200 A, and adding the road run (0.7-0.9 %) takes the end-to-end drop above 5 %. A design target of 3 % for a feeder is common practice but that limit is a CEC matter (needs CEC check), so I do not cite it. Real shop demand is 198 A at the very most, and typically less. Upsizing to 350-500 kcmil or shortening the route both fix it; the route fix is cheaper.

## If the tunnel architecture is reinstated

Not what `main` models (site.scad:33-35; PF §13 (a), (b)). With a ~70 ft heated tunnel and the shop as the service point:

- **Feeder voltage drop, shop switchboard to house panel, 200 A, 240 V.** Tunnel length alone, 70 ft = 21.3 m. Cu 4/0: V = 2 x 21.3 x 200 x 1.604e-4 = **1.37 V = 0.57 %**; Al 4/0: R = 2.63e-4, V = **2.25 V = 0.94 %**; Cu 350 kcmil 0.83 V (0.34 %); Al 350 kcmil 1.36 V (0.57 %). Realistic run, Bay 1 switchboard (inverters/switchgear at x 20..27, shop.scad:146) to the portal at x = 80 (Shop-Base-Plan:96, 184-185), about 55 ft inside Bay 1, plus 70 ft tunnel, plus about 40 ft inside the house = **165 ft** (assumed): Cu 4/0 **3.23 V = 1.34 %**, Al 4/0 **5.29 V = 2.20 %**, Cu 350 kcmil 1.95 V (0.81 %), Al 350 kcmil 3.20 V (1.33 %). Conductor implication: 4/0 aluminium is workable on the 70 ft tunnel alone but borderline on the 165 ft route; 350 kcmil Al or 4/0 Cu is comfortable.
- **Service size.** With the shop as the only service the whole site is on one service: 447 A (case A) to 652 A (case B) by the roll-up above. The Shop-Base-Plan designs the switchboard around a **1 000 A bus** (:227-229) and warns rural single-phase services are often capped well below that (:229-231); that is the key question for the utility. A service of this size is probably a utility-owned padmount transformer; not in the library.
- **Backup.** Both water (well in the shop) and sewage (house lift station) depend on the shop plant (Shop-Base-Plan:261-263), so the generator (50-80 kW class, :258-259) is mandatory, not optional. My critical-load numbers (ELE-07) give 15 to 50 kW for the house alone.
- **Tunnel sharing.** The tunnel carries a 200 A feeder in its own compartment, two fibre conduits, hydronic supply/return, domestic water, a sewage force main and spare conduits (Shop-Base-Plan:364-370). Power-versus-gas-versus-plumbing separation: needs CEC check and needs B149.1 check. Tunnel heating and its freeze alarms must sit on the generator-backed panel.
- **Parents' house** would feed from the shop switchboard with a similar run of about 63 ft or more plus its own route (not modelled).

## plan_facts corrections

1. **PF §12 (phase full): "buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side".** The 210 ft is the length of the drawn polyline (`site.scad:197`: 76 + 130 + 4 = 210); the polyline starts at (-50, 50), which is 72.2 ft west of the basement west wall (x = 22.16) and 57.3 ft west of the bedroom wing wall (x = 7.27). It is not the length from the house. Panel-to-shop is about 293 ft (72.2 + 11.1 + 210).
2. No other correction found; the 14.9 ft (22.16 - 7.27 = 14.89) and 197.3 ft figures reproduce.

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| ELE-01 | `search.py --doc abc_2023 '"9.34.1.1"'` | abc_2023 | 1064 | 9.34.1.1. | Electrical installations, including the service capacity of the installation and the number and distribution of circuits and receptacles, shall conform to the Electrical Code Regulation |
| ELE-02 | `search.py --doc electric_2022 "service connection"` | electric_2022 | 13 | 2-024 | The operator of a utility system shall not connect, or allow to be connected, an electrical consumer’s service to the electrical utility system unless: |
| ELE-02 | `search.py --doc electric_2022 "metering"` | electric_2022 | 14 | 2-024 | (b) the metering equipment and location are acceptable; |
| ELE-02 | `search.py --doc electric_2022 "service connection"` | electric_2022 | 14 | 2-024 | (d) the operator of the utility system has received a copy of a valid permit or authorization issued by the consumer’s authority having jurisdiction |
| ELE-04 | `search.py --doc electric_2022 "underground service"` | electric_2022 | 13 | 2-020 | Before an excavation is started, the person responsible for the excavation shall contact the operator of the underground cables in the area |
| ELE-04 | `search.py --doc electric_2022 "underground service"` | electric_2022 | 13 | 2-020 | no excavations are undertaken within 1 m of any underground utility cable unless |
| ELE-05 | `search.py --doc electric_2022 "metering"` | electric_2022 | 14 | 2-024 | (b) the metering equipment and location are acceptable; |
| ELE-12 | `search.py --doc electric_2022 "generation facilities interconnection"` | electric_2022 | 7 | Scope | the portion of generation facilities that are used to provide inter-connection to an electrical utility system up to the demarcation point |
| ELE-12 | `search.py --doc electric_2022 "generation facilities interconnection"` | electric_2022 | 7 | Scope | electrical utility systems that are used to transform, transmit, distribute, and deliver electrical power or energy to consumers’ services |
| ELE-14 | `search.py --doc abc_2023 '"9.34.2.1"'` | abc_2023 | 1065 | 9.34.2.1. | An exterior lighting outlet with fixture controlled by a wall switch located within the building shall be provided at every entrance to buildings of residential occupancy. |
| ELE-14 | `search.py --doc abc_2023 '"9.34.2.3"'` | abc_2023 | 1065 | 9.34.2.3. | 3-way wall switches located at the head and foot of every stairway shall be provided |
| ELE-14 | `search.py --doc abc_2023 '"9.10.19.4"'` | abc_2023 | 909 | 9.10.19.4. | be installed with permanent connections to an electrical circuit |
| ELE-15 | `search.py --doc abc_2023 '"9.34.1.2"'` | abc_2023 | 1064 | 9.34.1.2. | Where electrical services are available, electrical facilities shall be provided for every building in conformance with this Section. |
