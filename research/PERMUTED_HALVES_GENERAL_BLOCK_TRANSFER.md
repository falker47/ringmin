# General reflected-block recovery and global transfer

    status=PROVED; INTERNALLY_VALIDATED; external acceptance pending
    classification=exact recovery theorem; full-feasibility and global corollaries
    goal=20260911 research completion, checkpoints 2-3
    historical_arXiv_v1=unchanged

## 1. Statement with no branch hypothesis

Fix 0<=alpha<1 and nonnegative lengths ell_1,...,ell_k, k>=1, with
T=sum ell_j<1-alpha. Let t_0=0, t_j=sum_(h<=j) ell_h, A=1+alpha,
and b=1-alpha. On D=[0,1] x [1,2]^2 define the probability measure

    integral F dmu = (1/2) sum_j integral_(t_(j-1))^(t_j)
      [F(t,A+t,A+t_(j-1)+t_j-t)
       +F(t,A+t_(j-1)+t_j-t,A+t)] dt
      + integral_T^1 F(t,1+{t+alpha},1+{t+alpha}) dt.       (1)

Every low and each high marginal is uniform on its respective interval.
Indeed each reflection is a measure-preserving involution of its own slab,
and the unchanged diagonal shift is a bijection modulo its single wrap.
Zero lengths and endpoint assignments do not change the measure.

Write g=max(sqrt(t)*(sqrt(X)+sqrt(Y)),sqrt(X*Y)), I=integral g dmu,
C(mu)=I/(4*pi). For every integer m>=M=max(2,ceil(2/(1-alpha-T))),
the genuine order in Section 2 has full minimum rho_m and

    |rho_m/(2m)^2-C(mu)|
      <= [(6*k^2+28*k+1060)/m+16384/(3*m^2)]/(4*pi),
                                     m>=max(M,2048).     (2)

It has an all-pairs-feasible placement at rho_m. Deleting the largest label
gives odd feasible placements and hence

    limsup_(n->infinity) R*(n)/n^2 <= C(mu).                (3)

There is no chord-dominance condition, no ordering among the lengths, and no
restriction to a finite list of chosen widths. All actual maxima are retained.
This theorem asserts an upper construction, not global optimality.

## 2. Genuine integer permutations and complete cell inventory

Define exact floors, with rounded starts formed from rounded lengths:

    s=floor(alpha*m), l_j=2*floor(ell_j*m/2),
    a_0=0, a_j=sum_(h<=j) l_h, z=a_k, r=m-s,
    H(u)=m+1+((u+s-1) mod m).

For a_(j-1)<i<=a_j, set J(i)=2*a_(j-1)+l_j+2-i when i is even;
set J(i)=i at every other rank. Put P_i=H(J(i)), P_0=P_m, and
sigma_m=(1,P_1,...,m,P_m). Each block reverses its even ranks and fixes
its odd ranks; disjoint involutions followed by H prove bijectivity.
Lengths 0 and 2 are harmless identities. When l_j=2 modulo 4 there is
one fixed even rank; otherwise a positive block has none. Both parities
of m, all floor ties and arbitrarily many zero lengths are allowed.

Since s+z<=m*(alpha+T), the gate m>=M gives r-z>=2. Thus every block
and its exit lies before the high wrap. In particular P_r=2m, P_m=H(m).
The exact cell list is the following disjoint classification:

- Each nonempty block (a,a+l] has interior cells a+2,...,a+l.
  Even i has (P_(i-1),P_i)=(m+s+i-1,m+s+2*a+l+2-i).
  Odd i has (m+s+2*a+l+3-i,m+s+i).
- The exceptional set is {1,r,r+1} union {a_j+1:l_j>0}, intersected
  with {1,...,m}. Duplicates are counted once; its size is at most k+3.
  Cell 1 has (H(m),H(1)); the exit of a nonempty block (a,a+l] has
  (H(a+2),H(a+l+1)). This is also the entry cell of the next nonempty
  adjacent block, even if zero blocks intervene. Cell r has (2m-1,2m),
  and cell r+1, when present, has (2m,m+1).
- Every remaining cell is ordinary, with pair (H(i-1),H(i)).

An interior starts at a+2, so it never contains a shared boundary a+1.
The wrap is outside the blocks. These facts prove the classification is
exhaustive and disjoint, without an assumed size or relative block length.
No exceptional cell is omitted from the empirical measure or score.

## 3. Quantitative recovery of the literal complete maximum

Let mu_m=m^(-1) sum_i delta_(i/m,P_(i-1)/m,P_i/m), and omega_F be the
max-norm modulus of a continuous, possibly nonsymmetric F; B_F=||F||.
Replace alpha by s/m and ell_j by l_j/m in (1), obtaining bar_mu_m.
On each double panel [(a+2h-2)/m,(a+2h)/m], assign half the plus integral
to its even cell and half the minus integral to its odd cell. Each mass
is 1/m. Assign ordinary diagonal panels in the usual increasing order.
The interior coordinate errors from Section 2 are at most 4/m, and
ordinary errors at most 1/m. At most k+3 exceptional panel assignments
cost 2*B_F/m each. Thus

    |integral F d(mu_m-bar_mu_m)|
       <=omega_F(4/m)+2*(k+3)*B_F/m.                      (4)

