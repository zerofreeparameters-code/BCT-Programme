#!/usr/bin/env python3
"""
dls_rep2_routes.py -- Gate DL-STIFF, blind replication REP2 (card SHA-256 294da0f5...8e21).
Computes the kill test of every route in card section 6 (R1-R5) and of the R6 candidates found in
the pinned sources. Deterministic; mpmath 30 digits working, 10 reported; sympy for symbolic steps.

Run:  python3 -I dls_rep2_routes.py
Depends only on mpmath and sympy. Reads no files.

Sections
  0  constants, the three forms of beta_geom, and which length 'a' they assume
  1  R1  minimal coupling: Meissner mass; and no plaquette term at tree level
  2  R2  induced Maxwell term from dipole response: option-B effective action is a-independent
  3  R3  beta := phase stiffness: factorisation of Z; what 'J dimensionless' needs; duality direction
  4  R4  sigma_s = alpha_0 J (App J 1.3): re-derivation with every input named; a_e-independence;
         the TANH overlap coupling
  5  R5  induced Maxwell term from charged loops: cutoff ratio needed for 10.742
  6  R6  candidates from the pinned sources: (a) ICE E_J/E_C at nbar=1; (b) KR dual of the medium;
         (c) lattice-continuum matching on the void network
  7  Q3  comparison numbers
"""
from mpmath import mp, mpf, sqrt, pi, tanh, log, log10, nstr, exp
import sympy as sp

mp.dps = 30
R10 = 10
def p(label, v):
    print(f"  {label:<64s} {nstr(v, R10) if not isinstance(v, str) else v}")

# ---------------------------------------------------------------------------------------------
print("# 0. Constants (MINIMAL_BCT 1.3) and the geometric target")
r_oct = (sqrt(2) - 1) / 2            # MINIMAL_BCT l.56
r_tet = (sqrt(6) - 2) / 4            # MINIMAL_BCT l.57
alpha0 = r_oct * r_tet / pi          # l.58
xi = 1 / sqrt(8 * r_oct * r_tet)     # l.59, in units of MINIMAL's a
beta_geom = 1 / (4 * pi * alpha0)
alpha_codata = mpf("0.0072973525643")
p("r_oct", r_oct); p("r_tet", r_tet); p("alpha_0", alpha0); p("1/alpha_0", 1 / alpha0)
p("xi / a", xi)
p("beta_geom = 1/(4 pi alpha_0)", beta_geom)
p("          = 1/(4 r_oct r_tet)", 1 / (4 * r_oct * r_tet))
p("          = 2 xi^2/a^2  (a = MINIMAL's a)", 2 * xi**2)
p("|form1 - form3|", abs(beta_geom - 2 * xi**2))
p("1/(4 pi alpha_CODATA)", 1 / (4 * pi * alpha_codata))

print("\n  Which length is MINIMAL's 'a'?  Rebuild r_oct, r_tet from the FCC cubic cell of")
print("  gate_DL_step0_network.py (cubic edge = 1): oct void (1/2,1/2,1/2), tet void (1/4,1/4,1/4),")
print("  atoms at (1/2,1/2,0) and (0,0,0); sphere radius = half the nearest-neighbour distance.")
a_cub = mpf(1)
d_nn = a_cub / sqrt(2)
R_sph = d_nn / 2
roct_cub = mpf(1) / 2 - R_sph                  # oct centre to atom (1/2,1/2,0) = 1/2
rtet_cub = sqrt(3) / 4 - R_sph                 # tet centre to atom (0,0,0) = sqrt(3)/4
p("r_oct (cubic units) / d_nn", roct_cub / d_nn)
p("r_tet (cubic units) / d_nn", rtet_cub / d_nn)
print("  => MINIMAL's a is the nearest-neighbour distance d_nn (sphere diameter; App J/TANH: R = a/2).")
link = sqrt(3) / 4 * a_cub                      # oct-tet link length, gate_DL_step0 l.37
V_prim = a_cub**3 / 4                           # FCC primitive cell volume
a_site = (V_prim / 3) ** (mpf(1) / 3)           # volume per void node (1 oct + 2 tet per cell)
xi_abs = xi * d_nn
for name, L in (("a = d_nn (MINIMAL)", d_nn), ("a = cubic edge (Gate DL scripts)", a_cub),
                ("a = oct-tet link length (void-network spacing)", link),
                ("a = (volume per void node)^(1/3)", a_site)):
    p(f"2 xi^2 / a^2 with {name}", 2 * xi_abs**2 / L**2)
