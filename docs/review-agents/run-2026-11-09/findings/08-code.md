# 08 Code (Alberta) review

**Specialist:** Code (Alberta), Wave 4. **Date:** 2026-11-09.
**Inputs read:** COMMON-RULES, 08-code brief, findings 01-07 (07 has no code citations), plan_facts §1, §3-§5, §10, §12, computed/matrix.md, permit README §1.1/§6/§7, the code library (abc_2023, plumbing, sewage, electric_2022, National_Energy), `models/house_lib.scad`, `main_floor.scad` (guard), `model.json` (building area).
**Not in the library:** CEC Part I and CSA B149.1. Items needing them are marked. Structural and gas items are review items for a licensed Alberta engineer / gas contractor, not stamped conclusions. The main-floor A/B baseline and the tunnel are not assumed.

## Findings

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|
| CODE-01 | **Blocker** | Main stair, one straight flight of 22 risers | The flight rises 13.75 ft = 4 191 mm (22 x 190.5 mm) with no intermediate landing. Part 9 caps the vertical height of any flight at 3.7 m, so it is 491 mm over. The permit README §7 stair row (A5.1) says rise/run are "within the limits" and does not mention this; none of findings 01-07 caught it. Fix: a mid-flight landing (adds about 4 ft of run and moves the foot or the opening) or a quarter-turn. The rise (190.5 mm vs max 200) and run (267 mm vs min 255) pass; clear width 1 286 mm passes the 860 mm minimum. The basement exit stair is 19 x 7.42 in = 3.58 m, under the cap by 0.12 m. Engineer to redraw the stair, opening and foundation. | PF §10.1 (22 risers x 7.5 in, floor to floor 13.75 ft); PF §10.2 (11.75 ft, 19 risers); house_lib.scad:107,121 | ABC 2023 9.8.3.3.(1) - abc_2023 p.852; Table 9.8.4.1. p.853 | $$ (stair, floor opening, basement hallway geometry) |
| CODE-02 | **Should fix** | Door M28 (N-S hall to stair-top landing), see "ARC-05 verdict" | M28 is 28.8 in = 732 mm. Table 9.5.5.1 has its own 810 mm row for "Stairs to a floor level that contains a finished space", separate from the "line of passage" row. The basement is finished (gym, theatre, pool). M28 is a door into the stair-top landing, so declaring the front-door line does not exempt it. The other entrance to the same landing, M30 (38.4 in, wall-free), already complies. Fix: widen M28 to at least 810 mm, or make it a wall-free opening like M29/M30. | PF §4.1 (M28, M29, M30, M31); PF §3 landing room; 01-architecture ARC-05 | ABC 2023 Table 9.5.5.1. - abc_2023 p.842 | $ |
| CODE-03 | **Should fix** | Building area, Part 9 vs Part 3 | The Part 9 test is 600 m2 of building area to the outside surface of exterior walls. Result depends on the real wall: 587.0 m2 at wall centre lines, 595.4 m2 at the model's own 0.4 ft wall (0.2 ft out), 603.8 m2 at 0.4 ft out, 608.0 m2 at 0.5 ft out (the README figure, which PF itself calibrated to match). The 600 m2 line is crossed at 0.35 ft (4.1 in) from the centre line to the outside face. A real 2x6 wall with sheathing and cladding is plausibly 0.35-0.5 ft out from its framing centre, so the house is probably over. See "Part 9 determination". README §7 still says 626 m2 while README §1.1 says 608; fix the stale figure. | computed (shapely union of main_rooms heated + garage, model.json); PF §1.1; README:41 | ABC 2023 1.3.3.3.(1) p.40; "Building area" p.43; 1.3.3.4.(1) p.40 | $$$ if Part 3 (design by registered professionals) |
| CODE-04 | **Should fix** | Indoor pool and spa (basement) | The library's pool rules: Section 7.2 is mainly for public and semi-public pools, but 7.2.2.4 says waste water from a PRIVATE swimming pool is discharged to an existing municipal drainage system as the authority directs. A rural lot has no such system, so the drain-down destination is a question for the AHJ before design (supports PLB-01). The 7.2.2.1 fence rule is for an OUTDOOR pool, so it does not apply to this basement pool. 9.36.3.8 (heat recovery or 80% dehumidification) applies: water surface 26.9 m2 is over the 10 m2 exemption (GAS-04). Nothing found in the library for guards or doors at an indoor private pool. CEC bonding and GFCI (README says "Section 68") needs CEC check. | PF §3 (pool 15 x 15 ft + spa); GAS-04; PLB-01 | ABC 2023 7.2.2.4. p.623; 7.2.1.1. p.622; 7.2.2.1. p.622; 9.36.3.8. p.1083; needs CEC check | $ to $$ (AHJ ruling; the drain path is PLB-01's cost) |
| CODE-05 | **Should fix** | Patio north guard over the exit-stair areaway | The model's guard is 3.5 ft = 1 067 mm tall (`patio_guard`, top rail at 3.35 + 0.15). The drop is about 11 ft, over 1.8 m, so the 900 mm allowance for exterior guards does not apply and the general 1 070 mm minimum governs. 3 mm short. README says "42 in ... that guard is required": 42 in is 1 067 mm. Fix: 44 in. | main_floor.scad:345-352; PF §10.2 (11.75 ft rise); README §1.4 | ABC 2023 9.8.8.3. - abc_2023 p.860; 9.8.8.1.(1) p.859 | $ |
| CODE-06 | **Should fix** | Permit README §7 mis-citations | (1) Garage walls "9.10.9.16 gas-proofed" is the wrong article: 9.10.9.16 is Separation of Residential Suites. The air-barrier rule for an attached garage is 9.10.9.18.(4), and 9.10.9.18.(3) says a garage serving only its own dwelling is part of that dwelling (no fire separation). (2) The 626 m2 building-area figure is stale (see CODE-03). (3) "CEC Section 68" is not reproducible: needs CEC check. (4) "Tier 1 is the minimum in Alberta" (README §6) is not reproducible: the library only says Tier 1 is the baseline. Full table below. | README:437-464; the cited pages | ABC 2023 9.10.9.18. - abc_2023 p.887; 9.10.9.16. p.886 | $ (drawing notes) |
| CODE-07 | **Consider** | Stair-top landing | Landing room is 4.2 x 3.2 ft clear (PF §6); the dimension along the stair is 3.2 ft = 975 mm. A landing must be as long as the stair width (1 286 mm) or, if it turns less than 90 degrees, the lesser of the stair width and 1 100 mm. This one turns 90 degrees (exits are M28 west and M30 east), so the 1 286 mm rule may apply. Designer to confirm, and M28 swing must put the full arc over the landing if it swings toward the stair. | PF §3 landing row, PF §6; M28 swing 1 | ABC 2023 9.8.6.3.(1), (2), (5) - abc_2023 p.856 | $ |
| CODE-08 | **Consider** | Bedroom egress windows | Rough sizes pass: BUNK ROOM 3.5 x 5 ft, BEDROOM 2 5.4 x 5 ft (two), MASTER 2.5 x 5, 4.7 x 5, 4 x 5 ft. The code asks for 0.35 m2 (3.77 sq ft) unobstructed and no dimension under 380 mm; that is the clear opening of the sash, not the rough size. Window type is not specified. The smallest, MASTER north (2.5 ft wide), still has two other windows. Specify operator type. Window-opening guards (9.8.8.1.(4)-(5)): main-floor sills are 2.5-2.75 ft above the floor, floor is 2 ft above grade, so the exemption in Sentence (5)(b) (opening edge under 1 800 mm above the ground outside) applies: no guard needed. Basement has no bedroom (PF §3.1). | PF §5.1; PF §3.1 | ABC 2023 9.9.10.1.(2) - abc_2023 p.873; 9.8.8.1.(5) p.859 | $ |
| CODE-09 | **Consider** | Future shop, energy code and Part 3 | The shop is 100 x 100 ft = 929 m2, over the 600 m2 limit, so Part 3 governs it (not Part 9), and Part 9 energy rules (9.36.2-9.36.4) reach non-residential buildings only up to 300 m2. So the shop's energy path is the NECB, not 9.36 (confirms 06 tunnel section and STR-16). NECB 1.1.1.1 applies to buildings covered by the code. Later phase. | shop.scad (PF §12.1: 100 x 100 ft) | ABC 2023 1.3.3.2.(1)(c) p.40; 9.36.1.3.(3) p.1069; NECB 2020 1.1.1.1. - National_Energy p.56 | $$$ (later phase) |
| CODE-10 | **Consider** | Spatial separation: house, shop, parents' house | Measured: house heated wall to the future shop wall is 63.4 ft = 19.3 m (PF §12.2); garage to shop 94.5 ft = 28.8 m. Limiting distance can be taken to an imaginary line between two buildings on the same lot; at a midpoint line that is about 9.7 m, and the opening area allowed by 9.10.14.4.(1)(c) is limiting distance squared (about 93 m2) for the residential face, half that for the mercantile or industrial shop face. The line position is the designer's choice, and the shop is Part 3 so its own face is a Part 3 matter. Not measured / unknown: the parents' house is not in site.scad (PF §12 "Phase house"), so its distance is unknown; 9.10.15 (houses) would apply between the two houses. Property lines are unknown (land not chosen). | PF §12.2, §12.1 | ABC 2023 Limiting distance def. p.47; 9.10.14.4.(1)(c) p.895; 9.10.15.1.(1) p.900 | — |
| CODE-11 | **Consider** | Porches, steps, garage steps | Porch floors are 610 mm above grade, 10 mm over the 600 mm guard threshold (README §1.4): either guards or raise grade to within 600 mm. Porch steps with 4 risers need one handrail (exterior stairs over 3 risers serving one dwelling need only one; 3 risers or fewer need none). Garage steps (3 risers of 6 in, garage floor 1.5 ft below the house) count as in-dwelling stairs; a landing is required where a door opens onto the stair, and the door arc must be over it. Doors from the house onto a floor more than 600 mm above ground need a guard or opening limiter (9.8.8.1.(3)). | README §1.4, §7; PF §1.1 (garage z0 -1.5 ft) | ABC 2023 9.8.8.1.(1) p.859; 9.8.7.1. p.857; 9.8.6.2.(1) p.856; 9.8.1.2. p.851 | $ |
| CODE-12 | **Consider** | Septic: process items (SOP) | Process, not design: site evaluation per SOP Part 7 before design (README §6 step 7 has it); the drawn tank, field and separations pass (PLB-15). The library has no article in reach that names the certified installer or the permit step; those stay as README §6 items and are not cited here. | README §6; PLB-15 | SOP 2021 7.1.1.1. - sewage p.87 | — |
| CODE-13 | No issue | Smoke, CO, garage door, radon, foam | Confirmed in the library: smoke alarms on each storey incl. basement, in each sleeping room and the hallway, permanently connected and interconnected; CO alarms (attached garage and fuel-burning appliance both true); garage door tight, weather-stripped, self-closing, not in a sleeping room (M12 opens to a hall); radon rough-in (granular layer, 100 mm pipe, capped); foam protected by 9.29 finishes or a thermal barrier. | README §7 rows; PF §4.1 M12 | see table below | — |

