# Plan facts (variant mode)

main = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/main_floor_a.scad`, basement = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/basement_a.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/main_floor_a.scad`; basement = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/basement_a.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 5,486 | 5486.2; excl. stair opening 5432.4 |
| Building area, centre lines (house + attached garage) | 564.4 m2 | 6075 sq ft |
| Building area, outside face | 584.5 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Circulation % (strict / with foyer) | 16.6% / 22.2% | 909 sq ft strict of 5486 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 23 | type `door` rows, by opening width |
| Double / open counts (main) | 12 / 2 | type `double` / type `open` |
| Minimum hall clear width | 4.71 ft (HALL @22.1,48.64) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 1.15 ft ((suite entry, 2nd piece)) |
| Wet-wall groups (main / basement) | 15 / 8 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 1 of 15 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 1019.2 ft | alternate exit (22.16, 38.9): 866.1 ft |
| Water heater -> furthest fixture (main / basement) | 119.8 ft (toilet/tub/wash basin (MASTER BATH)) / 84.8 ft (toilet/tub/wash basin (POOL BATH)) | water heater at (30.1, 36.8); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 102.6 ft, MASTER LAUNDRY: 42.9 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 2 | 2 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 4:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | SCULLERY: 8.7 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(garage 11.2) W(porch/patio 3.1, yard 9.6) ;; BUNK ROOM: N(yard 15.1) E(yard 3.2) W(yard 4.6) ;; MASTER BEDROOM: N(porch/patio 18.4) E(porch/patio 23.4) W(porch/patio 4.7) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(porch/patio 18.4) S(porch/patio 1.7, yard 26.7) E(porch/patio 23.4, yard 11.2) W(porch/patio 4.7) | suite rooms: MASTER BEDROOM, (master entry), WIC @95.95,20.56, (closet passage), WIC @111.8,20.56, MASTER BATH, WC @99.7,16.71, (linen between the WCs), WC @99.7,9.31 |
| Living-kind rooms with S exposure | DEN (14.8 ft); (den alcove) (3.8 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 4: SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); BREAKFAST (S/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42.65..47.27, y 47.1; basement foot room x 42.65..47.27, y 27.6; **moved** (x offset +0.00/+0.00 ft, run 19.500 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 9.3 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_a.scad (defaults): 52 rooms, 56 doors, 17 windows - OK ; basement_a.scad (defaults): 19 rooms, 19 doors, 2 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 5486.2 | computed: sum (x1-x0)*(y1-y0) over 38 rows, main_floor.scad:72-129 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 53.8 | option-a-evolve-current/main_floor_a.scad:89 |
| Main-floor conditioned excluding the stair opening | 5432.4 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 5486.2 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 3475.0 | computed over basement.scad:60-79 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 589.3 | option-a-evolve-current/main_floor_a.scad:72 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| SIDE ENTRY | 83.7 | option-a-evolve-current/main_floor_a.scad:73 |
| PATIO | 193.4 | option-a-evolve-current/main_floor_a.scad:97 |
| FRONT PORCH | 796.1 | option-a-evolve-current/main_floor_a.scad:119 |
| (unlabelled porch) @49.24,0 | 30.5 | option-a-evolve-current/main_floor_a.scad:120 |
| (unlabelled porch) @95.95,0 | 50.8 | option-a-evolve-current/main_floor_a.scad:121 |
| (covered entry) | 44.6 | option-a-evolve-current/main_floor_a.scad:122 |
| DECK | 322.4 | option-a-evolve-current/main_floor_a.scad:123 |
| OFFICE PORCH | 146.9 | option-a-evolve-current/main_floor_a.scad:124 |
| MASTER PORCH | 175.1 | option-a-evolve-current/main_floor_a.scad:125 |
| SIDE PORCH | 320.3 | option-a-evolve-current/main_floor_a.scad:126 |
| (unlabelled porch) @128.13,26.84 | 25.4 | option-a-evolve-current/main_floor_a.scad:127 |
| (study stoop) | 14.6 | option-a-evolve-current/main_floor_a.scad:128 |
| (garage side-door pad) | 17.5 | option-a-evolve-current/main_floor_a.scad:129 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 2221.3 sq ft. PATIO alone: 193.4; DECK alone: 322.4. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 395.5 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 138.3 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 225.4 ft | same |
|   facing garage | 31.7 ft | same (garage is unheated) |
| Outside (convex) corners | 17 | vertices of the union polygon after 0.02 ft simplify (30 vertices) |
| Inside (reflex) corners | 13 | same polygon |
| Bounding box, heated rooms | x 7.27..128.13 (120.86 ft), y 0..66.64 (66.64 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..137.66 (137.66 ft), y -15.26..66.64 (81.9 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 16 hip-roof blocks in main_roof (main_floor.scad:331); each hip block is 4 sloped facets, so 4 x 16 = 64 nominal facets before overlapping blocks merge; 9 blocks at 6/12 pitch, 7 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| SCULLERY | S 11.3 (porch/patio (open)); W 8.7 (garage) | option-a-evolve-current/main_floor_a.scad:74 |
| MUDROOM | S 2.2 (garage) | option-a-evolve-current/main_floor_a.scad:75 |
| LAUNDRY | none | option-a-evolve-current/main_floor_a.scad:76 |
| BEDROOM 2 | S 11.2 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) | option-a-evolve-current/main_floor_a.scad:78 |
| WIC @18.5,35.46 | S 3.6 (garage) | option-a-evolve-current/main_floor_a.scad:79 |
| (suite entry) | none | option-a-evolve-current/main_floor_a.scad:80 |
| (suite entry, 2nd piece) | none | option-a-evolve-current/main_floor_a.scad:81 |
| WC @7.27,48.13 | W 7.2 (yard/soil) | option-a-evolve-current/main_floor_a.scad:82 |
| BATH 2 | N 10.2 (yard/soil); W 6.7 (yard/soil) | option-a-evolve-current/main_floor_a.scad:83 |
| BUNK ROOM | N 15.1 (yard/soil); E 3.2 (yard/soil); W 4.6 (yard/soil) | option-a-evolve-current/main_floor_a.scad:84 |
| STUDY | N 4.6 (porch/patio (open)), 5.4 (yard/soil) | option-a-evolve-current/main_floor_a.scad:85 |
| HALL @22.1,48.64 | none | option-a-evolve-current/main_floor_a.scad:87 |
| (N-S hall, unlabelled) | none | option-a-evolve-current/main_floor_a.scad:88 |
| STAIR DN | none | option-a-evolve-current/main_floor_a.scad:89 |
| (landing at the stair top) | none | option-a-evolve-current/main_floor_a.scad:90 |
| (upper hall, west of its door) | none | option-a-evolve-current/main_floor_a.scad:91 |
| HALL @53.95,45.39 | N 15.2 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:92 |
| BATH | none | option-a-evolve-current/main_floor_a.scad:93 |
| FLEX ROOM | none | option-a-evolve-current/main_floor_a.scad:94 |
| SUN ROOM | N 11.3 (yard/soil); E 12.7 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:95 |
| HALL @24.34,29.51 | W 6.0 (garage) | option-a-evolve-current/main_floor_a.scad:98 |
| GREAT ROOM | N 26.5 (porch/patio (open)); E 4.4 (porch/patio (open)); W 1.8 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:100 |
| KITCHEN / DINING | S 4.9 (porch/patio (open)), 13.6 (yard/soil); W 7.4 (porch/patio (open)), 7.1 (yard/soil) | option-a-evolve-current/main_floor_a.scad:101 |
| BREAKFAST | S 15.0 (porch/patio (open)); E 3.7 (porch/patio (open)); W 6.3 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:102 |
| FOYER | S 12.0 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:103 |
| DEN | S 14.8 (porch/patio (open)); E 9.3 (porch/patio (open)); W 3.7 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:104 |
| (den alcove) | S 3.8 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:105 |
| OFFICE | N 13.0 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:107 |
| MASTER BEDROOM | N 18.4 (porch/patio (open)); E 23.4 (porch/patio (open)); W 4.7 (porch/patio (open)) | option-a-evolve-current/main_floor_a.scad:108 |
| (master entry) | none | option-a-evolve-current/main_floor_a.scad:109 |
| WIC @95.95,20.56 | none | option-a-evolve-current/main_floor_a.scad:110 |
| (closet passage) | none | option-a-evolve-current/main_floor_a.scad:111 |
| WIC @111.8,20.56 | none | option-a-evolve-current/main_floor_a.scad:112 |
| MASTER LAUNDRY | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) | option-a-evolve-current/main_floor_a.scad:113 |
| MASTER BATH | S 21.6 (yard/soil); E 11.2 (yard/soil) | option-a-evolve-current/main_floor_a.scad:114 |
| WC @99.7,16.71 | none | option-a-evolve-current/main_floor_a.scad:115 |
| (linen between the WCs) | none | option-a-evolve-current/main_floor_a.scad:116 |
| WC @99.7,9.31 | S 1.7 (porch/patio (open)), 5.1 (yard/soil) | option-a-evolve-current/main_floor_a.scad:117 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SCULLERY | 24.34 | 20.82 | 35.6 | 29.51 | 11.26 x 8.69 | 10.9 x 8.3 | 98 | 90 | 1.30 | utility | 12 | option-a-evolve-current/main_floor_a.scad:74 |
| MUDROOM | 22.1 | 35.46 | 37.3 | 40.56 | 15.20 x 5.10 | 14.8 x 4.7 | 78 | 70 | 2.98 | utility | 10 | option-a-evolve-current/main_floor_a.scad:75 |
| LAUNDRY | 22.1 | 40.56 | 37.3 | 48.64 | 15.20 x 8.08 | 14.8 x 7.7 | 123 | 114 | 1.88 | utility | 10 | option-a-evolve-current/main_floor_a.scad:76 |
| BEDROOM 2 | 7.27 | 35.46 | 18.5 | 48.13 | 11.23 x 12.67 | 10.8 x 12.3 | 142 | 133 | 1.13 | bed | 10 | option-a-evolve-current/main_floor_a.scad:78 |
| WIC @18.5,35.46 | 18.5 | 35.46 | 22.1 | 48.13 | 3.60 x 12.67 | 3.2 x 12.3 | 46 | 39 | 3.52 | closet | 10 | option-a-evolve-current/main_floor_a.scad:79 |
| (suite entry) | 13.78 | 48.13 | 22.1 | 53.75 | 8.32 x 5.62 | 7.9 x 5.2 | 47 | 41 | 1.48 | hall | 10 | option-a-evolve-current/main_floor_a.scad:80 |
| (suite entry, 2nd piece) | 13.78 | 53.75 | 17.5 | 55.3 | 3.72 x 1.55 | 3.3 x 1.1 | 6 | 4 | 2.40 | hall | 0 | option-a-evolve-current/main_floor_a.scad:81 |
| WC @7.27,48.13 | 7.27 | 48.13 | 13.78 | 55.3 | 6.51 x 7.17 | 6.1 x 6.8 | 47 | 41 | 1.10 | bath | 10 | option-a-evolve-current/main_floor_a.scad:82 |
| BATH 2 | 7.27 | 55.3 | 17.5 | 62.04 | 10.23 x 6.74 | 9.8 x 6.3 | 69 | 62 | 1.52 | bath | 10 | option-a-evolve-current/main_floor_a.scad:83 |
| BUNK ROOM | 17.5 | 53.75 | 32.6 | 66.64 | 15.10 x 12.89 | 14.7 x 12.5 | 195 | 184 | 1.17 | bed | 10 | option-a-evolve-current/main_floor_a.scad:84 |
| STUDY | 32.6 | 53.75 | 42.65 | 63.42 | 10.05 x 9.67 | 9.6 x 9.3 | 97 | 89 | 1.04 | office | 10 | option-a-evolve-current/main_floor_a.scad:85 |
| HALL @22.1,48.64 | 22.1 | 48.64 | 37.3 | 53.75 | 15.20 x 5.11 | 14.8 x 4.7 | 78 | 70 | 2.97 | hall | 10 | option-a-evolve-current/main_floor_a.scad:87 |
| (N-S hall, unlabelled) | 37.3 | 35.46 | 42.65 | 53.75 | 5.35 x 18.29 | 5.0 x 17.9 | 98 | 89 | 3.42 | hall | 10 | option-a-evolve-current/main_floor_a.scad:88 |
| STAIR DN | 42.65 | 35.46 | 47.27 | 47.1 | 4.62 x 11.64 | 4.2 x 11.2 | 54 | - | 2.52 | stairwell | 0 | option-a-evolve-current/main_floor_a.scad:89 |
| (landing at the stair top) | 42.65 | 47.1 | 47.27 | 50.69 | 4.62 x 3.59 | 4.2 x 3.2 | 17 | 13 | 1.29 | hall | 0 | option-a-evolve-current/main_floor_a.scad:90 |
| (upper hall, west of its door) | 47.27 | 45.39 | 53.95 | 50.69 | 6.68 x 5.30 | 6.3 x 4.9 | 35 | 31 | 1.26 | hall | 10 | option-a-evolve-current/main_floor_a.scad:91 |
| HALL @53.95,45.39 | 53.95 | 45.39 | 69.14 | 50.69 | 15.19 x 5.30 | 14.8 x 4.9 | 81 | 72 | 2.87 | hall | 10 | option-a-evolve-current/main_floor_a.scad:92 |
| BATH | 47.27 | 35.46 | 53.95 | 45.39 | 6.68 x 9.93 | 6.3 x 9.5 | 66 | 60 | 1.49 | bath | 10 | option-a-evolve-current/main_floor_a.scad:93 |
| FLEX ROOM | 53.95 | 35.46 | 69.14 | 45.39 | 15.19 x 9.93 | 14.8 x 9.5 | 151 | 141 | 1.53 | office | 10 | option-a-evolve-current/main_floor_a.scad:94 |
| SUN ROOM | 42.65 | 50.69 | 53.95 | 63.42 | 11.30 x 12.73 | 10.9 x 12.3 | 144 | 134 | 1.13 | living | 10 | option-a-evolve-current/main_floor_a.scad:95 |
| HALL @24.34,29.51 | 24.34 | 29.51 | 105.2 | 35.46 | 80.86 x 5.95 | 80.5 x 5.5 | 481 | 447 | 13.59 | hall | 10 | option-a-evolve-current/main_floor_a.scad:98 |
| GREAT ROOM | 69.14 | 35.46 | 95.63 | 52.53 | 26.49 x 17.07 | 26.1 x 16.7 | 452 | 435 | 1.55 | living | 12 | option-a-evolve-current/main_floor_a.scad:100 |
| KITCHEN / DINING | 35.6 | 6.28 | 69.14 | 29.51 | 33.54 x 23.23 | 33.1 x 22.8 | 779 | 757 | 1.44 | kitchen | 12 | option-a-evolve-current/main_floor_a.scad:101 |
| BREAKFAST | 54.1 | 0 | 69.14 | 6.28 | 15.04 x 6.28 | 14.6 x 5.9 | 94 | 86 | 2.39 | dining | 10 | option-a-evolve-current/main_floor_a.scad:102 |
| FOYER | 69.14 | 3.72 | 81.12 | 29.51 | 11.98 x 25.79 | 11.6 x 25.4 | 309 | 294 | 2.15 | hall | 12 | option-a-evolve-current/main_floor_a.scad:103 |
| DEN | 81.12 | 0 | 95.95 | 29.51 | 14.83 x 29.51 | 14.4 x 29.1 | 438 | 420 | 1.99 | living | 12 | option-a-evolve-current/main_floor_a.scad:104 |
| (den alcove) | 95.95 | 9.31 | 99.7 | 20.56 | 3.75 x 11.25 | 3.4 x 10.8 | 42 | 36 | 3.00 | living | 10 | option-a-evolve-current/main_floor_a.scad:105 |
| OFFICE | 95.63 | 35.46 | 108.62 | 48.16 | 12.99 x 12.70 | 12.6 x 12.3 | 165 | 155 | 1.02 | office | 10 | option-a-evolve-current/main_floor_a.scad:107 |
| MASTER BEDROOM | 108.62 | 29.51 | 126.97 | 52.86 | 18.35 x 23.35 | 17.9 x 22.9 | 428 | 412 | 1.27 | bed | 10 | option-a-evolve-current/main_floor_a.scad:108 |
| (master entry) | 105.2 | 29.51 | 108.62 | 35.46 | 3.42 x 5.95 | 3.0 x 5.5 | 20 | 17 | 1.74 | hall | 10 | option-a-evolve-current/main_floor_a.scad:109 |
| WIC @95.95,20.56 | 95.95 | 20.56 | 106.51 | 29.51 | 10.56 x 8.95 | 10.2 x 8.6 | 95 | 87 | 1.18 | closet | 10 | option-a-evolve-current/main_floor_a.scad:110 |
| (closet passage) | 106.51 | 20.56 | 111.8 | 29.51 | 5.29 x 8.95 | 4.9 x 8.6 | 47 | 42 | 1.69 | hall | 10 | option-a-evolve-current/main_floor_a.scad:111 |
| WIC @111.8,20.56 | 111.8 | 20.56 | 121.94 | 29.51 | 10.14 x 8.95 | 9.7 x 8.6 | 91 | 83 | 1.13 | closet | 10 | option-a-evolve-current/main_floor_a.scad:112 |
| MASTER LAUNDRY | 121.94 | 20.56 | 128.13 | 29.51 | 6.19 x 8.95 | 5.8 x 8.6 | 55 | 50 | 1.45 | utility | 10 | option-a-evolve-current/main_floor_a.scad:113 |
| MASTER BATH | 106.51 | 9.31 | 128.13 | 20.56 | 21.62 x 11.25 | 21.2 x 10.8 | 243 | 230 | 1.92 | bath | 10 | option-a-evolve-current/main_floor_a.scad:114 |
| WC @99.7,16.71 | 99.7 | 16.71 | 106.51 | 20.56 | 6.81 x 3.85 | 6.4 x 3.4 | 26 | 22 | 1.77 | bath | 10 | option-a-evolve-current/main_floor_a.scad:115 |
| (linen between the WCs) | 99.7 | 13.09 | 106.51 | 16.71 | 6.81 x 3.62 | 6.4 x 3.2 | 25 | 21 | 1.88 | closet | 10 | option-a-evolve-current/main_floor_a.scad:116 |
| WC @99.7,9.31 | 99.7 | 9.31 | 106.51 | 13.09 | 6.81 x 3.78 | 6.4 x 3.4 | 26 | 22 | 1.80 | bath | 10 | option-a-evolve-current/main_floor_a.scad:117 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 11.25 | 24.34 | 35.46 | 24.34 x 24.21 | 23.9 x 23.8 | 589 | 570 | 1.01 | garage | 10 | option-a-evolve-current/main_floor_a.scad:72 |
| SIDE ENTRY | 24.34 | 13.39 | 35.6 | 20.82 | 11.26 x 7.43 | 11.3 x 7.4 (open) | 84 | - | 1.52 | porch | 0 | option-a-evolve-current/main_floor_a.scad:73 |
| PATIO | 53.95 | 50.69 | 69.14 | 63.42 | 15.19 x 12.73 | 15.2 x 12.7 (open) | 193 | - | 1.19 | porch | 0 | option-a-evolve-current/main_floor_a.scad:97 |
| FRONT PORCH | 49.24 | -15.26 | 101.41 | 0 | 52.17 x 15.26 | 52.2 x 15.3 (open) | 796 | - | 3.42 | porch | 0 | option-a-evolve-current/main_floor_a.scad:119 |
| (unlabelled porch) @49.24,0 | 49.24 | 0 | 54.1 | 6.28 | 4.86 x 6.28 | 4.9 x 6.3 (open) | 31 | - | 1.29 | porch | 0 | option-a-evolve-current/main_floor_a.scad:120 |
| (unlabelled porch) @95.95,0 | 95.95 | 0 | 101.41 | 9.31 | 5.46 x 9.31 | 5.5 x 9.3 (open) | 51 | - | 1.71 | porch | 0 | option-a-evolve-current/main_floor_a.scad:121 |
| (covered entry) | 69.14 | 0 | 81.12 | 3.72 | 11.98 x 3.72 | 12.0 x 3.7 (open) | 45 | - | 3.22 | porch | 0 | option-a-evolve-current/main_floor_a.scad:122 |
| DECK | 69.14 | 52.53 | 95.63 | 64.7 | 26.49 x 12.17 | 26.5 x 12.2 (open) | 322 | - | 2.18 | porch | 0 | option-a-evolve-current/main_floor_a.scad:123 |
| OFFICE PORCH | 95.63 | 48.16 | 108.62 | 59.47 | 12.99 x 11.31 | 13.0 x 11.3 (open) | 147 | - | 1.15 | porch | 0 | option-a-evolve-current/main_floor_a.scad:124 |
| MASTER PORCH | 108.62 | 52.86 | 126.97 | 62.4 | 18.35 x 9.54 | 18.3 x 9.5 (open) | 175 | - | 1.92 | porch | 0 | option-a-evolve-current/main_floor_a.scad:125 |
| SIDE PORCH | 126.97 | 29.51 | 137.66 | 59.47 | 10.69 x 29.96 | 10.7 x 30.0 (open) | 320 | - | 2.80 | porch | 0 | option-a-evolve-current/main_floor_a.scad:126 |
| (unlabelled porch) @128.13,26.84 | 128.13 | 26.84 | 137.66 | 29.51 | 9.53 x 2.67 | 9.5 x 2.7 (open) | 25 | - | 3.57 | porch | 0 | option-a-evolve-current/main_floor_a.scad:127 |
| (study stoop) | 36.6 | 63.42 | 41.2 | 66.6 | 4.60 x 3.18 | 4.6 x 3.2 (open) | 15 | - | 1.45 | porch | 0 | option-a-evolve-current/main_floor_a.scad:128 |
| (garage side-door pad) | 1.7 | 35.46 | 7.27 | 38.6 | 5.57 x 3.14 | 5.6 x 3.1 (open) | 17 | - | 1.77 | porch | 0 | option-a-evolve-current/main_floor_a.scad:129 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUSIC ROOM | 22.16 | 50.35 | 42.65 | 63.16 | 20.49 x 12.81 | 19.7 x 12.1 | 262 | 238 | 1.60 | living | 12 | option-a-evolve-current/basement_a.scad:60 |
| GYM | 42.65 | 45.34 | 54.14 | 63.16 | 11.49 x 17.82 | 10.7 x 17.1 | 205 | 183 | 1.55 | rec | 12 | option-a-evolve-current/basement_a.scad:61 |
| STORAGE | 22.16 | 42.77 | 37.37 | 50.35 | 15.21 x 7.58 | 14.5 x 7.2 | 115 | 104 | 2.01 | closet | 12 | option-a-evolve-current/basement_a.scad:62 |
| UTILITY | 22.16 | 35.08 | 37.37 | 42.77 | 15.21 x 7.69 | 14.5 x 6.9 | 117 | 100 | 1.98 | utility | 12 | option-a-evolve-current/basement_a.scad:63 |
| HALL @37.37,35.08 | 37.37 | 35.08 | 42.65 | 50.35 | 5.28 x 15.27 | 4.9 x 14.9 | 81 | 73 | 2.89 | hall | 12 | option-a-evolve-current/basement_a.scad:64 |
| STAIR UP | 42.65 | 27.6 | 47.27 | 45.34 | 4.62 x 17.74 | 4.2 x 17.3 | 82 | 73 | 3.84 | stair | 12 | option-a-evolve-current/basement_a.scad:65 |
| BATH @47.27,35.08 | 47.27 | 35.08 | 54.14 | 45.34 | 6.87 x 10.26 | 6.5 x 9.9 | 70 | 64 | 1.49 | bath | 12 | option-a-evolve-current/basement_a.scad:66 |
| HALLWAY | 35.27 | 27.6 | 42.65 | 35.08 | 7.38 x 7.48 | 6.6 x 7.1 | 55 | 47 | 1.01 | hall | 0 | option-a-evolve-current/basement_a.scad:67 |
| STAIR FOOT | 47.27 | 27.6 | 54.14 | 35.08 | 6.87 x 7.48 | 6.5 x 7.1 | 51 | 46 | 1.09 | hall | 0 | option-a-evolve-current/basement_a.scad:68 |
| LIVING ROOM | 35.27 | 5.79 | 54.14 | 27.6 | 18.87 x 21.81 | 18.1 x 21.1 | 412 | 382 | 1.16 | living | 10 | option-a-evolve-current/basement_a.scad:69 |
| HOME THEATER | 54.14 | 29.12 | 69.38 | 50.35 | 15.24 x 21.23 | 14.8 x 20.5 | 324 | 304 | 1.39 | tiered | 13.25 | option-a-evolve-current/basement_a.scad:70 |
| PET ROOM | 54.14 | 18.15 | 69.38 | 29.12 | 15.24 x 10.97 | 14.8 x 10.6 | 167 | 157 | 1.39 | utility | 12 | option-a-evolve-current/basement_a.scad:71 |
| POOL ROOM | 69.38 | 18.15 | 96.33 | 52.76 | 26.95 x 34.61 | 25.8 x 33.9 | 933 | 875 | 1.28 | pit | 12 | option-a-evolve-current/basement_a.scad:72 |
| POOL EQUIP. | 96.33 | 29.12 | 103.04 | 41.94 | 6.71 x 12.82 | 6.0 x 12.1 | 86 | 72 | 1.91 | utility | 12 | option-a-evolve-current/basement_a.scad:73 |
| POOL BATH | 96.33 | 18.15 | 103.04 | 29.12 | 6.71 x 10.97 | 6.0 x 10.6 | 74 | 63 | 1.63 | bath | 12 | option-a-evolve-current/basement_a.scad:74 |
| HALL @54.14,13.43 | 54.14 | 13.43 | 103.04 | 18.15 | 48.90 x 4.72 | 48.1 x 4.0 | 231 | 191 | 10.36 | hall | 12 | option-a-evolve-current/basement_a.scad:75 |
| BATH @54.14,5.79 | 54.14 | 5.79 | 67.4 | 13.43 | 13.26 x 7.64 | 12.9 x 6.9 | 101 | 89 | 1.74 | bath | 12 | option-a-evolve-current/basement_a.scad:76 |
| LAUNDRY | 67.4 | 5.79 | 81.68 | 13.43 | 14.28 x 7.64 | 13.5 x 6.9 | 109 | 93 | 1.87 | utility | 12 | option-a-evolve-current/basement_a.scad:77 |
| EXIT STAIR | 45.6 | 63.16 | 66.8 | 67.75 | 21.20 x 4.59 | 20.1 x 3.5 | 97 | - | 4.62 | stairwell | 0 | option-a-evolve-current/basement_a.scad:79 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (72, 3.72) x | 6.2 ft = 74.4 in | double | 1 | (covered entry) / FOYER | option-a-evolve-current/main_floor_a.scad:135 |
| M2 | (69.6, 3.72) x | 2 ft = 24 in | glass | - | (covered entry) / FOYER | option-a-evolve-current/main_floor_a.scad:136 |
| M3 | (78.6, 3.72) x | 2 ft = 24 in | glass | - | (covered entry) / FOYER | option-a-evolve-current/main_floor_a.scad:137 |
| M4 | (63.8, 0) x | 5 ft = 60 in | double | 1 | FRONT PORCH / BREAKFAST | option-a-evolve-current/main_floor_a.scad:138 |
| M5 | (37, 63.42) x | 3.75 ft = 45 in | double | 1 | STUDY / (study stoop) | option-a-evolve-current/main_floor_a.scad:139 |
| M6 | (99, 48.16) x | 6.5 ft = 78 in | double | 1 | OFFICE / OFFICE PORCH | option-a-evolve-current/main_floor_a.scad:140 |
| M7 | (114.1, 52.86) x | 6.05 ft = 72.6 in | double | 1 | MASTER BEDROOM / MASTER PORCH | option-a-evolve-current/main_floor_a.scad:141 |
| M8 | (2, 11.25) x | 16 ft = 192 in | garage | - | OUTSIDE / GARAGE | option-a-evolve-current/main_floor_a.scad:142 |
| M9 | (2.43, 35.46) x | 3 ft = 36 in | door | 1 | GARAGE / (garage side-door pad) | option-a-evolve-current/main_floor_a.scad:143 |
| M10 | (24.34, 16.1) y | 3 ft = 36 in | door | -1 | GARAGE / SIDE ENTRY | option-a-evolve-current/main_floor_a.scad:144 |
| M11 | (24.34, 31.9) y | 3 ft = 36 in | door | 1 | GARAGE / HALL @24.34,29.51 | option-a-evolve-current/main_floor_a.scad:146 |
| M12 | (24.34, 23.6) y | 3 ft = 36 in | door | 1 | GARAGE / SCULLERY | option-a-evolve-current/main_floor_a.scad:147 |
| M13 | (35.6, 23.3) y | 3 ft = 36 in | door | -1 | SCULLERY / KITCHEN / DINING | option-a-evolve-current/main_floor_a.scad:148 |
| M14 | (24.6, 35.46) x | 12.4 ft = 148.8 in | full | - | HALL @24.34,29.51 / MUDROOM | option-a-evolve-current/main_floor_a.scad:149 |
| M15 | (24.8, 40.56) x | 3 ft = 36 in | door | -1 | MUDROOM / LAUNDRY | option-a-evolve-current/main_floor_a.scad:150 |
| M16 | (25, 48.64) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @22.1,48.64 | option-a-evolve-current/main_floor_a.scad:151 |
| M17 | (22.1, 50) y | 3 ft = 36 in | door | -1 | (suite entry) / HALL @22.1,48.64 | option-a-evolve-current/main_floor_a.scad:153 |
| M18 | (14.1, 48.13) x | 4.2 ft = 50.4 in | full | - | BEDROOM 2 / (suite entry) | option-a-evolve-current/main_floor_a.scad:154 |
| M19 | (13.9, 53.75) x | 3.5 ft = 42 in | full | - | (suite entry) / (suite entry, 2nd piece) | option-a-evolve-current/main_floor_a.scad:155 |
| M20 | (14.3, 55.3) x | 3 ft = 36 in | door | -1 | (suite entry, 2nd piece) / BATH 2 | option-a-evolve-current/main_floor_a.scad:156 |
| M21 | (13.78, 50.6) y | 3 ft = 36 in | door | -1 | WC @7.27,48.13 / (suite entry) | option-a-evolve-current/main_floor_a.scad:157 |
| M22 | (18.5, 38.5) y | 4.4 ft = 52.8 in | open | - | BEDROOM 2 / WIC @18.5,35.46 | option-a-evolve-current/main_floor_a.scad:158 |
| M23 | (17.5, 56.2) y | 3 ft = 36 in | door | -1 | BATH 2 / BUNK ROOM | option-a-evolve-current/main_floor_a.scad:159 |
| M24 | (29.4, 53.75) x | 3 ft = 36 in | door | 1 | HALL @22.1,48.64 / BUNK ROOM | option-a-evolve-current/main_floor_a.scad:160 |
| M25 | (33, 53.75) x | 3 ft = 36 in | door | 1 | HALL @22.1,48.64 / STUDY | option-a-evolve-current/main_floor_a.scad:161 |
| M26 | (37.3, 49) y | 4.5 ft = 54 in | full | - | HALL @22.1,48.64 / (N-S hall, unlabelled) | option-a-evolve-current/main_floor_a.scad:162 |
| M27 | (37.6, 35.46) x | 4.8 ft = 57.6 in | full | - | HALL @24.34,29.51 / (N-S hall, unlabelled) | option-a-evolve-current/main_floor_a.scad:163 |
| M28 | (42.65, 47.3) y | 3 ft = 36 in | door | 1 | (N-S hall, unlabelled) / (landing at the stair top) | option-a-evolve-current/main_floor_a.scad:165 |
| M29 | (42.9, 47.1) x | 4.1 ft = 49.2 in | full | - | STAIR DN / (landing at the stair top) | option-a-evolve-current/main_floor_a.scad:166 |
| M30 | (47.27, 47.3) y | 3.2 ft = 38.4 in | full | - | (landing at the stair top) / (upper hall, west of its door) | option-a-evolve-current/main_floor_a.scad:167 |
| M31 | (53.95, 45.75) y | 3 ft = 36 in | door | -1 | (upper hall, west of its door) / HALL @53.95,45.39 | option-a-evolve-current/main_floor_a.scad:168 |
| M32 | (69.14, 45.6) y | 4.9 ft = 58.8 in | full | - | HALL @53.95,45.39 / GREAT ROOM | option-a-evolve-current/main_floor_a.scad:169 |
| M33 | (70.65, 52.53) x | 6 ft = 72 in | double | -1 | GREAT ROOM / DECK | option-a-evolve-current/main_floor_a.scad:170 |
| M34 | (47.8, 45.39) x | 3 ft = 36 in | door | -1 | BATH / (upper hall, west of its door) | option-a-evolve-current/main_floor_a.scad:171 |
| M35 | (58.3, 45.39) x | 6.5 ft = 78 in | slider | - | FLEX ROOM / HALL @53.95,45.39 | option-a-evolve-current/main_floor_a.scad:172 |
| M36 | (47.5, 50.69) x | 5.9 ft = 70.8 in | double | 1 | (upper hall, west of its door) / SUN ROOM | option-a-evolve-current/main_floor_a.scad:173 |
| M37 | (53.95, 53.9) y | 4.9 ft = 58.8 in | double | 1 | SUN ROOM / PATIO | option-a-evolve-current/main_floor_a.scad:174 |
| M38 | (58.55, 50.69) x | 6 ft = 72 in | double | -1 | HALL @53.95,45.39 / PATIO | option-a-evolve-current/main_floor_a.scad:175 |
| M39 | (38.2, 29.51) x | 4 ft = 48 in | full | - | KITCHEN / DINING / HALL @24.34,29.51 | option-a-evolve-current/main_floor_a.scad:177 |
| M40 | (48.9, 29.51) x | 5.9 ft = 70.8 in | full | - | KITCHEN / DINING / HALL @24.34,29.51 | option-a-evolve-current/main_floor_a.scad:178 |
| M41 | (54.4, 6.28) x | 14.5 ft = 174 in | full | - | BREAKFAST / KITCHEN / DINING | option-a-evolve-current/main_floor_a.scad:179 |
| M42 | (71.4, 29.51) x | 7.9 ft = 94.8 in | full | - | FOYER / HALL @24.34,29.51 | option-a-evolve-current/main_floor_a.scad:180 |
| M43 | (69.4, 35.46) x | 26 ft = 312 in | full | - | HALL @24.34,29.51 / GREAT ROOM | option-a-evolve-current/main_floor_a.scad:181 |
| M44 | (81.12, 12.66) y | 5 ft = 60 in | double | 1 | FOYER / DEN | option-a-evolve-current/main_floor_a.scad:182 |
| M45 | (95.95, 9.6) y | 10.7 ft = 128.4 in | full | - | DEN / (den alcove) | option-a-evolve-current/main_floor_a.scad:183 |
| M46 | (99.3, 35.46) x | 4.7 ft = 56.4 in | double | 1 | HALL @24.34,29.51 / OFFICE | option-a-evolve-current/main_floor_a.scad:185 |
| M47 | (105.2, 29.95) y | 4.6 ft = 55.2 in | double | 1 | HALL @24.34,29.51 / (master entry) | option-a-evolve-current/main_floor_a.scad:186 |
| M48 | (108.62, 29.8) y | 5.4 ft = 64.8 in | full | - | (master entry) / MASTER BEDROOM | option-a-evolve-current/main_floor_a.scad:187 |
| M49 | (108.7, 29.51) x | 3 ft = 36 in | open | - | (closet passage) / MASTER BEDROOM | option-a-evolve-current/main_floor_a.scad:188 |
| M50 | (106.51, 23.6) y | 3 ft = 36 in | door | -1 | WIC @95.95,20.56 / (closet passage) | option-a-evolve-current/main_floor_a.scad:189 |
| M51 | (111.8, 23.6) y | 3 ft = 36 in | door | 1 | (closet passage) / WIC @111.8,20.56 | option-a-evolve-current/main_floor_a.scad:190 |
| M52 | (107.1, 20.56) x | 3 ft = 36 in | door | -1 | MASTER BATH / (closet passage) | option-a-evolve-current/main_floor_a.scad:191 |
| M53 | (122.3, 20.56) x | 3 ft = 36 in | door | 1 | MASTER BATH / MASTER LAUNDRY | option-a-evolve-current/main_floor_a.scad:192 |
| M54 | (106.51, 17) y | 3 ft = 36 in | door | -1 | WC @99.7,16.71 / MASTER BATH | option-a-evolve-current/main_floor_a.scad:193 |
| M55 | (106.51, 13.4) y | 3 ft = 36 in | door | -1 | (linen between the WCs) / MASTER BATH | option-a-evolve-current/main_floor_a.scad:194 |
| M56 | (106.51, 9.8) y | 3 ft = 36 in | door | -1 | WC @99.7,9.31 / MASTER BATH | option-a-evolve-current/main_floor_a.scad:195 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (38.4, 50.35) x | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / MUSIC ROOM | option-a-evolve-current/basement_a.scad:84 |
| B2 | (42.65, 46.2) y | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / GYM | option-a-evolve-current/basement_a.scad:85 |
| B3 | (37.37, 45.6) y | 2.8 ft = 33.6 in | door | -1 | STORAGE / HALL @37.37,35.08 | option-a-evolve-current/basement_a.scad:86 |
| B4 | (37.37, 38.4) y | 3 ft = 36 in | door | -1 | UTILITY / HALL @37.37,35.08 | option-a-evolve-current/basement_a.scad:87 |
| B5 | (37.6, 35.08) x | 4.8 ft = 57.6 in | full | - | HALLWAY / HALL @37.37,35.08 | option-a-evolve-current/basement_a.scad:88 |
| B6 | (47.27, 28) y | 4.2 ft = 50.4 in | full | - | STAIR UP / STAIR FOOT | option-a-evolve-current/basement_a.scad:89 |
| B7 | (49.2, 35.08) x | 2.8 ft = 33.6 in | door | 1 | STAIR FOOT / BATH @47.27,35.08 | option-a-evolve-current/basement_a.scad:90 |
| B8 | (54.14, 31.7) y | 3 ft = 36 in | door | -1 | STAIR FOOT / HOME THEATER | option-a-evolve-current/basement_a.scad:91 |
| B9 | (36, 27.6) x | 6.4 ft = 76.8 in | open | - | LIVING ROOM / HALLWAY | option-a-evolve-current/basement_a.scad:92 |
| B10 | (50, 27.6) x | 4 ft = 48 in | open | - | LIVING ROOM / STAIR FOOT | option-a-evolve-current/basement_a.scad:93 |
| B11 | (54.14, 13.8) y | 4 ft = 48 in | open | - | LIVING ROOM / HALL @54.14,13.43 | option-a-evolve-current/basement_a.scad:94 |
| B12 | (56.5, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / PET ROOM | option-a-evolve-current/basement_a.scad:95 |
| B13 | (71, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / POOL ROOM | option-a-evolve-current/basement_a.scad:96 |
| B14 | (96.33, 20.5) y | 2.8 ft = 33.6 in | door | 1 | POOL ROOM / POOL BATH | option-a-evolve-current/basement_a.scad:97 |
| B15 | (99, 18.15) x | 2.8 ft = 33.6 in | door | 1 | HALL @54.14,13.43 / POOL BATH | option-a-evolve-current/basement_a.scad:98 |
| B16 | (96.33, 33.5) y | 3 ft = 36 in | door | 1 | POOL ROOM / POOL EQUIP. | option-a-evolve-current/basement_a.scad:99 |
| B17 | (59, 13.43) x | 2.8 ft = 33.6 in | door | -1 | BATH @54.14,5.79 / HALL @54.14,13.43 | option-a-evolve-current/basement_a.scad:100 |
| B18 | (73, 13.43) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @54.14,13.43 | option-a-evolve-current/basement_a.scad:101 |
| B19 | (46.2, 63.16) x | 3.5 ft = 42 in | door | -1 | GYM / EXIT STAIR | option-a-evolve-current/basement_a.scad:102 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 23 | 23 |
| double | 0 | 0 | 12 | 12 |
| open | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 15 | 15 |
| slider | 0 | 0 | 1 | 1 |
| glass | 2 | 0 | 0 | 2 |
| garage | 0 | 0 | 1 | 1 |
| ALL | 2 | 0 | 54 | 56 |
| passage (door+double+slider+open) | 0 | 0 | 38 | 38 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 7 | 7 | 14 |
| open | 0 | 0 | 3 | 3 |
| full | 0 | 0 | 2 | 2 |
| ALL | 0 | 7 | 12 | 19 |
| passage (door+double+slider+open) | 0 | 7 | 10 | 17 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-a-evolve-current/main_floor_a.scad:141 | MASTER BEDROOM / MASTER PORCH | double | 72.6 in | - |
| option-a-evolve-current/main_floor_a.scad:154 | BEDROOM 2 / (suite entry) | full | 50.4 in | - |
| option-a-evolve-current/main_floor_a.scad:156 | (suite entry, 2nd piece) / BATH 2 | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:157 | WC @7.27,48.13 / (suite entry) | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:158 | BEDROOM 2 / WIC @18.5,35.46 | open | 52.8 in | - |
| option-a-evolve-current/main_floor_a.scad:159 | BATH 2 / BUNK ROOM | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:160 | HALL @22.1,48.64 / BUNK ROOM | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:171 | BATH / (upper hall, west of its door) | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:187 | (master entry) / MASTER BEDROOM | full | 64.8 in | - |
| option-a-evolve-current/main_floor_a.scad:188 | (closet passage) / MASTER BEDROOM | open | 36 in | - |
| option-a-evolve-current/main_floor_a.scad:189 | WIC @95.95,20.56 / (closet passage) | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:190 | (closet passage) / WIC @111.8,20.56 | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:191 | MASTER BATH / (closet passage) | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:192 | MASTER BATH / MASTER LAUNDRY | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:193 | WC @99.7,16.71 / MASTER BATH | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:194 | (linen between the WCs) / MASTER BATH | door | 36 in | 34.5 |
| option-a-evolve-current/main_floor_a.scad:195 | WC @99.7,9.31 / MASTER BATH | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-a-evolve-current/basement_a.scad:86 | STORAGE / HALL @37.37,35.08 | door | 33.6 in | 32.1 |
| option-a-evolve-current/basement_a.scad:90 | STAIR FOOT / BATH @47.27,35.08 | door | 33.6 in | 32.1 |
| option-a-evolve-current/basement_a.scad:97 | POOL ROOM / POOL BATH | door | 33.6 in | 32.1 |
| option-a-evolve-current/basement_a.scad:98 | HALL @54.14,13.43 / POOL BATH | door | 33.6 in | 32.1 |
| option-a-evolve-current/basement_a.scad:100 | BATH @54.14,5.79 / HALL @54.14,13.43 | door | 33.6 in | 32.1 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BUNK ROOM | N | (21.45, 66.64, 'x') | 3.5 | 2.5 | 5 | 17.5 | option-a-evolve-current/main_floor_a.scad:200 |
| BEDROOM 2 | W | (7.27, 36.3, 'y') | 5.4 | 2.75 | 5 | 27.0 | option-a-evolve-current/main_floor_a.scad:201 |
| BEDROOM 2 | W | (7.27, 42.3, 'y') | 5.4 | 2.75 | 5 | 27.0 | option-a-evolve-current/main_floor_a.scad:202 |
| SUN ROOM | N | (44.3, 63.42, 'x') | 7.4 | 1.5 | 6.5 | 48.1 | option-a-evolve-current/main_floor_a.scad:203 |
| SUN ROOM | E | (53.95, 59.3, 'y') | 3.6 | 1.5 | 6.5 | 23.4 | option-a-evolve-current/main_floor_a.scad:204 |
| GREAT ROOM | N | (77.8, 52.53, 'x') | 3.6 | 2 | 6 | 21.6 | option-a-evolve-current/main_floor_a.scad:205 |
| GREAT ROOM | N | (89.4, 52.53, 'x') | 4.3 | 2 | 6 | 25.8 | option-a-evolve-current/main_floor_a.scad:206 |
| MASTER BEDROOM | N | (110, 52.86, 'x') | 2.5 | 2.5 | 5 | 12.5 | option-a-evolve-current/main_floor_a.scad:207 |
| MASTER BEDROOM | E | (126.97, 46, 'y') | 4.7 | 2.5 | 5 | 23.5 | option-a-evolve-current/main_floor_a.scad:208 |
| MASTER BEDROOM | E | (126.97, 31, 'y') | 4 | 2.5 | 5 | 20.0 | option-a-evolve-current/main_floor_a.scad:209 |
| MASTER BATH | E | (128.13, 9.8, 'y') | 4.6 | 3.5 | 4 | 18.4 | option-a-evolve-current/main_floor_a.scad:210 |
| MASTER LAUNDRY | E | (128.13, 21.3, 'y') | 3.6 | 4 | 3 | 10.8 | option-a-evolve-current/main_floor_a.scad:211 |
| DEN | S | (84, 0, 'x') | 8 | 2.5 | 5.5 | 44.0 | option-a-evolve-current/main_floor_a.scad:212 |
| DEN | E | (95.95, 1.8, 'y') | 5.8 | 2.5 | 5.5 | 31.9 | option-a-evolve-current/main_floor_a.scad:213 |
| BREAKFAST | W | (54.1, 0.7, 'y') | 4.8 | 2 | 6 | 28.8 | option-a-evolve-current/main_floor_a.scad:214 |
| BREAKFAST | S | (54.6, 0, 'x') | 5.6 | 2 | 6 | 33.6 | option-a-evolve-current/main_floor_a.scad:215 |
| KITCHEN / DINING | S | (37.7, 6.28, 'x') | 7.5 | 3.5 | 4 | 30.0 | option-a-evolve-current/main_floor_a.scad:216 |

Total main-floor window glass (width x height): 443.9 sq ft (17 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 5, S: 3, E: 6, W: 3

Rooms with windows on 2+ walls (main): SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); BREAKFAST (S/W)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| SCULLERY | utility | 98 |
| MUDROOM | utility | 78 |
| LAUNDRY | utility | 123 |
| WIC @18.5,35.46 | closet | 46 |
| (suite entry) | hall | 47 |
| (suite entry, 2nd piece) | hall | 6 |
| WC @7.27,48.13 | bath | 47 |
| BATH 2 | bath | 69 |
| STUDY | office | 97 |
| HALL @22.1,48.64 | hall | 78 |
| (N-S hall, unlabelled) | hall | 98 |
| (landing at the stair top) | hall | 17 |
| (upper hall, west of its door) | hall | 35 |
| HALL @53.95,45.39 | hall | 81 |
| BATH | bath | 66 |
| FLEX ROOM | office | 151 |
| HALL @24.34,29.51 | hall | 481 |
| FOYER | hall | 309 |
| (den alcove) | living | 42 |
| OFFICE | office | 165 |
| (master entry) | hall | 20 |
| WIC @95.95,20.56 | closet | 95 |
| (closet passage) | hall | 47 |
| WIC @111.8,20.56 | closet | 91 |
| WC @99.7,16.71 | bath | 26 |
| (linen between the WCs) | closet | 25 |
| WC @99.7,9.31 | bath | 26 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| LIVING ROOM | S | (40, 5.79, 'x') | 8 | 4.5 | 4 | 32.0 | foundation.scad:160 |
| MUSIC ROOM | N | (33.15, 63.16, 'x') | 3 | 4.5 | 4 | 12.0 | foundation.scad:161 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: GYM (rec, 205 sf); STORAGE (closet, 115 sf); UTILITY (utility, 117 sf); HALL @37.37,35.08 (hall, 81 sf); STAIR UP (stair, 82 sf); BATH @47.27,35.08 (bath, 70 sf); HALLWAY (hall, 55 sf); STAIR FOOT (hall, 51 sf); HOME THEATER (tiered, 324 sf); PET ROOM (utility, 167 sf); POOL ROOM (pit, 933 sf); POOL EQUIP. (utility, 86 sf); POOL BATH (bath, 74 sf); HALL @54.14,13.43 (hall, 231 sf); BATH @54.14,5.79 (bath, 101 sf); LAUNDRY (utility, 109 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (suite entry) | 13.78,48.13 to 22.1,53.75 | 47 | 5.2 ft clear width (63 in), length 7.9 | option-a-evolve-current/main_floor_a.scad:80 |
| (suite entry, 2nd piece) | 13.78,53.75 to 17.5,55.3 | 6 | 1.1 ft clear width (14 in), length 3.3 | option-a-evolve-current/main_floor_a.scad:81 |
| HALL @22.1,48.64 | 22.1,48.64 to 37.3,53.75 | 78 | 4.7 ft clear width (57 in), length 14.8 | option-a-evolve-current/main_floor_a.scad:87 |
| (N-S hall, unlabelled) | 37.3,35.46 to 42.65,53.75 | 98 | 5.0 ft clear width (59 in), length 17.9 | option-a-evolve-current/main_floor_a.scad:88 |
| (landing at the stair top) | 42.65,47.1 to 47.27,50.69 | 17 | 3.2 ft clear width (38 in), length 4.2 | option-a-evolve-current/main_floor_a.scad:90 |
| (upper hall, west of its door) | 47.27,45.39 to 53.95,50.69 | 35 | 4.9 ft clear width (59 in), length 6.3 | option-a-evolve-current/main_floor_a.scad:91 |
| HALL @53.95,45.39 | 53.95,45.39 to 69.14,50.69 | 81 | 4.9 ft clear width (59 in), length 14.8 | option-a-evolve-current/main_floor_a.scad:92 |
| HALL @24.34,29.51 | 24.34,29.51 to 105.2,35.46 | 481 | 5.5 ft clear width (67 in), length 80.5 | option-a-evolve-current/main_floor_a.scad:98 |
| (master entry) | 105.2,29.51 to 108.62,35.46 | 20 | 3.0 ft clear width (36 in), length 5.5 | option-a-evolve-current/main_floor_a.scad:109 |
| (closet passage) | 106.51,20.56 to 111.8,29.51 | 47 | 4.9 ft clear width (59 in), length 8.6 | option-a-evolve-current/main_floor_a.scad:111 |

**Circulation total (halls only): 909 sq ft = 16.6% of 5486 sq ft conditioned** (16.7% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 309 | 11.6 ft | 22.2% | option-a-evolve-current/main_floor_a.scad:103 |
| MUDROOM | 78 | 4.7 ft | 23.6% (halls+foyer+mudroom) | option-a-evolve-current/main_floor_a.scad:75 |
| STAIR DN opening (stairwell) | 54 | 4.2 ft | 24.6% (all four) | option-a-evolve-current/main_floor_a.scad:89 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL @37.37,35.08 | 37.37,35.08 to 42.65,50.35 | 81 | 4.9 ft clear width (59 in), length 14.9 | option-a-evolve-current/basement_a.scad:64 |
| HALLWAY | 35.27,27.6 to 42.65,35.08 | 55 | 6.6 ft clear width (80 in), length 7.1 | option-a-evolve-current/basement_a.scad:67 |
| STAIR FOOT | 47.27,27.6 to 54.14,35.08 | 51 | 6.5 ft clear width (78 in), length 7.1 | option-a-evolve-current/basement_a.scad:68 |
| HALL @54.14,13.43 | 54.14,13.43 to 103.04,18.15 | 231 | 4.0 ft clear width (48 in), length 48.1 | option-a-evolve-current/basement_a.scad:75 |

**Circulation total (halls only): 418 sq ft = 12.0% of 3475 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 82 | 4.2 ft | 14.4% | option-a-evolve-current/basement_a.scad:65 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): STAIR DN <-> (landing at the stair top) (4.6 ft shared edge); PATIO <-> DECK (10.9 ft shared edge); FRONT PORCH <-> (unlabelled porch) @49.24,0 (4.9 ft shared edge); FRONT PORCH <-> (unlabelled porch) @95.95,0 (5.5 ft shared edge); FRONT PORCH <-> (covered entry) (12.0 ft shared edge); DECK <-> OFFICE PORCH (6.9 ft shared edge); OFFICE PORCH <-> MASTER PORCH (6.6 ft shared edge); MASTER PORCH <-> SIDE PORCH (6.6 ft shared edge); SIDE PORCH <-> (unlabelled porch) @128.13,26.84 (9.5 ft shared edge)

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | (garage side-door pad); HALL @24.34,29.51; SCULLERY; SIDE ENTRY | garage to outside (option-a-evolve-current/main_floor_a.scad:142) |
| SIDE ENTRY | porch, ceiling 0 (open zone) | GARAGE | - |
| SCULLERY | utility | GARAGE; KITCHEN / DINING | - |
| MUDROOM | utility | HALL @24.34,29.51; LAUNDRY | - |
| LAUNDRY | utility | HALL @22.1,48.64; MUDROOM | - |
| BEDROOM 2 | bed | (suite entry); WIC @18.5,35.46 | - |
| WIC @18.5,35.46 | closet | BEDROOM 2 | - |
| (suite entry) | hall | (suite entry, 2nd piece); BEDROOM 2; HALL @22.1,48.64; WC @7.27,48.13 | - |
| (suite entry, 2nd piece) | hall, ceiling 0 (open zone) | (suite entry); BATH 2 | - |
| WC @7.27,48.13 | bath | (suite entry) | - |
| BATH 2 | bath | (suite entry, 2nd piece); BUNK ROOM | - |
| BUNK ROOM | bed | BATH 2; HALL @22.1,48.64 | - |
| STUDY | office | (study stoop); HALL @22.1,48.64 | - |
| HALL @22.1,48.64 | hall | (N-S hall, unlabelled); (suite entry); BUNK ROOM; LAUNDRY; STUDY | - |
| (N-S hall, unlabelled) | hall | (landing at the stair top); HALL @22.1,48.64; HALL @24.34,29.51 | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (landing at the stair top) | - |
| (landing at the stair top) | hall, ceiling 0 (open zone) | (N-S hall, unlabelled); (upper hall, west of its door); STAIR DN | - |
| (upper hall, west of its door) | hall | (landing at the stair top); BATH; HALL @53.95,45.39; SUN ROOM | - |
| HALL @53.95,45.39 | hall | (upper hall, west of its door); FLEX ROOM; GREAT ROOM; PATIO | - |
| BATH | bath | (upper hall, west of its door) | - |
| FLEX ROOM | office | HALL @53.95,45.39 | - |
| SUN ROOM | living | (upper hall, west of its door); PATIO | - |
| PATIO | porch, ceiling 0 (open zone) | DECK; HALL @53.95,45.39; SUN ROOM | - |
| HALL @24.34,29.51 | hall | (N-S hall, unlabelled); (master entry); FOYER; GARAGE; GREAT ROOM; KITCHEN / DINING; MUDROOM; OFFICE | - |
| GREAT ROOM | living | DECK; HALL @24.34,29.51; HALL @53.95,45.39 | - |
| KITCHEN / DINING | kitchen | BREAKFAST; HALL @24.34,29.51; SCULLERY | - |
| BREAKFAST | dining | FRONT PORCH; KITCHEN / DINING | - |
| FOYER | hall | (covered entry); DEN; HALL @24.34,29.51 | - |
| DEN | living | (den alcove); FOYER | - |
| (den alcove) | living | DEN | - |
| OFFICE | office | HALL @24.34,29.51; OFFICE PORCH | - |
| MASTER BEDROOM | bed | (closet passage); (master entry); MASTER PORCH | - |
| (master entry) | hall | HALL @24.34,29.51; MASTER BEDROOM | - |
| WIC @95.95,20.56 | closet | (closet passage) | - |
| (closet passage) | hall | MASTER BATH; MASTER BEDROOM; WIC @111.8,20.56; WIC @95.95,20.56 | - |
| WIC @111.8,20.56 | closet | (closet passage) | - |
| MASTER LAUNDRY | utility | MASTER BATH | - |
| MASTER BATH | bath | (closet passage); (linen between the WCs); MASTER LAUNDRY; WC @99.7,16.71; WC @99.7,9.31 | - |
| WC @99.7,16.71 | bath | MASTER BATH | - |
| (linen between the WCs) | closet | MASTER BATH | - |
| WC @99.7,9.31 | bath | MASTER BATH | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | (covered entry); (unlabelled porch) @49.24,0; (unlabelled porch) @95.95,0; BREAKFAST | - |
| (unlabelled porch) @49.24,0 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (unlabelled porch) @95.95,0 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (covered entry) | porch, ceiling 0 (open zone) | FOYER; FRONT PORCH | - |
| DECK | porch, ceiling 0 (open zone) | GREAT ROOM; OFFICE PORCH; PATIO | - |
| OFFICE PORCH | porch, ceiling 0 (open zone) | DECK; MASTER PORCH; OFFICE | - |
| MASTER PORCH | porch, ceiling 0 (open zone) | MASTER BEDROOM; OFFICE PORCH; SIDE PORCH | - |
| SIDE PORCH | porch, ceiling 0 (open zone) | (unlabelled porch) @128.13,26.84; MASTER PORCH | - |
| (unlabelled porch) @128.13,26.84 | porch, ceiling 0 (open zone) | SIDE PORCH | - |
| (study stoop) | porch, ceiling 0 (open zone) | STUDY | - |
| (garage side-door pad) | porch, ceiling 0 (open zone) | GARAGE | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| MUSIC ROOM | living | HALL @37.37,35.08 | - |
| GYM | rec | EXIT STAIR; HALL @37.37,35.08 | - |
| STORAGE | closet | HALL @37.37,35.08 | - |
| UTILITY | utility | HALL @37.37,35.08 | - |
| HALL @37.37,35.08 | hall | GYM; HALLWAY; MUSIC ROOM; STORAGE; UTILITY | - |
| STAIR UP | stair | STAIR FOOT | - |
| BATH @47.27,35.08 | bath | STAIR FOOT | - |
| HALLWAY | hall, ceiling 0 (open zone) | HALL @37.37,35.08; LIVING ROOM | - |
| STAIR FOOT | hall, ceiling 0 (open zone) | BATH @47.27,35.08; HOME THEATER; LIVING ROOM; STAIR UP | - |
| LIVING ROOM | living | HALL @54.14,13.43; HALLWAY; STAIR FOOT | - |
| HOME THEATER | tiered | STAIR FOOT | - |
| PET ROOM | utility | HALL @54.14,13.43 | - |
| POOL ROOM | pit | HALL @54.14,13.43; POOL BATH; POOL EQUIP. | - |
| POOL EQUIP. | utility | POOL ROOM | - |
| POOL BATH | bath | HALL @54.14,13.43; POOL ROOM | - |
| HALL @54.14,13.43 | hall | BATH @54.14,5.79; LAUNDRY; LIVING ROOM; PET ROOM; POOL BATH; POOL ROOM | - |
| BATH @54.14,5.79 | bath | HALL @54.14,13.43 | - |
| LAUNDRY | utility | HALL @54.14,13.43 | - |
| EXIT STAIR | stairwell, ceiling 0 (open zone) | GYM | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 60.9 | FOYER > HALL @24.34,29.51 > KITCHEN / DINING |
| front door -> range (option-a-evolve-current/main_floor_a.scad:223) | 69.2 | FOYER > HALL @24.34,29.51 > KITCHEN / DINING |
| garage (room centre) -> kitchen/dining room centre | 41.7 | GARAGE > SCULLERY > KITCHEN / DINING |
| garage (room centre) -> range | 32.3 | GARAGE > SCULLERY > KITCHEN / DINING |
| garage (room centre) -> SCULLERY centre (no pantry room in model) | 17.9 | GARAGE > SCULLERY |
| garage (room centre) -> tall pantry cabinets in kitchen (option-a-evolve-current/main_floor_a.scad:227) | 34.2 | GARAGE > SCULLERY > KITCHEN / DINING |
| master bedroom centre -> WIC @95.95,20.56 centre | 25.0 | MASTER BEDROOM > (closet passage) > WIC @95.95,20.56 |
| master bedroom centre -> WIC @111.8,20.56 centre | 23.7 | MASTER BEDROOM > (closet passage) > WIC @111.8,20.56 |
| master bedroom centre -> LAUNDRY centre | 102.6 | MASTER BEDROOM > (master entry) > HALL @24.34,29.51 > MUDROOM > LAUNDRY |
| master bedroom centre -> MASTER LAUNDRY centre | 42.9 | MASTER BEDROOM > (closet passage) > MASTER BATH > MASTER LAUNDRY |
| BEDROOM 2 centre -> BATH 2 centre | 19.2 | BEDROOM 2 > (suite entry) > (suite entry, 2nd piece) > BATH 2 |
| BEDROOM 2 centre -> hall BATH centre | 48.8 | BEDROOM 2 > (suite entry) > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 129.3 | BEDROOM 2 > (suite entry) > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 24.3 | BEDROOM 2 > (suite entry) > HALL @22.1,48.64 > LAUNDRY |
| BEDROOM 2 centre -> MASTER LAUNDRY centre | 138.8 | BEDROOM 2 > (suite entry) > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH > MASTER LAUNDRY |
| BUNK ROOM centre -> BATH 2 centre | 13.2 | BUNK ROOM > BATH 2 |
| BUNK ROOM centre -> hall BATH centre | 35.3 | BUNK ROOM > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > BATH |
| BUNK ROOM centre -> MASTER BATH centre | 115.8 | BUNK ROOM > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BUNK ROOM centre -> LAUNDRY centre | 20.6 | BUNK ROOM > HALL @22.1,48.64 > LAUNDRY |
| BUNK ROOM centre -> MASTER LAUNDRY centre | 125.2 | BUNK ROOM > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH > MASTER LAUNDRY |
| foyer centre -> hall BATH centre (no powder room in model; nearest toilet room reachable from the foyer side) | 65.8 | FOYER > HALL @24.34,29.51 > GREAT ROOM > HALL @53.95,45.39 > (upper hall, west of its door) > BATH |
| front door -> top of main stair (top nosing, (44.96, 47.1)) | 78.1 | FOYER > HALL @24.34,29.51 > (N-S hall, unlabelled) > (landing at the stair top) |
| garage mud-entry door -> top of main stair (top nosing, (44.96, 47.1)) | 32.3 | HALL @24.34,29.51 > (N-S hall, unlabelled) > (landing at the stair top) |
| master bedroom centre -> top of main stair (top nosing, (44.96, 47.1)) | 82.4 | MASTER BEDROOM > (master entry) > HALL @24.34,29.51 > GREAT ROOM > HALL @53.95,45.39 > (upper hall, west of its door) > (landing at the stair top) |
| BEDROOM 2 centre -> top of main stair (top nosing, (44.96, 47.1)) | 37.9 | BEDROOM 2 > (suite entry) > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) |
| BUNK ROOM centre -> top of main stair (top nosing, (44.96, 47.1)) | 24.3 | BUNK ROOM > HALL @22.1,48.64 > (N-S hall, unlabelled) > (landing at the stair top) |
| basement stair foot (44.96, 27.6) -> UTILITY centre | 26.4 | LIVING ROOM > HALLWAY > HALL @37.37,35.08 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @95.95,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @95.95,20.56); WIC @111.8,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @111.8,20.56)

## Section 8

### 8.1 GREAT ROOM (main; option-a-evolve-current/main_floor_a.scad:100) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @53.95,45.39 | hall | 5.3 | full 58.8 in |
| FLEX ROOM | office | 9.9 | - |
| PATIO | porch (ceil 0) | 1.8 | - |
| HALL @24.34,29.51 | hall | 26.5 | full 312 in |
| OFFICE | office | 12.7 | - |
| DECK | porch (ceil 0) | 26.5 | double 72 in |
| OFFICE PORCH | porch (ceil 0) | 4.4 | - |

### 8.1 DEN (main; option-a-evolve-current/main_floor_a.scad:104) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @24.34,29.51 | hall | 14.8 | - |
| FOYER | hall | 25.8 | double 60 in |
| (den alcove) | living | 11.2 | full 128.4 in |
| WIC @95.95,20.56 | closet | 9.0 | - |
| FRONT PORCH | porch (ceil 0) | 14.8 | - |
| (unlabelled porch) @95.95,0 | porch (ceil 0) | 9.3 | - |
| (covered entry) | porch (ceil 0) | 3.7 | - |

### 8.1 SUN ROOM (main; option-a-evolve-current/main_floor_a.scad:95) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| STUDY | office | 9.7 | - |
| (N-S hall, unlabelled) | hall | 3.1 | - |
| (landing at the stair top) | hall (ceil 0) | 4.6 | - |
| (upper hall, west of its door) | hall | 6.7 | double 70.8 in |
| PATIO | porch (ceil 0) | 12.7 | double 58.8 in |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are GREAT ROOM, DEN, SUN ROOM. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| STAIR UP | stair | 4.6 | - |
| HALLWAY | hall (ceil 0) | 7.4 | open 76.8 in |
| STAIR FOOT | hall (ceil 0) | 6.9 | open 48 in |
| PET ROOM | utility | 9.5 | - |
| HALL @54.14,13.43 | hall | 4.7 | open 48 in |
| BATH @54.14,5.79 | bath | 7.6 | - |

### 8.2 FOYER (option-a-evolve-current/main_floor_a.scad:103) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @24.34,29.51 | hall | 12.0 | full 94.8 in |
| KITCHEN / DINING | kitchen | 23.2 | - |
| BREAKFAST | dining | 2.6 | - |
| DEN | living | 25.8 | double 60 in |
| (covered entry) | porch (ceil 0) | 12.0 | double 74.4 in, glass 24 in, glass 24 in |

### 8.3 Closets, WICs, linen, scullery, storage: exterior exposure

No room is labelled PANTRY in the model. SCULLERY (kind utility) and the 'tall pantry cabinets' fixture row (option-a-evolve-current/main_floor_a.scad:227, inside KITCHEN/DINING) are the pantry-like items.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | SCULLERY | option-a-evolve-current/main_floor_a.scad:74 | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| main | WIC @18.5,35.46 | option-a-evolve-current/main_floor_a.scad:79 | S 3.6 (garage) |
| main | WIC @95.95,20.56 | option-a-evolve-current/main_floor_a.scad:110 | none |
| main | WIC @111.8,20.56 | option-a-evolve-current/main_floor_a.scad:112 | none |
| main | (linen between the WCs) | option-a-evolve-current/main_floor_a.scad:116 | none |
| base | STORAGE | option-a-evolve-current/basement_a.scad:62 | W 7.6 (yard/soil) |

Pantry/garage: SCULLERY shares 8.7 ft of wall with the garage; doors between SCULLERY and GARAGE: 1. The garage's doors to the house are: option-a-evolve-current/main_floor_a.scad:143 (GARAGE | (garage side-door pad), 36 in); option-a-evolve-current/main_floor_a.scad:144 (GARAGE | SIDE ENTRY, 36 in); option-a-evolve-current/main_floor_a.scad:146 (GARAGE | HALL @24.34,29.51, 36 in); option-a-evolve-current/main_floor_a.scad:147 (GARAGE | SCULLERY, 36 in). The tall pantry cabinets (x 42.24-49.14) are 17.9 ft east of the garage wall (x 24.34): no shared wall.

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN / DINING | range (223); sink (225); fridge (226); double island (228); prep sink (229) | front door -> kitchen/dining room centre; front door -> range (option-a-evolve-current/main_floor_a.scad:223); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> tall pantry cabinets in kitchen (option-a-evolve-current/main_floor_a.scad:227) |
| LAUNDRY | washer + dryer (235); laundry sink (237) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> LAUNDRY centre; BUNK ROOM centre -> LAUNDRY centre |
| MASTER LAUNDRY | master washer + dryer on the exterior wall (262) | master bedroom centre -> MASTER LAUNDRY centre; BEDROOM 2 centre -> MASTER LAUNDRY centre; BUNK ROOM centre -> MASTER LAUNDRY centre |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 5.6 (porch/patio (open)), 1.7 (yard/soil); S 24.3 (yard/soil); E 7.5 (porch/patio (open)), 2.1 (yard/soil); W 24.2 (yard/soil) |
| BEDROOM 2 | 9.3 | west driveway (site.scad:111) | S 11.2 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) |
| WC @7.27,48.13 | 11.1 | west driveway (site.scad:111) | W 7.2 (yard/soil) |
| BREAKFAST | 14.0 | loop north leg (:114) | S 15.0 (porch/patio (open)); E 3.7 (porch/patio (open)); W 6.3 (porch/patio (open)) |
| DEN | 14.0 | loop north leg (:114) | S 14.8 (porch/patio (open)); E 9.3 (porch/patio (open)); W 3.7 (porch/patio (open)) |
| BATH 2 | 16.2 | west driveway (site.scad:111) | N 10.2 (yard/soil); W 6.7 (yard/soil) |
| (suite entry) | 16.9 | west driveway (site.scad:111) | none |
| FOYER | 17.7 | loop north leg (:114) | S 12.0 (porch/patio (open)) |
| (suite entry, 2nd piece) | 19.7 | west driveway (site.scad:111) | none |
| KITCHEN / DINING | 20.3 | loop north leg (:114) | S 4.9 (porch/patio (open)), 13.6 (yard/soil); W 7.4 (porch/patio (open)), 7.1 (yard/soil) |
| WIC @18.5,35.46 | 20.5 | west driveway (site.scad:111) | S 3.6 (garage) |
| BUNK ROOM | 22.8 | west driveway (site.scad:111) | N 15.1 (yard/soil); E 3.2 (yard/soil); W 4.6 (yard/soil) |
| (den alcove) | 23.3 | loop north leg (:114) | S 3.8 (porch/patio (open)) |
| MASTER BATH | 23.3 | loop north leg (:114) | S 21.6 (yard/soil); E 11.2 (yard/soil) |
| WC @99.7,9.31 | 23.3 | loop north leg (:114) | S 1.7 (porch/patio (open)), 5.1 (yard/soil) |
| MUDROOM | 24.1 | west driveway (site.scad:111) | S 2.2 (garage) |
| LAUNDRY | 24.1 | west driveway (site.scad:111) | none |
| HALL @22.1,48.64 | 25.0 | west driveway (site.scad:111) | none |
| SCULLERY | 26.3 | west driveway (site.scad:111) | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| HALL @24.34,29.51 | 26.3 | west driveway (site.scad:111) | W 6.0 (garage) |
| (linen between the WCs) | 27.1 | loop north leg (:114) | none |
| WC @99.7,16.71 | 30.7 | loop north leg (:114) | none |
| WIC @95.95,20.56 | 34.6 | loop north leg (:114) | none |
| (closet passage) | 34.6 | loop north leg (:114) | none |
| WIC @111.8,20.56 | 34.6 | loop north leg (:114) | none |
| MASTER LAUNDRY | 34.6 | loop north leg (:114) | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) |
| STUDY | 36.5 | west driveway (site.scad:111) | N 4.6 (porch/patio (open)), 5.4 (yard/soil) |
| (N-S hall, unlabelled) | 39.3 | west driveway (site.scad:111) | none |

