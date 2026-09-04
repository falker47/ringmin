# Ringmin — Next Research Steps

## Role of this file

This is the sole ranked research roadmap. It records priorities and success criteria, not proofs, task chronology, or current task state.

The public arXiv-v1 paper already supplies:

- the angular reformulation;
- the anti-Monge/Supnick solution of the chain-ordering problem;
- a full all-pairs STN formulation;
- finite global certificates for `3 <= n <= 14`;
- explicit conjectures on seam failures, the floating cascade, and asymptotics.

The first ten precise transitions, the general fixed-radius persistence
mechanism, the uniform window `4k+1<=s_k<=4k+14`, and the eventual identity
`s_k=4k+6` have now been converted into exact theorems. The sequence theorem
in `research/SUPNICK_SEAM_SEQUENCES.md` proves this identity for every `k>=6`,
completing all formal seam onsets without expanding global certification.
The optimized shifted alternating-halves construction supplies the strongest
exact upper coefficient

```text
limsup R*(n)/n^2<=C_shift=0.14199597812771428498...<C_alt<1/(2*pi).
```

Together with `C_term=0.1405690808452567...` it proves quadratic growth while
leaving a much narrower genuine coefficient gap. The decimals are diagnostic;
the defining exact constants are recorded in the owning ledgers and proof.

## Resolved Priority 1 — First all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_n*` be the chain-optimal Supnick cyclic order on `{1,...,n}`, and let

```text
R_n = R_chain(sigma_n*).
```

The theorem now proved is:

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

for every integer `n >= 8`.

The reverse strict inequality holds for `3<=n<=7`, so the exact onset is `n=8`. The proof is in `research/RADIUS1_SEAM_OBSTRUCTION.md`. It compares strictly increasing chain roots with strictly decreasing explicit Descartes thresholds and closes `n=7,8` by rational inequalities. The raw angular deficit itself is not monotone.

This result concerns only the formal Supnick seam; it does not establish a global optimum or universal floating behavior.

## Resolved Priority 1 — Radius-2 all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_{2,n}*` be the chain-optimal Supnick cyclic order on `{2,...,n}`
and let

```text
R_{2,n} = R_chain(sigma_{2,n}*).
```

The theorem now proved is

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    > theta_{R_{2,n}}(n,n-1)       for 4 <= n <= 12,

theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)       for every n >= 13.
```

The proof is in `research/RADIUS2_SEAM_THRESHOLD.md`. It derives the shifted
Supnick convention and closure sums, proves that the implicit roots increase,
identifies the exact radius-2 threshold domain `n>=9`, proves that the
threshold decreases, and closes `n=12,13` by rational inequalities. The raw
angular deficit is not monotone.

This result concerns only the formal shifted Supnick seam; it does not
establish a global optimum or floating behavior.

## Resolved Priority 1 — General fixed-radius seam persistence

**Status:** proved after arXiv v1.

For every fixed integer `k>=1`, the canonical chain-minimizing Supnick order
on `{k,...,n}` has `n-1,n` as the neighbors of `k`. Its chain root
`R_{k,n}` strictly increases to infinity. The seam comparison has an exact
positive Descartes-threshold domain `n>=4k+1`, with

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))),
T_{k,n} = 1/kappa_{k,n}.
```

The thresholds strictly decrease to `k`, so `R_{k,n}-T_{k,n}` strictly
increases to infinity. Therefore every fixed radius has a finite first strict
seam obstruction, the obstruction persists thereafter, and equality can
occur at most once. The theorem by itself does not determine an exact onset
and makes no global-optimum or floating-circle claim.

The proof is in `research/FIXED_K_SUPNICK_SEAM.md`. The exact
`k=1,2,3,4,5,6,7,8,9,10` onsets follow by combining it with the endpoint bridges in
the ten specialized proof notes.

## Resolved Priority 1 — Uniform fixed-radius onset window

**Status:** proved after arXiv v1.

For the first strict-obstruction index of the formal fixed-radius Supnick
seam, the exact uniform bound is

```text
4k+1 <= s_k <= 4k+14              for every integer k>=1.
```

