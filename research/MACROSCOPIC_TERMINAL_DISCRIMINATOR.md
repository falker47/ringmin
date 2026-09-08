# Macroscopic terminal deletion of a prescribed Supnick cycle

    status=PROVED
    classification=exact chain-limit theorem / exact strict-comparison theorem
    domain=fixed real 0<q<beta<1; n tends to infinity through all integers
    proved_on=2026-09-09
    published_snapshot=arXiv v1 remains unchanged

## 1. Question, definitions and result

Retain the actual integer radii, without translating the angular kernel:

```text
k=floor(q*n),                  ell=floor(beta*n),
T_q(n)={k,...,n},              T_beta(n)={ell,...,n},
S_q(n)=Supnick(T_q(n)),        I_{q,beta}(n)=S_q(n)|T_beta(n),
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_sigma(R)=sum_{cyclic edges (a,b) of sigma} theta_R(a,b).
```

Restriction joins consecutive surviving vertices, including the closing
edge. All assertions about roots concern sufficiently large n, so k>=1,
ell>k and |T_beta(n)|>=3. Earlier sizes where these conditions fail do
not enter the limit. For a cycle with at least three positive radii,
F_sigma is continuous and strictly decreasing from |sigma|*pi to zero;
R_chain(sigma) is its unique positive 2*pi root.

Write s=1+q and c=s/2. Then the following limit exists along all integers,
with error constants independent of the cardinality parities:

```text
R_chain(I_{q,beta}(n))/n^2 = Psi(q,beta)+O_{q,beta}(1/n),

pi*Psi(q,beta) = W(q,beta)
 = 2 integral_beta^c sqrt(x*(s-x)) dx
     + [1-(s-beta)^2]/2,                         q<beta<=c,
 = (1-beta^2)/2,                                 c<=beta<1.       (1)
```

The branches agree at c. An equivalent explicit first branch is

```text
z=1-2*beta/s,
W(q,beta)=(s^2/4)*(asin(z)+z*sqrt(1-z^2))
           + [1-(s-beta)^2]/2.                                  (2)
```

The continuous extension to beta=q has

```text
Psi(q,q)=C(q):=(2/pi) integral_q^((1+q)/2)
                            sqrt(x*(1+q-x)) dx.                  (3)
```

Import precisely the terminal optimizer from
[the terminal-bound proof](INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md),
Sections 5-6:

```text
tau=cos(tau),                 0<tau<pi/2,
q_*=(1-sin(tau))/(1+sin(tau))=1/lambda_*,
C(q_*)=C_term=tau/(pi*(1+sin(tau))).                             (4)
```

Here lambda_* is the terminal-bound optimizer, not a parameter of an
upper-bound construction. The exact comparison is

```text
Psi(q_*,beta)>C_term       for every beta in [1/5,23/100].         (5)
```

More generally it is strict for q_*<beta<=(1+q_*)/5. Thus the proposed
inequality for every beta>q_* is false. This identifies a candidate of
quadratic incompatibility for the prescribed outer Supnick order. It
does not prove a positive quadratic gain of the minimax over common
tours. Section 6 states this logical boundary explicitly.

## 2. Exact surviving and replacement edges below the midpoint

Use the parity-independent rank traversal and the exact undirected edge
formulas in [the fixed-k note](FIXED_K_SUPNICK_SEAM.md), Section 1. Its
ordering premise is [published Theorem A](../paper_assets/ringmin_paper.tex).
Put N=n-k+1, d=ell-k and h=floor(N/2). First suppose

```text
1<=d<=h-1.                                                       (6)
```

Every deleted rank j=1,...,d is a low rank. Rank 1 has neighbors N-1,N;
rank j>=2 has neighbors N-j,N+2-j. Under (6) both neighbors survive,
and no two deleted vertices are adjacent. These statements follow directly
from the two original rank-edge families, including rank 1's special edge.
Deleting such vertices therefore replaces their two incident edges by one
chord each, without any further merging of deleted paths.

The complete restricted edge multiset consists of the following edges
(a range with its upper endpoint below its lower endpoint is empty):

| Original parity | Surviving minus family | Surviving plus family | Extra middle edge |
|---|---|---|---|
| N=2h | (i,n+k-1-i), ell<=i<=k+h-2 | (i,n+k+1-i), ell<=i<=k+h-1 | (k+h-1,k+h) |
| N=2h+1 | (i,n+k-1-i), ell<=i<=k+h-1 | (i,n+k+1-i), ell<=i<=k+h | none |

In both parities add exactly these d replacement chords:

```text
(n-1,n),
(n-j,n+2-j),                       j=2,...,d.                    (7)
```

The top edge (n-1,n) closes the two high arms at the cyclic seam and must
not be omitted. There are N-2*d retained original edges and d new edges,
hence N-d surviving-cycle edges in total. For even N the table contributes
(h-1-d)+(h-d)+1=N-2*d; for odd N it contributes
(h-d)+(h+1-d)=N-2*d. All listed edges are distinct; the table follows
by removing exactly the edges incident to deleted ranks, and (7) joins
their surviving neighbors. This is an exact cyclic identity, not a
replacement of the restricted cycle by the smaller Supnick optimizer.

