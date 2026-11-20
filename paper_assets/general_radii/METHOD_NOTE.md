# Exact brackets for distinct positive integer radii

Fix $n\ge3$ distinct positive integers $a_0<\cdots<a_{n-1}$ and let $R^*$ be the infimum of feasible central radii over all placements. Every outer circle is externally tangent to the central circle. Outer interiors must be pairwise disjoint. The input order of the radii is immaterial. The generator uses zero-based ranks internally and stores the radii themselves in the Cartesian witness.

## Angular constraints

At radius $R>0$, put $q_{ij}=a_i a_j/((R+a_i)(R+a_j))$ and $\theta_{ij}=2\arcsin\sqrt{q_{ij}}$. The law of cosines on the centers gives the following equivalence. For a directed polar separation $\alpha\in[0,2\pi]$, the outer interiors are disjoint exactly when $\theta_{ij}\le\alpha\le2\pi-\theta_{ij}$. The consecutive directed gaps of any induced cyclic subset of at least three circles sum to $2\pi$. Its sum of consecutive required angles is therefore at most $2\pi$. This is the induced-cycle inequality of Paper I, §6.

At a rational lower endpoint $L$, the certificate supplies integer weights $w_{ij}$ and threshold $T$ at scale $S=2^b$. The verifier establishes $w_{ij}/S\le\theta_{ij}(L)$ and $T/S>2\pi$. It uses the alternating series in Machin's identity $2\pi=32\arctan(1/5)-8\arctan(1/239)$, bounding each arctangent by successive rational partial sums. It checks $0\le w_{ij}/S<\pi$ against the resulting lower bound on $\pi$. For every positive entry it proves $\cos(w_{ij}/S)>1-2q_{ij}$. Zero is a valid lower bound directly.

For the cosine test, absolute Taylor terms are propagated on the integer grid $2^{2b+80}$. Each lower term is rounded down and each upper term up after multiplication by $x^2/((2j-1)2j)$. From the signed partial sum the verifier subtracts an upper term on a negative sign and adds a lower term on a positive sign. Once the first omitted term has index at least two and upper bound at most two grid units, subtracting its entire bound gives a lower enclosure. The omitted tail alternates with decreasing magnitudes because $x<\pi<4$ and $x^2/((2j+1)(2j+2))<1$ for $j\ge2$. Monotonicity of cosine on $[0,\pi]$ proves the desired ordering. Multiprecision trigonometry only proposes certificate entries.

## Deletion and insertion

**Exact theorem.** Delete the $d$ smallest labels, with $0\le d\le n-3$, and write $k=n-d$. Each unoriented cyclic order on the $k$ retained labels, called a core here, has precisely
$$
 I_{n,k}=\prod_{s=k}^{n-1}s=\frac{(n-1)!}{(k-1)!}
$$
full unoriented cyclic orders above it.

**Proof.** Pin the largest label and select the orientation in which its successor has smaller rank than its predecessor. The two neighbors differ because $k\ge3$ and labels are distinct. Insert the deleted labels in a fixed order. When $s$ labels are present there are exactly $s$ directed gaps, including the closing gap. Deleting these inserted labels in reverse order reconstructs the full insertion history. After restriction to the core, the known core orientation selects the same orientation for a full cyclic class, even when insertion changes the anchor's neighbors. Thus histories are in bijection with full classes above the core. For $d=0$ the empty product is one.

The verifier constructs the same collection a second way. For a fixed oriented core, choose a weakly increasing list of $d$ gap indices and independently permute the $d$ deleted labels. Assign the permuted labels to the chosen gaps from left to right. Reading the contents of each gap recovers this description. Its count is $\binom{k+d-1}{d}d!=I_{n,k}$.

## Complete lower coverage

Pin the largest core label $A$. For every nonempty subset $M$ of the other core labels and $j\in M$, let $D[M,j]$ be the least integer edge cost of a path from $A$ through exactly $M$, ending at $j$. Then
$$
 D[\{j\},j]=w_{Aj},\qquad
 D[M,j]=\min_{h\in M\setminus\{j\}}\bigl(D[M\setminus\{j\},h]+w_{hj}\bigr).
