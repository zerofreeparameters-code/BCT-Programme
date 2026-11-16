#!/usr/bin/env python3
"""Step-2 double-extrapolation sweep for Gate BB-ALPHA.
For each sigma_i>0 (well-conditioned, no void null space), solve FCC touching
at several N (exact-pinned f), 1 direction. Writes one JSON line per solve.
Later analysis: extrapolate N->inf at each sigma_i, then sigma_i->0."""
import numpy as np, json, time, sys
import bbalpha_spectral as B

ft = np.pi/(3*np.sqrt(2))          # FCC touching solid fraction = 0.7404805
centers = B.fcc_centers()
sigis = [0.10, 0.05, 0.02]
Ns    = [48, 64, 96, 128]

out = open('/home/claude/work/sweep_out.jsonl', 'w')
for si in sigis:
    for N in Ns:
        t0 = time.time()
        sigma, fs = B.build_sphere_array(N, centers, f_target=ft, sigma_i=si)
        se, vals, iters, res = B.sigeff_iso(sigma, dirs=(0,), tol=1e-9,
                                            maxit=4000, sigma_ref=0.5, conv='res')
        phi = 1.0 - fs
        rec = {'sigma_i': si, 'N': N, 'f_solid': fs, 'phi': phi,
               'sigma_eff': se, 'alpha': phi/se, 'iters': iters[0],
               'res': res[0], 't': round(time.time()-t0, 1)}
        out.write(json.dumps(rec) + '\n'); out.flush()
        print(json.dumps(rec)); sys.stdout.flush()
out.close()
print("DONE")
