# Global Bounds and Asymptotics

This thematic ledger owns stable global lower and upper bounds, induced-subset
limits, heuristic larger-`n` observations, disproved asymptotic claims, and
open global questions. Linked proof notes remain authoritative for
mathematical detail.

## Exact post-arXiv-v1 global and asymptotic results

### Optimized induced-terminal-subset global lower bound

**Status:** exact theorem / proved corollary, after arXiv v1.

Deleting circles from an actual feasible configuration preserves central
tangency and all surviving pairwise constraints. Thus for every
`k>=1,n>=k+2`, with the original radii retained,

```text
R*(n) >= R*({k,...,n})
      = min_sigma R_full(sigma)
      >= min_sigma R_chain(sigma) = R_{k,n}.
```

This uses the published Supnick theorem for arbitrary distinct positive
radii; it requires no full feasibility of the minimizing chain. Deletion
also proves that `R*(n)` is nondecreasing. More generally, for any integer
sequences with `k->infinity` and `n/k->lambda>1`, both Supnick parities and
uniform angular errors give

```text
R_{k,n}/k^2 -> rho(lambda)
  = (2/pi) integral_1^((lambda+1)/2) sqrt(x(lambda+1-x)) dx.
```

Writing `tau` for the unique root of `tau=cos(tau)` in `(0,pi/2)`, exact
optimization over `lambda>1` has the unique solution

```text
lambda_*=(1+sin(tau))/(1-sin(tau)),
C_term=tau/(pi(1+sin(tau))),
liminf_{n->infinity} R*(n)/n^2 >= C_term,
lambda_*=5.12767681049949...,
C_term=0.1405690808452567....
```

The decimals are independently bracketed diagnostics, not proof premises.
This is the exact best coefficient in the proportional terminal-subset
deletion family. Boundary coefficients are `0` as `lambda` decreases to
`1` and `1/8` as `lambda` tends to infinity. The earlier `lambda=4`
coefficient `rho/16` is strictly smaller than `C_term` but still exceeds
`3/22>1/8` exactly.

Both `R*(n)=n^2/8 (1+o(1))` and `n^2/8-R*(n)=O(sqrt(n))` remain
**disproved claims**. No explicit threshold, matching upper bound, true
liminf/limsup, existence of a normalized limit, or floating-set conclusion
is supplied. The fixed finite-union theorem below closes the fixed-shape
nonterminal optimization, and the later exact finite theorem closes every
arbitrary `n`-dependent choice of one induced subset. For the first coupled
case see the two-terminal-subset entries below; one-level coupling has
subquadratic gain, while more general coupling and the true global
coefficient remain open. The arXiv-v1 record
and finite certification scope remain unchanged.

**Source:** `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`;
exact/symbolic audits in
`ops/TASK-20260904__optimized_terminal_subset_bound/`. The earlier special
`lambda=4` dossier remains historical evidence.

### Terminal dominance for every fixed finite-union induced subset

**Status:** exact continuum theorem / exact terminal-dominance theorem /
proved single-subset optimization corollary, after arXiv v1.

For every fixed positive-measure finite union of normalized intervals
`A subset [0,1]`, with length `L` and increasing quantile `Q_A`, the Supnick
chain coefficient is

```text
C(A)=(2/pi) integral_0^(L/2) sqrt(Q_A(t)Q_A(L-t)) dt.
```

The earlier uniform angular/root proof extends to sets touching zero because
for `R=rn^2`, `r>=r_0`, and all retained `1<=a,b<=n`, denominator
rationalization is uniformly `O(n^-2)` per edge and the arcsine remainder is
`O(n^-3)`; no positive normalized lower endpoint is needed.

The exact tail-capacity inequality

```text
|A intersect [0,x]| >= L-(1-x)
```

at `x=1-L+t` gives the pointwise quantile dominance

```text
Q_A(t)<=1-L+t,                     0<t<L.
```

Applying it at `t` and `L-t` in the functional proves

