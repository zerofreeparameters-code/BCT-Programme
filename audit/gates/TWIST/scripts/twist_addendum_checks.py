#!/usr/bin/env python3
"""
Gate TWIST -- UNBLINDED ADDENDUM checks (run after the gate, against the 8 Nov desk-checks A-C
and the 8 Nov session record, as recorded in chat accb56de... "Lost physics chat").

1  Desk-check B numbers: spheromak wall pressure at the equator = u_bar/2 exactly? centre/average 4.71?
   inner half-radius ball 36%?
2  Desk-check A numbers: Hopf-1 texture filling the sphere, n-only and full |grad chi|^2, in eps_c l_P^3,
   against the desk's 191-287 and 366-548x.
3  The unwinding barrier: TWIST said "<= u_c V" (bulk only); desk A said ~23 eps_c l_P^3 (bulk + gradient
   on scale R). Settle it with radial minimisations of the corpus functional:
     (a) normal ball: s = 0 inside R, s free outside      -> cost of a fully depleted sphere
     (b) Hopf texture with the density free (radial)        -> what the medium does when it keeps the knot
     (c) Hopf texture at full density                       -> 2 xi^2 int 1/4|dn|^2
4  Impulse of a pinned knot, P = 1/2 int x * f dV  (f = curl a = vorticity of the twist superflow / (hbar/m)):
   is it nonzero? (if so: a knot self-propels, and an aligned array carries net momentum along c)
5  Desk-check C's ring size against xi; the alternating pattern's residual axis (nematic order)
Units: lengths in a = l_P (xi = 2.31754, R = 0.5); energies in eps_c l_P^3, eps_c = g n0^2/2 = u_c,
       energy density = eps_c [ 2 xi^2 ((grad s)^2 + s^2 (1/4)|dn|^2) + (s^2 - 1)^2 ].
Run: python3 -I twist_addendum_checks.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize
from scipy.integrate import dblquad, quad

ROCT = (np.sqrt(2) - 1) / 2; RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi
XI = 1 / np.sqrt(8 * np.pi * ALPHA0)
R = 0.5
V = 4 * np.pi * R ** 3 / 3

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# =============================================================================== 1
hdr("1. Desk-check B (spheromak) numbers, recomputed")
lam = brentq(lambda z: np.sin(z) / z ** 2 - np.cos(z) / z, 4, 5)
j1 = lambda x: np.sin(x) / x ** 2 - np.cos(x) / x
xj1p = lambda x: np.cos(x) / x - np.sin(x) / x ** 2 + np.sin(x)
def B2(r, t):
    q = lam * max(r, 1e-6)
    return (2 * j1(q) / q * np.cos(t)) ** 2 + (xj1p(q) / q * np.sin(t)) ** 2 + (j1(q) * np.sin(t)) ** 2
W = dblquad(lambda t, r: .5 * B2(r, t) * 2 * np.pi * r * r * np.sin(t), 1e-6, 1, 0, np.pi, epsabs=1e-12)[0]
ub = W / (4 / 3 * np.pi)
peq = 0.5 * B2(1.0, np.pi / 2)
pmean = quad(lambda t: 0.5 * B2(1.0, t) * np.sin(t) / 2, 0, np.pi)[0]
cen = 0.5 * B2(1e-6, 0.3)
W5 = dblquad(lambda t, r: .5 * B2(r, t) * 2 * np.pi * r * r * np.sin(t), 1e-6, 0.5, 0, np.pi, epsabs=1e-12)[0]
print(f"  mean wall pressure / u_bar = {pmean / ub:.10f}  (1/3)")
print(f"  equator wall pressure / u_bar = {peq / ub:.10f}  (desk: 1/2; exact because B^2 at the wall ~ sin^2 theta, <sin^2> = 2/3)")
print(f"  centre energy density / u_bar = {cen / ub:.4f} (desk 4.71);  / equator wall value = {cen / peq:.3f} (desk 9.4)")
print(f"  inner half-radius ball holds {100 * W5 / W:.2f}% of the energy (desk 36%)")

# =============================================================================== 2
X, Y, Z = sp.symbols('x y z', real=True); XYZ = (X, Y, Z)
rr = sp.sqrt(X ** 2 + Y ** 2 + Z ** 2)
g = sp.pi * (1 - rr / R)
u = [sp.sin(g) * X / rr, sp.sin(g) * Y / rr, sp.sin(g) * Z / rr, sp.cos(g)]
du = [[sp.diff(c, v) for c in u] for v in XYZ]
ddu = [[[sp.diff(c, v, w) for c in u] for w in XYZ] for v in XYZ]
fu = sp.lambdify(XYZ, u, 'numpy'); fdu = sp.lambdify(XYZ, du, 'numpy'); fddu = sp.lambdify(XYZ, ddu, 'numpy')
def leaf(v, n):
    if isinstance(v, (list, tuple)):
        return np.array([leaf(q, n) for q in v])
    return np.asarray(v, dtype=float) * np.ones(n)
def fields_at(P, second=False):
    n = len(P)
    U = leaf(fu(*P.T), n); dU = leaf(fdu(*P.T), n)
    u1, u2, u3, u4 = U
    def dn_of(Uu, dUu):
        a1, a2, a3, a4 = Uu; b1, b2, b3, b4 = dUu
        return np.array([2 * (b1 * a3 + a1 * b3 + b2 * a4 + a2 * b4), 2 * (b1 * a4 + a1 * b4 - b2 * a3 - a2 * b3),
                         2 * (a1 * b1 + a2 * b2 - a3 * b3 - a4 * b4)])
    dn = np.array([dn_of(U, dU[i]) for i in range(3)])
    a = np.array([u1 * dU[i][1] - u2 * dU[i][0] + u3 * dU[i][3] - u4 * dU[i][2] for i in range(3)])
    out = dict(e2=0.25 * np.sum(dn ** 2, axis=(0, 1)), gchi2=np.sum(dU ** 2, axis=(0, 1)), a=a)
    if second:
        ddU = leaf(fddu(*P.T), n)
        da = np.zeros((3, 3, n))
        for i in range(3):
            for j in range(3):
                da[i, j] = (dU[i][0] * dU[j][1] + u1 * ddU[i][j][1] - dU[i][1] * dU[j][0] - u2 * ddU[i][j][0]
                            + dU[i][2] * dU[j][3] + u3 * ddU[i][j][3] - dU[i][3] * dU[j][2] - u4 * ddU[i][j][2])
        out['f'] = np.array([da[1, 2] - da[2, 1], da[2, 0] - da[0, 2], da[0, 1] - da[1, 0]])
    return out
cg, cw = np.polynomial.legendre.leggauss(48); phg = (np.arange(48) + 0.5) * 2 * np.pi / 48; phw = 2 * np.pi / 48
def shell_avg(r):
    C, PH = np.meshgrid(cg, phg, indexing='ij'); S = np.sqrt(1 - C ** 2)
    P = np.stack([r * S * np.cos(PH), r * S * np.sin(PH), r * C], axis=-1).reshape(-1, 3)
    w = (cw[:, None] * phw * np.ones_like(PH)).ravel() / (4 * np.pi)
    F = fields_at(P)
    return np.sum(F['e2'] * w), np.sum(F['gchi2'] * w)

hdr("2. Desk-check A (neutral C^2 knot filling the sphere), recomputed")
rg, rw = np.polynomial.legendre.leggauss(80); rq = (rg + 1) * R / 2; rwq = rw * R / 2
e2bar = np.array([shell_avg(r)[0] for r in rq]); gbar = np.array([shell_avg(r)[1] for r in rq])
I_n = np.sum(4 * np.pi * rq ** 2 * e2bar * rwq); I_full = np.sum(4 * np.pi * rq ** 2 * gbar * rwq)
print(f"  int (1/4)|dn|^2 = {I_n:.4f};  int |grad chi|^2 = {I_full:.4f} (analytic 4 pi R (pi^2/3 + 1) = {4 * np.pi * R * (np.pi ** 2 / 3 + 1):.4f})")
E_n, E_full = 2 * XI ** 2 * I_n, 2 * XI ** 2 * I_full
print(f"  E_knot (n-only) = {E_n:.1f} eps_c l^3 -> {E_n / V:.0f}x the condensation energy in the sphere (desk: 191, 366x)")
print(f"  E_knot (with built-in flow) = {E_full:.1f} -> {E_full / V:.0f}x (desk: 287, 548x)")
print("  TWIST CN-TWIST-15 (369x) is the n-only number; the desk's lower end agrees to ~1% (its 181^3 grid).")

# =============================================================================== 3
hdr("3. The unwinding barrier: radial minimisations of the corpus functional")
rmax, N = 14 * XI, 3200
r = np.linspace(0, rmax, N + 1); dr = r[1] - r[0]
rm = 0.5 * (r[1:] + r[:-1])
from scipy.interpolate import interp1d
rs_fine = np.linspace(1e-4, R, 120)
e2_fine = np.array([shell_avg(x)[0] for x in rs_fine])
e2f = interp1d(rs_fine, e2_fine, kind='cubic', bounds_error=False, fill_value=(e2_fine[0], 0.0))
E2r = np.where(r <= R, e2f(np.clip(r, 1e-4, R)), 0.0)
wvol = 4 * np.pi * r ** 2 * dr; wvol[0] *= 0.5; wvol[-1] *= 0.5
wgrad = 4 * np.pi * rm ** 2 / dr
def energy(s_free, mask_fixed, s_fixed, texture):
    s = s_fixed.copy(); s[~mask_fixed] = s_free
    ds = np.diff(s)
    e = np.sum(2 * XI ** 2 * wgrad * ds ** 2) + np.sum(wvol * ((s ** 2 - 1) ** 2 + (2 * XI ** 2 * E2r * s ** 2 if texture else 0)))
    gfull = np.zeros_like(s)
    gfull[:-1] -= 4 * XI ** 2 * wgrad * ds; gfull[1:] += 4 * XI ** 2 * wgrad * ds
    gfull += wvol * (4 * s * (s ** 2 - 1) + (4 * XI ** 2 * E2r * s if texture else 0))
    return e, gfull[~mask_fixed]
def solve(mask_fixed, s_fixed, texture, s0):
    res = minimize(lambda x: energy(x, mask_fixed, s_fixed, texture), s0[~mask_fixed], jac=True, method='L-BFGS-B',
                   options={'maxiter': 20000, 'gtol': 1e-10, 'ftol': 1e-14})
    s = s_fixed.copy(); s[~mask_fixed] = res.x
    return res.fun, s
fixed = np.zeros(N + 1, bool); fixed[-1] = True; sf = np.ones(N + 1)
# (a) normal ball
fa = fixed.copy(); fa[r <= R] = True; sfa = sf.copy(); sfa[r <= R] = 0.0
Ea, sa = solve(fa, sfa, False, np.ones(N + 1))
# (b) texture, density free
Eb, sb = solve(fixed, sf, True, np.ones(N + 1))
# (c) texture at full density
Ec = 2 * XI ** 2 * I_n
print(f"  radial grid: {N} cells to {rmax:.1f} a (dr = {dr:.4f})")
print(f"  (a) fully normal sphere (s = 0 for r < R), healing outside:  E = {Ea:7.2f} eps_c l^3")
print(f"      [bulk part V = {V:.3f}; the rest is the healing profile outside, ~ 4 pi R xi^2 x 2 = {8 * np.pi * R * XI ** 2:.1f} for 1 - R/r]")
print(f"  (b) Hopf texture kept, density free to respond:              E = {Eb:7.2f} eps_c l^3;  s(0) = {sb[0]:.4f}, s(R) = {np.interp(R, r, sb):.4f}")
print(f"  (c) Hopf texture at full density (n-only):                   E = {Ec:7.2f} eps_c l^3")
print(f"  -> letting the density respond lowers the knot from {Ec:.0f} to {Eb:.0f} eps_c l^3 (it never reaches zero")
print(f"     density, so the radial minimum keeps the topology); a fully normal sphere would cost {Ea:.0f}.")
inside = r <= R
frac_dep = np.sum(wvol[inside & (sb ** 2 < 0.5)]) / np.sum(wvol[inside])
print(f"  In (b) the density is below half its bulk value over {100 * frac_dep:.0f}% of the sphere's volume.")
# Derrick with the density free: shrink the knot to size L < R inside the sphere
print("  Knot shrunk to size L inside the sphere, density free (radial):")
EL = []
for Lk in (0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.025):
    E2r_save = E2r.copy()
    sc = R / Lk
    E2r = np.where(r <= Lk, sc ** 2 * e2f(np.clip(r * sc, 1e-4, R)), 0.0)
    Ek, sk = solve(fixed, sf, True, np.ones(N + 1))
    EL.append(Ek)
    print(f"     L = {Lk:6.3f} a  ({Lk / R:5.3f} R):  E = {Ek:8.3f} eps_c l^3   s(0) = {sk[0]:.4f}")
    E2r = E2r_save
mono = all(EL[i] > EL[i + 1] for i in range(len(EL) - 1))
print(f"  E(L) decreases monotonically as the knot shrinks: {mono}. There is no barrier on the shrink path:")
print("  the knot collapses (Derrick, now with the density included) and unwinds at a point as L -> 0.")
print(f"  TWIST CN-TWIST-15/16 compared the knot with the bulk term u_c V = {V:.3f} and called unwinding '369x")
print("  cheaper'. That ratio is the knot's energy over the bulk condensation energy, not over a barrier.")
print("  Corrected statement: the knot sector has no barrier at all against shrinking, so the conclusion")
print("  (no protected knot in V0) is stronger than stated, while the '369x cheaper' wording is wrong.")
print(f"  Desk A's ~23 eps_c l^3 'barrier' (bulk + gradient on scale R) is likewise not the operative barrier;")
print("  its Derrick line ('the knot pulls inward') is the operative statement.")

# =============================================================================== 4
hdr("4. Impulse of a pinned knot (does it self-propel? does an aligned array carry momentum?)")
rg, rw = np.polynomial.legendre.leggauss(60); rq = (rg + 1) * R / 2; rwq = rw * R / 2
cg2, cw2 = np.polynomial.legendre.leggauss(40); ph2 = (np.arange(40) + 0.5) * 2 * np.pi / 40
Rr, Cc, PH = np.meshgrid(rq, cg2, ph2, indexing='ij'); Ss = np.sqrt(1 - Cc ** 2)
Pq = np.stack([Rr * Ss * np.cos(PH), Rr * Ss * np.sin(PH), Rr * Cc], axis=-1).reshape(-1, 3)
Wq = (rwq[:, None, None] * cw2[None, :, None] * (2 * np.pi / 40) * Rr ** 2).ravel()
F = fields_at(Pq, second=True); f = F['f']
net = np.array([np.sum(f[k] * Wq) for k in range(3)])
imp = 0.5 * np.array([np.sum(np.cross(Pq, f.T).T[k] * Wq) for k in range(3)])
absf = np.sum(np.linalg.norm(f, axis=0) * Wq)
print(f"  int f dV = {np.round(net, 12)}  (|.|/int|f| = {np.linalg.norm(net) / absf:.1e})")
print(f"  impulse P = 1/2 int x * f dV = {np.round(imp, 6)};  |P|/(R int|f| dV) = {np.linalg.norm(imp) / (R * absf):.4f}")
print("  Nonzero impulse along the knot axis: zero net vorticity but a dipolar outside flow, like a smoke ring.")
print("  => (i) a free knot translates; holding one at a lattice site needs a pinning force from the shell")
print("     (another input); (ii) an all-aligned array carries a net momentum density n P along c (an")
print("     'aether wind'); the alternating pattern cancels it. Desk C's dipolar void flows are consistent")
print("     with this; TWIST sec.9's 'no macroscopic twist field' is right for f, but not for the flow.")

# =============================================================================== 5
hdr("5. Desk-check C: ring size, and the alternating pattern's residual axis")
ring = 0.6106 * R
print(f"  desk ring radius 0.6106 R = {ring:.4f} a = {ring / XI:.3f} xi")
print("  Gross-Pitaevskii vortex rings exist only down to radii of order xi; smaller solutions lose their")
print("  zeros and become vortex-free rarefaction pulses (Jones & Roberts 1982). A ring of 0.13 xi is not a")
print("  vortex ring of this medium, so desk C's flow pattern is conditional on knots existing (TWIST: they don't).")
for name, m in (("all aligned", np.array([1, 1, 1, 1.0])), ("alternating", np.array([1, -1, 1, -1.0]))):
    net_m = m.mean()
    Qzz = np.mean(1.5 * m ** 2 - 0.5)    # knot axes all along +-z
    print(f"  {name:12s}: net axis <m_z> = {net_m:+.1f};  nematic order Q_zz = <3 m_z^2 - 1>/2 = {Qzz:.1f}")
print("  The alternating pattern has no net direction but still singles out the c-axis (Q_zz = 1, maximal).")
print("  A two-way speed-of-light anisotropy of that axial (cos 2 theta) type is what rotating-cavity")
print("  Michelson-Morley experiments measure (twice the rotation rate), at Delta c/c ~ 1e-17..1e-18.")
print("  So 'alternating eases the light-speed worry' (desk C) holds only for a net direction, not the axis.")
