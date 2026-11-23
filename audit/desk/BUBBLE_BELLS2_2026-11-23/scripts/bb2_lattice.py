#!/usr/bin/env python3
"""
Bubble Bells desk-check 2 (23 Nov 2026), part 2 — A LATTICE OF BELLS: Bloch band structure of the FCC void network.

Non-gate, same-session, CONJECTURE-capped.  Model (Gate BUBBLE_BELLS §1, as given): rigid depleted spheres R = a/2 on
FCC (touching), superfluid of uniform density in the void network, phase mode obeying the Neumann (no-flow) condition on the
sphere surfaces.  The Bloch eigenvalues lambda_n(K) of -Laplacian on the void network give the dispersion:
   hydrodynamic (phase) mode       omega^2 = c_s^2 lambda
   with the Bogoliubov correction  eps(lambda) = sqrt( lambda (lambda + 2 mu) ),  mu = 1/xi^2   (units hbar^2/2m = 1, a = 1)
(exact for uniform density with Neumann walls: u, v are eigenfunctions of the same operator).

Numerics: finite differences on the conventional cubic cell (edge L = a sqrt 2, 4 spheres), N^3 cells, h = L/N; void cells
= centres farther than R from every sphere centre; face conductance 1 (void-void) or 0 (face into a sphere: Neumann).
The FCC translations (L/2)(1,1,0), (L/2)(1,0,1), (L/2)(0,1,1) are exact grid shifts for even N, so the problem is reduced to
ONE primitive cell of grid cells (fundamental domain i < N/2, j < N/2) with Bloch phases exp(i K . Delta) on every bond that
leaves the domain — no band unfolding needed.  Lowest bands by shift-invert Lanczos (scipy eigsh).

Reported: lambda_n(K) along Gamma-X and Gamma-L and at X, W, K, L for N = 48, 64, 96; the acoustic band and its top; the
first optical (void-chamber) mode at Gamma; where App J's bell energy kappa0^2 and the hard-wall bell (2 pi)^2 sit relative to
the void network's own spectrum.  The K -> 0 slope of the acoustic band is the FD tortuosity on the same grid family as
bells_tortuosity.py — it is printed for consistency, NOT re-extrapolated (Gate BB-ALPHA is pre-registered to anchor it).
"""
import sys, time, functools
import numpy as np
print = functools.partial(print, flush=True)
import scipy.sparse as sps
import scipy.sparse.linalg as spla

a = 1.0; R = 0.5; L = np.sqrt(2.0)
alpha0 = (np.sqrt(2) - 1) / 2 * (np.sqrt(6) - 2) / 4 / np.pi
xi = a / np.sqrt(8 * np.pi * alpha0); mu = 1 / xi**2
kappa0 = 3.3904626; E_bell = kappa0**2; E_hard = (2 * np.pi)**2
centres = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]) * L
fcc_T = [np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, 0, 1]), np.array([0, 1, 1])]   # in units of N/2 cells

def build(N, K):
    """FCC-Bloch Neumann Laplacian on the void network, reduced to one primitive cell.  K in absolute units (1/a)."""
    h = L / N
    g = (np.arange(N) + 0.5) * h
    X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
    dmin = np.full((N, N, N), np.inf)
    for c in centres:
        dx = np.abs(X - c[0]); dx = np.minimum(dx, L - dx)
        dy = np.abs(Y - c[1]); dy = np.minimum(dy, L - dy)
        dz = np.abs(Z - c[2]); dz = np.minimum(dz, L - dz)
        dmin = np.minimum(dmin, np.sqrt(dx**2 + dy**2 + dz**2))
    void = dmin > R
    M = N // 2
    # fundamental domain: i < M, j < M, all k.  Map any cell (i,j,k) (mod N) to (rep index, FCC translation applied)
    def to_rep(i, j, k):
        i = i % N; j = j % N; k = k % N
        if i >= M and j >= M:   return (i - M, j - M, k), fcc_T[1]
        if i >= M:              return (i - M, j, (k + M) % N), fcc_T[2]      # subtract (M,0,M)
        if j >= M:              return (i, j - M, (k + M) % N), fcc_T[3]      # subtract (0,M,M)
        return (i, j, k), fcc_T[0]
    dom_void = void[:M, :M, :]
    idx = -np.ones((M, M, N), dtype=np.int64)
    idx[dom_void] = np.arange(dom_void.sum())
    n = dom_void.sum()
    rows, cols, vals = [], [], []
    diag = np.zeros(n)
    cells = np.argwhere(dom_void)
    for ax in range(3):
        for sgn in (+1, -1):
            e = np.zeros(3, dtype=int); e[ax] = sgn
            nb = cells + e                                        # unwrapped neighbour (may leave the torus / domain)
            # actual neighbour position relative to the cell: + sgn*h*e_ax.  Representative position: rep cell centre.
            # Delta = r_actual_nb - r_rep(nb) is an FCC lattice vector; phase = exp(i K.Delta).
            for c, nbc in zip(cells, nb):
                i0 = idx[tuple(c)]
                # is the neighbour a void cell (in the full torus)?
                if not void[nbc[0] % N, nbc[1] % N, nbc[2] % N]:
                    continue                                      # Neumann face: no bond, no diagonal contribution
                rep, T = to_rep(*nbc)
                j0 = idx[rep]
                # displacement from the representative cell to the actual neighbour cell, in cells:
                d_cells = nbc - np.array(rep)                      # includes torus wraps (multiples of N) and FCC shift (M)
                Delta = d_cells * h
                ph = np.exp(1j * (K @ Delta))
                rows.append(i0); cols.append(j0); vals.append(-ph)
                diag[i0] += 1.0
    A = sps.coo_matrix((np.array(vals), (np.array(rows), np.array(cols))), shape=(n, n)).tocsr()
    A = A + sps.diags(diag)
    A = A / h**2
    return A, n, dom_void.mean()

