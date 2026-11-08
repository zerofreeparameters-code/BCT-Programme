#!/usr/bin/env python3
"""
Gate TWIST -- Q3 (screening, virial) and Q4 (shell items), numeric parts.

Q3-A  Virial theorem for a relaxed (force-free) field in a ball with B.n = 0 at the wall:
      lowest Chandrasekhar-Kendall (spheromak) state, kR = 4.4934. Check <B^2/2>_wall = u_bar/3,
      W = (k/2) K (Arnold bound saturated), div B = 0, curl B = k B.
Q3-B  Wall pressure in condensation-energy units for a Hopf-1 twist field in a sphere of radius R,
      with the Q1/Q2 purchase (Maxwell coupling e, penetration depth lambda_L).
Q3-C  V0 alone: Hopf-1 texture confined to the ball (n fixed on the wall = grip granted):
      texture energy density vs condensation energy; local W~ = xi^2 (1/4)|dn|^2 vs the
      condensate-destruction threshold W~ = 1 (exact tree result, Q1 part F1).
Q4-iv Free edge: the same construction without the boundary pinned -> the 'Hopf number'
      varies continuously (no invariant).
Q4-iii Wire-medium (Pendry et al. PRL 76, 4773 (1996)) plasma cutoff for connected conducting shells
      at Planck spacing; transparency requirement vs screening requirement (Pearl length).
Units: a = l_P = 1 unless stated.  Run: python3 -I twist_q3q4_shell.py
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq

ROCT = (np.sqrt(2) - 1) / 2
RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi
XI = 1 / np.sqrt(8 * np.pi * ALPHA0)
R = 0.5

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

X, Y, Z = sp.symbols('x y z', real=True)
XYZ = (X, Y, Z)

def curl(F):
    return [sp.diff(F[2], Y) - sp.diff(F[1], Z), sp.diff(F[0], Z) - sp.diff(F[2], X), sp.diff(F[1], X) - sp.diff(F[0], Y)]

def ball_quadrature(Rb, nr=60, nc=40, nphi=40):
    rg, rw = np.polynomial.legendre.leggauss(nr); r = (rg + 1) * Rb / 2; rw = rw * Rb / 2
    cg, cw = np.polynomial.legendre.leggauss(nc)
    phg = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi; phw = np.full(nphi, 2 * np.pi / nphi)
    Rr, C, PH = np.meshgrid(r, cg, phg, indexing='ij')
    W = rw[:, None, None] * cw[None, :, None] * phw[None, None, :] * Rr ** 2
    S = np.sqrt(1 - C ** 2)
    P = np.stack([Rr * S * np.cos(PH), Rr * S * np.sin(PH), Rr * C], axis=-1).reshape(-1, 3)
    return P, W.ravel()

def sphere_quadrature(Rb, nc=60, nphi=60):
    cg, cw = np.polynomial.legendre.leggauss(nc)
    phg = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi; phw = np.full(nphi, 2 * np.pi / nphi)
    C, PH = np.meshgrid(cg, phg, indexing='ij')
    S = np.sqrt(1 - C ** 2)
    P = np.stack([Rb * S * np.cos(PH), Rb * S * np.sin(PH), Rb * C], axis=-1).reshape(-1, 3)
    return P, (cw[:, None] * phw[None, :]).ravel() * Rb ** 2

def leaf(v, n):
    if isinstance(v, (list, tuple)):
        return np.array([leaf(q, n) for q in v])
    return np.asarray(v, dtype=float) * np.ones(n)

# =============================================================================== Q3-A
hdr("Q3-A. Virial theorem for the relaxed knot field (spheromak, B.n = 0 at r = R)")
x1 = brentq(lambda x: np.sin(x) / x ** 2 - np.cos(x) / x, 4.0, 5.0)     # first zero of j1
kk = x1 / R
rr = sp.sqrt(X ** 2 + Y ** 2 + Z ** 2)
xs = sp.Float(kk) * rr
j1 = sp.sin(xs) / xs ** 2 - sp.cos(xs) / xs
psi = j1 * Z / rr
T = curl([psi * X, psi * Y, psi * Z])
Pf = [c / sp.Float(kk) for c in curl(T)]
B = [T[i] + Pf[i] for i in range(3)]
cB = curl(B)
divB = sum(sp.diff(B[i], v) for i, v in enumerate(XYZ))
fB = sp.lambdify(XYZ, B, 'numpy'); fcB = sp.lambdify(XYZ, cB, 'numpy'); fdiv = sp.lambdify(XYZ, divB, 'numpy')
P, Wq = ball_quadrature(R)
Bv = leaf(fB(*P.T), len(Wq)); cBv = leaf(fcB(*P.T), len(Wq)); dv = leaf(fdiv(*P.T), len(Wq))
scale = np.max(np.abs(Bv))
print(f"  kR = {x1:.6f} (first zero of j1)")
print(f"  max|curl B - k B|/max|B| = {np.max(np.abs(cBv - kk * Bv)) / scale:.2e};  max|div B|/(k max|B|) = {np.max(np.abs(dv)) / (kk * scale):.2e}")
Wmag = 0.5 * np.sum(np.sum(Bv ** 2, axis=0) * Wq)
K = np.sum(np.sum(Bv * (Bv / kk), axis=0) * Wq)                         # A = B/k
V = 4 * np.pi * R ** 3 / 3
Ps, Ws = sphere_quadrature(R)
Bs = leaf(fB(*Ps.T), len(Ws))
nhat = Ps.T / R
Bn = np.sum(Bs * nhat, axis=0)
wall_p = 0.5 * np.sum(np.sum(Bs ** 2, axis=0) * Ws) / (4 * np.pi * R ** 2)
print(f"  max|B.n| at wall / max|B| = {np.max(np.abs(Bn)) / scale:.2e}")
print(f"  W = {Wmag:.6e},  (k/2)K = {kk / 2 * K:.6e}   (Arnold bound saturated: ratio {Wmag / (kk / 2 * K):.8f})")
print(f"  mean wall pressure <B^2/2>_wall = {wall_p:.6e};  u_bar/3 = {Wmag / V / 3:.6e};  ratio = {wall_p / (Wmag / V / 3):.8f}")
print("  -> confirmed: a force-free knot with B.n = 0 pushes on its wall with mean pressure u_bar/3.")

# =============================================================================== Q3-B
hdr("Q3-B. Required wall pressure in condensation-energy units (bought Maxwell coupling)")
# twist-field Maxwell energy (1/2e^2)|curl a|^2 ; Hopf-1 helicity int a.curl a = 4 pi^2.
# Arnold: int |curl a|^2 >= k1 * 4 pi^2, k1 = x1/R. e^2 = 1/(2 lam^2 K_s); u_c = K_s/(2 xi^2).
coef = 6 * np.pi * x1 * (XI / R) ** 2
print(f"  u_bar/u_c >= 6 pi x1 (xi/R)^2 (lam_L/R)^2 = {coef:.1f} (lam_L/R)^2 ;  wall P/u_c = {coef / 3:.1f} (lam_L/R)^2")
lam_max = R * np.sqrt(3 / coef)
print(f"  A wall of the same condensate holds at most P ~ u_c (thermodynamic critical field). Requires")
print(f"  lam_L <= {lam_max / R:.4f} R = {lam_max:.4f} a,  i.e. kappa = lam_L/xi <= {lam_max / XI:.4f} (extreme type I).")
print(f"  lam_L is set by the bought coupling e: the requirement can only be met by choosing e (no-fit: forbidden).")
print(f"  Density is uniform to 0.6% (Q2), so lam_shell = lam_void = lam_interior to ~0.3%: the shell has no")
print(f"  screening of its own; it screens exactly as much as the interior it is supposed to hold the field in.")
print(f"  Shell thickness: corpus delta shell (d = 0); App J's input d = sqrt(r_oct r_tet) = {np.sqrt(ROCT * RTET):.4f} a.")
print(f"  Density-profile width of the shell perturbation: xi/sqrt2 = {XI / np.sqrt(2):.3f} a > R = {R} a.")

# =============================================================================== Q3-C
hdr("Q3-C. V0 alone: Hopf-1 texture pinned in the ball (grip granted), energy vs condensation")
def ball_hopf_u(svar, L=R):
    # unit 4-vector u = (sin g xhat, cos g), g = pi (1 - s r/L) for r<L, 0 outside; s=1 pins the wall
    g = sp.pi * (1 - svar * rr / L)
    return [sp.sin(g) * X / rr, sp.sin(g) * Y / rr, sp.sin(g) * Z / rr, sp.cos(g)]

def texture_numbers(svar, Rb=R, nr=80):
    u = ball_hopf_u(svar, Rb)
    du = [[sp.diff(c, v) for c in u] for v in XYZ]
    fu = sp.lambdify(XYZ, u, 'numpy'); fdu = sp.lambdify(XYZ, du, 'numpy')
    ddu = [[[sp.diff(c, v, w) for c in u] for w in XYZ] for v in XYZ]
    fddu = sp.lambdify(XYZ, ddu, 'numpy')
    P, Wq = ball_quadrature(Rb, nr=nr, nc=48, nphi=48)
    n = len(Wq)
    U = leaf(fu(*P.T), n); dU = leaf(fdu(*P.T), n); ddU = leaf(fddu(*P.T), n)
    u1, u2, u3, u4 = U
    def dn_of(Uu, dUu):
        a1, a2, a3, a4 = Uu; b1, b2, b3, b4 = dUu
        return np.array([2 * (b1 * a3 + a1 * b3 + b2 * a4 + a2 * b4), 2 * (b1 * a4 + a1 * b4 - b2 * a3 - a2 * b3),
                         2 * (a1 * b1 + a2 * b2 - a3 * b3 - a4 * b4)])
    dn = np.array([dn_of(U, dU[i]) for i in range(3)])
    a = np.array([u1 * dU[i][1] - u2 * dU[i][0] + u3 * dU[i][3] - u4 * dU[i][2] for i in range(3)])
    da = np.zeros((3, 3, n))
    for i in range(3):
        for j in range(3):
            da[i, j] = (dU[i][0] * dU[j][1] + u1 * ddU[i][j][1] - dU[i][1] * dU[j][0] - u2 * ddU[i][j][0]
                        + dU[i][2] * dU[j][3] + u3 * ddU[i][j][3] - dU[i][3] * dU[j][2] - u4 * ddU[i][j][2])
    curl_a = np.array([da[1, 2] - da[2, 1], da[2, 0] - da[0, 2], da[0, 1] - da[1, 0]])
    H = np.sum(np.sum(a * curl_a, axis=0) * Wq) / (4 * np.pi ** 2)
    e2 = 0.25 * np.sum(dn ** 2, axis=(0, 1))
    E2 = np.sum(e2 * Wq)
    return H, E2, e2, Wq

H1, E2, e2, Wq = texture_numbers(1.0)
V = 4 * np.pi * R ** 3 / 3
u2bar = E2 / V                                      # units K_s
uc = 1 / (2 * XI ** 2)                              # K_s / (2 xi^2)
Wt = XI ** 2 * e2
frac = np.sum(Wq[Wt > 1]) / V
print(f"  pinned ball map (g = pi(1 - r/R)): H = {H1:.6f}")
print(f"  E2 = int (1/4)|dn|^2 = {E2:.4f} K_s  (= {E2 / R:.3f} K_s R)")
print(f"  texture energy density / condensation energy density = {u2bar / uc:.1f}")
print(f"  local W~ = xi^2 (1/4)|dn|^2: mean {np.sum(Wt * Wq) / V:.1f}, fraction of ball with W~ > 1: {frac:.3f}")
print(f"  -> Exact tree result (Q1-F1): for W~ >= 1 the condensate is destroyed (s = 0). The knot's own")
print(f"     gradients exceed that threshold in {frac:.0%} of the sphere: the interior goes normal, n is")
print(f"     undefined there, and the Hopf number has nothing to live on.")
print(f"  Unwinding cost <= u_c V = {uc * V:.4f} K_s  vs texture energy {E2:.2f} K_s  (ratio {E2 / (uc * V):.0f}).")
print("  Derrick inside the ball: shrinking the texture to size L < R scales E2 -> E2 L/R (monotone), so")
print("  even with the wall pinned the knot collapses to a point and unwinds through a normal core.")

# =============================================================================== Q4-iv
hdr("Q4-iv. Free edge (no grip): is the Hopf number protected?")
print("   s (pinning)   'H' = (1/4pi^2) int_ball a.curl a   [gauge-dependent once the edge is free]")
for sv in (1.0, 0.9, 0.75, 0.5, 0.25, 0.0):
    Hs, _, _, _ = texture_numbers(sv, nr=60)
    print(f"     {sv:5.2f}       {Hs:+.6f}")
print("  With the wall value of n not fixed, a one-parameter family connects H = 1 to H = 0 continuously")
print("  (B^3 is contractible): no invariant, no protection. The corpus shell term ~|Psi|^2 is U(2)")
print("  invariant and cannot pin n. A direction-dependent grip term must be added.")

# =============================================================================== Q4-iii
hdr("Q4-iii. Wire medium of connected conducting shells at Planck spacing")
c = 2.99792458e8; lP = 1.616255e-35; hbar_eVs = 6.582119569e-16
wP = c / lP
w_hi = 3.7e15 / hbar_eVs           # highest-energy photon reported (LHAASO, Cygnus X-3, ~3.7 PeV)
w_lo = 2 * np.pi * 1e7             # cosmic radio routinely received at ~10 MHz
print(f"  Planck angular frequency c/l_P = {wP:.4e} s^-1")
print("  Pendry et al. (1996), thin wires radius r, spacing a:  omega_p^2 = 2 pi c^2 / (a^2 ln(a/r))")
for ra in (0.3, 0.1, 1e-2, 1e-5, 1e-10, 1e-30):
    wp = (c / lP) * np.sqrt(2 * np.pi / np.log(1 / ra))
    print(f"     r/a = {ra:7.0e}:  omega_p = {wp:.3e} s^-1 = {wp / wP:.3f} omega_Planck")
print(f"  Highest-energy photon observed ~3.7 PeV: omega = {w_hi:.2e} s^-1 = {w_hi / wP:.1e} omega_Planck")
print(f"  Low-frequency cosmic radio ~10 MHz:      omega = {w_lo:.2e} s^-1 = {w_lo / wP:.1e} omega_Planck")
print("  A plasma medium is opaque BELOW omega_p: every observed photon (radio to PeV gamma) lies 13-36")
print("  orders of magnitude below the cutoff -> connected conducting shells would make the vacuum opaque.")
need = (wP / w_lo) ** 2
print(f"  Transparency down to 10 MHz needs the dimensionless inductance per cell l = L/(mu0 a) >= (omega_P/omega)^2")
print(f"  = {need:.1e}. Geometric part ln(a/r)/2pi is O(1-10). Kinetic part (Lambda/2a) N_sq (Lambda = Pearl")
print(f"  length 2 lam^2/d of the shell, N_sq = squares along the path ~ ln(R/r_c)/pi) would need")
print(f"  Lambda >~ {2 * need:.0e} a / N_sq. Holding the knot needs the shell to screen on scale R: Lambda <~ R = 0.5 a.")
print(f"  Gap: ~{np.log10(2 * need / 0.5):.0f} orders of magnitude, closable only by N_sq ~ 1e71, i.e. contacts")
print(f"  narrower than R exp(-1e71): effectively insulating contacts -- an added input.")
print("  Static limit: a connected screening network also expels static magnetic fields (Meissner); static")
print("  fields are observed to penetrate the vacuum. The wire-medium argument HOLDS.")
