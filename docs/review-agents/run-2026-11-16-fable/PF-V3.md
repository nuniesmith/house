# PF-V3 — Version 3, a verified diff against PF-V12 (and PF-V2 where noted)

Conventions: page refs `v3 p.N`. Inches as printed. "meas." = measured on the 150-dpi image, scale 15.28 px/ft (scale.py 0.6110 pt/in); verified on the garage: printed outer 336.0 in (28.0 ft) = about 27.2 ft meas. on p3 (bias about -3%), so lengths carry +/- 1 ft, routes +/- 2-3 ft. "inferred" = from furniture/plan, not printed. "same as V12" = the V3 sheet's dimension labels are token-for-token identical to the V12 sheet (script `$RUN/work/PF2/match.py`, Jaccard 1.00) and the V3 page prints the quoted number. No north arrow, so positions are sheet positions. V3 room numbers differ from V12 (V3 hall = 5, master = 4, stair = 20, elevator closet = 21).

## §0 Set identity
- File `Version 3.pdf`; sha256 `091412be26e82cc6fabc89df94b120e54c03cc450aa352c5ccb6801d59d9e5aa`; 43 pages (A3 landscape).
- Project №1720789, title "Version 3" (bottom centre of the sheets).
- Sheet inventory: p1 Base plan; p2 Partitions; p3 Rooms; p4 Furniture; p5 Plumbing; p6 Wall elevations (key); p7 Garage (1-2); p8 Garage (3-4); p9 Unnamed room (1-2); p10 Unnamed room (3-4); p11 Unnamed room (1-4); p12 Unnamed room (1-10); p13 Unnamed room (11-12); p14 Unnamed room (1-8); p15 Unnamed room (9-10); p16 Unnamed room (11); p17 Unnamed room (1-4); p18 Unnamed room (1-4); p19 Unnamed room (1-6); p20 Bedroom (1-6); p21 Laundry (1-4); p22 Office (1-4); p23 Bedroom (1-4); p24-p26 Unnamed room (1-4 each); p27 Bathroom (1-6); p28 Unnamed room (1-6); p29 Unnamed room (1-4); p30 Unnamed room (1-12); p31 Unnamed room (1-5); p32 Future Elevator/Closet (1-6); p33 Vestibule (1-4); p34 Unnamed room (1-4); p35 Powder Room (1-4); p36-p42 Unnamed room (1-4 each); p43 Open to Basement (1-6).
- Versus V12 (42 pages): +1 page. Sheets named in V12 but unnamed in V3: Living Room, Mudroom, Sunroom, Pantry, Hall. "Garage" is named in V3 (p7, p8) and on p3 (room 1 "Garage"), unlike V2. Versus V2 (44 pages): garage sheets p7-p8 are two named pages, V2 had p7-p8 unnamed plus 2 more pages for its extra rooms.
- Legend on p1: Existing wall, Material: drywall, Material: glass, Terrace, Support post.
- Not in this set (titles + p1-p6 viewed): basement plan, foundation plan, roof plan, building elevations, sections, electrical sheet, site plan, north arrow, scale bar, door/window schedule table, wall-type / insulation notes, overall envelope dimension string, second storey, driveway/road. One floor only.
- p1 vs p3 differences: Hall S=378.57 (p1) vs 379.43 (p3); Bedroom (12) 143.48 (p1) vs 143.38 (p3); front terrace 232.61 (p1) vs 230.03 (p3); stair p1 S=54.25 + green S=54.57 box vs p3 room 19 54.79 and stair 49.30; p1 S=13.24 vs p3 13.35; p1 S=67.49 vs p3 67.38. This sheet quotes p3.

