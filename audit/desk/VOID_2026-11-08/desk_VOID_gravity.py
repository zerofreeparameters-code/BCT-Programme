#!/usr/bin/env python3
"""
Desk-check VOID-GRAVITY (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
Question: can gravity be the Bjerknes force between spheres that breathe in step?
  Bjerknes (1875/1906): in an incompressible ideal fluid, two spheres pulsating in phase attract with an
  inverse-square force proportional to the product of their pulsation strengths.
BCT premises used (corpus, Appendices Vol. 1 sec. 1): the medium is compressible with sound speed
c_s = c (light is the medium's sound); its density is the Planck density.

Notation: a breathing body has volume V(t) = V0 + dV(t), volume flux q = dV/dt = q0 cos(w t) (in phase).
Pressure of a monopole source, retarded:  p(r,t) = rho * qdot(t - r/c_s) / (4 pi r).
Force on body 2: F = -V2(t) grad p1 (buoyancy-type, small body). Only the dV2 part survives averaging.

Parts
 A  the law: time-averaged force, compressible case, checked by direct quadrature;
    the size of the alternating part
 B  strength: pulsation needed to reproduce Newton's G
 C  equivalence of inertial and gravitational mass: a lower bound on the frequency
 D  the frequency window: lower bounds against upper bounds
 E  can the VOID-Q1 liquid carry the flow?
 F  energy radiated as sound (= light in BCT)
 G  light bending
Runs in about a second.
"""
import numpy as np
from scipy.optimize import brentq

G, c, hbar = 6.674e-11, 2.998e8, 1.0546e-34
tP = np.sqrt(hbar * G / c ** 5); lP = c * tP; mP = np.sqrt(hbar * c / G); rhoP = c ** 5 / (hbar * G ** 2)
yr = 3.156e7
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# ---------------------------------------------------------------- A
hdr("A. The law: two spheres breathing in phase, time-averaged force")
print("  closed form (derived here): <F_r> = -(rho q0^2 / (8 pi r^2)) [cos kr + kr sin kr],  k = w/c_s")
print("  (negative = attraction).  Incompressible limit kr -> 0: -rho q0^2/(8 pi r^2) = -rho<q1 q2>/(4 pi r^2)")
rho, q0, w, cs = 1.0, 1.0, 1.0, 1.0
def F_numeric(r, n=200000):
    t = np.linspace(0, 2 * np.pi / w, n, endpoint=False)
    k = w / cs; tr = t - r / cs
    dV2 = (q0 / w) * np.sin(w * t)                         # volume part of body 2 that oscillates
    qd1 = -q0 * w * np.sin(w * tr); qdd1 = -q0 * w * w * np.cos(w * tr)
    dpdr = rho / (4 * np.pi) * (-qdd1 / (cs * r) - qd1 / r ** 2)   # d/dr of rho qdot(t-r/c)/(4 pi r)
    return np.mean(-dV2 * dpdr)
def F_closed(r):
    x = w * r / cs; return -(rho * q0 ** 2 / (8 * np.pi * r ** 2)) * (np.cos(x) + x * np.sin(x))
print(f"  {'kr':>6} {'numeric':>13} {'closed form':>13}  ratio to incompressible")
for x in (0.01, 0.3, 1.0, 2.0, 2.8, 3.5, 6.0, 10.0):
    r = x * cs / w; fn, fc = F_numeric(r), F_closed(r)
    print(f"  {x:6.2f} {fn:13.5e} {fc:13.5e}  {fc / (-(rho * q0 ** 2) / (8 * np.pi * r ** 2)):+.4f}")
x0 = brentq(lambda x: np.cos(x) + x * np.sin(x), 2.0, 3.2)
print(f"  attraction turns into repulsion at kr = {x0:.4f}, i.e. r = {x0 / (2 * np.pi):.3f} wavelengths;")
print("  beyond that the force oscillates in sign and falls as 1/r, not 1/r^2.")
print("  Alternating part: the undisplaced volume V0 gives a zero-mean force rho V0 qdot1/(4 pi r^2).")
print("  Its amplitude / mean attraction = 2 V0 w / q0 = 2/eps, eps = dV/V0 <= 1: at least TWICE gravity.")

# ---------------------------------------------------------------- B
hdr("B. Strength: pulsation needed to give Newton's law")
print("  rho q01 q02 /(8 pi) = G m1 m2  ->  q0 = m sqrt(8 pi G / rho)")
k_q = np.sqrt(8 * np.pi * G / rhoP)
print(f"  with rho = Planck density {rhoP:.3e} kg/m^3: q0/m = {k_q:.3e} m^3 s^-1 per kg")
print(f"  a Planck mass must breathe q0 = sqrt(8 pi) l_P^3/t_P = {np.sqrt(8 * np.pi):.3f} Planck volumes per Planck time")
for name, m in (("proton", 1.6726e-27), ("Earth", 5.972e24), ("Sun", 1.989e30)):
    print(f"    {name:7s}: q0 = {m * k_q:.3e} m^3/s")

