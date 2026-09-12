# Publication History

This thematic ledger owns the separation between the immutable public
arXiv-v1 record and active post-publication knowledge.

## Public snapshot

The public snapshot is arXiv v1, `arXiv:2607.28654`. Its claims, tables, and
wording remain historical publication content. This knowledge migration does
not revise or back-project later results into that snapshot.

The bootstrap provenance for active durable knowledge remains the repository
snapshot recorded in the canonical index. Publication-facing source and
derived assets remain synchronized historical material and require a
dedicated `STRICT` revision task before any change.

## Current two-manuscript architecture, 2026-09-11

**Status:** standalone `ARXIV_SUBMISSION_CANDIDATE`, task `READY_FOR_REVIEW`,
unsubmitted and without external acceptance. Finalized on 2026-09-12 in the
[standalone finalization dossier](../ops/TASK-20260912__standalone_submission_candidate/TASK_STATUS.md).
The primary finite/Supnick reference remains the real public v1. Default
citation and `CITATION.cff` remain anchored to it.

- [Standalone asymptotic sequel](../paper_assets/asymptotic_sequel/README.md):
  *Minimum central circles: an effective characterization of the global
  asymptotic constant*. It presents the angular-to-line reduction, existence,
  effective balanced-word LP characterization, full geometric recovery and
  explicit endpoints. Historical finite algorithms and tables are cited only.
- [Conservative corrective v2](../paper_assets/v1_correction/README.md):
  *Arranging circles of radii 1,2,...,n around a central circle: a Supnick TSP
  and certified finite optima*. It preserves the historical finite core and
  corrects superseded conjectures and witness quantifiers. Its distinct
  publication state is `AWAITING_STANDALONE_ARXIV_ID`; no identifier is invented.

The [architecture dossier](../ops/TASK-20260911__publication_architecture/TASK_STATUS.md)
and [overlap/policy audit](../ops/TASK-20260911__publication_architecture/POLICY_AND_OVERLAP.md)
identify the separation and residual moderation risk. The exact eight-page
standalone source bundle and copy-ready metadata are the manual NEW-submission
handoff; server PDF inspection is required before finalizing. Only later,
if arXiv accepts a distinct
submission and assigns a real identifier, may a separate task replace the
corrective placeholder and rebuild/re-audit before submission. If moderation
requires versioning, prepare a genuinely integrated reference paper containing
both the finite core and asymptotic theory. The old nine-page candidate is not
that fallback. This sequence is documented, not executed.

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
containing commit. Historical TeX/PDF, derived assets and CITATION.cff are
unchanged. No arXiv submission, journal submission, tag or release occurred.

## Navigation by epistemic role

- The stable model reformulation is owned by
  [`DEFINITIONS.md`](DEFINITIONS.md).
- Published chain theory and later fixed-order results are owned by
  [`FIXED_ORDER_THEORY.md`](FIXED_ORDER_THEORY.md).
- The current status of the paper's heuristic and asymptotic statements is
  owned by [`GLOBAL_BOUNDS_ASYMPTOTICS.md`](GLOBAL_BOUNDS_ASYMPTOTICS.md).
- Published finite claims and their current evidence-chain limitations are
  owned by [`CERTIFICATION.md`](CERTIFICATION.md).

Historical publication wording controls only what arXiv v1 said. For current
mathematical detail, the proof note linked by the owning thematic ledger
controls.
