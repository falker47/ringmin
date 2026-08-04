# Radius-1 seam obstruction in the Supnick chain

```text
status=PROVED
domain=integers n >= 3
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For each integer `n >= 3`, let `sigma_n*` be the chain-minimizing Supnick cyclic order on the radii `{1,...,n}` and let

```text
R_n = R_chain(sigma_n*).
```

Define the radius-1 seam deficit

```text
Delta_n = theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
          - theta_{R_n}(n,n-1).
```

This note proves the exact threshold

```text
Delta_n > 0  for 3 <= n <= 7,
Delta_n < 0  for every n >= 8.
```

In particular, the Priority 1 statement is proved for every integer `n >= 8`.

This is an exact theorem about the formal full Supnick chain and the single seam `(n,1,n-1)`. It does **not** identify `R*(n)`, prove that circle `1` floats in any or every global optimum, determine another contact structure, or prove any later level of the floating cascade.

The public arXiv-v1 paper reported the finite transition and explicitly left the all-`n` extension conjectural in Proposition `break1` and its open problems. The new proof below is post-v1 work; the historical paper source is not modified.

## 1. Definitions and the exact Supnick convention

For `R,a,b > 0`, write

```text
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

It is symmetric, positive, strictly decreasing in `R`, and strictly increasing in either surrounding radius.

The displayed Supnick order in the paper contains an ellipsis, so fix the following parity-independent representative. Let `h = ceil(n/2)`. Build two lists `A_n` and `B_n` as follows, with `j = 0,1,2,...`:

- append `1+2j` to `A_n` when `1+2j <= h`, then append `n-1-2j` when `n-1-2j > h`;
- append `2+2j` to `B_n` when `2+2j <= h`, then append `n-2-2j` when `n-2-2j > h`;
- stop each construction after a value of `j` appends nothing.

Then define

```text
sigma_n* = A_n followed by reverse(B_n) followed by n.
```

The low entries of `A_n,B_n` partition `{1,...,h}` by parity, and their high entries partition `{h+1,...,n-1}` by the complementary parities, so every value `1,...,n` occurs exactly once. This is the representative emitted by the repository's `supnick_max_tour`; `interleave` emits a cyclically equivalent rotation. The name `max` refers to maximizing the TSP on `-theta`, hence minimizing the sum of `theta` values.

For `n >= 4`, `A_n` begins with `(1,n-1)` and `B_n` begins with `2`. Therefore `sigma_n*` begins with `(1,n-1)` and ends with `(2,n)`. Its two cyclic neighbors of `1` are exactly `n-1` and `n`. The threshold representatives are

```text
sigma_7* = (1,6,3,4,5,2,7),
sigma_8* = (1,7,3,5,4,6,2,8).
```

Directly reading the adjacent undirected edges gives a useful parity-explicit form. For `n=2m`,

```text
E_{2m} = {(1,2m), (m,m+1)}
         union {(j,2m-j) : 1 <= j <= m-1}
         union {(j,2m+2-j) : 2 <= j <= m}.
```

For `n=2m+1`,

```text
E_{2m+1} = {(1,2m+1)}
           union {(j,2m+1-j) : 1 <= j <= m}
           union {(j,2m+3-j) : 2 <= j <= m+1}.
```

The two formulas contain exactly `n` distinct edges and include `(1,n)` and `(1,n-1)`.

## 2. The implicit chain root

Let `C_n(R)` be the adjacent-angle sum of `sigma_n*`. The preceding edge sets give the explicit finite sums

```text
C_{2m}(R)
  = theta_R(1,2m) + theta_R(m,m+1)
    + sum_{j=1}^{m-1} theta_R(j,2m-j)
    + sum_{j=2}^{m} theta_R(j,2m+2-j),

C_{2m+1}(R)
  = theta_R(1,2m+1)
    + sum_{j=1}^{m} theta_R(j,2m+1-j)
    + sum_{j=2}^{m+1} theta_R(j,2m+3-j).
```

Thus the dependence of `R_n` on `n` is fixed implicitly and without an order ellipsis by

```text
C_n(R_n) = 2 pi.
```

Every summand is continuous and strictly decreasing in `R`; moreover `C_n(R)` tends to `n*pi > 2*pi` as `R` tends to zero from above and to zero as `R` tends to infinity. Hence the root exists and is unique.

Supnick's theorem and the anti-Monge result in the paper also say that, for each fixed `R`, `C_n(R)` is the minimum adjacent-angle sum over every cyclic order on `{1,...,n}`. That fixed-`R` minimum is the only optimality fact used below.

## 3. An explicit seam threshold

Put `x=1/R` and abbreviate

```text
alpha_n = 1/n + 1/(n-1),
beta_n = 1/(n(n-1)).
```

When the central circle and the circles `n,n-1` are mutually tangent, the bounded Descartes pocket between them has curvature

