# Shop — Base Plan (100 × 100 ft, 4 bays, utility hub + tunnel to house)

Compiled 2026-10-29 for Jordan. Companion to *House-Review-and-Research-2026-10-28.md*.
Planning only — not construction documents. Land is not yet secured, so every
position below is **relative** (to the house), not a surveyed site plan.
Diagrams: `site-plan.png`, `shop-floor-plan.png`,
`tunnel-section.png`. SCAD: `shop.scad` and `site.scad` in
the house repo model this plan.

**Revision v2 (2026-10-29, Jordan's redirect):** the shop is **rotated
90°** from v1. The bays now run **north–south**, the front (overhead
doors) faces **south**, and Bay 1 (utilities) is the **easternmost**
bay, closest to the house. The tunnel leaves the **side** (east wall)
of Bay 1 at its portal room and runs due east on the centreline of the
basement's **UTILITIES room — which sits on the north side of the
basement** — instead of v1's southern alignment to a new room under
the mud room/garage. §5 and §6 carry the consequences.

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

| # | Assumption in v1 | Why |
|---|---|---|
| A1 | Shop sits **west of the house, 100 ft clear** between the garage's west wall and the shop's east wall | Round stakeout number, good fire/noise separation, room for the court. This is the single biggest cost lever on the tunnel (§6) |
| A2 | Shop's footprint sits west of the house with its middle on the basement UTILITIES centreline (house-frame y ≈ 52.5) | Aligns Bay 1's side portal, the tunnel and the basement UTILITIES room on one straight east–west line |
| A3 | Bays run **north–south** (100 ft deep), doors on the **south** wall, each bay 25 ft wide, stacking west → east: wash, work + pit, work, utilities (v2, Jordan) | The 90° rotation puts Bay 1's long east side facing the house, so the tunnel leaves its side, not its end |
| A4 | The tunnel lands in a **new receiving room at the basement's west wall, north end**, tied into the existing UTILITIES room (§5) | The UTILITIES room has no outside wall on the west — the theater sits between it and the foundation — see §5 |
| A5 | The drilled well itself is **outside** the shop; what lives in Bay 1 is the well *equipment* | §4.3 — wellheads inside buildings are a contamination/access problem |
| A6 | **Gas does not run inside the tunnel** by default; it goes direct-buried alongside it | §6.3 — gas in an enclosed occupied tunnel is the one part of the concept an inspector is likely to refuse as drawn |
| A7 | Shop boiler (from your 2026-10-28 note) lives in Bay 1 and is the heat hub for shop slab, tunnel, house hydronics and snow melt | Ties this plan to the earlier research instead of duplicating plant in the house |

---

## 1. Site base

Coordinates below reuse the house model's frame (feet; x = east, y = north;
garage west wall x = 0, house front wall y = 0, front porch to the south).

- **Shop:** east wall at x = −100, west wall at x = −200, south wall at
  y ≈ 2.5, north wall at y ≈ 102.5. Front (all overhead doors) faces
  **south** onto a **60 ft deep truck apron** — and south-facing doors
  get winter sun on the ice in front of them, which in Alberta is worth
  real money. Trucks reach the apron via the south spine (below).
- **Shared driveway:** a court between house and shop (over the tunnel),
  plus a south spine running from the garage's west doors, west along
  the shop's south front to the apron. Cars use the court; trucks use
  the spine + apron on the shop's south side.
- **Well zone:** south-west of the shop (short run into Bay 1's water
  room at its south end; keeps the well on the opposite side of the
  shop from the septic).
