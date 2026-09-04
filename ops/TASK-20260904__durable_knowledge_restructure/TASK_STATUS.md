# Task Status

```text
task=TASK-20260904__durable_knowledge_restructure
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-04
updated_at=2026-09-04
```

## Objective

Restructure the monolithic durable-knowledge ledger into a compact canonical
index plus six non-overlapping thematic ledgers, without changing any
mathematical result, epistemic classification, limitation, open claim,
disproved claim, non-implication, or relevant source link.

## Scientific or engineering question

This is a `STRICT` editorial and information-architecture migration. The
question is whether every stable knowledge unit in the pre-migration
`PROJECT_KNOWLEDGE.md` can be assigned to exactly one canonical thematic
ledger while preserving its wording, classification, qualifications, and
evidence pointers. No mathematical claim is being reconsidered.

## In scope

- `PROJECT_KNOWLEDGE.md` as compact canonical index;
- `knowledge/DEFINITIONS.md`;
- `knowledge/FIXED_ORDER_THEORY.md`;
- `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`;
- `knowledge/CERTIFICATION.md`;
- `knowledge/IMPLEMENTATION.md`;
- `knowledge/PUBLICATION_HISTORY.md`;
- `AGENTS.md` source hierarchy and startup/navigation rules;
- this task dossier and `CURRENT_STATUS.md`;
- explicit pre/post knowledge, link, classification, uniqueness, and
  protected-path audits.

## Out of scope

- proof notes and scientific roadmap changes;
- paper/arXiv assets and publication claims;
- code, tests, verifier, result artifacts, README, and REPORT;
- re-certification, new computation, and mathematical review;
- any change to the epistemic state or substantive wording of a claim.

## Expected delta

Replace the body of `PROJECT_KNOWLEDGE.md` with scope/provenance, only the
central object distinctions and guardrails, a descriptive module index, and
navigation/ownership rules. Move the pre-existing ledger content into six
thematic files, keeping claim blocks verbatim wherever possible and assigning
each stable claim to one module. Amend `AGENTS.md` to make the index and module
roles mandatory. Update task-local status/evidence only.

## Protected paths potentially affected

- `research/*.md`: authoritative proof notes; must remain byte-identical;
- `research/NEXT_RESEARCH_STEPS.md`: sole scientific roadmap; must remain
  byte-identical;
- `paper_assets/**`: historical publication assets; must remain byte-identical;
- `src/**`, `tests/**`, `verify.py`, `results/**`: implementation and
  certification chain; must remain byte-identical;
- `README.md`, `REPORT.md`: public/generated summaries; must remain
  byte-identical;
- all other tracked paths outside the authorized delta: protected by an
  aggregate pre/post manifest hash.

## Completion gates

- [x] thematic migration complete within stated scope;
- [x] all claim blocks and epistemic classifications preserved;
- [x] all relevant source links preserved and resolvable at the same scope;
- [x] no stable claim duplicated across thematic modules;
- [x] explicit pre/post audits agree;
- [x] protected tracked-file manifest hash unchanged;
- [x] durable-memory contract updated;
- [x] `git status --short` inspected;
- [x] complete tracked and untracked diff inspected;
- [x] direct whitespace check for untracked additions passed;
- [x] `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

The monolithic ledger is now a compact canonical index backed by six thematic
ledgers. All recorded claim blocks, classifications, source references, open
problems, limitations, and non-implications survived the migration; the
protected tracked-file manifest is unchanged. This is an editorial
preservation result, not a new mathematical proof or re-certification.

Exactly one next atomic task: independently review the migrated thematic
ledgers against the pre-migration `PROJECT_KNOWLEDGE.md` at the recorded base
HEAD and record acceptance or precise editorial corrections without reopening
any mathematical claim.
