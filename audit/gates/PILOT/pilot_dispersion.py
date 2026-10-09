#!/usr/bin/env python3
"""
Gate PILOT -- Step 3: dispersion, computed cold.

Card: audit/gates/gate_PILOT_prompt.md @ 34acd40, SHA-256
df9a4be17a9f359af6134651f011ced7203741590d6ef68266e4ff7518b29546.
Corpus pin 0305526015460b2c90d6cbcb6ca9d0e56d82f64e.

What this does (card Sec. 4, Step 3):
  (1) re-derives xi/a from r_oct, r_tet using the corpus's own stated formula
      xi = a / sqrt(8 pi alpha0), alpha0 = r_oct r_tet / pi  (Vol.1 Sec.4.3, App E.3;
      quoted in AZ6, AZ7, Vol.2 Phase 18), at 60 dps working / 40 dps reported;
  (2) builds the 12-neighbour lattice at c/a = sqrt2 (all 12 neighbours at distance a),
      its nearest-neighbour graph Laplacian normalised so lambda(k) -> |k|^2 as k -> 0,
      and its exact quartic term (tests the corpus conjecture of App E.0 Sec.3.1 that
      the lattice phonon dispersion is 'exactly linear');
  (3) for every distinct written law, gives omega(k) in the continuum and on the
      lattice, and the maximum group velocity |grad_k omega| over the Brillouin zone,
      the k where it occurs, to >= 10 digits (mpmath refinement at 60 dps);
  (4) measures the lattice front: retarded Green's function by FFT, amplitude outside
      the max-group-velocity cone and its decay law.

Units: a = nearest-neighbour distance = 1, c = k->0 sound speed = 1 (corpus: c_s = c,
AZ6 Lemma 'hyp' (i)). Any dimensionful statement inherits a = l_P (Vol.2 Sec.3 A2).
Run:  python3 -I pilot_dispersion.py      (numpy, scipy, mpmath, sympy)
"""
import sys
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.optimize import minimize

mp.mp.dps = 60
REP = 40          # digits reported for closed forms
NUMREP = 15       # digits reported for numerical maxima (card asks >= 10)
out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


def mpf_s(x, n=REP):
    return mp.nstr(x, n, strip_zeros=False)


# ---------------------------------------------------------------- 1. closed forms
say("=" * 78)
say("1. CLOSED FORMS (mpmath %d dps working, %d reported)" % (mp.mp.dps, REP))
say("=" * 78)
r_oct = (mp.sqrt(2) - 1) / 2
r_tet = (mp.sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / mp.pi
xi = 1 / mp.sqrt(8 * mp.pi * alpha0)          # corpus formula, units of a
say("r_oct  = (sqrt2-1)/2         =", mpf_s(r_oct))
say("r_tet  = (sqrt6-2)/4         =", mpf_s(r_tet))
say("alpha0 = r_oct r_tet / pi    =", mpf_s(alpha0))
say("xi/a   = 1/sqrt(8 pi alpha0) = 1/sqrt((sqrt2-1)(sqrt6-2)) =", mpf_s(xi))
S2, S6 = sp.sqrt(2), sp.sqrt(6)
xi2_exact = sp.nsimplify(1 / ((S2 - 1) * (S6 - 2)))
xi2_rad = sp.radsimp(1 / ((S2 - 1) * (S6 - 2)))
say("xi^2/a^2 exact               =", sp.simplify(xi2_rad), " =", mpf_s(xi ** 2))
assert abs(mp.mpf(str(sp.N(xi2_rad, 70))) - xi ** 2) < mp.mpf(10) ** -55
# cross-checks against corpus-quoted numbers
say("  check vs corpus: App J Higgs gap 2/xi =", mpf_s(2 / xi, 8), "(App J prints 0.8630)")
say("  check vs corpus: -1/xi + alpha0      =", mpf_s(-1 / xi + alpha0, 8), "(App J prints -0.424083)")
say("  check vs corpus: xi/r_oct            =", mpf_s(xi / r_oct, 8), "(Vol.2 prints 11.19 / 11.1901)")

# Conventions relating xi to the coupling (card: 'if sources differ, compute each')
#   C1  AZ6/AZ7: xi = hbar/sqrt(2 m g n0) = hbar/(sqrt2 m c_s)  ->  w = c k sqrt(1 + (k xi)^2 / 2)
#   C2  Letter 64 eq. for w(k):           w = c_s k sqrt(1 + (k xi)^2)  -> xi = hbar/(2 m c_s)
#   C3  Letter 64 text: xi = hbar/(m c_s)                               ->  w = c k sqrt(1 + (k xi)^2 / 4)
BETA = {
    "B-C1": xi ** 2 / 2,
    "B-C2": xi ** 2,
    "B-C3": xi ** 2 / 4,
    "GW-L73": alpha0,          # w^2 = c^2 k^2 [1 + alpha0 (k l_P)^2], a = l_P
}
for k_, b in BETA.items():
    say("  beta[%s] = %s" % (k_, mpf_s(b, 20)))

# ---------------------------------------------------------------- 2. the lattice
say("")
say("=" * 78)
say("2. 12-NEIGHBOUR LATTICE AT c/a = sqrt2 AND ITS GRAPH LAPLACIAN")
say("=" * 78)
s2 = sp.sqrt(2)
body = [sp.Matrix([sx * sp.Rational(1, 2), sy * sp.Rational(1, 2), sz / s2])
        for sx in (1, -1) for sy in (1, -1) for sz in (1, -1)]
plane = [sp.Matrix(v) for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0])]
NN = body + plane
assert len(NN) == 12 and all(sp.simplify(v.dot(v)) == 1 for v in NN)
say("12 neighbours, all at distance a: 8 body (+-1/2,+-1/2,+-1/sqrt2), 4 in-plane (+-1,0,0),(0,+-1,0)")
M2 = sp.zeros(3)
for v in NN:
    M2 += v * v.T
