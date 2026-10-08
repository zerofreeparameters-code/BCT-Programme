"""
Gate CRIT2 stage driver. Usage: python3 crit2.py <stage>
Stages: check3 check4 s51 s52 s53 s54a s54b
Every stage reads earlier stage results from out/state.json and applies the card's rules
(sections 4 and 5) mechanically. Two worker processes (2 cores, one simulation per core).
"""
import sys, os, json, time
import numpy as np
import multiprocessing as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1sim as U

OUT = os.environ.get("CRIT2_OUT", "/root/crit2/out")
STATE = f"{OUT}/state.json"
NPROC = 2
MAX_EXT = 20   # safety cap on grid extensions (reported if ever hit)


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {}


def save_state(st):
    with open(STATE, "w") as f:
        json.dump(st, f, indent=1)


def r6(x):
    return round(float(x), 6)


def grid(lo, hi, step):
    n = int(round((hi - lo) / step))
    return [r6(lo + i * step) for i in range(n + 1)]


def _scan_job(a):
    name, L, beta, start, nt, nm = a
    res, E = U.run_scan(name, L, beta, start, nt, nm)
    return res, E


def _mixed_job(a):
    name, L, beta, nsw, Estar = a
    res, E = U.run_mixed(name, L, beta, nsw, Estar)
    return res, E


def run_pool(fn, jobs):
    # biggest first for balance (all jobs in a stage have equal cost, so keep order)
    with mp.get_context("fork").Pool(NPROC) as pool:
        out = pool.map(fn, jobs, chunksize=1)
    return out


def dump(tag, results):
    with open(f"{OUT}/{tag}.jsonl", "a") as f:
        for r, _ in results:
            f.write(json.dumps(r) + "\n")
    arr = {}
    path = f"{OUT}/{tag}_series.npz"
    if os.path.exists(path):
        old = np.load(path)
        arr.update({k: old[k] for k in old.files})
    for r, E in results:
        key = f"{r['lattice']}_L{r['L']}_b{r['beta']:.6f}_{r['start']}"
        arr[key] = E.astype(np.float32) if len(E) > 5000 else E
    np.savez_compressed(path, **arr)


def table_scan(rows):
    rows = sorted(rows, key=lambda r: (r["beta"], r["start"]))
    lines = ["   beta    start      E          dE        C          dC     seed"]
    for r in rows:
        lines.append(f"{r['beta']:.4f}  {r['start']:5s}  {r['E']:.5f}  {r['E_err']:.5f}  "
                     f"{r['C']:9.3f}  {r['C_err']:7.3f}  {r['seed']}")
    return "\n".join(lines)


def cmax_beta(rows):
    best = {}
    for r in rows:
        b = r["beta"]
        if b not in best or r["C"] > best[b]["C"]:
            best[b] = r
    bmax = max(best, key=lambda b: best[b]["C"])
    return bmax, best[bmax]


def jump_interval(rows, start):
    rr = sorted([r for r in rows if r["start"] == start], key=lambda r: r["beta"])
    falls = [rr[i]["E"] - rr[i + 1]["E"] for i in range(len(rr) - 1)]
    i = int(np.argmax(falls))
    return dict(lo=rr[i]["beta"], hi=rr[i + 1]["beta"], E_lo=rr[i]["E"], E_hi=rr[i + 1]["E"],
                fall=falls[i], start=start)


def scan_stage(tag, name, L, betas, starts, nt, nm, extend_step=None):
    """Run a scan; if extend_step, extend the grid while the C maximum sits on an edge."""
    rows = []
    todo = list(betas)
    n_ext = 0
    while True:
        jobs = [(name, L, b, s, nt, nm) for b in todo for s in starts]
        t = time.time()
        res = run_pool(_scan_job, jobs)
        print(f"[{tag}] {len(jobs)} runs in {time.time()-t:.0f}s", flush=True)
        dump(tag, res)
        rows += [r for r, _ in res]
        if extend_step is None:
            break
        bmax, _ = cmax_beta(rows)
        bs = sorted({r["beta"] for r in rows})
        if bmax == bs[0]:
            todo = [r6(bs[0] - extend_step)]
        elif bmax == bs[-1]:
            todo = [r6(bs[-1] + extend_step)]
        else:
            break
        n_ext += 1
        print(f"[{tag}] C max on edge at {bmax}; extending to {todo}", flush=True)
        if n_ext > MAX_EXT:
            raise RuntimeError("extension cap hit")
    return rows, n_ext


