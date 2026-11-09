#!/usr/bin/env python3
"""
Gate TWIST — Q1(b),(c).  V0 in (rho, n, phi, a) variables; is a slaved?  Is a Maxwell term
c_F (curl a)^2 with c_F > 0 generated (i) at tree level, (ii) after integrating out density
fluctuations in a gradient expansion?  Sign and scaling with xi and a.

Model (card §4, fixed):  F = ∫ [ (ħ²/2m)|∇Ψ|² + (g/2)(|Ψ|² − n0)² ] d³r ,  Ψ = √ρ χ, χ∈C², |χ|=1.
Write χ = e^{iφ} ζ with ζ a CP¹ representative, a_i = −i ζ†∂_iζ, n = ζ†σζ.  By Q1(a):
    |∇Ψ|² = (∇√ρ)² + ρ [ (∇φ + a)² + ¼(∇n)² ].

Conventions: K := ħ² n0/(2m) (superfluid stiffness, energy/length);  ξ := ħ/√(2 m g n0)
(GP healing length; the card fixes ξ = a/√(8πα0) = 2.31754 a and says use it, don't repair it).
Faddeev tensor F_ij := n·(∂_i n × ∂_j n);  curl a = ¼ ε_kij F_ij  ⇒  (curl a)² = F_ij F_ij / 8.

Part A  — symbolic: expand F to second order in δρ = ρ − n0, eliminate δρ (Gaussian / classical;
          the fluctuation determinant is texture-independent at this order), gradient-expand the
          inverse kernel (g − (ħ²/4m n0)∇²)^{-1}.
Part B  — symbolic: the kernel of the phase-mode elimination acting on a (Fourier space):
          London/transverse projector (k⁰) vs Maxwell (k²).
Part C  — numeric (mpmath, exact derivatives): [(∇n)²]² = F_ij F_ij + (∂_i n·∂_j n)² on random
          unit fields, so the sign of the induced quartic's projection on F_ijF_ij is fixed.
Part D  — numbers: c_F in units of K a², at ξ/a = 2.31754 (40 dps reported).
"""
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
random.seed(20261109)

hbar, m, g, n0, xi = sp.symbols('hbar m g n0 xi', positive=True)
drho = sp.symbols('delta_rho', real=True)
v2, dn2 = sp.symbols('v2 dn2', nonnegative=True)   # v2 = (∇φ + a)²,  dn2 = (∇n)²
k = sp.symbols('k', positive=True)

print("=" * 78)
print("PART A — V0 in (rho, n, phi, a) variables and the density integration")
print("=" * 78)
# texture-dependent gradient energy density per unit rho
Xt = hbar**2 / (2 * m) * (v2 + sp.Rational(1, 4) * dn2)           # X̃: multiplies rho
print("Gradient term:  (ħ²/2m)|∇Ψ|² = (ħ²/2m)(∇√ρ)² + ρ·X̃,   X̃ =", Xt)
print("  -> the connection a enters ONLY through v = ∇φ + a (inside v2); curl v = curl a = ½ n·∂n×∂n")
print("     is fixed by n.  a has no kinetic term of its own: it is slaved to the texture (plus gauge).")
print("  -> tree level: F is quadratic in gradients; (curl a)² is quartic in gradients. c_F(tree) = 0.")

# Expand F[n0 + δρ] to second order in δρ (local terms)
rho = n0 + drho
pot = g / 2 * (rho - n0) ** 2
F_local = rho * Xt + pot
F2 = sp.series(F_local, drho, 0, 3).removeO()
print("\nLocal functional to O(δρ²):", sp.expand(F2))
# gradient term of δρ: (ħ²/2m)(∇√ρ)² = (ħ²/8m)(∇δρ)²/ρ -> (ħ²/8m n0)(∇δρ)² at leading order
D = hbar**2 / (8 * m * n0)
print("Gradient term of δρ: (ħ²/2m)(∇√ρ)² -> (ħ²/8m n0)(∇δρ)² + O(δρ³):  D =", D)
# Quadratic form in δρ:  ½ δρ [g − 2D ∇²] δρ + δρ X̃   -> kernel in Fourier space
Kker = g + 2 * D * k**2
print("Fourier kernel of the δρ quadratic form:  K(k) =", sp.simplify(Kker))
# Eliminate δρ:  F_eff = n0 X̃ − ½ X̃ K^{-1} X̃
Kinv_series = sp.series(1 / Kker, k, 0, 6).removeO()
Kinv_series = sp.expand(Kinv_series)
print("Gradient expansion of K^{-1}(k):", Kinv_series)
# substitute g = ħ²/(2 m n0 ξ²)
gsub = hbar**2 / (2 * m * n0 * xi**2)
Kinv_xi = sp.expand(sp.simplify(Kinv_series.subs(g, gsub)))
print("  with g = ħ²/(2 m n0 ξ²):  K^{-1}(k) = (1/g)[1 − (ξ²/2) k² + (ξ⁴/4) k⁴ − ...] :")
print("   ", sp.factor(Kinv_xi))
# Real-space: k² -> −∇² acting on X̃;  ∫ X̃ k² X̃ -> +∫ (∇X̃)²  (after one integration by parts).
F_eff_quartic = -sp.Rational(1, 2) * Xt**2 / g
F_eff_six = +sp.Rational(1, 2) * (xi**2 / 2) / g        # coefficient of (∇X̃)²  (sign: −½·(−ξ²/2)/g · ∫X̃(−∇²)X̃ = +ξ²/(4g) ∫(∇X̃)²)
print("\nInduced local terms after eliminating δρ (per unit volume):")
print("  4-derivative:  −(1/2g) X̃²  =", sp.expand(F_eff_quartic.subs(g, gsub)))
print("  6-derivative:  +(ξ²/4g) (∇X̃)²   [positive; NOT a function of F_ij; valid only for textures ≫ ξ]")
# Projection on the texture-only quartic
quart_n = sp.expand(F_eff_quartic.subs(g, gsub)).coeff(dn2, 2)
print("\nCoefficient of [(∇n)²]² in the induced quartic:  ", sp.simplify(quart_n))
Kstiff = hbar**2 * n0 / (2 * m)
print("  in units of K ξ² (K = ħ²n0/2m):", sp.simplify(quart_n / (Kstiff * xi**2)), " (i.e. −Kξ²/32)")

