# Induced-subset lower bound and disproof of the n^2/8 conjecture

```text
status=PROVED
classification=exact theorem / proved corollary / disproved claim
domain=integer n >= 3; asymptotic conclusions as n -> infinity
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Result and definitions

**Exact theorem.** In the Ringmin problem,

```text
liminf_{n->infinity} R*(n)/n^2 >= rho/16 > 3/22 > 1/8,

rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx
    = (12+25 atan(3/4))/(4pi).                           (1)
```

Consequently both `R*(n)=n^2/8 (1+o(1))` and
`n^2/8-R*(n)=O(sqrt(n))` are **disproved claims** for this model.
This is an analytic lower bound, not a new finite global certificate or
a determination of the true leading coefficient.

For a finite set S of distinct positive radii, with |S|>=3, a feasible
configuration at R>0 has centers

```text
p_a = (R+a)(cos(phi_a), sin(phi_a)),   a in S,
|p_a-p_b| >= a+b                      for all distinct a,b in S.
```

Thus every surrounding circle remains externally tangent to the central
circle, and tangency between surrounding circles is allowed. Let R*(S)
be the infimum of feasible R, and write R*(n)=R*({1,...,n}). For a cyclic
order sigma of S let R_full(sigma) be the corresponding infimum with
that order fixed. There are finitely many orders, so

```text
R*(S) = min_sigma R_full(sigma).
```

Using infima avoids any need to assume an optimizer in the deletion proof.
These quantities are finite: equal angular spacing is feasible for large
R because every required angle tends to zero. Define

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))),
C_sigma(R) = sum over cyclic adjacent pairs of theta_R(a,b).
```

The unique positive root C_sigma(R)=2pi is R_chain(sigma): C_sigma is
continuous, strictly decreasing, tends to |S|pi>2pi at zero, and tends
to zero at infinity. The restriction |S|>=3 matters here.

The only imported ordering result is the published Supnick theorem for
arbitrary distinct positive radii, [paper source](../paper_assets/ringmin_paper.tex),
Theorem `thm:A` (i). At each R>0 it gives the same order sigma*_S with
C_sigma*_S(R)<=C_sigma(R) for every sigma. Its hypotheses apply to
subsets with their actual radii; no subtraction of k-1 from the radii is
permitted. For S={k,...,n}, write

```text
R_{k,n} = R_chain(sigma*_{k,n}),   k>=1, n>=k+2.
```

The exact rank-tour convention is that of
[FIXED_K_SUPNICK_SEAM.md](FIXED_K_SUPNICK_SEAM.md), section 1.
Sections 3-4 below restate and verify the needed asymptotic argument from
[EVENTUAL_SUPNICK_SEAM_ONSET.md](EVENTUAL_SUPNICK_SEAM_ONSET.md), sections
1-4 and 6. No seam threshold or seam-onset theorem is needed for (1).

## 2. Deletion, induced orders, and the direction of each bound

**Deletion lemma.** If T is a subset of S and |T|>=3, every feasible
configuration of S at R restricts to a feasible configuration of T at the
same R. Indeed, keep the same central circle and the same centers p_a for
a in T. Their central tangencies and all their mutual distance inequalities
are unchanged. Nothing requires the survivors to remain a tight necklace,
or the deleted circles to have been floating. Hence

```text
R*(S) >= R*(T).                                         (2)
```

For clarity, the adjacent-chain step can be derived without a triangle
inequality for theta. In a feasible configuration on T unroll the cyclic
angles, and let g_i>0 be the consecutive gaps, including the closing gap.
Their sum is 2pi. The distance formula gives, for each adjacent pair a,b,

```text
theta_R(a,b) <= g_i <= 2pi-theta_R(a,b).
```

This remains true when g_i>pi: it follows from the smaller angular
separation min(g_i,2pi-g_i). Summing the lower constraints yields
C_sigma(R)<=2pi. Strict decrease therefore gives R>=R_chain(sigma),
and taking infima gives R_full(sigma)>=R_chain(sigma).

