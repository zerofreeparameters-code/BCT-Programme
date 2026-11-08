#!/usr/bin/env python3
"""
Gate TWIST -- Q1: does the twist field a = -i chi^dag grad chi get its own Maxwell-type
energy from the medium V0?

Model (card section 4, fixed):
  F = int [ (hbar^2/2m)|grad Psi|^2 + (g/2)(|Psi|^2 - n0)^2 ] d^3r,  Psi in C^2,
  Psi = sqrt(rho) chi, |chi| = 1, n = chi^dag sigma chi, a = -i chi^dag grad chi.
  Healing-length convention (declared): xi^2 = hbar^2/(2 m g n0)  [corpus App AZ6 form,
  quoted in Gate C1 RESULT l.255-260; App J eq.(1) has the same dimensionless form].
  xi = a_lat/sqrt(8 pi alpha0) = 2.31754 a_lat, used as given (CN-C1-04).

Parts
  A  identity |grad chi|^2 = 1/4 |grad n|^2 + a^2 on random smooth fields (exact derivatives)
  B  Mermin-Ho with its exact coefficient; F_ij F_ij = 8|curl a|^2;
     ((dn)^2)^2 = F_ij F_ij + (d_i n . d_j n)^2
  C  gauge decomposition |grad Psi|^2 = (grad sqrt rho)^2 + rho[1/4|grad n|^2 + (grad phi + a_zeta)^2]
  D  Hopf-number normalisation H = (1/4 pi^2) int a.(curl a) on the standard Hopf map
  E  Bogoliubov spectrum of V0 (C^2): mode count -> does a carry its own DOF?
  F  density integrated out: tree level (exact local + gradient kernel), one loop, sign theorem
  G  Derrick scaling with the induced quartic

Run:  python3 -I twist_q1_twistfield.py
"""
import numpy as np
import sympy as sp
from scipy import integrate, optimize

rng = np.random.default_rng(20261108)
X, Y, Z = sp.symbols('x y z', real=True)
XYZ = (X, Y, Z)

ALPHA0 = (np.sqrt(2) - 1) / 2 * (np.sqrt(6) - 2) / 4 / np.pi   # r_oct r_tet / pi
XI = 1.0 / np.sqrt(8 * np.pi * ALPHA0)                           # in units of a_lat

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# ---------------------------------------------------------------- field machinery
def random_trig(nterms=4):
    expr = sp.Float(rng.normal())
    for _ in range(nterms):
        k = rng.normal(size=3)
        ph = rng.uniform(0, 2 * np.pi)
        c = rng.normal()
        expr += sp.Float(c) * sp.sin(sp.Float(k[0]) * X + sp.Float(k[1]) * Y + sp.Float(k[2]) * Z + sp.Float(ph))
    return expr

def build_u(p):
    """p: list of 4 real sympy expressions (Re z1, Im z1, Re z2, Im z2). Returns lambdified
    u, du (3x4), ddu (3x3x4) for the unit 4-vector u = p/|p|."""
    N = sp.sqrt(sum(pi ** 2 for pi in p))
    u = [pi / N for pi in p]
    du = [[sp.diff(uc, v) for uc in u] for v in XYZ]
    ddu = [[[sp.diff(uc, v, w) for uc in u] for w in XYZ] for v in XYZ]
    f_u = sp.lambdify(XYZ, u, 'numpy')
    f_du = sp.lambdify(XYZ, du, 'numpy')
    f_ddu = sp.lambdify(XYZ, ddu, 'numpy')
    return f_u, f_du, f_ddu

def as_arr(val, npts):
    """lambdify returns nested lists whose leaves may be scalars; make every leaf shape (npts,)."""
    if isinstance(val, (list, tuple)):
        return np.array([as_arr(v, npts) for v in val])
    return np.asarray(val, dtype=float) * np.ones(npts)

