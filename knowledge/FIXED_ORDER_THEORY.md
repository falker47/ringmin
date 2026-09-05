# Fixed-Order Theory

This thematic ledger owns stable results about chain optimization, formal
Supnick seams, and full feasibility for a fixed cyclic order. It does not own
global-optimum, certification, or global-asymptotic claims; it does own the
fixed-order asymptotic statements used by its seam results. Linked proof notes
remain authoritative for mathematical detail.

## Published chain theory

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

## Post-arXiv-v1 seam and feasibility theory

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
`s_6=30`, `s_7=34`, `s_8=38`, `s_9=42`, and `s_10=46`. The later effective theorem below proves
`s_k=4k+6` for every `k>=4325`. The later sequence theorem below proves
the same identity for every `k>=6`, completing all formal seam onsets.
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
later effective theorem identifies the tail `k>=4325`; the sequence theorem
below subsequently completes the formula for every `k>=6`.
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

No finite scan is a premise, and `4325` is not claimed minimal. This earlier
tail theorem alone does not classify smaller indices; the sequence theorem
below supplies that completion. The onset identities do not determine
`R*(n)`, contact graphs, or floating circles. The chain-root asymptotic,
combined with deletion in the induced-subset theorem below, now supplies
an unconditional global asymptotic lower bound.

**Source:** `research/EVENTUAL_SUPNICK_SEAM_ONSET.md`; the qualitative and
effective stdlib/`Fraction` audits and task evidence are recorded in
`ops/TASK-20260830__eventual_supnick_seam_onset/` and
`ops/TASK-20260830__effective_supnick_seam_cutoff/`.

### Exact sequence monotonicity and complete formal seam onsets

**Status:** exact theorem / proved corollary, after arXiv v1.

For `D_c(k)=R_{k,4k+c}-T_{k,4k+c}`,

```text
D_5(k+1)<D_5(k),    D_6(k+1)>D_6(k)    for every integer k>=6.
```

The proof retains the even central-edge correction when consecutive k
changes closure parity. Strict closure comparisons and exact midpoint
bounds place `D_c(k)-V_c(k)` in a common interval of width less than `8/3`.
Exact derivative bounds give `V_5'<-8/3` and `V_6'>8/3` on real `k>=6`.
Ten coefficient-positive polynomial gates certify the rationalized
threshold derivative bounds; no finite scan or effective asymptotic bound
is a premise.

Only after both monotonicities are proved, the existing k=6 endpoint bridge
gives `D_5(k)<0<D_6(k)`. Fixed-k persistence then proves

```text
s_k=4k+6 for every integer k>=6,
Delta_{k,n}>0 for k+2<=n<=4k+5,
Delta_{k,n}<0 for every n>=4k+6.
```

There is no equality case. Together with `s_1=8`, `s_2=13`, `s_3=17`,
`s_4=21`, `s_5=25`, every positive integer formal seam index is classified.
The sequence theorem alone does not establish full feasibility below onset;
the following equivalence supplies that separate fixed-order conclusion.
Neither result establishes global optimality or floating behavior.

**Source:** `research/SUPNICK_SEAM_SEQUENCES.md`; independent stdlib/Fraction
gates, separate symbolic differentiation/coefficient checks, and the
rerun of the radius-6 bridge are recorded in
`ops/TASK-20260904__seam_sequence_monotonicity/`.

### Complete exact Supnick fixed-order feasibility classification

**Status:** exact theorem / proved fixed-order corollary, after arXiv v1.

For every integer `k>=1,n>=k+2`, the cumulative-angle Supnick placement
at `R_{k,n}` is fully feasible if and only if `Delta_{k,n}>=0`. Equivalently,
some placement in that fixed order exists at that radius if and only if
that inequality holds. Closure forces every adjacent gap tight, including
the closing gap, so a negative seam cannot be repaired at the chain root.

