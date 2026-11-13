"""
Gate DL-BETA P50 -- grids, seeds, estimators and rules (card sections 4.3-4.6, 5). Pre-registered with the card;
imported by dlbp_driver.py. Usage after the run:
    python -I dlbp_analysis.py numbers OUTDIR      -> OUTDIR/dlbp_numbers.txt, OUTDIR/analysis.json
    python -I dlbp_analysis.py verdict OUTDIR      -> OUTDIR/verdict.txt (refuses unless dlbp_numbers.sha256 exists)
"""
import json, math, os, sys
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import norm

U = 10 ** 7                         # beta held as integers in units of 1e-7
STEP = 25000                        # mixed-window step 0.0025
MAX_EXT = 2                         # extensions per lattice
N_BRANCH = (500, 1500)              # thermalisation, measurement sweeps (branch runs)
N_MIXED = 3000                      # sweeps per mixed-start chain
B_BOOT = 1000                       # bootstrap replicas
SIGMA_FLOOR = 0.0007                # one grid step's uniform sd, 0.0025/sqrt(12) rounded
U_SHARP = 0.0020                    # "sharpened" threshold on U
PRIOR_O = (12487500, 12587500)      # Gate DL-BETA, beta_inf +- u
PRIOR_R = (12562500, 12612500)      # Gate DL-BETA REP1, beta_inf +- u
Z4_K3 = (10051000, 10171000)        # K3 window (as REP1 K5)
Z4_LIT = 1.0111331                  # hep-lat/0210010

_S_Z4 = [9800000, 9850000, 9900000, 9950000]
_W_Z4 = [10200000, 10250000, 10300000, 10350000]
_S_V = [12300000, 12350000, 12400000, 12450000]
_W_V = [12650000, 12700000, 12750000, 12800000]
LATTICES = {
    "z4_8": dict(kind="z4", L=8, S=_S_Z4, W=_W_Z4, window=[10000000 + STEP * i for i in range(5)], chains=4),
    "z4_12": dict(kind="z4", L=12, S=_S_Z4, W=_W_Z4, window=[10050000 + STEP * i for i in range(5)], chains=4),
    "void_6": dict(kind="void", L=6, S=_S_V, W=_W_V, window=[12525000 + STEP * i for i in range(5)], chains=6),
    "void_8": dict(kind="void", L=8, S=_S_V, W=_W_V, window=[12525000 + STEP * i for i in range(5)], chains=6),
}
ORDER = ["z4_8", "z4_12", "void_6", "void_8"]

DRY = os.environ.get("DLBP_DRYRUN") == "1"     # dry run: code paths only (card section 7); never a gate result
if DRY:
    for _k, _L in (("z4_8", 4), ("z4_12", 6), ("void_6", 2), ("void_8", 3)):
        LATTICES[_k]["L"] = _L
    N_BRANCH, N_MIXED, B_BOOT = (20, 40), 1000, 50


def volume(kind, L):
    return float(L ** 4) if kind == "z4" else float(L ** 3 * 3 * L)


def seed(kind, L, bn, s, c):
    base = 3000000 if kind == "z4" else 4000000
    return base + 100000 * c + 7919 * L + round(1e4 * (bn / 1e7)) + s


def block_err(x, nb=20):
    x = np.asarray(x, dtype=float)
    assert len(x) % nb == 0
    bm = x.reshape(nb, -1).mean(axis=1)
    return float(np.std(bm, ddof=1) / np.sqrt(nb)), bm


def fit_line(bns, Es):
    x = np.array(bns, dtype=float) / U
    y = np.array(Es, dtype=float)
    xc = float(x.mean())
    A = np.vstack([np.ones_like(x), x - xc]).T
    (a, b), *_ = np.linalg.lstsq(A, y, rcond=None)
    return dict(xc=xc, a=float(a), slope=float(b), intercept0=float(a - b * xc),
                resid=[float(v - (a + b * (xx - xc))) for xx, v in zip(x, y)])


def line_at(line, bn):
    return line["a"] + line["slope"] * (bn / U - line["xc"])


