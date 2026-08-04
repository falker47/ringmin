# Task Status

```text
task=TASK-20260804__continuous_review_bootstrap
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-08-04
updated_at=2026-08-04
```

## Objective

Install the Ringmin durable-memory, atomic-task, and independent continuous-review workflow without modifying existing mathematics, code, tests, certificates, generated artifacts, paper files, publication metadata, or CI behavior.

## In scope

- `AGENTS.md`
- `PROJECT_KNOWLEDGE.md`
- `CURRENT_STATUS.md`
- `RINGMIN_REVIEW_PROTOCOL.md`
- `research/NEXT_RESEARCH_STEPS.md`
- `_TEMPLATES/*.md`
- this task dossier

## Out of scope

- source or test changes;
- artifact regeneration;
- paper or README revision;
- CI modification;
- tag, release, email, arXiv, or Math StackExchange action;
- starting the first mathematical research task.

## Expected delta

Add only the workflow files listed above. Preserve all pre-existing tracked files byte-for-byte.

## Protected paths potentially affected

None should be affected. The applying Codex session must explicitly inspect for accidental changes under:

- `src/`
- `tests/`
- `results/`
- `paper_assets/`
- `scripts/`
- `verify.py`
- `.github/`
- publication metadata and public documentation

## Completion gates

- [x] actual repository `HEAD` and initial working tree inspected;
- [x] proposed facts reconciled against the current repository;
- [x] workflow cross-links and relative paths checked;
- [x] `python -m pytest` run and result recorded;
- [x] smoke verifier run and correctly classified;
- [x] full verifier run locally and its provenance limitation recorded;
- [x] complete working-tree delta, including every untracked addition, inspected;
- [x] `git diff --check` passed and direct untracked whitespace checks passed;
- [x] no pre-existing tracked file changed;
- [x] dossier evidence completed with actual outputs;
- [x] `CURRENT_STATUS.md` and this file set to `READY_FOR_REVIEW`.

## Blockers

None. The pre-existing full-verifier fresh-clone portability gap is a recorded residual risk, not a blocker to reviewing this workflow-only delta.

## Handoff

The workflow bootstrap is ready for independent review. After external acceptance, begin exactly one new task: prove or refute the all-`n` radius-1 seam obstruction stated in `research/NEXT_RESEARCH_STEPS.md`.
