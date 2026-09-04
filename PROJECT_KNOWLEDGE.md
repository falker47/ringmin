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

## Proved post-arXiv-v1 results

### General fixed-radius Supnick seam persistence

**Status:** exact theorem, proved after arXiv v1.

Fix any integer `k>=1`. For `n>=k+2`, let `sigma*_{k,n}` be the
chain-minimizing Supnick order on `{k,...,n}`, let
`R_{k,n}=R_chain(sigma*_{k,n})`, and define

```text
Delta_{k,n}
  = theta_{R_{k,n}}(n,k) + theta_{R_{k,n}}(k,n-1)
    - theta_{R_{k,n}}(n,n-1).
```

The neighbors of `k` in this order are `n-1,n`. The root `R_{k,n}` exists
uniquely, strictly increases with `n`, and tends to infinity. The Descartes
comparison has no positive threshold for `k+2<=n<=4k`, where
`Delta_{k,n}>0`. Its exact positive domain is `n>=4k+1`, with

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))),
T_{k,n} = 1/kappa_{k,n}.
```

On that domain, `Delta_{k,n}<0` exactly when `R_{k,n}>T_{k,n}`. The roots
`R_{k,n}` strictly increase while `T_{k,n}` strictly decreases to `k`, so
`R_{k,n}-T_{k,n}` strictly increases to infinity. Consequently a strict
formal seam obstruction occurs eventually for every fixed `k`, persists
thereafter, and equality can occur for at most one integer. Equivalently,
the first strict-obstruction index `s_k` exists; all earlier deficits are
positive except for a possible equality at `s_k-1`.

This theorem by itself does not give a formula for `s_k`. Specialized exact
endpoint bridges recover `s_1=8`, `s_2=13`, `s_3=17`, `s_4=21`, `s_5=25`,
`s_6=30`, `s_7=34`, `s_8=38`, and `s_9=42`. The later effective theorem below proves
`s_k=4k+6` for every `k>=4325`; exact onsets for the unresolved finite range
`10<=k<4325` are not supplied by that tail theorem.
The fixed-`k` theorem concerns only the formal seam `(n,k,n-1)` and has no
implication for `R*(n)` or floating circles in global optima.

**Source:** `research/FIXED_K_SUPNICK_SEAM.md`; diagnostic algebra,
convention, and finite high-precision checks are recorded in
`ops/TASK-20260804__fixed_k_supnick_seam/`.

### Uniform exact window for the first seam obstruction

**Status:** exact theorem, proved after arXiv v1.

For every integer `k>=1`, the first strict-obstruction index of the formal
Supnick seam satisfies

```text
4k+1 <= s_k <= 4k+14.
```

The lower bound is exactly the no-threshold range from the general fixed-`k`
theorem. For the upper bound, at the single symbolic index `n=4k+14`, put

```text
N = 3k+15,
S_k = k(21k+83)/22.
```

The fixed-`k` chain lower bound, strict `sin(x)<x`, and the exact integral
witness `pi<22/7` give `R_{k,4k+14}>S_k`. An explicit positive gate before
squaring and a quadratic difference whose numerator and denominator have
positive coefficient certificates give
`kappa_{k,4k+14}>1/S_k>0`, hence `T_{k,4k+14}<S_k`. The fixed-`k` sign
criterion then gives `Delta_{k,4k+14}<0`.

No finite scan enters the proof. This theorem bounds but does not by itself
identify an onset; in particular it confines `s_8` to `33<=s_8<=46`. The
later effective theorem identifies the tail `k>=4325`, while the finite range
`10<=k<4325` remains unresolved after the radius-9 endpoint proof below.
The uniform theorem concerns only the formal seam `(n,k,n-1)` and has no
full-feasibility, global-optimum, contact-graph,
floating-circle, or global asymptotic consequence.

**Source:** `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md`; exact symbolic
stdlib/`Fraction` audit and task evidence are recorded in
`ops/TASK-20260830__uniform_seam_index_bound/`.

### Effective exact formula for the first seam obstruction

**Status:** exact theorem, proved after arXiv v1.

For every integer `k>=4325`, the first strict-obstruction index of the formal
fixed-radius Supnick seam is

```text
s_k = 4k+6.
```

For each `c in {5,6}`, the parity-explicit Supnick closure sums, including
both parity subsequences, satisfy

```text
R_{k,4k+c}/k^2 -> rho,
rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx.
```

Uniform estimates separately control the radius denominators and the
arcsine remainder. Exact rationalization of the Descartes threshold gives

```text
T_{k,4k+c}/k^2 -> 24/(2c-1).
```

An exact elementary certificate first proves the qualitative separation
`24/11<rho<8/3`. The effective bridge sharpens this to the rational
separators

```text
11/5 < 20/9 < rho < 41/16 < 13/5.
```

At `K=4325`, the recorded closure error proves
`R_{k,4k+5}<(13/5)k^2` and `R_{k,4k+6}>(11/5)k^2` throughout the tail. The
exact threshold error `4193/(256k)`, positivity of `k^2 kappa=H/Q`, and
rational reciprocal comparisons prove the opposite threshold brackets. The
critical cross margin is `256*4325-264*4193=248>0`. The fixed-`k` sign and
persistence theorem then gives the identity.

No finite scan is a premise, and `4325` is not claimed minimal. The theorem
does not classify any unresolved onset with `10<=k<4325`,
prove full feasibility, or imply anything about `R*(n)`, contact graphs, or
floating circles.

**Source:** `research/EVENTUAL_SUPNICK_SEAM_ONSET.md`; the qualitative and
effective stdlib/`Fraction` audits and task evidence are recorded in
`ops/TASK-20260830__eventual_supnick_seam_onset/` and
`ops/TASK-20260830__effective_supnick_seam_cutoff/`.

### Exact all-`n` radius-1 seam threshold

**Status:** exact theorem, proved after arXiv v1.

Let `sigma_n*` be the chain-minimizing Supnick order on `{1,...,n}` and `R_n=R_chain(sigma_n*)`. Then

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    > theta_{R_n}(n,n-1)       for 3 <= n <= 7,

theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)       for every n >= 8.
```

