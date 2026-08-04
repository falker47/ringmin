# Exact radius-5 Supnick seam onset

```text
status=PROVED
domain=integers n >= 7
proved_on=2026-08-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For every integer `n>=7`, let `sigma*_{5,n}` be the chain-minimizing
Supnick cyclic order on the consecutive radii `{5,...,n}`, and put

```text
R_{5,n} = R_chain(sigma*_{5,n}).
```

Define the radius-5 formal seam deficit

```text
Delta_{5,n}
  = theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    - theta_{R_{5,n}}(n,n-1).
```

This note proves the exact classification

```text
Delta_{5,n} > 0  for 7 <= n <= 24,
Delta_{5,n} < 0  for every n >= 25.
```

Consequently the first strict radius-5 formal seam obstruction is

```text
s_5 = 25.
```

The general theorem in `research/FIXED_K_SUPNICK_SEAM.md` is reused in full
and is not reproved here. The only new mathematical work is the exact
endpoint bridge

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.                              (1)
```

This theorem concerns only the formal seam `(n,5,n-1)` of one
chain-minimizing Supnick cycle. A positive seam deficit is not a proof of
full fixed-order feasibility. Nothing here determines `R*(n)`, classifies a
global optimum or contact graph, or says that circle `5` floats in any or
every global optimum. The result is post-arXiv-v1 work; the historical paper
and its publication assets remain unchanged.

## 1. Imported reduction

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `C_{5,n}(R)` be the adjacent-angle sum of `sigma*_{5,n}`. The fixed-`k`
theorem supplies, without any new proof here:

- the unique root `C_{5,n}(R_{5,n})=2*pi` and strict decrease of `C_{5,n}`
  in `R`;
- strict increase of `R_{5,n}` in `n`;
- `Delta_{5,n}>0` on the no-threshold range `7<=n<=20`;
- for `n>=21`, the positive threshold

  ```text
  kappa_{5,n}
    = 1/5 + 1/n + 1/(n-1)
      - 2 sqrt((2n+4)/(5n(n-1))),
  T_{5,n} = 1/kappa_{5,n},
  ```

  with the exact sign criterion

  ```text
  Delta_{5,n} < 0  iff  R_{5,n} > T_{5,n},
  Delta_{5,n} = 0  iff  R_{5,n} = T_{5,n},
  Delta_{5,n} > 0  iff  R_{5,n} < T_{5,n};
  ```

- strict decrease of `T_{5,n}` in `n` on that positive-threshold domain.

Thus only the four strict endpoint inequalities (1) remain.

## 2. Exact threshold inequalities at `R=75`

At `n=24`, the reciprocal threshold is

```text
kappa_{5,24} = 787/2760 - sqrt(26/345).
```

Both terms are positive, and the direct positivity margin is

```text
(787/2760)^2 - 26/345 = 45289/7617600 > 0.
```

Hence `kappa_{5,24}>0`. Moreover

```text
787/2760 - 1/75 = 3751/13800 > 0,
26/345 - (3751/13800)^2 = 281999/190440000 > 0.
```

All quantities compared before squaring are positive. Therefore

```text
0 < kappa_{5,24} < 1/75,
75 < T_{5,24}.                                         (2)
```

At `n=25`, one has

```text
kappa_{5,25} = 169/600 - sqrt(9/125).
```

Direct positivity is certified independently by

```text
(169/600)^2 - 9/125 = 2641/360000 > 0.
```

For the separator comparison,

```text
169/600 - 1/75 = 161/600 > 0,
(161/600)^2 - 9/125 = 1/360000 > 0.
```

Again the pre-square quantities are positive, so

```text
kappa_{5,25} > 1/75 > 0,
T_{5,25} < 75.                                         (3)
```

Equations (2)-(3) prove the two threshold sides of (1) using only sign gates
and rational comparisons of squares. In particular, the small but nonzero
`1/360000` margin at `n=25` is not replaced by a decimal approximation.

