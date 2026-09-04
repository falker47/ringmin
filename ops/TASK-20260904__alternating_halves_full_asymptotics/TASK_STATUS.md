# Task Status

```text
task=TASK-20260904__alternating_halves_full_asymptotics
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Determine rigorously the chain and fixed-order full leading asymptotics for

```text
sigma_{2m}=(1,m+1,2,m+2,...,m,2m),
```

including an explicit all-pairs gap construction, a matching leading lower
obstruction, the alternating low-radius valleys and the cyclic seam, and only
the global consequence justified by deletion monotonicity.

## Scientific question

For integer `m->infinity`, determine whether

```text
R_full(sigma_{2m})/(2m)^2
```

has a limit strictly below `1/(2*pi)`, without importing finite numerical
values into the proof. Keep `R_chain(sigma_{2m})`, the fixed-order full value,
and `R*(n)` separate. If the even-order theorem yields a global even-subsequence
upper bound, decide rigorously whether deletion transfers the same `limsup`
coefficient to every integer `n`.

## In scope

- parity-exact adjacent-edge formula and chain coefficient;
- analytic identification of the leading pairwise constraint families;
- explicit angular gaps and proof of both directed constraints for every pair;
- a matching leading lower bound for this fixed order;
- seam and alternating-valley treatment;
- the exact deletion-monotonicity consequence for global `R*(n)`;
- a task-local independent diagnostic/checker and synchronized proof/status
  documentation.

## Out of scope

- optimization over broader order families;
- a global lower bound matching the new construction or existence of the
  normalized global limit;
- sharp fixed-order subleading terms or the least finite validity index;
- changes to production code, finite certification, result artifacts, or the
  historical arXiv-v1 paper.

## Expected delta

Add one authoritative fixed-order proof note and this dossier, including a
task-local checker if useful. Update only the owning fixed-order ledger, the
global ledger for the proved global corollary, `CURRENT_STATUS.md`, and the
ranked roadmap. `PROJECT_KNOWLEDGE.md` should remain unchanged unless its
module routing or central guardrails genuinely need revision.

## Protected paths potentially affected

- `paper_assets/`: historical arXiv-v1 record; no change.
- `results/`, `verify.py`: finite certification; no change.
- `src/`, `tests/`, `scripts/`: production implementation; no change.
- `README.md`, `REPORT.md`, unrelated notes and prior dossiers: no change.

## Completion gates

- [x] chain coefficient proved without presupposing the root scale;
- [x] controlling valley/seam and any other leading constraints classified;
- [x] explicit gaps proved feasible for every pair and both cyclic arcs;
- [x] matching fixed-order leading lower obstruction proved;
- [x] even-only and all-`n` global deductions separated and justified;
- [x] independent diagnostic run with numerical output classified correctly;
- [x] durable memory updated without duplicate claim ownership;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct untracked whitespace audit and `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The task proves an exact finite fixed-order formula before taking the limit:
`R_full(sigma_{2m})` is the unique root of the disjoint cellwise valley sum
`S_m(R)=2*pi`, and displayed gaps attain that obstruction with a complete
all-pairs seam proof. The chain and full coefficients are respectively
`J/(2*pi)=0.1337405685...` and
`K/(2*pi)=0.1423338536...<1/(2*pi)`. Deletion transfers only the upper bound
`limsup R*(n)/n^2<=K/(2*pi)` to all integer sizes. Analytic, symbolic,
independent high-precision, production cross-check, documentary, and diff
gates pass. Suggested manual commit:
`Prove alternating-halves full asymptotics`.

Exactly one proposed next atomic task: independently review the exact
cellwise characterization, thick-shell/seam all-pairs proof, constants, and
deletion corollary without optimizing another order family.
