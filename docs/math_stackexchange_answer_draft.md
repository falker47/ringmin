# Draft answer

*Disclosure: I am the author of the paper described at the end of this answer. The question led me to study the problem in detail.*

There are really two problems here, and they agree only while a certain necklace is geometrically realizable.

1. In the **chain problem**, every circle is tangent to the central circle and to its two neighbors in a cyclic order. Dan's proposed “pyramid” order is optimal for this problem.
2. In the **full geometric problem**, every pair of surrounding circles must be non-overlapping, whether or not the pair is consecutive in the chosen order. At $n=8$, the optimal configuration is no longer an all-adjacent chain: the smallest circle becomes a *floating circle*, tangent to the central circle but not to another surrounding circle. That phenomenon continues throughout the certified range.

Thus the pyramid arrangement gives the full optimum for $3\le n\le7$, and an unconditional lower bound thereafter. The full optima have been certified computationally for $3\le n\le14$. A closed-form answer for every $n$ remains open.

## Angular formulation

If two surrounding circles have radii $a$ and $b$, their centers are at distances $R+a$ and $R+b$ from the center of the middle circle. The law of cosines shows that they do not overlap exactly when their smaller angular separation is at least

\[
\theta_R(a,b)
=2\arcsin\sqrt{\frac{ab}{(R+a)(R+b)}}.
\]

For a cyclic order $\sigma=(\sigma_1,\ldots,\sigma_n)$, forcing every consecutive pair to be tangent gives the closure equation

\[
\sum_{i=1}^n \theta_R(\sigma_i,\sigma_{i+1})=2\pi,
\qquad \sigma_{n+1}=\sigma_1.
\]

Call its unique solution $R_{\rm chain}(\sigma)$. Even when the corresponding necklace is not realizable, this is still a lower bound for every feasible placement having that cyclic order: the actual consecutive gaps must sum to $2\pi$ and each is at least the corresponding $\theta_R$.

## Why the pyramid order appears: anti-Monge and Supnick

For each fixed $R>0$, order the radii increasingly. The angular-cost matrix is strictly anti-Monge:

\[
\theta_R(a,b)+\theta_R(a',b')
>
\theta_R(a,b')+\theta_R(a',b)
\quad(a<a',\ b<b').
\]

There is a short reason for this. Put

\[
t_x=\sqrt{\frac{x}{R+x}},
\qquad
\theta_R(a,b)=2\arcsin(t_a t_b).
\]

For $f(x,y)=\arcsin(xy)$,

\[
\frac{\partial^2 f}{\partial x\,\partial y}
=\frac{1}{(1-x^2y^2)^{3/2}}>0,
\]

so $f$ is strictly supermodular, which gives the displayed anti-Monge inequality after the increasing substitutions $x=t_a,\ y=t_b$.

This puts the chain-ordering problem in a classical special case of the traveling-salesman problem. Supnick's theorem gives a fixed tour minimizing the total angular cost, independently of the numerical entries and therefore independently of $R$. Up to cyclic rotation and reversal, it is

\[
\sigma^*=\langle 1,n-1,3,n-3,5,n-5,\ldots,n-2,2,n\rangle,
\]

with the middle terms continued without repetition. For example, at $n=10$ one representative is

\[
(10,1,9,3,7,5,6,4,8,2).
\]

This is the proposed pyramid order. Since the same order minimizes the angular sum for every $R$, a self-consistency argument shows that it also minimizes $R_{\rm chain}$. Consequently

\[
R^*(n)\ge R_{\rm chain}(\sigma^*)
\]

for the full problem. If the necklace at that radius satisfies *all* pairwise non-overlap constraints, equality holds and it is a global optimum. This last condition is valid for $3\le n\le7$.

## Why the all-adjacent chain first breaks at $n=8$

In the full Supnick tour, circle $1$ lies between circles $n$ and $n-1$. If all three consecutive contacts are imposed, the angular separation between the centers of the two large circles along that arc is

\[
\theta_R(n,1)+\theta_R(1,n-1).
\]

But circles $n$ and $n-1$ themselves require separation at least $\theta_R(n,n-1)$. At the chain radius, the necessary condition is therefore

\[
\theta_R(n,1)+\theta_R(1,n-1)
\ge \theta_R(n,n-1).
\]