## 3. Exact chain inequality at `n=24`

The shifted Supnick formula gives the representative

```text
sigma*_{5,24}
  = (5,23,7,21,9,19,11,17,13,15,14,16,12,18,10,20,8,22,6,24).
```

For every adjacent edge `e=(a,b)` at `R=75`, set

```text
s_e^2 = ab/((75+a)(75+b)).
```

The following is the complete 20-edge table in cyclic order. Each displayed
margin is exact and positive, so `0<s_e<q_e<=167/1000<1/3` term by term.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(5,23)` | `23/1568` | `61/500` | `5283/24500000` |
| `(7,23)` | `23/1148` | `71/500` | `9267/71750000` |
| `(7,21)` | `49/2624` | `137/1000` | `61/640625` |
| `(9,21)` | `3/128` | `77/500` | `557/2000000` |
| `(9,19)` | `57/2632` | `37/250` | `10177/41125000` |
| `(11,19)` | `209/8084` | `161/1000` | `136341/2021000000` |
| `(11,17)` | `187/7912` | `77/500` | `20031/247250000` |
| `(13,17)` | `221/8096` | `83/500` | `32709/126500000` |
| `(13,15)` | `13/528` | `157/1000` | `917/33000000` |
| `(14,15)` | `7/267` | `81/500` | `1787/66750000` |
| `(14,16)` | `32/1157` | `167/1000` | `267573/1157000000` |
| `(12,16)` | `64/2639` | `39/250` | `13919/164937500` |
| `(12,18)` | `24/899` | `41/250` | `11219/56187500` |
| `(10,18)` | `12/527` | `151/1000` | `16127/527000000` |
| `(10,20)` | `8/323` | `79/500` | `15843/80750000` |
| `(8,20)` | `32/1577` | `143/1000` | `248073/1577000000` |
| `(8,22)` | `176/8051` | `37/250` | `21819/503187500` |
| `(6,22)` | `44/2619` | `13/100` | `2611/26190000` |
| `(6,24)` | `16/891` | `27/200` | `9539/35640000` |
| `(5,24)` | `1/66` | `31/250` | `463/2062500` |

For `0<u<=1/3`, the exact identity

```text
(1+3u^2/5)^2(1-u^2)-1
  = u^2(5-21u^2-9u^4)/25
```

has a positive right-hand side: the final polynomial decreases in `u^2`
and equals `23/9>0` at `u^2=1/9`. Positivity before taking square roots gives

```text
1/sqrt(1-u^2) < 1+3u^2/5.
```

Integrating from `0` to `s`, then using strict increase of `u+u^3/5`, yields

```text
asin(s) < s+s^3/5 < q+q^3/5
    for 0<s<q<=1/3.                                   (4)
```

Applying (4) to every table row gives the exact rational total

```text
sum_e asin(s_e)
  < sum_e (q_e+q_e^3/5)
  = 14962647891/5000000000
  = 3 - 37352109/5000000000
  < 3.                                                 (5)
```

The comparison with `pi` can also be made without decimals. On `0<x<1`, the
finite geometric identity gives

```text
1/(1+x^2)
  = (1-x^2+x^4-x^6+x^8-x^10+x^12-x^14)
    + x^16/(1+x^2).
```

The remainder is strictly positive. Exact termwise integration gives

```text
pi/4
  > 1-1/3+1/5-1/7+1/9-1/11+1/13-1/15
  = 33976/45045
  = 3/4 + 769/180180
  > 3/4.
```

Consequently

```text
3 < pi.                                                (6)
```

Equations (5)-(6) show

```text
C_{5,24}(75) = 2 sum_e asin(s_e) < 2*pi.
```

Strict decrease of the closure sum and its defining equality at the root
then imply

```text
R_{5,24} < 75.                                         (7)
```

## 4. Exact chain inequality at `n=25`

Here a shifted Supnick representative is

```text
sigma*_{5,25}
  = (5,24,7,22,9,20,11,18,13,16,15,14,17,12,19,10,21,8,23,6,25).
