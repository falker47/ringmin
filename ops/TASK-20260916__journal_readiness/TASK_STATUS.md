# TASK STATUS — Journal readiness

    repository=falker47/ringmin
    task=TASK-20260916__journal_readiness
    date=2026-09-16
    mode=STRICT
    state=IN_PROGRESS
    base=98d6a6e340e4008ce35e789c54333ae43466b49d
    branch=journal-readiness-20260916
    primary_target=Discrete & Computational Geometry

## Trigger

The official arXiv notification received on 2026-09-16 states that the
corrective replacement of `arXiv:2607.28654` by `submit/8082087` has been made
public. The arXiv-preparation phase is therefore closed unless a later official
message changes that state.

## Completed in this task

- reviewed the seven-commit delta from the previous accepted repository baseline
  `227d09d...` to `98d6a6e...`;
- accepted `98d6a6e...` as the new review baseline and recorded it in the Review
  State Registry with history preserved;
- reviewed the complete corrective-v2 manuscript as a mock referee;
- identified the main numerical-certification and self-containedness blockers;
- checked current journal scope/instructions and selected Discrete &
  Computational Geometry as the working target;
- preserved Computational Geometry: Theory and Applications and Discrete
  Applied Mathematics as alternatives;
- created `REFEREE_REPORT.md` and `VENUE_AND_SUBMISSION_PLAN.md`;
- advanced `CURRENT_STATUS.md`, `knowledge/PUBLICATION_HISTORY.md` and
  `paper_assets/v1_correction/README.md` from replacement-candidate language to
  public-v2 / journal-readiness language.

## Evidence boundary

The mock review is a journal-preparation exercise, not external peer review.
The historical finite-result verifier rechecks saved evidence and frontiers; it
is not a rerun of exhaustive generation. The official arXiv e-mail is the
current operational source for public-v2 state while public HTTP caches may lag.

## Open substantive blocker A — numerical certification

Determine whether the saved exhaustive-pruning evidence can be upgraded to a
rigorous worst-case numerical certificate without rerunning the full search.
The preferred solution is a directed-rounding/interval or analytic error bound
that validates every historical pruning comparison through the saved progress
and frontier evidence. If this cannot be done economically, narrow the journal
terminology so its exact numerical assumptions are explicit.

## Open substantive blocker B — fixed-order seam proof

Move the all-`n` fixed-order theorem needed by the finite paper into the journal
manuscript/appendix, or create a stable publication-quality source for it.
Avoid making the journal argument depend materially on a mutable repository
proof note.

## Human-only item

Create or confirm the author's ORCID at https://orcid.org/ and supply the exact
16-digit identifier. No ORCID is inferred from name matching.

## Next atomic task

Audit the historical pruning implementation and saved certificate structure for
an interval/directed-error upgrade path. Do not start the DCG journal manuscript
until this decision is made, because it controls the wording and strength of the
main finite-result claim.
