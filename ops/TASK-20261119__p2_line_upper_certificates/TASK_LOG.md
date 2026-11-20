# Task log

## 2026-11-19 — Startup

Verified base 7d257221d9034ca5f895f062e45e782d8e77b6c2 against the remote branch. The original checkout contains the pre-existing untracked arXiv ZIP. Created a clean sibling worktree. Sandbox DNS failed for arXiv. Authorized HTTPS reads returned the specified archive digests, and an isolated shallow clone supplied the exact quadratic reference revision. The reference sources are read-only.

## 2026-11-19 — Search protocol

For powers 1 and 2 run two seeded greedy-swap attempts per rung. Start from alternating, shifted and reflected words with sampled cuts. Retain the best complete recurrence span. For n >= 200 use cumulative budgets starting at 4096, then double until improvement is below 1e-6 in the normalized objective, with 262144 as a safety cap. For finite-reference controls use 1024 proposals. Certify the winning word independently of its float score.

## 2026-11-20 — Search extension and independent arithmetic

The first 262144-proposal cap arrived before the requested improvement threshold on 19 of the 20 ladder attempts. Extended those runs by resumed doubling with deterministic short-range sweeps. Every final doubling now gains less than 0.000001. Across both profiles and controls the search schedules count 14438400 proposals. Separate 12000-proposal reference runs reproduce scores near 0.14147.

Generated 20 exact placements. The independent standard-library verifier accepted 13634050 unordered pairs. The two unrelated integral implementations enclosed the rational four-block cost, including all branch switches. A separate endpoint-perturbation argument bounds the implicit published coefficient.

## 2026-11-20 — Verification and corrections

The finite-reference report initially stopped because the quadratic table escapes spaces after commas in TeX. Normalized that escape, then checked all nine applicable comparisons. The first three-pass preview had a 14.01495 pt overfull line. The scientific notation for its denominator cleared it. A subsequent three-pass build had one page and zero warnings of the checked types. The first file-write attempt for the section ended before any write when the transport interpreted a TeX quotation delimiter. The corrected section was read back and compiled.

The original global bracket verifier returned PASS_GLOBAL_BRACKETS. The final unit suite passed 82 tests and four subtests. A fresh search and certificate generation gave byte-identical files for every rung. Prepared the scoped local commit for independent review.
