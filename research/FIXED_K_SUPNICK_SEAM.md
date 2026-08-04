# Fixed-radius Supnick seam theorem

```text
status=PROVED
domain=integers k >= 1 and n >= k+2
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

Fix an integer `k >= 1`. For every integer `n >= k+2`, let
`sigma*_{k,n}` be the canonical chain-minimizing Supnick cyclic order on
the consecutive radii `{k,...,n}`, and put

```text
R_{k,n} = R_chain(sigma*_{k,n}).
```

Define the radius-`k` seam deficit

```text
Delta_{k,n}
  = theta_{R_{k,n}}(n,k) + theta_{R_{k,n}}(k,n-1)
    - theta_{R_{k,n}}(n,n-1).
```

This note proves the following exact fixed-`k` theorem.

1. The two cyclic neighbors of `k` in `sigma*_{k,n}` are `n-1` and `n`.
2. `R_{k,n}` exists uniquely, is strictly increasing in `n`, and tends to
   infinity.
3. `Delta_{k,n}>0` throughout the exact no-threshold range
   `k+2 <= n <= 4k`.
4. For `n>=4k+1`, the physical Descartes threshold is

   ```text
   kappa_{k,n}
     = 1/k + 1/n + 1/(n-1)
       - 2 sqrt((2n+k-1)/(k n(n-1))),

   T_{k,n} = 1/kappa_{k,n}.
   ```

   It satisfies

   ```text
   Delta_{k,n} < 0  iff  R_{k,n} > T_{k,n},
   Delta_{k,n} = 0  iff  R_{k,n} = T_{k,n},
   Delta_{k,n} > 0  iff  R_{k,n} < T_{k,n}.
   ```

   The thresholds `T_{k,n}` strictly decrease with `n` and tend to `k`.
5. A strict seam obstruction occurs for all sufficiently large `n`. Once it
   occurs, it persists for every larger `n`; equality can occur for at most
   one integer.

Equivalently, there is a finite first strict-obstruction index

```text
s_k = min {n >= k+2 : Delta_{k,n} < 0} >= 4k+1.
```

Then `Delta_{k,n}<0` for every `n>=s_k`; all earlier deficits are positive
except that `Delta_{k,s_k-1}=0` is possible. The theorem proves existence and
persistence, not a closed formula for `s_k`.

This is an exact theorem about one formal chain and its seam
`(n,k,n-1)`. A negative deficit proves that this chain is unrealizable across
that seam. A nonnegative deficit does not prove full realizability. Nothing
here determines `R*(n)`, proves that radius `k` floats in a global optimum, or
classifies any global contact graph. In particular, this note does not
classify the exact radius-3 onset. The result is post-arXiv-v1 work; the
historical paper remains unchanged.

## 1. Canonical shifted Supnick order

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

The paper proves that this cost is symmetric, strictly decreasing in `R`,
strictly increasing in either surrounding radius, and strictly anti-Monge
when the radii index the matrix in increasing order. Supnick's theorem
therefore supplies a fixed cyclic order minimizing the adjacent-angle sum at
every `R`. The result applies to arbitrary distinct increasing radii, not
only to a set beginning at `1`.

Here is a parity-independent representative for `{k,...,n}`. Put

```text
N = n-k+1,
h = ceil(N/2).
```

Construct two lists of ranks `A_N` and `B_N`, with `j=0,1,2,...`:

- append `1+2j` to `A_N` when `1+2j<=h`, then append `N-1-2j`
  when `N-1-2j>h`;
- append `2+2j` to `B_N` when `2+2j<=h`, then append `N-2-2j`
  when `N-2-2j>h`;
- stop each construction after a value of `j` appends nothing.

Let

```text
tau_N = A_N followed by reverse(B_N) followed by N,
sigma*_{k,n} = (k+i-1 : i occurs in tau_N).
```

The low entries of `A_N,B_N` partition the ranks `1,...,h` by parity; the
high entries partition `h+1,...,N-1` by the complementary parities; the last
rank is `N`. Thus every radius occurs exactly once. This is the standard
Supnick maximum tour for `-theta`, shifted by `k-1`, so it minimizes the sum
of `theta` and hence is chain-optimal.

For `N=3`, the representative is `(k,n-1,n)`. For `N>=4`, `A_N` begins
with `(1,N-1)`, so `sigma*_{k,n}` begins with `(k,n-1)`; it always ends with
`n`. Consequently the cyclic neighbors of `k` are exactly `n-1` and `n`.

For reference, direct reading of the shifted rank tour gives the following
undirected edge sets. If `N=2h`,

```text
E_{k,n}
  = {(k,n), (k+h-1,k+h)}
    union {(i,n+k-1-i) : k <= i <= k+h-2}
    union {(i,n+k+1-i) : k+1 <= i <= k+h-1}.
