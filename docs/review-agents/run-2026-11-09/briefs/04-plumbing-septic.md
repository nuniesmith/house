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

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/04-plumbing-septic.md`. **Prefix:** `PLB`.

1. **Kayla (present/absent, with evidence):** K-006 (grouped wet walls), K-036 + K-158 + K-203 + K-228 (laundry next to and connected to the master suite), K-037 + K-115 + K-315 (pantry Costco door to the garage), K-170 (dog bath near the rear entrance), K-169 (pet-bowl water filler), K-018 (laundry exhaust fan, as a plan item: is there a window or an exterior wall?).
2. **Tunnel premise is stale (PF §13).** "Field kept out of the tunnel alignment" goes only in the "If reinstated" section. On main, check the field and reserve against the buried service corridor and the future shop service lines on the west side (`site.scad`).
3. **Shop bathroom and wash bay:** a later phase (`shop.scad`). Still check gravity vs lift, and the wash-bay path to septic, labelled "later phase". An ambiguous wash-bay path to septic is still a Blocker for that phase.
4. **Hot water:** with no tunnel, find the plant/DHW in the house model (PF §11) and measure to the furthest fixture (PF §9).
5. **Basement pool + spa + pool bath:** where do the pool/spa drains and filter backwash go? Search the SOP for what may and may not discharge to the septic system and cite what you find.
6. **Septic sizing:** the main house (bedroom count from PF §3, all fixtures from PF §9), the parents' house later, the shop bathroom later. Cite the SOP sizing basis.
