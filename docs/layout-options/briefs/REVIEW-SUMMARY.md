# Review summary for the layout designers (coordinator, 2026-11-09)

What the review found that a main-floor layout must answer. Full detail is in `$RUN/findings/0*.md`; cite findings by ID.
- Current-model numbers, computed the same way your variant will be: `$RUN/computed/matrix.md`.
- Code's findings (`08-code.md`) are appended at the bottom of this file when they land. **Re-read this file before you finalise.**

## 1. Blockers (can't build / won't pass as drawn)

| ID | Blocker | Can a main-floor layout fix it? |
|---|---|---|
| **CODE-01** | **The main stair is one 4,191 mm flight; the maximum is 3.7 m (ABC 9.8.3.3).** See §5. | **Yes, and every option must fix it:** a landing or a turn. |
| STR-04 | **Over the Part 9 size limit.** Building area is 608 m² to the outside face (permit README §1.1; the same method as `matrix.md`, 0.5 ft offset), against 600 m² (ABC Div. A 1.3.3.3). Above 600 m², Part 3 applies. | **Yes, and every option must report its building area.** The README's smallest fix trims about 160 sf (15 m²) of enclosed area for margin. The cheapest square feet are the garage's (COST-02: the garage is 24.34 ft wide, so 6.6 ft of depth = 160 sf). Detaching the garage would break Kayla's Costco-door deal-breaker (K-037), so don't. |
| STR-01 | The basement ICF walls are past the Part 9 table: 12.125 ft (3.70 m) high against a 3.0 m limit, with 11.75 ft of backfill. | No (basement height). Leave it unless your option changes the basement, and list it as still open. |
| STR-02 | The pool pit runs 4.8 ft below the house footings, and the deep footing is drawn narrower than the footing above it. | No. List it as open. |
| STR-03 | The pool-room floor spans 26.95 ft (x 69.38–96.33, y 18.15–52.76), beyond the Part 9 joist tables. | Only indirectly: a main-floor bearing wall over a basement support line helps the engineer. Don't claim it as fixed. |
| PLB-01 | The pool/spa drain-down (about 35,100 L) and filter backwash have no legal destination (SOP 2.1.2.6 keeps them out of the septic). | No. List it as open. |

## 2. Kayla's deal-breakers on the current model (ARC cross-check)

| Deal-breaker | K-IDs | Current verdict | Evidence |
|---|---|---|---|
| Bedroom directly next to the foyer | K-328 | IN | |
| Laundry far from the bedrooms | K-329 | MISSING | 103.1 ft master→laundry |
| Major traffic only through the kitchen zone | K-330 | IN | |
| Closets on exterior walls | K-331 / K-070 | **CONTRADICTED** | BR2 WIC 3.0 ft west; LINEN 1.2 N + 9.0 E |
| Full open concept | K-332 | IN | |
| Closet reachable only through the master bath | K-333 / K-201 / K-304 | IN | the M49 opening is only 27.6 in |
| Bedroom sharing a wall with the living room | K-334 | IN | |
| Garage at the rear / drive past the bedrooms | K-335 / K-005 | **CONTRADICTED** | the west drive is 9.3 ft from BEDROOM 2, and the garage doors face it |
| Laundry tied to the master suite | K-036 | MISSING | no master W/D |
| Costco door, pantry↔garage | K-037 / K-115 | MISSING | the scullery shares 8.7 ft with the garage, 0 doors |
| Wide doors and halls | K-003 / K-060 / K-061 | MISSING | single doors: 7 under 32", 11 at 32–35", 4 at 36"+ |
| No-threshold shower | K-055 | MISSING | the shower pans are drawn raised |

Overall, of the 164 PLAN items: IN 62, MISSING 89, CONTRADICTED 13.

## 3. Should-fix findings a layout can move (main floor)

- **ARC-01, SITE-03, SITE-04: drive and garage doors.** The west drive passes Bedroom 2 at 9.3 ft, and plowed snow piles at its dead end (y 42) onto the meters, the service lines and the septic tank 10 ft away.
  - Turning the garage doors south (K-012 wants the drive south) fixes K-005 and K-335. It also frees the west side for the septic and services.
  - The site's drive geometry then changes: that is a site departure, so draw it, list it and cost it.
