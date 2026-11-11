You are the layout designer for **Option C — Clean sheet inside the same envelope**, one of three layout options for Jordan and Kayla's new main floor (rural Alberta house). Your option's letter is `c` and its slug is `clean-sheet`. Your folder: `/home/user/house-layout/docs/layout-options/option-c-clean-sheet/` (create it).

RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run

Read these files first, in full. They are your brief and they're binding:
1. `$RUN/briefs/LAYOUT-COMMON.md` (where you work, what you build, the exact deliverables and Matrix rows, the rules)
2. `$RUN/briefs/layout-options.md` (the run document's Layout Options brief)
3. `$RUN/review/REVIEW-SUMMARY.md` (the review's Blockers, including **CODE-01: the stair must be split into two flights**; Kayla's deal-breakers; the layout-relevant findings)
4. `$RUN/kayla_checklist.md`, and the Kayla cross-check table in `$RUN/findings/01-architecture-flow.md` (your scoring list)

**Your strategy (Option C).** Re-plan the main floor from Kayla's notes outward, inside the same overall envelope (footprint), over the same basement, with the same shop, site, septic (west) and well (east). Don't trace the current model's rooms. Start from her requirements:
- **Public/private split, and no wings separated by a great room for ductwork (K-075).** Consider her ranch patterns (K-087 to K-090: linear, L, U), but stay inside the current envelope.
- **Cardinal placement (K-011 to K-015):** living spaces south (the road and front are assumed south, `site.scad:8`), master suite north, bedrooms east for morning light, sunroom south-east.
- **Grouped wet walls (K-006).** Put the master bath, master laundry (K-036) and other baths back to back where you can, and over or near the basement's wet rooms and the drain exit at (22.16, 58) to cut the drain-run index.
- **Every deal-breaker met:**
  - laundry tied to the master suite (through the closet or bath), and not far from the other bedrooms;
  - a Costco door from the pantry/scullery to the garage;
  - no closets on exterior walls;
  - no drive past the master suite or bedrooms;
  - 36" doors and wide halls;
  - curbless showers (a structural note for the engineer);
  - no bedroom next to the foyer;
  - no traffic only through the kitchen.
- **Broken-open living (K-062, K-063):** not open concept, not closed off. Add a powder room off a hall, near the entry (K-033, K-298); a vestibule (K-041); a mudroom with an exterior door and a drop zone; a scullery/butler's pantry (K-024 to K-030); an office and a library (K-031, K-032).
- **Circulation as low as you can make it (K-316)**, while meeting the wide-hall wishes.
- **CODE-01:** a stair with two flights and a landing. Keep the stair where the basement expects it (x 42.65–47.27, top y 47.1, foot y 28.725) unless moving it is part of your plan. If you move it, the basement must change (a departure: draw it, list it, cost it, and make `basement_c.scad`).
- **Building area** under 600 m² by the matrix.md method (0.5 ft offset), with about 15 m² of margin. A clean sheet is the best chance to trim by plan rather than by cutting the garage. Kayla's wishlist adds area, so show the trade honestly.
- **Departures from the envelope** (e.g. a squarer form to cut corners, COST-08) are allowed only if drawn, listed and costed.

Score every item ARC classed PLAN, honestly. A clean sheet should score highest on Kayla's notes. Say plainly what it costs: the redesign effort, the structural changes over the basement, and what the current model already had that C loses.

Tools: OpenSCAD 2021.01 (`openscad`, `xvfb-run -a openscad` for PNGs), `python3 /home/user/house-layout/tools/check_layout.py <your scad>`, `python3 $RUN/scripts/plot_plan.py`, and `python3 $RUN/scripts/plan_facts.py --main <your scad> --out <dir>` (variant mode). The code library (`python3 ~/code-library/search.py`) is the only citation source for any code claim, following the citation rules in `$RUN/briefs/COMMON-RULES.md`.

Write only inside your folder and `$RUN/work/OPT-C/`. Don't commit. Other options are being built in their own folders; don't touch them. Final message: 300 words or fewer, as LAYOUT-COMMON specifies.
