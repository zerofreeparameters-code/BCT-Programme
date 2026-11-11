# Gate BULK — RESULT

**Card:** `audit/gates/gate_BULK_prompt.md`, SHA-256 `2ffb5f092f4ed140dfc92eb035d73fd20ec30bfeddf6fc212681d39aaf2c02ec` (19849 B), fetched by raw URL at pre-registration commit **C = cec526f16281e4a66750af459d741dcfd92a6ff6** and hashed before being read in this thread (see Protocol).
**Validation script:** `bulk_dimcheck.py`, SHA-256 `41fbc4ef284dee15a23610e9b5e2fd27e6ecf000381f27b354717cf3377b4674` (1755 B), fetched and hashed the same way; re-run, all §7 numbers reproduce.
**Sources:** pinned at `9582c54b6f22fc78eee0dc356f6d49cdfadd68b3`; all six §4.1 SHA-256 verified before any source was read (`sources_9582c54.sha256`); `audit/gates/BUBBLE_BELLS/` present, its own `SHA256SUMS` verified.
**Run:** 11 November 2026, 10:43–11:05 AEDT, Claude Fable 5.1, fresh thread (session `01CaE3p9NntTwEURvi1JDv8G`), one instance, not blind to the card's §9 forecast (the card carries it). **Tier cap: CONJECTURE** (same-session rule).
**Type:** provenance audit with a measurement attached. Not a derivation of G.

---

## Verdict — **SC-BULK-1 (inherits MP / RATIO), all four variants**

Every K_BCT (or ρ₀) that the pinned corpus prints as the quantity in G = c⁴/(8πK) either acquires its SI value through a G-bearing input declared in the corpus's own text (ρ₀ = ρ_Planck, m = m_P, a = ℓ_P) or is dimensionally inconsistent as written — and in fact each printed identification is both. Q2 is NO for (i), (ii), (iii) and (iv). Q3 was not opened. G = c⁴/(8πK) is an identity in G throughout the pinned corpus; App AL's own key result 1 stands; the "Exact / Zero Param" status of new_approach-6/7 is withdrawn. The stiffness-in-the-voids hypothesis yields no G without G.

| Q | result | one line |
|---|---|---|
| Q1 provenance | 3 variants + 1 summary statement located; ledgers below | every chain terminates in ħ, c **and** G (via ρ_P, m_P or ℓ_P); none of the printed identifications is dimensionally consistent as written |
| Q2 G-free scale | **NO** × 4 | (i) needs m and n₀; (ii) needs m, ξ and the site volume; (iii) ABSENT and a pure number; (iv) multiplies (i) by φ and α_∞ |
| Q3 G from K | not evaluated | no variant opened it |
| Q4 measurement | table below, no verdict | κ(a) = 1, a†/ℓ_P = 1/√(8π); κ(ii) = 4√2πα₀; f_K = φ/α_∞ under the §3 rule |

---

## Q1 — Input ledgers

Conventions: line numbers are in the pinned `.tex` files; "p. N L m" is page N (form-feed page = printed folio) and line m of `pdftotext -layout` on the pinned PDF (`bulk_ledger_cites.py` prints every cited line after re-hashing the files). A terminal input is ħ, c, a CODATA constant, or a corpus-declared assumption quoted verbatim. G-bearing per §4.2: any chain through G, m_P, ℓ_P, t_P, E_P, ρ_P, c⁴/G, or anything the corpus defines "= Planck …" / "at the Planck scale".

### Variant (a) — App AZ6 and Letter 20: K_BCT = ρ₀c², ρ₀ = ρ_Planck (or m_P n₀)

