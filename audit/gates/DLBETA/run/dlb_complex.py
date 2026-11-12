"""Gate DL-BETA -- cell complexes, written in the run thread from card section 4.2 only.

Void network (space): conventional FCC cube a = 1, integer coordinates in units of a/4, periodic
box of side M = 4L.  Atoms at 4(i,j,k) + {(0,0,0),(2,2,0),(2,0,2),(0,2,2)}; one atom per primitive
cell, so N = 4 L^3 cells.  Octahedral voids at atom + (2,2,2); tetrahedral voids at atom + (1,1,1)
and atom + (3,3,3), all mod M.

  node index   : oct of cell c -> c ; tet1 (atom+(1,1,1)) of cell c -> N + c ; tet2 -> 2N + c
  spatial link : one per oct-tet pair at offset d in {+-1}^3, oriented oct -> tet.
                 index = 8*c + OFFIDX(d), c = the oct's cell, OFFIDX(d) = 4[d0>0] + 2[d1>0] + [d2>0]
  rhombus      : for atom A and bond b in BONDS: octs A+o (|o-b|^2 = 4), tets A+t (|t-b|^2 = 3),
                 cyclic order O1 -> T1 -> O2 -> T2 -> O1 (O's in OCT_O order, T's in OFFSETS order).
                 links [O1T1, O2T1, O2T2, O1T2], signs [+1, -1, +1, -1].
                 index = 6*c + bond index.

Space x time (L_t slices, periodic):
  node (v, t)       -> t*3N + v
  link storage order (FIXED; this is also the heat-bath sweep order):
       slice-major; inside slice t: the 8N spatial links (index t*11N + s, s as above), then the 3N
       temporal links (v,t) -> (v,t+1) (index t*11N + 8N + v).
  loops: slice-major; inside slice t: the 6N rhombi (t*14N + r), then the 8N temporal squares
       (t*14N + 6N + s), square of spatial link s = u -> w:
       u(t) -> w(t) -> w(t+1) -> u(t+1) -> u(t): links [S(s,t), T(w,t), S(s,t+1), T(u,t)],
       signs [+1, +1, -1, -1].
  loop type: 0 = rhombus (spatial), 1 = temporal square.

Z4 (calibration): L^4 sites x = ((x0 L + x1) L + x2) L + x3; link (x, mu) -> 4x + mu (storage and
sweep order); plaquette (x, mu<nu) -> 6x + pair index, links [(x,mu)+, (x+mu,nu)+, (x+nu,mu)-,
(x,nu)-].  Direction 0 is called "time" for the E_s / E_t split (type 1 if mu = 0).
"""
import numpy as np
from itertools import product

ATOM_BASIS = np.array([(0, 0, 0), (2, 2, 0), (2, 0, 2), (0, 2, 2)], dtype=np.int64)
OFFSETS = np.array(list(product((-1, 1), repeat=3)), dtype=np.int64)       # 8 oct->tet offsets
BONDS = np.array([(2, 2, 0), (2, -2, 0), (2, 0, 2), (2, 0, -2), (0, 2, 2), (0, 2, -2)], dtype=np.int64)
OCT_O = np.array([(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)], dtype=np.int64)


def offidx(d):
    d = np.asarray(d)
    return 4 * (d[..., 0] > 0) + 2 * (d[..., 1] > 0) + (d[..., 2] > 0)


assert all(offidx(OFFSETS[i]) == i for i in range(8))


def _rhombus_template():
    """For each of the 6 bonds: (o1, t1, o2, t2) relative to the atom."""
    out = []
    for b in BONDS:
        os_ = [o for o in OCT_O if int(((o - b) ** 2).sum()) == 4]
        ts_ = [t for t in OFFSETS if int(((t - b) ** 2).sum()) == 3]
        assert len(os_) == 2 and len(ts_) == 2, (b, os_, ts_)
        out.append((os_[0], ts_[0], os_[1], ts_[1]))
    return out


RHOMB_T = _rhombus_template()


