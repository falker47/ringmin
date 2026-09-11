# Evidence

## Environment

```text
repository_head=4510e5a9042603997deaab83bc553638b231306b
platform=Windows / PowerShell / Codex workspace sandbox
python=3.14.3
dependency_source=standard library only, isolated -I -S execution
task_mode=STRICT
```

## Claim ledger

Mathematical authority is `research/THREE_LEVEL_COMMON_CHAIN.md`, Sections
7-10. Stable ownership is the new arbitrary-finite-cutoff entry in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md` only.

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Adjacent width separation gives one shared E for any finite cutoff count | Exact theorem | Section 7, consecutive-block proof | Analytic; standalone direct atom scorer has no production imports | Checks do not prove universal quantifiers |
| The width condition is equivalent to unrestricted pointwise long charging | Exact theorem | Section 8, explicit witness for each violated adjacent inequality | Exact arithmetic corroborates unequal and equal widths | Necessity is on the whole real line, not a fixed grid or integrated bound |
| Removing separation invalidates the integrated lemma | Exact counterexample | Section 8 (22), 162-point grid coupling | Direct rational marginal, symmetry, strip and crossing counts | A reflected symmetric edge coupling, not a claimed single tour |
| Finite positive-part minimax and full-feasible transfer | Proved corollary | Section 9, existing stability inputs checked at each cutoff | Scalar/error checks independent of production | Fixed finite number of cutoffs; no tour recovery or sharp geometric coefficient |
| Macroscopic equality does not ensure finite separation | Exact negative control | n=104, actual gap 3/104<3/100 | Integer floors and rational arithmetic | Does not obstruct the weak-separation liminf corollary |

No stable claim is duplicated into another thematic module. The compact
index and existing numerical endpoint need no update. The roadmap change
only prioritizes independent review of this extension.

## Commands and checks

All results here were run freshly and locally in this task. From the
repository root in PowerShell:

For the portable Git command below, the executed setup was
`$ringminGitRoot = (Get-Location).Path.Replace('\','/')`; the command was
followed by `exit $LASTEXITCODE` to propagate its exit status.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | Interpreter version | Dependency correctness |
| `python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 0, output below; rerun after adding an explicit strip-bound equality check, again 0 | Exact prescribed measures, actual oriented cycles, multi-crossings, negative controls, scalar and floor gates | Universal proof, optimum certificates, full geometry |
| `python -O -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 1, expected `RuntimeError: This checker requires enabled assertions; omit -O.` | Fails closed with disabled assertions | Mathematical correctness |
| `python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py` | 0, output below | Independently reruns existing parameter/integral/finite gates and 12 prescribed couplings | External review of that theorem or a production certificate audit |
| `git -c "safe.directory=$ringminGitRoot" diff --check` | 0, no output | Tracked-diff whitespace | Untracked additions, checked separately below |
| Inline PowerShell here-string piped to `python -I -S -` | 0, audit output below | Explicit eight-path allowlist, all new-file whitespace, local links/anchors, AST imports, old proof prefix | Mathematical proof or hosted CI |
| `(Get-FileHash -LiteralPath ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py -Algorithm SHA256).Hash` | 0, source hash below | Exact local checker bytes | Mathematics |

The command-local Git safe.directory is the actual repository root;
startup ownership failure and successful retry are preserved in TASK_LOG.md.
No global Git setting changed. Read-only `git status --short`, complete
`git diff`, and direct `Get-Content` reads inspected all changed content.

New checker output (final rerun):

```text
PASS 48 prescribed measures: equal marginals, strips, single E, up to 8 crossings
PASS 16 tour/cutoff cases: oriented mass, wrap, rotation, reversal, nesting, both parities
PASS boundaries and sharpness: d=h, cutoff endpoints, adjacent necessity, bounded-domain exception
PASS exact unseparated counterexample: 177/2500 > 7/100; excess 1/1250
PASS scalar signs, finite errors, 2-cutoff recovery, 4-cutoff domain, finite-floor negative control
PASS negative controls: independent budgets, on-grid cutoff, malformed parameters
PASS all finite shared-crossing checks; universal claims are analytic
```

Existing three-level checker output:

```text
PASS rational Taylor gates: tau, q, pi
PASS finite domain, floors, cutoff separation and scalar sign gates
PASS exact integral gates: both cutoffs, 80 terms and moving-q error
2.6023553183e-7 < eta_3 < 2.6023553184e-7
5.5513553e-9 < eta_3-eta_split < 5.5513554e-9
PASS finite transfer gates: A_3 < 2.593263; n >= 10^12
PASS 12 prescribed grid couplings: marginals, strips, shared energy, both parities
PASS negative controls: independent budgets, on-grid cutoff, missing separation
PASS all three-level checks; analytic proof supplies all-order quantifiers
```

Inline audit output:

```text
PASS audit: 8 scoped files; whitespace including all new files; 26 local links/anchors
PASS imports: collections/fractions only, no floating literals; old Sections 1-6 preserved
PASS protected-path allowlist: no production, verifier, certificate, paper or generated changes
```

The inline audit formed the union of unstaged paths, staged paths and
`git ls-files --others --exclude-standard`, and required exactly the four
changed tracked documents plus the four dossier files. It read every file,
rejected trailing whitespace, tabs and extra/missing terminal newlines,
resolved relative Markdown targets and heading anchors, parsed checker
imports/constants with `ast`, and compared the old proof prefix against
`git show HEAD:research/THREE_LEVEL_COMMON_CHAIN.md` with line endings
normalized. These checks also explicitly cover the untracked additions.

Full `pytest`, `verify.py` smoke/frontier modes and paper builds were not
run: production, verifier, finite certificates and publication sources are
unchanged. No local check is reported as hosted CI or independent reviewer
acceptance; final-SHA hosted CI has not been inspected.

## Artifact and provenance checks

No result artifact, certificate, publication asset or generated figure is
created or changed. The checker source is the only computational deliverable.

```text
checker_sha256=3c12de7d153a653ba9794d1a6f054abe842497c01ec68659eafe1d381e3376d3
inputs=prescribed rational values in the checker source
randomness=none
production_imports=none
prior_checker_imports=none
```

The coarse q enclosure used by the new finite-domain gate is an explicitly
identified dependency input. The separately run prior checker proves its
Taylor enclosure rather than trusting the copied interval. No new numerical
coefficient, optimized width or saved-result dependency is introduced.

## Failed checks and negative evidence

Environmental failures were initial Git dubious ownership and a later
`safe.directory="$PWD"` shorthand that printed Git's not-a-repository
usage message. That compound read command ended with successful file reads,
so its overall exit 0 was not treated as a passing Git check. Explicitly
normalizing the repository path to forward slashes and propagating
`$LASTEXITCODE` gave exit 0 with no output, as recorded above. No index or
configuration mutation occurred in those reads. The prescribed -O failure
is intentional. Both normal checker runs passed;
no failed mathematical check was erased. Negative controls reject:
adjacent overlap in unrestricted pointwise charging; outermost-only
separation; unconditional integrated shared charging (exact excess 1/1250);
independent single-cutoff budgets spending E repeatedly; an on-grid cutoff
at tiny width; and using macroscopic equality as a finite floor guarantee.
An overlapping bounded-domain case succeeds, preventing overstatement of
necessity. No parameter search was used to generate or tune results.

## Final diff inspection

- `git status --short`: four scoped tracked modifications and this new
  four-file dossier, with no unrelated changes.
- Complete tracked diff and all four new files read; truncated display of
  the proof tail was followed by a direct full tail read.
- Analytical review checked the multi-crossing block, endpoint/split
  conventions, pointwise necessity witness, relaxed counterexample status,
  unchanged stability domain, scalar signs, floors and full deletion logic.
- All eight files passed explicit whitespace checks; tracked diff also
  passed `git diff --check`. All 26 local links/anchors resolved.
- Source AST contains only `collections` and `fractions` imports and no
  floating-point literals. The checker runs with -I -S.
- No protected/generated path changed: `AGENTS.md`, `PROJECT_KNOWLEDGE.md`,
  prior dossiers, `src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`,
  public overview/report and release metadata are outside the exact
  changed-path set. Existing proof Sections 1-6 are preserved verbatim
  apart from comparison-normalized line endings.
- Precommit handoff: final dossier/status deltas, staged inspection and
  cached whitespace check precede authorized normal commit/push. The final
  response records the actual SHA, remote result and post-push tree state;
  this evidence does not pre-claim those operations or hosted CI.

## Residual uncertainty

Independent mathematical acceptance and hosted CI for final HEAD remain
separate. No numerical improvement, tour saturation or finite optimum
certificate is claimed. Sharpness is limited to the unrestricted local
charging argument and the displayed aggregate scalar branches. Fixed-grid
necessity, optimal integrated constants and actual minimizing tours remain
unresolved; no infinite-cutoff or growing-m limit is asserted.