## ARC-05 verdict

**Should fix (CODE-02), not a Blocker and not "no issue".**

- Table 9.5.5.1 lists 810 mm / 1 980 mm for doors "At Entrance to": the dwelling unit entrance, vestibule or entrance hall, **Stairs to a floor level that contains a finished space**, and "All doors in at least one line of passage from the exterior to the basement". The table is printed with the first three entries sharing one cell and the last on its own line, so the stair-entrance requirement stands apart from the line-of-passage requirement.
- Declaring the front-door line (M42, M43, M32, M31 at 823 mm, M30) satisfies the line-of-passage row only. The stair-entrance row is about the door into the stairs, and M28 is a door into the stair-top landing.
- Arguments the other way: M30 (wall-free, 38.4 in) is also an entrance to the same landing; an AHJ might treat one compliant entrance as enough. That reading is not supported by the table text, so plan for 810 mm.
- M31 is 32.4 in = 823 mm, a model opening width. The table's 810 mm is a door size the doorway must accommodate; keep M31 at 36 in to leave margin.
- Fix at low cost: widen M28 to 32 in or more, or drop the leaf.

## Part 9 determination

Applicability: Part 9 applies to Group C buildings of 3 storeys or less in building height, "having a building area not exceeding 600 m2" (1.3.3.3.(1), p.40). Above 600 m2 in building area, Group C falls to Parts 3-6 (1.3.3.2.(1)(c), p.40). "Building area" is "the greatest horizontal area of a building above grade within the outside surface of exterior walls" (p.43). The basement is below grade and does not count. The house is one storey above grade, so the storey test passes.

