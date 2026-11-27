# Current status

```text
repository=falker47/ringmin
task=TASK-20261124__test_std_handle_inheritance
mode=STANDARD
state=READY_FOR_REVIEW
paper_i_base=review/p1-square-radii@91ce1cbf42543b6bcaea8ac94688c34d29066087
paper_ii_base=review/p2-square-radius-project@51dfc1b8c9ba02faa665cb20f60ce2d87f761c00
branches=fable/p1-test-std-handles, fable/p2-test-std-handles
replaces_status_on_paper_i_base=TASK-20261023__proposition7_supplement
replaces_status_on_paper_ii_base=TASK-20261121__p2_sidma_major_revision
observed_on=2026-11-27
```

## Current task and scope

Two existing tests failed intermittently in full local runs on Windows. Both
failures have one cause, recorded with tracebacks and controls in the
[evidence](ops/TASK-20261124__test_std_handle_inheritance/EVIDENCE.md) of the
[dossier](ops/TASK-20261124__test_std_handle_inheritance/TASK_STATUS.md).
Three test call sites let a child process inherit standard streams of the
pytest process. They no longer do: one in `tests/test_general_radii.py` on
the Paper I branch, and one each in `tests/test_line_upper.py` and
`tests/test_journal_p2_v4.py` on the Paper II branch.

## Verification gates and blockers

The failure was reproduced only when the interpreter was started through the
Python Install Manager alias, and it did not recur after the change: 100 and
60 repeated sessions, and three full sessions per branch. A recorder that
does not depend on the failure occurring lists one exposed test on the Paper
I line and thirteen on the Paper II line before the change, none after. The
Paper I generator was never reached in a failing run, and its output was
byte-identical to the committed certificates in every run made. No
manuscript, certificate, result artifact, generator, verifier or production
code was changed. Not verified here: POSIX, hosted CI, other builds of the
alias. No blocker.

## Exactly one next atomic task

Independently review the two test-only changes against their bases.
