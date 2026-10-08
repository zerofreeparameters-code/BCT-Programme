"""Unit tests for u1sim (beyond the card's section 4 checks)."""
import time, sys
import numpy as np
from scipy.special import i0, i1
import u1sim as U

print("== lattice counts ==")
for name in ("d4", "hc"):
    for L in (4, 6, 8):
        lat = U.build(name, L)
        P = lat["plaq_links"].shape[0]
        print(f"{name} L={L}: sites={lat['Ns']} links={lat['nlinks']} plaq={P} "
              f"plaq/site={P/lat['Ns']:.0f} links/site={lat['nlinks']/lat['Ns']:.0f} "
              f"plaq/link={np.bincount(lat['plaq_links'].ravel()).min()}..{np.bincount(lat['plaq_links'].ravel()).max()}")

shapes = U.d4_triangle_shapes()
print("D4 triangle translation classes:", len(shapes))
_, allr = U.d4_roots()
rset = {tuple(r) for r in allr}
assert all(tuple(a) in rset and tuple(b) in rset and tuple(b - a) in rset for a, b in shapes)
# triangles touching a site: 96 (Celmaster), ordered (r1,r2) pairs from a site: 192
n_ord = sum(1 for r1 in allr for r2 in allr if tuple(r1 + r2) in rset)
print("ordered (r1,r2) pairs from a site:", n_ord, " -> triangles touching a site:", n_ord // 2)

print("== von Mises sampler: <cos psi> vs I1/I0 ==")
U.nb_seed(12345)
from numba import njit
@njit
def draw(k, n):
    s = 0.0; s2 = 0.0
    for i in range(n):
        p = U.vonmises0(k)
        s += np.cos(p); s2 += np.sin(p)
    return s / n, s2 / n
for k in (1e-9, 1e-4, 0.05, 0.5, 2.0, 8.0, 40.0, 160.0):
    c, sn = draw(k, 2_000_000)
    exact = i1(k) / i0(k)
    err = np.sqrt(max(1 - exact**2, 1e-12) / 2 / 2_000_000)
    print(f"kappa={k:<8g} <cos>={c:.6f} exact={exact:.6f} diff/sigma={(c-exact)/err:+.2f}  <sin>={sn:+.5f}")

print("== staple consistency: local Delta S vs global recompute ==")
rng = np.random.default_rng(1)
for name in ("d4", "hc"):
    lat = U.build(name, 4)
    U.nb_seed(7)
    th = U.init_hot(lat["nlinks"])
    P = lat["plaq_links"].shape[0]
    worst = 0.0
    for trial in range(200):
        l = rng.integers(lat["nlinks"])
        new = rng.uniform(0, 2 * np.pi)
        re, im = U.staple(th, lat["stp_l"], lat["stp_s"], l)
        dloc = -(re * (np.cos(new) - np.cos(th[l])) - im * (np.sin(new) - np.sin(th[l])))
        S0 = P * U.energy(th, lat["plaq_links"], lat["PS_f"])
        old = th[l]; th[l] = new
        S1 = P * U.energy(th, lat["plaq_links"], lat["PS_f"])
        worst = max(worst, abs((S1 - S0) - dloc))
    print(f"{name}: max |dS_global - dS_staple| over 200 trials = {worst:.2e}")
    assert worst < 1e-9

print("== timing (heat-bath sweep) ==")
for name, L in (("d4", 8), ("d4", 12), ("d4", 16), ("hc", 8), ("hc", 12)):
    lat = U.get_lat(name, L)
    U.nb_seed(1)
    th = U.init_hot(lat["nlinks"])
    U.evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], 0.6, 2, True)
    t = time.time()
    n = 20
    U.evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], 0.6, n, True)
    dt = (time.time() - t) / n
    print(f"{name} L={L}: {dt*1e3:.1f} ms per sweep+measure, {dt/lat['nlinks']*1e9:.0f} ns/link")
