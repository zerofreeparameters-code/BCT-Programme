"""Gate DL-BETA -- post-hash observations (NOT verdict inputs): where the unresolved mixed runs sit
relative to the pure branches, and what the step-6 histogram run does.  Usage: python3 -I post_obs.py OUTDIR"""
import sys, os, json
import numpy as np
OUT = sys.argv[1]
st = json.load(open(os.path.join(OUT, "state.json")))
o = []; w = o.append
t3 = st["S3"]["table"]
bs = sorted(float(b) for b in t3)
E = {b: t3[str(b) if str(b) in t3 else repr(b)]["cold"]["E"] for b in bs}
sb = [b for b in bs if b <= 1.25]; wb = [b for b in bs if b >= 1.26]
ps = np.polyfit(sb, [E[b] for b in sb], 1); pw = np.polyfit(wb, [E[b] for b in wb], 1)
w(f"Branch fits to the L = 6 cold scan (linear): strong (1.23-1.25) E = {ps[1]:.4f} {ps[0]:+.4f} beta;"
  f" weak (1.26-1.27) E = {pw[1]:.4f} {pw[0]:+.4f} beta")
w(f"Gap between the extrapolated branches at 1.2525: {np.polyval(ps,1.2525)-np.polyval(pw,1.2525):.4f}")
for key in ("S4_L6", "S4_L8"):
    w(f"\n{key}: E* = {st[key]['Estar']:.5f}")
    w("  beta     outcome     E(1550-2000)  strong-branch  weak-branch  fraction toward weak  min/max of readings 250-2000")
    for r in st[key]["rows"]:
        es, ew = np.polyval(ps, r["beta"]), np.polyval(pw, r["beta"])
        f = (es - r["E_last10"]) / (es - ew)
        rd = r["readings"][4:]
        w(f"  {r['beta']:.5f} {r['outcome']:<11s} {r['E_last10']:.5f}       {es:.5f}        {ew:.5f}      {f:5.2f}"
          f"                 {min(rd):.4f} / {max(rd):.4f}")
s6 = st["S6"]
z = np.load(os.path.join(OUT, "raw", "S6_hist", "void_L6_b1.25375_hist.npz"))
x = z["E"][2000:]
es, ew = np.polyval(ps, s6["beta"]), np.polyval(pw, s6["beta"])
w(f"\nS6 histogram run (L = 6, beta = {s6['beta']}, 20,000 measurement sweeps): mean E {x.mean():.5f}, sd {x.std():.5f};"
  f" strong branch {es:.5f}, weak branch {ew:.5f}, E* {st['S3']['Estar']:.5f}")
blk = x.reshape(40, 500).mean(1)
w("  500-sweep block means: " + " ".join(f"{v:.4f}" for v in blk))
h = np.array(s6["counts"]); ed = np.array(s6["edges"])
w(f"  histogram range [{ed[0]:.4f}, {ed[-1]:.4f}], peak bin {int(np.argmax(h))} at E = {(ed[np.argmax(h)]+ed[np.argmax(h)+1])/2:.4f}")
w("  counts: " + " ".join(str(c) for c in h))
ac = [np.corrcoef(x[:-k], x[k:])[0, 1] for k in (1, 10, 100, 500, 1000, 2000)]
w("  autocorrelation of E at lags 1, 10, 100, 500, 1000, 2000: " + " ".join(f"{a:.3f}" for a in ac))
open(os.path.join(OUT, "post_obs.txt"), "w").write("\n".join(o) + "\n")
print("\n".join(o))

# quadratic strong branch (curvature near the jump), same L = 6 cold points 1.23-1.25
pq = np.polyfit(sb, [E[b] for b in sb], 2)
w(f"\nQuadratic strong-branch fit (L = 6 cold, 1.23-1.25): E = {pq[2]:.4f} {pq[1]:+.4f} b {pq[0]:+.4f} b^2;"
  f" residuals at the fit points: " + " ".join(f"{E[b]-np.polyval(pq,b):+.5f}" for b in sb))
for key in ("S4_L6", "S4_L8"):
    w(f"  {key}: E(1550-2000) minus quadratic strong branch / minus linear weak branch:")
    for r in st[key]["rows"]:
        w(f"    {r['beta']:.5f} {r['outcome']:<11s} {r['E_last10']-np.polyval(pq, r['beta']):+.5f} / {r['E_last10']-np.polyval(pw, r['beta']):+.5f}")
w(f"  S6 histogram run mean minus quadratic strong branch at {s6['beta']}: {x.mean()-np.polyval(pq, s6['beta']):+.5f}")
w(f"  block-error scale of a single L = 6 cold-scan point: ~0.0003; of the strong-side mixed readings: sd of the 10 readings ~0.002")
open(os.path.join(OUT, "post_obs.txt"), "w").write("\n".join(o) + "\n")
print("\n".join(o[-20:]))
