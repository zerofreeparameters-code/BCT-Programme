#!/usr/bin/env python3
"""
Gate TWIST -- Q2: is a massless, with two transverse polarisations, in the voids?

Part A  (conditional on the Q1 purchase): grant a as an independent U(1) connection minimally
        coupled to the overall phase, with the minimal Maxwell term -(1/4e^2) f^2 (e counted).
        Static kernel in (phi, a): find the screening mass and count polarisations.
Part B  Does the corpus supply a location-dependent condensate (condensed in shells, not in voids)?
        Solve V0 + the card's shell term on the FCC lattice:
          -xi^2 lap s + (s^2-1) s + xi^2 lam_s delta_shell s = 0,  s = sqrt(rho/n0),
        lam_s = alpha0/R from (alpha0 hbar^2/2mR) oint |Psi|^2 dA  (card sec.4, repulsive).
        (i) linear response with the exact delta shell (Fourier sum over reciprocal lattice)
        (ii) full nonlinear solve on a grid with a smoothed shell
        Sensitivity variants: App J's opposite sign (attractive), App JH's BC strength alpha0,
        and the alternative xi convention (xi^2 -> xi^2/2).
Lengths in units of the nearest-neighbour distance a = l_P.
Run:  python3 -I twist_q2_mass_and_density.py
"""
import numpy as np
from scipy.special import spherical_jn

ROCT = (np.sqrt(2) - 1) / 2
RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi
XI = 1 / np.sqrt(8 * np.pi * ALPHA0)
R = 0.5
A = np.sqrt(2.0)                      # FCC conventional cube side for nn distance 1
CENTRES = np.array([[0, 0, 0], [A / 2, A / 2, 0], [A / 2, 0, A / 2], [0, A / 2, A / 2]])

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

print(f"alpha0 = {ALPHA0:.10f}   xi = {XI:.5f} a   R = {R} a   r_oct = {ROCT:.5f} a   r_tet = {RTET:.5f} a")
print(f"xi/R = {XI / R:.4f}   xi/r_oct = {XI / ROCT:.3f}   xi/r_tet = {XI / RTET:.3f}")

# =============================================================================== A
hdr("A. Granted Maxwell term: mass of a in a uniformly condensed medium")
# Static energy  E = int K_s (grad phi + a)^2 + (1/2e^2)|curl a|^2 ; units K_s = 1, e^2 = 1/(2 lam^2)
for lam in (0.1, 1.0, 10.0):
    e2 = 1 / (2 * lam ** 2)
    out = []
    for kmag in (1e-3, 0.5, 2.0):
        k = np.array([0, 0, kmag])
        # variables (phi, ax, ay, az); quadratic form q = |i k phi + a|^2 + (1/2e2)|k x a|^2
        M = np.zeros((4, 4), dtype=complex)
        B = np.zeros((3, 4), dtype=complex)
        B[:, 0] = 1j * k; B[:, 1:] = np.eye(3)
        M += B.conj().T @ B
        Kx = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
        C = np.zeros((3, 4), dtype=complex); C[:, 1:] = Kx
        M += (1 / (2 * e2)) * C.conj().T @ C
        ev = np.sort(np.linalg.eigvalsh(M))
        # transverse eigen-energy per |a_T|^2 = 1 + k^2 lam^2
        out.append((kmag, ev))
    print(f"  lambda = {lam:5.1f} (e^2 = {e2:.3g}):")
    for kmag, ev in out:
        print(f"     k = {kmag:6.3f}: eigenvalues {np.round(ev, 6)}   transverse predicted 1 + k^2 lam^2 = {1 + kmag ** 2 * lam ** 2:.6f}")
