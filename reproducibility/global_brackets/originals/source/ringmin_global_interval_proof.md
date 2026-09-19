# Ringmin — fresh global interval certificate candidate

Date: 2026-09-17. Status: **computer-assisted certificate candidate, awaiting external independent review and Windows replay**.

This document accompanies `ringmin_global_interval_replay.py` (version 0.1.0),
`ringmin_global_interval_candidate.json`, and the second checker
`ringmin_global_interval_crosscheck.py`. No repository or Review State Registry
baseline has been promoted. This is not a journal manuscript.

## 1. Findings from the uploaded evidence bundle

Input ZIP: `ringmin_interval_evidence_20260917_114928_d9feeef3.zip`.
SHA-256: `ab93503aa6d06b8661c48a54469b88e1b6395cab043d9c1ba39fafb3e9adf9b7`.

All 15 expected members were read and CRC-checked: 12 retained interval reports,
one structural report, one linkage report, and one SHA-256 CSV manifest.
There are 676,283 uncompressed bytes. There are no pickle files in this bundle.

The checks performed here established:

- 12 numerical reports, covering n=3,...,14, have consistent pinned input,
  script, reference-frontier, schema-report and preservation-manifest hashes.
- All 90 per-prefix summaries agree with the structural and linkage reports.
  The CSV contains 280 internally matching source/copy hash records.
- The 12 embedded historical frontier JSON objects reconstruct to the exact
  known Git blob identities from reference commit
  `c0d9d6e66afc8ec94918adbe23345bdc7a7fa43b`.
- Reported totals are 1,353,356 retained orders and 47 historical frontier
  orders. All reported lower tests pass; all 1,353,309 reported non-frontier
  upper-exclusion tests pass. Counts and minimum margins aggregate correctly.
- **All 908 saved pair-angle intervals** (both L and U for each n) contain
  independently recomputed, sharper exact-rational enclosures. The 2*pi
  enclosure was also rechecked. The new calculation sums the rational
  coefficient polynomial exactly, unlike the pilot's termwise fixed-point
  rounding.

Important limit: absent pickle/log bytes were not rehashed here. The ZIP's
aggregated order/witness hashes do not permit a replay of the 1,353,356 original
retained candidates. This bundle audit is distinct from the fresh, complete
combinatorial computation below, which does not require those bytes at all.

Machine-readable audit: `ringmin_bundle_review.json`.

## 2. Model and candidate claim

The model is exactly the all-pairs model for outer radii 1,...,n, with every
outer circle externally tangent to the central circle and pairwise disjoint
interiors. The reference definitions and implementation were read at the pinned
commit above:

- `knowledge/DEFINITIONS.md`;
- `src/ringmin/evaluator.py`.

For each n, the new computation supports the candidate statement

\[
L_n < R^*(n) \le U_n,\qquad U_n-L_n=10^{-11}.
\]

The decimals are rational test inputs, not assumed exact optimum values.
Neither the historical Top-K membership nor a floating-point error envelope is
an assumption of this new argument.

| n | L | U |
|---:|---:|---:|
| 3 | 0.26086956521 | 0.26086956522 |
| 4 | 0.84445358956 | 0.84445358957 |
| 5 | 1.69549408120 | 1.69549408121 |
| 6 | 2.79491951889 | 2.79491951890 |
| 7 | 4.15318955374 | 4.15318955375 |
| 8 | 5.76779428458 | 5.76779428459 |
| 9 | 7.72672655261 | 7.72672655262 |
| 10 | 9.97990738586 | 9.97990738587 |
| 11 | 12.48872048718 | 12.48872048719 |
| 12 | 15.25887043044 | 15.25887043045 |
| 13 | 18.31756304721 | 18.31756304722 |
| 14 | 21.66539518221 | 21.66539518222 |

This is a bracket for the minimum value. It is not exact decimal equality,
a uniqueness statement, a classification of all minimizers, or a theorem about
which circles float in all optimal placements.

## 3. Necessary angular inequalities

For central radius Q and two outer radii a,b, their center distances from the
origin are Q+a and Q+b. If their directed angular difference is delta, the
squared separation is

\[
(a-b)^2+4(Q+a)(Q+b)\sin^2(\delta/2).
\]

Thus non-overlap is equivalent to

\[
\phi_{ab}(Q)\le\delta\le2\pi-\phi_{ab}(Q),\qquad
\phi_{ab}(Q)=2\arcsin\sqrt{\frac{ab}{(Q+a)(Q+b)}}.
\]

The directed gaps in any cyclic subset of a feasible placement sum to 2*pi.
Consequently, for every induced cyclic sequence C of length at least three,

\[
A_C(Q):=\sum_{(a,b)\in E(C)}\phi_{ab}(Q)\le2\pi
\]

is necessary. Each angle is continuous and strictly decreasing in Q>0. A
strict violation at Q=L rules out that cyclic sequence at L and at smaller
radii. Its chain closing radius is strictly greater than L. There are only
finitely many full cyclic orders; therefore proving a strict chain violation
for every order yields a strictly greater-than-L global lower bound.

