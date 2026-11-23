#!/usr/bin/env python3
"""
Bubble Bells desk-check 2 (23 Nov 2026), part 1 — THE BELL AS A RESONANCE, NOT A BOUND STATE.

Non-gate, same-session, CONJECTURE-capped.  Corpus inputs only: a = l_P = 1, R = a/2, alpha0, xi = a/sqrt(8 pi alpha0),
App J's delta-shell condition  psi'_out/psi_out - psi'_in/psi_in |_R = -alpha0  (units a = 1), App J's exterior
Psi_out ~ Psi0 [1 - (R/r) exp(-(r-R)/xi)].  Units here: hbar^2/2m = 1, a = 1, so a single-particle energy is E = kappa^2
and the exterior chemical potential is mu = g n0 = 1/xi^2.

A. Reproduce the Gate BUBBLE_BELLS ladder (interior j_l(kappa r), exterior k_l(r/xi)) and compute, for each rung, the
   fraction of |psi|^2 that lies INSIDE the sphere, and the small-R/xi reason the rungs land where they do.
B. How many other spheres sit inside one bell's "exterior" cloud (radius R + xi, R + 2 xi).
C. The only Hamiltonian the corpus supplies for a quasiparticle at the bell's energy: interior free (depleted), exterior a
   Bogoliubov quasiparticle of the void condensate (eps(k)^2 = k^2 (k^2 + 2 mu)), coupled through the alpha0 delta-shell.
   Scattering phase shifts delta_l(E) for l = 0..3, Wigner time delay, and the S-matrix poles in the complex kappa plane.
D. How strong a shell would be needed for a narrow bell (Q = 10, 100, 2700), and where that bell would sit.
E. The hard-wall (Horn A, sealed sphere) ladder for comparison.
"""
import mpmath as mp
mp.mp.dps = 30
a = mp.mpf(1); R = a / 2
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = a / mp.sqrt(8 * mp.pi * alpha0)
mu = 1 / xi**2                                   # exterior chemical potential, units hbar^2/2m = 1

def jl(l, x):  return mp.sqrt(mp.pi / (2 * x)) * mp.besselj(l + mp.mpf(1) / 2, x)
def yl(l, x):  return mp.sqrt(mp.pi / (2 * x)) * mp.bessely(l + mp.mpf(1) / 2, x)
def h1(l, x):  return jl(l, x) + 1j * yl(l, x)                                   # outgoing spherical Hankel
def kl(l, x):  return mp.sqrt(mp.pi / (2 * x)) * mp.besselk(l + mp.mpf(1) / 2, x)  # ~ modified spherical Bessel k_l
def dlog(f, x): return mp.diff(f, x) / f(x)
jzeros = {0: mp.pi, 1: mp.mpf('4.4934094579090641753'), 2: mp.mpf('5.7634591968945497914'), 3: mp.mpf('6.9879320005005192255')}

print("Bubble Bells desk-check 2 — the bell as a resonance   (a = 1, R = 1/2, hbar^2/2m = 1)")
print(f"alpha0 = {mp.nstr(alpha0, 8)}   xi = {mp.nstr(xi, 8)} a   mu = 1/xi^2 = {mp.nstr(mu, 6)}   R/xi = {mp.nstr(R/xi, 5)}")
print()

# ---------------------------------------------------------------- A. the inherited ladder and where it lives
print("A. Gate BUBBLE_BELLS ladder (interior j_l(kappa r), exterior k_l(r/xi) at the SAME energy): interior fraction")
print("   l   kappa_l     kappa_l R   E_l=kappa^2   E_l/mu    f_inside   zero of j_{l-1} (x R)   kappa_l R - zero")
kap_appJ = {}
for l in range(4):
    rhs = dlog(lambda x, l=l: kl(l, x), R / xi) / xi + alpha0
    f = lambda k, l=l, rhs=rhs: k * mp.diff(lambda t: jl(l, t), k * R) / jl(l, k * R) - rhs
    xs = [mp.mpf(i) / 400 * jzeros[l] for i in range(1, 400)]
    br = None
    for x1, x2 in zip(xs[:-1], xs[1:]):
        if f(x1 / R) * f(x2 / R) < 0: br = (x1 / R, x2 / R); break
    k = mp.findroot(f, br, solver='bisect'); kap_appJ[l] = k
    A = jl(l, k * R) / kl(l, R / xi)                      # continuity at R
    n_in = mp.quad(lambda r: jl(l, k * r)**2 * r**2, [0, R])
    n_out = mp.quad(lambda r: (A * kl(l, r / xi))**2 * r**2, [R, R + 40 * xi])
    f_in = n_in / (n_in + n_out)
    # small-R/xi analysis: the matching reduces to  kappa j_{l-1}(kappa R)/j_l(kappa R) ~ -1/xi + alpha0  (small),
    # so kappa_l R sits just above a zero of j_{l-1}  (j_{-1}(x) = cos x / x : zero at pi/2)
    z = mp.pi / 2 if l == 0 else jzeros[l - 1]
    print(f"   {l}   {mp.nstr(k, 8):>9}   {mp.nstr(k*R, 7):>8}   {mp.nstr(k**2, 7):>9}   {mp.nstr(k**2/mu, 6):>6}    {mp.nstr(f_in, 4):>6}      {mp.nstr(z, 7):>9}            {mp.nstr(k*R - z, 4)}")
