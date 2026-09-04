# Supnick seam dominance and fixed-order full feasibility

```text
status=PROVED
domain=integers k >= 1, n >= k+2
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Statement, definitions and dependency order

For R,a,b>0 set

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Fix integers k>=1, n>=k+2, put N=n-k+1>=3, and let sigma be the
canonical Supnick cycle on {k,...,n}. All radii occur once. Let
R=R_{k,n}>0 be its exact chain root, so the sum over all N adjacent edges
is 2 pi. Write theta=theta_R and

```text
Delta = theta(n,k) + theta(k,n-1) - theta(n,n-1).
```

Initially import only the exact order and unique positive chain root from
[the fixed-k note](FIXED_K_SUPNICK_SEAM.md), sections 1-2. In both parities,
including N=3, the neighbors of k are exactly n and n-1. Sections 2-5 below
prove the equivalence without any imported sign of Delta or onset theorem.
Only section 6 combines that equivalence with the known seam signs.

The angular kernel and geometric interpretation are those of the published
angular lemma. Its monotonicity and positive mixed derivative are rederived
below. Full feasibility is not an imported premise.

For a simple path P=(v_0,...,v_m) of m>=1 adjacent edges define

```text
S_R(P) = sum_{j=0}^{m-1} theta_R(v_j,v_{j+1}) - theta_R(v_0,v_m).
```

Write S(P)=S_R(P) when the radius being used is clear, in particular at
R=R_{k,n}. The path lemmas also apply before imposing closure.

**Exact theorem (complete fixed-order criterion).** The following are
equivalent for every k,n in the stated domain:

```text
(i)   Delta_{k,n} >= 0;
(ii)  the cumulative-angle Supnick placement at R_{k,n} is fully feasible;
(iii) some fully feasible placement of this fixed order exists at R_{k,n}.
```

At any R>0, every simple m-edge path satisfies

```text
S(P) >= (m-1) delta_R,                                  (1)
delta_R = theta_R(n,k)+theta_R(k,n-1)-theta_R(n,n-1).
```

For m=1 its slack is exactly zero. At the chain root, Delta>=0 makes
both cyclic directions feasible for every pair, including adjacent
complements. Delta<0 prevents every feasible placement in this fixed order
at that radius: closure forces all its adjacent gaps tight.

**Proved fixed-order corollary.** If Delta>=0, then

```text
R_full(sigma) = R_chain(sigma) = R_{k,n}.                 (2)
```

The result concerns this fixed-order problem only. It makes no assertion
about global optimality, R*(n), global contact graphs, or floating behavior.

## 2. Exact minimum of every triangle defect

This lemma is valid for all integers k>=1, n>=k+2 and every R>0, before
imposing the chain equation and without a sign assumption. In this section write

```text
delta_R = theta_R(n,k)+theta_R(k,n-1)-theta_R(n,n-1).
```

**Triangle lemma.** If a,b,c are three distinct members of {k,...,n}, then

```text
theta_R(a,b)+theta_R(b,c)-theta_R(a,c) >= delta_R,          (3)
```

with equality exactly when b=k and {a,c}={n-1,n}.

Proof. Fix R and suppress its subscript. Direct differentiation on the
positive domain gives

```text
theta_1(a,b) = sqrt(R*b/a)/((R+a)*sqrt(R+a+b)) > 0,

theta_12(a,b) = sqrt(R)/(2*sqrt(a*b)*(R+a+b)^(3/2)) > 0.   (4)
```

The symmetric derivative theta_2 is positive as well. These identities
also follow by setting t_x=sqrt(x/(R+x)), noting t_x'>0, and differentiating
2 asin(t_a*t_b), whose mixed derivative in the two t variables is
2/(1-t_a^2*t_b^2)^(3/2).

Exchange the endpoints if needed to arrange a<c. Thus
k<=a<=n-1 and k<c<=n; the ordering of the middle radius b relative to a,c
is unrestricted. Since b>=k and theta increases in both arguments,

```text
theta(a,b)+theta(b,c)-theta(a,c)
    >= H(a,c),
H(x,z) = theta(x,k)+theta(k,z)-theta(x,z).                 (5)
```

This comparison is strict if b>k. It remains legitimate when a=k:
theta(k,k) is the analytic kernel value, not a self-pair constraint.

On x,z>=k, positivity of the mixed derivative gives

```text
H_1(x,z) = theta_1(x,k)-theta_1(x,z) <= 0,
H_2(x,z) = theta_2(k,z)-theta_2(x,z) <= 0.                 (6)
```

The first inequality is strict when z>k; the second is strict when x>k.
Increasing x from a to n-1 and then z from c to n therefore yields

```text
H(a,c) >= H(n-1,c) >= H(n-1,n) = delta_R.                 (7)
```

For an explicit nonnegative-remainder version of this step,

```text
H(a,c)-H(n-1,n)
  = integral_{x=a}^{n-1} integral_{y=k}^{c}
        theta_12(x,y) dy dx
    + integral_{y=c}^{n} integral_{x=k}^{n-1}
        theta_12(x,y) dx dy.                             (8)
