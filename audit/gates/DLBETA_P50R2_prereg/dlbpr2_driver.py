"""
Gate DL-BETA P50R2 -- driver (pre-registered with the card). Gate DL-BETA P50R's driver with ONE change: the branch
runs are 1500 + 4500 sweeps instead of P50's 500 + 1500 (card section 3, R1). Everything else is P50R's: K1, K2
(Gate DL-BETA's four K3 runs, its seeds, 1000 + 10,000), every window chain of card section 4.4 (3000 sweeps,
P50's grids and chain counts), P50's bracket-extension rule, and the records. The simulator is Gate DL-BETA's
ORIGINAL code (dlb_sim.py + dlb_complex.py), unmodified, called through its own entry point run_job(). The
estimators are P50's dlbp_analysis.py, unmodified. The seeds are a new family (section 4.4).

Usage:  nohup python3 -I dlbpr2_driver.py SIM_DIR ORIG_SERIES_DIR OUTDIR [WORKERS] > OUTDIR/driver_stdout.txt 2>&1 &
  SIM_DIR          Gate DL-BETA's run/ directory (dlb_sim.py, dlb_complex.py; hash-checked)
  ORIG_SERIES_DIR  Gate DL-BETA's out/series (K3_series.npz, for K2's bit-reproduction comparison)
  WORKERS          parallel chains (default: os.cpu_count())
Then: python3 -I dlbpr2_rules.py numbers OUTDIR ; hash ; post ;
      python3 -I dlbpr2_rules.py verdict OUTDIR P50_ANALYSIS_JSON [P50R_ANALYSIS_JSON]
Dry run (code paths only, tiny lattices, seeds + 9,000,000, branch runs 60 + 120): DLBP_DRYRUN=1 in the environment.

Series layout (as P50): series[k] = (E, E_s, E_t) after sweep k, k = 1..n; row 0 = (E at the start, NaN, NaN),
because run_job() returns the starting E only.
"""
import os, sys, json, time, hashlib
sys.dont_write_bytecode = True                  # write no __pycache__ into the repository's DLBETA/run
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ["NUMBA_CACHE_DIR"] = os.path.join(HERE, "numba_cache")   # numba's cache outside the repository
sys.path.insert(0, HERE)
import numpy as np
from concurrent.futures import ProcessPoolExecutor, wait as fwait
import dlbp_analysis as AN                      # P50's estimators, unmodified
import dlbpr2_rules as RU

SIM_SHA256 = {"dlb_sim.py": "4a813cf7eea0b883eaa3ced4fb6d1d10662683f6ac610077c1f85df62332ed77",
              "dlb_complex.py": "4aa142b0f57122b02a4590ce221d7510ca86ccff051a156ce38a1e8e75214d8a"}
K3_SERIES_SHA256 = "705bd34a814fbf38ec9e50b70ac2ae9fe46d1bfe85e439ff84046a24bd26ecf1"   # Gate DL-BETA out/series/K3_series.npz
DRY = os.environ.get("DLBP_DRYRUN") == "1"
N_BRANCH = RU.N_BRANCH                          # (1500, 4500); dry run (60, 120). THE one change from P50R.


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def log(out, msg):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(os.path.join(out, "driver_log.txt"), "a") as f:
        f.write(line + "\n")


def mk(lat, role, bn, c):
    spec = AN.LATTICES[lat]
    s = {"hot": 0, "cold": 1, "mixed": 2}[role]
    n_th, n_me = (N_BRANCH if role in ("hot", "cold") else (0, AN.N_MIXED))
    return dict(tag=f"{lat}_b{bn:09d}_{role}_c{c}", lat=lat, kind=spec["kind"], L=spec["L"], bn=int(bn), role=role,
                chain=c, s=s, seed=RU.seed(spec["kind"], spec["L"], bn, s, c), n_therm=n_th, n_meas=n_me)


def mk_k2(kind, L, beta, start, seed):
    """Gate DL-BETA's K3 runs, with its seeds and sweeps; its stored series key is <tag>__E/__Es/__Et."""
    tag = f"{kind}_L{L}_b{beta:.5f}_{start}"
    return dict(tag=f"K2_{tag}", lat="K2", kind=kind, L=L, bn=int(round(beta * AN.U)), role="k2_" + start, chain=0,
                s=-1, seed=seed, n_therm=1000, n_meas=10000, orig_key=tag)