say("second moment sum_d d d^T =", list(M2), " -> isotropic (= 4 I): k^2 term isotropic")
M2b = sp.zeros(3)
for v in body:
    M2b += v * v.T
say("8 body vectors alone (corpus gamma(k), z = 8):", list(M2b), " -> NOT isotropic (zz/xx = 2)")
kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
kv = sp.Matrix([kx, ky, kz])
T4 = sp.expand(sum((kv.dot(v)) ** 4 for v in NN))
# cubic axes of this fcc: X=(kx+ky)/sqrt2, Y=(kx-ky)/sqrt2, Z=kz
X_, Y_ = (kx + ky) / s2, (kx - ky) / s2
k2 = kx ** 2 + ky ** 2 + kz ** 2
SK4 = sp.expand(X_ ** 4 + Y_ ** 4 + kz ** 4)
A_, B_ = sp.symbols("A B")
sol = sp.solve(sp.Poly(sp.expand(T4 - A_ * k2 ** 2 - B_ * SK4), kx, ky, kz).coeffs(), [A_, B_])
say("sum_d (k.d)^4 = A |k|^4 + B sum_i K_i^4 (cubic axes):", sol)
# lambda(k) = (1/2) sum_d (1 - cos k.d) = |k|^2 - T4/48 + O(k^6)
say("lambda(k) = (1/2) sum_d (1 - cos k.d) = |k|^2 - |k|^4/16 + (sum_i K_i^4)/48 + O(k^6)")
for name, s in (("[001]", sp.Integer(1)), ("[110]", sp.Rational(1, 2)), ("[111]", sp.Rational(1, 3))):
    c4 = -sp.Rational(1, 16) + s / 48
    say("  quartic coefficient along %s: %s  (nonzero, direction-dependent)" % (name, c4))
say("  => App E.0 Sec.3.1 conjecture ('k^4 coefficient vanishes under O_h') is FALSE for the")
say("     nearest-neighbour lattice. For ANY finite-range lattice operator omega^2(k) is a")
say("     trigonometric polynomial (real-analytic, periodic); if it equalled c^2|k|^2 on a")
say("     neighbourhood of k=0 it would equal it everywhere, contradicting periodicity. Exact")
say("     linearity is impossible on any lattice with finite-range coupling.")

