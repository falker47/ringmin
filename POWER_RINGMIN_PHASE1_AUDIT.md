# Power-Ringmin Phase 1 Audit

Last updated: 2026-07-10

## Scope

This audit follows the immediate next step in `start.md`: isolate the current
Ringmin repository and audit which code and theorem components can support an
explicit radius sequence, initially for quadratic radii `r_k = k^2`.

No stable Ringmin certified result or saved output was modified.

## Isolation Baseline

- Source repository: `C:\Users\Falker\Desktop\Code\circle\ringmin`
- Source branch: `main`
- Source commit: `cc03274`
- Source commit date: `2026-06-26 11:05:41 +0200`
- Audit worktree: `C:\Users\Falker\Desktop\Code\ringmin-squared\ringmin-worktree`
- Audit branch: `power-ringmin-quadratic-audit`

Baseline checks in the audit worktree:

- `python -m pytest`: `12 passed`
- `python verify.py --start 3 --stop 8 --skip-frontier`: incumbent/local checks
  passed for `n=03..08`

The full frontier verifier was not run in this audit pass; it is slower and is
not needed to establish that the isolated checkout is functional.

## Reusable Code Inventory

### Radius-agnostic or nearly radius-agnostic

- `src/ringmin/geometry.py`
  - `theta(R, a, b)` already accepts arbitrary positive radii.
  - `as_order`, `cyclic_pairs`, and `cycle_equivalent` operate on radius values,
    not specifically on `1..n`.

- `src/ringmin/evaluator.py`
  - `chain_radius`, `build_stn_distances`, `is_feasible`, `recover_positions`,
    `full_radius_value`, and `full_radius` already accept explicit orders of
    positive radii.
  - Binding-pair and floating-circle detection are value-based and should work
    for quadratic radii.
  - The fixed high bracket `4.0 * len(radii) * len(radii)` is not scale-safe and
    will eventually fail for large quadratic cases or arbitrary scaled inputs.

- `src/ringmin/highprec.py`
  - The high-precision STN implementation accepts explicit radii.
  - It has the same fixed high-bracket issue as the float64 evaluator.

- `src/ringmin/patterns.py`
  - `interleave`, `supnick_max_tour`, `supnick_min_tour`, `sequential`, and
    `zigzag` sort arbitrary distinct values.
  - This matches the theorem statement when the values are sorted radii.

- `src/ringmin/search.py`
  - `canonical_orders_values(values)` and `certified_search_values(values)` are
    the main reusable hooks for explicit radius sets.
  - The implementation currently assumes values are integer radii and does not
    separate circle labels from geometric radii.

- `src/ringmin/artifacts.py`
  - Can serialize arbitrary radius values.
  - The output directory convention is still `results/nNN`, so problem metadata
    must be added before quadratic artifacts are generated.

- `src/ringmin/crosscheck.py`
  - `slsqp_fixed_order(order)` accepts explicit radii.
  - `slsqp_unconstrained_global(n)` is hard-coded to linear radii.

## Hard-coded Linear-Radius Assumptions

These are the main items to address before trusting quadratic outputs.

- Linear entry points:
  - `certified_search(n)`, `stage_a_candidates(n)`, `heuristic_search(n)`, and
    `random_canonical_order(n)` all construct `range(1, n + 1)`.
  - The CLI has `--n` and integer `--order`, but no `--radii quadratic`,
    `--values`, or label/radius input.

- Label/radius conflation:
  - Current orders are tuples of radius values.
  - For quadratic radii, using `(1, 4, 9, ...)` is geometrically correct, but it
    loses the natural labels `(1, 2, 3, ...)`.
  - Reporting floating "circle 4" would mean radius `4`, i.e. label `2`.
    Power-Ringmin should keep labels and radii separate.

- Stage-A lower bound:
  - `_lower_bounds_numpy` uses
    `max(chain(order), chain(order without 1), chain(order without 1,2))`.
  - For quadratic radii represented as radius values, this removes `{1}` and
    then `{1,2}`; the second component does not remove radius `4`.
  - This remains a valid but weaker bound because `chain(order)` is still a
    lower bound. It is not the intended `{smallest}` / `{two smallest}` bound.

- Fixed brackets:
  - `chain_radius`, `_chain_radii_numpy`, `full_radius_mp`, `verify.py`, and
    SLSQP bounds use `4*n^2`.
  - Quadratic asymptotics suggest `R ~ n^3/(6*pi)`, so the bracket should be
    adaptive before running beyond the small feasibility range.

- Certificate verifier:
  - `verify.py` assumes integer radii, linear artifact layout, and the same
    `{1}`, `{1,2}` pruning bound.
  - It should not be used as a quadratic certificate until generalized.

- Scripts and published assets:
  - Most scripts under `scripts/` read `results/nNN/optimum.json`, assume
    `1..n`, cast radii to `int`, and reproduce paper-specific linear claims.
  - These should remain Ringmin-linear scripts, or be copied/generalized into a
    quadratic namespace with separate output roots.

