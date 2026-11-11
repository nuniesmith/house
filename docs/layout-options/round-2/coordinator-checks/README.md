# Round-2 coordinator checks

Independent re-measurements of each option, the same way for every column.

- `matrix_current.md`, `matrix_d.md`, `matrix_e.md`: `plan_facts.py` in variant mode (`docs/review-agents/run-2026-11-09/scripts/plan_facts.py --main <main> --basement <base> --out <dir>`). The heated footprint row is the round-2 yardstick: outside face, 0.5 ft beyond the wall centre lines, excluding the garage and porches. That's the same offset that reproduces today's 608 m² permit building area.
- `envelope.py` / `envelope.txt`: heated perimeter, corners and bounding box at the outside face (cost drivers: wall length, corners, ICF wall area).

**One known tool artefact.** The matrix row "Main stair top/foot vs the basement stair" assumes today's north-to-south 21-tread flight. It reads "moved" for the round-2 options, whose 18-tread flights run north (D) or west (E). The stair is checked properly in `../review/r2-code-structure.md`.

`matrix_f.md` is F as committed (Kayla's Nov 11 list, drawn compact); `matrix_f_nov10.md` is the dated Nov 10 version.
