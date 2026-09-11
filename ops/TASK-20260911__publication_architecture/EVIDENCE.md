# Evidence

## Environment and provenance

Starting repository HEAD: `227d09d480c2d88d09d3450c9015fc9737440c17`.
Windows PowerShell, Python 3.14.3, pypdf 6.14.2, installed TinyTeX/TeX Live
2025, Poppler. Mode STRICT. Scientific supplement is pinned to the public
`3beb8d70c5b3748d370a92855847bdf574e5a14f`; publication packaging is identified
by the containing commit. Actual input byte hashes and distribution dependency
hashes are recorded by the builder and package checker.

## Claim and editorial evidence

- [Sequel claim map](SEQUEL_CLAIM_MAP.md): exact theorem dependencies and checks.
- [Correction audit](CORRECTION_AUDIT.md): finite scope, numerical guards,
  obsolete conjectures and historical content preservation.
- [Policy and overlap](POLICY_AND_OVERLAP.md): official sources, object inventory,
  shared-prose measurement and moderation fallback.

No new scientific conclusion is introduced. Exact theorems retain their proof
sources; finite optima remain computer-certified for 3..14 under recorded
numerical guards; larger finite cases remain heuristic. Internal separate-agent
review is not independent external acceptance.

## Verification record

All results below are local. Root ran packaging/frontier checks; separate
internal agents ran the mathematical commands in the linked audits. No
external acceptance is claimed. Existing mathematical checkers use independent
exact/rational or symbolic gates rather than production Ringmin imports.

