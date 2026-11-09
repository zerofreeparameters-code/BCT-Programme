#!/usr/bin/env python3
"""
Gate BUBBLE_BELLS Q4 — the zero-parameter number list the bubble-bells reading commits to (CONJECTURE).
Inputs: a = ℓ_P, R = a/2, ξ = a/√(8πα0), α_∞ (tortuosity, from Q1/desk-check), κ_ℓ (Q3), AZ6's identification
of the macroscopic sound speed with c.  Nothing fitted.
"""
import mpmath as mp
mp.mp.dps = 30
a = mp.mpf(1); R = a / 2
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = a / mp.sqrt(8 * mp.pi * alpha0)
phi = 1 - mp.pi / (3 * mp.sqrt(2))
alpha_inf = mp.mpf('1.64'); d_alpha = mp.mpf('0.03')
kap = [mp.mpf('3.390462612'), mp.mpf('6.305047667'), mp.mpf('8.99198018'), mp.mpf('11.52885231')]

print("Gate BUBBLE_BELLS Q4 — committed numbers (all CONJECTURE, zero free parameters)")
print(f"  N1  porosity of the void network            φ = 1 − π/(3√2) = {mp.nstr(phi, 8)}          [PROVEN geometry]")
print(f"  N2  tortuosity of the FCC void network      α_∞ = {mp.nstr(alpha_inf,3)} ± {mp.nstr(d_alpha,2)}                    [numerical; falsified if an exact/independent value lies outside 1.5–1.8]")
print(f"  N3  macroscopic sound speed                 c_eff/c_s = 1/√α_∞ = {mp.nstr(1/mp.sqrt(alpha_inf),4)} ± {mp.nstr(d_alpha/(2*alpha_inf**1.5),3)}      [follows from N2 + superleak physics (JKD 1987)]")
print(f"  N4  isotropy of c_eff at O(k²)              exact (cubic symmetry); first anisotropy O(k⁴) (Gates RATIO/WHY√2)")
print(f"  N5  bell ladder κ_ℓ a (ℓ = 0..3)            {', '.join(mp.nstr(k,7) for k in kap)}      [App J BC with k_ℓ(r/ξ) matching]")
print(f"  N6  ladder ratios E_ℓ/E_0                   {', '.join(mp.nstr((k/kap[0])**2,5) for k in kap)}")
cs_over_hbar2m = mp.sqrt(2) / xi               # c_s in units of (ħ²/2m)/a... see bells_resonator: ω0 a/c_s = ξ κ0²/√2
w0_over_cs = xi * kap[0]**2 / mp.sqrt(2)
w_zb_over_cs = mp.pi * mp.sqrt(1 + mp.pi**2 * xi**2 / 2)
print(f"  N7  bell note vs host sound                 ω0 a/c_s = ξκ0²/√2 = {mp.nstr(w0_over_cs,5)};  ω0/ω(π/a) = {mp.nstr(w0_over_cs/w_zb_over_cs,4)}  [bell at the zone edge]")
print(f"  N8  rigidity requirement                    soft shell fails (collapse ~4 t_P; P0/P_cap ≈ 250) ⇒ spheres rigid = Horn A")
m_noalpha = 1 / (mp.sqrt(2) * xi)
m_alpha = 1 / (mp.sqrt(2 * alpha_inf) * xi)
print(f"  N9  condensate particle mass implied by c_eff = c (AZ6's identification) with the corpus ξ:")
print(f"        without tortuosity (c_s = c):   m/m_P = 1/(√2 ξ/a) = {mp.nstr(m_noalpha,5)}")
print(f"        with tortuosity (c_s/√α_∞ = c): m/m_P = 1/(√(2α_∞) ξ/a) = {mp.nstr(m_alpha,5)} ± {mp.nstr(m_alpha*d_alpha/(2*alpha_inf),3)}")
print(f"        (AZ6's g = mc²/n0 becomes g = α_∞ mc²/n0; the printed 'c_s = c' is the microscopic speed, the observable one is c_eff)")
print(f"  N10 sub-resonant correction from the bells  ~ f (ω/ω0)² ≲ 1e-28 for any observed ω  ⇒ none")
