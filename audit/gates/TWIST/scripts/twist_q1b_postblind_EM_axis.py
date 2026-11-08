#!/usr/bin/env python3
"""
Gate TWIST -- POST-BLIND recompute of Q1 at Michel's request (12:13, 8 Nov 2026):
"requiring EM; spheres aligning along a particular axis".  The blind scores of the gate are
unchanged; this script answers Q1 again with two inputs declared and counted:

  EM    : the overall U(1) is gauged with an independent field A (charge q) and a Maxwell term
          (1/2mu)|curl A|^2  -> London length lambda, kappa_em = 1/(2 mu q^2) = K_s lambda^2.
  AXIS  : n is aligned to a common axis z: easy-axis/Zeeman potential  D (1 - n_z^2) or h (1 - n_z),
          or pinning n = z on every shell (the Q4(iv) grip term).

Parts
  1  gauge-covariant decomposition |(grad - iqA)Psi|^2 = (grad sqrt rho)^2 + rho[1/4|dn|^2 + C^2],
     C = grad phi + a_zeta - qA, and the identity q curl A = f[n] - curl C   (random fields, exact)
  2  London elimination of C: exact kernel c_F(k) = kappa_em/(1 + k^2 lambda^2) for the twist field,
     checked against a direct numerical minimisation on a periodic grid
  3  net local quartic: EM (+) vs density (-) -> sign threshold
  4  Derrick/size scan with the full non-local EM and density kernels on the scaled standard Hopf map:
     is there a stable knot, how big, and does the condensate survive in its core?
  5  axis alignment: what a zero-derivative potential / pinning can and cannot do for Q1
Units: lengths in a = l_P (xi = 2.31754 a, R = 0.5 a) unless stated; energies in K_s = (hbar^2/2m) n0.
Run: python3 -I twist_q1b_postblind_EM_axis.py
"""
import numpy as np
import sympy as sp
from scipy import optimize

ROCT = (np.sqrt(2) - 1) / 2; RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi
XI = 1 / np.sqrt(8 * np.pi * ALPHA0)
R = 0.5
rng = np.random.default_rng(1213)
X, Y, Z = sp.symbols('x y z', real=True); XYZ = (X, Y, Z)

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

def leaf(v, n):
    if isinstance(v, (list, tuple)):
        return np.array([leaf(q, n) for q in v])
    return np.asarray(v, dtype=float) * np.ones(n)

def rtrig(nt=3):
    e = sp.Float(rng.normal())
    for _ in range(nt):
        k = rng.normal(size=3)
        e += sp.Float(rng.normal()) * sp.sin(sp.Float(k[0]) * X + sp.Float(k[1]) * Y + sp.Float(k[2]) * Z + sp.Float(rng.uniform(0, 6.3)))
    return e

# =============================================================================== 1
hdr("1. Gauge-covariant decomposition with EM  (random rho, phi, zeta, A; exact derivatives)")
q = sp.Float(0.7)
p = [rtrig() + (2.0 if c == 0 else 0) for c in range(4)]
Nn = sp.sqrt(sum(t ** 2 for t in p))
u = [t / Nn for t in p]
phi = rtrig(); rho = sp.exp(sp.Float(0.3) * rtrig())
Avec = [rtrig(2) for _ in range(3)]
Psi = [sp.sqrt(rho) * sp.exp(sp.I * phi) * (u[0] + sp.I * u[1]), sp.sqrt(rho) * sp.exp(sp.I * phi) * (u[2] + sp.I * u[3])]
Dpsi2 = sum(sp.Abs(sp.diff(P_, v) - sp.I * q * Avec[i] * P_) ** 2 for P_ in Psi for i, v in enumerate(XYZ))
du = [[sp.diff(c, v) for c in u] for v in XYZ]
a_z = [u[0] * du[i][1] - u[1] * du[i][0] + u[2] * du[i][3] - u[3] * du[i][2] for i in range(3)]
nvec = [2 * (u[0] * u[2] + u[1] * u[3]), 2 * (u[0] * u[3] - u[1] * u[2]), u[0] ** 2 + u[1] ** 2 - u[2] ** 2 - u[3] ** 2]
dn2 = sum(sp.diff(nc, v) ** 2 for nc in nvec for v in XYZ)
C = [sp.diff(phi, v) + a_z[i] - q * Avec[i] for i, v in enumerate(XYZ)]
rhs = sum(sp.diff(sp.sqrt(rho), v) ** 2 for v in XYZ) + rho * (dn2 / 4 + sum(c ** 2 for c in C))
f_l = sp.lambdify(XYZ, Dpsi2, 'numpy'); f_r = sp.lambdify(XYZ, rhs, 'numpy')
Pts = rng.uniform(-2, 2, size=(600, 3))
L1 = np.real(f_l(*Pts.T)); R1 = f_r(*Pts.T)
print(f"  |(grad - iqA)Psi|^2 vs (grad sqrt rho)^2 + rho[1/4|dn|^2 + C^2]: max rel resid {np.max(np.abs(L1 - R1) / L1):.2e}")
def curl(F):
    return [sp.diff(F[2], Y) - sp.diff(F[1], Z), sp.diff(F[0], Z) - sp.diff(F[2], X), sp.diff(F[1], X) - sp.diff(F[0], Y)]
