# A self-contained fixed-order seam theorem for the finite Ringmin paper

**Classification:** exact theorem and proved corollaries; prepared for
independent STRICT review on 2026-09-19. This package proves the general
feasibility criterion, persistence for each fixed smallest radius, and the
first three complete classifications. Its proof uses elementary geometry,
calculus and explicit rational inequalities only. No repository theorem,
solver output, numerical root or certificate is a premise.

## 1. Definitions and statement

All surrounding circles are externally tangent to a central circle of radius
$R>0$. For surrounding radii $a,b>0$, define

$$
 \theta_R(a,b)=2\arcsin\sqrt{\frac{ab}{(R+a)(R+b)}}\in(0,\pi).
 \tag{1}
$$

If their centers have counterclockwise angular separation $A\in[0,2\pi]$,
the squared distance between them is
$(R+a)^2+(R+b)^2-2(R+a)(R+b)\cos A$. Thus their interiors are disjoint
if and only if

$$
 \theta_R(a,b)\le A\le2\pi-\theta_R(a,b).
 \tag{2}
$$

Indeed, the distance requirement is equivalent to
$\cos A\le1-2ab/((R+a)(R+b))=\cos\theta_R(a,b)$. In particular,
**both** directed arcs between a pair must have length at least its required
angle. Tangencies, including nonadjacent tangencies, are allowed.

Fix integers $k\ge1$, $n\ge k+2$, and put $N=n-k+1$. The
**canonical Supnick cycle** $\sigma_{k,n}$ is defined by the following
rank rule, which specifies every entry, without an order ellipsis.
Put $H=\lceil N/2\rceil$. For successive integers $j\ge0$:

- In a list $A$, append $1+2j$ if it is at most $H$, then append
  $N-1-2j$ if it is greater than $H$.
- In a list $B$, append $2+2j$ if it is at most $H$, then append
  $N-2-2j$ if it is greater than $H$.

Stop each list when neither entry can be appended. Concatenate $A$, the
reverse of $B$, and the singleton $N$; replace each rank $i$ by
$k+i-1$, and join the last entry to the first. Low ranks partition
$1,\ldots,H$ by parity, high ranks partition $H+1,\ldots,N-1$, and
the appended rank is $N$. Hence this is a cycle through each radius once.
Rotations and reversal represent the same undirected cycle.
Subscripts on cycle entries are read modulo $N$.

Let $E_{k,n}$ be its undirected edge set, and define

$$
 C_{k,n}(R)=\sum_{(a,b)\in E_{k,n}}\theta_R(a,b),\qquad
 C_{k,n}(R_{k,n})=2\pi,\qquad R_{k,n}=R_{\rm chain}(\sigma_{k,n}).
 \tag{3}
$$

Existence and uniqueness of this positive root are proved below. At any
radius write

$$
 \delta_R=\theta_R(n,k)+\theta_R(k,n-1)-\theta_R(n,n-1),\qquad
 \Delta_{k,n}=\delta_{R_{k,n}}.
 \tag{4}
$$

A **fully feasible placement in this fixed order** consists of angles
$\phi_0<\cdots<\phi_{N-1}<\phi_0+2\pi$, with centers
$(R+s_i)(\cos\phi_i,\sin\phi_i)$, where
$(s_0,\ldots,s_{N-1})=\sigma_{k,n}$, such that (2) holds for every
pair. The **cumulative-angle placement at the chain root** has $\phi_0=0$
and successive gaps $\theta_{R_{k,n}}(s_i,s_{i+1})$, including the
closing gap. Define $R_{\rm full}(\sigma)$ as the infimum of radii
admitting a fully feasible placement in order $\sigma$.

**Theorem (fixed-order seam criterion and persistence).** For every pair of
integers $k\ge1,n\ge k+2$:

1. The positive chain root exists uniquely. The following are equivalent:
   $\Delta_{k,n}\ge0$; the cumulative-angle placement at $R_{k,n}$
   is fully feasible; some fully feasible placement of this order exists at
   $R_{k,n}$. When these hold,
   $R_{\rm full}(\sigma_{k,n})=R_{k,n}$.