Thus the formal full Supnick necklace has an exact radius-1 seam obstruction from `n=8` onward. The proof makes the Supnick edge set parity-explicit, proves the chain roots `R_n` strictly increase, derives an explicit Descartes threshold

```text
T_n = 1 / (1 + 1/n + 1/(n-1) - 2 sqrt(2/(n-1))),
```

proves `T_n` strictly decreases on the relevant range, and closes the crossing with exact rational bounds at `n=7,8`.

This theorem concerns one formal chain and one seam. It does not determine `R*(n)`, prove that circle `1` floats in any or every global optimum, or prove another cascade level.

**Source:** `research/RADIUS1_SEAM_OBSTRUCTION.md`; diagnostic evidence and exact arithmetic checks are recorded in `ops/TASK-20260804__radius1_seam_obstruction/`.

### Exact all-`n` radius-2 seam threshold

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{2,n}` be the chain-optimal Supnick order on `{2,...,n}` and let
`R_{2,n}=R_chain(sigma*_{2,n})`. Then

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    > theta_{R_{2,n}}(n,n-1)       for 4 <= n <= 12,

theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)       for every n >= 13.
```

Thus the formal shifted Supnick necklace has an exact radius-2 seam
obstruction from `n=13` onward. The proof gives the shifted parity-explicit
edge and closure formulas, proves that `R_{2,n}` strictly increases, shows
that the positive radius-2 Descartes threshold exists exactly for `n>=9` and
strictly decreases, and closes the crossing with exact rational bounds at
`n=12,13`. The raw angular deficit is not monotone and is not used as a
comparison quantity.

This theorem concerns one formal chain and one seam. It does not determine
`R*(n)`, prove that circle `2` floats in any or every global optimum, or prove
the remaining radius-`k` cascade.

**Source:** `research/RADIUS2_SEAM_THRESHOLD.md`; diagnostic evidence and
exact arithmetic checks are recorded in
`ops/TASK-20260804__radius2_seam_threshold/`.

