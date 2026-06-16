# Submission Review Report

Date: 2026-06-16

## 1. Executive Verdict

Almost ready.

The endorsement-readiness pass is directionally strong: the claims are now separated into proved, certified, and conjectural parts; the endorsement templates ask for category appropriateness rather than peer review; and the lightweight verifier path is clear. I would not tag `v0.1-submission` yet, because the arXiv abstract is currently too long for metadata, LaTeX byproducts are tracked, and the arXiv source bundle / generated-artifact policy still needs one deliberate decision.

## 2. Highest-Risk Issues

1. **Abstract exceeds arXiv metadata limit.** The current TeX abstract is 2404 characters / 325 words after whitespace normalization. arXiv's metadata guidance says abstracts longer than 1920 characters are not accepted: https://info.arxiv.org/help/prep.html. This is the main submission blocker.

2. **Generated LaTeX byproducts are tracked.** `paper_assets/ringmin_paper.aux`, `.log`, and `.out` are tracked. They are volatile build artifacts and should not remain tracked for a clean submission tag. `paper_assets/ringmin_paper.pdf` is different: it is useful for endorsers and GitHub readers, but should be an intentional release artifact, not part of the arXiv source upload.

3. **Source bundle and generated figures need a decision.** The TeX includes figures from `paper_assets/figures/`, but that directory is ignored and untracked. A clean checkout can compile without those figures because of `\IfFileExists`, but it will not reproduce the same PDF. Before arXiv upload, either include the two used figures in the source bundle (`radii_vs_n.png`, `n14.png`) or accept that the arXiv-compiled PDF omits them.

4. **Related-work novelty claim is a little broad for the small bibliography.** The phrase "appears not to have been treated" is plausible but stronger than the citation base can fully support. For endorsement this is not fatal, but a softer formulation would reduce reviewer friction.

5. **LaTeX log has presentation warnings.** The PDF compiles, but the log reports three hyperref PDF-string warnings and three overfull boxes, including one in the title/abstract range. This is not a correctness blocker, but the final PDF should be visually inspected before tagging.

## 3. Recommended arXiv Primary Category

Recommended primary category: `math.CO`.

Reason: arXiv describes `math.CO` as covering discrete mathematics, enumeration, and combinatorial optimization; this paper's central proved mechanism is a Supnick/anti-Monge TSP ordering theorem, and the finite certification is an exhaustive search over cyclic orders. That is the most native framing for an endorser judging subject-area appropriateness.

Tradeoffs:

- `math.CO`: best endorsement fit for the core theorem and certification story. The geometry remains visible, but the main mathematical claim is combinatorial optimization.
- `math.MG`: good fit for the motivating tangent-circle geometry, and arXiv lists discrete and convex geometry under `math.MG`; however, an endorser may reasonably see the paper as primarily an ordering/TSP result with a geometric feasibility oracle.
- `cs.CG`: defensible only as a secondary audience if the computational geometry/certified-search angle is emphasized. The current manuscript reads as mathematics, not as a new computational-geometry algorithm paper.

Cross-listing: I would not request a cross-list during the initial endorsement ask unless the chosen endorser explicitly suggests it. arXiv notes that endorsement is per endorsement category and that cross-lists should be used sparingly and only with good reason: https://info.arxiv.org/help/endorsement.html and https://info.arxiv.org/help/cross.html. For getting endorsed, one strong primary category is cleaner than asking an endorser to bless multiple audiences.

## 4. Generated PDF/log/aux Policy

Recommendation:

- Keep `paper_assets/ringmin_paper.pdf` tracked only if the repository wants a convenient endorser-facing PDF snapshot. This is reasonable for GitHub and release assets.
- Do not keep `paper_assets/ringmin_paper.aux`, `.log`, or `.out` tracked. Remove them from git tracking in a later cleanup and add LaTeX byproducts to `.gitignore`.
- Do not include the generated PDF, `.aux`, `.log`, or `.out` in the arXiv source upload when submitting TeX. arXiv's submission guidance says TeX/LaTeX is preferred and PDF generated from TeX source is not the accepted source format: https://info.arxiv.org/help/submit/index.html.

Suggested `.gitignore` addition:

```gitignore
# LaTeX build byproducts
paper_assets/*.aux
paper_assets/*.log
paper_assets/*.out
paper_assets/*.fls
paper_assets/*.fdb_latexmk
paper_assets/*.synctex.gz
```

If the PDF should not be tracked as a release convenience, also add:

```gitignore
paper_assets/*.pdf
```

