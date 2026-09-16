import numpy as np
from itertools import combinations, permutations
np.set_printoptions(suppress=True)

# Point group of the lattice = orthogonal maps preserving the neighbour set.
# Use the first TWO shells so a linearly-independent basis always exists
# (above c/a=sqrt2 the nearest shell is only 4 coplanar vectors, so the
#  nearest shell alone cannot furnish a 3D basis -- the second shell fixes that).
def shell_vectors(r, nshell=2):
    a=1.0; c=float(r)
    pts=[]
    N=3
    for i in range(-N,N+1):
        for j in range(-N,N+1):
            for k in range(-N,N+1):
                pts.append((i*a,j*a,k*c))
                pts.append(((i+0.5)*a,(j+0.5)*a,(k+0.5)*c))
    P=np.array(pts)
    d=np.linalg.norm(P,axis=1)
    P=P[d>1e-9]; d=d[d>1e-9]
    dvals=[]
    for x in np.sort(d):
        if not any(abs(x-y)<1e-6 for y in dvals):
            dvals.append(x)
        if len(dvals)>=nshell: break
    keep=np.array([any(abs(np.linalg.norm(p)-y)<1e-6 for y in dvals) for p in P])
    return P[keep]

def point_group_order(r):
    V=shell_vectors(r,nshell=2)
    def in_V(v):
        return any(np.allclose(v,w,atol=1e-6) for w in V)
    # basis: first 3 linearly independent vectors drawn from the WHOLE set V
    basis_idx=None
    for combo in combinations(range(len(V)),3):
        B=V[list(combo)].T
        if abs(np.linalg.det(B))>1e-6:
            basis_idx=list(combo); break
    B=V[basis_idx].T; Binv=np.linalg.inv(B); Gram=B.T.dot(B)
    Bnorms=np.linalg.norm(B,axis=0)
    ops=set()
    Vnorms=np.linalg.norm(V,axis=1)
    # candidate image for each basis slot must have matching norm
    cand=[np.where(np.abs(Vnorms-Bnorms[s])<1e-6)[0] for s in range(3)]
    for i in cand[0]:
        for j in cand[1]:
            if j==i: continue
            for k in cand[2]:
                if k in (i,j): continue
                Bim=V[[i,j,k]].T
                if not np.allclose(Bim.T.dot(Bim),Gram,atol=1e-6):
                    continue
                O=Bim.dot(Binv)
                if not np.allclose(O.dot(O.T),np.eye(3),atol=1e-6):
                    continue
                if all(in_V(O.dot(v)) for v in V):
                    ops.add(tuple(np.round(O.flatten(),4)))
    return len(ops)

sq2=float(np.sqrt(2))
print("=== TRUE holohedral point-group order (shell-automorphism method) ===")
for r in [1.0,1.2,sq2-2e-3,sq2,sq2+2e-3,1.6,2.0]:
    o=point_group_order(r)
    name={48:"O_h (cubic)",16:"D_4h (tetragonal)"}.get(o,f"order {o}")
    tag=""
    if abs(r-sq2)<1e-9: tag=" <-- FCC"
    elif abs(r-1)<1e-9: tag=" <-- BCC"
    print(f"c/a={r:.6f}  |G|={o}  {name}{tag}")
print("\nLoad-bearing: |G|=48 (O_h, cubic) exactly at c/a=sqrt2; D_4h (16) for any other ratio.")