### Exact all-`n` radius-3 seam onset

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{3,n}` be the chain-optimal Supnick order on `{3,...,n}` and let
`R_{3,n}=R_chain(sigma*_{3,n})`. Then

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17.
```

Thus the exact first strict radius-3 seam obstruction is `s_3=17`. The proof
reuses the general fixed-`k` root/threshold monotonicity and persistence
theorem. It closes the finite bridge at the rational separator `R=32` with

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.
```

The threshold comparisons use rational square margins. The two chain
comparisons use rational termwise bounds on every arcsine argument and exact
elementary inequalities; high-precision roots are diagnostic only.

This theorem concerns one formal shifted Supnick seam. It does not determine
`R*(n)`, prove full realizability through `n=16`, or prove that circle `3`
floats in any or every global optimum.

**Source:** `research/RADIUS3_SEAM_ONSET.md`; exact checker gates and separate
finite diagnostics are recorded in
`ops/TASK-20260804__radius3_seam_onset/`.

### Exact all-`n` radius-4 seam onset

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{4,n}` be the chain-optimal Supnick order on `{4,...,n}` and let
`R_{4,n}=R_chain(sigma*_{4,n})`. Then

```text
theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    > theta_{R_{4,n}}(n,n-1)       for 6 <= n <= 20,

theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    < theta_{R_{4,n}}(n,n-1)       for every n >= 21.
```

Thus the exact first strict radius-4 formal seam obstruction is `s_4=21`.
The proof reuses the general fixed-`k` theorem without repeating it and closes
only the endpoint bridge at the rational separator `R=50`:

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.
```

The threshold comparisons use rational square margins. The chain comparisons
audit all `17` and `18` adjacent edges with rational termwise bounds and exact
elementary bounds for `pi`; finite high-precision roots remain diagnostic
only.

This theorem concerns one formal shifted Supnick seam. It does not prove full
feasibility through `n=20`, determine `R*(n)`, or prove that circle `4` floats
in any or every global optimum.

**Source:** `research/RADIUS4_SEAM_ONSET.md`; exact `Fraction` checker gates
and separate finite diagnostics are recorded in
`ops/TASK-20260804__radius4_seam_onset/`.

### Exact all-`n` radius-5 seam onset

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{5,n}` be the chain-optimal Supnick order on `{5,...,n}` and let
`R_{5,n}=R_chain(sigma*_{5,n})`. Then

```text
theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    > theta_{R_{5,n}}(n,n-1)       for 7 <= n <= 24,

theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    < theta_{R_{5,n}}(n,n-1)       for every n >= 25.
```

Thus the exact first strict radius-5 formal seam obstruction is `s_5=25`.
The proof reuses the general fixed-`k` theorem without repeating it and closes
only the endpoint bridge at the rational separator `R=75`:

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.
```

The threshold comparisons use explicit sign gates and rational square
margins. The chain comparisons audit all `20` and `21` adjacent edges with
rational termwise arcsine bounds and exact polynomial/integral comparisons
with `pi`; finite high-precision roots remain diagnostic only.

This theorem concerns one formal shifted Supnick seam. It does not prove full
feasibility through `n=24`, determine `R*(n)`, or prove that circle `5` floats
in any or every global optimum.

**Source:** `research/RADIUS5_SEAM_ONSET.md`; exact stdlib/`Fraction` checker
gates and separate finite diagnostics are recorded in
`ops/TASK-20260804__radius5_seam_onset/`.

### Exact all-`n` radius-6 seam onset

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{6,n}` be the chain-optimal Supnick order on `{6,...,n}` and let
`R_{6,n}=R_chain(sigma*_{6,n})`. Then

```text
theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    > theta_{R_{6,n}}(n,n-1)       for 8 <= n <= 29,

theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    < theta_{R_{6,n}}(n,n-1)       for every n >= 30.
```

