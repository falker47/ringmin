# Supnick seam dominance and fixed-order full feasibility

```text
status=PROVED
domain=integers k >= 6, n = 4k+5
proved_on=2026-09-04
published_snapshot=arXiv v1 remains unchanged
```

## 1. Statement, definitions and imported premises

For R,a,b>0 set

```text
theta_R(a,b) = 2 asin sqrt(ab/((R+a)(R+b))).
```

Fix an integer k>=6, put n=4k+5 and N=n-k+1=3k+6, and let sigma be the
canonical Supnick cycle on {k,...,n}. All radii occur once. Let
R=R_{k,n}>0 be its exact chain root, so the sum over all N adjacent edges
is 2 pi. Write theta=theta_R and

```text
Delta = theta(n,k) + theta(k,n-1) - theta(n,n-1).
```

The only imported seam premises are:

- [The sequence theorem](SUPNICK_SEAM_SEQUENCES.md), including its radius-6
  bridge, gives D_5(k)=R_{k,4k+5}-T_{k,4k+5}<0 for every integer k>=6.
- [The fixed-k theorem](FIXED_K_SUPNICK_SEAM.md), sections 1-3, supplies the
  exact order, unique root, and sign equivalence. Here n>=4k+1 is in the
  positive-threshold domain, so D_5(k)<0 gives **Delta>0**. In both order
  parities, the neighbors of k are exactly n and n-1.

The angular kernel and geometric interpretation are those of the published
angular lemma. Its monotonicity and positive mixed derivative are rederived
below. Full feasibility is not an imported premise.

For a simple path P=(v_0,...,v_m) of m adjacent edges of this cycle define

```text
S(P) = sum_{j=0}^{m-1} theta(v_j,v_{j+1}) - theta(v_0,v_m).
```

**Exact theorem.** For every nonadjacent pair and each of its two cyclic
paths P, separately,

```text
S(P) >= (m-1) Delta >= Delta > 0.                         (1)
```

The minimum over all such pair/path choices is exactly Delta, attained by
the two-edge seam n,k,n-1 (or its reversal). Every other unoriented path
has strictly larger slack. The formal placement with all adjacent angular
gaps equal to theta is fully feasible.

**Proved fixed-order corollary.** For this order on this radius set,

```text
R_full(sigma) = R_chain(sigma) = R_{k,4k+5}.               (2)
```

The result concerns this fixed-order problem only. It makes no assertion
about global optimality, R*(n), global contact graphs, or floating behavior.

## 2. Exact minimum of every triangle defect

This lemma is valid at every R>0, before imposing the chain equation and
without requiring the seam defect to be positive. In this section write

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

Only now specialize to the exact chain root and invoke Delta>0. For
m>=2 the bound implies S(P)>=Delta. For m>2 it is strictly greater than
Delta. For m=2 the equality statement in the triangle lemma identifies
exactly the seam and its reversal.

Positivity is essential at this last step: if delta_R<0, the telescoping
bound alone would not imply S(P)>=delta_R or any feasibility statement.

## 4. Both cyclic directions and the actual geometric placement

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

No assumption about which path subtends the smaller angle is made. Exact
closure gives their lengths A_++A_-=2 pi. Define positions by cumulative
adjacent angles, phi_0=0 and phi_i=sum_{j=0}^{i-1} theta(s_j,s_{j+1}).
All increments are positive. Equation (10) implies

```text
A_+ >= theta(s_i,s_j)+Delta,
A_- >= theta(s_i,s_j)+Delta,

theta(s_i,s_j) <= A_+ <= 2 pi-theta(s_i,s_j).              (11)
```

Thus min(A_+,A_-) in [0,pi] is at least the required angle. For adjacent
endpoints, the one-edge direction has slack zero; its N-1-edge complement
has slack at least (N-2)Delta>0 by (9). Adjacent pairs therefore satisfy
both constraints too, including the cyclic closing edge.

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

The seam n,k,n-1 is present in the cycle and has slack exactly Delta.
Its complementary path has N-2 edges and slack at least (N-3)Delta>Delta,
as N>=24. This also proves the stated minimum and uniqueness among
unoriented pair/path choices.

Finally, at any feasible radius r for this same order, summing its N
adjacent angular-gap constraints gives C_{k,n}(r)<=2 pi. Strict decrease
of C implies r>=R. The feasible placement at R proves (2), entirely
within the fixed-order problem.

## 5. Parity audit, including the central correction

The proof in sections 2-4 does not interpolate a chain root or replace an
edge sum by an approximation. Nevertheless the exact cycle used for its
closure must include every edge. Put L=n+k=5k+5.

| k | N=3k+6 | Exact cyclic edge multiset |
|---|---|---|
| even | 2h | (k,n), (k+h-1,k+h), (i,L-1-i) for k<=i<=k+h-2, (i,L+1-i) for k+1<=i<=k+h-1 |
| odd | 2h+1 | (k,n), (i,L-1-i) for k<=i<=k+h-1, (i,L+1-i) for k+1<=i<=k+h |

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
one actual central edge. By (4), e_R>0 in the even case. This is an exact
angular identity, not the square-root-weight correction used in an
asymptotic edge-weight sum. No such symmetrization is needed for (9)-(11):
they use the actual edges in either parity. Reversing either cycle simply
exchanges the two paths and leaves all bounds intact.

## 6. Evidence classification and limits

The triangle lemma, its equality conditions, the telescoping identity,
the two directional bounds and the fixed-order corollary are analytic
exact results. They use the explicitly imported all-k positive seam
theorem; no finite root or parity scan is a premise.

The dossier's independent symbolic audit differentiates the original
kernel and checks algebra and formal edge multiplicities. Its finite
order/path checks guard against transcription and indexing errors; they
are not an all-k proof. The bounded high-precision diagnostic is only a
numerical observation and cannot certify an exact root.

No production evaluator, independent global verifier, global certificate,
publication asset or prior theorem is changed. Independent human proof
review and manual integration remain outstanding. Detailed commands and
limitations are in
[the task evidence](../ops/TASK-20260904__supnick_full_feasibility/EVIDENCE.md).