## §1 Envelope
- Ceiling H=120.0 in everywhere (p1, p3, all elevations; V12 same). Window heights 59.1/60.0/72.0.
- S= areas are NET INTERIOR; gross footprint larger.
- (a) Derived from printed chains:
  - Garage inner **312.0 x 456.0 in** (p7 walls 1 and 2: 178.4+36.0+241.6 = 456.0; 49.4+42.0+220.6 = 312.0; p8 wall 3 21.9+220.0+35.6+118.1+60.4 = 456.0; p8 wall 4 312.0). Garage outer bottom wall 90.1+36.0+36.0+70.5+42.0+49.4+12.0 = **336.0 in (28.0 ft)** (p1 tile r2c2). Same as V12 (336.0 x 480.0 outer, 312.0 x 456.0 inner).
  - Hall south wall 744.3 in (p14 wall 1: 259.2 + 63.0 + 164.0 + 60.0 + remainder; V12 744.3). Hall wall 10 547.0 (V12 546.8 form).
  - Living 3: 357.3 x 230.3 in = 571.5 ft2 (p11) [p3 571.46]. Kitchen 2: 294.0 x 306.1 = 625.0 ft2 (p9) [p3 625.28]. Dining 6: 230.3 x 221.4 = 353.8 ft2 (p17) [p3 354.03]. Room 7: 234.5 x 137.0 = 223.1 ft2 (p18). Room 13: 105.6 x 160.7 = 117.9 ft2 (p24). Room 25: 60.0 x 72.0 = 30.0 ft2 (p36). Room 8: 160.7 wide with a notch (walls 160.7/114.5/67.0/79.0/93.7/193.5 in p19).
  - South terrace bounding chains 426.1 in (bottom) x 550.5 in (right) (p1 tile r2c3).
  - Master block top wall: solid 205.9 between 48.0 windows (p1 tile r1c3), as V12.
  - No printed overall string.
- (b) Measured on p3 (+/- 1 ft, about 3% low): lower block west wall (x=765) to dining east wall (x=1360) about 48 ft; vestibule west face to room 7 east wall (x=1660) about 79 ft; master top to the flat south wall of the lower block about 92 ft; garage west wall to master east wall about 99 ft. Bounding box of garage + heated part about 99 x 92 ft (V2: 104 x 108; V12: about 74-79 x 69-71 heated).
- Heated envelope outline (words): upper half as V12 (master block top-right, bedroom/office block top-left, hall/stair/laundry band, vestibule at left). The lower block is a plain rectangle about 48 x 50 ft (living + dining along the hall; mudroom/pantry/kitchen below) with a flat south wall flush with the garage's south wall. Kitchen 2 + dining 6 end at x=1225/1350; the dining room steps back ~12 ft from the kitchen's east face (p3: kitchen east wall x=1230, dining east wall x=1360), i.e. one inside corner on the east side of the lower block. No bay window (V12 had one). Garage: plain rectangle 336 x 480 outer on the lower left, 2 overhead doors on its left wall (220.0 + 118.1, H=88.6) (p8 wall 3), side door 42.0 H82.7 on its south wall (p7 wall 2), windows 2 x 36.0 (H60 ws36) on top and bottom walls (p7/p8). Garage is attached along its right wall to living 3 (upper part), mudroom 8 and pantry 13 (p3). Outside-corner count: not printed; not counted.
- Porches/terraces (p3): north terrace 390.52 (p1, p3, same as V12); front terrace 230.03 (p3; p1 232.61; V12 same); south terrace **1428.71** (p3; V12 954.77; V2 2797.78), wraps the kitchen/dining east side only: it lies east of kitchen 2 and below the hall/dining, bounded by the dining room and room 7 (p3). Total terraces (p3) = 390.52 + 230.03 + 1428.71 = **2049.26 ft2** (V12 1575.32). Support posts: red squares at the front terrace and the north-terrace edge; none drawn around the south terrace (p3 shows none). No roof/covering drawn.
- Totals (p3, 32 numbered rooms, rooms.py sum 5266.10, numbering by descending area verified): minus garage 988.03 = **net heated interior 4278.07 ft2** (includes stair rooms and Open to Basement 0.22; V12 3763.34). Garage 988.03 ft2.

## §2 Room table (Rooms sheet v3 p.3; verified against the image; rooms.py matched the sheet, no correction except that on the sheet 20 = stair "?" 49.30 and 21 = Future Elevator/Closet 44.24, which the script merges)
| № | Name as printed | S ft2 | Inside dims in (source) | Position (p3) | Use / change vs V12 |
|---|---|---|---|---|---|
| 1 | Garage | 988.03 | 312.0 x 456.0 (p7, p8) | bottom-left | printed; same as V12 |
| 2 | ? | 625.28 | 294.0 x 306.1 (p9) | bottom-centre | inferred: kitchen (island 120.0 x 60.0, cooktops on west wall run, fridge/ovens, sink under 144.4 window) + breakfast table (4 chairs) in the same room |
| 3 | ? | 571.46 | 357.3 x 230.3 (p11) | lower block top-left | inferred: living room (sectional, 3 armchairs, coffee table, built-in shelves p4); no windows |
| 4 | ? | 458.12 | as V12 | top-right | same as V12 room 2: master bedroom — verified p3 458.12 |
| 5 | ? | 379.43 | south wall 744.3 (p14) | centre band | hall (V12 4: 379.54; V2 379.32) |
| 6 | ? | 354.03 | 230.3 x 221.4 (p17) | lower block top-right | inferred: dining room (72.0 dia round table, 8 chairs, p4) |
| 7 | ? | 223.14 | 234.5 x 137.0 (p18) | right, below master wing | V12 Sunroom 147.04 — name no longer printed; wardrobe/dresser walls + window bench + armchairs/sofa on p4/p18: inferred dressing room / sitting room, not printed |
| 8 | ? | 179.22 | 160.7 wide, notched (p19) | left of kitchen, beside garage | inferred: mudroom (garage door, cabinets, coat units on p4); V12 Mudroom 156.08 |
| 9 | Bedroom | 162.97 | as V12 | top-left | verified p3 |
| 10 | Laundry | 144.56 | 117.3 x 177.5 | centre-right | verified p3 |
| 11 | Office | 144.02 | 144.0 x 144.0 | left-centre | verified p3 |
| 12 | Bedroom | 143.38 (p1 143.48) | 151.0 x 136.8 | top | verified p3 |
| 13 | ? | 117.87 | 105.6 x 160.7 (p24) | below mudroom, beside garage | inferred: pantry (counters, fridge, window); V12 Pantry 95.91 |
| 14 | ? | 113.88 | as V12 | right-top | same as V12 room 13 |
| 15 | ? | 72.01 | 96.0 x 107.9 (p26) | right-top | same as V12 room 17 (closet) |
| 16 | Bathroom | 68.57 | as V12 | top-centre-left | verified |
| 17 | ? | 67.38 (p1 67.49) | | right-centre | same as V12 room 19 |
| 18 | ? | 63.94 | | right-top-left | same as V12 room 20 |
| 19 | ? | 54.79 | | right-centre | same as V12 room 21 |
| 20 | ? (stair) | 49.30 | | centre | stair; same as V12 22 |
| 21 | Future Elevator/Closet | 44.24 | 72.0 x 90.5 + steps (p32, 6 walls) | centre | V12 45.21; same shape as V2 |
| 22 | Vestibule | 39.18 | 96.0 x 58.8 (p33) | left of hall | same as V12 (V2 39.29) |
| 23 | ? | 38.86 | 116.5 x 48.0 (p34) | right-centre | same as V12 room 25 |
| 24 | Powder Room | 34.44 | 60.1 x 82.3 (p35) | centre | same as V12 |
| 25 | ? | 30.03 | 60.0 x 72.0 (p36) | inside mudroom 8, lower-centre | inferred: toilet + sink room (WC and lavatory on p4/p5). New |
| 26 | ? | 23.90 | 47.8 x 72.0 (p37) | right-centre | toilet room, same as V12 27 |
| 27 | ? | 19.38 | 58.0 x 48.0 | right-centre | same as V12 28 |
| 28 | ? | 19.05 | 72.0 x 38.0 | top-centre | same as V12 29 |
| 29 | ? | 15.18 | | top-left | same as V12 30 |
| 30 | ? | 13.35 | | centre | same as V12 31 |
| 31 | ? | 6.89 | | right-centre | same as V12 32 |
| 32 | Open to Basement | 0.22 | 6 walls (p43) | centre | same as V12 33 |
- Elevation-page matching (inferred by wall products and the key plan p6): p7-p8 garage (named); p9-p10 kitchen 2; p11 living 3; p12-p13 master wing (identical to V12 p11-p12); p14-p16 hall; p17 dining 6; p18 room 7; p19 room 8; p20 bedroom 9; p21 laundry; p22 office; p23 bedroom 12; p24 room 13; p25 master wing room (identical to V12 p23); p26 closet 15; p27-p31 as V12 p27-p31; p32 elevator closet; p33 vestibule; p34 room 23; p35 powder room; p36 room 25; p37-p42 as V12 p36-p41; p43 Open to Basement.

