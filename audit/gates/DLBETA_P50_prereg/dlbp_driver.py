"""
Gate DL-BETA P50 -- driver (pre-registered with the card). Runs K1, K2, every branch run and mixed-start chain
of card section 4.4, applies the bracket-extension rule, and writes the records. The simulator is Gate
DL-BETA REP1's dlbr_sim.py, unmodified, called through get_lattice() and run_chain() with this card's seeds.

Usage:  nohup python3 -I dlbp_driver.py SIM_DIR REP1_SERIES_DIR OUTDIR [WORKERS] > OUTDIR/driver_stdout.txt 2>&1 &
  SIM_DIR          directory holding REP1's dlbr_sim.py (hash-checked)
  REP1_SERIES_DIR  REP1's out/series (for K2's bit-reproduction comparison)
  WORKERS          parallel chains (default: os.cpu_count())
Then: python3 -I dlbp_analysis.py numbers OUTDIR ; hash ; python3 -I dlbp_analysis.py verdict OUTDIR
Dry run (code paths only, tiny lattices, seeds + 9,000,000): DLBP_DRYRUN=1 in the environment.
"""
import os, sys, json, time, hashlib
import numpy as np
from concurrent.futures import ProcessPoolExecutor, wait as fwait

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dlbp_analysis as AN

SIM_SHA256 = "560c256fe391bfa7b0a2bf4e5abc520f8179b75647ece51006b5cba82425c9e6"   # Gate DL-BETA REP1 run/dlbr_sim.py
DRY = os.environ.get("DLBP_DRYRUN") == "1"


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
    n_th, n_me = (AN.N_BRANCH if role in ("hot", "cold") else (0, AN.N_MIXED))
    return dict(tag=f"{lat}_b{bn:09d}_{role}_c{c}", lat=lat, kind=spec["kind"], L=spec["L"], bn=int(bn), role=role,
                chain=c, s=s, seed=AN.seed(spec["kind"], spec["L"], bn, s, c) + (9000000 if DRY else 0),
                n_therm=n_th, n_meas=n_me)


def mk_k2(name, kind, L, beta, start, seed, rep1_file):
    return dict(tag=f"K2_{name}", lat="K2", kind=kind, L=L, bn=int(round(beta * AN.U)), role="k2_" + start, chain=0,
                s=-1, seed=seed, n_therm=1000, n_meas=10000, rep1_file=rep1_file)


def worker(t):
    sys.path.insert(0, t["sim_dir"])
    import dlbr_sim as S
    lat = S.get_lattice(t["kind"], t["L"])
    st = {"hot": 0, "cold": 1, "mixed": 2, "k2_hot": 0, "k2_cold": 1}[t["role"]]
    n = t["n_therm"] + t["n_meas"]
    t0 = time.time()
    ser = S.run_chain(int(t["seed"]), st, lat["mask"], t["bn"] / AN.U, n, lat["ptr"], lat["oth"], lat["osg"],
                      lat["loops"], lat["signs"], lat["ltype"])
    dt = time.time() - t0
    rec = {k: t[k] for k in ("tag", "lat", "kind", "L", "bn", "role", "chain", "s", "seed", "n_therm", "n_meas")}
    rec.update(beta=t["bn"] / AN.U, Np=int(lat["meta"]["Np"]), seconds=dt, ms_per_sweep=1e3 * dt / n,
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
        ref = t["rep1_file"]
        rec["bit_identical"] = bool(ref and os.path.exists(ref) and np.array_equal(np.load(ref)["series"], ser))
    fn = os.path.join(t["out"], "series", t["tag"] + ".npz")
    np.savez_compressed(fn, series=ser, seed=t["seed"], beta=t["bn"] / AN.U, tag=t["tag"])
    rec["series_file"] = os.path.basename(fn)
    rec["series_sha256"] = sha256(fn)
    rec["finished"] = time.strftime('%Y-%m-%dT%H:%M:%S')
    p = os.path.join(t["out"], "records", t["tag"] + ".json")
    json.dump(rec, open(p + ".tmp", "w"), default=float)
    os.replace(p + ".tmp", p)
    return rec


COST = {("z4", 8): 9, ("z4", 12): 53, ("void", 6): 85, ("void", 8): 255, ("void", 2): 1, ("void", 3): 3,
        ("z4", 4): 1, ("z4", 6): 4}


def have(out, tag):
    p = os.path.join(out, "records", tag + ".json")
    if not os.path.exists(p):
        return False
    r = json.load(open(p))
    f = os.path.join(out, "series", r["series_file"])
    return os.path.exists(f) and sha256(f) == r["series_sha256"]


def run(ex, out, sim_dir, tasks):
    todo = [dict(t, out=out, sim_dir=sim_dir) for t in tasks if not have(out, t["tag"])]
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
    sim_dir, rep1_series, out = [os.path.abspath(x) for x in sys.argv[1:4]]
    nw = int(sys.argv[4]) if len(sys.argv) > 4 else os.cpu_count()
    for d in ("series", "records"):
        os.makedirs(os.path.join(out, d), exist_ok=True)
    stp = os.path.join(out, "state.json")
    st = json.load(open(stp)) if os.path.exists(stp) else {"ext": {}}
    log(out, f"driver start; workers {nw}; dry run {DRY}")
    # K1 -- the simulator is REP1's, unmodified
    h = sha256(os.path.join(sim_dir, "dlbr_sim.py"))
    st["K1"] = {"dlbr_sim_sha256": h, "expected": SIM_SHA256, "pass": h == SIM_SHA256}
    log(out, f"K1 dlbr_sim.py sha256 {h} -> {'PASS' if st['K1']['pass'] else 'FAIL'}")
    json.dump(st, open(stp, "w"), indent=1)
    if not st["K1"]["pass"] and not DRY:
        log(out, "STOP: K1 failed (SC-DLBP-0)")
        return
    # fixed tasks: K2 (REP1's K3 runs, same seeds), every branch run, every window chain
    k2 = [mk_k2("void_b0.1_hot", "void", 2, 0.1, "hot", 716838, os.path.join(rep1_series, "k3_void_L2_b0.1_hot.npz")),
          mk_k2("void_b20_cold", "void", 2, 20.0, "cold", 915839, os.path.join(rep1_series, "k3_void_L2_b20_cold.npz")),
          mk_k2("z4_b0.1_hot", "z4", 4, 0.1, "hot", 332676, os.path.join(rep1_series, "k3_z4_L4_b0.1_hot.npz")),
          mk_k2("z4_b20_cold", "z4", 4, 20.0, "cold", 531677, os.path.join(rep1_series, "k3_z4_L4_b20_cold.npz"))]
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
        run(ex, out, sim_dir, tasks)
        recs = AN.load_records(out)
        # K2 evaluation (REP1 K3 criteria: within 2 %)
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
            log(out, f"K2 {t['tag']}: {val:.6f} vs {target:.6f} ({100*dev:+.2f}%), bit-identical to REP1: {r['bit_identical']}")
        json.dump(st, open(stp, "w"), indent=1)
        # bracket extensions (card 4.4): rounds over all lattices, at most MAX_EXT per lattice
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
            run(ex, out, sim_dir, new)
        st["complete"] = time.strftime('%Y-%m-%dT%H:%M:%S')
        json.dump(st, open(stp, "w"), indent=1)
        log(out, "DRIVER COMPLETE -- next: dlbp_analysis.py numbers OUTDIR, then hash dlbp_numbers.txt")
    finally:
        ex.shutdown()


if __name__ == "__main__":
    main()
