# House plan review — 9 November 2026

_What it covers: the model on `main` @ `d20a2fa` (main floor, basement and site; the shop as a later phase; the parents' house as a second pass)._
_Who did it: eight specialists (Sonnet) found and measured; the coordinator (Opus) merged and checked. 143 findings, every code citation re-checked against the code library._
_This is a docs-only change; no model file changes._
_The evidence is in [`docs/review-agents/run-2026-11-09/`](../review-agents/run-2026-11-09/README.md)._

## Verdict

**Not buildable as drawn, but nothing here is fatal.** Every Blocker has a known fix, and most are already on the engineer's list.

Six Blockers stop it as drawn, in four groups:
1. **The main stair breaks the code.** It's one flight of 22 risers rising 4.19 m; any flight may rise at most 3.7 m (ABC 9.8.3.3). It needs a landing, which moves the stair on both floors. No earlier review or the permit README caught it.
2. **The house is probably over the Part 9 size limit.** Building area is 587 m² at the wall centre lines and 608 m² to the outside face, against 600 m². The line is crossed 4 in out from the centre line, so real walls put it over. Over 600 m², Part 3 (the large-building code) applies to the whole house.
3. **The basement is past Part 9's tables in three places, so it needs engineered design either way:**
   - 3.70 m ICF walls holding back 3.58 m of soil;
   - a pool pit 4.8 ft below the house footings;
   - a 27 ft floor span over the pool room.
4. **The pool's ~35,100 L of water has nowhere legal to go.** Not the septic, and the code points to a municipal drain a rural lot doesn't have.

**Top 3 risks**

| # | Risk | Why it matters |
|---|---|---|
| 1 | **Code path: Part 9 or Part 3** | It sets the whole design and engineering scope. The cheapest fix is trimming about 160 sf (6.6 ft off the garage depth does it) **before** framing. Detaching the garage breaks Kayla's Costco-door deal-breaker. |
| 2 | **The basement + pool cluster** | The biggest cost driver, and the source of every structural Blocker. ICF walls alone come to $128K–$182K, and the whole foundation package $230K–$401K (computed from the Oct 28 research ranges, unverified at this scale). Fixing it later means demolition. |
| 3 | **Water on a lot not yet chosen** | The house sits between the well (east) and the septic field (west) on flat model grade. The sump, weeping tile, pool drain-down and well-treatment discharge have no destination, and plowed snow piles onto the septic tank. |

**The most expensive surprise: the basement pool.**
- It isn't just the pool. It brings 12 ft ICF walls past the code tables, a pit below the footings, engineered floor trusses over 27 ft, and a natatorium (indoor pool room) dehumidifier in a room with no route outdoors.
- It is all locked in at the pour.
- If the household still wants it after seeing the numbers, the engineer and a geotechnical report have to come first.

**Kayla's notes.** The current plan meets 62 of 164 plan items. It misses 89 and contradicts 13. Of her deal-breakers, **5 are met, 5 missing and 2 contradicted** (the drive passes Bedroom 2; closets on exterior walls).

**What Jordan and Kayla decide first:** the land, then the code path (Part 9 trim or Part 3), then the layout option. The decision list at the bottom is in that order.

---

## Blockers: can't build or won't pass as drawn

All six need professional design or an authority's ruling. Structural items are **review items for a licensed Alberta engineer**, not designs.

| # | Blocker | Evidence | Code (verified in the library) | Fix and cost |
|---|---|---|---|---|
| B1 | **Main stair is one 4,191 mm flight.** 22 risers × 7.5". Rise, run and width otherwise pass. | `house_lib.scad:107,121`; plan facts §10.1; CODE-01 | ABC 9.8.3.3.(1), "shall not exceed 3.7 m" (p.852); Table 9.8.4.1 (p.853) | Two flights with a landing: a straight run with a mid-landing adds ~4 ft, or a turn. Changes the opening and the basement. $$ now, demolition later. **Every layout option must show this.** |
| B2 | **Over 600 m² of building area, so Part 3 applies.** 587.0 m² at centre lines, 595.4 at the model's 0.4 ft wall, 608.0 at the README's 0.5 ft. The line is crossed at 0.35 ft (4.1 in) out from the centre line. The permit README's §7 "626 m²" is stale. | Plan facts §1; `matrix.md`; STR-04, CODE-03 | ABC Div. A 1.3.3.3.(1) (p.40); 1.3.3.2.(1) (p.39); "Building area", 1.4.1.2 (p.43) | Pick a path with the permit office **before** engineering: trim ~160 sf (garage depth cheapest, COST-02) / detach the garage / firewall / accept Part 3. See conflict C1. Trim: $–$$, a net saving. Part 3: $$$. |
| B3 | **ICF basement walls are past the Part 9 table.** 3.70 m tall (limit 3.0 m) with 3.58 m of backfill (largest table entry 2.85 m). | `levels`; `foundation.scad:20-27,37`; STR-01 | ABC 9.15.4.2.(1) (p.927); Table 9.15.4.2.-A (p.928); 9.4.1.1 (p.836) | Engineered wall design. Lowering the basement 1 ft saves $9.8K–$14.1K of ICF (COST-12). $$$; not fixable after the pour. |
| B4 | **Pool pit 4.8 ft below the house footings.** The deep footing is drawn narrower (1.0 ft) than the footing above it (1.67 ft). | `foundation.scad:205`; STR-02 | ABC 9.4.1.1 (p.836) | Engineer, after a geotech report. $$$; not fixable after the pour. |
| B5 | **Pool-room floor spans 26.95 ft (8.21 m).** Part 9 joist tables stop at 5.66 / 6.83 m. | `bearing_lines`; STR-03 | ABC 9.23.4.2 (p.967); Tables 9.23.4.2.-A/-B (pp.1315, 1317) | Engineered trusses, or a beam line in the pool room (COST-11: ask the engineer). $$ |
| B6 | **Pool and spa water has no legal destination.** ~28,700 L pool + ~6,400 L spa, plus filter backwash. | `foundation.scad:57-65`; PLB-01, CODE-04 | SOP 2021 2.1.2.6 (p.31); ABC 7.2.2.4 (p.623): private-pool waste goes to a municipal drain | Ask the permit office first. Pump-out, or a dry well if groundwater allows. $$, land-dependent. |

### Code misses that cost little to fix (won't pass as drawn)

| # | What | Code (verified) | Fix |
|---|---|---|---|
| B7 | Door M28 (732 mm) opens onto the stair-top landing; doors into stairs to a finished floor need 810 mm. Architecture's "a compliant route exists on paper" doesn't hold: this row applies anyway. | ABC Table 9.5.5.1 (p.842); CODE-02, ARC-05 | 36" door or an open archway. $ |
| B8 | Patio guard over the exit-stair areaway is 1,067 mm, against 1,070 mm. | ABC 9.8.8.3 (p.860); CODE-05 | 44" guard. $ |
| B9 | Porch floors sit 610 mm above grade, so they need guards or regrading to 600 mm. The garage steps need a landing where the door swings. | ABC 9.8.8.1 (p.859), 9.8.6.2 (p.856); CODE-11 | Grade, guards or a landing. $ |
| B10 | Permit README §7 errors: garage gas-proofing cites the wrong article (should be 9.10.9.18.(4), not 9.10.9.16); 626 m² is stale; "CEC Section 68" can't be checked here (needs CEC check). | CODE-06 | Fix the README text. $ |
| — | Stair-top landing is 975 mm long; a landing that turns 90° may need the stair's full 1,286 mm width. | ABC 9.8.6.3 (p.856); CODE-07 | Designer to confirm; the B1 redesign settles it. |

**Confirmed fine** (CODE-13): smoke and CO alarms, the garage-to-house door, the radon rough-in and the foam thermal barrier all match the code text. Bedroom windows pass on rough size (specify the sash type, CODE-08).

---

## What this review assumed

1. **Which plan.** This reviews the model on `main` (`d20a2fa`), traced from `docs/house/main_floor.jpg` (the November redesign). The main-floor baseline (Kayla's edited layer vs the as-drawn sheet) is still Jordan's call. No finding here presumes either answer. The layout-options PR draws both, plus a clean sheet, so the call can be made from drawings.
2. **No tunnel.**
   - The run document assumed the shop powers and heats the house through a ~70 ft heated tunnel.
   - `main` dropped the tunnel on Nov 3 (`models/site.scad:33`): house first, with power, gas and fibre from the road into the house's west side, and the shop as a later, separate project.
   - This review covers what `main` draws. Each specialist's tunnel numbers are in their "if reinstated" section, and Cost recommends keeping the Nov 3 decision (COST-03).
3. **Land isn't chosen.** Snow load, frost depth, soils (septic field size), groundwater (pool pit, sump), road side (orientation), and whether gas and grid power reach the lot are all assumptions. Alberta's ground snow load runs 1.1–5.5 kPa across the province (ABC Table C-2, STR-15).
4. **Other run-document premises are stale** (plan facts §13). The "U-stair in the former bar" is from the October model; today's stair is straight. The geothermal field and snow melt exist only in the research docs. The truck apron is 70 ft, not 80. The parents' house exists only as photos and isn't placed on the site.
5. **Engineering and code gaps.**
   - Nothing here is a stamped design. Structural and gas items are review items for a licensed Alberta engineer (and a gas fitter).
   - The code library has no Canadian Electrical Code and no CSA B149.1 (gas), so those items say "needs CEC check" or "needs B149.1 check" and cite nothing.

---

## Kayla's notes: how the current plan does

All 335 items in her notes were checked (numbered K-001…K-335 in `kayla_checklist.md`; full table in `findings/01-architecture-flow.md`).

| | Items | In the model | Missing | Contradicted |
|---|---:|---:|---:|---:|
| Plan items (a floor or site plan can show them) | 164 | **62** (38%) | **89** (54%) | **13** (8%) |
| Spec items (fit-out; carried to the spec stage) | 134 | — | — | — |
| Notes and questions (no requirement) | 37 | — | — | — |

"Missing" includes partly-there items: the cross-check counted conservatively.

**Her deal-breakers: 5 met, 5 missing, 2 contradicted.**

| Deal-breaker | Verdict | Why (evidence) |
|---|---|---|
| Bedroom next to the foyer (K-328) | ✅ met | Nearest bedroom is the master, 27 ft east of the foyer |
| Traffic only through the kitchen (K-330) | ✅ met | A 10 ft lane bypasses the island |
| Full open concept (K-332) | ✅ met | The hall splits kitchen/dining from the great room |
| Closet only through the master bath (K-333, K-201, K-304) | ✅ met | Closet passage opens to the bedroom, but that opening is only 27.6 in |
| Bedroom sharing a wall with the living room (K-334) | ✅ met | None |
| **Laundry far from bedrooms (K-329)** | ❌ missing | Master bed → laundry is **103.1 ft** |
| **Laundry tied to the master suite (K-036)** | ❌ missing | No washer/dryer in the master suite |
| **Costco door, pantry → garage (K-037, K-115)** | ❌ missing | Scullery shares 8.7 ft of wall with the garage, no door |
| **Wide doors and halls (K-003, K-060, K-061)** | ❌ missing | Of 22 single doors: 7 under 32", 11 at 32–35", **4** at 36"+ |
| **No-threshold shower (K-055)** | ❌ missing | Both shower pans drawn raised |
| **Closets on exterior walls (K-331, K-070)** | ⛔ contradicted | Bedroom 2 closet has 3.0 ft of west wall; LINEN has 10.2 ft |
| **Drive past the bedrooms (K-005, K-335)** | ⛔ contradicted | West drive is **9.3 ft** from Bedroom 2; the garage doors face it |

Site/Landscape called K-005 "partly met" (the master suite is clear of the drive); Architecture called it contradicted. **Ruling: contradicted.** K-005 says "not past master suite *or bedrooms*", and the drive passes Bedroom 2.

**Where her notes collide with other findings** (in the conflict table below): her wishlist adds area while Part 9 needs area taken out (C1); the snow-melt driveway (C3); two laundries vs one (C4); bathrooms everywhere vs grouped wet walls (C5).

---

## Should fix: real cost or function lost

Merged across specialists. The IDs point to the full findings in `docs/review-agents/run-2026-11-09/findings/`. **P** = settle before the basement pour, **F** = before framing; after those points the fix means tearing out finished work (COST fix-now/fix-later table).

### A. Main-floor layout (and Kayla's notes)

| # | What's wrong | Evidence | Fix and cost |
|---|---|---|---|
| S1 | **The drive passes Bedroom 2, and plowed snow piles onto the septic tank.** The west drive ends at y 42 beside the bedroom wing, so 4,260 sq ft of plowed snow has only that dead end to go to: onto the meters, the service lines and the tank 10 ft away. K-005 and K-335 contradicted. | 9.3 ft drive→Bedroom 2 (PF §8.5); `site.scad:111`; ARC-01, SITE-03, SITE-04 | Turn the garage doors to face south (conflict C2), or move the wing. $$ |
| S2 | **Laundry is 103 ft from the master bed.** K-036 and K-329 are missing. | PF §7.3; ARC-02 | Zero-area fix: the 55 sf LINEN becomes a master laundry on the master-bath wet wall, with a 36" door and an east window already there (PLB-09). Needs CEC check (dryer circuit). $ |
| S3 | **No Costco door.** Groceries walk 41–48 ft from the garage to the pantry. | Scullery↔garage wall x 24.34: 8.7 ft shared, 4.27 ft clear for a door; garage slab 1.5 ft lower (ARC-03) | A 3 ft door with 3 risers or a raised landing. $ |
| S4 | **Narrow doors.** 8 of 37 openings are under 32", including M28 (28.8") on the shortest garage→stair route and M49 (27.6") into the master closet passage. K-003, K-061 missing. Code ruled on M28 (B-list below). | PF §4.3; ARC-05 | 36" doors. $ (F) |
| S5 | **No curbless shower** (K-055, a deal-breaker). Both pans are drawn raised. | `main_floor.scad:224, 226`; ARC-06 | A recessed floor under each shower, detailed by the engineer. $$ now, $$$ later (F; tear-out) |
| S6 | **Circulation is 891 sf (16.2%), and one hall is 481 sf of it.** The east–west spine is 80.5 × 5.5 ft. With the foyer, mudroom and stair it's 24.3%. | PF §6.1; ARC-07; COST-07 | About 160–250 sf can come out without losing a room's function (COST-07). That overlaps the Part 9 trim (B1). $$ (F) |
| S7 | **Closets on exterior walls; two bedrooms without closets.** Bunk room and study have none. | PF §8.3; ARC-04 | Move closet rectangles inboard. $ |
| S8 | **Bedroom 2 is the noisy room.** It shares 12.7 ft of wall with the laundry and mudroom and 14.8 ft with the garage. A queen fits only on those walls. | PF §2.2, §4.1; ARC-08 | ARC has two sore-spot alternatives, both net 0 sf (COST: $ and $$). $–$$ |
| S9 | **No powder room.** The nearest toilet from the foyer is 65.8 ft away. K-033, K-145, K-157, K-298 missing. | PF §7.3; ARC-09 | Take it from the mudroom or foyer, on an existing wet wall (conflict C5). $$ |
| S10 | **Kitchen doesn't match her rules.** Triangle 41.4 ft vs 26 ft (K-261). Aisle 47" vs 54" (K-274). No dishwasher drawn. Island sink against K-108. Counter runs on exterior walls (K-096). | `main_floor.scad:197-205`; ARC-10, ARC-11 | Re-plan cabinets inside the same room. $–$$ |
| S11 | **No vestibule and no drop zones.** The 309 sf foyer holds a bench and wine racks; the mudroom has no outside door. K-041, K-141–K-143, K-155 missing. | PF §3.1, §4.1; ARC-14 | Shorten the foyer 8–12 ft (saves 100–150 sf, COST-07) and give the mudroom an exterior door. $–$$ |
| S12 | **No library; flex room has no window.** 2 bedrooms plus the master; FLEX (151 sf) can't be a bedroom without a window. | PF §3.1, §5.1; ARC-15, ARC-19 | Window the flex room. The office (165 sf, next to the master) is the nursery candidate. $ |
| S13 | **Bunk room bed under the window, no closet.** | `main_floor.scad:249-250`; ARC-12 | Move the window or the bunks; add a closet. $ |

### B. Structure: the engineer's list (all need a licensed Alberta engineer)

| # | What | Evidence | Code (verified) | Cost |
|---|---|---|---|---|
| S14 | Two supports in the permit set's framing plan (wall at x 42.65, beam at x 103.04) aren't in the model; without the wall the west basement zone spans 31.98 ft. | `bearing_lines` (4 rows); `make_drawings.py:852-868`; STR-05 | ABC Table 9.23.4.2.-B (p.1317) | $ |
| S15 | Garage west wall is 73% door. The 16 ft header is past the Part 9 lintel table (max 3.08 m), with almost no bracing length. | `main_doors` rows; STR-06 | ABC Table 9.23.12.3.-A (p.1338) | $$ |
| S16 | Porch and deck roof beams span 25.6 ft (deck), 17.45 ft (master porch) and 11.9 ft (front entry): engineered members. One valley is unframed. | `main_posts`, `main_roof`; STR-07 | ABC Table 9.23.12.3.-A (p.1338) | $$ |
| S17 | Stair headroom is 1,993 mm against a 1,950 mm minimum, a 43 mm margin. The model and the permit set draw different openings (11.43 vs 11.64 ft). An 11.4 ft header is needed. | PF §10.1; STR-08, STR-09 | ABC 9.8.2.2 (p.852) | $ |
| S18 | ICF wall tops: 155 ft (55% of the perimeter) runs parallel to the trusses, so wall restraint relies on blocking and the floor diaphragm. | `basement_outline`; STR-09 | ABC 9.4.1.1 (p.836) | $$ |
| S19 | Exit-stair areaway walls retain about 12 ft of soil as 8 in walls carrying porch posts. A porch post bears on the ICF next to a window lintel. | `foundation.scad:134-144, 317-325`; STR-10, STR-11 | ABC 9.4.1.1 (p.836) | $–$$ |
| S20 | Frost depth (4 ft) is an assumption. It sets every frost wall and 22 pier depths. Land-dependent. | `foundation.scad:22-26`; STR-12 | ABC 9.12.2.2, Table 9.12.2.2. (p.915) | $–$$ |
| S21 | No main-floor wall is marked bearing. Four walls sit 4–8 in off their supports; the great room has a 26 ft opening. | STR-13 | ABC 9.23.14.11 (p.986) | $–$$ |
| S22 | 2,221 sf of porches, patio and deck have no floor structure in the model. Each must carry the roof snow load or 1.9 kPa, whichever is greater. | PF §1.1; STR-14 | ABC 9.4.2.3 (p.838) | $$ |

### C. Water: drains, septic, grading

| # | What | Evidence | Code (verified) | Cost |
|---|---|---|---|---|
| S23 | **Basement fixtures can't drain to the tank by gravity.** They're 12–14 ft below the main floor and the tank is near grade. An ejector (sewage pump) is required but not drawn. | Levels (PF §1); PLB-04 | NPC 2.4.6.3, 2.5.5.5 | $$ (P) |
| S24 | **Weeping tile, pool-pit drain loop and sump have nowhere to go.** They may not go to the septic. A dry well works only if groundwater is below it, and the pool pit is 18'-3" below grade. Land-dependent. | Redesign §3; PLB-05, SITE-02 | SOP 2.1.2.6; ABC 9.14.5.1–9.14.5.3 | $$ (P) |
| S25 | **Master-wing drains run 120–145 ft** to the drain exit over an 18 in crawl space. That needs cleanouts (30 m limit), and the fall eats most of the floor depth. | PF §9.5; PLB-03 | NPC 2.4.7.1(6), Table 2.4.7.2 | $$ (F) |
| S26 | **Septic sizing.** 3 bedrooms and 55.5 fixture units give 3,055 L/day, and the tank needs 4,855 L. With the parents' house: 3,735 L/day. The drawn 55 × 55 ft field works only on good soil. Parents' and shop flows aren't counted yet. | PF §3, §9; PLB-02, SITE-09 | SOP Table 2.2.2.2.A, 4.2.1.1, 8.2.1.13 | $–$$ (land) |
| S27 | **Well-water treatment discharge has no path.** Iron-filter waste is barred from the septic. | `basement.scad`; PLB-06 | SOP 2.1.2.6(h)(i) | $–$$ |
| S28 | **No grading.** The site is one flat slab, and the house sits between the well (east) and the field (west), so any cross-fall sends water to one of them. Land-dependent. | `site.scad`; SITE-01 | ABC 9.14.6.1, 9.14.6.2 | $–$$ |
| S29 | **Field and reserve protected only by a dashed line.** The SOP bars drives, paving and structures on a field. | SITE-05 | SOP 8.2.2.9 | $ |
| S30 | **Tank is 4.3 ft (1.3 m) from the bedroom wing** (minimum 1 m) and deep: excavating beside the wing's footings needs the engineer. The docs say "by the utility room", but it's drawn 9–17 ft north of it. | PF §12, §15; SITE-06 | SOP 4.2.2.1, 4.2.2.3 | $$ |
| S31 | **Hot water to the master tub is ~134 ft of pipe** from one heater, with no recirculation. | PLB-07, GAS-14 | (no NPC rule found) | $$ |

### D. Heat, air and power

| # | What | Evidence | Code (verified) | Cost |
|---|---|---|---|---|
| S32 | **The mechanical rooms can't reach outdoors.** The basement UTILITY room (boiler, water heater, air handler, HRV) and the pool equipment room border crawl space on every outside face (14.9 and 14.3 ft to open air). The laundry is interior (dryer 23.7 ft from an outside wall). Combustion air may not come from a crawl space. **This becomes a Blocker if any drawing ends a vent or intake in the crawl.** | PF §3.2; GAS-01, GAS-04, GAS-13, PLB-08 | ABC 9.33.5.5; venting needs B149.1 check | $$ (P) |
| S33 | **The service comes in at the wrong wall.** Meters sit on Bedroom 2's west wall, 0.15 ft below its window sill. The lines stop 14.9 ft short of the panel in the UTILITY room, and the gas pipe runs ~31 ft through crawl space to the boiler. | `site.scad`; PF §15; ELE-05, GAS-02, SITE-14 | AEUC 2-024(b); clearances need CEC / B149.1 check | $ now, $$ later (P) |
| S34 | **No service size anywhere.** House demand is 193 A with fuel-fired heat and 398 A all-electric. Add the parents' house (56 A) and shop (198 A) for 447–652 A, so 400 A won't cover the full build. Heating fuel (decision #21) and pool-heater fuel drive it. | Load table in ELE-01, ELE-02, ELE-08 | ABC 9.34.1.1; AEUC 2-024; demand calc needs CEC check | $$–$$$ |
| S35 | **Cheap rough-ins missing from the pre-pour list:** meter→panel, well pump, Starlink, EV charger, generator transfer, parents' feeder, snow-melt sleeves, radiant tubing. | Permit README §8; ELE-06, COST-06 | needs CEC check | $ now, $$–$$$ later (P) |
| S36 | **No generator or transfer switch.** Critical loads are ~15 kW with fuel-fired heat, ~50 kW all-electric. | ELE-07 | needs CEC / B149.1 check | $$ |
| S37 | **No heat-loss calculation.** House heat is 134,418–224,030 BTU/h on today's areas. Add the default snow melt (110,670 BTU/h) and the plant is 71.8–98.1 kW, straddling the 88 kW break in the ABC boiler table. One air handler at the west end serves a 121 ft-wide house. | GAS-03, GAS-06 | ABC 9.33.5.1; Table 9.36.3.10 (boiler efficiency changes at 88 kW); 9.33.6.1; 9.33.3.1 | $$ (P: radiant tubing is impossible after the pour) |
| S38 | **Exhaust vs combustion.** Five exhaust sources, plus a pool room run negative on purpose, can pull the house negative around fuel-burning appliances. | GAS-05 | ABC 9.32.3.7, 9.32.3.8, Table 9.32.3.3; needs B149.1 check | $–$$ |
| S39 | **Pool heater fuel is unstated**, and the heater sits 70+ ft from the boiler. | GAS-07, ELE-08 | ABC Table 9.36.4.2, 9.36.4.6; wiring needs CEC check; gas needs B149.1 check | $$ |
| S40 | **Pool room humidity.** The pool room falls under the ABC pool heat-recovery rule, but its dehumidifier room can't reach outdoors (see S32). | GAS-04 | ABC 9.36.3.8, 9.25.4.2(3), 9.32.1.4 | $$ |

### E. Site and driveway

| # | What | Evidence | Code | Cost |
|---|---|---|---|---|
| S41 | **No geothermal field is sited.** Horizontal loops need 15,000–42,000 sq ft and the site leaves ~10,795 sq ft free. Gas heats at about half the running cost of geothermal (HR:824), but only if the road has gas (decision #8). | SITE-07, GAS-10, COST-04 | ABC 9.33.5.2(1)(f) (GSHP installation standard); drilling rules not in library | $$–$$$ |
| S42 | **Snow melt isn't drawn**, but it's a load as big as the house. The default hydronic scope is $33K–$70K; steps and walk only is $4K–$19K. | GAS-09, SITE-10, COST-05 | no house-side article in the library; needs B149.1 / CEC check | $–$$$ (conflict C3) |
| S43 | **A tractor-trailer can't turn in the house-phase drive.** It's a 142 ft dead end from the road. | `site.scad:108-118`; SITE-08 | — | $–$$ |
| S44 | **The propane tank sits behind the service lines**, with a 153 ft feed. | GAS-08 | needs B149.1 check | $ |

---

## Consider: judgement calls for Jordan and Kayla

One line each; the IDs hold the detail.

**Layout and daylight**
- Sight lines (ARC-13):
  - The 80 ft hall looks straight into the master bedroom (K-104).
  - Bedroom 2's bed sees the Bath 2 door (K-103).
  - The front door sees the whole great room (K-144).
- The great room has north glass only, and the sun room faces N/E instead of SE (ARC-16; K-014, K-064). Only 4 rooms have windows on 2+ walls; two windows sit dead centre on their walls (ARC-20).
- 27 heated spaces have no window, including the study, flex room, office and foyer (ARC-19). Adding windows is cheap: 19 windows cost $16K–$30K today (COST-09).
- Both tubs sit on exterior walls (K-074); the master tub is raised, not sunken (K-220) (ARC-17). The master WCs share a wall with the den alcove (ARC-18).
- No elevator space and no dumbwaiter (K-058, K-059). The basement (pool, gym, theatre) is reachable only by stairs (ARC-21; a shaft is $$–$$$).
- No kitchen door to a covered outdoor area (K-023, K-127). The deck is ~60 ft away through the great room (ARC-22, SITE-12).
- The dog wash is in the basement pet room (K-170). A main-floor spot exists on the laundry's south wall, next to the mudroom (ARC-23, PLB-10).
- Smaller items:
  - 87 sf of pass-through slivers (ARC-25).
  - The plan's bed symbols are smaller than a queen or king, though real sizes fit (ARC-26).
  - Two door swings block traffic (ARC-27).
  - The sun room table (2.6 × 3.6 ft) isn't the 4-seat dining set K-189 asks for (ARC-24).
  - Room sizes pass the code (ARC-28).
- **Form:** 30 corners (17 outside, 13 inside), about 86 ft more wall than an equal-area rectangle, and 16 hip roof blocks (COST-08). 12 ft ceilings cover 2,076 sf, and porches and decks are 2,221 sf, 40% of the heated area (COST-10).

**Services**
- Plumbing:
  - The master laundry works on the existing wet wall (PLB-09).
  - Grouped wet walls (K-006) are only partly met: 14 groups in 5 clusters (PLB-11).
  - Pipe sizes are fine (PLB-12). The master bath needs 2+ vent connections (PLB-13).
  - Four fixture groups sit on exterior walls (PLB-14).
  - All septic separations pass with wide margins (PLB-15). House-phase lines clear the field (PLB-16).
- Electrical:
  - Heating fuel swings the electrical load by 1.5 to 29.3 kW (ELE-09).
  - No EV charger for K-311 (ELE-10). The well pump cable route isn't drawn (155 ft, ELE-11). No solar or battery readiness (ELE-12).
  - Exterior lighting and alarm counts are needed (ELE-14).
  - **Is there grid power at the road at all?** That's land-dependent (ELE-15).
- Gas and air:
  - The fireplace and gas range need gas routing (GAS-11). The fuel choice is natural gas vs propane vs geothermal (GAS-12).
  - Five appliances share a 14.5 × 6.9 ft utility room (GAS-13). DHW size and fuel aren't stated (GAS-14).
  - No cooling, though Kayla asks for AC (K-194, K-217; GAS-15).
  - CO alarms confirmed (GAS-16). The energy path is 9.36 Tier 1 (GAS-17). The radon pipe competes for the utility room (GAS-19).
- Site:
  - Snow melt on the west drive fails K-012 (SITE-10). Cardinal placement is only partly met: bedrooms west, not east (K-014; SITE-11).
  - No well-head protection or rig access (SITE-13). The services run in three trenches 3 ft apart, which needs CEC / B149.1 checks (SITE-14).
  - No windbreak yet; a west windbreak would drift the drive shut (SITE-15).
- **Snow load:** Alberta ranges from 1.1 kPa (Calgary) to 5.5 kPa (Lake Louise), so a foothills lot changes the trusses, beams and porches (STR-15).
- **Basement height:** 1 ft lower saves $9.8K–$14.1K of ICF and eases B3, but the theatre and pool want the height (COST-12; conflict C8).

---

## Later phase: the shop (not part of the first build)

| ID | What | Note |
|---|---|---|
| STR-16, CODE-09, COST-13 | 100 × 100 ft = 929 m², a steel clear-span building | Part 3 + NECB, not Part 9. The single largest structural cost once it's built. Needs a quote. |
| ELE-03, ELE-04 | The "210 ft" buried run starts 72 ft west of the house, so panel → shop is ~293 ft. 200 A over 4/0 aluminium drops 3.9–4.9%. | A direct ~100 ft route drops under 1.4%. The west route squeezes past the septic tank and crosses the effluent line. |
| PLB-17, PLB-18 | Shop bathroom: gravity works only with a tank inlet 5.3–6.6 ft below grade, so a lift station is the safe default. Wash bay to a separator and holding tank, never the septic; three drain paths undefined. | The docs contradict each other on which tank the shop uses. |
| SITE-17, SITE-18, SITE-19 | The full-phase drive runs 5 ft from the tank and over the effluent and service lines. 23,340 sf of new paving has no drainage plan. Truck swept paths aren't run. | **Install marked sleeves under the future drive line now** ($ now vs $$$ later). |

## Second pass: the parents' house

Only the photos exist (`docs/small_house/`): 32 × 21 ft, 1 bed / 1 bath, crawl space, "services from main house (TBD)". It isn't placed on the site.
- **Reserve now:**
  - a site at least 10 m (33 ft) from the septic field (SITE-16);
  - its septic flow, 680 L/day (PLB-19);
  - a feeder or service decision (56 A, ELE-13);
  - gas vs electric (GAS-18).
- **Check the egg-chair hook:** it hangs from a sloped roof member, not the doubled joist the note describes. Confirm what carries the 500 lb (STR-17).
- **Unpriced decisions:** curbless shower vs tub and 36" doors (COST-14).

---

## Conflicts to decide

Each row is a real trade-off. Where the code or physics has already decided, that's said; otherwise it's Jordan and Kayla's call, with both sides priced.

| # | Conflict | One side | Other side | Cost each way | Who decides |
|---|---|---|---|---|---|
| C1 | **Kayla's wishlist adds area; Part 9 needs area out** | She's missing a powder room (S9), vestibule (S11), library (S12), wider halls and doors (S4), roomier baths (S5) | Building area is 608 m² against 600 (B2); trim ~160 sf, or go Part 3 | Garage depth trim: $, a net saving (garage sf are cheapest). Part 3: $$$, a professional design throughout. Detaching the garage: $$, **and it breaks her Costco door (K-037)**. | Jordan + Kayla, after the permit office. The layout options show what fits inside 600 m². |
| C2 | **Garage doors west (as drawn) or south** | South fixes K-005/K-335 (no drive past Bedroom 2) and K-012 (drive south). It also gets plowed snow off the septic tank (S1). | West keeps garage doors off the front elevation and keeps the front loop and garden (`site.scad`). Oct 28 #7 is still open. | Re-plan the drive and front loop: $$. Leaving it: K-005 stays contradicted. | Jordan + Kayla |
| C3 | **Snow melt** | Kayla wants the driveway south for snow melt (K-012) | The research says a full driveway is "generally no" (HR:902). It's a heating load as big as the house (S37). | Steps and walk: $4K–$19K. Default hydronic scope: $33K–$70K. The whole west drive: $192K–$405K (GAS-09). | Jordan + Kayla (Oct 28 #23) |
| C4 | **One laundry or two** | K-036: laundry tied to the master suite | K-329: laundry near the bedrooms. The wings are 103 ft apart, so one room can't do both. | A second W/D in today's LINEN: zero area, $ for the appliances, dryer circuit and vent (S2, PLB-09). | Kayla |
| C5 | **Bathrooms everywhere vs grouped wet walls** | K-033/K-034/K-157: a bathroom near every zone and entry, plus a powder room | K-006 and plumbing cost: 14 wet groups already, only 1 stacked (PLB-11) | Each new wet room on an existing wet wall: $. On a new one: $$. | Kayla, with the layout option |
| C6 | **Tunnel (run document) vs house-first services (repo, Nov 3)** | The run document's assumption: the shop powers and heats the house through a ~70 ft tunnel | The repo dropped it Nov 3. Cost: the only price is $110K–$220K (unverified), and it would have to be built with the house, contradicting "house first" (COST-03). | Tunnel: $$$. Hedge: a second spare sleeve and a recorded trench route: $. | **Jordan: confirm which is current** |
| C7 | **Heating fuel: geothermal, gas or propane** | Geothermal: $70K–$140K+ (HR:795); a horizontal loop field doesn't fit (15,000+ sf needed, ~10,795 sf free) | Natural gas heats at about half geothermal's running cost (HR:824), if the road has gas. Propane costs more to run than geothermal (HR:821). | $$$ vs needs a quote | Jordan, after the land (Oct 28 #8, #21) |
| C8 | **Basement height** | 12 ft clear (theatre 13.25 ft, pool) | 1 ft lower: −$9.8K–$14.1K and less backfill on the B3 walls (COST-12) | $$ | Jordan |
| C9 | **Accessibility future-proofing** | Kayla: curbless showers (K-055, deal-breaker), 36" doors, elevator space (K-058), dumbwaiter (K-059) | Area and cost: a shaft is $$–$$$. Curbless showers need a recessed floor before framing (S5). | Doors $, showers $$ now / $$$ later, shaft $$–$$$ | Kayla + Jordan |
| C10 | **Pool-room span** | An open pool room needs 27 ft engineered trusses (B5) | A beam line with columns in the pool room brings spans toward the Part 9 tables (COST-11) | Engineer to price both | Engineer, then Jordan |

**Already decided by code or physics (no choice):**
- The stair gets a landing (B1).
- Basement fixtures need a sewage ejector, because the tank sits above them (S23).
- Pool water, iron-filter waste and foundation drainage stay out of the septic (B6, S24, S27).
- Combustion air can't come from the crawl space (S32).
- The door into the stair is at least 810 mm (B7).

---

## Decision list, in order

Land first, because it sets the numbers everything else depends on. Then the code path, then the layout, then the systems that are locked in at the pour.

**A. The land (gates everything)**
1. **Choose the land, then record its values:**
   - snow load (1.1–5.5 kPa across Alberta), frost depth;
   - soils and percolation for the septic field size, and the groundwater depth for the pool pit and sump;
   - which side the road is on (orientation, K-011–K-015);
   - natural gas at the road, grid power distance;
   - well prospects, climate zone (7A/7B).
   - Covers Oct 28 #8, #9 and #10, which stay open until then. [STR-15, STR-12, PLB-02, SITE-02, ELE-15]
2. **Geotechnical report** before the foundation engineer starts. [Oct 28 #11; B3, B4]

**B. The code path (before paying for engineering)**
3. **Part 9 or Part 3:**
   - Ask the permit office how it measures building area. It's 587–608 m², depending on the wall build-up.
   - Then pick: trim ~160 sf / detach the garage / firewall / accept Part 3. [B2, C1]
4. **Confirm the services plan:** house-first with no tunnel (the repo, Nov 3), or the run document's shop-powers-house. [C6]
5. **Pool: ask the permit office where drain-down and backwash may go.** Then confirm the pool stays. [B6]

**C. The layout (before framing)**
6. **Choose the main-floor layout: Option A, B or C** (the layout-options PR). This settles the parked baseline question. Each option includes the stair landing (B1), its building area against 600 m² (B2), and Kayla's deal-breakers.
7. **Garage doors: west or south**, and the drive with them. [C2; Oct 28 #7]
8. **One laundry or two; powder-room and wet-wall placement.** [C4, C5]
9. **Accessibility level:** 36" doors throughout, curbless showers, elevator space or not. [C9]

**D. Systems locked in at the pour**
10. **Heating plant and fuel; radiant or forced air.** Tubing goes in before the slab or never. [C7; Oct 28 #21, #22; S37]
11. **Snow-melt scope.** [C3; Oct 28 #23]
12. **Service size:** 200, 400 or 600 A, and whether the shop and parents' house get their own service. [S34; after #10]
13. **Pool details:** heater fuel, dehumidifier route outdoors, basement height. [S39, S40, S32, C8]
14. **Septic inputs for the designer:** 3 bedrooms + the parents' house + the shop bathroom; sump and treatment waste kept out. [S26, S24, S27]
15. **Add to the pre-pour rough-in list:**
    - meter → panel, well pump, Starlink, EV charger;
    - generator transfer, parents' feeder;
    - snow-melt sleeves, radiant tubing;
    - ejector, vent chase. [S35, COST-06]

**E. Hand-off**
16. **Engineer's scope:** B1, B3–B5 and S14–S22 (stair, ICF walls, pool pit, pool floor, garage header, porch beams, landing and opening, areaway walls, frost depth, bearing walls, porch floors).
17. **After the land and climate zone:** window spec, wall assembly, roof package. [Oct 28 #16, #15, #18]
18. **Parents' house:** reserve its site, septic setback and service routes now. [SITE-16]

### The Oct 28 decision list after this run
- **Re-opened, 1:** #1, the basement stair. It was superseded by the straight stair, which now fails the 3.7 m flight rule (B1).
- **Narrowed with numbers, still open, 3:**
  - #21 heating: geothermal doesn't fit the drawn site, and gas runs at half its cost if available;
  - #22 distribution: must be decided before the pour;
  - #23 snow melt: $4K–$19K vs $33K–$70K vs $192K+.
- **Still open, 10:**
  - #7 (side-load garage doors: now a Kayla conflict, C2);
  - #8, #9, #10, #11 (land);
  - #13 (waterproofing contract wording);
  - #15, #16, #18 (after the land);
  - #20 (well contract).
- **Still decided, 7:** #2, #3, #5, #12, #14, #17, #19. This run adds items to #19's checklist (decision 15).
- **Superseded, 2:** #4, #6.

---

## How this review was checked

- **Who:** eight specialists (Sonnet) in four waves, at most two at a time. Opus coordinated. Specialists edited nothing. The session's usage limit paused the run once, from about 04:05 to 07:50 UTC. Wave 4 resumed from its saved state.
- **Evidence:** 143 findings rows (6 Blocker, 72 Should fix, 65 Consider), merged here into 10 Blocker/code-miss items, 44 Should-fix groups and the Consider list.
  - **0 findings cut.** Every row carries a plan-facts number, a `file:line`, a render or a verified citation.
  - Two rows use "generally", but they quote the repo's own research with its numbers.
- **Citations:** 188 rows in eight Citation logs, every one reproduced from the code library:
  - 185 matched page, article number and quote by script;
  - 3 matched by hand and were relabelled (a table without a printed number; an AEUC "Scope" clause);
  - **0 bounced**;
  - the Code specialist also read each cited page against its claim: 146 of 147 support their findings, and one conclusion was corrected (ARC-05, superseded by B7);
  - see `docs/review-agents/run-2026-11-09/citation-check.md`.
- **Not in the library:**
  - The Canadian Electrical Code (wiring) and CSA B149.1 (gas). Those items say "needs CEC check" / "needs B149.1 check" and cite nothing.
  - The permit README's "CEC Section 68" for the pool is one of them.
- **Environment:**
  - The run executed in a Claude Code cloud session, not oryx, so OpenSCAD 2021.01 was installed there.
  - The code library was rebuilt from the same five PDFs in `docs/codes/`. "PDF page" means the page index in the file, so every citation can be re-checked on oryx by opening that page.

## Files

- [`plan_facts.md`](../review-agents/run-2026-11-09/plan_facts.md): every measured number, sourced. [`renders/`](../review-agents/run-2026-11-09/renders/): labelled plans of both levels.
- [`findings/`](../review-agents/run-2026-11-09/findings/): the eight specialist reports in full, with the 335-row Kayla cross-check in `01-architecture-flow.md`.
- [`kayla_checklist.md`](../review-agents/run-2026-11-09/kayla_checklist.md): her notes, numbered. The layout options are scored on these same IDs.
- [`citation-check.md`](../review-agents/run-2026-11-09/citation-check.md): the citation re-run.
- [`briefs/`](../review-agents/run-2026-11-09/briefs/): exactly what each specialist was asked.