def worker(t):
    sys.path.insert(0, t["sim_dir"])
    import dlb_sim as S
    n = t["n_therm"] + t["n_meas"]
    start = {"hot": "hot", "cold": "cold", "mixed": "mixed", "k2_hot": "hot", "k2_cold": "cold"}[t["role"]]
    spec = dict(lattice=t["kind"], L=t["L"], Lt=(3 * t["L"] if t["kind"] == "void" else None),
                beta=t["bn"] / AN.U, start=start, seed=int(t["seed"]), n_sweeps=n)
    rj, sr = S.run_job(spec)
    ser = np.empty((n + 1, 3))
    ser[0] = (rj["E_start"], np.nan, np.nan)
    ser[1:, 0], ser[1:, 1], ser[1:, 2] = sr["E"], sr["Es"], sr["Et"]
    rec = {k: t[k] for k in ("tag", "lat", "kind", "L", "bn", "role", "chain", "s", "seed", "n_therm", "n_meas")}
    rec.update(beta=t["bn"] / AN.U, Np=int(rj["n_loops"]), seconds=rj["wall_s"], ms_per_sweep=rj["ms_per_sweep"],
               E_start=float(ser[0, 0]), E_final=float(ser[-1, 0]))
    m = ser[t["n_therm"] + 1:, 0]
    if t["role"] in ("hot", "cold", "k2_hot", "k2_cold"):
        e, bm = AN.block_err(m)
        rec.update(E=float(m.mean()), E_err=e, block_means=[float(x) for x in bm])
        if t["kind"] == "void":
            rec.update(Es=float(ser[t["n_therm"] + 1:, 1].mean()), Et=float(ser[t["n_therm"] + 1:, 2].mean()))
    if t["role"] == "mixed":
        idx = np.arange(50, n + 1, 50)
        rd = ser[idx, 0]
        rec["readings"] = [float(x) for x in rd]
        rec["E_end"] = float(rd[-10:].mean())
        half = n // 2
        mid = np.arange(half - 450, half + 1, 50)
        rec["E_mid"] = float(ser[mid, 0].mean())
        if t["kind"] == "void":
            rec["Es_end"] = float(ser[idx[-10:], 1].mean())
            rec["Et_end"] = float(ser[idx[-10:], 2].mean())
    if t["role"].startswith("k2_"):
        ref = t["orig_file"]
        ok = False
        if ref and os.path.exists(ref):
            z = np.load(ref)
            ok = all(f"{t['orig_key']}__{c}" in z.files for c in ("E", "Es", "Et"))
            if ok:
                for c in ("E", "Es", "Et"):
                    a, b = np.ascontiguousarray(z[f"{t['orig_key']}__{c}"], dtype=np.float64), np.ascontiguousarray(sr[c], dtype=np.float64)
                    ok = ok and a.shape == b.shape and np.array_equal(a.view(np.uint64), b.view(np.uint64))   # exact bits
        rec["bit_identical"] = bool(ok)
    fn = os.path.join(t["out"], "series", t["tag"] + ".npz")
    np.savez_compressed(fn, series=ser, seed=t["seed"], beta=t["bn"] / AN.U, tag=t["tag"])
    rec["series_file"] = os.path.basename(fn)
    rec["series_sha256"] = sha256(fn)
    rec["finished"] = time.strftime('%Y-%m-%dT%H:%M:%S')
    p = os.path.join(t["out"], "records", t["tag"] + ".json")
    json.dump(rec, open(p + ".tmp", "w"), default=float)
    os.replace(p + ".tmp", p)
    return rec


COST = {("z4", 8): 8, ("z4", 12): 42, ("void", 6): 75, ("void", 8): 236, ("void", 2): 1, ("void", 3): 3,
        ("z4", 4): 1, ("z4", 6): 4}


def have(out, tag):
    p = os.path.join(out, "records", tag + ".json")
    if not os.path.exists(p):
        return False
    r = json.load(open(p))
    f = os.path.join(out, "series", r["series_file"])
    return os.path.exists(f) and sha256(f) == r["series_sha256"]


def run(ex, out, sim_dir, orig_file, tasks):
    todo = [dict(t, out=out, sim_dir=sim_dir, orig_file=orig_file) for t in tasks if not have(out, t["tag"])]
    todo.sort(key=lambda t: -COST.get((t["kind"], t["L"]), 1) * (t["n_therm"] + t["n_meas"]))
    futs = [ex.submit(worker, t) for t in todo]
    pending = set(futs)
    while pending:
        done, pending = fwait(pending, return_when="FIRST_COMPLETED")
        for f in done:
            r = f.result()
            log(out, f"  done {r['tag']} seed {r['seed']} {r['seconds']:.0f}s ({r['ms_per_sweep']:.1f} ms/sweep)"
                + (f" E={r['E']:.5f}" if "E" in r else "") + (f" E_end={r['E_end']:.5f}" if "E_end" in r else ""))


