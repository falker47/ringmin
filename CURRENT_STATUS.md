# Current Status

## Repository snapshot

    repository=falker47/ringmin
    task_base_head=3c415b36ade354cfd9beff637ec98bb5cc6b7d0a
    observed_on=2026-09-09
    phase=post-arXiv-v1 active research

## Current task

    task=TASK-20260908__coupled_terminal_subsets
    mode=STRICT
    state=READY_FOR_REVIEW

### Objective and current result

Resolve the simplest two-terminal induced-subset minimax bound and redirect
research toward stronger lower bounds. The new analytic proof is
research/COUPLED_TERMINAL_SUBSETS.md: at n=M=8,N=7 the coupled bound
exceeds the maximum of separate Supnick minima by more than 1/6000.
Ambient size 8 is minimal. The proof also distinguishes the earlier
five/four-rank incompatibility from strict minimax separation.
If T_M must be proper in {1,...,n}, the minimal ambient example is
n=13,M=12,N=11, with a gap greater than 1/5000.

### Allowed delta

Eight paths: new canonical proof; STRICT dossier with one standalone exact
checker; global-bounds ledger; this file; roadmap. Initial tree clean at
the user-supplied accepted HEAD above. Only the global-bounds ledger owns
the new stable claim. The compact knowledge index needs no change.

### Verification gates

- Eight rational closure gates pass using both arcsine and independent
  arctangent formulas; exact pi bounds, gap constants and cyclic identities
  pass. No production imports, floating-point root or tour enumeration.
- Independent symbolic derivative identities and fresh radius-1/radius-2
  exact endpoint checks pass. Analytic proof covers all competing tours
  and every smaller ambient n under both inclusion conventions.
- Full source/protection audit passes: eight allowed paths, explicit
  tracked/untracked whitespace, eight rational table transcriptions, all
  local proof links, sole ledger owner, eight imported texts unchanged.
  Complete new sources and tracked diff inspected; git diff --check exits 0.
- Final record-only edits are inspected/restaged before authorized commit
  and normal origin/main push; final handoff records SHA/push/tree.
  Independent acceptance and hosted CI remain separate.

### Blockers and limitations

No blocker. The matrix-level classical Supnick theorem and accepted exact
triangle/seam results are imported. No exact value of either minimax, finite
geometric optimum, asymptotic gain, improved C_term or expanded certificate
is claimed. No third-block extension or Delta_* transfer was performed.

Protected: previous proofs/dossiers, paper_assets/, results/, src/, tests/,
scripts/, verify.py, README.md, REPORT.md, publication metadata and CI;
other knowledge modules, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md.

## Exactly one next atomic task

Independently review the coupled terminal-subset theorem at committed HEAD:
matrix perturbation and uniqueness, rational gates, derivative/root gap,
minimal ambient n and compatibility distinction. Reproduce its standalone
checker and record acceptance or corrections; stop before asymptotic
amplification, new subset optimization, certification or upper constructions.
