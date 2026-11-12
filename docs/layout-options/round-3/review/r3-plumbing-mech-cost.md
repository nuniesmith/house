# R3-PMC: plumbing, mechanical and cost (round 3, Option H "Knuckle hub")

**Specialist:** R3-PMC (prefix PMC). **Date:** 2026-11-12. **Role:** reviewer, read-only. Plumbing layout, septic design and structure are review items for a licensed Alberta plumber, septic designer and engineer. Gas items: "needs B149.1 check". Wiring: "needs CEC check". Prices come only from the repo (HR:line, COST-nn); anything else is "no data, needs a quote". Land is not chosen, so soil, frost depth, grade and utility availability are assumptions.

**Inputs read:** REVIEW-R3.md, ROUND3-BRIEF.md, COMMON-RULES.md; `r2-plumbing-mech-cost.md` (method; D and F numbers reused, not re-reviewed); `r3-code-structure.md` (CS, read so as not to duplicate); H's `main_floor_h.scad`, `basement_h.scad`, `matrix_h.md`, `plan_facts_h.md`, `envelope_h.txt`, `PROS-CONS.md`, `basement_plan_h.png`; `site.scad`; the repo research doc (HR).

**Re-measured, not trusted** (scratch `work/R3-PMC/`, geometry in `pmc_h.py`, shapely over the audit tables; outside face = centre line + 0.5 ft, as the matrix):
- `envelope.py`: heated main 3,571 sq ft, **288.8 ft, 22 corners (13 out + 9 in)**; garage 625 sq ft; basement **2,551 sq ft, 283.8 ft, 24 corners**. Matches the coordinator.
- `plan_facts.py`: wet groups **10 main / 3 basement, 0 of 10 within 5 ft of a basement group**; drain-run index **596.6 ft** (alt 466.7); water heater to furthest **83.1 ft main / 65.3 ft basement**; primary bed to laundry 27.8 ft. All match.
- `check_layout.py`: main 29 rooms / 33 doors / 19 windows OK; basement 24 / 20 / 6 OK.
- Where H's own text disagrees with my number: PROS-CONS section 7 prices the ICF wall on **288.8 ft (the main-floor heated perimeter) = 2,924 sq ft**; the basement perimeter is **283.8 ft = 2,873 sq ft** (PMC-12). PROS-CONS section 9 says the tank is "23 ft" from the nearest wall: measured **22.7 ft** (agrees). PROS-CONS says the dryer is "3.5 ft from the garage wall": agrees (PMC-09).

**Septic bedroom count (and how I count the flex room and the library).** A basement bedroom counts as a bedroom. The murphy-ready FLEX / CRAFT room (`basement_h.scad:45`, 12 x 12 ft, egress window, a door, no closet) counts as a bedroom for a conservative design, because it has an egress window and a bed footprint. The main-floor OFFICE / LIBRARY (x 35-50, y 20.4-36.4) is **not** counted: it has no door (a 4 ft cased opening to the hub, `main_floor_h.scad:99`), no closet, and is drawn with desks and reading chairs, not a bed. So **H is 4 bedrooms as drawn (BEDROOM 2, MASTER, BEDROOM 3, BEDROOM 4), 5 with the flex room counted (my design basis), and 6 if the library were also counted** (shown for completeness). Same rule as D and F in round 2.

## Findings

Sorted by severity. All rows are Option H. Shared round-2 items are marked "(shared)".