def interp_crossings(bns, vals, level=0.5):
    out = []
    for i in range(len(bns) - 1):
        v0, v1 = vals[i], vals[i + 1]
        if (v0 <= level < v1) or (v0 > level >= v1):
            out.append(bns[i] + (level - v0) * (bns[i + 1] - bns[i]) / (v1 - v0))
    return out


def probit(bvals, fvals, x0):
    """least squares of chain-level f on Phi((beta - b50)/w); beta in units of 1. Returns (b50, w, ok)."""
    b = np.asarray(bvals, dtype=float)
    f = np.asarray(fvals, dtype=float)

    def r(p):
        return norm.cdf((b - p[0]) / math.exp(p[1])) - f
    try:
        res = least_squares(r, [x0, math.log(0.003)], method="trf", xtol=1e-12, ftol=1e-12, max_nfev=2000)
        b50, w = float(res.x[0]), float(math.exp(res.x[1]))
        ok = bool(res.success) and 1e-5 <= w <= 0.1 and (b.min() - 0.01) <= b50 <= (b.max() + 0.01)
        return b50, w, ok
    except Exception:
        return float("nan"), float("nan"), False


# ------------------------------------------------------------------------------------------------------------
def load_records(out):
    recs = {}
    d = os.path.join(out, "records")
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json"):
            r = json.load(open(os.path.join(d, fn)))
            recs[r["tag"]] = r
    return recs


def lattice_data(recs, key):
    br = {"hot": {}, "cold": {}}
    ch = {}
    for r in recs.values():
        if r.get("lat") != key:
            continue
        if r["role"] in ("hot", "cold"):
            br[r["role"]][r["bn"]] = r
        elif r["role"] == "mixed":
            ch.setdefault(r["bn"], []).append(r)
    for bn in ch:
        ch[bn].sort(key=lambda r: r["chain"])
    return br, ch


def branch_lines(br, spec):
    S = fit_line(spec["S"], [br["hot"][b]["E"] for b in spec["S"]])
    W = fit_line(spec["W"], [br["cold"][b]["E"] for b in spec["W"]])
    return S, W


def phi_table(ch, S, W, which="E_end"):
    rows = []
    for bn in sorted(ch):
        Sb, Wb = line_at(S, bn), line_at(W, bn)
        fs = [(Sb - r[which]) / (Sb - Wb) for r in ch[bn]]
        rows.append(dict(bn=bn, S=Sb, W=Wb, gap=Sb - Wb, f=fs, phi=float(np.mean(fs)),
                         phi_err=float(np.std(fs, ddof=1) / np.sqrt(len(fs))) if len(fs) > 1 else float("nan"),
                         frac_weak=float(np.mean([x > 0.5 for x in fs])), n=len(fs)))
    return rows


def extensions_needed(rows):
    """card 4.4: phi at the lowest window point > 1/2 -> one step below; phi at the highest < 1/2 -> one above."""
    need = []
    if rows[0]["phi"] > 0.5:
        need.append(rows[0]["bn"] - STEP)
    if rows[-1]["phi"] < 0.5:
        need.append(rows[-1]["bn"] + STEP)
    return need


def integrity(br, spec, S, W):
    """card 4.5: every branch run's 20 block means span <= 0.25 G(beta); each branch strictly decreasing in beta;
    G > 0 at every branch and window point."""
    out = dict(ok=True, runs=[])
    for role, pts, ln in (("hot", spec["S"], S), ("cold", spec["W"], W)):
        Es = [br[role][b]["E"] for b in pts]
        mono = all(Es[i] > Es[i + 1] for i in range(len(Es) - 1))
        if not mono:
            out["ok"] = False
        for b in pts:
            r = br[role][b]
            G = line_at(S, b) - line_at(W, b)
            span = max(r["block_means"]) - min(r["block_means"])
            ok = G > 0 and span <= 0.25 * G
            out["runs"].append(dict(role=role, bn=b, E=r["E"], E_err=r["E_err"], span=span, G=G, ok=bool(ok), seed=r["seed"]))
            if not ok:
                out["ok"] = False
        out[f"{role}_monotone"] = bool(mono)
    return out


