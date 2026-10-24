#!/usr/bin/env python3
"""
Gate SINGLET -- Steps 1-3 on BCT's own variables (runner's own code).

Card Sec.4 asks for the construction on BCT variables only if (i)-(iii) are all supplied. They are
not (see RESULT Sec.4). This script therefore does three narrower things:

  A. S^1 branch (the written complex scalar Psi = sqrt(rho) e^{i theta}; AZ6 eq:SGP, App J eq:action,
     Letter 60, AZ7 Thm 'Scalar order parameter').
     A1. Functions of a single-valued Psi on the phase circle carry integer charges q only: a register
         built on theta (including a vortex frame, where rotation by alpha about the axis shifts theta
         by H*alpha) gets the holonomy e^{2 pi i q} = +1 per turn -> periodic sector only.
     A2. The construction with q = H = 1 (written) and with q = 1/2 (added) -- curves and CHSH.
     A3. A half-quantum vortex Psi ~ e^{i phi/2} is not single-valued (checked).
  B. Does any BCT number change the curve? Run the construction with BCT-derived choices for the
     free inputs (laziness p = alpha_0, m tied to coordination 8 or to 24) -- the limit is identical,
     so no BCT input enters the result.
  C. C^2 branch (App JH: Psi_2 : B^3(R_s) -> C^2, |psi_+|^2 + |psi_-|^2 = rho_0).
     C1. The unit field lies in S^3, not S^2; the Hopf map n = chi^dag sigma chi lands in S^2.
     C2. The real-spinor circle chi(psi) = (cos psi/2, sin psi/2) double-covers a great circle of
         Bloch vectors; chi(psi + 2 pi) = -chi(psi) automatically (antiperiodicity is forced, not chosen).
     C3. Built on that circle, with an ADDED walk and an ADDED squared (Born) readout, the construction
         reproduces -cos(theta); with a linear readout it does not give probabilities.
Run: python3 -I singlet_step3.py [outfile]
"""
import sys
import numpy as np

out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


TAU = 2 * np.pi
ALPHA0 = (np.sqrt(2) - 1) / 2 * (np.sqrt(6) - 2) / 4 / np.pi      # r_oct r_tet / pi


def sector_kernel(m, p, q):
    """Lazy NN walk on the m-site base circle; a step across the seam carries the holonomy
    exp(2 pi i q). q integer -> +1 (periodic); q half-odd -> -1 (antiperiodic)."""
    hol = np.cos(TAU * q)          # real for q in Z/2
    K = np.zeros((m, m))
    for k in range(m):
        for d, x in {0: 1 - p, 1: p / 2, -1: p / 2}.items():
            wraps = (k + d) // m
            K[k, (k + d) % m] += x * (hol ** abs(wraps))
    return K, hol


def matpow(K, t):
    lam = max(abs(np.linalg.eigvalsh((K + K.T) / 2)))
    R = np.eye(K.shape[0]); B = K / lam; e = t
    while e:
        if e & 1:
            R = R @ B
        B = B @ B; e >>= 1
    return R


def curve(m, p, t, q):
    K, hol = sector_kernel(m, p, q)
    G = matpow(K, t)
    h = m // 2
    GB = np.empty_like(G)
    for k in range(m):
        GB[k] = G[k + h] if k + h < m else hol * G[k + h - m]
    E = np.zeros((m, m)); N = np.zeros((m, m)); mA = np.zeros((m, m))
    for a in range(m):
        for b in range(m):
            W = np.array([[np.dot(G[:, a], GB[:, b]), np.dot(G[:, a], GB[:, (b + h) % m])],
                          [np.dot(G[:, (a + h) % m], GB[:, b]), np.dot(G[:, (a + h) % m], GB[:, (b + h) % m])]]) ** 2
            N[a, b] = W.sum(); P = W / N[a, b]
            E[a, b] = P[0, 0] + P[1, 1] - P[0, 1] - P[1, 0]
            mA[a, b] = P[0].sum()
    q8 = m // 8
    S = E[0, q8] - E[0, 3 * q8] + E[2 * q8, q8] + E[2 * q8, 3 * q8]
    th = np.array([[TAU * ((b - a) % m) / m for b in range(m)] for a in range(m)])
    return E, S, np.abs(E + np.cos(th)).max(), max(np.ptp(mA[a]) for a in range(m)), np.ptp(N) / N.mean()


