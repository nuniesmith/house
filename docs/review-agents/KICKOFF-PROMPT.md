# Kickoff Prompt — House Review + Layout Options Run

_For Jordan: open a Claude Code session (Opus) on oryx in `~/github/house`, paste everything in the block below as your first message, and let it run. It checks in after Phase 0, after the review draft, and when both PRs are up._

---

```text
You are the coordinator (Opus) for a multi-agent house plan review and layout-options run. Work in ~/github/house on this machine (oryx). I (Jordan) will be away from the desk for much of this run — work autonomously inside the scope below and check in at the milestones listed at the end, verdict first.

BEFORE SPAWNING ANYONE:
1. `git checkout main && git pull --ff-only`. Confirm HEAD includes docs/review-agents/HOUSE-REVIEW-RUN.md with the layout-options phase (Phase 4). Report the HEAD hash.
2. Read docs/review-agents/HOUSE-REVIEW-RUN.md end to end. That document governs this run: the runbook and repo map (Part 1), the agent briefs (Part 2), and Kayla's notes (Part 3). If anything in this prompt and that document disagree, the document wins.
3. Sanity-check your tools and report all three results in your first reply:
   - Code library: `python3 ~/code-library/search.py --doc abc_2023 "spatial separation"` returns hits.
   - `openscad --version` works (PNG renders will need `xvfb-run -a openscad`).
   - `python3 tools/check_layout.py --help` or an equivalent dry check shows the layout checker is runnable.
Then give me your wave plan in a few lines and start Phase 0 without waiting for my reply.

THE RUN (per the document):
- Phase 0: one Sonnet sub-agent extracts plan_facts.md from the SCAD models — specialists work from those numbers, not from vibes.
- Phases 1–3 (review): specialist waves on Sonnet, at most 2 sub-agents at a time, each briefed with its Part 2 section plus plan_facts.md. Enforce the citation rule: a code citation that doesn't reproduce via ~/code-library/search.py gets bounced, not published. Kayla's notes are requirements — mismatches are findings, and Architecture/Flow owns the full cross-check of Part 3. Review specialists edit nothing.
- Phase 4 (layout options): three options for the new floor plan, one Sonnet agent each, waves of 2, on the layout-options branch ONLY (models on main stay untouched): A = evolve the current model, B = the as-drawn sheet (docs/house/floor_plan.JPEG, geometry only — its printed dimensions are unreliable) with Kayla's notes applied, C = clean sheet inside the same envelope planned from Kayla's notes outward. Each option ships: a compilable SCAD variant passing tools/check_layout.py, a readable labelled top-down floor-plan render plus one 3D render, its own plan facts (same measures as Phase 0), and a detailed pros/cons sheet scored against Kayla's notes — including its Kayla-compliance count, cost drivers, and one honest "what you give up" line.
- Phase 5 (decision pack): you score A/B/C on the document's fixed matrix, give a ranked recommendation with the reasoning shown (and note cheap hybrids, e.g. one option's kitchen inside another), and end with the choice framed for me and Kayla. The final layout choice is ours — do not select a final plan and do not merge any option into main's models.

HOUSE RULES:
- Findings and pros/cons need evidence: a plan_facts number, a file/line, a render, or a reproducible code citation (doc + PDF page). No adjectives without numbers behind them.
- No stamped-engineer claims: structural and gas items are review items for a licensed Alberta engineer, flagged as such. CEC and CSA B149.1 are not in the library — mark those items "needs CEC/B149 check", never cite them from memory.
- PR status is explicit in every report: ✅ ready to merge only if the PR is clean on its own head; otherwise ⛔ not ready, and why.
- If the session limit hits mid-run, stop cleanly: push what's done, and note in the PR where the run stopped and which wave resumes first.

CHECK IN WITH ME (verdict first, short):
1. After Phase 0 — the headline plan facts and anything already obviously wrong.
2. After the review waves — the draft's top Blockers and the Kayla's-notes compliance picture.
3. When both PRs are up — review PR and layout decision pack PR, with links and status.

Start now.
```
