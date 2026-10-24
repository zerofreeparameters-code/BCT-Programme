#!/usr/bin/env python3
"""Gate PLASMOID — section 2.6 apparatus lengths and two structural facts.

(1) Where else does j11/j01 come from?  It is the ratio of the two lowest
    Dirichlet-mode frequencies of a disc: the TM110/TM010 ratio of a circular
    cylindrical cavity (p = 0), the (1,1)/(0,1) ratio of a circular membrane, and
    the same for a pressure-release cylinder.  A size set by a wavelength scales
    as 1/f, so a mode switch in a circular apparatus gives a size ratio of j11/j01.
(2) Decimal heaping has period ln 10 in x = ln D, so its Fourier harmonics sit at
    periods ln10/k.  k = 5 is the R5 preferred-number step, 1.14 % from P0.
    By the card's own resolution rule (span of k periods resolves ~1/k) we
    compute the span needed to separate P0 from each competitor.
(3) Minnaert resonance radius for air bubbles in water (adiabatic, 1 atm, no
    surface tension) at the frequencies used in the cavitation literature.
"""
import math
from scipy.special import jn_zeros, jnp_zeros

P0 = math.log(jn_zeros(1, 1)[0] / jn_zeros(0, 1)[0])

print("(1) Disc / cylinder Dirichlet modes (TM_mn0 of a circular cavity; circular membrane)")
modes = {(m, n): jn_zeros(m, n)[-1] for m in range(0, 4) for n in range(1, 3)}
base = modes[(0, 1)]
for (m, n), z in sorted(modes.items(), key=lambda kv: kv[1]):
    print(f"   (m,n) = ({m},{n})  j_mn = {z:.6f}   f/f_01 = {z/base:.6f}")
print(f"   -> TM110/TM010 = j11/j01 = {modes[(1,1)]/base:.10f}  (identical to #162's step ratio)")
print("   Rigid-wall acoustic modes use zeros of J_m' instead:")
jp = {(m, n): jnp_zeros(m, n)[-1] for m in range(1, 4) for n in range(1, 2)}
for (m, n), z in jp.items():
    print(f"   j'_{m}{n} = {z:.6f}")
print(f"   e.g. j'_21/j'_11 = {jp[(2,1)]/jp[(1,1)]:.6f}, j'_31/j'_21 = {jp[(3,1)]/jp[(2,1)]:.6f} (not 1.5933)")
print()

print("(2) Harmonics of decimal heaping, period ln10/k, vs P0")
for k in range(1, 9):
    P = math.log(10) / k
    print(f"   k = {k}: ratio {math.exp(P):.6f}  period {P:.6f}  offset from P0 {100*(P-P0)/P0:+.2f} %")
print("   Span (in periods of P0, and in decades of size) needed to resolve P0 from a competitor,")
print("   using the card's rule 'k periods resolves ~1/k':")
for name, r in (("R5 = 10^(1/5)", 10 ** 0.2), ("phi", (1 + 5 ** 0.5) / 2), ("sqrt(e)", math.e ** 0.5),
                ("1.5", 1.5), ("2", 2.0)):
    off = abs(math.log(r) - P0) / P0
    k = 1 / off
    print(f"   {name:<14} offset {100*off:6.2f} %  -> need >~ {k:6.1f} periods = {k*P0/math.log(10):6.2f} decades")
print()

print("(3) Minnaert resonance radius, air bubble in water: R_res = (1/2 pi f) sqrt(3 gamma p0 / rho)")
gamma, p0, rho = 1.4, 101325.0, 998.0
c = math.sqrt(3 * gamma * p0 / rho) / (2 * math.pi)
print(f"   f * R_res = {c:.4f} m/s")
for f_khz in (20, 213, 355, 515, 647, 1056):
    print(f"   f = {f_khz:>5} kHz -> R_res = {1e6 * c / (f_khz * 1e3):7.2f} um")
print("   (Sonoluminescing bubbles are typically below resonance size; the Minnaert value sets the scale only.)")
