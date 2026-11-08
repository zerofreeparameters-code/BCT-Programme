#!/usr/bin/env python3
"""
Desk-check VOID-HCP, part 2: matched-grid control (8 Nov 2026, same-session, CONJECTURE; NOT a gate).

Why: part 1 (desk_VOID_hcp.py) compared an HCP cell with the earlier FCC cubic cell. The two grids
sample the spheres at different sub-cell offsets. A shift of a few per cent of one grid step in the
effective sphere radius moves the octahedral level by ~1 unit, which is the size of the HCP-FCC gap
found there (+0.84). So part 1 cannot separate physics from staircase error.

Control: build BOTH packings as stacks of the same triangular layers, on the SAME grid:
  HCP = A B (2 layers per cell),  FCC = A B C (3 layers per cell), layer spacing sqrt(2/3) a.
Grid nodes sit exactly on every sphere centre (Nx even, Ny divisible by 6, same points per layer).
Then an octahedral cage between layers A and B is bit-identical in the two structures; only what lies
beyond its faces differs (HCP: two faces open into the next octahedral void; FCC: all eight faces open
into tetrahedral voids). Any HCP-FCC difference is then physics, not sampling.

Tight-binding reading: the mean of the octahedral states in the cell equals the on-site level e0
(nearest-neighbour hopping only; trace argument), so the means can be compared directly.
HCP cell: 4 octahedral voids (2 columns x 2). FCC cell: 6 octahedral voids.
Units hbar^2/2m = 1, a = 1 (nearest-neighbour distance). Spheres R = 0.5 as penalty walls.
Run: python3 -I desk_VOID_hcp2.py Nx Ny Nlayer wall [wall ...]
"""
import sys, itertools, warnings, numpy as np
from scipy.sparse.linalg import LinearOperator, lobpcg

R = 0.5; hl = np.sqrt(2 / 3); s3 = np.sqrt(3)
SITES = {'A': [(0.0, 0.0), (0.5, s3 / 2)],
         'B': [(0.5, s3 / 6), (0.0, 2 * s3 / 3)],
         'C': [(0.0, s3 / 3), (0.5, 5 * s3 / 6)]}
def third(x, y): return ({'A', 'B', 'C'} - {x, y}).pop()
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78, flush=True)

def build(stack, Nx, Ny, Nl):
    L = np.array([1.0, s3, hl * len(stack)])
    N = (Nx, Ny, Nl * len(stack))
    h = L / np.array(N)
    sph = [(x, y, i * hl) for i, lay in enumerate(stack) for (x, y) in SITES[lay]]
    octs = [(x, y, (i + 0.5) * hl) for i, lay in enumerate(stack)
            for (x, y) in SITES[third(lay, stack[(i + 1) % len(stack)])]]
    axes = [np.arange(n) * hh for n, hh in zip(N, h)]          # node-centred: spheres on nodes
    X, Y, Z = np.meshgrid(*axes, indexing='ij')
    inside = np.zeros(X.shape, bool)
    for s in sph:
        for k in itertools.product((-1, 0, 1), repeat=3):
            cc = np.array(s) + L * np.array(k)
            inside |= (X - cc[0]) ** 2 + (Y - cc[1]) ** 2 + (Z - cc[2]) ** 2 < R ** 2
    # check that every sphere centre is on a node
    off = max(np.max(np.abs(np.array(s) / h - np.round(np.array(s) / h))) for s in sph)
    kk = [2 * np.pi * np.fft.fftfreq(n, d=hh) for n, hh in zip(N, h)]
    KX, KY, KZ = np.meshgrid(*kk, indexing='ij')
    return dict(L=L, N=N, h=h, sph=np.array(sph), octs=np.array(octs), inside=inside,
                K2=KX ** 2 + KY ** 2 + KZ ** 2, off=off)

