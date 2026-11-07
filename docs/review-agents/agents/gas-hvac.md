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