| # | Severity | Option | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|---|
| PMC-01 | Should fix | H | Basement UTILITY (x 26-38, y 36.4-48.4); louvres `basement_h.scad:93-94`; ENSUITE directly above | **The room is well sited, but its vents are not outdoors yet, and the only route out goes up through the ensuite.** West wall 12.0 ft, all on the exterior ICF and 52.5 ft from the garage; no crawl space, so the round-1 GAS-01 blocker is gone. But: (1) both openings (west wall y 38-41 and 43-44.5) have heads 3.75 ft below grade with no well (CS-10), so combustion air, water-heater and HRV terminals are underground as drawn; (2) **the north wall (12.0 ft) is the retaining wall against undisturbed ground** (CS-03: the primary suite is not excavated), so it cannot take a terminal, and the south wall is 8.8 ft ICF with the rest on the storage; (3) the ENSUITE (x 26-38, y 36.4-48.4) is exactly over the utility room, so a riser must run up inside the ensuite wall to the rim, which is 0.4-2.0 ft above grade; (4) the ensuite's west window (`main_floor_h.scad:117`, y 40-43, sill 4 ft) sits above the louvre at y 38-41 and over the vent chase at y 43-44.5, so terminal-to-window clearance is a live question. The HRV intake and the dryer exhaust (PMC-09) are 50+ ft away, so the 1,800 mm exhaust-to-intake distance is not at risk. Fix: draw the terminals through the rim above grade, away from the ensuite window and clear of snow, with a chase noted in the ensuite wall. | `basement_h.scad:93-94`; `main_floor_h.scad:117`; `pmc_h.py` (W wall 12.0 ft free, N wall on undisturbed ground, garage 52.5 ft); CS-03, CS-10; R2 PMC-14 | ABC 9.33.5.5 (no combustion-air inlet in a crawl space; not the case here); 9.32.3.13.(4) (exhaust 1,800 mm from air intakes); terminal clearances needs B149.1 check | $ (a chase and two terminations; no repo price) |
| PMC-02 | Should fix | H | Foundation under the primary suite: 1,017 sq ft (centre lines) of main floor with no basement under it; 124.5 ft of exterior wall; 118.8 ft of ICF retaining the unexcavated edge (CS-03) | **The "ground not excavated" saving is real, but the repo has no price for what replaces it, and PROS-CONS leaves it unpriced.** What is not excavated: 1,017 sq ft of excavation, slab and ICF. What is added (CS-03): 124.5 ft of frost-depth wall or grade beam, a fill or void decision under the trusses, a thermal break at the step. **No repo price for any of these: no data, needs a quote.** The only repo figures are the ICF range (HR:321, $35-50/sq ft of wall) and the code-minimum footing depth of 1.2 m (HR:325). As a computed illustration only (not a price): if the 124.5 ft were built as an ICF wall 4.375 ft high (4 ft below grade + 2.0 ft above grade - 1.625 ft truss) that is 545 sq ft = **$19K-$27K**, which would take H's wall total to 3,418 sq ft ($119.6K-$170.9K), **level with today's 3,459 sq ft ($121.1K-$173.0K) and about $9K-$13K above D's 3,157 sq ft**. A shallow frost wall is not an ICF basement wall, so treat that as an upper bound; but it shows the saving against today and D is small until the engineer sizes the edge. Pipes in this floor: PMC-03. | `pmc_h.py` (1,017 sq ft; 283.8 ft); CS-03; `basement_h.scad:4-6`; HR:321, HR:325 | ABC 9.15.4.2 and the foundation-depth rules are in CS-01 and CS-03; nothing new cited here | $$ (no repo price for the edge; the illustration is $19K-$27K) |
| PMC-03 | Consider | H | Main-floor drain lines near the unexcavated edge (laundry G8, G10; shared bath G6, G9) | **No wet fixture sits over unexcavated ground, but the laundry and the shared bath are at its edge, so the lines have to stay over the basement hall.** The basement hall (x 38-66, y 33-46.4) is excavated; north of y 46.4 (x 38-59) and under the primary suite there is no basement (CS-03). G8 (laundry, 74.6, 44.6) is just outside the basement polygon and G10 (laundry sink, 69.0, 47.0) and G9 (shared bath vanity and shower, y 46.1) are within 1.6 ft of the edge. Their lines run 48 to 51 ft west to the utility room: kept at y 46 or less they run over the hall, in the 1.625 ft floor above a basement ceiling with room for access panels. Pushed north they cross the unexcavated strip, where the cavity's underside is 0.375 ft above grade and piping exposed to freezing must be protected. Fall is not the issue at a physical exit (longest line 82.5 ft, 0.83 ft at 1 in 100). Mark the drain routes on the plan so the CS-03 void is not crossed by a drain. | `pmc_h.py` (G8, G10 not over the basement polygon; others over); `basement_h.scad:43-44`; `house_lib_h.scad:107-110`; CS-03 | NPC 2.3.5.3.(1) (protect piping exposed to freezing); NPC 2.4.7.1.(6) | $ (routing and access; no repo price) |
| PMC-04 | Consider | H | Drain exit and drain-run index | **The matrix index (596.6 ft) is measured to a point that is open yard, so it overstates the in-building run; at the utility room's west wall it is 423.6 ft with no group over 98 ft.** The matrix point (22.16, 58) is 10 ft north of the utility room and beside the primary deck. At a physical exit on the utility west wall (26, 42) the index is **423.6 ft, longest group 82.5 ft (kitchen sink, G3), none over 98.4 ft (30 m)**; at the matrix point 2 of 10 are over (G2 99.0, G3 102.3 ft). For comparison at physical exits: D 485.6 / none over, F 916.0 / 7 of 9 over (R2 PMC-05, PMC-13). **H is the best of the three on drain length at a physical exit.** Each long line still needs the building-drain cleanout at the exit (NPC 2.4.7.1.(6)). The ensuite groups (G4, G5, G7) are 3.2 to 11.8 ft from the exit. | `pmc_h.py` exit sums; `plan_facts_h.md` 9.5; `site.scad:185-188` | NPC 2.4.7.1.(6); Table 2.4.10.6.-C (1 in 100 column for NPS 4) | $ (a wash or better against D) |
| PMC-05 | Consider | H | Basement ejector pit (x 35.4-37.6, y 44.4-46, `basement_h.scad:104`) and BATH (x 66-74, y 18.4-26.4) | **A pit is drawn, in the utility room, but it is an unlabelled dark rectangle 2.2 x 1.6 ft (0.05 ft high) and the only basement bath is 54 to 57 ft from it by plan.** Plan Manhattan from the pit centre (36.5, 45.2): bath groups 53.7, 54.7 and 57.4 ft = **16.4 to 17.5 m**, past the 15 m one-way figure of Table 2.4.7.2 (NPS 3 and 4) and inside the 30 m two-way figure; so a cleanout at the bath end, and the pit invert about 0.5 ft below the bath's under-slab invert at 1 in 100. The force main to the tank is about 46 ft (pit to the tank face at (3, 58)). Basement load is one bath, 6.5 FU (D 13, F 6.5). Add a label, a cover, a vent and a pit size for the plumber. Same unlabelled-pit point as R2 PMC-04, PMC-18. | `basement_h.scad:104`; `basement_plan_h.png` (pit not visible); `pmc_h.py` (distances, force main) | NPC 2.4.6.3.(1) (drain to a sump or receiving tank); Table 2.4.7.2 | $ |
| PMC-06 | Consider | H | Wet-wall grouping and stacking | **Main groups 10 (today 14, D 7, F 9); basement 3 (today 8, D 4, F 2); 0 of 10 within 5 ft of a basement group (D 3 of 7, F 0 of 9).** H's 10 groups are five back-to-back clusters (powder, kitchen, shared bath, ensuite, laundry), so the real plumbing walls are five. The nearest basement group is 19.6 ft from the kitchen sink and 21.1 ft from the powder vanity. The **ensuite sits directly over the utility room** (offset 0.0 ft), which is the best possible stack for the water heater, but the utility holds no wet fixture, so the matrix scores it 0. Kitchen sink on an exterior wall (x 88, gap 0.4 ft): supplies inside the insulated wall, as round-2 PMC-11. The powder room is on the south wall (y 0), 76-80 ft from the water heater. | `plan_facts_h.md` 9.3, 9.4; `matrix_h.md` | NPC 2.3.5.3.(1) (freezing, exterior-wall sink) | $ down (about the same as D) |
| PMC-07 | Consider | H | Hot water | **One water heater at (27.5, 44.1) serves a house 66 ft wide: the furthest main-floor fixture is 83.1 ft away (kitchen sink), 94.9 ft with the 11.75 ft rise.** Against 119.8 ft today (133.6 with rise), D 94.7 (106.5), F 114.8 (126.6). Using PLB-07's pipe volumes (1/2 in 0.0104 US gal/ft, 3/4 in 0.0231) and 5.7 L/min: **0.66 min (1/2 in, 3.7 L) to 1.46 min (3/4 in, 8.3 L)** before hot arrives, against today 0.92-2.05, D 0.74-1.63, F 0.87-1.94. The powder room (76-80 ft) and dining side are the long runs; the primary suite is 4-11 ft from the heater. Basement furthest 65.3 ft (bath vanity). A recirculation loop or point-of-use heater for the south wing is worth pricing (no data, needs a quote). Heater fuel and size are not in the model: gas needs a B149.1 check. | `matrix_h.md`; `plan_facts_h.md` 9.6; R2 PMC-10, PMC-16; PLB-07 | needs B149.1 check | $ |
| PMC-08 | Consider | H | Septic design flow, tank and setback | **Flow is 2,240 L/day at 4 bedrooms, 2,600 at 5 (flex counted), 3,060 at 6 (library also counted): below today's 3,055 until the library is counted.** Fixture units **32.0** by the SOP table: main 25.5 (kitchen sink 1.5; powder WC 4 + basin 1; shared bath WC 4 + basin 1 + shower 1.5; laundry tray 1.5 + standpipe 2; ensuite tub 1.5 + shower 1.5 + WC 4 + double vanity 2) plus basement bath 6.5; the dishwasher is not in the table. Peak = 1.5 persons x 340 L per bedroom + 50 L per FU over 28 (4 bedrooms), 31 (5) or 34 (6): **4 BR 2,040 + 4.0 x 50 = 2,240 L; 5 BR 2,550 + 1.0 x 50 = 2,600 L; 6 BR 3,060 + 0 = 3,060 L**. Tank = peak + 400 L per expected occupant (1.5 per bedroom): 4,640 L (4 BR), 5,600 L (5 BR), 6,660 L (6 BR), each above Table 4.2.2.2's 4,260 / 5,220 / 6,130 L. Field at the 9.80 L/m2/day floor: 229, 265 and 312 m2 (2,460, 2,856, 3,359 sq ft); 312 m2 equals today's. Softener +15% not included (none drawn). **Tank (x -3..3, y 52-64) to H's heated wall and basement: 22.7 ft** (garage 75.5 ft, primary deck 25.5 ft); SOP minimum 3.25 ft, so it clears by 19 ft. The 6-bedroom reading is the one to avoid: keep the library a library (no door, no closet, no bed). Land-dependent. D and F: 2,240 / 2,600 (F 3,060 at 6). | `pmc_h.py` tank distances; `plan_facts_h.md` 9.1, 9.2; `basement_h.scad:45`; `main_floor_h.scad:99`; R2 PMC-07, PMC-17 | SOP Table 2.2.2.2.A (p36, p37 FU list); SOP 4.2.1.1; Table 4.2.2.2; SOP 4.2.2.1; SOP 8.2.1.13 | $ to $$ (tank and field: no data, needs a quote) |
| PMC-09 | Consider | H | LAUNDRY (x 66-75.5, y 40.5-48.4); dryer (73.9-75.3, 41.4-47.8); window `main_floor_h.scad:113` | **Best dryer of any option so far: 1.4 ft from the exterior east wall (D 1.8, F 9.5, today 23.7), but the duct exits into a 3.5 ft slot between the laundry and the garage wall.** The slot (x 75.5-79, y 37-61) is roofed by overlapping eaves (the quiet-wing hip overhangs 1.5 ft, the garage hip 1.0 ft, leaving about 1 ft open to the sky), will collect drifted snow, and the terminal is 3.5 ft from the garage wall. Exhaust must be 1,800 mm from air intakes (HRV intake is 50 ft away at the utility). Fix: terminate the dryer on the laundry's south or north face if a free wall exists, or keep the terminal at least 1 ft above snow depth; duct length limits are not in the library: needs a manufacturer / ABC check. | `pmc_h.py` (1.4 ft); `main_floor_h.scad:113, 245-246`; PROS-CONS section 2 | ABC 9.32.3.13.(4) | $ |
| PMC-10 | Consider | H | Services route to the utility room | **Shortest of the options: 24.3 ft from the west-wall landing (7.27, 48; GAS-02) to the utility west wall (26, 42.4)** (F 24.3, E 31.7, D 48.7). Water, power and gas lengths are the same as F's. The services and the building sewer share the west side, and H's drive is on the east, so they no longer share a corridor (CS-16). Gas run and meter position: needs B149.1 check. Power feeder: needs CEC check. No repo price. | `pmc_h.py`; GAS-02; R2 PMC-20; CS-16 | needs B149.1 check; needs CEC check | $ (no data, needs a quote) |
| PMC-11 | Consider | H | Hot-tub sunroom (not drawn) | **Not drawn and not listed as a future addition** (K-034 MISSING: "No sunroom or screened porch drawn"). If added: spa clearwater may not go to the septic unless the system is designed for it, and a sunroom with a spa needs its own humidity exhaust and dehumidification (ABC 9.32 ventilation; sizing needs a mechanical designer). The 4 bedroom / 32 FU septic numbers above exclude it. | `PROS-CONS.md` K-034; R2 PMC-12 | SOP 2.1.2.6.(1)(e) (spa clearwater) | unknown, no data, needs a quote |
| PMC-12 | Consider | H | PROS-CONS section 7, ICF arithmetic | **The ICF wall is priced on the main-floor perimeter, not the basement's: 288.8 ft x 10.125 = 2,924 sq ft ($102K-$146K) in PROS-CONS; the basement perimeter is 283.8 ft = 2,873 sq ft = $100.6K-$143.7K** (HR:321, $35-50/sq ft). Difference 51 sq ft, $1.8K-$2.6K. The saving against today and the others, on the correct figure: today 3,459 sq ft ($121.1K-$173.0K): **-$20.5K to -$29.3K**; D 3,157 sq ft: **-$9.9K to -$14.2K**; F 4,184 sq ft: **-$45.9K to -$65.5K**. At the Winnipeg $20-30 (HR:316): $57.5K-$86.2K. Whole foundation package at 1.8-2.2 x the wall (HR:321, "unverified for this scale"): $181K-$316K for H. All computed from the repo ranges; before the PMC-02 edge. | `envelope_h.txt` line 3; `pmc_h.py`; PROS-CONS section 7; HR:316, HR:321 | none | $ (arithmetic) |
| PMC-13 | Consider | H | East drive strip (x 103-127, y -16 to 61) | **H draws 1,848 sq ft of drive (24 x 77 ft), 4.7 to 5 times the new drive strips in D, E and F (368-390 sq ft), and lists no drive among its departures** (CS-16). It replaces the site's west drive (`site.scad:108-118`), so the site's drive is not built there. Long drive means the garage doors have a 2.7% fall (CS-06), a benefit; the cost is the extra length from the road (road north edge y = -100, `site.scad:74`). No repo price for drives or snow melt for this length (COST-05 priced only steps and walk). | `main_floor_h.scad:70`; `pmc_h.py`; CS-06, CS-16; COST-05 | none | $$ (no data, needs a quote) |
| PMC-14 | Consider | H | Roof form | **Ten roof blocks (7 house, 2 porch, 1 raised hub) against D 9, F 7, today 16; all hips, with hip-on-hip valleys at the hub.** Every heated room is under a roof (CS, 0 sq ft uncovered). The raised hub block does not give a clerestory as modelled (CS-04), so either it is deleted (9 blocks) or rebuilt as a monitor (more framing). The quiet wing is a single 37.4 ft truss span (CS-09). No repo price per roof block or truss: no data, needs a quote. | `main_floor_h.scad:240-249`; CS-04, CS-09; R2 section 2 | none | $$ (no data, needs a quote) |
| PMC-15 | Consider | H | Elevator rough-in | **No repo price exists for an elevator, its pit, shaft, overrun or power. The rough-in items, their status in H's model and what is cheap now are in the section "Future elevator: what to do at build time vs later" below.** The repo marks a shaft "$$-$$$" (`House-Plan-Review-2026-11-09.md:204`, no dollars) and rough-ins before the pour "$ now vs $$ to $$$ later" (COST-06). Stack is exact (offset 0.0 ft); the pit is 6.6 ft from the basement ICF wall (CS-12); the overrun under the quiet-wing roof is 0.5 ft at the shaft's south face (CS-05). | CS-05, CS-12; COST-06 | ABC 3.5.2.1.(1) (Elevating Devices Codes Regulation; not in the library) | $$ (no repo price) |

