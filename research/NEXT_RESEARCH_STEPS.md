# Ringmin — Next Research Steps

## Role of this file

This is the sole ranked research roadmap. It records priorities and success criteria, not proofs, task chronology, or current task state.

The public arXiv-v1 paper already supplies:

- the angular reformulation;
- the anti-Monge/Supnick solution of the chain-ordering problem;
- a full all-pairs STN formulation;
- finite global certificates for `3 <= n <= 14`;
- explicit conjectures on seam failures, the floating cascade, and asymptotics.

The next work should convert one precise conjectural transition into an all-`n` theorem before expanding experiments or certification range.

## Priority 1 — Prove the first all-`n` seam obstruction

### Exact target

Let `sigma_n*` be the chain-optimal Supnick cyclic order on `{1,...,n}`, and let

```text
R_n = R_chain(sigma_n*).
```

Prove or refute:

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

for every integer `n >= 8`.

Equivalently, prove that the formal full Supnick necklace is geometrically unrealizable across the `(n,1,n-1)` seam for all `n >= 8`, while the threshold case below `8` remains correctly classified.

### Why this is first

- It is the first explicit missing monotonicity step in the paper’s open-problem list.
- It is a single falsifiable theorem, not the whole cascade.
- It separates a general mathematical obstruction from finite certification.
- A proof supplies the base pattern needed for the later radius-`k` cascade analysis.
- It is likely to yield more scientific value than extending local-search tables or immediately attempting factorial certification at `n=15`.

### Required deliverables

- a detailed proof note under `research/` with exact definitions and quantifiers;
- an explicit derivation of the Supnick seam and the dependence of `R_n` on `n`;
- a proof strategy that controls the implicit chain root, not only a numerical plot;
- exact or interval-safe handling of the finite threshold cases;
- a small independent high-precision checker used only to test intermediate inequalities and search for counterexamples;
- tests for that checker if it becomes reusable code;
- a clear status: proved, refuted with counterexample, or blocked at one named lemma;
- updates to `PROJECT_KNOWLEDGE.md` only if a stable conclusion is reached.

### Guardrails

- Do not assume monotonicity of `R_n`, normalized angles, or the seam deficit without proving it.
- Do not replace the theorem with verification up to a large finite `N`.
- Do not generalize to radius `k>1` in the same task.
- Do not modify certified artifacts, the paper, or heuristic result tables.
- Do not claim anything about the full optimum after proving only unrealizability of one candidate necklace.

### Useful decomposition candidates

These are hypotheses to test, not established facts:

1. express the chain closure for the Supnick tour as an explicit finite sum whose adjacent pairs have a controlled pattern;
2. obtain monotone upper/lower bounds for the implicit root `R_n`;
3. normalize by `n^2` and derive a seam-deficit comparison uniform for `n >= N_0`;
4. close the remaining finite interval exactly or with certified intervals;
5. inspect whether the raw seam deficit itself is monotone, or whether only a comparison bound is.

## Deferred priority 2 — General seam failure for radius `k`

After Priority 1 is resolved, formulate and test an exact analogue for the Supnick tour on `{k,...,n}`. The task must identify the correct seam neighbors and avoid assuming that the onset sequence `8,13,17,...` follows a simple closed form.

Expected value: a rigorous route toward the cascade conjecture.

## Deferred priority 3 — Rigorous leading asymptotics

Prove unconditional two-sided bounds sufficient to establish or refute

```text
R*(n) = n^2/8 * (1 + o(1)).
```

This requires controlling the full geometric problem, not only the chain sum, and must not assume the floating set is `o(n)` unless separately proved.

## Deferred priority 4 — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
