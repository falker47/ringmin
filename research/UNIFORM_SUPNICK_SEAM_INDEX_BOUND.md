# Uniform bounds for the first Supnick seam obstruction

```text
status=PROVED
domain=integers k >= 1
proved_on=2026-08-30
published_snapshot=arXiv v1 remains unchanged
```

## Result and scope

For integers `k>=1` and `n>=k+2`, use the definitions from
`research/FIXED_K_SUPNICK_SEAM.md`: `R_{k,n}` is the adjacent-chain root of
the chain-minimizing Supnick cycle on `{k,...,n}`, `Delta_{k,n}` is its
formal seam deficit at `(n,k,n-1)`, and

```text
s_k = min {n >= k+2 : Delta_{k,n} < 0}
```

is the first strict-obstruction index. This note proves the exact uniform
bound

```text
4k+1 <= s_k <= 4k+14              for every integer k>=1.       (1)
```

The proof imports the fixed-`k` theorem in full. It does not determine an
exact formula for `s_k`, classify any individual onset not already known, or
use a finite scan. The result concerns one formal Supnick seam only. It makes
no claim about full fixed-order feasibility, `R*(n)`, global optima, contact
graphs, floating circles, or global asymptotics. It is post-arXiv-v1 work;
the historical paper and publication assets remain unchanged.

## 1. Imported lower bound

The exact no-threshold range in `research/FIXED_K_SUPNICK_SEAM.md` gives

```text
Delta_{k,n} > 0                    for k+2 <= n <= 4k.
```

The definition of the first strict-obstruction index therefore immediately
implies

```text
s_k >= 4k+1.                                                (2)
```

This is the lower bound in (1); no endpoint computation is needed.

## 2. A uniform comparison radius

For the upper bound, fix an arbitrary integer `k>=1` and put

```text
n_0 = 4k+14,
N   = n_0-k+1 = 3k+15,
D   = 21k+83,
S_k = kD/22 = k(21k+83)/22.                               (3)
```

We prove the strict bridge

```text
T_{k,n_0} < S_k < R_{k,n_0}.                               (4)
```

Because `n_0>=4k+1`, the imported positive Descartes threshold exists at
this index, and its sign criterion may be applied once (4) is established.

## 3. The chain side: `R_{k,n_0}>S_k`

The fixed-`k` chain lower bound is

```text
R_{k,n_0} >= k(csc(pi/N)-1).                               (5)
```

Here `N=3k+15>=18`, so `0<pi/N<pi`. The strict elementary inequality
`sin(x)<x` for `x>0`, together with positivity of `sin(pi/N)`, gives

```text
csc(pi/N) > N/pi.                                         (6)
```

We use the strict exact bound `pi<22/7`. One self-contained witness is

```text
22/7 - pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx > 0.       (7)
```

Indeed,

```text
x^4(1-x)^4
  = (1+x^2)(x^6-4x^5+5x^4-4x^2+4)-4,
```

the polynomial quotient integrates to `22/7` on `[0,1]`, and
`4 integral_0^1 1/(1+x^2) dx=pi`. The integrand in (7) is strictly positive
on `(0,1)`, so the inequality is strict.

Equations (3), (5), (6), and (7) now give

```text
R_{k,n_0}
  >= k(csc(pi/N)-1)
   > k(N/pi-1)
   > k(7N/22-1)
   = k(21k+83)/22
   = S_k.                                                 (8)
```

Thus the chain side of (4) holds for every `k>=1`.

## 4. The threshold side: positivity before squaring

At `n_0=4k+14`, abbreviate

```text
Q_k = (2n_0+k-1)/(k n_0(n_0-1))
    = 9(k+3)/(k(4k+14)(4k+13)).                           (9)
```

The imported threshold formula becomes

```text
kappa_{k,n_0}
  = 1/k + 1/(4k+14) + 1/(4k+13) - 2 sqrt(Q_k),
T_{k,n_0} = 1/kappa_{k,n_0}.                              (10)
```

Since `1/S_k=22/(kD)`, define the rational part of the desired comparison by

```text
A_k = 1/k + 1/(4k+14) + 1/(4k+13) - 1/S_k.               (11)
```

Then

```text
kappa_{k,n_0} - 1/S_k = A_k - 2 sqrt(Q_k).                (12)
```

Before squaring, the required positivity gate is explicit:

```text
A_k
  = (21k+61)/(kD) + (8k+27)/((4k+14)(4k+13))
  = P(k)/(kD(4k+14)(4k+13)) > 0,                         (13)

P(k) = 504k^3 + 4475k^2 + 12651k + 11102.
```

Every numerator and denominator in the first line of (13) is positive for
`k>=1`; equivalently, every coefficient of `P` is positive. Equation (9)
also gives `Q_k>0`. Thus both sides of the forthcoming square comparison are
positive, and no sign can be lost by squaring.

## 5. The exact quadratic difference

Putting (9) and (13) over their common denominator gives

```text
A_k^2 - 4Q_k
  = F(k)/(k^2 D^2 (4k+14)^2 (4k+13)^2),                 (14)

F(k)
  = P(k)^2 - 36k(k+3)D^2(4k+14)(4k+13)
  = 26208k^5
    + 1199137k^4
    + 13559370k^3
    + 65399861k^2
    + 145492620k
    + 123254404.                                        (15)
```

For a fully coefficient-positive denominator certificate, write

```text
D^2(4k+14)^2(4k+13)^2
  = 112896k^6
    + 2416512k^5
    + 21523408k^4
    + 102108144k^3
    + 272124148k^2
    + 386290632k
    + 228191236.                                        (16)
```

All coefficients displayed in (15) and (16) are strictly positive. Since
`k>=1`, equations (14)-(16) prove

```text
A_k^2 - 4Q_k > 0.                                       (17)
```

The positivity gate (13), `Q_k>0`, and (17) imply

```text
A_k > 2 sqrt(Q_k).
```

Using (12) and positivity of `S_k`, we obtain

```text
kappa_{k,n_0} > 1/S_k > 0,
T_{k,n_0} = 1/kappa_{k,n_0} < S_k.                      (18)
```

This proves the threshold side of (4) without an extraneous squared branch.

## 6. Conclusion from the fixed-`k` sign criterion

Combining (8) and (18) yields

```text
T_{k,n_0} < S_k < R_{k,n_0},
R_{k,n_0} > T_{k,n_0}.
```

The imported exact criterion therefore gives

```text
Delta_{k,4k+14} < 0.
```

By the definition of the first strict-obstruction index,

```text
s_k <= 4k+14.                                           (19)
```

Together, (2) and (19) prove (1) for every integer `k>=1`. All decisive
inequalities are strict. The proof uses one symbolic index `n_0=4k+14` and
no finite enumeration of `k` or `n`.

## 7. Exact checker

The task-local script

```text
ops/TASK-20260830__uniform_seam_index_bound/check_uniform_bound.py
```

uses only the Python standard library and `fractions.Fraction`. It checks the
polynomial identity behind `pi<22/7`, the substitutions in (3), the exact
rational identities for `A_k` and `Q_k`, the denominator in (14), both
expanded products in (15), the coefficient-positive polynomial in (16), and
every positivity/strictness gate used before reciprocal or square comparison.
It performs symbolic coefficient arithmetic only: no finite parameter scan
is a premise or a substitute for the proof above.
