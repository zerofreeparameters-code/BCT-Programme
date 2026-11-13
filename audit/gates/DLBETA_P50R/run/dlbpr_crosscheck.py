"""
Gate DL-BETA P50R -- independent cross-check (written AFTER the verdict; not a verdict input).
Recomputes card section 4.5 from the raw .npz series rather than from the records' summary fields, with different
routines (numpy.polyfit, scipy.optimize.curve_fit with bounds) and re-derives every seed from the section 4.4 formula.
Usage: python3 -I dlbpr_crosscheck.py OUTDIR > OUTDIR/crosscheck_output.txt
"""
import hashlib, json, math, os, sys
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm

U = 10 ** 7
SIGMA_FLOOR = 0.0007
LAT = {"z4_8": ("z4", 8, 4096.0), "z4_12": ("z4", 12, 20736.0), "void_6": ("void", 6, 3888.0), "void_8": ("void", 8, 12288.0)}
S_PTS = {"z4": [9800000, 9850000, 9900000, 9950000], "void": [12300000, 12350000, 12400000, 12450000]}
W_PTS = {"z4": [10200000, 10250000, 10300000, 10350000], "void": [12650000, 12700000, 12750000, 12800000]}
ORDER = ["z4_8", "z4_12", "void_6", "void_8"]
fails = []


def ck(cond, msg):
    print(("  OK   " if cond else "  FAIL ") + msg)
    if not cond:
        fails.append(msg)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def seed_rule(kind, L, bn, s, c):
    base = 5000000 if kind == "z4" else 6000000
    return base + 100000 * c + 7919 * L + round(1e4 * (bn / 1e7)) + s


