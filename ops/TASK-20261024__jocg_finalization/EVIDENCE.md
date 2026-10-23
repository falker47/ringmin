# Evidence

## Environment

```text
repository_head=fa32c99e9da0d639dca5735864c7c341d2e60059
platform=Windows; existing dedicated worktree
python=3.14.3
scipy=1.17.1
pytest=9.0.2
pdftex=3.141592653-2.6-1.40.28 (TeX Live 2025)
pypdf=6.14.2
dependency_source=existing environment matching requirements.txt
task_mode=STRICT
```

No agent capability or local dependency was installed. The existing TinyTeX,
Poppler, Python/Pillow/pypdf and PyYAML installations were used. Read-only GitHub
connector metadata confirmed PR #4 is open/draft on the intended branch and
expected SHA. Live git ls-remote matched. The dedicated worktree was clean;
the unrelated main checkout was inspected and left untouched.

## Claim Ledger

| Claim | Classification | Evidence | Independence / limitation |
|---|---|---|---|
| Provisional labels removed; approved JoCG destination recorded | Editorial fact / author decision | Source/PDF inspection and explicit user mission | No submission or external acceptance |
| Mathematical text and abstracts unchanged | Engineering preservation fact | check_scope.py compares complete baseline sources with an explicit editorial allowlist | Git baseline comparison, independent of mathematical checkers |
| S1 and published scientific files preserved | Engineering preservation fact | 796 tracked-file raw-byte hashes match preflight; protected Git delta empty | No re-certification of all scientific results |
| Existing bounded arithmetic passes | Independently rerun finite arithmetic, inherited analytic statements | Fresh aggregate --with-lp; exact Fraction checks and corruption controls | Independent of production solver, not a new independent proof review |
| PDFs/ZIP reproduce and package is intact | Engineering fact | Double isolated builds, extracted replay, repeated export and manifests | Compiler-coupled; cross-version byte identity not promised |

## Commands and Checks

All listed checks were freshly executed locally, exit 0 unless explicitly
identified as a negative control. Workdir is the dedicated branch root.
Logs/renderings are ignored scratch files, not package artifacts.

| Exact command/check | Material result | Property / limitation |
|---|---|---|
| git status --short; git rev-parse HEAD; git branch --show-current; git ls-remote origin refs/heads/codex/paper-ii-journal-candidate | Clean; fa32c99e9da0d639dca5735864c7c341d2e60059; intended branch and matching remote | Startup identity, not review acceptance |
| python -m pytest | 59 passed in 49.09s | Production regression suite; not global frontier certification |
| python -I paper_assets/paper_ii_journal/verify_math.py --with-lp | PASS bounded arithmetic replay; six LP cases; 1119 complete inequalities; 18 corrupt certificates rejected | Standard-library S1/upper checks and SciPy discovery with exact LP validation; no all-n proof by computation |
| python -I -S paper_assets/paper_ii_journal/build.py | PASS isolated build main/S2/lower: 9/13/14 pages, zero reference/box warnings | Three no-shell passes each; S1 PDF not replaced |
| python -I -S paper_assets/paper_ii_journal/check_reproducibility.py --require-delivered | PASS two isolated builds per document; delivered_match=True for all three | Six fresh external-directory compilations; exact hashes below |
| python -I -S ops/TASK-20261024__jocg_finalization/check_reproduction_controls.py | PASS extracted package; non-mutating double builds; seven negative controls | Final code, same PDF sources; later changes only editorial documents/manifest |
| python -I -S paper_assets/paper_ii_journal/build.py --export | PASS export: 37 archive files | 36 payloads plus inner manifest; deterministic ZIP timestamp/order/permissions |
| python -I -S paper_assets/paper_ii_journal/verify_package.py | PASS archive: 36 payload hashes; PASS candidate manifest: 24 payload hashes | Exact archive/source/S1 identity and source/PDF binding; no truth claim |
| python -I -S ops/TASK-20261024__jocg_finalization/check_scope.py | PASS complete main/S2 source equality apart from enumerated editorial substitutions; unchanged abstract hashes | Explicitly bounds every source change, not just theorem environments |
| python - probe: repeat export and compare ZIP/manifest bytes; extract final ZIP to TemporaryDirectory; execute its python -I -S verify_package.py | Byte-identical repeated export; final 36-payload manifest passes outside repository | No original repository inputs available to extracted verifier |
| python - probe: compare preflight SHA-256 for all protected tracked files; inspect original checkout HEAD/status and ZIP hash | PASS 796 protected files; original main and sole untracked ZIP unchanged | Local raw-byte preservation, independently of Git EOL normalization |
| python - probe: yaml.BaseLoader on both workflows, inspect triggers/steps | PASS YAML structure; one aggregate math step, no separate S1 step; push/path-filtered LaTeX; no uploads | Structural local check; runtime result requires hosted execution |

