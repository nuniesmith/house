import re,math,sys
def load(path):
    src=open(path).read()
    def get(name):
        m=re.search(r'function '+name+r'\(\) = (\[.*?\n\]);',src,re.S)
        t=re.sub(r'//.*','',m.group(1))
        env={'basement_ceiling':(lambda:10),'bc':10,**{k:1 for k in 'counter wood steel dark basin hearth white shelf tile sofa bed circle_c table rug'.split()}}
        return eval(t,{},env)
    return src,get
D='/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/'
T=0.4
def nm(r): return r[0] if isinstance(r[0],str) else ' '.join(r[0])
def maxcirc(room,fx,doors,swing=False):
    x0,y0,x1,y1=[room[1]+T/2,room[2]+T/2,room[3]-T/2,room[4]-T/2]
    obs=[f[:4] for f in fx if f[5]>0.1 and not(len(f)>8 and f[8]=="round") and f[0]<x1 and f[2]>x0 and f[1]<y1 and f[3]>y0]
    if swing:
        # door leaf swing squares into room: door on room edge, swing into room if inside
        for d in doors:
            x,y,ax,w,t=d[:5]; 
            if t!='door': continue
            if ax=='x':
                if abs(y-room[2])<.01: obs.append((x,y,x+w,y+w))
                if abs(y-room[4])<.01: obs.append((x,y-w,x+w,y))
            else:
                if abs(x-room[1])<.01: obs.append((x,y,x+w,y+w))
                if abs(x-room[3])<.01: obs.append((x-w,y,x,y+w))
    best=(0,None)
    x=x0
    while x<=x1:
        y=y0
        while y<=y1:
            r=min(x-x0,x1-x,y-y0,y1-y)
            for a,b,c,d in obs:
                dx=max(a-x,0,x-c);dy=max(b-y,0,y-d)
                r=min(r,math.hypot(dx,dy))
            if r>best[0]: best=(r,(round(x,1),round(y,1)))
            y+=0.1
        x+=0.1
    return best
for f,names in [('main_floor_h.scad',['KITCHEN','POWDER','SHARED BATH','LAUNDRY','ENSUITE','VESTIBULE','FOYER']),('basement_h.scad',['BATH','UTILITY'])]:
    src,get=load(D+f)
    rooms=get('main_rooms' if 'main' in f else 'basement_rooms') if 'main' in f else None
    if rooms is None:
        m=re.findall(r'function (\w+)\(\)',src); print(m)
        rooms=get([x for x in m if 'rooms' in x][0])
        fx=get([x for x in m if 'fixtures' in x][0]); doors=get([x for x in m if 'doors' in x][0])
    else:
        fx=get('main_fixtures');doors=get('main_doors')
    for r in rooms:
        if nm(r) in names:
            a=maxcirc(r,fx,doors);b=maxcirc(r,fx,doors,True)
            print(f,nm(r),'max dia ft %.2f (%.0f mm) at %s; with door leaf %.2f ft'%(2*a[0],2*a[0]*304.8,a[1],2*b[0]))
