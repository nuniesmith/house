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
