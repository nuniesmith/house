# Round-3 review panel

Three read-only reviewers checked Option H against `../briefs/ROUND3-BRIEF.md`, under the rules in `../briefs/REVIEW-R3.md`. Round 2's D and F, and today's plan, are the comparison columns. Their numbers are reused from `../../round-2/review/`, not re-reviewed.

| File | Reviewer | Prefix |
|---|---|---|
| `r3-code-structure.md` | Code and structure (stair, egress, Part 9, ICF walls, spans, roof, garage) | CS |
| `r3-accessibility-kayla.md` | Daily routes, accessibility, flow, and an independent re-score of Kayla's 164 PLAN items | ACC |
| `r3-plumbing-mech-cost.md` | Plumbing, septic, mechanical, relative cost, and the future elevator's build-time items | PMC |
| `kayla-rescore-r3.md` | The re-score as a readable page: Today, D, F, H | |
| `kayla-rescore-r3.json` | H's verdicts as data | |

**How the numbers were checked:**
- **Citations:** the coordinator re-ran every code citation against the code library (`verify_citations.py`). CS 40 of 40, ACC 3 of 3, PMC 20 of 21. The 21st PMC row quotes page 37 of the sewage standard word for word. That page continues the fixture-unit list of Table 2.2.2.2.A without printing the table number, so the checker can't match the article.
- **Measurements:** footprints, matrix rows and routes were re-run independently (`../coordinator-checks/`).
- **Engineer items:** structural and gas items are review items for a licensed Alberta engineer. CEC and B149.1 items say "needs … check".

**Scripts.** `scripts/` holds the reviewers' measuring scripts, named `<reviewer>_<script>.py`. They were run from the session's scratch folder (written `$RUN` in the findings), so their paths need adjusting before re-running.
