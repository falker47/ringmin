# Eventual formula for the first Supnick seam obstruction

```text
status=PROVED
domain=integers k sufficiently large
proved_on=2026-08-30
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For integers `k>=1` and `n>=k+2`, import the definitions from
`research/FIXED_K_SUPNICK_SEAM.md`: `R_{k,n}` is the adjacent-chain root of
the chain-minimizing Supnick cycle on `{k,...,n}`, `T_{k,n}` is the positive
Descartes seam threshold when `n>=4k+1`, `Delta_{k,n}` is the formal seam
deficit at `(n,k,n-1)`, and

```text
s_k = min {n >= k+2 : Delta_{k,n} < 0}.
```

This note proves the exact eventual identity

```text
s_k = 4k+6                         for every sufficiently large integer k.
                                                                    (1)
```

No finite scan is used. The proof treats only `n=4k+c` for `c=5,6`, and
proves, simultaneously across both parity subsequences,

```text
R_{k,4k+c}/k^2 -> rho,
rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx,             (2)

T_{k,4k+c}/k^2 -> 24/(2c-1).                              (3)
```

It then certifies exactly

```text
24/11 < rho < 8/3.                                        (4)
```

The phrase "sufficiently large" is qualitative: this task does not extract
or claim an effective cutoff. The result concerns one formal Supnick seam.
It does not prove full fixed-order feasibility below the obstruction,
determine `R*(n)`, classify a global contact graph, or imply that radius `k`
floats in any global optimum. It is post-arXiv-v1 work; the historical paper
and publication assets remain unchanged.

## 1. Parity-explicit closure sums at `n=4k+c`

Fix `c` in `{5,6}` and put

```text
n = 4k+c,
N = n-k+1 = 3k+c+1,
I = integral_1^(5/2) sqrt(x(5-x)) dx.
```

Let `C_{k,n}(R)` be the closure sum from the imported fixed-`k` theorem, so
that its unique root satisfies

```text
C_{k,n}(R_{k,n}) = 2pi.                                   (5)
```

The parity-explicit formulas in that theorem become the following. If
`N=2h`, where `h=(3k+c+1)/2`, then

```text
C_{k,n}(R)
  = theta_R(k,n) + theta_R(k+h-1,k+h)
    + sum_{i=k}^{k+h-2} theta_R(i,5k+c-1-i)
    + sum_{i=k+1}^{k+h-1} theta_R(i,5k+c+1-i).            (6)
```

If `N=2h+1`, where `h=(3k+c)/2`, then

```text
C_{k,n}(R)
  = theta_R(k,n)
    + sum_{i=k}^{k+h-1} theta_R(i,5k+c-1-i)
    + sum_{i=k+1}^{k+h} theta_R(i,5k+c+1-i).              (7)
```

Both formulas are necessary. Their occurrence on the four subsequences is

| Offset | Parity of `k` | Parity of `N` | Formula |
|---|---:|---:|---:|
| `c=5` | even | even | (6) |
| `c=5` | odd | odd | (7) |
| `c=6` | odd | even | (6) |
| `c=6` | even | odd | (7) |

Thus no parity subsequence is discarded.

## 2. The two Riemann sums, uniformly in offset and parity

For an edge `(a,b)` define

```text
w_k(a,b) = sqrt((a/k)(b/k)),
W_{k,c} = (1/k) sum_{(a,b) in E_{k,4k+c}} w_k(a,b)
        = (1/k^2) sum_{(a,b) in E_{k,4k+c}} sqrt(ab).      (8)
