"""
Gate DL-BETA P50R -- seeds, numbers and verdict (card sections 4.4, 4.5, 4.7, 5). Pre-registered with the card;
imported by dlbpr_driver.py. Every estimator (branch lines, integrity, phi, probit, bootstrap, extensions,
extrapolation) is Gate DL-BETA P50's, imported unmodified from dlbp_analysis.py (hash-checked below), so the
two gates differ only in the simulator and the seeds.
Usage after the run:
    python3 -I dlbpr_rules.py numbers OUTDIR          -> OUTDIR/dlbpr_numbers.txt, OUTDIR/analysis.json
    python3 -I dlbpr_rules.py verdict OUTDIR P50_ANALYSIS_JSON
                                                      -> OUTDIR/verdict.txt (refuses unless dlbpr_numbers.sha256 exists)
"""
import hashlib, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlbp_analysis as AN          # Gate DL-BETA P50's estimators, unmodified

AN_SHA256 = "3ab1b43e44e3ace845880ceea6af66d1872b76da9637a80d5485fd5b6b57870b"      # P50 dlbp_analysis.py
P50_ANALYSIS_SHA256 = "56beab6898239358164235d7cc4b28ec29a2726922c3d0f29d04f8356c9f63c1"  # DLBETA_P50/OUT/analysis.json
U_SHARP = 0.0020                    # card 5: inconclusive above this U
DRY = os.environ.get("DLBP_DRYRUN") == "1"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def seed(kind, L, bn, s, c):
    """card 4.4: Z4 5,000,000 + 100,000 c + 7919 L + round(1e4 beta) + s; void 6,000,000 + ... (dry run: + 9,000,000)."""
    base = 5000000 if kind == "z4" else 6000000
    return base + 100000 * c + 7919 * L + round(1e4 * (bn / 1e7)) + s + (9000000 if DRY else 0)


def stat_inf(a_small, a_big, k):
    """sigma_inf from the bootstrap alone (no floor): the statistical error of beta_inf (card 4.5)."""
    return math.sqrt(((1 + k) * a_big["sigma_boot"]) ** 2 + (k * a_small["sigma_boot"]) ** 2)


def fmt(x, d=5):
    return "none" if x is None or x != x else f"{x:.{d}f}"


