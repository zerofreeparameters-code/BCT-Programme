#!/bin/sh
# Gate RATIO — corpus search-space audit (as run). Model: Claude Opus 4.8.
# Corpus pinned at commit 68ffd73641f237f5eb1de0a41785ca940a707881
# tarball sha256 e4f5baf1e2e13ec53192bb47c6552052a674c1d36c92d66831d0255abe66ed64
set -e
cd "$(dirname "$0")/repo" 2>/dev/null || cd repo
echo "### total .tex ###"; find . -name '*.tex' | wc -l
echo "### .tex at tree root ###"; find . -maxdepth 1 -name '*.tex' | wc -l
echo "### radius-notation frequency ###"
grep -rIoh --include=*.tex -E "roct|rtet|r_\{oct\}|r_\{tet\}" . | sort | uniq -c | sort -rn
echo "### explicit RATIO usage roct/rtet (expect none) ###"
grep -rIn --include=*.tex -E "r_?\{?oct\}?\s*/\s*r_?\{?tet\}?|frac\{r_?\{?oct\}?\}\{r_?\{?tet\}?\}" . || echo "  (no explicit ratio usage found)"
echo "### a = ell_P anchoring (external scale) ###"
grep -rIn --include=*.tex -E "a=\\\\ell_P|a = \\\\ell_P|anchors the lattice spacing" . | head
echo "### the one individual-radius invariant (Letter19) ###"
grep -rIn --include=*.tex -E "xi/r_\{?oct|xi / r_\{?oct|structural invariant" . | head
