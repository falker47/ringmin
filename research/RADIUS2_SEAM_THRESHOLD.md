# Radius-2 seam threshold in the shifted Supnick chain

```text
status=PROVED
domain=integers n >= 4
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For each integer `n >= 4`, let `sigma*_{2,n}` be the chain-minimizing
Supnick cyclic order on the radii `{2,...,n}` and let

```text
R_{2,n} = R_chain(sigma*_{2,n}).
```

Define

```text
Delta_{2,n} = theta_{R_{2,n}}(n,2)
              + theta_{R_{2,n}}(2,n-1)
              - theta_{R_{2,n}}(n,n-1).
```

This note proves the proposed exact classification:

```text
Delta_{2,n} > 0  for 4 <= n <= 12,
Delta_{2,n} < 0  for every n >= 13.
```

Thus the formal shifted Supnick necklace has an exact radius-2 seam
obstruction from `n=13` onward.

This is an exact theorem about one formal chain and the seam `(n,2,n-1)`.
It does **not** determine `R*(n)`, prove that circle `2` floats in any or
every global optimum, classify another contact graph, or establish a general
radius-`k` cascade. The finite `n=13` observation appears in arXiv v1; the
all-`n` proof is post-v1 work, and the historical paper is not modified.

## 1. Exact shifted Supnick convention

For `R,a,b > 0`, write

```text
theta_R(a,b) = 2 asin sqrt( ab / ((R+a)(R+b)) ).
```

It is symmetric, positive, strictly decreasing in `R`, and strictly
increasing in either surrounding radius.

There are `n-1` values in `{2,...,n}`. Put

```text
H = 1 + ceil((n-1)/2).
```

Build lists `A_{2,n}` and `B_{2,n}` as follows, with `j=0,1,2,...`:

- append `2+2j` to `A_{2,n}` when `2+2j <= H`, then append `n-1-2j`
  when `n-1-2j > H`;
- append `3+2j` to `B_{2,n}` when `3+2j <= H`, then append `n-2-2j`
  when `n-2-2j > H`;
- stop each construction after a value of `j` appends nothing.

Define

```text
sigma*_{2,n} = A_{2,n} followed by reverse(B_{2,n}) followed by n.
```

This is the standard Supnick maximum-tour rank convention on
`{1,...,n-1}`, shifted by `i -> i+1`. The low entries of the two lists
partition `{2,...,H}` by parity, the high entries partition
`{H+1,...,n-1}`, and `n` is appended, so every value occurs exactly once.
The word `maximum` refers to the TSP on `-theta`; this is the cycle that
minimizes the sum of `theta` values.

For `n>=5`, the displayed cycle begins `(2,n-1)` and ends in `n`; for `n=4`
it is `(2,3,4)`. Thus the two cyclic neighbors of `2` are exactly `n-1` and
`n` throughout the domain. The two threshold representatives are

```text
sigma*_{2,12} = (2,11,4,9,6,7,8,5,10,3,12),
sigma*_{2,13} = (2,12,4,10,6,8,7,9,5,11,3,13).
```

The parity-explicit undirected edge sets follow by shifting the rank formulas.
For `n=2m+1`, where `m>=2`,

```text
E_{2,2m+1} = {(2,2m+1), (m+1,m+2)}
             union {(k,2m+2-k) : 2 <= k <= m}
             union {(k,2m+4-k) : 3 <= k <= m+1}.
```

For `n=2m+2`, where `m>=1`,

```text
E_{2,2m+2} = {(2,2m+2)}
             union {(k,2m+3-k) : 2 <= k <= m+1}
             union {(k,2m+5-k) : 3 <= k <= m+2}.
```

Each formula contains exactly `n-1` distinct edges. In both, the first
indexed family begins with `(2,n-1)`, while the distinguished edge is `(2,n)`.

## 2. Closure formulas and the implicit root

Let `C_{2,n}(R)` be the adjacent-angle sum of `sigma*_{2,n}`. The edge sets
give

```text
C_{2,2m+1}(R)
  = theta_R(2,2m+1) + theta_R(m+1,m+2)
    + sum_{k=2}^{m} theta_R(k,2m+2-k)
    + sum_{k=3}^{m+1} theta_R(k,2m+4-k),

