#!/usr/bin/env python3
"""
Gate SINGLET -- Step 0: baseline and positive control.

Card: audit/gates/gate_SINGLET_prompt.md @ fc4b632,
SHA-256 272dca3d944518233b2f8e1846f179974fccfd1290006d3ed9dc8dfcb94ed16e.

Written BEFORE reading Hsieh's paper or code (card Sec.1: "re-implement ... independently").
The construction follows only the card's one-line description:
  "a lazy nearest-neighbour walk on a 2m-site double cover of an m-site phase circle,
   antiperiodic projection, sum over source framing, squared readout".

Construction (runner's own reading of that description)
------------------------------------------------------
  base circle   : m sites, phi_j = 2 pi j / m                (m even; m = 24 -> 15 deg steps)
  double cover  : 2m sites, psi_k = 2 pi k / m in [0, 4 pi),  projection j = k mod m
  walk          : lazy nearest-neighbour Markov kernel on the 2m-cycle,
                  K[k,k] = 1-p, K[k,k+-1] = p/2   (non-negative, local, row-stochastic)
  Z2 sign       : signed endpoint count  G_t(k, j) = K^t[k, j] - K^t[k, j+m]
                  (+1 if the walker ends on the same sheet as the lift of j, -1 on the other sheet)
                  = antiperiodic projection of the walk = (-1)^(winding parity) on the base circle
  source        : walker A starts at k, walker B at k + m/2 (half-turn on the base circle);
                  the source framing k is summed over all 2m double-cover sites, uniformly
  setting a     : base site j_a; outcome +1 -> j_a, outcome -1 -> j_a + m/2
  amplitude     : M(A,B | a,b) = sum_k G_t(k, j_a(A)) * G_t(k + m/2, j_b(B))
  readout       : P(A,B | a,b) = M^2 / sum_{A',B'} M^2        (squared readout of the signed sum)

Ablations (card: "dropping the Z2 sign, or the squaring, loses the violation"):
  noZ2       : periodic sector, G = K^t[k,j] + K^t[k,j+m] (the plain walk on the base circle), squared
  linear     : Z2 sign kept, no squaring: "P" = M / sum M -> shown not to be a probability
  signLHV    : Z2 sign kept, squaring replaced by a local readout A = sign G_t(k, j_a) at each wing,
               mixture over k  (a local-hidden-variable model by construction)
  power p    : readout |M|^p (p != 2) -- tests whether non-negativity alone forces the square
  kernels    : next-nearest-neighbour and wide kernels -- tests dependence on the walk itself
Run: python3 -I singlet_step0.py [outfile]
"""
import sys
import itertools
import numpy as np
import mpmath as mp

out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


TAU = 2 * np.pi

# ============================================================== 1. 16 local strategies
say("=" * 78)
say("1. BASELINE: the 16 deterministic local strategies")
say("=" * 78)
best, count = 0, 0
for A0, A1, B0, B1 in itertools.product((1, -1), repeat=4):
    S = A0 * B0 - A0 * B1 + A1 * B0 + A1 * B1
    best = max(best, abs(S))
    count += 1
say("strategies enumerated:", count, "  max |S| =", best,
    "  (S = E(a,b) - E(a,b') + E(a',b) + E(a',b'); convex hull => every LHV mixture has |S| <= 2)")


# ============================================================== 2. the construction
def offsets(p, kind="nn"):
    """Non-negative, rotation-invariant, row-stochastic step distribution."""
    if kind == "nn":                      # lazy nearest-neighbour
        return {0: 1 - p, 1: p / 2, -1: p / 2}
    if kind == "nnn":                     # lazy, nearest + next-nearest
        return {0: 1 - p, 1: p / 3, -1: p / 3, 2: p / 6, -2: p / 6}
    if kind == "wide":                    # binomial kernel, range 3
        c = np.array([1, 6, 15, 20, 15, 6, 1], float)
        c /= c.sum()
        return {d: c[d + 3] for d in range(-3, 4)}
    raise ValueError(kind)


def cover_kernel(m, p, kind="nn"):
    """The walk itself: non-negative kernel on the 2m-site double cover."""
    K = np.zeros((2 * m, 2 * m))
    for k in range(2 * m):
        for d, x in offsets(p, kind).items():
            K[k, (k + d) % (2 * m)] += x
    return K