print("  beta is dimensionless; the unit-free statement is beta_geom = 1/(4 pi alpha_0) = 1/(4 r_oct r_tet).")

# ---------------------------------------------------------------------------------------------
print("\n# 1. R1 -- minimal coupling (kill test: m_A^2 = q^2 rho_s != 0)")
J, Psi0, q, A, dth = sp.symbols('J Psi0 q A dtheta', real=True)
# MINIMAL 1.2 kinetic term J |d Psi|^2 with d -> d - i q A, Psi = Psi0 e^{i theta}
L1 = sp.expand(J * Psi0**2 * (dth - q * A)**2)
m2 = sp.diff(L1.subs(dth, 0), A, 2) / 2
print("  continuum: J|(d - iqA)Psi|^2 , Psi = Psi0 e^{i theta}  ->  L =", L1)
print("  coefficient of A^2 in unitary gauge (Meissner/London term):", sp.simplify(m2),
      "  -> nonzero for q != 0 (rho_s = J Psi0^2)")
# lattice form on a window link e: J|Psi_j - e^{i q a_e} Psi_i|^2 = 2 J Psi0^2 (1 - cos(theta_j - theta_i - q a_e))
a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', real=True)
th = sp.symbols('th0:4', real=True)
links = [(0, 1, a1), (1, 2, a2), (2, 3, a3), (3, 0, a4)]   # a girth-4 O-T-O-T loop of the void network
S_link = sum(2 * J * Psi0**2 * (1 - sp.cos(th[j] - th[i] - q * a)) for i, j, a in links)
S_u = S_link.subs({t: 0 for t in th})                      # unitary gauge
H = sp.hessian(S_u, (a1, a2, a3, a4)).subs({a1: 0, a2: 0, a3: 0, a4: 0})
print("  lattice, unitary gauge, Hessian in (a1..a4) around a = 0 on one 4-loop:")
print("   ", H.tolist())
off = [H[i, j] for i in range(4) for j in range(4) if i != j]
print("  all off-diagonal (link-link) entries zero:", all(sp.simplify(x) == 0 for x in off),
      " -> tree-level matter term is link-local: a mass, no plaquette (flux) term, no contribution to beta")
print("  Verdict R1: contradicts option B (medium must be neutral); even when charged it supplies a mass, not beta.")

# ---------------------------------------------------------------------------------------------
print("\n# 2. R2 -- induced Maxwell term from dipole response (kill test: chi = 0 without polarisable charge)")
psi, psib, Ef, a0, k = sp.symbols('psi psibar E a0 k', real=True)
Vpot = sp.Function('V')
# Option B: S = S_GP[Psi] + S_W[a]. Write the medium's action as any function of the medium's fields only.
S_GP = J * psib * psi - Vpot(psib * psi)
print("  option-B medium action (MINIMAL 1.2, schematic):", S_GP)
print("  d S_GP / d E  =", sp.diff(S_GP, Ef), "  -> Gamma_medium[a] = -ln Int DPsi e^{-S_GP} is a-independent")
print("  => chi = -d^2 Gamma/dE^2 = 0 identically in option B (stronger than, and consistent with, STIFF's P = 0).")
# The only nonzero 'polarisation' in the pinned sources: STIFF CN-STIFF-03 window dipole linear in an imposed
# NUMBER bias (a chemical-potential difference). It becomes a response to the link field only if the
# number current couples to a, i.e. d_t theta -> d_t theta - q a0 : that is R1.
L_bias = sp.expand(J * Psi0**2 * (dth - q * a0)**2)
c_a0sq = sp.diff(L_bias.subs(dth, 0), a0, 2) / 2
print("  number-bias response promoted to a0 by minimal coupling: L =", L_bias)
print("  coefficient of a0^2 at k = 0:", sp.simplify(c_a0sq),
      " (k^0: a screening mass for a0, not a chi E^2 = chi k^2 a0^2 term)")