```

In either long sum of (6)-(7), with `x=i/k`, the normalized summand is

```text
g_{k,d}(x) = sqrt(x(5-x+d/k)),
d = c-1 or c+1.                                          (9)
```

The scaled index endpoints are read directly from (6)-(7):

| Parity of `N` | `d` | First endpoint | Last endpoint |
|---|---:|---:|---:|
| even | `c-1` | `1` | `5/2+(c-3)/(2k)` |
| even | `c+1` | `1+1/k` | `5/2+(c-1)/(2k)` |
| odd | `c-1` | `1` | `5/2+(c-2)/(2k)` |
| odd | `c+1` | `1+1/k` | `5/2+c/(2k)` |

Consequently each long sum is a mesh-`1/k` Riemann sum for `I`. The
following estimates make that statement simultaneous and quantitative.

For `k>=8`, every displayed point and every comparison cell lies in `[1,3]`.
On that interval put

```text
g(x) = sqrt(x(5-x)).
```

Then `2<=g(x)<=5/2` and `|g'(x)|<=3/4`. Since
`d in {4,5,6,7}`, rationalization gives

```text
0 <= g_{k,d}(x)-g(x)
   = (dx/k)/(g_{k,d}(x)+g(x))
   <= 21/(4k).                                           (10)
```

Each long sum has at most `2k` terms. After multiplication by `1/k`,
(10) contributes at most `21/(2k)`. The mesh error for `g` is at most
`3/(4k)`. The two endpoints together differ from those of `[1,5/2]` by at
most `5/k`, so the corresponding integral error is at most `25/(2k)`.
Therefore, for each of the two long sums and for every row of the parity
table,

```text
| (1/k) sum g_{k,d}(i/k) - I |
  <= (21/2 + 3/4 + 25/2)/k
   = 95/(4k).                                            (11)
```

Formula (6) has two special edges and (7) has one. Since all endpoints are at
most `n<=5k` for `k>=8`, each special edge contributes at most `5/k` to
(8). Combining this with (11) yields the uniform weight-sum bound

```text
|W_{k,c}-2I| <= 58/k                                    (12)
```

for `c=5,6` and both parities.

## 3. Uniform denominator and arcsine errors

Fix `r_0>0`, let `r>=r_0`, set `R=rk^2`, and consider any edge in (6) or
(7). Write

```text
A=a/k,  B=b/k,
v = sqrt(AB)/(rk),
p = A/(rk),  q = B/(rk),
u = sqrt(ab/((R+a)(R+b)))
  = v/sqrt((1+p)(1+q)).                                  (13)
```

For `k>=8`, `1<=A,B<=5`. The elementary inequality

```text
0 <= 1-(1+y)^(-1/2) <= y/2                 for y>=0
```

and `1-xy=(1-x)+x(1-y)` for `0<x,y<=1` give the explicit denominator
control

```text
0 <= v-u <= v(p+q)/2 <= 25/(r_0^2 k^2).                 (14)
```

If also `k>=10/r_0`, then `0<=u<=v<=1/2`. From

```text
asin(u)-u
  = integral_0^u t^2/[sqrt(1-t^2)(1+sqrt(1-t^2))] dt
  <= u^3/3                                                (15)
```

we obtain the uniform arcsine control

```text
|theta_{rk^2}(a,b) - 2sqrt(AB)/(rk)|
  <= 50/(r_0^2 k^2) + 250/(3r_0^3 k^3).                 (16)
```

There are `N=3k+c+1<=4k` edges for `k>=8`. Summing (16), using (8), and then
(12) proves, simultaneously for `c=5,6` and both parities,

```text
sup_{r>=r_0} |C_{k,4k+c}(rk^2)-4I/r|
  <= (116/r_0+200/r_0^2)/k + 1000/(3r_0^3 k^2)
   -> 0.                                                  (17)
```

Thus the denominator replacement and the arcsine linearization have been
controlled separately before being summed; neither is a merely pointwise
formal expansion.

## 4. Convergence of the implicit chain roots

Define

```text
rho = 2I/pi,
```

so that `4I/rho=2pi`. Given `0<epsilon<rho`, put
`r_-=rho-epsilon` and `r_+=rho+epsilon`. Apply (17) with `r_0=r_-`. Since

```text
4I/r_- > 2pi > 4I/r_+,
```

for all sufficiently large `k`, simultaneously for `c=5,6`,

```text
C_{k,4k+c}(r_- k^2) > 2pi,
C_{k,4k+c}(r_+ k^2) < 2pi.                              (18)
```