def numbers(out):
    if sha256(os.path.join(HERE, "dlbp_analysis.py")) != AN_SHA256:
        sys.exit("refusing: dlbp_analysis.py is not P50's pinned file")
    recs = AN.load_records(out)
    st = json.load(open(os.path.join(out, "state.json")))
    A = {k: AN.analyse_lattice(recs, k, boot=AN.B_BOOT) for k in AN.ORDER}
    ex_v = AN.extrapolate(A["void_6"], A["void_8"])
    ex_z = AN.extrapolate(A["z4_8"], A["z4_12"])
    ex_v["sigma_inf_stat"] = stat_inf(A["void_6"], A["void_8"], ex_v["k"])
    ex_z["sigma_inf_stat"] = stat_inf(A["z4_8"], A["z4_12"], ex_z["k"])
    L = []
    w = L.append
    w("# Gate DL-BETA P50R -- dlbpr_numbers.txt (written before any comparison with Gate DL-BETA P50 or earlier gates)")
    w("# simulator: Gate DL-BETA's dlb_sim.py (original code); estimators: P50's dlbp_analysis.py, unmodified.")
    w("# beta in card convention; 1/e^2 = beta/sqrt2 on the void complex. f = (S - E_end)/(S - W).")
    for name, v in sorted(st.get("K2", {}).items()):
        w(f"K2 {name}: value = {v['value']:.6f}; target = {v['target']:.6f}; dev = {100*v['dev']:+.3f}%; pass = {'yes' if v['pass'] else 'no'}; "
          f"bit-identical to Gate DL-BETA's stored series = {'yes' if v.get('bit_identical') else 'no'}")
    for key in AN.ORDER:
        a = A[key]
        w(f"[{key}] {a['kind']} L = {a['L']}, V = {a['V']:.0f}")
        w(f"  S(beta) = {a['S_line']['intercept0']:.6f} + ({a['S_line']['slope']:.6f}) beta ; resid {[round(x, 5) for x in a['S_line']['resid']]}")
        w(f"  W(beta) = {a['W_line']['intercept0']:.6f} + ({a['W_line']['slope']:.6f}) beta ; resid {[round(x, 5) for x in a['W_line']['resid']]}")
        for r in a["integrity"]["runs"]:
            w(f"  branch {r['role']:4s} beta {r['bn']/AN.U:.4f} seed {r['seed']}: E = {r['E']:.5f} +- {r['E_err']:.5f}; span {r['span']:.5f} <= 0.25 G {0.25*r['G']:.5f}: {'ok' if r['ok'] else 'FAIL'}")
        w(f"  integrity = {'ok' if a['integrity']['ok'] else 'FAIL'} (hot monotone {a['integrity']['hot_monotone']}, cold monotone {a['integrity']['cold_monotone']}, window gaps > 0 {a['integrity']['window_gaps_positive']})")
        for r in a["rows"]:
            w(f"  beta {r['bn']/AN.U:.4f}: S {r['S']:.5f} W {r['W']:.5f}; phi = {r['phi']:.4f} +- {r['phi_err']:.4f} (n {r['n']}); frac_weak {r['frac_weak']:.3f}; f = {[round(x, 4) for x in r['f']]}")
        w(f"  grid = [{a['grid'][0]/AN.U:.4f}, {a['grid'][-1]/AN.U:.4f}]; extensions = {st['ext'].get(key, [])}; bracketed = {'yes' if a['bracketed'] else 'no'}")
        w(f"  beta_50 = {fmt(a['b50'])}; w = {fmt(a['w'])}; fit_ok = {a['fit_ok']}; sigma_boot = {fmt(a['sigma_boot'])}; sigma = {fmt(a['sigma'])}; "
          f"boot failures {a['boot_fail']}/{a['boot_n']}{' FLAG' if a['boot_fail_flag'] else ''}")
        w(f"  check: interp crossing(s) of phi = {[round(x, 5) for x in a['interp_cross']]}{' NON-MONOTONE' if a['nonmonotone'] else ''}; "
          f"frac_weak crossing(s) = {[round(x, 5) for x in a['frac_cross']]}; beta_50(mid, sweeps 1050-1500) = {fmt(a['b50_mid'])}; drift = {fmt(a['drift'])}")
    for nm, ex in (("void (L = 6, 8)", ex_v), ("Z4 (L = 8, 12)", ex_z)):
        w(f"extrapolation {nm}: k = {ex['k']:.4f}; beta_inf = {ex['beta_inf']:.5f}; sigma_inf = {ex['sigma_inf']:.5f}; "
          f"sigma_inf(stat, no floor) = {ex['sigma_inf_stat']:.5f}; shift = {ex['shift']:+.5f}; U = {ex['U']:.5f}")
    if A["void_6"]["fit_ok"] and A["void_8"]["fit_ok"]:
        w(f"RESULT beta_c(P50R) = {ex_v['beta_inf']:.5f} +- {ex_v['U']:.5f} (card convention); 1/e^2_c = {ex_v['inv_e2']:.5f} +- {ex_v['inv_e2_U']:.5f}")
    else:
        w("RESULT beta_c(P50R) = not defined (a void probit fit failed)")
    if A["z4_8"]["fit_ok"] and A["z4_12"]["fit_ok"]:
        w(f"Z4 calibration: beta_inf(Z4) - {AN.Z4_LIT} = {ex_z['beta_inf'] - AN.Z4_LIT:+.5f} = {(ex_z['beta_inf'] - AN.Z4_LIT)/ex_z['U']:+.2f} U")
    else:
        w("Z4 calibration: not defined (a Z4 probit fit failed)")
    txt = "\n".join(L) + "\n"
    open(os.path.join(out, "dlbpr_numbers.txt"), "w").write(txt)
    json.dump(dict(A=A, ex_void=ex_v, ex_z4=ex_z), open(os.path.join(out, "analysis.json"), "w"), indent=1, default=float)
    print(txt)