def twisted_kernel(m, p, kind="nn", sector="anti"):
    """The same walk reduced to the m-site base circle in one Z2 sector: a step that crosses the
    seam (sheet change) carries the holonomy -1 (antiperiodic) or +1 (periodic).
    Equivalent to K_cover[k,j] -/+ K_cover[k,j+m]; computing in the sector avoids the
    catastrophic cancellation of the even modes."""
    sgn = -1.0 if sector == "anti" else 1.0
    K = np.zeros((m, m))
    for k in range(m):
        for d, x in offsets(p, kind).items():
            wraps = (k + d) // m          # number of seam crossings (0, +1 or -1)
            K[k, (k + d) % m] += x * (sgn ** abs(wraps))
    return K


def matpow(K, t):
    """K^t / lam^t, lam = largest |eigenvalue| (only ratios matter after normalisation)."""
    lam = max(abs(np.linalg.eigvalsh((K + K.T) / 2)))
    R = np.eye(K.shape[0])
    B = K / lam
    e = t
    while e:
        if e & 1:
            R = R @ B
        B = B @ B
        e >>= 1
    return R, lam


def G_sector(m, p, t, kind="nn", sector="anti"):
    """G[k, j]: signed (anti) or unsigned (peri) walk count from base site k to base site j."""
    Gt, _ = matpow(twisted_kernel(m, p, kind, sector), t)
    return Gt


def rows_shifted(G, m, h, sector):
    """Row k -> row of the double-cover site k + h, expressed on base sites (sheet sign)."""
    sgn = -1.0 if sector == "anti" else 1.0
    R = np.empty_like(G)
    for k in range(m):
        kk = k + h
        R[k] = G[kk] if kk < m else sgn * G[kk - m]
    return R


def amplitudes(G, GB, m, ja, jb):
    """M[A,B], A,B in (+1,-1) -> (0,1). Source framing summed over base sites k (the other sheet
    gives the same product, both factors flipping together). Walker A starts at k, B at k + m/2."""
    h = m // 2
    M = np.zeros((2, 2))
    for iA, jA in enumerate((ja, (ja + h) % m)):
        for iB, jB in enumerate((jb, (jb + h) % m)):
            M[iA, iB] = np.dot(G[:, jA], GB[:, jB])
    return M


def probs(M, power=2.0):
    W = np.abs(M) ** power
    N = W.sum()
    if N == 0:
        return np.full((2, 2), np.nan), 0.0
    return W / N, N


def E_of(P):
    return P[0, 0] + P[1, 1] - P[0, 1] - P[1, 0]


