#!/usr/bin/env python3
"""
Bubble-bells desk-check, part 2 (non-gate, CONJECTURE-capped): the bells themselves.

Corpus inputs only: a = ℓ_P = 1, R = a/2, ξ = a/√(8πα0), κ0 from App J's BC, shell tension σ_sh = α0 ħ² n0/(2mR)
(the App JH surface term per unit area), Josephson coupling g_J = α0·4πR·tanh²(r_oct/ξ) (App J §3.1),
Planck normalisation n0 a³ = 1, m = m_P (K a² = ħ²n0/2m · a² = 1/2 ⇒ ħ²/2m = 1/2 in units ħ = c = a = 1).

B1  Bell frequency vs the host's sound: ω0 = ħκ0²/2m (free-particle regime since κ0 ξ ≫ 1), Bogoliubov
    ω(k) = c_s k √(1 + k²ξ²/2), c_s = ħ/(√2 m ξ);  which host wavenumber is resonant with the bell; how far
    the bell sits above the zone-boundary phonon (k = π/a) and above any observed frequency.
B2  Rigidity: can the sphere be a soft bubble?  (i) an EMPTY cavity with surface tension and no internal
    pressure collapses (Rayleigh) in τ ~ √(ρ R³/σ_sh);  (ii) ONE quantum in the κ0 mode exerts a zero-point
    pressure P0 = (2/3)E0/V that dwarfs the capillary pressure 2σ_sh/R.  Either way: the sphere must be a rigid
    prior structure (Horn A) — the corpus's own position.
B3  Driving: coupling of the bell to the host is App J's Josephson number g_J; a rough quality factor Q ~ 1/g_J.
B4  Size of the sub-resonant correction: a Liu-type local resonator contributes to the effective compressibility
    a term ∝ f·(ω/ω0)²/(1 − ω²/ω0²); at any observable ω this is (ω/ω0)² ≲ 1e-26.  So below resonance the ONLY
    effect of the bells is the rigid-matrix (tortuosity) renormalisation of part 1.
"""
import mpmath as mp
mp.mp.dps = 30
a = mp.mpf(1); R = a / 2
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = a / mp.sqrt(8 * mp.pi * alpha0)
r_oct = (mp.sqrt(2) - 1) / 2 * a
k0 = mp.findroot(lambda k: k * mp.cot(k * R) - (-1 / xi + alpha0), 3.39)
h2_2m = mp.mpf(1) / 2                     # ħ²/2m in Planck normalisation (n0 = 1, m = m_P, a = 1)
cs = mp.sqrt(2) * h2_2m / xi              # c_s = ħ/(√2 m ξ) = 2·(ħ²/2m)/(√2 ξ)
rho = mp.mpf(1)                           # mass density m n0 = 1

print("B1 — the bell's note")
w0 = h2_2m * k0**2
print("   κ0 =", mp.nstr(k0, 8), " ω0 = ħκ0²/2m =", mp.nstr(w0, 6), " (Planck units);  c_s = ħ/(√2 mξ) =", mp.nstr(cs, 6), " ⇒ ω0 a/c_s =", mp.nstr(w0 / cs, 6))
bog = lambda k: cs * k * mp.sqrt(1 + k**2 * xi**2 / 2)
k_res = mp.findroot(lambda k: bog(k) - w0, 3.0)
print("   host Bogoliubov mode resonant with the bell: k_res =", mp.nstr(k_res, 6), "/a  (k_res ξ =", mp.nstr(k_res * xi, 5), "≫ 1: particle-like, not phonon-like)")
w_zb = bog(mp.pi / a)
print("   zone-boundary phonon ω(π/a) =", mp.nstr(w_zb, 6), " ⇒ ω0/ω(π/a) =", mp.nstr(w0 / w_zb, 5))
w_obs = mp.mpf('1e30') / mp.mpf('1.855e43')   # ~PeV photon angular frequency in units of c/ℓ_P
print("   hardest observed photon ω ≈ 1e30 rad/s = ", mp.nstr(w_obs, 3), " c/a  ⇒ (ω/ω0)² ≈", mp.nstr((w_obs / w0)**2, 3))
print()
print("B2 — must the sphere be rigid?")
sig_sh = alpha0 * 2 * h2_2m * 1 / (2 * R)          # α0 ħ² n0/(2 m R) with n0 = 1  → α0 (ħ²/2m)·2/(2R)... = α0 (ħ²/2m)/R
sig_sh = alpha0 * h2_2m / R
tau_R = mp.sqrt(rho * R**3 / sig_sh)
print("   shell tension σ_sh = α0 ħ² n0/(2mR) =", mp.nstr(sig_sh, 6), " (Planck units)")
print("   (i) empty cavity, no internal pressure: Rayleigh collapse time τ ~ √(ρR³/σ_sh) =", mp.nstr(tau_R, 4), "t_P — a soft empty bubble is gone in a few Planck times")
E0 = w0; V = 4 * mp.pi * R**3 / 3
P0 = mp.mpf(2) / 3 * E0 / V
P_cap = 2 * sig_sh / R
print("   (ii) one quantum in the κ0 mode: zero-point pressure P0 = (2/3)E0/V =", mp.nstr(P0, 5), " vs capillary 2σ_sh/R =", mp.nstr(P_cap, 5), " ⇒ P0/P_cap =", mp.nstr(P0 / P_cap, 5))
print("   ⇒ a soft shell can neither hold an empty bubble up nor hold a rung bell in: the sphere is a RIGID prior structure.")
print("     That is Horn A (Gate U″ / lattice imposed) restated from the bubble side — consistent, not new.")
print()
print("B3 — what can ring it")
gJ = alpha0 * 4 * mp.pi * R * mp.tanh(r_oct / xi)**2
print("   App J Josephson coupling g_J = α0·4πR·tanh²(r_oct/ξ) =", mp.nstr(gJ, 5), " ⇒ rough Q ~ 1/g_J ≈", mp.nstr(1 / gJ, 4))
print("   Only a host excitation at k ≈", mp.nstr(k_res, 4), "/a (a Planck-scale Bogoliubov particle) is resonant; nothing in the observed")
print("   spectrum is within 13 orders of magnitude of the bell. Bells are silent in the low-energy world.")
print()
print("B4 — size of the resonant correction below resonance")
f = mp.pi / (3 * mp.sqrt(2))
print("   Liu-type correction to effective compressibility ~ f (ω/ω0)² ≈", mp.nstr(f * (w_obs / w0)**2, 3), " at the hardest observed photon → zero for all purposes.")
print("   So the sub-resonant vacuum = superfluid in a rigid FCC superleak: c_eff = c_s/√α_∞ with α_∞ from part 1, nothing else.")
