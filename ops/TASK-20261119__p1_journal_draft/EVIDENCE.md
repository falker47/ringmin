# Evidence

## Environment

```text
base=falker47/ringmin origin/main c26400b328c2f8fa338b588e61abb98266a265f9
branch=codex/p1-journal-draft
task_mode=STRICT
platform=Windows 11 x64, build 26300
python=CPython 3.14.3
matplotlib=3.10.9
mpmath=1.3.0
tex=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
poppler_pdfinfo=26.07.0
```

The isolated worktree was clean before creation of the named branch. The common setup verified the Paper I v4 source archive SHA-256 `e5d499657a47cea462fcaedae78f2dab1eb69f594315cd91aa9a61c71b5081ab`, the Paper II v3 archive SHA-256 `c65bfabb23d8764e46da3c03723573b5386a404a32e6a4082bb95e6b23e3d5b1`, and the Ringmin-squared commit `1d0a5dea10cd09783a9c0e2d54ede79b790cce2b`. This task used the two manuscript sources via the ignored input junction. Package files refer to portable repository paths.

## Claim ledger

| Claim | Classification | Evidence and independence | Scope |
| --- | --- | --- | --- |
| For n = 3 through 14, the rational brackets have an open lower endpoint, feasible upper endpoint and width 10^-11. | Computer-certified finite result, independently reproduced in this session | Protected standalone `verify_global_brackets.py` and the twelve-case canonical certificate, independent of the figure generator and production solver | Finite global radii. Upper witnesses do not establish contact graphs at the infimum. |
| The chain-order theorem, fixed-order seam theorem, onsets (8, 13, 17) and the small-n corollary are preserved. | Exact theorems and proved corollary inherited from v4 | Six verbatim statement environments, fourteen numbered main equations and the complete seam-proof input. [Claim matrix](../../paper_assets/journal_p1_v5/CLAIMS_DIFF.md) | Source correspondence checks the transcription. The manuscript proof supplies the universal quantifiers. |
| The plotted n = 14 witness has 14 central tangencies and 91 strictly separated outer pairs at U = 21.66539518222. | Independently reproduced finite result | Direct Fraction reconstruction in `make_figures.py`, including rejection of a collapsed direction, plus the separate standalone verifier | First supplied witness at the rational upper endpoint. |
| The seam plots and outlines in the chain diagrams illustrate the stated thresholds. | Numerical observations | 65-decimal mpmath evaluation, numerical all-pairs control at n = 7, overlapping pair at n = 8 and signs on both sides of the three onsets | Plot samples carry no independent exactness claim. |
| Paper II proves a limiting constant above 0.1405694688. | Inherited exact theorem and proved lower bound | Official v3 source, theorem `thm:existence` and proposition `prop:lower`, strict directed lower value 0.14056946887766098063257 | The horizontal line bounds the limit. The pending upper macro has no numeric value. |
| The local draft has 16 cited, DOI-verified records and six reproducible vector illustrations. | Engineering facts | [DOI metadata](../../paper_assets/journal_p1_v5/refs_verification.json), citation-set test, fresh PDF regeneration | Byte identity is recorded for this environment. |

## Commands and checks

All checks are local. The Python test setup put the worktree's `src` first on its import path. The final full suite used `PYTHONDONTWRITEBYTECODE=1` and `PYTEST_ADDOPTS=-p no:cacheprovider`.

