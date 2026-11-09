# House review run — 2026-11-09 (working record)

The evidence behind the review in `docs/house/House-Plan-Review-2026-11-09.md`.
Run per `docs/review-agents/HOUSE-REVIEW-RUN.md`, against `main` @ `d20a2fa`.
Specialists ran on Sonnet, with Opus coordinating.

| File | What |
|---|---|
| `plan_facts.md` | Phase 0: the measured facts every specialist worked from. Rooms, doors, windows, circulation, paths, adjacency, plumbing, stairs, services, site distances, stale-premise check, Oct 28 decision status. Each number is sourced to `file:line` or computed by `scripts/plan_facts.py`. |
| `renders/current_*_plan.png` | Labelled plans of the model as it stands on `main` (wall centre lines, sq ft, 10 ft grid, north up). |
| `kayla_checklist.md` | Kayla's notes, numbered K-001…K-335. These are the fixed IDs used by the cross-check and by every layout option. |
| `briefs/` | The exact briefs each specialist got: `COMMON-RULES.md` + the Part 2 brief + run-specific adjustments. |
| `findings/` | Each specialist's raw findings file (added wave by wave). |
| `citation-check.md` | The coordinator's re-run of every code citation against the code library. |
| `scripts/` | `plan_facts.py` (the computed tables), `plot_plan.py` (the plan renderer, works on any level file with `-D audit=true`), `kayla_checklist.py`, `verify_citations.py`. |

**Environment note.** This run executed in a Claude Code cloud session, not on oryx.
- OpenSCAD 2021.01 came from Ubuntu apt.
- The code library was rebuilt from the five PDFs in `docs/codes/` with the same CLI (`search.py --doc / --page`).
- "PDF page" means the page index in the PDF file. Every citation can be re-checked on oryx by opening that page.
- Script paths point at `/home/user/house`; on oryx, change `REPO` in `plan_facts.py` to `~/github/house`.
