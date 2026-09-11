# Task Status

```text
task=TASK-20260911__signed_discrepancy_family
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Resolve the signed deletion discrepancy of precisely the Section 11.5
family, for every multiple m of 10 with m>=40 and n=m^2, by analytic
formula and asymptotics; add only bounded independent corroboration.

## Scientific or engineering question

Determine the limit or other proved scale of |Delta|/E^(2/3), retaining
the actual floor k=floor(q*n), both outer parities and cyclic restriction.
The starting theorem determines E and K, not signed Delta.

## In scope

- `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md`: extend Section 11.
- `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`: existing common-chain owner.
- `CURRENT_STATUS.md`, `research/NEXT_RESEARCH_STEPS.md`: task and priority.
- This dossier and one standalone checker for fixed prescribed tours.

## Out of scope

Geometric feasibility, global coefficients, unrelated constants, general
tour enumeration, new coupling methods and publication/certification work.

## Expected delta

An exact replacement-edge formula and rigorous signed asymptotic with
classified consequence, four corresponding tracked documentation edits,
and four new dossier/checker files. No new thematic claim owner or index
change is needed.

## Protected paths potentially affected

`paper_assets/`, `results/`, `src/`, `tests/`, `verify.py`, all other
ledgers and the compact index remain unchanged. Existing proof Sections
1-10, 11.1-11.5 and 12 retain their proofs and coefficients; only minimal
forward references in Section 11's introductory/scope prose are allowed.
Verify against the base HEAD before staging.

## Completion gates

- [x] Analytic formula, parity/wrap accounting and asymptotic complete.
- [x] Claims classified and owning memory/roadmap updated.
- [x] Independent bounded checker, floors and symmetry checks pass.
- [x] Complete tracked diff and new files inspected; whitespace checked.
- [x] Protected paths and coefficients unchanged.
- [x] Set READY_FOR_REVIEW for the independent review handoff.

Staged inspection, authorized commit/normal push and remote/clean-tree
verification follow this precommit record; their result belongs in the
final response, without implying mathematical acceptance.

## Blockers

None. Command-local Git safe.directory handles sandbox ownership without
changing configuration.

## Handoff

Section 11.6 gives the exact finite radical formula, strict negative sign
and rigorous two-term asymptotic for the original family. The positive
normalized limit establishes the sharp signed exponent and rules out
uniform stronger exponents or little-o at that scale. Exact finite
identities and rational enclosures pass on six fixed sizes and 18 cyclic
presentations. These checks corroborate the analytic theorem; external
mathematical acceptance remains separate. No geometric or global
coefficient claim changed.

Exactly one proposed next task: independently review Section 11.6 at
committed HEAD, including its Section 11.5 dependencies, and reproduce
the new bounded checker. Record acceptance or precise corrections.