# primitive basis and the six neighbour pairs in primitive phases
a1 = np.array([1.0, 0.0, 0.0])
a2 = np.array([0.0, 1.0, 0.0])
a3 = np.array([0.5, 0.5, 1 / np.sqrt(2)])
Aprim = np.vstack([a1, a2, a3])                   # theta = Aprim @ k
Ainv = np.linalg.inv(Aprim)                       # k = Ainv @ theta
MPAIR = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 1], [0, -1, 1], [-1, -1, 1]], float)
DELTA = MPAIR @ Aprim                             # the six representative neighbour vectors
assert np.allclose(np.linalg.norm(DELTA, axis=1), 1)
BODY = [2, 3, 4, 5]                               # pairs that are body vectors (gamma(k), z=8)
E1C = np.array([1, 1, 0]) / np.sqrt(2)
E2C = np.array([-1, 1, 0]) / np.sqrt(2)
E3C = np.array([0, 0, 1.0])


def to_cubic(k):
    return np.array([k @ E1C, k @ E2C, k @ E3C])


def lam_and_grad(theta):
    """theta: (...,3) primitive phases. Returns lambda, grad_k lambda (Cartesian)."""
    phi = theta @ MPAIR.T
    lam = np.sum(1 - np.cos(phi), axis=-1)
    grad = np.sin(phi) @ DELTA
    return lam, grad


def gam_and_grad(theta):
    """corpus 8-neighbour structure factor gamma(k) = 8 cos(kx/2) cos(ky/2) cos(kz/sqrt2)."""
    phi = theta[..., BODY] if False else (theta @ MPAIR.T)[..., BODY]
    g = 2 * np.sum(np.cos(phi), axis=-1)
    grad = -2 * np.sin(phi) @ DELTA[BODY]
    return g, grad


# sanity: gamma product form
_th = np.array([0.3, -1.1, 0.7])
_k = Ainv @ _th
assert abs(gam_and_grad(_th)[0] - 8 * np.cos(_k[0] / 2) * np.cos(_k[1] / 2) * np.cos(_k[2] / np.sqrt(2))) < 1e-12

# ---------------------------------------------------------------- 3. laws and group velocities
LAWS = {}
LAWS["W"] = dict(desc="wave / TF-hydro / XY-Goldstone: w = c sqrt(lam)  [AZ6 eq.S2; Vol1 E.1, E.3; Vol2 acoustic; L129]",
                 F=lambda l, p: np.sqrt(l), dF=lambda l, p: 0.5 / np.sqrt(l), p=None, unit="c")
for key in ("B-C1", "B-C2", "B-C3"):
    LAWS[key] = dict(desc="Bogoliubov (first-order GP) w = c sqrt(lam + beta lam^2), beta=%s  [AZ6 eq.SGP; L60 eq.1; L64]" % mp.nstr(BETA[key], 8),
                     F=lambda l, b: np.sqrt(l + b * l * l), dF=lambda l, b: (1 + 2 * b * l) / (2 * np.sqrt(l + b * l * l)),
                     p=float(BETA[key]), unit="c")
LAWS["GW-L73"] = dict(desc="GW dispersion w = c sqrt(lam + alpha0 lam^2)  [Letter 73]",
                      F=lambda l, b: np.sqrt(l + b * l * l), dF=lambda l, b: (1 + 2 * b * l) / (2 * np.sqrt(l + b * l * l)),
                      p=float(alpha0), unit="c")
for key, m in (("KG-1/xi", 1 / xi), ("KG-2/xi", 2 / xi)):
    LAWS[key] = dict(desc="massive KG (App J amplitude mode) w = c sqrt(lam + m^2), m=%s" % mp.nstr(m, 8),
                     F=lambda l, mm: np.sqrt(l + mm * mm), dF=lambda l, mm: 0.5 / np.sqrt(l + mm * mm), p=float(m), unit="c")


def vg_lam(theta, law):
    lam, g = lam_and_grad(theta)
    L = LAWS[law]
    with np.errstate(divide="ignore", invalid="ignore"):
        v = L["dF"](lam, L["p"]) * np.linalg.norm(g, axis=-1)
    return np.nan_to_num(v, nan=0.0, posinf=0.0)


def vg_tb(theta):          # corpus tight-binding band w = alpha0 |gamma|, absolute units of c
    g, gg = gam_and_grad(theta)
    return float(alpha0) * np.linalg.norm(gg, axis=-1)


def vg_bh(theta):          # AZ7 Bose-Hubbard Bogoliubov: eps = t(8-gamma), E = sqrt(eps(eps+2U)), t=U=alpha0
    t = U = float(alpha0)
    g, gg = gam_and_grad(theta)
    eps = t * (8 - g)
    E = np.sqrt(eps * (eps + 2 * U))
    with np.errstate(divide="ignore", invalid="ignore"):
        v = (eps + U) / E * t * np.linalg.norm(gg, axis=-1)
    return np.nan_to_num(v, nan=0.0)