```text
C(A)<=C([1-L,1])<=C_term.
```

The first equality holds exactly when `A=[1-L,1]` modulo a Lebesgue-null
set: equality of the nonnegative integrand difference forces the terminal
quantile almost everywhere on both halves, and the generalized-inverse
distribution identity reconstructs the set measure. The accepted terminal
optimization makes the second equality unique at

```text
L=L_*=1-1/lambda_*=2 sin(tau)/(1+sin(tau)).
```

Consequently `C(A)=C_term` exactly for `A=[1/lambda_*,1]` modulo null sets.
This optimizes one fixed normalized finite-union induced subset, including
any fixed finite number of gaps. This continuum theorem itself does not cover
`A=A_n`, moving endpoints, a growing number of components, or diagonal
limits; the exact finite theorem below separately closes all of those cases
for one selected subset. Neither theorem covers genuinely coupled
information from several induced subsets, geometric upper bounds, or the
true Ringmin leading coefficient.

**Source:** `research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`; exact finite-grid
quantile/equality audit and dependency checks in
`ops/TASK-20260904__finite_union_terminal_dominance/`.

### Exact finite dominance for every induced subset

**Status:** exact finite theorem / exact asymptotic corollary, after arXiv v1.

For every `n`, every `3<=N<=n`, and every

```text
S={r_1<...<r_N} subset {1,...,n},
T={n-N+1,...,n},
```

the common Supnick rank-edge multiset and the order-statistic inequalities
`r_i<=n-N+i` give, at every fixed `R>0`, coordinatewise dominance of the
terminal closure sum. Strict angular monotonicity and decreasing-root
transfer prove

```text
R_chain(Supnick(S))<=R_chain(Supnick(T)),
```

with equality exactly when `S=T`.

For `0<=L<=1`, define

```text
G(L)=(2/pi) integral_0^(L/2) sqrt((1-L+t)(1-t)) dt.
```

A parity-uniform triangular-array argument for every moving terminal lower
endpoint proves that if arbitrary subsets `S_n` have `|S_n|/n->L`, then

```text
limsup R_chain(Supnick(S_n))/n^2<=G(L).
```

The boundary regimes are exact: the right side is `0` at `L=0` and `1/8`
at `L=1`. It has the unique maximum `C_term` at
`L_*=1-1/lambda_*`. With no cardinality limit or shape assumption at all,

```text
limsup R_chain(Supnick(S_n))/n^2<=C_term.
```

Every subsequence attaining `C_term` must have
`|S_n|/n->L_*=1-1/lambda_*`; no asymptotic subset-shape uniqueness follows.

This is sharp: the finite maximum over every subset and cardinality is the
maximum over terminal subsets, and its normalization tends to `C_term`.
Thus no arbitrary choice of one induced-subset chain bound improves that
leading coefficient. A pointwise maximum of individual subset bounds is
also inside the same envelope, but no conclusion is made for a genuinely
coupled-subset method, `R_full`, geometric upper bounds, or the true Ringmin
coefficient.

**Source:** `research/FINITE_INDUCED_SUBSET_DOMINANCE.md`; independent finite
enumeration and task evidence in
`ops/TASK-20260904__finite_induced_subset_dominance/`.

### Two coupled terminal subsets: exact finite separation

**Status:** exact counterexample / exact minimal-ambient-size theorem /
disproved universal equality, after arXiv v1.

For integers `3<=N<M<=n`, retain the original radii in
`T_j={n-j+1,...,n}`, and define

```text
A_j=R_chain(Supnick(T_j)),
B_{M,N}=min_{sigma on T_M}
             max{R_chain(sigma),R_chain(sigma|T_N)}.
```

Deletion from actual feasible configurations gives
`R*(n)>=B_{M,N}>=max{A_M,A_N}`. At `n=M=8,N=7`, with
`r_0=R_chain((1,7,3,5,4,6,2,8))`, the exact result is

```text
A_7<23/4<r_0=A_8<144/25,
B_{8,7}>max{A_8,A_7}+1/6000.
```

