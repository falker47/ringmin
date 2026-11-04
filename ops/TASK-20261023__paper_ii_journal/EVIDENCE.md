# Evidence

## Environment and Provenance

Local Windows/PowerShell; Python 3.14.3; SciPy 1.17.1; mpmath 1.3.0;
pdfTeX 1.40.28 (TeX Live 2025); existing Poppler and pypdf. STRICT.
Baseline: 75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae.
Analytic source pin: 3beb8d70c5b3748d370a92855847bdf574e5a14f.
Dedicated branch: codex/paper-ii-journal-candidate.
Original checkout remained at 6167e36cf6f80a6a7a7a6b41518a6b3f7155295d;
its sole untracked finite-v2 ZIP was explicitly protected by the mission.
Live remote HEAD/main was checked with git ls-remote, not inferred from the
older local main. Connector search found no open PR at preflight. Existing
journal_dcg is Paper I and was not reused as a Paper II workbench.

The initial environment lacked lineno.sty. Only the official latex-lineno
package v5.9 (style plus README/license) was installed into the existing local
TeX tree after the build demonstrated the need. The official style source was
https://raw.githubusercontent.com/latex-lineno/lineno/master/lineno.sty,
SHA-256 e12f4151f6e86448168fad536850c641c789e8a11babd9d7e8dbe36a38965f37.
No distribution upgrade, Python dependency upgrade, paid service or remote
compute was introduced. Actual TeX/font input hashes are in BUILD_REPORT.json.

## Evidence Classes and Authority

The global limit, LP error bound, all-pairs block transfer and endpoint
inequalities remain exact analytic theorems under their stated hypotheses.
Fresh rational outputs independently reproduce the stated finite signs,
intervals and bounded fixtures. They do not establish universal quantifiers
or a new finite global optimum. SciPy discovers LP candidates; Fraction
arithmetic checks the resulting bounded certificates. The checks do not
import src/ringmin or the production geometry solver.

Internal component reviews are separate from external referee acceptance:
[core](CORE_AUDIT.md), [lower](LOWER_REVIEW.md), [upper](UPPER_REVIEW.md), and
[package](PACKAGE_REVIEW.md). Each records its own scope and exact observed
checks; the lower analytic reviewer did not rerun arithmetic. The package
reviewer did not claim analytic proof acceptance. The main and supplements
are complete readable proof sources; these audit records are provenance.
No stable scientific conclusion changed, so knowledge modules and the central
index were not edited or duplicated. The roadmap changed only the editorial
review priority, preserving subsequent scientific questions.

## Commands Actually Run and Material Results

Unless stated otherwise, paths below are relative to the candidate repository,
commands are local, and each listed successful command exited 0.

| Command | Observed result / property / limit |
|---|---|
| python -m pytest | 59 passed in 52.32s; production regression suite, not an independent all-n proof |
| python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/verify.py | Fresh exact certificate equality; 144 rational deletion fixtures, 48 prescribed measures, 16 tour/cutoff cases; 12 output and 7 source hashes |
| python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/check_integrity_controls.py | Standalone with zero repository inputs passed; changed certificate/document and optimized Python rejected |
| python -I paper_assets/paper_ii_journal/verify_math.py --with-lp | Complete successful output retained verbatim in mathematics.log; all five upper scripts, S1, line and bounded LP checks |
| python paper_assets/paper_ii_journal/build.py | Fresh external directory for each document; three no-shell-escape pdflatex passes each; 9/13/14 pages; zero unresolved references, citations, missing glyphs or box warnings |
| python paper_assets/paper_ii_journal/build.py --export | Final export: 36 archive files; SHA-256 e18901f944d150ce31c0a08decfb96781c165b8ed1f4b14f6012e94c3f21dbde |
| python -I -S paper_assets/paper_ii_journal/verify_package.py | PASS archive: 35 payload hashes and current-source/reused-supplement identity; PASS candidate manifest: 23 payload hashes and lower provenance |
| python -I -S ops/TASK-20261023__paper_ii_journal/check_scope.py --original-checkout <original-checkout> | PASS 774 protected baseline paths; only declared task paths differ; original HEAD/status and sole untracked ZIP preserved |

