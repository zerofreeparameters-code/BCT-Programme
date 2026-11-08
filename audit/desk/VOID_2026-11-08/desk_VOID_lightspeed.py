#!/usr/bin/env python3
"""
Desk-check VOID-LIGHTSPEED (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
Question: VOID-Q2 found that, if a Coulomb phase were granted in the void-network liquid, charges
would outrun the emergent photon by R0 = v_charge/c_photon = 2.8e4 (edge of the liquid) to 1.5e12.
Can interactions pull the two speeds together, as in Chadha & Nielsen (1983) and
Anber & Donoghue (2011), before low energies?

Part A  Is there a window in which both are light? Running needs the charges to be dynamical
        (energies above the charge gap) while the photon exists (energies below its band top).
Part B  Grant a window anyway (a light charge, as in the real world). Integrate the one-loop flow of
        the two speeds and of alpha, starting from R0, over the largest window physics offers
        (Planck energy down to the electron mass, 51.5 e-folds).
        Photon side: exact one-loop result for a charge loop with its own speed v (derived here and
        checked against Anber & Donoghue eq. 33): the induced Maxwell term is Lorentz-invariant in
        the CHARGE's metric, so per e-fold of integrated-out modes (N Dirac charges)
            d a_E/dl = N/(6 pi^2 v),   d a_B/dl = N v/(6 pi^2),
        where L_photon = 1/2 (a_E E^2 - a_B B^2), c^2 = a_B/a_E, alpha = 1/(4 pi sqrt(a_E a_B)).
        Charge side: Anber & Donoghue eq. 33 (one loop, photon-metric alpha), IR direction
            dv/dl = -(2 alpha/3pi) (v - c)(4v^2 + 3vc + c^2)/(v + c)^2.
Part C  Final approach and the bounds: near equal speeds delta = v/c - 1 obeys
        d delta/dl = -(2 alpha/pi) delta with d alpha/dl = -(2N/3pi) alpha^2, so delta ~ alpha^3:
        the reduction is (alpha_IR/alpha_UV)^3, whatever the number of e-folds.
Units hbar = 1, speeds in units of the bare photon speed. Runs in about a second.
"""
import numpy as np
from scipy.integrate import solve_ivp

def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# ---------------------------------------------------------------- Part A
hdr("Part A: is there an energy window where charges and the emergent photon are both light?")
print("  Granting the Coulomb phase of VOID-Q2: photon band top ~ pi * J_ring, J_ring ~ t^L / U^(L-1);")
print("  charges (rule violations) cost the Mott gap Delta ~ U (it closes only at the Mott edge).")
print("  Running of speeds needs energies E with Delta < E < pi J_ring. Ratio Delta/(pi J_ring) = (U/t)^L / pi.\n")
print(f"  {'U/t':>6} {'L':>2} {'Delta/(pi J)':>14} {'window (e-folds)':>17} {'gap must be tuned to':>22}")
for Ut in (70, 310, 1241, 6421):
    for Lp in (3, 4):
        ratio = Ut ** Lp / np.pi
        # to open a window of l e-folds, Delta <= pi J e^-l. At the commensurate Mott edge the gap
        # closes as Delta/U ~ sqrt(distance to the edge) (D = 3+1, mean field, nu z = 1/2).
        tune = (1 / ratio) ** 2
        print(f"  {Ut:6d} {Lp:2d} {ratio:14.3e} {'none (' + format(-np.log(ratio), '.1f') + ')':>17}"
              f"   {tune:10.1e} x e^(-2 l)")
print("\n  Reading: the photon's whole band lies below the charge gap by (U/t)^L. Charges never run")
print("  as light particles while the photon exists, so nothing pulls the speeds together. The")
print("  photon's stiffness J_ring is itself the virtual-charge effect; it is already counted.")
print("  A window opens only within (pi J/U)^2 e^(-2l) of the Mott edge, where the charges are about to")
print("  condense; condensed charges Higgs the photon (it gets a mass: the TWIST outcome again).")

# ---------------------------------------------------------------- Part B
hdr("Part B: grant a window (light charges) and run the one-loop flow, l = 0 .. 51.5")
lmax = np.log(1.22e19 / 0.511e-3)          # Planck energy / electron mass, GeV units
print(f"  largest window: ln(E_Planck / m_e) = {lmax:.1f} e-folds; one Dirac charge (N = 1)")

def flow(R0, a0, N=1, charge_side=True, l_end=lmax):
    # state: a_E, a_B, v ; bare photon speed 1, alpha0 = a0
    g2 = 4 * np.pi * a0
    y0 = [1 / g2, 1 / g2, R0]
    def rhs(l, y):
        aE, aB, v = y
        c = np.sqrt(aB / aE); al = 1 / (4 * np.pi * np.sqrt(aE * aB))
        daE = N / (6 * np.pi ** 2 * v); daB = N * v / (6 * np.pi ** 2)
        dv = -(2 * al / (3 * np.pi)) * (v - c) * (4 * v * v + 3 * v * c + c * c) / (v + c) ** 2 if charge_side else 0.0
        return [daE, daB, dv]
    s = solve_ivp(rhs, (0, l_end), y0, method='LSODA', rtol=1e-10, atol=1e-14, dense_output=True)
    aE, aB, v = s.y[:, -1]
    c = np.sqrt(aB / aE); al = 1 / (4 * np.pi * np.sqrt(aE * aB))
    return v / c, al, c, v