Aggregate line checks report 1089 rational words, 13995 independent paths,
13941 pair/closure checks, 1089 concatenations, 94620 genuine-label quantiles
and four rejected controls. S1 reports fresh certificate equality, 144 deletion
fixtures and integrity rejection controls. The five unchanged upper scripts
pass their finite rational scopes. These are rerun checks, not fresh universal
proofs or an expansion of the certified finite scope.

## PDF and Editorial Review

Executed `pdftoppm -r 85 -png <pdf> <ignored-prefix>` on main and S2. All 22
pages were inspected as rendered page grids: no clipping, overlapping text or
missing glyphs; dense equations and reference pages fit. Main/S2 have visible
page and line numbers, title-case section headings and 11pt single spacing.
A pypdf probe checked all page numbers, metadata, removed labels and embedded
fonts: 17 main / 18 S2 subsets, author Maurizio Falconi, correct titles. S1 was
not visually re-reviewed in this editorial task; its 14-page PDF is unchanged
and reproduced. It retains its original A4 format without line numbering.

Abstract content SHA-256 (between TeX delimiters, baseline equal):
- main: 0c2daa162666e39abb0769bfb81c9b253bc3040bd494561246a608839369b3fb
- S2: 42d430e7247eb4677dd3d224ce77fc6fd547df9355e5e28713bc91d7bdbd816d

The available v1 DOI was added while preserving its version URL. Other external
references already have DOI links; S1/S2 have no independently assigned DOI.
The AI acknowledgment, preprint references and author-supplied DAM disclosure
remain. No personal metadata was invented. Official JoCG indexed pages were
rechecked on 2026-10-24; direct requests returned redirect loops. URLs, review
versus camera-ready rules and the preserved-S1 qualification are recorded in
EDITORIAL_REQUIREMENTS.md. The actual portal abstract/private metadata remain
human actions; no submission or Registry access was attempted.

## Artifact and Provenance Checks

Generation source is this branch's editorial delta from the baseline above;
the Git commit containing the manifest identifies the delivered revision
without a circular self-SHA. Scientific snapshot and original S1 baseline stay
unchanged. Exact compiler/system-input hashes are in BUILD_REPORT.json.
SOURCE_DATE_EPOCH=1792713600 and FORCE_SOURCE_DATE=1 remain fixed for S1;
the editorial/ZIP revision date is 2026-10-24. No transient machine paths are
embedded. ZIP and manifests are regenerated by build.py, never hand-edited.

| Artifact | SHA-256 |
|---|---|
| main.pdf | 6e1a25f88529450621ee368d798a05fa0e525d3e8e36039b4422ce02fea28470 |
| upper_supplement.pdf | b2b24051c77e0da72a854e2e36903823bd328066c1f868dba1370bd864b8340b |
| BUILD_REPORT.json | a2722809fe80c05190b548ce19e89bbb569540b2e93bb12f1da80ce9b5cee55f |
| MANIFEST.json | e2906347ae1500047234e1463d27423ef4f895f18c65e4fcfc1f49b8b5494472 |
| source_bundle.zip | c815847df3b8f6cea17ae0ca04210a49f642abf1523bf15a7c314c3ea2f03ea2 |
| Preserved S1 supplement.pdf | a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568 |

## Failed Checks and Negative Evidence

Initial sandbox access to external-worktree Git failed; scoped escalations
succeeded. Template basenames without _TEMPLATE were absent; actual templates
were read. No scientific or build failure occurred. The official site produced
direct-fetch redirect loops; indexed official text supplied the requirements.

Negative controls intentionally returned nonzero: a changed main PDF fails the
strict reproduction gate and the package hash gate; a missing new checker
fails inventory equality; undeclared .tex/.aux/.out/.toc inputs fail recorder
closure. The task harness catches those expected failures and exits 0. No
corrupted data was written to the delivered package.

## Final Diff and Handoff Gates

The complete tracked diff and new files are inspected before staging. The
staged package bytes are additionally checked with `check_scope.py --staged`.
Final status/diff/whitespace results are appended to TASK_LOG.md before commit.
Only explicit editorial, reproduction, CI, status/roadmap and task-dossier
paths may be staged. No protected science, S1, mathematical checker or stable
knowledge ledger changed; no stable mathematical claim needs a new ledger.

Commit/push and exact-SHA hosted checks follow immutable content freeze. Their
actual SHA, push result and CI links belong in CHATGPT_CODEX_HANDOFF_V1; this
file does not claim future hosted success. Python CI remains push/PR; the new
LaTeX job runs only on relevant pushes, installs the required review-document
TeX packages separately and uploads no redundant artifacts. Its byte check is
within its own TeX environment and reports delivered-byte equality separately.

## Residual Uncertainty

No fresh independent analytical review or historical full-frontier verifier
run was performed: neither mathematical content nor certification code changed.
External peer review, novelty/suitability judgments, human portal metadata and
submission remain pending. Cross-version PDF bytes may differ. S1's preserved
format differs from main/S2 review formatting; any editor-requested derivative
must be separately versioned. No author approval is inferred from a CI pass.

Exactly one next atomic task: independent review of the finalized JoCG package
at the exact committed SHA before human submission.
