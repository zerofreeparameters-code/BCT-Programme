#!/usr/bin/env python3
"""
Gate BUBBLE_BELLS Q1 — tortuosity of the FCC void network by OFF-LATTICE random walk (independent of the
finite-difference solve in bells_tortuosity.py).

Walkers diffuse in the void space between touching rigid spheres of radius R = a/2 on FCC (conventional cube
edge L = a√2, 4 spheres/cell, periodic images).  Steps are Gaussian with rms δ per axis; a step that would end
inside a sphere is specularly reflected off the sphere surface (one reflection; if still inside, the step is
rejected — rare for δ ≪ throat radius 0.077a).  Long-time ⟨|r(t) − r(0)|²⟩ = 6 D_w t with D_w = D0/α_∞
(Johnson–Koplik–Dashen tortuosity).  D0 = δ²/(2 dt) per axis with dt = 1 ⇒ D0 = δ²/2.
α_∞ is read from the slope of the MSD over the late half of the run (walkers have crossed many cells).
"""
import sys, time
import numpy as np

rng = np.random.default_rng(20261110)
L = np.sqrt(2.0)                                   # a = 1
R = 0.5
centres = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]) * L

def nearest_centre(p):
    """for positions p (n,3), return vector from nearest periodic sphere centre to p, and its length"""
    best_d2 = np.full(len(p), np.inf); best_v = np.zeros_like(p)
    for c in centres:
        v = p - c
        v -= L * np.round(v / L)                   # minimum image
        d2 = (v**2).sum(1)
        m = d2 < best_d2
        best_d2[m] = d2[m]; best_v[m] = v[m]
    return best_v, np.sqrt(best_d2)

def sample_void(n):
    out = np.empty((0, 3))
    while len(out) < n:
        p = rng.random((2 * n, 3)) * L
        _, d = nearest_centre(p)
        out = np.vstack([out, p[d > R]])
    return out[:n]

def run(n_walk=20000, n_steps=60000, delta=0.008):
    pos = sample_void(n_walk); start = pos.copy()
    D0 = delta**2 / 2
    msd_t = []; ts = []
    rejected = 0
    t0 = time.time()
    for step in range(1, n_steps + 1):
        new = pos + rng.normal(0.0, delta, pos.shape)
        v, d = nearest_centre(new)
        inside = d < R
        if inside.any():
            # specular reflection about the sphere surface: reflect the radial excess
            n_hat = v[inside] / d[inside, None]
            excess = (R - d[inside])
            cand = new[inside] + 2 * excess[:, None] * n_hat
            v2, d2 = nearest_centre(cand)
            ok = d2 >= R
            idx = np.where(inside)[0]
            new[idx[ok]] = cand[ok]
            new[idx[~ok]] = pos[idx[~ok]]           # reject
            rejected += (~ok).sum()
        pos = new
        if step % 1000 == 0:
            disp = pos - start
            msd_t.append((disp**2).sum(1).mean()); ts.append(step)
    ts = np.array(ts, float); msd = np.array(msd_t)
    # late-time slope (second half), least squares through the points
    half = len(ts) // 2
    A = np.vstack([ts[half:], np.ones(len(ts) - half)]).T
    slope, icpt = np.linalg.lstsq(A, msd[half:], rcond=None)[0]
    Dw = slope / 6
    alpha = D0 / Dw
    # statistical error from bootstrap over walkers is expensive; use split-half estimate
    return alpha, Dw, D0, rejected / (n_walk * n_steps), ts, msd, time.time() - t0

if __name__ == "__main__":
    n_walk = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    n_steps = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.008
    print(f"FCC void network, R = a/2, L = a√2; walkers = {n_walk}, steps = {n_steps}, δ = {delta} a (throat radius 0.0774 a)")
    phi = 1 - np.pi / (3 * np.sqrt(2))
    alpha, Dw, D0, rej, ts, msd, dt = run(n_walk, n_steps, delta)
    print(f"  rejection fraction = {rej:.2e};  D0 = {D0:.3e};  D_w = {Dw:.3e};  runtime {dt:.0f}s")
    print(f"  rms displacement at end = {np.sqrt(msd[-1]):.2f} a  ({np.sqrt(msd[-1])/L:.1f} cells)")
    print(f"  α_∞ (random walk) = {alpha:.3f}   ⇒ σ_eff/σ0 = φ/α_∞ = {phi/alpha:.4f},  c4/cs = {1/np.sqrt(alpha):.4f}")
    # convergence diagnostic: local slope in quarters
    q = len(ts) // 4
    for k in range(4):
        sl = np.polyfit(ts[k*q:(k+1)*q], msd[k*q:(k+1)*q], 1)[0] / 6
        print(f"    quarter {k+1}: α_∞(local) = {D0/sl:.3f}")
    print("  FD extrapolation for comparison: α_∞ = 1.64 ± 0.03 (bells_tortuosity.py)")
