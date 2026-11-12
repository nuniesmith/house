# Round-3 review panel (binding for the three reviewers)

`RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`

You review the round-3 layout option **H (knuckle hub)**, comparatively against round 2. A second option, G (a pinwheel block), was stopped without a plan; its `README.md` in `.../round-3/option-g-pinwheel-hub/` says why. Don't review G. H lives in `/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/`, with:
- `main_floor_<x>.scad` and `basement_<x>.scad` (+ the forked `house_lib_<x>.scad`);
- `plan_<x>.png`, `basement_plan_<x>.png`, `3d_<x>.png`;
- `matrix_<x>.md`, `plan_facts_<x>.md`, `routes_<x>.md`, `envelope_<x>.txt`;
- `PROS-CONS.md`, `README.md`.

The brief they were built to is `$RUN/briefs/ROUND3-BRIEF.md`. Read it first: it's the yardstick. Round 3 exists because Kayla found round 2's D, E and F too linear, with daily routes walking through the living rooms.

**Comparison columns:** H, plus round 2's **D** and **F** and **today's model**:
- **D** (`docs/layout-options/round-2/option-d-compact-l/`) was round 2's recommended option, 2,934 sq ft.
- **F** (`.../round-2/option-f-your-sizes-fitted/`) is Kayla's Nov 11 list drawn compactly, 3,910 sq ft.
- **Today's model:** `$RUN/computed/matrix.md`, heated footprint 5,685 sq ft at the outside face.

Round 2's findings for D and F are in `docs/layout-options/round-2/review/`. Reuse their numbers for those columns; don't re-review D or F.

## Rules

- **Read-only.** Don't edit, create or commit anything in `/home/user/house-review` or `/home/user/house`. Your ONLY deliverable is `$RUN/findings/r3-<your file>.md`. Scratch work goes under `$RUN/work/R3-<prefix>/`.
- **Re-measure, don't trust.** The coordinator re-runs every option's numbers independently:
  - `python3 $RUN/scripts/plan_facts.py --main <main> --basement <base> --out $RUN/work/R3-<prefix>/<x>`
  - `python3 /home/user/house-review/tools/check_layout.py <main> <base>`
  - Cite the numbers you measure. Where an option's own PROS-CONS disagrees with your measurement, say so with both numbers.
- **Code citations:** only from the library (`python3 ~/code-library/search.py`), exactly per `$RUN/briefs/COMMON-RULES.md` "Code citations", with a **Citation log** table in that exact format, under a heading that reads exactly `## Citation log` (no number), so the coordinator's verifier finds it. Never cite from memory. CEC (wiring) and CSA B149.1 (gas) aren't in the library: write "needs CEC check" / "needs B149.1 check".
- **No stamped-engineer claims.** Structural items are review items for a licensed Alberta engineer.
- **PRIVACY (binding): the repo is PUBLIC.** Never write a stair lift's weight rating, or anything about anyone's health, mobility, body or age. Use generic accessibility wording ("future mobility aids", "a stair lift").
- **Findings format, exactly as round 1:** `| # | Severity | Option | Location | Finding | Evidence | Code / standard | Cost impact |`, with severity Blocker / Should fix / Consider.
  - Number the findings with your prefix, starting at 01 (round 3 is a fresh file).
  - The **Option** column is H.
- **After the findings**, a comparison table: one row per criterion you own, with the columns H, D, F and today's model, with numbers. Then a 3-line verdict: how H compares on your criteria, and what it would take to fix its worst items.
- **Final message (250 words or fewer):** counts by severity per option, your 3-line verdict, and your file path.

## Reviewer briefs

### R3-ACC: Accessibility, flow and Kayla's notes (`$RUN/findings/r3-accessibility-kayla.md`, prefix `ACC`)

