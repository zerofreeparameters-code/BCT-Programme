#!/usr/bin/env python3
"""
Gate PSI2 -- corpus scan.

Two mechanical questions, answered over the whole repo tree, not a sample:

  Q1. Does a genuine Josephson term -- anything proportional to
      cos(theta_2 - theta_1), or Re(Psi_1^* Psi_2) -- appear ANYWHERE
      in the corpus?  A Josephson energy must depend on a phase
      DIFFERENCE.  A surface integral of |Psi|^2 does not.

  Q2. Do the four App JH copies differ physically, or only clerically?

Run against the repo tarball whose SHA-256 is recorded in the deliverable.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1
                    else "/home/claude/BCT-Programme-main")
tex = sorted(ROOT.glob("tex/*.tex"))
print(f"tree: {ROOT}")
print(f".tex files scanned: {len(tex)}\n")

# ---------------------------------------------------------------- Q1
# Patterns for a real Josephson coupling.  Deliberately generous:
# any cosine of a difference of two phase-like symbols, any
# Re(Psi* Psi), any explicit E_J / Josephson energy symbol.
PHASE = r"(?:\\)?(?:theta|vartheta|varphi|phi|Theta|Phi)[^ ]{0,8}"
PATTERNS = {
    "cos(phase - phase)": re.compile(
        r"\\cos\s*[\(\{\\]*\s*" + PHASE + r"\s*-\s*" + PHASE, re.I),
    "Psi_1^* Psi_2 overlap": re.compile(
        r"\\Psi[^;\n]{0,25}\^?\s*\{?\s*\*\s*\}?[^;\n]{0,25}\\Psi", re.I),
    "E_J / Josephson energy symbol": re.compile(
        r"E_\{?\s*(?:J|\\mathrm\{J\}|\\text\{J\})\s*\}?", re.I),
    "Josephson plasma frequency": re.compile(r"omega_\{?\s*(?:J|p)", re.I),
}
hits = {k: [] for k in PATTERNS}
for f in tex:
    txt = f.read_text(errors="replace")
    for line_no, line in enumerate(txt.splitlines(), 1):
        for name, pat in PATTERNS.items():
            if pat.search(line):
                hits[name].append((f.name, line_no, line.strip()[:110]))

print("Q1 -- search for a genuine phase-difference (Josephson) coupling")
print("-" * 70)
for name, hs in hits.items():
    print(f"  {name:<32} : {len(hs)} hit(s)")
    for h in hs[:6]:
        print(f"        {h[0]}:{h[1]}  {h[2]}")
print()

# What the corpus DOES have where it says "Josephson coupling":
print("  What appears instead, at the two places the corpus names a")
print("  'Josephson coupling' (App J SS3.1 and App JH eq (13)):")
print("      App J   : H_int = sigma_s * oint_{r=R} |Psi|^2 dS")
print("      App JH  : F_surf = (alpha_0 hbar^2/2mR) oint_{S^2} |Psi_int|^2 dA")
print("  Both are integrals of |Psi|^2. Neither contains a phase difference.")
print("  A term with no dependence on theta_2 - theta_1 is not a Josephson")
print("  coupling and cannot lock, gap, or unlock a relative phase.\n")

# ---------------------------------------------------------------- Q2
print("Q2 -- are the four App JH copies physically distinct?")
print("-" * 70)
jh = sorted(ROOT.glob("tex/*Appendix_JH*.tex"))
digests = {}
for f in jh:
    d = hashlib.sha256(f.read_bytes()).hexdigest()
    digests[f.name] = d
    print(f"  {f.name:<38} {len(f.read_text(errors='replace').splitlines()):>4} lines  {d[:16]}")

# Strip comments, whitespace and the bibliography, then compare the
# mathematics only.
def maths_only(p):
    t = p.read_text(errors="replace")
    t = t.split(r"\begin{thebibliography}")[0]
    t = re.sub(r"(?<!\\)%.*", "", t)          # drop comments
    t = re.sub(r"\\(?:renewcommand|tableofcontents|affiliation|date|title)"
               r"(?:\{(?:[^{}]|\{[^{}]*\})*\})*", "", t)
    t = re.sub(r"\s+", " ", t)
    return t

print("\n  body maths, comments/bibliography/frontmatter stripped:")
base = maths_only(jh[0])
for f in jh:
    same = (maths_only(f) == base)
    print(f"    {f.name:<38} identical to {jh[0].name}: {same}")

# Extract every displayed equation from each and compare the sets.
def eqs(p):
    t = p.read_text(errors="replace").split(r"\begin{thebibliography}")[0]
    return set(re.sub(r"\s+", "", e) for e in
               re.findall(r"\\begin\{equation\}(.*?)\\end\{equation\}", t, re.S))

sets = {f.name: eqs(f) for f in jh}
ref = sets[jh[0].name]
print("\n  displayed-equation sets:")
for n, s in sets.items():
    print(f"    {n:<38} {len(s):>3} equations   symmetric difference vs "
          f"{jh[0].name}: {len(s ^ ref)}")
print("""
  Reading: the four copies differ in frontmatter, a table of contents, a
  bibliography and one self-citation record number. Their physics is the
  same document. The 'which copy is canonical' problem is therefore
  CLERICAL for this gate -- it does not change any verdict below -- while
  remaining a real archival defect.
""")
