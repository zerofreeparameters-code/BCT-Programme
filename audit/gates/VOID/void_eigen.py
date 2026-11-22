#!/usr/bin/env python3
"""Gate VOID, §2.2 — lowest Dirichlet eigenvalue of the FCC interstitial region.

Finite-difference 7-point Laplacian on a uniform grid over the conventional
cubic cell (edge a = sqrt 2), periodic boundaries, Dirichlet (psi = 0) at every
grid point inside a sphere (radius 1/2, FCC centres).  Lowest eigenvalue by
scipy's sparse shift-invert eigensolver at N = 48, 64, 96 (h = a/N), then
Richardson extrapolation.

Domains
  ball     validation: the interior of a single ball of radius 1/2 placed at
           the cell centre; Dirichlet everywhere outside it.  Must reproduce
           pi^2/R^2 = 4 pi^2 to within 1 % after extrapolation (gate rule 2.2).
  network  the full periodic interstitial region (points outside all spheres).
  oct      one octahedral chamber: grid points inside the regular octahedron of
           edge 1 centred at the origin AND outside its six vertex spheres.
  tet      one tetrahedral chamber: points inside the regular tetrahedron with
           vertices (0,0,0), (a/2,a/2,0), (a/2,0,a/2), (0,a/2,a/2) AND outside
           its four vertex spheres.
For the chamber domains the polyhedron faces (window planes) carry a Neumann
condition: a neighbour that lies outside the polyhedron but not inside a sphere
is simply dropped from the stencil (zero-flux staircase approximation).  A
neighbour inside a sphere is Dirichlet regardless of where it sits.  Both
boundary treatments are first order in h, which is why three spacings and an
extrapolation are required.

Extrapolation: with three values lam(h1), lam(h2), lam(h3) the observed order p
is solved from (lam1-lam2)/(lam2-lam3) = (h1^p-h2^p)/(h2^p-h3^p), then
lam0 = lam3 - (lam2-lam3)*h3^p/(h2^p-h3^p).  If p falls outside [0.5, 3] the
staircase noise dominates and the fixed-order p = 1 two-point extrapolation on
the two finest grids is used instead; all variants are printed.
"""
from __future__ import annotations

import sys
import time
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import mpmath as mp

mp.mp.dps = 60
A = np.sqrt(2.0)          # cell edge
RAD = 0.5                 # sphere radius
GRIDS = (48, 64, 96)

FCC_BASE = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]]) * A


def grid(N):
    h = A / N
    idx = np.arange(N)
    X, Y, Z = np.meshgrid(idx * h, idx * h, idx * h, indexing="ij")
    return h, X, Y, Z


def inside_any_sphere_periodic(X, Y, Z, centres=FCC_BASE):
    """True where a grid point is strictly inside a sphere (minimum image)."""
    ins = np.zeros(X.shape, dtype=bool)
    for c in centres:
        dx = X - c[0]; dy = Y - c[1]; dz = Z - c[2]
        dx -= A * np.round(dx / A); dy -= A * np.round(dy / A); dz -= A * np.round(dz / A)
        ins |= (dx * dx + dy * dy + dz * dz) < RAD * RAD
    return ins


