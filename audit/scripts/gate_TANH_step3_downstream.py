from mpmath import mp, mpf, sqrt, pi, tanh, log, log10
mp.dps = 40
r_tet=(sqrt(6)-2)/4; r_oct=(sqrt(2)-1)/2; R=mpf(1)/2
a0=r_tet*r_oct/(4*pi*R**2); xi=1/sqrt(8*pi*a0)
g = a0*4*pi*R*tanh(r_oct/xi)**2          # corrected dimensionless Josephson coupling
print(f"alpha_0 (sigma_s/J, bare surface potential) = {mp.nstr(a0,10)}")
print(f"g       (dimensionless Josephson coupling)  = {mp.nstr(g,10)}")
print(f"ratio                                        = {mp.nstr(a0/g,10)}\n")

mP_GeV = mpf('1.220890e19')
print("=== 1. App J S3.2 : second-order shift  dE = -g^2/(kappa0 - xi_geom) ===")
den = mpf('3.39')-mpf('0.05')
print(f"   with alpha_0 : {mp.nstr(-a0**2/den,6)} m_P   (App J prints -1.6429e-5)")
print(f"   with g       : {mp.nstr(-g**2/den,6)} m_P")
print(f"   target m_e   : 4.2e-23 m_P  -> still too large by {mp.nstr((g**2/den)/mpf('4.2e-23'),4)}x")
print("   CONCLUSION 'does not explain m_e' : UNCHANGED (strengthened)\n")

print("=== 2. App K Theorem 3 : gap equation, c = 20 (App K's own DOS slope) ===")
c = mpf(20)
for lbl,t in [("t = alpha_0", a0), ("t = g", g)]:
    print(f"   {lbl:12s} t^2 = {mp.nstr(t**2,6):12s} c*t^2 = {mp.nstr(c*t**2,6):12s} "
          f"required 0.020 -> short by {mp.nstr(mpf('0.020')/(c*t**2),6)}x")
print("   App K printed 'a factor of 20 too weak'. Recomputed with g: ~7300x too weak.")
print("   CONCLUSION 'coupling insufficiency' : UNCHANGED (strengthened)\n")

print("=== 3. App K S6 : loop series a_n = t^n C_A(n)/n, n=16 ===")
a16_printed = mpf('1.0962e-26')
C_A16 = a16_printed*16/a0**16          # back out App K's own C_A(16)
print(f"   App K's implied C_A(16) = {mp.nstr(C_A16,6)}")
print(f"   recompute a_16 with t=g : {mp.nstr(g**16*C_A16/16,6)}   (was {mp.nstr(a16_printed,6)})")
print(f"   m_e/m_P                 : 4.1855e-23")
print("   the 'a_16 ~ m_e/4' near-coincidence DISAPPEARS entirely under g.")
print("   App K already called it 'a numerical accident with no physical content'.")
print("   CONCLUSION : UNCHANGED (the accident simply evaporates)\n")

print("=== 4. App AG.2 : naive Higgs mass m_H = 2 * coupling * m_P ===")
for lbl,t in [("alpha_0", a0), ("g", g)]:
    print(f"   with {lbl:8s}: {mp.nstr(2*t*mP_GeV,6)} GeV")
print("   App AG prints 180888423144 GeV and DISCARDS it as 'far too large'.")
print(f"   recomputed 9.03e9 GeV is still ~7e7 x the observed 125 GeV.")
print("   CONCLUSION 'naive estimate fails' : UNCHANGED\n")

print("=== 5. App AT.3 : lambda_gap = (coupling*v)^2/(8 v^4), dimensional estimate ===")
print(f"   lambda_gap scales as coupling^2 -> changes by 1/{mp.nstr((a0/g)**2,6)} = {mp.nstr((g/a0)**2,6)}")
print("   App AT.3 itself says this 'does not give the correct lambda'. Not a prediction.")
print("   CONCLUSION : UNCHANGED\n")

print("=== 6. App AN.2 / AG.4 / AT.2 : lambda(m_P) ~ 0 from VANISHING coupling ===")
print("   claim is that the coupling -> 0 in the symmetric phase. 0 = 0 either way.")
print("   CONCLUSION : NUMERICALLY UNAFFECTED\n")

print("=== 7. UNAFFECTED: alpha_0 in its two CORRECT roles ===")
print("   (a) sigma_s/J = alpha_0  -> App J S2 kappa_0 = 3.390462  [verified exact]")
print("   (b) alpha_0 = r_oct r_tet/pi as the geometric EM coupling")
print("       App D, Letter 106 (dz = alpha_0 kappa_0 = 0.02511, via Letter 57 two-step void),")
print("       App AY.3 (x_lep = 4 alpha_0/pi, via App AB instanton measure),")
print("       App V.3.1, phi_root = alpha_0/6pi, gauge couplings alpha_2 = r_oct^2/pi etc.")
print(f"   dz_BCT recheck: alpha_0*kappa_0 = {mp.nstr(a0*mpf('3.39'),6)}  (Letter 106 prints 0.02511)")
