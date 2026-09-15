# GATE MIX — RESULT

**Do the four correction-free mixing-angle relations forward-derive, or are they fits?**
Cold Ledger gate. Run 15 September 2026. Verdict below.

---

## HANDOFF / DIGEST (§0.1)

The gate prompt reached this session **as an uploaded document, not as a file at a
commit-pinned `raw.githubusercontent.com` URL**. It was therefore *pasted*, not `curl`ed to
disk. **Per §0.1 I claim no authoritative digest** — provenance cannot be established by
SHA-256 for a pasted prompt, and I do not have the raw bytes on disk to hash. Everything
below is re-derived cold from the primary corpus; the four relations are treated exactly as
quoted in the prompt.

## CONTAMINATION STATEMENT (§0.2, §0.3)

- I did **not** read: any `gate-*` memory summary, the Cold Ledger (`audit-findings.md`),
  `audit/notes/`, or any `audit/gates/*/` deliverable — in particular **not** PRED2, PRED,
  MP, RANK, FWD or STAT.
- The PRED2 bit-figures (6.7 / 4.6 / 4.0 / 3.4) and the "correction-free" framing reached me
  **only through the gate prompt itself**. Per §0.3 I declare this and **re-derived the
  statistic from my own grammar** (Part 4). My numbers differ from PRED2's and are not
  inherited: I obtain naive per-form bits of 12.5 / 10.5 / 8.0 / 7.4 (tighter, because I used
  current measured central values), collapsing to 7.6 / 5.0 / 2.5 / (miss) after a fair
  look-elsewhere.
- Primary sources read (permitted, required): `4_BCT_Appendices_Volume1` Part 1 & Part 2
  (plain-text), `BCT_Letter88_ThreeDimensions`, `BCT_Letter90_CompleteWolfenstein`,
  `BCT_GeometryOfEverything_v4`. Canonical constants reconstructed from the gate's own
  definitions (no `MINIMAL_BCT.md` was mounted): r_oct=(√2−1)/2=0.207106781,
  r_tet=(√6−2)/4=0.112372436, α₀=r_oct·r_tet/π=0.007408056.
- **Gap I could not close:** the derivation of β=arccos(2·r_oct) is cited to *Letter 87*,
  which is **not present** in the accessible corpus. I audited its *statement* (Letters 88/90)
  but could not audit its *proof*.

---

## SEARCH-SPACE COVERAGE — where each formula lives (§1)

| # | Relation | Located in corpus | Companion / competing forms for the *same* angle |
|---|----------|-------------------|--------------------------------------------------|
| 1 | β = arccos(2·r_oct) = 65.53° | **Letter 88** (table, 65.5302°) and **Letter 90** (δ_CP=arccos(2r_oct), +0.132% vs 65.44°); "proven in Letter 87" | δ_CKM = **arccos(1/3)** = 70.53° (App BY); unitarity-triangle β = arcsin(sin2β/2)=22.91° (App EJ) — a *different* angle also called β |
| 2 | sin²θ₁₃ = 3·α₀ = 0.022224 | **App EQ / GM2** (Phase 31C): "the factor 3 is the number of T_d triplet representations" | θ₁₃ = **arcsin(r_tet)+arctan(α₀/r_oct)** = 8.5006° (App BZ); **sin θ₁₃ = α₀·r_tet/(r_oct+r_tet)** |
| 3 | sin²θ₁₂ = ⅓ − r_tet·r_oct = 0.310060 | **App EQ** (Phase 31C): "tribimaximal ⅓ corrected by −r_tet·r_oct" | **(1/π)(1−5α₀)** (App GH2); **π/4 − arcsin(r_oct)** = 33.05° (App BZ); sin θ₁₂ = r_oct; r_oct+α₀r_tet/r_oct (CKM leading forms) |
| 4 | sin²θ_W = r_tet²/(r_oct²+r_tet²) = 0.227439 | **App O / D4-E0** (Phase 19D): "tan θ_W = g′/g with g∝r_oct, g′∝r_tet"; exact form (5−2√6)/(11−4√2−2√6) | single tree form; NLO/running variants deferred (App EZ, HT3) |

**Immediate structural finding:** each of the four "survivors" is *one selected member* of a
family of competing geometric forms the corpus wrote for the same observable — θ₁₂ has ≥3,
θ₁₃ has 3, the CP phase has 2. Selection-of-best-form is already most of the fit story.

---

## VERDICT (first)

**No relation forward-derives at decisive strength. The collection lands on SC-MIX-1** — the
numeric layer contains nothing forward-derived; the surviving BCT content is geometry alone.
Per-relation refinements:

| # | Relation | Step-0 class | Forward? | Fair bits (after joint look-elsewhere) | Stop condition |
|---|----------|--------------|----------|----------------------------------------|----------------|
| 2 | sin²θ₁₃ = 3·α₀ | **asserted (with a stated principle for "3")** | partial | ~5.0 (suggestive) | **SC-MIX-2** — motivated form, but not decisive |
| 1 | β = arccos(2·r_oct) | **asserted** (proof in absent Letter 87) | not auditable | ~7.6 nominal, but form asserted | **SC-MIX-2 / SC-MIX-4** |
| 3 | sin²θ₁₂ = ⅓ − r_tet·r_oct | **asserted** (⅓ = external TBM ansatz) | no | ~2.5 (weak) | **SC-MIX-1** — correction-free fit |
| 4 | sin²θ_W | **motivated SM form, wrong value** | no | value is a **95σ miss** | **SC-MIX-2 → falsified as a measured-value prediction** |

**The decisive systemic result (CN-MIX-05):** the declared grammar over {r_oct, r_tet, α₀,
integers 1–6} hits **14 of the 15** angles the programme assigns a formula to, to within **1%**.
Agreement at the ~1% level is *generic* in this grammar. That caps the system-level information
of the four "correction-free survivors" at ≈ 0 bits and is why none reaches the ≥10-bit
decisive band (SC-MIX-3) after an honest joint look-elsewhere.

Per §0.5: **this does not refute the void geometry.** r_oct, r_tet and α₀ as packing constants
are untouched. What fails is the claim that any of these four is a *forward-derived* Standard
Model parameter.

---

## STEP-0 CLASSIFICATION — derived vs asserted (§1)

**#4 θ_W — MOTIVATED FORM, ASSERTED ASSIGNMENT.** App O states the genuine SM relation
tan θ_W = g′/g and posits g ∝ r_oct (SU(2)/oct void), g′ ∝ r_tet (U(1)/tet void), giving
sin²θ_W = r_tet²/(r_oct²+r_tet²). The *structural form* is real physics. But the corpus itself
records the value as **1.6355% below** the PDG M_Z value and defers the gap to a **BCT RG
running calculation it has not performed** ("beyond the current scope"; naive SM running
"overshoots"). So the corpus does not claim to derive the *measured* angle — it derives a tree
value and asserts that uncomputed running would close a 95σ gap.

**#2 θ₁₃ — ASSERTED, WITH A STATED PRINCIPLE FOR THE INTEGER.** App EQ gives a *reason* for
the "3": D4 triality has order 3 (App W: the D4 Dynkin diagram is the unique simple Lie algebra
with an order-3 outer automorphism), mapped to 3 generations. The same "3" is invoked for
η̄=3r_tet and the Cabibbo NLO 3α₀/8. This is the **only one of the four whose free integer is
tied to a stated geometric principle rather than chosen numerically.** It is still an
identification after the fact (see forward test), but it is the strongest case in the set.

**#1 β — ASSERTED (proof not in accessible corpus).** Letters 88/90 state δ_CP=arccos(2r_oct)
and cite "Letter 87" for the proof. Letter 87 is absent, so the derivation cannot be audited.
The corpus also carries a competing form (arccos(1/3)=70.53°) for the same CP phase.

