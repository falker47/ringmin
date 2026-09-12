# Task Status

    task=TASK-20260912__standalone_submission_candidate
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-12
    updated_at=2026-09-12

## Objective

Finalize the existing standalone asymptotic sequel as the exact source-only
arXiv submission candidate for manual NEW submission, without new science.

## Expected delta and scope

Public prose and supplementary citations in `paper_assets/asymptotic_sequel/`;
rebuilt PDF and identical one-file source bundle; copy-ready metadata and
hash/environment manifest; minimal shared-builder update; canonical current
status/publication navigation; this task's reproducible audit evidence.

## Protected paths

Historical `paper_assets/ringmin_paper.tex` and PDF, tables and figures;
all `paper_assets/v1_correction/` and `paper_assets/v2/` assets;
`CITATION.cff`, proof notes and mathematical ledgers, results, production code,
`verify.py`, workflows and dependencies. Prior audit dossiers are immutable
evidence. The corrective v2 stays `AWAITING_STANDALONE_ARXIV_ID`; the older
replacement stays `EDITORIALLY_SUPERSEDED`.

## Completion gates

- [x] Public manuscript, citations, scope and overlap audited.
- [x] Bounded mathematical checks pass; no material scientific defect.
- [x] Isolated build and independent direct compile pass three times.
- [x] Every final PDF page visually inspected; objects and fonts checked.
- [x] Bundle, hashes, copy-ready metadata and canonical state agree.
- [x] Complete diff, untracked additions and whitespace inspected.
- [x] Authorized integration prepared: inspected paths only, normal commit/push.

## Integration identity

The containing commit identifies this exact source/PDF/manifest. Resolve it
with `git log -1 -- paper_assets/asymptotic_sequel/BUILD_MANIFEST.json`.
After the staged-diff/whitespace check, commit and normally push existing
`main` to `origin`; compare local HEAD with remote `refs/heads/main`.
The final command outputs and user handoff record the resulting exact SHA,
push result and clean working-tree state, without self-referential commit data.

## Blockers and handoff

No preparation blocker identified. Local verification is not external
acceptance. Server compilation and moderation remain the author's next gate.
Exactly one next human action: manually create a NEW arXiv submission using
the prepared standalone bundle and inspect arXiv's compiled PDF before finalizing.
