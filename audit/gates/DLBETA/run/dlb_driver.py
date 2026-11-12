"""Gate DL-BETA -- stage driver.  Applies card sections 4.3-4.4 mechanically, in order, reading each
stage's numbers from the previous one.  Resumable: a run whose raw files exist is not rerun; every
decision is recomputed deterministically from the raw records.  Written before any Monte Carlo run
at beta in [0.2, 5].

Usage: nohup python3 -I dlb_driver.py OUTDIR > OUTDIR/driver.log 2>&1 &

Readings of the card's wording, fixed here before the runs they affect:
 R1  "within 0.05 of an edge" (4.4 step 1): |beta0 - edge| <= 0.05.
 R2  Seeds: 7919*L + round(1e4*beta) + s (+500000 void), Python round() on the float 1e4*beta
     (ties half to even, as CRIT2 did); every seed is stored in the raw records.
 R3  Mixed-start readings: E after sweeps 50, 100, ..., 2000; "the 10 readings at sweeps 1550-2000"
     = sweeps 1550, 1600, ..., 2000.  "End-state E" for Delta E = the same 10-reading mean (the final
     sweep value is also stored).
 R4  Z4 mixed start (K5 = CRIT2 check 4): links whose origin site has x1 (first coordinate) < L/2.
 R5  K5 passes iff the flip interval [highest strong win, lowest weak win] meets [1.0051, 1.0171].
     No flip among the five fixed points = K5 fails.
 R6  beta_mix with a non-monotonic outcome pattern: the interval is [min(S, W), max(S, W)] with S the
     highest strong-win beta and W the lowest weak-win beta; flagged as non-monotonic.
 R7  "Two peaks" in the step-6 histogram (50 equal bins over [min E, max E] of the 20,000 measurement
     sweeps): a peak is a bin whose count is the maximum of the bins within +-5 of it (first bin of a
     plateau) and at least 10 % of the largest count; two peaks iff two such bins exist with a bin
     between them whose count is below half the smaller of the two.
 R8  Hysteresis (4.4 step 7a) at L = 4: hot and cold jump intervals differ, or |E_hot - E_cold| >
     3 sqrt(err_hot^2 + err_cold^2) at some grid point (20-block errors).
 R9  Order (7b): jump at L = 4 = the fall in E across the cold-start jump interval; at L = 6 the fall
     across the cold-scan jump interval; at L = 8 Delta E.  "Shrinks by more than 30 %" iff
     Delta E(8) < 0.7 * jump(4).
 R10 Scheduling: step 6 (histogram) depends only on beta_mix(6) and is launched together with the
     L = 8 mixed runs of step 4; every run is an independent seeded chain, so scheduling cannot change
     any number.
"""
import os, sys, json, time, math
import multiprocessing as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlb_sim as S

OUT = os.path.abspath(sys.argv[1])
RAW = os.path.join(OUT, "raw")
os.makedirs(RAW, exist_ok=True)
STATE = os.path.join(OUT, "state.json")
NCORES = 2

I1I0_01 = 0.04993760398793892   # I1(0.1)/I0(0.1) (scipy), checked below; card rounds it to 0.049938
TARGET20 = {("void", 2): 0.014258, ("z4", 4): 0.012451}
RANKS = {("void", 2, 6): 1533, ("z4", 4, None): 765}


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def load_state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}


def save_state(st):
    tmp = STATE + ".tmp"
    json.dump(st, open(tmp, "w"), indent=1)
    os.replace(tmp, STATE)


def grid(lo, hi, step):
    n = int(round((hi - lo) / step))
    return [round(lo + i * step, 6) for i in range(n + 1)]


def seed_of(lattice, L, beta, s):
    return int(7919 * L + round(1e4 * beta) + s + (500000 if lattice == "void" else 0))


SVAL = {"hot": 0, "cold": 1, "mixed": 2, "hist": 3}


def spec(stage, lattice, L, Lt, beta, start, n_therm, n_meas, s=None):
    s = SVAL[start] if s is None else s
    st = "mixed" if start == "hist" else start
    tag = f"{lattice}_L{L}_b{beta:.5f}_{start}"
    return dict(stage=stage, tag=tag, lattice=lattice, L=L, Lt=Lt, beta=float(beta), start=st, s=s,
                seed=seed_of(lattice, L, beta, s), n_therm=n_therm, n_meas=n_meas,
                n_sweeps=n_therm + n_meas)


