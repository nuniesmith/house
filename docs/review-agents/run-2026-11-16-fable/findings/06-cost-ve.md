# 06 Cost / Value-engineering findings (COST)

- Specialist: Cost/VE (Sonnet 5.5), prefix COST, date 2026-11-16.
- Inputs read: COMMON-RULES, SPECIALIST-FORMAT, brief 06; PF-V12, PF-V2, PF-V3, PF-ALT, PF-COMPARE (all sections); kayla_checklist.md (K-006, K-010, K-023, K-058, K-032, K-034 and the rest of the list); findings 01-architecture-flow, 02-structural, 03-plumbing-septic, 04-electrical, and 05-gas-hvac (05 WAS available when I reached that step and was read in full for the Should-fix list and the heat-volume numbers). Household brief docs/review-agents/agents/cost-ve.md.
- Repo price sources used (the only dollar figures in this file), cited by file:line:
  - `docs/house/House-Review-and-Research-2026-10-28.md` (HR) line 321: ICF basement wall planning allowance **$35-50 per sq ft of wall** (published range lines 316-319: $20-30 Winnipeg, $38-48 Ontario). Line 352: ICF "changes after the pour are expensive". Line 358: ICF above grade +$5-15/sq ft of floor area (HomeStars Alberta), about 3-5% of build cost (Fox Blocks). Line 432: standard window installed (Calgary) $500-$1,000; line 436: triple-pane premium +15-25% per unit, +$120-$350 per window; line 437: 60x48 picture window $700-$1,200. Lines 792/795: ground-source heat pump $25-45K for a typical 3-5 ton Alberta home; $70-140K+ UNVERIFIED for the large SCAD house (not these sets). Line 865: hydronic snow-melt $45-95/sq ft (driveway only).
  - `docs/house/House-Plan-Review-2026-11-09.md` line 151 (porch/deck floor structure for 2,221 sf rated $$), line 204 and 277 (an elevator shaft is $$-$$$).
  - `docs/layout-options/round-3/review/r3-plumbing-mech-cost.md` line 57: earlier runs priced ICF wall as perimeter x 10.125 ft (other options) and x 12.125 ft (the SCAD house today); `docs/layout-options/round-3/DECISION-PACK.md` line 101 shows the same $35-50 method.
  - Nothing in the repo prices: build cost per sq ft of house, roof, framing, finishes, septic, mechanical plant for these sets, garage, terraces, doors, partitions. Those are "needs a quote" or $/$$/$$$ only.
