## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/main_floor_e.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/basement_e.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 2,828 | 2827.5; excl. stair opening 2774.6 |
| Building area, centre lines (house + attached garage) | 322.9 m2 | 3476 sq ft |
| Building area, outside face | 335.6 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 2,940 sq ft | centre lines 2,828 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 2,940 sq ft | centre lines 2,828 sq ft |
| Circulation % (strict / with foyer) | 10.1% / 11.9% | 284 sq ft strict of 2828 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 19 | type `door` rows, by opening width |
| Double / open counts (main) | 2 / 0 | type `double` / type `open` |
| Minimum hall clear width | 5.10 ft ((private hall)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 4.20 ft ((stair-top landing)) |
| Wet-wall groups (main / basement) | 8 / 3 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 1 of 8 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 667.1 ft | alternate exit (22.16, 38.9): 514.3 ft |
| Water heater -> furthest fixture (main / basement) | 83.9 ft (shower (BATH)) / 51.3 ft (shower (JACK & JILL BATH)) | water heater at (25.7, 29.6); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 30.0 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 3:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 9.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(yard 14.5) E(yard 11.5) ;; MASTER BEDROOM: N(yard 20.0) E(porch/patio 16.0, yard 3.5) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 38.0) E(porch/patio 16.0, yard 3.5) | suite rooms: WIC @61.5,19.5, WIC @69,19.5, WC, MASTER BATH, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (18.5 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 3: BEDROOM 2 (E/S); KITCHEN (N/W); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42..53.5, y 39; basement foot room x 37.5..53.5, y 34.4; **moved** (x offset +4.50/+0.00 ft, run 4.600 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 14.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_e.scad (defaults): 28 rooms, 33 doors, 16 windows - OK ; basement_e.scad (defaults): 22 rooms, 18 doors, 7 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |
