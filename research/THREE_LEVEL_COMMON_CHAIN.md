# A three-level common-chain lower bound from two shared cutoff budgets

**Status: exact theorem / rigorous continuum relaxation / proved finite
and global corollary, after arXiv v1.** Independent acceptance is separate.

## 1. Fixed question and result

Use precisely the terminal optimizer and original radii:

```text
tau=cos(tau), 0<tau<1,
q=q_*=(1-sin(tau))/(1+sin(tau))=1/lambda_*,
beta_1=1/5, beta_2=23/100,
T_b(n)={floor(b*n),...,n},
C=C_term, J=pi*C=integral_q^1 sqrt(x*(1+q-x)) dx,
D_i=integral_q^beta_i [1+q-x-2*sqrt(x*(1+q-x))] dx.
```

For a cyclic order sigma on T_q(n), let sigma_i be its cyclic restriction
to T_beta_i(n), retaining the original radii. Define

```text
B_n^(3)=min_sigma max{R_chain(sigma),R_chain(sigma_1),R_chain(sigma_2)}.
```

The restrictions are nested: sigma_2=sigma_1|T_beta_2(n). They are not
chosen independently. This note uses the two fixed positive witnesses

```text
h_1=3/1000, h_2=9/1000, H=h_1+h_2=3/250,
Q_3=h_1^3+h_2^3=189/250000000,
L=16+432*H=2648/125,
zeta=(h_1*D_1+h_2*D_2-8*Q_3)/L,
eta_3=zeta/pi,
A_3=1+[5+19*H/(2*L)]/pi < 2.593263.
```

Here Q_3 is just a strip-width expression, unrelated to an upper
construction. In particular eta_3 is not a new meaning for eta_split.
For every integer n>=1000 the exact finite theorem is

```text
R*(n) >= B_n^(3),
B_n^(3)/n^2 >= C+eta_3-A_3/n.                           (1)
```

Exact rational enclosures, proved in Section 6, give

```text
2.6023553183e-7 < eta_3 < 2.6023553184e-7,
eta_3 > eta_split + 11/2000000000.                      (2)
```

Consequently

```text
liminf B_n^(3)/n^2 >= C+eta_3,
liminf R*(n)/n^2 >= C+eta_3 > C+eta_split+11/2000000000,
R*(n) >= B_n^(3) > (C+eta_split+11/2000000000)*n^2
                                                   for n>=10^12. (3)
```

This resolves the stated discriminator by a positive improvement. It does
not compute the three-level minimax, show a sharp constant or a normalized
global limit, or provide a geometric upper construction or finite optimum
certificate. The witnesses h_i are held fixed; no strip-width optimization,
tour enumeration or tuning of the old two-level constants is needed.

## 2. Precisely justified finite stability inputs

The dependencies are [common-chain Sections 2-5 and 11.1-11.3](COMMON_CHAIN_QUANTITATIVE_STABILITY.md).
Their original beta=23/100 statement cannot simply be declared a theorem
for a second beta. The following checks justify reuse of the proof.

Set k=floor(q*n), ell_i=floor(beta_i*n), a=k/n, s=1+a,
V={k/n,...,1}, B_i=(ell_i-1/2)/n, and r(x)=s-x. For n>=1000,
the rational parameter gates 0.19502009<q<0.19502010 give

```text
1/6<a<=q<ell_1/n<=beta_1<ell_2/n<=beta_2<s/2,
s-2*beta_i>1/2,
B_2-B_1=(ell_2-ell_1)/n >= 3/100-1/n >= 29/1000 > H.    (4)
```

Both deleted sets are nonempty and both surviving cycles have at least
three vertices. Thus the same grid reflection, midpoint strip count,
derivative bounds and maximal-run estimates apply at each cutoff.

Write W_0=n^-2 sum_edges sqrt(u*v) for sigma and W_i for sigma_i, and

```text
J_n=(1/n)*sum_{x in V} sqrt(x*(s-x)), e=W_0-J_n,
D_(i,n)=(1/n)*sum_{j=k}^{ell_i-1} [s-j/n-2*sqrt((j/n)*(s-j/n))],
Delta_i=W_i-W_0-D_(i,n),
mu_n=(1/(2*n))*sum_{oriented outer edges (x,y)} delta_(x,r(y)),
nu_n=(1/n)*sum_{x in V} delta_x,
E=integral (x-z)^2 dmu_n(x,z),
K_i=integral |x-z|*1_{(x-B_i)*(z-B_i)<0} dmu_n(x,z).
```

Each undirected cyclic edge has two orientations. Both marginals of the
SAME mu_n equal nu_n exactly; its total mass is (n-k+1)/n. Reusing the
dual potential h from common-chain Section 3 (distinct from the constants
h_i above) gives

```text
e>=0, E<=8*e.                                            (5)
```

This comes from pointwise anti-Monge dual slack and degree two, not
uniqueness of a minimizing tour or an assumption of closeness in order.

