#!/usr/bin/env python3
"""Independent check: FCC interstitial chambers, exact geometry, x-values, FD eigenvalues."""
import sys, time
import numpy as np
import sympy as sp
import mpmath as mp
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import pyamg

mp.mp.dps = 60
out = []
def P(s=""):
    print(s); out.append(str(s)); sys.stdout.flush()
def f30(x): return mp.nstr(mp.mpf(x), 30)
def f10(x): return mp.nstr(mp.mpf(x), 10)

# ---------------------------------------------------------------- A. exact
P("=== A. EXACT ===")
pi = sp.pi
Om_tet = sp.acos(sp.Rational(23, 27))          # solid angle at regular tet vertex
Om_oct = 4*sp.asin(sp.Rational(1, 3))          # solid angle at regular oct vertex
R = sp.Rational(1, 2)
Vtet_poly = sp.sqrt(2)/12                       # regular tetrahedron edge 1
Voct_poly = sp.sqrt(2)/3                        # regular octahedron edge 1
sector = lambda Om: Om/(4*pi) * sp.Rational(4, 3)*pi*R**3   # = Om/24
V_tet = sp.simplify(Vtet_poly - 4*sector(Om_tet))
V_oct = sp.simplify(Voct_poly - 6*sector(Om_oct))
A_tet = sp.simplify(4*R**2*Om_tet)
A_oct = sp.simplify(6*R**2*Om_oct)
ev = lambda e: mp.mpf(sp.N(e, 60))
P("A1 V_tet = %s = %s" % (V_tet, f30(ev(V_tet))))
P("A1 V_oct = %s = %s" % (V_oct, f30(ev(V_oct))))
P("A2 wall area tet = %s = %s" % (A_tet, f30(ev(A_tet))))
P("A2 wall area oct = %s = %s" % (A_oct, f30(ev(A_oct))))

# A3: identity V_oct + 2 V_tet = 1/sqrt2 - pi/6  <=>  asin(1/3) + acos(23/27)/3 = pi/6
# Proof: theta = acos(1/3); cos(3 theta) = 4c^3-3c = -23/27 -> 3 theta - pi in [0,pi] and cos(3theta-pi)=23/27
# so acos(23/27) = 3 acos(1/3) - pi; asin(1/3) = pi/2 - acos(1/3).  Sum = pi/2 - acos(1/3) + acos(1/3) - pi/3 = pi/6.
c = sp.Rational(1, 3)
cos3 = sp.expand(4*c**3 - 3*c)
P("A3 cos(3*acos(1/3)) = 4c^3-3c = %s ; so cos(3acos(1/3)-pi) = %s" % (cos3, -cos3))
th3 = 3*sp.acos(c) - pi
P("A3 3acos(1/3)-pi in [0,pi]? numeric = %s" % f30(ev(th3)))
diff = sp.simplify(V_oct + 2*V_tet - (1/sp.sqrt(2) - pi/6))
diff_sub = diff.subs(sp.acos(sp.Rational(23, 27)), 3*sp.acos(c) - pi).subs(sp.asin(c), pi/2 - sp.acos(c))
P("A3 symbolic residual after identities: %s" % sp.simplify(diff_sub))
mp.mp.dps = 60
num = ev(V_oct + 2*V_tet) - (1/mp.sqrt(2) - mp.pi/6)
P("A3 numeric (V_oct+2V_tet) - (1/sqrt2 - pi/6) = %s" % mp.nstr(num, 5))
P("A3 V_oct+2V_tet = %s" % mp.nstr(ev(V_oct + 2*V_tet), 50))
P("A3 1/sqrt2-pi/6 = %s" % mp.nstr(1/mp.sqrt(2) - mp.pi/6, 50))
P("A3 VERDICT: identity holds exactly (acos(23/27) = 3acos(1/3) - pi, asin(1/3) = pi/2 - acos(1/3))")

# A4
r_tet = sp.sqrt(6)/4 - R
r_oct = 1/sp.sqrt(2) - R
Vb_tet = sp.Rational(4, 3)*pi*r_tet**3
Vb_oct = sp.Rational(4, 3)*pi*r_oct**3
mub_tet = pi**2/r_tet**2
mub_oct = pi**2/r_oct**2
P("A4 r_tet = %s" % f30(ev(r_tet)))
P("A4 r_oct = %s" % f30(ev(r_oct)))
P("A4 V_ball_tet = %s" % f30(ev(Vb_tet)))
P("A4 V_ball_oct = %s" % f30(ev(Vb_oct)))
P("A4 V_tet/V_ball_tet = %s" % f30(ev(V_tet/Vb_tet)))
P("A4 V_oct/V_ball_oct = %s" % f30(ev(V_oct/Vb_oct)))
P("A4 mu_ball_tet = pi^2/r_tet^2 = %s" % f30(ev(mub_tet)))
P("A4 mu_ball_oct = pi^2/r_oct^2 = %s" % f30(ev(mub_oct)))

