# Task Status

    task=TASK-20260911__publication_architecture
    mode=STRICT
    state=READY_FOR_REVIEW
    started_at=2026-09-11
    updated_at=2026-09-12

## Objective and question

Reorganize the already established science into a standalone asymptotic sequel
and a conservative correction of the historical finite paper. Determine the
publication separation, overlap and policy risk without new research or any
external publication action. Internal checks do not confer external acceptance.

## Expected delta, defined before implementation

- New self-contained source trees, PDFs, source bundles, build manifests and
  review handoffs in `paper_assets/asymptotic_sequel/` and
  `paper_assets/v1_correction/`; one shared clean builder.
- Supersession notices on the old replacement's current handoff/metadata.
- Publication history, README, current status and roadmap navigation agree.
- This dossier owns editorial decisions, claim maps, overlap, policy and checks.

## Protected paths

Historical `paper_assets/ringmin_paper.tex` and PDF, appendix and figures;
old `paper_assets/v2/ringmin_v2.tex`, PDF, upload source and build evidence;
`CITATION.cff`, mathematical proof notes and thematic mathematical claims;
all results, production solver, verifier, workflows and dependencies. Existing
audits remain historical evidence, with explicit supersession where needed.
Copies of historical tables/figures retain identical bytes.

## Completion gates

- [x] Both editorial roles implemented and all obsolete conjectures audited.
- [x] Claims, overlap and official arXiv policy separately checked internally.
- [x] Clean source-only builds, references, metadata and every PDF page checked.
- [x] Relevant mathematical checks and full saved-frontier verifier pass.
- [x] Historical/protected assets unchanged; no false publication identifier.
- [x] Canonical navigation and supersession notices coherent.
- [x] Full additions/diff and whitespace inspected for authorized integration.

## Integration identity

Stage only the inspected 41 task files, inspect the staged diff and whitespace,
then commit and normally push main to origin under standing authorization.
The task's commit is the containing commit, resolvable through `git log -1 --
ops/TASK-20260911__publication_architecture/TASK_STATUS.md`; final tool evidence
and the user handoff record the actual SHA and remote verification. No external
review decision is implied by integration.

## Blockers and handoff

No implementation blocker. The corrective candidate intentionally awaits a
real standalone identifier; it must remain `AWAITING_STANDALONE_ARXIV_ID`.
Moderation and external mathematical review remain outside this task.
Exactly one next atomic task: independent human review of the standalone.
