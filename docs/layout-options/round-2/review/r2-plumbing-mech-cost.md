# R2-PMC: plumbing, mechanical and cost (round 2, options D and E)

**Specialist:** R2-PMC (prefix PMC). **Status:** D and E complete; **F pending** (its column is marked "pending"; findings, the comparison table, the verdict and the cost ranking will be rewritten for all three when F lands). **Date:** 2026-11-11.

**Inputs read:** REVIEW-R2.md, ROUND2-BRIEF.md, COMMON-RULES.md; round-1 `04-plumbing-septic.md` (PLB), `06-gas-hvac.md` (GAS), `07-cost-ve.md` (COST); `r2-code-structure.md` (CS, esp. CS-18) and `r2-accessibility-kayla.md` (ACC); both options' scad files, PNGs, matrix, plan_facts, PROS-CONS; `site.scad` (tank, drives); the repo research doc (HR:line).

**Method.** Re-ran `envelope.py`, `plan_facts.py` (`work/R2-PMC/d`, `e`) and `check_layout.py` (D: 29 main rooms / 28 basement, OK; E: 28 / 22, OK). Geometry measured with `work/R2-PMC/pmc.py` (shapely over the audit tables, outside face = centre line + 0.5 ft, same as the matrix). Gas items: "needs B149.1 check". Wiring: "needs CEC check". Prices come only from the repo's ranges (HR:line, or COST-nn); anything else is "no data, needs a quote". No stamped-engineer claims: structural and plumbing layout are review items for a licensed Alberta engineer / plumber / septic designer. Land is not chosen, so soil, frost depth, grade and utility availability are assumptions.

**Counting rule for the septic bedroom count.** A basement bedroom counts as a bedroom. The murphy-bed-ready FLEX / CRAFT room counts as a bedroom for a conservative design, because it has an egress window and a bed footprint (D `basement_d.scad:151`; D also draws it a closet). So both options are **4 bedrooms as drawn (BR 2, primary, BR 3, BR 4) and 5 if the flex room is counted**. I give both.

## 1. Findings

