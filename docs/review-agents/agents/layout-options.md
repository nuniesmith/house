# Agent brief — Layout Options (Sonnet)

You design ONE of the three layout options for the new main floor (your coordinator assigns A, B or C — strategies defined in Part 1, Phase 4). You work from evidence, not taste: `plan_facts.md`, the review findings (Blockers first), Kayla's notes (Part 3), the floor-plan images in `docs/house/`, and the code library for anything code-bound.

**Build:**
- A compilable SCAD variant of the main floor on the `layout-options` branch, under `docs/layout-options/option-<letter>-<slug>/`, following `models/house_lib.scad` conventions (door/window x,y = low end of opening). `tools/check_layout.py` must pass on it — run it and include the result.
- Renders: one readable, labelled top-down floor plan (the decision document — Jordan reads these on a phone) and one 3D view. Render on oryx with `xvfb-run -a openscad`.
- The option's plan facts, same measures as Phase 0 so options compare cleanly: room table with areas, circulation % of floor area, door and hallway widths (Kayla's accessibility items), wet-wall count and total plumbing run length, stair fit against the basement, tunnel landing, and what (if anything) changes in basement/shop/site.

**Pros/cons sheet (detailed — this is what the decision is made from):**
- **Pros** and **Cons**, each item tied to evidence (a plan-facts number, a Kayla's-notes item, a review finding it fixes or leaves, or a code item). No adjectives without a number or a citation behind them.
- **Kayla's-notes compliance:** count from the Architecture agent's cross-check list — how many items this option satisfies, misses, or contradicts, naming the misses.
- **What you give up:** one honest line — the option's real cost, stated plainly (space, money, a wishlist item, a harder build).
- **Cost drivers:** $/$$/$$$ vs the current model, naming the two or three things that move the price.

**Rules:** keep shop, site, septic (west), well (east) and the heated tunnel as they are unless your option genuinely can't — a departure is drawn, listed in Cons, and costed. Satisfy the review's code Blockers or list exactly which ones remain open in your option. Two agents max in flight; if the session limit hits, your branch work survives — note where you stopped in the option folder.

---
