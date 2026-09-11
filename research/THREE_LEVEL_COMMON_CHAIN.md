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