The imported theorem proves that each closure sum is strictly decreasing in
`R` and has the unique root (5). Hence (18) gives

```text
(rho-epsilon)k^2 < R_{k,4k+c} < (rho+epsilon)k^2.        (19)
```

This proves (2) for both offsets. No preliminary asymptotic bound on the root
has been assumed: the two fixed comparison points in (18) produce the root
bracket.

## 5. The Descartes thresholds without subtractive cancellation

The imported threshold formula is positive throughout the present domain,
because `4k+c>=4k+1`. Put `t=1/k` and define

```text
A = 4+ct,
B = 4+(c-1)t,
G = 9+(2c-1)t = A+B+1,
U = AB+A+B.                                               (20)
```

Substitution into the exact formula for `kappa=1/T` gives

```text
kappa_{k,4k+c} = t F_c(t),
F_c(t) = 1+1/A+1/B-2sqrt(G/(AB))
       = [U-2sqrt(ABG)]/(AB).                            (21)
```

The leading terms in (21) cancel, so we rationalize before taking a limit.
Direct exact expansion gives

```text
U^2-4ABG = t H_c(t),                                    (22)

H_c(t)
  = 32(2c-1)
    + [48c(c-1)+9]t
    + 6c(c-1)(2c-1)t^2
    + c^2(c-1)^2t^3.                                    (23)
```

All coefficients in (23) are positive for `c=5,6`; explicitly,

```text
H_5(t) = 288+969t+1080t^2+400t^3,
H_6(t) = 352+1449t+1980t^2+900t^3.                      (24)
```

Thus the conjugate used below is strictly positive and no sign or
extraneous branch is hidden. Equations (21)-(23) give the exact identity

```text
k^2 kappa_{k,4k+c}
  = F_c(t)/t
  = H_c(t)/Q_c(t),

Q_c(t) = AB[U+2sqrt(ABG)] > 0.                          (25)
```

At `t=0`, `Q_c(0)=16(24+24)=768`. This already proves

```text
k^2 kappa_{k,4k+c} -> 32(2c-1)/768 = (2c-1)/24.         (26)
```

For completeness, the denominator control can be made uniform rather than
left to continuity. For `c in {5,6}` and `0<=t<=1`,

```text
4<=A<=10,  4<=B<=9,  9<=G<=20,
Q_c(t)>=768,

0<=H_c(t)-H_c(0)<=4329t,
0<=Q_c(t)-768<=18000t.                                  (27)
```

Indeed `AB-16<=74t`, `ABG-144<=1656t`, and
`U-24<=85t`. Rationalizing the square root gives

```text
0<=2sqrt(ABG)-24<=138t.
```

Also `U+2sqrt(ABG)<195`, and hence

```text
Q_c(t)-768
  <= 74*195t + 16*(85+138)t
   = 17998t < 18000t.
```

Using `H_c(0)<=352`, (27) gives the simultaneous error estimate

```text
|k^2 kappa_{k,4k+c}-(2c-1)/24|
  <= [4329/768 + 352*18000/768^2]/k
   = 4193/(256k)
   < 17/k.                                               (28)
```

The exact positivity in (24)-(25) justifies inversion. For example, when
`k>=91`, (28) and `(2c-1)/24>=3/8` give
`k^2 kappa_{k,4k+c}>3/16`, and therefore

```text
|T_{k,4k+c}/k^2-24/(2c-1)| <= 2176/(9k).                (29)
```

This proves (3), with uniform control of every denominator and reciprocal.
In particular,

```text
T_{k,4k+5}/k^2 -> 8/3,
T_{k,4k+6}/k^2 -> 24/11.                                (30)
```

## 6. Exact certification of the constant `rho`

Completing the square and integrating a circular segment gives

```text
I = integral_0^(3/2) sqrt(25/4-u^2) du
  = 3/2 + (25/8) asin(3/5).                             (31)
```

Let

```text
alpha = asin(3/5) = atan(3/4).
```