print("  Sign note: the desk check's -chi/2 is the energy convention; in the Lagrangian it is +chi/2. Zero either way.")
print("  Verdict R2: closed -- no nonzero chi exists in the pinned sources for the neutral medium.")

# ---------------------------------------------------------------------------------------------
print("\n# 3. R3 -- beta := dimensionless phase stiffness (kill test: is any term coupling a_e to Psi?)")
beta = sp.symbols('beta', positive=True)
ZGP, ZW = sp.Function('Z_GP'), sp.Function('Z_W')
lnZ = sp.log(ZGP(J)) + sp.log(ZW(beta))
print("  option B: S = S_GP[Psi; J, xi, Psi0] + beta * sum_p (1 - cos Phi_p)  =>  Z = Z_GP(J) * Z_W(beta)")
print("  d^2 lnZ / dJ dbeta =", sp.diff(lnZ, J, beta), " -> no observable links J and beta")
print("  Terms of MINIMAL 1.2: J (d Psi)^* (d Psi),  (J/4 xi^2)(|Psi|^2 - Psi0^2)^2   -- neither contains a_e.")
xi_s = sp.symbols('xi', positive=True)
K = J * Psi0**2                      # phase stiffness of the 1.2 action: J|dPsi|^2 -> J Psi0^2 (d theta)^2
print("  phase stiffness of the 1.2 action, K = J Psi0^2 ; setting K = 2 xi^2 gives J =",
      sp.solve(sp.Eq(K, 2 * xi_s**2), J), " -- J and Psi0 are not in MINIMAL 1.3, so even the")
print("  identification beta = K would not return 2 xi^2/a^2 without a further asserted value.")
# side observation: amplitude gap of the 1.2 action
h = sp.symbols('h', real=True)
Vh = sp.expand((J / (4 * xi_s**2)) * ((Psi0 + h)**2 - Psi0**2)**2)
mass2 = sp.simplify(sp.diff(Vh, h, 2).subs(h, 0) / 2 / J)   # L_h = J (dh)^2 - V  ->  m^2 = V''/(2J)
print("  [side observation] amplitude-mode m^2 of the 1.2 action =", mass2,
      " -> m = Psi0/xi; MINIMAL 1.4 prints 2/xi, i.e. Psi0 = 2 or a different kinetic normalisation.")
# Duality direction (PROMOTE Step 2 (ii): KR 2-form dual of a 3+1D superfluid)
jv, v = sp.symbols('j v', real=True)
Kp = sp.symbols('K', positive=True)
gauss = sp.integrate(sp.exp(-jv**2 / (2 * Kp) + sp.I * jv * v), (jv, -sp.oo, sp.oo))
print("  Hubbard-Stratonovich: Int dj exp(-j^2/(2K) + i j v) =", sp.simplify(gauss))
print("  i.e. stiffness K (d theta)^2/2 <-> current action j^2/(2K); with j = (1/2pi) *dB the dual 2-form")
print("  carries coefficient 1/(8 pi^2 K): the medium's own gauge field (a 1-polarisation KR 2-form, PROMOTE")
print("  CN-PROMOTE-06/10) has coupling INVERSE to the stiffness, and it is not the 1-form link field a_e.")
print("  Verdict R3: closed -- assertion; nothing in the option-B action lets a_e inherit J.")

# ---------------------------------------------------------------------------------------------
print("\n# 4. R4 -- alpha_0 as the surface coupling (App J 1.3, lines 147-173)")
Q, d, eps0, Rr, Js = sp.symbols('Q d epsilon0 R J', positive=True)
sigma = Q / (4 * sp.pi * Rr**2)               # surface charge on the sphere of radius R
dV_SI = sigma * d / eps0                      # double-layer potential step (rationalised units)
sig_s = sp.simplify(dV_SI * d)                # App J eq. (sigma): sigma_s = Delta V * d
print("  sigma = Q/(4 pi R^2); Delta V = sigma d / eps0; sigma_s = Delta V d =", sig_s)
ro, rt = sp.symbols('r_oct r_tet', positive=True)
alpha0_s = ro * rt / (4 * sp.pi * Rr**2)      # App J eq. (alpha0)
cond = sp.simplify(sig_s / Js / alpha0_s)
print("  condition sigma_s / J = alpha_0  <=>  ", sp.Eq(cond, 1), "  : one equation, four inputs (Q, d, eps0, J)")
print("  solved for d:", sp.solve(sp.Eq(cond, 1), d))
print("  App J's point: Q = 1, eps0 = 1, J = J0 = 1, d = sqrt(r_tet r_oct) (App J l.161-173 calls Q, d inputs).")
dV_G = 4 * sp.pi * sigma * d                  # Gaussian units
print("  same step in Gaussian units: sigma_s =", sp.simplify(dV_G * d),
      " -- the 1/(4 pi R^2) 'identical structure' (l.156-160) holds only in rationalised units with eps0 = 1.")
