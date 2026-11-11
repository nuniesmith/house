import sys, numpy as np
from shapely.geometry import box, Point
from shapely.ops import unary_union
from parse import load
def lab(r): 
    l=r[0]; return ' '.join(l) if isinstance(l,list) else l
def swing_geoms(doors, room, mode):
    from shapely.geometry import LineString, Polygon
    import math
    out=[]
    for d in doors:
        x,y,ax,w,t=d[:5]; s=d[5] if len(d)>5 and isinstance(d[5],(int,float)) else 1
        if t not in('door','double'): continue
        leaves=[(0,w)] if t=='door' else [(0,w/2),(1,w/2)]
        for end,lw in leaves:
            u=(1,0) if ax=='x' else (0,1); n=(0,s) if ax=='x' else (s,0)
            hx,hy=(x,y) if end==0 else (x+w*u[0],y+w*u[1])
            du=u if end==0 else (-u[0],-u[1])
            if mode=='leaf':
                g=LineString([(hx,hy),(hx+n[0]*lw,hy+n[1]*lw)]).buffer(0.08)
            else:
                pts=[(hx,hy)]+[(hx+lw*(math.cos(a)*du[0]+math.sin(a)*n[0]),hy+lw*(math.cos(a)*du[1]+math.sin(a)*n[1])) for a in [i*math.pi/2/24 for i in range(25)]]
                g=Polygon(pts)
            out.append(g)
    return out
def swing_boxes(doors, room):
    x0,y0,x1,y1=room[1:5]; out=[]
    for d in doors:
        x,y,ax,w,t=d[:5]; s=d[5] if len(d)>5 and isinstance(d[5],(int,float)) else 1
        if t not in('door','double'): continue
        if ax=='x':
            b=box(x,y+(0 if s>0 else -w),x+w,y+(w if s>0 else 0))
        else:
            b=box(x+(0 if s>0 else -w),y,x+(w if s>0 else 0),y+w)
        if t=='double': 
            b=box(b.bounds[0]-(w/2 if ax=='y' else 0)*0, b.bounds[1],b.bounds[2],b.bounds[3])
        out.append((d,b))
    return out
def best(room, fixes, doors, inset=0.2, use_swing=True):
    x0,y0,x1,y1=room[1:5]
    inner=box(x0+inset,y0+inset,x1-inset,y1-inset)
    obs=[box(f[0],f[1],f[2],f[3]) for f in fixes if f[5]>0.5 and not (isinstance(f[6],list) and f[6]==[0.80,0.88,1.0])]
    if use_swing:
        for b in swing_geoms(doors,room,use_swing):
            if b.intersects(inner) and b.intersection(inner).area>0.5*b.area: obs.append(b)
    o=unary_union(obs) if obs else None
    bd=inner.boundary
    bestr=0;bc=None
    for cx in np.arange(x0+inset,x1-inset+1e-9,0.1):
        for cy in np.arange(y0+inset,y1-inset+1e-9,0.1):
            p=Point(cx,cy)
            if not inner.contains(p): continue
            r=p.distance(bd)
            if o is not None:
                if o.contains(p): continue
                r=min(r,p.distance(o))
            if r>bestr: bestr=r;bc=(round(cx,1),round(cy,1))
    return 2*bestr,bc
if __name__=='__main__':
    import json
    for opt in 'DE':
      for lvl in ('main','base'):
        d=load(opt,lvl); fx=[f for f in d['fixtures']+d['furniture']]
        for r in d['rooms']:
            L=lab(r); k=r[6]
            if k in('bath','kitchen') or 'LAUNDRY' in L or 'LDRY' in L or 'FOYER' in L or 'VESTIB' in L or 'MUD' in L and k!='porch' or 'POWDER' in L or 'WC' in L:
                a,c=best(r,fx,d['doors'],use_swing=False); b,c2=best(r,fx,d['doors'],use_swing='leaf'); e,c3=best(r,fx,d['doors'],use_swing='arc')
                print(opt,lvl,'%-18s'%L,'dims %.1fx%.1f'%(r[3]-r[1]-0.4,r[4]-r[2]-0.4),'maxcircle(no swing) %.2f ft (%.0f mm)'%(a,a*304.8),'| leaf@90 %.2f (%.0f) | arc %.2f (%.0f)'%(b,b*304.8,e,e*304.8), 'PASS' if e>=5.58 else ('pass-leaf' if b>=5.58 else ('pass-nodoor' if a>=5.58 else 'FAIL')), c)
