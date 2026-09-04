# Adjacent high swaps in the permuted alternating halves

```text
status=PROVED
classification=exact local identities / conditional exchange theorem /
               proved small-R structural corollary / disproved sign rules
domain=integer m>=2, P a permutation of {m+1,...,2m}, fixed R>0
proved_on=2026-09-05
published_snapshot=arXiv v1 unchanged
```

## 1. Question and exact locality

Use the full fixed-order criterion proved in
`research/PERMUTED_ALTERNATING_HALVES.md`, not the adjacent-chain relaxation.
At fixed R>0 write

```text
theta(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_t(a,b)=max(theta(t,a)+theta(t,b), theta(a,b)),
S_P(R)=sum_{i=1}^m F_i(P_{i-1},P_i),  P_0=P_m.
```

All radii are positive and asin has its principal branch; theta is in
(0,pi). Let P' swap positions j and j+1, with all POSITION subscripts
reduced cyclically to {1,...,m}. The low radii retain their actual values:
in particular a wrap does not replace low 1 by m+1. Define

```text
Delta S_P(R)=S_{P'}(R)-S_P(R).
```

For m>=3 put

```text
x=P_j, y=P_{j+1}, u=P_{j-1}, v=P_{j+2},
l=j, r=[j+2]_m.
```

Only cells j and [j+2]_m can change, and

```text
Delta S_P = F_l(u,y)-F_l(u,x) + F_r(x,v)-F_r(y,v).       (1)
```

Indeed the incident cells have high pairs (u,x), (x,y), (y,v), which
become (u,y), (y,x), (x,v). The middle cell [j+1]_m is EXACTLY invariant
by symmetry of F, including its branch and any branch equality. Every
other cell has the same arguments. For distinct x,y each exterior cell
changes strictly, since both branches increase strictly in either high;
the two changes have opposite signs and can cancel.

For m=3 the two exterior cells are distinct but u=v is the remaining
high. Formula (1) still applies. For j=m-1 the exterior low labels are
(m-1,1); for j=m they are (m,2). For m=2 every cell has the same unordered
pair of highs before and after the swap: Delta S_P=0. Formula (1) must
NOT be used by counting the coincident exterior cell twice. The preceding
criterion excludes m=1.

From now on x<y unless stated otherwise. For an actual descending pair,
evaluate the formulas with x=min(P_j,P_{j+1}), y=max(P_j,P_{j+1}) and
negate the result; l,r,u,v are unchanged. Consecutive means positions,
not consecutive numerical high values.

## 2. Exact branch test and the moving-high threshold

These cell facts hold more generally for R>0, t>0 and a,b>t. Write

```text
C_t(a,b)=theta(t,a)+theta(t,b), H(a,b)=theta(a,b),
A=1/R, c=1/a, d=1/b,
K_R(a,b)=A+c+d+2 sqrt(Ac+Ad+cd).                       (2)
```

The exact branch test is

```text
sign(C_t(a,b)-H(a,b)) = sign(K_R(a,b)-1/t).             (3)
```

Here the PLUS square root is essential. To prove (3) without assuming a
geometric branch, put h=sqrt(Ac+Ad+cd)>0, k=A+c+d+2h and t_0=1/k.
The half-angle tangent formula is

```text
tan(theta(a,b)/2)=A/h.
```

At t_0 the other two denominators satisfy

```text
sqrt((A+c)k+Ac)=A+c+h,
sqrt((A+d)k+Ad)=A+d+h,
(A+c+h)(A+d+h)-A^2=h(2A+c+d+2h)>0.
```

Thus the two positive half-angle tangents A/(A+c+h), A/(A+d+h)
have product less than 1. Their angles sum to an angle in (0,pi/2),
whose tangent by the addition formula is A/h. Injectivity of tan on
this interval proves C_{t_0}(a,b)=H(a,b). Strict increase of C_t in t
then proves (3), including equality and both strict signs. There is no
uncontrolled inverse-trigonometric branch or squaring in this step.

Fix t and a>t and vary the other high b>t. Set k=1/t, A=1/R, c=1/a.
Define a threshold in the extended positive reals:

```text
B_R(t,a)=infinity,                 if k<=(sqrt(A)+sqrt(c))^2;

B_R(t,a)=1/[k+A+c-2 sqrt(k(A+c)+Ac)],
                                  if k>(sqrt(A)+sqrt(c))^2.    (4)
```

