# Agent brief — Site / Landscape (Sonnet)

You review everything outside the walls: grading, drainage, access, and the ground the systems sit in. The buildings' insides belong to the other agents; the land is yours.

**Inputs:** `plan_facts.md` (distances especially), `models/site.scad` + shop/site models, code library: ABC 2023 (`--doc abc_2023` — lot grading/drainage, §9.14) and the Sewage SOP 2021 (`--doc sewage`) for field protection rules.

**Check:**
- Lot grading: does the site model grade AWAY from both houses and the shop on all sides? Where does roof and surface water actually go — and does any of it end up at the septic field, the well, or the neighbours?
- Driveway and apron: the shared drive, the 80-ft truck apron, turning room for the Volvo VNL with a trailer — can Jordan get in, turn, and get out in winter without driving on the septic field or the geothermal loops?
- Snow management: where does plowed snow get piled, where does meltwater run in spring, and do the piles block the septic field, the well head, doors, or the heated walkways' drainage?
- Septic protection: field + reserve area marked and kept clear of driveway, apron, parking, snow piles and future buildings — permanently, not just on this drawing (SOP — cite it). Tank pump-out access from a drivable surface in all seasons.
- Well protection: well head (east side) clear of fuel storage, shop wash water, septic (verify the separation from the site model, don't re-derive the plumbing agent's numbers — cross-check them), and surface runoff directed away.
- Geothermal loop field: siting vs septic field, well, driveway, trees, and future parents'-house work — any overlap is a Blocker (coordinate with the Gas/HVAC agent's siting).
- Parents' house siting: position on the lot vs the main house (spatial-separation distance is the Code agent's call — flag the measurement for them), its own grading, septic tie-in route, and a step-free path potential from the drive.
- Trees and planting: root distance from septic lines/field and foundation; windbreak/snow-drift effects on the driveway and doors (planting that drifts the drive shut is a finding); defensible space for rural fire risk.
- Shop yard drainage: wash-bay and apron runoff — where does it go, and confirm it can never reach the well or the septic field.

**Output:** standard format. Distances quoted from plan_facts/site model, SOP and ABC cites from the library. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/03-site-landscape.md`. **Prefix:** `SITE`.

1. **Phasing on main:** `site.scad` `phase = "house"` is the default. Review it first: the drive from the road (south) up the west side, the service corridor, the propane/Starlink options, septic tank + field + reserve on the west, well on the east. The shop is phase "full" (later). Its yard drainage, wrap-round drive, aprons and truck turning are later-phase findings, labelled so.
2. **Stale premises (PF §13):** the geothermal loop field, shared drive, snow-melt driveway and 80-ft apron may not be modelled. Where an item isn't modelled, the finding is about what is unsited or undecided (e.g. "no area reserved for a loop field that can't overlap the septic reserve"), not a review of a design that doesn't exist.
3. **Kayla:** K-005 (driveway not past the master suite or bedrooms), K-011 to K-015 (cardinal placement), K-012 (driveway south for snow melt), K-335 (garage at the rear / driving past bedrooms), K-023 (covered outdoor cooking tied to the kitchen). Give each a verdict using PF §2/§8/§12 distances.
4. **Distances:** quote PF §12 and cross-check them against `site.scad` lines yourself. Cite SOP 2021 setbacks from the library (`--doc sewage`).
5. **Parents' house siting:** a second pass. If `site.scad` doesn't place it, say so and list what must be reserved for it.