def t_for(m, p, tol=1e-14):
    lam = lambda n: 1 - p + p * np.cos(np.pi * n / m)
    return int(np.ceil(np.log(tol) / (2 * np.log(lam(3) / lam(1))))) + 1


say("=" * 78)
say("A. S^1 BRANCH -- the written complex scalar")
say("=" * 78)
say("A1. Single-valued Psi = sqrt(rho) e^{i theta}: functions of theta are e^{i q theta}, q in Z.")
say("    Vortex frame (Letter 60 profile, Psi = f(r) e^{i H phi}): rotating by alpha about the axis gives")
say("    Psi -> e^{-i H alpha} Psi, so a 2 pi rotation multiplies by e^{-2 pi i H} = +1 for every H in Z.")
for H in (1, 2, -1):
    say("      H = %+d : holonomy per turn = %+.1f  (periodic sector)" % (H, np.cos(TAU * H)))
say("A2. The construction on the written register (q = 1) versus with an added half-charge (q = 1/2):")
m, p = 24, 0.5
for q, label in ((1.0, "q = 1   (written: vortex frame / theta itself)"), (0.5, "q = 1/2 (ADDED: double cover, antiperiodic sector)")):
    t = 3200
    E, S, dE, sig, Nv = curve(m, p, t, q)
    say("    %-52s t=%d: |S| = %.12f  max|E+cos| = %.3e  max|E| = %.3e  marg var = %.1e  relvar N = %.1e"
        % (label, t, abs(S), dE, np.abs(E).max(), sig, Nv))
say("A3. Half-quantum vortex: Psi(phi) = f e^{i phi/2} on a loop around the core:")
phi = np.linspace(0, TAU, 9)
psi = np.exp(1j * phi / 2)
say("    Psi(0) = %s, Psi(2 pi) = %s -> jump %s: not single-valued, so not a configuration of the written"
    % (np.round(psi[0], 12), np.round(psi[-1], 12), np.round(psi[-1] - psi[0], 12)))
say("    scalar field (pi_1(S^1) = Z: integer winding only).")

say("")
say("=" * 78)
say("B. DOES ANY BCT NUMBER CHANGE THE CURVE?  (S^1 register with the q = 1/2 sector ADDED)")
say("=" * 78)
say("alpha_0 = r_oct r_tet / pi = %.15f" % ALPHA0)
for (mm, pp, why) in ((24, 0.5, "reference (Hsieh's m, p)"),
                      (24, ALPHA0, "laziness p = alpha_0 (AZ7 Lemma: hopping t = alpha_0)"),
                      (8, ALPHA0, "m = 8 (z = 8 coordination), p = alpha_0"),
                      (48, 2 * ALPHA0, "m = 48, p = 2 alpha_0")):
    t = t_for(mm, pp)
    E, S, dE, sig, Nv = curve(mm, pp, t, 0.5)
    say("  %-55s m=%2d t=%7d: max|E+cos| = %.1e  |S| = %.15f  relvar N = %.1e" % (why, mm, t, dE, abs(S), Nv))
say("  => identical limit for every choice: m, p (and t) are regulators. No BCT quantity (r_oct, r_tet,")
say("     alpha_0, xi/a, z) enters E(theta); BCT inputs change only the convergence rate.")

say("")
say("=" * 78)
say("C. C^2 BRANCH -- App JH's two-component interior field")
say("=" * 78)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
rng = np.random.default_rng(20261025)
v = rng.normal(size=(5, 4)); v /= np.linalg.norm(v, axis=1, keepdims=True)
chis = v[:, :2] + 1j * v[:, 2:]
say("C1. Unit C^2 vectors: |chi|^2 =", np.round(np.sum(np.abs(chis) ** 2, axis=1), 12),
    "-> 4 real components on the unit sphere: S^3.")