The lower bound is the general theorem's no-threshold range. For the upper
bound, the proof in `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md` uses only
the symbolic index `n=4k+14` and separator `S_k=k(21k+83)/22`: a strict chain
lower bound gives `R_{k,n}>S_k`, while a positive pre-square gate and an exact
coefficient-positive quadratic difference give `T_{k,n}<S_k`. The general
fixed-`k` sign criterion then supplies the strict obstruction. No finite scan
is used.

This theorem limits the search window for each formal onset but does not
identify the open exact onsets, prove full feasibility, or make a global or
floating-circle claim.

## Resolved Priority 1 — Effective fixed-radius onset formula and cutoff

**Status:** proved after arXiv v1.

For every integer `k>=4325`,

```text
s_k = 4k+6.
```

The proof in `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` treats only
`n=4k+c`, `c=5,6`. Both parity-explicit Supnick sums converge uniformly after
the `k^2` scaling:

```text
R_{k,4k+c}/k^2 -> rho,
rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx.
```

An exact conjugate calculation gives
`T_{k,4k+c}/k^2->24/(2c-1)`, while signed integral remainders certify
`24/11<rho<8/3`. The effective bridge uses the stronger rational separators
`11/5<20/9<rho<41/16<13/5`, the existing closure error, and the exact
threshold error `4193/(256k)`. The critical cutoff margin is
`256*4325-264*4193=248>0`. Thus the formal seam is unobstructed at `4k+5`
and obstructed at `4k+6` throughout the stated tail; fixed-`k` persistence
gives the formula. No finite scan is used.

The cutoff remains valid. This earlier theorem does not alone classify
smaller indices; the sequence theorem below completes them. Neither theorem
makes a full-feasibility, global-optimum, contact-graph, or floating-circle claim.

## Resolved Priority 1 — Radius-3 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{3,...,n}`, with
`R_{3,n}=R_chain(sigma*_{3,n})`, the exact classification is

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17.
```

Thus `s_3=17`. The proof in `research/RADIUS3_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.
```

The threshold inequalities are rational square comparisons. The chain
inequalities use rational termwise bounds on every arcsine argument and
elementary strict bounds with exact margins. Finite high-precision roots are
diagnostic only. The result concerns one formal seam and makes no claim about
`R*(n)`, full feasibility, or floating circles in global optima.

## Resolved Priority 1 — Radius-4 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{4,...,n}`, with
`R_{4,n}=R_chain(sigma*_{4,n})`, the exact classification is

```text
theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    > theta_{R_{4,n}}(n,n-1)       for 6 <= n <= 20,

theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    < theta_{R_{4,n}}(n,n-1)       for every n >= 21.
```

Thus `s_4=21`. The proof in `research/RADIUS4_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.
```

The threshold inequalities are rational square comparisons. The chain
inequalities audit all `17` and `18` adjacent edges with rational termwise
bounds and exact elementary bounds for `pi`. Finite high-precision roots are
diagnostic only. The result concerns one formal seam and makes no claim about
`R*(n)`, full feasibility, or floating circles in global optima.

## Resolved Priority 1 — Radius-5 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{5,...,n}`, with
`R_{5,n}=R_chain(sigma*_{5,n})`, the exact classification is

```text
theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    > theta_{R_{5,n}}(n,n-1)       for 7 <= n <= 24,

theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    < theta_{R_{5,n}}(n,n-1)       for every n >= 25.
```

Thus `s_5=25`. The proof in `research/RADIUS5_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.
```

The threshold inequalities use explicit sign gates and rational square
margins. The chain inequalities audit all `20` and `21` adjacent edges with
rational termwise arcsine bounds and exact polynomial/integral comparisons
with `pi`. Finite high-precision roots are diagnostic only. The result
concerns one formal seam and makes no claim about `R*(n)`, full feasibility,
or floating circles in global optima.

## Resolved Priority 1 — Radius-6 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{6,...,n}`, with
`R_{6,n}=R_chain(sigma*_{6,n})`, the exact classification is

```text
theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    > theta_{R_{6,n}}(n,n-1)       for 8 <= n <= 29,

theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    < theta_{R_{6,n}}(n,n-1)       for every n >= 30.
```

