#!/usr/bin/env python3
"""
Gate PILOT -- Steps 5-6: tests T1-T5 and the pilot-wave readings, as computations.

  T1  CHSH: exhaustive local deterministic strategies; the Letter 254 mechanism
      ('a single Hopf configuration fixed at creation, read locally at each wing')
      modelled as a shared global variable with local readout; quantum singlet.
  T4  Mermin (3 parties): exhaustive local strategies vs GHZ; parameter counting
      for what the written field supplies vs what an N-party joint state needs.
  T5  Salart et al. Eq.(3) applied to every finite lattice v_max from
      pilot_dispersion.py, worst case |beta_par| = beta (no Earth-rotation gain).
  P   Vortex-core beable check: GP vortex profile (Letter 60 radial equation, H=1);
      quantum-equilibrium weight |Psi|^2 at the core and the Madelung velocity there.
Run: python3 -I pilot_tests.py [outfile]
"""
import sys
import itertools
import numpy as np
import mpmath as mp
from scipy.integrate import quad, solve_bvp

mp.mp.dps = 60
out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


# ------------------------------------------------------------------ T1 CHSH
say("=" * 78)
say("T1 -- CHSH")
say("=" * 78)
best = 0
for A in itertools.product((1, -1), repeat=2):
    for B in itertools.product((1, -1), repeat=2):
        S = A[0] * B[0] + A[0] * B[1] + A[1] * B[0] - A[1] * B[1]
        best = max(best, abs(S))
say("max |S| over all 16 local deterministic strategies =", best, "(convex hull => every LHV mixture <= 2)")

# Letter 254 mechanism: shared global orientation lam fixed at creation; each wing reads the local
# projection of the same configuration: A = sign cos(lam - a), B = -sign cos(lam - b).
def E_l254(a, b):
    f = lambda lam: np.sign(np.cos(lam - a)) * -np.sign(np.cos(lam - b))
    pts = np.sort(np.mod(np.array([a + np.pi / 2, a - np.pi / 2, b + np.pi / 2, b - np.pi / 2]), 2 * np.pi))
    edges = np.concatenate([[0], pts, [2 * np.pi]])
    return sum(quad(f, edges[i], edges[i + 1])[0] for i in range(len(edges) - 1)) / (2 * np.pi)


def S_of(E, a, a2, b, b2):
    return E(a, b) - E(a, b2) + E(a2, b) + E(a2, b2)


Eq = lambda a, b: -np.cos(a - b)
ang = (0.0, np.pi / 2, np.pi / 4, 3 * np.pi / 4)
say("Tsirelson settings for S = E(a,b) - E(a,b') + E(a',b) + E(a',b'): a=0, a'=pi/2, b=pi/4, b'=3pi/4:")
say("  quantum singlet E=-cos(a-b):          |S| = %.12f  (2 sqrt2 = %.12f)" % (abs(S_of(Eq, *ang)), 2 * np.sqrt(2)))
say("  L254 'local readout of shared Hopf geometry': |S| = %.12f" % abs(S_of(E_l254, *ang)))
rng = np.random.default_rng(20261009)
mx = 0
for _ in range(3000):
    st = rng.uniform(-np.pi, np.pi, 4)
    mx = max(mx, abs(S_of(E_l254, *st)))
say("  L254 model, max |S| over 3000 random setting quadruples = %.12f (never > 2: Bell)" % mx)
say("  r_oct identity 1/(2 r_oct + 1) = 1/sqrt2 = cos(pi/4): algebraically true; supplies no setting-")
say("  dependence term, no correlation function, no bound -> scored ZERO (card Sec.5 guard).")

# ------------------------------------------------------------------ T4 Mermin + counting
say("")
say("=" * 78)
say("T4 -- MERMIN (three defects) AND COUNTING")
say("=" * 78)
best = 0
for A in itertools.product((1, -1), repeat=2):          # A[0]=X outcome, A[1]=Y outcome
    for B in itertools.product((1, -1), repeat=2):
        for C in itertools.product((1, -1), repeat=2):
            M = A[0] * B[0] * C[0] - A[0] * B[1] * C[1] - A[1] * B[0] * C[1] - A[1] * B[1] * C[0]
            best = max(best, abs(M))
say("max |M| over all 64 local deterministic strategies =", best)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
ghz = np.zeros(8, complex)
ghz[0] = ghz[7] = 1 / np.sqrt(2)
k3 = lambda P, Q, R: np.kron(np.kron(P, Q), R)
Mop = k3(X, X, X) - k3(X, Y, Y) - k3(Y, X, Y) - k3(Y, Y, X)
say("GHZ (|000>+|111>)/sqrt2: <M> = %.12f" % np.real(ghz.conj() @ Mop @ ghz))
prod = np.kron(np.kron([1, 1], [1, 1]), [1, 1]) / np.sqrt(8)
bestp = 0
for th in rng.uniform(0, np.pi, (2000, 3, 2)):
    v = [np.array([np.cos(t[0] / 2), np.exp(1j * t[1]) * np.sin(t[0] / 2)]) for t in th]
    p = np.kron(np.kron(v[0], v[1]), v[2])
    bestp = max(bestp, abs(np.real(p.conj() @ Mop @ p)))
say("product (mean-field) states, max |<M>| over 2000 random = %.6f  (<= 2: a condensate in one" % bestp)
say("  classical field is a product state; it cannot reach 4)")
say("Counting (real parameters):")
for nm, per in (("GP / complex scalar Psi (AZ6, L60)", 2), ("XY phase theta (Vol1 E.1)", 1), ("App JH interior C^2", 4)):
    say("  %-38s supplies %d real numbers per site -> %d N_s for N_s sites" % (nm, per, per))
