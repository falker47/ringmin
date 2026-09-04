# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=2a3af790de73e1694cbb510245e14015f810e3b0
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__radius9_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Prove the radius-9 endpoint bridge using only n=41,42 and separator 220.
All four exact gates close:

```text
R_{9,41} < 220 < T_{9,41},
T_{9,42} < 220 < R_{9,42}.
```

**Classification: exact theorem / proved corollary.** Applying the fixed-k
theorem gives positive formal seam deficit for 11<=n<=41 and negative
deficit for every n>=42; hence s_9=42. No numerical scan or floating root
is a premise. The proof and all rational witnesses are in
`research/RADIUS9_SEAM_ONSET.md`. The remaining unresolved radius-index
range is 10<=k<4325.

### Allowed delta

- The radius-9 proof note.
- `ops/TASK-20260904__radius9_seam_onset/`: three dossier documents,
  standalone exact checker and task-local rejection tests.
- `PROJECT_KNOWLEDGE.md`, the relevant roadmap entries, and this file.

### Verification gates

- Both threshold positivity/pre-square signs and directed margins pass.
- All 33/34 cyclic edges agree between independent rank and parity
  constructions, including closure, multiplicity, degree and 134 symmetry
  variants. A separate integer scorer reconstructs every rational witness.
- Strict arcsine bounds and exact Machin identities with signed remainders
  prove both complete chain inequalities against pi.
- Isolated stdlib checker, normal and -O: exit 0, exact_bridge=PASS,
  inequalities=4, cyclic_edges=67, symmetry_variants=134.
- Task-local suite, normal and -O: 24 tests, OK, exit 0 in each mode.
- Complete tracked diff and all six untracked additions inspected. Final
  nine-file audit: exit 0, four hashes verified, zero protected changes,
  UTF-8/LF and whitespace checks passed. `git diff --check`: exit 0,
  no output. HEAD unchanged.

### Blockers and limitations

No blocker. The first candidate bound on edge (20,30) had zero square
margin; the checker rejected it. The corrected strict witness 999/10000
passes and the original candidate is retained as a rejection test.

The all-integer deduction imports the fixed-k mathematical theorem.
Local checks do not replace independent proof review; rejection tests are
coupled to the checker. Production code, global certificates, verify.py,
existing proof notes and arXiv-v1 assets remain protected. The production
test suite, global verifier and paper build were not run because these
components are unchanged and the scoped exact checks cover this delta.
Hosted CI and an external reviewer were not run/inspected in this task.

## Exactly one next atomic task after acceptance

Attempt a STRICT exact radius-10 endpoint bridge at n=45,46, seeking a
rational separator and verifying both complete edge representations and
all four chain/threshold gates. The candidate s_10=46 remains unproved;
record failure if the bridge cannot be established. This next task has
not begun.
