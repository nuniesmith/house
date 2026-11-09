# Cost / Value Engineering review (COST), Wave 4

- **Specialist:** Cost / VE. **Date:** 2026-11-09. **Prefix:** `COST`.
- **Inputs read:** COMMON-RULES.md; 07-cost-ve.md; findings 01-06 (all Blockers and Should-fixes); plan_facts.md (PF §1, §2, §3, §5, §6, §12); computed/matrix.md; `House-Review-and-Research-2026-10-28.md` (cited HR:line); `Redesign-and-Spec-2026-11-02.md`; `docs/permit/README.md`; `docs/shop/Shop-Base-Plan.md` (cited SBP:line).
- **Price rule:** dollar figures come only from the repo's research ranges. Where I multiply a repo $/unit by a model quantity, the row is marked "computed" and shows the arithmetic. The repo has no whole-house $/sq ft, no pool, theatre, roof, framing, door or bathroom price. Those are "no data, needs a quote", and I rank them with $/$$/$$$.
- **Assumptions held:** main-floor A/B baseline is Jordan's call; I review `main` as modelled. Land is not chosen, so everything land-dependent is an assumption. No stamped-engineer claims. **No code claims are made in this file, so the Citation log is empty.**
- **Area figures disagree:** permit README §1.1 says 608 m2 (8 m2 over the 600 m2 limit); Redesign:574 says about 626 m2 (26 m2 over, the figure in my brief); the model centre-line figure is 587 m2 (STR-04, PF §15 #10). I cost both.
- **Stale research quantity:** HR:321 prices "3,840 sq ft" of ICF wall, from the old 100 x 60 ft basement (HR:15). The current basement outline perimeter is 281.3 ft (PF §1.2) and the wall runs from footing top (-14.58) to sill (-1.625), 12.96 ft (STR-01 levels). Computed: 281.3 x 12.96 = **3,646 sq ft**, 5% under the research's figure, so its $135-190K allowance still stands.

## Findings

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|
| COST-01 | Should fix | Basement and pool cluster | **The basement and pool cluster is the largest cost driver, and every structural Blocker comes from it.** STR-01 (ICF wall past the Part 9 table), STR-02 (pit 18'-3" below grade, deep footing narrower than the footing above), STR-03 (26.95 ft pool-room floor span) and PLB-01 (pool drain-down has no destination) all trace to the 12 ft basement plus the pool pit. ICF walls alone, computed: 3,646 sq ft x $35-50 (HR:321) = **$128K-$182K**; the Winnipeg low-end source ($20-30, HR:316) would give $73K-$109K. Whole foundation package at 1.8-2.2x the wall cost (HR:321, "unverified for this scale") = **$230K-$401K** computed. Each foot of basement wall height is 281.3 sq ft = **$9.8K-$14.1K** of ICF alone, computed, before excavation, backfill and the engineering fix. Pool, spa, shotcrete shell, theatre tiers, dehumidification: no data, needs a quote. | PF §1.2 (281.3 ft); STR-01, STR-02, STR-03, PLB-01; HR:316, 321; Redesign:98-100 | — | $$$ |
| COST-02 | Should fix | Part 9 vs Part 3 (STR-04) | **Fixing the 600 m2 problem by trimming is cheapest and the saving is real; the cheapest square feet to cut are garage square feet.** See "Part 9 vs Part 3 costing" below. Decide before the engineer starts (README:68-70). | README §1.1; STR-04; PF §1.1 (garage 833 sf) | — | $ to $$ (trim, net saving) vs $$$ (Part 3) |
| COST-03 | Should fix | Tunnel question | **Keep the Nov 3 decision (no tunnel).** The repo's only tunnel price is $110K-$220K for about 70 ft (SBP:387-390, "unverified"), which is $1,571-$3,143 per ft (computed). The tunnel also forces the shop plant to be built with the house (SBP:397-403, 428-446), which contradicts "house first, shop later". Full argument below. Cheap hedge: the README already requires one spare sleeve for shop lines (README:487-488); add a second spare and record the trench route. | SBP:387-403; Redesign:39; README §2, §8 | — | $ (hedge) vs $$$ (tunnel) |
| COST-04 | Should fix | Heating plant (HR decision #21) | **Geothermal is the biggest HVAC capital line and does not fit the drawn site.** HR:795 carries $70K-$140K+ (unverified at this scale). GAS-10: 10,795 sq ft of free land against 15,000 sq ft minimum for a horizontal loop. Operating cost: gas about $8.30/GJ vs GSHP about $17.50/GJ (HR:817-818), so gas heats at roughly half the cost (HR:824); propane is about $43/GJ (HR:821), worse than GSHP. **The gas-line question decides it (HR:846, decision 8).** Capital for a gas plant: no data, needs a quote. Do not pour the slab before the radiant-tubing decision (GAS-06). | GAS-10, GAS-06, GAS-03; HR:795, 817-824, 846 | needs B149.1 check | $$$ |
| COST-05 | Should fix | Snow melt (GAS-09) | **Default hydronic scope is 737.8 sq ft = $33K-$70K** (GAS-09, from HR:865). Steps and walk only (200 sq ft per HR:886): electric $4K-$12K (200 x $20-60, HR:861) or hydronic $9K-$19K (200 x $45-95), computed. The 538 sq ft garage apron is the expensive part and faces west (GAS-09 point 1). Gold-plating candidate: steps and walk yes (HR:898); apron is a plow job unless Jordan wants it. | GAS-09; HR:861, 865, 886, 898 | needs CEC check (electric) | $$$ (apron) vs $ (steps only) |
| COST-06 | Should fix | Rough-ins before the pour | **Cheap now, tear-out later.** ELE-05/06 (meter-to-panel, well, generator, EV, feeder, melt sleeves), GAS-06 (radiant tubing), PLB-04/05 (ejector, sump discharge), GAS-01/02 (vent chase, meter position) all sit in or under the ICF and slab. After the pour, each means coring ICF or breaking slab. Add them to README §8 now. See fix-now table. | ELE-06; GAS-06; PLB-04; README:466-500 | — | $ now vs $$ to $$$ later |
| COST-07 | Should fix | Wasted space | **Low-value space is priced below.** The main hall system is 891 sf strict (16.2%), 24.3% with foyer, mudroom and stair opening (PF §6.1). The 481 sf spine and the 309 sf foyer are 790 sf of it. Trim opportunity about 160-250 sf without losing a room function (table below). | PF §6.1; ARC-07, ARC-14, ARC-25 | — | $$ |
| COST-08 | Consider | Footprint, corners, roof | Heated envelope: 395.5 ft of perimeter, **17 outside + 13 inside corners = 30** (PF §1.2). An equal-area rectangle at 1.8:1 (assumed aspect) has 309 ft (computed), so the plan carries about 86 ft (28%) more wall. Roof is 16 hip blocks, 64 nominal facets, 9 at 6/12 and 7 porch blocks at 4/12 (PF §1.2), with valleys, girder trusses (STR-13) and the ice-dam detail HR:904 flags. No $/ft price in the repo. Levers: pull the 13 inside corners out (bunk/study notch, den alcove, master porch), and gable or shed the seven 4/12 porch blocks. | PF §1.2; STR-13; HR:494, 904 | — | $$ to $$$ (roof is the largest framing line) |
| COST-09 | Consider | Windows | **The window package is smaller than the research assumed.** The model has 17 main-floor windows (443.9 sq ft of glass = 8.1% of 5,486 sf, computed) plus 2 basement windows (PF §5). At $850-$1,600 each (HR:434), 19 windows = **$16K-$30K**, computed; the research's "six-figure line item" (HR:439) was for the older, glassier model, though glazed doors and the 8 ft units are extra. Triple-pane premium $120-$350 each (HR:436) = **$2.3K-$6.7K** for 19, computed. Triple-pane U <= 1.0 is not gold-plating. Adding the windows Kayla wants (K-064, ARC-19: 27 heated rows have none) is a small cost. | PF §5.1; HR:434-439 | — | $ |
| COST-10 | Consider | Ceilings and porches | 12 ft ceilings on 2,076 sf (kitchen 779, den 438, great room 452, foyer 309, scullery 98; PF §3.1) cost taller walls, MSR studs (HR:495) and heated volume. Porch/patio/deck rows are 2,221 sf (PF §1.1, 40% of heated area) under 7 roof blocks, with posts and beams that need engineering (STR-07, STR-14). No prices. A foyer at 12 ft over a bench and a wine rack (ARC-14) is the weakest value. | PF §1.1, §3.1; STR-07, STR-14 | — | $$ |
| COST-11 | Consider | Pool room (discretionary) | The pool room is 933 sf (PF §3.2); the 15 x 15 pool and 8 x 8 spa are 290 sf of water (computed from STR-02 / PLB-01 dimensions), about 31%. Its 26.95 ft span drives engineered trusses (STR-03). Lever: an intermediate beam line over the pool deck would cut the span toward Part 9 table range, at the price of columns in a humid room. **Ask the engineer; I do not assert it works.** | PF §3.2; STR-03 | — | $$ (no data) |
| COST-12 | Consider | Basement height | HR decision: 12 ft clear (Redesign:11). Lowering the slab by 1 ft saves $9.8K-$14.1K of ICF (COST-01) and reduces the 11.75 ft backfill that puts STR-01 past the Part 9 table (3.70 m wall against a 3.0 m limit). The theatre (13.25 ft ceiling, PF §3.2) and pool need the height. Jordan's call. | STR-01; PF §3.2 | — | $$ |
| COST-13 | Consider | Shop (later) | A 100 x 100 ft steel clear-span building (SBP:150, D11 at 491) is STR-16's "single largest structural cost". No price in the repo; needs a quote. Footprint lever: every 10 ft of depth is 1,000 sf (10%). SBP:471 already calls shrinking the house-shop gap the biggest saving. | STR-16; SBP:150, 471 | — | $$$ |
| COST-14 | Consider | Parents' house | See section below. | IMG_0415, ARC | — | $ |

## Ranked cost drivers

| Rank | Driver | Size from the model | $ tier | What moves it |
|---|---|---|---|---|
| 1 | Basement + pool cluster (ICF, pit, deep footings, trusses, drainage) | 281.3 ft perimeter, 12.96 ft wall, pit 18'-3" deep; ICF $128K-$182K computed | $$$ | basement height (-$9.8K-$14.1K per ft), pool size/position, mid-span support |
| 2 | Heating plant + distribution | 134K-224K BTU/h (GAS-03); GSHP $70K-$140K+ (HR:795) | $$$ | gas vs GSHP; radiant vs forced air; one plant vs two (GAS-06) |
| 3 | Heated footprint and area | 5,486 sf main + 3,475 sf basement; 587-626 m2 incl. garage | $$$ | trim 160-280 sf; hall and foyer area |
| 4 | Roof | 16 hip blocks, 64 facets, girder trusses | $$ to $$$ | fewer blocks, gable the porch roofs |
| 5 | Shop (later) | 10,000 sf steel clear-span, 7 overhead doors | $$$ (later) | shrink depth; defer |
| 6 | Exterior wall and corners | 395.5 ft perimeter, 30 corners, about 86 ft over an equal-area rectangle | $$ | remove inside corners |
| 7 | Snow melt | 737.8 sf default = $33K-$70K hydronic | $$$ if built | steps only = $4K-$19K |
| 8 | Porches/decks | 2,221 sf, 7 roof blocks, long beams | $$ | trim north porches |
| 9 | Heated tunnel | $110K-$220K for 70 ft (SBP:389) | $$$ if reinstated | not built on `main` |
| 10 | Windows | 19 units: $16K-$30K computed; triple premium $2.3K-$6.7K | $ | frame choice (fibreglass vs vinyl, HR:439) |

Septic, well ($15K-$35K plus $5K-$12K treatment, HR:51) and engineering fees are separate lines; the repo gives no engineering fee.

## The tunnel question, argued both ways

**For standalone services at the house (what `main` models):**
- Tunnel cost: $110K-$220K for about 70 ft = $1,571-$3,143 per ft (SBP:387-390, computed per ft). The house-side landing no longer exists. The UTILITY room moved west, and the old landing wall is now the gym/music room (STR tunnel section). A route from the west UTILITY room is at least about 20 ft longer (STR), so **+$31K-$63K** computed at the same per-ft price.
- Buried trench: SBP:388-389 says it "does the same job for a fraction of that"; the 210 ft route is already drawn (site.scad:197) but its real length from the panel is about 293 ft (ELE-03). **No data on trench $/ft, needs a quote.**
- The tunnel must be built with the house (SBP:397-403), putting its cost into phase 1 while the shop is "later" and the land is not chosen. The shop spot 63 ft behind the house is itself a land assumption (site.scad:56-60).
- Reinstating it makes the house depend on the shop plant, a mandatory generator and a feeder up to 447-652 A (ELE tunnel section; GAS tunnel section), and raises fire separation and egress questions between "connected" buildings (SBP:384).
- The house already needs a plant, well and septic of its own to be livable first.

**For the tunnel:**
- One plant, one well, one septic and one service point for the site (SBP:101, D4), instead of two. The duplicated house plant is the saving; the repo has no price for a second boiler plant, so **no data, needs a quote**.
- A walkable, heated house-to-shop route in January (SBP:459-460, "pays for itself in daily use"), with services serviceable under floor grates.
- Trench digging later under a finished back yard is the "expensive way" (SBP:401-403), but only if the tunnel is wanted at all.

**Verdict:** the evidence in the repo favours standalone. The tunnel's cost is high, unverified, front-loaded and tied to an unchosen site; the savings it offers (one plant) have no price attached. If Jordan wants the walk-through in the future, the cheap hedge is the spare sleeves and a kept-clear corridor.

## Part 9 vs Part 3 costing

| Path (README §1.1) | Area effect | Cost relative | Notes |
|---|---|---|---|
| 3. Trim enclosed area | README: about 160 sf (15 m2), enough from 608 m2. From 626 m2: 26 m2 = **280 sf** plus margin (computed, 1 m2 = 10.76 sf). From 608: 86 sf plus margin | **$ to $$, net saving** (less build) | Cheapest sf to remove: garage, which counts fully but is unheated. Garage is 24.34 ft wide, so 160 sf = 6.6 ft of depth, 280 sf = 11.5 ft (computed); depth is 34.21 ft (PF §3.1). Heated candidates: foyer 309 sf, spine 481 sf, slivers 87 sf (below). Measure the true building area first (STR-04) |
| 1. Detach garage | house alone 528 m2 (README) | $$ (second foundation/roof, walkway) | Breaks K-037 / K-115 garage-to-pantry deal-breaker (ARC-03); a roof joining them may make one building again (README:57-58) |
| 2. Firewall between | each side its own building | $$ to $$$ | README: "costly at a house scale" (README:59-62) |
| 4. Accept Part 3 | none | $$$ | README: professional design throughout, many extra rules. The house already needs 11 engineered elements (README §4.3, E1-E11), so the incremental engineering is smaller than for a normal house; the unpriced extras are fire and egress items (other specialists). No dollar data in the repo |

**Recommendation on cost grounds:** trim, using garage depth first, then foyer and sliver cleanup. All fix-later versions of this are cheap before framing and impossible after.

## Wasted-space audit

Price basis: the repo has no $/sq ft for floor area. Relative cost is build + finish + lifetime heat. The only dollar handle: design heat load 15-25 BTU/h per sq ft (HR:783) against GSHP $70K-$140K for 10-16 tons (HR:795), which gives plant capacity of about **$550-$2,900 per 100 sf** (computed; 100 sf x 15-25 = 0.125-0.208 ton x $4,375-$14,000 per ton; an upper bound, since interior halls lose almost nothing through walls). Real waste is in build cost, not heat.

| Space | sf | Why low-value | Possible saving | $ tier |
|---|---|---|---|---|
| Spine hall (24.34,29.51 to 105.2,35.46) | 481 (PF §6.1) | 54% of all hall area; 158 sf overlaps the great-room opening (ARC-07); also the 80 ft master-to-front-door distance | Not by narrowing (Kayla wants wider, K-060); by making it a gallery or shortening the plan | $$ |
| Foyer | 309 | Bench and wine racks only (ARC-14); 12 ft ceiling | 100-150 sf by shortening 8-12 ft | $$ |
| Pass-only slivers: suite-entry 2nd piece 6, stair landing 17, closet passage 44, master entry 20 | 87 (ARC-25) | No furniture | Merge into neighbours | $ |
| Bedroom-wing halls (E-W 84, N-S 76, upper 35, suite entry 47) | 242 | Circulation 230 sf in this wing (ARC) | Little; ARC says only the 6 sf sliver is a lever | $ |
| Basement halls | 423 (12.2%, PF §6.2) | 48 ft x 4 ft hall serves four rooms; 3-row hallway zone with a 0.7 ft sliver | Replan before the partitions (Phase 2) | $ to $$ |
| Windowless FLEX 151, STUDY 97, OFFICE 165 | 413 | Cannot sleep or work well (ARC-19) | Add windows rather than remove rooms | $ |
| Master WICs 95 + 94, passage 44 | 233 | Kayla's requirement (K-201); leave it | none | — |
| Porches/decks | 2,221 | Not conditioned; roofs and beams (STR-07, STR-14) | Trim north porches | $$ |

Recoverable without losing a function: about 160-250 sf. That covers the README trim (160 sf) but not the 626 m2 case (280 sf plus margin) without also using garage depth.

## Bedroom-wing alternatives (ARC "sore spot")

| Option | Area change | Cost relative | Notes |
|---|---|---|---|
| A: widen E-W hall 4.11 to 5.0 ft | 0 net; hall +18.3 sf, bunk -9.3, study -8.9 | **$** (framing change before walls go up) | Gives 55 in clear; three doors can go to 36 in; no noise benefit (ARC-08) |
| B: swap STUDY and LAUNDRY, plus master laundry | 0 net; study +41, laundry -41 | **$$** (moves the wet group and dryer vent) | The new laundry position has 5.4 ft of yard-facing north wall (PF §2.2), which may fix the dryer path (PLB-08); plumbing agent to confirm. Noise moves to the bunk room and sun room |
| Hybrid: rename LINEN to MASTER LAUNDRY (ARC-02) | 0 | **$** | Wall already carries the bath services |

## Parents' house (second pass, photos only)

No door, shower or tub price exists in the repo; all rows are relative.

| Parked decision | Fix now | Fix later | Notes |
|---|---|---|---|
| Curbless shower instead of tub | $ to $$: floor is raised over an accessible crawl space (IMG_0415), so a framing recess is easy before the subfloor | $$ to $$$: tear out finished bath floor, cut joists | The plan shows a tub on the north wall and no walk-in shower (ARC parents table) |
| 36 in doors | $: wider rough openings at framing | $$: reframe walls, move wiring | Scaled doors are about 2.5-3 ft; clear width unconfirmed |
| Ramp/step-free entry | no data; 28 in rise = 28 ft of 1:12 ramp (ARC arithmetic) | $$ and a site change | Four porch steps drawn, no ramp |

## Gold-plating hunt (summary)

- **Likely beyond need:** hydronic apron melt (COST-05); geothermal if piped gas exists (COST-04); 12 ft foyer over a bench (COST-10).
- **Justified by climate and use:** triple-pane (premium $2.3K-$6.7K); 8 in ICF core (required, STR-01); radon rough-in and the waterproofing stack (HR:327 context, "do not value-engineer out"); the sump and backup power for a pool house on a well and septic.
- **Not gold-plating but undefined:** the pool cluster as a whole is the largest discretionary line; no price in the repo.

## Fix-now vs fix-later (every Blocker and Should-fix from the other agents)

"Tear-out" = fixing later means demolishing finished or poured work. Phase markers: **P** = before the basement pour, **F** = before framing, **S** = site/land stage, **L** = safe to defer.

| ID | Item | Fix now | Fix later | When / tear-out? |
|---|---|---|---|---|
| STR-01 | ICF wall past Part 9 table | $$$ (engineered core/rebar, in the quote) | not possible after pour | **P**; later = demolition |
| STR-02 | Pool pit, deep footings | $$$ (geotech first) | not possible after pour | **P**; tear-out |
| STR-03 | Pool-room floor span | $$ (truss design) | $$$ redo floor | **F** |
| STR-04 | Part 9 vs Part 3 | $ to $$ trim (net saving) | $$$ redesign of permits | before engineer |
| PLB-01 | Pool drain-down destination | $$ | $$$ if under-slab piping must change | **P** |
| STR-05 | Added bearing wall x=42.65, beam x=103.04 | $ | $$ cut slab, new footing under finished basement | **P** |
| STR-06 | Garage 16 ft header | $$ | $$ rework wall | F |
| STR-07 | Porch beams, 25.6 ft | $$ | $$ replace beam | F |
| STR-08 | Stair headroom 43 mm margin | $ (fix one opening size) | $$ rebuild stair | F |
| STR-09 | Stair header, ICF wall-top restraint | $$ | $$ | **P/F** |
| STR-10 | Areaway/patio frost wall | $$ | $$$ retaining wall rebuild | **P** |
| STR-11 | Post at (49.69, 5.83) | $ | $$ | P |
| STR-12 | Frost depth 4 ft | $ to $$ (land) | $$ | S |
| STR-13 | Bearing-wall plan for trusses | $ to $$ | $$ truss redesign | F |
| STR-14 | Porch/deck floors | $$ | $$ | F |
| ELE-01 | Service size 200 vs 400 A | $$ (larger sleeves and gear) | $$$ service upgrade | **P** (sleeves) |
| ELE-02 | Do not size for shop and parents | $ (utility talk) | $$$ if wrong | S |
| ELE-03 | Shop feeder 293 ft not 210 | $$ (spec) | $$ | L |
| ELE-04 | Shop trench pinched by septic | $$ | $$ | S (route now) |
| ELE-05 | Meter-to-panel route | $ | $$ core ICF | **P**; tear-out |
| ELE-06 | Missing rough-ins list | $ | $$ to $$$ | **P**; tear-out |
| ELE-07 | Generator and transfer | $$ | $$ | F (panel space now) |
| ELE-08 | Pool/spa heater fuel | $$ | $$ | **P** (sleeves) |
| PLB-02 | Septic sizing | $ to $$ | $$ | S |
| PLB-03 | Master-wing drains 120-145 ft | $$ | $$$ rework in floor | **F** |
| PLB-04 | Ejector, sump, vents | $$ | $$$ under-slab | **P** |
| PLB-05 | Weeping tile discharge | $ to $$ | $$ | **P** |
| PLB-06 | Treatment discharge | $ to $$ | $$ | F |
| PLB-07 | Hot-water recirculation | $$ | $$ (pipe in walls) | F |
| PLB-08 | Laundry dryer exhaust | $ to $$ | $$ | F |
| PLB-18 | Shop wash-bay drains | $ (drawing) | $$ | L |
| GAS-01 | UTILITY room vents | $$ | $$$ move plant | **P/F** |
| GAS-02 | Meter under window | $ | $$ | **P** (sleeve) |
| GAS-03 | Heat-loss calc | $ (fee) | avoids $$-$$$ oversizing | F |
| GAS-04 | Pool heat recovery | $$ | $$$ | F |
| GAS-05 | Make-up air | $ to $$ | $$ | F |
| GAS-06 | Radiant vs forced air | $ (tubing) | **impossible after pour** | **P**; tear-out |
| GAS-07 | Pool heat source | $$ | $$ | P (sleeves) |
| GAS-08 | Propane tank | $ to $$ | $$ | S |
| GAS-09 | Snow melt | $ (sleeves) | $$$ breaking drive and apron | P/S |
| GAS-10 | Geothermal loop land | $$$ | cannot add later | S (buy land) |
| SITE-01 | Grading and drainage | $ to $$ | $$ | S |
| SITE-02 | Sump discharge | $$ | $$ | **P** |
| SITE-03 | Drive past bedrooms | $ | $$ move drive | S |
| SITE-04 | Snow storage | $ | $ | L |
| SITE-05 | Protect septic field | $ | $$ | S |
| SITE-06 | Tank next to wing | $$ | $$ | S/F |
| SITE-07 | Loop field not reserved | $$ to $$$ | land purchase | S |
| SITE-08 | Truck turn-around | $$ | $$ | S |
| SITE-09 | Septic flows for parents, shop | $ to $$ | $$ | S |
| SITE-17 | Drive extension over tank | $ now | $$$ retrofit | L |
| SITE-18 | Shop drainage | $$ to $$$ | $$ to $$$ | L |
| ARC-01 | Drive/garage doors face bedroom wing | $$ | $$$ | S/F |
| ARC-02 | Master laundry | $ | $$ | F |
| ARC-03 | Garage-to-pantry door | $ | $$ | F (before slab for risers) |
| ARC-04 | Closets on exterior walls | $ | $$ | F |
| ARC-05 | Narrow doors | $ | $$ reframe | F |
| ARC-06 | Curbless showers | $$ (floor recess) | $$$ | **F**; tear-out |
| ARC-07 | Circulation spine | $$ (area) | impossible | F |
| ARC-08 | Bedroom noise adjacency | $ to $$ | $$ | F |
| ARC-09 | Powder room | $$ | $$$ | F |
| ARC-10 | Kitchen layout | $ to $$ | $$ cabinets | F |
| ARC-12 | Bunk room | $ | $ | F |
| ARC-14 | Entry/drop zones | $ to $$ | $$ | F |
| ARC-15 | Library/bedroom count | $ | $$ | F |

## If the tunnel architecture is reinstated

Priced in the tunnel section above: $110K-$220K for about 70 ft (SBP:389, unverified), plus about $31K-$63K if the route is 20 ft longer (computed). Other dollars: no data, needs a quote.

## plan_facts corrections

None. One caution: PF §1 uses 608 m2 (calibrated to the permit README), Redesign:574 says 626 m2; STR-04 already flags the conflict.

## Citation log

| Finding | Command | Doc | PDF page | Article as printed | Quote |
|---|---|---|---|---|---|
| — | none: this file makes no code claims | — | — | — | — |
