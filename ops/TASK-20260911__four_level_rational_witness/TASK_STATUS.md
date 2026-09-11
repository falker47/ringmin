# Task Status

```text
task=TASK-20260911__four_level_rational_witness
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Decide rigorously whether the user-supplied three-cutoff rational witness
proves eta_4 > eta_3 + 1/10000000 through the accepted finite
shared-crossing corollary. Keep the witness fixed even if it fails.

## Scientific or engineering question

For the same outer cyclic order and its three nested restrictions, prove
the finite/stability hypotheses for all sufficiently large integers n,
enclose the three deletion integrals and the resulting coefficient, and
transfer the bound to the full geometric problem. Exact theorem and
rational arithmetic support; no floating-only inference.

## In scope

- `research/THREE_LEVEL_COMMON_CHAIN.md`: append the fixed four-level result.
- `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`: single owning entry and navigation.
- `CURRENT_STATUS.md` and `research/NEXT_RESEARCH_STEPS.md`.
- This dossier and one standalone bounded arithmetic checker.

## Out of scope

Solver, certificates, verifier, paper, generated publication assets,
parameter search, optimization, tour enumeration and new stability constants.

## Expected delta

One fixed-witness proof section, one exact checker, one owning ledger entry,
and the required task/status/priority handoff. Preserve proof Sections 1-10
and the original meanings of eta_3 and C_term.

## Protected paths potentially affected

`src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`, `REPORT.md`,
`README.md`, generation scripts and all pre-existing checkers: compare the
final changed-path list against the explicit eight-path allowlist.
`AGENTS.md`, `PROJECT_KNOWLEDGE.md` and other thematic ledgers need no edits.

## Completion gates

- [x] Exact separations and all finite/stability gates proved.
- [x] Rational enclosures and strict discriminator resolved.
- [x] Finite, asymptotic and full-geometric statements justified analytically.
- [x] Bounded checker and relevant dependency checks run locally.
- [x] Claims classified; durable memory and handoff updated.
- [x] Full new-file/diff/whitespace/link/protected-path inspection complete.
- [x] READY_FOR_REVIEW precommit handoff; inspected staging, authorized
  commit and normal push are the remaining integration steps, reported in
  the final response with SHA and remote/working-tree verification.

## Blockers

None. The user reports the finite shared-crossing theorem accepted; its
old status file is a precommit review handoff, not a contrary review decision.

## Handoff

The unchanged witness proves the requested strict gain via the accepted
corollary. Exact enclosures, all-n gates and limitations are in proof
Section 11 and EVIDENCE.md. No mathematical blocker; independent acceptance
and endpoint sharpness remain separate.

Exactly one next atomic task: independently review this fixed-witness
theorem and reproduce its checker at committed HEAD, recording acceptance
or precise corrections without parameter search or further research.