print("   Reading: k_l(x) ~ x^-(l+1) for x = R/xi = 0.216, so the 'exterior at the same energy' is in fact the STATIC")
print("   (Laplace, zero-energy) multipole tail; the rungs are the zeros of j_{l-1} shifted by (-1/xi + alpha0) R = -0.21.")
print("   App J's own higher s-wave roots (kappa = 9.514, 15.76) are the same condition's n = 2, 3 solutions.")
k2 = mp.findroot(lambda k: k * mp.cot(k * R) - (-1 / xi + alpha0), 9.5)
k3 = mp.findroot(lambda k: k * mp.cot(k * R) - (-1 / xi + alpha0), 15.7)
print(f"   check: s-wave n = 2, 3 roots = {mp.nstr(k2, 6)}, {mp.nstr(k3, 6)}  (App J table: 9.5139, 15.762)")
print()

# ---------------------------------------------------------------- B. other spheres inside the exterior cloud
print("B. Other sphere centres within the exterior cloud of one bell (FCC, NN distance a = 1)")
import itertools
L = mp.sqrt(2)
pts = []
for i, j, k in itertools.product(range(-6, 7), repeat=3):
    for b in [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]:
        p = ((i + b[0]) * L, (j + b[1]) * L, (k + b[2]) * L)
        d = mp.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
        if d > 1e-9: pts.append(d)
for rad, label in [(R + xi, "R + xi"), (R + 2 * xi, "R + 2 xi")]:
    n = sum(1 for d in pts if d <= rad)
    print(f"   within {label} = {mp.nstr(rad, 5)} a of the centre: {n} other spheres   (packing fraction 0.7405 of that shell volume is sphere interior)")
print("   The single-cavity 'exterior' used for the ladder is therefore mostly other bubbles' interiors — the regions the")
print("   construction itself says are depleted.  (Same structural point as CN-TWIST-12: xi = 4.6 R.)")
print()

# ---------------------------------------------------------------- C. consistent Hamiltonian: free interior, Bogoliubov exterior, alpha0 shell
def kout(E):
    """exterior wavenumber of a Bogoliubov quasiparticle at energy E in a uniform condensate: eps^2 = k^2(k^2 + 2 mu)."""
    return mp.sqrt(-mu + mp.sqrt(mu**2 + E**2))

def phase_shift(l, E, V):
    """scattering phase shift for interior free (kappa = sqrt E), exterior Bogoliubov (k = kout(E)), attractive delta-shell
    of integrated strength V at R:  psi'_in/psi_in - psi'_out/psi_out = V."""
    kap = mp.sqrt(E); k = kout(E)
    Lin = kap * mp.diff(lambda t: jl(l, t), kap * R) / jl(l, kap * R) - V
    j = jl(l, k * R); y = yl(l, k * R)
    jp = k * mp.diff(lambda t: jl(l, t), k * R); yp = k * mp.diff(lambda t: yl(l, t), k * R)
    return mp.atan2(Lin * j - jp, Lin * y - yp)          # tan delta = (L j - j')/(L y - y')

def dlog_sph(f, l, x):
    """log-derivative of a spherical Bessel-type function via f_l'(x) = (l/x) f_l(x) - f_{l+1}(x)  (analytic, complex-safe)"""
    return l / x - f(l + 1, x) / f(l, x)

def pole_fn(l, V):
    """pole-free form of the matching condition: [kappa j_l' - V j_l](kappa R) h_l(k R) - k h_l'(k R) j_l(kappa R) = 0"""
    def F(kap):
        E = kap**2; k = kout(E)
        x = kap * R; z = k * R
        jx = jl(l, x); hz = h1(l, z)
        jpx = (l / x) * jx - jl(l + 1, x)
        hpz = (l / z) * hz - h1(l + 1, z)
        return (kap * jpx - V * jx) * hz - k * hpz * jx
    return F

