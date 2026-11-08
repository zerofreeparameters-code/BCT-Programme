#!/usr/bin/env python3
"""
Desk-check VOID-HCP (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
Tie-breaker: FCC (BCT's lattice, stacking ABC) and HCP (stacking AB) are equally dense packings of
touching spheres. Does the void-network fluid of VOID-Q1 prefer one of them?

Key difference: in FCC every octahedral void opens only into tetrahedral voids (bipartite network);
in HCP the octahedral voids are stacked in columns along c and share faces (direct oct-oct windows).
Method as VOID-Q1: lowest states of -lap + V_wall in the pore space (spheres as walls), spectral
Hamiltonian on an orthorhombic HCP cell (a x sqrt3 a x c, 4 spheres, 4 octahedral voids), subspace
iteration + LOBPCG. Same grid spacing as the FCC runs (h ~ 0.022 a). Units hbar^2/2m = 1, a = 1.
FCC reference values (VOID-Q1, 64^3 cubic cell, h = 0.0221):
   wall 3000 : 127.22999, 127.23202 x3   wall 10000: 137.16159, 137.16205 x3
Run: python3 -I desk_VOID_hcp.py 3000 10000
"""
import sys, itertools, numpy as np
from scipy.sparse.linalg import LinearOperator, lobpcg

R = 0.5; c = np.sqrt(8 / 3)
L = np.array([1.0, np.sqrt(3), c])
spheres = np.array([[0, 0, 0], [0.5, np.sqrt(3) / 2, 0],
                    [0.5, np.sqrt(3) / 6, c / 2], [0.0, np.sqrt(3) / 6 + np.sqrt(3) / 2, c / 2]])
octs = np.array([[0, np.sqrt(3) / 3, c / 4], [0.5, np.sqrt(3) / 3 + np.sqrt(3) / 2, c / 4],
                 [0, np.sqrt(3) / 3, 3 * c / 4], [0.5, np.sqrt(3) / 3 + np.sqrt(3) / 2, 3 * c / 4]])
FCC = {3000.0: (127.22999, 127.23202), 10000.0: (137.16159, 137.16205)}
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78, flush=True)

def mind(d): return d - L * np.round(d / L)
hdr("Geometry check (HCP, nearest-neighbour distance 1 a)")
dd = [np.linalg.norm(mind(spheres[i] - spheres[j])) for i in range(4) for j in range(4) if i < j]
print(f"  sphere-sphere distances in the cell: {np.round(sorted(dd), 4)}")
for o in octs[:1]:
    ds = sorted(np.linalg.norm(mind(s + L * np.array(k) - o)) for s in spheres for k in itertools.product((-1, 0, 1), repeat=3))
    print(f"  octahedral void: 6 nearest spheres at {np.round(ds[:6], 4)} -> radius {ds[0] - R:.5f} a (FCC 0.20711)")
d_oo = np.linalg.norm(mind(octs[0] - octs[2]))
print(f"  octahedral voids stacked along c, centre spacing {d_oo:.4f} a: they share a triangular face (FCC: never)")

N = (45, 78, 74)
h = L / np.array(N)
print(f"  grid {N}, spacing {np.round(h, 4)}")
axes = [(np.arange(n) + 0.5) * hh for n, hh in zip(N, h)]
X, Y, Z = np.meshgrid(*axes, indexing='ij')
inside = np.zeros(X.shape, bool)
for s in spheres:
    for k in itertools.product((-1, 0, 1), repeat=3):
        cc = s + L * np.array(k)
        inside |= (X - cc[0]) ** 2 + (Y - cc[1]) ** 2 + (Z - cc[2]) ** 2 < R ** 2
print(f"  pore fraction {1 - inside.mean():.4f} (exact 0.2595, same as FCC)")
k = [2 * np.pi * np.fft.fftfreq(n, d=hh) for n, hh in zip(N, h)]
KX, KY, KZ = np.meshgrid(*k, indexing='ij'); K2 = KX ** 2 + KY ** 2 + KZ ** 2
n = X.size

