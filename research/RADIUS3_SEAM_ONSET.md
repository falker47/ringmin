# Exact radius-3 Supnick seam onset

```text
status=PROVED
domain=integers n >= 5
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For every integer `n>=5`, let `sigma*_{3,n}` be the chain-minimizing
Supnick cyclic order on the consecutive radii `{3,...,n}`, and put

```text
R_{3,n} = R_chain(sigma*_{3,n}).
```

Define its radius-3 seam deficit

```text
Delta_{3,n}
  = theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    - theta_{R_{3,n}}(n,n-1).
```

This note proves the exact classification

```text
Delta_{3,n} > 0  for 5 <= n <= 16,
Delta_{3,n} < 0  for every n >= 17.
```

Consequently the first strict radius-3 seam obstruction is exactly

```text
s_3 = 17.
```

The all-`n` conclusion reuses the general monotonicity and persistence
theorem in `research/FIXED_K_SUPNICK_SEAM.md`. The new work here consists of
exact endpoint bridges at `n=16,17`, both using the rational separator
`R=32`.

This is an exact theorem about the formal chain-minimizing Supnick cycle and
its single seam `(n,3,n-1)`. A positive deficit does not prove that the whole
cycle is fully realizable. The result does not determine `R*(n)`, prove
fixed-order full feasibility, or say that circle `3` floats in any or every
global optimum. It is post-arXiv-v1 work; the historical paper and its finite
or heuristic classifications remain unchanged.

## 1. Reduction supplied by the fixed-radius theorem

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `C_{3,n}(R)` be the sum of `theta_R` over the adjacent edges of
`sigma*_{3,n}`. Its unique root is characterized by

```text
C_{3,n}(R_{3,n}) = 2 pi.
```

The fixed-radius theorem proves all of the following facts used below.

1. The two cyclic neighbors of `3` are `n-1,n`.
2. The roots `R_{3,n}` strictly increase with `n`.
3. `Delta_{3,n}>0` throughout the no-threshold range `5<=n<=12`.
4. For every `n>=13`, the positive Descartes threshold is

   ```text
   kappa_{3,n}
     = 1/3 + 1/n + 1/(n-1)
       - 2 sqrt((2n+2)/(3n(n-1))),
   T_{3,n} = 1/kappa_{3,n},
   ```

   and

   ```text
   Delta_{3,n} < 0  iff  R_{3,n} > T_{3,n},
   Delta_{3,n} = 0  iff  R_{3,n} = T_{3,n},
   Delta_{3,n} > 0  iff  R_{3,n} < T_{3,n}.
   ```

5. The thresholds `T_{3,n}` strictly decrease with `n`.

It is therefore enough to prove the four strict inequalities

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.                              (1)
```

No numerical root or finite scan is used in this reduction.

## 2. Exact threshold inequalities at `R=32`

At `n=16`, the threshold reciprocal simplifies to

```text
kappa_{3,16} = 37/80 - sqrt(17/90).
```

First, it is positive: both terms are positive and

```text
(37/80)^2 - 17/90 = 1441/57600 > 0.
```

Moreover,

```text
kappa_{3,16} - 1/32 = 69/160 - sqrt(17/90),
17/90 - (69/160)^2 = 671/230400 > 0.
```

All quantities compared before squaring are positive. Hence

```text
0 < kappa_{3,16} < 1/32,
32 < T_{3,16}.                                         (2)
```

At `n=17`, one has

```text
kappa_{3,17} = 371/816 - sqrt(3/17),
kappa_{3,17} - 1/32 = 691/1632 - sqrt(3/17).
```

Again the terms compared are positive, and the exact square margin is

```text
(691/1632)^2 - 3/17 = 7465/2663424 > 0.
```

Thus

```text
kappa_{3,17} > 1/32 > 0,
T_{3,17} < 32.                                         (3)
```

Equations (2)-(3) prove both threshold inequalities in (1) by rational
algebra, with no decimal approximation to either radical.

## 3. Exact chain inequality at `n=16`

The canonical cycle and its undirected edge set may be read from the general
shifted Supnick formula. One representative is

```text
sigma*_{3,16}
  = (3,15,5,13,7,11,9,10,8,12,6,14,4,16).
```

For every edge `e=(a,b)` at `R=32`, set

```text
s_e^2 = ab/((32+a)(32+b)).
```

The following table gives a rational upper bound `q_e`. Every displayed
margin is exact and positive, so `0<s_e<q_e<=6/25<1/3` term by term.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(3,16)` | `1/35` | `17/100` | `23/70000` |
| `(9,10)` | `15/287` | `23/100` | `1823/2870000` |
| `(3,15)` | `9/329` | `17/100` | `5081/3290000` |
| `(4,14)` | `7/207` | `19/100` | `4727/2070000` |
| `(5,13)` | `13/333` | `1/5` | `8/8325` |
| `(6,12)` | `9/209` | `21/100` | `2169/2090000` |
| `(7,11)` | `77/1677` | `11/50` | `10417/4192500` |
| `(8,10)` | `1/21` | `11/50` | `41/52500` |
| `(4,16)` | `1/27` | `1/5` | `2/675` |
| `(5,15)` | `75/1739` | `21/100` | `16899/17390000` |
| `(6,14)` | `21/437` | `11/50` | `377/1092500` |
| `(7,13)` | `7/135` | `23/100` | `283/270000` |
| `(8,12)` | `3/55` | `6/25` | `21/6875` |
| `(9,11)` | `99/1763` | `6/25` | `1593/1101875` |

The required elementary arcsine bound follows directly from its derivative.
For `0<u<=1/3`, put `z=u^2`. Then

```text
(1+3u^2/5)^2(1-u^2)-1
  = u^2(5-21u^2-9u^4)/25 > 0,
