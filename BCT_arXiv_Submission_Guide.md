# BCT arXiv Submission Guide
## Complete Step-by-Step Instructions for Three-Paper Submission
### Prepared for Michel Robert Cabrié — March 2026

---

## QUICK ANSWERS TO YOUR QUESTIONS

**Do I submit all three via arXiv?**
Yes. All three papers go on arXiv. You submit them as three separate arXiv submissions (each gets its own arXiv ID), but you coordinate them so they cross-reference each other. Submit them on the same day if possible, or within the same week.

**Do I need to wait for my email address change?**
No. Submit now with whatever email is on your account. The email on your arXiv profile is only used for arXiv to contact you about moderation — it does not appear on the paper. Your papers already have ZeroFreeParameters@gmail.com hardcoded in the LaTeX source. You can update your arXiv email later.

**Do I need endorsement?**
If this is your first arXiv submission to hep-ph, you will need endorsement from an established arXiv author in that category. Check your arXiv account — if it says "Awaiting endorsement" for hep-ph, you'll need to get endorsed first. If you've submitted before (even in a different category), you may already be endorsed. If you need endorsement, email moderation@arxiv.org explaining your research programme.

---

## SUBMISSION ORDER AND TIMING

Submit in this order, ideally all on the same day:

| Order | Paper | arXiv Category | Journal Target |
|-------|-------|----------------|----------------|
| 1st | PRL Letter (Paper 1) | hep-ph (primary) | Physical Review Letters |
| 2nd | Strong CP Letter (Paper 2) | hep-ph (primary) | Physical Review Letters |
| 3rd | PLB Monograph (Paper 3) | hep-ph (primary) | Physics Letters B |

**Why this order?** The PRL Letter is the flagship — it contains the full 92-prediction summary. The Strong CP Letter references it. The Monograph references both Letters. Submitting in this order means each paper's arXiv ID is available when the next one needs it.

**Timing tip:** If you submit all three before 14:00 ET (US Eastern) on a weekday, they will typically all appear together on arXiv the following evening (~20:00 ET).

---

## BEFORE YOU START: CHECKLIST

- [ ] arXiv account active (arxiv.org — logged in)
- [ ] Endorsement confirmed for hep-ph (check under "Endorsement status")
- [ ] All three .tex files compile cleanly in Overleaf
- [ ] Download each Overleaf project as a .zip (Source → Download as ZIP)
- [ ] You have this guide open in a separate tab

---

## SUBMISSION 1: PRL LETTER (Paper 1)

### Step 1: Download from Overleaf
In your Overleaf PRL Letter project, click **Menu → Download → Source**. This downloads a .zip file containing your .tex and all supporting files.

### Step 2: Start new arXiv submission
1. Go to https://arxiv.org/submit
2. Click **"Start New Submission"**

### Step 3: Choose category
- **Primary:** hep-ph (High Energy Physics - Phenomenology)
- **Cross-list:** hep-th (High Energy Physics - Theory), gr-qc (General Relativity and Quantum Cosmology)

### Step 4: Upload files
Upload the .zip file from Overleaf. arXiv will compile the LaTeX on their servers.

**IMPORTANT:** Do NOT include `revtex4-2.cls` in your zip — arXiv has it pre-installed and including it causes conflicts.

### Step 5: Check the compiled PDF
arXiv shows you a preview. Check carefully:
- Title renders correctly
- Equations display properly
- Table I (precision summary) is complete
- References are numbered correctly
- Author name and ORCID appear

### Step 6: Fill in metadata

**Title:**
```
Zero Free Parameters: Deriving 92 Standard Model Observables from Body-Centred Tetragonal Vacuum Geometry
```

**Authors:**
```
Michel Robert Cabrié
```

