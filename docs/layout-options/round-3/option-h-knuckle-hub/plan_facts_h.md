# Plan facts (variant mode)

main = `/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/main_floor_h.scad`, basement = `/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/basement_h.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/main_floor_h.scad`; basement = `/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/basement_h.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 3,428 | 3427.8; excl. stair opening 3362.9 |
| Building area, centre lines (house + attached garage) | 372.0 m2 | 4004 sq ft |
| Building area, outside face | 388.3 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 3,571 sq ft | centre lines 3,428 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 2,551 sq ft | centre lines 2,410 sq ft |
| Circulation % (strict / with foyer) | 9.9% / 12.0% | 341 sq ft strict of 3428 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 16 | type `door` rows, by opening width |
| Double / open counts (main) | 2 / 0 | type `double` / type `open` |
| Minimum hall clear width | 5.60 ft ((unlabelled hall) @60,22.4) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 3.60 ft ((unlabelled hall) @55.4,22.4) |
| Wet-wall groups (main / basement) | 10 / 3 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 0 of 10 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 596.6 ft | alternate exit (22.16, 38.9): 466.7 ft |
| Water heater -> furthest fixture (main / basement) | 83.1 ft (sink (KITCHEN)) / 65.3 ft (vanity (BATH)) | water heater at (27.5, 44.1); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 27.8 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 4:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 12.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: N(yard 12.0) E(yard 12.0) ;; MASTER BEDROOM: N(yard 28.0) E(yard 10.0) W(porch/patio 12.0, yard 10.0) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 36.5) S(yard 9.0) E(yard 10.0) W(porch/patio 12.0, yard 22.0) | suite rooms: WIC @44,36.4, WIC @38,36.4, ENSUITE, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (22.0 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 5: LIVING (N/S/W); DINING / NOOK (E/S); BEDROOM 2 (E/N); MASTER BEDROOM (N/W); ENSUITE (S/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 50..55.4, y 26.4; basement foot room x 50..55.4, y 10.45; **moved** (x offset +0.00/+0.00 ft, run 15.950 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 37.1 ft (MASTER BEDROOM) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_h.scad (defaults): 29 rooms, 33 doors, 19 windows - OK ; basement_h.scad (defaults): 24 rooms, 20 doors, 6 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 3427.8 | computed: sum (x1-x0)*(y1-y0) over 24 rows, main_floor.scad:41-73 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 64.8 | option-h-knuckle-hub/main_floor_h.scad:48 |
| Main-floor conditioned excluding the stair opening | 3362.9 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 3427.8 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 2501.6 | computed over basement.scad:33-60 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 576.0 | option-h-knuckle-hub/main_floor_h.scad:41 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| DRIVE (LEVEL TO GARAGE DOORS) | 1848.0 | option-h-knuckle-hub/main_floor_h.scad:70 |
| PATIO | 120.0 | option-h-knuckle-hub/main_floor_h.scad:71 |
| FRONT PORCH | 80.0 | option-h-knuckle-hub/main_floor_h.scad:72 |
| DECK | 72.0 | option-h-knuckle-hub/main_floor_h.scad:73 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 2120.0 sq ft. PATIO alone: 120.0; DECK alone: 72.0. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 284.8 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 237.3 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 32.0 ft | same |
|   facing garage | 15.5 ft | same (garage is unheated) |
| Outside (convex) corners | 13 | vertices of the union polygon after 0.02 ft simplify (22 vertices) |
| Inside (reflex) corners | 9 | same polygon |
| Bounding box, heated rooms | x 26..91 (65 ft), y 0..70.4 (70.4 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 26..127 (101 ft), y -16..70.4 (86.4 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 10 hip-roof blocks in main_roof (main_floor.scad:239); each hip block is 4 sloped facets, so 4 x 10 = 40 nominal facets before overlapping blocks merge; 0 blocks at 6/12 pitch, 10 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| LIVING | N 7.0 (yard/soil); S 22.0 (yard/soil); W 20.4 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:41 |
| VESTIBULE | S 9.6 (porch/patio (open)) | option-h-knuckle-hub/main_floor_h.scad:42 |
| POWDER | S 0.4 (porch/patio (open)), 6.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:43 |
| DINING / NOOK | S 19.0 (yard/soil); E 10.0 (porch/patio (open)), 4.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:44 |
| KITCHEN | S 3.0 (yard/soil); E 15.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:45 |
| FOYER | none | option-h-knuckle-hub/main_floor_h.scad:47 |
| STAIR DN | none | option-h-knuckle-hub/main_floor_h.scad:48 |
| (unlabelled hall) @55.4,14.4 | none | option-h-knuckle-hub/main_floor_h.scad:49 |
| (unlabelled hall) @55.4,22.4 | none | option-h-knuckle-hub/main_floor_h.scad:50 |
| (stair-top landing) | none | option-h-knuckle-hub/main_floor_h.scad:51 |
| (unlabelled hall) @60,22.4 | none | option-h-knuckle-hub/main_floor_h.scad:52 |
| OFFICE / LIBRARY | W 16.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:53 |
| MUDROOM | N 3.5 (yard/soil); E 3.5 (garage) | option-h-knuckle-hub/main_floor_h.scad:55 |
| PANTRY | N 12.0 (garage); S 3.0 (yard/soil); E 8.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:56 |
| (the bedroom hall) | none | option-h-knuckle-hub/main_floor_h.scad:59 |
| ELEVATOR (FUTURE) | none | option-h-knuckle-hub/main_floor_h.scad:60 |
| LINEN | none | option-h-knuckle-hub/main_floor_h.scad:61 |
| SHARED BATH | none | option-h-knuckle-hub/main_floor_h.scad:62 |
| WIC @44,36.4 | none | option-h-knuckle-hub/main_floor_h.scad:63 |
| WIC @38,36.4 | none | option-h-knuckle-hub/main_floor_h.scad:64 |
| ENSUITE | N 8.5 (yard/soil); S 9.0 (yard/soil); W 12.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:65 |
| LAUNDRY | N 1.0 (yard/soil); E 7.9 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:66 |
| BEDROOM 2 | N 12.0 (yard/soil); E 12.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:67 |
| MASTER BEDROOM | N 28.0 (yard/soil); E 10.0 (yard/soil); W 12.0 (porch/patio (open)), 10.0 (yard/soil) | option-h-knuckle-hub/main_floor_h.scad:68 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LIVING | 28 | 0 | 50 | 20.4 | 22.00 x 20.40 | 21.6 x 20.0 | 449 | 432 | 1.08 | living | 10 | option-h-knuckle-hub/main_floor_h.scad:41 |
| VESTIBULE | 50 | 0 | 59.6 | 7.4 | 9.60 x 7.40 | 9.2 x 7.0 | 71 | 64 | 1.30 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:42 |
| POWDER | 59.6 | 0 | 66 | 7.4 | 6.40 x 7.40 | 6.0 x 7.0 | 47 | 42 | 1.16 | bath | 10 | option-h-knuckle-hub/main_floor_h.scad:43 |
| DINING / NOOK | 66 | 0 | 85 | 14 | 19.00 x 14.00 | 18.6 x 13.6 | 266 | 253 | 1.36 | dining | 10 | option-h-knuckle-hub/main_floor_h.scad:44 |
| KITCHEN | 66 | 14 | 88 | 29 | 22.00 x 15.00 | 21.6 x 14.6 | 330 | 315 | 1.47 | kitchen | 10 | option-h-knuckle-hub/main_floor_h.scad:45 |
| FOYER | 50 | 7.4 | 66 | 14.4 | 16.00 x 7.00 | 15.6 x 6.6 | 112 | 103 | 2.29 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:47 |
| STAIR DN | 50 | 14.4 | 55.4 | 26.4 | 5.40 x 12.00 | 5.0 x 11.6 | 65 | - | 2.22 | stairwell | 0 | option-h-knuckle-hub/main_floor_h.scad:48 |
| (unlabelled hall) @55.4,14.4 | 55.4 | 14.4 | 66 | 22.4 | 10.60 x 8.00 | 10.2 x 7.6 | 85 | 78 | 1.33 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:49 |
| (unlabelled hall) @55.4,22.4 | 55.4 | 22.4 | 60 | 26.4 | 4.60 x 4.00 | 4.2 x 3.6 | 18 | 15 | 1.15 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:50 |
| (stair-top landing) | 50 | 26.4 | 60 | 33 | 10.00 x 6.60 | 9.6 x 6.2 | 66 | 60 | 1.52 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:51 |
| (unlabelled hall) @60,22.4 | 60 | 22.4 | 66 | 33 | 6.00 x 10.60 | 5.6 x 10.2 | 64 | 57 | 1.77 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:52 |
| OFFICE / LIBRARY | 35 | 20.4 | 50 | 36.4 | 15.00 x 16.00 | 14.6 x 15.6 | 240 | 228 | 1.07 | office | 10 | option-h-knuckle-hub/main_floor_h.scad:53 |
| MUDROOM | 66 | 29 | 79 | 40.5 | 13.00 x 11.50 | 12.6 x 11.1 | 150 | 140 | 1.13 | utility | 10 | option-h-knuckle-hub/main_floor_h.scad:55 |
| PANTRY | 79 | 29 | 91 | 37 | 12.00 x 8.00 | 11.6 x 7.6 | 96 | 88 | 1.50 | utility | 10 | option-h-knuckle-hub/main_floor_h.scad:56 |
| (the bedroom hall) | 59 | 33 | 66 | 48.4 | 7.00 x 15.40 | 6.6 x 15.0 | 108 | 99 | 2.20 | hall | 10 | option-h-knuckle-hub/main_floor_h.scad:59 |
| ELEVATOR (FUTURE) | 53 | 33 | 59 | 40 | 6.00 x 7.00 | 5.6 x 6.6 | 42 | 37 | 1.17 | closet | 10 | option-h-knuckle-hub/main_floor_h.scad:60 |
| LINEN | 50 | 33 | 53 | 40 | 3.00 x 7.00 | 2.6 x 6.6 | 21 | 17 | 2.33 | closet | 10 | option-h-knuckle-hub/main_floor_h.scad:61 |
| SHARED BATH | 50 | 40 | 59 | 48.4 | 9.00 x 8.40 | 8.6 x 8.0 | 76 | 69 | 1.07 | bath | 10 | option-h-knuckle-hub/main_floor_h.scad:62 |
| WIC @44,36.4 | 44 | 36.4 | 50 | 48.4 | 6.00 x 12.00 | 5.6 x 11.6 | 72 | 65 | 2.00 | closet | 10 | option-h-knuckle-hub/main_floor_h.scad:63 |
| WIC @38,36.4 | 38 | 36.4 | 44 | 48.4 | 6.00 x 12.00 | 5.6 x 11.6 | 72 | 65 | 2.00 | closet | 10 | option-h-knuckle-hub/main_floor_h.scad:64 |
| ENSUITE | 26 | 36.4 | 38 | 48.4 | 12.00 x 12.00 | 11.6 x 11.6 | 144 | 135 | 1.00 | bath | 10 | option-h-knuckle-hub/main_floor_h.scad:65 |
| LAUNDRY | 66 | 40.5 | 75.5 | 48.4 | 9.50 x 7.90 | 9.1 x 7.5 | 75 | 68 | 1.20 | utility | 10 | option-h-knuckle-hub/main_floor_h.scad:66 |
| BEDROOM 2 | 62.5 | 48.4 | 74.5 | 60.4 | 12.00 x 12.00 | 11.6 x 11.6 | 144 | 135 | 1.00 | bed | 10 | option-h-knuckle-hub/main_floor_h.scad:67 |
| MASTER BEDROOM | 34.5 | 48.4 | 62.5 | 70.4 | 28.00 x 22.00 | 27.6 x 21.6 | 616 | 596 | 1.27 | bed | 10 | option-h-knuckle-hub/main_floor_h.scad:68 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 79 | 37 | 103 | 61 | 24.00 x 24.00 | 23.6 x 23.6 | 576 | 557 | 1.00 | garage | 10 | option-h-knuckle-hub/main_floor_h.scad:57 |
| DRIVE (LEVEL TO GARAGE DOORS) | 103 | -16 | 127 | 61 | 24.00 x 77.00 | 24.0 x 77.0 (open) | 1848 | - | 3.21 | porch | 0 | option-h-knuckle-hub/main_floor_h.scad:70 |
| PATIO | 85 | 1 | 97 | 11 | 12.00 x 10.00 | 12.0 x 10.0 (open) | 120 | - | 1.20 | porch | 0 | option-h-knuckle-hub/main_floor_h.scad:71 |
| FRONT PORCH | 50 | -8 | 60 | 0 | 10.00 x 8.00 | 10.0 x 8.0 (open) | 80 | - | 1.25 | porch | 0 | option-h-knuckle-hub/main_floor_h.scad:72 |
| DECK | 28.5 | 54 | 34.5 | 66 | 6.00 x 12.00 | 6.0 x 12.0 (open) | 72 | - | 2.00 | porch | 0 | option-h-knuckle-hub/main_floor_h.scad:73 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LIVING ROOM | 28 | 0 | 50 | 20.4 | 22.00 x 20.40 | 20.9 x 19.3 | 449 | 403 | 1.08 | living | 10 | option-h-knuckle-hub/basement_h.scad:33 |
| (landing at the stair foot) | 50 | 0 | 66 | 10.45 | 16.00 x 10.45 | 15.6 x 9.7 | 167 | 151 | 1.53 | hall | 10 | option-h-knuckle-hub/basement_h.scad:35 |
| STAIR UP | 50 | 10.45 | 55.4 | 26.4 | 5.40 x 15.95 | 5.0 x 15.5 | 86 | 78 | 2.95 | stair | 10 | option-h-knuckle-hub/basement_h.scad:36 |
| (unlabelled hall) @55.4,10.45 | 55.4 | 10.45 | 66 | 22.4 | 10.60 x 11.95 | 10.2 x 11.5 | 127 | 118 | 1.13 | hall | 10 | option-h-knuckle-hub/basement_h.scad:37 |
| (unlabelled hall) @55.4,22.4 | 55.4 | 22.4 | 60 | 26.4 | 4.60 x 4.00 | 4.2 x 3.6 | 18 | 15 | 1.15 | hall | 10 | option-h-knuckle-hub/basement_h.scad:38 |
| (unlabelled hall) @50,26.4 | 50 | 26.4 | 60 | 33 | 10.00 x 6.60 | 9.6 x 6.2 | 66 | 60 | 1.52 | hall | 10 | option-h-knuckle-hub/basement_h.scad:39 |
| (unlabelled hall) @50,33 | 50 | 33 | 53 | 36.4 | 3.00 x 3.40 | 2.6 x 3.0 | 10 | 8 | 1.13 | hall | 10 | option-h-knuckle-hub/basement_h.scad:40 |
| (unlabelled hall) @60,22.4 | 60 | 22.4 | 66 | 33 | 6.00 x 10.60 | 5.6 x 10.2 | 64 | 57 | 1.77 | hall | 10 | option-h-knuckle-hub/basement_h.scad:41 |
| ELEVATOR (FUTURE) | 53 | 33 | 59 | 40 | 6.00 x 7.00 | 5.6 x 6.6 | 42 | 37 | 1.17 | closet | 10 | option-h-knuckle-hub/basement_h.scad:42 |
| STORAGE @35,20.4 | 35 | 20.4 | 50 | 36.4 | 15.00 x 16.00 | 14.2 x 15.6 | 240 | 222 | 1.07 | utility | 10 | option-h-knuckle-hub/basement_h.scad:43 |
| (unlabelled hall) @66,13 | 66 | 13 | 80 | 18.4 | 14.00 x 5.40 | 13.2 x 4.6 | 76 | 62 | 2.59 | hall | 10 | option-h-knuckle-hub/basement_h.scad:45 |
| BEDROOM 3 | 66 | 0 | 78 | 13 | 12.00 x 13.00 | 10.9 x 12.2 | 156 | 133 | 1.08 | bed | 10 | option-h-knuckle-hub/basement_h.scad:46 |
| BEDROOM 4 | 74 | 18.4 | 88 | 29 | 14.00 x 10.60 | 13.2 x 9.5 | 148 | 126 | 1.32 | bed | 10 | option-h-knuckle-hub/basement_h.scad:47 |
| BATH | 66 | 18.4 | 74 | 26.4 | 8.00 x 8.00 | 7.6 x 7.6 | 64 | 58 | 1.00 | bath | 10 | option-h-knuckle-hub/basement_h.scad:48 |
| STORAGE @66,26.4 | 66 | 26.4 | 74 | 40.5 | 8.00 x 14.10 | 7.2 x 13.3 | 113 | 97 | 1.76 | utility | 10 | option-h-knuckle-hub/basement_h.scad:49 |
| (unlabelled hall) @59,33 | 59 | 33 | 66 | 48.4 | 7.00 x 15.40 | 5.9 x 14.6 | 108 | 86 | 2.20 | hall | 10 | option-h-knuckle-hub/basement_h.scad:51 |
| FLEX / CRAFT | 62.5 | 48.4 | 74.5 | 60.4 | 12.00 x 12.00 | 10.9 x 10.9 | 144 | 119 | 1.00 | office | 10 | option-h-knuckle-hub/basement_h.scad:52 |
| (unlabelled hall) @38,40 | 38 | 40 | 59 | 46.4 | 21.00 x 6.40 | 20.6 x 5.6 | 134 | 116 | 3.28 | hall | 10 | option-h-knuckle-hub/basement_h.scad:53 |
| STORAGE @38,36.4 | 38 | 36.4 | 53 | 40 | 15.00 x 3.60 | 14.6 x 3.2 | 54 | 47 | 4.17 | utility | 10 | option-h-knuckle-hub/basement_h.scad:54 |
| UTILITY | 26 | 36.4 | 38 | 48.4 | 12.00 x 12.00 | 10.9 x 10.9 | 144 | 119 | 1.00 | utility | 10 | option-h-knuckle-hub/basement_h.scad:55 |
| WINDOW WELL @32.5,-3.5 | 32.5 | -3.5 | 42 | 0 | 9.50 x 3.50 | 9.5 x 3.5 (open) | 33 | - | 2.71 | porch | 0 | option-h-knuckle-hub/basement_h.scad:57 |
| WINDOW WELL @69,-3.5 | 69 | -3.5 | 74.5 | 0 | 5.50 x 3.50 | 5.5 x 3.5 (open) | 19 | - | 1.57 | porch | 0 | option-h-knuckle-hub/basement_h.scad:58 |
| WINDOW WELL @88,21 | 88 | 21 | 91.5 | 26 | 3.50 x 5.00 | 3.5 x 5.0 (open) | 18 | - | 1.43 | porch | 0 | option-h-knuckle-hub/basement_h.scad:59 |
| WINDOW WELL @65,60.4 | 65 | 60.4 | 71 | 64 | 6.00 x 3.60 | 6.0 x 3.6 (open) | 22 | - | 1.67 | porch | 0 | option-h-knuckle-hub/basement_h.scad:60 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (103, 40) y | 9 ft = 108 in | garage | - | GARAGE / DRIVE (LEVEL TO GARAGE DOORS) | option-h-knuckle-hub/main_floor_h.scad:78 |
| M2 | (103, 50) y | 9 ft = 108 in | garage | - | GARAGE / DRIVE (LEVEL TO GARAGE DOORS) | option-h-knuckle-hub/main_floor_h.scad:79 |
| M3 | (54.5, 0) x | 3.5 ft = 42 in | door | 1 | FRONT PORCH / VESTIBULE | option-h-knuckle-hub/main_floor_h.scad:80 |
| M4 | (85, 3) y | 6 ft = 72 in | double | 1 | DINING / NOOK / PATIO | option-h-knuckle-hub/main_floor_h.scad:81 |
| M5 | (34.5, 55) y | 6 ft = 72 in | double | -1 | DECK / MASTER BEDROOM | option-h-knuckle-hub/main_floor_h.scad:82 |
| M6 | (51, 7.4) x | 3 ft = 36 in | door | 1 | VESTIBULE / FOYER | option-h-knuckle-hub/main_floor_h.scad:84 |
| M7 | (62, 7.4) x | 3 ft = 36 in | door | -1 | POWDER / FOYER | option-h-knuckle-hub/main_floor_h.scad:85 |
| M8 | (50, 8.5) y | 5 ft = 60 in | full | - | LIVING / FOYER | option-h-knuckle-hub/main_floor_h.scad:86 |
| M9 | (66, 8) y | 4 ft = 48 in | full | - | FOYER / DINING / NOOK | option-h-knuckle-hub/main_floor_h.scad:87 |
| M10 | (66, 17) y | 4 ft = 48 in | full | - | (unlabelled hall) @55.4,14.4 / KITCHEN | option-h-knuckle-hub/main_floor_h.scad:88 |
| M11 | (57, 14.4) x | 6 ft = 72 in | full | - | FOYER / (unlabelled hall) @55.4,14.4 | option-h-knuckle-hub/main_floor_h.scad:89 |
| M12 | (56, 22.4) x | 3.5 ft = 42 in | full | - | (unlabelled hall) @55.4,14.4 / (unlabelled hall) @55.4,22.4 | option-h-knuckle-hub/main_floor_h.scad:90 |
| M13 | (56, 26.4) x | 4 ft = 48 in | full | - | (unlabelled hall) @55.4,22.4 / (stair-top landing) | option-h-knuckle-hub/main_floor_h.scad:91 |
| M14 | (61, 22.4) x | 4 ft = 48 in | full | - | (unlabelled hall) @55.4,14.4 / (unlabelled hall) @60,22.4 | option-h-knuckle-hub/main_floor_h.scad:92 |
| M15 | (60, 28) y | 4 ft = 48 in | full | - | (stair-top landing) / (unlabelled hall) @60,22.4 | option-h-knuckle-hub/main_floor_h.scad:93 |
| M16 | (50.2, 26.4) x | 5.2 ft = 62.4 in | full | - | STAIR DN / (stair-top landing) | option-h-knuckle-hub/main_floor_h.scad:94 |
| M17 | (50, 28) y | 4 ft = 48 in | full | - | OFFICE / LIBRARY / (stair-top landing) | option-h-knuckle-hub/main_floor_h.scad:95 |
| M18 | (60, 33) x | 4 ft = 48 in | full | - | (unlabelled hall) @60,22.4 / (the bedroom hall) | option-h-knuckle-hub/main_floor_h.scad:96 |
| M19 | (77, 14) x | 8 ft = 96 in | full | - | DINING / NOOK / KITCHEN | option-h-knuckle-hub/main_floor_h.scad:98 |
| M20 | (66, 30) y | 3 ft = 36 in | door | 1 | (unlabelled hall) @60,22.4 / MUDROOM | option-h-knuckle-hub/main_floor_h.scad:99 |
| M21 | (79, 37.3) y | 3 ft = 36 in | door | 1 | MUDROOM / GARAGE | option-h-knuckle-hub/main_floor_h.scad:100 |
| M22 | (79, 30) y | 3 ft = 36 in | door | 1 | MUDROOM / PANTRY | option-h-knuckle-hub/main_floor_h.scad:101 |
| M23 | (80, 29) x | 3 ft = 36 in | door | -1 | KITCHEN / PANTRY | option-h-knuckle-hub/main_floor_h.scad:102 |
| M24 | (83, 37) x | 3 ft = 36 in | door | 1 | PANTRY / GARAGE | option-h-knuckle-hub/main_floor_h.scad:103 |
| M25 | (59, 34) y | 3 ft = 36 in | door | -1 | ELEVATOR (FUTURE) / (the bedroom hall) | option-h-knuckle-hub/main_floor_h.scad:105 |
| M26 | (59, 43) y | 3 ft = 36 in | door | -1 | SHARED BATH / (the bedroom hall) | option-h-knuckle-hub/main_floor_h.scad:106 |
| M27 | (50, 40) x | 3 ft = 36 in | full | - | LINEN / SHARED BATH | option-h-knuckle-hub/main_floor_h.scad:107 |
| M28 | (66, 43) y | 3 ft = 36 in | door | 1 | (the bedroom hall) / LAUNDRY | option-h-knuckle-hub/main_floor_h.scad:108 |
| M29 | (59, 48.4) x | 3 ft = 36 in | door | 1 | (the bedroom hall) / MASTER BEDROOM | option-h-knuckle-hub/main_floor_h.scad:109 |
| M30 | (63, 48.4) x | 3 ft = 36 in | door | 1 | (the bedroom hall) / BEDROOM 2 | option-h-knuckle-hub/main_floor_h.scad:110 |
| M31 | (39, 48.4) x | 3 ft = 36 in | door | -1 | WIC @38,36.4 / MASTER BEDROOM | option-h-knuckle-hub/main_floor_h.scad:112 |
| M32 | (45, 48.4) x | 3 ft = 36 in | door | -1 | WIC @44,36.4 / MASTER BEDROOM | option-h-knuckle-hub/main_floor_h.scad:113 |
| M33 | (35, 48.4) x | 3 ft = 36 in | door | 1 | ENSUITE / MASTER BEDROOM | option-h-knuckle-hub/main_floor_h.scad:114 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (50, 2) y | 4 ft = 48 in | full | - | LIVING ROOM / (landing at the stair foot) | option-h-knuckle-hub/basement_h.scad:65 |
| B2 | (57, 10.45) x | 6 ft = 72 in | full | - | (landing at the stair foot) / (unlabelled hall) @55.4,10.45 | option-h-knuckle-hub/basement_h.scad:66 |
| B3 | (50.2, 26.4) x | 5.2 ft = 62.4 in | full | - | STAIR UP / (unlabelled hall) @50,26.4 | option-h-knuckle-hub/basement_h.scad:67 |
| B4 | (56, 22.4) x | 3.5 ft = 42 in | full | - | (unlabelled hall) @55.4,10.45 / (unlabelled hall) @55.4,22.4 | option-h-knuckle-hub/basement_h.scad:68 |
| B5 | (56, 26.4) x | 4 ft = 48 in | full | - | (unlabelled hall) @55.4,22.4 / (unlabelled hall) @50,26.4 | option-h-knuckle-hub/basement_h.scad:69 |
| B6 | (61, 22.4) x | 4 ft = 48 in | full | - | (unlabelled hall) @55.4,10.45 / (unlabelled hall) @60,22.4 | option-h-knuckle-hub/basement_h.scad:70 |
| B7 | (60, 28) y | 4 ft = 48 in | full | - | (unlabelled hall) @50,26.4 / (unlabelled hall) @60,22.4 | option-h-knuckle-hub/basement_h.scad:71 |
| B8 | (50.2, 33) x | 2.7 ft = 32.4 in | full | - | (unlabelled hall) @50,26.4 / (unlabelled hall) @50,33 | option-h-knuckle-hub/basement_h.scad:72 |
| B9 | (59, 34) y | 3 ft = 36 in | door | 1 | ELEVATOR (FUTURE) / (unlabelled hall) @59,33 | option-h-knuckle-hub/basement_h.scad:73 |
| B10 | (50, 27) y | 3 ft = 36 in | door | -1 | STORAGE @35,20.4 / (unlabelled hall) @50,26.4 | option-h-knuckle-hub/basement_h.scad:74 |
| B11 | (66, 14.5) y | 3.5 ft = 42 in | full | - | (unlabelled hall) @55.4,10.45 / (unlabelled hall) @66,13 | option-h-knuckle-hub/basement_h.scad:75 |
| B12 | (70, 13) x | 3 ft = 36 in | door | 1 | BEDROOM 3 / (unlabelled hall) @66,13 | option-h-knuckle-hub/basement_h.scad:76 |
| B13 | (77, 18.4) x | 3 ft = 36 in | door | 1 | (unlabelled hall) @66,13 / BEDROOM 4 | option-h-knuckle-hub/basement_h.scad:77 |
| B14 | (70, 18.4) x | 3 ft = 36 in | door | 1 | (unlabelled hall) @66,13 / BATH | option-h-knuckle-hub/basement_h.scad:78 |
| B15 | (70, 26.4) x | 3 ft = 36 in | door | 1 | BATH / STORAGE @66,26.4 | option-h-knuckle-hub/basement_h.scad:79 |
| B16 | (60, 33) x | 4 ft = 48 in | full | - | (unlabelled hall) @60,22.4 / (unlabelled hall) @59,33 | option-h-knuckle-hub/basement_h.scad:80 |
| B17 | (63, 48.4) x | 3 ft = 36 in | door | 1 | (unlabelled hall) @59,33 / FLEX / CRAFT | option-h-knuckle-hub/basement_h.scad:81 |
| B18 | (59, 41) y | 4 ft = 48 in | full | - | (unlabelled hall) @38,40 / (unlabelled hall) @59,33 | option-h-knuckle-hub/basement_h.scad:82 |
| B19 | (38, 42) y | 3 ft = 36 in | door | -1 | UTILITY / (unlabelled hall) @38,40 | option-h-knuckle-hub/basement_h.scad:83 |
| B20 | (45, 40) x | 3 ft = 36 in | door | -1 | STORAGE @38,36.4 / (unlabelled hall) @38,40 | option-h-knuckle-hub/basement_h.scad:84 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 16 | 16 |
| double | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 13 | 13 |
| garage | 0 | 0 | 2 | 2 |
| ALL | 0 | 0 | 33 | 33 |
| passage (door+double+slider+open) | 0 | 0 | 18 | 18 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 9 | 9 |
| full | 0 | 1 | 10 | 11 |
| ALL | 0 | 1 | 19 | 20 |
| passage (door+double+slider+open) | 0 | 0 | 9 | 9 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-h-knuckle-hub/main_floor_h.scad:82 | DECK / MASTER BEDROOM | double | 72 in | - |
| option-h-knuckle-hub/main_floor_h.scad:85 | POWDER / FOYER | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:105 | ELEVATOR (FUTURE) / (the bedroom hall) | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:106 | SHARED BATH / (the bedroom hall) | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:107 | LINEN / SHARED BATH | full | 36 in | - |
| option-h-knuckle-hub/main_floor_h.scad:109 | (the bedroom hall) / MASTER BEDROOM | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:110 | (the bedroom hall) / BEDROOM 2 | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:112 | WIC @38,36.4 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:113 | WIC @44,36.4 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-h-knuckle-hub/main_floor_h.scad:114 | ENSUITE / MASTER BEDROOM | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-h-knuckle-hub/basement_h.scad:73 | ELEVATOR (FUTURE) / (unlabelled hall) @59,33 | door | 36 in | 34.5 |
| option-h-knuckle-hub/basement_h.scad:76 | BEDROOM 3 / (unlabelled hall) @66,13 | door | 36 in | 34.5 |
| option-h-knuckle-hub/basement_h.scad:77 | (unlabelled hall) @66,13 / BEDROOM 4 | door | 36 in | 34.5 |
| option-h-knuckle-hub/basement_h.scad:78 | (unlabelled hall) @66,13 / BATH | door | 36 in | 34.5 |
| option-h-knuckle-hub/basement_h.scad:79 | BATH / STORAGE @66,26.4 | door | 36 in | 34.5 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| VESTIBULE | S | (50.8, 0, 'x') | 3 | 0.5 | 6.5 | 19.5 | option-h-knuckle-hub/main_floor_h.scad:119 |
| LIVING | S | (34, 0, 'x') | 12 | 2 | 6 | 72.0 | option-h-knuckle-hub/main_floor_h.scad:120 |
| LIVING | W | (28, 6, 'y') | 5 | 2.5 | 5 | 25.0 | option-h-knuckle-hub/main_floor_h.scad:121 |
| LIVING | N | (29, 20.4, 'x') | 4 | 3 | 4 | 16.0 | option-h-knuckle-hub/main_floor_h.scad:122 |
| DINING / NOOK | S | (70, 0, 'x') | 8 | 3 | 4.5 | 36.0 | option-h-knuckle-hub/main_floor_h.scad:123 |
| DINING / NOOK | E | (85, 10, 'y') | 3 | 2.5 | 5 | 15.0 | option-h-knuckle-hub/main_floor_h.scad:124 |
| KITCHEN | E | (88, 17, 'y') | 6 | 3.5 | 4 | 24.0 | option-h-knuckle-hub/main_floor_h.scad:125 |
| OFFICE / LIBRARY | W | (35, 22, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-h-knuckle-hub/main_floor_h.scad:126 |
| OFFICE / LIBRARY | W | (35, 29, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-h-knuckle-hub/main_floor_h.scad:127 |
| PANTRY | E | (91, 31, 'y') | 3 | 4 | 3 | 9.0 | option-h-knuckle-hub/main_floor_h.scad:128 |
| BEDROOM 2 | N | (65.5, 60.4, 'x') | 6 | 2.5 | 5 | 30.0 | option-h-knuckle-hub/main_floor_h.scad:129 |
| BEDROOM 2 | E | (74.5, 52, 'y') | 4 | 2.5 | 5 | 20.0 | option-h-knuckle-hub/main_floor_h.scad:130 |
| LAUNDRY | E | (75.5, 43, 'y') | 3 | 3.5 | 3.5 | 10.5 | option-h-knuckle-hub/main_floor_h.scad:131 |
| MASTER BEDROOM | W | (34.5, 50, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-h-knuckle-hub/main_floor_h.scad:132 |
| MASTER BEDROOM | W | (34.5, 62.5, 'y') | 4.5 | 2.5 | 5 | 22.5 | option-h-knuckle-hub/main_floor_h.scad:133 |
| MASTER BEDROOM | N | (38, 70.4, 'x') | 4 | 2.5 | 5 | 20.0 | option-h-knuckle-hub/main_floor_h.scad:134 |
| MASTER BEDROOM | N | (57.5, 70.4, 'x') | 4 | 2.5 | 5 | 20.0 | option-h-knuckle-hub/main_floor_h.scad:135 |
| ENSUITE | W | (26, 40, 'y') | 3 | 4 | 3 | 9.0 | option-h-knuckle-hub/main_floor_h.scad:136 |
| ENSUITE | S | (28, 36.4, 'x') | 3 | 4 | 3 | 9.0 | option-h-knuckle-hub/main_floor_h.scad:137 |

Total main-floor window glass (width x height): 410.0 sq ft (19 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 4, S: 4, E: 5, W: 6

Rooms with windows on 2+ walls (main): LIVING (N/S/W); DINING / NOOK (E/S); BEDROOM 2 (E/N); MASTER BEDROOM (N/W); ENSUITE (S/W)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| POWDER | bath | 47 |
| FOYER | hall | 112 |
| (unlabelled hall) @55.4,14.4 | hall | 85 |
| (unlabelled hall) @55.4,22.4 | hall | 18 |
| (stair-top landing) | hall | 66 |
| (unlabelled hall) @60,22.4 | hall | 64 |
| MUDROOM | utility | 150 |
| (the bedroom hall) | hall | 108 |
| ELEVATOR (FUTURE) | closet | 42 |
| LINEN | closet | 21 |
| SHARED BATH | bath | 76 |
| WIC @44,36.4 | closet | 72 |
| WIC @38,36.4 | closet | 72 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BEDROOM 3 | S | (71, 0, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:160 |
| BEDROOM 4 | E | (88, 22, 'y') | 4 | 3.5 | 3 | 12.0 | foundation.scad:161 |
| FLEX / CRAFT | N | (66, 60.4, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:0 |
| LIVING ROOM | S | (34, 0, 'x') | 6 | 3.5 | 3 | 18.0 | foundation.scad:0 |
| UTILITY | W | (26, 38, 'y') | 3 | 4 | 2 | 6.0 | foundation.scad:0 |
| UTILITY | W | (26, 43, 'y') | 1.5 | 4 | 2 | 3.0 | foundation.scad:0 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: (landing at the stair foot) (hall, 167 sf); STAIR UP (stair, 86 sf); (unlabelled hall) @55.4,10.45 (hall, 127 sf); (unlabelled hall) @55.4,22.4 (hall, 18 sf); (unlabelled hall) @50,26.4 (hall, 66 sf); (unlabelled hall) @50,33 (hall, 10 sf); (unlabelled hall) @60,22.4 (hall, 64 sf); ELEVATOR (FUTURE) (closet, 42 sf); STORAGE @35,20.4 (utility, 240 sf); (unlabelled hall) @66,13 (hall, 76 sf); BATH (bath, 64 sf); STORAGE @66,26.4 (utility, 113 sf); (unlabelled hall) @59,33 (hall, 108 sf); (unlabelled hall) @38,40 (hall, 134 sf); STORAGE @38,36.4 (utility, 54 sf); WINDOW WELL @32.5,-3.5 (porch, 33 sf); WINDOW WELL @69,-3.5 (porch, 19 sf); WINDOW WELL @88,21 (porch, 18 sf); WINDOW WELL @65,60.4 (porch, 22 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (unlabelled hall) @55.4,14.4 | 55.4,14.4 to 66,22.4 | 85 | 7.6 ft clear width (91 in), length 10.2 | option-h-knuckle-hub/main_floor_h.scad:49 |
| (unlabelled hall) @55.4,22.4 | 55.4,22.4 to 60,26.4 | 18 | 3.6 ft clear width (43 in), length 4.2 | option-h-knuckle-hub/main_floor_h.scad:50 |
| (stair-top landing) | 50,26.4 to 60,33 | 66 | 6.2 ft clear width (74 in), length 9.6 | option-h-knuckle-hub/main_floor_h.scad:51 |
| (unlabelled hall) @60,22.4 | 60,22.4 to 66,33 | 64 | 5.6 ft clear width (67 in), length 10.2 | option-h-knuckle-hub/main_floor_h.scad:52 |
| (the bedroom hall) | 59,33 to 66,48.4 | 108 | 6.6 ft clear width (79 in), length 15.0 | option-h-knuckle-hub/main_floor_h.scad:59 |

**Circulation total (halls only): 341 sq ft = 9.9% of 3428 sq ft conditioned** (10.1% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 71 | 7.0 ft | 12.0% | option-h-knuckle-hub/main_floor_h.scad:42 |
| MUDROOM | 150 | 11.1 ft | 16.4% (halls+foyer+mudroom) | option-h-knuckle-hub/main_floor_h.scad:55 |
| STAIR DN opening (stairwell) | 65 | 5.0 ft | 18.3% (all four) | option-h-knuckle-hub/main_floor_h.scad:48 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (landing at the stair foot) | 50,0 to 66,10.45 | 167 | 9.7 ft clear width (116 in), length 15.6 | option-h-knuckle-hub/basement_h.scad:35 |
| (unlabelled hall) @55.4,10.45 | 55.4,10.45 to 66,22.4 | 127 | 10.2 ft clear width (122 in), length 11.5 | option-h-knuckle-hub/basement_h.scad:37 |
| (unlabelled hall) @55.4,22.4 | 55.4,22.4 to 60,26.4 | 18 | 3.6 ft clear width (43 in), length 4.2 | option-h-knuckle-hub/basement_h.scad:38 |
| (unlabelled hall) @50,26.4 | 50,26.4 to 60,33 | 66 | 6.2 ft clear width (74 in), length 9.6 | option-h-knuckle-hub/basement_h.scad:39 |
| (unlabelled hall) @50,33 | 50,33 to 53,36.4 | 10 | 2.6 ft clear width (31 in), length 3.0 | option-h-knuckle-hub/basement_h.scad:40 |
| (unlabelled hall) @60,22.4 | 60,22.4 to 66,33 | 64 | 5.6 ft clear width (67 in), length 10.2 | option-h-knuckle-hub/basement_h.scad:41 |
| (unlabelled hall) @66,13 | 66,13 to 80,18.4 | 76 | 4.6 ft clear width (56 in), length 13.2 | option-h-knuckle-hub/basement_h.scad:45 |
| (unlabelled hall) @59,33 | 59,33 to 66,48.4 | 108 | 5.9 ft clear width (71 in), length 14.6 | option-h-knuckle-hub/basement_h.scad:51 |
| (unlabelled hall) @38,40 | 38,40 to 59,46.4 | 134 | 5.6 ft clear width (68 in), length 20.6 | option-h-knuckle-hub/basement_h.scad:53 |

**Circulation total (halls only): 770 sq ft = 30.8% of 2502 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 86 | 5.0 ft | 34.2% | option-h-knuckle-hub/basement_h.scad:36 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): none

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| LIVING | living | FOYER | - |
| VESTIBULE | hall | FOYER; FRONT PORCH | - |
| POWDER | bath | FOYER | - |
| DINING / NOOK | dining | FOYER; KITCHEN; PATIO | - |
| KITCHEN | kitchen | (unlabelled hall) @55.4,14.4; DINING / NOOK; PANTRY | - |
| FOYER | hall | (unlabelled hall) @55.4,14.4; DINING / NOOK; LIVING; POWDER; VESTIBULE | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (stair-top landing) | - |
| (unlabelled hall) @55.4,14.4 | hall | (unlabelled hall) @55.4,22.4; (unlabelled hall) @60,22.4; FOYER; KITCHEN | - |
| (unlabelled hall) @55.4,22.4 | hall | (stair-top landing); (unlabelled hall) @55.4,14.4 | - |
| (stair-top landing) | hall | (unlabelled hall) @55.4,22.4; (unlabelled hall) @60,22.4; OFFICE / LIBRARY; STAIR DN | - |
| (unlabelled hall) @60,22.4 | hall | (stair-top landing); (the bedroom hall); (unlabelled hall) @55.4,14.4; MUDROOM | - |
| OFFICE / LIBRARY | office | (stair-top landing) | - |
| MUDROOM | utility | (unlabelled hall) @60,22.4; GARAGE; PANTRY | - |
| PANTRY | utility | GARAGE; KITCHEN; MUDROOM | - |
| GARAGE | garage | DRIVE (LEVEL TO GARAGE DOORS); MUDROOM; PANTRY | - |
| (the bedroom hall) | hall | (unlabelled hall) @60,22.4; BEDROOM 2; ELEVATOR (FUTURE); LAUNDRY; MASTER BEDROOM; SHARED BATH | - |
| ELEVATOR (FUTURE) | closet | (the bedroom hall) | - |
| LINEN | closet | SHARED BATH | - |
| SHARED BATH | bath | (the bedroom hall); LINEN | - |
| WIC @44,36.4 | closet | MASTER BEDROOM | - |
| WIC @38,36.4 | closet | MASTER BEDROOM | - |
| ENSUITE | bath | MASTER BEDROOM | - |
| LAUNDRY | utility | (the bedroom hall) | - |
| BEDROOM 2 | bed | (the bedroom hall) | - |
| MASTER BEDROOM | bed | (the bedroom hall); DECK; ENSUITE; WIC @38,36.4; WIC @44,36.4 | - |
| DRIVE (LEVEL TO GARAGE DOORS) | porch, ceiling 0 (open zone) | GARAGE | - |
| PATIO | porch, ceiling 0 (open zone) | DINING / NOOK | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | VESTIBULE | - |
| DECK | porch, ceiling 0 (open zone) | MASTER BEDROOM | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| LIVING ROOM | living | (landing at the stair foot) | - |
| (landing at the stair foot) | hall | (unlabelled hall) @55.4,10.45; LIVING ROOM | - |
| STAIR UP | stair | (unlabelled hall) @50,26.4 | - |
| (unlabelled hall) @55.4,10.45 | hall | (landing at the stair foot); (unlabelled hall) @55.4,22.4; (unlabelled hall) @60,22.4; (unlabelled hall) @66,13 | - |
| (unlabelled hall) @55.4,22.4 | hall | (unlabelled hall) @50,26.4; (unlabelled hall) @55.4,10.45 | - |
| (unlabelled hall) @50,26.4 | hall | (unlabelled hall) @50,33; (unlabelled hall) @55.4,22.4; (unlabelled hall) @60,22.4; STAIR UP; STORAGE @35,20.4 | - |
| (unlabelled hall) @50,33 | hall | (unlabelled hall) @50,26.4 | - |
| (unlabelled hall) @60,22.4 | hall | (unlabelled hall) @50,26.4; (unlabelled hall) @55.4,10.45; (unlabelled hall) @59,33 | - |
| ELEVATOR (FUTURE) | closet | (unlabelled hall) @59,33 | - |
| STORAGE @35,20.4 | utility | (unlabelled hall) @50,26.4 | - |
| (unlabelled hall) @66,13 | hall | (unlabelled hall) @55.4,10.45; BATH; BEDROOM 3; BEDROOM 4 | - |
| BEDROOM 3 | bed | (unlabelled hall) @66,13 | - |
| BEDROOM 4 | bed | (unlabelled hall) @66,13 | - |
| BATH | bath | (unlabelled hall) @66,13; STORAGE @66,26.4 | - |
| STORAGE @66,26.4 | utility | BATH | - |
| (unlabelled hall) @59,33 | hall | (unlabelled hall) @38,40; (unlabelled hall) @60,22.4; ELEVATOR (FUTURE); FLEX / CRAFT | - |
| FLEX / CRAFT | office | (unlabelled hall) @59,33 | - |
| (unlabelled hall) @38,40 | hall | (unlabelled hall) @59,33; STORAGE @38,36.4; UTILITY | - |
| STORAGE @38,36.4 | utility | (unlabelled hall) @38,40 | - |
| UTILITY | utility | (unlabelled hall) @38,40 | - |
| WINDOW WELL @32.5,-3.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @69,-3.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @88,21 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @65,60.4 | porch, ceiling 0 (open zone) | - | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 37.4 | VESTIBULE > FOYER > (unlabelled hall) @55.4,14.4 > KITCHEN |
| front door -> range (option-h-knuckle-hub/main_floor_h.scad:145) | 32.1 | VESTIBULE > FOYER > (unlabelled hall) @55.4,14.4 > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 30.9 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> range | 37.1 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> PANTRY centre | 17.7 | GARAGE > PANTRY |
| master bedroom centre -> WIC @44,36.4 centre | 17.2 | MASTER BEDROOM > WIC @44,36.4 |
| master bedroom centre -> WIC @38,36.4 centre | 19.6 | MASTER BEDROOM > WIC @38,36.4 |
| master bedroom centre -> LAUNDRY centre | 27.8 | MASTER BEDROOM > (the bedroom hall) > LAUNDRY |
| BEDROOM 2 centre -> SHARED BATH centre | 18.5 | BEDROOM 2 > (the bedroom hall) > SHARED BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 16.1 | BEDROOM 2 > (the bedroom hall) > LAUNDRY |
| foyer centre -> POWDER centre (powder room) | 19.1 | VESTIBULE > FOYER > POWDER |
| front door -> top of main stair (top nosing, (52.70, 26.4)) | 36.2 | VESTIBULE > FOYER > (unlabelled hall) @55.4,14.4 > (unlabelled hall) @55.4,22.4 > (stair-top landing) |
| master bedroom centre -> top of main stair (top nosing, (52.70, 26.4)) | 43.5 | MASTER BEDROOM > (the bedroom hall) > (unlabelled hall) @60,22.4 > (stair-top landing) |
| BEDROOM 2 centre -> top of main stair (top nosing, (52.70, 26.4)) | 34.6 | BEDROOM 2 > (the bedroom hall) > (unlabelled hall) @60,22.4 > (stair-top landing) |
| basement stair foot (52.70, 10.45) -> UTILITY centre | 67.8 | (landing at the stair foot) > (unlabelled hall) @55.4,10.45 > (unlabelled hall) @60,22.4 > (unlabelled hall) @59,33 > (unlabelled hall) @38,40 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @44,36.4 centre: no (via MASTER BEDROOM > WIC @44,36.4); WIC @38,36.4 centre: no (via MASTER BEDROOM > WIC @38,36.4)

## Section 8

### 8.1 LIVING (main; option-h-knuckle-hub/main_floor_h.scad:41) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| VESTIBULE | hall | 7.4 | - |
| FOYER | hall | 7.0 | full 60 in |
| STAIR DN | stairwell (ceil 0) | 6.0 | - |
| OFFICE / LIBRARY | office | 15.0 | - |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are LIVING. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| (landing at the stair foot) | hall | 10.4 | full 48 in |
| STAIR UP | stair | 9.9 | - |
| STORAGE @35,20.4 | utility | 15.0 | - |
| WINDOW WELL @32.5,-3.5 | porch (ceil 0) | 9.5 | - |

### 8.2 FOYER (option-h-knuckle-hub/main_floor_h.scad:42) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| LIVING | living | 7.4 | - |
| POWDER | bath | 7.4 | - |
| FOYER | hall | 9.6 | door 36 in |
| FRONT PORCH | porch (ceil 0) | 9.6 | door 42 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: PANTRY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | PANTRY | option-h-knuckle-hub/main_floor_h.scad:56 | N 12.0 (garage); S 3.0 (yard/soil); E 8.0 (yard/soil) |
| main | ELEVATOR (FUTURE) | option-h-knuckle-hub/main_floor_h.scad:60 | none |
| main | LINEN | option-h-knuckle-hub/main_floor_h.scad:61 | none |
| main | WIC @44,36.4 | option-h-knuckle-hub/main_floor_h.scad:63 | none |
| main | WIC @38,36.4 | option-h-knuckle-hub/main_floor_h.scad:64 | none |
| base | ELEVATOR (FUTURE) | option-h-knuckle-hub/basement_h.scad:42 | none |
| base | STORAGE @35,20.4 | option-h-knuckle-hub/basement_h.scad:43 | W 16.0 (yard/soil) |
| base | STORAGE @66,26.4 | option-h-knuckle-hub/basement_h.scad:49 | N 8.0 (yard/soil); E 11.5 (yard/soil) |
| base | STORAGE @38,36.4 | option-h-knuckle-hub/basement_h.scad:54 | none |

Pantry/garage: PANTRY shares 12.0 ft of wall with the garage; doors between PANTRY and GARAGE: 1. The garage's doors to the house are: option-h-knuckle-hub/main_floor_h.scad:100 (MUDROOM | GARAGE, 36 in); option-h-knuckle-hub/main_floor_h.scad:103 (PANTRY | GARAGE, 36 in).

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | range run, west wall (144); fridge, by the pantry door, end of a run (147); sink run, east wall (149); sink under the east window (150); dishwasher (151); island: 10 ft aisle to the dishwasher (152) | front door -> kitchen/dining room centre; front door -> range (option-h-knuckle-hub/main_floor_h.scad:145); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range |
| LAUNDRY | laundry sink (177) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> LAUNDRY centre |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| LIVING | 14.0 | loop north leg (:114) | N 7.0 (yard/soil); S 22.0 (yard/soil); W 20.4 (yard/soil) |
| VESTIBULE | 14.0 | loop north leg (:114) | S 9.6 (porch/patio (open)) |
| POWDER | 14.0 | loop north leg (:114) | S 0.4 (porch/patio (open)), 6.0 (yard/soil) |
| DINING / NOOK | 14.0 | loop north leg (:114) | S 19.0 (yard/soil); E 10.0 (porch/patio (open)), 4.0 (yard/soil) |
| FOYER | 21.4 | loop north leg (:114) | none |
| KITCHEN | 28.0 | loop north leg (:114) | S 3.0 (yard/soil); E 15.0 (yard/soil) |
| ENSUITE | 28.0 | west driveway (site.scad:111) | N 8.5 (yard/soil); S 9.0 (yard/soil); W 12.0 (yard/soil) |
| STAIR DN | 28.4 | loop north leg (:114) | none |
| (unlabelled hall) @55.4,14.4 | 28.4 | loop north leg (:114) | none |
| OFFICE / LIBRARY | 34.4 | loop west leg (:115) | W 16.0 (yard/soil) |
| (unlabelled hall) @55.4,22.4 | 36.4 | loop north leg (:114) | none |
| (unlabelled hall) @60,22.4 | 36.4 | loop north leg (:114) | none |
| MASTER BEDROOM | 37.1 | west driveway (site.scad:111) | N 28.0 (yard/soil); E 10.0 (yard/soil); W 12.0 (porch/patio (open)), 10.0 (yard/soil) |

Other rooms are > 40 ft from any drive. Garage doors (rows option-h-knuckle-hub/main_floor_h.scad:78, option-h-knuckle-hub/main_floor_h.scad:79) face E; garage rectangle to the nearest drive piece: 51.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (86.2, 18.4, 87.6, 22.4) | (86.9, 20.4) | E wall x=88 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:150 |
| toilet/tub/wash basin (POWDER) | POWDER | (59.8, 0.4, 61.4, 2) | (60.6, 1.2) | W wall x=59.6 | 0.20 | option-h-knuckle-hub/main_floor_h.scad:168 |
| vanity (POWDER) | POWDER | (64, 0.4, 65.8, 3) | (64.9, 1.7) | E wall x=66 | 0.20 | option-h-knuckle-hub/main_floor_h.scad:169 |
| toilet/tub/wash basin (SHARED BATH) | SHARED BATH | (56.6, 40.4, 58.2, 42) | (57.4, 41.2) | S wall y=40 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:171 |
| vanity (SHARED BATH) | SHARED BATH | (50.4, 44, 52, 48) | (51.2, 46.0) | N wall y=48.4 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:172 |
| shower (SHARED BATH) | SHARED BATH | (53.4, 44.6, 58.2, 48) | (55.8, 46.3) | N wall y=48.4 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:173 |
| washer/dryer (LAUNDRY) | LAUNDRY | (73.9, 41.4, 75.3, 47.8) | (74.6, 44.6) | E wall x=75.5 | 0.20 | option-h-knuckle-hub/main_floor_h.scad:175 |
| sink (LAUNDRY) | LAUNDRY | (68, 46.4, 70, 47.5) | (69.0, 47.0) | N wall y=48.4 | 0.90 | option-h-knuckle-hub/main_floor_h.scad:177 |
| shower (ENSUITE) | ENSUITE | (26.4, 36.8, 33.4, 40.6) | (29.9, 38.7) | S wall y=36.4 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:179 |
| toilet/tub/wash basin (ENSUITE) | ENSUITE | (26.4, 37, 31, 39.6) | (28.7, 38.3) | W wall x=26 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:180 |
| shower (ENSUITE) | ENSUITE | (31.6, 37, 33.2, 40.2) | (32.4, 38.6) | S wall y=36.4 | 0.60 | option-h-knuckle-hub/main_floor_h.scad:181 |
| vanity (ENSUITE) | ENSUITE | (26.4, 45.4, 32.4, 47) | (29.4, 46.2) | W wall x=26 | 0.40 | option-h-knuckle-hub/main_floor_h.scad:182 |
| toilet/tub/wash basin (ENSUITE) | ENSUITE | (36.2, 42, 37.8, 43.6) | (37.0, 42.8) | E wall x=38 | 0.20 | option-h-knuckle-hub/main_floor_h.scad:183 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| shower (BATH) | BATH | (68.4, 24, 73.6, 26) | (71.0, 25.0) | N wall y=26.4 | 0.40 | option-h-knuckle-hub/basement_h.scad:106 |
| toilet/tub/wash basin (BATH) | BATH | (66.4, 21.4, 68, 23) | (67.2, 22.2) | W wall x=66 | 0.40 | option-h-knuckle-hub/basement_h.scad:107 |
| vanity (BATH) | BATH | (66.4, 18.8, 70, 20.2) | (68.2, 19.5) | S wall y=18.4 | 0.40 | option-h-knuckle-hub/basement_h.scad:108 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER) | POWDER | x=59.6 (vertical wall) | (60.6, 1.2) |
| G2 | vanity (POWDER) | POWDER | x=66 (vertical wall) | (64.9, 1.7) |
| G3 | sink (KITCHEN) | KITCHEN | x=88 (vertical wall) | (86.9, 20.4) |
| G4 | toilet/tub/wash basin (ENSUITE); vanity (ENSUITE) | ENSUITE | x=26 (vertical wall) | (29.0, 42.2) |
| G5 | shower (ENSUITE); shower (ENSUITE) | ENSUITE | y=36.4 (horizontal wall) | (31.2, 38.7) |
| G6 | toilet/tub/wash basin (SHARED BATH) | SHARED BATH | y=40 (horizontal wall) | (57.4, 41.2) |
| G7 | toilet/tub/wash basin (ENSUITE) | ENSUITE | x=38 (vertical wall) | (37.0, 42.8) |
| G8 | washer/dryer (LAUNDRY) | LAUNDRY | x=75.5 (vertical wall) | (74.6, 44.6) |
| G9 | vanity (SHARED BATH); shower (SHARED BATH) | SHARED BATH | y=48.4 (horizontal wall) | (53.5, 46.1) |
| G10 | sink (LAUNDRY) | LAUNDRY | y=48.4 (horizontal wall) | (69.0, 47.0) |

**Main floor: 10 wet-wall groups** (5 back-to-back plumbing clusters of rooms: POWDER | KITCHEN | SHARED BATH | ENSUITE | LAUNDRY)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | vanity (BATH) | BATH | y=18.4 (horizontal wall) | (68.2, 19.5) |
| G2 | toilet/tub/wash basin (BATH) | BATH | x=66 (vertical wall) | (67.2, 22.2) |
| G3 | shower (BATH) | BATH | y=26.4 (horizontal wall) | (71.0, 25.0) |

**Basement: 3 wet-wall groups** (1 clusters: BATH)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 11/3; 6 ft: 10/3; 8 ft: 10/3; 12 ft: 9/3; inf: 9/3

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER) | (60.6,1.2) | B1 (BATH) | (68.2,19.5) | 7.6 | 18.3 | 25.9 |
| G2 | vanity (POWDER) | (64.9,1.7) | B1 (BATH) | (68.2,19.5) | 3.3 | 17.8 | 21.1 |
| G3 | sink (KITCHEN) | (86.9,20.4) | B1 (BATH) | (68.2,19.5) | 18.7 | 0.9 | 19.6 |
| G4 | toilet/tub/wash basin (ENSUITE); vanity (ENSUITE) | (29.0,42.2) | B2 (BATH) | (67.2,22.2) | 38.2 | 20.1 | 58.2 |
| G5 | shower (ENSUITE); shower (ENSUITE) | (31.2,38.7) | B2 (BATH) | (67.2,22.2) | 36.0 | 16.5 | 52.5 |
| G6 | toilet/tub/wash basin (SHARED BATH) | (57.4,41.2) | B2 (BATH) | (67.2,22.2) | 9.8 | 19.0 | 28.8 |
| G7 | toilet/tub/wash basin (ENSUITE) | (37.0,42.8) | B2 (BATH) | (67.2,22.2) | 30.2 | 20.6 | 50.8 |
| G8 | washer/dryer (LAUNDRY) | (74.6,44.6) | B3 (BATH) | (71.0,25.0) | 3.6 | 19.6 | 23.2 |
| G9 | vanity (SHARED BATH); shower (SHARED BATH) | (53.5,46.1) | B2 (BATH) | (67.2,22.2) | 13.7 | 23.9 | 37.7 |
| G10 | sink (LAUNDRY) | (69.0,47.0) | B3 (BATH) | (71.0,25.0) | 2.0 | 22.0 | 24.0 |

Main-floor groups with a basement group within 5 ft Manhattan: 0 of 10; within 10 ft: 0.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (60.6,1.2) | 95.2 | 76.1 |
| G2 | (64.9,1.7) | 99.0 | 79.9 |
| G3 | (86.9,20.4) | 102.3 | 83.2 |
| G4 | (29.0,42.2) | 22.6 | 10.2 |
| G5 | (31.2,38.7) | 28.3 | 9.2 |
| G6 | (57.4,41.2) | 52.0 | 37.5 |
| G7 | (37.0,42.8) | 30.0 | 18.7 |
| G8 | (74.6,44.6) | 65.8 | 58.1 |
| G9 | (53.5,46.1) | 43.2 | 38.6 |
| G10 | (69.0,47.0) | 57.9 | 54.9 |

**DRI (E = (22.16, 58)) = 596.6 ft over 10 groups; mean 59.7 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 466.7 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:102, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:101). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **sink (KITCHEN), 83.1 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: sink (KITCHEN), 73.0 ft.
- Furthest basement fixture: **vanity (BATH), 65.3 ft** from the water heater.
- Nearest main-floor fixture: vanity (ENSUITE), 4.0 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 83; toilet/tub/wash basin (POWDER) 76; vanity (POWDER) 80; toilet/tub/wash basin (SHARED BATH) 33; vanity (SHARED BATH) 26; shower (SHARED BATH) 30; washer/dryer (LAUNDRY) 48; sink (LAUNDRY) 44; shower (ENSUITE) 8; toilet/tub/wash basin (ENSUITE) 7; shower (ENSUITE) 10; vanity (ENSUITE) 4; toilet/tub/wash basin (ENSUITE) 11; shower (BATH) 63; toilet/tub/wash basin (BATH) 62; vanity (BATH) 65

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-h-knuckle-hub/main_floor_h.scad:48 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-h-knuckle-hub/basement_h.scad:36 |
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
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 23.3 ft (7.1 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 91.0 ft (27.7 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 91.0 ft (27.7 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 70.2 ft (21.4 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 26.9 ft (8.2 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 59.6 ft (18.2 m) |
| House incl. porches/deck to future shop | 59.6 ft (18.2 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

