# Evidence

## Environment

```text
repository_head=f4d1f1bd671849101e23d95aa76bfd143910ee12
platform=Windows, PowerShell, Codex sandbox
python=3.14.3 (MSC v.1944 64 bit, AMD64)
dependency_source=standard library only; isolated Python with site disabled
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Shared crossing inequality with one E | Exact theorem | Proof Section 3 | Analytic; bounded coupling checks use no production code | External review pending |
| Continuum relaxation is necessary for common orders | Exact theorem | Proof Section 4, weak limits with atom-free marginals | Analytic | No converse/recovery or exact minimax |
| Uniform finite three-level bound | Exact theorem | Proof Sections 2, 3, 5; explicit floors and root sandwich | Imports specified stability proof only after hypothesis checks | n>=1000; cutoff not optimal |
| Global lower transfer | Proved corollary | Proof Section 5, deletion from every full feasible order | Analytic | No global normalized limit or upper construction |
| eta_3-eta_split>11/2000000000 | Exact strict comparison | Rational Taylor, integral and cubic gates | New checker imports no production/prior-checker modules | Bounded arithmetic is not a finite optimum certificate |
| Coupling and negative-control gates pass | Engineering fact / bounded exact arithmetic | 12 prescribed grid couplings and 3 negative controls | Independent of production and prior checkers | Not tour enumeration or proof of universal quantifiers |

## Commands and checks

All executions below are local in this task. No hosted CI result is claimed.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| git status --short | Rejected by dubious ownership | Initial environment check | Tree status was not available from this call |
| git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short | 0; no status paths | Clean startup tree | Warned that the user-level ignore file was unreadable |
| git with same command-local setting: rev-parse HEAD, branch --show-current, remote -v | 0; base above, main, origin=falker47/ringmin | Integration destination | No remote mutation |
| python -c environment and fixed midpoint diagnostic | 0; Python 3.14.3, q about 0.19502009, D_1 about 0.0005467, D_2 about 0.0024141 | Preliminary discriminator only | Floating output proves no comparison |
| python -I -S ops/TASK-20260911__optimized_midpoint_split/check_split.py | 0; all printed gates pass | Independently reproduced prior input enclosures, cubic coefficient and finite error | Not an external review of its analytic dependencies |
| python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py (first run) | 1 at initial D_1 display upper endpoint | Found incorrect drafted display rounding | No theorem constant was computed from that endpoint |
| python -I -S -c diagnostic loading the new checker only | 0; fraction interval displayed with Decimal | Located corrected D_1 display bracket | Decimal display is not used by exact gates |
| python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py (corrected run) | 0; exact output below | Parameters, both integrals, shared-measure accounting and positive gap | Not geometric certification or universal-proof automation |
| python -I -S -O ops/TASK-20260911__three_level_common_chain/check_three_level.py | 1; RuntimeError: This checker requires enabled assertions; omit -O. | Rejects disabled checks | Expected failure, not a failed mathematical gate |

Corrected checker output:

```text
PASS rational Taylor gates: tau, q, pi
PASS finite domain, floors, cutoff separation and scalar sign gates
PASS exact integral gates: both cutoffs, 80 terms and moving-q error
2.6023553183e-7 < eta_3 < 2.6023553184e-7
5.5513553e-9 < eta_3-eta_split < 5.5513554e-9
PASS finite transfer gates: A_3 < 2.593263; n >= 10^12
PASS 12 prescribed grid couplings: marginals, strips, shared energy, both parities
PASS negative controls: independent budgets, on-grid cutoff, missing separation
PASS all three-level checks; analytic proof supplies all-order quantifiers
```

Prior checker material output included
2.546841764900829732093748e-7 < eta_split <
2.546841764900829732093749e-7 and
2.592952349827745447477519 < A < 2.592952349827745447477520.

## Artifact and provenance checks

Not applicable to results/ or publication assets: none are regenerated.
The new proof and checker are source files; exact input intervals and term
counts are embedded in the checker. There are no random seeds, third-party
dependencies, production imports, saved-output inputs or new certificates.
The generation/review base is the HEAD above; the integration SHA is reported
in the task's final response to avoid embedding a self-referential commit.

## Failed checks and negative evidence

- The first D_1 display bracket was too low by its last digit. The true
  fraction interval starts 0.00054671287051631122720866093116. Corrected both
  displays and reran all new checks successfully; see append-only TASK_LOG.
- An equal-weight aggregation did not supply the discriminator. Independent
  single-cutoff envelopes still admit the old scalar crossing. The new
  weighted COMMON-energy inequality rules it out; see proof Section 6.
- Removing midpoint placement or cutoff separation invalidates intermediate
  inequalities, as exhibited by exact negative controls.

## Final diff inspection

- Complete new proof/checker/dossier content and tracked diff inspected.
  The analytic audit checks shared energy counting, stability hypotheses
  at beta_1, continuum weak limits, finite floors and geometric transfer.
- Inline `python -I -S -` source audit: exit 0. It compares git diff and
  untracked filenames to the explicit eight-path allowlist; checks final
  newlines, trailing whitespace and tabs on every file; resolves local
  Markdown links and their heading anchors; and parses checker imports.
  Output: `PASS scope audit: 8 expected paths, protected paths unchanged,
  one owning ledger`; `PASS explicit whitespace/newline audit: all 8 paths,
  including 5 untracked additions`; `PASS local link and anchor audit: 23
  links`; `PASS checker AST/import audit: fractions and math only`.
- `git diff --check`: exit 0, no errors. `git status --short`: only three
  expected tracked modifications and the new proof/dossier additions.
- No diff under paper_assets/, results/, src/, tests/, verify.py, README.md,
  REPORT.md, AGENTS.md or PROJECT_KNOWLEDGE.md, or any existing proof/checker.
  Their source contents need no regeneration or recertification for this task.
- Authorized path-specific `git add`: exit 0. Complete `git diff --cached`
  inspected (including a scoped reread where the combined output truncated).
  `git diff --cached --check`: exit 0. `git diff --exit-code`: exit 0,
  confirming the inspected working files equal the staged versions before
  this final evidence update. Only the eight authorized paths are staged.
- Authorized integration follows this handoff. The final response records
  actual commit, push and remaining tree state.

## Residual uncertainty

External mathematical acceptance and exact-SHA hosted CI remain unrecorded.
No minimizing tour, sharp three-level value, normalized limit, upper
construction or expanded certification is proved. The continuum feasible
set is a necessary relaxation only. Unit tests, verify.py frontier runs and
paper builds are not relevant to these proof/checker-only changes and were
not run; no claim is made about their current outcomes.
