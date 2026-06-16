# ringmin

Exact solver and certificate artifacts for the minimum central circle problem:
circles of radii `1,2,...,n` are externally tangent to a central circle, and the
goal is to minimize the central radius `R`.

The repository certifies the global optimum for `n=3..14` by exhaustive
enumeration of cyclic orderings. The fixed-order feasibility oracle is a
high-precision Simple Temporal Network check over all pairwise angular
constraints; chain-only values are used only as lower bounds.

## Endorser-Facing Summary

This project studies a finite geometric optimization problem about arranging
circles of radii `1,2,...,n` around a central circle while minimizing the
central radius. The paper proves that the chain-ordering lower-bound problem is
a fixed Supnick/anti-Monge TSP, then uses explicit certificate artifacts and an
independent verifier to certify global optima for `3 <= n <= 14`. Results for
larger `n` are reported only as heuristic evidence and conjectural structure.

## Environment

The submission-gate environment is pinned in `requirements.txt` and was:

- Python `3.14.3`
- `numpy==2.4.3`
- `scipy==1.17.1`
- `mpmath==1.3.0`
- `matplotlib==3.10.9`
- `pytest==9.0.2`

Install:

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
```

`pyproject.toml` intentionally leaves runtime dependencies unpinned for normal
editable development; use `requirements.txt` for the exact submission
reproduction environment.

## Quick Verification

These checks are intended for a quick local or CI smoke test. They do not
regenerate the long-run certificates.

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
python -m pytest
python verify.py --start 3 --stop 8
```

If a LaTeX distribution with `pdflatex` is available, compile the paper with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

## Certified Results

The 30-digit values are generated in `results/highprec.csv` and copied into
`paper_assets/appendix_tables.tex`.

| n | R* | optimal cycle | floaters |
|---:|---|---|---|
| 3 | 0.260869565217391304347826086957 | `[3, 1, 2]` | `{}` |
| 4 | 0.844453589560855604347528524674 | `[4, 1, 3, 2]` | `{}` |
| 5 | 1.69549408120271081351328017371 | `[5, 1, 4, 3, 2]` | `{}` |
| 6 | 2.79491951889692485617024406797 | `[6, 1, 5, 3, 4, 2]` | `{}` |
| 7 | 4.15318955374381246513863858202 | `[7, 1, 6, 3, 4, 5, 2]` | `{}` |
| 8 | 5.7677942845896143026361805725 | `[8, 1, 6, 4, 5, 3, 7, 2]` | `{1}` |
| 9 | 7.72672655261128921886246177604 | `[9, 2, 8, 1, 5, 6, 4, 7, 3]` | `{1}` |
| 10 | 9.97990738586347760966552641468 | `[10, 2, 9, 4, 7, 1, 6, 5, 8, 3]` | `{1}` |
| 11 | 12.4887204871876588517468786264 | `[11, 2, 10, 4, 8, 6, 7, 1, 5, 9, 3]` | `{1}` |
| 12 | 15.2588704304484933617250043503 | `[12, 2, 11, 4, 9, 6, 7, 8, 5, 1, 10, 3]` | `{1}` |
| 13 | 18.3175630472173206282821941532 | `[13, 3, 1, 12, 2, 10, 6, 8, 7, 9, 5, 11, 4]` | `{1}` |
| 14 | 21.6653951822145150956462891793 | `[14, 3, 13, 2, 9, 8, 7, 10, 6, 11, 5, 1, 12, 4]` | `{1,2}` |

Certified means global optimality up to absolute tolerance `1e-10` in `R`.
The bisection tolerances are `1e-12`/`1e-13`, and the displayed binding
structures are rechecked to 50 decimal digits.

## Submission-Gate Verification

Run the independent verifier:

```bash
python verify.py --start 3 --stop 14
```

`verify.py` imports only the Python standard library and `mpmath`. It does not
import `src/ringmin`. It checks three layers for every certified `n`:

1. Incumbent feasibility: reloads `results/nNN/optimum.json`, rebuilds the
   theta matrix at 50 digits, checks the saved witness angles, all pairwise
   angular constraints, Cartesian non-overlap, essential pairs, and floating
   circles.
2. Local optimality for the incumbent order: verifies feasibility at
   `R* + 1e-12` and infeasibility at `R* - 1e-12`.
3. Global pruning certificate: reloads `results/frontiers/nNN_frontier.json`,
   verifies enumeration counts, canonicalization metadata, progress-log proof,
   frontier hash, top-excluded guard, and recomputes every frontier lower bound
   at 50 digits.

Current verifier summary:

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

The n=14 frontier was extracted from the existing `K=50000` checkpoint heaps;
no Stage-A rerun was needed.

## Full Certification And Regeneration

The following commands are for full audit or artifact regeneration. They are not
CI checks: the certified sweeps, especially `n=13` and `n=14`, are long-running
jobs.

Run tests:

```bash
python -m pytest
```

Regenerate certified searches:

```bash
python scripts/sweep_certified.py --start 3 --stop 13 --k 20000 --workers 8 --resume
powershell -ExecutionPolicy Bypass -File scripts/start_detached_sweep.ps1 -Start 14 -Stop 14 -K 50000 -Workers 8 -Resume
```

Run the full independent certificate verifier:

```bash
python verify.py --start 3 --stop 14
```

Regenerate high-precision values and certificate metadata:

```bash
python scripts/highprec_verify.py --start 3 --stop 14 --digits 50
```

Regenerate frontier certificates:

```bash
python scripts/extract_frontiers.py --start 3 --stop 14 --margin 2e-10
```

Run the float64-vs-mpmath calibration:

```bash
python scripts/calibrate_float64.py --start 8 --stop 14 --samples 100000 --workers 8 --batch-size 500
```

The current global maximum absolute deviation is
`1.75137506176142662e-14`, below the `1e-11` submission threshold.

Regenerate paper tables, figures, and report artifacts:

```bash
python scripts/refresh_heuristic_artifacts.py
python scripts/free_float_criterion.py
python scripts/patterns_table.py
python scripts/supnick_validity.py
python scripts/asymptotic_fit.py
python scripts/generate_figures.py
python scripts/build_report.py
python scripts/export_paper_assets.py
```

Compile the paper:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

## Run Logs And Data-Generation Hash

The M6 artifacts record `generation_commit_hash` in every
`results/nNN/optimum.json`. The current data-generating commit recorded there is:

```text
fea000523a1ec4193d8ba9c4637563fd65e86d1a
```

Long-run evidence:

- n=13 progress log: `results/checkpoints/progress_n13_lb3.log`
- n=14 progress log: `results/checkpoints/progress_n14_lb3.log`
- n=14 detached stdout: `results/logs/sweep_14_14_20260610_221502.out.log`
- n=14 detached stderr: `results/logs/sweep_14_14_20260610_221502.err.log`

Checkpoint `.pkl` files under `results/checkpoints/` are intentionally ignored
because they are large and regenerated by `--resume`; the frontier JSON files
under `results/frontiers/` are the portable pruning certificates.

## Workflow And AI Assistance

The project was built in an AI-assisted workflow under the author's direction
and final review. AI assistance supported research design, mathematical
argument development, software implementation, tests, scripts, and repository
artifacts. All certified numerical claims are backed by the independent
`verify.py` verifier and the saved result artifacts.

## Layout

- `src/ringmin/`: solver library and CLI.
- `tests/`: pytest coverage for geometry, evaluator, search, patterns, and SLSQP
  cross-validation.
- `scripts/`: reproducibility and artifact-generation scripts.
- `verify.py`: standalone mpmath/stdlib-only certificate verifier.
- `results/`: certified optima, frontier certificates, calibration data, and logs.
- `figures/`: regenerated per-n figures.
- `paper_assets/`: paper source, PDF, figures, tables, and appendix snippets.

## License

MIT - see `LICENSE`.