def bands(G, Vw, nev, tau=4e-4, steps=600, seed=0):
    inside, K2 = G['inside'], G['K2']; shp = inside.shape; n = inside.size
    V = np.where(inside, Vw, 0.0)
    eV = np.exp(-tau * V / 2); eK = np.exp(-tau * K2)
    rng = np.random.default_rng(seed)
    B = rng.normal(size=(nev,) + shp) * (~inside)
    def orth(B):
        Q, _ = np.linalg.qr(B.reshape(nev, -1).T); return Q.T.reshape(B.shape)
    B = orth(B)
    for it in range(steps):
        B = eV * np.real(np.fft.ifftn(eK * np.fft.fftn(eV * B, axes=(1, 2, 3)), axes=(1, 2, 3)))
        if it % 10 == 9: B = orth(B)
    B = orth(B); Vf = V.ravel()
    def Hmv(v):
        v = np.asarray(v).reshape(shp + (-1,))
        out = np.real(np.fft.ifftn(K2[..., None] * np.fft.fftn(v, axes=(0, 1, 2)), axes=(0, 1, 2)))
        return out.reshape(n, -1) + Vf[:, None] * v.reshape(n, -1)
    def Pmv(v):
        v = np.asarray(v).reshape(shp + (-1,))
        return np.real(np.fft.ifftn(np.fft.fftn(v, axes=(0, 1, 2)) / (K2[..., None] + 300.0),
                                    axes=(0, 1, 2))).reshape(n, -1)
    Hop = LinearOperator((n, n), matvec=Hmv, matmat=Hmv, dtype=float)
    Pop = LinearOperator((n, n), matvec=Pmv, matmat=Pmv, dtype=float)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        w, vecs = lobpcg(Hop, B.reshape(nev, -1).T, M=Pop, largest=False, tol=1e-7, maxiter=400)
    o = np.argsort(w); return w[o]

Nx, Ny, Nl = (int(a) for a in sys.argv[1:4])
walls = [float(a) for a in sys.argv[4:]] or [3000.0]
assert Nx % 2 == 0 and Ny % 6 == 0
hdr(f"Matched grid: Nx={Nx}, Ny={Ny}, {Nl} points per layer")
out = {}
for name, stack in (('HCP', 'AB'), ('FCC', 'ABC')):
    G = build(stack, Nx, Ny, Nl)
    no = len(G['octs'])
    print(f"  {name} ({stack}): grid {G['N']}, spacing {np.round(G['h'], 5)}, spheres {len(G['sph'])}, "
          f"octahedral voids {no}, max sphere-centre offset from a node {G['off']:.1e} steps, "
          f"pore fraction {1 - G['inside'].mean():.5f}", flush=True)
    for Vw in walls:
        w = bands(G, Vw, nev=no + 2)
        out[(name, Vw)] = (w, no)
        oc = w[:no]
        print(f"    wall {Vw:.0f}: levels {np.round(w, 5)}", flush=True)
        print(f"      octahedral states: mean (on-site e0) {oc.mean():.5f}, bottom {oc[0]:.5f}, "
              f"top {oc[-1]:.5f}, spread {np.ptp(oc):.5f}; gap to next {w[no] - oc[-1]:.2f}", flush=True)

hdr("HCP - FCC on the identical grid")
for Vw in walls:
    wh, nh = out[('HCP', Vw)]; wf, nf = out[('FCC', Vw)]
    oh, of = wh[:nh], wf[:nf]
    t_c = (oh[2:].mean() - oh[:2].mean()) / 4
    print(f"  wall {Vw:.0f}: on-site e0  HCP {oh.mean():.5f}  FCC {of.mean():.5f}  diff {oh.mean() - of.mean():+.5f}")
    print(f"              band bottom HCP {oh[0]:.5f}  FCC {of[0]:.5f}  diff {oh[0] - of[0]:+.5f}")
    print(f"              HCP column hopping t_c = {t_c:.5f};  FCC spread {np.ptp(of):.2e}")
