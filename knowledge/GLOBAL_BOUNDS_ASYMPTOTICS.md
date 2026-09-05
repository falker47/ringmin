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
arbitrary `n`-dependent choice of one induced subset. Genuinely coupled
subset methods and full geometry remain open. The arXiv-v1 record and finite
certification scope remain unchanged.

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

The reflected-coupling recovery construction above gives the strongest
proved upper bound

```text
limsup R*(n)/n^2<=C_ref<C_shift<C_alt<1/(2*pi),
```

and hence `R*(n)=Theta(n^2)`. The true normalized liminf and limsup, their
possible equality, and either endpoint's sharpness remain unresolved.

**Sources:** `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`,
`research/ONE_GAP_TERMINAL_SUBSET_VARIATION.md`, and
`research/FINITE_INDUCED_SUBSET_DOMINANCE.md` for the lower side, and
`research/PERMUTED_HALVES_MU_REF_RECOVERY.md` for the strongest upper
side. The earlier shifted, unshifted and increasing-order theorems remain valid but
are weaker. The single-subset envelope does not settle the remaining coefficient gap.

## Primary open problems

1. Prove or refute the parts of the floating-cascade conjecture that concern global optima rather than formal Supnick seams.
2. Characterize the floating set `F(n)` asymptotically.
3. Determine the true global normalized liminf and limsup inside
   `[C_term,C_ref]`, including whether they agree; improve beyond the
   reflected-coupling construction or obtain sharper
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
- Recovery of mu_ref improves the upper bound to C_ref; it does not
  identify the best high-permutation coefficient, a relaxation minimum,
  a global optimum or a normalized global limit.