# ---------------------------------------------------------------- C
hdr("C. Equivalence principle: the frequency must exceed sqrt(2 pi G rho)")
print("  A body of volume V moving through an ideal fluid carries added mass rho V/2, so m_inertial >= rho V/2.")
print("  Its breathing flux is at most q0 = w dV <= w V. Gravitational charge q0 = m sqrt(8 pi G/rho).")
print("  m_grav = m_inertial for every body  =>  m sqrt(8 pi G/rho) <= 2 w m / rho  =>  w >= sqrt(2 pi G rho).")
w_eq = np.sqrt(2 * np.pi * G * rhoP)
print(f"  BCT (rho = Planck density): w >= {w_eq:.3e} s^-1 = {w_eq * tP:.3f} / t_P  (above the Planck frequency)")
r_flip = x0 * c / w_eq
print(f"  with c_s = c the attraction then reverses at r = {r_flip:.2e} m = {r_flip / lP:.2f} Planck lengths.")
print("  So in a Planck-density medium whose sound speed is c, Bjerknes attraction cannot reach past ~1 l_P.")
rho_max = (x0 * c / 2.5e20) ** 2 / (2 * np.pi * G)
print(f"  (For the attraction to reach the Galaxy, 2.5e20 m, the medium would need rho <= {rho_max:.1e} kg/m^3.)")

# ---------------------------------------------------------------- D
hdr("D. Frequency window (c_s = c). Every lower bound must sit below every upper bound.")
lower = [("gravity steady over a low-Earth orbit (alternating part >= 2x must average out): w >> 2pi/90 min",
          2 * np.pi / 5400.0),
         ("equivalence principle in a Planck-density medium (part C)", w_eq)]
upper = [("inverse-square to 1% out to Neptune (4.5e12 m): (kr)^2/2 < 0.01", np.sqrt(0.02) * c / 4.5e12),
         ("still attractive at the Sun's galactic orbit (2.5e20 m): kr < 2.80", x0 * c / 2.5e20),
         ("Sun and Earth stay in phase for 4.5 Gyr if pulsations redshift like all clocks (dw/w = 2.1e-6)",
          (np.pi / 2) / (4.5e9 * yr * 2.12e-6))]
for s, v in lower: print(f"  LOWER  {v:10.2e} s^-1   {s}")
for s, v in upper: print(f"  UPPER  {v:10.2e} s^-1   {s}")
lo_min, up_max = min(v for _, v in lower), max(v for _, v in upper)
print(f"\n  most lenient pair: lower {lo_min:.2e} vs upper {up_max:.2e} -> window empty by a factor {lo_min / up_max:.0f}")
print(f"  with BCT's own density: lower {w_eq:.2e} vs upper {up_max:.2e} -> empty by {np.log10(w_eq / up_max):.0f} orders")
cs_need = lo_min / up_max
print(f"  The lenient gap closes only if the medium's sound is >= {cs_need:.0f} c, but in BCT sound is light (c_s = c).")

# ---------------------------------------------------------------- E
hdr("E. Can the VOID-Q1 liquid carry the breathing flow?")
print("  Q1's liquid is a Mott state: density changes cost the gap, mass currents are blocked. A static push")
print("  spreads only by virtual hops, each costing t/U, so it decays as (z t/U)^(r/a): range l = a / ln(U/(z t)).")
z = 12
for Ut in (70, 310, 1241, 6421):
    l = 1 / np.log(Ut / z)
    print(f"    U/t = {Ut:5d}: range {l:.2f} a  (force down by e^-{1 / l:.1f} per void spacing)")
print("  So the void liquid screens the breathing within one void spacing. Long-range flow needs the")
print("  gapless superfluid, which brings in sound at c_s = c and the limits of part D.")

# ---------------------------------------------------------------- F
hdr("F. Energy radiated as sound (in BCT, sound is light)")
print("  monopole radiation: P = rho q0^2 w^2/(8 pi c_s) = G m^2 w^2 / c_s  (independent of rho)")
wL = 2 * np.pi / 5400.0
for name, m in (("Earth", 5.972e24), ("Sun", 1.989e30)):
    P = G * m ** 2 * wL ** 2 / c; tdrain = m * c ** 2 / P
    print(f"    {name:5s} at the lenient minimum w = {wL:.1e}: P = {P:.2e} W, rest energy gone in {tdrain / yr:.1e} yr")
print(f"    (solar luminosity 3.8e26 W: the Sun would shine {G * 1.989e30 ** 2 * wL ** 2 / c / 3.828e26:.1e} times brighter, at frequency w)")

# ---------------------------------------------------------------- G
hdr("G. Light bending")
print("  The force acts only between bodies that breathe in step: its 1/r part is <q1 q2>, which is zero for")
print("  anything not pulsating at w. The time-averaged pressure round one breathing body is second order,")
print("  ~ rho <v^2>/2 ~ 1/r^4, so light sees no 1/r potential: no deflection, no Shapiro delay.")
print("  Even if light were made to breathe in step, a scalar force gives at most the Newtonian half.")
print("  Observed: gamma = 1 + (2.1 +- 2.3)e-5 (Cassini), i.e. full GR bending to ~1e-5.")

hdr("Summary")
print("  A. Law and sign right at short range: in-phase breathing attracts as 1/r^2 (Bjerknes).")
print("  B-C. Matching G with inertial = gravitational mass forces w >= sqrt(2 pi G rho), above the Planck")
print("       frequency for BCT's density; with c_s = c the attraction then reverses beyond ~1 Planck length.")
print("  D. Independently of density, steady gravity (w >~ 1e-3 /s) and inverse-square over the solar system")
print("     with c_s = c (w <~ 1e-5 /s) exclude each other; phase-locking under redshift needs w <~ 5e-12 /s.")
print("  E. The Q1 void liquid cannot carry the flow at all (range < 1 void spacing).")
print("  F. Breathing bodies would radiate their rest mass as light: the Sun within ~4,000 yr.")
print("  G. No light bending. FAIL.")
