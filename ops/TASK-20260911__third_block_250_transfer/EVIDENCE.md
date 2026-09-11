# Evidence

## Environment

```text
repository_head=d895d5592ea6422c404ffc85c5b1d36972bf146d
platform=Windows / PowerShell
python=Python 3.14.3
dependency_source=standard library only; isolated mode, site disabled
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Fixed 1/250 recovery, even root equality, odd squeeze/limits | exact theorem | new proof Sections 1-6 | checker independent of production; external review pending | imported parameter theorems |
| Improved global limsup | proved corollary | new proof Section 7 | follows from both parity constructions | no sharpness, global limit or optimum |
| Bounded identities/seams/root signs/all-pairs | exact finite arithmetic checks | checker output below | no project/old-checker imports | finite samples do not prove all-m quantifiers |

## Commands and checks

All checks here were run locally in this task. No copied historical output
is presented as a current run. Commands are relative to the repository root.
The portable PowerShell Git prefix used for the final checks was:

```powershell
$ringminRoot = (Get-Location).Path.Replace('\', '/')
```

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | runtime | other Python versions |
| `python -I -S ops/TASK-20260911__third_block_250_transfer/check_transfer.py` | final run 0; exact excerpts below | bounded identities, actual seams, panel bounds, deletion, root signs, both directed paths | all-m proof, imported parameter minima, global optimum |
| `python -I -S -O ops/TASK-20260911__third_block_250_transfer/check_transfer.py` | expected 1; `ERROR: assertions must be enabled` | refuses an assertion-disabled run | mathematical result |
| `python -I -S ops/TASK-20260908__third_block_width/check_width.py` | 0; excerpts below | independently reruns the accepted continuous comparison dependency | geometric transfer |
| Inline scope/import/link/whitespace audit via `python -I -S -` | 0; 9 files, 5 additions, 27 local links/anchors pass | explicit untracked-file whitespace, exact changed-path whitelist, protected ranges, AST imports | mathematical correctness |
| `git -c "safe.directory=$ringminRoot" diff --check` | 0; no output | tracked whitespace | untracked additions (separately checked) |
| `git -c "safe.directory=$ringminRoot" status --short` and full diff/direct source reads | 0; four tracked modifications and five additions in this task only | scope and complete source inspection | independent mathematical acceptance |

Final new-checker output (exact excerpts):

```text
EXACT gates/floors/cells/panels/deletion: sizes=525 cases=614 cells=208182 seams=3063
EXACT root/all-pairs m=500 floors=(54,158,20) f=2 bracket=[141455168259/1000000,70727584131/500000]
EXACT root/all-pairs m=1000 floors=(109,318,42) f=4 bracket=[566736017443/1000000,283368008723/500000]
EXACT root/all-pairs m=1500 floors=(163,478,64) f=6 bracket=[159480517067/125000,1275844136539/1000000]
EXACT rational root brackets: even=17 retained_odd=15; width<=1/100000
EXACT directed all-pairs witnesses: unordered_pairs=28999561 detailed_angles=56088; both paths checked
EXACT negative controls rejected=6; integer interval scale=10^32 terms=64
PASS: bounded exact evidence only; all-m theorem and external review remain separate
```

The range is fixed in the source: m=2..512 plus 14 declared sizes through
2501 for combinatorics, and 14 declared root sizes through 1500. All
strict-bracket-compatible floors are overcovered; they are not numerical
estimates of the implicit parameters. Larger-radius universal angular
bounds discharge long paths; 56,088 near-path angles get individual exact
enclosures. Both paths are tested for every counted unordered pair, in
both even and deleted odd witnesses. This is polynomial bounded work on
one explicit family, with no tour search or width search.

The 60-step float bisection proposes rational endpoints only. Exact integer
arithmetic proves S(lower)>2*pi>S(upper), or the analogous retained score.
Square roots are enclosed with isqrt, arctangents use range reduction and
64 alternating-series terms with signed remainder, and Machin's identity
encloses pi. The placement uses rational angles and leaves the final cyclic
gap equal to exact 2*pi minus their total. Direct angular inequalities
therefore certify the upper-radius witnesses without floating tolerances.
They are not certificates at a rounded root or certificates of global
optimality. Cartesian non-overlap follows analytically by the cosine law;
no separate Cartesian floating diagnostic is claimed.

The six rejection controls are: lost binding chord (direct all-pairs
failure), duplicate high, merged second/third reflection, false shared
predecessor preserving the high multiset, m=1, and an odd block length.
The exact finite-onset assertion initially failed and was corrected as
recorded below. A complete passing run preceded the final run; the final
rerun followed added exact Machin and angular-error identity checks and
had the same reported counts. No later checker code change was made.

Continuous-width dependency rerun, exact excerpts:

```text
PASS 24 raw full-max/closed-cost and Leibniz/closed-derivative enclosures
PASS 120 new-slab reflection moments; 24 high partitions; 8 chain/tie endpoint controls
EXACT raw old-minus-new lower = 283676612415711588261712186381902839/160000000000000000000000000000000000000000000
PASS independent saving >1/576000000; cost saving >1/9216000000 via pi<4
PASS 5 radical sign/tie controls; zero inverse sine; 6 invalid inputs
```

Production pytest, verify.py (including frontier verification) and paper
builds were not run: no production, verification, result or publication
file changed, and those suites do not check this new analytic transfer.
No production-coupled check is substituted for the standalone arithmetic
checks. The all-m theorem comes from the new proof, using the inspected
arbitrary-high criterion and audited width-independent error arguments.

## Artifact and provenance checks

No result/certificate/publication artifact generated. New proof and checker
are source files committed together with this dossier; no random seed,
network input or parameter refinement is used. The exact rational bracket
excerpts above are audit evidence, not result/certificate artifacts.

Final checker SHA-256:
`e95b5ff969727544443137f643615683f8abb16752d3842ae2d8daabb75213b1`.
The checker itself imports only fractions, itertools and math, confirmed by
AST inspection, and runs with `-I -S`; it does not read/write files, import
production/verify.py/previous checkers, or depend on installed packages.
Its interval algebra shares elementary identities with the analytic proof;
this independence is not a claim of an external proof review.

## Failed checks and negative evidence

- Initial plain git status: dubious ownership; remedied with per-command
  safe.directory. No global Git configuration mutation. Subsequent local
  Git reads warn that the sandbox cannot access the user's global ignore
  file, but return successful scoped results.
- Initial new-checker run exited 1 at the m=500 floor example. The draft
  hand calculation included a forbidden strict upper endpoint. Corrected
  d=20 at m=500 and unique d=42 at m=1000, with their example seams.
  General construction, seam formulas and theorem gates were unaffected.
- A documentation patch attempted delete/add of the same CURRENT_STATUS.md
  in one apply_patch call; the tool rejected the patch before applying it.
  Reissued as an ordinary update successfully. No source change was lost.

## Final diff inspection

- Directly read the complete new proof, checker and three dossier files;
  inspected all tracked diffs. Follow-up scoped reads covered output that
  had been truncated in a batched tool response.
- Explicit whitespace audit included all five untracked additions, final
  newline and no trailing spaces. Tracked diff check exited 0.
- Local Markdown links and heading anchors: 27 checked successfully.
- Changed-path whitelist: exactly nine task files; no incidental generated
  or protected changes. In the global ledger, the entire prefix before the
  old three-block global entry is byte-equivalent after newline decoding,
  protecting every lower-bound owning entry and prior construction. In the
  fixed-order ledger, the prefix before the variable-width entry is likewise
  unchanged. The new theorem has one fixed-order owner and one separate
  global-corollary owner; index/navigation scope did not require modification.
- Protected unchanged paths: AGENTS.md, PROJECT_KNOWLEDGE.md, all earlier
  proof notes/checkers/dossiers, src/, tests/, verify.py, results/,
  paper_assets/, README.md, REPORT.md, CI and publication metadata.
- Staging, staged whitespace/content review and authorized commit/normal
  push follow this precommit record. The final task response supplies the
  actual SHA, remote result and remaining working-tree state; this file
  does not pre-assert those later operations or hosted CI.

## Residual uncertainty

External independent mathematical review and exact-SHA hosted CI have not
been asserted. No finite optimum/certificate, sharp asymptotic endpoint,
global normalized limit or optimized width is claimed. Earlier parameter
definitions and brackets are imported, not re-proved by this checker.