cA = curl(Avec); cC = curl(C); ca = curl(a_z)
idres = sp.lambdify(XYZ, [q * cA[k] - (ca[k] - cC[k]) for k in range(3)], 'numpy')
mh = sp.lambdify(XYZ, ca, 'numpy')
res = leaf(idres(*Pts.T), len(Pts)); scl = np.max(np.abs(leaf(mh(*Pts.T), len(Pts))))
print(f"  q curl A = curl a - curl C  (curl a = f[n] by Mermin-Ho):     max rel resid {np.max(np.abs(res)) / scl:.2e}")
print("  => with EM the gauge-invariant variables are (rho, n, C) plus B = (f[n] - curl C)/q. The twist")
print("     field's curl is still f[n] identically: a stays slaved. The new independent field is A (or C).")

# =============================================================================== 2
hdr("2. London elimination of C: kernel for the twist field  c_F(k) = kappa/(1 + k^2 lam^2)")
# E[C] = sum K_s |C|^2 + kappa |curl C - f|^2  on a periodic grid; K_s = 1, kappa = lam^2
Ng, Lb = 16, 8.0
h = Lb / Ng
k1 = 2 * np.pi * np.fft.fftfreq(Ng, d=h)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij'); Kv = np.stack([KX, KY, KZ]); K2 = KX ** 2 + KY ** 2 + KZ ** 2
# random smooth transverse f
g = np.stack([np.fft.fftn(rng.normal(size=(Ng, Ng, Ng))) * np.exp(-K2 / 2) for _ in range(3)])
kdotg = np.sum(Kv * g, axis=0); Kn = np.where(K2 == 0, 1, K2)
fk = g - Kv * kdotg / Kn; fk[:, 0, 0, 0] = 0
f = np.real(np.fft.ifftn(fk, axes=(1, 2, 3)))
def curl_fft(Cr):
    Ck = np.fft.fftn(Cr, axes=(1, 2, 3))
    cr = 1j * np.cross(Kv, Ck, axis=0)
    return np.real(np.fft.ifftn(cr, axes=(1, 2, 3)))
for lam in (0.3, 1.0, 3.0):
    kap = lam ** 2
    def E_and_grad(cflat):
        Cr = cflat.reshape(3, Ng, Ng, Ng)
        d = curl_fft(Cr) - f
        E = np.sum(Cr ** 2 + kap * d ** 2) * h ** 3
        gr = 2 * Cr + 2 * kap * curl_fft(d)          # curl is self-adjoint on periodic grid
        return E, gr.ravel() * h ** 3
    sol = optimize.minimize(E_and_grad, np.zeros(3 * Ng ** 3), jac=True, method='L-BFGS-B',
                            options={'maxiter': 5000, 'gtol': 1e-12, 'ftol': 1e-15})
    fk2 = np.sum(np.abs(np.fft.fftn(f, axes=(1, 2, 3))) ** 2, axis=0)
    E_th = np.sum(kap / (1 + K2 * lam ** 2) * fk2) * h ** 3 / Ng ** 3
    print(f"  lam = {lam:3.1f}: numerical min E = {sol.fun:.8f}   kernel formula = {E_th:.8f}   rel diff {abs(sol.fun - E_th) / E_th:.1e}")
print("  => texture scale >> lam: +kappa |curl a|^2 = +K_s lam^2 |curl a|^2 (the BFN Faddeev term, sign +);")
print("     texture scale << lam: kernel -> K_s/k^2, i.e. it degrades to a 2-derivative-like cost.")

