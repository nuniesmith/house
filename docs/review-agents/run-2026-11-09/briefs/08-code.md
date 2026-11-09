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

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/08-code.md`. **Prefix:** `CODE`.

1. **Also read** the findings files 01–07 in `$RUN/findings/`.
2. **Part 9 applicability first.**
   - Find in the library the article that limits Part 9 by building area (the permit README cites Div. A 1.3.3.3) and the definition of "building area".
   - Compute the building area from PF §1 per that definition, showing what's in or out (garage, porches) and the arithmetic.
   - State Part 9 or Part 3, with the margin.
3. **Permit README §7:** verify each row of its code-flag table against the library (confirmed / not reproducible, with your citation).
4. **Stairs:** the CURRENT straight stair and the basement exit stair (PF §10), not the October U-stair.
5. **Pool/spa:** search abc_2023 for requirements on swimming pools/hot tubs in or at dwellings (e.g. guards, enclosure) and cite only what you find.
6. **Spatial separation:** main house ↔ future shop, and ↔ the parents' house if `site.scad` places it (PF §12). Say which distances are measured and which are unknown.
7. **Citation-verification appendix:**
   - For EVERY row of the Citation logs in findings 01–07, re-run it and record one of: CONFIRMED / WRONG PAGE / WRONG ARTICLE / QUOTE NOT ON PAGE / DOESN'T SUPPORT THE FINDING / NOT IN LIBRARY.
   - The coordinator also runs a script check of page, number and quote. Your job is the substance: does the cited text actually say what the finding claims?