Every admissible triple with `n<=7` has equality, so 8 is the smallest
ambient counterexample size. A matrix-level strict anti-Monge perturbation
proves a positive cost gap for every other larger tour without enumeration;
the unchanged tour incurs the positive induced seam defect.

If the outer inclusion must be proper (`M<n`), the exact counterexample
is `n=13,M=12,N=11`, with

```text
B_{12,11}>max{A_12,A_11}+1/5000.
```

Every proper-outer-set triple with `n<=12` has equality, so 13 is minimal
under that convention. Both interpretations of the nested-set notation
therefore have a negative answer.

The same proof establishes uniqueness of the chain-optimal undirected
Supnick cycle for distinct positive radii. The top-four restriction of the
five-rank optimum is already nonoptimal, giving the smallest-cardinality
compatibility obstruction `M=5,N=4`. Yet the minimax equality holds at
`n=5`: simultaneous optimality is sufficient, not necessary for it.

The finite strict gain does not compute either minimax or geometric
optimum, improve `C_term`, establish asymptotic gain, classify all strict
triples, or expand global certification. This entry solely owns the finite
coupled result and its strictness/compatibility consequences; the next entry
resolves the one-level asymptotic scale. Prior one-subset results are unchanged.

**Source:** `research/COUPLED_TERMINAL_SUBSETS.md`; eight rational closure
gates corroborated by two independent angular formulas in
`ops/TASK-20260908__coupled_terminal_subsets/check_exact.py`.

### One-level terminal coupling: uniform linear gain and eventual equality

**Status:** exact theorem / proved asymptotic corollaries, after arXiv v1.

With precisely the preceding definitions, set M=n-k+1,N=n-k, so that
T_M={k,...,n} and T_N={k+1,...,n}. For all integers k>=1,n>=k+3,

```text
0<=G_{k,n}:=B_{M,N}-max{A_M,A_N}<=n/2.
n>=48k(k+1)^2 implies A_M<A_N, B_{M,N}=A_N, G_{k,n}=0.
```

Deleting k from the larger Supnick tour adds at most one pair angle;
the global closure derivative inequality -F'(R)>=F(R)/(R+n) converts
that seam defect to the uniform n/2 radius bound. For eventual equality,
insert k into the smaller Supnick tour's (k+1,n) edge. A degree-count
lower bound on its root and an analytic endpoint derivative estimate
make this insertion strictly decrease the closure sum at A_N.
Neither proof enumerates tours or assumes their full geometric feasibility.

Thus every fixed k has G_{k,n}=o(n^2), indeed eventual zero. Explicit
sufficient cutoffs are n>=192 for k=1 and n>=864 for k=2; these do not
contradict the preceding strict finite gaps at n=8 and n=13 and are not
claimed minimal. Both parities and the smallest admissible N=3 are covered.
The imported terminal-array theorem gives B_{n-k+1,n-k}/n^2->1/8 for
fixed k. Uniformity of n/2 also rules out a leading quadratic gain for
any moving one-level k(n); its limsup remains at most C_term by the
existing single-subset envelope.

This result rules out the one-level mechanism as a route to a stronger
leading coefficient. It does not classify all finite equality cases,
give a sharp transient gain bound, settle simultaneous multilevel or
widely separated coupling, prove any full feasibility or global optimum,
or change the existing global coefficients or finite certification scope.
This entry solely owns the one-level gain result; the earlier finite
counterexamples and single-subset theorems keep their own entries.

**Source:** `research/COUPLED_TERMINAL_ONE_LEVEL_ASYMPTOTICS.md`;
bounded exact checks, separate symbolic identities and optional prescribed
numerical diagnostics in `ops/TASK-20260909__coupled_terminal_scale/`.

### Increasing-order full asymptotic upper bound

**Status:** exact asymptotic theorem / explicit feasible construction /
proved global corollary, after arXiv v1.

