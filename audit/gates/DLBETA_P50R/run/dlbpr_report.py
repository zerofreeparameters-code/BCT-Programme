"""
Gate DL-BETA P50R -- Markdown tables for the result file. Written during the run (while the void chains ran).
Reads OUT/analysis.json (from `dlbpr_rules.py numbers`), OUT/state.json and OUT/records/*.json, and prints tables.
It computes no verdict input and no estimator: every number is read from analysis.json or the records.
Usage: python3 -I dlbpr_report.py OUTDIR > OUTDIR/tables.md
"""
import json, os, sys, math

U = 10 ** 7
NAMES = {"z4_8": "z4 L = 8 (L_t = 8)", "z4_12": "z4 L = 12 (L_t = 12)", "void_6": "void L = 6 (L_t = 18)", "void_8": "void L = 8 (L_t = 24)"}
ORDER = ["z4_8", "z4_12", "void_6", "void_8"]


def load_records(out):
    recs = {}
    d = os.path.join(out, "records")
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            r = json.load(open(os.path.join(d, fn)))
            recs[r["tag"]] = r
    return recs


def main(out):
    an = json.load(open(os.path.join(out, "analysis.json")))
    st = json.load(open(os.path.join(out, "state.json")))
    recs = load_records(out)
    A = an["A"]
    w = print
    # ---- K table
    w("## K table\n")
    w("| check | run | seed | value | target | dev | pass | bit-identical to Gate DL-BETA's stored series |")
    w("|---|---|---|---|---|---|---|---|")
    k1 = st["K1"]
    w(f"| K1 | dlb_sim.py SHA-256 | — | `{k1['sim']['dlb_sim.py'][:16]}…` | `{k1['sim_expected']['dlb_sim.py'][:16]}…` | — | {'PASS' if k1['pass'] else 'FAIL'} | — |")
    w(f"| K1 | dlb_complex.py SHA-256 | — | `{k1['sim']['dlb_complex.py'][:16]}…` | `{k1['sim_expected']['dlb_complex.py'][:16]}…` | — | {'PASS' if k1['pass'] else 'FAIL'} | — |")
    w(f"| K1 | dlbp_analysis.py SHA-256 | — | `{k1['dlbp_analysis_sha256'][:16]}…` | `{k1['dlbp_analysis_expected'][:16]}…` | — | {'PASS' if k1['pass'] else 'FAIL'} | — |")
    w(f"| K1 | K3_series.npz SHA-256 (reference) | — | `{str(k1['k3_series_sha256'])[:16]}…` | `{k1['k3_series_expected'][:16]}…` | — | {'match' if k1['k3_series_sha256'] == k1['k3_series_expected'] else 'MISMATCH'} | — |")
    for name, v in sorted(st["K2"].items()):
        w(f"| K2 | {name} (1000 + 10000) | {v['seed']} | {v['value']:.6f} | {v['target']:.6f} | {100*v['dev']:+.3f} % | {'PASS' if v['pass'] else 'FAIL'} | {'yes' if v['bit_identical'] else 'no'} |")
    z12 = A["z4_12"]
    k3 = z12["integrity"]["ok"] and z12["bracketed"] and z12["fit_ok"] and 1.0051 <= z12["b50"] <= 1.0171
    w(f"| K3 | Z4 L = 12 control | — | β₅₀ = {z12['b50']:.5f}; clean {z12['integrity']['ok']}; bracketed {z12['bracketed']}; fit {z12['fit_ok']} | β₅₀ in [1.0051, 1.0171] | — | {'PASS' if k3 else 'FAIL'} | — |")
    # K2 timings
    w("\nK2 run timings:\n")
    w("| run | seed | sweeps | seconds | ms/sweep | E_start | E (meas.) |")
    w("|---|---|---|---|---|---|---|")
    for tag in sorted(t for t in recs if t.startswith("K2_")):
        r = recs[tag]
        w(f"| {tag[3:]} | {r['seed']} | {r['n_therm']} + {r['n_meas']} | {r['seconds']:.1f} | {r['ms_per_sweep']:.2f} | {r['E_start']:.5f} | {r['E']:.6f} |")
    # ---- per lattice
    for key in ORDER:
        a = A[key]
        w(f"\n### {key}: {NAMES[key]}, V = {a['V']:.0f}\n")
        w("**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)\n")
        w("| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        for r in a["integrity"]["runs"]:
            tag = f"{key}_b{r['bn']:09d}_{r['role']}_c0"
            ms = recs[tag]["ms_per_sweep"]
            w(f"| {r['role']} | {r['bn']/U:.4f} | {r['seed']} | {r['E']:.5f} | {r['E_err']:.5f} | {r['span']:.5f} | {r['G']:.5f} | {0.25*r['G']:.5f} | {'ok' if r['ok'] else 'FAIL'} | {ms:.1f} |")
        S, W = a["S_line"], a["W_line"]
        w(f"\n- S(β) = {S['intercept0']:.6f} + ({S['slope']:.6f})·β; residuals {[round(x, 5) for x in S['resid']]}")
        w(f"- W(β) = {W['intercept0']:.6f} + ({W['slope']:.6f})·β; residuals {[round(x, 5) for x in W['resid']]}")
        ig = a["integrity"]
        spans_ok = all(r["ok"] for r in ig["runs"])
        w(f"- Integrity: **{'clean' if ig['ok'] else 'FAIL'}** (every span ≤ 0.25·G: {spans_ok}; S strictly decreasing: {ig['hot_monotone']}; "
          f"W strictly decreasing: {ig['cold_monotone']}; G > 0 at every window point: {ig['window_gaps_positive']})")
        w("\n**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)\n")
        w("| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |")
        w("|---|---|---|---|---|---|---|---|")
        for r in a["rows"]:
            w(f"| {r['bn']/U:.4f} | {r['S']:.5f} | {r['W']:.5f} | {r['gap']:.5f} | {r['n']} | {r['phi']:.4f} | {r['phi_err']:.4f} | {r['frac_weak']:.3f} |")
        ext = st["ext"].get(key, [])
        ext_s = "none" if not ext else ", ".join(f"{b/U:.4f}" for b in ext)
        w(f"\n- Grid [{a['grid'][0]/U:.4f}, {a['grid'][-1]/U:.4f}]; extensions: {ext_s}; bracketed: **{'yes' if a['bracketed'] else 'no'}**")
        w(f"- Probit: **β₅₀ = {a['b50']:.5f}**, w = {a['w']:.5f}, converged: **{a['fit_ok']}**; σ_boot = {a['sigma_boot']:.5f}, **σ = {a['sigma']:.5f}**; "
          f"bootstrap failures {a['boot_fail']}/{a['boot_n']}{' FLAG' if a['boot_fail_flag'] else ''}")
    # ---- integrity margins
    w("\n**Integrity margins.** The largest block span as a fraction of its limit 0.25·G:\n")
    w("| lattice | largest span / (0.25·G) | at |")
    w("|---|---|---|")
    for key in ORDER:
        a = A[key]
        best = max(a["integrity"]["runs"], key=lambda r: r["span"] / (0.25 * r["G"]))
        w(f"| {NAMES[key].split(' (')[0]} | {best['span']/(0.25*best['G']):.2f} | {best['role']}, β = {best['bn']/U:.4f} |")
    # ---- extrapolations
    exv, exz = an["ex_void"], an["ex_z4"]
    w("\n## Extrapolations\n")
    w("| extrapolation | k | β₅₀(small) ± σ | β₅₀(big) ± σ | shift | σ_∞ | σ_∞,stat (no floor) | U | β_∞ |")
    w("|---|---|---|---|---|---|---|---|---|")
    for nm, ex, s, b in (("**void, L = 6 → 8**", exv, A["void_6"], A["void_8"]), ("Z4, L = 8 → 12", exz, A["z4_8"], A["z4_12"])):
        w(f"| {nm} | {ex['k']:.5f} | {s['b50']:.5f} ± {s['sigma']:.5f} | {b['b50']:.5f} ± {b['sigma']:.5f} | {ex['shift']:+.5f} | {ex['sigma_inf']:.5f} | {ex['sigma_inf_stat']:.5f} | **{ex['U']:.5f}** | **{ex['beta_inf']:.5f}** |")
    w(f"\n> **β_c(P50R) = {exv['beta_inf']:.5f} ± {exv['U']:.5f}** (card convention); **1/e²_c = {exv['inv_e2']:.5f} ± {exv['inv_e2_U']:.5f}**")
    w(f"> Statistical part alone (σ_∞,stat): {exv['sigma_inf_stat']:.5f} in β, {exv['sigma_inf_stat']/math.sqrt(2):.5f} in 1/e².")
    # ---- diagnostics
    w("\n## Diagnostics (Q5)\n")
    w("| lattice | β₅₀ (probit) | φ interpolation crossing | weak-fraction crossing | β₅₀ from E_mid | drift β₅₀ − β₅₀(mid) | w | bootstrap failures |")
    w("|---|---|---|---|---|---|---|---|")
    for key in ORDER:
        a = A[key]
        ic = ", ".join(f"{x:.5f}" for x in a["interp_cross"]) + (" (NON-MONOTONE)" if a["nonmonotone"] else "")
        fc = ", ".join(f"{x:.5f}" for x in a["frac_cross"]) or "—"
        w(f"| {NAMES[key].split(' (')[0]} | {a['b50']:.5f} | {ic} | {fc} | {a['b50_mid']:.5f} | {a['drift']:+.5f} | {a['w']:.5f} | {a['boot_fail']} / {a['boot_n']} |")
    # ---- Appendix A
    w("\n## Appendix A — every mixed chain\n")
    w("f = (S(β) − E_end)/(S(β) − W(β)), with S and W the lattice's lines. f_mid uses E_mid. Seeds follow §4.4.\n")
    for key in ORDER:
        a = A[key]
        S, W = a["S_line"], a["W_line"]
        w(f"**{key}**\n")
        w("| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |")
        w("|---|---|---|---|---|---|---|---|")
        chains = sorted((r for r in recs.values() if r.get("lat") == key and r["role"] == "mixed"), key=lambda r: (r["bn"], r["chain"]))
        for r in chains:
            Sb = S["a"] + S["slope"] * (r["bn"] / U - S["xc"])
            Wb = W["a"] + W["slope"] * (r["bn"] / U - W["xc"])
            f = (Sb - r["E_end"]) / (Sb - Wb)
            fm = (Sb - r["E_mid"]) / (Sb - Wb)
            w(f"| {r['bn']/U:.4f} | {r['chain']} | {r['seed']} | {r['E_end']:.5f} | {f:.4f} | {r['E_mid']:.5f} | {fm:.4f} | {r['ms_per_sweep']:.1f} |")
        w("")
    # ---- timing summary
    w("\n## Timing\n")
    w("| lattice | runs | sweeps | core-seconds | mean ms/sweep |")
    w("|---|---|---|---|---|")
    tot_s = 0
    for key in ["K2"] + ORDER:
        rs = [r for r in recs.values() if r.get("lat") == key]
        sw = sum(r["n_therm"] + r["n_meas"] for r in rs)
        sec = sum(r["seconds"] for r in rs)
        tot_s += sec
        w(f"| {key} | {len(rs)} | {sw} | {sec:.0f} | {1000*sec/sw if sw else 0:.1f} |")
    w(f"| **total** | {len(recs)} | | **{tot_s:.0f}** ({tot_s/60:.1f} core-minutes) | |")


if __name__ == "__main__":
    main(sys.argv[1])