def analyse_lattice(recs, key, boot=B_BOOT, dry=False):
    spec = LATTICES[key]
    br, ch = lattice_data(recs, key)
    S, W = branch_lines(br, spec)
    integ = integrity(br, spec, S, W)
    rows = phi_table(ch, S, W)
    grid = [r["bn"] for r in rows]
    gaps_ok = all(r["gap"] > 0 for r in rows)
    integ["ok"] = integ["ok"] and gaps_ok
    integ["window_gaps_positive"] = bool(gaps_ok)
    bracketed = rows[0]["phi"] <= 0.5 <= rows[-1]["phi"]
    xs = interp_crossings(grid, [r["phi"] for r in rows])
    x0 = (np.mean(xs) if xs else 0.5 * (grid[0] + grid[-1])) / U
    bv = [r["bn"] / U for r in rows for _ in r["f"]]
    fv = [x for r in rows for x in r["f"]]
    b50, w, ok = probit(bv, fv, x0)
    # bootstrap: chains resampled within beta; branch points redrawn from their 20-block errors
    seed_b = (52000 if spec["kind"] == "z4" else 51000) + spec["L"]
    rng = np.random.default_rng(seed_b)
    reps, nfail = [], 0
    for _ in range(boot):
        Sb = fit_line(spec["S"], [br["hot"][b]["E"] + br["hot"][b]["E_err"] * rng.standard_normal() for b in spec["S"]])
        Wb = fit_line(spec["W"], [br["cold"][b]["E"] + br["cold"][b]["E_err"] * rng.standard_normal() for b in spec["W"]])
        bb, ff = [], []
        for bn in grid:
            cs = ch[bn]
            idx = rng.integers(0, len(cs), len(cs))
            s_, w_ = line_at(Sb, bn), line_at(Wb, bn)
            for i in idx:
                bb.append(bn / U)
                ff.append((s_ - cs[i]["E_end"]) / (s_ - w_))
        x, _, okb = probit(bb, ff, b50 if ok else x0)
        if okb:
            reps.append(x)
        else:
            nfail += 1
    sboot = float(np.std(reps, ddof=1)) if len(reps) > 1 else float("nan")
    sigma = max(sboot, SIGMA_FLOOR) if sboot == sboot else float("nan")
    # diagnostics (reported, not verdict inputs)
    rows_mid = phi_table(ch, S, W, which="E_mid")
    bmid, wmid, okmid = probit([r["bn"] / U for r in rows_mid for _ in r["f"]], [x for r in rows_mid for x in r["f"]], x0)
    xfrac = interp_crossings(grid, [r["frac_weak"] for r in rows])
    return dict(key=key, kind=spec["kind"], L=spec["L"], V=volume(spec["kind"], spec["L"]), S_line=S, W_line=W,
                integrity=integ, rows=rows, grid=grid, bracketed=bool(bracketed),
                b50=b50, w=w, fit_ok=bool(ok), sigma_boot=sboot, sigma=sigma, boot_fail=nfail, boot_n=boot,
                boot_fail_flag=bool(nfail > 0.05 * boot),
                interp_cross=[x / U for x in xs], nonmonotone=bool(len(xs) > 1),
                frac_cross=[x / U for x in xfrac], b50_mid=bmid, mid_ok=bool(okmid),
                drift=(b50 - bmid) if (ok and okmid) else float("nan"))


def extrapolate(a_small, a_big):
    """first-order 1/V extrapolation through two sizes; U = sqrt(sigma_inf^2 + shift^2)."""
    xs, xb = 1.0 / a_small["V"], 1.0 / a_big["V"]
    k = xb / (xs - xb)
    shift = -k * (a_small["b50"] - a_big["b50"])
    binf = a_big["b50"] + shift
    sinf = math.sqrt(((1 + k) * a_big["sigma"]) ** 2 + (k * a_small["sigma"]) ** 2)
    Uc = math.sqrt(sinf ** 2 + shift ** 2)
    return dict(k=k, beta_inf=binf, sigma_inf=sinf, shift=shift, U=Uc, inv_e2=binf / math.sqrt(2), inv_e2_U=Uc / math.sqrt(2))


def fmt(x, d=5):
    return "none" if x is None or x != x else f"{x:.{d}f}"


