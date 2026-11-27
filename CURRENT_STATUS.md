# Current status

```text
repository=falker47/ringmin
tasks=TASK-20261124__fable_proofcheck, TASK-20261124__test_std_handle_inheritance
mode=STRICT (proof check), STANDARD (test change)
state=READY_FOR_REVIEW
paper_i_branch=review/p1-square-radii (PRs #23 and #26 merged)
paper_ii_branch=review/p2-square-radius-project (PRs #24 and #27 merged)
observed_on=2026-11-27
```

## Current task and scope

Two completed tasks were merged into both review branches at the author's
request on 2026-11-27.

- **Proof check.** An independent check of Paper I (angular reformulation
  through the seam criterion, with Appendices A–C) and of lemmas L1–L8 in
  supplement S1 of Paper II. The [report](docs/referee/proofcheck-2026-11.md)
  lists every statement with its verdict and evidence. The
  [checks](independent_check/fable_proofcheck/README.md) run with
  `python -I -B independent_check/fable_proofcheck`. The
  [dossier](ops/TASK-20261124__fable_proofcheck/TASK_STATUS.md) and its
  [evidence](ops/TASK-20261124__fable_proofcheck/EVIDENCE.md) record the
  commands and their limits.
- **Test isolation.** Three test call sites no longer let a child process
  inherit standard streams of the pytest process: one in
  `tests/test_general_radii.py` on the Paper I line, and one each in
  `tests/test_line_upper.py` and `tests/test_journal_p2_v4.py` on the Paper
  II line. The [dossier](ops/TASK-20261124__test_std_handle_inheritance/TASK_STATUS.md)
  and its [evidence](ops/TASK-20261124__test_std_handle_inheritance/EVIDENCE.md)
  record the cause and the controls.

## Verification gates and blockers

The proof check found no error and no gap. With the author's approval on
2026-11-24 the four imprecisions were reworded in separate commits, each with
its regression test, `MATH_DIFF.md` and rebuilt PDF; the five style remarks
were not applied. The test change touched no manuscript, certificate, result
artifact, generator, verifier or production code. Hosted CI passed on the
four PR heads `dd2c06e`, `2ec4e9e`, `5a1d8b4` and `3ec3e64` before merging.

Merging is the author's integration decision, not an independent review;
the test change has not been independently reviewed. Not verified: cited
sources, certificates, upper witnesses for `n >= 8`, square-radius results,
other builds of the Windows Python alias. No blocker.

## Exactly one next atomic task

Independent review of the explicit convergence-rate theorem in Draft PR #25
(`research/fable_sprint_2026-11/NOTE_QUANTILE_RATE.md`), before it is
proposed for the SIDMA draft of Paper II.
