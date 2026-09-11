# Task Status

```text
task=TASK-20260911__three_level_common_chain
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-11
updated_at=2026-09-11
```

## Objective

Resolve the common-chain minimax on T_q(n), T_(1/5)(n) and
T_(23/100)(n), with q=q_*, by an exact improvement over C_term+eta_split
or an exact obstruction for this concrete mechanism.

## Scientific or engineering question

Can two distinct deletion cutoffs consume a shared reflected-edge energy
budget in a way that strengthens the existing single-cutoff envelope?
All bounds must hold for every outer cyclic order, with original radii.

## In scope

- New authoritative proof research/THREE_LEVEL_COMMON_CHAIN.md.
- Standalone bounded exact checker and this dossier.
- Owning global-bounds ledger, current status and research priorities.
- Finite order-uniform transfer, including full-feasible deletion if proved.

## Out of scope

Upper constructions, width optimization, two-level constant tuning, tour
enumeration, finite certificates, production changes and paper revisions.

## Expected delta

A shared-measure relaxation, a joint crossing inequality at the two fixed
cutoffs, and either a rigorously separated coefficient or an obstruction.

## Protected paths potentially affected

paper_assets/, results/, src/, tests/, verify.py, README.md, REPORT.md,
AGENTS.md, PROJECT_KNOWLEDGE.md, and existing proof/checker files remain
unchanged. Verification checks their diff against the startup HEAD.

## Completion gates

- [x] proof and finite transfer complete;
- [x] exact arithmetic and negative controls pass;
- [x] continuum relaxation and claim scope inspected;
- [x] durable memory and handoff updated;
- [x] complete new files, tracked diff and explicit whitespace inspected;
- [x] protected paths unchanged;
- [x] READY_FOR_REVIEW precommit handoff.

Integration gates: staged inspection, normal authorized commit/push and
remote verification follow this handoff; their outcome is reported in the
final response. No separate mathematical acceptance is implied.

## Blockers

None. A command-local Git safe.directory setting resolves the sandbox
ownership mismatch without modifying user configuration.

## Handoff

Completed the positive discriminator: the common outer measure supplies a
joint crossing inequality and an exact coefficient strictly above the old
two-level bound. The proof includes a necessary continuum relaxation and
an all-order finite transfer through full-feasible deletion. The new and
prior dependency checkers pass locally; the optimized-mode guard rejects
disabled assertions. Exact minimax/sharpness and external acceptance remain
unresolved. Exactly one next atomic task: independently review this
three-level theorem and reproduce its bounded checker at committed HEAD.
