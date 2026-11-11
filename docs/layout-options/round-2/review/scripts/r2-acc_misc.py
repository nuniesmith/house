from parse import load
from circ import lab, swing_geoms
from shapely.geometry import box
from shapely.ops import unary_union
import sys
for o in (sys.argv[1] if len(sys.argv)>1 else 'DE'):
  for l in ('main','base'):
    d=load(o,l)
    ws=[(x[4],x[3]) for x in d['doors'] if x[4] in('door','double')]
    sing=[w for t,w in ws if t=='door']
    print(o,l,'single doors',len(sing),'min width in',round(min(sing)*12,1),'<3.0ft:',[(x[0],x[1],x[3]) for x in d['doors'] if x[4]=='door' and x[3]<3.0], 'doubles',[(x[0],x[1],x[3]) for x in d['doors'] if x[4]=='double'])
    print('  halls:',[(lab(r)[:12],round(r[3]-r[1]-0.4,1),round(r[4]-r[2]-0.4,1)) for r in d['rooms'] if r[6]=='hall'])
    # elevator approach
    el=[r for r in d['rooms'] if 'ELEVATOR' in lab(r)][0]
    print('  elevator',el[1:5],'door',[ (x[0],x[1],x[2],x[3]) for x in d['doors'] if x[4]=='door' and abs(x[0]-el[1])<0.05 or  x[4]=='door' and abs(x[0]-el[3])<0.05 and el[2]<=x[1]<=el[4] or x[4]=='door' and (abs(x[1]-el[2])<0.05 or abs(x[1]-el[4])<0.05) and el[1]<=x[0]<=el[3]])
