# House Review Run — Sunday Kickoff Document

_One document, everything the run needs. Prepared 2026-11-07; run after the Claude usage reset, Sunday 2026-11-08, 5:00 p.m. ET._

**Scope update (Jordan, 2026-11-08 evening): this run now has TWO deliverables.**
1. The multi-agent **review** of the current plan (Parts 1–2, Phases 0–3).
2. **Three layout options for the new floor plan** (Phase 4–5 + the Layout Options brief in Part 2), each drawn and modelled, with detailed pros and cons scored against Kayla's notes and the review findings, and a coordinator recommendation. Jordan and Kayla choose the final layout from the options — **no option becomes the plan in this run**, and the models on `main` stay untouched.

## How to start (Jordan)

1. Open a Claude Code session on **oryx**, in `~/github/house`.
2. Paste the kickoff prompt below.
3. The session runs the specialists on Sonnet in waves of 2, with Opus coordinating — per Part 1.

**Kickoff prompt (copy-paste — also in `KICKOFF-PROMPT.md`):**

> You are the coordinator (Opus) for a multi-agent house plan review and layout-options run. Work in ~/github/house on this machine (oryx). I (Jordan) will be away from the desk for much of this run — work autonomously inside the scope below and check in at the milestones listed at the end, verdict first.
> 
> BEFORE SPAWNING ANYONE:
> 1. `git checkout main && git pull --ff-only`. Confirm HEAD includes docs/review-agents/HOUSE-REVIEW-RUN.md with the layout-options phase (Phase 4). Report the HEAD hash.
> 2. Read docs/review-agents/HOUSE-REVIEW-RUN.md end to end. That document governs this run: the runbook and repo map (Part 1), the agent briefs (Part 2), and Kayla's notes (Part 3). If anything in this prompt and that document disagree, the document wins.
> 3. Sanity-check your tools and report all three results in your first reply:
>    - Code library: `python3 ~/code-library/search.py --doc abc_2023 "spatial separation"` returns hits.
>    - `openscad --version` works (PNG renders will need `xvfb-run -a openscad`).
>    - `python3 tools/check_layout.py --help` or an equivalent dry check shows the layout checker is runnable.
> Then give me your wave plan in a few lines and start Phase 0 without waiting for my reply.
> 
> THE RUN (per the document):
> - Phase 0: one Sonnet sub-agent extracts plan_facts.md from the SCAD models — specialists work from those numbers, not from vibes.
> - Phases 1–3 (review): specialist waves on Sonnet, at most 2 sub-agents at a time, each briefed with its Part 2 section plus plan_facts.md. Enforce the citation rule: a code citation that doesn't reproduce via ~/code-library/search.py gets bounced, not published. Kayla's notes are requirements — mismatches are findings, and Architecture/Flow owns the full cross-check of Part 3. Review specialists edit nothing.
> - Phase 4 (layout options): three options for the new floor plan, one Sonnet agent each, waves of 2, on the layout-options branch ONLY (models on main stay untouched): A = evolve the current model, B = the as-drawn sheet (docs/house/floor_plan.JPEG, geometry only — its printed dimensions are unreliable) with Kayla's notes applied, C = clean sheet inside the same envelope planned from Kayla's notes outward. Each option ships: a compilable SCAD variant passing tools/check_layout.py, a readable labelled top-down floor-plan render plus one 3D render, its own plan facts (same measures as Phase 0), and a detailed pros/cons sheet scored against Kayla's notes — including its Kayla-compliance count, cost drivers, and one honest "what you give up" line.
> - Phase 5 (decision pack): you score A/B/C on the document's fixed matrix, give a ranked recommendation with the reasoning shown (and note cheap hybrids, e.g. one option's kitchen inside another), and end with the choice framed for me and Kayla. The final layout choice is ours — do not select a final plan and do not merge any option into main's models.
> 
> HOUSE RULES:
> - Findings and pros/cons need evidence: a plan_facts number, a file/line, a render, or a reproducible code citation (doc + PDF page). No adjectives without numbers behind them.
> - No stamped-engineer claims: structural and gas items are review items for a licensed Alberta engineer, flagged as such. CEC and CSA B149.1 are not in the library — mark those items "needs CEC/B149 check", never cite them from memory.
> - PR status is explicit in every report: ✅ ready to merge only if the PR is clean on its own head; otherwise ⛔ not ready, and why.
> - If the session limit hits mid-run, stop cleanly: push what's done, and note in the PR where the run stopped and which wave resumes first.
> 
> CHECK IN WITH ME (verdict first, short):
> 1. After Phase 0 — the headline plan facts and anything already obviously wrong.
> 2. After the review waves — the draft's top Blockers and the Kayla's-notes compliance picture.
> 3. When both PRs are up — review PR and layout decision pack PR, with links and status.
> 
> Start now.
---
# Part 1 — Runbook

# House Review Run — Sunday Runbook

**When:** after the Claude usage reset, **Sunday 2026-11-08, 5:00 p.m. ET**.
**Where:** Claude Code session on oryx, in `~/github/house`.
**What:** (1) a multi-agent plan review of the house (main house + shop + site; parents' house as a second pass if time allows), and (2) three layout options for the new floor plan with a decision pack (Phase 4–5, Jordan's call 2026-11-08). Review specialists make no model edits; layout variants live only on the `layout-options` branch. The final floor plan is built in a later run, after Jordan and Kayla choose an option.

## Model assignments (Jordan's call, 2026-11-06)

- **Specialist sub-agents run on Sonnet** — they do the reading, measuring and checking.
- **The coordinator runs on Opus** — it oversees: merges the specialists' findings, enforces the citation rule, builds the conflict table and the decision list. This is the usual pattern for this household: Sonnet builds, Opus reviews.
- **At most 2 sub-agents at a time** (standing rule — the shared session limit kills background agents mid-task; worktrees survive, resume after reset if it happens anyway).

## Where everything is (repo map — verified on oryx 2026-11-08)

