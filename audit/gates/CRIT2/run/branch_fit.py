"""Section 9 observation (not a verdict input): pure-branch energies near the D4 flip.
Pooled fits over the L=8 hot, L=8 cold and L=12 cold scans: strong branch on 0.600-0.610,
weak branch on 0.615-0.625; linear and quadratic. Compared with the L=12 and L=16 mixed runs."""
import json
import numpy as np

OUT = "/root/crit2/out"


def load(tag):
    return [json.loads(l) for l in open(f"{OUT}/{tag}.jsonl")]


scans = load("s52") + load("s53")
mixed = {(r["L"], round(r["beta"], 6)): r for r in load("s54a") + load("s54b")}
branches = {
    "strong": [(r["beta"], r["E"]) for r in scans if 0.5995 < r["beta"] < 0.6105],
    "weak": [(r["beta"], r["E"]) for r in scans if 0.6145 < r["beta"] < 0.6255],
}
fits = {}
for nm, pts in branches.items():
    b = np.array([p[0] for p in pts]); e = np.array([p[1] for p in pts])
    fits[nm] = [np.polyfit(b, e, d) for d in (1, 2)]
    print(f"{nm} branch: {len(pts)} points, beta {b.min():.3f}-{b.max():.3f}")


def rng(nm, x):
    v = [np.polyval(c, x) for c in fits[nm]]
    return min(v), max(v)


for x in (0.6125, 0.61375, 0.615, 0.61625):
    s, w = rng("strong", x), rng("weak", x)
    print(f"beta={x:.5f}: strong {s[0]:.4f}-{s[1]:.4f}   weak {w[0]:.4f}-{w[1]:.4f}")
s, w = rng("strong", 0.615), rng("weak", 0.615)
print(f"gap at 0.615: {s[0]-w[1]:.4f}-{s[1]-w[0]:.4f}")
for L, x in ((12, 0.6125), (16, 0.61375)):
    r = mixed[(L, x)]; s = rng("strong", x)
    rd = np.array(r["readings"])
    print(f"L={L} beta={x}: E_last500={r['E_last500']:.4f}, below strong branch by "
          f"{s[0]-r['E_last500']:.4f}-{s[1]-r['E_last500']:.4f}; readings from sweep 50: "
          f"{rd.min():.3f}-{rd.max():.3f}")
s = rng("strong", 0.61375); w = rng("weak", 0.61625)
dE = mixed[(16, 0.61375)]["E_last500"] - mixed[(16, 0.61625)]["E_last500"]
print(f"pure-phase expectation for the two L=16 runs: {s[0]-w[1]:.4f}-{s[1]-w[0]:.4f}; "
      f"measured dE={dE:.4f}; shortfall {s[0]-w[1]-dE:.4f}-{s[1]-w[0]-dE:.4f}")