def flip_analysis(rows):
    rr = sorted(rows, key=lambda r: r["beta"])
    strong = [r["beta"] for r in rr if r["outcome"] == "strong"]
    weak = [r["beta"] for r in rr if r["outcome"] == "weak"]
    if not strong or not weak:
        return None
    hs, lw = max(strong), min(weak)
    return dict(highest_strong=hs, lowest_weak=lw, beta_mix=r6((hs + lw) / 2),
                lo=min(hs, lw), hi=max(hs, lw), half_width=abs(lw - hs) / 2,
                monotonic=bool(hs < lw),
                pattern=[(r["beta"], r["outcome"][0].upper()) for r in rr])


def mixed_stage(tag, name, L, betas, nsw, Estar, step=0.0025):
    rows = []
    todo = list(betas)
    n_ext = 0
    while True:
        jobs = [(name, L, b, nsw, Estar) for b in todo]
        t = time.time()
        res = run_pool(_mixed_job, jobs)
        print(f"[{tag}] {len(jobs)} runs in {time.time()-t:.0f}s", flush=True)
        dump(tag, res)
        rows += [r for r, _ in res]
        for r, _ in res:
            print(f"   beta={r['beta']:.5f}  E_last500={r['E_last500']:.5f}  E*={Estar:.5f}  -> {r['outcome']}",
                  flush=True)
        fa = flip_analysis(rows)
        if fa is not None:
            break
        bs = sorted({r["beta"] for r in rows})
        has_s = any(r["outcome"] == "strong" for r in rows)
        has_w = any(r["outcome"] == "weak" for r in rows)
        todo = []
        if not has_w:
            todo.append(r6(bs[-1] + step))
        if not has_s:
            todo.append(r6(bs[0] - step))
        n_ext += 1
        print(f"[{tag}] no flip inside grid; extending to {todo}", flush=True)
        if n_ext > MAX_EXT:
            raise RuntimeError("extension cap hit")
    return rows, fa, n_ext


# ----------------------------------------------------------------------------------
def stage_check3(st):
    betas = grid(0.995, 1.020, 0.0025)
    rows, _ = scan_stage("check3", "hc", 8, betas, ["hot", "cold"], 1000, 3000)
    print(table_scan(rows))
    bmax, rmax = cmax_beta(rows)
    passed = 1.000 - 1e-9 <= bmax <= 1.012 + 1e-9
    ji = jump_interval(rows, "cold")
    Ehc = (ji["E_lo"] + ji["E_hi"]) / 2
    print(f"C max at beta={bmax} ({rmax['start']}, C={rmax['C']:.2f}); required in [1.000, 1.012] -> "
          f"{'PASS' if passed else 'FAIL'}")
    print(f"cold jump interval: [{ji['lo']}, {ji['hi']}], fall={ji['fall']:.5f}; E*_hc={Ehc:.5f}")
    st["check3"] = dict(beta_Cmax=bmax, Cmax=rmax["C"], Cmax_start=rmax["start"], passed=bool(passed),
                        jump_cold=ji, jump_hot=jump_interval(rows, "hot"), Estar_hc=Ehc)


def stage_check4(st):
    Ehc = st["check3"]["Estar_hc"]
    betas = [1.002, 1.007, 1.012, 1.017, 1.022]
    rows, fa, n_ext = mixed_stage("check4", "hc", 12, betas, 2000, Ehc)
    lo, hi = fa["lo"], fa["hi"]
    passed = (lo <= 1.0111 + 0.006) and (hi >= 1.0111 - 0.006)
    print(f"flip interval [{lo}, {hi}] (strong<= {fa['highest_strong']}, weak>= {fa['lowest_weak']}), "
          f"beta_mix={fa['beta_mix']}; must contain a point within 0.006 of 1.0111 -> {'PASS' if passed else 'FAIL'}")
    st["check4"] = dict(flip=fa, n_ext=n_ext, passed=bool(passed), Estar_hc=Ehc,
                        runs=[dict(beta=r["beta"], E_last500=r["E_last500"], outcome=r["outcome"]) for r in rows])


def stage_s51(st):
    betas = grid(0.40, 0.90, 0.01)
    rows, _ = scan_stage("s51", "d4", 4, betas, ["hot", "cold"], 500, 2000)
    print(table_scan(rows))
    b0, r0 = cmax_beta(rows)
    print(f"beta0 = {b0} (C={r0['C']:.2f}, {r0['start']})")
    st["s51"] = dict(beta0=b0, Cmax=r0["C"], start=r0["start"])


def stage_s52(st):
    b0 = st["s51"]["beta0"]
    betas = grid(b0 - 0.030, b0 + 0.030, 0.005)
    rows, n_ext = scan_stage("s52", "d4", 8, betas, ["hot", "cold"], 2000, 4000, extend_step=0.005)
    print(table_scan(rows))
    b8, r8 = cmax_beta(rows)
    jh, jc = jump_interval(rows, "hot"), jump_interval(rows, "cold")
    print(f"beta8 = {b8} (C={r8['C']:.2f}, {r8['start']}); extensions={n_ext}")
    print(f"jump interval L=8 hot : [{jh['lo']}, {jh['hi']}] fall={jh['fall']:.5f}")
    print(f"jump interval L=8 cold: [{jc['lo']}, {jc['hi']}] fall={jc['fall']:.5f}")
    st["s52"] = dict(beta8=b8, Cmax=r8["C"], start=r8["start"], n_ext=n_ext, jump_hot=jh, jump_cold=jc)