## §3 Door-type openings (ws=0)
p1 door-type label counts by H: 98.4 x1, 88.6 x2, 84.0 x3, 82.7 x37 = 43 (V12: 43; V2: 46). Widths from the elevations.
Changed block:
| Opening | Connects | Width in | H in | Type | Source |
|---|---|---|---|---|---|
| Garage overhead doors (2) | garage / outside (left wall) | 220.0 and 118.1 | 88.6 | overhead | p8 wall 3 |
| Garage side door | garage / outside (south wall) | 42.0 | 82.7 | single | p7 wall 2 (49.4+42.0+220.6) |
| Garage -> mudroom 8 | garage / room 8 | 36.0 | 82.7 | single swing | p7 wall 1 (178.4+36.0+241.6), p19 wall 6 (129.0+36.0+28.4) |
| Mudroom 8 -> kitchen 2 | room 8 / room 2 | 42.0 | 82.7 | sliding (track symbol) | p19 wall (29.4+42.0+43.0...), p9 wall 2 (31.8+36.0+166.8+42.0+29.4) |
| Mudroom 8 -> pantry 13 | room 8 / room 13 | 42.0 | 82.7 | sliding | p19 (21.0+42.0+30.7), p24 wall (30.7+42.0+88.0...) |
| Mudroom 8 -> room 25 | room 8 / toilet room | 36.0 | 82.7 | swing | p19 (7.0+36.0...), p36 prints 36.0 + 36.0 (two 36.0 openings; which walls: not resolved) |
| Pantry 13 -> kitchen 2 | room 13 / room 2 | 36.0 | 82.7 | single | p24 (37.8+36.0+31.8), p9 wall 2 (31.8+36.0+166.8) |
| Hall -> living 3 | hall / room 3 | 60.0 | 82.7 | double | p14 wall 1, p11 wall 1 (197.8+60.0+99.5) |
| Hall -> dining 6 | hall / room 6 | 63.0 | 82.7 | double | p14 wall 1, p17 wall 4 (57.5+63.0+100.9) |
| Living 3 -> kitchen 2 | room 3 / room 2 | 48.0 | 82.7 | double | p11 wall 3 (100.9+48.0+208.4), p10 wall 3 (40.7+48.0+132.5+48.0+25.2) |
| Living 3 -> dining 6 | room 3 / room 6 | 48.0 | 82.7 | double | p11 wall 2 (6.0+48.0+176.3), p17 wall 3 (176.3+48.0+6.0) |
| Kitchen 2 -> dining 6 | room 2 / room 6 | 48.0 | 82.7 | double | p10 wall 3, p17 wall 2 (148.9+48.0+24.5) |
| Kitchen 2 -> terrace | room 2 / outside (east) | 72.1 | 82.7 | sliding glazed | p10 wall 4 (14.1+72.1+219.9) |
| Dining 6 -> terrace | room 6 / outside (east) | 94.5 | 82.7 | 3-panel sliding glazed | p17 wall 1 (68.2+94.5+67.6) |
| Hall -> room 7 | hall / room 7 | 47.2 | 82.7 | double | p18 wall 3 (47.2+187.3), p16 (0.7+47.2) |
- No hall -> kitchen door: the hall's south wall has only the 60.0 (living) and 63.0 (dining) doors (p14 wall 1). V12 had 48.0+48.0 (kitchen) and 60.0 (living); V2 had 48.0 (kitchen) and 48.0 (living).
- **Garage-to-house door: 36.0 in H82.7, into mudroom 8** (V12: 42.0 mudroom + 36.0 pantry). The pantry shares the garage wall but has NO door to the garage.
Unchanged wing (same as V12 §3; verified by identical strings): vestibule 94.5 front + 60.0 to hall (p33); hall -> laundry 48.0 (p21); laundry -> terrace 36.0 H98.4; office 48.0 (p22); bedroom 9 -> hall 36.0 H84 (p20; p14 wall 8: 36.0 + 36.0 H84.0); bedroom 12 36.0 (p23); master wing doors as V12 (p12, p13, p25, p31); bathroom 31.5 + 36.0 (p27); room 17/18/19 sub-room doors 31.5/36.0 (p28, p29, p30); toilet room 26 31.5 (p37: 8.1+31.5+8.2); room 27 36.0/36.0/48.0 open (p38); room 28 36.0; closet 30 48.0; closet 31 42.1; powder room 36.0 (p35: 22.4+36.0+2.0; V12 24.4); elevator closet opening 42.7 H82.7 (p32; V12 46.0); room 23 doors 36.0, 47.3 open, 36.0 (p34; V12 47.8); hall wall 11 p16: 0.7 + 47.2 = 48.0 H82.7 (V12 47.8, H84.0); room 7 closet-type openings none other.
Summary: widths in V3: 36.0 (most common), 42.0 (garage side, two sliders), 47.2/48.0 (doubles), 60.0, 63.0, 72.1, 94.5, 220.0/118.1 (overheads). **Narrowest door-type opening: 31.5 in** (unchanged wing only: bathroom, sub-room, toilet room 26; about 4 doors, as V12). **Doors under 36 in: 31.5 in x about 4.** Every door in the changed block is 36.0 in or wider. Exterior doors in the lower block: garage 2 overhead + 1 side, kitchen slider 72.1, dining slider 94.5; room 7 door 47.2 opens to the hall (interior). Upper block as V12.

