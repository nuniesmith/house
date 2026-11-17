# PF-V2 — Version 2 ("Alt Layout"), a verified diff against PF-V12

Conventions: page refs `v2 p.N`. Inches as printed. "meas." = measured on the 150-dpi image with scale 13.06 px/ft (scale.py 0.5226 pt/in; verified: garage outer 384.0 in printed chain = 327 px on p3 = 31.1 ft meas., bias about -3%, so meas. lengths carry +/- 6 in per measurement, +/- 2 ft on routes). "inferred" = read from furniture/plan, not printed. "same as V12" = the dimension strings of that V2 sheet are token-for-token identical to the named V1-2 sheet (checked by script `$RUN/work/PF2/match.py`: Jaccard 1.00 of all `nn.n''` labels on the page) AND the V2 page prints the number quoted. Positions are on the sheet (no north arrow). V2 prints different room numbers from V1-2 (V1-2 -> V2: master 2->4, hall 4->5, living 3->3, kitchen 5 / dining 6 / 15 -> new rooms 2, 6, 7, 13, 15, 27). PF-V12 §n = baseline.

## §0 Set identity
- File `Version 2.pdf`; sha256 `f180261304cb271355102d677c62a6fb85729c191c5071f1e8c5f2e5698636b9`; 44 pages (A3 landscape).
- Project №1720863, title "Alt Layout" (bottom centre of every sheet, v2 p.1-p.6 seen; p.44 prints "Sheet 44" and the project number).
- Sheet inventory: p1 Base plan; p2 Partitions; p3 Rooms; p4 Furniture; p5 Plumbing; p6 Wall elevations (key plan); p7 Unnamed room (1-4); p8 Unnamed room (5-6); p9 Unnamed room (1-8); p10 Unnamed room (9-10); p11 Unnamed room (1-4); p12 Unnamed room (1-10); p13 Unnamed room (11-12); p14 Unnamed room (1-8); p15 Unnamed room (9-10); p16 Unnamed room (11); p17 Unnamed room (1-4); p18 Unnamed room (1-8); p19 Unnamed room (1-9); p20 Bedroom (1-6); p21 Laundry (1-4); p22 Office (1-4); p23 Bedroom (1-4); p24-p27 Unnamed room (1-4 each); p28 Bathroom (1-6); p29 Unnamed room (1-6); p30 Unnamed room (1-4); p31 Unnamed room (1-12); p32 Unnamed room (1-5); p33 Future Elevator/Closet (1-6); p34 Vestibule (1-4); p35 Unnamed room (1-4); p36 Powder Room (1-4); p37-p43 Unnamed room (1-4 each); p44 Open to Basement (1-6).
- Versus V1-2 (42 pages): +2 pages. Named sheets lost: Garage, Living Room, Mudroom, Sunroom, Pantry, Hall (now "Unnamed room" on p7-p19). Named sheets kept: Bedroom (p20, p23), Laundry, Office, Bathroom, Future Elevator/Closet, Vestibule, Powder Room, Open to Basement. Rooms sheet p3 prints names only for Bedroom x2, Laundry, Office, Bathroom, Future Elevator/Closet, Vestibule, Powder Room, Open to Basement; the garage is printed "?" (room 1).
- Legend on p1: Existing wall, Material: drywall, Material: glass, Terrace, Support post (same as V12).
- Not in this set (each sheet title checked, p1-p6 looked at): basement plan, foundation plan, roof plan, building elevations, sections, electrical sheet, site plan, north arrow, scale bar, door/window schedule table, wall-type / insulation notes, overall envelope dimension string, second storey, driveway/road. One floor only.
- Printed-area differences between p1 (Base plan) and p3 (Rooms), same set: Hall S=378.46 (p1) vs 379.32 (p3); Bedroom (room 12) 143.48 (p1) vs 143.38 (p3); front terrace 234.22 (p1) vs 230.78 (p3); south terrace 2799.93 (p1) vs 2797.78 (p3); Master/room 4 458.12 both; stair p1 S=54.25 and a green S=54.57 box (room 20) vs p3 room 20 = 54.79 and stair room 21 = 49.30; p1 S=13.24 (p3 room 31 = 13.35); p1 S=67.49 (p3 room 18 = 67.38). This sheet quotes p3 unless stated.