For the increasing cyclic order `inc_n=(1,2,...,n)`, including the seam
`(n,1)`, let `A_n=R_chain(inc_n)` and `F_n=R_full(inc_n)`. A uniform angular
linearization over all `1<=a,b<=n` and the exact increasing edge-weight sum
give

```text
A_n = n^2/(2*pi)+O(n).
```

Closure at the chain root does not imply full feasibility: its forced tight
gaps violate the `(n,2)` constraint eventually, with scaled seam deficit

```text
n^(3/2)[theta(n,1)+theta(1,2)-theta(n,2)]
    -> 4*pi*(1-sqrt(2))<0.
```

At the explicit radius

```text
Rhat_n=n^2/(2*pi)+n^(3/2),
```

the unused closure angle `E_n` satisfies
`sqrt(n)E_n->4*pi^2`, while every pair angle is `O(1/n)` uniformly. Keep
every internal gap `(k,k+1)` tight and add all `E_n` to the seam gap.
Ordered-radius triangle inequalities make each non-seam path long enough;
every complementary path contains the enlarged seam and is guarded by
`E_n>max theta`. Hence all pairwise constraints hold for every sufficiently
large `n`, including pairs with a fixed or `o(n)` endpoint. Consequently

```text
F_n/n^2 -> 1/(2*pi),
limsup R*(n)/n^2 <= 1/(2*pi),
C_term <= liminf R*(n)/n^2 <= limsup R*(n)/n^2 <= 1/(2*pi),
R*(n)=Theta(n^2).
```

The theorem does not prove that the normalized global sequence converges,
that either endpoint is sharp, that the increasing order is asymptotically
optimal, or that the displayed `n^(3/2)` additive term is subleading-sharp.

**Source:** `research/INCREASING_ORDER_FULL_ASYMPTOTICS.md`; independent
high-precision all-pairs and Cartesian diagnostics in
`ops/TASK-20260904__increasing_order_full_asymptotics/`.

### Alternating-halves improved full asymptotic upper bound

**Status:** proved global limsup corollary of an exact fixed-order asymptotic
theorem, after arXiv v1.

For even `n=2m`, the fixed-order theorem owned by
`knowledge/FIXED_ORDER_THEORY.md` proves that

```text
sigma_{2m}=(1,m+1,2,m+2,...,m,2m),

R_full(sigma_{2m})/(2m)^2 -> C_alt,

C_alt=K/(2*pi),
K=3sqrt(2)/4-1/12
    +(log(3)-log(3+2sqrt(2)))/8
  =0.14233385361931275491....
```

The decimal is diagnostic only. Exact inequalities give `K<1`, hence
`C_alt<1/(2*pi)`. Minimization over orders gives the same upper coefficient
on even sizes. For odd `n=2m-1`, delete radius `2m` from the explicit even
configuration; the surviving radii are exactly `1,...,2m-1`, and the
normalization ratio `(2m/(2m-1))^2` tends to one. Therefore

```text
limsup R*(n)/n^2<=C_alt<1/(2*pi).
```

This strictly improves the increasing-order upper bound. It does not prove
that `C_alt` is globally sharp, give a matching global lower bound, establish
a normalized global limit, or optimize any broader order family.

**Source:** `research/ALTERNATING_HALVES_FULL_ASYMPTOTICS.md`; fixed-order
claim detail remains canonically owned by `knowledge/FIXED_ORDER_THEORY.md`.

### Optimized shifted alternating-halves global upper bound

**Status:** proved global limsup corollary, after arXiv v1.

Let alpha_* be the unique minimizer of the shifted-family full functional K,
as defined and proved in `knowledge/FIXED_ORDER_THEORY.md` and its source.
Choosing integer shifts floor(alpha_* m) gives an explicit even-size
construction. For odd n=2m-1, delete radius 2m from that same even
configuration; every retained central tangency and pairwise constraint
persists, and (2m/(2m-1))^2->1. Therefore

```text
limsup R*(n)/n^2 <= C_shift=K(alpha_*)/(2*pi)<C_alt,
C_shift=0.1419959781277142849792181240... .
```

