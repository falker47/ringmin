# Evidence

## Environment and exact capture

Windows, CPython 3.14.3; source checkout 13ddb41180b3911940f4fe5cf7d61c0545f9f834.

`python scripts/frontier_logs.py capture --source-commit 13ddb41180b3911940f4fe5cf7d61c0545f9f834`
exited 0: `PASS captured 12 original logs; 710353 archive bytes`.
`python scripts/frontier_logs.py check` exited 0:
`PASS 12 exact log archives; 9649682 original bytes; check only`.
Manifest records each uncompressed/archive hash and the generator source hash.
This preserves existing evidence; it is not a search rerun or new certificate.

The unmodified full verifier already passed all n=3..14 before this checkpoint.
The new path normalization retains the exact original frontier JSON and hashes.

## Negative and subsequent checks

Initial `python -m pytest tests/test_frontier_reproduction.py` exited 1 with
three fixture setup permission errors at the default temporary directory;
no new test body ran. Retry uses an explicit workspace temp directory and
`-p no:cacheprovider`. Complete commands/results and internal review follow.

The first explicit base-temp retry also failed before tests because its parent
directory did not yet exist. After creating the parent, the test fixture's
overbroad copy recursively copied its own temporary directory: two tests failed,
one passed. The source was narrowed to the archives directory, and only the
failed task-owned fixture was removed after resolving and checking containment.
`python -m pytest -p no:cacheprovider --basetemp=reproducibility/.work/pytest-repro2 tests/test_frontier_reproduction.py`
then exited 0: `3 passed in 0.68s`.

Independent review found a Windows drive-qualified path alias; the verifier
now rejects such paths, and three regression controls were added.
`python -m pytest -p no:cacheprovider --basetemp=reproducibility/.work/pytest-repro3 tests/test_frontier_reproduction.py`
exited 0: `3 passed in 0.44s`. The separate reviewer reran the corrected tests
and additional corruption/idempotency/path checks: see [INTERNAL_REVIEW.md](INTERNAL_REVIEW.md).

## Clean tracked-source gate

The exact gate implementation is [run_clean_export.py](run_clean_export.py).
It was executed as `python reproducibility/.work/run_clean_gate.py` before its
byte-identical preservation under this dossier. It exports tracked commit
13ddb41180b3911940f4fe5cf7d61c0545f9f834 with `git archive`, then copies only
the explicit task paths listed in [CLEAN_SOURCE_MANIFEST.json](CLEAN_SOURCE_MANIFEST.json).
The manifest hashes every input file. An assertion first checks that no
`results/checkpoints` directory exists. No ignored original log or editable
source tree is copied. Tests prepend that clean export's `src` through the
tracked conftest; the verifier and new checkers do not import production code.

This is a clean **source** reproduction using the installed pinned interpreter
and packages, not an isolated dependency reinstall. The documented assumption
is CPython 3.14.3 with requirements.txt installed. POSIX execution is untested.

Every command, full material output and exit code is retained in
[CLEAN_RUN.txt](CLEAN_RUN.txt). All ten commands exited 0:

- Restore: 12 exact archives, 9649682 original bytes, readback identical.
- Full pytest: `15 passed in 41.19s`.
- Smoke n=3..8: incumbent/local PASS for six sizes; frontier explicitly SKIP.
- Full n=3..14: incumbent/local/frontier PASS for all twelve sizes; n=14
  canonical coverage 3113510400. This is the independent certificate verifier,
  not a rerun of production enumeration.
- General-block checker, normal and `-O`: 30034 small orders, 580560 cells;
  18 rational-surrogate orders, 1080000 cells; 342 directed full-max and
  438 panel probes; four corruption controls reject.
- Line checker, normal and `-O`: 1089 words, 13995 independent paths,
  13941 pair/closure checks, 1089 concatenations, 94620 genuine-label
  quantiles; four negative controls reject.
- Word-LP checker, normal and `-O`: 1119 complete rational word inequalities;
  18 corrupt certificates reject. SciPy proposes candidates; rational arithmetic
  validates the certificates. Analytic proofs supply infinite quantifiers.

These checks preserve finite scope; they neither certify n>14 nor establish
the new analytic theorems by finite testing. The small exact LP brackets are
not asserted to improve the explicit endpoint interval.

## Integration checks

All text additions, manifest entries and compressed evidence were inspected;
each archive matches its original and both manifest hashes. Final staged
whitespace/content checks precede the normal checkpoint commit/push.
Original results/frontiers, optimum artifacts, production code and historical
publication assets have no task diff. Hosted CI is uninspected and unclaimed.
