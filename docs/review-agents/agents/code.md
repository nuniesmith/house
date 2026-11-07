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