| Symbol | Value | SI dimension | Source | Terminal inputs | G-bearing | Notes |
|---|---|---|---|---|---|---|
| G = c⁴/(8πK_BCT), "K_BCT = ρ₀c² is the BCT condensate bulk modulus" | — | [K] = Pa = kg m⁻¹ s⁻² | AZ6 L91–92; Letter 20 L96–97, L311–313 | — | — | the claim under test |
| G = c²/(8πρ₀) | — | [c²/ρ₀] = m⁵ kg⁻¹ s⁻² | AZ6 L261, L277, L310, L373, L393 | — | — | same identification with K = ρ₀c² substituted |
| P = c²ρ²/(2ρ₀) (γ = 2 polytrope) → K = ρ∂P/∂ρ at ρ₀ = ρ₀c² | — | Pa | Letter 20 L137–141 | ρ₀, c | Y (via ρ₀) | c_s² = ∂P/∂ρ = c² at ρ₀ ✓ |
| ρ₀ = ρ_Planck = c⁵/(ħG²) | 5.1548 × 10⁹⁶ kg m⁻³ (CODATA 2022) | kg m⁻³ | Letter 20 L141; L230 "ρ₀ = ρ_Planck = c⁵/(ħG²)"; L314–316 "Planck density, the unique condensate density consistent with c_s = c" | ħ, c, **G** | **Y** | declared, not derived; "consistent with c_s = c" fixes no scale (c_s = c is a ratio condition) |
| ρ₀ = m_P n₀ ("the exact BCT condensate density") | √2 ρ_P with n₀ = 1/site; ρ_P with n₀ = 1/ℓ_P³ | kg m⁻³ | AZ6 L373–374 | m_P, n₀ | **Y** | AZ6 does not say which n₀; AZ7 L162–163 says 1 per site |
| m = m_P = √(ħc/G), "the GP condensate quantum mass. Not a free parameter—set by dimensional analysis from G, ħ, c" | 2.1764 × 10⁻⁸ kg | kg | Letter 20 L230–231, L317–319 | ħ, c, **G** | **Y** | the corpus's own words: set from G |
| n₀ = 1 per site "in BCT lattice units" | √2/a³ (site volume a³/√2 at c/a = √2) | m⁻³ | AZ7 L162–163 | a | Y (via a) | |
| a = nearest-neighbour distance "= 2R = 1 l_P", "in Planck units" | ℓ_P | m | App K p. 120 L40–41, L45 | ℓ_P | **Y** | declared assumption (Gate MP, SC-MP-3) |
| g = mc²/n₀ "(Josephson condition, App D)" | — | J m³ | AZ6 L353–354 | m, c, n₀ | Y | App D in the pinned volume has no Josephson condition of this form (it has g = α₀, App J/K); flagged, not followed |
| ξ = ħ/√(2mgn₀) "= 2.32 ℓ_P (App E.3)" | 2.31754 a | m | AZ6 L168–169 | m, g, n₀ / ℓ_P | Y | with g = mc²/n₀ and m = m_P this formula gives ξ = ℓ_P/√2, not 2.32 ℓ_P (CN-BULK-04) |
| 8π | 8π | 1 | AZ6 L91, L261; Letter 20 L96, L322–324 | — | N | coefficient; E.3's intermediate 4π and AI/AL's 16π recorded in (b), (c) |
| c, ħ | CODATA (exact) | — | — | — | N | |
| Summary statement | — | — | Vol. 1 Foundations L209–215 (Letter 9): "reproduces G to the accuracy of the input Planck mass" | m_P | Y | the corpus states the inheritance itself |
| Letter 20 L441–443: m_P "is itself a BCT prediction: m_P = M_R/α₀² to −0.08% (Letter 9)" | — | — | Letter 20 L441–443 | M_R (a mass) | hierarchy route | passes through a measured mass; out of scope by §3; flagged, not followed |

**Dimensional consistency as written:** [c⁴/(8πK)] = m⁵ kg⁻¹ s⁻² with K a pressure; [c²/(8πρ₀)] = m⁵ kg⁻¹ s⁻² with ρ₀ a mass density; [G] = m³ kg⁻¹ s⁻². **Inconsistent.** With ρ₀ = ρ_P: c⁴/(8πρ_P c²) = 6.9372 × 10⁻⁸² m⁵ kg⁻¹ s⁻² = G·ℓ_P²/(8π) exactly (ratio 1.0 to 40 digits); the length² that closes the identity is ℓ_P²/(8π), L/ℓ_P = 1/√(8π) = 0.19947. (c²/G = m_P/ℓ_P exactly, so "ρ₀" would have to be a line density m_P/(8πℓ_P) for G = c²/(8πρ₀) to hold as written.)

### Variant (b) — App E.3 §3.2 (printed p. 72, text-extract line 3539; the card's "p. 71" is CN-BULK-01): K_BCT = 8 M_FCC α₀/(9√2)