| # | Severity | Option | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| PMC-01 | Should fix | D | Basement UTILITY (x 24.4-35, y 9.6-21.6) | **No vent or combustion-air opening is drawn, and 12.0 ft of the room's west wall (all of it) sits against the garage.** The only free exterior wall is the north wall, 10.6 ft long. The boiler (28.6-30.8, 19.4-21.2) and water heater (31-33, 19-21) are against that north wall, so a short sidewall route exists; the HRV (33-34.6, 10.5-12.5) is 9 ft from it. No crawl space remains (full basement), so the round-1 GAS-01 blocker (every wall faced a crawl space) is gone. What is still missing is the opening itself, drawn above grade: the rim zone is about 2 ft above grade (PLB-04: grade 2 ft below the main floor), and the pantry sits above, so the termination must be placed clear of the pantry wall and the patio edge at x 36 (6 ft away). Same finding as CS-18; this adds the plumbing/mechanical placement. | `basement_d.scad:46-47,123-128`; `base_windows()` `:109-118` has no UTILITY row; pmc.py: west wall 12.0 ft all garage-side, north wall 10.6 ft free; `main_floor_d.scad` PATIO x 36-77.8 | ABC 9.33.5.5 (no combustion-air inlet in a crawl space; not the case here); vent and intake clearances needs B149.1 check | $ (a chase and two terminations; no repo price) |
| PMC-02 | Should fix | E | Basement UTILITY (x 24-32, y 19.5-39) | **Both vent louvres are below grade, and the room's west wall is half garage.** Louvres at (24, 22-25) and (24, 27-30), sill 4 ft, height 2 ft: heads 6 ft above the slab against grade 9.75 ft above it, so 3.75 ft below grade with no well (same as CS-18). The garage runs to y = 27 (27.5 at the outside face), so only y 27.5-39 (11.5 ft) of the 19.5 ft west wall faces open yard; the first louvre faces the garage fill and the second straddles its corner. The air handler (24.6-27.6, 20.5-23.5) and boiler (24.6-26.8, 25-27) are on the garage-side stretch; the water heater (28.5-30.7) and HRV (32-34) are on the free stretch. The north wall (8.0 ft) is free. Fix: take the vents through the rim above grade on the free north/west corner. | `basement_e.scad:94-95,103-107`; `main_floor_e.scad:41` (garage 0-24 x 0-27); pmc.py | ABC 9.33.5.5; clearances needs B149.1 check | $ |
| PMC-03 | Should fix | D | Basement baths to the ejector pit | **The ejector pit is in the far south-west corner (25-27, 10.2-12.2) and the two basement baths are 74 to 109 ft away by plan.** Plan Manhattan from the pit centre (26, 11.2): bath 1 groups 73.5-74.8 ft; bath 2 groups 101.2-109.2 ft (30.8-33.3 m). That is past the 30 m two-way cleanout spacing for NPS 4 (Table 2.4.7.2), so bath 2's under-slab line needs a mid-run cleanout, and at 1 in 100 the fall is 1.0-1.1 ft, so the pit invert has to sit about a foot below bath 2's under-slab invert. Alternatives (each needs a plumber): a second ejector or macerating unit at bath 2 (no data, needs a quote), or move the pit east. **E** has the pit at the north wall (29.5-31.8, 36.2-38.5) and the Jack-and-Jill bath 39.3-45.1 ft away (12-14 m; fall 0.4-0.5 ft), inside the 15 m one-way figure. | pmc.py pit distances; `basement_d.scad:128`, `:130-137`; `basement_e.scad:107` | NPC 2.4.6.3.(1) (drain to a sump); Table 2.4.7.2; NPC 2.4.8.1; Table 2.4.10.6.-C | $ to $$ (second unit: no data, needs a quote) |
| PMC-04 | Consider | D, E | Ejector pit on the plan | **The ejector pit is drawn only as an unlabelled dark rectangle** (D 2.0 x 2.0 ft, lid 0.3 ft high; E 2.3 x 2.3 ft, 0.05 ft high). Neither basement PNG labels it; it is named only in a scad comment and PROS-CONS. Brief item "draw a small ejector/sump spot" is met geometrically, not on the drawing. Add a label, a vent, a cover and a pit size for the plumber. Basement fixture load to size it: D 13 FU (two baths), E 7.5 FU (one bath), by the SOP fixture-unit table. | `basement_d.scad:128`; `basement_e.scad:107`; both `basement_plan_*.png` | NPC 2.4.6.3.(1); SOP FU table p37 | $ |
| PMC-05 | Consider | D, E | Main-floor drains to the septic side | **The matrix drain-run index is measured to a point (22.16, 58) that is open yard in both options, so it overstates the in-building run.** D's nearest heated wall to that point is the pantry/utility corner (24.4, 21.6), 36 ft south; E's bar ends at y 39.5, 18 ft south. With a physical exit (D: utility north wall (30, 22); E: utility north-west corner (24, 39)) the index is **D 485.6 ft (longest group 94.7 ft), E 500.3 ft (longest 95.0 ft)**, a tie, against the matrix's 587.2 (D) and 667.1 ft (E), and 879.4 ft today (747.1 at the alternate exit). At the matrix point, groups over 98 ft (30 m): D 3 of 7 (113.6, 106.3, 105.7), E 4 of 8 (108.6, 103.8, 115.8, 109.6), today 4 of 14 (PLB-11). With the physical exits none exceeds 98 ft, but each long line still needs a cleanout at the exit (2.4.7.1.(6)) and 0.95-1.1 ft of fall at 1 in 100 inside a 1.625 ft floor or a hung basement-ceiling line. The tank (3, 52-64) is west of both houses, so the exit does go the right way. Decide whether the main-floor groups drain by gravity at ceiling level or to the ejector (bigger pit). | plan_facts `9.5` for D and E; pmc.py exit sums; `site.scad:185-188` | NPC 2.4.7.1.(6); Table 2.4.7.2; NPC 2.4.8.1; Table 2.4.10.6.-C | $ (a wash between D and E) |
| PMC-06 | Should fix | E | LAUNDRY (x 53.5-61.5, y 19.5-29) | **The laundry is an interior room with no window; the dryer (53.7-58, 19.7-22.2) is 18.6 ft from the nearest exterior wall.** The shortest route is straight north in the floor-truss space to the rim at y 39 (stair-top landing, x 53.5-58.5), about 17 ft plus a drop and two elbows; south is 19.5 ft through the living room. Dryer duct length limits are not in the library: needs a manufacturer / ABC check. Outlet must be 1,800 mm from any air intake (HRV intake is at the utility, far away). Today's laundry has the same problem (PLB-08: 23.7 ft). **D** is fine: the laundry has a west window and the dryer is 1.8 ft from the west wall. | pmc.py (E 18.6 ft; D 1.8 ft); `main_floor_e.scad:172`, laundry rooms; `main_floor_d.scad:74.0,43.5` window | ABC 9.32.3.13.(4); duct length: no article found in the library | $ (a 17 ft duct and a chase) |
| PMC-07 | Consider | D, E | Septic design flow and tank | **Both options give a lower design flow than today, because the fixture-unit surcharge falls from 55.5 FU to 32.0 (D) and 32.5 (E).** FU by the SOP table (basin 1, shower 1.5, WC 4, kitchen sink 1.5, laundry sink 1.5 + standpipe 2; double vanity = 2 basins per the scad comments; dishwasher not in the table). 4 bedrooms: D 2,040 + 4.0 x 50 = **2,240 L/day**, E 2,040 + 4.5 x 50 = **2,265 L/day**; tank = peak + 400 L x 6 occupants = 4,640 L (D), 4,665 L (E), above Table 4.2.2.2's 4,260 L. 5 bedrooms (flex counted): D 2,550 + 1.0 x 50 = **2,600 L/day**, E 2,550 + 1.5 x 50 = **2,625 L/day**; tank 5,600 L (D), 5,625 L (E), above the table's 5,220 L. Today (PLB-02): 3,055 L/day, tank 4,855 L. Field at the lowest loading rate (9.80 L/m2/d): 229-268 m2 (2,460-2,883 sq ft), against 312 m2 for today's flow and the drawn 3,025 sq ft footprint; fits only on good soil in the 5-bedroom case. A softener adds 15% (D 2,576-2,990, E 2,605-3,019 L/day); D draws a water-treatment box, E draws none. Land-dependent. The two options differ by 25 L/day: no differentiator. | FU count from `plan_facts` 9.1/9.2 and scad comments; PLB-02 | SOP Table 2.2.2.2.A.; SOP Table 2.2.2.2.A. note (FU values, p37 list); SOP 4.2.1.1.; Table 4.2.2.2.; 8.2.1.13.; Table 2.2.2.3. | $ to $$ (tank: no data, needs a quote) |
| PMC-08 | Consider | D, E | Tank setback to the new footprints | **Both clear SOP 4.2.2.1 by a wide margin; two PROS-CONS statements are slightly off.** Tank (x -3..3, y 52-64) to: D heated wall (outside face) **36.5 ft**, D garage 27.1 ft, D basement 36.5 ft, D deck 37.6 ft; E heated wall and basement **24.0 ft**, E garage 24.5 ft. SOP minimum 1 m (3.25 ft); the model's own rule is 3.3 ft. D's PROS-CONS says the nearest heated wall is x 74: it is the pantry/utility corner, 36.5 ft. E's says "25 ft or more": measured 24.0 ft. Neither changes the result. The ejector force main (D from the utility north wall; E from the north wall at y 39) is 40-55 ft to the tank. | pmc.py tank distances; `site.scad:70-73` `septic_tank()`; D PROS-CONS section 9; E PROS-CONS section 9 | SOP 4.2.2.1. | $ |
| PMC-09 | Consider | D, E | Services route to the utility room | **D's utility room has no free west wall, so the services have to wrap the garage; E's reach it directly.** From the west-wall landing the model uses for the service lines (7.27, 48; GAS-02): to D's utility north wall (30, 22) is 48.7 ft by plan; to E's free west wall (24, 33) is 31.7 ft. Water, power and gas lengths differ by about 17 ft each; no repo price. Gas run and meter position: needs B149.1 check. Power feeder: needs CEC check. | pmc.py geometry; GAS-02; `main_floor_d.scad:54`, `main_floor_e.scad:41` | needs B149.1 check; needs CEC check | $ (no data, needs a quote) |
| PMC-10 | Consider | D, E | Hot water | **One water heater in the utility room serves each house; the furthest fixture is 94.7 ft (D) and 83.9 ft (E) away, against 119.8 ft today.** Add 11.75 ft of rise: D 106.5 ft, E 95.7 ft, today 133.6 ft. Using PLB-07's pipe volumes (1/2 in 0.0104 US gal/ft, 3/4 in 0.0231) and 5.7 L/min: D 0.74 min (1/2 in) to 1.63 min (3/4 in) before hot arrives; E 0.66 to 1.47 min; today 0.92 to 2.05 min. The basement fixtures: D's bath 2 is 94.4 ft from the heater, E's Jack-and-Jill 51.3 ft. A recirculation loop or point-of-use heater is still worth pricing for the primary suite (D, in the north-east of the private wing). Heater fuel and size are not in the model: gas needs a B149.1 check. | matrix_d.md / matrix_e.md water-heater rows; PLB-07 | needs B149.1 check | $ |
| PMC-11 | Consider | D, E | Wet-wall grouping and stacking | **Main-floor wet groups fall from 14 to 7 (D) and 8 (E); basement groups from 8 to 4 and 3.** D stacks 3 of 7 main groups within 5 ft of a basement group (the guest bath sits exactly over basement bath 1, 0.0 ft); E stacks 1 of 8 within 5 ft (the master shower/vanity over the Jack-and-Jill, 0.8 ft) and 2 within 10 ft. E's laundry group backs onto the living-room wall (y 19.5) and the powder room is 29.5-34.3 ft from the basement bath. Neither has island plumbing, so round-1 PLB-13's island-vent item no longer applies. Kitchen sink on an exterior wall in both (D south wall 0.4 ft, E north wall 0.5 ft): supplies inside the insulated wall (PLB-14). | matrix rows; plan_facts 9.3/9.4 | NPC 2.3.5.3. (freezing) | $ |
| PMC-12 | Consider | ALL | Hot-tub sunroom (not drawn) | **Neither option draws it.** D lists it as a future addition outside the 3,000 sq ft; E drops it. If added later: spa clearwater may not go to the septic unless the system is designed for it, and a sunroom with a spa needs its own humidity exhaust and dehumidification (ABC 9.32 ventilation; sizing: needs a mechanical designer). | D PROS-CONS section 2 ("sun room and hot-tub sunroom (none; a future addition outside the 3,000)"); E PROS-CONS section 8 | SOP 2.1.2.6. (spa clearwater) | unknown, no data, needs a quote |