- **Repo:** `~/github/house` on oryx (github.com/nuniesmith/house). Read from `main`; the only writes in this run are the review branch and the `layout-options` branch.
- **SCAD models:** `models/main_floor.scad`, `models/basement.scad`, `models/foundation.scad`, `models/house_lib.scad` (shared room/door/window tables — door/window x,y is the LOW end of the opening, not the centre), `models/house_combined.scad`, `models/export.scad`, `models/shop.scad`, `models/site.scad`.
- **Model tools:** `tools/check_layout.py` (layout options must pass it), `tools/make_drawings.py`, `tools/model_data.py`. OpenSCAD is `/usr/bin/openscad` **on oryx only**; PNG export needs `xvfb-run -a`.
- **Floor-plan images:** `docs/house/floor_plan.JPEG` — the architect's layout sheet (its auto-generated labels/dimensions are unreliable — do not model from its numbers; its geometry matches the current model). Drawn plans: `docs/house/main_floor_plan.png`, `docs/house/main_floor.jpg`, `docs/house/basement_plan.png`, `docs/house/basement.jpg`. Elevations/sections: `docs/house/house_front.png`, `house_back.png`, `section_a.png`–`section_e.png`, `cutaway.png`, `house_exploded.png`, `site_plan_house.png`. Shop/site: `docs/shop/*.png` (floor plan, site plan, tunnel section, 3D). Parents' house plan photos: `docs/small_house/IMG_0415.PNG`–`IMG_0420.PNG`.
- **Prior work:** `docs/house/House-Review-and-Research-2026-10-28.md` (the 23-item decision list), `docs/house/Redesign-and-Spec-2026-11-02.md`, permit set at `docs/permit/House-Drawing-Set.pdf` (+ `docs/permit/README.md`).
- **Code documents:** the five PDFs live in the repo at `docs/codes/` (ABC 2023 Alberta Edition, National Plumbing Code 2020, NECB 2020, Alberta Electrical Utility Code 2022, Alberta Private Sewage SOP 2021). The **searchable** copy is the index at `~/code-library/` on oryx (`search.py` + `codes.db`) — citations come from there, per the runbook. Not available: CEC Part I (house wiring) and CSA B149.1 (gas) — flag "needs CEC/B149 check", never cite from memory.
- **Kayla's notes:** Notion original (for Jordan/Kayla): https://app.notion.com/p/Home-Build-40f879a556f180ea8ae5f12afc36fe01 — agents work from the frozen in-repo copy: **Part 3 of this document** and `docs/review-agents/KAYLAS-NOTES.md`. Do not rely on reaching Notion from the agent session.

## Inputs (all on oryx)