In the infinite-threshold case the chain branch is strictly larger at
every finite b>t, even when equality holds in the condition in (4).
In the finite case B_R(t,a)>t and

```text
b<B: F_t(a,b)=C_t(a,b)>H(a,b),
b=B: C_t(a,b)=H(a,b),
b>B: F_t(a,b)=H(a,b)>C_t(a,b).                         (5)
```

For completeness let w=1/b and s=A+c. The right side of (2) is
s+w+2 sqrt(Ac+sw), strictly increasing for w>=0, with value
s+2 sqrt(Ac) at zero and infinite limit. A positive crossing exists
exactly under the strict second condition of (4). Squaring k-s-w>0
gives roots w_-=k+s-2 sqrt(ks+Ac) and w_+=k+s+2 sqrt(ks+Ac).
Under that condition k-s>2 sqrt(Ac), so

```text
(k+s)^2-4(ks+Ac)=(k-s)^2-4Ac>0,
k-s-w_-=2(sqrt(ks+Ac)-s)>0,
k-s-w_+=-2(s+sqrt(ks+Ac))<0.
```

The first two expressions prove w_->0 and its correct pre-square sign;
the last rejects the extraneous root. This proves (4)-(5). At b=t,
C_t(a,t)-H(a,t)=theta(t,t)>0, hence a finite crossing lies above t.

## 3. Closed increment formula: all branches, no other cells

Define the clipped threshold and a cell increment, for t<min(a,x), x<y:

```text
q(t,a)=min(y,max(x,B_R(t,a))),
I(t,a;x,y)=theta(t,q)-theta(t,x)+theta(a,y)-theta(a,q),  (6)
q=q(t,a).
```

An infinite B clips to y. Equations (5) give the complete table:

| Threshold location | Cell increment F_t(a,y)-F_t(a,x) |
|---|---|
| B>=y, including infinity | theta(t,y)-theta(t,x) |
| B<=x | theta(a,y)-theta(a,x) |
| x<B<y | theta(t,B)-theta(t,x)+theta(a,y)-theta(a,B) |

The third line uses equality C_t(a,B)=H(a,B). Endpoint equalities
B=x or B=y are included in the first two lines consistently. Therefore
the requested explicit local variation is

```text
Delta S_P(R)=I(l,u;x,y)-I(r,v;x,y).                   (7)
```

This evaluates every combination of the two exterior branches, including
one or both crossings; it requires no sum over the unaffected cells.
In particular define the positive kernel derivative

```text
h_R(a;b)=d theta(a,b)/db
        =sqrt(Ra)/(sqrt(b)(R+b)sqrt(R+a+b)),
d h_R(a;b)/da=sqrt(R)/(2 sqrt(ab)(R+a+b)^(3/2))>0.     (8)
```

Then I is the integral over x<b<y of h_R(t;b) until q and h_R(a;b)
after q. A branch equality at one point cannot affect this integral;
F is continuous, piecewise smooth and has only the one possible kink.

Put q_L=q(l,u), q_R=q(r,v). Formula (7) has the following exhaustive
three-interval form, with zero-length integrals omitted:

| Interval | If q_L<=q_R, integrand for Delta S | If q_R<=q_L, integrand for Delta S |
|---|---|---|
| (x,min(q_L,q_R)) | h_R(l;b)-h_R(r;b) | h_R(l;b)-h_R(r;b) |
| (min(q_L,q_R),max(q_L,q_R)) | h_R(u;b)-h_R(r;b)>0 | h_R(l;b)-h_R(v;b)<0 |
| (max(q_L,q_R),y) | h_R(u;b)-h_R(v;b) | h_R(u;b)-h_R(v;b) |

Every integral has the explicit primitive theta of (6). Thus in cases
with opposing signs the exact condition is comparison of these explicit
angular increments, not a proposed universal ordering rule.

## 4. Conditional exchange and necessary optimality conditions

**Conditional exchange theorem.** In the domain of Section 1, x<y:

```text
l<=r, u<=v, q_L>=q_R  => Delta S_P<=0;                (9)
l>=r, u>=v, q_L<=q_R  => Delta S_P>=0.                (10)
```

The middle interval has the stated strict sign since every high exceeds
every low. The exterior intervals have the weak stated signs by (8).
This proves both implications. In either implication equality occurs
exactly when

```text
q_L=q_R=q,
(q=x or l=r), and (q=y or u=v).                       (11)
```