*plan_facts note.* Section 9.6 of both `plan_facts_d.md` and `plan_facts_e.md` still prints the water-heater position of today's model ("(30.1, 36.8)", `basement.scad`); the matrix rows are right (D (32.0, 20.0), E (25.7, 29.6)). Not used here.

## 2. Quantities (re-measured; today's model from `envelope.py`)

| Driver | Today | D | E | F |
|---|---|---|---|---|
| Heated main floor, outside face, sq ft | 5,685 | 2,934 | 2,940 | pending |
| Basement footprint, outside face, sq ft | 3,617 | 2,934 | 2,940 | pending |
| Heated envelope perimeter, ft (outside face) | 399.5 | 311.8 | 227.0 | pending |
| Envelope corners (out + in) | 30 (17+13) | 14 (9+5) | 4 (4+0) | pending |
| Basement perimeter, ft | 285.3 | 311.8 | 227.0 | pending |
| ICF wall area, sq ft (perimeter x slab-top-to-main-floor: 12.125 ft today, 10.125 ft D/E) | 3,459 | 3,157 | 2,298 | pending |
| ICF wall area on today's 12.96 ft basis (COST-01) | 3,697 | n/a | n/a | n/a |
| Roof blocks (house + porch) | 16 hip blocks (PF 1.2, COST-08) | 9 (5 house, 4 porch) | 4 (bar ridge, garage, 2 porch) | pending |
| Porch / patio / deck area under roof, sq ft (excl. drive) | 2,221 (COST-10) | 756 | 772 | pending |
| Garage, outside face, sq ft | 892 | 645 | 700 | pending |
| Window rows (main + basement) | 19 (COST-09) | 24 (16 + 8) | 23 (16 + 7) | pending |
| Basement window wells drawn | 0 | 3 | 5 | pending |
| Wet-wall groups (main + basement) | 14 + 8 | 7 + 4 | 8 + 3 | pending |
| Drain-run index at matrix point, ft | 879.4 | 587.2 | 667.1 | pending |
| Drain-run index at a physical exit, ft | 747.1 (alternate) | 485.6 | 500.3 | pending |
| Fixture units (SOP table) | 55.5 | 32.0 | 32.5 | pending |
| Bedrooms for septic (flex not counted / counted) | 3 | 4 / 5 | 4 / 5 | pending |
| Design flow, L/day (flex not counted / counted) | 3,055 | 2,240 / 2,600 | 2,265 / 2,625 | pending |
| Elevator rough-in | none | stacked 6.0 x 7.4 ft, offset 0.0 | stacked 6.0 x 7.4 ft, offset 0.0 | pending |
| Stair | 22 risers, 13.75 ft | 19 risers, one flight, 3,581 mm | 19 risers, one flight | pending |