## §4 Window-type openings (ws>0)
p1 labels: H72 ws6 x2, H72 ws24 x6, H60 ws24 x6, H60 ws36 x1, H59.1 ws33.5 x5, H59.1 ws42.0 x2 = 22 (V12 23).
Changed block:
- Garage: 2 x 36.0 on top wall + 2 x 36.0 on bottom wall, H=60.0 ws=36.0 (p7 wall 2 / p8 wall 4; p1 tile r2c2). 2 walls, opposite.
- Kitchen 2: one window 144.4 in wide, H=59.1 ws=42.0 on the south wall (p9 wall 1 "59.1/42.0", chain 71.0+144.4+78.6; p1 tile r2c2). Windows on 1 wall (also the 72.1 slider on the east wall).
- Pantry 13: one window 47.2 in, H=59.1 ws=42.0, south wall (p1 tile r2c2 "57.1 | 47.2 | 56.4").
- Living 3: no window (p11 shows none; walls: hall, kitchen, dining, garage). None.
- Dining 6: east wall two windows 47.2 wide each (H=59.1 ws=33.5) flanking the 94.5 slider (p17 wall 1, p1 tile r2c3); south wall one window about 92.8 in (H=59.1 ws=33.5; p17 wall 2 window, p1 "92.8"). Windows on 2 exterior walls.
- Mudroom 8, room 25: no window on elevations (p19, p36).
- Room 7: window bench with 3-panel window (H=60.0 ws=24.0, width not dimensioned) on wall 1 (p18); window H=59.1 ws=33.5 on wall 2 (p18); p1 shows south-wall windows H59.1 ws33.5 (2) and an east-wall window 77.1 in (H60 ws24). Windows on 2-3 walls.
- Hall: a 3-panel window H=59.1 ws=33.5 on its south wall west part (p14 wall 1; width not dimensioned). V12 hall none.
- Elevator closet: no window (V2 had one).
Unchanged wing (as V12 §4): bedroom 9 2 walls; bedroom 12 2 walls; office 2 walls; master 3 walls (p12/p13 identical); vestibule 2 walls; Open to Basement 2 windows H72 ws6 (p43).
No-window rooms: living 3, mudroom 8, pantry-adjacent room 25, laundry, bathroom 16, powder room, closets, rooms 14, 17-19, 23-31, stair, elevator closet. Windows directly across: garage top/bottom; dining east wall window pair has nothing opposite (west wall is the living room).

## §5 Halls and circulation
- Hall (room 5): 379.43 ft2 (p3), 378.57 (p1). Share of net heated interior 379.43 / 4278.07 = 8.9%.
- Narrowest printed hall width: west hall zone 96.0 in (p14 wall 2 "96.0"); corridor width east of it not printed as one chain, meas. about 48-55 in. p14 wall 3 142.0 coat wall, slat screen 49.3+7.0+49.3 (as V12).
- Vestibule (room 22): 39.18 ft2, 96.0 x 58.8; doors 94.5 front, 60.0 to hall. Vestibule + hall = 418.61 ft2 = 9.8%.
- Mudroom 8 (179.22) is the garage entry; its narrowest printed width 67.0 (p19 wall 3). Rooms 23, 27 circulation (inferred).