```text
P_n(x) = x + alpha_n + 2 sqrt(alpha_n*x + beta_n).
```

The plus sign is the bounded Soddy-circle branch. By the exact angular/pocket equivalence already proved in the paper, a unit circle fits strictly inside the angular gap between `n` and `n-1` precisely when `P_n(x) < 1`. Equivalently,

```text
theta_R(n,1) + theta_R(1,n-1) < theta_R(n,n-1)
    iff P_n(1/R) < 1.                                      (1)
```

The function `P_n` is strictly increasing in `x`. Define

```text
kappa_n = 1 + 1/n + 1/(n-1) - 2 sqrt(2/(n-1)).
```

Since

```text
alpha_n + beta_n = 2/(n-1),
```

substitution gives `P_n(kappa_n)=1`: if `q=sqrt(alpha_n+beta_n)`, then

```text
alpha_n*kappa_n + beta_n = (q-alpha_n)^2
```

and the positive root is `q-alpha_n` in the relevant range. Indeed, for every `n>=4`,

```text
alpha_n < 2/(n-1) < sqrt(2/(n-1)) = q.
```

The other algebraic root produced by squaring violates the sign condition in the unsquared equation and is not the bounded-pocket crossing.

Whenever `kappa_n>0`, define

```text
T_n = 1/kappa_n.
```

Section 5 proves positivity at `n=8` and hence throughout the target range; Section 6 also checks it from `n=5` for the lower-side classification. Strict monotonicity of `P_n`, together with (1), yields the exact sign criterion whenever `T_n` is defined:

```text
Delta_n < 0  iff  R_n > T_n,
Delta_n = 0  iff  R_n = T_n,
Delta_n > 0  iff  R_n < T_n.                               (2)
```

## 4. The two opposing monotonicities

### Lemma 1: `R_n` is strictly increasing

Fix `R>0`. In the fixed-`R` minimizing tour on `{1,...,n+1}`, let `a,b <= n` be the neighbors of `n+1`. Delete `n+1` and join `a` directly to `b`. The cost falls strictly, because

```text
theta_R(a,n+1) + theta_R(n+1,b) > theta_R(a,b):
```

indeed `theta_R(a,n+1) > theta_R(a,b)` since `n+1>b`, and the other removed angle is positive. The resulting tour on `{1,...,n}` need not be `sigma_n*`, but its cost is at least the fixed-`R` minimum `C_n(R)`. Consequently

```text
C_{n+1}(R) > C_n(R)        for every R>0.                  (3)
```

At `R=R_{n+1}`, equation (3) gives `C_n(R_{n+1})<2*pi`. Since `C_n` is strictly decreasing and equals `2*pi` at `R_n`,

```text
R_{n+1} > R_n.                                             (4)
```

No identification of the induced tour with `sigma_n*` is made or needed; that identification is generally false.

### Lemma 2: `T_n` is strictly decreasing where it is defined

Write `t=n-1` and extend the reciprocal threshold to a real variable:

```text
kappa(t) = 1 + 1/t + 1/(t+1) - 2 sqrt(2/t).
```

For `t>2`,

```text
kappa'(t)
  = -1/t^2 - 1/(t+1)^2 + sqrt(2)/t^(3/2)
  > -2/t^2 + sqrt(2)/t^(3/2)
  > 0.
```

The last inequality is equivalent to `t>2`. Thus `kappa_n` is strictly increasing for the integer range of interest, and its reciprocal `T_n` is strictly decreasing wherever `kappa_n>0`.

## 5. Exact threshold bounds at `n=7,8`

Only rational square comparisons and the classical strict bounds `3<pi<22/7` are used here. For completeness, `pi>3` follows from the regular hexagon inscribed in the unit circle, while

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

### The obstructed side: `T_8 < 51/10 < R_8`

First,

```text
kappa_8 = 71/56 - 2 sqrt(2/7) > 10/51.
```

Indeed

```text
71/56 - 10/51 = 3061/2856 > sqrt(8/7),
(3061/2856)^2 - 8/7 = 47737/8156736 > 0.
```

Therefore `T_8<51/10`.

At the rational radius `R=51/10`, for each edge `e=(a,b)` of `sigma_8*`, put

```text
s_e^2 = ab / ((R+a)(R+b)).
```

The following exact rational checks give `s_e>q_e`.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(1,8)` | `800/7991` | `79/250` | `128169/499437500` |
| `(4,5)` | `2000/9191` | `233/500` | `1029801/2297750000` |
| `(1,7)` | `700/7381` | `307/1000` | `4348131/7381000000` |
| `(2,6)` | `400/2627` | `39/100` | `4333/26270000` |
| `(3,5)` | `500/2727` | `107/250` | `28577/170437500` |
| `(2,8)` | `1600/9301` | `207/500` | `1461451/2325250000` |
| `(3,7)` | `700/3267` | `231/500` | `669613/816750000` |
| `(4,6)` | `800/3367` | `487/1000` | `1451977/3367000000` |

Their lower bounds sum to

```text
sum_e q_e = 327/100 > 22/7 > pi.
```

Since `asin(s)>s` for `s>0`,

```text
C_8(51/10) = 2 sum_e asin(s_e)
             > 2 sum_e q_e
             > 2 pi.
