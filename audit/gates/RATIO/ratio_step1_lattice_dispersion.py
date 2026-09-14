#!/usr/bin/env python3
"""
Gate RATIO — Step 1: scalar phonon dispersion on the BCT lattice.
Model executing: Claude Opus 4.8.

The continuum GP action (MINIMAL_BCT 1.2) is rotationally invariant: its phonon
dispersion is exactly isotropic and cannot depend on direction, let alone on a
radius ratio. Anisotropy can only come from the LATTICE. We test, by explicit
lattice dynamics, whether the sound-speed anisotropy depends on the lattice
shape eta = c/a (the shape that the void radii encode), and what happens at the
FCC point eta = sqrt(2) that the model's specific radii pin.

Scalar field phi_n, harmonic n.n. coupling:  omega^2(k) = sum_delta K_delta * 4 sin^2(k.delta/2)
Quadratic (sound) tensor:  D_ij = sum_delta K_delta * delta_i * delta_j
"""
import numpy as np

def neighbor_set(eta, a=1.0):
    """Return list of (vector, kind) for BCT with axial ratio eta=c/a.
       Body-centre bonds: (+-a/2,+-a/2,+-c/2) [8].  In-plane bonds: (+-a,0,0),(0,+-a,0) [4]."""
    c = eta*a
    bc = []
    for sx in (+1,-1):
        for sy in (+1,-1):
            for sz in (+1,-1):
                bc.append((np.array([sx*a/2, sy*a/2, sz*c/2]), 'bc'))
    ip = [ (np.array([+a,0,0]),'ip'), (np.array([-a,0,0]),'ip'),
           (np.array([0,+a,0]),'ip'), (np.array([0,-a,0]),'ip') ]
    return bc, ip

def sound_tensor(bonds_with_K):
    D = np.zeros((3,3))
    for delta, K in bonds_with_K:
        D += K*np.outer(delta,delta)
    return D

print("MODEL: Claude Opus 4.8")
print("="*70)
print("REGIME A: touching shell only (eta < sqrt2): body-centre bonds dominate")
print("  Spheres touch along the body diagonal; coordination 8; K_bc = K.")
print("-"*70)
for eta in [1.0, 1.1, 1.2247, 1.3, np.sqrt(2)]:
    bc, ip = neighbor_set(eta)
    bonds = [(d,1.0) for d,_ in bc]        # only body-centre shell
    D = sound_tensor(bonds)
    cx2, cz2 = D[0,0], D[2,2]
    print(f"  eta={eta:6.4f}:  D_xx={cx2:.4f}  D_zz={cz2:.4f}   "
          f"c_z/c_x = {np.sqrt(cz2/cx2):.5f}   (predict eta={eta:.5f})")
print("  => c_z/c_x = eta EXACTLY. The scalar sound speed reads out the SHAPE.")
print("     If eta (equivalently the radius ratio) is free, the ratio DOES work.")

print("\n"+"="*70)
print("REGIME B: FCC point eta=sqrt2. Close-packing brings in-plane bonds to")
print("  the SAME distance -> coordination 12, cubic symmetry, K_bc=K_ip=K.")
print("-"*70)
eta = np.sqrt(2)
bc, ip = neighbor_set(eta)
# verify all 12 at equal distance:
dists = sorted(set(round(np.linalg.norm(d),6) for d,_ in bc+ip))
bonds = [(d,1.0) for d,_ in bc+ip]
D = sound_tensor(bonds)
print(f"  neighbour distances present: {dists}  (all equal => 12-fold FCC)")
print(f"  D_xx={D[0,0]:.4f}  D_yy={D[1,1]:.4f}  D_zz={D[2,2]:.4f}")
print(f"  c_z/c_x = {np.sqrt(D[2,2]/D[0,0]):.6f}   (off-diagonal max={np.abs(D-np.diag(np.diag(D))).max():.1e})")
print("  => ISOTROPIC at O(k^2). At the FCC point the shape's imprint on the")
print("     leading dispersion CANCELS: the ratio does NO work at leading order.")

print("\n"+"="*70)
print("O(k^4): residual cubic anisotropy for FCC (a FIXED number, no free ratio)")
print("-"*70)
# omega^2(k) = sum_delta K*4 sin^2(k.delta/2). Expand to k^4 along [100] and [111].
def omega2(kvec, bonds):
    s=0.0
    for delta,K in bonds:
        s += K*4*np.sin(np.dot(kvec,delta)/2)**2
    return s
a=1.0
for direction,label in [((1,0,0),'[100]'), ((1,1,1),'[111]')]:
    u=np.array(direction,float); u/=np.linalg.norm(u)
    ks=np.array([1e-3,2e-3,3e-3])
    # fit omega^2 = A k^2 + B k^4
    y=np.array([omega2(k*u,bonds) for k in ks])
    M=np.vstack([ks**2,ks**4]).T
    A,B=np.linalg.lstsq(M,y,rcond=None)[0]
    print(f"  {label}: omega^2 ~ {A:.4f} k^2 + ({B:.4f}) k^4   (A isotropic; B carries cubic anisotropy)")
print("  => Anisotropy appears only at O(k^4) and is a pure FCC constant;")
print("     it contains no independent r_oct/r_tet information.")

print("\n"+"="*70)
print("CONCLUSION OF STEP 1")
print("-"*70)
print("  * Shape FREE  -> c_z/c_x = eta: ratio does genuine work, BUT eta is then")
print("    a free geometric parameter (breaks 'zero free parameters').")
print("  * Shape PINNED to FCC (what the model's radii do) -> leading dispersion")
print("    isotropic; ratio's imprint vanishes; only a fixed O(k^4) constant.")
print("  The model cannot have both a fixed (zero-parameter) shape AND have the")
print("  ratio do observable work. The specific radii choose the pinned horn.")
