# Evidence

## Environment

```text
repository_head=0e09cf774aa11543e86887ccc2a6fb6b3563644e
platform=Windows / PowerShell
python=3.14.3
dependency_source=Python standard library only for the new checker
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence and limitation |
|---|---|---|---|
| Exact finite Delta formula and strict negative sign | Exact theorem | Research note Section 11.6, (39e)-(39g) and sign argument | Analytic deleted-vertex accounting; external review separate |
| Uniform two-term expansion and positive limit | Exact asymptotic theorem | Section 11.6, Taylor argument (39h) through (39d) | Uniform derivative bounds, actual floor and exact finite sums; no numerical premise |
| No stronger uniform exponent or little-o at exponent 2/3 | Proved corollary / disproved stronger bounds | Section 11.6 with Section 11.5 energy and existing upper envelope | Concerns signed costs; not a geometric or optimized-constant claim |
| Six fixtures satisfy radical/edge/defect identities and sign | Exact finite diagnostic / engineering fact | New standalone checker, exit 0 | Direct traversal scorer independent of local formula; no production or previous-checker imports; not the infinite proof |
| Displayed scaled remainders | Numerical observation with rational enclosures | Checker fixed sizes only | Does not establish uniformity by sampling |

## Commands and checks

All commands below were run locally in this task at the repository root,
using PowerShell. Git read commands use command-local `safe.directory`
for the repository root and `core.excludesFile=` for the sandbox account;
no configuration was modified. The checker uses isolated Python and only
its standard library.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | Interpreter | Other environments |
| `python -I ops/TASK-20260911__signed_discrepancy_family/check_signed_discrepancy.py` | 0; full output below | Actual floors, exact radical identity, all replacement edges, wrap, both N parities, defect sums, E, rational sign and coefficient enclosures | Infinite theorem, geometry, production or certificates |
| `python -I -O ops/TASK-20260911__signed_discrepancy_family/check_signed_discrepancy.py` | 1, intentionally; `Do not run this assert-based checker with -O` | Rejects disabled assertions | Mathematical truth |
| Direct analytic review of Section 11.6 | Passed | Normalization, seam, unchanged/shifted intervals, first variations, derivatives, finite sums, common compact domain, floor remainder, energy limit | External mathematical acceptance |
| One-off audit, literal PowerShell script piped to `python -I -` | 0; output below | Exact changed-path sets, preserved proof/ledger sections, eight files' whitespace and local links | Mathematical validity |
| `git diff --check` with the command-local settings above | 0; no output | Tracked whitespace | Untracked files, which the audit checks directly |
| `Get-FileHash -Algorithm SHA256 ops/TASK-20260911__signed_discrepancy_family/check_signed_discrepancy.py` | 0; hash below | Source identity | Correctness by itself |

Checker output:

```text
exact rational optimizer gates: PASS
exact limit enclosure: 0.203 < A_q/4^(2/3) < 0.204 PASS
m=40, n=1600, k=312, N=1289: exact identities/sign PASS; m^2*Delta~-0.525866075472, |Delta|/E^(2/3)~0.207993030758, m^4 remainder~-1.276073625668
m=50, n=2500, k=487, N=2014: exact identities/sign PASS; m^2*Delta~-0.522872163433, |Delta|/E^(2/3)~0.206947157000, m^4 remainder~-1.142206040518
m=80, n=6400, k=1248, N=5153: exact identities/sign PASS; m^2*Delta~-0.518628757609, |Delta|/E^(2/3)~0.205473506976, m^4 remainder~-1.237435199863
m=120, n=14400, k=2808, N=11593: exact identities/sign PASS; m^2*Delta~-0.516307172266, |Delta|/E^(2/3)~0.204667870962, m^4 remainder~-1.192381527113
m=200, n=40000, k=7800, N=32201: exact identities/sign PASS; m^2*Delta~-0.514482013107, |Delta|/E^(2/3)~0.204035471355, m^4 remainder~-1.059096249242
m=400, n=160000, k=31203, N=128798: exact identities/sign PASS; m^2*Delta~-0.513136439170, |Delta|/E^(2/3)~0.203570057890, m^4 remainder~-1.204430268189
6 actual floors; both N parities; 18 rotations/reversals: PASS
Full cyclic signed radical identity, induced replacement edges, wrap, defect sums, E and negative Delta: PASS
Remainder values are finite corroboration; no inference of a uniform bound or infinite theorem from these six sizes.
```

The six widths are fixed in source, with maximum n=160000. The scorer
constructs both full cycles before subtracting their radical edge sums
and the defining D_n sum. It compares the resulting integer constant and
signed radical coefficients to a separate local formula. No approximate
zero test is involved in that equality. It also recovers actual deletion
neighbors from the walk and compares removed/replacement edge sets,
including rotated and reversed written wraps, and checks all signed
integer defect sums. Exact integer square-root bounds at scale 10^60
enclose each displayed Delta and remainder; decimal formatting of their
midpoints and of |Delta|/E^(2/3) is observational. The limit bracket uses
exact rational inequalities after cubing, not decimal evaluation.

The one-off audit compares `git diff --name-only HEAD` and untracked
paths with the eight-path allowlist, then compares old/new proof text
and the owning ledger boundaries. It permits only two forward-reference
edits outside new Section 11.6, checks the entire Section 12 suffix
unchanged, directly checks every new file's whitespace/EOF and resolves
Markdown local paths and anchors. Output:

```text
scope: 4 tracked edits, 4 dossier additions; 466 other tracked paths unchanged PASS
original proof unchanged except two forward references; Section 12 identical PASS
sole owning ledger section changed; other thematic entries unchanged PASS
whitespace/EOF: 8 files; local links/anchors: 36 PASS
```

Production pytest, certificate verification, previous checkers, paper builds
and hosted CI were not run: no corresponding production logic, artifact,
coefficient or premise is changed. The prior Section 11.5 external review
is not represented as complete; the new checker corroborates its energy
identity as a dependency. External independent mathematical acceptance of
either theorem remains separate from all local checks listed here.

## Artifact and provenance checks

Not applicable to results/certificates/publication assets: none is
regenerated. Checker source and fixed inputs are committed with the proof;
the task starts from the base recorded above. No random seed, production
import or network dependency is used. There is no generated result file or finite-optimum
certificate. Final checker SHA-256:
`e205acffdf2e3d1c3566322c7fb38aae7aa83b417be35765ebed78c20cc9164c`.

## Failed checks and negative evidence

Initial plain Git calls failed on sandbox/repository ownership; the
command-local settings resolved this without changing configuration.
No mathematical checker failed. The -O rejection is an intentionally
exercised guard, not a theorem failure. The stronger signed bounds are
refuted analytically by the family, without a search over general tours.

## Final diff inspection

- Four intended tracked modifications and four new dossier files; the
  complete tracked diff and every new file were inspected in full.
- Direct whitespace/EOF check includes untracked files; `git diff --check`
  exits 0. Local links and anchors pass.
- All 466 other tracked paths are unchanged, including `paper_assets/`,
  `results/`, `src/`, `tests/`, `verify.py`, `PROJECT_KNOWLEDGE.md`,
  `AGENTS.md`, old checkers and all other thematic ledgers. Sections 1-10,
  11.1-11.4 and 12 are identical, and the Section 11.5 proof/formulas are
  identical apart from a forward reference to the new result.
- Only the existing common-chain ledger section owns the stable claim.
  No generated/protected file changed incidentally and no coefficient was
  altered. Current status and roadmap name exactly one next atomic task.
- This is the precommit evidence snapshot. Staged diff/whitespace inspection,
  authorized commit/normal push and remote/clean-tree verification follow
  this record; the final response supplies SHA and push outcome.

## Residual uncertainty

The family question is resolved analytically. The checker is bounded
corroboration, not an all-n computational certificate. No optimal
multiplicative constant, exact limit for |Delta|/e^(2/3), minimax tour,
geometric feasibility, new global coefficient, expanded finite certificate
or hosted CI result is asserted. External mathematical acceptance remains
separate; the handoff state is READY_FOR_REVIEW.
