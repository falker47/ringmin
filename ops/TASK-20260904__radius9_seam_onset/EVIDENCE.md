# Evidence

## Environment

```text
repository_head=2a3af790de73e1694cbb510245e14015f810e3b0
platform=Windows-11-10.0.26200-SP0; PowerShell; local Codex sandbox
python=3.14.3, MSC v.1944 64 bit (AMD64)
dependency_source=standard library only for exact proof/checker
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Four endpoint inequalities at 41,42,220 | Exact theorem | RADIUS9_SEAM_ONSET.md sections 2-6, complete rational tables | Checker independent of production/diagnostics; separate integer cross-products | Formal chain/seam only |
| s_9=42, positive deficit through 41 and negative from 42 onward | Proved corollary | Four gates plus fixed-k sections 1-5 | Mathematical deduction | Imported theorem, not a finite-scan extrapolation |
| Complete 33/34 edges, strict witnesses and guarded rejection | Engineering fact | Two constructions, 134 symmetry variants, 24 task-local tests | Integer scorer independent of checker arithmetic; rejection tests coupled | Tests are not a proof assistant or external review |
| Global optima beyond n=14 or floating of radius 9 | Unresolved claim | No new evidence from this task | Not applicable | No promotion |

## Commands and checks

- `python --version`: exit 0, `Python 3.14.3`.
- Read-only startup Git inspection: clean tree, HEAD above. Plain Git failed
  ownership checks; per-command safe-directory inspection succeeded.
- Inline `python -I -S -B -` exact preliminary calculation: exit 0;
  two endpoints, 33/34 parity edges, rational margins recorded in TASK_LOG.
  This preliminary computation alone does not verify the complete proof.

The commands below were executed locally from the repository root. All
script inputs are embedded exact integers/Fractions; no third-party
dependencies, numerical seeds or nondeterminism enter the endpoint audit.

| Exact command | Exit and material output | Property checked / limitation |
|---|---|---|
| `python -I -S -B ops/TASK-20260904__radius9_seam_onset/check_seam.py --tables` | Final run: 0, exact_bridge=PASS, inequalities=4, cyclic_edges=67, symmetry_variants=134; all 67 rows printed | Complete rational endpoint proof checks; imports fixed-k theorem mathematically |
| `python -I -S -O -B ops/TASK-20260904__radius9_seam_onset/check_seam.py` | 0, same exact output/margins | Gates survive disabled assert statements and isolated stdlib execution |
| `python -I -S -B ops/TASK-20260904__radius9_seam_onset/check_mutations.py` | Corrected run: 0; Ran 24 tests in 0.052s; OK | Complete note tables/tours, integer scorer, malformed/altered-witness rejection |
| `python -I -S -O -B ops/TASK-20260904__radius9_seam_onset/check_mutations.py` | 0; Ran 24 tests in 0.050s; OK | Same checks with optimization; not external review |
| `python -c "import platform,sys; print(platform.platform()); print(sys.version)"` | 0; platform/Python above | Environment provenance only |

Successful checker output (identical in normal and optimized modes):

```text
threshold n=41 A=2369/14760 B=1/41 A2-B=298561/217857600 H=25321/162360 directed_margin=1792559/26360769600
threshold n=42 A=823/5166 B=184/7749 A2-B=43633/26687556 H=87947/568260 directed_margin=66953209/322919427600
pi lower=281476/89625 margin=107/179250 upper=670143059704/213311234375 margin=1845738322/1493178640625
chain n=41 edges=33 upper_half_sum=194613679989/62500000000 margin=1636320011/62500000000
chain n=42 edges=34 lower_half_sum=32503/10000 margin=7521/70000
exact_bridge=PASS inequalities=4 cyclic_edges=67 symmetry_variants=134
corollary=s_9=42 using FIXED_K_SUPNICK_SEAM.md; scope=formal_seam_only
```

The 24 tests include 67 individual one-unit witness corruptions, the
original zero-margin candidate, missing closure, duplicate/invalid edges,
an alternative Hamiltonian cycle, invalid endpoint/domain/type/direction,
nonpositive curvature, pre-square zero/negative signs, threshold equality,
invalid pi/arcsine bounds and aggregate failure despite valid term bounds.

Not run: production pytest suite, global `verify.py` (including smoke mode),
paper build, hosted CI, or external reviewer. These unchanged components are
outside this delta; the task-local exact suite is the proportionate gate.

## Artifact and provenance checks

No global or publication artifact generated. Witnesses are embedded in the
checker and fully tabulated in the proof note. `check_seam.py --tables`
reproduces the tables; `check_mutations.py` independently reconstructs m_e
with integer isqrt and verifies table equality, every square margin and sum.
No production solver or prior diagnostic was used to construct the witnesses.

Base/generation source snapshot: `2a3af790de73e1694cbb510245e14015f810e3b0`
plus the uncommitted task files identified by these SHA-256 values. This is
not a claim that the new files already belong to that commit.

`Get-FileHash -Algorithm SHA256` on the four paths below returned exit 0:

| Path | SHA-256 |
|---|---|
| `research/FIXED_K_SUPNICK_SEAM.md` | `24eefee0f028fdf6b41a804aeca7eafcdebf2eca54306af9f98177ad36c23b71` |
| `research/RADIUS9_SEAM_ONSET.md` | `d4ea0074cc13ffa3295a0047b7ea9bb721fdb8a1d2e73ce7ea93419e606164c5` |
| `ops/TASK-20260904__radius9_seam_onset/check_seam.py` | `a52dcde671211c398515f7f027ec16ee2ff5bb1472528eb431d82f628c7acb0a` |
| `ops/TASK-20260904__radius9_seam_onset/check_mutations.py` | `a19d8f7d8020dbdb37aa56561686d6d71caf4cf669fddf3784f65b0b24a9b86e` |

## Failed checks and negative evidence

The first checker run exited 1 with `strict lower sine square margin`.
At n=42, edge (20,30), m=1000 gives exactly zero margin, so the initial
integer-floor witness was invalid as a strict lower bound. It was rejected
before any promotion. The repaired m=999 gives M_e=119940000>0 and the
final lower total above. This was a failed candidate witness, not a
counterexample to the four target inequalities. No failed witness is used.

First mutation run: 24 tests, two Markdown-parser failures, exit 1; all 22
other tests passed. Leading-blank table extraction and regex brace escaping
were corrected; both final runs pass. An intervening patch failed its log
context match and made no edit. The chronology preserves these failures.
Startup Git ownership/external-ignore limitations are recorded above.

## Final diff inspection

- Read-only `git status --short --untracked-files=all`: three modified
  tracked documents and six untracked additions, exactly the nine paths below.
- Complete `git diff` inspected for all three tracked documents; every
  untracked addition read in full with `Get-Content -LiteralPath` semantics.
- Inline stdlib audit (`python -I -S -B -`): exit 0. It compared the complete
  Git status path set with the nine-file allowlist, checked the exact five
  dossier filenames, UTF-8/LF, one final newline, zero trailing whitespace
  on every line of all nine files, recomputed all four hashes, checked HEAD,
  and ran `git diff --check`. It includes untracked files explicitly.
- Output: `delivery_audit=PASS files=9 untracked=6 hashes=4 protected_changes=0`;
  `format=UTF-8/LF final_newlines=PASS trailing_whitespace=0 HEAD=unchanged`.
- `git diff --check`: exit 0, no output. Read-only Git commands used the
  per-command safe-directory setting for the current repository root.
- Protected paths inspected through the complete change allowlist:
  `src/`, `tests/`, `verify.py`, `results/`, `paper_assets/`, generation
  scripts, CI/configuration, README/REPORT, AGENTS, earlier proof notes and
  dossiers. No protected or generated file changed.

Final changed paths:

```text
CURRENT_STATUS.md
PROJECT_KNOWLEDGE.md
research/NEXT_RESEARCH_STEPS.md
research/RADIUS9_SEAM_ONSET.md
ops/TASK-20260904__radius9_seam_onset/TASK_STATUS.md
ops/TASK-20260904__radius9_seam_onset/TASK_LOG.md
ops/TASK-20260904__radius9_seam_onset/EVIDENCE.md
ops/TASK-20260904__radius9_seam_onset/check_seam.py
ops/TASK-20260904__radius9_seam_onset/check_mutations.py
```

## Residual uncertainty

The all-integer deduction imports `research/FIXED_K_SUPNICK_SEAM.md`.
The checker is independent of production and diagnostics, not a proof
assistant or a new proof of the imported Supnick theorem.
The proof still awaits independent review and manual integration. No
geometric feasibility, global optimum, contact graph or floating-circle
conclusion is supplied. The unresolved radius-index range is 10<=k<4325.
