#!/usr/bin/env python3
"""Gate VOID, §2.1 — exact geometry of the FCC interstitial chambers.

Conventions (fixed by the gate card): FCC packing, sphere radius 1/2,
nearest-neighbour distance 1, conventional cubic cell edge a = sqrt(2).

A *chamber* is the polyhedron of the surrounding sphere centres (regular
tetrahedron or regular octahedron of edge 1) minus the sphere sectors that
intrude into it.  A *window* is a triangular face of that polyhedron minus
the three circular caps (sectors of radius 1/2, angle pi/3) that cross it.
Wall area of a chamber = sum over its spheres of R^2 * Omega_sector.

Everything expressible in closed form is done exactly in sympy; evaluation
uses mpmath at 60 decimal places.  A Monte Carlo estimate (1e7 points,
seed 17) is the required cross-check against the exact values.
"""
from __future__ import annotations

import sys
import sympy as sp
import mpmath as mp
import numpy as np

mp.mp.dps = 60
DPS = 60

# ---------------------------------------------------------------------------
# Exact symbols
# ---------------------------------------------------------------------------
R = sp.Rational(1, 2)                   # sphere radius
A_CELL = sp.sqrt(2)                     # conventional cubic cell edge
OMEGA_T = sp.acos(sp.Rational(23, 27))  # solid angle at a regular-tetrahedron vertex
OMEGA_O = 4 * sp.asin(sp.Rational(1, 3))  # solid angle at a regular-octahedron vertex

# Polyhedra of the centres (edge 1)
V_TET_POLY = sp.sqrt(2) / 12            # regular tetrahedron, edge 1
V_OCT_POLY = sp.sqrt(2) / 3             # regular octahedron, edge 1
A_TET_POLY = sp.sqrt(3)                 # 4 faces of area sqrt(3)/4
A_OCT_POLY = 2 * sp.sqrt(3)             # 8 faces

# Sphere sectors: volume (1/3) R^3 Omega, surface R^2 Omega
def sector_volume(omega):
    return sp.Rational(1, 3) * R**3 * omega

def sector_area(omega):
    return R**2 * omega

# True chambers
V_TET = V_TET_POLY - 4 * sector_volume(OMEGA_T)
V_OCT = V_OCT_POLY - 6 * sector_volume(OMEGA_O)
WALL_TET = 4 * sector_area(OMEGA_T)
WALL_OCT = 6 * sector_area(OMEGA_O)

# Window: equilateral triangle of side 1 minus three 60-degree sectors of radius 1/2
A_FACE = sp.sqrt(3) / 4
A_WINDOW = A_FACE - 3 * (sp.Rational(1, 2) * R**2 * sp.pi / 3)

# Inscribed balls (the corpus shorthand): radius = circumradius of polyhedron - 1/2
R_TET = sp.sqrt(6) / 4 - R              # circumradius of tetrahedron edge 1 is sqrt(6)/4
R_OCT = 1 / sp.sqrt(2) - R              # circumradius of octahedron edge 1 is 1/sqrt(2)
V_BALL_TET = sp.Rational(4, 3) * sp.pi * R_TET**3
V_BALL_OCT = sp.Rational(4, 3) * sp.pi * R_OCT**3
A_BALL_TET = 4 * sp.pi * R_TET**2
A_BALL_OCT = 4 * sp.pi * R_OCT**2
MU_BALL_TET = sp.pi**2 / R_TET**2       # Dirichlet ground state of a ball
MU_BALL_OCT = sp.pi**2 / R_OCT**2

# Interstitial volume per sphere, exact
V_INTERSTITIAL_PER_SPHERE = 1 / sp.sqrt(2) - sp.pi / 6
PACKING_FRACTION = sp.pi / (3 * sp.sqrt(2))
VOID_FRACTION = 1 - PACKING_FRACTION


def N(expr, dps=DPS):
    """Evaluate a sympy expression with mpmath at `dps` digits."""
    return mp.mpf(str(sp.N(expr, dps + 10)))


