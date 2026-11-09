# Agent brief — Architecture / Flow (Sonnet)

You review how the house lives: movement, space use, furniture fit. You do not review structure, services, or code beyond clearances you can cite.

**Inputs:** `plan_facts.md`, main-floor + basement renders/drawn plans, parents'-house plan, the Oct 28 review's open items.

**Check:**
- Circulation: trace every daily path (entry→kitchen, bedrooms→bath, garage→kitchen with groceries, basement↔main). Total the hall/circulation area from plan_facts and state it as a % of floor area — flag waste.
- The known sore spot: the 2–3 bedroom + hallway arrangement on the main floor. Propose at most 2 concrete alternatives with the area math for each.
- Door swings: conflicts, doors hitting fixtures/furniture, travel through one room to reach another.
- Furniture fit: primary bed (king), bedroom closets usable depth, kitchen work triangle and island clearances, dining seats.
- Kitchen: Kayla's two-path requirement; laundry open from both sides; bedroom→closet direct access — verify each is actually in the model as it stands, report present/absent with evidence.
- Kayla's notes (Part 3): you own the full cross-check described in Part 1 — every wishlist / mistakes-to-avoid / don't-like item in your scope gets an in-model / missing / contradicted verdict, incl. wide doors and hallways, no-threshold shower and bathroom clearances, public vs private grouping, noise separation (closets/bathrooms as buffers), broken-open (not open-concept) living, sight lines (no view of a toilet, bedroom or laundry from public areas), scullery/butler's pantry, mudroom and entry drop zones, and storage where things are used.
- Parents' house: aging-in-place — door widths, bathroom layout, step-free potential, porch egg-chair zone clearances.
- Sight lines and dead corners: space that exists on plan but can't hold furniture or storage.

**Output:** findings in the standard format (runbook). Alternatives costed in area (sq ft gained/lost), not dollars. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/01-architecture-flow.md`. **Prefix:** `ARC`.

1. **Kayla cross-check (you own it).**
   - Write a table over ALL 335 items in `$RUN/kayla_checklist.md`, in K order, with columns `| K-ID | Class | Verdict | Evidence |`.
   - **Class:**
     - **PLAN**: a floor or site plan can show it or prevent it (placement, adjacency, room size, door, window, path, orientation, clearance, where storage sits).
     - **SPEC**: fit-out, finishes, equipment or a construction detail a plan can't show (e.g. glass rinser, pant racks, wall blocking).
     - **INFO**: a note, question or empty heading with no requirement in it.
   - **Verdict, PLAN rows only:**
     - **IN**: the model shows it. Cite PF § or file:line.
     - **MISSING**: absent, or only partly there. Say which part.
     - **CONTRADICTED**: the model does the opposite. Cite it.
   - SPEC and INFO rows get Verdict `—` and a few words.
   - Open the section with a summary block:
     - PLAN / SPEC / INFO counts, and the IN / MISSING / CONTRADICTED counts for PLAN items.
     - Then one line per deal-breaker with its verdict: K-328 to K-335, K-005, K-201 + K-304 (closet access not only through the bath), K-070 + K-331 (closets on exterior walls), K-036 + K-329 (laundry tied to the master suite / near the bedrooms), K-037 + K-115 (Costco door pantry↔garage), K-003 + K-060 + K-061 (wide doors and halls: give the door and hall widths from PF §4/§6), K-055 (no-threshold shower).
   - Your Class column becomes the fixed scoring list for the three layout options, so be consistent, and conservative with IN.
2. **Present/absent items from your brief** (two-path kitchen, laundry open from both sides, bedroom→closet direct access). These came from Kayla's October rounds, applied to the OCTOBER model (see `docs/house/House-Review-and-Research-2026-10-28.md`, the "Kayla's notes: what changed" section near line 1091). Check them on the CURRENT model (traced from `main_floor.jpg`, Nov redesign) and say which carried over.
3. **The sore spot** ("2–3 bedroom + hallway arrangement"): identify the bedroom wing in the current model from PF §3/§7. Propose at most 2 alternatives as room rectangles in model coordinates (feet, x = east, y = north), with the area math: sq ft gained/lost and circulation % before/after. The layout designers will read these.
4. **Furniture fit:** use the model's `main_furniture` table (`tools/model_data.py`) where it exists.
5. **Code:** cite only room-size and clearance items you can find in the library (ABC 2023 Section 9.5 covers room sizes; search it, don't assume article numbers).
6. **Parents' house:** a short final section (second pass), from `docs/small_house/` only.
7. **Budget:** 30 findings rows or fewer. Merge duplicates; the Kayla table carries the item-level detail.
