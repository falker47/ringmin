# Task Status

```text
task=TASK-20260919__finite_journal_manuscript
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-09-19
updated_at=2026-09-19
accepted_baseline=6c16af422d1cb38641c62d43b6e0e547921b9ba9
```

## Objective

Prepare the first complete standalone finite Ringmin working manuscript for
Discrete & Computational Geometry, with its own source, PDF and reproduction
provenance under `paper_assets/journal_dcg/`.

## Scientific or engineering question

Publication integration of accepted exact theorems and computer-certified
brackets, not a new solver, certificate or extension of the finite scope.
Only `L_n < R*(n) <= U_n`, width exactly `10^-11`, is imported from the
exact finite certificate. The seam theorem includes the general criterion,
fixed-k persistence and the complete k=1,2,3 classifications.

## In scope and expected delta

- New journal manuscript, self-contained seam appendix, exact endpoint table,
  build/reproduction instructions and manuscript provenance.
- This dossier, CURRENT_STATUS, publication-history navigation and the
  materially changed roadmap priority.
- Read-only complete exact verification and manuscript transcription checks.

## Out of scope and protected paths

All public v1/v2 sources and assets, the asymptotic sequel, production solver,
results, certificates, verifiers, tests and existing proof notes are protected.
The existing untracked v2 publication ZIP is explicitly exempted by the user
in this task and must retain its bytes and remain unstaged.
No external submission, release, tag, PR, issue, or Registry change.

## Completion gates

- [x] Standalone manuscript and self-contained selected seam proof complete.
- [x] Exact global verifier and targeted existing checks pass locally.
- [x] Endpoint transcription, scope and protected-path checks pass.
- [x] PDF builds without unresolved references or layout defects; pages inspected.
- [x] Dossier, provenance and durable navigation updated.
- [x] Full new/modified files reviewed; direct and tracked whitespace checks pass.
- [x] READY_FOR_REVIEW; staged inspection and authorized integration are the
  final operation, with commit/push/remote results reported in the handoff.

## Blockers

None. User confirmed the ZIP exemption and absence of specific funding and
relevant competing interests. No ORCID was supplied and none is inferred.

## Handoff

The new artifact contains editable TeX, the 18-page PDF, a full seam appendix,
generated rational tables, build/export scripts, provenance manifest and
source map. Exact verification passed all twelve cases and 44 regression
tests; the seam checker and manuscript audit passed. Two builds yielded the
same PDF bytes. Protected paths and the exempt ZIP are unchanged. Independent
manuscript review, hosted CI and journal submission are not claimed.

Exactly one next atomic task: independent STRICT review of the complete
finite DCG manuscript and its evidence at the resulting committed HEAD.
