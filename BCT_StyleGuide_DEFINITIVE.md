# BCT SUPERFLUID LATTICE MODEL
# ══════════════════════════════════════════════════
# DEFINITIVE DOCUMENT STYLE GUIDE — v2.0
# 23 March 2026 — LOCKED, never alter
# ══════════════════════════════════════════════════

## THE SINGLE GOLDEN RULE

> **BCT Letters are LaTeX documents.**
> They look like Physical Review Letters, 1965.
> Computer Modern serif. Old-world. Timeless.
> Wallpaper-worthy.

Python/ReportLab PDFs are for **internal tracking only**
(Master State, To-Do lists, patent drafts).
They are NEVER published. They are NEVER Letters.

---

## TWO DOCUMENT TYPES

### TYPE A — BCT LETTER (published, Zenodo, outreach)
**Tool:** LaTeX → Overleaf → PDF download
**Font:** Computer Modern (LaTeX default — DO NOT change)
**Look:** Old-world serif. PRL style. Beautiful.
**Examples:** L73, L90, L28–L32 (the good ones)

### TYPE B — INTERNAL TRACKING DOCUMENT
**Tool:** Python/ReportLab
**Font:** Any (currently Helvetica — acceptable for internal)
**Look:** Clean, functional. Never published.
**Examples:** Master State, BCT_StyleGuide, To-Do lists

---

## TYPE A: LATEX LETTER SPEC

### Document class (ALL Letters)
```latex
\documentclass[aps,prl,twocolumn,superscriptaddress,floatfix]{revtex4-2}
```

### Required packages
```latex
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{bm}           % bold math
\usepackage{hyperref}     % clickable links
\usepackage{xcolor}       % colour definitions
\usepackage{booktabs}     % beautiful tables
\usepackage{siunitx}      % proper units: \SI{9.8}{\metre\per\second\squared}
```

### Colour definitions (paste in every Letter)
```latex
\definecolor{bctnavy}{RGB}{10,36,68}    % #0A2444
\definecolor{bctblue}{RGB}{13,71,161}   % #0D47A1
\definecolor{bctgreen}{RGB}{27,94,32}   % #1B5E20
\definecolor{bctteal}{RGB}{0,96,100}    % #006064
```

### Standard header (every Letter)
```latex
\title{BCT Letter NNN: [Title]\\
\large [Subtitle Line 1]\\
\large [Subtitle Line 2 if needed]}

\author{Michel Robert Cabri\'{e}}
\affiliation{Independent Researcher, Victoria, Australia}
\email{ZeroFreeParameters@gmail.com}
\date{\today}
```

### Abstract rule (CRITICAL — revtex4-2 quirk)
```latex
% abstract BEFORE \maketitle — not after!
\begin{abstract}
[Content.] Prediction~\#NNN: [prediction with equation].
Error: $N\%$. Zero free parameters. Dedicated to [person].
\end{abstract}
\maketitle
```

### Section headings
```latex
\section{Introduction}          % Roman numeral auto-added
\subsection{The Key Result}     % Letter auto-added
```

### Equations — ALWAYS LaTeX math mode
```latex
% CORRECT — old-world beautiful:
The void ratio $\mathcal{R} = r_\mathrm{tet}/r_\mathrm{oct} = 0.5426$

% CORRECT — display equation:
\begin{equation}
\frac{\rho_\mathrm{cusp}}{\rho_\mathrm{amb}} =
1 + \frac{r_\mathrm{tet}}{r_\mathrm{oct}} = \boxed{1.5426}
\label{eq:pred163}
\end{equation}

% WRONG — black boxes in PDF:
ρ_cusp/ρ_amb = 1 + r_tet/r_oct  ← Unicode = black boxes!!
j₁,₁  ←  BLACK BOX
H=1    ←  fine (plain ASCII)
```

### Prediction box (standard format)
```latex
\noindent\fbox{\parbox{\columnwidth-2\fboxsep}{%
\textbf{Prediction~\#NNN:} [Statement with math].
Observed: $[\mathrm{value}]$. Error: $N\%$.
\textbf{Zero free parameters.}}}
```

### Tables
```latex
\begin{table}[h]
\caption{[Caption]}
\label{tab:label}
\begin{ruledtabular}     % revtex4-2 beautiful ruled table
\begin{tabular}{lll}
Column A & Column B & Column C \\
\hline
data & data & data \\
\end{tabular}
\end{ruledtabular}
\end{table}
```
MAX table width = \columnwidth (auto in LaTeX — no overflow possible)

### Block quotes (dedication/epigraph)
```latex
\begin{quotation}
\noindent\textit{``The quote text.''}\\
\hfill --- Speaker, Date.
\end{quotation}
```

### Acknowledgements (standard footer — EVERY Letter)
```latex
\begin{acknowledgments}
Dedicated to [person]. Also: [specific people].
Zeta Vera (CSSC) for computational and editorial support;
and the Gang Gang Cockatoos (\textit{Callocephalon fimbriatum}),
[relevant note].

\noindent\textbf{Support the BCT programme:}
\url{https://www.patreon.com/cw/TheBCTSuperfluidLatticeModel}\\
\textbf{Open archive:}
\url{https://zenodo.org/search?q=cabri\'{e}}\\
\textbf{Substack:}
\url{https://substack.com/@thebctsuperfluidlattice}\\
\textbf{ORCID:} 0009-0007-9561-9859
\end{acknowledgments}
```

---

## FORBIDDEN IN ALL FORMAL BCT DOCUMENTS

| Item | Reason |
|------|--------|
| Unicode subscripts ₀₁₂₃ | BLACK BOXES in PDF |
| Unicode superscripts ⁰¹²³ | BLACK BOXES in PDF |
| Unicode math symbols ∈ ℝ ∇ (in body text) | RISKY — font dependent |
| Orange, gold, yellow, amber | BANNED colours |
| Purple, red, warm colours | BANNED colours |
| DejaVu / Helvetica body text | CORPORATE look |
| "BCT-SHE" | Private nickname only |
| "OH Condensate" | Private joke only |
| "physicist" or "scientist" for Michel | Michel is an artist |

---

## PERMITTED COLOURS (formal documents)

```
Navy    #0A2444    titles, headings, prediction boxes
Blue    #0D47A1    subheadings, equations  
Green   #1B5E20    biology/ecology content
Teal    #006064    appendices, secondary content
Greys   #222–#999  metadata, references
White   #FFFFFF    backgrounds
```

**Orange #FF6D00** — CSSC HTML interfaces ONLY. Never in PDFs.

---

## STANDARD EMAIL/OUTREACH SIGNATURE

```
Michel Robert Cabrié
Independent Researcher & Artist · Victoria, Australia
ORCID: 0009-0007-9561-9859
ZeroFreeParameters@gmail.com

Patreon: https://www.patreon.com/cw/TheBCTSuperfluidLatticeModel
Archive: https://zenodo.org/search?q=cabrié
Substack: https://substack.com/@thebctsuperfluidlattice
```

---

## WORKFLOW: NEW LETTER

1. **Write** .tex source (Claude generates, Michel reviews)
2. **Upload** to Overleaf (overleaf.com) → new project
3. **Compile** → Computer Modern PDF ← THE BEAUTIFUL ONE
4. **Download** PDF → upload to Zenodo
5. **Tag** in all 6 BCT Zenodo communities

---

## CMI MILLENNIUM PRIZE PATH

Per Naomi Kraker (CMI, 17 March 2026):
1. Publish in **qualifying outlet** (peer-reviewed journal)
   - Best targets: *Comm. Math. Phys.* (Springer), *Ann. PDE*
   - Zenodo does NOT count
2. Wait **2 years** after publication
3. Achieve **general acceptance** in global maths community
4. THEN CMI will consider

**Start clock now:** Submit L38 + Appendix JH4 to
*Communications in Mathematical Physics* immediately.
arXiv upload simultaneously (use endorsement code EFTSKF).

---

*"The vacuum crystallises into what it is."*
*Zero free parameters.*
