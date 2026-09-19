# Task Status

```text
task=TASK-20260919__journal_fixed_order_seam
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
accepted_baseline=2169bd429e25682777175ed31248b76feea8fabd
```

## Objective

Produce one self-contained, publication-quality fixed-order seam theorem
package for the finite journal paper, without constructing that manuscript.

## Scientific question

Choose between the full all-k onset table and the smaller theorem sufficient
for the public v2's fixed-order narrative. Reconstruct the proof rather than
treating ledger labels as evidence. All mathematical conclusions are exact
theorems or proved corollaries awaiting independent STRICT review.

## In scope and expected delta

- New `research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md`.
- This dossier, with a production-independent bounded exact/symbolic checker.
- A source-navigation update in `knowledge/FIXED_ORDER_THEORY.md`.
- `CURRENT_STATUS.md` and the finite-paper priority in
  `research/NEXT_RESEARCH_STEPS.md`.

## Out of scope and protected paths

All other tracked paths, particularly solver, results, global bracket
certificate/verifiers, old proof notes, public paper TeX/PDF/bundles and
asymptotic sequel. No Registry operations, tags, releases or journal directory.
The sole initial untracked path is the explicitly exempt
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip`;
preserve its SHA-256 and exclude it from staging.

## Completion gates

- [x] Complete self-contained proof and justified A/B decision.
- [x] Both parities, small cycles, both directions and closing gap audited.
- [x] Exact endpoint signs and stated equality exclusions checked.
- [x] Independent bounded checks pass, with limitations recorded.
- [x] Durable memory, full diff and untracked additions inspected.
- [x] Whitespace and protected-path checks pass.
- [x] State set to READY_FOR_REVIEW for the authorized integration sequence.

Integration follows this evidence snapshot: stage only inspected task paths,
audit the staged diff and whitespace, commit, normal push to origin/main,
and verify the remote SHA and status. The final task handoff reports the
observed result; this status is not external acceptance.

## Blockers

None. The ZIP exception is explicitly authorized in this task; AGENTS.md
does not require a second authorization for an already specified exception.
Read-only Git uses a command-local `safe.directory` setting because the
sandbox account differs from the repository owner; no Git config is changed.

## Handoff

Completed the narrow journal theorem package (option B). Its entire proof is
contained in the new note, with no essential development-note dependency.
Exact/symbolic checks pass; no protected mathematical/publication asset changed.
The explicit all-k onset formula is outside this package's scope, and independent
mathematical acceptance remains pending.

Exactly one next atomic task: independent STRICT review of the new theorem
package. Do not start the DCG manuscript here.
