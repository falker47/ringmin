# Evidence

## Environment

```text
repository=falker47/ringmin
base_head=4303fe4d937c5f2c7915070a0aaffa67f9b448ca
branch=codex/ringmin-editorial-review
platform=Windows / PowerShell
python=Python 3.14.3
compiler=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
renderer=pdftoppm 26.07.0
pdf_text=pypdf from the bundled Codex Python runtime
task_mode=STRICT
integration=local_commit_only_no_push
```

All paths below are repository-relative. Commands ran in the user-selected
worktree. No machine-specific absolute path is embedded in delivered artifacts.
The original startup entry and snapshots were already present when this
continuation inspected the worktree: six tracked task changes and this untracked
dossier. Their content matched this exact authorized task; no unrelated change
was found or overwritten. HEAD remained the supplied base. Fresh checks below
are distinguished from that inherited startup record.

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Exact requested source text | Engineering fact | Both supplied raw/LF SHA-256 pins; exact diff; source scope check | Read-only comparison with baseline Git blobs and user pins; not mathematical truth |
| Formulas, statements/proofs and disclosures preserved | Engineering fact | Scope checker and negative controls; separate read-only agent check | Parser shares the earlier task's extractor; exact whole-source pins and human diff provide separate checks |
| PDFs match the approved source build | Engineering fact | Two fresh three-pass builds per paper; recorder closure; same PDF bytes and recorded inputs | Production-coupled compilation, local toolchain only |
| S1/S2 and public/scientific assets preserved | Engineering fact | Full tracked inventory; 20 supplement hashes; complete supplement record equality | Hash comparisons do not re-prove their contents |
| Package coherent | Engineering fact | Unmodified build-report validator and package verifier; paired manifest check | Integrity/provenance only; no scientific acceptance |
| Removed chronology | Historical statement | PAPER_I_PROVENANCE.md, verbatim baseline text | No current submission or accepted-baseline verification |

## Commands and exact material results

Freshly executed in this continuation; all successful commands below exit 0.

- `git status --short`, `git rev-parse HEAD`, `git branch --show-current`,
  `git hash-object paper_assets/journal_dcg/ringmin_dcg.tex paper_assets/paper_ii_journal/main.tex`:
  HEAD and branch as above; modified source blobs `af64e35da089d21e51262d94778ad1806963c3e5`
  and `c4b52264250a4e740f80ba24349ef337c14544af`.
- `python ops/TASK-20261107__two_paper_approved_refinements/approved_build.py build`:
  `revised paper_i: 18 pages; 0 final-log warnings`; repeat same;
  `revised paper_ii: 9 pages; zero final-log warnings`; repeat same;
  `PASS main-only delivery, repeated builds and validate_build_report`.
- Copied `approved_build.py` to
  `reproducibility/.work/approved_refinements_20261107/export_approved_tmp.py`,
  then ran `python reproducibility/.work/approved_refinements_20261107/export_approved_tmp.py export --root .`.
  Final result after documentation synchronization:
  `PASS export: 39 archive files; archive SHA256 81923e4e76aaaed8180e3d3059d87adbe07022c0782b901ce24dba68f97bde50`.
- `python ops/TASK-20261107__two_paper_approved_refinements/approved_build.py verify`:
  `PASS preserved 20 supplement files, full inherited records, and paired manifest context`.
- `python paper_assets/paper_ii_journal/verify_package.py`:
  `PASS archive: 38 payload hashes; current-source and reused-supplement identity`;
  `PASS candidate manifest: 26 payload hashes; lower-supplement provenance`.
- `python ops/TASK-20261107__two_paper_approved_refinements/check_approved_scope.py`:
  Paper I: 19 protected environments, 249 delimited formulas, 16 math environments;
  Paper II: 14 protected environments, 268 delimited formulas, 11 math environments;
  both supplied source hashes match, all formula/proof/disclosure negative controls detected;
  `PASS protected inventory: 857 tracked files byte-identical; exact baseline inventory 869 files`;
  `PASS scope, historical paragraph, saved original report, full supplement records and inherited context`.
- `pdftoppm -f <p> -l <p> -scale-to 1600 -png -singlefile <pdf> <prefix>`:
  Paper I pages 2, 9, 10, 11, 18 and Paper II pages 1, 2, 3 rendered successfully
  and inspected visually. No clipping, overlap, unresolved references or missing
  glyphs observed. Paper I's release commit continues from page 9 onto page 10;
  all chronology, declarations and final references remain present and readable.
- Bundled Python inline `PdfReader` extraction of all pages, whitespace-normalized
  phrase checks: `PASS paper_i: 18 pages; all requested extracted-text spot checks`;
  `PASS paper_ii: 9 pages; all requested extracted-text spot checks`.
  Checks covered the contribution sentence, archival wording, data/code statement,
  normalized-radii abstract text, endpoint sharpness sentence and Theorem 5 pointer.
- Inline Python compared `source_bundle.before.zip` byte-for-byte with
  `git show 4303fe4d937c5f2c7915070a0aaffa67f9b448ca:paper_assets/paper_ii_journal/source_bundle.zip`:
  `PASS original ZIP preserved: 98de8db15430ded9c2ab3e82f0d0ca94ac10e6e09db15512a5dac32a63de3c8b`.

