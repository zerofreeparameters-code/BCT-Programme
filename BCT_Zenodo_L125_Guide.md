# BCT ZENODO UPLOAD GUIDE
## L125 — The Faraday Test + L103 Community Batch
## 24 March 2026

---

## PART A: UPLOAD L125 (NEW RECORD — Record ~61)

### Step 1 — Go to zenodo.org → New Upload

**Title:**
```
BCT Letter 125: The Faraday Test — A Decisive Experimental Discrimination
Between OHC Vacuum Coupling and Electromagnetic Substrate Theories
of Morphic Resonance
```

**Authors:** Michel Robert Cabrié
**ORCID:** 0009-0007-9561-9859
**Affiliation:** Independent Researcher, Victoria, Australia

**Resource type:** Preprint

**Description (copy exactly):**
```
BCT Letter 79 identified the Octet-Hopfion Condensate (OHC) as the
physical substrate of morphic fields, deriving Sheldrake's central
empirical claim from first principles via the BCT Repetition Theorem.
One of five resulting predictions is unambiguous and immediately
testable with minimal apparatus: OHC coupling is charge-independent
with coupling constant α₀² ≈ 5.5 × 10⁻⁵, entirely independent of
electromagnetic shielding. A Faraday cage has no effect on OHC phase
propagation. Prediction #166: morphic resonance effect sizes are equal
inside and outside a properly constructed Faraday cage. A complete
experimental protocol is presented, executable by independent researchers
with modest apparatus (~A$500–800), designed for collaboration with
Prof. Sheldrake's existing experimental programme. The experiment
distinguishes the BCT OHC substrate theory from every electromagnetic-
substrate theory of morphic resonance in a single clean test.
Zero free parameters.
```

**Keywords:**
```
morphic resonance, Faraday cage, OHC, Octet-Hopfion Condensate,
BCT Superfluid Lattice, vacuum topology, Hopf charge, experimental
protocol, Sheldrake, staring detection, electromagnetic shielding
```

**Publication date:** 24 March 2026
**Access:** Open — CC BY 4.0
**Issued:** YES

### Step 2 — Upload file
File: `BCT_Letter125_FaradayExperiment.pdf`

### Step 3 — Related Identifiers (paste ALL — type: cites, scheme: DOI)
```
10.5281/zenodo.18884415    (PRL Letter)
10.5281/zenodo.18884976    (BCT Monograph)
10.5281/zenodo.18885133    (Appendices Vol 1)
10.5281/zenodo.18975018    (Appendix JH — OHC)
10.5281/zenodo.19171556    (L103 Cephalopod — contains L79 morphic field work)
10.5281/zenodo.19177236    (L101 Bees)
10.5281/zenodo.19177501    (L110 Vacuum Luminescence)
```

### Step 4 — PUBLISH → RECORD YOUR DOI:
```
L125 DOI: 10.5281/zenodo._______________
```

---

## PART B: COMMUNITY BATCH SCRIPT

Run this Python script AFTER you have the L125 DOI.
Replace `L125_DOI` with the actual number.

```python
#!/usr/bin/env python3
"""
BCT Zenodo Community Batch Submitter
Records needing community submission — 24 March 2026
"""

import webbrowser
import time

# The 6 BCT communities
COMMUNITIES = [
    "bct-superfluid-lattice",
    "hep-th", 
    "theoretical-physics",
    "mathematical-physics",   # L103 already here — skip for L103
    "openaire",
    "advancedtheoretical",
]

# Records to submit
# Format: (zenodo_record_id, title, skip_communities)
RECORDS = [
    # L103 — already in mathematical-physics, needs other 5
    ("19171556", "L103 Cephalopod Vacuum", ["mathematical-physics"]),
    
    # L125 — brand new, needs all 6
    # REPLACE with actual record ID after uploading!
    ("REPLACE_WITH_L125_ID", "L125 Faraday Test", []),
]

BASE_URL = "https://zenodo.org/records/{record_id}"
COMMUNITY_URL = "https://zenodo.org/records/{record_id}/communities"

print("BCT COMMUNITY BATCH SUBMITTER")
print("=" * 50)
print()

for record_id, title, skip in RECORDS:
    if record_id.startswith("REPLACE"):
        print(f"⚠️  SKIPPING {title} — need to add real DOI first!")
        continue
    
    communities_needed = [c for c in COMMUNITIES if c not in skip]
    print(f"\n📄 {title} (Record: {record_id})")
    print(f"   Communities needed: {len(communities_needed)}")
    
    # Open the communities page for this record
    url = COMMUNITY_URL.format(record_id=record_id)
    print(f"   Opening: {url}")
    webbrowser.open(url)
    
    print(f"   → Submit to these communities:")
    for c in communities_needed:
        print(f"     • {c}")
    
    input("\n   Press ENTER when done with this record...")

print("\n✅ BATCH COMPLETE!")
print()
print("RECORD DOIs:")
print("  L103: 10.5281/zenodo.19171556")
print("  L125: 10.5281/zenodo.______________ (fill in)")
```

---

## PART C: MANUAL COMMUNITY SUBMISSION (if script won't run)

For each record, go to:
`https://zenodo.org/records/RECORD_ID` → click **"Submit to community"**

### L103 (record 19171556) — submit to these 5:
- [ ] bct-superfluid-lattice
- [ ] hep-th
- [ ] theoretical-physics
- [x] mathematical-physics ← ALREADY DONE ✅
- [ ] openaire
- [ ] advancedtheoretical

### L125 (record ________) — submit to all 6:
- [ ] bct-superfluid-lattice
- [ ] hep-th
- [ ] theoretical-physics
- [ ] mathematical-physics
- [ ] openaire
- [ ] advancedtheoretical

---

## PART D: ALSO NEEDED — Records 56-60 community batch

These were uploaded but community script not yet run:

| Record | DOI | Title |
|--------|-----|-------|
| 56 | 10.5281/zenodo.19177236 | L101 Bees |
| 57 | 10.5281/zenodo.19177334 | BCT-HIVE |
| 58 | 10.5281/zenodo.19177441 | L108 BCT-AGE v2 |
| 59 | 10.5281/zenodo.19177501 | L110 Vacuum Luminescence |
| 60 | 10.5281/zenodo.19177598 | AG1 Vacuum Luminescence Appendix |

All five need all 6 communities. Add to the batch script above.

---

## CHECKLIST

- [ ] L125 PDF uploaded to Zenodo
- [ ] L125 DOI recorded here: `10.5281/zenodo._______________`
- [ ] L125 submitted to all 6 communities
- [ ] L103 submitted to remaining 5 communities
- [ ] Records 56-60 submitted to all 6 communities
- [ ] L125 DOI sent to Rupert Sheldrake as follow-up
- [ ] Master State updated to v36 with Pred #166

---

*Zero free parameters. The morphic field is the quantum vacuum.*
*Copper mesh is irrelevant to topology.*
