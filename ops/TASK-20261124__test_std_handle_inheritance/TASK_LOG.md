# Task Log

Append entries; do not erase failed attempts or contradictory evidence.

## 2026-11-24 10:18 — Startup

- repository HEAD: `review/p1-square-radii` at `91ce1cb`, `review/p2-square-radius-project` at `51dfc1b`, both fetched with explicit refspecs and confirmed with `git ls-remote`.
- working-tree state: clean; two detached worktrees created for the runs.
- files read: `AGENTS.md`, `PROJECT_KNOWLEDGE.md`, `CURRENT_STATUS.md`, the failure record in `ops/TASK-20261124__fable_proofcheck/EVIDENCE.md` on the two proof-check branches, the two test files, `paper_assets/general_radii/certify_radii.py`.
- task mode: STANDARD. No certificate or mathematical claim is touched.
- expected delta: none until a cause is established.
- known risks: mistaking an environmental failure for nondeterminism of the generator.

## 2026-11-24 10:22 — First reproduction

- action: one full session per base, alias launcher, output logged.
- result: the Paper I session failed with `OSError: [WinError 6]` at `subprocess.Popen` → `_make_inheritable(errwrite)`; the Paper II session passed.
- interpretation: the exception is raised before the generator starts, so the generator cannot be the cause.
- claim status: engineering fact.
- next step within the same task: find why a standard handle of the pytest process is invalid.

## 2026-11-24 10:25 — Handle probe

- action: a diagnostic plugin recorded `GetStdHandle` and the handles behind descriptors 0–2 around every test phase, six sessions of two Paper I test files.
- result: `GetStdHandle` never changes during a session; the descriptor handles change at every phase; two of the six sessions failed.
- interpretation: descriptor redirection does not reach the Win32 standard handles in this process.
- claim status: engineering fact.
- next step within the same task: test the same redirection outside pytest, with each launcher.

## 2026-11-24 10:30 — Cause

- action: host probe, descriptor probe and a minimal reproduction, alias against runtime.
- result: the alias hosts the interpreter in its own process image, with C-runtime application type 0; there `os.dup2` leaves `GetStdHandle` stale and the minimal reproduction fails every time. Under the runtime none of this happens.
- interpretation: one cause for both tests. The hypothesis I formed first for Paper II, that pytest keeps the Win32 handles valid, was wrong for this launcher.
- claim status: engineering fact; the role of the application type is an inference.
- next step within the same task: measure frequencies with and without the alias, and list the exposed tests.

## 2026-11-24 10:36 — Frequencies and exposed tests

- action: repeated sessions per base and launcher; a recorder plugin listing every test that reaches `GetStdHandle`.
- result: failures only with the alias; a second error, `[WinError 50]` at `CreateProcess`; one exposed test on the Paper I line, thirteen on the Paper II line.
- interpretation: the thirteen agree with the failure counts reported for Paper II. Eleven full Paper II sessions passed, so those counts were not reproduced as full sessions.
- claim status: engineering fact.
- next step within the same task: change the three call sites on two new branches.

## 2026-11-24 10:45 — Implementation

- action: `fable/p1-test-std-handles` from `91ce1cb` and `fable/p2-test-std-handles` from `51dfc1b`; three call sites changed.
- result: the recorder reports no exposed test on either branch; both suites pass with the runtime.
- interpretation: the children no longer depend on the standard streams of the pytest process.
- claim status: engineering fact.
- next step within the same task: repeated sessions with the alias after the change.

## 2026-11-24 10:50 — Generator check

- action: `certify_radii.py --linear 3` twenty times per launcher, and `--linear 4` to `--linear 8` once.
- result: my first comparison, against the working copy, reported every file as different. The working copy has CRLF line endings under `core.autocrlf=true`. Against the committed blobs every file is byte-identical.
- interpretation: the generator output did not vary; the first comparison was wrong.
- claim status: engineering fact for the runs made.
- next step within the same task: finish verification.

## 2026-11-27 09:00 — Verification

- command/check: alias, after the change: 100 sessions of the two Paper I files, 60 sessions of `tests/test_line_upper.py`, three full sessions per branch; negative control for the rewritten assertion; `git diff --check`.
- exit/result: every session passed; the control fails as intended; no whitespace finding.
- property checked: no recurrence, and the Paper I test still fails when the generator fails.
- limitation: this machine only; the work was interrupted between 24 and 27 November, and both bases were confirmed unchanged on resuming.

## 2026-11-27 09:05 — Handoff

- final state: READY_FOR_REVIEW.
- files changed: `tests/test_general_radii.py` on the Paper I branch; `tests/test_line_upper.py` and `tests/test_journal_p2_v4.py` on the Paper II branch; `CURRENT_STATUS.md` and this dossier on both.
- unresolved items: the reason inside the C runtime is inferred; no upstream report was found or filed.
- exactly one next atomic task: independently review the two test-only changes against their bases.