def masks(N, domain):
    """Return (dom, dirichlet, neumann) boolean arrays on the N^3 periodic grid.

    dom: unknowns.  dirichlet: psi = 0 there.  neumann: outside the domain but
    not Dirichlet — a neighbour there is dropped from the stencil.
    """
    h, X, Y, Z = grid(N)
    if domain == "ball":
        c = np.array([A / 2, A / 2, A / 2])
        d2 = (X - c[0]) ** 2 + (Y - c[1]) ** 2 + (Z - c[2]) ** 2
        dom = d2 < RAD * RAD
        dirichlet = ~dom
        neumann = np.zeros_like(dom)
    elif domain == "network":
        dirichlet = inside_any_sphere_periodic(X, Y, Z)
        dom = ~dirichlet
        neumann = np.zeros_like(dom)
    elif domain == "oct":
        # octahedron centred at origin (use periodic coordinates in (-a/2, a/2])
        Xc = X - A * (X > A / 2); Yc = Y - A * (Y > A / 2); Zc = Z - A * (Z > A / 2)
        half = A / 2
        in_poly = (np.abs(Xc) + np.abs(Yc) + np.abs(Zc)) <= half + 1e-12
        verts = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]) * half
        ins = np.zeros_like(in_poly)
        for v in verts:
            ins |= ((Xc - v[0]) ** 2 + (Yc - v[1]) ** 2 + (Zc - v[2]) ** 2) < RAD * RAD
        dirichlet = ins
        dom = in_poly & ~ins
        neumann = ~in_poly & ~ins
    elif domain == "tet":
        half = A / 2
        verts = np.array([[0, 0, 0], [half, half, 0], [half, 0, half], [0, half, half]])
        # tetrahedron = {x+y+z <= a, x+y-z >= 0, x-y+z >= 0, -x+y+z >= 0} in the cell corner;
        # use the first-octant copy (no wrap needed: it sits in [0, a/2]^3)
        e = 1e-12
        in_poly = ((X + Y + Z) <= A + e) & ((X + Y - Z) >= -e) & ((X - Y + Z) >= -e) & ((-X + Y + Z) >= -e)
        ins = np.zeros_like(in_poly)
        for v in verts:
            ins |= ((X - v[0]) ** 2 + (Y - v[1]) ** 2 + (Z - v[2]) ** 2) < RAD * RAD
        dirichlet = ins
        dom = in_poly & ~ins
        neumann = ~in_poly & ~ins
    else:
        raise ValueError(domain)
    return h, dom, dirichlet, neumann


def laplacian(N, domain):
    """Sparse -Laplacian restricted to the domain unknowns."""
    h, dom, dirichlet, neumann = masks(N, domain)
    n_dom = int(dom.sum())
    num = -np.ones(dom.shape, dtype=np.int64)
    num[dom] = np.arange(n_dom)
    diag = np.zeros(n_dom)
    rows, cols = [], []
    for axis in range(3):
        for shift in (+1, -1):
            nb_dom = np.roll(dom, -shift, axis=axis)          # neighbour's dom flag, viewed from each point
            nb_dir = np.roll(dirichlet, -shift, axis=axis)
            nb_num = np.roll(num, -shift, axis=axis)
            # neighbour in domain: off-diagonal -1 and +1 on diagonal
            sel = dom & nb_dom
            rows.append(num[sel]); cols.append(nb_num[sel])
            np.add.at(diag, num[sel], 1.0)
            # neighbour Dirichlet: +1 on diagonal only
            seld = dom & nb_dir
            np.add.at(diag, num[seld], 1.0)
            # neighbour Neumann (outside polyhedron, not in sphere): nothing
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    off = sps.coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n_dom, n_dom))
    L = (off + sps.diags(diag)).tocsc() / (h * h)
    return L, h, n_dom


def _opinv(L):
    """Shift-invert operator about sigma = 0: x = L^{-1} b.

    A direct LU factorisation of a 3-D grid Laplacian with >10^5 unknowns is
    prohibitively slow here, so the inverse is applied by preconditioned
    conjugate gradients (algebraic multigrid preconditioner, pyamg) solved to
    1e-12 relative residual — numerically equivalent to the exact inverse at
    the eigenvalue tolerance used.  L is SPD for every domain in this gate.
    """
    import pyamg
    ml = pyamg.smoothed_aggregation_solver(L.tocsr(), max_coarse=200)
    M = ml.aspreconditioner(cycle="V")

    def solve(b):
        x, info = spla.cg(L, b, M=M, rtol=1e-12, maxiter=500)
        if info != 0:
            raise RuntimeError(f"inner CG did not converge (info={info})")
        return x

    return spla.LinearOperator(L.shape, matvec=solve, dtype=float)


def lowest_eigenvalue(N, domain, verbose=True):
    t0 = time.time()
    L, h, n = laplacian(N, domain)
    # shift-invert about sigma = 0 (matrix is SPD for every domain used here)
    vals, vecs = spla.eigsh(L, k=1, sigma=0.0, which="LM", OPinv=_opinv(L), tol=1e-10, maxiter=5000)
    lam = float(vals[0])
    v = vecs[:, 0]
    resid = float(np.linalg.norm(L @ v - lam * v) / np.linalg.norm(v))   # independent residual check
    if resid > 1e-6 * lam:
        raise RuntimeError(f"eigenpair residual too large: {resid:.3e}")
    if verbose:
        print(f"  {domain:8s} N={N:3d} h={h:.6f} unknowns={n:7d}  lambda={lam:.8f}  resid={resid:.1e}  ({time.time()-t0:.1f}s)", flush=True)
    return lam, h, n


