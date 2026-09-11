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

The relaxation theorem alone gives
L_3/(4*pi)<=liminf B_m<=limsup B_m<=C_shift for
B_m=min_P rho_P/(2m)^2. A cheap coupling by itself is not a geometric
construction. The recovery theorem below supplies that missing step for
mu_ref specifically. The exact L_3 and convergence of B_m remain unresolved.

**Source:** `research/PERMUTED_HALVES_THREE_MARGINAL_RELAXATION.md`;
exact algebra/affine-marginal gates and bounded independent atan/integral
diagnostics in `ops/TASK-20260905__three_marginal_relaxation/`.

### Deterministic permutation recovery of mu_ref

**Status:** exact recovery theorem / exact fixed-order asymptotic theorem /
disproved asymptotic shift-optimality claim, after arXiv v1.

Fix the exact alpha=alpha_*. For every m>=2 set s=floor(alpha*m),
q=2*floor(m/8), H_m(j)=m+1+((j+s-1) mod m), and

```text
J_m(i)=q+2-i if i<=q is even, and J_m(i)=i otherwise,
P_{m,i}=H_m(J_m(i)).
```

The odd block ranks, reversed even block ranks and fixed tail partition
{1,...,m} exactly, so these are true high permutations at every size.
Their empirical triples converge weakly to the single mu_ref above,
along all integers m. The proof keeps the actual cyclic predecessor;
outside {1,q+1,m-s,m-s+1} intersect {1,...,m}, the comparison error is
at most 3/m. Parity Riemann sums yield the two half-weight orientations.

The already proved uniform full-radius theorem therefore gives

```text
R_full(1,P_{m,1},...,m,P_{m,m})/(2m)^2 -> C_ref
 = (integral g dmu_ref)/(4*pi)
 = C_shift-delta_alpha/(4*pi) < C_shift-1/(9984*pi),
```

where delta_alpha is the exact reflected-block saving defined in the
source. Thus limsup B_m<=C_ref<C_shift: optimized shifts are not
asymptotically optimal among all high permutations. This is an explicit
construction, not a determination of the best permutation coefficient,
the relaxation value or a general recovery theorem for balanced couplings.
The separate global upper-bound corollary is owned only by
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under reflected-coupling recovery.
No finite global certificate or contact/floater classification is changed.

**Source:** `research/PERMUTED_HALVES_MU_REF_RECOVERY.md`, Sections 2-5;
bounded exact occurrence, seam and independently integrated polynomial
checks in `ops/TASK-20260905__mu_ref_recovery/`.

### Longer reflected prefix with alpha_* fixed

**Status:** exact recovery, full-cost branch and fixed-order asymptotic
theorem; exact strict coefficient improvement, after arXiv v1.

For fixed alpha=alpha_* and every fixed 1/4<=lambda<1-alpha, replace the
preceding q by q_m=2*floor(lambda*m/2), retaining the same parity involution
and cyclic shift. These are true high permutations for every m>=2; their
empirical triples converge for every continuous test to the symmetric
reflection (A+t,A+lambda-t) on [0,lambda], A=1+alpha, and the diagonal
shift elsewhere. Exact predecessor bookkeeping includes q=0,2 and the
possible junction/endpoint coincidence r=q+1, r=m-s.

The limiting full coefficient is C_ref(lambda)=(integral g dmu_lambda)/(4*pi).
The reflected block switches from chord to chain sum at most once, when
sqrt(t/(A+t))+sqrt(t/(A+lambda-t)) reaches 1; the tail retains its own
switch and wrap. Rational sign gates prove alpha_*>1/12 and no reflected
block switch for the explicit witness lambda=3/10. Consequently

```text
C_30:=C_ref(3/10) < C_ref(1/4)-37/(1830400*pi),
C_ref(1/4)=C_ref (the preceding constant),
R_full(sigma_m(3/10))/(2m)^2 -> C_30.
```

The numerical observation C_30=0.1419245920564058523022... is diagnostic;
the strict inequality uses exact rational saving bounds. The uniform
full-radius theorem is imported, including all cyclic seam cells. There
is no reoptimization of alpha, best-lambda claim or general recovery or
permutation/coupling optimization. The separate global deletion corollary
is owned only by `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under longer
reflected prefix. Independent external review remains pending.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX.md`, Sections 2-6;
stdlib/Fraction and canonical mpmath bounded audits in
`ops/TASK-20260905__reflected_prefix/`.

### Exact lambda optimization of the reflected prefix at fixed alpha_*

**Status:** exact family-minimization and fixed-order coefficient theorem;
disproved whole-right-side monotonicity, after arXiv v1. Isolated sign and
constant gates use exact rational interval arithmetic.

Keep alpha=alpha_* exactly fixed and 1/4<=lambda<1-alpha_*. Put
A=1+alpha_*, x=lambda/A and Phi(x)=E'(x), where E is the normalized full
block cost minus the removed diagonal cost defined in the source.
The block changes from chord to chain at x=tau in (1/4,1/3); the tail
changes at x=1/3. The exact signs are Phi<0 before its unique middle
zero x_*, Phi>0 until a second zero x_dagger, and Phi<0 thereafter.
Analytically Phi'>41/72 on (tau,1/3) and Phi'<-1/420 on (1/3,1).

Consequently C_ref(lambda) has a unique global minimum lambda_*=A*x_*
and a subsequent strict local maximum lambda_dagger=A*x_dagger:

```text
159/500<lambda_*<319/1000,
A/3<lambda_dagger<4*A/5<1-alpha_*,
C_rp:=C_ref(lambda_*),
C_rp<C_ref(159/500)<C_30-1/100000,
C_rp<14191369/100000000,
R_full(sigma_m(lambda_*))/(2m)^2 -> C_rp.
```

The coefficient strictly decreases, increases, then decreases over the
three consecutive intervals. In particular
C_ref(891/1000)<C_ref(89/100) is a rigorous counterexample to strict
increase on the entire right side of the minimum. Concavity and an exact
positive endpoint comparison prove that the final descent never reaches
the unique minimum. The observations lambda_*=0.3183453891702156... and
C_rp=0.1419136786491478... are numerical, not definitions or premises.

