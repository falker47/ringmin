# Evidence

## Environment and provenance

```text
repository_head=bfc2caff2ae6b1d1f149eb52cac4dc220dcf85d6
platform=Windows-11-10.0.26200-SP0 / PowerShell
python=3.14.3
symbolic_dependency=SymPy 1.14.0 (existing installation)
pdf_runtime=Codex bundled Python, pypdf, Pillow and Poppler
latex=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
task_mode=STRICT
```

The user supplied the accepted revision baseline and four mock-referee findings.
The mathematical code/data pin remains `6c16af422d1cb38641c62d43b6e0e547921b9ba9`.
The user explicitly exempted the pre-existing untracked public-v2 source ZIP.
No review registry was read or changed. All checks below were run locally in
this task; no hosted CI or new independent reviewer decision is asserted.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| A.5 threshold comparison | Explicit proof of an existing exact statement | Two positive reciprocal-square-root comparisons at the existing boundary | Analytic argument for every integer k>=1; bounded checker is supplementary |
| Finite brackets and counts | Reproduced computer-certified finite result | Complete unchanged verifier and fresh report | Independent of production/generator; reproduces the existing reviewer lineage |
| Seam scope and floating quantifiers | Existing exact theorems and qualified numerical descriptions, unchanged | Baseline section comparison and STRICT seam checker | No new onset, global-optimum contact, or uniqueness theorem |
| Two related-work descriptions | Source-supported attribution | Primary article definitions/intro and publication records in SOURCE_MAP | Context only, no new theorem or certificate premise |
| PDF fidelity and Git provenance | Engineering facts | Build manifest, rendering, diff and protected-path audit | Git content addressing does not imply permanent archival availability |

## Commands actually run and results

Commands use the repository root. Git uses command-local
`-c safe.directory=<repository-root>` for sandbox ownership, without persistent
configuration changes. `<bundled-python>` is the workspace runtime returned by
`load_workspace_dependencies`. Paths below are repository relative.

| Command/check | Exit/result | Property and limits |
|---|---|---|
| `git rev-parse HEAD`, `git status --short`, branch/remote reads | 0 after command-local ownership override; baseline matches, main/origin, only exempt ZIP initially | Establishes local starting state |
| `python --version` | 0, `Python 3.14.3` | Runtime identity |
| `python -I -S verify_global_brackets.py --output ops/TASK-20260919__dcg_presubmission_revision/global_brackets_verified.json` | 0, `PASS_GLOBAL_BRACKETS`, `pinned_input_verification: PASS`, 13 preserved files | Complete twelve-case certification and pinned binding; no historical-search replay or execution attestation |
| `python ops/TASK-20260919__journal_fixed_order_seam/check_exact.py --symbolic` | 0, all requested bounded and symbolic checks PASS | Existing exact/symbolic check independent of production; analytic proof remains the all-k authority |
| `python paper_assets/journal_dcg/build.py` (tool escalation) | 0, `18 pages; 0 overfull boxes; no unresolved references` | Two pdflatex passes, `-no-shell-escape`, metadata/hash generation |
| Same build repeated without source changes | 0, same output and identical PDF SHA-256 below | Local byte reproducibility only, not a cross-toolchain promise |
| `pdftoppm -r 85 -png paper_assets/journal_dcg/ringmin_dcg.pdf reproducibility/.work/journal_dcg/page` | 0, 18 PNG pages | Poppler render; inspected all pages in three contact sheets and enlarged pages 2, 15, 18 |
| `<bundled-python> ops/TASK-20260919__finite_journal_manuscript/inspect_pdf.py` | 0, `PASS: 18 Poppler pages, extracted text without unresolved references/replacement characters.` | Existing read-only PDF audit; extraction alone is not visual inspection |
| `pdfinfo paper_assets/journal_dcg/ringmin_dcg.pdf` | 0, 18 A4 pages, PDF 1.7, 400297 bytes, no JavaScript/encryption | Metadata, not mathematical or accessibility certification |
| `python ops/TASK-20260919__dcg_presubmission_revision/check_manuscript.py` | 0; exact PASS summary below | Transcription, baseline mathematical-text preservation, hashes, bibliography, protected paths and all new text whitespace; not independent acceptance |
| `git diff --check` | 0, no findings | Tracked whitespace; new dossier files additionally checked directly by the manuscript audit |

The exact verifier reports 908 angle intervals, 47 witnesses, 540 central
tangencies, 3,004 outer pairs, 6,008 angular inequalities, 268,648 explicit
full classes and 3,374,988,556 covered full classes. The
[fresh report](global_brackets_verified.json) retains every per-case endpoint,
coverage count, witness count, margin, strictness buffer and digest. The
manuscript checker compares every certificate case with this generated report.
An additional recursive comparison of the entire fresh report to the accepted
manuscript report differs only in `/seconds` (4.16834639996523 versus
3.743162000027951); every other field is identical.

