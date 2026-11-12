"""
Gate DL-BETA REP1 -- stage driver. Applies the card's rules (REP1 sections 4.3-4.5 with the original card's
4.3-4.4 as amended by C1/C2) mechanically, in order, reading each stage's numbers from the previous one.
Every run is an independently seeded chain; each completed run is checkpointed to disk (series npz + record
json) and is never re-run once recorded. Resumable: re-running the driver skips recorded runs.

Usage: nohup python3 -I dlbr_driver.py OUTDIR > OUTDIR/driver_stdout.txt 2>&1 &
"""
import os, sys, json, hashlib, time, math
import numpy as np
from concurrent.futures import ProcessPoolExecutor, wait as fwait

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlbr_stats as ST

U = 10 ** 7                     # beta grid unit: 1e-7 (RD12)
NWORK = 2


def bf(n):
    return n / 1e7


def fb(n, d=4):
    """beta to d decimals, exact grid value in brackets when rounding loses digits (REP1 4.8)."""
    s = f"{bf(n):.{d}f}"
    exact = f"{bf(n):.7f}".rstrip("0")
    if abs(float(s) - bf(n)) > 1e-12:
        return f"{s} [{exact}]"
    return s


OUT = os.path.abspath(sys.argv[1])
SER = os.path.join(OUT, "series")
REC = os.path.join(OUT, "records")
STATE = os.path.join(OUT, "state.json")
LOGF = os.path.join(OUT, "driver_log.txt")
os.makedirs(SER, exist_ok=True)
os.makedirs(REC, exist_ok=True)


def log(msg):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOGF, "a") as f:
        f.write(line + "\n")


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {}


def save_state(st):
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(st, f, indent=1, default=float)
    os.replace(tmp, STATE)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------------------------------------
# worker
# ------------------------------------------------------------------------------------------------
def worker(task):
    import dlbr_sim as S
    n = task["n_therm"] + task["n_meas"]
    rec, ser = S.do_run(task["kind"], task["L"], bf(task["bn"]), task["start"], n)
    rec.update({k: task[k] for k in ("tag", "stage", "bn", "n_therm", "n_meas", "mode")})
    Np = rec["Np"]
    m = ser[task["n_therm"] + 1:, :]
    assert m.shape[0] == task["n_meas"]
    rec["E_start"] = float(ser[0, 0])
    rec["E_final"] = float(ser[-1, 0])
    if task["mode"] in ("scan", "hist"):
        E = m[:, 0]
        rec.update(E=float(E.mean()), E_err=ST.block_err(E), C=ST.spec_heat(E, Np), C_err=ST.spec_heat_jk(E, Np))
        if task["kind"] == "void":
            rec.update(Es=float(m[:, 1].mean()), Es_err=ST.block_err(m[:, 1]),
                       Et=float(m[:, 2].mean()), Et_err=ST.block_err(m[:, 2]))
    if task["mode"] == "mixed":
        idx = np.arange(50, n + 1, 50)
        rec["readings"] = [float(x) for x in ser[idx, 0]]
        endidx = np.arange(1550, 2001, 50)
        assert len(endidx) == 10 and n == 2000
        rec["E_end"] = float(ser[endidx, 0].mean())
        if task["kind"] == "void":
            rec["Es_end"] = float(ser[endidx, 1].mean())
            rec["Et_end"] = float(ser[endidx, 2].mean())
    if task["mode"] == "hist":
        E = m[:, 0]
        two, counts, edges, peaks, pair = ST.two_peaks(E)
        rec.update(B=ST.binder(E), two_peaks=bool(two), hist_counts=[int(c) for c in counts],
                   hist_edges=[float(e) for e in edges], hist_peaks=[int(p) for p in peaks],
                   hist_pair=list(pair) if pair else None)
    fn = os.path.join(SER, task["tag"] + ".npz")
    np.savez_compressed(fn, series=ser, seed=rec["seed"], beta=rec["beta"], tag=task["tag"])
    rec["series_file"] = os.path.basename(fn)
    rec["series_sha256"] = sha256(fn)
    rec["finished"] = time.strftime('%Y-%m-%dT%H:%M:%S')
    tmp = os.path.join(REC, task["tag"] + ".json.tmp")
    with open(tmp, "w") as f:
        json.dump(rec, f, default=float)
    os.replace(tmp, os.path.join(REC, task["tag"] + ".json"))
    return rec


