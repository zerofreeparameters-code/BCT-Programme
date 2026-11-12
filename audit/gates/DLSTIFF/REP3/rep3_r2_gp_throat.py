#!/usr/bin/env python3
"""
rep3_r2_gp_throat.py -- Gate DL-STIFF REP3, route R2 support: re-derive (not inherit) STIFF's
CN-STIFF-01/03 with my own deterministic solver.

1D Gross-Pitaevskii across a window, lengths in units of a, xi/a from MINIMAL_BCT §1.3:
    -xi^2 psi'' + V(z) psi + (psi^2 - 1) psi = 0,   psi(+-L) = 1,
solved by Newton iteration from psi = 1 (converges to the real nodeless ground state).
  (a) V even (symmetric constriction):     number dipole p = int z (psi^2 - 1) dz -> 0.
  (b) V + b*s(z), s odd and localised:     p is linear in b (a NUMBER bias, i.e. a chemical-potential
      step, which in option B is not the field E of a_e).
The window shape (V0, w) is a modelling choice; (a) holds for every even V, (b) for every odd s.
Run:  python3 -I rep3_r2_gp_throat.py
"""
import numpy as np

xi = 1.0 / np.sqrt(8 * ((np.sqrt(2) - 1) / 2) * ((np.sqrt(6) - 2) / 4))   # 2.3175...
L, N = 40.0, 4001
z = np.linspace(-L, L, N)
h = z[1] - z[0]


def thomas(lower, diag, upper, rhs):
    """Tridiagonal solve (lower/upper constant scalars)."""
    n_ = len(diag)
    c = np.empty(n_); dd = np.empty(n_)
    c[0] = upper / diag[0]; dd[0] = rhs[0] / diag[0]
    for i in range(1, n_):
        den = diag[i] - lower * c[i - 1]
        c[i] = upper / den
        dd[i] = (rhs[i] - lower * dd[i - 1]) / den
    out = np.empty(n_); out[-1] = dd[-1]
    for i in range(n_ - 2, -1, -1):
        out[i] = dd[i] - c[i] * out[i + 1]
    return out


def residual(psi, V):
    u = psi[1:-1]
    lap = (psi[2:] - 2 * u + psi[:-2]) / h ** 2                 # psi(+-L) = 1 held fixed (Dirichlet)
    return -xi ** 2 * lap + V[1:-1] * u + (u ** 2 - 1) * u


def solve(V):
    psi = np.ones(N)
    off = -xi ** 2 / h ** 2
    for it in range(1, 41):
        u = psi[1:-1]
        F = residual(psi, V)
        diag = 2 * xi ** 2 / h ** 2 + V[1:-1] + 3 * u ** 2 - 1    # Newton Jacobian, tridiagonal
        du = thomas(off, diag, off, -F)
        psi[1:-1] += du
        if np.max(np.abs(du)) < 1e-13:
            break
    return psi, it, np.max(np.abs(residual(psi, V)))


def trap(f):
    return h * (np.sum(f) - 0.5 * (f[0] + f[-1]))


V0, w = 1.0, 0.5
Veven = V0 / np.cosh(z / w) ** 2
s_odd = np.tanh(z / w) / np.cosh(z / w) ** 2

print(f"xi/a = {xi:.10f}   grid: L = {L}, N = {N}, h = {h:.4f}   window: V0 = {V0}, w = {w}")
psi, it, res = solve(Veven)
n = psi ** 2
p0 = trap(z * (n - 1))
print("\n(a) symmetric window")
print(f"    Newton iterations {it}, final residual {res:.2e}")
print(f"    min density in throat n(0) = {n[N // 2]:.10f}   (a symmetric DEPLETION: monopole-type)")
print(f"    evenness residual max|n(z) - n(-z)| = {np.max(np.abs(n - n[::-1])):.2e}")
print(f"    number dipole p = int z (n - 1) dz   = {p0:.3e}")
print(f"    depletion monopole int (n - 1) dz    = {trap(n - 1):.10f}")

print("\n(b) odd number bias b * s(z) added (s localised, odd)")
for b in (1e-4, 2e-4, 4e-4, 8e-4):
    psi_b, it_b, res_b = solve(Veven + b * s_odd)
    pb = trap(z * (psi_b ** 2 - 1))
    print(f"    b = {b:.0e}:  p = {pb:+.6e}   p/b = {pb / b:+.8f}   (Newton {it_b} it, residual {res_b:.1e})")
print("    p/b constant -> linear response of NUMBER to a NUMBER bias; vanishes with the bias.")
print("    In option B nothing couples this response to a_e, so it is not a dielectric chi for the added field.")