## §1 Envelope
- Ceiling H=120.0 in in every room label (p1, p3), garage included. H=60.0/72.0/82.0 etc. are window heights. (V12: same.)
- S= areas are NET INTERIOR; gross footprint is larger.
- (a) Derived from printed chains:
  - Garage inner: bottom wall 74.6+36.0+36.0+147.3+36.0+30.1 = **360.0 in** (p1 tile r2c2; p8 wall 5 "360.0''"); left wall 31.8+108.0+15.0+108.0+15.0+108.0+94.1 = **480.0 in** (p8 wall 6 "480.0''"). Garage outer: bottom 86.6+36.0+36.0+147.3+36.0+30.1+12.0 = **384.0 in (32.0 ft)**; left 106.2+108.0+15.0+108.0+15.0+108.0+43.8 = **504.0 in (42.0 ft)** (p1 tile r2c2). Inner 360 x 480 in = 1200 ft2 box; printed garage S=1111.92 (p3) plus room 15 S=78.04 = 1189.96 (the difference to 1200 is the wall that bounds room 15).
  - Master block top wall: solid segment 205.9 in between two 48.0 windows (p1 tile r1c3), as V12.
  - Hall south wall inner 743.9 in (p14 wall 1; V12 prints 744.3). Hall wall 1 on p14: 419.2 of window wall (5 window panels H=60.0 ws=24.0) then 48.0 door, 35.8 wall, 48.0 door.
  - Living room walls 265.1 x 254.6 in (p11) = 468.7 ft2 (p3 468.77); dining room 242.0 x 169.4 in (p17) = 284.7 ft2 (p3 284.71); room 2 as walls 270.1, 85.2, 150.5, 152.0, 144.1, 20.1, 5.0, 207.4 (p9) and 271.5, 253.9 (p10), 10 walls in all; room 13 106.1 x 180.3 in (p24) = 132.9 ft2; room 15 80.1 x 140.0/140.4 in (p26) = 77.9 ft2; room 27 42.2 x 72.5 in (p38); room 7 8 walls 71.3 / 79.5 / 49.2 / 102.8 / 34.0 / 157.0 / 86.5 / 339.2 (p18).
  - No printed overall string exists across the heated block or the whole plan.
- (b) Measured on p3 (150 dpi, scale 13.06 px/ft, outer wall edges, +/- 1 ft each): garage west outer wall to east-most master-wing wall about 104 ft (3 overhead-door bays face left); main heated block west wall (bedroom 9 / office, p3 x=805) to east wall of master wing (x=1580) about 73.6 ft; vestibule west face (x=750) to the east bay of room 8 (x=1602) about 80.9 ft; top of master block (y=130) to south wall of the kitchen/living/dining block (y=1070) about 89.3 ft; top of master block to garage south wall (y=1272) about 108.5 ft. So the heated plan plus garage is about 104 ft wide x 108 ft deep as a bounding box; heated part alone about 81 x 89 ft bounding box.
- Heated envelope outline (words, p3/p1): irregular multi-wing shape as V1-2 for the upper half (top-right master block, top-left bedroom/office block, centre hall/stair/laundry band, vestibule jutting left). Differences: the lower block is now a stepped rectangle: a larger west part (room 2 + room 13 + room 7, x 815-1030/1105 on p3) and an east part (living 3 and dining 6, x 1030-1255) — the dining room 6 projects further south than the living room, and the block ends with a flat south wall (no bay window as in V1-2). The upper-right room 8 has a bay on its east side (two 12.0 in jogs printed p1 r1c3 at 12.0/12.1). Garage: rectangle 384.0 x 504.0 in outer, attached along its right (east) wall to rooms 13 and 7; room 15 sits inside the garage's top-right corner. Outside-corner count of the heated envelope: not printed; about 32 counted on p3 by eye (inferred).
- Garage: one room, 3 overhead doors 108.0 in wide, H=88.6, 15.0 in piers between, all on the LEFT (outer) wall (p1, p8 wall 6); the garage has 3 cars drawn 195.7 x 88.2 in (p4); no 118.1/220.0 doors as in V1-2.
- Porches/terraces as printed (p3): north terrace 390.52 ft2 (p1,p3; same as V12); front (vestibule) terrace 230.78 ft2 (p3; p1 234.22; V12 230.03/232.61), steps drawn at left 266.3 in long (p1); south terrace **2797.78 ft2** (p3; p1 2799.93), edges 888.1 in x 811.6 in bounding (p1 tile r2c3), wraps the full south and east side of the living/dining block and fills the area between garage and dining; V12 south terrace was 954.77. Total terraces (p3) = 390.52 + 230.78 + 2797.78 = **3419.08 ft2** (V12 1575.32). Support posts drawn: red hatched squares along the south terrace edge (4 along the bottom, 1 more at x=1258 on p3) and around the front terrace. No roof/covering drawn; the sheet does not say any terrace is covered.
- Totals (p3, 33 numbered rooms): sum of all printed areas = 5316.47 ft2 (rooms.py; checked: numbering is by descending area, OK). Minus garage 1111.92 = **net heated interior 4204.55 ft2** (includes room 15 78.04 which sits inside the garage walls — heated status not printed; excluding room 15: 4126.51) (includes the stair rooms and "Open to Basement" 0.22 as printed). Garage 1111.92 ft2 (1189.96 with room 15). V12: 3763.34 net, garage 988.03.

