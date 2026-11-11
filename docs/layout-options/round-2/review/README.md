# Round-2 review panel

Three read-only reviewers checked the round-2 options against `../briefs/ROUND2-BRIEF.md`, under the rules in `../briefs/REVIEW-R2.md`.

| File | Reviewer | Prefix |
|---|---|---|
| `r2-code-structure.md` | Code and structure (stair, egress, Part 9, ICF walls, spans, garage) | CS |
| `r2-accessibility-kayla.md` | Accessibility, flow, daylight, and an independent re-score of Kayla's 164 PLAN items | ACC |
| `r2-plumbing-mech-cost.md` | Plumbing, septic, mechanical, and relative cost | PMC |
| `kayla-rescore-r2.json` | The re-score, item by item (`IN` / `MISSING` / `CONTRADICTED`) | |

**Status:** D and E are reviewed; F is added when its drawing lands (its columns read "pending" until then).

**How the numbers were checked:**
- The coordinator re-ran every code citation against the code library (`verify_citations.py`): CS 44 of 44, ACC 3 of 3, PMC 20 of 20 confirmed.
- The footprint and matrix numbers were re-run independently (`../coordinator-checks/`).
- Structural and gas items are review items for a licensed Alberta engineer. CEC (wiring) and CSA B149.1 (gas) aren't in the library, so those items say "needs CEC check" / "needs B149.1 check".

**Scripts.** `scripts/` holds the reviewers' measuring scripts, named `<reviewer>_<script>.py`. They were run from the session's scratch folder (written `$RUN` in the findings), so their paths need adjusting before re-running. The findings' "Evidence" column names the script and the SCAD file and line each number comes from.
