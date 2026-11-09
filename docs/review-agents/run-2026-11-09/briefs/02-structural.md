# Agent brief — Structural (Sonnet)

You review whether the geometry can stand up, and what it assumes. You are a reviewer, not the engineer of record — every Blocker you raise is phrased as "requires a licensed Alberta engineer's design/confirmation", never as a design.

**Inputs:** `plan_facts.md`, SCAD models (main floor, basement, shop, site), code library (ABC 2023 — Parts 4 and 9 span tables via `search.py`).

**Check:**
- Load paths: do upper walls/point loads land on structure below, floor by floor, down to the ICF basement walls? List every load that lands mid-span or on nothing.
- Spans: floor and roof spans vs ABC Part 9 span tables (cite table/article from the library). Anything beyond Part 9 tables = Part 4 territory, flag it.
- ICF basement: wall height vs backfill height, openings (windows/doors) interrupting walls, the stair openings.
- The basement stair question: the U-stair in the former bar area — headroom, opening size, support around the opening.
- Shop: 100×100 ft — what structure does the model imply for those clear spans? Flag as the single biggest structural cost/risk item if unresolved.
- Heated tunnel (~70 ft, floor at basement level): retaining, waterproofing, and the joint where it meets the basement UTILITIES wall.
- Parents' house: crawl-space foundation, floor 2'-4" up, porch roof posts + the egg-chair hook (500 lb design load, doubled joist + through-bolted eye — verify the model shows structure there).
- Snow load: land isn't chosen, so state the assumption range across Alberta (cite ABC climatic data article) and flag which design choices change if the land is foothills vs prairie.

**Output:** standard format. Every span claim cites the library. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/02-structural.md`. **Prefix:** `STR`.

1. **Stale premises (PF §13).** The basement "U-stair in the former bar area" is from the OCTOBER model. Review the CURRENT stair: straight, from the upper hall running ~15¾ ft south (`models/main_floor.scad:10-16`, Redesign-and-Spec §2, PF §10), plus the basement exit stair. The tunnel goes only in the "If the tunnel architecture is reinstated" section.
2. **Part 9 vs Part 4.** `docs/permit/README.md` §1.1/§7 say the building area is 626 m² against the 600 m² Part 9 limit. Find the scope article in the library (the README cites Div. A 1.3.3.3; verify it). State what changes structurally if the house leaves Part 9 (engineered Part 4 design of the whole structure vs Part 9 prescriptive spans).
3. **Use the model's structural tables** (`python3 tools/model_data.py > $RUN/work/STR/model.json`): `bearing_lines`, `deep_footings`, `piers`, `frost_walls`, `main_posts`, `main_roof`, `levels`, `pool`, `spa`, `theatre`, `exit_stair`; `models/foundation.scad`; and the `floor_assembly` module in `main_floor.scad`. Spans come from those tables and PF, not estimates. The large basement rooms (pool, theater) under main-floor rooms are the obvious long-span suspects. Measure them.
4. **Basement:** 12 ft clear ICF (Redesign Nov 2 update), pool + spa shells, theater tiers, two light wells, the exit-stair areaway. Check openings in the ICF walls, and the backfill height against grade (`site.scad` header: grade 2 ft below the main floor).
5. **Shop:** a later phase, modelled in `shop.scad`. One finding on the implied clear spans, labelled "later phase".
6. **Snow load:** state the Alberta range from the library's climatic data (search abc_2023 for the climatic table and snow-load entries; quote locations as printed). Say which design choices change between foothills and prairie values.
7. **Parents' house:** a second pass, short, from `docs/small_house/` only.