Other rooms are > 40 ft from any drive. Garage doors (rows option-a-evolve-current/main_floor_a.scad:142) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN / DINING) | KITCHEN / DINING | (39.93, 6.68, 42.57, 8.26) | (41.2, 7.5) | S wall y=6.28 | 0.40 | option-a-evolve-current/main_floor_a.scad:225 |
| sink (KITCHEN / DINING) | KITCHEN / DINING | (43.22, 16.68, 44.87, 18.65) | (44.0, 17.7) | island | 7.62 | option-a-evolve-current/main_floor_a.scad:229 |
| sink (SCULLERY) | SCULLERY | (28.09, 27.34, 31.71, 28.91) | (29.9, 28.1) | N wall y=29.51 | 0.60 | option-a-evolve-current/main_floor_a.scad:233 |
| washer/dryer (LAUNDRY) | LAUNDRY | (28.09, 46.2, 34.01, 48.2) | (31.0, 47.2) | N wall y=48.64 | 0.44 | option-a-evolve-current/main_floor_a.scad:235 |
| sink (LAUNDRY) | LAUNDRY | (33.22, 41.02, 35.1, 43.52) | (34.2, 42.3) | S wall y=40.56 | 0.46 | option-a-evolve-current/main_floor_a.scad:237 |
| toilet/tub/wash basin (BATH 2) | BATH 2 | (7.7, 55.55, 10.33, 61.41) | (9.0, 58.5) | S wall y=55.3 | 0.25 | option-a-evolve-current/main_floor_a.scad:244 |
| vanity (BATH 2) | BATH 2 | (10.99, 60.1, 17.3, 61.68) | (14.1, 60.9) | E wall x=17.5 | 0.20 | option-a-evolve-current/main_floor_a.scad:245 |
| toilet/tub/wash basin (WC @7.27,48.13) | WC @7.27,48.13 | (8.03, 51.55, 10.33, 53.85) | (9.2, 52.7) | W wall x=7.27 | 0.76 | option-a-evolve-current/main_floor_a.scad:246 |
| vanity (BATH) | BATH | (51.78, 42.34, 53.42, 44.31) | (52.6, 43.3) | E wall x=53.95 | 0.53 | option-a-evolve-current/main_floor_a.scad:247 |
| toilet/tub/wash basin (BATH) | BATH | (51.12, 39.7, 53.09, 41.35) | (52.1, 40.5) | E wall x=53.95 | 0.86 | option-a-evolve-current/main_floor_a.scad:248 |
| shower (BATH) | BATH | (47.83, 35.89, 53.42, 38.39) | (50.6, 37.1) | S wall y=35.46 | 0.43 | option-a-evolve-current/main_floor_a.scad:249 |
| vanity (MASTER BATH) | MASTER BATH | (111.64, 17.86, 121.51, 19.64) | (116.6, 18.8) | N wall y=20.56 | 0.92 | option-a-evolve-current/main_floor_a.scad:250 |
| shower (MASTER BATH) | MASTER BATH | (111.97, 9.55, 120.2, 14.05) | (116.1, 11.8) | S wall y=9.31 | 0.24 | option-a-evolve-current/main_floor_a.scad:251 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (123.16, 9.55, 127.63, 15.03) | (125.4, 12.3) | S wall y=9.31 | 0.24 | option-a-evolve-current/main_floor_a.scad:252 |
| toilet/tub/wash basin (WC @99.7,16.71) | WC @99.7,16.71 | (100.79, 17.01, 103.42, 19.31) | (102.1, 18.2) | S wall y=16.71 | 0.30 | option-a-evolve-current/main_floor_a.scad:253 |
| toilet/tub/wash basin (WC @99.7,9.31) | WC @99.7,9.31 | (100.79, 9.77, 103.42, 12.07) | (102.1, 10.9) | S wall y=9.31 | 0.46 | option-a-evolve-current/main_floor_a.scad:254 |
| washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | (125.4, 21.1, 127.9, 26) | (126.7, 23.6) | E wall x=128.13 | 0.23 | option-a-evolve-current/main_floor_a.scad:262 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| toilet/tub/wash basin (BATH @47.27,35.08) | BATH @47.27,35.08 | (52, 41.5, 53.8, 43.3) | (52.9, 42.4) | E wall x=54.14 | 0.34 | option-a-evolve-current/basement_a.scad:126 |
| vanity (BATH @47.27,35.08) | BATH @47.27,35.08 | (52.1, 38.5, 53.9, 41) | (53.0, 39.8) | E wall x=54.14 | 0.24 | option-a-evolve-current/basement_a.scad:127 |
| shower (BATH @47.27,35.08) | BATH @47.27,35.08 | (47.6, 42, 50.6, 45) | (49.1, 43.5) | W wall x=47.27 | 0.33 | option-a-evolve-current/basement_a.scad:128 |
| toilet/tub/wash basin (POOL BATH) | POOL BATH | (100.6, 22.5, 102.4, 24.3) | (101.5, 23.4) | E wall x=103.04 | 0.64 | option-a-evolve-current/basement_a.scad:129 |
| vanity (POOL BATH) | POOL BATH | (96.6, 25.5, 98.6, 28.8) | (97.6, 27.1) | W wall x=96.33 | 0.27 | option-a-evolve-current/basement_a.scad:130 |
| shower (POOL BATH) | POOL BATH | (99.2, 25.4, 102.45, 28.9) | (100.8, 27.1) | N wall y=29.12 | 0.22 | option-a-evolve-current/basement_a.scad:131 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (54.4, 6.4, 59.4, 8.95) | (56.9, 7.7) | W wall x=54.14 | 0.26 | option-a-evolve-current/basement_a.scad:132 |
| vanity (BATH @54.14,5.79) | BATH @54.14,5.79 | (62.5, 6.4, 67.1, 8.25) | (64.8, 7.3) | E wall x=67.4 | 0.30 | option-a-evolve-current/basement_a.scad:133 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (65.2, 9.5, 67.1, 11.3) | (66.2, 10.4) | E wall x=67.4 | 0.30 | option-a-evolve-current/basement_a.scad:134 |
| washer/dryer (LAUNDRY) | LAUNDRY | (67.8, 6.4, 72.6, 8.75) | (70.2, 7.6) | W wall x=67.4 | 0.40 | option-a-evolve-current/basement_a.scad:136 |
| toilet/tub/wash basin (PET ROOM) | PET ROOM | (65.5, 26.5, 69, 28.9) | (67.2, 27.7) | N wall y=29.12 | 0.22 | option-a-evolve-current/basement_a.scad:138 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | sink (KITCHEN / DINING) | KITCHEN / DINING | y=6.28 (horizontal wall) | (41.2, 7.5) |
| G2 | toilet/tub/wash basin (WC @99.7,9.31) | WC @99.7,9.31 | y=9.31 (horizontal wall) | (102.1, 10.9) |
| G3 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | MASTER BATH | y=9.31 (horizontal wall) | (120.7, 12.0) |
| G4 | sink (KITCHEN / DINING) | KITCHEN / DINING | free-standing island (>3 ft from any wall) | (44.0, 17.7) |
| G5 | toilet/tub/wash basin (WC @99.7,16.71) | WC @99.7,16.71 | y=16.71 (horizontal wall) | (102.1, 18.2) |
| G6 | vanity (MASTER BATH) | MASTER BATH | y=20.56 (horizontal wall) | (116.6, 18.8) |
| G7 | washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | x=128.13 (vertical wall) | (126.7, 23.6) |
| G8 | sink (SCULLERY) | SCULLERY | y=29.51 (horizontal wall) | (29.9, 28.1) |
| G9 | shower (BATH) | BATH | y=35.46 (horizontal wall) | (50.6, 37.1) |
| G10 | sink (LAUNDRY) | LAUNDRY | y=40.56 (horizontal wall) | (34.2, 42.3) |
| G11 | vanity (BATH); toilet/tub/wash basin (BATH) | BATH | x=53.95 (vertical wall) | (52.4, 41.9) |
| G12 | washer/dryer (LAUNDRY) | LAUNDRY | y=48.64 (horizontal wall) | (31.0, 47.2) |
| G13 | toilet/tub/wash basin (WC @7.27,48.13) | WC @7.27,48.13 | x=7.27 (vertical wall) | (9.2, 52.7) |
| G14 | toilet/tub/wash basin (BATH 2) | BATH 2 | y=55.3 (horizontal wall) | (9.0, 58.5) |
| G15 | vanity (BATH 2) | BATH 2 | x=17.5 (vertical wall) | (14.1, 60.9) |

