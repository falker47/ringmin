# Task Status

```text
task=TASK-20260905__shifted_alternating_halves
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective and scientific question

For every integer m>=2 and shift 0<=s<m, check the exact fixed-R cellwise
characterization for the shifted alternating-halves order. If it survives,
derive the full coefficient for every s/m->alpha, decide rigorously whether
alpha=0 minimizes it, and transfer any improvement to the all-integer global
limsup by deletion. The supplied alpha near 0.107 is a diagnostic, not a premise.

## In scope and expected delta

One new authoritative proof note, independent task-local checks, this dossier,
the owning fixed-order and global ledgers, roadmap and CURRENT_STATUS.md.
Retain distinct chain, fixed-order full and global quantities; audit thick
shell, both seams, both directions and all endpoint types before taking limits.

## Out of scope and protected paths

No global optimality or global-limit existence claim; no other order family,
subleading optimization or expanded finite certification. Protect paper_assets/,
results/, verify.py, src/, tests/, scripts/, README.md, REPORT.md, AGENTS.md,
PROJECT_KNOWLEDGE.md, the preceding proof note and prior dossiers. Check the
final changed-path inventory and tracked diff against this scope.

## Completion gates

- [x] exact fixed-R necessity and sufficiency for all shifts;
- [x] uniform limit including wrap cells and endpoint alpha values;
- [x] rigorous comparison with alpha=0 and deletion corollary;
- [x] independent algebraic and direct all-pairs diagnostics;
- [x] classified durable knowledge and status updated;
- [x] complete tracked/untracked review and whitespace checks;
- [x] no incidental protected or generated changes;
- [x] READY_FOR_REVIEW handoff.

## Blockers

None. Read-only Git uses a command-local safe.directory override for sandbox
ownership; no Git configuration, history or GitHub state is written.

## Handoff

The proof establishes the exact cellwise formula for every shift, the
chain/full limit functionals, the unique full-coefficient minimizer within
the shift family, and the strictly improved global limsup by deletion.
Alpha_*=0.106784760199900199... and C_shift=0.141995978127714285... are
diagnostic displays of exact implicit definitions. A separate rational
calculation certifies the 107/1000 witness interval. Both retained checker
commands exit 0; 65 finite all-pairs cases and 44 independent LP brackets
pass. Full tracked/untracked review, explicit whitespace and scope gates pass.

No global equality, normalized global limit or expanded finite certification
is inferred. Human proof review remains pending. Four tracked files and six
new files are left for manual integration, with no protected-path changes.
Suggested manual commit: `Prove optimal shifted alternating-halves upper bound`.

Exactly one proposed next atomic task: independently review this theorem's
cellwise and both-seam all-pairs proof, moving-jump limit, unique-minimum
argument, rational witness enclosure and deletion corollary; record acceptance
or precise corrections without starting another order family.