## §2 Room table (Rooms sheet v2 p.3; names and areas read from the image and from `rooms.py v2 3`, which matched)
Script corrections: rows 21/22 print merged "Future Elevator/Closet ?": on the sheet room 21 = stair "?" 49.30, room 22 = Future Elevator/Closet 44.24. "Unnamed" = "?" printed.
| № | Name as printed | S ft2 | Inside dims in (source) | Position (p3) | Use / change vs V12 |
|---|---|---|---|---|---|
| 1 | ? | 1111.92 | 360.0 x 480.0 box less room 15 (p8) | bottom-left | inferred: garage (3 cars drawn p4; V12 room 1 Garage 988.03) |
| 2 | ? | 636.15 | 10 walls: 270.1/85.2/150.5/152.0/144.1/20.1/5.0/207.4 (p9), 271.5/253.9 (p10) | centre-left of lower block | inferred: kitchen + breakfast nook, one open L-shaped room: island 120.0 x 60.0, counters on W and N walls, round table 35.4 + banquette 78.7 (p4). New. |
| 3 | ? | 468.77 | 265.1 x 254.6 (p11) | lower right-upper | inferred: living room (sectional, TV wall, coffee table p4); V12 Living 457.58 |
| 4 | ? | 458.12 | as V12 | top-right | same as V12 room 2: master bedroom (king bed 76.0 x 84.0, p4) — verified v2 p3 prints S=458.12 |
| 5 | ? | 379.32 | hall: south wall 743.9 (p14) | centre band | Hall (V12 room 4 379.54; V1-2 Rooms sheet named it Hall, V2 p3 prints "?" only; inferred hall) |
| 6 | ? | 284.71 | 242.0 x 169.4 (p17) | lower right | inferred: dining room (table 96.0 x 42.0, 8 chairs, p4). New walled room |
| 7 | ? | 219.69 | 8 walls, south wall 339.2 (p18) | lower-left of block, beside garage | inferred: entry/mudroom (coat hooks, benches, boot storage, shoe/coat cabinets p18, p4). V12 Mudroom was 156.08 |
| 8 | ? | 186.11 | 9 walls; wall 8 174.6, wall 9 137.1 (p19) | right, below master wing | V12 "Sunroom" 147.04 — name no longer printed. Furniture sheet p4/p19 show wardrobe/dresser walls, armchair and a window bench: inferred dressing room / walk-in (not printed). |
| 9 | Bedroom | 162.97 | as V12 (144.1 x 136.8-144.0, p20) | top-left | verified p3 S=162.97 (V12 room 7) |
| 10 | Laundry | 144.56 | as V12 117.3 x 177.5 (p21) | centre-right | verified p3 144.56 |
| 11 | Office | 144.02 | 144.0 x 144.0 (p22) | left-centre | verified p3 144.02 |
| 12 | Bedroom | 143.38 (p1 143.48) | 151.0 x 136.8 (p23 vs V12 p22) | top, right of bedroom 9 | verified p3 143.38 |
| 13 | ? | 132.83 | 106.1 x 180.3 (p24) | lower-left of block, between kitchen and room 7 | inferred: pantry / scullery (counters, sink, cooktop-type items on p4/p5, shelving along east wall). New. |
| 14 | ? | 113.88 | as V12 (V12 room 13) | right-top | same as V12 room 13 — verified p3 113.88 |
| 15 | ? | 78.04 | 80.1 x 140.0 (p26) | inside garage, top-right corner | inferred: small garage-side room with toilet, hand-sink and a washer-type object drawn (p4/p5 grey); door 36.0 H84.0 into the garage. New. |
| 16 | ? | 72.01 | 96.0 x 108.0 (p27; V12 107.9) | right-top | same as V12 room 17, walk-in closet |
| 17 | Bathroom | 68.57 | as V12 | top-centre-left | verified p3 |
| 18 | ? | 67.38 (p1 67.49) | 125.0 vanity wall | right-centre | same as V12 room 19 |
| 19 | ? | 63.94 | 96.0 x 96.0 | right-top-left | same as V12 room 20 |
| 20 | ? | 54.79 | as V12 | right-centre | same as V12 room 21 (shower + tub; p1 also prints S=54.57 box) |
| 21 | ? (stair) | 49.30 | stair 53.8 wide p1 | centre | stair (V12 room 22); confirmed by the stair drawn p4/p5 |
| 22 | Future Elevator/Closet | 44.24 | 72.0 x 90.5/78.6 (p33, 6 walls) | centre | V12 45.21 (72.0 x 90.6, 4 walls); now 6 walls with a step (12.0 + 12.0) |
| 23 | Vestibule | 39.29 | 96.0 x 58.7/59.3 (p34) | left of hall | V12 39.18 (96.0 x 58.8) |
| 24 | ? | 38.86 | 116.5 x 48.0 (p35) | right-centre | same as V12 room 25 |
| 25 | Powder Room | 34.44 | 60.1 x 82.3 (p36) | centre | same as V12 room 26 |
| 26 | ? | 23.90 | 47.8 x 72.0 | right-centre | same as V12 room 27, toilet room |
| 27 | ? | 21.21 | 42.2 x 72.5 (p38) | bottom-left of block, beside room 7 | inferred: toilet + sink room (WC and 23.6 in lavatory on p5). New (V12 room 27 was 23.90 elsewhere). |
| 28 | ? | 19.38 | 58.0 x 48.0 | right-centre | same as V12 room 28 |
| 29 | ? | 19.05 | 72.0 x 38.0 | top-centre | same as V12 room 29 |
| 30 | ? | 15.18 | 84.0 x 26.0 | top-left | same as V12 room 30 (bedroom 9 closet) |
| 31 | ? | 13.35 | 82.3 x 23.1-23.4 (p42) | centre | same as V12 room 31; p42 now also prints a window H=60.0 ws=24.0 |
| 32 | ? | 6.89 | 47.8 x 20.8 | right-centre | same as V12 room 32 |
| 33 | Open to Basement | 0.22 | 6 walls (p44) | centre | same as V12 room 33 |
- Unnumbered: terraces (§1). Stair 49.30 and elevator closet 44.24 printed; p1 also shows a grey rectangle 118.3 in wide beside the stair.
- Elevation-page matching: pages are titled "Unnamed room" for most; matches below are INFERRED by multiplying printed wall lengths (and, for changed rooms, by the key plan p6 circle numbers): p7-p8 garage (walls 274.9/145.4/85.1/333.2/360.0/480.0); p9-p10 room 2; p11 living 3; p12-p13 master wing (identical to V12 p11-p12); p14-p16 hall (V12 p14-p16); p17 dining 6; p18 room 7; p19 room 8; p20 bedroom 9; p21 laundry; p22 office; p23 bedroom 12; p24 room 13; p25 identical to V12 p23 (master wing room); p26 room 15; p27 closet 16; p28-p32 as V12 p27-p31 (bathroom 17, 18, 19, 20, stair); p33 elevator closet; p34 vestibule; p35 room 24; p36 powder room; p37 identical to V12 p36 (toilet room 26); p38 room 27; p39-p43 identical/near V12 p38-p41; p44 Open to Basement.

