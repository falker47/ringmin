# Optimized induced-terminal-subset asymptotic lower bound

```text
status=PROVED
classification=exact theorem / proved corollary / disproved claim
domain=integer terminal subsets {k,...,n}; n/k -> lambda>1
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Results and definitions

For `lambda>1`, put

```text
I(lambda) = integral_1^((lambda+1)/2)
                sqrt(x(lambda+1-x)) dx,
rho(lambda) = 2 I(lambda)/pi,
c(lambda) = rho(lambda)/lambda^2.                       (1)
```

**General terminal-subset chain theorem.** If `k_j,n_j` are integers with

```text
k_j -> infinity,       n_j/k_j -> lambda>1,
```

then, for the chain-minimizing Supnick cycle on the actual radii
`{k_j,...,n_j}` and its closure root `R_{k_j,n_j}`,

```text
R_{k_j,n_j}/k_j^2 -> rho(lambda),
R_{k_j,n_j}/n_j^2 -> c(lambda).                         (2)
```

This holds along the whole sequence, irrespective of the parity of
`n_j-k_j+1`.

**Optimized global lower bound.** Let `tau` be the unique solution in
`(0,pi/2)` of

```text
tau = cos(tau),                                         (3)
```

and define

```text
lambda_* = (1+sin(tau))/(1-sin(tau)),
C_term = tau/(pi(1+sin(tau))).                          (4)
```

Then

```text
liminf_{n->infinity} R*(n)/n^2 >= C_term,               (5)
```

and `C_term` is the unique maximum of `c(lambda)` over `lambda>1`.
Reviewer-side numerical diagnostics, not premises of the proof, give

```text
tau       = 0.7390851332151606416553120877...
lambda_*  = 5.1276768104994934856704362505...
C_term    = 0.1405690808452567665455162310....           (6)
```

The previous choice `lambda=4` gives exactly the earlier coefficient
`rho/16=0.1396959023...`; it is strictly suboptimal in this family.

For a finite set `S` of distinct positive radii, with `|S|>=3`, a feasible
configuration at `R>0` has centers

```text
p_a = (R+a)(cos(phi_a), sin(phi_a)),   a in S,
|p_a-p_b| >= a+b                      for all distinct a,b in S.
```

Let `R*(S)` be the infimum of feasible `R`, and write
`R*(n)=R*({1,...,n})`. For a cyclic order `sigma` of `S`, let
`R_full(sigma)` be the corresponding fixed-order infimum. Define

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))),
C_sigma(R) = sum over cyclic adjacent pairs of theta_R(a,b).
```

The unique positive root `C_sigma(R)=2pi` is `R_chain(sigma)`. The only
imported ordering result is the arbitrary-radii Supnick theorem in the
[published source](../paper_assets/ringmin_paper.tex), Theorem `thm:A`.
For `S={k,...,n}`, the chain-minimizing order and root are denoted by
`sigma*_{k,n}` and `R_{k,n}`. The exact order convention and edge formulas
come from [FIXED_K_SUPNICK_SEAM.md](FIXED_K_SUPNICK_SEAM.md), section 1.
No seam theorem or full feasibility of this formal chain is used here.

## 2. Deletion and the unconditional direction

**Deletion lemma.** If `T` is a subset of `S` and `|T|>=3`, every feasible
configuration of `S` at `R` restricts to a feasible configuration of `T`
at the same `R`: retain the same central circle and the same centers of the
surviving circles. Central tangencies and all surviving pairwise distance
constraints are unchanged. Taking infima gives

```text
R*(S) >= R*(T).                                         (7)
```

For completeness, in a feasible fixed order unroll the cyclic angles and
let the consecutive gaps be `g_i>0`, including the closing gap. Their sum
is `2pi`. The distance formula gives `g_i>=theta_R(a,b)` for every adjacent
pair when the gap is at most `pi`; when it is larger, the complementary
arc constraint implies the same lower bound for the smaller separation and
the displayed cyclic-gap inequality follows in the standard unrolling.
Equivalently, one may use the two exact bounds

