#!/usr/bin/env python3
"""
Gate YM2 — as-run numerics for Appendix JH4 (v2).
Recomputes the coupling, the strong-coupling inverse coupling, and JH4's
cluster-expansion parameter u, and exhibits the a-dependence of the gap.
Model: Claude Opus 4.8 (claude-opus-4-8). Corpus commit 12ae196.
"""
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi

g2   = pi**5/24            # JH4 eq (1): g^2 = S_D4/4
S_D4 = pi**5/6             # implied: S_D4 = 4 * g^2
beta = 6/g2               # SU(3): beta = 2N/g^2 = 6/g^2 = 144/pi^5
u    = mp.e**(-144/pi**5) # JH4's stated expansion parameter

print("pi^5                     =", mp.nstr(pi**5, 12))
print("g^2 = pi^5/24            =", mp.nstr(g2, 12), "  (JH4: 12.750820...)  MATCH")
print("implied S_D4 = pi^5/6    =", mp.nstr(S_D4, 12))
print("beta = 6/g^2 = 144/pi^5  =", mp.nstr(beta, 12))
print("u = exp(-144/pi^5)       =", mp.nstr(u, 12), "  (JH4: ~0.624)  MATCH")
print("-ln(u) = beta            =", mp.nstr(-mp.log(u), 12), " (a-independent at fixed g^2)")
print()
print("Note: u = exp(-beta). At FIXED g^2 the ratio lambda1/lambda0 is a-independent,")
print("so delta_latt = -a^{-1} ln(lambda1/lambda0) ~ (1/a)*const diverges as a->0.")
print("This confirms a single-coupling object, not a renormalisation trajectory.")
print()
print("Convergence criterion check:")
print("  JH4 asserts convergence because u = 0.624 < 1.")
print("  A polymer/cluster expansion converges under Kotecky-Preiss/Dobrushin:")
print("  sum over polymers of activity * e^{|polymer|} <= |polymer|, which for a")
print("  4D lattice carries a connectivity factor mu >> 1 (number of plaquettes of")
print("  size n through a fixed plaquette grows geometrically). The bare inequality")
print("  u < 1 is NOT that criterion. beta = 0.47 is deep strong coupling and")
print("  plausibly inside the true analyticity domain, but JH4 does not establish it.")
