# A profile limit for minimum central circles

**Status.** The theorems and corollaries below have written proofs, independent review pending. This note starts from the all-pairs line model in §§2–4 of [Paper II, arXiv:2609.13630v3](https://arxiv.org/abs/2609.13630v3). Its finite checks and numerical observations are documented in the [companion package](../paper_assets/paper_ii_profiles/ADVERSARIAL_REVIEW.md).

## 1. A finite geometric comparison

**Definitions.** Fix $n\ge3$, $N_n>0$ and marks $0\le a_i\le M<\infty$. Let $R^*(N_na)$ be the infimum of central radii $R>0$ for externally tangent outer disks of radii $N_na_i$ with pairwise disjoint interiors, over all orders and placements. A zero mark denotes a point of radius zero and imposes no pair constraint. For a word $w$, let $\ell(w)$ be the least span of nondecreasing coordinates satisfying $x_j-x_i\ge\sqrt{w_iw_j}$ whenever $j>i$. Write $b(a)=\min_w\ell(w)$ over permutations of the multiset. The fixed-word recurrence starts at zero and places each new point at the largest predecessor coordinate plus the corresponding separation. Thus $\ell(w)$ is also the maximum edge sum along an increasing-index path from the first to the last vertex. This proves attainment, and permits zero marks and coincident coordinates. Deleting or decreasing marks preserves feasibility. Scaling marks and coordinates by the same positive factor preserves every inequality.

**Theorem 1 (exact theorem, written proof, independent review pending).** For every such array,
$$
 \frac{b(a)}{\pi n}-\frac{M}{n}
 \le \frac{R^*(N_na)}{N_n n}
 \le \frac{b(a)+M}{\pi n}.
$$
For profiles, take $a_i=f(i/n)$ and $b_n^f=b(a)$.

*Proof.* For $u=N_na_i,\ v=N_na_j$, both directed angle differences must be at least $\theta_R=2\arcsin\sqrt{uv/((R+u)(R+v))}$. Using $\arcsin z\ge z$ and the alternative expression $2\arctan\sqrt{uv/(R(R+u+v))}$ gives
$$
 2\sqrt{uv}/(R+N_nM)\le\theta_R\le2\sqrt{uv}/R .
$$
Multiply feasible angles by $(R+N_nM)/(2N_n)$. Cutting the resulting circle produces a line of span at most its circumference $\pi(R/N_n+M)$ meeting every mark separation. Take the infimum in $R$. Conversely, close a minimizing line placement with a gap $M$. The complementary arc of each pair contains this gap, while the forward arc is its original separation. Rescale this circumference $b+M$ to $2\pi$ and take $R=N_n(b+M)/\pi$. The upper angle inequality gives full feasibility for both arcs. When $M=0$ every positive central radius works. $\square$

## 2. Replication with genuine labels

**Lemma 2 (exact theorem, written proof, independent review pending).** Lists of marks can be matched with each target no larger than its assigned donor exactly when their equally long sorted lists satisfy coordinatewise domination. With a donor surplus, use the largest required number of donors.

*Proof.* Sorted matching suffices. If the $i$-th target exceeds the $i$-th of the top donors, there are more targets at least that large than available donors. $\square$

**Theorem 3 (exact theorem, written proof, independent review pending).** For every bounded nonnegative nondecreasing $f:(0,1]\to[0,M]$, with any common bound $M$, the limit
$$
 E(f)=\lim_{n\to\infty} b_n^f/n
     =\inf_{n\ge2}(b_n^f+M)/n
$$
exists. For $m\ge n\ge2$, $q=\lceil m/n\rceil$,
$$
 b_m^f\le q(b_n^f+M)-M.                                      \tag{1}
$$

*Proof.* Place $q$ copies of a minimizing $n$-template with gaps $M$. Every cross-copy requirement is at most $M$. Put $d=nq-m$, discard the $d$ smallest marks and sort the surviving labels. The $i$-th donor equals $f(\lceil(i+d)/q\rceil/n)$. Since $m(i+d)-nqi=d(m-i)\ge0$, its argument is at least $i/m$. Assign and decrease each donor to the corresponding target. Deleting points and retaining coordinates proves (1), including ties and jumps. For fixed $n$, $q/m\to1/n$, so $\limsup b_m^f/m\le(b_n^f+M)/n$. Equally spaced points bound $0\le b_n^f\le(n-1)M$. The infimum of the displayed finite ratios is at most their liminf, which is $\liminf b_n^f/n$. These inequalities give both equalities. $\square$

For $f(t)=t^p$, $p>0$, the smallest $m$ donors also work after multiplying marks and coordinates by $(nq/m)^p$, since $\lceil i/q\rceil/n\ge i/(nq)$. Keeping the largest $m$ proves (1) without rescaling and handles profiles with arbitrarily small positive marks. Lemma 2 gives the precise matching condition for this decrease-only argument.

## 3. Distributional stability

**Lemma 4 (exact theorem, written proof, independent review pending).** After any matching of $n$ marks of two arrays in $[0,M]$,
$$
 |b(a)-b(c)|\le2\sqrt M\sum_i |\sqrt{a_i}-\sqrt{c_i}|.
                                                               \tag{2}
$$
*Proof.* An edge cost is a product of two square roots. Its difference is bounded by $\sqrt M$ times the sum of their changes. A path uses each vertex at most twice as an endpoint. Comparing longest paths in a fixed order and using an optimal order in each direction proves (2). $\square$

**Theorem 5 (exact theorem, written proof, independent review pending).** Suppose the empirical measures of bounded triangular arrays on $[0,M]$ converge weakly to $\mu$. Let $Q_\mu(t)=\inf\{x:\mu([0,x])\ge t\}$ for $0<t\le1$. Then the normalized line span tends to $E(Q_\mu)$, and $R^*(N_na)/(N_n n)\to E(Q_\mu)/\pi$ for every sequence $N_n>0$. In particular $E(f)=E(Q_\mu)$ if grid samples of $f$ have limit law $\mu$. For bounded Riemann-integrable $f$, this law is that of $f(U)$ for $U$ uniform on $(0,1)$.

*Proof.* Match sorted square roots of the array to sorted $\sqrt{Q_\mu(i/n)}$. For two sorted lists, the mean absolute difference equals the integral, from 0 to $\sqrt M$, of the absolute difference of their empirical distribution functions. Indeed integrating the number of unequal threshold indicators counts every intervening interval once because sorted matching makes the differing indicators have the same sign at each threshold. The quantile sample has distribution function within $1/n$ of that of $\sqrt{Q_\mu(U)}$, since its count at $s$ is $\lfloor n\mu([0,s^2])\rfloor$. The other distribution functions converge at every continuity point by weak convergence. The exceptional jump set is countable, and dominated convergence makes the integral tend to zero. Apply (2), Theorem 3 and Theorem 1. If $f$ is bounded Riemann integrable (extend at $0$ arbitrarily), every continuous test function composed with $f$ is Riemann integrable. Its equally spaced right-endpoint sums give the claimed weak convergence. $\square$

**Corollaries (proved corollaries, written proof, independent review pending).** Write $E(\mu)=E(Q_\mu)$. Then $E(c f)=cE(f)$ for $c\ge0$ and $E$ is monotone under pointwise profile domination or sorted quantile domination, by the corresponding finite properties. For laws supported in $[0,M]$,
$$
 |E(\mu)-E(\nu)|\le
 2\sqrt M\int_0^1|\sqrt{Q_\mu(t)}-\sqrt{Q_\nu(t)}|\,dt .
$$
Apply (2) to quantile samples and pass to Riemann integrals of bounded functions with at most countably many discontinuities. For two sampled profiles with existing limits the right side of (2), divided by $n$, is also bounded by $2\sqrt M\|\sqrt f-\sqrt g\|_\infty$. If $\mu((0,M])>0$, select $s>0$ with positive mass in $[s,M]$. In a quantile sample these marks have limiting positive frequency, and consecutive selected points have separation at least $s$. Thus $E(\mu)>0$. For $f=1$, $b_n=n-1$, $E=1$, and equal angle spacing realizes the minimum $R^*(N_n{\bf1})=N_n(\csc(\pi/n)-1)$. Summing the $n$ equal adjacent angular requirements proves the matching lower bound.

A bounded measurable function can violate the sampling condition, and the infimum identity for a monotone representative need not hold for a particular nonmonotone representative. Explicit counterexamples appear in the [adversarial review](../paper_assets/paper_ii_profiles/ADVERSARIAL_REVIEW.md).

## 4. Finite words for any limit law

**Theorem 6 (exact theorem, written proof, independent review pending).** Write $Q=Q_\mu$, $Q(0)=0$ and $v_j=Q(j/k)$. For $k\ge1,\ r\ge2$, take all length-$r$ words on the $k$ *indexed* types (equal values may have different indices). Let $c_j(w)$ count index $j$ and use the actual mark values for $\ell(w)$. Define
$$
 \lambda_{k,r}=\min \sum_w p_w\ell(w)/r,\qquad
 p_w\ge0,\quad\sum_w p_w=1,\quad\sum_w p_wc_j(w)=r/k.
$$
Then
$$
 \lambda_{k,r}-M/k\le E(\mu)\le\lambda_{k,r}+M/r.
$$
In particular, for $f(t)=t^p,\ p>0$, $v_j=(j/k)^p$ and the ring-constant bracket has width $(1/k+1/r)/\pi$.

*Proof.* Let $e_k$ be the limiting span per mark for $q$ copies of each upper type as $q\to\infty$, and $e_k^-$ for the types $Q((j-1)/k)$. Both limits exist by Theorem 5 for the corresponding discrete laws. The $kq$ monotone quantile samples sit between the lower and upper arrays, sorted. These type lists share the middle $k-1$ indexed types. Delete the extra zeros from the lower array, then add the $q$ top marks in one block. Each added mark costs at most $M$, including the first join. The same upper bound applies to an empty common part. Consequently $e_k-M/k\le E(\mu)\le e_k$.

Partition an optimal upper-type word into successive pieces of $r$ vertices. The sum of their spans is at most the total span, and each is at least its word minimum. Fewer than $r$ remaining vertices affect limiting type frequencies by zero. Along a convergent subsequence of piece distributions, the equal proportions enforce all LP constraints. This gives $\lambda_{k,r}\le e_k$. Conversely the nonempty finite polytope (mix constant words uniformly) has rational vertices, since its constraints are rational, regardless of the real costs. A minimizing vertex with common denominator $D$ yields a batch of $D$ words, exactly $Dr/k$ copies of each type. Repeating the batch with gaps $M$ bounds $e_k\le\lambda_{k,r}+M/r$. $\square$

Computational interpretation requires access to the $v_j$ or rigorous enclosures for them. If all edge costs have directed enclosures of width $\epsilon$, each length-$r$ path has at most $r-1$ edges, giving additional LP-width at most $(r-1)\epsilon/r$. Computable quantile values suffice for numerical evaluation.

## 5. Power radii and an adjacent-pair lower bound

**Corollary 7 (proved corollary, written proof, independent review pending).** For every fixed real $p>0$, take $N_n=n^p$ and $f(t)=t^p$. Then
$$
 R_p^*(n)=C_p n^{p+1}+o(n^{p+1}),\qquad
 C_p=E(t^p)/\pi .
$$
For $p=1$ this agrees with Paper II. For $p=2$ it proves convergence in the quadratic problem. Combining the theorem with the lower and upper bounds already proved at [Ringmin-squared, pinned revision](https://github.com/falker47/ringmin-squared/blob/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b/research/ALL_N_LOWER_BOUND.md) gives
$$
 (434+4\sqrt2)/(1587\pi)\le C_2\le857/(3000\pi).
$$
The endpoints come from the cited project. The new deduction is that they enclose one limit.

**Corollary 8 (proved corollary, written proof, independent review pending).** For any law on $[0,M]$,
$$
 E(\mu)\ge\int_0^1\sqrt{Q_\mu(t)Q_\mu(1-t)}\,dt .
$$
Indeed the successor map in a cyclic order permutes the $n$ sorted square roots $s_i$. The rearrangement inequality gives a cyclic product sum at least $\sum_i s_i s_{n+1-i}$ (exchanging similarly sorted pairs lowers the product sum). Closing a line order adds a product at most $M$. Thus every line span exceeds or equals this sum minus $M$. Use quantile samples and dominated convergence, pairing $i/n$ with $(n+1-i)/n$. Both arguments converge at almost every quantile continuity point. For positive distinct radii the angular adjacent-chain minimizer is the Supnick order from [Paper I, §3](https://arxiv.org/abs/2607.28654v4). The argument here only needs a lower bound on the cyclic sum and also covers ties. For $p=1$ the integral is $\pi/8$, yielding $C_1\ge1/8$. For $p=2$ it is $1/6$, yielding $C_2\ge1/(6\pi)$.