The exact inner TeX command is recorded in BUILD_REPORT.json:
`pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder <source>`.
SOURCE_DATE_EPOCH=1792713600 and FORCE_SOURCE_DATE=1. The script rejects
undeclared external inputs after resolving their paths. The independent
reviewer rebuilt all three documents again after the final auxiliary-input
repair, reproducing the same PDFs byte for byte.

The aggregate line check reported 1089 rational words, 13995 independent
paths, 13941 pair/closure checks, 1089 concatenations, 94620 genuine-label
quantiles and four rejected negative controls. Six LP cases cover
(k,r)=(1,2),(1,5),(2,2),(2,3),(3,4),(4,5): 1119 complete inequalities,
18 corrupt certificates rejected. The core reviewer also checked 17090
independent endpoint-path evaluations and four additional negative controls.

Upper exact checks include 2835 point and 297 interval arithmetic oracles,
the required implicit-parameter signs, 120 single-prefix recovery cases,
16 fourth-block corners, 448 reflection moments and 48 branch probes.
The fourth raw increment upper bound was
-701561353/200000000000000000000000 < -1/288000000000000;
using pi<4 gives the stated normalized saving >1/4608000000000000.
The separate upper reviewer tested 1720 permutations, 90645 cells and 24472
affine panel endpoints, and checked 12 source identities. These remain
bounded arithmetic corroboration, not substitutes for the transfer proof.

## Final Portable Archive

The package reviewer extracted the full archive into a fresh external
TemporaryDirectory and independently ran `python -I -S verify_package.py`,
`python -I -S build.py`, `python -I -S verify_math.py --with-lp`, and repeated
`python -I -S build.py --export`. Builds and checks exited 0; repeated exports
were byte-identical at that review checkpoint. Expected `-O` rejection exited
1. Final documentary updates changed the archive hash without changing any
mathematical source or PDF; the corrected build.py was separately replayed.

For the final archive, a local `python -` probe used zipfile.extractall in a
fresh TemporaryDirectory, then executed
`[sys.executable, '-I', '-S', str(target/'verify_package.py')]` with cwd=target.
It exited 0: `PASS candidate manifest: 35 payload hashes; lower-supplement
provenance`, then `PASS: final archive verifies outside repository with all
35 inner payload files`. No repository source or historical ops file was
available to this extracted verifier.

| Delivered file | SHA-256 |
|---|---|
| main.pdf | 0001c5c4b5ae26d106715d4a25f452b2a0386b24308213262465f7bd14c5994a |
| upper_supplement.pdf | bb6b2704151ced2464e76cf6272072d1185258ff2655b7baea5ed468285ba56b |
| preserved S1 supplement.pdf | a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568 |
| BUILD_REPORT.json | 7bc9752bc8112f6d24c2830463f8f8182f24d8e21df9fea115b9fd6700b39ba4 |
| MANIFEST.json | 53e63a3dd5780866169df7be636ec4a0f870d10f456dceb2e94db5d0647c215a |
| source_bundle.zip | e18901f944d150ce31c0a08decfb96781c165b8ed1f4b14f6012e94c3f21dbde |

Hash identity is an engineering property, not mathematical truth. The final
Git commit containing this manifest identifies the candidate revision without
a circular embedded self-SHA. Identical PDF bytes are environment-dependent.

## PDF and Editorial Inspection

Executed `pdftoppm -r 95 -png` for main.pdf and upper_supplement.pdf, and
`pdftoppm -r 85 -png` for preserved S1, writing only ignored preview images.
All nine main, thirteen upper and fourteen lower pages were visually inspected:
no clipping, missing text, overlaps or unreadable equations were found. Dense
formulas and the reference-only last pages are visible and fit their margins.
Main/S2 have page/line numbering; unchanged S1 retains its original format.

A `python -` pypdf probe traversed each page's /Resources /Font dictionary,
then each /DescendantFonts entry or simple font's /FontDescriptor, requiring
one of /FontFile, /FontFile2 or /FontFile3. It exited 0:
main 9 pages, 17 embedded font subsets, 612x792 pt;
S2 13 pages, 18 embedded subsets, 612x792 pt;
S1 14 pages, 17 embedded subsets, 595.276x841.89 pt.
The optional pdffonts executable was unavailable; it is not claimed to have run.

