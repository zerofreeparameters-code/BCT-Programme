# -*- coding: utf-8 -*-
r"""
DESK CHECK routeC — illustrates the CN-BZ category-error claim with textbook machinery.
NOT a verification of Gate IG's specific number; it shows the STRUCTURE of Sakharov
induced gravity so the reconciliation knows what to look for in the IG deliverable.

Heat-kernel (Sakharov) induced gravity, massive Laplace-type operator Delta+m^2 in d dims:
  one-loop W = (1/2) ln det(Delta+m^2) = -(1/2) \int_eps^inf (ds/s) Tr e^{-s(Delta+m^2)}
  Tr e^{-s Delta} ~ (4 pi s)^{-d/2} sum_k a_k s^k ;  a_1 ∝ \int sqrt(g) R  (Einstein-Hilbert)
Induced 1/G = coefficient of \int sqrt(g) R. Extract its eps-dependence in d=4 and confirm
NO Brillouin-zone momentum integral \int_BZ d^3k appears.
"""
import sympy as sp
s, eps, m = sp.symbols('s epsilon m', positive=True)

def contrib(k, d):
    # (drop constant prefactors) proper-time integral for SD coefficient a_k in dim d
    return sp.integrate(s**(k - sp.Rational(d,2) - 1) * sp.exp(-s*m**2), (s, eps, sp.oo))

print("d=4, proper-time cutoff eps (dim length^2), IR-regulated by mass m:")
labels = {0:"cosmological (a0 ∝ Vol)",1:"EINSTEIN-HILBERT (a1 ∝ ∫√g R) → 1/G",2:"R^2 (a2, log)"}
for k in [0,1,2]:
    val = sp.simplify(contrib(k,4))
    lead = sp.series(val, eps, 0, 1).removeO() if k<2 else "~ -ln(eps m^2) - gamma_E"
    print(f"  k={k}: {sp.nsimplify(val)}    leading eps->0: {lead}    [{labels[k]}]")

print()
print("=> Induced 1/G ∝ a1 · (1/eps): set by the single proper-time cutoff eps.")
print("   No ∫_BZ d^3k anywhere — the zone SHAPE (trunc. octahedron vs Debye sphere)")
print("   does not enter. 'Sharpen the zone' refines a momentum domain the method lacks.")
print("   The free 'moment index p' (CN-BZ: span 4.18%) lives here: which SD moment /")
print("   which power of eps is called 1/G, and the shape factor mapping a k-cutoff to eps.")
