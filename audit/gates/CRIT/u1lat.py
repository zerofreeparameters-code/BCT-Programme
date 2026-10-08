"""Compact U(1) lattice gauge theory, Wilson action, heat-bath Monte Carlo.

Two geometries on an L^4 periodic integer array:
  'hc' : hypercubic lattice, square plaquettes (validation; known beta_c = 1.0111)
  'd4' : D4 (= F4, body-centred hypercubic) lattice, triangular plaquettes.
         Links are the 24 roots (+-1,+-1,0,0). The integer array then holds two
         decoupled copies (even and odd coordinate sum); L must be even.
  'a4' : A4 root ("simplicial") lattice, triangular plaquettes (validation; published
         transition near beta = 0.85, Drouffe, Moriarty and Mouhas 1984). Integer
         coordinates n_k on the basis b_k = e_k - e_5; links are u_i and u_i - u_j.

Action:  S = beta * sum_plaquettes (1 - cos theta_p).
"""
import itertools
import numpy as np

AX = (0, 1, 2, 3)


def at(a, v):
    """Field a evaluated at x+v."""
    return np.roll(a, tuple(-int(c) for c in v), axis=AX)


class Lattice:
    def __init__(self, kind, L, seed):
        self.kind, self.L = kind, L
        self.rng = np.random.default_rng(seed)
        if kind == 'hc':
            self.dirs = [np.eye(4, dtype=int)[m] for m in range(4)]
        elif kind == 'd4':
            assert L % 2 == 0
            ds = []
            for i, j in itertools.combinations(range(4), 2):
                for sj in (1, -1):
                    v = np.zeros(4, dtype=int); v[i] = 1; v[j] = sj
                    ds.append(v)
            self.dirs = ds                       # 12 positive roots
        elif kind == 'a4':
            I = np.eye(4, dtype=int)
            self.dirs = [I[i] for i in range(4)] + [I[i] - I[j] for i, j in itertools.combinations(range(4), 2)]
        else:
            raise ValueError(kind)
        self.nd = len(self.dirs)
        self.index = {}
        for k, d in enumerate(self.dirs):
            self.index[tuple(d)] = (k, +1)
            self.index[tuple(-d)] = (k, -1)
        self.theta = np.zeros((self.nd,) + (L,) * 4)
        # staple paths: for each direction k, list of step-sequences going x -> x+d_k
        self.paths = []
        for k, d in enumerate(self.dirs):
            ps = []
            if kind == 'hc':
                for n, e in enumerate(self.dirs):
                    if n == k: continue
                    for s in (e, -e):
                        ps.append([s, d, -s])
            else:
                for s in list(self.index):
                    s = np.array(s)
                    if tuple(d - s) in self.index:
                        ps.append([s, d - s])
            self.paths.append(ps)
        # plaquette list (each once) for measurement: (steps) closed loops
        self.plaqs = []
        if kind == 'hc':
            for m, n in itertools.combinations(range(4), 2):
                a, b = self.dirs[m], self.dirs[n]
                self.plaqs.append([a, b, -a, -b])
        else:
            seen = set()
            roots = [np.array(r) for r in self.index]
            for r1 in roots:
                for r2 in roots:
                    r3 = r1 + r2
                    if tuple(r3) not in self.index: continue
                    # triangle 0 -> r1 -> r3 -> 0 ; canonical key = sorted vertex set
                    # count each triangle once per site-translation class: require 0 be the
                    # lexicographically smallest vertex
                    verts = [(0, 0, 0, 0), tuple(r1), tuple(r3)]
                    if min(verts) != (0, 0, 0, 0): continue
                    key = frozenset(verts)
                    if key in seen: continue
                    seen.add(key)
                    self.plaqs.append([r1, r2, -r3])
        self.npl = len(self.plaqs)               # plaquettes per site
        par = np.indices((L,) * 4).sum(axis=0) % 2
        self.par = [par == 0, par == 1]

    def link(self, step, off):
        """Angle of the oriented link from x+off to x+off+step."""
        k, sg = self.index[tuple(int(c) for c in step)]
        if sg > 0:
            return at(self.theta[k], off)
        return -at(self.theta[k], np.array(off) + np.array(step))

    def path_angle(self, steps):
        off = np.zeros(4, dtype=int); tot = 0.0
        for s in steps:
            tot = tot + self.link(s, off); off = off + np.array(s)
        return tot

    def staple(self, k):
        W = 0.0
        for p in self.paths[k]:
            W = W + np.exp(1j * self.path_angle(p))
        return W

    def sweep(self, beta):
        for k in range(self.nd):
            groups = self.par if self.kind == 'hc' else [None]
            for g in groups:
                W = self.staple(k)
                new = self.rng.vonmises(np.angle(W), beta * np.abs(W) + 1e-300)
                if g is None:
                    self.theta[k] = new
                else:
                    self.theta[k][g] = new[g]

    def energy(self):
        """Mean of (1 - cos theta_p) over all plaquettes."""
        e = 0.0
        for p in self.plaqs:
            e += np.mean(1.0 - np.cos(self.path_angle(p)))
        return e / self.npl

    def gauge_transform(self):
        lam = self.rng.uniform(-np.pi, np.pi, (self.L,) * 4)
        for k, d in enumerate(self.dirs):
            self.theta[k] += lam - at(lam, d)

    def hot(self):
        self.theta = self.rng.uniform(-np.pi, np.pi, self.theta.shape)

    def cold(self):
        self.theta[:] = 0.0


def naive_k(kind):
    """Geometry constant k with 1/e^2 = k*beta in the classical continuum limit."""
    lat = Lattice(kind, 2, 0)
    F = np.zeros((4, 4)); F[0, 1] = 1.0; F[1, 0] = -1.0
    # rows of M: integer basis vectors in orthonormal coordinates
    M = np.linalg.cholesky(np.eye(4) + 1.0) if kind == 'a4' else np.eye(4)
    tot = 0.0
    for p in lat.plaqs:
        a, b = p[0] @ M, p[1] @ M
        flux = a @ F @ b if kind == 'hc' else 0.5 * (a @ F @ b)
        tot += flux ** 2
    # sites per unit volume (d4: one of the two copies in the integer array)
    dens = {'hc': 1.0, 'd4': 0.5, 'a4': 1.0 / abs(np.linalg.det(M))}[kind]
    # (beta/2) * dens * tot * F12^2  ==  (1/(2 e^2)) * F12^2
    return dens * tot


if __name__ == '__main__':
    for kind in ('hc', 'd4', 'a4'):
        lat = Lattice(kind, 4, 1)
        print(kind, 'dirs', lat.nd, 'staples/link', len(lat.paths[0]), 'plaq/site', lat.npl,
              'k', naive_k(kind))
        lat.hot(); e0 = lat.energy(); lat.gauge_transform(); e1 = lat.energy()
        print('  gauge invariance:', abs(e0 - e1))
