# Independent internal proof review

    reviewed_on=2026-09-11
    mode=STRICT
    review_kind=fresh reviewer subagent; internal adversarial validation
    conclusion=INTERNALLY_VALIDATED
    external_acceptance=not performed or implied

## Scope and source

The reviewer independently reconstructed the argument in
[`GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md`](../../research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md)
from the canonical angular definition and the all-pair line separation
constraint. The review did not take the builder's status or conclusions as
evidence. It covers the exact theorem argument for existence of the global
normalized limit and its effective finite-word variational characterization.
It does not certify additional finite optima or evaluate the constant to a
new practical numerical precision.

No fatal mathematical gap was found. The following audit is independent
reasoning within the same research task, not independent external acceptance.

## Reconstructed proof obligations

- **Line minimization:** every earlier point supplies a lower bound on the
  next coordinate. The maximum recurrence satisfies every such constraint,
  and its longest-path interpretation gives the minimum span. Nonnegative
  weights preserve coordinate order, including coincident zero marks.
- **Exact geometry:** subtracting the numerator `u*v` from
  `(R+u)*(R+v)` gives `R*(R+u+v)`, proving the stated atan identity. The
  inequalities for asin and atan have the required directions. Cutting
  preserves one directed arc; closing with gap 1 controls the other arc.
  Scaling these inequalities recovers both bounds in equation (6), with
  the factor `E/pi` and the error `1/n` in the correct places. This uses
  all pairs rather than only consecutive circles.
- **Limit and actual labels:** the retained sorted marks of `k` copies are
  exactly `ceil(i/k)/n`. Multiplication by `n*k/N` dominates `i/N` for
  each individual retained point. Each target label is then assigned once,
  so the recovery is a genuine finite permutation and not only a marginal
  assertion. The concatenation cost and its normalization give the claimed
  limsup bound for every large `N`; taking a liminf subsequence closes
  existence and the infimum formula. Intermediate marks above 1 cause no
  problem because both marks and distances are scaled homogeneously.
- **Finite types and zero marks:** concatenation supplies subadditivity
  with a bounded remainder. The two quantized systems share every nonzero
  type except the top type. Removing zero marks and appending `q` unit
  marks costs at most `q`, yielding the stated `1/k` error, including
  `k=1`. The sorted uniform labels lie between the two quantized arrays.
- **LP lower bound:** disjoint blocks contain all but fewer than `r`
  vertices. Their spans sum to at most the total span. In a convergent
  empirical-distribution subsequence the discarded type counts vanish,
  and the normalized block counts are exactly the LP constraints.
- **LP upper recovery:** a rational polytope has a minimizing rational
  vertex even with algebraic objective coefficients. A common denominator
  produces integer word counts and exactly equal integer type counts.
  Gap 1 makes every cross-block pair feasible. Repetition and the already
  established finite-type limit give the `1/r` error without a cyclic
  compatibility assumption.
- **Effective characterization:** enclosing each edge weight encloses
  every path of at most `r-1` edges and then its maximum. The objective
  enclosure has the claimed width after division by `r`. Rational endpoint
  LPs can be solved or certified with finite rational arithmetic. Their
  bounds together with a rational enclosure of pi give arbitrarily small
  certified intervals in principle. This does not imply practical
  high-precision complexity, an elementary closed form, or a unique
  microscopic optimizer.

## Corrections requested and verified

1. The initial geometry statement included `n=2`, although the canonical
   model requires positive central radius and the two-circle optimum is
   an unattained infimum zero. Equation (6) now explicitly applies for
   `n>=3`. The auxiliary line construction still correctly starts at
   `n=2`, and the asymptotic result is unaffected.
2. Directed intervals alone do not decide every algebraic equality in
   finite time. Section 6 now explicitly certifies the rational endpoint
   LPs. Both success and failure of those checks are decidable by rational
   arithmetic; no interval-refinement equality oracle is claimed.

Both corrections were inspected in the updated proof before this review
was recorded. Neither changes the substantive limiting theorem.

## Independent bounded exact checker

[`check_line_recovery.py`](check_line_recovery.py) uses only the Python
standard library and imports no production Ringmin module. Marks are
`0,1/4,1`, represented by rational square roots `0,1/2,1`, making all
tested separation weights exact rational numbers. Every word of lengths
2 through 6 is checked. Exhaustive increasing-index paths are an oracle
independent of the recurrence used to construct coordinates. Direct
all-pair checks also test closing, reversal and two-block concatenation.

The quantile check constructs the copied lists explicitly for template
sizes 2 through 20 and every target size from the template size through
100. It checks the claimed quantile formula, scaled pointwise domination
and the genuine target-label multiset. It does not numerically solve a
line optimization for those uniform labels.

Four negative controls must be rejected:

- an adjacency-feasible zero-mark bridge that violates a nonadjacent pair;
- closure of two unit marks without the added gap;
- a reversed label assignment that increases a retained mark;
- quantile recovery with its necessary scale factor omitted.

Every guard uses explicit exceptions, so disabled Python assertions do
not disable verification.

Environment: local Windows PowerShell; Python 3.14.3, standard library only.
Commands independently executed by this reviewer:

```text
python ops/TASK-20260911__global_variational_limit/check_line_recovery.py
python -O ops/TASK-20260911__global_variational_limit/check_line_recovery.py
```

Both commands exited 0 with identical output:

```text
PASS: 1089 rational words; 13995 independent paths; 13941 pair/closure checks; 1089 all-pair concatenations; 94620 genuine-label quantiles; 4 negative controls rejected.
```