C_{2,2m+2}(R)
  = theta_R(2,2m+2)
    + sum_{k=2}^{m+1} theta_R(k,2m+3-k)
    + sum_{k=3}^{m+2} theta_R(k,2m+5-k).
```

The chain root is defined without any order ellipsis by

```text
C_{2,n}(R_{2,n}) = 2 pi.
```

Every summand is continuous and strictly decreasing in `R`. As `R` tends to
zero from above, the sum tends to `(n-1)pi > 2pi`; as `R` tends to infinity,
it tends to zero. Hence `R_{2,n}` exists and is unique.

The paper's anti-Monge theorem and Supnick's fixed-tour theorem apply to
arbitrary distinct increasing radii, not only to a set starting at `1`.
Consequently, for each fixed `R`, `C_{2,n}(R)` is the minimum chain cost over
all cyclic orders on `{2,...,n}`.

### Lemma 1: the chain roots strictly increase

Fix `R>0`. In a fixed-`R` minimizing cycle on `{2,...,n+1}`, let `a,b<=n`
be the neighbors of `n+1`. Delete `n+1` and join `a` directly to `b`. The
cost falls strictly, because

```text
theta_R(a,n+1) + theta_R(n+1,b) > theta_R(a,b).
```

Indeed, `theta_R(a,n+1)>theta_R(a,b)` since `n+1>b`, and the other removed
angle is positive. The induced cycle on `{2,...,n}` need not itself be the
canonical Supnick representative, but its cost is at least the fixed-`R`
minimum `C_{2,n}(R)`. Therefore

```text
C_{2,n+1}(R) > C_{2,n}(R)       for every R>0.
```

At the two implicit roots, strict decrease in `R` now gives

```text
R_{2,n+1} > R_{2,n}.                                  (1)
```

No claim that vertex deletion preserves the displayed Supnick order is used.

## 3. Radius-2 Descartes threshold

Put `x=1/R` and abbreviate

```text
alpha_n = 1/n + 1/(n-1),
beta_n  = 1/(n(n-1)).
```

When the central circle and circles `n,n-1` are mutually tangent, the bounded
Descartes pocket between them has curvature

```text
P_n(x) = x + alpha_n + 2 sqrt(alpha_n*x + beta_n).       (2)
```

The plus sign is the bounded Soddy-circle branch. Its radius is `1/P_n(x)`.
The exact angular/pocket equivalence, together with strict increase of
`theta_R(a,rho)` in `rho`, yields

```text
sign( theta_R(n,2) + theta_R(2,n-1) - theta_R(n,n-1) )
    = sign(P_n(1/R) - 1/2).                              (3)
```

The function `P_n` is strictly increasing in `x>=0`.

### The threshold domain starts at `n=9`

For fixed `x>=0`, both `alpha_n` and `beta_n` strictly decrease with `n`, so

```text
P_{n+1}(x) < P_n(x).                                    (4)
```

At `x=0`, exact endpoint comparisons give

```text
P_8(0) = 15/56 + 1/sqrt(14) > 1/2,
1/14 - (13/56)^2 = 55/3136 > 0,

P_9(0) = 17/72 + sqrt(2)/6 < 1/2,
(19/72)^2 - 1/18 = 73/5184 > 0.
```

Thus `P_n(x)>1/2` for every `x>0` when `4<=n<=8`, and (3) immediately gives

```text
Delta_{2,n} > 0  for 4 <= n <= 8.                       (5)
```

For every `n>=9`, `P_n(0)<1/2` and `P_n(x)` tends to infinity with `x`, so
there is a unique positive crossing.

### Solving the crossing without an extraneous root

Let

```text
q_n = sqrt(alpha_n/2 + beta_n).
```

In the positive-threshold domain, `P_n(0)<1/2` implies `alpha_n<1/2` and

```text
q_n^2 - alpha_n^2
    = alpha_n(1/2-alpha_n) + beta_n > 0.
