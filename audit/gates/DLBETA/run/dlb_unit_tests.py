"""Gate DL-BETA -- unit tests of the run's simulator (not card checks; card K2-K5 are in the driver).
(1) von Mises sampler vs the exact law (KS test + <cos> = I1/I0), kappa 1e-3 .. 200, two seeds;
(2) the heat-bath conditional: staple() reproduces the global action change;
(3) timing at beta = 20 on every lattice size the run uses.
Usage: python3 -I dlb_unit_tests.py OUTDIR
"""
import os, sys, time, json
import numpy as np
from scipy import stats, special

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dlb_sim as S

OUT = sys.argv[1]
lines = []
fails = []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


say("(1) von Mises sampler (Best-Fisher, cancellation-free), 1,000,000 draws per (kappa, seed)")
say(f"{'kappa':>8} {'seed':>5} {'KS p':>8} {'<cos>':>10} {'I1/I0':>10} {'dev/sigma':>9}")
ps = []
for kappa in (1e-3, 0.05, 0.3, 1.0, 2.5, 6.0, 15.0, 40.0, 120.0, 200.0):
    for seed in (11, 12):
        x = S.vm_many(kappa, 1_000_000, seed)
        assert np.all(np.abs(x) <= np.pi)
        p = stats.kstest(x, stats.vonmises(kappa).cdf).pvalue
        ps.append(p)
        c = np.cos(x)
        m, sd = c.mean(), c.std() / np.sqrt(len(c))
        ex = special.i1e(kappa) / special.i0e(kappa)
        say(f"{kappa:8.3f} {seed:5d} {p:8.3f} {m:10.6f} {ex:10.6f} {(m-ex)/sd:9.2f}")
        if abs(m - ex) / sd > 4.5:
            fails.append(f"vm <cos> kappa={kappa}")
ks = stats.kstest(ps, "uniform").pvalue
say(f"KS p-values: min {min(ps):.3f}, max {max(ps):.3f}; their own uniformity KS p = {ks:.3f}")
if min(ps) < 1e-4:
    fails.append("vm KS")

say("\n(2) staple(): local action change = global recompute (beta = 1), 200 random links each")
for name, (lat, L, Lt) in (("void L=2 Lt=6", ("void", 2, 6)), ("Z4 L=4", ("z4", 4, None)),
                           ("void L=3 Lt=5", ("void", 3, 5))):
    a = S.get_complex(lat, L, Lt)
    rng = np.random.default_rng(777)
    th = rng.uniform(0, 2 * np.pi, a["n_links"])
    Sg = lambda t: np.sum(1 - S.loop_cos(t, a["LL"], a["LS"]))
    worst = 0.0
    for l in rng.choice(a["n_links"], 200, replace=False):
        R, phi = S.staple(th, l, a["LL"], a["LS"], a["ptr"], a["il"], a["isg"])
        new = th.copy()
        new[l] = rng.uniform(0, 2 * np.pi)
        dl = -R * (np.cos(new[l] + phi) - np.cos(th[l] + phi))
        worst = max(worst, abs(dl - (Sg(new) - Sg(th))))
    say(f"  {name}: max |dS_local - dS_global| = {worst:.1e}")
    if worst > 1e-9:
        fails.append(f"staple {name}")

say("\n(3) timing at beta = 20, cold start, 20 sweeps after 2 warm-up sweeps")
timing = {}
for name, (lat, L, Lt) in (("void L=2 Lt=6", ("void", 2, 6)), ("void L=4 Lt=12", ("void", 4, 12)),
                           ("void L=6 Lt=18", ("void", 6, 18)), ("void L=8 Lt=24", ("void", 8, 24)),
                           ("Z4 L=8", ("z4", 8, None)), ("Z4 L=12", ("z4", 12, None))):
    t0 = time.time()
    a = S.get_complex(lat, L, Lt)
    tb = time.time() - t0
    S.simulate(1, 1, a["cold"], 20.0, 2, a["LL"], a["LS"], a["LT"], a["ptr"], a["il"], a["isg"], a["n_links"])
    t0 = time.time()
    S.simulate(1, 1, a["cold"], 20.0, 20, a["LL"], a["LS"], a["LT"], a["ptr"], a["il"], a["isg"], a["n_links"])
    dt = (time.time() - t0) / 20
    timing[name] = dt
    say(f"  {name:<16s} N_l = {a['n_links']:>7d} N_loops = {a['n_loops']:>7d} build {tb:5.1f} s  {1e3*dt:8.2f} ms/sweep")
    S._CACHE.clear()

say("\n" + ("ALL UNIT TESTS PASSED" if not fails else "FAILED: " + "; ".join(fails)))
open(os.path.join(OUT, "unit_tests.txt"), "w").write("\n".join(lines) + "\n")
json.dump(dict(timing_s_per_sweep=timing, ks_p=ps, fails=fails), open(os.path.join(OUT, "unit_tests.json"), "w"), indent=1)
sys.exit(1 if fails else 0)