### Counts

| Severity | H |
|---|---|
| Blocker | 0 |
| Should fix | 2 (PMC-01, PMC-02) |
| Consider | 13 (PMC-03 to PMC-15) |

(Round 2, from `r2-plumbing-mech-cost.md`: D Should fix PMC-01, 03; F Should fix PMC-13, 14; no Blockers.)

## Quantities (re-measured)

| Driver | Today | D | F | H |
|---|---|---|---|---|
| Heated main floor, outside face, sq ft | 5,685 | 2,934 | 3,910 | **3,571** |
| Basement footprint, outside face, sq ft | 3,617 | 2,934 | 3,917 | **2,551** |
| Both levels, sq ft | 9,302 | 5,868 | 7,827 | **6,122** |
| Heated envelope perimeter, ft | 399.5 | 311.8 | 413.2 | **288.8** |
| Corners (out + in) | 30 (17+13) | 14 (9+5) | 24 (14+10) | **22 (13+9)** |
| Basement perimeter, ft | 285.3 | 311.8 | 413.2 | **283.8** |
| ICF wall area, sq ft (perimeter x 12.125 today; x 10.125 others) | 3,459 | 3,157 | 4,184 | **2,873** |
| Main floor with no basement under it, sq ft (centre lines) | n/a | 0 | 0 | **1,017** |
| Roof blocks | 16 | 9 | 7 | **10** |
| Porch / patio / deck, sq ft (excl. drive) | 2,221 | 756 | 224 | **272** (front porch 80, patio 120, deck 72) |
| Drive strip drawn, sq ft | n/a | 390 | 368 | **1,848** |
| Garage, outside face, sq ft | 892 | 645 | 619 | **625** |
| Window rows (main + basement) | 19 | 24 | 23 | **25 (19 + 6)** |
| Window wells drawn | 0 | 3 | 3 | **4** (louvres: none) |
| Wet groups main + basement | 14 + 8 | 7 + 4 | 9 + 2 | **10 + 3** |
| Fixture units | 55.5 | 32.0 | 32.0 | **32.0** |
| Elevator rough-in | none | stacked, 2.0 ft to ICF | stacked, 0 ft to ICF | **stacked, offset 0.0, 6.6 ft to ICF** |
| Stair | 22 risers | 19, one flight | 19, one flight | **19, one flight, 3,581 mm** |

