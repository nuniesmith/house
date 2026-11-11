## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/main_floor_d.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/basement_d.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 2,779 | 2778.7; excl. stair opening 2725.8 |
| Building area, centre lines (house + attached garage) | 313.5 m2 | 3374 sq ft |
| Building area, outside face | 330.4 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 2,934 sq ft | centre lines 2,779 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 2,934 sq ft | centre lines 2,779 sq ft |
| Circulation % (strict / with foyer) | 6.9% / 8.7% | 193 sq ft strict of 2779 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 1 / 12 | type `door` rows, by opening width |
| Double / open counts (main) | 4 / 10 | type `double` / type `open` |
| Minimum hall clear width | 5.60 ft (HALL) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 4.20 ft ((stair top landing)) |
| Wet-wall groups (main / basement) | 7 / 4 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 3 of 7 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 587.2 ft | alternate exit (22.16, 38.9): 557.3 ft |
| Water heater -> furthest fixture (main / basement) | 94.7 ft (shower (SHOWER)) / 94.4 ft (toilet/tub/wash basin (BATH @92.8,41.2)) | water heater at (32.0, 20.0); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 23.5 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 3 of 5: LINEN [W(yard 2.7)]; BR 2 CLOSET [S(yard 3.8) E(yard 7.4)]; WIC @96.4,41.2 [S(yard 4.8) E(yard 8.4)] | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 10.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: E(yard 12.2) ;; MASTER BEDROOM: N(yard 22.0) E(porch/patio 14.0, yard 5.9) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 31.0) S(yard 4.8) E(porch/patio 14.0, yard 14.3) W(yard 19.9) | suite rooms: (suite hall), WIC @88.4,41.2, WIC @96.4,41.2, MASTER BATH, WC, SHOWER, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING ROOM (20.0 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 3: KITCHEN (N/S); LIVING ROOM (N/S); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 77.8..82.4, y 38.5; basement foot room x 77.8..82.4, y 27; **moved** (x offset +0.00/+0.00 ft, run 11.500 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 43.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_d.scad (defaults): 29 rooms, 31 doors, 16 windows - OK ; basement_d.scad (defaults): 28 rooms, 24 doors, 8 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |
