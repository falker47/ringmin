# Third adjacent reflection: exact continuous cost with variable width

    status=PROVED
    classification=exact continuous theorem; explicit rational improvement
    domain=alpha_hat; x_*; lambda=(1+alpha_hat)*x_*; epsilon_b; v=lambda+epsilon_b fixed
    variable=Delta>0; guaranteed interval 0<Delta<=1986317/400000000
    finite_recovery_and_geometric_transfer=not supplied for new widths
    proved_on=2026-09-08
    published_snapshot=arXiv v1 unchanged

## 1. Exact inputs, notation and result

Use the exact definitions, existence, uniqueness and accepted brackets in
the [boundary minimum](PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md),
Sections 1 and 6, and the measure mu_b in
[boundary recovery](PERMUTED_HALVES_BOUNDARY_RECOVERY.md), equation (4).
Thus x_* is the unique minimizer of the complete-max E, alpha_hat is the
unique zero of K'(alpha)+(1+alpha)*E(x_*), and epsilon_b is the unique
zero of D_b' on (0,A/3-lambda). These parameters are held fixed throughout:

    AL=1093/10000 < alpha=alpha_hat < AH=10931/100000,
    XL=719/2500 < x=x_* < XH=2877/10000,
    EL=43/1000 < e=epsilon_b < EH=11/250,
    A=1+alpha, lambda=A*x, v=lambda+e,
    a=A/3, b=1-alpha, B=A+v, h=a-v.                       (1)

In this note B is A+v, not the A+lambda of the boundary-minimum note.
Only Delta varies; in particular B is constant when differentiating.
No midpoint, approximate root, new bracket or stationarity calculation
replaces any accepted parameter. Write

    A_L=1+AL, A_H=1+AH,
    L=A_L*(1-3*XH)-3*EH=1986317/100000000,
    D_g=L/4=1986317/400000000,
    d_0=1/1000, d_1=1/250.                               (2)

On D=[0,1] x [1,2]^2 retain

    k(t,X,Y)=sqrt(t)*(sqrt(X)+sqrt(Y)), c(X,Y)=sqrt(X*Y),
    g=max(k,c), C(mu)=(integral g dmu)/(4*pi).

Define mu_3(Delta) by replacing only the diagonal slab [v,v+Delta]
of mu_b by its own symmetric reflection (Section 2), and put
C_3(Delta)=C(mu_3(Delta)), C_b=C(mu_b). The older unqualified C_3 and
mu_3 in the [fixed-width theorem](PERMUTED_HALVES_THIRD_ADJACENT_BLOCK.md)
and its recovery/transfer continue to mean C_3(d_0) and mu_3(d_0).

**Theorem.** For every 0<Delta<=D_g, the measure has the required
coordinate domain, three uniform marginals and equal (t,X)/(t,Y)
marginals. Both changed full maxima are strictly chord on the closed
slab. With M=B+Delta/2 and q=Delta/(2*B+Delta),

    F(Delta):=4*pi*[C_3(Delta)-C_b]
      =-integral_(-Delta/2)^(Delta/2)
          z^2/[M+sqrt(M^2-z^2)] dz
      =(Delta/2)*sqrt(B*(B+Delta))+M^2*asin(q)-Delta*M,

    F'(Delta)=sqrt(B*(B+Delta))+M*asin(q)-(B+Delta)<0.    (3)

The principal real inverse sine is used, with 0<q<1. In particular,

    0<d_0<d_1<D_g,
    C_3(d_0)-C_3(d_1)>1/(2304000000*pi)
                       >1/9216000000>0.                 (4)

Section 3 identifies exactly the maximal all-chord width tau_3>D_g
and the first switch. Formula (3) and strict decrease hold also through
tau_3, with its endpoint tie; after tau_3 a positive chain contribution
must be retained. No decreasing-cost assertion past that switch or
minimizing third width is needed or claimed here.

## 2. Coordinate gates, measure and marginals for all widths in the interval

The accepted brackets give 0<lambda<v<a<b<1 and

    V_L=A_L*XL+EL=9050867/25000000 < v
       < V_H=A_H*XH+EH=363148487/1000000000.

Because 1-3*XH>0, the directed lower corner is

    A-3*v=A*(1-3*x)-3*e > L > 0.

For every 0<Delta<=D_g this proves, with strict inequalities even at D_g,

    A-3*v-4*Delta > L-4*Delta >=0,
    a-v-Delta > L/3-Delta >=L/12>0,
    b-v-Delta > 1-AH-V_H-D_g=1045151441/2000000000>0,
    3/2-M > 3/2-A_H-V_H-D_g/2
           =100234467/4000000000>0.                      (5)

Thus the slab is strictly before both the diagonal cutoff a and wrap b;
its highs lie in [B,B+Delta] subset (1,2). At d_1 the first two margins
in (5), before the final weakening, are respectively

    L-4*d_1=386317/100000000>0,
    L/3-d_1=786317/300000000>0.                           (6)

For I_Delta=[v,v+Delta] and R_Delta(t)=2*v+Delta-t define, for every
continuous, possibly nonsymmetric test T on D,

    integral T d(mu_3(Delta)-mu_b)
      =(1/2)*integral_I_Delta [T(t,A+t,A+R_Delta(t))
                              +T(t,A+R_Delta(t),A+t)
                              -2*T(t,A+t,A+t)] dt.       (7)

The removed conditional measure is precisely diagonal almost everywhere
there. Replacing it by the two positive masses of weight 1/2 preserves
total mass and the low Lebesgue marginal. R_Delta is a measure-preserving
involution of I_Delta, so for each continuous phi on [1,2],

    (1/2)*integral_I_Delta [phi(A+t)+phi(A+R_Delta(t))] dt
       =integral_I_Delta phi(A+t) dt.

This proves preservation of each high marginal separately, for every
width in (5). Conditional swap symmetry proves equality of the (t,X)
and (t,Y) marginals for arbitrary continuous tests of those two variables.
Their common two-variable marginal need not be unchanged from mu_b.

Keep three separate reflections on [0,lambda], [lambda,v] and I_Delta.
The last two low intervals meet only at v, and their high ranges only
at A+v. Both points have zero mass because the maps have slopes +/-1.
The five high ranges [1,A], [A,A+lambda], [A+lambda,A+v],
[A+v,A+v+Delta], [A+v+Delta,2] partition [1,2] modulo endpoints.
Half-open endpoint assignments make the same measure. No seam atom,
extra cost or reflection of the union is introduced. These arguments
actually hold for 0<Delta<=h, since a<b; no finite recoverability is used.

## 3. Full-max cancellation and its first branch obstruction

Set s=t-v, X=B+s, Y=B+Delta-s, t=v+s. Before choosing any branch,
the exact cost difference is

    F(Delta)=integral_0^Delta [max(k(t,X,Y),c(X,Y))
                               -max(2*sqrt(t*X),X)] ds.  (8)

Every unchanged cost cancels with its complete maximum, including the
mixed second block and all old switches. For Delta<=D_g,

    k/c=sqrt(t/X)+sqrt(t/Y)
        <=2*sqrt((v+Delta)/B)<1,
    X-4*t=A-3*v-3*s >=A-3*v-3*Delta>0.                   (9)

The first strict sign uses B-4*(v+Delta)>0 from (5); all quantities
are positive before squaring. This covers both endpoints and every
interior point, not only a sample of the slab. Thus (8) reduces to

    F_ch(Delta)=integral_0^Delta
                 [sqrt((B+s)*(B+Delta-s))-(B+s)] ds.     (10)

The closed bracket corners used by the checker are covered too: even
if B-4*(v+Delta)=0 at the weakest corner and Delta=D_g, the first
comparison in (9) is strict for Delta>0. At s<Delta one has t<v+Delta;
at s=Delta one has X>B. Hence their literal full maximum is chord as well.

For an exact description of the first obstruction, consider 0<Delta<=h.
The removed diagonal remains chord, with its sole tie at Delta=s=h.
For the reflected ratio V(s,Delta)=sqrt(t/X)+sqrt(t/Y),

    V_s=[A/X^(3/2)+(Y+t)/Y^(3/2)]/(2*sqrt(t))>0,
    V(0,Delta)<2*sqrt(v/B)<1,
    V(Delta/2,Delta)<1.

The last sign follows from v+Delta/2<a. The endpoint function

    W(Delta)=sqrt((v+Delta)/(B+Delta))+sqrt((v+Delta)/B)   (11)

is strictly increasing: the derivatives of its squared summands are
A/(B+Delta)^2 and 1/B. Moreover

    W(0)=2*sqrt(v/B)<1,
    W(h)=1/2+sqrt(a/B)>1,

since B=A+v<4*a. Hence there is exactly one UNSQUARED root

    tau_3 in (D_g,h), W(tau_3)=1.                        (12)

The lower bound follows from the strict uniform gate (9). Equation (12)
is an exact definition with a unique specified root, not a numerical
estimate or an unconstrained squared root. It identifies the first
obstacle as Delta increases: an endpoint tie in the third reflection,
strictly before the diagonal cutoff and the high wrap. There are no
earlier measure or branch obstructions.

For 0<Delta<tau_3 the slab is strictly chord. At tau_3 only s=Delta
ties; it has zero mass and (10) is still exact. For tau_3<Delta<=h
there is a unique switch z(Delta) in (Delta/2,Delta), defined by
V(z,Delta)=1. The full cost then is exactly

    F(Delta)=F_ch(Delta)
               +integral_z(Delta)^Delta [k(t,X,Y)-c(X,Y)] ds,
    integral_z(Delta)^Delta [k-c] ds>0.                  (13)

Thus continuing (10) alone after tau_3 would give the wrong cost.
A branch switch does not by itself imply a change in the sign of F'.
We stop the monotonicity assertion at tau_3 and do not optimize the
mixed regime. No claim is made here for widths beyond h.

## 4. Exact formula and strict width monotonicity

For 0<Delta<=tau_3, center z=s-Delta/2. Since
X*Y=M^2-z^2>=B*(B+Delta)>0 and integral_0^Delta (B+s) ds=Delta*M,
rationalization gives (3). Integrating sqrt(M^2-z^2) between the
symmetric endpoints gives its closed form. Leibniz differentiation of
(10), with both width dependences retained, gives

    F_ch'=sqrt(B*(B+Delta))-(B+Delta)
             +(1/2)*integral_0^Delta sqrt((B+s)/(B+Delta-s)) ds.

The last integral is 2*M*asin(Delta/(2*M)): in centered coordinates
the odd part of (M+z)/sqrt(M^2-z^2) integrates to zero. This proves
the derivative formula in (3), including the left derivative at tau_3.

To prove its strict sign without a small-width expansion, put

    Q=B/Delta+1/2>1/2,
    H(Q)=integral_(-1/2)^(1/2) [Q-sqrt(Q^2-r^2)] dr.

For every Q>1/2, H(Q)>0 and

    H'(Q)=integral_(-1/2)^(1/2)
              [1-Q/sqrt(Q^2-r^2)] dr<0.                 (14)

Both strict signs hold off the single point r=0. Differentiation under
the integral is justified on each compact Q interval inside (1/2,infinity)
by positive radicands and bounded derivatives. The exact identity is

    -F_ch(Delta)=Delta^2*H(B/Delta+1/2),
    -F_ch'(Delta)=2*Delta*H(Q)-B*H'(Q)>0.                (15)

This explicitly accounts for the moving M and endpoints. Consequently
C_3 is strictly decreasing on (0,tau_3], in particular on the rational
interval (0,D_g]. Its continuous zero-width extension is C_3(0)=C_b,
with right derivative zero. No negative derivative at zero is asserted.
At tau_3, (3) is the all-chord left derivative. Since V_s>0, the implicit
function theorem gives z(Delta)=tau_3+O(Delta-tau_3) near entry.
The added interval has length O(Delta-tau_3), and the smooth k-c vanishes
at entry, so (13)'s added integral is O((Delta-tau_3)^2). Thus (3) is
also the full-cost derivative there. Its sign alone is not used
to assert monotonicity on an unexamined mixed interval.

## 5. Explicit rational improvement and bounded verification

The centered formula has denominator between 2*B and 2*M, so

    -Delta^3/(24*B)<=F_ch(Delta)<=-Delta^3/(24*M).         (16)

At the two explicit widths d_0,d_1, gates (5)-(6) give B>1, M<3/2 and
strict chord dominance. Therefore

    F(d_0)>-d_0^3/24, F(d_1)<-d_1^3/36,
    F(d_0)-F(d_1)>d_1^3/36-d_0^3/24=1/576000000.

Divide by 4*pi>0 and use pi<4 to obtain (4). This is an exact separation
from the old width, not a diagnostic comparison of approximate minima.

The [standalone checker](../ops/TASK-20260908__third_block_width/check_width.py)
uses only stdlib Fraction arithmetic, directed square roots and a bounded
positive-series inverse-sine enclosure. It checks the new rational gates,
the old and new widths and the rational interval endpoint at all eight
accepted bracket corners. Concave trapezoid/midpoint bounds on the
literal full max independently enclose the closed formula; monotone
rectangle bounds on the Leibniz integral enclose the derivative and its
strict sign. The chord's second s derivative is
-M^2/(M^2-(s-Delta/2)^2)^(3/2)<0; the logarithmic derivative of
sqrt(X/Y) is (1/X+1/Y)/2>0. These justify the respective quadrature
directions; the removed diagonal is integrated exactly.
The checker also encloses the old-minus-new raw cost across the whole
B bracket and checks the strict rational saving without using (16).
For that bracket comparison, F_ch is increasing in B: the derivative
of the integrand in (10) is (2*B+Delta)/(2*sqrt(X*Y))-1>=0 because
(2*B+Delta)^2-4*X*Y=(Delta-2*s)^2, with positive sides before squaring.
The endpoint at h is a deliberate chain/tie control; it demonstrates
failure of continuing the chord branch indefinitely. All finite probes
supplement the analytic all-width and arbitrary-test proofs.

The checker does not import production code or any previous checker,
refine the accepted parameters, solve for tau_3, scan widths or write files.
Exact commands, outputs, source protection and limitations are in the
[task evidence](../ops/TASK-20260908__third_block_width/EVIDENCE.md).

This continuous result has its sole stable owner in
knowledge/FIXED_ORDER_THEORY.md. Existing finite recovery, full-root
transfer and global coefficient remain at d_0=1/1000. There is no finite
recovery, R_full transfer or new global limsup claim for d_1 or variable
Delta, no change to alpha_hat, x_*, lambda or epsilon_b, and no new
optimum, finite certificate or paper revision. External review is separate.
