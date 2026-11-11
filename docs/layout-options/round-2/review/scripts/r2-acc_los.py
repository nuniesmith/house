from parse import load
from circ import lab
from shapely.geometry import LineString, Point, box
from shapely.ops import unary_union
import sys
def walls(d):
    segs=[]
    for r in d['rooms']:
        if r[6] in('porch',): continue
        x0,y0,x1,y1=r[1:5]
        segs+= [((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))]
    lines=[LineString(s) for s in segs]
    W=unary_union(lines)
    gaps=[]
    for x in d['doors']:
        xx,yy,ax,w,t=x[:5]
        g=LineString([(xx,yy),(xx+w,yy)]) if ax=='x' else LineString([(xx,yy),(xx,yy+w)])
        gaps.append((g.buffer(0.01,cap_style=2),t,g))
    openg=unary_union([g.buffer(0.06,cap_style=2) for g,t,_ in gaps if t in('open','full')])
    W=W.difference(openg)
    return W
def vis(d,P,doorxy,w):
    W=walls(d)
    xx,yy,ax,wd=doorxy
    Q=(xx+wd/2,yy) if ax=='x' else (xx,yy+wd/2)
    # approach from P side: move Q 0.3 toward P
    import math
    dx,dy=P[0]-Q[0],P[1]-Q[1]; L=math.hypot(dx,dy)
    Q2=(Q[0]+dx/L*0.3,Q[1]+dy/L*0.3)
    return not LineString([P,Q2]).intersects(W)
def seesroom(d,P,room):
    W=walls(d); x0,y0,x1,y1=room[1:5]
    import numpy as np
    pts=[(x,y) for x in np.arange(x0+0.5,x1-0.4,1.0) for y in np.arange(y0+0.5,y1-0.4,1.0)]
    n=sum(1 for q in pts if not LineString([P,q]).intersects(W))
    return n,len(pts)
