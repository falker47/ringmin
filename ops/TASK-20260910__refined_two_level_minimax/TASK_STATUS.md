# Task Status

```text
task=TASK-20260910__refined_two_level_minimax
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-10
updated_at=2026-09-10
```

## Objective

Resolve the scalar minimax implied by Section 11's proved deletion bound,
enclose its asymptotic coefficient rationally, propagate the existing finite
errors and transfer the lower bound through deletion from full feasibility.

## Scientific or engineering question

For every common outer tour at every integer n>=102, what lower bound follows
from the envelope max{e,e+D_n-40*e^(2/3)-432*e}, e>=0? The input deletion
theorem is proved; the requested scalar consequence is the bounded question.

## In scope

- Extend `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md` with the proof.
- Add a bounded standalone exact checker and this dossier.
- Update the sole owning common-chain entry in the global-bounds ledger,
  current status and the materially affected roadmap endpoint/review scope.

## Out of scope

Exponent/constant optimization, changing q or beta, new couplings, tour enumeration,
upper constructions, finite certification, normalized limits and paper changes.

## Expected delta

Four existing Markdown files and this task's four dossier/checker files.
No index change: scope, central guardrails, ownership and navigation persist.

## Protected paths potentially affected

`paper_assets/`, `results/`, `src/`, `verify.py`, `tests/`, `.github/`,
publication/release metadata and all prior dossiers: preserve baseline blobs.
Sections 2-11 of the proof retain their historical statements; add a clearly
scoped extension and a navigation pointer in Section 1.

## Completion gates

- [x] Scalar proof, exact enclosures and finite/global transfer complete.
- [x] Independent bounded checker and relevant dependency checkers pass.
- [x] Claim classifications and limitations audited; sole ledger owner updated.
- [x] Complete tracked/untracked diff and addition whitespace inspected.
- [x] All 458 other tracked paths and original proof Sections 2-11 preserved.
- [x] State set to `READY_FOR_REVIEW`; external acceptance remains separate.

Staged inspection, commit and normal push occur after this precommit snapshot;
their exact results, SHA and final working-tree state belong to the final
handoff. They are required integration steps, not a mathematical review decision.

## Blockers

None. Git ownership mismatch is handled with a per-command safe.directory
option; no global configuration is changed.

## Handoff

The requested refinement is proved: exact scalar minimum, rational
coefficient enclosures and propagated finite/global bounds are in Section 12.
The checker supplies independent bounded algebra/enclosure support; prior
Section 11 and minimax diagnostics pass. No exponent optimality, geometric
sharpness, normalized limit or finite certification is claimed.

Exactly one next atomic task: independently review the refined Section 12
bound and its required Section 11 dependency, reproducing the bounded checker
at committed HEAD; record acceptance or precise corrections.
