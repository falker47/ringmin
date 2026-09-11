# Task Status

```text
task=TASK-20260911__optimized_midpoint_split
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Optimize the already-proved midpoint split without new structural
hypotheses and propagate its coefficient through Sections 11-12, or
identify the first rigorous obstruction.

## Scientific or engineering question

For every existing-domain tour (n>=102), determine the best bound obtained
by minimizing 4*h^2+E/h over h>0. Prove its finite/asymptotic scalar and
global lower consequences, keeping scalar sharpness, tour realizability
and full geometry separate.

## In scope

- `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md`, Sections 11.3-11.4
  and 12, with affected overview statements;
- the owning common-chain entry of `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`;
- `CURRENT_STATUS.md`, the relevant roadmap entries, and this dossier;
- a bounded independent standard-library checker of new identities and
  rational enclosures, including necessary parameter gates.

## Out of scope

New structural estimates, q/beta optimization, tour enumeration or
realization, upper constructions, expanded finite certification, paper revisions.

## Expected delta

The split coefficient decreases from 5 to 3; the propagated deletion
coefficient decreases from 40 to 24. Replace the active Section 12 scalar
formula and enclosures; preserve the previous coefficient's provenance.

## Protected paths potentially affected

`paper_assets/`, `results/`, `src/`, `tests/`, `verify.py`, publication/release
metadata, all previous dossiers, the central index, other ledgers and
proof notes. Sections 2-10 and the Section 11.5-11.6 family proofs stay
unchanged. Verify their absence from the final diff.

## Completion gates

- [x] proof and classification complete within scope;
- [x] independent exact checker and disabled-assertion guard run;
- [x] rational enclosures and finite-error/global transfer audited;
- [x] durable memory updated without duplicate ownership;
- [x] complete proof, ledger, roadmap and new checker inspected;
- [x] protected/generated paths unchanged;
- [x] state set to READY_FOR_REVIEW.

This is the precommit handoff. The final status/dossier diff and complete
staged diff are inspected before the authorized commit and normal push.
The commit containing this dossier identifies the submitted version;
the final response records its SHA, push result and working-tree state.

## Blockers

None. Git needs a command-local safe.directory because the sandbox account
differs from the repository owner; no global configuration was changed.

## Handoff

The exact split optimization propagates successfully with no new structural
premise. The new finite bound is uniform for n>=102; its strict rounded
corollary has a sufficient cutoff n>=10^12. All coefficient values and
their classifications are owned by the proof and common-chain ledger.
The checker is independent of production and earlier checkers, not an
external mathematical review or a geometric optimality certificate.

Exactly one next atomic task: independently review the optimized split
and its Section 12 propagation at committed HEAD, audit its unchanged
all-tour inputs as needed and reproduce the new bounded checker.
