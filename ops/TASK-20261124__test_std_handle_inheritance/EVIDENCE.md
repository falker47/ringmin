# Evidence

## Environment

```text
repository_head=91ce1cbf42543b6bcaea8ac94688c34d29066087 (Paper I base), 51dfc1b8c9ba02faa665cb20f60ce2d87f761c00 (Paper II base)
platform=Windows 11 Home 10.0.26300.10075, x64
python=3.14.3 (tags/v3.14.3:323c59a, MSC v.1944 64 bit), installed by the Python Install Manager
packages=pytest 9.0.2, mpmath 1.3.0, python-flint 0.9.0
dependency_source=other (packages already installed for the interpreter; nothing was installed in this task)
task_mode=STANDARD
```

The same interpreter is started in two ways throughout.

* **alias**: `python` on `PATH`, which is `%LOCALAPPDATA%\Python\bin\python.exe`.
  This is the Install Manager's alias, a 605,016-byte executable beside a
  `python.exe.__target__` file that names the runtime.
* **runtime**: `%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe`, the
  interpreter's own executable.

`sys.executable` is the runtime path in both cases. Every pytest command below
is `<launcher> -m pytest -p no:cacheprovider -o addopts=""`, with
`--tb=long -rfE` added for reporting. All runs are local. Each ran in a
detached worktree of the stated base, or in a worktree of the fix branch.

## Claim ledger

All claims are engineering facts about this environment unless marked.

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| C1. Every captured failure is `OSError: [WinError 6]` or `OSError: [WinError 50]`, raised in the pytest process inside `subprocess.Popen`, before the child exists. | engineering fact | 42 failing test instances in the logs: 31 with error 6, at `DuplicateHandle` in `_make_inheritable`; 11 with error 50, at `CreateProcess`. No other exception type occurs. | no | this machine only |
| C2. Under the alias, the process image is the alias executable, the C runtime reports application type 0, and `os.dup2` onto descriptors 0–2 leaves `GetStdHandle` unchanged. Under the runtime the image is the runtime executable, the type is 1, and `GetStdHandle` follows `os.dup2`. | engineering fact | host probe and descriptor probe below, one run per launcher; the application type was the same in each of the three runs of the minimal reproduction | no | one alias build |
| C3. While pytest runs under the alias, the three `GetStdHandle` values never change, the handles behind descriptors 0–2 change at every test phase, and at least one of the three Win32 values is not a live handle in most recorded snapshots. | engineering fact | six probed runs: one distinct `GetStdHandle` triple per run, 13 to 19 distinct descriptor triples, an invalid value in 171 to 188 of the 180 to 188 snapshots recorded per run | no | two test files of the Paper I line |
| C4. On Windows `subprocess.Popen` takes `GetStdHandle` for each stream left as `None`. | engineering fact | standard-library source, visible in the tracebacks | n/a | — |
| C5. C2–C4 produce C1: a stale value that names no handle gives error 6; one that names a handle the child cannot inherit gives error 50; otherwise the child starts with an unrelated handle and the test passes. | engineering fact for errors 6 and 50; inference for the third case | minimal reproduction without pytest, deterministic in three of three runs per launcher | yes: no pytest, no repository code | the third case was not inspected |
| C6. On the Paper I line one test reaches `GetStdHandle`; on the Paper II line thirteen do. After the change none does. | engineering fact | recorder runs below; the result does not depend on the failure occurring | yes: independent of launcher | Windows only |
| C7. The C runtime forwards `dup2` to `SetStdHandle` only when the application type is “console”. | inference | consistent with C2; the runtime source was not read here | no | unverified |
| C8. Output of `certify_radii.py --linear n` does not vary between runs. | engineering fact for the runs made | 40 runs for `n = 3`, 20 per launcher, and one run each for `n = 4,…,8`: every file is byte-identical to the committed blob | partly: comparison by SHA-256 against `git show` | `n <= 8`; this machine |

## Commands and checks

