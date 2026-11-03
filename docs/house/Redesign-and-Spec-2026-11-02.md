# House redesign (November 2026): model notes and build spec

The main floor and the basement were redrawn. The plans are
[`main_floor.jpg`](main_floor.jpg) and [`basement.jpg`](basement.jpg); the
Oct 30 [`floor_plan.JPEG`](floor_plan.JPEG) is the version before them.
This document covers:

1. how the plans were turned into the OpenSCAD model, and what changed on the way;
2. the stair between the floors;
3. the foundation;
4. the concrete for the indoor pool and the hot tub that spills into it;
5. the stadium-tiered home theater floor;
6. the basement exit stair;
7. basement windows;
8. the open questions.

**Update, Nov 2:**

- The basement is now 12 ft clear.
- The great room has a door onto the deck.
- The basement has an exit stair up to the back yard (section 6).
- The shop tunnel will connect to the basement utility room; its route
  comes later. *(Superseded Nov 3: no tunnel.)*

**Update, Nov 2 (later):** basement windows are planned: two light wells
and a glazed exit door (section 7).

**Update, Nov 3:**

- **Sun room and patio.**
  - The room north of the upper hall, beside the study, is the
    **sun room**. It was labelled "sitting room" before, and now has
    tall windows.
  - The "breakfast nook" beside it is an open, covered **patio** at
    floor level, running onto the deck. It has no walls, and a guard
    along its edge over the exit stair.
- **House first.** The house is built first. The shop is a separate,
  later project.
- **No tunnel.** The shop tunnel is dropped. The shop will get buried
  service lines from the house's west side, by the UTILITY room.
- See [`../permit/README.md`](../permit/README.md).

The site is rural Alberta (see
[`../House-Review-and-Research-2026-10-28.md`](../House-Review-and-Research-2026-10-28.md)).
Code references are to the National Building Code, Alberta Edition (NBC-AE), and to CSA A23.1.

> **Not construction documents.** The sizes below are a planning basis for
> quotes and for the engineer. Footings, the ICF walls, the pool and spa
> shell, and the depressed slabs all need a structural engineer's design.
> Concrete classes depend on a geotechnical report (sulphates, groundwater).
> Code values quoted from secondary sources are marked *verify* and must be
> checked against the current CSA A23.1 and NBC-AE text.

![Cutaway: both levels, cut east-west](cutaway.png)

## 1. The model

| View | File |
|---|---|
| Main floor plan | [`main_floor_plan.png`](main_floor_plan.png) |
| Basement plan | [`basement_plan.png`](basement_plan.png) |
| Section A: east-west through the stair, theater and pool | [`section_a.png`](section_a.png) |
| Section B: along the stair | [`section_b.png`](section_b.png) |
| Section C: through the theater | [`section_c.png`](section_c.png) |
| Section D: through the pool and spa | [`section_d.png`](section_d.png) |
| Section E: along the basement exit stair | [`section_e.png`](section_e.png) |
| The exit stair, from the back yard and cut open | [`exit_stair.png`](exit_stair.png), [`exit_stair_cut.png`](exit_stair_cut.png) |
| The basement light wells | [`light_wells.png`](light_wells.png) |
| The basement alone, in 3D | [`basement_3d.png`](basement_3d.png) |
| Foundation alone | [`foundation.png`](foundation.png) |
| Both levels, apart | [`house_exploded.png`](house_exploded.png) |
| Outside | [`house_front.png`](house_front.png), [`house_back.png`](house_back.png) |

![Section A](section_a.png)

### 1.1 One coordinate frame for both floors

Both floors now share the main floor's coordinates, in feet:

- x runs east, with x = 0 at the garage's west wall.
- y runs north, with y = 0 at the front wall of the den and the breakfast bay.
- z = 0 is the finished main floor.

The main-floor plan reads at 15.2 px/ft and the basement sketch at
29.7 px/ft. The two are registered through the stair, the one element
that must line up. With that registration, every basement room comes out
within 1–2 in of its labelled size.