def _paths(sp):
    d = os.path.join(RAW, sp["stage"])
    return os.path.join(d, sp["tag"] + ".json"), os.path.join(d, sp["tag"] + ".npz")


def _worker(sp):
    jp, npth = _paths(sp)
    os.makedirs(os.path.dirname(jp), exist_ok=True)
    rec, ser = S.run_job(sp)
    np.savez(npth + ".tmp.npz", **ser)
    os.replace(npth + ".tmp.npz", npth)
    json.dump(rec, open(jp + ".tmp", "w"))
    os.replace(jp + ".tmp", jp)
    return sp["tag"], rec["wall_s"]


def run_specs(specs):
    """Run all specs not yet on disk (2 at a time); return {tag: (record, series)} for all."""
    todo = [sp for sp in specs if not all(os.path.exists(p) for p in _paths(sp))]
    if todo:
        log(f"  running {len(todo)} of {len(specs)} runs ({specs[0]['stage']})")
        ctx = mp.get_context("fork")
        with ctx.Pool(NCORES) as pool:
            for tag, w in pool.imap_unordered(_worker, todo):
                log(f"    done {tag}  {w:.1f} s")
    out = {}
    for sp in specs:
        jp, npth = _paths(sp)
        rec = json.load(open(jp))
        z = np.load(npth)
        out[sp["tag"]] = (rec, {k: z[k] for k in z.files})
    return out


def scan_stats(rec, ser):
    n0, nl = rec["n_therm"], rec["n_loops"]
    r = {}
    for key in ("E", "Es", "Et"):
        x = ser[key][n0:]
        bm = np.array([b.mean() for b in np.array_split(x, 20)])
        r[key] = float(x.mean())
        r[key + "_err"] = float(bm.std(ddof=1) / math.sqrt(20))
    x = ser["E"][n0:]
    blocks = np.array_split(x, 20)
    r["C"] = float(nl * x.var())
    cj = np.array([nl * np.concatenate([blocks[j] for j in range(20) if j != i]).var() for i in range(20)])
    r["C_err"] = float(math.sqrt(19 / 20 * ((cj - cj.mean()) ** 2).sum()))
    return r


