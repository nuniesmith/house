# Engineering review and permit package

This folder is the hand-off package for the house. It is for two
readers:

- the **engineer** who reviews the design and engineers the structure;
- **you**, getting from here to an Alberta building permit.

It is generated from the model in `models/`, so it always matches the
3D design. Regenerate it after any model change with
`python3 tools/make_drawings.py`.

| File | What |
|---|---|
| [`House-Drawing-Set.pdf`](House-Drawing-Set.pdf) | 14 sheets, 24 × 36 in (ARCH D). Plans at 3/16" = 1'-0"; details at 1/4" to 3/4" |
| [`cad/`](cad/) | The main floor, basement and foundation plans as DXF files (inches, layered), for the engineer's or a drafter's CAD |
| [`schedules/`](schedules/) | Door, window and room schedules (CSV) |
| this README | The engineering brief (§4), the Alberta permit roadmap (§6), the code flags (§7) and the Phase 1 rough-ins (§8) |

> **Status: not for construction.** The set describes the design you
> want, drawn accurately from the model. It is **not engineered**. The
> foundation, the pool shell and the framing need an Alberta-registered
> engineer (APEGA) before they can be permitted or built.

---

## 1. Decide these before the engineer starts

### 1.1 The house is over the Part 9 size limit

The building code's Part 9, "Housing and Small Buildings", covers
buildings with a **building area of up to 600 m²** [P2][P3].

- **Building area** is the largest area above grade, measured to the
  outside face of the exterior walls.
- Porches and the basement don't count. The attached garage does.

| | ft² | m² |
|---|---:|---:|
| House + attached garage, at the wall centre lines | 6 319 | **587** |
| House + attached garage, to the outside face of the walls | 6 544 | **608** |
| House alone, to the outside face | 5 685 | 528 |

These numbers count the old breakfast nook as the open, covered patio it
is meant to be (§9). That took about 18 m² off.

As drawn, the house is still about 8 m² over the limit, so **Part 3**
would apply. Part 3 is the code for large buildings. It brings
professional design throughout and many rules that a house normally
never sees.

There are four ways to get back under 600 m²:

1. **Detach the garage.** It becomes a separate building.
   - The house alone is about 528 m².
   - Ask the permit office how it treats a covered walkway between them.
     A roof that joins the two can make them one building again.
2. **Separate the garage with a firewall.** Each side then counts as its
   own building.
   - A firewall is a heavy, rated concrete or masonry wall that has to
     carry through the roof.
   - It is costly at a house scale.
3. **Trim about 15 m² (160 ft²)** of enclosed area. That is enough for
   a margin under 600 m² once wall thicknesses are final. This is now
   the smallest change.
4. **Accept Part 3** and have the house designed to it.

This changes the code path for the whole design. Settle it with the
permit office (the "authority having jurisdiction") **before** paying for
engineering.

### 1.2 The land

Several things wait on the land:

- **Climate data.** Snow load, wind, frost, the heating degree-days and
  the energy-code zone (7A or 7B) all come from the location (§4.2).
- **The site survey.** An Alberta Land Surveyor draws the plot plan.
  Sheet A0.1 only shows the buildings relative to each other.
- **The geotechnical investigation.**
  - The basement footings sit about 13'-5" below grade.
  - The pool pit goes down to about **18'-3"**.
  - The design needs to know the groundwater level, the soil's bearing
    capacity and the sulphate exposure before it can be finalised.

### 1.3 Who builds it

Before a building permit is issued for a new home, Alberta needs one of
these [P4][P5][P6]:

- **a licensed residential builder**, who also provides new home
  warranty;
- **an Owner Builder Authorization** from the New Home Buyer Protection
  Office, if you build it yourself.
  - With it, warranty is optional.
  - From December 1, 2025, an authorization issued *without* warranty
    puts a caveat on the land title [P4].

### 1.4 Smaller decisions that change the drawings

- **Porches.** The porch floors are 2'-0" (610 mm) above the grade drawn
  around the house. A guard is needed wherever a walking surface is more
  than 600 mm above the ground next to it [P17]. Choose one:
  - raise the finished grade along the porch edges by an inch or two;
  - add guards (railings).

  The new patio's north edge is different: it stands right over the
  exit stair's areaway, about 11 ft down. It has a 42" guard in the
  model, and that guard is required.
