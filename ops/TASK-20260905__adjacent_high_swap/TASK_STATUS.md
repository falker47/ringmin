# Task Status

```text
task=TASK-20260905__adjacent_high_swap
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective and scientific question

Derive the exact local variation of S_P(R) under adjacent high swaps for
all m>=2 and R>0, and resolve bounded, falsifiable exchange candidates
before proving any universal sign rule. Preserve a minimal robust
counterexample to failed rearrangement rules. Do not begin general
permutation asymptotics.

## In scope and expected delta

- research/PERMUTED_HALVES_ADJACENT_SWAP.md: authoritative local result.
- knowledge/FIXED_ORDER_THEORY.md: single owning ledger entry.
- research/NEXT_RESEARCH_STEPS.md and CURRENT_STATUS.md.
- This dossier, with deterministic falsification and independent checks.

## Protected paths potentially affected

All other paths, especially research/PERMUTED_ALTERNATING_HALVES.md,
paper_assets/, results/, src/, tests/, scripts/, verify.py, publication
metadata, README.md, REPORT.md, prior dossiers, AGENTS.md,
RINGMIN_REVIEW_PROTOCOL.md, PROJECT_KNOWLEDGE.md and other knowledge
modules. Check an explicit changed-path whitelist and empty staged diff.
No production or certification algorithm is changed.

## Predeclared bounded falsification

Enumerate every permutation for m=2..6, every cyclic adjacent swap with
the first high smaller than the second, at R in {1/10,1,2,5,10,100}.
Use deterministic float64 direct cell sums, guard 1e-10; ambiguous signs
are undecided, never proofs of equality. Stop after this finite domain.
Retain the first lexicographic robust witness, ordered by m, P, R, j,
against: (a) the chain-only sign, (b) the chord-only sign, (c) coordinate
ordering of both external lows/highs, and (d) cyclic-shift optimality at
fixed R. Also probe increasing differences of the cell cost in low/high
coordinates over the same finite ranges. No RNG or symmetry quotient.
These are numerical discriminators, not global certificates. Recheck
retained witnesses independently and prove exact signs when practical.

## Completion gates

- [x] bounded falsification before universal exchange proof;
- [x] exact changed cells, small cycles, seams and branch domains;
- [x] exact nontrivial exchange condition or precise negative conclusion;
- [x] independent verification and robust counterexample;
- [x] owning memory, roadmap and task evidence updated;
- [x] tracked/untracked full review, whitespace and protected-path audit;
- [x] READY_FOR_REVIEW handoff with exactly one next atomic task.

## Blockers and handoff

No blocker. The exact proof, conditional rule, small-R reduction and minimal
counterexample are complete. Both bounded scripts exited 0; the second
includes exact rational/symbolic checks and 30228 independent atan swap
comparisons. Three tracked files and six new files comprise the authorized
delta. Complete content, whitespace, source hashes, empty staged diff and
protected-path checks passed; see EVIDENCE.md for exact scope/results.

Independent human proof review remains pending. Local necessary conditions
do not prove local minima global; neither the small-R structure nor fixed-R
shift comparisons were transferred to general closure radii. No production
or publication change, expanded certificate, or hosted CI claim was made.

Suggested manual commit: Prove local high-swap variation and conditional exchange

Exactly one next atomic task: independently review this adjacent-high-swap
theorem, its fixed-order dependency, threshold branches, conditional signs,
small-R reduction and minimal counterexample; reproduce the bounded checks
and record acceptance or precise corrections. Do not start general
permutation/asymptotic optimization in that review.
