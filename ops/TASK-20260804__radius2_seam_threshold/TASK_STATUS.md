# Task Status

```text
task=TASK-20260804__radius2_seam_threshold
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove or refute the exact radius-2 Supnick seam classification on
`{2,...,n}`: positive deficit for `4 <= n <= 12` and negative deficit for
every integer `n >= 13`.

## Scientific question

For the chain-minimizing Supnick cycle `sigma*_{2,n}` on `{2,...,n}` and

```text
R_{2,n} = R_chain(sigma*_{2,n}),
```

classify the sign of

```text
Delta_{2,n} = theta_{R_{2,n}}(n,2)
              + theta_{R_{2,n}}(2,n-1)
              - theta_{R_{2,n}}(n,n-1)
```

for every integer `n >= 4`. The incoming all-`n` classification is
conjectural; only the finite onset at `n=13` is reported in arXiv v1.

## In scope

- `research/RADIUS2_SEAM_THRESHOLD.md`;
- this task dossier and a production-independent finite diagnostic checker;
- `CURRENT_STATUS.md`;
- `PROJECT_KNOWLEDGE.md` and `research/NEXT_RESEARCH_STEPS.md` only if a
  stable proof or refutation is obtained.

## Out of scope

- claims about `R*(n)`, fixed-order full feasibility beyond this seam, or
  floating circles in global optima;
- radius-`k` generalization for `k >= 3`;
- production code, tests, certificates, `verify.py`, publication assets,
  README/report, and generated artifacts.

## Expected delta

Add one authoritative proof note, this dossier, and one self-contained finite
checker. Replace the live current-status entry and conditionally update compact
knowledge and the ranked roadmap after the theorem is established.

## Protected paths potentially affected

The following paths must remain byte-for-byte unchanged and will be audited:

- `paper_assets/`, including the public arXiv-v1 source and generated assets;
- `src/`, `tests/`, `scripts/`, `results/`, and `verify.py`;
- `README.md`, `REPORT.md`, `.github/`, dependencies, and publication metadata.

## Completion gates

- [x] exact shifted Supnick convention, edges, and closure sums proved;
- [x] implicit chain-root existence, uniqueness, and monotonicity proved;
- [x] radius-2 Descartes threshold, domain, and monotonicity proved;
- [x] `n=12,13` and all earlier threshold-domain cases handled exactly;
- [x] proposed all-`n` classification proved or refuted;
- [x] raw-deficit monotonicity is neither assumed nor silently used;
- [x] independent finite checker run normally and under `python -O`;
- [x] production Supnick helpers compared without modifying them;
- [x] relevant regression tests passed;
- [x] claims classified correctly and durable memory synchronized;
- [x] complete tracked and untracked delta inspected;
- [x] `git diff --check` and direct whitespace checks passed;
- [x] no incidental protected or generated file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The proposed classification is proved exactly. The proof, task-local
independent checker, optimized-mode run, production-helper comparison,
regression suite, three adversarial reviews, durable-memory synchronization,
and complete delta audit all pass. Manual review and commit remain with the
user.

Exactly one next atomic task after acceptance: prove or refute the radius-3
seam classification on `{3,...,n}`, with proposed onset `n=17`, including the
physical Descartes-threshold domain and exact bounds on both sides.