```

Hence `q_n>alpha_n`. Define

```text
kappa_{2,n}
  = 1/2 + alpha_n - 2 q_n
  = 1/2 + 1/n + 1/(n-1)
    - 2 sqrt((2n+1)/(2n(n-1))).                          (6)
```

Then

```text
alpha_n*kappa_{2,n} + beta_n = (q_n-alpha_n)^2,
```

and the positive square root is `q_n-alpha_n`, so direct substitution in
(2) gives `P_n(kappa_{2,n})=1/2`. The other root produced by squaring is
`1/2+alpha_n+2q_n`; it makes the right side of the unsquared square-root
equation negative and is extraneous.

Define

```text
T_{2,n} = 1/kappa_{2,n}       for n >= 9.
```

Equations (2), (3), and strict increase in `x` give the exact sign criterion

```text
Delta_{2,n} < 0  iff  R_{2,n} > T_{2,n},
Delta_{2,n} = 0  iff  R_{2,n} = T_{2,n},
Delta_{2,n} > 0  iff  R_{2,n} < T_{2,n}.                 (7)
```

### Lemma 2: the thresholds strictly decrease

At `x=kappa_{2,n}`, equation (4) gives

```text
P_{n+1}(kappa_{2,n}) < 1/2.
```

Because `P_{n+1}` is strictly increasing and reaches `1/2` at its unique
positive root,

```text
kappa_{2,n+1} > kappa_{2,n},
T_{2,n+1} < T_{2,n}             for n >= 9.              (8)
```

This implicit comparison is the only threshold monotonicity needed. It does
not use or imply monotonicity of the raw angular deficit.

## 4. Exact bounds at `n=12,13`

Only rational square comparisons and the classical strict bounds
`3<pi<22/7` are used. The lower bound follows from the regular hexagon
inscribed in the unit circle; the upper bound follows, for example, from

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

### The positive side: `R_{2,12}<17<T_{2,12}`

Formula (6) gives

```text
kappa_{2,12} = 89/132 - 5/sqrt(66).
```

Moreover,

```text
89/132 - 1/17 = 1381/2244,
25/66 - (1381/2244)^2 = 239/5035536 > 0.
```

All quantities compared are positive, so `kappa_{2,12}<1/17` and therefore
`T_{2,12}>17`.

It remains to put the chain root below `17`. For each edge `e=(a,b)` of
`sigma*_{2,12}` at `R=17`, set

```text
s_e^2 = ab / ((17+a)(17+b)).
```

The following exact rational checks give `s_e<q_e<1/3`.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(2,11)` | `11/266` | `51/250` | `2183/8312500` |
| `(11,4)` | `11/147` | `137/500` | `9043/36750000` |
| `(4,9)` | `6/91` | `257/1000` | `10459/91000000` |
| `(9,6)` | `27/299` | `301/1000` | `89699/299000000` |
| `(6,7)` | `7/92` | `69/250` | `32/359375` |
| `(7,8)` | `7/75` | `153/500` | `227/750000` |
| `(8,5)` | `4/55` | `27/100` | `19/110000` |
| `(5,10)` | `25/297` | `291/1000` | `150257/297000000` |
| `(10,3)` | `1/18` | `59/250` | `79/562500` |
| `(3,12)` | `9/145` | `1/4` | `1/2320` |
| `(12,2)` | `24/551` | `209/1000` | `68231/551000000` |

For `0<u<=1/3`, putting `z=u^2` gives

```text
(1+3u^2/5)^2(1-u^2)-1
    = u^2(5-21u^2-9u^4)/25 > 0;
```

the last polynomial is decreasing in `z` and at `z=1/9` equals `23/9`.
Therefore

```text
1/sqrt(1-u^2) < 1+3u^2/5,
asin(s) < s+s^3/5       for 0<s<1/3.
```

Using the table and monotonicity of `s+s^3/5`,

```text
sum_e asin(s_e)
  < sum_e (q_e+q_e^3/5)
  = 1457520693/500000000
  < 3 < pi.
```

Hence `C_{2,12}(17)<2pi`. Since the closure sum decreases strictly in `R`,

```text
R_{2,12}<17<T_{2,12}.                                  (9)
```