## Cost: drivers ranked, priced only from the repo

"down" = a saving against today's model, "up" = added cost; "$ / $$ / $$$" = small / medium / large. Dollar figures are the repo's ICF range times the measured area (computed). Everything else is "no data, needs a quote". The repo has no whole-house $/sq ft (COST header).

| Rank | Driver | H vs today | D vs today | F vs today | Repo price |
|---|---|---|---|---|---|
| 1 | Heated floor, both levels | $$$ down (9,302 to 6,122, -34%) | $$$ down (5,868) | $$ down (7,827) | none |
| 2 | ICF basement wall | $ to $$ down: 2,873 sq ft = $100.6K-$143.7K vs $121.1K-$173.0K (**-$20.5K to -$29.3K**) | $ down (-$10.6K to -$15.2K) | $$ up (+$25.4K to +$36.3K) | HR:321 $35-50/sq ft |
| 3 | The unexcavated edge (PMC-02) | $$ up: 124.5 ft of frost wall; illustration $19K-$27K | none | none | **no data, needs a quote** |
| 4 | Whole foundation package at 1.8-2.2 x the wall (HR:321, unverified for this scale) | $181K-$316K vs $218K-$381K today | $199K-$347K | $264K-$460K | HR:321 |
| 5 | Roof form (10 hip blocks, one 37.4 ft truss span) | $$ down vs 16 blocks; **$ up vs D's 9** | $$ down | $$ down | no data, needs a quote |
| 6 | Envelope perimeter and corners | $$ down (288.8 ft, 22 corners); fewer feet than D, 8 more corners | $ down (311.8, 14) | about equal (413.2, 24) | no $/ft in the repo (COST-08) |
| 7 | Porches | $$$ down (272 sq ft vs 2,221) | $$ down (756) | $$$ down (224) | no data |
| 8 | Drive | up (1,848 sq ft strip; D and F 368-390) | up | up | no data |
| 9 | Windows | $ up (25 rows vs 19): $21.3K-$40.0K vs $16.2K-$30.4K today | $20.4K-$38.4K | $19.6K-$36.8K | HR:434 $850-$1,600 each (wells priced nowhere) |
| 10 | Plumbing groups and runs | $$ down (13 groups vs 22; shortest drain index of the three at a physical exit, 423.6 ft) | $$ down (11) | $ down (11, but 7 of 9 lines over 98 ft) | no data |
| 11 | Elevator rough-in | $ to $$ up | $ up | $ up | **no repo price** |
| 12 | Stair (straight) | no difference | none | none | no repo price |
| 13 | Utility venting and services | $ (PMC-01, 10) | $ | $ | no data |

