"""Gate SONO - Q2 reproduction. BCT Letter 110 (DOI 10.5281/zenodo.19177501), predictions #154 and #155.
Recomputes every printed value and printed error from the letter's own formula and inputs.
mpmath, 30 digits working, 10 reported (card 4.5). No comparison value is constructed here (card 4.6);
the "observed" ratios are the letter's printed numbers (card 6: 'obs' from the letter for Q2).
Also Q3(d): literal evaluation of Letter 207's "r = r_tet x lambda_acoustic" (orientation only; water 1482 m/s, card 4.4)."""
from mpmath import mp, mpf, sqrt, besseljzero, log
mp.dps = 30
R = lambda x, n=10: mp.nstr(x, n)

r_oct = (sqrt(2) - 1) / 2            # FCC octahedral-void inradius / sphere diameter (corpus definition, Gate RATIO)
r_tet = (sqrt(6) - 2) / 4            # FCC tetrahedral-void inradius / sphere diameter
j11 = besseljzero(1, 1); j12 = besseljzero(1, 2); j21 = besseljzero(2, 1)

print("=== constants (30 dps, 10 printed) ===")
print("r_oct           =", R(r_oct))
print("r_tet           =", R(r_tet))
print("r_tet/r_oct     =", R(r_tet / r_oct), "  (letter: 0.5426)")
print("r_oct/r_tet     =", R(r_oct / r_tet), "  (Gate RATIO: 1.8430)")
print("j_{1,1}         =", R(j11), "  (letter 'j(1,1) = 3.832', first zero of J_1)")
print("j_{1,2}         =", R(j12), "  (letter 'j(2,1) = 7.016' -- this is the SECOND zero of J_1)")
print("j_{2,1}         =", R(j21), "  (the actual first zero of J_2; not used by the letter)")
print("j_{1,2}/j_{1,1} =", R(j12 / j11), "  (letter: 1.830)")
print("(j12/j11)^2     =", R((j12 / j11) ** 2), "  (letter: 3.348; 1.830^2 =", R(mpf('1.830') ** 2, 6), ")")
print("j_{2,1}/j_{1,1} =", R(j21 / j11), "  (label-literal reading of the letter's 'j(2,1)/j(1,1)')")
print("(j21/j11)^2     =", R((j21 / j11) ** 2))
print("abstract L15-16 prints 'j(2,1)/j(1,1) = 3.054': matches none of the four values above.")
# record-only scan: is 3.054 any ratio of low-order Bessel zeros? (reproduction aid, not a new comparison value)
best = []
for m in range(0, 5):
    for n in range(1, 5):
        for m2 in range(0, 5):
            for n2 in range(1, 5):
                if (m, n) == (m2, n2):
                    continue
                v = besseljzero(m, n) / besseljzero(m2, n2)
                best.append((abs(v / mpf('3.054') - 1), m, n, m2, n2, v))
best.sort(key=lambda t: t[0])
print("nearest low-order Bessel-zero ratios to 3.054 (record only):")
for d, m, n, m2, n2, v in best[:3]:
    print("   j_{%d,%d}/j_{%d,%d} = %s  (off by %s %%)" % (m, n, m2, n2, R(v, 6), R(100 * d, 3)))
print("   (j12/j11)^2 = 3.3523 is off by %s %%; j21/j11 = %s is off by %s %%" %
      (R(100 * abs((j12 / j11) ** 2 / mpf('3.054') - 1), 3), R(j21 / j11, 5), R(100 * abs(j21 / j11 / mpf('3.054') - 1), 3)))

print()
print("=== #154  lambda_UV/lambda_peak = r_tet/r_oct ===")
bct154 = r_tet / r_oct
for num, den, note in [(200, 370, "the letter's arithmetic (L53)"), (200, 350, "the letter's text (L52, 'broad peak near 350 nm')")]:
    obs = mpf(num) / den
    print("  obs = %d/%d = %s  [%s]" % (num, den, R(obs, 10), note))
    print("     delta_154 = BCT/obs - 1 = %s %%   ;   obs/BCT - 1 = %s %%" % (R(100 * (bct154 / obs - 1), 4), R(100 * (obs / bct154 - 1), 4)))
print("  letter prints: Observed 0.541 (=200/370 rounded), BCT 0.5426, 'Error: -0.3%' (text) and '0.3%' (table).")
print("  -0.3% is obs/BCT - 1 = -0.376% rounded to one figure; the card's delta_154 (BCT/obs - 1) is +0.378%.")

print()
print("=== #155  lambda_1/lambda_2 = j(2,1)/j(1,1) [= j_{1,2}/j_{1,1}] ===")
bct155 = j12 / j11
obs = mpf(700) / 380
print("  letter's '7.016/3.832' =", R(mpf('7.016') / mpf('3.832'), 10), " (prints 1.830); full precision", R(bct155))
print("  obs = 700/380 =", R(obs, 10), " (letter prints 1.842)")
print("     delta_155 = BCT/obs - 1 = %s %%   ;   obs/BCT - 1 = %s %%" % (R(100 * (bct155 / obs - 1), 4), R(100 * (obs / bct155 - 1), 4)))
print("  letter prints 'Error: +0.65%' (text) and '0.65%' (table): that is obs/BCT - 1 = +0.610% rounded up, or")
print("  (1.842/1.830 - 1) from the rounded printed values =", R(100 * (mpf('1.842') / mpf('1.830') - 1), 4), "%  <- reproduces 0.65% to two figures")
print("  sign convention consistent with #154: the letter's 'Error' = obs/BCT - 1 computed from the ROUNDED printed values.")
print("  check #154 the same way: 0.541/0.5426 - 1 =", R(100 * (mpf('0.541') / mpf('0.5426') - 1), 4), "% -> prints -0.3%  (consistent)")
print("  other corpus '1.84': r_oct/r_tet =", R(r_oct / r_tet, 6), "; vs 700/380:", R(100 * ((r_oct / r_tet) / obs - 1), 4), "%  (look-elsewhere illustration only)")
print("  j_{1,2}/j_{1,1} vs r_oct/r_tet differ by", R(100 * ((j12 / j11) / (r_oct / r_tet) - 1), 4), "%")

print()
print("=== tolerances handed to Q4 (card Q4: 'printed tolerance') ===")
eps154 = abs(bct154 / (mpf(200) / 370) - 1)
eps155 = abs(bct155 / obs - 1)
print("  eps_154 = |delta_154| =", R(eps154, 6), " (card: 0.38 %)")
print("  eps_155 = |delta_155| =", R(eps155, 6), " (card: 0.61 %)")

print()
print("=== Q3(d): Letter 207's 'r = r_tet x lambda_acoustic' (absent from Letter 110; literal reading, record only) ===")
c_w = mpf(1482)
for f_kHz in (20, 26.5, 40):
    lam = c_w / (f_kHz * 1000)
    print("  f = %5.1f kHz: lambda_acoustic = %s mm ; r_tet x lambda = %s mm = %s um" %
          (f_kHz, R(lam * 1000, 4), R(r_tet * lam * 1000, 4), R(r_tet * lam * 1e6, 4)))
print("  measured SBSL radii (pinned refs): R0 ~ 4-5 um, Rmax ~ 40-50 um, Rmin ~ 0.5 um.")
print("  6.28 mm (26.5 kHz) / 50 um = %s x Rmax ; / 0.5 um = %s x Rmin" % (R(r_tet * c_w / 26500 / mpf('50e-6'), 4), R(r_tet * c_w / 26500 / mpf('0.5e-6'), 4)))
