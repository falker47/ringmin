# Exact radius-9 Supnick seam onset

```text
status=PROVED
domain=integers n >= 11
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

Let `sigma*_{9,n}` be the chain-minimizing Supnick cycle on `{9,...,n}`,
put `R_{9,n}=R_chain(sigma*_{9,n})`, and define

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))),
Delta_{9,n} = theta_{R_{9,n}}(n,9) + theta_{R_{9,n}}(9,n-1)
             - theta_{R_{9,n}}(n,n-1).
```

The exact endpoint bridge is

```text
R_{9,41} < 220 < T_{9,41},
T_{9,42} < 220 < R_{9,42}.                              (1)
```

Only after proving all four inequalities below, the fixed-k theorem gives

```text
Delta_{9,n} > 0   for 11 <= n <= 41,
Delta_{9,n} < 0   for every integer n >= 42,
s_9 = 42.
```

**Classification:** exact theorem / proved corollary. This is exclusively a
formal-seam statement. It does not establish full fixed-order feasibility
before the onset, determine `R*(n)`, classify a global contact graph, or
assert floating of circle 9 in any or every global optimum. The global
certification scope remains `3<=n<=14`; arXiv-v1 assets are unchanged.

The review suggested the endpoints and integer separator. Every witness
here is reconstructed from the exact formulas. No scan, floating root,
previous numerical diagnostic, or reviewer pre-check is a proof premise.

## 1. Imported reduction

Use `research/FIXED_K_SUPNICK_SEAM.md`, sections 1-5. If `C_{9,n}(R)`
is the complete adjacent-angle sum, it is continuous and strictly decreasing
in `R>0`, with unique root `C_{9,n}(R_{9,n})=2*pi`. The chain roots
strictly increase with `n`. The no-threshold theorem gives positive deficit
on `11<=n<=36`. On `n>=37`, the physical minus-root threshold is

```text
kappa_{9,n} = 1/9 + 1/n + 1/(n-1)
              - 2 sqrt((2n+8)/(9n(n-1))),
T_{9,n} = 1/kappa_{9,n} > 0,
sign(Delta_{9,n}) = sign(T_{9,n}-R_{9,n}).
```

The thresholds strictly decrease with `n`. The imported proof establishes
the physical branch and excludes the extraneous plus root. Explicit
endpoint positivity and pre-square signs are also supplied next.

## 2. Threshold signs and directed square margins

Set `A_n=1/9+1/n+1/(n-1)`, `B_n=4(2n+8)/(9n(n-1))`, and
`H_n=A_n-1/220`, so `kappa_{9,n}=A_n-sqrt(B_n)`.
Every entry in this table is strictly positive:

| n | A_n | B_n | A_n^2-B_n | H_n | directed square margin |
|---:|---:|---:|---:|---:|---:|
| 41 | `2369/14760` | `1/41` | `298561/217857600` | `25321/162360` | `B_41-H_41^2 = 1792559/26360769600` |
| 42 | `823/5166` | `184/7749` | `43633/26687556` | `87947/568260` | `H_42^2-B_42 = 66953209/322919427600` |

First, `A_n>0`, `B_n>0`, and `A_n^2-B_n>0` imply
`A_n>sqrt(B_n)>0`. Thus both curvatures are positive, and reciprocal
comparisons are valid. For n=41, `H_41>0` and `B_41-H_41^2>0` give
`sqrt(B_41)>H_41`, hence

```text
0 < kappa_{9,41} < 1/220,     220 < T_{9,41}.           (2)
```

For n=42, `H_42>0` and `H_42^2-B_42>0` give
`H_42>sqrt(B_42)`, hence

```text
kappa_{9,42} > 1/220 > 0,     T_{9,42} < 220.           (3)
```

The sign checks precede the square comparisons; the direction of each
margin is essential.

## 3. Two complete edge representations

The shifted rank-arm construction from the fixed-k theorem gives

