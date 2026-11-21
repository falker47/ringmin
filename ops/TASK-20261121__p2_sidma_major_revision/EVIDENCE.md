# Revision evidence

## Environment and inputs

Clean revision base `b70e280203b8261814de2eb669ed752b2b31a86c`, Windows, CPython 3.14.3, pytest 9.0.2, python-flint 0.9.0, pdfTeX 1.40.28 (TeX Live 2025). The referee report and its numbering refer to that base. The PDF generation sources, SIAM distribution and products are versioned together in the revision commit. The build pins `SOURCE_DATE_EPOCH=1793664000`.

## Claim and source map

| Referee baseline | Revised article | Evidence and scope |
|---|---|---|
| Lemmas 2.2–2.3, 5.1 | Lemmas 2.2–2.3, Corollary 3.3 | Exact all-pairs comparison for bounded marks and its integer specialization. A gap of length M pays for either the complementary arc or all cross-word pairs. |
| Lemma 5.2, Theorems 5.3 and 3.1 | Lemma 3.1, Theorem 3.2, Corollary 3.3 | Exact analytic limit for every weakly converging bounded array and positive scales. Donor indices cover every larger sample size. Sorted-root path sensitivity gives law stability. Uniform marks and integer radii follow by substitution. |
| Theorems 5.4 and 4.1 | Theorem 4.1, Corollary 4.2 | Exact variational brackets. For the lower direction take q divisible by r; the full finite-type limit already exists. A rational vertex gives an exact integer batch for the upper direction. Effective numerical access for arbitrary laws requires quantile input. |
| Corollaries 5.5–5.6 | Corollaries 4.3–4.4 | Exact adjacent-pair bound and fixed-power limiting statement. Alternating positive/zero marks and the rational-indicator grid are exact examples of the law and sampling hypotheses. |
| Proposition 6.1, Remark 6.2 | Proposition 5.1, Remark 5.2 and square comparison | Independently replayed finite rational upper witnesses and fixed four-block integral. [Quadratic source](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/ALL_N_LOWER_BOUND.md), (22)–(23), supplies the external liminf and limsup bounds. The lower combined bracket is conditional in the distributed PDF. Its proof was outside this replay. |
| Proposition 7.1, Figure 2 | Proposition 6.1, Figure 2 | The existing analytic S1 lower bound, directed arithmetic for its expression, and 12 finite global brackets retain their separate evidence. Section 7.1 distinguishes the finite ring/line error, structural LP width, and sampling error. |

The two new sections are expository proof reorganizations. The analytic checks above are by inspection. The finite replay verifies numerical results and witnesses. The mathematical ledger, ranked research priorities, certificate data and arXiv snapshots consequently required no change.

## Local verification

| Command or comparison | Result | Scope |
|---|---|---|
| `python -I -S paper_assets/journal_p2_sidma/build.py` | Exit 0. `main.pdf: 10 pages; 3 passes; final log clean (overfull limit 1 pt)`. S1 reported 13 pages with the same clean log. | SIAM/BibTeX build with reciprocal references. Baseline counts read directly from both tracked PDFs were 10 and 13. |
| Same build with `--output-dir` in an empty scratch destination | Exit 0. Both PDFs identical by byte comparison. | Reproduction under the recorded toolchain. |
| Scratch copy of the package with only the two-argument selector changed to the first argument | Exit 0. Both PDFs built. PDF text selected “Taking its lower bound as given” for the distributed copy and “Its lower bound and Proposition” for the alternate copy. | Editorial switch and rendered wording. This does not verify the external proof. |
| `python -I -B independent_check/p2` | Exit 0. `130 passed, 0 failed`. | Independent arithmetic for the existing line certificates, S1 lower expression, uniform word-width example, elementary quadratic bound, four-block comparison and finite brackets. Manuscript lookups for the LP and corollary follow their new source file. |
| `python -I -B -m unittest discover -s independent_check/p2` | Exit 0. `Ran 4 tests ... OK`. | Negative controls and small unpruned enumeration comparisons. |
| Full pytest suite (command below) | Exit 0. `110 passed, 4 subtests passed in 63.17s (0:01:03)`; zero skips. | Includes every optional fixture and the revised regression tests. This suite exercises repository code. |
| `python -m ruff check --no-cache independent_check/p2` and the same check on `tests/test_journal_p2_sidma.py paper_assets/journal_p2_sidma/build.py` | Both exit 0. `All checks passed!` | Changed Python and independent checker static checks. |
| Poppler rendering, pypdf text and page comparisons against Git base | Article 10 → 10, supplement 13 → 13. In S1 only page SM1 changes extracted text, from the article's Proposition 7.1 to 6.1. | Page 1 contains the convergence statement, the contrast with uniform v3 and the upper improvements. Page 2 gives the finite shelf comparison. Visual inspection covered both documents. |
| Supplemental finite donor-index check | Every index with 2 ≤ n ≤ m ≤ 120 satisfied the comparison. | Spot check supporting the general algebraic identity in Lemma 3.1. |

On Windows the final full-suite command used the worktree's package and a valid subprocess input handle:

```powershell
$env:PYTHONPATH = (Resolve-Path src).Path
python -c "import pathlib,subprocess,sys,ringmin;print(ringmin.__file__, flush=True);assert pathlib.Path(ringmin.__file__).resolve().is_relative_to(pathlib.Path('src').resolve());sys.exit(subprocess.run([sys.executable,'-m','pytest','--capture=no','-ra'],stdin=subprocess.DEVNULL).returncode)"
```

One Paper I bracket table and four quadratic small-n fixtures were temporarily copied from the existing profile verification setup. All five matched the source SHA-256 values and were removed after the test.

## Artifact binding

| Output or source | Raw SHA-256 in the build worktree |
|---|---|
| main.pdf | `e56d4c31e095ee3f20948387105d6ee4a4936c5d27cfdede92d25101619aeffa` |
| supplement.pdf | `bcc50dc7752975a07eb5c34ae08e4ed1dfc29411a4b6f6ddad6a8567caea5680` |
| main.tex | `f9790a2b442a900688e2682849ea5221d37b4a9565df36e28bc9a59f0a5b4901` |
| sections/law.tex | `4df61d2a305bf8ab81e9ebbe97d945e062cbdbb587d8595b6d74345bf6768ec8` |
| sections/words.tex | `30daea2b403a7493d98ab968c6fad6cbc5cd3365465ea6dbc1ef51e606a29605` |
| sections/worked_lp_example.tex | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (zero bytes) |
| references.bib | `8f5389f4afbf10f8ecfb8561f4c316743053001602ef0ac4d7ae60115b1b7eb8` |

The bibliography adds the pinned quadratic note. The sources for [shelf packing](https://jocg.org/index.php/jocg/article/view/3056) and the [uniform paper](https://arxiv.org/abs/2609.13630v3) were checked directly for the opening comparison. The historical formula inventory in the SIDMA directory now identifies its applicable version.

## Diff review and limits

The review set covers only the SIDMA revision, checker source locations, their regression tests, the task dossier and current handoff. Checked complete task sources, new files, projected Git paths and whitespace before commit. The abstract, AI-use declaration, date settings, S1 source and supporting archive, certificate inputs, figures, publication packages, cover letters and arXiv metadata are protected. The only committed PDF changes are the requested article and supplement. The source regression compares the full S1 mathematical text with the frozen copy. Hosted CI and the live draft PR are reported separately at the delivered commit. The work selects no sharp constant, optimizer, finite-size convergence rate or journal submission.