nvec = np.array([[np.real(c.conj() @ s @ c) for s in (sx, sy, sz)] for c in chis])
say("    Hopf map n = chi^dag sigma chi: |n| =", np.round(np.linalg.norm(nvec, axis=1), 12), "-> S^2.")
say("    So the field Psi_2/|Psi_2| has target S^3 (pi_3(S^3) = Z, pi_1(S^3) = 0); 'S^3 -> S^2' in App JH")
say("    is the Hopf projection n, not the field map. On the domain B^3(R_s) an integer invariant exists")
say("    only with a constant boundary value (compactification to S^3), which App JH does not impose.")
say("C2. Real-spinor circle chi(psi) = (cos psi/2, sin psi/2):")
for ps in (0.0, np.pi / 2, np.pi, 2 * np.pi):
    c = np.array([np.cos(ps / 2), np.sin(ps / 2)], complex)
    n = [np.real(c.conj() @ s @ c) for s in (sx, sy, sz)]
    say("    psi = %5.3f : chi = %s   n = (%+.3f, %+.3f, %+.3f)" % (ps, np.round(c.real, 6), *n))
say("    n(psi) = (sin psi, 0, cos psi): the spinor circle double-covers the x-z great circle and")
say("    chi(psi + 2 pi) = -chi(psi): antiperiodicity is automatic for a C^2 field (the SU(2) centre -1).")
say("    |<chi(a)|chi(b)>| = |cos((a-b)/2)| -- the spin-1/2 overlap (checked):",
    all(abs(abs(np.cos(a / 2) * np.cos(b / 2) + np.sin(a / 2) * np.sin(b / 2)) - abs(np.cos((a - b) / 2))) < 1e-15
        for a, b in rng.uniform(0, TAU, (1000, 2))))
say("C3. Construction on the spinor circle: walker position psi_k on the 2m-site circle (ADDED walk),")
say("    readout amplitude <chi(a_A)|chi(psi)> (the spinor component itself, no projection needed),")
say("    joint amplitude summed over source framing, squared (ADDED Born readout):")
mm = 24
psi_k = TAU * np.arange(2 * mm) / mm                        # 2m sites, [0, 4 pi)
def comp(ang, ps):                                          # <chi(ang)|chi(ps)>, real
    return np.cos(ang / 2) * np.cos(ps / 2) + np.sin(ang / 2) * np.sin(ps / 2)
# lazy walk kernel on the 2m circle, long-time; amplitude for wing = sum_y K^t(k,y) <chi(a)|chi(psi_y)>
K = np.zeros((2 * mm, 2 * mm))
for k in range(2 * mm):
    for d, x in {0: 0.5, 1: 0.25, -1: 0.25}.items():
        K[k, (k + d) % (2 * mm)] += x