## §6 Plumbing fixtures (p5, p4, p36)
- Kitchen 2: sink under the 144.4 window on the SOUTH wall (p4: sink 40.0 in, p1 tile r2c2); cooktops (two burner groups, 2 x ... drawn) on the WEST wall run (shared with pantry/mudroom); fridge + ovens on the EAST wall run (p4/p1 tile r2c3 fridge snowflake and oven symbols along the east wall 219.9 in); dishwasher not labelled.
- Pantry 13: sink/tap and counters on south wall (p4).
- Room 25: WC + lavatory 23.6 in (p4/p5).
- Garage: utility sink 55.1 x 26.8 and a tool sink item (p4).
- Laundry: washer + dryer + sink as V12; bathroom 16, powder room 24, rooms 17, 19, 26, 28 as V12 (p5, p21, p27-p30, p35, p37, p39).
- Outdoor tap, dog wash, mop sink: not shown.
- Wet-wall map (meas. p3/p5, +/- 2 ft, centre to centre): kitchen sink (south wall, x about 1080,y 1250) <-> room 25 WC about 14 ft; kitchen cooktops are on the wall shared with room 25 / pantry / mudroom (p3); kitchen -> laundry about 55 ft; kitchen -> bathroom 16 about 50 ft; kitchen -> powder room 24 about 47 ft; powder room <-> bathroom 16 adjacent (about 8 ft); powder -> laundry about 20 ft; laundry <-> master wet rooms adjacent. In V12 the kitchen was against the hall band; here the whole lower block, including the kitchen plumbing, is 25-30 ft south of the hall band (p3).
- Basement plumbing / mechanical: nothing drawn; no utility room.

## §7 Kitchen, pantry, dining — what is walled off vs V12
- V12: kitchen + dining + room 15 one open room (p1 S=616.78), pantry/mudroom west, living at right via 48.0 pocket pair, three hall doors.
- V3: the same area is re-cut into: living 3 (571.46) and dining 6 (354.03) along the hall (top row), and kitchen 2 (625.28), mudroom 8 (179.22), pantry 13 (117.87), room 25 (30.03) below them (bottom row). Everything is a closed room with doors; the kitchen is NOT on the hall — it is reached through the living room, dining room, mudroom or pantry. Living has no exterior wall and no window.
- Kitchen island 120.0 x 60.0 (p4). Clearance dimensions printed in red near the island on p4: 36.8 in, 49.5 in and 56.6 in (text layer p4; the sheet does not label which gap each spans, so they are listed without assignment; the 56.6 value is split across text pieces in the layer). Cabinet depths 24.0, 36.0, 35.4 along the walls.
- Sink: south wall under a 144.4 window; range/cooktop: west wall run (against pantry/mudroom); fridge + ovens: east wall run (p4, p1).
- Pantry 13: 117.87 ft2; shares its west wall with the garage; no garage door; 36.0 door to the kitchen (p24), 42.0 slider to mudroom 8.
- Route garage door -> kitchen: garage -> mudroom 8 (36.0) -> 42.0 slider -> kitchen (1 room passed: mudroom); or mudroom -> pantry (42.0) -> kitchen (36.0) (2 rooms: mudroom, pantry).
- Kitchen <-> dining: 48.0 double door, direct. Kitchen <-> living: 48.0 double door, direct. Dining <-> living: 48.0 double door, direct (p11 wall 2).
- Kitchen as a through-route: yes — north doors (2 x 48.0) opposite the south wall (no door), west doors (pantry 36.0, mudroom 42.0) opposite the east slider (72.1) (p9, p10). Hall to kitchen: not direct (through living or dining).

## §8 Furniture sheet facts (p4)
- Master bed 76.0 x 84.0; bedroom 9 bed 63.0 x 84.0; bedroom 12 bed about 59.4 x 79.9 with 43.3 desk; office two 72.0 desks (as V12); kitchen island 120.0 x 60.0; breakfast table round 35.4 dia with 4 chairs in the kitchen; dining table round 72.0 dia with 8 chairs; living room: sectional modules 39.4/31.5/51.2, 66.9 run, 3 armchairs, 36.0 x 60.0 coffee table; outdoor: 96.0 x 42.0 table with 8 chairs, two sofas with a 23.6 x 1.5 table (p4); garage 3 cars 195.7 x 88.2; room 7 wardrobes (36.0/33.6/36.0 on the north wall), sofa 55.1, armchairs.
- Library: none; Sunroom: not named in V3.

## §9 Stair and elevator space
- Stair 53.8 wide (p1), run 132.1 (p31), stair room 20 = 49.30, Open to Basement 0.22 (p3); p43 walls 119.1 etc.
- Future Elevator/Closet **44.24** ft2 (p3; V12 45.21): 6 walls (72.0, 78.6, 12.0, 12.0, 60.0, 90.5), opening 42.7 H82.7 (p32; V12 46.0). Same drawing as V2 p33 except no window label on V3 p32.

