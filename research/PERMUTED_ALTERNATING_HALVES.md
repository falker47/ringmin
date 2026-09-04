# Arbitrarily permuted alternating halves: exact fixed-order feasibility

```text
status=PROVED
classification=exact fixed-order theorem / proved immediate fixed-order corollaries
domain=every integer m>=2, every permutation P of {m+1,...,2m}, every R>0
proved_on=2026-09-05
published_snapshot=arXiv v1 remains unchanged
```

## 1. Question, model and result

Fix m>=2, write L_i=i, and let (P_1,...,P_m) be ANY permutation of
{m+1,...,2m}. All subscripts are cyclic, in particular P_0=P_m. The
prescribed cyclic order is sigma_P=(1,P_1,2,P_2,...,m,P_m). Write

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
a_i=theta_R(P_{i-1},i),  b_i=theta_R(i,P_i),
c_i=theta_R(P_{i-1},P_i),
d_i=max(a_i+b_i,c_i),    S_P(R)=sum_i d_i.               (1)
```

Here asin is the principal branch. For R,a,b>0 its argument lies in
(0,1), theta lies in (0,pi), increases strictly in each outer radius and
decreases strictly in R. These facts follow directly from the formula.

**Theorem.** At every R>0, full feasibility of sigma_P is equivalent to

```text
sum_i max(theta_R(i,P_i)+theta_R(P_{i-1},i),
          theta_R(P_{i-1},P_i)) <= 2*pi.                (2)
```

More precisely, let x_i be the positive gap P_{i-1}->i, and y_i the
positive gap i->P_i. The entire set of feasible gaps in this order is
exactly

```text
x_i>=a_i,  y_i>=b_i,  x_i+y_i>=c_i  (every i),
sum_i(x_i+y_i)=2*pi.                                   (3)
```

The full angular model requires BOTH directed cyclic path lengths for
each unordered pair a,b to be at least theta_R(a,b). Since their sum is
2*pi, this is the interval [theta_R(a,b),2*pi-theta_R(a,b)] for either
directed separation. The cosine law then gives Cartesian non-overlap.
We prove both paths individually, not just the shorter path or adjacency.

The numerical falsification in Section 7 was run before developing this
proof. It is not a premise. The only inputs are the angular model and the
elementary inequalities proved below. In particular no monotonicity of P,
shift representation, Supnick optimality or asymptotic assertion is used.

## 2. A permutation-free high-shell triangle inequality

**Lemma.** If 0<u<=v<=2u, then for every R>0,

```text
2 theta_R(u,u) > theta_R(v,v).                          (4)
```

Put x=u/(R+u) in (0,1) and z=v/(R+v). Monotonicity in v gives
z<=2x/(1+x)<1. If x>=1/sqrt(2), then
2 asin(x)>=pi/2>asin(z), which proves (4). If 0<x<1/sqrt(2), then

```text
(1+x)^2(1-x^2)-1=x(2-2x^2-x^3)>0.                     (5)
```

For an explicit positive bound, x^2<1/2 and x<3/4 imply
x^3<3/8, hence 2-2x^2-x^3>5/8. Every factor being positive, (5) gives

```text
z<=2x/(1+x)<2x sqrt(1-x^2)=sin(2 asin(x)).              (6)
```

Both comparison angles are in (0,pi/2); applying asin proves
asin(z)<2 asin(x), or (4). The endpoint x=1/sqrt(2) was covered by the
first branch, so no squaring or inverse-sine branch is missing.

Consequently, for ANY a,b,c in [u,v], with b in any relative order,

```text
theta_R(a,b)+theta_R(b,c)
 >=2 theta_R(u,u)>theta_R(v,v)>=theta_R(a,c).           (7)
```

Repeated application proves that every nonempty path of high vertices
H_0,...,H_k in this shell satisfies

```text
sum_{j=1}^k theta_R(H_{j-1},H_j)>=theta_R(H_0,H_k),    (8)
```

with equality allowed for k=1. Indeed the k=1 assertion is equality;
for k>=2, collapse the first k-1 edges by induction and apply (7) at
H_{k-1}. This applies independently to either cyclic path. Our shell is
[m+1,2m], with 2m<2(m+1). Its triangle inequality has no ordering hypothesis.

## 3. Necessity and a closed gap construction

In any feasible placement, adjacency requires x_i>=a_i and y_i>=b_i.
The path P_{i-1}->i->P_i also satisfies x_i+y_i>=c_i, because the full
model imposes its lower bound as well as that of the complementary path.
Thus x_i+y_i>=d_i. The m cells partition the 2m gaps, so S_P(R)<=2*pi.
This proves necessity of (2) and (3).

Conversely, suppose S_P(R)<=2*pi. Define base gaps

```text
e_i=max(0,c_i-a_i-b_i),
x_i=a_i,  y_i=b_i+e_i,  x_i+y_i=d_i.                  (9)
```

They are strictly positive. Before imposing closure, Section 4 proves
that every directed pair path in the abstract cycle already meets its
angular lower bound. That proof uses only the three local inequalities in
(3), and therefore also applies to any other choice satisfying them.

Finally put E=2*pi-S_P(R)>=0 into any single gap, for example x_1.
For each pair the two paths partition all edges. This addition increases
one path by E and leaves the other unchanged. Both lower bounds survive,
and their new total is 2*pi. Cumulative angles therefore give a full
placement in precisely sigma_P, also when E=0. This proves sufficiency of
(2); Section 4 simultaneously proves sufficiency of (3).

## 4. Every pair type, each direction separately

Take any nonnegative gaps satisfying x_i>=a_i, y_i>=b_i and
x_i+y_i>=c_i. Write D_i=x_i+y_i>=c_i. Each occurrence of a whole valley
P_{i-1}->i->P_i, traversed in either direction, can be contracted to a
high edge of length D_i. Bounds below apply even before total length is
2*pi. For each pair choose either of its two simple cyclic paths; the
argument is repeated for the other path with its own endpoints/highs.

### High-high: P_j, P_k, j!=k

Each of the two paths is a nonempty concatenation of whole valley cells.
Replacing their lengths D_i by c_i only decreases the path length. Apply
(8) to the actual high sequence in that direction to obtain
length>=theta_R(P_j,P_k). The two high sequences may have any rises or
falls. For m=2 each direction has exactly one cell, so its bound is
already D_i>=c_i; there is no need for a third high vertex.

### Low-high: i, P_j

Start at i and fix one direction. Its first high U is P_{i-1} or P_i.

- If U=P_j, the path is the single adjacent gap and is at least
  theta_R(i,P_j).
- Otherwise the remaining path from U to P_j is a nonempty sequence of
  whole cells. By the high-path bound its length is at least
  theta_R(U,P_j)>theta_R(i,P_j), since U>i. The initial positive
  gap only adds length.

Starting from i in the opposite direction uses its other neighbor and
the same two exhaustive cases. In particular the complement of an
adjacent low-high pair contains a nonempty high path, even when m=2.
We never assume that the target high lies before or after a larger high.

### Low-low: i, j, i!=j

Fix either direction from i to j. It first reaches a high U and finally
leaves a high V before reaching j.

- If U=V, simplicity of the cyclic path means this is the two-edge
  path i->U->j. Its first gap alone is at least
  theta_R(i,U)>theta_R(i,j), because U>j.
- If U!=V, the middle segment is a nonempty whole-cell high path. Its
  length is at least theta_R(U,V)>theta_R(i,j), because U>i and V>j.
  The first and last positive gaps can be discarded in this lower bound.

Both directions satisfy this dichotomy independently. It covers adjacent
lows in cyclic index order as well as arbitrarily separated lows. A
path cannot revisit the same high before reaching j because it is simple.

These three cases exhaust all unordered pairs. The strict margins used
for nonadjacent mixed/low paths are not assertions about all contacts or
floaters in global optima.

## 5. Small cycles and arbitrary seam/wrap configurations

For m=2 the order is (1,P_1,2,P_2), for either P=(3,4) or P=(4,3).
There are six unordered pairs. Both paths for all six are explicitly:

| Pair | One path length | Other path length | Lower-bound reason |
|---|---|---|---|
| P_1,P_2 | D_1 | D_2 | Each cell has its own c_i=theta_R(P_1,P_2) |
| 1,2 | y_1+x_2 | x_1+y_2 | First incident high gap suffices in each direction |
| 1,P_1 | y_1 | x_1+D_2 | Adjacency; high path through P_2 |
| 1,P_2 | x_1 | y_1+D_2 | Adjacency; high path through P_1 |
| 2,P_1 | x_2 | y_2+D_1 | Adjacency; high path through P_2 |
| 2,P_2 | y_2 | x_2+D_1 | Adjacency; high path through P_1 |

The two c_i coincide numerically for m=2 but belong to different arcs;
neither may be dropped. As R decreases to zero each d_i tends to 2*pi,
not pi. The theorem intentionally excludes m=1, where the two neighboring
highs would be the same circle and c_i would not be a pair constraint.

For m=3 every high-high pair has a one-cell path and a two-cell path.
Every low-low pair has a common-high path and a path with two distinct
highs. A low-high pair either has an adjacent path and a complementary
high path, or has a three-edge path in each direction. Thus the cases of
Section 4 cover all six permutations, including (4,6,5), which is not an
increasing cyclic shift. There is no assumption that m>=4 in the proof.

For arbitrary m the low-index seam is exactly the whole cell

```text
P_m -> 1 -> P_1,  with gaps x_1,y_1 and bound c_1.     (10)
```

The other cells are P_{i-1}->i->P_i, i=2,...,m. A permutation may have
many high descents and jumps, at interior cells or at (10). The extremes
2m and m+1 need not even be consecutive in the cyclic high sequence.
Every such cell has its own actual chord c_i. A path crossing (10) with
high endpoints includes that whole cell; a path with endpoint low 1
uses its appropriate partial first/last gap exactly as in Section 4.
The same description works for every interior descent or jump, and for
paths crossing several of them. No exceptional edge is omitted.

For example P=(7,5,8,6) at m=4 has descents at cells 2 and 4, while
the low seam is the rising high step 6->7. Its paths are covered without
relabeling these into a single high wrap. Rotation or reflection of the
geometric cycle merely exchanges starting points or the two paths; it
does not alter any of their bounds. We do not require a reflected cycle
to retain the displayed increasing-low notation.

## 6. Immediate fixed-order consequences and scope

**Unique full radius.** Each a_i+b_i and c_i is positive, continuous and
strictly decreasing in R. Their maximum is strictly decreasing too:
for R_1<R_2 choose a branch attaining the maximum at R_2; its value at
R_1 is strictly larger, and the maximum at R_1 is at least that value.
Moreover

```text
lim_{R->0+} S_P(R)=2*pi*m>2*pi,
lim_{R->infinity} S_P(R)=0.
```

Hence there is a unique positive rho_P with S_P(rho_P)=2*pi, and
R_full(sigma_P)=rho_P. Feasible radii form [rho_P,infinity); equality
is realized by (9). Evaluating the scalar obstruction and building gaps
uses m local cells at each fixed R, with no all-pairs optimization needed
once this theorem is available. This is a mathematical reduction, not a
change to the production evaluator or its numerical guarantees.

**All gap choices at the optimum.** At rho_P, necessity gives D_i>=d_i
and both sums equal 2*pi, forcing D_i=d_i for every i. Conversely, all
choices

```text
x_i in [a_i,d_i-b_i],  y_i=d_i-x_i                    (11)
```

(evaluated at rho_P) are feasible by (3). Thus (11) describes all optimal
gap vectors for this prescribed orientation and labeling, up to overall
rotation of the placement. If d_i=a_i+b_i the two gaps are forced; if
d_i>a_i+b_i the interval has positive length. This is a fixed-order gap
parametrization, with no inference about essential constraints or global
floating behavior.

**Chain/full equality test.** Let Q_P(R)=sum_i(a_i+b_i), whose unique
root q_P at 2*pi is R_chain(sigma_P). Since

```text
S_P(R)=Q_P(R)+sum_i max(0,c_i-a_i-b_i),
```

R_full(sigma_P)>=q_P, with equality iff every c_i<=a_i+b_i at q_P.
If any cell violates that inequality there, the full radius is strictly
larger. This is an exact per-order comparison, not chain optimality over
orders or a global optimum.

The fixed-R part of research/SHIFTED_ALTERNATING_HALVES.md, Sections 2-3,
is recovered by substituting P_i=m+1+((i+s-1) mod m). No step of that
fixed-R proof fails: its high-shell lemma already applies to arbitrary
high paths. The monotone edge selection in the earlier unshifted note
would not extend directly, but is replaced by (8). The shifted note's
later approximation that ordinary consecutive highs differ by 1 does
depend on shifts; it is neither used nor extended here.

No optimization, continuum functional or asymptotics over arbitrary
permutations is started. Existing global bounds and certificates retain
their previous scope; the public paper is unchanged.

## 7. Independent bounded checks and authority

Before the proof, check_falsification.py enumerated all 872 permutations
for m=2..6, without symmetry reduction. Each was checked at seven radii,
including both sides of the conjectured root, by an independent all-pairs
position LP using the half-angle atan2 formula. All 6104 probes agreed.
Those finite floating-point observations do not decide every R or m.

Post-proof checks audit the exact shell algebra/sign gates, direct
70-digit path sums with an alternate angular formula, independent
Cartesian distances, three cell-excess splits, seam placement of closure
slack and symmetries. Their bounded domains, tolerances, outputs and
source hashes are in ops/TASK-20260905__permuted_alternating_halves/.
Neither checker imports src/ringmin, verify.py, or the previous checker.

The proof in Sections 2-5 establishes the exact theorem. Section 6 contains
only its proved immediate fixed-order corollaries. The sole thematic owner
is knowledge/FIXED_ORDER_THEORY.md; task-local computation is evidence,
not a second theorem authority or a finite global certificate.
