#!/usr/bin/env python3
"""Gate PILOT corpus search. Usage: search.py <repo_root> <text_dir> <terms_set>
Counts hits per term over (a) every .tex outside audit/ in the pinned tree and
(b) the Volume PDF text layers. Case-insensitive for word terms, literal for
LaTeX terms. Prints term, total hits, file count, and files."""
import os, re, sys, json

repo, textdir, which = sys.argv[1], sys.argv[2], sys.argv[3]

DYN_TEX = [r"\partial_t", r"\dot", r"i\hbar", r"\partial_\mu", r"\Box",
           "Bogoliubov", "dispersion", "omega(k)", "group velocity",
           "phase velocity", "superlumin", r"v_{\rm ph}", "healing"]
# PDF text-layer equivalents of the LaTeX tokens (unicode as typeset)
DYN_PDF_EXTRA = {r"\partial_t": ["∂t", "∂_t", "∂/∂t"], r"i\hbar": ["iℏ", "iħ", "i ℏ", "i ħ"],
                 r"\partial_\mu": ["∂μ", "∂_μ"], r"\Box": ["□", "◻"],
                 "omega(k)": ["ω(k)", "ω(𝑘)", "ω(q)", "ω²(k)", "ω2(k)"],
                 r"\dot": ["φ̇", "ψ̇", "θ̇", "Φ̇", "Ψ̇"], r"v_{\rm ph}": ["vph", "v_ph"]}
QM = ["entangle", "Bell", "CHSH", "Tsirelson", "nonlocal", "non-local", "pilot",
      "Bohm", "de Broglie", "hidden variable", "configuration space", "Born",
      "collapse", "superposition", "wave functional", "Fock", "second quantis"]

SUPP = ["\\hat{a}", "creation", "annihilation", "Hilbert", "wavefunction", "wave function",
        "second-quantis", "second quantiz", "second-quantiz", "quantum field", "Bose-Hubbard",
        "path integral", "commutat"]
terms = {"dyn": DYN_TEX, "qm": QM, "supp": SUPP}[which]
latexy = {r"\partial_t", r"\dot", r"i\hbar", r"\partial_\mu", r"\Box", r"v_{\rm ph}"}
# proper nouns / acronyms: case-sensitive whole word, so lower-case citation keys
# (\cite{chsh}, \bibitem{tsirelson}) and 'Belle'/'Bells' are not counted
case_sensitive = {"Bell", "Born", "Bohm", "Fock", "CHSH", "Tsirelson"}

def load_tex():
    out = {}
    for root, dirs, files in os.walk(repo):
        rel = os.path.relpath(root, repo)
        if rel.split(os.sep)[0] in ("audit", ".git"):
            continue
        for f in files:
            if f.endswith(".tex"):
                p = os.path.join(root, f)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    out[os.path.relpath(p, repo)] = fh.read()
    return out

def load_pdf():
    out = {}
    for f in sorted(os.listdir(textdir)):
        if f.endswith(".txt"):
            with open(os.path.join(textdir, f), encoding="utf-8", errors="replace") as fh:
                out["PDF:" + f] = fh.read()
    return out

def count(text, term, pdf=False):
    pats = [term]
    if pdf and term in DYN_PDF_EXTRA:
        pats = pats + DYN_PDF_EXTRA[term]
    n = 0
    for p in pats:
        if p in latexy and not pdf:
            # LaTeX token: literal, and for \dot / \Box require non-letter after
            n += len(re.findall(re.escape(p) + r"(?![A-Za-z])", text))
        elif p in latexy and pdf:
            continue  # LaTeX source tokens do not survive typesetting
        elif term in case_sensitive:
            # whole word: 'Bell' must not count 'Belle' (experiment) or 'Bells'
            n += len(re.findall(r"\b" + re.escape(p) + r"\b", text))
        elif p == "\\hat{a}":
            n += text.count(p)
        else:
            n += len(re.findall(re.escape(p), text, flags=re.I))
    return n

tex, pdf = load_tex(), load_pdf()
res = {}
for t in terms:
    tf = {k: count(v, t) for k, v in tex.items()}
    pf = {k: count(v, t, pdf=True) for k, v in pdf.items()}
    tf = {k: n for k, n in tf.items() if n}
    pf = {k: n for k, n in pf.items() if n}
    res[t] = {"tex_hits": sum(tf.values()), "tex_files": len(tf),
              "pdf_hits": sum(pf.values()), "pdf_files": len(pf),
              "tex": dict(sorted(tf.items(), key=lambda x: -x[1])), "pdf": pf}
print(f"# .tex files searched: {len(tex)}; PDF text layers: {len(pdf)}")
for t, r in res.items():
    print(f"{t!r:22} tex {r['tex_hits']:5d} hits/{r['tex_files']:3d} files | PDF {r['pdf_hits']:5d} hits/{r['pdf_files']} vols")
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"search_{which}.json"), "w"), indent=1)
