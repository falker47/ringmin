# Task Status

```text
task=TASK-20260905__mu_ref_recovery
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-05
updated_at=2026-09-05
```

## Objective and scientific question

Decide whether the single coupling mu_ref in
research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md is a weak limit of
empirical triples of actual high permutations. Either give a deterministic
sequence with exact occurrence/seam bookkeeping and transfer its full-radius
coefficient, or prove a necessary-condition obstruction.

## In scope and expected delta

- research/PERMUTED_HALVES_MU_REF_RECOVERY.md: authoritative new proof;
- knowledge/FIXED_ORDER_THEORY.md: recovery and fixed-order coefficient;
- knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md: only the immediate geometric
  upper-bound corollary, if recovery is proved;
- research/NEXT_RESEARCH_STEPS.md, CURRENT_STATUS.md and this dossier;
- a bounded task-local checker, independent of production implementations.

## Out of scope and protected paths

General recovery theorems, optimization over permutations or couplings,
search for a relaxation minimum, finite global certification, production
changes and paper revision. All previous proof notes/dossiers, paper_assets/,
results/, src/, tests/, scripts/, verify.py, README.md, REPORT.md, publication
metadata, other ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md are protected. No Git/GitHub state writes.

## Verification design

Prove the deterministic parity map is a permutation, retain the exact cyclic
predecessor, list every exceptional cell and prove weak convergence for all
continuous test functions. Use the already proved uniform root transfer.
Bounded exact checks: all m=2..128 and all integer shifts 0<=s<m/2, with
endpoint and interior rational alpha representatives of each floor interval.
This checks only the prescribed construction, not permutation enumeration.
Audit the parity formulas symbolically. Optional diagnostic moments use
alpha=1/10 and m=8,9,15,16,31,32,64,128,256,512,1024; exact rational
integration supplies the target and a proved modulus bound supplies the gate.
No randomness or numerical optimizer. These checks audit the proof and do
not substitute for its all-m argument.

## Completion gates

- [x] exact recovery proved for the requested coupling;
- [x] consequent full-radius coefficient justified and claims classified;
- [x] bounded exact/independent checks run and recorded;
- [x] ledger owners, roadmap, current status and dossier synchronized;
- [x] full tracked/untracked content and whitespace inspection;
- [x] no incidental protected/generated changes;
- [x] state set to READY_FOR_REVIEW.

## Blockers

None. Clean startup at HEAD 49714545aeb77c0384753d1f29560b7a4c03d429.
Use per-command safe.directory for read-only Git queries; no persistent
configuration change. Imported proofs await external review; this task does
not record acceptance on their behalf.

## Handoff

Recovery is proved by the explicit parity construction. The uniform theorem
transfers its cost to C_ref<C_shift for full radii; deletion gives only the
immediate global upper bound. Exact finite checks and the complete nine-file
content/whitespace/provenance audit passed. No minimum or general recovery
theorem is asserted. External independent review remains pending.

Suggested manual commit: research: realize mu_ref by deterministic high permutations

Exactly one proposed next atomic task:
independently review this recovery proof and its uniform root-transfer
dependency, reproduce its checker and record acceptance or corrections.
