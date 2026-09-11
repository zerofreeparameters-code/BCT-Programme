#!/bin/bash
# Downstream scan. Search space = repo(134 tex + md/py) + mount(33 unzipped txt layers + 14 pdftotext + 2 plain-text appendix vols)
# Patterns: any NUMERIC use of a Josephson coupling, or a citation of App J for one.
PAT='[Jj]osephson|Appendix[ ~]J[^HXQ]|\\cite\{AppJ\}|AppJ\b'
NUM='g *= *\\?α₀|g *= *\\?\\alpha|t *= *\\?α₀|t *= *\\?\\alpha_?0|0\.00740806|0\.0074081|0\.00036975|3\.3905|3\.39|κ₀|\\kz'
echo "### A. files matching a Josephson/AppJ reference"
grep -rlE "$PAT" BCT-Programme-cec214b --include='*.tex' --include='*.md' --include='*.py' unz mounttxt 2>/dev/null | sort
echo
echo "### B. of those, lines that use a coupling NUMERICALLY"
for f in $(grep -rlE "$PAT" BCT-Programme-cec214b --include='*.tex' --include='*.md' --include='*.py' unz mounttxt 2>/dev/null); do
  h=$(grep -nE "$NUM" "$f" | grep -viE 'gate_|crossaudit' )
  if [ -n "$h" ]; then echo "== $f"; echo "$h" | head -6 | sed 's/^/    /'; fi
done
