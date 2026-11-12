"""Gate DL-BETA -- assemble gate_DLBETA_RESULT.md from run/RESULT_template.md, out/tables.md and the
SHA-256 of every delivered file.  Usage: python3 -I assemble_result.py DELIVERDIR"""
import sys, os, re, hashlib

D = sys.argv[1]
tpl = open(os.path.join(D, "run", "RESULT_template.md")).read()
tables = open(os.path.join(D, "out", "tables.md")).read()
sec = {}
for m in re.finditer(r"^## (\S+)[^\n]*\n(.*?)(?=^## |\Z)", tables, re.S | re.M):
    sec[m.group(1)] = m.group(2).strip()
key = {"K3": "K3", "K4": "K4", "K5": "K5", "S1": "S1", "S2": "S2", "S3": "S3", "S4_L6": "S4_L6", "S4_L8": "S4_L8"}
for k, v in key.items():
    tag = f"<!--TABLE:{k}-->"
    assert tpl.count(tag) == 1, tag
    tpl = tpl.replace(tag, sec[v])
rows = []
for root, _, files in os.walk(D):
    for f in files:
        p = os.path.relpath(os.path.join(root, f), D)
        if p in ("gate_DLBETA_RESULT.md", "MANIFEST.sha256"):
            continue
        h = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
        rows.append((p, h, os.path.getsize(os.path.join(D, p))))
rows.sort()
ft = ["All under `audit/gates/DLBETA/`. `MANIFEST.sha256` lists every file including this one.",
      "Raw time series: `out/series/<stage>_series.npz` (E, E_s, E_t after every sweep, float64, key",
      "`<tag>__E` etc.) and `out/series/<stage>.jsonl` (one record per run, with its seed); consolidated",
      "bit-identically from the per-run files by `run/consolidate.py`.", "",
      "| file | bytes | SHA-256 |", "|---|---|---|"]
ft += [f"| `{p}` | {n} | `{h}` |" for p, h, n in rows]
tpl = tpl.replace("<!--FILES-->", "\n".join(ft))
assert "<!--" not in tpl
open(os.path.join(D, "gate_DLBETA_RESULT.md"), "w").write(tpl)
print(f"written; {len(rows)} files listed")