The checker uses C itself, C without radius 1, and C without radii 1 and 2,
omitting sequences shorter than three. These are necessary conditions only;
the proof needs just one violated condition for each rejected full order.

## 4. Exact outward enclosures — no libm assumptions

Set S=2^128. The checker constructs integers w_ab,h_ab,T_-,T_+ satisfying

\[
w_{ab}/S\le\phi_{ab}(Q)\le h_{ab}/S,\qquad
T_-/S\le2\pi\le T_+/S.
\]

Let q=ab/((Q+a)(Q+b)), an exact positive rational. On all tested inputs q<0.9.
The series identity is

\[
\arcsin x=x\sum_{k\ge0}\frac{\binom{2k}{k}}{4^k(2k+1)}x^{2k}.
\]

Source for the series: NIST DLMF 4.24.1,
https://dlmf.nist.gov/4.24.E1 .

Let s_k denote the kth term of the coefficient polynomial in q. Then

\[
\frac{s_{k+1}}{s_k}
=q\frac{(2k+1)^2}{(2k+2)(2k+3)}<q.
\]

With P_N=sum(s_0,...,s_(N-1)), the remaining polynomial tail lies between
zero and s_N/(1-q). All s_k and P_N are computed as exact Fractions. A
192-bit integer square-root enclosure x_- <= sqrt(q) <= x_+ gives

\[
2x_-P_N\le\phi_{ab}(Q)
\le2x_+\left(P_N+\frac{s_N}{1-q}\right).
\]

The program stops when the polynomial tail is less than 2^-176, and converts
only the final endpoints outwards to the common S grid. Every accepted test is
an integer comparison. The 192-bit square-root bracket is checked by exact
squaring. Domain or iteration failures stop the computation.

For 2*pi, use

\[
2\pi=32\arctan(1/5)-8\arctan(1/239).
\]

The alternating arctangent series (DLMF 4.24.3) with its signed first-omitted
term encloses each value exactly. The implementation uses 80 and 25 terms,
respectively. Opposite endpoints are used for the negative coefficient.
The Machin identity follows because tan(2 atan(1/5))=5/12,
tan(4 atan(1/5))=120/119, and subtraction of atan(1/239) gives tangent 1;
the angle lies in the first quadrant and is pi/4.

If sum of the lower integer edge weights exceeds T_+, then the true angle
sum exceeds 2*pi. No assertion about binary64 transcendental accuracy is used.

## 5. Fresh complete lower-bound coverage

### 5.1 n=3,...,9: small direct enumeration

Fix n at the first position and enumerate all permutations of 1,...,n-1,
retaining exactly those with second radius less than the last radius.
This selects one representative from each rotation/reflection class.
Every order is rejected by a strict induced-chain angular violation.
The checked count equals (n-1)!/2. There are 23,116 such full orders in total
across this range. These are newly generated, not read from checkpoints.

### 5.2 n=10,...,14: delete radius 1 and bound every completion

Take a full cyclic order and delete radius 1, producing a skeleton cycle on
{2,...,n}. Fix n as anchor. Conversely, a skeleton cycle and the gap in which
1 is inserted determine a full cycle. There are n-1 insertion gaps.
For n>=4 the skeleton has at least three distinct vertices, so quotienting
its reflection is unambiguous: retain second radius < last radius.
This construction covers every full cyclic order up to rotation and reflection.

At Q=L use the lower integer edge weights w. For current vertex v and unvisited
set M, define the exact minimum completion cost

\[
H(\varnothing,v)=w_{v,n},\qquad
H(M,v)=\min_{u\in M}\{w_{v,u}+H(M\setminus\{u\},u)\}.
\]

This recurrence follows by partitioning all Hamiltonian completions according
to their next vertex. Induction on |M| proves it equals the minimum completion
cost. The implementation computes it bottom-up and verifies the Bellman
equations for every populated state.

For a partial skeleton with accumulated integer cost c, prune only when

\[
c+H(M,v)>T_+.
\]

Every completion of that prefix has a lower-rounded cycle sum greater than
T_+, hence its true angular sum exceeds 2*pi. Every full order obtained by
inserting radius 1 into such a skeleton is therefore infeasible at L, regardless
of the insertion position. A subtree with |M| unvisited vertices covers |M|!
oriented skeleton completions; this count is accumulated exactly.

For skeletons not pruned, retain one orientation, insert radius 1 in every
cyclic gap, and check the full/remove-1/remove-{1,2} chain inequalities directly.
All such full orders have a strict violation at L.

Let P be the total number of oriented skeleton completions covered by pruned
subtrees, and K the number of unpruned skeletons after reflection quotienting.
The program checks

\[
P+2K=(n-2)!,\quad P\text{ even},\quad
\frac{P(n-1)}2+K(n-1)=\frac{(n-1)!}2.
\]