For clarity, the deletion proof at either cutoff has the following
specific ingredients. Put p(x)=(1-sqrt(x/(s-x)))/2 and

```text
L_i=2*integral p(x)*1_{x<B_i}*(x-z) dmu_n(x,z).
```

Isolated deleted vertices have Taylor remainder at most 3 times the sum
of squared incident defects. A maximal deleted run with m>=2 vertices
has m-1 LL edges; its discrepancy is at most 4m, while its contribution
to the omitted first variation is at most m. Hence all bad runs together
cost at most 10*M_LL/n, and M_LL/n<=4E by (4). This proves
|Delta_i-L_i|<=43E. The smooth p has |p|<1 and |p'|<11 on [a,1].
Integrating its cutoff primitive and using equal marginals proves
|L_i|<=11E+2K_i. Thus, for both restrictions,

```text
|Delta_i|<=54*E+2*K_i.                                  (6)
```

Runs are counted cyclically after rotating to a survivor, so this includes
consecutive deletions and the wrap. Neither computation depends on either
cardinality parity. Each cutoff midpoint avoids all grid points, giving

```text
nu_n({x:|x-B_i|<=h})<=4*h for every h>0.                 (7)
```

Finally the same rectangle and moving-endpoint estimates apply because
all arguments lie in [1/6,1], and ell_i/n>q:

```text
|J_n-J|<=5/n, |D_(i,n)-D_i|<=19/(2*n).                 (8)
```

The order-uniform angular sandwich in common-chain Section 2 gives, for
each of these three cycles,

```text
W_i/pi-1/n <= R_chain(sigma_i)/n^2 <= W_i/pi,             (9)
```

where sigma_0=sigma. No chain-scale assumption precedes this inequality.

## 3. The new joint crossing inequality

**Lemma.** Let mu have equal grid marginals as above, and cutoffs B_1<B_2
satisfy (7). For any h_1,h_2>0 with h_1+h_2<=B_2-B_1,

```text
h_1*K_1+h_2*K_2 <= 4*(h_1^3+h_2^3)+E.                 (10)
```

Proof. Put d=|x-z|. At cutoff i, split crossing pairs into short d<=h_i
and long d>h_i. A short crossing starts within distance h_i of B_i, so
its weighted integral is at most h_i^2 times that strip's marginal mass,
at most 4h_i^3. On a pair crossing only one cutoff, its long contribution
is h_i*d<=d^2. A pair crossing both has d>=B_2-B_1>=h_1+h_2 and is long
at both cutoffs; its combined contribution is (h_1+h_2)*d<=d^2.
Integrating bounds the TOTAL long contribution by E once. This proves
(10), including equality cases in the length split.

The shared E is the extra information. Separate one-cutoff inequalities
would spend E twice. No independence of the two crossing events is
assumed; long pairs that cross both are explicitly covered.

Multiply the lower half of (6) by h_i, sum, and use (10) and (5):

```text
h_1*W_1+h_2*W_2
 >= H*W_0+h_1*D_(1,n)+h_2*D_(2,n)-8*Q_3-(54*H+2)*E
 >= H*(J_n+e)+h_1*D_(1,n)+h_2*D_(2,n)-8*Q_3-L*e.       (11)
```

The constants 54 and 8 from the existing anti-Monge/deletion estimates
are unchanged. The new inequality is genuinely joint information about
two different macroscopic cutoffs.

## 4. A rigorous continuum common-order relaxation

Let lambda_b denote Lebesgue measure restricted to [b,1], without
probability normalization. Consider symmetric nonnegative measures gamma_i
on [b_i,1]^2, each with both marginals lambda_(b_i), where
b_0=q, b_1=beta_1, b_2=beta_2. Put

```text
w_i=integral sqrt(x*y) dgamma_i,
mu=(x,y -> x,1+q-y)_# gamma_0,
E=integral (x-z)^2 dmu, e=w_0-J,
K_i=integral |x-z|*1_{(x-beta_i)*(z-beta_i)<0} dmu,
l_i=2*integral [(1-sqrt(x/(1+q-x)))/2]*1_{x<beta_i}*(x-z) dmu.
```

Define the relaxed feasible set by these marginal requirements and

```text
e>=0, E<=8e, |w_i-w_0-D_i-l_i|<=43E, i=1,2.            (12)
```

The same primitive argument gives |l_i|<=11E+2K_i. The continuum marginal
has strip mass at most 2h, hence also at most the deliberately retained
4h of (7); therefore (10) applies unchanged at separation 3/100.
In particular (12) implies the continuum version of (11).

This is a relaxation of a common cyclic order, not three freely minimized
assignment problems. Both deletion discrepancies are tied to one outer
measure mu. The inner measures need not be recoverable from that measure;
we assert necessity and no converse or tour recovery theorem.

