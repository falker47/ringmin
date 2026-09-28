# Task Status

```text
task=TASK-20260928__dcg_submission_package
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-28
updated_at=2026-09-28
accepted_baseline=6749d6b165f982136117481be322c8beaec223ce
```

## Objective

Prepare an upload-ready DCG package from the accepted manuscript, without
manuscript revision, scientific changes or journal submission.

## Scientific or engineering question

Can the exact accepted sources compile independently to the accepted PDF,
with a deterministic manifest and complete submission instructions?
All new conclusions are engineering checks or dated journal-policy observations.

## In scope and expected delta

- New `paper_assets/dcg_submission/`: exact manuscript copies, deterministic
  source ZIP, manifest, checksums, cover letter and upload checklist.
- This task dossier, packaging checker, and verification evidence.
- `CURRENT_STATUS.md` and the finite-submission priority in the roadmap.

## Out of scope and protected paths

Every pre-existing tracked path except `CURRENT_STATUS.md` and
`research/NEXT_RESEARCH_STEPS.md` is protected byte for byte. This includes
accepted journal sources/PDF/build metadata, public arXiv v1/v2, the sequel,
all scientific code, certificates, results, verifiers and thematic ledgers.
The sole untracked exception explicitly authorized by the user is
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip`, SHA-256
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.
It must not be changed, moved, renamed, staged, committed or packaged.
No other unrelated untracked path is exempt. Registry reads only.

## Completion gates

- [x] Live baseline and Registry agreement; exact source/PDF byte binding.
- [x] Live guidelines checked; no mandatory template migration.
- [x] Existing manuscript audit run; inherited evidence distinguished.
- [x] Clean independent two-pass compilation and PDF/render inspection.
- [x] Deterministic ZIP/manifest, all package hashes and protected bytes checked.
- [x] Cover letter, checklist and private metadata boundaries inspected.
- [x] Full working diff, untracked contents and direct whitespace checked.
- [x] State set to READY_FOR_REVIEW; no Registry promotion or submission.

Scoped staging, staged inspection, commit and normal push follow these local
gates under standing authorization. The final handoff records their observed
outcomes and exact resulting commit rather than predicting its hash here.

## Blockers

None for packaging. The public portal warning requires human confirmation
before any eventual upload. See the upload checklist.

## Handoff

Exactly one next atomic task: independent review of the exact committed
submission package; if accepted, human upload through Editorial Manager.