def fields(f_u, f_du, f_ddu, P):
    x, y, z = P.T
    n = len(x)
    u = as_arr(f_u(x, y, z), n)            # (4,n)
    du = as_arr(f_du(x, y, z), n)          # (3,4,n)
    ddu = as_arr(f_ddu(x, y, z), n)        # (3,3,4,n)
    u1, u2, u3, u4 = u
    # n vector and its gradient
    def nvec(U):
        a1, a2, a3, a4 = U
        return np.array([2 * (a1 * a3 + a2 * a4), 2 * (a1 * a4 - a2 * a3), a1 ** 2 + a2 ** 2 - a3 ** 2 - a4 ** 2])
    nv = nvec(u)
    # d_i n is bilinear: d(n) = J(u) du
    def dn_of(U, dU):
        a1, a2, a3, a4 = U
        b1, b2, b3, b4 = dU
        return np.array([2 * (b1 * a3 + a1 * b3 + b2 * a4 + a2 * b4),
                         2 * (b1 * a4 + a1 * b4 - b2 * a3 - a2 * b3),
                         2 * (a1 * b1 + a2 * b2 - a3 * b3 - a4 * b4)])
    dn = np.array([dn_of(u, du[i]) for i in range(3)])        # (3 dirs, 3 comps, n)
    # connection a_i = Im(chi^dag d_i chi) = u1 d u2 - u2 d u1 + u3 d u4 - u4 d u3
    a = np.array([u1 * du[i][1] - u2 * du[i][0] + u3 * du[i][3] - u4 * du[i][2] for i in range(3)])
    # Re(chi^dag d chi) = u.du must vanish
    re_part = np.array([np.sum(u * du[i], axis=0) for i in range(3)])
    # d_i a_j
    da = np.zeros((3, 3, n))
    for i in range(3):
        for j in range(3):
            da[i, j] = (du[i][0] * du[j][1] + u1 * ddu[i][j][1] - du[i][1] * du[j][0] - u2 * ddu[i][j][0]
                        + du[i][2] * du[j][3] + u3 * ddu[i][j][3] - du[i][3] * du[j][2] - u4 * ddu[i][j][2])
    grad_chi_sq = np.sum(du ** 2, axis=(0, 1))
    return dict(u=u, du=du, n=nv, dn=dn, a=a, da=da, re=re_part, gchi2=grad_chi_sq)

# =============================================================================== A
hdr("A. Identity |grad chi|^2 = 1/4 |grad n|^2 + a^2   (random smooth fields, exact derivatives)")
worst_A = 0.0
worst_re = 0.0
for trial in range(5):
    p = [random_trig() + (2.0 if c == 0 else 0.0) for c in range(4)]
    f_u, f_du, f_ddu = build_u(p)
    P = rng.uniform(-3, 3, size=(2000, 3))
    F = fields(f_u, f_du, f_ddu, P)
    lhs = F['gchi2']
    rhs = 0.25 * np.sum(F['dn'] ** 2, axis=(0, 1)) + np.sum(F['a'] ** 2, axis=0)
    rel = np.max(np.abs(lhs - rhs) / np.maximum(1e-300, np.abs(lhs)))
    worst_A = max(worst_A, rel)
    worst_re = max(worst_re, np.max(np.abs(F['re'])))
    print(f"  trial {trial}: max relative residual = {rel:.3e}   max|Re chi^dag d chi| = {np.max(np.abs(F['re'])):.3e}")
print(f"  WORST over 5 x 2000 points: {worst_A:.3e}   (card threshold 1e-10)  ->  {'PASS' if worst_A < 1e-10 else 'FAIL'}")

# =============================================================================== B
hdr("B. Mermin-Ho coefficient and the Faddeev/Maxwell identities")
eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
    eps[i, j, k] = s