class VoidSpace:
    def __init__(self, L):
        self.L = L
        M = self.M = 4 * L
        N = self.N = 4 * L ** 3
        ijk = np.array(list(product(range(L), repeat=3)), dtype=np.int64)
        atoms = (4 * ijk[:, None, :] + ATOM_BASIS[None, :, :]).reshape(-1, 3)   # cell c
        self.atoms = atoms
        octs = (atoms + 2) % M
        tet1 = (atoms + 1) % M
        tet2 = (atoms + 3) % M
        pos = np.vstack([octs, tet1, tet2])
        self.pos = pos
        self.kind = np.repeat(np.arange(3), N)          # 0 oct, 1 tet1, 2 tet2
        lookup = -np.ones((M, M, M), dtype=np.int64)
        lookup[pos[:, 0], pos[:, 1], pos[:, 2]] = np.arange(3 * N)
        assert (lookup >= 0).sum() == 3 * N, "duplicate void positions"
        assert (lookup[atoms[:, 0], atoms[:, 1], atoms[:, 2]] < 0).all(), "void on an atom"
        self.lookup = lookup
        self.nv = 3 * N
        # spatial links
        tgtpos = (octs[:, None, :] + OFFSETS[None, :, :]) % M
        tnode = lookup[tgtpos[..., 0], tgtpos[..., 1], tgtpos[..., 2]]
        assert (tnode >= N).all(), "oct neighbour at (+-1)^3 is not a tet"
        self.ne = 8 * N
        self.link_org = np.repeat(np.arange(N), 8)
        self.link_tgt = tnode.ravel()
        self.link_vec = np.tile(OFFSETS, (N, 1))          # tgt - org, unwrapped, units a/4
        # rhombi
        nr = 6 * N
        rl = np.zeros((nr, 4), dtype=np.int64)
        rv = np.zeros((nr, 4, 3), dtype=np.int64)        # unwrapped vertices O1,T1,O2,T2
        self.rhomb_atom = np.repeat(np.arange(N), 6)
        self.rhomb_bond = np.tile(np.arange(6), N)
        for bi, (o1, t1, o2, t2) in enumerate(RHOMB_T):
            O1 = lookup[tuple(((atoms + o1) % M).T)]
            O2 = lookup[tuple(((atoms + o2) % M).T)]
            assert (O1 < N).all() and (O2 < N).all()
            sl = slice(bi, nr, 6)
            rl[sl, 0] = 8 * O1 + offidx(t1 - o1)
            rl[sl, 1] = 8 * O2 + offidx(t1 - o2)
            rl[sl, 2] = 8 * O2 + offidx(t2 - o2)
            rl[sl, 3] = 8 * O1 + offidx(t2 - o1)
            for k, vtx in enumerate((o1, t1, o2, t2)):
                rv[sl, k, :] = atoms + vtx
        self.rhomb_links = rl
        self.rhomb_signs = np.tile(np.array([1, -1, 1, -1], dtype=np.int64), (nr, 1))
        self.rhomb_verts = rv
        self.nr = nr
        # consistency: the links named really join the vertices named
        T1 = lookup[tuple((rv[:, 1] % M).T)]
        T2 = lookup[tuple((rv[:, 3] % M).T)]
        assert (self.link_tgt[rl[:, 0]] == T1).all() and (self.link_tgt[rl[:, 1]] == T1).all()
        assert (self.link_tgt[rl[:, 2]] == T2).all() and (self.link_tgt[rl[:, 3]] == T2).all()


class VoidST:
    """Void network x time.  See module docstring for index conventions."""

    def __init__(self, L, Lt):
        sp = self.sp = VoidSpace(L)
        self.L, self.Lt = L, Lt
        N = self.N = sp.N
        nv1, ns1, nt1 = 3 * N, 8 * N, 3 * N
        blk = self.blk = ns1 + nt1                       # 11 N links per slice
        lblk = self.lblk = 6 * N + 8 * N                 # 14 N loops per slice
        self.n_nodes = nv1 * Lt
        self.n_links = blk * Lt
        self.n_loops = lblk * Lt
        t = np.arange(Lt)
        # link origin / target nodes, and per-link slice and class
        org = np.zeros(self.n_links, dtype=np.int64)
        tgt = np.zeros(self.n_links, dtype=np.int64)
        lcls = np.zeros(self.n_links, dtype=np.int64)
        lslice = np.repeat(t, blk)
        for tt in range(Lt):
            b = tt * blk
            org[b:b + ns1] = tt * nv1 + sp.link_org
            tgt[b:b + ns1] = tt * nv1 + sp.link_tgt
            org[b + ns1:b + blk] = tt * nv1 + np.arange(nv1)
            tgt[b + ns1:b + blk] = ((tt + 1) % Lt) * nv1 + np.arange(nv1)
            lcls[b:b + ns1] = np.tile(np.arange(8), N)
            lcls[b + ns1:b + blk] = 8 + sp.kind
        self.link_org, self.link_tgt, self.link_cls, self.link_slice = org, tgt, lcls, lslice
        # loops
        LL = np.zeros((self.n_loops, 4), dtype=np.int64)
        LS = np.zeros((self.n_loops, 4), dtype=np.int64)
        LT = np.zeros(self.n_loops, dtype=np.int64)
        s_idx = np.arange(ns1)
        for tt in range(Lt):
            b, lb = tt * blk, tt * lblk
            t1 = ((tt + 1) % Lt) * blk
            LL[lb:lb + 6 * N] = b + sp.rhomb_links
            LS[lb:lb + 6 * N] = sp.rhomb_signs
            q = slice(lb + 6 * N, lb + lblk)
            LL[q, 0] = b + s_idx
            LL[q, 1] = b + ns1 + sp.link_tgt
            LL[q, 2] = t1 + s_idx
            LL[q, 3] = b + ns1 + sp.link_org
            LS[q] = np.array([1, 1, -1, -1])
            LT[q] = 1
        self.loop_links, self.loop_signs, self.loop_type = LL, LS, LT
        self.loop_slice = np.repeat(t, lblk)
        # loop translation class: rhombus -> bond (0..5), square -> 6 + offset class (0..7)
        lc = np.zeros(self.n_loops, dtype=np.int64)
        for tt in range(Lt):
            lb = tt * lblk
            lc[lb:lb + 6 * N] = np.tile(np.arange(6), N)
            lc[lb + 6 * N:lb + lblk] = 6 + np.tile(np.arange(8), N)
        self.loop_cls = lc

    def loop_vertices_4d(self, a_t):
        """Unwrapped 4D vertices (t, x, y, z) of every loop, spatial units of a (= 4 grid units)."""
        sp, N, Lt = self.sp, self.N, self.Lt
        V = np.zeros((self.n_loops, 4, 4))
        for tt in range(Lt):
            lb = tt * self.lblk
            rv = sp.rhomb_verts / 4.0
            V[lb:lb + 6 * N, :, 0] = tt * a_t
            V[lb:lb + 6 * N, :, 1:] = rv
            q = slice(lb + 6 * N, lb + self.lblk)
            u = sp.pos[sp.link_org] / 4.0
            w = u + sp.link_vec / 4.0
            V[q, 0, 0], V[q, 0, 1:] = tt * a_t, u
            V[q, 1, 0], V[q, 1, 1:] = tt * a_t, w
            V[q, 2, 0], V[q, 2, 1:] = (tt + 1) * a_t, w
            V[q, 3, 0], V[q, 3, 1:] = (tt + 1) * a_t, u
        return V

    def volume4(self, a_t):
        return float(self.L ** 3) * self.Lt * a_t      # conventional cube side a = 1


