# Evidence

## Environment

```text
repository_head=2ea596414dd582b8ebf810983c96a0f4883ac4f0
platform=Windows PowerShell sandbox
python=3.14.3
mpmath=1.3.0 (opt-in diagnostics only)
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `140<T_{7,33}` and `T_{7,34}<140` | exact theorem (endpoint lemma) | positive pre-square gates and exact rational square margins in `research/RADIUS7_SEAM_ONSET.md` | three independent derivations and exact checker | formal Descartes seam threshold only |
| `R_{7,33}<140<R_{7,34}` | exact theorem (endpoint lemma) | complete 27/28-edge tables, strict termwise arcsine bounds, and exact `pi` bridges | all rows and totals independently generated; checker audit | adjacent-chain roots only |
| `Delta_{7,n}>0` for `9<=n<=33` and `<0` for every `n>=34`; hence `s_7=34` | exact theorem, post-arXiv-v1 | endpoint lemmas plus the existing fixed-`k` sign/monotonicity/persistence theorem | two adversarial file reviews; exact checker corroboration | formal seam `(n,7,n-1)` only; no full/global/floating claim |
| High-precision root/threshold/deficit values | numerical observation | opt-in mpmath scan at 60/100 digits | precision comparison | diagnostic only; no finite scan proves the all-`n` claim |
| Checker exact path is stdlib/`Fraction`-only and production-independent | engineering fact | optimized/no-site run, AST audit, and separate production comparison | yes | checker corroborates endpoint arithmetic; it does not reprove the imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin status --short` | exit `0`; no paths | clean startup tree after the sandbox ownership workaround | mathematical correctness |
| independent `Fraction` derivations | exact thresholds, all 55 row margins, totals, and root directions agreed | endpoint arithmetic before implementation | the imported fixed-`k` theorem |
| `python -B ops/TASK-20260805__radius7_seam_onset/check_seam.py --order-stop 250` | exit `0`; `180182` explicit gates; diagnostics skipped | exact table transcriptions, parity formulas, sign/square/domain margins, rational totals, and `pi` identities | a proof of the imported fixed-`k` theorem |
| `python -B -O -S ops/TASK-20260805__radius7_seam_onset/check_seam.py --order-stop 250` | exit `0`; identical `180182` gates and output | optimization-safe explicit gates and stdlib-only exact default path | numerical diagnostics |
| `python -B ops/TASK-20260805__radius7_seam_onset/check_seam.py --order-stop 250 --diagnostics --start 9 --stop 120 --digits 60 --stability-digits 100` | exit `0`; `NUMERICAL_DIAGNOSTIC_ONLY`; max relative root delta `4.9137935e-46`, max absolute deficit delta `5.013963e-47` | finite sign/domain/monotonicity/precision checks and separator closure signs | exact endpoint proof or all-`n` certification |
| external task-local/production convention comparison, `n=9..250` | exit `0`; `484` comparisons | exact equality with production `supnick_max_tour` and cyclic equivalence with `interleave` | mathematical optimality of Supnick's theorem |
| AST/source audit | exit `0`; zero `assert`, float literals, `ringmin` imports, and top-level `mpmath` imports; one lazy `mpmath` import | exact-source literals, gate persistence, dependency separation | dynamic behavior by itself |
| in-memory corrupted-upper-margin and zero-lower-bound mutations | exit `0`; both intended `AuditFailure` gates caught | corrupted arithmetic and lost strictness are rejected | every possible tamper |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 33.90s` | repository regression suite without changing tests | the new all-`n` proof or global frontier certification |
| independent mathematical and engineering reviews | detailed `PASS`; all 55 rows, thresholds, totals, `pi` identities, quantifiers, checker modes, CLI gates, and representative mutations rechecked | adversarial mathematical and implementation scrutiny | hosted CI |
| direct eight-file format audit | exit `0`; strict UTF-8/no BOM, LF-only, one final LF, no trailing whitespace | tracked and untracked text integrity | mathematical correctness |
| `git -c safe.directory=C:/Users/Falker/Desktop/Code/circle/ringmin diff --check` | exit `0`; no output | whitespace errors in the tracked diff | untracked additions, covered separately |
| protected-path status and task-directory audit | exit `0`; no protected paths; exactly four task files and zero directories | scope containment and generated-cache absence | hosted state |

The exact compact invocations for the two external source/convention audits
were:

```powershell
python -B -c "import importlib.util as u,sys; sys.path.insert(0,'src'); s=u.spec_from_file_location('radius7_check','ops/TASK-20260805__radius7_seam_onset/check_seam.py'); c=u.module_from_spec(s); s.loader.exec_module(c); from ringmin.patterns import interleave,supnick_max_tour; checks=[(c.shifted_supnick_tour(n)==supnick_max_tour(range(7,n+1)),c.cycle_equivalent(c.shifted_supnick_tour(n),interleave(range(7,n+1)))) for n in range(9,251)]; passed=sum(flag for pair in checks for flag in pair); print(f'production_convention_comparison=PASS n=9..250 comparisons={passed}'); raise SystemExit(passed!=484)"
```

```powershell
python -B -c "import ast,pathlib; p=pathlib.Path('ops/TASK-20260805__radius7_seam_onset/check_seam.py'); t=ast.parse(p.read_text(encoding='utf-8')); nodes=list(ast.walk(t)); a=sum(isinstance(n,ast.Assert) for n in nodes); f=sum(isinstance(n,ast.Constant) and isinstance(n.value,float) for n in nodes); r=sum((isinstance(n,ast.ImportFrom) and ((n.module or '')=='ringmin' or (n.module or '').startswith('ringmin.'))) or (isinstance(n,ast.Import) and any(x.name=='ringmin' or x.name.startswith('ringmin.') for x in n.names)) for n in nodes); tm=sum((isinstance(n,ast.ImportFrom) and ((n.module or '')=='mpmath' or (n.module or '').startswith('mpmath.'))) or (isinstance(n,ast.Import) and any(x.name=='mpmath' or x.name.startswith('mpmath.') for x in n.names)) for n in t.body); lm=sum(isinstance(n,ast.Import) and any(x.name=='mpmath' for x in n.names) for n in nodes); print(f'ast_source_audit=PASS assert_nodes={a} float_literals={f} ringmin_imports={r} top_level_mpmath_imports={tm} lazy_mpmath_imports={lm}'); raise SystemExit((a,f,r,tm,lm)!=(0,0,0,0,1))"
```

The mutation harness loaded the checker in memory, changed the first `n=33`
stored upper margin to `margin+1`, and required the `upper margin failed`
`AuditFailure`; after restoration it changed the first `n=34` lower bound to
zero with the corresponding square margin and required the `arcsine domain
failed` gate. Both corruptions were rejected; no file was written.

## Artifact and provenance checks

- artifact path: not applicable; this task changes no result or certificate artifact;
- generating source/command: not applicable;
- input/version: `research/FIXED_K_SUPNICK_SEAM.md` at task-base `HEAD`;
- generation commit: not applicable;
- schema/hash: not applicable;
- independent verifier: task-local stdlib/`Fraction` exact checker rerun in
  normal and optimized/no-site modes;
- reproducibility limitation: the checker corroborates only the new endpoint
  arithmetic and intentionally does not reprove the imported persistence
  theorem; mpmath is needed only for opt-in diagnostics.

## Failed checks and negative evidence

- The first combined startup read ended with `git status --short` exit `128`
  because Git rejected the sandbox account's repository ownership. A scoped
  per-invocation `-c safe.directory=...` rerun returned exit `0` and a clean
  tree; no Git configuration or repository state was changed.
- Floating-point roots and deficits were used only after the exact bridge was
  complete and remain diagnostic rather than premises of the conclusion.
- No counterexample or sign disagreement was found in three independent
  endpoint reconstructions.
- One ignored `__pycache__` directory created by independent module loading
  was found in the task directory and removed. It contained only regenerable
  checker bytecode and was never part of the intended delta.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths, comprising three tracked modifications and five untracked additions;
- complete tracked diff inspected: yes, including final durable-memory state;
- untracked additions inspected directly: all five read in full; the proof and
  checker also received two separate adversarial reviews;
- direct format check: all eight paths are strict UTF-8 without BOM, LF-only,
  have exactly one final LF, and contain no trailing whitespace;
- `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none under `src/`, `tests/`,
  `scripts/`, `results/`, `verify.py`, `paper_assets/`, or the imported
  theorem;
- generated files unexpectedly changed: none; the detected review-time
  `__pycache__` was removed and the task directory has exactly four files.

## Residual uncertainty

The exact theorem intentionally depends on
`research/FIXED_K_SUPNICK_SEAM.md`; the task-local checker does not reprove
that source. A positive formal seam deficit is not full feasibility, and a
negative one says nothing about a replacement chain or global optimum.
Hosted CI, `verify.py`, certificate frontiers, and paper builds are unrelated
to this delta and will not be run.