Counts are pytest sessions. Six of the 46 two-file sessions on the Paper I
base ran with the handle probe loaded; two of those six failed.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| Paper I base, alias, full suite, 7 sessions | 5 × `101 passed`; 2 × `1 failed, 100 passed` | the failure recurs; the failing test is the one named in the task | — |
| Paper I base, alias, `tests/test_frontier_reproduction.py tests/test_general_radii.py`, 46 sessions | 42 × `31 passed`; 4 × `1 failed, 30 passed` | the failure needs only these two files | — |
| Paper I base, runtime, the same two files, 40 sessions | 40 × `31 passed` | the failure depends on the launcher | absence in general |
| Paper II base, alias, full suite, 11 sessions | 11 × `110 passed, 1 skipped` | — | the twelve- and thirteen-failure sessions of the task did not recur |
| Paper II base, alias, `tests/test_line_upper.py`, 30 sessions | 25 × `14 passed`; 5 sessions with 6, 7, 7, 7 and 9 failures | the failure occurs with the file run alone; all 36 failures are `test_rejects_tampering` cases | — |
| Paper II base, runtime, `tests/test_line_upper.py`, 30 sessions | 30 × `14 passed` | the failure depends on the launcher | absence in general |
| Host probe (`GetModuleFileNameW`, `ucrtbase._query_app_type`), both launchers | alias: image is the alias executable, type 0; runtime: image is the runtime executable, type 1 | C2 | — |
| Descriptor probe: compare `GetStdHandle` with `msvcrt.get_osfhandle` before and after `os.dup2`, both launchers | alias: `GetStdHandle` unchanged while all three descriptor handles change; runtime: the two agree throughout | C2 | — |
| Minimal reproduction (below), 3 runs per launcher, plus one through the `python3.14` alias | alias: `stdin inherited -> OSError: [WinError 6]`, `stdin=DEVNULL -> child started`, every run; runtime: both lines `child started`, every run | C5, and that the remedy works | — |
| Recorder (below), runtime, full suite, both bases | Paper I: 1 test, streams `stderr,stdout`; Paper II: 13 tests, stream `stdin`; suites pass | which tests are exposed | — |
| Recorder, runtime, full suite, both fix branches | `INHERIT_COUNT 0` on both; `101 passed` and `110 passed, 1 skipped` | no test is exposed after the change; the suites pass with the runtime | — |
| Paper I fix, alias, the two files, 100 sessions | 100 × `31 passed` | no recurrence, against 4 failing sessions in 46 before | — |
| Paper II fix, alias, `tests/test_line_upper.py`, 60 sessions | 60 × `14 passed` | no recurrence, against 5 failing sessions in 30 before | — |
| Paper I fix and Paper II fix, alias, full suite, 3 sessions each | 3 × `101 passed`; 3 × `110 passed, 1 skipped` | the suites pass with the alias | — |
| Negative control for the rewritten Paper I assertion: the same call with `--linear 99` | return code 1; the assertion fails and shows `FAIL no published bracket for that n` | the test still fails when the generator fails | — |
| `certify_radii.py --linear 3`, 20 runs per launcher; `--linear 4` … `--linear 8`, one run each, runtime | every output has the SHA-256 of the committed blob | C8 | `n >= 9` |

The Paper II tests exposed before the change are the nine
`test_rejects_tampering` cases of `tests/test_line_upper.py` and
`test_figure_reproduction`, `test_build_and_fail_closed` and the two
`test_page_limit_excludes_bibliography` cases of `tests/test_journal_p2_v4.py`.
The second file is changed for that reason. Thirteen exposed tests agree with
the thirteen and twelve failures reported in the task, which I could not
reproduce as full sessions.

Skipped: `verify.py` and the paper builds outside the test suites, because no
file they read was changed. Hosted CI is not asserted.

### Minimal reproduction, without pytest

```python
import os, subprocess, sys
nul = os.open(os.devnull, os.O_RDWR)
os.dup2(nul, 0)  # what pytest's descriptor capture does to stdin
for label, kwargs in (("stdin inherited ", {}), ("stdin=DEVNULL   ", {"stdin": subprocess.DEVNULL})):
    try:
        subprocess.run([sys.executable, "-c", "pass"], capture_output=True, check=True, **kwargs)
        sys.stdout.write(label + "-> child started\n")
    except OSError as exc:
        sys.stdout.write(label + "-> %s: %s\n" % (type(exc).__name__, exc))
```

### Recorder, a pytest plugin loaded with `-p`

