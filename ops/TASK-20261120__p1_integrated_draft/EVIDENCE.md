# Verification evidence

## Environment and source identity

Windows 11, CPython 3.14.3, NumPy 2.4.3, mpmath 1.3.0, Matplotlib 3.10.9, pytest 9.0.2 and pypdf 6.14.2. Document builds used pdfTeX 1.40.28 (TeX Live 2025) and Poppler. The build script fixes the source epoch, suppresses PDF time metadata and uses a new temporary directory on each run.

| Input | Revision or identity |
| --- | --- |
| PR #7, journal base | `56a9b999925ab61a0217273adf8f61a9b176c5e4` |
| PR #9, general pipeline and certificates | `d93fca92714fc9e59e69ed036fab734c9c5edb2d` |
| Common ancestor and target main at preflight | `c26400b328c2f8fa338b588e61abb98266a265f9` |
| Ordinary merge of both source revisions | `a437cc86ad6393c6c2f9b2f86ffa81ef96637aeb`, with PR #7 as first parent and PR #9 as second parent |
| Canonical quadratic TeX input | Git blob `4b6794222812281213e99401c0d7d81c9c94d18a` on PR #9 |
| Original linear certificate field | SHA-256 `6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0` |
| Paper II derivations | [Profile limit and finite-template bound](https://github.com/falker47/ringmin/blob/f2f46294a1cfb869b36ecc147d5b19df432214b3/paper_assets/paper_ii_profiles/profiles_section.tex) and [certified limiting ceilings](https://github.com/falker47/ringmin/blob/eb9467dfa1429d622402e26e2f33017f984d2b1f/paper_assets/line_upper/NOTE.md) |

## Claim and verification scope

| Claim | Classification and evidence |
| --- | --- |
| Original anti-Monge and chain statements for arbitrary distinct positive radii, seam statements for consecutive integers | Existing exact theorems and corollary. Original statement, equation and seam appendix digests checked by the journal regression. |
| Linear brackets, sizes 3 through 14 | Computer-certified finite results, independently reproduced by a second implementation. Its generator was given the original endpoints and a candidate order per size. Local exact replay verifies the evidence at those endpoints. |
| Quadratic brackets, sizes 3 through 14 | Computer-certified finite results. The independent standard-library verifier rechecks every certificate. The printed endpoints were matched against all twelve exact rational pairs. A separate rational Descartes comparison checks the three-circle row. |
| General coverage and strict lower endpoint | Written counting argument and proved strictness corollary from the PR #9 method. Scope requires distinct labels, at least three retained labels, a successful lower audit and an exact feasible upper witness. |
| Two asymptotic limits and ceilings | Cited results of revised Paper II. The quadratic ceiling combines the finite-template inequality with its line witness. The public record on 20 November 2026 still lists v3. The draft's submission dependency is explicit. [arXiv record](https://arxiv.org/abs/2609.13630) |
| Reported outside review | The author supplied the November 20 report of floating-point enumeration through linear size 8 and quadratic size 9, and comparisons with the four guarded small-size intervals. These are attributed cross-checks. The local work independently checked the three-circle identity and the certificates. |

## Pre-merge commands and checks

The original linear verifier ran on the dedicated worktree. The general verifier ran on the input checkout at the PR #9 SHA. For pre-merge manuscript QA, an isolated working directory held the journal package, its test, the original witness input and read-only copies of the PR #9 table and certificates. In the combined test command below, `<proof>` denotes that temporary source root.

| Command or check | Local result and meaning |
| --- | --- |
| `python -I -S paper_assets/general_radii/verify_radii_certificate.py --all` | Exit 0. All 24 files printed `PASS`. Both size-14 rows printed `classes=3113510400`. The checker independently replays the lower partition, strict buffer and rational witnesses. |
| `python -I -S verify_global_brackets.py` | Exit 0, `PASS_GLOBAL_BRACKETS`, `pinned_input_verification=PASS`. 908 angle enclosures, 47 witnesses, 540 central tangencies, 3,004 outer pairs, 6,008 directed angular inequalities, 268,648 explicit and 3,374,988,556 total order classes. |
| `python paper_assets/journal_p1_v5/make_figures.py` and a second invocation with `--output-dir` | Exit 0, `PASS_WITNESS_14 central=14 strict_outer_pairs=91`. Compared all six PDF files byte for byte. The regression also renders with hash seeds 12 and 47. Five figures match PR #7 exactly. |
| `python paper_assets/journal_p1_v5/build.py` and a second invocation with `--output` | Both exited 0 with `PDF pages=21 before_appendices=12 appendix_starts=13 overfull_boxes=0 pdflatex_passes=3 unresolved=0`. The files are byte-identical. |
| `python -m pytest -p no:cacheprovider tests <proof>/tests/test_journal_p1_v5.py` from the PR #9 checkout | Exit 0, `93 passed in 71.19s` on the final draft and builder. Two previous runs also passed. Includes the general-radii oracles, the original tests and the seven journal tests. Bytecode output was disabled in the input checkout. |
| `python -m pytest` in the dedicated pre-merge worktree | Exit 1, `1 failed, 65 passed in 63.57s` on the final files. The earlier run had the same failure in 63.71s. The new source-to-plot regression raised `FileNotFoundError` for `paper_assets/general_radii/quadratic_brackets.tex`. This path belongs to the unmerged PR #9. The same regression passed with the canonical input available. |
| `python -m ruff check paper_assets/journal_p1_v5/build.py paper_assets/journal_p1_v5/make_figures.py tests/test_journal_p1_v5.py --no-cache` | Exit 0, `All checks passed!`. Static Python checks. |
| Exact arithmetic, independent of either verifier | `PASS_DESCARTES_QUADRATIC_03 exact signs +,-`. With the three reciprocal radii, let s be their sum and t the sum of their pairwise products. Rational arithmetic gave 1/U > s and (1/L − s)² > 4t > (1/U − s)² for the stored endpoints. |
| PDF text and visual checks | pypdf found the exact title, both verifier commands, the three limit constants and all 24 quadratic endpoint strings. Searches returned zero unresolved markers, upper-bound placeholders, TODO, TBD or FIXME. Poppler page renders showed the legible table and both normalized series on page 10, reproduction and declarations on page 11, references before the appendices, and the new proof on pages 20–21. |
| Original content comparison | The six main theorem-family statements, fourteen numbered equation environments, literal original table bodies, three inherited TeX inputs and original declaration block satisfy the v4 digest tests. Separate source comparisons matched author/affiliation/date and the text of Appendix B. The new main-text table shifts the printed numbers of the three appendix tables by one. |

## Artifact identity

SHA-256 of the rendered manuscript is `1669602260c64e0b183989c8ccc8d925893019be984ff66df5c67a5b78154cc1`. Figure 5 is `10818bdee83bd9edc7f8f8f5929dad0bd609ce14120f37711d442de2db4e8c18`. The PR #9 Git blob for the quadratic table has SHA-256 `47b5545f972a72bfcc7514455f7392a90b7f978228136527c440653b80c6251f`. These PDF identity checks concern the recorded renderer and fonts.

The editorial generation sources are task-local edits based on PR #7. SHA-256 over UTF-8 text with LF newlines identifies `main.tex` as `4b1da36a0166a539c9077507eced677dd6946c919091fa6fc3dc67aac818b349`, the figure generator as `04822dc91c60b2abc9cb6676d55978254812a20b74ad6c3bcfefee820935789a`, and Appendix C as `db574b4da22d4591894aad95aa19717546ce746532ae77eaddac60851bf0487e`.

Two builds using direct overwrite exited 1 when Windows rejected opening the existing output for truncation. Both had completed all three TeX passes. The prior PDF digest survived both attempts. With same-filesystem staging and replacement, the default build on that path exited 0 and the delivered 488,956 bytes matched the independently generated output. The updated build script has LF-normalized SHA-256 `a1b1de1f08f9a1fbc281c89a781bd41eb8b2f73f4a51630043bbd15f3aba6832`.

## Working-tree inspection

Reviewed the tracked diff against the journal base and read each of the five untracked additions. The two PDF changes are Figure 5 and the manuscript. `git diff --check` exited 0. A separate byte-level whitespace check covered all 15 changed text files, including all five additions, and found no trailing whitespace or missing final newline. `git status --short --untracked-files=all` listed 17 task paths and the diff excluding the three allowed path groups was empty. The original main checkout retained its pre-existing untracked v2 archive.

## Integrated worktree verification

After the author's direct confirmation, `git merge --no-ff --no-autostash -m "Merge general-radii certification into the Paper I journal draft" origin/codex/p1-general-radii-certification` exited 0 with the merge made by the ort strategy. Comparing `git ls-tree -rz` for the common ancestor, both parents and the merge established equality of the complete merged tree with the union of the two disjoint changes, including blob identities and modes. The 17 local editorial and dossier files retained their pre-merge digests.

| Command or check on the merged branch | Local result and scope |
| --- | --- |
| `python paper_assets/journal_p1_v5/build.py` | Exit 0. Three pdfLaTeX passes, 21 pages, 12 before Appendix A on page 13, zero overfull boxes and zero unresolved references or citations. |
| `python -I -S paper_assets/general_radii/verify_radii_certificate.py --all` | Exit 0. All 12 linear and 12 quadratic certificates passed. Each size-14 replay covered 3,113,510,400 cyclic classes. |
| `python -I -S verify_global_brackets.py` | Exit 0. `PASS_GLOBAL_BRACKETS` and pinned input verified. The counts agree with the original replay above. |
| `python -m pytest` | Exit 0, `93 passed in 63.24s`. Set `PYTHONPATH` to the worktree's absolute `src` directory for this process and checked `ringmin.__file__` before running the default suite. This includes the previously unavailable canonical-table regression. The isolated verifiers ran as separate processes. |
| `python paper_assets/journal_p1_v5/make_figures.py` | Exit 0, `PASS_WITNESS_14 central=14 strict_outer_pairs=91`. Regenerated all six figures, then reran the figure generator and the three-pass build into temporary destinations and compared each PDF byte for byte. All seven matched. |
| Independent PDF and source comparison | Exit 0. PDF text contains all 24 quadratic endpoints from the exact rational certificate files, all three limit constants and both replay commands. Zero unresolved markers or placeholders. The first raw working-copy comparison of the two quadratic tables found the Windows checkout had added CRLF line endings. Both sources matched the PR #9 Git blob after LF normalization. |
| `python -m ruff check paper_assets/journal_p1_v5/build.py paper_assets/journal_p1_v5/make_figures.py tests/test_journal_p1_v5.py --no-cache` | Exit 0, `All checks passed!`. |

The staging command listed the 17 authorized paths explicitly. Git returned exit 1 for the existing `figures/` ignore rule. Readback of the index showed that both tracked figure paths and all 15 other task paths had been staged. A blob comparison against the working files confirmed their content, including both binary PDFs. The staged quadratic table has the same Git object ID as the canonical PR #9 table. The unstaged diff was empty, and `git diff --cached --check` exited 0. The full staged diff contained 13 journal files, one test and the three dossier files.

The integrated draft PR is the handoff for independent mathematical and editorial review. The revised Paper II publication requirement applies before journal submission.