The decimal is diagnostic. An explicit rational shift alpha=107/1000 and
directed rational sqrt/log/pi enclosures also give the weaker exact bound
limsup R*(n)/n^2<0.14199597951. This improves the unshifted construction;
it neither proves global sharpness nor a normalized global limit. The
existing lower coefficient C_term and finite certification scope are
unchanged. Optimization within the shift family remains canonically owned
by the fixed-order ledger.

**Source:** `research/SHIFTED_ALTERNATING_HALVES.md`, Sections 6-8;
arithmetic and diagnostic evidence in
`ops/TASK-20260905__shifted_alternating_halves/`.

### Reflected-coupling recovery: improved global upper bound

**Status:** proved global limsup corollary of an explicit feasible
construction, after arXiv v1.

Let C_ref be the exact full-radius coefficient of the deterministic
mu_ref recovery sequence defined in `knowledge/FIXED_ORDER_THEORY.md`.
At even size 2m, the exact full criterion supplies a feasible placement
at its full radius rho_m. Deleting radius 2m supplies an odd-size
placement at the same radius, and (2m/(2m-1))^2->1. Hence

```text
limsup R*(n)/n^2 <= C_ref < C_shift-1/(9984*pi) < C_shift.
```

Together with the existing terminal lower bound, this gives
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_ref. No equality,
normalized global limit, endpoint sharpness or finite global optimum
is asserted. The construction recovers only the prescribed coupling;
neither permutations nor the relaxation are optimized.

**Source:** `research/PERMUTED_HALVES_MU_REF_RECOVERY.md`, Section 6.
The recovery and fixed-order coefficient are owned by the fixed-order
ledger; the earlier shift upper bound remains valid but is weaker.

### Longer reflected prefix: improved global upper bound

**Status:** proved global limsup corollary of an explicit feasible
construction, after arXiv v1.

Use C_30=C_ref(3/10) from the fixed-order ledger's longer reflected prefix
theorem, with alpha=alpha_* unchanged. The exact full criterion supplies
feasible even configurations; deletion of radius 2m supplies odd ones.
Thus this construction supplies the valid upper bound

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_30<C_ref.
```

The strict comparison and the definition of C_30 have their sole owner in
`knowledge/FIXED_ORDER_THEORY.md`; C_ref keeps its original 1/4-prefix
meaning. The preceding bound remains valid but is weaker. No normalized
global limit, sharp endpoint, finite global optimum or stronger lower
bound is established.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX.md`, Section 6;
task-local evidence in `ops/TASK-20260905__reflected_prefix/`.

### Optimized reflected prefix: improved global upper bound

**Status:** proved global limsup corollary of the explicit feasible
fixed-alpha construction, after arXiv v1.

Use C_rp and the exact lambda_* defined solely in the fixed-order
ledger's lambda-optimization entry. Its all-integer recovery and full
radius theorem supply feasible placements at even sizes 2m. Deleting
only radius 2m gives the required odd sizes; the normalization ratio
(2m/(2m-1))^2 tends to one. Hence this construction gives the upper bound

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_rp<C_30.
```

The coefficient comparison and rational enclosure belong to
`knowledge/FIXED_ORDER_THEORY.md`; they also give the explicit global
corollaries limsup R*(n)/n^2<C_30-1/100000 and
limsup R*(n)/n^2<14191369/100000000. Uniqueness of the family minimizer
does not imply geometric global optimality, endpoint sharpness, a
normalized global limit, a new lower bound or a finite certificate.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md`,
Section 8; task-local evidence in
`ops/TASK-20260905__reflected_prefix_lambda/`.

### Alpha-improved reflected prefix: improved global upper bound

**Status:** proved global limsup corollary of the explicit feasible
construction at alpha=107/1000 and fixed x_*, after arXiv v1.

