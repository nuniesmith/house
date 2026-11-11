# Round-2 review panel

Three read-only reviewers checked the round-2 options against `../briefs/ROUND2-BRIEF.md`, under the rules in `../briefs/REVIEW-R2.md`.

| File | Reviewer | Prefix |
|---|---|---|
| `r2-code-structure.md` | Code and structure (stair, egress, Part 9, ICF walls, spans, garage) | CS |
| `r2-accessibility-kayla.md` | Accessibility, flow, daylight, and an independent re-score of Kayla's 164 PLAN items | ACC |
| `r2-plumbing-mech-cost.md` | Plumbing, septic, mechanical, and relative cost | PMC |
| `kayla-rescore-r2.md` | The re-score as a readable page: summary, deal-breakers, disagreements with the designers, all 164 items (Today, D, E, F) | |
| `kayla-rescore-r2.json` | The same verdicts as data | |

**Status:** all three options (D, E, F) are reviewed. F is Kayla's Nov 11 list, drawn with no footprint cap on purpose, so its size is context rather than a finding.

**How the numbers were checked:**
- The coordinator re-ran every code citation against the code library (`verify_citations.py`): CS 45 of 45, ACC 3 of 3, PMC 22 of 22 confirmed.
- The footprint and matrix numbers were re-run independently (`../coordinator-checks/`).
- Structural and gas items are review items for a licensed Alberta engineer. CEC (wiring) and CSA B149.1 (gas) aren't in the library, so those items say "needs CEC check" / "needs B149.1 check".

**Scripts.** `scripts/` holds the reviewers' measuring scripts, named `<reviewer>_<script>.py`. They were run from the session's scratch folder (written `$RUN` in the findings), so their paths need adjusting before re-running. The findings' "Evidence" column names the script and the SCAD file and line each number comes from.
