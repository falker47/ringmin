# Current Status

## Repository snapshot

    repository=falker47/ringmin
    task_base_head=273662513c2816d10ce12a5ba821fe04bbfea5aa
    observed_on=2026-09-10
    phase=post-arXiv-v1 active research

## Current task

    task=TASK-20260910__deletion_exponent_sharpness
    mode=STRICT
    state=READY_FOR_REVIEW

### Objective and current result

Decide whether the accepted deletion estimate's square-root exponent is
sharp for actual common tours at the fixed q=q_* and beta=23/100.
Section 11 of research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md proves
|Delta|<=40*e^(2/3)+432*e uniformly for every n>=102 and every cyclic
order, with exactly the accepted e, J_n and D_n. Hence |Delta| is uniformly
o(sqrt(e)); no requested square-root-sharp tour family exists. The proof
uses exact reflected marginals, signed cancellation and midpoint strip
counts. This supports refining the two-level method. It does not establish
optimality of 2/3 or compute a new minimax/global coefficient.

### Allowed delta

Eight paths: append to the existing proof note, update its sole owning
global-bounds ledger, the research roadmap, this file, and add the task
dossier's TASK_STATUS.md, TASK_LOG.md, EVIDENCE.md and bounded
check_sharpness.py. The compact index
retains its scope, central guardrails, module ownership and navigation.

### Verification gates

- Local bounded checker passed (exit 0): exact q/domain/constant gates;
  twelve exact floor cases, sixty prescribed tours in 180 orientations,
  all four parity combinations, maximal runs and wrap, 360 strip checks.
- Eight independent symbolic identities and sixty direct-cost checks at
  each of 70 and 100 dps passed (exit 0); numerical output is not a premise.
- Analytic audit covers orientation factors, Hessian remainder, LL squared
  defects, exact marginal cancellation, cutoff jumps, submesh strips and
  uniformity in n with no additive error.
- Complete tracked/untracked audit passed (exit 0): eight paths, eleven
  proof links, 449 protected tracked paths unchanged, entire accepted proof
  preserved as a prefix, all additions explicitly checked for whitespace.
  Final records receive the same audit; staged inspection precedes authorized
  commit and normal origin/main push. The final handoff reports results and SHA.
- Independent external mathematical review and hosted CI remain separate.

### Blockers and limitations

No mathematical blocker. The improved exponent 2/3 is not asserted sharp.
No new scalar or global coefficient, geometric feasibility, normalized
limit, finite optimum certification, upper construction or paper revision.
The accepted input and global coefficients are preserved in full.

Protected: the entire accepted proof as a prefix; all other
proof notes and prior dossiers/checkers; other knowledge modules;
PROJECT_KNOWLEDGE.md; AGENTS.md; RINGMIN_REVIEW_PROTOCOL.md; paper_assets/;
results/; src/; tests/; scripts/; verify.py; README.md; REPORT.md;
publication metadata and CI.

## Exactly one next atomic task

Independently review Section 11's deletion exponent improvement at committed
HEAD. Reproduce the bounded checker and audit signed cancellation, midpoint
strip counts, maximal runs, wrap, floors, parities and uniform little-o.
Record acceptance or corrections without further exponent/constant or
minimax refinement, enumeration, additional coupling, certification or upper work.