print("\n" + "=" * 78)
print("PART B — what the medium generates for a: London (k⁰) vs Maxwell (k²)")
print("=" * 78)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kk = sp.Matrix([k1, k2, k3]); ksq = (kk.T * kk)[0]
# Eliminating φ at fixed uniform ρ = n0:  minimise K ∫ (∇φ + a)²  -> ∇²φ = −∇·a  -> residual K a_T²
# Fourier kernel acting on a_i a_j:
P_T = sp.eye(3) - kk * kk.T / ksq
print("Phase-mode elimination leaves  K a_i P^T_ij a_j ,  P^T_ij = δ_ij − k_i k_j/k²  (TRANSVERSE PROJECTOR, k⁰).")
print("A Maxwell term would be  (1/e²) k² P^T_ij  (k²).  The medium supplies k⁰ (a mass/London term), not k².")
print("Check: P^T is a projector, P^T·k = 0:", sp.simplify(P_T * P_T - P_T) == sp.zeros(3), ",", sp.simplify(P_T * kk) == sp.zeros(3, 1))
print("Equivalently K a_T² = K |curl a|²/k²  -> infrared-ENHANCED (1/k²), the opposite of Maxwell's k².")
print("This is the Meissner/Higgs/London term: the same wall as CN-LINK-10 and Gate QED (ii).")

print("\n" + "=" * 78)
print("PART C — numeric: [(∇n)²]² = F_ij F_ij + (∂_i n·∂_j n)²  on random unit fields")
print("=" * 78)
x, y, z = sp.symbols('x y z', real=True); X = (x, y, z)
def trig_poly_real():
    e = sp.Rational(random.randint(1, 4), 2)
    for _ in range(3):
        kx, ky, kz = (sp.Rational(random.randint(-2, 2)) for _ in range(3))
        ph = sp.Rational(random.randint(0, 7), 4) * sp.pi
        e += sp.Rational(random.randint(-6, 6), 4) * sp.cos(kx * x + ky * y + kz * z + ph)
    return e
worst = mp.mpf(0); worst_pos = mp.mpf(0)
for trial in range(3):
    w = sp.Matrix([trig_poly_real() for _ in range(3)])
    n = w / sp.sqrt((w.T * w)[0])
    dn = [n.diff(v) for v in X]
    dn2e = sum((dn[i].T * dn[i])[0] for i in range(3))
    FF = sum(n.dot(dn[i].cross(dn[j])) ** 2 for i in range(3) for j in range(3))
    GG = sum((dn[i].T * dn[j])[0] ** 2 for i in range(3) for j in range(3))
    f = sp.lambdify(X, [dn2e**2 - FF - GG, FF, GG], 'mpmath')
    for _ in range(5):
        pt = [mp.mpf(random.random()) * 6 - 3 for _ in range(3)]
        r, ff, gg = f(*pt)
        worst = max(worst, abs(r)); assert ff >= 0 and gg >= 0
print("  max residual of the identity:", mp.nstr(worst, 5), " (both invariants non-negative, as required)")
print("  => −c[(∇n)²]² = −c F_ijF_ij − c(∂_i n·∂_j n)²:  the projection on the Faddeev invariant is NEGATIVE.")

print("\n" + "=" * 78)
print("PART D — numbers (card §4: a = ℓ_P, ξ/a = 2.31754...)")
print("=" * 78)
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi_over_a = 1 / mp.sqrt(8 * mp.pi * alpha0)
print("  α0 = r_oct r_tet/π           =", mp.nstr(alpha0, 40))
print("  ξ/a = 1/√(8πα0)               =", mp.nstr(xi_over_a, 40))
# coefficient of F_ijF_ij from −(1/2g)X̃² restricted to the texture part:  −(ħ²/2m)²/(32 g) = −K ξ²/32
# (curl a)² = F_ijF_ij/8  =>  c_F := coefficient of (curl a)² = 8 × (−Kξ²/32) = −Kξ²/4
cF_over_Ka2 = -(xi_over_a ** 2) / 4
print("  c_F / (K a²)  [Faddeev projection of the induced quartic, (curl a)² normalisation] =", mp.nstr(cF_over_Ka2, 40))
print("  sign: NEGATIVE.  scaling: c_F = −K ξ²/4 ∝ −ξ²;  in units of a: −(ξ/a)²/4 = −1.3427...")
print("  Mixed and superflow pieces of −(1/2g)X̃²: −(Kξ²/2)·[v⁴ + ½ v² (∇n)²] — also negative.")
print("  Six-derivative remainder +(Kξ⁴/4)(∇X̃/K)² ... positive but outside the F_ij basis and outside the")
print("  expansion's validity for textures smaller than ξ = 2.3 a (sphere radius R = 0.5 a).")
print("\nQ1 summary: (a) identities PASS; (b) a is slaved to n (enters only via ∇φ + a, curl fixed by n);")
print("(c) c_F(tree) = 0; c_F(density integration) < 0 (= −Kξ²/4 on the Faddeev invariant); phase-mode")
print("integration gives a London (k⁰) term, not Maxwell (k²).  No Maxwell-type energy from the medium.")
