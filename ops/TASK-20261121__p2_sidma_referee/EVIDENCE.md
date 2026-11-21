# Evidence

## Scope and environment

Reviewed `falker47/ringmin` at `5aec65c85c3436e7f0cebead37460bc085307fec` on Windows 11 build 26300, CPython 3.14.3, python-flint 0.9.0, pytest 9.0.2 and TeX Live 2025 (pdfTeX 1.40.28). Mode STRICT. The mathematical review and finite replay target the SIDMA article and supplement, including the two cited data sources. Scientific statements and their limitations are indexed by theorem in the [report](../../docs/referee/p2-sidma-referee-2026-11.md).

## Local commands and results

Commands below start at the repository root. The process, supplemental regression and hosted checks have different evidence roles.

| Command or check | Exit and observed result | Property checked |
|---|---|---|
| `git ls-remote origin refs/heads/codex/p2-sidma-format refs/heads/codex/p2-sidma-referee` at startup | 0; only the base at `5aec65c85c3436e7f0cebead37460bc085307fec` | Live target before creating the review branch. |
| `python -I -B independent_check/p2` | 0; `130 passed, 0 failed` | One macro inventory, 28 line and printed-upper items, 49 lower items, four historical/elementary comparisons and 48 finite-figure items. Arithmetic independent of repository implementations. |
| `python -I -B -m unittest discover -s independent_check/p2` | 0; `Ran 4 tests`, `OK` | Mutations of line data, a bound, KKT and certificate intervals; 24 comparisons to unpruned enumeration; swapped endpoint directions and colliding Cartesian centers. The unpruned control shares the fixed-order angular engine. |
| `python -m ruff check --no-cache independent_check/p2` | 0; `All checks passed!` | Static Python checks. |
| `python -I -S paper_assets/journal_p2_sidma/build.py --output-dir <scratch>` | 0; `main.pdf: 10 pages; 3 passes; final log clean (overfull limit 1 pt)`; same for S1 with 13 pages | Rebuilt both using the packaged SIAM class and the project's pinned epoch. `<scratch>` was an empty external build destination. |
| Text extraction with `pypdf.PdfReader`, page-by-page comparison; `git diff --cached` PDF text driver | Changed extracted pages `[10]`; bibliography lines 360–361 only. S1 rebuild identical byte for byte. | Local source/PDF synchronization for the single erratum; the extraction does not establish theorem correctness. |
| `python -m pytest -q tests/test_journal_p2_sidma.py` | 0; five tests passed | Existing scientific-text freeze, citation keys/DOIs, figures and companion identity. Production-coupled regression. |
| Full local suite, invocation below | 0; `109 passed, 4 subtests passed in 58.78s` | Existing regressions with this checkout's `src` first on `PYTHONPATH` and all five external fixtures available. |
| `git diff --check` and `git diff --cached --check` | 0, no diagnostics for the inspected task changes | Whitespace, including additions once staged. Full staged diffs were reviewed. |

Full-suite command with a valid inherited input handle on Windows:

```powershell
python -c "import subprocess,sys,ringmin; print(ringmin.__file__, flush=True); sys.exit(subprocess.run([sys.executable,'-m','pytest','--capture=no','-ra'],stdin=subprocess.DEVNULL).returncode)"
```

The first `python -m pytest -q` returned 1 with thirteen `WinError 6` failures in subprocess creation. Replacing the invalid input handle with `DEVNULL` and disabling pytest capture returned 0 with 108 passes, one missing-fixture skip and four subtests. The final run above temporarily supplied the existing Paper I v4 table and four quadratic JSON files (`n=3..6`) from the profile setup and confirmed import from the review checkout. The clean-room command needs none of those external fixtures or the installed ringmin package.

## Independent evidence and controls