- **Great room fireplace.** Gas or wood decides how it is vented and
  which code and permit apply to it.
- **Energy path.** NBC 9.36 has a prescriptive checklist and a
  performance path. The performance path uses an energy advisor's
  computer model of the whole house.
  - The house is large, with a lot of glass and an indoor pool, so the
    performance path is the practical choice [P8].

---

## 2. Phasing

The house is built first, on its own. **The shop is a separate, later
project with its own permits**, once the house is lived in. There is no
utility tunnel any more. When the shop is built, it gets buried service
lines in a trench from the house's west side. The basement UTILITY room
is on that side.

### Phase 1: the house, and all of the basement concrete

- **Concrete:**
  - footings, the ICF basement walls and the basement slab;
  - the pool and spa shells;
  - the theater's stepped floor;
  - the exit stair areaway and stair, and the light wells;
  - the frost walls, the garage slab and the porch piers.
- **Below the slab**, everything Phase 2 will need (§8). After the pour,
  nothing gets cut into the concrete.
- **Structure:**
  - the main stair;
  - the basement **bearing walls, beams and posts** (S1.1).

  They hold up the main floor, so they can't wait for the basement
  finish.
- **The mechanical room:** heating, HRV, water heater, water treatment,
  the electrical panel and the sump pump.
- **The main floor, roof and envelope**, finished for occupancy.
- **The site and services**, the bare minimum to live in the house (sheet
  A0.1):
  - **Driveway** from the road on the south, up the west side to the
    garage's west-facing doors. The front loop round the garden is
    optional.
  - **Power**, run underground from the road to a meter on the west
    wall. The panel is in the basement UTILITY room.
  - **Gas.** Natural gas from the road if a gas utility or co-op serves
    it. If not, a **propane tank** (1 000 US gal shown) on the west
    side, where the supplier can reach it from the driveway.
  - **Septic, on the west side** by the basement UTILITY room (§2.1).
    - The **tank** sits just off the house, so the sewer run out of the
      basement is short. It is within hose reach of the driveway for
      pump-outs, with an **effluent pump chamber**.
    - The **treatment field** goes further west, where the treated
      water soaks into the soil. A **reserve area** beside it is kept
      clear for a replacement field.
  - **Water.** A drilled **well** on the east side, clear of the septic.
    - Its line enters the basement at the pool equipment room, which
      needs water for the pool, and runs on inside to the UTILITY room.
  - **Internet.**
    - **Fibre**, if an internet provider on the Alberta SuperNet
      network reaches the road. It runs in the same trench corridor as
      the power.
    - **Starlink.** A dish with a clear view of the northern sky.
    - Either one can back up the other.
- **In the unfinished basement:**
  - a **thermal barrier over all of the ICF foam** inside, for example
    ½" gypsum board [P18][P19];
  - smoke and CO alarms;
  - the lighting and outlets the code requires.

### 2.1 Septic and well distances

Alberta's minimum separation distances, from the Private Sewage Systems
Standard of Practice 2021 [P25][P26]:

| Part | From a water well or source | From a watercourse | From a property line | From a building |
|---|---|---|---|---|
| Septic, holding or effluent tank | 10 m (33 ft) | 10 m | 1 m | 1 m |
| Disposal (treatment) field | 15 m (50 ft) | 15 m * | 1.5 m | 10 m from a basement, cellar or crawl space; 5 m from a foundation without one |
| Treatment mound | 15 m (50 ft) | 15 m * | 3 m | 10 m from a basement or crawl space |
| Packaged treatment plant | 10 m | 10 m | 6 m | 1 m |

- A field is also 5 m from its own septic tank.
- \* If the property adjoins a lake, river, stream or creek, the soil
  treatment part needs **90 m (300 ft)** from the shore. The exception is
  when the house sits between it and the water; then the table governs.
- The well regulations mirror this from the other side: no well within
  10 m of a watertight tank or 15 m of a field.
- My earlier plan used 30 m (100 ft) from every septic part. That is
  more cautious than the rule, and is not needed.

The table doesn't settle everything:

- **The installer's site evaluation** decides two more things: the
  field's vertical separation to the water table, and how much the soil
  can take. The evaluation uses soil pits, soil texture and the water
  table, and it decides between a field, a mound and an at-grade system.
  Its result can move the field.
- **Basement drains are pumped.** The building sewer leaves the house
  deep, so the tank sits deep too. Effluent is usually pumped up to a
  shallower field from a pump chamber. That is normal practice, and the
  designer handles it.
- **Size the system for everything that will connect to it.** A future
  house for the parents is planned. If it will join this septic system,
  count its flow now, and keep the field 10 m from its basement or crawl
  space when it is placed. A second house on the parcel also needs the
  municipality's approval under its land-use bylaw.
- **The shop, later:**
  - The **wash bay never goes to the septic**. It needs its own oil and
    grit separator and holding tank.
  - The **shop bathroom** can pump to the house tank through a small
    lift station.

### Phase 2: finishing the basement, after you move in

- Partitions, drywall, ceilings and floors.
- The bathrooms and the laundry.
- The theater build-out: room-within-a-room walls, seating, the screen.
- The music room, and the pool room finishes.

Phase 2 is interior work only, but it still needs **its own building
permit, plus electrical and plumbing permits**.

---

## 3. The drawing set

| Sheet | Title | Contents |
|---|---|---|
| A0.0 | Cover | Project data, building areas and the Part 9 flag, code basis, phasing, the Alberta roadmap, drawing index |
| A0.1 | Site plan (schematic) | The house-first site at 1" = 20': driveway, power, gas or propane, fibre or Starlink, well, septic tank and field, and the future shop's spot. **Must be replaced** by a surveyed plot plan (what it needs is listed on the sheet) |
| S0.1 | Structural design brief | Design criteria for the engineer to fill in, the elements that need engineering, questions, materials assumed |
| S1.0 | Foundation plan | ICF walls and footings, bearing-line and deepened footings, pool and spa shells, theater tiers, exit stair, light wells, frost walls, piers, crawlspaces, elevations, dimension chains |
| S1.1 | Main floor framing concept | The supports below the main floor and indicative clear spans; two **added supports** (red); the stair opening |
| A1.1 | Basement plan | Rooms, doors, windows, dimensions, the main floor outline overhead, the Phase 1 / Phase 2 split |
| A1.2 | Main floor plan | Rooms, doors, windows, dimensions, life-safety notes |
| A1.3 | Roof plan | Hip blocks with their pitches and plate heights |
| A3.0 | Elevations | All four sides, with plate and ridge heights |
| A4.0, A4.1 | Sections A–E | Cut through the model, with level lines |
| A5.0 | Foundation details | ICF wall, frost wall, bearing-line footing, porch pier, garage slab edge |
| A5.1 | Other details | Pool and spa, theater tiers with the sightline, exit stair, light well, main stair headroom |
| A6.0 | Schedules | Doors (D1xx, DBxx), windows (W1xx, WBxx), rooms |

Conventions (on every sheet):

- Dimensions are to wall centre lines. The ICF walls are dimensioned to
  their centre line, which is also the centre line of the main floor
  walls above.
- Elevations are relative to the **main floor = 0'-0"**. The surveyor
  ties that to a geodetic elevation.
- Finished grade is taken as −2'-0" all round until there is a grading
  plan.

---

## 4. Brief for the engineer

### 4.1 The project

- A one-storey house, about 5 680 ft² heated on the main floor, with a
  full basement and an attached three-car garage.
- **Basement:**
  - a **13¼" ICF (8" concrete core)** basement with 12'-0" ceilings,
    3 321 ft² inside the walls;
  - the basement floor is 13'-9" below the main floor, and about 11'-9"
    of backfill stands against the walls.
- **Concrete inside the basement:**
  - an **indoor pool**: 15'-0" × 15'-0", 4'-6" of water;
  - a **raised spa** that spills into the pool;
  - a **stepped theater floor** with a 15" drop.
- **Exit stair:** an exterior stair runs from the basement up to the back
  yard, in a concrete areaway.
- **No basement:**
  - the rest of the main floor stands on frost walls over conditioned
    crawlspaces;
  - the porches stand on piers.
- **Roof:** hip roofs with engineered trusses.

### 4.2 Design criteria to establish

