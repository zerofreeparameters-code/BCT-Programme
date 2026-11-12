#!/usr/bin/env python3
"""
rep3_routes.py -- Gate DL-STIFF, blind replication REP3. Q1 route ledger (R1-R6) and Q3 table.

Deterministic. mpmath 30 digits working, 10 reported; sympy for symbolic steps (card §4.4).
Run from any directory:  python3 -I rep3_routes.py
Inputs are only the MINIMAL_BCT §1.3 definitions and the formulas quoted (with line numbers) from
the eleven sources pinned in card §4.1. Nothing here adds a coupling, a field or a definition of
alpha (card §4.5); where a route needs an identification, the script states it as an input.
"""
from mpmath import mp, mpf, sqrt, pi, log, log10, tanh, nstr, binomial
import sympy as sp

mp.dps = 30
N10 = lambda v: nstr(v, 10)


def p(label, v):
    print(f"  {label:<62s} {v if isinstance(v, str) else N10(v)}")


def head(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)


# ---------------------------------------------------------------------------------------------
head("0. Constants (MINIMAL_BCT §1.3) and the target number beta_geom = 2 xi^2/a^2")
# ---------------------------------------------------------------------------------------------
r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4              # MINIMAL_BCT writes (sqrt6-2)/4; dls_deskcheck writes (sqrt(3/2)-1)/2
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)
beta_geom = 2 * xi ** 2
alpha_codata = mpf("0.0072973525643")   # the value dls_deskcheck.py uses, for comparison only
p("r_oct", r_oct); p("r_tet", r_tet); p("alpha_0", alpha0); p("xi/a", xi)
p("beta_geom = 2 xi^2/a^2", beta_geom)
p("1/(4 pi alpha_0) - 2 xi^2   (30-digit residual)", abs(1 / (4 * pi * alpha0) - beta_geom))
p("1/(4 r_oct r_tet) - 2 xi^2  (30-digit residual)", abs(1 / (4 * r_oct * r_tet) - beta_geom))
s6 = sp.sqrt(6)
print("  sympy: (sqrt6-2)/4 - (sqrt(3/2)-1)/2 =",
      sp.simplify((s6 - 2) / 4 - (sp.sqrt(sp.Rational(3, 2)) - 1) / 2), "  (the two r_tet forms agree exactly)")
ro, rt = sp.symbols("r_oct r_tet", positive=True)
xi_s = 1 / sp.sqrt(8 * ro * rt)
print("  sympy: 1/(4 pi alpha_0) - 2 xi^2 =", sp.simplify(1 / (4 * sp.pi * ro * rt / sp.pi) - 2 * xi_s ** 2),
      "  (identity, exact by definition)")

# ---------------------------------------------------------------------------------------------
head("R1. Minimal coupling: condensate charged under a_e  (kill test: m_A^2 = q^2 rho_s != 0)")
# ---------------------------------------------------------------------------------------------
x = sp.symbols("x", real=True)
J, rho0, q, A, e2 = sp.symbols("J rho0 q A e2", positive=True)
dth = sp.symbols("dtheta", real=True)                         # local phase gradient d(theta)/dx
Psi = sp.sqrt(rho0) * sp.exp(sp.I * dth * x)
D = sp.diff(Psi, x) - sp.I * q * A * Psi                      # covariant derivative, constant A
kin = sp.simplify(sp.expand(J * D * sp.conjugate(D)))           # J |(d - i q A) Psi|^2
print("  continuum  J|(d - iqA)Psi|^2 with Psi = sqrt(rho0) e^{i theta}  =", sp.factor(kin))
kin_u = sp.expand(kin)
coefA2 = sp.diff(kin_u.subs(dth, 0), A, 2) / 2
print("  unitary gauge (dtheta -> 0): coefficient of A^2 in L_medium =", coefA2,
      " -> with -(1/4e^2)F^2:  m_A^2 = 2 e^2 * coeff =", sp.simplify(2 * e2 * coefA2))
print("  coefficient of (dA)^2 in L_medium at tree level =", 0,
      " (minimal coupling contains A, not dA: it gives a MASS, never a Maxwell/beta term)")