2. For each fixed $k$, there is a finite integer
   $s_k\ge4k+1$ such that $\Delta_{k,n}<0$ for every $n\ge s_k$.
   For $k+2\le n<s_k$ the deficit is positive, with at most one
   possible exception: $\Delta_{k,s_k-1}=0$. Thus feasibility at the
   chain root holds exactly before $s_k$, and failure persists thereafter.
3. For $k=1,2,3$, the complete classifications are:

   | Smallest radius | Fully feasible at the chain root, with $\Delta_{k,n}>0$ | Infeasible in this order at the chain root, with $\Delta_{k,n}<0$ |
   |---|---|---|
   | $k=1$ | $3\le n\le7$ | $n\ge8$ |
   | $k=2$ | $4\le n\le12$ | $n\ge13$ |
   | $k=3$ | $5\le n\le16$ | $n\ge17$ |

   In particular $s_1=8,s_2=13,s_3=17$, with no integer equality
   case for these three values of $k$.

The proof does not assert the absence of equality for every $k\ge4$,
nor give an explicit formula for their onsets. It establishes the weak
criterion in part 1 even when equality is not excluded.

## 2. Exact edges, both parities, and growth of the chain root

Put $L=k+n$. Reading the rank rule gives the following edge lists;
indexed families are listed in increasing order of $i$:

$$
\begin{array}{ll}
 N=2h:\quad &(k,n),\ (k+h-1,k+h),\\
 &(i,L-1-i),\quad k\le i\le k+h-2,\\
 &(i,L+1-i),\quad k+1\le i\le k+h-1;\\[2mm]
 N=2h+1:\quad &(k,n),\\
 &(i,L-1-i),\quad k\le i\le k+h-1,\\
 &(i,L+1-i),\quad k+1\le i\le k+h.
\end{array}
 \tag{5}
$$

Here $h\ge2$ in the even case and $h\ge1$ in the odd case. To
check the formula directly, consecutive low/high ranks inside either list
alternate endpoint sums $N$ and $N+2$. After translation these are
$L-1$ and $L+1$. The closing edge is $(k,n)$. At the join of
the two lists, an even-sized cycle has the additional central edge
$(k+h-1,k+h)$; an odd-sized cycle completes the two indexed families
instead. Their lower endpoints run through exactly the ranges in (5).
The counts are $2+(h-1)+(h-1)=2h$ and $1+h+h=2h+1$.
The endpoint ranges give distinct edges, so none is omitted or repeated.

For $N=3$ the cycle is $(k,k+1,k+2)$. For every $N\ge4$,
the rank list starts with $(1,N-1)$ and ends with $N$.
Consequently the two neighbors of $k$ are exactly $n-1,n$ in both
parities, including $N=3$.

For fixed positive $a,b$, (1) is continuous and strictly decreasing in
$R$, with limits $\pi$ at zero and zero at infinity. Hence
$C_{k,n}$ decreases continuously from $N\pi>2\pi$ to zero.
This proves the asserted existence and uniqueness.

**Lemma 1 (growth without an ordering-optimality premise).** For fixed
$k$, $R_{k,n+1}>R_{k,n}$, and $R_{k,n}\to\infty$.

*Proof.* The kernel strictly increases in either surrounding radius, since
$a/(R+a)$ and $b/(R+b)$ do so separately in (1).
Compare (5) at $n$ and $n+1$, so $L$ increases by one.

- If $N=2h+1$, match the seam and each indexed edge $(a,b)$ to
  $(a,b+1)$. The new even list contains all these edges and the
  additional central edge $(k+h,k+h+1)$.
- If $N=2h$, match the seam and each indexed edge to $(a,b+1)$,
  retaining the old central edge $(k+h-1,k+h)$ unchanged. That retained
  edge is the last member of the new lower-sum family. The only remaining
  edge in the new odd list is $(k+h,k+h+1)$.

Thus for every $R>0$, $C_{k,n+1}(R)>C_{k,n}(R)$. Strict decrease
in $R$ implies strict growth of the roots. No deletion of a vertex and
no optimality over other cycles is used.

All endpoints are at least $k$; at the root,
$2\pi\ge2N\arcsin(k/(R_{k,n}+k))$. Inversion on the increasing
branch, followed by $\sin x\le x$, gives

$$
 R_{k,n}\ge k\bigl(\csc(\pi/N)-1\bigr)
             \ge k(N/\pi-1)\longrightarrow\infty
 \quad (k\text{ fixed}). \tag{6}
$$

This completes the proof. $\square$

## 3. The least triangle defect and the fan identity

**Lemma 2 (triangle defect, including equality).** For any three distinct
members $a,b,c$ of $\{k,\ldots,n\}$, at every $R>0$,

$$
 \theta_R(a,b)+\theta_R(b,c)-\theta_R(a,c)\ge\delta_R.
 \tag{7}
$$

Equality holds exactly when $b=k$ and $\{a,c\}=\{n-1,n\}$.

*Proof.* Suppress $R$ from the notation. Differentiating (1) on the
positive domain gives

$$
 \theta_1(a,b)=\frac{\sqrt{Rb/a}}{(R+a)\sqrt{R+a+b}}>0,\qquad
 \theta_{12}(a,b)=\frac{\sqrt R}{2\sqrt{ab}(R+a+b)^{3/2}}>0.
 \tag{8}
$$

Exchange endpoints so that $a<c$. Decreasing the middle argument
$b$ to $k$ gives
$\theta(a,b)+\theta(b,c)-\theta(a,c)\ge H(a,c)$, strictly if
$b>k$, where $H(x,z)=\theta(x,k)+\theta(k,z)-\theta(x,z)$.
Analytic values such as $\theta(k,k)$ are legitimate here; they are
not self-pair constraints. For $x,z\ge k$,

$$
 H_1(x,z)=\theta_1(x,k)-\theta_1(x,z)\le0,\qquad
 H_2(x,z)=\theta_2(k,z)-\theta_2(x,z)\le0.
$$

The inequalities are strict respectively when $z>k$ and $x>k$.
Since $a\le n-1$, $c\le n$, $c>k$, and $n-1>k$,
increasing first $a$ to $n-1$, then $c$ to $n$, proves
$H(a,c)\ge H(n-1,n)=\delta_R$. More explicitly the difference is

$$
 \int_a^{n-1}\int_k^c\theta_{12}(x,y)\,dy\,dx
 +\int_c^n\int_k^{n-1}\theta_{12}(x,y)\,dx\,dy.
 \tag{9}
$$

It vanishes exactly when $a=n-1,c=n$. Together with the strict
middle-argument comparison this proves the equality statement. This argument
covers every ordering of the three distinct radii. $\square$

For a simple path $P=(v_0,\ldots,v_m)$, define its angular slack as
the sum of its $m$ edge angles minus $\theta_R(v_0,v_m)$.
For $m\ge2$, cancellation gives the exact fan identity

$$
 S_R(P)=\sum_{j=1}^{m-1}
 [\theta_R(v_0,v_j)+\theta_R(v_j,v_{j+1})-\theta_R(v_0,v_{j+1})]
 \ge(m-1)\delta_R. \tag{10}
$$

All triples are distinct, so Lemma 2 applies term by term. For $m=1$
the slack and the empty sum are both zero. If $\delta_R=0$ and
$m\ge3$, at least two distinct vertices serve as middle arguments;
they cannot both equal $k$. Thus the slack is strictly positive.
For $m=2$, equality in (10) occurs only at the seam through $k$,
up to reversal. No triangle inequality has been assumed: (7) permits a
negative lower bound.

## 4. Full feasibility, closing gap and small cycles

Work at $R=R_{k,n}$, and abbreviate $\Delta=\Delta_{k,n}$.
For two distinct positions $i<j$, the two cyclic paths are

$$
 P_+=(s_i,s_{i+1},\ldots,s_j),\qquad
 P_-=(s_j,s_{j+1},\ldots,s_{N-1},s_0,\ldots,s_i).
$$

Their edge counts are $d=j-i$ and $N-d$. Both are simple, even
when one uses the closing edge. If $\Delta\ge0$, applying (10)
separately to both paths shows that each angular length is at least
$\theta_R(s_i,s_j)$. Their sum is exactly $2\pi$ by (3).
Hence (2) holds for every pair in the cumulative-angle placement. It is
unnecessary to decide which direction is the shorter one.

For adjacent endpoints the one-edge slack is zero. Its complement has
exact slack $2\pi-2\theta_R(s_i,s_{i+1})>0$, since $\theta_R<\pi$.
This checks the upper constraint as well as the lower one, for the closing
pair just as for every other adjacent pair. Formula (2) then proves the
claimed Cartesian non-overlap, and the center radii enforce tangency to the
central circle.

Conversely, suppose some placement of this order is feasible at the chain
root. Unroll its angles and let $g_i>0$ be all $N$ consecutive
gaps, with $g_{N-1}=\phi_0+2\pi-\phi_{N-1}$. Adjacent feasibility
gives $g_i\ge\theta_R(s_i,s_{i+1})$. Therefore

$$
 \sum_i[g_i-\theta_R(s_i,s_{i+1})]=2\pi-C_{k,n}(R)=0.
 \tag{11}
$$

Every summand is nonnegative, so every gap, including the closing gap, equals
its adjacent angle. The two-edge path $(n,k,n-1)$, which exists by
section 2, consequently has length
$A=\theta_R(n,k)+\theta_R(k,n-1)$. Feasibility of its endpoints
requires $A\ge\theta_R(n,n-1)$, namely $\Delta\ge0$.
If $\Delta<0$, the complementary arc $2\pi-A$ also exceeds the
upper bound $2\pi-\theta_R(n,n-1)$. There is no freedom to repair
this failure by changing gaps at the same radius and order. This proves
all three equivalences in part 1.

At any feasible radius $r$ for this order, summing adjacent constraints
gives $C_{k,n}(r)\le2\pi$, hence $r\ge R_{k,n}$. Feasibility
at $R_{k,n}$ when $\Delta\ge0$ proves the asserted equality of
the full and chain radii.

For clarity the small cycles are explicit:

- For $N=3$, $\sigma=(k,k+1,k+2)$. All pairs are adjacent; each
  two-edge complement has slack $2\pi-2\theta_R(a,b)>0$.
  In particular $\Delta=2\pi-2\theta_R(k+2,k+1)>0$. There is no
  nonadjacent pair and no equality case.
- For $N=4$, $\sigma=(k,k+2,k+1,k+3)$. The pair $(k,k+1)$
  has the two paths through $k+2$ and through $k+3$; the pair
  $(k+2,k+3)$ has the two paths through $k$ and through $k+1$.
  These are precisely the four nonadjacent directed constraints. Lemma 2
  bounds all four defects below by $\Delta$, with equality only on the
  path through $k$. In particular the seam complement has two edges,
  not three. Adjacent complements have the positive slack already computed.
  Section 5 also gives $\Delta>0$, since $n=k+3\le4k$.

For any $N\ge4$, even a hypothetical $\Delta=0$ is sufficient:
only the two-edge seam can have zero slack among multi-edge paths, by (10)
and its equality discussion. When $\Delta>0$, the least nonadjacent
directed-path slack is exactly $\Delta$, attained only by that seam
up to reversal. Longer paths have slack at least $2\Delta$; the other
two-edge paths have strictly larger defects by Lemma 2.

## 5. Algebraic threshold and eventual persistence

We derive the threshold identity rather than invoke a circle-packing
formula. With $x=1/R$, $u=1/a$, $v=1/b$, (1) gives

$$
 \tan\frac{\theta_R(a,b)}2
 =\sqrt{\frac{ab}{R(R+a+b)}}=\frac{x}{\sqrt{x(u+v)+uv}}.
 \tag{12}
$$

Set $q=\sqrt{x(u+v)+uv}>0$ and $w=x+u+v+2q>0$. The positive
square-root identities

$$
 \sqrt{xu+(x+u)w}=x+u+q,\qquad
 \sqrt{xv+(x+v)w}=x+v+q
$$

follow by squaring. Also

$$
 (x+u+q)(x+v+q)-x^2=q(2x+u+v+2q)>0.
$$

Consequently the sum of the half-angles for pairs $(a,1/w)$ and
$(1/w,b)$ has tangent $x/q$. Each half-angle lies in
$(0,\pi/2)$; the positive denominator means their sum also lies
there. It therefore equals $\theta_R(a,b)/2$, with no branch
ambiguity. We have proved

$$
 \theta_R(a,1/w)+\theta_R(1/w,b)=\theta_R(a,b).
 \tag{13}
$$

For the seam endpoints put

$$
 \alpha_n=\frac1n+\frac1{n-1},\quad \beta_n=\frac1{n(n-1)},\quad
 P_n(x)=x+\alpha_n+2\sqrt{\alpha_n x+\beta_n}.
 \tag{14}