The seam checker passes six rational bridges, 128 rank cycles, 128 parity-growth
matches, 30,976 directed fan identities, 512 exact boundary comparisons
(k=1,...,256), twelve independently enclosed roots, 670 positive directed
slacks and three negative seams. SymPy 1.14.0 checks the kernel derivatives,
three pocket identities, threshold algebra, arcsine estimate and pi integral.

Final manuscript audit output:

```text
PASS: 27 seam displays preserved, 21 tags, six vectors, 12 endpoint and coverage rows.
PASS: abstract 184 whitespace words; scope, source references, artifact hashes, UTF-8/whitespace.
PASS: protected tracked paths unchanged; exempt ZIP unchanged; only allowed task paths.
PASS: complete stored reproduction report bound to all twelve certificate rows and positive recorded margins.
PASS: mathematical body, arithmetic appendix, floating quantifiers and seam outside A.5 unchanged from revision baseline.
PASS: two explanatory displays, five resolved bibliography entries, revision provenance and Git wording.
LIMIT: transcription and scope audit, not independent mathematical review or hosted CI.
```

## Artifact and source checks

The [source map](../../paper_assets/journal_dcg/SOURCE_MAP.md) records the
related-work sources actually read and the editorial boundaries. Mathews-Zymaris
is supported by its author manuscript's flower definition and institutional
publication metadata. Collins-Stephenson is supported by the publisher abstract
and original article introduction/Section 1, pp. 233-235, read in a full-text
mirror. Only the original article text, not the mirror's automated description,
is used. Direct DOI/publisher opens sometimes returned errors; indexed publisher
records and accessible primary article text supplied the required information.

The [build manifest](../../paper_assets/journal_dcg/BUILD_MANIFEST.json) records
the revision baseline separately from the unchanged mathematical source commit,
every TeX/builder input hash, protected-source hashes, compiler and two passes.
The generation commit is the commit containing that manifest, discoverable by
file history. SOURCE_DATE_EPOCH=1789776000 and metadata suppression are unchanged.
PDF SHA-256, identical across both successful builds:

```text
115772f6fdab87f3cd2aa9340060b23347990dbaec7df24eb13442c2977e2fb4
```

Visual inspection covers every page, including the abstract (p. 1), related
work (p. 2), reproduction/declarations (pp. 9-10), A.5 comparison (p. 15),
bridge tables and bibliography (pp. 16-18). No clipping, overlaps, missing
glyphs or layout defects were found. The second PDF is byte-identical to the
rendered/inspected one. Compiler logs and images remain in ignored work storage.

## Failed checks and corrections

- Plain Git failed on sandbox ownership; scoped configuration resolved it.
  The sandbox's unreadable global-ignore warning does not hide the observed
  exempt ZIP; its hash is checked explicitly.
- Initial sandbox LaTeX exited 1 resolving AppData. Tool escalation ran the
  same builder successfully; no automatic approval rejection occurred.
- Three documentation patch attempts failed context checks before changing
  files. Corrected patches applied successfully.
- The new manuscript audit initially exited 1 on its display-count assertion:
  it compared with the proof-note display count, while accepted TeX already
  contains the extra classification-array display. Comparison now uses accepted
  TeX for the two added displays, preserving the separate 27-source-display gate.

## Final diff inspection and protected paths

The complete tracked text diff, new checker, status/log/evidence and generated
report were inspected. The checker parses the full report and independently
binds its material per-case data to the unchanged certificate. New files receive
direct UTF-8, final-newline and trailing-whitespace checks, since ordinary
unstaged Git diff omits them. The PDF was reviewed visually, not as binary diff.

Allowlisted changes are the seven revised journal files, this five-file dossier,
CURRENT_STATUS and the roadmap's finite-paper review entry. All other tracked
paths are compared with the accepted baseline, including public arXiv v1/v2,
the asymptotic sequel, solver, results, certificates, both verifiers, tests,
proof notes, prior dossiers and thematic ledgers. The journal's endpoint and
coverage tables, exporter and Git attributes are explicitly protected too.
No stable claim owner or index change is needed; no duplicate stable claim
was introduced.

The exempt untracked ZIP retains SHA-256
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`
and is excluded from staging. Only inspected paths are staged; staged diff and
whitespace inspection precede the authorized commit and normal push to
origin/main. Final commit/remote identity and remaining working-tree state are
reported in the handoff rather than inventing a circular self-commit reference.

## Residual uncertainty and handoff

No new mathematics, certificate logic or numerical search was introduced.
This is local reproduction and editorial verification, not independent review
or journal acceptance. No hosted CI, tag, release, archival DOI, cover letter
or submission is claimed. PDF bytes can differ under other TeX/font versions.

Exactly one next atomic task: independent review della pre-submission revision;
se accettata, freeze release/archival DOI.