worst = dict(MH=0.0, curl=0.0, F2=0.0, quart=0.0)
for trial in range(5):
    p = [random_trig() + (2.0 if c == 0 else 0.0) for c in range(4)]
    f_u, f_du, f_ddu = build_u(p)
    P = rng.uniform(-3, 3, size=(1500, 3))
    F = fields(f_u, f_du, f_ddu, P)
    dn, n, da = F['dn'], F['n'], F['da']
    # F_ij = n . (d_i n x d_j n)
    Fij = np.zeros((3, 3, P.shape[0]))
    for i in range(3):
        for j in range(3):
            Fij[i, j] = np.sum(n * np.cross(dn[i], dn[j], axis=0), axis=0)
    fij = da.transpose(1, 0, 2) - da            # f_ij = d_i a_j - d_j a_i ; da[i,j]=d_i a_j
    fij = np.array([[da[i, j] - da[j, i] for j in range(3)] for i in range(3)])
    scale = np.max(np.abs(Fij)) + 1e-300
    worst['MH'] = max(worst['MH'], np.max(np.abs(fij - 0.5 * Fij)) / scale)
    curl_a = np.array([sum(eps[k, i, j] * da[i, j] for i in range(3) for j in range(3)) for k in range(3)])
    mh_vec = np.array([0.25 * sum(eps[k, i, j] * Fij[i, j] for i in range(3) for j in range(3)) for k in range(3)])
    worst['curl'] = max(worst['curl'], np.max(np.abs(curl_a - mh_vec)) / scale)
    FF = np.sum(Fij ** 2, axis=(0, 1))
    worst['F2'] = max(worst['F2'], np.max(np.abs(FF - 8 * np.sum(curl_a ** 2, axis=0)) / (np.max(FF) + 1e-300)))
    dn2 = np.sum(dn ** 2, axis=(0, 1))
    dij = np.einsum('icn,jcn->ijn', dn, dn)
    quart_res = dn2 ** 2 - (FF + np.sum(dij ** 2, axis=(0, 1)))
    worst['quart'] = max(worst['quart'], np.max(np.abs(quart_res)) / np.max(dn2 ** 2))
print(f"  f_ij = d_i a_j - d_j a_i  vs  (1/2) n.(d_i n x d_j n):          max rel resid {worst['MH']:.3e}")
print(f"  (curl a)_k  vs  (1/4) eps_kij n.(d_i n x d_j n):                max rel resid {worst['curl']:.3e}")
print(f"  F_ij F_ij  vs  8 |curl a|^2:                                     max rel resid {worst['F2']:.3e}")
print(f"  ((dn)^2)^2  vs  F_ij F_ij + (d_i n . d_j n)^2:                   max rel resid {worst['quart']:.3e}")
print("  => precise Mermin-Ho: f_ij = (1/2) n.(d_i n x d_j n); the card's 'curl a = 1/2 n.(dn x dn)'")
print("     is shorthand for the 2-form statement (vector form carries 1/4 eps_kij).")

# =============================================================================== C
hdr("C. Gauge decomposition: a enters V0 only through v = grad(phi) + a_zeta")
# chi = e^{i phi} zeta ; check grad chi^2 = 1/4 |dn|^2 + (dphi + a_zeta)^2 and the full |grad Psi|^2
p = [random_trig() + (2.0 if c == 0 else 0.0) for c in range(4)]
phi = random_trig()
rho = sp.exp(sp.Float(0.3) * random_trig())   # positive smooth density
zeta1 = (p[0] + sp.I * p[1]) / sp.sqrt(sum(q ** 2 for q in p))
zeta2 = (p[2] + sp.I * p[3]) / sp.sqrt(sum(q ** 2 for q in p))
Psi1 = sp.sqrt(rho) * sp.exp(sp.I * phi) * zeta1
Psi2 = sp.sqrt(rho) * sp.exp(sp.I * phi) * zeta2
gradPsi2 = sum(sp.Abs(sp.diff(Psi1, v)) ** 2 + sp.Abs(sp.diff(Psi2, v)) ** 2 for v in XYZ)
f_gP = sp.lambdify(XYZ, gradPsi2, 'numpy')
f_u, f_du, f_ddu = build_u(p)
f_rho = sp.lambdify(XYZ, rho, 'numpy')
f_grho = sp.lambdify(XYZ, [sp.diff(sp.sqrt(rho), v) for v in XYZ], 'numpy')
f_gphi = sp.lambdify(XYZ, [sp.diff(phi, v) for v in XYZ], 'numpy')
P = rng.uniform(-2, 2, size=(800, 3))
F = fields(f_u, f_du, f_ddu, P)
x, y, z = P.T
lhs = np.real(f_gP(x, y, z))
grho = as_arr(f_grho(x, y, z), len(x)); gphi = as_arr(f_gphi(x, y, z), len(x))
r = f_rho(x, y, z)
v = gphi + F['a']
rhs = np.sum(grho ** 2, axis=0) + r * (0.25 * np.sum(F['dn'] ** 2, axis=(0, 1)) + np.sum(v ** 2, axis=0))
print(f"  |grad Psi|^2 vs (grad sqrt rho)^2 + rho[1/4|dn|^2 + (grad phi + a_zeta)^2]: max rel resid "
      f"{np.max(np.abs(lhs - rhs) / lhs):.3e}")
