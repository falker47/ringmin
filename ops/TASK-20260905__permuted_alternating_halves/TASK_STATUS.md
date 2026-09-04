# Task Status

```text
task=TASK-20260905__permuted_alternating_halves
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective

Prove or refute the proposed exact cell-sum full-feasibility criterion for
every m>=2, every permutation P of {m+1,...,2m}, and every R>0.

## Scientific question

Does the shifted fixed-order proof extend without any order or shift
assumption on the highs? The target was initially unresolved and is now an
exact theorem, with proof in research/PERMUTED_ALTERNATING_HALVES.md.
Bounded independent falsification preceded the proof, which treats both
directed paths for HH, LH and LL pairs, small cycles and arbitrary wraps.

## In scope and expected delta

- New authoritative research/PERMUTED_ALTERNATING_HALVES.md proof or refutation.
- One entry in knowledge/FIXED_ORDER_THEORY.md, the sole claim owner.
- research/NEXT_RESEARCH_STEPS.md, including explicit correction of the
  obsolete/ambiguous treatment of 1/8 as an open candidate.
- CURRENT_STATUS.md and this task dossier with reproducible local checks.

## Out of scope and protected paths

Optimization over permutations and new asymptotics are out of scope.
Protect paper_assets/, results/, src/, tests/, verify.py, scripts/,
publication metadata, README.md, REPORT.md, prior research notes/dossiers,
AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, PROJECT_KNOWLEDGE.md and all other
knowledge modules (including existing global bounds). No Git/GitHub writes.

## Predeclared bounded falsification

All permutations for m=2..6, lexicographic with no symmetry quotient (872).
For each: 64 float64 bisections on [1e-9,16m^2]; probe R=m^2 times
{1e-6,.01,.1,1,100}, and the cell root times {1-1e-5,1+1e-5}.
The independent all-pairs HiGHS LP uses atan2 angles, not cell constraints;
primal/dual tolerances 1e-9, witness angular guard 1e-7, and a 1e-7
exclusion band around S=2*pi. A point in the band or unexpected solver
status fails the check instead of silently deciding equality. No RNG.
Stop on the first discrepancy, preserving m, P, R and both results; this
is only a numerical candidate for a counterexample pending exact analysis.
Otherwise the result guides a proof and is not its premise. No larger
permutation search or asymptotic optimization is authorized by this check.

## Completion gates

- [x] bounded falsification completed before writing the proof;
- [x] exact proof; both directions and all wraps;
- [x] immediate fixed-order consequences only, classifications explicit;
- [x] proportionate independent algebra and angular/Cartesian checks;
- [x] durable owner, roadmap and current status updated;
- [x] full tracked/untracked review, whitespace and protected-path checks;
- [x] READY_FOR_REVIEW handoff with exactly one next atomic task.

## Blockers

None. Local HEAD equals the accepted registry baseline.

## Handoff

The criterion is true for every allowed m,P,R. Only the fixed-order
characterization, optimal gap parametrization, unique full root and
chain/full equality test were integrated. Both retained checkers exited 0;
the complete outputs and limitations are in EVIDENCE.md. The final diff
contains exactly three tracked modifications and six new allowed files.
No protected/generated path or Git/GitHub state changed.

Independent human proof review remains pending; numerical checks are
non-interval finite observations and do not expand global certification.
Suggested manual commit: Prove fixed-order feasibility for arbitrary high permutations

Exactly one next atomic task: independently review this arbitrary-permutation
criterion, both paths and wraps, small cycles and immediate corollaries;
reproduce the bounded checks and record acceptance or precise corrections.
Do not start permutation asymptotics as part of that review.