**#3 θ₁₂ — ASSERTED (the anchor ⅓ is external).** The ⅓ is the tribimaximal-mixing value, a
pre-existing non-BCT ansatz; the corpus adds −r_tet·r_oct as "the T_d symmetry-breaking
correction." Only the correction is BCT, and it is one of ≥3 competing correction forms.

---

## STEP-1 — FORWARD-DERIVATION TEST, each free integer/structure interrogated (§2)

**#2 sin²θ₁₃ = 3·α₀. Why 3 and not 2 or 4?**
- The corpus answer — "3 = triality order / 3 families" — is a real principle, but three steps
  still require the target: (a) **why sin² and not sin or the angle itself?** 3α₀=0.02222 sits
  on sin²θ₁₃; had you written 3α₀ = sin θ₁₃ or = θ₁₃(rad) it would miss. The choice of which
  function of θ₁₃ equals 3α₀ is fixed by the data, not by triality. (b) **why α₀ (which already
  hides a /π)?** α₀ = r_oct·r_tet/π; the π is inherited from the fine-structure construction
  and has no stated reactor-angle meaning. (c) the corpus's *other* two θ₁₃ forms carry no "3"
  at all, so "3 families ⇒ 3α₀" is not forced even within BCT. **Verdict: motivated integer,
  but the surrounding form (sin², α₀) is selected against the measurement. Partial forward at
  best.**

**#1 β = arccos(2·r_oct). Why arccos, why the 2, why 2·r_oct = √2−1?**
- 2·r_oct = √2−1 is a natural octahedral quantity ("octahedral void diameter"), which is a
  genuine steelman. But arccos vs arcsin, and the factor 2, are the degrees of freedom, and
  their fixing is in Letter 87, **which is not available to audit**. Within the accessible
  sources the relation is asserted. A competing correction-free form (arccos(1/3)) exists for
  the same phase. **Verdict: not auditable as forward from the sources I have.**

**#3 sin²θ₁₂ = ⅓ − r_tet·r_oct. Why the product, why the sign, why ⅓?**
- ⅓ is external (TBM). The correction −r_tet·r_oct is chosen over r_tet² (→0.321, worse) and
  r_oct² (→0.290, worse): the product is picked **because it lands closest** — textbook fit.
  Decisive tell: the corpus applies the *same* correction with opposite sign to θ₂₃
  (½ + r_tet·r_oct = 0.523) and it is **6.2% off** vs the ~1% for θ₁₂. A genuine T_d correction
  would not be right to 1% in one angle and wrong by 6% in its sibling. **Verdict: fit.**

**#4 sin²θ_W = r_tet²/(r_oct²+r_tet²). Why r_tet² on top and not r_oct²?**
- r_oct²/(r_oct²+r_tet²) = 0.773 (the complement); r_tet²/(…) = 0.227. The numerator is chosen
  to land below ½, i.e. **the void↔coupling assignment (SU(2)↔oct, U(1)↔tet) is fixed by the
  requirement sin²θ_W < ½**, not by an independent geometric argument that the weak coupling
  must scale linearly with the octahedral radius. And the resulting number misses the measured
  value by 95σ. **Verdict: motivated SM skeleton, data-fixed assignment, wrong value.**

---

## STEP-2 — THE NULL MODEL (honest look-elsewhere) (§3)