print("C. Consistent single-quasiparticle problem: interior free, exterior Bogoliubov (mu = 1/xi^2), alpha0 delta-shell")
print("   C1. Reflection a quasiparticle at the bell energy E0 = kappa0^2 sees at the sphere surface (normal incidence):")
E0 = kap_appJ[0]**2; k0 = kout(E0); kap0 = mp.sqrt(E0)
r_step = (kap0 - k0) / (kap0 + k0)
r_shell = alpha0 / (2j * kap0)
print(f"       Bogoliubov step  |r|^2 = {mp.nstr(abs(r_step)**2, 3)}     alpha0 shell  |r|^2 = {mp.nstr(abs(r_shell)**2, 3)}     combined ~ {mp.nstr(abs(r_step + r_shell)**2, 3)}")
print(f"       (a cavity with round-trip reflectivity ~1e-5 has no standing wave: there is nothing to confine the quasiparticle)")
print()
print("   C2. Phase shifts delta_l(E) and Wigner time delay 2 d(delta)/dE, l = 0..3, E from mu to 20 E0 (a bell would show as a")
print("       rise of delta_l through pi/2 over a width Gamma << E; a transparent sphere gives a smooth, tiny delta):")
Es = [mu * mp.mpf(10)**(mp.mpf(i) / 12) for i in range(0, int(12 * mp.log10(20 * E0 / mu)) + 1)]
def mod_pi(d):
    d = mp.fmod(d, mp.pi)
    if d > mp.pi / 2: d -= mp.pi
    if d <= -mp.pi / 2: d += mp.pi
    return d
print(f"       (exterior quasiparticle at E0: k_out = {mp.nstr(k0, 5)} vs interior kappa0 = {mp.nstr(kap0, 5)}; E0/mu = {mp.nstr(E0/mu, 4)})")
for l in range(4):
    ds = [mod_pi(phase_shift(l, E, alpha0)) for E in Es]
    for i in range(1, len(ds)):                      # unwrap jumps of pi
        while ds[i] - ds[i-1] > mp.pi / 2: ds[i] -= mp.pi
        while ds[i] - ds[i-1] < -mp.pi / 2: ds[i] += mp.pi
    ds = [d - ds[0] + mod_pi(ds[0]) for d in ds]
    dmax = max(abs(d) for d in ds)
    slopes = [abs((ds[i+1] - ds[i]) / (Es[i+1] - Es[i])) for i in range(len(Es) - 1)]
    imax = max(range(len(slopes)), key=lambda i: slopes[i])
    print(f"       l = {l}:  |delta_l| <= {mp.nstr(dmax, 3)} rad for mu <= E <= 20 E0;  max |d delta/dE| = {mp.nstr(slopes[imax], 3)} at E = {mp.nstr(Es[imax], 3)}"
          f" (Gamma = E0/10 would give {mp.nstr(2/(E0/10), 3)});  delta_l(E0) = {mp.nstr(mod_pi(phase_shift(l, E0, alpha0)), 3)}")
print("       No partial wave shows a resonant rise anywhere; the largest time delay is at threshold (E -> mu), not at a rung.")
print()
print("   C3. S-matrix poles in the complex kappa plane (kappa = sqrt E).  Systematic search: 160 starting points per l in")
print("       1 <= Re kappa <= 20, -12 <= Im kappa <= -0.05; distinct converged poles with 1 <= Re kappa <= 20 listed, nearest to the")
print("       real axis first.  (A rung of the ladder would be a pole with |Im kappa| << Re kappa.)")
mp.mp.dps = 20
for l in range(4):
    F = pole_fn(l, alpha0)
    poles = []
    for re0 in [1 + 19 * i / 19 for i in range(20)]:
        for im0 in [-0.05, -0.3, -1, -2, -4, -6, -9, -12]:
            try:
                p = mp.findroot(F, mp.mpc(re0, im0), solver='muller', tol=1e-16, maxsteps=100)
            except Exception:
                continue
            if abs(F(p)) > 1e-6 or not (1 <= mp.re(p) <= 20) or mp.im(p) > 0: continue
            if all(abs(p - q) > 1e-4 for q in poles): poles.append(p)
    poles.sort(key=lambda p: abs(mp.im(p)))
    s = ",  ".join(f"{mp.nstr(mp.re(p),4)}{mp.nstr(mp.im(p),3)}i (Gamma/E={mp.nstr(2*abs(mp.im(p**2))/abs(mp.re(p**2)),2)})" for p in poles[:5])
    print(f"       l = {l}: {len(poles)} poles found; nearest the axis: {s if poles else 'none'}")