Use C_107 as defined only in the fixed-order ledger's alpha-improvement
entry. Its recovery and full-root theorem give feasible placements for
every even size 2m. Deleting only radius 2m gives exactly {1,...,2m-1},
preserving all remaining central tangencies and pairwise non-overlaps.
The normalization ratio tends to one, giving the upper bound

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_107<C_rp.
```

The coefficient comparisons owned by `knowledge/FIXED_ORDER_THEORY.md`
also yield the separate global corollaries
limsup R*(n)/n^2<C_rp-1/60000000 and
limsup R*(n)/n^2<14191368/100000000. The lower bound and finite certified
scope are unchanged. No joint parameter optimum, general permutation
optimum, global sharpness or normalized global limit is established.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA.md`,
Section 6; task-local evidence in `ops/TASK-20260905__reflected_prefix_alpha/`.

### Fixed-x_* alpha minimum: improved global upper bound

**Status:** proved global limsup corollary of the explicit feasible
construction at the exact family minimizer, after arXiv v1.

Use alpha_hat and C_hat as defined only in the fixed-order ledger's exact
alpha-minimum entry. Its full-root theorem provides actual feasible
placements for every even size. Deleting just radius 2m preserves all
central tangencies and non-overlaps for {1,...,2m-1}; the normalization
ratio tends to one. That construction gives the valid upper bound

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_hat<C_107.
```

The coefficient comparisons owned by `knowledge/FIXED_ORDER_THEORY.md`
also imply limsup R*(n)/n^2<C_107-1/22000000 and
limsup R*(n)/n^2<14191364/100000000. The lower theorem and finite certified
scope are unchanged. The later joint-family result is owned separately by
`knowledge/FIXED_ORDER_THEORY.md`, under the exact joint reflected-prefix
minimum. It leaves this upper coefficient unchanged and supplies no
general permutation/coupling optimality, global sharpness or normalized
global limit.

**Source:** `research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md`,
Section 7; task-local evidence in
`ops/TASK-20260905__reflected_prefix_alpha_minimum/`.
For the separate family result and its feasibility/deletion relationship,
see `research/PERMUTED_HALVES_REFLECTED_PREFIX_JOINT_MINIMUM.md`, Sections 6-8.

### Fixed second-block transfer: improved global upper bound

**Status:** proved global limsup corollary of the fixed recovered
construction and separate all-pairs/deletion proof, after arXiv v1.

Use C_2 as defined only in the fixed-order ledger's fixed second-block
entry. Its even orders are fully feasible at their exact roots; deleting
only radius 2m gives feasible placements on {1,...,2m-1}. Their normalized
root limits, proved separately from feasibility, yield the global upper bound

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_2<C_hat.
```

The exact coefficient comparisons owned by `knowledge/FIXED_ORDER_THEORY.md`
also imply limsup R*(n)/n^2<C_hat-1/(144000000*pi) and
limsup R*(n)/n^2<141913638/10^9. This transfers the earlier strict
continuum saving only after the empirical/full-root hypotheses have been
verified. Neither feasibility nor balanced marginals substitute for weak
recovery. No parameter or further block is optimized. The lower theorem,
finite certified scope and public arXiv-v1 assets are unchanged; global
sharpness, equality of liminf/limsup and finite global optimality remain
unresolved. Independent external review remains separate.

**Source:** `research/PERMUTED_HALVES_SECOND_BLOCK_FULL_ROOT.md`, Section 9;
fixed-order dependencies in Sections 1-8; local exact evidence in
`ops/TASK-20260906__second_block_full_root/`.

### Boundary full-root transfer: improved global upper bound

**Status:** proved global limsup corollary of the exact recovered
construction and all-pairs/deletion theorem, after arXiv v1.