def load_rec(tag):
    p = os.path.join(REC, tag + ".json")
    if os.path.exists(p):
        with open(p) as f:
            r = json.load(f)
        fn = os.path.join(SER, r["series_file"])
        if os.path.exists(fn) and sha256(fn) == r["series_sha256"]:
            return r
    return None


def mk(stage, kind, L, bn, start, n_therm, n_meas, mode):
    tag = f"{stage}_{kind}_L{L}_b{bn:09d}_{start}"
    return dict(tag=tag, stage=stage, kind=kind, L=L, bn=int(bn), start=start,
                n_therm=n_therm, n_meas=n_meas, mode=mode)


COST = {("z4", 8): 9, ("z4", 12): 53, ("void", 2): 1, ("void", 4): 20, ("void", 6): 101, ("void", 8): 265}


class Runner:
    def __init__(self):
        self.ex = ProcessPoolExecutor(NWORK)

    def submit(self, tasks):
        futs = {}
        for t in sorted(tasks, key=lambda t: -COST[(t["kind"], t["L"])] * (t["n_therm"] + t["n_meas"])):
            if load_rec(t["tag"]) is None:
                futs[self.ex.submit(worker, t)] = t
        return futs

    def wait(self, futs):
        pending = set(futs)
        while pending:
            done, pending = fwait(pending, return_when="FIRST_COMPLETED")
            for f in done:
                r = f.result()
                log(f"  done {r['tag']} seed {r['seed']} {r['seconds']:.0f}s ({r['ms_per_sweep']:.1f} ms/sweep)"
                    + (f" E={r['E']:.5f}" if 'E' in r else "") + (f" E_end={r['E_end']:.5f}" if 'E_end' in r else ""))

    def run(self, tasks):
        self.wait(self.submit(tasks))
        out = {}
        for t in tasks:
            r = load_rec(t["tag"])
            assert r is not None, t["tag"]
            out[t["tag"]] = r
        return out

    def close(self):
        self.ex.shutdown()


def scan_table(recs, grid, kind, L, stage, starts=("hot", "cold")):
    rows = {}
    for bn in grid:
        row = {}
        for s in starts:
            r = recs[mk(stage, kind, L, bn, s, 0, 0, "")["tag"]]
            row[s] = r
        rows[bn] = row
    return rows


# ------------------------------------------------------------------------------------------------
# stages
# ------------------------------------------------------------------------------------------------
def stage_K4(R, st):
    if "K4" in st:
        return
    log("STAGE K4: Z4 L=8, beta 0.995..1.020 step 0.0025, hot+cold, 1000+3000")
    grid = [9950000 + 25000 * i for i in range(11)]
    tasks = [mk("K4", "z4", 8, bn, s, 1000, 3000, "scan") for bn in grid for s in ("hot", "cold")]
    recs = R.run(tasks)
    rows = scan_table(recs, grid, "z4", 8, "K4")
    Cmax = [max(rows[b]["hot"]["C"], rows[b]["cold"]["C"]) for b in grid]
    i = ST.argmax_low(Cmax)
    bK = grid[i]
    Ec = [rows[b]["cold"]["E"] for b in grid]
    j, fall = ST.largest_fall(grid, Ec)
    Estar = 0.5 * (Ec[j] + Ec[j + 1])
    passC = 10000000 <= bK <= 10120000
    st["K4"] = dict(grid=grid, Cmax=Cmax, beta_Cmax=bK, Cmax_start="hot" if rows[bK]["hot"]["C"] >= rows[bK]["cold"]["C"] else "cold",
                    cold_jump=[grid[j], grid[j + 1]], cold_fall=fall, Estar_hc=Estar, pass_=passC,
                    tags=[t["tag"] for t in tasks])
    log(f"K4: C max at {fb(bK)} -> {'PASS' if passC else 'FAIL'}; cold jump [{fb(grid[j])},{fb(grid[j+1])}] fall {fall:.5f}; E*_hc = {Estar:.5f}")
    save_state(st)


