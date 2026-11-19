# Finite line certificates for the Ringmin constant

For surrounding radii $1,\ldots,n$, the certificate at $n=3200$ gives
**$0.1405694688<C_*<0.140958576058$**. The lower endpoint rounds down the existing Paper II lower bound. The upper endpoint uses one feasible rational placement and Paper II's genuine-label concatenation theorem. This is a proved corollary of that theorem and a computer-certified finite witness.

A separate four-block construction with explicit rational parameters has cost in $[0.14191330499527,0.14191330499528]$. The line upper bound lies below this whole interval. It is also below the separate enclosure of the implicit published $U_4$ given below.

## Finite placements

A label $i$ has mark $(i/n)^p$. Write $S$ for the span of the displayed rational coordinates. Each entry in the table is a strict, independently checked upper bound $B$ on $(S+1)/(\pi n)$, rounded upward to twelve decimal places.

| $n$ | $p=1$ | $p=2$ |
|---:|---:|---:|
| 3 | 0.217379634673 | 0.176838825658 |
| 4 | 0.196232142276 | 0.149207759149 |
| 5 | 0.181386159486 | 0.134963391742 |
| 6 | 0.174163670568 | 0.126734491722 |
| 14 | 0.155076073460 | 0.103009904859 |
| 200 | 0.141787844501 | 0.089403618155 |
| 400 | 0.141331065055 | 0.088940099278 |
| 800 | 0.141112670212 | 0.088727754877 |
| 1600 | 0.141005256439 | 0.088615870196 |
| 3200 | **0.140958576058** | **0.088581212993** |

The file `p1_n03200.json` gives span $4531424532506678377/3200000000000000$.
The quadratic file at the same size gives $9108638531/10240000$. These are feasible spans. Optimality of the orders and equality with the least spans over all orders remain open.

### Search and exact reconstruction

For a fixed left-to-right word $w$, Paper II's recurrence sets the first coordinate to zero and each subsequent coordinate to the maximum of $x_j+\sqrt{w_iw_j}$ over earlier $j$. Every feasible ordered placement anchored at zero dominates these coordinates by induction. The recurrence itself satisfies all pair constraints.

The two seeded searches per ladder rung explore interleavings of the lower and upper halves, a cyclic shift of the high labels, and the even-rank reversals from S2's block recovery theorem. A sampled cut converts each template to a line word. Proposals exchange two labels. Binary64 scoring reuses the unchanged prefix and drops predecessors once even their maximum possible gap cannot improve the current maximum. The first phase allows equal-score swaps. If the improvement after 262144 proposals still exceeds the threshold, short-range sweeps continue with forward and backward longest-path distances. Each path crosses the cut after the changed segment once, which supplies a cheap proposal score. A full suffix replay confirms accepted improvements. For each run at $n\ge200$, the last doubling improved $(S+1)/(\pi n)$ by less than $10^{-6}$. Small reference cases use 1024 proposals. Each certificate records both seeds and budget histories. These scores are numerical observations used for choosing orders.

The generator reruns the ordered recurrence with **integer** edge lengths. For $p=1$ take $D=n\,10^{12}$ and use $\lceil10^{12}\sqrt{ij}\rceil$. For $p=2$ take $D=n^2$ and use $ij$ exactly. Discarding an earlier predecessor when $X_j+D$ is already at most the current maximum preserves the integer recurrence, since every gap is at most $D$. The file stores the positions in label order, the word, $D$, the span numerator and the numerator/denominator of $B$.

The isolated verifier reads the stored coordinates directly. It checks the full permutation and its increasing order, the exact extrema, and every unordered pair. For $p=1$ its integer test is $n^2(X_i-X_j)^2\ge ijD^2$. For $p=2$ it is $n^2|X_i-X_j|\ge ijD$. To check the final strict inequality, it uses $\pi=16\arctan(1/5)-4\arctan(1/239)$. The tangent addition formula gives tangent one for $4\arctan(1/5)-\arctan(1/239)$ in the first quadrant. The first 32 alternating terms for $\arctan(1/5)$ give a lower endpoint and the first 11 for $\arctan(1/239)$ an upper endpoint. Exact rational cross-multiplication proves the printed ceiling. Search metadata plays no role in feasibility.

### Finite radii and the quadratic profile

For prescribed radii $r_i=n^p(i/n)^p$ take the angular positions $2\pi x_i/(S+1)$ modulo $2\pi$. One directed arc between normalized line marks has their line separation and the other contains the unit closing gap. Both are at least $\sqrt{a_i a_j}$ before angular scaling. The upper angular comparison in Paper II gives
\[
 \theta_R(r_i,r_j)\le 2\sqrt{r_i r_j}/R .
\]
At $R=n^p(S+1)/\pi$ both angular arcs therefore meet the required angle. This proves the finite upper bound $R_p^*(n)\le n^p(S+1)/\pi$. For $p=1$ the source squeeze gives the factor $n$ and implies the looser $n^2$ comparison in the task. For $p=2$ the factor is $n^2$.