print("  One zero eigenvalue (the gauge direction phi -> phi - chi, a -> a + grad chi); the two transverse")
print("  eigenvalues stay >= K_s as k -> 0: screening mass m^2 = 2 e^2 K_s, lambda = 1/sqrt(2 e^2 K_s).")
print("  With the time-dependent terms granted (GP i hbar Psi* d_t Psi couples to a_0; Maxwell E^2 term),")
print("  the transverse doublet disperses as omega^2 = c_a^2 (k^2 + lambda^-2) and the longitudinal mode is")
print("  the gapped plasmon: 3 massive polarisations (Anderson-Higgs/Meissner), 0 massless.")
print("  Massless only if e -> 0, where a decouples from the medium (no twist field left). -> FAIL.")

# =============================================================================== B (i)
def reciprocal(nmax):
    h = np.arange(-nmax, nmax + 1)
    H, K, L = np.meshgrid(h, h, h, indexing='ij')
    H, K, L = H.ravel(), K.ravel(), L.ravel()
    par = (H % 2 == K % 2) & (K % 2 == L % 2)            # FCC: all even or all odd
    G = 2 * np.pi / A * np.stack([H[par], K[par], L[par]], axis=1)
    return G

def linear_response(lam_s, xi, pts, nmax=60):
    G = reciprocal(nmax)
    Gm = np.linalg.norm(G, axis=1)
    Vc = A ** 3
    S = 4 * 4 * np.pi * R ** 2 * spherical_jn(0, Gm * R) / Vc        # structure factor 4 included
    uG = -xi ** 2 * lam_s * S / (xi ** 2 * Gm ** 2 + 2)
    res = []
    for p in pts:
        res.append(np.sum(uG * np.cos(G @ p)))                         # S_G real (centrosymmetric)
    return np.array(res), uG[Gm == 0][0]

# sample points (relative to sphere at origin)
PTS = {
    'sphere centre        ': np.array([0.0, 0.0, 0.0]),
    'shell, facing oct void': np.array([R, 0.0, 0.0]),
    'shell, facing tet void': R * np.array([1, 1, 1]) / np.sqrt(3),
    'contact point (12/sph)': np.array([A / 4, A / 4, 0.0]),
    'oct void centre      ': np.array([A / 2, 0.0, 0.0]),
    'tet void centre      ': np.array([A / 4, A / 4, A / 4]),
}
# sanity: distances
d_oct = np.min(np.linalg.norm(CENTRES - PTS['oct void centre      '], axis=1))
d_tet = np.min(np.linalg.norm(CENTRES - PTS['tet void centre      '], axis=1))
d_con = np.linalg.norm(PTS['contact point (12/sph)'])
print(f"\ngeometry check: oct centre to nearest sphere centre {d_oct:.5f} (R + r_oct = {R + ROCT:.5f}); "
      f"tet {d_tet:.5f} (R + r_tet = {R + RTET:.5f}); contact at r = {d_con:.5f}")

VARIANTS = [
    ("card shell term, repulsive, lam_s = +alpha0/R", +ALPHA0 / R, XI),
    ("App J sign (attractive),     lam_s = -alpha0/R", -ALPHA0 / R, XI),
    ("App JH BC strength,          lam_s = +alpha0  ", +ALPHA0, XI),
    ("alt. xi convention xi/sqrt2, lam_s = +alpha0/R", +ALPHA0 / R, XI / np.sqrt(2)),
]
hdr("B(i). Linear response, exact delta shells on FCC (density rho/n0 = (1+u)^2)")
lin_store = {}
for name, lam_s, xi in VARIANTS:
    u, u0 = linear_response(lam_s, xi, list(PTS.values()))
    rho = (1 + u) ** 2
    lin_store[name] = rho
    print(f"  {name}:  mean u0 = {u0:+.4f}")
    for (lab, _), r_ in zip(PTS.items(), rho):
        print(f"       {lab}  rho/n0 = {r_:.5f}")
    print(f"       contrast (max-min)/mean over these points = {(rho.max() - rho.min()) / rho.mean():.4%};  "
          f"oct-void minus shell = {rho[4] - rho[1]:+.5f}")

