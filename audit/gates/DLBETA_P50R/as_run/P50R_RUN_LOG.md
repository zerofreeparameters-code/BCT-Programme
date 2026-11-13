# Gate DL-BETA P50R — run log (UTC)

- 05:00:38 Card and record fetched by commit-pinned raw URL (curl) to disk; sha256 before reading. Both match the run prompt's expected digests. Commit dcf22c72170e55613be779718a19488f726ecc9e recorded.
- 05:01 Repository cloned; `git checkout dcf22c72…`. origin/main was at the same commit. All eleven §4.1 hashes verified OK (as_run/pins_check.txt). Card read.
- 05:02 dlbpr_driver.py, dlbpr_rules.py, dlbp_analysis.py copied to a work directory outside the repository; re-hashed there (match). Toolchain: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1 present; `pip install numba==0.68.1` (llvmlite 0.50.0) — matches Gate DL-BETA's recorded toolchain.
- 05:03:35 Driver launched: `nohup python3 -I dlbpr_driver.py <repo>/audit/gates/DLBETA/run <repo>/audit/gates/DLBETA/out/series OUT 2`. K1 PASS. 136 fixed tasks submitted. Both cores ~99 %. Repository working tree clean.
- 05:14:39 First void L = 8 chains complete at 221–225 ms/sweep (budget 236).
- 05:22 Delivery path checked: `gh auth status` reports the GH_TOKEN invalid; `git push --dry-run` is refused by the git proxy ("not in this session's authorized repository set"); no `add_repo` tool exists in this session. Per the proxy README, policy denials are not retried. Delivery will be the `git format-patch` fallback (one commit adding audit/gates/DLBETA_P50R/ only, on top of dcf22c72…).
- 08:20:37 void L = 8 stage complete: 38/38 runs (30 mixed chains + 8 branch runs).
- 09:23:18 void L = 6 stage complete: 38/38 runs. Z4 L = 12 started.
- 09:47:14 Z4 L = 12 stage complete: 28/28 runs. Z4 L = 8 started.
- 09:51:22 DRIVER COMPLETE. 136 runs, 575.5 core-minutes. No bracket extension on any lattice. K2: all four within 2 % and all four bit-identical to Gate DL-BETA's stored series.
- 09:53:55 §4.7 step 1: `python3 -I dlbpr_rules.py numbers OUT` -> dlbpr_numbers.txt, analysis.json. void L = 6 integrity FAIL (hot beta 1.2450: span 0.00919 > 0.25 G = 0.00809).
- 09:54:06 §4.7 step 2: dlbpr_numbers.txt hashed -> 0b624155e579c82581f65a54ec4b5943d0bc598add1300a07cc0a6b26ca64c63; recorded in OUT/dlbpr_numbers.sha256.
- 09:54 §4.7 step 2: hash posted in the conversation with SendUserMessage, before the verdict step.
- 09:54:15 §4.7 step 3: `python3 -I dlbpr_rules.py verdict OUT <repo>/audit/gates/DLBETA_P50/OUT/analysis.json` -> VERDICT SC-DLBPR-5.
- 10:00 Independent cross-check written and run (after the verdict): CROSS-CHECK PASS.
- 10:08 Result assembled; deliverable tree built; format-patch produced (push refused by the git proxy).
