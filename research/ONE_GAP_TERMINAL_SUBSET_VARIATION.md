# One-gap variation of the optimized terminal-subset bound

```text
status=PROVED
classification=exact continuum theorem / proved first-order local-optimality corollary
domain=one fixed interior gap in the optimized normalized terminal interval
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Result and exact scope

Let `tau` be the unique root of

```text
tau=cos(tau),        0<tau<pi/2,
```

and put

```text
q=sin(tau),
lambda_*=(1+q)/(1-q),
alpha=1/lambda_*=(1-q)/(1+q),
s=1+alpha,
m=s/2.
```

Thus `[alpha,1]` is the normalized terminal interval which gives the
coefficient

```text
C_term=tau/(pi(1+sin(tau)))
```

in [the optimized terminal-subset theorem](INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md).
Fix an interior normalized radius `x in (alpha,1)`. For

```text
0<epsilon<2 min(x-alpha,1-x),
```

delete the band of total normalized width `epsilon` centered at `x`:

```text
A_{epsilon,x}
  =[alpha,x-epsilon/2] union [x+epsilon/2,1].            (1)
```

For each integer `n`, retain the actual, unshifted radii

```text
S_n(epsilon,x)={j in {1,...,n}: j/n in A_{epsilon,x}}.  (2)
```

Changing open to closed endpoints changes at most two radii and does not
change any limit below.

**Continuum Supnick functional.** If `A` is a finite union of intervals in
`[alpha,1]`, let `L=|A|` be its Lebesgue measure and let `Q_A:[0,L]->A` be
its increasing quantile, defined up to values at its finitely many jumps.
The chain root of the arbitrary-radii Supnick tour on
`{j: j/n in A}` satisfies

```text
R_chain(Supnick(S_n(A)))/n^2 -> C(A),

C(A)=(2/pi) integral_0^(L/2)
                 sqrt(Q_A(t) Q_A(L-t)) dt.              (3)
```

Consequently deletion from a feasible Ringmin configuration gives

```text
liminf_{n->infinity} R*(n)/n^2 >= C(A).                 (4)
```

For (1), write `C_epsilon(x)=C(A_{epsilon,x})`. Its exact
first variation at the unperforated interval is

```text
C_epsilon(x)=C_term+epsilon V(x)+o(epsilon),

V(x)=(s/pi)[pi/4-theta-sin(theta)cos(theta)],
theta=asin sqrt(x/s).                                  (5)
```

The sign is

```text
V(x)<0       for every fixed x in (alpha,1).            (6)
```

Thus no fixed interior gap center has a positive first variation. For each
such `x`, all sufficiently small positive gaps give a strictly weaker
coefficient than `C_term`. This proves first-order local optimality of the
optimized terminal interval within the stated one-gap, single-induced-subset
family.

The conclusion is pointwise in the fixed center `x`. The continuous extension
has `V(alpha)=0`, reflecting stationarity of the already optimized terminal
endpoint, so (6) is not a uniform negative margin as `x` approaches `alpha`.
No moving-center or multi-gap claim is made.

## 2. From arbitrary-radii Supnick tours to (3)

Let the retained radii be

```text
r_{n,1}<...<r_{n,N_n},       u_{n,j}=r_{n,j}/n.
```

The published arbitrary-radii Supnick theorem applies to these radii in their
increasing rank order. It is important that the values are neither filled
across the gap nor translated. Directly reading the Supnick rank tour gives
the following undirected edge multisets.

If `N_n=2h`, the two long families and the two exceptional edges are

```text
(j,N_n-j),       1<=j<=h-1,
(j,N_n+2-j),     2<=j<=h,
(1,N_n), (h,h+1).                                      (7)
```

If `N_n=2h+1`, they are

```text
(j,N_n-j),       1<=j<=h,
(j,N_n+2-j),     2<=j<=h+1,
(1,N_n).                                                (8)
```

Here an edge `(i,j)` means `(r_{n,i},r_{n,j})`. The counts in (7) are
`(h-1)+(h-1)+2=N_n`; those in (8) are `h+h+1=N_n`.
Thus the cyclic seam and the even central edge are both retained.

For a finite union of intervals, elementary grid counting gives

```text
N_n/n -> L
```

and the increasing grid order statistics converge to `Q_A` at every
continuity point after ranks are divided by `n`. The first long family in
(7) or (8), divided by `n^2`, is a mesh-`1/n` Riemann sum for

```text
integral_0^(L/2) sqrt(Q_A(t)Q_A(L-t)) dt.
```

The rank shifts in the second family are at most `2/n`, so it has the same
limit. The quantile has only finitely many jumps, and the bounded integrand is
Riemann integrable; values at the jump ranks do not affect the limit. Each
exceptional edge has weight at most `n`, so its contribution after division
by `n^2` is `O(1/n)`. Uniformly across both parities,

```text
(1/n^2) sum_{Supnick edges (a,b)} sqrt(ab)
  -> 2 integral_0^(L/2) sqrt(Q_A(t)Q_A(L-t)) dt.         (9)