| Level | Elevation |
|---|---|
| Main floor (finished) | 0'-0" |
| Top of foundation walls (sill) | −1'-7½" (18" floor trusses + subfloor) |
| Grade | −2'-0" |
| Basement ceiling | 12'-0" clear (theater front tier: 13'-3") |
| Basement floor (slab top) | −13'-9" (11'-9" below grade) |
| Footing top / bottom | −14'-7" / −15'-5" (13'-5" below grade) |
| Theater front tier | −15'-0" |
| Pool water surface / pool floor | −14'-3" / −18'-9" |
| Spa rim / water / floor | −12'-3" / −12'-5" / −15'-11" |
| Bottom of the pool excavation | −20'-3" (18'-3" below grade) |
| Frost-wall footings | −6'-0" (4'-0" below grade) |

The floor-to-floor height is one parameter, `floor_to_floor()` in
`models/house_lib.scad`. It is **13.75 ft, which gives 12 ft basement
ceilings**. These follow it automatically:

- the basement rooms;
- the main stair: 22 risers;
- the exit stair: 19 risers up to grade;
- the foundation;
- the pool and theater levels.

For 10 ft ceilings, set it to 11.75.

### 1.2 Changes from the drawings

1. **The stair** (section 2). It is drawn entered from the south on both
   floors, which no straight stair can do, and its box is about 9 ft long,
   too short for any basement stair. It now starts at the north end in the
   upper hall and runs 18'-4½" south, under the main hall, to the basement
   hallway.
2. **Basement hallway**: 1.7 ft deeper, and the living room 1.7 ft shorter.
   The foot of the stair lands in the hallway, at the 8 ft archway into the
   living room.
3. **Basement doors**: the sketch has none, so 19 were added. Two to note:
   - the theater door swings out into the hallway, clear of the back row;
   - the pool room and the pool bath each open off the long hall.
4. **Main floor upper hall**: split at the sun room / patio line by a
   wall with a 2'-8" door, as drawn.
5. **Master-suite double doors**: set where the plan shows them,
   1.3 ft west of the closet wall.
6. **Basement fixtures**: inset 6½" from the outside walls. The 13¼" ICF
   walls are thicker than the drawn walls.
7. **Furniture and fixtures** are illustrative: the plan's own, plus
   equipment in the utility and pool equipment rooms.
8. **Great room to the deck**: 6'-0" French doors, swinging in, take the
   place of the drawn 6'-9" two-pane window at the west end of the great
   room's north wall, nearest the kitchen and the patio. The plan had no
   door onto the deck.
9. **Basement exit stair**: added outside the gym (section 6).
10. **Basement windows**: two windows in light wells (section 7).

`tools/check_layout.py` checks both levels after every edit. It confirms:

- every door joins the rooms it should;
- every leaf swings clear of walls, fixtures, the theater seats and other leaves;
- every room is reachable;
- rooms neither overlap nor leave slivers between them.

## 2. Stair between the floors

