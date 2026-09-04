# Exact radius-8 Supnick seam onset

```text
status=PROVED
domain=integers n >= 10
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

Let `sigma*_{8,n}` be the chain-minimizing Supnick cycle on `{8,...,n}`,
let `R_{8,n}=R_chain(sigma*_{8,n})`, and define

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))),
Delta_{8,n} = theta_{R_{8,n}}(n,8) + theta_{R_{8,n}}(8,n-1)
             - theta_{R_{8,n}}(n,n-1).
```

The exact classification is

```text
Delta_{8,n} > 0   for 10 <= n <= 37,
Delta_{8,n} < 0   for every integer n >= 38,
s_8 = 38.
```

**Classification:** exact theorem; a proved corollary of the fixed-`k`
theorem and the exact endpoint arithmetic below. The new bridge is

```text
R_{8,37} < 176 < T_{8,37},
T_{8,38} < 176 < R_{8,38}.                              (1)
```

This concerns the formal seam `(n,8,n-1)` at a chain root. It neither proves
full fixed-order feasibility before the onset, determines `R*(n)`,
classifies a global contact graph, nor asserts that radius `8` floats in
any or every global optimum. The finite global certification scope remains
`3<=n<=14`. The historical paper and publication assets are unchanged.

The earlier two-precision diagnostic nominated the endpoints and separator;
none of its numerical values, residuals or artifact fields is a premise.

## 1. Imported fixed-k reduction

We use `research/FIXED_K_SUPNICK_SEAM.md`, sections 1-5, without changing
or reproving it. Write `C_{8,n}(R)` for the full adjacent-angle sum of the
Supnick cycle. The imported facts are:

- `C_{8,n}` is continuous and strictly decreasing in `R>0`, with unique
  root `C_{8,n}(R_{8,n})=2*pi`.
- `R_{8,n}` strictly increases with `n`.
- `Delta_{8,n}>0` on the no-threshold range `10<=n<=32`.
- For `n>=33`, the physical minus-root threshold is positive and equals

  ```text
  kappa_{8,n} = 1/8 + 1/n + 1/(n-1)
                - 2 sqrt((2n+7)/(8n(n-1))),
  T_{8,n} = 1/kappa_{8,n}.
  ```

  It strictly decreases with `n`, and
  `sign(Delta_{8,n})=sign(T_{8,n}-R_{8,n})`.

The physical branch and rejection of the extraneous plus root are supplied
by that theorem. The endpoint positivity and sign gates are also checked
explicitly below before any squaring or reciprocal comparison.

## 2. Exact threshold gates at q=176

Set

```text
A_n = 1/8 + 1/n + 1/(n-1),
B_n = (2n+7)/(2n(n-1)),
H_n = A_n - 1/176,
kappa_{8,n} = A_n - sqrt(B_n).
```

All displayed entries in the following table are strictly positive:

| n | A_n | B_n | A_n^2-B_n | H_n | directed square margin |
|---:|---:|---:|---:|---:|---:|
| 37 | `479/2664` | `9/296` | `13657/7096896` | `10205/58608` | `B_37-H_37^2 = 297431/3434897664` |
| 38 | `1003/5624` | `83/2812` | `72425/31629376` | `21363/123728` | `H_38^2-B_38 = 4523113/15308617984` |

First `A_n>0`, `B_n>0` and `A_n^2-B_n>0` imply
`A_n>sqrt(B_n)`, so both curvatures are strictly positive.
At `n=37`, the positive sign gate `H_37>0` and
`B_37-H_37^2>0` imply `sqrt(B_37)>H_37`, hence

```text
0 < kappa_{8,37} < 1/176,
176 < T_{8,37}.                                        (2)
```

At `n=38`, `H_38>0` and `H_38^2-B_38>0` imply
`H_38>sqrt(B_38)`, hence

```text
kappa_{8,38} > 1/176 > 0,
T_{8,38} < 176.                                        (3)
```

Every comparison is a rational sign or rational quadratic comparison.

## 3. Complete chain witnesses

The shifted rank representatives from the fixed-`k` theorem are

```text
sigma*_{8,37} =
 (8,36,10,34,12,32,14,30,16,28,18,26,20,24,22,
  23,21,25,19,27,17,29,15,31,13,33,11,35,9,37),

sigma*_{8,38} =
 (8,37,10,35,12,33,14,31,16,29,18,27,20,25,22,23,
  24,21,26,19,28,17,30,15,32,13,34,11,36,9,38).
```

For independent edge accounting, specializing both parity formulas gives

```text
E_{8,37} = {(8,37),(22,23)}
           union {(i,44-i): 8<=i<=21}
           union {(i,46-i): 9<=i<=22},

E_{8,38} = {(8,38)}
           union {(i,45-i): 8<=i<=22}
           union {(i,47-i): 9<=i<=23}.
```

The unions contain respectively `2+14+14=30` and `1+15+15=31`
distinct undirected edges. Each cycle uses every radius once and includes
both seam edges and cyclic closure. The tables below follow the full cyclic
order, normalizing each edge to `a<b`.