def numbers(out, boot=B_BOOT, dry=False):
    recs = load_records(out)
    st = json.load(open(os.path.join(out, "state.json")))
    A = {k: analyse_lattice(recs, k, boot=boot, dry=dry) for k in ORDER}
    ex_v = extrapolate(A["void_6"], A["void_8"])
    ex_z = extrapolate(A["z4_8"], A["z4_12"])
    L = []
    w = L.append
    w("# Gate DL-BETA P50 -- dlbp_numbers.txt (written before any comparison with the prior gates)")
    w("# beta in card convention; 1/e^2 = beta/sqrt2 on the void complex. f = (S - E_end)/(S - W).")
    k2 = st.get("K2", {})
    for name, v in sorted(k2.items()):
        w(f"K2 {name}: value = {v['value']:.6f}; target = {v['target']:.6f}; dev = {100*v['dev']:+.3f}%; pass = {'yes' if v['pass'] else 'no'}; "
          f"bit-identical to REP1 series = {'yes' if v.get('bit_identical') else 'no'}")
    for key in ORDER:
        a = A[key]
        w(f"[{key}] {a['kind']} L = {a['L']}, V = {a['V']:.0f}")
        w(f"  S(beta) = {a['S_line']['intercept0']:.6f} + ({a['S_line']['slope']:.6f}) beta ; resid {[round(x, 5) for x in a['S_line']['resid']]}")
        w(f"  W(beta) = {a['W_line']['intercept0']:.6f} + ({a['W_line']['slope']:.6f}) beta ; resid {[round(x, 5) for x in a['W_line']['resid']]}")
        for r in a["integrity"]["runs"]:
            w(f"  branch {r['role']:4s} beta {r['bn']/U:.4f} seed {r['seed']}: E = {r['E']:.5f} +- {r['E_err']:.5f}; span {r['span']:.5f} <= 0.25 G {0.25*r['G']:.5f}: {'ok' if r['ok'] else 'FAIL'}")
        w(f"  integrity = {'ok' if a['integrity']['ok'] else 'FAIL'} (hot monotone {a['integrity']['hot_monotone']}, cold monotone {a['integrity']['cold_monotone']}, window gaps > 0 {a['integrity']['window_gaps_positive']})")
        for r in a["rows"]:
            w(f"  beta {r['bn']/U:.4f}: S {r['S']:.5f} W {r['W']:.5f}; phi = {r['phi']:.4f} +- {r['phi_err']:.4f} (n {r['n']}); frac_weak {r['frac_weak']:.3f}; f = {[round(x, 4) for x in r['f']]}")
        w(f"  grid = [{a['grid'][0]/U:.4f}, {a['grid'][-1]/U:.4f}]; extensions = {st['ext'].get(key, [])}; bracketed = {'yes' if a['bracketed'] else 'no'}")
        w(f"  beta_50 = {fmt(a['b50'])}; w = {fmt(a['w'])}; fit_ok = {a['fit_ok']}; sigma_boot = {fmt(a['sigma_boot'])}; sigma = {fmt(a['sigma'])}; "
          f"boot failures {a['boot_fail']}/{a['boot_n']}{' FLAG' if a['boot_fail_flag'] else ''}")
        w(f"  check: interp crossing(s) of phi = {[round(x, 5) for x in a['interp_cross']]}{' NON-MONOTONE' if a['nonmonotone'] else ''}; "
          f"frac_weak crossing(s) = {[round(x, 5) for x in a['frac_cross']]}; beta_50(mid, sweeps 1050-1500) = {fmt(a['b50_mid'])}; drift = {fmt(a['drift'])}")
    for nm, ex in (("void (L = 6, 8)", ex_v), ("Z4 (L = 8, 12)", ex_z)):
        w(f"extrapolation {nm}: k = {ex['k']:.4f}; beta_inf = {ex['beta_inf']:.5f}; sigma_inf = {ex['sigma_inf']:.5f}; shift = {ex['shift']:+.5f}; U = {ex['U']:.5f}")
    if A["void_6"]["fit_ok"] and A["void_8"]["fit_ok"]:
        w(f"RESULT beta_c = {ex_v['beta_inf']:.5f} +- {ex_v['U']:.5f} (card convention); 1/e^2_c = {ex_v['inv_e2']:.5f} +- {ex_v['inv_e2_U']:.5f}")
    else:
        w("RESULT beta_c = not defined (a void probit fit failed)")
    if A["z4_8"]["fit_ok"] and A["z4_12"]["fit_ok"]:
        w(f"Z4 calibration: beta_inf(Z4) - {Z4_LIT} = {ex_z['beta_inf'] - Z4_LIT:+.5f} = {(ex_z['beta_inf'] - Z4_LIT)/ex_z['U']:+.2f} U")
    else:
        w("Z4 calibration: not defined (a Z4 probit fit failed)")
    txt = "\n".join(L) + "\n"
    open(os.path.join(out, "dlbp_numbers.txt"), "w").write(txt)
    json.dump(dict(A=A, ex_void=ex_v, ex_z4=ex_z), open(os.path.join(out, "analysis.json"), "w"), indent=1, default=float)
    print(txt)
    return A, ex_v, ex_z