```

For completeness, (9) determines the implicit chain-root scale rather than
assuming it. Fix `r_0>0`, take `r>=r_0`, and set `R=rn^2`. Since all retained
radii lie in `[alpha n,n]`, the same rationalization and arcsine estimate as
in the terminal-interval proof gives, uniformly in every edge and `r>=r_0`,

```text
theta_{rn^2}(a,b)=2 sqrt(ab)/(rn^2)+O_{r_0}(n^-2).      (10)
```

There are at most `n` edges, so (9)-(10) imply the parity-uniform closure
limit

```text
C_chain(rn^2)
  -> (4/r) integral_0^(L/2)
                 sqrt(Q_A(t)Q_A(L-t)) dt.              (11)
```

Bracketing the unique decreasing closure root on the two sides of (3), as in
the proof of the terminal theorem, proves (3). The deletion lemma and the
arbitrary-radii Supnick theorem then give (4). No full feasibility of the
formal Supnick chain is used.

For the unperforated interval `A_0=[alpha,1]`,

```text
Q_0(t)=alpha+t,       L_0=1-alpha,
```

and (3) becomes

```text
C(A_0)=(2/pi) integral_alpha^m sqrt(y(s-y))dy=C_term,   (12)
```

which is the `lambda_*` case of the existing terminal theorem after scaling
by `n` rather than its lower endpoint.

## 3. Exact one-gap reindexing

Set

```text
f_S(y)=sqrt(y(S-y)),       J_epsilon(x)=pi C_epsilon(x)/2.
```

The median here is the median by retained rank, not the geometric midpoint of
each component. The quantile pairing in (3) gives three exact cases.

### 3.1 Gap below the old median

If `alpha<x<m`, then the retained lower half ends at `m+epsilon/2`.
Before the gap, a lower point `y` remains paired with `s-y`; after the gap,
the reindexing pairs it with `s+epsilon-y`. Hence

```text
J_epsilon(x)
 = integral_alpha^(x-epsilon/2) f_s(y)dy
   + integral_(x+epsilon/2)^(m+epsilon/2)
         f_(s+epsilon)(y)dy.                            (13)
```

Both appearances of the deleted boundary matter: omitting either one loses
half of the direct removal term.

### 3.2 Gap at the old median

If `x=m`, every surviving lower point keeps its old partner and the paired
domain simply shortens:

```text
J_epsilon(m)
 = integral_alpha^(m-epsilon/2) f_s(y)dy.               (14)
```

### 3.3 Gap above the old median

If `m<x<1`, put `p=s-x`, which lies in `(alpha,m)`. The retained lower half
ends at `m-epsilon/2`. Its first part keeps pair sum `s`, while its second
part is reindexed to pair sum `s-epsilon`:

```text
J_epsilon(x)
 = integral_alpha^(p-epsilon/2) f_s(y)dy
   + integral_(p-epsilon/2)^(m-epsilon/2)
         f_(s-epsilon)(y)dy.                            (15)
```

Equations (13)-(15) also show why the below- and above-median calculations
look different before simplification. They encode the two exact directions
of the rank shift.

## 4. First variation and unification of the three cases

For `0<y<s`,

```text
partial f_s(y)/partial s = y/(2 f_s(y)),
f_s(m)=m=s/2.                                          (16)
```

Differentiating (13) at `epsilon=0+` gives

```text
J'_0(x)
 =-f_s(x)+m/2+(1/2) integral_x^m sqrt(y/(s-y))dy,
                                                    alpha<x<m.  (17)
```

Differentiating (15), with cancellation of the two moving terms at `p`,
gives

```text
J'_0(x)
 =-m/2-(1/2) integral_p^m sqrt(y/(s-y))dy,
                                                    m<x<1.      (18)