```

If `N=2h+1`,

```text
E_{k,n}
  = {(k,n)}
    union {(i,n+k-1-i) : k <= i <= k+h-1}
    union {(i,n+k+1-i) : k+1 <= i <= k+h}.
```

These are precisely the rank formulas for the unshifted tour with every
endpoint translated by `k-1`; each contains `N` distinct edges and includes
both seam edges `(k,n-1)` and `(k,n)`.

## 2. The implicit chain root

Let `C_{k,n}(R)` be the sum of `theta_R` over `E_{k,n}`. Explicitly, when
`N=2h`,

```text
C_{k,n}(R)
  = theta_R(k,n) + theta_R(k+h-1,k+h)
    + sum_{i=k}^{k+h-2} theta_R(i,n+k-1-i)
    + sum_{i=k+1}^{k+h-1} theta_R(i,n+k+1-i),
```

and when `N=2h+1`,

```text
C_{k,n}(R)
  = theta_R(k,n)
    + sum_{i=k}^{k+h-1} theta_R(i,n+k-1-i)
    + sum_{i=k+1}^{k+h} theta_R(i,n+k+1-i).
```

The root `R_{k,n}` is defined without an order ellipsis by

```text
C_{k,n}(R_{k,n}) = 2 pi.                                (1)
```

Every summand is continuous and strictly decreasing in `R`, while

```text
lim_{R->0+} C_{k,n}(R) = N pi > 2 pi,
lim_{R->infinity} C_{k,n}(R) = 0.
```

Hence (1) has exactly one positive solution.

### Lemma 1: strict growth in `n`

Fix `R>0`. In a fixed-`R` minimizing cycle on `{k,...,n+1}`, let `a,b<=n`
be the neighbors of `n+1`. Delete `n+1` and join `a` to `b`. The cost drops
strictly because

```text
theta_R(a,n+1) + theta_R(n+1,b) > theta_R(a,b):
```

the first term alone is greater than `theta_R(a,b)` by strict increase in
its second radius, and the other removed term is positive. The induced cycle
on `{k,...,n}` need not be the displayed Supnick representative, but its
cost is at least the fixed-`R` minimum `C_{k,n}(R)`. Therefore

```text
C_{k,n+1}(R) > C_{k,n}(R)       for every R>0.           (2)
```

Evaluating (2) at the two roots and using strict decrease in `R` gives

```text
R_{k,n+1} > R_{k,n}.                                    (3)
```

No claim that vertex deletion preserves the canonical tour is used.

### Lemma 2: divergence

Every endpoint of every edge is at least `k`, so monotonicity in the radii
and (1) give

```text
2 pi = C_{k,n}(R_{k,n})
     >= 2N asin(k/(R_{k,n}+k)).
```

Because `N>=3`, inversion on the increasing branch of `asin` yields the
explicit lower bound

```text
R_{k,n} >= k(csc(pi/N)-1) >= k(N/pi-1).                 (4)
```

The last inequality uses `sin x<=x`. Since `N=n-k+1` tends to infinity for
fixed `k`, (4) proves

```text
R_{k,n} -> infinity.                                    (5)
```

This is only a chain-root bound; it assumes no conjectural asymptotic formula
for the global problem.

## 3. Exact Descartes equivalence

Put `x=1/R` and abbreviate

```text
alpha_n = 1/n + 1/(n-1),
beta_n  = 1/(n(n-1)).
```

When the central circle and circles `n,n-1` are mutually tangent, the
bounded Descartes pocket between them has curvature

```text
P_n(x) = x + alpha_n + 2 sqrt(alpha_n x + beta_n).       (6)
```

The plus sign is the bounded Soddy-circle branch. If its radius is
`rho=1/P_n(x)`, exact tangency gives

```text
theta_R(n,rho) + theta_R(rho,n-1) = theta_R(n,n-1).
```

Both angles on the left increase strictly with the inserted radius. Comparing
`rho` with `k` therefore gives the exact sign identity, for every `R>0`,

```text
sign(theta_R(n,k) + theta_R(k,n-1) - theta_R(n,n-1))
  = sign(P_n(1/R) - 1/k).                               (7)