### The negative side: `T_{2,13}<14<R_{2,13}`

Here

```text
kappa_{2,13} = 103/156 - 3/sqrt(26),
103/156 - 1/14 = 643/1092,
(643/1092)^2 - 9/26 = 673/1192464 > 0.
```

Thus `kappa_{2,13}>1/14`, so `T_{2,13}<14`.

At `R=14`, the following exact checks give `s_e>q_e` for every edge of
`sigma*_{2,13}`.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(2,12)` | `3/52` | `6/25` | `3/32500` |
| `(12,4)` | `4/39` | `8/25` | `4/24375` |
| `(4,10)` | `5/54` | `38/125` | `149/843750` |
| `(10,6)` | `1/8` | `353/1000` | `391/1000000` |
| `(6,8)` | `6/55` | `33/100` | `21/110000` |
| `(8,7)` | `4/33` | `87/250` | `223/2062500` |
| `(7,9)` | `3/23` | `361/1000` | `2617/23000000` |
| `(9,5)` | `45/437` | `8/25` | `157/273125` |
| `(5,11)` | `11/95` | `17/50` | `9/47500` |
| `(11,3)` | `33/425` | `139/500` | `1543/4250000` |
| `(3,13)` | `13/153` | `291/1000` | `43807/153000000` |
| `(13,2)` | `13/216` | `49/200` | `173/1080000` |

Their lower bounds sum to

```text
sum_e q_e = 373/100 > 22/7 > pi.
```

Since `asin(s)>s` for `s>0`, `C_{2,13}(14)>2pi`. Thus

```text
T_{2,13}<14<R_{2,13}.                                  (10)
```

## 5. Uniform conclusion

For `9<=n<=12`, equations (1), (8), and (9) give

```text
R_{2,n} <= R_{2,12} < 17 < T_{2,12} <= T_{2,n}.
```

Criterion (7) proves `Delta_{2,n}>0` there. Equation (5) supplies the same
strict sign for `4<=n<=8`.

For every `n>=13`, equations (1), (8), and (10) give

```text
R_{2,n} >= R_{2,13} > 14 > T_{2,13} >= T_{2,n}.
```

Criterion (7) proves `Delta_{2,n}<0` for the entire upper range. This
completes the exact `4..12` versus `13..infinity` classification.

## 6. Counterexample search and excluded routes

1. **The raw deficit is not monotone.** A production-independent
   high-precision scan gives

   ```text
   Delta_{2,29} = -0.18210378851879555...,
   Delta_{2,30} = -0.18209965250262137....
   ```

   The proof compares increasing roots with decreasing thresholds; it never
   assumes that `Delta_{2,n}` decreases.

2. **The shifted convention matters.** The chain-minimizing cycle is the
   Supnick maximum tour for `-theta`. The complementary minimum-tour helper
   produces plausible numerical radii but is the wrong cycle for this claim.

3. **Deleting the largest vertex need not preserve the displayed order.**
   Lemma 1 uses only that the induced order is a valid smaller cycle whose
   cost is bounded below by the fixed-`R` minimum.

4. **There is no positive Descartes threshold for `4<=n<=8`.** Those cases
   are resolved directly from the limiting pocket curvature rather than by
   taking a reciprocal of a nonpositive algebraic root.

5. **Finite diagnostics are not the proof.** The all-`n` conclusion rests on
   exact opposing monotonicities and rational endpoint bounds.

6. **The quantifiers stop at this seam.** Failure of the formal shifted
   necklace neither constructs a feasible replacement nor determines the
   behavior of circle `2` across all global optima.

## 7. Independent finite diagnostic checker

The task-local script

```text
ops/TASK-20260804__radius2_seam_threshold/check_seam.py
```

does not import `ringmin`. It reconstructs the shifted order in two ways,
checks both parity edge formulas, verifies every displayed rational bridge
with `fractions.Fraction`, solves the chain roots in high precision over a
selected finite range, and repeats the scan at higher precision. A separate
integration command compares its conventions with the production
`supnick_max_tour` and `interleave` helpers. These checks corroborate the
proof and expose raw-deficit nonmonotonicity; they are not an all-`n`
certificate.