$$

This is the Descartes pocket curvature, but (13) proves every identity
needed here independently of that interpretation. Strict increase of the
two angles with the inserted radius gives, for every $R>0$,

$$
 \operatorname{sign}\delta_R
 =\operatorname{sign}(k-1/P_n(1/R))
 =\operatorname{sign}(P_n(1/R)-1/k). \tag{15}
$$

The function $P_n$ is continuous and strictly increasing for $x\ge0$,
and tends to infinity. Its value at zero is
$(1/\sqrt n+1/\sqrt{n-1})^2$, strictly decreasing in $n$.
At $n=4k$ it is strictly greater than $1/k$, whereas at
$n=4k+1$ it is strictly less. Thus $\delta_R>0$ for every
$R>0$ when $k+2\le n\le4k$; a unique positive crossing
$P_n(x)=1/k$ exists exactly when $n\ge4k+1$.

On this latter domain set $c=1/k$ and
$q_n=\sqrt{\alpha_n c+\beta_n}$. Squaring the crossing equation
produces $c+\alpha_n\pm2q_n$. The plus root is extraneous because
the unsquared equation requires $c-\alpha_n-x\ge0$, while the plus
root gives $-2(\alpha_n+q_n)<0$. Since the unique positive crossing
exists, it must be the minus root

$$
 \kappa_{k,n}=\frac1k+\frac1n+\frac1{n-1}
 -2\sqrt{\frac{2n+k-1}{kn(n-1)}}>0,\qquad
 T_{k,n}=\frac1{\kappa_{k,n}}. \tag{16}
$$

One can also check its branch directly: $P_n(0)<c$ gives
$q_n^2-\alpha_n^2=\alpha_n(c-\alpha_n)+\beta_n>0$, and
$\alpha_n\kappa_{k,n}+\beta_n=(q_n-\alpha_n)^2$; its positive
square root is $q_n-\alpha_n$. From (15),

$$
 \operatorname{sign}\Delta_{k,n}
 =-\operatorname{sign}(R_{k,n}-T_{k,n})\quad(n\ge4k+1).
 \tag{17}
$$

For fixed $x\ge0$, both $\alpha_n$ and $\beta_n$ strictly
decrease with $n$, so $P_{n+1}(x)<P_n(x)$. Evaluating at the
crossing and using strict increase in $x$ shows
$\kappa_{k,n+1}>\kappa_{k,n}$, hence $T_{k,n+1}<T_{k,n}$.
Equation (16) gives $T_{k,n}\to k$. Lemma 1 now implies that
$D_{k,n}=R_{k,n}-T_{k,n}$ strictly increases to infinity on
$n\ge4k+1$.

Define $s_k$ as the first integer where $D_{k,n}>0$. It exists;
the deficits are negative from then on. Before it they are positive except
possibly at one integer with $D_{k,n}=0$. Such an equality, if present,
must immediately precede $s_k$ by strict increase. The earlier
no-threshold domain has strictly positive deficits. This proves part 2,
including every quantifier, without assuming monotonicity of the raw
angular deficits.

## 6. Six exact bridges and the three onset classifications

By (17) and strict growth of $D_{k,n}$, it suffices to establish

$$
\begin{array}{ll}
 R_{1,7}<6<T_{1,7}, & T_{1,8}<51/10<R_{1,8},\\
 R_{2,12}<17<T_{2,12}, & T_{2,13}<14<R_{2,13},\\
 R_{3,16}<32<T_{3,16}, & T_{3,17}<32<R_{3,17}.
\end{array} \tag{18}
$$

Here is all the rational arithmetic needed to verify these bridges.

### 6.1 Threshold sides, with signs checked before squaring

For each row let $r$ be its separator, let
$h=1/k+\alpha_n-1/r>0$, and put
$v=4(\alpha_n/k+\beta_n)>0$. Then
$\kappa_{k,n}-1/r=h-\sqrt v$. The indicated margins are strictly
positive rational numbers:

| $(k,n)$ | $r$ | $h$ | $v$ | Positive square margin | Conclusion |
|---|---:|---:|---:|---:|---|
| $(1,7)$ | $6$ | $8/7$ | $4/3$ | $v-h^2=4/147$ | $r<T_{1,7}$ |
| $(1,8)$ | $51/10$ | $3061/2856$ | $8/7$ | $h^2-v=47737/8156736$ | $T_{1,8}<r$ |
| $(2,12)$ | $17$ | $1381/2244$ | $25/66$ | $v-h^2=239/5035536$ | $r<T_{2,12}$ |
| $(2,13)$ | $14$ | $643/1092$ | $9/26$ | $h^2-v=673/1192464$ | $T_{2,13}<r$ |
| $(3,16)$ | $32$ | $69/160$ | $17/90$ | $v-h^2=671/230400$ | $r<T_{3,16}$ |
| $(3,17)$ | $32$ | $691/1632$ | $3/17$ | $h^2-v=7465/2663424$ | $T_{3,17}<r$ |

All six rows lie in the positive-threshold domain, so reciprocation is
legitimate. No sign is inferred by squaring quantities of unknown sign.

### 6.2 Chain sides, including every closing and central edge

For each edge $e=(a,b)$ in the **list order of (5)** put
$z_e^2=ab/((r+a)(r+b))$. In the table below, the displayed integer
vector divided by $d$ defines the entire vector $(q_e)$.
An upper row certifies $q_e^2-z_e^2>0$ for every edge; a lower row
certifies $z_e^2-q_e^2>0$. All entries are positive. These are finite
rational comparisons, using (5) and the displayed formula for $z_e^2$.

| $(k,n)$ | $r$ | Direction | $d$ | Numerators of $(q_e)$, in order |
|---|---:|---|---:|---|
| $(1,7)$ | $6$ | upper | 100 | 28,27,34,37,37,41,43 |
| $(1,8)$ | $51/10$ | lower | 1000 | 316,466,307,390,428,414,462,487 |
| $(2,12)$ | $17$ | upper | 1000 | 209,204,236,257,270,276,250,274,291,301,306 |
| $(2,13)$ | $14$ | lower | 1000 | 245,348,240,278,304,320,330,291,320,340,353,361 |
| $(3,16)$ | $32$ | upper | 100 | 17,23,17,19,20,21,22,22,20,21,22,23,24,24 |
| $(3,17)$ | $32$ | lower | 100 | 17,16,18,20,21,22,22,22,19,21,22,23,24,24,24 |

For example, the first edge of the first row is $(1,7)$, giving
$(28/100)^2-1/13=12/8125>0$. An even row includes its central
edge as the second entry. The exact minimum square margin in each row is,
respectively,

$$
 \frac{43}{30000},\quad\frac{4333}{26270000},\quad
 \frac{32}{359375},\quad\frac{3}{32500},\quad
 \frac{23}{70000},\quad\frac{1}{5625}.
 \tag{19}
$$

For upper rows we use two elementary estimates. For $0<z<1/2$,

$$
 \arcsin z<\frac{z}{\sqrt{1-z^2}}<\frac{2z}{\sqrt3}<\frac65z.
 \tag{20}
$$

The first comparison integrates the strictly increasing derivative; the
last follows by squaring positive quantities. For $0<u\le1/3$,

$$
 (1+3u^2/5)^2(1-u^2)-1
 =\frac{u^2(5-21u^2-9u^4)}{25}>0.
$$

Indeed the parenthesis decreases as a function of $u^2$ and equals
$23/9>0$ at $u^2=1/9$. Taking positive square roots and
integrating proves

$$
 \arcsin z<z+z^3/5\quad(0<z\le1/3). \tag{21}
$$

For lower rows simply use $\arcsin z>z$ on $(0,1)$. The standard
strict bounds $3<\pi<22/7$ suffice: the lower bound follows from the
inscribed regular hexagon, and the upper has the elementary witness

$$
 \frac{22}7-\pi=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0,
$$

obtained by polynomial division and $\int_0^1dx/(1+x^2)=\pi/4$.
Thus every closure comparison has the following exact rational bound:

| $(k,n)$ | Bound on $C_{k,n}(r)/2=\sum_e\arcsin z_e$ | Strict comparison |
|---|---|---|
| $(1,7)$ | $<(6/5)\sum q_e=741/250$, all $q_e<1/2$ | $<3<\pi$ |
| $(1,8)$ | $>\sum q_e=327/100$ | $>22/7>\pi$ |
| $(2,12)$ | $<\sum(q_e+q_e^3/5)=1457520693/500000000$, all $q_e<1/3$ | $<3<\pi$ |
| $(2,13)$ | $>\sum q_e=373/100$ | $>22/7>\pi$ |
| $(3,16)$ | $<\sum(q_e+q_e^3/5)=14885133/5000000$, all $q_e<1/3$ | $<3<\pi$ |
| $(3,17)$ | $>\sum q_e=63/20$ | $>22/7>\pi$ |

Strict decrease of $C_{k,n}$ converts these to the root sides of (18).
Sections 6.1 and 6.2 therefore prove all six bridges without numerical
approximations to roots or transcendental functions.

### 6.3 Completing the integer ranges

For $k=1,2,3$, let $s$ be respectively $8,13,17$. The
two bridges for that $k$ give $D_{k,s-1}<0<D_{k,s}$. Strict
increase of $D_{k,n}$ on $n\ge4k+1$ supplies the same strict
signs throughout the respective earlier and later ranges. On
$k+2\le n\le4k$, section 5 already gives strict positivity of
$\Delta$. Equation (17) and the equivalence in section 4 now prove
the entire table in part 3. No integer lies between the two endpoints of
each bridge, so no equality case remains for these three $k$.

## 7. Journal corollary and non-implications

**Corollary for the finite paper.** The complete canonical cycle on
$\{1,\ldots,n\}$ is fully feasible at its chain root exactly for
$3\le n\le7$; its seam failure persists for every $n\ge8$.
The corresponding shifted orders beginning at 2 and 3 have first failures
at 13 and 17, with feasibility at every earlier admissible integer. For
each fixed positive integer $k$, its canonical necklace eventually
becomes and remains unrealizable at its chain root.

This is a fixed-order result. **Chain optimality** would additionally
compare $R_{\rm chain}(\sigma)$ over all cyclic orders. That separate
ordering theorem is neither a premise nor a conclusion of this proof.
**Full fixed-order optimization** allows all gaps but keeps the order;
section 4 identifies its radius only when the chain-root placement is
feasible. **Global optimization** compares the full problems for different
orders; for $\{1,\ldots,n\}$ its value is denoted $R^*(n)$.
This package does not determine it, nor any larger-radius optimizer after
seam failure.

In particular it proves no statement that a specified circle is strictly
slack against all other surrounding circles in some global optimum, or in
every global optimum. Those are distinct **floating-circle claims**.
Neither contact graphs, paid-then-free regimes, the number of floating
circles, nor an indefinite global cascade follows from this seam theorem.
No result for arbitrary radius sequences or global asymptotics is asserted.

## 8. Transposition, provenance and independent checks

For a journal appendix, transpose sections 1-6 in their present logical
order and retain the rational tables. The main text needs only the
corollary and the scope distinctions in section 7. The generic phrase
“fixed-order seam classification” should identify the general criterion
and the three explicit classifications; it should not imply an explicit
all-k onset formula in this appendix. All definitions, finite inequalities
and their analytic justification are contained here. No code execution or
mutable repository proof note is needed to complete the proof.

The development sources are
[the full-feasibility note](SUPNICK_FULL_FEASIBILITY.md),
[the fixed-k note](FIXED_K_SUPNICK_SEAM.md), and the
[radius-1](RADIUS1_SEAM_OBSTRUCTION.md),
[radius-2](RADIUS2_SEAM_THRESHOLD.md), and
[radius-3](RADIUS3_SEAM_ONSET.md) notes. They remain unchanged provenance,
not mathematical dependencies of this package. The stronger explicit
all-k onset formula in [the sequence note](SUPNICK_SEAM_SEQUENCES.md)
is deliberately outside the selected journal theorem.

The [task dossier](../ops/TASK-20260919__journal_fixed_order_seam/EVIDENCE.md)
records the A/B editorial comparison and an independent bounded checker.
The checker differentiates the original kernel symbolically, checks the
positive-branch algebra, compares rank cycles with both parity edge sets,
audits the new root-growth matching and the fan cancellation, and verifies
every rational table entry. A separate rational arctangent method encloses
closure values and all directed pair slacks at selected small and boundary
roots. These checks support transcription and falsification; the all-k
proof is the analytic argument above. Independent STRICT review remains
pending. Public arXiv sources and numerical certificates are unchanged.