```text
theta_R(a,b) <= g_i <= 2pi-theta_R(a,b).
```

Summing the lower bounds yields `C_sigma(R)<=2pi`, so strict decrease of
the closure sum gives `R_full(sigma)>=R_chain(sigma)`.

Supnick's theorem applies to the retained radii themselves; the radii must
not be translated by `k-1`. At every fixed `R` the same Supnick order
minimizes the adjacent-angle sum. Transferring this inequality to the
unique roots gives

```text
R*(n) >= R*({k,...,n})
      = min_sigma R_full(sigma)
      >= min_sigma R_chain(sigma)
      = R_{k,n},                  k>=1, n>=k+2.          (8)
```

When deletion makes two survivors adjacent, their constraint was already
present among the original all-pairs constraints. This is why (8) starts
from an actual feasible configuration, not from an infeasible formal chain.

## 3. Exact parity formulas and the limiting edge-weight measure

Fix a sequence from (2), suppress its sequence index, and write

```text
N=n-k+1,       ell=n/k -> lambda.
```

For an edge `(a,b)` define `A=a/k`, `B=b/k`, and

```text
W_{k,n} = (1/k^2) sum_{(a,b) in E_{k,n}} sqrt(ab)
        = (1/k)   sum_{(a,b) in E_{k,n}} sqrt(AB).       (9)
```

The Supnick edge formulas have two long families. Their exact endpoints,
including both parities, are as follows.

| Parity and family | Paired radius `b` | First `i/k` | Last `i/k` | Number of edges |
|---|---|---:|---:|---:|
| `N=2h`, minus | `n+k-1-i` | `1` | `(ell+1)/2-3/(2k)` | `h-1` |
| `N=2h`, plus | `n+k+1-i` | `1+1/k` | `(ell+1)/2-1/(2k)` | `h-1` |
| `N=2h+1`, minus | `n+k-1-i` | `1` | `(ell+1)/2-1/k` | `h` |
| `N=2h+1`, plus | `n+k+1-i` | `1+1/k` | `(ell+1)/2` | `h` |

The even cycle also has the special edges

```text
(k,n), (k+h-1,k+h),
```

while the odd cycle has only `(k,n)` outside the two long families. Thus
the edge counts are respectively `2+(h-1)+(h-1)=N` and `1+h+h=N`;
no central or closing edge has been dropped.

In the minus and plus families, respectively, the normalized summands are

```text
g_{k,-}(x) = sqrt(x(ell+1-1/k-x)),
g_{k,+}(x) = sqrt(x(ell+1+1/k-x)).                      (10)
```

Both families converge to

```text
g_lambda(x)=sqrt(x(lambda+1-x))
```

on the interval from `1` to `(lambda+1)/2`. Here is a uniform version of
the Riemann-sum argument. On a common compact interval containing every
eventual grid point, both factors under the square roots are bounded away
from zero. Rationalization therefore gives, with a constant depending only
on a fixed neighborhood of `lambda`,

```text
sup_x |g_{k,+/-}(x)-g_lambda(x)|
    <= C_lambda (|ell-lambda|+1/k).                     (11)
```

There are `O_lambda(k)` terms. The four exact endpoints in the table differ
from `1` and `(lambda+1)/2` by
`O(|ell-lambda|+1/k)`. Since `g_lambda` is continuously differentiable
on that common compact interval, the ordinary mesh error and the two
endpoint errors are `O_lambda(1/k)` and
`O_lambda(|ell-lambda|+1/k)`, respectively. Hence, uniformly across the
two parities and the two families,

```text
(1/k) sum_i g_{k,+/-}(i/k)
    = I(lambda)+O_lambda(|ell-lambda|+1/k).              (12)
```

Choose `M>lambda` so that eventually `ell<=M`. Every normalized endpoint
of a special edge is at most `M`, so each such edge contributes at most
`M/k` to (9). Equations (9)-(12) now give the parity-uniform limit

```text
W_{k,n} = 2I(lambda)
           +O_lambda(|ell-lambda|+1/k) -> 2I(lambda).   (13)
```

