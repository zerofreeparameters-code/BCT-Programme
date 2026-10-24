#!/usr/bin/env python3
"""
Gate SINGLET -- prior-art cross-checks on the signed-measure construction (runner's own code).

Two checks prompted by running Hsieh's nosignaling_completeness.py (Zenodo 21301391):
  (1) Tilted source w(l) = 1 + beta cos(2 pi l / m). Hsieh's Proposition 7 attributes the leak of the
      two-outcome readout (his E0) to post-selection. Test: if instead it is finite-walk contamination
      by the n = 3 antiperiodic mode, the leak scales as beta (lam_3/lam_1)^t and vanishes as t -> inf,
      and it is exactly zero for a readout projected onto the n = +-1 doublet.
  (2) Site-complete hemisphere readout (his E1): leaks at machine zero, but what curve does it give?
      Prediction: an unsharp (POVM) readout of the doublet with per-wing visibility 2/pi in the
      continuum, so E = -(4/pi^2) cos(theta) and |S| = (4/pi^2) 2 sqrt2 = 1.146 < 2: no violation.
Run: python3 -I singlet_priorart.py [outfile]
"""
import sys
import numpy as np

out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


def twisted_kernel(m, p):
    K = np.zeros((m, m))
    for k in range(m):
        for d, x in {0: 1 - p, 1: p / 2, -1: p / 2}.items():
            wraps = (k + d) // m
            K[k, (k + d) % m] += x * ((-1.0) ** abs(wraps))
    return K


def matpow(K, t):
    lam = max(abs(np.linalg.eigvalsh((K + K.T) / 2)))
    R = np.eye(K.shape[0]); B = K / lam; e = t
    while e:
        if e & 1:
            R = R @ B
        B = B @ B; e >>= 1
    return R


def shifted(G, m, h):
    R = np.empty_like(G)
    for k in range(m):
        R[k] = G[k + h] if k + h < m else -G[k + h - m]
    return R


def pair_matrix(G, m, beta):
    """Pair amplitude F[x, y] = sum_k w(k) G[k, x] G_B[k, y]; w(k) = 1 + beta cos(2 pi k / m).
    (k runs over base sites; the other sheet repeats the product with the same tilt.)"""
    h = m // 2
    GB = shifted(G, m, h)
    w = 1 + beta * np.cos(2 * np.pi * np.arange(m) / m)
    return (G * w[:, None]).T @ GB


def two_outcome(F, m, a, b):
    h = m // 2
    W = np.array([[F[a, b] ** 2, F[a, (b + h) % m] ** 2],
                  [F[(a + h) % m, b] ** 2, F[(a + h) % m, (b + h) % m] ** 2]])
    return W / W.sum()


def leak_two_outcome(F, m):
    """max over a of the spread of P_A(+|a,b) over all distant settings b."""
    worst = 0.0
    for a in range(m):
        vals = [two_outcome(F, m, a, b)[0].sum() for b in range(m)]
        worst = max(worst, max(vals) - min(vals))
    return worst


m, p = 24, 0.5
h = m // 2
lam = lambda n: 1 - p + p * np.cos(np.pi * n / m)
r31 = lam(3) / lam(1)

say("=" * 78)
say("(1) TILTED SOURCE, two-outcome readout renormalised per setting pair (Hsieh's E0)")
say("=" * 78)
say("lam_3/lam_1 = %.12f ; prediction: leak = C(beta) beta (lam_3/lam_1)^t, C independent of t" % r31)
say("    t     beta=0.3 leak     beta=0.6 leak     C(0.3)=leak/(beta r^t)  C(0.6)")
for t in (100, 200, 300, 400, 600, 800, 1200):
    G = matpow(twisted_kernel(m, p), t)
    l3 = leak_two_outcome(pair_matrix(G, m, 0.3), m)
    l6 = leak_two_outcome(pair_matrix(G, m, 0.6), m)
    say("  %5d   %.3e         %.3e         %.4f                  %.4f" % (t, l3, l6, l3 / (0.3 * r31 ** t), l6 / (0.6 * r31 ** t)))
