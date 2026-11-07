# House Review Run — Sunday Kickoff Document

_One document, everything the run needs. Prepared 2026-11-07; run after the Claude usage reset, Sunday 2026-11-08, 5:00 p.m. ET._

## How to start (Jordan)

1. Open a Claude Code session on **oryx**, in `~/github/house`.
2. Paste the kickoff prompt below.
3. The session runs the specialists on Sonnet in waves of 2, with Opus coordinating — per Part 1.

**Kickoff prompt (copy-paste):**

> Read this document end to end and run it. You are the coordinator (Opus). Work in ~/github/house. Follow Part 1 exactly: Phase 0 plan-facts extraction first (one Sonnet sub-agent), then the specialist waves, at most 2 sub-agents at a time, each briefed with its Part 2 section plus plan_facts.md. Enforce the citation rule against ~/code-library/search.py. Review only — no SCAD edits. Deliver the merged review as a document on a branch with a PR, and report the PR status explicitly (ready / not ready, and why).

---
# Part 1 — Runbook

# House Review Run — Sunday Runbook

**When:** after the Claude usage reset, **Sunday 2026-11-08, 5:00 p.m. ET**.
**Where:** Claude Code session on oryx, in `~/github/house`.
**What:** a multi-agent plan review of the house (main house + shop + site; parents' house as a second pass if time allows). Review only — no model edits in this run. Fixes are a later run, on Jordan's word.

## Model assignments (Jordan's call, 2026-11-06)

- **Specialist sub-agents run on Sonnet** — they do the reading, measuring and checking.
- **The coordinator runs on Opus** — it oversees: merges the specialists' findings, enforces the citation rule, builds the conflict table and the decision list. This is the usual pattern for this household: Sonnet builds, Opus reviews.
- **At most 2 sub-agents at a time** (standing rule — the shared session limit kills background agents mid-task; worktrees survive, resume after reset if it happens anyway).

## Inputs (all on oryx)

- Models: `~/github/house/models/*.scad` (main_floor, basement, house_combined, shop, site) + drawn plans/renders in the repo docs.
- Prior review: `docs/House-Review-and-Research-2026-10-28.md` (the 23-item decision list — specialists check what's still open, don't redo what's decided).
- **Code library:** `~/code-library/` — full text of ABC 2023 (Alberta Ed.), NPC 2020, NECB 2020, Alberta Electrical Utility Code 2022, Alberta Private Sewage SOP 2021, indexed in `codes.db`.
  Query: `python3 ~/code-library/search.py [--doc <stem-prefix>] "<fts query>"` — full-text syntax, phrases in quotes. `--page <doc-prefix> <n>` dumps a whole PDF page.
  Doc prefixes: `abc_2023`, `electric_2022`, `National_Energy`, `plumbing`, `sewage`.
- Assumption set (do not re-litigate): build is in **Alberta** (land not yet secured — snow load and other site values stay flagged as assumptions); roof colour blue, product parked; Kayla's edits are design input; shop (100×100, utilities bay) powers the house via the heated tunnel; well east, septic west by the utility room; parents' house (no basement, crawl space) ties into services later.
- Known open question the run must NOT resolve: the main-floor baseline — Kayla's edited layer vs the as-drawn sheet — is Jordan's pending A/B call. Review the model **as it stands on main** and list the divergence as an assumption in the report.

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

## Standard finding format (every specialist, no exceptions)

| # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
|---|---|---|---|---|---|---|

- Severity: **Blocker** (can't build / won't pass), **Should fix** (real cost or function loss), **Consider** (judgement call for Jordan/Kayla).
- Evidence: a plan_facts number, a SCAD line, or a render — never "typically" or "usually".
- Code / standard: article number **as returned by the code library search**, with doc + PDF page. A citation the coordinator can't reproduce gets bounced, not published.
- Cost impact: rough order only ($ / $$ / $$$) unless real price data is in the repo. Say "unknown" rather than inventing a number.

## Hard rules

1. **Review only.** No SCAD edits, no commits by specialists. The coordinator's only write is the review document on its branch.
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
7. **Delivery.** Write the review as one document on a branch in the house repo, open a PR, and report its status explicitly (✅ ready to merge only if it's a clean docs PR). No model files change in this run.

**Tone of the report:** Jordan reads verdict-first, on a phone, between other things. Short sentences, tables for comparisons, plain language for trade terms on first use.