VG = {k: (lambda th, kk=k: vg_lam(th, kk)) for k in LAWS}
VG["TB-AppK"] = vg_tb
VG["BH-AZ7"] = vg_bh


def grid_max(f, N=96):
    best = []
    t1 = np.linspace(0, 2 * np.pi, N, endpoint=False)
    T2, T3 = np.meshgrid(t1, t1, indexing="ij")
    for x in t1:
        th = np.stack([np.full_like(T2, x), T2, T3], axis=-1)
        v = f(th)
        idx = np.unravel_index(np.argmax(v), v.shape)
        best.append((v[idx], np.array([x, T2[idx], T3[idx]])))
    best.sort(key=lambda z: -z[0])
    return best[:12]


# --- mpmath versions for refinement
MP_MPAIR = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 1], [0, -1, 1], [-1, -1, 1]]
mp_a = [mp.matrix([1, 0, 0]), mp.matrix([0, 1, 0]), mp.matrix([mp.mpf(1) / 2, mp.mpf(1) / 2, 1 / mp.sqrt(2)])]
MP_DELTA = [sum((mp.mpf(r[i]) * mp_a[i] for i in range(3)), mp.matrix([0, 0, 0])) for r in MP_MPAIR]


def mp_lam_grad(th):
    phis = [sum(mp.mpf(r[i]) * th[i] for i in range(3)) for r in MP_MPAIR]
    lam = sum(1 - mp.cos(p) for p in phis)
    g = mp.matrix([0, 0, 0])
    for p, d in zip(phis, MP_DELTA):
        g += mp.sin(p) * d
    return lam, g


def mp_gam_grad(th):
    phis = [sum(mp.mpf(r[i]) * th[i] for i in range(3)) for r in MP_MPAIR]
    g = 2 * sum(mp.cos(phis[j]) for j in BODY)
    gg = mp.matrix([0, 0, 0])
    for j in BODY:
        gg += -2 * mp.sin(phis[j]) * MP_DELTA[j]
    return g, gg


def mp_v2(th, law):
    if law == "TB-AppK":
        g, gg = mp_gam_grad(th)
        return (alpha0 ** 2) * (gg[0] ** 2 + gg[1] ** 2 + gg[2] ** 2)
    if law == "BH-AZ7":
        g, gg = mp_gam_grad(th)
        eps = alpha0 * (8 - g)
        E2 = eps * (eps + 2 * alpha0)
        return ((eps + alpha0) ** 2 / E2) * alpha0 ** 2 * (gg[0] ** 2 + gg[1] ** 2 + gg[2] ** 2)
    lam, g = mp_lam_grad(th)
    n2 = g[0] ** 2 + g[1] ** 2 + g[2] ** 2
    if law == "W":
        return n2 / (4 * lam)
    if law.startswith("KG"):
        m = 1 / xi if law == "KG-1/xi" else 2 / xi
        return n2 / (4 * (lam + m * m))
    b = BETA[law]
    return (1 + 2 * b * lam) ** 2 * n2 / (4 * (lam + b * lam * lam))


MP_A = mp.matrix([[1, 0, 0], [0, 1, 0], [mp.mpf(1) / 2, mp.mpf(1) / 2, 1 / mp.sqrt(2)]])


def mp_v_of_k(kvec, law):
    return mp.sqrt(mp_v2(MP_A * kvec, law))