print(f"\n  {'R0':>8} {'alpha0':>7} {'charge side':>11} {'R after 51.5':>13} {'photon speed-up':>15}"
      f" {'charge slow-down':>16} {'alpha_IR':>9}")
for R0 in (2.8e4, 1.5e12):
    for a0 in (1 / 137, 0.08, 1.0):
        for cs in (True, False):
            R, al, c, v = flow(R0, a0, charge_side=cs)
            print(f"  {R0:8.1e} {a0:7.4f} {('on' if cs else 'off'):>11} {R:13.3e} {c:15.2f}x {R0 / v:15.4f}x {al:9.2e}")
# closed form check of the fast phase (charge side off): R^2 = R0^2 / (1 + (2 N alpha0/3pi) R0 l)
R0, a0 = 2.8e4, 1 / 137
Rcf = R0 / np.sqrt(1 + 2 * a0 / (3 * np.pi) * R0 * lmax)
print(f"\n  closed form, charge side off, R0 = 2.8e4, alpha0 = 1/137:  R = {Rcf:.1f}  (numeric above)")
print("  Fast charges speed the photon up, but they also screen the charge: alpha * c stays fixed")
print("  (the electric coefficient a_E hardly moves), so the pull weakens as it works and R falls")
print("  only as 1/sqrt(l). e-folds needed just to reach R = 2 from R0:")
for R0 in (2.8e4, 1.9e6, 1.5e12):
    for a0 in (1 / 137, 0.08, 1.0):
        lneed = (R0 ** 2 / 4 - 1) * 3 * np.pi / (2 * a0 * R0)
        print(f"     R0 = {R0:8.1e}, alpha0 = {a0:6.4f}:  l = {lneed:9.2e}  (available {lmax:.1f})")

# ---------------------------------------------------------------- Part C
hdr("Part C: final approach (speeds nearly equal) and the observational bounds")
print("  Near equal speeds: d delta/dl = -(2 alpha/pi) delta and d alpha/dl = -(2/3pi) alpha^2")
print("  give delta_IR/delta_UV = (alpha_IR/alpha_UV)^3. alpha_IR is measured (1/137); weak coupling")
print("  needs alpha_UV <~ 1, and one-loop QED reaches alpha_UV = 1 only after (3pi/2)(137 - 1) e-folds.")
l_to_1 = 1.5 * np.pi * (137 - 1)
best = (1 / 137) ** 3
print(f"    e-folds from alpha = 1/137 up to alpha = 1: {l_to_1:.0f} (available {lmax:.1f})")
print(f"    best possible reduction at weak coupling: (1/137)^3 = {best:.2e}")
aUV = 1 / (137 - 2 / (3 * np.pi) * lmax)
print(f"    over the real 51.5 e-folds: alpha_UV = 1/{1 / aUV:.1f}, reduction (alpha_IR/alpha_UV)^3 = {(aUV * 137) ** -3:.3f}")
# numeric check of the alpha^3 law
def near(d0, a0, l_end):
    def rhs(l, y):
        d, a = y; return [-(2 * a / np.pi) * d, -(2 / (3 * np.pi)) * a * a]
    s = solve_ivp(rhs, (0, l_end), [d0, a0], rtol=1e-11, atol=1e-30)
    return s.y[0, -1], s.y[1, -1]
d, a = near(1e-2, aUV, lmax)
print(f"    numeric check: delta 1e-2 -> {d:.4e} over 51.5 e-folds ((alpha ratio)^3 predicts {1e-2 * (a / aUV) ** 3:.4e})")
print("\n  Observed limits on the electron-photon speed difference:")
print("    LEP/Tevatron (no vacuum Cherenkov, stable photons): -5.8e-12 <= k_tr - (4/3) c_e00 <= 1.2e-11")
print("    astrophysical (Altschul, as quoted by Anber & Donoghue): |eta| <~ 1e-14")
for start, label in ((1.0, 'delta_UV = 1 (after the fast phase)'), (1e-2, 'delta_UV = 1e-2 (Collins et al. size)')):
    print(f"    {label}: weak-coupling floor {start * best:.1e};  51.5 e-folds give {start * (aUV * 137) ** -3:.1e}")
need = 1e-14 / best
print(f"  To reach 1e-14 at weak coupling the starting mismatch would already have to be <= {need:.1e}.")

hdr("Summary")
print("  A. In the void Coulomb phase there is no window: the charge gap sits (U/t)^L above the photon's")
print("     whole band. Nothing runs. Opening a window means tuning to the Mott edge, where the photon")
print("     is Higgsed.")
print("  B. Granting light charges, one loop drags the photon up only as 1/sqrt(l): R0 = 2.8e4 ends at")
print("     ~600 (alpha0 = 1/137) to ~50 (alpha0 = 1) after the largest window physics offers, and the")
print("     same fast charges screen the coupling: alpha_IR ends 4x to 50x below 1/137.")
print("  C. The last stretch is logarithmic (delta ~ alpha^3). Best case at weak coupling: a factor 4e-7,")
print("     and that needs 641 e-folds (12x more than exist): short of 1e-11 (lab) / 1e-14 (astro) by")
print("     4.5 / 7.4 orders. Over the real 51.5 e-folds the factor is 0.78: short by 11 / 14 orders.")
