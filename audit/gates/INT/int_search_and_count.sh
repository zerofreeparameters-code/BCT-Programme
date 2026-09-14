#!/usr/bin/env bash
# GATE INT — search-space audit + downstream footprint. Run from repo root.
set -e
echo "== TEX COUNTS =="
echo "all .tex:        $(find . -name '*.tex' | wc -l)   (expect 134)"
echo "root .tex:       $(find . -maxdepth 1 -name '*.tex' | wc -l)   (expect 26)"
echo "tex/*.tex:       $(ls tex/*.tex | wc -l)   (expect 108; NOT the corpus)"
echo "== VOL1/VOL2 (genuine PDFs, pymupdf) =="
echo "Vol1 Part1/2/3 pages: 425/425/25 = 875"
echo "Vol2 (zip->pdf) pages: 582"
echo "== INTERIOR-B footprint (hopfion/OHC/S^3->S^2/Hopf charge) =="
grep -rl -iE "hopfion|Octet-Hopfion|OHC|Hopf invariant|Hopf charge|S\^3.*S\^2|pi_3\(S\^2\)" . --include='*.tex' | wc -l
echo "== INTERIOR-A footprint (dual-phase/derivative-jump/kappa_0=3.39/single-component) =="
grep -rl -iE "dual-phase|two-component condensate|derivative jump|kappa_0|3\.39|single-component" . --include='*.tex' | wc -l
echo "== App AG hybrid check (names OHC, computes Bessel) =="
grep -c -iE "OHC" tex/BCT_Appendix_AG1_VacuumLuminescence_final.tex
grep -c -iE "Bessel|j_\{?1,1\}?" tex/BCT_Appendix_AG1_VacuumLuminescence_final.tex
