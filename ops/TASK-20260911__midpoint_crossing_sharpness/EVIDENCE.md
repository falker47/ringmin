# Evidence

## Environment

```text
repository_head=1917e106223b3b913d4a3b3fa344e455495ec9a3
platform=Windows / PowerShell
python=3.14.3
dependency_source=Python standard library only for the new checker
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Explicit cyclic family and exact E/K formulas | Exact theorem | Proof Section 11.5 | Direct finite algebra, no production imports | External mathematical review separate |
| No uniform K=O(E^alpha), alpha>2/3; no uniform little-o(E^(2/3)) | Proved corollary / disproved stronger bound | Exact family limit, combined with Section 11.3 | Analytic | Concerns K, not signed Delta |
| Bounded fixtures satisfy the formulas and exact marginals | Exact finite diagnostic / engineering fact | Standalone checker, exit 0 | Direct traversal scorer, no production imports | Does not prove the infinite theorem |

## Commands and checks

All checks below were run locally in this task, in PowerShell at the
repository root. Git uses command-local `safe.directory` for the repository
and `core.excludesFile=` for sandbox-account portability; neither setting
modifies configuration.

| Command/check | Exit/result | Checks | Does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | Local interpreter | Other environments |
| `python -I ops/TASK-20260911__midpoint_crossing_sharpness/check_crossing.py` | 0; output below | Exact rational q gates/floors; six prescribed base cycles and 18 relabeled orientations; both parities, cyclic wrap, exact degree/marginals/reflection symmetry and E/K identities | Infinite theorem, signed Delta, geometry or production code |
| `python -I -O ops/TASK-20260911__midpoint_crossing_sharpness/check_crossing.py` | 1, intentionally; `Do not run this assert-based diagnostic with -O` | Disabled assertions are rejected before diagnostics | Mathematical validity |
| One-off repository audit, PowerShell literal script piped to `python -I -` | 0; output below | Exact changed-path sets, preserved proof sections, all eight files' whitespace/EOF and local links | External mathematical acceptance |
| `git diff --check` (with the command-local settings above) | 0, no output | Tracked-diff whitespace | Untracked files; those were checked separately |
| `Get-FileHash -Algorithm SHA256 ops/TASK-20260911__midpoint_crossing_sharpness/check_crossing.py` | 0; hash below | Checker identity | Correctness by itself |

Checker material output (the first run and final run both exited 0):

```text
exact rational optimizer bracket: PASS
m=40, n=1600, k=312, N=1289: n^3*E=257288, 2*n^2*K=6322, crossings=158 PASS
m=50, n=2500, k=487, N=2014: n^3*E=502012, 2*n^2*K=9902, crossings=198 PASS
m=60, n=3600, k=702, N=2899: n^3*E=866898, 2*n^2*K=14282, crossings=238 PASS
m=80, n=6400, k=1248, N=5153: n^3*E=2053152, 2*n^2*K=25442, crossings=318 PASS
m=100, n=10000, k=1950, N=8051: n^3*E=4008050, 2*n^2*K=39802, crossings=398 PASS
m=120, n=14400, k=2808, N=11593: n^3*E=6923592, 2*n^2*K=57362, crossings=478 PASS
exact floors and base cycles: 6; both N parities PASS
relabeled cycles: 18 orientations; degree, both marginals, reflection symmetry, wrap, E/K formulas and bounds PASS
No tour enumeration; finite diagnostics only, not the all-n proof.
```

The repository audit compared `git diff --name-only HEAD` with the four
intended tracked modifications and `git ls-files --others --exclude-standard`
with the four dossier additions. It compared `git show HEAD:` proof text
with working text (newline normalized): prefix through Section 10,
Sections 11.1-11.4 and the entire Section 12 suffix. It checked final
newlines, no trailing spaces/tabs or extra EOF blank line, and resolved
Markdown local paths and heading anchors in all seven changed Markdown
files. Material output:

```text
final scope: 4 tracked modifications, 4 new dossier files; 462 other tracked paths unchanged PASS
original proof Sections 1-10, 11.1-11.4 and 12 unchanged PASS
whitespace/EOF: 8 files; local links/anchors: 33 PASS
```

Production pytest, the certificate verifier, previous minimax checkers,
paper builds and hosted CI were not run: this task changes no corresponding
code, artifact or theorem premise. The diagnostic scorer uses the written
rank construction but independently sums actual edges rather than computing
E/K from the proposed formulas. The all-family justification remains the
analytic proof, whose parity and crossing cases were directly inspected.

## Artifact and provenance checks

Not applicable: no result, certificate, generated publication asset or
production code is regenerated. The new source checker uses fixed finite
inputs, exact arithmetic and no random seed or external data.

Final checker SHA-256:
`951c51616b3c0cc41592cfb8106192dc66a23c01a27daac6ce6183916724b471`.
Its complete source and fixed fixtures are committed with the proof; the
generation base is the repository HEAD recorded above. No generated result
file is used to support the theorem.

## Failed checks and negative evidence

Initial plain Git status failed on sandbox/repository ownership mismatch.
Command-local `safe.directory` resolves it. `core.excludesFile=NUL` was
rejected by Git; an empty command-local excludes setting is used instead.
The stronger K bound is disproved analytically, not rejected by tour search.
One combined delete/add patch was rejected before writes because it targeted
current status twice; an in-place update succeeded. Checker review caught
an ineffective assert-based -O guard before handoff; the final explicit
rejection was independently exercised. No mathematical checker failed.

## Final diff inspection

- `git status --short`: exactly four intended tracked modifications and the
  new task directory (four inspected files), no unrelated changes.
- Complete tracked diff inspected; every new file read in full; explicit
  direct whitespace/EOF audit includes untracked files.
- `git diff --check`: exit 0, no output; 33 local links/anchors pass.
- All 462 other tracked paths unchanged, including `paper_assets/`,
  `results/`, `src/`, `tests/`, `verify.py`, the compact index and all other
  thematic ledgers. Section 12's coefficients and proof are unchanged.
- No incidental protected or generated-file changes and no duplicate
  thematic claim owner. Exactly one next task is independent review.
- This is the precommit evidence snapshot. Final staged diff/whitespace
  inspection, commit, normal push and remote/clean-tree verification follow
  this record; the final response supplies the SHA and push outcome.

## Residual uncertainty

No claim about sharpness of the signed deletion discrepancy, optimal
multiplicative constant, full geometric realizability at the chain root,
new global coefficient or expanded finite certification. Local diagnostics
are not external acceptance or an inspected hosted CI run.
