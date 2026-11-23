#!/usr/bin/env python3
"""Convergence table and 1/N extrapolations for the void-network Bloch eigenvalues (bb2_lattice.py outputs)."""
import numpy as np
N = np.array([32, 48, 64, 96, 128, 160])          # N = 160: Gamma and X only (bb2_lattice_N160.txt); nan elsewhere
data = {                       # from bb2_lattice_N48_64.txt (and the N=32 test run), bb2_lattice_N96.txt, bb2_lattice_N128.txt
 'lambda_ac(X) = lambda_ac(W)':          [5.6141, 6.9526, 7.4758, 8.3515, 8.6364, 8.8197],
 'lambda_ac(L)':                         [3.7196, 4.3932, 4.6761, 5.1027, 5.2445, np.nan],
 '2nd band at X (gap bottom)':           [12.0291, 13.2076, 13.8889, 14.1835, 14.3606, 14.5022],
 '2nd band at L':                        [13.6561, 14.7732, 15.4667, 15.7638, 15.9382, np.nan],
 '2nd band at W (pair)':                 [14.1716, 15.4138, 16.1675, 16.5061, 16.6901, np.nan],
 '2nd band at Gamma (chamber mode)':     [22.6625, 22.9502, 23.5903, 23.7857, 23.8405, 24.0348],
 'flat triplet at Gamma':                [37.1094, 39.3398, 41.2127, 42.8457, 43.8628, 44.3997],
 'triplet at X':                         [35.5404, 37.9633, 39.6698, 41.0789, 42.0053, 42.4437],
}
print("Convergence in N (first order expected: contact-point staircase).  Extrapolations: linear a+b/N on the two finest grids,")
print("quadratic a+b/N+c/N^2 on the three finest; spread between them is the quoted uncertainty.")
print("(The K -> 0 slope |K|^2/lambda_0 — the FD tortuosity — is 2.356, 2.058, 1.943, 1.813, 1.770 at N = 32..128 and is NOT")
print(" extrapolated here: Gate BB-ALPHA is pre-registered to anchor it by a non-FD method; these are the same grid family as bells_tortuosity.py.)")
print(f"{'quantity':38s} " + " ".join(f"N={n:<4d}" for n in N) + "   lin(2 finest)  quad(3 finest)")
ext = {}
for k, v in data.items():
    v = np.array(v, float); x = 1.0 / N
    m = ~np.isnan(v); xv, vv = x[m], v[m]
    lin = np.polyfit(xv[-2:], vv[-2:], 1)[-1]
    quad = np.polyfit(xv[-3:], vv[-3:], 2)[-1]
    ext[k] = (lin, quad)
    print(f"{k:38s} " + " ".join(f"{t:7.3f}" if not np.isnan(t) else "    -  " for t in v) + f"   {lin:8.3f}      {quad:8.3f}")
mu = 0.186185
top = ext['lambda_ac(X) = lambda_ac(W)']; bot = ext['2nd band at X (gap bottom)']
print()
print(f"acoustic top lambda_X -> {min(top):.2f}-{max(top):.2f} /a^2  (free 19.74): zone-edge frequency compression sqrt(19.74/lambda_X) = {np.sqrt(19.7392/max(top)):.2f}-{np.sqrt(19.7392/min(top)):.2f}")
print(f"gap bottom min_K lambda_1 (at X) -> {min(bot):.2f}-{max(bot):.2f} /a^2;  gap ratio bottom/top = {min(bot)/max(top):.2f}-{max(bot)/min(top):.2f}  (complete gap if > 1)")
print(f"in mu: acoustic top {min(top)/mu:.0f}-{max(top)/mu:.0f} mu, gap bottom {min(bot)/mu:.0f}-{max(bot)/mu:.0f} mu;  Bogoliubov eps/mu: top {np.sqrt(np.mean(top)*(np.mean(top)+2*mu))/mu:.0f}, bottom {np.sqrt(np.mean(bot)*(np.mean(bot)+2*mu))/mu:.0f}")
print(f"omega_max = c_s sqrt(lambda_X) = {np.sqrt(min(top)):.2f}-{np.sqrt(max(top)):.2f} c_s/a   (free zone-edge sound at X would be {np.sqrt(19.7392):.2f} c_s/a)")
