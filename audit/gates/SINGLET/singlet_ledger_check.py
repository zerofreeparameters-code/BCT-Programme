"""Gate SINGLET ledger-entry checks. Written in the ledger thread, 25 Oct 2026,
without opening the run's scripts. numpy for the walk, mpmath (60 dps working, 40 reported)
for closed forms."""
import itertools, sys
import numpy as np
import mpmath as mp
mp.mp.dps = 60
out = []
def say(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

# 1. Construction on the 2m-site double cover, written from the card's description
def construction(m, p, t, settings_deg):
    n2 = 2*m
    K = np.zeros((n2, n2))
    for k in range(n2):
        K[k, k] = 1 - p; K[k, (k+1) % n2] += p/2; K[k, (k-1) % n2] += p/2
    Kt = np.linalg.matrix_power(K, t)
    G = lambda k, j: Kt[k, j % n2] - Kt[k, (j + m) % n2]       # antiperiodic projection to base site j
    def M(ja, jb):
        return sum(G(k, ja) * G((k + m//2) % n2, jb) for k in range(n2))
    res = {}
    for a in settings_deg:
        for b in settings_deg:
            ja, jb = round(a*m/360), round(b*m/360)
            amp = {(sA, sB): M(ja + (0 if sA > 0 else m//2), jb + (0 if sB > 0 else m//2))
                   for sA in (1, -1) for sB in (1, -1)}
            N = sum(v*v for v in amp.values())
            P = {k: v*v/N for k, v in amp.items()}
            E = sum(sA*sB*P[(sA, sB)] for (sA, sB) in P)
            res[(a, b)] = (E, P[(1, 1)] + P[(1, -1)], N)
    return res

# Settings every 15 deg (24 x 24 = 576 pairs). At t = 3200 this direct double-cover form
# loses digits to cancellation (the antiperiodic part is ~1e-6 of each matrix entry).
angles = [15*i for i in range(24)]
for m, p, t in [(24, 0.5, 800), (24, 0.5, 3200)]:
    r = construction(m, p, t, angles)
    dE = max(abs(E + np.cos(np.radians(b - a))) for (a, b), (E, _, _) in r.items())
    say(f"[1] own construction m={m} p={p} t={t}: max|E+cos(b-a)| over {len(r)} pairs = {dE:.1e}")
    S = r[(0, 45)][0] - r[(0, 135)][0] + r[(90, 45)][0] + r[(90, 135)][0]
    say(f"    CHSH a,a'=0,90 b,b'=45,135 deg = {S:.15f}   2*sqrt2 = {2*np.sqrt(2):.15f}")
    sp = max(max(r[(a, b)][1] for b in angles) - min(r[(a, b)][1] for b in angles) for a in angles)
    say(f"    max spread of P_A(+|a,b) over distant b = {sp:.1e}")
    Ns = [v[2] for v in r.values()]
    say(f"    rel. variation of normalisation N(a,b) = {(max(Ns)-min(Ns))/np.mean(Ns):.1e}")

# periodic sector (no Z2): replace the antiperiodic projection by the periodic one
def periodic(m, p, t):
    n2 = 2*m; K = np.zeros((n2, n2))
    for k in range(n2):
        K[k, k] = 1 - p; K[k, (k+1) % n2] += p/2; K[k, (k-1) % n2] += p/2
    Kt = np.linalg.matrix_power(K, t)
    G = lambda k, j: Kt[k, j % n2] + Kt[k, (j + m) % n2]
    E = []
    for a, b in [(0, 45), (0, 135), (90, 45), (90, 135)]:
        ja, jb = round(a*m/360), round(b*m/360)
        amp = {(sA, sB): sum(G(k, ja + (0 if sA > 0 else m//2)) * G((k+m//2) % n2, jb + (0 if sB > 0 else m//2)) for k in range(n2))
               for sA in (1, -1) for sB in (1, -1)}
        N = sum(v*v for v in amp.values()); E.append(sum(sA*sB*v*v/N for (sA, sB), v in amp.items()))
    return E[0] - E[1] + E[2] + E[3]
say(f"[1b] periodic sector (Z2 dropped), t=3200: |S| = {abs(periodic(24, 0.5, 3200)):.1e}")

# 2. Closed forms, mpmath
lam = lambda n: 1 - mp.mpf(1)/2 + mp.mpf(1)/2*mp.cos(mp.pi*n/24)
say(f"[2] lambda3/lambda1 (m=24, p=1/2) = {mp.nstr(lam(3)/lam(1), 40)}")
say(f"    visibility of sign readout of the n=1 harmonic, (2/pi)^2 = {mp.nstr((2/mp.pi)**2, 40)}")
say(f"    |S| = 2 sqrt2 (2/pi)^2 = {mp.nstr(2*mp.sqrt(2)*(2/mp.pi)**2, 40)}")
say("    readout exponent: sum_AB |M|^q = 2(|sin th/2|^q + |cos th/2|^q); relative variation over th in [0,pi]:")
for q in [mp.mpf('0.5'), 1, mp.mpf('1.5'), 2, 3, 4]:
    vals = [2*(abs(mp.sin(th/2))**q + abs(mp.cos(th/2))**q) for th in mp.linspace(0, mp.pi, 181)]
    say(f"      q={mp.nstr(q, 3):>4}: {mp.nstr((max(vals)-min(vals))/(sum(vals)/len(vals)), 6)}")

# 3. Lattice: c/a = sqrt2 bct is fcc, and spin structures fixed by the point group
a, c = 1.0, np.sqrt(2)
pts = np.array([(i*a, j*a, k*c) for i in range(-3, 4) for j in range(-3, 4) for k in range(-3, 4)] +
               [((i+.5)*a, (j+.5)*a, (k+.5)*c) for i in range(-3, 3) for j in range(-3, 3) for k in range(-3, 3)])
d = np.sort(np.round(np.linalg.norm(pts, axis=1), 9)); d = d[d > 0]
say(f"[3] bct c/a=sqrt2: nearest-neighbour distance {d[0]:.6f}, count {int(np.sum(d == d[0]))}")

def invariant_spin_structures(basis, group):
    B = np.array(basis, float).T; Binv = np.linalg.inv(B); inv = []
    for eps in itertools.product((0, 1), repeat=3):
        ok = True
        for g in group:
            Mg = np.rint(Binv @ g @ B).astype(int)       # action on lattice coordinates
            for i in range(3):
                if sum(eps[j]*Mg[j, i] for j in range(3)) % 2 != eps[i]: ok = False
        if ok: inv.append(eps)
    return inv
signs = list(itertools.product((1, -1), repeat=3))
Oh = [np.diag(s) @ np.eye(3)[list(pm)] for pm in itertools.permutations(range(3)) for s in signs]
D4h = [g for g in Oh if abs(g[2, 2]) == 1]
fcc = [(0, .5, .5), (.5, 0, .5), (.5, .5, 0)]
bct = [(1, 0, 0), (0, 1, 0), (.5, .5, .5)]
say(f"    fcc lattice, O_h (order {len(Oh)}): invariant spin structures {invariant_spin_structures(fcc, Oh)}")
say(f"    bct lattice, D4h (order {len(D4h)}): invariant spin structures {invariant_spin_structures(bct, D4h)}")

with open(sys.argv[1], "w") as f: f.write("\n".join(out) + "\n")
