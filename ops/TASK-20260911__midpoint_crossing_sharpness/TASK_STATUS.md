# Task Status

```text
task=TASK-20260911__midpoint_crossing_sharpness
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Resolve whether the Section 11 midpoint crossing term K admits a uniform
bound with an exponent greater than 2/3 over genuine cyclic tours.

## Scientific question

Keep exactly q, beta, mu, E, B and K from the common-chain proof. Either
prove a stronger uniform bound or prove an explicit infinite family
obstructing it. The established counterexample is an exact theorem about
cyclic orders, not a full-feasibility or finite optimum certificate.

## In scope and expected delta

- Add the construction and proof in Section 11.5 of
  `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md`.
- Add a bounded standalone integer/rational checker and this dossier.
- After establishing the theorem, update the existing common-chain entry
  in `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, `CURRENT_STATUS.md` and
  `research/NEXT_RESEARCH_STEPS.md`.

## Out of scope and protected paths

No signed-deletion sharpness theorem, constant optimization, scalar minimax
change, new coupling method, tour search or geometric claim. Protect
`paper_assets/`, `results/`, `src/`, `tests/`, `verify.py`, generated assets,
publication metadata and other ledgers. Preserve the existing Section 12
bounds and the compact index. Verify protection by the final path diff.

## Completion gates

- [x] exact construction, parity and midpoint accounting proved;
- [x] bounded independent diagnostic passes;
- [x] claims and non-implications classified;
- [x] owning ledger, status and roadmap updated after the theorem;
- [x] tracked and untracked additions inspected with whitespace checks;
- [x] protected paths unchanged;
- [x] state set to `READY_FOR_REVIEW`.

Authorized integration follows this precommit record: inspect staged diff
and whitespace, commit the eight inspected paths and normally push to the
existing `origin/main`; verify the remote SHA and clean working tree. The
final task response records those post-record outcomes.

## Blockers

None. Git reads use command-local `safe.directory` because the sandbox
account differs from the repository owner; no global configuration change.

## Handoff

Resolved: exponent 2/3 is sharp for K, with an explicit single-cycle family
and exact finite formulas. Local isolated checker exit 0; no general-tour
enumeration. Signed Delta sharpness and optimal constants are not claimed;
the existing global coefficients and protected files are unchanged.
Exactly one next atomic task: independently review the new Section 11.5
crossing-sharpness theorem and reproduce its bounded checker, without
starting further research. External acceptance remains separate.