```

All integration intervals have nonnegative lengths. Since c>k and
n-1>k, the first term is strictly positive if a<n-1 and the second if
c<n. Combining (5)-(8) proves both (3) and its equality classification.
This covers all six orderings of three distinct radii, including a middle
radius greater than either or both endpoints. No triangle inequality was
assumed. QED.

## 3. Telescoping over an arbitrary simple path

For distinct v_0,...,v_m and m>=2, the exact identity is

```text
sum_{j=0}^{m-1} theta(v_j,v_{j+1}) - theta(v_0,v_m)
  = sum_{j=1}^{m-1} [theta(v_0,v_j)+theta(v_j,v_{j+1})
                     -theta(v_0,v_{j+1})].               (9)
```

Indeed, the positive theta(v_0,v_j) terms for 2<=j<=m-1 cancel the
preceding negative terms, leaving the first edge and the last negative
term. Each summand uses three distinct radii, so (3) bounds it below by
delta_R. This proves S(P)>=(m-1)delta_R at every R>0. For a single-edge
path m=1 the empty-sum version of (9) gives S(P)=0.

No step depends on N=3k+6 or n=4k+5. At the exact chain root, Delta>=0
implies S(P)>=0 for every m, including Delta=0. If Delta>0 and m>=2,
then S(P)>=Delta; for m>2 it is strictly larger. For m=2, equality in
S(P)>=Delta occurs only for the seam and its reversal.

When Delta=0, an m>=3 fan contains at least two distinct middle vertices
v_1,v_2. At most one can be k, so at least one triangle inequality in the
fan is strict by section 2. Thus S(P)>0 for m>=3; for m=2 only the seam
can have zero slack. No division by Delta or strict-positivity assumption
is used to infer feasibility at equality. If Delta<0, (1) alone does not
imply S(P)>=Delta or any feasibility statement.

## 4. Equivalence, both directions, small cycles and equality

Write sigma=(s_0,...,s_{N-1}), with indices modulo N. For indices i<j put
d=j-i, and define the two paths explicitly:

```text
P_+ = (s_i,s_{i+1},...,s_j),                    m_+ = d,
P_- = (s_j,s_{j+1},...,s_{N-1},s_0,...,s_i),    m_- = N-d.
```

They are simple paths with the same unordered endpoints. If the endpoints
are nonadjacent, 2<=d<=N-2, so both have at least two edges. Applying (9)
to each path with its own first vertex gives the two separate bounds

```text
S(P_+) >= (d-1) Delta,
S(P_-) >= (N-d-1) Delta.                                 (10)
```

First suppose Delta>=0. No assumption about which path subtends the smaller
angle is made. Exact closure gives their lengths A_++A_-=2 pi.
Define positions by cumulative
adjacent angles, phi_0=0 and phi_i=sum_{j=0}^{i-1} theta(s_j,s_{j+1}).
All increments are positive. Equation (10) implies

```text
A_+ >= theta(s_i,s_j),
A_- >= theta(s_i,s_j),

