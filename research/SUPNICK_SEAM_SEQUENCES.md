# Exact monotonicity of the two Supnick seam sequences

```text
status=PROVED
domain=integers k >= 6, c in {5,6}
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## Result and dependencies

Use the definitions in [the fixed-k theorem](FIXED_K_SUPNICK_SEAM.md).
For the chain-minimizing Supnick cycle on `{k,...,n}`, `R_{k,n}` is its
unique adjacent-chain closure root, and `T_{k,n}` is the positive Descartes
threshold for the formal seam `(n,k,n-1)`. Define

```text
D_c(k) = R_{k,4k+c} - T_{k,4k+c},       c=5,6.
```

**Exact theorem.** For every integer `k>=6`,

```text
D_5(k+1) < D_5(k),
D_6(k+1) > D_6(k).                                      (1)
```

**Proved corollary.** The [already proved radius-6 bridge](RADIUS6_SEAM_ONSET.md)
gives `D_5(6)<0<D_6(6)`. Therefore (1), followed by fixed-k persistence,
proves

```text
s_k = 4k+6                       for every integer k>=6. (2)
```

More precisely, the formal angular seam deficit is strictly positive for
`k+2<=n<=4k+5` and strictly negative for `n>=4k+6`, with no equality case.
Together with the prior radius-1 through radius-5 notes, this classifies
every positive integer radius index: `s_1=8`, `s_2=13`, `s_3=17`,
`s_4=21`, `s_5=25`, and (2).

The proof below compares consecutive implicit roots through exact closure
bounds and a differentiable comparison function. It uses the exact
rationalized threshold identity from section 5 of
[the effective-onset note](EVENTUAL_SUPNICK_SEAM_ONSET.md), but none of that
note's asymptotic estimates, limiting separators or cutoff. The small
high-precision diagnostic in the dossier is not a premise.

This is exclusively a formal-seam result. It does not prove full geometric
feasibility before onset, determine `R*(n)`, classify global contact graphs,
or prove floating behavior in any or every global optimum. The published
paper and existing global certificates are unchanged.

## 1. Both closure parities, including their change at each step

Put `n=4k+c`, `N=3k+c+1`, `L=n+k=5k+c`, `d=n-k=3k+c`, and

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

The imported closure function `C_{k,n}` sums `theta` over these edges.
For `N=2h`, its edges are

```text
(k,n), (k+h-1,k+h),
(i,L-1-i), k<=i<=k+h-2,
(i,L+1-i), k+1<=i<=k+h-1.                               (3)
```

For `N=2h+1`, they are

```text
(k,n),
(i,L-1-i), k<=i<=k+h-1,
(i,L+1-i), k+1<=i<=k+h.                                 (4)
```

| Offset | k even | k odd | Change when k increases by 1 |
|---|---|---|---|
| 5 | (3), N even | (4), N odd | N increases by 3; parity flips |
| 6 | (4), N odd | (3), N even | N increases by 3; parity flips |

All endpoint sums are `L-1,L,L+1`. Define the **exact edge-weight sum**

```text
S = sum_{(a,b) in E_{k,n}} sqrt(ab),
w(x) = sqrt(x(L-x)),    w_0 = sqrt(kn),
J = integral_k^n w(x) dx,    F = J+w_0.
```

Here and below integrals are exact analytic objects, not quadrature output.
Symmetrizing each long sum in (3)-(4) gives the identity

```text
S = w_0 + sum_{x=k+1/2,k+3/2,...,n-1/2}
          [g_x(-1/2)+g_x(1/2)]/2 - epsilon_N,
g_x(m) = sqrt((x+m)(L-x+m)),

epsilon_N = 0                              if N is odd,
epsilon_N = (L-sqrt(L^2-1))/2               if N is even. (5)
```

To verify the central correction explicitly: when `N` is even, `L` is odd,
and the two symmetrized long sums include half of each diagonal term at
`p=(L-1)/2` and `p+1`. Their total is `L/2`; the actual central edge has
weight `sqrt(p(p+1))=sqrt(L^2-1)/2`. When `N` is odd, both reflection axes
are half-integral, so there are no diagonal terms or central correction.
The seam edge `(k,n)` remains in both cases. This accounts for the entire
parity change, rather than interpolating a parity-specific edge sum.

## 2. A uniform exact enclosure for the edge sum

For `k>=6` and `c=5,6`, we have `d<=4k`, `L<=6k`, `n-1>=4k` and
`w(x)>=sqrt(kn)>=2k` on `[k,n]`. Direct differentiation gives

```text
w''(x) = -L^2/(4w(x)^3),
|w''(x)| <= 9/(8k).
```

The unit-mesh midpoint bound (Taylor's formula integrated on each cell)
and concavity give

```text
0 <= sum w(x) - J <= d sup|w''|/24 <= 3/16.              (6)
```

For each midpoint in (5) and `|m|<=1/2`,

```text
g_x''(m) = -(L-2x)^2/(4g_x(m)^3),
g_x(m)^2 >= k(n-1),    |L-2x| <= d-1 < 4k.
```

Thus `|g_x''(m)|<1/(2k)`. Taylor's formula at the two endpoints of the
m interval, or its integral remainder, yields

```text
0 <= w(x)-[g_x(-1/2)+g_x(1/2)]/2 < 1/(16k).
```

Summing the `d` terms costs less than `1/4`. Also

```text
0 <= epsilon_N < 1/(2L) <= 1/60.
```

Together with (5)-(6), this proves, for both parities,

```text
F-4/15 < S < F+3/16.                                    (7)
```

The upper bound is strict because `w(x)>2k`, making the derivative bound
used in (6) strict. These are absolute bounds valid at every stated index;
no limiting or effective-tail estimate is being imported.

## 3. Comparing the actual implicit root with the edge sum

Write `R=R_{k,n}`, `X=S/pi` and `Q=R+L/2`. The closure equation is
`C_{k,n}(R)/2=pi`. Since every edge has endpoint sum at most `L+1`,
the arithmetic-geometric mean inequality and `asin z>z` give

```text
pi > S/(Q+1/2),    hence    Q > X-1/2.                   (8)
```

For the upper comparison we first prove

```text
12X+9 > (L-1)^2.                                        (9)
```

On each half of `[k,n]`, the concave graph of `w` lies above the chord
joining its endpoint value `w_0` to its central value `L/2`. Therefore

```text
J >= d(w_0+L/2)/2.
```

The positive square comparison `kn-(2k+c/5)^2=c(5k-c)/25>0` gives
`w_0>2k+c/5`, so

```text
J > P := (27/4)k^2+(33/10)ck+(7/20)c^2.
```

By (7), `S>J`, since `w_0>4/15`. Using `pi<22/7` (certified in section 5),
`X>7P/22`. The exact coefficient identity

```text
12(7P/22)-(5k+c-1)^2+9
  = (17/22)k^2+(13/5)ck+(37/110)c^2+10k+2c+8 > 0