def main(out):
    an = json.load(open(os.path.join(out, "analysis.json")))
    A = an["A"]
    recs = {}
    for fn in sorted(os.listdir(os.path.join(out, "records"))):
        if fn.endswith(".json"):
            r = json.load(open(os.path.join(out, "records", fn)))
            recs[r["tag"]] = r
    print(f"# Gate DL-BETA P50R cross-check ({len(recs)} records)\n")

    print("## 1. Series hashes and seeds")
    bad_h = bad_s = 0
    for t, r in recs.items():
        if sha256(os.path.join(out, "series", r["series_file"])) != r["series_sha256"]:
            bad_h += 1
        if r["lat"] != "K2":
            if r["seed"] != seed_rule(r["kind"], r["L"], r["bn"], r["s"], r["chain"]):
                bad_s += 1
    ck(bad_h == 0, f"all {len(recs)} series files match their recorded SHA-256 ({bad_h} mismatches)")
    ck(bad_s == 0, f"every gate seed follows the section 4.4 formula ({bad_s} mismatches)")
    k2seeds = {r["seed"] for t, r in recs.items() if r["lat"] == "K2"}
    ck(k2seeds == {516838, 715839, 32676, 231677}, f"K2 reuses Gate DL-BETA's four K3 seeds: {sorted(k2seeds)}")
    gate = sorted(r["seed"] for r in recs.values() if r["lat"] != "K2")
    ck(len(gate) == len(set(gate)), f"all {len(gate)} gate seeds distinct; range {min(gate)}–{max(gate)}")
    ck(min(gate) >= 5000000, "every gate seed is in the card's 5,000,000 / 6,000,000 families")

    print("\n## 2. Observables recomputed from the raw series")
    worst_E = worst_err = worst_end = worst_mid = 0.0
    for t, r in recs.items():
        z = np.load(os.path.join(out, "series", r["series_file"]))
        ser = z["series"]
        n = r["n_therm"] + r["n_meas"]
        ck_shape = ser.shape == (n + 1, 3)
        if not ck_shape:
            fails.append(f"{t} series shape")
        m = ser[r["n_therm"] + 1:, 0]
        if "E" in r:
            worst_E = max(worst_E, abs(float(m.mean()) - r["E"]))
            bm = m.reshape(20, -1).mean(axis=1)
            e = float(np.std(bm, ddof=1) / np.sqrt(20))
            worst_err = max(worst_err, abs(e - r["E_err"]))
        if "E_end" in r:
            idx = np.arange(50, n + 1, 50)
            rd = ser[idx, 0]
            worst_end = max(worst_end, abs(float(rd[-10:].mean()) - r["E_end"]))
            half = n // 2
            mid = np.arange(half - 450, half + 1, 50)
            worst_mid = max(worst_mid, abs(float(ser[mid, 0].mean()) - r["E_mid"]))
    ck(worst_E < 1e-12, f"branch E reproduced from the series (max |diff| {worst_E:.2e})")
    ck(worst_err < 1e-12, f"20-block sigma_E reproduced (max |diff| {worst_err:.2e})")
    ck(worst_end < 1e-12, f"E_end (sweeps 2550-3000) reproduced (max |diff| {worst_end:.2e})")
    ck(worst_mid < 1e-12, f"E_mid (sweeps 1050-1500) reproduced (max |diff| {worst_mid:.2e})")
    ck(all(np.isnan(np.load(os.path.join(out, "series", r["series_file"]))["series"][0, 1]) for r in list(recs.values())[:5]),
       "row 0 of the series is (E at the start, NaN, NaN) as card section 4.2 states")

    print("\n## 3. Branch lines, phi and the probit, with different routines")
    for key in ORDER:
        kind, L, V = LAT[key]
        a = A[key]
        br = {ro: {} for ro in ("hot", "cold")}
        ch = {}
        for r in recs.values():
            if r.get("lat") != key:
                continue
            if r["role"] in ("hot", "cold"):
                br[r["role"]][r["bn"]] = r
            elif r["role"] == "mixed":
                ch.setdefault(r["bn"], []).append(r)
        # lines by numpy.polyfit (the pinned code uses lstsq on a centred design)
        sl, si = np.polyfit([b / U for b in S_PTS[kind]], [br["hot"][b]["E"] for b in S_PTS[kind]], 1)
        wl, wi = np.polyfit([b / U for b in W_PTS[kind]], [br["cold"][b]["E"] for b in W_PTS[kind]], 1)
        d1 = max(abs(si - a["S_line"]["intercept0"]), abs(sl - a["S_line"]["slope"]))
        d2 = max(abs(wi - a["W_line"]["intercept0"]), abs(wl - a["W_line"]["slope"]))
        ck(max(d1, d2) < 1e-9, f"{key}: S and W lines match polyfit (max |diff| {max(d1, d2):.2e})")
        # integrity, recomputed
        worst = None
        for ro, pts in (("hot", S_PTS[kind]), ("cold", W_PTS[kind])):
            for b in pts:
                r = br[ro][b]
                z = np.load(os.path.join(out, "series", r["series_file"]))["series"]
                bm = z[r["n_therm"] + 1:, 0].reshape(20, -1).mean(axis=1)
                span = float(bm.max() - bm.min())
                G = (si + sl * (b / U)) - (wi + wl * (b / U))
                ratio = span / (0.25 * G)
                if worst is None or ratio > worst[0]:
                    worst = (ratio, ro, b, span, 0.25 * G)
                rec_run = [x for x in a["integrity"]["runs"] if x["role"] == ro and x["bn"] == b][0]
                if abs(span - rec_run["span"]) > 1e-12:
                    fails.append(f"{key} {ro} {b} span")
                if (ratio <= 1.0) != rec_run["ok"]:
                    fails.append(f"{key} {ro} {b} integrity verdict")
        print(f"  {key}: worst span/(0.25 G) = {worst[0]:.3f} at {worst[1]} beta {worst[2]/U:.4f} "
              f"(span {worst[3]:.5f}, limit {worst[4]:.5f}) -> integrity {'ok' if worst[0] <= 1 else 'FAIL'}")
        ck((worst[0] <= 1.0) == a["integrity"]["ok"], f"{key}: integrity verdict reproduced ({'ok' if a['integrity']['ok'] else 'FAIL'})")
        # phi and probit by curve_fit
        bv, fv = [], []
        for bn in sorted(ch):
            Sb = si + sl * (bn / U)
            Wb = wi + wl * (bn / U)
            for r in sorted(ch[bn], key=lambda x: x["chain"]):
                bv.append(bn / U)
                fv.append((Sb - r["E_end"]) / (Sb - Wb))
        p, _ = curve_fit(lambda x, b50, w: norm.cdf((x - b50) / w), np.array(bv), np.array(fv),
                         p0=[a["b50"], a["w"]], bounds=([min(bv) - 0.01, 1e-5], [max(bv) + 0.01, 0.1]), maxfev=20000)
        ck(abs(p[0] - a["b50"]) < 1e-6 and abs(p[1] - a["w"]) < 1e-6,
           f"{key}: beta_50 {p[0]:.6f} vs {a['b50']:.6f}, w {p[1]:.6f} vs {a['w']:.6f}")
        # independent bootstrap, different RNG and replica count
        rng = np.random.default_rng(987654 + L)
        reps = []
        for _ in range(300):
            sl2, si2 = np.polyfit([b / U for b in S_PTS[kind]],
                                  [br["hot"][b]["E"] + br["hot"][b]["E_err"] * rng.standard_normal() for b in S_PTS[kind]], 1)
            wl2, wi2 = np.polyfit([b / U for b in W_PTS[kind]],
                                  [br["cold"][b]["E"] + br["cold"][b]["E_err"] * rng.standard_normal() for b in W_PTS[kind]], 1)
            bb, ff = [], []
            for bn in sorted(ch):
                cs = ch[bn]
                Sb, Wb = si2 + sl2 * (bn / U), wi2 + wl2 * (bn / U)
                for i in rng.integers(0, len(cs), len(cs)):
                    bb.append(bn / U)
                    ff.append((Sb - cs[i]["E_end"]) / (Sb - Wb))
            try:
                q, _ = curve_fit(lambda x, b50, w: norm.cdf((x - b50) / w), np.array(bb), np.array(ff),
                                 p0=[p[0], p[1]], bounds=([min(bb) - 0.01, 1e-5], [max(bb) + 0.01, 0.1]), maxfev=20000)
                reps.append(q[0])
            except Exception:
                pass
        s2 = float(np.std(reps, ddof=1))
        print(f"  {key}: independent 300-replica bootstrap sigma_boot = {s2:.5f} (pinned 1000-replica: {a['sigma_boot']:.5f})")

    print("\n## 4. Extrapolations")
    for nm, small, big, ex in (("void", A["void_6"], A["void_8"], an["ex_void"]), ("z4", A["z4_8"], A["z4_12"], an["ex_z4"])):
        k = (1.0 / big["V"]) / (1.0 / small["V"] - 1.0 / big["V"])
        shift = -k * (small["b50"] - big["b50"])
        binf = big["b50"] + shift
        sinf = math.sqrt(((1 + k) * big["sigma"]) ** 2 + (k * small["sigma"]) ** 2)
        Uc = math.sqrt(sinf ** 2 + shift ** 2)
        sstat = math.sqrt(((1 + k) * big["sigma_boot"]) ** 2 + (k * small["sigma_boot"]) ** 2)
        ck(abs(binf - ex["beta_inf"]) < 1e-12 and abs(Uc - ex["U"]) < 1e-12 and abs(sstat - ex["sigma_inf_stat"]) < 1e-12,
           f"{nm}: k {k:.5f}, beta_inf {binf:.6f}, U {Uc:.6f}, sigma_inf_stat {sstat:.6f} all reproduced")
        if nm == "void":
            ck(abs(binf / math.sqrt(2) - ex["inv_e2"]) < 1e-12, f"void: 1/e^2 = beta_inf/sqrt(2) = {binf/math.sqrt(2):.6f} reproduced")

    print("\n## 5. Verdict inputs recomputed (card section 5 order)")
    p50 = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else None
    if p50:
        exP, exR = p50["ex_void"], an["ex_void"]
        kP = exP["k"]
        sP = math.sqrt(((1 + kP) * p50["A"]["void_8"]["sigma_boot"]) ** 2 + (kP * p50["A"]["void_6"]["sigma_boot"]) ** 2)
        D = exR["beta_inf"] - exP["beta_inf"]
        U_D = math.hypot(exR["U"], exP["U"])
        s_D = math.hypot(exR["sigma_inf_stat"], sP)
        print(f"  D = {D:+.6f}; U_D = {U_D:.6f} ({abs(D)/U_D:.2f} U_D); sigma_D = {s_D:.6f} ({abs(D)/s_D:.2f} sigma_D)")
        vt = open(os.path.join(out, "verdict.txt")).read()
        ck(f"{D:+.5f}" in vt and f"{U_D:.5f}" in vt and f"{s_D:.5f}" in vt, "D, U_D and sigma_D match verdict.txt")
        void_ok = all(A[k]["integrity"]["ok"] and A[k]["bracketed"] and A[k]["fit_ok"] for k in ("void_6", "void_8"))
        code = "SC-DLBPR-5" if not void_ok else ("SC-DLBPR-4" if exR["U"] > 0.0020 else
               ("SC-DLBPR-3" if abs(D) > 2 * U_D else ("SC-DLBPR-2" if abs(D) > 2 * s_D else "SC-DLBPR-1")))
        ck(f"VERDICT {code}" in vt, f"verdict code reproduced: {code}")
        print(f"  (had the void integrity passed, the ordered code would have been "
              f"{'SC-DLBPR-4' if exR['U'] > 0.0020 else ('SC-DLBPR-3' if abs(D) > 2*U_D else ('SC-DLBPR-2' if abs(D) > 2*s_D else 'SC-DLBPR-1'))})")

    print("\n" + ("CROSS-CHECK PASS" if not fails else f"CROSS-CHECK FAIL: {fails}"))


if __name__ == "__main__":
    main(sys.argv[1])
