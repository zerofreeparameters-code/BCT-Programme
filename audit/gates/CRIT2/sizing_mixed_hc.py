import sys, json, numpy as np
from u1lat import Lattice
b=float(sys.argv[1]); L=int(sys.argv[2]); N=int(sys.argv[3])
lat=Lattice('hc',L,int(b*1e4)); lat.hot()
half=np.indices((L,)*4)[0] < L//2
for k in range(lat.nd): lat.theta[k][half]=0.0      # half ordered, half random
traj=[]
for s in range(1,N+1):
    lat.sweep(b)
    if s%250==0: traj.append(round(lat.energy(),4))
print(json.dumps(dict(beta=b,L=L,traj=traj)))
