# Gate DL-BETA P50 — run log (UTC)

- 2026-11-12 23:31 — Scheduled-task session started (fresh cloud session). Card and PREREG record fetched by
  commit-pinned raw URL with curl to disk and hashed before reading:
  card 50525acce2f167ee78536c519562f6ea09d8aaa1768d524b2e6aaa1b483cfb9e (match);
  record fdb993a5b0b5255426ac27096ec1dffc8c28914a73c0606b0fd958d237e88b53 (match); record content = card digest (match).
  Commit 26c91c99608a2742d7cbf8dafdec6193c7831926.
- 23:31 — Repository: the session's clone was already at 26c91c99…; `git fetch --depth 1 origin <commit>` returned the
  same SHA; `git diff HEAD FETCH_HEAD` empty. All ten §4.1 hashes verified (pins.sha256: all OK).
- 23:32 — Read the card, then dlbp_driver.py, dlbp_analysis.py, dlbr_sim.py (card-vs-code check, see RESULT §CN).
- 23:32 — `pip install numba scipy` → numba 0.68.1, llvmlite 0.50.0 (SciPy 1.18.1, NumPy 2.5.3, Python 3.13.18 already
  present). 2 cores (Intel Xeon @ 2.10GHz), 7 GB RAM.
- 23:33 — Copied the two pinned files to work/ (hashes re-verified) and launched
  `nohup python3 -I dlbp_driver.py <repo>/audit/gates/DLBETA_REP1/run <repo>/audit/gates/DLBETA_REP1/out/series OUT 2`.
  K1 PASS. 136 fixed tasks submitted.
- 23:35 — Seed audit: none of the 212 P50 seeds (fixed + every possible extension) coincides with any of REP1's 410
  gate seeds (K2 re-uses REP1's four K3 seeds on purpose).
- 02:05 — void L = 8: all 30 mixed chains done (≈ 200–212 ms/sweep, faster than REP1's 255). Branch runs started 02:05.
- 02:32 — void L = 8 complete (8 branch runs + 30 chains). void L = 6 started.
- 03:28 — void L = 6 complete (8 branch + 30 chains, ≈ 63 ms/sweep). Z4 L = 12 started.
- 03:35–03:53 — Z4 L = 12, Z4 L = 8, then K2 (REP1's four K3 runs, REP1 seeds): all K2 pass.
- 03:53:03 — DRIVER COMPLETE. No bracket extension was triggered on any lattice (state.json ext = {} for all four).
  136 runs, 518.9 core-minutes, wall 4 h 19 min on 2 cores.
- 03:54:15–03:54:38 — `dlbp_analysis.py numbers OUT` → dlbp_numbers.txt, analysis.json. SHA-256 of dlbp_numbers.txt
  810450ce0a940ee195fbdf87713ed114ac400f2602fb5fc0010ceed3080bf31f written to OUT/dlbp_numbers.sha256 (03:54:38Z).
- 03:54:4x — hash posted to the user with SendUserMessage (posted_at recorded 03:54:45Z). Then
  `dlbp_analysis.py verdict OUT` (03:54:49Z): VERDICT SC-DLBP-1.
- 03:55 — Diagnosis: the driver's K2 "bit-identical: no" for the two Z4 series is a NaN artefact (Z4's E_t column is
  NaN; np.array_equal treats NaN != NaN). Byte comparison: all four K2 series identical to REP1's.
- 03:55–03:57 — CN-DLBP-01 (card §6): one-line fix (uint64 view) in dlbp_driver_CN01.py
  (29e7e175… → 9f26b6fc…); first-pass state/analysis/numbers/verdict/logs and the four K2 records+series preserved in
  OUT/superseded_CN01/; re-ran only the four K2 chains (series byte-identical to the first pass); K2 now reports
  bit-identical = yes for all four. numbers re-run: diff vs the first file = the two Z4 K2 lines only; analysis.json
  byte-identical. New SHA-256 3e033974730cbeaf9fa963bbc5e72af2ff270559bbe56688593e0ff0698b2d5b (03:57:04Z), posted
  (posted_at 03:57:16Z), then verdict re-run: SC-DLBP-1, verdict.txt byte-identical to the first.
- 03:58–04:05 — dlbp_report.py (tables, formatting only) and dlbp_crosscheck.py (independent recomputation from the
  raw series with different routines; verification only): CROSS-CHECK PASS.
- 04:01 — gate_DLBETA_P50_RESULT.md assembled (narrative + OUT/tables.md); MANIFEST.sha256 written; one commit
  adding audit/gates/DLBETA_P50/ only prepared on top of main (= 26c91c99…, unchanged since the card's commit) for
  push to main (delivery outcome reported in the conversation).