## §10 Daily routes (p3, straight segments through doorways, 12.32 px/ft on the 2000-px view, +/- 2-3 ft; rooms passed THROUGH)
| Route | Length ft | Rooms passed through |
|---|---|---|
| garage door -> kitchen via mudroom slider | about 13 to the kitchen threshold; about 28 to the island | mudroom 8 |
| garage door -> kitchen via pantry | about 22 | mudroom 8, pantry 13 |
| garage door -> pantry (13) | about 13 | mudroom 8 |
| front door -> kitchen (shortest) | about 43 to the kitchen door (5.7 vestibule + 17.5 hall + 19 across living) | vestibule, hall, living 3 |
| front door -> kitchen via dining | about 70 | vestibule, hall, dining 6 |
| front door -> powder room | about 22-24 | vestibule, hall |
| front door -> primary bedroom door | about 85 (hall unchanged) | vestibule, hall, laundry, room 17, (room 14) |
| primary bedroom door -> laundry | about 20 | room 14, room 17 |
| primary bedroom -> kitchen | about 68 to the kitchen door | room 14, room 17, laundry, hall, living 3 |
| bedroom 12 -> nearest bath (16) | about 18 | hall |
| bedroom 9 -> nearest bath (16) | about 20 | hall |
| kitchen -> dining | about 20 (island to the 48.0 door) | none |
| dining -> living | about 24 (table centre to sectional centre via 48.0 door) | none |
| living -> sunroom (room 7 if taken as sunroom) | about 59 (living -> hall door 12, hall east 44, door 3) | hall |

## §11 Kayla-relevant adjacency facts (yes / no / not shown)
- Laundry adjacent to master suite via bath/closet: yes (laundry 36.0 door to room 17; p21, p1), as V12.
- Pantry <-> garage: shared wall yes (p3); door NO (garage opens to mudroom 8 only).
- Powder room near front entry: yes, about 22-24 ft through the hall (p3).
- Vestibule at front door: yes (room 22, 39.18 ft2).
- Bedroom sharing a wall with the living room: no. Bedroom adjacent to the foyer: bedrooms 9 and 12 open to the hall.
- Closets on exterior walls: closets 15 and 18 (master wing) as V12; room 7 wardrobes on its east wall.
- Tubs on exterior walls: no (p1).
- Master closet reachable without the master bath: no (via room 17 vanity zone), as V12 (inferred from p1).
- A bathroom reachable from every living zone without crossing the house: powder room 24 off the hall (about 22 ft from the vestibule; about 40-45 ft from the living/kitchen/dining area through the hall); room 25 (toilet) beside the mudroom/kitchen: about 14 ft from the kitchen sink.
- Sunroom/screened porch: no named sunroom; screened porch not shown; room 7 sits at the old sunroom position (inferred).
- Library: no. Office: yes (144.02). Bedrooms printed "Bedroom": 2 + master (room 4, inferred) = **3**.
- Guest room with ensuite: not drawn. Dog bath: not drawn (cat tree on p4 in the master zone). Covered outdoor cooking area: not shown.
- Sight line front door -> kitchen/living: vestibule opens to the hall; the living door (60.0) and dining door (63.0) are on the hall's south wall about 17-45 ft along the hall; no direct line from the front door into either room (p3).
- Toilet visible from a bathroom door when open: not determinable. Second laundry in master suite: no.
- Garage position: bottom-left of the plan, its right wall shared with the living room (upper part), mudroom 8 and pantry 13; garage doors on the left edge; bedrooms are at the top; no drive drawn — not shown. Living room has the garage on its west wall.

## §12 Unreadable / not done
- Kitchen aisle dimensions: the three red clearance numbers near the island (p4) are listed in §7 without a stated gap; which gap each measures not determined.
- Room 25's two 36.0 openings (p36 prints 36.0 + 36.0): which walls they are on not resolved.
- Per-wall window widths for room 7, hall, bedrooms and master not fully dimensioned; hall window width not printed.
- Elevation page <-> room mapping inferred (p12/p13 master wing; p25; p39-p42).
- Not every p1 dimension string at 300 dpi in the dense rooms around 17-19/23/27 (tile r1c3).
- Routes by eye on p3, +/- 2-3 ft.
- Outside-corner count of the envelope not made.
