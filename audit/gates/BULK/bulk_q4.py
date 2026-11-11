#!/usr/bin/env python3
"""
Gate BULK — Q4 measurement table (NO VERDICT) and the dimensional checks behind the Q1 ledgers.

Rules (card §3–§5, fixed before the run):
  * K is the thermodynamic bulk modulus K = rho dP/drho at the ground state (= rho_0 c_s^2).
    GP quartic:  P = g n^2/2  ->  K = g n_0^2.    gamma=2 polytrope (Letter 20): K = rho_0 c^2.
  * c/a = sqrt2 (FCC), touching spheres, a = nearest-neighbour distance = 2R.
    Site volume v = a^3/sqrt2 (BCT cell a*a*sqrt2 a with 2 sites). "n_0 = 1 per site" -> n_0 = sqrt2/a^3.
  * Void-localised (iv), §3 rule: K_eff = rho_eff c_eff^2, rho_eff = phi rho_0, c_eff = c_s/sqrt(alpha_inf).
  * kappa = K a^4/(hbar c);  a_dagger: c^4/(8 pi K a_dagger^2) = G_CODATA;  f_K = K_void/K_bulk.
  * Reference: CODATA 2022, G = 6.67430(15)e-11.  mpmath 60 digits working, 40 reported.
Every number below traces to a ledger line in gate_BULK_RESULT.md (§Q1), cited in the comments.
"""
from mpmath import mp, mpf, pi, sqrt
mp.dps = 60
R = lambda x: mp.nstr(x, 40)

# ---- CODATA 2022 (terminal inputs) ---------------------------------------------------------
c    = mpf('299792458')                 # exact
h    = mpf('6.62607015e-34')            # exact
hbar = h/(2*pi)
G    = mpf('6.67430e-11'); dG = mpf('0.00015e-11')

lP   = sqrt(hbar*G/c**3)
mP   = sqrt(hbar*c/G)
rhoP = c**5/(hbar*G**2)                 # Letter 20 L141 / AI.4 p265 L26 "rho_Planck = c^5/(hbar G^2)"
EP   = mP*c**2
FP   = c**4/G

# ---- corpus dimensionless numbers (permitted inputs, §4.3) ---------------------------------
r_oct  = (sqrt(2)-1)/2                  # Letter 27 L61
r_tet  = (sqrt(6)-2)/4                  # Letter 27 L61
alpha0 = r_oct*r_tet/pi                 # AZ7 L108: alpha_0 = r_oct r_tet/pi = 0.00740806
xi_a   = 1/sqrt(8*pi*alpha0)            # BUBBLE_BELLS bb_q4_numbers.py: xi = a/sqrt(8 pi alpha0) = 2.31754 a (Gate RATIO)
phi    = 1 - pi/(3*sqrt(2))             # FCC void fraction at c/a = sqrt2, touching spheres (BB N1)
alpha_inf = mpf('1.64'); d_alpha = mpf('0.03')   # BB N2
v_site = 1/sqrt(2)                      # site volume in units of a^3 (BCT cell a^2 * sqrt2 a, 2 sites)
n0_site = sqrt(2)                       # n_0 = 1 per site, in units of a^-3   (AZ7 L162-163)
m_BB   = 1/(sqrt(2*alpha_inf)*xi_a)     # BB N9: m/m_P = 1/(sqrt(2 alpha_inf) xi/a) = 0.238
m_noA  = 1/(sqrt(2)*xi_a)               # BB N9 "without tortuosity": 0.305

out = []; md = []
def P(s=''):
    print(s); out.append(s)