```python
import os
import _winapi

NAMES = {_winapi.STD_INPUT_HANDLE: "stdin", _winapi.STD_OUTPUT_HANDLE: "stdout",
         _winapi.STD_ERROR_HANDLE: "stderr"}
SEEN = {}
_original = _winapi.GetStdHandle

def _recording(ident):
    where = os.environ.get("PYTEST_CURRENT_TEST", "<outside a test>").rsplit(" (", 1)[0]
    SEEN.setdefault(where, set()).add(NAMES.get(ident, str(ident)))
    return _original(ident)

def pytest_configure(config):
    _winapi.GetStdHandle = _recording

def pytest_terminal_summary(terminalreporter):
    for where in sorted(SEEN):
        terminalreporter.write_line("INHERITS %s :: %s" % (",".join(sorted(SEEN[where])), where))
    terminalreporter.write_line("INHERIT_COUNT %d" % len(SEEN))
```

### Traceback excerpts

Paper I base, error 6:

```text
tests\test_general_radii.py:183:
>       subprocess.run([sys.executable, str(ASSETS / "certify_radii.py"), "--linear", "3",
                        "--output", str(output)], cwd=tmp_path, stdin=subprocess.DEVNULL, check=True)
...\Lib\subprocess.py:554:   with Popen(*popenargs, **kwargs) as process:
...\Lib\subprocess.py:1004:  errread, errwrite) = self._get_handles(stdin, stdout, stderr)
...\Lib\subprocess.py:1421:  errwrite = self._make_inheritable(errwrite)
handle = 400
>       h = _winapi.DuplicateHandle(
            _winapi.GetCurrentProcess(), handle,
            _winapi.GetCurrentProcess(), 0, 1,
            _winapi.DUPLICATE_SAME_ACCESS)
E       OSError: [WinError 6] Handle non valido
...\Lib\subprocess.py:1430: OSError
```

Paper II base, error 50:

```text
tests\test_line_upper.py:34:
>       assert cli(ROOT / "certificates" / "p1_n00006.json").returncode == 0
tests\test_line_upper.py:25:
>       return subprocess.run([sys.executable, "-I", "-S",
...\Lib\subprocess.py:554:   with Popen(*popenargs, **kwargs) as process:
...\Lib\subprocess.py:1038:  self._execute_child(args, executable, preexec_fn, close_fds,
>           hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
E                                    OSError: [WinError 50] Richiesta non supportata
...\Lib\subprocess.py:1552: OSError
```

The Windows messages are localized: “Handle non valido” is “The handle is
invalid”; “Richiesta non supportata” is “The request is not supported”.

## Artifact and provenance checks

Not applicable. No artifact, certificate, table, figure or PDF was generated
or modified in the repository. Generator output for C8 was written outside
the repository and compared by hash.

## Failed checks and negative evidence

* **The temporary-directory conjecture is not supported.** None of the 42
  captured failures originates in pytest's temporary-directory code, and the
  minimal reproduction fails in a single process with no pytest session at
  all.
* **The original Paper II sessions were not reproduced as such.** Eleven full
  sessions with the alias passed. The failure was reproduced with
  `tests/test_line_upper.py` alone, where at most nine tests can fail.
* **A byte comparison against the working tree misleads here.** With
  `core.autocrlf=true` the checked-out certificates have CRLF line endings,
  so a freshly generated file differs from the working copy and equals the
  committed blob. The test compares parsed JSON and is not affected.
* **Upstream.** One web search found no report of this launcher behaviour.
  That is not evidence that none exists.

## Final diff inspection

- `git status --short`: on `fable/p1-test-std-handles`, `tests/test_general_radii.py` modified; on `fable/p2-test-std-handles`, `tests/test_line_upper.py` and `tests/test_journal_p2_v4.py` modified; on both, `CURRENT_STATUS.md` modified and this dossier untracked.
- complete `git diff` inspected: yes, on both branches.
- untracked additions inspected directly or with a no-index diff: yes; the three dossier files were written in this task and read in full.
- direct whitespace check for untracked additions: `git diff --no-index --check` against an empty file, no finding.
- `git diff --check`: no finding on either branch.
- protected paths unexpectedly changed: none.
- generated files unexpectedly changed: none.

## Residual uncertainty

* C7 is an inference. Whether other builds of the alias behave the same way
  is unknown.
* A passing run under the alias proves less than it seems: the child may have
  started with an unrelated handle in place of a standard stream. After the
  change no child in the two suites inherits a standard stream.
* POSIX and hosted CI were not run. `subprocess` uses descriptors there, so
  the mechanism does not apply; the changed calls are valid on every platform.
* C8 covers `n <= 8` on one machine. It is not a certification statement.
