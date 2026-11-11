import json
des=json.load(open('designer.json')); cur=json.load(open('rescore.json')); o=json.load(open('out.json'))
F={k:v[0] for k,v in des['F'].items()}
oF={
'K-002':('IN','Basement 3,917 sf with rec room (LIVING ROOM 21x20), gym/music, flex, future theatre. The note asks for a basement, not a pool (same call as D and E).'),
'K-004':('MISSING','Powder 6.0x7.0 ft clear: largest circle 4.6 ft (3.6 ft with the door leaf); the drawn powder circle [98.7,6.6,104.3,12] overlaps the toilet and vanity. Designer says 7 of 7.'),
'K-008':('MISSING','Basement GYM / MUSIC (x 114.6-127, y 6-25.8) is under BEDROOM 2 (x 114.6-127, y 6-20.4), same footprint; THEATRE (future) is under the laundry, walk-ins and ensuite. Same ruling as E.'),
'K-012':('MISSING','Round-1 ruling on C: south living spaces but no south backyard. Patio is 12x10 ft on the road side; the private deck is a 3 ft strip on the east wall.'),
'K-033':('MISSING','Powder is 12 ft from the front door but about 75 ft by door path from the mudroom (kitchen, dining, living, foyer, passage) and from the office; designer scored IN on the front-door distance only.'),
'K-040':('IN','LINEN 35 sf (x 107.8-111.2, y 25.8-36.2) off the bedroom hall beside the shared bath and 12 ft from the bedroom 2 door. Carried MISSING came from E, which has no linen closet.'),
'K-041':('MISSING','No vestibule: the 3.5 ft front door opens straight into the 11.4x8 ft foyer, and the foyer is open to the living room (6.5 ft) and the stair passage (4.5 ft). Carried IN came from E.'),
'K-043':('MISSING','No console, shelf or mail counter is drawn in the foyer or the mudroom (fixtures: foyer coat cabinet only; mudroom lockers and bench only). Carried IN came from E.'),
'K-044':('MISSING','Same: no key/purse drop surface drawn near the entrance.'),
'K-061':('MISSING','Hard target 6, all swing doors 36 in: main floor 19 of 19 pass, but basement door (23.8, 24.8) is 2.8 ft (34 in). Same rule as D.'),
'K-069':('MISSING','L with 4 re-entrant corners and 412 ft of perimeter (designer\'s own cons); carried IN came from E, a 4-corner bar.'),
'K-070':('CONTRADICTED','matrix_f: 4 of 6 closets touch an exterior wall (junction CLOSET [N 5.4, W 7.4], ELEVATOR [N 6.4], BR2 closet [S 7.8], WIC @98.4,36.2 [W 8.4]). Designer scores K-331 MISSING but K-070 IN: inconsistent. Same call as D.'),
'K-071':('MISSING','Same four closets are not on interior walls (carried IN came from E).'),
'K-075':('IN','Public wing and quiet wing meet at the junction (foyer, stair, elevator); the living room is at the west, not between the wings. Same call as D.'),
'K-077':('MISSING','Windows directly across: kitchen south x 36-42 vs north x 35-43; living south x 68-80 vs north x 66-74 (overlap x 68-74).'),
'K-114':('MISSING','Pantry fixtures are a 0.6 ft shelf bank and a freezer; no small-appliance counter (main_floor_f.scad fixtures rows). Carried IN came from E.'),
'K-123':('IN','Island (x 38.6-41.6, y 6-15.4) lines up with the two 14 ft openings: from its west side 281/308 sf of dining and 448/480 sf of living are in view.'),
'K-128':('MISSING','72 in table (x 48.5-54.5, y 4-10) sits 0.5 ft from the kitchen/dining opening plane (x 47.8), not the 3 ft or more the brief asks; carried IN used E\'s 3.8 ft.'),
'K-140':('MISSING','No bench in the foyer (coat cabinet only); the only bench is in the mudroom. Same call as D.'),
'K-143':('MISSING','No drop surface in foyer or mudroom.'),
'K-144':('CONTRADICTED','Line of sight from just inside the front door: kitchen 200 of 330 sf, dining 220 of 308 sf, living 359 of 480 sf; from the foyer centre kitchen 245/330. Same call as round-1 C.'),
'K-151':('MISSING','No mudroom counter drawn (lockers x 23.2-24.4 and a bench only).'),
'K-153':('MISSING','No mail organiser or command area drawn.'),
'K-166':('IN','Round-1 ruling: laundry door (101.5, 36.2) opens straight into WIC @98.4 (door row `[101.5,36.2,x,3.0]`), so the basket stays in the suite.'),
'K-191':('MISSING','DECK is 3.0 x 16 ft (48 sf, `[127,48,130,64]`): a strip, not a porch to sit on. D 112 sf, E 184 sf.'),
'K-210':('IN','Same ruling as K-166.'),
'K-227':('MISSING','Toilet [124.8,38,126.4,39.6] stands in the open ensuite; no water-closet room is drawn.'),
'K-228':('MISSING','Ensuite has one door (to the bedroom, 120,44.6); no link to the laundry or the walk-ins.'),
'K-229':('MISSING','No door from the ensuite to either walk-in.'),
'K-245':('MISSING','BEDROOM 2 (y 6-20.4) is 24 ft from the primary bedroom (y 44.6+) with the laundry, walk-ins and ensuite between, about 28 ft by door path; D and E are 8 ft apart.'),
'K-253':('MISSING','Covered area is one 120 sf patio, a 56 sf front porch and a 48 sf deck; the patio cannot take both the dining table (K-252) and a lounge set.'),
'K-257':('IN','4 ft of counter (y 12-16) between range and fridge on the west run, touching the fridge: 48 in landing.'),
'K-262':('CONTRADICTED','Same sight line as K-144: range and fridge on the west run are visible from the front door.'),
'K-270':('IN','Fridge to sink 7.0 ft, sink to range 12.2 ft, range to fridge 6.8 ft (euclidean, fixture centres) = about 3, 5 and 3 steps at 2.5 ft.'),
'K-292':('IN','Fridge (x 32.6-34.8, y 16-18.6) ends the west counter run; it does not interrupt a run.'),
'K-306':('CONTRADICTED','Bed x 110-116.3, head on the north wall; north window x 114-120 sits behind the right 2.3 ft of the headboard.'),
'K-316':('MISSING','10.7 pct strict, 13.4 pct with foyer: past the midpoint between round-1 C (10.2 pct with foyer, IN) and B (14.8 pct, MISSING).'),
'K-317':('MISSING','Bedroom 2, shared bath, laundry, linen and the primary entry all hang off one 28 ft hall plus two short halls (round-1 B ruling: most rooms still open to a hall).'),
'K-320':('MISSING','Entry has shoes (lockers), coats and groceries, but no mail or drop surface.'),
'K-325':('MISSING','Basement BEDROOM 4 (x 53.2-65.6, y 0-14.4) shares a 14.4 ft wall with the basement LIVING ROOM (x 65.6-86.6).'),
'K-331':('CONTRADICTED','Same four closets as K-070; designer scored MISSING.'),
'K-332':('CONTRADICTED','Kitchen/dining and dining/living are two 14 ft openings (62 pct of the 22.4 ft wall) with no door, plus a 6.5 ft foyer opening; kitchen, dining and living are in view from the front door. Same call as E.'),
'K-334':('CONTRADICTED','Basement BEDROOM 4 shares a 14.4 ft wall at x 65.6 with the basement LIVING ROOM (the brief\'s rec-room label). The matrix row counts the main floor only.'),
}
for k,(v,_) in oF.items(): F[k]=v
cur['F']=F
json.dump(cur,open('rescore.json','w'),indent=1)
def cnt(x): return tuple(sum(1 for v in x.values() if v==s) for s in('IN','MISSING','CONTRADICTED'))
def db(x):
    g=lambda *ks: all(x[k]=='IN' for k in ks)
    return {'K-328':g('K-328'),'K-329':g('K-329'),'K-330':g('K-330'),'K-331/K-070':g('K-331','K-070'),'K-332':g('K-332'),'K-333/K-201/K-304':g('K-333','K-201','K-304'),'K-334':g('K-334'),'K-335/K-005':g('K-335','K-005'),'K-036+K-329':g('K-036','K-329'),'K-037+K-115':g('K-037','K-115'),'wide K-003/060/061':g('K-003','K-060','K-061'),'K-055':g('K-055')}
o['oF']=oF;o['cF']=cnt(F);o['dF']=db(F)
print(o['cF'],sum(o['dF'].values()),len(F))
json.dump(o,open('out.json','w'))