The separate read-only agent executed two inline Python checks (both exit 0)
reconstructing exactly 3 Paper I and 4 Paper II approved replacements from the
baseline. It confirmed both baseline blobs, both raw/LF source hashes, all formal
invariants, the complete historical paragraph, all 20 supplement hashes directly
against baseline Git bytes, and both full inherited records and original compiler
contexts. This is fresh local cross-checking, not the continuous reviewer's
acceptance decision or a mathematical certification audit.

## Artifact and provenance checks

Source and PDF SHA-256 values, final package hashes and inspected pages are in
FINAL_ARTIFACT_CHECKS.json. SOURCE_HASH_COMPARISON.json records the supplied source
hashes; the fresh scope check confirms them. BUILD_REPORT.before.json is the full
pre-edit report and is checked against the baseline Git object. The initial
tracked inventory covers all 869 baseline paths; no old dossier was modified.

Paper I uses the existing isolated builder through the task wrapper and records
all four local TeX inputs and TeX system inputs. Its computation commit, archived
release commit and DOI are unchanged. The complete removed historical paragraph
is preserved in PAPER_I_PROVENANCE.md.

Paper II uses `runpy.run_path(build.py)` and calls only
`compile_document(package / "main.tex")`, twice. Neither full build nor
`--document main` was used. The saved report is copied and only `documents.main`
is replaced. Both supplement records, including S1's preserved-PDF metadata,
remain equal to the saved report. `build_context_by_document` identifies the
current main compiler (TeX Live 2025) and the inherited supplement check-build
context (TeX Live 2023/Debian). The top-level historical environment is explicitly
scoped; it does not claim a current all-document build.

The export wrapper is outside the package and temporarily overrides the factory
used by `export()`. Both manifests have date 2026-11-07, editorial base 4303fe4,
and main-recompiled/supplements-reused provenance. The unchanged exporter still
uses 2026-11-03 as its deterministic ZIP-member timestamp; this packaging constant
is not the manuscript or generation date. The original ZIP is retained in ignored
work storage and in the baseline Git history. The named approved-refinements ZIP
and patch were not found in the attachment area, Downloads or either relevant
checkout (`rg --files` with their exact names: exit 1, no matches); the verified
source delta supplies the directly applied approved text.

Build logs, recorder files, renderings and text extraction are in ignored
`reproducibility/.work/approved_refinements_20261107/`. Compact full input/output
hash records are tracked in this dossier. PDF identity was reproduced within
this local environment; different toolchains can change bytes and pagination.

## Failed checks and negative evidence

Sandboxed Git initially returned worktree-access errors; explicit authorized
escalated commands succeeded. The app could not attach a worktree owned by
another chat; all operations used the explicit requested path. No Git
configuration or ownership was changed.

`pdftotext` was absent from PATH and the bundled Poppler directory. The compound
PowerShell invocation still exited 0 after later successful commands; that is
not counted as successful text extraction. Bundled pypdf then completed the
separate text checks. No dependency was installed. The original broader task's
whole-declarations invariant was not weakened: the new checker allows only the
exact approved availability passage and the one new `thm:lp` reference, and
requires the complete user-approved source hashes.

The first export passed with SHA-256
`f1c77a0d710cd4a28f2f074646a152d481b109ecb237db236dcc890cd6b0b6a5`.
The final export differs solely because README/readiness pointers were then
synchronized. Both export results are retained here to avoid concealing chronology.

## Final diff inspection

All tracked source, metadata and accompanying-document diffs have been read.
All 17 untracked files were inspected in full; large JSON records were completely
parsed and validated. `git diff --check` and an explicit untracked whitespace/EOF
scan passed (exit 0). Staged checks are recorded in TASK_LOG.md before commit.
Only the approved two-paper outputs, three synchronized accompanying documents,
CURRENT_STATUS.md and this dossier are permitted. Protected paths include
`paper_assets/ringmin_paper.*`, public correction/sequel/deposit assets,
`paper_assets/asymptotic_sequel/proposition7_supplement/`, S2 and its checkers,
`results/`, scientific `src/` and verifier files, proof notes, ledgers and older
dossiers. The full hash inventory, not this illustrative list, defines coverage.

## Residual uncertainty

No solver tests, mathematical verifier, S1/S2 compile, hosted CI, current journal
submission query, Registry query or external independent-review acceptance was
performed. All mathematical claims retain their prior epistemic status. The
hand-off is READY_FOR_REVIEW after a local scoped commit, with no push as requested.
Exactly one next atomic task: independent editorial/provenance review of that
local commit.

## Closing read-only content audit

The separate agent's closing command exited 0. It validated every one of the
869 initial hashes against baseline Git bytes: 155 exact and 714 expected
LF-to-CRLF checkout conversions. All retained build logs and records agree with
the delivered PDFs, 118 actual Paper I TeX-system hashes and 113 Paper II hashes.
All 11 final artifact hashes and all 20 supplement hashes match. All 17 new
dossier files were read completely, including full JSON field/inventory checks;
no private absolute path, whitespace issue or substantive finding was reported.
This local editorial audit is separate from external independent acceptance.