def stage_K5(R, st):
    if "K5" in st:
        return
    Estar = st["K4"]["Estar_hc"]
    log(f"STAGE K5: Z4 L=12 mixed, beta 1.002..1.022, 2000 sweeps, band E*_hc = {Estar:.5f} +- 0.01")
    grid = [10020000, 10070000, 10120000, 10170000, 10220000]
    tasks = [mk("K5", "z4", 12, bn, "mixed", 0, 2000, "mixed") for bn in grid]
    recs = R.run(tasks)
    outs = [ST.outcome_band(recs[t["tag"]]["E_end"], Estar) for t in tasks]
    fl = ST.flip(grid, outs)
    ok = fl["exists"] and fl["lo"] <= 10171000 and fl["hi"] >= 10051000
    st["K5"] = dict(grid=grid, outcomes=outs, E_end=[recs[t["tag"]]["E_end"] for t in tasks], flip=fl, pass_=bool(ok),
                    tags=[t["tag"] for t in tasks])
    log(f"K5: outcomes {outs}; flip {fl}; {'PASS' if ok else 'FAIL'}")
    save_state(st)


def stage_S1(R, st):
    if "S1" in st:
        return
    log("STAGE S1 (locate): void L=2 Lt=6, beta 0.50..2.00 step 0.01, hot+cold, 500+2000")
    lo, hi, step = 5000000, 20000000, 100000
    ext = []
    while True:
        grid = list(range(lo, hi + 1, step))
        tasks = [mk("S1", "void", 2, bn, s, 500, 2000, "scan") for bn in grid for s in ("hot", "cold")]
        recs = R.run(tasks)
        rows = scan_table(recs, grid, "void", 2, "S1")
        Cmax = [max(rows[b]["hot"]["C"], rows[b]["cold"]["C"]) for b in grid]
        i = ST.argmax_low(Cmax)
        b0 = grid[i]
        near_lo = (b0 - lo) <= 500000
        near_hi = (hi - b0) <= 500000
        log(f"S1: grid [{fb(lo)},{fb(hi)}] beta_0 = {fb(b0)} (C {Cmax[i]:.4f}); near edge lo {near_lo} hi {near_hi}")
        if not near_lo and not near_hi:
            interior = True
            break
        changed = False
        if near_lo and lo > 2000000:
            lo = max(2000000, lo - 2500000); changed = True; ext.append(("lo", lo))
        if near_hi and hi < 40000000:
            hi = min(40000000, hi + 2500000); changed = True; ext.append(("hi", hi))
        if not changed:
            interior = False
            break
    st["S1"] = dict(grid=grid, Cmax=Cmax, beta0=b0, interior=interior, extensions=ext,
                    beta0_start="hot" if rows[b0]["hot"]["C"] >= rows[b0]["cold"]["C"] else "cold",
                    tags=sorted(recs.keys()))
    log(f"S1: beta_0 = {fb(b0)}; interior = {interior}; extensions {ext}")
    save_state(st)