# lattice form on one window link: J|Psi_j - e^{i q a} Psi_i|^2 with |Psi| = Psi0
a_l, Psi0, dt_l = sp.symbols("a Psi0 Delta_theta", real=True)
link = 2 * J * Psi0 ** 2 * (1 - sp.cos(dt_l - q * a_l))
print("  lattice link energy 2 J Psi0^2 (1 - cos(Delta_theta - q a)); d^2/da^2 at Delta_theta=0, a=0 =",
      sp.simplify(sp.diff(link, a_l, 2).subs({dt_l: 0, a_l: 0})))
print("  option B sets q = 0  -> coefficient of A^2 =", coefA2.subs(q, 0),
      " : R1 is not the neutral medium of option B; it contradicts the construction.  R1 CLOSED.")

# ---------------------------------------------------------------------------------------------
head("R2. Induced Maxwell term from the medium's dipole response  (kill test: chi = dP/dE = 0 ?)")
# ---------------------------------------------------------------------------------------------
# Pinned action (MINIMAL_BCT §1.2): S = J (dPsi)^*(dPsi) - (J/4 xi^2)(|Psi|^2 - Psi0^2)^2.
# Option B adds the Wilson term in a_e only. Represent one Fourier component: field a, its time
# derivative ad (E = -ad - grad a0), and the medium variables psi_r, psi_i, their derivatives.
pr, pim, dpr, dpi, xi_sym, ad, a0g = sp.symbols("psi_r psi_i dpsi_r dpsi_i xi adot grad_a0", real=True)
Psi2 = pr ** 2 + pim ** 2
L_med_B = J * (dpr ** 2 + dpi ** 2) - J / (4 * xi_sym ** 2) * (Psi2 - Psi0 ** 2) ** 2   # q = 0: no a at all
# E = -adot - grad_a0, so dL/dE and d^2L/dE^2 are read off from the adot dependence
P_B = sp.diff(L_med_B, ad)
chi_B = sp.diff(L_med_B, ad, 2)
print("  option B medium Lagrangian contains a_e?  free symbols:", sorted(map(str, L_med_B.free_symbols)))
print("  P  = dL_medium/dE  =", sp.simplify(P_B), "    chi = d^2 L_medium/dE^2 =", chi_B)
# The card-§7 form: dipole response P = P0 + chi E contributes -chi/2 to the E^2 coefficient
chi, P0, E = sp.symbols("chi P0 E", real=True)
U = -sp.integrate(P0 + chi * E, E)
print("  card §7 form: U(E) = -int(P0 + chi E)dE =", sp.expand(U), "-> E^2 coefficient", sp.diff(U, E, 2) / 2,
      "; at chi = 0:", (sp.diff(U, E, 2) / 2).subs(chi, 0))
# even with q != 0 the TREE-LEVEL medium gives no E^2 term (only a mass): chi needs loops (= R5)
L_med_q = J * ((dpr + q * A * pim) ** 2 + (dpi - q * A * pr) ** 2) - J / (4 * xi_sym ** 2) * (Psi2 - Psi0 ** 2) ** 2
print("  for comparison, q != 0 at tree level: d^2 L/d(adot)^2 =", sp.diff(L_med_q, ad, 2),
      "(the charged medium also gives chi = 0 at tree level; a nonzero chi needs loops of charged matter = R5)")
print("  STIFF (pinned): number dipole p = int z dn dz = 0 by reflection symmetry (CN-STIFF-01); re-derived")
print("  numerically in rep3_r2_gp_throat.py. Its only nonzero response is to a NUMBER bias (a chemical-")
print("  potential step), which in option B is not E of a_e.  chi = 0 from every pinned term.  R2 CLOSED.")

# ---------------------------------------------------------------------------------------------
head("R3. beta := dimensionless phase stiffness (Josephson-array analogy)  (kill test: any term a_e<->Psi?)")
# ---------------------------------------------------------------------------------------------
beta_s, Wc = sp.symbols("beta W_C", positive=True)
Phi = sp.symbols("Phi_p", real=True)
S_W = beta_s * (1 - sp.cos(Phi))                      # DL / card §1: Wilson term, a_e only
S_tot = L_med_B + S_W
print("  option B total action = S_GP[Psi] + S_W[a]; mixed derivatives d^2 S/(d psi d Phi):",
      [sp.diff(S_tot, v, Phi) for v in (pr, pim, dpr, dpi)])