```text
sigma*_{9,41} =
 (9,40,11,38,13,36,15,34,17,32,19,30,21,28,23,26,25,
  24,27,22,29,20,31,18,33,16,35,14,37,12,39,10,41),

sigma*_{9,42} =
 (9,41,11,39,13,37,15,35,17,33,19,31,21,29,23,27,25,
  26,24,28,22,30,20,32,18,34,16,36,14,38,12,40,10,42).
```

Independently specialize the parity edge formulas, with undirected edges
normalized to `a<b`:

```text
E_{9,41} = {(9,41)}
           union {(i,49-i): 9<=i<=24}
           union {(i,51-i): 10<=i<=25},

E_{9,42} = {(9,42),(25,26)}
           union {(i,50-i): 9<=i<=24}
           union {(i,52-i): 10<=i<=25}.
```

The counts are `1+16+16=33` and `2+16+16=34`. Each displayed tour
contains every radius once. Reading all cyclic adjacencies, including the
last-to-first edge, gives exactly the corresponding edge family, with no
duplicates. Each vertex has degree two and both seam edges `(9,n-1)` and
`(9,n)` occur. The checker compares complete multisets and also all 134
rotations/reflections of these two tours; the two constructions share no
edge-generation implementation.

## 4. Complete rational sine witnesses at R=220

For each edge put

```text
D=10000, Q_e=(220+a)(220+b), s_e=sqrt(ab/Q_e), u_e=m_e/D.
```

Since `Q_e-ab=220(220+a+b)>0`, every `s_e` lies strictly in `(0,1)`.
For n=41 the table records `M_e=m_e^2 Q_e-D^2 ab>0`, so `s_e<u_e`.
For n=42 it records `M_e=D^2 ab-m_e^2 Q_e>0`, so `u_e<s_e`.
The corresponding directed rational square margin is `M_e/(D^2 Q_e)`.
All bounds are positive. The upper bounds satisfy
`u_e<=1039/10000<1/5`, with domain margin `961/10000>0`.

These integers can be reconstructed without real-number square roots:

```text
n=41: m_e = isqrt((D^2 ab)//Q_e)+1,
n=42: m_e = isqrt((D^2 ab-1)//Q_e).
```

Here `//` is integer floor division and `isqrt(v)` is the largest integer
whose square is at most v. Subtracting one in the lower construction keeps
the bound strict even when the sine is rational: at `(20,30)` it is exactly
`1/10`, and the valid witness is `999/10000`. The candidate `1000/10000`
has zero square margin and is explicitly rejected by the checker tests.

### Complete table for n=41

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 9 | 41 | 786 | 59769 | 25049124 |
| 9 | 40 | 778 | 59540 | 38609360 |
| 10 | 39 | 810 | 59570 | 83877000 |
| 11 | 38 | 838 | 59598 | 52337912 |
| 12 | 37 | 863 | 59624 | 6106856 |
| 13 | 36 | 886 | 59648 | 23441408 |
| 14 | 35 | 907 | 59670 | 87465830 |
| 15 | 34 | 925 | 59690 | 72256250 |
| 16 | 33 | 941 | 59708 | 70299548 |
| 17 | 32 | 955 | 59724 | 69781100 |
| 18 | 31 | 967 | 59738 | 60346682 |
| 19 | 30 | 977 | 59750 | 33107750 |
| 20 | 29 | 986 | 59760 | 98432960 |
| 21 | 28 | 992 | 59768 | 15537152 |
| 22 | 27 | 997 | 59774 | 15893966 |
| 23 | 26 | 1001 | 59778 | 97615778 |
| 24 | 25 | 1002 | 59780 | 19359120 |
| 10 | 41 | 827 | 60030 | 56257870 |
| 11 | 40 | 856 | 60060 | 8124160 |
| 12 | 39 | 883 | 60088 | 49952632 |
| 13 | 38 | 907 | 60114 | 52721986 |
| 14 | 37 | 929 | 60138 | 101559658 |
| 15 | 36 | 948 | 60160 | 66032640 |
| 16 | 35 | 965 | 60180 | 41120500 |
| 17 | 34 | 980 | 60198 | 14159200 |
| 18 | 33 | 994 | 60214 | 93599704 |
| 19 | 32 | 1005 | 60228 | 31785700 |
| 20 | 31 | 1015 | 60240 | 60754000 |
| 21 | 30 | 1023 | 60250 | 53372250 |
| 22 | 29 | 1029 | 60258 | 3640978 |
| 23 | 28 | 1034 | 60264 | 31617184 |
| 24 | 27 | 1037 | 60268 | 10338892 |
| 25 | 26 | 1039 | 60270 | 62730670 |