def main():
    sim_dir, orig_series, out = [os.path.abspath(x) for x in sys.argv[1:4]]
    nw = int(sys.argv[4]) if len(sys.argv) > 4 else os.cpu_count()
    for d in ("series", "records"):
        os.makedirs(os.path.join(out, d), exist_ok=True)
    stp = os.path.join(out, "state.json")
    st = json.load(open(stp)) if os.path.exists(stp) else {"ext": {}}
    log(out, f"driver start; workers {nw}; dry run {DRY}; branch runs {N_BRANCH[0]} + {N_BRANCH[1]} sweeps")
    # K1 -- the simulator is Gate DL-BETA's original code and the estimators are P50's, all unmodified
    hs = {f: sha256(os.path.join(sim_dir, f)) for f in SIM_SHA256}
    ha = sha256(os.path.join(HERE, "dlbp_analysis.py"))
    orig_file = os.path.join(orig_series, "K3_series.npz")
    hk = sha256(orig_file) if os.path.exists(orig_file) else None
    ok = all(hs[f] == SIM_SHA256[f] for f in SIM_SHA256) and ha == RU.AN_SHA256
    st["K1"] = {"sim": hs, "sim_expected": SIM_SHA256, "dlbp_analysis_sha256": ha, "dlbp_analysis_expected": RU.AN_SHA256,
                "k3_series_sha256": hk, "k3_series_expected": K3_SERIES_SHA256, "pass": bool(ok)}
    st["N_BRANCH"] = list(N_BRANCH)
    log(out, f"K1 dlb_sim.py {hs['dlb_sim.py'][:16]}, dlb_complex.py {hs['dlb_complex.py'][:16]}, dlbp_analysis.py {ha[:16]}, "
             f"K3_series.npz {str(hk)[:16]} (reference) -> {'PASS' if ok else 'FAIL'}")
    json.dump(st, open(stp, "w"), indent=1)
    if not ok:
        log(out, "STOP: K1 failed (SC-DLBPR2-0)")
        return
    # fixed tasks: K2 (Gate DL-BETA's K3 runs, its seeds), every branch run, every window chain
    k2 = [mk_k2("void", 2, 0.1, "hot", 516838), mk_k2("void", 2, 20.0, "cold", 715839),
          mk_k2("z4", 4, 0.1, "hot", 32676), mk_k2("z4", 4, 20.0, "cold", 231677)]
    if DRY:
        for t in k2:
            t["n_therm"], t["n_meas"], t["seed"] = 100, 1000, t["seed"] + 9000000
    tasks = list(k2)
    for key in AN.ORDER:
        spec = AN.LATTICES[key]
        tasks += [mk(key, "hot", b, 0) for b in spec["S"]] + [mk(key, "cold", b, 0) for b in spec["W"]]
        grid = sorted(set(spec["window"]) | set(x for x in st["ext"].get(key, [])))
        tasks += [mk(key, "mixed", b, c) for b in grid for c in range(spec["chains"])]
    ex = ProcessPoolExecutor(nw)
    try:
        log(out, f"submitting {len(tasks)} fixed tasks")
        run(ex, out, sim_dir, orig_file, tasks)
        recs = AN.load_records(out)
        # K2 evaluation (within 2 % of the targets)
        from scipy.special import i0e, i1e
        tg = {"void": 1533 / (2 * 20.0 * 2688), "z4": 765 / (2 * 20.0 * 1536)}
        st["K2"] = {}
        for t in k2:
            r = recs[t["tag"]]
            if t["role"] == "k2_hot":
                val, target = 1 - r["E"], i1e(0.1) / i0e(0.1)
            else:
                val, target = r["E"], tg[t["kind"]]
            dev = val / target - 1
            st["K2"][t["tag"][3:]] = {"value": val, "target": target, "dev": dev, "pass": bool(abs(dev) < 0.02),
                                      "seed": r["seed"], "bit_identical": r["bit_identical"]}
            log(out, f"K2 {t['tag']}: {val:.6f} vs {target:.6f} ({100*dev:+.2f}%), bit-identical to Gate DL-BETA: {r['bit_identical']}")
        json.dump(st, open(stp, "w"), indent=1)
        # bracket extensions (P50 card 4.4): rounds over all lattices, at most MAX_EXT per lattice
        for rnd in range(AN.MAX_EXT):
            recs = AN.load_records(out)
            new = []
            for key in AN.ORDER:
                spec = AN.LATTICES[key]
                br, ch = AN.lattice_data(recs, key)
                S, W = AN.branch_lines(br, spec)
                rows = AN.phi_table(ch, S, W)
                need = AN.extensions_needed(rows)
                used = st["ext"].setdefault(key, [])
                for b in need:
                    if len(used) < AN.MAX_EXT:
                        used.append(int(b))
                        new += [mk(key, "mixed", b, c) for c in range(spec["chains"])]
                        log(out, f"extension {key}: add {b/AN.U:.4f} (phi at edge {rows[0]['phi'] if b < rows[0]['bn'] else rows[-1]['phi']:.3f})")
            json.dump(st, open(stp, "w"), indent=1)
            if not new:
                break
            run(ex, out, sim_dir, orig_file, new)
        st["complete"] = time.strftime('%Y-%m-%dT%H:%M:%S')
        json.dump(st, open(stp, "w"), indent=1)
        log(out, "DRIVER COMPLETE -- next: dlbpr2_rules.py numbers OUTDIR, then hash dlbpr2_numbers.txt")
    finally:
        ex.shutdown()


if __name__ == "__main__":
    main()
