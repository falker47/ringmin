# PROJECT_KNOWLEDGE - Power-Ringmin

Last reviewed: 2026-07-10

This file contains stable, reusable project knowledge. It is not a backlog or
task diary.

## Purpose and Scope

- `VERIFIED FACT`: The authoritative project brief is `../start.md`; it defines
  Power-Ringmin as the quadratic-radii extension of Ringmin with peripheral
  radii `r_k = k^2`.
- `VERIFIED FACT`: The initial objective is a feasibility sprint, not an
  immediate full independent repository or paper.
- `VERIFIED FACT`: Exploratory numerical observations, certified computations,
  heuristics, conjectures and proofs must remain explicitly separated.
- `VERIFIED FACT`: The long-term target conjecture in the brief is
  `R_2^*(n) = n^3/(6*pi) * (1 + o(1))`.

## Definitions and Domain Rules

- `definition`: Peripheral circles are externally tangent to one central circle
  of radius `R`.
- `definition`: For quadratic radii, `r_i = i^2` for `i = 1,...,n`.
- `definition`: Pairwise non-overlap is required for every pair of peripheral
  circles, not only cyclic neighbors.
- `definition`: The angular separation formula is
  `theta_R(a,b) = 2*arcsin(sqrt(a*b/((R+a)*(R+b))))`.
- `definition`: For quadratic radii this is
  `theta_R(i^2,j^2) = 2*arcsin(ij/sqrt((R+i^2)*(R+j^2)))`.
- `definition`: An STN is a simple temporal network or equivalent system of
  difference constraints for angular-separation feasibility.
- `definition`: A certified optimum requires a reproducible certificate or
  rigorous numerical bound sufficient to exclude better configurations.
- `definition`: An exploratory optimum is a best found numerical configuration
  without a complete global certificate.

## Architecture / Structure

- `VERIFIED FACT`: Current Git root:
  `C:\Users\Falker\Desktop\Code\ringmin-squared\ringmin-worktree`.
- `VERIFIED FACT`: The worktree was created from the original Ringmin repository
  at `C:\Users\Falker\Desktop\Code\circle\ringmin`.
- `VERIFIED FACT`: Phase 1 audit branch: `power-ringmin-quadratic-audit`.
- `VERIFIED FACT`: Phase 1 source commit: `cc03274`.
- `VERIFIED FACT`: `src/ringmin/` contains the solver library and CLI.
- `VERIFIED FACT`: `tests/` contains pytest coverage for geometry, evaluator,
  search, patterns and SLSQP cross-validation.
- `VERIFIED FACT`: `scripts/` contains reproducibility and artifact-generation
  scripts.
- `VERIFIED FACT`: `verify.py` is a standalone mpmath/stdlib-only verifier for
  the original linear Ringmin certified artifacts.
- `VERIFIED FACT`: `results/` contains original Ringmin certified optima,
  frontier certificates, calibration data and logs.
- `VERIFIED FACT`: `paper_assets/` contains paper source, PDF, tables and
  appendix snippets for the original Ringmin project.

## Canonical Commands and Environments

- `VERIFIED FACT`: Project package metadata is in `pyproject.toml`; runtime
  dependencies are `numpy`, `scipy`, `mpmath` and `matplotlib`.
- `VERIFIED FACT`: `pyproject.toml` requires Python `>=3.11`.
- `VERIFIED FACT`: Canonical baseline commands for this project are:

```bash
python -m pytest
python verify.py --start 3 --stop 8 --skip-frontier
```

- `VERIFIED FACT`: The smoke verifier skips frontier/progress-log audit because
  `results/checkpoints/` is intentionally not tracked.

## Verified Results and Decisions

- `COMPUTATIONAL RESULT`: On 2026-07-10, Phase 1 baseline
  `python -m pytest` passed with `12 passed`.
- `COMPUTATIONAL RESULT`: On 2026-07-10, Phase 1 baseline
  `python verify.py --start 3 --stop 8 --skip-frontier` passed incumbent and
  local checks for `n=03..08`.
- `VERIFIED FACT`: Repository workflow uses manual human review and manual
  commits. Codex may inspect Git state and diffs, but must not stage, commit,
  push, merge, rebase, reset or rewrite history.
- `VERIFIED FACT`: `READY_FOR_REVIEW` means implementation and verification are
  complete; the user reviews the diff and decides whether to accept, modify or
  reject the work, then commits manually if accepted.
- `VERIFIED FACT`: `POWER_RINGMIN_PHASE1_AUDIT.md` records the completed Phase 1
  isolation and code/theorem audit.
- `VERIFIED FACT`: The local Ringmin paper states its optimal chain-order
  theorem for arbitrary distinct positive radii, which covers the chain lower
  bound for quadratic radii after citing that local theorem.
- `RISK`: That chain-order theorem does not by itself transfer full-feasibility,
  floating-circle, finite-certification or asymptotic claims to quadratic
  radii.
- `RISK`: The external Supnick citation itself was not independently rechecked
  in the Phase 1 offline audit.

## Reusable Code Inventory

- `VERIFIED FACT`: `src/ringmin/geometry.py` is radius-agnostic for positive
  radius values.
- `VERIFIED FACT`: `src/ringmin/evaluator.py` accepts explicit radius orders for
  chain and full fixed-order STN solves.
- `VERIFIED FACT`: `src/ringmin/highprec.py` accepts explicit radii for
  high-precision STN checks.
- `VERIFIED FACT`: `src/ringmin/patterns.py` sorts arbitrary distinct values for
  Supnick/interleave comparison orders.
- `VERIFIED FACT`: `src/ringmin/search.py` exposes `certified_search_values`,
  but the current implementation still conflates labels with radius values.

## Conventions

- Use separate artifact roots or metadata for quadratic outputs. Do not mix
  them silently into original Ringmin `results/`.
- Preserve old linear Ringmin behavior unless a task explicitly changes it and
  verifies non-regression.
- For quadratic radii, distinguish circle label `k` from radius value `k^2`.
- Treat `results/` and paper assets as original Ringmin artifacts unless a task
  explicitly says otherwise.

## Recurring Pitfalls

- Current search lower bounds remove hard-coded values `{1}` and `{1,2}`; for
  quadratic radii represented as values `(1,4,9,...)`, this does not mean
  removing the two smallest labels.
- Several brackets use `4*n^2`; quadratic scaling suggests adaptive brackets are
  needed before moderate or large quadratic experiments.
- `verify.py` assumes linear integer radii and current artifact layout; it is
  not yet a quadratic certificate verifier.
- Plot labels currently show integer radius values; quadratic work should label
  by circle index when appropriate.

## Open Global Questions

- `OPEN DECISION`: Final independent repository name.
- `OPEN DECISION`: Initial exhaustive-search limit for quadratic certification.
- `OPEN DECISION`: Initial moderate-`n` exploratory experiment limit after
  benchmarking.
- `OPEN DECISION`: Canonical certification arithmetic strategy for quadratic
  results.
- `OPEN DECISION`: Whether a shared core library is useful after both projects
  stabilize.
