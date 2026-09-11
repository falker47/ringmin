# Evidence

## Environment

```text
repository_head=5400dc12373be80456602f68aea785efc8fb6585
platform=Windows / PowerShell
python=3.14.3
dependency_source=standard library only; python -I -S
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Universal Section 9 method ceiling | Exact theorem | Proof Section 13 | Analytic proof; arithmetic checker independent of production | Only the specified scalar functional |
| q, endpoint D, pi and strict margin | Exact rational inequalities | Focused checker and explicit finite series/tails in proof | No production, third-party, prior-checker or result imports | Does not supply universal quantifiers by sampling |
| m=1 and weak/zero-width controls | Exact finite arithmetic controls | Focused checker | Independent of production | Corroborates, does not replace the analytic case split |

## Commands and checks

All checks below were run locally in this task under Python 3.14.3 or
PowerShell. Hosted CI and independent reviewer acceptance are not asserted.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | Actual runtime | Other environments |
| `python -I -S ops/TASK-20260911__shared_crossing_method_ceiling/check_method_ceiling.py` | 0; exact output below | Rational q/D/pi enclosures, margin, one-cutoff sign and weak-boundary controls | Universal quantifiers, supplied analytically |
| `python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 0; exact output below | Existing shared-energy/scalar/floor dependency controls | Full geometry or exhaustive certification |
| `python -O -I -S ops/TASK-20260911__shared_crossing_method_ceiling/check_method_ceiling.py` | 1; expected `RuntimeError: This checker requires enabled assertions; omit -O.` | Refusal to skip proof assertions | No arithmetic proof under `-O` |
| `git diff --check` with command-local safe.directory set to the repository root | 0; no output | Tracked whitespace | Untracked additions checked explicitly below |
| Read-only PowerShell here-string piped to `python -I -S -` | 0; four PASS lines below | Eight-path allowlist, original proof prefix, UTF-8/whitespace, 36 links/anchors | Mathematical correctness or hosted CI |
| Complete `git diff` and direct `Get-Content` of four additions | 0; inspected in full | Exact final change and all new file content | Independent mathematical acceptance |

The new checker's exact output:

```text
PASS rational Taylor root/sine gates: 0.19502009 < q < 0.19502010
PASS rational Machin gates: 3.14159 < pi < 3.14160
PASS 40-term integral/tail: 0.00241410289 < D(b) < 0.00241410290
PASS m=1 controls: positive/zero/negative F; unconditional H bound rejected
PASS m>=2 controls: adjacent equality, internal/endpoint zeros, H=0
PASS uniform ceiling U=8444510567073/5026544000000000000
PASS 1.68e-6 - U=83352927/5026544000000000000 > 0
PASS Section 13 arithmetic; universal quantifiers and scope use the proof
```

The separately run dependency checker's exact output:

```text
PASS 48 prescribed measures: equal marginals, strips, single E, up to 8 crossings
PASS 16 tour/cutoff cases: oriented mass, wrap, rotation, reversal, nesting, both parities
PASS boundaries and sharpness: d=h, cutoff endpoints, adjacent necessity, bounded-domain exception
PASS exact unseparated counterexample: 177/2500 > 7/100; excess 1/1250
PASS scalar signs, finite errors, 2-cutoff recovery, 4-cutoff domain, finite-floor negative control
PASS negative controls: independent budgets, on-grid cutoff, malformed parameters
PASS all finite shared-crossing checks; universal claims are analytic
```

The read-only inspection compared `git diff --name-only HEAD` plus
`git ls-files --others --exclude-standard` with the eight task paths;
compared the proof with `git show` at base HEAD using normalized newlines;
checked UTF-8 decoding, final newline and `line.rstrip()==line` for every
line of all eight files; and resolved every local Markdown target and
heading anchor in the seven Markdown files. Its exact output:

```text
PASS exactly 8 authorized changed paths; no protected/generated paths changed
PASS proof Sections 1-12 preserved as original normalized-text prefix
PASS UTF-8, final newline and explicit whitespace checks across all 8 paths
PASS 36 local Markdown links/anchors
```

The new checker uses only `fractions` and integer `math.comb/factorial`;
all comparisons are rational. Both checkers are independent of production
and saved results, but this is the author's local verification, not an
independent review of the new analytic proof. The Section 11/12 coefficient
checkers, pytest, the frontier verifier and paper build were not rerun:
their code, claims and artifacts are unchanged, and they do not test the
new functional ceiling. No dependency installation was needed.

## Artifact and provenance checks

Not applicable: no result/certificate or generated publication artifacts
are created or regenerated. The focused source checker has no external
inputs, random seeds, floating arithmetic or third-party dependencies.

## Failed checks and negative evidence

- Initial plain Git status failed on sandbox ownership. A command-local
  safe.directory override succeeded without changing persistent settings.
- The unconditional m=1 width-budget assertion is false; the proof must
  use F>0 before bounding that single width. The checker verifies the
  admissible beta=b, h=1/20 control: h>b-q but F<0 and eta=0.
- The `-O` run deliberately exits 1, as recorded above. The normal proof
  run exits 0. There are no unresolved failed mathematical checks.

## Final diff inspection

- Four tracked paths and the four new dossier/checker paths inspected in
  full; explicit whitespace checks include every previously untracked file.
- `git diff --check`: exit 0, no output. The proof's original Sections 1-12
  remain its unchanged normalized-text prefix.
- Exactly the eight TASK_STATUS.md paths changed. This checks preservation
  of `paper_assets/`, `results/`, `src/`, `tests/`, `verify.py`, `README.md`,
  `REPORT.md`, generated/publication assets, `AGENTS.md`, the compact index,
  other ledgers and prior dossiers. No protected/generated file changed.
- The arbitrary-finite-cutoff ledger entry is the single stable owner;
  roadmap/status route to the theorem, without a second thematic entry.
- Integration handoff: stage only these eight inspected paths, inspect
  `git diff --cached` and its whitespace check, commit and push normally
  to existing `origin/main`, then compare local/remote SHA and tree state.
  The final response records the resulting SHA and outcome; this file is
  the precommit evidence and does not claim a future push or hosted CI run.

## Residual uncertainty

The exact family supremum is not determined. No upper bound on another
coupled functional, the common-chain minimax, or full geometry follows.
Finite floor gates remain separate. No growing-m/infinite-cutoff transfer,
new certificate or hosted CI result is asserted. Independent mathematical
acceptance remains a separate review.