```

The following is the complete 21-edge table in cyclic order. With `s_e`
defined at `R=75` as above, every displayed margin is exact and positive,
so `s_e>q_e>0` on every row.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(5,24)` | `1/66` | `3/25` | `31/41250` |
| `(7,24)` | `28/1353` | `7/50` | `3703/3382500` |
| `(7,22)` | `77/3977` | `27/200` | `180767/159080000` |
| `(9,22)` | `33/1358` | `31/200` | `7481/27160000` |
| `(9,20)` | `3/133` | `3/20` | `3/53200` |
| `(11,20)` | `22/817` | `4/25` | `678/510625` |
| `(11,18)` | `33/1333` | `31/200` | `38987/53320000` |
| `(13,18)` | `39/1364` | `33/200` | `18651/13640000` |
| `(13,16)` | `2/77` | `4/25` | `18/48125` |
| `(15,16)` | `8/273` | `17/100` | `1103/2730000` |
| `(14,15)` | `7/267` | `4/25` | `103/166875` |
| `(14,17)` | `119/4094` | `17/100` | `3417/20470000` |
| `(12,17)` | `17/667` | `31/200` | `39013/26680000` |
| `(12,19)` | `38/1363` | `33/200` | `35693/54520000` |
| `(10,19)` | `19/799` | `3/20` | `409/319600` |
| `(10,21)` | `7/272` | `4/25` | `23/170000` |
| `(8,21)` | `7/332` | `29/200` | `197/3320000` |
| `(8,23)` | `92/4067` | `3/20` | `197/1626800` |
| `(6,23)` | `23/1323` | `13/100` | `6413/13230000` |
| `(6,25)` | `1/54` | `27/200` | `317/1080000` |
| `(5,25)` | `1/64` | `3/25` | `49/40000` |

For `0<s<1`, the integral formula for `asin` gives `asin(s)>s`. The strict
domain `s_e<1` follows directly from `(75+a)(75+b)>ab`. Hence the table gives

```text
sum_e asin(s_e)
  > sum_e q_e
  = 63/20
  = 22/7 + 1/140
  > 22/7
  > pi.                                                 (8)
```

The final classical strict inequality has the exact positive witness

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

It follows that

```text
C_{5,25}(75) = 2 sum_e asin(s_e) > 2*pi,
R_{5,25} > 75.                                         (9)
```

Equations (2), (3), (7), and (9) establish all four strict inequalities in
(1), each with an explicit nonzero exact margin.

## 5. Exact onset from the imported theorem

For `21<=n<=24`, the imported opposing monotonicities and (1) give

```text
R_{5,n} <= R_{5,24} < 75 < T_{5,24} <= T_{5,n}.
```

Hence `Delta_{5,n}>0`; the imported no-threshold result already gives the
same sign for `7<=n<=20`. For every `n>=25`,

```text
T_{5,n} <= T_{5,25} < 75 < R_{5,25} <= R_{5,n},
```

so `Delta_{5,n}<0`. This proves `s_5=25`, with no endpoint equality, and
imports persistence for all larger integers without using any finite scan or
any monotonicity assertion about the raw angular deficits.

## 6. Exact checker and diagnostic separation

The task-local script

```text
ops/TASK-20260804__radius5_seam_onset/check_seam.py
```

imports no production package. Its default exact path uses only the Python
standard library, reconstructs the shifted Supnick order in two ways, audits
both parity edge formulas, checks that every row above appears exactly once
in cyclic order, and recomputes all threshold, square, arcsine-bound, and
rational-total margins with `fractions.Fraction`. Explicit exceptions keep
every gate active under `python -O`.

The opt-in mpmath path performs a finite two-precision root and deficit scan.
Its output is labeled `NUMERICAL_DIAGNOSTIC_ONLY`; it checks transcription and
convention stability but is neither a premise nor a certificate for the
all-`n` theorem.