| Symbol | Value | SI dimension | Source | Terminal inputs | G-bearing | Notes |
|---|---|---|---|---|---|---|
| S_BCT⁽²⁾ = (ρ₀c²/8)∫[h² − h_μν h^μν]; S_EH⁽²⁾ = (c⁴/32πG)∫[…]; "ρ₀c²/8 = c⁴/(32πG)", G = c²/(4πρ₀) | — | [c²/ρ₀] = m⁵ kg⁻¹ s⁻² | p. 72 L9–20 | ρ₀ | — | 4π coefficient (vs 8π) recorded; matching step itself closed elsewhere (Gates T/IG-BZ/QP/AM/J), not reopened |
| "BCT equation of state ρ₀ = 2K_BCT/c²" → G = c⁴/(8πK_BCT) | K = ρ₀c²/2 | Pa if ρ₀ is a density | p. 72 L22–26 | ρ₀ | — | factor 2 vs AZ6's K = ρ₀c² (CN-BULK-03) |
| K_BCT = 8 M_FCC α₀/(9√2) "derived from the Madelung energy (Appendix D)" | 0.0046563 × M_FCC | **pure number as printed** | p. 72 L29–31 | α₀, M_FCC | see below | [c⁴/(8πK)] = m⁴ s⁻⁴ for a pure number: **inconsistent as written** |
| α₀ = r_oct r_tet/π | 0.00740806 | 1 | AZ7 L108–109; Letter 27 L61 | r_oct = (√2−1)/2, r_tet = (√6−2)/4 | N | permitted input |
| M_FCC "the FCC Madelung constant" | **undefined in the pinned sources** | — | p. 72 L31 only | — | — | no definition, value or computation anywhere in the pinned PDF or .tex files |
| App D (the cited derivation) | **ABSENT** (as-of-date, commit 9582c54) | — | D0 pp. 14–20, D1 pp. 21–26, D2 pp. 27–31, D3 pp. 32–40, D4/E0 pp. 41–51 searched for "bulk modulus", "modulus", "stiffness", "M_FCC", "9√2": no hit | — | — | D0 p. 20 L9–11: "The Madelung constant argument cites established results. A BCT-specific Madelung computation … would strengthen Step 2" — i.e. no Madelung energy is computed; not reconstructed (§4.1) |
| E.3's own caveat | — | — | p. 72 L31–34: "cannot be numerically verified without first deriving the electron mass (the hierarchy between G and α involves the mass ratio m_e/m_P)" | m_e, m_P | hierarchy route | out of scope by §3 |
| App E roadmap on this K | — | — | p. 49 L45–46: "K_BCT was computed in Appendix D (though it required l_P as an external input)" | **ℓ_P** | **Y** | the corpus's own statement of the unit that was supplied |
| Elsewhere | — | — | p. 75 L51 "G = c⁴/(8πK_BCT) — BCT Madelung bulk modulus — D + E.3"; p. 69 L18–19, L36 | — | — | all cite App D |

**Dimensional consistency as written:** a pure number in c⁴/(8πK) gives m⁴ s⁻⁴, not G. **Inconsistent.** To become a pressure the number needs ħc/a⁴ (or equivalent); the only unit-bearing scale in the pinned corpus is a = ℓ_P, and p. 49 says that is what was used. Variant (iii) of Q2 is therefore **ABSENT** for its derivation and **G-bearing by the corpus's own declaration** for its unit.

### Variant (c) — App AI.4 and App AL (pp. 265, 273–274): G = c⁴/(16πρ_BCT), ρ_BCT = ρ_Planck or (π²/16)ρ_Planck

| Symbol | Value | SI dimension | Source | Terminal inputs | G-bearing | Notes |
|---|---|---|---|---|---|---|
| G_eff = c⁴/(16πρ₀); G_eff = c⁴/(16πρ_BCT) | — | [c⁴/ρ] = m⁷ kg⁻¹ s⁻⁴ | p. 265 L7, L22–24 (text line 12802); p. 273 L19–20 | ρ_BCT | — | 16π coefficient recorded, not used (§5) |
| ρ_BCT = ρ_Planck = c⁵/(ħG²) "= 5.1560e+96 kg/m³" | CODATA 2022: 5.1548 × 10⁹⁶ (CN-BULK-06) | kg m⁻³ | p. 265 L25–27; p. 267 "ρ_BCT = Planck density" | ħ, c, **G** | **Y** | "the BCT condensate density at the Planck scale" |
| ρ_BCT = ρ_D4 × ρ_Planck, ρ_D4 = π²/16 | 0.61685 ρ_P | kg m⁻³ | p. 274 L22–24 (text line 13190) | ħ, c, **G**; π²/16 | **Y** | π²/16 is the D4 4-sphere packing density (p. 261), not the FCC packing π/(3√2) = 0.74048 at c/a = √2; recorded, not reconciled (§7) |
| AI.4's own statement | — | — | p. 265 L29–34: "G_eff ~ G (up to a numerical coefficient of order 1 …). The numerical coefficient requires computing the BCT equation of state, but the dimensional structure is correct." | — | — | the "dimensional structure" claim is false as written (m⁷ kg⁻¹ s⁻⁴) |
| App AL key result 1 | — | — | p. 274 L29–31: "G CANNOT be derived numerically from BCT first principles alone. The structural formula G = c⁴/(16πρ_BCT) is dimensionally self-referential." | — | — | stands |
| AL.1 arithmetic | "G = ħG²/(16πc) ⇒ 1 = ħG/(16πc) [dimensionally inconsistent!]" | — | p. 273 L23–25 | — | — | AL calls the formula "dimensionally correct" one line later (L25); it is not (CN-BULK-02) |
| AL.3 arithmetic | "G = c⁴/(16πρ_BCT) = c⁴ħ/(c⁵π³) = ħ/(cπ³) … has dimensions of time" | — | p. 274 L25–26 | — | — | the step dropped G² and ħ/c is kg·m; the quantity is ħG²/(π³c) = 5.0538 × 10⁻⁶⁵ m⁷ kg⁻¹ s⁻⁴ (CN-BULK-02) |
| AL.2 / AZ6 §4.2, Prediction #100 (G from the hierarchy residual) | 6.684 × 10⁻¹¹ (AZ6); printed as "0.000000×10⁻¹¹" in AL | — | AZ6 L401–454; p. 273 L10–13, p. 274 L1–17, L31–33 | m_e, α₀, G_CODATA | hierarchy route | out of scope by §3 (Gates PRED/STAT); the AL figures are typeset as zeros in the pinned PDF (CN-BULK-07) |

