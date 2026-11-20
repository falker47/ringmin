# Adversarial review of the profile argument

The [proof note](../../research/PROFILE_GENERALIZATION.md) is authoritative. This is an internal proof audit with independent finite arithmetic. The written theorems await independent mathematical review.

## Hypotheses and failure tests

| Step | Failure tested | Resolution or counterexample |
| --- | --- | --- |
| All-pairs squeeze | Cutting a ring could lose a complementary arc. Closing a line could create a new crossing at the seam. | Both original arcs obey the pair angle. On closing, each complementary arc contains the single gap $M\ge\sqrt{a_i a_j}$. With two unit marks and a candidate zero closing gap, the complementary separation is zero. |
| Scaling | Treating $N_n$ as the number of vertices, as an integer, or as a fixed power changes units. | The lower comparison multiplies angles by $(R+N_nM)/(2N_n)$. The upper comparison gives the *unscaled* radius $N_n(b+M)/\pi$. All manipulations use only $N_n>0$. The choices $N_n=1/2$ and $N_n=\sqrt n$ give the same normalized inequalities. A null scale makes the normalization undefined. |
| Zero and tiny marks | Division by a small $f(i/n)$ fails when $f(0+)=0$, when a whole interval maps to zero or when every mark vanishes. | The donor proof uses rank comparisons and the stability proof uses square roots and products. Zero marks permit coincident points. The all-zero list has $b=R^*=0$. No positive minimum is required. |
| Genuine-label transfer | Keeping the smallest $m$ donors without a dilation can fail. | For $n=2,m=3$, take $f=0$ on $(0,1/2]$, $f=1$ above. The smallest three replicated donors are $0,0,1$ and the targets are $0,1,1$. No finite dilation repairs the second zero. Keeping the largest three gives $0,1,1$. For powers, dilating the smallest donors by $(nq/m)^p$ also works. |
| Jumps, ties and parity | Continuous approximation or blocks of exactly divisible size could leave out labels at jumps or odd sizes. | $m(i+d)-nqi=d(m-i)$ is exact, including equality at the largest label, for every $m\ge n$. Break donor ties arbitrarily and retain the coordinates. The matching checker tests every assignment on a finite alphabet, including zeros, ties and donor surpluses. |
| Nonmonotone profiles and maximum location | $f(1)$ might vanish despite a positive interior maximum. Unsorted input values can invalidate endpoint matching. | For $f(t)=1-t$, $M=1$ works and the sampled law converges to the uniform law. Use a common upper bound over all marks and sort before comparison. The empirical-law theorem covers continuous nonmonotone and bounded Riemann-integrable profiles. |
| Infimum formula | The finite-template infimum of a particular nonmonotone representative can differ from its limit. | Let $f=1$ except $f(1/2)=f(1)=1/4$. The Riemann-integrable profile has limit $E=1$ while its $n=2$ template gives $(1/4+1)/2=5/8$. Use the quantile representative in the infimum. |
| Sampling a measurable profile | Lebesgue-equivalent profiles may disagree on every grid and generate divergent subsequences. | For the rational indicator, $f(U)=0$ almost surely, but all sampled marks equal one. More strongly, set $f$ to one on reduced rationals with even denominator and zero elsewhere. Odd prime grid sizes give only zeros. At $n=2^j$, all but the endpoint are ones, hence $b_n=n-2$. These subsequences have different normalized limits. |
| Uniform mark bound | Weak convergence alone can hide a few marks of unbounded size. | Take three marks equal to $n$ and all remaining marks zero. The empirical laws tend to the point mass at zero. Their spans are $2n$, and at scale $N_n=1$ the three equal positive disks require $R=n(\csc(\pi/3)-1)$. Uniform boundedness in both squeeze and stability matters. |
| Change of marks | A small fraction of extreme ranks near an atom can destroy sup-norm matching. | Inequality (2) sums errors over vertices. Every path uses each vertex in at most two edges. For sorted matching the normalized error is an integral of distribution-function differences. The argument is unaffected by jumps or a vanishing fraction of mismatches on bounded support. |
| Finite words | Repeated quantile values can collapse LP count constraints. A real-cost optimum may give unrealizable counts. | Symbols retain their indices. Constraints are rational even for irrational costs, so the optimal face contains a rational vertex. An integer batch realizes its word counts. The $M/r$ term pays the cross-word gap. For $k=1$ or all types equal, the same construction applies. Evaluation for noncomputable data requires an additional oracle assumption. |
| Chain versus full feasibility | Minimizing adjacent products can ignore a long-range constraint. | The rearrangement argument gives a one-sided lower bound since every feasible line placement separates adjacent points too. The upper recovery used the full line constraints. |
| Quadratic inference | A small table of square radii or a good order at $n=512$ might be mistaken for proof of convergence or the value of $C_2$. | Apply the distributional theorem with $N_n=n^2$. Only then combine the existing liminf/limsup bounds to enclose one limit. Neither the exact value nor an optimal order follows here. |