## 5. Suggested Paper Edits

These are suggested snippets only. I did not apply them.

### Title

Current title is acceptable, but slightly long and TeX-heavy for metadata. Suggested replacement:

```tex
\title{Circles of radii $1,\dots,n$ around a central circle:\\
Supnick ordering and certified finite optima}
```

If this title changes, update `CITATION.cff` too.

### Abstract

Replace the current abstract with a shorter version below the arXiv metadata limit:

```tex
\begin{abstract}
We study the following discrete-geometric optimization problem: circles of radii $1,2,\dots,n$ are all externally tangent to a central circle, and the central radius $R$ is to be minimized over cyclic orders of the surrounding circles. The chain version of the problem is governed by a fixed Supnick/anti-Monge traveling-salesman order. For every $R$, the angular-separation matrix is symmetric anti-Monge, so Supnick's theorem identifies a single minimizing cyclic order, independent of $R$. This proves Dan's conjectured ``pyramid'' order optimal whenever the corresponding chain necklace is geometrically realizable, and gives an unconditional lower bound in all cases.

The lower bound is not always attained: from $n=8$ the smallest circle can float, tangent only to the central circle. We formulate the full feasibility problem as a circular system of pairwise angular constraints, equivalently a simple temporal network, and certify global optima for $3\le n\le14$ using branch-and-bound plus an independent 50-digit verifier. The certified values exhibit several regimes, including a second floating circle at $n=14$. Computations beyond the certified range are reported only as heuristic evidence for a continuing cascade and for the conjectural asymptotic form $R^\ast(n)=n^2/8(1+o(1))$. We also identify the radius-maximizing chain order as the complementary Supnick tour.
\end{abstract}
```

### Introduction Claims Framing

The introduction is basically safe. To make the scope even clearer, consider replacing:

```tex
This paper addresses the problem on three levels, keeping the epistemic status of each result explicit.
```

with:

```tex
This paper separates a proved ordering theorem, finite certified computations, and conjectural extrapolations. The proved theorem concerns the chain lower-bound problem; the certified computations concern the full pairwise-constraint problem only on the stated finite range.
```

### Epistemic Ledger

The ledger is good and should remain. A small clarity tweak would be to replace "the three seam-failure computations" with "the three finite Supnick-tour seam-failure computations", so the phrase is less insider-ish.

### AI-Assistance Disclosure

No correction required. The acknowledgment is concise, attributes responsibility to the author, and does not list AI as an author, consistent with arXiv metadata guidance.

### Bibliography / Related Work

Suggested safer replacement:

```tex
\paragraph{Related work.}
Supnick's fixed-tour theorem \cite{supnick} and the Monge/Supnick taxonomy of polynomially solvable TSPs are surveyed in \cite{bdvvw}. The problem is adjacent to circle-packing literature, especially questions about tangent circles and containers \cite{hifi}, but differs from standard container-packing formulations because the variables here are cyclic order and angular feasibility around a prescribed central circle. Descartes' Circle Theorem \cite{descartes-ref} enters only in the analysis of local pockets. We are not aware of prior work connecting Supnick matrices with this tangent-circle ring problem.
```

This preserves novelty while avoiding an overbroad literature claim.

## 6. Email-Template Corrections

The email templates are well scoped. They explicitly say the request is not peer review and ask for comfort endorsing category appropriateness.

Suggested minimal corrections:

- Prefer the `math.CO` template as the primary template.
- Replace `[proposed category]` with `math.CO (Combinatorics)` everywhere before sending.
- Add one category-rationale sentence after the first paragraph:

```text
I am proposing math.CO because the central proved result is a Supnick/anti-Monge TSP ordering theorem, with the circle geometry providing the motivating feasibility problem.
```

- Consider replacing "short paper" in the `math.MG` template with "paper"; the current PDF is 10 pages, which is short enough, but the adjective is unnecessary.
- Add a gentle exit line if writing to someone not personally known:

```text
If this is outside your endorsement area, I completely understand.
```

Do not send to many potential endorsers at once; arXiv explicitly discourages that.

## 7. Tag-Readiness Checklist for `v0.1-submission`

Blockers before tagging:

- [ ] Shorten the abstract to <= 1920 characters for arXiv metadata.
- [ ] Decide title finality; if changed, update `CITATION.cff`.
- [ ] Remove tracked `.aux`, `.log`, and `.out` from git tracking, or consciously document why they remain.
- [ ] Add LaTeX byproducts to `.gitignore`.
- [ ] Decide whether the tracked PDF stays as an endorser-facing artifact.
- [ ] Decide whether the two paper figures should be committed, bundled for arXiv only, or intentionally omitted in source builds.
- [ ] Visually inspect the regenerated PDF for overfull-box fallout.
- [ ] Fill email placeholders and choose final endorsement recipient(s).
- [ ] Confirm final `git status` contains only intentional files.
- [ ] Optionally rerun `python verify.py --start 3 --stop 14` immediately before the tag if any result-facing files changed.

Not blockers if no result artifacts changed:

- Re-running the long certification search.
- Rewriting theorem statements or numerical tables.
- Adding new bibliography entries without verified metadata.

## 8. Commands Run and Results

- `rg -n ... paper_assets/ringmin_paper.tex README.md ENDORSEMENT_SUMMARY.md SUBMISSION_CHECKLIST.md endorsement/email_templates.md .gitignore CITATION.cff .github/workflows/ci.yml`: located title, abstract, introduction, ledger, related work, AI disclosure, templates, and checklist references.
- `Get-Content` line-range inspections: reviewed `ringmin_paper.tex`, `email_templates.md`, `.gitignore`, `README.md`, `ENDORSEMENT_SUMMARY.md`, `SUBMISSION_CHECKLIST.md`, `CITATION.cff`, and CI workflow.
- `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short --untracked-files=all`: clean before creating this report; sandbox emitted warnings about unreadable global git ignore.
- `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --stat`: no working-tree diff before creating this report.
- `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin ls-files -s ...`: confirmed `ringmin_paper.pdf`, `.aux`, `.log`, and `.out` are tracked.
- `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin check-ignore -v ...`: confirmed `paper_assets/figures/` and `figures/` are ignored; LaTeX PDF/log/aux/out are not ignored.
- `rg -n "(^!|Error|Warning|Overfull|Underfull|Rerun|undefined|multiply defined)" paper_assets/ringmin_paper.log`: found hyperref PDF-string warnings and three overfull boxes; no fatal LaTeX error in the log.
- Abstract/title count via PowerShell regex: abstract 2404 characters / 325 words; title 109 characters.
- `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check`: clean before creating this report.
- `python -m pytest`: 12 passed.
- `python verify.py --start 3 --stop 8`: PASS for all `n=3..8`.

Failed or retried commands:

- Initial git commands without `safe.directory` failed under the sandbox due dubious ownership; rerun with `-c safe.directory=...` succeeded.
- One parallel `rg` scan of the LaTeX log hit a sandbox ACL helper error; rerun separately succeeded.

## 9. Files Changed

- Added `SUBMISSION_REVIEW_REPORT.md`.

No certified result artifacts, paper source, generated paper artifacts, email templates, or git metadata were modified.

## 10. Final Recommendation

The human reviewer should inspect the current PDF visually, then make the abstract/artifact-policy decisions before tagging. The most important next edit is the abstract reduction; after that, clean up LaTeX byproducts and decide whether the release should include a tracked PDF and/or tracked figure assets. Once those are resolved, `v0.1-submission` looks appropriate.

## Fix pass results

Date: 2026-06-16

1. Files changed.
   - `.gitignore`: added LaTeX byproduct ignores; kept only the two TeX-included paper figures trackable under `paper_assets/figures/`.
   - `paper_assets/ringmin_paper.tex`: replaced only the abstract. New abstract count: 189 words, 1383 characters after whitespace normalization.
   - `paper_assets/ringmin_paper.pdf`: regenerated by one successful LaTeX pass.
   - `paper_assets/figures/radii_vs_n.png` and `paper_assets/figures/n14.png`: added to tracking as the two figure assets included by the paper source.
   - `endorsement/email_templates.md`: minimally scoped the `math.MG` and follow-up templates to distinguish proved chain ordering, certified `n <= 14`, and heuristic/conjectural larger-`n` behavior.
   - `SUBMISSION_CHECKLIST.md`: recorded current category strategy: primary target `math.MG`, use `math.CO` framing for Monge/Supnick/TSP researchers, consider `cs.CG` only if a computational-geometry endorser recommends it.
   - `SUBMISSION_REVIEW_REPORT.md`: appended this section.

2. Files removed from tracking.
   - `paper_assets/ringmin_paper.aux`
   - `paper_assets/ringmin_paper.log`
   - `paper_assets/ringmin_paper.out`

   These were removed with `git rm --cached`; the files remain on disk after LaTeX compilation but are now ignored by `.gitignore`.