print("  STIFF 1 / CN-STIFF-05: the neutral medium has no electric charge and no eps0; Q is STIFF's e*, a free input.")
psiR = sp.symbols('PsiR', real=True)
Hint = sp.Symbol('sigma_s') * 4 * sp.pi * Rr**2 * psiR**2
print("  H_int = sigma_s Oint |Psi|^2 dS (App J l.238) =", Hint, ";  d H_int / d a_e =", sp.diff(Hint, a1),
      " -> no plaquette term; nothing maps the sphere shell to a window link.")
R_half = mpf(1) / 2
g_over = alpha0 * 4 * pi * R_half * tanh(r_oct / xi)**2
p("g (App J 3.1 overlap coupling, computed) = alpha_0 4 pi R tanh^2(r_oct/xi)", g_over)
p("alpha_0 / g", alpha0 / g_over)
print("  Verdict R4: closed -- sigma_s needs Q and d (and eps0, J units) asserted; the sphere-shell term is")
print("  independent of a_e, so the second clause of the kill test (sphere surface -> window-link plaquette) fails.")

# ---------------------------------------------------------------------------------------------
print("\n# 5. R5 -- induced Maxwell term from charged matter loops")
# one-loop: d(1/e^2)/d ln mu = -b q^2/(8 pi^2), b = 4/3 per Dirac fermion, 1/3 per complex scalar.
# induced ('beta(Lambda) = 0'): beta(m) = b q^2/(8 pi^2) ln(Lambda/m)
for name, b in (("one unit-charge Dirac fermion (b = 4/3)", mpf(4) / 3),
                ("one unit-charge complex scalar (b = 1/3)", mpf(1) / 3)):
    coef = b / (8 * pi**2)
    L_needed = beta_geom / coef
    p(f"{name}: beta = c ln(Lambda/m), c", coef)
    p("   ln(Lambda/m) needed for beta = 10.742", L_needed)
    p("   log10(Lambda/m)", L_needed / log(10))
p("check: 1/(6 pi^2) (Dirac coefficient)", 1 / (6 * pi**2))
print("  The card's '(1/12 pi^2) ln(Lambda/m)' is the Dirac coefficient written with ln(Lambda^2/m^2).")
print("  Charged matter in the pinned sources: none (MINIMAL 1.1 one neutral scalar; 1.5 vortex strings,")
print("  neutral under a field the superfluid is neutral under). Verdict R5: closed.")

# ---------------------------------------------------------------------------------------------
print("\n# 6. R6 -- candidates found in the pinned sources")
print("  (a) ICE 3 / CN-ICE-04: E_J/E_C = 2 nbar^2 (xi/a)^2. Re-derive:")
hb, m, g, a_, nb = sp.symbols('hbar m g a nbar', positive=True)
t = hb**2 / (2 * m * a_**2); U = g / a_**3; n = nb / a_**3
xi2 = hb**2 / (2 * m * g * n)
ratio = sp.simplify((2 * t * nb) / U)
print("      E_J/E_C =", ratio, " ; / (2 nbar^2 xi^2/a^2) =", sp.simplify(ratio / (2 * nb**2 * xi2 / a_**2)))
p("      at nbar = 1, a = d_nn: E_J/E_C", 2 * xi**2)
p("      equals beta_geom to", abs(2 * xi**2 - beta_geom))
for name, L in (("a = oct-tet link length", link), ("a = (volume per void node)^(1/3)", a_site)):
    p(f"      at nbar = 1, {name}", 2 * xi_abs**2 / L**2)