# A5 Monte Carlo
rng = np.random.default_rng(20261017)
n = 2_000_000
# tetrahedron: vertices of regular tet edge 1 (sphere centres)
T = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0.5, np.sqrt(3)/6, np.sqrt(6)/3]])
u = np.sort(rng.random((n, 3)), axis=1)
bary = np.column_stack([u[:, 0], u[:, 1]-u[:, 0], u[:, 2]-u[:, 1], 1-u[:, 2]])
pts = bary @ T
d2 = ((pts[:, None, :] - T[None, :, :])**2).sum(-1)
inside = (d2 < 0.25).any(1)
p = 1 - inside.mean()
Vt_mc = float(Vtet_poly.evalf(30))*p
st = float(Vtet_poly.evalf(30))*np.sqrt(p*(1-p)/n)
P("A5 MC V_tet = %.8f +- %.8f  z = %+.3f" % (Vt_mc, st, (Vt_mc - float(ev(V_tet)))/st))
# octahedron: |x|+|y|+|z| <= s, s = 1/sqrt2
s = 1/np.sqrt(2)
u = np.sort(rng.random((n, 3)), axis=1)
q = np.column_stack([u[:, 0], u[:, 1]-u[:, 0], u[:, 2]-u[:, 1]])*s   # uniform in simplex x+y+z<=s
sg = rng.choice([-1.0, 1.0], size=(n, 3))
pts = q*sg
O = np.array([[s, 0, 0], [-s, 0, 0], [0, s, 0], [0, -s, 0], [0, 0, s], [0, 0, -s]])
d2 = ((pts[:, None, :] - O[None, :, :])**2).sum(-1)
inside = (d2 < 0.25).any(1)
p = 1 - inside.mean()
Vo_mc = float(Voct_poly.evalf(30))*p
so = float(Voct_poly.evalf(30))*np.sqrt(p*(1-p)/n)
P("A5 MC V_oct = %.8f +- %.8f  z = %+.3f" % (Vo_mc, so, (Vo_mc - float(ev(V_oct)))/so))

# ---------------------------------------------------------------- C. finite differences
P("")
P("=== C. FINITE-DIFFERENCE EIGENVALUES ===")

def build(dom, dir_mask, periodic, h):
    """dom: bool array of domain points. dir_mask: bool array of Dirichlet points.
    Neighbours that are neither domain nor Dirichlet are dropped (Neumann)."""
    idx = -np.ones(dom.shape, dtype=np.int64)
    nd = int(dom.sum())
    idx[dom] = np.arange(nd)
    diag = np.zeros(nd)
    rows, cols = [], []
    for ax in range(3):
        for sh in (+1, -1):
            if periodic:
                nidx = np.roll(idx, -sh, axis=ax)
                ndir = np.roll(dir_mask, -sh, axis=ax)
            else:
                nidx = np.full(idx.shape, -1, dtype=np.int64)
                ndir = np.zeros(idx.shape, dtype=bool)
                src = [slice(None)]*3; dst = [slice(None)]*3
                if sh == 1:
                    src[ax] = slice(1, None); dst[ax] = slice(0, -1)
                else:
                    src[ax] = slice(0, -1); dst[ax] = slice(1, None)
                nidx[tuple(dst)] = idx[tuple(src)]
                ndir[tuple(dst)] = dir_mask[tuple(src)]
            ni = nidx[dom]; nd_ = ndir[dom]
            has = ni >= 0
            diag[has] += 1.0
            diag[nd_] += 1.0
            rows.append(np.nonzero(has)[0]); cols.append(ni[has])
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    A = sps.coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(nd, nd)).tocsr()
    A = A + sps.diags(diag)
    return (A/h**2).tocsr(), nd

def lowest(A):
    ml = pyamg.smoothed_aggregation_solver(A, max_coarse=200)
    M = ml.aspreconditioner(cycle='V')
    cnt = [0]
    def solve(b):
        x, info = spla.cg(A, b, M=M, rtol=1e-12, atol=0, maxiter=2000)
        if info != 0:
            raise RuntimeError("CG did not converge: info=%d" % info)
        cnt[0] += 1
        return x
    OPinv = spla.LinearOperator(A.shape, matvec=solve, dtype=float)
    vals, vecs = spla.eigsh(A, k=1, sigma=0.0, which='LM', OPinv=OPinv, tol=1e-13, maxiter=5000)
    lam = vals[0]; v = vecs[:, 0]
    res = np.linalg.norm(A @ v - lam*v)/np.linalg.norm(v)
    return lam, res, cnt[0]