Indeed unequal thresholds give a nonempty interval of strict sign. When
the thresholds agree, each remaining integral is zero exactly when its
interval is empty or its two anchors agree. For actual m>=3 one has
l!=r; equality in these implications requires all-chord increments and
u=v (the coincident exterior high is specific to m=3). There are no other
equality branches. These sufficient ordering conditions are not claimed necessary
when contributions of opposite signs compensate.

Particularly simple EXACT signs, without comparing thresholds in their
interiors, are:

| Left increment throughout [x,y] | Right increment throughout [x,y] | sign(Delta S_P) |
|---|---|---|
| chain | chain | sign(l-r) |
| chord | chord | sign(u-v) |
| chain | chord | negative |
| chord | chain | positive |

At fixed R, every minimizing permutation exists in a finite set and must
have Delta S_P>=0 for every actual adjacent swap. Consequently it cannot
contain an ascending interior pair P_j<P_{j+1}, 1<=j<=m-2, whose two
exterior increments are chain throughout [P_j,P_{j+1}]. Other exclusions
follow from (9)-(11) and the table; actual descending pairs reverse signs.
The low seam must use l>r for j=m-1,m, not the interior rule l<r.
These are necessary local conditions, not a proof that a local minimum is
global or that swaps connect every better order by a decreasing path.

For optimization of the full radius, the earlier note gives the unique
root rho_P of S_P=2*pi. A strict negative Delta S at R=rho_P implies
rho_{P'}<rho_P by strict decrease of S_{P'}. Hence any radius minimizer
also satisfies the local nonnegative-swap condition AT ITS OWN ROOT.
A sign or structural restriction proved at another R does not imply it
at rho_P. None of these statements addresses orders outside this family.

## 5. An exact small-R reduction and the cyclic-shift obstruction

**Structural corollary.** For every m>=3 and 0<R<=1, every minimizer of
S_P(R) over the allowed permutations satisfies

```text
P_1>P_2>...>P_{m-1},    P_{m-1}<P_m<P_1.             (12)
```

Equivalently P_1=2m, P_{m-1}=m+1, and one chooses
P_m in {m+2,...,2m-1}; the other highs occupy the first m-1 positions
in strictly decreasing order. There are only m-2 possible candidates.
This is a necessary reduction, not a claim that all candidates minimize.

Proof: K_R(a,b)>1/R>=1>=1/i for every low i. Thus all cells and every
intermediate moving-high value are strictly chain-active. The first row
of the preceding table excludes all interior ascents, and excludes a
descent at either of the two wrap swaps, where l>r. This proves (12)
and the endpoint/range characterization. Existence of a minimum is
automatic on the finite set. At m=2 both permutations remain tied.

In particular, NO increasing cyclic shift
P_i=m+1+((i+s-1) mod m) minimizes S_P(R) when m>=4 and 0<R<=1.
A shift satisfying the necessary P_1=2m would have
(P_1,P_2,P_3)=(2m,m+1,m+2), an excluded interior ascent. Every other
shift already fails (12). The inequalities are strict, so no such shift
ties for the minimum. For m=3 the sole candidate (6,4,5) is a cyclic
shift; for m=2 all orders are shifts and tied. Thus m=4 is minimal for
this small-R shift obstruction, without relying on a finite search.

A concrete witness at m=4,R=1 is P=(8,6,5,7). Exact rational angular
enclosures in the checker show it beats all four shifts by more than
8/1000. The initial scan also retained P=(6,8,7,5),R=10, which beats
all four shifts at that R. Neither fixed-R comparison by itself refutes
optimality of shifts for the separate full-radius objective. General root
optimization and permutation asymptotics have not been undertaken.

## 6. Minimal sign reversal and the precise Monge failure

**Disproved rule:** the sign of an adjacent swap is determined by the
relative ordering of the exterior radii and swapped highs, independently
of R; in particular the chain-only sign sign(l-r) is not universal.

Take the same swap

```text
m=3, P=(4,5,6), P'=(5,4,6), j=1,
l=1, r=3, u=v=6, x=4, y=5.
```

At R=1 both exterior increments are chain, so Delta S<0. At R=100 the
left increment is chord and the right is chain, so Delta S>0. The branch
tests are exact via (3). Explicitly put e=1/t-A-c-d and
D=Ac+Ad+cd. If e<=0 the chain branch is strict; if e>0 then
sign(C_t-H)=sign(4D-e^2). At R=100 the two left-cell endpoint triples
(t,a,b)=(1,6,4),(1,6,5) have e=43/75,187/300>0 and respectively
4D-e^2=-3271/22500,-21649/90000<0. The right-cell triples
(3,6,4),(3,6,5) have e=-7/75,-13/300<0. The one-crossing lemma
then fixes each branch on the whole interval [4,5]. These are exact
rational sign gates, also checked by the retained Fraction checker.
There are no threshold equalities.
Rational series enclosures additionally give robust numerical margins:

```text
R=1:   -0.017413 < Delta S < -0.017412;
R=100:  0.002980 < Delta S <  0.002981.                (13)
```

Thus neither a universal chain sign nor even the weak rule
`l<r and u<=v => Delta S<=0` is valid. A chord-only rule also fails:
u=v does not force Delta S=0. This is minimal in m in the entire task
domain, since all m=2 swaps have Delta S=0 for every R>0. By continuity
the strict signs persist in neighborhoods of these radii; this is not
a floating-point tie or an isolated threshold event. Reversing the
orientation does not remove the failure.

The angular kernel ITSELF retains strict increasing differences:
theta_ab>0 by (8). Moreover F_t(a,b), for fixed low t and highs a,b>t,
retains WEAK increasing differences in its two high coordinates. Indeed
g=H-C_t has g_a=h_R(b;a)-h_R(t;a)>0. Increasing a can only switch a
fixed-b cell from chain to chord. Its b derivative then changes from
h_R(t;b) to the larger h_R(a;b), and the latter increases with a.
Integrating this nondecreasing derivative in b proves

```text
F_t(a',b')+F_t(a,b)>=F_t(a',b)+F_t(a,b')
for t<a<a', t<b<b'.                                  (14)
```

Strictness is not universal: a rectangle wholly in the chain branch
has zero cross difference. No violation of (14) is claimed.

What FAILS is increasing differences between the LOW label and a moving
HIGH, with the other high fixed. Define

```text
M=F_{t'}(a,y)-F_{t'}(a,x)-F_t(a,y)+F_t(a,x).
```

For the valid m=3 data t=1,t'=2,a=4,x=5,y=6, at R=1 all increments
are chain and M>0 by h_R(2;b)>h_R(1;b). At R=100 the t=1 increment
is chord while t'=2 is chain, and M<0 by h_R(2;b)<h_R(4;b).
Again the checker verifies all four branch tests exactly. Thus F has
neither a uniform Monge nor a uniform anti-Monge inequality in these
low/high coordinates. For an explicit rational audit at R=100, all four
gates e are positive and the values of 4D-e^2 for
(t,a,b)=(1,4,5),(1,4,6),(2,4,5),(2,4,6) are respectively
-46/625, -3271/22500, 541/2500, 1001/5625. These establish the
claimed branches throughout [5,6] by the one-crossing lemma.
Increasing the low can move the active derivative
DOWN from the high anchor to the low anchor. Rearranging the highs
against ordered low positions as if this were a fixed anti-Monge
assignment ignores precisely that branch change. The useful repair is
the threshold-aware rule (9)-(10), not a claim that every exchange or
uncrossing principle is impossible.

## 7. Verification and scope of authority

Before universal sign proofs, the deterministic bounded checker scanned
all 872 permutations for m=2..6 on six radii, 15114 ascending cyclic
swaps and 5232 comparisons against shifts. It found the sign reversal,
both low/high cross-difference signs, and a nonshift improvement. These
are float64 observations, with an exclusion guard, not proof premises.

The separate checker uses symbolic identities, exact rational branch
tests, rigorously bounded rational square roots and the positive asin
series for the retained witnesses. It also compares the local threshold
formula with independent 70-digit atan full cell sums, including every
cyclic seam, m=2 degeneracy and m=3 coincident exterior highs. Additional
positive-real cell probes cover all nine combinations of increment
branches and explicit threshold endpoints; these are not integer-half
permutation samples.
Exact enclosures certify only the displayed local inequalities; the
70-digit scan is numerical corroboration. Complete bounds, commands,
outputs and hashes are in `ops/TASK-20260905__adjacent_high_swap/`.

The proofs here concern the exact fixed-R objective and its immediate
local/root implications. They do not certify a global geometric optimum,
extend the finite certified range, optimize the large-m permutation
problem, alter any global asymptotic coefficient, or classify contacts
or floating circles. The single thematic owner is
`knowledge/FIXED_ORDER_THEORY.md`. The preceding fixed-order theorem,
production implementation, independent verifier and arXiv v1 are unchanged.