Here is the limiting argument. For any sequence of outer tours with
n->infinity, form gamma_(i,n) by giving each oriented edge of its ith
restriction mass 1/(2n). Its marginals are the corresponding grid
measures. Compactness of finite measures on the fixed compact square,
with masses at most one, gives simultaneous weakly convergent
subsequences. Their limits have the symmetric Lebesgue marginals above.
The continuous edge costs converge, as do J_n and D_(i,n) by (8).
The reflection s=1+floor(q*n)/n converges uniformly to 1+q. The only
discontinuities in cutoff integrands occur on x=beta_i or z=beta_i;
these lines have zero limiting mass because both marginals are Lebesgue.
One may remove strips of width epsilon, pass to the limit off the strips,
then send epsilon to zero. This also handles the moving B_i. Thus (5)
and the stronger finite |Delta_i-L_i|<=43E pass to (12).

Applying this to minimizing tours along a liminf subsequence and using
(9) proves

```text
liminf B_n^(3)/n^2 >= inf_(12) max{w_0,w_1,w_2}/pi.     (13)
```

There is no exchange of a minimum and a limit. Section 5 bounds the
right side from below by C+eta_3; it also proves the stronger uniform
finite statement directly, so compactness is not a substitute for finite
transfer. The outer reflection reference is an assignment relaxation,
never asserted to be an actual cycle.

## 5. Finite minimax and full-geometric transfer

Set F_n=h_1*D_(1,n)+h_2*D_(2,n)-8*Q_3. Since the maximum of W_1,W_2
is at least their positive weighted average, (11) gives

```text
max{W_0,W_1,W_2} >= J_n+max{e, F_n/H-(L/H-1)*e}.
```

Here L/H>1. For any real F_n the minimum of this last maximum over e>=0
is (F_n)_+/L: for F_n>0 the increasing and decreasing branches meet at
e=F_n/L, and for F_n<=0 the value at e=0 is zero. Taking finite minima
and using (9) proves the stronger finite formula

```text
B_n^(3)/n^2 >= [J_n+(F_n)_+/L]/pi-1/n, n>=1000.        (14)
```

By (8), F_n>=L*zeta-19H/(2n), and (F_n)_+>=F_n. Thus (14) implies
(1) for B_n^(3), with exactly the displayed A_3. This proof covers small
excess, large excess, both parities, every floor, and even a negative
finite numerator; it has no implicit asymptotic order-dependent error.

To prove the separate geometric inequality in (1), take ANY full feasible
configuration at radius R, with order omega on {1,...,n}. Restricting to
each terminal subset preserves all original radii and all surviving pair
constraints. For each consecutive surviving pair u,v, its directed gap g
satisfies min{g,2*pi-g}>=theta_R(u,v), so g>=theta_R(u,v). Summing over
the restricted cycle, including its closing gap, gives a chain sum at
most 2*pi. Strict monotonicity implies R_chain(omega|T_b(n))<=R for
all three b. Their common outer order is sigma=omega|T_q(n), and the
two subsequent restrictions agree exactly with sigma_i.

Taking infima over feasible configurations of each full order and then
minimizing over full orders proves R*(n)>=B_n^(3). Neither attainment,
deletion from a merely chain-feasible arrangement, nor a reconstruction
at the chain radius is assumed. This is the required order-uniform finite
transfer; (3) is propagated only after this proof.

## 6. Exact strictness, evidence and scope

The [standalone checker](../ops/TASK-20260911__three_level_common_chain/check_three_level.py)
uses standard-library integers and fractions only for its proof gates.
Alternating Taylor bounds bracket tau, sin(tau), q and Machin's pi.
For each D_i use q_- as parameter and substitute z=(1+q_--2x)/(1+q_-).
With s=1+q_-, z_q=(1-q_-)/s and z_b=(s-2beta_i)/s,

```text
integral_q_-^beta_i sqrt(x*(s-x)) dx
 = (s^2/4)*integral_z_b^z_q sqrt(1-z^2) dz,
sqrt(1-z^2)=1-sum_(j>=1) c_j*z^(2j),
c_j=binomial(2j,j)/(4^j*(2j-1))>0.
```

Integrate 80 terms exactly. Since c_j decreases, the omitted integral
is between zero and
(s^2/4)*(z_q-z_b)*c_81*z_q^162/(1-z_q^2). The resulting interval for
D_i is widened by 4*(q_+-q_-), which bounds its moving-endpoint and
parameter errors on these intervals. This proves, in particular,

```text
0.0005467128705163 < D_1 < 0.0005467128705164,
0.0024141028962390 < D_2 < 0.0024141028962391.            (15)
```

The checker uses the unrounded rational bounds, rather than (15), in
the linear expression for zeta and opposite pi endpoints for eta_3.
It independently brackets the old cubic root
432*t^3+24*t^2=D_2 to obtain eta_split=t^3/pi, so the strict comparison
does not depend on a copied decimal claim. Rational comparisons prove
(2), A_3<2.593263, and the finite n=10^12 gate in (3).