At every `R>0`, each triangle defect on distinct members of `{k,...,n}`
is at least `delta_R`, with equality only at middle radius `k` and endpoints
`n-1,n`. Fan telescoping gives `S_R(P)>=(m-1)delta_R` for every simple
m-edge path. Both cyclic directions, adjacent complements, N=3, N=4 and
Delta=0 are treated explicitly. These lemmas and the equivalence do not
import any seam-sign theorem or rely on finite numerical checks.

Only then, the known strict seam signs give the complete classification:

| k | Fully feasible at the chain root | Infeasible at the chain root in this fixed order |
|---|---|---|
| 1 | 3<=n<=7 | n>=8 |
| 2 | 4<=n<=12 | n>=13 |
| 3 | 5<=n<=16 | n>=17 |
| 4 | 6<=n<=20 | n>=21 |
| 5 | 7<=n<=24 | n>=25 |
| k>=6 | k+2<=n<=4k+5 | n>=4k+6 |

There is no integer equality case. In every feasible case,
`R_full(sigma)=R_chain(sigma)`. For N>=4 the minimum nonadjacent directed
path slack is exactly Delta>0, attained only by the seam up to reversal;
adjacent one-edge paths have zero slack. The earlier boundary family
n=4k+5,k>=6 is included. No global-optimum or floating conclusion is drawn.

**Source:** `research/SUPNICK_FULL_FEASIBILITY.md`; independent symbolic
identities, exact small-cycle checks and a separate finite falsification
check in `ops/TASK-20260904__supnick_feasibility_classification/`.
The earlier boundary-family dossier remains historical evidence.

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

### Exact all-`n` radius-10 seam onset

**Status:** exact theorem, proved after arXiv v1.

For the chain-minimizing Supnick cycle on `{10,...,n}`, put
`R_{10,n}=R_chain(sigma*_{10,n})`. Its formal seam deficit satisfies

```text
Delta_{10,n} > 0  for 12 <= n <= 45,
Delta_{10,n} < 0  for every n >= 46,
s_10 = 46.
```

The exact endpoint bridge is

```text
R_{10,45} < 270 < T_{10,45},
T_{10,46} < 270 < R_{10,46}.
```

Both complete cycle constructions agree on all 36/37 edges, including
closure and multiplicity. Positive pre-square gates and exact directed
threshold margins, strict rational witnesses on every edge, and analytic
arcsine/pi bounds close all four gates. The fixed-k theorem alone supplies
the all-integer deduction. No scan, floating root or reviewer suggestion
is a premise. This result concerns one formal seam and makes no full
feasibility, global-optimum, contact-graph or floating-circle claim.

**Source:** `research/RADIUS10_SEAM_ONSET.md`; stdlib/Fraction checker,
separate integer witness scorer and targeted rejection tests in
`ops/TASK-20260904__radius10_seam_onset/`.

### Alternating-halves exact full feasibility and asymptotics

**Status:** exact finite fixed-order characterization / exact asymptotic
theorem / explicit feasible construction, after arXiv v1.

For `n=2m` and

```text
sigma_{2m}=(1,m+1,2,m+2,...,m,2m),
```

write `L_i=i`, `H_i=m+i`, and, cyclically,

```text
A_i=theta_R(L_i,H_i),
B_i=theta_R(H_i,L_{i+1}),
C_i=theta_R(H_{i-1},H_i),
S_m(R)=sum_i max(A_i+B_{i-1},C_i).
```

The exact full radius for this fixed order is the unique root
`S_m(R)=2*pi`. Necessity sums the disjoint two-edge valley constraints.
For sufficiency, the explicit gaps

```text
g(L_i,H_i)=A_i+[C_i-A_i-B_{i-1}]_+,
g(H_i,L_{i+1})=B_i
```

have total `S_m(R)`; any unused closure angle may be added to one gap. A
thick-shell triangle lemma for `m+1<=H_i<=2m<2(m+1)` proves both cyclic
paths for all high-high pairs, including the seam, and monotonicity then
lifts the result to every low-high and low-low pair. Thus no longer pairwise
constraint strengthens the cellwise obstruction.