print("  => Z = Z_GP(J, xi, Psi0) * Z_W(beta): every a_e observable is independent of J (d/dJ log Z_W = 0).")
print("  MINIMAL_BCT §1.3 lists r_oct, r_tet, alpha_0, xi -- it gives NO value for J itself.")
# Sharpest pinned form of R3: Gate ICE (CN-ICE-04) Bose-Hubbard map. Re-derived here:
hb, m, g, a, nbar = sp.symbols("hbar m g a nbar", positive=True)
t_hop = hb ** 2 / (2 * m * a ** 2)
EJ = 2 * t_hop * nbar
EC = g / a ** 3
xi2 = hb ** 2 / (2 * m * g * (nbar / a ** 3))
ratio = sp.simplify(EJ / EC)
print("  ICE map: E_J = 2 t nbar, t = hbar^2/(2 m a^2), E_C = U = g/a^3, xi^2 = hbar^2/(2 m g n), n = nbar/a^3")
print("  E_J/E_C =", ratio, " ;  E_J/E_C - 2 nbar^2 xi^2/a^2 =", sp.simplify(ratio - 2 * nbar ** 2 * xi2 / a ** 2))
val_n1 = 2 * xi ** 2                                     # nbar = 1
p("E_J/E_C at nbar = 1  (= 2 xi^2/a^2)", val_n1)
p("  ... minus beta_geom (30 digits)", abs(val_n1 - beta_geom))
p("E_J/E_C at nbar = 1 with E_C = U/2 convention", 4 * xi ** 2)
p("E_J/E_C at nbar = 1 with E_J = t nbar convention", xi ** 2)
p("E_J/E_C at nbar = 2", 8 * xi ** 2)
print("  So 2 xi^2/a^2 IS present in the pinned sources -- as a phase-sector ratio E_J/E_C, equal to beta_geom")
print("  only at nbar = 1 (ICE CN-ICE-08: nbar is not fixed by geometry) and only in one O(1) convention.")
print("  Nothing in the pinned action carries it into the a_e sector (mixed derivatives = 0 above).")
print("  JJ-array analogue: plaquette energy Phi^2/(2 L_loop); d/dE_J of it = 0 (independent scale).  R3 CLOSED.")

# ---------------------------------------------------------------------------------------------
head("R4. alpha_0 as surface/boundary coupling, App J §1.3 lines 147-173  (re-derive sigma_s, list inputs)")
# ---------------------------------------------------------------------------------------------
Q, d, Rr, eps0 = sp.symbols("Q d R epsilon0", positive=True)
sigma_q = Q / (4 * sp.pi * Rr ** 2)                 # surface charge density of a sphere carrying Q
dV_HL = sigma_q * d / eps0                           # double-layer potential step (field sigma/eps0 across d)
sig_s = sp.simplify(dV_HL * d)                       # App J eq.(sigma): sigma_s = DeltaV * d
print("  sigma_s = DeltaV * d = (Q/(4 pi R^2 eps0)) d * d =", sig_s, " ; eps0 = 1 gives App J line 153:",
      sp.simplify(sig_s.subs(eps0, 1)))
alpha0_D = rt * ro / (4 * sp.pi * Rr ** 2)           # App J line 158 (App D formula)
cond = sp.simplify(sig_s.subs(eps0, 1) / alpha0_D)
print("  sigma_s / alpha_0(App D) =", cond, "  -> sigma_s = alpha_0  iff  Q d^2 = r_tet r_oct  (R drops out)")
print("  one equation, two unknowns: a one-parameter family; App J picks Q=1, d=sqrt(r_tet r_oct) and itself")
print("  labels the choice an input (lines 172-173, 385-386).")
for Qv in (mpf(1), mpf(1) / 2, mpf(2), mpf(3)):
    dv = sqrt(r_tet * r_oct / Qv)
    p(f"  Q = {N10(Qv):>4s}  ->  d = sqrt(r_tet r_oct / Q) =", dv)
    p("        sigma_s (HL, R = 1/2) =", Qv * dv ** 2 / (4 * pi * mpf(1) / 4))