print("  Gauge check: under zeta -> e^{i lam} zeta, phi -> phi - lam: n and v invariant, a_zeta -> a_zeta + grad lam.")
print("  => V0 depends on a only via v (superflow) and on curl a only via n (Mermin-Ho identity).")
print("     Field content (rho, phi, n) = 1+1+2 = 4 real = C^2. a adds no variable: it is slaved.")

# =============================================================================== D
hdr("D. Hopf normalisation H = (1/4 pi^2) int a.(curl a) on the standard Hopf map")
r2 = X ** 2 + Y ** 2 + Z ** 2
pH = [2 * X / (1 + r2), 2 * Y / (1 + r2), 2 * Z / (1 + r2), (r2 - 1) / (1 + r2)]
f_u, f_du, f_ddu = build_u(pH)
# Gauss-Legendre in (t, cos th, ph), r = tan(t)
nt, nc, nphi = 120, 60, 48
tg, tw = np.polynomial.legendre.leggauss(nt); t = (tg + 1) * (np.pi / 4); tw = tw * np.pi / 4
cg, cw = np.polynomial.legendre.leggauss(nc)
phg = np.arange(nphi) * 2 * np.pi / nphi; phw = np.full(nphi, 2 * np.pi / nphi)
T, C, PH = np.meshgrid(t, cg, phg, indexing='ij')
W = (tw[:, None, None] * cw[None, :, None] * phw[None, None, :])
Rr = np.tan(T); jac = Rr ** 2 / np.cos(T) ** 2
S = np.sqrt(1 - C ** 2)
P = np.stack([Rr * S * np.cos(PH), Rr * S * np.sin(PH), Rr * C], axis=-1).reshape(-1, 3)
F = fields(f_u, f_du, f_ddu, P)
curl_a = np.array([sum(eps[k, i, j] * F['da'][i, j] for i in range(3) for j in range(3)) for k in range(3)])
wts = (W * jac).ravel()
Hval = np.sum(np.sum(F['a'] * curl_a, axis=0) * wts) / (4 * np.pi ** 2)
E2_std = np.sum(0.25 * np.sum(F['dn'] ** 2, axis=(0, 1)) * wts)
dn2 = np.sum(F['dn'] ** 2, axis=(0, 1))
Q4_std = np.sum((0.25 * dn2) ** 2 * wts)
curl2_std = np.sum(np.sum(curl_a ** 2, axis=0) * wts)
print(f"  H (standard Hopf map, scale L=1) = {Hval:.8f}   -> |H| = 1 to {abs(abs(Hval) - 1):.1e}")
print(f"  int (1/4)|dn|^2 d^3x            = {E2_std:.6f}  = {E2_std / np.pi ** 2:.6f} pi^2   (times L)")
print(f"  int [(1/4)|dn|^2]^2 d^3x        = {Q4_std:.6f}                     (times 1/L)")
print(f"  int |curl a|^2 d^3x             = {curl2_std:.6f}                     (times 1/L)")
print("  Consistency with App JH eq.(hopf-invariant): pullback area form A = 2a, so 1/(16pi^2) int A dA = 1/(4pi^2) int a da.")