With

```text
J=3sqrt(2)/4-log(3+2sqrt(2))/8,
K=J-1/12+log(3)/8,
```

uniform angular scaling and the analytic valley switch at `i/(2m)=1/6`
give

```text
R_chain(sigma_{2m})/(2m)^2 -> J/(2*pi),
R_full(sigma_{2m})/(2m)^2 -> K/(2*pi)
  =0.14233385361931275491...<1/(2*pi).
```

Below the switch, consecutive-high chords control; above it, the two chain
adjacencies control. The seam chord is treated exactly but has only `O(1/n)`
closure mass. The decimal is diagnostic only. This fixed-order theorem does
not assert global optimality or optimize any broader order family. The global
all-integer limsup consequence is owned by
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`.

**Source:** `research/ALTERNATING_HALVES_FULL_ASYMPTOTICS.md`; independent
70-digit root and direct all-pairs gap diagnostics in
`ops/TASK-20260904__alternating_halves_full_asymptotics/`.

### Shifted alternating-halves: exact feasibility and unique optimal shift

**Status:** exact finite fixed-order theorem / exact asymptotic and
family-minimization theorem, after arXiv v1.

For every m>=2 and 0<=s<m, set P_i=m+1+((i+s-1) mod m) and consider
sigma_{m,s}=(1,P_1,...,m,P_m). With these shifted highs, the cellwise
formula in the preceding entry remains exact: full feasibility at fixed R
is equivalent to the sum of max(two-adjacency sum, high-high chord) being
at most 2*pi. A fresh thick-shell triangle proof treats every high path,
then every low-high and low-low path in both directions, including m=2,
the low seam and the separately moving high wrap.

For h_alpha(t)=1+{t+alpha}, with h_1=h_0, define

```text
J(alpha)=integral_0^1 sqrt(t h_alpha(t)) dt,
K(alpha)=integral_0^1 max(sqrt(t h_alpha(t)),h_alpha(t)/2) dt.
```

For every integer shift sequence s_m/m->alpha in [0,1],

```text
R_chain(sigma_{m,s_m})/(2m)^2 -> J(alpha)/(2*pi),
R_full(sigma_{m,s_m})/(2m)^2 -> K(alpha)/(2*pi),
J(alpha)<K(alpha).
```

The piecewise elementary K has a unique minimum alpha_* in (0,1/2),
defined by equation (11) in the proof note. Strict convexity on [0,1/2],
the exact negative derivative at zero, and separate concavity/monotonicity
arguments on the other two branches prove K(alpha_*)<K(0) without numerical
premises. The moving-wrap derivative term is retained. Diagnostic values are
alpha_*=0.106784760199900199... and K(alpha_*)/(2*pi)=0.141995978127714285....
This also gives the asymptotic minimum over all finite shifts in this family;
it does not optimize all cyclic orders. The global deletion corollary is
owned by `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`.

**Source:** `research/SHIFTED_ALTERNATING_HALVES.md`; exact rational/symbolic
checks, independent direct angular/Cartesian audits and all-pairs LP checks
in `ops/TASK-20260905__shifted_alternating_halves/`.

### Arbitrary high permutations: exact fixed-order cell characterization

**Status:** exact fixed-order theorem / proved immediate fixed-order
corollaries, after arXiv v1.

For every integer m>=2, every permutation P of {m+1,...,2m}, and every
R>0, full feasibility of sigma_P=(1,P_1,2,P_2,...,m,P_m) is equivalent to

```text
S_P(R)=sum_i max(theta_R(P_{i-1},i)+theta_R(i,P_i),
                theta_R(P_{i-1},P_i)) <= 2*pi,