for Ns in (10 ** 3, 10 ** 6):
    for N in (2, 3):
        say("  pure joint state of N=%d defects on N_s=%.0e sites: 2 N_s^N - 2 = %.3e reals; field: 2 N_s = %.1e"
            % (N, Ns, 2 * Ns ** N - 2, 2 * Ns))
say("  three qubits: product 3x2 = 6 reals; general pure state 2*8-2 = 14 reals (GHZ needs the 14-dim space).")
say("  Escape route (Norsen 2010; Norsen-Marian-Oriols 2015): physical-space fields CAN carry this, but")
say("  only with an infinite network of added interacting fields -> added structure, not the written field.")

# ------------------------------------------------------------------ T5 Salart
say("")
say("=" * 78)
say("T5 -- SPEED: Salart et al. (Nature 454, 861) Eq.(3) vs lattice v_max")
say("=" * 78)
rho = mp.mpf("5.4e-6")
def salart(beta, bpar):
    return mp.sqrt(1 + (1 - beta ** 2) * (1 - rho ** 2) / (rho + abs(bpar)) ** 2)
say("Eq.(3): (V/c)^2 >= 1 + (1-beta^2)(1-rho^2)/(rho+|beta_par|)^2,  rho = 5.4e-6 (18 km, 323 ps)")
say("Paper's stated result: V > 1e4 c for privileged frames with Earth speed beta <= 1e-3 (Earth-rotation analysis).")
for b in (mp.mpf("1e-4"), mp.mpf("1e-3"), mp.mpf("1e-2"), mp.mpf("0.1")):
    say("  worst case |beta_par| = beta = %s : V/c >= %s" % (mp.nstr(b, 3), mp.nstr(salart(b, b), 6)))
VMAX = {"B-C1 (GP, AZ6 xi)": mp.mpf("4.63968713561952724031851567454"),
        "B-C2 (GP, L64 dispersion xi)": mp.mpf("6.55670061415945919348401597274"),
        "B-C3 (GP, L64 text xi)": mp.mpf("3.28952755197413963517788681607"),
        "KA2 asserted phase-imprint speed": mp.mpf("6.78")}
for nm, v in VMAX.items():
    bstar = mp.findroot(lambda b: salart(b, b) - v, mp.mpf("0.1"))
    say("  %-34s v_max/c = %-10s excluded as the carrier of the 18-km correlations for EVERY" % (nm, mp.nstr(v, 8)))
    say("  %-34s privileged frame with Earth speed beta < %s (worst-case alignment)" % ("", mp.nstr(bstar, 6)))
say("Bancal et al. (Nat. Phys. 8, 867): ANY finite v (c < v < inf) v-causal model reproducing quantum")
say("  4-party correlations permits superluminal signalling; for 2 parties only experimental bounds on v")
say("  (as above) exclude it.")

# ------------------------------------------------------------------ P: vortex-core beable
say("")
say("=" * 78)
say("READING P -- vortex-core beable vs quantum equilibrium (Letter 60 radial equation, H = 1)")
say("=" * 78)
Hn = 1
R = 30.0
r0 = 1e-3
def ode(r, y):
    f, fp = y
    return np.vstack([fp, -fp / r + Hn ** 2 * f / r ** 2 - (1 - f ** 2) * f])
def bc(ya, yb):
    # regular core f ~ c r  (f - r f' = 0 at r0);  far field f ~ 1 - 1/(2 r^2)
    return np.array([ya[0] - r0 * ya[1], yb[0] - (1 - 1 / (2 * R ** 2))])
r = np.linspace(r0, R, 3000)
guess = np.vstack([r / np.sqrt(2 + r ** 2), 2 / (2 + r ** 2) ** 1.5])
sol = solve_bvp(ode, bc, r, guess, tol=1e-8, max_nodes=1000000)
say("solve_bvp status:", sol.status, "(0 = converged); core slope f'(0) = %.6f" % sol.sol(r0)[1],
    "(dimensionless GP vortex, Letter 60 normalisation)")
for rr in (0.01, 0.1, 0.5, 1.0, 2.0):
    f = sol.sol(rr)[0]
    say("  r/xi = %-5s |Psi|^2/n0 = f^2 = %.3e   Madelung speed |v| = (hbar/m)/r = %.1f (hbar/(m xi))" % (rr, f * f, 1 / rr))
w_core = quad(lambda x: sol.sol(x)[0] ** 2 * x, 1e-4, 0.1)[0] / quad(lambda x: x, 1e-4, 0.1)[0]
say("  equilibrium weight |Psi|^2 inside r < 0.1 xi relative to bulk: %.3e" % w_core)
say("  => if the defect core were the beable and Psi its pilot wave, quantum equilibrium rho = |Psi|^2")
say("     would assign it ~zero probability of being where the defect is, and the guidance velocity")
say("     (hbar/m) Im(grad Psi / Psi) diverges there. Psi cannot pilot its own defects.")
say("Order in time of the defect (node) motion, from Psi(X(t),t) = 0:")
say("  first-order GP:  X'.grad Psi = -(i hbar/2m) lap Psi at the node -> X' fixed by Psi alone: FIRST order")
say("  second-order (wave/KG/XY): X'.grad Psi = -d_t Psi, and d_t Psi is independent Cauchy data")
say("                   -> X' is extra initial data; differentiating again gives X'': SECOND order")

with open(sys.argv[1] if len(sys.argv) > 1 else "pilot_tests_output.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