def readings(ser):
    E = ser["E"]
    return [float(E[50 * k - 1]) for k in range(1, len(E) // 50 + 1)]


def mixed_outcome(ser, Estar):
    rd = readings(ser)
    m = float(np.mean(rd[30:40]))          # sweeps 1550..2000
    Es = float(np.mean([ser["Es"][50 * k - 1] for k in range(31, 41)]))
    Et = float(np.mean([ser["Et"][50 * k - 1] for k in range(31, 41)]))
    if m < Estar - 0.01:
        o = "weak"
    elif m > Estar + 0.01:
        o = "strong"
    else:
        o = "unresolved"
    return o, m, Es, Et, rd


def jump_interval(betas, E):
    falls = [E[i] - E[i + 1] for i in range(len(betas) - 1)]
    i = int(np.argmax(falls))
    return [betas[i], betas[i + 1]], float(falls[i]), [float(E[i]), float(E[i + 1])]


def beta_mix(outs):
    """outs: {beta: outcome}.  Returns dict or None if no flip."""
    bs = sorted(outs)
    strong = [b for b in bs if outs[b] == "strong"]
    weak = [b for b in bs if outs[b] == "weak"]
    if not strong or not weak:
        return None
    Sb, Wb = max(strong), min(weak)
    lo, hi = min(Sb, Wb), max(Sb, Wb)
    mono = all(outs[b] != "weak" for b in bs if b < Sb) and all(outs[b] != "strong" for b in bs if b > Wb) \
        and Sb < Wb
    unres_between = [b for b in bs if lo < b < hi and outs[b] == "unresolved"]
    return dict(S=Sb, W=Wb, interval=[lo, hi], beta_mix=round((Sb + Wb) / 2, 7), monotonic=mono,
                unresolved_all=[b for b in bs if outs[b] == "unresolved"], unresolved_between=unres_between)


def mixed_stage(stage, lattice, L, Lt, betas, Estar, max_ext=8):
    """Card 4.4 step 4 (and CRIT2 5.4): run grid, extend by 0.0025 if no flip, at most max_ext times."""
    betas = list(betas)
    ext = 0
    while True:
        res = run_specs([spec(stage, lattice, L, Lt, b, "mixed", 0, 2000) for b in betas])
        outs, rows = {}, []
        for b in betas:
            rec, ser = res[f"{lattice}_L{L}_b{b:.5f}_mixed"]
            o, m, Es, Et, rd = mixed_outcome(ser, Estar)
            outs[b] = o
            rows.append(dict(beta=b, seed=rec["seed"], E_start=rec["E_start"], E_last10=m, E_final=rec["E_final"],
                             Es_last10=Es, Et_last10=Et, outcome=o, readings=rd))
        bm = beta_mix(outs)
        if bm is not None or max_ext is None:
            break
        if ext >= max_ext:
            break
        if not any(v == "weak" for v in outs.values()):
            betas.append(round(max(betas) + 0.0025, 6))
        else:
            betas.insert(0, round(min(betas) - 0.0025, 6))
        ext += 1
        log(f"  {stage}: no flip; extension {ext}: now {betas}")
    rows.sort(key=lambda r: r["beta"])
    return dict(rows=rows, beta_mix=bm, extensions=ext, Estar=Estar)


def scan(stage, lattice, L, Lt, betas, starts, n_therm, n_meas):
    specs = [spec(stage, lattice, L, Lt, b, st, n_therm, n_meas) for b in betas for st in starts]
    res = run_specs(specs)
    table = {}
    for b in betas:
        for st in starts:
            rec, ser = res[f"{lattice}_L{L}_b{b:.5f}_{st}"]
            r = scan_stats(rec, ser)
            r.update(seed=rec["seed"], E_final=rec["E_final"])
            table.setdefault(b, {})[st] = r
    return table


def write_jsonl(name, table_rows):
    with open(os.path.join(OUT, name), "w") as f:
        for r in table_rows:
            f.write(json.dumps(r) + "\n")


def halt(st, code, why):
    st["HALT"] = dict(code=code, why=why)
    save_state(st)
    log(f"HALT {code}: {why}")
    sys.exit(2)


def main():
    from scipy.special import i0, i1
    assert abs(i1(0.1) / i0(0.1) - I1I0_01) < 1e-14
    st = load_state()
    log(f"driver start; OUT = {OUT}")

    # ---------------- K2: gauge invariance and local dS (deterministic) ----------------
    k2 = {}
    for name, (lat, L, Lt) in (("void L=2 Lt=6", ("void", 2, 6)), ("Z4 L=4", ("z4", 4, None))):
        a = S.get_complex(lat, L, Lt)
        rng = np.random.default_rng(20261112)
        th = rng.uniform(0, 2 * np.pi, a["n_links"])
        lam = rng.uniform(0, 2 * np.pi, a["n_nodes"])
        th2 = th + lam[a["org"]] - lam[a["tgt"]]
        dev = float(np.abs(S.loop_cos(th, a["LL"], a["LS"]) - S.loop_cos(th2, a["LL"], a["LS"])).max())
        Sg = lambda t: np.sum(1 - S.loop_cos(t, a["LL"], a["LS"]))
        worst = 0.0
        for l in rng.choice(a["n_links"], 100, replace=False):
            R, phi = S.staple(th, l, a["LL"], a["LS"], a["ptr"], a["il"], a["isg"])
            new = th.copy(); new[l] = rng.uniform(0, 2 * np.pi)
            worst = max(worst, abs(-R * (np.cos(new[l] + phi) - np.cos(th[l] + phi)) - (Sg(new) - Sg(th))))
        k2[name] = dict(gauge_max_dcos=dev, local_vs_global_max=float(worst),
                        pass_=bool(dev < 1e-10 and worst < 1e-9))
        log(f"K2 {name}: gauge max|dcos| = {dev:.1e}, local-vs-global {worst:.1e}")
    st["K2"] = k2
    save_state(st)
    if not all(v["pass_"] for v in k2.values()):
        halt(st, "SC-DLB-0", "K2 failed")

    # ---------------- K3: limits ----------------
    specs = []
    for lat, L, Lt in (("void", 2, 6), ("z4", 4, None)):
        specs.append(spec("K3", lat, L, Lt, 0.1, "hot", 1000, 10000))
        specs.append(spec("K3", lat, L, Lt, 20.0, "cold", 1000, 10000))
    res = run_specs(specs)
    k3 = {}
    for sp in specs:
        rec, ser = res[sp["tag"]]
        r = scan_stats(rec, ser)
        if sp["beta"] == 0.1:
            m, e, tgt = 1 - r["E"], r["E_err"], I1I0_01
        else:
            m, e = r["E"], r["E_err"]
            tgt = RANKS[(sp["lattice"], sp["L"], sp["Lt"])] / (2 * 20.0 * rec["n_loops"])
        dev = (m - tgt) / tgt
        k3[sp["tag"]] = dict(lattice=sp["lattice"], L=sp["L"], Lt=sp["Lt"], beta=sp["beta"], start=sp["start"],
                             seed=sp["seed"], measured=m, err=e, target=tgt, rel_dev=dev,
                             Es=r["Es"], Es_err=r["Es_err"], Et=r["Et"], Et_err=r["Et_err"],
                             pass_=bool(abs(dev) < 0.02))
        log(f"K3 {sp['tag']}: {m:.6f} +- {e:.6f} vs {tgt:.6f} ({100*dev:+.2f} %)")
    st["K3"] = k3
    save_state(st)
    if not all(v["pass_"] for v in k3.values()):
        halt(st, "SC-DLB-0", "K3 failed")

    # ---------------- K4: Z4 L = 8 transition ----------------
    b4 = grid(0.995, 1.020, 0.0025)
    t4 = scan("K4", "z4", 8, None, b4, ("hot", "cold"), 1000, 3000)
    Cmax = {b: max(t4[b]["hot"]["C"], t4[b]["cold"]["C"]) for b in b4}
    bC = max(b4, key=lambda b: Cmax[b])
    ji, fall, ends = jump_interval(b4, [t4[b]["cold"]["E"] for b in b4])
    Ehc = float(np.mean(ends))
    k4 = dict(table={str(b): t4[b] for b in b4}, beta_Cmax=bC, Cmax=Cmax[bC],
              cold_jump=ji, cold_fall=fall, E_star_hc=Ehc, pass_=bool(1.000 - 1e-9 <= bC <= 1.012 + 1e-9))
    st["K4"] = k4
    save_state(st)
    log(f"K4: C max at {bC} (C = {Cmax[bC]:.3f}); cold jump {ji} fall {fall:.5f}; E*_hc = {Ehc:.5f}; pass {k4['pass_']}")
    if not k4["pass_"]:
        halt(st, "SC-DLB-0", "K4 failed")

    # ---------------- K5: Z4 L = 12 mixed phase ----------------
    k5 = mixed_stage("K5", "z4", 12, None, [1.002, 1.007, 1.012, 1.017, 1.022], Ehc, max_ext=0)
    bm = k5["beta_mix"]
    ok5 = bm is not None and bm["interval"][0] <= 1.0171 + 1e-9 and bm["interval"][1] >= 1.0051 - 1e-9
    k5["pass_"] = bool(ok5)
    st["K5"] = k5
    save_state(st)
    log(f"K5: {[(r['beta'], r['outcome'], round(r['E_last10'], 5)) for r in k5['rows']]} -> {bm}; pass {ok5}")
    if not ok5:
        halt(st, "SC-DLB-0", "K5 failed")
    log("K2-K5 all pass")

    # ================= void runs (card 4.4) =================
    # step 1 -- locate, L = 2, Lt = 6
    lo, hi = 0.50, 2.00
    while True:
        b1 = grid(lo, hi, 0.01)
        t1 = scan("S1_locate", "void", 2, 6, b1, ("hot", "cold"), 500, 2000)
        Cm = {b: max(t1[b]["hot"]["C"], t1[b]["cold"]["C"]) for b in b1}
        beta0 = max(b1, key=lambda b: Cm[b])
        st["S1"] = dict(range=[lo, hi], beta0=beta0, Cmax=Cm[beta0],
                        beta0_start="hot" if t1[beta0]["hot"]["C"] >= t1[beta0]["cold"]["C"] else "cold",
                        table={str(b): t1[b] for b in b1})
        save_state(st)
        log(f"S1: range [{lo}, {hi}], beta0 = {beta0} (C = {Cm[beta0]:.3f})")
        moved = False
        if beta0 - lo <= 0.05 + 1e-9:
            if lo <= 0.20 + 1e-9:
                halt(st, "SC-DLB-3", "no interior C maximum in [0.20, 4.00] (low edge)")
            lo = round(max(0.20, lo - 0.25), 6); moved = True
        elif hi - beta0 <= 0.05 + 1e-9:
            if hi >= 4.00 - 1e-9:
                halt(st, "SC-DLB-3", "no interior C maximum in [0.20, 4.00] (high edge)")
            hi = round(min(4.00, hi + 0.25), 6); moved = True
        if not moved:
            break
        log(f"S1: beta0 within 0.05 of an edge; extending to [{lo}, {hi}]")

    # step 2 -- fine scan, L = 4, Lt = 12
    lo, hi = round(beta0 - 0.050, 6), round(beta0 + 0.050, 6)
    while True:
        b2 = grid(lo, hi, 0.005)
        t2 = scan("S2_fine", "void", 4, 12, b2, ("hot", "cold"), 2000, 4000)
        Cm = {b: max(t2[b]["hot"]["C"], t2[b]["cold"]["C"]) for b in b2}
        beta4 = max(b2, key=lambda b: Cm[b])
        if beta4 == b2[0]:
            lo = round(lo - 0.005, 6); log(f"S2: beta4 at low edge; extend to {lo}"); continue
        if beta4 == b2[-1]:
            hi = round(hi + 0.005, 6); log(f"S2: beta4 at high edge; extend to {hi}"); continue
        break
    jh = jump_interval(b2, [t2[b]["hot"]["E"] for b in b2])
    jc = jump_interval(b2, [t2[b]["cold"]["E"] for b in b2])
    st["S2"] = dict(range=[lo, hi], beta4=beta4, Cmax=Cm[beta4],
                    beta4_start="hot" if t2[beta4]["hot"]["C"] >= t2[beta4]["cold"]["C"] else "cold",
                    jump_hot=jh[0], fall_hot=jh[1], ends_hot=jh[2], jump_cold=jc[0], fall_cold=jc[1],
                    ends_cold=jc[2], table={str(b): t2[b] for b in b2})
    save_state(st)
    log(f"S2: beta4 = {beta4}; jump hot {jh[0]} ({jh[1]:.5f}), cold {jc[0]} ({jc[1]:.5f})")

    # step 3 -- cold scan, L = 6, Lt = 18
    b3 = grid(round(beta4 - 0.020, 6), round(beta4 + 0.020, 6), 0.005)
    t3 = scan("S3_cold", "void", 6, 18, b3, ("cold",), 500, 1500)
    j6 = jump_interval(b3, [t3[b]["cold"]["E"] for b in b3])
    Estar = float(np.mean(j6[2]))
    st["S3"] = dict(jump=j6[0], fall=j6[1], ends=j6[2], Estar=Estar, table={str(b): t3[b] for b in b3})
    save_state(st)
    log(f"S3: L=6 jump {j6[0]} fall {j6[1]:.5f}; E* = {Estar:.5f}")

    # step 4 -- mixed, L = 6
    c6 = round((j6[0][0] + j6[0][1]) / 2, 6)
    m6 = mixed_stage("S4_mixed6", "void", 6, 18, [round(c6 + j * 0.0025, 6) for j in range(-3, 4)], Estar)
    st["S4_L6"] = m6
    save_state(st)
    log(f"S4 L=6: {[(r['beta'], r['outcome']) for r in m6['rows']]} -> {m6['beta_mix']}")
    if m6["beta_mix"] is None:
        st["S4_L6"]["stopped"] = True
        halt(st, "SC-DLB-2", "L = 6 mixed phase did not flip within 8 extensions")
    bmix6 = m6["beta_mix"]["beta_mix"]

    # step 6 (scheduled with step 4 L = 8; R10) -- histogram, L = 6, at beta_mix(6)
    hsp = spec("S6_hist", "void", 6, 18, bmix6, "hist", 2000, 20000)
    # step 4 -- mixed, L = 8 (histogram queued first so the long run starts at once)
    b8 = [round(bmix6 + j * 0.0025, 6) for j in range(-2, 3)]
    pre = [hsp] + [spec("S4_mixed8", "void", 8, 24, b, "mixed", 0, 2000) for b in b8]
    run_specs_multi(pre)
    m8 = mixed_stage("S4_mixed8", "void", 8, 24, b8, Estar)
    st["S4_L8"] = m8
    save_state(st)
    log(f"S4 L=8: {[(r['beta'], r['outcome']) for r in m8['rows']]} -> {m8['beta_mix']}")

    # step 5 -- result
    res5 = {}
    if m8["beta_mix"] is not None:
        bm8 = m8["beta_mix"]
        binf = bm8["beta_mix"]
        unc = max((bm8["interval"][1] - bm8["interval"][0]) / 2, abs(binf - bmix6))
        rows8 = m8["rows"]
        sb = [r for r in rows8 if r["outcome"] == "strong" and r["beta"] < binf]
        wb = [r for r in rows8 if r["outcome"] == "weak" and r["beta"] > binf]
        rs = max(sb, key=lambda r: r["beta"]) if sb else None
        rw = min(wb, key=lambda r: r["beta"]) if wb else None
        dE = (rs["E_last10"] - rw["E_last10"]) if rs and rw else None
        dEf = (rs["E_final"] - rw["E_final"]) if rs and rw else None
        x6, x8 = 1 / (6 ** 3 * 18), 1 / (8 ** 3 * 24)
        lin0 = binf - x8 * (bmix6 - binf) / (x6 - x8)
        res5 = dict(beta_inf=binf, unc=unc, inv_e2c=binf / math.sqrt(2), inv_e2c_unc=unc / math.sqrt(2),
                    dE=dE, dE_final=dEf, dE_runs=[rs["beta"] if rs else None, rw["beta"] if rw else None],
                    lin_extrap_0=lin0, half_flip8=(bm8["interval"][1] - bm8["interval"][0]) / 2,
                    shift_6_8=abs(binf - bmix6))
    st["S5"] = res5
    save_state(st)
    log(f"S5: {res5}")

    # step 6 -- histogram analysis
    res = run_specs([hsp])
    rec, ser = res[hsp["tag"]]
    x = ser["E"][2000:]
    h, edges = np.histogram(x, bins=50, range=(float(x.min()), float(x.max())))
    B = float(1 - np.mean(x ** 4) / (3 * np.mean(x ** 2) ** 2))
    st["S6"] = dict(beta=bmix6, seed=rec["seed"], counts=h.tolist(), edges=edges.tolist(), binder=B,
                    two_peaks=two_peaks(h), E_mean=float(x.mean()),
                    crossings_of_Estar=int(np.sum(np.diff(np.sign(x - Estar)) != 0)),
                    frac_below_Estar=float(np.mean(x < Estar)))
    save_state(st)
    log(f"S6: B = {B:.6f}, two peaks = {st['S6']['two_peaks']}")
    st["DONE"] = True
    save_state(st)
    log("ALL STAGES DONE")


def run_specs_multi(specs):
    """Run specs from different stages in one pool (R10)."""
    todo = [sp for sp in specs if not all(os.path.exists(p) for p in _paths(sp))]
    if todo:
        log(f"  running {len(todo)} runs ({', '.join(sorted(set(s['stage'] for s in todo)))})")
        ctx = mp.get_context("fork")
        with ctx.Pool(NCORES) as pool:
            for tag, w in pool.imap_unordered(_worker, todo):
                log(f"    done {tag}  {w:.1f} s")


def two_peaks(h):
    h = np.asarray(h)
    n = len(h)
    hmax = h.max()
    peaks = []
    for i in range(n):
        w = h[max(0, i - 5):min(n, i + 6)]
        left = h[max(0, i - 5):i]
        if h[i] == w.max() and (len(left) == 0 or h[i] > left.max()) and h[i] >= 0.1 * hmax:
            peaks.append(i)
    for a in range(len(peaks)):
        for b in range(a + 1, len(peaks)):
            i, j = peaks[a], peaks[b]
            if h[i:j + 1].min() < 0.5 * min(h[i], h[j]):
                return dict(two=True, peaks=peaks, pair=[i, j])
    return dict(two=False, peaks=peaks)


if __name__ == "__main__":
    main()