# ---------------------------------------------------------------------------
# §2.1 exact check: V_oct + 2 V_tet = 1/sqrt(2) - pi/6
# ---------------------------------------------------------------------------
def solid_angle_identity_exact() -> bool:
    """Prove 8 Omega_t + 6 Omega_o = 4 pi exactly.

    With alpha = asin(1/3): the identity reduces to acos(23/27) = pi/2 - 3 alpha,
    i.e. sin(3 alpha) = 23/27 with 0 < 3 alpha < pi/2.  sin(3a) = 3 sin a - 4 sin^3 a
    = 1 - 4/27 = 23/27.  Both sides are verified symbolically below.
    """
    a = sp.asin(sp.Rational(1, 3))
    lhs = sp.expand_trig(sp.sin(3 * a))          # 3 sin a - 4 sin^3 a with sin a = 1/3
    ok_sin = sp.simplify(lhs - sp.Rational(23, 27)) == 0
    # range check 0 < 3a < pi/2  <=>  1/3 < sin(pi/6) = 1/2, i.e. a < pi/6
    ok_range = sp.Rational(1, 3) < sp.Rational(1, 2)
    # therefore acos(23/27) = pi/2 - 3a exactly, and 8 Omega_t + 6 Omega_o = 8(pi/2 - 3a) + 24a = 4pi
    return bool(ok_sin and ok_range)


def volume_sum_check() -> tuple[bool, mp.mpf, mp.mpf]:
    """V_oct + 2 V_tet == 1/sqrt(2) - pi/6 (exact + 60-dps numeric)."""
    # Substitute the proven identity acos(23/27) -> pi/2 - 3 asin(1/3), then simplify.
    a = sp.asin(sp.Rational(1, 3))
    lhs = (V_OCT + 2 * V_TET).subs(sp.acos(sp.Rational(23, 27)), sp.pi / 2 - 3 * a)
    diff = sp.simplify(lhs - V_INTERSTITIAL_PER_SPHERE)
    exact_ok = (diff == 0) and solid_angle_identity_exact()
    lhs_num = N(V_OCT + 2 * V_TET)
    rhs_num = N(V_INTERSTITIAL_PER_SPHERE)
    numeric_ok = abs(lhs_num - rhs_num) < mp.mpf(10) ** (-(DPS - 5))
    return bool(exact_ok and numeric_ok), lhs_num, rhs_num


# ---------------------------------------------------------------------------
# Monte Carlo (1e7 points, seed 17)
# ---------------------------------------------------------------------------
TET_VERTS = np.array([[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=float) * (np.sqrt(2) / 2)
OCT_VERTS = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]],
                     dtype=float) * (np.sqrt(2) / 2)


def _outside_all_spheres(pts: np.ndarray, centres: np.ndarray, r=0.5) -> np.ndarray:
    ok = np.ones(len(pts), dtype=bool)
    for c in centres:
        d2 = np.sum((pts - c) ** 2, axis=1)
        ok &= d2 > r * r
    return ok


def mc_tet(n: int, seed: int):
    """Uniform points in the tetrahedron via Dirichlet(1,1,1,1) barycentrics."""
    rng = np.random.default_rng(seed)
    w = rng.exponential(size=(n, 4))
    w /= w.sum(axis=1, keepdims=True)
    pts = w @ TET_VERTS
    hits = _outside_all_spheres(pts, TET_VERTS)
    p = hits.mean()
    vol_poly = float(sp.N(V_TET_POLY, 20))
    est = p * vol_poly
    sigma = vol_poly * np.sqrt(p * (1 - p) / n)
    return est, sigma


def mc_oct(n: int, seed: int):
    """Uniform points in the octahedron |x|+|y|+|z| <= a/2 by rejection from its bounding cube."""
    rng = np.random.default_rng(seed)
    half = np.sqrt(2) / 2
    got = []
    count = 0
    while count < n:
        m = int((n - count) * 6.5) + 1000     # cube/octahedron volume ratio is 6
        q = rng.uniform(-half, half, size=(m, 3))
        inside = np.sum(np.abs(q), axis=1) <= half
        q = q[inside]
        take = q[: n - count]
        got.append(take)
        count += len(take)
    pts = np.concatenate(got)
    hits = _outside_all_spheres(pts, OCT_VERTS)
    p = hits.mean()
    vol_poly = float(sp.N(V_OCT_POLY, 20))
    est = p * vol_poly
    sigma = vol_poly * np.sqrt(p * (1 - p) / n)
    return est, sigma


