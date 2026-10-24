#!/usr/bin/env python3
"""Gate PLASMOID, card section 1 (Step 0): the arithmetic behind Prediction #162.

Verifies j_{0,1}, j_{1,1}, their ratio and log, the ladder D_n/D_0 for n = 1..4,
Letter 114's printed figures, and the ball-lightning sequence for D_0 = 2 cm.
Pure mpmath; 30-digit precision.
"""
from mpmath import mp, besseljzero, log, mpf, nstr, phi, sqrt, e

mp.dps = 30
j01 = besseljzero(0, 1)
j11 = besseljzero(1, 1)
r = j11 / j01
P0 = log(r)

print("j_{0,1}            =", nstr(j01, 16))
print("j_{1,1}            =", nstr(j11, 16))
print("ratio j11/j01      =", nstr(r, 16), "   (card expects 1.59334)")
print("ln(ratio) = P0     =", nstr(P0, 16), "   (card expects 0.46583)")
print()

letter_ratio = mpf("1.5934")
letter = {1: mpf(1), 2: mpf("1.5934"), 3: mpf("2.5389"), 4: mpf("4.0441")}
print("Ladder D_n/D_0, n = 1..4")
print(" n | exact ratio^(n-1)   | Letter's 1.5934^(n-1) | Letter 114 prints | agrees with exact to 4 dp?")
for n in range(1, 5):
    ex = r ** (n - 1)
    lr = letter_ratio ** (n - 1)
    pr = letter[n]
    ok = abs(ex - pr) < mpf("0.00005")
    print(f" {n} | {nstr(ex, 10):<19} | {nstr(lr, 10):<21} | {nstr(pr, 6):<17} | {ok}")
print()
print("Rounding of the ratio itself: exact", nstr(r, 8), "-> 4 dp =", nstr(r, 5),
      "; Letter prints 1.5934 (last digit rounds the wrong way).")
print("D_4 exact =", nstr(r**3, 8), "; Letter prints 4.0441;",
      "difference =", nstr(r**3 - mpf('4.0441'), 4),
      f"({nstr(100*(r**3 - mpf('4.0441'))/r**3, 3)} %)")
print("D_3 exact =", nstr(r**2, 8), "; Letter prints 2.5389 (= 1.5934^2 to 4 dp:",
      nstr(letter_ratio**2, 8), ")")
print()
print("Ball-lightning sequence for D_0 = 2 cm")
for n in range(1, 5):
    d = 2 * r ** (n - 1)
    print(f"  D_{n} = {nstr(d, 8)} cm  -> {nstr(d, 2)} cm")
print("  Letter 114 prints: 2, 3.2, 5.1, 8.1 cm")
print()
print("Competitor ratios and their log offset from P0 (card section 2.4)")
comps = [("phi", phi), ("R5 = 10^(1/5)", mpf(10) ** (mpf(1) / 5)),
         ("sqrt(e)", sqrt(e)), ("1.5", mpf("1.5")), ("2", mpf(2))]
for name, c in comps:
    print(f"  {name:<14} = {nstr(c, 8):<11} ln = {nstr(log(c), 6):<9} "
          f"(ln c - P0)/P0 = {nstr(100*(log(c) - P0)/P0, 3)} %")