- **Septic zone:** tank north-west of the shop, treatment field further
  north — as far from the well as the layout allows (plan on the
  ≥ 30 m / ~100 ft well-to-septic separation from the well research;
  final distances are the septic designer's, after a soil test).
- **Reserved corridors:** a services corridor north from Bay 1 and one
  east (over the tunnel) for future houses (§9). Keep buildings, the
  septic field and the well out of both.
- **Grading:** shop slab at grade for truck entry. The house basement
  floor is ~11 ft below grade, so the tunnel is a deep structure its
  whole length and arrives *under* the shop — see §6.2 for the shop-end
  stair. Surface drainage must fall away from both buildings and must
  not pond over the tunnel.

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
  east side (§6.2) — its opening is in the shop's foundation, not a pour
  embed in the slab itself.
- **Doors:** Bays 2–4: **14 ft wide × 14 ft high** insulated overhead,
  on the **south** wall. Bay 1: 10 ft wide × 12 ft overhead + a man door
  (equipment in/out, no trucks), also south. Man door on the east
  (house) side for daily use on foot.
- **Fire/life safety flags for the designer:** fuel, welding, a pit,
  batteries and a generator in one building drive separations, ventilation
  and possibly sprinkling. The generator and battery rooms below are
  planned as separated rooms from day one because retrofitting that is
  miserable.

## 3. Bay by bay (west → east)

### Bay 1 — Utilities (25 × 100 ft, easternmost) — §4 has the detail
The hub. Subdivided south → north: **1A generator room (south end) →
1B electrical + batteries → 1E tunnel portal, stair and manifold room
(mid-bay, on the east wall, on the tunnel centreline) → 1C water +
heat → 1D network/server + bathroom (north end)**. Everything the
house (and later, other houses) needs is generated, stored or
terminated here, and every service leaves through 1E — the portal
room sits between the electrical and water/heat rooms on purpose, so
both feed it with short runs.

### Bay 2 — Truck work (25 × 100 ft)
General work bay. 14 × 14 door on the south wall, open floor for a
2-post or mobile-column lift, benches/tool storage on the **north
(back) wall**, welder and air compressor at the north wall with drops
down the bay. Keep the middle of the floor empty — a 100 ft deep bay
is for a truck + trailer *inside*, which only works if nothing creeps
into the lane.

### Bay 3 — Truck work + pit (25 × 100 ft)
Second work bay with the **pit**: proposed **40 ft long × ~4 ft wide ×
~5.5 ft deep**, running north–south (the bay's direction), centred in
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

### Bay 4 — Wash bay (25 × 100 ft, westernmost)
14 × 14 door on the south wall, slab sloped to a **centre trench drain**
(running north–south), hose reels and pressure-washer plant (hot-water
unit) in a small equipment zone at the north end. Drainage: trench →
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
- **Generator (1A, south end of Bay 1):** its own fire-separated room
  with combustion-air louvres and exhaust direct to outside through
  the south wall — the south end is deliberate: shortest air/exhaust
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

### 4.3 Water (1C, ~24 ft)
- Well drilled **outside, south-west of the shop** (A5); line enters
  Bay 1 underground and runs to 1C. In 1C: pressure tanks, treatment train (decided by the
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

### 4.5 Bathroom (1D, north end with the network room)
Simple and complete: WC, sink, **shower** (a shop you can wash in
before going to the house is the point), floor drain, water heater
fed from 1C next door. Drains **by gravity north/west to the shop
septic tank** (shop slab is at grade, tank is below grade — gravity
works here, unlike the house run, §7). Hot water and the room itself
are on the shop slab heat zone.

## 5. The house end — landing in the north-side UTILITIES room

**The geometry (checked against the current house model,
`nuniesmith/house` @ a88cf06):** the basement's UTILITIES room sits on
the **north side** of the basement (basement coords (30,45)–(70,60),
under the nook/kitchen area). It has exactly one outside wall — its
north wall is foundation. On its west, between UTILITIES and the
basement's west foundation wall, sits the **theater** (basement
(0,35)–(30,60)). So a tunnel running due east on the UTILITIES
centreline (house-frame y = 52.5) reaches the basement's west wall
in line with UTILITIES, but enters through the theater's territory.

**The fix in this plan (v2):** a **utility receiving room carved from
the theater's west end** — basement coords roughly (0,44)–(12,60),
12 ft wide × 16 ft deep at the basement's north-west corner:
- the tunnel's fire-rated door on its west (foundation) wall;
- the **duplex grinder lift station** for all house sewage (§7) —
  or it lives in UTILITIES itself if space prefers; decide at
  mechanical design;
- services then continue **east along the theater's north wall in a
  ceiling bulkhead/soffit** straight into the UTILITIES room's west
  wall — pipes and cables don't need a walkable corridor, and a
  bulkhead over the theater's screen wall is a small, honest price;
- people reach UTILITIES from the receiving room via the theater and
  the existing basement circulation (theater door → rec room →
  utilities door), which is fine for a route used occasionally;
- the house's 200 A panel, water manifold, hydronic exchangers and
  fibre termination live in **UTILITIES itself**, as originally
  intended — it is 40 × 15 ft, big enough for the house's minimal
  kit once the shop carries the plant.
The cost is real and stated plainly: **the theater narrows from
30 ft to ~18 ft wide.** It stays a big theater (the screen wall moves
to the receiving room's east wall), but if that trade is unacceptable
the alternative is a deeper tunnel passing *under* the basement slab
and stairing up inside UTILITIES — more structure, more money, no
theater loss. That's decision D7. Either way this is
**house-foundation design work** — it has to be drawn with the
basement ICF, not dug later. (v1's extension under the mud room/
garage is superseded by this section.)

## 6. The tunnel (utilidor)

### 6.1 Route and size
Straight, Bay 1's portal room (mid-way along its **east side**) →
the basement's west wall, on the UTILITIES centreline (house-frame
y = 52.5). At A1's 100 ft building gap the run is **~130 ft** — the
extra ~30 ft is the basement itself, which sits 30 ft east of the
garage's west wall — plus the two end structures. **Proposed section:
~8 ft wide × 7.5 ft clear inside** — a real walkway (4 ft clear) plus
a service trench zone under **removable floor grates**, per your
spec. Grate sections sized to lift by hand (< ~40 lb each). Precast
concrete box sections are the default construction (fast, known cost
per foot, watertight joints available); cast-in-place is the
fallback.

### 6.2 The level problem (read this one)
The tunnel floor sits at **house basement level — about 11 ft below
the shop slab**. At the house end that's perfect (it walks straight
into the new receiving room at the basement's west wall, §5). At the
shop end it arrives *under* Bay 1: **1E is a stair room** — services
rise up the manifold wall to grade-level distribution, and you reach
the tunnel down a full flight of stairs (~19 risers) inside 1E. No
way around it; a ramp would eat half the bay. The tunnel roof is
~3–4 ft below grade — deep enough for frost and for the driveway
court to drive over it.

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
  of this idea — at Alberta prices, budget *in the order of* $200K–
  $400K for ~130 ft installed, deep, serviced and finished
  *(rough planning range, unverified — get precast quotes early)*.
  A direct-buried bundle + access vaults does the same job for a
  fraction of that, minus walk-in access. Your concept is the walkable
  one and this plan follows it — just go in with eyes open, and note
  decision D1 below: **every foot of house–shop gap you remove is
  roughly a foot of tunnel you don't buy.**

### 6.5 Build timing — do the tunnel with the house
Excavation and concrete crews are already mobilised for the house
basement + receiving room (§5). **Build the full tunnel (or at minimum
the house-end half, capped at a bulkhead) during the house build**,
while the trench is cheap to open. Digging it later, under a finished
driveway, is the expensive way to own the same tunnel.

## 7. Septic — house pumps to the shop, shop drains by gravity

- **Tank + field:** at the shop, north-west zone (§1), sized and sited
  by the septic designer after soil testing (house is ~5 bedrooms plus
  a shop bathroom — don't guess the size here).
- **House → tank:** all house sewage collects to the **duplex grinder
  lift station** in the basement receiving room / UTILITIES (§5)
  (duplex = a pump can fail without an emergency; high-level alarm to
  the phone; on the generator-backed panel because it must never be
  without power). Forcemain runs through the tunnel (§6.3), rises at
  the shop, and drops into the tank. Lift is ~8–10 ft plus ~130 ft of
  friction — routine for grinder pumps.
- **Shop bathroom → tank:** gravity, short run north/west from Bay 1D
  (the bathroom sits at Bay 1's north end, nearest the tank).
- **Wash bay → NOT the tank:** separator + holding (§3, Bay 4). Pool
  backwash/drain water also stays out of the septic (volume + chlorine)
  — it needs its own discharge arrangement in the house mechanical
  design; flagged, not solved here.

## 8. Build order — house first, shed in between, shop second

1. **Land + tests:** geotech, well test hole/AWWID records, septic
   soil test — these pick the well and field zones for real.
2. **House build**, including: the basement receiving room (§5), the
   UTILITIES room's 200 A panel and the lift station, the tunnel
   (§6.5), and a **temporary service shed** at the house's north-west
   side, on the tunnel alignment — insulated ~10 × 12 ft, holding the
   meter + temporary main feeding the house panel through the
   *already-built tunnel trench/conduits* (services laid in their
   final path from day one, even though their source is temporary).
   Interim water: the well (drilled early, at its final shop-side
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

- **D1 — House–shop gap: 100 ft** (tunnel ~130 ft, §6.1). Shortening
  to 60 ft is the biggest single saving in this whole plan; lengthening
  costs tunnel money for separation you may not need.
- **D2 — Bay order west → east as drawn** (wash, work + pit, work,
  utilities). Utilities easternmost is what makes the side-portal
  tunnel work; the rest of the order is preference.
- **D3 — Gas stays out of the tunnel** (direct-buried). Override only
  with the AHJ-approved vented compartment.
- **D4 — Well outside, south-west of the shop**; equipment in 1C.
- **D5 — Utility service conversation early**: single-phase cap vs
  three-phase decides the electrical design's shape.
- **D6 — Tunnel built with the house** (full length preferred, capped
  half-tunnel as the fallback).
- **D7 — Basement link: receiving room carved from the theater's
  west end** (theater 30 ft → ~18 ft wide) **+ north-wall bulkhead**
  into UTILITIES — vs the under-slab tunnel that spares the theater
  for more money. Receiving room is my default.
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
already carry this v2 plan, including the proposed receiving room
drawn as a translucent change over the theater's west end in
`site.scad` — the basement tables themselves are unchanged until
D7 is settled.