def verdict(out, p50_json):
    if not os.path.exists(os.path.join(out, "dlbpr_numbers.sha256")):
        sys.exit("refusing: hash dlbpr_numbers.txt first (card 4.7)")
    if sha256(p50_json) != P50_ANALYSIS_SHA256:
        sys.exit("refusing: P50 analysis.json does not match its pinned hash")
    st = json.load(open(os.path.join(out, "state.json")))
    an = json.load(open(os.path.join(out, "analysis.json")))
    p50 = json.load(open(p50_json))
    A, ex = an["A"], an["ex_void"]
    P, exP = p50["A"], p50["ex_void"]
    z12 = A["z4_12"]
    k1_ok = bool(st.get("K1", {}).get("pass"))
    k2_ok = bool(st.get("K2")) and all(v["pass"] for v in st["K2"].values())
    k3_ok = z12["integrity"]["ok"] and z12["bracketed"] and z12["fit_ok"] and AN.Z4_K3[0] / AN.U <= z12["b50"] <= AN.Z4_K3[1] / AN.U
    void_ok = all(A[k]["integrity"]["ok"] and A[k]["bracketed"] and A[k]["fit_ok"] for k in ("void_6", "void_8"))
    D = ex["beta_inf"] - exP["beta_inf"]
    U_D = math.hypot(ex["U"], exP["U"])
    sP = stat_inf(P["void_6"], P["void_8"], exP["k"])
    s_D = math.hypot(ex["sigma_inf_stat"], sP)
    if not (k1_ok and k2_ok and k3_ok):
        code = "SC-DLBPR-0"
    elif not void_ok:
        code = "SC-DLBPR-5"
    elif ex["U"] > U_SHARP:
        code = "SC-DLBPR-4"
    elif abs(D) > 2 * U_D:
        code = "SC-DLBPR-3"
    elif abs(D) > 2 * s_D:
        code = "SC-DLBPR-2"
    else:
        code = "SC-DLBPR-1"
    L = [f"K1 {k1_ok}; K2 {k2_ok}; K3 (Z4 L=12 beta_50 = {z12['b50']:.5f} in [1.0051, 1.0171], clean, bracketed, fit) {k3_ok}",
         f"void L=6, L=8 clean, bracketed, fit: {void_ok}",
         f"beta_c(P50R) = {ex['beta_inf']:.5f} +- {ex['U']:.5f} (stat {ex['sigma_inf_stat']:.5f}); U <= {U_SHARP}: {ex['U'] <= U_SHARP}",
         f"beta_c(P50)  = {exP['beta_inf']:.5f} +- {exP['U']:.5f} (stat {sP:.5f})",
         f"D = beta_c(P50R) - beta_c(P50) = {D:+.5f}; U_D = {U_D:.5f} (|D| = {abs(D)/U_D:.2f} U_D); sigma_D(stat) = {s_D:.5f} (|D| = {abs(D)/s_D:.2f} sigma_D)",
         f"|D| <= 2 U_D: {abs(D) <= 2 * U_D}; |D| <= 2 sigma_D(stat): {abs(D) <= 2 * s_D}"]
    # diagnostics (reported, not verdict inputs)
    for key in AN.ORDER:
        a, p = A[key], P[key]
        d = a["b50"] - p["b50"]
        sf, ss = math.hypot(a["sigma"], p["sigma"]), math.hypot(a["sigma_boot"], p["sigma_boot"])
        L.append(f"diag {key}: beta_50 {a['b50']:.5f} vs P50 {p['b50']:.5f}; diff {d:+.5f} = {d/sf:+.2f} sigma (with floor) = {d/ss:+.2f} sigma_boot")
        zs = []
        for r, q in zip(a["integrity"]["runs"], p["integrity"]["runs"]):
            assert (r["role"], r["bn"]) == (q["role"], q["bn"])
            zs.append((r["E"] - q["E"]) / math.hypot(r["E_err"], q["E_err"]))
        L.append(f"diag {key}: branch E cross-code z (hot then cold) = {[round(z, 2) for z in zs]}; rms {math.sqrt(sum(z*z for z in zs)/len(zs)):.2f}; max |z| {max(abs(z) for z in zs):.2f}")
        pr = {r["bn"]: r for r in p["rows"]}
        L.append(f"diag {key}: phi(P50R) - phi(P50) at common window points = "
                 + str([(round(r['bn']/AN.U, 4), round(r['phi'] - pr[r['bn']]['phi'], 3)) for r in a["rows"] if r["bn"] in pr]))
    exz, exzP = an["ex_z4"], p50["ex_z4"]
    L.append(f"diag Z4: beta_inf(P50R) = {exz['beta_inf']:.5f} +- {exz['U']:.5f}; P50 {exzP['beta_inf']:.5f} +- {exzP['U']:.5f}; literature {AN.Z4_LIT}")
    L.append(f"VERDICT {code}")
    txt = "\n".join(L) + "\n"
    open(os.path.join(out, "verdict.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    cmd, out = sys.argv[1], sys.argv[2]
    if cmd == "numbers":
        numbers(out)
    elif cmd == "verdict":
        verdict(out, sys.argv[3])
