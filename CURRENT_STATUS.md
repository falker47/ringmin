# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=bbcdb0330dc080d619152074c6bbbf7d4980651c
observed_on=2026-09-05
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260905__reflected_prefix
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Generalize deterministic reflected-prefix recovery at the fixed alpha_* and
prove an explicit improvement over the 1/4 prefix. The proof establishes
the witness lambda=3/10, full-sequence recovery and a strict exact saving.
Authoritative proof: research/PERMUTED_HALVES_REFLECTED_PREFIX.md.
The fixed-order and global claims have distinct owners in the corresponding
knowledge ledgers. Independent external review remains pending.

### Allowed delta

The new proof note, knowledge/FIXED_ORDER_THEORY.md,
knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md, research/NEXT_RESEARCH_STEPS.md,
this file and ops/TASK-20260905__reflected_prefix/.

### Verification gates

- Canonical-dependency checker: exit 0; exact rational branch/sign/saving
  gates, 17423 finite (m,s,q) cases and 839207 predecessor cells.
- All seam counts, including 527 junction/endpoint coincidences, pass;
  4315 rational parameter tests cover 123407 ordinary coordinate pairs.
- 216 exact polynomial moment checks pass. Independent integral/primitive
  diagnostics include both block/tail branches and the switch boundary.
- Nine full roots have alternate-formula brackets; 1165 pair checks
  corroborate angular and Cartesian feasibility at selected small sizes.
- Final content and whitespace audit passed for all nine changed files:
  four tracked edits, five additions, five local links and six source hashes;
  staged diff empty and protected paths unchanged. git diff --check exit 0.
  Checker compilation/import audit passed; dependencies are canonical.

### Blockers and limitations

No blocker. Numerical diagnostics are not interval or global certificates;
the all-m recovery and strict improvement are analytic. Exact feasibility,
uniform root transfer and the alpha_* definition remain imported theorem
dependencies. No optimization of alpha or lambda, general recovery,
relaxation optimum, global optimality or normalized global limit is claimed.

Protected: previous proof notes and dossiers, paper_assets/, results/,
src/, tests/, scripts/, verify.py, publication metadata, README, REPORT,
other knowledge ledgers, PROJECT_KNOWLEDGE.md, AGENTS.md and
RINGMIN_REVIEW_PROTOCOL.md. No Git/GitHub state writes.

## Exactly one next atomic task

Independently review the longer reflected-prefix theorem: audit finite
occurrences and seams, continuous-test convergence, the full-cost branches,
the rational alpha/branch/saving gates, imported uniform root transfer and
deletion corollary. Reproduce the checker and record acceptance or precise
corrections without beginning parameter or permutation/coupling optimization.