def stage_S2(R, st):
    if "S2" in st:
        return
    b0 = st["S1"]["beta0"]
    step = 50000
    lo, hi = b0 - 500000, b0 + 500000
    log(f"STAGE S2 (fine scan): void L=4 Lt=12, beta_0 +- 0.050 step 0.005, hot+cold, 2000+4000")
    ext = []
    while True:
        grid = list(range(lo, hi + 1, step))
        tasks = [mk("S2", "void", 4, bn, s, 2000, 4000, "scan") for bn in grid for s in ("hot", "cold")]
        recs = R.run(tasks)
        rows = scan_table(recs, grid, "void", 4, "S2")
        Cmax = [max(rows[b]["hot"]["C"], rows[b]["cold"]["C"]) for b in grid]
        i = ST.argmax_low(Cmax)
        b4 = grid[i]
        log(f"S2: grid [{fb(lo)},{fb(hi)}] beta_4 = {fb(b4)} (C {Cmax[i]:.4f})")
        if i == 0:
            lo -= step; ext.append(("lo", lo)); continue
        if i == len(grid) - 1:
            hi += step; ext.append(("hi", hi)); continue
        break
    jumps = {}
    for s in ("hot", "cold"):
        E = [rows[b][s]["E"] for b in grid]
        j, fall = ST.largest_fall(grid, E)
        jumps[s] = dict(interval=[grid[j], grid[j + 1]], fall=fall, E=[E[j], E[j + 1]])
    st["S2"] = dict(grid=grid, Cmax=Cmax, beta4=b4, interior=True, extensions=ext, jumps=jumps,
                    beta4_start="hot" if rows[b4]["hot"]["C"] >= rows[b4]["cold"]["C"] else "cold",
                    tags=sorted(recs.keys()))
    log(f"S2: beta_4 = {fb(b4)}; jump hot {[fb(x) for x in jumps['hot']['interval']]} fall {jumps['hot']['fall']:.5f}; "
        f"cold {[fb(x) for x in jumps['cold']['interval']]} fall {jumps['cold']['fall']:.5f}")
    save_state(st)


def fit_line(xs_n, ys):
    x = np.array([bf(n) for n in xs_n]); y = np.array(ys)
    xc = x.mean()
    A = np.vstack([np.ones_like(x), x - xc]).T
    (a, b), *_ = np.linalg.lstsq(A, y, rcond=None)
    return dict(xc=float(xc), a=float(a), slope=float(b), intercept0=float(a - b * xc),
                points=[[int(n), float(v)] for n, v in zip(xs_n, ys)],
                resid=[float(v - (a + b * (xx - xc))) for xx, v in zip(x, y)])


def line_at(line, bn):
    return line["a"] + line["slope"] * (bf(bn) - line["xc"])


def stage_S3(R, st):
    if "S3" in st:
        return
    b4 = st["S2"]["beta4"]
    step = 50000
    lo, hi = b4 - 300000, b4 + 300000
    log("STAGE S3 (scan, C2): void L=6 Lt=18, beta_4 +- 0.030 step 0.005, hot AND cold, 500+1500")
    ext = []
    while True:
        grid = list(range(lo, hi + 1, step))
        tasks = [mk("S3", "void", 6, bn, s, 500, 1500, "scan") for bn in grid for s in ("hot", "cold")]
        recs = R.run(tasks)
        rows = scan_table(recs, grid, "void", 6, "S3")
        Ec = [rows[b]["cold"]["E"] for b in grid]
        j, fall = ST.largest_fall(grid, Ec)
        blo, bhi = grid[j], grid[j + 1]
        need_S = [blo - 200000, blo - 150000, blo - 100000, blo - 50000]
        need_W = [bhi + 50000, bhi + 100000, bhi + 150000, bhi + 200000]
        changed = False
        if min(need_S) < lo:
            lo -= step; changed = True; ext.append(("lo", lo))
        if max(need_W) > hi:
            hi += step; changed = True; ext.append(("hi", hi))
        log(f"S3: grid [{fb(lo)},{fb(hi)}] cold jump [{fb(blo)},{fb(bhi)}] fall {fall:.5f}; extend: {changed}")
        if not changed:
            break
    Eh = [rows[b]["hot"]["E"] for b in grid]
    jh, fallh = ST.largest_fall(grid, Eh)
    Estar = 0.5 * (rows[blo]["cold"]["E"] + rows[bhi]["cold"]["E"])
    s_lo, s_hi = rows[blo]["cold"]["E_err"], rows[bhi]["cold"]["E_err"]
    thr = 3 * math.sqrt(s_lo ** 2 + s_hi ** 2)
    g4 = st["S2"]["grid"]
    b4_interior = g4[0] < b4 < g4[-1]
    located = bool(b4_interior and fall > thr)
    Sline = fit_line(need_S, [rows[b]["hot"]["E"] for b in need_S])
    Wline = fit_line(need_W, [rows[b]["cold"]["E"] for b in need_W])
    st["S3"] = dict(grid=grid, extensions=ext, cold_jump=[blo, bhi], cold_fall=fall, cold_fall_threshold=thr,
                    hot_jump=[grid[jh], grid[jh + 1]], hot_fall=fallh, Estar=Estar, located=located,
                    b4_interior=b4_interior, S_line=Sline, W_line=Wline, tags=sorted(recs.keys()))
    log(f"S3: jump(6) cold [{fb(blo)},{fb(bhi)}] fall {fall:.5f} (3 sigma {thr:.5f}); hot [{fb(grid[jh])},{fb(grid[jh+1])}]; "
        f"E* = {Estar:.5f}; Located {located}")
    log(f"S3: S(beta) = {Sline['intercept0']:.5f} + {Sline['slope']:.5f} beta  (hot, {[fb(x) for x in need_S]})")
    log(f"S3: W(beta) = {Wline['intercept0']:.5f} + {Wline['slope']:.5f} beta  (cold, {[fb(x) for x in need_W]})")
    save_state(st)


