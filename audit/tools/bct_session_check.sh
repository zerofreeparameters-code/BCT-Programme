#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# BCT session file check — 15 Sep 2026 session (KAUDIT + App K m_e scoping)
# Reports, for each file created this session:
#   (1) have you downloaded it?   (searched by CONTENT HASH, not filename)
#   (2) is it in your git repo, committed?
# Usage:
#   ./bct_session_check.sh [REPO_DIR] [DOWNLOADS_DIR]
# Defaults: REPO_DIR=~/BCT-Programme   DOWNLOADS_DIR=~/Downloads
# ---------------------------------------------------------------------------
set -u
REPO="${1:-$HOME/BCT-Programme}"
DL="${2:-$HOME/Downloads}"

# cross-platform sha256 -> lowercase hex, first field only
hash_of() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | awk '{print $1}';
  else shasum -a 256 "$1" | awk '{print $1}'; fi
}

# manifest: HASH|display_name|expected_repo_path|kind
MANIFEST="
9562bb7acf8ae08719898ffc340829cdaa2b1144b27d5348d832c22c79d08633|gate_KAUDIT_RESULT.md|audit/gates/KAUDIT/gate_KAUDIT_RESULT.md|kaudit
08ea655ec3f39c446b100f2bf92cd5f2aac4ad6619b046a7bd51993c661430b1|gate_KAUDIT_prompt_asrun.md|audit/gates/KAUDIT/gate_KAUDIT_prompt_asrun.md|kaudit
8ef1266e8f0d165387e70b5117821709dc1266ba9321b564d600a4403340ef69|kaudit_1_lattice.py|audit/gates/KAUDIT/kaudit_1_lattice.py|kaudit
99f0d1dcbd4d1ffe8f64d2642cb008be18674801672505645be153407a07bc52|kaudit_2_band.py|audit/gates/KAUDIT/kaudit_2_band.py|kaudit
ec47b43298dd00e62478d368a573122b965e3b14f0648d15df8d69dfabb91943|kaudit_3_selfenergy_gap_n16.py|audit/gates/KAUDIT/kaudit_3_selfenergy_gap_n16.py|kaudit
5a22e5454225a17dfef39d5c6cbf68aa76f19a395f4313dc19c84d556ace0f62|KAUDIT_gate.patch|-|transport
4a87434b405b3f127c0990f124158357ea3b10f51a8451ceaa3c075f42e4cf5c|selfenergy_vertex2.py|audit/scoping/selfenergy_vertex2.py|scoping
2e0399d8cfb183ac97712d97cdc754a26b41855bf49db5670ebeb892e9ff8e39|scoping_K7_candidates.md|audit/scoping/scoping_K7_candidates.md|scoping
"

# Build a hash index of the downloads dir once (name+hash), for speed.
echo ">> indexing downloads: $DL"
DL_INDEX="$(mktemp)"
if [ -d "$DL" ]; then
  find "$DL" -type f 2>/dev/null | while IFS= read -r f; do
    printf '%s  %s\n' "$(hash_of "$f")" "$f"
  done > "$DL_INDEX"
else
  echo "   (downloads dir not found: $DL — pass it as arg 2)"
fi

# Build a hash index of the repo working tree once (excluding .git).
echo ">> indexing repo: $REPO"
REPO_INDEX="$(mktemp)"
IS_GIT=0
if [ -d "$REPO/.git" ]; then IS_GIT=1; fi
if [ -d "$REPO" ]; then
  find "$REPO" -type f -not -path '*/.git/*' 2>/dev/null | while IFS= read -r f; do
    printf '%s  %s\n' "$(hash_of "$f")" "$f"
  done > "$REPO_INDEX"
else
  echo "   (repo dir not found: $REPO — pass it as arg 1)"
fi
echo

printf '%-34s %-12s %-28s %s\n' "FILE" "DOWNLOADED" "IN REPO (committed?)" "NOTE"
printf '%-34s %-12s %-28s %s\n' "----" "----------" "--------------------" "----"

need_dl=0; need_repo=0
printf '%s\n' "$MANIFEST" | while IFS='|' read -r H NAME RPATH KIND; do
  [ -z "${H:-}" ] && continue

  # (1) downloaded?  match by hash anywhere in downloads
  if grep -q "^$H  " "$DL_INDEX" 2>/dev/null; then DLST="yes"; else DLST="NO"; fi

  # (2) in repo?
  if [ "$KIND" = "transport" ]; then
    RST="n/a"; NOTE="patch — apply, don't commit"
  else
    match_path="$(grep "^$H  " "$REPO_INDEX" 2>/dev/null | head -1 | sed 's/^[^ ]*  //')"
    if [ -n "$match_path" ]; then
      # content is somewhere in the tree; check git status of that path
      if [ "$IS_GIT" = "1" ]; then
        rel="${match_path#$REPO/}"
        if git -C "$REPO" ls-files --error-unmatch "$rel" >/dev/null 2>&1; then
          if [ -z "$(git -C "$REPO" status --porcelain -- "$rel" 2>/dev/null)" ]; then
            RST="yes (committed)"; NOTE=""
          else
            RST="staged/dirty"; NOTE="git add + commit"
          fi
        else
          RST="present, UNTRACKED"; NOTE="git add + commit"
        fi
        # flag if it's sitting at an unexpected path
        [ "$rel" != "$RPATH" ] && NOTE="$NOTE (at $rel, expected $RPATH)"
      else
        RST="present (not a git repo)"; NOTE="init/commit"
      fi
    else
      RST="ABSENT"; NOTE="add to $RPATH"
    fi
  fi

  printf '%-34s %-12s %-28s %s\n' "$NAME" "$DLST" "$RST" "$NOTE"
done

echo
echo ">> suggested actions (run from inside the repo):"
echo "   # KAUDIT files (5): apply the patch, which creates audit/gates/KAUDIT/"
echo "   git am /path/to/KAUDIT_gate.patch    # or: git apply, then git add + commit"
echo "   # scoping note + its script (2): add manually"
echo "   mkdir -p audit/scoping"
echo "   cp /path/to/scoping_K7_candidates.md audit/scoping/"
echo "   cp /path/to/selfenergy_vertex2.py    audit/scoping/"
echo "   git add audit/scoping && git commit -m 'scoping: retire App K K.7 m_e candidates'"
rm -f "$DL_INDEX" "$REPO_INDEX"
