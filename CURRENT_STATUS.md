# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=0d2eef8702d19fd93982a495bc1aeea50f29a79a
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__induced_subset_asymptotic_bound
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Verify the induced-subset bound and its implication for the proposed
global asymptotic. **Exact theorem / proved corollary:**

```text
R*(n) >= R*({k,...,n}) >= R_{k,n},     k>=1,n>=k+2,
liminf_{n->infinity} R*(n)/n^2 >= rho/16 > 3/22 > 1/8.
```

The proof uses deletion, the published arbitrary-radii Supnick theorem,
the exact chain-root asymptotic and monotonicity with a floor index.
Full feasibility of the subset necklace is not needed. Both
`R*(n)=n^2/8 (1+o(1))` and `n^2/8-R*(n)=O(sqrt(n))` are disproved.
Authoritative proof: research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md.

### Allowed delta

The new proof note, PROJECT_KNOWLEDGE.md, this file, the roadmap, a minimal
README scope correction, and ops/TASK-20260904__induced_subset_asymptotic_bound/.

### Verification gates

- Analytic review covers the exact deletion/relaxation inequalities, both
  closure parities, uniform errors, root bracketing and all-integer liminf.
- Existing asymptotic audit rerun locally: exit 0, 68 explicit gates.
- Task-local exact arithmetic audit: exit 0, signed-remainder identities,
  rational margins and all four symbolic residues; no parameter scan.
- 80-digit constant-only sanity check: integral and closed form agree;
  numerical observation, not a proof premise.
- Complete four-file tracked diff and all five additions inspected.
  Nine-file scope/UTF-8 audit and complete untracked whitespace audit pass;
  git diff --check exits 0. HEAD, index and protected paths are unchanged.

### Blockers and limitations

No mathematical blocker identified. The true leading coefficient,
matching upper bounds, existence of a normalized limit and an explicit
eventual threshold remain unresolved. Independent human proof review
and manual integration are pending. No floating-set claim follows.

The arXiv-v1 paper/assets, production code, tests, verify.py, results and
prior proof notes/dossiers are protected. No enumeration, new certificate,
paper build or hosted CI check is required. The recorded finite global
certification scope remains 3<=n<=14.

## Exactly one next atomic task after acceptance

Independently review the induced-subset theorem, its Supnick/asymptotic
dependencies and the all-integer liminf deduction; record acceptance or
precise corrections. This review has not begun.
