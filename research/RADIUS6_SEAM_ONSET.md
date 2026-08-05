# Exact radius-6 Supnick seam onset

```text
status=PROVED
domain=integers n >= 8
proved_on=2026-08-05
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For every integer `n>=8`, let `sigma*_{6,n}` be the chain-minimizing
Supnick cyclic order on the consecutive radii `{6,...,n}`, and put

```text
R_{6,n} = R_chain(sigma*_{6,n}).
```

Define the radius-6 formal seam deficit

```text
Delta_{6,n}
  = theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    - theta_{R_{6,n}}(n,n-1).
```

This note proves the exact classification

```text
Delta_{6,n} > 0  for 8 <= n <= 29,
Delta_{6,n} < 0  for every n >= 30.
```

Consequently the first strict radius-6 formal seam obstruction is

```text
s_6 = 30.
```

The general theorem in `research/FIXED_K_SUPNICK_SEAM.md` is reused in full
and is not reproved here. The only new mathematical work is the exact
endpoint bridge

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30}.                           (1)
```

This theorem concerns only the formal seam `(n,6,n-1)` of one
chain-minimizing Supnick cycle. A positive seam deficit is not a proof of
full fixed-order feasibility. Nothing here determines `R*(n)`, classifies a
global optimum or contact graph, or says that circle `6` floats in any or
every global optimum. The result is post-arXiv-v1 work; the historical paper
and its publication assets remain unchanged.

## 1. Imported reduction

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `C_{6,n}(R)` be the adjacent-angle sum of `sigma*_{6,n}`. The fixed-`k`
theorem supplies, without any new proof here:

- the unique root `C_{6,n}(R_{6,n})=2*pi` and strict decrease of `C_{6,n}`
  in `R`;
- strict increase of `R_{6,n}` in `n`;
- `Delta_{6,n}>0` on the no-threshold range `8<=n<=24`;
- for `n>=25`, the positive threshold

  ```text
  kappa_{6,n}
    = 1/6 + 1/n + 1/(n-1)
      - 2 sqrt((2n+5)/(6n(n-1))),
  T_{6,n} = 1/kappa_{6,n},
  ```

  with the exact sign criterion

  ```text
  Delta_{6,n} < 0  iff  R_{6,n} > T_{6,n},
  Delta_{6,n} = 0  iff  R_{6,n} = T_{6,n},
  Delta_{6,n} > 0  iff  R_{6,n} < T_{6,n};
  ```

- strict decrease of `T_{6,n}` in `n` on that positive-threshold domain.

Thus only the four strict endpoint inequalities (1) remain.

## 2. Exact threshold inequalities at `R=211/2`

At `n=29`, write the reciprocal threshold as

```text
kappa_{6,29} = 577/2436 - sqrt(3/58).
```

Both displayed terms are positive, and positivity of the difference has the
independent exact witness

```text
(577/2436)^2 - 3/58 = 25993/5934096 > 0.
```

For comparison with the reciprocal separator,

```text
577/2436 - 2/211 = 116875/513996 > 0,
3/58 - (116875/513996)^2
  = 5332031/264191888016 > 0.
```

Every quantity compared before squaring is positive. Therefore

```text
0 < kappa_{6,29} < 2/211,
211/2 < T_{6,29}.                                      (2)
```

At `n=30`, one has

```text
kappa_{6,30} = 34/145 - sqrt(13/261).
```

Again positivity is checked before taking a reciprocal:

```text
(34/145)^2 - 13/261 = 979/189225 > 0.
```

For the separator comparison,

```text
34/145 - 2/211 = 6884/30595 > 0,
(6884/30595)^2 - 13/261
  = 6894679/8424486225 > 0.
```

Thus

```text
kappa_{6,30} > 2/211 > 0,
T_{6,30} < 211/2.                                      (3)
```

Equations (2)-(3) prove both threshold sides of (1) by rational sign and
square comparisons only.

## 3. Exact chain inequality at `n=29`

The shifted Supnick formula gives the representative

```text
sigma*_{6,29}
  = (6,28,8,26,10,24,12,22,14,20,16,18,
     17,19,15,21,13,23,11,25,9,27,7,29).
```

For every adjacent edge `e=(a,b)` at `R=211/2`, set

```text
s_e^2 = ab/((211/2+a)(211/2+b)).
```

The following is the complete 24-edge table in cyclic order. Each displayed
margin is exact and positive.

| edge `e` | `s_e^2` | `q_e` | `q_e^2-s_e^2` |
|---|---:|---:|---:|
| `(6,28)` | `224/19847` | `1063/10000` | `26494743/1984700000000` |
| `(8,28)` | `896/60609` | `76/625` | `77584/23675390625` |
| `(8,26)` | `832/59701` | `1181/10000` | `68626461/5970100000000` |
| `(10,26)` | `1040/60753` | `1309/10000` | `99111193/6075300000000` |
| `(10,24)` | `320/19943` | `1267/10000` | `14278527/1994300000000` |
| `(12,24)` | `1152/60865` | `86/625` | `31508/4755078125` |
| `(12,22)` | `352/19975` | `83/625` | `4311/312109375` |
| `(14,22)` | `1232/60945` | `711/5000` | `1795469/304725000000` |
| `(14,20)` | `1120/59989` | `1367/10000` | `100784421/5998900000000` |
| `(16,20)` | `1280/60993` | `1449/10000` | `60963793/6099300000000` |
| `(16,18)` | `128/6669` | `693/5000` | `2780581/166725000000` |
| `(17,18)` | `1224/60515` | `1423/10000` | `27715687/1210300000000` |
| `(17,19)` | `1292/61005` | `91/625` | `98981/4766015625` |
| `(15,19)` | `380/20003` | `1379/10000` | `38524923/2000300000000` |
| `(15,21)` | `1260/60973` | `719/5000` | `20663053/1524325000000` |
| `(13,21)` | `364/19987` | `27/200` | `10523/799480000` |
| `(13,23)` | `1196/60909` | `701/5000` | `30743509/1522725000000` |
| `(11,23)` | `1012/59881` | `1301/10000` | `154640481/5988100000000` |
| `(11,25)` | `1100/60813` | `269/2000` | `489493/243252000000` |
| `(9,25)` | `100/6641` | `307/2500` | `907609/41506250000` |
| `(9,27)` | `972/60685` | `633/5000` | `3162393/303425000000` |
| `(7,27)` | `84/6625` | `1127/10000` | `116837/5300000000` |
| `(7,29)` | `812/60525` | `1159/10000` | `4083301/242100000000` |
| `(6,29)` | `696/59987` | `539/5000` | `27483227/1499675000000` |

Thus every row has

```text
0 < s_e < q_e <= 91/625 < 3/20 < 1,
```

where the last nontrivial domain margin is

```text
3/20 - 91/625 = 11/2500 > 0.                           (4)
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

Applying (5) to all 24 rows gives the exact rational total

```text
sum_e asin(s_e)
  < sum_e (q_e+7q_e^3/40)
  = 12564579832327/4000000000000
  = 333/106 - 77268886669/212000000000000
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
pi/4 = 4 atan(1/5) - atan(1/239).                      (7)
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

Using (7) and multiplying by four yields

```text
pi > 1231847548/392109375
   = 333/106 + 3418213/41563593750
   > 333/106.                                         (8)
```

Equations (6)-(8) show

```text
C_{6,29}(211/2) = 2 sum_e asin(s_e) < 2*pi.
```

Strict decrease of the closure sum and its defining equality at the root
then imply

```text
R_{6,29} < 211/2.                                      (9)
```

## 4. Exact chain inequality at `n=30`

Here a shifted Supnick representative is

```text
sigma*_{6,30}
  = (6,29,8,27,10,25,12,23,14,21,16,19,18,
     17,20,15,22,13,24,11,26,9,28,7,30).
```

The following is the complete 25-edge table in cyclic order. Each displayed
margin is exact and positive.

| edge `e` | `s_e^2` | `q_e` | `s_e^2-q_e^2` |
|---|---:|---:|---:|
| `(6,29)` | `696/59987` | `1/10` | `9613/5998700` |
| `(8,29)` | `928/61063` | `3/25` | `30433/38164375` |
| `(8,27)` | `864/60155` | `11/100` | `272249/120310000` |
| `(10,27)` | `72/4081` | `13/100` | `30311/40810000` |
| `(10,25)` | `1000/60291` | `3/25` | `82381/37681875` |
| `(12,25)` | `80/4089` | `13/100` | `108959/40890000` |
| `(12,23)` | `1104/60395` | `13/100` | `166649/120790000` |
| `(14,23)` | `1288/61423` | `7/50` | `210273/153557500` |
| `(14,21)` | `1176/60467` | `13/100` | `1541077/604670000` |
| `(16,21)` | `448/20493` | `7/50` | `115843/51232500` |
| `(16,19)` | `1216/60507` | `7/50` | `75157/151267500` |
| `(18,19)` | `24/1079` | `7/50` | `7129/2697500` |
| `(17,18)` | `1224/60515` | `7/50` | `18953/30257500` |
| `(17,20)` | `272/12299` | `7/50` | `77349/30747500` |
| `(15,20)` | `1200/60491` | `7/50` | `35941/151227500` |
| `(15,22)` | `88/4097` | `7/50` | `19247/10242500` |
| `(13,22)` | `1144/60435` | `13/100` | `245297/120870000` |
| `(13,24)` | `416/20461` | `7/50` | `37411/51152500` |
| `(11,24)` | `1056/60347` | `13/100` | `361357/603470000` |
| `(11,26)` | `1144/61279` | `13/100` | `1083849/612790000` |
| `(9,26)` | `936/60227` | `3/25` | `42957/37641875` |
| `(9,28)` | `336/20381` | `3/25` | `26571/12738125` |
| `(7,28)` | `784/60075` | `11/100` | `22837/24030000` |
| `(7,30)` | `56/4065` | `11/100` | `13627/8130000` |
| `(6,30)` | `720/60433` | `1/10` | `11567/6043300` |

For every row, positivity of `R=211/2` gives

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
  = 159/50
  = 22/7 + 13/350
  > 22/7
  > pi.                                                (10)
```

The final classical strict inequality has the exact positive witness

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.
```

It follows that

```text
C_{6,30}(211/2) = 2 sum_e asin(s_e) > 2*pi,
R_{6,30} > 211/2.                                     (11)
```

Equations (2), (3), (9), and (11) establish all four strict inequalities in
(1), each with an explicit nonzero exact margin.

## 5. Exact onset from the imported theorem

For `25<=n<=29`, the imported opposing monotonicities and (1) give

```text
R_{6,n} <= R_{6,29} < 211/2 < T_{6,29} <= T_{6,n}.
```

Hence `Delta_{6,n}>0`; the imported no-threshold result already gives the
same sign for `8<=n<=24`. For every `n>=30`,

```text
T_{6,n} <= T_{6,30} < 211/2 < R_{6,30} <= R_{6,n},
```

so `Delta_{6,n}<0`. This proves `s_6=30`, with no endpoint equality, and
imports persistence for all larger integers without using any finite scan or
any monotonicity assertion about the raw angular deficits.

## 6. Exact checker and diagnostic separation

The task-local script

```text
ops/TASK-20260805__radius6_seam_onset/check_seam.py
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
