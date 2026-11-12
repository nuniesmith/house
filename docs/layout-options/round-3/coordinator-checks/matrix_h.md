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
