#!/usr/bin/env python3
"""
Bubble-bells desk-check, part 1 (non-gate, CONJECTURE-capped):
EFFECTIVE SOUND SPEED OF A SUPERFLUID CONFINED TO THE FCC INTERSTITIAL (VOID) NETWORK.

Model: rigid, depleted spheres of radius R = a/2 on FCC (touching), superfluid of sound speed c_s filling the
voids (porosity φ = 1 − π/(3√2) = 0.25952).  At T = 0 the superfluid in a rigid porous matrix propagates
"fourth sound" at   c_4² = c_s² / α_∞ ,  α_∞ = tortuosity = φ · F,  F = σ_0/σ_eff the formation factor
(Johnson, Koplik & Dashen, J. Fluid Mech. 176, 379 (1987): α_∞ is the electrical tortuosity of the pore space,
measurable by fourth sound in He-II).  So the whole computation is the DC effective conductivity of the void
space with the spheres insulating — a Laplace problem on the periodic FCC cell.

Numerics: conventional cubic cell of edge L = a√2 containing 4 spheres; N³ grid; face conductances by harmonic
mean (void σ = 1, sphere σ = ε ≪ 1 for regularity); applied unit field along x via φ = −x + ψ, ψ periodic;
sparse CG with Jacobi preconditioner; σ_eff = mean current density.  Convergence in N and ε reported.
Isotropy: cubic symmetry makes the conductivity tensor a scalar; we verify σ_xx = σ_yy = σ_zz numerically.
Dilute check: Maxwell–Garnett for insulating spheres σ/σ_0 = (1−f)/(1+f/2) — an upper bound at touching.
"""
import sys, time
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla

def void_mask(N, R_over_L):
    # grid points at cell centres; periodic distance to the 4 FCC centres (in units of L)
    g = (np.arange(N) + 0.5) / N
    X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
    centres = [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]
    dmin = np.full((N, N, N), np.inf)
    for cx, cy, cz in centres:
        dx = np.abs(X - cx); dx = np.minimum(dx, 1 - dx)
        dy = np.abs(Y - cy); dy = np.minimum(dy, 1 - dy)
        dz = np.abs(Z - cz); dz = np.minimum(dz, 1 - dz)
        dmin = np.minimum(dmin, np.sqrt(dx**2 + dy**2 + dz**2))
    return dmin > R_over_L

def solve_sigma_eff(N, eps=1e-6, direction=0, tol=1e-10):
    R_over_L = 0.5 / np.sqrt(2)          # R = a/2, L = a√2
    void = void_mask(N, R_over_L)
    sig = np.where(void, 1.0, eps)
    idx = np.arange(N**3).reshape(N, N, N)
    rows, cols, vals = [], [], []
    diag = np.zeros(N**3)
    rhs = np.zeros(N**3)
    for ax in range(3):
        sig_n = np.roll(sig, -1, axis=ax)           # neighbour in +ax
        g = 2 * sig * sig_n / (sig + sig_n)          # harmonic-mean face conductance (h = 1 units)
        idx_n = np.roll(idx, -1, axis=ax)
        i = idx.ravel(); j = idx_n.ravel(); gv = g.ravel()
        rows += [i, j]; cols += [j, i]; vals += [-gv, -gv]
        np.add.at(diag, i, gv); np.add.at(diag, j, gv)
        if ax == direction:
            # source from the applied field E = 1 along `direction`: ∇·(σ ê) → face conductance differences
            # φ = −x + ψ:  Σ_faces g (φ_i − φ_j) = 0  ⇒  Σ g (ψ_i − ψ_j) = −Σ g (x_i − x_j) = −Σ_{+faces} g·(−1) ... per node:
            # node i has +face (to j=i+1) with x_i − x_j = −1 and −face (from k=i−1) with x_i − x_k = +1
            np.add.at(rhs, i, -gv)      # outflow through +face carries drive +g_+ ; conservation ⇒ Σg(ψ_i−ψ_j) = g_− − g_+
            np.add.at(rhs, j, +gv)      # same face is node j's −face
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    A = sps.coo_matrix((np.concatenate([vals, diag]), (np.concatenate([rows, idx.ravel()]), np.concatenate([cols, idx.ravel()]))),
                       shape=(N**3, N**3)).tocsr()
    # gauge: the system is singular (constant ψ) but consistent (rhs sums to zero); CG handles it, then remove the mean
    M = sps.diags(1.0 / A.diagonal())
    t0 = time.time()
    psi, info = spla.cg(A, rhs, M=M, rtol=tol, maxiter=50000)
    psi = (psi - psi.mean()).reshape(N, N, N)
    # conservation check: discrete divergence of the total current
    div = np.zeros((N, N, N))
    for ax in range(3):
        sg = np.roll(sig, -1, axis=ax); gg = 2 * sig * sg / (sig + sg)
        Jp = gg * ((1.0 if ax == direction else 0.0) + psi - np.roll(psi, -1, axis=ax))
        div += Jp - np.roll(Jp, 1, axis=ax)
    assert np.abs(div).max() < 1e-6, f"current not conserved: max|div| = {np.abs(div).max()}"
    # current density along `direction`: J = g (φ_i − φ_j)/h over faces, φ = −x + ψ ⇒ φ_i − φ_j = +1 + ψ_i − ψ_j (h=1)
    sig_n = np.roll(sig, -1, axis=direction); g = 2 * sig * sig_n / (sig + sig_n)
    psi_n = np.roll(psi, -1, axis=direction)
    J = g * (1.0 + psi - psi_n)
    sigma_eff = J.mean()            # mean current density = σ_eff · E (E = 1), in units of void σ
    # also check conservation: current through each plane equals the mean
    planes = J.sum(axis=tuple(k for k in range(3) if k != direction)) / N**2
    return sigma_eff, void.mean(), planes.std() / planes.mean(), info, time.time() - t0

