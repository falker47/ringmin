# Publication History

This thematic ledger owns the separation between the historical arXiv-v1
record, the current public corrective v2, and active post-publication knowledge.

## Current public finite-paper record

The current finite-paper record is
[arXiv:2607.28654](https://arxiv.org/abs/2607.28654). The official arXiv
notification received on 2026-09-16 states that replacement submission
`submit/8082087` has been made public. The announced corrective v2 is dated
2026-09-15 10:14:17 GMT, has 12 pages and 2 figures, preserves the finite
certified results, corrects the superseded v1 asymptotic conjectures, clarifies
floating-circle quantifiers and cites the standalone sequel
`arXiv:2609.13630`.

The original v1 dated 2026-06-25 remains historical publication provenance and
must not be silently rewritten. Public HTTP mirrors or cached arXiv views may
lag the official replacement notification; a stale v1 page is not by itself
evidence that the replacement was rolled back.

## Current two-manuscript architecture, 2026-09-16

**Status:** both manuscripts now have public arXiv records.

- [Standalone asymptotic sequel](../paper_assets/asymptotic_sequel/README.md),
  [arXiv:2609.13630](https://arxiv.org/abs/2609.13630):
  *Minimum central circles: an effective characterization of the global
  asymptotic constant*. It presents the angular-to-line reduction, existence,
  effective balanced-word LP characterization, full geometric recovery and
  explicit endpoints. Historical finite algorithms and tables are cited only.
- [Conservative corrective v2](../paper_assets/v1_correction/README.md),
  [arXiv:2607.28654](https://arxiv.org/abs/2607.28654):
  *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP
  and certified finite optima*. It preserves the finite core, explicitly
  retracts the superseded asymptotic conjectures, distinguishes existential
  floating placements from universal claims, and cites the standalone sequel.
  Publication state: `ARXIV_V2_PUBLISHED`.

The historical [publication-architecture dossier](../ops/TASK-20260911__publication_architecture/TASK_STATUS.md),
[overlap/policy audit](../ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md)
and [corrective finalization dossier](../ops/TASK-20260915__finalize_corrective_v2/TASK_STATUS.md)
record the state and checks at the time those tasks completed. They are not
retroactively rewritten merely because arXiv later made the replacement public.

The old nine-page replacement candidate remains historical provenance and is
not the recommended source for any future publication.

## Journal-readiness phase, 2026-09-16

The arXiv v2 source is now frozen as the public correction. Journal development
must happen in a separate manuscript rather than by editing the public-v2
artifact in place.

A strict internal mock-referee pass is recorded under
[`ops/TASK-20260916__journal_readiness/`](../ops/TASK-20260916__journal_readiness/REFEREE_REPORT.md).
The working primary target is **Discrete & Computational Geometry** because its
scope explicitly includes packing/configurations, geometric algorithms and
geometrically flavored combinatorial optimization. The two substantive
pre-submission blockers are:

1. make the numerical meaning of the finite global certificates fully robust
   for journal scrutiny — ideally by a rigorous worst-case directed/interval
   error envelope for pruning, otherwise by narrower terminology;
2. make the all-`n` fixed-order seam theorem used by the finite paper
   self-contained or cite it through a stable publication-quality source rather
   than relying on a repository proof supplement.

Venue and compliance details are tracked in
[`VENUE_AND_SUBMISSION_PLAN.md`](../ops/TASK-20260916__journal_readiness/VENUE_AND_SUBMISSION_PLAN.md).

## Superseded replacement strategy, 2026-09-11

**Status:** `EDITORIALLY_SUPERSEDED`. Its technical audit remains historical
evidence; this artifact is no longer a recommended upload or current candidate.
Its source, PDF, original source-only bundle and build evidence are preserved.

The source/PDF and reproducible build manifest are in
[`paper_assets/v2/`](../paper_assets/v2/README.md). The effective global
asymptotic theorem is central; its mathematical status remains owned by
[`GLOBAL_BOUNDS_ASYMPTOTICS.md`](GLOBAL_BOUNDS_ASYMPTOTICS.md), while the
fixed-order and finite-certificate owners retain their separate scopes.
The historical [final review packet](../ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md)
identifies the source supplement, claims, dependencies, checks and final
containing commit.

## Navigation by epistemic role

- The stable model reformulation is owned by
  [`DEFINITIONS.md`](DEFINITIONS.md).
- Published chain theory and later fixed-order results are owned by
  [`FIXED_ORDER_THEORY.md`](FIXED_ORDER_THEORY.md).
- The current status of the paper's heuristic and asymptotic statements is
  owned by [`GLOBAL_BOUNDS_ASYMPTOTICS.md`](GLOBAL_BOUNDS_ASYMPTOTICS.md).
- Published finite claims and their current evidence-chain limitations are
  owned by [`CERTIFICATION.md`](CERTIFICATION.md).

Historical v1 wording controls only what v1 said. The public corrective v2
controls the current finite-paper arXiv record. For post-v2 mathematical detail,
the owning thematic ledgers and proof notes remain the active repository source
until a journal manuscript freezes its own exact scope.
