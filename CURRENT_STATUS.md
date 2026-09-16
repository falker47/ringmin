# Current Status

    repository=falker47/ringmin
    task=TASK-20260916__journal_readiness
    observed_on=2026-09-16
    mode=STRICT
    state=JOURNAL_READINESS
    standalone=ARXIV:2609.13630_PUBLIC
    corrective_original=ARXIV:2607.28654v2_PUBLIC
    old_replacement=EDITORIALLY_SUPERSEDED

The standalone asymptotic sequel is public as
[arXiv:2609.13630](https://arxiv.org/abs/2609.13630).

The conservative corrective replacement of the finite paper is no longer a
candidate. The official arXiv notification received on 2026-09-16 states that
replacement submission `submit/8082087` for
[arXiv:2607.28654](https://arxiv.org/abs/2607.28654) **has been made public**.
The announced revision is dated 2026-09-15 10:14:17 GMT and describes the
12-page corrective v2 that preserves the certified finite results, corrects the
superseded v1 asymptotic conjectures, clarifies floating-circle quantifiers and
cites the standalone sequel.

Public HTTP mirrors/caches may temporarily continue to expose v1 metadata. A
stale page alone is not treated as an arXiv hold or rollback; the official
arXiv notification is the current operational publication-state evidence.

## Repository review baseline

The review-state registry was advanced on 2026-09-16 from
`227d09d480c2d88d09d3450c9015fc9737440c17` to
`98d6a6e340e4008ce35e789c54333ae43466b49d` after reviewing the seven-commit
delta. The delta is publication architecture, finalization, source bundles,
metadata, checks and task evidence; no new finite solver science was accepted
implicitly by the baseline update.

The final corrective dossier records a complete saved-evidence verification:
`python verify.py --start 3 --stop 14` reported `incumbent=PASS`, `local=PASS`
and `frontier=PASS` for every certified `n`, and the repository regression suite
reported 15 passing tests. These checks reproduce the saved evidence chain; they
do not rerun the historical exhaustive generation or replace external peer
review.

## Journal-readiness state

The public arXiv correction is frozen as publication history. Journal work is
being developed separately on `journal-readiness-20260916` rather than by
editing the public-v2 source in place.

The current internal mock review identifies two substantive pre-submission
blockers:

1. **Numerical certification boundary.** Historical pruning used float64 lower
   bounds with a stated `1e-10` global guard, calibration against 50-digit
   arithmetic and independent high-precision frontier verification, but not
   directed interval arithmetic for every excluded order. The journal version
   should either strengthen this to a rigorous worst-case numerical envelope or
   narrow the certification terminology precisely.
2. **Self-contained fixed-order seam result.** The corrective paper cites a
   pinned repository proof supplement for all-`n` fixed-order seam claims. The
   journal version should incorporate the needed proof, cite a stable
   publication-quality source, or remove claims that require the supplement.

Working primary venue: **Discrete & Computational Geometry**. Its scope directly
covers packing/configurations, geometric algorithms and geometrically flavored
combinatorial optimization. Alternatives retained are *Computational Geometry:
Theory and Applications* and *Discrete Applied Mathematics*.

See:

- `ops/TASK-20260916__journal_readiness/REFEREE_REPORT.md`
- `ops/TASK-20260916__journal_readiness/VENUE_AND_SUBMISSION_PLAN.md`

## Exactly one next atomic task

Resolve the numerical-certification blocker first: determine whether the saved
lower-bound/pruning evidence can be upgraded to a rigorous directed-error or
interval certificate without rerunning the complete multi-billion-order search.
Only after that decision should the definitive DCG journal manuscript be built.