def refine(law, th0):
    """Nelder-Mead in 3D from the best grid point; then, if the maximum is at Gamma, report the
    analytic sup; otherwise solve dv/ds = 0 at 60 dps along the line k = s*d through the
    located maximum and check (60 dps) that perpendicular displacements lower v."""
    f = VG[law]
    r = minimize(lambda t: -f(np.array(t)), th0, method="Nelder-Mead",
                 options=dict(xatol=1e-13, fatol=1e-16, maxiter=40000))
    k_nm = reduce_k(Ainv @ r.x)
    if np.linalg.norm(k_nm) < 1e-3:
        return None, None, k_nm, "GAMMA"
    # snap the direction to the nearest symmetry axis if within 1e-6 (cubic or tetragonal axes)
    d = k_nm / np.linalg.norm(k_nm)
    axes = [E1C, E2C, E3C, (E1C + E2C) / np.sqrt(2), (E1C - E2C) / np.sqrt(2),
            (E1C + E2C + E3C) / np.sqrt(3), (E1C + E3C) / np.sqrt(2), (E2C + E3C) / np.sqrt(2)]
    snapped = "unsnapped"
    for ax in axes:
        for sgn in (1, -1):
            if np.linalg.norm(d - sgn * ax) < 1e-6:
                d = sgn * ax
                snapped = "snapped"
    dm = mp.matrix([mp.mpf(x) for x in d])
    # exact direction for the axes used (avoid double rounding): rebuild with mp
    def mpdir(v):
        v = mp.matrix(v)
        return v / mp.norm(v)
    s2m = mp.sqrt(2)
    for name, vv in (("E1C", [1 / s2m, 1 / s2m, 0]), ("E2C", [-1 / s2m, 1 / s2m, 0]), ("E3C", [0, 0, 1]),
                     ("x", [1, 0, 0]), ("y", [0, 1, 0])):
        for sgn in (1, -1):
            cand = mpdir([sgn * x for x in vv])
            if mp.norm(cand - dm) < mp.mpf("1e-5"):
                dm = cand
    s0 = mp.mpf(np.linalg.norm(k_nm))
    g = lambda s: mp.diff(lambda ss: mp_v_of_k(ss * dm, law), s)
    s_star = mp.findroot(g, s0, tol=mp.mpf(10) ** -45)
    vstar = mp_v_of_k(s_star * dm, law)
    # perpendicular check at 60 dps
    e1 = mp.matrix([1, 0, 0]) if abs(dm[0]) < mp.mpf("0.9") else mp.matrix([0, 1, 0])
    p1 = e1 - (e1.T * dm)[0] * dm
    p1 = p1 / mp.norm(p1)
    p2 = mp.matrix([dm[1] * p1[2] - dm[2] * p1[1], dm[2] * p1[0] - dm[0] * p1[2], dm[0] * p1[1] - dm[1] * p1[0]])
    worst = max(mp_v_of_k(s_star * dm + h * p, law) - vstar
                for h in (mp.mpf("1e-6"), mp.mpf("-1e-6"), mp.mpf("1e-3"), mp.mpf("-1e-3")) for p in (p1, p2))
    return s_star, vstar, (dm, worst, snapped), "LINE"


def mp_k_of_theta(th):
    Ainv_mp = mp.inverse(mp.matrix([[1, 0, 0], [0, 1, 0], [mp.mpf(1) / 2, mp.mpf(1) / 2, 1 / mp.sqrt(2)]]))
    return Ainv_mp * th


def reduce_k(k):
    """Map k to the shortest equivalent vector (first BZ) via reciprocal lattice."""
    B = 2 * np.pi * Ainv              # columns b_i satisfy a_j . b_i = 2 pi delta_ij
    best = k
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            for n3 in range(-2, 3):
                kk = k - B @ np.array([n1, n2, n3])
                if np.linalg.norm(kk) < np.linalg.norm(best) - 1e-12:
                    best = kk
    return best


PTS = {"Gamma": np.zeros(3), "X": np.array([0, 0, 1.0]) * 2 * np.pi / np.sqrt(2),
       "L": np.array([1, 1, 1.0]) * np.pi / np.sqrt(2), "W": np.array([1, 0.5, 0]) * 2 * np.pi / np.sqrt(2),
       "K": np.array([0.75, 0.75, 0]) * 2 * np.pi / np.sqrt(2)}


def label(kc):
    a = np.sort(np.abs(kc))[::-1]
    for nm, p in PTS.items():
        if np.allclose(a, np.sort(np.abs(p))[::-1], atol=1e-6):
            return nm
    return "general/line point"


