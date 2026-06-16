# Endorsement Summary

## Problem Statement

The project studies a discrete-geometric optimization problem: circles of radii `1,2,...,n` are required to be externally tangent to one central circle, and the goal is to arrange the surrounding circles so that the central radius is as small as possible. The difficulty is that the cyclic order suggested by pairwise chain tangencies can become geometrically unrealizable once non-adjacent circle constraints are enforced.

## Main Proved Mathematical Result

The paper proves that the chain-ordering component is governed by a fixed Supnick/anti-Monge TSP. For every central radius `R`, the angular-separation matrix is symmetric anti-Monge, so Supnick's theorem gives a fixed cyclic order minimizing the chain-angle sum. This yields an unconditional lower bound for the true optimum and proves the conjectured pyramid arrangement whenever that chain necklace is geometrically realizable.

## Certified Computational Results

The repository contains certified global optima for `3 <= n <= 14`. Each certified result has saved optimum artifacts under `results/nNN/`, frontier certificates under `results/frontiers/`, and independent high-precision verification through `verify.py`. The verifier is intentionally separate from `src/ringmin` and checks incumbent feasibility, local optimality around the stated radius, and the pruning frontier.

## Heuristic And Conjectural Parts

For `n > 14`, the repository reports heuristic/local-search evidence only. The paper states the continuation of the floating-circle cascade and the asymptotic form `R*(n) = n^2/8 (1+o(1))` as conjectural, with finite supporting computations separated from the certified global optima.

## Proposed arXiv Categories

### `math.MG`

Pros: closest to the geometric statement of the problem, circle tangency constraints, Descartes pockets, and metric geometry flavor.

Cons: the main proof tool is an ordering theorem from Supnick/Monge TSP theory, so some endorsers may view the core as more combinatorial optimization than metric geometry.

### `math.CO`

Pros: strong fit for the Supnick TSP, anti-Monge structure, cyclic ordering, exhaustive finite certificates, and branch-and-bound enumeration.

Cons: the motivating problem and feasibility oracle are geometric; a purely combinatorics reader may care less about the circle-packing interpretation.

### `cs.CG`

Pros: reasonable secondary fit for computational geometry, certified geometric feasibility, and reproducible search artifacts.

Cons: the paper is written as a mathematics paper and relies on a classical TSP theorem rather than a new computational-geometry algorithmic framework.

## Minimal Reproduction Commands

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
python -m pytest
python verify.py --start 3 --stop 8
```

If LaTeX is available:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

## Full Reproduction Commands

Full certification is a long-running workflow, not a smoke test.

```bash
python scripts/sweep_certified.py --start 3 --stop 13 --k 20000 --workers 8 --resume
powershell -ExecutionPolicy Bypass -File scripts/start_detached_sweep.ps1 -Start 14 -Stop 14 -K 50000 -Workers 8 -Resume
python verify.py --start 3 --stop 14
python scripts/highprec_verify.py --start 3 --stop 14 --digits 50
python scripts/extract_frontiers.py --start 3 --stop 14 --margin 2e-10
python scripts/calibrate_float64.py --start 8 --stop 14 --samples 100000 --workers 8 --batch-size 500
python scripts/refresh_heuristic_artifacts.py
python scripts/free_float_criterion.py
python scripts/patterns_table.py
python scripts/supnick_validity.py
python scripts/asymptotic_fit.py
python scripts/generate_figures.py
python scripts/build_report.py
python scripts/export_paper_assets.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper_assets paper_assets/ringmin_paper.tex
```

## What An Endorser Is Being Asked To Evaluate

An endorser is being asked to assess whether the paper appears appropriate for arXiv submission in the proposed category, whether the claims are framed responsibly, and whether the repository provides enough context for later readers to reproduce the finite computations.

An endorser is not being asked for peer review, a guarantee of correctness, a full audit of the long-running enumeration, or an endorsement of the conjectures beyond their stated evidentiary status.