class Z4:
    def __init__(self, L):
        self.L = L
        n = self.n_sites = L ** 4
        x = np.array(list(product(range(L), repeat=4)), dtype=np.int64)
        self.x = x

        def idx(y):
            y = y % L
            return ((y[:, 0] * L + y[:, 1]) * L + y[:, 2]) * L + y[:, 3]

        assert (idx(x) == np.arange(n)).all()
        E = np.eye(4, dtype=np.int64)
        self.n_nodes = n
        self.n_links = 4 * n
        self.link_org = np.repeat(np.arange(n), 4)
        self.link_tgt = np.stack([idx(x + E[m]) for m in range(4)], axis=1).ravel()
        self.link_dir = np.tile(np.arange(4), n)
        pairs = [(m, v) for m in range(4) for v in range(m + 1, 4)]
        self.pairs = pairs
        LL = np.zeros((6 * n, 4), dtype=np.int64)
        LT = np.zeros(6 * n, dtype=np.int64)
        for p, (m, v) in enumerate(pairs):
            sl = slice(p, 6 * n, 6)
            LL[sl, 0] = 4 * np.arange(n) + m
            LL[sl, 1] = 4 * idx(x + E[m]) + v
            LL[sl, 2] = 4 * idx(x + E[v]) + m
            LL[sl, 3] = 4 * np.arange(n) + v
            LT[sl] = 1 if m == 0 else 0
        self.loop_links = LL
        self.loop_signs = np.tile(np.array([1, 1, -1, -1], dtype=np.int64), (6 * n, 1))
        self.loop_type = LT
        self.n_loops = 6 * n
        V = np.zeros((6 * n, 4, 4))
        for p, (m, v) in enumerate(pairs):
            sl = slice(p, 6 * n, 6)
            V[sl, 0] = x
            V[sl, 1] = x + E[m]
            V[sl, 2] = x + E[m] + E[v]
            V[sl, 3] = x + E[v]
        self._verts = V

    def loop_vertices_4d(self, a_t=1.0):
        V = self._verts.copy().astype(float)
        V[..., 0] *= a_t
        return V

    def volume4(self, a_t=1.0):
        return float(self.L ** 4) * a_t


def incidence_csr(n_links, loop_links, loop_signs):
    """For each link: the loops it lies in and its sign there (CSR)."""
    flat = loop_links.ravel()
    order = np.argsort(flat, kind="stable")
    counts = np.bincount(flat, minlength=n_links)
    ptr = np.zeros(n_links + 1, dtype=np.int64)
    ptr[1:] = np.cumsum(counts)
    loops = (order // 4).astype(np.int64)
    signs = loop_signs.ravel()[order].astype(np.float64)
    return ptr, loops, signs


def boundary2_dense(n_links, loop_links, loop_signs):
    D = np.zeros((len(loop_links), n_links))
    for k in range(4):
        np.add.at(D, (np.arange(len(loop_links)), loop_links[:, k]), loop_signs[:, k])
    return D