**Where H sits on cost between D and F, and by what driver.** **H is in D's band, a little above it overall, and well below F.** Ranked cheapest first: D, H, F. The drivers pull both ways:
- **Below D:** the basement wall. H's ICF is 2,873 sq ft against D's 3,157 (-284 sq ft, **$9.9K-$14.2K less**), perimeter 288.8 ft against 311.8 ft, and 1,017 sq ft of main floor is not excavated. Porches are 272 sq ft against D's 756.
- **Above D:** floor area and roof. The main floor is 3,571 sq ft against 2,934 (+637 sq ft, +22%), both levels 6,122 against 5,868 (+4%); 10 roof blocks against 9; 22 corners against 14; 13 wet groups against 11; a 1,848 sq ft drive against 390; and **the unexcavated edge (PMC-02) is unpriced and, if built in ICF-equivalent, would add $19K-$27K and take H's wall total above D's**.
- **Against F:** H is 339 sq ft smaller on the main floor (-9%), 1,366 sq ft smaller in the basement (-35%), has 124 ft less perimeter, and its ICF wall is **$45.9K-$65.5K lower**. The wall is the single biggest driver. F also has 7 of 9 drain lines over 98 ft; H has none at a physical exit.
- **Net:** no repo $/sq ft exists for floor, roof or drive, so the sign of H against D is not provable from the repo. By the drivers the repo can price (the ICF wall) H is cheaper than D by $10K-$14K; by the area drivers it is dearer. Call H about D, plus a cost for the edge that needs a quote. **Against today, H is $$$ down on floor area and $ to $$ down on the wall, with the edge as the open item.**

