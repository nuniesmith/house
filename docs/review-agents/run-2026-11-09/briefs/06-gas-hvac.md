# Agent brief — Gas / HVAC (Sonnet)

You review the heating plant and everything it feeds: house heat, pool, domestic hot water, snow melt, the heated tunnel, the shop, and geothermal.

**Inputs:** `plan_facts.md`, models, code library: ABC 2023 (`--doc abc_2023` — ventilation §9.32, energy §9.36) and NECB 2020 (`--doc National_Energy`) for the shop.

**Hard limit:** the gas code (CSA B149.1) is NOT in the library. Review gas routing and appliance siting as layout findings; mark code-specific gas items "needs B149.1 check" — never cite it from memory.

**Check:**
- One plant or several: the plan puts the heating plant in the shop utilities bay (boiler for pool + DHW + snow melt + house heat, geothermal backup). Heat load rough math per building from plan_facts areas; is one plant credible, and what fails when it's down? (Single point of failure finding — house heat depends on the tunnel run.)
- The tunnel as a utility run: heating mains house↔shop, freeze risk if the plant stops mid-winter, insulation/heat-trace findings.
- Distribution in the house: radiant vs forced air vs hybrid — what do the plans imply, and what does the basement pool do to humidity/ventilation (§9.32 cite)?
- Geothermal: loop field siting on the site model — conflicts with septic field (west), well (east), shop apron, driveway. Flag any overlap as a Blocker.
- Snow melt: heated driveway + walkways — zones, load on the plant, and the run from the shop plant to the house driveway.
- Shop heating: 100×100 with a wash bay — NECB applies; unit heaters vs radiant tube; wash-bay humidity.
- Gas service: meter/regulator location relative to the shop utilities bay; the parents'-house supply later (gas or electric — state the trade-off as a finding for Jordan).
- Radon: Alberta is high-radon; ABC rough-in requirements (coordinator will want the Code agent to confirm the article — cross-reference, don't duplicate).

**Output:** standard format; plant load table with arithmetic shown. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/06-gas-hvac.md`. **Prefix:** `GAS`.

1. **Plant location on main:** there is no tunnel, so find where the boiler, heating plant and DHW sit in the current house model (PF §11), and review that. The shop-Bay-1 single plant, and its single-point-of-failure analysis, go in the "If the tunnel architecture is reinstated" section.
2. **Gas service:** natural gas from the road if available, otherwise the propane-tank option drawn in `site.scad`. Review the tank's siting against house openings, the septic and the well as a layout finding, with "needs B149.1 check" for clearances.
3. **Basement pool + spa:** humidity, ventilation and dehumidification, cited from ABC 9.32 via the library.
4. **Geothermal and snow melt:** PF §13 says whether either is modelled. If not, the findings are about what must be sited or decided. If the Oct 28 research proposes a loop field, test where one could fit on the `site.scad` layout against the septic field, reserve, well and service corridor, with distances.
5. **Energy:** the ABC 9.36 path (prescriptive or performance) the plans imply. Radon: cross-reference only; the Code agent confirms the article.
