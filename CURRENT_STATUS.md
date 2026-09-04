# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=32f97d2b3bf37aa1603df02a6e44af17a2b98bba
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__finite_induced_subset_dominance
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Prove or refute finite terminal dominance for every induced subset, then
determine the sharp consequence for arbitrary subset sequences with no
shape, endpoint, component-count, or cardinality-limit assumption.

The exact finite theorem is

```text
R_chain(Supnick(S))<=R_chain(Supnick({n-|S|+1,...,n})),
```

with equality exactly for the terminal subset. The proof is the
rank-coordinate bound, the common Supnick rank-edge multiset, strict angular
monotonicity, and decreasing-root transfer.

For every arbitrary sequence `S_n subset {1,...,n}`, `|S_n|>=3`, the proved
terminal triangular-array limit and compactness give

```text
limsup R_chain(Supnick(S_n))/n^2<=C_term.
```

The finite envelope over all subsets is attained among terminal subsets and
converges to `C_term`, so the coefficient is sharp for the one-subset chain
mechanism.

Authoritative proof:
`research/FINITE_INDUCED_SUBSET_DOMINANCE.md`.

### Allowed delta

The new authoritative proof note; narrow limitation cross-references in the
two earlier induced-subset notes; this file, `PROJECT_KNOWLEDGE.md`, the
roadmap, and `ops/TASK-20260904__finite_induced_subset_dominance/`.

### Verification gates

- Exact finite dominance and equality proof: complete.
- Terminal triangular-array proof: complete for interior cardinality ratios
  and both boundary regimes.
- Arbitrary no-limit sequence and finite-envelope compactness: complete.
- Task-local finite enumerator: pass for all 3797 subsets with `3<=n<=11`.
- Accepted rank/parity and terminal-optimization dependency checks: pass.
- Complete five-modification/five-addition diff, strict text/whitespace,
  empty index, and protected-path checks: pass.

### Blockers and limitations

No mathematical blocker identified. The conclusion covers one selected
induced-subset chain bound at each `n`, and any pointwise maximum of such
individual bounds. It does not cover a genuinely coupled method that combines
constraints from several subsets, `R_full`, matching upper bounds, or the
true Ringmin leading asymptotics.

The arXiv-v1 paper/assets, production code, search, tests, `verify.py`,
results, finite certificates, and unrelated proof notes/dossiers are
protected. The recorded finite global certification scope remains
`3<=n<=14`.

## Exactly one next atomic task after acceptance

Independently review the rank-edge convention, strict equality case,
decreasing-root direction, terminal limit at cardinality ratios zero and
one, compactness/envelope proof, and coupled-method limitation; record
acceptance or precise corrections.
