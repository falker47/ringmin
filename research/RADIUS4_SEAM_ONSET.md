# Exact radius-4 Supnick seam onset

```text
status=PROVED
domain=integers n >= 6
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For every integer `n>=6`, let `sigma*_{4,n}` be the chain-minimizing
Supnick cyclic order on the consecutive radii `{4,...,n}`, and put

```text
R_{4,n} = R_chain(sigma*_{4,n}).
```

Define the radius-4 formal seam deficit

```text
Delta_{4,n}
  = theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    - theta_{R_{4,n}}(n,n-1).
```

This note proves the exact classification

```text
Delta_{4,n} > 0  for 6 <= n <= 20,
Delta_{4,n} < 0  for every n >= 21.
```

Consequently the first strict radius-4 formal seam obstruction is

```text
s_4 = 21.
```

The general theorem in `research/FIXED_K_SUPNICK_SEAM.md` is reused in full
and is not reproved here. The only new mathematical work is the exact
endpoint bridge

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.                              (1)
```

This theorem concerns only the formal seam `(n,4,n-1)` of one
chain-minimizing Supnick cycle. A positive seam deficit is not a proof of
full fixed-order feasibility. Nothing here determines `R*(n)`, classifies a
global optimum or contact graph, or says that circle `4` floats in any or
every global optimum. The result is post-arXiv-v1 work; the historical paper
and its publication assets remain unchanged.

## 1. Imported reduction

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `C_{4,n}(R)` be the adjacent-angle sum of `sigma*_{4,n}`. The fixed-`k`
theorem supplies, without any new proof here:

- the unique root `C_{4,n}(R_{4,n})=2*pi` and strict decrease of `C_{4,n}`
  in `R`;
- strict increase of `R_{4,n}` in `n`;
- `Delta_{4,n}>0` on the no-threshold range `6<=n<=16`;
- for `n>=17`, the positive threshold

  ```text
  kappa_{4,n}
    = 1/4 + 1/n + 1/(n-1)
      - 2 sqrt((2n+3)/(4n(n-1))),
  T_{4,n} = 1/kappa_{4,n},
  ```

  with the exact sign criterion

  ```text
  Delta_{4,n} < 0  iff  R_{4,n} > T_{4,n},
  Delta_{4,n} = 0  iff  R_{4,n} = T_{4,n},
  Delta_{4,n} > 0  iff  R_{4,n} < T_{4,n};
  ```

- strict decrease of `T_{4,n}` in `n` on that positive-threshold domain.

Thus only the four strict endpoint inequalities (1) remain.

## 2. Exact threshold inequalities at `R=50`

At `n=20`, the reciprocal threshold is

```text
kappa_{4,20} = 67/190 - sqrt(43/380).
```

The rational term and radical are positive, and

```text
(67/190)^2 - 43/380 = 101/9025 > 0.
```

Hence `kappa_{4,20}>0`. Moreover

```text
67/190 - 1/50 = 158/475 > 0,
43/380 - (158/475)^2 = 2269/902500 > 0.
```

Every term compared before squaring is positive. Therefore

```text
0 < kappa_{4,20} < 1/50,
50 < T_{4,20}.                                         (2)
```

At `n=21`, one has

```text
kappa_{4,21} = 73/210 - sqrt(3/28),
73/210 - 1/50 = 172/525 > 0.
```

Again all pre-square terms are positive, and

```text
(172/525)^2 - 3/28 = 211/1102500 > 0.
```

Consequently

```text
kappa_{4,21} > 1/50 > 0,
T_{4,21} < 50.                                         (3)
```

For completeness, direct positivity also has the independent square margin

```text
(73/210)^2 - 3/28 = 151/11025 > 0.
```

Equations (2)-(3) prove the two threshold sides of (1) using only rational
square comparisons.

## 3. Exact chain inequality at `n=20`

The shifted Supnick formula gives the representative

```text
sigma*_{4,20}
  = (4,19,6,17,8,15,10,13,12,11,14,9,16,7,18,5,20).
```

For every adjacent edge `e=(a,b)` at `R=50`, set

```text
s_e^2 = ab/((50+a)(50+b)).
```

The following is the complete 17-edge table in cyclic order. Each displayed
margin is exact and positive, so `0<s_e<q_e<=1/5<1/3` term by term.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(4,19)` | `38/1863` | `18/125` | `9862/29109375` |
| `(6,19)` | `19/644` | `43/250` | `407/5031250` |
| `(6,17)` | `51/1876` | `83/500` | `43441/117250000` |
| `(8,17)` | `68/1943` | `47/250` | `42087/121437500` |
| `(8,15)` | `12/377` | `9/50` | `537/942500` |
| `(10,15)` | `1/26` | `99/500` | `2413/3250000` |
| `(10,13)` | `13/378` | `93/500` | `9661/47250000` |
| `(12,13)` | `26/651` | `1/5` | `1/16275` |
| `(11,12)` | `66/1891` | `47/250` | `52219/118187500` |
| `(11,14)` | `77/1952` | `1/5` | `27/48800` |
| `(9,14)` | `63/1888` | `23/125` | `14377/29500000` |
| `(9,16)` | `24/649` | `97/500` | `106441/162250000` |
| `(7,16)` | `56/1881` | `87/500` | `237289/470250000` |
| `(7,18)` | `21/646` | `91/500` | `49763/80750000` |
| `(5,18)` | `9/374` | `39/250` | `3177/11687500` |
| `(5,20)` | `2/77` | `81/500` | `5197/19250000` |
| `(4,20)` | `4/189` | `73/500` | `7181/47250000` |

Only the following elementary endpoint estimate is needed. For
`0<u<=1/3`,

```text
(1+3u^2/5)^2(1-u^2)-1
  = u^2(5-21u^2-9u^4)/25 > 0,
