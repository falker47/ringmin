# Ringmin — Next Research Steps

## Role of this file

This is the sole ranked research roadmap. It records priorities and success criteria, not proofs, task chronology, or current task state.

The public arXiv-v1 paper already supplies:

- the angular reformulation;
- the anti-Monge/Supnick solution of the chain-ordering problem;
- a full all-pairs STN formulation;
- finite global certificates for `3 <= n <= 14`;
- explicit conjectures on seam failures, the floating cascade, and asymptotics.

The first precise conjectural transition has now been converted into an all-`n` theorem. The next work should test whether its comparison method survives the radius-2 seam before expanding experiments or certification range.

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

## Priority 1 — Radius-2 all-`n` seam obstruction

The next atomic target is the direct analogue on `{2,...,n}`. Let `sigma_{2,n}*` be the chain-optimal Supnick cyclic order on that set and let

```text
R_{2,n} = R_chain(sigma_{2,n}*).
```

Prove or refute, with an exact lower-side threshold check, that

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)
```

for every integer `n>=13`.

The task must establish the precise Supnick convention on `{2,...,n}`, derive the radius-2 Descartes threshold, determine whether the delete-largest monotonicity argument still supplies the needed comparison, and avoid assuming that the observed onset sequence `8,13,17,...` follows a closed form. It must preserve the distinction between a formal seam obstruction and floating behavior in global optima.

Expected value: a rigorous route toward the cascade conjecture.

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