P("Gate BULK — Q4 measurement table (no verdict).  mpmath dps=60, 40 digits reported.  CODATA 2022.")
P("="*110)
P("Terminal inputs")
P(f"  c      = {R(c)} m/s (exact)")
P(f"  hbar   = {R(hbar)} J s")
P(f"  G      = {R(G)} m^3 kg^-1 s^-2  (±{R(dG)}, rel 2.2e-5)")
P(f"  l_P    = {R(lP)} m")
P(f"  m_P    = {R(mP)} kg")
P(f"  rho_P  = {R(rhoP)} kg m^-3     (AI.4 prints 5.1560e+96)")
P(f"  rho_P c^2 (Planck pressure) = {R(rhoP*c**2)} Pa")
P(f"  c^4/G (Planck force)        = {R(FP)} N")
P()
P("Corpus dimensionless numbers")
P(f"  alpha_0 = r_oct r_tet/pi        = {R(alpha0)}")
P(f"  xi/a    = 1/sqrt(8 pi alpha_0)  = {R(xi_a)}")
P(f"  phi     = 1 - pi/(3 sqrt2)      = {R(phi)}")
P(f"  alpha_inf                       = {R(alpha_inf)} ± {R(d_alpha)}")
P(f"  m/m_P (BB N9, with alpha_inf)   = {R(m_BB)}")
P(f"  m/m_P (BB N9, without)          = {R(m_noA)}")
P(f"  1/(8 pi)                        = {R(1/(8*pi))}")
P(f"  1/sqrt(8 pi)                    = {R(1/sqrt(8*pi))}")
P(f"  pi^2/16 (App AL rho_D4)         = {R(pi**2/16)}")
P()

# ---- Section A: dimensional checks of the printed identifications (Q1 column 'consistent as written')
P("A. Dimensional checks of the printed identifications (SI)")
P("  [c^4/(8 pi K)] with K a pressure [kg m^-1 s^-2]        = m^5 kg^-1 s^-2   (G is m^3 kg^-1 s^-2)  -> INCONSISTENT")
P("  [c^2/(8 pi rho_0)] with rho_0 a mass density [kg m^-3]  = m^5 kg^-1 s^-2                          -> INCONSISTENT")
P("  [c^4/(16 pi rho_BCT)] with rho_BCT [kg m^-3]            = m^7 kg^-1 s^-4                          -> INCONSISTENT")
P("  [c^4/(8 pi K)] with K a pure number                     = m^4 s^-4                                -> INCONSISTENT")
x = c**4/(8*pi*rhoP*c**2)
P(f"  c^4/(8 pi rho_P c^2)  = {R(x)}  [m^5 kg^-1 s^-2];  / (G l_P^2/(8 pi)) = {R(x/(G*lP**2/(8*pi)))}")
y = c**4/(16*pi*rhoP)
P(f"  c^4/(16 pi rho_P)     = {R(y)}  [m^7 kg^-1 s^-4] = hbar G^2/(16 pi c): {R(y/(hbar*G**2/(16*pi*c)))}")
P(f"  (App AL p274 L25-26 calls this 'dimensions of time'; it is m^7 kg^-1 s^-4, and AL's ħ/(cπ³) dropped G².  See CN-BULK-02.)")
z = c**4/(16*pi*(pi**2/16)*rhoP)
P(f"  c^4/(16 pi (pi^2/16) rho_P) = {R(z)}  [m^7 kg^-1 s^-4]  (= hbar G^2/(pi^3 c), not hbar/(c pi^3))")
P(f"  closing length for variant (a): L^2 = c^4/(8 pi K G) with K = rho_P c^2 -> L/l_P = {R(sqrt(c**4/(8*pi*rhoP*c**2*G))/lP)}")
P()

# ---- Section B: the Q4 table --------------------------------------------------------------
def row(label, kappa, note='', md_label=None):
    """kappa = K a^4/(hbar c) with a = l_P.  a_dagger from c^4/(8 pi K a^2) = G with K = kappa hbar c / l_P^4."""
    K = kappa*hbar*c/lP**4
    a_dag = sqrt(c**4/(8*pi*K*G))
    md.append(f"| {md_label or label.strip()} | {R(K)} | {R(kappa)} | {R(a_dag/lP)} |")
    P(f"  {label}")
    P(f"      K [Pa]          = {R(K)}")
    P(f"      kappa           = {R(kappa)}")
    P(f"      a_dagger/l_P    = {R(a_dag/lP)}")
    if note: P(f"      note: {note}")
    return K, a_dag