```

The strict decrease of `C_8` now gives `R_8>51/10>T_8`.

### The unobstructed side: `R_7 < 6 < T_7`

Here

```text
kappa_7 = 55/42 - 2/sqrt(3).
```

It is positive because

```text
(55/42)^2 - 4/3 = 673/1764 > 0,
```

and it is less than `1/6` because `8/7<2/sqrt(3)`, whose squared comparison is `192<196`. Hence `T_7>6`.

At `R=6`, use the following exact upper bounds `s_e<q_e<1/2` for the edges of `sigma_7*`.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(1,7)` | `1/13` | `7/25` | `12/8125` |
| `(1,6)` | `1/14` | `27/100` | `103/70000` |
| `(2,5)` | `5/44` | `17/50` | `27/13750` |
| `(3,4)` | `2/15` | `37/100` | `107/30000` |
| `(2,7)` | `7/52` | `37/100` | `297/130000` |
| `(3,6)` | `1/6` | `41/100` | `43/30000` |
| `(4,5)` | `2/11` | `43/100` | `339/110000` |

For `0<s<1/2`,

```text
asin(s) = integral_0^s du/sqrt(1-u^2)
        < s/sqrt(1-s^2)
        < (2/sqrt(3))s
        < (6/5)s.
```

The last strict comparison follows by squaring `2/sqrt(3)<6/5`, which reduces to `100<108`.

Because `sum_e q_e=247/100`,

```text
C_7(6) < (12/5)(247/100) = 741/125 < 6 < 2 pi.
```

Thus `R_7<6<T_7`.

## 6. Uniform conclusion and the lower side

For every `n>=8`, equations (4), Lemma 2, and the exact `n=8` bridge give

```text
R_n >= R_8 > T_8 >= T_n.
```

The sign criterion (2) proves

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

for every integer `n>=8`.

The same comparisons certify the other side of the threshold. One has

```text
kappa_5 = 29/20 - sqrt(2) > 0
```

by squaring (`841>800`), so `T_n` exists and decreases for `5<=n<=7`. Hence

```text
R_n <= R_7 < T_7 <= T_n,
```

and `Delta_n>0` for `5<=n<=7`. For `n=3,4`, already the limiting pocket curvatures satisfy

```text
P_3(0) = 5/6 + 2/sqrt(6) > 1,
P_4(0) = 7/12 + 1/sqrt(3) > 1.
```

The two strict comparisons reduce respectively to `2/3>1/36` and `1/3>25/144` after moving the rational term and squaring positive quantities.

Since `P_n(x)` increases with `x>0`, `Delta_n>0` there as well. This completes the exact `3..7` versus `8..infinity` classification.

## 7. Counterexample search and excluded routes

The proof was checked against the following failure modes.

1. **Raw-deficit monotonicity is false.** A production-independent high-precision scan gives

   ```text
   Delta_19 = -0.291721956355170...
   Delta_20 = -0.291070673718319...
   ```

   Thus the deficit stops decreasing at this point. The proof compares the increasing roots `R_n` with the decreasing thresholds `T_n`; it never assumes that `Delta_n` is monotone.

2. **Deleting a vertex does not preserve the canonical tour.** Deleting `n+1` from `sigma_{n+1}*` is generally not dihedrally equivalent to `sigma_n*`. Lemma 1 uses only that the induced order is a valid `n`-tour whose cost is bounded below by `C_n(R)`.

3. **A finite scan is not the proof.** High-precision calculations are diagnostic only. The all-`n` step is the exact opposing-monotonicity argument plus the rational `n=8` bridge.

4. **Large-`n` asymptotics are unnecessary and unavailable as a premise.** No conjectural estimate for `R*(n)`, no asymptotic formula for `R_n`, and no assumption on a floating set enters the proof.

5. **The quantifiers stop at this seam.** Failure of this formal necklace across `(n,1,n-1)` neither supplies a feasible replacement nor determines what happens in all globally optimal placements.

## 8. Independent diagnostic checker

The task-local script

```text
ops/TASK-20260804__radius1_seam_obstruction/check_seam.py
```

reimplements the order, closure root, threshold, and seam deficit without importing `ringmin`. It checks the rational `n=7,8` inequalities exactly with `fractions.Fraction`, compares two independently written cyclic-order constructors, scans a user-selected finite range in `mpmath`, and repeats the scan at higher precision. Its finite output corroborates the proof and exposes the `n=19,20` monotonicity failure; it is not an all-`n` certificate.