## 4. Uniform small-angle errors and the implicit root

The angular expansion must be uniform over the growing edge set and must
not assume the scale of the unknown root. Fix `r_0>0`, let `r>=r_0`, set
`R=rk^2`, and consider any Supnick edge. With `1<=A,B<=M`, put

```text
v = sqrt(AB)/(rk),
p = A/(rk),       q_0 = B/(rk),
u = sqrt(ab/((rk^2+a)(rk^2+b)))
  = v/sqrt((1+p)(1+q_0)).                               (14)
```

The inequalities

```text
0 <= 1-(1+y)^(-1/2) <= y/2,          y>=0,
1-xy = (1-x)+x(1-y),                 0<x,y<=1,
```

give, simultaneously for every edge and every `r>=r_0`,

```text
0 <= v-u <= M^2/(r_0^2 k^2).                           (15)
```

For `k>=2M/r_0`, `u<=v<=1/2`. Integration of the arcsine derivative gives

```text
0 <= asin(u)-u <= u^3/3.
```

Consequently the explicit per-edge error is

```text
|theta_{rk^2}(a,b)-2sqrt(AB)/(rk)|
 <= 2M^2/(r_0^2 k^2)+2M^3/(3r_0^3 k^3).                (16)
```

Since `N<=n<=Mk` eventually, summing (16) proves

```text
sup_{r>=r_0} |C_{k,n}(rk^2)-(2/r)W_{k,n}|
 <= 2M^3/(r_0^2 k)+2M^4/(3r_0^3 k^2).                  (17)
```

Combining (13) and (17), still uniformly in `r>=r_0` and in parity,

```text
sup_{r>=r_0} |C_{k,n}(rk^2)-4I(lambda)/r|
 = O_lambda,r_0(|ell-lambda|+1/k) -> 0.                (18)
```

Define `rho(lambda)=2I(lambda)/pi>0`. For any
`0<epsilon<rho(lambda)`, apply (18) with
`r_-=rho(lambda)-epsilon` and `r_+=rho(lambda)+epsilon`. The two limiting
closure sums satisfy

```text
4I(lambda)/r_- > 2pi > 4I(lambda)/r_+.
```

For all sufficiently large sequence indices, the same strict inequalities
hold for the exact closure sums. Their strict decrease in `R` and unique
roots therefore imply

```text
(rho(lambda)-epsilon)k^2 < R_{k,n}
                         < (rho(lambda)+epsilon)k^2.    (19)
```

This proves the first limit in (2), without presupposing root scale. The
second follows from `n/k->lambda`.

## 5. Closed form for the coefficient

Let

```text
L=lambda+1,       q=(lambda-1)/(lambda+1) in (0,1).
```

Under `z=2x/L-1`, the endpoints `x=1,L/2` become `z=-q,0`, and

```text
I(lambda)
 = (L^2/4) integral_{-q}^0 sqrt(1-z^2) dz
 = (L^2/8)(asin(q)+q sqrt(1-q^2)).                      (20)
```

Thus

```text
rho(lambda)
 = ((lambda+1)^2/(4pi))
     (asin(q)+q sqrt(1-q^2)),                           (21)

c(lambda)
 = [asin(q)+q sqrt(1-q^2)]/[pi(1+q)^2].                (22)
```

At `lambda=4`, `q=3/5`, `sqrt(1-q^2)=4/5`, and
`asin(3/5)=atan(3/4)`. Formula (21) reduces to the former constant

```text
rho(4)=(12+25 atan(3/4))/(4pi),
c(4)=rho(4)/16.                                         (23)
```

The exact separation in
[EVENTUAL_SUPNICK_SEAM_ONSET.md](EVENTUAL_SUPNICK_SEAM_ONSET.md), section 6,
remains valid for this value:

```text
c(4)=rho(4)/16 > 3/22 > 1/8.                           (24)
```

## 6. Exact optimization, boundaries, and uniqueness

The map `lambda -> q=(lambda-1)/(lambda+1)` is a strictly increasing
bijection from `(1,infinity)` to `(0,1)`. Put

```text
H(q)=asin(q)+q sqrt(1-q^2),
F(q)=H(q)/(pi(1+q)^2)=c(lambda).
```

Direct differentiation gives the exact cancellations

```text
H'(q)=2sqrt(1-q^2),
F'(q)=2[sqrt(1-q^2)-asin(q)]/[pi(1+q)^3].               (25)
```

Set `t=asin(q)`, so `t in (0,pi/2)` and
`sqrt(1-q^2)=cos(t)`. The sign of (25) is the sign of

```text
D(t)=cos(t)-t.
```

Now `D(0)=1`, `D(pi/2)=-pi/2`, and
`D'(t)=-sin(t)-1<0`. The intermediate value theorem and strict monotonicity
therefore give exactly one zero `tau` in `(0,pi/2)`. Hence `F`, and thus
`c`, is strictly increasing before `q=sin(tau)` and strictly decreasing
after it. The optimizer (4) exists, is unique, and is global.

At the critical point, `sqrt(1-q^2)=tau` and

```text
H(q)=tau+q tau=tau(1+q),
```

so (22) gives the exact optimized value `C_term` in (4). Moreover,

```text
lim_{lambda down to 1} c(lambda)=0,
lim_{lambda to infinity} c(lambda)=1/8.                 (26)
```

Indeed `q` tends respectively to `0` and `1`, while `H(q)` tends to `0`
and `pi/2`. These boundary values are strictly below the interior maximum.
The former `lambda=4` point is also strictly before the optimizer: at
`q=3/5`,

```text
sqrt(1-q^2)=4/5 > 3/4 > atan(3/4)=asin(3/5),
```

where `atan(x)<x` for `x>0`. Thus (25) is positive there and
`C_term>c(4)` without numerical comparison.

## 7. Passage to every integer and optimality within the method

Fix the exact `lambda_*` from (4). For every sufficiently large integer
`n`, choose

```text
k_n=floor(n/lambda_*).
```

Then `k_n->infinity`, `n/k_n->lambda_*`, and `n>=k_n+2`. The unconditional
deletion bound (8) and the sequence theorem give

```text
R*(n)/n^2 >= R_{k_n,n}/n^2 -> c(lambda_*)=C_term
```

on the right. Taking the liminf proves (5) for the complete integer
sequence; normalized monotonicity of `R*(n)` is neither assumed nor needed.

More generally, the same floor choice for any fixed `lambda>1` gives

```text
liminf_{n->infinity} R*(n)/n^2 >= c(lambda).             (27)
```

Section 6 proves that `C_term=max_{lambda>1} c(lambda)`, attained only at
`lambda_*`. Therefore (5) is exactly the best coefficient furnished by the
fixed-ratio terminal-subset deletion family analyzed here. This statement
does not claim optimality among nonterminal deletions, combinations of
several subsets, or other geometric lower-bound methods.

## 8. Consequences and unresolved true asymptotics

Because `C_term>c(4)>3/22>1/8`, the earlier conclusions remain valid:
both

```text
R*(n)=n^2/8 (1+o(1))
```

and `n^2/8-R*(n)=O(sqrt(n))` are **disproved claims**. The new theorem
strictly strengthens their unconditional refutation.

What remains unresolved is exact and substantial:

- whether `R*(n)/n^2` has a limit;
- the value of its liminf or limsup, and whether either equals `C_term`;
- any matching feasible upper bound at coefficient `C_term`;
- whether a stronger lower bound follows from nonterminal or multiple
  induced subsets, full all-pairs geometry, or another method;
- the asymptotic number and identity of floating circles.

The maximizing `lambda_*` optimizes a lower-bound mechanism, not a proposed
optimal configuration and not the true Ringmin coefficient. No finite
global certificate is extended: the recorded certified scope remains
`3<=n<=14`. Production search, result artifacts, `verify.py`, and the
historical arXiv-v1 paper/assets are unchanged. Task-local exact/symbolic
checks and their limitations are recorded in
[the evidence dossier](../ops/TASK-20260904__optimized_terminal_subset_bound/EVIDENCE.md).
