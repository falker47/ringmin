# Exact global brackets for prescribed integer radii

The 24 certificates give exact rational intervals $L<R^*\le U$ of width $10^{-11}$ for the linear and quadratic radii families, for every $n=3,\ldots,14$. The quadratic results refine the four earlier guarded intervals through $n=6$ and extend the exact calculation through $n=14$. A standalone verifier reproduces both endpoints' proof obligations from each file. [Results and scope](RESULTS.md) · [Method and proof](METHOD_NOTE.md)

## Verification

From the repository root, run the following commands with Python 3.11 or newer. The standalone checker uses only the standard library under isolated mode.

```console
python -I -S paper_assets/general_radii/verify_radii_certificate.py --all
python -I -S paper_assets/general_radii/verify_radii_certificate.py paper_assets/general_radii/certificates/quadratic_14.json
python -I -S verify_global_brackets.py
python -m pytest tests/test_general_radii.py
```

A verified file prints `PASS`, its size $n$ and the full number of cyclic-order classes. A failed proof exits nonzero with a reason. The original Paper I verifier remains a separate regression.

## Exact endpoints

Each decimal in this table represents its exact rational value. The last two columns give wall-clock seconds per generated JSON on one local Windows 11 run with CPython 3.14.3 and mpmath 1.3.0, including process startup and output comparison. Machine load affects timings.

| $n$ | Linear $L$ | Linear $U$ | Quadratic $L$ | Quadratic $U$ | Linear s | Quadratic s |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0.26086956521 | 0.26086956522 | 0.38338703613 | 0.38338703614 | 0.293 | 0.313 |
| 4 | 0.84445358956 | 0.84445358957 | 1.49562841187 | 1.49562841188 | 0.319 | 0.324 |
| 5 | 1.69549408120 | 1.69549408121 | 3.93432771714 | 3.93432771715 | 0.303 | 0.333 |
| 6 | 2.79491951889 | 2.79491951890 | 8.46793507608 | 8.46793507609 | 0.279 | 0.343 |
| 7 | 4.15318955374 | 4.15318955375 | 15.00637525781 | 15.00637525782 | 0.290 | 0.454 |
| 8 | 5.76779428458 | 5.76779428459 | 24.81845494656 | 24.81845494657 | 0.337 | 0.337 |
| 9 | 7.72672655261 | 7.72672655262 | 37.92684891176 | 37.92684891177 | 0.345 | 0.363 |
| 10 | 9.97990738586 | 9.97990738587 | 54.90598352079 | 54.90598352080 | 0.324 | 2.261 |
| 11 | 12.48872048718 | 12.48872048719 | 76.60997082351 | 76.60997082352 | 0.294 | 0.401 |
| 12 | 15.25887043044 | 15.25887043045 | 103.29187664743 | 103.29187664744 | 0.297 | 0.903 |
| 13 | 18.31756304721 | 18.31756304722 | 135.45085966939 | 135.45085966940 | 0.345 | 0.993 |
| 14 | 21.66539518221 | 21.66539518222 | 173.72227944147 | 173.72227944148 | 2.550 | 3.993 |

## Reproduction and arbitrary inputs

The generator requires mpmath. For the linear regression it reads the public Paper I v4 endpoint table from `.codex_inputs/arxiv/p1_v4/bracket_rows.tex` and takes one word per row from the tracked original certificate. The quadratic search uses only $n$. Run each family command for the desired values of $n$.

```console
python paper_assets/general_radii/certify_radii.py --linear 14 --output linear_14.json
python paper_assets/general_radii/certify_radii.py --quadratic 14 --output quadratic_14.json
python paper_assets/general_radii/certify_radii.py --radii 2 5 17 38 --delete 1 --digits 6 --output custom.json
python -I -S paper_assets/general_radii/verify_radii_certificate.py custom.json
```

The output location is supplied explicitly. Acceptable inputs are at least three distinct positive integers. The generator sorts them. `--delete d` selects the $d$ smallest radii for insertion, with $0\le d\le n-3$. For prescribed endpoints use `--lower` and `--upper` with rational or terminating decimal values. A known upper witness order may be supplied with `--order`, as the actual radius values. Automatic search bisects the radius grid of step $10^{-\text{digits}}$, using shortest-path feasibility on surviving orders. It may enlarge the upper endpoint by one grid step to construct strict rational separation. `--bits` controls the proposal grid when finer angular resolution is needed. All committed rows use 128 bits.

The search is deterministic. Each family was regenerated independently in a temporary directory and all 24 files matched byte for byte. The dossier records the hashes, commands, scope and failed exploratory runs. [Evidence](../../ops/TASK-20261119__p1_general_radii_certification/EVIDENCE.md)

The paper-ready quadratic table uses `booktabs`. [LaTeX table](quadratic_brackets.tex)