| | Model | NBC-AE limit (stairs in a dwelling unit) |
|---|---|---|
| Rise | 22 risers × 7½" (190.5 mm) = 13'-9" | ≤ 200 mm (7⅞") *verify* [S1] |
| Run | 21 treads × 10½" (267 mm) = 18'-4½" | ≥ 255 mm (10") *verify* [S1] |
| 2R + T | 25½" | comfortable range ~24–25½" (rule of thumb) |
| Clear width | 4'-2½" (1 286 mm) between walls | ≥ 860 mm |
| Headroom | ≥ 1 993 mm at the tightest point | ≥ 1 950 mm [S1][S2] |
| Handrails | both sides in the model | at least one side for > 2 risers; 865–965 mm high *verify* [S3] |
| Landings | top: the upper hall; bottom: at the 8 ft archway into the living room, 5 ft clear to the sofa | ≥ stair width, ≥ 900 mm long |

**Headroom.** Headroom is the tight dimension. The main hall's floor
(1'-7½" deep) crosses over the lower half of the flight. The floor opening
runs 11'-5" from the top nosing back to the main hall's north wall. That
keeps 1 993 mm of clear height under the floor edge, measured vertically
from the line of the nosings. The opening cannot get shorter without
cutting into the main hall.

**Width.** The stair is wider than 1 100 mm. Check NBC 9.8.7.1 to see
whether a second handrail is required at that width. The model draws one on
each side either way.

## 3. Foundation

Model: `models/foundation.scad`, and `mode = "foundation"` in
`models/house_combined.scad`. Alberta practice is in the research
document, §1.3–1.5.

![Foundation](foundation.png)

### 3.1 Basement walls and footings

- **ICF walls:** an 8" concrete core with 2⅝" EPS on each face, 13¼"
  overall, running from the footing to the sill (about 13'-0" of wall).
  - About 11¾ ft of backfill against a 13 ft wall is past most prescriptive
    ICF tables, so it needs an **engineered design**. Expect 15M verticals
    and horizontals at about 400 mm (16") or closer.
  - Build in a buck for the exit door (section 6), and for any windows.
- **Perimeter footings:** 24" × 10", on undisturbed soil 13'-5" below
  grade. Frost does not govern at this depth.
- **Interior bearing lines:** thickened-slab strip footings, 20" wide,
  under the main floor's bearing walls:
  - x = 54.14 ft, which is the theater, hallway and living room line;
  - x = 69.38 ft, the theater / pool room wall;
  - x = 96.33 ft, the pool room / pool equipment wall;
  - y = 18.15 ft, along the long hall.
- **Deepened footings round the pool room:** the pool pit is dug
  6½ ft below the basement footings, inside their 1:1 bearing zone. The
  model takes those footings down to the pit depth. The alternative is
  designing the pool shell to retain them; that is the engineer's call
  (section 4.5).
- **Theater pit:** the lowered front tier stops 1 ft short of the side
  walls and 2½ ft short of the screen wall (section 5). That keeps it out of
  the footings' 1:1 bearing zones, so no footing steps down for it.

### 3.2 Slab, insulation, radon

- **Slab:** 4" (100 mm) on 6" (150 mm) of clear crushed stone, over a
  sealed 10-mil poly vapour barrier taped to the walls.
- **Insulation:** 2" rigid insulation (EPS Type 2 or XPS) under the slab is
  worth it in zone 7A/7B. It is essential if the slab carries in-floor heat.
- **Radon (NBC 9.13.4):** Alberta adopts these provisions unchanged [S4][S5].
  - The clear stone is the gas-permeable layer.
  - Rough in a sealed, capped pipe through the slab to that layer.
  - The pool pit and the theater pit have their own stone beds, so connect
    them to the main layer with a pipe, or give them their own rough-in.

### 3.3 Waterproofing and drainage

Use the standard stack in research §1.5:

- membrane or dampproofing on the ICF;
- drainage board;
- weeping tile at the footings, to a sump;
- free-draining backfill.

The pool pit adds a second, deeper drain loop (section 4.4).

### 3.4 Concrete for the house foundation

| Element | CSA A23.1 class | Strength / max w/cm | Notes |
|---|---|---|---|
| Footings, ICF walls | S-class from the geotech report; else N | S-2: 32 MPa at 56 days, 0.45, HS/HSb cement [S6] *verify* | Alberta soils are often sulphate-bearing; the geotech report decides S-1/S-2/S-3 |
| Basement slab | N (interior, above the poly) | 25–32 MPa, ≤ 0.55 | Lower w/cm curls less; cure wet for 7 days |
| Garage slab | C-2 (de-icing salts drip off cars) | 32 MPa, 0.45, air-entrained *verify* | |
| Frost walls, porch piers | as the footings (S-class if sulphates) | air-entrained where exposed above grade *verify* | |

### 3.5 Where there is no basement

- **Frost walls:** 8" concrete on 20" × 8" footings with the bottom
  4'-0" (1.2 m) below grade, the Alberta minimum (research §1.4). They run
  under every main-floor outside wall that is not over the basement:
  - the bedroom wing;
  - the scullery;
  - the patio's edges (the old nook);
  - the office and master wing;
  - the den, foyer and breakfast-bay fronts;
  - the garage.

  They stop against the basement walls. The model's `frost_walls()` lists
  all 26 segments.
- **Crawlspace:** 18" clear under those parts of the main floor.
  Condition it as part of the house, with insulated frost walls and a
  sealed ground cover tied into the radon layer. That beats venting it in
  zone 7.
- **Garage:** a 4" slab on 6" stone. Its top is 18" below the house floor;
  the house door has a landing and two steps.
- **Porch posts:** 12" piers on 24" bells, 4½ ft below grade, or helical
  piles. The one post that stands on the basement wall needs no pier.

## 4. Pool and hot tub: the concrete

![Section D: pool and spa](section_d.png)

### 4.1 Geometry, as drawn on the basement plan

| | Pool | Spa (hot tub) |
|---|---|---|
| Inside size | 15'-0" × 15'-0" | 8'-0" × 8'-2" |
| Water depth | 4'-6" uniform (no diving) | 3'-6"; bench 21" below the water on three sides |
| Water level | 6" below the deck | rim 18" above the deck; water 2" below the rim |
| Water volume | 28.7 m³ (≈ 7 600 US gal) | 4.9 m³ (≈ 1 280 US gal) |
| Entry | four 12" steps in the NW corner, the top one 6" under water | over the rim |
| Join | the spa sits against the pool's south wall, flush with its east side | a 2'-0" spillway in the shared wall drops spa water into the pool |

### 4.2 Shell

- **Thickness:** 9" (230 mm) walls and a 10" (250 mm) floor. That is
  thicker than a typical backyard pool's 6–8". This shell sits beside
  basement footings and up to 6½ ft below the basement slab, and it must
  hold the soil when empty.
- **Construction:** wet-mix shotcrete per ACI 506.2 and the new ACI pool
  guide, ACI PRC-506.8-24 [S7][S8]. Form-and-pour cast-in-place concrete
  also works.
- **Strength:** specify **35 MPa (5 000 psi) at 28 days**. The shotcrete
  industry's floor for pool concrete is 28 MPa (4 000 psi) in place
  [S7][S9]. Specify above it for an indoor shell that is never allowed to
  leak into a basement.
- **Exposure class:** the water is chlorinated, or salt if a
  salt-chlorine generator is used, and the shell never freezes.
  - Treat the water face as chloride exposure: **max w/cm 0.40**,
    CSA C-1-level durability [S10] *verify*.
  - C-3, for continuously submerged concrete without freezing, may be the
    code-minimum class. The engineer can choose it, but keep 0.40.
  - No air entrainment is needed indoors.
  - Use the soil side's sulphate class (section 3.4) if the geotech report
    calls for one; HS/HSb cement then serves both faces.
- **Waterproofing:** a crystalline waterproofing admixture in the shell
  mix. Then a waterproof interior finish:
  - pool plaster or an aggregate finish; or
  - tile on a bonded waterproof membrane. Tile is a good choice for the
    spa and the spillway.
- **Reinforcement:** typically 15M at 300 mm (12") each way.
  - Double mat in the floor and in the pool walls.
  - Cover: 75 mm (3") on faces cast against soil, 50 mm (2") to the
    water face.
  - *Engineer to design*, including the spa walls standing 18" above the
    deck and the step-down where the spa floor meets the pool wall.
- **Quantity:** about **20 m³ (26 yd³) in place**:
  - pool walls 6.7 m³;
  - pool floor 6.4 m³;
  - pool steps 1.1 m³;
  - spa walls, floor and bench 6.5 m³;
  - less 0.6 m³ for the shared wall.

  Order 10–15 % more for shotcrete rebound and overspray.

### 4.3 The pool–spa join and the spillway

- **One continuous placement.** Shoot the pool, the spa and the shared wall
  in one placement, with no cold joints. Shotcrete placed this way bonds
  monolithically, and shared pool–spa walls are routinely built without
  waterstops [S11][S12].
- **Where a joint is unavoidable,** for example if the 18" of spa wall
  above the deck is shot later:
  - roughen and prepare the joint;
  - cast in a PVC or hydrophilic waterstop;
  - hire a crew that has done it before, because encapsulating a waterstop
    in shotcrete takes skill [S13].
- **The weir sets the spa's water level, not the tile line.** Survey the
  spillway lip to ±⅛". A notch set 2–3" high is a classic failure: it puts
  the spa's waterline into the tile and the coping [S14].
  - Finish the 2'-0" lip in stone or tile, with a drip edge, so the water
    sheets into the pool instead of dribbling down the wall.
  - The spa needs its own suction and returns, and a means to fill it above
    the spillway. Plumb the spa as the high body that overflows into the
    pool.

### 4.4 Below the shell: water, insulation, drainage

- **Groundwater.** The pit bottom is 18'-3" below grade. Before anything
  else, the geotech must establish the seasonal-high water table.
  - The design must resist uplift when the pool is drained. A drained shell
    in high groundwater can float.
  - Set a **hydrostatic relief valve** in the main-drain sump [S15][S16].
  - Keep it working; never drain the pool with the relief blocked.
- **Drain loop.** Run a perforated loop at the pit bottom in the 6" stone,
  tied to the house's weeping tile and sump.
- **Insulation.** 2" rigid insulation under the floor and around the
  walls below the slab: EPS Type 2 or XPS, rated well above the ~3 psi that
  the shell and water impose. Without it, the pool water heats the ground.
- **Plumbing:**
  - two main drains with ANSI/APSP-16 anti-entrapment covers, piped to the
    pool equipment room next door;
  - pressure-test all piping before the shoot;
  - fill-test the shell for about 7 days before finishes.

### 4.5 The room around it

- **Footings.** The basement footings round the pool room go down to
  the pit depth, or the shell is designed to retain them (section 3.1).
- **Dehumidification.** An indoor pool needs a dedicated pool dehumidifier
  sized on evaporation, holding 50–60 % RH. Run the room air 1–2 °C above
  the water and slightly negative to the house. A pool cover cuts the load
  sharply.
- **Envelope.** The ICF walls keep the cold side out of the wall
  assembly.
- **The main floor above.** The pool room ceiling (the main floor's
  underside) needs a vapour-tight, corrosion-safe finish. The great room,
  the main hall, the foyer and the den are above it.
- **Equipment room.** The pool equipment room needs ventilation and safe
  chemical storage.

## 5. Home theater: the stepped floor

![Section C: theater](section_c.png)

### 5.1 Layout

A cinema-style stadium floor in the 14'-10" × 20'-6" room:

- **Rear tier** at the basement floor level, so there is no step at the
  door: 4 recliners, with a 2'-2" aisle by the door.
- **One 7½" step** with a 10¾" tread. The 15" total drop is split in two
  equal steps.
- **Front tier** 15" down, 9'-9½" deep and 12'-6" wide: 4 recliners.
- **Ledges** 1'-2" wide at floor level on each side, and a **2'-6" stage**
  at floor level under the screen. These keep the sunken slab clear of the
  footings (section 3.1).
- **Screen:** 120" 16:9 (8'-8¾" × 4'-10¾"), 18" above the floor, which is
  33" above the front tier.

### 5.2 Sightlines

Assumptions:

- seated eye height 40" above the seat's floor;
- top of head 4¾" above the eye;
- eyes about 11" in front of the seat backs.

| | Front row | Rear row |
|---|---|---|
| Eye elevation | 2'-1" (above the basement floor) | 3'-4" |
| Distance to the screen | 10.3 ft | 18.2 ft |
| Horizontal viewing angle | 46° | 27° |
| Look up to the screen centre | 10° | 2° |

**Check.** The rear row's sightline to the bottom of the screen passes
**5.4" above the front-row eye**, clearing a 4¾" head. That gives every-row
vision: each rear seat sees the whole screen over the head in front.

**Riser.** The minimum riser for that is 13.8"; 15" is provided.

**Trade-off.** Raising the screen bottom to 24" would cut the riser needed
to about 9". The cost is a front row looking up more steeply.

**The C-value method.** C is the height of the rear sightline above the
front spectator's eye. It is the standard way to size risers [S17].
- Here it is set to the eye-to-head-top distance; that is every-row vision.
- SMPTE's withdrawn EG-18 used 9–10" for a more generous margin [S18].
- Theater-seating suppliers quote 12–18" risers for two rows [S19].

### 5.3 Construction

- **Depressed slab:** form the step and the front tier as a depressed slab
  in the basement pour.
  - 4" slab on 6" stone at −15".
  - Thicken (turn down) the slab edges at the pit's sides.
  - Carry the poly and the radon stone layer continuously into the pit, and
    connect them (section 3.2).
- **Structure overhead:** the ceiling is the main floor's trusses, under
  the flex room, the upper hall and the main hall. The pit gains 1'-3" of
  height at the front.
- **Sound isolation:** build it as a room within a room:
  - double drywall with damping compound on isolation clips and channel,
    on the walls and on a ceiling hung under the trusses;
  - a solid-core door with perimeter seals;
  - lined, baffled duct runs.
- **Neighbours:** the bath, gym, hallway, pet room and pool room share its
  walls. The music room is next door to the gym, so isolate it the same
  way.
- **Cheaper alternative:** build a framed 15" riser on a flat slab. This
  needs no depressed concrete, but it puts a step at the door and leaves the
  rear row 10'-9" of headroom.

## 6. Basement exit stair

![The exit stair, cut along its length](exit_stair_cut.png)

The basement plan has no way out but the main stair. As in the previous
design, the model adds an exterior stair in an **areaway**: a walled,
open-topped stairwell outside the foundation.

### 6.1 Where it can go

An outdoor stair needs open sky above it for headroom. Most of the
basement's outside walls are under the main floor or its porches, which
rules them out.

| Basement wall | What is above or beside it | Verdict |
|---|---|---|
| **Gym's north wall** | Open back yard behind the sun room and the patio; the deck to the east, the study stoop to the west | **Chosen** |
| Music room's north wall | The bunk room above it as far as x = 32.6; the study stoop and its steps beside the rest | No room for the stair |
| Living room's south wall | Open front yard, west of the front porch | Possible, but it sits in the front elevation, next to the main stair |
| Living room's west wall | An 11 ft gap between the garage and the kitchen, with the side-entry steps in it | Too small for a straight stair |
| Pool room and pool equipment (north, east) | Under the deck and the office porch, which are 2 ft above grade | No headroom; a pool-room exit also fights condensation |
| Every other outside wall | The main floor | — |

### 6.2 The design

![The exit stair from the back yard](exit_stair.png)

- **Door:** a 3'-6" exterior door in the gym's north wall, between the
  treadmill and the power rack.
  - It opens inward, so drifting snow can't block it.
  - It is at the opposite end of the basement from the foot of the main
    stair, so the two ways out are far apart.
- **Areaway:** 4'-0" clear, running along the outside of the house.
  - A 4'-8" landing at the basement floor.
  - Then a straight flight rising east along the north wall of the sun
    room and the edge of the patio.
  - It reaches grade just west of the deck, beside the deck steps, on a
    2'-2" landing slab.
- **Stair:** 19 risers × 7.42" (188 mm) = 11'-9", and 18 treads × 11"
  (279 mm) = 16'-6". The treads are a little deeper than indoors, for snow
  and boots.
- **Walls:**
  - 8" concrete retaining walls on 20" footings, on the north and west
    sides, up to a 6" curb above grade.
  - A **42" guard** on the curb. Over a drop this deep the NBC calls for
    1 070 mm *verify*.
- **The house side:**
  - Along the gym it is the basement's ICF wall.
  - East of the gym it is the patio's frost wall, which must be **carried
    down to the areaway floor** for about 12 ft; the model shows this.
- **Water and snow:**
  - a drain at the bottom landing, piped to the sump;
  - a cover, at least over the lower half, so the stair doesn't fill with
    snow: a shed roof or a canopy off the house wall;
  - heated or heat-traced treads are worth considering.
- **Service entrance.** A straight stair and a 3'-6" door are also how the
  piano, the gym equipment and the pool plant get into the basement.

## 7. Basement windows

### 7.1 Do you need them?

**Egress windows: no.** The NBC requires an egress window, or an outside
door, from each bedroom (9.9.10). The basement has no bedrooms, and the
exit stair (section 6) is a second way out anyway.

**Natural light: probably not, but ask.**
- NBC 9.7.2 sets minimum window glass by room type. Living rooms, dining
  rooms and bedrooms are the strictest.
- Basement recreation rooms and unfinished basements carry the smallest
  requirement, and electric lighting can often stand in.
- Whether the building official reads the basement "living room" and
  "music room" as recreation rooms is their call: ask the municipality
  *verify*.
- If they class the living room as a living room, it needs glass equal to
  about 10 % of its floor, roughly 40 ft². Two windows would be needed.

**Livability: yes, a few.** A 3,000 ft² basement with a gym, a music room
and a living room is a lot of space with no daylight.

**What makes windows expensive here.** The floor is 11'-9" below grade.
Every window needs a light well about 8 ft deep:
- concrete walls and a drain;
- a guard or a walkable grate;
- a buck and lintel in the ICF before the pour.

And most of the basement's outside walls sit under the house or its
porches, where no well can go.

### 7.2 The plan

![Basement light wells](light_wells.png)

| Room | Window | Light well | Notes |
|---|---|---|---|
| Living room | 8'-0" × 4'-0", sill 4'-6" above the floor, south-facing | 9 × 5 ft, in front of the kitchen's front wall, beside the front porch | The best one: the main room, with south sun. Terrace or plant the well's outer side so it reads as a sunken garden, not a pit |
| Music room | 3'-0" × 4'-0", north | 3'-5" × 5'-3", between the bunk room and the study stoop | Small, but the room's only daylight. The bunk room's frost wall is carried down to the well floor, as at the exit stair |
| Gym | a full-glass 3'-6" exit door | the exit stair's areaway | No extra digging |

**Optional:**
- **Pool room:** the only place for a well is under the deck. Daylight
  could come down through a glazed or open section of the deck floor above
  a well at the pool room's north wall. Worth pricing, since an indoor pool
  with no daylight is gloomy, but it is not modelled.
- **Living room, second window:** a second well in the corner between the
  garage and the kitchen, west of the living room. Use it if the official
  wants about 10 % glass there.

**For the ICF crew:**
- Window bucks at the right heights before the pour.
- Lintels sized for the 13 ft walls.
- Each well's drain tied to the weeping tile and the sump.

## 8. Open questions for you

1. **Services to the shop.** The tunnel is dropped (Nov 3).
   - The shop is a separate, later project.
   - It will get buried service lines in a trench from the house's west
     side. That is where the basement's UTILITY room is: 14'-6" × 7',
     behind the storage room.
   - `models/site.scad` draws those lines dashed when `phase = "full"`.
2. **Natural light.** Confirm with the municipality how the basement
   living room is classed (section 7.1).
3. **Geotech first.** These all hang on the report:
   - sulphate class (cement type);
   - seasonal-high groundwater against a pool pit 18 ft down;
   - bearing capacity for the deepened footings.
4. **Building area.** With the attached garage, the house is about
   626 m² to the outside face of its walls. Part 9 of the building code
   stops at 600 m². See
   [the permit package, §1.1](../permit/README.md#11-the-house-is-over-the-part-9-size-limit)
   for the options; decide before the engineering starts.

## Sources

- [S1] Canada stair code summary (NBC 9.8: rise, run, headroom): <https://stairscalc.pages.dev/stair-code-requirements/canada>
- [S2] BC Building Code 9.8 excerpt (1 950 mm headroom in dwelling units): <https://www.bcpublications.ca/civix/document/id/bcbc2012/bcbc2012/ep001029.3>
- [S3] Rocky View County (Alberta), handrails in dwelling units: <https://www.rockyview.ca/Portals/0/Files/BuildingPlanning/Building/Guideline-Handrails-Dwelling-Units.pdf>
- [S4] Canadian Contractor, provinces adopting NBC 9.13.4 radon provisions without variation: <https://www.canadiancontractor.ca/features/unintended-consequences-quest-for-energy-efficient-homes-could-be-killing-canadians/>
- [S5] C-NRPP radon interpretive guide (NBC 9.13.4.2 / 9.13.4.3): <https://c-nrpp.ca/wp-content/uploads/2026/07/CNRPP-Bulletin-Radon-Document-Interpretive-Guide.pdf>
- [S6] Abridged CSA A23.1-04 exposure-class table (S-1 / S-2): <https://www.scribd.com/doc/282684746/Durability-of-concrete>
- [S7] American Shotcrete Association, 4 000 psi minimum for pool shotcrete: <https://shotcrete.org/faq-items/when-was-the-4000-psi-28-mpa-standard-set-for-shotcrete/>
- [S8] ACI PRC-506.8-24, *Shotcrete Use in Pool Construction—Guide*: <https://watershapes.com/?p=49783>
- [S9] ASA position paper, pool shotcrete strength: <https://shotcrete.org/wp-content/uploads/2020/01/ASAPositionPaper%5FPoolRec%5F1.pdf>
- [S10] Eng-Tips, CSA C-1 / C-2 w/cm limits: <https://eng-tips.com/viewthread.cfm?qid=474358>
- [S11] Shotcrete magazine, monolithic joints in pool shotcrete: <https://shotcrete.org/wp-content/uploads/2020/05/2014Fal_PoolRecShotcrete.pdf>
- [S12] Shotcrete magazine, interconnected pools built monolithic without waterstops: <https://shotcrete.org/wp-content/uploads/2025/03/Pool-and-Rec_Boundless-Waters.pdf>
- [S13] ASA FAQ, encapsulating waterstops in shotcrete: <https://shotcrete.org/faq-items/we-will-be-shotcreting-a-pool-and-the-designer-has-put-an-expansion-joint-in-the-pool-going-from-the-top-of-one-wall-through-the-floor-to-the-top-of-the-other-wall-it-also-shows-a-9-in-229-mm-poly/>
- [S14] WaterShapes, "High Waterlines, Bad Leaks" (raised-spa spillway levels): <https://watershapes.com/?p=38431>
- [S15] AstralPool, hydrostatic valve in the main drain: <https://www.astralpool.com/master/en/pool-shell-equipment/main-drains/main-drain-accessories/hydrostatic-valve.html>
- [S16] TMI Aquatics, why hydrostatic relief valves matter: <https://tmiaquatics.com/?p=5514>
- [S17] Sightline (architecture), the C-value: <https://en.wikipedia.org/wiki/Sightline_(architecture)>
- [S18] SMPTE EG 18 (withdrawn), theater design: <https://pub.smpte.org/doc/eg18/19940325-pub/eg0018-1994_withdrawn2003.pdf>
- [S19] Seatcraft, home-theater riser heights: <https://www.seatcraft.com/blogs/news/home-theater-seat-risers>