**Main floor: 15 wet-wall groups** (5 back-to-back plumbing clusters of rooms: SCULLERY+KITCHEN / DINING | LAUNDRY | WC @7.27,48.13+BATH 2 | BATH | MASTER LAUNDRY+MASTER BATH+WC @99.7,16.71+WC @99.7,9.31)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | vanity (BATH @54.14,5.79); toilet/tub/wash basin (BATH @54.14,5.79); washer/dryer (LAUNDRY) | BATH @54.14,5.79; LAUNDRY | x=67.4 (vertical wall) | (67.0, 8.4) |
| G2 | toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | x=54.14 (vertical wall) | (56.9, 7.7) |
| G3 | toilet/tub/wash basin (POOL BATH) | POOL BATH | x=103.04 (vertical wall) | (101.5, 23.4) |
| G4 | vanity (POOL BATH) | POOL BATH | x=96.33 (vertical wall) | (97.6, 27.1) |
| G5 | shower (POOL BATH) | POOL BATH | y=29.12 (horizontal wall) | (100.8, 27.1) |
| G6 | toilet/tub/wash basin (PET ROOM) | PET ROOM | y=29.12 (horizontal wall) | (67.2, 27.7) |
| G7 | toilet/tub/wash basin (BATH @47.27,35.08); vanity (BATH @47.27,35.08) | BATH @47.27,35.08 | x=54.14 (vertical wall) | (53.0, 41.1) |
| G8 | shower (BATH @47.27,35.08) | BATH @47.27,35.08 | x=47.27 (vertical wall) | (49.1, 43.5) |

