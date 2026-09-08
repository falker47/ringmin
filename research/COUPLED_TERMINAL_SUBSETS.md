# Two nested terminal subsets: exact incompatibility and separation

    status=PROVED
    classification=exact counterexample / exact minimal-ambient-size theorem
    domain=integers 3<=N<M<=n; T_j={n-j+1,...,n}
    proved_on=2026-09-09
    published_snapshot=arXiv v1 remains unchanged

## 1. Question and result

For distinct positive radii define

```text
theta_R(a,b)=2 asin sqrt(ab/((R+a)(R+b))),
F_sigma(R)=sum_{cyclic edges (a,b) of sigma} theta_R(a,b).
```

For a cycle with at least three vertices, F_sigma decreases continuously
from |sigma| pi to zero on R>0. Its unique 2 pi root is R_chain(sigma).
Restriction deletes the omitted vertices and joins successive survivors,
including the closing edge. Cycles are identified up to rotation and
reversal. Write

```text
A_j=R_chain(Supnick(T_j)),
B_{M,N}=min_{sigma a cycle on T_M}
             max{R_chain(sigma), R_chain(sigma|T_N)}.
```

Always B_{M,N}>=max{A_M,A_N}. The proposed equality for every admissible
triple is **false**.
Allowing N=M adds only the trivial equality cases B_{M,M}=A_M.

**Exact counterexample.** At n=M=8, N=7, put

```text
S=(1,7,3,5,4,6,2,8)=Supnick({1,...,8}),
T=(2,7,4,5,6,3,8)=Supnick({2,...,8}),
I=S|{2,...,8}=(7,3,5,4,6,2,8),
r_0=R_chain(S).
```

Then

```text
R_chain(T)<23/4<r_0<144/25,
R_chain(I)>577/100,
B_{8,7}>r_0+1/6000=max{A_8,A_7}+1/6000.             (1)
```

Here B_{8,7} is evaluated in the ambient set {1,...,8}. Moreover, for
every 3<=N<M<=n<=7 the proposed equality holds. Thus **8 is the smallest
ambient n admitting a counterexample**. We do not need to identify the
tour attaining B_{8,7} or its exact value.

If the notation T_M subset {1,...,n} requires a **proper** outer subset,
the identity is still false: at n=13,M=12,N=11,

```text
B_{12,11}>max{A_12,A_11}+1/5000.                       (1p)
```

In that stricter domain 3<=N<M<n, the smallest ambient counterexample
size is **13**, proved in Section 7. Thus neither convention for the
outer inclusion changes the negative answer.

There is a separate, earlier obstruction to compatibility itself:
M=5,N=4 already fails for every terminal translate (indeed for the top
four of any five distinct positive radii). Compatibility is sufficient
for the minimax equality but is not necessary; see Section 6.

## 2. A strictness lemma for the universal Supnick tour