# =============================================================================== 3
hdr("3. Net local quartic: EM (+K_s lam^2 |curl a|^2) vs density (-(xi^2/2) K_s W^2)")
print("  F^2 projection: c_F,net = K_s (lam^2 - xi^2/4).   Standard-map Derrick coefficient (both integrals")
print("  = 8 pi^2 for the standard map): E = 8pi^2 K_s [L + (lam^2 - xi^2/2)/L].")
for lx in (0.1, 0.25, 0.5, 0.7071, 1.0, 2.0, 5.0):
    lam = lx * XI
    print(f"   lam/xi = {lx:6.4f} (lam = {lam:6.3f} a = {lam / R:6.2f} R):  c_F,net/K_s = {lam ** 2 - XI ** 2 / 4:+8.3f} a^2;"
          f"  Derrick coeff = {lam ** 2 - XI ** 2 / 2:+8.3f} a^2")
print("  Local stabilisation needs lam > xi/sqrt2 = %.3f a = %.2f R (F^2 projection alone: lam > xi/2)." % (XI / np.sqrt(2), XI / np.sqrt(2) / R))
print("  The sign is decided by the bought coupling (lam ~ 1/q sqrt(mu)), not by corpus quantities.")

# =============================================================================== 4
hdr("4. Size scan with the full non-local kernels (scaled standard Hopf map)")
# spectra of f_1 = curl a and W_1 = 1/4 |dn|^2 for L = 1, computed once by FFT
r2 = X ** 2 + Y ** 2 + Z ** 2
pH = [2 * X / (1 + r2), 2 * Y / (1 + r2), 2 * Z / (1 + r2), (r2 - 1) / (1 + r2)]
duH = [[sp.diff(c, v) for c in pH] for v in XYZ]
dduH = [[[sp.diff(c, v, w) for c in pH] for w in XYZ] for v in XYZ]
fu = sp.lambdify(XYZ, pH, 'numpy'); fdu = sp.lambdify(XYZ, duH, 'numpy'); fddu = sp.lambdify(XYZ, dduH, 'numpy')
N, Lbox = 128, 24.0
hh = Lbox / N
xs = (np.arange(N) - N // 2) * hh
G = np.stack(np.meshgrid(xs, xs, xs, indexing='ij'), axis=-1).reshape(-1, 3)
npt = len(G)
U = leaf(fu(*G.T), npt); dU = leaf(fdu(*G.T), npt); ddU = leaf(fddu(*G.T), npt)
u1, u2, u3, u4 = U
def dn_of(Uu, dUu):
    a1, a2, a3, a4 = Uu; b1, b2, b3, b4 = dUu
    return np.array([2 * (b1 * a3 + a1 * b3 + b2 * a4 + a2 * b4), 2 * (b1 * a4 + a1 * b4 - b2 * a3 - a2 * b3),
                     2 * (a1 * b1 + a2 * b2 - a3 * b3 - a4 * b4)])
dn = np.array([dn_of(U, dU[i]) for i in range(3)])
W1 = 0.25 * np.sum(dn ** 2, axis=(0, 1))
da = np.zeros((3, 3, npt))
for i in range(3):
    for j in range(3):
        da[i, j] = (dU[i][0] * dU[j][1] + u1 * ddU[i][j][1] - dU[i][1] * dU[j][0] - u2 * ddU[i][j][0]
                    + dU[i][2] * dU[j][3] + u3 * ddU[i][j][3] - dU[i][3] * dU[j][2] - u4 * ddU[i][j][2])
f1 = np.array([da[1, 2] - da[2, 1], da[2, 0] - da[0, 2], da[0, 1] - da[1, 0]])
del dU, ddU, da
print(f"  grid {N}^3, box {Lbox} L:  int W1 = {np.sum(W1) * hh ** 3:.3f} (8pi^2 = {8 * np.pi ** 2:.3f}),"
      f"  int W1^2 = {np.sum(W1 ** 2) * hh ** 3:.3f},  int |f1|^2 = {np.sum(f1 ** 2) * hh ** 3:.3f}")
Wmax = W1.max()
kk = 2 * np.pi * np.fft.fftfreq(N, d=hh)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij'); K2 = (KX ** 2 + KY ** 2 + KZ ** 2).ravel()
Sf = np.sum(np.abs(np.fft.fftn(f1.reshape(3, N, N, N), axes=(1, 2, 3))) ** 2, axis=0).ravel() * hh ** 3 / N ** 3
SW = (np.abs(np.fft.fftn(W1.reshape(N, N, N))) ** 2).ravel() * hh ** 3 / N ** 3
print(f"  k=0 component of f1 (should vanish, int f dV = 0): |S_f(0)|/sum S_f = {Sf[K2 == 0][0] / Sf.sum():.2e} -> set to 0 (IR artefact)")
Sf[K2 == 0] = 0.0
del f1
def E_of_L(Lx, lam, xi=XI, density=True):
    em = np.sum(lam ** 2 / (1 + K2 * lam ** 2 / Lx ** 2) * Sf) / Lx
    den = np.sum((xi ** 2 / 2) * 2 / (K2 * xi ** 2 / Lx ** 2 + 2) * SW) / Lx if density else 0.0
    return 8 * np.pi ** 2 * Lx + em - den
Ls = np.geomspace(0.02, 200, 400)
print(f"  max of (1/4)|dn|^2 for L = 1: {Wmax:.4f}  -> condensate survives the core only if L > xi sqrt(Wmax) = "
      f"{XI * np.sqrt(Wmax):.3f} a = {XI * np.sqrt(Wmax) / R:.2f} R")
print("   lam/xi    E(L) has a local minimum?   L*/a     L*/R    W~max(L*)   fits in sphere (L* <~ R)?")
for lx in (0.1, 0.5, 0.7071, 1.0, 2.0, 5.0, 20.0):
    lam = lx * XI
    E = np.array([E_of_L(Lx, lam) for Lx in Ls])
    E0 = np.array([E_of_L(Lx, lam, density=False) for Lx in Ls])
    idx = [i for i in range(1, len(Ls) - 1) if E[i] < E[i - 1] and E[i] < E[i + 1]]
    idx0 = [i for i in range(1, len(Ls) - 1) if E0[i] < E0[i - 1] and E0[i] < E0[i + 1]]
    if idx0:
        i0 = idx0[0]
        print(f"   [density frozen: METASTABLE local min at L* = {Ls[i0]:.2f} a = {Ls[i0] / R:.1f} R = {Ls[i0] / lam:.2f} lam, "
              f"E* = {E0[i0]:.1f} K_s > E(L->0) = {E0[0]:.3f} K_s; W~max(L*) = {XI ** 2 * Wmax / Ls[i0] ** 2:.3f}]")
    else:
        print(f"   [density frozen: no local minimum; E(L=0.02a)/E(L=200a) = {E0[0] / E0[-1]:.2e}]")
    if idx:
        i = idx[0]
        Ls_ = Ls[i]
        print(f"   {lx:6.3f}       yes                    {Ls_:8.3f}  {Ls_ / R:7.2f}   {XI ** 2 * Wmax / Ls_ ** 2:8.3f}      {'yes' if Ls_ <= R else 'NO'}")
    else:
        print(f"   {lx:6.3f}       no (collapses)          --        --        --          --")
# diagnostics: large-L limit vs the local formula, and the small-L behaviour
for lx in (1.0, 5.0):
    lam = lx * XI
    for Lx in (1000.0 * lam, 0.3 * lam, 0.03 * lam, 0.003 * lam):
        loc = 8 * np.pi ** 2 * (Lx + (lam ** 2 - XI ** 2 / 2) / Lx)
        print(f"     lam/xi={lx}: L/lam = {Lx / lam:8.3f}  E(L)/K_s = {E_of_L(Lx, lam):12.4f}  [density frozen: "
              f"{E_of_L(Lx, lam, density=False):12.4f}]   local formula {loc:12.4f}")
print("  With the density frozen (no negative term at all), E(L) -> 0 linearly as L -> 0: below lam the field")
print("  penetrates, the supercurrent C cancels the twist cost, and the 'Faddeev' energy degrades to ~L.")
print("  With the density kernel included E(L) even goes negative at small L; that is the linear kernel")
print("  overshooting where W~ >> 1 (the physical floor is the normal state).")
print("  Either way E(L) -> 0 along the family: the H = 1 sector has infimum 0, so there is no stable knot at")
print("  any lam (agrees with Speight, J. Geom. Phys. 60, 599 (2010) and Jaykka-Speight, PRD 84, 125035 (2011):")
print("  restoring the supercurrent coupling makes BFN knots shrink and disappear).")
print("  W~max = xi^2 max(1/4|dn|^2): values > 1 mean the linear density kernel is outside its range and the")
print("  condensate is locally destroyed (Q1-F1).")

# =============================================================================== 5
hdr("5. Axis alignment: easy-axis / Zeeman potential, or pinning n = z on every shell")
print("  (i) A potential D(1 - n_z^2) or h(1 - n_z) has no derivatives: it adds nothing to c_F and scales as")
print("      L^3 under x -> x/L, so it cannot stop Derrick collapse; it only caps the knot size from above.")
print("      It gaps the magnon (omega = eps_k + 2D/hbar-type gap): still no photon-like mode.")
print("  (ii) Pinning n = z on each shell is the Q4(iv) grip term: it makes H well-defined per sphere,")
print("      but does not touch c_F, the slaving of a, or the Higgs mass.")
# (iii) aligned knots carry no macroscopic twist field: int f dV = 0 per sphere (div f = 0, f.n = 0 on the wall)
rr = sp.sqrt(r2)
gpin = sp.pi * (1 - rr / R)
up = [sp.sin(gpin) * X / rr, sp.sin(gpin) * Y / rr, sp.sin(gpin) * Z / rr, sp.cos(gpin)]
dup = [[sp.diff(c, v) for c in up] for v in XYZ]
ddup = [[[sp.diff(c, v, w) for c in up] for w in XYZ] for v in XYZ]
fU = sp.lambdify(XYZ, up, 'numpy'); fdU = sp.lambdify(XYZ, dup, 'numpy'); fddU = sp.lambdify(XYZ, ddup, 'numpy')
rg, rw = np.polynomial.legendre.leggauss(60); rq = (rg + 1) * R / 2; rw = rw * R / 2
cg, cw = np.polynomial.legendre.leggauss(40); phg = (np.arange(40) + 0.5) * 2 * np.pi / 40
Rr, Cc, PH = np.meshgrid(rq, cg, phg, indexing='ij')
Wq = (rw[:, None, None] * cw[None, :, None] * (2 * np.pi / 40)) * Rr ** 2
Ss = np.sqrt(1 - Cc ** 2)
Pq = np.stack([Rr * Ss * np.cos(PH), Rr * Ss * np.sin(PH), Rr * Cc], axis=-1).reshape(-1, 3); Wq = Wq.ravel()
n_ = len(Wq)
U = leaf(fU(*Pq.T), n_); dU = leaf(fdU(*Pq.T), n_); ddU = leaf(fddU(*Pq.T), n_)
u1, u2, u3, u4 = U
da = np.zeros((3, 3, n_))
for i in range(3):
    for j in range(3):
        da[i, j] = (dU[i][0] * dU[j][1] + u1 * ddU[i][j][1] - dU[i][1] * dU[j][0] - u2 * ddU[i][j][0]
                    + dU[i][2] * dU[j][3] + u3 * ddU[i][j][3] - dU[i][3] * dU[j][2] - u4 * ddU[i][j][2])
fb = np.array([da[1, 2] - da[2, 1], da[2, 0] - da[0, 2], da[0, 1] - da[1, 0]])
net = np.array([np.sum(fb[k] * Wq) for k in range(3)])
tot = np.sum(np.sqrt(np.sum(fb ** 2, axis=0)) * Wq)
print(f"  (iii) pinned Hopf-1 knot in one sphere: |int f dV| / int |f| dV = {np.linalg.norm(net) / tot:.2e}")
print("      Each knot's twist field integrates to zero over its sphere, so aligning every knot along one")
print("      axis gives no macroscopic twist field and no long-range mode; aligning the knot axes in space")
print("      is a vector (T1u-type) order -> lattice anisotropy (Gate PROMOTE, CN-PROMOTE-02).")

hdr("POST-BLIND Q1 SUMMARY (inputs: EM = charge q + Maxwell mu; AXIS = D or grip)")
print("  (a) identity unchanged (gauge-covariant form verified).")
print("  (b) a still slaved (curl a = f[n]); the new independent field A is London-screened (massive).")
print("  (c) c_F > 0 is now generated (+K_s lam^2), but the net sign needs lam > xi/sqrt2 (Derrick, standard map),")
print("      i.e. it is set by the bought coupling; alignment adds nothing to c_F.")
print("  No stable knot exists at any lam once the supercurrent relaxes (part 4); and any knot whose core keeps")
print("  its superfluid must be larger than xi*sqrt(8) = 13 sphere radii.")
print("  Q1 under these inputs: BOUGHT for c_F > 0 (coupling-dependent); the twist field itself still has no")
print("  independent propagating DOF. The downstream Q2 kill (Higgs mass) is untouched.")