These come from **NBC(AE) 2023 Division B, Appendix C** for the site's
location, and from the geotechnical report. Sheet S0.1 has blanks for
them.

| Item | Value |
|---|---|
| Location / nearest listed place, climate zone (7A/7B), heating degree-days | ____ |
| Ground snow load S<sub>s</sub>, rain load S<sub>r</sub> | ____ |
| Hourly wind pressure q<sub>1/50</sub> | ____ |
| Seismic S<sub>a</sub>(0.2), site class | ____ |
| Frost penetration (minimum footing depth 1.2 m in Alberta) | ____ |
| Bearing capacity at the footing level, about 13'-5" below grade | ____ |
| Groundwater level, especially against the pool pit 18'-3" down | ____ |
| Sulphate exposure class, for the concrete | ____ |
| Lateral earth pressure of the backfill | ____ |

### 4.3 Elements that need engineered design

| # | Element | Where | Notes |
|---|---|---|---|
| E1 | **ICF basement walls** | S1.0, A5.0 | About 13'-0" tall with 11'-9" of backfill. That is past the prescriptive ICF tables. Needs reinforcement, and lintels over the exit door and the two windows |
| E2 | **Top of the ICF walls** | A5.0 | The main floor holds the wall tops against the soil. The floor deck and the sill connection have to carry that load, including where the stair opening interrupts the floor and along the long pool-room wall |
| E3 | **Footings** | S1.0 | Perimeter footings 24" × 10". Interior bearing lines on 20" strips. Steps in the footings where the pool room's footings go deeper |
| E4 | **Pool and spa shells** | S1.0, A5.1 | Full of water and empty. Soil and groundwater pressure from outside. Uplift when empty. The deepened footings round the pool room, or a shell designed to hold up the footings instead |
| E5 | **Theater depressed slab** | A5.1 | The 7½" step and the 15" front tier, with thickened edges |
| E6 | **Exit stair areaway and light wells** | A5.1 | 8" retaining walls with 11'-9" and 8'-0" of soil |
| E7 | **Main floor framing** | S1.1 | The truss layout and spans. The two added supports. The stair opening (4'-7½" × 11'-7⅝"). Posts and their footings |
| E8 | **Roof** | A1.3 | Hip trusses by the supplier. Girder-truss reactions traced down to the footings. Uplift and drift |
| E9 | **Lateral bracing** | — | Braced walls or shear walls on the main floor for wind and earthquake |
| E10 | **Garage** | S1.0 | Door headers 16'-0" and 9'-0", the slab, the frost walls |
| E11 | **Porches and deck** | S1.0 | Piers, beams and the guards' anchorage |

### 4.4 Questions for the engineer

1. Is an 8" ICF core enough for 13'-0" walls with 11'-9" of backfill, or
   does it need 10"? What bar sizes and spacing?
2. Should the pool-room footings go deeper (as drawn), or should the pool
   shell hold them up instead?
3. Does the groundwater allow a pit 18'-3" below grade? Is dewatering
   needed during construction? Is a drain loop and hydrostatic relief
   valve enough over the long term?
4. Interior bearing lines: strip footings (as drawn), or a thickened
   slab?
5. Will 18"-deep floor trusses work for the 26'-11" pool-room span?
   - At what spacing, and how stiff will the floor feel?
   - How should they be protected from the pool room's moist air?
6. How is the top of the ICF wall held where the stair opening and the
   exit door interrupt it?
7. Can the exit-stair and light-well walls cantilever on their own, or
   do they need ties back to the house?
8. What sulphate class and concrete mixes for the footings, the walls and
   the shells?
9. For the crawlspaces and the garage: frost walls (as drawn), or
   frost-protected shallow foundations?
10. Which pours and stages need your field review? Which letters of
    assurance will the permit office want?
11. The building area is over 600 m² (§1.1). Which path do you
    recommend?

### 4.5 Assumptions in the drawings

These are the designer's assumptions, all for the engineer to confirm or
change.

- **Concrete (CSA A23.1):**
  - footings and walls: the sulphate class from the geotech report, else
    N;
  - basement slab: N, 25–32 MPa;
  - garage slab: C-2, 32 MPa, air-entrained;
  - pool and spa: 35 MPa, w/cm 0.40, wet-mix shotcrete with a crystalline
    waterproofing admixture.

  The full reasoning is in
  [the redesign spec, §3.4 and §4.2](../house/Redesign-and-Spec-2026-11-02.md).
- **Reinforcement:** CSA G30.18 400W. The sizes are yours to set.
- **Slab:**
  - 4" thick, on a 10 mil sealed poly over 6" of clear stone;
  - the stone is the radon layer (NBC 9.13.4);
  - 2" of rigid insulation under it is recommended.
- **Frost walls:** 8" walls on 20" × 8" footings, with the bottom 4'-0"
  below grade.
- **Porch piers:** 12" piers on 24" bells, 4'-6" deep, or helical piles.
- **Main floor depth:** 1'-7½" from the top of the ICF wall to the top of
  the subfloor.

### 4.6 What we need back

- Stamped foundation drawings, or a design letter, covering E1–E6 and
  E10–E11.
- Framing: beam, post and header sizes (E7). The truss layout reviewed
  against the supports.
- The lateral design (E9).
- A schedule of field reviews, and the letters of assurance the permit
  office asks for.

---

## 5. Other people the project needs

| Who | For |
|---|---|
| **Alberta Land Surveyor** | Plot plan with setbacks, easements and the elevation datum; later, staking the house |
| **Geotechnical engineer** | Boreholes to below the pool pit: bearing capacity, groundwater, sulphates, backfill |
| **Energy advisor** | The NBC 9.36 compliance model (HOT2000), air-tightness tests |
| **Truss supplier** | Floor and roof truss layouts, engineered and stamped |
| **ICF supplier** | Engineered wall tables or the engineer's design; window and door bucks |
| **HVAC designer** | Heat loss and gain, HRV, the **pool dehumidifier**, combustion air for the fireplace if it burns fuel |
| **Pool contractor** | The shell (shotcrete), main drains, equipment, the hydrostatic relief valve |
| **Electrician** | Panel, alarms, pool and spa bonding and GFCI protection (Canadian Electrical Code, Section 68) |
| **Plumber, gas fitter** | Under-slab drains, sump, gas or propane |
| **Private sewage (PSDS) installer** | Site evaluation (test pits) and the system design; they take out the permit [P11][P12] |
| **Water well driller** | A licensed driller; household use doesn't need a water licence [P13] |
| **Electric utility or REA** | The power service from the road: transformer, route, meter location |
| **Gas utility or co-op, or a propane supplier** | Natural gas from the road, or the propane tank and its placement |
| **Internet provider** | Fibre over Alberta SuperNet if it reaches the road, or Starlink |

---

## 6. Alberta permit roadmap and checklist

Permits for building, electrical, gas, plumbing and private sewage are
issued by one of these [P10]:

- the municipality, if it is accredited;
- in a non-accredited area, an **accredited agency** working for the
  province.

The Alberta Safety Codes Authority's website has a tool that names the
agency for a property [P24]. The county's development permit is a
separate approval [P23].

| # | Step | Who | You need | Done |
|---|---|---|---|---|
| 1 | **Land and zoning:** the land-use district, setbacks, height limit, a **development permit**, the road approach | County / MD | Title, the plot plan, these drawings | ☐ |
| 2 | **Survey and geotech** on the real parcel | ALS, geotechnical engineer | — | ☐ |
| 3 | **Who builds:** a licensed builder (with warranty), or an **Owner Builder Authorization** [P4][P5][P6] | New Home Buyer Protection Office | Builder licence number or authorization | ☐ |
| 4 | **Design completed:** the engineer's drawings (§4.6), truss layouts, the **9.36 energy compliance** (Tier 1 is the minimum in Alberta) [P7][P8][P9] | Engineer, truss supplier, energy advisor | This package | ☐ |
| 5 | **Building permit** (the indoor pool is part of it) [P10][P15][P16] | Municipality or accredited agency | Site plan, floor plans, sections, elevations, foundation and engineering, truss layouts, 9.36 documents, step 3 | ☐ |
| 6 | **Electrical, gas and plumbing permits** | The contractors, or you where homeowner permits are allowed | — | ☐ |
| 7 | **Private sewage permit** [P11][P12] | Certified PSDS installer | Site evaluation per the 2021 Standard of Practice, Part 7 | ☐ |
| 8 | **Water well** [P13] | Licensed driller | Separation distances from the PSDS [P22] | ☐ |
| 8a | **Power, gas and internet**: apply for the power service early, because a rural connection can take months; natural gas service or a propane supplier; a fibre provider or Starlink | Electric utility or REA; gas utility, co-op or propane supplier; ISP | The site plan with the service route | ☐ |
| 9 | **Locate utilities** before any digging, at least 3 working days ahead [P14] | Utility Safety Partners (Click Before You Dig) | — | ☐ |
| 10 | **Inspections:** footings and foundation before backfill, framing, insulation and vapour barrier, final; each trade separately; the engineer's field reviews | Safety codes officers, engineer | — | ☐ |
| 11 | **Phase 2:** building, electrical and plumbing permits for the basement finish | Municipality or agency | Phase 2 drawings | ☐ |

---

## 7. Code flags in the current design

References are to the NBC(AE) 2023, Division B, unless noted. "Verify"
means check the article in the code itself; the summaries here come from
the sources listed.

| Item | Where | Reference | Status |
|---|---|---|---|
| Building area 626 m² against the 600 m² Part 9 limit | A0.0 | Div. A 1.3.3.3 [P2][P3] | **Decide (§1.1)** |
| Porch floors 610 mm above grade | A1.2 | 9.8.8.1 [P17] | Guards, or raise the grade to within 600 mm |
| Porch steps, 4 risers | A1.2 | 9.8.7 *verify* | Add handrails |
| Garage steps: 3 risers of 6", a 2'-4" landing at the door | A1.2 | 9.8.6 *verify* | Check the landing length against the door swing |
| Door between the garage and the house | A1.2, A6.0 | 9.10.13.15 *verify* | Self-closing and weatherstripped (in the schedule) |
| Garage walls and ceiling next to the house | — | 9.10.9.16 *verify* | Gas-proofed: sealed drywall, taped joints, sealed penetrations |
| Smoke alarms | all floors | 9.10.19 *verify* | In each bedroom, outside the bedrooms, on each storey; hard-wired and interconnected |
| CO alarms | near the bedrooms | 9.32.3.9 *verify* [P20] | Required: the garage is attached, and any fuel-burning appliance |
| Foam plastic (the ICF faces) | basement | 9.10.17.10 [P18][P19] | A thermal barrier (e.g. ½" gypsum) over all interior foam **in Phase 1** |
| Radon | slab | 9.13.4 | Sealed poly, the clear-stone layer, a capped pipe through the slab, in Phase 1. The pool pit and the theater pit connect to the main stone layer |
| Main stair | A5.1 | 9.8 | 7½" rise and 10½" run are within the limits. Headroom 1 993 mm against a 1 950 mm minimum. Width 1 286 mm: check whether a second handrail is required (9.8.7.1); the model has one on each side |
| Exit stair | A5.1 | 9.8 | 7.42" rise, 11" run, 4'-0" wide: handrails per 9.8.7.1 (both sides drawn). 42" guard round the areaway. A drain at the landing |
| Light wells | A5.1 | 9.8.8 | 42" guards (as drawn) or walkable grates. Drains |
| Bedroom windows | A6.0 | 9.9.10.1 | Bedroom 2 and the bunk room meet the 0.35 m², 380 mm minimum. No basement bedrooms, so no basement egress windows are needed |
| Fireplace | A1.2 | 9.22 or CSA B149.1 | Type to choose |
| Indoor pool | basement | Building and electrical permits [P15][P16] | Bonding and GFCI protection (CEC Section 68), mechanical dehumidification, protection of the envelope and trusses from moist air |
| Energy | all | 9.36, Tier 1 [P7] | The performance path with an energy advisor. The ICF walls help; the great room's glass counts against |
| Ventilation | all | 9.32 | An HRV for the principal ventilation |

---

## 8. Phase 1 rough-ins

These have to be in before the slab is poured. Then Phase 2 can be
interior work only.

- [ ] Under-slab drains and vents for **every** future basement fixture:
  - the two basement bathrooms and the pool bath;
  - the laundry;
  - the dog wash in the pet room;
  - floor drains in the mechanical room, the laundry and the pool room.
- [ ] The **sump** (the utility room is suggested) for the weeping tile,
  and a second sump or ejector for the pool pit's drain loop.
- [ ] The **radon pipe**: capped through the slab into the stone layer.
  - Connect the theater and pool pit stone layers to the main layer.
- [ ] **Pool and spa:**
  - main drains (two each, anti-entrapment);
  - returns, skimmer and spillway piping to the equipment room;
  - the **hydrostatic relief valve**;
  - the bonding grid.
- [ ] **Conduits** under the slab or in the ICF for:
  - the theater's power, data and speakers;
  - the music room;
  - the pool equipment.
- [ ] **Service entries on the west side**, by the UTILITY room:
  - sleeves for power, water, gas and fibre;
  - one spare sleeve for the future buried lines to the shop.
- [ ] **Window and door bucks** in the ICF: the exit door and the two
  light-well windows.
- [ ] **Floor heat**, if it is wanted anywhere in the basement: tubing
  and insulation go in under the slab now.
- [ ] **Bearing walls, beams and posts** in the basement (S1.1),
  including the added bearing wall at x = 42.65.
- [ ] **Thermal barrier** over all of the ICF foam inside, and the
  basement smoke and CO alarms, before occupancy.

---

## 9. Changes to the model with this package

- **Roof over the main hall.** The kitchen roof block now runs north to
  y = 35.46 ft. It covers the main hall, which no roof block covered
  before; a gap of about 3 ft had shown between the eaves.
  - That block's ridge is now about 20'-0" above the main floor (22'-0"
    above grade), the highest on the house.
- **Sun room and patio** (Nov 3).
  - The north room beside the study is the **sun room**, not a sitting
    room. It gets tall windows to the north and beside its patio doors.
  - The old "breakfast nook" is an open, **covered patio** at floor
    level. It has no walls, posts at its open corner, a 42" guard over
    the exit stair's areaway, and it continues straight onto the deck.
  - The hall's north wall and the sun room's east wall are now outside
    walls.
  - The building area drops by about 18 m² (§1.1).
- **Site** (Nov 3). The site model now builds the house first (§2). The
  shop and its drives are a later phase. The utility tunnel is gone.
- **Septic west, well east** (Nov 3, later).
  - The septic tank is now by the basement UTILITY room, with its field
    and a reserve area further west.
  - The well moves to the east side.
  - The distances follow the Standard of Practice 2021 table (§2.1),
    replacing my 30 m rule.
- **Steps as tables.** The porch and garage steps are now tables,
  `main_porch_steps()` and `garage_steps()`, so the drawings can read
  them.
- **New files:**
  - `models/export.scad` echoes every table;
  - `tools/model_data.py` reads them;
  - `tools/make_drawings.py` draws the set.

---

## Sources

Sources for the stair, radon, concrete and pool specifications are
listed in
[the redesign spec](../house/Redesign-and-Spec-2026-11-02.md#sources).

- [P1] Alberta.ca, codes in force (NBC(AE) 2023 in force May 1, 2024): <https://www.alberta.ca/building-codes-and-standards>
- [P2] National Research Council, *National Building Code – 2023 Alberta Edition*: <https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada/codes-canada-publications/national-building-code-2023-alberta-edition>
- [P3] Greater Sudbury, "Does my project fall under Part 9 or Part 3?" (the same 600 m² rule, Div. A 1.3.3.3): <https://www.greatersudbury.ca/live/building-and-renovating/frequently-asked-questions/does-my-project-fall-under-part-9-or-part-3-of-the-building-code/>
- [P4] Alberta.ca, Owner Builder Authorization: <https://www.alberta.ca/owner-builder-authorization>
- [P5] Alberta.ca, builder licensing: <https://www.alberta.ca/builder-licensing.aspx>
- [P6] Alberta.ca, new home warranty overview: <https://alberta.ca/new-home-warranty-overview>
- [P7] Alberta Municipal Affairs, STANDATA 23-BCB-001 (Tier 1 energy efficiency): <https://open.alberta.ca/dataset/5cd7e000-4f7c-4188-b26f-11a16bbe43f8/resource/37c27a63-3517-4b03-b4e2-bd2733219caa/download/ma-standata-bulletin-building-23-bcb-001-2024-04.pdf>
- [P8] City of Edmonton, NBC(AE) 9.36 Energy Efficiency Requirements Guide: <https://www.edmonton.ca/sites/default/files/public-files/NBC_AE_9.36_Energy_Efficiency_Requirements_Guide.pdf>
- [P9] BILD Alberta, 2023 NBC(AE) Tier 1: <https://bildalberta.ca/wp-content/uploads/2024/04/2023-NBCAE-Tier-1.pdf>
- [P10] Alberta.ca, permits and Alberta's safety codes system: <https://www.alberta.ca/permits-and-albertas-safety-code-system>
- [P11] Alberta.ca, private sewage codes and standards: <https://www.alberta.ca/private-sewage-codes-and-standards.aspx>
- [P12] Municipal Affairs notice, Alberta Private Sewage Systems Standard of Practice 2021: <https://open.alberta.ca/dataset/a990f2f9-756f-474b-8671-cb14acdc516a/resource/f8642527-5be7-4556-90c1-b8bcc6e8fea9/download/ma-notice-alberta-private-sewage-systems-standard-of-practice-2021.pdf>
- [P13] Alberta Environment, *Working Well* Issue 8, well owner responsibilities (household use, 1 250 m³/yr): <https://open.alberta.ca/dataset/09b71647-f9f5-45e0-9fa5-36276471f4fc/resource/d1939cdf-5a15-4b03-bb3b-478cc07b75da/download/issue8-wellownerresponsibilities-mar2017.pdf>
- [P14] Utility Safety Partners, Click Before You Dig: <https://utilitysafety.ca/wheres-the-line/click-before-you-dig>
- [P15] City of Medicine Hat, swimming pools and hot tubs (24" / 600 mm and deeper need a building permit): <https://www.medicinehat.ca/home-property-utilities/home-improvement/swimming-pools-hot-tubs/>
- [P16] City of St. Albert, pools, hot tubs and ponds: <https://stalbert.ca/city/approvals/development/pools/>
- [P17] Rocky View County, residential exterior guards (NBC(AE) 9.8.8.1): <https://www.rockyview.ca/Portals/0/Files/BuildingPlanning/Building/Guideline-Residential-Exterior-Guards.pdf>
- [P18] Rocky View County, spray foam insulation guideline (thermal barriers): <https://www.rockyview.ca/Portals/0/Files/BuildingPlanning/Building/Guideline-Spray-Foam-Insulation.pdf>
- [P19] Construction Canada, "Thermal barriers and the protection of foamed plastic": <https://www.constructioncanada.net/thermal-barriers-and-the-protection-of-foamed-plastic/>
- [P20] Alberta Municipal Affairs safety tips, carbon monoxide alarms: <https://open.alberta.ca/dataset/89e3f4bb-8b57-4c3c-9d3c-2e1dad9bf4af/resource/2b43665f-d5a7-40ae-925f-7f78990b024a/download/safetytips-coalarms.pdf>
- [P21] APEGA, engineers and geoscientists in Alberta: <https://www.apega.ca>
- [P22] Alberta Municipal Affairs safety tips, private sewage separation distances: <https://open.alberta.ca/dataset/b8c07f17-395d-4580-8a7f-45b395bc5b2d/resource/616e6f01-a2f1-4224-9ab0-88ffbc46aa20/download/2012-safety-tips-private-sewage-treatment-systems-separation-distances-september-2012.pdf>
- [P23] Municipal District of Greenview, accredited agencies (a development permit is not a building permit): <https://mdgreenview.ab.ca//standard-document/alberta-municipal-affairs-approved-accredited-agencies>
- [P24] County of Northern Lights, safety code permits (finding the accredited agency through the Alberta Safety Codes Authority): <https://www.countyofnorthernlights.com/business-and-development/development/safety-code-permits>
- [P25] Leduc County, private sewage separation distances under the 2021 Standard of Practice (tanks 10 m and mounds 15 m from a water source or well): <https://www.leduc-county.com/public/download/files/353332>
- [P26] Lamont County, private sewage separation distances: <https://lamontcounty.ca/public/download/files/186489>. The full table above is as published by Alberta counties and the accredited agency Superior Safety Codes from the 2021 Standard of Practice. The Standard itself is a licensed document; confirm the numbers with the installer.