Thus the exact first strict radius-6 formal seam obstruction is `s_6=30`.
The proof imports the general fixed-`k` theorem and closes only the endpoint
bridge at the rational separator `R=211/2`:

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30}.
```

The threshold comparisons use explicit sign gates and rational square
margins. The chain comparisons audit all `24` and `25` adjacent edges with
rational termwise arcsine bounds and exact rational comparisons with `pi`;
finite high-precision roots remain diagnostic only.

This theorem concerns one formal shifted Supnick seam. It does not prove full
feasibility through `n=29`, determine `R*(n)`, or prove that circle `6` floats
in any or every global optimum.

**Source:** `research/RADIUS6_SEAM_ONSET.md`; exact stdlib/`Fraction` checker
gates and separate finite diagnostics are recorded in
`ops/TASK-20260805__radius6_seam_onset/`.

### Exact all-`n` radius-7 seam onset

**Status:** exact theorem, proved after arXiv v1.

Let `sigma*_{7,n}` be the chain-optimal Supnick order on `{7,...,n}` and let
`R_{7,n}=R_chain(sigma*_{7,n})`. Then

```text
theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    > theta_{R_{7,n}}(n,n-1)       for 9 <= n <= 33,

theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    < theta_{R_{7,n}}(n,n-1)       for every n >= 34.
```

Thus the exact first strict radius-7 formal seam obstruction is `s_7=34`.
The proof imports the general fixed-`k` theorem and closes only the endpoint
bridge at the rational separator `R=140`:

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34}.
```

The threshold comparisons use explicit positive sign gates and rational
square margins. The chain comparisons audit all `27` and `28` adjacent edges
with strict rational termwise arcsine bounds and exact rational comparisons
with `pi`; finite high-precision roots remain diagnostic only.

This theorem concerns one formal shifted Supnick seam. It does not prove full
feasibility through `n=33`, determine `R*(n)`, classify a global contact
graph, or prove that circle `7` floats in any or every global optimum.

**Source:** `research/RADIUS7_SEAM_ONSET.md`; exact stdlib/`Fraction` checker
gates and separate finite diagnostics are recorded in
`ops/TASK-20260805__radius7_seam_onset/`.

### Exact all-`n` radius-8 seam onset

**Status:** exact theorem, proved after arXiv v1.

For the chain-minimizing Supnick cycle on `{8,...,n}`, put
`R_{8,n}=R_chain(sigma*_{8,n})`. Its formal seam deficit satisfies

```text
Delta_{8,n} > 0  for 10 <= n <= 37,
Delta_{8,n} < 0  for every n >= 38,
s_8 = 38.
```

The exact endpoint bridge is

```text
R_{8,37} < 176 < T_{8,37},
T_{8,38} < 176 < R_{8,38}.
```

The chain inequalities cover all 30/31 cyclic edges, use strict rational
arcsine bounds, and compare with `pi` through exact Machin identities and
signed finite remainders. The general fixed-`k` theorem supplies the
all-integer conclusion. The preceding numerical diagnostic is not a premise.
This result concerns one formal seam, not full feasibility, `R*(n)`, global
contact graphs, or floating circles in any or every global optimum.

**Source:** `research/RADIUS8_SEAM_ONSET.md`; independent stdlib/Fraction
checker, integer cross-checks and targeted rejection tests in
`ops/TASK-20260904__radius8_seam_onset/`.

### Exact all-`n` radius-9 seam onset

**Status:** exact theorem, proved after arXiv v1.

For the chain-minimizing Supnick cycle on `{9,...,n}`, put
`R_{9,n}=R_chain(sigma*_{9,n})`. Its formal seam deficit satisfies

```text
Delta_{9,n} > 0  for 11 <= n <= 41,
Delta_{9,n} < 0  for every n >= 42,
s_9 = 42.
```

The exact endpoint bridge is

```text
R_{9,41} < 220 < T_{9,41},
T_{9,42} < 220 < R_{9,42}.
```

All 33/34 cyclic edges are checked through separate rank-tour and parity
representations. Positive threshold/pre-square gates, directed rational
square margins, strict arcsine bounds and a signed-remainder proof of
`157/50<pi<22/7` close all four gates. The fixed-k theorem then supplies
the all-integer conclusion. No numerical scan or floating root is a premise.
This concerns one formal seam, without full-feasibility, global-optimum,
contact-graph or floating-circle consequences.

