import json
des=json.load(open('designer.json')); txt=json.load(open('ktext.json'))
D={k:v[0] for k,v in des['D'].items()}; E={k:v[0] for k,v in des['E'].items()}
oD={
'K-004':('MISSING','Basement BATH @92.8,41.2 (7.6x8.0 clear): largest clear circle 5.40 ft (1,646 mm) <5.58; its drawn "circle" is a 4.4x3.4 ft disc (basement_d.scad fixture [93.6,46,98,49.4]). Partial = MISSING (round-1 standard). 5 of 5 main-floor circles do measure clear.'),
'K-030':('MISSING','PANTRY 8.0x9.6 = 77 sf clear (84 sf CL), 1 shelf bank + 6.4 ft counter + freezer; smaller than round-1 option B pantry (90 sf) that was ruled MISSING; basement storage is 2 floors from the Costco door.'),
'K-041':('MISSING','Vestibule->foyer is door row [83.2,8.0,x,4.8,"open"]: a cased opening, no inner door, so no air lock (round-1 B and C drew inner doors).'),
'K-061':('MISSING','Hard target 6 = all swing doors 36 in. Three single doors are 2.8 ft (34 in): main WC [75.5,62.0], basement [77.8,44.0] and [101.0,49.6] (parse of main_floor_d.scad / basement_d.scad).'),
'K-100':('MISSING','Round-1 ruling on C (a bedroom with no east light = MISSING): basement BEDROOM 4 has west (x74) and north windows only.'),
'K-144':('MISSING','Line of sight (shapely, closed doors, cased openings open): from the foyer centre 339 of 420 sf of LIVING ROOM and 110 of 294 sf of DINING are visible through the 6 ft opening; kitchen 0 of 315. One of two messy areas in view = partial.'),
'K-210':('MISSING','Same ground as K-166: laundry opens off the ensuite and the suite hall, not the walk-ins (round-1 IN needed the laundry door off the WIC). Walk-ins are 6 ft of hall away on the other side of the suite hall.'),
'K-292':('MISSING','North "run" is fridge + tall cabinets only (x 33.2-38.7, y 18.4-21.4): a separate 5.5 ft tall-unit wall with no counter beside it, which is what K-292 asks to avoid.'),
}
oE={
'K-002':('IN','The note asks for a basement; it does not ask for a pool. E has a 2,940 sf basement with rec room 374 sf, theatre 273 sf, gym/music 254 sf. Round 1 scored IN with these rooms.'),
'K-004':('MISSING','POWDER 4.1x7.6 ft clear: largest circle 3.0 ft; the J&J bath circle (66.7-72.3, 26.2-31.8) is crossed by the swung leaves of three doors, 4.8 ft clear with leaves at 90 deg; WC room 3.7 ft with its leaf. Designer concedes the powder has no circle.'),
'K-008':('MISSING','Basement GYM / MUSIC (x 83.5-96.5, y 0-19.5) sits under main BEDROOM 2 (x 82-96.5, y 0-11.5), 13 x 11.5 ft overlap; basement bedrooms 3 and 4 face the theatre and gym across a 5.1 ft hall.'),
'K-012':('MISSING','Round-1 ruling on C: living spaces south but no south backyard = MISSING. E kitchen faces north (windows N and W only); the south side is the road side (drive, front porch); the private deck is east.'),
'K-099':('MISSING','Kitchen is on the north wall (windows x 28-40, y 39; west x=24): one of the three named active spaces gets no south or east light. Designer evidence says "the kitchen is north" yet scores IN.'),
'K-100':('MISSING','Round-1 ruling on C: BEDROOM 3 with a north window only = MISSING. E basement bedrooms 3 and 4 have north windows only (y 39).'),
'K-114':('MISSING','Pantry 74 sf has a 1 ft shelf bank (x 31.8-32.8) and a freezer, no counter; designer\'s own K-030 says "no room for small-appliance counters".'),
'K-144':('CONTRADICTED','Sight line from the foyer west edge (66,10) through the 6 ft foyer/living opening, the 15 ft living/dining opening and the 8 ft dining/kitchen opening reaches the island (31-40.8, 27-31.5) and west counter run. 223 of 342 sf of living and 245 of 266 sf of dining are visible from the foyer centre. Same call as round-1 C.'),
'K-166':('IN','Round-1 ruling: laundry door off the WIC = basket never leaves the suite. E laundry opens off WIC B (door [61.5,22,y]).'),
'K-210':('IN','Same ruling as K-166.'),
'K-255':('IN','Round 1 scored K-255 IN for a roofed front porch/deck of 10+ ft depth (C, B). E has a 420 sf roofed front porch, a 168 sf patio and a 184 sf deck.'),
'K-262':('CONTRADICTED','Same sight line as K-144: the kitchen island and range are in view from the foyer through the living and dining openings.'),
}
for k,(v,_) in oD.items(): D[k]=v
for k,(v,_) in oE.items(): E[k]=v
json.dump({'D':D,'E':E,'F':'pending'},open('rescore.json','w'),indent=1)
def cnt(x): 
    return tuple(sum(1 for v in x.values() if v==s) for s in('IN','MISSING','CONTRADICTED'))
print(cnt(D),cnt(E),len(D),len(E))
def db(x):
    g=lambda *ks: all(x[k]=='IN' for k in ks)
    return {'K-328':g('K-328'),'K-329':g('K-329'),'K-330':g('K-330'),'K-331/K-070':g('K-331','K-070'),'K-332':g('K-332'),'K-333/K-201/K-304':g('K-333','K-201','K-304'),'K-334':g('K-334'),'K-335/K-005':g('K-335','K-005'),'K-036+K-329':g('K-036','K-329'),'K-037+K-115':g('K-037','K-115'),'wide K-003/060/061':g('K-003','K-060','K-061'),'K-055':g('K-055')}
dD,dE=db(D),db(E); print(sum(dD.values()),sum(dE.values()))
json.dump({'oD':oD,'oE':oE,'cD':cnt(D),'cE':cnt(E),'dD':dD,'dE':dE},open('out.json','w'))