0. **Daily routes, the reason for round 3.** Run `python3 $RUN/scripts/routes.py <main> --md` on H with `--extended` (14 trips), and on round 2's D and F for the comparison. Report each route's walk and every living room passed through. Then check the result by eye on the plans: name any route the script finds that a person wouldn't actually walk, or one it misses. The brief's targets are 0 pass-throughs and a total walk ≤ 420 ft.
1. **Independent Kayla re-score** of H on the 164 items ARC classed PLAN (`$RUN/findings/01-architecture-flow.md`), with the round-1 rulings (`/home/user/house-review/docs/layout-options/kayla-rescore.md`):
   - a garage-wall closet = exterior;
   - a drive that's only noted, not drawn, doesn't count;
   - a kitchen crossing needs a clear lane outside the work zone;
   - a flush shower with a stated recess counts.
   - Write `$RUN/work/R3-ACC/rescore.json` as `{"H": {"K-001": "IN", ...}}`, with every PLAN item and verdicts IN / MISSING / CONTRADICTED.
   - In the findings file, give the counts table (IN / MISSING / CONTRADICTED, the 12 deal-breakers met, and each designer's self-score). List every item where you disagree with the designer: K-ID, your verdict, evidence.
2. **Accessibility audit** per option:
   - a 1,700 mm turning circle in the entry, kitchen, every bathroom and the laundry (ABC 3.8.4.3.(4), p.318; measure the clear space on the plan);
   - a step-free route house → garage and house → deck (3.8.4.3.(3));
   - door widths; hall clear widths (≥ 5 ft is the brief's target);
   - curbless showers;
   - the elevator: a stacked 6 × 7 ft on both levels at the same x/y, with a 5 × 5 ft approach off the hub;
   - **the hub's daylight:** how it's lit (glazing, clerestory, skylight) and whether it would read as dark;
   - the stair: straight, one flight, ≥ 42 in clear, landings top and bottom.
3. **Flow and daylight:** the daily paths (garage → kitchen with groceries; primary bed → toilet at night; primary bed → laundry; entry → powder room; kitchen → dining). Every bedroom and living room has an exterior wall + window, there are no dark interior living rooms, and the depth is ≤ 40 ft. Noise: bedrooms vs the living room and the basement theatre.
4. **Program check:** each option's rooms against the brief's round-3 sizes and Kayla's own sizes (in range / under / over). The library, primary and kitchen are kept at her sizes; flag any that aren't.

### R3-CODE: Code and structure (`$RUN/findings/r3-code-structure.md`, prefix `CS`)

Per option, cited from the library:
1. **Stair:**
   - flight height ≤ 3.7 m (9.8.3.3);
   - rise and run within Table 9.8.4.1;
   - width; headroom (9.8.2.2: compute it from the stair, the opening and the 1.625 ft floor depth);
   - landings (9.8.6.3);
   - handrails.
2. **Basement bedroom egress (9.9.10.1, p.873).** For each bedroom and murphy-ready flex room:
   - a window ≥ 0.35 m² unobstructed, with no dimension < 380 mm (estimate a casement's clear opening from the rough size, and state your assumption);
   - a window well ≥ 760 mm clear;
   - smoke alarms (9.10.19) and CO (9.32.3.9) as needed.
3. **Part 9 applicability.** Building area with the garage (1.3.3.3; the "building area" definition), by the matrix method.
4. **Structure, for the engineer:**
   - the basement wall height vs the ICF table at a 10 ft basement (Table 9.15.4.2.-A; slab top to main floor = floor_to_floor − 1.625 ft);
   - the main-floor spans over the basement (Table 9.23.4.2.-A/-B);
   - the roof span across each plan's depth (trusses) and the interior bearing lines;
   - the elevator shaft (framed opening, pit in the basement slab);
   - the garage door header;
   - any long opening.
5. **Garage ↔ house:** the door (9.10.13.15), the air barrier (9.10.9.18.(4)), and whether the step-free entry the option chose works with the garage slab and drive grades.
6. **Window wells and guards:** wells deeper than 600 mm next to a walkway need guards or covers (9.8.8.1). Search the library; cite only what you find.

### R3-PMC: Plumbing, mechanical and cost (`$RUN/findings/r3-plumbing-mech-cost.md`, prefix `PMC`)

1. **Plumbing:**
   - wet-wall groups and stacking between floors;
   - the drain-run index (matrix);
   - basement fixtures need an ejector (NPC 2.4.6.3, as round 1 cited): is a spot drawn?;
   - the drain exit toward the septic side (west);
   - cleanout distances (NPC 2.4.7.1(6), round 1).
2. **Septic:** the bedroom count per option → the SOP design flow (Table 2.2.2.2.A; round 1 PLB-02 used 3 bedrooms = 3,055 L/day). The tank stays ≥ 1 m from the new house walls (SOP 4.2.2.1). Check against the new footprint and the `site.scad` tank at x −3..3, y 52–64.
3. **Mechanical:**
   - the room is on an exterior wall, so the boiler, water heater and HRV can vent outdoors (round 1 GAS-01; ABC 9.33.5.5: no combustion air from a crawl space);
   - the DHW distance to the furthest fixture (matrix);
   - the laundry dryer-vent path to an exterior wall;
   - the hot-tub sunroom if drawn (humidity/exhaust, ABC 9.32).
4. **Cost, relative to today's model and to each other.** Use only the repo research ranges (`docs/house/House-Review-and-Research-2026-10-28.md` and round 1 COST findings `$RUN/findings/07-cost-ve.md`, cited by line). Otherwise "no data — needs a quote". Rank the drivers:
   - heated footprint (sq ft) and envelope perimeter/corners;
   - basement area and ICF wall area (perimeter × height at a 10 ft basement vs today's 12 ft: round 1 priced ICF at $35–50/sq ft of wall, HR:321);
   - roof form;
   - porches;
   - the elevator rough-in (no repo price: say so);
   - the stair;
   - plumbing groups.

   Give a $/$$/$$$ table vs today's model and vs round 2's D and F, and say plainly where H sits on cost between D and F, and by what driver. `python3 $RUN/scripts/envelope.py <main> <base>` gives the perimeter and corners.