The exact reference check compares the constructed radius to each applicable published $U_n$ using $n^p(S+1)7/22<R$ from $\pi<22/7$. At $n=3,4,5,6,14$ for the linear family and $n=3,4,5,6$ for the quadratic family, each published upper endpoint is below even this rational lower estimate on the constructed radius. The finite witnesses are consistent with the sharper published brackets. The quadratic reference uses the outward display endpoints from the pinned README and its stated interval-backend assumptions.

The pinned quadratic project proves
\[
 (434+4\sqrt2)/(1587\pi)\le\liminf R_2^*(n)/n^3
 \le\limsup R_2^*(n)/n^3\le857/(3000\pi).
\]
The outer endpoints are approximately $0.08818344249$ and $0.09093052415$. The $n=3200$ certificate yields the **conditional claim** $C_2<0.088581212993$ under the radius-profile theorem's quadratic limit and finite-template upper inequality. The finite geometric construction above and its exact pair checks stand on their own.

## Two evaluations of the four-block cost

Take $\alpha=10930/100000$ and consecutive lengths $(31903,4370,580,5)/100000$. Their sum is $0.36858<1-\alpha$. Put $A=1+\alpha$, and let $[u,v]$ denote a slab. S2's measure averages $(t,A+t,A+u+v-t)$ and its high-coordinate transpose with weights $1/2$. The two give the same value of
\[
 g(t,X,Y)=\max\{\sqrt{tX}+\sqrt{tY},\sqrt{XY}\}.
\]
After the slabs, $X=Y=1+\{t+\alpha\}$. Thus the integral of $g$ is the sum of four unweighted slab integrals and a diagonal integral split at $1-\alpha$. The final normalization is $1/(4\pi)$ by the main paper's block-cost equation. Its general block transfer theorem proves $C_*\le C(\mu)$ for these parameters.

| Independent calculation | Closed enclosure of $C(\mu)$ | Width |
|---|---|---:|
| Exact switch signs and antiderivatives in Arb | $[0.14191330499527,0.14191330499528]$ | $10^{-14}$ |
| Directed integer subdivision | $[0.1419133048777,0.1419133051216]$ | $2.439\times10^{-10}$ |

**Antiderivatives.** The sign determining the active branch is that of $\sqrt{t/X}+\sqrt{t/Y}-1$. Both ratios increase on each piece because the intercepts of $X,Y$ are positive. With $p=t/X$, $q=t/Y$ and $r=1-p-q$, the sign is positive when $r<0$ and otherwise equals the sign of $4pq-r^2$. Eighty-eight exact rational bisections enclose any interior switch. Its strip contributes between zero and three times its length. The primitives used off that strip follow by differentiating
\[
 H_M(z)=\tfrac12\bigl(z\sqrt{M^2-z^2}+M^2\arcsin(z/M)\bigr),\qquad
 K_c(t)=\tfrac12\bigl((t+c/2)\sqrt{t(t+c)}
                  -(c/2)^2\log(t+c/2+\sqrt{t(t+c)})\bigr).
\]
Their derivatives are $\sqrt{M^2-z^2}$ and $\sqrt{t(t+c)}$. For $X=A+t,Y=e-t$ put $e=A+u+v$. The chord primitive is $H_{(A+e)/2}(t-(e-A)/2)$ and the legs primitive is $K_A(t)+H_{e/2}(t-e/2)$. On a diagonal $t+c$ the primitives are $ct+t^2/2$ and $2K_c(t)$. Arb operates at 192 bits with outward rounding.

**Integer subdivision.** A separate standard-library program encodes the six pieces by their endpoints. Each piece has 32768 equal panels. Integer square roots give lower and upper estimates for the two candidates from the respective extrema of $t,X,Y$ on each panel. If these separate, the active smooth branch is integrated by a midpoint enclosure. When $t\le1/4$ the chord dominates since $1/\sqrt X+1/\sqrt Y\le2$. For $q(t)=at^2+bt+c$ the second derivative of $\sqrt q$ is $(4ac-b^2)/(4q^{3/2})$. On a chord $q\ge1$ and the affine factors in these pieces have intercepts of absolute value below two. For an active legs panel with $t\ge1/4$, each product $tX,tY\ge1/4$ and its discriminant has absolute value at most four. In particular the absolute second derivative of each smooth branch is less than 100. A panel of length $h$ therefore has midpoint error at most $100h^3/24$. Seven undecided panels use a direct range enclosure. Rational summation and a separately implemented two-sided Machin series enclose the normalization. The methods share the published mathematical definition and run in different arithmetic implementations.

