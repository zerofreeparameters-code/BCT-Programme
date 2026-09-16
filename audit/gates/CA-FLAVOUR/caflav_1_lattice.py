import numpy as np
from mpmath import mp, mpf, sqrt
mp.dps = 60

# BCT lattice: conventional cell points at (0,0,0) and (1/2,1/2,1/2) in units (a,a,c).
# Set a=1, vary r = c/a. Enumerate all lattice points in a box, find NN shell.
def bct_points(r, N=3):
    a=1.0; c=float(r)
    pts=[]
    for i in range(-N,N+1):
        for j in range(-N,N+1):
            for k in range(-N,N+1):
                # corner sublattice
                pts.append((i*a, j*a, k*c))
                # body-centre sublattice
                pts.append(((i+0.5)*a,(j+0.5)*a,(k+0.5)*c))
    return np.array(pts)

def nn_shell(r):
    P=bct_points(r)
    d=np.linalg.norm(P,axis=1)
    d=d[d>1e-9]
    dmin=d.min()
    tol=1e-7
    count=int(np.sum(np.abs(d-dmin)<tol))
    return dmin, count

print("=== NN coordination vs c/a  (a=1) ===")
sq2=float(np.sqrt(2))
for r in [1.0, 1.20, 1.35, 1.40, sq2-1e-3, sq2, sq2+1e-3, 1.45, 1.55, 1.70, 2.0]:
    dmin,cnt=nn_shell(r)
    tag = "  <-- sqrt2 (FCC)" if abs(r-sq2)<1e-9 else ""
    print(f"c/a={r:.6f}  d_NN={dmin:.6f}  coordination={cnt}{tag}")

# Exact analytic check of the three distances at general r:
# body-centre NN: d1 = 0.5*sqrt(2 + r^2)
# in-plane corner: d2 = 1
# axial corner:    d3 = r
print("\n=== exact distances (a=1) ===")
for r in [mpf('1.0'), sqrt(2), mpf('1.5')]:
    d1=mpf('0.5')*sqrt(2+r*r); d2=mpf('1'); d3=r
    print(f"c/a={float(r):.6f}: d_body={float(d1):.9f}  d_inplane={float(d2):.9f}  d_axial={float(d3):.9f}")
print("\nAt c/a=sqrt2: d_body = 0.5*sqrt(2+2) = 0.5*2 = 1 = d_inplane  -> 8 body + 4 in-plane = 12 (cubic FCC)")
print("Just below sqrt2: d_body<1 -> 8 NN (BCC-type). Just above: d_body>1, in-plane=1 nearest -> 4 NN.")