3. Commands run.
   - `python -m pytest`
   - `python verify.py --start 3 --stop 8`
   - `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check`
   - `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex`
   - `rg -n "(^!|Error|Warning|Overfull|Underfull|Rerun|undefined|multiply defined|Label\(s\) may have changed)" paper_assets/ringmin_paper.log`
   - git status/diff/ignore checks for the artifact policy

4. Command results.
   - `python -m pytest`: `12 passed`.
   - `python verify.py --start 3 --stop 8`: PASS for all `n=3..8`.
   - `git diff --check`: clean.
   - First sandboxed `pdflatex`: failed before TeX processing with `fatal: Can't get long name for C:\Users\Falker\AppData`.
   - Escalated `pdflatex`: succeeded; output `paper_assets/ringmin_paper.pdf` with 10 pages, 541590 bytes.
   - Second escalated `pdflatex`: not run; the environment rejected the elevated command because the usage limit was hit.

5. Whether the PDF was regenerated.
   - Yes, by one successful LaTeX pass. Because the second pass was blocked, the PDF should be regenerated once more before tagging.

6. Warnings requiring visual inspection.
   - The LaTeX log still reports three hyperref PDF-string warnings around line 178.
   - The log reports overfull boxes at lines 259--260, 286--292, and inside `appendix_tables.tex` lines 26--48.
   - The log reports `Label(s) may have changed. Rerun to get cross-references right.`

7. Remaining blockers before `v0.1-submission`.
   - Run a second LaTeX pass and visually inspect the regenerated PDF.
   - Fill actual endorsement email placeholders: recipient, PDF link, repository link, arXiv endorsement code/link, and proposed category.
   - Confirm final `git status` contains only intentional changes.
   - Do not tag until the human reviewer accepts the PDF/artifact policy and category strategy.

## Final pre-tag cleanup results

Date: 2026-06-16

1. Files changed in this final pass.
   - `paper_assets/ringmin_paper.tex`: changed only the certified-results section title to use `\texorpdfstring{$n\le 14$}{n <= 14}` for PDF bookmarks.
   - `paper_assets/ringmin_paper.pdf`: regenerated by the final LaTeX passes.
   - `SUBMISSION_REVIEW_REPORT.md`: appended this final cleanup section.

2. Commands run.
   - `python -m pytest`
   - `python verify.py --start 3 --stop 8`
   - `git diff --check`
   - `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check`
   - `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex`
   - `rg -n "(^!|Error|Warning|Overfull|Underfull|Rerun|undefined|multiply defined|Label\(s\) may have changed|Package hyperref)" paper_assets/ringmin_paper.log`
   - git status/ignored checks for LaTeX byproducts

3. Command results.
   - `python -m pytest`: `12 passed`.
   - `python verify.py --start 3 --stop 8`: PASS for all `n=3..8`.
   - Plain `git diff --check`: failed under the sandbox's Git safe-directory behavior.
   - `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check`: clean.
   - Sandboxed `pdflatex`: blocked before TeX processing with `fatal: Can't get long name for C:\Users\Falker\AppData`.
   - Escalated `pdflatex`: succeeded twice. The first pass regenerated changed outline data; the second pass settled it. Final output: `paper_assets/ringmin_paper.pdf`, 10 pages, 541598 bytes.

4. Remaining warnings after the final compile.
   - Cross-reference warnings are gone; no `Label(s) may have changed. Rerun to get cross-references right.` remains in the final log.
   - Hyperref PDF-string warnings are gone; the previous math-in-bookmark warning for the results section no longer appears.
   - Rerun/outlines warnings are gone; no `rerunfilecheck` rerun warning remains.
   - Three overfull boxes remain: `paper_assets/ringmin_paper.tex` lines 259--260, `paper_assets/ringmin_paper.tex` lines 286--292, and `paper_assets/appendix_tables.tex` lines 26--48. These were not aggressively fixed; human visual PDF inspection should decide whether they matter.

5. Artifact policy status.
   - `ringmin_paper.pdf`, TeX source, and the required paper figures remain tracked.
   - `.aux`, `.log`, and `.out` remain removed from tracking and ignored; current status shows their cached deletions plus ignored local build copies.
   - No `.toc`, `.synctex.gz`, `.fls`, or `.fdb_latexmk` files are tracked in the checked status set.

6. Readiness.
   - The PDF was regenerated successfully.
   - The repo is ready for human visual PDF inspection.
   - No known technical blockers remain before `v0.1-submission`; the remaining gate is human visual review and final acceptance of the intentional working-tree changes.