**Basement: 8 wet-wall groups** (4 clusters: BATH @47.27,35.08 | PET ROOM | POOL BATH | BATH @54.14,5.79+LAUNDRY)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 15/8; 6 ft: 15/8; 8 ft: 15/8; 12 ft: 14/8; inf: 14/6

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | sink (KITCHEN / DINING) | (41.2,7.5) | B2 (BATH @54.14,5.79) | (56.9,7.7) | 15.6 | 0.2 | 15.9 |
| G2 | toilet/tub/wash basin (WC @99.7,9.31) | (102.1,10.9) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 12.5 | 13.1 |
| G3 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | (120.7,12.0) | B3 (POOL BATH) | (101.5,23.4) | 19.2 | 11.4 | 30.6 |
| G4 | sink (KITCHEN / DINING) | (44.0,17.7) | B2 (BATH @54.14,5.79) | (56.9,7.7) | 12.9 | 10.0 | 22.8 |
| G5 | toilet/tub/wash basin (WC @99.7,16.71) | (102.1,18.2) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 5.2 | 5.8 |
| G6 | vanity (MASTER BATH) | (116.6,18.8) | B3 (POOL BATH) | (101.5,23.4) | 15.1 | 4.6 | 19.7 |
| G7 | washer/dryer (MASTER LAUNDRY) | (126.7,23.6) | B3 (POOL BATH) | (101.5,23.4) | 25.2 | 0.2 | 25.3 |
| G8 | sink (SCULLERY) | (29.9,28.1) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 19.2 | 15.4 | 34.6 |
| G9 | shower (BATH) | (50.6,37.1) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 2.3 | 3.9 | 6.3 |
| G10 | sink (LAUNDRY) | (34.2,42.3) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 14.9 | 1.2 | 16.2 |
| G11 | vanity (BATH); toilet/tub/wash basin (BATH) | (52.4,41.9) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 0.6 | 0.9 | 1.4 |
| G12 | washer/dryer (LAUNDRY) | (31.0,47.2) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 18.1 | 3.7 | 21.8 |
| G13 | toilet/tub/wash basin (WC @7.27,48.13) | (9.2,52.7) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 39.9 | 9.2 | 49.1 |
| G14 | toilet/tub/wash basin (BATH 2) | (9.0,58.5) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 40.1 | 15.0 | 55.1 |
| G15 | vanity (BATH 2) | (14.1,60.9) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 35.0 | 17.4 | 52.3 |

