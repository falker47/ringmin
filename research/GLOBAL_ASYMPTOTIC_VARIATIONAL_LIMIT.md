# The global asymptotic limit and finite-word variational certificates

    status=PROVED; INTERNALLY_VALIDATED; external acceptance pending
    classification=exact theorem; effective variational characterization
    domain=all genuine orders and all pairwise constraints for radii 1,...,n
    historical_arXiv_v1=unchanged

## 1. An intrinsic line problem

For a finite multiset of marks a=(a_1,...,a_N) in [0,1], let b(a) be the
least span of points on a line with these marks and

    |x_i-x_j| >= sqrt(a_i*a_j) for every distinct pair.    (1)

Equal marks still label distinct points. Zero marks may coincide. A fixed
word/order w=(w_1,...,w_N) has its minimum span ell(w) given exactly by

    x_1=0, x_i=max_(j<i) [x_j+sqrt(w_i*w_j)],
    ell(w)=x_N.                                          (2)

Induction proves each feasible increasing placement has x_i at least this
value, and the displayed positions satisfy all constraints. In particular
ell(w) is the maximum sum along an increasing-index path from 1 to N.
The minimum over finitely many orders is b(a); it is attained. Monotonicity
under decreasing marks, deleting marks and enlarging distances is immediate.
Multiplying all marks by h>=0 multiplies the minimum span by h.

Write b_n=b(1/n,2/n,...,1). We will prove that E=lim b_n/n exists and

    R*(n)=C_* n^2+o(n^2), C_*=E/pi,
    E=inf_(n>=2) (b_n+1)/n.                              (3)

This formulation retains arbitrary genuine orders and all-pairs constraints.
It is not a relaxation to edge or triple marginals.

## 2. Exact comparison with the original circle geometry

Let B(a) be the least circumference of a circle carrying the marked points
with BOTH directed arcs for every pair at least sqrt(a_i*a_j). Cutting
any such circle at a point and reading its order yields a feasible line
placement, so b(a)<=B(a). Conversely, close any feasible line placement
with an extra gap 1. The line path for each pair is feasible; its complementary
arc contains the added gap and is at least 1>=sqrt(a_i*a_j). Therefore

    b(a)<=B(a)<=b(a)+1.                                  (4)

For R,u,v>0 the exact angular kernel obeys

    2*sqrt(u*v)/(R+n) <= theta_R(u,v) <= 2*sqrt(u*v)/R,
                                             1<=u,v<=n. (5)

The lower bound follows from asin(z)>=z and
sqrt((R+u)*(R+v))<=R+n. For the upper bound use the exact identity
theta_R(u,v)=2*atan(sqrt(u*v)/sqrt(R*(R+u+v))) and atan(t)<=t.
There is no Taylor remainder, small-angle hypothesis or chain-only step.

Given a feasible original placement, scale every angular arc by
(R+n)/(2*n). This produces a feasible B(1/n,...,1) circle of circumference
pi*(R+n)/n. Conversely a feasible linear circle of circumference b_n+1
gives an original feasible placement at R=n*(b_n+1)/pi, by scaling to 2*pi
and applying the upper inequality (5). The cosine law is exactly the
original non-overlap condition. Thus for EVERY n>=3,

    b_n/(pi*n)-1/n <= R*(n)/n^2 <= (b_n+1)/(pi*n).        (6)

The full global problem is squeezed, not a chosen fixed-order or cell model.

## 3. Concatenation proves existence, with correct marginal counts

Place copies of a line arrangement in consecutive blocks with a gap 1
between them. Pairs in one block remain feasible, and every cross-block
distance is at least 1. Hence k copies of a span-b template have total
span k*(b+1)-1 and exactly k copies of each of its marks.

Fix n>=2. For arbitrary N>=n choose k=ceil(N/n), form k copies of an
optimal b_n arrangement, and retain its N smallest marks. In the sorted
list the i-th retained mark is ceil(i/k)/n. After multiplying all marks
and coordinates by h=n*k/N, it is at least i/N. Decrease these N marks
to i/N, assigning the labels in sorted mark order (break ties arbitrarily).
Monotonicity preserves feasibility. Therefore

    b_N <= (n*k/N)*[k*(b_n+1)-1].                        (7)

Intermediate marks may exceed 1 after scaling; (1) and its homogeneity
remain meaningful for them, and the final marks are exactly i/N. No claim
that independent marginals alone imply a genuine permutation is needed.
Each label is assigned once to an actual point in the copied arrangement.

Since k/N tends to 1/n, (7) gives limsup_N b_N/N <=(b_n+1)/n for every n.
Also 0<=b_N/N<=1 from the equally spaced construction. Take n along a
subsequence attaining liminf: limsup<=liminf, proving existence. Taking
the infimum and then n tending to infinity proves (3). Equation (6)
transfers existence and the same constant to R*(n). This proof works for
both parities and supplies a recovery construction for every sufficiently
large N, not only a subsequence.

## 4. Finite-type thermodynamic values and quantization

For k>=1 let A_(k,q) contain q copies of each mark 1/k,...,1. Define

    e_k=lim_(q->infinity) b(A_(k,q))/(k*q).               (8)

This limit exists. If a_q=b(A_(k,q))+1 then concatenation gives
a_(p+q)<=a_p+a_q. For each fixed p, division q=hp+r and bounded remainder
gives limsup a_q/q<=a_p/p. Taking p along the liminf subsequence proves
the elementary subadditive limit and infimum formula. Dividing by k
gives (8). Allow q=0 with empty span 0 for harmless remainders.