p("Gaussian units (DeltaV = 4 pi sigma d) with App J's Q, d: sigma_s = Q d^2/R^2 =", r_tet * r_oct / (mpf(1) / 4))
p("  = 4 pi alpha_0 =", 4 * pi * alpha0)
print("  -> the boxed sigma_s = alpha_0 also needs the Heaviside-Lorentz choice eps0 = 1 (factor 4 pi otherwise).")
print("  STIFF (pinned): the neutral condensate has no electric charge Q at all (CN-STIFF-01/02/07).")
# the computed Josephson g of App J §3.1 (TANH)
R_half = mpf(1) / 2
g_comp = alpha0 * 4 * pi * R_half * tanh(r_oct / xi) ** 2
p("App J §3.1 g = alpha_0 * 4 pi R * tanh^2(r_oct/xi)", g_comp)
p("  alpha_0 / g", alpha0 / g_comp)
p("  discarded factor 4 pi R tanh^2(r_oct/xi)", 4 * pi * R_half * tanh(r_oct / xi) ** 2)
# the transfer step the card requires: sphere-surface potential -> window-link plaquette coupling
dlt = sp.symbols("delta_shell", positive=True)      # stands for delta(r - R) on the sphere surface
H_shell = sp.Symbol("sigma_s") * dlt * Psi2         # App J line 111 / 238: a potential acting on |Psi|^2
print("  App J's sigma_s term:", H_shell, " ; d/dPhi_p of it =", sp.diff(H_shell, Phi),
      " (it lives in the Psi sector on sphere surfaces, not on window loops)")
print("  To reach beta one would further need beta := 1/(4 pi sigma_s), an identification (forbidden, §4.5).")
p("  if it were made: beta = 1/(4 pi alpha_0) =", 1 / (4 * pi * alpha0))
p("  with the computed g instead: 1/(4 pi g) =", 1 / (4 * pi * g_comp))
print("  R4 CLOSED: sigma_s = alpha_0 needs Q = 1, d = sqrt(r_tet r_oct) (and eps0 = 1), and no term moves it to a_e.")

# ---------------------------------------------------------------------------------------------
head("R5. Induced Maxwell term from charged-matter loops  (kill test: charged matter? coefficient geometric?)")
# ---------------------------------------------------------------------------------------------
print("  Pinned field content (MINIMAL_BCT §1.1): one complex scalar, neutral under a_e in option B;")
print("  vortex strings (§1.5) are excitations of that neutral field. Charged matter in the corpus: none -> beta_ind = 0.")
print("  If charged matter were added: beta_ind = c * sum q^2 * ln(Lambda/m). Cutoff ratio needed for beta_geom:")
for name, c in (("card form   c = 1/(12 pi^2)", 1 / (12 * pi ** 2)),
                ("Dirac       c = 1/(6 pi^2) ", 1 / (6 * pi ** 2)),
                ("cplx scalar c = 1/(24 pi^2)", 1 / (24 * pi ** 2))):
    L = beta_geom / c
    p(f"{name}: ln(Lambda/m)", L)
    p("      log10(Lambda/m)", L / log(10))
me_mP = mpf("4.1855e-23")                            # App J line 321 (CODATA, quoted there)
LmP = log(1 / me_mP)
p("illustration: ln(m_P/m_e) from App J line 321", LmP)
p("  one unit-charge Dirac species over that range: beta_ind", LmP / (6 * pi ** 2))
p("  species needed for beta_geom (Dirac)", beta_geom * 6 * pi ** 2 / LmP)
p("  species needed for beta_geom (card coefficient)", beta_geom * 12 * pi ** 2 / LmP)
print("  beta_ind is a logarithm of a cutoff ratio times a species count; 10.742 requires tuning either.  R5 CLOSED.")

