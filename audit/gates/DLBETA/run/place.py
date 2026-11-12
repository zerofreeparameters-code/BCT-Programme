"""Gate DL-BETA -- section 6 placement and section 9 forecast scoring.  Run ONLY after
dlb_numbers.txt is written and its SHA-256 recorded (card 4.6).  Usage: python3 -I place.py OUTDIR"""
import sys, os, json, math

OUT = sys.argv[1]
assert os.path.exists(os.path.join(OUT, "dlb_numbers.sha256")), "hash dlb_numbers.txt first (card 4.6)"
st = json.load(open(os.path.join(OUT, "state.json")))
s5 = st["S5"]
b, u = s5["beta_inf"], s5["unc"]
lo, hi = b - u, b + u
o = []
w = o.append
r2 = math.sqrt(2)

# 6.1
w("6.1 against the other lattices")
w("| lattice | β_c (card) | k | 1/e²_c | ratio of 1/e²_c to Z4 |")
w("|---|---|---|---|---|")
rows = [("Z4", 1.0111, None, 1.0, "Arnold et al.; K4/K5 here"), ("D4", 0.6150, 0.00125, 2.0, "CRIT2"),
        ("void x time", b, u, 1 / r2, "this gate")]
for name, bc, du, k, src in rows:
    e2 = k * bc
    w(f"| {name} | {bc:.4f}{' ± ' + format(du, '.5f') if du else ''} | {k:.6g} | {e2:.4f}"
      f"{' ± ' + format(k*du, '.5f') if du else ''} | {e2/1.0111:.4f} |")
w(f"beta_inf / beta_c(Z4) = {b/1.0111:.4f};  beta_inf / beta_c(D4) = {b/0.6150:.4f}")

# 6.2 and section 9 heuristics -- recomputed from their stated definitions
w("")
w("6.2 heuristics (hit iff [beta_inf - unc, beta_inf + unc] meets the interval)")
rank_per_loop = {"Z4": 3 / 6, "D4": 11 / 32, "void": 8 / 14}
th2 = {k: rank_per_loop[k] / v for k, v in (("Z4", 1.0111), ("D4", 0.6150))}
H1 = sorted(rank_per_loop["void"] / t for t in th2.values())
H2 = sorted(r2 * x for x in (1.0111, 1.2300))
lpl = {"Z4": 6, "D4": 8, "void": 56 / 11}
H3 = sorted(x / lpl["void"] for x in (1.0111 * 6, 0.6150 * 8))
card = {"H1": (1.0223, 1.1555), "H2": (1.4299, 1.7395), "H3": (0.9664, 1.1917)}
res62 = {}
for name, iv in (("H1", H1), ("H2", H2), ("H3", H3)):
    assert abs(iv[0] - card[name][0]) < 6e-5 and abs(iv[1] - card[name][1]) < 6e-5, (name, iv)
    hit = lo <= iv[1] and hi >= iv[0]
    dist = 0.0 if hit else (iv[0] - hi if hi < iv[0] else lo - iv[1])
    res62[name] = dict(interval=iv, hit=hit, distance=dist)
    w(f"  {name}: interval [{iv[0]:.4f}, {iv[1]:.4f}] (card [{card[name][0]}, {card[name][1]}])  ->  "
      f"{'HIT' if hit else 'MISS'}{'' if hit else f' by {dist:.4f}'}")
sc = (0.615, 1.011)
hit_sc = lo <= sc[1] and hi >= sc[0]
w(f"  scoping note §7 forecast [0.615, 1.011]: {'HIT' if hit_sc else 'MISS'}"
  f"{'' if hit_sc else f' (beta_inf - unc exceeds 1.011 by {lo - sc[1]:.4f})'}")
# implied infinite-volume <theta^2> and implied loops-per-link product, for the record
w(f"  implied (rank/N_loops)/beta_inf = {rank_per_loop['void']/b:.4f}  (Z4 {th2['Z4']:.4f}, D4 {th2['D4']:.4f})")
w(f"  implied 1/e^2_c = {b/r2:.4f}  (Z4 1.0111, D4 1.2300)")
w(f"  implied beta_inf x loops/link = {b*56/11:.4f}  (Z4 6.0666, D4 4.9200)")

# 6.3
w("")
w("6.3 the programme's candidate number, for orientation only (DL-STIFF card §1 convention, k = 1)")
bg = 10.742018
w(f"  beta_geom / beta_inf = {bg:.6f} / {b:.4f} = {bg/b:.3f}")
w(f"  15.191508 / beta_inf = {15.191508/b:.3f}    (15.191508 = sqrt2 x 10.742018 = {r2*bg:.6f})")
w(f"  a Wilson beta of 10.742018 on this complex means 1/e^2 = {bg/r2:.6f}")
json.dump(dict(H=res62, scoping_hit=hit_sc, ratio_geom=bg / b, ratio_15=15.191508 / b),
          open(os.path.join(OUT, "placement.json"), "w"), indent=1)
txt = "\n".join(o) + "\n"
open(os.path.join(OUT, "placement.txt"), "w").write(txt)
print(txt)
