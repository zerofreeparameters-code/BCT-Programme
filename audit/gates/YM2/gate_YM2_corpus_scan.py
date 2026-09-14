#!/usr/bin/env python3
"""
Gate YM2 — as-run search-space audit.
Locates every JH4 version, counts .tex, and scans the appendix volumes for
Yang-Mills / Millennium tiering language. Run from repo root.
Model: Claude Opus 4.8. Corpus commit 12ae196.
"""
import glob, re, subprocess, os, pymupdf

print("== .tex counts ==")
tex_all  = subprocess.run("find . -name '*.tex'", shell=True, capture_output=True, text=True).stdout.split()
tex_root = subprocess.run("find . -maxdepth 1 -name '*.tex'", shell=True, capture_output=True, text=True).stdout.split()
print(f"  total .tex: {len(tex_all)} (prompt states 134); root .tex: {len(tex_root)} (prompt states 26)")

print("== JH4 filename matches ==")
for f in glob.glob("tex/*JH4*"): print("  ", f)

print("== JH-family siblings (title line) ==")
for f in sorted(glob.glob("tex/BCT_Appendix_JH*.tex")):
    txt = open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'(SU\(2\)|SU\(3\)|Yang.?Mills|Geometrically.?Fixed|Partially Dual)[^\n]{0,60}', txt)
    print(f"  {os.path.basename(f):45s} -> {m.group(0)[:60] if m else '?'}")

print("== appendix-volume Millennium/Clay tiering lines ==")
vols = sorted(glob.glob("BCT_Appendices_Volume1_2026_compressed_Part*.pdf"))
v2 = "/home/claude/vol2/BCT_Appendices_Volume2_2026 (1)-compressed.pdf"
if os.path.exists(v2): vols.append(v2)
pat = re.compile(r'Conjectured|not a mathematical proof|Clay sense|Millennium', re.I)
for f in vols:
    doc = pymupdf.open(f)
    for i, pg in enumerate(doc):
        for line in pg.get_text().splitlines():
            if pat.search(line):
                print(f"  {os.path.basename(f)} p{i+1}: {line.strip()[:90]}")
