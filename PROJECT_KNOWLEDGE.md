# Ringmin Project Knowledge

## Scope and provenance

This is the compact durable knowledge ledger for active work after the public Ringmin arXiv-v1 snapshot.

Bootstrap source snapshot:

```text
repository=falker47/ringmin
commit=9f67244b6226619df99a5eea2249f3fca8a32669
paper=arXiv:2607.28654
snapshot_date=2026-08-04
```

The commit records the post-arXiv-v1 repository update. This file summarizes existing claims; it does not independently re-certify them. Detailed published proofs remain in `paper_assets/ringmin_paper.tex`. Finite certificate claims require the optimum and frontier artifacts, their provenance, and `verify.py`. The full frontier audit also reads local progress logs that are intentionally ignored by Git; tracked files alone are not currently sufficient to reproduce that audit in a fresh clone.

## Core definitions

For surrounding radii `a,b > 0` and central radius `R > 0`, the minimum angular separation is

```text
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

For a cyclic order `sigma`:

- `R_chain(sigma)` is the unique radius at which the sum of consecutive `theta_R` values is `2*pi`.
- `R_full(sigma)` is the minimum radius for which all pairwise angular non-overlap constraints are feasible in that fixed cyclic order.
- `R*(n) = min_sigma R_full(sigma)` is the global optimum for radii `1,2,...,n`.

Stable relations:

```text
R_chain(sigma) <= R_full(sigma)
min_sigma R_chain(sigma) <= R*(n) = min_sigma R_full(sigma)
R_chain(sigma*) <= R*(n)
```

Here `sigma*` denotes the chain-optimal Supnick order. These inequalities do not imply that `sigma*` is fully realizable.

## Proved mathematical results in arXiv v1

### Exact angular reformulation

**Status:** exact theorem.

Pairwise non-overlap for circles tangent to the central circle is equivalent to the angular-separation inequality defined above. The angle is symmetric, lies in `(0,pi)`, decreases strictly with `R`, and increases with each surrounding radius.

**Source:** `paper_assets/ringmin_paper.tex`, model section.

### Anti-Monge/Supnick chain order

**Status:** exact theorem, using Supnick’s classical TSP result.

For each fixed `R`, the angular-cost matrix ordered by increasing radii is strictly anti-Monge. The chain-ordering problem therefore has a fixed Supnick tour independent of `R`. A self-consistency argument transfers this fixed-`R` order to the variable-radius chain problem.

Consequences:

- the conjectured pyramid/Supnick order minimizes `R_chain`;
- its chain radius is an unconditional lower bound for the full global problem;
- equality with the geometric optimum requires all pairwise constraints to be realizable.

**Source:** `paper_assets/ringmin_paper.tex`, Supnick theorem section.

### Worst chain arrangement

**Status:** proved at chain level in arXiv v1; finite geometric realizability statements must retain their stated finite scope.

**Source:** `paper_assets/ringmin_paper.tex` and generated appendix tables.

## Computer-certified finite results

**Status:** computer-certified finite results reported by the paper and artifact chain, and independently reproduced by the full verifier in this bootstrap checkout; not all-`n` theorems.

The repository reports global optima for every `n` in `3 <= n <= 14`, with claimed global absolute tolerance `1e-10` in `R`, local bracket scale `eta=1e-12`, and high-precision reconstruction/checking at 50 decimal digits.

Reported finite regimes:

- `3 <= n <= 7`: full Supnick necklace is realizable; no floating circle.
- `n = 8,9`: circle `1` floats, and the reduced necklace must be distorted to open a sufficient pocket.
- `n = 10,11,12`: circle `1` fits freely in a pocket of the Supnick necklace on `{2,...,n}`.
- `n = 13`: circle `1` floats, while the reduced Supnick necklace encounters a second seam obstruction involving circle `2`.
- `n = 14`: circles `1` and `2` float in a reported certified optimum.

Evidence chain:

- `results/nNN/optimum.json` and companion text artifacts;
- tracked `results/frontiers/nNN_frontier.json` artifacts and their coverage metadata;
- locally present, Git-ignored `results/checkpoints/progress_nNN_lb3.log` files referenced by those frontier artifacts;
- standalone `verify.py`, which does not import `src/ringmin`;
- source and generation metadata embedded in artifacts, including generation commit `fea000523a1ec4193d8ba9c4637563fd65e86d1a`;
- public paper tables and appendix.

A `certified` field is not sufficient by itself. The full verifier mode must include frontier verification. The bootstrap did not regenerate any artifact or prove that the current source tree is identical to the recorded generation commit.

## Current implementation facts

**Status:** engineering facts at the bootstrap snapshot.

- `src/ringmin/evaluator.py` separates the adjacent-chain relaxation from fixed-order all-pairs STN feasibility.
- `src/ringmin/search.py` implements canonical cyclic enumeration, vectorized lower bounds, Stage-B full evaluation, checkpoints, and an exhaustive fallback when the retained candidate frontier is insufficient.
- The production lower bound version is `lb3`, using the maximum of the full-order chain radius and selected induced-order chain radii after removing `{1}` and `{1,2}` where defined.
- `verify.py` reimplements the relevant geometry, STN, local bracket, artifact, canonical-count, frontier, guard, and progress-log checks using the standard library and `mpmath`, without importing `src/ringmin`.
- The test suite contains property checks and SciPy SLSQP cross-checks, but it is not a replacement for the independent verifier.
- Hosted CI runs the unit suite and `verify.py --start 3 --stop 8 --skip-frontier`; this is a smoke gate, not full `3..14` global-certificate verification.

### Full-verifier portability limitation

**Status:** engineering and certification-reproducibility limitation at the bootstrap snapshot.

The tracked frontier JSON files refer to `results\checkpoints\progress_nNN_lb3.log`, while `results/checkpoints/` is Git-ignored. Those logs were present in this Windows checkout and the full local `3..14` verifier passed. A fresh clone cannot reproduce the current full-verifier run without restoring or regenerating the logs; the stored backslash paths also require portable handling before a POSIX full-frontier run can be claimed. Hosted CI avoids this dependency by using `--skip-frontier`. This limitation does not turn the smoke verifier into a global certificate and was not repaired in the documentation-only bootstrap task.

## Heuristic and conjectural results

### Larger-`n` arrangements

**Status:** heuristic upper bounds and empirical structure.

The paper reports non-exhaustive local-search candidates for `15 <= n <= 18`. Their feasibility makes each radius an upper bound on `R*(n)` if independently checked, but no global optimality follows.

Reported patterns include:

- circles `{1,2}` floating in best-known candidates for `n=15,16,17`;
- circles `{1,2,3}` floating in the best-known candidate for `n=18`;
- repeated paid/free and seam-failure behavior resembling the finite regimes.

### Floating cascade

**Status:** conjecture.

For each fixed small radius `k`, the reduced Supnick necklace is conjectured eventually to become unrealizable and circle `k` is conjectured eventually to float, with recurring paid-then-free regimes.

Observed seam-failure onsets in the paper are `8,13,17` for circles `1,2,3`; only the explicitly stated finite cases retain their published proof/certification status.

### Asymptotics

**Status:** conjecture.

The public paper conjectures

```text
R*(n) = n^2/8 * (1 + o(1))
```

and tentatively the stronger deficit bound

```text
n^2/8 - R*(n) = O(sqrt(n)).
```

The paper states that rigorous two-sided leading-order bounds appear approachable but were not proved there.

## Primary open problems

1. Prove analytically, for all relevant `n`, the seam-obstruction inequalities underlying the first finite regime transitions; the missing step is monotonic control in `n`.
2. Generalize the obstruction to radius `k` and prove or refute the floating-cascade conjecture.
3. Characterize the floating set `F(n)` asymptotically.
4. Prove unconditional two-sided bounds establishing or refuting the leading term `n^2/8`.
5. Extend the structural analysis from radii `k` to `k^alpha` or general sequences without silently importing conclusions.

The sole ranked priority is maintained in `research/NEXT_RESEARCH_STEPS.md`.

## Non-implications to preserve

- Chain optimum is not automatically geometric optimum.
- Fixed-order feasibility is not global optimality.
- Local `R* +/- eta` behavior is not a global certificate.
- `--skip-frontier` does not verify global pruning.
- A best-known heuristic is not certified.
- Certified cases through `n=14` do not prove the cascade or asymptotics.
- One recovered contact graph does not establish uniqueness or a universal contact graph for all optima.
- Generated README/report/table agreement does not replace source and verifier agreement.