| Command | Exit and result | Property and limit |
|---|---|---|
| `python scripts/frontier_logs.py restore` | 0; PASS 12 exact archives, 9649682 bytes, readback identical | Original progress evidence; no new enumeration. |
| `python verify.py --start 3 --stop 14` | 0; all twelve incumbent/local/frontier checks PASS, eta=1e-12 | Saved witnesses, brackets, frontier/coverage summaries; original float64 guards retained, not interval rescoring of every excluded order. |
| `python -I -S ops/TASK-20260911__global_variational_limit/check_line_recovery.py` | 0; 1089 words, 13995 paths, 13941 pair/closure checks, 94620 quantiles, 4 controls | Bounded independent evidence; analytic proof carries all-n limit. |
| `python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py` | 0; 1119 inequalities, 18 corrupt certificates rejected | Exact rational certificates; SciPy only proposes candidates. |
| `python -I -S ops/TASK-20260911__general_block_transfer/check_general_blocks.py` | 0; 30034 small orders/580560 cells; 18 larger orders/1080000 cells; 4 controls | Bounded cell recovery checks, not an all-n proof by sampling. |
| `python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py` | 0; 16 partitions, 448 moments, 48 branch probes, exact saving >1/4608000000000000 | Exact finite gates supporting unchanged fourth-block proof. |
| `python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | 0 on separate rerun; all polynomial/root/KKT/boundary gates PASS | Same directed lower enclosure; all-n theorem remains analytic. |
| `python -I -S ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py` | 0; exact_sequence_gates=PASS; 104 edges, 10 polynomial gates, 6 rejections | Bounded exact support for formal-seam theorem. |
| `python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py` | 0; 9 identities, 32 constructions, 2964 directed paths, 82 rejections | Fixed-order evidence; not global floating claims. |
| `python paper_assets/build_publications.py sequel` | Final exit 0; 3 clean passes, stable aux/out, zero warnings | Empty-directory build; local TeX distribution. |
| `python paper_assets/build_publications.py correction` | Final exit 0; 3 clean passes, stable aux/out, zero warnings | Four-input build; pending identifier retained. |
| `& './ops/TASK-20260911__publication_architecture/clean_compile.ps1' -Candidate sequel` | 0; 1 input, 3 passes, zero warnings | Independent direct pdflatex build without Python builder. |
| `& './ops/TASK-20260911__publication_architecture/clean_compile.ps1' -Candidate correction` | 0; 4 inputs, 3 passes, zero warnings | Independent orchestration, same installed distribution. |
| `python ops/TASK-20260911__publication_architecture/check_publications.py sequel reproducibility/.work/independent-sequel-662586ef1b424351a0c27f95eb3d807a` | 0; 20 labels, 6 references, 8 exact pages, 16 embedded scalable fonts, 108 system dependencies | Exact candidate/independent text, painting, dimensions, metadata and fonts; hygiene and source inventory. |
| `python ops/TASK-20260911__publication_architecture/check_publications.py correction reproducibility/.work/independent-correction-1570dfb9b5e74cfcbe856cc336727372` | 0; 20 labels, 8 references, 12 exact pages, 20 embedded scalable fonts, 130 system dependencies | Same checks; no active content, external build inputs or unembedded fonts. |

First package checks against the builder's directories also passed. Final
reports compare against separate direct builds above. Temporary paths are
ignored; reproduction creates new empty directories and reports their names.
The full frontier output was:

```text
n=03 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=1
n=04 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=3
n=05 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=12
n=06 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=60
n=07 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=360
n=08 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=2520
n=09 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=1 total=20160
n=10 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=4 total=181440
n=11 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=6 total=1814400
n=12 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=9 total=19958400
n=13 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=10 total=239500800
n=14 incumbent=PASS local=PASS frontier=PASS eta=1.0e-12 frontier_size=11 total=3113510400
```

## Artifacts, provenance and visual inspection

Each candidate's BUILD_MANIFEST.json owns its source inventory, byte hashes,
compiler, fixed SOURCE_DATE_EPOCH=1789084800 and builder hash.
[SEQUEL_PACKAGE_CHECK.json](SEQUEL_PACKAGE_CHECK.json) and
[CORRECTION_PACKAGE_CHECK.json](CORRECTION_PACKAGE_CHECK.json) record actual
dependency/font hashes and PDF inspection. Generation code is identified by
the containing commit; mathematical inputs remain at the public pinned commit.
No mathematical endpoint or finite certificate was regenerated.

| Candidate | Source SHA256 | PDF SHA256 |
|---|---|---|
| Sequel | `28853635a65267e1772352436f29d6c19d0a0b8ace823aa72a0d77f52ad8622f` | `fb909549dd9b123a8e97b84d015682788244bb8996e65f86bd1be8656b237d8b` |
| Correction | `4724d3d6f222e22293a61b5bbed70685550c8a341f4a070f535ebd6fbfc7d2af` | `6cc92c516894606901c14ee1280b4cd392b575861e83b26264186f3573d26cf6` |

Actual root rendering commands, each exit 0:

```text
pdftoppm -scale-to 1300 -png paper_assets/asymptotic_sequel/ringmin_asymptotic.pdf reproducibility/.work/sequel-page
pdftoppm -scale-to 1300 -png paper_assets/v1_correction/ringmin_finite_v2.pdf reproducibility/.work/correction-page
```

Root directly inspected all 8 sequel and 12 correction PNG pages using the
image viewer: title/abstract, formulas, theorem/proof transitions, every table
and figure, page numbers, glyphs and references. No clipping, overlap or
illegible content remains. The correction's unchanged historical curve is
captioned as the disproved conjectural asymptote; original appendix captions
are qualified by adjacent prose. Table 5 occupies a normal centered float page.
First-page pending status and the reference-7 placeholder are intentional,
legible user requirements, not accidental missing fields.

The retained author contact already appeared in the public historical source;
no new private data was introduced. Source bundles contain only declared
TeX/PNG inputs, not audits, metadata JSON, builders, PDFs or local paths.

## Findings and failed attempts

- Editorial IMPORTANT: the old replacement omitted the finite reference's
  identity. Resolved by two distinct manuscripts and superseded active handoffs;
  old source/PDF and audit evidence preserved.
- Scientific IMPORTANT: inherited exact/numerical and floating-quantifier
  ambiguities narrowed, including the regime-III equality caught by separate
  internal cross-review. All original numerical rows and three proof bodies
  remain unchanged. No new scientific conclusion.
- Layout IMPORTANT: first sequel build exited 1 for a 15.74173pt overfull box;
  shortened one supplement sentence without changing its link or content.
- Layout IMPORTANT: first correction build exited 1 for unused EPS-conversion
  warning, four overflowing tables/value lines and two underfull bibliography
  lines. Used the graphics driver's documented DoNotLoadEpstopdf switch (PNG
  inputs only), displayed the pocket values and adjusted table spacing and
  ragged-right bibliography. Second build still failed on the wide appendix;
  reduced surrounding column spacing only. Final/independent builds pass;
  warnings were not suppressed by relaxing the build gate.
- Source helpers: wrong template filenames, the source author's escaped-string,
  overbroad-language and whitespace checks, and root's rejected combined
  delete/add patch were corrected. The rejected patch made no changes.
  Component audits retain failed attempts and successful reruns.
- Attribution limitation: hidden Henigman MSE comment not independently fetched;
  historical attribution retained and flagged. Official UQ listing corroborates
  the question; individual page unavailable. Neither is a theorem/certificate
  premise.
- Final separate internal packaging review found an adjacent TeX macro token
  in generated abstract metadata (`\\leC` after custom-macro expansion) and an
  imprecise README witness phrase. The generator now braces expansions and
  rejects unknown/joined abstract macros; metadata checks were rerun and both
  passed. README now says existence of strict-slack placements at reported
  radii. Manuscript sources/PDFs are unaffected.
- First final diff whitespace check found one extra EOF blank line in the
  newly appended historical-log note; corrected and rerun with exit 0.

## Acceptance and final-diff boundaries

The 51-item inventory covers all substantive objects. The two papers share no
12-token main-prose sequence under documented normalization; formulas, tables
and bibliography are excluded from that metric and covered semantically. It
is not an arXiv threshold. Correction intentionally retains v1 proofs/tables;
sequel reuses the unsubmitted old candidate's asymptotic core. Elementary
shared geometry serves self-containment.

Publication history, current status, README, roadmap and review handoffs agree.
Old current readiness labels are removed. The append-only historical log
retains its earlier readiness event with explicit supersession; that is not
current status. Historical audit wording remains in the starting commit.
Only the publication-state ledger changed; no stable mathematical owner was
duplicated. No research, submission, release/tag, workflow dispatch or external
acceptance write occurred. Final status/diff/whitespace/protection/integration
checks are recorded in TASK_LOG.md. Four copied PNGs require explicit staging
because the existing figures/ ignore rule also hides these new asset paths.

## Completion audit against the goal

The continuation after local midnight re-read the full objective and inspected
current status/diff/HEAD. The preceding turn was substantive progress: two
manuscripts, clean builds, verification, source reviews and publication routing
were completed. No process was restarted and no completed check was relabeled
as a newly executed check.

| Required end state | Current evidence |
|---|---|
| Standalone title/abstract/core narrative | Eight-page source/PDF; Sections 1-7 and SEQUEL_CLAIM_MAP cover every required line/limit/LP/error/recovery/endpoint topic. |
| Self-containment and attribution | Local angular and line proofs; explicit v1 citation for Supnick/framework/3..14/conjecture; full source read by authoring agent and root. |
| Historical source intact | Protected-path git diffs against starting HEAD exit 0; v1 source/PDF unchanged. |
| Conservative finite correction | Twelve-page separate source/PDF; original title, all three proof bodies and complete numerical tabulars preserved; exact copied appendix/figures. |
| Every obsolete conjecture corrected | CORRECTION_AUDIT occurrence inventory includes abstract, introduction, chain calculation, figure, deficit and cascade/open-question passages. |
| No fake identifier | One explicit pending token in corrective citation; first-page pending status; metadata checker and direct source review. |
| Old candidate preserved and superseded | Old TeX/PDF/bundle/build evidence unchanged; current README/handoff/metadata carry EDITORIALLY_SUPERSEDED. |
| Canonical repository truth | Current status, publication-history owner, READMEs, roadmap and historical review-packet banner agree; separate internal final review completed. |
| No stale current readiness label | Direct scan passed all current status/handoff/metadata; append-only historical event explicitly marked superseded. |
| Clean reproducible builds | Builder and independent direct clean compile each pass three times; 1+4 inputs; exact 8+12 PDF page equivalence. |
| Claim sources/classifications | Both claim audits, 51-object semantic inventory, seven bounded checkers and full saved-frontier output above. |
| Overlap and arXiv policy | POLICY_AND_OVERLAP contains exact diagnostic script/results, primary policy/bibliography sources and root's explicit versions/splitting check. |
| Future publication sequence only | Review first, standalone submission later, real-ID correction later; moderator-required fully integrated fallback documented; no submission performed. |
| Complete dossier/provenance | Status, append-only log, evidence, two claim audits, policy audit, build/independent-compile/checker code and two package reports. |
| No unrelated changes | Exactly 41 inspected task files; historical math, solver, results, verifier, citation and dependencies unchanged. |
| Authorized integration | Final remaining gate is staged diff/whitespace, normal main commit/push and local/remote SHA comparison; recorded by terminal tools and final handoff. |
| Review state | READY_FOR_REVIEW; correction AWAITING_STANDALONE_ARXIV_ID; no external acceptance. |

## Residual limitations at handoff

Local TeX Live 2025 packages are newer than arXiv's frozen 2025-08-03 snapshot.
Server compilation and moderation are not exercised. Matching PDF bytes requires
matching TeX dependencies and source bytes; line-ending conversion can change
source hashes. The correction deliberately contains a visible machine-detectable
pending identifier. No new exhaustive finite search or hosted CI claim is made.