# =============================================================================== E
hdr("E. Bogoliubov spectrum of V0 with Psi in C^2  (does a carry its own propagating DOF?)")
# units hbar = 1, 2m = 1 (so hbar^2/2m = 1), g n0 = 1 -> xi = 1. 1-D periodic grid, numeric Hessian.
Ng, Lbox = 64, 40.0
h = Lbox / Ng
def energy_grad(vars4):
    x1, y1, x2, y2 = vars4.reshape(4, Ng)
    lap = lambda f: (np.roll(f, -1) - 2 * f + np.roll(f, 1)) / h ** 2
    dens = x1 ** 2 + y1 ** 2 + x2 ** 2 + y2 ** 2
    # E = sum h [ |grad psi|^2 + 1/2 (|psi|^2 - 1)^2 ]  with psi = x + i y
    g = []
    for f in (x1, y1, x2, y2):
        g.append(h * (-2 * lap(f) + 2 * (dens - 1) * f))
    return np.concatenate(g)
v0 = np.concatenate([np.ones(Ng), np.zeros(Ng), np.zeros(Ng), np.zeros(Ng)])
Hs = np.zeros((4 * Ng, 4 * Ng)); dlt = 1e-6
for i in range(4 * Ng):
    e = np.zeros(4 * Ng); e[i] = dlt
    Hs[:, i] = (energy_grad(v0 + e) - energy_grad(v0 - e)) / (2 * dlt)
Hs = 0.5 * (Hs + Hs.T) / h            # Hessian per unit length (density form)
# dynamics: hbar dx/dt = 1/2 dE/dy, hbar dy/dt = -1/2 dE/dx  (psi = x+iy, i dpsi/dt = dE/dpsi*)
Jm = np.zeros_like(Hs)
for c in (0, 2):
    I = np.eye(Ng)
    Jm[c * Ng:(c + 1) * Ng, (c + 1) * Ng:(c + 2) * Ng] = 0.5 * I
    Jm[(c + 1) * Ng:(c + 2) * Ng, c * Ng:(c + 1) * Ng] = -0.5 * I
ev = np.linalg.eigvals(Jm @ Hs)
om = np.sort(np.abs(ev.imag[ev.imag > 1e-9]))
k = 2 * np.pi * np.arange(Ng) / Lbox
eps_k = (4 / h ** 2) * np.sin(k * h / 2) ** 2            # lattice hbar^2 k^2/2m
pred = np.sort(np.concatenate([np.sqrt(eps_k * (eps_k + 2)), eps_k])[1:])  # drop k=0 Goldstones
pred = pred[pred > 1e-9]
# compare multiset (each nonzero k appears twice: +k and -k)
pred_full = np.sort(np.concatenate([np.sqrt(eps_k[1:] * (eps_k[1:] + 2)), eps_k[1:]]))
om_nz = om[om > 1e-3]          # drop the k=0 Goldstone/zero-mode block (numerically split ~1e-5)
mismatch = np.max(np.abs(np.sort(om_nz) - pred_full)) if len(om_nz) == len(pred_full) else np.nan
print(f"  nonzero positive-frequency modes: {len(om_nz)}  (expected 2 x {Ng-1} = {2*(Ng-1)}; k=0 block = zero modes)")
print(f"  branch 1 (density/phase, Bogoliubov): omega = sqrt(eps(eps+2gn0)) -> c_s k at small k")
print(f"  branch 2 (n-texture / magnon):        omega = eps_k = hbar k^2/2m (quadratic, no gap)")
print(f"  max |numeric - analytic| over all modes: {mismatch:.2e}")
print("  => 2 modes per k for C^2 (phonon + quadratic magnon). No third branch, no linear transverse")
print("     doublet: the twist connection a has no propagating degrees of freedom of its own.")