## §3 Door-type openings (ws=0)
p1 door-type label count by H (openings.py): 98.4 x1, 88.6 x3, 84.0 x8, 82.7 x34 = 46 (V12: 43; 98.4 x3, 88.6 x2). Widths from elevation sheets.
Changed block (full treatment):
| Opening | Connects | Width in | H in | Type | Source |
|---|---|---|---|---|---|
| Garage overhead doors (3) | garage / outside (left wall) | 108.0 each | 88.6 | overhead | p8 wall 6, p1 |
| Garage side/exterior door | garage / outside (bottom wall) | 36.0 | 84.0 | single swing | p8 wall 5, p1 |
| Garage -> room 7 (entry) | garage / room 7 | 36.0 | 84.0 | single swing | p18 wall 1 (27.2 + 36.0 + 8.2), p7 |
| Garage -> room 15 | garage / room 15 | 36.0 | 84.0 | single swing | p26 wall 1 (4.4 + 36.0 + 100.1) |
| Room 7 -> room 27 | entry / toilet room | 36.0 | 82.7 | two leaves drawn, one 36.0 opening (pocket-type symbol on p4) | p18 wall 2 (23.3+36.0+20.1), p38 wall (13.1+36.0+23.3) |
| Room 7 -> room 13 | entry / pantry-scullery | 36.0 | 82.7 | single swing | p18 wall 4 (56.6+36.0+10.2), p24 wall 3 (8.2+36.0+136.1) |
| Room 7 -> room 2 | entry / kitchen nook | 42.0 | 82.7 | sliding/pocket (track symbol p4) | p18 wall 6 (32.8+42.0+82.2), p9 wall 4 (82.2+42.0+27.8) |
| Room 7 -> south terrace | entry / outside | 36.0 | 84.0 | single swing, exterior | p18 wall 8 (81.0+36.0+222.2) |
| Room 13 -> room 2 | pantry-scullery / kitchen | 36.0 | 82.7 | single swing | p24 wall 1 (26.6+36.0+117.7), p9 wall 8 (144.8+36.0+26.6) |
| Room 2 -> hall | kitchen / hall | 48.0 | 82.7 | double leaves | p10 wall 10 (192.9+48.0+13.0), p14 wall 1 (419.2 + 48.0 + 35.8 + 48.0) |
| Room 2 -> living 3 | kitchen / living | 48.0 | 84.0 | double leaves | p9 wall 1 (197.3+48.0+24.8), p11 wall 3 (19.8+48.0+197.3) |
| Room 2 -> dining 6 | kitchen nook / dining | 48.0 | 82.7 | double leaves | p9 wall 3 (89.6+48.0+12.9), p17 wall 1 (104.4+48.0+89.6) |
| Living 3 -> hall | living / hall | 48.0 | 82.7 | double leaves | p11 wall 4 (17.8+48.0+188.8), p14 wall 1 |
| Living 3 -> south/east terrace | living / outside | 72.0 | 82.7 | sliding glazed (two panels) | p11 wall 1 (185.5+72.0+7.6) |
| Dining 6 -> south terrace | dining / outside | 72.0 | 82.7 | sliding glazed | p17 wall 4 (48.7+72.0+48.7) |
- Hall: hall south wall has TWO 48.0 doors (p14 wall 1) = the hall->kitchen and hall->living doors above. V12 had two 48.0 + one 60.0 (p14).
- Room 7 is the only room that connects to the garage (one door, 36.0). **Garage-to-house door width: 36.0 in** (to room 7); room 15 is entered from the garage with a 36.0 door. There is NO door from the garage into room 13 (pantry-scullery) although they share a wall (p3, p24 walls). V12 had garage->mudroom 42.0 and garage->pantry 36.0.
- Dining 6 is NOT connected to the hall or living room by a door (only the 48.0 from room 2 + 72.0 terrace slider); its north wall carries 3 glazed units (H=82.0 ws=36.0, p17 wall 2 / p11 wall 2) — windows, not doors.
Unchanged wing (same as V12 §3; each verified by identical dimension strings on the V2 page): vestibule front 94.5 + 60.0 hall door (p34; V12 p33: 58.7/59.3 vs 58.8); hall->vestibule; hall->laundry 48.0 (p21 = V12 p20); laundry->north terrace 36.0 H98.4 (p21); laundry <-> room 18 36.0; office->hall 48.0 (p22); bedroom 9 ->hall 36.0 H84.0 (p20 wall 2 144.0+36.0...), closet bifold 63.0 (p20); bedroom 12->hall 36.0 (p23); master wing doors 48.0/36.0 as V12 (p12, p13, p25, p27, p29, p31 identical to V12); bathroom 17 doors 31.5 + 36.0 (p28 = V12 p27); room 19-20 sub-room doors 31.5/36.0 (p29, p30 identical); toilet room 26 31.5 (p37 = V12 p36); room 28 36.0/36.0/48.0 open (p39); room 29 36.0 slider; room 31 closet 48.0 double (p42 = V12 p40 plus window); room 32 closet 42.1 (p43); powder room 36.0 (p36: 22.4 + 36.0 + 2.0; V12 24.4); elevator closet opening 42.7 H82.7 (p33; V12 46.0); room 24 36.0, 47.6 open, 36.0 (p35; V12 36.0, 47.8, 36.0); hall wall 8 p14 two 36.0 H84.0 doors (bedrooms 9 and 12; 2 x 36.0 + 2.2 + 5.0 chain); hall wall 11 p16 prints 23.4+24.6+23.4 = 48.0, H82.7 (V12 p16: 47.8, H84.0); room 8 door 36.0 H82.7 (p19 wall 8: 34.9+36.0+103.6) leads off its west side to room 24 (inferred from p1 tile r1c3; the receiving room is not printed in text).
Summary: widths in V2: 36.0 (most common), 42.0 (room 7 slider), 48.0 (hall/living/kitchen/dining doubles; 5 in the lower block), 72.0 (two terrace sliders), 94.5 (vestibule), 108.0 (garage overhead x3). **Narrowest door-type opening: 31.5 in**, unchanged wing only (bathroom 17 doors p28, room 18/19/20 sub-room glass door p29/p30, toilet room 26 p37; 4 doors as V12). **Doors under 36 in: 31.5 in x about 4.** Doors under 32 in: the same 31.5 in. **Every door in the changed lower block is 36.0 in or wider.** Exterior doors in the lower block: garage side 36.0, garage overhead 3, room 7 south door 36.0, living slider 72.0, dining slider 72.0; upper block as V12 (vestibule 94.5, laundry 36.0 glazed, master west 48.0 to north terrace; room 8 east glazed units).

