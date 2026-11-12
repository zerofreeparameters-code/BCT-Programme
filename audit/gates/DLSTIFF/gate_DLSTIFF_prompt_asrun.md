# Gate DL-STIFF — as-run prompt

The instruction below is the verbatim text that opened the run thread on 12 November 2026
(Australia/Melbourne). It is reproduced so that the run can be replicated exactly.

The canonical card it points to is `audit/gates/gate_DLSTIFF_prompt.md` at commit
`9993a2381cdbdd8604975f285644aabb94063325`, SHA-256
`294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21` — fetched, hashed and
**verified before being read**, together with `PREREG_20261112_DLSTIFF.sha256`
(`682effc9…9cdbb696`) and `DLSTIFF/dls_deskcheck.py` (`332e2d12…5989bde5`). See
`dls_source_verification.txt` for the full transcript, including the `sha256sum -c` pass over
every §4.1 source.

---

```
Gate DL-STIFF — run. One gate per thread; fresh thread; nothing from memory or past chats.

Before reading anything, fetch the pre-registered card, its record and its validation script to disk
and hash them:

  mkdir -p /home/claude/gate_DLSTIFF && cd /home/claude/gate_DLSTIFF
  R=https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/9993a2381cdbdd8604975f285644aabb94063325
  curl -sS -o gate_DLSTIFF_prompt.md          $R/audit/gates/gate_DLSTIFF_prompt.md
  curl -sS -o PREREG_20261112_DLSTIFF.sha256  $R/audit/gates/PREREG_20261112_DLSTIFF.sha256
  curl -sS -o dls_deskcheck.py                $R/audit/gates/DLSTIFF/dls_deskcheck.py
  sha256sum gate_DLSTIFF_prompt.md PREREG_20261112_DLSTIFF.sha256 dls_deskcheck.py

Expected:
  294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21  gate_DLSTIFF_prompt.md
  682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696  PREREG_20261112_DLSTIFF.sha256
  332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5  dls_deskcheck.py

If any digest differs, stop and report; do not read the card. If all three match, record the digests
and the commit 9993a2381cdbdd8604975f285644aabb94063325, read the card, and run exactly what it says (its
section 11 is the protocol; its section 4.1 pins the other sources at commit
9114b6e8da4032f944d141995a0a2baafaf38bce with hashes to verify before reading). The container can
git clone over HTTPS but cannot push: deliver the result as a git format-patch bundle adding
audit/gates/DLSTIFF/ only, on top of 9993a2381cdbdd8604975f285644aabb94063325. If any result file already exists under
audit/gates/DLSTIFF/, do not open it. Same-session results are capped at CONJECTURE.
```

---

## Run record

- **Thread:** fresh, inside the BCT Project. One gate.
- **Model:** the thread opened under Claude Fable 5.1, which performed the fetch, the digest
  verification, the clone, the §4.1 hash check and the reading of the eleven pinned sources. It
  switched to Claude Opus 5 before any kill test was computed; Opus 5 wrote and ran the four scripts
  and this deliverable. Recorded because a replication would want to know.
- **Deviations from the card's §11 protocol:** none. The two settings §11 names ("Search and
  reference past chats", "Generate memory from chats") are the user's to toggle; this run consulted
  neither facility and nothing from either reached it, which is recorded in the result's
  contamination statement rather than claimed as a verified setting state.
- **`audit/gates/DLSTIFF/` on arrival:** one file, `dls_deskcheck.py`. No result file existed, so
  none was opened.
- **Delivered as:** a `git format-patch` bundle on top of `9993a238…`, adding
  `audit/gates/DLSTIFF/` only.