def bands(Vw, nev=6, tau=4e-4, steps=700, seed=0):
    V = np.where(inside, Vw, 0.0)
    eV = np.exp(-tau * V / 2); eK = np.exp(-tau * K2)
    rng = np.random.default_rng(seed)
    B = rng.normal(size=(nev,) + X.shape) * (~inside)
    def orth(B):
        Q, _ = np.linalg.qr(B.reshape(nev, -1).T); return Q.T.reshape(B.shape)
    B = orth(B)
    for it in range(steps):
        B = eV * np.real(np.fft.ifftn(eK * np.fft.fftn(eV * B, axes=(1, 2, 3)), axes=(1, 2, 3)))
        if it % 10 == 9: B = orth(B)
    B = orth(B)
    Vf = V.ravel()
    def Hmv(v):
        v = np.asarray(v).reshape(X.shape + (-1,))
        out = np.real(np.fft.ifftn(K2[..., None] * np.fft.fftn(v, axes=(0, 1, 2)), axes=(0, 1, 2)))
        return out.reshape(n, -1) + Vf[:, None] * v.reshape(n, -1)
    def Pmv(v):
        v = np.asarray(v).reshape(X.shape + (-1,))
        return np.real(np.fft.ifftn(np.fft.fftn(v, axes=(0, 1, 2)) / (K2[..., None] + 300.0), axes=(0, 1, 2))).reshape(n, -1)
    Hop = LinearOperator((n, n), matvec=Hmv, matmat=Hmv, dtype=float)
    Pop = LinearOperator((n, n), matvec=Pmv, matmat=Pmv, dtype=float)
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        w, vecs = lobpcg(Hop, B.reshape(nev, -1).T, M=Pop, largest=False, tol=1e-7, maxiter=400)
    o = np.argsort(w); return w[o], vecs[:, o]

walls = [float(a) for a in sys.argv[1:]] or [3000.0]
res = {}
for Vw in walls:
    hdr(f"HCP, wall {Vw:.0f}")
    w, v = bands(Vw)
    res[Vw] = w
    print(f"  lowest levels: {np.round(w, 5)}")
    oct4 = w[:4]
    print(f"  octahedral band (4 states): centre {oct4.mean():.4f}, bottom {oct4[0]:.4f}, spread {np.ptp(oct4):.4f}")
    # chain picture: each column has 2 sites per cell along c; at the cell's zone centre a column gives
    # e - 2 t_c (bonding) and e + 2 t_c (antibonding): splitting 4 t_c
    pair_low, pair_high = oct4[:2].mean(), oct4[2:].mean()
    t_c = (pair_high - pair_low) / 4
    print(f"  column hopping t_c ~ (upper pair - lower pair)/4 = {t_c:.4f}")
    f_bot, f_x = FCC[Vw]
    f_centre = (f_bot + 3 * f_x) / 4; t_f = (f_x - f_bot) / 16
    print(f"  FCC (same wall): centre {f_centre:.4f}, bottom {f_bot:.4f}, hopping t = {t_f:.5f}")
    print(f"  per octahedral void, HCP - FCC:  band centre {oct4.mean() - f_centre:+.4f},  band bottom {oct4[0] - f_bot:+.4f}")
    print(f"  hopping ratio t_c(HCP column) / t(FCC) = {t_c / t_f:.0f}")

hdr("Reading")
gn0 = 1 / 2.31754 ** 2
for Vw, w in res.items():
    oct4 = w[:4]; t_c = (oct4[2:].mean() - oct4[:2].mean()) / 4
    f_bot, f_x = FCC[Vw]; f_centre = (f_bot + 3 * f_x) / 4
    print(f"  wall {Vw:.0f}: t_c = {t_c:.3f} vs g n0 = {gn0:.3f} -> in HCP the columns are "
          f"{'strongly' if t_c > 10 * gn0 else 'weakly'} coupled (U/t_c <= {gn0 / t_c:.3g})")
    print(f"    energy per void particle, HCP - FCC: band centre {oct4.mean() - f_centre:+.3f};"
          f" band bottom {oct4[0] - f_bot:+.3f}  (E0 ~ {f_centre:.0f})")