def classify(rec, st):
    Sl, Wl, Estar = st["S3"]["S_line"], st["S3"]["W_line"], st["S3"]["Estar"]
    bn = rec["bn"]
    Sb, Wb = line_at(Sl, bn), line_at(Wl, bn)
    o, f, flag = ST.outcome_primary(rec["E_end"], Sb, Wb)
    o2 = ST.outcome_band(rec["E_end"], Estar)
    return dict(bn=bn, E_end=rec["E_end"], S=Sb, W=Wb, f=f, flagged=flag, primary=o, secondary=o2,
                E_start=rec["E_start"], E_final=rec["E_final"], seed=rec["seed"], tag=rec["tag"],
                Es_end=rec.get("Es_end"), Et_end=rec.get("Et_end"))


def mixed_rounds(R, st, stage, L, centre, half, extra_futs=None):
    step = 25000
    grid = list(range(centre - half, centre + half + 1, step))
    ext = []
    while True:
        tasks = [mk(stage, "void", L, bn, "mixed", 0, 2000, "mixed") for bn in grid]
        recs = R.run(tasks)
        rows = [classify(recs[t["tag"]], st) for t in tasks]
        outs = [r["primary"] for r in rows]
        fl = ST.flip(grid, outs)
        log(f"{stage}: grid [{fb(grid[0])},{fb(grid[-1])}] primary {outs}")
        added = False
        if not fl["has_weak"] and len(ext) < 8:
            grid = grid + [grid[-1] + step]; ext.append(("above", grid[-1])); added = True
        if not fl["has_strong"] and len(ext) < 8:
            grid = [grid[0] - step] + grid; ext.append(("below", grid[0])); added = True
        if not added:
            break
    fl2 = ST.flip(grid, [r["secondary"] for r in rows])
    return dict(grid=grid, extensions=ext, runs=rows, flip=fl, flip_secondary=fl2,
                n_unresolved=sum(1 for r in rows if r["primary"] == "unresolved"),
                n_unresolved_secondary=sum(1 for r in rows if r["secondary"] == "unresolved"),
                ext_limit_hit=(len(ext) >= 8 and not fl["exists"]))


def stage_S4a(R, st):
    if "S4a" in st:
        return
    blo, bhi = st["S3"]["cold_jump"]
    centre = (blo + bhi) // 2
    assert (blo + bhi) % 2 == 0
    log(f"STAGE S4a (mixed L=6, Lt=18): centre {fb(centre)} +- 0.0075 step 0.0025, 2000 sweeps")
    st["S4a"] = mixed_rounds(R, st, "S4a", 6, centre, 75000)
    st["S4a"]["centre"] = centre
    fl = st["S4a"]["flip"]
    log(f"S4a: flip {fl}")
    save_state(st)