theta(s_i,s_j) <= A_+ <= 2 pi-theta(s_i,s_j).              (11)
```

Thus min(A_+,A_-) in [0,pi] is at least the required angle. For adjacent
endpoints, the one-edge direction has slack zero; its N-1-edge complement
has slack at least (N-2)Delta>=0 by (9). Adjacent pairs therefore satisfy
both constraints too, including the cyclic closing edge.
In fact closure gives its exact slack 2pi-2theta(s_i,s_{i+1})>0,
since 0<theta<pi. This also checks the upper constraint for an adjacent
gap; checking only the one-edge lower constraint would be insufficient.

For completeness, place each center at
(R+s_i)(cos(phi_i),sin(phi_i)). The squared distance for endpoints a,b
and either angular path A is

```text
(R+a)^2+(R+b)^2-2(R+a)(R+b) cos(A).
```

Since (11) holds in both directions, the smaller angle is at least
theta(a,b), where cos(theta(a,b))=1-2ab/((R+a)(R+b)). Consequently the
squared distance is at least (a+b)^2. Each surrounding circle is externally
tangent to the central circle. This proves full geometric feasibility.

This proves (i)=>(ii); (ii)=>(iii) is immediate.

### Necessity: closure forces every adjacent gap

Suppose any fully feasible placement in this fixed cyclic order exists
at R=R_{k,n}. Unroll its positions as phi_0<...<phi_{N-1}<phi_0+2pi.
Write g_i=phi_{i+1}-phi_i for i<N-1 and
g_{N-1}=phi_0+2pi-phi_{N-1}. All N gaps are positive and sum to 2pi.
The all-pairs condition for each adjacent pair implies separately

```text
theta(s_i,s_{i+1}) <= g_i <= 2pi-theta(s_i,s_{i+1}),
sum_i [g_i-theta(s_i,s_{i+1})] = 2pi-C_{k,n}(R) = 0.
```

Each summand is nonnegative; hence every one is zero. This forces all N
gaps, including the closing edge, not merely the two incident to k.
There is no remaining angular freedom to enlarge the seam at this radius.

Let A be the two-edge path n,k,n-1 (in either orientation), and B its
N-2-edge complement avoiding k. Forced tightness and closure give

```text
A = theta(n,k)+theta(k,n-1),
B = 2pi-A,
A-theta(n,n-1) = Delta,
B-[2pi-theta(n,n-1)] = -Delta.                          (11a)
```

If Delta<0, A violates the pair's lower angular constraint and B exceeds
its upper angular constraint. Thus the seam complement is impossible,
even if B happens to satisfy its lower constraint. No assumption about
which arc is shorter is needed. This proves (iii)=>(i).

### N=3, N=4, and the weak inequality

For N=3 the tour is (k,k+1,k+2); all three pairs are adjacent. Every
two-edge complement has slack 2pi-2theta(a,b)>0 by closure. In particular
Delta=2pi-2theta(k+2,k+1)>0, so the configuration is fully feasible.
There are no nonadjacent pairs and no equality case. In (11a), B is the
single edge (n-1,n); its forced value theta(n,n-1)<pi also rules out a
negative Delta directly.

For N=4 the tour is (k,k+2,k+1,k+3). Its four adjacent pairs have
one-edge slack zero and three-edge complement slack 2pi-2theta(a,b)>0.
There are precisely two nonadjacent pairs and four two-edge directions:

| Endpoints | First path | Second path |
|---|---|---|
| k, k+1 | k,k+2,k+1 | k,k+3,k+1 |
| k+2, k+3 | k+2,k,k+3 | k+2,k+1,k+3 |

All four defects are >=Delta by the triangle lemma; only the path through
k in the second row equals Delta. In particular the seam complement has
two edges, not an assumed three or more, and its defect is strictly
greater than Delta. This proves sufficiency even under the hypothetical
Delta=0 in this case; section 6 will exclude equality in the integer domain.

For any N>=4 under Delta=0, the two-edge seam is feasible with equality,
all other paths with at least two edges have strictly positive slack by
section 3, and single edges have zero slack. Tangency is permitted in full
feasibility. Under Delta>0, the least nonadjacent directed-path slack is
exactly Delta, uniquely at the two-edge seam up to reversal. For N=4 its
complement is larger by the strict triangle lemma; for N>=5 it is larger
by (1). These statements do not extend that minimum to adjacent one-edge
paths, whose slack is zero.

Finally, at any feasible radius r for this same order, summing its N
adjacent angular-gap constraints gives C_{k,n}(r)<=2 pi. Strict decrease
of C implies r>=R. When Delta>=0, the feasible placement at R proves (2), entirely
within the fixed-order problem.

## 5. Parity audit, including the central correction

The proof in sections 2-4 does not interpolate a chain root or replace an
edge sum by an approximation. Nevertheless the exact cycle used for its
closure must include every edge. Put L=n+k for arbitrary k,n in the domain.

| Cycle size | Exact cyclic edge multiset |
|---|---|
| N=2h, h>=2 | (k,n), (k+h-1,k+h), (i,L-1-i) for k<=i<=k+h-2, (i,L+1-i) for k+1<=i<=k+h-1 |
| N=2h+1, h>=1 | (k,n), (i,L-1-i) for k<=i<=k+h-1, (i,L+1-i) for k+1<=i<=k+h |

These are the imported exact rank-tour formulas. In the even case there
are 2+(h-1)+(h-1)=2h edges, including the central edge with consecutive
endpoints p=k+h-1=(L-1)/2 and p+1. In the odd case there are
1+h+h=2h+1 edges and no extra central edge. Both contain (k,n) and
(k,n-1); the rank tour proves they form one cycle with no repeated vertex.

An explicit check against a symmetrized angular sum makes the parity
correction unambiguous. At any R>0 define

```text
B_R = theta_R(k,n)
    + (1/2) sum_{i=k}^{n-1} theta_R(i,L-1-i)
    + (1/2) sum_{i=k+1}^{n} theta_R(i,L+1-i).

C_{k,n}(R) = B_R - e_R,

e_R = 0,                                               N odd,
e_R = [theta_R(p,p)+theta_R(p+1,p+1)]/2
          - theta_R(p,p+1),                             N even. (12)
```

For odd N, the two reflection axes are half-integral, so every term is
paired with a distinct reflected term. For even N, the two diagonal terms
at p and p+1 occur with weight 1/2; subtracting e_R replaces them by the
one actual central edge. By symmetry and (4),
2e_R=integral_p^{p+1} integral_p^{p+1} theta_12(x,y) dy dx>0.
This is an exact
angular identity, not the square-root-weight correction used in an
asymptotic edge-weight sum. No such symmetrization is needed for (9)-(11):
they use the actual edges in either parity. Reversing either cycle simply
exchanges the two paths and leaves all bounds intact.

## 6. Complete integer classification, after the equivalence

Now import the seam signs, which were not premises of sections 2-5.
[FIXED_K_SUPNICK_SEAM.md](FIXED_K_SUPNICK_SEAM.md) proves Delta>0 on
k+2<=n<=4k and, for n>=4k+1, sign(Delta)=-sign(R_{k,n}-T_{k,n}).
The latter difference strictly increases in n. The exact endpoint bridges
in the [radius-1](RADIUS1_SEAM_OBSTRUCTION.md),
[radius-2](RADIUS2_SEAM_THRESHOLD.md), [radius-3](RADIUS3_SEAM_ONSET.md),
[radius-4](RADIUS4_SEAM_ONSET.md), and [radius-5](RADIUS5_SEAM_ONSET.md)
notes put strict opposite signs at s_k-1 and s_k, where respectively
s_k=8,13,17,21,25. Monotonicity and the no-threshold range cover every
other n for those five k, with no equality.

For all k>=6, [SUPNICK_SEAM_SEQUENCES.md](SUPNICK_SEAM_SEQUENCES.md),
section 6, gives D_5(k)<0<D_6(k) by its sequence inequalities and the
exact radius-6 bridge. The same fixed-k theorem therefore gives
Delta>0 for k+2<=n<=4k+5 and Delta<0 for n>=4k+6, with no equality.
The already proved radius-7 through radius-10 onsets agree with this
formula; they are not additional premises needed for the infinite family.

Applying the equivalence, and only now, gives the complete classification:

| k | Fully feasible at R_{k,n} (Delta>0) | Infeasible at R_{k,n} in this fixed order (Delta<0) |
|---|---|---|
| 1 | 3<=n<=7 | n>=8 |
| 2 | 4<=n<=12 | n>=13 |
| 3 | 5<=n<=16 | n>=17 |
| 4 | 6<=n<=20 | n>=21 |
| 5 | 7<=n<=24 | n>=25 |
| every k>=6 | k+2<=n<=4k+5 | n>=4k+6 |

Thus no integer k>=1,n>=k+2 realizes Delta=0. The equivalence nevertheless
proved sufficiency for the weak inequality before excluding equality.
The N=3 and N=4 families lie in the feasible column (also n=k+3<=4k for
N=4 and k>=1). Formula (2) applies in that column. In the other column no
placement of this order attains its chain lower bound. No value or contact
structure at a larger fixed-order radius is determined here.

## 7. Evidence classification and limits

The triangle lemma, its equality conditions, the telescoping identity,
the two directional bounds and the fixed-order corollary are analytic
exact results throughout k>=1,n>=k+2. The equivalence uses the kernel,
the exact cycle and closure, without any seam-sign import. The classification
in section 6 is a proved fixed-order corollary of the equivalence and the
explicitly imported exact sign theorems; no finite scan is a premise.

The dossier's independent symbolic audit differentiates the original
kernel and checks algebra and formal edge multiplicities. Its finite
order/path checks guard against transcription and indexing errors; they
are not an all-k proof. The bounded high-precision diagnostic is only a
numerical observation and cannot certify an exact root.

No production evaluator, independent global verifier, global certificate,
publication asset or prior theorem is changed. Independent human proof
review and manual integration remain outstanding. Detailed commands and
limitations are in
[the classification task evidence](../ops/TASK-20260904__supnick_feasibility_classification/EVIDENCE.md).
The earlier n=4k+5 proof and its checks remain recorded in
[the boundary-family dossier](../ops/TASK-20260904__supnick_full_feasibility/EVIDENCE.md).
