#!/usr/bin/env python3
"""
Gate LINK, Step 3 numbers: healing length ratio, lattice-gauge coupling beta,
monopole action.  Inputs are the corpus's own formulae, quoted at source:
  alpha0 = (sqrt6-2)(sqrt2-1)/(8pi)              [App D.3 Sec 5.2]
  xi     = a / sqrt(8 pi alpha0),  a = l_P       [App F, Vol1 Part1 line ~3003]
  J      = 1/(4 pi alpha0)                       [App E.1 Sec 3.3]
  S_mono = 4 pi^2 J                              [App E.1 Sec 3.3]
mpmath, 60 dps working, 40 dps reported.
"""
from mpmath import mp, mpf, sqrt, pi, exp, log
mp.dps = 60
a0 = (sqrt(6)-2)*(sqrt(2)-1)/(8*pi)
alpha = a0*(1-2*a0)
xi_over_a = 1/sqrt(8*pi*a0)
J = 1/(4*pi*a0)
S_mono = 4*pi**2*J
def r(x,n=40): return mp.nstr(x, n)
print("alpha0                 =", r(a0))
print("alpha = a0(1-2a0)      =", r(alpha), "  1/alpha =", r(1/alpha))
print("xi/a = 1/sqrt(8 pi a0) =", r(xi_over_a))
print("xi/r_oct               =", r(xi_over_a/((sqrt(2)-1)/2)))
print("xi/R (R=0.5 a)         =", r(xi_over_a/mpf('0.5')))
print("J = 1/(4 pi alpha0)    =", r(J), "   <-- this is beta of the Wilson action (1/e^2 = J)")
print("S_mono = 4 pi^2 J      =", r(S_mono))
print("exp(-S_mono)           =", mp.nstr(exp(-S_mono), 8))
print()
print("Corpus states S_mono ~ 34 and P ~ 2e-15.  Check what gives 34:")
print("  exp(-34)             =", mp.nstr(exp(-34),4))
for name, val in [("4 pi^2 J", 4*pi**2*J), ("pi/alpha0", pi/a0),
                  ("pi/(4 a0 alpha)", pi/(4*a0*alpha)), ("4 pi^2 alpha0*J^2", 4*pi**2*a0*J**2),
                  ("-ln(2e-15)", -log(mpf('2e-15')))]:
    print(f"  {name:<18} = {mp.nstr(val,8)}")
print()
print("Compact U(1) 4D Wilson action: confinement for beta < beta_c ~ 1.01 (literature).")
print("  BCT beta = J =", r(J,12), " -> beta/beta_c =", mp.nstr(J/mpf('1.011'),6))