- Plot labels:
  - `plots.py` labels circles by integer radius. For quadratic work it should
    label by circle index `k` while using radius `k^2`.

## Theorem Audit

Local source checked:

- `paper_assets/ringmin_paper.tex`
- Section: `The optimal cyclic order is a fixed Supnick tour`
- Lemma: `Supermodularity` (`lem:supermodular`)
- Theorem: `Optimal order` (`thm:A`)

Exact local theorem content, paraphrased:

- For arbitrary positive distinct radii `r_1 < ... < r_n`, and every `R > 0`,
  the matrix `theta_R(r_i, r_j)` is symmetric strictly anti-Monge.
- Supnick's theorem gives a fixed tour
  `sigma* = <1, n-1, 3, n-3, 5, n-5, ..., n-2, 2, n>`
  minimizing the adjacent angular sum for every `R`.
- Therefore `sigma*` minimizes the chain radius over cyclic orders, giving an
  unconditional lower bound for the full geometric optimum.
- If the `sigma*` necklace at its chain radius has no non-adjacent violations,
  then it is the full global optimum.

Audit status:

- The local Ringmin paper explicitly states that Theorem A holds for arbitrary
  distinct positive radii, not only `1..n`.
- This covers quadratic radii for the chain lower-bound problem.
- It does not transfer any full-feasibility, floating-circle, finite
  certification, or asymptotic claim to the quadratic problem.
- The external Supnick citation itself was not independently rechecked in this
  offline audit pass.

## Quadratic Smoke Results

These are exploratory observations using the existing float64 search on explicit
radius values `(1^2, 2^2, ..., n^2)`. They are useful implementation smoke tests,
not Power-Ringmin certificates.

Target asymptotic constant:

```text
1/(6*pi) = 0.0530516476973
```

Exhaustive current-code search with `certified_search_values`:

| n | best order by radius values | R_full | R_full / n^3 | floating radii |
|---:|---|---:|---:|---|
| 3 | `(9, 1, 4)` | `0.383387036139` | `0.014199519857` | `()` |
| 4 | `(16, 1, 9, 4)` | `1.49562841187` | `0.023369193936` | `()` |
| 5 | `(25, 4, 16, 1, 9)` | `3.93432771714` | `0.031474621737` | `(1,)` |
| 6 | `(36, 4, 1, 25, 16, 9)` | `8.46793507607` | `0.039203403130` | `(1,)` |
| 7 | `(49, 1, 4, 25, 16, 36, 9)` | `15.0063752578` | `0.043750365183` | `(1,)` |
| 8 | `(64, 1, 16, 36, 25, 4, 49, 9)` | `24.8184549465` | `0.048473544817` | `(1, 4)` |

Additional observation:

- The Supnick chain order is not the full optimum from at least `n=5` in this
  smoke test. This is consistent with the project brief's warning that
  non-adjacent constraints and floaters must be handled separately from the
  chain lower bound.

## Recommended Next Implementation Steps

1. Add an explicit problem/radius-sequence layer.
   - Minimal option: `radii_for_n(n, sequence="linear"|"quadratic")`.
   - Better option: a small instance object carrying both `labels` and `radii`.

2. Preserve old linear APIs.
   - Keep `certified_search(n)` and current scripts as Ringmin-linear wrappers.
   - Add new APIs such as `certified_search_instance(...)` or
     `certified_search_values(..., labels=...)`.

3. Make all brackets adaptive.
   - Replace fixed `4*n^2` upper brackets with a loop that doubles until the
     chain sum is below `2*pi` or the STN is feasible.

4. Generalize Stage-A lower-bound components.
   - Replace hard-coded removals `{1}` and `{1,2}` with configurable induced
     subsets, initially `()`, `{smallest radius}`, `{two smallest radii}`.
   - Keep the linear default exactly reproducing the old behavior.

5. Separate artifact roots.
   - Use a quadratic-specific root such as `results_quadratic/` or include
     `problem_id = "quadratic"` in paths.
   - Add metadata: sequence name, labels, radii, code commit, method, precision,
     and certificate status.

6. Generalize the independent verifier before claiming certification.
   - It must read labels/radii from artifacts rather than reconstructing
     `1..n`.
   - It must use the same configured lower-bound components as the search.

7. Add regression tests before broad experiments.
   - Existing linear tests must still pass unchanged.
   - Add tests for scaling invariance.
   - Add a small quadratic smoke test using direct `full_radius`.
   - Add an exhaustive small quadratic test for `n <= 5` after the artifact and
     verifier formats are generalized.

## Phase-1 Exit Status

- Isolated worktree: complete.
- Existing Ringmin tests: pass.
- Local theorem statement and proof location: identified.
- Reusable module inventory: complete.
- Hard-coded linear assumptions: identified.
- Radius-sequence implementation: not yet changed.
- Quadratic certificates: not yet created.
