## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/main_floor_f.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/basement_f.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 2,915 | 2914.7; excl. stair opening 2865.5 |
| Building area, centre lines (house + attached garage) | 337.7 m2 | 3635 sq ft |
| Building area, outside face | 350.8 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 3,032 sq ft | centre lines 2,915 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 3,003 sq ft | centre lines 2,878 sq ft |
| Circulation % (strict / with foyer) | 7.7% / 10.6% | 225 sq ft strict of 2915 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 16 | type `door` rows, by opening width |
| Double / open counts (main) | 3 / 0 | type `double` / type `open` |
| Minimum hall clear width | 3.80 ft ((stair-top landing)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 2.00 ft ((elevator approach)) |
| Wet-wall groups (main / basement) | 6 / 3 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 0 of 6 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 514.8 ft | alternate exit (22.16, 38.9): 400.2 ft |
| Water heater -> furthest fixture (main / basement) | 89.9 ft (vanity (SHARED BATH / POWDER)) / 58.4 ft (vanity (JACK & JILL BATH)) | water heater at (25.7, 32.9); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 31.0 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 2 of 3: WIC @91.5,12.4 [S(yard 1.6) E(yard 6.2)]; ELEVATOR (FUTURE) [N(yard 6.0) W(yard 2.2)] | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 5.2 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(yard 12.4) E(yard 12.4) ;; MASTER BEDROOM: N(yard 22.4) E(porch/patio 16.0, yard 4.4) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 35.8) S(yard 10.0) E(porch/patio 16.0, yard 10.6) | suite rooms: SHARED BATH / POWDER, (bedroom hall), WIC @91.5,12.4, MASTER BATH, WIC @68.2,18.6, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (20.4 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 2: BEDROOM 2 (E/S); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 47.8..59.5, y 24.6; basement foot room x 43.55..59.5, y 20.4; **moved** (x offset +4.25/+0.00 ft, run 4.200 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 14.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_f.scad (defaults): 25 rooms, 29 doors, 15 windows - OK ; basement_f.scad (defaults): 22 rooms, 22 doors, 6 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |
