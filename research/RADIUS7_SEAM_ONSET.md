# Exact radius-7 Supnick seam onset

```text
status=PROVED
domain=integers n >= 9
proved_on=2026-08-05
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For every integer `n>=9`, let `sigma*_{7,n}` be the chain-minimizing
Supnick cyclic order on the consecutive radii `{7,...,n}`, and put

```text
R_{7,n} = R_chain(sigma*_{7,n}).
```

Define the radius-7 formal seam deficit

```text
Delta_{7,n}
  = theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    - theta_{R_{7,n}}(n,n-1).
```

This note proves the exact classification

```text
Delta_{7,n} > 0  for 9 <= n <= 33,
Delta_{7,n} < 0  for every n >= 34.
```

Consequently the first strict radius-7 formal seam obstruction is

```text
s_7 = 34.
```

The general theorem in `research/FIXED_K_SUPNICK_SEAM.md` is reused in full
and is not reproved here. The only new mathematical work is the exact
endpoint bridge

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34}.                             (1)
```

This theorem concerns only the formal seam `(n,7,n-1)` of one
chain-minimizing Supnick cycle. A positive seam deficit is not a proof of
full fixed-order feasibility. Nothing here determines `R*(n)`, classifies a
global optimum or contact graph, or says that circle `7` floats in any or
every global optimum. The result is post-arXiv-v1 work; the historical paper
and its publication assets remain unchanged.

## 1. Imported reduction

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `C_{7,n}(R)` be the adjacent-angle sum of `sigma*_{7,n}`. The fixed-`k`
theorem supplies, without any new proof here:

- the unique root `C_{7,n}(R_{7,n})=2*pi` and strict decrease of `C_{7,n}`
  in `R`;
- strict increase of `R_{7,n}` in `n`;
- `Delta_{7,n}>0` on the no-threshold range `9<=n<=28`;
- for `n>=29`, the positive threshold

  ```text
  kappa_{7,n}
    = 1/7 + 1/n + 1/(n-1)
      - 2 sqrt((2n+6)/(7n(n-1))),
  T_{7,n} = 1/kappa_{7,n},
  ```

  with the exact sign criterion

  ```text
  Delta_{7,n} < 0  iff  R_{7,n} > T_{7,n},
  Delta_{7,n} = 0  iff  R_{7,n} = T_{7,n},
  Delta_{7,n} > 0  iff  R_{7,n} < T_{7,n};
  ```

- strict decrease of `T_{7,n}` in `n` on that positive-threshold domain.

Thus only the four strict endpoint inequalities (1) remain.

## 2. Exact threshold inequalities at `R=140`

At `n=33`, write the reciprocal threshold as

```text
kappa_{7,33} = 1511/7392 - sqrt(3/77).
```

Both displayed terms are positive, and positivity of the difference has the
independent exact witness

```text
(1511/7392)^2 - 3/77 = 154225/54641664 > 0.
```

For comparison with the reciprocal separator,

```text
1511/7392 - 1/140 = 7291/36960 > 0,
3/77 - (7291/36960)^2
  = 63719/1366041600 > 0.
```

Every quantity compared before squaring is positive. Therefore

```text
0 < kappa_{7,33} < 1/140,
140 < T_{7,33}.                                        (2)
```

At `n=34`, one has

```text
kappa_{7,34} = 1591/7854 - sqrt(148/3927).
```

Again positivity is checked before taking a reciprocal:

```text
(1591/7854)^2 - 148/3927 = 206497/61685316 > 0.
```

For the separator comparison,

```text
1591/7854 - 1/140 = 15349/78540 > 0,
(15349/78540)^2 - 148/3927
  = 3113401/6168531600 > 0.
```

Thus

```text
kappa_{7,34} > 1/140 > 0,
T_{7,34} < 140.                                        (3)
```

Equations (2)-(3) prove both threshold sides of (1) by rational sign and
square comparisons only. The physical minus root and exclusion of the
extraneous plus root are already part of the imported fixed-`k` theorem.

## 3. Exact chain inequality at `n=33`

The shifted Supnick formula gives the representative

```text
sigma*_{7,33}
  = (7,32,9,30,11,28,13,26,15,24,17,22,19,20,
     21,18,23,16,25,14,27,12,29,10,31,8,33).
```

For every adjacent edge `e=(a,b)` at `R=140`, set

```text
s_e^2 = ab/((140+a)(140+b)).
```

The following is the complete 27-edge table in cyclic order. Each displayed
margin is exact and positive.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(7,32)` | `8/903` | `12/125` | `5032/14109375` |
| `(9,32)` | `72/6407` | `27/250` | `170703/400437500` |
| `(9,30)` | `27/2533` | `13/125` | `6202/39578125` |
| `(11,30)` | `33/2567` | `57/500` | `90183/641750000` |
| `(11,28)` | `11/906` | `14/125` | `5701/14156250` |
| `(13,28)` | `13/918` | `3/25` | `137/573750` |
| `(13,26)` | `169/12699` | `29/250` | `117359/793687500` |
| `(15,26)` | `39/2573` | `31/250` | `35153/160812500` |
| `(15,24)` | `18/1271` | `3/25` | `189/794375` |
| `(17,24)` | `102/6437` | `63/500` | `48453/1609250000` |
| `(17,22)` | `187/12717` | `61/500` | `569957/3179250000` |
| `(19,22)` | `209/12879` | `16/125` | `31399/201234375` |
| `(19,20)` | `19/1272` | `31/250` | `8723/19875000` |
| `(20,21)` | `3/184` | `16/125` | `229/2875000` |
| `(18,21)` | `27/1817` | `61/500` | `11057/454250000` |
| `(18,23)` | `207/12877` | `16/125` | `62137/201203125` |
| `(16,23)` | `92/6357` | `61/500` | `654397/1589250000` |
| `(16,25)` | `20/1287` | `63/500` | `108103/321750000` |
| `(14,25)` | `5/363` | `59/500` | `13603/90750000` |
| `(14,27)` | `27/1837` | `61/500` | `85477/459250000` |
| `(12,27)` | `81/6346` | `57/500` | `184077/793250000` |
| `(12,29)` | `87/6422` | `59/500` | `302491/802750000` |
| `(10,29)` | `29/2535` | `27/250` | `7103/31687500` |
| `(10,31)` | `31/2565` | `11/100` | `73/5130000` |
| `(8,31)` | `62/6327` | `1/10` | `127/632700` |
| `(8,33)` | `66/6401` | `51/500` | `149001/1600250000` |
| `(7,33)` | `11/1211` | `12/125` | `2509/18921875` |

Thus every row has

```text
0 < s_e < q_e <= 16/125 < 3/20 < 1,
```

where the last nontrivial domain margin is

```text
3/20 - 16/125 = 11/500 > 0.                            (4)
```

For `0<u<=3/20`, the exact identity

```text
(1+21u^2/40)^2(1-u^2)-1
  = u^2(80-1239u^2-441u^4)/1600
```

has a positive right-hand side. Indeed, the final polynomial is strictly
decreasing in `u^2>=0` and at `u^2=9/400` equals

```text
8303879/160000 > 0.
```

The factors squared above are positive on the stated domain, so

```text
1/sqrt(1-u^2) < 1+21u^2/40.
```

Integrating from `0` to `s`, and then using strict increase of
`u+7u^3/40`, gives

```text
asin(s) < s+7s^3/40 < q+7q^3/40
    for 0<s<q<=3/20.                                  (5)
```

Applying (5) to all 27 rows gives the exact rational total

```text
sum_e asin(s_e)
  < sum_e (q_e+7q_e^3/40)
  = 3919372517/1250000000
  = 333/106 - 398256599/66250000000
  < 333/106.                                          (6)
```

For completeness, the comparison with `pi` is also exact. Put

```text
a = atan(1/5),   b = atan(1/239).
```

The tangent double-angle formula gives

```text
tan(2a)=5/12,   tan(4a)=120/119,
tan(4a-b)=(120/119-1/239)/(1+(120/119)(1/239))=1.
```

Here `0<b<a<pi/4` because `atan` is increasing and
`0<1/239<1/5<1=tan(pi/4)`. Thus `0<2a<pi/2`; comparison of
`tan(2a)=5/12` with `tan(pi/4)=1` gives `2a<pi/4` and hence
`4a<pi/2`. Therefore `0<4a-b<pi/2`, so the branch is fixed and

```text
pi/4 = 4 atan(1/5) - atan(1/239).
```

The finite geometric identity

```text
1/(1+x^2) = 1-x^2+x^4-x^6 + x^8/(1+x^2)
```

has positive remainder for `0<x<1`. Integration gives

```text
atan(1/5)
  > 1/5 - 1/(3*5^3) + 1/(5*5^5) - 1/(7*5^7),
atan(1/239) < 1/239.
```

Consequently

```text
pi > 1231847548/392109375
   = 333/106 + 3418213/41563593750
   > 333/106.                                         (7)
```

Equations (6)-(7) show

```text
C_{7,33}(140) = 2 sum_e asin(s_e) < 2*pi.
```

Strict decrease of the closure sum and its defining equality at the root
then imply

```text
R_{7,33} < 140.                                        (8)
```

## 4. Exact chain inequality at `n=34`

Here a shifted Supnick representative is

```text
sigma*_{7,34}
  = (7,33,9,31,11,29,13,27,15,25,17,23,19,21,
     20,22,18,24,16,26,14,28,12,30,10,32,8,34).