- **ARC-02, PLB-09: laundry.** Zero-area fix: LINEN (55 sf, x 121.94–128.13, y 20.56–29.51) becomes a MASTER LAUNDRY on the master-bath wet wall.
- **ARC-03: Costco door.** The scullery↔garage wall at x = 24.34 has 4.27 ft clear for a 3 ft door. The garage slab is 1.5 ft lower, so it needs 3 risers or a landing.
- **ARC-05: doors.** 8 openings are under 32". Use 36" doors (K-061). Code is checking M28 (28.8", on the garage→stair route) against ABC Table 9.5.5.1.
- **ARC-06: no-threshold shower (K-055).** A curbless shower needs a recessed floor. Flag it for the engineer.
- **ARC-07, COST-07: circulation.** 891 sf (16.2%). The 80.5 ft × 5.5 ft spine is 481 sf, 54% of the hall area. The foyer is 309 sf. 160–250 sf is recoverable without losing a function.
- **ARC-04: closets on exterior walls.** The bunk room and the study have no closet.
- **ARC-08: bedroom-wing noise.** Bedroom 2 shares 12.7 ft of wall with the laundry and mudroom, and 14.8 ft with the garage. ARC has two "sore spot" alternatives with rectangles and area math in `01-architecture-flow.md`, section "The sore spot".
- **ARC-09:** no powder room; the nearest WC from the foyer is 65.8 ft away.
- **ARC-14:** no vestibule (K-041), the foyer has no drop zone, and the mudroom has no exterior door.
- **ARC-15:** no library; only 2 non-master bedrooms plus a windowless flex room.
- **ARC-10, ARC-11: kitchen.** The triangle is 41.4 ft against Kayla's 26 ft; the aisle is 47" against 54"; no dishwasher is drawn; the island sink goes against K-108.
- **ARC-16, ARC-19, ARC-20: daylight.** Only 4 rooms have windows on 2+ walls. 27 heated rows have no window, including the STUDY, FLEX, OFFICE and FOYER. The great room has north glass only.
- **PLB-08, GAS-01, GAS-04: mechanical rooms.** The laundry is interior (the dryer is 23.7 ft from an exterior wall). The basement UTILITY room and the pool-equipment room have no wall to outdoors. A main-floor layout can give the laundry an exterior wall and keep a vertical chase clear over the UTILITY room (basement x ≈ 22–37, y ≈ 35–43).
- **PLB-03, PLB-11: wet walls.** There are 14 main-floor wet groups, only 1 stacked over a basement group. The master wing is 120–145 ft of drain run from the drain exit at (22.16, 58). Grouping wet rooms nearer the west/centre, or over basement wet rooms, shortens it (drain-run index in `matrix.md`).
- **ELE-05, GAS-02: meters.** The meters sit under Bedroom 2's west window. If your west wall changes, say where the meters go.
- **STR-05, STR-06, STR-08, STR-13: structure.** The garage west wall is 73% openings (STR-06). Stair headroom has a 43 mm margin (STR-08). No main-floor wall is marked bearing (STR-13).
- **COST-08: corners.** 30 corners (17 outside, 13 inside) and 395.5 ft of perimeter, about 86 ft more wall than an equal-area rectangle.

## 4. Fixed constraints (unless your option draws, lists and costs a departure)

- **Envelope:** heated bounding box about 120.9 × 66.6 ft; garage on the west edge; front porch south; road assumed south (`site.scad:8`).
- **Basement:** under the centre only (3,475 sf), with crawl-space wings W and E.
- **Stair:** top (nosing) x 42.65–47.27, y 47.1; foot y 28.725 (basement); 22 risers. If you move it, the basement must still work.
- **Site:** septic tank (x −3..3, y 52–64) and field on the west; well at (150, 75) on the east; the services enter on the west.

## 5. Code findings (Wave 4): read these, they change the stair

| ID | Severity | Finding | What a layout must do |
|---|---|---|---|
| **CODE-01** | **Blocker** | **The main stair is ONE flight of 22 risers rising 4,191 mm (13.75 ft floor to floor). ABC 9.8.3.3.(1) (abc_2023 p.852): "The vertical height of any flight of stairs shall not exceed 3.7 m."** It's 491 mm over. Nobody had caught this, including the permit README. | **Every option must split the stair into two flights with a landing** (a straight run with a mid-landing adds about 4 ft of run; an L or U turn is more compact). Rise 7.5 in and run 10.5 in pass (Table 9.8.4.1, p.853), and clear width 1,286 mm passes. Show the new stair on both levels: top (main floor opening), the landing, and the foot (basement). If the foot moves, check the basement room it lands in, and make `basement_<x>.scad` if needed. |
| CODE-02 | Should fix (won't pass as drawn) | Door M28 (28.8 in = 732 mm, from the N-S hall to the stair-top landing) is under the 810 mm that Table 9.5.5.1 (p.842) requires for doors at the entrance to stairs to a finished floor. Declaring another line of passage doesn't exempt it. | Every door into the stair landing at least 810 mm (Kayla wants 36 in anyway), or a wall-free opening. |
| CODE-07 | Consider | The stair-top landing is 975 mm along the stair; a landing that turns 90° may need to be as long as the stair is wide (1,286 mm) (9.8.6.3, p.856). | Make landings at least as long as the stair width. |
| CODE-03 | Should fix | Building area is 587.0 m² at centre lines, 595.4 at the model's 0.4 ft wall, 603.8 at 0.4 ft out, and 608.0 at 0.5 ft out (the README figure). The 600 m² line is crossed 0.35 ft (4.1 in) out from the centre line, so the house is **probably over**. The README's §7 "626 m²" is stale. | Report your building area by the `matrix.md` method (0.5 ft offset), and aim for at least 15 m² (160 sf) of margin under 600. |
| CODE-05 | Should fix (won't pass as drawn) | The patio guard over the exit-stair areaway is 1,067 mm against a 1,070 mm minimum. | 44 in guard if your option keeps it. |
| CODE-11 | Consider | Porch floors are 610 mm above grade, 10 mm over the 600 mm guard threshold. The garage steps need a landing where the door opens onto them. A door onto a floor more than 600 mm above ground needs a guard. | Note it if your option changes porches or garage steps. |
| CODE-04 | Should fix | ABC 7.2.2.4 sends private-pool waste water to a municipal drain, and a rural lot has none (supports PLB-01). | Basement item; list it as open. |