P("B. Q4 numbers per variant (a = l_P by the corpus's declared assumption, App K p120 L40-41; m = m_P by Letter 20 L230 unless stated)")
P("   kappa = K a^4/(hbar c);  a_dagger/l_P: the lattice-spacing completion c^4/(8 pi K a^2) = G_CODATA.  No verdict attached.")
P()
# (a) Letter 20: K = rho_0 c^2, rho_0 = rho_P
row("(a-L20)  K = rho_0 c^2, rho_0 = rho_Planck            [AZ6 L91-92; Letter 20 L138-141]", mpf(1),
    "kappa = rho_P c^2 l_P^4/(hbar c) = 1 identically; a_dagger/l_P = 1/sqrt(8 pi)", md_label="(a-L20) K = ρ₀c², ρ₀ = ρ_P (AZ6 L91–92; L20 L138–141)")
# (a) AZ6: rho_0 = m_P n_0 with n_0 = 1 per site (sqrt2/a^3) or 1/a^3
row("(a-AZ6)  K = rho_0 c^2, rho_0 = m_P n_0, n_0 = 1/site  [AZ6 L373-374; AZ7 L162-163]", n0_site,
    "kappa = n_0 l_P^3 = sqrt2;  with n_0 = 1/a^3 instead, identical to (a-L20)", md_label="(a-AZ6) ρ₀ = m_P n₀, n₀ = 1/site (AZ6 L373–374; AZ7 L162–163)")
# (i) GP quartic with Josephson g = m c^2/n_0: K = g n_0^2 = m n_0 c^2
row("(i-mP)   K = g n_0^2, g = m c^2/n_0, m = m_P, n_0 = 1/site [AZ6 L139, L353-354]", n0_site,
    "identical in content to (a-AZ6): K = m n_0 c^2", md_label="(i-mP) K = g n₀², g = mc²/n₀, m = m_P (AZ6 L139, L353–354)")
row("(i-BB)   same with m = 0.238 m_P (BB N9)                [§4.4 second value]", n0_site*m_BB,
    f"kappa = sqrt2 * {R(m_BB)}", md_label="(i-BB) same, m = 0.238 m_P (BB N9)")
# (ii) Bose-Hubbard: K = U n_0 = hbar^2/(2 m xi^2 v_site), xi = 2.31754 a
k_ii = n0_site/(2*xi_a**2)            # (hbar/(m_P c l_P)) = 1
row("(ii-mP)  K = U/v_site, U = hbar^2/(2 m xi^2), xi = 2.31754 a, m = m_P [AZ7 L154-170; Letter 27 L75-76]", k_ii,
    f"kappa = sqrt2/(2 (xi/a)^2) = 4 sqrt2 pi alpha_0 = {R(4*sqrt(2)*pi*alpha0)}  (because (xi/a)^2 = 1/(8 pi alpha_0))", md_label="(ii-mP) K = U/v_site, U = ħ²/(2mξ²), ξ = 2.31754 a, m = m_P (AZ7 L154–170; L27 L75–80)")
row("(ii-BB)  same with m = 0.238 m_P", k_ii/m_BB, "", md_label="(ii-BB) same, m = 0.238 m_P")
row("(ii-t)   K = U/v_site with U = t = alpha_0 E_P (App K p121 L2, L11: t = alpha_0 'in Planck units')", n0_site*alpha0,
    f"kappa = sqrt2 alpha_0; AZ7's t/U = 1 would need (xi/a)^2 = 1/(2 alpha_0) -> xi/a = {R(1/sqrt(2*alpha0))}, vs 2.31754 (sentence only)", md_label="(ii-t) U = t = α₀E_P (App K p. 121 L2, L11)")