def stage_s53(st):
    b8 = st["s52"]["beta8"]
    betas = grid(b8 - 0.020, b8 + 0.020, 0.005)
    rows, _ = scan_stage("s53", "d4", 12, betas, ["cold"], 500, 1500)
    print(table_scan(rows))
    j = jump_interval(rows, "cold")
    Estar = (j["E_lo"] + j["E_hi"]) / 2
    print(f"jump interval L=12 cold: [{j['lo']}, {j['hi']}] fall={j['fall']:.5f}; E* = {Estar:.5f}")
    st["s53"] = dict(jump=j, Estar=Estar)


def stage_s54a(st):
    j = st["s53"]["jump"]
    c = (j["lo"] + j["hi"]) / 2
    betas = [r6(c + k * 0.0025) for k in range(-3, 4)]
    rows, fa, n_ext = mixed_stage("s54a", "d4", 12, betas, 2000, st["s53"]["Estar"])
    print(f"L=12 flip: pattern={fa['pattern']}  beta_mix(12)={fa['beta_mix']}  interval=[{fa['lo']}, {fa['hi']}]")
    st["s54a"] = dict(center=r6(c), flip=fa, n_ext=n_ext,
                      runs=[dict(beta=r["beta"], E_last500=r["E_last500"], E_final=r["E_final"],
                                 outcome=r["outcome"]) for r in rows])


def stage_s54b(st):
    c = st["s54a"]["flip"]["beta_mix"]
    betas = [r6(c + k * 0.0025) for k in range(-2, 3)]
    rows, fa, n_ext = mixed_stage("s54b", "d4", 16, betas, 2000, st["s53"]["Estar"])
    bmix12 = c
    binf = fa["beta_mix"]
    unc = max(fa["half_width"], abs(binf - bmix12))
    # Delta E: nearest strong-win run below beta_inf and weak-win run above it
    sb = [r for r in rows if r["outcome"] == "strong" and r["beta"] < binf]
    wa = [r for r in rows if r["outcome"] == "weak" and r["beta"] > binf]
    flag = ""
    if sb and wa:
        rs = max(sb, key=lambda r: r["beta"]); rw = min(wa, key=lambda r: r["beta"])
    else:
        rs = [r for r in rows if r["beta"] == fa["highest_strong"]][0]
        rw = [r for r in rows if r["beta"] == fa["lowest_weak"]][0]
        flag = "non-monotonic: used highest strong / lowest weak"
    dE = rs["E_last500"] - rw["E_last500"]
    dE_final = rs["E_final"] - rw["E_final"]
    print(f"L=16 flip: pattern={fa['pattern']}  beta_mix(16)={binf}  interval=[{fa['lo']}, {fa['hi']}]")
    print(f"beta_inf = {binf} +- {unc:.5f}  (beta_KN = {2*binf:.5f} +- {2*unc:.5f});  "
          f"Delta E(L=16) = {dE:.5f} (strong {rs['beta']} -> weak {rw['beta']}) {flag}")
    st["s54b"] = dict(center=c, flip=fa, n_ext=n_ext,
                      runs=[dict(beta=r["beta"], E_last500=r["E_last500"], E_final=r["E_final"],
                                 outcome=r["outcome"]) for r in rows])
    st["s55"] = dict(beta_inf=binf, unc=unc, beta_inf_KN=2 * binf, unc_KN=2 * unc,
                     beta_mix12=bmix12, beta_mix16=binf, half_width16=fa["half_width"],
                     dE16=dE, dE16_final=dE_final, dE_runs=[rs["beta"], rw["beta"]], dE_flag=flag,
                     kill_reopened=bool(binf - unc < 0.5601))


STAGES = dict(check3=stage_check3, check4=stage_check4, s51=stage_s51, s52=stage_s52,
              s53=stage_s53, s54a=stage_s54a, s54b=stage_s54b)

if __name__ == "__main__":
    stage = sys.argv[1]
    st = load_state()
    if stage in st:
        raise SystemExit(f"stage {stage} already in state.json; refusing to rerun")
    t = time.time()
    STAGES[stage](st)
    st.setdefault("_timing", {})[stage] = round(time.time() - t, 1)
    save_state(st)
    print(f"[{stage}] done in {time.time()-t:.0f}s")