Thus `s_6=30`. The proof in `research/RADIUS6_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30}.
```

The threshold inequalities use exact rational square comparisons. The chain
inequalities audit all `24` and `25` adjacent edges with strict rational
termwise arcsine bounds and exact comparisons with `pi`. Finite
high-precision roots are diagnostic only. The result concerns one formal
seam and makes no claim about `R*(n)`, full feasibility, or floating circles
in global optima.

## Resolved Priority 1 — Radius-7 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{7,...,n}`, with
`R_{7,n}=R_chain(sigma*_{7,n})`, the exact classification is

```text
theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    > theta_{R_{7,n}}(n,n-1)       for 9 <= n <= 33,

theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    < theta_{R_{7,n}}(n,n-1)       for every n >= 34.
```

Thus `s_7=34`. The proof in `research/RADIUS7_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34}.
```

The threshold inequalities use explicit sign gates and exact rational square
comparisons. The chain inequalities audit all `27` and `28` adjacent edges
with strict rational termwise arcsine bounds and exact comparisons with
`pi`. Finite high-precision roots are diagnostic only. The result concerns
one formal seam and makes no claim about `R*(n)`, full feasibility, contact
graphs, or floating circles in global optima.

## Resolved Priority 1 — Radius-8 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS8_SEAM_ONSET.md` proves

```text
R_{8,37} < 176 < T_{8,37},
T_{8,38} < 176 < R_{8,38}.
```

Exact threshold sign/square gates and complete rational chain bounds for
all 30/31 edges, with exact comparisons to `pi`, close the bridge. The
fixed-`k` theorem then gives `Delta_{8,n}>0` for `10<=n<=37` and
`Delta_{8,n}<0` for every `n>=38`, hence `s_8=38`.
The prior numerical diagnostic is not a proof premise. This concerns one
formal seam and does not expand the global certification scope.

## Resolved Priority 1 — Radius-9 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS9_SEAM_ONSET.md` proves

```text
R_{9,41} < 220 < T_{9,41},
T_{9,42} < 220 < R_{9,42}.
```

All 33/34 edges, threshold positivity/pre-square signs, directed square
margins and strict rational arcsine/pi bounds close all four gates. The
fixed-k theorem gives positive deficit on `11<=n<=41` and negative deficit
for every `n>=42`, hence `s_9=42`. Only the two endpoints enter the exact
arithmetic; no numerical scan is a premise and no global claim is changed.

## Resolved Priority 1 — Radius-10 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS10_SEAM_ONSET.md` proves

```text
R_{10,45} < 270 < T_{10,45},
T_{10,46} < 270 < R_{10,46}.
```

Both full cycle representations, all 36/37 rational edge witnesses,
threshold positivity/pre-square signs and exact arcsine/pi bounds close
all four gates. The fixed-k theorem yields positive deficit for
`12<=n<=45` and negative deficit for every `n>=46`, hence `s_10=46`.
No numerical scan, floating root or preliminary reviewer value is a
premise. This concerns the formal seam exclusively.

## Resolved Priority 1 — Sequence monotonicity and all formal seam onsets

**Status:** proved after arXiv v1.

The proof in `research/SUPNICK_SEAM_SEQUENCES.md` establishes
`D_5(k+1)<D_5(k)` and `D_6(k+1)>D_6(k)` for every integer `k>=6`, where
`D_c(k)=R_{k,4k+c}-T_{k,4k+c}`. It treats the parity change through the
exact central-edge correction, compares implicit roots with an error
smaller than the consecutive-step margin, and checks all finite algebraic
gates exactly. No effective asymptotic bound or numerical scan is a premise.

The prior k=6 bridge and fixed-k persistence then give `s_k=4k+6` for
every `k>=6`. Together with the first five specialized onsets, all formal
seam indices are classified. Separate radius-11 and later endpoint bridges
are no longer needed to classify these onsets.

## Resolved Priority 1 — All-pairs feasibility just before the formal seam onset

**Status:** exact theorem / proved fixed-order corollary, after arXiv v1.

