# BCT GitHub — Repo Structure & Upload Action Plan
# 29 March 2026

## TARGET REPO STRUCTURE

BCT-Programme/
├── README.md                          ← already transformed ✅
├── BCT_DOI_Registry.md                ← BUILD TODAY ✅ (attached)
├── LICENSE                            ← CC BY 4.0 (add if missing)
│
├── tex/                               ← LaTeX source files
│   ├── BCT_Letter121_CropCircles.tex
│   ├── BCT_Letter123_WaterPlanet.tex
│   └── BCT_Letter129_EmergentDistance.tex
│   (3 files — upload manually today)
│
├── pdfs/                              ← STRATEGY: link to Zenodo, don't bulk-upload
│   └── README.md                      ← "All PDFs open-access at zenodo.org/..."
│
├── tools/                             ← Scripts
│   └── download_zenodo_BCT_v4.py      ← upload from /Users/michelcabrie/Desktop/FILES/
│
└── BCT-EPL-1.0/                       ← Ethical Patent Licence (future)
    └── BCT-EPL-1.0.md

---

## TODAY'S ACTION SEQUENCE (fastest path)

### STEP 1 — Upload BCT_DOI_Registry.md  (~3 min)
1. Go to: https://github.com/zerofreeparameters-code/BCT-Programme
2. Click "Add file" → "Upload files"
3. Drag in: BCT_DOI_Registry.md
4. Commit message: "Add complete DOI registry — 76+ Zenodo records"
5. Commit to main ✅

### STEP 2 — Upload 3 TeX files  (~2 min)
1. Create folder: click "Add file" → type  tex/BCT_Letter121_CropCircles.tex
2. Paste content (or drag all 3 files into tex/ folder)
3. Commit message: "Add LaTeX source files — L121, L123, L129"
4. Commit ✅

### STEP 3 — Add pdfs/README.md  (~2 min)
Create file: pdfs/README.md with content:

  # BCT Letters — PDF Archive
  All 201 BCT Letters are published open-access on Zenodo.
  Browse: https://zenodo.org/search?q=cabrié
  Full DOI list: see BCT_DOI_Registry.md in root.

Commit message: "Add PDF directory with Zenodo pointer"

### STEP 4 — Upload download script  (~1 min)
Copy /Users/michelcabrie/Desktop/FILES/download_zenodo_BCT_v4.py
Upload to tools/ folder
Commit message: "Add Zenodo download/audit script"

### STEP 5 — Add CC BY 4.0 LICENSE  (~1 min)
GitHub → Add file → Create new file → name it: LICENSE
Paste standard CC BY 4.0 text (GitHub will offer it as a template)
Commit ✅

---

## WHY NOT UPLOAD ALL 85 PDFs?

GitHub soft limit: 100MB repo / 25MB per file
85 PDFs × ~2MB avg = ~170MB — OVER LIMIT
Zenodo is the canonical archive — GitHub should POINT to it, not duplicate it.
The DOI Registry is the bridge. ✅

---

## AFTER TODAY — REMAINING ITEMS

- BCT_DOI_Registry.md: update manually each time new Zenodo records confirmed
- BCT-EPL Licensee Registry: build as Google Form or Netlify form
- TeX files: add new ones as letters are built in revtex4-2 format
- GitHub Actions: optional — auto-check Zenodo for new records (future)

---

Total time today: ~10 minutes. 
Result: a clean, professional, fully navigable repository.