Main-floor groups with a basement group within 5 ft Manhattan: 1 of 15; within 10 ft: 3.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (41.2,7.5) | 69.6 | 50.5 |
| G2 | (102.1,10.9) | 127.0 | 107.9 |
| G3 | (120.7,12.0) | 144.5 | 125.4 |
| G4 | (44.0,17.7) | 62.2 | 43.1 |
| G5 | (102.1,18.2) | 119.8 | 100.7 |
| G6 | (116.6,18.8) | 133.7 | 114.6 |
| G7 | (126.7,23.6) | 138.9 | 119.8 |
| G8 | (29.9,28.1) | 37.6 | 18.5 |
| G9 | (50.6,37.1) | 49.3 | 30.2 |
| G10 | (34.2,42.3) | 27.7 | 15.4 |
| G11 | (52.4,41.9) | 46.3 | 33.2 |
| G12 | (31.0,47.2) | 19.7 | 17.2 |
| G13 | (9.2,52.7) | 18.3 | 26.8 |
| G14 | (9.0,58.5) | 13.6 | 32.7 |
| G15 | (14.1,60.9) | 10.9 | 30.0 |

**DRI (E = (22.16, 58)) = 1019.2 ft over 15 groups; mean 67.9 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 866.1 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:142, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:141). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **toilet/tub/wash basin (MASTER BATH), 119.8 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: toilet/tub/wash basin (MASTER BATH), 122.4 ft.
- Furthest basement fixture: **toilet/tub/wash basin (POOL BATH), 84.8 ft** from the water heater.
- Nearest main-floor fixture: sink (SCULLERY), 8.9 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN / DINING) 40; sink (KITCHEN / DINING) 33; sink (SCULLERY) 9; washer/dryer (LAUNDRY) 11; sink (LAUNDRY) 10; toilet/tub/wash basin (BATH 2) 43; vanity (BATH 2) 40; toilet/tub/wash basin (WC @7.27,48.13) 37; vanity (BATH) 29; toilet/tub/wash basin (BATH) 26; shower (BATH) 21; vanity (MASTER BATH) 105; shower (MASTER BATH) 111; toilet/tub/wash basin (MASTER BATH) 120; toilet/tub/wash basin (WC @99.7,16.71) 91; toilet/tub/wash basin (WC @99.7,9.31) 98; washer/dryer (MASTER LAUNDRY) 110; toilet/tub/wash basin (BATH @47.27,35.08) 28; vanity (BATH @47.27,35.08) 26; shower (BATH @47.27,35.08) 26; toilet/tub/wash basin (POOL BATH) 85; vanity (POOL BATH) 77; shower (POOL BATH) 80; toilet/tub/wash basin (BATH @54.14,5.79) 56; vanity (BATH @54.14,5.79) 64; toilet/tub/wash basin (BATH @54.14,5.79) 62; washer/dryer (LAUNDRY) 69; toilet/tub/wash basin (PET ROOM) 46