At `R=176`, put

```text
D = 10000, Q_e = (176+a)(176+b),
s_e^2 = ab/Q_e, u_e = m_e/D.
```

At `n=37` the table records the positive integer
`M_e=m_e^2 Q_e-D^2 ab`, proving the strict upper square margin
`u_e^2-s_e^2=M_e/(D^2 Q_e)>0`.
At `n=38` it records `M_e=D^2 ab-m_e^2 Q_e`, proving
`s_e^2-u_e^2=M_e/(D^2 Q_e)>0`. No rounded decimals are used.

### Complete table for n=37

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 8 | 36 | 860 | 39008 | 50316800 |
| 10 | 36 | 956 | 39432 | 38324352 |
| 10 | 34 | 933 | 39060 | 1300340 |
| 12 | 34 | 1017 | 39480 | 33729720 |
| 12 | 32 | 991 | 39104 | 3295424 |
| 14 | 32 | 1065 | 39520 | 24572000 |
| 14 | 30 | 1036 | 39140 | 8805440 |
| 16 | 30 | 1102 | 39552 | 32107008 |
| 16 | 28 | 1070 | 39168 | 43443200 |
| 18 | 28 | 1129 | 39576 | 45192216 |
| 18 | 26 | 1093 | 39188 | 15905012 |
| 20 | 26 | 1147 | 39592 | 87591528 |
| 20 | 24 | 1107 | 39200 | 37600800 |
| 22 | 24 | 1155 | 39600 | 27390000 |
| 22 | 23 | 1134 | 39402 | 69238312 |
| 21 | 23 | 1110 | 39203 | 2016300 |
| 21 | 25 | 1152 | 39597 | 49337088 |
| 19 | 25 | 1101 | 39195 | 12218195 |
| 19 | 27 | 1139 | 39585 | 54451785 |
| 17 | 27 | 1083 | 39179 | 52618131 |
| 17 | 29 | 1117 | 39565 | 64815285 |
| 15 | 29 | 1055 | 39155 | 80493875 |
| 15 | 31 | 1085 | 39537 | 43944825 |
| 13 | 31 | 1015 | 39123 | 5492675 |
| 13 | 33 | 1043 | 39501 | 71123349 |
| 11 | 33 | 964 | 39083 | 19675568 |
| 11 | 35 | 988 | 39457 | 15713808 |
| 9 | 35 | 899 | 39035 | 48126035 |
| 9 | 37 | 920 | 39405 | 52392000 |
| 8 | 37 | 870 | 39192 | 64424800 |

### Complete table for n=38

| a | b | m_e | Q_e | M_e |
|---:|---:|---:|---:|---:|
| 8 | 37 | 869 | 39192 | 3730088 |
| 10 | 37 | 966 | 39618 | 30225592 |
| 10 | 35 | 944 | 39246 | 26476544 |
| 12 | 35 | 1028 | 39668 | 79492288 |
| 12 | 33 | 1003 | 39292 | 71894372 |
| 14 | 33 | 1078 | 39710 | 53644360 |
| 14 | 31 | 1050 | 39330 | 38675000 |
| 16 | 31 | 1117 | 39744 | 11848384 |
| 16 | 29 | 1085 | 39360 | 64424000 |
| 18 | 29 | 1145 | 39770 | 60535750 |
| 18 | 27 | 1110 | 39382 | 77437800 |
| 20 | 27 | 1164 | 39788 | 91397952 |
| 20 | 25 | 1126 | 39396 | 50757104 |
| 22 | 25 | 1175 | 39798 | 53886250 |
| 22 | 23 | 1133 | 39402 | 20086022 |
| 23 | 24 | 1177 | 39800 | 63905800 |
| 21 | 24 | 1131 | 39400 | 1056600 |
| 21 | 26 | 1171 | 39794 | 32835646 |
| 19 | 26 | 1119 | 39390 | 77378210 |
| 19 | 28 | 1156 | 39780 | 40553920 |
| 17 | 28 | 1099 | 39372 | 46459028 |
| 17 | 30 | 1132 | 39758 | 53144608 |
| 15 | 30 | 1069 | 39346 | 36925694 |
| 15 | 32 | 1099 | 39728 | 16481872 |
| 13 | 32 | 1028 | 39312 | 55707392 |
| 13 | 34 | 1055 | 39690 | 24037750 |
| 11 | 34 | 975 | 39270 | 68956250 |
| 11 | 36 | 999 | 39644 | 35248356 |
| 9 | 36 | 908 | 39220 | 64521920 |
| 9 | 38 | 929 | 39590 | 32206810 |
| 8 | 38 | 878 | 39376 | 45671616 |

Because `Q_e-ab=176(176+a+b)>0`, every sine satisfies `0<s_e<1`.
All `m_e` are positive. At `n=37` the maximum is `1155`, so

```text
0 < s_e < u_e <= 231/2000 < 3/20 < 1,
3/20 - 231/2000 = 69/2000 > 0.                         (4)
```

At `n=38`, every row proves `0<u_e<s_e<1`.

## 4. Elementary arcsine and pi bounds

For `0<u<=3/20`, the exact polynomial identity is

```text
(1+21u^2/40)^2 (1-u^2) - 1
  = u^2(80-1239u^2-441u^4)/1600.
```

The polynomial `80-1239t-441t^2` strictly decreases for `t>=0` and
at `t=9/400` equals `8303879/160000>0`. Since both factors compared
before squaring are positive, this proves
`1/sqrt(1-u^2)<1+21u^2/40` for positive `u` in the domain.
Integrating from zero and using strict increase of `s+7s^3/40` gives

```text
asin(s) < s+7s^3/40 < u+7u^3/40   for 0<s<u<=3/20.      (5)
```

Also `asin(s)>s` for `0<s<1`, directly by the same integral formula.

For a self-contained exact comparison with `pi`, let
`a=atan(1/5)` and `b=atan(1/239)`. The exact tangent identities are

```text
tan(2a)=5/12, tan(4a)=120/119,
tan(4a-b)=(120/119-1/239)/(1+(120/119)(1/239))=1.
```

Since `0<b<a<pi/4`, we have `0<2a<pi/2`. Comparing its tangent
`5/12<1` gives `2a<pi/4` and thus `4a<pi/2`.
Consequently `0<4a-b<pi/2`, fixing the branch and proving

```text
pi = 16 atan(1/5) - 4 atan(1/239).
```

Define the rational finite sums

```text
A_m(x) = sum_{j=0}^{m-1} (-1)^j x^(2j+1)/(2j+1).
```

The exact finite geometric identity

```text
1/(1+t^2) = sum_{j=0}^{m-1} (-1)^j t^(2j)
            + (-1)^m t^(2m)/(1+t^2)
```

shows by integration on `0..x`, for `0<x<1`, that `A_m(x)` is
strictly below `atan(x)` for even `m` and strictly above it for odd `m`.
Therefore

```text
L_pi = 16 A_4(1/5) - 4 A_1(1/239)
     = 1231847548/392109375 < pi,
L_pi - 333/106 = 3418213/41563593750 > 0,

U_pi = 16 A_5(1/5) - 4 A_2(1/239)
     = 5277328977275528/1679825970703125 > pi,
22/7 - U_pi = 303439072246/239975138671875 > 0.
```

This proves, with the branches and remainder signs fixed,

```text
333/106 < pi < 22/7.                                  (6)
```

## 5. Exact chain-sum comparisons

Applying (5) to all 30 upper-table rows yields

```text
C_{8,37}(176)/2 = sum_{e in E_{8,37}} asin(s_e)
  < sum_e (u_e+7u_e^3/40)
  = 62794038854497/20000000000000
  = 333/106 - 1915940711659/1060000000000000
  < 333/106 < pi.
```

Strict decrease of `C_{8,37}` and its equality to `2*pi` at the root give

```text
R_{8,37} < 176.                                        (7)
```

For the complete 31-edge lower table, `asin(s_e)>s_e>u_e` gives

```text
C_{8,38}(176)/2 = sum_{e in E_{8,38}} asin(s_e)
  > sum_e u_e
  = 16459/5000
  = 22/7 + 5213/35000
  > 22/7 > pi.
```

The same strict-decrease argument gives

```text
176 < R_{8,38}.                                        (8)
```

Equations (2), (3), (7), and (8) close all four inequalities in (1).

## 6. All-integer conclusion

For `33<=n<=37`, the imported opposing monotonicities imply

```text
R_{8,n} <= R_{8,37} < 176 < T_{8,37} <= T_{8,n}.
```

The exact sign criterion gives `Delta_{8,n}>0` throughout that range;
the no-threshold theorem already covers `10<=n<=32`.
For every integer `n>=38`,

```text
T_{8,n} <= T_{8,38} < 176 < R_{8,38} <= R_{8,n},
```

so `Delta_{8,n}<0`. Hence `s_8=38`, with no equality case anywhere
in `n>=10`. This uses no numerical scan or monotonicity of the raw deficits.

## 7. Reproduction and independence

The standalone script
`ops/TASK-20260904__radius8_seam_onset/check_seam.py` uses only stdlib
integers and `fractions.Fraction`. It reconstructs the rank tours and both
parity edge families separately, checks complete edge multiplicities and
all rotations/reflections, then audits the threshold signs, square margins,
arcsine polynomial/domain, Machin identities/remainders, and rational sums.
Explicit exceptions keep the gates active under `python -O`. `--tables`
prints all 61 witness rows for direct comparison with this note.

The task-local `check_mutations.py` checks integer cross-products separately,
audits the note's complete tables, and rejects targeted invalid certificates.
It is coupled to the exact checker for rejection tests, but imports neither
production code nor the prior diagnostic. The checker imports no production
package, mpmath, numerical artifact, or earlier checker. Its all-`n`
conclusion still depends on the imported mathematical theorem; this is not
a new independent proof of Supnick optimality or of the general theorem.

Commands, output, provenance, mutation checks and regression results are in
`ops/TASK-20260904__radius8_seam_onset/EVIDENCE.md`.