## §4 Window-type openings (ws>0)
p1 window label counts: H72 ws6 x0 (V12 x2? p1 label list shows ws=6 at the "Open to Basement" window; openings.py shows only H72 ws24 x6), H72 ws24 x6, H60 ws24 x14, H60 ws36 x2 = 22 (V12: 23). Also three H=82.0 ws=36.0 labels (living/dining interior glazing) which openings.py reads as ceiling-height labels, not windows.
Changed block:
- Garage: 2 x 36.0 on the top wall and 2 x 36.0 on the bottom wall, H=60.0 ws=36.0 (p7 wall 1, p8 wall 5, p1); windows on 2 walls (opposite each other, top/bottom).
- Room 2 (kitchen): west wall 3 windows, 36.0 each, H=60.0 ws=36.0 (p10 wall 9; p1 tile r2c2 chain 36.0 x3), sink 40.0 in drawn beneath (p5). Windows on 1 wall.
- Room 3 (living): east wall 3 windows H=60.0 ws=24.0 (p11 wall 1) beside the 72.0 slider; south wall 3 glazed units H=82.0 ws=36.0 (p11 wall 2) that look into the dining room (interior wall per p3/p17). Windows on 2 walls; none on its north (hall) or west (kitchen) wall.
- Room 6 (dining): east wall 3 windows H=60.0 ws=24.0 (p17 wall 3; p1 48.0 x3); south wall windows flank the 72.0 slider (H=60.0 ws=24.0, chain 48.7+72.0+48.7; p1 prints 24.0 on each side, p17 wall 4); north wall 3 interior glazed units H=82.0 ws=36.0 (p17 wall 2). 2 exterior walls with windows + 1 interior glazed wall.
- Room 7 (entry): 1 window 36.0 H=60.0 ws=24.0 on the south wall (p18 wall 8; p1 tile r2c2 36.0 at the west part of the south wall). Windows on 1 wall.
- Room 13, room 15, room 27: no window on their elevations (p24, p26, p38).
- Room 8: wall 4 window 101.9 in (two panels, H=60.0 ws=24.0) over a window bench; wall 7 a small window above the dresser run (H=60.0 ws=24.0, width not dimensioned, p19); east bay: two H=60.0 ws=24.0 units, 48.0 each (p1 tile r1c3). Windows on 2 or 3 walls.
- Hall: south wall 5 window panels H=60.0 ws=24.0 (p14 wall 1; p1 prints 4 x 48.0 + a 24.0 end piece). V12 hall had no windows.
- Elevator closet: one window H=60.0 ws=24.0 on wall 6 (p33; V12 none).
- Room 31 (13.35): one window H=60.0 ws=24.0 (p42; V12 none).
Unchanged wing (same as V12 §4): bedroom 9 windows on 2 walls (top 36.0 H72 ws24; west two H72 ws24, p20); bedroom 12 on 2 walls (top 36.0 H72 ws24; east 36.0 H60 ws36); office 2 walls (west 2 x 36.0; bottom 48.0 H72 ws24, p22); master bedroom 3 walls (top 2 x 48.0, east 2 x 48.0, west 48.0, H60 ws24; p12/p13 identical to V12); vestibule 2 x 48.0 H72 ws24 on 2 walls (p34 wall 1/3: 72.0 / 24.0); Open to Basement 2 windows H72 ws6 (p44 walls 1).
Rooms with NO window (from elevations): garage-side room 15, 13, 27, laundry, bathroom 17, powder room, closets 16/19/30/32, rooms 14, 18-20, 24-29, 33; stair. Directly across: garage top/bottom windows (opposite); living east windows face nothing opposite (west is the kitchen); master as V12.

