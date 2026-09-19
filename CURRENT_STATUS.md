# Current Status

```text
repository=falker47/ringmin
task=TASK-20260919__merge_global_bracket_verifier
observed_on=2026-09-19
mode=STRICT
state=READY_FOR_REVIEW
standalone=ARXIV:2609.13630_PUBLIC
corrective_original=ARXIV:2607.28654v2_PUBLIC
old_replacement=EDITORIALLY_SUPERSEDED
```

The authorized non-rewriting merge combines local c0075cf (including the STRICT
verifier implementation ff1a51b) with remote 5c98063. Only this status file
conflicted. The [merge dossier](ops/TASK-20260919__merge_global_bracket_verifier/TASK_STATUS.md)
records the resolution, checks and integration gates. The prior
[implementation dossier](ops/TASK-20260919__global_bracket_verifier/TASK_STATUS.md)
retains its historical rejected-push/blocker record.

## Verification state and gates

The standalone `python -I -S verify_global_brackets.py` checks all twelve
brackets and pinned original inputs, existential Cartesian witnesses,
recomputed intervals, DP/pruning digests and complete insertion coverage.
The claim and its limits remain in the unchanged
[proof note](research/GLOBAL_BRACKET_CERTIFICATE.md) and
[certification ledger](knowledge/CERTIFICATION.md#independent-exact-arithmetic-global-brackets).
It does not validate historical float64 pruning or settle journal readiness.

Merged-tree local checks passed: all twelve global brackets with pinned inputs,
44 STRICT regressions, 59 full-suite tests, the full historical n=3..14 verifier
including frontiers, the CI smoke command, lint and formatting. The parent-tree
audit preserves all 656 nonconflicting paths, 95 external source files and 13
selected originals. Exact commands/results are in the merge dossier.

READY_FOR_REVIEW describes the locally verified integration, not scientific
acceptance. Normal push and hosted CI are checked after the merge commit is
created; the exact SHA/run outcome is reported in the task handoff, never
inferred from these local results. The exempt untracked publication ZIP remains
untouched and unstaged. No generator replay or Stage A rerun occurs.

## Preserved publication and review context

The following publication/journal context is retained from remote 5c98063.
Its baseline transition and earlier verification counts are historical reports,
not a Registry read or acceptance decision in this merge task. This task does
not modify the Registry or advance the accepted baseline.

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

## Current integration boundary

No scientific choice is required by the status conflict. The independent
exact-arithmetic bracket route is integrated for review; the historical
numerical-certification audit, checkpoint-recovery notes and fixed-order seam
publication issue remain preserved in the remote journal dossier. The merge
does not declare those journal decisions resolved or begin a journal manuscript.

## Exactly one next atomic task

Independently review the final merge SHA and the STRICT global bracket verifier
integration, including the proof/evidence boundary. Scientific acceptance and
any later Registry decision belong to that separate review.
