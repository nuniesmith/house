import re,sys,math
src=open('/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/main_floor_h.scad').read()
def get(name):
    m=re.search(r'function '+name+r'\(\) = (\[.*?\n\]);',src,re.S)
    t=re.sub(r'//.*','',m.group(1))
    env=dict(counter=1,wood=1,steel=1,dark=1,basin=1,hearth=1,white=1,shelf=1,tile=1,sofa=1,bed=1,circle_c=1,table=1)
    return eval(t,{},env)
rooms=get('main_rooms');fx=get('main_fixtures');doors=get('main_doors')
T=0.4
def circ(room,r=2.785,obst_doors=True):
    nm=room[0] if isinstance(room[0],str) else ' '.join(room[0])
    x0,y0,x1,y1=room[1:5]
    x0+=T/2;y0+=T/2;x1-=T/2;y1-=T/2
    obs=[f[:4] for f in fx if f[5]>0.1 and f[6]!=None and not(len(f)>8 and f[8]=="round") and f[0]<x1 and f[2]>x0 and f[1]<y1 and f[3]>y0]
    # door swing discs: doors with swing on this room's walls
    best=None
    step=0.1
    x=x0+r
    while x<=x1-r+1e-9:
        y=y0+r
        while y<=y1-r+1e-9:
            ok=True
            for a,b,c,d in obs:
                dx=max(a-x,0,x-c);dy=max(b-y,0,y-d)
                if math.hypot(dx,dy)<r: ok=False;break
            if ok: return nm,(round(x,1),round(y,1))
            y+=step
        x+=step
    return nm,None
for n in ['KITCHEN','POWDER','SHARED BATH','LAUNDRY','ENSUITE','FOYER','VESTIBULE']:
    for rm in rooms:
        nm=rm[0] if isinstance(rm[0],str) else ' '.join(rm[0])
        if nm==n: print(circ(rm), 'room',rm[1:5])