## §5 Halls and circulation
- Hall (room 5): 379.32 ft2 (p3), 378.46 (p1). Share of net heated interior 379.32 / 4204.55 = 9.0% (excl. room 15: 9.2%). Narrowest printed hall width: west hall zone 96.0 in N-S next to the vestibule (p1 tile r1c2 "96.0"); the corridor width east of it is not printed as one chain (meas. about 48 in +/- 6, p3). Hall now has a window band on its south wall (§4).
- Hall's slat screen: p14 walls 4-6 (49.3 + 7.0 + 49.3 = 105.6) drawn as a slatted wooden partition, as V12 (no V12 diff).
- Vestibule (room 23): 39.29 ft2, 96.0 x 58.7/59.3 (p34); doors 94.5 front, 60.0 to hall.
- Room 7 (entry, 219.69 ft2) acts as the garage entry hall: narrowest printed dimension 34.0 (wall 5, p18) / 49.2 (wall 3); drawn clear width between the garage door and room 27 about 5 ft (meas. p3).
- Vestibule + hall = 418.61 ft2 = 10.0% of 4204.55. Rooms 24 (38.86), 28 (19.38) as V12 circulation (inferred).

## §6 Plumbing fixtures (p5 + p4; sheet plumbing p5 highlights fixtures in green)
- Kitchen (room 2): sink 40.0 in on the WEST wall under the three 36.0 windows (p5); range with 4 burners and fridge/ovens on the room's north wall run (p4: fridge snowflake, wall oven pair, cooktop 36.0, 124.7 in run on p1) ; dishwasher not labelled.
- Room 13 (pantry-scullery): green items near its NW corner (13.8 / 7 in dims) = a small sink/prep fixture; also sink/tap icons on its south counter (p4/p5 grey); cooktop-symbol items along its north wall (p4). Dishwasher not labelled.
- Room 27: WC (clearance 42.1 x 15.0 in) and lavatory 23.6 in (p5).
- Room 15: toilet + small sink + a machine drawn in grey (p4/p5); garage: a utility sink 55.1 x 26.8 in on the garage's top wall (p4) — plumbing-looking, not highlighted on p5.
- Room 7: sink/tap under the south window (p18 wall 8, tap drawn).
- Laundry: washer + dryer pair + sink as V12 (p21). Bathroom 17: shower/tub, vanity (p5; p28). Powder room 25: WC + vanity (p36). Room 18: two lavatories 31.5 in (p5). Room 20: shower 49.3 wide x 78.6 / 78.3 + tub 78.6 x 27.6 (p5). Room 26 WC (p37), room 29 WC (p40) as V12. Outdoor tap, dog wash, mop sink: not shown.
- Wet-wall map (meas. p3/p5, +/- 2 ft, centre to centre): kitchen sink (room 2 west wall) -> room 13 sink about 11 ft; room 13 / room 27 / room 15 sit along the garage's east wall in a column (rooms 15, 13, 27 at p3 y 860-980): room 27 toilet room shares its north wall with room 13 (p3) and its west wall with the garage wall; room 15 toilet is across the garage wall from room 13 (about 20 ft from room 27 on p3). Kitchen -> laundry about 40 ft (laundry at p3 x 1230,y 490; kitchen sink x 820,y 745); kitchen -> hall bath 17 about 40 ft; kitchen -> powder room 25 about 35 ft; hall bath 17 -> powder room 25 about 8 ft (adjacent block); powder room -> laundry about 20 ft; laundry <-> master wet group (rooms 18-20) adjacent (shared wall), 8-12 ft. In V12 the kitchen was against the hall band; the lower block is now about 15-20 ft further from every upper wet group than room 27 / 13 are from each other (they are at the garage side).
- Basement plumbing / mechanical room: nothing drawn. No furnace/water-heater room labelled.

