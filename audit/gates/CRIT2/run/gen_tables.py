"""Fill {{PLACEHOLDERS}} in the result template with tables generated from raw outputs."""
import json, sys

OUT = "/root/crit2/out"
st = json.load(open(f"{OUT}/state.json"))
c12 = json.load(open(f"{OUT}/checks12.json"))


def rows(tag):
    return [json.loads(l) for l in open(f"{OUT}/{tag}.jsonl")]


def pair_table(tag, mark=None, errs=False):
    d = {}
    for r in rows(tag):
        d.setdefault(r["beta"], {})[r["start"]] = r
    if errs:
        out = ["| β | E hot | E cold | C hot | C cold | C_max |", "|---|---|---|---|---|---|"]
    else:
        out = ["| β | E hot | E cold | C hot | C cold | C_max |", "|---|---|---|---|---|---|"]
    for b in sorted(d):
        h, c = d[b]["hot"], d[b]["cold"]
        cm = max(h["C"], c["C"])
        bs = f"**{b:.4f}**" if mark is not None and abs(b - mark) < 1e-9 else f"{b:.4f}"
        cms = f"**{cm:.3f}**" if mark is not None and abs(b - mark) < 1e-9 else f"{cm:.3f}"
        if errs:
            out.append(f"| {bs} | {h['E']:.5f} ± {h['E_err']:.5f} | {c['E']:.5f} ± {c['E_err']:.5f} | "
                       f"{h['C']:.3f} ± {h['C_err']:.3f} | {c['C']:.3f} ± {c['C_err']:.3f} | {cms} |")
        else:
            out.append(f"| {bs} | {h['E']:.5f} | {c['E']:.5f} | {h['C']:.3f} | {c['C']:.3f} | {cms} |")
    return "\n".join(out)


def cold_table(tag):
    out = ["| β | E cold | C cold | seed |", "|---|---|---|---|"]
    for r in sorted(rows(tag), key=lambda r: r["beta"]):
        out.append(f"| {r['beta']:.4f} | {r['E']:.5f} ± {r['E_err']:.5f} | {r['C']:.3f} ± {r['C_err']:.3f} | {r['seed']} |")
    return "\n".join(out)


def mixed_table(tag):
    out = ["| β | E at start | E, mean of last 500 sweeps | E final | outcome | seed |", "|---|---|---|---|---|---|"]
    for r in sorted(rows(tag), key=lambda r: r["beta"]):
        out.append(f"| {r['beta']:.5f} | {r['E_initial']:.4f} | {r['E_last500']:.5f} | {r['E_final']:.5f} | "
                   f"{r['outcome']} | {r['seed']} |")
    return "\n".join(out)


def readings_table(tag):
    out = ["| β | E after 250, 500, 750, …, 2000 sweeps |", "|---|---|"]
    for r in sorted(rows(tag), key=lambda r: r["beta"]):
        out.append(f"| {r['beta']:.5f} | " + " ".join(f"{x:.3f}" for x in r["readings"][4::5]) + " |")
    return "\n".join(out)


def checks12():
    out = ["| Check | Lattice | Measured | Target | Deviation | Pass |", "|---|---|---|---|---|---|"]
    for name in ("hc", "d4"):
        g = c12["check1"][name]
        out.append(f"| 1 gauge invariance | {name.upper()} | max ΔE = {g['max_dE']:.1e}, max Δcos = {g['max_dcos_plaq']:.1e} | 0 | — | {'yes' if g['passed'] else 'NO'} |")
    for name in ("hc", "d4"):
        a = c12["check2"][name]["beta01"]
        out.append(f"| 2 β = 0.1, hot | {name.upper()} | ⟨cos⟩ = {a['cos']:.5f} ± {a['err']:.5f} | β/2 = 0.05 | {a['rel_dev']*100:+.2f}% | {'yes' if a['passed'] else 'NO'} |")
    for name in ("hc", "d4"):
        a = c12["check2"][name]["beta20"]
        tgt = "1/(4β)" if name == "hc" else "11/(64β)"
        out.append(f"| 2 β = 20, cold | {name.upper()} | E = {a['E']:.6f} ± {a['err']:.6f} | {tgt} = {a['target']:.6f} | {a['rel_dev']*100:+.2f}% | {'yes' if a['passed'] else 'NO'} |")
    return "\n".join(out)


def files():
    import hashlib, glob, os
    out = ["| File | SHA-256 |", "|---|---|"]
    paths = sorted(glob.glob("/root/crit2/code/*.py")) + ["/root/crit2/code/RESULT_template.md"]
    paths += sorted(glob.glob(f"{OUT}/*"))
    for p in paths:
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        sub = "run" if "/code/" in p else "out"
        out.append(f"| `{sub}/{os.path.basename(p)}` | `{h}` |")
    return "\n".join(out)


rep = {
    "{{FILES}}": files(),
    "{{CHECKS12}}": checks12(),
    "{{CHECK3}}": pair_table("check3", mark=st["check3"]["beta_Cmax"], errs=True),
    "{{CHECK4}}": mixed_table("check4"),
    "{{CHECK4_READ}}": readings_table("check4"),
    "{{S51}}": pair_table("s51", mark=st["s51"]["beta0"]),
    "{{S52}}": pair_table("s52", mark=st["s52"]["beta8"], errs=True),
    "{{S53}}": cold_table("s53"),
    "{{S54A}}": mixed_table("s54a"),
    "{{S54A_READ}}": readings_table("s54a"),
    "{{S54B}}": mixed_table("s54b"),
    "{{S54B_READ}}": readings_table("s54b"),
}
tpl = open(sys.argv[1]).read()
for k, v in rep.items():
    assert k in tpl, k
    tpl = tpl.replace(k, v)
assert "{{" not in tpl
open(sys.argv[2], "w").write(tpl)
print("written", sys.argv[2])