say("")
say("=" * 78)
say("3. GROUP VELOCITY: max |grad_k omega| OVER THE BRILLOUIN ZONE")
say("=" * 78)
say("Continuum forms (lam -> |k|^2): W: w=ck (v_g=c, strict front c); KG: v_g<c, front c;")
say("Bogoliubov/GW: v_g = c(1+2 beta k^2)/sqrt(1+beta k^2) -> unbounded as k->inf (no front);")
say("first-order GP kernel is non-hyperbolic: response nonzero everywhere for t>0.")
RESULTS = {}
for law in ["W", "KG-1/xi", "KG-2/xi", "B-C1", "B-C2", "B-C3", "GW-L73", "TB-AppK", "BH-AZ7"]:
    cand = grid_max(VG[law])
    s_star, vmax, info, kind = refine(law, cand[0][1])
    desc = LAWS[law]["desc"] if law in LAWS else (
        "corpus tight-binding w = alpha0|gamma(k)| (8 nbrs) [App K/N; Vol1 R.2; L39] -- absolute units of c (a=l_P)"
        if law == "TB-AppK" else
        "AZ7 Bose-Hubbard Bogoliubov, t=U=alpha0, n0=1, z=8 -- absolute units of c (a=l_P)")
    say("-" * 78)
    say("[%s] %s" % (law, desc))
    if kind == "GAMMA":
        # analytic: v_g -> c as k -> 0; check below c on the grid away from Gamma and along directions
        excess = []
        for dname, dv in (("cubic[001]", E3C), ("cubic[110]", (E1C + E2C) / np.sqrt(2)),
                          ("cubic[111]", (E1C + E2C + E3C) / np.sqrt(3))):
            kk = mp.matrix([mp.mpf(x) for x in dv]) * mp.mpf("1e-4")
            excess.append("%s: v-c = %s" % (dname, mp.nstr(mp_v_of_k(kk, law) - 1, 6)))
        RESULTS[law] = (mp.mpf(1), np.zeros(3), np.zeros(3))
        say("    grid max away from Gamma = %.12f < 1. Supremum = c exactly, approached only as k -> 0" % cand[0][0])
        say("    (not attained). At |k|a = 1e-4: " + "; ".join(excess))
        say("    i.e. v_g = c[1 + (3/2)(c4 + beta) k^2 + ...] with c4 + beta < 0 in every direction.")
        continue
    dm, worst, snapped = info
    kr = np.array([float(x) for x in (s_star * dm)])
    kc = to_cubic(kr)
    RESULTS[law] = (vmax, kr, kc)
    say("    grid max %.12f  ->  60-dps line maximum |v_g| = %s" % (cand[0][0], mp.nstr(vmax, 30)))
    say("    at |k|a = %s along direction (tetragonal) (%.8f, %.8f, %.8f) [%s]" % (
        mp.nstr(s_star, 25), float(dm[0]), float(dm[1]), float(dm[2]), snapped))
    say("    cubic-axis components = (%.10f, %.10f, %.10f)  [%s]; |k|/|Gamma-X| = %.10f" % (
        *kc, label(kc), np.linalg.norm(kr) / (2 * np.pi / np.sqrt(2))))
    say("    3D check: max over perpendicular displacements (|h| = 1e-6, 1e-3) of v(k+h) - v(k) = %s (<0 => true max)"
        % mp.nstr(worst, 6))

# independent cross-checks (closed forms on the symmetry lines)
say("-" * 78)
say("Cross-checks, independent of the 3D machinery:")
tb_closed = 4 * mp.sqrt(2) * alpha0          # |grad gamma| max = 4 sqrt2 at k = (0,0,pi/sqrt2)
say("  TB: v_max = 4 sqrt2 alpha0 = (2-sqrt2)(sqrt6-2)/(2 pi) =", mp.nstr(tb_closed, REP),
    "| line result:", mp.nstr(RESULTS["TB-AppK"][0], 20), "| at |k|a = pi/sqrt2 =", mp.nstr(mp.pi / mp.sqrt(2), 20))
# Gamma-X line of the 12-neighbour lattice: lambda = 4(1 - cos u), u = |k| a / sqrt2, |grad lambda| = 2 sqrt2 sin u
for key in ("B-C1", "B-C2", "B-C3", "KG-1/xi", "KG-2/xi"):
    if key.startswith("B"):
        b = BETA[key]
        vline = lambda u: (1 + 2 * b * 4 * (1 - mp.cos(u))) / (2 * mp.sqrt(4 * (1 - mp.cos(u)) + b * 16 * (1 - mp.cos(u)) ** 2)) * 2 * mp.sqrt(2) * mp.sin(u)
    else:
        mm = 1 / xi if key == "KG-1/xi" else 2 / xi
        vline = lambda u: 1 / (2 * mp.sqrt(4 * (1 - mp.cos(u)) + mm ** 2)) * 2 * mp.sqrt(2) * mp.sin(u)
    u0 = mp.mpf(float(np.linalg.norm(RESULTS[key][1]))) / mp.sqrt(2)
    u_star = mp.findroot(lambda u: mp.diff(vline, u), u0, tol=mp.mpf(10) ** -50)
    say("  %-8s Gamma-X closed line: v_max = %s at |k|a = sqrt2*u* = %s" % (
        key, mp.nstr(vline(u_star), 25), mp.nstr(mp.sqrt(2) * u_star, 20)))

