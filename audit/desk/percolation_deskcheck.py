# DESK CHECK (non-gate): is the FCC interstitial void space a single connected
# percolating network, and what is the flow bottleneck? Textbook FCC geometry.
# BCT at c/a=sqrt(2) == FCC. Ratios are convention-free; corpus units use r_s=1/2.
import numpy as np, networkx as nx
from math import sqrt
from collections import Counter
from scipy.spatial import cKDTree

N = 4                                  # N x N x N conventional FCC cells, edge a = 1
def cells(frac):
    pts=[]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for f in frac:
                    pts.append((i+f[0], j+f[1], k+f[2]))
    return np.array(pts)

atoms = cells([(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)])
octs  = cells([(.5,.5,.5),(.5,0,0),(0,.5,0),(0,0,.5)])
tets  = cells([(.25,.25,.25),(.75,.25,.25),(.25,.75,.25),(.25,.25,.75),
               (.75,.75,.25),(.75,.25,.75),(.25,.75,.75),(.75,.75,.75)])

def dedup(P):
    seen=set(); out=[]
    for p in P:
        key=tuple(np.round(p,6))
        if key not in seen and all(0<=c<=N for c in p):
            seen.add(key); out.append(p)
    return np.array(out)
octs=dedup(octs); tets=dedup(tets)

# --- sphere & void radii (spheres touch along the FCC face diagonal) ---
nn   = 1/sqrt(2)                        # nearest-neighbour atom distance (a=1)
r_s  = nn/2                             # sphere radius (a=1 units)
# ratios (convention-free):
R_oct = sqrt(2)-1                       # r_oct / r_s
R_tet = sqrt(3/2)-1                     # r_tet / r_s
R_win = 2/sqrt(3)-1                     # r_window / r_s  (triangular gap, 3 touching spheres)
# corpus units set r_s = 1/2, so multiply each ratio by 1/2:
c_oct, c_tet, c_win = R_oct/2, R_tet/2, R_win/2

print("=== FCC void geometry ===")
print(f"  ratios to sphere radius:  r_oct/r_s = {R_oct:.6f} (sqrt(2)-1)")
print(f"                            r_tet/r_s = {R_tet:.6f} (sqrt(3/2)-1)")
print(f"                            r_win/r_s = {R_win:.6f} (2/sqrt(3)-1)  <-- bottleneck")
print(f"  ordering: window {R_win:.4f} < tet {R_tet:.4f} < oct {R_oct:.4f}")
print(f"  corpus units (r_s=1/2):   r_oct = {c_oct:.6f}, r_tet = {c_tet:.6f}, r_win = {c_win:.6f}")

# --- oct<->tet adjacency graph (shared triangular face) ---
oct_tet = sqrt(3)/4                     # nearest oct-tet separation (a=1)
G = nx.Graph()
for idx,p in enumerate(octs): G.add_node(('O',idx), pos=p)
for idx,p in enumerate(tets): G.add_node(('T',idx), pos=p)
tree=cKDTree(tets); deg_o=[]
for oi,p in enumerate(octs):
    nb=tree.query_ball_point(p, oct_tet+1e-3); deg_o.append(len(nb))
    for ti in nb: G.add_edge(('O',oi),('T',ti))

print("\n=== connectivity of the void network (4x4x4 supercell) ===")
print(f"  octahedral sites: {len(octs)},  tetrahedral sites: {len(tets)}")
comps=list(nx.connected_components(G)); big=max(comps,key=len)
print(f"  connected components: {len(comps)};  largest holds {len(big)}/{G.number_of_nodes()} nodes")
print(f"  oct->tet degree distribution: {dict(Counter(deg_o))}  (bulk oct shares 8 tet faces)")

pos=nx.get_node_attributes(G,'pos')
span=[max(pos[n][ax] for n in big)-min(pos[n][ax] for n in big) for ax in range(3)]
perc = all(s>=N-0.6 for s in span) and len(comps)==1
print(f"  largest component spans (x,y,z) = ({span[0]:.2f},{span[1]:.2f},{span[2]:.2f}) of {N}.0")
print(f"  PERCOLATES in all 3 axes and single component: {perc}")