### Complete table for n=42

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 9 | 42 | 793 | 59998 | 70317698 |
| 25 | 26 | 1038 | 60270 | 62450120 |
| 9 | 41 | 785 | 59769 | 68847975 |
| 10 | 40 | 817 | 59800 | 84157800 |
| 11 | 39 | 846 | 59829 | 79427436 |
| 12 | 38 | 872 | 59856 | 86455296 |
| 13 | 37 | 896 | 59881 | 26575104 |
| 14 | 36 | 917 | 59904 | 27385344 |
| 15 | 35 | 935 | 59925 | 112066875 |
| 16 | 34 | 952 | 59944 | 72513024 |
| 17 | 33 | 967 | 59961 | 31128471 |
| 18 | 32 | 979 | 59976 | 116542584 |
| 19 | 31 | 990 | 59989 | 104781100 |
| 20 | 30 | 999 | 60000 | 119940000 |
| 21 | 29 | 1007 | 60009 | 47933559 |
| 22 | 28 | 1013 | 60016 | 13441296 |
| 23 | 27 | 1017 | 60021 | 20939931 |
| 24 | 26 | 1019 | 60024 | 73419336 |
| 10 | 42 | 834 | 60260 | 85795440 |
| 11 | 41 | 864 | 60291 | 93009664 |
| 12 | 40 | 892 | 60320 | 5547520 |
| 13 | 39 | 916 | 60347 | 65487568 |
| 14 | 38 | 938 | 60372 | 82058032 |
| 15 | 37 | 958 | 60395 | 71643220 |
| 16 | 36 | 976 | 60416 | 49168384 |
| 17 | 35 | 992 | 60435 | 28092160 |
| 18 | 34 | 1006 | 60452 | 20399728 |
| 19 | 33 | 1018 | 60467 | 36596692 |
| 20 | 32 | 1028 | 60480 | 85703680 |
| 21 | 31 | 1037 | 60491 | 49853821 |
| 22 | 30 | 1044 | 60500 | 58872000 |
| 23 | 29 | 1049 | 60507 | 118036693 |
| 24 | 28 | 1053 | 60512 | 103749792 |
| 25 | 27 | 1056 | 60515 | 17544960 |

## 5. Strict elementary arcsine and pi bounds

For `0<u<=1/5`, the exact identity

```text
(1+3u^2/5)^2(1-u^2)-1 = u^2(5-21u^2-9u^4)/25
```

is positive: `5-21t-9t^2` decreases for `t>=0` and equals
`2591/625>0` at `t=1/25`. Since `1+3u^2/5` and
`1/sqrt(1-u^2)` are positive, the identity proves
`1/sqrt(1-u^2)<1+3u^2/5`. Integrate from zero; the inequality is
strict on the positive interval. The polynomial `u+u^3/5` increases, so

```text
asin(s) < s+s^3/5 < u+u^3/5  when 0<s<u<=1/5.          (4)
```

The same integral formula gives `asin(s)>s` for `0<s<1`.

To prove the pi bounds without a decimal constant, put
`a=atan(1/5)`, `b=atan(1/239)`. Exact tangent identities give

```text
tan(2a)=5/12, tan(4a)=120/119,
tan(4a-b)=(120/119-1/239)/(1+(120/119)(1/239))=1.
```

Here `0<b<a<pi/4`. Thus `0<2a<pi/2`, and `tan(2a)<1` implies
`2a<pi/4`. Consequently `0<4a-b<pi/2`, fixing the tangent branch:

```text
pi = 16 atan(1/5) - 4 atan(1/239).
```

For `0<x<1` define `A_m(x)=sum_{j=0}^{m-1} (-1)^j x^(2j+1)/(2j+1)`.
The finite geometric identity

```text
1/(1+t^2) = sum_{j=0}^{m-1} (-1)^j t^(2j)
            + (-1)^m t^(2m)/(1+t^2)
```

gives, after integration, a strictly positive remainder for even m and a
strictly negative remainder for odd m. Therefore

```text
L_pi = 16 A_2(1/5) - 4 A_1(1/239)
     = 281476/89625 < pi,
L_pi - 157/50 = 107/179250 > 0,

U_pi = 16 A_3(1/5) - 4 A_2(1/239)
     = 670143059704/213311234375 > pi,
22/7 - U_pi = 1845738322/1493178640625 > 0.
```

Hence, with explicit branches and signed remainders,

```text
157/50 < pi < 22/7.                                    (5)
```

## 6. Complete chain inequalities

Using all 33 upper-table rows in (4),

```text
C_{9,41}(220)/2 = sum_{e in E_{9,41}} asin(s_e)
  < sum_e (u_e+u_e^3/5)
  = 194613679989/62500000000
  = 157/50 - 1636320011/62500000000
  < 157/50 < pi.
```

Strict decrease in R and the defining equality at the chain root give

```text
R_{9,41} < 220.                                        (6)
```

For all 34 lower-table rows, `asin(s_e)>s_e>u_e` gives

```text
C_{9,42}(220)/2 = sum_{e in E_{9,42}} asin(s_e)
  > sum_e u_e = 32503/10000
  = 22/7 + 7521/70000
  > 22/7 > pi,
```

and therefore

```text
220 < R_{9,42}.                                        (7)
```

Equations (2), (3), (6), (7) prove all four gates in (1).

## 7. All-integer deduction, after the four gates

For `37<=n<=41`, the opposing monotonicities imply

```text
R_{9,n} <= R_{9,41} < 220 < T_{9,41} <= T_{9,n}.
```

The exact sign criterion gives `Delta_{9,n}>0`, and the no-threshold
theorem already covers `11<=n<=36`. For every integer `n>=42`,

```text
T_{9,n} <= T_{9,42} < 220 < R_{9,42} <= R_{9,n},
```

so `Delta_{9,n}<0`. Thus `s_9=42`; there is no equality case anywhere
on `n>=11`. No monotonicity of the raw angular deficits is assumed.

## 8. Reproduction and independence

`ops/TASK-20260904__radius9_seam_onset/check_seam.py` imports only stdlib
modules and evaluates only the two endpoints. It verifies both edge
representations, symmetry, threshold signs and margins, the arcsine
identity/domain, exact Machin/remainder identities, all 67 rational square
witnesses, and both complete sums. `--tables` prints the full tables above.
All gates remain active under `-O`.

The task-local `check_mutations.py` independently reconstructs each witness
using integer isqrt, checks integer cross-products and aggregate sums,
reads the note's complete tables/tours, and exercises targeted rejected
inputs. Its rejection tests are coupled to the checker; the integer scorer
uses no checker arithmetic. Neither script imports production code, earlier
checkers, numerical diagnostics or external packages. The mathematical
fixed-k theorem remains an explicit imported dependency, not something
these finite tests reprove. Commands, provenance, the rejected initial
zero-margin witness and limitations are in the accompanying dossier.
