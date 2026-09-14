#!/usr/bin/env python3
"""
Gate LINK, Step 1: degree-of-freedom count of compact U(1) LINK variables on the
BCT lattice at c/a = sqrt(2) (= FCC: 12 equal nearest neighbours, 6 link directions
per site).  Linearised (weak-coupling) magnetic term = sum over the minimal closed
loops of the nearest-neighbour graph (triangles) of (lattice curl)^2.
We Fourier-transform the 6 link fields per site and diagonalise the 6x6 curl-energy
matrix M(k).  Expected structure, DERIVED here rather than asserted:
  * 1 exact zero eigenvalue for all k  -> the gauge mode (A_l -> A_l + grad lambda)
  * 2 eigenvalues ~ k^2               -> the two transverse photon polarisations
  * 3 eigenvalues O(1)                -> gapped lattice modes (link fields not of the
                                         form e_l . A(x) for any smooth vector A)
Source: constructed for Gate LINK; no BCT-corpus numbers enter.
"""
import numpy as np, itertools
np.set_printoptions(precision=6, suppress=True)

# FCC nearest-neighbour vectors (nn distance = sqrt(2) in these units)
nn = [np.array(v) for v in itertools.product([-1,0,1], repeat=3) if sum(abs(x) for x in v)==2]
assert len(nn)==12
# choose 6 positive directions
dirs = []
for v in nn:
    if not any(np.array_equal(v,-d) for d in dirs): dirs.append(v)
assert len(dirs)==6
def dir_index(v):
    for i,d in enumerate(dirs):
        if np.array_equal(v,d): return i,+1
        if np.array_equal(v,-d): return i,-1
    return None

# triangles through the origin: {0, d1, d2} with d2-d1 a nn vector
tris=[]
for a in nn:
    for b in nn:
        if np.array_equal(a,b): continue
        if any(np.array_equal(b-a,v) for v in nn):
            tris.append((a,b))
# each unordered triangle {0,a,b} appears twice (a,b),(b,a); keep one
seen=set(); T=[]
for a,b in tris:
    key=tuple(sorted([tuple(a),tuple(b)]))
    if key in seen: continue
    seen.add(key); T.append((a,b))
print("triangles through a site:", len(T))

def M_of_k(k):
    """6x6 Hermitian matrix of the quadratic form sum_tri |curl_tri|^2 (per site)."""
    M=np.zeros((6,6),dtype=complex)
    for a,b in T:
        c=np.zeros(6,dtype=complex)
        # link 0->a, then a->b, then b->0  : curl = A(0,a) + A(a,b) - A(0,b)
        for (x,v,sign) in [(np.zeros(3),a,+1),(a,b-a,+1),(np.zeros(3),b,-1)]:
            i,s = dir_index(v)
            # A_{v}(x) with v = s*dirs[i] : A_{-d}(x) = -A_d(x-d)
            if s==+1: c[i]+= sign*np.exp(1j*k@x)
            else:     c[i]+= -sign*np.exp(1j*k@(x-dirs[i]))
        M+=np.outer(c,c.conj())
    return M

def gauge_vector(k):
    return np.array([np.exp(1j*k@d)-1 for d in dirs])

print("\nk-direction   |k|      eigenvalues of M(k) (sorted)")
for kd in [np.array([1,0,0]),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3)]:
    for kk in [1e-3,1e-2,1e-1,0.5]:
        k=kk*kd; M=M_of_k(k); ev=np.linalg.eigvalsh(M)
        g=gauge_vector(k); res=np.linalg.norm(M@g)/np.linalg.norm(g)
        print(f"{np.round(kd,3)}  {kk:6.3f}  {ev}   |M g_gauge|/|g|={res:.1e}")

# scaling test of the two soft modes
print("\nSoft-mode scaling (k along [100]): eigenvalue/k^2 should approach a constant")
for kk in [1e-3,3e-3,1e-2,3e-2]:
    ev=np.linalg.eigvalsh(M_of_k(kk*np.array([1,0,0])))
    print(f"|k|={kk:7.4f}  ev[1]/k^2={ev[1]/kk**2:.6f}  ev[2]/k^2={ev[2]/kk**2:.6f}  ev[3]={ev[3]:.4f}")

# isotropy of the soft modes at small k (they should be degenerate and direction independent)
print("\nIsotropy of the photon branch at |k|=1e-2:")
for kd in [np.array([1,0,0]),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3),np.array([2,1,0])/np.sqrt(5)]:
    ev=np.linalg.eigvalsh(M_of_k(1e-2*kd)); print(np.round(kd,3), ev[1:3]/1e-4)

# formal count
Nlinks=6; Ngauge=1
print(f"\nPer site: link fields={Nlinks}; exact gauge null modes={Ngauge}; soft (photon) modes=2; gapped lattice modes={Nlinks-Ngauge-2}")