```

In particular, (7) applies at `R=R_{k,n}`. The function `P_n` is continuous,
strictly increasing in `x>=0`, and tends to infinity with `x`.

## 4. Exact threshold domain and formula

At `x=0`,

```text
P_n(0)
  = alpha_n + 2 sqrt(beta_n)
  = (1/sqrt(n) + 1/sqrt(n-1))^2,                        (8)
```

which strictly decreases with `n`. At the adjacent boundary integers,

```text
P_{4k}(0)
  > (1/(2 sqrt(k)) + 1/(2 sqrt(k)))^2 = 1/k,

P_{4k+1}(0)
  < (1/(2 sqrt(k)) + 1/(2 sqrt(k)))^2 = 1/k.            (9)
```

For the first inequality, `1/sqrt(4k-1)>1/sqrt(4k)`; for the second,
`1/sqrt(4k+1)<1/sqrt(4k)`. Equations (8)-(9), strict decrease in `n`, and
strict increase in `x` prove:

- when `k+2<=n<=4k`, `P_n(x)>1/k` for every `x>0`, so (7) gives
  `Delta_{k,n}>0`;
- a unique positive solution of `P_n(x)=1/k` exists exactly when
  `n>=4k+1`.

It remains to solve that crossing without accepting an extraneous squared
root. Write

```text
c = 1/k,
q_{k,n} = sqrt(alpha_n/k + beta_n)
          = sqrt((2n+k-1)/(k n(n-1))).
```

The two algebraic roots after squaring are

```text
c + alpha_n - 2 q_{k,n},
c + alpha_n + 2 q_{k,n}.
```

In the physical domain, `P_n(0)<c`, and hence

```text
q_{k,n}^2-alpha_n^2
  = alpha_n(c-alpha_n)+beta_n > 0.
```

Thus `q_{k,n}>alpha_n`. Define the minus root

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))).                      (10)
```

It satisfies

```text
alpha_n kappa_{k,n} + beta_n
  = (q_{k,n}-alpha_n)^2.
```

The square root in (6) is therefore `q_{k,n}-alpha_n`, not its negative,
and direct substitution gives `P_n(kappa_{k,n})=c`. The unsquared equation
requires `c-alpha_n-x>=0`, whereas at the plus root

```text
c-alpha_n-x = -2(alpha_n+q_{k,n}) < 0.
```

Thus the plus root is extraneous.

For an exact sign check valid across the whole original domain, rationalizing
(10) gives

```text
kappa_{k,n}(c+alpha_n+2q_{k,n})
  = (c-P_n(0))(c-alpha_n+2sqrt(beta_n)).                 (11)
```

The second factor on the right is positive because

```text
alpha_n-2sqrt(beta_n)
  = (1/sqrt(n-1)-1/sqrt(n))^2
  < 1/(n-1) < 1/k.
```

Thus `kappa_{k,n}>0` exactly for `n>=4k+1`, in agreement with the geometric
domain; the minus root is negative before that domain. Define

```text
T_{k,n} = 1/kappa_{k,n}       for n>=4k+1.              (12)
```

Strict increase of `P_n` and (7) now give

```text
Delta_{k,n} < 0  iff  1/R_{k,n} < kappa_{k,n}
                     iff  R_{k,n} > T_{k,n},

Delta_{k,n} = 0  iff  R_{k,n} = T_{k,n},
Delta_{k,n} > 0  iff  R_{k,n} < T_{k,n}.                (13)
```

## 5. Decreasing thresholds and the terminal obstruction tail

For each fixed `x>=0`, both `alpha_n` and `beta_n` strictly decrease with
`n`, so

```text
P_{n+1}(x) < P_n(x).                                    (14)
```

