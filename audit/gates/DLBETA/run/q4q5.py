"""Gate DL-BETA -- Q4 (order diagnostics, card 4.4 step 7, readings R7-R9 of dlb_driver.py) and
Q5 (anisotropy record E_s, E_t).  Not verdict inputs.  Usage: python3 -I q4q5.py OUTDIR"""
import sys, os, json, math

OUT = sys.argv[1]
st = json.load(open(os.path.join(OUT, "state.json")))
o = []
w = o.append
res = {}

# (a) hysteresis at L = 4
s2 = st["S2"]
t2 = s2["table"]
diff_iv = s2["jump_hot"] != s2["jump_cold"]
worst = max(((abs(t2[b]["hot"]["E"] - t2[b]["cold"]["E"]) /
              math.sqrt(t2[b]["hot"]["E_err"] ** 2 + t2[b]["cold"]["E_err"] ** 2), float(b)) for b in t2))
a = diff_iv or worst[0] > 3
res["a"] = dict(jump_hot=s2["jump_hot"], jump_cold=s2["jump_cold"], intervals_differ=diff_iv,
                max_hot_cold_sigma=worst[0], at_beta=worst[1], holds=a)
w(f"(a) hysteresis, L = 4: jump intervals hot {s2['jump_hot']}, cold {s2['jump_cold']} "
  f"({'differ' if diff_iv else 'identical'}); largest |E_hot - E_cold| = {worst[0]:.2f} sigma at beta = {worst[1]}"
  f"  ->  {'HOLDS' if a else 'does not hold'}")

# (b) jump sizes
j4, j6 = s2["fall_cold"], st["S3"]["fall"]
dE8 = st["S5"].get("dE") if st.get("S5") else None
if dE8 is not None:
    shr = 1 - dE8 / j4
    b_shrinks = dE8 < 0.7 * j4
else:
    shr, b_shrinks = None, None
res["b"] = dict(jump4_cold=j4, jump6_cold=j6, dE8=dE8, fractional_shrink_4_to_8=shr, shrinks_more_than_30pc=b_shrinks)
w(f"(b) jump: L = 4 (cold) {j4:.5f}; L = 6 (cold scan) {j6:.5f}; Delta E(L = 8) "
  f"{'n/a' if dE8 is None else format(dE8, '.5f')}"
  + ("" if shr is None else f"  ->  change L = 4 -> 8: {-100*shr:+.1f} %; shrinks by more than 30 %: {'YES' if b_shrinks else 'no'}"))

# (c) two peaks
s6 = st.get("S6")
c = s6["two_peaks"]["two"] if s6 else None
res["c"] = dict(two_peaks=c, peaks=s6["two_peaks"]["peaks"] if s6 else None, binder=s6["binder"] if s6 else None)
if s6:
    w(f"(c) histogram L = 6 at beta_mix(6) = {s6['beta']}: peak bins {s6['two_peaks']['peaks']}; two peaks: "
      f"{'YES' if c else 'no'}; Binder B = {s6['binder']:.6f} (2/3 = 0.666667); E* crossings {s6['crossings_of_Estar']}, "
      f"fraction of sweeps below E* {s6['frac_below_Estar']:.3f}")
first = bool(a and c and (b_shrinks is False))
res["call"] = "first-order" if first else "order undetermined"
w(f"Call (card 4.4 step 7): {res['call']}")

# Q5 -- anisotropy record
w("")
w("Q5 -- E_s (rhombi) and E_t (temporal squares)")
q5 = {}
t3 = st["S3"]["table"]
for b in sorted(t3, key=float):
    cc = t3[b]["cold"]
    q5[f"L6_cold_{b}"] = dict(Es=cc["Es"], Et=cc["Et"], ratio=cc["Et"] / cc["Es"])
j = st["S3"]["jump"]
for lab, b in (("below", j[0]), ("above", j[1])):
    cc = t3[str(b)]["cold"]
    w(f"  L = 6 cold scan, {lab} the jump (beta = {b}): E_s = {cc['Es']:.5f} +- {cc['Es_err']:.5f}, "
      f"E_t = {cc['Et']:.5f} +- {cc['Et_err']:.5f}, E_t/E_s = {cc['Et']/cc['Es']:.4f}")
if st.get("S5") and st["S5"].get("dE_runs"):
    rows = {r["beta"]: r for r in st["S4_L8"]["rows"]}
    for lab, b in zip(("strong side (below beta_inf)", "weak side (above beta_inf)"), st["S5"]["dE_runs"]):
        if b is None:
            continue
        r = rows[b]
        q5[f"L8_{b}"] = dict(Es=r["Es_last10"], Et=r["Et_last10"], ratio=r["Et_last10"] / r["Es_last10"])
        w(f"  L = 8 mixed run at {b} ({lab}, {r['outcome']}): E_s = {r['Es_last10']:.5f}, E_t = {r['Et_last10']:.5f}, "
          f"E_t/E_s = {r['Et_last10']/r['Es_last10']:.4f}")
k3 = [v for v in st["K3"].values() if v["lattice"] == "void" and v["beta"] == 20.0][0]
q5["beta20"] = dict(Es=k3["Es"], Et=k3["Et"], ratio=k3["Et"] / k3["Es"])
w(f"  beta = 20 (K3, void L = 2, Lt = 6, cold): E_s = {k3['Es']:.6f} +- {k3['Es_err']:.6f}, "
  f"E_t = {k3['Et']:.6f} +- {k3['Et_err']:.6f}, E_t/E_s = {k3['Et']/k3['Es']:.4f}")
res["Q5"] = q5
json.dump(res, open(os.path.join(OUT, "q4q5.json"), "w"), indent=1)
txt = "\n".join(o) + "\n"
open(os.path.join(OUT, "q4q5.txt"), "w").write(txt)
print(txt)