# k->0 sound speeds of the z=8 laws (anisotropy)
say("-" * 78)
for d, nm in ((np.array([1.0, 0, 0]), "tetragonal x (= cubic [110])"), (np.array([0, 0, 1.0]), "tetragonal z (= cubic [001])")):
    h = 1e-6
    th = Aprim @ (h * d)
    gb, _ = gam_and_grad(th)
    eps = float(alpha0) * (8 - gb)
    E = np.sqrt(eps * (eps + 2 * float(alpha0)))
    say("BH-AZ7 k->0 sound speed along %s: %.10f c" % (nm, E / h))
say("  => the z=8 (gamma(k)) laws are anisotropic at O(k^2): c_s(z)/c_s(x) = sqrt2, and c_s << c.")

# ---------------------------------------------------------------- 4. lattice front
say("")
say("=" * 78)
say("4. LATTICE FRONT: retarded Green's function G = IFFT[ sin(w t)/w ] along a1")
say("=" * 78)
N = 128
m = np.fft.fftfreq(N) * N
TH = np.stack(np.meshgrid(2 * np.pi * m / N, 2 * np.pi * m / N, 2 * np.pi * m / N, indexing="ij"), axis=-1)
LAM, _ = lam_and_grad(TH)


def green(w, t):
    with np.errstate(divide="ignore", invalid="ignore"):
        Gk = np.where(w > 0, np.sin(w * t) / np.where(w > 0, w, 1), t)
    return np.real(np.fft.ifftn(Gk))


for law, t in (("W", 8.0), ("B-C1", 4.0), ("GW-L73", 8.0)):
    L = LAWS[law]
    w = L["F"](LAM, L["p"])
    G = green(w, t)
    vmax = float(RESULTS[law][0])
    rc = vmax * t
    gmax = np.max(np.abs(G))
    say("-" * 78)
    say("[%s] t = %.1f a/c, v_max = %.6f c, cone radius v_max t = %.3f a; max|G| = %.3e" % (law, t, vmax, rc, gmax))
    rows = []
    for r in range(0, 60):
        g = abs(G[r % N, 0, 0])
        rows.append((r, g))
    prev = None
    for r, g in rows:
        if r >= int(rc) - 2 and (r - int(rc)) % 2 == 0 and r <= int(rc) + 26:
            note = "inside" if r < rc else "OUTSIDE cone"
            say("    r = %2d a   |G| = %.3e   (%s)%s" % (r, g, note, "  [~float floor]" if g < 1e-16 * gmax * 10 else ""))
    # decay law outside the cone: fit log|G| ~ -p r log r + q r
    rs = np.array([r for r, g in rows if r > rc + 1 and g > 1e-14 * gmax])
    gs = np.array([g for r, g in rows if r > rc + 1 and g > 1e-14 * gmax])
    if len(rs) >= 4:
        Afit = np.vstack([rs * np.log(rs), rs, np.ones_like(rs)]).T
        coef = np.linalg.lstsq(Afit, np.log(gs), rcond=None)[0]
        say("    fit outside cone: ln|G| = %.3f r ln r + %.3f r + %.2f  (r ln r term < 0 => superexponential)" % tuple(coef))
say("No strict front on the lattice for ANY law: a continuous-time evolution generated by a")
say("bounded nearest-neighbour operator gives G(r,t) entire in t and nonzero at every r for t>0,")
say("but outside the cone it decays faster than any exponential (Lieb-Robinson / Bessel-type).")
say("Continuum: W and KG have a strict front at c; Bogoliubov and GW-L73 have none.")

with open(sys.argv[1] if len(sys.argv) > 1 else "pilot_dispersion_output.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