- **Line upper bounds.** The clean-room program compares squared cross-products of integer coordinates for every unordered pair, validates the permutation and extrema, and bounds $\pi$ on both sides by alternating rational sums. Every certificate passes. The 3200-label witnesses each require 5,118,400 comparisons. Generation/search scores are unnecessary. The TeX table, both repeated abstract values and their outward precision are checked.
- **S1.** Recover the root of $\cos t-t$ from its full domain, compute the three $D_i$ by independently integrating a semicircle primitive, and isolate $G=0$ by monotone sign bisection. Propagate 320-bit Arb balls to the gradients, multipliers and width objective. All numerical JSON intervals, the companion copy, main/S1 endpoint expressions and the finite threshold/residue arithmetic pass. The all-order deletion and limiting steps are analytic premises reviewed in the report.
- **Historical four-block cost.** Source is the block-cost equation in the cited preprint. For each reflected or diagonal piece, both $t/X$ and $t/Y$ increase. Rational bisection localizes the one possible switch. Arb integrates each smooth branch with analytic branch-cut checking; the leftover strip contributes between zero and three times its length. The integral is divided by $4\pi$. This independent replay checks the fixed decimal interval; the earlier general recovery theorem is imported.
- **Figure 2.** Outward rational angle ticks and an exact minimum adjacent completion DP exclude partial orders safely. Descending insertion after deletion covers all completions of every surviving order, up to rotation and reversal. All-pairs difference inequalities are necessary at each stage. For upper checks the program constructs potentials with $10^{-26}$ radians of extra slack per inequality. It tests every pair of reconstructed Cartesian centers by 256-bit balls. Passed 12 lower exclusions and 47 upper orders. The 24 small brute-force controls agree. A separate PDF coordinate readback found all 12 markers and 24 cap positions within $5\times10^{-7}$ PDF points of the expected normalized coordinates.
- **Additional failure probes.** During development eight upper mutations were rejected, including an all-adjacent-pass/nonadjacent-fail placement, a truncated ceiling, duplicate label, float coordinate, incorrect span, and changes to the abstract, table or macro. Eight lower probes detected corruptions in printed or saved bounds, including a false active-constraint multiplier. The tracked control suite preserves representative cases.

## Input binding and protected assets

Raw SHA-256 values below identify the locally read files. The review generated no replacement certificates.

| File | SHA-256 |
|---|---|
| `line_upper/certificates/p1_n03200.json` | `2c27bf208d7b4e9a7faa99f8842d6cd84c7423276b4660f6023b8c468bb4a836` |
| `line_upper/certificates/p2_n03200.json` | `9fd0f928d06f3b4af9c2c758b1b2410a80974b5ddd7a5cf54bb7b199c4373e04` |
| `asymptotic_sequel/proposition7_supplement/certificate.json` | `d8cf058a5d31a2651e603e14b907b09445b2cf563b9142a71d20e47517a1de46` |
| SIDMA `main.pdf` before and after the citation correction | `279aa9bae7b661bc32167e1605b28fba247e187ac9df9b34409e944a50ebe2dc` → `9b3b9e599574de54bfa45bf0b8c421e8590d7f7b40702faf8927de8b51daba69` |
| SIDMA `supplement.pdf` | `3bc5dfcc41fe7957b8c9981729de001de75988e80a09440c7a11ee698afbfaac` |
| SIDMA `s1_support.zip` | `6e083d0e8b52d6bd32d57859c946e38854cb637fd30695b3935307b605fdd33d` |

The 13 companion archive members match the frozen package. The line files are the witness format from `eb9467d`. Article PDF generation used `c045357`'s bibliography and the base build script/TeX inputs. Pre-existing historical publication packages, raw data, manuscript TeX (including declaration and date), covers, figures, and production code are outside the diff. The main checkout's unrelated untracked finite-paper archive was left in place.

## Review limits and final inspection

The working changes, full staged diff, protected-path diff against the base and whitespace checks were inspected before push. The review provides an independent numerical implementation and an internal review of analytic proofs. It does not formally verify the proofs, determine sharp constants, establish priority against all literature, or decide a venue's acceptance. The external quadratic result is cited from its pinned proof. The two limiting upper certificates establish feasible constructions regardless of heuristic search quality. Exact-head hosted conclusions are recorded in the draft PR's checks and handoff, separately from this local record.