# =============================================================================== F
hdr("F. Integrating out the density: sign and size of the induced (curl a)^2 coefficient c_F")
print("  Units: energy density / (g n0^2), length / xi, W~ = xi^2 W, W = 1/4|dn|^2 + v^2 >= 0.")
print("  Reduced functional: f = (grad s)^2 + W~ s^2 + 1/2 (s^2 - 1)^2,  s = sqrt(rho/n0).")
print("  Tree level (bare V0): no (curl a)^2 term appears anywhere -> c_F(tree) = 0 exactly.")
# F1 exact local minimisation
Wg = np.linspace(0, 1.6, 17)
fmin = np.array([optimize.minimize_scalar(lambda s: w * s * s + 0.5 * (s * s - 1) ** 2, bounds=(0, 2), method='bounded',
                                          options={'xatol': 1e-12}).fun for w in Wg])
fan = np.where(Wg < 1, Wg - Wg ** 2 / 2, 0.5)
print(f"  F1 local elimination: min_s f = W - W^2/2 (W<1), 1/2 (W>=1);  max |num - formula| = {np.max(np.abs(fmin - fan)):.2e}")
print("     -> induced quartic -(1/2)W~^2, i.e. dimensionful  -(xi^2/2) K_s W^2,  K_s = (hbar^2/2m) n0.")
print("     -> at W~ >= 1 the condensate is destroyed locally (s = 0): texture energy saturates.")
# F2 gradient kernel by direct 1-D solve
def solve_1d(W0, W1, q, N=512):
    L = 2 * np.pi / q
    x = np.arange(N) * L / N
    Wx = W0 + W1 * np.cos(q * x)
    kk = 2 * np.pi * np.fft.fftfreq(N, d=L / N)
    s = np.sqrt(np.clip(1 - Wx, 0.05, None))
    Mpre = 4.0
    for it in range(4000):
        rhs = Mpre * s - (Wx * s + (s ** 2 - 1) * s)
        s_new = np.real(np.fft.ifft(np.fft.fft(rhs) / (kk ** 2 + Mpre)))
        if np.max(np.abs(s_new - s)) < 1e-14:
            s = s_new; break
        s = s_new
    ds = np.real(np.fft.ifft(1j * kk * np.fft.fft(s)))
    e = np.mean(ds ** 2 + Wx * s ** 2 + 0.5 * (s ** 2 - 1) ** 2)
    return e
W0, W1 = 0.2, 0.02
s0sq = 1 - W0
print("  F2 gradient kernel (W~ = W0 + W1 cos qx, exact 1-D solve vs 2nd-order formula):")
print("       q*xi     dE(num)        dE(formula)= -s0^2 W1^2 / (2(q^2+2 s0^2))")
for q in (0.05, 0.3, 1.0, 2.0, 4.0):
    e_num = solve_1d(W0, W1, q) - (W0 - W0 ** 2 / 2)
    e_th = -s0sq * W1 ** 2 / (2 * (q ** 2 + 2 * s0sq))
    print(f"      {q:5.2f}   {e_num:+.6e}   {e_th:+.6e}")