Bounded measure checks exercise the midpoint count, exact grid marginals,
single and double cutoff crossings, and both grid cardinality parities.
Negative controls exhibit why independent crossing budgets do not imply
(10), and why a cutoff through a grid point would invalidate (7) at tiny
h. They neither enumerate tours nor prove the all-order statements, which
are supplied analytically above. The existing optimized-split checker is
also run independently as a dependency check; it is not imported.

Separate single-cutoff scalar information does not already yield this
improvement: at e=m(D_2), one can formally set W_1=W_2=W_0, with
Delta_i=-D_i, because 0<D_1<D_2=432e+24e^(2/3). Those data satisfy both
individual envelopes. The joint inequality excludes them. This is an
obstruction only to that uncoupled scalar inference, not an upper bound
on the two-level method. No minimizing tour or sharpness is asserted.

The [task evidence](../ops/TASK-20260911__three_level_common_chain/EVIDENCE.md)
records commands, environment, negative evidence and limitations. Stable
claim ownership is the new three-level entry in the global-bounds ledger.
Existing two-level theorems, upper constructions, certificates and the
arXiv-v1 record retain their meanings and contents.

## 7. Any fixed finite number of shared cutoffs

**Status: exact theorem.** Sections 7-10 generalize the crossing argument
and its natural finite corollary; Sections 1-6 retain their fixed constants.
Let m>=1 be finite, B_1<...<B_m, and h_i>0. Let mu be a finite nonnegative
measure on the real plane with finite energy and first marginal nu. Assume

```text
nu({x: |x-B_i|<=h_i}) <= 4*h_i,                          (16)
E = integral |x-z|^2 dmu,
K_i = integral |x-z|*1_{(x-B_i)*(z-B_i)<0} dmu.
```

Equal reflected grid marginals, as in Section 2, imply (16) at midpoint
cutoffs. The crossing lemma itself needs only the displayed first-marginal
bounds. There is exactly one mu and one E, with no probability renormalization.

**Finite shared-crossing lemma.** The explicit adjacent conditions

```text
h_i+h_(i+1) <= B_(i+1)-B_i,       1<=i<m,                (17)
```

imply

```text
sum_i h_i*K_i <= 4*sum_i h_i^3+E.                       (18)
```

For m=1 condition (17) is empty. It permits equality for any m.

Proof. Write d=|x-z| and split each cutoff crossing into short d<=h_i
and long d>h_i. Its short integrand is at most
h_i^2*1_{|x-B_i|<=h_i}; by (16) the sum of all short integrals is at
most 4*sum_i h_i^3. It remains to bound the TOTAL long integrand by d^2.

The strictly crossed cutoffs form a consecutive index block [p,q]. If
there are none, the long integrand is zero; if there is one, it is either
zero or h_p*d<d^2. If q>p, summing (17) gives

```text
sum_(i=p)^q h_i
 = sum_(i=p)^(q-1) (h_i+h_(i+1))-sum_(i=p+1)^(q-1) h_i
 <= B_q-B_p-sum_(i=p+1)^(q-1) h_i
 <= B_q-B_p < d.                                        (19)
```

The empty internal sum is zero. Thus EVERY crossing of this pair is
long, even when it crosses three, four or all m cutoffs, and their total
weighted integrand is d*sum_(i=p)^q h_i<=d^2. Integration spends E once.
A pair with d=h_i belongs to the short part; a pair endpoint exactly at
a cutoff does not strictly cross that cutoff. Neither convention leaves
an unaccounted pair. This proves (18).

Equivalently, (17) says that every block with p<q has
sum_(i=p)^q h_i<=B_q-B_p: adjacent blocks give necessity for this
equivalence, and (19) gives sufficiency. Requiring only the single
outermost-block inequality is insufficient.

## 8. What is sharp, and what fails without separation

**Exact pointwise sharpness.** Define the long weight at a pair by

```text
A_h(x,z) = sum_{i: (x-B_i)*(z-B_i)<0, h_i<|x-z|} h_i.
```

Conditions (17) are necessary and sufficient for the pointwise statement

```text
A_h(x,z) <= |x-z|       for EVERY x!=z in the real line. (20)
```

Sufficiency was proved above. For necessity suppose an adjacent gap
g=B_(j+1)-B_j violates (17). Put

```text
M=max{g,h_j,h_(j+1)}, S=h_j+h_(j+1),
d=(M+S)/2, epsilon=(d-g)/2,
x=B_j-epsilon, z=B_(j+1)+epsilon.
```

Positivity of both widths and g<S imply M<d<S. Both cutoffs are strictly
crossed and long, so A_h(x,z)>=S>d. Any additional crossed cutoffs can
only increase A_h. This is a local obstruction to paying the long terms
by d^2; it proves sharpness of (17) for precisely (20).

For example B=(0,1), h=(3/5,3/5), x=-1/20, z=21/20 give d=11/10 and
long integrand 33/25>121/100=d^2. With B=(0,1,3) and
h=(3/4,3/4,1/4), the outermost sum 7/4<=3 holds, but x=-1/8,z=9/8
already violate (20) at the first two cutoffs.

