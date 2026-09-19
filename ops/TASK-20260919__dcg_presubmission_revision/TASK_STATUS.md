# Task Status

```text
task=TASK-20260919__dcg_presubmission_revision
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
accepted_baseline=bfc2caff2ae6b1d1f149eb52cac4dc220dcf85d6
```

## Objective

Address the four supplied mock-referee findings in the finite DCG manuscript,
without introducing new mathematics or changing its accepted scope.

## Scientific or engineering question

Editorial clarification of an existing exact threshold comparison, minimizing
order wording, related-work attribution, and Git provenance. The finite result
remains the computer-certified brackets for 3<=n<=14; seam theorems and floating
quantifiers remain as accepted. This task is not independent acceptance.

## In scope and expected delta

- `paper_assets/journal_dcg/`: main source, seam appendix, PDF, source map,
  build metadata and necessary README wording.
- This dossier, a scoped manuscript audit and fresh verifier report.
- `CURRENT_STATUS.md` and the sole next review priority in the roadmap.

## Out of scope and protected paths

Every other tracked path is protected, particularly public arXiv v1/v2,
asymptotic sequel, `src/`, `results/`, certificates, both verifiers, tests,
proof notes and prior dossiers. Generated endpoint/coverage tables are also
protected. The user explicitly re-exempted the pre-existing untracked public-v2
ZIP: leave its bytes unchanged and never stage it. No tag, release, DOI,
cover letter, submission, or new mathematical claim is authorized.

## Completion gates

- [x] Baseline and scope inspected; existing ZIP exception confirmed.
- [x] Four editorial findings resolved and classifications preserved.
- [x] Complete exact verifier, STRICT seam checker and manuscript audit pass.
- [x] Two-pass LaTeX, references/boxes, render and visual inspection pass.
- [x] Source/build provenance and protected-path audit pass.
- [x] Complete diff, untracked additions and whitespace inspected.
- [x] READY_FOR_REVIEW for authorized scoped stage/commit/push and remote verification.

## Blockers

None after the explicit ZIP exception; local verification is complete.

## Handoff

All four findings are addressed in the 18-page PDF and sources. Complete
verification results and limitations are in EVIDENCE.md. Integration and the
remote/working-tree check are reported in the final handoff, not self-certified
as independent acceptance. No tag, release, archival deposit or submission.

Exactly one next atomic task: independent review della pre-submission revision;
se accettata, freeze release/archival DOI.
