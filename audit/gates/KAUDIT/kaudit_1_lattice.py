#!/usr/bin/env python3
# GATE KAUDIT — Script 1: THE LATTICE (counted cold, no inheritance).
# Build the c/a=sqrt(2) BCT point set from its definition, enumerate the
# nearest-neighbour shell by brute force, test bipartiteness, exhibit a
# triangle, and compute C_A(3) = (A^3)_ii from a finite cluster.
# Deterministic: no randomness.
import numpy as np
import itertools

SQRT2 = np.sqrt(2.0)

def bct_points(N):
    """All BCT sites (a=1, c=sqrt2) with integer indices in [-N,N].
       A = corners (n1,n2,n3*sqrt2); B = body centres (n1+1/2,n2+1/2,(n3+1/2)*sqrt2)."""
    pts=[]; tags=[]
    rng=range(-N,N+1)
    for n1,n2,n3 in itertools.product(rng,rng,rng):
        pts.append((n1, n2, n3*SQRT2)); tags.append('A')
        pts.append((n1+0.5, n2+0.5, (n3+0.5)*SQRT2)); tags.append('B')
    return np.array(pts), np.array(tags)

pts,tags = bct_points(3)
# reference site: an A site at the origin
origin = np.array([0.0,0.0,0.0])
d = np.linalg.norm(pts-origin,axis=1)
order = np.argsort(d)
print("=== NN shells around an A (corner) site at origin ===")
shell={}
for i in order[1:]:  # skip self
    dd = round(d[i],6)
    shell.setdefault(dd,[]).append((tuple(np.round(pts[i],4)), tags[i]))
for k in sorted(shell)[:4]:
    vs=shell[k]
    print(f"  distance {k:.6f}: multiplicity {len(vs)}")
    for v,tg in vs:
        print(f"      {v}  [{tg}]")

nn_dist = sorted(shell)[0]
nn = shell[nn_dist]
print(f"\nCOORDINATION NUMBER at minimum distance {nn_dist:.6f}: {len(nn)}")
n_to_B = sum(1 for _,tg in nn if tg=='B')
n_to_A = sum(1 for _,tg in nn if tg=='A')
print(f"   of which to B (body-centre): {n_to_B}   to A (in-plane corner): {n_to_A}")

# App K's claimed NN set: 8 vectors (+-1/2,+-1/2,+-sqrt2/2)
print("\n=== App K's claimed 8 NN (+-1/2,+-1/2,+-sqrt2/2) distances ===")
for s in itertools.product([+.5,-.5],[+.5,-.5],[+SQRT2/2,-SQRT2/2]):
    print(f"   {s} -> |.|={np.linalg.norm(s):.6f}")
print("In-plane A-A candidates App K omits:")
for s in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]:
    print(f"   {s} -> |.|={np.linalg.norm(s):.6f}")

# ---- Bipartite test: exhibit an odd (length-3) closed walk among mutual NN ----
print("\n=== Bipartite / triangle test ===")
O = np.array([0.0,0.0,0.0])          # A site
P = np.array([1.0,0.0,0.0])          # A site, in-plane NN of O
Q = np.array([0.5,0.5,SQRT2/2])      # B site, NN of O
def dist(a,b): return np.linalg.norm(a-b)
print(f"  |O-P| = {dist(O,P):.6f}  (NN? {np.isclose(dist(O,P),nn_dist)})")
print(f"  |O-Q| = {dist(O,Q):.6f}  (NN? {np.isclose(dist(O,Q),nn_dist)})")
print(f"  |P-Q| = {dist(P,Q):.6f}  (NN? {np.isclose(dist(P,Q),nn_dist)})")
tri = np.isclose(dist(O,P),nn_dist) and np.isclose(dist(O,Q),nn_dist) and np.isclose(dist(P,Q),nn_dist)
print(f"  -> O,P,Q form a length-3 closed walk (triangle): {tri}")
print(f"  -> lattice is BIPARTITE: {not tri}")

# ---- Are 'A' and 'B' sites equivalent (single FCC Bravais lattice)? ----
def neighbour_multiset(site):
    dd=np.linalg.norm(pts-site,axis=1)
    m=dd[(dd>1e-9)&(dd<nn_dist+1e-6)]
    return len(m)
iA=np.argmin(np.linalg.norm(pts-np.array([0,0,0]),axis=1))
iB=np.argmin(np.linalg.norm(pts-np.array([0.5,0.5,SQRT2/2]),axis=1))
print(f"\n=== A vs B site environment (Bravais equivalence) ===")
print(f"  coordination of an A site: {neighbour_multiset(pts[iA])}")
print(f"  coordination of a B site : {neighbour_multiset(pts[iB])}")
print("  identical environment => A and B are equivalent points of ONE Bravais (FCC) lattice,")
print("  so the correct tight-binding model is SINGLE-BAND, not a bipartite 2-band model.")

# ---- C_A(3) = (A^3)_ii from a finite cluster adjacency matrix ----
print("\n=== C_A(3) = (A^3)_ii  (closed 3-walks per site) ===")
# Build adjacency for sites well inside the cluster to avoid boundary undercount.
core_mask = np.max(np.abs(pts[:, :2]),axis=1) <= 1.5
# use full set for adjacency, evaluate (A^3)_ii only at a central site
D = np.linalg.norm(pts[:,None,:]-pts[None,:,:],axis=2)
A = ((D>1e-9)&(D<nn_dist+1e-6)).astype(np.int64)
# central A site index
c_idx = np.argmin(np.linalg.norm(pts-np.array([0,0,0]),axis=1))
A2 = A @ A
A3 = A2 @ A
print(f"  row-sum (coordination) at central site: {A.sum(axis=1)[c_idx]}")
print(f"  (A^3)_ii at central A site  = C_A(3) = {A3[c_idx,c_idx]}")
# also check a B central site
cB_idx = np.argmin(np.linalg.norm(pts-np.array([0.5,0.5,SQRT2/2]),axis=1))
print(f"  (A^3)_ii at central B site  = C_A(3) = {A3[cB_idx,cB_idx]}")
print(f"  triangles through the site  = C_A(3)/2 = {A3[c_idx,c_idx]//2}")
print("\n  C_A(3) != 0  ==>  T1 (all closed walks even) is FALSE on the correct lattice.")