def stage_S4b_S6(R, st):
    if "S4b" in st and "S6" in st:
        return
    fl6 = st["S4a"]["flip"]
    if fl6["exists"]:
        hb = int(round(fl6["mid"]))
        assert abs(hb - fl6["mid"]) < 1e-9
        hist_src = "beta_mix(6)"
    else:
        blo, bhi = st["S3"]["cold_jump"]
        hb = (blo + bhi) // 2
        hist_src = "(beta_lo+beta_hi)/2"
    log(f"STAGE S6 (histogram L=6) at {fb(hb)} [{hist_src}], mixed start, s=3, 2000+20000 -- scheduled concurrently (R9)")
    htask = mk("S6", "void", 6, hb, "hist", 2000, 20000, "hist")
    hfuts = R.submit([htask])
    if fl6["exists"]:
        c8 = int(round(fl6["mid"]))
        log(f"STAGE S4b (mixed L=8, Lt=24): centre beta_mix(6) = {fb(c8)} +- 0.005 step 0.0025, 2000 sweeps")
        st["S4b"] = mixed_rounds(R, st, "S4b", 8, c8, 50000)
        st["S4b"]["centre"] = c8
        st["S4b"]["run"] = True
        log(f"S4b: flip {st['S4b']['flip']}")
    else:
        st["S4b"] = dict(run=False, reason="RD9: no L = 6 primary flip; L = 8 grid undefined", flip=dict(exists=False),
                         flip_secondary=dict(exists=False), runs=[], grid=[], extensions=[], n_unresolved=0,
                         n_unresolved_secondary=0)
        log("S4b: not run (RD9)")
    save_state(st)
    R.wait(hfuts)
    h = load_rec(htask["tag"])
    st["S6"] = dict(bn=hb, source=hist_src, tag=h["tag"], seed=h["seed"], B=h["B"], two_peaks=h["two_peaks"],
                    peaks=h["hist_peaks"], pair=h["hist_pair"], counts=h["hist_counts"], edges=h["hist_edges"],
                    E=h["E"], E_err=h["E_err"], C=h["C"])
    log(f"S6: B = {h['B']:.6f}; two peaks = {h['two_peaks']} (peaks {h['hist_peaks']}, pair {h['hist_pair']})")
    save_state(st)