It holds through $n=7$, but at $n=8$ the inequality reverses (the deficit is about $0.0271$ radians). Thus the two large circles would overlap: the formal solution of the adjacent-contact closure equation is not a physical configuration.

The remedy is not simply another all-adjacent permutation. Circle $1$ leaves the load-bearing necklace and can sit in a gap while remaining tangent only to the central circle; a pair of larger circles is then effectively adjacent across it. For $n=8,9$, the necklace on $\{2,\ldots,n\}$ must be distorted slightly to open a pocket large enough for circle $1$. For $n=10,11,12$, its Supnick necklace already has such a pocket, so circle $1$ fits without increasing that reduced chain radius. At $n=13$, the same seam obstruction begins to affect circle $2$; at $n=14$, both circles $1$ and $2$ float in a certified optimum.

This is why optimizing only the closure sum is insufficient after $n=7$: nonconsecutive constraints can be the binding constraints.

## Certified finite answer

Here are representative optimal cyclic orders. Orders differing by rotation or reflection are equivalent. For a floating circle, its displayed position is only one possible hosting gap; it is not tangent to its displayed neighbors.

| $n$ | certified $R^*(n)$ | one representative angular order | floating radii |
|---:|---:|:---|:---|
| 3 | 0.260869565217 | (3, 1, 2) | none |
| 4 | 0.844453589561 | (4, 1, 3, 2) | none |
| 5 | 1.695494081203 | (5, 1, 4, 3, 2) | none |
| 6 | 2.794919518897 | (6, 1, 5, 3, 4, 2) | none |
| 7 | 4.153189553744 | (7, 1, 6, 3, 4, 5, 2) | none |
| 8 | 5.767794284590 | (8, 1, 6, 4, 5, 3, 7, 2) | $\{1\}$ |
| 9 | 7.726726552611 | (9, 2, 8, 1, 5, 6, 4, 7, 3) | $\{1\}$ |
| 10 | 9.979907385863 | (10, 2, 9, 4, 7, 1, 6, 5, 8, 3) | $\{1\}$ |
| 11 | 12.488720487188 | (11, 2, 10, 4, 8, 6, 7, 1, 5, 9, 3) | $\{1\}$ |
| 12 | 15.258870430448 | (12, 2, 11, 4, 9, 6, 7, 8, 5, 1, 10, 3) | $\{1\}$ |
| 13 | 18.317563047217 | (13, 3, 1, 12, 2, 10, 6, 8, 7, 9, 5, 11, 4) | $\{1\}$ |
| 14 | 21.665395182215 | (14, 3, 13, 2, 9, 8, 7, 10, 6, 11, 5, 1, 12, 4) | $\{1,2\}$ |

The certification treats the full pairwise problem. For a fixed order and $R$, unrolling the angular coordinates turns every pairwise separation requirement into two difference constraints, i.e. a simple temporal network; feasibility is checked by detecting negative cycles. A branch-and-bound search covers all cyclic orders, using chain radii of the full and induced orders as lower bounds. The saved frontier certificates are then rechecked by a separate 50-decimal-digit verifier. Global optimality is certified with an absolute guard of $10^{-10}$ in $R$; the displayed binding configurations were also checked at high precision.

## What is proved, computed, and still open

- **Proved analytically:** the angular reformulation; the strict anti-Monge property; the Supnick/pyramid order for the chain problem (in fact for arbitrary distinct positive radii, not only $1,2,\ldots,n$); the resulting unconditional lower bound; and global optimality whenever that necklace is realizable.
- **Certified computation:** the full pairwise optima and floating sets in the table for $3\le n\le14$, including the first breakdown at $n=8$ and the second floater at $n=14$.
- **Heuristic evidence:** non-exhaustive searches for $15\le n\le18$ suggest that the floating-circle mechanism continues, but those values are not certified optima.
- **Conjectural:** that this cascade persists for arbitrarily large $n$, and that
  \[
  R^*(n)=\frac{n^2}{8}(1+o(1)).
  \]

So the general answer is not “always use one tangent pyramid necklace.” The rigorous organizing principle is the Supnick/anti-Monge pyramid tour, but geometric realizability decides when that chain is attainable; after the first failure, floating circles and all-pairs angular constraints must be included.

Full proofs and details are in [the arXiv paper](https://arxiv.org/abs/2607.28654). The [source code, independent verifier, and certificate artifacts](https://github.com/falker47/ringmin) are also public.