When deletion makes previously nonadjacent circles adjacent, their
constraint was already among the full all-pairs constraints. Their new
gap is the sum of the old gaps between the surviving endpoints. This
explains why deletion of a merely formal chain would not suffice.

To transfer Supnick's fixed-R theorem to roots, set r=R_chain(sigma).
Then C_sigma*_T(r)<=C_sigma(r)=2pi, so
R_chain(sigma*_T)<=r. Taking the minimum over sigma proves

```text
R*(S) >= R*(T)
      = min_sigma R_full(sigma)
      >= min_sigma R_chain(sigma)
      = R_chain(sigma*_T).                              (3)
```

In particular, for every k>=1,n>=k+2,

```text
R*(n) >= R*({k,...,n}) >= R_{k,n}.                       (4)
```

The same deletion lemma gives R*(m)<=R*(n) for 3<=m<=n. It does not
assert monotonicity of the normalized sequence R*(n)/n^2.

**Relation to full feasibility.**
[SUPNICK_FULL_FEASIBILITY.md](SUPNICK_FULL_FEASIBILITY.md), section 6,
proves full feasibility at R_{k,4k+5} for k>=6. Combined with (3), this
also gives R*({k,...,4k+5})=R_{k,4k+5} for that family. This extra
equality is not a premise of (4) or (1). Feasibility on the subset supplies
no placement of the deleted circles, and therefore no upper bound for
the original problem on {1,...,4k+5}.

## 3. Audit of the exact chain asymptotic on n=4k+5

Put N=3k+6. The exact undirected cyclic edge multiset is

| Parity | Edges |
|---|---|
| N=2h (k even) | (k,4k+5), (k+h-1,k+h), (i,5k+4-i) for k<=i<=k+h-2, (i,5k+6-i) for k+1<=i<=k+h-1 |
| N=2h+1 (k odd) | (k,4k+5), (i,5k+4-i) for k<=i<=k+h-1, (i,5k+6-i) for k+1<=i<=k+h |

The counts are respectively 2+(h-1)+(h-1)=N and 1+h+h=N.
The even central edge and the closing edge are retained.
Let I=integral_1^(5/2) sqrt(x(5-x)) dx and

```text
W_k = (1/k^2) sum_{(a,b) in E} sqrt(ab).
```

Each of the two long edge sums contributes a mesh-1/k Riemann sum
for I. More explicitly its summand, after factoring 1/k, is
sqrt(x(5-x+d/k)), where x=i/k and d=4 or 6. Both endpoint pairs tend
to 1 and 5/2, in both parities. For all sufficiently large k these
points and their mesh cells lie in [1,3]. On that fixed compact interval
the summands converge uniformly to sqrt(x(5-x)), since rationalization
has a denominator bounded away from zero. Thus each sum tends to I.
There are at most two special edges, with a,b=O(k); each contributes
O(1/k) to W_k. Consequently

```text
W_k -> 2I.                                              (5)
```

The small-angle step must hold uniformly across the growing edge set.
Fix r>0 and set R=rk^2, A=a/k, B=b/k. For k>=8 all endpoints satisfy
1<=A,B<=5. With

```text
v=sqrt(AB)/(rk),
u=sqrt(ab/((rk^2+a)(rk^2+b)))
 =v/ sqrt((1+A/(rk))(1+B/(rk))),
```

the inequality 0<=1-(1+y)^(-1/2)<=y/2 gives
0<=v-u<=25/(r^2 k^2). For k>=10/r, u<=v<=1/2; integration of the
arcsine derivative gives 0<=asin(u)-u<=u^3/3. Therefore every edge obeys

```text
|theta_{rk^2}(a,b)-2sqrt(AB)/(rk)|
    <= 50/(r^2 k^2)+250/(3r^3 k^3).
```

There are N<=4k edges for k>=8. Sum the bound and use (5) to obtain

```text
C_{k,4k+5}(rk^2) = (2/r)W_k + O_r(1/k) -> 4I/r.        (6)
```

Define rho=2I/pi>0. For any 0<epsilon<rho, apply (6) separately at
r_-=rho-epsilon and r_+=rho+epsilon. Their limiting sums lie strictly
above and below 2pi respectively. For all sufficiently large k this
gives, by strict decrease of the exact closure sum,