These are deterministic exact finite checks corroborating selected arithmetic
cores of the proof. They do not replace its quantifier arguments, implement
the finite-word LP, run the independent finite-optimum verifier, or establish
hosted CI status. No production, certificate, historical publication, or
external review-state file was edited by this reviewer. Only the checker
and this review record were created.

## Independent audit of the rational word-LP checker

The reviewer subsequently inspected all of
[`check_word_lp.py`](check_word_lp.py), written separately by the builder.
The exact-certificate boundary is sound for its bounded instances:

- Integer square roots construct directed rational edge endpoints. The
  subsequent squared comparisons explicitly check their directions.
- The complete Cartesian product supplies every word, with repetitions.
  Recurrence costs are divided by `r` exactly once, as required by the LP.
- SciPy proposes only a support and approximate dual. Exact Gaussian
  elimination reconstructs the primal weights, rejecting dependent or
  inconsistent supports. Every type equation, including the omitted
  redundant discovery row, is then checked with Fractions.
- The dual has coefficients for the mass constraint and the first `k-1`
  types. Its absent last-type coefficient is implicitly zero, which is a
  valid dual for the full proof formulation. Rationalizing the discovered
  coefficients does not establish validity by itself. Subtracting the
  exact largest violation from the mass coefficient, followed by checking
  every lower-endpoint word inequality, does establish validity.
- The lower dual value and upper primal value therefore bound the true
  algebraic-cost LP without relying on floating-point solver tolerances.
  Their gap and outward decimal formatting are checked rationally.
- Clearing primal denominators gives nonnegative integer word
  multiplicities and exactly equal type counts. This is the finite
  rational-mixture recovery required by the proof.

The checker remains solver-dependent for successful candidate discovery:
another solver version could fail to produce a usable sparse support.
Such failure stops verification; it cannot certify an invalid candidate.
The code is a bounded certificate generator/checker, not the proof's
general terminating exact-vertex-enumeration algorithm. No finding requires
a change to the checker or its theorem claims.

Environment: the same local Python 3.14.3, with SciPy 1.17.1. Both commands
below were independently run by this reviewer and exited 0:

```text
python ops/TASK-20260911__global_variational_limit/check_word_lp.py
python -O ops/TASK-20260911__global_variational_limit/check_word_lp.py
```

Their identical complete output was:

```text
PASS k=1 r=2: 1 words; 1 primal blocks; lambda in [0.500000000,0.500000000]; all rational primal/dual gates
PASS k=1 r=5: 1 words; 1 primal blocks; lambda in [0.800000000,0.800000000]; all rational primal/dual gates
PASS k=2 r=2: 4 words; 1 primal blocks; lambda in [0.353553390,0.353553391]; all rational primal/dual gates
PASS k=2 r=3: 8 words; 2 primal blocks; lambda in [0.436886723,0.436886724]; all rational primal/dual gates
PASS k=3 r=4: 81 words; 2 primal blocks; lambda in [0.409906398,0.409906399]; all rational primal/dual gates
PASS k=4 r=5: 1024 words; 3 primal blocks; lambda in [0.396136075,0.396136076]; all rational primal/dual gates
PASS 1119 complete word inequalities; 18 corrupt certificates rejected
Scope: bounded exact LP certificates; no finite Ringmin optimum, simple closed form, or asymptotic proof by computation.
```

The built-in controls reject negative primal mass, changed total mass and
an invalid dual. Additional independent probes checked rejection of a
negative radicand, dependent and inconsistent proposed supports, and an
incorrect type margin with total mass and nonnegativity preserved. An
independent enumeration of every increasing-index path checked both rational
cost endpoints for all six word sets. The exact PowerShell command was:

```powershell
@'
from fractions import Fraction as Q
from itertools import product
import runpy
import scipy

ns = runpy.run_path('ops/TASK-20260911__global_variational_limit/check_word_lp.py')
ns['rejects'](ns['sqrt_interval'], Q(-1))
ns['rejects'](ns['solve_columns'], [[Q(1), Q(1)], [Q(2), Q(2)]], [Q(1), Q(2)])
ns['rejects'](ns['solve_columns'], [[Q(1)], [Q(1)]], [Q(1), Q(2)])
counts = [(2, 0), (0, 2)]
ns['check_primal']([Q(1, 2), Q(1, 2)], counts, 2, 2)
ns['rejects'](ns['check_primal'], [Q(3, 4), Q(1, 4)], counts, 2, 2)
checks = 0
for k, r in [(1, 2), (1, 5), (2, 2), (2, 3), (3, 4), (4, 5)]:
    roots = {(i, j): ns['sqrt_interval'](Q(i*j, k*k)) for i in range(1, k+1) for j in range(1, k+1)}
    for word in product(range(1, k+1), repeat=r):
        for endpoint in (0, 1):
            best = Q(0)
            for bits in product((0, 1), repeat=r-2):
                indices = [0] + [j+1 for j, bit in enumerate(bits) if bit] + [r-1]
                value = sum((roots[word[i], word[j]][endpoint] for i, j in zip(indices, indices[1:])), Q(0))
                best = max(best, value)
                checks += 1
            if best != ns['span'](word, roots, endpoint):
                raise RuntimeError('independent endpoint path oracle failed')
print(f'PASS: {checks} independent endpoint-path evaluations; 4 additional negative controls rejected; SciPy {scipy.__version__}.')
'@ | python -
```

It exited 0 with:

```text
PASS: 17090 independent endpoint-path evaluations; 4 additional negative controls rejected; SciPy 1.17.1.
```

This later audit changes neither the internal-only review classification nor
the stated limits of the bounded computational evidence.
