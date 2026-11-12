# Gate DL-STIFF — REP2 — replication prompt as received

Received in a fresh Claude thread (attached to the BCT Project) on Thu 12 Nov 2026, 18:09 AEDT.
Executed by Claude Opus 5.5 (`claude-opus-5-5`). Text below is verbatim.

---

Gate DL-STIFF — BLIND REPLICATION. One gate per thread; fresh thread; nothing from memory, past chats or the Project's knowledge base.

This gate has been run once before. You are not told that run's result. Do not look for it, and do not compare against it; comparison happens later, elsewhere.

1. Before reading anything, fetch the card, its record and its validation script to disk and hash them:

  mkdir -p /home/claude/gate_DLSTIFF_rep && cd /home/claude/gate_DLSTIFF_rep
  R=https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/9993a2381cdbdd8604975f285644aabb94063325
  curl -sS -o gate_DLSTIFF_prompt.md          $R/audit/gates/gate_DLSTIFF_prompt.md
  curl -sS -o PREREG_20261112_DLSTIFF.sha256  $R/audit/gates/PREREG_20261112_DLSTIFF.sha256
  curl -sS -o dls_deskcheck.py                $R/audit/gates/DLSTIFF/dls_deskcheck.py
  sha256sum gate_DLSTIFF_prompt.md PREREG_20261112_DLSTIFF.sha256 dls_deskcheck.py

Expected:
  294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21  gate_DLSTIFF_prompt.md
  682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696  PREREG_20261112_DLSTIFF.sha256
  332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5  dls_deskcheck.py

If any digest differs, stop and report; do not read the card.

2. Get the sources as ONE commit with no later history. Do not git clone the full repository, and do not fetch any other commit, branch or tag:

  mkdir repo && cd repo && git init -q
  git remote add origin https://github.com/zerofreeparameters-code/BCT-Programme.git
  git fetch -q --depth 1 origin 9993a2381cdbdd8604975f285644aabb94063325
  git checkout -q FETCH_HEAD
  git log --oneline | wc -l          # must print 1; if not, stop and report

This is a shallow checkout, so HEAD~1 is not available; the card's §4.1 hashes are what establish the sources.

3. Read ONLY these: the card, the record, dls_deskcheck.py, and the eleven files §4.1 pins (verify every hash before reading any of them). Nothing else from the repository, the Project, past chats or memory. If a pinned source points to an unpinned file, record the pointer and do not follow it. If any file under audit/gates/DLSTIFF/ other than dls_deskcheck.py is present, do not open it; report it.

4. Run exactly what the card says (§11 is the protocol). Record the model you are running as.

5. Deliverable: as card §11, but under audit/gates/DLSTIFF/REP2/ — gate_DLSTIFF_RESULT.md, scripts, a copy of this prompt. The container can commit but not push: deliver a git format-patch bundle adding audit/gates/DLSTIFF/REP2/ only, on top of 9993a2381cdbdd8604975f285644aabb94063325. Same-session results are capped at CONJECTURE.

Delivery: when the patch is ready, also upload it to my Google Drive with link sharing on, and give me one Terminal block that downloads it with curl, checks its SHA-256, and only then runs git am in ~/BCT-Programme and git push.