print("     kernel C(q) = 2 s0^2/(q^2 + 2 s0^2) > 0, decreasing: 4-derivative term -C(0)W^2 < 0;")
print("     next order +(xi^2/4)(grad W)^2 > 0 is 6-derivative and appears only where the gradient")
print("     expansion has broken down (texture scale ~ xi), so it gives no controlled stabilisation.")
# F3 one loop
I2_num = integrate.quad(lambda kk: kk ** 2 / (kk ** 2 + 2) ** 2, 0, np.inf)[0] / (2 * np.pi ** 2)
I2_th = 1 / (8 * np.pi * np.sqrt(2))
print(f"  F3 one loop (Gaussian amplitude fluctuations about the saddle, M^2 = 2 - 2W~):")
print(f"     I2 = int d^3k/(2pi)^3 (k^2+2)^-2 = {I2_num:.10f}  (analytic 1/(8 pi sqrt2) = {I2_th:.10f})")
print(f"     one-loop W~^2 coefficient = -t I2 = -{I2_th:.6f} t  (t = T/(g n0^2 xi^3)); tree = -0.5")
print("     same sign as tree; the 1-loop/tree ratio is 2 t I2 = t/(4 sqrt2 pi).")
# concavity
def g1(Wt, Lam=50.0):
    return integrate.quad(lambda kk: kk ** 2 * 0.5 * (np.log(kk ** 2 + 2 - 2 * Wt) - np.log(kk ** 2 + 2)), 0, Lam, limit=200)[0] / (2 * np.pi ** 2)
hW = 1e-3
for Wt in (0.0, 0.2, 0.5):
    sec = (g1(Wt + hW) - 2 * g1(Wt) + g1(Wt - hW)) / hW ** 2
    print(f"     d^2/dW~^2 of the 1-loop term at W~={Wt}: {sec:+.5f}  (analytic -2 int (k^2+2-2W~)^-2 = "
          f"{-2 * integrate.quad(lambda kk: kk**2/(kk**2+2-2*Wt)**2,0,50.0)[0]/(2*np.pi**2):+.5f}, same cutoff 50/xi)")
print("  F4 sign theorem (all orders): W enters the density sector linearly (int rho W), so the ground-state")
print("     energy E0[W] = min_state <H0 + int rho W> is a minimum of affine functionals -> concave in W.")
print("     Its W-W kernel is minus a (positive) density-density response: no positive W^2 at any order.")
cF = -XI ** 2 / 4
print(f"  F5 projection onto the Faddeev/Maxwell structure. Using ((dn)^2)^2 = F_ijF_ij + (d_i n.d_j n)^2 and")
print(f"     F_ijF_ij = 8|curl a|^2 (part B):  -(xi^2/2)K_s W^2  contains  -(xi^2/4) K_s |curl a|^2 + (other <= 0).")
print(f"     c_F(induced) = -(xi^2/4) K_s = {cF:+.4f} a^2 K_s   (xi = {XI:.5f} a).   SIGN: NEGATIVE.")
print(f"     Pointwise: induced quartic <= c_F |curl a|^2 <= 0 for every configuration.")
print(f"     Scaling: c_F ~ -K_s xi^2 = -K_s a^2/(8 pi alpha0); c_F/(K_s a^2) = {cF:+.4f}.")

# =============================================================================== G
hdr("G. Derrick scaling with the induced quartic (standard Hopf map rescaled by L, units of xi)")
print("     E(L)/(K_s xi) = c2 L/xi - (1/2) c4 xi/L ;  c2 = int 1/4|dn|^2 = %.4f, c4 = int (1/4 |dn|^2)^2 = %.4f" % (E2_std, Q4_std))
for Lx in (2.0, 1.0, 0.5, 0.25, 0.1):
    print(f"       L/xi = {Lx:5.2f}:  E = {E2_std * Lx - 0.5 * Q4_std / Lx:+9.4f}")
print("     Monotone decreasing as L -> 0 (the quartic only accelerates collapse): no stable knot in V0.")
print("     (Below L ~ xi the gradient expansion fails; the true endpoint is a normal core, s -> 0, where")
print("      n is undefined and the Hopf number can unwind.)")

hdr("Q1 SUMMARY")
print("  (a) identity verified to %.1e (threshold 1e-10)." % worst_A)
print("  (b) a enters V0 only through v = grad phi + a; curl a = f[n] identically: a is slaved, 0 own DOF.")
print("  (c) c_F(tree) = 0; c_F(density integrated out) = -(xi^2/4)K_s < 0 at tree level, more negative at")
print("      one loop, and non-positive at all orders (concavity). Score: FAIL (BFN route = BOUGHT).")