### The implicit published parameter choice

Paper II isolates $\widehat\alpha$ in $(0.1093,0.10931)$, $x_*$ in $(0.2876,0.2877)$, the second length in $(0.043,7/160)$ and the third in $(29/5000,27/4000)$. Its first length is $(1+\widehat\alpha)x_*$ and its last is $1/20000$. These isolations give the **separate** rigorous enclosure
\[
    0.141895293745\ \le U_4\le\ 0.141931316245 .
\]

Here is the perturbation bound. At fixed $t$ either branch of $g$ is individually 1-Lipschitz in each high coordinate on $[1,2]$, as follows from its first derivatives. Write the integral as the full shifted diagonal plus a correction on each slab. Changing the shift by at most $d$ changes that diagonal integral by at most $4d$, including the wrap interval of length at most $d$ where $1\le g<3$. Suppose corresponding slab endpoints differ by at most $d_u,d_v$ and their lengths are at most $L$. The slab correction relative to the diagonal has absolute value at most $L$ since the second high coordinate moves by at most one slab length. The symmetric difference costs at most $L(d_u+d_v)$. On the overlap the reflected and diagonal terms together change by at most $4d+d_u+d_v$ per unit length. Thus the total cost error is bounded by
\[
 \frac{4d+\sum_j L_j[\,4d+2(d_{u,j}+d_{v,j})\,]}{4\pi}.
\]
The Arb script forms all endpoint deviations from exact rational parameter ranges. This coarser enclosure preserves the published definition and still places the finite line bound strictly below $U_4$.

### Replaying the numerical starting points

At the explicit shift $107/1000$ the zero-slab cost lies in $[0.14199597949845,0.14199597949846]$ by the same antiderivatives. The independent subdivision gives $[0.1419959791910,0.1419959798214]$. This accounts for the diagonal-only estimate near $0.1419960$. The published implicit $U_4$ and this note's fixed four-block value have distinct parameters. The reported approximate $0.1419132$ for the former lies inside the coarser literal enclosure.

As a separate numerical observation, two runs at $n=400$ starting from the plain alternating word and making 12000 swap proposals returned $0.1414455073191551$ and $0.14146746207639196$. Their seeds were 20367056 and 20367057. Run `node paper_assets/line_upper/search.cjs --interleaved-reference` to reproduce them.

## Estimating the limiting line span

**Numerical observation.** Least-squares intercepts for the searched $S/n$ versus $1/n$ are $0.442666$, $0.442654$ and $0.442634$ using the largest three, four and five rungs. They suggest $\lim b_n/n=\pi C_*$ near **0.44265**. The words have unknown optimization gaps. A fit in $1/\sqrt n$ on the same windows instead gives $0.442986$ to $0.443345$, above the rigorous ceiling $\pi(0.140958576058)$. The model sensitivity is larger than the spread of the $1/n$ fits. A rigorous outer range from the two proved endpoints is $(0.44161201050,0.44283442701)$. The regressions supply neither a confidence interval nor a rate of convergence.

## Reproduction

From the repository root, with the official pinned inputs prepared as in the task, choose a fresh temporary directory for the search output. The following commands use relative paths to illustrate one replay.

~~~sh
node paper_assets/line_upper/search.cjs /tmp/ringmin-line-orders
python paper_assets/line_upper/generate.py /tmp/ringmin-line-orders /tmp/ringmin-line-certificates
python -I -S paper_assets/line_upper/verify_line_certificate.py paper_assets/line_upper/certificates/p1_n03200.json
python paper_assets/line_upper/block_antiderivatives.py
python -I -S paper_assets/line_upper/verify_block_subdivision.py
python paper_assets/line_upper/report.py --inputs .codex_inputs
python -m pytest tests/test_line_upper.py
~~~

The verifier accepts several files in one invocation. In PowerShell run
`python -I -S paper_assets/line_upper/verify_line_certificate.py (Get-ChildItem paper_assets/line_upper/certificates/*.json).FullName`.
Build `preview.tex` from its directory in three passes with `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=TEMP preview.tex`, substituting an existing temporary output directory. The dossier records the tool versions, source hashes and independent replay.

Sources for the theorem, construction and finite comparisons are [Paper II v3 and S1/S2](https://arxiv.org/abs/2609.13630v3), [Paper I v4](https://arxiv.org/abs/2607.28654v4), and the [pinned quadratic project](https://github.com/falker47/ringmin-squared/tree/1d0a5dea10cd09783a9c0e2d54ede79b790cce2b).