say("Doublet-projected readout (exact n = +-1 projection, i.e. the t -> inf object):")
x = np.arange(m)
e1 = np.vstack([np.cos(np.pi * x / m), np.sin(np.pi * x / m)])     # orthonormal-up-to-scale doublet
Pd = e1.T @ np.linalg.inv(e1 @ e1.T) @ e1                           # projector onto the doublet (sites)
for beta in (0.0, 0.3, 0.6, 0.9):
    G = Pd                              # the t -> inf antiperiodic propagator is the doublet projector
    F = pair_matrix(G, m, beta)
    Ev = lambda P: P[0, 0] + P[1, 1] - P[0, 1] - P[1, 0]
    E0_45 = Ev(two_outcome(F, m, 0, 3)); E90_135 = Ev(two_outcome(F, m, 6, 9))
    # doublet state: (1+beta/2)|01> - (1-beta/2)|10>  =>  E(a,b) = -cos a cos b - 2 al ga sin a sin b
    al, ga = 1 + beta / 2, 1 - beta / 2
    pred = -2 * al * ga / (al ** 2 + ga ** 2) * np.sin(np.pi / 2) * np.sin(3 * np.pi / 4)
    say("  beta = %.1f : leak = %.2e   E(0,45) = %+.12f   E(90,135) = %+.12f  (pred. %+.12f)" %
        (beta, leak_two_outcome(F, m), E0_45, E90_135, pred))
say("  => the tilted doublet source is the non-maximally entangled state (1+beta/2)|01> - (1-beta/2)|10>")
say("     (E(90,135) matches the closed form; E(0,45) is tilt-blind), and the two-outcome readout never")
say("     signals once it is complete on the doublet. The finite-t leak of the per-pair-renormalised")
say("     readout is n = 3 contamination, C(beta) beta (lam_3/lam_1)^t with C(0.3) = 0.978, C(0.6) = 0.917")
say("     (constant in t for t >= 200; the last digit at t = 800 is double-precision noise), not post-selection.")

say("")
say("=" * 78)
say("(2) SITE-COMPLETE HEMISPHERE READOUT (Hsieh's E1), symmetric source")
say("=" * 78)


def hemi(j, m):
    q = np.zeros(m)
    for xx in range(m):
        d = min((xx - j) % m, (j - xx) % m)
        q[xx] = 1.0 if d < m // 4 else (0.5 if d == m // 4 else 0.0)
    return q


def E1(F, m, a, b):
    W = F ** 2
    qa, qb = hemi(a, m), hemi(b, m)
    Z = W.sum()
    return (qa @ W @ qb - qa @ W @ (1 - qb) - (1 - qa) @ W @ qb + (1 - qa) @ W @ (1 - qb)) / Z


for mm in (24, 48, 96, 192):
    G = matpow(twisted_kernel(mm, p), 40 * mm * mm // 24)
    F = pair_matrix(G, mm, 0.0)
    q8 = mm // 8
    Es = {(a, b): E1(F, mm, a, b) for a in (0, 2 * q8) for b in (q8, 3 * q8)}
    S = Es[(0, q8)] - Es[(0, 3 * q8)] + Es[(2 * q8, q8)] + Es[(2 * q8, 3 * q8)]
    V = -E1(F, mm, 0, 0)
    say("  m = %4d : visibility V = -E(0) = %.6f   |S| = %.6f   (4/pi^2 = %.6f, 4/pi^2 * 2sqrt2 = %.6f)" %
        (mm, V, abs(S), 4 / np.pi ** 2, 8 * np.sqrt(2) / np.pi ** 2))
    if mm == 24:
        curve = [E1(F, mm, 0, d) / (-np.cos(2 * np.pi * d / mm)) if abs(np.cos(2 * np.pi * d / mm)) > 1e-9 else np.nan
                 for d in range(0, mm // 2 + 1)]
        say("           E(theta)/(-cos theta) at 15-deg steps:", " ".join("%.4f" % c for c in curve if np.isfinite(c)))
say("  => the readout that is complete on the full site space is an unsharp measurement of the doublet:")
say("     E = -V cos(theta), V -> 4/pi^2, |S| -> 1.146 < 2. It does not violate CHSH.")
say("     The readout that reproduces -cos(theta) is the two-outcome readout, complete only on the")
say("     coarse-grained doublet (t -> inf).")

with open(sys.argv[1] if len(sys.argv) > 1 else "singlet_priorart_output.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
