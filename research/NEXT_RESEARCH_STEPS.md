# Ringmin — Next Research Steps

## Role of this file

This is the sole ranked research roadmap. It records priorities and success criteria, not proofs, task chronology, or current task state.

The public arXiv-v1 paper already supplies:

- the angular reformulation;
- the anti-Monge/Supnick solution of the chain-ordering problem;
- a full all-pairs STN formulation;
- finite global certificates for `3 <= n <= 14`;
- explicit conjectures on seam failures, the floating cascade, and asymptotics.

The first three precise transitions and the general fixed-radius persistence
mechanism have now been converted into exact theorems. The next work should
reuse that architecture for the finite endpoint bridge at radius `4`, without
repeating the monotonicity proof or expanding experiments or certification
range.

## Resolved Priority 1 — First all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_n*` be the chain-optimal Supnick cyclic order on `{1,...,n}`, and let

```text
R_n = R_chain(sigma_n*).
```

The theorem now proved is:

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

for every integer `n >= 8`.

The reverse strict inequality holds for `3<=n<=7`, so the exact onset is `n=8`. The proof is in `research/RADIUS1_SEAM_OBSTRUCTION.md`. It compares strictly increasing chain roots with strictly decreasing explicit Descartes thresholds and closes `n=7,8` by rational inequalities. The raw angular deficit itself is not monotone.

This result concerns only the formal Supnick seam; it does not establish a global optimum or universal floating behavior.

## Resolved Priority 1 — Radius-2 all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_{2,n}*` be the chain-optimal Supnick cyclic order on `{2,...,n}`
and let

```text
R_{2,n} = R_chain(sigma_{2,n}*).
```

The theorem now proved is

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    > theta_{R_{2,n}}(n,n-1)       for 4 <= n <= 12,

theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)       for every n >= 13.
```

The proof is in `research/RADIUS2_SEAM_THRESHOLD.md`. It derives the shifted
Supnick convention and closure sums, proves that the implicit roots increase,
identifies the exact radius-2 threshold domain `n>=9`, proves that the
threshold decreases, and closes `n=12,13` by rational inequalities. The raw
angular deficit is not monotone.

This result concerns only the formal shifted Supnick seam; it does not
establish a global optimum or floating behavior.

## Resolved Priority 1 — General fixed-radius seam persistence

**Status:** proved after arXiv v1.

For every fixed integer `k>=1`, the canonical chain-minimizing Supnick order
on `{k,...,n}` has `n-1,n` as the neighbors of `k`. Its chain root
`R_{k,n}` strictly increases to infinity. The seam comparison has an exact
positive Descartes-threshold domain `n>=4k+1`, with

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))),
T_{k,n} = 1/kappa_{k,n}.
```

The thresholds strictly decrease to `k`, so `R_{k,n}-T_{k,n}` strictly
increases to infinity. Therefore every fixed radius has a finite first strict
seam obstruction, the obstruction persists thereafter, and equality can
occur at most once. The theorem does not determine the exact onset for
`k>=3` and makes no global-optimum or floating-circle claim.

The proof is in `research/FIXED_K_SUPNICK_SEAM.md`. The exact `k=1,2,3`
onsets follow by combining it with the endpoint bridges in the three
specialized proof notes.

## Resolved Priority 1 — Radius-3 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{3,...,n}`, with
`R_{3,n}=R_chain(sigma*_{3,n})`, the exact classification is

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17.
```

Thus `s_3=17`. The proof in `research/RADIUS3_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.
```

The threshold inequalities are rational square comparisons. The chain
inequalities use rational termwise bounds on every arcsine argument and
elementary strict bounds with exact margins. Finite high-precision roots are
diagnostic only. The result concerns one formal seam and makes no claim about
`R*(n)`, full feasibility, or floating circles in global optima.

## Priority 1 — Radius-4 all-`n` seam obstruction

The next atomic target is the exact finite onset on `{4,...,n}`. Let
`R_{4,n}=R_chain(sigma*_{4,n})`. The existing independent finite diagnostic
suggests, but does not prove, the classification

```text
theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    > theta_{R_{4,n}}(n,n-1)       for 6 <= n <= 20,

theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    < theta_{R_{4,n}}(n,n-1)       for every n >= 21.
```

The general theorem already supplies the no-threshold range `6<=n<=16`, the
positive threshold domain `n>=17`, opposing monotonicities, and persistence.
Prove or refute only the missing exact endpoint bridge at `n=20,21`, finding
a rational separator or isolating the one explicit inequality that fails.
A finite scan remains diagnostic, and the result must stay confined to the
formal radius-4 seam.

Expected value: one bounded endpoint theorem extending the exact onset
sequence without guessing a general formula from finitely many radii.

## Deferred priority 2 — Rigorous leading asymptotics

Prove unconditional two-sided bounds sufficient to establish or refute

```text
R*(n) = n^2/8 * (1 + o(1)).
```

This requires controlling the full geometric problem, not only the chain sum, and must not assume the floating set is `o(n)` unless separately proved.

## Deferred priority 3 — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
