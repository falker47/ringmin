# Task Status

```text
task=TASK-20260915__finalize_corrective_v2
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-15
updated_at=2026-09-15
```

## Objective

Finalize the prepared corrective v2 of arXiv:2607.28654 now that its
standalone asymptotic sequel has the permanent identifier arXiv:2609.13630.
Replace only obsolete pending-identifier and draft-readiness material, rebuild
the corrective manuscript with the existing tooling, and complete the existing
publication/package audits without any arXiv submission or other external
publication action.

## Scientific or engineering question

Does the already audited corrective source remain byte-preserving in its
mathematical content while its companion citation and publication state move
from pending to a locally copy-ready replacement candidate? This is an
editorial and reproducibility task; it introduces no mathematical claim,
result, certificate, proof, or reinterpretation.

## In scope

- `paper_assets/v1_correction/` source, README, review metadata and build manifest;
- the shared publication builder and existing publication checker status expectations;
- current status, publication history, public README and research roadmap navigation;
- this task's build, audit, protection and handoff evidence.

## Out of scope

- any edit to `paper_assets/asymptotic_sequel/` beyond the navigation-only
  identifier-status cleanup required by the final marker audit;
- historical v1 assets, the superseded former replacement, proof notes,
  mathematical ledgers, numerical results, certificates, production code,
  verifier, citation metadata or external publication systems;
- arXiv submission, replacement finalization, moderation, or hosted-CI claims.

## Expected delta

Replace the two pending sequel markers and stale draft-readiness wording in
the corrective source and README with the supplied permanent identifier and a
truthful unsubmitted replacement-candidate status. Regenerate the correction's
source bundle, PDF, manifest and review metadata through the existing builder
and checker, then record only current navigation/status changes and this
dossier.

## Protected paths potentially affected

- `paper_assets/asymptotic_sequel/` — source bundle, manuscript, PDF and
  mathematical content remain frozen; README navigation-only cleanup is checked;
- `paper_assets/ringmin_paper.tex`, its PDF, appendix, figures and `CITATION.cff`
  — historical v1 and default citation remain unchanged;
- `paper_assets/v2/` — superseded former replacement remains provenance;
- `research/`, `knowledge/` mathematical sources, `results/`, `src/`,
  `verify.py` and workflows — no scientific or computational changes;
- `paper_assets/v1_correction/appendix_tables.tex` and copied figures —
  numerical/table/figure inputs must remain byte-identical.

## Completion gates

- [x] obsolete pending identifier/draft-status material removed only in scope;
- [x] mathematical source/data preservation checked independently;
- [x] builder passes with stable references and zero warnings; author-supplied
      independent direct clean compile passes with deterministic dates;
- [x] existing publication/package checks pass with finalized status and ID
      when given the actual builder clean directory;
- [x] final PDF is rendered and every page inspected for layout defects;
- [x] protected source/data paths and standalone mathematical tree are
      unchanged; the standalone README change is navigation-only;
- [x] status, metadata, manifest and dossier agree after this update;
- [x] full diff, additions and whitespace inspected;
- [x] commit and normal push verified under repository authorization;
- [x] state set to `READY_FOR_REVIEW`.

## Integration record

The author-run builder completed three clean passes with zero warnings and
produced the current PDF/manifest/metadata. The builder's actual clean
directory is
`reproducibility/.work/publication-correction-cb650a4f8a1144d28846f13ff0e894e2`;
the existing checker passes against it.

The author independently compiled the four-file source bundle in a TeX-capable
environment with `SOURCE_DATE_EPOCH=1789084800` and `FORCE_SOURCE_DATE=1`. The
resulting independent clean build is
`reproducibility/.work/independent-correction-local`; the existing checker
passes against it. Codex did not rerun the completed TeX compilation. The
earlier sandbox AppData failure remains historical negative evidence only.

After the Codex sandbox could not create `.git/index.lock`, the author verified
that the local repository itself was writable, staged exactly the inspected
14 tracked changes plus the three-file task dossier, ran
`git diff --cached --check` successfully, committed the package as
`79c784e5300fd98c454eaa59c10507191ec86b69` (`Finalize corrective v2 after
sequel publication`) and pushed `main` to `origin`. The remote commit was read
back after the push. Therefore no repository-integration blocker remains.

`TASK_LOG.md` and `EVIDENCE.md` retain the earlier sandbox blocker entries as
chronological evidence; this status file is the current disposition and
supersedes those blocker states.

## Handoff

The identifier/source edit, builder artifact, package audit, source/data
preservation check, PDF inspection, independent source-only compile and
repository integration are complete. The corrective package is ready for the
author's arXiv replacement step. No arXiv replacement was submitted by this
task.

The next atomic task is to upload only the contents of
`paper_assets/v1_correction/source_bundle/` as the replacement of
arXiv:2607.28654v1, inspect arXiv's compiled PDF and metadata against the
reviewed candidate, and finalize only if the server output is correct.
