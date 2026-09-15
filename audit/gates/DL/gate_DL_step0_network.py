# GATE DL — STEP 0: FCC void network as a graph (deterministic, cold build)
# Nodes = octahedral + tetrahedral interstitial voids of FCC (c/a=sqrt2).
# Edges = triangular "windows" = nearest oct-tet face-sharing pairs.
# Reports V, E, components C, cycle rank b1 = E - V + C, degrees, per-cell densities.
# Also computes the edge-direction second-moment tensor S = sum_e dhat_e (x) dhat_e
# as a symmetry proxy for leading-order dielectric/response isotropy.
import numpy as np
from itertools import product

# --- conventional FCC cubic cell, a = 1 ---
# FCC lattice points per cube: (0,0,0),(1/2,1/2,0),(1/2,0,1/2),(0,1/2,1/2)
fcc_basis = np.array([[0,0,0],[.5,.5,0],[.5,0,.5],[0,.5,.5]])
# Octahedral holes = FCC + (1/2,1/2,1/2)  (an FCC lattice, 1 per atom)
oct_basis = (fcc_basis + np.array([.5,.5,.5])) % 1.0
# Tetrahedral holes = (1/4,1/4,1/4)+FCC  and  (3/4,3/4,3/4)+FCC  (2 per atom)
tet_basis = np.vstack([(fcc_basis+np.array([.25,.25,.25]))%1.0,
                       (fcc_basis+np.array([.75,.75,.75]))%1.0])

def build(L, periodic=True):
    octs=[]; tets=[]
    for i,j,k in product(range(L),repeat=3):
        shift=np.array([i,j,k])
        for b in oct_basis: octs.append(b+shift)
        for b in tet_basis: tets.append(b+shift)
    octs=np.array(octs); tets=np.array(tets)
    # dedupe (periodic images across cube faces coincide)
    def dedupe(P):
        keys={}; keep=[]
        for idx,p in enumerate(P):
            key=tuple(np.round(p%L if periodic else p,6))
            if key not in keys:
                keys[key]=len(keep); keep.append(idx)
        return P[keep]
    octs=dedupe(octs); tets=dedupe(tets)
    nodes=np.vstack([octs,tets])
    n_oct=len(octs); n_tet=len(tets)
    d_target=np.sqrt(3)/4.0     # nearest oct-tet distance in units of a
    edges=set(); deg=np.zeros(len(nodes),dtype=int)
    dirs=[]
    box=np.array([L,L,L],dtype=float)
    for io in range(n_oct):
        o=octs[io]
        diff=tets-o
        if periodic:
            diff=diff-box*np.round(diff/box)
        dist=np.linalg.norm(diff,axis=1)
        for it in np.where(np.abs(dist-d_target)<1e-6)[0]:
            a=io; b=n_oct+it
            e=(min(a,b),max(a,b))
            if e not in edges:
                edges.add(e); deg[a]+=1; deg[b]+=1
                v=diff[it]; dirs.append(v/np.linalg.norm(v))
    V=len(nodes); E=len(edges)
    # components via union-find
    par=list(range(V))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for (a,b) in edges:
        ra,rb=find(a),find(b)
        if ra!=rb: par[ra]=rb
    C=len({find(x) for x in range(V)})
    b1=E-V+C
    S=np.zeros((3,3))
    for d in dirs: S+=np.outer(d,d)
    return dict(L=L,V=V,E=E,C=C,b1=b1,n_oct=n_oct,n_tet=n_tet,
               oct_deg=int(deg[:n_oct].mean()) if n_oct else 0,
               oct_deg_min=int(deg[:n_oct].min()), oct_deg_max=int(deg[:n_oct].max()),
               tet_deg=int(deg[n_oct:].mean()) if n_tet else 0,
               tet_deg_min=int(deg[n_oct:].min()), tet_deg_max=int(deg[n_oct:].max()),
               S=S/len(dirs))

print("=== FCC void network (periodic torus of L^3 conventional cubic cells) ===")
for L in [2,3,4]:
    r=build(L,periodic=True)
    cells=L**3
    print(f"\nL={L}  ({cells} cubic cells, {4*cells} atoms):")
    print(f"  V={r['V']}  (oct={r['n_oct']}, tet={r['n_tet']})   E={r['E']}   C={r['C']}   b1=E-V+C={r['b1']}")
    print(f"  per cubic cell:  V/cell={r['V']/cells:.3f}  E/cell={r['E']/cells:.3f}  (E-V)/cell={(r['E']-r['V'])/cells:.3f}")
    print(f"  per atom      :  V/atom={r['V']/(4*cells):.3f}  E/atom={r['E']/(4*cells):.3f}  (E-V)/atom={(r['E']-r['V'])/(4*cells):.3f}")
    print(f"  b1 per node   :  {r['b1']/r['V']:.4f}")
    print(f"  oct degree: mean={r['oct_deg']} (min {r['oct_deg_min']}, max {r['oct_deg_max']})   tet degree: mean={r['tet_deg']} (min {r['tet_deg_min']}, max {r['tet_deg_max']})")
    S=r['S']
    print(f"  edge-direction 2nd-moment tensor S = <dhat (x) dhat> (should be ~ (1/3) I for isotropy):")
    print("   ",np.array2string(S,precision=5,suppress_small=True).replace('\n','\n    '))
    w=np.linalg.eigvalsh(S)
    print(f"   eigenvalues: {np.array2string(w,precision=5)}   anisotropy(max-min)={w.max()-w.min():.2e}")