- Models: `~/github/house/models/*.scad` (main_floor, basement, house_combined, shop, site) + drawn plans/renders in the repo docs.
- Prior review: `docs/house/House-Review-and-Research-2026-10-28.md` (the 23-item decision list — specialists check what's still open, don't redo what's decided), plus `docs/house/Redesign-and-Spec-2026-11-02.md`.
- **Kayla's notes (design intent — READ THESE):** Kayla's Notion "Home Build" notes, handed over by Jordan 2026-11-08. Full text is **Part 3 of this document** (also `KAYLAS-NOTES.md` / `docs/review-agents/KAYLAS-NOTES.md`). These are requirements, not background colour: room-by-room wishlists, accessibility needs (wide doors/hallways, no-threshold shower, generous clearances), noise and public/private separation, wet-wall grouping, cardinal-direction placement, storage, the mistakes-to-avoid list, and the things-she-doesn't-like-on-plans list. Every specialist checks the plan against the sections that touch their brief, and any mismatch is a finding (severity by impact, "Kayla's notes" as the evidence source). Where the model already reflects one of her earlier edits, verify it's actually there — present/absent, with evidence.
- **Code library:** `~/code-library/` — full text of ABC 2023 (Alberta Ed.), NPC 2020, NECB 2020, Alberta Electrical Utility Code 2022, Alberta Private Sewage SOP 2021, indexed in `codes.db`.
  Query: `python3 ~/code-library/search.py [--doc <stem-prefix>] "<fts query>"` — full-text syntax, phrases in quotes. `--page <doc-prefix> <n>` dumps a whole PDF page.
  Doc prefixes: `abc_2023`, `electric_2022`, `National_Energy`, `plumbing`, `sewage`.
- Assumption set (do not re-litigate): build is in **Alberta** (land not yet secured — snow load and other site values stay flagged as assumptions); roof colour blue, product parked; Kayla's edits are design input; shop (100×100, utilities bay) powers the house via the heated tunnel; well east, septic west by the utility room; parents' house (no basement, crawl space) ties into services later.
- Known open question the run must NOT resolve: the main-floor baseline — Kayla's edited layer vs the as-drawn sheet — is Jordan's pending A/B call. Review the model **as it stands on main** and list the divergence as an assumption in the report.

## Kayla's notes — how this run uses them

- **Architecture / Flow owns the full cross-check:** every item in Part 3 gets a verdict — in the model, missing, or contradicted — starting with her deal-breakers: laundry far from bedrooms, traffic through the kitchen work zone, closets on exterior walls, bedrooms sharing a wall with the living room, a bedroom next to the foyer, the garage/driveway past the master suite or bedrooms, and having to go through the master bath to reach the closet.
- **Plumbing / Septic:** wet-wall grouping, laundry next to (and connected to) the master suite, Costco door from pantry to garage, dog bath near the rear entrance, pet-bowl water filler.
- **Site / Landscape:** cardinal directions (south = living/backyard/driveway, north = master suite, east = bedrooms/sunroom), and no driveway past the master suite or bedrooms (noise).
- **Cost / VE:** design in 2-ft increments where the plan can, grouped wet walls, simple forms — flag where the plan fights these and what it costs.
- **Coordinator:** the final report includes a short **Kayla's-notes compliance summary** — how many items checked, how many are in / missing / contradicted — and any conflict between her notes and another specialist's fix goes in the conflict table for Jordan and Kayla to decide, not resolved silently.

## Phases

**Phase 0 — Plan facts (1 Sonnet agent, solo).**
Read the SCAD models and produce `plan_facts.md` in a scratch branch/worktree:
room table (name, dims, area), door/window schedule, wall runs, plumbing fixture list with locations by floor, wet-wall map, electrical service/panel facts, distances (house↔shop tunnel run, house↔septic, well↔septic), circulation area total vs floor area. Every number sourced to a file + line or a render measurement. Specialists review THESE numbers, not vibes.

**Phase 1 — Specialist waves (Sonnet, 2 at a time).**
Wave 1: Architecture/flow + Structural.
Wave 2: Site/Landscape + Plumbing/septic.
Wave 3: Electrical + Gas/HVAC.
Wave 4: Cost/value-engineering + Code (Code also sanity-checks the other specialists' citations against the actual code text).
Each specialist gets: its brief (`agents/<name>.md` in this folder), `plan_facts.md`, the renders, and the code library. Each returns findings in the standard format (below) and nothing else — no file edits.

**Phase 2 — Coordination (Opus).**
Coordinator brief: `agents/coordinator.md`. It dedupes, **bounces any finding whose code citation doesn't check out against `search.py` output**, builds the cross-trade conflict table (e.g. plumbing wants stacked wet walls vs architecture wants the open plan), and produces the final review doc: verdict first, findings by severity, conflict table, decision list ordered so land/site decisions come before the design freezes they gate — same shape as the Oct 28 review Jordan already used.

**Phase 3 — Delivery.**
Final review lands in the repo as a document on a branch + PR, per household rules (Jordan merges). Coordinator states PR status explicitly: ✅ ready only if it's a clean docs PR; this run changes no models.

**Phase 4 — Layout options (Sonnet, 2 at a time; Jordan's call 2026-11-08).**
Using the review findings, `plan_facts.md`, and Kayla's notes (Part 3), build **three** genuinely different layout options for the new main-floor plan. One Sonnet agent per option, waves of 2. Each option is a strategy, not a tweak:
- **Option A — Evolve the current model.** Same footprint, basement, stairs, shop and site. Fix the review's Blockers and Kayla's deal-breakers with the smallest moves that honestly fix them.
- **Option B — The as-drawn sheet, with Kayla's notes applied.** Start from the arrangement on `docs/house/floor_plan.JPEG` (geometry only — its printed dimensions are unreliable) and apply her edits and notes to it. This makes the parked A/B baseline question concrete and decidable.
- **Option C — Clean sheet inside the same envelope.** Re-plan the floor from Kayla's notes outward — public/private split, grouped wet walls, laundry tied to the master suite, broken-open living, cardinal orientation — keeping the same overall footprint, basement, shop and site unless a departure is listed and costed in the option's cons.
Deliverables per option, in `docs/layout-options/option-<a|b|c>-<slug>/` on the `layout-options` branch: a compilable SCAD variant of the main floor (reusing `models/house_lib.scad` conventions; `tools/check_layout.py` must pass), a **readable, labelled top-down floor-plan render** plus one 3D render (`xvfb-run -a openscad` on oryx), the option's own plan facts (room areas, circulation %, door/hall widths, wet-wall/plumbing run lengths, stair and tunnel-landing fit), and a pros/cons sheet (template in the Layout Options brief). Basement/shop/site change only where an option truly needs it — and then it's drawn, listed, and costed, never silent.

**Phase 5 — Decision pack (Opus coordinator).**
The coordinator scores all three options on the fixed matrix in the Layout Options brief, writes the comparison + a ranked recommendation with its reasoning, and lands it as the top document of the `layout-options` PR. The pack ends with the decision Jordan and Kayla have to make — it does not make it. After they choose, a later run turns the chosen option into the final floor plan; nothing from the options branch merges to `main`'s models before that choice.

## Standard finding format (every specialist, no exceptions)

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|

- Severity: **Blocker** (can't build / won't pass), **Should fix** (real cost or function loss), **Consider** (judgement call for Jordan/Kayla).
- Evidence: a plan_facts number, a SCAD line, or a render — never "typically" or "usually".
- Code / standard: article number **as returned by the code library search**, with doc + PDF page. A citation the coordinator can't reproduce gets bounced, not published.
- Cost impact: rough order only ($ / $$ / $$$) unless real price data is in the repo. Say "unknown" rather than inventing a number.

## Hard rules

1. **Review specialists: no edits.** No SCAD edits and no commits by review specialists; their only output is findings. **Layout agents (Phase 4) are the one exception:** they may create variant SCAD and renders, only on the `layout-options` branch, never on `main`. The coordinator's writes are the review document and the decision pack, each on its own branch + PR.
2. **No stamped-engineer claims.** Findings are review items for Jordan and, where flagged, for a licensed Alberta engineer — structural and gas especially.
3. **Known library gaps — flag, don't fake:** house wiring is governed by the Canadian Electrical Code, which is NOT in the library (the electrical doc on hand is the utility code); the gas code (CSA B149.1) is also not in the library. Electrical and gas agents cite what the library has and mark the rest "needs CEC/B149 check" instead of citing from memory.
4. **Two agents max, always.** Waves, not a swarm.
5. If the session limit hits mid-run: worktrees and finished wave outputs survive; resume the run from the last completed wave after the reset.

---

# Part 2 — Agent briefs

---

# Agent brief — Architecture / Flow (Sonnet)

You review how the house lives: movement, space use, furniture fit. You do not review structure, services, or code beyond clearances you can cite.

**Inputs:** `plan_facts.md`, main-floor + basement renders/drawn plans, parents'-house plan, the Oct 28 review's open items.

**Check:**
- Circulation: trace every daily path (entry→kitchen, bedrooms→bath, garage→kitchen with groceries, basement↔main). Total the hall/circulation area from plan_facts and state it as a % of floor area — flag waste.
- The known sore spot: the 2–3 bedroom + hallway arrangement on the main floor. Propose at most 2 concrete alternatives with the area math for each.
- Door swings: conflicts, doors hitting fixtures/furniture, travel through one room to reach another.
- Furniture fit: primary bed (king), bedroom closets usable depth, kitchen work triangle and island clearances, dining seats.
- Kitchen: Kayla's two-path requirement; laundry open from both sides; bedroom→closet direct access — verify each is actually in the model as it stands, report present/absent with evidence.
- Kayla's notes (Part 3): you own the full cross-check described in Part 1 — every wishlist / mistakes-to-avoid / don't-like item in your scope gets an in-model / missing / contradicted verdict, incl. wide doors and hallways, no-threshold shower and bathroom clearances, public vs private grouping, noise separation (closets/bathrooms as buffers), broken-open (not open-concept) living, sight lines (no view of a toilet, bedroom or laundry from public areas), scullery/butler's pantry, mudroom and entry drop zones, and storage where things are used.
- Parents' house: aging-in-place — door widths, bathroom layout, step-free potential, porch egg-chair zone clearances.
- Sight lines and dead corners: space that exists on plan but can't hold furniture or storage.

**Output:** findings in the standard format (runbook). Alternatives costed in area (sq ft gained/lost), not dollars. No model edits.

---

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

---

# Agent brief — Site / Landscape (Sonnet)

You review everything outside the walls: grading, drainage, access, and the ground the systems sit in. The buildings' insides belong to the other agents; the land is yours.

**Inputs:** `plan_facts.md` (distances especially), `models/site.scad` + shop/site models, code library: ABC 2023 (`--doc abc_2023` — lot grading/drainage, §9.14) and the Sewage SOP 2021 (`--doc sewage`) for field protection rules.

**Check:**
- Lot grading: does the site model grade AWAY from both houses and the shop on all sides? Where does roof and surface water actually go — and does any of it end up at the septic field, the well, or the neighbours?
- Driveway and apron: the shared drive, the 80-ft truck apron, turning room for the Volvo VNL with a trailer — can Jordan get in, turn, and get out in winter without driving on the septic field or the geothermal loops?
- Snow management: where does plowed snow get piled, where does meltwater run in spring, and do the piles block the septic field, the well head, doors, or the heated walkways' drainage?
- Septic protection: field + reserve area marked and kept clear of driveway, apron, parking, snow piles and future buildings — permanently, not just on this drawing (SOP — cite it). Tank pump-out access from a drivable surface in all seasons.
- Well protection: well head (east side) clear of fuel storage, shop wash water, septic (verify the separation from the site model, don't re-derive the plumbing agent's numbers — cross-check them), and surface runoff directed away.
- Geothermal loop field: siting vs septic field, well, driveway, trees, and future parents'-house work — any overlap is a Blocker (coordinate with the Gas/HVAC agent's siting).
- Parents' house siting: position on the lot vs the main house (spatial-separation distance is the Code agent's call — flag the measurement for them), its own grading, septic tie-in route, and a step-free path potential from the drive.
- Trees and planting: root distance from septic lines/field and foundation; windbreak/snow-drift effects on the driveway and doors (planting that drifts the drive shut is a finding); defensible space for rural fire risk.
- Shop yard drainage: wash-bay and apron runoff — where does it go, and confirm it can never reach the well or the septic field.

**Output:** standard format. Distances quoted from plan_facts/site model, SOP and ABC cites from the library. No model edits.

---

# Agent brief — Plumbing / Septic (Sonnet)

You review water in, waste out — the house, the parents' house tie-in, the shop bathroom, and the septic system.

**Inputs:** `plan_facts.md` (fixture list + wet-wall map), models, code library: National Plumbing Code 2020 (`--doc plumbing`) and the Alberta Private Sewage SOP 2021 (`--doc sewage`).

**Check:**
- Wet-wall stacking: do main-floor and basement fixtures share walls/stacks? Measure the horizontal drain runs from plan_facts; every long run is cost + freeze + cleanout findings (NPC cleanout rules — cite them).
- Fixture-unit load vs the proposed stack/building-drain sizes (NPC — cite the sizing articles you use).
- Venting: any fixture group that can't vent within NPC distance rules given the layout.
- Septic (SOP 2021 — cite the SOP itself, not memory): tank and field separation distances vs the site model (well east, tank west by the utility room, field further west, ≥ required clearance from BOTH the main-house basement and the parents'-house crawl space); system sized for the combined flow of both houses + shop bathroom; tank within pump-out reach of a drivable surface; field kept out of the tunnel alignment and off the shop apron (never driven on).
- Shop bathroom: the gravity run west along Bay 1 vs the septic tank position — does it work by gravity, or does it need the lift station? Decide from elevations in the model, and price both ways in the finding.
- Shop wash bay: confirm NO path from wash-bay drainage to septic (oil/grit separation instead) — Blocker if ambiguous.
- Freeze protection: any supply/drain in exterior walls or the tunnel; the parents'-house crawl space plumbing.
- Hot water: tankless in the parents'-house mech closet; main-house DHW from the boiler plant — distance/wait-time to the furthest fixture.

**Output:** standard format, SOP/NPC citations from the library only. No model edits.

---

# Agent brief — Electrical (Sonnet)

You review the electrical scheme: service, distribution, and the shop-powers-house architecture.

**Inputs:** `plan_facts.md`, models (shop, site, tunnel), code library: Alberta Electrical Utility Code 2022 (`--doc electric`) for service/utility requirements.

**Hard limit:** the library does NOT contain the Canadian Electrical Code (house wiring). Cite the AEUC where it applies (service entrance, metering, utility side) and mark every wiring-level item "needs CEC check" — never cite a CEC article from memory.

**Check:**
- Service architecture: shop is the service point; house keeps a 200A panel fed from the shop. Feeder run length through the tunnel from plan_facts — voltage-drop finding at 200A over that distance, and the conductor implication (state the math).
- Load inventory: build the demand list from the plans — house (incl. pool equipment, DHW/heating plant auxiliaries), shop (welder, compressor, lift, wash bay), heated driveway/walkways, tunnel heating, EV/truck charging, parents' house later. Total it against the service size the AEUC process would approve; flag if the architecture needs 400A.
- Generator: size and transfer — what stays live (heating plant, well pump, septic pumps) vs what sheds.
- Separation/coordination: feeder in the heated tunnel with plumbing and gas — clearances and what shares the tunnel.
- Parents' house: fed from where, what size, and does its later tie-in force a service upgrade now?
- Future-proofing findings: conduit/rough-in that is cheap now and expensive later (porch hook lighting, shop expansion, solar-ready).

**Output:** standard format; load table included. Every number shown with its arithmetic. No model edits.

---

# Agent brief — Gas / HVAC (Sonnet)

You review the heating plant and everything it feeds: house heat, pool, domestic hot water, snow melt, the heated tunnel, the shop, and geothermal.

**Inputs:** `plan_facts.md`, models, code library: ABC 2023 (`--doc abc_2023` — ventilation §9.32, energy §9.36) and NECB 2020 (`--doc National_Energy`) for the shop.

**Hard limit:** the gas code (CSA B149.1) is NOT in the library. Review gas routing and appliance siting as layout findings; mark code-specific gas items "needs B149.1 check" — never cite it from memory.

**Check:**
- One plant or several: the plan puts the heating plant in the shop utilities bay (boiler for pool + DHW + snow melt + house heat, geothermal backup). Heat load rough math per building from plan_facts areas; is one plant credible, and what fails when it's down? (Single point of failure finding — house heat depends on the tunnel run.)
- The tunnel as a utility run: heating mains house↔shop, freeze risk if the plant stops mid-winter, insulation/heat-trace findings.
- Distribution in the house: radiant vs forced air vs hybrid — what do the plans imply, and what does the basement pool do to humidity/ventilation (§9.32 cite)?
- Geothermal: loop field siting on the site model — conflicts with septic field (west), well (east), shop apron, driveway. Flag any overlap as a Blocker.
- Snow melt: heated driveway + walkways — zones, load on the plant, and the run from the shop plant to the house driveway.
- Shop heating: 100×100 with a wash bay — NECB applies; unit heaters vs radiant tube; wash-bay humidity.
- Gas service: meter/regulator location relative to the shop utilities bay; the parents'-house supply later (gas or electric — state the trade-off as a finding for Jordan).
- Radon: Alberta is high-radon; ABC rough-in requirements (coordinator will want the Code agent to confirm the article — cross-reference, don't duplicate).

**Output:** standard format; plant load table with arithmetic shown. No model edits.

---

# Agent brief — Cost / Value Engineering (Sonnet)

You review where the money goes and where it's wasted. You get the other specialists' findings (from the earlier waves) plus `plan_facts.md` — your job is the price tag on the design and on their findings.

**Inputs:** `plan_facts.md`, models, Oct 28 research doc (materials/windows/geothermal research already in the repo — use its ranges, don't invent new ones), specialists' findings from the earlier waves.

**Check:**
- Cost drivers, ranked: footprint and corner count, roof complexity, ICF basement vs alternatives, the 100×100 shop structure, the heated tunnel, the pool, snow-melt area, window area/ratings for Alberta winters. Give each a $/$$/$$$ and say what design change moves it.
- Wasted-space audit: from the architecture agent's circulation % and your own read — every 100 sq ft of low-value space is a build-cost + lifetime heating cost finding. Price the waste.
- The tunnel question, honestly: total cost of the heated-tunnel architecture vs the alternative (standalone services at the house). This is the biggest single VE item in the project — both directions argued with numbers.
- Parents' house: cost effect of the parked decisions (curbless shower vs tub, 36" doors) so Jordan can decide with prices attached.
- Finding-by-finding: for each Blocker/Should-fix from the other agents, add the cost of fixing it now vs the cost of living with it or fixing it later. "Fix later" that means "tear out finished work" gets said plainly.
- Gold-plating hunt: anything specified beyond what the Alberta climate or the household's actual use justifies.

**Rules:** use ranges from the repo's research or say "no data — needs a quote". Never present a made-up point estimate as a fact. Standard format. No model edits.

---

# Agent brief — Code, Alberta (Sonnet)

You check the plans against the actual code text. You run LAST: you verify the project against the code, and you spot-check the other agents' citations.

**Inputs:** `plan_facts.md`, models + drawn plans + `docs/permit/House-Drawing-Set.pdf`, ALL other specialists' findings, code library: ABC 2023 (`--doc abc_2023`), NECB 2020, NPC 2020, AEUC 2022, Sewage SOP 2021.

**Check (Part 9 first — cite everything from the library):**
- Egress: bedroom window egress sizes/openings (§9.9), basement egress, exit doors.
- Stairs: geometry, guards, handrails (§9.8) for both stairs — including the U-stair in the former bar area — plus headroom.
- Spatial separation between houses (§9.10.15 — the main house and parents' house are two buildings on one lot; limiting distance from the site model) and exposure to the shop.
- Fire/smoke: smoke and CO alarms (§9.10.19), fire separations garage↔house.
- Radon: rough-in requirements (§9.13) — Alberta.
- Energy: §9.36 tier — what the design must hit; what documentation the permit will need. Shop under NECB (or Part 9? determine and say which, with the article).
- Health/safety details: bathroom clearances, window guards where required, deck/porch guards (both porches, back decks).
- Septic: SOP sign-off items — certified installer, site evaluation, permit — listed as process findings.
- Permit readiness: read the drawing set in `docs/permit/` against what a permit submission needs; list what's missing as findings (this is a checklist gap list, not a redesign).

**Citation duty:** for every code citation in the other seven agents' findings, re-run their article through `search.py`. Confirm or flag each one in an appendix table. A citation you cannot reproduce is reported to the coordinator as unverified — plainly, without softening.

**Output:** standard format + citation-verification appendix. No model edits.

---

# Agent brief — Layout Options (Sonnet)

You design ONE of the three layout options for the new main floor (your coordinator assigns A, B or C — strategies defined in Part 1, Phase 4). You work from evidence, not taste: `plan_facts.md`, the review findings (Blockers first), Kayla's notes (Part 3), the floor-plan images in `docs/house/`, and the code library for anything code-bound.

**Build:**
- A compilable SCAD variant of the main floor on the `layout-options` branch, under `docs/layout-options/option-<letter>-<slug>/`, following `models/house_lib.scad` conventions (door/window x,y = low end of opening). `tools/check_layout.py` must pass on it — run it and include the result.
- Renders: one readable, labelled top-down floor plan (the decision document — Jordan reads these on a phone) and one 3D view. Render on oryx with `xvfb-run -a openscad`.
- The option's plan facts, same measures as Phase 0 so options compare cleanly: room table with areas, circulation % of floor area, door and hallway widths (Kayla's accessibility items), wet-wall count and total plumbing run length, stair fit against the basement, tunnel landing, and what (if anything) changes in basement/shop/site.

**Pros/cons sheet (detailed — this is what the decision is made from):**
- **Pros** and **Cons**, each item tied to evidence (a plan-facts number, a Kayla's-notes item, a review finding it fixes or leaves, or a code item). No adjectives without a number or a citation behind them.
- **Kayla's-notes compliance:** count from the Architecture agent's cross-check list — how many items this option satisfies, misses, or contradicts, naming the misses.
- **What you give up:** one honest line — the option's real cost, stated plainly (space, money, a wishlist item, a harder build).
- **Cost drivers:** $/$$/$$$ vs the current model, naming the two or three things that move the price.

**Rules:** keep shop, site, septic (west), well (east) and the heated tunnel as they are unless your option genuinely can't — a departure is drawn, listed in Cons, and costed. Satisfy the review's code Blockers or list exactly which ones remain open in your option. Two agents max in flight; if the session limit hits, your branch work survives — note where you stopped in the option folder.

---

# Agent brief — Coordinator / Overseer (Opus)

You oversee the run. Specialists (Sonnet) produce findings; you turn eight stacks of findings into one decision document Jordan can act on. You do not do specialist work yourself — you judge theirs.

**Inputs:** runbook, all specialist findings, `plan_facts.md`, the Oct 28 decision list, the Code agent's citation appendix.

**Your jobs:**
1. **Enforce the evidence rule.** Any finding without a plan_facts number, a file/line, or a reproducible code citation gets bounced back or cut — never published. Say in the report how many findings you cut and why (one line, no drama).
2. **Dedupe and merge.** The same wall will appear in four reports. One finding, all perspectives attached.
3. **Build the conflict table.** Where specialists disagree or their fixes collide (plumbing's stacked wet walls vs architecture's open plan; cost's tunnel challenge vs the whole shop-powers-house architecture), lay out: the conflict, each side's evidence, what it costs each way, and what Jordan has to decide. Do not pick winners on genuine value calls — price both and hand him the choice. Do pick winners where the code or the physics has already decided.
4. **Sequence the decisions.** Final decision list ordered so site/land decisions (snow load, septic siting, well) come before the design freezes they gate — same discipline as the Oct 28 list. Mark which of the Oct 28 items this run closes, and which remain open.
5. **Verdict first.** The report opens with: is this plan buildable as drawn, what are the top 3 risks, and what's the single most expensive surprise hiding in it. Then findings by severity, conflict table, decision list.
6. **Respect the parked items.** The main-floor A/B baseline question (Kayla layer vs as-drawn) is Jordan's unmade call: state it as an assumption at the top of the report, do not let any specialist's finding quietly presume either answer. Roof product is parked. Land-dependent numbers stay flagged as assumptions.
7. **Layout decision pack.** Score Options A/B/C on the fixed matrix — Kayla's-notes compliance count, review Blockers fixed, circulation %, plumbing run length, accessibility (door/hall widths, no-threshold shower), public/private and noise separation, orientation/daylight, basement/shop/site fit, cost drivers — one row per criterion, one column per option, numbers not adjectives. Give a ranked recommendation with the reasoning shown, including what the recommended option gives up. End the pack with the choice itself, framed for Jordan and Kayla (including hybrids: "B's kitchen inside A" is a legitimate answer — note which hybrids are cheap to combine). The decision is theirs; your job is to make it easy, not to make it.
8. **Delivery.** Write the review as one document on a branch in the house repo, open a PR, and report its status explicitly (✅ ready to merge only if it's a clean docs PR). The layout options and decision pack go on the separate `layout-options` branch + PR, also reported explicitly. No model files on `main` change in this run.

**Tone of the report:** Jordan reads verdict-first, on a phone, between other things. Short sentences, tables for comparisons, plain language for trade terms on first use.

---

# Part 3 — Kayla's Notes (full text)

_Kayla's Notion page "Home Build" (https://app.notion.com/p/Home-Build-40f879a556f180ea8ae5f12afc36fe01), exported by Jordan and handed over 2026-11-08. Reproduced verbatim (spelling as in the original). This frozen export is the copy agents work from — do not rely on reaching Notion from the session. This is the design-intent source the specialists check against — see "Kayla's notes — how this run uses them" in Part 1._

---

# Home Build

[Floor Plans](https://app.notion.com/p/Floor-Plans-413879a556f18017bcc5c3cbdee03716?pvs=21) 

- one story (no stairs to reach essential areas)
- basement for honeybun
- Wider doorwars/hallways to accomodate size & potential mobility aids
- More space in areas like bathroom/shower/to walk around furniture d/t size
- Driveway not past master suite or bedrooms - noise!
- Considerate of cost/complications - group “wet walls” for plumbing runs where possible
- Consider which spaces need daylight/windows
- Consider which rooms need noise protection/quiet and which rooms are noisy to ensure proper noise separation (i.e. bedrooms somewhere quiet away from main areas, bathrooms not direct to main areas for privacy)
- Which rooms are public vs private, group accordingly - shouldn’t have to walk through private area to reach public
- Consider building materials come in 2’ increments - working with those measurements reduces extra costs

Lot Notes

- Cardinal directions play a big role in determining placement & plan
- Ideal directions
    - South - living spaces, backyard, driveway (for snow melt)
    - North - master suite (cooler)
    - East - bedrooms for morning light, sunroom (southeast)
    - West

Building Notes

- Place blocking in walls during framing where anything will be wall mounted - towel racks, toilet paper holders,
- Recess into wall behind fridge to reduce protruding into aisles - needs a 2x6 wall
- Exhaust fan in laundry room - especially if no window
- In wall insulation for noise protection between rooms - should consider for all bedrooms, office, library, laundry, bathrooms
- Consider dutch doors - good for pet control (or kids), ventilation in hot weather

Space Planning Notes

- Somewhere to sit/hangout so not isolated when cooking in kitchen or close to living room with open concept
- TV/large tablet space in kitchen for entertainent & recipes
- Outdoor cooking space for BBQ that’s covered and easily connected to kitchen
- Scullery/Butler’s pantry
    - keep small appliances off main kitchen counters
    - appliance storage for things like waffle maker/crock pot/etc
    - baking zone with stand mixer and break maker
    - shallow storage for pantry - things don’t get buried
    - Upright freezer for extra storage
    - Hide the microwave in here
    - Lots of storage for food - like to stock up, emergency stores, buy in bulk
- Home office with some privacy/noise separation - quiet place to study or work
- Home library with floor to ceiling bookshelves and cozy seating/reading area that’s relatively quiet
- Access to bathroom from all living zones (office, library, living room, kitchen/dining) and entries (front and mudroom) without crossing the whole house
- Somewhere to sit outside that’s bug free - sunroom or screened in porch - maybe convertible windows that open
- Direct access to dining room from kitchen - hate having to walk through living room, or around or through pantry, down a hallway
- Laundry room next to and connected to master suite either through bathroom or closet - or a second W/D in master bath
- Pantry directly adjacent/connected to garage with a costco door for ease of unloading groceries
- Broom & vacuum closets - more than one so not hiking across whole house
    - Home for robot vacuum to dock
- Linen closets near bedrooms/bathrooms vs. storing all linens in laundry room
- Adding a vestibule at the front entry - air lock for heat/cool control, privacy
- Storage - think about things where we use them and need storage
    - Mail drop zone/command centre near entrance
    - Somewhere to drop purse/keys/wallets near entrance
    - Blankets & pillows for the couch and extras for the beds
    - Pet food - near bowls, pet leashes near door etc.
    - Shoes in doorway - tend to kick off
    - Random shit like board games & puzzles, coolers
    - Cleaning supplies in every room (or close) - no central location or we won’t clean as often
    - Maximize by avoiding or utilizing dead voids - blind corners, over fridge, under stairs, garage ceiling, attic
- Pet Peeves I want to fix
    - Clothes always end up on floor - kick laundry baskets - on floor, basket where I actually take off my clothes
    - Walking into the bedframe - generous clearance around bed, clear path from door
- Accessibility needs - current and potential future
    - No threshold walk in shower
    - Shower bench and foot notches
    - Bathtub with steps in and out - no large step over
    - Leave empty space for elevator?
    - Dumb waiter! these were so smart
    - Wide walkways - not skinny people plus future walker/wheelchair use
    - Wide doorframes - again not skinny, plus easier to move furniture

Notes on Interior Design/Architecture

- Not open concept, not totally closed off - broken open
    - Use half walls with glass or shelf partitions, pocket or barn doors, pony walls, full glass partitions
- Living spaces should have windows on 2 walls
    - If not possible, use skylights or mirrors to add additional light
- Avoid creating glare on TVs/monitors/computers with side facing light
    - Avoid backlight and light directly across
- Need soft surfaces in large rooms - especially open concept to absorb noise and reduce echo
- Simple forms/shapes are more efficient for insulation, water seal, keeping bugs out etc. - need to take extra care at every 90 degree joint
- Closets = insulation - avoid on exterior walls as they can create condensation
    - Ideally closets should be entirely on interior walls
- Ideal exhaust placement has toilet between shower and door with exhaust fan over shower
    - Water closets require separate exhaust fan
- Bathtubs on exterior walls cause water to cool down faster
- Avoid having 2 wings separated by great room - causes issues with running duct work
- Rooms should have a focal point - somewhere to draw your eye
- Window placement
    - Don’t place windows directly across from each other (within room, or envelope)
    - Want to place on a diagonal to promote cross breeze through entire room, not direct path
    - Create pressure systems to pool in cool air by having larger windows placed lower and smaller windows higher in elevation
    - Don’t place windows in centre of room - create dark corners/edges, pull windows to corners to create light reflection off walls
    - Consider shading windows with overhangs especially hottest West facing windows for energy efficiency
- Golden Ratio is 1:1.4 to 1:1.6
    - Room dimensions that meet these ratios feel more comfortable
    - Long wall points the eye
        - Should hold your sofa as well
    - Reduces echo
- Ranch style houses
    - Linear - garage on one end, bedrooms on the other
    - L shaped, one wing public, one private, private back patio
    - U shaped - surround central patio
    - V shaped - ?no examples
- Managing daylight
    - Consider path of sun - northern hemisphere, most sunlight on N side
        - E - morning light, noon - N, evening - W
    - Covered patios - light fades off significantly after 4-5m, too deep and light doesn’t reach interior living areas
        - Leave open tops like pergola style with retractable roof cover
        - Reduce depth or reposition to allow light to reach living area windows unobstructed
    - Kitchen counter runs (especially if using overheads) should go on inside walls
    - Square shaped building - interiors are very dark
        - Shallow building depth allows sun to warm interior areas in winter
    - Considerations
        - Active spaces should be nearest the sunlight - living room, dining room, kitchen and have access to nature
        - Bedrooms should be positioned to receive morning light - circadian rhythm
- Consider views & sightlines
    - Bathrooms should never open to toilet
    - Should not have a direct view of bathrooms from entry, couch, dining table, bed
    - Should not have a direct view from public area into bedroom door
    - Should not have direct view of laundry room from public area
- 

Room Wishlist

- Kitchen
    - large island - no seating
    - breakfast nook - bench ok on one side, need to have some chairs
    - Prefer nothing in island (sink/cooktop)
    - No upper cabinets, full size ok
    - All drawers/pull outs - no cupboards
    - XL fridge & range
    - Wall ovens
    - Elevated dishwasher? - possible to stack 2 dishwasher like the ovens?
    - Walk in pantry/butler’s pantry with space for small appliances
    - Costco door in pantry - share wall with garage
    - Kitchen near rear entrance - close for unloading groceries
    - Coffee bar near breakfast nook - pot filler to fill coffee maker
    - Glass rinser
    - Instant hot water tap
    - Pot filler for stove
    - Extra freezer storage (deep freeze in pantry)
    - Microwave not under or overhead
    - Face living areas from island
    - Ideally sink under window
    - Pull out island extension - lower height - seated prep or extra seating?
    - Workstation sink - single bowl or 70/30, side drain
- Dining Room
    - Access to outdoor kitchen/dining area
    - Seats 8
    - Fully openable doors to outside?
- Living Room
    - Gas fireplace
    - TV/media center
    - Room for sectional + chairs
    - Access to outdoor patio or sunroom
    - Fully openable doors to outside?
    - Every seat have easy access to side/coffee table
    - Built in storage
    - Place to store blankets/pillows
    - Pet stuff - cat tree/dog bed
    - Ceiling fan
- Entry
    - Somewhere to sit and put on shoes
    - Coat storage for guests
    - Hidden coat/shoe storage
    - Drop zone
    - No direct line of sight to messiest areas - kitchen/living?
    - Powder room near front door
- Mudroom
    - Seating to put on shoes
    - Easy access shoe storage
    - Coat hooks
    - Hidden coat storage
    - Seasonal storage - winter boots, hats, etc
    - Drop zone!!
    - Hooks for bags
    - Mail organizer area - command center
    - Garbage/recycle chutes to garage?
    - Outdoor entrance
    - Garage entrance
    - Bathroom or powder room off mudroom
- Laundry
    - Near master suite? or a second laundry in/next to master
    - washer/dryer raised to waist height
    - Pull out shelf to rest basket on
    - Pull out/down hang to dry racks
    - Pull out/down ironing board
    - laundry sink
    - Lots of storage for soap/cleaning supplies
    - Rod for hanging clothes on hangers
    - Pull through laundry basket from master?
    - Storage for linens
    - Garbage for lint
- Pets
    - Pet bowl area with water filler (kitchen v mudroom)
    - Dog bath near rear entrance (mudroom v laundry)
    - Integrated space for cat/dog beds (counters/shelves) (mudroom?, library, living)
    - Cat litter area (connect to garage?) - mudroom?
    - Dog door to mudroom?
    - Cat wall climbers (anywhere, stylish)
- Library
    - Floor to ceiling bookshelves (at least one wall, preferably 2 or more)
    - Comfy seating - oversize chair, loveseat/couch, window seat?
    - Fireplace?
- Anywhere features
    - Window seat - library, living room, bedroom, ?
    - At least one full bathroom not through a bedroom
- Office
    - Lots of desk space to spread out
    - Built in storage/shelves
    - French or barn door?
    - Access to porch?
    - Shared with Jordan or shared with craft space?
- Sunroom
    - Full walls of windows/glass
    - Open to patio (french doors)
    - Windows open to screens - screened in porch
    - Room for comfy lounge furniture (couch/chair)
    - Small dining set for 4
- Master Suite
    - Bedroom
        - TV on wall
        - Access to private porch
        - No fireplace
        - Ceiling fan
        - Extra AC blowers
        - Lots of room to walk around bed
        - Pet sleep area - dog/cat beds/tree
        - Dog/cat door
        - Chairs
        - Bench at end of bed
    - Closets
        - Separate walk in closets
        - Access from bedroom NOT JUST bathroom
        - Access from bath ok as long as not only way into
        - Access to laundry or through bathroom
        - Kayla
            - More drawer/easy access storage
            - Pull out pant racks
            - Hooks
            - Space for jewelry
            - hooks/rings for scarves/hats, etc
            - Shoe storage
            - Floor/kick laundry or pass through basket to laundry
    - Bathroom
        - Large walk in shower - lots of elbow room, no step/barrier
        - Bench seat in shower
        - Alcoves in shower for shampoo
        - Hooks in shower for back brush
        - Precise temperature control
        - Hand shower right next to bench
        - Fan/cooling in shower?
        - Foot notch in wall to raise leg
        - Somewhere to put water bottle in easy reach
        - Sunken bathtub - large enough for HB and maybe 2?
        - Steps up to bath for ease of access
        - Shelf space next to tub for soaps
        - Somewhere to put drink while in bath
        - Double sink vanity or totally separate vanities
        - Lots of storage next to vanity
        - Closed storage for towels? or in laundry?
        - Water closet - potentially 2 - spacious/wide
        - Access to laundry?
        - Access to closets?
        - Makeup vanity with built in storage and storage for hot tools
        - Built in hair dryer with seat
- Craft/Hobby/Flex Room
    - Lots of desk space for crafts
    - Lots of storage
    - Desk chair and space for laptop
    - Comfy chair for crochet?
    - Pull out island? with rolling stolls
    - Arranged so a bed can be added or a day bed or murphy bed in room
- Guest Room
    - At least one set up with queen size bed
    - Ensuite
    - Private access? from porch or garage
- Bedroom 3 & 4?
    - Additional bedrooms for future planning - extra guests, kids?
    - Potentially other uses in meantime
    - Jack & Jill bath
- One small bedroom/flex room near Master for nursery?
- Front Porch
    - Porch swing
    - Couple of chairs & table
    - Covered
- Covered Entry to Mudroom
- Back Patio
    - Outdoor kitchen counter tops
    - BBQ/smoker/blackstone
    - Dining table for 6-8 under cover
    - Lounge area with sofas and chairs and coffee table  under cover
    - Open area to sit in sun
    - Place to sit and work outside - small desk/table and chair

Room Notes

- Kitchen
    - Clear counter tops on either side of cooktop and sink as landing zones - min. 15”
    - Landing zone near fridge for putting groceries away - 30 to 60”
    - Work triangle
        - Fridge - Sink - Range
        - Outdated now? originally designed for single person small kitchens
        - Still somewhat applicable
        - No more than 9’ per side, 26’ total journey
    - No direct line of sight to kitchen mess from entry (keep semi-private)
    - Try to centre features - sink tap or range on fireplace, sink on window, etc.
    - Zones - new way to organize/plan your kitchen, potentially replace work triangle
        - Zones:
            - Consumables - fridge, pantry
            - Non-Consumables - dishes, etc.
            - Prep - cutting boards, sink, knives, prep bowls, etc
            - Cooking - range, ovens, pots, pans, oven mitts, hot pads, spatulas
            - Cleaning - sink, dishwasher, trash, cleaning supplies
        - Try to aim for 3-5 steps between zones
    - Consider counter vs. standard depth appliances
    - Think about clearances when planning kitchen size/cabinet layout
        - Oven/fridge/dishwasher doors opening into walkway
            - Dishwasher door is 36” - consider 54” walkway on this side
        - Handles/knobs hitting each other
        - Drawers hitting appliance handles/bump outs
    - Sink shouldn’t face a wall - under a window or in island/peninsula
    - Consider a raised dishwasher - better on back, more efficient without constant bending
    - Appliance placement
        - Consider workflow
            - Take food from pantry/fridge - need a landing zone!
            - Wash food/hands in sink
            - Prep food - empty counter space!
                - Prep zone should be near/between both fridge and range
            - Cook - need landing zones on either side of range and beside oven for hot items!
                - Range hood needs to fully over range and be at least 6” wider
            - Plate or Pack food
            - Clean - scrape food into trash, rinse in sink, load in dishwasher, need landing zone for dirty dishes
                - Trash/waste management should be next to sink
                - Dishwasher should be next to sink
                - Everyday dishes, silverware and glassware should be stored directly beside, above or across from dishwasher for ease of unloading
        - Fridge should be - closer to sink than range, closer to pantry, at the end of a counter run, outside the prep/cooking zones, not next to stove or oven (increased wear on fridge due to extra compressor use)
    - Counter slabs for island - consider maximum slab sizes, if island is larger, will require a seam that’s visible
    - Tall cabinets or appliances should go at end of counter runs - not interrupt them or go on a separate tall unit wall
    - Typical cabinet dimensions - 24” deep, 25.5-26” with overhang, 36” high (with countertop, 34.5 + 1.5), 3.5” toe-kick, width - can get 3&6” (useful?), 9” (spice) - 48” (corner)
        - Come in 3” increments
        - Anything over 24” = 2 doors, 2 knobs/handles, or long handle
        - Can raise toe-kick to raise counter height for comfort - tall people
- Dining Room
- Living Room
- Foyer/Entry
    - Consider glass partitions instead of walls to allow in more natural light
    - Access to powder room should be after closet or storage, ideally off a hallway not opening directly into main entryway
    - Should have a focal point or something to draw your eye through the house directly across from front door
        - i.e. large window to backyard or glass doors to outside
    - Consider milk door (modern version for package receiving)
- Mudroom
- Laundry
- Pets
- Library
- Office
    - Consider door to bathroom?
- Sunroom
    - Motorized screens? very cool but probably expensive
- Master Suite
    - Access to closet should not require going through bathroom
- Flex Room
    - Consider making flex rooms vs. dedicated guest rooms by using murphy beds, furniture that can be easily stored, multi-use furniture (i.e. daybeds)
- Bedrooms
    - Avoid window directly behind bed
    - Pull windows to corners to allow options for which wall bed goes on - measure headboard to ensure enough clearance
    - Recess ceiling lights - should be in 4 corners not central
- Garage
    - Wall mount fans in garage
    - Retractable - hose, outlet, extension cord, air compressor
    - Electric vehicle charger
    - Consider side mount garage door openers for greater height clearance, roof storage
    - Insulated garage doors if want usable space
    - Epoxy floor with extra clear coat - cleanable floor for spills/messes
    - Costco door to pantry!
- Outdoor

Mistakes to Avoid

- too much hallway space/circulation space - wasted sq. ft.
    - Try to redesign room access to minimize
- having the kitchen be a highway through the house - interferes with work zones of cooking
- Not having landing zones!
    - Entry for shoes, coats, bags, mail, groceries - think about everyday life and guests
- Not enough usable wall space
    - Needed for furniture placement, TV placement, art and photographs
    - Leave wall space uninterrupted by windows or doors
- Too open concept with no visual or functional zones
- Bedrooms sharing walls with or too close to noisy living areas
    - Use bathrooms and closets as buffers
    - Think about in wall insulation

Things I Don’t Like on Plans

- Bedroom directly adjacent to foyer
- Laundry far from bedrooms
- Major path of traffic (i.e. to laundry, master suite) only through kitchen zone - past range or dishwasher or anything that might block path
- Closets on exterior walls - waste of natural light - bad for condensation
- Full open concept - linear living - dining - kitchen
- Have to go all the way through master bath to access closet
- Bedrooms directly sharing wall with living room
- Garage at rear - require driving past master bedroom especially, or other bedrooms not ideal