# =============================================================================== B (ii)
hdr("B(ii). Nonlinear solve on a grid (smoothed shell, width w), cubic FCC cell, periodic")
def shell_density(N, w):
    x = (np.arange(N) + 0.5) * A / N
    Xg, Yg, Zg = np.meshgrid(x, x, x, indexing='ij')
    dsum = np.zeros_like(Xg)
    for c in CENTRES:
        for ix in (-1, 0, 1):
            for iy in (-1, 0, 1):
                for iz in (-1, 0, 1):
                    cc = c + A * np.array([ix, iy, iz])
                    r = np.sqrt((Xg - cc[0]) ** 2 + (Yg - cc[1]) ** 2 + (Zg - cc[2]) ** 2)
                    m = np.abs(r - R) < 6 * w
                    dsum[m] += np.exp(-0.5 * ((r[m] - R) / w) ** 2) / (np.sqrt(2 * np.pi) * w)
    return x, dsum

def solve_nonlinear(lam_s, xi, N=112, w=0.025, tol=1e-11, Mp=3.0):
    x, dsh = shell_density(N, w)
    # check normalisation: integral of shell density per cell = 4 * 4 pi R^2
    area = np.sum(dsh) * (A / N) ** 3
    k1 = 2 * np.pi * np.fft.fftfreq(N, d=A / N)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    K2 = KX ** 2 + KY ** 2 + KZ ** 2
    s = np.ones((N, N, N))
    for it in range(3000):
        rhs = Mp * s - (s ** 2 - 1) * s - xi ** 2 * lam_s * dsh * s
        s_new = np.real(np.fft.ifftn(np.fft.fftn(rhs) / (xi ** 2 * K2 + Mp)))
        err = np.max(np.abs(s_new - s))
        s = s_new
        if err < tol:
            break
    return x, s, area, it, err

def sample(x, s, p):
    N = len(x); hgrid = A / N
    idx = np.mod(np.round(p / hgrid - 0.5).astype(int), N)
    return s[idx[0], idx[1], idx[2]] ** 2

for name, lam_s, xi in VARIANTS:
    x, s, area, it, err = solve_nonlinear(lam_s, xi)
    rho = np.array([sample(x, s, p) for p in PTS.values()])
    print(f"  {name}:  (shell area/cell {area:.4f} vs 4*pi = {4 * np.pi:.4f}; iters {it}, residual {err:.1e})")
    print(f"       grid min rho/n0 = {np.min(s ** 2):.5f}, max = {np.max(s ** 2):.5f}, mean = {np.mean(s ** 2):.5f}")
    for (lab, _), r_ in zip(PTS.items(), rho):
        print(f"       {lab}  rho/n0 = {r_:.5f}")
    print(f"       oct-void minus shell(oct-facing) = {rho[4] - rho[1]:+.5f};  global contrast (max-min)/mean = "
          f"{(np.max(s ** 2) - np.min(s ** 2)) / np.mean(s ** 2):.3%}")

hdr("B(iii). What 'condensed in shells, uncondensed in voids' would cost in V0")
for lab, r_v in (("oct void", ROCT), ("tet void", RTET)):
    # suppressing s from 1 to 0 over a distance r_v costs gradient energy density ~ xi^2 / r_v^2 (units g n0^2)
    print(f"  {lab}: r = {r_v:.4f} a; gradient cost ~ (xi/r)^2 = {(XI / r_v) ** 2:7.1f} x  vs condensation gain 1/2"
          f"  -> ratio ~ {2 * (XI / r_v) ** 2:7.0f}")
print("  The model's only length is xi = 2.32 a; the voids are 11-21x smaller. No location-dependent")
print("  phase can form on the void scale. The shell term is repulsive (card) and DEPLETES the shells,")
print("  the opposite of 'condensed in the shells'.")
print(f"  Cross-check vs App J sec. J.3.1: |Psi(R)|/Psi0 = tanh(r_oct/xi) = {np.tanh(ROCT / XI):.5f} is asserted there;")
print("  solving the functional itself gives |Psi(R)|/Psi0 = sqrt(rho/n0) = 0.80 (card term), 0.91 (JH strength),")
print("  1.16 (App J sign) -- never ~0.09. The tanh value is not a solution of the corpus's own equations.")
