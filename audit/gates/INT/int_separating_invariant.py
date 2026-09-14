#!/usr/bin/env python3
"""GATE INT — separating invariant + re-derivation of App J kappa_0.
Model: Claude Opus 4.8. Corpus digest pinned in deliverable."""
import numpy as np
from scipy.optimize import brentq

print("="*64)
print("SEPARATING INVARIANT: order-parameter target homotopy")
print("="*64)
# Interior A (App I / App J): Psi in C  -> vacuum manifold S^1
# Interior B (App JH/OHC):   Psi in C^2, |Psi|^2 fixed -> target S^2
# Standard homotopy (re-derived / textbook):
#   S^1 universal cover = R (contractible) => pi_n(S^1)=0 for n>=2
#   pi_3(S^2)=Z (Hopf), generator eta:S^3->S^2
homo = {
 "Interior A  Psi in C, vacuum S^1": dict(components_real=2, target="S^1",
      pi1="Z (vortices)", pi2="0", pi3="0"),
 "Interior B  Psi in C^2 |Psi|^2=rho0, target S^2": dict(components_real="4-1=3 (raw)/2 (CP^1)",
      target="S^2", pi1="0", pi2="Z", pi3="Z (Hopf)"),
}
for k,v in homo.items():
    print(f"\n{k}\n   real comps={v['components_real']}  pi1={v['pi1']}  pi2={v['pi2']}  pi3={v['pi3']}")
print("\nA Hopf charge H is an element of pi_3(target).")
print("  target S^1: pi_3=0     -> NO Hopf charge definable (obstruction)")
print("  target S^2: pi_3=Z     -> Hopf charge H in Z definable")
print(">> The interiors differ by a homotopy invariant notation cannot change.")
print(">> Null hypothesis (one object, two notations) is FALSE.")

print("\n"+"="*64)
print("RE-DERIVE App J kappa_0 (Interior A single-component Bessel problem)")
print("="*64)
alpha0 = 0.00740806
xi = 1.0/np.sqrt(8*np.pi*alpha0)   # App I healing length
R  = 0.5                            # Planck units, App I/J
rhs = -1.0/xi + alpha0
print(f"alpha0={alpha0}  xi=1/sqrt(8*pi*alpha0)={xi:.4f}  R={R}")
print(f"eigenvalue eqn:  kappa*cot(kappa*R) = -1/xi + alpha0 = {rhs:.6f}")
def f(k): return k/np.tan(k*R) - rhs
roots=[]
grid=np.linspace(1e-3, 20, 20000)
for i in range(len(grid)-1):
    a,b=grid[i],grid[i+1]
    try:
        if np.isfinite(f(a)) and np.isfinite(f(b)) and f(a)*f(b)<0:
            r=brentq(f,a,b)
            if abs(np.tan(r*R))>1e-6 and (not roots or abs(r-roots[-1])>1e-3):
                roots.append(r)
    except Exception: pass
print("lowest interior modes kappa_n:", [f"{r:.4f}" for r in roots[:3]])
print(f">> kappa_0 = {roots[0]:.4f}  (App J states 3.3905)")
print(">> This number is Interior A's. App JH's epsilon_0=hbar^2 kappa_0^2/(2mR^2)")
print("   REUSES this single-component Bessel eigenvalue for a C^2/S^2 hopfion,")
print("   whose radial structure is not the same eigenproblem -> unjustified inheritance.")
