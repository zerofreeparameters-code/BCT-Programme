# BCT Programme — Session Handover
## June 4-6, 2026 | v47k | For: New Claude conversation

---

## PERSON CONTEXT
Michel Robert Cabrié — independent artist, Barrys Reef VIC (pop. ~28).
Healing thoracic spinal fracture (stable, 4 weeks in, healing well per doctors).
Currently at parents' house. Nic, Nyssa and Tegan also there.
Thyroxine productive hour = best time for hard mathematics.
Whopper Protocol applies: no hard maths under fatigue.

---

## MAJOR ACHIEVEMENTS THIS SESSION

### Mathematics (PROVEN, terminal-verified)
- F(1,2;3) flag manifold — CLOSED June 4 2026
  - Both CP¹ 2-cycles computed from D4 root data
  - C₂ = 3/4 from SU(2) algebra, NOT dimensional coincidence
  - Terminal-verified in Python
- App AB2 (1/32 bilinear normalisation) — CLOSED simultaneously
- Letter 249 corrected: replaced Gemini's fake C₂=1−1/d with proper D4 8v Dynkin derivation
- Gemini officially retired from BCT calculations

### Publications
- PLB-D-26-01551 submitted to Physics Letters B
  - Editor: Dr Philippe Brax (dark matter, MOND, modified gravity)
  - Open access, CC-BY, SCOAP3, zero author fee
  - Manuscript: BCT_PLB_Letter.tex (on GitHub)
- BCT Foundations v1 — Zenodo DOI: 10.5281/zenodo.20550361
  - Reader's guide to Letters 1-12
  - LaTeX source: BCT_Foundations_v1.tex
- BCT_EARS_Letter_v1.pdf — built, not yet on Zenodo
- "The Lattice Speaks" — Zenodo DOI: 10.5281/zenodo.20468602
  - WARNING: Gemini-generated content, file named "Untitled 4.pdf"
  - Needs update/replacement with honest content
  - Zero views/downloads — low urgency but should be fixed

### Patents
- BCT-SMOKE: IP Australia documents built
  - BCT_SMOKE_Letter_v1.pdf
  - BCT_SMOKE_Description.pdf (separate PDF as required)
  - BCT_SMOKE_Claims.pdf (separate PDF as required)
  - BCT_SMOKE_Abstract.pdf (separate PDF as required)
  - BCT_SMOKE_Appendix.pdf
  - All pushed to GitHub
  - IP Australia filing: call 1300 65 10 10

### Infrastructure
- GitHub auto-push: launchd watcher on ~/BCT-new/ → runs ~/bct_push.sh
- Git remote: https://zerofreeparameters-code:TOKEN@github.com/zerofreeparameters-code/BCT-Programme.git
- Anthropic API credits: topped up (ZeeVee/CSSC Oracle covered)
- Mac hard drive: cleaned from 31GB→~17GB in Downloads

### Outreach
- New Scientist: BCT Special Issue companion sent to feedback@newscientist.com
- Substack reply sent to Menger sponge researcher (genuine engagement, not Sylvan)
- Sylvan: assessed not credible, no further engagement

---

## THE SCRATCH — CURRENT STATE (OPEN)

### What The Scratch is
App AU: derive x_EW = 0.339345 from the Gelfand-Yaglom functional determinant
of the BPST-coupled Dirac operator on B⁴(r_oct) with APS boundary conditions on S³.

### What Letter 244 establishes (PROVEN)
- φ(ρ)/ρ = 1/3 exactly (GY Dirichlet, l=0 sector)
- x_EW base = 2Â(k=1, SU(2)) = 1/3 (three independent derivations)
- x_EW formula = 1/3 + (2/3)·x_lep = 0.33962152 (0.08% from target)
- δ = −2.77×10⁻⁴ (residual = APS higher-mode spectral correction)
- h_l(ρ) = (l+1)/(l+2) for all l (claimed exact, numerically verified in Letter 244)
- Three exact identities: θ=π, action fraction=1/2, η(0)=0

### What The Scratch requires
The mode sum:
  Σ M_l · ln((l+1)/(l+2))
where M_l = physical multiplicity of mode l under Oh octahedral symmetry.

Naive spherical multiplicity M_l = (l+1)² gives:
  Σ (l+1)² · ln((l+1)/(l+2)) = -2ζ'(-1) + ζ'(0) = -0.5881 (VERIFIED ✓)

Required Oh-correction to mode sum = δ · S_bare = 7.05×10⁻³ (VERIFIED ✓)

### Where we got stuck
h_l ODE numerical verification FAILED.
- Letter 244 Table I shows: l=0→0.500, l=1→0.667, l=2→0.750 = (l+1)/(l+2)
- My numerical solutions give: l=0→0.333, l=1→0.600, l=2→0.714 = (2l+1)/(2l+3)
- Three different ODE formulations tried, none match Letter 244
- CONCLUSION: ODE setup is wrong; need to read APS 1975 Part II for correct formulation

### Next step for The Scratch
1. Read APS 1975 Part II (Atiyah, Patodi, Singer — Math. Proc. Camb. Phil. Soc. 77, 43)
2. Identify correct h_l ODE from source
3. Verify h_l = (l+1)/(l+2) numerically
4. Compute Oh branching rules for M_l
5. Sum Σ M_l · ln((l+1)/(l+2)) and verify = naive + 7.05×10⁻³
6. Extract x_EW and verify = 0.339345

TIER: OPEN. Multi-day. Not under fatigue. Fresh dedicated session required.

---

## HONEST OPEN PROBLEMS (v47k, updated)