def run(m, p, t, sector="anti", kind="nn", power=2.0):
    G = G_sector(m, p, t, kind, sector)
    GB = rows_shifted(G, m, m // 2, sector)
    Etab = np.zeros((m, m)); margA = np.zeros((m, m)); margB = np.zeros((m, m)); Nab = np.zeros((m, m))
    for ja in range(m):
        for jb in range(m):
            M = amplitudes(G, GB, m, ja, jb)
            P, N = probs(M, power)
            Etab[ja, jb] = E_of(P)
            margA[ja, jb] = P[0, :].sum()
            margB[ja, jb] = P[:, 0].sum()
            Nab[ja, jb] = N
    return Etab, margA, margB, Nab, G


def completeness_var(G, m):
    """Local completeness: C_a(k,k') = sum_A u_{a,A}(k) u_{a,A}(k'), u_{a,A}(k) = G[k, j_A].
    A setting-independent C_a is what lets M^2 be a bilinear form in local objects with a
    setting-independent normalisation. Returns max_a ||C_a - mean C|| / ||mean C||."""
    h = m // 2
    Cs = [np.outer(G[:, a], G[:, a]) + np.outer(G[:, (a + h) % m], G[:, (a + h) % m]) for a in range(m)]
    Cm = sum(Cs) / m
    nrm = np.linalg.norm(Cm)
    return max(np.linalg.norm(C - Cm) for C in Cs) / nrm if nrm > 0 else np.nan


def chsh(Etab, m):
    q = m // 8                                   # pi/4 in sites
    a, a2, b, b2 = 0, 2 * q, q, 3 * q            # (0, pi/2, pi/4, 3pi/4)
    return Etab[a, b] - Etab[a, b2] + Etab[a2, b] + Etab[a2, b2]


def summary(tag, m, p, t, **kw):
    Etab, mA, mB, N, G = run(m, p, t, **kw)
    th = np.array([[TAU * ((jb - ja) % m) / m for jb in range(m)] for ja in range(m)])
    dE = np.abs(Etab + np.cos(th)).max()
    S = chsh(Etab, m)
    sigA = max(np.ptp(mA[ja, :]) for ja in range(m))   # variation of A-marginal over distant b
    sigB = max(np.ptp(mB[:, jb]) for jb in range(m))
    Nvar = np.ptp(N) / N.mean() if N.mean() > 0 else np.nan
    return Etab, dict(tag=tag, dE=dE, S=S, sigA=sigA, sigB=sigB, Nvar=Nvar,
                      Cvar=completeness_var(G, m), nundef=int(np.sum(N == 0)))


m, p = 24, 0.5
say("")
say("=" * 78)
say("2. POSITIVE CONTROL  (m = %d base sites, 2m = %d double-cover sites, laziness 1-p = %.2f)" % (m, 2 * m, 1 - p))
say("=" * 78)
lam = lambda n: 1 - p + p * np.cos(np.pi * n / m)
say("Odd (antiperiodic) eigenvalues of the lazy walk: lam_n = 1-p+p cos(pi n/m), n odd")
say("  lam_1 = %.15f   lam_3 = %.15f   lam_3/lam_1 = %.15f" % (lam(1), lam(3), lam(3) / lam(1)))
say("  => at long times the odd sector is the n = +-1 pair, cos(psi/2) and sin(psi/2): half-angle harmonics.")

# consistency: the twisted (seam-sign) kernel equals the double-cover subtraction
Kc = cover_kernel(m, p)
tchk = 60
Kct = np.linalg.matrix_power(Kc, tchk)
Gsub = Kct[:m, :m] - Kct[:m, m:]
Gtw = np.linalg.matrix_power(twisted_kernel(m, p), tchk)
say("check: seam-sign kernel^t vs double-cover K^t[k,j] - K^t[k,j+m] at t = %d: max diff = %.1e" %
    (tchk, np.abs(Gsub - Gtw).max()))
say("       (non-negative walk on the cover + Z2 sign on sheet change = flat Z2 connection on the base circle)")
say("")
say("Convergence in walk length t, all 24 x 24 setting pairs, per-pair normalised readout P = M^2 / N(a,b):")
say("     t   max|E+cos th|   |S|-2sqrt2     max dP_A over b  max dP_B over a  relvar N(a,b)  relvar C_a")
for t in (2, 5, 10, 20, 50, 100, 200, 400, 800, 1600, 3200):
    _, r = summary("anti", m, p, t)
    say("  %5d   %.3e       %+.3e     %.2e         %.2e         %.3e      %.3e" %
        (t, r["dE"], abs(r["S"]) - 2 * np.sqrt(2), r["sigA"], r["sigB"], r["Nvar"], r["Cvar"]))
say("  Note: marginals are exactly 1/2 at EVERY t (the outcome flip a -> a+pi swaps the two terms of")
say("  sum_B M^2), but at short t |S| exceeds 2 sqrt2 (up to 4). That excess is bought by the per-pair")
say("  normalisation N(a,b), which depends on both settings; N and the local completeness C_a become")
say("  setting-independent only as t -> inf, at rate (lam_3/lam_1)^(2t).")
T = 3200
Etab, r = summary("anti", m, p, T)
say("")
say("E(theta) table at t = %d, a = 0, b = theta (13 angles in [0, pi]):" % T)
say("   theta(deg)    E(theta)               -cos(theta)            |dE|")
for jb in range(0, m // 2 + 1):
    thv = TAU * jb / m
    say("   %6.1f      %+.15f    %+.15f    %.1e" % (np.degrees(thv), Etab[0, jb], -np.cos(thv), abs(Etab[0, jb] + np.cos(thv))))
say("CHSH at (a,a',b,b') = (0, pi/2, pi/4, 3pi/4): S = %.15f   (2 sqrt2 = %.15f)" % (r["S"], 2 * np.sqrt(2)))
say("max over all 576 (a,b) of |E + cos(b-a)| = %.2e" % r["dE"])
say("single-wing marginals: max_a [max_b P_A(+|a,b) - min_b P_A(+|a,b)] = %.2e ; B: %.2e" % (r["sigA"], r["sigB"]))
say("normalisation N(a,b): relative variation = %.2e ; local completeness C_a: relative variation = %.2e"
    % (r["Nvar"], r["Cvar"]))

mp.mp.dps = 40
def g_exact(x, t, m, p):
    """antiperiodic propagator at time 2t, site difference x on the double cover (mpmath)."""
    s_ = mp.mpf(0)
    for n in range(1, 2 * m, 2):
        ln = 1 - mp.mpf(p) + mp.mpf(p) * mp.cos(mp.pi * n / m)
        s_ += ln ** (2 * t) * mp.cos(mp.pi * n * x / m)
    return s_ / m
say("")
say("Closed form (mpmath 40 dps): by the semigroup property M(A,B) = c * g_2t(j_A - j_B + m/2), with")
say("  g_2t(x) = (1/m) sum_{n odd} lam_n^(2t) cos(pi n x/m). Check against the matrix computation:")
h = m // 2
for jb in (3, 6, 9):
    W = [g_exact(-jb + h, T, m, p) ** 2, g_exact(-jb, T, m, p) ** 2,
         g_exact(2 * h - jb, T, m, p) ** 2, g_exact(h - jb, T, m, p) ** 2]
    Ecf = (W[0] + W[3] - W[1] - W[2]) / sum(W)
    say("   theta = %5.1f deg: E_closed = %+.18f   E_matrix = %+.15f   -cos = %+.15f" %
        (360 * jb / m, float(Ecf), Etab[0, jb], -np.cos(TAU * jb / m)))
say("  t -> inf: g -> lam_1^(2t) cos(pi x/m)/m, so M(+,+) ~ sin((a-b)/2), M(+,-) ~ -cos((a-b)/2), giving")
say("  P(++) = P(--) = sin^2((a-b)/2)/2, P(+-) = P(-+) = cos^2((a-b)/2)/2  =>  E = -cos(a-b) exactly,")
say("  with N(a,b) = const. Settings on lattice sites carry no discretisation error.")

# ============================================================== 3. ablations
say("")
say("=" * 78)
say("3. ABLATIONS")
say("=" * 78)
say("(a) Z2 sign dropped (periodic sector = the plain walk on the base circle), squared readout kept:")
say("     t   |S|        max|E|     undefined pairs (N=0)  max marginal var  relvar N(a,b)  relvar C_a")
for tt in (1, 2, 5, 10, 20, 40, 100, 400, 3200):
    E5, r5 = summary("noZ2", m, p, tt, sector="peri")
    say("  %5d   %.6f   %.6f   %4d                   %.2e          %.3e      %.3e" %
        (tt, abs(r5["S"]), np.nanmax(np.abs(E5)), r5["nundef"], max(r5["sigA"], r5["sigB"]), r5["Nvar"], r5["Cvar"]))
say("  Per-pair normalisation lets the periodic sector reach |S| = 4 at short t with flat marginals,")
say("  but N(a,b) then varies by O(1) and vanishes for some pairs. Requiring a setting-independent")
say("  normalisation (relvar N < 1e-3):")
for sec in ("peri", "anti"):
    best_ok = (0.0, None)
    for tt in list(range(1, 200)) + list(range(200, 3201, 50)):
        E5, r5 = summary(sec, m, p, tt, sector=sec)
        if np.isfinite(r5["Nvar"]) and r5["Nvar"] < 1e-3 and abs(r5["S"]) > best_ok[0]:
            best_ok = (abs(r5["S"]), tt)
    say("    sector %-4s : max |S| over t with relvar N < 1e-3 = %.9f (at t = %s)" % (sec, best_ok[0], best_ok[1]))
say("  => with a setting-independent normalisation, dropping the Z2 sign removes the violation.")

G = G_sector(m, p, T, "nn", "anti")
GB = rows_shifted(G, m, h, "anti")
M = amplitudes(G, GB, m, 0, 3)
say("(b) Z2 sign kept, squaring dropped (linear readout of the signed sum), t = %d:" % T)
say("    M(A,B | a=0, b=45deg)/sum M =", np.array2string(M / M.sum(), precision=6).replace("\n", ""),
    "-> negative entries: not a probability")
Glift = G.copy(); Glift[:, 0] = -G[:, 0]        # the setting a=0 lifted to the other sheet
M2 = amplitudes(Glift, GB, m, 0, 3)
say("    lifting setting a to the other sheet flips M(+,.):", np.array2string(M2[0], precision=6),
    "vs", np.array2string(M[0], precision=6))
say("    => a linear readout is not a function of the setting on the base circle; the square is what")
say("       makes the readout well defined on the phase circle.")

say("(c) Z2 sign kept, square replaced by a local readout A = sign G(k, j_a), B = sign G_B(k, j_b),")
say("    mixed over the source framing k -- a local-hidden-variable model by construction:")
def E_sign(ja, jb):
    return np.mean(np.sign(G[:, ja]) * np.sign(GB[:, jb]))
Es = np.array([[E_sign(ja, jb) for jb in range(m)] for ja in range(m)])
mx = 0
for a_, a2_, b_, b2_ in itertools.product(range(m), repeat=4):
    mx = max(mx, abs(Es[a_, b_] - Es[a_, b2_] + Es[a2_, b_] + Es[a2_, b2_]))
say("    S at the Tsirelson settings = %+.6f ; max |S| over all 24^4 setting quadruples = %.12f" % (chsh(Es, m), mx))

say("(d) readout |M|^q, q != 2 (non-negative; Z2 sign kept), t = %d:" % T)
say("     q      |S|            max|E+cos|   max marginal var  relvar N(a,b)  relvar C_a")
for q in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 8.0, 32.0):
    Eq, rq = summary("pow", m, p, T, power=q)
    say("    %4.1f    %.9f    %.3e    %.2e          %.3e      %.3e" %
        (q, abs(rq["S"]), rq["dE"], max(rq["sigA"], rq["sigB"]), rq["Nvar"], rq["Cvar"]))
say("    closed form (t->inf): E_q = (|s|^q - |c|^q)/(|s|^q + |c|^q), s = sin(th/2), c = cos(th/2).")
say("    Marginals are 1/2 for EVERY q; sum_AB |M|^q = 2(|s|^q + |c|^q) is setting-independent iff q = 2.")
say("    => non-negativity plus flat marginals do NOT force the square: q > 2 gives |S| > 2 sqrt2 (-> 4)")
say("       but only with a normalisation that depends on both settings. q = 2 is singled out by the")
say("       requirement that the normalisation be setting-independent (completeness).")

say("(e) kernel and laziness (t chosen so the n = 3 contamination is < 1e-14):")
for kind, pp in (("nn", 0.5), ("nn", 0.9), ("nn", 0.1), ("nnn", 0.5), ("wide", 1.0)):
    ev = np.sort(np.abs(np.linalg.eigvalsh(twisted_kernel(m, pp, kind, "anti"))))[::-1]
    ratio = ev[2] / ev[0]           # ev[0] = ev[1]: the n = +-1 pair
    tt = int(np.ceil(np.log(1e-14) / (2 * np.log(ratio)))) + 1
    Ek, rk = summary(kind, m, pp, tt, kind=kind)
    say("    %-4s p=%.1f  lam3/lam1=%.6f  t=%5d : max|E+cos| = %.1e  |S|-2sqrt2 = %+.1e  relvar N = %.1e"
        % (kind, pp, ratio, tt, rk["dE"], abs(rk["S"]) - 2 * np.sqrt(2), rk["Nvar"]))
say("    => kernel-independent: the walk only filters down to the lowest antiperiodic harmonic.")

say("(f) m dependence (t chosen as in (e)):")
for mm in (8, 16, 24, 48, 96):
    lr = (1 - p + p * np.cos(3 * np.pi / mm)) / (1 - p + p * np.cos(np.pi / mm))
    tt = int(np.ceil(np.log(1e-14) / (2 * np.log(lr)))) + 1
    Em, rm = summary("m", mm, p, tt)
    say("    m = %3d  t = %6d : max|E+cos| = %.1e   |S| = %.15f   relvar N = %.1e" %
        (mm, tt, rm["dE"], abs(rm["S"]), rm["Nvar"]))

with open(sys.argv[1] if len(sys.argv) > 1 else "singlet_step0_output.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