lam1 = 0.5 + 0.5 * np.cos(np.pi / mm)
t = t_for(mm, 0.5)
Kt = np.linalg.matrix_power(K / lam1, t)                    # even mode grows, but it is annihilated below
Emax = 0.0; margv = 0.0
Etab = {}
for a in range(mm):
    for b in range(mm):
        aa, bb = TAU * a / mm, TAU * b / mm
        amps = np.zeros((2, 2))
        for iA, A in enumerate((aa, aa + np.pi)):
            for iB, B in enumerate((bb, bb + np.pi)):
                uA = Kt @ comp(A, psi_k)
                uB = Kt @ comp(B, np.roll(psi_k, -mm // 2))   # B starts a half-turn away
                amps[iA, iB] = np.dot(uA, uB)
        W = amps ** 2; P = W / W.sum()
        Etab[(a, b)] = P[0, 0] + P[1, 1] - P[0, 1] - P[1, 0]
        Emax = max(Emax, abs(Etab[(a, b)] + np.cos(bb - aa)))
for a in range(mm):
    vals = []
    for b in range(mm):
        aa, bb = TAU * a / mm, TAU * b / mm
        amps = np.zeros((2, 2))
        for iA, A in enumerate((aa, aa + np.pi)):
            for iB, B in enumerate((bb, bb + np.pi)):
                amps[iA, iB] = np.dot(Kt @ comp(A, psi_k), Kt @ comp(B, np.roll(psi_k, -mm // 2)))
        W = amps ** 2
        vals.append(W[0].sum() / W.sum())
    margv = max(margv, np.ptp(vals))
q8 = mm // 8
S = Etab[(0, q8)] - Etab[(0, 3 * q8)] + Etab[(2 * q8, q8)] + Etab[(2 * q8, 3 * q8)]
say("    t = %d: max|E + cos| over 576 pairs = %.2e ; |S| = %.12f ; marginal variation = %.1e" % (t, Emax, abs(S), margv))
aa, bb = 0.0, np.pi / 4
lin = np.array([[np.dot(Kt @ comp(A, psi_k), Kt @ comp(B, np.roll(psi_k, -mm // 2))) for B in (bb, bb + np.pi)]
                for A in (aa, aa + np.pi)])
say("    linear (unsquared) readout at (0, 45deg), normalised:", np.array2string(lin / lin.sum(), precision=6).replace("\n", ""),
    "-> negative entries")
say("    The walk is inert here: the readout vector <chi(a)|chi(psi)> is already the pure n = +-1 harmonic,")
say("    so K^t only rescales it. On this branch the spinor overlap does the filtering the walk does on S^1.")
say("    => on the C^2 branch the Z2 sign (ii) comes with the field, but the walk (i), the readout")
say("       rule (iii), the source framing and the setting-to-SU(2) identification are all still added.")

say("")
say("=" * 78)
say("D. LATTICE POINT GROUP AND SPIN STRUCTURES (candidate (ii): 'a spin structure fixed by the point group')")
say("=" * 78)
import itertools
a_, c_ = 1.0, np.sqrt(2.0)                       # c/a = sqrt2; a = in-plane spacing
pts = []
for i, j, k in itertools.product(range(-3, 4), repeat=3):
    pts.append((i * a_, j * a_, k * c_))
    pts.append(((i + .5) * a_, (j + .5) * a_, (k + .5) * c_))
pts = np.array(pts)
d = np.linalg.norm(pts, axis=1)
shells = np.unique(np.round(d[d > 1e-9], 9))[:3]
NN = pts[np.abs(d - shells[0]) < 1e-9]
say("body-centred tetragonal, c/a = sqrt2: first shells at", shells, "; nearest-neighbour count =", len(NN))
# brute-force the point group: orthogonal maps sending the NN set to itself
def frame(u, v):
    w = np.cross(u, v)
    return np.column_stack([u, v, w])
v1 = NN[0]
v2 = [v for v in NN if abs(np.dot(v, v1) - 0.5) < 1e-9][0]          # 60 degrees
F0 = frame(v1, v2)
ops = []
key = lambda X: tuple(sorted(map(tuple, np.round(X, 6))))
NNkey = key(NN)
for w1 in NN:
    for w2 in NN:
        if abs(np.dot(w1, w2) - 0.5) > 1e-9:
            continue
        for sgn in (1, -1):
            F1 = frame(w1, w2); F1[:, 2] *= sgn
            R = F1 @ np.linalg.inv(F0)
            if np.allclose(R @ R.T, np.eye(3), atol=1e-9) and key((R @ NN.T).T) == NNkey:
                if not any(np.allclose(R, Q) for Q in ops):
                    ops.append(R)
has3 = any(abs(np.trace(R) - 0.0) < 1e-9 and abs(np.linalg.det(R) - 1) < 1e-9 for R in ops)
inv = any(np.allclose(R, -np.eye(3)) for R in ops)
say("point group order = %d ; contains inversion: %s ; contains a 3-fold rotation: %s" % (len(ops), inv, has3))
say("  => order 48 with 3-fold axes = O_h: the c/a = sqrt2 BCT lattice is fcc. AZ7 Sec.'Argument 3' uses")
say("     C_4v (order 8, no inversion); the Bravais lattice's holohedry is O_h, which contains D_4h and C_4v.")
say("  C_4v 'E' irrep (AZ7 Lemma 'Spinor excluded') is the single-valued 2D rep; its C_4 matrix:")
C4 = np.array([[0, -1], [1, 0]])
say("    C4 =", C4.tolist(), "; C4^4 =", np.linalg.matrix_power(C4, 4).tolist(),
    "(= +identity: single-valued, not a spinor; spinor irreps belong to the double group, where C4^4 = -1)")
# spin structures on T^3 = R^3 / Lambda (primitive fcc lattice): homomorphisms Lambda -> Z2
P = np.array([NN[0], [v for v in NN if abs(np.dot(v, NN[0]) - 0.5) < 1e-9][0]])
cands = [v for v in NN if abs(np.linalg.det(np.vstack([P, v]))) > 1e-6]
B = np.vstack([P, cands[0]])                      # primitive basis (rows)
def coords(v):
    return np.round(np.linalg.solve(B.T, v)).astype(int)
def invariant_structures(group):
    found = []
    for f in itertools.product((0, 1), repeat=3):
        fv = np.array(f)
        if all((coords(v) @ fv) % 2 == (coords(R @ v) @ fv) % 2 for R in group for v in NN):
            found.append(f)
    return found
ez = np.array([0, 0, 1.0])
subgroups = {
    "O_h (full, order %d)" % len(ops): ops,
    "O (proper rotations)": [R for R in ops if np.linalg.det(R) > 0],
    "D_4h (preserve z-axis)": [R for R in ops if np.allclose(np.abs(R @ ez), ez)],
    "C_4v (fix +z, as in AZ7)": [R for R in ops if np.allclose(R @ ez, ez)],
}
say("spin structures on the lattice torus R^3/Lambda: homomorphisms Lambda -> Z2 (sign of each lattice")
say("  translation's lift), 8 in all; f = (0,0,0) is the trivial, all-periodic one. Invariant under:")
for nm, Gp in subgroups.items():
    inv_f = invariant_structures(Gp)
    desc = []
    for f in inv_f:
        fv = np.array(f)
        val = lambda v: int((coords(np.array(v)) @ fv) % 2)
        desc.append("f(a=(1,0,0))=%d f(body=(1/2,1/2,c/2))=%d f(c=(0,0,c))=%d" %
                    (val([1, 0, 0]), val([0.5, 0.5, c_ / 2]), val([0, 0, c_])))
    say("    %-28s |G| = %2d : %d invariant -> %s" % (nm, len(Gp), len(inv_f), "; ".join(desc)))
say("  => the full lattice point group fixes the spin structure uniquely, and fixes it to the TRIVIAL")
say("     (periodic) one; only a reduced subgroup (C_4v, D_4h) leaves room for antiperiodic choices, and")
say("     then the choice is free. Either way the lattice does not supply an antiperiodic sector, and a")
say("     spin structure of space acts on spatial loops, not on the internal phase register.")

say("")
say("=" * 78)
say("E. APP JH FREE ENERGY UNDER ITS OWN CONSTRAINT |Psi_2|^2 = rho_0 (side finding)")
say("=" * 78)
say("With |Psi_2|^2 = rho_0 fixed, the |Psi|^4 and surface terms of eq:free-energy are constants, so")
say("F = const + (hbar^2 rho_0 / 2m) * D, D = integral |grad chi|^2 over B^3(R_s), chi = Psi_2/sqrt(rho_0) in S^3.")
say("Degree-1 radial texture of size eps (chi = (sin g(r) rhat, cos g(r)), g: pi -> 0 on [0, eps], constant outside):")
from scipy.integrate import quad
def D_of(eps):
    g = lambda r: np.pi * (1 - r / eps)
    gp = -np.pi / eps
    dens = lambda r: (gp ** 2 + 2 * np.sin(g(r)) ** 2 / r ** 2) * 4 * np.pi * r ** 2
    return quad(dens, 1e-12, eps, limit=200)[0]
for eps in (1.0, 0.5, 0.25, 0.125):
    say("    eps/R_s = %.3f : D = %.6f   D/eps = %.6f" % (eps, D_of(eps), D_of(eps) / eps))
say("  => D scales as eps: the degree-1 (Hopf-charge-1 after projection) class has infimum equal to the")
say("     uniform (H = 0) value and no minimiser. The written F does not select H = 1; App JH's selection")
say("     rests on eq:hopf-matching (a net current out of a closed surface), which is not part of F.")

with open(sys.argv[1] if len(sys.argv) > 1 else "singlet_step3_output.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