```text
(rho-epsilon)k^2 < R_{k,4k+5} < (rho+epsilon)k^2.
```

Thus R_{k,4k+5}/k^2 -> rho. This covers both parities and does not
assume the scale of the unknown root before bracketing it. It agrees with
the stronger quantitative error bound in the existing asymptotic note.

## 4. Exact constant separation

Completing the square and substituting u=5/2-x gives

```text
I = integral_0^(3/2) sqrt(25/4-u^2) du
  = 3/2+(25/8)asin(3/5).
```

On the positive acute branches alpha=asin(3/5)=atan(3/4), so
rho=(12+25alpha)/(4pi). The signed geometric remainder integrated
from zero to 3/4 gives the strict lower bound

```text
alpha > L = 3/4-(3/4)^3/3+(3/4)^5/5-(3/4)^7/7
          = 365721/573440.
```

Indeed the omitted integrand is x^8/(1+x^2)>0 away from zero.
The positive integral identity

```text
integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7-pi > 0
```

gives pi<22/7. It follows exactly that

```text
132+275alpha-96pi
  > 132+275L-96*(22/7) = 650463/114688 > 0,
rho-24/11 = (132+275alpha-96pi)/(44pi) > 0.
```

All divisions use positive denominators. Hence

```text
rho/16 > (24/11)/16 = 3/22,
3/22-1/8 = 1/88 > 0.                                   (7)
```

No numerical approximation of pi, alpha or rho is a premise.

## 5. Subsequence bound and extension to every integer

Set n_k=4k+5. Equations (4)-(6) imply

```text
R*(n_k)/n_k^2 >= R_{k,n_k}/n_k^2
              = (R_{k,n_k}/k^2) (k/(4k+5))^2 -> rho/16
```

on the right-hand side. Thus liminf_k R*(4k+5)/(4k+5)^2>=rho/16.
The global quantity on the left has not been asserted to converge.

For every integer n>=9 put k=floor((n-5)/4)>=1. Then

```text
n=4k+5+j for a unique j in {0,1,2,3},
4k+5<=n<=4k+8,    k->infinity as n->infinity.
```

Monotonicity from deletion and (4) give

```text
R*(n)/n^2 >= R*(4k+5)/n^2
           >= R_{k,4k+5}/n^2
           >= (R_{k,4k+5}/k^2) (k/(4k+8))^2.            (8)
```

The final expression tends to rho/16. The denominator inequality in (8)
uses positivity of the chain root. Taking liminf proves (1) for all
integers, including every residue class. Values n<9 do not affect the
limit. The floor choice uses a smaller index; rounding upward would not
be justified by monotonicity.

## 6. Consequences, failed shortcuts, and limits

Since the liminf is strictly greater than 3/22, there exists N_0 such
that for all integers n>=N_0,

```text
R*(n) > (3/22)n^2,
n^2/8-R*(n) < -n^2/88.                                 (9)
```

This contradicts both convergence R*(n)/n^2->1/8 and an absolute
O(sqrt(n)) bound on the deficit. It does not supply an explicit N_0.
The original four-step argument is valid; no failed implication remains.

The distinction between full feasibility and formal closure is essential:
one cannot delete from an infeasible chain, invoke a triangle inequality
that theta need not satisfy, or infer an upper bound by reinserting circles
without a feasible placement. The strict separation concerns the constants;
(1) does not claim liminf R*(n)/n^2>rho/16.

Existence and value of a global leading coefficient, sharpness of rho/16,
matching upper bounds, and floating sets remain unresolved. No inference
about the number or identity of floating circles follows. The generic
deletion argument for actual configurations does not validate any particular
floating-point pruning implementation for new subsets or radius sequences.
The finite certificate scope remains 3<=n<=14; no certificate was rerun.

The arXiv-v1 conjecture remains in the historical paper unchanged; its
post-v1 status in active project memory is disproved. Arithmetic audit and
review limits are recorded in
[the task evidence](../ops/TASK-20260904__induced_subset_asymptotic_bound/EVIDENCE.md).
