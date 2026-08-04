# Task Status

```text
task=TASK-20260804__radius1_seam_obstruction
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Prove or refute, for every integer `n >= 8`, the radius-1 seam inequality for the chain-optimal Supnick tour, or reduce it rigorously to one explicit missing lemma.

## Scientific question

For the Supnick cyclic order `sigma_n*` on `{1,...,n}` and its chain root

```text
R_n = R_chain(sigma_n*),
```

determine whether

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

holds for every integer `n >= 8`. The incoming status is conjectural beyond the finite range reported in arXiv v1.

## In scope

- `research/RADIUS1_SEAM_OBSTRUCTION.md`;
- a deterministic, production-independent diagnostic checker in this dossier;
- this dossier;
- `CURRENT_STATUS.md`;
- `PROJECT_KNOWLEDGE.md` and `research/NEXT_RESEARCH_STEPS.md` only if a stable conclusion is established.

## Out of scope

- any claim about `R*(n)` or a global optimum;
- any universal claim about floating circles or the full cascade;
- generalization to seam radius `k > 1`;
- production solver, verifier, certificate, frontier, heuristic, paper, README, or generated-asset changes.

## Expected delta

Add one authoritative proof note, this task dossier, and one self-contained high-precision checker. Replace the live current-status entry. Update compact knowledge and the ranked roadmap only if the all-`n` statement is proved or refuted. Do not modify production or publication paths.

## Protected paths potentially affected

The following paths must remain byte-for-byte unchanged and will be audited:

- `paper_assets/`, including the public arXiv-v1 source and generated assets;
- `src/`, `tests/`, `scripts/`, `results/`, and `verify.py`;
- `README.md`, `REPORT.md`, `.github/`, dependencies, and publication metadata.

## Completion gates

- [x] exact Supnick convention and the neighbors of radius `1` proved;
- [x] implicit chain-root dependence on `n` derived;
- [x] threshold cases below and at `n=8` handled by exact bounds;
- [x] all-`n` argument proved;
- [x] counterexamples and failed approaches recorded;
- [x] independent diagnostic checker and precision-stability checks run;
- [x] `python -m pytest` passed;
- [x] claims classified correctly and durable memory synchronized;
- [x] `git status --short` and complete diff inspected;
- [x] untracked additions inspected directly and checked for whitespace;
- [x] `git diff --check` passed;
- [x] no incidental protected or generated file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The Priority 1 inequality is proved for every integer `n>=8`, with the reverse inequality proved for `3<=n<=7`. The proof, exact task-local checks, high-precision diagnostics, production convention comparison, regression suite, and complete delta audit all pass. Manual review and commit remain with the user.

Exactly one next atomic task after acceptance: prove or refute the radius-2 seam inequality on the Supnick tour over `{2,...,n}` for every `n>=13`, with the exact lower-side threshold classified.