Grammar: atoms {r_oct, r_tet, α₀, integers 1–6}; operators {+, −, ×, ÷, √, ², arccos, arcsin};
expressions enumerated to complexity ≤ 3 (covering all four relations' own complexity).
**Pool: 204,605 distinct values** (49,207 in (0,1.2) for sin²/ratios; 71,245 angle candidates).
Fully reproducible in `mix_nullmodel.py`.

**Per-relation density and bits** (grammar expressions within the *achieved* fractional error):

| # | Relation | achieved err | grammar hits | p | naive bits | −log₂(m) | **−log₂(m·N)** |
|---|----------|-------------|--------------|-----|-----------|----------|----------------|
| 1 | β | 0.05% | 12 / 71,245 | 1.7e-4 | 12.5 | 11.5 | **7.6** |
| 2 | θ₁₃ | 0.15% | 34 / 49,207 | 6.9e-4 | 10.5 | 8.9 | **5.0** |
| 3 | θ₁₂ | 1.00% | 194 / 49,207 | 3.9e-3 | 8.0 | 6.4 | **2.5** |
| 4 | θ_W | 1.64% | 295 / 49,207 | 6.0e-3 | 7.4 | 7.4 | **3.5** (but a 95σ miss) |

`m` = number of competing forms the corpus wrote for that angle (2, 3, 3, 1). N = 15 angles.
The `−log₂(m·N)` column is the fair per-relation significance after charging the search.

**Joint look-elsewhere (the decisive number).** Testing the grammar against **every** angle the
programme addresses:

| tolerance | angles hit (of 15) |
|-----------|--------------------|
| 1.0% | **14 / 15** |
| 1.5% | **14 / 15** |
| 2.0% | **14 / 15** |
| 3.0% | **14 / 15** |

The grammar reproduces almost the entire mixing sector to ~1% *by itself*. When a framework's
symbol grammar hits 14/15 targets at the survivors' own error level, a ~1% hit on any single
target is not evidence of derivation — it is the base rate. **6.7 / 4.6 / 4.0 / 3.4 do not
survive:** they are pre-look-elsewhere figures. After the joint charge the collection carries
≈ 0 bits and **no relation reaches the decisive ≥10-bit band.**

**Measurement-precision ceiling (CN-MIX-06).** Three of the four matches are *tighter than the
data can resolve*: θ₁₃ (data ±2.7%, match 0.15%), θ₁₂ (data ±4.2%, match 1.0%) and β (data
±5.3%, match 0.05%) are all **inside 1σ** — their sub-1% "precision" is not information the
measurement can confer. θ_W is the opposite pathology: data known to ±0.02%, so its 1.6% is a
**95σ miss.**

---

## STEP-3 — THE STEELMAN (§4, required)

The strongest case that these are derivations:

1. **Dimensionless mixing angles are exactly where a pure-geometry theory should speak** — no
   mass scale is needed, so if BCT geometry means anything, the angles are the fair test.
2. **α is not among the four; these are correction-free.** Unlike α (which needs post-hoc
   factors), these forms carry no fudge terms — a real difference in kind from the FWD/STAT
   failures.
3. **θ₁₃'s integer is principled.** D4 triality's order-3 automorphism is a genuine,
   non-negotiable mathematical fact, and it is invoked consistently (θ₁₃, η̄=3r_tet, 3α₀/8,
   3 generations, 3 spatial dimensions) rather than only where convenient. If any relation in
   the programme has a real forward integer, it is this "3". **This gate certifies that the "3"
   in 3α₀ has a stated geometric principle** — that part is not a bare fit.
4. **θ_W's skeleton is real physics.** tan θ_W = g′/g *is* the SM definition; identifying the
   two couplings with the two void radii is a legitimate hypothesis, and the direction of the
   1.6% offset (BCT below PDG) is the direction RG running would move a Planck-scale boundary
   condition. A defender can fairly say θ_W is an *un-run* prediction, not a wrong one.

Why the steelman does not carry the day: (2) is true but the null model shows correction-free
hits are cheap here, so "no fudge factor" buys little; (3) the principled "3" still sits inside
a form (sin², α₀ with its /π) fixed against the data, and two rival θ₁₃ forms lack the 3; (4)
the running is *uncomputed* and naive running overshoots, so the tree agreement is not itself
evidence. The steelman elevates θ₁₃ and θ_W above bare fits, but not to forward-derivation.

---

## CN-MIX NOTICES (tiered)

- **CN-MIX-01 [ASSERTED]** β = arccos(2·r_oct) = 65.53° is stated in Letters 88/90 as the CP
  phase, matched to δ_CP ≈ 65.44° (+0.13%); its proof is cited to *Letter 87*, absent from the
  accessible corpus. A competing form arccos(1/3) exists for the same phase. Not auditable as a
  derivation; matched to a phase measured only to ~5%.
- **CN-MIX-02 [CONJECTURE]** sin²θ₁₃ = 3·α₀ is a motivated form: the integer 3 is tied to a
  stated geometric principle (D4 triality order / 3 families), but the sin²-vs-sin choice, the
  /π inside α₀, and the existence of two rival θ₁₃ forms leave it short of forward at decisive
  strength. Fair significance ~5 bits (suggestive).
- **CN-MIX-03 [ASSERTED / FIT]** sin²θ₁₂ = ⅓ − r_tet·r_oct: ⅓ is the external tribimaximal
  ansatz; −r_tet·r_oct is selected over r_tet² and r_oct² because it lands closest, and the
  identical correction fails at 6% for θ₂₃. Correction-free fit. ~2.5 bits.
- **CN-MIX-04 [FALSIFIED as a measured-value prediction]** sin²θ_W = r_tet²/(r_oct²+r_tet²) =
  0.227439 is a **95σ miss** vs the PDG M_Z value 0.23122 (±0.00004); the void↔coupling
  assignment direction is fixed by the data; the gap is deferred to an uncomputed BCT running.
  Motivated SM skeleton, not a forward derivation of the measured angle.
- **CN-MIX-05 [PROVEN]** The declared grammar over {r_oct, r_tet, α₀, 1–6} hits 14/15 of the
  angles the programme assigns formulas to within 1%. ~1% agreement is generic; the four
  survivors carry ≈0 system-level bits after joint look-elsewhere; none reaches ≥10 bits.
- **CN-MIX-06 [PROVEN]** Measurement-precision ceiling: θ₁₃, θ₁₂ and β match *inside 1σ* of
  data known to only 2.7 / 4.2 / 5.3% — their sub-1% precision is not measurable information;
  θ_W is 95σ off.
- **CN-MIX-07 [PROVEN]** Formula multiplicity: the corpus writes ≥3 forms for θ₁₂, 3 for θ₁₃,
  2 for the CP phase. The four survivors are best-of-family selections — a selection effect that
  must be, and here is, charged in the look-elsewhere.

---

## §0.5 — WHAT SETTLING THIS BUYS (reproduced verbatim)

> This gate decides whether the four best numeric survivors are forward-derivations or
> correction-free fits. A verdict that one or more **forward-derives at decisive strength** would be
> the strongest result in the programme — the first BCT Standard-Model parameter that is derived
> rather than matched — and it would demand independent replication and scrutiny, not celebration.
> A verdict that **all four are correction-free fits** does not refute the void geometry (r_oct,
> r_tet, α₀ as packing constants stand) — it means the numeric/parameter layer contains nothing
> forward-derived, and BCT's surviving content is geometry alone (the packing, the percolating
> network, ξ, the emergent acoustic metric). Neither outcome vindicates or refutes BCT as a whole.

---

## WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** refute the void geometry. r_oct, r_tet, α₀ as packing constants are untouched;
  this gate concerns only whether the four *angle relations* forward-derive.
- It did **not** audit the actual proof of β = arccos(2·r_oct): Letter 87 was not available.
  If Letter 87 contains a genuine blind derivation of arccos and the factor 2, CN-MIX-01 should
  be revisited — this gate could not see it.
- It did **not** compute BCT RG running for θ_W. If a first-principles BCT running calculation
  lands 0.2274 → 0.23122, CN-MIX-04 changes materially; as of the accessible corpus it is
  uncomputed.
- It did **not** score non-angle predictions (masses, α, ρ_CC, etc.); scope was the four
  quoted relations only (§0.4).
- The joint look-elsewhere used N = 15 angle targets compiled from the corpus; a different
  defensible census would shift the fair bits by ≤ log₂ of the ratio, not the qualitative
  verdict (14/15 hit rate is robust across tolerances 1–3%).

---

*Scripts: `mix_nullmodel.py` (deterministic; `python3 mix_nullmodel.py`). As-run prompt:
`gate_MIX_prompt_asrun.md`. audit/NEXT.md intentionally not modified (§6).*
