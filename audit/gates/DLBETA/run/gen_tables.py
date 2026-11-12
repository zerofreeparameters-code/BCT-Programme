"""Gate DL-BETA -- markdown tables for the RESULT, from out/state.json.  Usage: python3 -I gen_tables.py OUTDIR"""
import sys, os, json

OUT = sys.argv[1]
st = json.load(open(os.path.join(OUT, "state.json")))
o = []
w = o.append


def scan_table(tab, starts, mark=None, errs=True):
    bs = sorted(tab, key=float)
    if len(starts) == 2:
        w("| β | E hot | E cold | C hot | C cold | C_max |")
        w("|---|---|---|---|---|---|")
        for b in bs:
            h, c = tab[b]["hot"], tab[b]["cold"]
            cm = max(h["C"], c["C"])
            bb = f"**{float(b):.4f}**" if mark is not None and abs(float(b) - mark) < 1e-9 else f"{float(b):.4f}"
            if errs:
                w(f"| {bb} | {h['E']:.5f} ± {h['E_err']:.5f} | {c['E']:.5f} ± {c['E_err']:.5f} | "
                  f"{h['C']:.3f} ± {h['C_err']:.3f} | {c['C']:.3f} ± {c['C_err']:.3f} | {cm:.3f} |")
            else:
                w(f"| {bb} | {h['E']:.5f} | {c['E']:.5f} | {h['C']:.3f} | {c['C']:.3f} | {cm:.3f} |")
    else:
        w("| β | E cold | E_s (rhombi) | E_t (temporal) | E_t/E_s | C cold | seed |")
        w("|---|---|---|---|---|---|---|")
        for b in bs:
            c = tab[b]["cold"]
            w(f"| {float(b):.4f} | {c['E']:.5f} ± {c['E_err']:.5f} | {c['Es']:.5f} | {c['Et']:.5f} | "
              f"{c['Et']/c['Es']:.4f} | {c['C']:.3f} ± {c['C_err']:.3f} | {c['seed']} |")


def mixed_table(m):
    w(f"E* = {m['Estar']:.5f}; strong wins above {m['Estar']+0.01:.5f}, weak wins below {m['Estar']-0.01:.5f}.")
    w("")
    w("| β | E at start | E, mean of readings 1550–2000 | E final | E_s, E_t (same readings) | outcome | seed |")
    w("|---|---|---|---|---|---|---|")
    for r in m["rows"]:
        w(f"| {r['beta']:.5f} | {r['E_start']:.4f} | {r['E_last10']:.5f} | {r['E_final']:.5f} | "
          f"{r['Es_last10']:.5f}, {r['Et_last10']:.5f} | {r['outcome']} | {r['seed']} |")
    w("")
    w("| β | E after 250, 500, 750, …, 2000 sweeps |")
    w("|---|---|")
    for r in m["rows"]:
        rd = r["readings"]
        w(f"| {r['beta']:.5f} | " + " ".join(f"{rd[k]:.4f}" for k in range(4, 40, 5)) + " |")


w("## K3")
w("| run | seed | measured | target | deviation | pass |")
w("|---|---|---|---|---|---|")
for t, r in st["K3"].items():
    q = "⟨cos⟩" if r["beta"] == 0.1 else "E"
    w(f"| {r['lattice']} L={r['L']}{' Lt='+str(r['Lt']) if r['Lt'] else ''} β={r['beta']} {r['start']} | {r['seed']} | "
      f"{q} = {r['measured']:.6f} ± {r['err']:.6f} | {r['target']:.6f} | {100*r['rel_dev']:+.2f} % | {'yes' if r['pass_'] else 'NO'} |")
w("")
w("## K4")
scan_table(st["K4"]["table"], ("hot", "cold"), mark=st["K4"]["beta_Cmax"])
w("")
if "K5" in st:
    w("## K5")
    mixed_table(st["K5"])
    w("")
if "S1" in st:
    w("## S1 locate")
    scan_table(st["S1"]["table"], ("hot", "cold"), mark=st["S1"]["beta0"], errs=False)
    w("")
if "S2" in st:
    w("## S2 fine")
    scan_table(st["S2"]["table"], ("hot", "cold"), mark=st["S2"]["beta4"])
    w("")
    w("E_s and E_t, L = 4:")
    w("| β | E_s hot | E_t hot | E_s cold | E_t cold | E_t/E_s cold |")
    w("|---|---|---|---|---|---|")
    for b in sorted(st["S2"]["table"], key=float):
        h, c = st["S2"]["table"][b]["hot"], st["S2"]["table"][b]["cold"]
        w(f"| {float(b):.4f} | {h['Es']:.5f} | {h['Et']:.5f} | {c['Es']:.5f} | {c['Et']:.5f} | {c['Et']/c['Es']:.4f} |")
    w("")
if "S3" in st:
    w("## S3 cold")
    scan_table(st["S3"]["table"], ("cold",))
    w("")
for k in ("S4_L6", "S4_L8"):
    if k in st:
        w(f"## {k}")
        mixed_table(st[k])
        w("")
txt = "\n".join(o) + "\n"
open(os.path.join(OUT, "tables.md"), "w").write(txt)
print(txt)