What is in: heated main floor (5 486.2 sq ft) plus the attached garage (832.7 sq ft), as one building, because the garage shares a wall and roof with the house and is part of the dwelling (9.10.9.18.(3)). What is out: the porch, patio and deck rows (2 221.3 sq ft in PF §1.1) have no exterior walls. That is the README's reading and the definition's text supports it ("within the outside surface of exterior walls"); an AHJ could count a walled or screened porch. The SIDE ENTRY notch (83.7 sq ft = 7.8 m2) is open on one side; if the AHJ counted it, the area rises by that.

Arithmetic (shapely union of the room rectangles, `model.json` main_rooms; 1 sq ft = 0.092903 m2):

| Measure to | House + garage ft2 | m2 | Margin to 600 m2 |
|---|---:|---:|---:|
| Wall centre line (offset 0) | 6 318.9 | 587.0 | +13.0 m2 under |
| Outside face, model wall 0.4 ft thick (offset 0.2 ft) | 6 408.9 | 595.4 | +4.6 m2 under |
| Offset 0.3 ft | 6 454.0 | 599.6 | +0.4 m2 under |
| Offset 0.35 ft (4.1 in) | - | 601.7 | -1.7 m2 over |
| Offset 0.4 ft | 6 499.2 | 603.8 | -3.8 m2 over |
| Offset 0.5 ft (README 608) | 6 544.5 | 608.0 | -8.0 m2 over |

House alone (no garage), offset 0.5 ft: 5 684.9 sq ft = 528.1 m2 (README 528). The 600 m2 limit corresponds to 6 458 sq ft of footprint. **Determination: undetermined by the drawings; probably over (Part 3).** The deciding number is the real distance from the framing centre line to the outside face of cladding; at 4.1 in or more the building is over. The README's four options (detach garage, firewall, trim 15 m2, accept Part 3) stand. Firewall option: 1.3.3.4.(1) says each portion divided by a firewall is a separate building (p.40), confirmed. The covered-walkway claim in option 1 is not in the library: not found. This is an AHJ and engineer decision.

## Permit README §7 verification table

| README row | Reference given | Library result | Status |
|---|---|---|---|
| Building area 626 m2 vs 600 m2 | Div. A 1.3.3.3 | 1.3.3.3.(1) p.40 says Part 9 applies up to 600 m2 | Article CONFIRMED; the 626 figure is stale (§1.1 says 608; model says 587-608) |
| Porch floors 610 mm above grade | 9.8.8.1 | Guard needed where the drop is more than 600 mm within 1.2 m, p.859 | CONFIRMED |
| Porch steps, 4 risers, handrails | 9.8.7 verify | 9.8.7.1.(3)(b): no handrail for 3 risers or fewer; (4): one handrail on exterior stairs over 3 risers, p.857 | CONFIRMED (one handrail is enough) |
| Garage steps, 3 risers, 2'-4" landing | 9.8.6 verify | 9.8.6.2.(1)(a),(c) landing at the top and where a door opens onto a stair; 9.8.6.3.(5) full arc of door swing over landing, p.856; garage stairs treated as in-dwelling, 9.8.1.2. p.851 | CONFIRMED |
| Garage door to house | 9.10.13.15 verify | Tight-fitting, weather-stripped, self-closing; not in a sleeping room, p.894 | CONFIRMED |
| Garage walls and ceiling gas-proofed | 9.10.9.16 verify | 9.10.9.16 is Separation of Residential Suites (p.886). The garage rule is 9.10.9.18.(4) air barrier, p.887 | WRONG ARTICLE (CODE-06) |
| Smoke alarms | 9.10.19 verify | 9.10.19.3 each storey incl. basements, each sleeping room, hallway (p.909); 9.10.19.4 permanent connection; 9.10.19.5 interconnected (p.910) | CONFIRMED |
| CO alarms | 9.32.3.9 [P20] | Applies to residential buildings with a fuel-burning appliance or storage garage, p.1049 | CONFIRMED |
| Foam plastic (ICF faces) | 9.10.17.10 | Foamed plastics protected by 9.29.4-9.29.9 interior finishes or a 3.1.5.15 thermal barrier, p.907 | CONFIRMED |
| Radon | 9.13.4 | 9.13.4.2.(2) rough-in required; 9.13.4.3 granular layer plus 100 mm pipe with airtight cap, pp.920-921 | CONFIRMED |
| Main stair: rise, run, headroom, handrails | 9.8, 9.8.7.1.(1) | Rise 190.5 mm (max 200), run 267 mm (min 255), headroom 1 950 mm (p.852, 853); handrail: one side for a stair inside a dwelling unit (Table 9.8.7.1, p.857), both drawn is extra; **flight height cap 3.7 m exceeded** | PARTLY: omits 9.8.3.3 (CODE-01) |
| Exit stair | 9.8, 9.8.7.1 | Rise 188.5 mm, run 279 mm, width 1 219 mm (min 860, 9.8.2.1.(2)); height 3.58 m under the cap; guard 42 in is 3 mm under 1 070 mm | PARTLY (CODE-05) |
| Light wells | 9.8.8 | Guards where drop over 600 mm, p.859; 900 mm height if the surface is within 1.8 m of grade, 1 070 mm above that, p.860 | CONFIRMED |
| Bedroom windows | 9.9.10.1 | 0.35 m2 unobstructed, no dimension under 380 mm, p.873; window well clearance 760 mm | CONFIRMED text; compliance needs sash type (CODE-08) |
| Fireplace | 9.22 or B149.1 | 9.22.1.1 applies to masonry fireplaces built on site (p.959); a gas fireplace goes to B149.1 and ABC 9.36.3.10 (GAS-11) | CONFIRMED; needs B149.1 check |
| Indoor pool | CEC Section 68 [P15][P16] | Not in the library (no CEC Part I) | NOT REPRODUCIBLE: needs CEC check |
| Energy 9.36 Tier 1 | 9.36, Tier 1 [P7] | 9.36.1.3.(1): prescriptive/trade-off, performance or NECB, p.1069; Table 9.36.8.2 note: Tier 1 is the baseline of 9.36.2-9.36.4, p.1106. "Minimum in Alberta" and the energy-advisor documents: not found in library | PARTLY CONFIRMED |
| Ventilation 9.32 HRV | 9.32 | Principal ventilation capacity by bedroom count (Table 9.32.3.3, 3 bedrooms: 22 to 32 L/s, p.1044); the text found does not require an HRV; 9.36.3.9.(1) applies "where" heat recovery is fitted | PARTLY CONFIRMED (HRV not mandated by text found) |