# (iii) Madelung: pure number as printed; M_FCC undefined in pinned sources
coef_iii = 8*alpha0/(9*sqrt(2))
P(f"  (iii)    K = 8 M_FCC alpha_0/(9 sqrt2)                  [E.3 p72 L29]  -- ABSENT (App D not in pinned sources)")
P(f"      coefficient 8 alpha_0/(9 sqrt2) = {R(coef_iii)}   (times M_FCC, undefined in the pinned sources)")
P(f"      kappa 'as printed' = the printed number itself (dimensionless); no SI K; no a_dagger.")
P()
# (c) AI.4 / AL: rho_BCT; K read as rho_BCT c^2 to put it on the same footing; 8 pi rule of §5 (16 pi recorded)
row("(c-AI4)  K := rho_BCT c^2, rho_BCT = rho_Planck            [AI.4 p265 L24-27]", mpf(1),
    f"printed coefficient is 16 pi (recorded, not used): with 16 pi, a_dagger/l_P = 1/sqrt(16 pi) = {R(1/sqrt(16*pi))}", md_label="(c-AI4) K := ρ_BCT c², ρ_BCT = ρ_P (p. 265 L24–27); printed 16π recorded in q4_table.txt")
row("(c-AL3)  K := rho_BCT c^2, rho_BCT = (pi^2/16) rho_Planck   [AL.3 p274 L24]", pi**2/16,
    f"a_dagger/l_P = 1/sqrt(pi^3/2) = {R(1/sqrt(pi**3/2))};  with 16 pi: {R(1/sqrt(pi**3))}", md_label="(c-AL3) ρ_BCT = (π²/16)ρ_P (p. 274 L24); 16π value in q4_table.txt")
# (iv) void-localised, §3 rule: K_eff = phi rho_0 c_s^2/alpha_inf; with g = alpha_inf m c^2/n_0 (c_eff = c): K_eff = phi m n_0 c^2
P("  (iv) void-localised, §3 rule: K_eff = rho_eff c_eff^2 = phi rho_0 c_s^2/alpha_inf; with AZ6 L362's g = alpha_inf m c^2/n_0, c_eff = c and K_eff = phi rho_0 c^2")
row("(iv-L20) rho_0 = rho_Planck                              [Letter 20 L141 + BB N1-N3]", phi,
    f"kappa = phi; a_dagger/l_P = 1/sqrt(8 pi phi)", md_label="(iv-L20) K_eff = φρ₀c², ρ₀ = ρ_P (AZ6 L362; BB N1–N3)")
row("(iv-AZ6) rho_0 = m_P n_0, n_0 = 1/site", phi*n0_site, "kappa = sqrt2 phi", md_label="(iv-AZ6) ρ₀ = m_P n₀, n₀ = 1/site")
row("(iv-BB)  rho_0 = m n_0, m = 0.238 m_P, n_0 = 1/site", phi*n0_site*m_BB, "", md_label="(iv-BB) m = 0.238 m_P, n₀ = 1/site")
P()
P("  f_K = K_void/K_bulk for variant (iv):")
fK = phi/alpha_inf; dfK = fK*d_alpha/alpha_inf
P(f"      §3 rule, same microscopic g in both (K_bulk = rho_0 c_s^2):     f_K = phi/alpha_inf = {R(fK)} ± {R(dfK)}")
P(f"      both moduli with their sound speed set to c (K_bulk = rho_0 c^2, K_void = phi rho_0 c^2): f_K = phi = {R(phi)}")
P(f"      other homogenisations (listed, no verdict): per unit fluid volume K = rho_0 c_s^2/alpha_inf -> 1/alpha_inf = {R(1/alpha_inf)};")
P(f"        Biot/JKD equivalent fluid K_eff = K_f/phi with rho_eff = alpha_inf rho_0/phi -> 1/phi = {R(1/phi)}")
P()
P("  Reference column: 1/(8 pi) = %s ; 1/sqrt(8 pi) = %s ; phi = %s ; alpha_inf = %s ; 1/alpha_inf = %s ; 1/sqrt(8 pi phi) = %s"
  % (R(1/(8*pi)), R(1/sqrt(8*pi)), R(phi), R(alpha_inf), R(1/alpha_inf), R(1/sqrt(8*pi*phi))))
