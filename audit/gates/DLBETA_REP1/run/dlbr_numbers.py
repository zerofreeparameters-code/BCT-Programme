"""
Gate DL-BETA REP1 -- write dlbr_numbers.txt (REP1 section 4.7) from out/state.json. Written before any void
number existed. Usage: python -I dlbr_numbers.py OUTDIR
"""
import os, sys, json, math

OUT = sys.argv[1]
U = 1e7
st = json.load(open(os.path.join(OUT, "state.json")))


def b(n, d=4):
    if n is None:
        return "none"
    v = n / U
    s = f"{v:.{d}f}"
    ex = f"{v:.7f}".rstrip("0").rstrip(".")
    return s if abs(float(s) - v) < 1e-12 else f"{s} [{ex}]"


def e(x):
    return "none" if x is None else f"{x:.5f}"


L = []
w = L.append
w("# Gate DL-BETA REP1 -- dlbr_numbers.txt (all Q3 and Q6 numbers; written before unblinding)")
w("# beta in card convention (coefficient of sum over loops); 1/e^2 = beta/sqrt2. beta to 4 dp [exact grid value], E to 5 dp.")
w(f"K4_beta_Cmax = {b(st['K4']['beta_Cmax'])}")
w(f"K4_pass = {'yes' if st['K4']['pass_'] else 'no'}")
w(f"K4_Estar_hc = {e(st['K4']['Estar_hc'])}")
fl = st["K5"]["flip"]
w(f"K5_flip_interval = [{b(fl['lo'])}, {b(fl['hi'])}]" if fl["exists"] else "K5_flip_interval = none")
w(f"K5_pass = {'yes' if st['K5']['pass_'] else 'no'}")
w(f"beta_0 = {b(st['S1']['beta0'], 2)}")
w(f"beta_0_grid = [{b(st['S1']['grid'][0], 2)}, {b(st['S1']['grid'][-1], 2)}]; extensions = {st['S1']['extensions']}")
w(f"beta_4 = {b(st['S2']['beta4'], 3)}")
w(f"beta_4_grid = [{b(st['S2']['grid'][0], 3)}, {b(st['S2']['grid'][-1], 3)}]; extensions = {st['S2']['extensions']}")
for s in ("hot", "cold"):
    j = st["S2"]["jumps"][s]
    w(f"jump_interval_L4_{s} = [{b(j['interval'][0], 3)}, {b(j['interval'][1], 3)}]; fall = {e(j['fall'])}")
s3 = st["S3"]
w(f"L6_grid = [{b(s3['grid'][0], 3)}, {b(s3['grid'][-1], 3)}]; extensions = {s3['extensions']}")
w(f"jump_interval_L6_cold = [{b(s3['cold_jump'][0], 3)}, {b(s3['cold_jump'][1], 3)}]; fall = {e(s3['cold_fall'])}; 3sigma = {e(s3['cold_fall_threshold'])}")
w(f"jump_interval_L6_hot = [{b(s3['hot_jump'][0], 3)}, {b(s3['hot_jump'][1], 3)}]; fall = {e(s3['hot_fall'])}")
w(f"beta_lo = {b(s3['cold_jump'][0], 3)}")
w(f"beta_hi = {b(s3['cold_jump'][1], 3)}")
w(f"E_star = {e(s3['Estar'])}")
w(f"Located = {'yes' if s3['located'] else 'no'}")
for nm, key in (("S", "S_line"), ("W", "W_line")):
    ln = s3[key]
    pts = "; ".join(f"({b(p[0], 3)}, {e(p[1])})" for p in ln["points"])
    w(f"branch_{nm}: E = {ln['intercept0']:.6f} + ({ln['slope']:.6f}) * beta ; points {pts}")
for stage, Lx in (("S4a", 6), ("S4b", 8)):
    sx = st[stage]
    if Lx == 8 and not sx.get("run", True):
        w(f"mixed_L8: not run ({sx.get('reason')})")
        continue
    w(f"mixed_L{Lx}_grid = [{b(sx['grid'][0])}, {b(sx['grid'][-1])}] step 0.0025; centre = {b(sx['centre'])}; extensions = {sx['extensions']}")
    for r in sx["runs"]:
        f = "nan" if r["f"] != r["f"] else f"{r['f']:.6f}"
        w(f"mixed_L{Lx} beta = {b(r['bn'])} seed {r['seed']}: E_end = {e(r['E_end'])}; S = {e(r['S'])}; W = {e(r['W'])}; "
          f"f = {f}; primary = {r['primary']}{' (flagged S-W<=0)' if r['flagged'] else ''}; secondary = {r['secondary']}")
    fl = sx["flip"]
    if fl["exists"]:
        w(f"beta_mix({Lx}) = {b(round(fl['mid']))}; flip_interval = [{b(fl['lo'])}, {b(fl['hi'])}]; non_monotonic = {'yes' if fl['nonmono'] else 'no'}; "
          f"unresolved_inside = {fl['n_unres_inside']}; unresolved_total = {fl['n_unres_total']}")
    else:
        w(f"beta_mix({Lx}) = none (no primary flip); unresolved_total = {fl.get('n_unres_total')}")
    fs = sx["flip_secondary"]
    if fs["exists"]:
        w(f"Q6 beta_mix_sec({Lx}) = {b(round(fs['mid']))}; flip_interval_sec = [{b(fs['lo'])}, {b(fs['hi'])}]; non_monotonic = {'yes' if fs['nonmono'] else 'no'}; "
          f"unresolved_total_sec = {fs['n_unres_total']}")
    else:
        w(f"Q6 beta_mix_sec({Lx}) = none; unresolved_total_sec = {fs.get('n_unres_total')}")
fi = st["final"]
if fi.get("beta_inf") is not None:
    w(f"beta_inf = {b(round(fi['beta_inf']))}")
    w(f"uncertainty = {b(round(fi['u']))}")
    w(f"half_L8_flip_interval = {b(round(fi['half8']))}; |beta_mix(8)-beta_mix(6)| = {b(round(fi['d68']))}")
    w(f"inv_e2_c = {fi['inv_e2']:.4f} +- {fi['inv_e2_u']:.4f}")
    w(f"Delta_E_L8 = {e(fi['dE8'])} (strong run at {b(fi['dE8_below'])} minus weak run at {b(fi['dE8_above'])})")
    w(f"extrapolation_check_beta(1/(L^3 L_t)->0) = {fi['extrap0']/U:.5f}")
else:
    w("beta_inf = none")
    w("uncertainty = none")
w(f"Resolved = {'yes' if fi['resolved'] else 'no'}")
w(f"beta_R = {b(round(fi['betaR']))}")
w(f"histogram_beta = {b(st['S6']['bn'])} ({st['S6']['source']}); B = {st['S6']['B']:.6f}; two_peaks = {'yes' if st['S6']['two_peaks'] else 'no'}")
q6 = fi["Q6"]
w(f"Q6 beta_inf_sec = {b(round(q6['beta_inf_sec'])) if q6.get('beta_inf_sec') is not None else 'none'}")
w(f"Q6 u_sec = {b(round(q6['u_sec'])) if q6.get('u_sec') is not None else 'none'}")
w(f"Q6 unresolved_L8_sec = {q6['n_unres8_sec']}")
w(f"Q6 original_card_code = {q6['original_card_code']}")
txt = "\n".join(L) + "\n"
with open(os.path.join(OUT, "dlbr_numbers.txt"), "w") as f:
    f.write(txt)
print(txt)