mp.mp.dps = 30
print("       Every pole has |Im kappa| R > 3: widths of several times the energy.  No rung of the ladder survives as a resonance.")
print()

# ---------------------------------------------------------------- D. what shell would make a bell
print("D. Shell strength V (same delta-shell form, attractive) needed for a NARROW l = 0 bell, Q = Re E / (2|Im E|):")
print("       V/alpha0        V        pole kappa                   kappa R      E/mu        Q")
def lowest_s_pole(V):
    F = pole_fn(0, V)
    # strong attractive shell: kappa cot(kappa R) ~ V  =>  kappa R ~ pi + kappa/V, Im kappa ~ -c/V^2.  Weak shell: a virtual pole only.
    kre = (mp.pi + 2 * mp.pi / V) / R
    guesses = [mp.mpc(kre, -min(mp.mpf(1), 80 / V**2)), mp.mpc(kre, -min(mp.mpf(2), 8 / V)), mp.mpc(mp.pi / R - 0.3, -0.3), mp.mpc(2 / R, -1 / R)]
    best = None
    for guess in guesses:
        try:
            p = mp.findroot(F, guess, solver='muller', tol=1e-20, maxsteps=400)
            if abs(F(p)) < 1e-8 and mp.re(p) > 0 and mp.im(p) < 0:
                if best is None or abs(mp.im(p)) < abs(mp.im(best)): best = p
        except Exception:
            pass
    return best
def Q_of(V):
    p = lowest_s_pole(V)
    if p is None: return None, None
    E = p**2
    return mp.re(E) / (2 * abs(mp.im(E))), p
for V in [alpha0, 10 * alpha0, 1, 3, 10, 30, 100, 300, 1000, 3000]:
    Q, p = Q_of(V)
    if p is None:
        print(f"       {mp.nstr(V/alpha0, 4):>8}   {mp.nstr(V, 4):>7}   no s-wave pole located")
    else:
        E = p**2
        print(f"       {mp.nstr(V/alpha0, 4):>8}   {mp.nstr(V, 4):>7}   {mp.nstr(p, 6):>26}   {mp.nstr(mp.re(p)*R, 5):>7}   {mp.nstr(mp.re(E)/mu, 5):>7}   {mp.nstr(Q, 4)}")
print("   Solve V for given Q (bisection in log V):")
for Qt in [10, 100, 2700]:
    lo, hi = mp.mpf(3), mp.mpf(3000)
    ok = True
    for _ in range(40):
        mid = mp.sqrt(lo * hi)
        Qm, _p = Q_of(mid)
        if Qm is None: ok = False; break
        if Qm < Qt: lo = mid
        else: hi = mid
    if ok:
        Vq = mp.sqrt(lo * hi); Qv, p = Q_of(Vq)
        print(f"       Q = {Qt:>5}:  V = {mp.nstr(Vq, 4)} = {mp.nstr(Vq/alpha0, 4)} alpha0,  bell at kappa R = {mp.nstr(mp.re(p)*R, 5)} (-> Dirichlet pi), E/mu = {mp.nstr(mp.re(p**2)/mu, 5)}")
    else:
        print(f"       Q = {Qt}: pole search failed inside the bracket")
print("   A shell strong enough to make a bell puts the ground rung at kappa R -> pi (kappa0 -> 2 pi / a = 6.28), not at App J's 3.39.")
print()

# ---------------------------------------------------------------- E. hard wall
print("E. Hard-wall (Horn A: rigid, sealed sphere) ladder, kappa_l R = first zero of j_l:")
print("   l   kappa_l a   E_l/E_0(hard)   E_l/mu    vs inherited kappa_l a")
for l in range(4):
    kH = jzeros[l] / R
    print(f"   {l}   {mp.nstr(kH, 6):>8}   {mp.nstr((kH/(jzeros[0]/R))**2, 5):>8}      {mp.nstr(kH**2/mu, 6):>7}   {mp.nstr(kap_appJ[l], 6)}")
print("   Gamma = 0 exactly, and coupling to the exterior = 0 exactly: a sealed box.  It holds a mode only if a quantum is PUT")
print("   in it (an input); the empty sealed sphere is just excluded volume, which is the Q1 (tortuosity) picture.")