| Command or direct check | Exit and material result | Property checked |
| --- | --- | --- |
| `git status --short --branch` then `git rev-parse HEAD` | 0, clean detached base, then named branch at c26400b328c2f8fa338b588e61abb98266a265f9 | Correct isolated base. |
| Targeted HTTP GETs against Crossref works, doi.org handle registration and arXiv metadata | 0, 16 records with status VERIFIED | Each cited entry has a DOI, title, author list, publication year, venue and verification URL. Alt's author-supplied journal reference and DOI were cross-checked. The Zenodo registry handle was bound to the deposited metadata snapshot. |
| `python -B paper_assets/journal_p1_v5/make_figures.py` | 0, `PASS_WITNESS_14 central=14 strict_outer_pairs=91` | All six figures and exact upper-witness check. |
| `python -B paper_assets/journal_p1_v5/build.py` | 0, `PDF pages=18 before_appendices=10 appendix_starts=11 overfull_boxes=0 pdflatex_passes=3 unresolved=0` | Final temporary three-pass TeX build, final log, A4 size from pdfinfo, appendix boundary from the auxiliary labels. |
| Regenerate figures using `make_figures.py --output-dir DIRECTORY` in a fresh directory and compare bytes | 0, all six PDFs MATCH | Exact repeat of delivered figure bytes in the checked environment. Separate test compares two interpreter runs with different hash seeds. |
| Fresh `build.py --output DIRECTORY/repeat.pdf` and byte comparison | 0, 475579 bytes, SHA-256 `1d7752a882c61a2d0aebad35f045ca58ee4d7c05f15182c6ba093c2b13db4f7a`, MATCH | Repeat of final manuscript PDF. |
| `python -m pytest tests/test_journal_p1_v5.py` | 0, 6 passed in 8.23 s | Source transcription, updated bibliography, independent geometry checks, tampering rejection, determinism and build smoke. |
| `python -m pytest` | 0, 65 passed in 57.95 s, followed by 65 passed in 54.80 s on the staged version | Full worktree suite, including the noninteractive Windows subprocess correction. |
| `python -I -S verify_global_brackets.py` | 0, PASS_GLOBAL_BRACKETS, pinned input PASS | All 908 angle intervals, 47 witnesses, 540 central equalities, 3004 outer pairs, 6008 directed inequalities, 268648 explicit and 3374988556 covered cyclic classes. No hosted CI claim. |
| `python -m ruff check paper_assets/journal_p1_v5/build.py paper_assets/journal_p1_v5/make_figures.py tests/test_journal_p1_v5.py --no-cache` | 0, All checks passed | Python lint. |
| Direct source comparison and two isolated three-pass auxiliary files | 0, six formal statements, 14 numbered equations, both literal main table bodies and all three inputs match v4. All theorem and table labels preserve their printed numbers. | The sole ordinary section-label move is `sec:repro` (10 to 9). The six new labels are figure labels. |
| Source counts using the method in CHANGES.md | 0, abstract 156 words, negation count 53 to 7 | Abstract limit and editorial count. |
| Poppler rasterization and PDF page inspection | 0, figures and page layout inspected | True-scale graphics, the two small-disk callouts, layout, and Appendix A starting on page 11. |

## Artifact provenance

The published v4 `ringmin_dcg.tex` SHA-256 is `60e892a63c308d99325672a6455eef52498c1777aba2fb51d526b76b827f58e8`. The published v3 `main.tex` SHA-256 is `792473ac5b2f0b39bcf9bb3e0d0d576c70aa42bc55c941bc914e4eb8354e98e4`. The n = 14 source, its outer file and canonical certificate hashes, precision and Figure 1–6 generation rules appear in [figure provenance](../../paper_assets/journal_p1_v5/figures/README.md). Generation uses the source and figure renderer in the same local T2 commit. The published manuscript, code archive, certificate and their generation provenance remain distinct.

| Generated figure | SHA-256 |
| --- | --- |
| 01_kernel.pdf | 56bd1bf168c41bb958bdc5f5eecc32c1cc11eb55439c06b9e940c076f7d884a4 |
| 02_necklace.pdf | 2c62cde67ae94c0934a393c196c6126466ccb9637d3993b9ffa7ba85fac562c3 |
| 03_seam.pdf | cf32ba005067f8298ecf99ee29f5ccc0026cc8d12f66309b72958f802e951e9a |
| 04_witness.pdf | 9318ed70e5a46f150e29a770aa2683f7bc86c7366bc0d149bac9b0c8e701d15f |
| 05_ratios.pdf | 812566ae1c883f3655be49488195cc00de8a3b182b5774dea94565eaca2424ab |
| 06_deficits.pdf | 98299cd045545272a8627e2b14a0eef9f8649ed1fe202cb8adb1c9fc2c373035 |

## Failed checks and remedies

Transient title-query throttling was resolved by targeted sequential DOI lookups. DataCite DOI registrations were checked through doi.org, with the corresponding arXiv metadata or archived Zenodo record corroborating authorship. The proposed Szabó monograph and the Stephenson book were omitted for the metadata reasons in CHANGES.md. The corrections to figure labels, the release-DOI line break and Windows helper commands are recorded in TASK_LOG.md.

One complete repeat after the first green suite reported 63 passed and two failures. Both newly spawned processes failed with Windows error 6 while Python was duplicating the parent's standard input. All four subprocess invocations in the draft builder and its tests now use `stdin=subprocess.DEVNULL`; the replay passed 65 tests. The final PDF still rebuilt byte for byte.

## Final diff inspection

All 777 baseline tracked paths are protected. The task's 25 paths comprise 20 new journal-package files, a new test and four dossier files. The existing ignore rule at .gitignore line 23 covers the entire figures folder. Its six PDFs and one README were staged by explicit names. A complete staged-diff and index-to-file comparison returned PASS_STAGED for 25 added paths, with zero modified or deleted baseline paths, zero unstaged changes and zero undisclosed untracked paths. Both ordinary and staged git diff --check returned 0. Only the setup input junction remains ignored outside the deliverables.

## Residual uncertainty

External mathematical and editorial review of the draft remains pending. No manuscript was submitted and no hosted CI was claimed for the local commit. The upper-bound macro remains a visible placeholder pending an independently certified result from the companion work.
