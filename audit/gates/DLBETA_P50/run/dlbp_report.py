"""
Gate DL-BETA P50 -- report tables (written during the run, after the driver started; formatting only).
Reads OUTDIR/analysis.json, OUTDIR/state.json and OUTDIR/records/*.json and prints Markdown tables for the
result file. It computes no estimator, threshold or verdict input: every number it prints is either copied
from those files or (for E_end / E_mid per chain) read from the records the analysis used.
Usage: python3 -I dlbp_report.py OUTDIR > tables.md
"""
import json, os, sys

U = 10 ** 7


def main(out):
    an = json.load(open(os.path.join(out, "analysis.json")))
    st = json.load(open(os.path.join(out, "state.json")))
    recs = {}
    for fn in sorted(os.listdir(os.path.join(out, "records"))):
        if fn.endswith(".json"):
            r = json.load(open(os.path.join(out, "records", fn)))
            recs[r["tag"]] = r
    P = print
    # K table
    P("### K table\n")
    P("| check | run | seed | value | target | dev | pass | bit-identical to REP1 |")
    P("|---|---|---|---|---|---|---|---|")
    P(f"| K1 | dlbr_sim.py SHA-256 | — | `{st['K1']['dlbr_sim_sha256'][:16]}…` | `{st['K1']['expected'][:16]}…` | — | {'PASS' if st['K1']['pass'] else 'FAIL'} | — |")
    for name, v in sorted(st["K2"].items()):
        r = recs["K2_" + name]
        P(f"| K2 | {name} ({r['n_therm']} + {r['n_meas']}) | {v['seed']} | {v['value']:.6f} | {v['target']:.6f} | {100*v['dev']:+.3f} % | {'PASS' if v['pass'] else 'FAIL'} | {'yes' if v['bit_identical'] else 'no'} |")
    P()
    A = an["A"]
    for key in ("z4_8", "z4_12", "void_6", "void_8"):
        a = A[key]
        lt = a["L"] if a["kind"] == "z4" else 3 * a["L"]
        P(f"### {key}: {a['kind']} L = {a['L']} (L_t = {lt}), V = {a['V']:.0f}\n")
        P("**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)\n")
        P("| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |")
        P("|---|---|---|---|---|---|---|---|---|---|")
        for r in a["integrity"]["runs"]:
            tag = f"{key}_b{r['bn']:09d}_{r['role']}_c0"
            ms = recs[tag]["ms_per_sweep"]
            P(f"| {r['role']} | {r['bn']/U:.4f} | {r['seed']} | {r['E']:.5f} | {r['E_err']:.5f} | {r['span']:.5f} | {r['G']:.5f} | {0.25*r['G']:.5f} | {'ok' if r['ok'] else 'FAIL'} | {ms:.1f} |")
        S, W = a["S_line"], a["W_line"]
        P()
        P(f"- S(β) = {S['intercept0']:.6f} + ({S['slope']:.6f})·β; residuals {[round(x, 5) for x in S['resid']]}")
        P(f"- W(β) = {W['intercept0']:.6f} + ({W['slope']:.6f})·β; residuals {[round(x, 5) for x in W['resid']]}")
        ig = a["integrity"]
        P(f"- Integrity: **{'clean' if ig['ok'] else 'NOT CLEAN'}** (every span ≤ 0.25·G: {all(x['ok'] for x in ig['runs'])}; "
          f"S strictly decreasing: {ig['hot_monotone']}; W strictly decreasing: {ig['cold_monotone']}; G > 0 at every window point: {ig['window_gaps_positive']})")
        P()
        P("**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)\n")
        P("| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |")
        P("|---|---|---|---|---|---|---|---|")
        for r in a["rows"]:
            P(f"| {r['bn']/U:.4f} | {r['S']:.5f} | {r['W']:.5f} | {r['gap']:.5f} | {r['n']} | {r['phi']:.4f} | {r['phi_err']:.4f} | {r['frac_weak']:.3f} |")
        P()
        ext = st["ext"].get(key, [])
        P(f"- Grid [{a['grid'][0]/U:.4f}, {a['grid'][-1]/U:.4f}]; extensions: {', '.join(f'{b/U:.4f}' for b in ext) if ext else 'none'}; "
          f"bracketed: **{'yes' if a['bracketed'] else 'no'}**")
        P(f"- Probit: **β₅₀ = {a['b50']:.5f}**, w = {a['w']:.5f}, converged: **{a['fit_ok']}**; σ_boot = {a['sigma_boot']:.5f}, "
          f"**σ = {a['sigma']:.5f}**; bootstrap failures {a['boot_fail']}/{a['boot_n']}{' (FLAG > 5 %)' if a['boot_fail_flag'] else ''}")
        P()
    P("### Appendix A — every mixed chain\n")
    for key in ("z4_8", "z4_12", "void_6", "void_8"):
        a = A[key]
        P(f"**{key}**\n")
        P("| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |")
        P("|---|---|---|---|---|---|---|---|")
        for r in a["rows"]:
            Sb, Wb = r["S"], r["W"]
            for c, f in enumerate(r["f"]):
                rec = recs[f"{key}_b{r['bn']:09d}_mixed_c{c}"]
                fm = (Sb - rec["E_mid"]) / (Sb - Wb)
                P(f"| {r['bn']/U:.4f} | {c} | {rec['seed']} | {rec['E_end']:.5f} | {f:.4f} | {rec['E_mid']:.5f} | {fm:.4f} | {rec['ms_per_sweep']:.1f} |")
        P()


if __name__ == "__main__":
    main(sys.argv[1])