## Comparison table

| Criterion | H | D | F | Today |
|---|---|---|---|---|
| Wet-wall groups main / basement | 10 / 3 | 7 / 4 | 9 / 2 | 14 / 8 |
| Main groups within 5 ft of a basement group | 0 of 10 | 3 of 7 | 0 of 9 | 1 of 14 |
| Drain-run index (matrix point / physical exit), ft | 596.6 / 423.6 | 587.2 / 485.6 | 1,017.1 / 916.0 | 879.4 / 747.1 |
| Groups over 98 ft at the matrix point / physical exit | 2 of 10 / 0 | 3 of 7 / 0 | 8 of 9 / 7 of 9 | 4 of 14 / n.a. |
| Longest main-floor drain at a physical exit, ft | 82.5 | 94.7 | 121.4 | n.a. |
| Ejector pit drawn (labelled) | yes (unlabelled), utility | yes (unlabelled), SW corner | yes (unlabelled), NW of utility | no |
| Longest basement drain to the pit, ft (m) | 57.4 (17.5) | 109.2 (33.3) | 63.3 (19.3) | not drawn |
| Utility room on an exterior wall | yes, W wall 12.0 ft free; N wall on undisturbed ground | yes, 10.6 ft free N; W is garage | yes, 16.4 ft W + 10.0 ft N free | no (crawl space) |
| Vent openings drawn above grade | 2, both below grade, no wells | none drawn | 2, both below grade | no |
| Water heater to furthest fixture, ft (main / basement) | 83.1 / 65.3 | 94.7 / 94.4 | 114.8 / 62.4 | 119.8 / 84.8 |
| Dryer to nearest exterior wall, ft | 1.4 (into a 3.5 ft slot) | 1.8 | 9.5 (11.7 by plan) | 23.7 |
| Hot-tub sunroom | not drawn | none (future) | not drawn | none |
| Septic bedrooms (4 / 5 reading; 6 if the library counts) | 4 / 5 (6) | 4 / 5 | 4 / 5 (6) | 3 |
| Design flow, L/day (4 / 5 / 6) | 2,240 / 2,600 / 3,060 | 2,240 / 2,600 | 2,240 / 2,600 / 3,060 | 3,055 |
| Tank to nearest heated wall, ft (SOP min 3.25) | 22.7 | 36.5 | 16.7 | 4.3 |
| Services run to the utility, ft | 24.3 | 48.7 | 24.3 | n.a. |
| Perimeter / corners | 288.8 / 22 | 311.8 / 14 | 413.2 / 24 | 399.5 / 30 |
| ICF wall, sq ft | 2,873 | 3,157 | 4,184 | 3,459 |
| ICF at HR:321 $35-50 | $100.6K-$143.7K | $110K-$158K | $146K-$209K | $121K-$173K |
| Cost vs today (overall) | $$$ down in floor area, the edge unpriced | $$$ down | $$ down | n/a |
| Should fix findings (R2 PMC for D, F) | 2 | 2 | 2 | n/a |

## Verdict