```

proves (9). It also follows that `X>(189/88)k^2>L/2` on this domain.

Now evaluate the closure at the positive trial radius
`R_0=X+2-L/2`. For an edge with `s=a+b`, the exact positive-branch identity is

```text
theta_{R_0}(a,b)/2 = atan(sqrt(ab)/sqrt(R_0(R_0+s))).
```

Since `s>=L-1`, `atan z<z`, and (9) implies

```text
R_0(R_0+L-1) = (X+3/2)^2-(L-1)^2/4 > X^2,
```

we obtain `C_{k,n}(R_0)/2<S/X=pi`. Strict decrease of the closure implies
`R<R_0`. Combined with (8),

```text
X-L/2-1/2 < R_{k,n} < X-L/2+2.                          (10)
```

Define the exact comparison function, extending only its explicit terms
to real `k>=6`,

```text
V_c(k) = F(k,4k+c)/pi - (5k+c)/2 - T_{k,4k+c}.
```

Equations (7) and (10) give

```text
a < D_c(k)-V_c(k) < b,
a = -1/2-4/(15pi),    b = 2+3/(16pi),
b-a = 5/2+109/(240pi) < 1909/720 < 8/3.                 (11)
```

Only `pi>3` is used in the last bound. Thus to compare the actual roots
at consecutive indices, it suffices to prove

```text
V_5'(k)<-8/3,    V_6'(k)>8/3              for real k>=6. (12)
```

This is a unit-step comparison with an explicit error smaller than the
step margin. It makes no assumption that either parity-specific root has
a differentiable interpolation.

## 4. Exact derivative bounds for the rationalized threshold

Put `t=1/k`, so `0<t<=1/6`. Import just the exact rationalization

```text
A=4+ct, B=4+(c-1)t, G=9+(2c-1)t,
U=AB+A+B, Z=ABG,
H=32(2c-1)+[48c(c-1)+9]t+6c(c-1)(2c-1)t^2+c^2(c-1)^2t^3,
U^2-4Z=tH,
T_{k,4k+c}=k^2 f_c(t),    f_c(t)=AB(U+2sqrt(Z))/H.       (13)
```

All relevant denominators and radicals are positive. The following
uniform derivative bounds will be proved by exact polynomial gates:

```text
2a_c k+b_c-1/8 < dT_{k,4k+c}/dk < 2a_c k+b_c+1/8,
(a_5,b_5)=(8/3,61/36),
(a_6,b_6)=(24/11,2447/1452).                             (14)
```

These rational constants are comparison coefficients; no series
approximation to the threshold is needed. Here is a completely rational
certificate specification, including the signs before squaring. A prime
in the rest of this section denotes polynomial differentiation in `t`.
Set

```text
P_0=ABU, J_0=2AB,
P_1=2HP_0-tHP_0'+tH'P_0,
J_1=2HJ_0-tHJ_0'+tH'J_0,
den=2ZH^2,
num_r=2ZP_1,
num_s=2ZJ_1-tHJ_0 Z'.
```

Direct differentiation of (13) gives the exact identity

```text
2f_c-t f_c' = (num_r+num_s sqrt(Z))/den,
dT/dk = (2f_c-t f_c')/t.                                (15)
```

For `q=-1,+1`, define

```text
M_q=[2a_c+(b_c+q/8)t]den-num_r,
W_q=q[M_q^2-num_s^2 Z].                                 (16)
```

The gates are `num_s>0`, `M_-1>0`, `M_+1>0`, `W_-1>0`, `W_+1>0`.
With these positive pre-square signs, (16) is equivalent to (14).

For reproducibility, the finite polynomial certificates use this rule.
For `p(t)=sum_{i=0}^m p_i t^i`, define the exact rational coefficients

```text
B_j(p)=sum_{i=0}^j p_i 6^(-i) binom(m-i,j-i),  0<=j<=m.
```

Then

```text
(1+y)^m p(y/[6(1+y)]) = sum_{j=0}^m B_j(p)y^j.          (17)
```

Every coefficient in each row below is positive, except for the stated
constant zeros. Thus all gates are strict on `0<t<1/6`. The closed endpoint
is included because `p(1/6)=B_m(p)>0`.

| c | Polynomial | Degree | Positive coefficients | Zero coefficients |
|---|---|---:|---:|---|
| 5 and 6 | num_s | 8 | 9 | none |
| 5 and 6 | M_-1 | 10 | 11 | none |
| 5 and 6 | M_+1 | 10 | 11 | none |
| 5 and 6 | W_-1 | 20 | 20 | B_0 only |
| 5 and 6 | W_+1 | 20 | 20 | B_0 only |

The independent stdlib/Fraction checker reconstructs every polynomial
from (13)-(16), verifies the conjugate identity, computes **every**
coefficient in (17), checks the closed endpoint and rejects a zero
polynomial or a reversed margin. No floating-point signs or samples in
`k` enter these gates. This proves (14).

## 5. Exact derivative bounds for the integral comparison

Leibniz differentiation of `J`, using symmetry about `L/2`, gives

```text
dF/dk = 3sqrt(kn)+(5L/2)asin((n-k)/L)+(8k+c)/(2sqrt(kn)). (18)
```

Set `x=c/k`, so `0<x<=1`, and define

```text
A_0(x)=3sqrt(4+x)+(5(5+x)/2)asin((3+x)/(5+x)),
B_0(x)=(8+x)/(2sqrt(4+x)).
```

Thus `F'=k A_0(x)+B_0(x)`. With `u=asin(3/5)=atan(3/4)`,

```text
A_0(0)=6+(25/2)u,    A_0'(0)=2+(5/2)u,    B_0(0)=2,
0 <= A_0''(x)=x/[2(5+x)(4+x)^(3/2)] <= x/80,
0 <= B_0'(x)=x/[4(4+x)^(3/2)] <= x/32.
```

Integrating these inequalities with their exact values at zero gives

```text
F'/pi = alpha k+beta c+gamma+e,
alpha=[6+(25/2)u]/pi, beta=[2+(5/2)u]/pi, gamma=2/pi,
0 <= e <= [c^3/480+c^2/64]/(pi k^2) < 3/320.            (19)
```

These are Taylor bounds with signed, explicit integral remainders valid
on the entire interval, rather than formal expansions.

For clarity, all transcendental constants used here have finite rational
certificates. Write

```text
S_m(z)=sum_{j=0}^{m-1} (-1)^j z^(2j+1)/(2j+1).
```

The finite geometric identity for `1/(1+z^2)`, integrated from 0, proves
`S_{2r}(z)<atan z<S_{2r+1}(z)` for `0<z<1`, with the remainder sign fixed
by the next term. Use

```text
u_lo=S_24(3/4),    u_hi=S_25(3/4),
pi_lo=16 S_10(1/5)-4 S_3(1/239),
pi_hi=16 S_11(1/5)-4 S_2(1/239).
```

Machin's identity follows here from
`tan(2 atan(1/5))=5/12`, `tan(4 atan(1/5))=120/119`, and
`tan(4 atan(1/5)-atan(1/239))=1`. Its argument is positive and less than
`4/5<1<pi/2`, so it is `pi/4`, with no branch ambiguity. The elementary
`pi/2>1` follows by integrating `(1-z^2)^(-1/2)>1` on `(0,1)`.
The positive branch also gives `asin(3/5)=atan(3/4)`.

The exact checker evaluates these rational sums and verifies

```text
3 < pi_lo < pi < pi_hi < 22/7,
447/100 < alpha < 4471/1000,
287/250 < beta < 1149/1000,
159/250 < gamma < 637/1000.                              (20)
```

Finally combine `V_c'=F'/pi-5/2-T'` with (14), (19), and (20).
For `c=5` the upper affine bound has slope
`4471/1000-16/3<0`; its value at `k=6` is exactly

```text
6(4471/1000-16/3)+5(1149/1000)+637/1000+3/320
  -5/2-61/36+1/8
  = -205349/72000
  = -8/3-13349/72000.                                   (21)
```

For `c=6` the lower affine bound has slope
`447/100-48/11=117/1100>0`; its value at `k=6` is exactly

```text
6(447/100-48/11)+6(287/250)+159/250
  -5/2-2447/1452-1/8
  = 1398247/363000
  = 8/3+430247/363000.                                  (22)
```

These strictly signed rational margins prove (12) for every real `k>=6`.

## 6. Consecutive-root comparison and the onset corollary

Let `E_c(k)=D_c(k)-V_c(k)`. By (11), `a<E_c(k)<b` independently of
parity, and `b-a<8/3`. Integrating (12) over `[k,k+1]` gives

```text
D_5(k+1)-D_5(k)
  = V_5(k+1)-V_5(k)+E_5(k+1)-E_5(k)
  < -8/3+(b-a) < 0,

D_6(k+1)-D_6(k)
  > 8/3-(b-a) > 0.                                     (23)
```

Equivalently, (23) compares the next implicit chain root to
`R_{k,4k+c}+[T_{k+1,4k+4+c}-T_{k,4k+c}]`, below it for `c=5` and above
it for `c=6`. Thus the threshold increment is included exactly. The
enclosure (10) came from strict evaluations of the actual closure
function, and (5) retained the parity correction at both endpoints.
This proves both all-k inequalities, not just their eventual versions.

Only now import the radius-6 bridge:

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30}.
```

Induction using (23) gives `D_5(k)<0<D_6(k)` for every integer `k>=6`.
For each fixed k, the fixed-k theorem says that `R_{k,n}-T_{k,n}` is
strictly increasing on `n>=4k+1`, and that the seam deficit is positive
through `n=4k`. Its exact sign equivalence gives precisely (2), including
the strict sign ranges and absence of equality stated above.

## 7. Verification and limitations

The exact gate checker is
`ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py`.
It imports neither the production package nor the diagnostic, performs
no root evaluations or scan over k, and uses only integer/Fraction
arithmetic. It audits all ten threshold polynomials, the rational
constants and final margins, and checks four complete rank-tour/parity
representations (104 edges) including the even central correction.
Those four construction checks are corroboration; the general parity
identity is proved by symmetrization in section 1.

The analytic inequalities and imported fixed-k theorem remain mathematical
proof dependencies requiring review; this checker is not a proof assistant.
The dossier records normal/optimized exact runs, rejection checks, a
separate symbolic differentiation audit, and the existing radius-6 exact
bridge check. No finite diagnostic supplies a premise of (1) or (2), and
no radius-by-radius onset artifacts were generated.