def verdict(out):
    if not os.path.exists(os.path.join(out, "dlbp_numbers.sha256")):
        sys.exit("refusing: hash dlbp_numbers.txt first (card 4.7)")
    st = json.load(open(os.path.join(out, "state.json")))
    an = json.load(open(os.path.join(out, "analysis.json")))
    A, ex = an["A"], an["ex_void"]
    z12 = A["z4_12"]
    k2_ok = all(v["pass"] for v in st["K2"].values())
    k1_ok = bool(st.get("K1", {}).get("pass"))
    k3_ok = z12["integrity"]["ok"] and z12["bracketed"] and z12["fit_ok"] and Z4_K3[0] / U <= z12["b50"] <= Z4_K3[1] / U
    void_ok = all(A[k]["integrity"]["ok"] and A[k]["bracketed"] and A[k]["fit_ok"] for k in ("void_6", "void_8"))
    lo, hi = ex["beta_inf"] - 2 * ex["U"], ex["beta_inf"] + 2 * ex["U"]
    ovO = lo <= PRIOR_O[1] / U and hi >= PRIOR_O[0] / U
    ovR = lo <= PRIOR_R[1] / U and hi >= PRIOR_R[0] / U

    def dist(x, I):
        a, b = I[0] / U, I[1] / U
        return 0.0 if a <= x <= b else min(abs(x - a), abs(x - b))
    if not (k1_ok and k2_ok and k3_ok):
        code = "SC-DLBP-0"
    elif not void_ok:
        code = "SC-DLBP-4"
    elif ex["U"] > U_SHARP:
        code = "SC-DLBP-3"
    elif not (ovO and ovR):
        code = "SC-DLBP-2"
    else:
        code = "SC-DLBP-1"
    L = [f"K1 {k1_ok}; K2 {k2_ok}; K3 (Z4 L=12 beta_50 = {z12['b50']:.5f} in [1.0051, 1.0171], clean, bracketed, fit) {k3_ok}",
         f"void L=6, L=8 clean, bracketed, fit: {void_ok}",
         f"beta_c = {ex['beta_inf']:.5f} +- {ex['U']:.5f}; U <= {U_SHARP}: {ex['U'] <= U_SHARP}",
         f"beta_c +- 2U = [{lo:.5f}, {hi:.5f}]; overlaps Gate DL-BETA [1.24875, 1.25875]: {ovO}; overlaps REP1 [1.25625, 1.26125]: {ovR}",
         f"distance of beta_c to Gate DL-BETA interval = {dist(ex['beta_inf'], PRIOR_O):.5f} ({dist(ex['beta_inf'], PRIOR_O)/ex['U']:.2f} U); "
         f"to REP1 interval = {dist(ex['beta_inf'], PRIOR_R):.5f} ({dist(ex['beta_inf'], PRIOR_R)/ex['U']:.2f} U)",
         f"VERDICT {code}"]
    txt = "\n".join(L) + "\n"
    open(os.path.join(out, "verdict.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    cmd, out = sys.argv[1], sys.argv[2]
    dry = os.environ.get("DLBP_DRYRUN") == "1"
    if cmd == "numbers":
        numbers(out, boot=B_BOOT, dry=dry)
    elif cmd == "verdict":
        verdict(out)