**Dimensional consistency as written:** m⁷ kg⁻¹ s⁻⁴ ≠ m³ kg⁻¹ s⁻². **Inconsistent.** c⁴/(16πρ_P) = 3.1174 × 10⁻⁶⁵ m⁷ kg⁻¹ s⁻⁴ = ħG²/(16πc) (ratio 1.0 to 40 digits). The card's §7 restatement of App AL's unit is corrected in CN-BULK-02; its number is right.

### Further K / ρ identifications located in the run (not additional variants)

- **Letter 9 summary** (Vol. 1 Foundations L209–215): G = c⁴/(8πK_BCT), "reproduces G to the accuracy of the input Planck mass." A summary of (a)/(b); no new K.
- **Jacobson–Parentani proof sketch**, AZ6 L316–319: "With P = ρc²/3 (ultra-relativistic equation of state at c_s = c), ε + P = c²ρ and the sound speed is identically c." This is a different EOS (K = ρ₀c²/3, and dP/dρ = c²/3, not c²) from the quartic/polytrope used everywhere else; it appears inside the theorem's proof sketch, not as the BCT K, and the matching route is closed — recorded, not followed.
- **Symbol collisions** (for the record): K_BCT = 0.970375 is the Koide quantity (p. 269 L42, text-extract line 12997 — the card's location is correct); ρ_BCT on p. 108 is a density of states; ρ_BCT ~ α₀ m_P⁴ on pp. 153–156 is a vacuum energy density. None is the K of this gate.
- **Not in the pinned sources, by title only** (Complete Index, pp. 3–10): App FP "BCT Gravity: Planck Scale and Newton's Constant" (p. 634, Part 2) and App JB6 "Newton's Constant from BCT: The Planck-QCD Identity" (Vol. 2 index). Neither is pinned; neither was opened. A card for another day if either claims a G-free scale (§4.6 sentence).

---

## Q2 — G-free scale, per variant

Permitted inputs: ħ, c; c/a = √2, π/(3√2), r_oct, r_tet, α₀, ξ/a = 2.31754, α_∞ = 1.64 ± 0.03, Madelung constants with quoted definitions; the EOS forms as printed. Forbidden: G, m_P, ℓ_P, t_P, E_P, ρ_P, c⁴/G, anything "= Planck …".

**(i) GP quartic, V = (g/2)(|Ψ|² − n₀)², Josephson g = mc²/n₀ (AZ6 L139, L353–354).** P = gn²/2 (+ const), K = g n₀² = m n₀ c² = ρ₀c². The EOS fixes the *ratio* c_s = c and nothing else: K in SI needs m and n₀. m is m_P (Letter 20 L230) or 0.238 m_P (BUBBLE_BELLS N9, obtained from ξ = 2.31754 a with a = ℓ_P) — both G-bearing (§4.4); n₀ = 1 per site needs the site volume a³/√2 with a = ℓ_P (App K p. 120 L40–41) — G-bearing. **NO.** Side-finding (sentence only): AZ6's own ξ = ħ/√(2mgn₀) with g = mc²/n₀ reads ξ = ħ/(√2 mc) = ƛ_C/√2, which is ℓ_P/√2 for m = m_P and 2.32 ℓ_P only for m = 0.305 m_P (CN-BULK-04).

**(ii) Bose–Hubbard, U = μ = t_kin = ħ²/(2mξ²), n₀ = 1 per site (AZ7 L154–170; Letter 27 L75–80).** With U = g in lattice units (AZ7 L159–160), the continuum coupling is g = U·v_site and K = g n₀² = U/v_site = ħ²/(2mξ²v_site). ξ = 2.31754 a and v_site = a³/√2 are G-free *ratios*; the SI value needs m (G-bearing, §4.4) and a (= ℓ_P, G-bearing). The alternative reading U = t = α₀ "in Planck units" (App K p. 121 L2, L11) makes U = α₀E_P, G-bearing through E_P. **NO.** Side-finding (sentence only): with a = ℓ_P and m = m_P, U = ħ²/(2m_Pξ²) = 4πα₀E_P while t = α₀E_P, so t/U = 1/(4π), not 1 (CN-BULK-05); it does not touch the verdict.

**(iii) Madelung bulk modulus K_BCT = 8 M_FCC α₀/(9√2) (E.3 p. 72 L29).** **ABSENT**: App D at the pinned commit contains no bulk-modulus computation and no definition of M_FCC (D0 explicitly defers the Madelung computation to the literature). As printed it is a pure number of magnitude 0.0046563 × M_FCC and needs a unit; E.3 defers evaluation to m_e/m_P (hierarchy, out of scope) and the App E roadmap states the unit used was ℓ_P (p. 49 L45–46). Not reconstructed (§4.1, §4.6). **NO** (dimensionally inconsistent as printed; unit G-bearing by declaration).

**(iv) Void-localised (Bubble Bells): g = α_∞mc²/n₀, condensate on the void network, φ = 1 − π/(3√2), c_eff = c_s/√α_∞ (AZ6 L362; `audit/gates/BUBBLE_BELLS/`).** Under the §3 rule, K_eff = ρ_eff c_eff² = φρ₀c_s²/α_∞; with g = α_∞mc²/n₀, c_s² = α_∞c², c_eff = c and K_eff = φ m n₀ c². φ and α_∞ are dimensionless and cannot supply a scale; m and n₀ are those of (i). The BUBBLE_BELLS mass m/m_P = 1/(√(2α_∞) ξ/a) = 0.238 is itself obtained with a = ℓ_P (`bb_q4_numbers.py` docstring line 4 "Inputs: a = ℓ_P", line 9 `a = mp.mpf(1)`). **NO.** Inherits CONJECTURE from Gate BUBBLE_BELLS in addition.

No variant is G-free. Q3 is not opened.

---

## Q3 — not evaluated

No variant fixed K in SI without a forbidden input. G_BULK ≡ c⁴/(8πK) with K a pressure returns DIMENSIONALLY INCONSISTENT for (a), (i), (ii), (iv) and (c) [as m⁵ kg⁻¹ s⁻²], and for (iii) [as m⁴ s⁻⁴]; the a²-completion is reported in Q4 instead, with no verdict.

---

## Q4 — Measurement table (no verdict)

`bulk_q4.py` (mpmath, 60 digits working, 40 reported; full output in `output/q4_table.txt`). a = ℓ_P by the corpus's declaration; m = m_P unless stated; n₀ = 1 per site = √2/a³; touching spheres at c/a = √2. κ ≡ K a⁴/(ħc); a†/ℓ_P solves c⁴/(8πK a†²) = G_CODATA (the 8π rule of §5; 16π values recorded in notes only). Every row traces to the ledger lines named.

| Variant (ledger lines) | K [Pa] | κ = K a⁴/(ħc) | a†/ℓ_P |
|---|---|---|---|
| (a-L20) K = ρ₀c², ρ₀ = ρ_P (AZ6 L91–92; L20 L138–141) | 4.632946787895116622627852811132214908986e+113 | 1.0 | 0.1994711402007163389699730299671909342379 |
| (a-AZ6) ρ₀ = m_P n₀, n₀ = 1/site (AZ6 L373–374; AZ7 L162–163) | 6.551976181194140869217301079446994260655e+113 | 1.41421356237309504880168872420969807857 | 0.1677345667413534790556974219940278948585 |
| (i-mP) K = g n₀², g = mc²/n₀, m = m_P (AZ6 L139, L353–354) | 6.551976181194140869217301079446994260655e+113 | 1.41421356237309504880168872420969807857 | 0.1677345667413534790556974219940278948585 |
| (i-BB) same, m = 0.238 m_P (BB N9) | 1.561016301145870557313678943776032011777e+113 | 0.3369381028127642210903902619511333188011 | 0.343641026037283594669420362816730853968 |
| (ii-mP) K = U/v_site, U = ħ²/(2mξ²), ξ = 2.31754 a, m = m_P (AZ7 L154–170; L27 L75–80) | 6.099390158158952100389826136809045611676e+112 | 0.1316524975873958534715264574097171035928 | 0.5497503555139371775800487906901944041225 |
| (ii-BB) same, m = 0.238 m_P | 2.560066733879227713994433467792692499314e+113 | 0.5525784886129333225882400295998586428338 | 0.2683385588775150265138964806697237452032 |
| (ii-t) U = t = α₀E_P (App K p. 121 L2, L11) | 4.853740467585272565233575010902806181474e+111 | 0.01047657288071393752415152349340004068513 | 1.948814269334708873981253556772097978863 |
| (c-AI4) K := ρ_BCT c², ρ_BCT = ρ_P (p. 265 L24–27); printed 16π recorded in q4_table.txt | 4.632946787895116622627852811132214908986e+113 | 1.0 | 0.1994711402007163389699730299671909342379 |
| (c-AL3) ρ_BCT = (π²/16)ρ_P (p. 274 L24); 16π value in q4_table.txt | 2.857834500488903141949756964855073817488e+113 | 0.6168502750680849136771556874922594459571 | 0.2539745437369638791430532197385440806202 |
| (iv-L20) K_eff = φρ₀c², ρ₀ = ρ_P (AZ6 L362; BB N1–N3) | 1.202340081672646460691735742932576983515e+113 | 0.2595195103069389588306865016565510502309 | 0.3915570642162611773241264019865266249165 |
| (iv-AZ6) ρ₀ = m_P n₀, n₀ = 1/site | 1.700365650086231400589435026656537413598e+113 | 0.3670160111764973026474742631165304505039 | 0.3292589316667225303337749423069624458665 |
| (iv-BB) m = 0.238 m_P, n₀ = 1/site | 4.051141860545254837489157608785256673884e+112 | 0.08744201144571762287064639951182620787665 | 0.6745590924282455110083239096527124517778 |

**f_K ≡ K_void/K_bulk, variant (iv):**

| reading | f_K |
|---|---|
| §3 rule as written — K_eff = ρ_eff c_eff² with the same microscopic g in void and bulk (K_bulk = ρ₀c_s²) | **φ/α_∞ = 0.1582436038456944870918820132052140550188 ± 0.002894700070348069885827109997656354664979** |
| both moduli with their own sound speed set to c (K_bulk = ρ₀c², K_void = φρ₀c²; the §9 reading) | φ = 0.2595195103069389588306865016565510502309 |
| per unit fluid volume, K = ρ₀c_s²/α_∞ (listed, no verdict) | 1/α_∞ = 0.6097560975609756097560975609756097560976 |
| Biot/JKD equivalent fluid, K_eff = K_f/φ with ρ_eff = α_∞ρ₀/φ (listed, no verdict) | 1/φ = 3.853274841715290815690235798377522997142 |

**Reference column (no verdict):** 1/(8π) = 0.03978873577297383394222094084312859050861; 1/√(8π) = 0.1994711402007163389699730299671909342379; φ = 0.2595195103069389588306865016565510502309; α_∞ = 1.64 ± 0.03; 1/α_∞ = 0.6097560975609756097560975609756097560976; 1/√(8πφ) = 0.3915570642162611773241264019865266249165; π²/16 = 0.6168502750680849136771556874922594459571; 4√2πα₀ = 0.1316524975873958534715264574097171035928. Coincidences noted per §8 and not pursued: κ(a-L20) = 1 and a†/ℓ_P = 1/√(8π) are identities of the Planck units (ρ_P c² ℓ_P⁴ = ħc), not findings; κ(ii-mP) = 4√2πα₀ follows from ξ/a = 1/√(8πα₀) and n₀ℓ_P³ = √2, i.e. from inputs already in the ledger.

---

## §9 disclosure, scored

| §9 item | forecast | outcome |
|---|---|---|
| SC-BULK-1 for all four variants, ~90% | — | **correct** (SC-BULK-1 × 4) |
| (a), (c) set ρ₀ = ρ_Planck and m = m_P in their own text | — | **confirmed** (Letter 20 L141, L230, L314–319; AI.4 p. 265 L25–27) |
| (ii) needs a (via n₀ = 1/site) and m (via U = ħ²/(2mξ²)); corpus has no G-free value for either | — | **confirmed**; also U = t = α₀ "in Planck units" is G-bearing via E_P |
| (iii) pure number needing a unit; only unit-bearing scale is a = ℓ_P by declaration; E.3 defers to m_e/m_P | — | **confirmed**, and stronger: p. 49 L45–46 says ℓ_P was the external input |
| (iv) multiplies (a) by dimensionless φ, α_∞ | — | **confirmed**; the BB mass 0.238 m_P is itself built with a = ℓ_P |
| Residual 10%: App D supplies a Madelung energy with an absolute unit (e, ε₀) | — | **did not materialise**: App D is ABSENT at 9582c54; D0 cites the literature and computes no Madelung energy |
| Q4 guess (a): κ = 1 at a = ℓ_P, a†/ℓ_P = 1/√(8π) ≈ 0.1995 | 1; 0.1995 | **correct** for ρ₀ = ρ_P (Letter 20); the AZ6 sub-variant with n₀ = 1/site gives √2 and 0.1677 |
| Q4 guess (iv): f_K = φ ≈ 0.2595, a†/ℓ_P = 1/√(8πφ) ≈ 0.3916 | 0.2595; 0.3916 | **a† correct** (0.39156 for ρ₀ = ρ_P with c_eff = c). **f_K depends on the K_bulk reference**: the §3 rule as written (K_eff = ρ_eff c_eff², K_bulk = ρ₀c_s²) gives φ/α_∞ = 0.158; φ results only if K_bulk is also re-tuned to c. Both reported; scored as *half right* |
| Q4 guess (iii): no guess for κ; "of order α₀ × a Madelung constant of order 1" | — | the printed coefficient is 8α₀/(9√2) = 0.629 α₀ × M_FCC; consistent with the order-of-magnitude statement; M_FCC undefined so no number |
| Value of running: (i) decide the void-localised variant; (ii) the Q4 table replaces "f = 1/(8π)"; (iii) a ledger entry settling new_approach-6/7 by a fresh-thread run | — | (i) decided: G-bearing; (ii) delivered: the corpus's own EOS gives κ = 1 and a†/ℓ_P = 1/√(8π) for (a), φ-scaled values for (iv), and 4√2πα₀ for (ii); (iii) delivered: SC-BULK-1, "Exact / Zero Param" withdrawn |
| Analyst's interest in the gated line being a real question | — | it was a real question with a known answer, as forecast; the only new content is in the Q4 table and the CNs |

---

## Correction notices

- **CN-BULK-01 (card §1(b), location).** App E.3 §3.2 is on printed p. 72 of the pinned Appendices Vol. 1 Part 1 (text-extract line 3539), not p. 71. The AI.4/AL locations (pp. 265, 273–274) and the Koide line (12997) are as the card states.
- **CN-BULK-02 (card §7, last bullet; App AL p. 273 L25, p. 274 L25–26).** c⁴/(16πρ_P) = 3.1174 × 10⁻⁶⁵ has SI dimension m⁷ kg⁻¹ s⁻⁴ (= ħG²/(16πc)), not time. App AL's "ħ/(cπ³) … has dimensions of time" rests on an arithmetic slip that dropped G² (c⁴/(16π·(π²/16)·c⁵/(ħG²)) = ħG²/(π³c)), and ħ/c is kg·m in any case; App AL's statement one line earlier that the formula is "dimensionally correct" is also false. The card's number is right; its unit label, copied from App AL, is wrong. The verdict is unaffected (the identification fails dimensionally either way).
- **CN-BULK-03 (corpus).** The two printed EOS relations differ by a factor 2: E.3 p. 72 L22 "ρ₀ = 2K_BCT/c²" (K = ρ₀c²/2) versus AZ6 L91–92 and Letter 20 (K = ρ₀c²). The run used the §3 definition (K = ρ∂P/∂ρ = ρ₀c² for the printed EOS) throughout; E.3's factor would halve every κ and multiply every a† by √2.
- **CN-BULK-04 (corpus, AZ6 L168–169 vs L353–354).** ξ = ħ/√(2mgn₀) with g = mc²/n₀ gives ξ = ħ/(√2 mc), which is ℓ_P/√2 for m = m_P; the printed ξ = 2.32 ℓ_P requires m = 0.305 m_P (ratio 3.28). BUBBLE_BELLS N9 already records the resolution-by-m (0.305 → 0.238 with α_∞); the inconsistency with Letter 20's m = m_P is recorded here, not resolved (§4.4).
- **CN-BULK-05 (corpus, AZ7 Lemma "BCT on-site repulsion"; sentence only, outside scope).** With a = ℓ_P and m = m_P, U = ħ²/(2mξ²) = 4πα₀E_P while t = α₀E_P (App K), so t/U = 1/(4π) ≈ 0.08, not 1 (still above the quoted (t/U)_c ≈ 0.025, so the superfluid conclusion survives; the "exact" equality does not). Not followed.
- **CN-BULK-06 (corpus, AI.4 p. 265 L26).** ρ_Planck is printed as 5.1560 × 10⁹⁶ kg/m³; CODATA 2022 gives 5.1548 × 10⁹⁶ (0.02%). Immaterial.
- **CN-BULK-07 (pinned PDF, typesetting).** App AL's predicted G is printed as "0.000000×10⁻¹¹" at p. 273 L12, p. 274 L2, L5, L13 and L32; the intended value (6.684 × 10⁻¹¹, +0.151%) appears in AZ6 L429–432. Out of scope for this gate; recorded so the ledger does not misreport AL.

**Out-of-scope observation (not a CN, not followed, one sentence as §8 allows):** Letter 20 L233–242 evaluates α_GB = ħ²ρ₀/(32m) to m_Pc²/32 (an energy) and then boxes ℓ_P²/(8π) "in natural units" — the same dimension-by-fiat step as the K identification, in a route (Gate QP) already closed.

---

## Plain-language summary

The question was whether the BCT corpus's own equation of state gives the vacuum stiffness K an absolute size without quietly using Newton's constant to set it. It does not. Every version of K in the pinned files — the Gross–Pitaevskii one, the Bose–Hubbard one, the Madelung one, and the new "stiffness lives in the voids" one — gets its size from one of three declared inputs: the Planck density, the Planck mass, or the lattice spacing set equal to the Planck length. All three are G in disguise, and the corpus says so in its own words in at least four places (Letter 20's input audit, App E's roadmap, Letter 9's summary, App AL's key result). On top of that, none of the printed formulas G = c⁴/(8πK), G = c²/(8πρ₀), G = c⁴/(16πρ) has the right units as written; each only works after a hidden factor of ℓ_P² is inserted, and the "geometric 1/(8π)" of the November PDFs is that insertion read backwards. The Madelung version cannot even be checked, because the appendix it cites is not in the pinned volume and its Madelung constant is never defined. The void-localised version changes K by φ and α_∞, which are pure numbers and cannot remove G. Verdict SC-BULK-1: the hypothesis yields no G without G; "Exact / Zero Param" is withdrawn; nothing here touches the closed action-matching gates. The measurements the card asked for are tabulated — κ = 1 and a†/ℓ_P = 1/√(8π) for the corpus's own K (these are Planck-unit identities, not findings), κ = 4√2πα₀ for the Bose–Hubbard K, φ-scaled values for the void variant, f_K = φ/α_∞ ≈ 0.158 under the pre-registered homogenisation rule — with no verdict attached, as the card requires. Seven correction notices, one of them against the card's own §7 unit label.

---

## Protocol record and deviations

- Card fetched by commit-pinned raw URL (`raw.githubusercontent.com/…/cec526f…/audit/gates/gate_BULK_prompt.md`) with curl to disk and hashed before being re-read; digest matched `audit/gates/PREREG_20261111_BULK.sha256`. `bulk_dimcheck.py` likewise.
- **Disclosure:** the apply script that produced commit C (and so the card text, verbatim) was attached to this thread by Michel before the run began, so the card had been in the analyst's context before the raw-URL fetch; the attachment's embedded card hashed to the same digest. The pre-registration itself was found already pushed (commit C, 10:38:53 +1100) and was not re-done here.
- Memory and past-chat retrieval: this session reports no memory enabled; no Project document was read during the run; the only inputs were the raw-URL card, the pinned worktree at 9582c54, and CODATA 2022.
- Sources checked out in a detached worktree at `9582c54b6f22fc78eee0dc356f6d49cdfadd68b3`; all six §4.1 digests verified (`sources_9582c54.sha256`) before reading. `audit/gates/BULK/` at C contained only `bulk_dimcheck.py`; no result file existed.
- Order followed: Q1 ledgers → Q2 per variant → (Q3 not opened) → Q4.
- The session cannot push; deliverable returned as a `git format-patch` bundle adding `audit/gates/BULK/`.
- Nothing in §3–§5 was changed after the run started. No new field, coupling, scale or convention was added (§4.6).

## Files

`gate_BULK_RESULT.md` (this file) · `bulk_q4.py` → `output/q4_table.txt` · `bulk_ledger_cites.py` → `output/ledger_cites.txt` (every cited line, printed after re-hashing the pinned files) · `sources_9582c54.sha256` · `prompt_asrun.md` (the as-run prompt and run log) · `bulk_dimcheck.py` (card-thread, unchanged) · `SHA256SUMS`.