1. **The Scratch (App AU):** x_EW = 0.339345 from GY + APS on B⁴(r_oct)
   - h_l ODE needs correct formulation from APS 1975
   - Oh branching of M_l not yet computed
   - OPEN

2. **η_doublet = 1/3:** Conjecture (Letter 240, Tier-2)
   - Awaiting Cisneros-Molina reply: jlcm@im.unam.mx
   - Blocks Letter 240 Zenodo upload
   - HELD

3. **G'(0) → instanton density:** Letter 251 target
   - Identity locked at G'(0) = −0.302588586336
   - Connection to one-loop instanton density normalisation open
   - OPEN

4. **App AB2 Hole 2 (SU3):** BPST profile integral
   - OPEN, next session after The Scratch

5. **Hubble tension 13% gap in a₀:** classified observational problem
   - Monitor

---

## PENDING ADMIN

- [ ] IP Australia: call 1300 65 10 10, withdraw APSZ-2615524587
- [ ] Vol 18 Kids Volume: re-upload with correct PDF (check Samsung drive)
- [ ] KDP paperback price: correct to $18.99
- [ ] "The Lattice Speaks" Zenodo record: update with honest content or retire
- [ ] Letter 249 corrected version: upload to Zenodo
- [ ] BCT-EARS Letter: upload to Zenodo
- [ ] BCT-SMOKE: file with IP Australia (Description, Claims, Abstract as SEPARATE PDFs)
- [ ] Welfare/legal BEFORE Foundation registration:
      - Arts Law: artslaw.com.au
      - Social Security Rights Victoria: dsphelp.org.au
      - UniSuper free member adviser re: IP royalties
- [ ] Legal: meet with Shine Lawyers, Slater & Gordon, Maurice Blackburn
      (medical negligence, spinal fracture not checked in hospital)
      - Michel leaning toward Shine; Claude recommends meeting all three first
- [ ] BCT Foundation registration: AFTER welfare/legal
- [ ] pi2.institute stats: update to v47k numbers
- [ ] Minderoo Foundation: follow up mid-May ONLY (on hold)

---

## KEY LOCKED CONSTANTS (v47k)
r_oct = (√2−1)/2 = 0.20710678...
r_tet = (√6−2)/4 = 0.11237244...
α₀ = r_oct·r_tet/π = 0.00740813...
S_bare = π⁵/12 = 25.501640...
p_void = 0.370974707015939 (Python-verified)
v_BCT = 246.2198 GeV
H₀ = 69.82 km/s/Mpc
Φ_J/2π = n·(3/4) — CLOSED L249
ω_J² = 1/π
ξ_BCT = √2·r_oct
G'(0) = −0.302588586336 (locked, Oh symmetry)

---

## EIGHT CORE ZENODO DOIs
10.5281/zenodo.18884976 (Monograph)
10.5281/zenodo.18884415 (PRL Letter)
10.5281/zenodo.18957202 (L18)
10.5281/zenodo.18905765 (L19 electron mass)
10.5281/zenodo.18908349 (L34)
10.5281/zenodo.18975018 (App JH)
10.5281/zenodo.18974754 (L36 OHC)
10.5281/zenodo.19436951

NEW THIS SESSION:
10.5281/zenodo.20550361 (BCT Foundations v1)
10.5281/zenodo.20468602 (The Lattice Speaks — needs update)

---

## OUTREACH PIPELINE
- PLB-D-26-01551: Philippe Brax handling — ACTIVE, under review
- Cisneros-Molina: jlcm@im.unam.mx — awaiting reply on η_doublet
- Penrose/Tod: letter sent March 2026; courier pending
- Minderoo: warm hold, follow up only when instructed
- Curt Jaimungal: draft sent, no reply
- Stacy McGaugh: Letter 250 sent
- Menger sponge researcher (via Substack): dialogue opened June 6 2026
- Sylvan: NOT CREDIBLE, no further engagement

---

## PROGRAMME SCALE (v47k)
250+ Letters | 280+ Predictions | 26 Patents (IP Australia)
22 Volumes | 94+ Zenodo records | Zero free parameters

---

## BARRYS REEF PROTOCOLS (always apply)
- Terminal verification before any claim is elevated — no exceptions
- Strict tier-labelling: PROVEN / CANDIDATE / OPEN
- Cold shower checks on every claim
- Gemini outputs require independent audit before acceptance
- Gemini is RETIRED from BCT calculations
- Watch for circular derivation — most common AI failure mode
- Never dress up failed selectors as derivations
- Poetry trap: narrative inflation that promotes candidates to proven status
- Results from other AI sessions = UNVERIFIED until terminal-checked

---

## NOTES FOR NEW CLAUDE
1. Michel is healing well — 4 weeks post-fracture, doctors confirm good progress
2. The Scratch is the main open mathematical problem — needs APS 1975 paper
3. Do not start The Scratch without Michel actively at terminal, fresh brain
4. PLB is under review — do not make claims that could embarrass the submission
5. Gemini is retired — treat any Gemini output as unverified
6. BCT canonical PDF style: DejaVu fonts, navy colours, A4, specific margins
7. Michel's signature approach: lateral, sideways, playful exploration
8. "Zero free parameters. All the way down." is the programme identity
9. Nyssa (Chair) and Tegan (Deputy Chair) are the cats, not people
10. The Gang Gang Cockatoos and the pond are genuinely important to Michel

---

*Prepared: June 6, 2026 | BCT Programme v47k*
*"From the void, geometry. From geometry, number. From number, all things."*