The proof in `research/SUPNICK_FULL_FEASIBILITY.md` establishes seam
dominance and full feasibility at the exact chain root on `{k,...,4k+5}`
for every integer `k>=6`. Every nonadjacent pair's two cyclic paths,
separately, have slack at least `(m-1)Delta>=Delta>0`, where `m` is the
path's edge count. Only the two-edge seam attains the minimum, up to reversal.

The proof first minimizes the defect over all triples through monotonicity
and the strictly positive mixed derivative of the angular kernel, then
telescopes over each path. It retains the exact central correction for
even cycles. The imported positive seam is used after that argument;
numerical diagnostics are not proof premises. The conclusion is restricted
to fixed-order full feasibility, without global or floating consequences.

## Resolved Priority 1 — Complete fixed-order full-feasibility classification

**Status:** exact theorem / proved fixed-order corollary, after arXiv v1.

The proof in `research/SUPNICK_FULL_FEASIBILITY.md` establishes full
feasibility at `R_{k,n}` iff `Delta_{k,n}>=0` for every k>=1,n>=k+2.
The generalized triangle and path lemmas cover both directions, adjacent
complements, small cycles and equality. Necessity uses closure to force all
adjacent gaps, then contradicts the seam complement's upper constraint.

The existing strict signs, imported only after that equivalence, give
feasibility precisely for k+2<=n<s_k and infeasibility at the root for
n>=s_k, where s_1=8, s_2=13, s_3=17, s_4=21, s_5=25 and s_k=4k+6 for
k>=6. No integer equality case exists. All conclusions remain fixed-order.

## Resolved priority — Optimized terminal-subset asymptotic lower bound

**Status:** exact theorem / disproved claim, after arXiv v1.

The proof in `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md` gives
the chain-root limit for every terminal-subset ratio `n/k->lambda>1` and
optimizes its normalized coefficient exactly. If `tau` is the unique root
of `tau=cos(tau)` in `(0,pi/2)`, the unique maximizing ratio and bound are

```text
lambda_*=(1+sin(tau))/(1-sin(tau))=5.12767681049949...,
liminf R*(n)/n^2>=C_term=tau/(pi(1+sin(tau)))
                         =0.1405690808452567....
```

The decimals are diagnostic only. This strictly improves the earlier
`lambda=4` coefficient `rho/16>3/22>1/8`. It combines deletion of actual
feasible configurations, arbitrary-radii Supnick chain optimality, both
edge parities, uniform small-angle control and an analytic uniqueness proof.
Both the proposed leading coefficient `1/8` and the stronger `O(sqrt(n))`
deficit remain disproved. The paper stays historical.

## Resolved priority — One-gap variation of the optimized terminal interval

**Status:** exact continuum theorem / proved first-order local-optimality
corollary, after arXiv v1.

The proof in `research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md` derives the
arbitrary-radii Supnick continuum functional for finite unions of normalized
intervals,

```text
C(A)=(2/pi) integral_0^(|A|/2)
                 sqrt(Q_A(t)Q_A(|A|-t)) dt,
```

then applies it to `[1/lambda_*,1]` with one fixed interior band of width
`epsilon` deleted. Both exact Supnick parities, exceptional edges, the
below/above-median rank shifts, and the iterated order `n->infinity` before
`epsilon->0+` are explicit. With `alpha=1/lambda_*`, `s=1+alpha`, and
`theta=asin sqrt(x/s)`, the variation is

```text
V(x)=(s/pi)[pi/4-theta-sin(theta)cos(theta)]<0
```

for every fixed `x in (alpha,1)`. The exact zero at the excluded lower
endpoint follows from `tau=cos(tau)`; strict decrease in `theta` gives the
sign without numerical input. Thus no fixed-center one-gap perturbation
improves `C_term` to first order. This variation statement is pointwise, not
a uniform moving-center or multi-gap variation; the next theorem supplies a
separate nonvariational comparison for every fixed finite-union set.

## Resolved priority — Terminal dominance for fixed finite-union subsets

**Status:** exact continuum theorem / exact terminal-dominance theorem /
proved single-subset optimization corollary, after arXiv v1.