P_0=P_m.
```

The entire feasible gap set is given by adjacency lower bounds, the
high-high bound across each low cell, and total length 2*pi. The proof
contracts high paths using a triangle inequality valid in any order in
the shell [m+1,2m], then checks both directions for every low-high and
low-low pair. It explicitly includes all six pairs at m=2, m=3, the low
seam and arbitrarily many interior high descents/jumps. No shift or
monotonicity assumption on P is used.

R_full(sigma_P) is the unique positive root of S_P=2*pi. At that root,
write a_i=theta_R(P_{i-1},i), b_i=theta_R(i,P_i), and
d_i=max(a_i+b_i,theta_R(P_{i-1},P_i)). Every feasible gap vector, up to
overall rotation, is exactly x_i in [a_i,d_i-b_i], y_i=d_i-x_i, where
x_i is the gap P_{i-1}->i and y_i the gap i->P_i.
Chain/full equality holds iff every high chord is at most its two
adjacent requirements at the chain root.

This generalizes only the fixed-R portion of the preceding shift theorem.
It does not optimize over permutations, extend its asymptotic functional,
change global bounds/certified scope, or classify global contacts/floaters.

**Source:** `research/PERMUTED_ALTERNATING_HALVES.md`; pre-proof independent
all-permutation LP falsification and post-proof algebra, topology and
high-precision angular/Cartesian checks in
`ops/TASK-20260905__permuted_alternating_halves/`.

### Adjacent high swaps: exact variation and conditional exchange

**Status:** exact local identities / conditional exchange theorem / proved
small-R structural corollary / disproved universal sign rules, after arXiv v1.

For the preceding permuted-halves criterion, an adjacent high swap at
positions j,j+1 changes exactly cells j and [j+2]_m for m>=3; the middle
cell is symmetric and invariant. At m=2 every cell is invariant. Writing
F_t(a,b)=max(theta_R(t,a)+theta_R(t,b),theta_R(a,b)), the variation is
F_j(u,y)-F_j(u,x)+F_{[j+2]_m}(x,v)-F_{[j+2]_m}(y,v), where
(u,x,y,v)=(P_{j-1},P_j,P_{j+1},P_{j+2}) cyclically.

The moving-high branch has an explicit single threshold, including its
infinite case, endpoint equality and rejection of the extraneous squared
root. The proof gives a closed two-part angular increment and conditional
exchange rules from the ordering of the two clipped thresholds and the
external lows/highs. These yield necessary local optimality conditions;
radius comparisons require applying them at the relevant full-radius root.

For 0<R<=1 and m>=3, every fixed-R minimizer has P_1=2m,
P_{m-1}=m+1, P_m in {m+2,...,2m-1}, and all other highs in descending
order. Only m-2 candidates remain; this does not say they all minimize.
No increasing cyclic shift minimizes in this subdomain for m>=4.

The minimal sign reversal is at m=3: (4,5,6)->(5,4,6) has negative
variation at R=1 and positive variation at R=100, with exact rational
enclosures. The cell cost retains weak increasing differences in its two
highs, but has neither uniform Monge nor uniform anti-Monge sign between
a low label and a moving high. Thus the original kernel's anti-Monge
property does not justify ignoring the max branches or assuming shifts
optimal. No general permutation/root optimization, new asymptotics,
global certificate or contact/floater claim follows.

**Source:** `research/PERMUTED_HALVES_ADJACENT_SWAP.md`; pre-proof bounded
falsification, exact symbolic/rational checks and independent high-precision
local-versus-full comparisons in `ops/TASK-20260905__adjacent_high_swap/`.

### Root-level cyclic-shift optimality: minimal finite counterexample

**Status:** disproved claim / computer-certified finite result, after arXiv v1.

For the preceding permuted-halves full-radius objective rho_P, the claim
that an increasing cyclic high shift always minimizes over all high
permutations is false. The least counterexample size is m=4: the unique
minimizer among all 24 labeled permutations is A=(8,7,5,6), while the
unique best shift is B=(7,8,5,6). Exact rational enclosures prove

```text
rho_A < 577/100 < rho_B,
0.0157658012 < rho_B-rho_A < 0.0157658014.
```

At m=2 every permutation is a shift and both score functions coincide;
at m=3 a separate rational separator proves (6,4,5) uniquely minimizes
among all six. The local swap B->A has mixed/chain increments and a
rigorously negative variation at rho_B; a generic fixed-R improvement
was not substituted for a root comparison.

The predeclared m=2..8 exhaustive experiment stopped after m=4, with
32 orders evaluated by independent 80/110-digit scorers; m=5..8 were
not run. The finite root minimizers and strict separation use exact
rational certificates, while longer root decimals are numerical evidence.
This neither determines R*(8) nor extends to an all-m structure or
general permutation asymptotics. Global bounds/certificates are unchanged.

**Source:** `research/PERMUTED_HALVES_ROOT_SEARCH.md`; complete finite
root data, independent scorer and exact separator checks in
`ops/TASK-20260905__permuted_halves_root_search/`.

### Uniform local stability of the permuted-halves full radius

**Status:** exact fixed-order theorem / proved asymptotic corollaries,
after arXiv v1.

For all m>=3, a path of adjacent high-position swaps P->Q with exchanged
values x_h,y_h and D=sum_h |x_h-y_h| satisfies

```text
|rho_P-rho_Q| <= C_m D <= 2D,
L_m=max(1,(m+1)(csc(pi/m)-1)),
C_m=sqrt(2)/(2*pi)*(1+2m/L_m)=sqrt(2)/(2*pi)+O(1/m).
```

Here rho is the exact full-radius root of S=2*pi. Cyclic wrap swaps are
included; all m=2 roots coincide. Thus at most K swaps give
|rho_P-rho_Q|<=2K(m-1)=O_K(m)=o(m^2), uniformly for each fixed K.
Numerically consecutive exchanged values give O_K(1). The proof bounds
the two opposite cell increments and transfers their difference through
a radial contraction valid across max-branch ties. A constructed
one-swap family has radius drop >m/(12288*pi) for all m>=32, so the
unrestricted O(m) scale cannot be improved to o(m).

For m>=32 and any increasing shift 1<=s<=m-3, its first-two-high swap
strictly decreases rho by at most
3*(1+8*pi/m)/(4*pi*(m+1))=O(1/m). Both exterior cells are then chords;
the proof uses their positive angular mixed derivative. Choosing any
best finite shift at each m gives a precise continuation of the m=4
counterexample. Its shift ratio tends to alpha_*, so this sharper bound
holds eventually, and its leading coefficient remains C_shift. The
mixed/chain finite m=4 sign is imported from the preceding certificate,
not from the eventual chord argument.

The union of the distance-K neighborhoods of every shift has the same
minimum asymptotic coefficient C_shift for K fixed, or even K=o(m).
A strictly better coefficient requires distance at least of order m
from the shift family; that necessary condition is not a construction.
No global upper coefficient, finite certified scope, arbitrary-permutation
optimum or contact/floater classification changes.

**Source:** `research/PERMUTED_HALVES_LOCAL_STABILITY.md`; symbolic
derivatives, rational gates, targeted reused m=4 bracket checks and
bounded independent atan diagnostics (no enumeration) are recorded in
`ops/TASK-20260905__permuted_halves_local_stability/`.

### Three-marginal continuum relaxation: strict gap below the shifts

**Status:** exact continuum theorem / explicit coupling / disproved
relaxation-certificate claim, after arXiv v1.

For any sequence of high permutations, put
mu_m=(1/m) sum_i delta_(i/m,P_{i-1}/m,P_i/m) and
g(t,x,y)=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)). At R=c*(2m)^2,
the exact full-cell score satisfies

```text
S_P(R)=(integral g dmu_m)/(2*c)+O(1/m),
rho_P/(2m)^2=(integral g dmu_m)/(4*pi)+O(1/m),
```

uniformly over P (and compact positive c intervals for the score).
Every weak empirical limit has uniform marginals t in [0,1], x,y in
[1,2], and equal (t,x)/(t,y) marginals. Independence, conditional
uniformity and exclusion of diagonal support are not necessary conditions.

Let L_3 minimize integral g with the three uniform marginals. Adding
the necessary (t,x)/(t,y) balance condition leaves its value unchanged,
by x/y symmetrization. An explicit symmetric reflection of the optimal
shift on t in [0,1/4] preserves all these marginals and proves

```text
L_3 <= integral g dmu_ref < 4*pi*C_shift - 1/2496.
```

The entire altered slab uses the high-high chord branch; rationalizing
the geometric-mean saving supplies the analytic strict gap. Thus a sound
dual certificate for this relaxation cannot reach 4*pi*C_shift, even
with the balance constraint. No LP or numerical quadrature is a premise.

For B_m=min_P rho_P/(2m)^2, only
L_3/(4*pi)<=liminf B_m<=limsup B_m<=C_shift is asserted here. The
exact L_3, convergence of B_m and permutation realizability of mu_ref
remain unresolved in this task. A cheap coupling does not itself improve
B_m or R*(n); global bounds and finite certification are unchanged.

**Source:** `research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md`;
exact algebra/affine-marginal gates and bounded independent atan/integral
diagnostics in `ops/TASK-20260905__three_marginal_relaxation/`.

## Conjectural global interpretation of the fixed-order pattern

### Floating cascade

**Status:** mixed exact theorem and conjecture.

For every fixed integer radius `k>=1`, the general theorem above now proves
that the formal Supnick necklace on `{k,...,n}` eventually becomes
unrealizable across the seam `(n,k,n-1)` and remains obstructed thereafter.
The uniform theorem proves `4k+1<=s_k<=4k+14`, and the sequence theorem
proves `s_k=4k+6` for every `k>=6`. Specialized endpoint notes
prove `s_1=8`, `s_2=13`, `s_3=17`, `s_4=21`, `s_5=25`, `s_6=30`,
`s_7=34`, `s_8=38`, `s_9=42`, and `s_10=46`. All formal seam onsets are now
classified; global floating behavior is a separate problem.

The stronger claim that circle `k` eventually floats in global optima, with
recurring paid-then-free regimes, remains conjectural.

The paper reported seam-failure onsets `8,13,17` for circles `1,2,3` with
finite published scope. The post-v1 theorems above prove the exact all-`n`
onsets `s_1=8`, `s_2=13`, `s_3=17`, `s_4=21`, `s_5=25`, `s_6=30`,
`s_7=34`, `s_8=38`, `s_9=42`, and `s_10=46`, eventual persistent seam failure for every fixed radius, and
`s_k=4k+6` for every radius index `k>=6`. Every assertion about eventual
floating in global optima remains conjectural.

## Non-implications owned by this module

- Chain optimum is not automatically geometric optimum.
- Fixed-order feasibility is not global optimality.
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
- The all-`n` radius-10 seam obstruction does not prove full realizability
  before `n=46`, classify a global contact graph, or imply that radius `10`
  floats in any or every global optimum.
- The general fixed-`k` seam theorem does not by itself identify `s_k` for
  `k>=11`, prove full realizability before `s_k`, or imply that radius `k`
  floats in any or every global optimum.
- The uniform bound `4k+1<=s_k<=4k+14` does not identify any new exact onset,
  prove full realizability below it, determine `R*(n)`, classify a contact
  graph, or imply that radius `k` floats in any or every global optimum.
- The earlier effective identity `s_k=4k+6` for `k>=4325` does not alone
  classify smaller indices; the sequence theorem supplies that result.
- The sequence theorem alone does not prove full realizability below the
  seam; the separate fixed-order equivalence now proves that conclusion.
  It does not determine `R*(n)` or imply floating in any global optimum.