Let A^-_(k,q) instead contain q copies of 0,1/k,...,(k-1)/k, and define
e^-_k analogously. Zero marks impose no constraint and may be added at
an occupied position. The common nonzero types of A and A^- are identical;
the missing top mark 1 may be placed as a separate block of q equally
spaced points, costing q-1 plus one join gap. For k=1 the lower system
has span zero and the same conclusion is immediate. Thus

    e^-_k <= e_k <= e^-_k+1/k.                            (9)

For n=k*q, sorted marks i/n are bounded above by the sorted multiset A
and below by A^-. By monotonicity and Section 3,

    e^-_k <= E <= e_k, hence e_k-1/k <= E <= e_k.          (10)

In particular e_k tends to E, with a certified one-sided error <=1/k.
This simple shift of uniform bins is special to the present mark law.

## 5. A finite linear program with a vanishing certified gap

Fix k>=1 and r>=2. Let W={1/k,...,1}^r be ALL words of length r, allowing
repetitions. For each word compute ell(w) by (2), and c_j(w), its count
of type j/k. Define the compact finite linear program

    lambda_(k,r) = min (1/r)*sum_(w in W) p_w*ell(w),
    p_w>=0, sum_w p_w=1,
    sum_w p_w*c_j(w)=r/k for every j=1,...,k.             (11)

The constraints are feasible, for example by equally mixing the k constant
words. They are genuine block frequencies with exact type counts. The
program remembers all pair constraints WITHIN every word. It forgets
cross-block constraints only at a quantified cost below; no exact cyclic
compatibility of arbitrary marginals is asserted.

**Lower bound.** Partition an optimal order of A_(k,q) into successive
blocks of r vertices plus fewer than r leftover vertices. Its total span
is at least the sum of the block spans, each at least ell(w). Along any
q sequence tending to infinity, empirical word distributions have convergent
subsequences in the finite simplex. Their type means tend to r/k because
the discarded count is <r. Each limit is feasible in (11). It follows that
lambda_(k,r)<=e_k. This argument uses only nonnegative interblock distances;
it does not need an optimal cycle or a local-contact hypothesis.

**Upper recovery.** The feasible polytope in (11) has rational coefficients
and rational vertices. A minimizing vertex p can therefore be chosen rational,
despite the algebraic cost coefficients. Choose a common denominator D.
One batch of D blocks, with D*p_w copies of word w, has exactly D*r/k
copies of each type (this is an integer by the count constraints). Place
each word at its minimum span and separate consecutive blocks by gap 1.
Repeated batches have all pair constraints, and their mean length per point
tends to sum p_w*(ell(w)+1)/r=lambda_(k,r)+1/r. Therefore

    lambda_(k,r) <= e_k <= lambda_(k,r)+1/r.             (12)

Combining with (10) proves the explicit two-sided certificate

    (lambda_(k,r)-1/k)/pi <= C_*
                       <= (lambda_(k,r)+1/r)/pi.         (13)

In particular

    C_* = (1/pi)*lim_(k,r->infinity) lambda_(k,r),
    certified bracket width = (1/k+1/r)/pi.              (14)

The limit is joint: the bracket error holds for every k,r separately.
The upper recovery uses finite words, rational mixtures, actual point
placements, quantization, and the exact geometric comparison (6). The lower
bound applies to all possible geometric orders. Thus the two theories match
at an effective variational value, with no unpaid continuum recovery debt.

## 6. Exact computation, dual certificates and limitations

All entries sqrt((i/k)*(j/k)) are nonnegative real algebraic numbers. The
recursion (2) contains finitely many sums and maxima, so every ell(w) is
computable with directed rational enclosures. If every pair weight enclosure
has width <=epsilon, the longest-path enclosure has width <=(r-1)*epsilon.
Replacing costs in (11) by their lower or upper endpoints yields rational
LP values lambda^-<=lambda<=lambda^+, with

    lambda^+-lambda^- <= (r-1)*epsilon/r.                (15)

The equality-constraint matrix has integer/rational entries. Finite exact
vertex enumeration is a terminating algorithm, even if impractical. A more
efficient solver may discover candidates; its output must be checked by exact
primal feasibility and an exact dual lower certificate for the RATIONAL
endpoint LPs. Explicitly if y_0+sum_j y_j*c_j(w)<=ell^-(w)/r for every word,
where ell^- is the directed rational lower cost, then
y_0+(r/k)*sum_j y_j is a lower bound on lambda. Feasible rational p gives
an upper bound using the directed upper costs. Both success and failure of
these rational certificate checks are decidable by finite rational arithmetic.
We do not decide equality of algebraic expressions by endlessly tightening
intervals; no such equality oracle is needed for this scheme.

Given any rational requested error, choose k and r to control 1/k+1/r,
choose directed pair-weight precision to control (15), and enclose pi by a
convergent rational series. This certifies C_* to arbitrary precision in
principle. Complexity is exponential in r (k^r words); no claim of practical
high-precision evaluation, simple closed form, unique extremizer or optimal
reflected partition follows. Previously proved numeric endpoints remain useful
because they can be far sharper than a small instance of (13).

The normalized constant is characterized intrinsically and effectively; its
recognition in elementary constants and optimal microscopic structure remain
secondary open questions. The theorem does not expand the certified finite
range or establish a universal contact graph.