Starting from the continuum functional in
`research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`, the proof now removes its
unnecessary positive-support restriction and covers every fixed
positive-measure finite union `A subset [0,1]`. If `L=|A|`, tail capacity
gives

```text
Q_A(t)<=1-L+t,
C(A)<=C([1-L,1])<=C_term.
```

Equality in the first inequality holds exactly for the terminal interval
modulo null sets; the already proved terminal optimization makes total
equality unique at `A=[1/lambda_*,1]` modulo null sets. This closes the
single fixed normalized finite-union route, including any fixed finite
number of gaps. This continuum theorem does not itself treat
`n`-dependent/diagonal sets or a growing number of components; the next
resolved theorem closes those cases for one selected subset. Neither covers
genuinely coupled multiple-subset bounds or geometric upper bounds.

## Resolved priority — Exact finite dominance for arbitrary induced subsets

**Status:** exact finite theorem / exact asymptotic corollary, after arXiv v1.

For every `S={r_1<...<r_N} subset {1,...,n}`, `3<=N<=n`, the proof in
`research/FINITE_INDUCED_SUBSET_DOMINANCE.md` compares it with
`T={n-N+1,...,n}`. The order-statistic inequalities
`r_i<=n-N+i`, the common Supnick rank-edge multiset, and strict angular
monotonicity give pointwise closure-sum dominance and hence

```text
R_chain(Supnick(S))<=R_chain(Supnick(T)),
```

with equality exactly for `S=T`. A separate parity-uniform triangular-array
limit covers every moving terminal endpoint, including cardinality ratios
tending to zero or one. Compactness then proves for every arbitrary sequence
of one selected induced subset

```text
limsup R_chain(Supnick(S_n))/n^2<=C_term.
```

The finite envelope over all subsets and cardinalities is attained among
terminal subsets and converges to `C_term`, so the result is sharp. This
closes every leading-coefficient improvement from a single induced-subset
chain bound, without shape, component-count, endpoint, or cardinality-limit
assumptions. Genuinely coupled-subset methods and full geometry remain open.

## Resolved priority — Increasing-order full asymptotic upper bound

**Status:** exact asymptotic theorem / explicit feasible construction /
proved global corollary, after arXiv v1.

For `inc_n=(1,2,...,n)`, the proof in
`research/INCREASING_ORDER_FULL_ASYMPTOTICS.md` first establishes

```text
R_chain(inc_n)=n^2/(2*pi)+O(n).
```

It then exhibits a full all-pairs placement at
`Rhat_n=n^2/(2*pi)+n^(3/2)`: all internal adjacent gaps are tight and all
closure slack is put into `(n,1)`. Internal paths satisfy an ordered-radius
triangle inequality, while every seam-crossing path is controlled uniformly
because the added slack is asymptotic to `4*pi^2/sqrt(n)` and every pair
angle is `O(1/n)`. This includes fixed and `o(n)` endpoints. Separately, the
`(n,2)` path proves that the exact chain-root placement is eventually
infeasible, so closure was not used as a substitute for full feasibility.

Therefore

```text
R_full(inc_n)/n^2->1/(2*pi),
limsup R*(n)/n^2<=1/(2*pi),
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=1/(2*pi),
R*(n)=Theta(n^2).
```

No normalized global limit, endpoint sharpness, optimality of the increasing
order, or sharp subleading scale is claimed.

## Resolved priority — Alternating-halves full asymptotic upper bound

**Status:** exact finite fixed-order characterization / exact asymptotic
theorem / explicit feasible construction / proved global corollary, after
arXiv v1.

For `n=2m` and

```text
sigma_{2m}=(1,m+1,2,m+2,...,m,2m),
```

the proof in `research/ALTERNATING_HALVES_FULL_ASYMPTOTICS.md` gives an exact
fixed-`R` criterion. Around each low valley, take the maximum of its two
adjacent constraints and the chord between its two high neighbors; the sum
`S_m(R)` of these disjoint cell requirements satisfies

```text
R_full(sigma_{2m}) = the unique root of S_m(R)=2*pi.
```