```

because the final polynomial decreases in `u^2` and equals `23/9>0` at
`u^2=1/9`. Positivity before squaring gives

```text
1/sqrt(1-u^2) < 1+3u^2/5.
```

Integrating from `0` to `s`, then using strict increase of `u+u^3/5`, gives

```text
asin(s) < s+s^3/5 < q+q^3/5
    for 0<s<q<=1/3.                                    (4)
```

Applying (4) to every table row yields the exact rational total

```text
sum_e asin(s_e)
  < sum_e (q_e+q_e^3/5)
  = 47493609/15625000
  = 76/25 - 6391/15625000
  < 76/25.                                             (5)
```

To compare this with `pi` without decimals, the perimeter of a regular
octagon inscribed in the unit circle is strictly smaller than the
circumference, so

```text
pi > 4 sqrt(2-sqrt(2)).
```

The nested radical is bounded by one rational square audit:

```text
(889/625)^2 - 2 = 9071/390625 > 0.
```

Since all quantities are positive, `sqrt(2)<889/625<2`, and hence

```text
2-sqrt(2) > 2-889/625 = 361/625 = (19/25)^2.
```

Therefore

```text
pi > 4 sqrt(2-sqrt(2)) > 76/25.                        (6)
```

Equations (5)-(6) give

```text
C_{4,20}(50) = 2 sum_e asin(s_e) < 2*pi.
```

Strict decrease of the closure sum and its defining equality at the root
then imply

```text
R_{4,20} < 50.                                         (7)
```

## 4. Exact chain inequality at `n=21`

Here a shifted Supnick representative is

```text
sigma*_{4,21}
  = (4,20,6,18,8,16,10,14,12,13,11,15,9,17,7,19,5,21).
```

The following is the complete 18-edge table in cyclic order. With `s_e`
defined at `R=50` as above, every displayed margin is exact and positive,
so `s_e>q_e>0` on every row.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(4,20)` | `4/189` | `7/50` | `739/472500` |
| `(6,20)` | `3/98` | `17/100` | `839/490000` |
| `(6,18)` | `27/952` | `4/25` | `1643/595000` |
| `(8,18)` | `18/493` | `19/100` | `2027/4930000` |
| `(8,16)` | `32/957` | `9/50` | `2483/2392500` |
| `(10,16)` | `4/99` | `1/5` | `1/2475` |
| `(10,14)` | `7/192` | `19/100` | `43/120000` |
| `(12,14)` | `21/496` | `1/5` | `29/12400` |
| `(12,13)` | `26/651` | `19/100` | `24989/6510000` |
| `(11,13)` | `143/3843` | `19/100` | `42677/38430000` |
| `(11,15)` | `33/793` | `1/5` | `32/19825` |
| `(9,15)` | `27/767` | `9/50` | `5373/1917500` |
| `(9,17)` | `153/3953` | `19/100` | `102967/39530000` |
| `(7,17)` | `119/3819` | `17/100` | `86309/38190000` |
| `(7,19)` | `7/207` | `9/50` | `733/517500` |
| `(5,19)` | `19/759` | `3/20` | `769/303600` |
| `(5,21)` | `21/781` | `4/25` | `629/488125` |
| `(4,21)` | `14/639` | `7/50` | `3689/1597500` |

For `0<s<1`, the integral formula for `asin` gives `asin(s)>s`. The strict
domain `s_e<1` follows directly from `(50+a)(50+b)>ab`. Thus the table gives

```text
sum_e asin(s_e)
  > sum_e q_e
  = 159/50
  = 22/7 + 13/350
  > 22/7
  > pi.                                                 (8)
```

The final classical strict inequality has the exact positive witness

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

It follows that

```text
C_{4,21}(50) = 2 sum_e asin(s_e) > 2*pi,
R_{4,21} > 50.                                         (9)
```

Equations (2), (3), (7), and (9) establish all four strict inequalities in
(1), each with an explicit nonzero exact margin.

## 5. Exact onset from the imported theorem

For `17<=n<=20`, the imported opposing monotonicities and (1) give

```text
R_{4,n} <= R_{4,20} < 50 < T_{4,20} <= T_{4,n}.
```

Hence `Delta_{4,n}>0`; the imported no-threshold result already gives the
same sign for `6<=n<=16`. For every `n>=21`,

```text
T_{4,n} <= T_{4,21} < 50 < R_{4,21} <= R_{4,n},
```

so `Delta_{4,n}<0`. This proves `s_4=21`, with no endpoint equality, and
imports persistence for all larger integers without using any finite scan or
any monotonicity assertion about the raw angular deficits.

## 6. Exact checker and diagnostic separation

The task-local script

```text
ops/TASK-20260804__radius4_seam_onset/check_seam.py
```

imports no production package. Its default stdlib-only path reconstructs the
shifted Supnick order in two ways, audits both parity edge formulas, checks
that every row above appears exactly once in cyclic order, and recomputes all
threshold, square, arcsine-bound, octagon, and rational-total margins with
`fractions.Fraction`. Explicit exceptions keep every gate active under
`python -O`.

The opt-in mpmath path performs a finite two-precision root and deficit scan.
Its output is labeled `NUMERICAL_DIAGNOSTIC_ONLY`; it checks transcription and
convention stability but is neither a premise nor a certificate for the
all-`n` theorem.
