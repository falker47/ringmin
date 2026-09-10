# Task Status

```text
task=TASK-20260910__knowledge_hygiene
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-10
updated_at=2026-09-10
task_base_head=ab6f663200f8d9eae95d30c6c96eb6c052aed881
```

## Objective

Reduce routine orientation context while preserving current scientific
meaning, thematic ownership, and all historical evidence and provenance.

## Scientific or engineering question

Engineering/documentation only: can the current roadmap be made compact
without changing its live research priorities, strongest bounds or claim
classifications, and can all displaced text be recovered exactly?
The user supplies task-start HEAD as the accepted baseline. This task does
not independently decide mathematical acceptance or perform a review backlog.

## In scope

- Compact `research/NEXT_RESEARCH_STEPS.md` and add its complete verbatim
  baseline snapshot in `docs/archive/RESEARCH_ROADMAP_20260910.md`.
- Clarify targeted retrieval in `AGENTS.md` and `PROJECT_KNOWLEDGE.md`.
- Label historical navigation in `docs/post_arxiv_tasks.md`,
  `SUBMISSION_CHECKLIST.md`, and `SUBMISSION_REVIEW_REPORT.md`.
- Update `CURRENT_STATUS.md` and this dossier, with one bounded documentation
  audit script, `check_hygiene.py`.

## Out of scope

Mathematical research/review, ledger splitting, proof or claim changes,
certification, code/tests, publication revision, regeneration, deletion of
old dossiers or evidence, and external publication actions.

## Expected delta

Exactly seven modified Markdown paths and five added paths (archive plus
four dossier files). The archive preserves the full former roadmap, including
retained current passages, to make completeness a byte-equality check.
Only the current roadmap ranks research; only `CURRENT_STATUS.md` records
current task state. The index and thematic owners keep their distinct roles.

## Protected paths potentially affected

All baseline tracked paths outside the seven allowed modifications,
especially `knowledge/`, every other `research/` note, old `ops/TASK-*`,
`RINGMIN_REVIEW_PROTOCOL.md`, `src/`, `tests/`, `scripts/`, `verify.py`,
`results/`, `paper_assets/`, `README.md`, `REPORT.md`, publication metadata
and CI. Check Git-normalized blob equality for every such path. Historical
bodies of the three labeled documents are also protected.

## Completion gates

- [x] compact current roadmap and explicit retrieval policy;
- [x] exact archive payload, complete section coverage and provenance;
- [x] current priorities/bounds/limitations preserved semantically;
- [x] historical navigation and local links checked;
- [x] protected files and historical bodies unchanged;
- [x] full tracked/untracked diff and whitespace checks;
- [x] dossier/current status consistent; no new thematic claim owner;
- [x] state set to `READY_FOR_REVIEW` for independent review.

Integration sequence: inspect the staged diff and its whitespace, commit only
these 12 paths, push normally to existing `origin/main`, and verify the remote
SHA and remaining tree. The final handoff reports the outcome; the commit
containing this dossier identifies the reviewed delta from `task_base_head`.

## Blockers

None. Sandbox Git ownership requires a command-local `safe.directory`
override; no persistent Git configuration change is needed.

## Handoff

Verified documentation restructuring; no scientific change. Exactly one next atomic task: independently
review this knowledge-hygiene diff and its preservation/navigation evidence.
The scientific roadmap's existing Section 11 review priority is retained;
no mathematical task is started here.
