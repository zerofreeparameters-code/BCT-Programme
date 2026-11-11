# Gate BULK — as-run prompt and run log

## Prompt as received (the fresh-thread text printed by the apply script, with C filled in)

```
Gate BULK — run. One gate per thread; fresh thread; nothing from memory or past chats.

Before reading anything, fetch the pre-registered card to disk and hash it:

  mkdir -p /home/claude/gate_BULK && cd /home/claude/gate_BULK
  curl -sS -o gate_BULK_prompt.md https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/cec526f16281e4a66750af459d741dcfd92a6ff6/audit/gates/gate_BULK_prompt.md
  curl -sS -o bulk_dimcheck.py https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/cec526f16281e4a66750af459d741dcfd92a6ff6/audit/gates/BULK/bulk_dimcheck.py
  sha256sum gate_BULK_prompt.md bulk_dimcheck.py

Expected:
  2ffb5f092f4ed140dfc92eb035d73fd20ec30bfeddf6fc212681d39aaf2c02ec  gate_BULK_prompt.md
  41fbc4ef284dee15a23610e9b5e2fd27e6ecf000381f27b354717cf3377b4674  bulk_dimcheck.py

If either digest differs, stop and report; do not read the card. If both match, record the digests and
the commit cec526f16281e4a66750af459d741dcfd92a6ff6, read the card, and run exactly what it says
(its section 11 is the protocol; its section 4.1 pins the corpus sources at commit
9582c54b6f22fc78eee0dc356f6d49cdfadd68b3 with hashes to verify before reading). The container can
git clone over HTTPS but cannot push: deliver the result as a git format-patch bundle adding
audit/gates/BULK/. If any result file already exists under audit/gates/BULK/, do not open it.
Same-session results are capped at CONJECTURE.
```

How it actually arrived: Michel attached the whole apply script (`bct_apply_BULK.sh`, which embeds the card, the
sha record, `bulk_dimcheck.py`, and the text above with `$C` unfilled) to a fresh thread with no message. The
analyst verified the script's embedded files against its own digests, asked how to proceed, and was told
"apply, then run the gate". The pre-registration turned out to be already pushed as commit C (see log).

# Gate BULK run log (as-run)

- Run thread: Claude Fable 5.1, session https://claude.ai/code/session_01CaE3p9NntTwEURvi1JDv8G, 11 November 2026 (Australia/Melbourne).
- Pre-registration commit C = cec526f16281e4a66750af459d741dcfd92a6ff6 (author Michel Robert Cabrié, 2026-11-11 10:38:53 +1100).
- Card fetched by raw URL at C: audit/gates/gate_BULK_prompt.md
    sha256 2ffb5f092f4ed140dfc92eb035d73fd20ec30bfeddf6fc212681d39aaf2c02ec  (19849 B)  == expected
- Validation script fetched by raw URL at C: audit/gates/BULK/bulk_dimcheck.py
    sha256 41fbc4ef284dee15a23610e9b5e2fd27e6ecf000381f27b354717cf3377b4674  (1755 B)   == expected
- Disclosure: the apply script that generated commit C (containing the card text verbatim) was attached to this
  thread by Michel before the run began, so the card text was in the analyst's context before the raw-URL fetch.
  The fetched copy was hashed before being re-read; the attachment's embedded copy hashed to the same digest.
- audit/gates/BULK/ at C contains only bulk_dimcheck.py (no result file present; nothing to avoid opening).
- Pinned sources checked out in a detached worktree at 9582c54b6f22fc78eee0dc356f6d49cdfadd68b3 ("Auto-sync Zenodo DOIs", 2026-11-10 14:06:23 +0000).
- §4.1 hashes: all six files OK (sha256sum -c, record sources_9582c54.sha256); PDF 11,428,679 B; audit/gates/BUBBLE_BELLS/ present (4 files + output/ + scripts/).
- Q1 ledgers built first (AZ6, Letter 20, AZ7, Letter 27, Vol. 1 Foundations read in full or at the cited lines;
  pinned PDF extracted with `pdftotext -layout`, 426 form-feed pages; pages 14–51, 49, 58, 69–76, 120–121, 153–157,
  261–274 read; whole-volume searches for "bulk modulus", "Madelung", "M_FCC", "9√2", "ρ_BCT", "16π", "K_BCT").
- Q2 per variant second; Q3 not opened; Q4 last (`bulk_q4.py`, mpmath dps 60, 40 reported).
- Check step: both scripts re-run cold with byte-identical output; headline numbers re-derived in plain floats
  by different routes (ρ_P = m_P/ℓ_P³, SI-route κ for (ii), direct a† in SI); every ledger citation re-printed from
  the re-hashed pinned files (`output/ledger_cites.txt`).
- Finished 11:05 AEDT. Deliverable: `git format-patch` bundle adding `audit/gates/BULK/` on top of commit C.
