# Task Status

```text
task=TASK-20260804__fixed_k_supnick_seam
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove the general fixed-radius Supnick seam theorem for every integer
`k>=1`: derive the exact threshold domain and formula, prove eventual and
persistent obstruction, and recover the existing `k=1,2` results without
classifying the exact `k=3` onset.

## Scientific question

For the chain-minimizing Supnick cycle `sigma*_{k,n}` on `{k,...,n}`, with
fixed integers `k>=1`, `n>=k+2`, and

```text
R_{k,n} = R_chain(sigma*_{k,n}),
```

determine the exact structural behavior of

```text
Delta_{k,n}
  = theta_{R_{k,n}}(n,k) + theta_{R_{k,n}}(k,n-1)
    - theta_{R_{k,n}}(n,n-1),
```

including the physical Descartes-threshold domain, uniqueness of a possible
equality, and persistence after the first strict crossing. The incoming
general statement is conjectural; only the exact `k=1,2` theorems are already
proved in the durable notes.

## In scope

- `research/FIXED_K_SUPNICK_SEAM.md`;
- this task dossier and one production-independent diagnostic checker;
- `CURRENT_STATUS.md`;
- `PROJECT_KNOWLEDGE.md` and `research/NEXT_RESEARCH_STEPS.md` only after a
  complete exact theorem survives independent review and verification.

## Out of scope

- an exact onset classification for `k=3` or any formula for `s_k`;
- claims about `R*(n)`, fixed-order full feasibility beyond this seam, or
  floating circles in global optima;
- production code, tests, certificates, `verify.py`, paper/publication assets,
  generated results, README, and report changes.

## Expected delta

Add one authoritative proof note, this dossier, and one self-contained finite
checker. Replace the live status entry and conditionally update compact
knowledge and the ranked roadmap only after the theorem is complete.

## Protected paths potentially affected

The following paths must remain byte-for-byte unchanged and will be audited:

- `paper_assets/`, including the public arXiv-v1 source and generated assets;
- `src/`, `tests/`, `scripts/`, `results/`, and `verify.py`;
- `README.md`, `REPORT.md`, `.github/`, dependencies, publication metadata,
  and the existing radius-1/radius-2 proof notes and dossiers.

## Completion gates

- [x] canonical shifted Supnick order and seam neighbors derived;
- [x] chain-root existence, uniqueness, strict growth, and divergence proved;
- [x] Descartes sign equivalence and exact `n>=4k+1` domain proved;
- [x] explicit physical `kappa_{k,n}` and decreasing `T_{k,n}` proved;
- [x] eventual obstruction, possible-equality uniqueness, and persistence
  proved without raw-deficit monotonicity;
- [x] existing `k=1,2` classifications recovered from their exact bridges;
- [x] no exact `k=3` onset or global-optimum/floating claim made;
- [x] independent checker run normally and under `python -O`;
- [x] production convention compared read-only;
- [x] relevant regression tests passed;
- [x] three independent proof/checker reviews closed;
- [x] durable memory synchronized;
- [x] complete tracked and untracked delta inspected;
- [x] `git diff --check` and direct whitespace checks passed;
- [x] no incidental protected or generated file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The exact theorem, task-local checker, broad and optimized diagnostics,
production convention comparison, regression suite, three independent
reviews, durable-memory synchronization, and complete delta/protected-path
audit all pass. Manual review and commit remain with the user.

Exactly one proposed next atomic task after acceptance: prove or refute the
exact radius-3 onset by supplying rigorous endpoint bridges around the first
crossing, without revisiting the general persistence theorem.