**Abstract (plain text — no LaTeX):**
```
We report that 92 observables of the Standard Model and beyond -- including all particle masses, mixing angles, CP phases, coupling constants, and hadronic spectroscopy -- can be derived to sub-1% precision from three inputs: the octahedral and tetrahedral void radii of a body-centred tetragonal (BCT) lattice with axial ratio c/a = sqrt(2), r_oct = (sqrt(2)-1)/2 and r_tet = (sqrt(6)-2)/4, plus a single dimensionful anchor Lambda_QCD = 220 MeV. No parameters are adjusted. The BCT crystal coupling alpha_0 = r_oct r_tet / pi = 0.0074081 yields the fine structure constant alpha = alpha_0(1 - 2 alpha_0) = 1/137.018 (error -0.013%), while the D4 root lattice provides exactly three generations via triality and solves the strong CP problem (theta-bar = 0 exact). A baryon Regge tower built from void-geometric coefficients predicts seven baryon masses to sub-0.3%, and 16 parameter-free structural theorems connect BCT geometry directly to the meson spectrum, electromagnetic radii, and the Planck mass m_P = M_R / alpha_0^2 (-0.08%). Of the 92 sub-1% predictions, 32 are sub-0.1% and 18 are sub-0.01%.
```

**Comments:**
```
3 pages, 1 table. Companion papers: arXiv:26XX.YYYYY [hep-ph] (Strong CP) and arXiv:26XX.ZZZZZ [hep-ph] (full monograph with 473 appendices)
```
*(You'll update these arXiv IDs once you have them — see "After Submission" below)*

**Journal reference:** Leave blank for now (fill in after journal submission)

**Report number:** Leave blank

**DOI:** Leave blank

**ORCID:** 0009-0007-9561-9859

### Step 7: Submit
Click **"Submit"**. You'll receive a confirmation email with your submission ID.

**WRITE DOWN YOUR ARXIV ID** — you need it for Papers 2 and 3.

---

## SUBMISSION 2: STRONG CP LETTER (Paper 2)

### Before uploading:
Update the .tex file reference [9] to include the actual arXiv ID from Paper 1:
```
[9] M. R. Cabrié, "Zero Free Parameters: ..." arXiv:26XX.XXXXX [hep-ph].
```

### Metadata

**Title:**
```
Geometric Resolution of the Strong CP Problem without an Axion
```

**Authors:**
```
Michel Robert Cabrié
```

**Abstract (plain text):**
```
The strong CP problem -- why the QCD vacuum angle satisfies |theta-bar_QCD| < 10^{-10} despite receiving O(1) contributions -- has resisted solution for nearly fifty years. The Peccei-Quinn axion remains undetected after four decades of experimental searches. We present a geometric resolution within the Body-Centred Tetragonal Crystal Theory (BCT), in which the quantum vacuum crystallises into a D4 root lattice with tetrahedral void symmetry group T_d. Three independent mechanisms enforce theta-bar_QCD = 0 exactly: (i) the Z_2 centre of the D4 Weyl group maps theta to -theta, requiring theta_bare = 0; (ii) T_d reflection symmetry forces all BCT Yukawa couplings to be real, giving arg det M_q = 0 to all orders; (iii) D4 modular self-duality (D4* = D4) makes the partition function satisfy Z(theta) = Z(-theta). The result is radiatively stable: the one-loop correction delta-theta ~ J_BCT/(16 pi^2) = 2.4 x 10^{-9} is 23 orders of magnitude below the residual theta_res = (Lambda_QCD/M_R)^2 alpha_0 = 8.0 x 10^{-34}. BCT predicts d_n = 1.0 x 10^{-32} e.cm (CKM contribution only; no QCD theta-term), testable at n2EDM and next-generation facilities. No axion is required or predicted.
```

**Comments:**
```
3 pages, 1 table. Companion to arXiv:26XX.XXXXX [hep-ph] (92 predictions letter)
```

**Category:** hep-ph (cross-list: hep-th)

**ORCID:** 0009-0007-9561-9859

Follow the same upload → check → submit workflow as Paper 1.

---

## SUBMISSION 3: PLB MONOGRAPH (Paper 3)

### Before uploading:
Update the .tex references to include actual arXiv IDs for both Letters:
```
[6] M. R. Cabrié, "Zero Free Parameters: ..." arXiv:26XX.XXXXX [hep-ph].
[7] M. R. Cabrié, "Geometric Resolution ..." arXiv:26XX.YYYYY [hep-ph].
```

### Metadata

**Title:**
```
The BCT Superfluid Lattice Model: Complete Derivation of Standard Model Parameters from Vacuum Geometry
```

**Authors:**
```
Michel Robert Cabrié
```

**Abstract (plain text):**
```
We present the Body-Centred Tetragonal (BCT) Superfluid Lattice Model, a geometric framework that derives 92 Standard Model observables to sub-1% precision from three inputs: the octahedral and tetrahedral void radii of a BCT lattice with axial ratio c/a = sqrt(2), r_oct = (sqrt(2)-1)/2 and r_tet = (sqrt(6)-2)/4, plus a single dimensionful anchor Lambda_QCD = 220 MeV. No parameters are adjusted. The BCT crystal coupling alpha_0 = r_oct r_tet / pi = 0.0074081 yields the fine structure constant alpha = alpha_0(1 - 2 alpha_0) = 1/137.018 (error -0.013%). The D4 root lattice provides exactly three generations via triality and solves the strong CP problem (theta-bar = 0 exact). All six quark masses, three charged lepton masses (via the Koide formula), the complete CKM and PMNS mixing matrices, seven baryon masses, eight meson masses, electromagnetic radii, the Planck mass, the cosmological constant, the Hubble constant, and the spectral index are derived with zero free parameters. Sixteen structural theorems -- parameter-free algebraic identities -- connect BCT geometry directly to hadronic observables. Of the 92 sub-1% predictions, 32 are sub-0.1% and 18 are sub-0.01%. This paper presents the complete derivation framework; all 473 technical appendices are provided as supplementary material.
```

**Comments:**
```
53 pages, 8 tables, 473 supplementary appendices. Companion letters: arXiv:26XX.XXXXX and arXiv:26XX.YYYYY [hep-ph]
```

**Category:** hep-ph (cross-list: hep-th, gr-qc)

**ORCID:** 0009-0007-9561-9859

---

## AFTER ALL THREE ARE SUBMITTED

### 1. Update cross-references
Once all three arXiv IDs are assigned, go to **"My Submissions"** on arXiv and use **"Replace"** to upload updated versions of each paper with the correct arXiv IDs filled in. Add a note:
```
v2: Updated companion paper arXiv cross-references. Results unchanged.
```

### 2. Submit to journals (parallel process)

**PRL Letter → Physical Review Letters**
- Go to https://journals.aps.org/prl/authors
- Create account / log in
- "Submit a manuscript"
- Upload the .tex source
- Cover letter should mention: "This paper has been posted on arXiv as [ID]. It is the first of three companion papers presenting the BCT framework."
- Suggested reviewers: choose 2-3 phenomenologists working on SM precision tests

**Strong CP Letter → Physical Review Letters**
- Same portal
- Cover letter: "Companion to arXiv:[PRL ID]. Presents the geometric resolution of the strong CP problem within the BCT framework."

**PLB Monograph → Physics Letters B**
- Go to https://www.editorialmanager.com/plb/
- Create account / log in
- Upload the .tex source
- Cover letter: "This is the full monograph companion to two PRL letters [arXiv IDs]. It presents the complete derivation framework with 92 sub-1% predictions from zero free parameters."

### 3. Handling moderation holds
Papers with unconventional claims sometimes get placed on "hold" for additional review. If this happens:
- You'll receive an email from arXiv moderation
- Reply politely and concisely
- Emphasise: the paper engages with standard physics (QCD, SM, Planck data), all predictions are numerically testable against PDG data, and the mathematical framework (D4 lattice geometry, Koide formula, Regge theory) uses well-established tools
- Do not argue — provide context
- Holds are typically resolved within a few days

### 4. After papers appear on arXiv
- Share the arXiv links
- Papers are permanently citable as arXiv:26XX.XXXXX
- When journal acceptance comes, update arXiv metadata with "Accepted for publication in [Journal]" and add the DOI

---

## USEFUL LINKS

| Resource | URL |
|----------|-----|
| arXiv submission | https://arxiv.org/submit |
| arXiv help | https://info.arxiv.org/help/submit.html |
| PRL submission | https://journals.aps.org/prl/authors |
| PLB submission | https://www.editorialmanager.com/plb/ |
| Your ORCID | https://orcid.org/0009-0007-9561-9859 |
| arXiv moderation help | moderation@arxiv.org |
| arXiv general help | help@arxiv.org |

---

*This guide was prepared for the BCT programme arXiv submission, March 2026.*
