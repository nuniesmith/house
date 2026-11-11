from parse import load
from circ import lab, swing_geoms
from shapely.geometry import box
from shapely.ops import unary_union
import numpy as np
for o in 'DE':
  for l in ('main','base'):
    d=load(o,l)
    el=[r for r in d['rooms'] if 'ELEVATOR' in lab(r)][0]
    ex0,ey0,ex1,ey1=el[1:5]
    dr=[x for x in d['doors'] if x[4]=='door' and ((x[2]=='y' and (abs(x[0]-ex0)<.05 or abs(x[0]-ex1)<.05) and ey0<=x[1]<=ey1) or (x[2]=='x' and (abs(x[1]-ey0)<.05 or abs(x[1]-ey1)<.05) and ex0<=x[0]<=ex1))]
    dr=[x for x in dr if 'ELEV' not in str(x)] 
    print(o,l,'elevator',el[1:5],'doors on its boundary',dr)
    for x in dr:
        # side of approach
        if x[2]=='y': side = -1 if abs(x[0]-ex0)<.05 else 1
        else: side = -1 if abs(x[1]-ey0)<.05 else 1
        # candidate: free floor = hall-kind rooms union (CL) + any room, minus fixtures
        halls=unary_union([box(*r[1:5]) for r in d['rooms'] if r[6] in('hall','stairwell') or (r[6]=='stair')])
        fl=halls.buffer(-0.2)
        obs=unary_union([box(f[0],f[1],f[2],f[3]) for f in d['fixtures']+d['furniture'] if f[5]>0.5] +swing_geoms([y for y in d['doors'] if y is not x],None,'leaf'))
        ok=[]
        for s in np.arange(-5+0.5,0.5+1e-9,0.25):
            if x[2]=='y':
                lo=x[1]+s; 
                sq=box(x[0]+0.2*side if side>0 else x[0]-5-0.2*0,lo,(x[0]+5) if side>0 else x[0],lo+5)
                sq=box(x[0],lo,x[0]+5,lo+5) if side>0 else box(x[0]-5,lo,x[0],lo+5)
            else:
                lo=x[0]+s
                sq=box(lo,x[1],lo+5,x[1]+5) if side>0 else box(lo,x[1]-5,lo+5,x[1])
            # shrink touching wall by 0.2 on elevator side: test sq buffered -0.01 within halls buffered
            inner=sq.buffer(-0.05)
            full=halls.buffer(0.2)  # allow wall face
            if fl.buffer(0.05).contains(sq.buffer(-0.2)) or (halls.buffer(-0.0).contains(sq.buffer(-0.01)) and fl.contains(sq.buffer(-0.01).buffer(0).intersection(fl))):
                pass
        # simpler: report max free depth/width of hall in front
        print('   hall union bounds in front:',[ (round(g.bounds[0],1),round(g.bounds[1],1),round(g.bounds[2],1),round(g.bounds[3],1)) for g in getattr(halls,'geoms',[halls])])