# rotor -> classical (d+1) XY: Villain K_s = E_J dtau, K_tau = 1/(E_C dtau); isotropic choice
EJ, EC, dtau = sp.symbols('E_J E_C dtau', positive=True)
sol = sp.solve(sp.Eq(EJ * dtau, 1 / (EC * dtau)), dtau)
K_iso = sp.simplify(EJ * sol[0])
print("      quantum rotor -> isotropic classical XY coupling K =", K_iso)
p("      K at nbar = 1, a = d_nn", sqrt(2 * xi**2))
print("      E_J, E_C are couplings of the scalar's phase theta and number; a_e appears in neither (R3's test).")
print("      nbar is not geometry-fixed (CN-ICE-08). Closed: wrong sector, nbar = 1 and a = d_nn asserted.")
print("  (b) KR 2-form dual of the medium (PROMOTE Step 2 (ii)): see section 3 -- coupling 1/(8 pi^2 K),")
print("      a 2-form with one polarisation, not a_e. Closed.")
print("  (c) Lattice-continuum matching on the void network (the only 'theorem about the network' slot):")
e, aL = sp.symbols('e a_L', positive=True); Phi = sp.symbols('Phi', real=True)
F = Phi / aL**2                                   # field strength on a hypercubic plaquette of side a_L
S_cont = aL**4 * F**2 / (2 * e**2)                # (1/4e^2) F_mn F^mn summed over one plaquette's orientation
S_wil = sp.series(beta * (1 - sp.cos(Phi)), Phi, 0, 3).removeO()
print("      continuum per plaquette:", sp.simplify(S_cont), "  Wilson:", S_wil,
      "  -> beta =", sp.solve(sp.Eq(S_cont, S_wil), beta), "(a_L cancels)")
lam = sp.symbols('lambda', positive=True)
print("      homogeneity: S_W(lambda beta) / S_W(beta) =", sp.simplify((lam * beta * (1 - sp.cos(Phi))) / (beta * (1 - sp.cos(Phi)))))
print("      On an irregular cell complex beta_p = kappa_p / e^2 with kappa_p = |*p|/|p| a pure number of the")
print("      network: geometry fixes the relative plaquette weights, never the overall 1/e^2. Closed.")
print("  (d) STIFF 3 charitable double layer -- the one pinned expression carrying the added field's")
print("      normalisation (eps0, with a charge e*). Re-run its cancellation:")
es, ep, xs, fs = sp.symbols('e_star epsilon0 xi f', positive=True)
P_ = es * nb * xs; dPhi = P_ / ep; EJ_ = hb**2 / (2 * m) * nb * fs
S_stiff = sp.simplify(dPhi / EJ_)
print("      S = DeltaPhi/E_J =", S_stiff, "; d S/d nbar =", sp.diff(S_stiff, nb),
      " -> nbar cancels, e*/eps0 does not (CN-STIFF-05 re-derived). Supplies no value. Closed.")

# ---------------------------------------------------------------------------------------------
print("\n# 7. Q3 -- comparison (no route survives; beta_geom shown for orientation only)")
for name, bc in (("hypercubic Z4, Wilson", mpf("1.0111")), ("D4, CRIT2 card convention", mpf("0.6150")),
                 ("D4, Katz-Nogradi convention", mpf("1.2300"))):
    p(f"beta_geom / beta_c [{name}]", beta_geom / bc)
    p(f"beta_CODATA / beta_c [{name}]", 1 / (4 * pi * alpha_codata) / bc)
print("  void network beta_c: DL-BETA pending.")

# ---------------------------------------------------------------------------------------------
print("\n# 8. Card section 9 forecast, scored against the outcome code of this run (SC-DLS-2)")
fc = {"SC-DLS-0": mpf(0), "SC-DLS-1": mpf("0.05"), "SC-DLS-2": mpf("0.70"), "SC-DLS-3": mpf("0.10"),
      "SC-DLS-4": mpf("0.15"), "SC-DLS-5": mpf(0)}
outcome = "SC-DLS-2"
p("sum of forecast probabilities", sum(fc.values()))
brier = sum((pv - (1 if c == outcome else 0))**2 for c, pv in fc.items())
p("multi-class Brier score (0 best, 2 worst)", brier)
p("log score ln p(outcome)", log(fc[outcome]))
p("Brier of a uniform forecast over the 6 codes, for reference", sum((mpf(1)/6 - (1 if c == outcome else 0))**2 for c in fc))
