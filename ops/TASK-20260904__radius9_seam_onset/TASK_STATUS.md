# Task Status

```text
task=TASK-20260904__radius9_seam_onset
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Prove or refute the four exact endpoint gates at n=41,42 and separator 220;
deduce s_9=42 from the fixed-k theorem only if all four gates close.

## Scientific question

Does `R_{9,41}<220<T_{9,41}` and `T_{9,42}<220<R_{9,42}` hold?
The proposed all-integer conclusion concerns only the formal Supnick seam
on consecutive radii starting at 9. No numerical scan is a premise.

## In scope and expected delta

- `research/RADIUS9_SEAM_ONSET.md`: exact proof and complete rational tables.
- This dossier: status, append-only log, evidence, stdlib/Fraction checker
  and proportionate rejection tests.
- Knowledge, current status and roadmap only after the exact bridge closes.

## Out of scope / protected paths potentially affected

`src/`, `tests/`, `verify.py`, `results/`, generation scripts, CI/configuration,
`paper_assets/`, `README.md`, `REPORT.md`, `AGENTS.md`, and existing proof
notes/dossiers are protected. Check the final allowlist and tracked diff;
no solver, global certificate, publication build or regeneration is needed.

## Completion gates

- [x] Four exact gates, positivity, pre-square signs and directed margins.
- [x] Complete 33/34 edges via independent rank and parity constructions.
- [x] Strict rational arcsine/pi witnesses, without floating roots.
- [x] Standalone checker and rejection tests pass normally and under -O.
- [x] Proof, classifications, provenance and durable memory synchronized.
- [x] Complete tracked/untracked review, explicit whitespace/scope audit.
- [x] No protected changes; state READY_FOR_REVIEW.

## Blockers

None. The initial Git ownership rejection was resolved with per-command
`safe.directory`; persistent configuration was not changed.

## Handoff

All four endpoint gates are proved; the fixed-k theorem gives s_9=42.
Classification: exact theorem / proved corollary concerning the formal seam.
The checker is independent of production/diagnostics; rejection tests are
checker-coupled and the separate integer scorer audits every witness.
Independent mathematical review remains necessary for acceptance; no full
geometric or global certification result is claimed. Final diff audit passed
for all nine files, including six untracked additions and four provenance
hashes. Manual integration only; state READY_FOR_REVIEW.

Suggested manual commit: `Prove exact radius-9 Supnick seam onset at n=42`.

Exactly one next atomic task after acceptance: attempt an exact radius-10
bridge at n=45,46 with a rational separator and four strict gates. The
candidate s_10=46 remains unproved. That task has not begun.