The full-radius transfer uses the preceding all-integer recovery and
uniform full-root theorem. Only lambda in this family is optimized;
alpha, general permutations/couplings and geometric global optima are
not optimized. The separate feasibility/deletion corollary is owned by
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under the optimized reflected
prefix. The alpha extension below takes this theorem as its accepted input.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md`,
Sections 2-8; exact integer interval gates and independent full-max
diagnostics in `ops/TASK-20260905__reflected_prefix_lambda/`.

### Alpha improvement of the reflected prefix at fixed normalized minimizer

**Status:** exact recovery, fixed-order coefficient and first-variation
theorem; exact strict coefficient improvement, after arXiv v1.

Keep the preceding exact x_* fixed, and set lambda=(1+alpha)*x_*.
On the explicit neighborhood I=[53/500,107/1000], the same parity
involution and shift, with s=floor(alpha*m), q=2*floor(lambda*m/2),
give true high permutations for every m>=2. The block stays before the
wrap, with b-lambda>131/250; all predecessor/seam cells are retained.
Recovery for every continuous test and the imported uniform full-root
theorem give

```text
C(alpha,x_*)=K(alpha)/(2*pi)+(1+alpha)^2*E(x_*)/(4*pi),
R_full(sigma_m(alpha))/(2m)^2 -> C(alpha,x_*),
partial_alpha C(alpha,x_*)=[K'(alpha)+(1+alpha)*E(x_*)]/(2*pi)
                         < -1/12000 throughout I,
partial_alpha C(alpha_*,x_*)=(1+alpha_*)*E(x_*)/(2*pi)<0.
```

The wrapped-tail dependence is in K; neither that tail nor lambda is
held constant in this variation. The analytic saving E(x_*)<-1/1728
and fresh rational concave-quadrature gates prove

```text
53/500<alpha_*<267/2500<107/1000,
C_107:=C(107/1000,x_*) < C_rp-1/60000000,
C_107<14191368/100000000.
```

The full criterion supplies actual all-pairs feasible placements at each
fixed-order root. The numerical observations C_107=0.1419136480067209...
and derivative at alpha_*=-0.0001487181275456... are not proof premises.
This is a strict improvement at one rational alpha, without alpha or
joint parameter minimization, or a general permutation/coupling search.
The separate deletion corollary has its sole owner in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under the alpha-improved reflected
prefix. Independent external review of this extension remains pending.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md`,
Sections 2-5; independent stdlib rational gates and full-max/geometry
diagnostics in `ops/TASK-20260905__reflected_prefix_alpha/`.

### Exact alpha minimum of the reflected prefix at fixed x_*

**Status:** exact recovery, family-minimization and fixed-order full-radius
theorem; exact coefficient improvement, after arXiv v1.

Keep the accepted normalized x_* fixed. The preceding coefficient formula
extends to every fixed alpha in [0,1/2], with lambda=(1+alpha)*x_* and
uniform pre-wrap gap greater than 1/15. The parity involution gives true
high permutations for every m>=2. Unioned exceptions handle coincident
small-m seams, alpha=0 and alpha=1/2; the full cost retains both branches.

For F(alpha)=2*pi*C(alpha,x_*), the exact analytic bounds give

```text
-1/324<E(x_*)<-1/1728,
F'=D(alpha)+(1+alpha)*E(x_*),
F''>46/405>1/9 on [0,1/2],
F'(0)<-29/1245<0<13/108<F'(1/2).
```

Therefore F' has exactly one zero alpha_hat and it is the unique minimum
of this fixed-x_* coefficient family on [0,1/2]. Independent rational
full-block and D enclosures prove

```text
1093/10000<alpha_hat<10931/100000,
C_hat:=C(alpha_hat,x_*)<C_107-1/22000000,
C_hat<14191364/100000000,
R_full(sigma_m(alpha))/(2m)^2 -> C(alpha,x_*) for every fixed alpha in [0,1/2],
R_full(sigma_m(alpha_hat))/(2m)^2 -> C_hat.
```

The accepted full-root theorem and explicit valley gaps separately give
actual all-pairs feasibility at every exact root. The bracket and
coefficient comparisons use no decimal premise. The numerical observations
alpha_hat=0.1093036963264... and C_hat=0.1419134913446... are diagnostic.
This fixed-x theorem alone does not establish a finite-m family minimizer,
joint parameter optimum, other alpha regime, general permutation/coupling
optimum or geometric global optimum. The joint result follows below.
The separate global deletion corollary is owned only by
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under the fixed-x_* alpha minimum.
Independent external review of the new extension remains pending.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md`,
Sections 1-6; bounded independent exact gates and original full-max
diagnostics in `ops/TASK-20260905__reflected_prefix_alpha_minimum/`.

### Exact joint minimum of the two-parameter reflected-prefix family

**Status:** exact recovery, fixed-order full-radius and family-minimization
theorem, after arXiv v1; the two one-variable minima are user-accepted inputs.

For every fixed 0<=alpha<=1/2 and 1/4<=lambda<1-alpha, use the same
parity involution with s=floor(alpha*m), q=2*floor(lambda*m/2).
The resulting high permutation exists for every m>=2. The inequality
s+q<m keeps the reflected block before the finite wrap. Exact exception
unions include q=0,2, both alpha endpoints, junction/endpoint coincidences
and the m=2,alpha=1/2 low-seam/wrap-endpoint coincidence. Continuous-test
recovery needs no common positive lower bound on 1-alpha-lambda.

Writing A=1+alpha and x=lambda/A, the full max, with both block and
diagonal switches retained, gives

```text
R_full(sigma_m(alpha,lambda))/(2m)^2 -> C(alpha,lambda)
 =K(alpha)/(2*pi)+A^2*E(lambda/A)/(4*pi).
```

Here E is exactly the normalized function in the lambda theorem above;
the previous alpha theorem's C(alpha,x_*) denotes this formula with
lambda=A*x_*. Since 1/(4*A)<=1/4<x_*<1/3<=(1-alpha)/A,
that comparison construction is strictly admissible at every alpha.
Subtracting C_hat splits the coefficient difference into the positive
factor A^2/(4*pi) times E(x)-E(x_*) and the fixed-x_* alpha difference.
The accepted strict equality conditions prove

```text
C(alpha,lambda)>=C_hat,
equality iff (alpha,lambda)=(alpha_hat,(1+alpha_hat)*x_*).
```

This is the unique global minimum of the stated two-parameter leading
coefficient family. The excluded wrap boundary has a strict coefficient
gap, including when alpha varies. The exact full-root theorem separately
supplies actual all-pairs feasible placements at every m. No finite-m
family optimizer, other alpha regime, wrap-crossing construction, general
permutation/coupling optimum or geometric global optimum is established.
The existing global limsup bound keeps its sole owner in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`; its value C_hat is unchanged.
Independent external review of this extension remains pending.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md`,
Sections 1-7; bounded stdlib exact domain and finite floor/seam checks in
`ops/TASK-20260905__reflected_prefix_joint_minimum/`.

### Second disjoint reflected block: exact continuum direction

**Status:** exact continuum theorem / counterexample to balanced-coupling
local minimality, after arXiv v1.

At the baseline alpha=alpha_hat, A=1+alpha, lambda=A*x_*, set a=A/3 and
b=1-alpha. For a fixed lambda<u<b, replace only the diagonal slab
I=[u,u+epsilon], 0<epsilon<b-u, by the equal mixture of high pairs
(A+t,A+2*u+epsilon-t) and its swap. Reflection preserves both high
marginals separately; the swap preserves exact local balance. The low
marginal is unchanged. For C(mu)=(integral g dmu)/(4*pi) and the full
g=max(sqrt(t)*(sqrt(x)+sqrt(y)),sqrt(x*y)), the width derivative is zero
at every u, but the first nonzero terms are

```text
Delta C=-epsilon^3/(96*pi*(A+u))+o(epsilon^3),      lambda<u<a;
Delta C=+epsilon^2/(256*pi)+O(epsilon^3/a),         u=a;
Delta C=-epsilon^3/(96*pi*sqrt(u*(A+u)))
         +o(epsilon^3),                          a<u<b.
```

Every fixed u!=a strictly decreases the cost for all sufficiently small
positive widths; at a it strictly increases. The linear coefficient
vanishes everywhere, the quadratic coefficient vanishes exactly off a,
and neither cubic coefficient has a zero. Exact branch intervals and a
positive remainder bound at a are in the proof. The rational witness
u=1/3, epsilon=1/100 satisfies all domain/branch gates and has
C(mu)<C_hat-1/(144000000*pi). The smaller-width witnesses approach the
baseline in total variation, disproving balanced-coupling local minimality.

This preserves the earlier unique minimum within the one-prefix family.
The original continuum note does not establish finite recovery; the
following entry resolves that separate question for the fixed witness.
No moving-u or arbitrary larger-width sign classification, finite radius
improvement, or new geometric/global upper bound is established by the
continuum variation alone. The full-root entry below supplies the later
geometric transfer for the fixed witness.
Independent external review remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_REFLECTED_BLOCK.md`;
bounded stdlib exact gates, formal Taylor checks and an independent
rational cost enclosure in `ops/TASK-20260905__second_reflected_block/`.

### Deterministic recovery of the fixed second reflected block

**Status:** exact finite construction / exact weak-recovery theorem,
after arXiv v1.

At exactly alpha=alpha_hat, lambda=(1+alpha_hat)*x_*, the baseline
prefix and the fixed second block [1/3,103/300] are recovered together
by deterministic high permutations for every integer m>=2. Keep
s=floor(alpha*m), q=2*floor(lambda*m/2), and reverse even ranks
separately in {1,...,q} and {p+1,...,p+d}, with
p=2*floor(m/6), d=2*floor(m/200), before the cyclic high shift.
The two rank sets are disjoint and pre-wrap for every m; each high
occurs exactly once. The proof treats actual cyclic predecessors,
empty/length-2 identity blocks, odd/even m, both junctions of the
second block and the separate wrap endpoint/jump.

There are exactly six exceptional comparison cells for m>=200,
with the complete smaller-m counts stated in the proof. For every
continuous F on [0,1] x [1,2]^2, the empirical error is bounded by
omega_F(5/m)+omega_F(2/m)+32*||F||_infinity/m for m>=200, and hence
tends to zero along all integers. Both orientations are recovered
for nonsymmetric tests; limiting marginals/local balance are not
used as a sufficient condition. The signed empirical difference
from the baseline also recovers exactly the second-slab replacement.

This recovers the preceding continuum witness, including its continuous
g-integral. The recovery theorem alone does not identify a full radius;
the following entry supplies that separate transfer. No general coupling
recovery or optimization is asserted. Independent external review of the
proof and its imported inputs remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_RECOVERY.md`, Sections
1-5; bounded independent list/cyclic checks and exact interval test
integrals in `ops/TASK-20260905__second_block_recovery/`.

### Fixed second reflected block: full-root transfer and odd-order limit

**Status:** exact fixed-order feasibility and asymptotic theorem / exact
coefficient comparison, after arXiv v1.

Keep exactly alpha=alpha_hat, lambda=(1+alpha_hat)*x_* and [1/3,103/300]
in the preceding recovery construction. Every resulting alternating
order sigma_m satisfies the arbitrary-permutation all-pairs criterion:
the highs are distinct, occupy [m+1,2m], and exceed every low. All actual
cyclic cells, small coincident seams, both second-block junctions and the
separate wrap endpoint/jump are retained in the full max. At its unique
root rho_m, explicit positive valley gaps give actual all-pairs feasible
placements, with both directed paths checked for every pair type.

For the full cost g, t<=1/4 is always chord, making g globally
4-Lipschitz on [0,1] x [1,2]^2. The independent weak-recovery theorem
therefore gives |integral g dmu_m-integral g dmu_2|<=124/m for m>=200.
Uniform angular errors first bracket rho_m/(2m)^2 in (1/32,1/2), then
prove

```text
|R_full(sigma_m)/(2m)^2-C_2|
 <=(1148/m+16384/(3*m^2))/(4*pi), m>=2048.
```

With A=1+alpha_hat, epsilon=1/100, h=1/200 and M=A+1/3+1/200,
the exact coefficient and comparisons are

```text
J=integral_(-h)^h z^2/(M+sqrt(M^2-z^2)) dz,
C_2=C_hat-J/(4*pi),
C_2<C_hat-1/(144000000*pi), C_2<141913638/10^9,
2290431561/10^18 < C_hat-C_2 < 2290454215/10^18.
```

The full integral retains both prefix branches and both diagonal-tail
regimes; exact inequalities make the entire second block chord. At the
finite roots, explicit sign margins also distinguish all seam branches
for m>=100000; smaller m always use the full max.

Deleting radius 2m defines an odd order sigma_m^- with a feasible
placement at rho_m. Deletion alone is only an upper bound. A separate
necessary sum of the m-2 surviving whole cells, with uniform O(1/m)
cost for the two omitted cells, supplies the lower squeeze and proves
R_full(sigma_m^-)/(2m-1)^2->C_2. Thus both parities have this prescribed
fixed-order limit. The global corollary has its sole owner in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under the fixed second-block
transfer. No larger-family optimization, finite comparison cutoff,
global sharpness or contact/floating statement is established.
External independent proof review remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md`, Sections
1-8; exact branch/seam gates, independent arctangent intervals, deletion
incidence and recovery rerun in `ops/TASK-20260906__second_block_full_root/`.

### Complete continuous width minimum of the second reflected block

**Status:** exact continuous theorem with rational interval gates,
after arXiv v1.

Keep exactly alpha=alpha_hat, lambda=(1+alpha_hat)*x_* and u=1/3.
For the same symmetric second-slab replacement, the full-max difference
Delta C(epsilon)=C(mu_epsilon)-C_hat is classified throughout
0<epsilon<L=1-alpha_hat-u. Its sole global minimum satisfies

```text
31248/10^6<epsilon_*<1/32.
```

It decreases to epsilon_*, increases to a unique local maximum
epsilon_dagger in (1/3,2/5), and decreases from there to L. Its value
at the minimum is negative, whereas the continuous endpoint value at L
and the value at h=alpha_hat/3 are positive. There is exactly one
positive-width zero, between epsilon_* and h. The complete formula
retains the block-entry switch tau, the diagonal switch h and the
spatial crossing z=h at epsilon=2*h. Analytic monotonicity before h,
strict concavity of the first derivative after h, and eleven critical
rational enclosures prove uniqueness and all signs. The additional
digits epsilon_*=0.0312483174... remain a numerical observation.

This optimizes only the continuous width. No finite permutation at this
new width is constructed, and no new R_full limit or geometric/global
bound is deduced. The preceding recovery and full-root statements keep
their fixed width 1/100. The following entry resolves the local start
variation; joint minimization and a general continuum optimum remain
unresolved. External independent review and the imported baseline minimum
proofs remain separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_WIDTH.md`, Sections
1-8; bounded integer interval gates and separate raw-integral diagnostics
in `ops/TASK-20260906__second_block_width/`.

### Exact start derivative at the continuous width minimum

**Status:** exact continuous theorem with a rational interval gate,
after arXiv v1.

Fix exactly alpha=alpha_hat, A=1+alpha_hat, lambda=A*x_* and the preceding
exact epsilon_*. For the continuous second-slab family in (u,epsilon), put
D=4*pi*Delta C and B=A+1/3. Then

```text
D_u(1/3,epsilon_*)
 =2*B+epsilon_*-sqrt(B*(B+epsilon_*))
  -sqrt(1/3+epsilon_*)*(sqrt(B)+sqrt(B+epsilon_*)),
66955912/10^12 <= D_u(1/3,epsilon_*) <= 74512461/10^12.
```

The full-max derivation retains both moving slab endpoints and the
implicit switch velocity. Switch terms cancel by equality of costs.
Exact domain gates keep the removed diagonal wholly chord and the
reflected block mixed in a neighborhood. In translated coordinates the
chord derivative minus the diagonal derivative is nonnegative, and the
chain contribution is strictly positive. This proves the sign directly;
the width stationarity identity separately eliminates all integrals for
the displayed enclosure, using only the accepted alpha/epsilon brackets.

At (1/3,epsilon_*), D_epsilon=0 and D_u>0. Hence this point is not
stationary or locally minimizing in the continuous two-parameter family.
Moving the start slightly left at fixed exact width lowers the cost.
The local smooth branch of strict width minima exists by positive width
curvature; its value also has positive start derivative at this point.
No joint minimizer elsewhere or global continuation of that branch is
identified. Extra digits D_u=0.00007192229619488977... are diagnostic.

No finite recovery at epsilon_*, R_full transfer, new geometric/global
bound or finite optimization is asserted. Baseline and width-minimum
theorems are imported; independent external review remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_START.md`, Sections 1-6;
bounded stdlib domain/radical gates and independent raw-full-max diagnostics
in `ops/TASK-20260906__second_block_start/`.

### Exact start monotonicity on the entire chord-diagonal domain

**Status:** exact continuous theorem / proved boundary-infimum corollary,
after arXiv v1.

Keep exactly alpha=alpha_hat, A=1+alpha_hat, lambda=A*x_* and a=A/3.
For the same continuous symmetric second-slab replacement, put
D(u,epsilon)=4*pi*[C(mu_(u,epsilon))-C(mu_0)]. Throughout

```text
Omega={(u,epsilon): lambda<u, 0<epsilon<a-u},
D_u(u,epsilon)>=epsilon^3/[48*(A+u+epsilon)^2]>0.
```

The full max makes the removed diagonal chord on this domain. The
reflected block is either all chord or mixed, separated by the unique
unsquared endpoint threshold tau(u) in (0,a-u). Its first half is always
strictly chord and already gives the quantitative derivative bound;
any chain contribution is positive. At the entry tie the clipped switch
is only piecewise smooth, but D is C^1, with matching first derivatives.
The proof retains both moving slab endpoints and the switch cost term.

The coupling and cost extend continuously to lambda<=u<=a,
0<=epsilon<=a-u. At u=lambda the two separate reflections touch only
at zero-mass endpoints, preserving the same marginals and local balance.
For every interior pair, D(lambda,epsilon)<D(u,epsilon), and

```text
inf_Omega D = inf_(0<epsilon<a-lambda) D(lambda,epsilon).
```

No interior point is a local minimum. This theorem alone is an infimum
reduction; the following boundary theorem resolves width attainment,
location and uniqueness.
The zero-width edge has D=D_u=0 and is outside the strict-sign claim.
No sign beyond the chord-diagonal domain, finite permutation recovery,
R_full transfer or new R*(n) bound is supplied. The baseline minima are
imported; the width minimum and numerical diagnostics are not proof
premises. Independent external review remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_START_DOMAIN.md`,
Sections 1-6; only rational baseline-admissibility gates and separate
bounded raw-full-max diagnostics in
`ops/TASK-20260906__second_block_start_domain/`.

### Exact minimum of the continuous second-block boundary family

**Status:** exact continuous theorem with two rational endpoint sign gates /
proved continuous corollary, after arXiv v1.

Keep exactly alpha=alpha_hat, A=1+alpha_hat and u=lambda=A*x_*. Put
B=A+lambda and h=A/3-lambda. The same symmetric slab replacement at
the touching-block boundary defines D_b(epsilon)=D(lambda,epsilon).
On 0<epsilon<h it has a unique attained global minimum epsilon_b:

```text
43/1000<tau_b<87/2000,
tau_b<epsilon_b<tau_b+tau_b^2/(8*B)<11/250.
```

Here tau_b is the unique unsquared block-entry width. The full max
gives an all-chord branch before entry and a mixed branch afterwards;
the removed diagonal stays chord, with a tie only at the upper endpoint.
The cost is C^1 across entry but not C^2. Its derivative is negative
on the all-chord branch, and its mixed second derivative exceeds 1.
Analytic endpoint bounds prove D_b(h)>11*h^2/1440>0 and
D_b'(h)>11*h/280>0. Thus D_b decreases to epsilon_b, increases from
there to h, and has exactly one positive-width zero after the minimum.
The minimum is also unique on the closed width interval [0,h].

Only the two rational entry comparisons use the checker; curvature,
attainment, uniqueness and the distance from entry are analytic. The
exact baseline definitions and coarse brackets are imported. The digits
epsilon_b=0.04349174800601259590... and the corresponding cost
D_b(epsilon_b)=-0.00000235526264033607323... are numerical observations.

Together with the preceding start-domain theorem, this identifies its
open-domain infimum as D_b(epsilon_b) and the unique minimum of the
closed continuous triangle as (lambda,epsilon_b). The open domain
still has no minimizing point. This continuous theorem supplies no finite
recovery; that is established separately below. No new R_full limit or
R*(n) bound is supplied. The earlier fixed-width transfer keeps its
original parameters; general coupling optimality and transfer remain
outside the theorem. External independent review is separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md`,
Sections 1-7; Fraction-only endpoint gates and separate raw-full-max
diagnostics in `ops/TASK-20260906__second_block_boundary_minimum/`.

### Deterministic weak recovery of the adjacent-block boundary optimizer

**Status:** exact finite construction / exact quantitative weak-recovery
theorem, after arXiv v1.

Keep the exact alpha_hat, lambda=(1+alpha_hat)*x_*, u=lambda and
epsilon_b from the preceding boundary theorem. For every integer m>=2
set s=floor(alpha_hat*m), q=2*floor(lambda*m/2),
d=2*floor(epsilon_b*m/2). Rotate the high list by s, then reverse
the even positions separately in the adjacent rank blocks 1,...,q
and q+1,...,q+d. This gives a true permutation P_m of {m+1,...,2m}
for both parities and every floor or empty/length-2 case.

With the actual cyclic predecessor P_0=P_m, the empirical triples
(i/m,P_(i-1)/m,P_i/m) converge weakly to the boundary coupling with
its two separate adjacent reflections and unchanged diagonal tail.
The shared first-block exit/second-block entry is ONE cell, with pair
(m+s+2,m+s+q+1) when d>0. A complete cell partition has at most five
exceptions, including the cyclic seam and high-wrap comparisons.
No positive interblock gap from the older recovery is used.

For every continuous F on [0,1] x [1,2]^2 and every m>=2,

```text
|integral F dmu_m - integral F dmu_b|
 <=omega_F(4/m)+omega_F(7/m)+24*||F||_infinity/m.
```

The proof first allocates a rounded coupling exactly to parity panels,
then compares true and rounded parameters outside a union of three
short boundary intervals. Overlap of these intervals is allowed. The
standalone bounded checker audits all bracket-compatible floor triples
for m=2..512 using integer/Fraction arithmetic; the all-m theorem is
analytic. This recovery theorem alone asserts no full-root transfer or
radius conclusion; the next entry supplies that separate step. It uses
no numerical minimizer and asserts no finite-m optimality or general
recovery. The earlier fixed-width transfer retains its parameters.

**Source:** `research/PERMUTED_HALVES_BOUNDARY_RECOVERY.md`, Sections 1-6;
bounded exact checker and task evidence in
`ops/TASK-20260906__boundary_recovery/`.

### Boundary recovery: exact full root, uniform limit and odd lower squeeze

**Status:** exact fixed-order feasibility/limit theorem and proved
coefficient comparison, after arXiv v1.

Keep precisely alpha_hat, lambda=(1+alpha_hat)*x_* and epsilon_b in
the adjacent-block recovery. For every m>=2, the resulting permutation
satisfies all hypotheses of the arbitrary-high all-pairs criterion,
including the shared seam, small identity/empty blocks and high wrap.
The unique root rho_m of the sum of actual chain/chord maxima equals
R_full(sigma_m); explicit positive gaps realize all pair constraints
in both directions, including the m=2 two-cell case.

For the complete cost g the preceding recovery gives
|integral g dmu_m-integral g dmu_b|<=116/m for every m>=2.
The uniform angular estimate and a separately verified compact root
bracket give

```text
C_b=(integral g dmu_b)/(4*pi)=C_hat+D_b(epsilon_b)/(4*pi),
|R_full(sigma_m)/(2m)^2-C_b|
 <=[1140/m+16384/(3*m^2)]/(4*pi), m>=2048.
```

The second reflected block has a positive-length chord interval and a
positive-length chain interval; its removed diagonal is chord. The
full integral and the finite score retain both branches. The exact
boundary-minimum and start-domain theorems, with rational domain gates
for the old (1/3,1/100) comparison point, imply

```text
C_2-C_b>297881773/26740107869939200000>0.
```

Deleting only 2m gives a feasible odd order sigma_m^- at rho_m for
every m>=2. A separate necessary sum of the m-2 surviving cells has
root tau_m for m>=4 and proves tau_m<=R_full(sigma_m^-)<=rho_m.
The two omitted cells have an explicit uniform O(1/m) score bound.
This lower squeeze, with the normalization change, proves
R_full(sigma_m^-)/(2m-1)^2 -> C_b and the explicit odd error in source
equation (26). Deletion alone would give only the upper bound.

The global consequence is owned solely by
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`, under boundary full-root
transfer. No new parameter optimization, finite comparison cutoff,
global sharpness, global optimum or floating-circle claim is made.
The analytic proof supplies all-m quantifiers; finite arithmetic checks
and numerical all-pairs diagnostics are separate evidence. Independent
external mathematical review remains separate.

**Source:** `research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md`, Sections
1-8; standalone exact audits, alternate-angle/Cartesian and all-pairs
difference-constraint diagnostics, and dependency reruns in
`ops/TASK-20260907__boundary_full_root/`.

### Third adjacent reflected block: strict continuous full-cost improvement

**Status:** exact continuous theorem / explicit rational strict saving,
after arXiv v1.

Keep exactly alpha_hat, lambda=(1+alpha_hat)*x_* and epsilon_b in the
boundary coupling mu_b. At v=lambda+epsilon_b replace the diagonal slab
[v,v+1/1000] by its own symmetric reflection, defining mu_3 and C_3.
All three uniform marginals and equality of the (t,X)/(t,Y) marginals
are preserved. The second and third blocks and their high ranges touch
only at null endpoints; they retain separate reflections.

With delta=1/1000, A=1+alpha_hat, B=A+v and M=B+delta/2, the accepted
brackets alone give A-3v-4delta>1586317/100000000 and M<3/2.
Both the new slab and the removed diagonal are strictly chord in the
full max, including both endpoints. All unchanged mixed costs cancel.
The exact centered identity and its rational consequence are

```text
4*pi*(C_3-C_b)=-integral_(-delta/2)^(delta/2)
                z^2/[M+sqrt(M^2-z^2)] dz < -1/36000000000,
C_b-C_3 > 1/(144000000000*pi) > 1/576000000000 > 0.
```

The baseline definitions/brackets are imported; no new parameter bracket
or optimizer is computed. This continuous cost theorem alone supplies no
finite recovery, R_full transfer, new global bound or optimality of mu_3;
the following entries supply the separate finite recovery and geometric
transfer. Current global bounds belong to their separate owning ledger.
Independent external mathematical acceptance remains separate.

**Source:** `research/PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md`, Sections
1-6; standalone rational gates, endpoint/marginal probes and independent
raw-full-max integral enclosure in `ops/TASK-20260908__third_adjacent_block/`.

### Third adjacent reflection with variable width: exact continuous cost

**Status:** exact continuous theorem / explicit rational improvement,
after arXiv v1.

Keep alpha_hat, x_*, lambda=A*x_* and epsilon_b fixed; set
v=lambda+epsilon_b, A=1+alpha_hat, B=A+v, h=A/3-v. Replacing the
diagonal slab [v,v+Delta] by its own symmetric reflection defines
mu_3(Delta) and C_3(Delta). The existing unqualified mu_3 and C_3 retain
their width 1/1000, including in the finite and global results below.

The accepted brackets alone prove the explicit interval
0<Delta<=D_g=1986317/400000000. Throughout it, the coordinate domain,
all three uniform marginals and equal (t,X)/(t,Y) marginals hold; both
changed full maxima are strictly chord even at closed slab endpoints.
All unchanged costs, including the mixed second block, cancel in full.
With M=B+Delta/2 and q=Delta/(2*B+Delta),

```text
4*pi*[C_3(Delta)-C_b]
  =(Delta/2)*sqrt(B*(B+Delta))+M^2*asin(q)-Delta*M,
4*pi*C_3'(Delta)=sqrt(B*(B+Delta))+M*asin(q)-(B+Delta)<0,
C_3(1/1000)-C_3(1/250)>1/(2304000000*pi)>1/9216000000>0.
```

The exact first switch is the unique unsquared endpoint root tau_3 in
(D_g,h) of sqrt((v+Delta)/(B+Delta))+sqrt((v+Delta)/B)=1.
The formula and strict decrease extend through tau_3, with a single
endpoint tie. For tau_3<Delta<=h the third slab has one interior switch
and a positive chain correction to the displayed chord formula. That
chord-branch theorem stops at entry; the following entry resolves the
mixed-regime derivative and stationary width.

This continuous theorem alone supplies no finite recovery or geometric
transfer. The [uniform transfer entry](#uniform-third-width-recovery-and-full-feasibility-transfer)
below supplies that separate step on [0,h]; the imported parameter
definitions/brackets remain unchanged.
Independent external acceptance remains separate.

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md`, Sections 1-5;
one standalone exact gate/formula checker and independent raw integral
enclosures in `ops/TASK-20260908__third_block_width/`.

### Unique continuous mixed-width minimum of the third reflection

**Status:** exact continuous theorem with two rational endpoint sign gates,
after arXiv v1.

With the preceding entry's exact alpha_hat, x_*, lambda and epsilon_b
fixed, put F(Delta)=4*pi*[C_3(Delta)-C_b] and Psi=F'. On precisely
tau_3<Delta<=h=A/3-v retain the unique switch z in (Delta/2,Delta)
defined by sqrt((v+z)/(B+z))+sqrt((v+z)/(B+Delta-z))=1. The full cost
is F_ch plus its strictly positive chain correction. Its exact derivative
is the chain endpoint cost minus (B+Delta), plus half the chord/chain
partial-width integrals in the source's (5)-(6).

Analytically Psi'>131/120>1 throughout the mixed interval, including the
left derivative at h. Entry has -tau_3^2/(8*B)<Psi(tau_3)<0, whereas
Psi(h)>11*h/280>0. Thus neither direction of monotonicity holds on the
whole mixed interval: there is exactly one stationary width Delta_*, a
strict minimum. C_3 decreases up to it and increases thereafter through h.
Together with the preceding chord theorem it is the unique minimum on
the continuous extension [0,h]. Two rational signed-square gates and the
analytic distance from entry prove

```text
29/5000 < tau_3 < Delta_* < tau_3+tau_3^2/(8*B) < 27/4000 < h,
C_3(Delta_*) < C_3(tau_3) < C_3(D_g) < C_3(1/250) < C_3(1/1000) < C_b,
C_3(1/250)-C_3(Delta_*) > 12389/72000000000000 > 0,
-2187/2048000000000 < C_3(Delta_*)-C_b < -24389/72000000000000.
```

The sharper input inequality epsilon_b<7/160 is a rational weakening of
the already accepted boundary theorem's distance bound, not a new input
optimization. All interval quantifiers and cost comparisons are analytic;
the standalone Fraction checker checks only two fixed endpoint sign gates
and rational implications. No width scan or numerical root is used.
Finite recovery and geometric transfer at Delta_* require the separate
[uniform transfer theorem](#uniform-third-width-recovery-and-full-feasibility-transfer)
below; they are not consequences of this continuous calculation alone.
No reoptimization of fixed inputs, finite certification or paper revision
follows. Unqualified C_3 retains its historical meaning C_3(1/1000).

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md`, Sections 1-7;
bounded rational checker and local evidence in
`ops/TASK-20260908__third_block_mixed_width/`. External review is separate.

### Deterministic finite weak recovery of mu_3

**Status:** exact finite construction / exact quantitative weak-recovery
theorem, after arXiv v1.

Keep exactly alpha_hat, lambda=(1+alpha_hat)*x_*, epsilon_b and
delta=1/1000 in the preceding mu_3. For every integer m>=2 use
s=floor(alpha_hat*m), q=2*floor(lambda*m/2),
d=2*floor(epsilon_b*m/2), f=2*floor(m/2000). Rotate the high list
by s and reverse its even slots separately in the adjacent integer
blocks (0,q], (q,q+d], (q+d,q+d+f]. This extends boundary recovery
exactly, with no separately rounded starts or merged reflections.

The permutation and actual cyclic predecessor P_0=P_m handle every
floor tie, both parities, empty/length-2 blocks, fixed even midpoints,
shared endpoints and high wrap. With e=q+d and r=m-s, the complete
exception set is {1,r,r+1} union {q+1:q>0} union {e+1:d>0}
union {e+f+1:f>0}, intersected with 1,...,m. It has at most six
cells. When f>0, the second-third seam e+1 is one cell with ordered
pair (m+s+q+2,m+s+e+1), using the actual second-block predecessor.
The source gives the complete pair/parity/count tables and m=1 extension.

For every continuous, possibly nonsymmetric F on [0,1] x [1,2]^2,

```text
|integral F dmu_m - integral F dmu_3|
 <=omega_F(4/m)+omega_F(11/m)+38*||F||_infinity/m.
```

Exact parity-panel allocation and a union bound for all three moving
block boundaries and the wrap prove weak convergence along all integers;
overlapping bad intervals and disappearing rounded blocks are allowed.
The standalone integer/Fraction checker covers all bracket-compatible
floors for m=2..512 and 13 declared sizes through 8000. It checks
actual cyclic cells, exact third-floor onsets, counts, panel bounds,
residual corners and negative controls. The finite scan does not replace
the analytic all-m proof or select ambiguous implicit floors by decimals.

This theorem alone ends at finite recovery. The following entry supplies
the separate full-root transfer and odd squeeze. No finite-n optimum or
third-block parameter optimization is asserted; independent external
mathematical review remains separate.

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_RECOVERY.md`, Sections
1-6; standalone checker and evidence in
`ops/TASK-20260908__third_block_recovery/`.

### Three-block full-root transfer and quantitative even/odd limits

**Status:** exact fixed-order theorem / quantitative limits, after arXiv v1.

Keep precisely the preceding recovery's parameters and high permutation.
For every integer m>=2, its full-cell root rho_m equals R_full(sigma_m).
The actual q+1, e+1, z+1 seams, cyclic predecessor, high wrap and
empty/short blocks meet every arbitrary-high criterion hypothesis. Every
cell retains max(chain,chord); positive closed gaps realize both directed
constraints for every pair. The criterion also covers m=2 separately.

For the complete g and the preceding continuous definition of C_3,

```text
|integral g dmu_m-integral g dmu_3|<=174/m, m>=2,
|rho_m/(2m)^2-C_3|<=[1198/m+16384/(3*m^2)]/(4*pi), m>=2048.
```

The proof brackets the unknown root before substituting the uniform
angular error there. The max estimate allows finite/continuum branch
disagreement; the mixed second block remains mixed. The strict C_3<C_b
comparison and its exact rational saving are owned by the continuous
third-block entry above; the geometric limit identifies exactly that C_3.

Delete only 2m=P_r, r=m-s. For m>=4 the m-2 surviving disjoint cells
give a necessary score root tau_m and the genuine lower/upper squeeze
tau_m<=R_full(sigma_m^-)<=rho_m. The two removed cells have explicit
uniform O(1/m) score. Source equation (19) proves the quantitative odd
limit R_full(sigma_m^-)/(2m-1)^2 -> C_3. Small m=2,3 use deletion
feasibility without asserting a positive retained-score root.

The global corollary has its sole owner in
`knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md`. No global optimum, sharpness,
global normalized limit, finite comparison cutoff, new certificate,
floating conclusion or third-parameter optimization follows. Exact finite
checks and numerical observations support the analytic proof; independent
external mathematical acceptance remains separate.

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md`, Sections
1-7; bounded exact seam/branch/deletion checks, independent all-pairs and
Cartesian diagnostics and dependency reruns in
`ops/TASK-20260908__third_block_full_root/`.

### Fixed third width 1/250: integer recovery and full-root transfer

**Status:** exact fixed-order theorem / quantitative even and odd limits,
after arXiv v1; independent mathematical acceptance remains separate.

Keep the exact alpha_hat, lambda=(1+alpha_hat)*x_* and epsilon_b.
In the preceding three-block construction replace only the third length
by f=2*floor(m/500), corresponding to Delta=1/250. The strict half-wrap
margin is 23541513/1000000000; the new third block is empty at m<500,
identity of length 2 at 500<=m<1000, and nonidentity at m>=1000.
Every actual cyclic predecessor, shared second/third seam and exit remains
in the full maximum. In particular r=m-s>=q+d+f+2 and P_r=2m.

The recovered measures converge to precisely mu_3(1/250), with the same
arbitrary-continuous-test error omega_F(4/m)+omega_F(11/m)+38*||F||/m.
For EVERY integer m>=2 the full-cell root rho_m equals R_full(sigma_m)
and admits an all-pairs placement. Its quantitative limit is

```text
|rho_m/(2m)^2-C_3(1/250)|
  <=[1198/m+16384/(3*m^2)]/(4*pi), m>=2048.
```

Deletion of only 2m gives an odd feasible placement. For m>=4, the m-2
surviving disjoint cells give a necessary-score root tau_m and the separate
squeeze tau_m<=R_full(sigma_m^-)<=rho_m. Equation (12) of the source
proves R_full(sigma_m^-)/(2m-1)^2 -> C_3(1/250), also with an explicit
error at m>=2048. This gate concerns error bounds; even root feasibility
and deletion feasibility hold already at m>=2. Finite odd minima are not
identified with either bounding root.

The strict continuous saving remains owned by the variable-width entry
above. The global limsup consequence belongs only to the global ledger.
This transfer concerns exactly 1/250, without optimizing any parameter,
enumerating tours, changing lower bounds, proving global sharpness or
expanding finite certification. Old unqualified C_3 remains C_3(1/1000).

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_250_TRANSFER.md`,
Sections 1-6; independent bounded integer/rational root, seam, panel,
deletion and direct both-path checks in
`ops/TASK-20260911__third_block_250_transfer/check_transfer.py`.

### Uniform third-width recovery and full-feasibility transfer

**Status:** exact fixed-order theorem / uniform quantitative even and odd
limits, after arXiv v1; independent mathematical acceptance remains separate.

Keep precisely alpha_hat, x_*, lambda=A*x_* and epsilon_b from the
continuous-width entries. With v=lambda+epsilon_b and h=A/3-v, EVERY
real Delta in [0,h] admits the deterministic construction (6) in the source,
for every integer m>=2. It uses f=2*floor(Delta*m/2), with all starts
sums of rounded even lengths. Zero width, exact floor ties, short blocks,
both midpoint parities, actual shared seams and both cyclic paths are covered.

The uniform gates h<epsilon_b and alpha+v+Delta<1/2-523/25000 imply
f<=d<=q, r>=q+d+f+2 and P_r=2m. The high-shell triangle inequality
then makes the actual full-cell score a necessary and sufficient condition
for full feasibility, independently of its chord/chain branch. In particular
the old chord gate fails at h but is not a geometric necessity.

The empirical measures recover mu_3(Delta) uniformly on [0,h], with
arbitrary-test error omega_F(4/m)+omega_F(11/m)+38*||F||/m. Their
full-cell roots equal the actual even fixed-order full minima and satisfy

```text
sup_(0<=Delta<=h) |R_full(sigma_(m,Delta))/(2m)^2-C_3(Delta)|
  <=[1198/m+16384/(3*m^2)]/(4*pi), m>=2048.
```

Deleting only 2m gives odd feasible orders. The separate surviving-cell
lower root proves the uniform limit of their actual full minima, with
the explicit error (15). Feasibility holds at m>=2; only the error bound
requires m>=2048. Width sequences Delta_m->Delta in [0,h] also transfer,
using the width-continuity estimate (10).

Thus the entire mixed regime through the already defined Delta_* transfers.
The continuous minimum and strict saving remain owned by the mixed-width
entry; the global corollary belongs only to the global ledger. The endpoint
h is the studied cost-domain boundary, not a proved maximal geometric
threshold. No parameter reoptimization, global optimality, normalized global
limit, expanded finite certification or paper revision follows.

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_UNIFORM_TRANSFER.md`,
Sections 1-5; precise bounded endpoint/floor/panel discriminator and local
executable evidence in `ops/TASK-20260911__third_block_uniform_transfer/EVIDENCE.md`.

### Fourth independent reflection after the exact third-width minimum

**Status:** exact continuous theorem with an explicit rational width witness,
after arXiv v1; independent mathematical review remains separate.

Keep alpha_hat, x_*, epsilon_b and Delta_* exact and fixed. With
A=1+alpha_hat, v=A*x_*+epsilon_b, w=v+Delta_* and B_4=A+w, replace
only the diagonal slab [w,w+eta] by its own symmetric reflection, retaining
all three old reflections. The domain, uniform individual marginals and
equality of the (t,X)/(t,Y) marginals are preserved. For the normalized
complete-max increment J_4(eta)=C_4(eta)-C_3(Delta_*), the exact result is

```text
eta_0=1/20000, M=B_4+eta/2,
4*pi*J_4(eta)=-integral_(-eta/2)^(eta/2) z^2/[M+sqrt(M^2-z^2)] dz,
J_4(eta)=-eta^3/(96*pi*B_4)+R_4(eta),
0<=R_4(eta)<=eta^4/(192*pi*B_4^2),              0<eta<=eta_0,
J_4(eta)<-eta^3/576<0,
C_3(Delta_*)-C_4(1/20000)>1/4608000000000000.
```

The first nonzero unilateral term is cubic; the linear and quadratic terms
vanish. The inherited brackets yield A-3*w-4*eta>154539/1000000000,
so BOTH changed full maxima are strictly chord throughout the closed slab.
Old mixed blocks cancel with their full costs. The exact first new switch
is the unique unsquared root tau_4 in (eta_0,A/3-w) of
sqrt((w+eta)/(B_4+eta))+sqrt((w+eta)/B_4)=1. Beyond it a positive
chain integral is required; the witness does not encounter it.

This is a continuous improvement in an additional independent-block
direction, not an improvement by varying the third width alone. The
rational witness specifies only eta; all baseline minimizers stay exact.
The source identifies the later route's required genuine high permutations,
actual complete-cost recovery and existing shell full-cell criterion,
without constructing new finite orders or executing that transfer. The
transferred global bound remains owned by the global ledger; no new global
coefficient, finite certification, four-block optimum or paper claim follows.

**Source:** `research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md`, Sections 1-6;
bounded rational gates, raw-full-max enclosure and evidence in
`ops/TASK-20260911__fourth_adjacent_block/`.

### General finite and countable reflected-block recovery

**Status:** exact recovery and full-feasibility theorem, after arXiv v1;
separately internally adversarially validated, external acceptance pending.

Fix 0<=alpha<1 and nonnegative adjacent slab lengths ell_1,...,ell_k
with T=sum ell_j<1-alpha. Round each length downward to an even integer,
form starts from those rounded lengths, reverse even high ranks within
each block, and apply the cyclic shift floor(alpha*m). These are genuine
high permutations for all m>=max(2,ceil(2/(1-alpha-T))). Every shared
boundary, zero block, length-two identity, cyclic predecessor and wrap
cell is included. The empirical measures recover the separately reflected
slabs and unchanged shifted diagonal; no finite branch agreement is needed.

For the complete max g and C(mu)=integral g/(4*pi), the actual full minima
of the resulting even orders obey

```text
|R_full(sigma_m)/(2m)^2-C(mu)|
 <=[(6*k^2+28*k+1060)/m+16384/(3*m^2)]/(4*pi),
m>=max(2048,2,ceil(2/(1-alpha-T))).
```

The arbitrary-high cell theorem supplies every pair and both arc directions.
Deleting the largest high gives odd feasible placements. Countably many
slabs with total length strictly below 1-alpha also recover by finite
truncation and a diagonal sequence, so no indefinite transfer debt accumulates.
For the exact fourth-block inputs, k=4 gives coefficient 1268/m in the
root estimate and actual geometric realization of the continuous saving.
The global corollary has its sole owner in the global-bounds ledger.

**Source:** `research/PERMUTED_HALVES_GENERAL_BLOCK_TRANSFER.md`, Sections 1-5;
bounded exact arithmetic and internal review in
`ops/TASK-20260911__general_block_transfer/`.

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