Official JoCG submission requirements and review criteria were checked online;
review and camera-ready instructions are distinct. Sources, retrieval limits
and exact treatment are in EDITORIAL_REQUIREMENTS.md. Primary shelf, temporal-
constraint and weighted-contact sources were compared in PRIOR_ART.md; the
search is explicitly targeted, not exhaustive. Paper I v2 is the current
finite citation; v1 remains historical. The DAM submission date/reference is
author-supplied information, not a claim of journal acceptance.

## Failed Attempts and Repairs

TASK_LOG.md and PACKAGE_REVIEW.md preserve chronology. Material failures:

- Sandbox remote access and managed-worktree writes/Git were unavailable;
  narrowly scoped escalated calls succeeded. gh was unavailable; GitHub
  connector was used. One arXiv v2 request cache-missed; subsequent official
  public record and protected local v2 supplied the source.
- First TeX build lacked lineno. tlmgr returned exit 0 but refused the
  TL2025/remote2026 mismatch; the historical mirror failed. Only the official
  needed package was installed, then the build passed. A literal newline
  escape and an initially overstrict TEXMFROOT omission were fixed.
- Aggregate math first reached optional mpmath diagnostics under -S and failed.
  Wrapper now requests the existing --exact-only modes; copied checkers are
  unchanged and the complete aggregate then passed.
- Adversarial packaging checks originally accepted stale source/PDF pairs,
  a missing main source, and undeclared external TeX. Required inventories,
  source/PDF bindings, exact archive inventories and a TeX-root allowlist
  corrected these. A further external .aux bypass was found and fixed by
  restricting auxiliary allowances to the isolated document's own names.
  Fresh .tex/.aux/.out/.toc regressions all reject external inputs.
- Five inherited upper checkers contain CRLF. The initial LF attribute would
  change their hashes on staging; explicit -text preserves exact copied bytes.
  Both raw and filtered Git hashes now agree for every package file; the
  staged comparison passed for all 38 task paths. CRLF is explicitly declared
  for those five copies while the ordinary trailing-space checks remain active.
- The final extraction probe initially failed on sandbox writing .gitattributes
  in a temporary directory (exit 1). The identical scoped escalated replay
  exited 0. No delivered archive or original work was changed by the failure.

## Final Diff and Git Handoff Gates

The complete new TeX, Python, Markdown and generated inventories were inspected
by the parent and independent reviewers; PDFs were visually read and copied
checkers compared to their pinned sources. Ordinary diff omits untracked
additions, so a separate all-new-text whitespace scan covered all 32 additions and
passed; the staged diff was inspected in full by component, with copied
checker identity and generated JSON inventories checked mechanically. check_scope.py verifies the complete 774-path local byte snapshot
and baseline object inventory, then --staged compares every candidate package
blob byte for byte to its manifested file. This local preservation guard is
separate from the portable package verifier.

Only three old paths are allowed: CI, CURRENT_STATUS.md, and the editorial
roadmap. No public arXiv source/PDF, Review State Registry, accepted scientific
source, stable ledger, solver, finite certificate or original ZIP may change.
The final staged inspection/whitespace results are appended to TASK_LOG.md.
Commit/push and draft PR use the dedicated branch, never main or force-push.

Hosted CI is deliberately PENDING at this pre-commit content freeze. The final
handoff must identify the exact persisted SHA, draft PR and observed run/jobs;
no baseline CI claim or local PASS substitutes for that check. The workflow
runs tests on push and PR and now executes S1 verification/integrity controls.
Full historical frontier verification was not rerun: no certification code,
pruning logic or certified artifact changed. CI's smoke mode remains a smoke
check, separate from its complete exact-bracket verification step.

## Residual Uncertainty and Next Action

No invalidating mathematical or packaging gap was found in the reviewed scope.
The internal reviews are fallible and are not external scientific acceptance.
A sharp C*, efficient precision algorithm, universal contact structure and
finite certification beyond n=14 are not established. Venue approval,
submission, external refereeing and exhaustive bibliographic priority remain
outside this candidate-preparation task.

Exactly one next atomic task: independently review the exact delivered Paper II
candidate commit and its scientific, reproduction and editorial gates.