$$
Removing the last edge proves the recurrence by induction. Since the weight matrix is symmetric, reversing a completion shows that a prefix of cost $c$ ending in $j$ with unvisited labels $M$ has minimum full cost $c+D[M\cup\{j\},j]$. At the root one minimizes the full path plus its closing edge. At a terminal prefix the completion is precisely the closing edge.

Prune a prefix only if this minimum exceeds $T$. Every full order extending that prefix contains a core cycle violating the necessary induced-cycle inequality. A pruned prefix with $h$ remaining labels represents $h!$ oriented completions. Let $P$ be the sum over the disjoint pruned prefixes and $K$ the number of surviving canonical cores. Symmetry pairs the surviving orientations and also the excluded orientations. The traversal and all insertions give
$$
 P+2K=(k-1)!,\qquad P\equiv0\pmod2,\qquad
 E=KI_{n,k},\qquad \frac P2 I_{n,k}+E=\frac{(n-1)!}{2}.
$$
The verifier recomputes the traversal, counts reversed survivors, expands every gap assignment and checks every surviving full word. The generator builds suffix costs recursively and inserts one label at a time. The verifier builds forward costs by subset size and assigns deleted labels directly to gaps.

For an explicit full word, each rank threshold gives a candidate induced violation by removing all smaller labels. If these tests are inconclusive, there is also an exact difference-constraint test. Write $x_i$ for unwrapped angles in word order. For $i<j$ a feasible configuration satisfies the integer relaxation
$$
 x_j\ge x_i+w_{ij},\qquad x_i\ge x_j+w_{ij}-T
$$
in scaled units, where the subscripts here denote the word positions. A directed cycle with positive total integer weight contradicts this system by summation. A positive closed walk contains a positive simple cycle after decomposing at repeated vertices. The generator detects positive cycles by longest-path relaxation, and the verifier computes maximum path weights by the Floyd–Warshall recurrence. A positive diagonal describes a real closed walk even when a positive cycle already exists. Each simple cycle has at most $n$ edges. All explicit exclusions in the two reported families use the threshold tests. A separate synthetic oracle exercises the general graph fallback.

## Strict lower endpoint

**Proved corollary.** If the lower audit succeeds, every full order has a necessary inequality with true excess at least $1/S$ at $L$. For a core or induced cycle this follows from the integer bound $T+1$. A positive simple constraint cycle with $h$ backward edges instead gives $\sum\theta_{ij}(L)-h\,2\pi\ge1/S$. For $R\ge L$,
$$
 |\theta'_{ij}(R)|
 =\sqrt{\frac{a_i a_j}{R(R+a_i+a_j)}}\left(\frac1{R+a_i}+\frac1{R+a_j}\right)
 \le\frac{2a_{n-1}}{L^2}.
$$
The excess of every relevant cycle drops by at most $D\,\delta$ on $[L,L+\delta]$, where $D=2n a_{n-1}/L^2$. Choose the rational buffer
$$
 \varepsilon=\min\{(U-L)/2,\ 1/(2SD)\}.
$$
Each violation then retains at least half a grid unit throughout $[L,L+\varepsilon]$. At smaller positive radii all angles increase. Hence $R^*\ge L+\varepsilon>L$, including when the optimum is defined as an infimum.

## Upper endpoint

At $U$ the certificate gives one rational parameter $t_i$ for each member of a full word. Its center is
$$
 c_i=(U+a_i)\big((1-t_i^2)/(1+t_i^2),\ 2t_i/(1+t_i^2)\big).
$$
The verifier checks the polar order, all $n$ rational equalities $\|c_i\|^2=(U+a_i)^2$ and each of the $\binom n2$ strict inequalities $\|c_i-c_j\|^2>(a_i+a_j)^2$. Thus the witness proves $R^*\le U$. The generator obtains candidate angles from all-pairs difference constraints at the upper endpoint and converts them to rational stereographic directions. For automatic search it bisects a rational grid and checks partial insertions only to find witness orders. The final lower audit always replays every insertion of every retained core. If a grid point equals the optimum, a strict upper witness may require the next grid point.

The finite proof uses no assumption about contact at an exact optimizer. The DP uses $O(k2^k)$ states. Out-of-core expansion and complete word testing can still require factorial time. Distinct labels and at least three core vertices are hypotheses of the coverage argument.

Maurizio Falconi gives the angular model and original one-label construction in Paper I, §6. [Versioned paper](https://arxiv.org/abs/2607.28654v4)