For fixed beta<c, condition (6) holds for every sufficiently large n.
Normalize an edge weight by defining

```text
W_n=(1/n^2) sum_{(a,b) in I_{q,beta}(n)} sqrt(a*b).
```

Each long original family has normalized first endpoint ranging from
beta+O(1/n) to c+O(1/n) with mesh 1/n. Its second endpoint is
1+k/n +/- 1/n - i/n, so its normalized weight converges to
sqrt(x*(s-x)). Both endpoint and summand errors are O_q(1/n): all
radius factors stay bounded away from zero. The extra middle edge has
weight at most n, hence contributes O(1/n) to W_n.

For (7), j/n ranges from O(1/n) to beta-q+O(1/n). The normalized
endpoint pair is (1-j/n,1-j/n+2/n), and its weight is
1-j/n+O_q(1/n). The separate top chord is another O(1/n) term.
Consequently the entire replacement family contributes

```text
integral_0^(beta-q) (1-t) dt
 = integral_(s-beta)^1 x dx = [1-(s-beta)^2]/2.                    (8)
```

There are O(n) summands, each multiplied by 1/n in W_n. Ordinary
Riemann-sum error, the integer floors, the two original parity endpoint
shifts and the extra edges therefore give

```text
W_n=2 integral_beta^c sqrt(x*(s-x)) dx
      + integral_(s-beta)^1 x dx + O_{q,beta}(1/n).                (9)
```

The replacement chords form two interlaced high paths with step two;
their combined density is one, not two. The two retained original
families each have density one. Formula (9) keeps this distinction.

## 3. Above and at the midpoint; both parity transitions

If the smallest retained rank is greater than ceil(N/2), every retained
vertex is in a high arm or is rank N. The two arms traverse alternating
high ranks in opposite directions. After deleting their lower prefixes,
they join at the two smallest survivors and, through rank N, at the two
largest survivors. Thus the exact edge multiset in actual radii is

```text
{(a,a+2): ell<=a<=n-2} union {(ell,ell+1),(n-1,n)}.              (10)
```

This statement uses only the rank traversal: the two parity classes of
high ranks give the step-two edges, their lower join gives (ell,ell+1),
and the closing join gives (n-1,n). It holds in either parity of N and
either parity of n-ell+1, including three surviving vertices. The edge
count is n-ell-1+2=n-ell+1. For fixed beta>c this condition holds
eventually. Since sqrt(a*(a+2))/n=a/n+O_beta(1/n), (10) gives

```text
W_n=integral_beta^1 x dx+O_beta(1/n)
   =(1-beta^2)/2+O_beta(1/n).                                   (11)
```

For the exact boundary beta=c, choose instead the integer cutoff
ell_0=k+ceil(N/2), whose smallest retained rank is ceil(N/2)+1.
It differs from floor(c*n) by at most two and ell_0/n=c+O(1/n).
Both retained sets have at least three vertices eventually. Removing one
vertex changes at most three edge weights, each at most n, so changing
the cutoff between these two values changes W_n by at most 6/n.
Apply (10)-(11) to ell_0 to obtain (11) with beta=c. Its value equals
the first branch because s-c=c and its integral has length zero.

These arguments cover the parity changes caused by both floor functions,
including the midpoint. No subsequence of even sizes or parity-dependent
redefinition of the tour is used. They also prove W_n=W(q,beta)+O(1/n)
with constants independent of those parities.

## 4. Uniform angular estimate and root transfer

For any edge with 1<=a,b<=n, r>=r_0>0 and R=r*n^2, set
v=sqrt(a*b)/(r*n^2) and
u=v/ sqrt((1+a/(r*n^2))*(1+b/(r*n^2))). The elementary inequalities
0<=1-(1+y)^(-1/2)<=y/2 and 0<=asin(u)-u<=u^3/3 for u<=1/2 imply,
when n>=2/r_0,

```text
|theta_(r*n^2)(a,b)-2*sqrt(a*b)/(r*n^2)|
 <=2/(r_0^2*n^2)+2/(3*r_0^3*n^3).                              (12)
```

For the arcsine bound, integrate
1/sqrt(1-t^2)-1<=t^2 on [0,1/2]. The denominator estimate gives
v-u<=1/(r_0^2*n^2). Thus (12) is valid uniformly even on the new
chords; it does not depend on adjacency in the original tour.
There are at most n edges, so

```text
sup_(r>=r_0) |F_I(r*n^2)-2*W_n/r|
 <=2/(r_0^2*n)+2/(3*r_0^3*n^2).                                (13)
```

