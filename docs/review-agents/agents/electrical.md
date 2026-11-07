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
