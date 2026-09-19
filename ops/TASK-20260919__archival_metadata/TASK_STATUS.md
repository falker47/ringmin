# Task Status

```text
task=TASK-20260919__archival_metadata
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
accepted_baseline=2a1118b1236a8c8f9e356a5e01bd2afb4f689276
```

## Objective

Prepare one authoritative software citation metadata file for the forthcoming
GitHub/Zenodo archive of the accepted finite DCG pre-submission companion.
No tag, GitHub release, Zenodo deposit or DOI is created in this task.

## Scientific or engineering question

Can CFF 1.2.0 describe the current software and exact finite certificate
companion while GitHub continues to recommend the public finite paper?
This is an engineering metadata task, not mathematical recertification.

## In scope and expected delta

- `CITATION.cff`: software identity, abstract, sole author, URLs, MIT license,
  keywords, candidate archival version and preferred public finite-v2 citation.
- This three-file dossier: release contract, expected metadata, archive contents
  and validation evidence.
- `CURRENT_STATUS.md` and the finite priority in `research/NEXT_RESEARCH_STEPS.md`:
  review handoff and exactly one subsequent release/archive task.

## Out of scope and protected paths potentially affected

Every other tracked path is protected, including all `paper_assets/`,
`results/`, `reproducibility/`, `src/`, `scripts/`, `tests/`, both root verifiers,
proof notes, thematic ledgers, package/dependency files and published sources.
Compare all tracked paths against the accepted baseline. The user explicitly
exempted the pre-existing untracked
`paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip`;
retain its bytes, leave it unstaged and exclude it from the archive.

## Release contract

- Candidate CFF/archive version: `1.1.0-dcg-presubmission`.
- Candidate tag: `v1.1.0-dcg-presubmission`.
- Exact intended GitHub release title:
  **Ringmin 1.1.0-dcg-presubmission - finite DCG pre-submission companion**.
- Intended target: the independently accepted metadata commit descended from
  the baseline above, identified by its full SHA during the next task.
- Rationale: advance the archival snapshot identity beyond `1.0-arxiv-v1`,
  with an explicit pre-submission suffix. This is the repository companion's
  archival version; it is neither the arXiv version nor the Python distribution
  version (`0.1.0` remains unchanged). It makes no API compatibility claim.
- No release date or DOI is invented. No tag, release, deposit or DOI has yet
  been created for this candidate. Historical tags remain historical records.
- `CITATION.cff` is the sole release metadata source. No requested field needs
  Zenodo-specific grants, communities, contributor roles or related identifiers;
  `.zenodo.json` is intentionally absent.

## Expected Zenodo metadata and archive contents

See [EVIDENCE.md](EVIDENCE.md#expected-zenodo-metadata) for the documented field
mapping and its limits, and [the archive inventory](EVIDENCE.md#archival-snapshot-contents)
for the files that the forthcoming source archive must contain.

## Completion gates

- [x] bounded metadata change and release contract prepared;
- [x] claim scope inherited from the accepted finite baseline, without expansion;
- [x] CFF schema validation and GitHub citation rendering inspected;
- [x] metadata consistency and protected-path checks pass;
- [x] new files inspected in full;
- [x] current status and finite roadmap handoff updated;
- [x] complete working diff inspected;
- [x] state set to `READY_FOR_REVIEW`.

Final integration gates are direct/staged whitespace checks, staged-diff
inspection, scoped commit/push and remote/working-tree verification. Their
outputs and the self-referential final commit SHA are recorded in the handoff.

## Blockers and handoff

No preparation blocker remains. The untracked ZIP exemption is explicit in this task.
Independent review remains separate from local validation and commit/push.

After independent review, exactly one next atomic task: create the authorized
GitHub release/tag and archive it through Zenodo, then verify the issued DOI
and archived record.
