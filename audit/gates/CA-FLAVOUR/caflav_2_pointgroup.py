import numpy as np
from itertools import product
from mpmath import mp, mpf, sqrt
mp.dps=60

# Holohedral point group of the BCT lattice = set of orthogonal matrices O (det=+-1)
# mapping the lattice to itself. Enumerate signed permutation matrices (the candidates
# for a lattice with orthogonal conventional axes) and test lattice invariance.
def point_group_order(r):
    a=1.0; c=float(r)
    B=np.diag([a,a,c])            # conventional cell metric axes
    Binv=np.linalg.inv(B)
    # candidate O in Cartesian must map lattice vectors to lattice vectors.
    # Generate all 48 signed permutation matrices (proper+improper cubic-axis ops).
    perms=[]
    import itertools
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i in range(3):
                M[i,p[i]]=s[i]
            perms.append(M)
    good=0
    # lattice points (fractional): all integer combos of primitive vectors.
    # Use conventional + centering: a point is lattice iff frac coords are all int OR all half-int-shifted by (1/2,1/2,1/2).
    def is_lattice(v):
        f=Binv.dot(v)
        # either all integer, or all (integer+1/2)
        allint = np.all(np.abs(f-np.round(f))<1e-9)
        shifted=f-0.5
        allhalf = np.all(np.abs(shifted-np.round(shifted))<1e-9)
        return allint or allhalf
    # test each candidate on the generating lattice vectors
    gens=[np.array([a,0,0]),np.array([0,a,0]),np.array([0,0,c]),np.array([a/2,a/2,c/2])]
    for O in perms:
        if all(is_lattice(O.dot(g)) for g in gens):
            good+=1
    return good

print("=== holohedral point-group order vs c/a ===")
sq2=float(np.sqrt(2))
for r in [1.0,1.1,1.3,sq2-1e-3,sq2,sq2+1e-3,1.6,2.0]:
    tag=""
    if abs(r-1.0)<1e-9: tag=" (BCC: O_h)"
    if abs(r-sq2)<1e-9: tag=" (FCC: O_h)"
    print(f"c/a={r:.6f}  |point group|={point_group_order(r)}{tag}")

print("\n=== tetrahedral void geometry vs c/a ===")
# In FCC(=BCT at sqrt2) the tetrahedral interstitial sits at (1/4,1/4,1/4) of the FCC cube,
# surrounded by 4 lattice atoms forming a tetrahedron. Test regularity via the 4 vertices
# of the tet void in the BCT description and measure edge-length spread.
# Tet void vertices (one standard set) around site (a/4,a/4,c/4)-type; simplest:
# use FCC cube of side L. At sqrt2, a_fcc = a*sqrt2? We just test the *shape*:
# the 4 nearest atoms to a tetrahedral hole in BCT. Build from NN geometry.
def tet_void_edge_spread(r):
    a=1.0;c=float(r)
    # candidate tetrahedral coordination: pick the tetrahedral hole between
    # two corner atoms and two body atoms. Vertices:
    V=np.array([
        [0,0,0],
        [a,0,0],
        [a/2,a/2,c/2],
        [a/2,-a/2,c/2],
    ])
    ctr=V.mean(axis=0)
    # edges
    edges=[]
    for i in range(4):
        for j in range(i+1,4):
            edges.append(np.linalg.norm(V[i]-V[j]))
    edges=np.array(edges)
    return edges.min(),edges.max(),edges.std()
for r in [1.0,sq2-0.05,sq2,sq2+0.05,1.6]:
    lo,hi,sd=tet_void_edge_spread(r)
    reg="REGULAR (T_d)" if sd<1e-9 else "distorted"
    print(f"c/a={r:.6f}  tet-void edges min={lo:.6f} max={hi:.6f} std={sd:.2e}  -> {reg}")

print("\n=== second-moment (acoustic) tensor M_ij vs c/a, over the 12-shell at sqrt2 ===")
# M_ij = sum over NN bonds of r_i r_j. At sqrt2 this must be isotropic (prop to identity).
def second_moment(r,use_full=True):
    a=1.0;c=float(r)
    # the 12 vectors that are NN AT sqrt2 (8 body + 4 in-plane); evaluate M at general r
    body=[np.array([sx*a/2,sy*a/2,sz*c/2]) for sx in(1,-1) for sy in(1,-1) for sz in(1,-1)]
    inpl=[np.array([a,0,0]),np.array([-a,0,0]),np.array([0,a,0]),np.array([0,-a,0])]
    vecs=body+inpl
    M=np.zeros((3,3))
    for v in vecs:
        M+=np.outer(v,v)
    return M
for r in [1.0,sq2-0.02,sq2,sq2+0.02]:
    M=second_moment(r)
    diag=np.diag(M)
    print(f"c/a={r:.6f}  M_diag={np.round(diag,6)}  isotropic={np.allclose(diag,diag[0]) and np.allclose(M-np.diag(diag),0)}")
print("\nAnalytic: M_ij/a^2 = diag(4,4,2*(c/a)^2). Isotropic iff 2(c/a)^2=4 <=> c/a=sqrt2. (reproduces CN-AM-04)")
