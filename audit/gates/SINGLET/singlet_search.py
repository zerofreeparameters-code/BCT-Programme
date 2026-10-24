#!/usr/bin/env python3
"""
Gate SINGLET -- corpus search over exactly the files card Sec.0.2 allows (plus JH4, disclosed).
Usage: python3 -I singlet_search.py <repo_root> <letter254_at_501ea79.tex> [outfile]
Counts hits per term group per file and prints every hit line for the ingredient groups, so that
'NONE FOUND' in the RESULT is reproducible. Case-insensitive substring unless noted.
"""
import os
import re
import sys

repo, l254 = sys.argv[1], sys.argv[2]
outfile = sys.argv[3] if len(sys.argv) > 3 else "singlet_search_output.txt"
FILES = {
    "L254@501ea79": l254,
    "AppJH_FINAL": os.path.join(repo, "tex/BCT_Appendix_JH_FINAL.tex"),
    "AppJ": os.path.join(repo, "tex/BCT_Appendix_J_SphereAction.tex"),
    "AZ6": os.path.join(repo, "tex/BCT_Appendix_AZ6.tex"),
    "AZ7": os.path.join(repo, "tex/BCT_Appendix_AZ7.tex"),
    "L36_OHC": os.path.join(repo, "tex/BCT_Letter36_OHC_tex.tex"),
    "L60": os.path.join(repo, "tex/BCT_Letter60.tex"),
    "L64": os.path.join(repo, "tex/BCT_Letter64.tex"),
    "OneMedium": os.path.join(repo, "tex/BCT_OneMedium_JournalEdition_v2.txt"),
    "Monograph_PLB(search)": os.path.join(repo, "tex/BCT_Monograph_PLB.tex"),
    "AppJH4(disclosed)": os.path.join(repo, "tex/BCT_Appendix_JH4_YangMills_v2_CORRECTED.tex"),
}
GROUPS = {
    "(i) stochastic process": [r"stochastic", r"markov", r"random walk", r"random", r"transfer (matrix|operator)",
                               r"master equation", r"langevin", r"fokker", r"noise", r"diffus", r"heat kernel",
                               r"path integral", r"partition function", r"probability measure"],
    "(ii) Z2 / double cover": [r"double cover", r"antiperiod", r"anti-period", r"spin structure", r"holonomy",
                               r"half-quantum", r"half quantum", r"half-integer", r"\\mathbb\{Z\}_2", r"Z_2",
                               r"spinor", r"SU\(2\)", r"4\\pi", r"720", r"\\pi phase|phase of \$\\pi\$|\u03c0 phase"],
    "(iii) readout rule": [r"\bborn\b", r"measurement", r"readout", r"read out", r"projector", r"probabilit",
                           r"\|\^2|\|\^\{2\}", r"modulus", r"expectation value"],
    "carrier: C^2 / S^2 / S^3": [r"mathbb\{C\}\^2", r"C\^2", r"two-component", r"S\^2", r"S\^3", r"pi_3", r"pi_1",
                                 r"\\psi_\+|\\psi_-", r"qubit", r"bloch"],
    "Bell vocabulary": [r"\bbell\b", r"chsh", r"tsirelson", r"entangl", r"singlet", r"signed", r"negative prob",
                        r"quasi"],
}
out = []
def say(s=""):
    s = s.rstrip(); print(s); out.append(s)

say("files searched (card Sec.0.2 list; JH4 disclosed as a separate appendix, not a JH version):")
for k, p in FILES.items():
    say("  %-24s %s" % (k, os.path.relpath(p, repo) if p.startswith(repo) else p))
texts = {k: open(p, encoding="utf-8", errors="replace").read().split("\n") for k, p in FILES.items()}
for g, pats in GROUPS.items():
    say(""); say("=" * 78); say(g); say("=" * 78)
    for pat in pats:
        rx = re.compile(pat, re.I)
        counts = {k: sum(1 for ln in L if rx.search(ln)) for k, L in texts.items()}
        tot = sum(counts.values())
        say("  %-38s total %3d | %s" % (pat, tot, ", ".join("%s:%d" % (k, c) for k, c in counts.items() if c)))
    say("  -- hit lines --")
    seen = set()
    for k, L in texts.items():
        for i, ln in enumerate(L, 1):
            if any(re.search(p, ln, re.I) for p in pats) and (k, i) not in seen:
                seen.add((k, i))
                say("    %s:%d: %s" % (k, i, ln.strip()[:150]))
with open(outfile, "w") as fh:
    fh.write("\n".join(out) + "\n")