Use C_b, its exact definition and strict comparison with C_2 solely
from the fixed-order ledger's boundary full-root entry. Even orders
are fully feasible at their exact roots for every m>=2; deleting only
2m supplies odd feasible placements, with normalization ratio tending
to one. These give the following upper bound, improved by the three-block
corollary below:

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_b<C_2.
```

The separate odd fixed-order lower squeeze is stronger than what this
global upper corollary needs. The recovered second block retains its
mixed full cost; the older chord-only hypothesis is not imported.
No global optimality, sharp endpoint, global normalized limit or new
finite certificate is established. Lower bounds, published assets and
production code retain their scope; external review is separate.

**Source:** `research/PERMUTED_HALVES_BOUNDARY_FULL_ROOT.md`, Section 9;
fixed-order dependencies in Sections 1-8 and local exact/numerical
evidence in `ops/TASK-20260907__boundary_full_root/`.

### Three-block full-root transfer: improved global upper bound

**Status:** proved global limsup corollary of the exact three-block
recovery, all-pairs transfer and separate odd lower squeeze, after arXiv v1.

Use the definition of C_3 and strict comparison C_3<C_b solely from
the fixed-order ledger's third-block entries. The exact recovered even
orders and the odd orders deleting only 2m are fully feasible; their
normalized fixed-order radii both tend to C_3. In particular

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=C_3<C_b.
```

This is the strongest current proved upper bound. Every finite cell
retains the full maximum, including all actual seams. The odd order's
lower squeeze is proved from retained disjoint cells, with no use of the
alternating criterion after deletion. Parameters are unchanged and no
third width/start is optimized. No global normalized limit, sharp endpoint,
finite-n global optimum or expanded certificate is established. The lower
bound and public arXiv-v1 assets retain their scope; external review is separate.

**Source:** `research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md`, Section 7;
fixed-order hypotheses and quantitative even/odd limits in Sections 1-6,
local exact/numerical evidence in `ops/TASK-20260908__third_block_full_root/`.

### First-order one-gap local optimality of the optimized terminal interval

**Status:** exact continuum theorem / proved first-order corollary, after
arXiv v1.

Let `alpha=1/lambda_*`, `s=1+alpha`, and delete a normalized band of total
width `epsilon` centered at a fixed `x in (alpha,1)` from `[alpha,1]`. For a
finite union `A` of normalized intervals, with increasing quantile `Q_A` and
length `L`, the arbitrary-radii Supnick edge formulas and the uniform angular
root bracket give the single-subset coefficient

```text
C(A)=(2/pi) integral_0^(L/2) sqrt(Q_A(t)Q_A(L-t)) dt.
```

Both exact Supnick parities, the seam, the even central edge, and the two
directions of rank reindexing are retained before the limit. For the one-gap
set, if `theta=asin sqrt(x/s)`, the iterated limit `n->infinity` first and
then `epsilon->0+` has first variation

```text
V(x)=(s/pi)[pi/4-theta-sin(theta)cos(theta)].
```

Writing `tau=cos(tau)` and using
`theta_alpha=pi/4-tau/2`, the bracket is zero at the non-interior endpoint
`alpha` and has derivative `-2cos(theta)^2<0`. Hence

```text
V(x)<0 for every fixed x in (alpha,1).
```

No fixed interior one-gap deletion therefore improves `C_term` to first
order; each gives a strictly smaller coefficient for all sufficiently small
positive fixed widths. The stronger terminal-dominance theorem above shows
strict loss for every admissible positive fixed width and covers every one
fixed finite-union multi-gap set. The variation itself remains pointwise in
`x`, not uniform for a center approaching `alpha`; the finite theorem above
separately closes moving and `n`-dependent single subsets. No result here
covers coupled-subset arguments, upper bounds, true asymptotics, floating
circles, or finite certification.

**Source:** `research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`; independent
symbolic rank/identity checks and finite diagnostics are recorded in
`ops/TASK-20260904__one_gap_terminal_subset_variation/`.

## Heuristic, conjectural, and disproved global claims

### Larger-`n` arrangements

**Status:** heuristic upper bounds and empirical structure.

The paper reports non-exhaustive local-search candidates for `15 <= n <= 18`. Their feasibility makes each radius an upper bound on `R*(n)` if independently checked, but no global optimality follows.

Reported patterns include:

- circles `{1,2}` floating in best-known candidates for `n=15,16,17`;
- circles `{1,2,3}` floating in the best-known candidate for `n=18`;
- repeated paid/free and seam-failure behavior resembling the finite regimes.

### Asymptotics

**Status:** exact two-sided coefficient bounds and disproved older claims,
after arXiv v1.

The unchanged public arXiv-v1 paper conjectures

```text
R*(n) = n^2/8 * (1 + o(1))
```

and tentatively the stronger deficit bound

```text
n^2/8 - R*(n) = O(sqrt(n)).
```

Both statements are now disproved by the exact optimized terminal-subset
theorem: `liminf R*(n)/n^2>=C_term>rho/16>3/22>1/8`. In particular,
eventually `n^2/8-R*(n)<-n^2/88`. This is a post-v1 correction to active
knowledge, not a revision of the historical paper.

The three-block full-root construction above gives the strongest
proved upper bound

```text
limsup R*(n)/n^2<=C_3<C_b<C_2<C_hat<C_107<C_rp<C_30<C_ref<C_shift<C_alt<1/(2*pi),
```

and hence `R*(n)=Theta(n^2)`. The true normalized liminf and limsup, their
possible equality, and either endpoint's sharpness remain unresolved.

**Sources:** `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`,
`research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`, and
`research/FINITE_INDUCED_SUBSET_DOMINANCE.md` for the lower side, and
`research/PERMUTED_HALVES_THIRD_BLOCK_FULL_ROOT.md` for the strongest upper
side. The earlier boundary, fixed second-block, one-prefix, reflected, shifted,
unshifted and increasing-order theorems remain valid but are weaker.
The single-subset envelope does not
settle the remaining coefficient gap.

## Primary open problems

1. Prove or refute the parts of the floating-cascade conjecture that concern global optima rather than formal Supnick seams.
2. Characterize the floating set `F(n)` asymptotically.
3. Determine the true global normalized liminf and limsup inside
   `[C_term,C_3]`, including whether they agree; improve beyond the
   current three-block construction or obtain sharper
   genuinely coupled-subset or full-geometric lower bounds beyond every single induced-subset chain
   bound. The proposed coefficient `1/8` is disproved.
4. Extend the structural analysis from radii `k` to `k^alpha` or general sequences without silently importing conclusions.

The sole ranked priority is maintained in `research/NEXT_RESEARCH_STEPS.md`.

## Non-implications owned by this module

- Finite induced-subset dominance optimizes the leading coefficient of every
  arbitrary one-subset chain-bound sequence; it does not cover genuinely
  coupled multiple-subset methods, `R_full`, or geometric upper bounds.
- The increasing-order theorem proves a feasible upper coefficient and the
  full asymptotic for that fixed order; it does not prove a global normalized
  limit, sharpness of `1/(2*pi)`, global optimality of that order, or a sharp
  subleading scale. Its chain root is eventually not fully feasible.
- The alternating-halves theorem improves the global limsup upper bound to
  `C_alt`; it does not prove equality, a normalized global limit, global
  optimality of that order, or a matching global lower bound.
- The shifted-family theorem improves that upper bound to `C_shift`; its
  unique family minimizer does not establish global optimality, global
  sharpness, a matching lower bound or a normalized global limit.
- Recovery of mu_ref and its longer prefix improve the upper bound to
  C_ref and C_30 respectively; neither result identifies
  the best high-permutation coefficient, a relaxation minimum,
  a global optimum or a normalized global limit.
- Optimizing lambda in the reflected-prefix family improves the upper
  bound to C_rp; its unique family minimum does not settle any of those
  broader optimization problems or optimize alpha.
- The rational alpha increase improves the upper bound to C_107; its
  strict directional improvement does not identify a joint parameter
  minimum or resolve those broader optimization problems.
- The exact fixed-x_* alpha minimum improves the upper bound to C_hat;
  its family uniqueness does not establish a general permutation/coupling
  optimum, global sharpness or a normalized global limit.