**Domain qualification.** On a specified grid V, the exact condition for
this pointwise proof is instead the finite family

```text
sum_{i: min(x,z)<B_i<max(x,z), h_i<|x-z|} h_i <= |x-z|
                                      for x,z in V, x!=z. (21)
```

One may further restrict to the support of a particular mu. Condition
(17) suffices for (21), but need not be necessary: if all h_i>=diam(V),
there are no long pairs, regardless of adjacent overlap. This also gives
(18) directly from the short estimate. On a fixed grid, absence of
attainable intermediate distances can matter even for smaller widths.
Thus (17) is sharp for the unrestricted local charging rule (20), not
a claimed necessary condition for the integrated inequality, the best
constant 4, equal-marginal couplings, genuine tours or a geometric minimax.

**Exact negative control for the unrestricted integrated claim.** Merely
dropping separation is in fact invalid for the equal-grid-marginal lemma.
Take n=200, V={j/200:39<=j<=200}, nu=(1/200)*sum_{x in V} delta_x,
and the permutation

```text
T(j)=j+60  for 60<=j<=119,
T(j)=j-60  for 120<=j<=179,
T(j)=j     otherwise.
mu=(1/200)*sum_(j=39)^200 delta_(j/200,T(j)/200),
B=(237/400,239/400,241/400,243/400), h_i=1/10.
```

Both marginals are nu. All cutoffs are grid midpoints, so the original
strip bound holds for every positive width. Reflection r(x)=239/200-x
commutes with this involution T; hence reflecting the second coordinate
back gives a symmetric equal-marginal edge measure as well. It is a
coupling, not a claim of realization as one cyclic tour.

There are 120 moved atoms, each of length 3/10. The four crossing atom
counts are respectively 118,120,118,116; many pairs cross all four.
Exact arithmetic gives

```text
E=27/500,
(K_1,K_2,K_3,K_4)=(177/1000,9/50,177/1000,87/500),
sum_i h_i*K_i=177/2500 > 7/100=4*sum_i h_i^3+E,
excess=1/1250.                                          (22)
```

This refutes the unseparated general lemma even with its correct
marginals and strip counts. It is not a counterexample to (18) under
(17), to the stability theorem, or a statement about tour sharpness.

## 9. The natural finite common-chain minimax corollary

**Status: proved corollary under the existing stability hypotheses.**
Keep q=q_*, C=C_term and all original radii. A concrete domain requiring
no new stability estimates is any fixed finite collection

```text
q<beta_1<...<beta_m<=23/100,
T_b(n)={floor(b*n),...,n}.
```

There are m cutoffs and m+1 chain levels, including the outer chain.
For m TOTAL levels use m-1 cutoffs in the formulas below. Define

```text
sigma_0=sigma cyclic on T_q(n), sigma_i=sigma|T_beta_i(n),
M_(n,m+1)=min_sigma max_(0<=i<=m) R_chain(sigma_i),
k=floor(q*n), a=k/n, s=1+a, ell_i=floor(beta_i*n),
B_i=(ell_i-1/2)/n,
J_n=(1/n)*sum_(j=k)^n sqrt((j/n)*(s-j/n)),
D_(i,n)=(1/n)*sum_(j=k)^(ell_i-1) [s-j/n-2*sqrt((j/n)*(s-j/n))],
D_i=integral_q^beta_i [1+q-x-2*sqrt(x*(1+q-x))] dx,
H=sum_i h_i, Q_3=sum_i h_i^3, L=16+432*H,
F_n=sum_i h_i*D_(i,n)-8*Q_3,
F=sum_i h_i*D_i-8*Q_3, eta(h)=F_+/(pi*L),
A(h)=1+[5+19*H/(2*L)]/pi,       u_+=max{u,0}.
```

At any integer n and positive widths (allowed to depend on n) satisfying

```text
n>=102, ell_1/n>q, ell_1<...<ell_m<=n-2,
h_i+h_(i+1) <= (ell_(i+1)-ell_i)/n    for 1<=i<m,       (23)
```

the finite, order-uniform conclusions are

```text
R*(n) >= M_(n,m+1),
M_(n,m+1)/n^2 >= [J_n+(F_n)_+/L]/pi-1/n,               (24)
M_(n,m+1)/n^2 >= C+[(F-19*H/(2*n))_+/L-5/n]/pi-1/n
              >= C+eta(h)-A(h)/n.                     (25)
```

In the m=1 case omit all adjacent conditions. The positive part handles
negative, zero and positive numerators; no gain is asserted when F<=0.