## 3. Cost: drivers ranked, priced only from the repo

Scale for the table below: "down" = a saving against today's model, "$ / $$ / $$$" = small / medium / large. Dollar figures are the repo's ICF range multiplied by the measured area (the rows marked "computed").

| Rank | Driver | D vs today | E vs today | Repo price |
|---|---|---|---|---|
| 1 | Heated footprint (both levels) | $$$ down (5,685 to 2,934; 3,617 to 2,934) | $$$ down (to 2,940; 2,940) | no whole-house $/sq ft in the repo (COST header) |
| 2 | ICF basement wall | $ down: 3,157 sq ft = $110K-$158K vs $121K-$173K today (**-$10.6K to -$15.2K**, computed, HR:321 $35-50/sq ft) | $$ down: 2,298 sq ft = $80K-$115K (**-$40.7K to -$58.2K**, computed) | HR:321; Winnipeg low end $20-30 (HR:316) would give D $63K-$95K, E $46K-$69K |
| 3 | Whole foundation package at 1.8-2.2x the wall (HR:321, "unverified for this scale") | D $199K-$347K vs $218K-$381K today | E $145K-$253K | computed from HR:321 |
| 4 | Envelope perimeter and corners | $ down (311.8 ft, 14 corners vs 399.5, 30) | $$ down (227.0 ft, 4 corners) | no $/ft in the repo (COST-08) |
| 5 | Roof form | $$ down (9 blocks, 5 inside corners in the L) | $$$ down (one ridge, 4 blocks; but a 39 ft clear span, CS-08) | no data, needs a quote |
| 6 | Porches and patios | $$ down (756 sq ft) | $$ down (772 sq ft) | no data, needs a quote |
| 7 | Windows | $ up (24 rows vs 19) | $ up (23 rows vs 19) | HR:434 $850-$1,600 each: D $20.4K-$38.4K, E $19.6K-$36.8K vs $16.2K-$30.4K today (computed; egress rows and wells are priced separately: no data) |
| 8 | Plumbing groups and runs | $$ down (11 groups vs 22; longer ejector run to bath 2, PMC-03) | $$ down (11 groups vs 22) | no data, needs a quote |
| 9 | Elevator rough-in (stacked shaft, pit in the basement slab) | $ up, same in both | $ up, same | no repo price |
| 10 | Straight stair | no difference | no difference | no repo price |
| 11 | Utility venting and services | $ (PMC-01, PMC-09: +17 ft of services) | $ (PMC-02) | no data, needs a quote |
| 12 | New south drive and apron (both depart from the site's west drive) | D 390 sq ft | E 384 sq ft | no data, needs a quote |

**Which is cheapest to build, and by what driver.** On the repo's ranges, **E**, and the driver is the envelope, not the floor area (the two have the same area to within 6 sq ft). E's outline is a 73.5 x 40 ft rectangle: 227.0 ft of perimeter against D's 311.8 ft (85 ft or 27% less), 4 corners against 14, a single ridge, and 2,298 sq ft of ICF wall against D's 3,157 (859 sq ft less, which is **$30K-$43K** at HR:321). Against today, D saves little on the basement wall (-9%) while E saves about a third. E's offsets: a 39 ft clear roof span that is within the 12.2 m Part 9 limit by 0.43 m (CS-08), a stair-headroom blocker to fix (CS-02), 5 window wells against 3, and the louvre fix (PMC-02). D's offsets: a L-shaped roof with 5 inside corners, a 16 ft garage-door header beyond the lintel table (CS-09), and the longer ejector run (PMC-03). Plumbing, septic and elevator are a wash between them.

## 4. Comparison table (one column per option, with today's model)

| Criterion | Today | D | E | F |
|---|---|---|---|---|
| Wet-wall groups main / basement | 14 / 8 | 7 / 4 | 8 / 3 | pending |
| Main groups within 5 ft of a basement group | 1 of 14 | 3 of 7 | 1 of 8 | pending |
| Drain-run index (matrix point / physical exit), ft | 879.4 / 747.1 | 587.2 / 485.6 | 667.1 / 500.3 | pending |
| Groups over 98 ft at the matrix point | 4 of 14 | 3 of 7 | 4 of 8 | pending |
| Ejector pit drawn (labelled) | no | yes (unlabelled), SW corner | yes (unlabelled), north wall | pending |
| Longest basement drain to the pit, ft (m) | not drawn | 109.2 (33.3) | 45.1 (13.7) | pending |
| Utility room on an exterior wall | no (crawl space) | yes, 10.6 ft free (north); west is garage | yes, 11.5 ft free west + 8.0 ft north | pending |
| Vent openings drawn above grade | no | none drawn | 2, both below grade | pending |
| Water heater to furthest fixture, ft (main / basement) | 119.8 / 84.8 | 94.7 / 94.4 | 83.9 / 51.3 | pending |
| Dryer to the nearest exterior wall, ft | 23.7 (PLB-08) | 1.8 | 18.6 | pending |
| Hot-tub sunroom | none | none (future, outside 3,000) | none | pending |
| Septic bedrooms (4 / 5 reading) and flow, L/day | 3: 3,055 | 4: 2,240; 5: 2,600 | 4: 2,265; 5: 2,625 | pending |
| Tank to nearest heated wall, ft (SOP min 3.25) | 4.3 (PLB-15) | 36.5 | 24.0 | pending |
| Perimeter / corners (cost) | 399.5 / 30 | 311.8 / 14 | 227.0 / 4 | pending |
| ICF wall, sq ft | 3,459 | 3,157 | 2,298 | pending |
| ICF at HR:321 $35-50 | $121K-$173K | $110K-$158K | $80K-$115K | pending |
| Cost vs today (overall) | n/a | $$$ down | $$$ down, the larger saving | pending |

## 5. Verdict (D and E only; F pending)

1. **E is cheapest to build** (227.0 ft perimeter, 4 corners, one ridge, ICF wall $30K-$43K below D's, computed from HR:321); D and E are equal on floor area (2,934 and 2,940 sq ft), septic flow (2,240-2,600 vs 2,265-2,625 L/day) and plumbing group count (11 each).
2. **D is stronger on stacking and the laundry** (3 of 7 groups stacked; dryer 1.8 ft from a wall) **but has a far ejector pit (bath 2 at 109 ft) and a utility room with no free west wall; E's defects are the interior laundry (18.6 ft dryer run) and below-grade louvres, while its hot-water run is shorter (83.9 vs 94.7 ft).**
3. Both fix round 1's crawl-space venting root cause and lower the septic load below today's; each still needs its vent openings drawn above grade (PMC-01, PMC-02) and its pit labelled (PMC-04).

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| PMC-03 | `search.py --page plumbing 103` | plumbing | 103 | 2.4.6.3. | Piping that is too low to drain into a building sewer by gravity shall be drained to a sump or receiving tank. |
| PMC-03 | `search.py --page plumbing 105` | plumbing | 105 | Table 2.4.7.2. | 3 and 4 3 15 30 |
| PMC-05 | `search.py --page plumbing 105` | plumbing | 105 | 2.4.7.1. | Building drains shall be provided with a cleanout fitting of NPS 4 or larger |
| PMC-03 | `search.py --page plumbing 106` | plumbing | 106 | 2.4.8.1. | drainage pipes that are NPS 3 or less shall have a downward slope in the direction of flow of at least 1 in 50 |
| PMC-03 | `search.py --page plumbing 111` | plumbing | 111 | Table 2.4.10.6.-C | 4 n/a n/a n/a 180 240 300 |
| PMC-11 | `search.py --doc plumbing "pipes exposed to freezing"` | plumbing | 97 | 2.3.5.3. | Where piping may be exposed to freezing conditions, it shall be protected from the effects of freezing. |
| PMC-01 | `search.py --doc abc_2023 '"9.33.5.5"'` | abc_2023 | 1057 | 9.33.5.5. | Combustion air intake inlets shall be located on the outside of the building and not within an attic or roof space or a crawl space. |
| PMC-06 | `search.py --page abc_2023 1054` | abc_2023 | 1054 | 9.32.3.13. | shall be located at least 1 800 mm from air intakes and vented soffits |
| PMC-07 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | Add 50 L (11 Imp. gal.) for |
| PMC-07 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | - 28 in a 4-bedroom |
| PMC-07 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | - 31 in a 5-bedroom |
| PMC-07 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | 1.5 persons per |
| PMC-07 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | Fixture units are a value assigned to plumbing fixtures related to their frequency of use |
| PMC-07 | `search.py --page sewage 58` | sewage | 58 | 4.2.1.1. | 400 L (88 Imp. gal.) per expected occupant in a residential development to accommodate sludge and scum accumulation |
| PMC-07 | `search.py --page sewage 59` | sewage | 59 | Table 4.2.2.2. | 4 bedrooms 4,260 L (940 Imp. gal.) |
| PMC-07 | `search.py --page sewage 59` | sewage | 59 | Table 4.2.2.2. | 5 bedrooms 5,220 L (1,150 Imp. gal.) |
| PMC-07 | `search.py --page sewage 103` | sewage | 103 | 8.2.1.13. | A treatment field shall not be installed on soils that have an effluent hydraulic loading rate of less than 9.80 L per square metre |
| PMC-07 | `search.py --page sewage 39` | sewage | 39 | Table 2.2.2.3. | Water Softener Discharge 15% increase in peak daily wastewater volume |
| PMC-08 | `search.py --page sewage 59` | sewage | 59 | 4.2.2.1. | 1 m (3.25 ft.) of a building. |
| PMC-12 | `search.py --page sewage 31` | sewage | 31 | 2.1.2.6. | clearwater waste from a hot tub, spa, or hydro massage bath that is not of the fill-and-drain design |