The equality uses the positive acute branches and the `3-4-5` triangle.
Integrating the signed geometric remainder

```text
1/(1+x^2) = 1-x^2+x^4-x^6 + x^8/(1+x^2)
```

from `0` to `3/4` gives the strict rational lower bound

```text
alpha > L
      = 3/4-(3/4)^3/3+(3/4)^5/5-(3/4)^7/7
      = 365721/573440.                                  (32)
```

The same integral representation gives `alpha<3/4`, because its integrand is
strictly less than `1` away from zero.

Two exact elementary bounds on `pi` suffice. Polynomial division gives

```text
x^4(1-x)^4
  = (1+x^2)(x^6-4x^5+5x^4-4x^2+4)-4,
```

and therefore

```text
0 < integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7-pi.       (33)
```

In the other direction,

```text
1/(1+x^2)
  = sum_{j=0}^7 (-1)^j x^(2j) + x^16/(1+x^2),
```

so

```text
pi/4 > sum_{j=0}^7 (-1)^j/(2j+1)
     = 33976/45045
     = 3/4 + 769/180180,

pi > 3.                                                  (34)
```

From (31),

```text
rho = (12+25alpha)/(4pi).                                (35)
```

The lower comparison in (4) is equivalent to
`132+275alpha-96pi>0`. Equations (32)-(33) certify it with the exact margin

```text
132+275L-96*(22/7) = 650463/114688 > 0.                 (36)
```

The upper comparison is equivalent to
`32pi-36-75alpha>0`. Equations (32)-(34), using only the upper bound
`alpha<3/4`, give the exact margin

```text
32*3-36-75*(3/4) = 15/4 > 0.                            (37)
```

Thus (4) is an exact theorem; no decimal evaluation of `rho` is a premise.

## 7. Deduction of the eventual onset

At `c=5`, equations (2), (4), and (30) imply

```text
R_{k,4k+5} < T_{k,4k+5}                                 (38)
```

for every sufficiently large `k`. At `c=6` they imply

```text
R_{k,4k+6} > T_{k,4k+6}.                                (39)
```

The inequalities are eventually strict because their scaled limits are
separated by the strict margins in (4). The imported exact sign criterion
turns (38)-(39) into

```text
Delta_{k,4k+5} > 0,
Delta_{k,4k+6} < 0.                                     (40)
```

Finally, the imported persistence theorem states that
`D_{k,n}=R_{k,n}-T_{k,n}` is strictly increasing on `n>=4k+1`, and that a
strict obstruction, once present, persists. Since (38) says
`D_{k,4k+5}<0`, no earlier index can be strictly obstructed: any such
obstruction would persist through `4k+5`. Equation (39) supplies a strict
obstruction at the next index. Therefore (1) follows.

This argument does not assert monotonicity of the raw deficits
`Delta_{k,n}`. It uses the exact `R-T` comparison and its imported
persistence property.

## 8. Exact checker and excluded routes

The task-local script

```text
ops/TASK-20260830__eventual_supnick_seam_onset/check_asymptotic_onset.py
```

uses only the Python standard library and `fractions.Fraction`. It checks the
four parity classes, scaled endpoint identities, threshold factorization,
coefficient signs, uniform rational margins, signed geometric-remainder
identities, and the exact inequalities in (36)-(37). It contains no scan over
`k` or `n`; it is corroborative and does not replace the analytic Riemann-sum
argument or reprove the imported fixed-`k` theorem.

The proof explicitly excludes the following invalid routes.

1. A finite scan cannot prove an eventual identity and is not used.
2. One parity formula cannot stand in for both parity subsequences.
3. The approximation `asin(u)~u` is not used before a uniform small-argument
   and denominator bound.
4. The leading cancellation in `kappa` is not evaluated by subtracting
   floating-point quantities; it is removed by the exact conjugate (22).
5. The reciprocal defining `T` is taken only after exact positivity and a
   uniform lower bound.
6. A positive formal seam deficit is not full feasibility, while a negative
   one neither constructs a replacement chain nor determines a global
   optimum.
