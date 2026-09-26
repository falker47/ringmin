# Task Status

```text
task=POST-RING-6_ARCHIVE_EVIDENCE_INTEGRATION
phase=implementation
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-26
updated_at=2026-09-26
initial_local_head=80919666c3c54f8ce20cf66c456d413f6a2c075f
base_head=7201f788b586ae059078dde6221d58b0ce8f79a1
accepted_review_baseline=80919666c3c54f8ce20cf66c456d413f6a2c075f
accepted_baseline_source=live Review State Registry, State!A1:F2, 2026-09-26
release_commit=80919666c3c54f8ce20cf66c456d413f6a2c075f
version_doi=10.5281/zenodo.22849826
```

## Objective and engineering question

Can the completed archival audit remain inspectable without depending
exclusively on Temp, with unambiguous archive identity and provenance?
This is documentary persistence and engineering validation, not a new audit,
scientific review, finite certification or submission.

## In scope and expected delta

- This dossier: original-output provenance, public evidence, manifests and
  task-local preparation/integrity scripts.
- `CURRENT_STATUS.md`, the archival roadmap entry, one README archive reference,
  and the software version DOI in `CITATION.cff`.
- An external durable copy of the original audit's top-level files.

## Out of scope and protected paths

Every other baseline tracked path is protected, including solver, verifier,
scientific tests, dependencies, certificates, original scientific manifests,
proof notes, ledgers, manuscripts, PDFs, arXiv sources and historical dossiers.
`AGENTS.md` and `RINGMIN_REVIEW_PROTOCOL.md` are unchanged. The exempted
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip` must stay
untracked and byte-identical. Registry, PersonalContext, tag, release and
Zenodo metadata are read-only. No new scientific computation is authorized.

## Completion gates

- [x] Audit report, structured evidence, inventory and pertinent logs read and
  cross-checked before editing existing tracked files.
- [x] Registry baseline and Git identities checked; authorized fast-forward
  completed without a merge commit or loss of local commits.
- [x] 68 original files copied with matching before/after SHA-256 and sizes.
- [x] Public package distinguishes 20 byte-identical files and 8 derivatives.
- [x] Current references reconciled; paper preferred-citation preserved.
- [x] Documentary checks and protected-path checks.
- [x] Staged evidence blobs match their declared hashes; whitespace checks.
- [x] State set to `READY_FOR_REVIEW` for independent review after integration.

Final integration gates are complete staged-diff inspection, re-staging only
the finalized task files, scoped commit, normal push and remote SHA readback.
Their exact results and commit identity are recorded in the final handoff.

## Blockers and handoff

The initial blocker was the local main lag, already present in the prior audit.
The user explicitly authorized fetch and a strictly fast-forward synchronization
for this task; it resolved that blocker. No evidence is missing from the local
original audit set. Public omissions and redactions are documented in
[EVIDENCE.md](EVIDENCE.md); no scientific acceptance follows from this work.

After successful push, exactly one next atomic task: independent review of the
exact integration commit and the full accepted-baseline delta. Commit identity,
push result and exact-SHA hosted CI observation belong to the final handoff;
this file cannot contain its own containing commit's hash.