The residual alpha-s/m is <1/m and each ell_j-l_j/m is <2/m.
The bad set between a_j/m and t_j for j=1,...,k, together with the wrap
interval [1-alpha,1-s/m], has total length at most [k*(k+1)+1]/m.
This upper bound remains valid when intervals overlap or slabs vanish.
Outside it the same slab and orientation apply. On block j, the reflected
high coordinate error is <(4*j-1)/m; the other high coordinate error is
<1/m. Hence

    |integral F d(mu_m-mu)| <= omega_F(4/m)+omega_F((4*k-1)/m)
                             +(2*k^2+4*k+8)*B_F/m.       (5)

The full maximum g satisfies 1<=g<3 and is 4-Lipschitz on D. For t<1/4
the chord dominates because sqrt(t/X)+sqrt(t/Y)<=2*sqrt(t)<=1.
For t>=1/4 the chain's sum of absolute partial derivatives is at most
2*sqrt(2)+1<4, and the chord's is <2. Along any segment, split at t=1/4
and at max branch changes; this proves the global Lipschitz statement.
Consequently, with G_m=integral g dmu_m,

    |G_m-I| <= (6*k^2+28*k+36)/m.                         (6)

This includes every seam, mixed branch, tie and finite rounding mismatch.
No finite cell is replaced by a chord because its continuum limit is chord.

## 4. Full feasibility and the radius scale

For each actual cell put

    d_i(R)=max(theta_R(P_(i-1),i)+theta_R(i,P_i),
               theta_R(P_(i-1),P_i)), S_m(R)=sum_i d_i(R).

The [arbitrary-high theorem](PERMUTED_ALTERNATING_HALVES.md), Sections 1-6,
applies: m>=2, every high is distinct in [m+1,2m], every low is below every
high, and 2m<2(m+1). Thus S_m(R)<=2*pi is necessary and sufficient for
all-pairs feasibility. Its unique root rho_m is the actual full minimum.
At the root choose x_i=theta_R(P_(i-1),i), y_i=d_i-x_i. Both directed
paths for every pair satisfy their bounds by the high-shell triangle
inequality and high/low separation, including all wrap and shared seams.
Their total is 2*pi; the cosine law gives Cartesian non-overlap.

For completeness the angle estimate is independent of all block parameters.
At R=4*c*m^2, c>=1/32, m>=32 and 1<=u,v<=2m, denominator linearization
and asin(t)-t<=t^3/3 for t<=1/2 give

    |theta_R(u,v)-2*sqrt(u*v)/R|
       <=512/m^2+8192/(3*m^3),
    |S_m(4*c*m^2)-G_m/(2*c)|
       <=E_m=1024/m+16384/(3*m^2).                       (7)

Indeed sqrt(u*v)/R<=1/(2*c*m), and its denominator relative change is
at most (u+v)/(2*R); twice their product is at most 1/(2*c^2*m^2).
Twice the inverse-sine remainder is at most 1/(12*c^3*m^3).
The scalar maximum is 1-Lipschitz in its entries; a chain has two angles.
These estimates rederive (7), rather than assume branch agreement.

For m>=2048, E_m<1 and 1<=G_m<3. At c=1/32 the score exceeds 15>2*pi;
at c=1/2 it is below 4<2*pi. Thus the normalized root lies between these
constants before substitution into (7). At the root,
|rho_m/(2m)^2-G_m/(4*pi)|<=E_m/(4*pi). Equation (6) proves (2).

Deleting only label 2m from this feasible placement preserves all constraints
on labels 1,...,2m-1. Since (2m/(2m-1))^2 tends to one, the even root
limit yields (3) for both parities. We do not identify the odd full minimum
or claim a finite-n global optimum.

## 5. Fourth-block corollary and a countable family without transfer debt

Use precisely alpha_hat and lengths (lambda,epsilon_b,Delta_*,1/20000)
from the [fourth-block proof](PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md).
Its rational margins prove alpha+T<1/2, so the general hypotheses hold
(and its direct integer gate r-z>=2 already holds at every m>=2).
For k=4, (2) has numerator 1268/m+16384/(3*m^2). Its continuum measure
is exactly mu_4(1/20000), with the third and fourth reflections separate.
Therefore

    limsup R*(n)/n^2 <= U_4=C_4(1/20000)
      < C_3(Delta_*)-1/4608000000000000.                  (8)

The exact definitions of the baseline minimizers are unchanged. This is a
new rigorous global upper coefficient conditional only on the cited proved
input theorems, not an assertion that the four-block family is optimal.

More generally let ell_j>=0 be a finite or countably infinite sequence
with sum T<1-alpha. Reflect separately on all its consecutive slabs and
keep the diagonal from T to 1. This defines (1) by a convergent sum.
Truncating after k slabs and reverting the remaining tail to diagonal
changes integral F by at most 2*B_F*sum_(j>k) ell_j. Consequently the
finite-block measures converge weakly, and their complete costs converge.
Apply (3) to each finite truncation and let k tend to infinity: the entire
countable family supplies global upper bounds without assuming that a
measure with correct marginals is automatically recoverable.

A single genuine recovery sequence is also available. Choose integers M_k
increasing to infinity, satisfying the common geometric gate and making
the right side of (5) tend to zero for Lipschitz tests (for example M_k
growing faster than k^3). At size m use the largest k<=m with M_k<=m.
The finite-panel error and omitted tail both vanish. Formula (7) then
transfers these actual orders to full geometry. Density of Lipschitz
functions on compact D gives recovery for every continuous test.

This structural closure prevents an endless succession of individual
transfer tasks. It does not characterize the best partition, all recoverable
couplings, or the global asymptotic constant. Those are separate questions.
