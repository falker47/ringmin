# Increasing-order chain and full asymptotics

```text
status=PROVED
classification=exact asymptotic theorem / explicit feasible construction / proved global corollary
domain=integer n -> infinity; fixed cyclic order (1,2,...,n)
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Statement and epistemic scope

For `R,a,b>0`, write

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Let `inc_n=(1,2,...,n)` be the increasing cyclic order, including the
closing edge `(n,1)`. Denote its adjacent closure sum, chain root, and
fixed-order full optimum by

```text
C_n(R) = sum_{k=1}^{n-1} theta_R(k,k+1) + theta_R(n,1),
A_n = R_chain(inc_n),
F_n = R_full(inc_n).
```

The exact asymptotic conclusions are

```text
A_n = n^2/(2*pi) + O(n),
F_n/n^2 -> 1/(2*pi).                                  (1)
```

More explicitly, at

```text
Rhat_n = n^2/(2*pi) + n^(3/2)                          (2)
```

there is a fully feasible placement in the increasing order for every
sufficiently large `n`. The construction keeps every gap `(k,k+1)` tight
and puts all unused closure angle into the `(n,1)` gap. It checks both
cyclic paths for every pair; full feasibility is not inferred from closure.

Consequently

```text
limsup_{n->infinity} R*(n)/n^2 <= 1/(2*pi).             (3)
```

Combining (3) with the already proved terminal-subset lower bound gives

```text
C_term <= liminf R*(n)/n^2
       <= limsup R*(n)/n^2 <= 1/(2*pi),
R*(n)=Theta(n^2),                                      (4)

C_term = tau/(pi(1+sin(tau))),    tau=cos(tau),
tau in (0,pi/2).
```

These statements neither assert existence of the normalized global limit
nor optimality of the increasing order. They also do not identify the
sharp subleading term of `F_n`.

## 2. A uniform angular approximation

The approximation must be uniform over all edge radii, including radius
`1`. Fix `r_0>0`, let `r>=r_0`, set `R=r n^2`, and take arbitrary
`1<=a,b<=n`. Put

```text
u = sqrt(ab/((R+a)(R+b))),
v = sqrt(ab)/R,
p = a/R,    q = b/R.
```

Then

```text
u = v/((1+p)^(1/2)(1+q)^(1/2)).
```

For `x>=0`,

```text
0 <= 1-(1+x)^(-1/2) <= x/2.
```

Splitting the difference of the product into two one-variable differences
therefore gives

```text
0 <= v-u <= v(p+q)/2 <= 1/(r_0^2 n^2).                 (5)
```

For all sufficiently large `n`, `0<=u<=v<=1/(r_0 n)<=1/2`. On
`0<=t<=1/2`, rationalization of the derivative gives

```text
0 <= (1-t^2)^(-1/2)-1 <= t^2,
0 <= asin(u)-u <= u^3/3.
```

It follows uniformly in `a,b` and `r>=r_0` that

```text
|theta_{r n^2}(a,b)-2sqrt(ab)/(r n^2)|
  <= 2/(r_0^2 n^2) + 2/(3r_0^3 n^3).                  (6)
```

Thus summing over any `n` cyclic edges incurs total error `O(1/n)`, with
a constant depending only on `r_0`. This estimate is uniform at the seam
and does not require either radius to be proportional to `n`.

## 3. The increasing-order chain root

Define the square-root edge-weight sum

```text
W_n = sum_{k=1}^{n-1} sqrt(k(k+1)) + sqrt(n).           (7)
```

For every `k>=1`, exact rationalization yields

```text
0 <= k+1/2-sqrt(k(k+1))
   = 1/[4(k+1/2+sqrt(k(k+1)))] <= 1/(8k).
```

Since `sum_{k=1}^{n-1}(k+1/2)=(n^2-1)/2`, this proves

```text
W_n = (n^2-1)/2 + sqrt(n) - D_n,
0 <= D_n <= (1/8) sum_{k=1}^{n-1} 1/k,
2W_n/n^2 = 1+o(1).                                    (8)
```

Apply (6) to the `n` actual edges of `inc_n`. Uniformly for `r>=r_0`,

```text
C_n(r n^2) = 2W_n/(r n^2) + O(1/n)
            = 1/r + O(1/n).                            (9)
```

The last error is uniform when `r` ranges over any fixed compact subset of
`(0,infinity)`. This also gives a root proof that does not assume the root
scale. Set `c=1/(2*pi)`. For any fixed `0<epsilon<c`, (9) gives

```text
C_n((c-epsilon)n^2) -> 1/(c-epsilon) > 2*pi,
C_n((c+epsilon)n^2) -> 1/(c+epsilon) < 2*pi.
```

The exact closure sum is continuous and strictly decreasing in `R`, with
its unique root `A_n`. Hence

```text
A_n/n^2 -> c.                                          (10)
```

In particular its normalized value eventually lies in a fixed compact
subset of `(0,infinity)`, so (9) may now be evaluated at
`r_n=A_n/n^2`. Since `C_n(A_n)=2*pi=1/c`,

```text
1/r_n = 1/c + O(1/n).
```

Both `r_n` and `c` are bounded above and away from zero, and therefore

```text
|r_n-c| = c r_n |1/r_n-1/c| = O(1/n).
```

This proves the quantitative chain asymptotic in (1).

## 4. Why chain closure is not full feasibility

At `R=A_n`, any feasible placement in this fixed order would have every
adjacent gap at least its corresponding `theta` value. Their lower bounds
already sum to `2*pi`, so closure forces every adjacent gap, including the
seam, to be tight.

This forced placement is eventually infeasible. For every fixed positive
integer `k`, (10) and the exact angular formula give

```text
n^(3/2) theta_{A_n}(n,k) -> 2sqrt(k)/c = 4*pi*sqrt(k).  (11)
```

Also `n^(3/2)theta_{A_n}(1,2)->0`. Therefore the two-edge seam path for the
pair `(n,2)` satisfies

```text
n^(3/2)[theta_{A_n}(n,1)+theta_{A_n}(1,2)
        -theta_{A_n}(n,2)]
  -> 4*pi(1-sqrt(2)) < 0.                              (12)
```

Thus `F_n>A_n` for all sufficiently large `n`. Equation (12) is an exact
asymptotic obstruction involving a fixed, hence `o(n)`, endpoint. It is why
the proof of (1) must add and distribute closure slack rather than declare
the chain necklace feasible.

## 5. Explicit all-pairs gap construction

Use `Rhat_n` from (2), and abbreviate all angles in this section at that
radius. Let

```text
E_n = 2*pi-C_n(Rhat_n).                                (13)
```

Because `Rhat_n=(c+n^(-1/2))n^2`, equation (9) gives

```text
E_n = 1/c - 1/(c+n^(-1/2)) + O(1/n),
sqrt(n) E_n -> 1/c^2 = 4*pi^2.                         (14)
```

In particular `E_n>0` eventually. By monotonicity of `theta` in both
radii, every actual pair angle is at most the analytic envelope

```text
M_n = theta_{Rhat_n}(n,n)
    = 2 asin(n/(Rhat_n+n)) = O(1/n).                   (15)
```

Equations (14)-(15) imply the uniform seam guard

```text
E_n > M_n >= theta_{Rhat_n}(i,j)                       (16)
```

for every `1<=i<j<=n` once `n` is sufficiently large. This single
inequality covers proportional endpoints, one endpoint `o(n)`, fixed
endpoints, and every transition between those regimes.

Now define the cyclic gaps

```text
g_k = theta(k,k+1),                 1<=k<=n-1,
g_n = theta(n,1)+E_n.                                  (17)
```

They are positive and sum exactly to `2*pi`. It remains to check all pairs,
not only adjacent ones.

First, if `0<x<=y<=z`, monotonicity in each radius gives the elementary
ordered-triple inequality

```text
theta(x,y)+theta(y,z)-theta(x,z)
  >= theta(x,x) > 0.                                  (18)
```

Indeed `theta(x,y)>=theta(x,x)` and
`theta(y,z)>=theta(x,z)`. Repeated application of (18) proves, for every
`1<=i<j<=n`,

```text
sum_{k=i}^{j-1} theta(k,k+1) >= theta(i,j).             (19)
```

This is the directed path from `i` to `j` that does not cross the seam.
The complementary directed path crosses `(n,1)`, hence contains `g_n` and
has length at least `E_n`. By (16), it too has length at least
`theta(i,j)`. Thus both cyclic arcs between every pair have the required
length.

For an explicit placement, set `phi_1=0` and

```text
phi_j = sum_{k=1}^{j-1} g_k,          2<=j<=n.          (20)
```

Equations (17), (19), and (16) show

```text
theta(i,j) <= phi_j-phi_i <= 2*pi-theta(i,j)
```

for every `i<j`. The exact angular reformulation therefore places the
circle of radius `j` at angle `phi_j`, tangent to the central circle, with
all surrounding circles pairwise non-overlapping. This proves

```text
A_n <= F_n <= Rhat_n                                  (21)
```

for all sufficiently large `n`. Dividing (21) by `n^2` and using (10)
proves the full fixed-order limit in (1).

The deliberately coarse guard `E_n>M_n` is stronger than necessary. It
makes the seam audit uniform, but it does not claim that the `n^(3/2)`
additive radius in (2) is sharp. The obstruction (12) only proves a strict
gap between chain and full values, not its optimal scale.

## 6. Global consequences and exact limitations

The construction is a feasible configuration for the original radii
`1,...,n`, so minimization over all cyclic orders gives

```text
R*(n) <= F_n <= Rhat_n
```

eventually. This proves (3). Importing only the already proved exact
terminal-subset result from
[INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md](INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md)
gives the lower side of (4).

For completeness, the two exact coefficients are compatible strictly.
Let `D(t)=cos(t)-t`, whose unique zero is `tau`. The elementary bounds
`pi<4`, `sqrt(3)>5/3`, and the alternating cosine bound at `3/4` give

```text
D(pi/6)>0,
D(3/4)<1-9/32+27/2048-3/4=-37/2048<0.
```

Hence `pi/6<tau<3/4`, so `sin(tau)>1/2` and
`2tau<3/2<1+sin(tau)`. Therefore

```text
C_term = tau/(pi(1+sin(tau))) < 1/(2*pi).              (22)
```

Because the lower coefficient is positive and the upper coefficient is
finite, (4) implies `R*(n)=Theta(n^2)`. Nothing here proves

- that `R*(n)/n^2` converges;
- that either endpoint in (4) is the true liminf or limsup;
- that the increasing order is globally or asymptotically optimal;
- a sharp subleading expansion of `F_n` or `A_n` beyond the stated bounds;
- any extension of the finite certified range `3<=n<=14`.

The public arXiv-v1 paper, production implementation, verifier, result
artifacts, and finite certificates remain unchanged. The independent
high-precision diagnostic and its limitations are recorded in the
[task evidence](../ops/TASK-20260904__increasing_order_full_asymptotics/EVIDENCE.md).
