#!/usr/bin/env python3
"""
Bubble Bells desk-check 2 (23 Nov 2026), part 3 — WHICH CONDENSATE MASS DOES THE CORPUS USE?
Non-gate, CONJECTURE-capped.  Reads tex/ of the BCT-Programme checkout (path as argv[1]) and reports every place the GP
boson mass m, the healing length xi, the coupling g and the sound speed are fixed, then the arithmetic that relates them.
"""
import sys, re, os, glob
import mpmath as mp
mp.mp.dps = 30
texdir = sys.argv[1] if len(sys.argv) > 1 else 'tex'
pats = {
    'm = m_P (Planck mass as the GP boson mass)': r'm\s*=\s*(m_P|\\mP)',
    'g = m c^2 / n_0 (Josephson condition => c_s = c)': r'g\s*=\s*mc\^2/n_0|c_s\^2\s*=\s*gn_0/m\s*=\s*c\^2',
    'xi = hbar / sqrt(2 m g n_0) (GP healing length)': r'\\xi\s*=\s*\\hbar/\\sqrt\{2mgn_0\}',
    'xi = 2.32 l_P (App E.3 value)': r'\\xi\s*=\s*2\.32',
    'xi / r_oct = 1/[r_oct sqrt(8 pi alpha0)] (xi from alpha0)': r'sqrt\{8\\pi\\alpha_0\}\]',
    'E_n = hbar c kappa_n (App J: linear dispersion, no m)': r'E_n\s*=\s*\\hbar c\\kappa_n',
    'c_s = c (identification)': r'c_s\s*=\s*c\b',
}
print("Bubble Bells desk-check 2 — condensate-mass sweep of tex/  (%d files)" % len(glob.glob(os.path.join(texdir, '*.tex'))))
for label, pat in pats.items():
    hits = []
    for f in sorted(glob.glob(os.path.join(texdir, '*.tex'))):
        with open(f, errors='replace') as fh:
            for i, line in enumerate(fh, 1):
                if re.search(pat, line): hits.append(f"{os.path.basename(f)}:{i}")
    print(f"\n[{label}]  {len(hits)} hits")
    for h in hits[:8]: print("   ", h)
    if len(hits) > 8: print(f"    ... and {len(hits)-8} more")

print("\nArithmetic (units: a = l_P, n_0 a^3 = 1):")
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = 1 / mp.sqrt(8 * mp.pi * alpha0)
print(f"  xi = a/sqrt(8 pi alpha0) = {mp.nstr(xi, 6)} l_P   (App E.3 / AZ6 / AZ7: 2.32 l_P)")
print(f"  with g = m c^2/n_0 (AZ6):  xi = hbar/sqrt(2 m g n_0) = hbar/(sqrt2 m c) = (m_P/m) l_P/sqrt2")
print(f"     Letter 20's m = m_P  =>  xi = l_P/sqrt2 = {mp.nstr(1/mp.sqrt(2), 5)} l_P   (factor {mp.nstr(xi*mp.sqrt(2), 4)} below App E.3's 2.32)")
print(f"     App E.3's xi = 2.32 l_P  =>  m = l_P/(sqrt2 xi) m_P = {mp.nstr(1/(mp.sqrt(2)*xi), 5)} m_P   (Gate BUBBLE_BELLS N9, c_s = c)")
print(f"     bubble bells (c_eff = c_s/sqrt(alpha_inf) = c, alpha_inf = 1.64):  m = {mp.nstr(1/(mp.sqrt(2*mp.mpf('1.64'))*xi), 5)} m_P   (N9 with tortuosity)")
k0 = mp.mpf('3.3904626')
print(f"  App J's bell energy under the three conventions (kappa0 = {mp.nstr(k0,6)}/l_P):")
print(f"     E = hbar c kappa0                      = {mp.nstr(k0, 4)} m_P c^2   (App J table)")
print(f"     E = hbar^2 kappa0^2/2m,  m = m_P       = {mp.nstr(k0**2/2, 4)} m_P c^2   (Gate BUBBLE_BELLS bells_resonator.py)")
print(f"     E = hbar^2 kappa0^2/2m,  m = 0.305 m_P = {mp.nstr(k0**2/2/(1/(mp.sqrt(2)*xi)), 4)} m_P c^2   (c_s = c with xi = 2.32 l_P)")
print("  Finding: the corpus carries two incompatible values of the GP boson mass (m = m_P in Letter 20 / Monograph App AI;")
print("  m = 0.305 m_P forced by AZ6's c_s = c together with App E.3's xi = 2.32 l_P) and a third energy convention in App J")
print("  (E = hbar c kappa, no m).  Gate BUBBLE_BELLS' N9 is the second of these, shifted by 1/sqrt(alpha_inf).  Any corpus")
print("  number that uses both m = m_P and xi = 2.32 l_P (or c_s = c) is off by the factor 3.28 somewhere.")
