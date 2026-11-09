# Agent brief — Electrical (Sonnet)

You review the electrical scheme: service, distribution, and the shop-powers-house architecture.

**Inputs:** `plan_facts.md`, models (shop, site, tunnel), code library: Alberta Electrical Utility Code 2022 (`--doc electric`) for service/utility requirements.

**Hard limit:** the library does NOT contain the Canadian Electrical Code (house wiring). Cite the AEUC where it applies (service entrance, metering, utility side) and mark every wiring-level item "needs CEC check" — never cite a CEC article from memory.

**Check:**
- Service architecture: shop is the service point; house keeps a 200A panel fed from the shop. Feeder run length through the tunnel from plan_facts — voltage-drop finding at 200A over that distance, and the conductor implication (state the math).
- Load inventory: build the demand list from the plans — house (incl. pool equipment, DHW/heating plant auxiliaries), shop (welder, compressor, lift, wash bay), heated driveway/walkways, tunnel heating, EV/truck charging, parents' house later. Total it against the service size the AEUC process would approve; flag if the architecture needs 400A.
- Generator: size and transfer — what stays live (heating plant, well pump, septic pumps) vs what sheds.
- Separation/coordination: feeder in the heated tunnel with plumbing and gas — clearances and what shares the tunnel.
- Parents' house: fed from where, what size, and does its later tie-in force a service upgrade now?
- Future-proofing findings: conduit/rough-in that is cheap now and expensive later (porch hook lighting, shop expansion, solar-ready).

**Output:** standard format; load table included. Every number shown with its arithmetic. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/05-electrical.md`. **Prefix:** `ELE`.

1. **Service architecture on main:** power comes from the road along the west side into the house by the basement UTILITY room (`site.scad` header, PF §11/§12). The house is the service point, and the shop gets buried lines from the house later. Review THAT:
   - The service size needed for the house, the pool/spa, EV/truck charging, the future shop fed from the house, and the parents' house later. Does the house-first service need to be sized now (e.g. 400A) for what comes later?
   - AEUC items for a rural Alberta service entrance and metering, cited from `--doc electric_2022`.
2. **Voltage drop:**
   - The brief's 200A feeder through the tunnel goes in the "If the tunnel architecture is reinstated" section.
   - Do the same math for the current plan's reverse direction: a feeder from the house to the future shop, over the buried-line length (PF §12).
   - Show all arithmetic. The library has no conductor tables (that's CEC), so any resistance values are labelled assumptions, plus "needs CEC check".
3. **Load table** with arithmetic, and the generator section, as the brief asks.
