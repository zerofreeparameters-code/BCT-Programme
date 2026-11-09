#!/usr/bin/env python3
"""
Gate TWIST — Q3.  Is the twist field screened in the shells, and can the shell hold the knot?

(1) λ_shell: the corpus shell (App J eq. deltashell; App JH eq. free-energy) is a δ-shell POTENTIAL
    σ_s δ(r−R)|Ψ|², σ_s = α0 J, with Ψ continuous across it (App J §1.2) — it carries NO areal superfluid
    density of its own.  Screening of a comes from the bulk London term (Q2), the same inside and outside
    the sphere (App J: same medium).  A shell screening length can only be defined after buying a shell
    thickness d with areal density n0 d: then the Pearl length Λ = 2 λ_L²/d.

(2) Virial budget: a relaxed force-free Maxwell-type knot inside a rigid sphere with B·n̂ = 0 on the wall
    exerts mean wall pressure ū_B/3 (ū_B = mean field-energy density).  The corpus surface term
    E_s = (α0 ħ²/2mR)∮|Ψ|²dA = 4π α0 K R supplies an inward pressure P_s = −dE_s/dV = α0 K / R².
    In condensation-energy units ε_c = g n0²/2 = K/(2ξ²):  P_s/ε_c = 2 α0 ξ²/R² = 1/π exactly
    (because ξ² = a²/(8π α0) and R = a/2 are fixed by the card — no fit, an identity of the inputs).

    ū_B for the minimal knot: the H = 1 Hopf map at scale R, n = z†σz with
       z1 = 2R(x+iy)/(r²+R²),  z2 = (r² − R² + 2iRz)/(r²+R²),
    field energy (1/2e²)(curl a)², curl a = ¼ ε_kij n·(∂_i n × ∂_j n).  We integrate (curl a)² over |x|<R
    exactly-differentiated, mpmath quadrature (axisymmetric → 2D).  c₁ := R⁴ ⟨(curl a)²⟩_{B_R}.
    Then ū_B/ε_c = c₁ ξ²/(e² K R⁴) and, with the Planck normalisation K a² = 1/2 (declared, as in Q2),
    needed/available = (ū_B/3)/(P_s) = π c₁ ξ² /(3 e² K R⁴).
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
a = mp.mpf(1); R = a / 2; xi = a / mp.sqrt(8 * mp.pi * alpha0)
K = 1 / (2 * a**2)
eps_c = K / (2 * xi**2)
r_tet = (mp.sqrt(6) - 2) / 4 * a; r_oct = (mp.sqrt(2) - 1) / 2 * a

print("Gate TWIST Q3 — shell screening and the virial pressure budget")
print("Inputs: a=1, R=a/2, ξ/a =", mp.nstr(xi, 15), ", α0 =", mp.nstr(alpha0, 15), ", K a² = 1/2 (declared)")
print()
print("(1) SCREENING LENGTH")
print("    Corpus shell = δ-potential on |Ψ|², Ψ continuous, zero thickness → areal superfluid density 0 →")
print("    the shell by itself screens nothing (Pearl length Λ = 2λ_L²/d → ∞ as d → 0).")
print("    Bulk London length λ_L = a/e (Q2) applies INSIDE the sphere as much as outside: the knot's own")
print("    field is Meissner-screened in the interior; 'screened in the shell, free inside' needs a medium")
print("    that differs inside and out — which A1 and App J deny.")
d = mp.sqrt(r_tet * r_oct) * a      # the corpus's asserted shell thickness (App J §1.3, input)
print("    If one BUYS a shell of thickness d = √(r_tet r_oct) a =", mp.nstr(d, 6), "a (App J's own asserted d) with areal density n0 d:")
for e2 in [mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)]:
    lamL = a / mp.sqrt(e2)
    Pearl = 2 * lamL**2 / d
    print(f"      e² = {mp.nstr(e2,3):>4}:  λ_L = {mp.nstr(lamL,5)} a,  Pearl Λ = 2λ_L²/d = {mp.nstr(Pearl,6)} a,  Λ/R = {mp.nstr(Pearl/R,6)},  Λ/d = {mp.nstr(Pearl/d,6)}")
print("    A closed shell with Λ ≫ R screens only a fraction ~R/Λ of the field: no shell screening at counted O(1) e.")
print("    Screening at R needs e² ≳ 2a²/(dR) =", mp.nstr(2 * a**2 / (d * R), 5), "— a value chosen to pass = fitting (forbidden, §8).")
print()
print("(2) VIRIAL BUDGET")
Ps_over_eps = 2 * alpha0 * xi**2 / R**2
print("    shell pressure / condensation energy density  P_s/ε_c = 2α0 ξ²/R² =", mp.nstr(Ps_over_eps, 20), " (= 1/π =", mp.nstr(1 / mp.pi, 20), ")")

# Hopf map energy density, exact derivatives
x, y, z = sp.symbols('x y z', real=True); Rs = sp.Rational(1, 2)
r2 = x**2 + y**2 + z**2
z1 = 2 * Rs * (x + sp.I * y) / (r2 + Rs**2)
z2 = (r2 - Rs**2 + 2 * sp.I * Rs * z) / (r2 + Rs**2)
zz = sp.Matrix([z1, z2]); zd = zz.H
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
n = sp.Matrix([sp.simplify(sp.re(sp.expand((zd * s * zz)[0]))) for s in (s1, s2, s3)])
X = (x, y, z)
dn = [n.diff(v) for v in X]
F = [[n.dot(dn[i].cross(dn[j])) for j in range(3)] for i in range(3)]
curl2 = sp.Rational(1, 16) * sum(F[i][j] ** 2 for i in range(3) for j in range(3)) * 2   # (curl a)² = F_ijF_ij/8
dn2 = sum((dn[i].T * dn[i])[0] for i in range(3))
f_curl2 = sp.lambdify(X, curl2, 'mpmath'); f_dn2 = sp.lambdify(X, dn2, 'mpmath')
# sanity: |n| = 1 and Hopf map has H = 1 (we check |n| only; H=1 is the standard Hopf map)
assert abs(mp.sqrt(sum(float(sp.N(c))**2 for c in n.subs({x: sp.Rational(3,10), y: sp.Rational(-1,5), z: sp.Rational(7,10)}))) - 1) < 1e-12
# axisymmetric: integrate in cylindrical (rho, z), density depends on (rho, z) only
def integrand_curl(rho, zc):
    return mp.re(f_curl2(rho, 0, zc)) * 2 * mp.pi * rho
def integrand_dn2(rho, zc):
    return mp.re(f_dn2(rho, 0, zc)) * 2 * mp.pi * rho
Rm = mp.mpf(R)
I_curl = mp.quad(lambda zc: mp.quad(lambda rho: integrand_curl(rho, zc), [0, mp.sqrt(Rm**2 - zc**2)]), [-Rm, Rm])
I_dn2 = mp.quad(lambda zc: mp.quad(lambda rho: integrand_dn2(rho, zc), [0, mp.sqrt(Rm**2 - zc**2)]), [-Rm, Rm])
V = 4 * mp.pi * Rm**3 / 3
c1 = Rm**4 * I_curl / V
c2 = Rm**2 * I_dn2 / V
print("    H=1 Hopf map at scale R, integrated over the ball |x|<R (mpmath quad):")
print("      ∫(curl a)² d³x =", mp.nstr(I_curl, 12), "  →  c₁ = R⁴⟨(curl a)²⟩ =", mp.nstr(c1, 12))
print("      ∫(∇n)² d³x     =", mp.nstr(I_dn2, 12), "  →  c₂ = R²⟨(∇n)²⟩   =", mp.nstr(c2, 12))
print("    (a) Maxwell part (BOUGHT, ∝ 1/e²):  ū_B/ε_c = c₁ ξ²/(e² K R⁴);  needed/available = (ū_B/3)/P_s = π c₁ ξ²/(3 e² K R⁴):")
for e2 in [mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)]:
    uB = c1 / (2 * e2 * Rm**4)
    ratio = (uB / 3) / (Ps_over_eps * eps_c)
    print(f"      e² = {mp.nstr(e2,3):>4}:  ū_B/ε_c = {mp.nstr(uB/eps_c,6)},  needed/available = {mp.nstr(ratio,6)}")
print("    (b) texture part (e-independent): ū_tex = (K/4)⟨(∇n)²⟩ = K c₂/(4R²):  ū_tex/ε_c =", mp.nstr(K * c2 / (4 * Rm**2) / eps_c, 8))
print("        this part PULLS INWARD (Derrick: E₂ ∝ size), so it is not a pressure the shell must hold — it is the")
print("        collapse the shell cannot stop (Gate JHF).  Only the Maxwell part pushes on the wall.")
e2_needed = mp.pi * c1 * xi**2 / (3 * K * Rm**4) / 1   # e² at which needed/available = 1
print("    The shell holds the Maxwell knot only if e² ≳", mp.nstr(e2_needed, 6), "— choosing e to pass is fitting (§8). At counted O(1) coupling the shell")
print("    is short by a factor ~", mp.nstr(e2_needed, 4), ".")
print()
print("Q3 verdict: FAIL (conditional on Q1 BOUGHT and Q2 FAIL). Screening does not follow from the model (the shell")
print("has no superfluid density of its own; bulk screening is the same inside and out); the surface term supplies")
print("P_s = ε_c/π, three orders (×2.4×10³) below the virial requirement at e² = 1.")