To justify every reused input, n>=102 implies 1/6<a<=q<1/5. Every
deleted x satisfies x<ell_i/n<=23/100, and
s-2*(ell_i/n)>7/6-46/100=53/75>1/2. The cutoff is a midpoint, the
deleted set is nonempty, and at least three vertices survive. Thus the
Hessian bounds, cyclic maximal-run accounting, primitive derivative
bounds and moving-endpoint estimates in Sections 2 and the linked
common-chain Sections 2-5 and 11.1-11.3 apply at EACH cutoff unchanged.
In particular for the SAME outer measure, with W_i the normalized
sqrt-product edge costs and e=W_0-J_n, they give

```text
e>=0, E<=8*e, |W_i-W_0-D_(i,n)|<=54*E+2*K_i,
|J_n-pi*C|<=5/n, |D_(i,n)-D_i|<=19/(2*n),
W_i/pi-1/n <= R_chain(sigma_i)/n^2 <= W_i/pi.           (26)
```

No new stability theorem for arbitrary cutoffs or arbitrary radius
sequences is inferred. More generally, (24) is conditional on precisely
the first and last lines of (26) and (18); (25) additionally uses the
middle error bounds. The domain above explicitly supplies all of them.

Multiply each lower deletion estimate by h_i, sum, and use (18):

```text
sum_i h_i*W_i >= H*(J_n+e)+F_n-(54*H+2)*E
              >= H*(J_n+e)+F_n-L*e.
```

The energy coefficient is 8*(54*H+2)=L, not m copies of 16. Taking the
positive weighted average of the inner costs and retaining the outer
one yields

```text
max_(0<=i<=m) W_i >= J_n+max{e,F_n/H-(L/H-1)*e}.
```

Since L>H>0, the exact scalar infimum over e>=0 is (F_n)_+/L: at
F_n>0 the branches meet at e=F_n/L, and at F_n<=0 the minimum is zero
at e=0. This is sharp only for these two aggregate scalar branches.
Taking finite minima and the angular lower sandwich proves (24) for
M. The error estimates and the monotone, 1-Lipschitz positive-part map
prove (25). All orders, both cardinality parities, wrap and floors are
included; the error is uniform in the order. Setting m=2 and the fixed
witnesses of Section 1 recovers (14) and its A_3 exactly.

For fixed widths with strict macroscopic margins

```text
delta_i=beta_(i+1)-beta_i-h_i-h_(i+1)>0,
```

choose any integer N>=102 with N*(beta_1-q)>1 and N*delta_i>=1 for
all i. Then (23) holds for every n>=N, since
(ell_(i+1)-ell_i)/n>=beta_(i+1)-beta_i-1/n; the last surviving-cycle
size condition follows from beta_m<=23/100. Hence

```text
liminf_(n->infinity) M_(n,m+1)/n^2 >= C+eta(h),
liminf_(n->infinity) R*(n)/n^2 >= C+eta(h).              (27)
```

Weak macroscopic separation also suffices for (27): apply the strict
result to t*h with any fixed 0<t<1, then let t increase to 1 and use
continuity of eta. This limit neither optimizes widths nor exchanges a
minimum and a limit. Weak macroscopic separation alone does NOT imply
the finite (23) at the unchanged widths; the floor loss must be checked.
The theorem fixes m independently of n and asserts no infinite-cutoff
or growing-m limit.

Finally the geometric inequality must be proved from full feasibility.
Take any full feasible configuration at R and order omega on {1,...,n}.
Deletion to each T_b(n), for b=q,beta_1,...,beta_m, preserves original
radii and every surviving pair constraint. Each consecutive directed
gap g in its restricted cycle satisfies
min{g,2*pi-g}>=theta_R(u,v), hence g>=theta_R(u,v). Summing all gaps,
including the closing one, and using strict decrease of the chain sum
gives R_chain(omega|T_b(n))<=R. All restrictions come from the same
sigma=omega|T_q(n), and remain nested. Thus M_(n,m+1)<=R for EVERY
full feasible configuration; taking infima proves R*(n)>=M_(n,m+1).
No attainment, deletion from a merely chain-feasible arrangement, or
reconstruction at the chain root is required. This proves the global
parts of (24)-(27) separately from the scalar calculation.

## 10. Bounded checks and stopping scope for the generalization

The [finite-cutoff standalone checker](../ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py)
uses only standard-library rational arithmetic and no production, prior
checker or saved-result imports. Prescribed small grid couplings exercise
one, two, four and eight cutoffs, short/long equality, adjacent separation
equality, both parities and pairs crossing every cutoff. Exact controls
check the local overlap obstruction, insufficient outermost separation,
the integrated counterexample (22), a harmless overlap on a bounded
domain, separate-budget overspending and macroscopic/finite floor loss.
Scalar and finite-domain gates include all signs of F_n and recovery of
the existing two-cutoff constants. The earlier three-level checker is
rerun as a separate dependency check, without imports between checkers.

These bounded checks corroborate accounting and constants; the analytic
proof supplies the arbitrary finite m, all-order and all-n quantifiers.
The [task evidence](../ops/TASK-20260911__finite_shared_crossing/EVIDENCE.md)
records fresh local commands and limitations. No cutoff/width optimization,
tour enumeration, new numerical coefficient, geometric upper construction,
normalized global limit, expanded finite certificate or paper revision is
part of this corollary. Independent mathematical acceptance remains separate.