## Independent finite checks

Classification is **independently reproduced finite result** for the arithmetic assertions in this section. The standard-library checker imports neither the numerical search nor the project solver. It enumerates every ordering and every increasing path for $2\le n\le7$ at $p=0,1/2,1,2,3$ where used. For $p=0,2$ the chosen denominator represents the weights exactly. For other exponents it bounds each scaled edge between adjacent integers with integer square or fourth roots. Path and order bounds use the same directed endpoints throughout.

The check covers 754 small matching problems, 70 inequalities relating two genuinely different grid sizes, and 480 reconstructed concatenations checked pair by pair by integer powers. Another 225 comparisons test square-root stability. Twelve small balanced-word comparisons use exact rational primal/dual values for two types and length-two words. Their rational dual inequalities cover every word.

For $p=1$, all twelve Paper I brackets from $n=3$ to 14 lie inside the squeeze. For $p=2$, all four cited quadratic brackets from $n=3$ to 6 lie inside it. Up to seven labels the comparison uses the exhaustive span. For larger linear instances, the checker sandwiches the unknown span between the reverse-pair lower bound minus the closing edge and the ascending-word span. A Machin alternating-series interval for $\pi$ keeps all endpoint comparisons rational. The external source check compares every exact decimal with Paper I's arXiv table or the pinned quadratic JSON. This verifies consistency with the stated brackets. Their original proofs and guarded interval-backend assumptions retain their original scope.

## Numerical observations at 512 labels

The search starts from interleaved increasing half-words, tests 64 shifts at $n=512$, and considers 16,000 seeded pair swaps per nonconstant profile, retaining strict improvements. The scores in the table are $(\ell(w)+1)/(\pi n)$ for the best word found. They estimate the optimized finite expression from above. A separately implemented integer recurrence using all predecessors encloses each word's score and verifies the displayed rounding. Optimality of the words is open except for the constant profile.

| Power $p$ | Seed | Word score, rounded to ten decimals |
| ---: | ---: | ---: |
| 0 | 20261119 | 0.3183098862 |
| $1/2$ | 20261120 | 0.1999947376 |
| 1 | 20261121 | 0.1413183229 |
| 2 | 20261122 | 0.0889945783 |
| 3 | 20261123 | 0.0651515025 |

The linear observation exceeds Paper II's proved lower endpoint, approximately $0.14056946887766$. That paper also gives the independent upper construction $U_4$. The quadratic observation lies between the previous lower and upper coefficients $(434+4\sqrt2)/(1587\pi)$ and $857/(3000\pi)$. The comparison uses the finite-template upper direction in both cases. Ten-decimal values in this table are nearest roundings.

From the repository root, use any writable temporary location for the orders. The second command also checks the source versions prepared by the prompt.

~~~sh
python -I -S paper_assets/paper_ii_profiles/checks/observe.py --n 512 --moves 16000 --seed 20261119 --output orders.json
python -I -S paper_assets/paper_ii_profiles/checks/verify_finite.py --sources .codex_inputs --observations orders.json
python -m pytest tests/test_profile_generalization.py
~~~

Without an orders file or prepared external sources, the verifier still runs its exhaustive comparisons and the 16 bracket tests on the recorded endpoint data.