```

Equation (14) gives `J'_0(m)=-m/2`.

Let

```text
theta=asin sqrt(x/s),       f_s(x)=s sin(theta)cos(theta).
```

The elementary primitive

```text
integral sqrt(y/(s-y))dy
  =s asin sqrt(y/s)-sqrt(y(s-y))                       (19)
```

reduces (17) to

```text
J'_0(x)
 =(s/2)[pi/4-theta-sin(theta)cos(theta)].               (20)
```

For (18), `p=s-x` has angle `pi/2-theta`; substitution in (19) gives the
same expression. At `x=m`, `theta=pi/4` and (20) equals `-s/4=-m/2`, so
(20) holds for all `x in (alpha,1)`. Since `C=2J/pi`, (20) is exactly (5).

## 5. Rigorous sign at the optimized endpoint

Define

```text
Phi(theta)=pi/4-theta-sin(theta)cos(theta),
                    0<theta<pi/2.                      (21)
```

Then

```text
Phi'(theta)=-1-cos(2theta)=-2 cos(theta)^2<0.           (22)
```

It remains to locate the angle corresponding to the lower terminal endpoint.
Using `q=sin(tau)` and the half-angle identity,

```text
alpha/s=(1-q)/2=sin^2(pi/4-tau/2).
```

Therefore

```text
theta_alpha=asin sqrt(alpha/s)=pi/4-tau/2              (23)
```

and the defining equation `tau=cos(tau)` gives

```text
Phi(theta_alpha)
 =tau/2-(1/2)sin(pi/2-tau)
 =(tau-cos(tau))/2=0.                                  (24)
```

Every interior center has `x>alpha`, hence `theta>theta_alpha`. Strict
decrease (22) now proves `Phi(theta)<0`, and (5) proves (6). This is an exact
sign argument; no decimal approximation to `tau`, `alpha`, or `x` enters it.

## 6. Order of limits and lower-bound interpretation

The proof uses the iterated order required by an induced-subset asymptotic:

1. Fix `x in (alpha,1)` and a positive `epsilon` satisfying (1).
2. Let `n->infinity` in (2). The deleted set has
   `epsilon n+O(1)` radii; parity, endpoint rounding, the seam, and the even
   central edge contribute only `O(1/n)` after normalization.
3. Obtain the genuine single-subset lower bound (4) with coefficient
   `C_epsilon(x)`.
4. Only then let `epsilon->0+` and differentiate the continuum functional.

Thus the first variation is

```text
lim_(epsilon->0+) lim_(n->infinity)
 [R_chain(Supnick(S_n(epsilon,x)))/n^2-C_term]/epsilon
 =V(x)<0.                                               (25)
```

The two limits are not interchanged. If `epsilon` is sent to zero first at
fixed `n`, the band eventually contains no integer radius. If a diagonal
`epsilon=epsilon_n` has bounded `n epsilon_n`, parity and rounding need not
disappear before division by `epsilon_n`. No diagonal or uniform-in-`x`
statement is needed for, or asserted by, the first-order local result.

Because `V(x)<0`, the definition of the one-sided derivative supplies, for
each fixed interior `x`, an `epsilon_0(x)>0` such that

```text
C_epsilon(x)<C_term,       0<epsilon<epsilon_0(x).       (26)
```

Therefore this perturbation family produces no one-gap induced-subset lower
bound strictly exceeding `C_term`. The conclusion concerns the strength of a
single Supnick chain lower bound only. It does not optimize multiple gaps or
combined subsets, determine the true leading asymptotics, give an upper
bound, change any floating-circle claim, or extend finite certification.

## 7. Independent checks and epistemic limits

The task-local symbolic checker independently verifies the two parity edge
counts, the primitive (19), the below/above-median derivative reductions, the
common formula (20), and the optimized-endpoint identity (24). A separate
finite diagnostic constructs the Supnick tour by ranks, compares its edge
set with (7)-(8), and checks convergence toward (3) on gaps below, at, and
above the median with both retained-set parities.

These checks are corroborative. The proof is the rank formulas, Riemann-sum
limit, uniform angular/root bracket, exact reindexing identities, and strict
sign argument above. The published arbitrary-radii Supnick theorem is
imported rather than reproved. The arXiv-v1 source, result artifacts,
`verify.py`, and the certified finite range `3<=n<=14` are unchanged.
