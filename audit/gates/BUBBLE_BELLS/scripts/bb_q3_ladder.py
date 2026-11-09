#!/usr/bin/env python3
"""
Gate BUBBLE_BELLS Q3 — the bell ladder with PROPER exterior matching for each ℓ.

App J's s-wave condition  κ cot(κR) = −1/ξ + α0  follows from:  ψ_in = j0(κr),  ψ_out ∝ e^{−(r−R)/ξ}/r = k0(r/ξ)
(modified spherical Bessel of the 2nd kind, up to normalisation), with the δ-shell jump
      ψ'_out/ψ_out − ψ'_in/ψ_in |_R  =  −α0        (units a = 1, as App J uses it).
Check: ψ'_in/ψ_in = κ cot κR − 1/R ;  ψ'_out/ψ_out = −1/ξ − 1/R  ⇒  κ cot κR = −1/ξ + α0.  ✓ (the −1/R cancels)
Generalisation to ℓ ≥ 1:  ψ_in = j_ℓ(κr),  ψ_out = k_ℓ(r/ξ)  ⇒
      κ j_ℓ'(κR)/j_ℓ(κR)  =  (1/ξ) k_ℓ'(R/ξ)/k_ℓ(R/ξ) + α0 .
The desk-check instead applied the s-wave Robin constant to all ℓ; here we see how much that mattered.
"""
import mpmath as mp
mp.mp.dps = 30
a = mp.mpf(1); R = a / 2
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = a / mp.sqrt(8 * mp.pi * alpha0)

def jl(l, x):  return mp.sqrt(mp.pi / (2 * x)) * mp.besselj(l + mp.mpf(1) / 2, x)
def kl(l, x):  return mp.sqrt(mp.pi / (2 * x)) * mp.besselk(l + mp.mpf(1) / 2, x)   # ∝ modified spherical Bessel k_ℓ
def dlog(f, x): return mp.diff(f, x) / f(x)

zeros = {0: mp.pi, 1: mp.mpf('4.4934094579090641753'), 2: mp.mpf('5.7634591968945497914'), 3: mp.mpf('6.9879320005005192255')}
print("Gate BUBBLE_BELLS Q3 — bell ladder with k_ℓ(r/ξ) exterior matching (a = 1, R = 1/2, ξ =", mp.nstr(xi, 10), ")")
print("   ℓ   rhs = k_ℓ'/k_ℓ/ξ + α0     κ_ℓ            κ_ℓ R      E_ℓ/E_0    desk-check E_ℓ/E_0 (inherited Robin)")
desk = {0: 1.0, 1: 2.8139583, 2: 5.4516692, 3: 8.8868568}
kap = {}
for l in range(4):
    rhs = dlog(lambda x, l=l: kl(l, x), R / xi) / xi + alpha0
    f = lambda k, l=l, rhs=rhs: k * mp.diff(lambda t: jl(l, t), k * R) / jl(l, k * R) - rhs
    # first root below the first zero of j_ℓ(κR)
    xs = [mp.mpf(i) / 400 * zeros[l] for i in range(1, 400)]
    br = None
    for x1, x2 in zip(xs[:-1], xs[1:]):
        if f(x1 / R) * f(x2 / R) < 0: br = (x1 / R, x2 / R); break
    k = mp.findroot(f, br, solver='bisect')
    kap[l] = k
    print(f"   {l}   {mp.nstr(rhs, 10):>14}     {mp.nstr(k, 10):>12}   {mp.nstr(k*R, 8):>8}   {mp.nstr((k/kap[0])**2, 8):>9}      {desk[l]}")
print()
print("   κ0 reproduces App J's 3.3905:", mp.nstr(kap[0], 8), "→", "YES" if abs(kap[0] - mp.mpf('3.3905')) < 5e-4 else "NO")
print("   E1/E0 proper =", mp.nstr((kap[1]/kap[0])**2, 6), " vs desk-check 2.814 → change", mp.nstr(((kap[1]/kap[0])**2 / 2.8139583 - 1) * 100, 3), "%")
print("   ΔE(ℓ=1) = κ1² − κ0² =", mp.nstr(kap[1]**2 - kap[0]**2, 6), "ħ²/2m a²")
