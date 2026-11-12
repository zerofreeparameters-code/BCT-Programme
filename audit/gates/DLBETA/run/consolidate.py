"""Gate DL-BETA -- consolidate the per-run raw files (out/raw/<stage>/<tag>.json|.npz) into one JSONL
(run records, every seed) and one NPZ (full E, E_s, E_t series after every sweep, float64) per stage,
and check that the consolidated arrays are bit-identical to the per-run files.
Usage: python3 -I consolidate.py OUTDIR DESTDIR"""
import sys, os, json, glob
import numpy as np

OUT, DEST = sys.argv[1], sys.argv[2]
os.makedirs(DEST, exist_ok=True)
for sd in sorted(glob.glob(os.path.join(OUT, "raw", "*"))):
    stage = os.path.basename(sd)
    recs, arrs = [], {}
    for jp in sorted(glob.glob(os.path.join(sd, "*.json"))):
        rec = json.load(open(jp))
        z = np.load(jp[:-5] + ".npz")
        recs.append(rec)
        for k in ("E", "Es", "Et"):
            arrs[f"{rec['tag']}__{k}"] = z[k]
    recs.sort(key=lambda r: (r["beta"], r["start"], r["tag"]))
    with open(os.path.join(DEST, f"{stage}.jsonl"), "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    np.savez_compressed(os.path.join(DEST, f"{stage}_series.npz"), **arrs)
    z = np.load(os.path.join(DEST, f"{stage}_series.npz"))
    for r in recs:
        zz = np.load(os.path.join(sd, r["tag"] + ".npz"))
        for k in ("E", "Es", "Et"):
            assert np.array_equal(z[f"{r['tag']}__{k}"], zz[k])
    print(f"{stage}: {len(recs)} runs, {sum(r['n_sweeps'] for r in recs)} sweeps, bit-identical")
