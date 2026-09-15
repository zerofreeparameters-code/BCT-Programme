#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# BCT repo inventory — which gates have artifacts committed, which are empty.
# Scans <repo>/audit (and repo root) and buckets files by gate token, then
# compares against the Cold-Ledger roster of closed gates so gaps are visible.
# Usage: ./bct_repo_inventory.sh [REPO_DIR]     (default ~/BCT-Programme)
# The roster is from memory of the Cold Ledger — verify, don't trust blindly.
# ---------------------------------------------------------------------------
set -u
REPO="${1:-$HOME/BCT-Programme}"
[ -d "$REPO" ] || { echo "repo not found: $REPO (pass path as arg 1)"; exit 1; }

# gate tokens the ledger records as RUN AND CLOSED (or pre-registered)
ROSTER="FWD GEO STAT KND OP INVENTORY R2 P J LINK RANK MP PRED RATIO JHF KL KAUDIT \
IG SYM AM QP BZ SCR PH N F T"

echo ">> scanning: $REPO"
echo
# gather candidate artifact files (audit tree + any gate_/RESULT files at root)
LIST="$(mktemp)"
{
  find "$REPO/audit" -type f 2>/dev/null
  find "$REPO" -maxdepth 2 -type f \( -iname 'gate_*' -o -iname '*RESULT*' -o -iname 'inv_*' \) 2>/dev/null
} | grep -v '/\.git/' | sort -u > "$LIST"

printf '%-12s %-8s %s\n' "GATE" "FILES" "PATHS (relative to repo)"
printf '%-12s %-8s %s\n' "----" "-----" "------------------------"
for G in $ROSTER; do
  # match token as a word-ish boundary in the path (case-insensitive)
  hits="$(grep -iE "(^|[/_])gate[_-]?${G}([/_.]|$)|(^|[/_])${G}([/_.]|$)" "$LIST" 2>/dev/null \
          | grep -iE "${G}" | sed "s#^$REPO/##" | sort -u)"
  n="$(printf '%s' "$hits" | grep -c . )"
  if [ "$n" -eq 0 ]; then
    printf '%-12s %-8s %s\n' "$G" "0" "— none found (GAP if ledger says closed)"
  else
    first="$(printf '%s\n' "$hits" | head -1)"
    printf '%-12s %-8s %s\n' "$G" "$n" "$first"
    printf '%s\n' "$hits" | tail -n +2 | sed 's/^/                     /'
  fi
done

echo
echo ">> files under audit/ NOT matched to any roster gate (orphans / other):"
grep -ivE "$(printf '%s' "$ROSTER" | tr ' ' '|')" "$LIST" | sed "s#^$REPO/##" | sed 's/^/   /' | head -40
echo
echo ">> known gaps the Cold Ledger already flags (recover these first if absent):"
echo "   FWD  : gate_FWD_Deliverable.md + gate_FWD_grammar_PREREG.md + 5x gate_FWD_*.py"
echo "   STAT : clean re-run of gate_STAT_sections2to5.py was recommended, not done"
echo "   J    : gate_J deliverable + gate_J_step1.py were 'only in chat'"
echo "   KAUDIT: today's 5 files (apply KAUDIT_gate.patch) + scoping note x2"
echo "   plus assorted prereg prompts noted as 'only in session outputs'"
rm -f "$LIST"
