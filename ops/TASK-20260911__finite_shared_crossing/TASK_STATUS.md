# Task Status

```text
task=TASK-20260911__finite_shared_crossing
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Prove or refute the shared-crossing argument for any fixed finite number
of cutoffs, identify its width conditions and precise sharpness, and
propagate only the natural finite common-chain minimax/deletion corollary.

## Scientific or engineering question

For one reflected-edge measure, can all weighted crossing terms spend
the same quadratic energy once? Distinguish the integrated inequality,
its pointwise long-pair proof, and the actual finite grid/tour domain.

## In scope

- Extend `research/THREE_LEVEL_COMMON_CHAIN.md` without changing Sections 1-6.
- Add a bounded standalone rational checker in this dossier.
- Update the single owning global-bounds ledger, current status and review
  priority; record audit evidence here.

## Out of scope

Width/cutoff optimization, enumeration, new stability estimates, geometric
upper constructions, certificates, production changes and paper revisions.

## Expected delta

Adjacent separation theorem with explicit multi-crossing proof; sharpness
of uniform pointwise charging, exact negative controls, and a finite
positive-part minimax formula with the existing stability constants.

## Protected paths potentially affected

`AGENTS.md`, `PROJECT_KNOWLEDGE.md`, prior dossiers, `src/`, `tests/`,
`verify.py`, `results/`, `paper_assets/`, `README.md`, `REPORT.md`, generated
assets and release metadata: inspect the final changed-path set to confirm
preservation. The existing three-level numeric theorem remains intact.

## Completion gates

- [x] proof, quantifiers and sharpness complete;
- [x] standalone exact checks and negative controls pass;
- [x] existing three-level dependency checker rerun independently;
- [x] claims classified and durable memory updated;
- [x] complete tracked/new content inspected, explicit whitespace passed;
- [x] protected paths and old proof Sections 1-6 preserved;
- [x] state set to `READY_FOR_REVIEW` for independent review.

The final integration sequence is staged diff/whitespace inspection,
authorized normal commit/push and remote/tree verification. The final
response reports those actual results; no hosted-CI result is pre-claimed.

## Blockers

None. Git reads require a command-local safe.directory because the sandbox
user differs from the repository owner; no global Git configuration changed.

## Handoff

The extension is proved with adjacent separation, sharp for unrestricted
pointwise long charging. Its finite minimax corollary retains the existing
stability constants and full-feasible deletion transfer. Exact checks
include multi-crossing and a counterexample when separation is dropped.
Fixed-grid/integrated/tour sharpness and numerical optimization are not
claimed. No mathematical blocker; independent acceptance remains separate.

Exactly one next atomic task: independent review of the finite
shared-crossing theorem and its common-chain corollary at committed HEAD,
including the standalone checker and stability dependencies.
