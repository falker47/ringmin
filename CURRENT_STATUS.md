# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=4fc2bae962fb534f8758bab930a0863e3006bff7
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__radius10_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Prove or refute the exact radius-10 bridge using only n=45,46 and R=270.
All four gates close:

```text
R_{10,45} < 270 < T_{10,45},
T_{10,46} < 270 < R_{10,46}.
```

**Classification: exact theorem / proved corollary.** The fixed-k theorem
then gives positive formal seam deficit for 12<=n<=45 and negative deficit
for every n>=46; hence s_10=46, with no equality case. The proof and all
73 rational witnesses are in `research/RADIUS10_SEAM_ONSET.md`.
No scan, floating root or reviewer pre-check is a premise. The remaining
unresolved radius-index range is 11<=k<4325.

### Allowed delta

- The radius-10 proof note.
- `ops/TASK-20260904__radius10_seam_onset/`: three dossier documents,
  exact checker, separate integer scorer, and task-local rejection tests.
- `PROJECT_KNOWLEDGE.md`, the relevant roadmap entries, and this file.

### Verification gates

- Complete rank-tour/parity-edge agreement: 36/37 edges, closure,
  multiplicity, degree and 146 rotations/reflections.
- Both threshold positivity/pre-square signs and directed margins pass.
- All 73 strict sine witnesses and both complete sums pass exact analytic
  arcsine and pi bounds, including tangent branches and signed remainders.
- Isolated stdlib checker, normal/-O: exit 0, exact_bridge=PASS,
  inequalities=4, cyclic_edges=73, symmetry_variants=146.
- Separate integer scorer, normal/-O: exit 0, 73 witnesses reconstructed,
  complete note tables/tours and threshold cross-products pass.
- Rejection suite, normal/-O: 28 tests, OK, exit 0 in each mode.
- `python -m pytest`: exit 0, `12 passed in 27.86s`.
- Complete tracked diff and all seven untracked additions inspected;
  ten-file scope/UTF-8/LF/whitespace audit and five source hashes checked.
  `git diff --check`: exit 0, no output. HEAD unchanged.

### Blockers and limitations

No blocker or failed mathematical gate. The all-integer deduction imports
`research/FIXED_K_SUPNICK_SEAM.md`; finite checks do not reprove that theorem
or replace independent proof review. Rejection tests are checker-coupled;
the separate integer scorer executes no checker code.

Global certification remains 3<=n<=14. Production code, tests, verify.py,
results, prior notes/dossiers and arXiv-v1 assets are unchanged. The global
verifier and paper build were not run because those components are protected
and unchanged. Hosted CI and an external reviewer were not run/inspected.

## Exactly one next atomic task after acceptance

Attempt a STRICT exact radius-11 endpoint bridge at n=49,50, seeking a
rational separator and checking both complete cycle representations and
all four chain/threshold gates. The candidate s_11=50 is unproved; record
failure without promotion if a gate cannot close. This task has not begun.