Equations (9)-(11) give W>0 for every fixed 0<q<beta<1. Define
psi=W/pi and evaluate (13) first at r=psi/2 and r=3*psi/2.
The limiting closure sums are 4*pi and 4*pi/3. By strict decrease,
the unique exact normalized root r_n is eventually between these two
positive constants. Only after obtaining that bracket, evaluate (13)
at r_n. It yields

```text
2*pi=2*W_n/r_n+O_{q,beta}(1/n),
r_n=W_n/pi+O_{q,beta}(1/n)=Psi(q,beta)+O_{q,beta}(1/n).           (14)
```

This proves (1) without assuming the scale of an unknown root. Substitution
z=1-2*x/s in the first integral gives (2); setting beta=q eliminates
the chord integral and proves (3).

## 5. Exact comparison with the terminal coefficient

For q<beta<c, differentiation of the actual edge integral gives

```text
pi*partial_beta Psi(q,beta)
 = (s-beta)-2*sqrt(beta*(s-beta))
 = sqrt(s-beta)*(sqrt(s-beta)-2*sqrt(beta)).                     (15)
```

Both square roots are positive. Thus its sign is exactly the sign of
s-5*beta. In particular, if q<1/4, the coefficient strictly increases
on (q,s/5) and its value remains above C(q) through beta=s/5.
For beta>c the derivative is -beta/pi; at c the first branch has the
same derivative. These signs concern this prescribed family only.

Here are explicit rational gates for the existing implicit optimizer;
no decimal approximation of tau or C_term is used. Put a=73/100,
b=3/4 and define the usual alternating Taylor polynomials

```text
P_6(x)=1-x^2/2+x^4/24-x^6/720,
P_4(x)=1-x^2/2+x^4/24,
Q_7(x)=x-x^3/6+x^5/120-x^7/5040,
Q_5(x)=x-x^3/6+x^5/120.
```

On 0<x<1, alternating series with decreasing terms give
P_6(x)<cos(x)<P_4(x) and Q_7(x)<sin(x)<Q_5(x). Exactly,

```text
P_6(a)-a   =10924138073711/720000000000000 >0,
b-P_4(b)   =37/2048 >0,
Q_7(a)-2/3 =102214670540903/504000000000000000 >0,
7/10-Q_5(b)=751/40960 >0.                                      (16)
```

Since cos(t)-t is strictly decreasing on (0,pi/2), the first two
gates give a<tau<b. Sine is strictly increasing there, and the last
two give 2/3<sin(tau)<7/10. The decreasing map u -> (1-u)/(1+u)
therefore proves

```text
3/17 < q_* < 1/5 < 1/4,
(1+q_*)/5 > 4/17 > 23/100,     4/17-23/100=9/1700.             (17)
```

For every beta in [1/5,23/100] we now have
q_*<beta<(1+q_*)/5<c_*. Integrate (15) from q_* to beta:

```text
pi*(Psi(q_*,beta)-C_term)
 = integral_(q_*)^beta [(1+q_*-x)-2*sqrt(x*(1+q_*-x))] dx >0.   (18)
```

Every interior integrand is strictly positive, and the interval has
positive length. This proves (5) for the entire closed rational interval,
not merely at sample values. The same argument gives strictness through
beta=(1+q_*)/5, where only the final integrand vanishes.

## 6. Precisely what the positive discriminator implies

For fixed beta>q_* let B_n denote the chain minimax on these two terminal
sets, using one common outer cycle. Its definition permits S_{q_*}(n)
as a comparison cycle, so

```text
B_n <= max{R_chain(S_{q_*}(n)),R_chain(I_{q_*,beta}(n))}.         (19)
```

Had Psi(q_*,beta)<=C_term held, (19) and the outer Supnick lower
minimum would have forced B_n/n^2->C_term for that beta. That would
have been a common-order obstruction to improving C_term with this pair.

Instead (5) proves that, for the displayed interval, this particular
comparison cycle incurs a strictly positive quadratic restricted-chain
excess over its own outer coefficient. Inequality (19) is an upper
comparison for B_n, not a lower comparison. A different sequence of common
tours could alter both costs and remove that excess. Even finite uniqueness
of the Supnick optimizer would not supply quantitative asymptotic stability
over such sequences. Thus this is only a candidate of quadratic
incompatibility, not a proved incompatibility of all common tours and not
a stronger lower bound on the coupled minimax or the global problem.

No common tours are optimized here. No statement concerns R_full, a new
feasible upper construction, floating circles, finite global certification
or a revision of the public paper. The existing C_term is unchanged.

## 7. Evidence and authority

All limit and interval quantifiers are proved analytically above. The
[standalone checker](../ops/TASK-20260909__macroscopic_terminal_discriminator/check_discriminator.py)
audits bounded exact cyclic edge identities and rational Taylor gates;
its optional angular diagnostics use only prescribed orders and are
numerical observations. Neither is a finite global certificate or the
premise of the all-n theorem. Symbolic cross-checks and exact commands
are recorded in the dossier. External independent acceptance is separate.

The sole stable owner of this result is the macroscopic-discriminator
entry in [the global ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