def richardson(hs, lams):
    """Three-point extrapolation with fitted order; returns dict of variants."""
    h1, h2, h3 = [mp.mpf(x) for x in hs]
    l1, l2, l3 = [mp.mpf(x) for x in lams]
    out = {}
    # fixed-order two-point (finest pair)
    for p in (1, 2):
        out[f"p={p}_2pt"] = l3 - (l2 - l3) * h3 ** p / (h2 ** p - h3 ** p)
    # fitted order
    ratio = (l1 - l2) / (l2 - l3)
    p_fit = None
    try:
        f = lambda p: (h1 ** p - h2 ** p) / (h2 ** p - h3 ** p) - ratio
        p_fit = mp.findroot(f, 1.0)
        if not (mp.mpf("0.5") <= p_fit <= 3):
            p_fit = None
    except Exception:
        p_fit = None
    if p_fit is not None:
        out["p_fit"] = p_fit
        out["p_fit_3pt"] = l3 - (l2 - l3) * h3 ** p_fit / (h2 ** p_fit - h3 ** p_fit)
        out["primary"] = out["p_fit_3pt"]
        out["primary_rule"] = f"3-point, fitted order p={mp.nstr(p_fit, 6)}"
    else:
        out["p_fit"] = None
        out["primary"] = out["p=1_2pt"]
        out["primary_rule"] = "2-point finest pair, fixed p=1 (fitted order out of [0.5,3])"
    return out


def run_domain(domain, grids=GRIDS):
    lams, hs, ns = [], [], []
    for N in grids:
        lam, h, n = lowest_eigenvalue(N, domain)
        lams.append(lam); hs.append(h); ns.append(n)
    ex = richardson(hs, lams)
    return dict(domain=domain, grids=list(grids), h=hs, unknowns=ns, lam=lams, extrap=ex)


def validate_ball():
    target = 4 * mp.pi ** 2
    res = run_domain("ball")
    lam0 = res["extrap"]["primary"]
    rel = abs(lam0 - target) / target
    res["target"] = target
    res["rel_err"] = rel
    res["pass"] = rel < mp.mpf("0.01")
    return res


def report(res):
    print(f"\n[{res['domain']}]")
    for N, h, n, lam in zip(res["grids"], res["h"], res["unknowns"], res["lam"]):
        print(f"  N={N:3d}  h={h:.6f}  unknowns={n:7d}  lambda_h={lam:.8f}")
    ex = res["extrap"]
    print(f"  extrap p=1 (2pt, finest) = {mp.nstr(ex['p=1_2pt'], 12)}")
    print(f"  extrap p=2 (2pt, finest) = {mp.nstr(ex['p=2_2pt'], 12)}")
    if ex["p_fit"] is not None:
        print(f"  fitted order p           = {mp.nstr(ex['p_fit'], 8)}")
        print(f"  extrap 3pt fitted p      = {mp.nstr(ex['p_fit_3pt'], 12)}")
    print(f"  PRIMARY extrapolated     = {mp.nstr(ex['primary'], 12)}   ({ex['primary_rule']})")
    if "target" in res:
        print(f"  target 4 pi^2            = {mp.nstr(res['target'], 12)}   rel.err = {mp.nstr(res['rel_err']*100, 4)} %   "
              f"{'PASS' if res['pass'] else 'FAIL'}")


def main(domains=("network", "oct", "tet")):
    print("# Gate VOID §2.2 eigenvalues — validation first")
    val = validate_ball()
    report(val)
    if not val["pass"]:
        print("SC-VOID-0: ball eigenvalue validation FAILED — halt.")
        return 2
    results = {"ball": val}
    for d in domains:
        results[d] = run_domain(d)
        report(results[d])
    return 0, results


if __name__ == "__main__":
    rc = main()
    sys.exit(rc if isinstance(rc, int) else rc[0])
