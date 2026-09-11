# Evidence

## Environment

```text
repository_head=f78dac1e1521d3cbd9eea8ca4ab38a298a86413c
platform=Windows / PowerShell
python=3.14.3
dependency_source=standard library only, isolated -I -S
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Adjacent margins 1/50000 and 1/100000; all finite/stability gates for n>=100000 | Exact theorem | Proof Section 11.1, rational sufficient inequalities in checker | Independent of production and saved results | N is sufficient, not asserted minimal |
| Three D_i, F, eta_4, old eta_3 and total coefficient lie in stated intervals | Exact arithmetic support for theorem | Rational Taylor, integrated binomial series and explicit tails/moving-q errors | Standalone; same justified enclosure method as the dependency | No floating quadrature premise; no separate external review |
| eta_4>eta_3+1e-7 | Exact theorem | Strict rational interval subtraction, Section 11.2 | Old eta_3 recomputed from its definition | Not a sharp coefficient or a comparison of the two finite minimaxes |
| All-n finite bound, global liminf and strict finite gain for n>=10^8 | Proved corollary | Sections 7, 9 and 11.3; finite gates verified | Analytic full-feasible deletion | Bounded checker does not supply universal quantifiers |
| Unchanged witness fails the old n=1000 floor gate | Exact negative result | ell=(209,218,230), 9/1000<451/50000 | Direct rational calculation | Does not refute the eventual theorem |

## Commands and checks

Startup: `python --version` exited 0, `Python 3.14.3`.
Command-local safe.directory Git status exited 0 with no changed paths;
HEAD/branch/remote are recorded above and in TASK_LOG.md.

All runs below were executed locally in this task, using Python 3.14.3;
the checkers are independent of `src/ringmin` and `verify.py`. The two
existing checkers are run as separate processes, never imported by the new
checker. These are dependency reproductions by this agent, not an external
mathematical review or hosted CI.

| Exact command | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python -I -S ops/TASK-20260911__four_level_rational_witness/check_four_level.py` | 0, complete transcript below | Fixed witness, exact enclosures, sufficient all-n gates and strict comparison | Analytic theorem's universal quantifiers, global optima |
| `python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py` | 0, final `PASS all three-level checks; analytic proof supplies all-order quantifiers` | Reproduces parameter/integral gates, 12 prescribed couplings, parities and negative controls | External acceptance or independent theorem proof |
| `python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 0, final `PASS all finite shared-crossing checks; universal claims are analytic` | 48 prescribed measures, 16 tour/cutoff cases, exact 1/1250 counterexample and floor/scalar controls | Unbounded enumeration or all-order proof |
| `python -I -S -O ops/TASK-20260911__four_level_rational_witness/check_four_level.py` | 1, `RuntimeError: This checker requires enabled assertions; omit -O.` | Disabled proof assertions fail closed | Not a failure of the witness |

Exact successful transcript of the new checker:

```text
PASS rational Taylor gates: tau, q, pi
PASS all-n domain: N=100000; adjacent margins 1/50000, 1/100000
PASS finite boundary checks; negative control rejects n=1000
H=409/25000; sum(h_i^3)=289457303/500000000000000; L=72086/3125
0.00136820131190299899 < D_1 < 0.00136820131190299902
0.00196196296152142893 < D_2 < 0.00196196296152142896
0.00241410289623904894 < D_3 < 0.00241410289623904897
0.00002810723928353877 < F < 0.00002810723928353880
0.00000038785322987835 < eta_4 < 0.00000038785322987838
0.00000026023553183385 < eta_3 < 0.00000026023553183388
0.00000012761769804449 < eta_4-eta_3 < 0.00000012761769804452
0.00000002761769804449 < eta_4-eta_3-1e-7 < 0.00000002761769804452
0.14056946869848664490 < C_term+eta_4 < 0.14056946869848664493
2.59369407943386457250 < A_4 < 2.59369407943386457253
PASS strict improvement eta_4 > eta_3 + 1e-7
PASS finite strict transfer for n>=10^8
PASS fixed four-level witness; universal quantifiers use the proved corollary
```

The dependency three-level run reproduces
`2.6023553183e-7 < eta_3 < 2.6023553184e-7` and
`5.5513553e-9 < eta_3-eta_split < 5.5513554e-9`.
The general checker's exact integrated negative control again gives
`177/2500 > 7/100; excess 1/1250`.

The production unit suite and finite-certificate verifier were not run:
no solver, test, verifier, certificate or generation logic changes. They
would not validate this analytic theorem. No paper build was needed.

## Artifact and provenance checks

Not applicable: no solver output, certificate or publication asset generated.
The fixed user inputs and exact arithmetic algorithm live in the checker;
its transcript is recorded above. No machine paths are proof inputs.

## Failed checks and negative evidence

The initial Git ownership refusal and corrected preliminary separation
calculation are retained in TASK_LOG.md. The first checker run exited 1
only at an auxiliary draft bound `A_4 < 2.593694`; the exact value is above
it. The valid conservative bound is `A_4 < 2.594`. This did not alter the
witness, comparison threshold or any stability constant. The requested
strict margin had already passed in that run. The next run passed all gates
with finite strict threshold 10^13; after inspecting the exact residual,
the final run proved the stronger round threshold 10^8. No parameter
adjustment or search was made.

## Final diff inspection

- Full tracked diff inspected using command-local safe.directory
  `git diff -- CURRENT_STATUS.md research/NEXT_RESEARCH_STEPS.md
  knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md` and
  `git diff -- research/THREE_LEVEL_COMMON_CHAIN.md`; both exit 0.
- Every untracked addition inspected in full with `Get-Content`, including
  the entire checker and all three dossier files. Ordinary Git diff omits
  these additions, so a separate direct whitespace audit covered them.
- The relocatable command `python -I -S -c "import pathlib,subprocess; subprocess.run(['git','-c','safe.directory='+pathlib.Path.cwd().as_posix(),'diff','--check'],check=True)"`
  exited 0 with no output. The path is command context, not a proof input.
- A read-only inline Python audit via PowerShell stdin to `python -I -S -`
  exited 0 with the exact output below. It compared `git diff --name-only`
  plus `git ls-files --others --exclude-standard` with the eight explicitly
  authorized paths; checked trailing whitespace and final newlines; compared
  the proof prefix with `git show HEAD:research/THREE_LEVEL_COMMON_CHAIN.md`;
  resolved local Markdown paths/heading anchors; checked the AST has only
  `fractions`/`math` imports and no float literals; and reran the checker
  to compare its full transcript with this dossier and all ten decimal
  intervals with proof Section 11. No file was generated by this audit.

```text
PASS eight-path allowlist; direct whitespace includes all four untracked additions
PASS original proof Sections 1-10 preserved; protected paths unchanged
PASS 29 local Markdown links/anchors
PASS standalone imports; no floating literals
PASS 10 exact printed enclosures match proof; complete transcript matches evidence
```

- Protected-path scope check: no changes to `src/`, `tests/`, `verify.py`,
  `results/`, `paper_assets/`, `REPORT.md`, `README.md`, generation scripts,
  existing checkers, `AGENTS.md`, `PROJECT_KNOWLEDGE.md` or other ledgers.
  No generated files changed. The one new stable claim is owned only by
  the new four-level entry in GLOBAL_BOUNDS_ASYMPTOTICS.md; status and
  roadmap reference it rather than creating another thematic owner.
- Precommit handoff: staged diff/whitespace inspection and authorized normal
  commit/push follow this snapshot. The final task response records the
  resulting SHA, push result and remaining tree state. Hosted CI is not claimed.

## Residual uncertainty

Independent acceptance of this new result remains separate. No sharp
coefficient, normalized global limit, minimizing tour or expanded finite
certification is sought.