def final(st):
    """REP1 4.4 step 5 (result), step 7 (order), Q5, Q6."""
    res = {}
    fl6, fl8 = st["S4a"]["flip"], st["S4b"]["flip"]
    if fl8["exists"]:
        binf = fl8["mid"]
        half8 = (fl8["hi"] - fl8["lo"]) / 2.0
        d68 = abs(fl8["mid"] - fl6["mid"])
        u = max(half8, d68)
        runs8 = st["S4b"]["runs"]
        below = [r for r in runs8 if r["primary"] == "strong" and r["bn"] < binf]
        above = [r for r in runs8 if r["primary"] == "weak" and r["bn"] > binf]
        rb = max(below, key=lambda r: r["bn"]) if below else None
        ra = min(above, key=lambda r: r["bn"]) if above else None
        dE = (rb["E_end"] - ra["E_end"]) if (rb and ra) else None
        x6, x8 = 1.0 / (6 ** 3 * 18), 1.0 / (8 ** 3 * 24)
        b0x = fl8["mid"] - x8 * (fl6["mid"] - fl8["mid"]) / (x6 - x8)
        resolved = bool(st["S4b"]["n_unresolved"] <= 1 and u <= 0.010 * U)
        res.update(beta_inf=binf, half8=half8, d68=d68, u=u, inv_e2=bf(binf) / math.sqrt(2), inv_e2_u=bf(u) / math.sqrt(2),
                   dE8=dE, dE8_below=rb["bn"] if rb else None, dE8_above=ra["bn"] if ra else None,
                   extrap0=b0x, resolved=resolved, betaR=binf)
    else:
        blo, bhi = st["S3"]["cold_jump"]
        res.update(beta_inf=None, u=None, resolved=False, betaR=(blo + bhi) / 2.0, dE8=None)
    # order (Q4)
    hyst = {}
    for stage, L in (("S2", 4), ("S3", 6)):
        g = st[stage]["grid"]
        recs = {b: {s: load_rec(mk(stage, "void", L, b, s, 0, 0, "")["tag"]) for s in ("hot", "cold")} for b in g}
        Eh = [recs[b]["hot"]["E"] for b in g]; Ec = [recs[b]["cold"]["E"] for b in g]
        jh, _ = ST.largest_fall(g, Eh); jc, _ = ST.largest_fall(g, Ec)
        z = [abs(recs[b]["hot"]["E"] - recs[b]["cold"]["E"]) / math.sqrt(recs[b]["hot"]["E_err"] ** 2 + recs[b]["cold"]["E_err"] ** 2) for b in g]
        hyst[L] = dict(jump_hot=[g[jh], g[jh + 1]], jump_cold=[g[jc], g[jc + 1]], intervals_differ=bool(jh != jc),
                       max_z=float(max(z)), beta_max_z=g[int(np.argmax(z))], n_over_3sigma=int(sum(1 for x in z if x > 3)),
                       points_over_3sigma=[g[i] for i, x in enumerate(z) if x > 3])
        hyst[L]["hysteresis"] = bool(hyst[L]["intervals_differ"] or hyst[L]["n_over_3sigma"] > 0)
    a = bool(hyst[4]["hysteresis"] or hyst[6]["hysteresis"])
    j4 = st["S2"]["jumps"]["cold"]["fall"]; j6 = st["S3"]["cold_fall"]; d8 = res.get("dE8")
    shrink = None if d8 is None else bool(d8 < 0.7 * j4)
    c = bool(st["S6"]["two_peaks"])
    if shrink is None:
        order = "order undetermined"
    else:
        order = "first-order" if (a and c and not shrink) else "order undetermined"
    res["order"] = dict(a_hysteresis=a, hyst=hyst, jump4=j4, jump6=j6, dE8=d8, shrinks_more_than_30pct=shrink,
                        c_two_peaks=c, call=order)
    # Q6: secondary rule
    fs6, fs8 = st["S4a"]["flip_secondary"], st["S4b"]["flip_secondary"]
    q6 = dict(beta_mix6_sec=fs6, beta_mix8_sec=fs8, n_unres8_sec=st["S4b"]["n_unresolved_secondary"])
    if fs8["exists"] and fs6["exists"]:
        u2 = max((fs8["hi"] - fs8["lo"]) / 2.0, abs(fs8["mid"] - fs6["mid"]))
        q6["u_sec"] = u2
        q6["beta_inf_sec"] = fs8["mid"]
        ok = st["S4b"]["n_unresolved_secondary"] <= 1 and u2 <= 0.010 * U
    else:
        q6["u_sec"] = None
        ok = False
    if not (st["K4"]["pass_"] and st["K5"]["pass_"]):
        code = "SC-DLB-0"
    elif not st["S1"]["interior"]:
        code = "SC-DLB-3"
    elif ok:
        code = "SC-DLB-1"
    elif st["S3"]["located"]:
        code = "SC-DLB-2"
    else:
        code = "SC-DLB-3 (not located)"
    q6["original_card_code"] = code
    res["Q6"] = q6
    st["final"] = res
    save_state(st)
    log(f"FINAL: {json.dumps(res, default=float)[:2000]}")


def main():
    st = load_state()
    log(f"driver start; state keys {sorted(st.keys())}")
    R = Runner()
    try:
        stage_K4(R, st)
        stage_K5(R, st)
        if not (st["K4"]["pass_"] and st["K5"]["pass_"]):
            st["verdict_stop"] = "SC-DLBR-0 (K4/K5 failed)"
            save_state(st)
            log("STOP: SC-DLBR-0")
            return
        stage_S1(R, st)
        if not st["S1"]["interior"]:
            st["verdict_stop"] = "SC-DLBR-5 (no interior C maximum in [0.20, 4.00])"
            save_state(st)
            log("STOP: SC-DLBR-5")
            return
        stage_S2(R, st)
        stage_S3(R, st)
        stage_S4a(R, st)
        stage_S4b_S6(R, st)
        final(st)
        log("DRIVER COMPLETE")
    finally:
        R.close()


if __name__ == "__main__":
    main()
