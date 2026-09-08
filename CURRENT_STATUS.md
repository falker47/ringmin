# Current Status

## Repository snapshot

    repository=falker47/ringmin
    task_base_head=f03f6267ea98cf5c3a709595721ec322114c405b
    observed_on=2026-09-09
    phase=post-arXiv-v1 active research

## Current task

    task=TASK-20260909__coupled_terminal_scale
    mode=STRICT
    state=READY_FOR_REVIEW

### Objective and current result

Resolve the asymptotic scale of the one-level coupled-terminal gain.
The analytic proof in research/COUPLED_TERMINAL_ONE_LEVEL_ASYMPTOTICS.md
proves 0<=G_{k,n}<=n/2 for all k>=1,n>=k+3, and G_{k,n}=0 for
n>=48k(k+1)^2. The sufficient cutoffs are 192 for k=1 and 864 for k=2.
The existing finite strict gaps remain unchanged. This mechanism cannot
affect the leading quadratic lower-bound coefficient.

### Allowed delta

Eight paths: new canonical proof; scoped STRICT dossier with one standalone
bounded checker; global-bounds ledger; this file; roadmap. Initial tree
clean at the base HEAD above. Only the global-bounds ledger owns the new
stable theorem. The compact index needs no change.

### Verification gates

- Analytic proof complete; symbolic radial/endpoint/elasticity identities
  pass with SymPy 1.14.0. Both comparison tours are explicit.
- Bounded exact checker passes 512 cyclic cases and 64 rational cutoff
  substitutions. All ten prescribed diagnostics and the unchanged eight
  finite-counterexample rational gates pass; numerics remain diagnostic.
- Complete new sources and tracked diff inspected. The eight-path audit
  passes tracked/untracked whitespace, links, sole ownership, isolated
  imports and nine protected source comparisons. git diff --check exits 0.
- Final record edits are inspected/restaged before authorized commit and
  normal origin/main push; the final handoff records actual SHA/push/tree.
- Independent acceptance and hosted CI remain separate.

### Blockers and limitations

No blocker. Supnick optimality and the terminal-array limit are imported.
The sufficient cutoffs and linear bound are not sharp; intermediate
finite equality cases and more general coupling remain unresolved. No
all-pairs feasibility, global optimum, new coefficient or certificate
is claimed. No third-block upper-bound work or paper revision is included.

Protected: previous proofs/dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, README.md, REPORT.md, publication metadata and CI;
other knowledge modules, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md.

## Exactly one next atomic task

Independently review the one-level gain theorem at committed HEAD: cyclic
deletion/insertion, integrated closure derivative, degree-count root bound,
strict cutoff comparison, both parities and fixed/moving-k corollaries.
Reproduce the standalone checker and record acceptance or corrections;
stop before new coupling research, certification or upper constructions.
