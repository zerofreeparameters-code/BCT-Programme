"""
Gate DL-BETA REP1 -- markdown tables for the result file, from out/state.json and out/records/.
Usage: python -I dlbr_tables.py OUTDIR  -> OUTDIR/tables.md
"""
import os, sys, json

OUT = sys.argv[1]
U = 1e7
st = json.load(open(os.path.join(OUT, "state.json")))


def rec(stage, kind, L, bn, start):
    tag = f"{stage}_{kind}_L{L}_b{bn:09d}_{start}"
    return json.load(open(os.path.join(OUT, "records", tag + ".json")))


def b(n, d=4):
    v = n / U
    s = f"{v:.{d}f}"
    ex = f"{v:.7f}".rstrip("0").rstrip(".")
    return s if abs(float(s) - v) < 1e-12 else f"{s} [{ex}]"


T = []
w = T.append


def scan(stage, kind, L, d, mark=(), void=True):
    g = st[stage]["grid"]
    w(f"| β | E hot | E cold | C hot | C cold | C_max | seeds (hot, cold) |")
    w("|---|---|---|---|---|---|---|")
    for bn in g:
        h, c = rec(stage, kind, L, bn, "hot"), rec(stage, kind, L, bn, "cold")
        cm = max(h["C"], c["C"])
        bb = f"**{b(bn, d)}**" if bn in mark else b(bn, d)
        w(f"| {bb} | {h['E']:.5f} ± {h['E_err']:.5f} | {c['E']:.5f} ± {c['E_err']:.5f} | {h['C']:.3f} ± {h['C_err']:.3f} | "
          f"{c['C']:.3f} ± {c['C_err']:.3f} | {cm:.3f} | {h['seed']}, {c['seed']} |")
    w("")


w("### K4 — Z4, L = 8, hot and cold, 1000 + 3000 sweeps")
scan("K4", "z4", 8, 4, mark=(st["K4"]["beta_Cmax"],))
w("### K5 — Z4, L = 12, mixed start, 2000 sweeps, band E\\*_hc ± 0.01")
w("| β | E at start | E_end (mean of readings 1550–2000) | E final | outcome | seed |")
w("|---|---|---|---|---|---|")
for bn, o in zip(st["K5"]["grid"], st["K5"]["outcomes"]):
    r = rec("K5", "z4", 12, bn, "mixed")
    w(f"| {b(bn)} | {r['E_start']:.5f} | {r['E_end']:.5f} | {r['E_final']:.5f} | {o} | {r['seed']} |")
w("")
w("### Stage 1 — locate, void L = 2, L_t = 6 (full table in `out/S1_table.md`)")
g = st["S1"]["grid"]
i0 = g.index(st["S1"]["beta0"])
full = []
full.append("| β | E hot | E cold | C hot | C cold | C_max |")
full.append("|---|---|---|---|---|---|")
for bn in g:
    h, c = rec("S1", "void", 2, bn, "hot"), rec("S1", "void", 2, bn, "cold")
    full.append(f"| {b(bn,2)} | {h['E']:.5f} | {c['E']:.5f} | {h['C']:.3f} | {c['C']:.3f} | {max(h['C'], c['C']):.3f} |")
open(os.path.join(OUT, "S1_table.md"), "w").write("\n".join(full) + "\n")
w(full[0]); w(full[1])
for k in range(max(0, i0 - 8), min(len(g), i0 + 9)):
    line = full[2 + k]
    if k == i0:
        line = line.replace(f"| {b(g[k],2)} |", f"| **{b(g[k],2)}** |", 1)
    w(line)
w("")
w("### Stage 2 — fine scan, void L = 4, L_t = 12, 2000 + 4000 sweeps")
scan("S2", "void", 4, 3, mark=(st["S2"]["beta4"],))
w("### Stage 3 — scan, void L = 6, L_t = 18, hot and cold (C2), 500 + 1500 sweeps")
scan("S3", "void", 6, 3, mark=tuple(st["S3"]["cold_jump"]))
for stage, L in (("S4a", 6), ("S4b", 8)):
    sx = st[stage]
    if not sx.get("run", True):
        continue
    w(f"### Stage 4 — mixed-phase starts, void L = {L}, L_t = {3*L}, 2000 sweeps")
    w("| β | E at start | E_end | S(β) | W(β) | f | primary (C1) | secondary (E\\* ± 0.01) | seed |")
    w("|---|---|---|---|---|---|---|---|---|")
    for r in sx["runs"]:
        f = "—" if r["f"] != r["f"] else f"{r['f']:.3f}"
        w(f"| {b(r['bn'])} | {r['E_start']:.5f} | {r['E_end']:.5f} | {r['S']:.5f} | {r['W']:.5f} | {f} | {r['primary']} | {r['secondary']} | {r['seed']} |")
    w("")
    w(f"Readings (E after sweeps 250, 500, …, 2000):")
    w("")
    w("| β | readings |")
    w("|---|---|")
    for r in sx["runs"]:
        rr = rec(stage, "void", L, r["bn"], "mixed")["readings"]
        w(f"| {b(r['bn'])} | " + " ".join(f"{x:.4f}" for x in rr[4::5]) + " |")
    w("")
s6 = st["S6"]
w(f"### Stage 6 — histogram, void L = 6, β = {b(s6['bn'])}, mixed start, seed {s6['seed']}, 2000 + 20,000 sweeps")
w(f"B = {s6['B']:.6f}; ⟨E⟩ = {s6['E']:.5f} ± {s6['E_err']:.5f}; peaks (bins) {s6['peaks']}; two peaks: {s6['two_peaks']} {s6['pair'] or ''}")
w("")
w("Counts (50 bins over [min E, max E] = [" + f"{s6['edges'][0]:.5f}, {s6['edges'][-1]:.5f}]):")
w("")
w("`" + " ".join(str(c) for c in s6["counts"]) + "`")
w("")
open(os.path.join(OUT, "tables.md"), "w").write("\n".join(T) + "\n")
print("\n".join(T))
