# House — Layout Review & Build Research (Alberta)

Compiled 2026-10-28 for Jordan (and Kayla). Purpose: one document to make
the next round of design decisions from, before the next SCAD editing
session.

**What's in it**

- **Part 1 — Layout review.** An independent pass over the current model
  (`nuniesmith/house` @ `b22774d`): circulation and pathways, a full
  room-size table, and the foundation facts the rest of the document has to
  respect. Default model state reviewed: `changes = true` (Kayla's rounds
  1 + 2 applied), `stair = "proposed"`.
- **Part 2 — Foundation, windows & materials.** ICF foundation systems and
  costs for the 100 × 60 ft, 12-ft-wall basement; windows specced for
  Alberta winters; framing, insulation and drywall, including a starter
  materials-list structure.
- **Part 3 — Site systems.** Water wells under Alberta rules, geothermal
  (ground-source heat pumps) with an honest operating-cost comparison, and
  heated driveways/walkways.
- **Decision list.** Every decision the three parts land on, consolidated
  at the end of this document. Each research section also keeps its own
  short decision list and its sources (URLs) — costs are CAD, 2025–26,
  Alberta-specific where a source exists, and anything that couldn't be
  verified is flagged "(unverified)" in line.

**The house in numbers (from the model):** ~5,300 sq ft main floor
(wall centre lines), 6,000 sq ft basement (100 × 60, 12-ft ceilings,
indoor pool), ~2,000 sq ft of porches. Rural Alberta land, not yet chosen —
so well + septic, unknown gas service, climate zone 7A/7B depending on
parcel.

**Headlines**

- The bedroom wing's flow problems are **fixed in the current model** — the
  rebuild (PRs #5–#7) put in the central hall, and Bedrooms 2, 3 and 4,
  Bath 2 and the PWDR all connect properly now. The one layout decision
  left is **where the basement stair goes** (Part 1, §1.3).
- The basement still has **no bathroom** — worth fixing on paper now,
  because its rough-in is a before-the-pour decision.
- ICF: plan on an **8-in core** (~$135K–$190K planning allowance for the
  basement walls); the waterproofing stack is the line to get in writing.
- Windows: **triple-pane, U ≤ 1.0** is the spec; it's the easiest energy
  money in the build.
- Geothermal works in Alberta but **loses to gas on operating cost** at
  today's rates — whether a parcel has a gas line is a land-buying
  question, not a mechanical one. Budget **$0 in incentives** (Greener
  Homes is closed; nothing provincial exists).
- Snow melt: do the **steps, walkways and garage apron** (hydronic if the
  house has a boiler anyway); a full heated driveway doesn't pay.
- Well: budget **$15–35K** drilled and installed plus **$5–12K**
  treatment, design for **12–18 gpm**, and never drill without written
  dry-hole terms.

---

---

# Layout review — circulation, room sizes, foundation (current model)

Source: `nuniesmith/house` @ `b22774d` (main, merged PR #7), read 2026-10-28.
The repo is now table-driven: `main_floor.scad` / `basement.scad` hold room,
door and window tables, `house_lib.scad` holds the shared modules and the
basement alignment, `house_combined.scad` just stacks the two, and
`tools/check_layout.py` checks reachability. The repo's own `REVIEW.md`
(Oct 2026) documents the rebuild; this review is an independent pass over the
same files, plus the items in §1.3 and §3 that it doesn't cover.

Two switches define the model you look at:

- `changes = true` (default): Kayla's notes, rounds 1 + 2, are applied.
  `changes = false` shows the architect's plan as drawn.
- `stair = "proposed"` (default): the basement stair is a U-stair in the
  former bar. `stair = "as_drawn"` keeps each drawing's own stair — and the
  two drawings' stairs do not meet (see §1.3).

Room dimensions below are the model's wall-centre-line rectangles, so they
run roughly 5–10% larger than finished clear sizes. The rebuild measures
~5,300 sq ft of main-floor rooms this way; the earlier model (~4,300) had
used the plan's printed clear sizes as wall-to-wall boxes and was ~20%
undersized.

**Correction to this review's first pass:** the first draft of this section
was written against the superseded `6acf434` model (the oryx clone was a day
behind GitHub — Jordan spotted it). Its four headline findings — Bedroom 4
sealed, Bedroom 2 reachable only through Bedroom 3/the laundry, Bath 2
sealed, PWDR through the pantry — match the rebuild session's own bug list
for that old model in `REVIEW.md`, and **all four are fixed in the current
model**, as detailed below. The first draft is replaced by this version.

---

## 1. Circulation

### 1.1 The bedroom wing — fixed, and the fix is the one that was needed

Tracing the current door table (`changes = true`):

- The **main hall** (garage → kitchen, 30 × 4.4 ft) is a clean spine: garage
  door at its west end, mud room opening along it, kitchen at its east end.
- A **new 4-ft central hall** leaves the main hall beside the laundry and runs
  straight north into the **bedroom hall**, in line with it (no jog). The
  laundry (now 7½ × 11½ ft) has one door off this hall and is no longer a
  through-route.
- **Bedroom 2** has a hall door, and its WIC and Bath 2 are a proper en-suite
  off the bedroom (the old through-the-bath/through-the-laundry arrangements
  are closed in `changes = true`; as drawn, Bath 2 still opens off Bedroom 2,
  so it is not sealed in either state).
- **Bedroom 3** has a hall door; its WIC and Bath 3 sit in their own little
  vestibule off the bedroom, as drawn on the plan.
- **Bedroom 4** is entered from the main hall through a short vestibule past
  Bath 4/WIC, has an en-suite Bath 4, a direct Bedroom 4 → WIC door (Kayla's
  note), and a door to the front porch.
- **PWDR opens off the main hall** (door at its south wall) — no longer
  through the pantry. The pantry itself has doors on both sides, the linen
  closet opens off the bedroom hall, and both sit between the wing and the
  nook where they belong.

Verdict: the wing's flow is now conventional and good. The remaining wing
note is sizing, not flow: Bath 2 is ~5.2 ft wide at centre lines (~4.8 ft
clear) — workable with the tub along its 10-ft length, but it is the tightest
bath in the house, and WIC 2 (~25 sq ft) is a modest walk-in.

### 1.2 Centre, east, and basement — good, with Kayla's round 2 in

- Kitchen: one 4-ft work aisle (range wall + island sink), fridge and wall
  ovens on the range wall facing the aisle, through-traffic routed north
  (nook ↔ family) and south (hall/butler's ↔ family) of the work zone, and
  the nook opening widened to 5 ft. The two-paths problem is solved properly,
  not just with a door.
- A new 4-ft hall beside the shortened butler's pantry runs kitchen → dining
  room, so the dining room no longer routes through the pantry.
- Master wing: gallery → office (cased opening) and suite (double doors);
  suite → WIC direct door; a **master laundry (W/D)** carved from the west
  5 ft of the closet, opening off the dressing area; shower enlarged to
  ~11.7 × 5.7 ft with a bench; WC separate.
- Basement: theater, pool room and pool equipment all have real rooms and
  doors now; the NE storage room is walled with a door; the rec room/library
  is one open floor with the coffee/bar island; the exit door is cut through
  the foundation at the foot of the exit stair. All of the old basement's
  "open floor pretending to be rooms" issues are gone.

### 1.3 What is still open

1. **The basement stair is the one real decision left in the layout.**
   The architect's plan draws a short stair at the back of the garage; the
   basement sketch draws its stair beside the utilities. Placed under the
   house, the sketch's stair comes up through the office/master suite, and
   the plan's stair lands west of the basement entirely (and shows only 7
   treads for a 13-ft drop). The model's default (option A) puts a U-stair
   where the bar is, landing mid-rec-room; option B extends the basement
   west under Bedroom 3/garage and moves the theater/pool; option C keeps
   the sketch's stair and moves the office. `REVIEW.md` recommends A. This
   needs Jordan's (and Kayla's) call — it is Decision #1 in the compiled
   list at the end of this document.
2. **One interior stair vs two.** Both the old model and the original
   drawings effectively had more vertical routes; the rebuild has exactly
   one interior stair (plus the exterior exit stair). If a second stair
   (e.g. the west wing down to the theater/pool end) is wanted for
   convenience, it has to be designed in — it is not in either drawing.
3. **There is still no basement bathroom.** A pool, hot tub, theater,
   library and music room with no WC or shower/change room on the level:
   swimmers cross the rec room and climb the main stair in wet swimsuits.
   A WC + shower/change room beside the pool vestibule (or carved from the
   pool-equipment strip) is the single most useful room the basement lacks,
   and its plumbing rough-in is a before-the-pour decision.
4. **Theater under the laundry/pantry/nook** — plan sound and vibration
   isolation for that ceiling (also in `REVIEW.md`).
5. **Exit stair vs side porch** — as sketched, the exit stair's areaway runs
   under the side porch; the porch floor needs an opening there or the stair
   moves (also in `REVIEW.md`).
6. Small stuff: the garage floor sits 1.5 ft below the house floor with
   steps up inside the garage at the hall door (fine, but it makes the
   garage→house door a poor accessible entry); the garage's side-load doors
   are an assumption (the plan image cuts off the west wall); no basement
   windows are drawn, so any future basement bedroom needs an egress window
   roughed in now.

---

## 2. Room sizes — main floor (wall centre lines, sq ft rounded)

| Room | Size (ft) | Sq ft | Note |
|---|---|---|---|
| Garage | 25.2 × 31.8 | 801 | Floor 1.5 ft below house; side-load doors (assumed) |
| Mud room | 11.7 × 7.6 | 89 | With stoop outside |
| Main hall | 30 × 4.4 | 132 | The wing's spine |
| Bath 4 | 8.6 × 5.2 | 45 | En-suite |
| WIC 4 | 5.2 × 5.2 | 27 | Modest |
| Bedroom 4 | 18.3 × 14.3 | 262 | Plus a door to the front porch |
| Bedroom 3 | 17.8 × 13.4 | 239 | Behind the garage |
| WIC 3 / Bath 3 | 5.3 × 5.6 / 9.3 × 5.6 | 30 / 52 | In Bed 3's vestibule |
| Bedroom 2 | 14.9 × 15 | 223 | |
| WIC 2 / Bath 2 | 5.2 × 4.8 / 5.2 × 10 | 25 / 52 | Bath 2 is the tightest bath (see §1.1) |
| Bedroom hall + alcove | 11.5 × 4.3 | ~60 | Serves Beds 2 + 3 |
| Central hall (new) | 4 × 11.5 | 46 | Kayla round 2 |
| Laundry (wing) | 7.5 × 11.5 | 86 | Was 152 as drawn, and a through-route |
| PWDR | 7.3 × 6.3 | 46 | Generous for a powder room |
| Linen | 7.3 × 5.2 | 38 | |
| Pantry | 6.5 × 11.5 | 75 | Plus the butler's pantry |
| Breakfast nook | 13.8 × 19.2 | 265 | |
| Kitchen | 16.1 × 23.1 | 372 | Open zone incl. walkways; work aisle 4 ft |
| Family room | 25.9 × 21.2 | 549 | Printed 16'-6" × 15'-2" is the seating area |
| Dining room | 16.1 × 19.6 | 316 | Deeper than wide (old model had it sideways) |
| Butler's pantry | 12.1 × 9.9 | 120 | Shortened 4 ft for the dining hall |
| Dining hall (new) | 4 × 9.9 | 40 | Kayla round 2 |
| Foyer | 11 × 14.8 | 163 | |
| Front hall | 11 × 13.7 | 151 | |
| Lounge | 14.9 × 21 | 313 | |
| Bar → stair bay | 14.9 × 10.4 | 155 | Becomes the U-stair under option A |
| Gallery | 12.5 × 5.9 | 74 | |
| Office | 12.5 × 12.6 | 158 | |
| Master suite | 18.2 × 22.9 | 417 | |
| Master laundry | 5 × 9.1 | 46 | Carved from WIC (Kayla round 2) |
| Master WICs | 6.5 × 9.1 + 8.4 × 9.1 | 59 + 76 | Still 135 sq ft of closet after the laundry |
| Dressing | 19.9 × 4.2 | 84 | |
| WC | 8.2 × 5.7 | 47 | |
| Shower | 11.7 × 5.7 | 67 | Enlarged, with bench (Kayla) |
| Master bath | 13 × 19 | 247 | Tub modelled |
| Porches | — | ~1,990 total | Front 708 + returns, outdoor living 419, side 286, breakfast 192, master 182, office 130, stoop 67 |

Basement (sketch dimensions, exact): theater 30 × 25 (750); pool room
25 × 35 (875) with a 12 × 20 pool and the hot tub inside the room's north
end; pool equipment 5 × 31 (155); utilities 40 × 15 (600); storage
30 × 10 (300); music room 40 × 20 (800); the rest is the open rec
room/library (~2,300 across its three plates). Ceilings 12 ft.

**Size verdicts:** nothing in the rebuild is undersized except Bath 2's
width, and the space allocation now matches the brief (two laundries, big
kitchen zone, 135 sq ft of master closet even after the laundry carve-out).
The numbers to carry into budgeting are the totals: ~5,300 sq ft main floor
(centre-line), 6,000 sq ft basement, ~2,000 sq ft of porches.

---

## 3. Foundation — alignment facts the research has to respect

- The model draws the ICF shell as **1-ft walls, 100 × 60 ft**, 13 ft of
  wall (12-ft ceiling + 1-ft floor structure), slab under. Core width and
  detailing are research questions (next section of this document) — the
  envelope research recommends an 8-in core, which makes the real wall
  ~13.25 in, not 12.
- **Alignment** (`basement_offset = [30.1, 0]`): the basement spans main-floor
  x 30.1–130.1, y 0–60. Consequences:
  - The **garage and Bedroom 3 are not over the basement at all** — they sit
    west of it and need their own frost-protected foundations.
  - The **pool room sits under Bedroom 4, Bath 4 and the mud room**;
    utilities sit partly under the back porch; the music room sits partly in
    front of the master closets. Per `REVIEW.md`, **~20% of the basement
    lies outside the house's walls** — either the foundation is fitted to
    the house outline, or those parts get structural slabs designed for it.
  - The front porch, side porch east edge, and yard steps are outside the
    foundation and need frost footings/FPSF detailing.
- The pool is ~30+ tonnes of water on the basement slab in a room whose
  ceiling is the main floor's structure: engineered slab/footings plus a
  hard vapour break and dedicated dehumidification over the pool room are
  design inputs **now**, not finishes later (the envelope research's pool
  section says the same from the materials side).
- Before-the-pour decisions to lock with the foundation package: basement
  bathroom rough-in (§1.3.3), pool plumbing, floor drains, radon rough-in,
  well/septic/service entries, and the exit-stair areaway vs side porch
  (§1.3.5).

---

# House Build Research — Foundation, Windows & Materials (Alberta)

**Project:** ~5,300 sq ft heated main floor + 100 ft × 60 ft basement (12 ft ceilings, indoor pool room, home theater), rural Alberta, site not yet chosen.
**Currency:** CAD, 2025–2026 figures. **Code references:** National Building Code — Alberta Edition (NBC-AE), Section 9.36 energy provisions and municipal 9.36 compliance forms (Airdrie / Edmonton / Kneehill County). Alberta spans NBC climate zones **7A** (5,000–5,999 HDD — Edmonton, Red Deer), **7B** (6,000–6,999 HDD — Grande Prairie, colder rural/northern sites) and **8** (≥7,000 HDD — far north). Calgary is Zone 7A on the cusp of Zone 6 values in some tables. **The exact zone locks in only when land is chosen** — several numbers below move one step colder from 7A → 7B.

Items flagged **(unverified)** could not be confirmed from a citable source during this pass — treat them as leads, not facts. Manufacturer R-value claims are the manufacturers' own numbers, not code effective values.

---

## 1. ICF Foundation — 100 × 60 ft, 12 ft walls

### Scale of your basement (drives every number below)

| Quantity | Value |
|---|---|
| Perimeter | 320 lin ft |
| Gross wall area @ 12 ft | **3,840 sq ft** (before openings) |
| Concrete in core, 6 in core | ≈ 1,920 ft³ ≈ **54 m³** |
| Concrete in core, 8 in core | ≈ 2,560 ft³ ≈ **73 m³** |
| Basement floor plate | 6,000 sq ft |

### 1.1 Systems sold and serviced in Alberta

All four major brands are available in Alberta through distributor/dealer networks; on a rural build, **which brand has a stocking distributor and experienced installers within hauling distance of the (unknown) site matters more than brand-vs-brand spec differences**. Confirm the specific dealer once land is chosen.

| System | Origin | Standard block | Core widths | EPS panels | Claimed R | Notes |
|---|---|---|---|---|---|---|
| **Nudura** (Tremco CPG) | Barrie, ON | Largest block in the industry: **96 in long × 18 in course**, 12 sq ft per block, ships folded flat | 4, 6, 8, 10, 12 in | 2⅝ in each side (std); 4 in on XR35 | R-24 std; **R-35** XR35 | Full-height fastening strips on every web; strong distributor/technical-support network is its main selling point [1][2] |
| **Logix** (now also sold as Element ICF) | Canadian; 6 manufacturing plants, stocking-distributor network | 16 in course (12/18 in also appear in its engineering tables) | 4, **6.25**, 8, 10, 12 in | 2¾ in each side | R-25 (Pro, EPS); **R-28** (Platinum, Neopor/graphite EPS) | Publishes a Canadian prescriptive engineering manual keyed to NBC Part 9 — handy for permit backup [3][4] |
| **Fox Blocks** (Airlite Plastics) | USA, wide Canadian dealer network | 16 in course × 48 in long | 4, 6, 8, 10, 12 in | 2½ in each side | R-22 clear-wall; R-24 whole-wall claim | Good published guidance library (sizing, waterproofing, costs) [5][6] |
| **Amvic** | Toronto, ON | 16 in course | R22 line: 4, 6, 8, 10, 12 in; R30 line: 6, 8 in | 2½ in (R22 line); 3¼ in (R30 line) | **R-22 / R-30** | Webs on 6 in centres (R22 line) = more fastening points; reversible blocks [7] |

**Wall thickness warning for the SCAD model:** your model has a 1 ft (12 in) ICF shell. Real total thicknesses:

- 6 in core + standard panels ≈ **11.25–11.5 in** — model is right.
- 8 in core + standard panels ≈ **13–13.5 in** — model would need the shell thickened ~1.5 in, which eats ~1.5 in of interior room depth all around.

### 1.2 Core width: 6 in vs 8 in for a 12 ft below-grade wall

- Building-code minimum concrete core below grade is **6 in**; the 4 in form is never allowed below grade. A 6 in core is prescriptively limited to roughly 14 ft of wall height above grade, and prescriptive tables (NBC 9.15 / manufacturer Canadian tables) assume specific backfill heights and lateral support at top and bottom [5][8].
- Your wall is **12 ft tall with up to ~11 ft of backfill** against much of it, plus it carries a very heavy house (5,300 sq ft main floor + big hip roof). That combination is at or past the comfortable edge of prescriptive 6 in design. **Expect the engineer to land on an 8 in core** (or a 6 in core with heavier rebar and possibly pilasters/thickened sections on the 100 ft walls). Budget and model for 8 in; treat 6 in as a value-engineering outcome, not the plan.
- Cost of the step up: ~19 m³ more concrete (≈35% more core volume) plus a modest block price step — small money against the foundation total, and it buys stiffness for the long 100 ft walls.
- The 100 ft uninterrupted walls also need **control/expansion detailing and careful bracing** — long walls bow during pours if bracing is skimped.

### 1.3 Installed cost (CAD)

Published Canadian ranges for **installed ICF basement wall** (forms + rebar + concrete + placing labour, typically excluding excavation, footings, waterproofing, slab, backfill):

| Source | Range | Basis |
|---|---|---|
| Winnipeg ICF contractor (Assured Foundations) | **$20–30 /sq ft of wall** | Prairie market, contractor's own pricing page [9] |
| Southern Ontario ICF builder (Builders Ontario) | **$38–48 /sq ft** finished basement wall; wall-only worked example ≈ $52/sq ft all-in with HST | Itemized calculator scope incl. bracing, pump, bucks [10] |
| Fox Blocks 2026 cost guide | US$22–45 /sq ft installed basement wall (US source — treat as directional only) | Manufacturer guide [6] |
| HomeStars Alberta house-cost guide | ICF walls run **$5–15 /sq ft of floor area more** than wood frame (whole-wall comparison, Alberta) | Alberta-specific [11] |

**Planning allowance for this project (estimate, not a quote):** 3,840 sq ft × **$35–50/sq ft** ≈ **$135,000–$190,000 for the basement walls alone**, with the 12 ft height, rural haul distances and 8 in core pushing toward the top. Builders Ontario's rule of thumb — a *complete* foundation package (excavation, footings, walls, waterproofing, slab, backfill) runs **1.8–2.2× the wall cost** — would imply roughly **$240K–$420K all-in** for a foundation of this size; that multiplier comes from a typical-house example, so treat the top end cautiously **(unverified for this scale)**. Get itemized quotes; ICF quotes vary wildly for identical scope (one US owner's quotes ranged $25–45/sq ft for the same job [12]).