1. **H is the best plumbed of D, H and F:** shortest drains at a physical exit (423.6 ft against D's 485.6 and F's 916.0), the shortest main-floor hot-water run of the three (83.1 ft, D 94.7, F 114.8), a 1.4 ft dryer, the shortest services run (tied with F) and a design flow under today's at 4 or 5 bedrooms (2,240 / 2,600 L/day against 3,055).
2. **On cost H is in D's band, a little above it, and far below F** (ICF wall $100.6K-$143.7K, $10K-$14K below D, $46K-$66K below F), but the unexcavated edge under the primary suite (PMC-02, 1,017 sq ft of floor on a frost-depth wall with no repo price) can erase that saving, and the floor, roof and 1,848 sq ft drive are above D.
3. **To fix the worst items:** take the utility vents through the rim above grade away from the ensuite window (PMC-01), get a quote for the edge (PMC-02), keep drain routes over the basement hall (PMC-03), label the ejector pit and put a cleanout at the bath (PMC-05), and keep the library door-less so the septic stays at 4 or 5 bedrooms (PMC-08).

## Future elevator: what to do at build time vs later

The household plans to build the stacked space now, install a lift later, and keep the stairs as the backup. Nothing below is sized: **lift-specific sizes (shaft, pit, door, overhead, machine space) come from the chosen supplier and the engineer.** **The repo has no elevator price** (no unit, pit, shaft or install), so every cost basis below is "no data, needs a quote"; the only repo markers are "a shaft is $$-$$$" (`House-Plan-Review-2026-11-09.md:204`, no dollars) and "cheap now, tear-out later" for rough-ins before the pour ("$ now vs $$ to $$$ later", COST-06). The lift falls under the Elevating Devices Codes Regulation (ABC 3.5.2.1.(1)), which is not in the library; the engineer and supplier own it. H's stack: ELEVATOR (FUTURE) at x 53-59, y 33-40 on both levels, offset 0.0 ft, door on the bedroom hall (`main_floor_h.scad:60, 109`; `basement_h.scad:38, 106`).

### Do at build time (far cheaper now than as a retrofit)

| # | Item | Status in H's model | Why now | Cost basis |
|---|---|---|---|---|
| E1 | **Framed floor opening: trimmer and header trusses at the shaft** | **Not provided.** The closet is a room on a full truss floor (`floor_assembly()` cuts out only stairwell rooms); nothing reserves the opening in the truss layout. | Cutting a hole later through 18 in open-web trusses means retrofit headers and trimmers (R2 CS-11). Lay the trusses out to leave the opening, or frame it now and floor over it with a removable panel; the engineer and truss supplier decide. | No data, needs a quote |
| E2 | **Pit or slab recess at the basement stop** | **Not provided.** The basement slab is level under the shaft; no recess is drawn. The shaft is 6.6 ft from the nearest basement ICF wall (CS-12), so a pit does not reach the footing line as it did in D (2.0 ft) or F (0 ft). | A pit formed before the slab pour is cheap; coring a pit out of a finished slab, with a radon layer and vapour barrier already laid (HR:328, HR:339), is not. Depth is the supplier's. | No data, needs a quote |
| E3 | **Pit drain, sump and waterproofing** | **Not provided.** The nearest drain is the ejector pit, about 20 ft by plan to the west (pit x 35.4-37.6; shaft x 53-59). | A pit drain or sump is plumbing under the slab: it goes in before the pour (COST-06 lists ejector and sump discharge as pre-pour rough-ins). Method is the supplier's and a licensed plumber's. | No data, needs a quote |
| E4 | **Door openings at both stops** | **Drawn.** A 3.0 ft door at (59, 34) on both levels, onto the 7 ft bedroom hall; a 5 x 5 ft approach fits in the hall (`main_floor_h.scad:109`; `basement_h.scad:106`). The supplier's landing-door size may differ from 3.0 ft. | Headers in the shaft walls are cheap to frame to the supplier's rough opening before drywall; re-framing a bearing wall later is not. Confirm the width with the supplier first. | No data, needs a quote |
| E5 | **Shaft walls** | **Drawn as ordinary 0.4 ft room walls**, same x/y on both levels; the shaft is enclosed by rooms (linen, storage, bedroom hall) so no exterior face. | Wall construction, rail anchorage and any fire rating are the supplier's and engineer's; framing and blocking are far cheaper before the walls close. | No data, needs a quote |
| E6 | **Overhead and roof over the shaft** | **A problem as drawn.** The quiet-wing hip surface is 10.5 ft above the main floor at the shaft's south face; a 10 ft shaft ceiling leaves 0.5 ft (CS-05). | Raising the roof over a shaft (a small dormer, or moving the shaft north to y 36-43) is a framing change now and a re-roof later. The needed overhead is the supplier's. | No data, needs a quote |
| E7 | **Power feed and conduit** | **Not provided.** The model has no electrical table. Panel space and a conduit sleeve to the pit and to the shaft head are not noted. The utility room (x 26-38) is about 20 ft by plan from the shaft, through the basement hall y 40-46.4. | A sleeve and a spare breaker space are cheap before drywall and slab; fishing a feeder later is not (COST-06 lists feeders as pre-pour). Circuit size is the supplier's. **Needs CEC check.** | No data, needs a quote |
| E8 | **Machine space** | **Not provided.** No machine room or cabinet is drawn. Rooms sharing a wall with the shaft: LINEN (x 50-53, main) and STORAGE (x 38-53, y 36.4-40, basement). | Some units need a controller cabinet or a machine space, some do not; the supplier says which. If one is needed, reserving a closet or storage wall now costs nothing; carving it later takes a room. | No data, needs a quote |
| E9 | **Stair kept as the backup: blocking and power in the stair walls** | **Not provided as notes.** The stair is straight, 19 risers, 5.0 ft between walls, handrails both sides, landings top and bottom (CS-18), so a stair lift rail and a handrail both fit. | Solid blocking in both stair walls for rail or handrail anchors, and an outlet at the top and foot landings, are lumber and a sleeve before drywall. Rail and unit are the supplier's. **Outlet: needs CEC check.** | No data, needs a quote |
| E10 | **Hub-side access and no-regret closet use** | **Drawn.** The shaft opens off the 7 ft bedroom hall, one 4 ft opening from the hub at (60, 33); the stair and the hub's 5 x 5 ft clear zone are not obstructed. Until the lift goes in, the stacked space reads as two closets. | Keep the closets on both levels free of permanent shelving or services on the shaft walls so they can be cleared. | $ (no data) |

