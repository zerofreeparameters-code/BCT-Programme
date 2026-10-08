"""Full-distribution test of the von Mises sampler (KS against scipy.stats.vonmises)."""
import numpy as np
from numba import njit
from scipy import stats
from scipy.special import iv
import u1sim as U

@njit
def draws(k, n):
    out = np.empty(n)
    for i in range(n):
        out[i] = U.vonmises0(k)
    return out

for seed in (101, 202):
    U.nb_seed(seed)
    for k in (0.05, 0.5, 1.0, 2.0, 3.0, 8.0, 40.0):
        x = draws(k, 1_000_000)
        ks = stats.kstest(x, stats.vonmises(k).cdf)
        m = np.cos(x).mean()
        ex = iv(1, k) / iv(0, k)
        var = (1 + iv(2, k) / iv(0, k)) / 2 - ex**2
        z = (m - ex) / np.sqrt(var / len(x))
        print(f"seed={seed} kappa={k:<5g} KS p={ks.pvalue:.3f}  <cos> z={z:+.2f}")