# ---------------------------------------------------------------------------------------------
head("R6. Other routes found in the pinned sources")
# ---------------------------------------------------------------------------------------------
# R6a -- particle-vortex duality of the superfluid (PROMOTE Step 2 (ii), CN-PROMOTE-06/10)
K = sp.symbols("K", positive=True)
print("  R6a duality. Villain XY: Z = sum_{j: div j = 0} exp(-sum j^2/(2K)); j = curl m (m integer) ->")
print("        S_dual = sum (curl m)^2/(2K); m = a/(2 pi) -> S = (1/(8 pi^2 K)) sum F^2 = (beta/2) sum F^2")
beta_dual = 1 / (4 * sp.pi ** 2 * K)
print("        beta_dual(K) =", beta_dual, "   d beta_dual/dK =", sp.diff(beta_dual, K), "(INVERSE to the stiffness)")
p("        beta_dual at K = beta_geom (if R3's K were used)", 1 / (4 * pi ** 2 * beta_geom))
Dd = 4
print("        in D = 4 the dual of a superfluid is a p = 2 form; polarisations C(D-2, p):",
      {pp: int(binomial(Dd - 2, pp)) for pp in (0, 1, 2)}, "-> 2-form has 1, the photon (1-form) has 2")
print("        It is the phonon re-expressed (PROMOTE CN-PROMOTE-10 FALSIFIED 'superfluid dual = photon'),")
print("        not the added a_e; and K ~ 2 J Psi0^2 (lattice link energy) needs Psi0 / nbar, not in §1.3.  R6a CLOSED.")
# R6b -- topological quantisation (MINIMAL_BCT §1.5)
eg, gm = sp.symbols("e g_m", positive=True)
print("  R6b quantisation. Dirac/flux condition e * g_m = 2 pi n:  solve for e ->", sp.solve(sp.Eq(eg * gm, 2 * sp.pi), eg),
      "(fixes a product, not e)")
print("        Circulation 2 pi of the neutral field is not flux of a_e without a charge q (R1).  R6b CLOSED.")
# R6c -- App E.1 §3.3 J = 1/(4 pi alpha_0), reported by the scoping note §4 (orientation only)
print("  R6c pointer: scoping note §4 reports App E.1 §3.3 writes J = 1/(4 pi alpha_0) = 10.74 (monopole-action")
print("        parameter). App E.1 is NOT pinned; not read. Whatever value J has, R3's kill test fails at the")
print("        J -> a_e transfer (mixed derivatives = 0), so the pointer cannot change the ledger.  CLOSED via R3.")
# R6d -- network geometry (DL step 0)
print("  R6d network geometry. DL step 0 fixes V=3, E=8, b1=5 per primitive cell and S = I/3. These dimensionless")
print("        numbers enter the beta <-> 1/e^2 continuum-matching factor on the graph (DL-BETA's job), not beta:")
print("        compact U(1) on any graph is a one-coupling family in beta.  R6d CLOSED (no term, no coefficient).")

# ---------------------------------------------------------------------------------------------
head("Q3. Comparison against beta_c (no route survives; rows are orientation only)")
# ---------------------------------------------------------------------------------------------
bcs = (("/ Z4 1.0111", mpf("1.0111")), ("/ D4 0.6150 card", mpf("0.6150")),
       ("/ D4 1.2300 K-N", mpf("1.2300")))
rows = (("beta_geom = 2 xi^2/a^2 (hypothetical SC-DLS-1 value)", beta_geom),
        ("1/(4 pi alpha_CODATA) (fit, for scale)", 1 / (4 * pi * alpha_codata)),
        ("R3 steelman E_J/E_C, nbar=1, E_C=U (closed)", 2 * xi ** 2),
        ("R3 steelman E_J/E_C, nbar=1, E_C=U/2 (closed)", 4 * xi ** 2),
        ("R5 one Dirac species over m_P/m_e (closed)", LmP / (6 * pi ** 2)),
        ("R6a dual coupling at K = beta_geom (closed; a 2-form)", 1 / (4 * pi ** 2 * beta_geom)))
print(f"  {'value':<56s} {'beta':>14s} " + " ".join(f"{n[:16]:>16s}" for n, _ in bcs) + "  void network")
for lab, b in rows:
    print(f"  {lab:<56s} {N10(b):>14s} " + " ".join(f"{N10(b / bc):>16s}" for _, bc in bcs) + "  DL-BETA pending")
print("\nAll routes closed by their kill tests (card §6). Surviving beta: none.")