## Permit-readiness gap list

Read against `docs/permit/House-Drawing-Set.pdf` and the README. Checklist only; no redesign.

1. **Part 9 or Part 3 decision** (CODE-03): a measured building area with real wall thicknesses. Gates everything below.
2. **Stair redesign** for the 3.7 m flight limit (CODE-01), and the guard height (CODE-05).
3. **Site and plot plan**: Sheet A0.1 shows buildings relative to each other only; an ALS survey, setbacks, limiting distances and property lines are unknown (land not chosen; README §1.2, §6 step 2).
4. **Climate and loads**: snow load, wind, frost depth, degree-days, energy zone depend on location (STR-12, STR-15).
5. **Structure**: the set is "not engineered" (README banner). Missing for an engineer: ICF wall design beyond 3.0 m unsupported height (STR-01), pool-floor trusses (STR-03), garage header (STR-06), truss layouts, load-bearing wall marking (STR-13).
6. **Energy compliance documents**: 9.36 path and an energy advisor's model, with wall/roof/window assemblies and U-values on the drawings (README §6 step 4). The pool heat-recovery rule (9.36.3.8) must be shown on the mechanical drawings.
7. **Mechanical**: heat-loss calculation to CSA F280 (GAS-03), combustion-air and venting for the UTILITY room (GAS-01), ventilation design.
8. **Plumbing and septic**: fixture list and flow calculation, pool/spa and filter waste destination (PLB-01, CODE-04), weeping-tile discharge (PLB-05), SOP Part 7 site evaluation, certified installer and permit.
9. **Electrical**: service size (ELE-01, needs CEC check), meter-to-panel route (ELE-05), pool bonding (needs CEC check).
10. **Door and window schedules** against Table 9.5.5.1 (CODE-02) and egress sash type (CODE-08).
11. **Wall sections, roof and floor assemblies** (fire separation to garage, air barrier line to garage per 9.10.9.18.(4)) and the README §7 corrections (CODE-06).
12. **Builder or Owner Builder Authorization** (README §1.3, §6 step 3); development permit from the county (§6 step 1); Alberta Safety Codes agency name.

## If the tunnel architecture is reinstated

Not reviewed from `main`. If reinstated, the house and shop would be connected by a roofed heated passage; the README's own caution is that a joining roof can make them one building, which would put the combined area well over 600 m2 (shop alone is 929 m2) and so under Part 3. The library has no article on connected buildings that I could find: not found in library. Spatial separation (CODE-10) would then be replaced by a firewall or fire-separation question for Part 3.

## plan_facts corrections

None to the numbers. One note: PF §matrix says the 608 m2 outside-face figure is "calibrated so the CURRENT model = 608 m2 (permit README:41)" using a 0.5 ft offset. That is the README's number reproduced, not an independent measurement; the model's own wall thickness (0.4 ft, centre-lined) gives 595.4 m2. Both are listed in the Part 9 table.


## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| CODE-01 | `search.py --doc abc_2023 '"9.8.3.3"'` | abc_2023 | 852 | 9.8.3.3. | The vertical height of any flight of stairs shall not exceed 3.7 m. |
| CODE-01 | `search.py --doc abc_2023 '"9.8.4.1"'` | abc_2023 | 853 | Table 9.8.4.1. | Private (1) 200 125 |
| CODE-02 | `search.py --doc abc_2023 '"9.5.5.1"'` | abc_2023 | 842 | Table 9.5.5.1. | Stairs to a floor level that contains a finished space |
| CODE-03 | `search.py --doc abc_2023 '"1.3.3.3"'` | abc_2023 | 40 | 1.3.3.3. | having a building area not exceeding 600 m2 |
| CODE-03 | `search.py --doc abc_2023 '"greatest horizontal area"'` | abc_2023 | 43 | 1.4.1.2. | the greatest horizontal area of a building above grade within the outside surface of exterior walls |
| CODE-03 | `search.py --doc abc_2023 '"1.3.3.4"'` | abc_2023 | 40 | 1.3.3.4. | Where a firewall divides a building, each portion of the building so divided shall be considered as a separate building |
| CODE-03 | `search.py --doc abc_2023 '"1.3.3.2"'` | abc_2023 | 40 | 1.3.3.2. | exceeding 600 m2 in building area or exceeding 3 storeys in building height |
| CODE-04 | `search.py --doc abc_2023 '"7.2.2.4"'` | abc_2023 | 623 | 7.2.2.4. | Waste water from a private swimming pool shall be discharged to an existing municipal drainage system |
| CODE-04 | `search.py --doc abc_2023 '"7.2.1.1"'` | abc_2023 | 622 | 7.2.1.1. | Except for specific requirements for a private swimming pool, this Section applies |
| CODE-04 | `search.py --doc abc_2023 '"7.2.2.1"'` | abc_2023 | 622 | 7.2.2.1. | the entire area of an outdoor swimming pool shall be protected by a fence, building wall or enclosure |
| CODE-04 | `search.py --doc abc_2023 '"9.36.3.8"'` | abc_2023 | 1083 | 9.36.3.8. | spaces containing an indoor swimming pool shall be equipped with air exhaust systems |
| CODE-05 | `search.py --doc abc_2023 '"9.8.8.3"'` | abc_2023 | 860 | 9.8.8.3. | all guards shall be not less than 1 070 mm high. |
| CODE-05 | `search.py --doc abc_2023 '"9.8.8.1"'` | abc_2023 | 859 | 9.8.8.1. | where the difference in elevation is more than 600 mm between the walking surface and the adjacent surface within 1.2 m. |
| CODE-06 | `search.py --doc abc_2023 '"9.10.9.18"'` | abc_2023 | 887 | 9.10.9.18. | an air barrier system conforming to Subsection 9.25.3. shall be installed between the garage and the remainder of the building |
| CODE-06 | `search.py --doc abc_2023 '"9.10.9.18"'` | abc_2023 | 887 | 9.10.9.18. | it shall be considered as part of that dwelling unit |
| CODE-06 | `search.py --doc abc_2023 '"9.10.9.16"'` | abc_2023 | 886 | 9.10.9.16. | Separation of Residential Suites |
| CODE-07 | `search.py --doc abc_2023 '"9.8.6.3"'` | abc_2023 | 856 | 9.8.6.3. | landings shall be at least as wide and as long as the width of the stair or ramp in which they occur. |
| CODE-07 | `search.py --doc abc_2023 '"9.8.6.3"'` | abc_2023 | 856 | 9.8.6.3. | Where a door swings toward a stair, the full arc of the swing shall be over the landing. |
| CODE-08 | `search.py --doc abc_2023 '"9.9.10.1"'` | abc_2023 | 873 | 9.9.10.1. | unobstructed opening of not less than 0.35 m2 in area with no dimension less than 380 mm |
| CODE-08 | `search.py --doc abc_2023 '"9.8.8.1"'` | abc_2023 | 859 | 9.8.8.1. | less than 1 800 mm above the floor or ground on the other side of the window. |
| CODE-09 | `search.py --doc abc_2023 '"9.36.1.3"'` | abc_2023 | 1069 | 9.36.1.3. | whose combined total floor area does not exceed 300 m2 |
| CODE-09 | `search.py --doc National_Energy '"1.1.1.1"'` | National_Energy | 56 | 1.1.1.1. | This Part applies to all buildings covered in this Code. |
| CODE-10 | `search.py --doc abc_2023 '"imaginary line"'` | abc_2023 | 47 | 1.4.1.2. | an imaginary line between 2 buildings or fire compartments on the same property |
| CODE-10 | `search.py --doc abc_2023 '"9.10.14.4"'` | abc_2023 | 895 | 9.10.14.4. | the limiting distance squared, for residential occupancies, |
| CODE-10 | `search.py --doc abc_2023 '"9.10.15.1"'` | abc_2023 | 900 | 9.10.15.1. | buildings that contain only dwelling units and have no dwelling unit above another dwelling unit |
| CODE-11 | `search.py --doc abc_2023 '"9.8.7.1"'` | abc_2023 | 857 | 9.8.7.1. | Only one handrail is required on exterior stairs having more than 3 risers |
| CODE-11 | `search.py --doc abc_2023 '"9.8.6.2"'` | abc_2023 | 856 | 9.8.6.2. | a landing shall be provided |
| CODE-11 | `search.py --doc abc_2023 '"9.8.1.2"'` | abc_2023 | 851 | 9.8.1.2. | the garage shall be considered to be part of the dwelling unit |
| CODE-12 | `search.py --doc sewage '"7.1.1.1"'` | sewage | 87 | 7.1.1.1. | The objective of a site evaluation is to assess and quantify the capability of the site to infiltrate and disperse the effluent load into the soil |
| CODE-13 | `search.py --doc abc_2023 '"9.10.19.3"'` | abc_2023 | 909 | 9.10.19.3. | at least one smoke alarm installed on each storey, including basements |
| CODE-13 | `search.py --doc abc_2023 '"9.10.19.5"'` | abc_2023 | 910 | 9.10.19.5. | the smoke alarms shall be interconnected |
| CODE-13 | `search.py --doc abc_2023 '"9.32.3.9"'` | abc_2023 | 1049 | 9.32.3.9. | applies to every building that contains a residential occupancy |
| CODE-13 | `search.py --doc abc_2023 '"9.10.13.15"'` | abc_2023 | 894 | 9.10.13.15. | shall be tight fitting and weather-stripped |
| CODE-13 | `search.py --doc abc_2023 '"9.13.4.3"'` | abc_2023 | 921 | 9.13.4.3. | a pipe not less than 100 mm in diameter installed through the floor |
| CODE-13 | `search.py --doc abc_2023 '"9.10.17.10"'` | abc_2023 | 907 | 9.10.17.10. | foamed plastics that form part of a wall or ceiling assembly shall be protected from adjacent space |
| CODE-06 | `search.py --doc abc_2023 '"9.36.8.2"'` | abc_2023 | 1106 | Table 9.36.8.2. | Tier 1 represents compliance with the baseline energy efficiency requirements |
| CODE-06 | `search.py --doc abc_2023 '"9.22.1.1"'` | abc_2023 | 959 | 9.22.1.1. | this Section applies to masonry fireplaces constructed on-site. |
| CODE-06 | `search.py --doc abc_2023 '"9.32.3.3"'` | abc_2023 | 1044 | Table 9.32.3.3. | 3 22 32 |
| CODE-06 | `search.py --doc abc_2023 '"9.8.7.1"'` | abc_2023 | 857 | Table 9.8.7.1. | Within a dwelling unit or a house with a secondary suite |
| CODE-06 | `search.py --doc abc_2023 '"9.8.2.2"'` | abc_2023 | 852 | 9.8.2.2. | shall not be less than 1 950 mm. |
| CODE-06 | `search.py --doc abc_2023 '"9.8.2.1"'` | abc_2023 | 851 | 9.8.2.1. | Exit stairs serving a single dwelling unit or a house with a secondary suite including their common spaces shall have a width of not less than 860 mm. |

