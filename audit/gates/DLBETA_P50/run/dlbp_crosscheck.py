"""
Gate DL-BETA P50 -- independent cross-check (verification only; written after the verdict; not a verdict input).
Recomputes every §4.5 quantity from the raw series files (not from the records' summary fields), using the
card's text and different routines (numpy.polyfit, scipy curve_fit), and re-derives every seed from §4.4.
Usage: python3 -I dlbp_crosscheck.py OUTDIR
"""
import hashlib, json, math, os, sys
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm

out = sys.argv[1]
an = json.load(open(os.path.join(out, "analysis.json")))
recs = [json.load(open(os.path.join(out, "records", f))) for f in sorted(os.listdir(os.path.join(out, "records"))) if f.endswith(".json")]
LAT = {"z4_8": ("z4", 8, 4), "z4_12": ("z4", 12, 4), "void_6": ("void", 6, 6), "void_8": ("void", 8, 6)}
bad = 0


def chk(cond, msg):
    global bad
    if not cond:
        bad += 1
        print("MISMATCH", msg)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def seed_card(kind, L, beta, s, c):
    return (3000000 if kind == "z4" else 4000000) + 100000 * c + 7919 * L + round(1e4 * beta) + s


nser = 0
for r in recs:
    p = os.path.join(out, "series", r["series_file"])
    chk(sha(p) == r["series_sha256"], f"series hash {r['tag']}")
    z = np.load(p)
    ser = z["series"]
    chk(int(z["seed"]) == r["seed"], f"seed in npz {r['tag']}")
    nser += 1
    if r["lat"] == "K2":
        continue
    kind, L, _ = LAT[r["lat"]]
    s = {"hot": 0, "cold": 1, "mixed": 2}[r["role"]]
    chk(r["seed"] == seed_card(kind, L, r["beta"], s, r["chain"]), f"seed rule {r['tag']}")
    if r["role"] in ("hot", "cold"):
        chk(ser.shape == (2001, 3), f"branch length {r['tag']}")
        m = ser[501:2001, 0]
        bm = m.reshape(20, 75).mean(1)
        chk(abs(m.mean() - r["E"]) < 1e-13 and abs(bm.std(ddof=1) / math.sqrt(20) - r["E_err"]) < 1e-13, f"branch E {r['tag']}")
    else:
        chk(ser.shape == (3001, 3), f"mixed length {r['tag']}")
        chk(abs(ser[2550:3001:50, 0].mean() - r["E_end"]) < 1e-13, f"E_end {r['tag']}")
        chk(abs(ser[1050:1501:50, 0].mean() - r["E_mid"]) < 1e-13, f"E_mid {r['tag']}")
print(f"series files checked: {nser}")

res = {}
for key, (kind, L, nch) in LAT.items():
    a = an["A"][key]
    br = {r["role"]: {} for r in recs if r["lat"] == key}
    for r in recs:
        if r["lat"] == key and r["role"] in ("hot", "cold"):
            br[r["role"]][round(r["beta"], 4)] = r
    Sb = sorted(br["hot"]); Wb = sorted(br["cold"])
    pS = np.polyfit(Sb, [br["hot"][b]["E"] for b in Sb], 1)
    pW = np.polyfit(Wb, [br["cold"][b]["E"] for b in Wb], 1)
    chk(abs(pS[0] - a["S_line"]["slope"]) < 1e-9 and abs(pW[0] - a["W_line"]["slope"]) < 1e-9, f"lines {key}")
    ch = sorted([r for r in recs if r["lat"] == key and r["role"] == "mixed"], key=lambda r: (r["beta"], r["chain"]))
    betas = sorted(set(round(r["beta"], 4) for r in ch))
    chk(all(sum(1 for r in ch if round(r["beta"], 4) == b) == nch for b in betas), f"chain count {key}")
    bv = np.array([r["beta"] for r in ch])
    fv = np.array([(np.polyval(pS, r["beta"]) - r["E_end"]) / (np.polyval(pS, r["beta"]) - np.polyval(pW, r["beta"])) for r in ch])
    phi = [fv[np.isclose(bv, b)].mean() for b in betas]
    chk(all(abs(x - y["phi"]) < 1e-9 for x, y in zip(phi, a["rows"])), f"phi {key}")
    popt, _ = curve_fit(lambda x, b0, w: norm.cdf((x - b0) / w), bv, fv, p0=[np.mean(betas), 0.002],
                        bounds=([min(betas) - 0.01, 1e-5], [max(betas) + 0.01, 0.1]))
    chk(abs(popt[0] - a["b50"]) < 2e-6 and abs(popt[1] - a["w"]) < 2e-6, f"probit {key}: {popt} vs {a['b50']}, {a['w']}")
    # an independent bootstrap (different RNG; 300 replicas), only to confirm the size of sigma_boot
    rng = np.random.default_rng(777 + L)
    reps = []
    for _ in range(300):
        pS2 = np.polyfit(Sb, [br["hot"][b]["E"] + br["hot"][b]["E_err"] * rng.standard_normal() for b in Sb], 1)
        pW2 = np.polyfit(Wb, [br["cold"][b]["E"] + br["cold"][b]["E_err"] * rng.standard_normal() for b in Wb], 1)
        xb, yb = [], []
        for b in betas:
            idx = np.where(np.isclose(bv, b))[0]
            for i in rng.choice(idx, len(idx)):
                s_, w_ = np.polyval(pS2, bv[i]), np.polyval(pW2, bv[i])
                xb.append(bv[i]); yb.append((s_ - ch[i]["E_end"]) / (s_ - w_))
        try:
            pp, _ = curve_fit(lambda x, b0, w: norm.cdf((x - b0) / w), xb, yb, p0=popt,
                              bounds=([min(betas) - 0.01, 1e-5], [max(betas) + 0.01, 0.1]))
            reps.append(pp[0])
        except Exception:
            pass
    res[key] = dict(b50=popt[0], w=popt[1], sboot=float(np.std(reps, ddof=1)), V=a["V"])
    print(f"{key}: beta_50 = {popt[0]:.5f} (pinned {a['b50']:.5f}); w = {popt[1]:.5f} (pinned {a['w']:.5f}); "
          f"independent sigma_boot = {res[key]['sboot']:.5f} (pinned {a['sigma_boot']:.5f}), {len(reps)}/300 converged")


def extrap(s, b):
    k = (1 / b["V"]) / (1 / s["V"] - 1 / b["V"])
    sh = -k * (s["b50"] - b["b50"])
    ss, sb = max(s["sboot"], 0.0007), max(b["sboot"], 0.0007)
    si = math.hypot((1 + k) * sb, k * ss)
    return k, b["b50"] + sh, si, sh, math.hypot(si, sh)


for nm, s, b, ex in (("void", "void_6", "void_8", an["ex_void"]), ("Z4", "z4_8", "z4_12", an["ex_z4"])):
    k, bi, si, sh, Uc = extrap(res[s], res[b])
    chk(abs(bi - ex["beta_inf"]) < 5e-6 and abs(Uc - ex["U"]) < 5e-6, f"extrapolation {nm}")
    print(f"extrapolation {nm}: k = {k:.5f}; beta_inf = {bi:.5f} (pinned {ex['beta_inf']:.5f}); U = {Uc:.5f} (pinned {ex['U']:.5f}); "
          + (f"1/e^2 = {bi/math.sqrt(2):.5f} +- {Uc/math.sqrt(2):.5f}" if nm == "void" else "(1/e^2 convention is for the void complex only)"))
print("CROSS-CHECK", "PASS" if bad == 0 else f"FAIL ({bad} mismatches)")
