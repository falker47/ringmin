# Independent internal reproducibility review

    reviewed_on=2026-09-11
    mode=STRICT
    review_kind=fresh internal adversarial implementation review
    review_state=INTERNALLY_VALIDATED
    external_acceptance=not performed or implied

## Scope and implementation findings

The reviewer read the complete new archive utility, its manifest and tests,
and the narrow diff of `verify.py` against the current committed baseline.
The utility preserves historical bytes; it does not generate new search
evidence. Archive integrity does not establish search correctness. No
additional finite optimum or stronger certification scope is claimed here.

The archive reader requires the complete ordered coverage `3,...,14`, fixed
archive and target names, compressed SHA-256 values, decoded lengths and
decoded SHA-256 values. The resolved restore targets must remain within the
selected root. It validates every archive and every existing target before
writing any missing log. Exclusive creation prevents replacing an existing
file, and readback checks the restored bytes. Identical existing evidence is
accepted without rewriting it. Capture likewise preflights all existing
evidence before creating missing files.

The new verifier function preserves all existing prefix-completion parsing,
expected counts, missing-prefix decisions and downstream frontier checks.
Only the progress-log path handling changes. The verifier and archive utility
have no production Ringmin import, checked both statically and after loading
the modules. This review does not treat the archive manifest or an internal
PASS label as a replacement for the independent full verifier.

## Findings and corrections

1. The initial tests copied the complete `reproducibility` tree. A workspace
   temporary directory below `reproducibility/.work` therefore lay within its
   own copy source. The reviewer identified the recursion before launching
   tests; the builder independently observed the same failure. The corrected
   tests copy only `reproducibility/frontier_logs`. The reviewer inspected
   the correction and independently ran the tests successfully below.
2. Capture initially hardcoded its interpreter metadata as CPython 3.14.3.
   The reviewer requested dynamic metadata so a future runtime could not be
   mislabeled. The builder changed it to the actual Python implementation
   and version. The reviewer checked the current generator hash and recreated
   the full bundle in an isolated fixture: all archive and manifest bytes
   matched the corrected bundle. Existing compressed log bytes were unchanged.
3. The initial path normalizer treated `C:/results/...`, `C:results/...`
   and `C:\\results\\...` as relative PurePosix paths. Windows joining then
   aliased them to the fixture's valid relative log. Three independent probes
   returned `(True, [])` for these drive-qualified names, although the same
   helper rejected slash-prefixed absolute paths. No outside-root write
   occurred. The builder added `PureWindowsPath(str(relative)).drive` to
   the rejection guard and added all three regression cases. The reviewer
   inspected that correction, independently reran pytest and directly
   rechecked the formerly accepted names. All three now reject, while all
   24 original relative names with either separator spelling still pass.

All three findings are resolved in the reviewed implementation. No remaining
correctness finding was identified within this checkpoint's scope.

## Independently executed checks

Environment: local Windows PowerShell, Python 3.14.3. POSIX execution was not
available and is not claimed. Separator-normalization logic was inspected,
and both Windows and POSIX separator spellings were tested on Windows.

Exact pytest command:

```text
python -B -m pytest tests/test_frontier_reproduction.py -p no:cacheprovider --basetemp=reproducibility/.work/reviewer-frontier-pytest-20260911a
```

Exit code 0, material output:

```text
3 passed in 0.59s
```

After the drive-path correction, the independent final command was:

```text
python -B -m pytest tests/test_frontier_reproduction.py -p no:cacheprovider --basetemp=reproducibility/.work/reviewer-frontier-pytest-20260911b
```

It exited 0 with `3 passed in 0.63s`. A separate inline `python -B -`
probe used the original n=3 payload with each formerly accepted
drive-qualified name, then tested both relative separator spellings for
all 12 payloads. Explicit exception guards exited 0 with:

```text
PASS: all 3 formerly accepted drive-qualified paths rejected; all 24 original Windows/POSIX-spelled relative paths preserved.
```

The three tests cover restored original-prefix evidence, repeat restoration,
both separator styles, archive corruption, refusal to overwrite differing
existing evidence before creating earlier logs, and rejection of absent or
incorrect prefix-completion counts.

An additional inline command, `python -B -`, independently read and hashed
every original log and archive. It decoded every archive with `gzip`, checked
all manifest lengths and hashes, and reproduced compressed bytes using
`gzip.compress(..., compresslevel=9, mtime=0)`. The current generator's file
hash also matched the manifest.

All mutation fixtures were created exclusively under
`reproducibility/.work/reviewer-frontier-probes-20260911a`. The command checked
check-only behavior before any target existed, complete restoration,
idempotent restoration, 36 accepted relative-path variants, and six rejected
parent/absolute/UNC path variants. Its six archive/restore/capture controls
were: corrupted archive bytes, an existing different final log, a manifest
target with parent traversal, a wrong decoded-log hash, an invalid capture
commit string, and changed source bytes targeting already captured evidence.
Every expected rejection was checked explicitly, including absence of partial
restoration or evidence replacement. Capture was performed only in the
isolated fixture. Root originals were read before and after and were identical.

Exit code 0, complete material output:

```text
PASS 12 exact log archives; 9649682 original bytes; check only
PASS 12 exact log archives; 9649682 original bytes; restored/existing readback identical
PASS 12 exact log archives; 9649682 original bytes; restored/existing readback identical
PASS captured 12 original logs; 710353 archive bytes
PASS: 12 archive/original/generator identities; 36 valid path probes; 6 rejected path escapes; 6 rejected archive/restore/capture mutations; root originals unchanged; no production imports.
```

A second inline `python -B -` command loaded the committed `HEAD:verify.py`
through read-only Git, compared its prefix-check outcomes with the current
module on all 12 restored originals, and compared function ASTs. It exited
0 with:

```text
PASS: all 12 original prefix-verification outcomes unchanged; only progress_log_has_prefixes differs in the verifier function ASTs.
```

The raw Git commands initially encountered sandbox ownership checks. The
read-only comparison constructed a command-scoped safe-directory option from
the resolved workspace root; no Git configuration was changed:

```python
subprocess.run(['git', '-c', f'safe.directory={root.as_posix()}',
                'show', 'HEAD:verify.py'],
               text=True, capture_output=True, check=True)
```

## Limits and protected state

This reviewer did not rerun the complete frontier verifier or a historical
search. Full-verifier executions by the builder must be recorded separately.
Hosted CI and independent external acceptance were not inspected or claimed.
The archive check establishes byte identity to the preserved local evidence,
not authenticity beyond the recorded repository provenance.

The reviewer edited only this review record. Tests and capture/restore
mutations were confined to the ignored reviewer fixture directories. Root
logs, frontier JSON, optimum certificates, production code, the historical
paper and external review state were not changed by the reviewer.
