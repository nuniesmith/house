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
- **Kayla's notes (design intent — READ THESE):** Kayla's Notion "Home Build" notes, handed over by Jordan 2026-11-08. Full text in `HOUSE-REVIEW-RUN.md` Part 3 and in `KAYLAS-NOTES.md`. Requirements, not background: every specialist checks the plan against the sections touching their brief; mismatches are findings. Architecture / Flow owns the full cross-check, and the coordinator's report includes a Kayla's-notes compliance summary.
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
