import sys, json, numpy as np
from u1lat import Lattice
kind, L, b, nth, nme, seed, start = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
lat = Lattice(kind, L, seed)
lat.hot() if start == 'hot' else lat.cold()
for _ in range(nth): lat.sweep(b)
es = []
for _ in range(nme): lat.sweep(b); es.append(lat.energy())
es = np.array(es)
Np = lat.npl * L**4
print(json.dumps(dict(kind=kind, L=L, beta=b, start=start, E=es.mean(), C=Np*es.var(), q=[float(np.quantile(es,x)) for x in (.05,.5,.95)])))
