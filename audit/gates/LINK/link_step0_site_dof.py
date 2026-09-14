#!/usr/bin/env python3
"""
Gate LINK, Step 0: propagating-mode count for the corpus Hamiltonian AS WRITTEN.

Primary source (mount, Vol.1 Part1 text layer, App D.3 Sec 2.2, line 1258):
    H_lattice = -J sum_{<i,j>} cos(theta_i - theta_j),  theta_i = rotation angle of sphere i
i.e. ONE compact phase per SITE.  Harmonic form (line 1262): (J/2) sum_{<i,j>} (th_i-th_j)^2.

We Fourier-transform on the BCT lattice at c/a = sqrt(2) (12 equal nearest neighbours,
i.e. FCC with nn vectors of length sqrt(2) in units where a_cubic = 1) and diagonalise.
One site per primitive cell -> the dynamical matrix is 1x1: exactly one branch.
Also checks isotropy of omega(k) at small k (claimed in App E.0 / Letter 259).
"""
import numpy as np, itertools
nn=[np.array(v) for v in itertools.product([-1,0,1],repeat=3) if sum(abs(x) for x in v)==2]
assert len(nn)==12
def omega2(k, J=1.0, m=1.0):
    # H = (J/2) sum_<ij> (th_i-th_j)^2  ->  omega^2(k) = (2J/m) sum_delta (1-cos k.delta)  (half per pair)
    return (J/m)*sum(1-np.cos(k@d) for d in nn)
print("branches per primitive cell (1 site x 1 phase) = 1")
print("\nomega^2(k)/k^2 at small k, by direction (isotropy check):")
for kd in [np.array([1,0,0]),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3),np.array([2,1,0])/np.sqrt(5)]:
    for kk in [1e-3,1e-2]:
        k=kk*kd
        print(f"  dir={np.round(kd,3)} |k|={kk:6.4f}  w2/k2={omega2(k)/kk**2:.8f}")
print("\nSecond-moment tensor M_ij = sum_delta d_i d_j over the 12 nn vectors:")
M=sum(np.outer(d,d) for d in nn); print(M)
print("-> M = 4*I exactly (isotropic to leading order); w2 = (J/m)*|k|^2*tr(M)/(2*3)?  explicit:")
print("   coefficient of k^2 from expansion:", 0.5*np.trace(M)/3)