The imported matrix-level theorem is: the same Supnick rank cycle
minimizes tour cost on **every symmetric anti-Monge matrix**. Equivalently
it maximizes cost on every symmetric Monge matrix after negating the
entries. This is the classical matrix theorem used in the published
[chain theorem](../paper_assets/ringmin_paper.tex), not an assumption that
a perturbed matrix is still an angular kernel. A precise external source
is Burkard, Deineko, van Dal, van der Veen and Woeginger,
[*Well-solvable special cases of the Traveling Salesman Problem: a survey*](https://pure.tue.nl/ws/files/2373438/Metis148543.pdf),
Section 2.2.3, p.507, together with Proposition 2.13(i), p.508.

**Lemma.** If a symmetric matrix c is strictly anti-Monge, its universal
Supnick minimizer is unique as an undirected cycle. If every rectangle
slack

```text
c_ij+c_i'j'-c_ij'-c_i'j > 2 epsilon
                       (i<i', j<j')                    (2)
```

for epsilon>0, every different cycle has cost at least the Supnick cost
plus epsilon.

Proof. A different undirected cycle H has an edge e absent from S.
Decrease the two symmetric entries for e by epsilon, leaving all others
(including diagonal entries) unchanged. A rectangle contains at most two
modified entries, so its slack can decrease by at most 2 epsilon. The
new matrix remains symmetric anti-Monge by (2). The matrix theorem
therefore still makes S minimizing. Its cost is unchanged, whereas H's
cost decreases by exactly epsilon: an undirected tour edge is counted
once. Consequently cost_c(H)>=cost_c(S)+epsilon. For arbitrary strict
anti-Monge c, take epsilon smaller than half the least of its finitely
many positive rectangle slacks. This proves uniqueness. QED.

For the angular matrix, include the analytic diagonal values theta_R(a,a)
when checking rectangles, even though they are not tour edges. Direct
differentiation gives

```text
partial_a partial_b theta_R(a,b)
    =sqrt(R)/(2 sqrt(ab) (R+a+b)^(3/2))>0.              (3)
```

Thus all ordered-radius rectangle slacks are positive integrals of (3).
The lemma applies at every R>0 for arbitrary distinct positive radii.
At the Supnick chain root any different cycle has closure sum strictly
above 2 pi, hence a strictly larger root. Chain minimizers are therefore
unique up to rotation/reversal too. No uniqueness assumption was imported
from the angular version of the published theorem.

## 3. Four explicit rational gates

This section proves the root comparisons in (1) by finite rational
inequalities. No tour enumeration, numerical root, or certificate artifact
is a premise. The arithmetic expressions below are part of the proof;
the task-local checker merely reproduces them.

Put D=10^6 and

```text
P(x)=sum_{j=0}^{11} binom(2j,j) x^(2j+1)/(4^j(2j+1)).
```

All coefficients of the arcsine series are positive and at most one, so
for 0<x<1,

```text
P(x)<asin(x)<P(x)+x^25/(1-x^2).                        (4)
```

For an edge (a,b) at the listed rational R let
z=ab/((R+a)(R+b)). The integers p below satisfy

```text
(p/D)^2<=z<((p+1)/D)^2.                               (5)
```

Use x=p/D in the lower side of (4), and y=(p+1)/D in the upper
side. Twice the sums of these rational expressions give bounds L<F<U
on the complete cyclic closure sum. Edges are listed in increasing
lexicographic order:

```text
E(S): (1,7),(1,8),(2,6),(2,8),(3,5),(3,7),(4,5),(4,6)
E(T): (2,7),(2,8),(3,6),(3,8),(4,5),(4,7),(5,6)
E(I): (2,6),(2,8),(3,5),(3,7),(4,5),(4,6),(7,8).
```

| Cycle and R | Integers p in that edge order | l | u |
|---|---|---:|---:|
| S, 23/4 | 285195, 293590, 363011, 387487, 399334, 433860, 436825, 457703 | 628726 | 628728 |
| S, 144/25 | 284872, 293266, 362623, 387097, 398921, 433443, 436399, 457274 | 628049 | 628051 |
| T, 23/4 | 376407, 387487, 418420, 446632, 436825, 474593, 487346 | 626827 | 626829 |
| I, 577/100 | 362236, 386707, 398508, 433026, 435973, 456846, 564327 | 630128 | 630131 |

In each row, rational substitution gives

```text
l/10^5 < L=2 sum P(p/D)
        < F
        < U=2 sum [P((p+1)/D)+((p+1)/D)^25/(1-((p+1)/D)^2)]
        < u/10^5.                                     (6)
```

Equations (5)-(6) are explicit integer/rational inequalities: they can
be verified by squaring and clearing positive denominators. For the
comparison constant, let

```text
H(x)=sum_{j=0}^7 (-1)^j x^(2j+1)/(2j+1).
```

The alternating series bounds H(x)<atan(x)<H(x)+x^17/17 and Machin's
identity pi=16 atan(1/5)-4 atan(1/239) give by rational substitution

```text
3141592653/10^9 < pi < 3141592654/10^9.                 (7)
```

The first and fourth rows of (6) lie strictly above 2 pi; the second
and third lie strictly below it. Strictly decreasing closure sums prove
all three root comparisons in the first two lines of (1).

The independent arithmetic corroboration also uses
theta_R(a,b)=2 atan sqrt(ab/(R(R+a+b))) with alternating-series bounds,
different square-root enclosures, and no floating-point operations.

## 4. Uniform positive separation for every larger tour

At R=r_0 the gates give 5<r_0<6. Throughout 5<=R<=6 and 1<=a,b<=8,
equation (3) has the explicit lower bound

```text
partial_a partial_b theta_R(a,b)
  > 2/(2*8*22*5)=1/880.                               (8)
```

Here sqrt(R)>2, sqrt(ab)<=8, R+a+b<=22 and sqrt(22)<5.
Every ordered integer rectangle has both side lengths at least one.
Its slack is therefore >1/880. Choose epsilon=1/2000; then
1/880>2 epsilon=1/1000. Section 2 now gives, simultaneously for
**every** cycle H on {1,...,8} with E(H)!=E(S),

```text
F_H(r_0)>=2 pi+1/2000.                                (9)
```

To turn this into a radius separation, put
u=sqrt(ab/((R+a)(R+b))). For R>=5 and 1<=a,b<=8,

```text
|partial_R theta_R(a,b)|
  =u/sqrt(1-u^2) * (1/(R+a)+1/(R+b))
  <(4/5)(1/3)=4/15.                                  (10)
```

Indeed u<=8/13, sqrt(1-u^2)>=sqrt(105)/13>10/13, and
each denominator R+a,R+b is at least 6. An eight-edge closure sum thus
has |F'_H|<32/15<3 on R>=5. Integrating (10) from r_0 to
r_0+1/6000 in (9) leaves F_H strictly above 2 pi. Hence

```text
R_chain(H)>r_0+1/6000,           E(H)!=E(S).             (11)
```

The only remaining cycle is S up to rotation/reversal. Its restriction
has the same undirected edges as I, and the fourth gate gives

```text
R_chain(I)>577/100>144/25+1/6000>r_0+1/6000.            (12)
```

Equations (11)-(12) cover all cycles. There are finitely many, so their
minimum still satisfies the strict inequality in (1). Section 3 gives
A_7<r_0=A_8, identifying the independent maximum exactly. This is a
positive-separation proof without enumerating any competing tour.

## 5. Smallest ambient n

We use three exact, previously proved analytic facts, not the finite
global certificates:

- The [triangle/path theorem](SUPNICK_FULL_FEASIBILITY.md), Sections 2-3:
  for a set {k,...,n}, every simple path P with m edges satisfies
  sum_P theta_R - theta_R(endpoints)>=(m-1) delta_R, where
  delta_R=theta_R(n,k)+theta_R(k,n-1)-theta_R(n,n-1).
- The [radius-1 seam theorem](RADIUS1_SEAM_OBSTRUCTION.md), Sections 5-6:
  delta_R>0 at the Supnick root for k=1 and 3<=n<=7.
- The [fixed-k threshold theorem](FIXED_K_SUPNICK_SEAM.md), Section 4:
  delta_R>0 at every R>0 for k+2<=n<=4k.

Let 3<=N<M<=n<=7 and k=n-M+1. If k=1 the second fact applies;
if k>=2 then n<=7<4k and the third fact applies. Thus at the larger
Supnick root A_M every simple path has nonnegative defect.

The paths between consecutive survivors of T_N partition the edges of
the larger cycle, including the cyclic seam. Replace each such path by
its direct edge and sum the path inequalities. The induced closure sum
is at most the original 2 pi, giving

```text
R_chain(Supnick(T_M)|T_N)<=A_M,
A_N<=R_chain(Supnick(T_M)|T_N)<=A_M.
```

This same larger cycle attains the minimax value A_M, while the universal
lower bound is max{A_M,A_N}=A_M. Equality follows for every admissible
triple with n<=7. Together with (1), this proves minimal ambient size 8.
The argument also covers all N=3 possibilities; a three-vertex cycle has
only one undirected edge set. Cardinalities below three have no positive
chain-closure root in this model and are outside the definition.

## 6. Structural explanation and the compatibility distinction

The larger Supnick cycle has the two smallest-radius seam edges (1,7)
and (1,8). Deleting radius 1 replaces them by (7,8):

```text
F_I(R)-F_S(R)=theta_R(7,8)-theta_R(1,7)-theta_R(1,8).
```

At r_0 this is positive, consistently with the exact n=8 seam onset.
The canonical minimizing cycle on {2,...,8} has a different edge set.
Strict anti-Monge optimality charges a positive cost for every change
to the larger cycle; keeping that cycle incurs the induced seam cost.
This is the obstruction behind the minimax separation.

Compatibility itself fails even earlier. On increasing ranks 1,...,5,
the unique minimizing cycle is (1,4,3,2,5). Its restriction to ranks
2,...,5 is (4,3,2,5), whereas their unique minimizing cycle is
(2,4,3,5). The edge sets differ. Section 2 proves uniqueness for every
choice of five distinct positive radii, so neither a different angular
radius nor a terminal translation can restore simultaneous optimality.
With M<=4 the only proper admissible smaller size is N=3, for which
every restriction is optimal. Thus M=5,N=4 is the smallest-cardinality
compatibility obstruction. Nevertheless at n=5 the minimax equality
holds by Section 5. A proof of incompatibility alone would therefore
not have answered the displayed question.

## 7. Proper outer subset: exact counterexample and minimality

Now require M<n. At n=13,M=12,N=11 let

```text
S12=(2,12,4,10,6,8,7,9,5,11,3,13)=Supnick({2,...,13}),
T11=(3,12,5,10,7,8,9,6,11,4,13)=Supnick({3,...,13}),
I11=S12|{3,...,13},
r_1=R_chain(S12).
```

Using exactly P,D,L,U and the pi enclosure in Section 3, four further
rational rows prove

```text
R_chain(T11)<1827/100<r_1<457/25,
R_chain(I11)>183/10.                                   (13)
```

The edge lists and p values for the same inequalities (5)-(6) are

```text
E(S12): (2,12),(2,13),(3,11),(3,13),(4,10),(4,12),
        (5,9),(5,11),(6,8),(6,10),(7,8),(7,9)
E(T11): (3,12),(3,13),(4,11),(4,13),(5,10),(5,12),
        (6,9),(6,11),(7,8),(7,10),(8,9)
E(I11): (3,11),(3,13),(4,10),(4,12),(5,9),(5,11),
        (6,8),(6,10),(7,8),(7,9),(12,13).
```

| Cycle and R | Integers p in that edge order | l | u |
|---|---|---:|---:|
| S12, 1827/100 | 197775, 202533, 230229, 242150, 252061, 266842, 266296, 284165, 274382, 295718, 290443, 302360 | 628508 | 628512 |
| S12, 457/25 | 197694, 202450, 230136, 242054, 251960, 266738, 266190, 284056, 274273, 295604, 290330, 302245 | 628255 | 628258 |
| T11, 1827/100 | 236461, 242150, 259809, 273260, 275691, 291857, 285640, 304807, 290443, 313028, 317025 | 626690 | 626694 |
| I11, 183/10 | 229949, 241863, 251758, 266530, 265978, 283837, 274056, 295378, 290105, 302015, 405572 | 630763 | 630766 |

The proof of all-tour separation is identical in form but has new
explicit constants. On 18<=R<=19, 2<=a,b<=13, equation (3) gives

```text
partial_a partial_b theta_R(a,b)
   >4/(2*13*45*7)=2/4095>2/5000,
```

using sqrt(R)>4 and sqrt(R+a+b)<=sqrt(45)<7. Integer rectangles
therefore meet (2) with epsilon=1/5000. Every cycle H different from
S12 has F_H(r_1)>=2 pi+1/5000. For R>=18, u<=13/31 and
sqrt(1-u^2)>=sqrt(792)/31>28/31; also R+a,R+b>=20. Thus

```text
|partial_R theta_R(a,b)|<(13/28)(1/10)=13/280,
|F'_H(R)|<12*13/280=39/70<1.
```

Integrating to r_1+1/5000 leaves F_H above 2 pi. The unchanged cycle
has induced root >183/10>457/25+1/5000. The two cases prove (1p)
without enumerating any tour. Structurally, deleting 2 replaces the
seam edges (2,12),(2,13) by (12,13).

For minimality suppose n<=12 and 3<=N<M<n; then k=n-M+1>=2.
For k=2, the exact [radius-2 seam theorem](RADIUS2_SEAM_THRESHOLD.md),
Sections 4-5, gives positive defect at the larger Supnick root for
4<=n<=12. For k>=3, n<=12<=4k gives positive defect by the fixed-k
no-threshold theorem. The same path-partition argument in Section 5
proves B_{M,N}=max{A_M,A_N} for every such triple. Ambient size 13
is consequently minimal when both inclusions must be proper.

## 8. Lower-bound meaning and limits

Deleting circles from any feasible configuration preserves all surviving
constraints. Each induced chain sum is at most 2 pi at its radius, so
minimizing over the induced order on T_M gives the valid lower bound

```text
R*(n)>=B_{M,N}>=max{A_M,A_N}.
```

The first inequality uses actual feasibility only to justify a lower
bound; no feasible configuration is constructed here. Equation (1)
shows that coupling two terminal chain constraints can strictly improve
the maximum of their separate minima at a finite n.

This does not compute either counterexample's exact minimax or global
geometric value, expand finite global certification, improve C_term,
prove a positive asymptotic gain, or classify all triples with strict
separation. The lower-bound direction
remains scientifically viable, but quantitative large-n amplification
requires a separate task. The third-block construction and its widths,
all prior coefficients, and the arXiv-v1 paper remain unchanged.

Canonical stable ownership: the coupled-subset entry in
[knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md](../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md).
Task-local arithmetic and handoff:
[ops/TASK-20260908__coupled_terminal_subsets/](../ops/TASK-20260908__coupled_terminal_subsets/).