### Do later (not a build-time item)

| Item | Why it can wait |
|---|---|
| The lift or elevator itself: unit, cab, doors, controls, installation | Chosen when the household decides; priced then (no repo price). |
| Final shaft dimensions, door hardware, finishes | Come from the chosen supplier's drawings; framing in E1-E5 is the open cavity that takes them. |
| Permit, inspection and registration under the Elevating Devices Codes Regulation | Done with the supplier at install (not in the library). |
| Stair lift unit and rail | Supplier's; E9 only prepares the walls. |

**Build-time order, cheapest first:** E9 (blocking and outlets), E7 (conduit and a breaker space), E4/E5 (shaft framing), E1 (trusses), E2/E3 (pit before the slab), E6 (roof over the shaft). E1, E2, E3 and E6 are the four that cannot be done cheaply after the slab, trusses and roof are on, and they are the four H does not yet draw or reserve. Get the supplier's rough-in sheet before the engineer starts and before the slab.

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| PMC-01 | `search.py --page abc_2023 1057` | abc_2023 | 1057 | 9.33.5.5. | Combustion air intake inlets shall be located on the outside of the building and not within an attic or roof space or a crawl space. |
| PMC-01, PMC-09 | `search.py --page abc_2023 1054` | abc_2023 | 1054 | 9.32.3.13.(4) | shall be located at least 1 800 mm from air intakes and vented soffits |
| PMC-03, PMC-06 | `search.py --page plumbing 97` | plumbing | 97 | 2.3.5.3. | Where piping may be exposed to freezing conditions, it shall be protected from the effects of freezing. |
| PMC-03, PMC-04 | `search.py --page plumbing 105` | plumbing | 105 | 2.4.7.1.(6) | Building drains shall be provided with a cleanout fitting of NPS 4 or larger |
| PMC-05 | `search.py --page plumbing 103` | plumbing | 103 | 2.4.6.3.(1) | Piping that is too low to drain into a building sewer by gravity shall be drained to a sump or receiving tank. |
| PMC-05 | `search.py --page plumbing 105` | plumbing | 105 | Table 2.4.7.2. | 3 and 4 3 15 30 |
| PMC-04 | `search.py --page plumbing 111` | plumbing | 111 | Table 2.4.10.6.-C | 1 in 400 1 in 200 1 in 133 1 in 100 1 in 50 1 in 25 |
| PMC-08 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | Add 50 L (11 Imp. gal.) for |
| PMC-08 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | - 28 in a 4-bedroom |
| PMC-08 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | - 31 in a 5-bedroom |
| PMC-08 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | - 34 in a 6-bedroom |
| PMC-08 | `search.py --page sewage 36` | sewage | 36 | Table 2.2.2.2.A. | 1.5 persons per |
| PMC-08 | `search.py --page sewage 37` | sewage | 37 | FU list (Part 2) | Kitchen sink 1.5 |
| PMC-08 | `search.py --page sewage 58` | sewage | 58 | 4.2.1.1. | 400 L (88 Imp. gal.) per expected occupant in a residential development to accommodate sludge |
| PMC-08 | `search.py --page sewage 59` | sewage | 59 | Table 4.2.2.2. | 4 bedrooms 4,260 L (940 Imp. gal.) |
| PMC-08 | `search.py --page sewage 59` | sewage | 59 | Table 4.2.2.2. | 5 bedrooms 5,220 L (1,150 Imp. gal.) |
| PMC-08 | `search.py --page sewage 59` | sewage | 59 | Table 4.2.2.2. | 6 bedrooms 6,130 L (1,350 Imp. gal.) |
| PMC-08 | `search.py --page sewage 59` | sewage | 59 | 4.2.2.1. | 1 m (3.25 ft.) of a building. |
| PMC-08 | `search.py --page sewage 103` | sewage | 103 | 8.2.1.13. | A treatment field shall not be installed on soils that have an effluent hydraulic loading rate of less than |
| PMC-11 | `search.py --page sewage 31` | sewage | 31 | 2.1.2.6. | clearwater waste from a hot tub, spa, or hydro massage bath that is not of the fill-and-drain design |
| PMC-15, Elevator | `search.py --page abc_2023 287` | abc_2023 | 287 | 3.5.2.1. | shall conform to the Elevating Devices Codes Regulation made pursuant to the Safety Codes Act |