def lowest(A, k=8, sigma=-1.0):
    n = A.shape[0]
    if n <= 70000:
        # direct shift-invert (sparse LU); fine up to N = 96 in 7 GB
        vals = spla.eigsh(A, k=k, sigma=sigma, which='LM', return_eigenvectors=False, tol=1e-9)
    else:
        # memory-light shift-invert: (A - sigma I) is Hermitian positive definite for sigma < 0, solve it by
        # Jacobi-preconditioned CG inside ARPACK instead of factorising it
        B = (A - sigma * sps.identity(n, dtype=A.dtype, format='csr')).tocsr()
        Minv = sps.diags(1.0 / B.diagonal().real)
        def solve(b):
            x, info = spla.cg(B, b, M=Minv, rtol=1e-11, maxiter=20000)
            if info != 0: raise RuntimeError(f"inner CG did not converge (info={info})")
            return x
        OPinv = spla.LinearOperator(B.shape, matvec=solve, dtype=B.dtype)
        vals = spla.eigsh(A, k=k, sigma=sigma, which='LM', OPinv=OPinv, return_eigenvectors=False, tol=1e-9)
    return np.sort(vals.real)

def bog(lam):
    return np.sqrt(np.maximum(lam, 0) * (np.maximum(lam, 0) + 2 * mu))

if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if x != '--key']
    key_only = '--key' in sys.argv[1:]          # --key: Gamma, X, L, W and the zeta = 0.1 slope points only (large N)
    gx_only = '--gx' in sys.argv[1:]            # --gx: Gamma and X only (very large N)
    args = [x for x in args if x != '--gx']
    Ns = [int(x) for x in args] or [48, 64]
    b = 2 * np.pi / L                                    # reciprocal unit (2 pi / L)
    pts = {'Gamma': (0, 0, 0), 'X': (1, 0, 0), 'W': (1, 0.5, 0), 'K': (0.75, 0.75, 0), 'L': (0.5, 0.5, 0.5)}
    path = [('G-X', ζ, (ζ, 0, 0)) for ζ in (0.1, 0.25, 0.5, 0.75)] + [('G-L', ζ, (ζ / 2, ζ / 2, ζ / 2)) for ζ in (0.1, 0.25, 0.5, 0.75)]
    if key_only:
        pts = {k: v for k, v in pts.items() if k in ('Gamma', 'X', 'L', 'W')}
        path = [p for p in path if p[1] == 0.1]
    if gx_only:
        pts = {k: v for k, v in pts.items() if k in ('Gamma', 'X')}
        path = []
    print("Bubble Bells desk-check 2 — Bloch spectrum of the FCC void network (Neumann walls), eigenvalues lambda of -Laplacian in 1/a^2")
    print(f"a = 1, R = 1/2, L = a sqrt2 = {L:.5f}, mu = 1/xi^2 = {mu:.5f};  App J bell kappa0^2 = {E_bell:.3f} (61.7 mu);  hard-wall bell (2pi)^2 = {E_hard:.3f}")
    print(f"free-space |K|^2 at X = {(b)**2:.4f}, at L = {3*(b/2)**2:.4f}, at W = {1.25*b**2:.4f}, at K = {1.125*b**2:.4f}")
    print()
    for N in Ns:
        t0 = time.time()
        print(f"=== N = {N}  (h = {L/N:.5f} a, throat radius 0.0774 a = {0.0774/(L/N):.2f} cells)")
        res = {}
        for name, frac in pts.items():
            K = b * np.array(frac, dtype=float)
            A, n, phi_dom = build(N, K)
            herm = abs(A - A.getH()).max()
            lam = lowest(A, k=8)
            res[name] = lam
            print(f"  {name:>5}  K/b = {frac}  n = {n}  phi_grid = {phi_dom:.5f}  |A-A^H|max = {herm:.1e}   lambda = " + "  ".join(f"{x:8.4f}" for x in lam))
        print("  --- acoustic band along Gamma-X and Gamma-L (lowest eigenvalue), with |K|^2 and the local 'slope' |K|^2/lambda:")
        for lab, ζ, frac in path:
            K = b * np.array(frac, dtype=float)
            A, n, _ = build(N, K)
            lam = lowest(A, k=4)
            K2 = float(K @ K)
            print(f"    {lab} zeta = {ζ:<5} |K|^2 = {K2:8.4f}   lambda_0 = {lam[0]:8.4f}   |K|^2/lambda_0 = {K2/lam[0]:.4f}   lambda_1..3 = " + "  ".join(f"{x:8.4f}" for x in lam[1:]))
        lamX = res['X'][0]; lamL = res['L'][0] if 'L' in res else float('nan'); lam1G = res['Gamma'][1]
        print(f"  --- acoustic top: lambda_ac(X) = {lamX:.4f} (free {b**2:.3f}), lambda_ac(L) = {lamL:.4f} (free {3*(b/2)**2:.3f});  first optical at Gamma: lambda_1(Gamma) = {lam1G:.4f}")
        print(f"      in units of mu: lambda_ac(X)/mu = {lamX/mu:.2f}, lambda_1(Gamma)/mu = {lam1G/mu:.2f};  App J bell = 61.7 mu, hard-wall bell = {E_hard/mu:.1f} mu")
        print(f"      Bogoliubov energies eps/mu:  acoustic top (X) {bog(lamX)/mu:.2f},  first optical (Gamma) {bog(lam1G)/mu:.2f},  App J bell {bog(E_bell)/mu:.2f},  free zone-edge k=pi/a {bog(np.pi**2)/mu:.2f}")
        print(f"      elapsed {time.time()-t0:.0f}s")
        print()