## Section 10

### 10.1 Main to basement stair (house_lib.scad:107-125, values via model.json `stair`)

| Item | Value | Source / formula |
|---|---|---|
| Wall centre lines x | 42.65 to 47.27 | house_lib.scad:120 stair_x() |
| Clear width between walls | 4.22 ft = 50.6 in | x range minus wall_t 0.4 (Redesign doc line 157 says 4'-2 1/2") |
| Floor to floor | 13.75 ft | house_lib.scad:107 |
| Risers / rise each | 22 x 7.500 in | house_lib.scad:121-122 ceil(floor_to_floor*12/7.5) |
| Treads / run each | 21 x 10.5 in | house_lib.scad:123 stair_run=10.5/12; treads = risers-1 |
| Total run | 18.375 ft (220.5 in) | 21 x 10.5 in |
| Top nosing y / foot y | 47.1 / 28.725 | house_lib.scad:124-125; foot = top - 21*run |
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-a-evolve-current/main_floor_a.scad:89 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-a-evolve-current/basement_a.scad:65 |
| Headroom | Redesign doc: >= 1 993 mm at the tightest point vs 1 950 mm required; the floor opening was sized for it (house_lib.scad:112-119 comment) | Redesign-and-Spec-2026-11-02.md:158, 162-167; not recomputed here |
| Handrails | both sides in the model (house_lib.scad main_stair rail=true) | house_lib.scad:324-340 main_stair(); Redesign doc:159 |
| Landings | top: the stair landing/upper hall; bottom: HALLWAY at the 8 ft archway (basement.scad:89 'open' 8 ft) into the living room | Redesign doc:160 |

### 10.2 Basement exit stair (foundation.scad:134-142, model.json `exit_stair`)

| Item | Value | Source |
|---|---|---|
| Door | x 46.2, 3.5 ft wide (42 in) in the gym's north wall y=63.16, opens in | basement.scad:98; foundation.scad:134 |
| Rise to grade | 11.75 ft; 19 risers x 7.42 in | foundation.scad:135-136 |
| Run | 11 in treads; flight length 16.50 ft | foundation.scad:137, 139 |
| Landing x range | [45.6, 50.3] | foundation.scad:138 |
| Areaway clear inside | x 45.6-66.80, y 63.75-67.75 (4.0 ft wide) | foundation.scad:139 |
| Top landing at grade | 2.2 ft past the top step | foundation.scad:141 |
| Footprint with walls | [44.93, 63.09, 69, 68.42] | foundation.scad:144 |
| Direction | rises east along the house's north side, ending beside the deck steps (Redesign doc:473-480) | Redesign doc |

The exit stair comes up beside the PATIO, whose north edge has a guard (main_floor.scad:345-354 patio_guard). Basement windows: 2 wells (foundation.scad:159-162).

## Section 12

Read with `phase = "house"` (site.scad:47, the default) for everything except the shop rows, which are the `phase = "full"` geometry (site.scad:122-131, 196-197, 245) and the future-shop dashed rectangle (site.scad:217-221, shop_origin() = [0,130], site.scad:60). Land is not chosen: positions are relative to the house (site.scad:6-8). Road assumed on the south (site.scad:8, 74: road north edge y = -100).

### 12.1 Coordinates (site.scad)

| Item | Coordinates [x0,y0,x1,y1] or point | Source |
|---|---|---|
| Septic tank | [-3, 52, 3, 64]  (6 x 12 ft) | site.scad:70 |
| Pump chamber | [-3, 64, 3, 68] | site.scad:71 |
| Treatment field | [-120, 45, -65, 100]  (55 x 55 ft) | site.scad:72 |
| Reserve field | [-120, -15, -65, 40] | site.scad:73 |
| Well | (150, 75) | site.scad:63 |
| Propane tank | (-60, -45) centre; pad 16 x 6 ft | site.scad:64, 170 |
| Starlink dish | (12, 80) | site.scad:65 |
| West driveway | x -32..-2 (30 ft wide), y -100..42 (142 ft long) | site.scad:111 |
| Front loop | ring x 25..130, y -72..-14, 14 ft wide legs; connector x -2..25, y -50..-36 | site.scad:113-117 |
| Future shop (house phase) | dashed [0,130]-[100,230] | site.scad:60, 218 |
| Service lines | fibre x=-41, power x=-44, gas x=-47, from y=-100 north to y=44/46/48 then east to x=7.27 (bedroom-wing west wall) | site.scad:162-164 |
| Meters | two boxes on x=6.6, y 45 and 47.5 | site.scad:175 |
| Water line | well (150,75) -> (150,45) -> (126.97,45) | site.scad:167 |
| Building sewer | (22.16,58) -> (3,58) (tank east face); effluent line (-3,66) -> (-65,66) | site.scad:188, 191 |

### 12.2 Distances (computed with shapely from those rectangles; ft and m)

| Pair | Distance |
|---|---|
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 4.3 ft (1.3 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 72.3 ft (22.0 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 72.3 ft (22.0 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 31.9 ft (9.7 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 19.8 ft (6.0 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 63.4 ft (19.3 m) |
| House incl. porches/deck to future shop | 63.4 ft (19.3 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

