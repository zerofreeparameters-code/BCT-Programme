# Gate SONO card-thread validation (NOT the run): arithmetic of BCT Letter 110's two ratio predictions.
# Letter 110 (DOI 10.5281/zenodo.19177501, 23 March 2026): #154 lambda_UV/lambda_peak = r_tet/r_oct = 0.5426 vs "200/370 = 0.541";
# #155 lambda_1/lambda_2 = j(2,1)/j(1,1) = 7.016/3.832 = 1.830 vs "700/380 = 1.842".
from mpmath import mp, mpf, pi, sqrt, besseljzero
mp.dps = 30
R = lambda x, n=10: mp.nstr(x, n)
r_oct = (sqrt(2)-1)/2; r_tet = (sqrt(6)-2)/4
print("r_oct = %s  r_tet = %s  r_tet/r_oct = %s  r_oct/r_tet = %s" % (R(r_oct), R(r_tet), R(r_tet/r_oct), R(r_oct/r_tet)))
j11 = besseljzero(1, 1); j12 = besseljzero(1, 2); j21 = besseljzero(2, 1); j01 = besseljzero(0, 1)
print("Bessel zeros: j_{1,1} = %s  j_{1,2} = %s  j_{2,1} = %s  j_{0,1} = %s" % (R(j11), R(j12), R(j21), R(j01)))
print("Letter's 'j(2,1) = 7.016' is j_{1,2} (second zero of J_1), not j_{2,1} = %s (first zero of J_2)." % R(j21, 6))
print("ratio used, j_{1,2}/j_{1,1} = %s (letter: 1.830); squared = %s (letter: 3.348 from the rounded 1.830)" % (R(j12/j11), R((j12/j11)**2)))
print("true j_{2,1}/j_{1,1} = %s; abstract's '3.054' matches neither (j_{1,2}/j_{1,1} = %s, squared %s)." % (R(j21/j11, 6), R(j12/j11, 6), R((j12/j11)**2, 6)))
print()
print("#154 comparison arithmetic as printed:")
for num, den in [(200, 370), (200, 350)]:
    obs = mpf(num)/den
    print("  %d/%d = %s ; BCT 0.5426 vs obs: (BCT/obs - 1) = %s %% ; (obs/BCT - 1) = %s %%" % (num, den, R(obs, 6), R(100*(r_tet/r_oct/obs-1), 3), R(100*(obs/(r_tet/r_oct)-1), 3)))
print("  The text says 'broad peak near 350 nm' and then computes 200/370; the printed -0.3% uses 370. With 350 the error is ~5%.")
print()
print("#155 comparison arithmetic as printed:")
obs = mpf(700)/380
print("  700/380 = %s ; BCT %s ; (BCT/obs - 1) = %s %% (letter: +0.65%%)" % (R(obs, 6), R(j12/j11, 6), R(100*((j12/j11)/obs-1), 3)))
print("  r_oct/r_tet = %s differs from j_{1,2}/j_{1,1} = %s by %s %% -- the corpus has two '1.83's; the letter uses one for each prediction."
      % (R(r_oct/r_tet, 6), R(j12/j11, 6), R(100*((r_oct/r_tet)/(j12/j11)-1), 3)))
print()
print("Letter 207's paraphrase 'flash at r = r_tet x lambda_acoustic' does not occur in Letter 110 (no flash-radius formula there).")
print("  Orientation only: water, 26.5 kHz: lambda = 1482/26500 m = %s mm; r_tet x lambda = %s mm; SBSL radii ~0.5-50 um." % (R(mpf(1482)/26500*1000, 4), R(r_tet*mpf(1482)/26500*1000, 4)))
