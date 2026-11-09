# Layout options for the new main floor

**Start here: [`DECISION-PACK.md`](DECISION-PACK.md).** It has the three plans side by side, the fixed matrix, the ranked recommendation, cheap hybrids, and the choice for Jordan and Kayla.

| Folder / file | What |
|---|---|
| `option-a-evolve-current/` | Option A: the current model with the smallest moves that fix the Blockers and the cheap deal-breakers |
| `option-b-as-drawn-plus-kayla/` | Option B: the architect's as-drawn sheet (`docs/house/floor_plan.JPEG`), with Kayla's notes applied |
| `option-c-clean-sheet/` | Option C: re-planned from Kayla's notes, in a simpler block |
| `kayla-rescore.md` | An independent re-score of all three options on the same 164 Kayla plan items, by one judge |
| `coordinator-checks/` | The coordinator's own re-run of every option's numbers (the same script as for the current model) |
| `briefs/` | The exact briefs the option designers worked from, including the review summary they used |

Each option folder holds:
- a SCAD model of the main floor (plus the basement where the stair changes), which passes `tools/check_layout.py`;
- a labelled plan and a 3D view;
- plan facts;
- `PROS-CONS.md`.

The models in `models/` are unchanged. The chosen option is built into the model in a later run.