## §7 Kitchen, pantry, dining — what is walled off vs V12
- V12: kitchen + dining + room 15 were ONE open room (S=616.78 p1), pantry/mudroom west of it, living room on the right with a 48.0 pocket-pair opening, three hall doors (48+48+60).
- V2: the single open room is split into FOUR enclosed spaces plus a larger kitchen:
  - Room 2 kitchen + breakfast nook (636.15): open L-shaped; doors N (48.0 hall), E (48.0 H84 living), SE (48.0 dining), S (42.0 slider to room 7), SW-ish (36.0 to room 13). Windows on west wall.
  - Room 13 (132.83) pantry/scullery: enclosed by walls on all sides, 2 doors (36.0 + 36.0): one to room 2 (NW), one to room 7 (SE) — a walk-through between kitchen and entry.
  - Room 6 dining (284.71): enclosed 242.0 x 169.4; one interior door (48.0 from room 2) and a 72.0 terrace slider; windows on E, S; glass to living on N.
  - Living 3 (468.77): enclosed 265.1 x 254.6; doors: hall 48.0, kitchen 48.0, terrace 72.0.
  - Room 7 entry (219.69) with room 27 toilet room off it.
- Island 120.0 x 60.0 (p4). Aisle widths printed between island and runs: not printed as chains on p1/p4 (labels 36.0, 24.0, 12.0 are cabinet depths; p4 prints 35.4 / 36.0 / 24.0 counters on the west wall). On p3 the island sits about 4-5 ft from the west counter and 7-8 ft from the north run (meas. +/- 1.5 ft).
- Sink: west wall under three 36.0 windows (p4/p5). Range/cooktop: north wall (the wall facing the hall, p4 "4 burners"). Fridge + wall ovens: on p9 wall 8 elevation (fridge, double oven, with 36.0 door) i.e. on the wall between room 2 and room 13. Coffee/cabinet wall: p9 wall 1 (197.3 solid with coffee bar, shared with the living room).
- Pantry: room 13, 132.83 ft2 (V12 pantry 95.91). It shares its WEST wall with the garage (p3); NO door connects pantry and garage. The garage's only house door goes into room 7 (36.0). Room 13 is reached by 36.0 doors from room 2 and from room 7 (p24).
- Route garage door -> kitchen: garage -> room 7 (36.0) -> room 13 (36.0) -> room 2 (36.0): passes through 2 rooms (7, 13); or room 7 -> 42.0 slider -> room 2: passes room 7.
- Kitchen <-> dining: through the 48.0 double door in room 2's nook (p9 wall 3 / p17 wall 1): direct, no intermediate room. Kitchen <-> living: 48.0 H84.0 double door (p9 wall 1).
- Kitchen is a through-route: yes — doors to hall (N), living (E), dining (SE), room 7 (S), room 13: openings on three sides including opposite sides (hall N / room 7 S, living E).
- Dining <-> living: no door; the shared wall has 3 glazed units (H82.0 ws36.0) — see-through but not passable (p11, p17).

## §8 Furniture sheet facts (p4)
- Master bed 76.0 x 84.0 (as V12). Bedroom 9 bed 63.0 x 84.0; bedroom 12 bed about 59.4 x 79.9 with desk 43.3 wide; office two 72.0 desks; kitchen island 120.0 x 60.0 (p4); nook round table 35.4 dia with banquette 78.7 (p4); dining table 96.0 x 42.0 with 8 chairs; living-room sectional (39.4 / 51.2 / 31.5 modules, 72.0 long run, depth 39.4), 2 armchairs, coffee table 60.0 x 36.0, linear fireplace/bench 72.0 on the west wall (p4, p11 wall 3 "fireplace-like unit"); cat tree and cat bed drawn in living room (p11); room 7: coat hooks, bench 72.0, shoe/coat units, ladder-type shelf, dog-like item "paw" icon drawn on the nook bench corner (p4 paw at the nook); room 8: wardrobes, dresser 137.1, armchair 55.1, window bench 101.9; outdoor: 72.0 dia round table with 8 chairs, two 3-seat sofas with 23.6 table, outdoor grill-like items 27.6 x 39.4 at the south of room 7 (p4); garage: 3 cars 195.7 x 88.2, workbench 83.1 x 42.9 and shelf runs 59.1 x 17.7 (p4); north terrace hammock 157.5 long.
- Library: none. Sunroom: no room is named Sunroom in V2 (room 8 inferred as above).

## §9 Stair and elevator space
- Stair: 53.8 in wide (p1), run 132.1 in (p32 chain as V12 p31); stair room 21 = 49.30 ft2 (p3), "Open to Basement" room 33 0.22 ft2 (p3), 119.1 + 40.4/60.8/41.5/58.3/81.8 walls (p44).
- Future Elevator/Closet: **44.24 ft2** (p3; V12 45.21). 6 walls on p33: 72.0, 78.6, 12.0, 12.0, 60.0, 90.5; one opening 42.7 in H82.7 (grey, no leaf; V12 46.0); a window H60.0 ws24.0 on wall 6. Sits immediately left of the stair, below the bath block, entered from the hall band (p1/p3).

