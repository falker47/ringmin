# Task Status

```text
task=TASK-20260904__supnick_feasibility_classification
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute full feasibility at the Supnick chain root iff Delta>=0
for every integer k>=1,n>=k+2, then classify that entire fixed-order domain.

## Scientific question and expected delta

Generalize the triangle defect and path lemmas beyond n=4k+5; cover both
arcs, adjacent complements, N=3, N=4 and equality. Necessity must force
every adjacent gap from closure before ruling out the seam complement.
The result is an exact theorem and its fixed-order classification corollary,
subject to independent proof review. No integer equality case occurs.

## In scope

- research/SUPNICK_FULL_FEASIBILITY.md: authoritative proof and classification.
- This dossier: independent exact audit and separate bounded falsification check.
- PROJECT_KNOWLEDGE.md, CURRENT_STATUS.md, research/NEXT_RESEARCH_STEPS.md.

## Protected paths and out of scope

AGENTS.md; src/; tests/; verify.py; results/; paper_assets/; README.md;
REPORT.md; generation scripts; dependencies; all other proof notes and
prior dossiers. Check the exact changed-file set and unchanged HEAD.
No inference about global optima or floating circles, no factorial search,
no Git-history/index or GitHub writes, and no publication regeneration.

## Completion gates

- [x] Complete analytic equivalence and strict integer classification.
- [x] Exact identity and small-cycle checks, with rejection gates.
- [x] Bounded numerical falsification check, separate from the proof.
- [x] Durable knowledge, roadmap and current status updated.
- [x] Full tracked diff and untracked contents reviewed; whitespace checked.
- [x] Protected paths and HEAD unchanged; READY_FOR_REVIEW handoff.

## Blockers

None. Independent human proof review and manual integration remain pending.

## Handoff

Exact audit normal/optimized: exit 0, 9 identities, 32 cycles, 2964 directed
paths and 82 rejection gates. Finite diagnostic: exit 0, 106 cases and no
counterexample. All detailed commands, limitations and hashes are in EVIDENCE.md.
The proof depends on the explicitly cited exact sign theorems; independent
human review and manual integration remain outstanding.

Suggested manual commit: `Prove complete Supnick fixed-order feasibility criterion`.

Exactly one proposed next atomic task: independently
review the complete fixed-order equivalence and its imported sign dependencies.