def mc_cell(n: int, seed: int):
    """Interstitial volume per sphere from the conventional cell (4 spheres, edge sqrt 2)."""
    rng = np.random.default_rng(seed)
    a = np.sqrt(2)
    pts = rng.uniform(0, a, size=(n, 3))
    base = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]]) * a
    # periodic images: shift by all combinations of {0, a} and test
    ok = np.ones(n, dtype=bool)
    for c in base:
        d = pts - c
        d -= a * np.round(d / a)             # minimum image
        ok &= np.sum(d * d, axis=1) > 0.25
    p = ok.mean()
    vol_cell = a ** 3
    est = p * vol_cell / 4
    sigma = vol_cell / 4 * np.sqrt(p * (1 - p) / n)
    return est, sigma


def monte_carlo_check(n: int = 10_000_000, seed: int = 17):
    """All three MC estimates must agree with the exact values to within 3 sigma."""
    out = {}
    for name, fn, exact in (("tet", mc_tet, V_TET), ("oct", mc_oct, V_OCT),
                            ("cell_per_sphere", mc_cell, V_INTERSTITIAL_PER_SPHERE)):
        est, sig = fn(n, seed)
        ex = float(sp.N(exact, 20))
        z = (est - ex) / sig
        out[name] = dict(estimate=est, sigma=sig, exact=ex, z=z, pass_3sigma=abs(z) < 3)
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
QUANTITIES = {
    "Omega_t (sr)": OMEGA_T,
    "Omega_o (sr)": OMEGA_O,
    "V_tet_poly": V_TET_POLY,
    "V_oct_poly": V_OCT_POLY,
    "A_tet_poly": A_TET_POLY,
    "A_oct_poly": A_OCT_POLY,
    "V_tet_chamber": V_TET,
    "V_oct_chamber": V_OCT,
    "wall_tet_chamber": WALL_TET,
    "wall_oct_chamber": WALL_OCT,
    "A_window": A_WINDOW,
    "r_tet": R_TET,
    "r_oct": R_OCT,
    "V_ball_tet": V_BALL_TET,
    "V_ball_oct": V_BALL_OCT,
    "A_ball_tet": A_BALL_TET,
    "A_ball_oct": A_BALL_OCT,
    "mu_ball_tet = pi^2/r_tet^2": MU_BALL_TET,
    "mu_ball_oct = pi^2/r_oct^2": MU_BALL_OCT,
    "V_interstitial_per_sphere = 1/sqrt2 - pi/6": V_INTERSTITIAL_PER_SPHERE,
    "packing_fraction = pi/(3 sqrt2)": PACKING_FRACTION,
    "void_fraction = 1 - pi/(3 sqrt2)": VOID_FRACTION,
    "V_tet_chamber / V_ball_tet": V_TET / V_BALL_TET,
    "V_oct_chamber / V_ball_oct": V_OCT / V_BALL_OCT,
    "wall_tet / A_ball_tet": WALL_TET / A_BALL_TET,
    "wall_oct / A_ball_oct": WALL_OCT / A_BALL_OCT,
}


def main(mc_points: int = 10_000_000, seed: int = 17) -> int:
    ok, lhs, rhs = volume_sum_check()
    print("# Gate VOID §2.1 geometry (sphere radius 1/2, NN distance 1)")
    print(f"volume_sum_check_exact_and_60dps: {'PASS' if ok else 'FAIL'}")
    print(f"  V_oct + 2 V_tet        = {mp.nstr(lhs, 50)}")
    print(f"  1/sqrt(2) - pi/6       = {mp.nstr(rhs, 50)}")
    if not ok:
        print("SC-VOID-0: volume sum check FAILED — halt.")
        return 2
    for k, v in QUANTITIES.items():
        print(f"{k:45s} = {mp.nstr(N(v), 50)}   [{sp.sstr(v)}]")
    print(f"\n# Monte Carlo, {mc_points} points, seed {seed}")
    mc = monte_carlo_check(mc_points, seed)
    all_ok = True
    for k, d in mc.items():
        all_ok &= d["pass_3sigma"]
        print(f"MC_{k:16s} est={d['estimate']:.7f}  sigma={d['sigma']:.2e}  exact={d['exact']:.7f}  "
              f"z={d['z']:+.2f}  {'PASS' if d['pass_3sigma'] else 'FAIL'}")
    print(f"monte_carlo_3sigma: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        print("SC-VOID-0: Monte Carlo check FAILED — halt.")
        return 2
    return 0


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    sys.exit(main(n))
