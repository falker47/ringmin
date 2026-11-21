# Referee check of the square-radius lower bound

**Verdict: CONFIRMED.** For the infimum central radius with outer radii
$1^2,\ldots,n^2$, the pinned proof establishes

$$
\liminf_{n\to\infty}\frac{R_2^*(n)}{n^3}
\ \ge\ \frac{434+4\sqrt2}{1587\pi}
=0.0881834424928036317\ldots .
$$

The inequality covers all integer sizes. Paper II proves that this same
sequence converges to $C_2$ and supplies the strict upper bound
$C_2<0.088581212993$. The external result supplies the lower endpoint of
this comparison. Neither endpoint is asserted to be sharp for the geometric
problem.

**Evidence and scope.** This STRICT review concerns the common **left**
endpoint of (22) and (23). Sections 1–7 below give a proof from the geometric
constraints through the two limiting arguments. Section 8 checks the
identification with Paper II and its upper witness. The checker uses standard
library integer and rational arithmetic, the vendored note, and the target
repository's square-radius upper certificate. All steps needed for the lower
bound are **proved**. There are no assumed intermediate research claims,
missing cases, or fixes. **Finite computation** is identified separately.
The upper constructions behind the external right endpoints $1/(2\pi)$
and $857/(3000\pi)$ are outside this verdict.
[Vendored statement](../../independent_check/p2_squared/source/ALL_N_LOWER_BOUND.md#L2791-L2837) ·
[Source identity](../../independent_check/p2_squared/source/PIN.txt)

## 1. Feasibility gives a product budget for every induced cycle — proved

Fix $n\ge3$ and any placement at radius $R$ with all outer disks externally
tangent to the central circle and pairwise disjoint in their interiors.
The objective is the infimum over such $R$ and over every cyclic order.
Radius zero would require every two center directions to be opposite, which
is impossible for three positive radii. At sufficiently large $R$, equally
spaced directions are feasible, since every required pair angle tends to zero.

For labels $u,v$, external tangency fixes the center distances from the origin
at $R+u^2,R+v^2$. For either oriented angular gap $d\in(0,2\pi)$,
the cosine law writes squared center distance as
$(u^2-v^2)^2+4(R+u^2)(R+v^2)\sin^2(d/2)$. Non-overlap requires this
to be at least $(u^2+v^2)^2$. Consequently

$$
 d\ \ge\ 2\sin(d/2)\ \ge\
 \frac{2uv}{\sqrt{(R+u^2)(R+v^2)}}\ \ge\ \frac{2uv}{R+n^2}.
$$

This also covers a gap larger than $\pi$. Retain any subset with at least
three labels in its induced circular order $D$. Its consecutive clockwise
gaps, including the closing gap, sum to $2\pi$. Writing
$P(D)=\sum_{\{u,v\}\in E(D)}uv$, summation gives

$$
P(D)\le\pi(R+n^2). \tag{A}
$$

Every induced cycle has this budget in the **same** placement. Deletion
just selects gaps between surviving directions. It requires no reinsertion
theorem, rearrangement, or chain-feasibility assumption.
[Source definitions and induced gaps](../../independent_check/p2_squared/source/ALL_N_LOWER_BOUND.md#L559-L805)

**Connection to the source's cyclic ratio.** Sort positions in increasing
angle $\phi$. For a directed step $a\to b$ take the angular length
$\phi_a-\phi_b+2\pi{\bf1}_{a<b}$. On any closed walk the lengths sum to
$2\pi q$, where $q$ counts ascending steps and is positive. The same pair
inequality gives $S(C)/q\le\pi(R+n^2)$, with $S(C)$ the sum of label products
counted with traversal multiplicity. A closed walk decomposes into simple
cycles, so its ratio is a weighted average of their ratios. This proves the
needed lower side $R_2^*(n)\ge\Lambda_n/\pi-n^2$ for the minimum over orders
of the maximum ratio. Traversing an induced tail in decreasing position
with one return step has $q=1$. Thus $\Lambda(\sigma)$ dominates each of
its tail scores. The source's $\gamma^{(r)}_{m,n}$ takes the minimum over
orders of the maximum score on the consecutive tails starting at $m$ through
$m+r-1$. Each such minimum is at most $\Lambda_n$. Maximizing these scalar
minima gives $\Lambda_n\ge\Gamma_n^{(r)}\ge\gamma^{(r)}_{1,n}$.
Equation (A) will let us use the same tail scores directly.
[Pinned cyclic-ratio definitions](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/FIXED_ORDER_CYCLE_RATIO.md#L909-L1099) ·
[Pinned tail-block definitions](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/FIXED_ORDER_CYCLE_RATIO.md#L1956-L2061)

## 2. Tail score and the cost of inserting a label — proved

Fix $2\le r\le n-2$. Write $D_t$ for the cycle induced on labels
$t,\ldots,n$ and $S=n+r$. The base cycle $D_r$ has $q=n-r+1\ge3$
edges. Its score exceeds the reference sum

$$
P_{r,n}=\sum_{x=r}^n x(S-x)
=\frac{(n-r+1)(r^2+4rn+r+n^2-n)}6
$$

by exactly $\sum_{e\in E(D_r)}\Delta_e$, where
$\Delta_{\{u,v\}}=(u+v-S)^2/2$. Indeed,
$\sum_{x=r}^n x=qS/2$, and in the expansion of the edge squares each
vertex occurs twice. This gives
$\sum_e\Delta_e=P(D_r)+\sum_{x=r}^n x^2-qS^2/2$.
The displayed polynomial follows by summing $x$ and $x^2$. The reference
sum need not itself be the score of a realizable base cycle.

Reinsert labels $t=r-1,r-2,\ldots$ in their original positions. In passing
from $D_{t+1}$ to $D_t$, the single edge between the neighboring surviving
labels $u,v>t$ becomes two edges. Its signed increment is

$$
A_t=t(u+v)-uv=t^2-(u-t)(v-t).
$$

Deleting $t$ reverses this operation. In particular, every order gives a
compatible sequence, including insertions across the closing edge. The proof
works for this one sequence of nested cycles associated to the order.
[Pinned base identity and local estimates](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/FIXED_ORDER_CYCLE_RATIO.md#L2272-L2396)

## 3. Each split has a lower estimate and each base edge pays once — proved

Take $0\le\lambda\le1$ and set

$$
G_\lambda(t)=\frac{\lambda(4St-S^2-2\lambda t^2)}{2(2-\lambda)}.
$$

If the split uses an original edge, put $w=u+v$. Completing a square gives

$$
\Delta_{\{u,v\}}+\lambda A_t-G_\lambda(t)
=\frac{\lambda(u-v)^2}{4}
 +\frac{2-\lambda}{4}
  \left(w-\frac{2(S-\lambda t)}{2-\lambda}\right)^2\ge0 .
$$

If the split uses a later edge, at least one endpoint belongs to
$\{t+1,\ldots,r-1\}$. Initially every edge is original. After each split the
new edges both carry the just-inserted label, and all other edges retain
their endpoints. This inductive argument includes the case in which both
endpoints were previously inserted. Hence
$A_t\ge t^2-(r-1-t)(n-t)=(S-1)t-n(r-1)$. With
$J_\lambda(t)=\lambda((S-1)t-n(r-1))$, direct subtraction gives

$$
J_\lambda(t)-G_\lambda(t)=
\frac{\lambda\big((n-r)^2+4(n-t)+2\lambda(r-1-t)(n-t)\big)}
     {2(2-\lambda)}\ge0 .
$$

Finally $G_\lambda(t+1)-G_\lambda(t)=
\lambda[2S-\lambda(2t+1)]/(2-\lambda)\ge0$ for $t\le r-1$.
The denominator stays positive, including at $\lambda=1$, and the estimates
hold at $\lambda=0$. An original edge disappears at its first split. All
new edges have a low endpoint, so later splits cannot charge that original
edge a second time.

## 4. A finite inequality valid simultaneously on any chosen prefixes — proved

Take any finite $k\ge1$ and integers $1\le s_k<\cdots<s_1\le r-1$.
Put $s_0=r$ and $1\ge\lambda_1\ge\cdots\ge\lambda_k\ge\lambda_{k+1}=0$.
Write $H_0=0$ and $H_i=\sum_{t=s_i}^{r-1}A_t$. The selected scores are
$P(D_r)+H_i$. The weights $1-\lambda_1,\lambda_1-\lambda_2,\ldots,
\lambda_k$ are nonnegative and sum to one. Their weighted score is bounded
by the largest selected score. Telescoping writes the weighted score as

$$
P(D_r)+\sum_{i=1}^k\lambda_i\sum_{t=s_i}^{s_{i-1}-1}A_t .
$$

In segment $i$, Section 3 gives at least $G_{\lambda_i}(s_i)$ per split
after charging its unique original-edge slack if applicable. All unused
slacks are nonnegative. There are exactly $s_{i-1}-s_i$ splits in this
segment. Equation (A) and the infimum over all full placements now give

$$
\pi\big(R_2^*(n)+n^2\big)\ \ge\
P_{r,n}+\sum_{i=1}^k (s_{i-1}-s_i)G_{\lambda_i}(s_i). \tag{B}
$$

This uses signed increments and the original maximum over prefixes. It
allows a negative local floor. The argument covers $k=1$, equal successive
weights, and the smallest base cycle of three labels.
[Vendored finite statement](../../independent_check/p2_squared/source/ALL_N_LOWER_BOUND.md#L1682-L1747) ·
[Pinned charging proof, CR28dr–dw](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/FIXED_ORDER_CYCLE_RATIO.md#L5570-L5775)

## 5. Fix the densities first and let every integer size grow — proved

Fix $1/3<\alpha<1/2$, $s=1+\alpha$, $A=3\alpha-1>0$, and any strictly
ordered $1=x_0>x_1>\cdots>x_k>0$. Set

$$
\beta_0=\alpha,\qquad \beta_i=(s+Ax_i)/4,\qquad
\lambda_i=Ax_i/\beta_i=4-s/\beta_i .
$$

The same formula for $\beta$ at $x_0=1$ gives $\alpha$. All chosen cutoffs
satisfy $s/4<\beta_i<\alpha<s/3$ because $\alpha<1/2$. Thus
$0<\lambda_k<\cdots<\lambda_1<1$ and all cutoff spacings are positive.
Use $r=\lfloor\alpha n\rfloor$, $s_i=\lceil\beta_i n\rceil$.
For a concrete threshold let $\delta$ be the minimum of
$1-\alpha,\beta_k,\alpha-\beta_1$ and all successive $\beta_i-\beta_{i+1}$
(the latter list is empty for $k=1$). Whenever $n\delta>3$, the floor
and ceiling errors of less than one give all the integer conditions in (B).
This is a tail of the entire integer sequence, including both parities.

Divide (B) by $n^3$. Its base term tends to the Riemann integral
$p(\alpha)=\int_\alpha^1 x(1+\alpha-x)\,dx
=(1-\alpha)(\alpha^2+4\alpha+1)/6$.
For each of the fixed $k$ terms, the length divided by $n$ tends to
$\beta_{i-1}-\beta_i$, and $G_{\lambda_i}(s_i)/n^2$ tends to

$$
g(\alpha,\beta,\lambda)=
\frac{\lambda(4s\beta-s^2-2\lambda\beta^2)}{2(2-\lambda)}.
$$

Substituting $s=(4-\lambda)\beta$ cancels the factor $2-\lambda$ and
gives $g=(\lambda\beta)^2/2=A^2x_i^2/2$. Also
$\beta_{i-1}-\beta_i=A(x_{i-1}-x_i)/4$. Since the term $\pi n^2/n^3$
vanishes, the same scalar $L=\pi\liminf_n R_2^*(n)/n^3$ satisfies

$$
L\ \ge\ p(\alpha)+\frac{A^3}{8} F_k(x),\qquad
F_k(x)=\sum_{i=1}^k(x_{i-1}-x_i)x_i^2 . \tag{C}
$$

## 6. The prefix supremum is one third — proved in two ways

**Source route.** The polynomial $F_k$ attains a maximum $M_k$ on the
closed ordered simplex. At first coordinate $y$, scaling the remaining
coordinates by $y$ scales their contribution by $y^3$. With $M_0=0$,
the maximum therefore equals the maximum of $y^2-(1-M_{k-1})y^3$
on $[0,1]$. For $u=M_{k-1}<1/3$ the derivative
$y[2-3(1-u)y]$ changes sign at $y=2/[3(1-u)]\in(0,1)$.
The maximizing coordinates obtained successively by this scaling are
strictly interior and so are admissible in (C). Substitution gives
$M_k=T(u)=4/[27(1-u)^2]=y^2/3<1/3$. Moreover

$$
T(u)-u=\frac{(1-3u)^2(4-3u)}{27(1-u)^2}>0 \qquad(0\le u<1/3).
$$

The increasing sequence has a limit in $[0,1/3]$, where the only fixed
point of $T$ is $1/3$. This proves $M_k\uparrow1/3$.
[Pinned simplex lemma, CR28cr–cy](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/FIXED_ORDER_CYCLE_RATIO.md#L5347-L5482)

**Independent witness.** Every term of $F_k$ is a lower rectangle for the
integral of $x^2$ on $[0,1]$. For each fixed $k$, let
$x_i=1-i/(k+1)$. These strict coordinates give

$$
F_k=\frac{\sum_{j=1}^k j^2}{(k+1)^3}
=\frac{k(2k+1)}{6(k+1)^2}\ \longrightarrow\ \frac13 .
$$

Thus (C) yields $L\ge p(\alpha)+A^3/24$ along this explicit family as well.
The quantifiers are $\forall k\,\exists N_k\,\forall n\ge N_k$.
First take the liminf in $n$ at each fixed $k$. Each resulting number
bounds the **same** $L$ from below, so their supremum also bounds $L$
from below. No finite mesh attains the limiting integral. No uniform
rounding threshold or exchange of two limits is required.
[Vendored all-fixed-$k$ deduction](../../independent_check/p2_squared/source/ALL_N_LOWER_BOUND.md#L1854-L1945)

## 7. Evaluate the coefficient — proved, with finite arithmetic replay

The lower estimate at density $\alpha$ is

$$
H(\alpha)=p(\alpha)+(3\alpha-1)^3/24
=\frac{23\alpha^3-39\alpha^2+21\alpha+3}{24}.
$$

Its derivative is $(23\alpha^2-26\alpha+7)/8$. The roots are
$(13\pm2\sqrt2)/23$. Since $1<\sqrt2<3/2$, the smaller root
$\alpha_*=(13-2\sqrt2)/23$ lies in $(1/3,1/2)$ and the larger exceeds
$1/2$. The derivative changes from positive to negative at $\alpha_*$.
This optimization on the stated interval suffices for the lower bound.
Using $(\sqrt2)^2=2$ gives the following exact values.

| Quantity | Independent expression | Value at $\alpha_*$ |
|---|---|---|
| Tail contribution | $p(\alpha_*)$ | $(9038+722\sqrt2)/36501$ |
| Prefix contribution | $(3\alpha_*-1)^3/24$ | $(944-630\sqrt2)/36501$ |
| Product coefficient | $H(\alpha_*)$ | $(9982+92\sqrt2)/36501=(434+4\sqrt2)/1587$ |
| Radius coefficient | $H(\alpha_*)/\pi$ | $(434+4\sqrt2)/(1587\pi)$ |

Here $36501=23\cdot1587$. Combining Sections 1–7 proves the claimed
lower endpoint. The result determines a bound on the geometric optimum.
The optimization in this calculation is over parameters of the proof.

## 8. Paper II uses exactly this limit — proved

Paper II minimizes over all circular orders and all placements with
external tangency and disjoint interiors. Set $N_n=n^2$,
$a_{n,i}=(i/n)^2$, $M=1$. Then $N_na_{n,i}=i^2$ and $N_n n=n^3$.
The quantile of the limiting mark law is $Q(t)=t^2$ for $0<t\le1$.
For normalized marks $a,b$ the required line spacing is $\sqrt{ab}$,
which here is $ij/n^2$. If $b_n$ is the minimum line span, the angular
comparison and the replication lemma imply

$$
\frac{b_n}{\pi n}-\frac1n\le\frac{R_2^*(n)}{n^3}
\le\frac{b_n+1}{\pi n},\qquad
\lim_n\frac{b_n}{n}=\inf_{m\ge2}\frac{b_m+1}{m}.
$$

For the lower comparison, multiply the angular distances by
$(R+n^2)/(2n^2)$ and cut the circle to obtain a feasible line span at
most $\pi(R/n^2+1)$. Conversely, close a feasible line with a unit gap.
Each arc for a pair then has length at least its required mark spacing.
At $R=n^2(b_n+1)/\pi$ the angular scale suffices, since the required
angle is $2\arctan\sqrt{uv/[R(R+u+v)]}\le2\sqrt{uv}/R$ for physical
radii $u,v$.

For replication from $m$ marks to any $\ell\ge m$, take
$h=\lceil\ell/m\rceil$ copies of the optimal line with unit gaps and
delete the $d=hm-\ell$ smallest donors. The $i$th remaining quantile
argument $\lceil(i+d)/h\rceil/m$ is at least $i/\ell$, since
$\ell(i+d)-hmi=d(\ell-i)\ge0$. Reassignment to the target quantiles
can only decrease the required separations. This gives
$b_\ell\le h(b_m+1)-1$. Take $\limsup_\ell$ of the quotient by $\ell$
and then the infimum in $m$. The reverse inequality follows from
$\inf_m (b_m+1)/m\le\liminf_m b_m/m$. Thus Paper II supplies existence
of the limit and identifies $C_2=E(\mathrm{law}(U^2))/\pi
=\lim_n R_2^*(n)/n^3$. The factor $\pi$ has already converted the
product coefficient into the radius coefficient. No normalization mismatch
was found.
[Paper II geometry](../../paper_assets/journal_p2_sidma/main.tex#L104-L111) ·
[Comparison and replication](../../paper_assets/journal_p2_sidma/main.tex#L327-L387) ·
[Power-radius corollary and upper certificate](../../paper_assets/journal_p2_sidma/main.tex#L478-L522)

**Finite computation for the comparison.** For $m=3200$ the certificate
has $D=m^2$, integer positions $X_i$ indexed by label, and span numerator
$H=9{,}108{,}638{,}531$. The integer inequalities
$m^2|X_i-X_j|\ge Dij$ check the required separation for each of the
$m(m-1)/2=5{,}118{,}400$ pairs. Hence $b_m\le H/D$ and
$(H/D+1)/(\pi m)<0.088581212993$ supplies Paper II's upper endpoint.
[Upper witness](../../paper_assets/line_upper/certificates/p2_n03200.json) ·
[Printed ceiling](../../paper_assets/journal_p2_sidma/numbers.tex#L4)

## Reproduce offline

From the repository root run

~~~sh
python -I -S -B independent_check/p2_squared/check.py
~~~

The pinned source is the complete byte-for-byte Git blob
`ab21727593fe9acbc0a28fffc50ef2dcf2cc4d84` at external commit
`1d0a5dea10cd09783a9c0e2d54ede79b790cce2b`. The report compares it
with Paper II at `b70e280203b8261814de2eb669ed752b2b31a86c`.
On an isolated Python 3.14.3 run the checker reproduced the exact identities
for the edge split and checked all 360 cyclic orders on seven labels up to
rotation and reflection, each with two weight choices. It also replayed all
5,118,400 upper-witness pairs. The symbolic identities are checked by polynomial
coefficients or by exact interpolation on a grid exceeding the degree in each
variable. The small-order enumeration is a finite control on the combinatorial
argument in Sections 2–4.

For the decimal, the checker bounds $\sqrt2$ between two successive rationals
with denominator $10^{50}$ by integer squaring. For each arctangent in
$\pi=16\arctan(1/5)-4\arctan(1/239)$, consecutive alternating partial sums
enclose its value. Two tangent doublings give $5/12$ and $120/119$ from
$1/5$. Subtracting the angle with tangent $1/239$ gives tangent one in the
first quadrant, proving the identity. Dividing a positive lower numerator
by the upper bound for $\pi$, and vice versa, yields the outward enclosure

~~~text
[0.088183442492803631749528358531, 0.088183442492803631749528358532]
~~~

The mathematical argument and its inputs are available in this checkout.
The companion proof links are provenance for the source's named lemmas.
The script imports neither project's `src` and installs no packages.
The PR job executes it on the pull request's head commit.
[Checker](../../independent_check/p2_squared/check.py) ·
[PR workflow](../../.github/workflows/p2-squared-lower-bound.yml)
