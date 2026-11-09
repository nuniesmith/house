# Common rules — every review specialist (binding)

You are one of eight review specialists (Sonnet) in a multi-agent review of Jordan and Kayla's house design (rural Alberta; land not yet chosen). The coordinator (Opus) merges the eight reports into one review document, and re-runs every code citation you give. You produce findings. You change nothing.

## Paths

- **Repo, READ-ONLY:** `/home/user/house` (branch `main` @ `d20a2fa`).
  - Do not edit, create, delete or commit anything in the repo. Do not switch branches.
  - Do not run `tools/make_drawings.py` (it writes into `docs/permit/`).
  - Read-only tools are fine: `python3 tools/check_layout.py`, `python3 tools/model_data.py > <your work folder>/model.json`, and openscad renders written to your own work folder (`xvfb-run -a openscad -o <png> ...`).
- **Run folder:** `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`
  - Your ONLY deliverable: `$RUN/findings/<your file>.md` (named in your prompt).
  - Scratch scripts and renders go under `$RUN/work/<your-prefix>/`.
- **Plan facts:** `$RUN/plan_facts.md`. Measured numbers, each sourced to file:line. Work from these and cite them as `PF §N`. If you find a plan_facts number that's wrong, don't silently substitute your own: list it under "plan_facts corrections" with file:line evidence.
- **Renders:**
  - `$RUN/renders/current_main_floor_plan.png` and `current_basement_plan.png` (labelled, 10 ft grid, north up).
  - Repo renders in `docs/house/` (sections a–e, elevations, cutaway, site_plan_house) and `docs/shop/`.
  - The permit set: `docs/permit/House-Drawing-Set.pdf`, `docs/permit/README.md` (its §1 and §7 already list code flags; verify them, don't just copy them), and `docs/permit/schedules/*.csv`.
- **Kayla's notes** are requirements, not background: `docs/review-agents/KAYLAS-NOTES.md`, numbered in `$RUN/kayla_checklist.md` (K-001…K-335). Cite items by K-number. A mismatch between her notes and the model is a finding. Evidence = the K-number + the model evidence.
- **Prior work:** `docs/house/House-Review-and-Research-2026-10-28.md` (the Oct 28 review and its 23-item decision list; `PF §14` has the statuses, so don't redo what's decided), `docs/house/Redesign-and-Spec-2026-11-02.md` (the current design; read its dated updates at the top), `docs/shop/Shop-Base-Plan.md`.

## Code citations — the rule the coordinator enforces

- The **only** citation source is the code library:
  - `python3 ~/code-library/search.py [--doc PREFIX] "<fts query>"`
  - `python3 ~/code-library/search.py --page PREFIX N` dumps one whole PDF page.
  - Prefixes: `abc_2023` (Alberta Building Code 2023), `plumbing` (National Plumbing Code 2020), `National_Energy` (NECB 2020), `electric_2022` (Alberta Electrical Utility Code 2022), `sewage` (Alberta Private Sewage Systems Standard of Practice 2021).
  - Article numbers search best as a quoted phrase: `search.py --doc abc_2023 '"9.8.4.1"'`.
- For every citation:
  1. Find it with a search.
  2. Open the page with `--page`.
  3. Write the article / sentence / table number exactly as printed on that page, with the doc and the PDF page. Example: `ABC 2023 9.10.15.4.(2) — abc_2023 p.NNN`.
  4. Put the requirement's key words (25 words or fewer, verbatim) in your Citation log.
- **Never cite from memory**: no article numbers, no values, no table entries. If the library doesn't have it, write "not found in library" and leave the citation out.
- **Not in the library:** the Canadian Electrical Code Part I (house wiring) and CSA B149.1 (gas). Mark those items "needs CEC check" / "needs B149.1 check". Never cite them.
- A citation the coordinator can't reproduce from your Citation log is bounced, and the finding is cut.

## Assumptions — state them, don't resolve them

1. **Main-floor baseline.** Kayla's edited layer vs the as-drawn sheet is Jordan's pending A/B call. Review the model as it stands on `main` (traced from `docs/house/main_floor.jpg`). Don't let any finding presume either answer.
2. **Tunnel / shop-powers-house.** The run document assumes the shop (100×100 ft, Bay 1 utilities) powers and heats the house through a ~70 ft heated tunnel. The models on `main` dropped the tunnel on Nov 3:
   - Sources: `models/site.scad:33`, the Redesign-and-Spec Nov 3 update, `README.md`, the Shop-Base-Plan Nov 3 note.
   - What `main` models now: house first; power, gas and fibre come from the road along the west side, into the house by the basement UTILITY room; the shop is a later, separate project.
   - Review what `main` models. Where your brief asks about the tunnel or the shop plant, answer in a separate short section, "If the tunnel architecture is reinstated", with numbers. Don't mix it into the main findings.
   - `PF §13` lists which other brief premises are stale (e.g. the basement "U-stair in the former bar area" belongs to the October model; the current stair is straight, per Redesign §2).
3. **Land isn't chosen.** Snow load, soils, water table, road side and utility availability are assumptions. Flag any land-dependent conclusion as such.
4. **No stamped-engineer claims.** Structural and gas items are review items for a licensed Alberta engineer. Say so.
5. **Parents' house** (`docs/small_house/IMG_0415–0420.PNG`) is a second pass. Cover it in a short final section only if your brief lists it, and only from what the photos and repo docs show.

## Output: your findings file

1. Header: specialist, date, inputs you read.
2. Findings table with exactly these columns:

   | # | Severity | Location | Finding | Evidence | Code / standard | Cost impact |
   |---|---|---|---|---|---|---|

   - **#**: your prefix + number (e.g. `ARC-01`).
   - **Severity**: **Blocker** (can't build / won't pass), **Should fix** (real cost or function loss), **Consider** (a judgement call for Jordan/Kayla).
   - **Evidence**: `PF §N` + the number, a `file:line`, a render name, or a K-number + model evidence. Never "typically", "usually", or an adjective without a number.
   - **Code / standard**: a citation as above, "needs CEC check" / "needs B149.1 check", or "—".
   - **Cost impact**: `$` / `$$` / `$$$` or "unknown". No invented dollar figures. Ranges only from the repo's research docs, cited.
   - Sort by severity (Blockers first).
3. Any extra tables your brief asks for.
4. "If the tunnel architecture is reinstated" (only if your brief touches it).
5. "plan_facts corrections" (if any).
6. **Citation log**: a table with exactly these columns, one row per citation. The coordinator checks it by script, so keep the format exact:

   | Finding | Command | Doc | PDF page | Article as printed | Quote |
   |---|---|---|---|---|---|
   | ARC-03 | `search.py --doc abc_2023 '"9.5.3.1"'` | abc_2023 | 812 | 9.5.3.1.(1) | <verbatim words copied from that page, 25 or fewer> |

   - **Doc** is one of the five prefixes.
   - **PDF page** is a bare number.
   - **Article as printed** is the number exactly as it appears on that page (e.g. `9.10.15.4.`, `Table 9.23.4.2.-A`, `Sentence 2.2.1.1.(2)`; SOP and AEUC numbering as printed there).
   - **Quote** must be copied from the `--page` output of that exact page. Line breaks become single spaces. Don't paraphrase.

**Final message to the coordinator (300 words or fewer):** counts by severity, your top 3 findings in one line each, and the path of your file. Nothing else.
