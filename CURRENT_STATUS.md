# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=22bc88834c38421efba068fd573206dae3bdb07b
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__optimized_terminal_subset_bound
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and exact outcome

Generalize and optimize the induced terminal-subset asymptotic lower bound.
**Exact theorem / proved corollary:** for every integer sequence with
`k->infinity` and `n/k->lambda>1`,

```text
R_{k,n}/k^2 -> rho(lambda)
  = (2/pi) integral_1^((lambda+1)/2) sqrt(x(lambda+1-x)) dx.
```

If `tau` is the unique root of `tau=cos(tau)` in `(0,pi/2)`, then the
normalized coefficient is uniquely maximized at

```text
lambda_*=(1+sin(tau))/(1-sin(tau))=5.12767681049949...,
C_term=tau/(pi(1+sin(tau)))=0.1405690808452567...,
liminf_{n->infinity} R*(n)/n^2 >= C_term.
```

The decimals are independently bracketed diagnostics, not proof premises.
This is the best coefficient within the proportional terminal-subset
deletion family and strictly improves the former `lambda=4` bound `rho/16`.
The boundary coefficients are `0` as `lambda` decreases to `1` and `1/8`
as `lambda` tends to infinity.

Authoritative proof:
`research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md`.

### Allowed delta

The existing proof note, `PROJECT_KNOWLEDGE.md`, this file, the roadmap, and
`ops/TASK-20260904__optimized_terminal_subset_bound/`.

### Verification gates

- Analytic proof covers both exact Supnick edge parities and endpoints,
  moving-ratio Riemann sums, uniform denominator/arcsine errors, implicit-root
  bracketing, closed form, boundary behavior, unique optimization and the
  all-integer floor deduction.
- Task-local stdlib audit: exact rational root/coefficient brackets plus 894
  independent finite edge-set comparisons, exit 0.
- Separate SymPy audit: parity endpoint/count, integral, coefficient,
  derivative and boundary identities, exit 0.
- Complete tracked diff and all five untracked additions inspected. Exact
  four-modification/five-addition scope, UTF-8/LF/final-newline/whitespace,
  empty index, protected-path and `git diff --check` gates pass.

### Blockers and limitations

No mathematical blocker identified. Independent human proof review and
manual integration remain pending. The theorem does not determine the true
liminf or limsup, prove existence of a normalized limit, supply a matching
upper bound, optimize nonterminal or combined-subset methods, or imply any
floating-circle conclusion.

The arXiv-v1 paper/assets, production search, tests, scripts, `verify.py`,
results, finite certificates, and prior proof notes/dossiers are protected.
The recorded finite global certification scope remains `3<=n<=14`.

## Exactly one next atomic task after acceptance

Independently review the generalized terminal-subset limit, its parity and
uniform-error arguments, the analytic optimization, and the all-integer
deduction; record acceptance or precise corrections.
