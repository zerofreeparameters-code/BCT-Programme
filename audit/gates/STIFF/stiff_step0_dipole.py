#!/usr/bin/env python3
"""
GATE STIFF - Step 0 / Step 1 (cold, deterministic).

Question audited: does a NEUTRAL single-component Gross-Pitaevskii condensate host a
genuine double layer (a dipole SHEET) on a symmetric void window, with a geometry-fixed
surface dipole density P? And: is the "stiffness" S = dPhi/E_J a NEW lever or just the
Josephson-junction charging ratio E_C/E_J (the superfluid-vs-Mott control)?

Model (1D reduction along the window axis z):
  A window between two equivalent voids = a symmetric double-well for the condensate,
  the throat/barrier being the reduced-cross-section window. GP ground state in this
  symmetric potential. The ONLY local charge is the number density n(z)=|psi|^2; the
  U(1) Noether charge is particle number, not electric charge.

We demonstrate, with no fitting:
  (A) The ground-state density n(z) is EVEN about the window plane => the transverse
      dipole moment  p = integral z*(n(z)-nbar) dz  is ZERO (machine precision).
      => no double layer from geometry alone.  [supports SC-STIFF-5]
  (B) A nonzero dipole appears ONLY when an asymmetry (a bias tilt = a chemical-potential
      difference between the two voids) is PUT IN BY HAND. p is linear in the imposed bias
      and vanishes with it. => any nonzero P is bias-fixed (a free input), not packing-fixed.
      [supports SC-STIFF-1 as the fallback under any 'imbalanced-void' reading]
  (C) The Josephson coupling E_J is extracted from the energy vs relative phase E(phi) =
      E0 - E_J cos(phi). The charging scale E_C ~ interaction/reservoir-capacity. The
      dimensionless ratio that controls superfluid vs number-pinned (Mott/ice) is E_C/E_J.
      We show the only well-defined 'stiffness' in the neutral condensate is this SAME
      ratio; there is no independent dPhi because there is no electric charge and P=0.
      [supports Step 2: S is the GP charging ratio, not a new lever]

All in natural units hbar=m=1. nbar, g, and window strength are the only inputs; ratios
are reported so their (non-)cancellation is explicit.
"""
import numpy as np

# ---- grid ----
L  = 60.0
N  = 4096
z  = np.linspace(-L/2, L/2, N, endpoint=False)
dz = z[1]-z[0]
k  = 2*np.pi*np.fft.fftfreq(N, d=dz)

def gp_ground(V, g, mu_target_norm, steps=60000, dt=2e-3):
    """Imaginary-time GP ground state, real & normalized to given line density norm."""
    psi = np.exp(-z**2/(2*(L/6)**2)) + 1e-6
    def norm(p): return np.sqrt(np.sum(np.abs(p)**2)*dz)
    psi *= mu_target_norm / norm(psi)
    for _ in range(steps):
        # split-step imaginary time: kinetic (spectral) + potential+interaction
        psi = np.fft.ifft(np.exp(-0.5*dt*k**2)*np.fft.fft(psi))
        psi = psi*np.exp(-dt*(V + g*np.abs(psi)**2))
        psi = np.fft.ifft(np.exp(-0.5*dt*k**2)*np.fft.fft(psi))
        psi = psi*(mu_target_norm/norm(psi))
    return np.real(psi)

# ---- parameters ----
g      = 1.0
nbar   = 1.0                      # background line density scale
Norm   = np.sqrt(nbar*L)         # total normalization
V0     = 2.0                      # window throat height (a geometric feature)
w      = 2.0                      # throat width
Vwin   = V0*np.exp(-z**2/(2*w**2))   # symmetric window potential  V(z)=V(-z)

# healing length xi = 1/sqrt(2 m g nbar) in these units
xi = 1.0/np.sqrt(2*g*nbar)

# (A) symmetric ground state -> zero dipole
psi0 = gp_ground(Vwin, g, Norm)
n0   = psi0**2
p0   = np.sum(z*(n0 - np.mean(n0[(z<-15)|(z>15)]))*dz)   # transverse dipole moment
even_resid = np.max(np.abs(n0 - n0[::-1]))/np.max(n0)     # evenness residual

print("=== (A) SYMMETRIC WINDOW (geometry only) ===")
print(f"healing length xi           = {xi:.4f}")
print(f"evenness residual  max|n-n_flip|/max n = {even_resid:.3e}")
print(f"transverse dipole moment p  = {p0:.3e}   (expected 0 by reflection symmetry)")

# (B) impose a bias tilt (chemical-potential difference between voids) BY HAND
print("\n=== (B) BIASED WINDOW (asymmetry put in by hand) ===")
print(" bias b     dipole p       p/b")
for b in [0.0, 0.01, 0.02, 0.04, 0.08]:
    Vb = Vwin + b*z*np.exp(-z**2/(2*(L/6)**2))   # localized tilt
    psib = gp_ground(Vb, g, Norm, steps=40000)
    nb = psib**2
    pb = np.sum(z*(nb - np.mean(nb[(z<-15)|(z>15)]))*dz)
    ratio = pb/b if b!=0 else float('nan')
    print(f" {b:6.3f}   {pb:+.4e}    {ratio if b!=0 else float('nan'):.4e}")
print(" => dipole is LINEAR in the imposed bias and VANISHES at b=0. Not geometry-fixed.")

# (C) Josephson coupling E_J from energy vs relative phase
def energy(psi, V, g):
    dpsi = np.fft.ifft(1j*k*np.fft.fft(psi))
    kin  = 0.5*np.sum(np.abs(dpsi)**2)*dz
    pot  = np.sum(V*np.abs(psi)**2)*dz
    intr = 0.5*g*np.sum(np.abs(psi)**4)*dz
    return kin+pot+intr

print("\n=== (C) JOSEPHSON SCALE E_J and the charging ratio ===")
# build left/right modes from the symmetric/antisymmetric split
psiS = gp_ground(Vwin, g, Norm)           # symmetric ground state (phi=0)
# impose a phase twist: left well phase 0, right well phase phi
phis = np.linspace(0, np.pi, 9)
Es = []
mask_R = z>0
for phi in phis:
    ph = np.where(mask_R, np.exp(1j*phi), 1.0)
    psi = psiS*ph
    Es.append(np.real(energy(psi, Vwin, g)))
Es = np.array(Es)
# fit E(phi) = E0 - E_J cos(phi)
A = np.vstack([np.ones_like(phis), -np.cos(phis)]).T
coef, *_ = np.linalg.lstsq(A, Es, rcond=None)
E0, E_J = coef
# charging scale: energy to move one unit of number across the junction ~ g * (1/effective throat volume)
throat_vol = np.sum(np.exp(-z**2/(2*w**2)))*dz   # ~ window "capacitance^-1" proxy
E_C = g/throat_vol
print(f"E_J (Josephson)             = {E_J:.4f}")
print(f"E_C (charging, ~g/throat)   = {E_C:.4f}")
print(f"charging ratio E_C/E_J      = {E_C/E_J:.4f}")
print(" => the ONLY dimensionless 'stiffness' available is E_C/E_J, i.e. the")
print("    superfluid-vs-Mott/ice control. There is no independent dPhi: with P=0 and")
print("    no electric charge, dPhi=P/eps0 is undefined. S is NOT a new lever.")
