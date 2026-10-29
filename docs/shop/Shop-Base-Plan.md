# Shop — Base Plan (100 × 100 ft, 4 bays, utility hub + tunnel to house)

Compiled 2026-10-29 for Jordan. Companion to *House-Review-and-Research-2026-10-28.md*.
Planning only — not construction documents. Land is not yet secured, so every
position below is **relative** (to the house), not a surveyed site plan.
Diagrams: `site-plan.png`, `shop-floor-plan.png`,
`tunnel-section.png`. SCAD: `shop.scad` and `site.scad` in
the house repo model this plan.

**Revision v3 (2026-10-29, Jordan's redirect — supersedes v2):** the
shop moves **behind the house, to the north side**, rotated 90° right
from v2: the front (overhead doors) faces **west** again, the bays run
**east–west**, and Bay 1 (utilities) is the **southernmost** bay,
closest to the house. A **shared driveway runs up the west side** of
house and shop (past the garage's west doors) to the shop's west
apron; a **loop driveway with a garden island** sits in front (south)
of the house; and **trees belt the shop on its north, east and south
edges** (the west edge is the working front). The tunnel now runs due
**south** from Bay 1's south side into the basement UTILITIES room
**through its north foundation wall** — UTILITIES is on the north
side of the basement, so v3 gives the tunnel the direct landing v2
couldn't: **no basement room is touched at all**, and v2's theater
receiving-room proposal is dead. §5 and §6 carry the details.

**The concept, in Jordan's words:** the shop is the property's utility hub.
Power, water, gas, internet and heat originate in the shop's utility bay,
cross to the house in a heated, walkable tunnel with the services under floor
grates, and land in a basement utility room. The house itself carries the
bare minimum — a 200 A panel fed from the shop. House first, shop second:
a small temporary service shed carries the house until the shop is ready,
then the service moves. Any future house on the property is fed from the
shop the same way.

---

## 0. Assumptions I had to make (change any of these and the plan moves)

| # | Assumption | Why |
|---|---|---|
| A1 | Shop sits **behind (north of) the house**: south wall at house-frame y = 130, west wall aligned with the garage's west wall (x = 0), so the shop occupies x 0–100, y 130–230 | Jordan v3. Leaves ~62 ft of back yard between the house's north porches and the shop |
| A2 | The tunnel runs on house-frame **x = 80**, the centreline of both the basement UTILITIES room (x 60.1–100.1) and Bay 1's portal room (shop-local x 72–88) | One straight north–south line: Bay 1 → tunnel → UTILITIES north wall. Tunnel length ~70 ft |
| A3 | Bays run **east–west** (100 ft deep), doors on the **west** wall, each bay 25 ft wide, stacking south → north: utilities, work, work + pit, wash (v3, Jordan) | Bay 1 southernmost = shortest tunnel and shortest runs to the house |
| A4 | The tunnel lands **directly in the UTILITIES room** through its north foundation wall (§5) | UTILITIES' north wall IS foundation — v3 needs no new basement room and touches no other room |
| A5 | The drilled well itself is **outside** the shop (east side); what lives in Bay 1 is the well *equipment*. Septic tank/field go west/north-west, as far from the well as the layout allows | §4.3, §7 — wellheads inside buildings are a contamination/access problem; ≥ 30 m well-to-septic separation |
| A6 | **Gas does not run inside the tunnel** by default; it goes direct-buried alongside it | §6.3 — gas in an enclosed occupied tunnel is the one part of the concept an inspector is likely to refuse as drawn |
| A7 | Shop boiler (from your 2026-10-28 note) lives in Bay 1 and is the heat hub for shop slab, tunnel, house hydronics and snow melt | Ties this plan to the earlier research instead of duplicating plant in the house |
| A8 | **Trees on the shop's north, east and south edges** (rows ~14 ft off the walls; a gap in the south row at the tunnel) | Jordan v3 — shelter/screening. Keep the south row's shade and roots in mind: gap at the tunnel, and don't plant over the septic/well lines |

---

## 1. Site base

Coordinates below reuse the house model's frame (feet; x = east, y = north;
garage west wall x = 0, house front wall y = 0, front porch to the south).

- **Shop:** x 0–100, y 130–230 (behind the house). Front (all overhead
  doors) faces **west** onto a **70 ft deep truck apron** (x −72–0).
- **Shared driveway (west side):** one drive runs the whole west side —
  from the front loop (below) north past the garage's west doors and
  the house's west side, widening into the shop apron. Cars and trucks
  share it; the apron is the truck working area.
- **Front loop + garden (south of the house):** a loop driveway in
  front of the front porch (ring roughly x 25–130, y −72…−14) with a
  **garden island in its middle**, connected to the west drive at its
  south-west corner. This is the house's public face — keep truck
  traffic on the west drive/apron, not on the loop.
- **Tree belt:** rows along the shop's **north, east and south edges**
  (~14 ft off the walls), with a gap in the south row where the tunnel
  passes. The south row sits between shop and back yard — it screens
  the shop from the house's north porches; pick species/height with
  that and winter shade in mind.
- **Well zone:** east side, around (140, 110) — east of the shop's
  south-east corner. Line runs west, underground, into Bay 1's water
  room (toward its east end). Keeps the well on the opposite side of
  the property from the septic.
- **Septic zone:** tank north-west of the apron (around (−89, 212)),
  treatment field further west (x −165…−105, y 150–205) — as far from
  the well as the layout allows (plan on the ≥ 30 m / ~100 ft
  well-to-septic separation from the well research; final distances
  are the septic designer's, after a soil test).
- **Reserved corridors:** services corridors north and east from Bay 1
  for future houses (§9). Keep buildings, the septic field, the well
  and the tree rows out of both.
- **Grading:** shop slab at grade for truck entry. The house basement
  floor is ~11 ft below grade, so the tunnel is a deep structure its
  whole length and arrives *under* the shop — see §6.2 for the shop-end
  stair. Surface drainage must fall away from both buildings and must
  not pond over the tunnel — and the south tree row must not dam the
  back yard's drainage.

## 2. The shop building — base spec

- **Structure:** 100 × 100 ft, **20 ft eave** proposed. 14 ft doors plus
  truck stacks, lifts and door operators don't fit honestly in less;
  a clear-span steel building is the default at this size (wood post-frame
  is the budget alternative — decide with quotes, not by default).
- **Foundation/slab (engineer final, Alberta frost):** engineered
  slab-on-grade on a compacted, geotech-confirmed pad — thickened edge /
  grade beam taken below frost or a frost-protected shallow foundation
  with insulation wings. **8 in reinforced slab in Bays 2–4** (truck axle
  loads, pit and lift anchors), **6 in in Bay 1**. Wash-bay slab sloped
  to its trench drain; truck bays essentially flat with drainage to the
  separator, never to the septic.
- **Heat:** in-slab hydronic, **one zone per bay**, fed from the Bay 1
  boiler (§4.4). Tubing is a before-the-pour decision.
- **Before-the-pour embeds (shop):** pit excavation and walls (§3, Bay 3),
  wash-bay trench drain + separator line, Bay 1 floor drains, every
  conduit sleeve in/out of Bay 1 (service entrance, well line, septic/
  bathroom drains, solar/future sleeves), lift anchor zones kept clear
  of hydronic loops. The tunnel portal is *below* the slab on Bay 1's
  **south side** (§6.2) — its opening is in the shop's foundation, not
  a pour embed in the slab itself.
- **Doors:** Bays 2–4: **14 ft wide × 14 ft high** insulated overhead,
  on the **west** wall. Bay 1: 10 ft wide × 12 ft overhead + a man door
  (equipment in/out, no trucks), also west. Man door on the south side
  (back-yard side) for daily use on foot between house and shop.
- **Fire/life safety flags for the designer:** fuel, welding, a pit,
  batteries and a generator in one building drive separations, ventilation
  and possibly sprinkling. The generator and battery rooms below are
  planned as separated rooms from day one because retrofitting that is
  miserable.

## 3. Bay by bay (south → north)

### Bay 1 — Utilities (25 × 100 ft, southernmost) — §4 has the detail
The hub. Subdivided west → east: **1A generator room (west end, at
the apron) → 1B electrical + batteries → 1D network/server +
bathroom → 1C water + heat → 1E tunnel portal, stair and manifold
room (near the east end, tunnel leaving its south side on the x = 80
line) → future/expansion room at the east end**. Everything the house
(and later, other houses) needs is generated, stored or terminated
here; services gather at 1E and drop to the tunnel. The portal sits
beside the water/heat room and one room from electrical — short runs
either way.

### Bay 2 — Truck work (25 × 100 ft)
General work bay. 14 × 14 door on the west wall, open floor for a
2-post or mobile-column lift, benches/tool storage on the **east
(back) wall**, welder and air compressor at the east wall with drops
down the bay. Keep the middle of the floor empty — a 100 ft deep bay
is for a truck + trailer *inside*, which only works if nothing creeps
into the lane.

### Bay 3 — Truck work + pit (25 × 100 ft)
Second work bay with the **pit**: proposed **40 ft long × ~4 ft wide ×
~5.5 ft deep**, running east–west (the bay's direction), centred in
the bay, roughly mid-length. Non-negotiables to design in, not add later:
- **Drive-over rated covers** (flush, axle-rated) so the bay still works
  with the pit closed.
- Stair access (both ends if space allows), ventilation sized for
  heavier-than-air vapours, pit lighting/electrical placed and rated
  for a pit, drainage to the **separator** (not septic, not dry well).
- No benches, lifts or storage over/around the pit zone.
A pit is the most regulated single item in the building — raise it with
the designer/insurer early. (The honest alternative is a second lift bay;
your call, the plan keeps the pit as asked.)

### Bay 4 — Wash bay (25 × 100 ft, northernmost)
14 × 14 door on the west wall, slab sloped to a **centre trench drain**
(running east–west), hose reels and pressure-washer plant (hot-water
unit) in a small equipment zone at the east end. Drainage: trench →
**oil/grit separator → holding tank**,
pumped out as waste. **Wash water never goes to the septic system or the
field** — detergents, oil and volume would kill it, and it's the standard
Alberta rule for vehicle wash water. Water reclaim/recycle is an optional
later add; rough in the space, not the plant.

## 4. Bay 1 — the utility hub in detail

### 4.1 Electrical (1B, ~24 ft of the bay)
- **Service:** the property's only utility service terminates here once
  the shop is live. Design the main switchboard around a **1,000 A bus**
  with the initial service as large as the utility will reasonably give
  — rural Alberta services are often capped well below that in single
  phase, so **talk to the utility before the design is final** (three-
  phase availability changes everything, including generator and
  inverter choices).
- **Distribution (each its own feeder, breaker and conduit from day one):**
  house 200 A (through the tunnel), shop's own panel(s) ~200 A,
  future-house feeder positions (empty breaker spaces + capped conduits
  in the reserved corridors), solar inverter input, generator input,
  battery inverter/charger.
- **Load reality check:** 200 A panels are *capacity*, not draw. With
  load management (EV/truck charging, wash plant, welders staggered),
  the site does not need a service equal to the sum of its panels.
  Say so to the utility exactly that way when sizing.
- **Batteries/inverters:** rack-mounted **LFP** in 1B with code working
  clearances, vehicle bollards, and the room's separation/ventilation
  designed for energy storage from the start. Sized to *grow* — leave
  the second half of the rack row empty floor, with busway/conduit
  already run. Solar arrives as ground-mount south/west of the shop
  later (roof-mount on a 100 ft shop is also possible; ground-mount is
  easier to service and expand, and doesn't load the roof with Alberta
  snow math).
- **Generator (1A, west end of Bay 1):** its own fire-separated room
  with combustion-air louvres and exhaust direct to outside through
  the west wall — the west end is deliberate: shortest air/exhaust
  path onto the apron, fuel delivery from the apron, and the room sits
  at the opposite end of the bay from the bathroom/network rooms. Diesel vs natural gas follows the same
  parcel question as the house heat (gas line or not); diesel with an
  on-site tank is the no-gas-line default and doubles as truck fuel
  infrastructure. Rough size class for house + critical shop + pumps
  is **50–80 kW** — a real load study sets the number, this is a
  placeholder class, not a spec.
- The generator backs up, at minimum: house panel critical loads, the
  house sewage lift station, well pumps, tunnel heat, Bay 1 itself.
  Sewage and water are why "the house can lose power" is not an option
  in this design — both depend on the shop.

### 4.2 Network / server (1D, shared with bathroom zone)
Small, separately cooled room in 1D: fibre termination (the property's
internet lands in the shop first), core switch/router, server/NAS rack,
security/camera recorder, and the tunnel/house monitoring (freeze
alarms, lift-station alarm, generator status). Two fibre conduits shop →
house (one lit, one spare/dark). House gets a small termination panel in
its utility room — no servers in the house.

### 4.3 Water (1C, ~14 ft of the bay)
- Well drilled **outside, east of the shop** (A5); line enters Bay 1
  underground from the east and runs to 1C. In 1C: pressure tanks, treatment train (decided by the
  water test on the finished well — iron/sediment/softener/UV as needed,
  per the well research), manifold with a valved outlet per consumer:
  house (through tunnel), shop/bathroom, wash bay (separate, with
  backflow protection — wash water must never be able to reach the
  potable side), yard hydrants, future houses.
- Space to grow: room for a cistern if the well comes in weak (the
  research's 12–18 gpm target; a cistern + booster is the fix if it
  doesn't), and a second pressure tank.
- Everything water in the tunnel is insulated **and** heat-traced as
  backup, even though the tunnel is heated — the trace is for the one
  week the heater fails in January.

### 4.4 Heat (1C, with the water plant)
Shop boiler hub (your snow-melt boiler idea, extended): one plant room
feeding — shop in-slab zones, the tunnel unit heater(s), house hydronic
supply/return through the tunnel (house radiant/heat, domestic hot
water via exchanger, and the basement pool's heat exchanger — the pool
is a year-round load and belongs on this plant, not on a house
appliance), and the snow-melt loops (shop apron edges/garage apron/
walkways — sized and zoned per the earlier research, no all-winter
idling). Fuel = the parcel gas question again; the plant room is laid
out so a second boiler or a future ground-source unit fits beside
the first.

### 4.5 Bathroom (1D, mid-bay with the network room)
Simple and complete: WC, sink, **shower** (a shop you can wash in
before going to the house is the point), floor drain, water heater
fed from 1C next door. Drains **by gravity west along Bay 1, then
north to the shop septic tank** (shop slab is at grade, tank is
below grade — gravity works here, unlike the house run, §7). Hot
water and the room itself are on the shop slab heat zone.

## 5. The house end — straight into UTILITIES (v3's big win)

**The geometry (checked against the current house model,
`nuniesmith/house` @ a88cf06):** the basement's UTILITIES room sits on
the **north side** of the basement (basement coords (30,45)–(70,60),
under the nook/kitchen area), and **its north wall is foundation
wall**. With the shop now behind the house, the tunnel runs due
south on x = 80 and **enters UTILITIES directly through that north
foundation wall** — no new basement room, no bulkhead, nothing carved
out of anything. (This kills both earlier workarounds: v1's extension
under the mud room/garage and v2's receiving room in the theater.
The theater keeps its full 30 ft.)

In UTILITIES, exactly as the room was always meant to work:
- the tunnel's fire-rated door on its north wall;
- the house's 200 A panel (fed from the shop; the house's *only*
  panel besides sub-panels) and transfer/protection gear;
- the **duplex grinder lift station** for all house sewage (§7);
- water entry + house manifold, hydronic entry + exchangers;
- fibre termination + small network panel;
- sump and floor drain.
UTILITIES is 40 × 15 ft — big enough for the house's minimal kit
because the shop carries all the plant. The one design note: the
tunnel penetration and its fire-rated door go in **with the basement
ICF pour** — formed, sleeved and waterproofed as foundation work,
not cored later.

## 6. The tunnel (utilidor)

### 6.1 Route and size
Straight, Bay 1's portal room (on its **south side**) → due south →
the UTILITIES room's **north foundation wall**, on house-frame
x = 80, the centreline of both rooms. From Bay 1's south wall
(y = 130) to the basement wall (y = 60) the run is **~70 ft** — the
shortest of the three layouts (v1 ~100 ft, v2 ~130 ft). **Proposed section:
~8 ft wide × 7.5 ft clear inside** — a real walkway (4 ft clear) plus
a service trench zone under **removable floor grates**, per your
spec. Grate sections sized to lift by hand (< ~40 lb each). Precast
concrete box sections are the default construction (fast, known cost
per foot, watertight joints available); cast-in-place is the
fallback.

### 6.2 The level problem (read this one)
The tunnel floor sits at **house basement level — about 11 ft below
the shop slab**. At the house end that's perfect (it walks straight
into the UTILITIES room through its north wall, §5). At the
shop end it arrives *under* Bay 1: **1E is a stair room** — services
rise up the manifold wall to grade-level distribution, and you reach
the tunnel down a full flight of stairs (~19 risers) inside 1E. No
way around it; a ramp would eat half the bay. The tunnel roof is
~3–4 ft below grade — deep enough for frost and for the back yard
(and the south tree row's gap) to pass over it.

### 6.3 What runs in it — and the one thing that doesn't
| Service | In tunnel? | How |
|---|---|---|
| Power — 200 A house feeder + spare conduit | Yes | Own trench compartment, in conduit |
| Fibre ×2 + copper spare | Yes | Own conduit, separated from power |
| Potable water | Yes | Insulated + heat trace; in the trench's wet compartment, **above** sewer level, never shared with it |
| Hydronic supply/return (heat, DHW, pool) | Yes | Insulated pair; wall-rack is an option if trench space gets tight |
| Sewage forcemain (house → shop) | Yes | Own compartment, leak-checked, cleanouts both ends |
| **Gas** | **No (default)** | **Direct-buried outside the tunnel**, entering the house UTILITIES room through its own sleeve in the north foundation wall. Gas inside an enclosed, occupied, below-grade tunnel is an explosion-path problem; the only acceptable in-tunnel version is a sealed steel pipe in a separately vented compartment with gas detection — and only if the gas inspector (AHJ) approves it in advance. My recommendation: don't fight this one; the buried line costs less than the argument |
| Spare conduits ×2 | Yes | Capped, labelled, pull strings in — future you says thanks |

### 6.4 Environment and safety
- **Heat: 60–66 °F (15.5–19 °C) as you specified** — warmer than most
  utilidors run, but at ~800 sq ft of tunnel it's a small load on the
  shop boiler, it makes the tunnel genuinely usable, and it gives the
  water lines a wide freeze margin. Electric unit heater (generator-
  backed) as the backup source, thermostat + **low-temperature alarm
  to your phone** either way.
- Insulated + waterproofed shell (membrane and protection board, like
  the house ICF waterproofing stack), perimeter drainage to a sump at
  the low end — a tunnel that floods is a tunnel full of services.
- LED lighting on motion, small exhaust fan for humidity (a sewer
  forcemain lives here), **fire-rated doors at both ends** — connecting
  two buildings with a tunnel makes the code treat them as connected,
  so raise fire separation, egress and insurance with the designer/AHJ
  **before** the design is final, not at permit time.
- **Cost honesty:** a heated walkable utilidor is the expensive version
  of this idea — at Alberta prices, budget *in the order of* $110K–
  $220K for ~70 ft installed, deep, serviced and finished
  *(rough planning range, unverified — get precast quotes early)*.
  A direct-buried bundle + access vaults does the same job for a
  fraction of that, minus walk-in access. Your concept is the walkable
  one and this plan follows it — just go in with eyes open, and note
  decision D1 below: **every foot of house–shop gap you remove is
  roughly a foot of tunnel you don't buy.**

### 6.5 Build timing — do the tunnel with the house
Excavation and concrete crews are already mobilised for the house
basement (§5). **Build the full tunnel (or at minimum the house-end
half, capped at a bulkhead) during the house build**,
while the trench is cheap to open. Digging it later, under a finished
back yard, is the expensive way to own the same tunnel.

## 7. Septic — house pumps to the shop, shop drains by gravity

- **Tank + field:** at the shop, north-west zone (§1), sized and sited
  by the septic designer after soil testing (house is ~5 bedrooms plus
  a shop bathroom — don't guess the size here).
- **House → tank:** all house sewage collects to the **duplex grinder
  lift station** in UTILITIES (§5)
  (duplex = a pump can fail without an emergency; high-level alarm to
  the phone; on the generator-backed panel because it must never be
  without power). Forcemain runs north through the tunnel (§6.3),
  rises into Bay 1, runs west inside the shop and out to the tank.
  Lift is ~8–10 ft plus ~70 ft of friction — routine for grinder pumps.
- **Shop bathroom → tank:** gravity — west along Bay 1, then north
  past the apron to the tank (§4.5).
- **Wash bay → NOT the tank:** separator + holding (§3, Bay 4). Pool
  backwash/drain water also stays out of the septic (volume + chlorine)
  — it needs its own discharge arrangement in the house mechanical
  design; flagged, not solved here.

## 8. Build order — house first, shed in between, shop second

1. **Land + tests:** geotech, well test hole/AWWID records, septic
   soil test — these pick the well and field zones for real.
2. **House build**, including: the UTILITIES room's fit-out (§5 —
   200 A panel, lift station, manifolds), the tunnel penetration in
   the north foundation wall, the tunnel itself
   (§6.5), and a **temporary service shed** in the back yard, on the
   tunnel alignment (x ≈ 80, just north of the house) — insulated
   ~10 × 12 ft, holding the meter + temporary main feeding the house
   panel through the *already-built tunnel trench/conduits* (services
   laid in their final path from day one, even though their source
   is temporary).
   Interim water: the well (drilled early, at its final east-side
   location) feeding the house through the tunnel line. Interim
   sewage: lift station pumping through the forcemain to… the septic
   tank, which therefore gets installed in this phase too, at its
   final shop-side location — a tank in the ground doesn't need the
   shop building over it.
3. **Live in the house.** Shed carries it. Nothing about the house's
   internal systems knows the source is temporary.
4. **Shop build:** slab + building, Bay 1 fit-out (service, inverters,
   batteries, generator, boiler, water plant). Stair down to the
   tunnel portal in 1E connects to the existing tunnel.
5. **Cutover:** utility service moved shed → shop (one planned outage),
   house feeder energised from 1B, generator/battery proven under
   load, *then* the shed is emptied. Shed retires to garden/pump
   storage or is sold — it was always a means to an end.
6. **Later:** solar field, second battery row, snow-melt loops,
   future houses (§9) — all land on capacity reserved in phase 4.

## 9. Future houses

Each future house repeats the house pattern at smaller scale: a panel
fed from 1B, water from the 1C manifold, fibre from 1D, sewage via its
own lift station to the shop tank (or a gravity line if the land
falls kindly). **Default: direct-buried services in the reserved
corridors, not tunnels** — one walkable tunnel is a luxury that pays
for itself in daily use; three is just concrete. The things that make
this cheap later are all phase-4 decisions: switchboard space, spare
conduits in the corridors, manifold outlets, and a septic design that
either has the capacity or a documented expansion area.

## 10. Consolidated decisions for you

My recommended default is in **bold** — say the word and it stands.

- **D1 — Back-yard depth: ~62 ft** (house north porches → shop south
  wall; tunnel ~70 ft, §6.1). Shrinking it is still the biggest single
  saving in this plan; growing it costs tunnel money and back yard.
- **D2 — Bay order south → north as drawn** (utilities, work,
  work + pit, wash). Utilities southernmost is what makes the short
  southbound tunnel work; the rest of the order is preference.
- **D3 — Gas stays out of the tunnel** (direct-buried). Override only
  with the AHJ-approved vented compartment.
- **D4 — Well outside, east of the shop**; equipment in 1C.
- **D5 — Utility service conversation early**: single-phase cap vs
  three-phase decides the electrical design's shape.
- **D6 — Tunnel built with the house** (full length preferred, capped
  half-tunnel as the fallback).
- **D7 — Basement link: RESOLVED by v3** — the tunnel enters
  UTILITIES directly through its north foundation wall; no receiving
  room, no theater impact, nothing to decide.
- **D8 — Pit in Bay 3 only**, 40 × 4 ft, drive-over covers.
- **D9 — Wash bay to separator + holding tank** (no alternative on
  the table — this one is rules, not preference).
- **D10 — Generator fuel: diesel** if the parcel has no gas line,
  natural gas if it does (same open question as house heat).
- **D11 — Shop structure: steel clear-span** vs post-frame, decided
  on quotes at 20 ft eave.
- **D12 — Interim septic installed in the house phase** (§8.2) — the
  alternative is a temporary holding tank and a second install bill.

## 11. What this plan is not

Not a permit set, not engineered, and not priced beyond the one
flagged tunnel range. The AHJ conversations that gate real design:
gas-in/near-tunnel routing, tunnel fire separation/egress, pit
requirements, septic design, well siting, and the utility service
size. The SCAD models (`shop.scad`, `site.scad` in the house repo)
already carry this v3 plan — shop behind the house, west shared
drive, front loop + garden, tree belt, and the tunnel entering
UTILITIES' north wall. The basement tables are unchanged: v3 needs
no basement change at all.