At `x=kappa_{k,n}`, equation (14) gives
`P_{n+1}(kappa_{k,n})<1/k`. Since `P_{n+1}` is strictly increasing and
reaches `1/k` at its unique positive root,

```text
kappa_{k,n+1} > kappa_{k,n},
T_{k,n+1} < T_{k,n}              for n>=4k+1.           (15)
```

The explicit formula also gives

```text
kappa_{k,n} -> 1/k,
T_{k,n} -> k.                                           (16)
```

On the positive-threshold domain set

```text
D_{k,n} = R_{k,n} - T_{k,n}.
```

Equations (3) and (15) show

```text
D_{k,n+1}-D_{k,n}
  = (R_{k,n+1}-R_{k,n}) + (T_{k,n}-T_{k,n+1}) > 0.      (17)
```

By (5) and (16), `D_{k,n}->infinity`. Therefore `D_{k,n}=0` can occur for
at most one integer, `D_{k,n}>0` eventually, and once it is positive it
stays positive. Criterion (13) proves the claimed existence, uniqueness of
any equality, and persistence of the seam obstruction. More precisely, the
finite index `s_k` defined in the result section exists; equality, if it
occurs, is exactly at `s_k-1`.

Notice that the raw values `Delta_{k,n}` need not form a monotone numerical
sequence. The proof uses the strictly increasing comparison quantity
`D_{k,n}`, not monotonicity of the angular deficit itself.

## 6. The existing radius-1 and radius-2 theorems as corollaries

For `k=1`, formula (10) becomes

```text
kappa_{1,n}
  = 1 + 1/n + 1/(n-1) - 2 sqrt(2/(n-1)),
```

and the general physical domain begins at `n=5`. The existing exact proof in
`research/RADIUS1_SEAM_OBSTRUCTION.md` supplies the two bridges

```text
R_{1,7} < 6 < T_{1,7},
T_{1,8} < 51/10 < R_{1,8}.
```

Together with (13), (17), and the no-threshold cases `n=3,4`, these recover

```text
Delta_{1,n} > 0  for 3<=n<=7,
Delta_{1,n} < 0  for every n>=8.
```

For `k=2`, formula (10) becomes

```text
kappa_{2,n}
  = 1/2 + 1/n + 1/(n-1)
    - 2 sqrt((2n+1)/(2n(n-1))),
```

and the physical domain begins at `n=9`. The exact bridges in
`research/RADIUS2_SEAM_THRESHOLD.md` are

```text
R_{2,12} < 17 < T_{2,12},
T_{2,13} < 14 < R_{2,13}.
```

They recover

```text
Delta_{2,n} > 0  for 4<=n<=12,
Delta_{2,n} < 0  for every n>=13.
```

The endpoint arithmetic stays authoritative in those two proof notes and is
not duplicated here. For `k=3`, the present theorem proves the exact
no-threshold range and eventual persistence but intentionally does not
identify `s_3` or classify its proposed exact onset.

## 7. Excluded routes and diagnostic checker

The proof was checked against the following scope and logic failures.

1. **A finite scan is not the all-`n` proof.** The proof is the exact
   Descartes reduction, the two opposing monotonicities, and divergence of
   the chain roots.
2. **Raw-deficit monotonicity is not assumed.** The radius-1 and radius-2
   notes already record counterexamples to that stronger statement.
3. **Deleting a vertex need not preserve the canonical order.** Lemma 1
   uses only fixed-`R` minimality of the induced valid cycle.
4. **The algebraic root is not automatically physical.** The exact domain,
   positive square-root branch, and extraneous plus root are handled before
   taking a reciprocal.
5. **The theorem stops at one formal seam.** A positive deficit does not
   check other nonadjacent pairs; a negative deficit neither constructs a
   replacement nor says what happens in global optima.
6. **No exact radius-3 onset is claimed.** Its finite endpoint bridge remains
   a separate task.

The task-local script

```text
ops/TASK-20260804__fixed_k_supnick_seam/check_seam.py
```

imports no production package. It checks the shifted order in two independent
ways, verifies both parity edge formulas, audits the threshold algebra and
the exact `4k,4k+1` domain boundary with rational arithmetic, and performs a
finite high-precision diagnostic scan at two precisions. Its output is
explicitly diagnostic and does not certify an exact onset for `k>=3`.
