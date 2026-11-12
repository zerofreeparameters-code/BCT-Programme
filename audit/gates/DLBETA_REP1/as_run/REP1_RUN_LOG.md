# DL-BETA REP1 run log (this session)
- 2026-11-12T23:42:03+11:00 fetched card+record from commit 6058f4e63d1ec0aadeb60ce5bb4a73e5c76b5369
- sha256 gate_DLBETA_REP1_prompt.md = 2ffa8de365a01af1cd3e372998d264d16c2327459e2ffbb5b126f08e7f39a349 (MATCH)
- sha256 PREREG_20261112_DLBETA_REP1.sha256 = fc6b6d22c98474795eb470f99ce9f19bc187f4ff61bd60a591caf1f4ffcd51b2 (MATCH)
- NOTE: directory pre-existed with files from an earlier attempt (not opened):
    CHECKPOINT_00_fetch.txt  732 bytes  mtime=2026-11-12 23:36:38.787693360 +1100
    CHECKPOINT_01_hash_verified.txt  532 bytes  mtime=2026-11-12 23:40:47.979708173 +1100
    dirs: prior_attempt_note/ sources/ (contents not listed)
- 2026-11-12T23:42:56+11:00 repo fetched depth 1 at 6058f4e; §4.1 open sources extracted by path with git show; all 8 hashes MATCH (src_rep1/HASHCHECK.txt). dlb_deskcheck.py locked (unopened).
- 2026-11-12T23:46:59+11:00 read open sources: gate_DLBETA_prompt.md, gate_CRIT2_prompt.md, gate_CRIT2_RESULT.md, gate_LATT_prompt.md, dlb_deskcheck_output.txt. Work dir W/.
- 2026-11-12T23:49:42+11:00 OWN K1 RECORDED (0 fails) and hashed BEFORE opening dlb_deskcheck.py:
    469b6ff85c1a6a0ce5c3add9955c7af6167caae7e984619581e6e91c1cc820cd  out/k1_own.txt
    139b5dc20534f18e6b2410b821303263354d3042eb5e9cbbf99baec64fbc12e1  out/k1_own.json
    560c256fe391bfa7b0a2bf4e5abc520f8179b75647ece51006b5cba82425c9e6  run/dlbr_sim.py
    7f24667b48fb0aae0fcb40c4f4853afe4d70a752ecac7ee39bde1d7bef6a29ad  run/dlbr_k1.py
- 2026-11-12T23:49:48+11:00 dlb_deskcheck.py unlocked (hash re-verified) after own K1 hash.
- 2026-11-12T23:51:51+11:00 dlb_deskcheck.py re-run: 49/49 assertions; output identical to dlb_deskcheck_output.txt except timing lines. K1 own == desk check. rerun output sha256 c27bcbb7...ccba3
- 2026-11-12T23:55:49+11:00 K2/K3/sampler: 0 fails (out/k23.txt). Code frozen before K4 (out/code_frozen_before_K4.sha256):
    560c256fe391bfa7b0a2bf4e5abc520f8179b75647ece51006b5cba82425c9e6  run/dlbr_sim.py
    2ded89b33779c3c612dbdfcbcb350fdc30584985dbc6eae251b1ae78eb7e0d45  run/dlbr_stats.py
    37a9ecfb94e1d341db96bbb6d40124c161a39c517eb08e43986cdfbd1aa6c957  run/dlbr_driver.py
    7f24667b48fb0aae0fcb40c4f4853afe4d70a752ecac7ee39bde1d7bef6a29ad  run/dlbr_k1.py
    a3dff1d8752b8edd58d2211178f984aed4db5bbbd176c58e02f0ab7111d4bd5b  run/dlbr_k23.py
    ffd2629bf250c98ad2ef7195fb94386f5613e2cc8048255457f6c2979bf4a757  out/k23.txt
    a94d8fe4acce604417a9c556497956b0a8527654893353d1820c586e117b2327  out/k23.json
- 2026-11-13T00:07:48+11:00 K4 PASS (C max 1.0075; E*_hc 0.37301). K5 PASS (flip [1.007,1.012]). Void stages started 00:06:32.
- 2026-11-13T00:47:14+11:00 S1 beta_0=1.22 interior; S2 beta_4=1.255 interior, L4 jump [1.250,1.255] hot+cold. S3 started 00:45:46.
- 2026-11-13T01:25:03+11:00 S3: L6 cold jump [1.250,1.255] fall 0.01665 (3sig 0.00491) Located; hot jump [1.260,1.265]; E*=0.32205; no extension. S4a started 01:21:57.
- 2026-11-13T01:34:35+11:00 S4a: beta_mix(6)=1.25875 flip [1.2575,1.2600] monotonic, 0 unresolved. S4b + S6 started 01:32:29.
- 2026-11-13T02:13:53+11:00 dlbr_numbers.txt written+hashed: dfafee6ca8f2cba4f7967990d500ea4daaab6c7595fe77bb48de37494c2d5646. Sealed files NOT yet opened.
- 2026-11-13T02:14:06+11:00 UNBLIND: sealed files extracted by path (after hash posted at 02:13:53).
- 2026-11-13T02:16:28+11:00 Q7 computed: I_O=[1.24875,1.25875], betaR=1.25875, d=0, Resolved yes -> SC-DLBR-1. Post-unblind observations in out/post_obs.txt.
- 2026-11-13T02:20:08+11:00 deliverable assembled in repo (branch dlbeta-rep1 on 6058f4e).