## §10 Daily routes (p3, straight segments through doorways, scale 13.06 px/ft, +/- 2-3 ft; rooms passed THROUGH)
| Route | Length ft | Rooms passed through |
|---|---|---|
| garage door (into room 7) -> kitchen via room 13 | about 26 (to the kitchen NW door) | room 7, room 13 |
| garage door -> kitchen via 42.0 slider | about 18 (to the nook edge) / about 38 to the island centre | room 7, (nook part of room 2) |
| garage door -> pantry (room 13) | about 13 (to its SE door) | room 7 |
| front door (vestibule front) -> kitchen (hall door to room 2) | about 25 to the door, about 33 to the island | vestibule, hall |
| front door -> powder room | about 22-24 | vestibule, hall |
| front door -> primary bedroom door | about 85 (as V12: hall unchanged) | vestibule, hall, laundry, room 18, (room 14) |
| primary bedroom door -> laundry | about 20 | room 14, room 18 |
| primary bedroom -> kitchen | about 60 to the kitchen door (12 + 15 + 22 + 8, hall unchanged; V12 105) | room 14, room 18, laundry, hall |
| bedroom 12 -> nearest bath (17) | about 18 | hall |
| bedroom 9 -> nearest bath (17) | about 20 | hall |
| kitchen -> dining | about 25 (island centre to dining door; 0 rooms between) | none (same room: nook) |
| dining -> living | about 35 (dining door -> room 2 -> living door) | room 2 |
| living -> sunroom (room 8 if taken as the sunroom) | about 60 (living -> hall door 14, hall east 37, to room 8 side door 8) | hall (possibly room 24, not determinable) |
- Note: the V12 table value "primary -> kitchen about 105 ft" was not re-derived; the V2 value above is measured with V2's geometry only.

## §11 Kayla-relevant adjacency facts (yes / no / not shown)
- Laundry adjacent to master suite, connected via bath/closet: yes — laundry 36.0 door to room 18 (p21, p1), as V12.
- Pantry <-> garage shared wall / door: shared wall yes (p3); door NO (p24; garage's house door goes to room 7).
- Powder room near front entry: yes, about 22-24 ft through hall (p3).
- Vestibule at front door: yes (room 23, 39.29 ft2).
- Bedroom sharing a wall with the living room: no. Bedroom adjacent to the foyer: bedrooms 9, 12 open to the hall (no named foyer; vestibule + hall).
- Closets on exterior walls: closets 19 and 16 on master wing exterior walls as V12; room 8 (wardrobes) on the east exterior wall (p4/p19).
- Tubs on exterior walls: no (tub in room 20 interior, p1).
- Master closet reachable without passing the master bath: not by my reading of p1: closets 19/16 open off room 18 (vanity zone), as V12 (inferred).
- A bathroom reachable from every living zone without crossing the house: powder room 25 from hall (22-24 ft from vestibule); from living via hall (about 55 ft from the living door? p3 meas. living door -> powder room about 40 ft); from the kitchen about 35 ft; from dining about 50 ft; room 27 (WC + sink) opens off the entry (room 7), about 8 ft from the garage door — a second toilet near the garage side; room 15 has a toilet inside the garage.
- Sunroom/screened porch: no room named sunroom; screened porch not shown; room 8 is the former sunroom position (inferred).
- Library: no. Office: yes (144.02 ft2). Bedrooms printed "Bedroom": 2 (rooms 9, 12) + master (room 4, inferred) = **3**.
- Guest room with ensuite: not drawn. Dog bath / pet area: not drawn (cat tree p11; a paw icon on p4 at the nook). Covered outdoor cooking area: not shown (grill-type items drawn on the open south terrace).
- Sight line from the front door straight into kitchen/living: vestibule opens to the hall corridor running east-west; kitchen and living doors are 48.0 doubles on the hall's south wall about 18-30 ft along the hall (p3); no direct line.
- Toilet visible from a bathroom door when open: not determinable. Second laundry in the master suite: no.
- Garage position: bottom-left of plan, attached by its east wall to rooms 13/7/15; garage doors face the LEFT edge of the sheet; the garage runs along the whole lower-left side; bedrooms are at top-left/top-right, far side; no drive drawn — not shown.

## §12 Unreadable / not done
- Per-wall window widths for H60/H72 units not dimensioned on elevations (dining south windows, room 8 wall 7, bedroom/master) not all read.
- Elevation-page to room mapping for p9/p10, p12/p13, p25, p39-p43 inferred; p12-p13 not tied to specific master-wing rooms.
- The receiving room of room 8's 36.0 door and whether room 8 has a separate hall door could not be resolved in the dense p1 tile r1c3 area (labels overlap).
- Which room the second 36.0 door on p15 wall 9 (98.8+36.0+13.5+36.0+57.5, H84.0/H82.7) belongs to was not resolved (hall/bath wall; same as V12 p15).
- Room 13 / room 15 fixture identification is from the furniture/plumbing symbols (inferred), no labels.
- Routes: straight segments by eye on p3, +/- 2-3 ft; the V12 "primary -> kitchen 105 ft" was not re-checked.
- Not every dimension string on p1 was cross-checked at 300 dpi in the dense areas around rooms 18-20/24/28 (tile r1c3).