- **Perimeter method (mine, not in any PF):** the sets print no overall dimension, so I traced the heated outline on each Rooms sheet by image processing (`$RUN/work/COST/perim.py`, scale 15.5 / 13.06 / 15.28 px/ft for V1-2/V2/V3 from the PF headers, 11.44 px/ft for ALT p.2 per PF-ALT header; garage rectangle cut out; terraces excluded; region smoothed with a 21-px open/close). Result is the outer-wall perimeter of the heated block. **Uncertainty about +/- 10%** (scale bias of PF about -3%, wall-edge reading, smoothing). Traced gross footprint checks against net printed area (+8 to +13%, the wall thickness), which is a sanity test of the trace. The line along the garage party wall IS counted (a basement wall is needed there if the garage is slab on grade).
- Assumptions stated: full ICF basement under the heated footprint only (not under the garage; not drawn in any set); wall height not drawn, so a bracket: 8.0 ft (my assumption, low) and 10.125 ft (the repo's round-3 figure, r3-plumbing-mech-cost.md:57). All $ ranges below are the repo's $35-50 per sq ft of wall x perimeter x height. Excludes excavation, footings, waterproofing, slab, backfill (HR:312, "typically excluding"); HR:321 says a complete foundation runs 1.8-2.2x the wall cost, "unverified for this scale".
- Scope: not a budget. See section 5 for what these sets cannot price. Structural and gas items are review items for licensed Alberta professionals.

## 1. Findings (sorted by severity, then plan)

| # | Severity | Plan | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| COST-01 | Should fix | All | Basement ICF wall under the heated footprint (the one driver the repo can price) | Heated outer perimeter, traced: V1-2 about 340 ft, V2 about 378, V3 about 378, ALT about 386 (+/- 10%). At the repo's $35-50/sq ft that is the ranges in table 3: at 10.125 ft wall V1-2 $120-172K, V2 $134-191K, V3 $134-192K, ALT $137-195K; at 8 ft wall $95-136K / $106-151K / $106-151K / $108-154K. V1-2 is cheapest on every assumption; V2 and V3 add about +$14-19K, ALT about +$17-23K (10.125 ft case; 8 ft case +$11-15K and +$13-18K). **The brief's expectation that ALT's narrow wing costs more per sq ft is NOT supported:** ALT's perimeter per net heated ft2 is the lowest (0.080 ft per ft2 against 0.090 / 0.092 / 0.088), because the 32 x 55 ft wing is fat enough and the main block is a plain rectangle. ALT costs more in total only because it is 1,062 ft2 bigger (+28%). The 120 in ceilings force an engineered ICF design (STR-01) that nobody has priced. | PF-COMPARE §3 (net areas); perim.py trace on v12 p.3, v2 p.3, v3 p.3, alt p.2; HR:321; r3-plumbing-mech-cost.md:57; STR-01 | - | $$$ (ranges as stated; needs a quote) |
| COST-02 | Should fix | V2, V3, ALT | Net heated area and heated volume | Every alternative is bigger than the baseline: net heated 4204.55 (V2, includes 78.04 ft2 room 15 inside the garage walls; 4126.51 without it), 4278.07 (V3), 4825.80 (ALT) against 3763.34 (V1-2): +441.21 (+11.7%), +514.73 (+13.7%), +1062.46 (+28.2%). Heated volume (HVAC-08): 37,633 / 42,046 / 42,781 / 42,749 ft3, so ALT's 106.3 in ceilings cut its volume premium to +13.6% (V3 +13.7%, V2 +11.7%). Area drives basement footprint, floor, roof, finishes, plant size and lifetime heating. Repo has no $/ft2 for the house, so no dollar figure: unknown, but this is the largest lever after the ICF wall and it favours V1-2. | PF-COMPARE §3; HVAC-08 (05-gas-hvac.md) | - | $$$ (unknown, needs a quote) |
| COST-03 | Should fix | V2, ALT | Garage (V2 room 1 1111.92 ft2, ALT room 1 1199.86 ft2) | Garage area: V1-2 and V3 988.03 ft2 (28 x 40 ft outer), V2 1111.92 (32 x 42 ft outer, +123.89 = +12.5%), ALT 1199.86 (32 x 42 ft outer, +211.83 = +21.4%). All four draw three bays. V2 and ALT also carry three 108 in doors with piers of 15 in (V2) or 35-42 in (ALT) and a 12.19 m inside length against the 12.2 m Part 9 cap (STR-05, STR-06); V1-2 and V3 carry a 220 in door header past the lintel table (STR-04). Each garage therefore has an engineered-structure item; V2 and ALT are the biggest slabs and roofs. | PF-COMPARE §2 (garage outer 1120.0 / 1344.0 / 1120.0 / 1344.4 ft2); STR-04, STR-05, STR-06 | - | $$ (unknown; structure items $$ per STR) |
| COST-04 | Should fix | V2, ALT, V3 | Terraces: V2 3419.08 ft2, ALT 2708.66, V3 2049.26, V1-2 1575.32 | Terrace area is 2.17x (V2), 1.72x (ALT), 1.30x (V3) the baseline (PF-COMPARE §2). V2's south terrace alone is 2797.78 ft2 with posts drawn on its edge; ALT has five separate terraces and no "Support post" in its legend. No sheet shows a roof or cover, so K-023 (covered BBQ) is not met or contradicted. Even uncovered, each needs a structural floor/footing system (STR-16; the repo rates 2,221 sf of porch/deck structure in another model $$, House-Plan-Review-2026-11-09.md:151). Covered, it also needs roof, beams and posts. The repo has no $/ft2 for terraces; snow-melt ($45-95/sq ft, HR:865) is NOT assumed for terraces. | PF-COMPARE §2; STR-16; K-023 | - | $$ to $$$ (unknown; uncovered vs covered not shown) |
| COST-05 | Should fix | All | Fix-now vs fix-later: the "tear out finished work" items | The expensive-later items are the ones that sit under or inside the structure: ICF wall height/engineering (STR-01), interior beam lines and posts in the basement (STR-07), stair floor opening (STR-11), elevator shaft and pit (STR-12), basement drains, sump and radon vent under the slab (PLB-03), long buried drains and cleanouts (PLB-05), conduit stubs to garage bays and elevator (ELE-06, ELE-07), plant/flue/hood/dryer duct chases (HVAC-01, 03, 05). Poured ICF "changes after the pour are expensive" (HR:352); a future shaft is $$-$$$ (House-Plan-Review:204). Paper cost of each is $ to $$ (drawing, engineer); after framing or a poured slab it is $$ to $$$. See table 4 for every Blocker and Should fix. | STR-01, 07, 11, 12; PLB-03, 05; ELE-06, 07; HVAC-01, 03, 05; HR:352 | - | $ now vs $$-$$$ later |
| COST-06 | Should fix | V2, V3, ALT | Plumbing spread and septic size | Largest gap between plumbing groups: V1-2 about 30 ft, V2 about 40, V3 about 55, ALT 80+ ft; groups 4 / 5 / 4 / 5; fixture units 27 / 41.5 / 35 / 37.5 (PLB table). Peak daily septic flow 1,630 / 2,355 / 2,030 / 2,515 L per day (PLB-08, PLB-09): V2 is 44% and ALT 54% above V1-2, which means a larger tank and field. V2 draws 5 WC rooms (V1-2: 3). K-006 (group wet walls) is IN only for V1-2. The repo has no septic or drain-run prices: needs a quote. Direction: V1-2 cheapest, ALT dearest (PLB-04 rates V2/V3 $$ and ALT $$$). | PF-COMPARE §7; PLB-04, PLB-06, PLB-08, PLB-09; K-006 | - | $$ (V2, V3), $$$ (ALT); needs a quote |
| COST-07 | Should fix | V2, V3 | Kitchen/dining versions against V1-2 (see table 6) | V1-2 keeps kitchen and dining as one 616.78 ft2 room with 3 hall doors (48+48+60) - the cheapest partition set. V2 splits it into four walled rooms (kitchen+nook 636.15, scullery 132.83, dining 284.71, entry 219.69) with 46 door-type labels (+3), a 5-panel hall glass wall (419.2 in, STR-09), a garage-side WC room 27 and a toilet room inside the garage (room 15), and a south terrace 2.9x the baseline. V3 walls kitchen, mudroom, pantry and WC room behind a living room with no window (571.46 ft2, 43 labels, same as V1-2) and a 55 ft kitchen-to-laundry plumbing gap. Direction against V1-2: V2 more cost ($$), V3 more cost ($ to $$); neither saves anything. | PF-COMPARE §4, §5, §7; PF-V2 §3, §7; PF-V3 §3, §7; STR-09 | - | $$ (V2), $ to $$ (V3) |
| COST-08 | Consider | All | Ceiling height 120 in (V1-2, V2, V3) against 106.3 in (ALT) | A 120 in ceiling is 3.05 m; the prescriptive ICF wall stops at 3 m floor-to-floor (STR-01 Blocker) so V1-2/V2/V3 need an engineered ICF wall, and ALT (2.70 m) is close to the line (STR-02). 120 in also adds 13.7 in of wall height, drywall and heated volume on every wall: ALT at 106.3 in houses 28% more floor in only +13.6% volume. Dropping V1-2/V2/V3 to a lower ceiling might bring them under 3 m floor-to-floor, but floor depth is not shown, so that is for the engineer. Direction: lower ceiling is cheaper in walls, finishes, volume and possibly foundation; costs room volume. | PF-COMPARE §2; STR-01, STR-02; HVAC-08 | - | $$ (unknown) |
| COST-09 | Consider | All | Windows and glazed units | p.1 window-type labels: 23 / 22 / 22 / 18 (V1-2 / V2 / V3 / ALT; PF-COMPARE §5). At the repo's installed $500-$1,000 per standard window (HR:432) those labels alone are about $11.5-23K (V1-2), $11-22K (V2, V3), $9-18K (ALT); the labels undercount (PF-ALT §4 and §12: p.1 prints fewer than the elevations show) and exclude glazed doors, sliders and bays. Triple pane adds +15-25% (HR:436). Big-glass items: V1-2 sunroom has about 155 ft2 of 98.4 in-high glazing, at least 64% of its two exterior walls (HVAC-07); ALT sunroom 269.42 ft2 with two 126 in glazed doors, and a 203.2 in living-room opening that needs an engineered header (STR-03); V2 dining has 3 exterior windows plus a 72 in slider, V3 two sliders 72.1 and 94.5. Window widths are mostly not dimensioned, so no area total can be summed. | PF-COMPARE §5; PF-ALT §4; HVAC-07; STR-03; HR:432, HR:436, HR:437 | - | $$ (labels x HR:432 range as a floor; needs a quote) |
| COST-10 | Consider | All | Wasted-space audit (see table 7) | Circulation: V1-2 hall 379.54 ft2 = 10.1%, with vestibule 11.1%; V2 9.0% (10.0%); V3 8.9% (9.8%); ALT halls 7.6%, with the 380.29 ft2 foyer (includes the stair) 15.5%. V1-2/V2/V3 each hold 74.07 ft2 in six rooms under 20 ft2 (19.38, 19.05, 15.18, 13.35, 6.89, 0.22) and 58.24 ft2 in two pure passage rooms (38.86 + 19.38). ALT has 21.74 ft2 in two open-niche closets. No $/ft2 is in the repo, so every 100 ft2 of low-value space is a "build + heating" cost I cannot price: unknown. V1-2's hall is the largest circulation share (ARC-10). | PF-COMPARE §3; PF-V12 §2; ARC-10, ARC-11, ARC-24 | - | unknown (ft2 and % given; needs a quote) |
| COST-11 | Consider | All | K-010 two-foot increments (examples in table 8) | Metric-derived sizes sit off the 2-ft grid in every set: openings 82.7, 98.4, 88.6, 47.2, 94.5, 31.5, 59.1 in; V1-2/V2/V3 master top wall outer 348.0 in (29.0 ft); ALT wing outer 386.0 in (32.17 ft); ALT ceiling 106.3 in (8 ft 10.3 in); interior chains like 205.9, 326.0, 151.0, 117.3 x 177.5 in. Many are already on the grid: garage outer 336 x 480 in (28 x 40 ft, V1-2/V3) and 384 x 504 in (32 x 42 ft, V2/ALT), 144 x 144 in rooms, 96 / 72 / 60 / 48 / 36 in doors and a 120 in ceiling. Keeping metric sizes costs offcuts, non-standard doors and windows and odd cabinet and truss modules; redrawing means re-dimensioning every wall chain (no repo number for either). It is cheap now on paper ($) and costly after framing or after custom windows are ordered ($$). Not a plan defect; the printed chains cannot show stock-size waste. | PF-V12 §3, §1; PF-V2 §1; PF-ALT §1; K-010 (scored N/S by ARC) | - | $ now; $$ after framing (needs a quote) |
| COST-12 | Consider | All | Elevator closet (K-058): 45.21 / 44.24 / 44.24 / 34.12 ft2 | The closet space is cheap now; the shaft, pit and a floor opening are not drawn (STR-12) and the repo rates a shaft $$-$$$ (House-Plan-Review:204). Framing the opening and stubbing power and conduit now is $; cutting a finished floor and digging a pit later is $$ to $$$. ALT's 34.12 ft2 is 10-11 ft2 smaller and is entered only from the Utility (ELE-07); whether any elevator fits is a supplier question. | PF-COMPARE §4; STR-12; ELE-07 | needs elevator code check (not in library) | $ now; $$-$$$ later |
| COST-13 | Consider | V1-2, V2, V3, ALT | Gold-plating hunt (see table 9): judgement calls for Jordan and Kayla | Largest items beyond a daily-use baseline, by plan: ALT living room 790.08 ft2 (16.4% of net) and ALT library + office + sunroom = 746.69 ft2 (K-032 and K-034 ask for a library and sunroom, so these are Kayla's, not waste); V3 living 571.46 ft2 with no window; V2/V3 sunroom-position rooms 186.11 / 223.14 ft2 that do not meet K-034 (ARC-08); master wing V1-2/V2/V3: two walk-in closets 72.01 + 63.94 plus a 113.88 ft2 dressing area = 249.83 ft2 (ALT two WICs 106.24); three-bay garages in all four; V2 terrace 3419 ft2 and a toilet-and-sink room inside the garage (78.04 ft2); ALT foyer 380.29 ft2. None is an Alberta requirement. | PF-COMPARE §3, §4, §10; ARC-08 | - | $$ to $$$ (unknown) |
| COST-14 | Consider | V1-2, ALT | Heated sunroom glass | Glass drives both capital and winter loss: V1-2's 147.04 ft2 sunroom is at least 64% glazed on two walls (HVAC-07); ALT's 269.42 ft2 is glazed on two sides. K-185 (full walls of glass) is IN for both; its cost is a glazing-package and heating-load question the code treats per orientation, and no north arrow is printed (HVAC-09). Triple pane +15-25% (HR:436) is the repo's only price lever. | HVAC-07, HVAC-09; PF-V12 §3; PF-ALT §3 | - | $$ |
| COST-15 | Consider | ALT | Utility room 129.17 ft2 (ALT room 19) | The only labelled mechanical room: no equipment drawn, no exterior wall, four doors (HVAC-02), so it is a thoroughfare, not a plant room. V1-2/V2/V3 put the plant in the basement under the stair. Either way the plant room is not priced anywhere. ALT also has the longest plumbing and duct runs (COST-06, HVAC-11). | HVAC-02, HVAC-11; PF-ALT §2, §6 | needs B149.1 check | $$ |
| COST-16 | Consider | All | What these sets cannot price (see section 5) | Roof, foundation below the main floor, mechanical, electrical, finishes, site work, well, septic, tunnel and shop are not in any sheet. Ranking in this file is a ranking, not a budget. | PF-COMPARE "Not in set" row | - | unknown |

## 2. Cost-driver comparison table (driver x plan x what moves it)

Ranking per plan, first to last, by my read of the size of the lever (the only dollar-ranged item is the basement wall): V1-2: net area/volume, basement wall, 28 corners and the bay, garage header, terraces. V2: net area, basement wall, terraces 3419 ft2, garage 1112 ft2, corners (~32), plumbing spread/septic. V3: net area/volume, basement wall, plumbing spread (55 ft), garage header, terraces. ALT: net area, basement wall, garage 1200 ft2, plumbing spread (80+ ft), terraces, 4 bedrooms (septic).

| Driver | V1-2 | V2 | V3 | ALT | What moves it |
|---|---|---|---|---|---|
| Net heated interior, ft2 (PF-COMPARE §3) | 3763.34 | 4204.55 (4126.51 without room 15) | 4278.07 | 4825.80 | Cut or merge rooms; $$$ |
| Heated volume, ft3 (HVAC-08) | 37,633 | 42,046 | 42,781 | 42,749 | Ceiling height (ALT 106.3 in); $$$ |
| Gross heated footprint, my trace, ft2 | about 4,136 | about 4,499 | about 4,632 | about 5,465 | Same as area; +8 to +13% over net is wall thickness; $$$ |
| Heated outer perimeter, my trace, ft (+/- 10%) | about 340 | about 378 | about 378 | about 386 | Simpler outline; drives basement wall and envelope; $$$ |
| Perimeter per net ft2 | 0.090 | 0.092 (0.092 without room 15) | 0.088 | 0.080 | ALT's fat wing and plain block help; $ |
| Outside corners (PF-V12 §1 / PF-V2 §1 / STR-14) | about 28 | about 32 | about 16 (STR trace; PF did not count) | about 12-14 (STR trace; PF 10-12) | Remove bays and notches; $ to $$ |
| Garage ft2 / outer / doors | 988.03 / 28 x 40 ft / 2 doors (220 + 118.1 in) | 1111.92 / 32 x 42 ft / 3 x 108 in | 988.03 / 28 x 40 ft / 2 doors | 1199.86 / 32 x 42 ft / 3 x 108 in | Bay count and depth; $$ |
| Terraces total, ft2 (roof not shown) | 1575.32 | 3419.08 | 2049.26 | 2708.66 (5 areas) | Shrink or leave uncovered; $$ to $$$ |
| Window-type labels, p.1 (PF-COMPARE §5) | 23 | 22 | 22 | 18 | Fewer, grouped units; HR:432 $500-1,000 each; $$ |
| Door-type labels, p.1 | 43 | 46 | 43 | 41 | Open vs walled kitchen/dining; $ |
| Big glazed units | sunroom ~155 ft2 glass | sliders 72.0 x2, hall glass wall 419.2 in | sliders 72.1, 94.5 | 203.2 in opening, 126 in x2 | Orientation, triple pane (HR:436); $$ |
| WC rooms / plumbing groups / largest gap | 3 / 4 / about 30 ft | 5 / 5 / about 40 ft | 4 / 4 / about 55 ft | 4 / 5 / 80+ ft | Group wet walls (K-006); $$ (ALT $$$) |
| Septic design flow, L/day (PLB) | 1,630 | 2,355 | 2,030 | 2,515 | Bedroom count, fixture units; $$ |
| Ceiling height | 120.0 in | 120.0 in | 120.0 in | 106.3 in | Ceiling height; $$ |
| Elevator closet, ft2 | 45.21 | 44.24 | 44.24 | 34.12 | Frame now, fit later; $ to $$$ |
| Roof, foundation depth, mechanical | not shown | not shown | not shown | not shown | Unpriceable here |

## 3. Basement-wall range table (ICF, wall only)

Formula: perimeter (my trace, +/- 10%) x wall height x $35-50 per sq ft (HR:321). Heights: 8.0 ft is my low assumption; 10.125 ft is the repo's round-3 figure (r3-plumbing-mech-cost.md:57). Garage not included (assumed not over a basement; nothing is shown). Excludes excavation, footings, waterproofing, slab, backfill, wall engineering. +/- 10% perimeter widens each range to about -10% / +10%.

| Plan | Perimeter, ft | Wall area at 8.0 ft, sq ft | $ at 8.0 ft | Wall area at 10.125 ft, sq ft | $ at 10.125 ft | With perimeter +/- 10% at 10.125 ft |
|---|---|---|---|---|---|---|
| V1-2 | 339.7 | 2,718 | $95-136K | 3,439 | $120-172K | $108-189K |
| V2 | 377.6 | 3,021 | $106-151K | 3,823 | $134-191K | $120-210K |
| V3 | 378.3 | 3,026 | $106-151K | 3,830 | $134-192K | $121-211K |
| ALT | 385.7 | 3,086 | $108-154K | 3,905 | $137-195K | $123-215K |

- Difference against V1-2 (10.125 ft): V2 +$14-19K, V3 +$14-20K, ALT +$17-23K. At 8.0 ft: V2 +$11-15K, V3 +$11-15K, ALT +$13-18K. These deltas are smaller than the trace error on any one plan, so treat the ordering V1-2 < V2 about V3 < ALT as firm and the gaps as approximate.
- ALT's narrow-wing premise: perimeter per net heated ft2 is 0.080, the lowest (V1-2 0.090). The wing's 386.0 in outer width is not penalised by perimeter; its issues are spans (STR-08), plumbing length (PLB-04) and the unexcavated question (STR-17), not basement wall per ft2.
- Whole-foundation multiplier: HR:321 quotes 1.8-2.2x the wall cost for excavation, footings, waterproofing, slab and backfill, "unverified for this scale"; I do not apply it.

## 4. Fix on paper now vs after framing, for every Blocker and Should fix in 01-05

Symbols are $ / $$ / $$$ (relative). "Tear-out" = work already built or poured has to be demolished. No dollars; repo prices only where cited.

**All plans**

| Finding | Fix on paper now | Fix after framing / pour | Tear-out? |
|---|---|---|---|
| STR-01 (Blocker) ICF over 3 m floor-to-floor, V1-2/V2/V3; STR-02 ALT near the limit | $ to $$ engineer, or change ceiling/floor depth on paper | $$$ a poured ICF wall "changes after the pour are expensive" (HR:352) | yes, poured wall |
| STR-07 basement beam lines; STR-08 roof spans; STR-13 missing sheets | $ to $$ (engineer, drafting) | $$ posts and beams in a finished basement; trusses re-ordered | yes if basement is finished |
| STR-11 stair opening and trimmers; STR-12 elevator shaft | $ | $$ (stair), $$-$$$ (shaft, HPR:204) | yes, cut floor and slab |
| STR-17/ARC-25 basement layout | $ | $$ | yes |
| PLB-03 basement drains, sump, radon vent; PLB-05 long drains | $ | $$ cut slab, buried cleanouts | yes |
| PLB-04 wet-wall spread (K-006); PLB-12 septic siting; PLB-08/09 bedroom count | $ (move rooms, count bedrooms) | $$ longer runs; resite tank/field; bigger field | no, but re-dig |
| ELE-01..06, 08, 09 service, panel, stubs, circuits | $ | $$ through finished slab or walls | yes, minor |
| HVAC-01, 03, 04, 05, 08, 09, 12 plant, flue, hoods, fans, dryer duct, orientation | $ | $$ chases through finished framing | yes, minor |
| ARC-09 wide doors and halls (Consider but K-003/K-061) | $ | $$ widen openings | yes |

**V1-2, V2, V3**

| Finding | Fix on paper now | Fix after framing / pour | Tear-out? |
|---|---|---|---|
| ARC-04 master closets only via bath (K-333) | $ to $$ | $$ rebuild partitions and finished closets | yes |
| ARC-05 closets on exterior walls (K-070/K-331) | $ to $$ | $$$ re-plan wing | yes |
| STR-04 220 in garage header (V1-2, V3) | $ to $$ | $$ swap header under a loaded roof | yes |
| PLB-08 septic bedroom count | $ | $$ | no |

**V2, V3**

| Finding | Fix on paper now | Fix after framing / pour | Tear-out? |
|---|---|---|---|
| ARC-01 garage entry has no hall door | $ to $$ | $$ cut a wall that may bear | yes |
| ARC-03 no Costco door | $ | $ to $$ | yes, small |
| ARC-08 sunroom gone (K-034) | $$ | $$$ add glazed room | yes |
| V3 ARC-02 living room has no window or exterior wall | $$ re-plan | $$$ | yes |
| V2 STR-09 hall 419.2 in glass wall; STR-05/06 garage | $$ | $$ to $$$ | yes |

**ALT**

| Finding | Fix on paper now | Fix after framing / pour | Tear-out? |
|---|---|---|---|
| STR-03 203.2 in opening, 8.13 m living; STR-10 bearing line; STR-05/06 garage | $$ | $$$ | yes |
| PLB-01 tubs on exterior walls (K-074) | $ to $$ | $$ rebuild wet walls | yes |
| PLB-02 / PLB-19 powder-room tub fixture; laundry sink | $ | $ to $$ | minor |
| ARC-06 no bath on kitchen/living side; ARC-07 dining/breakfast without windows | $$ | $$$ new wet group, new openings | yes |
| HVAC-02 utility room not a plant room | $ to $$ | $$ | yes |

## 5. What is unpriceable from these sets

Roof (type, pitch, trusses; no roof plan, STR-08); foundation below the main floor (no basement, foundation or footing sheet; ICF is the household's assumption only); mechanical (plant, ducts or radiant, HRV, water heater: none drawn, HVAC-01); electrical (no sheet, ELE-01); finishes, cabinets, appliances (K-109..K-113 are SPEC); doors, windows and sliders (counts only, no schedule; widths mostly undimensioned); wall assembly and insulation (not stated); well, septic and site work (no site plan, no north arrow); the shop and heated tunnel (not drawn, nothing in these sets to price; the earlier-run argument is in House-Plan-Review-2026-11-09.md:274, not repeated here); elevator; terraces and any roofs over them; furniture. The ICF wall range in table 3 is the only repo-priced item.

## 6. Kitchen/dining versions against V1-2 (what is added or removed)

| Item | V1-2 | V2 | V3 |
|---|---|---|---|
| Kitchen + dining + living arrangement | one 616.78 ft2 kitchen/dining room, living walled with a 48 in opening | kitchen+nook 636.15, scullery 132.83, dining 284.71, living 468.77, entry 219.69, WC room 27 21.21, plus room 15 78.04 in the garage | kitchen 625.28, dining 354.03, living 571.46, mudroom 179.22, pantry 117.87, WC room 30.03 |
| Door-type labels (p.1) | 43 | 46 (+3) | 43 (0) |
| Window-type labels | 23 | 22 (-1) | 22 (-1) |
| Hall-side partition | 3 doors (48 + 48 + 60) | 2 doors (48 + 48) plus a 5-panel glass wall | 2 doors (60 + 63), no hall-kitchen door |
| WC rooms | 3 | 5 | 4 |
| Plumbing groups / largest gap | 4 / about 30 ft | 5 / about 40 ft | 4 / about 55 ft |
| South terrace ft2 | 954.77 | 2797.78 (2.9x) | 1428.71 (1.5x) |
| Direction vs V1-2 | baseline, fewest walls | more walls, glass, plumbing, terrace: $$ up | more walls and a windowless living room: $ to $$ up |

## 7. Wasted-space audit

| Item | V1-2 | V2 | V3 | ALT |
|---|---|---|---|---|
| Hall ft2 and % of net | 379.54, 10.1% | 379.32, 9.0% | 379.43, 8.9% | 229.60 + 137.99 = 367.59, 7.6% |
| Vestibule/foyer + hall | 418.72 (11.1%) | 418.61 (10.0%) | 418.61 (9.8%) | 747.88 (15.5%, foyer includes stair) |
| Rooms under 20 ft2 | 6 rooms, 74.07 ft2 | 6 rooms, 74.07 ft2 | 6 rooms, 74.07 ft2 | 2 rooms, 21.74 ft2 |
| Pure passage rooms (38.86 + 19.38) | 58.24 ft2 | 58.24 ft2 | 58.24 ft2 | none |
| Rooms with no equipment or no clear use | V1-2 room 14 lounge 113.67 | V2 room 15 in garage 78.04 | V3 room 25 inside mudroom 30.03 | Utility 129.17 (no equipment drawn) |

Price: unknown (no repo $/ft2); every ft2 above is also basement-footprint and heated volume.

## 8. K-010 examples by plan

| Plan | On the 2-ft grid | Off the grid (metric-derived) |
|---|---|---|
| V1-2 | garage 336 x 480 in; 144 x 144 in office; doors 36/48/60/96 | master wall outer 348.0 in (29.0 ft), 205.9 in solid wall, 82.7 in doors, 47.2 and 94.5 in openings, 98.4 in glazed |
| V2 | garage 384 x 504 in; 108 in doors | same wing as V1-2; 72.0 in sliders on grid; 82.7 in doors; 163-174 in room chains |
| V3 | garage 336 x 480 in | 357.3 x 230.3, 294.0 x 306.1 in rooms; 72.1 and 94.5 in sliders; 59.1 in window heights |
| ALT | garage 384 x 504 in; 240 x 144 in rooms; 108 in doors | ceiling 106.3 in (8 ft 10.3 in), wing 386.0 in outer, 203.2 in and 126.0 in glazed, 82.7 in doors |

## 9. Gold-plating list (judgement, not requirement)

Items: three-bay garages in all four; ALT living 790.08 ft2; ALT library + office + sunroom 746.69 ft2; V3 living 571.46 ft2; V2 terrace 3419 ft2; two walk-in closets plus dressing area 249.83 ft2 (V1-2/V2/V3); V2 toilet-and-sink room inside the garage; ALT foyer 380.29 ft2. K-032, K-034 and K-185 make the library and sunroom Kayla's own requests, so they are not gold-plating against her list.

## 10. plan_facts corrections

- PF-COMPARE §3: V2 net heated 4204.55 includes room 15 (78.04 ft2, inside the garage walls, heated status not printed); the PF states this, and I used 4126.51 for the V2 per-ft2 perimeter ratio only where marked.
- No PF number was found wrong. Perimeter, gross footprint and the 10.125 ft / 8.0 ft heights are mine and are labelled as such.

## 11. Citation log

No code citations in this file.
