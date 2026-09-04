# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=cf78a3b5d7334d3933b62988acae0f048f7b638f
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__radius8_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Prove the radius-8 endpoint bridge at `n=37,38` with separator `176`.
All four exact gates close:

```text
R_{8,37} < 176 < T_{8,37},
T_{8,38} < 176 < R_{8,38}.
```

**Classification: exact theorem / proved corollary.** The fixed-`k`
theorem therefore gives `Delta_{8,n}>0` for `10<=n<=37` and
`Delta_{8,n}<0` for every `n>=38`, hence `s_8=38`.
The proof and complete rational witnesses are in
`research/RADIUS8_SEAM_ONSET.md`; the prior numerical diagnostic is not a
premise. The remaining unresolved radius-index range is `9<=k<4325`.

### Allowed delta

- The new radius-8 proof note.
- `ops/TASK-20260904__radius8_seam_onset/`: three dossier documents,
  standalone exact checker and task-local mutation checks.
- `PROJECT_KNOWLEDGE.md`, the relevant roadmap entries, and this file.

### Verification gates

- Exact positive sign gates before squaring and taking reciprocals at both
  endpoints; directed quadratic margins are strictly positive.
- All 30/31 cyclic edges checked through independent rank and parity
  constructions, including closure, multiplicity, degree and 122 symmetry
  variants. Exact integer/table cross-check agrees with Fraction arithmetic.
- Rational arcsine upper and lower bounds and exact Machin/remainder
  comparisons prove both complete chain inequalities against `pi`.
- Isolated stdlib checker, normal and `-O`: exit 0, `exact_bridge=PASS`.
- Task-local suite, normal and `-O`: 25 tests, `OK`, exit 0 in both modes.
- `python -B -m pytest`: exit 0; `12 passed, 1 warning in 30.49s`.
  Warning: existing pytest cache could not be written by the sandbox user.
- Complete tracked diff and all six untracked additions inspected; nine-file
  format/scope audit passes with zero protected changes and five verified
  provenance hashes. `git diff --check`: exit 0, no output. HEAD unchanged.

### Blockers and limitations

No blocker. The all-integer conclusion imports the general fixed-`k`
mathematical theorem; local tests do not replace independent proof review.
The mutation suite is coupled to the checker for rejection testing.

No full-feasibility, global-optimum, contact-graph or floating-circle claim
is made. Production code, finite certificates, the standalone global verifier
and arXiv-v1 publication assets are protected. No global verifier or paper
build was needed for this endpoint task; hosted CI was not inspected.

## Exactly one next atomic task after acceptance

Perform a bounded STRICT two-precision diagnostic for `s_9` on every integer
`37<=n<=50`, using independent rank-tour and parity-edge reconstructions.
Identify a stable adjacent crossing and rational separator if possible;
retain numerical-diagnostic status pending a separate exact endpoint proof.
This next task has not begun.
