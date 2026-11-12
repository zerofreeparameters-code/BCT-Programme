"""Gate DL-BETA -- write dlb_numbers.txt (card 4.6): every Q3 number, from out/state.json only.
Nothing from section 6 is computed here.  Usage: python3 -I make_numbers.py OUTDIR"""
import sys, os, json, math, hashlib

OUT = sys.argv[1]
st = json.load(open(os.path.join(OUT, "state.json")))
assert st.get("DONE") or "HALT" in st, "stages not finished"
L = []
w = L.append
f4 = lambda b: f"{b:.4f}"
w("Gate DL-BETA -- Q3 numbers (card 4.6), card convention beta = coefficient of sum over loops.")
w("Exact grid values in brackets where 4-decimal rounding (card 4.7) loses digits.")
w(f"beta0 (L = 2, Lt = 6; C maximum, larger of hot and cold) = {f4(st['S1']['beta0'])}   [{st['S1']['beta0']}] "
  f"(scan range {st['S1']['range']}, C = {st['S1']['Cmax']:.4f}, {st['S1']['beta0_start']} start)")
s2 = st["S2"]
w(f"beta4 (L = 4, Lt = 12; C maximum) = {f4(s2['beta4'])}   [{s2['beta4']}] (scan range {s2['range']}, C = {s2['Cmax']:.4f}, {s2['beta4_start']} start)")
w(f"jump interval L = 4 hot  = [{f4(s2['jump_hot'][0])}, {f4(s2['jump_hot'][1])}]  E {s2['ends_hot'][0]:.5f} -> {s2['ends_hot'][1]:.5f}, fall {s2['fall_hot']:.5f}")
w(f"jump interval L = 4 cold = [{f4(s2['jump_cold'][0])}, {f4(s2['jump_cold'][1])}]  E {s2['ends_cold'][0]:.5f} -> {s2['ends_cold'][1]:.5f}, fall {s2['fall_cold']:.5f}")
s3 = st["S3"]
w(f"jump interval L = 6 cold = [{f4(s3['jump'][0])}, {f4(s3['jump'][1])}]  E {s3['ends'][0]:.5f} -> {s3['ends'][1]:.5f}, fall {s3['fall']:.5f}")
w(f"E* = {s3['Estar']:.5f}")
for key, Lx in (("S4_L6", 6), ("S4_L8", 8)):
    if key not in st:
        w(f"beta_mix({Lx}): not reached")
        continue
    m = st[key]
    bm = m["beta_mix"]
    outs = ", ".join(f"{r['beta']}:{r['outcome'][0].upper()}" for r in m["rows"])
    if bm is None:
        w(f"beta_mix({Lx}): NO FLIP after {m['extensions']} extensions; outcomes {outs}")
    else:
        w(f"beta_mix({Lx}) = {f4(bm['beta_mix'])}   [{bm['beta_mix']}]  interval [{bm['interval'][0]}, {bm['interval'][1]}]"
          f"  monotonic {bm['monotonic']}, unresolved points {bm['unresolved_all']}, extensions {m['extensions']}")
        w(f"    outcomes (S strong, W weak, U unresolved): {outs}")
s5 = st.get("S5", {})
if s5:
    w(f"beta_inf = beta_mix(8) = {f4(s5['beta_inf'])}   [{s5['beta_inf']}]")
    w(f"uncertainty = max(half L=8 flip interval {s5['half_flip8']:.5f}, |beta_mix(8) - beta_mix(6)| {s5['shift_6_8']:.5f}) = {s5['unc']:.5f}")
    w(f"1/e^2_c = beta_inf/sqrt2 = {s5['inv_e2c']:.4f} +- {s5['inv_e2c_unc']:.4f}   [{s5['inv_e2c']:.7f} +- {s5['inv_e2c_unc']:.7f}]")
    dE = s5["dE"]
    w(f"Delta E(L = 8) = {dE:.5f} (runs at {s5['dE_runs'][0]} strong, {s5['dE_runs'][1]} weak; last-10-reading means); "
      f"final-sweep values: {s5['dE_final']:.5f}" if dE is not None else "Delta E(L = 8): not defined (no strong-win run below or weak-win run above beta_inf)")
    w(f"check (not headline): line through (1/(L^3 Lt), beta_mix(L)), L = 6, 8, at 0: {s5['lin_extrap_0']:.5f}")
if "HALT" in st:
    w(f"HALT: {st['HALT']}")
txt = "\n".join(L) + "\n"
p = os.path.join(OUT, "dlb_numbers.txt")
open(p, "w").write(txt)
print(txt)
print("SHA-256", hashlib.sha256(txt.encode()).hexdigest())
