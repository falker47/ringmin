# Task Status

```text
task=TASK-20261124__test_std_handle_inheritance
mode=STANDARD
state=READY_FOR_REVIEW
started_at=2026-11-24
updated_at=2026-11-27
paper_i_base=review/p1-square-radii@91ce1cbf42543b6bcaea8ac94688c34d29066087
paper_ii_base=review/p2-square-radius-project@51dfc1b8c9ba02faa665cb20f60ce2d87f761c00
branches=fable/p1-test-std-handles, fable/p2-test-std-handles
```

## Objective

Find why two existing tests failed intermittently in full local runs on
Windows, and repair them only if the defect lies in the test or in the code
under test.

## Scientific or engineering question

An engineering question; no mathematical claim is involved.

1. `tests/test_general_radii.py::test_linear_generator_reproduces_tracked_certificate_from_a_clean_checkout`
   failed in one of four full runs on the Paper I line. Does anything in the
   generator `paper_assets/general_radii/certify_radii.py` or in the test vary
   between runs?
2. Twelve to thirteen tests failed with a Windows `OSError` in two of eight
   full runs on the Paper II line. Which error is it, and where does it come
   from?

## In scope

- `tests/test_general_radii.py` on `fable/p1-test-std-handles`;
- `tests/test_line_upper.py` and `tests/test_journal_p2_v4.py` on
  `fable/p2-test-std-handles`;
- this dossier and `CURRENT_STATUS.md` on both branches.

## Out of scope

- manuscripts, certificates, `results/`, generators, verifiers and production
  code: none is changed;
- the interpreter launcher whose behaviour triggers the failure: it is outside
  the repository;
- the knowledge ledgers: a text is proposed below and left to the reviewer.

## Expected delta

Three test call sites stop passing the standard streams of the pytest process
to a child process. Each asserts the same thing as before.

## Protected paths potentially affected

None. `paper_assets/general_radii/certify_radii.py` and the tracked
certificates were read and executed, with output written outside the
repository; `git status --short` shows no change to them.

## Completion gates

- [x] implementation complete within stated scope;
- [x] claims classified correctly;
- [x] relevant tests run;
- [x] relevant independent verification run (a recorder that does not depend on the failure occurring);
- [x] artifacts/provenance checked when applicable (no artifact is produced);
- [x] durable memory updated (this dossier; ledger text proposed, not applied);
- [x] `git status --short` inspected;
- [x] complete `git diff` inspected;
- [x] `git diff --check` passed;
- [x] no incidental generated/protected-file changes;
- [x] state set to `READY_FOR_REVIEW`.

## Blockers

None.

## Handoff

Both failures have one cause, reproduced with complete tracebacks. The
generator is not involved: in every failing run the exception is raised in
the pytest process, inside `subprocess.Popen`, before a child process exists.

The trigger is outside the repository. When the interpreter is started through
the Python Install Manager alias (`python` on `PATH`), redirecting file
descriptors 0–2 does not update the Win32 standard handles. pytest redirects
them around every test phase, so the Win32 values go stale. A test that leaves
a standard stream of its child unset makes `subprocess` duplicate a stale
handle. This raises `[WinError 6]` or `[WinError 50]`, or it silently hands
the child an unrelated handle, depending on what the operating system has
since done with that handle value. Started from the interpreter's own
`python.exe`, the same suites did not fail.

The defect on the repository side is that three test call sites depended on
those inherited streams without needing them. They now pass
`stdin=subprocess.DEVNULL` and capture both output streams, as the other
subprocess calls in the suites already did. See [EVIDENCE.md](EVIDENCE.md).

**Reproducibility of the Paper I generator.** Not affected. Forty runs of
`certify_radii.py --linear 3`, twenty per launcher, each wrote a file
byte-identical to the committed `linear_03.json`; one run each for
`n = 4,…,8` did the same.

**Residual uncertainty.** The link between the launcher and the missing handle
update is measured; the reason inside the C runtime is an inference. One web
search found no upstream report. POSIX was not run.

**Proposed ledger text** for `knowledge/IMPLEMENTATION.md`, not applied:
“Test subprocesses pass `stdin=subprocess.DEVNULL` and capture both output
streams. A child that inherits a standard stream from the pytest process can
fail to start on Windows when the interpreter runs through the Python Install
Manager alias; see the
[dossier](../ops/TASK-20261124__test_std_handle_inheritance/EVIDENCE.md).”

**Next atomic task.** Independently review the two test-only changes against
their bases.