P()
# ---- Section C: GP internal consistency checks that bear on which K exists ------------------
P("C. Internal checks recorded in the ledgers (sentences only; nothing is changed)")
xi_J = 1/sqrt(2)                       # xi = hbar/sqrt(2 m g n_0) with g n_0 = m c^2, m = m_P: xi = l_P/sqrt2
P(f"  AZ6 L168 xi = hbar/sqrt(2 m g n_0) with L353 g = m c^2/n_0 and m = m_P gives xi/l_P = 1/sqrt2 = {R(xi_J)}, vs AZ6 L169 xi = 2.32 l_P (ratio {R(xi_a/xi_J)}).")
P(f"  Resolving by m instead gives m/m_P = 1/(sqrt2 xi/a) = {R(m_noA)} (BB N9 'without tortuosity').")
P(f"  E.3 p72 L22 'rho_0 = 2 K_BCT/c^2' (K = rho_0 c^2/2) vs AZ6 L92 K = rho_0 c^2: factor 2 between the two printed EOS relations.")
P(f"  Coefficients printed in front of K or rho: 8 pi (AZ6 L91, L261; Letter 20 L96; E.3 p72 L26), 4 pi (E.3 p72 L20), 16 pi (AI.4 p265 L7, L24; AL p273 L20).")
P()
P("Q3 not evaluated: no variant has a G-free SI value (see gate_BULK_RESULT.md §Q2).")

import pathlib, hashlib
pathlib.Path(__file__).resolve().parent.joinpath('output').mkdir(exist_ok=True)
pathlib.Path(__file__).resolve().parent.joinpath('output', 'q4_table.txt').write_text('\n'.join(out)+'\n', encoding='utf-8')
hdr = ["| Variant (ledger lines) | K [Pa] | κ = K a⁴/(ħc) | a†/ℓ_P |", "|---|---|---|---|"]
md_f = ["", "**f_K ≡ K_void/K_bulk, variant (iv):**", "", "| reading | f_K |", "|---|---|",
        f"| §3 rule as written — K_eff = ρ_eff c_eff² with the same microscopic g in void and bulk (K_bulk = ρ₀c_s²) | **φ/α_∞ = {R(fK)} ± {R(dfK)}** |",
        f"| both moduli with their own sound speed set to c (K_bulk = ρ₀c², K_void = φρ₀c²; the §9 reading) | φ = {R(phi)} |",
        f"| per unit fluid volume, K = ρ₀c_s²/α_∞ (listed, no verdict) | 1/α_∞ = {R(1/alpha_inf)} |",
        f"| Biot/JKD equivalent fluid, K_eff = K_f/φ with ρ_eff = α_∞ρ₀/φ (listed, no verdict) | 1/φ = {R(1/phi)} |",
        "",
        f"**Reference column (no verdict):** 1/(8π) = {R(1/(8*pi))}; 1/√(8π) = {R(1/sqrt(8*pi))}; φ = {R(phi)}; α_∞ = 1.64 ± 0.03; 1/α_∞ = {R(1/alpha_inf)}; 1/√(8πφ) = {R(1/sqrt(8*pi*phi))}; π²/16 = {R(pi**2/16)}; 4√2πα₀ = {R(4*sqrt(2)*pi*alpha0)}."]
pathlib.Path(__file__).resolve().parent.joinpath('output', 'q4_table.md').write_text('\n'.join(hdr+md+md_f)+'\n', encoding='utf-8')