The factorial identity is an additional coverage check; the proof of coverage
is the exhaustive recursion plus the valid pruning inequality and the
insertion correspondence. Cardinality metadata alone would not suffice.

### 5.3 Observed exact counts in the new execution

| n | DP states, including root | Unpruned skeletons (reflection removed) | Full orders explicitly checked | Full orders covered by pruning | Total canonical coverage |
|---:|---:|---:|---:|---:|---:|
| 10 | 1,025 | 0 | 0 | 181,440 | 181,440 |
| 11 | 2,305 | 0 | 0 | 1,814,400 | 1,814,400 |
| 12 | 5,121 | 0 | 0 | 19,958,400 | 19,958,400 |
| 13 | 11,265 | 246 | 2,952 | 239,497,848 | 239,500,800 |
| 14 | 24,577 | 18,660 | 242,580 | 3,113,267,820 | 3,113,510,400 |

For n=10,...,12 the DP root already violates the angular condition, so the
whole skeleton tree is pruned rigorously at the root. Zero explicitly expanded
full orders does not mean zero coverage.

At n=13 the search visits 9,234 prefix nodes and prunes 6,084 subtrees; at n=14
it visits 435,074 prefix nodes and prunes 245,060 subtrees. This is a new small
instance-specific computation, not a full repeat of the historical Stage A.

## 6. Constructive upper bound and independent rational geometry

At Q=U, use upper angular bounds h_ab and lower circumference T_-.
Solve the stronger integer difference constraints

\[
h_{ab}+p\le x_j-x_i\le T_--h_{ab}-p,
\]

where p=ceil(S/10^16) is a positive constructive margin, not a tolerance.
The positions x_i/S are rational angles. A shortest-path procedure proposes
them; a separate checker tests every pair and the cyclic ordering exactly.

Then construct an entirely rational Cartesian placement. For each direction,
propose a rational stereographic parameter t, using a fixed-point polynomial
approximation only to obtain a candidate. The proposal's approximation error
is not assumed or needed in the final proof. Define

\[
C_r=(U+r)\left(\frac{1-t_r^2}{1+t_r^2},
                    \frac{2t_r}{1+t_r^2}\right).
\]

All coordinates are rational. The checker verifies exactly

\[
\|C_r\|^2=(U+r)^2,\qquad
\|C_a-C_b\|^2>(a+b)^2\quad(a\ne b).
\]

Thus every circle is externally tangent to the central circle, and all outer
pairs are disjoint. No numerical trigonometry or interval assumption is needed
for this final Cartesian validation. The stereographic parameters are stored
in the certificate, so the coordinates are reconstructible exactly.

The second checker uses the algebraically equivalent independent test

\[
(U+a)(U+b)(t_a-t_b)^2
>ab(1+t_a^2)(1+t_b^2).
\]

Every one of the 47 trial frontier orders has a valid rational Cartesian
placement at its U, comprising 3,004 outer-pair checks in total. One placement
per n already suffices for the global upper bound. These are feasible placements
at U, not claims that all 47 orders attain exactly the same true optimum.

## 7. Execution and checks actually completed here

On the assistant's Linux runtime:

1. The complete input-bundle consistency audit passed, including the 908
   independently re-enclosed saved angle intervals.
2. The fresh standalone replay passed all n=3,...,14, including all 47 rational
   Cartesian upper witnesses. One run took 6.58 seconds on this runtime.
3. Eighteen randomly generated small symmetric integer TSP instances were
   checked against exhaustive enumeration as DP regression controls.
4. A second implementation used top-down memoization and an explicit stack,
   rather than the replay's bottom-up table and recursive traversal. Counts,
   exact minimum leaf/pruning margins and explicit witness-stream hashes
   agreed for every n. Rational geometry passed via the independent identity.
5. Deliberately collapsed placement directions were rejected. Proven feasible
   trial orders at U were not falsely rejected by the lower angular tests.
6. The standalone script was copied to a separate directory and run with
   `python -I -S`, without the pilot or evidence bundle. It reproduced the
   same deterministic certificate hash in 6.88 seconds.

Deterministic certificate SHA-256 (excluding runtime/report metadata):

`6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0`

These are computational cross-checks performed in this conversation, **not
external peer review or proof-assistant verification**. Windows replay remains
the next local reproducibility check. No identical runtime on another machine
is promised.

## 8. What this changes — and what it does not

The candidate global proof **bypasses historical float64 pruning**. It does not
establish a posteriori that every historical pruning comparison was rigorous.
If the new derivation and implementation pass independent review, a journal
certificate can rely on this new exact-arithmetic route instead of a numerical
error proof for the old Top-K exclusions.

Outstanding work before acceptance remains: Windows replay; independent review
of the mathematical argument, coverage and implementations; an atomic repository
task and compact versioned/archive artifact; review of the resulting exact commit
under the existing Registry protocol; and alignment of journal claims with what
was actually checked. The fixed-order seam theorem and editorial submission
requirements remain separate. No journal-ready status is asserted here.
