# Plan facts (variant mode)

main = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/main_floor_f.scad`, basement = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/basement_f.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/main_floor_f.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/basement_f.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 3,704 | 3704.1; excl. stair opening 3639.3 |
| Building area, centre lines (house + attached garage) | 397.1 m2 | 4275 sq ft |
| Building area, outside face | 417.8 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 3,910 sq ft | centre lines 3,704 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 3,917 sq ft | centre lines 3,711 sq ft |
| Circulation % (strict / with foyer) | 10.7% / 13.4% | 396 sq ft strict of 3704 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 19 | type `door` rows, by opening width |
| Double / open counts (main) | 2 / 0 | type `double` / type `open` |
| Minimum hall clear width | 5.00 ft ((short hall to the primary)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 5.00 ft ((short hall to the primary)) |
| Wet-wall groups (main / basement) | 9 / 2 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 0 of 9 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 1017.1 ft | alternate exit (22.16, 38.9): 847.8 ft |
| Water heater -> furthest fixture (main / basement) | 114.8 ft (toilet/tub/wash basin (MASTER BATH)) / 62.4 ft (vanity (JACK & JILL BATH)) | water heater at (18.1, 31.5); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 29.6 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 4 of 6: CLOSET @86.6,25.8 [N(yard 5.4) W(yard 7.4)]; ELEVATOR (FUTURE) [N(yard 6.4)]; CLOSET @106.8,12.4 [S(yard 7.8)]; WIC @98.4,36.2 [N(yard 1.2) W(yard 8.4)] | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 12.4 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(yard 12.4) E(yard 14.4) W(yard 6.4) ;; MASTER BEDROOM: N(yard 27.4) E(porch/patio 16.0, yard 6.4) W(yard 22.4) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 28.6) E(porch/patio 16.0, yard 25.2) W(yard 30.8) | suite rooms: (short hall to the primary), WIC @98.4,36.2, WIC @104.8,36.2, (primary entry), MASTER BATH, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (24.4 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 5: KITCHEN (N/S); LIVING (N/S); OFFICE / LIBRARY (N/W); BEDROOM 2 (E/S); MASTER BEDROOM (E/N/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 86.6..92, y 20.4; basement foot room x 86.6..92, y 4.45; **moved** (x offset +0.00/+0.00 ft, run 15.950 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 20.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_f.scad (defaults): 30 rooms, 32 doors, 17 windows - OK ; basement_f.scad (defaults): 23 rooms, 22 doors, 6 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 3704.1 | computed: sum (x1-x0)*(y1-y0) over 25 rows, main_floor.scad:40-74 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 64.8 | option-f-your-sizes-fitted/main_floor_f.scad:51 |
| Main-floor conditioned excluding the stair opening | 3639.3 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 3704.1 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 3779.7 | computed over basement.scad:37-63 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 570.4 | option-f-your-sizes-fitted/main_floor_f.scad:40 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| DRIVE (SLOPES UP TO GARAGE) | 368.0 | option-f-your-sizes-fitted/main_floor_f.scad:71 |
| PATIO | 120.0 | option-f-your-sizes-fitted/main_floor_f.scad:72 |
| FRONT PORCH | 56.0 | option-f-your-sizes-fitted/main_floor_f.scad:73 |
| DECK | 48.0 | option-f-your-sizes-fitted/main_floor_f.scad:74 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 592.0 sq ft. PATIO alone: 120.0; DECK alone: 48.0. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 409.2 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 343.0 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 35.0 ft | same |
|   facing garage | 31.2 ft | same (garage is unheated) |
| Outside (convex) corners | 14 | vertices of the union polygon after 0.02 ft simplify (24 vertices) |
| Inside (reflex) corners | 10 | same polygon |
| Bounding box, heated rooms | x 16.6..127 (110.4 ft), y 0..67 (67 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..130 (130 ft), y -16..67 (83 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 7 hip-roof blocks in main_roof (main_floor.scad:232); each hip block is 4 sloped facets, so 4 x 7 = 28 nominal facets before overlapping blocks merge; 0 blocks at 6/12 pitch, 7 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| PANTRY | S 9.4 (yard/soil); W 12.4 (garage) | option-f-your-sizes-fitted/main_floor_f.scad:42 |
| MUDROOM | N 0.4 (yard/soil); E 2.4 (yard/soil); W 12.4 (garage) | option-f-your-sizes-fitted/main_floor_f.scad:43 |
| OFFICE / LIBRARY | N 15.4 (yard/soil); S 6.4 (garage); E 16.4 (yard/soil); W 16.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:44 |
| KITCHEN | N 15.4 (yard/soil); S 15.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:46 |
| DINING / NOOK | N 14.4 (yard/soil); S 12.0 (porch/patio (open)), 2.4 (yard/soil); E 2.0 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:47 |
| LIVING | N 24.4 (yard/soil); S 24.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:48 |
| FOYER | S 7.0 (porch/patio (open)), 4.8 (yard/soil); E 5.0 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:50 |
| STAIR DN | none | option-f-your-sizes-fitted/main_floor_f.scad:51 |
| (junction passage) | none | option-f-your-sizes-fitted/main_floor_f.scad:52 |
| (junction hall) | W 5.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:53 |
| CLOSET @86.6,25.8 | N 5.4 (yard/soil); W 7.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:54 |
| ELEVATOR (FUTURE) | N 6.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:55 |
| POWDER | S 6.4 (yard/soil); E 7.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:57 |
| (bedroom hall) | E 5.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:58 |
| SHARED BATH | S 2.0 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:59 |
| CLOSET @106.8,12.4 | S 7.8 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:60 |
| BEDROOM 2 | S 12.4 (yard/soil); E 14.4 (yard/soil); W 6.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:61 |
| LAUNDRY | W 3.0 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:62 |
| LINEN | none | option-f-your-sizes-fitted/main_floor_f.scad:63 |
| (short hall to the primary) | none | option-f-your-sizes-fitted/main_floor_f.scad:64 |
| WIC @98.4,36.2 | N 1.2 (yard/soil); W 8.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:65 |
| WIC @104.8,36.2 | none | option-f-your-sizes-fitted/main_floor_f.scad:66 |
| (primary entry) | none | option-f-your-sizes-fitted/main_floor_f.scad:67 |
| MASTER BATH | E 18.8 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:68 |
| MASTER BEDROOM | N 27.4 (yard/soil); E 16.0 (porch/patio (open)), 6.4 (yard/soil); W 22.4 (yard/soil) | option-f-your-sizes-fitted/main_floor_f.scad:69 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PANTRY | 23 | 0 | 32.4 | 12.4 | 9.40 x 12.40 | 9.0 x 12.0 | 117 | 108 | 1.32 | utility | 10 | option-f-your-sizes-fitted/main_floor_f.scad:42 |
| MUDROOM | 23 | 12.4 | 32.4 | 24.8 | 9.40 x 12.40 | 9.0 x 12.0 | 117 | 108 | 1.32 | utility | 10 | option-f-your-sizes-fitted/main_floor_f.scad:43 |
| OFFICE / LIBRARY | 16.6 | 24.8 | 32 | 41.2 | 15.40 x 16.40 | 15.0 x 16.0 | 253 | 240 | 1.06 | office | 10 | option-f-your-sizes-fitted/main_floor_f.scad:44 |
| KITCHEN | 32.4 | 0 | 47.8 | 22.4 | 15.40 x 22.40 | 15.0 x 22.0 | 345 | 330 | 1.45 | kitchen | 10 | option-f-your-sizes-fitted/main_floor_f.scad:46 |
| DINING / NOOK | 47.8 | 0 | 62.2 | 22.4 | 14.40 x 22.40 | 14.0 x 22.0 | 323 | 308 | 1.56 | dining | 10 | option-f-your-sizes-fitted/main_floor_f.scad:47 |
| LIVING | 62.2 | 0 | 86.6 | 20.4 | 24.40 x 20.40 | 24.0 x 20.0 | 498 | 480 | 1.20 | living | 10 | option-f-your-sizes-fitted/main_floor_f.scad:48 |
| FOYER | 86.6 | 0 | 98.4 | 8.4 | 11.80 x 8.40 | 11.4 x 8.0 | 99 | 91 | 1.40 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:50 |
| STAIR DN | 86.6 | 8.4 | 92 | 20.4 | 5.40 x 12.00 | 5.0 x 11.6 | 65 | - | 2.22 | stairwell | 0 | option-f-your-sizes-fitted/main_floor_f.scad:51 |
| (junction passage) | 92 | 8.4 | 98.4 | 20.4 | 6.40 x 12.00 | 6.0 x 11.6 | 77 | 70 | 1.87 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:52 |
| (junction hall) | 86.6 | 20.4 | 98.4 | 25.8 | 11.80 x 5.40 | 11.4 x 5.0 | 64 | 57 | 2.19 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:53 |
| CLOSET @86.6,25.8 | 86.6 | 25.8 | 92 | 33.2 | 5.40 x 7.40 | 5.0 x 7.0 | 40 | 35 | 1.37 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:54 |
| ELEVATOR (FUTURE) | 92 | 25.8 | 98.4 | 33.2 | 6.40 x 7.40 | 6.0 x 7.0 | 47 | 42 | 1.16 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:55 |
| POWDER | 98.4 | 5 | 104.8 | 12.4 | 6.40 x 7.40 | 6.0 x 7.0 | 47 | 42 | 1.16 | bath | 10 | option-f-your-sizes-fitted/main_floor_f.scad:57 |
| (bedroom hall) | 98.4 | 20.4 | 127 | 25.8 | 28.60 x 5.40 | 28.2 x 5.0 | 154 | 141 | 5.30 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:58 |
| SHARED BATH | 98.4 | 12.4 | 106.8 | 20.4 | 8.40 x 8.00 | 8.0 x 7.6 | 67 | 61 | 1.05 | bath | 10 | option-f-your-sizes-fitted/main_floor_f.scad:59 |
| CLOSET @106.8,12.4 | 106.8 | 12.4 | 114.6 | 20.4 | 7.80 x 8.00 | 7.4 x 7.6 | 62 | 56 | 1.03 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:60 |
| BEDROOM 2 | 114.6 | 6 | 127 | 20.4 | 12.40 x 14.40 | 12.0 x 14.0 | 179 | 168 | 1.16 | bed | 10 | option-f-your-sizes-fitted/main_floor_f.scad:61 |
| LAUNDRY | 98.4 | 25.8 | 107.8 | 36.2 | 9.40 x 10.40 | 9.0 x 10.0 | 98 | 90 | 1.11 | utility | 10 | option-f-your-sizes-fitted/main_floor_f.scad:62 |
| LINEN | 107.8 | 25.8 | 111.2 | 36.2 | 3.40 x 10.40 | 3.0 x 10.0 | 35 | 30 | 3.06 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:63 |
| (short hall to the primary) | 111.2 | 25.8 | 116.6 | 36.2 | 5.40 x 10.40 | 5.0 x 10.0 | 56 | 50 | 1.93 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:64 |
| WIC @98.4,36.2 | 98.4 | 36.2 | 104.8 | 44.6 | 6.40 x 8.40 | 6.0 x 8.0 | 54 | 48 | 1.31 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:65 |
| WIC @104.8,36.2 | 104.8 | 36.2 | 111.2 | 44.6 | 6.40 x 8.40 | 6.0 x 8.0 | 54 | 48 | 1.31 | closet | 10 | option-f-your-sizes-fitted/main_floor_f.scad:66 |
| (primary entry) | 111.2 | 36.2 | 116.6 | 44.6 | 5.40 x 8.40 | 5.0 x 8.0 | 45 | 40 | 1.56 | hall | 10 | option-f-your-sizes-fitted/main_floor_f.scad:67 |
| MASTER BATH | 116.6 | 25.8 | 127 | 44.6 | 10.40 x 18.80 | 10.0 x 18.4 | 196 | 184 | 1.81 | bath | 10 | option-f-your-sizes-fitted/main_floor_f.scad:68 |
| MASTER BEDROOM | 99.6 | 44.6 | 127 | 67 | 27.40 x 22.40 | 27.0 x 22.0 | 614 | 594 | 1.22 | bed | 10 | option-f-your-sizes-fitted/main_floor_f.scad:69 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 0 | 23 | 24.8 | 23.00 x 24.80 | 22.6 x 24.4 | 570 | 551 | 1.08 | garage | 10 | option-f-your-sizes-fitted/main_floor_f.scad:40 |
| DRIVE (SLOPES UP TO GARAGE) | 0 | -16 | 23 | 0 | 23.00 x 16.00 | 23.0 x 16.0 (open) | 368 | - | 1.44 | porch | 0 | option-f-your-sizes-fitted/main_floor_f.scad:71 |
| PATIO | 49 | -10 | 61 | 0 | 12.00 x 10.00 | 12.0 x 10.0 (open) | 120 | - | 1.20 | porch | 0 | option-f-your-sizes-fitted/main_floor_f.scad:72 |
| FRONT PORCH | 89 | -8 | 96 | 0 | 7.00 x 8.00 | 7.0 x 8.0 (open) | 56 | - | 1.14 | porch | 0 | option-f-your-sizes-fitted/main_floor_f.scad:73 |
| DECK | 127 | 48 | 130 | 64 | 3.00 x 16.00 | 3.0 x 16.0 (open) | 48 | - | 5.33 | porch | 0 | option-f-your-sizes-fitted/main_floor_f.scad:74 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UTILITY | 16.6 | 24.8 | 26.6 | 41.2 | 10.00 x 16.40 | 9.2 x 15.3 | 164 | 141 | 1.64 | utility | 10 | option-f-your-sizes-fitted/basement_f.scad:37 |
| STORAGE @26.6,24.8 | 26.6 | 24.8 | 32 | 41.2 | 5.40 x 16.40 | 4.6 x 15.6 | 89 | 73 | 3.04 | closet | 10 | option-f-your-sizes-fitted/basement_f.scad:38 |
| (unlabelled hall) @23,14.4 | 23 | 14.4 | 32.4 | 24.8 | 9.40 x 10.40 | 8.3 x 9.6 | 98 | 80 | 1.11 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:39 |
| STORAGE @23,0 | 23 | 0 | 32.4 | 14.4 | 9.40 x 14.40 | 8.6 x 13.6 | 135 | 118 | 1.53 | closet | 10 | option-f-your-sizes-fitted/basement_f.scad:40 |
| BEDROOM 3 | 32.4 | 0 | 44.8 | 14.4 | 12.40 x 14.40 | 12.0 x 13.6 | 179 | 164 | 1.16 | bed | 10 | option-f-your-sizes-fitted/basement_f.scad:42 |
| JACK & JILL BATH | 44.8 | 0 | 53.2 | 14.4 | 8.40 x 14.40 | 8.0 x 13.6 | 121 | 109 | 1.71 | bath | 10 | option-f-your-sizes-fitted/basement_f.scad:43 |
| BEDROOM 4 | 53.2 | 0 | 65.6 | 14.4 | 12.40 x 14.40 | 12.0 x 13.6 | 179 | 164 | 1.16 | bed | 10 | option-f-your-sizes-fitted/basement_f.scad:44 |
| LIVING ROOM | 65.6 | 0 | 86.6 | 20.4 | 21.00 x 20.40 | 20.2 x 19.3 | 428 | 391 | 1.03 | living | 10 | option-f-your-sizes-fitted/basement_f.scad:45 |
| (basement hall) | 32.4 | 14.4 | 65.6 | 22.4 | 33.20 x 8.00 | 32.4 x 7.2 | 266 | 235 | 4.15 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:46 |
| (landing at the stair foot) | 86.6 | 0 | 92 | 4.45 | 5.40 x 4.45 | 5.0 x 3.7 | 24 | 18 | 1.21 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:48 |
| STAIR UP | 86.6 | 4.45 | 92 | 20.4 | 5.40 x 15.95 | 5.0 x 15.5 | 86 | 78 | 2.95 | stair | 10 | option-f-your-sizes-fitted/basement_f.scad:49 |
| (unlabelled hall) @92,0 | 92 | 0 | 98.4 | 20.4 | 6.40 x 20.40 | 5.3 x 19.6 | 131 | 104 | 3.19 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:50 |
| (unlabelled hall) @86.6,20.4 | 86.6 | 20.4 | 98.4 | 25.8 | 11.80 x 5.40 | 11.0 x 5.0 | 64 | 55 | 2.19 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:51 |
| CLOSET | 86.6 | 25.8 | 92 | 33.2 | 5.40 x 7.40 | 4.6 x 6.6 | 40 | 31 | 1.37 | closet | 10 | option-f-your-sizes-fitted/basement_f.scad:52 |
| ELEVATOR (FUTURE) | 92 | 25.8 | 98.4 | 33.2 | 6.40 x 7.40 | 6.0 x 6.6 | 47 | 40 | 1.16 | closet | 10 | option-f-your-sizes-fitted/basement_f.scad:53 |
| (unlabelled hall) @98.4,5 | 98.4 | 5 | 104.8 | 25.8 | 6.40 x 20.80 | 5.6 x 20.0 | 133 | 113 | 3.25 | hall | 10 | option-f-your-sizes-fitted/basement_f.scad:55 |
| FLEX / CRAFT | 104.8 | 12.4 | 114.6 | 25.8 | 9.80 x 13.40 | 9.4 x 12.6 | 131 | 119 | 1.37 | office | 10 | option-f-your-sizes-fitted/basement_f.scad:56 |
| GYM / MUSIC | 114.6 | 6 | 127 | 25.8 | 12.40 x 19.80 | 11.3 x 19.0 | 246 | 215 | 1.60 | rec | 10 | option-f-your-sizes-fitted/basement_f.scad:57 |
| THEATRE (FUTURE) | 98.4 | 25.8 | 127 | 44.6 | 28.60 x 18.80 | 27.5 x 18.0 | 538 | 496 | 1.52 | rec | 10 | option-f-your-sizes-fitted/basement_f.scad:58 |
| FUTURE ROOM | 99.6 | 44.6 | 127 | 67 | 27.40 x 22.40 | 26.3 x 21.6 | 614 | 569 | 1.22 | rec | 10 | option-f-your-sizes-fitted/basement_f.scad:59 |
| WINDOW WELL @33.5,-3.5 | 33.5 | -3.5 | 40 | 0 | 6.50 x 3.50 | 6.5 x 3.5 (open) | 23 | - | 1.86 | porch | 0 | option-f-your-sizes-fitted/basement_f.scad:61 |
| WINDOW WELL @61.5,-3.5 | 61.5 | -3.5 | 67 | 0 | 5.50 x 3.50 | 5.5 x 3.5 (open) | 19 | - | 1.57 | porch | 0 | option-f-your-sizes-fitted/basement_f.scad:62 |
| WINDOW WELL @104.8,8.4 | 104.8 | 8.4 | 111.5 | 12.4 | 6.70 x 4.00 | 6.7 x 4.0 (open) | 27 | - | 1.68 | porch | 0 | option-f-your-sizes-fitted/basement_f.scad:63 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (1.5, 0) x | 9 ft = 108 in | garage | - | DRIVE (SLOPES UP TO GARAGE) / GARAGE | option-f-your-sizes-fitted/main_floor_f.scad:79 |
| M2 | (12.5, 0) x | 9 ft = 108 in | garage | - | DRIVE (SLOPES UP TO GARAGE) / GARAGE | option-f-your-sizes-fitted/main_floor_f.scad:80 |
| M3 | (91, 0) x | 3.5 ft = 42 in | door | 1 | FRONT PORCH / FOYER | option-f-your-sizes-fitted/main_floor_f.scad:81 |
| M4 | (51, 0) x | 6 ft = 72 in | double | -1 | PATIO / DINING / NOOK | option-f-your-sizes-fitted/main_floor_f.scad:82 |
| M5 | (127, 52) y | 3 ft = 36 in | double | 1 | MASTER BEDROOM / DECK | option-f-your-sizes-fitted/main_floor_f.scad:83 |
| M6 | (23, 2) y | 3 ft = 36 in | door | 1 | GARAGE / PANTRY | option-f-your-sizes-fitted/main_floor_f.scad:85 |
| M7 | (23, 15) y | 3 ft = 36 in | door | 1 | GARAGE / MUDROOM | option-f-your-sizes-fitted/main_floor_f.scad:86 |
| M8 | (32.4, 3) y | 3 ft = 36 in | door | 1 | PANTRY / KITCHEN | option-f-your-sizes-fitted/main_floor_f.scad:87 |
| M9 | (32.4, 18.9) y | 3 ft = 36 in | door | -1 | MUDROOM / KITCHEN | option-f-your-sizes-fitted/main_floor_f.scad:88 |
| M10 | (24.5, 24.8) x | 3 ft = 36 in | door | 1 | MUDROOM / OFFICE / LIBRARY | option-f-your-sizes-fitted/main_floor_f.scad:89 |
| M11 | (47.8, 3) y | 14 ft = 168 in | full | - | KITCHEN / DINING / NOOK | option-f-your-sizes-fitted/main_floor_f.scad:91 |
| M12 | (62.2, 3) y | 14 ft = 168 in | full | - | DINING / NOOK / LIVING | option-f-your-sizes-fitted/main_floor_f.scad:92 |
| M13 | (86.6, 1.5) y | 6.5 ft = 78 in | full | - | LIVING / FOYER | option-f-your-sizes-fitted/main_floor_f.scad:93 |
| M14 | (93.5, 8.4) x | 4.5 ft = 54 in | full | - | FOYER / (junction passage) | option-f-your-sizes-fitted/main_floor_f.scad:95 |
| M15 | (93.5, 20.4) x | 4.5 ft = 54 in | full | - | (junction passage) / (junction hall) | option-f-your-sizes-fitted/main_floor_f.scad:96 |
| M16 | (87, 20.4) x | 4.8 ft = 57.6 in | full | - | STAIR DN / (junction hall) | option-f-your-sizes-fitted/main_floor_f.scad:97 |
| M17 | (87.5, 25.8) x | 3 ft = 36 in | door | 1 | (junction hall) / CLOSET @86.6,25.8 | option-f-your-sizes-fitted/main_floor_f.scad:98 |
| M18 | (94, 25.8) x | 3 ft = 36 in | door | -1 | (junction hall) / ELEVATOR (FUTURE) | option-f-your-sizes-fitted/main_floor_f.scad:99 |
| M19 | (98.4, 9) y | 3 ft = 36 in | door | 1 | (junction passage) / POWDER | option-f-your-sizes-fitted/main_floor_f.scad:100 |
| M20 | (98.4, 21.2) y | 4.5 ft = 54 in | full | - | (junction hall) / (bedroom hall) | option-f-your-sizes-fitted/main_floor_f.scad:101 |
| M21 | (100, 20.4) x | 3 ft = 36 in | door | -1 | SHARED BATH / (bedroom hall) | option-f-your-sizes-fitted/main_floor_f.scad:103 |
| M22 | (117, 20.4) x | 3 ft = 36 in | door | -1 | BEDROOM 2 / (bedroom hall) | option-f-your-sizes-fitted/main_floor_f.scad:104 |
| M23 | (114.6, 15) y | 3 ft = 36 in | door | 1 | CLOSET @106.8,12.4 / BEDROOM 2 | option-f-your-sizes-fitted/main_floor_f.scad:105 |
| M24 | (100, 25.8) x | 3 ft = 36 in | door | 1 | (bedroom hall) / LAUNDRY | option-f-your-sizes-fitted/main_floor_f.scad:106 |
| M25 | (108.1, 25.8) x | 3 ft = 36 in | door | -1 | (bedroom hall) / LINEN | option-f-your-sizes-fitted/main_floor_f.scad:107 |
| M26 | (101.5, 36.2) x | 3 ft = 36 in | door | 1 | LAUNDRY / WIC @98.4,36.2 | option-f-your-sizes-fitted/main_floor_f.scad:108 |
| M27 | (112, 25.8) x | 4 ft = 48 in | full | - | (bedroom hall) / (short hall to the primary) | option-f-your-sizes-fitted/main_floor_f.scad:109 |
| M28 | (112, 36.2) x | 4 ft = 48 in | full | - | (short hall to the primary) / (primary entry) | option-f-your-sizes-fitted/main_floor_f.scad:110 |
| M29 | (113, 44.6) x | 3 ft = 36 in | door | 1 | (primary entry) / MASTER BEDROOM | option-f-your-sizes-fitted/main_floor_f.scad:111 |
| M30 | (100.5, 44.6) x | 3 ft = 36 in | door | -1 | WIC @98.4,36.2 / MASTER BEDROOM | option-f-your-sizes-fitted/main_floor_f.scad:112 |
| M31 | (106, 44.6) x | 3 ft = 36 in | door | -1 | WIC @104.8,36.2 / MASTER BEDROOM | option-f-your-sizes-fitted/main_floor_f.scad:113 |
| M32 | (120, 44.6) x | 3 ft = 36 in | door | -1 | MASTER BATH / MASTER BEDROOM | option-f-your-sizes-fitted/main_floor_f.scad:114 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (32.4, 16) y | 4 ft = 48 in | full | - | (unlabelled hall) @23,14.4 / (basement hall) | option-f-your-sizes-fitted/basement_f.scad:68 |
| B2 | (23.8, 24.8) x | 2.8 ft = 33.6 in | door | -1 | (unlabelled hall) @23,14.4 / UTILITY | option-f-your-sizes-fitted/basement_f.scad:69 |
| B3 | (28, 24.8) x | 3 ft = 36 in | door | 1 | (unlabelled hall) @23,14.4 / STORAGE @26.6,24.8 | option-f-your-sizes-fitted/basement_f.scad:70 |
| B4 | (24, 14.4) x | 3 ft = 36 in | door | -1 | STORAGE @23,0 / (unlabelled hall) @23,14.4 | option-f-your-sizes-fitted/basement_f.scad:71 |
| B5 | (34, 14.4) x | 3 ft = 36 in | door | -1 | BEDROOM 3 / (basement hall) | option-f-your-sizes-fitted/basement_f.scad:72 |
| B6 | (45.5, 14.4) x | 3 ft = 36 in | door | -1 | JACK & JILL BATH / (basement hall) | option-f-your-sizes-fitted/basement_f.scad:73 |
| B7 | (44.8, 5) y | 3 ft = 36 in | door | 1 | BEDROOM 3 / JACK & JILL BATH | option-f-your-sizes-fitted/basement_f.scad:74 |
| B8 | (53.2, 5) y | 3 ft = 36 in | door | 1 | JACK & JILL BATH / BEDROOM 4 | option-f-your-sizes-fitted/basement_f.scad:75 |
| B9 | (55, 14.4) x | 3 ft = 36 in | door | -1 | BEDROOM 4 / (basement hall) | option-f-your-sizes-fitted/basement_f.scad:76 |
| B10 | (65.6, 16) y | 4 ft = 48 in | full | - | (basement hall) / LIVING ROOM | option-f-your-sizes-fitted/basement_f.scad:77 |
| B11 | (86.6, 0.6) y | 3 ft = 36 in | door | -1 | LIVING ROOM / (landing at the stair foot) | option-f-your-sizes-fitted/basement_f.scad:78 |
| B12 | (92, 1) y | 3 ft = 36 in | full | - | (landing at the stair foot) / (unlabelled hall) @92,0 | option-f-your-sizes-fitted/basement_f.scad:79 |
| B13 | (92, 6) y | 3.6 ft = 43.2 in | full | - | STAIR UP / (unlabelled hall) @92,0 | option-f-your-sizes-fitted/basement_f.scad:80 |
| B14 | (93, 20.4) x | 4.5 ft = 54 in | full | - | (unlabelled hall) @92,0 / (unlabelled hall) @86.6,20.4 | option-f-your-sizes-fitted/basement_f.scad:81 |
| B15 | (94, 25.8) x | 3 ft = 36 in | door | -1 | (unlabelled hall) @86.6,20.4 / ELEVATOR (FUTURE) | option-f-your-sizes-fitted/basement_f.scad:82 |
| B16 | (87.5, 25.8) x | 3 ft = 36 in | door | 1 | (unlabelled hall) @86.6,20.4 / CLOSET | option-f-your-sizes-fitted/basement_f.scad:83 |
| B17 | (98.4, 8) y | 4 ft = 48 in | full | - | (unlabelled hall) @92,0 / (unlabelled hall) @98.4,5 | option-f-your-sizes-fitted/basement_f.scad:84 |
| B18 | (98.4, 21) y | 4 ft = 48 in | full | - | (unlabelled hall) @86.6,20.4 / (unlabelled hall) @98.4,5 | option-f-your-sizes-fitted/basement_f.scad:85 |
| B19 | (104.8, 17) y | 3 ft = 36 in | door | 1 | (unlabelled hall) @98.4,5 / FLEX / CRAFT | option-f-your-sizes-fitted/basement_f.scad:86 |
| B20 | (114.6, 16) y | 3 ft = 36 in | door | 1 | FLEX / CRAFT / GYM / MUSIC | option-f-your-sizes-fitted/basement_f.scad:87 |
| B21 | (100, 25.8) x | 3 ft = 36 in | door | -1 | (unlabelled hall) @98.4,5 / THEATRE (FUTURE) | option-f-your-sizes-fitted/basement_f.scad:88 |
| B22 | (105, 44.6) x | 3 ft = 36 in | door | -1 | THEATRE (FUTURE) / FUTURE ROOM | option-f-your-sizes-fitted/basement_f.scad:89 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 19 | 19 |
| double | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 9 | 9 |
| garage | 0 | 0 | 2 | 2 |
| ALL | 0 | 0 | 32 | 32 |
| passage (door+double+slider+open) | 0 | 0 | 21 | 21 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 1 | 14 | 15 |
| full | 0 | 0 | 7 | 7 |
| ALL | 0 | 1 | 21 | 22 |
| passage (door+double+slider+open) | 0 | 1 | 14 | 15 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-f-your-sizes-fitted/main_floor_f.scad:83 | MASTER BEDROOM / DECK | double | 36 in | - |
| option-f-your-sizes-fitted/main_floor_f.scad:98 | (junction hall) / CLOSET @86.6,25.8 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:99 | (junction hall) / ELEVATOR (FUTURE) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:100 | (junction passage) / POWDER | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:103 | SHARED BATH / (bedroom hall) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:104 | BEDROOM 2 / (bedroom hall) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:105 | CLOSET @106.8,12.4 / BEDROOM 2 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:107 | (bedroom hall) / LINEN | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:108 | LAUNDRY / WIC @98.4,36.2 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:111 | (primary entry) / MASTER BEDROOM | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:112 | WIC @98.4,36.2 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:113 | WIC @104.8,36.2 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/main_floor_f.scad:114 | MASTER BATH / MASTER BEDROOM | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-f-your-sizes-fitted/basement_f.scad:70 | (unlabelled hall) @23,14.4 / STORAGE @26.6,24.8 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:71 | STORAGE @23,0 / (unlabelled hall) @23,14.4 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:72 | BEDROOM 3 / (basement hall) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:73 | JACK & JILL BATH / (basement hall) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:74 | BEDROOM 3 / JACK & JILL BATH | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:75 | JACK & JILL BATH / BEDROOM 4 | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:76 | BEDROOM 4 / (basement hall) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:82 | (unlabelled hall) @86.6,20.4 / ELEVATOR (FUTURE) | door | 36 in | 34.5 |
| option-f-your-sizes-fitted/basement_f.scad:83 | (unlabelled hall) @86.6,20.4 / CLOSET | door | 36 in | 34.5 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| KITCHEN | S | (36, 0, 'x') | 6 | 3.5 | 4 | 24.0 | option-f-your-sizes-fitted/main_floor_f.scad:119 |
| KITCHEN | N | (35, 22.4, 'x') | 8 | 3.5 | 4 | 32.0 | option-f-your-sizes-fitted/main_floor_f.scad:120 |
| DINING / NOOK | S | (48.2, 0, 'x') | 2.5 | 2.5 | 5.5 | 13.8 | option-f-your-sizes-fitted/main_floor_f.scad:121 |
| DINING / NOOK | S | (58, 0, 'x') | 3.5 | 2.5 | 5.5 | 19.2 | option-f-your-sizes-fitted/main_floor_f.scad:122 |
| LIVING | S | (68, 0, 'x') | 12 | 2 | 6 | 72.0 | option-f-your-sizes-fitted/main_floor_f.scad:123 |
| LIVING | N | (66, 20.4, 'x') | 8 | 3 | 4 | 32.0 | option-f-your-sizes-fitted/main_floor_f.scad:124 |
| OFFICE / LIBRARY | W | (16.6, 26, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-f-your-sizes-fitted/main_floor_f.scad:125 |
| OFFICE / LIBRARY | W | (16.6, 35, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-f-your-sizes-fitted/main_floor_f.scad:126 |
| OFFICE / LIBRARY | N | (20, 41.2, 'x') | 4 | 2.5 | 5 | 20.0 | option-f-your-sizes-fitted/main_floor_f.scad:127 |
| OFFICE / LIBRARY | N | (26, 41.2, 'x') | 4 | 2.5 | 5 | 20.0 | option-f-your-sizes-fitted/main_floor_f.scad:128 |
| BEDROOM 2 | S | (116, 6, 'x') | 6 | 2.5 | 5 | 30.0 | option-f-your-sizes-fitted/main_floor_f.scad:129 |
| BEDROOM 2 | E | (127, 10, 'y') | 5 | 2.5 | 5 | 25.0 | option-f-your-sizes-fitted/main_floor_f.scad:130 |
| MASTER BATH | E | (127, 30, 'y') | 3 | 4 | 3 | 9.0 | option-f-your-sizes-fitted/main_floor_f.scad:131 |
| MASTER BEDROOM | N | (103, 67, 'x') | 5 | 2.5 | 5 | 25.0 | option-f-your-sizes-fitted/main_floor_f.scad:132 |
| MASTER BEDROOM | N | (114, 67, 'x') | 6 | 2.5 | 5 | 30.0 | option-f-your-sizes-fitted/main_floor_f.scad:133 |
| MASTER BEDROOM | W | (99.6, 52, 'y') | 5 | 2.5 | 5 | 25.0 | option-f-your-sizes-fitted/main_floor_f.scad:134 |
| MASTER BEDROOM | E | (127, 60, 'y') | 4 | 2.5 | 5 | 20.0 | option-f-your-sizes-fitted/main_floor_f.scad:135 |

Total main-floor window glass (width x height): 432.0 sq ft (17 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 6, S: 5, E: 3, W: 3

Rooms with windows on 2+ walls (main): KITCHEN (N/S); LIVING (N/S); OFFICE / LIBRARY (N/W); BEDROOM 2 (E/S); MASTER BEDROOM (E/N/W)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| PANTRY | utility | 117 |
| MUDROOM | utility | 117 |
| FOYER | hall | 99 |
| (junction passage) | hall | 77 |
| (junction hall) | hall | 64 |
| CLOSET @86.6,25.8 | closet | 40 |
| ELEVATOR (FUTURE) | closet | 47 |
| POWDER | bath | 47 |
| (bedroom hall) | hall | 154 |
| SHARED BATH | bath | 67 |
| CLOSET @106.8,12.4 | closet | 62 |
| LAUNDRY | utility | 98 |
| LINEN | closet | 35 |
| (short hall to the primary) | hall | 56 |
| WIC @98.4,36.2 | closet | 54 |
| WIC @104.8,36.2 | closet | 54 |
| (primary entry) | hall | 45 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BEDROOM 3 | S | (35, 0, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:160 |
| BEDROOM 4 | S | (62, 0, 'x') | 3.6 | 3.5 | 3 | 10.8 | foundation.scad:161 |
| FLEX / CRAFT | S | (106, 12.4, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:0 |
| LIVING ROOM | S | (72, 0, 'x') | 8 | 3.5 | 3 | 24.0 | foundation.scad:0 |
| UTILITY | W | (16.6, 28, 'y') | 3 | 4 | 2 | 6.0 | foundation.scad:0 |
| UTILITY | W | (16.6, 32, 'y') | 1.5 | 4 | 2 | 3.0 | foundation.scad:0 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: STORAGE @26.6,24.8 (closet, 89 sf); (unlabelled hall) @23,14.4 (hall, 98 sf); STORAGE @23,0 (closet, 135 sf); JACK & JILL BATH (bath, 121 sf); (basement hall) (hall, 266 sf); (landing at the stair foot) (hall, 24 sf); STAIR UP (stair, 86 sf); (unlabelled hall) @92,0 (hall, 131 sf); (unlabelled hall) @86.6,20.4 (hall, 64 sf); CLOSET (closet, 40 sf); ELEVATOR (FUTURE) (closet, 47 sf); (unlabelled hall) @98.4,5 (hall, 133 sf); GYM / MUSIC (rec, 246 sf); THEATRE (FUTURE) (rec, 538 sf); FUTURE ROOM (rec, 614 sf); WINDOW WELL @33.5,-3.5 (porch, 23 sf); WINDOW WELL @61.5,-3.5 (porch, 19 sf); WINDOW WELL @104.8,8.4 (porch, 27 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (junction passage) | 92,8.4 to 98.4,20.4 | 77 | 6.0 ft clear width (72 in), length 11.6 | option-f-your-sizes-fitted/main_floor_f.scad:52 |
| (junction hall) | 86.6,20.4 to 98.4,25.8 | 64 | 5.0 ft clear width (60 in), length 11.4 | option-f-your-sizes-fitted/main_floor_f.scad:53 |
| (bedroom hall) | 98.4,20.4 to 127,25.8 | 154 | 5.0 ft clear width (60 in), length 28.2 | option-f-your-sizes-fitted/main_floor_f.scad:58 |
| (short hall to the primary) | 111.2,25.8 to 116.6,36.2 | 56 | 5.0 ft clear width (60 in), length 10.0 | option-f-your-sizes-fitted/main_floor_f.scad:64 |
| (primary entry) | 111.2,36.2 to 116.6,44.6 | 45 | 5.0 ft clear width (60 in), length 8.0 | option-f-your-sizes-fitted/main_floor_f.scad:67 |

**Circulation total (halls only): 396 sq ft = 10.7% of 3704 sq ft conditioned** (10.9% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 99 | 8.0 ft | 13.4% | option-f-your-sizes-fitted/main_floor_f.scad:50 |
| MUDROOM | 117 | 9.0 ft | 16.5% (halls+foyer+mudroom) | option-f-your-sizes-fitted/main_floor_f.scad:43 |
| STAIR DN opening (stairwell) | 65 | 5.0 ft | 18.3% (all four) | option-f-your-sizes-fitted/main_floor_f.scad:51 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (unlabelled hall) @23,14.4 | 23,14.4 to 32.4,24.8 | 98 | 8.3 ft clear width (100 in), length 9.6 | option-f-your-sizes-fitted/basement_f.scad:39 |
| (basement hall) | 32.4,14.4 to 65.6,22.4 | 266 | 7.2 ft clear width (87 in), length 32.4 | option-f-your-sizes-fitted/basement_f.scad:46 |
| (landing at the stair foot) | 86.6,0 to 92,4.45 | 24 | 3.7 ft clear width (44 in), length 5.0 | option-f-your-sizes-fitted/basement_f.scad:48 |
| (unlabelled hall) @92,0 | 92,0 to 98.4,20.4 | 131 | 5.3 ft clear width (64 in), length 19.6 | option-f-your-sizes-fitted/basement_f.scad:50 |
| (unlabelled hall) @86.6,20.4 | 86.6,20.4 to 98.4,25.8 | 64 | 5.0 ft clear width (60 in), length 11.0 | option-f-your-sizes-fitted/basement_f.scad:51 |
| (unlabelled hall) @98.4,5 | 98.4,5 to 104.8,25.8 | 133 | 5.6 ft clear width (68 in), length 20.0 | option-f-your-sizes-fitted/basement_f.scad:55 |

**Circulation total (halls only): 715 sq ft = 18.9% of 3780 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 86 | 5.0 ft | 21.2% | option-f-your-sizes-fitted/basement_f.scad:49 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): none

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | DRIVE (SLOPES UP TO GARAGE); MUDROOM; PANTRY | - |
| PANTRY | utility | GARAGE; KITCHEN | - |
| MUDROOM | utility | GARAGE; KITCHEN; OFFICE / LIBRARY | - |
| OFFICE / LIBRARY | office | MUDROOM | - |
| KITCHEN | kitchen | DINING / NOOK; MUDROOM; PANTRY | - |
| DINING / NOOK | dining | KITCHEN; LIVING; PATIO | - |
| LIVING | living | DINING / NOOK; FOYER | - |
| FOYER | hall | (junction passage); FRONT PORCH; LIVING | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (junction hall) | - |
| (junction passage) | hall | (junction hall); FOYER; POWDER | - |
| (junction hall) | hall | (bedroom hall); (junction passage); CLOSET @86.6,25.8; ELEVATOR (FUTURE); STAIR DN | - |
| CLOSET @86.6,25.8 | closet | (junction hall) | - |
| ELEVATOR (FUTURE) | closet | (junction hall) | - |
| POWDER | bath | (junction passage) | - |
| (bedroom hall) | hall | (junction hall); (short hall to the primary); BEDROOM 2; LAUNDRY; LINEN; SHARED BATH | - |
| SHARED BATH | bath | (bedroom hall) | - |
| CLOSET @106.8,12.4 | closet | BEDROOM 2 | - |
| BEDROOM 2 | bed | (bedroom hall); CLOSET @106.8,12.4 | - |
| LAUNDRY | utility | (bedroom hall); WIC @98.4,36.2 | - |
| LINEN | closet | (bedroom hall) | - |
| (short hall to the primary) | hall | (bedroom hall); (primary entry) | - |
| WIC @98.4,36.2 | closet | LAUNDRY; MASTER BEDROOM | - |
| WIC @104.8,36.2 | closet | MASTER BEDROOM | - |
| (primary entry) | hall | (short hall to the primary); MASTER BEDROOM | - |
| MASTER BATH | bath | MASTER BEDROOM | - |
| MASTER BEDROOM | bed | (primary entry); DECK; MASTER BATH; WIC @104.8,36.2; WIC @98.4,36.2 | - |
| DRIVE (SLOPES UP TO GARAGE) | porch, ceiling 0 (open zone) | GARAGE | - |
| PATIO | porch, ceiling 0 (open zone) | DINING / NOOK | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | FOYER | - |
| DECK | porch, ceiling 0 (open zone) | MASTER BEDROOM | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| UTILITY | utility | (unlabelled hall) @23,14.4 | - |
| STORAGE @26.6,24.8 | closet | (unlabelled hall) @23,14.4 | - |
| (unlabelled hall) @23,14.4 | hall | (basement hall); STORAGE @23,0; STORAGE @26.6,24.8; UTILITY | - |
| STORAGE @23,0 | closet | (unlabelled hall) @23,14.4 | - |
| BEDROOM 3 | bed | (basement hall); JACK & JILL BATH | - |
| JACK & JILL BATH | bath | (basement hall); BEDROOM 3; BEDROOM 4 | - |
| BEDROOM 4 | bed | (basement hall); JACK & JILL BATH | - |
| LIVING ROOM | living | (basement hall); (landing at the stair foot) | - |
| (basement hall) | hall | (unlabelled hall) @23,14.4; BEDROOM 3; BEDROOM 4; JACK & JILL BATH; LIVING ROOM | - |
| (landing at the stair foot) | hall | (unlabelled hall) @92,0; LIVING ROOM | - |
| STAIR UP | stair | (unlabelled hall) @92,0 | - |
| (unlabelled hall) @92,0 | hall | (landing at the stair foot); (unlabelled hall) @86.6,20.4; (unlabelled hall) @98.4,5; STAIR UP | - |
| (unlabelled hall) @86.6,20.4 | hall | (unlabelled hall) @92,0; (unlabelled hall) @98.4,5; CLOSET; ELEVATOR (FUTURE) | - |
| CLOSET | closet | (unlabelled hall) @86.6,20.4 | - |
| ELEVATOR (FUTURE) | closet | (unlabelled hall) @86.6,20.4 | - |
| (unlabelled hall) @98.4,5 | hall | (unlabelled hall) @86.6,20.4; (unlabelled hall) @92,0; FLEX / CRAFT; THEATRE (FUTURE) | - |
| FLEX / CRAFT | office | (unlabelled hall) @98.4,5; GYM / MUSIC | - |
| GYM / MUSIC | rec | FLEX / CRAFT | - |
| THEATRE (FUTURE) | rec | (unlabelled hall) @98.4,5; FUTURE ROOM | - |
| FUTURE ROOM | rec | THEATRE (FUTURE) | - |
| WINDOW WELL @33.5,-3.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @61.5,-3.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @104.8,8.4 | porch, ceiling 0 (open zone) | - | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 54.9 | FOYER > LIVING > DINING / NOOK > KITCHEN |
| front door -> range (option-f-your-sizes-fitted/main_floor_f.scad:142) | 61.3 | FOYER > LIVING > DINING / NOOK > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 34.2 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> range | 30.1 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> PANTRY centre | 20.0 | GARAGE > PANTRY |
| master bedroom centre -> WIC @98.4,36.2 centre | 20.1 | MASTER BEDROOM > WIC @98.4,36.2 |
| master bedroom centre -> WIC @104.8,36.2 centre | 16.8 | MASTER BEDROOM > WIC @104.8,36.2 |
| master bedroom centre -> LAUNDRY centre | 29.6 | MASTER BEDROOM > WIC @98.4,36.2 > LAUNDRY |
| BEDROOM 2 centre -> SHARED BATH centre | 28.7 | BEDROOM 2 > (bedroom hall) > SHARED BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 49.8 | BEDROOM 2 > (bedroom hall) > (short hall to the primary) > (primary entry) > MASTER BEDROOM > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 30.8 | BEDROOM 2 > (bedroom hall) > LAUNDRY |
| foyer centre -> POWDER centre (powder room) | 12.4 | FOYER > (junction passage) > POWDER |
| front door -> top of main stair (top nosing, (89.30, 20.4)) | 27.4 | FOYER > (junction passage) > (junction hall) |
| master bedroom centre -> top of main stair (top nosing, (89.30, 20.4)) | 48.4 | MASTER BEDROOM > WIC @98.4,36.2 > LAUNDRY > (bedroom hall) > (junction hall) |
| BEDROOM 2 centre -> top of main stair (top nosing, (89.30, 20.4)) | 37.5 | BEDROOM 2 > (bedroom hall) > (junction hall) |
| basement stair foot (89.30, 4.45) -> UTILITY centre | 82.0 | (landing at the stair foot) > LIVING ROOM > (basement hall) > (unlabelled hall) @23,14.4 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @98.4,36.2 centre: no (via MASTER BEDROOM > WIC @98.4,36.2); WIC @104.8,36.2 centre: no (via MASTER BEDROOM > WIC @104.8,36.2)

## Section 8

### 8.1 LIVING (main; option-f-your-sizes-fitted/main_floor_f.scad:48) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| DINING / NOOK | dining | 20.4 | full 168 in |
| FOYER | hall | 8.4 | full 78 in |
| STAIR DN | stairwell (ceil 0) | 12.0 | - |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are LIVING. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| BEDROOM 4 | bed | 14.4 | - |
| (basement hall) | hall | 6.0 | full 48 in |
| (landing at the stair foot) | hall | 4.5 | door 36 in |
| STAIR UP | stair | 15.9 | - |
| WINDOW WELL @61.5,-3.5 | porch (ceil 0) | 1.4 | - |

### 8.2 FOYER (option-f-your-sizes-fitted/main_floor_f.scad:50) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| LIVING | living | 8.4 | full 78 in |
| STAIR DN | stairwell (ceil 0) | 5.4 | - |
| (junction passage) | hall | 6.4 | full 54 in |
| POWDER | bath | 3.4 | - |
| FRONT PORCH | porch (ceil 0) | 7.0 | door 42 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: PANTRY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | PANTRY | option-f-your-sizes-fitted/main_floor_f.scad:42 | S 9.4 (yard/soil); W 12.4 (garage) |
| main | CLOSET @86.6,25.8 | option-f-your-sizes-fitted/main_floor_f.scad:54 | N 5.4 (yard/soil); W 7.4 (yard/soil) |
| main | ELEVATOR (FUTURE) | option-f-your-sizes-fitted/main_floor_f.scad:55 | N 6.4 (yard/soil) |
| main | CLOSET @106.8,12.4 | option-f-your-sizes-fitted/main_floor_f.scad:60 | S 7.8 (yard/soil) |
| main | LINEN | option-f-your-sizes-fitted/main_floor_f.scad:63 | none |
| main | WIC @98.4,36.2 | option-f-your-sizes-fitted/main_floor_f.scad:65 | N 1.2 (yard/soil); W 8.4 (yard/soil) |
| main | WIC @104.8,36.2 | option-f-your-sizes-fitted/main_floor_f.scad:66 | none |
| base | STORAGE @26.6,24.8 | option-f-your-sizes-fitted/basement_f.scad:38 | N 5.4 (yard/soil); E 16.4 (yard/soil) |
| base | STORAGE @23,0 | option-f-your-sizes-fitted/basement_f.scad:40 | S 9.4 (yard/soil); W 14.4 (yard/soil) |
| base | CLOSET | option-f-your-sizes-fitted/basement_f.scad:52 | N 5.4 (yard/soil); W 7.4 (yard/soil) |
| base | ELEVATOR (FUTURE) | option-f-your-sizes-fitted/basement_f.scad:53 | N 6.4 (yard/soil) |

Pantry/garage: PANTRY shares 12.4 ft of wall with the garage; doors between PANTRY and GARAGE: 1. The garage's doors to the house are: option-f-your-sizes-fitted/main_floor_f.scad:85 (GARAGE | PANTRY, 36 in); option-f-your-sizes-fitted/main_floor_f.scad:86 (GARAGE | MUDROOM, 36 in).

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | west run: oven column, range, fridge (141); fridge beside the range wall (143); sink under the north window (145); dishwasher (146); island, no seating, nothing in it (147) | front door -> kitchen/dining room centre; front door -> range (option-f-your-sizes-fitted/main_floor_f.scad:142); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 16.6 (yard/soil); S 23.0 (porch/patio (open)); W 24.8 (yard/soil) |
| PANTRY | 14.0 | loop north leg (:114) | S 9.4 (yard/soil); W 12.4 (garage) |
| KITCHEN | 14.0 | loop west leg (:115) | N 15.4 (yard/soil); S 15.4 (yard/soil) |
| DINING / NOOK | 14.0 | loop north leg (:114) | N 14.4 (yard/soil); S 12.0 (porch/patio (open)), 2.4 (yard/soil); E 2.0 (yard/soil) |
| LIVING | 14.0 | loop north leg (:114) | N 24.4 (yard/soil); S 24.4 (yard/soil) |
| FOYER | 14.0 | loop north leg (:114) | S 7.0 (porch/patio (open)), 4.8 (yard/soil); E 5.0 (yard/soil) |
| OFFICE / LIBRARY | 18.6 | west driveway (site.scad:111) | N 15.4 (yard/soil); S 6.4 (garage); E 16.4 (yard/soil); W 16.4 (yard/soil) |
| POWDER | 19.0 | loop north leg (:114) | S 6.4 (yard/soil); E 7.4 (yard/soil) |
| BEDROOM 2 | 20.0 | loop north leg (:114) | S 12.4 (yard/soil); E 14.4 (yard/soil); W 6.4 (yard/soil) |
| STAIR DN | 22.4 | loop north leg (:114) | none |
| (junction passage) | 22.4 | loop north leg (:114) | none |
| MUDROOM | 25.0 | west driveway (site.scad:111) | N 0.4 (yard/soil); E 2.4 (yard/soil); W 12.4 (garage) |
| SHARED BATH | 26.4 | loop north leg (:114) | S 2.0 (yard/soil) |
| CLOSET @106.8,12.4 | 26.4 | loop north leg (:114) | S 7.8 (yard/soil) |
| (junction hall) | 34.4 | loop north leg (:114) | W 5.4 (yard/soil) |
| (bedroom hall) | 34.4 | loop east leg (:116) | E 5.4 (yard/soil) |
| CLOSET @86.6,25.8 | 39.8 | loop north leg (:114) | N 5.4 (yard/soil); W 7.4 (yard/soil) |
| ELEVATOR (FUTURE) | 39.8 | loop north leg (:114) | N 6.4 (yard/soil) |
| LAUNDRY | 39.8 | loop north leg (:114) | W 3.0 (yard/soil) |
| LINEN | 39.8 | loop north leg (:114) | none |
| (short hall to the primary) | 39.8 | loop north leg (:114) | none |
| MASTER BATH | 39.8 | loop north leg (:114) | E 18.8 (yard/soil) |

Other rooms are > 40 ft from any drive. Garage doors (rows option-f-your-sizes-fitted/main_floor_f.scad:79, option-f-your-sizes-fitted/main_floor_f.scad:80) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (38, 20.6, 41, 21.8) | (39.5, 21.2) | N wall y=22.4 | 0.60 | option-f-your-sizes-fitted/main_floor_f.scad:145 |
| toilet/tub/wash basin (POWDER) | POWDER | (98.8, 5.4, 100.4, 7) | (99.6, 6.2) | W wall x=98.4 | 0.40 | option-f-your-sizes-fitted/main_floor_f.scad:159 |
| vanity (POWDER) | POWDER | (102.4, 5.4, 104.6, 8) | (103.5, 6.7) | E wall x=104.8 | 0.20 | option-f-your-sizes-fitted/main_floor_f.scad:160 |
| toilet/tub/wash basin (SHARED BATH) | SHARED BATH | (98.8, 13, 100.4, 14.6) | (99.6, 13.8) | W wall x=98.4 | 0.40 | option-f-your-sizes-fitted/main_floor_f.scad:162 |
| vanity (SHARED BATH) | SHARED BATH | (98.7, 15.2, 100, 19) | (99.3, 17.1) | W wall x=98.4 | 0.30 | option-f-your-sizes-fitted/main_floor_f.scad:163 |
| shower (SHARED BATH) | SHARED BATH | (102, 12.6, 106.6, 16.2) | (104.3, 14.4) | S wall y=12.4 | 0.20 | option-f-your-sizes-fitted/main_floor_f.scad:164 |
| washer/dryer (LAUNDRY) | LAUNDRY | (106.2, 26.2, 107.7, 36) | (107.0, 31.1) | E wall x=107.8 | 0.10 | option-f-your-sizes-fitted/main_floor_f.scad:168 |
| sink (LAUNDRY) | LAUNDRY | (100, 34.8, 102, 35.8) | (101.0, 35.3) | N wall y=36.2 | 0.40 | option-f-your-sizes-fitted/main_floor_f.scad:170 |
| shower (MASTER BATH) | MASTER BATH | (117, 26.2, 126.6, 33.4) | (121.8, 29.8) | S wall y=25.8 | 0.40 | option-f-your-sizes-fitted/main_floor_f.scad:175 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (117.4, 26.4, 123, 29.4) | (120.2, 27.9) | S wall y=25.8 | 0.60 | option-f-your-sizes-fitted/main_floor_f.scad:176 |
| shower (MASTER BATH) | MASTER BATH | (123.6, 26.4, 126.4, 32.6) | (125.0, 29.5) | E wall x=127 | 0.60 | option-f-your-sizes-fitted/main_floor_f.scad:177 |
| vanity (MASTER BATH) | MASTER BATH | (117, 37, 118.4, 43.4) | (117.7, 40.2) | W wall x=116.6 | 0.40 | option-f-your-sizes-fitted/main_floor_f.scad:178 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (124.8, 38, 126.4, 39.6) | (125.6, 38.8) | E wall x=127 | 0.60 | option-f-your-sizes-fitted/main_floor_f.scad:179 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| shower (JACK & JILL BATH) | JACK & JILL BATH | (45.2, 8.4, 51.4, 13.8) | (48.3, 11.1) | W wall x=44.8 | 0.40 | option-f-your-sizes-fitted/basement_f.scad:111 |
| toilet/tub/wash basin (JACK & JILL BATH) | JACK & JILL BATH | (45.2, 0.6, 47, 2.4) | (46.1, 1.5) | W wall x=44.8 | 0.40 | option-f-your-sizes-fitted/basement_f.scad:112 |
| vanity (JACK & JILL BATH) | JACK & JILL BATH | (48, 0.5, 52.4, 2) | (50.2, 1.2) | S wall y=0 | 0.50 | option-f-your-sizes-fitted/basement_f.scad:113 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER); toilet/tub/wash basin (SHARED BATH); vanity (SHARED BATH) | POWDER; SHARED BATH | x=98.4 (vertical wall) | (99.5, 12.4) |
| G2 | vanity (POWDER) | POWDER | x=104.8 (vertical wall) | (103.5, 6.7) |
| G3 | shower (SHARED BATH) | SHARED BATH | y=12.4 (horizontal wall) | (104.3, 14.4) |
| G4 | sink (KITCHEN) | KITCHEN | y=22.4 (horizontal wall) | (39.5, 21.2) |
| G5 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | MASTER BATH | x=127 (vertical wall) | (125.3, 34.1) |
| G6 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | MASTER BATH | y=25.8 (horizontal wall) | (121.0, 28.8) |
| G7 | washer/dryer (LAUNDRY) | LAUNDRY | x=107.8 (vertical wall) | (107.0, 31.1) |
| G8 | sink (LAUNDRY) | LAUNDRY | y=36.2 (horizontal wall) | (101.0, 35.3) |
| G9 | vanity (MASTER BATH) | MASTER BATH | x=116.6 (vertical wall) | (117.7, 40.2) |

**Main floor: 9 wet-wall groups** (4 back-to-back plumbing clusters of rooms: KITCHEN | POWDER+SHARED BATH | LAUNDRY | MASTER BATH)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | vanity (JACK & JILL BATH) | JACK & JILL BATH | y=0 (horizontal wall) | (50.2, 1.2) |
| G2 | shower (JACK & JILL BATH); toilet/tub/wash basin (JACK & JILL BATH) | JACK & JILL BATH | x=44.8 (vertical wall) | (47.2, 6.3) |

**Basement: 2 wet-wall groups** (1 clusters: JACK & JILL BATH)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 11/3; 6 ft: 9/2; 8 ft: 9/2; 12 ft: 9/2; inf: 9/2

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER); toilet/tub/wash basin (SHARED BATH); vanity (SHARED BATH) | (99.5,12.4) | B2 (JACK & JILL BATH) | (47.2,6.3) | 52.3 | 6.1 | 58.4 |
| G2 | vanity (POWDER) | (103.5,6.7) | B2 (JACK & JILL BATH) | (47.2,6.3) | 56.3 | 0.4 | 56.7 |
| G3 | shower (SHARED BATH) | (104.3,14.4) | B2 (JACK & JILL BATH) | (47.2,6.3) | 57.1 | 8.1 | 65.2 |
| G4 | sink (KITCHEN) | (39.5,21.2) | B2 (JACK & JILL BATH) | (47.2,6.3) | 7.7 | 14.9 | 22.6 |
| G5 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | (125.3,34.1) | B2 (JACK & JILL BATH) | (47.2,6.3) | 78.1 | 27.8 | 105.9 |
| G6 | shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | (121.0,28.8) | B2 (JACK & JILL BATH) | (47.2,6.3) | 73.8 | 22.5 | 96.3 |
| G7 | washer/dryer (LAUNDRY) | (107.0,31.1) | B2 (JACK & JILL BATH) | (47.2,6.3) | 59.8 | 24.8 | 84.5 |
| G8 | sink (LAUNDRY) | (101.0,35.3) | B2 (JACK & JILL BATH) | (47.2,6.3) | 53.8 | 29.0 | 82.8 |
| G9 | vanity (MASTER BATH) | (117.7,40.2) | B2 (JACK & JILL BATH) | (47.2,6.3) | 70.5 | 33.9 | 104.4 |

Main-floor groups with a basement group within 5 ft Manhattan: 0 of 9; within 10 ft: 0.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (99.5,12.4) | 123.0 | 103.9 |
| G2 | (103.5,6.7) | 132.6 | 113.5 |
| G3 | (104.3,14.4) | 125.7 | 106.6 |
| G4 | (39.5,21.2) | 54.1 | 35.0 |
| G5 | (125.3,34.1) | 127.0 | 107.9 |
| G6 | (121.0,28.8) | 128.0 | 108.9 |
| G7 | (107.0,31.1) | 111.7 | 92.6 |
| G8 | (101.0,35.3) | 101.5 | 82.4 |
| G9 | (117.7,40.2) | 113.3 | 96.8 |

**DRI (E = (22.16, 58)) = 1017.1 ft over 9 groups; mean 113.0 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 847.8 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:107, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:106). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **toilet/tub/wash basin (MASTER BATH), 114.8 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: toilet/tub/wash basin (MASTER BATH), 116.1 ft.
- Furthest basement fixture: **vanity (JACK & JILL BATH), 62.4 ft** from the water heater.
- Nearest main-floor fixture: sink (KITCHEN), 31.7 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 32; toilet/tub/wash basin (POWDER) 107; vanity (POWDER) 110; toilet/tub/wash basin (SHARED BATH) 99; vanity (SHARED BATH) 96; shower (SHARED BATH) 103; washer/dryer (LAUNDRY) 89; sink (LAUNDRY) 87; shower (MASTER BATH) 105; toilet/tub/wash basin (MASTER BATH) 106; shower (MASTER BATH) 109; vanity (MASTER BATH) 108; toilet/tub/wash basin (MASTER BATH) 115; shower (JACK & JILL BATH) 51; toilet/tub/wash basin (JACK & JILL BATH) 58; vanity (JACK & JILL BATH) 62

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-f-your-sizes-fitted/main_floor_f.scad:51 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-f-your-sizes-fitted/basement_f.scad:49 |
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
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 17.4 ft (5.3 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 81.7 ft (24.9 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 81.6 ft (24.9 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 24.4 ft (7.4 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 22.8 ft (7.0 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 63.0 ft (19.2 m) |
| House incl. porches/deck to future shop | 63.0 ft (19.2 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

