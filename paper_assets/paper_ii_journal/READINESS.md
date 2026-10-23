# JoCG Pre-Submission Readiness

Finalization baseline: fa32c99e9da0d639dca5735864c7c341d2e60059.
Assessment date: 2026-10-24. Mode STRICT. State: READY_FOR_REVIEW.
The author has approved JoCG as the destination. This revision completes
editorial and reproducibility preparation; journal submission and external
scientific acceptance have not occurred.

| Gate | Evidence at content freeze | Scope / limit |
|---|---|---|
| Preserved science | Complete main/S2 source comparison permits only enumerated editorial substitutions; both abstracts unchanged; 796 protected files retain preflight bytes | All S1, public science, research proofs, mathematical checkers and prior dossiers unchanged |
| Earlier analytic review | Prior CORE_AUDIT, LOWER_REVIEW and UPPER_REVIEW in TASK-20261023__paper_ii_journal | Inherited internal evidence for the unchanged mathematical content; no new independent scientific review is claimed |
| Arithmetic replay | Fresh verify_math.py --with-lp passes S1, its integrity controls, line recovery, five upper checks and six rational LP cases | Finite arithmetic support, not an all-n proof by testing |
| JoCG review formatting | 11pt single-spaced main/S2; page and line numbers; title-case headings; available DOI references; provisional masthead labels removed | S1 preserved as separately indexed supporting material |
| Metadata and disclosures | Main/S2 PDF titles and Maurizio Falconi; 17/18 embedded font subsets; preprints, Paper I DAM review and AI assistance disclosed | Human author supplies/confirms private portal metadata and copies the unchanged abstract |
| PDF builds and visual inspection | 9/13/14 pages; three passes per build; no reference/box warnings; two fresh builds reproduce every delivered PDF; all 22 changed pages inspected | Byte equality requires the recorded TeX/fonts; S1 remains byte-identical |
| Portable package | 24 outer / 36 inner payload hashes; extracted standalone verification and double builds pass; seven negative controls reject corruption/missing files/external inputs | Hashes bind content, not mathematical truth |
| Local regression suite | python -m pytest: 59 passed in 49.09s, exit 0 | Production regression tests, separate from arithmetic replay |
| CI integration | Existing Python job runs package integrity and aggregate math with LP, including S1 once; separate push/path-filtered LaTeX workflow, no artifact uploads | No TeX installation in ordinary Python CI; hosted TeX checks repeated builds within its own environment |
| Hosted CI on containing commit | Pending until commit/push; final handoff supplies exact SHA and run links | No historical run substituted for this gate |
| Independent review / human submission | Next action / not performed | READY_FOR_REVIEW does not advance the Review State Registry |

## Evidence and Provenance

Current checks and the explicit editorial source allowlist are in
`ops/TASK-20261024__jocg_finalization/`. The earlier internal analytical reviews
remain in `ops/TASK-20261023__paper_ii_journal/`. Those audit records are
provenance, not proof premises; the proofs are in main and S1/S2.
MANIFEST.json binds the package and identifies the Git revision containing it.
BUILD_REPORT.json records the actual compiler, system inputs and output hashes.
The deterministic epoch remains 2026-10-23 for compatibility with preserved S1;
the manuscript and package revision date is 2026-10-24.

## Evidence Classes and Limits

The unchanged mathematical statements retain their original classifications:
analytic theorems under their stated hypotheses and bounded rational
certificates for specified signs/enclosures. LP candidates are discovered by
SciPy and checked with exact Fraction arithmetic. New work in this revision is
editorial and engineering. No new mathematical theorem, finite optimum or
certification scope is asserted; no independent scientific acceptance is implied.

PDF byte equality across different TeX/font versions is not promised. The
hosted LaTeX gate compares two fresh isolated builds without replacing delivered
files; its log reports whether those bytes also match the recorded PDFs.
`--require-delivered` enforces that stronger condition in the recorded local
environment. Configured distribution TeX trees are recognized, while undeclared
external .tex/.aux/.out/.toc inputs remain rejected. S1 retains its original
A4 format without line numbering; main/S2 use the JoCG review format.

The sharp constant, efficient high-precision computation and universal contact
structure remain open. Prior-art comparison is targeted, not exhaustive.
Journal suitability and acceptance are external editorial judgments. No new
capability, portal action, arXiv update or Registry change was performed.
