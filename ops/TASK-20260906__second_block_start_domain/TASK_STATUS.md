# Task Status

```text
task=TASK-20260906__second_block_start_domain
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-06
updated_at=2026-09-06
```

## Objective

Resolve the sign of D_u on lambda<u, 0<epsilon<A/3-u, with exactly
alpha=alpha_hat, A=1+alpha_hat and lambda=A*x_* fixed. Retain the full
max, every applicable switch endpoint, and continuity at u=lambda;
deduce the precise boundary reduction if the sign is global.

## Scientific question and scope

The proposed exact discriminator is the translated derivative: the
removed diagonal is chord, both reflected-branch contributions are
nonnegative, and the first half of every positive-width block supplies
a strict contribution. Prove regularity when the switch enters through
the upper endpoint, rather than assuming the clipped switch is smooth.

## Expected delta

Eight paths: a new canonical domain proof; this three-file STRICT
dossier and its minimal rational checker; the single owning fixed-order
ledger; CURRENT_STATUS.md; research/NEXT_RESEARCH_STEPS.md.

## Protected paths potentially affected

All existing proof notes and earlier dossiers, other knowledge ledgers,
PROJECT_KNOWLEDGE.md, AGENTS.md, RINGMIN_REVIEW_PROTOCOL.md, paper_assets/,
results/, src/, tests/, scripts/, verify.py, README.md, REPORT.md and
publication metadata. Inspect the final path set against HEAD.
The task's input image remains untracked and outside the commit.

No optimization of boundary width, finite permutation construction,
R_full transfer or R*(n) bound belongs to this task.

## Completion gates

- [x] Full-max domain proof and all switch endpoints.
- [x] Continuity, strict boundary dominance and equality of infima.
- [x] Minimal exact checker and independent bounded diagnostics.
- [x] Proof, single owner, roadmap and dossier synchronized.
- [x] Full tracked/untracked source and protection audit.
- [x] READY_FOR_REVIEW source prepared for authorized integration.

## Blockers

None. The exact baseline minimizers and their coarse rational brackets
are imported; the width minimum is not a dependency of this extension.

## Handoff

The [canonical proof](../../research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md)
establishes D_u>=epsilon^3/[48*(A+u+epsilon)^2]>0 throughout the requested
domain, with C^1 matching at entry. The actual touching-block coupling
extends continuously to u=lambda. Every interior pair is strictly
dominated at the same width, and both directions of the infimum equality
are proved. Width attainment, location and uniqueness remain undetermined.

Both the new minimal checker and previous local checker exit 0.
Independent 70-digit diagnostics pass 54 identities, 54 central
differences with regime-appropriate tolerances, positive lower bounds,
strict boundary comparisons and switch/boundary limits. The source audit
passes all eight paths, explicit untracked whitespace, five proof links,
one owning ledger and sixteen unchanged protected texts. EVIDENCE.md
records exact commands, complete diagnostic/audit sources and hashes.

Under the standing authorization, stage only the eight inspected paths,
inspect the cached diff, commit, push normally to origin/main and verify
the remote result. The containing commit and final handoff identify the
integrated SHA. The user-supplied image remains untracked. Integration
does not constitute independent mathematical acceptance.

Exactly one next atomic task: independently review the domain sign
theorem, switch regularity and boundary reduction, and record acceptance
or corrections without optimizing the boundary width.
