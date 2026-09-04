# Exact radius-10 Supnick seam onset

```text
status=PROVED
domain=integers n >= 12
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For the chain-minimizing Supnick cycle `sigma*_{10,n}` on `{10,...,n}`, let
`R_{10,n}=R_chain(sigma*_{10,n})` and define

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))),
Delta_{10,n} = theta_{R_{10,n}}(n,10) + theta_{R_{10,n}}(10,n-1)
              - theta_{R_{10,n}}(n,n-1).
```

The four endpoint gates proved below are

```text
R_{10,45} < 270 < T_{10,45},
T_{10,46} < 270 < R_{10,46}.                            (1)
```

Only after these gates close, the fixed-k theorem gives

```text
Delta_{10,n} > 0   for 12 <= n <= 45,
Delta_{10,n} < 0   for every integer n >= 46,
s_10 = 46.
```

**Classification:** exact theorem / proved corollary. This concerns the
formal seam only. It does not prove full fixed-order feasibility before
the onset, determine `R*(n)`, classify a global contact graph, or assert
floating of radius 10 in any or every global optimum. The global certified
scope remains `3<=n<=14`; the historical paper is unchanged.

The separator and candidate threshold margins were suggested by a reviewer.
All quantities below are reconstructed from the authoritative formulas.
Neither that suggestion nor any scan, numerical root or floating arithmetic
is a premise. The only evaluated endpoints are n=45,46.

## 1. Imported fixed-k reduction

Use `research/FIXED_K_SUPNICK_SEAM.md`, sections 1-5. The complete adjacent
sum `C_{10,n}(R)` is continuous and strictly decreasing on `R>0`, and its
unique chain root satisfies `C_{10,n}(R_{10,n})=2*pi`. The roots strictly
increase with n. The formal deficit is positive on `12<=n<=40`.
For `n>=41`, the physical minus-root threshold is

```text
kappa_{10,n} = 1/10 + 1/n + 1/(n-1)
               - 2 sqrt((2n+9)/(10n(n-1))),
T_{10,n} = 1/kappa_{10,n} > 0,
sign(Delta_{10,n}) = sign(T_{10,n}-R_{10,n}).
```

The thresholds strictly decrease. The imported proof supplies the physical
branch and excludes the extraneous plus root. We also check endpoint
curvature positivity explicitly before reciprocating or squaring.

## 2. Threshold gate reconstruction

Put

```text
A_n=1/10+1/n+1/(n-1), B_n=4(2n+9)/(10n(n-1)),
H_n=A_n-1/270, kappa_{10,n}=A_n-sqrt(B_n).
```

Every entry in the following table is strictly positive:

| n | A_n | B_n | A_n^2-B_n | H_n | directed square margin |
|---:|---:|---:|---:|---:|---:|
| 45 | `287/1980` | `1/50` | `3961/3920400` | `839/5940` | `B_45-H_45^2 = 1751/35283600` |
| 46 | `149/1035` | `101/5175` | `1294/1071225` | `871/6210` | `H_46^2-B_46 = 5989/38564100` |

Because `A_n>0`, `B_n>0`, and `A_n^2-B_n>0`, we have
`A_n>sqrt(B_n)>0`, hence both curvatures are positive. Also `270>0`.
For n=45, the sign `H_45>0` and margin `B_45-H_45^2>0` imply
`sqrt(B_45)>H_45`, giving

```text
0 < kappa_{10,45} < 1/270,   270 < T_{10,45}.           (2)
```

For n=46, `H_46>0` and `H_46^2-B_46>0` give `H_46>sqrt(B_46)`, so

```text
kappa_{10,46} > 1/270 > 0,   T_{10,46} < 270.           (3)
```

These positive pre-square signs fix both square-comparison directions.
The displayed fractions are recomputed, not accepted as input evidence.

## 3. Independent complete Supnick cycle constructions

First use the rank-tour formula of fixed-k section 1. Put `N=n-9` and
`h=ceil(N/2)`. For successive `j>=0`, append `1+2j` if at most h and then
`N-1-2j` if greater than h to arm A. Independently append `2+2j` if at
most h and then `N-2-2j` if greater than h to arm B. Stop each arm when
neither entry qualifies. Concatenate `A, reverse(B), N` and add 9 to each
rank. This gives the complete tours

```text
sigma*_{10,45} =
 (10,44,12,42,14,40,16,38,18,36,20,34,22,32,24,30,26,28,
  27,29,25,31,23,33,21,35,19,37,17,39,15,41,13,43,11,45),

sigma*_{10,46} =
 (10,45,12,43,14,41,16,39,18,37,20,35,22,33,24,31,26,29,28,
  27,30,25,32,23,34,21,36,19,38,17,40,15,42,13,44,11,46).
```

Second, specialize the parity-edge formulas without using those tours.
For n=45, `N=36=2*18`; for n=46, `N=37=2*18+1`. Normalizing every
undirected pair to `a<b` gives

```text
E_{10,45} = {(10,45),(27,28)}
            union {(i,54-i): 10<=i<=26}
            union {(i,56-i): 11<=i<=27},

E_{10,46} = {(10,46)}
            union {(i,55-i): 10<=i<=27}
            union {(i,57-i): 11<=i<=28}.
```

Counts are `2+17+17=36` and `1+18+18=37`. Every radius occurs once in
its tour. Reading all consecutive pairs, including the final-to-first
closure `(10,n)`, yields exactly the corresponding edge family with
multiplicity one. Each vertex has degree two and both `(10,n-1)` and
`(10,n)` occur. Thus `C_{10,n}(R)=sum_{(a,b) in E_{10,n}} theta_R(a,b)`
uses every cyclic edge. The checker compares complete multisets from the
two implementations and all `2*36+2*37=146` rotations/reflections.

## 4. Strict rational witnesses on every edge at R=270

For each edge e=(a,b) let

```text
D=10000, Q_e=(270+a)(270+b), s_e=sqrt(ab/Q_e), u_e=m_e/D.
```

Since `Q_e-ab=270(270+a+b)>0`, all `s_e` lie in `(0,1)`.
In the upper table (n=45), `M_e=m_e^2 Q_e-D^2 ab>0` proves `s_e<u_e`.
In the lower table (n=46), `M_e=D^2 ab-m_e^2 Q_e>0` proves `u_e<s_e`.
The directed rational square margin is exactly `M_e/(D^2 Q_e)`.
All m_e are positive. The upper witnesses satisfy
`u_e<=940/10000=47/500<1/5`, with domain margin `53/500>0`.

Every witness is reproducible using integer arithmetic alone:

```text
n=45: m_e=isqrt((D^2 ab)//Q_e)+1,
n=46: m_e=isqrt((D^2 ab-1)//Q_e).
```

Here `//` denotes floor division and isqrt denotes integer square root.
The subtraction of one in the lower formula enforces strictness even at
a perfect-square boundary. The checker verifies the signed margin itself;
it does not rely on the generation rule to accept a witness.

### Complete table for n=45

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 10 | 45 | 715 | 88200 | 90045000 |
| 27 | 28 | 925 | 88506 | 127946250 |
| 10 | 44 | 708 | 87920 | 71130880 |
| 11 | 43 | 734 | 87953 | 85206468 |
| 12 | 42 | 757 | 87984 | 19143216 |
| 13 | 41 | 779 | 88013 | 109896933 |
| 14 | 40 | 798 | 88040 | 64224160 |
| 15 | 39 | 816 | 88065 | 138608640 |
| 16 | 38 | 831 | 88088 | 30137368 |
| 17 | 37 | 845 | 88109 | 12028725 |
| 18 | 36 | 858 | 88128 | 76660992 |
| 19 | 35 | 869 | 88145 | 63666345 |
| 20 | 34 | 879 | 88160 | 116030560 |
| 21 | 33 | 887 | 88173 | 71783037 |
| 22 | 32 | 894 | 88184 | 79827424 |
| 23 | 31 | 900 | 88193 | 136330000 |
| 24 | 30 | 904 | 88200 | 78451200 |
| 25 | 29 | 907 | 88205 | 61755045 |
| 26 | 28 | 909 | 88208 | 84594448 |
| 11 | 45 | 748 | 88515 | 24496560 |
| 12 | 44 | 773 | 88548 | 109997892 |
| 13 | 43 | 795 | 88579 | 84142475 |
| 14 | 42 | 815 | 88608 | 55648800 |
| 15 | 41 | 833 | 88635 | 2851515 |
| 16 | 40 | 850 | 88660 | 56850000 |
| 17 | 39 | 865 | 88683 | 54837675 |
| 18 | 38 | 879 | 88704 | 136347264 |
| 19 | 37 | 891 | 88723 | 135503963 |
| 20 | 36 | 901 | 88740 | 39220740 |
| 21 | 35 | 911 | 88755 | 159638355 |
| 22 | 34 | 918 | 88768 | 6924032 |
| 23 | 33 | 925 | 88779 | 61531875 |
| 24 | 32 | 931 | 88788 | 157975668 |
| 25 | 31 | 935 | 88795 | 126808875 |
| 26 | 30 | 938 | 88800 | 130147200 |
| 27 | 29 | 940 | 88803 | 166330800 |

### Complete table for n=46

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 10 | 46 | 721 | 88480 | 4468320 |
| 10 | 45 | 714 | 88200 | 35992800 |
| 11 | 44 | 740 | 88234 | 83061600 |
| 12 | 43 | 764 | 88266 | 79488864 |
| 13 | 42 | 786 | 88296 | 51084384 |
| 14 | 41 | 806 | 88324 | 21549936 |
| 15 | 40 | 824 | 88350 | 12470400 |
| 16 | 39 | 840 | 88374 | 43305600 |
| 17 | 38 | 854 | 88396 | 131382864 |
| 18 | 37 | 867 | 88416 | 138665376 |
| 19 | 36 | 879 | 88434 | 72265806 |
| 20 | 35 | 889 | 88450 | 96107550 |
| 21 | 34 | 898 | 88464 | 62276544 |
| 22 | 33 | 905 | 88476 | 135944100 |
| 23 | 32 | 912 | 88486 | 2300416 |
| 24 | 31 | 916 | 88494 | 148578336 |
| 25 | 30 | 920 | 88500 | 93600000 |
| 26 | 29 | 923 | 88504 | 875784 |
| 27 | 28 | 924 | 88506 | 35701344 |
| 11 | 46 | 754 | 88796 | 118053264 |
| 12 | 45 | 779 | 88830 | 94313970 |
| 13 | 44 | 802 | 88862 | 43606152 |
| 14 | 43 | 822 | 88892 | 137097872 |
| 15 | 42 | 841 | 88920 | 108573480 |
| 16 | 41 | 858 | 88946 | 121156856 |
| 17 | 40 | 874 | 88970 | 37952280 |
| 18 | 39 | 888 | 88992 | 25892352 |
| 19 | 38 | 900 | 89012 | 100280000 |
| 20 | 37 | 911 | 89030 | 112133370 |
| 21 | 36 | 921 | 89046 | 67531914 |
| 22 | 35 | 929 | 89060 | 137568540 |
| 23 | 34 | 936 | 89072 | 164377088 |
| 24 | 33 | 942 | 89082 | 151840152 |
| 25 | 32 | 947 | 89090 | 103286190 |
| 26 | 31 | 951 | 89096 | 21488504 |
| 27 | 30 | 953 | 89100 | 78578100 |
| 28 | 29 | 954 | 89102 | 106844168 |

## 5. Exact analytic arcsine and pi bounds

For `0<u<=1/5`, put `t=u^2`. The exact polynomial identity

```text
(1+3u^2/5)^2(1-u^2)-1 = u^2(5-21u^2-9u^4)/25
```

is positive: `5-21t-9t^2` decreases for `t>=0`, and at `t=1/25` it
equals `2591/625>0`. Both compared quantities are positive, so taking
square roots and dividing by `sqrt(1-u^2)>0` gives
`1/sqrt(1-u^2)<1+3u^2/5`. Integrating the strict inequality over the
positive interval and using the increasing polynomial yields

```text
asin(s) < s+s^3/5 < u+u^3/5  for 0<s<u<=1/5.           (4)
```

Also `asin(s)>s` for `0<s<1`, since its integrand `1/sqrt(1-t^2)`
is strictly greater than one for t>0.

For exact bounds on pi, let `a=atan(1/5)` and `b=atan(1/239)`.
The tangent identities give

```text
tan(2a)=5/12, tan(4a)=120/119,
tan(4a-b)=(120/119-1/239)/(1+(120/119)(1/239))=1.
```

The branches are fixed as follows: `0<b<a<pi/4`, so `0<2a<pi/2`;
`tan(2a)<1` then implies `2a<pi/4`. Thus `0<4a-b<pi/2`, proving
`pi=16 atan(1/5)-4 atan(1/239)`.

For `0<x<1`, define `A_m(x)=sum_{j=0}^{m-1} (-1)^j x^(2j+1)/(2j+1)`.
The exact finite identity

```text
1/(1+t^2) = sum_{j=0}^{m-1} (-1)^j t^(2j)
            + (-1)^m t^(2m)/(1+t^2)
```

has an integral remainder of strict sign `(-1)^m`. Consequently even
partial sums are below atan and odd partial sums above it. In particular,

```text
L_pi = 16 A_2(1/5)-4 A_1(1/239) = 281476/89625 < pi,
L_pi-157/50 = 107/179250 > 0,

U_pi = 16 A_3(1/5)-4 A_2(1/239)
     = 670143059704/213311234375 > pi,
22/7-U_pi = 1845738322/1493178640625 > 0.
```

This proves, without decimal constants,

```text
157/50 < pi < 22/7.                                    (5)
```

## 6. Both complete chain gates

For all 36 upper-table rows, (4) gives

```text
C_{10,45}(270)/2 = sum_e asin(s_e)
  < sum_e (u_e+u_e^3/5)
  = 15404369802693/5000000000000
  = 157/50-295630197307/5000000000000
  < 157/50 < pi.
```

The sum is strictly decreasing in R and equals pi at its chain root;
therefore

```text
R_{10,45} < 270.                                       (6)
```

For all 37 lower-table rows, `asin(s_e)>s_e>u_e`, so

```text
C_{10,46}(270)/2 = sum_e asin(s_e)
  > sum_e u_e = 8011/2500
  = 22/7+1077/17500
  > 22/7 > pi.
```

Hence

```text
270 < R_{10,46}.                                       (7)
```

Equations (2), (3), (6), (7) close all four gates of (1).

## 7. All-integer deduction solely through the fixed-k theorem

For `41<=n<=45`, opposing root/threshold monotonicities give

```text
R_{10,n} <= R_{10,45} < 270 < T_{10,45} <= T_{10,n}.
```

The sign criterion yields `Delta_{10,n}>0`. The no-threshold part of the
same theorem covers `12<=n<=40`. For every integer `n>=46`,

```text
T_{10,n} <= T_{10,46} < 270 < R_{10,46} <= R_{10,n},
```

and the deficit is negative. Thus `s_10=46`, with no equality case anywhere
on `n>=12`. No monotonicity of the raw angular deficit, no finite scan and
no eventual-onset formula is used for this deduction.

## 8. Reproduction and independence

The dossier `ops/TASK-20260904__radius10_seam_onset/` contains:

- `check_seam.py`: stdlib/Fraction arithmetic, explicit exceptions active
  under `-O`, both cycle constructions, all signs, identities, 73 witnesses
  and complete sums. `--tables` reproduces the tables. Its analytic checks
  are adapted from the radius-9 checker with newly constructed endpoints
  and witnesses; it imports no earlier checker or production code.
- `score_witnesses.py`: separate integer-only scorer. It reads literals
  without executing the checker, reconstructs every witness with isqrt,
  verifies note tables/tours, coverage, integer cross-products and sums.
- `check_mutations.py`: task-local rejection tests for incomplete cycles,
  multiplicity, witness strictness, pre-square signs, threshold direction,
  analytic-bound domains, aggregate failure and transcription tampering.

The finite checks do not reprove the imported fixed-k theorem or constitute
a full geometric certificate. The proof is subject to independent review;
the exact commands, provenance and limitations are recorded in EVIDENCE.md.