if __name__ == "__main__":
    f_fcc = np.pi / (3 * np.sqrt(2)); phi_exact = 1 - f_fcc
    print("Bubble bells — tortuosity of the FCC void network (rigid insulating spheres, R = a/2)")
    print(f"exact porosity φ = 1 − π/(3√2) = {phi_exact:.6f};  Maxwell–Garnett upper estimate σ/σ0 = (1−f)/(1+f/2) = {phi_exact/(1+f_fcc/2):.5f}")
    print()
    print("   N    ε      φ_grid    σ_eff/σ0    F=1/σ_eff   α_∞=φF    c4/cs=1/√α_∞   plane-flux spread   cg   time")
    results = {}
    Ns = [int(x) for x in sys.argv[1:]] or [32, 48, 64, 96]
    for N in Ns:
        for eps in ([1e-6] if N > 48 else [1e-4, 1e-6]):
            s, phig, spread, info, dt = solve_sigma_eff(N, eps=eps)
            F = 1 / s; alpha = phi_exact * F
            results[(N, eps)] = s
            print(f"  {N:3d}  {eps:.0e}  {phig:.5f}   {s:.5f}     {F:8.4f}    {alpha:7.4f}     {1/np.sqrt(alpha):.5f}         {spread:.1e}        {info:2d}  {dt:5.1f}s")
    # isotropy check at the largest N
    N = Ns[-1]
    sx = results[(N, 1e-6)]
    sy, *_ = solve_sigma_eff(N, eps=1e-6, direction=1)
    sz, *_ = solve_sigma_eff(N, eps=1e-6, direction=2)
    print(f"\nIsotropy at N={N}: σ_xx={sx:.6f} σ_yy={sy:.6f} σ_zz={sz:.6f}  (cubic symmetry ⇒ scalar tensor; off-diagonals vanish by the mirror planes)")
    # Richardson-style extrapolation on the two largest N (first-order in h near contact singularities)
    if len(Ns) >= 2:
        N1, N2 = Ns[-2], Ns[-1]; s1, s2 = results[(N1, 1e-6)], results[(N2, 1e-6)]
        s_ext = s2 + (s2 - s1) * (1 / N2) / (1 / N1 - 1 / N2)
        a_ext = phi_exact / s_ext
        print(f"Extrapolated (1/N → 0, linear): σ_eff/σ0 ≈ {s_ext:.4f},  α_∞ ≈ {a_ext:.3f},  c4/cs ≈ {1/np.sqrt(a_ext):.4f}  (≈ ±1–2 % from the contact singularities)")
