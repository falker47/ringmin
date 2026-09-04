# Task Status

```text
task=TASK-20260904__induced_subset_asymptotic_bound
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Verify the induced-subset lower bound and decide whether the exact
R_{k,4k+5}/k^2 limit disproves the n^2/8 global asymptotic, including
the passage from this subsequence to all integers.

## Scientific question and expected delta

For every n>=3 in the full all-pairs Ringmin model, prove or refute
liminf R*(n)/n^2>=rho/16>3/22>1/8. Record an authoritative proof and
the resulting epistemic status. This task supplies an analytic theorem,
not a new finite global certificate.

## In scope

- research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md: self-contained deduction.
- PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, research/NEXT_RESEARCH_STEPS.md.
- README.md: minimal correction of current mathematical scope.
- This dossier and its task-local exact arithmetic audit.

## Out of scope and protected paths

AGENTS.md; all existing proof notes except the roadmap; all prior dossiers;
paper_assets/; results/; verify.py; src/; tests/; scripts/; REPORT.md;
publication metadata, dependencies and build files. No enumeration,
production pruning change, global certificate, paper build, Git index/history
or GitHub write. Full-feasibility classification is inspected as context,
not re-proved or required for the main lower bound.

## Completion gates

- [x] Exact deletion, order relaxation, asymptotic and liminf reasoning.
- [x] Separate theorem, corollary, disproved claim and unresolved claims.
- [x] Proportionate arithmetic verification and dependency audit.
- [x] Durable memory and public scope corrected.
- [x] Full tracked diff and all additions inspected; whitespace checked.
- [x] HEAD/index and protected paths unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. Independent human proof review and manual integration remain pending.

## Handoff

All four requested implications are valid. The analytic lower bound
disproves both the n^2/8 leading term and the O(sqrt(n)) deficit. Existing
asymptotic audit: 68 gates, exit 0. New exact rational audit: signed
remainders, margins and four symbolic residues, exit 0. Constant-only
80-digit sanity: exit 0. Nine-file scope/format audit and git diff --check:
exit 0. Details and limitations are in EVIDENCE.md.

No sharp coefficient, matching upper bound, explicit eventual threshold,
floating behavior or new certificate is established. Human proof review
and manual integration remain pending.

Suggested manual commit: `Prove induced-subset bound refuting n^2/8 asymptotic`.

Exactly one proposed next atomic task:
independently review the induced-subset theorem, its Supnick/asymptotic
dependencies, and the all-integer liminf deduction; record acceptance or
precise corrections.