def domains(N):
    a = np.sqrt(2.0); h = a/N; m = N//2; R2 = N*N//8     # sphere radius^2 in grid units (integer)
    assert N*N % 8 == 0
    ii = np.arange(N)
    I, J, K = np.meshgrid(ii, ii, ii, indexing='ij')
    def mi(d):  # minimum image in grid units
        d = np.mod(d, N); return np.where(d > N//2, d - N, d)
    # (a) ball centred at (m,m,m)
    ball = (I-m)**2 + (J-m)**2 + (K-m)**2 < R2
    # (b) network: outside all four FCC spheres (min image)
    insph = np.zeros(I.shape, bool)
    for (ci, cj, ck) in [(0, 0, 0), (0, m, m), (m, 0, m), (m, m, 0)]:
        insph |= mi(I-ci)**2 + mi(J-cj)**2 + mi(K-ck)**2 < R2
    # (c) octahedral chamber, box [-m-1, m+1]^3
    jj = np.arange(-m-1, m+2)
    I2, J2, K2 = np.meshgrid(jj, jj, jj, indexing='ij')
    poly_o = (np.abs(I2)+np.abs(J2)+np.abs(K2) <= m)
    sph_o = np.zeros(I2.shape, bool)
    for (ci, cj, ck) in [(m, 0, 0), (-m, 0, 0), (0, m, 0), (0, -m, 0), (0, 0, m), (0, 0, -m)]:
        sph_o |= (I2-ci)**2 + (J2-cj)**2 + (K2-ck)**2 < R2
    # tetrahedral chamber, box [-1, m+1]^3
    kk = np.arange(-1, m+2)
    I3, J3, K3 = np.meshgrid(kk, kk, kk, indexing='ij')
    poly_t = (I3 <= J3+K3) & (J3 <= I3+K3) & (K3 <= I3+J3) & (I3+J3+K3 <= 2*m)
    sph_t = np.zeros(I3.shape, bool)
    for (ci, cj, ck) in [(0, 0, 0), (m, m, 0), (m, 0, m), (0, m, m)]:
        sph_t |= (I3-ci)**2 + (J3-cj)**2 + (K3-ck)**2 < R2
    return h, dict(
        ball=(ball, ~ball, True),
        network=(~insph, insph, True),
        oct=(poly_o & ~sph_o, sph_o, False),
        tet=(poly_t & ~sph_t, sph_t, False))

Ns = [48, 64, 96]
results = {k: {} for k in ['ball', 'network', 'oct', 'tet']}
hs = {}
for N in Ns:
    h, doms = domains(N)
    hs[N] = h
    for name, (dom, dmask, per) in doms.items():
        t0 = time.time()
        A, nd = build(dom, dmask, per, h)
        lam, res, nsol = lowest(A)
        results[name][N] = lam
        P("C %-8s N=%3d  h=%.6f  unknowns=%8d  lam=%.10f  resid=%.2e  (inner solves %d, %.1fs)"
          % (name, N, h, nd, lam, res, nsol, time.time()-t0))

def rich(d):
    l64, l96 = d[64], d[96]
    return l96 + (l96 - l64)*hs[96]/(hs[64] - hs[96])

P("")
ext = {}
for name in results:
    ext[name] = rich(results[name])
    P("C %-8s raw: %s  extrapolated: %.10f" % (name, "  ".join("%.10f" % results[name][N] for N in Ns), ext[name]))
P("C ball target 4pi^2 = %.10f ; rel error of extrapolation = %.3e" % (4*np.pi**2, ext['ball']/(4*np.pi**2) - 1))

# ---------------------------------------------------------------- B. x values
P("")
P("=== B. x VALUES ===")
S_EW = mp.pi**5/12
S_QCD = mp.pi**5/24
rt = ev(r_tet); ro = ev(r_oct)
alpha0 = ro*rt/mp.pi
NLO = alpha0*(4*mp.pi+1)/mp.pi**2
nnlo = 1 - NLO*(1-8*alpha0)/4
P("alpha0 = %s   NLO = %s   NNLO factor = %s" % (f10(alpha0), f10(NLO), f10(nnlo)))
def xEW(mu, V): return mu*V/S_EW*(1+NLO)
def xSU3_noNNLO(mu, V): return 2*mu*V/S_QCD*(1-NLO)
def xSU3(mu, V): return xSU3_noNNLO(mu, V)*nnlo
cases = [
    ("(i)   mu=pi^2/r^2, V=ball",    ev(mub_oct), ev(Vb_oct), ev(mub_tet), ev(Vb_tet)),
    ("(ii)  mu=pi^2/r^2, V=chamber", ev(mub_oct), ev(V_oct),  ev(mub_tet), ev(V_tet)),
    ("(iii) mu=FD extrap, V=chamber", mp.mpf(ext['oct']), ev(V_oct), mp.mpf(ext['tet']), ev(V_tet)),
]
for lab, muo, Vo, mut, Vt in cases:
    P("%s: mu_oct=%s V_oct=%s mu_tet=%s V_tet=%s" % (lab, f10(muo), f10(Vo), f10(mut), f10(Vt)))
    P("    x_EW  = %s" % f10(xEW(muo, Vo)))
    P("    x_SU3 = %s   (without NNLO factor: %s)" % (f10(xSU3(mut, Vt)), f10(xSU3_noNNLO(mut, Vt))))

open("/tmp/claude-0/-home-claude/167c2ecd-27e9-5de8-9853-57d4f91688cb/scratchpad/indep/report.txt", "w").write("\n".join(out)+"\n")