### 1.4 Footings and frost depth (Alberta)

- **Code minimum footing depth in Alberta is 1.2 m (4 ft) below finished grade** — this is the number every municipal guide cites [13][14]. In practice, frost penetration in parts of Alberta (notably the Edmonton region) is deeper than 1.2 m for unheated/shallow elements; utility water lines are buried much deeper. **For your 12 ft basement this is moot** — the footing sits ~3.7 m down, far below any frost line. Frost depth still governs the **garage slab edges, porch/deck footings, the walkout/exterior stair tower, and any frost walls**, which need either full-depth footings or a frost-protected shallow foundation (insulated wing) design.
- **Footings under ICF:** a conventional reinforced concrete strip footing, poured first, with vertical dowel rebar projecting up into the ICF core; the wall is then stacked on it. For a 12 ft wall on unknown rural soils, footing size is an engineer's number (commonly 24–36 in wide × 10–12 in thick on decent soil **(unverified — depends on geotechnical report)**). Foam footing-form systems (e.g., Fab-Form FastFoot) and brand footing forms exist and speed this step [15].
- **Alberta soils note:** much of prairie Alberta has **sulphate-bearing soils** — specify sulphate-resistant cement (Type HS or MS) for footings/walls if the geotech report confirms exposure; this is routine Alberta practice [16]. A geotechnical report is effectively mandatory for a house of this size and weight — budget for it.
- **Radon:** Alberta is a high-radon province and Calgary-area guidance flags it explicitly [17]. NBC-AE requires a radon rough-in (sealed slab, granular layer, extraction pipe rough-in). With ICF walls + a sealed, insulated slab this is cheap to do perfectly at build time — do not value-engineer it out.
- **Winter pouring:** one genuine ICF advantage in Alberta — concrete curing between two layers of EPS is protected from freezing, so foundation work can proceed in cold weather that would stop conventional forming [18].

### 1.5 Waterproofing and drainage below grade (the standard Alberta stack)

Code minimum is *dampproofing*; on a finished basement of this value, build the full *waterproofing* stack. The accepted sequence (Fox Blocks / ICF Magazine guidance) [19][20]:

1. **Peel-and-stick "flood boot"** wrapping the footing-to-wall cold joint, carried at least 12 in above the anticipated water table — the cold joint is the #1 leak path [21].
2. **Self-adhered or fluid-applied waterproofing membrane** over the full below-grade EPS face (Nudura's Tremco parent sells bundled ICF + waterproofing systems — one warranty throat to choke).
3. **Dimple drainage membrane** (e.g., DELTA-MS, Platon) outboard of the waterproofing — creates the drainage gap and protects the membrane from backfill damage. On ICF it fastens into the block webs. Drainage board is **not optional** in this stack [22].
4. **Weeping tile:** continuous 4 in (100 mm) perforated pipe at the footing, bedded in and covered by ≥6 in washed rock, wrapped in filter fabric, draining to an interior sump pit (rural site = sump pump, with battery backup; daylight outlet only if the site grades allow) [21].
5. **Under-slab:** poly vapour barrier sealed to the footing/wall system + radon granular layer (see 1.4). ICF's airtightness *increases* moisture drive through the slab, so the under-slab barrier matters more here, not less [20].
6. **Backfill carefully** (no frozen lumps, no sharp rubble against the membrane) and finish-grade sloping away from the house.

### 1.6 ICF vs poured concrete + insulation — for *this* basement

| Factor | ICF | Poured + exterior/interior insulation |
|---|---|---|
| Bare-wall sticker price | Higher — form cost is real; published comparisons put ICF ~5–10% over poured for the wall itself [23], up to 10–20% over a *comparable insulated* poured foundation [15] | Cheapest structure-only |
| Apples-to-apples (finished, insulated, ready to drywall) | Often **cost-neutral or better**: insulation, vapour control and drywall fastening strips are built in [10][23] | Needs exterior rigid foam + interior framing/insulation/vapour barrier added — labour-heavy |
| Thermal | R-22–24 continuous, no thermal bridging, thermal mass; meets 9.36 foundation-wall minimums (RSI 3.46 ≈ R-19.7 in 7A/7B) straight out of the box [24] | Same R achievable, but bridging through slab edge and framing; more pieces to get wrong |
| Finished-basement comfort | Warm walls, very low air leakage, quiet — suits a theater/rec room basement | Fine if detailed well; colder wall surfaces if insulation is interior-only |
| **Pool room behaviour** | **Strong fit:** concrete core doesn't care about humidity; interior EPS face must still be covered by a thermal-barrier finish (code) — use glass-mat/cement board, not paper-faced drywall, in the pool room (see §3.4). Continuous vapour control is inherent to the assembly | Interior-insulated poured wall in a pool room is a classic rot trap — humid air reaching cold concrete condenses *inside* the stud cavity. Exterior-insulation-only poured walls can work but are the least common residential detail |
| Schedule | Fast stacking; winter-friendly pours; one trade does structure + insulation | Forming/stripping + separate insulation and framing passes |
| Risks | Needs an experienced ICF crew (bracing, pour lifts ≤ ~4 ft, consolidation); changes after the pour are expensive; rural dealer support varies | Every Alberta concrete crew can do it; easier late changes |

**Verdict for this design:** with a finished, humid, 12 ft basement, ICF is the right call and the premium over a *properly insulated* poured wall is small. The decision is really about locking the **core width, brand/dealer and crew** — not ICF yes/no.

### 1.7 Extending ICF above grade for the main floor?

- Typical whole-house ICF premium over wood frame is often quoted at **~3–5% of total build cost** (Fox Blocks) [6] or **+$5–15/sq ft of floor area** vs wood frame in Alberta (HomeStars) [11]. Some foundation specialists argue ICF basements can come in *at or below* poured cost because no forms are stripped [25].
- Benefits in Alberta: R-24+ continuous walls with huge thermal mass (chinook swings get flattened), near-zero air leakage, excellent sound/fire/hail resilience, no stud thermal bridging. Downsides: 11–13 in thick walls change window/door jamb detailing and eat floor area; big window openings need bucks and lintel engineering; fewer rural framers' worth of ICF-experienced trades above grade; design changes after pour are costly.
- **Middle path used on many Alberta custom builds:** ICF basement + high-performance wood wall above (§3.1) gets most of the energy benefit at lower cost and keeps window detailing conventional. ICF-to-the-roof pays best on simple rectangular plans; your plan (many wings, porches, big glass) is *not* simple geometry, which is where ICF above grade gets expensive [25].

### Decisions for Jordan — ICF

1. **Core width:** plan on **8 in** below grade (12 ft wall + heavy house) unless the engineer blesses 6 in with added rebar. This changes the SCAD shell from 12 in to ~13.25 in.
2. **Brand follows the dealer/crew, not the brochure** — shortlist Nudura vs Logix (both Canadian, strong support networks) once the land's region is known; get the *installer*, not just the block, quoted.
3. **Waterproofing spec:** full membrane + dimple board + flood boot + weeping tile to sump — write it into the quote scope explicitly; it's the most commonly under-scoped line.
4. **Geotechnical report** before footing design (soil bearing + sulphates drive footing size and cement type).
5. **Above grade:** decide ICF-to-roof vs ICF-basement-only — basement-only is the value pick for this plan's complexity.

---

## 2. Windows for Alberta Winters

### 2.1 The numbers that matter — and a zone clarification

Two different "zone" systems get mixed up in window shopping:

- **NBC-AE Section 9.36 zones (7A / 7B / 8)** are heating-degree-day bands used for the *building code*. Prescriptively, 9.36 caps fenestration U-value at roughly **U ≤ 1.61 W/m²·K in Zone 7A** (per Airdrie's 9.36 compliance form; skylights U ≤ 2.75) with tighter limits in colder zones [26]. Code minimum is a *floor*, not a target — a U-1.6 window is a cold window in Edmonton.
- **ENERGY STAR Canada (NRCan) since v5.0 (2020) uses one national bar — no zones.** Certification requires **U ≤ 1.22 W/m²·K (0.21 Btu/h·ft²·°F) or Energy Rating ER ≥ 34**. The **ENERGY STAR Most Efficient** tier — the benchmark worth shopping against in Alberta — is **U ≤ 1.05 or ER ≥ 40** [27]. If a salesperson shows you a climate-zone map, that's a *US* label.

**Practical targets for this build:**

| Metric | Code minimum (7A) | Sensible Alberta target | Best available |
|---|---|---|---|
| Whole-unit U-factor | ≤ 1.61 W/m²·K | **≤ 1.0** (triple-pane territory) | ~0.8 W/m²·K (high-end triple, krypton) [28] |
| ER | ≥ 25 (alt. path) | ≥ 34 (ENERGY STAR) | ≥ 40 (Most Efficient) |
| Air leakage | — | CSA A440 rated, casement/awning/fixed preferred over sliders | — |

Context: NRCan attributes **up to 35% of a home's total heat loss** to windows, doors and skylights [29][28] — on a 5,300 sq ft house with generous glass, this line item earns its budget.

### 2.2 Spec checklist

- **Triple pane, full stop, for exposed walls.** Triple pane cuts heat loss through the glass ~30–40% vs double, keeps the interior pane warm enough to sit beside at −30 °C, and is the practical standard in Calgary/Edmonton for north and west walls [28]. Typical triple U: 0.8–1.1 W/m²·K vs 1.2–1.6 for double [28].
- **Orientation still matters:** triple-pane/low-e packages sacrifice solar gain. On true-south glass, a higher-SHGC package (or premium double) can net out warmer in sunny Alberta winters; spec the glass package **per elevation**, not one package house-wide [28].
- **Gas fill:** argon is standard and adequate in triple units; krypton performs better in the thinner cavities of triple units but adds cost — worth it mainly in slim fiberglass high-performance units [28].
- **Low-e coatings:** at least one, ideally tuned by orientation (high-solar-gain low-e south; low-solar-gain west). Multiple low-e surfaces are standard in Most-Efficient-tier units.
- **Warm-edge spacers — non-negotiable.** The spacer is the coldest part of the unit and where condensation/frost starts. A triple-pane unit with an **aluminum spacer can underperform a good double-pane unit with a warm-edge spacer** [28]. Also Alberta-specific: Calgary's ~25 chinook days/winter cycle temperatures 20–30 °C in hours, and that freeze-thaw cycling works on seals — warm-edge + dual-seal (PIB primary) construction resists it better [30]. Edmonton doesn't get chinook relief: weeks at −25 to −35 °C will frost the interior edge of a double-pane/aluminum-spacer unit outright [28].
- **Frames:**

| Frame | Cold-climate behaviour | Cost tier | Verdict for this build |
|---|---|---|---|
| **Fiberglass (pultruded)** | Lowest thermal expansion — expands/contracts *with* the glass, so seals live longest through chinook cycling; strong enough for large units; paintable | Premium | **Best choice** for big glass + −40 °C; the Alberta high-performance default (Inline, Duxton, Fibertec) |
| **Vinyl (uPVC)** | Good insulator (multi-chamber, foam-filled better), zero maintenance; large sizes and dark colours are the weak points; quality varies enormously by maker | Lowest–mid | Fine for standard-size openings from a quality maker (All Weather, Ply Gem, Lux PVC) |
| **Aluminum-clad wood** | Wood insulates well; aluminum skin protects outside; must be *thermally broken* — plain aluminum frames are poor insulators and a condensation path | Mid–premium | Good where the wood interior look is wanted (Lux's core product) |
| **Plain aluminum** | Conducts cold straight through unless thermally broken | — | Avoid for this climate except thermally-broken commercial-style systems |

- **Operators:** casements/awnings/fixed seal tightest; sliders and single-hungs leak the most air and are the first to frost. On a house this size, default to casement/awning/fixed and use sliders only where they're really wanted.

### 2.3 Condensation resistance

- Condensation is a *surface-temperature* problem: interior glass/edge temperature vs indoor dew point. Triple pane + warm edge raises edge-of-glass temperature several degrees — that's the whole game at −35 °C [28].
- Ask for the unit's **Temperature Index (I) / CSA A440 condensation resistance** data when comparing quotes, not just centre-of-glass U **(specific published I-ratings per model: unverified — request from each bidder)**.
- NRCan's standing warning: airtight new windows raise indoor humidity (the old leaky windows were ventilating for you), so **humidity control is part of the window spec** — plan winter indoor RH ≈ 30% or lower in deep cold, with an HRV sized for the house. New triple-pane homes commonly see first-winter condensation appear on *other* cold surfaces until humidity is dialed in [27][28]. This matters doubly in your house: the basement pool will be a permanent moisture source, and the pool room must be pressure- and vapour-isolated from the rest of the house (§3.4).

### 2.4 Alberta / Canadian shortlist

| Maker | Base | Products | Why on the list |
|---|---|---|---|
| **All Weather Windows** | **Edmonton** — founded 1978, manufacturing in Alberta, ~300,000 sq ft capacity, ~800 dealers nationally [31][32] | Vinyl (Renova), fiberglass and clad products; triple-pane across the line | The Alberta incumbent: made in Edmonton, dealer/installer coverage everywhere in the province, purpose-built for the climate |
| **Lux Windows & Doors** | **Calgary** — family-owned since 1969, 105,000 sq ft plant, 150+ staff [31] | Aluminum-clad wood, LynX hybrid, PVC; TESORO folding doors | Calgary-made premium line; strong for clad-wood look and big door systems |
| **Inline Fiberglass** | Toronto manufacturing; sells nationally incl. Alberta dealers | Pultruded fiberglass, incl. **Passive House (PHI) certified** windows [33] | The benchmark fiberglass frame; specified on Canadian Passive House projects |
| **Duxton Windows & Doors** | Winnipeg manufacturing (uses Inline lineals); Edmonton location listed [34][35] | Fiberglass, triple-pane low-e; centre-of-glass R-8 packages | High-performance specialist with an Alberta footprint; used on Edmonton deep-energy-retrofit projects [33] |
| **Ply Gem Canada** | **Calgary plant/branch** (7140 40 St SE) plus Edmonton and Lethbridge branches [36] | Vinyl windows/doors, builder to mid-range | Ubiquitous Alberta supply chain; the budget-control option |
| Durabuilt Windows & Doors | Edmonton **(unverified in this pass)** | Vinyl/aluminum | Major Edmonton maker worth adding to the bid list — confirm current lines |

### 2.5 Costs (CAD, installed, 2025–26 Alberta replacement-market data)

New construction buys windows supply-only + install within the framing contract, so use these as planning ranges, not quotes:

| Item | Range | Source |
|---|---|---|
| Standard window, installed (Calgary) | $500–$1,000 | Norden Seal Calgary guide [30] |
| Window replacement, installed (Edmonton) | $850–$1,500 typical; $500–$1,500 broad range | Edmonton cost guides [37][38] |
| Quality triple-pane vinyl/fiberglass, installed (Bow Valley) | $850–$1,600 per window | Windows Canmore [39] |
| Casement, triple glazing, installed (Calgary) | $550–$1,100 by size | Windows A to Z 2026 guide [40] |
| **Triple-pane premium over double** | **+15–25%** per unit (Weather Pro); **+$120–$350 per window** (Edmonton guide) | [28][37] |
| Large picture window 60×48 in | $700–$1,200 (double) — big custom fiberglass units run far above this | [40] |

For a house of this size and glass area, the window package will be a six-figure line item; the **triple-vs-double decision is worth roughly 15–25% of that package**, and in zones 7A/7B it's the easiest energy money in the whole build. Fiberglass vs vinyl is the bigger cost swing — get both quoted.

### 2.6 Hail (brief)

- Alberta is Canada's hail alley (roofing research already on file covers the roof itself). **Vertical glazing rarely fails from hail** — tempered outer lites shrug off most storms; the realistic window risks are chipped cladding/frames and cracked sealed units in extreme events (golf-ball+).
- **Skylights are the exposure.** Rules: glass (not acrylic dome — acrylic embrittles and is the usual hail casualty), **tempered outer + laminated inner lite** (lamination is also the code-driven safety choice overhead), and look for an explicit **hail warranty** — VELUX laminated units carry one [41][42]. One long-running Ontario installer reports <20 hail-damaged skylights in 29 years, nearly all old acrylic domes [43] — so: glass skylights, minimal count, and they're fine.
- Laminated glass on large ground-floor units is also a security/insurance plus, at a modest premium **(premium %: unverified)**.

### Decisions for Jordan — Windows

1. **Set the house spec: triple-pane, warm-edge, argon, U ≤ 1.0, ER ≥ 34** — then tune SHGC per elevation (higher gain south).
2. **Frame call: fiberglass vs vinyl vs clad-wood** — get the same elevations quoted in fiberglass (Inline/Duxton/AWW) and vinyl (AWW/Ply Gem) to see the real delta before deciding.
3. **Operators:** casement/awning/fixed as the default palette; sliders only by exception.
4. **Skylights:** minimize count; glass, tempered + laminated, hail-warranty line confirmed in writing.
5. **Humidity plan is part of the window decision** — HRV/humidification control sized for a house with an indoor pool next door (in the basement).

---

## 3. Framing, Wood and Drywall — Building the Materials List

### 3.1 What the code asks for (NBC-AE 9.36 prescriptive, effective RSI / R)

From municipal 9.36 compliance packages (Airdrie, Edmonton, Kneehill County) [24][26][44]:

| Assembly | Zone 7A | Zone 7B | Zone 8 |
|---|---|---|---|
| Ceiling below attic | RSI 10.43 (**R-59**) with or without HRV in 7A per NEC table; some AB guides allow R-49 with HRV — confirm on the permit form | R-59 | R-59 |
| Cathedral / flat roof | RSI 5.02 (**R-28.5**) | R-28.5 | R-28.5 |
| Above-grade walls | RSI 3.08 (**R-17.5**); R-16.9 with HRV | RSI 3.85 (**R-21.9**); R-17.5 with HRV | R-21.9 |
| Foundation walls (below grade) | RSI 3.46 (**R-19.7**); R-16.9 with HRV | R-19.7 | RSI 3.97 (**R-22.5**) |
| Floors over unheated space | RSI 5.02 (**R-28.5**) | R-28.5 | R-28.5 |
| Heated floor in ground contact | RSI 2.84 (**R-16.1**) | R-16.1 | R-16.1 |
| Slab-on-grade w/ integral footing | RSI 3.72 (**R-21.1**) | R-21.1 | RSI 4.59 (**R-26**) |
| Windows (max U) | **1.61 W/m²·K** | tighter (≈1.40) | tighter |

Read: code wall minimums are *effective* values — a 2×6 wall with R-22 batts lands around R-17.5 effective after stud bridging, i.e., exactly at the 7A line with no margin, and **short of 7B**. Design one step above code; land location decides whether you're forced to.

### 3.2 Exterior wall options for the main floor

| Assembly | Effective R (approx.) | Strengths | Weaknesses | Fit |
|---|---|---|---|---|
| **2×6 @ 16 in + R-22/24 batts** (code standard) | ~R-17–19 | Every Alberta framer knows it; cheapest | No margin over 7A code; fails 7B effective target without help; stud bridging | Only if land lands in 7A and budget rules |
| **2×6 + exterior continuous insulation** (1.5–3 in mineral wool or EPS/XPS outboard of sheathing) | ~R-24–30 | Kills thermal bridging; keeps sheathing warm (moisture-safe); conventional framing inside; mineral wool adds fire/sound performance; the "split-insulation" wall northern Canadian guides recommend [45][46] | Thicker wall, window jamb extensions; exterior foam thickness must be enough relative to cavity R to protect sheathing in deep cold (with interior poly, less critical) [46] | **Recommended default** — best performance per dollar and per unit of builder familiarity |
| **2×8 @ 24 in + high-density batts** | ~R-24 | Single-wall simplicity, deep window sills | 2×8s cost more than two 2×4 walls and still bridge at every stud — building-science consensus is it's the worst value of the three [46] | Not recommended |
| **Double-stud (2× 2×4, gap, dense-pack cellulose)** | ~R-30–40 | Highest R per dollar; huge sound isolation; cheap materials | 10–12 in walls, more labour, needs a crew that has done it; cellulose settling/air-sealing detailing is everything | Excellent if a local crew knows it |
| **ICF to the roof** | R-24+ continuous + mass | See §1.7 | See §1.7 | Alternative, not a framing option per se |

**Sheathing:** 7/16 in OSB is the Alberta standard wall sheathing (plywood where budget allows); 5/8 in roof sheathing for snow load and shingle/metal fastening; 3/4 in T&G OSB/plywood subfloor, glued and screwed. Exterior mineral-wool walls typically strap outboard for cladding attachment, which also creates a drained/vented rainscreen gap — good practice in hail-and-chinook country [45].

### 3.3 Structure: floors and roof for *this* plan

- **Spans are the story.** A 100 × 60 ft basement and ~132 ft-wide main floor mean long clear spans (theater, family room, pool room below). Dimensional lumber can't do this — plan on **engineered floor systems throughout**:
  - **Wood I-joists (TJI-type)** for typical 14–20 ft spans, 11⅞–16 in deep;
  - **Open-web floor trusses** where you want long spans *and* duct/plumbing runs inside the floor (very useful over the theater/rec room), up to ~24 ft+;
  - **LVL beams + steel or LVL posts** for the long carries; glulam where a beam wants to be visible.
- **Roof: engineered trusses, not site rafters.** Multiple big hips at 6/12–7/12 with vaults = truss package, full stop. Specify **raised-heel (energy-heel) trusses** so the full R-59 attic insulation depth carries right out to the wall line (standard heels crush insulation at the eaves and cause ice-dam/condensation stripes). Scissors trusses where the vaulted ceilings are (family/master/outdoor living in the model). Trusses are designed for the site's snow load — another number that waits on land location (Alberta ground snow loads vary widely, roughly Ss 1.1 kPa Calgary to 2.2 kPa Grande Prairie, per the roofing research already on file).
- **Lumber species/grade:** Alberta framing is SPF (spruce-pine-fir) #2 & better; MSR/LSL studs worth it for the tall (12–14 ft) straight walls in this design to avoid bowed studs.

### 3.4 Insulation plan (code min → sensible target)

| Location | Code min (7A/7B) | Practical spec |
|---|---|---|
| Attic (blown cellulose or fiberglass) | R-59 (7A/7B per NEC table) | Blown cellulose R-60; it settles — blow to settled depth; air-seal the ceiling plane first |
| Cathedral/vaulted | R-28.5 effective | Ventilated assembly with dense batts + rigid above deck, or closed-cell spray foam; raised-heel + high-density is the fussy detail — get it drawn |
| Above-grade walls | R-17.5 / R-21.9 effective | Per §3.2: 2×6 + R-24 batts (mineral wool preferred for fire/sound) + 2–3 in exterior mineral wool ≈ R-30 effective |
| ICF basement walls | R-19.7 | Included in the ICF (R-22–24) ✓ |
| Under basement slab (heated, w/ in-floor) | R-16.1 heated floor | 3–4 in EPS/XPS (R-15–20) under slab + perimeter edge insulation; more if the pool room floor is heated |
| Rim joists | = wall value | Closed-cell spray foam or cut-and-cobble rigid + seal — the leakiest detail in most builds |
| Garage ceiling/floor over garage | R-28.5 | Batts + sealed gypsum ceiling (also the fire separation, §3.5) |

**Insulation material notes:** fiberglass batts = cheapest, most sensitive to install quality; **mineral wool batts** (Rockwool — Canadian-made) = better fit tolerance, fire and sound, slight premium, the usual custom-home upgrade; **blown cellulose** = best attic value and great in double-stud walls; **closed-cell spray foam** = R-6+/in, air seal + vapour retarder in one, priced per board-foot — reserve for rim joists, cathedral ceilings, and trouble spots, not whole walls, on cost.

### 3.5 Drywall — what goes where

| Board | Where in this house |
|---|---|
| **1/2 in regular gypsum** | Standard interior walls (studs @ 16 in); **not** on 24 in o.c. ceilings (sags) |
| **1/2 in ceiling board / 5/8 in regular** | Ceilings — 5/8 in where trusses/joists are @ 24 in o.c.; also flatter walls on tall 12–14 ft walls |
| **5/8 in Type X (fire-rated)** | **Garage ↔ house separation** (walls and the garage ceiling under any living space) — NBC requires the attached-garage separation to be a gas-tight fire separation; 5/8 Type X on the garage side is the near-universal spec [47][48]; also furnace/utility room enclosures, and doubled-up for the **theater** (mass = sound isolation, with resilient channel) |
| **Moisture/mould-resistant board** (glass-mat preferred, e.g., DensArmor-type; "purple" XP-type) | Bathrooms (outside wet zones), laundry, kitchen splash walls, basement bathroom, mud room |
| **Cement board / glass-mat tile backer** + waterproofing membrane | Inside showers and tub surrounds under tile — **no paper-faced gypsum in wet zones, ever** [49] |
| **Sound-rated laminated board** (QuietRock/SilentFX-type) — optional | Theater walls/ceiling, primary bedroom — delivers big STC gains; heavy and pricey, use selectively [48] |

#### The pool room is its own building-science problem — read this before finishing the basement

An indoor pool room is a natatorium: constant ~50–60% RH warm air trying to drive vapour into every wall and ceiling cavity, plus chloramine-laden air that corrodes metals. Natatorium guidance (ASHRAE-based) is blunt [50][51][52]:

- **Continuous vapour barrier on the warm side of ALL pool-room walls and ceiling** — heavy poly sheeting (10–15 mil) sealed at every seam and penetration, or a rated vapour-retarder paint system on masonry; "at least half of problem pool facilities have vapour-retarder defects (rips, poor seals)" [51]. Standard latex paint over drywall is *not* a vapour strategy [53].
- **No standard drywall.** Paper-faced gypsum "fails in natatoriums" [54]. Use cement board or glass-mat board, tile or other non-organic finishes, PVC/marine-grade trim. (Your pool room's ICF walls are a head start: the concrete/EPS assembly tolerates humidity — but the interior thermal-barrier finish in the pool room should be glass-mat/cement board, and the **ceiling** — the main-floor structure above — is the vulnerable assembly and needs the continuous vapour barrier + corrosion protection.)
- **No exposed galvanized metal** — chloramines attack it; even stainless corrodes over time. Epoxy-coated or plastic fittings, corrosion-rated light fixtures and fasteners [54].
- **Dedicated dehumidification** sized to the pool surface, and the room held at **slight negative pressure** (~10% more exhaust than supply) so moist air never migrates into the house [51][52].
- **A pool cover is engineering, not an accessory** — it slashes the evaporation load the dehumidifier must handle [50].
- No wood window/door frames in the pool room [54]; thermally broken, corrosion-resistant everything.

### 3.6 Starter materials list — structure (by assembly)

A takeoff for a build this size is normally organized **by assembly/build stage**, each line with material, spec, unit and quantity from the drawings. Starter structure with the main line items:

**A. Foundation & below grade**
- Geotechnical report; excavation & backfill (m³); strip footings — concrete (m³, sulphate-resistant if required), rebar (kg), footing forms/FastFoot
- ICF blocks by core size incl. corners/T-blocks (sq ft of wall + waste %), ICF bracing (rental), rebar vertical/horizontal (kg), wall concrete (m³), pump time
- Waterproofing membrane (sq ft), dimple membrane (rolls), flood-boot detail, weeping tile (lin ft), washed rock (m³), filter fabric, sump pit + pump + battery backup
- Under-slab: granular/radon layer, poly vapour barrier, slab insulation EPS/XPS (sq ft × thickness), slab concrete + rebar/mesh, radon rough-in piping

**B. Framing package**
- SPF plates/studs by size (2×6 ext., 2×4 int.), LSL/MSR studs for tall walls; LVL/glulam beams; steel posts
- I-joists / floor trusses (lin ft by depth); rim board; 3/4 in T&G subfloor (sheets); hangers, hardware, structural screws/nails
- Roof truss package (count by type: common, hip, scissors, raised-heel); 5/8 in roof sheathing; wall sheathing 7/16 in OSB; housewrap/WRB + tapes

**C. Envelope**
- Exterior insulation (mineral wool boards, sq ft × thickness) + strapping/furring
- Windows & exterior doors by schedule (unit count, per-elevation glass packages); flashing membranes, sill pans
- Roofing (per roofing research on file — metal shingle shortlist), underlayment, ice-and-water at eaves/valleys
- Cladding + soffit/fascia; sealants

**D. Insulation & air sealing**
- Wall batts (mineral wool/fiberglass, sq ft); attic blown cellulose (bags to settled R-60); cathedral assembly materials
- Spray foam (board-ft allowance: rims, trouble spots); poly vapour barrier + acoustic sealant; HRV ducting rough-in

**E. Interior — drywall & finishes substrate**
- Gypsum by type, each its own line: 1/2 in regular; 5/8 in regular/ceiling; 5/8 in Type X; moisture/glass-mat; cement board + waterproofing membrane (showers, pool room)
- Corner bead, resilient channel (theater), screws, tape, compound; primer (vapour-retarder paint system for pool room)

**F. Mechanical/electrical rough-in materials** (usually trade-supplied — list for coordination only)
- Pool dehumidification unit + corrosion-rated ducting; HRV; in-floor heating loops/manifolds if slab is heated

### Decisions for Jordan — Framing & Materials

1. **Wall assembly:** 2×6 + exterior mineral wool (recommended) vs double-stud vs ICF-up. This also fixes the SCAD wall thickness (6.5 in vs ~9 in vs 11–12 in).
2. **Land location locks the code tier** (7A vs 7B changes wall/foundation/attic minimums) — design to 7B numbers now and you're safe anywhere in Alberta.
3. **Pool room finishes:** accept the natatorium spec (vapour barrier continuity, glass-mat/cement board, no exposed galvanized, dehumidification + cover) as a *design input now*, not a finishing decision later — the ceiling assembly above the pool depends on it.
4. **Theater sound package:** resilient channel + doubled 5/8 Type X is cheap at framing stage and miserable to retrofit.
5. **Truss order is the long-lead item** — raised-heel + scissors mix needs the roof geometry frozen earlier than feels natural.

---

## Sources

1. Nudura product overview (Rok Form Solutions, Nudura distributor) — http://www.rokformsolutions.ca/builder.html
2. Nudura XR35 product information (R-35, 4 in EPS, core widths) — http://cms.nudura.com/media/4551/xr35-product-information.pdf
3. Logix ICF Canadian Prescriptive Engineering (NBC Part 9) — https://logixicf.com/wp-content/uploads/technical_library/Canadian-Prescriptive-Engineering.pdf
4. Element ICF / Logix Platinum (Neopor R-28, core sizes) — https://elementicf.com/featured-projects/why-do-net-zero-energy-home-builders-choose-insulated-concrete-forms-and-logix-icf-blocks/
5. Fox Blocks FAQ (core sizing rules: 6 in min below grade, height limits, R-22/R-24) — https://www.foxblocks.com/search?query=1&section=faqs
6. Fox Blocks, "How Much Does an ICF Foundation Cost in 2025?" (2026 ranges, whole-home 3–5% premium) — https://www.foxblocks.com/blog/icf-foundation-cost
7. Amvic ICF (R22/R30 lines, core sizes, panel thickness) — https://www.amvicsystem.com/
8. Logix reinforcement tables referencing NBC 9.15.4.2.A — via [3]
9. Assured Foundations, ICF Foundation Construction Winnipeg ($20–30/sq ft) — https://assuredfoundations.ca/icf-foundations-winnipeg/
10. Builders Ontario, ICF Cost Calculator (apples-to-apples table; complete-foundation 1.8–2.2× rule) — https://buildersontario.com/icf-cost-calculator-2/
11. HomeStars, Cost of Building a House in Alberta: 2026 Guide (ICF +$5–15/sq ft vs wood frame) — https://www.homestars.com/home-constructions-renovations/price-guides/cost-of-building-a-house-in-alberta
12. Owner-reported ICF quote spread ($25–45/sq ft) — https://danssearchformeaning.substack.com/p/build-update-and-price-breakdown
13. Calgary Deck Contractors, Permits & Regulations (ABC frost depth 1.2 m) — https://calgarydeckcontractors.com/guides/permits-regulations-guide.pdf
14. Strathcona County, Residential Accessory Buildings (frost wall/footing min depth 1.2 m) — https://www.strathcona.ca/your-property-utilities/residential-permits/dwellings-and-additions/accessory-buildings/
15. ICF Near Me, ICF Basement & Foundation Systems (10–20% premium vs insulated poured; FastFoot footings) — https://icfnearme.com/products/foundation
16. Alberta foundation trade study material (sulphate-resistant concrete on alkali soils) — https://www.brainscape.com/flashcards/foundation-supports-3620249/packs/5523226
17. HomeStars, Basement Development Cost in Calgary 2026 (radon context) — https://www.homestars.com/home-constructions-renovations/price-guides/basement-development-cost-in-calgary
18. ICF basement cost breakdown (winter pouring advantage) — https://sayforest.weebly.com/blog/do-i-insulate-floors-with-icf-blocks
19. Fox Blocks, "How to Waterproof Below-Grade ICF" (installation sequence) — https://www.foxblocks.com/blog/icf-waterproofing
20. ICF Magazine, "Foolproof Waterproofing for Below Grade Walls" — https://icfmag.com/2006/04/foolproof-waterproofing-for-below-grade-walls/
21. ICF Forming (Nudura installer), Dampproofing & Waterproofing (flood boot, Platon, weeping tile detail) — https://www.icforming.com/16-damproofing-waterproofing
22. AW Waterproofing, Duraflex systems (membrane + drainage board as a system) — https://www.awwaterproofingsolutions.ca/duraflex-products.html
23. Builders Ontario, Foundation Types in Ontario 2026: Poured vs ICF (like-for-like cost) — https://buildersontario.com/foundation-types-in-ontario/
24. LSAC, Illustrated Guide — ABC 9.36 effective RSI table (zones 6/7A/7B, HRV vs no-HRV) — https://lsac.ca/assets/documents/Library/Documents/Planning-Documents/Building-Codes-and-Standards/Building-Code-Documents/ab-building-code-residential.pdf
25. Offsite Builder, "The Real Value of ICFs" (basement cost parity claims; simple-geometry caveat) — https://offsitebuilder.com/the-real-value-of-icfs/
26. City of Airdrie, 9.36 Project Summary compliance form (RSI values; window max U 1.61) — https://www.airdrie.ca/getDocument.cfm?ID=9861
27. Homeowner.ca, "Storm Doors vs Window Film vs Replacement" (ENERGY STAR Canada v5.0: U ≤ 1.22 or ER ≥ 34; Most Efficient U ≤ 1.05 or ER ≥ 40; NRCan humidity warning) — https://www.homeowner.ca/a/storm-doors-vs-window-film-vs-replacement-which-one-fits-an-older-canadian-house
28. Weather Pro Windows & Doors (Edmonton/Calgary), "Are Triple Pane Windows Worth It in Canada?" (U-factors, spacers, chinook/Edmonton analysis, costs) — https://weatherpro.ca/the-pros-and-cons-of-double-pane-vs-triple-pane-windows-in-canada/
29. Western Windows (Calgary), Window Ratings for Alberta (ENERGY STAR U ≤ 1.22 / ER ≥ 34; NRCan 35% heat-loss figure) — https://westernwindows.com/blog/window-and-door-financing/energy-ratings-for-windows-decoded-u-factor-er-and-low-e-coatings-for-albertas-climate/
30. Norden Seal, Window Replacement Calgary (installed costs; chinook freeze-thaw and warm-edge spacers) — https://nordenseal.ca/window-replacement-calgary/
31. Parlun Building, "30 Best Window and Door Manufacturers in Canada" (All Weather Windows — Edmonton, 1978; Lux — Calgary, 1969) — https://www.parlunbuilding.com/top-30-window-and-door-manufacturers-in-canada/
32. All Weather at Home, Windows 101 (made in Alberta; triple-pane position) — https://allweatherathome.ca/windows-101/page/2/?user-location=bc&et_blog
33. SABMag, Building Standards (Duxton triple-glazed fiberglass on Edmonton retrofit; Inline PHI-certified windows) — https://sabmagazine.com/category/net-zero-energy-zero-carbon-living-building-challenge/
34. Composites World, "Pultruded windows: Rising high?" (Duxton fiberglass, Inline lineals, Calgary demonstration project) — http://www.compositesworld.com/articles/pultruded-windows-rising-high
35. Duxton Windows & Doors (Edmonton location listing) — http://www.duxtonwindows.com/
36. Ply Gem Canada (Calgary / Edmonton / Lethbridge branches) — https://www.plygem.ca/
37. General Magazine, "The True Cost of Window Replacement in Edmonton in 2025" ($850–1,500/window; triple upgrade +$120–350) — https://generalmagazine.ca/home-improvement-trends/the-true-cost-of-window-replacement-in-edmonton-in-2025/
38. Canadian Choice / WindowsCanada, Edmonton window replacement ($500–$1,500/window) — https://www.windowscanada.com/edmonton.html
39. Windows Canmore (Bow Valley triple-pane installed $850–$1,600) — https://www.windowscanmore.ca/
40. Windows A to Z, Calgary Window Replacement Cost Guide 2026 (double vs triple by type/size) — https://windowsatoz.ca/articles/window-replacement-cost-guide-2026
41. Hubbard Exteriors, "The Best Skylights for Cold Climates" (tempered/laminated; VELUX hail warranty) — https://hubbardexteriors.com/the-best-skylights-for-cold-climates/
42. GNH Roofing, Skylight Installation: Alberta Homeowner Guide (hail and skylights) — https://gnhroofing.ca/roofs-and-roofing/alberta-homeowner-guide-to-skylights/
43. Skylights Unlimited, Skylight FAQs (29-year hail damage experience; laminated option) — https://skylightsunlimited.ca/index.php/faqs
44. Kneehill County, National Energy Code Compliance Package (9.36.2 RSI tables by zone) — https://kneehillcounty.com/DocumentCenter/View/3570/National-Energy-Code-Compliance-Package-Reduced-File-Size?bidId=
45. Yukon Housing, Energy Efficient Housing Guidelines (split-insulation 2×6 + exterior mineral wool assembly) — https://d7.yukon.ca/sites/yukon.ca/files/yhc/yhc-energy-efficient-housing-guide-cost-optimized.pdf
46. Green Building Advisor, wall assembly discussions (2×8 value critique; exterior-foam thickness) — https://www.greenbuildingadvisor.com/question/what-is-the-best-way-to-build-a-2x8-exterior-wall-and-achieve-r-40
47. NBC garage-separation practice (5/8 in Type X at garage/common separations) — https://steemit.com/drywallpatching/@cynthiakase/drywall-patching-vs-full-panel-replacement-how-to-choose-the-right-fix
48. CraftedCalcs, Drywall Thickness Guide (board types, STC data, ceiling spans) — https://craftedcalcs.com/guides/drywall-thickness-guide/
49. Sensible Digs, Types of Drywall (wet-zone backer practice) — https://sensibledigs.com/types-of-drywall/
50. Elevate Home Guide, Indoor Pools: 2026 Cost & Humidity Guide (cover ROI, dehumidification, negative pressure) — https://www.elevatehomeguide.space/articles/indoor-pool-cost-dehumidification
51. Contracting Business, "Dive into Indoor Pool Dehumidification" (vapour-retarder failure statistics; negative pressure rule) — https://www.contractingbusiness.com/iaq-ventilation/article/20867016/dive-into-indoor-pool-dehumidification
52. DXair, Dehumidification FAQs (ASHRAE natatorium vapour-barrier options: poly sheeting or vapour-retarder paint) — https://dxair.com/pool-room-design-guidelines/frequently-asked-dehumidification-questions/
53. Elevate Home Guide, Pool House HVAC Guide 2026 (envelope/vapour detailing) — https://www.elevatehomeguide.space/articles/pool-house-hvac-guide
54. Chloramine Consulting, "Is a Home Indoor Pool Right for You?" (no standard sheetrock; no exposed galvanized; corrosion) — https://blog.chloramineconsulting.com/residential-indoor-pools

*Prepared 2026-10-28. Costs are planning-grade ranges from published contractor/manufacturer guides, not quotes. Items marked (unverified) need confirmation at design/permit stage.*

---

# Site Systems Research — Wells, Geothermal, Heated Driveway/Walkways

**Project:** Large custom home, rural Alberta (land not yet chosen — no municipal water/sewer assumed)
**Design basis:** ~5,300 sq ft heated main floor + 100 ft × 60 ft basement (6,000 sq ft gross) with indoor pool + hot tub, 4+ bathrooms, large laundry. Total conditioned area likely 10,000+ sq ft once finished basement space is counted.
**Currency / date:** All figures CAD, 2025–2026 Alberta planning numbers unless stated otherwise. Researched 2026-10-28.
**How to read this:** Numbers are for decisions and budgeting, not quotes. Anything marked **unverified** could not be confirmed from a source found in this pass — treat it as a planning assumption to confirm with a local contractor/designer once land is chosen. Location matters enormously in Alberta: depth-to-water, geology, snow load, gas availability, and utility delivery charges all change by county.

**The three headline answers**

1. **Well:** Budget **$15,000–$35,000** all-in for a drilled well + pump + pressure system, plus **$5,000–$12,000** for treatment. Target a sustained yield of **12–18 US gpm**; if the hole only makes ~5 gpm, solve it with a cistern/storage tank and booster pump, not by drilling forever.
2. **Geothermal:** It works fine in Alberta winters (the ground, not the air, is the heat source), but for a house this size expect **multiple units (likely 10–16 tons total)** and **roughly $70,000–$140,000+ installed — unverified at this scale, get real quotes.** Where cheap natural gas is available, gas still heats for roughly **half** the operating cost of geothermal at current Alberta rates. Geothermal's case is strongest if the site has **no gas line** (vs. propane or electric resistance) and because one system can also heat the pool and domestic hot water.
3. **Snow melt:** Do **not** heat the whole driveway by default. Hydronic (gas boiler) melting costs roughly **$1.40/hr per 1,000 sq ft in fuel** vs. roughly **$11/hr per 1,000 sq ft for electric** at the rates below. Best value: hydronic tire tracks on the driveway + full melt on walkways, porch steps and the garage apron. The #1 money trap is "idle mode" (holding the slab just above freezing all winter).

---

## 1. Water Wells (Alberta)

### 1.1 Rules — Water Act, licensing, construction, testing

| Item | What applies to this build |
|---|---|
| Governing law | Alberta *Water Act* and the Water (Ministerial) Regulation set well construction standards and owner/driller responsibilities. |
| Do you need a water licence? | **No, for household use.** Household use = up to **1,250 m³/year per household** for human consumption, sanitation, fire prevention, watering animals, gardens, lawns and trees. No permission or licence is needed to use a well for that purpose (Alberta Working Well, Issue 8). If you divert **more** than that, or use water for non-household purposes, you must contact Alberta Environment and Protected Areas about a diversion licence. |
| Who can drill? | **Only a licensed water well contractor** holding a current **Approval to Drill Water Wells** from Alberta Environment and Parks. Drilling must be supervised/performed by a certified journeyman water well driller (Class A approval covers drilling for diversion/use). Narrow exception: a landowner drilling **their own** well with **their own** rig, solely for household use, is exempt from the approval requirement — not a realistic path for this build. |
| Construction standards | The Regulation prescribes casing type/diameter/wall thickness, annular sealing/grouting, disinfection, yield testing, pump installation and well closure (plugging). Well casing must extend **at least 20 cm above ground surface** (Working Well guidance; many installers use ~30 cm), with a vermin-proof cap with shielded/screened vent, and ground graded to slope away. |
| Paperwork | The driller must file a **water well drilling report** with the province; it lands in the public **Alberta Water Well Information Database (AWWID)**. Keep your copy — it records depth, geology, static level, tested yield and the driller's recommended pumping rate. Never pump above that recommended rate. |
| Testing — bacteria | Test for **coliform bacteria twice a year** (more often if the well is <50 ft deep), via your local Community Health Centre / Public Health Unit (sample bottles and instructions from Alberta Health Services). Disinfect (shock chlorinate) the well annually as preventive maintenance. |
| Testing — chemistry | Test **routine chemistry every few years**, and do a full diagnostic suite on a **new** well before designing treatment (Alberta Agriculture's Level C diagnostic suite is ~39 parameters, approx. **$400**). Have results interpreted by a Public Health Inspector / treatment professional. |
| Owner duties | Maintain the wellhead sanitary, inspect cap/casing/grading, keep contamination sources away and downslope, monitor pumping/non-pumping levels, and **properly plug any abandoned wells** on the property — an open old well is a direct contamination path into the aquifer. |
| Setbacks from septic | See the warning box below — sources found disagree, and this must be confirmed at design. |

> **Setback caution (read this):** Alberta's Private Sewage Systems Standard of Practice separation distances are the controlling document, and secondary sources found in this pass disagree: several cite **15 m (50 ft) minimum between a soil-based treatment field and a water source/well**, while acreage due-diligence checklists commonly cite **30 m to the septic system**. Alberta's own safety-tips summary also lists 15 m (50 ft) from a water source for a treatment system, with much larger distances (90–100 m) applying to lagoons and water bodies, not ordinary fields.
> **Design decision:** plan the site layout with **at least 30 m between the well and any septic tank/field, well uphill of the septic**, and have the certified septic designer confirm the exact Standard of Practice distances for the chosen system type. On a rural acreage this is normally easy to achieve — but it must be drawn on the site plan *before* the house, well, septic, geothermal field and driveway are fixed, because all five compete for the yard.

### 1.2 Drilling methods, depths, yields, costs

**Methods used in Alberta**

- **Rotary drilling (mud rotary or air rotary)** — the standard for most Alberta residential wells: fast through glacial till, sand/gravel and soft bedrock (sandstone/shale). Air rotary is common in hard/fractured bedrock.
- **Cable-tool** — older, slower percussion method; still used by some drillers, can be better in boulders/caving formations. **Unverified** how much cable-tool work remains in Alberta in 2026 — most quotes you get will be rotary.
- **Dual rotary / casing-advance** — used where thick, bouldery glacial till makes conventional rotary difficult; typically a premium price. **Unverified** per-foot premium — ask if the driller expects it.
- **Well completion type:** sand/gravel aquifers are usually **screened** (stainless screen + gravel pack); consolidated bedrock wells are usually **open hole** below casing, producing from fractures.

**Typical depths and yields (planning ranges — geology decides)**

| Formation | Typical depth | Typical yield behaviour |
|---|---|---|
| Sand & gravel (buried channels, river valleys, outwash) | ~100–300 ft (30–90 m) overall is the common Alberta residential band | Best yields; 10–30+ US gpm possible. Higher iron/hardness is common. |
| Bedrock — sandstone/shale (much of central/southern Alberta) | Often 150–400 ft where overburden water is poor or saline | Fracture-dependent: one hole can make 15 gpm and a neighbour's 2 gpm. Water tends to be softer naturally but higher in sodium and TDS. |
| Foothills / mountain bedrock | Highly variable | Depth and yield vary more than almost anywhere in the province; historic coal workings can affect quality (iron, manganese, sulphur). |

Before signing anything, **pull the AWWID records for wells on neighbouring parcels** — reported depths, yields and geology there are the single best predictor of what your hole will do, and drillers will use them to price the job.

**Costs (CAD, 2025/26)**

| Item | Planning range | Notes |
|---|---|---|
| Drilling, per foot | Conflicting published Alberta figures: **$15–$30/ft** (one Alberta new-home guide) vs. **$80–$200/m (~$24–$61/ft)** (acreage guide, central Alberta 30–100 m wells) vs. ~$45/ft (older Q&A). **Use $40–$65/ft as a budgeting band and get local quotes — exact 2026 Alberta per-foot rates are unverified and vary by rig, casing size and rock.** |
| Complete well, total installed | **$15,000–$35,000** typical Alberta range including drilling, casing, pump, pressure tank and electrical hookup. Deeper wells (150–250 m) can push **above $40,000**. |
| Pump + pressure system (within/above total) | Submersible pump package roughly $1,000–$3,200 in published Canadian breakdowns; a **constant-pressure (VFD) pump + larger pressure/storage tank sized for this house will be at the top end or above — unverified, quote it.** |
| Water testing | Bacteria via AHS: no/low charge historically — **verify locally**. Full diagnostic chemistry suite ~$400. |
| Treatment (see 1.3) | **$5,000–$12,000** typical for this house size — budget separately from the well itself. |

**Dry / low-yield hole risk — the contract point that matters most**

- A licensed driller **cannot guarantee the amount or quality of water** under your land — the Alberta Water Well Drilling Association's own fact sheet says so plainly. Quantity/quality are determined by local geology.
- Standard practice is **pay per foot drilled whether or not the hole produces** (a dry hole still consumed rig time, fuel, casing decisions and grouting/plugging). Some drillers offer a reduced dry-hole rate, a test-hole-first arrangement, or a capped attempt — **none of that is automatic. Get it in writing before mobilization:** price per foot for a producing well, price per foot if dry/abandoned, who pays for casing/screen on a failed hole, plugging cost, and what happens after hole #1 (move and retry? deepen? hydrofracture a bedrock well? switch to cistern?).
- Risk reducers, in order: (1) AWWID neighbour records; (2) driller with local formation experience; (3) a test hole / staged contract; (4) designing the house system so a modest-yield well + storage still works (see 1.4) — that converts "low yield" from a disaster into a line item.

### 1.3 Alberta groundwater quality — what to expect and what treatment costs

Alberta's pattern is depth-driven:

- **Shallower sand/gravel water:** lower TDS, but **hard** (calcium/magnesium) and often **higher iron/manganese** — staining, metallic taste, scale.
- **Deeper bedrock water:** naturally "softened" by ion exchange in the sediments — little hardness but **higher sodium and TDS**, sometimes sulphate; can exceed drinking-water aesthetic/health objectives for sodium/TDS.
- **Sulphur (H₂S, "rotten egg"):** associated with sulphate-reducing bacteria and coal/shale formations; also a well-maintenance issue (iron/sulphate bacteria foul wells and pumps).
- **Methane/dissolved gas:** documented in Alberta bedrock groundwater (methanogenic conditions, coal-bearing formations). Usually a venting/safety and nuisance issue at residential concentrations rather than a treatment item — **if gas is noted on the drilling report, raise venting of the wellhead and any enclosed well pit with the driller; specific Alberta residential methane guidance was not verified in this pass.**
- Also test for: arsenic, fluoride, nitrate (health-based), uranium, barium, manganese (now has a health-based guideline in Canada) — all occur naturally in parts of Alberta.

**Typical treatment train for this house (in flow order)**

Sediment filter → iron/sulphur filter (air-injection oxidation or similar) → **large twin-tank water softener** (sized for peak flow, not just grains) → UV disinfection → point-of-use **reverse osmosis** at kitchen/drinking taps. Add whole-house RO **only** if sodium/TDS come back high — it is a different cost class entirely.

| Component | Rough installed cost (CAD) | Notes |
|---|---|---|
| Softener (large / twin-tank, high-flow) | $1,200–$3,500 published for standard homes; **budget $2,500–$5,500 for this house's flow rates — unverified at this size** | Published Canadian ranges: softeners $1,200–$3,500 installed. |
| Iron / sulphur filter | Included in many well combos; well combo systems (softener + iron filter + UV) commonly **$2,500–$5,500** for standard homes | Size up for 4+ bathrooms. |
| UV disinfection | ~$600–$1,200 **unverified** | Cheap insurance on any private well. |
| Point-of-use RO (per kitchen location) | $400–$1,500 installed | Handles sodium/TDS/arsenic at drinking taps without whole-house RO. |
| Whole-house RO (only if TDS/sodium demand it) | **$8,000–$20,000+ — unverified** | Plus reject-water volume — which also loads the septic. Avoid unless the lab results force it. |
| **Realistic total treatment budget** | **$5,000–$12,000** | Excluding whole-house RO. Design only **after** the diagnostic test — buying treatment before lab results is the classic acreage money-waster. |

Pool note: fill/top-up water should go through softening/iron removal **before** the pool equipment — iron and hardness are hard on pool finishes, heaters and the hot tub. That raises the treatment system's required flow/capacity; tell the treatment designer the pool is on the well.

### 1.4 Demand check — is a normal well enough for this house?

**Daily volume vs. the licence cap:** Household exemption is 1,250 m³/year ≈ **3,425 L/day average**. A 2–4 person household with 4+ bathrooms and a big laundry typically uses ~800–1,200 L/day (~300–440 m³/yr). Add indoor pool top-up (see below) and you are still comfortably under the cap. What *can* blow through it is large-scale lawn/garden irrigation in summer — if extensive irrigation is planned, flag it early; it may change the licensing conversation.

**Peak flow is the real design problem, not daily volume.** Simultaneous showers, laundry, dishwasher and a filling tub want **15–20 US gpm delivered at pressure** inside the house. The well does not need to sustain that directly if storage does the buffering.

| Well sustained yield | Sensible system |
|---|---|
| **12–18+ US gpm** (target) | Straightforward: constant-pressure (VFD) submersible pump + pressure tank (e.g., ~80–120 gal drawdown-equivalent). **Unverified exact tank sizing — designer's call.** No cistern needed. |
| **5–10 US gpm** | Workable with a storage/cistern tank (e.g., 1,000–2,500 US gal) + booster pump feeding the house at full pressure/flow. Adds cost and a maintenance item, but completely normal on Alberta acreages. |
| **<5 US gpm** | Problem for this house without large storage. Options: deepen, hydrofracture (bedrock), second hole, or large cistern with trucked-water backup. Decide using the contract terms in 1.2 — before the foundation is poured, not after. |

**Pool specifics:** The modelled pool is roughly 12 ft × 22 ft. Initial fill is on the order of **35,000–50,000 L depending on depth — unverified, depends on final depth profile.** Do not plan to fill it quickly from the well: fill slowly over several days at a rate the well sustains, or truck the initial fill (common practice, and it also avoids stirring up the well). Indoor pools lose far less to evaporation than outdoor pools **if a cover is used and the room dehumidification recovers water**; without a cover, evaporation + splash-out + filter backwashing can run to hundreds of litres per day and also drives the pool-room humidity load. Hot tub: ~1,500 L per fill, drained/refilled a few times a year — trivial for the well, but note **hot tub drains and pool backwash should not go into the septic field without the septic designer's say-so** (volume + chemicals).

### Decisions for Jordan — Wells

1. **Before buying land:** pull AWWID records around any candidate parcel (depths, yields, quality notes) and ask two local drillers what holes there typically cost. A parcel with 8 gpm bedrock wells is a different build budget than one with 25 gpm gravel wells.
2. **Contract:** no drilling without written dry-hole / low-yield terms (per-foot rates both ways, casing/plugging costs, retry plan).
3. **Site plan:** fix well ↔ septic separation at **≥30 m, well uphill**, on the drawing, alongside the geothermal field and driveway — confirm exact distances with the septic designer.
4. **System target:** design for **12–18 gpm sustained**; if the hole delivers less, go cistern + booster rather than chasing yield.
5. **Treatment:** budget **$5,000–$12,000**, but buy nothing until the ~$400 diagnostic test on the finished well is back. Route pool fill water through treatment.
6. **Irrigation:** decide how much lawn/garden watering is planned — it is the one use that can threaten the 1,250 m³/yr household exemption.

---

## 2. Geothermal (Ground-Source Heat Pumps) in Alberta

### 2.1 How it performs in an Alberta winter

A GSHP does not care that it is −35 °C outside, because it is not pulling heat from the air. Undisturbed ground at loop depth in Alberta sits at roughly **5–10 °C year-round** (one Alberta installer cites ~10 °C; published Canadian sources cite 10–15 °C nationally — **use the lower Alberta end for design; the exact figure for your parcel is unverified until a designer models it**).

- **Efficiency:** GSHPs deliver roughly **300–500% efficiency — COP 3–5** — across the season, versus a gas furnace's ~96% and electric resistance's 100%. COP falls as the required output water temperature rises: delivering low-temperature heat (in-floor radiant at ~35 °C supply) can run COP ~4–5; making domestic-hot-water temperatures (~55–65 °C) drops COP toward ~2.5–3. **Design implication: this house should distribute heat at low temperature (radiant floors / oversized fan coils) to get the efficiency you are paying for.**
- **Capacity does not collapse in a cold snap** the way an air-source unit's does — output is essentially flat vs. outdoor temperature. What *does* happen over a long cold winter is gradual cooling of the loop field if it is undersized; the fix is field sizing (and why a proper load calculation + loop design matters more than the brand of heat pump).
- **Design temperatures (for the alternatives discussion):** Edmonton's heating design temperature is about **−30 °C**, Calgary's about **−26 °C** (Hot2000 climate data). Any system — geo, air-source, or gas — must be sized to the parcel's actual design temperature once the location is known.

### 2.2 Loop options and land needed

Rule-of-thumb sizing used across the sources: **vertical boreholes ≈ 150–250 ft of bore per ton**; **horizontal loops ≈ 400–600 ft of pipe per ton**, buried ~4–6 ft deep (below frost influence as much as practical), requiring roughly **1,500–3,000 sq ft of clear land per ton**.

| | Horizontal (trench / slinky) | Vertical (boreholes) |
|---|---|---|
| How | Excavator trenches ~4–6 ft deep; straight pipe or coiled "slinky" pipe | Drilled boreholes typically 150–400 ft deep, spaced 15–20 ft apart, grouted U-loops |
| Land for this house (assume 10–14 tons — see 2.3) | Roughly **0.5–1.0 acre of clear, unserviced field** (15,000–42,000 sq ft) kept free of septic field, well setbacks, buildings, deep-rooted trees and future shops | A drilling pad area only — a few hundred sq ft of borefield footprint plus rig access |
| Cost tendency | Loop field roughly **$1,500–$3,000 per ton** (industry guides, mostly US-sourced — **CAD conversion/scale unverified**) | Loop field roughly **$3,000–$6,000 per ton**; drilling often quoted ~$10–$30/ft of bore, with hard-rock premiums |
| Alberta fit | Attractive **here** because land is available and the field can be trenched while the site is already torn up for the house/septic. Watch: dry Alberta soils conduct heat worse than wet soils — fields are often sized **20–40% larger** in dry sand/soil. | Better where land is tight or soil trenching is poor/rocky. Drilling availability in rural Alberta and mobilization distance can dominate the quote. |
| Watch-outs | Field must be mapped and protected forever — no future building, no septic, careful with later trenching/fence posts | Boreholes for a closed-loop GSHP fall under Alberta's Water Wells / Ground Source Heat Exchange directive — use a qualified driller/installer; approvals/expiry rules apply to the drilling work (**confirm current directive requirements with the installer — the directive found in this pass dates to 2018**). |

**Hybrid worth knowing about:** an **open-loop** system (pumping well water through the heat pump) is cheapest per ton *if* the well has abundant yield and water quality suits — but for this build it competes with the house/pool for the same well, adds pumping energy and discharge handling, and risks fouling heat exchangers with iron. Not recommended as the default here; closed-loop keeps the two systems independent. **Unverified for Alberta permitting specifics — do not assume open-loop is permitted without checking.**

### 2.3 Sizing for THIS house — and installed cost

**Load reality check.** Conditioned area is roughly 5,300 sq ft (main) + most of a 6,000 sq ft basement. A new, well-built Alberta envelope might lose ~15–25 BTU/hr per sq ft at design temperature; a merely code-minimum one, more. That brackets a design heating load of roughly **150,000–280,000 BTU/hr ≈ 12–23 tons** before the pool room. The **indoor pool is its own load**: evaporation control/dehumidification, pool water heating and ventilation air can rival a large room's entire heating budget, and pool water heating is a year-round (not just winter) load.

- Practical expectation: **two (possibly three) residential GSHP units staged together** (residential units top out around 5–6 tons each), or a light-commercial unit — plus a separate solution or water-to-water unit for pool heating. **A CSA F280 heat-loss calculation by the designer is not optional at this size; the tonnage above is a budgeting bracket, not a design — unverified until calculated.**
- A water-to-water GSHP is also the natural partner for **snow melt** (Section 3) and radiant floors — one plant can serve space heat, DHW preheat (desuperheater), pool and melt loads, though melt peaks may still want boiler support (see 3.2).

**Installed cost (CAD, 2025/26)**

| Benchmark | Figure | Source quality |
|---|---|---|
| Typical Alberta residential GSHP | **$25,000–$45,000** for a typical home (most often a 3–5 ton system) | Alberta installer (Alpine GeoThermal, Calgary) |
| Canada-wide typical | $20,000–$40,000 complete; horizontal $15,000–$25,000, vertical $20,000–$40,000 | Canadian installer (Greenfoot) |
| Larger/complex Canadian installs | $55,000–$80,000+ for bigger homes/complex loop fields | Ontario installer guide, 2026 |
| **This house (10–16 tons, multi-unit, pool tie-in)** | **Budget $70,000–$140,000+ — UNVERIFIED extrapolation.** No source found prices a residential Alberta system this large. Get two design-build quotes; expect loop field to be 30–50% of the total. New-build installation (ducts/hydronics roughed in anyway, excavation already on site) should price better than a retrofit of the same size. | — |

Offset against that: the loop field lasts **50+ years** and the indoor units **20–25 years** — the expensive part is essentially permanent infrastructure.

### 2.4 Backup heat, and the honest operating-cost comparison

**Backup/auxiliary norms in Alberta:** GSHP systems are normally sized to carry ~90–98% of annual heating energy, with auxiliary heat for design-day peaks and resilience. Common Alberta arrangements: electric resistance auxiliary in the air handler (simple, expensive to run, rarely used), a **gas/propane furnace or boiler as backup**, or — best for this build — a **hydronic boiler that also serves snow melt and pool backup**. For a rural home of this size, some form of non-electric backup is strongly advisable for power-outage and −40 °C resilience planning (a generator discussion belongs in the electrical design either way).

**Rates used for the math below (state your assumptions — here they are):**

| Rate | Value used | Basis |
|---|---|---|
| Electricity, commodity (fixed contract) | ~7–9 ¢/kWh | Alberta fixed offers ~7.08–9.48 ¢/kWh (2026 rate trackers); Rate of Last Resort default is 12.01–12.06 ¢/kWh (Jan 2025–Dec 2026) |
| Electricity, **all-in delivered** (commodity + transmission/distribution + riders) | **$0.22/kWh planning figure (range $0.18–$0.28)** | Rural (FortisAlberta) delivery charges are materially higher than city delivery. **Exact figure unverified — it depends on the parcel's distributor and rate class, and it is the single most sensitive number in this comparison.** |
| Natural gas, commodity | ~$3.20–$3.70/GJ | Alberta forward/fixed offers 2026 |
| Natural gas, **all-in delivered** | **~$8/GJ planning figure — unverified, confirm locally** | Commodity + ATCO delivery + fees. Note: the federal consumer carbon charge on gas was set to zero effective April 1, 2025, which removed roughly $3.33/GJ that older comparisons still include — **any geothermal payback article written before 2025 overstates gas's cost.** |
| Propane (if no gas line) | ~$0.90–$1.10/L **unverified** | ≈ $36–$44/GJ before delivery fees — i.e., 4–5× the per-energy cost of piped gas. |

**Cost per unit of heat delivered (using the rates above):**

| Heating system | Math | Cost per GJ of heat | Cost per kWh of heat |
|---|---|---|---|
| Gas furnace/boiler, 96% | $8 ÷ 0.96 | **~$8.30/GJ** | ~3.0 ¢ |
| GSHP, seasonal COP 3.5 | $0.22/kWh ÷ 3.5 | **~$17.50/GJ** | ~6.3 ¢ |
| GSHP, seasonal COP 4.0 (low-temp radiant, good field) | $0.22 ÷ 4.0 | ~$15.30/GJ | ~5.5 ¢ |
| Cold-climate ASHP, seasonal COP ~2.0 in Alberta conditions | $0.22 ÷ 2.0 | ~$30.60/GJ | ~11 ¢ |
| Propane furnace, 92% | ~$40/GJ ÷ 0.92 | ~$43/GJ | ~15.6 ¢ |
| Electric resistance | $0.22/kWh | ~$61/GJ | 22 ¢ |

**Read of the table:** *If the parcel has a natural gas line, gas heats this house for about half the operating cost of geothermal*, and geothermal's 7–12 year typical payback claims (which assume displacing electric/propane/oil heat) stretch out dramatically or never arrive on energy savings alone. *If the parcel has no gas* — entirely possible on rural Alberta land — the comparison flips: geothermal at ~6 ¢/kWh-heat crushes propane (~16 ¢) and resistance (22 ¢), and beats a cold-climate ASHP on both cost and deep-cold capacity. **Gas-line availability at the actual parcel is therefore a gating question for the whole heating design** — and the cost of bringing gas in (line extension charges can be substantial) belongs in the land-evaluation checklist beside the well records.

### 2.5 Incentives — status checked 2026-10-28 (read the dates)

| Program | Status | Geothermal eligible? |
|---|---|---|
| **Canada Greener Homes Grant** (up to $5,000) | **CLOSED.** Stopped accepting new applications in 2024 (Feb 2024); final document deadline Dec 31, 2025. Multiple sources + NRCan status pages agree. | Was — irrelevant now. **Do not budget for it.** |
| **Canada Greener Homes Loan** (0%, up to $40,000) | **CLOSED.** Last day to apply **October 1, 2025**; NRCan states funding is fully committed and no new applications can be approved. Previously approved loans are unaffected. | Was — irrelevant for a new build starting now. |
| **New federal National Heat Pump Rebate** | **ANNOUNCED Oct 2026, NOT OPEN.** Reported as $2,000 per eligible household, up to $10,000 for below-median-income households; applications expected **early 2027**, with a possible retroactivity window starting Nov 1, 2026. Multiple installer/industry sources; **official eligibility details (including whether ground-source qualifies and whether new construction qualifies) are unpublished — unverified.** | **Unknown.** Announced framing centres on cold-climate **air-source** heat pumps. Do not count on GSHP eligibility, and note most federal retrofit programs historically exclude **new construction** — this house may not qualify regardless. |
| **Alberta provincial rebate for GSHP** | **None found.** Alberta has no provincial heat-pump/GSHP rebate as of this check. | — |
| **CEIP (Clean Energy Improvement Program)** | **Municipal financing, not a rebate** — upgrades financed on the property tax bill (up to $50,000, up to ~20 yrs, rates vary ~3–6% by municipality), administered by Alberta Municipalities **only in participating municipalities that passed the bylaw**. Status late Oct 2026: Calgary residential intake **closed until winter 2026/27**; Edmonton effectively multi-unit only; many smaller municipalities waitlist-only or closed; a few (e.g., Banff, Medicine Hat) open. | Heat pumps/heating upgrades are an eligible category in many municipal CEIP lists **— but:** eligibility typically targets **existing homes**, a brand-new rural build in a county that may not even run CEIP is a poor bet. **Treat CEIP as $0 for planning; check the specific county/municipality once land is chosen.** |

**Bottom line on incentives: plan on paying for geothermal yourself.** Anything that materializes (2027 federal rebate, a county CEIP) is a bonus, and none of it should drive the design decision for a new build in 2026/27.

### 2.6 Alternatives in one paragraph each

**Cold-climate air-source heat pumps (ccASHP):** Modern units hold rated capacity to about −25 °C and keep working (at reduced capacity and COP ~1.5–2) toward −30 °C, covering all but roughly the coldest ~65 hours/year in Calgary — but Edmonton-design (−30 °C) and rural sites are colder, capacity shortfall lands exactly on the coldest nights, and seasonal COP in Alberta conditions (~1.8–2.5) makes operating cost roughly **double** geothermal's per unit of heat (see table). Installed cost is far lower ($8,000–$16,000 for a typical ducted dual-fuel setup; more at this house's scale — **unverified at 10+ tons**), which is why they dominate retrofits. For a new build of this size with land available, an ASHP-only solution saves capital but gives back much of it in winter bills and still needs full backup.

**Hybrid / dual-fuel (heat pump + gas furnace or boiler):** The pragmatic Alberta default installers actually recommend: a heat pump (air- or ground-source) carries the shoulder seasons and mild winter days at high COP, and a high-efficiency gas furnace/boiler takes over below a switchover temperature and provides backup. If gas is at the parcel, a **gas boiler plant + radiant floors + optional GSHP** is a legitimate architecture — e.g., gas does design-day peaks, pool heating and snow melt (all high-temperature, high-load jobs gas does cheaply), while geothermal or a ccASHP carries base space-heating efficiently. This is also the architecture that de-risks the −40 °C week. The trade-off is two systems to buy and maintain.

### Decisions for Jordan — Geothermal

1. **Gas first:** for any candidate parcel, find out (a) is there a gas line, (b) what does a service extension cost? That answer largely decides geothermal's economics before any heat-pump discussion.
2. **Get a real load number:** commission a CSA F280 heat-loss calc from the working plans — tonnage (10–16 assumed here) sets loop size, unit count and price. Don't accept per-sq-ft guesses on a house with a pool.
3. **Loop choice:** with acreage available, price **horizontal first** (trenched during site excavation), vertical as the comparator. Keep the loop field, septic field and well setbacks non-overlapping on the site plan.
4. **Architecture:** decide between (a) full GSHP + electric aux, (b) GSHP + gas boiler backup (boiler also does pool + snow melt), or (c) gas plant + ccASHP hybrid. On a no-gas parcel, (a) with propane or electric backup.
5. **Budget honestly:** carry **$70,000–$140,000+ (unverified at this scale)** for GSHP, and **$0** for incentives.
6. **Distribution:** commit to low-temperature distribution (radiant floors) in the design — it is what makes GSHP COP, ASHP COP, and boiler condensing efficiency all work.

---

## 3. Heated Driveway + Walkways (Snow Melt) for Alberta

### 3.1 The two systems

| | Hydronic (glycol) | Electric (cable/mat) |
|---|---|---|
| How it works | PEX tubing embedded in the slab circulates heated propylene-glycol solution (typically 30–50% for freeze protection) from a boiler (or water-to-water heat pump) through a heat exchanger; supply ~120–140 °F, 20–30 °F ΔT; tubes ½″–¾″ at 6–9″ spacing, loops kept under ~300–450 ft each to a manifold | Resistance heating cables or pre-made mats embedded in concrete/asphalt/pavers, typically **~50 W/sq ft** installed density, switched in zones by contactors |
| Best at | Large areas, whole driveways, anywhere a boiler already exists; lowest operating cost by a wide margin (gas-fired) | Small, well-defined areas: steps, landings, a walkway, a garage apron, an accessible ramp; no mechanical room equipment |
| Lifespan | Tubing 30–50 years; boiler/pumps are normal HVAC service items | Cable life commonly 20+ years in-slab **(manufacturer-dependent — unverified)**; controls/contactors are the service items |
| Failure mode to respect | A leak or dead boiler = cold slab; glycol concentration must be maintained/tested | A cut cable during later slab work = dead zone; can't repair without opening the slab |
| Installed cost (Canada, 2025/26) | Published Ontario 2026 figures: **$60–$95/sq ft installed**, and $90–$120/sq ft with concrete/interlock finish included. Another contractor average: ~$43.75/sq ft. Treat **$45–$95/sq ft** as the planning band depending on whether slab/finishing is in the number — **Alberta-specific pricing unverified; Ontario numbers used as the Canadian proxy. Always ask whether the quote includes the slab itself.** | Published Ontario 2026 figures: **$20–$60/sq ft installed**; heating components alone often $10–$20/sq ft. Same caveat: confirm whether slab/finish is included. |

Those per-sq-ft numbers are why area discipline matters: a modest 20 ft × 40 ft driveway apron is 800 sq ft — hydronic at $60/sq ft is ~$48,000 before the boiler is even discussed. **Snow melt is priced like a renovation, not like a driveway option.**

### 3.2 Design loads and slab detailing (Alberta)

- **Heat output classes (ASHRAE snow-melting classes):** Class I (residential walks/drives, some snow/ice acceptable briefly) is the residential standard. Published design outputs vary by method/climate: roughly **75–150 BTU/hr·sq ft** in ASHRAE class tables, with cold-climate Class I designs commonly landing **~150–200 BTU/hr·sq ft** once wind and Alberta design snowfall are applied. **Use ~150 BTU/hr·sq ft as the Alberta planning number for Class I, ~200+ for exposed/windy sites — the designer must run the ASHRAE calc for the actual location; treat class table values as unverified until then.** For scale: 1,000 sq ft at 150 BTU/hr·sq ft = **150,000 BTU/hr** — a whole extra mid-size boiler's worth of plant, which is why melt area and boiler sizing are one conversation.
- **Slab detailing that decides whether it works:** tubing/cable 2–3″ below the surface (close enough to respond, deep enough to survive); **insulation under the slab (R-5 minimum in published guidance; R-10 is common practice for melt slabs — unverified as an Alberta standard)** plus **edge insulation** — an uninsulated slab edge and bottom can waste a third or more of the heat to the ground and the outdoors (one design example showed ~61 BTU/sq ft of downward loss with no insulation). Rigid foam under a driveway must be rated for vehicle loads and the slab engineered accordingly.
- **Drainage is part of the system:** melted snow goes somewhere. Slabs must slope to a drain/trench that itself won't freeze, and meltwater must not sheet across an unheated area and refreeze into a skating rink at the bottom of the driveway or across the sidewalk — a classic Alberta liability and the reason aprons and the first metres of walks matter.
- **Controls — where the money is saved or burned:**
  - **Automatic snow/ice sensor (aerial or in-slab) + slab temperature sensor** is the correct control: system wakes on snowfall + cold slab, runs until the surface is dry, shuts off. In-slab sensors respond better than aerial alone.
  - **Manual timer/switch** is cheapest and how systems get left on for three days after a storm.
  - **⚠️ The idle-mode trap:** many hydronic designs offer "idling" — holding the slab at ~32–35 °F all winter so it can respond instantly. On an Alberta winter that can mean the boiler maintaining a warm outdoor slab for **5+ months**, and idle energy can **exceed the actual snow-melting energy**. Insist the designer quote seasonal operating cost **with and without idling**, and default to **off + sensor start** (accepting a slower first melt) or the lowest defensible idle temperature for the steps/walkway zone only.
  - Pre-heating before a forecast storm (some controls accept weather data) improves first-hour performance without all-winter idling.

### 3.3 Operating cost — worked examples (assumptions stated)

**Assumptions:** electricity all-in **$0.22/kWh**; gas all-in **$8/GJ**; boiler efficiency 92%; electric density 50 W/sq ft; hydronic design output 150 BTU/hr·sq ft; a "melt event" = 6 energized hours; ~30 meaningful events/season (Calgary/Edmonton average ~120 cm of snow/year across roughly 40–50 snow days — systems run hours, not days, per event).

| Heated area | Electric: power draw | Electric: cost per 6-hr event | Electric: rough season (30 events) | Hydronic (gas): fuel per hour | Hydronic: rough season |
|---|---|---|---|---|---|
| 200 sq ft (walkway + steps) | 10 kW | ~$13 | ~$400 | ~$0.28/hr → ~$1.70/event | ~$50 fuel |
| 600 sq ft (two tire tracks + apron) | 30 kW | ~$40 | ~$1,200 | ~$0.83/hr → ~$5/event | ~$150 fuel |
| 1,000 sq ft (full small driveway) | 50 kW | ~$66 | ~$2,000 | ~$1.40/hr → ~$8.40/event | ~$250 fuel |

Published seasonal figures for comparison: Ontario installers cite **$120–$250 per winter per 1,000 sq ft** (12–25 ¢/sq ft/season) for typical systems — consistent with the hydronic column above once realistic sensor-controlled runtime is applied, and a reminder that the **electric column is the pessimistic end** because electric systems also get sensor-controlled and rarely run 180 full-power hours. **Both columns are planning arithmetic, not quotes — actual cost lives and dies by controls and runtime.** Note also: a 50 kW electric driveway is a **major electrical service load** — on a rural service that also runs a well pump, GSHP and a pool plant, service size becomes a real design constraint and a real cost.

### 3.4 Where it makes sense for THIS house

The design has: a **long front porch** with centre steps, **multiple porch stairs** (front, breakfast porch, outdoor living, side porch), a **garage**, and (rural Alberta) likely a **long driveway**.

| Zone | Recommendation | Why |
|---|---|---|
| Porch steps + landings (all porches used in winter) | **Yes — highest value per sq ft.** Electric mats/cable are ideal at this scale, or a hydronic zone if a boiler plant exists | Steps are where people fall. Small area = small install and operating cost. Ice on shaded porch steps persists for weeks in Alberta. |
| Main walkway (driveway → front steps) | **Yes** | Short, defined path; guests and deliveries use it. |
| Garage apron (first 10–20 ft out of the garage) + area in front of garage doors | **Yes — hydronic if any hydronic exists** | Stops the ice dam of compacted, refrozen slush exactly where vehicles and people transition; also protects the slab/door seals from freeze-thaw and salt tracking. |
| Driveway tire tracks (two 18–24″ strips) | **Maybe — the value option if the driveway is heated at all** | Cuts heated area ~60–70% vs. full width while keeping vehicles mobile; does nothing for people walking the driveway. |
| Full driveway | **Generally no** — especially a long rural driveway | Cost scales brutally ($45–$95/sq ft hydronic; a 150 ft rural drive is 3,000+ sq ft). Snow on a flat rural drive is a plow/blower problem, not a melt problem. Exceptions: steep grade, mobility needs, or a short courtyard-style drive. |
| Around the house / pool exits / hot-tub path | **Yes for the hot-tub route** if the tub sits outside the pool room — a short heated path is a genuine quality-of-life item in January. **Unverified scope — depends on final plan.** | Barefoot + January + ice is a bad combination. |
| Roof / ice dams | Snow melt in slabs does **nothing** for roof ice dams. Ice damming on this design (multiple hips/valleys, porch roofs at 4:12 tying into walls) is handled by roof/attic detailing: continuous air barrier, generous attic insulation and ventilation (or a conditioned "hot roof"), ice-and-water shield membrane at eaves/valleys, and heat cable only as a spot remedy | The 4:12 porch roofs against taller walls are the classic Alberta ice-dam/snow-drift detail — flag it to the designer now, while the roof is still lines in SCAD. |

**Freeze/thaw note:** a properly run melt system *reduces* freeze-thaw cycling and salt damage on the slabs it covers. The damage concentrates at the **boundaries** — the unheated slab next to the heated one, and where meltwater refreezes. Detail transitions and drainage, not just the heated zones.

### 3.5 Code / permit / insurance notes (Alberta)

- **Electrical:** electric snow-melt is a large fixed heating load — CSA C22.1 (Canadian Electrical Code, as adopted in Alberta) rules for heating cables/systems apply, GFCI/equipment protection requirements apply to outdoor heating cable circuits, and the installation needs an **electrical permit and inspection**; the service-size calculation must include it. **Specific code sections not verified in this pass — the electrician confirms.**
- **Hydronic:** a gas boiler installation requires a **gas permit** and must meet Alberta gas code (CSA B149.1 as adopted); boiler may also trigger plumbing/mechanical permits through the county/municipality or an accredited agency. Glycol systems need backflow protection between the glycol loop and any potable connection.
- **Building/development permits:** slabs and driveways themselves are usually part of the main building permit/site grading plan in rural counties — confirm with the county; meltwater drainage may not be directed onto neighbouring land or the road allowance.
- **Insurance:** tell the insurer the systems exist. Heated steps/walkways generally *reduce* slip-and-fall liability exposure; an undocumented boiler or a large electrical load added without permit is the kind of thing that complicates a claim. **No Alberta-specific insurer guidance verified in this pass.**
- **Safety:** never use a melt system as a reason to skip drainage design — a melted-but-undrained slab in a cold snap becomes black ice, which insurers and visitors both dislike more than snow.

### Decisions for Jordan — Snow Melt

1. **Default scope:** steps + landings + main walk + garage apron. Price tire tracks as an option; price full driveway only if the final driveway is short.
2. **System choice follows the heating plant:** if the house gets a gas boiler (backup/pool/melt plant), snow melt is **hydronic** on that boiler. If the house is all-electric/GSHP with no boiler, keep melt **electric and small** (steps/walks only) — do not add a boiler just for a driveway.
3. **Controls in writing:** snow sensor + slab sensor, **no all-winter idling** (or an idle cost figure quoted and accepted explicitly).
4. **Slab spec in writing:** under-slab + edge insulation, tube/cable depth, drainage path for meltwater, and where the meltwater freezes (it must not be on a walking/driving surface).
5. **Electrical planning:** if any electric melt is included, put its kW in the service-size calculation on day one.
6. **Roof flag for the SCAD/design phase:** porch roofs at 4:12 against walls = ice-dam/drift detailing conversation with the designer, independent of slab melt.

---

## Sources

**Wells — Alberta rules and owner guidance**
- Alberta Working Well, Issue 8 — Well Owner Responsibilities (household-use definition 1,250 m³/yr, testing frequency, casing height, owner duties): https://open.alberta.ca/dataset/09b71647-f9f5-45e0-9fa5-36276471f4fc/resource/d1939cdf-5a15-4b03-bb3b-478cc07b75da/download/issue8-wellownerresponsibilities-mar2017.pdf
- Alberta Water Well Drilling Association, Issue 9 — Drilling a New Well (licensed contractor / Approval to Drill, construction standards, driller cannot guarantee quantity/quality, AWWID): https://awwda.ca/uploads/PDFs/FactSheets/2019/Drilling_A_New_Well_2019.pdf
- Alberta Environment, Water Wells and Ground Source Heat Exchange Systems Directive (approval classes, journeyman requirements; dated Dec 2018 — confirm currency): https://open.alberta.ca/dataset/5bc817ba-3d6d-45cd-a403-2e727abe665e/resource/508b38c0-0ca7-4fbe-8a90-cfeb5139e122/download/directivewaterwellsgroundsourceheatexchange-dec11-2018.pdf
- Owen's Drilling (Crowsnest Pass) — Alberta Water Act summary, household exemption, bedrock conditions: https://www.owensdrilling.com/area/expert-well-drilling-in-crowsnest-pass-ab/

**Wells — costs, quality, treatment**
- My Acreage — Buying Bare Land in Alberta (well $15,000–$35,000 installed; $80–$200/m; septic ranges): https://www.myacreage.ca/blog/buying-bare-land-alberta-build-acreage.html
- New Homes Alberta — lot selection guide (well drilling $15–$30/ft, 100–300 ft depths): https://newhomesalberta.ca/how-to-choose-lot-for-new-home-alberta/
- Alberta.ca — Testing farm drinking water (Level C diagnostic suite ~$400, parameter lists): https://alberta.ca/testing-farm-drinking-water
- Alberta Environment — Focus on Groundwater (hardness/iron by aquifer type; confined aquifers softer, higher TDS): https://open.alberta.ca/dataset/fdedd210-7599-494c-b89e-7e3eb1a5d5bb/resource/bd21e14f-749a-4a9e-b9fc-340226bdce89/download/aenv-focus-on-groundwater-2005-08.pdf
- Alberta Agriculture — Understanding Groundwater (shallow = hard/high iron; deep = sodium/soft, ion exchange): https://studyres.com/doc/20325450/understanding-groundwater---alberta-agriculture-and-forestry
- Domestic well water quality in Alberta 2002–2008 (provincial survey): https://open.alberta.ca/dataset/2fd238f2-abb2-4bcd-8e85-4c8bbd965395/resource/1259e8b1-a4de-4148-8ac0-ba156d45e260/download/6657752-domestic-well-water-quality-alberta-2001-2008.pdf
- WaterFilterHelp.ca (Canadian installed costs: softeners $1,200–$3,500; RO $400–$1,500; well combos $2,500–$5,500): https://waterfilterhelp.ca/
- HomeStars Canada — water softener replacement cost guide 2026 (lab analysis $100–$150; RO $500–$1,500): https://www.homestars.com/plumbing/price-guides/cost-to-replace-water-softener
- Foothills County well guide (30 m septic setback checklist; casing/cap/grading checks): https://albertatownandcountry.com/well-water-guide-foothills-county.html
- Alberta Safety Tips — Private Sewage Treatment Systems separation distances (15 m from water source): https://open.alberta.ca/dataset/b8c07f17-395d-4580-8a7f-45b395bc5b2d/resource/616e6f01-a2f1-4224-9ab0-88ffbc46aa20/download/2012-safety-tips-private-sewage-treatment-systems-separation-distances-september-2012.pdf

**Geothermal, rates, incentives**
- Alpine GeoThermal (Calgary) — Alberta GSHP cost $25,000–$45,000, ~10 °C ground, 7–12 yr typical payback, loop/unit life: https://www.alpinegeothermal.com
- Greenfoot Energy (Canada) — GSHP $20,000–$40,000; horizontal vs. vertical ranges; 150–250 ft bore per ton: https://www.greenfootenergy.ca/services/geothermal-heat-pumps
- Builders Ontario — geothermal cost 2026 (horizontal $25–40k, vertical $35–55k, large installs $80k+; Greener Homes closed): https://buildersontario.com/how-much-does-a-geothermal-system-cost-in-2025/
- Umny Inc. case study — Alberta ground-temperature/oversizing, $20/ft drilling illustration: http://umny.ca/case-study-ground-temp/
- Alberta Indoor Comfort — Calgary heat pump costs & rebates 2026 (Greener Homes Grant/Loan closed; CEIP closed until winter 2026/27; dual-fuel guidance): https://albertaindoorcomfort.com/articles/heat-pump-installation-calgary-ceip-rebate/
- Solenery — Greener Homes closure + National Heat Pump Rebate announcement (early 2027 applications, retroactivity from Nov 1, 2026): https://solenery.com/blog/greener-homes-grant-update/ and https://solenery.com/greener-homes-replacement/
- Home Energy Canada — program tracker (Loan closed Oct 1, 2025; Grant final deadline Dec 31, 2025): https://www.homeenergycanada.ca/
- Xolar — Alberta CEIP status by municipality (checked Oct 26, 2026): https://xolar.ca/rebates/
- Solution 105 — Alberta residential energy rates Nov 2025 (electricity forwards ~6 ¢/kWh; gas forwards ~$3.20/GJ): https://solution105.com/blog/residential-energy-rates-in-alberta-what-to-do-november-2025/
- The Energy Exchange Market — Alberta RoLR 12.01–12.06 ¢/kWh (2025–2026) and gas default-rate ranges: https://www.theenergyexchangemarket.com/blog/canada-alberta-ontario-energy-shopping-guide.html
- EcoSolar — Alberta design temperatures (Edmonton −30 °C, Calgary −26 °C) and cold-climate ASHP behaviour: https://www.ecosolar.ca/CCHP_2026.pdf

**Snow melt**
- Action Home Services (Ontario, 2026) — electric $20–$60/sq ft, hydronic $60–$95/sq ft installed; seasonal operating 12–25 ¢/sq ft: https://actionhomeservices.ca/are-heated-driveways-worth-it/
- Floor Heating Systems Inc. (Toronto, 2026) — 50 W/sq ft worked operating-cost arithmetic: https://www.floorheatingsystemsinc.com/driveway-heating-cost-breakdown/
- WarmlyYours Canada — snow-melting cost examples (50 W/sq ft basis): https://www.warmlyyours.com/en-CA/snow-melting/mat/omnimat/WHMA-120-0205-4/support
- H2X Engineering — hydronic snow melt sizing (ASHRAE classes; Class I 150–200 BTU/hr·sq ft cold climates; tube spacing/supply temps): https://www.h2xengineering.com/blogs/hydronic-snow-melt-systems-sizing-guide/
- Plastic Pipe Institute / ConduitCalc — Design & Installation of Hydronic Snow & Ice Melting Systems (150 BTU/hr·sq ft example; insulation pick-up loss allowance): https://conduitcalc.plasticpipe.org/pdf/designing-hydronic-snow.pdf
- EZ Virtual Tools — ASHRAE snow-melt classes and R-5 minimum under-slab insulation guidance: https://hvac.ezvirtualtools.com/calc/snow-melt.html

*Prepared 2026-10-28. Verify all program statuses and prices again once land is purchased — incentives in particular have changed three times in three years.*

---

# Consolidated decision list

Work through these roughly in order — the land decisions (B) gate several
of the design ones. Detail and reasoning are in the part noted.

## A. Layout (Part 1)

1. **Basement stair: A, B or C?** A = U-stair in the former bar (model
   default, recommended by both reviews). B = basement extends west under
   Bedroom 3/garage, theater and pool shift. C = sketch's stair kept,
   office moves. [Part 1 §1.3]
2. **One interior stair, or design in a second?** The rebuild has one
   (plus the exterior exit stair). [Part 1 §1.3]
3. **Add a basement bathroom (WC + shower/change) by the pool** — and its
   rough-in — yes/no before the foundation design starts. [Part 1 §1.3]
4. **Basement outline:** fit the foundation to the house, or accept ~20%
   of the basement outside the walls with structural slabs over it.
   [Part 1 §3]
5. **Theater package:** sound/vibration isolation for the theater ceiling
   (laundry/pantry/nook above) — cheap at framing, miserable later.
   [Part 1 §1.3, Part 2 §3]
6. **Exit stair vs side porch:** porch floor opening over the areaway, or
   move the stair. [Part 1 §1.3]
7. **Ask the architect:** is the garage-corner stair actually an attic
   stair? And confirm side-load garage doors (the plan image cuts the
   west wall off). [Repo REVIEW.md §2/§5]

## B. Land-dependent (decide per parcel, before design freezes)

8. **Gas service:** is there a line, and what does extension cost? This
   largely decides geothermal's economics. [Part 3 §2]
9. **Well prospects:** pull AWWID records near any candidate parcel;
   budget changes a lot between 8 gpm bedrock and 25 gpm gravel country.
   [Part 3 §1]
10. **Climate zone:** design to 7B numbers now and the envelope is safe
    anywhere in Alberta; confirm the tier once land is chosen.
    [Part 2 §3]
11. **Geotechnical report** before footing design (bearing + sulphates).
    [Part 2 §1]

## C. Foundation & envelope (Part 2)

12. **ICF core: 8 in** below grade (SCAD shell becomes ~13.25 in), brand
    by dealer/crew — shortlist Nudura vs Logix once the region is known.
13. **Waterproofing in writing:** membrane + dimple board + weeping tile
    to sump, explicitly in the quote scope.
14. **ICF above grade?** Basement-only is the value pick for this plan.
15. **Wall assembly:** 2×6 + 2–3 in exterior mineral wool (~R-30
    effective) as the default; skip 2×8.
16. **Windows:** house spec triple-pane, warm-edge, argon, U ≤ 1.0,
    ER ≥ 34, SHGC tuned per elevation; get fiberglass vs vinyl quotes on
    the same elevations before choosing frames; casement/awning/fixed as
    the default palette.
17. **Pool room = natatorium spec** (sealed vapour barrier, glass-mat /
    cement board only, no exposed galvanized metal, dedicated
    dehumidification, pool cover) as a design input now — the pool-room
    ceiling is the main floor's structure.
18. **Roof package:** raised-heel trusses; freeze roof geometry early —
    it's the long-lead order. (Roof *product* stays parked until land,
    per the earlier call; blue colour is in the model.)
19. **Before-the-pour checklist:** basement bathroom rough-in (#3), pool
    plumbing runs, floor drains, radon rough-in, well/septic/service
    entries, exit areaway (#6).

## D. Site systems (Part 3)

20. **Well contract:** written dry-hole / low-yield terms before drilling;
    site plan fixes well ≥30 m from septic, well uphill, non-overlapping
    with the geothermal field; target 12–18 gpm sustained, else
    cistern + booster; treatment ($5–12K) bought only after the finished
    well's water test.
21. **Heating plant architecture:** (a) GSHP + electric aux, (b) GSHP +
    gas boiler (boiler also serves pool + snow melt), or (c) gas plant +
    cold-climate ASHP hybrid. Needs a CSA F280 heat-loss calc from the
    working plans — no per-sq-ft guesses on a house with a pool. Carry
    GSHP at $70–140K+ (unverified at this scale), incentives $0.
22. **Distribution:** commit to low-temperature delivery (radiant floors)
    — it makes every plant option above efficient.
23. **Snow melt scope:** steps + landings + main walk + garage apron by
    default; tire tracks priced as an option; full driveway only if the
    final drive is short. Hydronic if there's a boiler (#21b), else
    electric and small. Controls (snow + slab sensors, **no all-winter
    idling**) and meltwater drainage written into the spec.

---

*Parts 1–3 above this list are the working detail. When decisions are
made, the SCAD changes that follow from them (stair option, basement
bathroom, ICF wall thickness, wall assembly thickness) are a single
editing session in `nuniesmith/house` — the tables make them small,
mechanical edits, and `tools/check_layout.py` re-checks the layout
afterwards.*
