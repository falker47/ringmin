# Global bracket evidence and complete verifier

Run from the repository root with Python >=3.11; no third-party dependency is
needed for the complete verifier:

```bash
python -I -S verify_global_brackets.py
```

Optional `--output path.json` creates a new result and refuses overwrites.
`--certificate path.json --mathematical-only` checks the full mathematical
claim and derived trace metadata, explicitly omitting original-input identity.
It has no smoke, skip-frontier or partial-case success mode.

The [proof note](../../research/GLOBAL_BRACKET_CERTIFICATE.md) defines the claim,
coverage, exact numerical guards and provenance limits. Run regressions with
`python -m pytest tests/test_global_brackets.py`; CI also runs the complete
default command. A test pass is not a replacement for that command.

`originals/` contains only 13 selected files from the supplied external STRICT
review package: candidate, received Windows JSON, generator as data, original
proof, independent review and programs, historical test reports, and three
essential negative fixtures. It is deliberately not a complete copy of the
original review directory; historical scripts may reference unarchived inputs
and are not the integrated command. New checks are in the repository root and
test suite. Existing reports retain their original status and wording.

[manifest.json](manifest.json) records original byte hashes and sizes;
`.gitattributes` disables newline conversion for these originals. This preserves
identity without treating manifests, filenames or PASS labels as proof.
`DELIBERATELY_INVALID_*` JSON files are falsification fixtures and **never valid
certificates**. The complete command checks their preservation, not their truth.

The SHA-256
`6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0`
identifies the canonical serialization of the **certificate field**, not the
candidate file's bytes. The original generator is retained for static CASES
binding only; it is never imported or replayed by the integrated verifier/tests.

Historical reviewer outcomes, current local results, hosted CI and independent
review of the integration commit are distinct evidence layers. This archive
does not promote a baseline or alter public results or manuscripts.
