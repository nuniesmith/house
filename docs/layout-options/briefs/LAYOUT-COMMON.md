# Layout options — common rules (binding for options A, B and C)

You design ONE layout option for the new main floor. Your strategy is in your prompt; the brief is `$RUN/briefs/layout-options.md` (the run document's Layout Options brief, verbatim). The coordinator (Opus) compares A, B and C on a fixed matrix. Jordan and Kayla choose. Nothing you make merges into `main`'s models in this run.

`RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`

## Where you work

- **Worktree:** `/home/user/house-layout` (branch `layout-options`). Your folder: `/home/user/house-layout/docs/layout-options/option-<x>-<slug>/` (letter and slug are in your prompt).
- **Write ONLY** inside your folder, plus scratch under `$RUN/work/OPT-<X>/`.
  - Don't touch `models/`, `tools/`, other options' folders, or anything else in either checkout.
  - Don't commit, don't switch branches, and don't run `tools/make_drawings.py`.
  - The coordinator commits and pushes your folder.
- **Read-only inputs:**
  - `$RUN/plan_facts.md`: the current model's measured facts. Your numbers must use the same definitions.
  - `$RUN/renders/current_main_floor_plan.png`: the current plan.
  - `$RUN/review/REVIEW-SUMMARY.md`: the review's Blockers and Should-fixes, and the Kayla compliance picture.
  - `$RUN/findings/*.md`: the specialists' full findings, especially `01-architecture-flow.md` and its Kayla cross-check table, which is your scoring list.
  - `$RUN/kayla_checklist.md`.
  - The plan images in `/home/user/house/docs/house/`.
  - The code library: `python3 ~/code-library/search.py`. The citation rules in `$RUN/briefs/COMMON-RULES.md` apply to any code claim you make.

## What you build

1. **`main_floor_<x>.scad`**: a compilable variant of the main floor.
   - Start from a copy of `/home/user/house/models/main_floor.scad` and keep its structure and table formats exactly (`main_rooms`, `main_doors`, `main_windows`, `main_fixtures`, `main_furniture`, `main_porch_steps`, `main_posts`, `main_roof`, the `audit` echo), so the existing tools read it.
   - Change its `use <house_lib.scad>` line to `use <../../../models/house_lib.scad>`.
   - House conventions: units are feet, x = east, y = north; rooms are wall-centre-line rectangles; a door/window x,y is the LOW end of the opening, not the centre.
   - Keep a short header comment saying what the option is and what changed.
2. **Basement.** If your stair, wet walls or any load path moves, check the basement against it (`/home/user/house/models/basement.scad`).
   - If the basement must change, make `basement_<x>.scad` the same way. Check it, render it, and list it as a departure.
   - At minimum, show that the stair top and foot land where they work on both levels: the stair table is in `house_lib.scad` (`stair` in `python3 /home/user/house/tools/model_data.py` output).
3. **The checker must pass.** Run `python3 /home/user/house-layout/tools/check_layout.py <path-to-your-scad>` (and on the basement variant if you made one). It must print `OK`. Save the output to `check_layout.txt`.
4. **Renders**, legible on a phone. Open them and check:
   - The plan: `python3 $RUN/scripts/plot_plan.py <your scad> <folder>/plan_<x>.png --title "Option <X> — <name>"`.
   - The 3D view: `xvfb-run -a openscad -o <folder>/3d_<x>.png --imgsize=1800,1300 -D show_roof=false --viewall --autocenter --camera=<a view from the south-east, above> <your scad>`. Make sure it shows the rooms; adjust the camera until it does.
5. **Plan facts, with the same definitions as Phase 0:** `python3 $RUN/scripts/plan_facts.py --main <your scad> [--basement <your basement scad>] --out $RUN/work/OPT-<X>/facts` (variant mode; usage and limits in `$RUN/scripts/README-variant.md`). It writes `matrix.md` (most of your Matrix numbers, computed the same way as the current model's `$RUN/computed/matrix.md`) and `plan_facts.md`. Copy both into your folder (`plan_facts_<x>.md`, `matrix_<x>.md`). Run it again after every layout change, and make sure the room `kind` and labels (MASTER, LAUNDRY, SCULLERY/PANTRY, FOYER, MUDROOM, GREAT ROOM/LIVING, VESTIBULE, POWDER) let it find your rooms. Put the results in `plan_facts_<x>.md`, with:
   - the room table with areas;
   - main-floor conditioned area;
   - **building area to the outside face of the walls, in m², against the 600 m² Part 9 limit** (method of PF §1 / `docs/permit/README.md` §1.1: the attached garage counts, porches don't);
   - circulation % (strict, and with the foyer);
   - the door-width counts and the minimum hall clear width;
   - wet-wall groups, groups stacked over the basement, the drain-run index, and the water heater → furthest fixture distance;
   - the §7 daily paths and the §8 adjacency facts;
   - stair fit;
   - what changes in the basement/shop/site.
6. **`PROS-CONS.md`**, the decision document for your option. Sections in this order:
   1. **Matrix numbers** (exactly these rows, numbers only):
      - Kayla PLAN items IN / MISSING / CONTRADICTED (of N);
      - deal-breakers met (of the deal-breaker list in ARC's summary);
      - review Blockers fixed / open (of N);
      - circulation % (strict / with foyer);
      - drain-run index (ft), wet-wall groups, groups stacked over the basement;
      - single doors under 32" / 32–35" / 36"+, and the minimum hall clear width;
      - a no-threshold shower (Y/N);
      - bedrooms sharing a wall with the living/great room;
      - a bedroom next to the foyer (Y/N);
      - the master bed → laundry path (ft);
      - the master suite's side;
      - bedrooms with east light;
      - living spaces facing south;
      - living spaces with windows on 2+ walls;
      - building area (m², outside face) against 600;
      - basement/shop/site changes (list);
      - cost vs the current model ($ / $$ / $$$ up or down).
   2. **What it is**: one paragraph, plus what changed vs the current model.
   3. **Pros**: each tied to evidence (a plan-facts number, a K-number, a review finding it fixes, a code item).
   4. **Cons**: the same.
   5. **Kayla compliance**: re-score EVERY item ARC classed PLAN, with the same verdicts (IN / MISSING / CONTRADICTED), in a table: K-ID | verdict | evidence | change vs the current model. Then the counts, and the misses and contradictions named.
   6. **Review Blockers**: each Blocker in `REVIEW-SUMMARY.md`, marked fixed / open / not applicable, with evidence. Satisfy the code Blockers, or list exactly which stay open.
   7. **Cost drivers**: $/$$/$$$ vs the current model, naming the 2–3 things that move the price. Use relative terms unless the repo's research gives a range (cite it).
   8. **What you give up**: one honest line.
   9. **Departures** from the shop, site, septic (west), well (east), basement and envelope: each drawn, listed and costed, or "none".
7. **`README.md`** in your folder: 5 lines on the option, then the status: complete, or exactly where you stopped and what's left.

## Rules

- **No adjectives without numbers.** Every pro and con cites a number, a K-item, a finding ID or a code citation.
- **Keep the envelope.** Keep the shop, site, septic (west), well (east) and basement unless your strategy genuinely can't. Any departure is drawn, listed in Cons, and costed.
- **No stamped-engineer claims.** Structural moves (a new bearing line, a long span) are flagged for the licensed Alberta engineer.
- **If the session limit hits,** write your status into your folder's README first, and save what you have.
- **Final message to the coordinator (300 words or fewer):** the Matrix numbers block, your top 3 pros and cons, the "what you give up" line, the checker result, and your folder path.
