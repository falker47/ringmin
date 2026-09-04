# Task Status

```text
task=TASK-20260904__radius10_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute the four exact radius-10 endpoint gates at n=45,46 with
separator R=270. Deduce s_10=46 only after all four gates close and only
through the fixed-k theorem.

## Scientific question

Does R_{10,45}<270<T_{10,45} and T_{10,46}<270<R_{10,46} hold for the
formal Supnick seam? No other endpoint, floating root or scan is a premise.

## In scope and expected delta

- `research/RADIUS10_SEAM_ONSET.md`: exact proof and complete witnesses.
- This dossier: status, append-only log, evidence, stdlib/Fraction checker,
  separate integer witness scorer, and rejection tests.
- `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`.

## Out of scope and protected paths

Production `src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`,
generation scripts, CI/configuration, README/REPORT, AGENTS, earlier proof
notes and dossiers. No global certificate or publication asset is affected.
Check the complete change allowlist at handoff. No Git/GitHub writes.

## Completion gates

- [x] Both full cyclic representations, closure and multiplicity checked.
- [x] Both threshold positivity/pre-square signs and directed margins pass.
- [x] Both complete chain sums pass exact arcsine/pi bounds.
- [x] Checker normal/-O, independent scorer and rejection tests pass.
- [x] `python -m pytest` run and exact result recorded.
- [x] Proof classification and fixed-k deduction checked; memory synchronized.
- [x] Provenance, complete tracked/untracked diff, scope and whitespace checked.
- [x] No incidental protected changes; state READY_FOR_REVIEW.

## Blockers

None. Git uses a per-command safe.directory override because the sandbox
identity differs from the repository owner; no global setting is changed.

## Handoff

All four gates close at R=270. The exact threshold directed margins are
1751/35283600 and 5989/38564100. Both complete chain bounds are strict;
see the authoritative proof note for every witness and analytic bound.
The fixed-k theorem gives s_10=46, with positive deficit on 12<=n<=45
and negative deficit on n>=46. Classification: exact theorem / proved
corollary, exclusively for the formal seam.

Checker/scorer normal and -O: pass; 28 rejection tests in both modes: OK;
`python -m pytest`: 12 passed in 27.86s. Exact outputs, five source hashes,
scope/diff/whitespace checks and limitations are in EVIDENCE.md.

Awaiting independent review and manual integration. Suggested manual commit:
`Prove exact radius-10 Supnick seam onset at n=46`.

Exactly one next atomic task after acceptance: attempt the STRICT radius-11
bridge only at n=49,50, with an exact rational separator and all four gates;
record failure if needed. The candidate s_11=50 is unproved. Not started.
