import re,math,sys
sys.path.insert(0,'.')
exec(open('circ.py').read().split("T=0.4")[0])
from shapely.geometry import LineString, Point, box, MultiLineString
from shapely.ops import unary_union
OPEN_INNER={(51,7.4)}
def walls(openclosed=True,open_doors=((51,7.4),)):
    segs=[]
    for r in rooms:
        if r[6] in('porch',): continue
        x0,y0,x1,y1=r[1:5]
        for s in [((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))]:
            segs.append(LineString(s))
    U=unary_union(segs)
    gaps=[]
    for d in doors:
        x,y,ax,w,t=d[:5]
        if t=='garage': continue
        if t=='full' or (x,y) in open_doors:
            if ax=='x': gaps.append(box(x+0.02,y-0.15,x+w-0.02,y+0.15))
            else: gaps.append(box(x-0.15,y+0.02,x+0.15,y+w-0.02))
    return U.difference(unary_union(gaps))
W=walls()
def vis(px,py,room):
    x0,y0,x1,y1=room[1:5]
    n=0;v=0
    gx=x0+0.5
    while gx<x1:
        gy=y0+0.5
        while gy<y1:
            n+=1
            if not LineString([(px,py),(gx,gy)]).intersects(W): v+=1
            gy+=1
        gx+=1
    return v,n
def name(r): return r[0] if isinstance(r[0],str) else ' '.join(r[0])
for pt in [(56.25,1.0),(52.5,6.9),(52.5,8.2),(58,10.9)]:
    print(pt)
    for r in rooms:
        if name(r) in('LIVING','DINING / NOOK','KITCHEN','OFFICE / LIBRARY','POWDER','MASTER BEDROOM','BEDROOM 2'):
            v,n=vis(pt[0],pt[1],r); print('  ',name(r),v,'of',n)
print('--- kitchen features')
feats={'island':(73.7,21.6),'cooktop':(67.2,24.9),'sink':(86.8,20.4),'fridge':(75.4,27.7),'DW':(86.8,24.7),'dining table':(71,6),'living sofa':(36,10),'powder door':(62,7.4),'WC powder':(60.6,1.2)}
for pt in [(56.25,1.0),(52.5,8.2),(58,10.9),(54.5,10.9)]:
    print(pt,{k:(not LineString([pt,v]).intersects(W)) for k,v in feats.items()})
# hall sight line end from hub: view from (62,24) north
for pt in [(62,10),(62,24)]:
    print(pt,'primary door',not LineString([pt,(60.5,48.0)]).intersects(W),'bed2 door',not LineString([pt,(64.5,48.0)]).intersects(W),'laundry door',not LineString([pt,(66,44.5)]).intersects(W))
print('--- island')
for pt in [(73.7,16.8),(71.2,21.6),(76.5,21.6)]:
    print(pt)
    for r in rooms:
        if name(r) in('LIVING','DINING / NOOK','OFFICE / LIBRARY','FOYER'):
            print('  ',name(r),vis(pt[0],pt[1],r))