## Citation-verification appendix

Method: every row of the Citation logs in 01-06 re-run (page, article number and quote re-checked against the `--page` dump), then judged on whether the cited text supports the finding's claim. 'Read' = I opened the page and compared the text with the claim; 'Quote' = the quoted line was compared with the claim without a full read of the page. Rows already checked by script: coordinator's relabels for STR-15, PLB-02 and ELE-12 accepted (see citation_manual.md).
**07 (Cost/VE): no code citations.** Its Citation log holds one placeholder row only ("—"); nothing to verify.
**Result: 147 rows. 146 CONFIRMED, 1 DOESN'T SUPPORT THE FINDING in part (ARC-05, row 0), 0 WRONG PAGE, 0 WRONG ARTICLE, 0 QUOTE NOT ON PAGE, 0 NOT IN LIBRARY. Every row counts as reproduced; the one substantive disagreement is ARC-05.** Two notes: STR-04's "1.4.1.2" is the Division A article that holds the definition (page 43 header prints 1.4.1.2.); 06 'Tunnel' rows (NECB, shop plant) were checked by quote only.

| # | Finding | Doc | Page | Article | Verdict | Basis |
|---|---|---|---|---|---|---|
| 1 | ARC-05 | abc_2023 | 842 | Table 9.5.5.1. | CONFIRMED text; finding's conclusion ("compliant on paper" via the M31 line) DOESN'T SUPPORT: the same table has a separate 810 mm row for stairs to a finished level (CODE-02) | Read |
| 2 | ARC-05 | abc_2023 | 842 | Table 9.5.5.1. | CONFIRMED | Read |
| 3 | ARC-21 | abc_2023 | 841 | 9.5.4.1. | CONFIRMED | Read |
| 4 | ARC-28 | abc_2023 | 841 | Table 9.5.3.1. | CONFIRMED | Read |
| 5 | STR-01 | abc_2023 | 927 | 9.15.4.2. | CONFIRMED | Read |
| 6 | STR-01 | abc_2023 | 928 | Table 9.15.4.2.-A | CONFIRMED | Read |
| 7 | STR-01 | abc_2023 | 836 | 9.4.1.1. | CONFIRMED | Read |
| 8 | STR-03 | abc_2023 | 967 | 9.23.4.2. | CONFIRMED | Quote |
| 9 | STR-03 | abc_2023 | 1315 | Table 9.23.4.2.-A | CONFIRMED | Quote |
| 10 | STR-03 | abc_2023 | 1317 | Table 9.23.4.2.-B | CONFIRMED | Quote |
| 11 | STR-04 | abc_2023 | 40 | 1.3.3.3. | CONFIRMED | Read |
| 12 | STR-04 | abc_2023 | 39 | 1.3.3.2. | CONFIRMED | Read |
| 13 | STR-04 | abc_2023 | 43 | 1.4.1.2. | CONFIRMED | Read |
| 14 | STR-06 | abc_2023 | 1338 | Table 9.23.12.3.-A | CONFIRMED | Quote |
| 15 | STR-08 | abc_2023 | 852 | 9.8.2.2. | CONFIRMED | Read |
| 16 | STR-08 | abc_2023 | 852 | 9.8.2.2. | CONFIRMED | Read |
| 17 | STR-12 | abc_2023 | 915 | 9.12.2.2. | CONFIRMED | Read |
| 18 | STR-13 | abc_2023 | 986 | 9.23.14.11. | CONFIRMED | Quote |
| 19 | STR-13 | abc_2023 | 837 | 9.4.2.1. | CONFIRMED | Quote |
| 20 | STR-14 | abc_2023 | 838 | 9.4.2.3. | CONFIRMED | Read |
| 21 | STR-15 | abc_2023 | 667 | Table C-2 | CONFIRMED | Quote |
| 22 | STR-15 | abc_2023 | 667 | Table C-2 | CONFIRMED | Quote |
| 23 | STR-15 | abc_2023 | 667 | Table C-2 | CONFIRMED | Quote |
| 24 | STR-15 | abc_2023 | 668 | Table C-2 | CONFIRMED | Quote |
| 25 | STR-15 | abc_2023 | 668 | Table C-2 | CONFIRMED | Quote |
| 26 | STR-15 | abc_2023 | 669 | Table C-2 | CONFIRMED | Quote |
| 27 | STR-15 | abc_2023 | 669 | Table C-2 | CONFIRMED | Quote |
| 28 | STR-16 | abc_2023 | 837 | 9.4.2.1. | CONFIRMED | Quote |
| 29 | SITE-01 | abc_2023 | 923 | 9.14.6.1. | CONFIRMED | Quote |
| 30 | SITE-01 | abc_2023 | 923 | 9.14.6.2. | CONFIRMED | Quote |
| 31 | SITE-01 | abc_2023 | 923 | 9.14.6.4. | CONFIRMED | Quote |
| 32 | SITE-02 | abc_2023 | 923 | 9.14.5.1. | CONFIRMED | Quote |
| 33 | SITE-02 | abc_2023 | 923 | 9.14.5.2. | CONFIRMED | Quote |
| 34 | SITE-02 | abc_2023 | 923 | 9.14.5.3. | CONFIRMED | Quote |
| 35 | SITE-02 | abc_2023 | 923 | 9.14.5.3. | CONFIRMED | Quote |
| 36 | SITE-04 | sewage | 59 | 4.2.2.3. | CONFIRMED | Quote |
| 37 | SITE-05 | sewage | 106 | 8.2.2.9. | CONFIRMED | Quote |
| 38 | SITE-05 | sewage | 120 | 8.5.2.2. | CONFIRMED | Quote |
| 39 | SITE-06 | sewage | 59 | 4.2.2.1. | CONFIRMED | Quote |
| 40 | SITE-06 | sewage | 58 | 4.2.1.2. | CONFIRMED | Quote |
| 41 | SITE-09 | sewage | 103 | 8.2.2.1. | CONFIRMED | Quote |
| 42 | SITE-13 | sewage | 59 | 4.2.2.1. | CONFIRMED | Quote |
| 43 | SITE-13 | sewage | 103 | 8.2.2.1. | CONFIRMED | Quote |
| 44 | SITE-04 | abc_2023 | 923 | 9.14.6.2. | CONFIRMED | Quote |
| 45 | SITE-06 | sewage | 59 | 4.2.2.3. | CONFIRMED | Quote |
| 46 | SITE-16 | sewage | 103 | 8.2.2.1. | CONFIRMED | Quote |
| 47 | SITE-18 | abc_2023 | 923 | 9.14.6.2. | CONFIRMED | Quote |
| 48 | PLB-01 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 49 | PLB-01 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 50 | PLB-01 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 51 | PLB-05 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 52 | PLB-06 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 53 | PLB-06 | sewage | 39 | Table 2.2.2.3. | CONFIRMED | Read |
| 54 | PLB-02 | sewage | 36 | Table 2.2.2.2.A. | CONFIRMED | Read |
| 55 | PLB-02 | sewage | 36 | Table 2.2.2.2.A. | CONFIRMED | Read |
| 56 | PLB-02 | sewage | 36 | 2.2.2.2. | CONFIRMED | Read |
| 57 | PLB-18 | sewage | 31 | 2.1.2.6. | CONFIRMED | Read |
| 58 | PLB-02 | sewage | 38 | Table 2.2.2.2.B. | CONFIRMED | Read |
| 59 | PLB-02 | sewage | 37 | Table (fixture units) | CONFIRMED | Quote |
| 60 | PLB-02 | sewage | 58 | 4.2.1.1. | CONFIRMED | Quote |
| 61 | PLB-02 | sewage | 59 | Table 4.2.2.2. | CONFIRMED | Read |
| 62 | PLB-02 | sewage | 103 | 8.2.1.13. | CONFIRMED | Quote |
| 63 | PLB-15 | sewage | 59 | 4.2.2.1. | CONFIRMED | Read |
| 64 | PLB-15 | sewage | 103 | 8.2.2.1. | CONFIRMED | Read |
| 65 | PLB-15 | sewage | 103 | 8.2.2.1. | CONFIRMED | Read |
| 66 | PLB-15 | sewage | 58 | 4.2.1.2. | CONFIRMED | Read |
| 67 | PLB-16 | sewage | 89 | Appendix B-7.1.1.2.(7) | CONFIRMED | Quote |
| 68 | PLB-04 | plumbing | 103 | 2.4.6.3. | CONFIRMED | Read |
| 69 | PLB-04 | plumbing | 117 | 2.5.5.5. | CONFIRMED | Read |
| 70 | PLB-03 | plumbing | 105 | 2.4.7.1.(6) | CONFIRMED | Read |
| 71 | PLB-03 | plumbing | 105 | Table 2.4.7.2. | CONFIRMED | Read |
| 72 | PLB-03 | plumbing | 106 | 2.4.7.4. | CONFIRMED | Read |
| 73 | PLB-03 | plumbing | 111 | Table 2.4.10.6.-C | CONFIRMED | Read |
| 74 | PLB-03 | plumbing | 106 | 2.4.8.1. | CONFIRMED | Read |
| 75 | PLB-12 | plumbing | 106 | 2.4.9.2. | CONFIRMED | Read |
| 76 | PLB-12 | plumbing | 110 | Table 2.4.10.6.-A | CONFIRMED | Read |
| 77 | PLB-12 | plumbing | 111 | Table 2.4.10.6.-B | CONFIRMED | Read |
| 78 | PLB-13 | plumbing | 117 | Table 2.5.6.3. | CONFIRMED | Read |
| 79 | PLB-13 | plumbing | 117 | 2.5.6.3.(3) | CONFIRMED | Read |
| 80 | PLB-13 | plumbing | 123 | 2.5.9.2. | CONFIRMED | Read |
| 81 | PLB-13 | plumbing | 106 | 2.4.8.2. | CONFIRMED | Read |
| 82 | PLB-14 | plumbing | 97 | 2.3.5.3. | CONFIRMED | Read |
| 83 | PLB-09 | plumbing | 108 | Note A-2.4.9.3.(3) | CONFIRMED | Read |
| 84 | ELE-01 | abc_2023 | 1064 | 9.34.1.1. | CONFIRMED | Read |
| 85 | ELE-02 | electric_2022 | 13 | 2-024 | CONFIRMED | Read |
| 86 | ELE-02 | electric_2022 | 14 | 2-024 | CONFIRMED | Read |
| 87 | ELE-02 | electric_2022 | 14 | 2-024 | CONFIRMED | Read |
| 88 | ELE-04 | electric_2022 | 13 | 2-020 | CONFIRMED | Read |
| 89 | ELE-04 | electric_2022 | 13 | 2-020 | CONFIRMED | Read |
| 90 | ELE-05 | electric_2022 | 14 | 2-024 | CONFIRMED | Read |
| 91 | ELE-12 | electric_2022 | 7 | Scope | CONFIRMED | Read |
| 92 | ELE-12 | electric_2022 | 7 | Scope | CONFIRMED | Read |
| 93 | ELE-14 | abc_2023 | 1065 | 9.34.2.1. | CONFIRMED | Read |
| 94 | ELE-14 | abc_2023 | 1065 | 9.34.2.3. | CONFIRMED | Read |
| 95 | ELE-14 | abc_2023 | 909 | 9.10.19.4. | CONFIRMED | Read |
| 96 | ELE-15 | abc_2023 | 1064 | 9.34.1.2. | CONFIRMED | Read |
| 97 | GAS-01 | abc_2023 | 1057 | 9.33.5.5. | CONFIRMED | Quote |
| 98 | GAS-01 | abc_2023 | 1064 | 9.33.10.1. | CONFIRMED | Quote |
| 99 | GAS-01 | abc_2023 | 1057 | 9.33.5.2. | CONFIRMED | Quote |
| 100 | GAS-01 | abc_2023 | 1040 | 9.31.6.4. | CONFIRMED | Quote |
| 101 | GAS-03 | abc_2023 | 1057 | 9.33.5.1. | CONFIRMED | Read |
| 102 | GAS-03 | abc_2023 | 1086 | Table 9.36.3.10. | CONFIRMED | Read |
| 103 | GAS-03 | abc_2023 | 1086 | Table 9.36.3.10. | CONFIRMED | Read |
| 104 | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | CONFIRMED | Read |
| 105 | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | CONFIRMED | Read |
| 106 | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | CONFIRMED | Read |
| 107 | GAS-04 | abc_2023 | 999 | A-9.25.4.2.(3) | CONFIRMED | Quote |
| 108 | GAS-04 | abc_2023 | 1041 | 9.32.1.4. | CONFIRMED | Quote |
| 109 | GAS-05 | abc_2023 | 1048 | 9.32.3.8. | CONFIRMED | Read |
| 110 | GAS-05 | abc_2023 | 1048 | 9.32.3.8. | CONFIRMED | Read |
| 111 | GAS-05 | abc_2023 | 1048 | 9.32.3.7. | CONFIRMED | Read |
| 112 | GAS-05 | abc_2023 | 1048 | 9.32.3.7. | CONFIRMED | Read |
| 113 | GAS-05 | abc_2023 | 1044 | Table 9.32.3.3. | CONFIRMED | Read |
| 114 | GAS-05 | abc_2023 | 1047 | 9.32.3.5. | CONFIRMED | Quote |
| 115 | GAS-05 | abc_2023 | 1041 | 9.32.1.3. | CONFIRMED | Quote |
| 116 | GAS-06 | abc_2023 | 1057 | 9.33.6.1. | CONFIRMED | Read |
| 117 | GAS-06 | abc_2023 | 1046 | 9.32.3.4. | CONFIRMED | Read |
| 118 | GAS-06 | abc_2023 | 1055 | 9.33.3.1. | CONFIRMED | Read |
| 119 | GAS-06 | abc_2023 | 1056 | 9.33.4.5. | CONFIRMED | Read |
| 120 | GAS-07 | abc_2023 | 1089 | Table 9.36.4.2. | CONFIRMED | Read |
| 121 | GAS-07 | abc_2023 | 1090 | 9.36.4.6. | CONFIRMED | Read |
| 122 | GAS-09 | National_Energy | 149 | 5.2.8.7. | CONFIRMED | Read |
| 123 | GAS-10 | abc_2023 | 1057 | 9.33.5.2. | CONFIRMED | Read |
| 124 | GAS-11 | abc_2023 | 1087 | 9.36.3.10. | CONFIRMED | Read |
| 125 | GAS-11 | abc_2023 | 1087 | Table 9.36.3.10. | CONFIRMED | Read |
| 126 | GAS-13 | abc_2023 | 1056 | 9.33.4.4. | CONFIRMED | Quote |
| 127 | GAS-14 | abc_2023 | 1089 | 9.36.4.2. | CONFIRMED | Quote |
| 128 | GAS-14 | abc_2023 | 1090 | 9.36.4.4. | CONFIRMED | Quote |
| 129 | GAS-14 | abc_2023 | 1089 | Table 9.36.4.2. | CONFIRMED | Quote |
| 130 | GAS-14 | abc_2023 | 1040 | 9.31.6.2. | CONFIRMED | Quote |
| 131 | GAS-15 | abc_2023 | 1057 | 9.33.5.2. | CONFIRMED | Quote |
| 132 | GAS-15 | abc_2023 | 1064 | 9.33.9.1. | CONFIRMED | Quote |
| 133 | GAS-16 | abc_2023 | 1049 | 9.32.3.9. | CONFIRMED | Read |
| 134 | GAS-16 | abc_2023 | 1049 | 9.32.3.9. | CONFIRMED | Read |
| 135 | GAS-17 | abc_2023 | 1069 | 9.36.1.3. | CONFIRMED | Read |
| 136 | GAS-17 | abc_2023 | 1106 | Table 9.36.8.2. | CONFIRMED | Read |
| 137 | GAS-17 | abc_2023 | 1090 | 9.36.5.2. | CONFIRMED | Read |
| 138 | GAS-17 | abc_2023 | 1040 | 9.32.1.1. | CONFIRMED | Quote |
| 139 | GAS-18 | abc_2023 | 1055 | 9.33.1.1. | CONFIRMED (weak: scope sentence only; supports 'gas vs electric' only as a pointer to Part 6) | Read |
| 140 | Tunnel | National_Energy | 154 | 5.2.11.4. | CONFIRMED | Quote |
| 141 | Tunnel | National_Energy | 154 | 5.2.11.4. | CONFIRMED | Quote |
| 142 | Tunnel | National_Energy | 154 | 5.2.11.5. | CONFIRMED | Quote |
| 143 | Tunnel | National_Energy | 166 | Table 5.2.12.1.-O | CONFIRMED | Quote |
| 144 | Tunnel | National_Energy | 167 | Table 5.2.12.1.-P | CONFIRMED | Quote |
| 145 | Tunnel | National_Energy | 167 | Table 5.2.12.1.-P | CONFIRMED | Quote |
| 146 | Tunnel | National_Energy | 150 | 5.2.9.1. | CONFIRMED | Quote |
| 147 | Tunnel | abc_2023 | 1069 | 9.36.1.3. | CONFIRMED | Read |