## 11. A fixed four-level rational improvement

**Status: exact theorem / proved finite and asymptotic global corollary,
after arXiv v1.** This section applies the finite shared-crossing theorem
and corollary in Sections 7 and 9 to the following fixed user-supplied
rationals, without optimizing or changing any parameter:

```text
beta=(2091/10000, 10907/50000, 23/100),
h=(451/100000, 451/100000, 367/50000).
```

Retain q=q_*, C=C_term, T_b(n) and the original radii as in Section 9.
For one cyclic order sigma on T_q(n), let sigma_i be its restriction to
T_beta_i(n), and define the FOUR-level minimax

```text
B_n^(4)=M_(n,4)=min_sigma max{R_chain(sigma),
                  R_chain(sigma_1),R_chain(sigma_2),R_chain(sigma_3)},
D_i=integral_q^beta_i [1+q-x-2*sqrt(x*(1+q-x))] dx,
H=409/25000, Q_3=sum_i h_i^3=289457303/500000000000000,
L=16+432*H=72086/3125,
F=sum_i h_i*D_i-8*Q_3, eta_4=F/(pi*L),
A_4=1+[5+19*H/(2*L)]/pi < 2.594.
```

The positive numerator F is proved below; hence this eta_4 agrees with
the positive-part definition in Section 9. Here Q_3 still denotes the
sum of cubes, not the number of levels or an upper-bound construction.
The old eta_3, with its old cutoffs and widths in Section 1, is unchanged.
In particular B_n^(4) does not contain the old cutoff 1/5, and no pointwise
comparison B_n^(4)>=B_n^(3) is asserted.

### 11.1 Exact separations and every finite stability gate

The two adjacent macroscopic margins are exactly

```text
beta_2-beta_1=113/12500, h_1+h_2=451/50000,
delta_1=beta_2-beta_1-h_1-h_2=1/50000,
beta_3-beta_2=593/50000, h_2+h_3=237/20000,
delta_2=beta_3-beta_2-h_2-h_3=1/100000.                 (28)
```

Both are strictly positive. Fix N=100000. The checked q bracket in
Section 6 gives N*(beta_1-q)>1, N*delta_1=2 and N*delta_2=1.
For EVERY integer n>=N, put k=floor(q*n), a=k/n, s=1+a,
ell_i=floor(beta_i*n), B_i=(ell_i-1/2)/n. Then

```text
1/6 < q_- - 1/N <= q-1/n < a <= q < 1/5 < beta_1,
ell_1/n > beta_1-1/n >= beta_1-1/N > q,
B_(i+1)-B_i=(ell_(i+1)-ell_i)/n
            > beta_(i+1)-beta_i-1/n >= h_i+h_(i+1),
ell_1<ell_2<ell_3<=n-2,
s-2*(ell_i/n) > 7/6-2*beta_3=53/75>1/2.              (29)
```

For the surviving-size gate, n-ell_3>=n*(1-beta_3)=77*n/100>=2;
thus each restriction has at least three vertices. Also ell_1>k, so all
three deleted sets are nonempty. All cutoffs are below s/2, all radii
are positive, and reflection permutes the outer grid. Every h_i>0.
Midpoints avoid grid points: a strip of radius t<1/(2n) is empty;
otherwise its mass is at most 2t+1/n<=4t. This proves the strip gate
for every t>0, in particular at each of the unchanged h_i.

These are the full hypotheses (23), including n>=102. They also justify
the stability inputs (26) individually at all three cutoffs: 1/6<a<1/5
supplies the Hessian norm bound 6, isolated-deletion remainder 3E,
|p|<1 and |p'|<11; the LL-edge defect is >1/2, so maximal cyclic runs
cost at most 40E in addition to 3E. Marginal cancellation adds 11E+2K_i,
giving |W_i-W_0-D_(i,n)|<=54E+2K_i. The moving-endpoint/rectangle
bounds remain 5/n and 19/(2n), and the angular lower loss remains 1/n.
They all use the SAME outer measure and E<=8e, with no extra copies
of the energy budget. No parity or adjacency-pattern restriction is used.

Summing the finite adjacent inequalities in (29) also controls a pair crossing all
three cutoffs: sum_i h_i<=B_3-B_1-h_2<B_3-B_1. Thus the third crossing
is covered by the single energy term, not by a separate budget.
The floor gate cannot simply be claimed at the older N=1000: there
ell=(209,218,230), and (ell_2-ell_1)/1000=9/1000<451/50000.
This refutes that smaller finite gate, not the fixed witness or its limit.

### 11.2 Rational enclosures and the strict discriminator