```

because `5-21z-9z^2` decreases with `z` and at `z=1/9` equals `23/9>0`.
Both sides being positive,

```text
1/sqrt(1-u^2) < 1+3u^2/5.
```

Integrating from `0` to `s`, and then using strict increase of
`u+u^3/5`, gives

```text
asin(s) < s+s^3/5 < q+q^3/5       for 0<s<q<=1/3.      (4)
```

Applying (4) term by term to the table yields the exact total

```text
sum_e asin(s_e)
  < sum_e (q_e+q_e^3/5)
  = 14885133/5000000
  = 3 - 114867/5000000
  < 3 < pi.                                             (5)
```

The strict classical bound `3<pi` follows, for example, by comparing the
circumference of the unit circle with its inscribed regular hexagon. Since
`C_{3,16}(32)=2 sum_e asin(s_e)`, equation (5) gives

```text
C_{3,16}(32) < 2 pi.
```

The closure sum is strictly decreasing in `R` and equals `2pi` at its root,
so

```text
R_{3,16} < 32.                                         (6)
```

## 4. Exact chain inequality at `n=17`

One canonical representative is

```text
sigma*_{3,17}
  = (3,16,5,14,7,12,9,10,11,8,13,6,15,4,17).
```

With the same definition of `s_e` at `R=32`, the next table gives rational
lower bounds. Every exact margin is positive, hence `s_e>q_e>0` for every
edge.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(3,17)` | `51/1715` | `17/100` | `2873/3430000` |
| `(3,16)` | `1/35` | `4/25` | `13/4375` |
| `(4,15)` | `5/141` | `9/50` | `1079/352500` |
| `(5,14)` | `35/851` | `1/5` | `24/21275` |
| `(6,13)` | `13/285` | `21/100` | `863/570000` |
| `(7,12)` | `7/143` | `11/50` | `197/357500` |
| `(8,11)` | `11/215` | `11/50` | `297/107500` |
| `(9,10)` | `15/287` | `11/50` | `2773/717500` |
| `(4,17)` | `17/441` | `19/100` | `10799/4410000` |
| `(5,16)` | `5/111` | `21/100` | `1049/1110000` |
| `(6,15)` | `45/893` | `11/50` | `4447/2232500` |
| `(7,14)` | `49/897` | `23/100` | `15487/8970000` |
| `(8,13)` | `13/225` | `6/25` | `1/5625` |
| `(9,12)` | `27/451` | `6/25` | `639/281875` |
| `(10,11)` | `55/903` | `6/25` | `1867/564375` |

For every `0<s<1`, the integral formula for `asin` gives `asin(s)>s`.
Here every `s_e` lies in `(0,1)` because
`(32+a)(32+b)>ab`. The rational lower bounds therefore give

```text
sum_e asin(s_e)
  > sum_e q_e
  = 63/20
  = 22/7 + 1/140
  > 22/7
  > pi.                                                 (7)
```

The last strict inequality is the classical Archimedean bound; an exact
elementary witness is

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

Thus `C_{3,17}(32)=2 sum_e asin(s_e)>2pi`. Strict decrease of the closure
sum now implies

```text
R_{3,17} > 32.                                         (8)
```

Together, (2), (3), (6), and (8) prove the four separator inequalities (1)
with exact nonzero margins.

## 5. Exact onset and persistence

For `13<=n<=16`, root growth, threshold decrease, and the lower endpoint of
(1) give

```text
R_{3,n} <= R_{3,16} < 32 < T_{3,16} <= T_{3,n}.
```

The fixed-`k` sign criterion therefore gives `Delta_{3,n}>0`. Its
no-threshold clause already gives the same strict sign for `5<=n<=12`.

For every `n>=17`, the upper endpoint of (1) gives

```text
R_{3,n} >= R_{3,17} > 32 > T_{3,17} >= T_{3,n},
```

and hence `Delta_{3,n}<0`. This proves `s_3=17` and persistence for every
larger integer without assuming monotonicity of the raw deficits.

## 6. Excluded routes and non-implications

1. **The numerical scan is not the proof.** The proof consists of the exact
   endpoint tables and threshold algebra above, plus the already-proved
   fixed-`k` monotonicity and persistence theorem.
2. **Every square comparison has a sign check.** No radical inequality or
   reciprocal is inferred from squaring terms of unknown sign.
3. **Every adjacent edge is included.** The two displayed tours have `14`
   and `15` distinct edges respectively, including the cyclic closing edge;
   the factor `2` in `theta=2 asin(s)` is retained.
4. **The raw seam deficit need not be monotone.** Only the strictly increasing
   root-minus-threshold comparison from the general theorem is used.
5. **The quantifiers stop at one formal seam.** Positivity through `n=16`
   does not prove full feasibility; obstruction from `n=17` does not
   construct a replacement chain or classify any global optimum.
6. **The published snapshot is historical.** Its computed radius-3 seam
   onset is not silently rewritten; this note is the post-v1 exact proof.

## 7. Independent checker

The task-local script

```text
ops/TASK-20260804__radius3_seam_onset/check_seam.py
```

imports no production package. Its exact layer reconstructs the two shifted
Supnick conventions and parity edge sets, checks every rational table entry,
threshold square margin, arcsine-domain gate, final sum, and edge count using
`fractions.Fraction`. The gates use explicit exceptions and remain active
under `python -O`.

Its separately labeled numerical layer solves selected chain roots at two
high precisions and compares the diagnostic signs with the theorem. Those
finite values corroborate the transcription and conventions; they are not a
premise or certificate for the all-`n` result.