**Source:** `research/RADIUS9_SEAM_ONSET.md`; independent stdlib/Fraction
checker, integer cross-checks and targeted rejection tests in
`ops/TASK-20260904__radius9_seam_onset/`.

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

**Status:** mixed exact theorem and conjecture.

For every fixed integer radius `k>=1`, the general theorem above now proves
that the formal Supnick necklace on `{k,...,n}` eventually becomes
unrealizable across the seam `(n,k,n-1)` and remains obstructed thereafter.
The uniform theorem proves `4k+1<=s_k<=4k+14`, and the later effective
theorem proves `s_k=4k+6` for every `k>=4325`. Specialized endpoint notes
prove `s_1=8`, `s_2=13`, `s_3=17`, `s_4=21`, `s_5=25`, `s_6=30`,
`s_7=34`, `s_8=38`, and `s_9=42`; the finite range `10<=k<4325` remains unresolved.

The stronger claim that circle `k` eventually floats in global optima, with
recurring paid-then-free regimes, remains conjectural.

The paper reported seam-failure onsets `8,13,17` for circles `1,2,3` with
finite published scope. The post-v1 theorems above prove the exact all-`n`
onsets `s_1=8`, `s_2=13`, `s_3=17`, `s_4=21`, `s_5=25`, `s_6=30`,
`s_7=34`, `s_8=38`, and `s_9=42`, eventual persistent seam failure for every fixed radius, and
`s_k=4k+6` for every radius index `k>=4325`. Exact onset classifications in
the finite unresolved range `10<=k<4325` remain open. Every assertion about
eventual floating in global optima also remains conjectural.

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

1. Classify the unresolved finite range `10<=k<4325`, beginning with an
   exact endpoint-bridge attempt for radius 10 at n=45,46. The candidate
   `s_10=46` is unproved; all four rational gates must close before promotion.
   The proved cutoff `4325` is valid but not claimed minimal.
2. Prove or refute the parts of the floating-cascade conjecture that concern global optima rather than formal Supnick seams.
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
- The all-`n` radius-1 seam obstruction does not prove that radius `1` floats in any or every global optimum.
- The all-`n` radius-2 seam obstruction does not prove that radius `2` floats in any or every global optimum.
- The all-`n` radius-3 seam obstruction does not prove full realizability
  before `n=17` or that radius `3` floats in any or every global optimum.
- The all-`n` radius-4 seam obstruction does not prove full realizability
  before `n=21` or that radius `4` floats in any or every global optimum.
- The all-`n` radius-5 seam obstruction does not prove full realizability
  before `n=25` or that radius `5` floats in any or every global optimum.
- The all-`n` radius-6 seam obstruction does not prove full realizability
  before `n=30` or that radius `6` floats in any or every global optimum.
- The all-`n` radius-7 seam obstruction does not prove full realizability
  before `n=34`, classify a global contact graph, or imply that radius `7`
  floats in any or every global optimum.
- The all-`n` radius-8 seam obstruction does not prove full realizability
  before `n=38`, classify a global contact graph, or imply that radius `8`
  floats in any or every global optimum.
- The all-`n` radius-9 seam obstruction does not prove full realizability
  before `n=42`, classify a global contact graph, or imply that radius `9`
  floats in any or every global optimum.
- The general fixed-`k` seam theorem does not by itself identify `s_k` for
  `k>=10`, prove full realizability before `s_k`, or imply that radius `k`
  floats in any or every global optimum.
- The uniform bound `4k+1<=s_k<=4k+14` does not identify any new exact onset,
  prove full realizability below it, determine `R*(n)`, classify a contact
  graph, or imply that radius `k` floats in any or every global optimum.
- The effective identity `s_k=4k+6` for `k>=4325` does not claim a minimal
  cutoff, classify the unresolved finite range `10<=k<4325`, prove full
  realizability below the seam, determine `R*(n)`, classify a contact graph,
  or imply that radius `k` floats in any or every global optimum.
- One recovered contact graph does not establish uniqueness or a universal contact graph for all optima.
- Generated README/report/table agreement does not replace source and verifier agreement.