```

The following is the complete 28-edge table in cyclic order. Each displayed
margin is exact and positive.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(7,33)` | `11/1211` | `19/200` | `2829/48440000` |
| `(9,33)` | `297/25777` | `21/200` | `512343/1031080000` |
| `(9,31)` | `31/2831` | `1/10` | `269/283100` |
| `(11,31)` | `341/25821` | `11/100` | `285659/258210000` |
| `(11,29)` | `319/25519` | `11/100` | `102201/255190000` |
| `(13,29)` | `29/1989` | `3/25` | `224/1243125` |
| `(13,27)` | `39/2839` | `23/200` | `58169/113560000` |
| `(15,27)` | `81/5177` | `1/8` | `7/331328` |
| `(15,25)` | `5/341` | `3/25` | `56/213125` |
| `(17,25)` | `85/5181` | `1/8` | `259/331584` |
| `(17,23)` | `391/25591` | `3/25` | `14056/15994375` |
| `(19,23)` | `437/25917` | `1/8` | `2051/1658688` |
| `(19,21)` | `19/1219` | `3/25` | `904/761875` |
| `(20,21)` | `3/184` | `1/8` | `1/1472` |
| `(20,22)` | `11/648` | `13/100` | `61/810000` |
| `(18,22)` | `11/711` | `3/25` | `476/444375` |
| `(18,24)` | `54/3239` | `1/8` | `217/207296` |
| `(16,24)` | `8/533` | `3/25` | `203/333125` |
| `(16,26)` | `4/249` | `1/8` | `7/15936` |
| `(14,26)` | `13/913` | `23/200` | `37023/36520000` |
| `(14,28)` | `1/66` | `3/25` | `31/41250` |
| `(12,28)` | `1/76` | `11/100` | `201/190000` |
| `(12,30)` | `9/646` | `23/200` | `9133/12920000` |
| `(10,30)` | `1/85` | `21/200` | `503/680000` |
| `(10,32)` | `8/645` | `11/100` | `391/1290000` |
| `(8,32)` | `16/1591` | `1/10` | `9/159100` |
| `(8,34)` | `34/3219` | `1/10` | `181/321900` |
| `(7,34)` | `17/1827` | `19/200` | `20453/73080000` |

For every row, positivity of `R=140` gives

```text
(R+a)(R+b)-ab = R^2+R(a+b) > 0,
```

so `s_e<1`. The exact table margins therefore establish the complete domain

```text
0 < q_e < s_e < 1.
```

For `0<s<1`, the integral formula for `asin` gives `asin(s)>s`. Hence

```text
sum_e asin(s_e)
  > sum_e q_e
  = 641/200
  = 22/7 + 87/1400
  > 22/7
  > pi.                                                (9)
```

The final classical strict inequality has the exact positive witness

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

It follows that

```text
C_{7,34}(140) = 2 sum_e asin(s_e) > 2*pi,
R_{7,34} > 140.                                       (10)
```

Equations (2), (3), (8), and (10) establish all four strict inequalities in
(1), each with an explicit nonzero exact margin.

## 5. Exact onset from the imported theorem

For `29<=n<=33`, the imported opposing monotonicities and (1) give

```text
R_{7,n} <= R_{7,33} < 140 < T_{7,33} <= T_{7,n}.
```

Hence `Delta_{7,n}>0`; the imported no-threshold result already gives the
same sign for `9<=n<=28`. For every `n>=34`,

```text
T_{7,n} <= T_{7,34} < 140 < R_{7,34} <= R_{7,n},
```

so `Delta_{7,n}<0`. This proves `s_7=34`, with no endpoint equality, and
imports persistence for all larger integers without using any finite scan or
any monotonicity assertion about the raw angular deficits.

## 6. Exact checker and diagnostic separation

The task-local script

```text
ops/TASK-20260805__radius7_seam_onset/check_seam.py
```

imports no production package. Its default exact path uses only the Python
standard library, reconstructs the shifted Supnick order in two ways, audits
both parity edge formulas, checks that every row above appears exactly once
in cyclic order, and recomputes all threshold, square, arcsine-domain,
termwise-bound, rational-total, and `pi` gates with `fractions.Fraction`.
Explicit exceptions keep every gate active under optimized execution.

The opt-in mpmath path performs a finite 60/100-digit root and deficit scan.
Its output is labeled `NUMERICAL_DIAGNOSTIC_ONLY`; it is neither a premise
nor a certificate for the all-`n` theorem. A separate task command compares
the checker constructions with the production `supnick_max_tour` and
`interleave` conventions without adding a production import to the checker.