Explicit gaps attain this obstruction. A thick-shell lemma on the high radii
`m+1,...,2m` checks every long pair and the seam. Uniform angular scaling then
gives

```text
R_chain(sigma_{2m})/(2m)^2 -> J/(2*pi),
R_full(sigma_{2m})/(2m)^2 -> C_alt=K/(2*pi),

J=3sqrt(2)/4-log(3+2sqrt(2))/8,
K=J-1/12+log(3)/8<1.
```

The consecutive-high chords control below normalized low radius `1/6`; the
two chain adjacencies control above it; the seam is exact but lower order.
Deleting radius `2m` transfers `limsup R*(n)/n^2<=C_alt` to odd sizes. No
global equality, normalized global limit, or broader order optimization is
claimed.

## Resolved priority — Optimal macroscopic alternating-halves shift

**Status:** exact fixed-order and shift-family minimization theorem / proved
global limsup corollary, after arXiv v1.

`research/SHIFTED_ALTERNATING_HALVES.md` extends the exact cellwise criterion
to every cyclic high shift, derives the limit functional for every limiting
shift ratio, and proves its unique minimizer analytically. Deletion gives
the strictly improved upper coefficient C_shift defined in the owning global
ledger. Thus another macroscopic shift within this family cannot improve the
leading coefficient; broader full-geometric constructions remain open.

## Priority 1 — Independent review of the shifted alternating-halves theorem

Exactly one next atomic task: independently review the fresh thick-shell and
both-seam all-pairs proof, moving-jump Riemann limit, piecewise functional,
derivative boundary terms, unique-minimum argument, rational witness enclosure
and deletion corollary in `research/SHIFTED_ALTERNATING_HALVES.md`; record
acceptance or precise corrections without starting another order family.
Check recovery of the unshifted theorem as a dependency consistency gate.

## Deferred priority 2 — Independent review of increasing-order full asymptotics

Independently review the uniform angular
error, increasing edge-weight/root transfer, fixed-endpoint seam obstruction,
explicit two-directed-path gap proof, and the limited global deductions;
record acceptance or precise corrections without optimizing subleading terms.

## Deferred priority 3 — Independent review of exact finite subset dominance

Independently review the rank-edge convention,
strict equality case, decreasing-root direction, terminal triangular-array
limit at both boundary regimes, compactness argument, and distinction between
one-subset envelopes and genuinely coupled methods; record acceptance or
precise corrections.

## Deferred priority 4 — Independent review of finite-union terminal dominance

Independently review the extension of the
continuum functional to sets touching zero, the tail-capacity quantile
inequality, both equality reconstructions, the imported unique length
optimization, and the fixed-`A` limit scope. Success means an acceptance or
precise correction report without starting diagonal or coupled-subset
research.

## Deferred priority 5 — Independent review of the one-gap variation theorem

Independently review the continuum quantile pairing, both parity/reindexing
formulas, the first-variation calculation, the optimized-endpoint sign, and
the iterated-limit statement. The stronger dominance theorem does not make
the exact local variation calculation incorrect, but removes it as the sole
barrier to fixed finite-union optimization.

## Deferred priority 6 — Review the optimized terminal-subset theorem

Independently review the generalized terminal-subset limit, all
parity/end-point and uniform-error steps, the analytic optimization and the
all-integer floor deduction. This remains a dependency review rather than a
new research direction.

## Deferred priority 7 — Review the complete fixed-order classification

The previously proposed independent review remains pending. Its scope is
the generalized triangle/path lemmas, closure-forced necessity, equality,
small cycles and imported strict signs. This theorem is not a premise of
the new global lower bound.

## Deferred priority 8 — Determine the true leading asymptotics

Determine the true normalized liminf and limsup within
`[C_term,C_shift]`, and whether they agree. Improve beyond the optimized
shifted alternating-halves upper construction or derive stronger valid lower bounds beyond the resolved
envelope of every single induced-subset chain bound. Success must address
full feasibility or genuinely coupled constraints. Do not call either known
endpoint sharp, retain `1/8` as an open candidate, or assume the floating set
is `o(n)` without proof.

## Deferred priority 9 — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
