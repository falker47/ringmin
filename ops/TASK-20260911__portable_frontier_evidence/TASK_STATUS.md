# Task Status

    task=TASK-20260911__portable_frontier_evidence
    mode=STRICT
    state=READY_FOR_REVIEW
    base_head=13ddb41180b3911940f4fe5cf7d61c0545f9f834

## Objective and scope

Make the existing full n=3..14 certificate audit reproducible from tracked
files by preserving exact historical logs, restoring them with hash/readback
checks, and interpreting their existing Windows paths portably. Preserve
certificate payloads, production search and historical paper unchanged.

## Gates

- [x] Byte-identical, deterministic archive capture and restoration.
- [x] Corruption and overwrite failures tested; no weakened frontier check.
- [x] Independent internal implementation audit.
- [x] Full tests and full verifier from a tracked-source clean copy.
- [x] Provenance/ledger updates; final diff inspection precedes integration.

## Blockers and handoff

No blocker. Default pytest temp ownership fails in this sandbox; use an
explicit task-local base temp path and disable its unrelated global cache.
Continue the goal to publication consolidation after this checkpoint.

Integration commit is identified in the goal's final packet. Internal review
is complete; independent external acceptance is pending.