The [bounded arithmetic checker](../ops/TASK-20260911__four_level_rational_witness/check_four_level.py)
reproves the tau, q and pi brackets by alternating rational Taylor sums.
It imports neither production code, saved results nor a prior checker.
For each new beta_i it then uses exactly the Section 6 integral enclosure:
at q_-, set s=1+q_-, u=(s-2*beta_i)/s, v=(1-q_-)/s, and

```text
c_j=binomial(2j,j)/(4^j*(2j-1)),
P=v-u-sum_(j=1)^80 c_j*(v^(2j+1)-u^(2j+1))/(2j+1),
T=(v-u)*c_81*v^162/(1-v^2),
I_-=(s^2/4)*(P-T), I_+=(s^2/4)*P,
d_-=s*(beta_i-q_-)-(beta_i^2-q_-^2)/2-2*I_+-4*(q_+-q_-),
d_+=s*(beta_i-q_-)-(beta_i^2-q_-^2)/2-2*I_-+4*(q_+-q_-).
```

All entries are rational and 0<u<v<1. The positive decreasing c_j give
a geometric majorant T for the omitted integral, so d_-<=D_i<=d_+.
For the moving parameter, |partial_q D(q,beta_i)|<=4 follows from
the endpoint bound 2 and integrand derivative bound 2, on a domain
of length at most one. Thus the displayed widening is outward.
This is an enclosure proof, not quadrature or an unbounded numerical sum.

Unrounded rational bounds are propagated through the positive h_i and L.
The old eta_3 is recomputed from its defining cutoffs 1/5 and 23/100
and widths 3/1000 and 9/1000; its decimal enclosure is not a premise.
Opposite pi endpoints give outward quotient bounds. Finally the existing
terminal theorem gives C=tau/(pi*(1+sin(tau)))=tau*(1+q)/(2*pi), so
its positive endpoint products also enclose the full lower coefficient.
The resulting strict rational enclosures are

```text
0.00136820131190299899 < D_1 < 0.00136820131190299902,
0.00196196296152142893 < D_2 < 0.00196196296152142896,
0.00241410289623904894 < D_3 < 0.00241410289623904897,
0.00002810723928353877 < F < 0.00002810723928353880,
0.00000038785322987835 < eta_4 < 0.00000038785322987838,
0.00000026023553183385 < eta_3 < 0.00000026023553183388,
0.00000012761769804449 < eta_4-eta_3 < 0.00000012761769804452,
0.00000002761769804449 < eta_4-eta_3-1e-7
                                      < 0.00000002761769804452,
0.14056946869848664490 < C+eta_4 < 0.14056946869848664493,
2.59369407943386457250 < A_4 < 2.59369407943386457253.   (30)
```

Every displayed terminating decimal denotes an exact rational, enlarged
outwards by integer division of the internal rational endpoints. In
particular F>0 and the requested strict eta_4>eta_3+1/10000000 is proved.

### 11.3 All-n and global consequences of the proved corollary

Let J_n and D_(i,n) retain exactly their Section 9 definitions for these
three cutoffs, and F_n=sum_i h_i*D_(i,n)-8*Q_3. Equations (24)-(26),
with all their gates discharged in (29), prove for every integer n>=100000

```text
R*(n)>=B_n^(4),
B_n^(4)/n^2 >= [J_n+(F_n)_+/L]/pi-1/n
             >= C+eta_4-A_4/n.                        (31)
```

The second inequality uses |J_n-pi*C|<=5/n,
F_n>=F-19H/(2n) and (F_n)_+>=F_n. It holds even if a finite numerator
is negative. The scalar coefficient is L=8*(54H+2)>H, exactly as in
Section 9; the energy is spent once. Full-geometric transfer is that
corollary's separate deletion argument for every full feasible order:
retain original radii, sum the directed surviving gaps including closure,
then minimize over the same outer order and its nested restrictions.
This never assumes chain feasibility implies all-pairs feasibility.

Consequently the exact asymptotic statements are

```text
liminf B_n^(4)/n^2 >= C+eta_4,
liminf R*(n)/n^2 >= C+eta_4 > C+eta_3+1/10000000.       (32)
```

There is also an explicit finite strict conclusion. Since (30) gives
eta_4-eta_3-1/10000000>2.761769804449e-8>2.594/10^8,
(31) yields

```text
R*(n)>=B_n^(4)>(C+eta_3+1/10000000)*n^2
                                      for EVERY n>=10^8. (33)
```

These are analytic all-order and all-n results via the accepted
corollary, supported by bounded exact parameter arithmetic. The checker
does not enumerate tours or prove those universal quantifiers by sampling.
The fixed witness succeeds; no cutoff/width search or adjustment occurred.
No sharp endpoint, normalized global limit, minimizing tour, geometric
upper construction, expanded finite certificate or paper revision follows.
The [owning ledger](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md#four-level-improvement-at-a-fixed-rational-witness)
and [task evidence](../ops/TASK-20260911__four_level_rational_witness/EVIDENCE.md)
record scope and reproducibility. Independent acceptance of this new
fixed-witness theorem remains separate from its accepted general premise.
