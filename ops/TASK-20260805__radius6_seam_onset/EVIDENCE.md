# Evidence

## Environment

```text
repository_head=ee34b5eec26ae1113a2d22a393d383d5cb96bdd2
platform=Windows PowerShell sandbox
python=3.14.3
mpmath=1.3.0 (opt-in diagnostics only)
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `211/2<T_{6,29}` and `T_{6,30}<211/2` | exact theorem (endpoint lemma) | positive pre-square gates and exact rational square margins in `research/RADIUS6_SEAM_ONSET.md` | recomputed by three derivations, exact checker, and proof review | formal Descartes seam threshold only |
| `R_{6,29}<211/2<R_{6,30}` | exact theorem (endpoint lemma) | complete 24/25-edge tables, strict termwise arcsine bounds, and exact `pi` bridges | all 49 rows and totals independently regenerated; checker audit | adjacent-chain roots only |
| `Delta_{6,n}>0` for `8<=n<=29` and `<0` for every `n>=30`; hence `s_6=30` | exact theorem, post-arXiv-v1 | endpoint lemmas plus the existing fixed-`k` sign/monotonicity/persistence theorem | adversarial proof and checker reviews; exact checker corroboration | formal seam `(n,6,n-1)` only; no full/global/floating claim |
| High-precision root/threshold/deficit values | numerical observation | opt-in mpmath scan at 60/100 digits | precision comparison and independent reruns | diagnostic only; no finite scan proves the all-`n` claim |
| Checker exact path is stdlib/`Fraction`-only and production-independent | engineering fact | optimized/no-site run, AST audit, and separate production comparison | yes | checker corroborates endpoint arithmetic; it does not reprove the imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | exit `0`; no paths | clean startup tree | mathematical correctness |
| independent `Fraction` derivations | all proposed threshold/table margins and totals agreed across three audits | transcription and exact endpoint arithmetic before implementation | the imported fixed-`k` theorem |
| `python -B ops/TASK-20260805__radius6_seam_onset/check_seam.py --order-stop 250` | exit `0`; `181612` explicit gates; diagnostics skipped | exact table transcriptions, parity formulas, sign/square/domain margins, rational totals, and `pi` identities | a proof of the imported fixed-`k` theorem |
| `python -B -O -S ops/TASK-20260805__radius6_seam_onset/check_seam.py --order-stop 250` | exit `0`; identical `181612` gates and output | optimization-safe explicit gates and stdlib-only exact default path | numerical diagnostics |
| checker with `--diagnostics --start 8 --stop 120 --digits 60 --stability-digits 100` | exit `0`; `NUMERICAL_DIAGNOSTIC_ONLY`; max relative root delta `3.6470679e-46`, max absolute deficit delta `1.9594859e-46` | finite sign/domain/monotonicity/precision checks and separator closure signs | exact endpoint proof or all-`n` certification |
| external task-local/production convention comparison, `n=8..250` | exit `0`; `486` comparisons | exact equality with production `supnick_max_tour` and cyclic equivalence with `interleave` | mathematical optimality of Supnick's theorem |
| AST/source audit | exit `0`; zero `assert`, float literals, `ringmin` imports, and top-level `mpmath` imports; one lazy `mpmath` import | exact-source literals, gate persistence, dependency separation | dynamic behavior by itself |
| in-memory corrupted-upper-margin and zero-lower-bound mutations | exit `0`; both intended `AuditFailure` gates caught | corrupted arithmetic and lost strictness are rejected | every possible tamper |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 32.98s` | repository regression suite without changing tests | the new all-`n` proof or global frontier certification |
| independent proof-note and checker reviews | detailed `PASS`; every table row, threshold, total, `pi` identity, quantifier, and checker mode rechecked | adversarial mathematical and engineering scrutiny | hosted CI |

The exact compact invocations rerun for the two external source/convention
audits were:

```powershell
python -B -c "import importlib.util as u,sys; sys.path.insert(0,'src'); s=u.spec_from_file_location('radius6_check','ops/TASK-20260805__radius6_seam_onset/check_seam.py'); c=u.module_from_spec(s); s.loader.exec_module(c); from ringmin.patterns import interleave,supnick_max_tour; checks=[(c.shifted_supnick_tour(n)==supnick_max_tour(range(6,n+1)),c.cycle_equivalent(c.shifted_supnick_tour(n),interleave(range(6,n+1)))) for n in range(8,251)]; passed=sum(flag for pair in checks for flag in pair); print(f'production_convention_comparison=PASS n=8..250 comparisons={passed}'); raise SystemExit(passed!=486)"
```

```powershell
python -B -c "import ast,pathlib; t=ast.parse(pathlib.Path('ops/TASK-20260805__radius6_seam_onset/check_seam.py').read_text(encoding='utf-8')); nodes=list(ast.walk(t)); a=sum(isinstance(n,ast.Assert) for n in nodes); f=sum(isinstance(n,ast.Constant) and isinstance(n.value,float) for n in nodes); r=sum((isinstance(n,ast.ImportFrom) and ((n.module or '')=='ringmin' or (n.module or '').startswith('ringmin.'))) or (isinstance(n,ast.Import) and any(x.name=='ringmin' or x.name.startswith('ringmin.') for x in n.names)) for n in nodes); tm=sum((isinstance(n,ast.ImportFrom) and ((n.module or '')=='mpmath' or (n.module or '').startswith('mpmath.'))) or (isinstance(n,ast.Import) and any(x.name=='mpmath' or x.name.startswith('mpmath.') for x in n.names)) for n in t.body); lm=sum(isinstance(n,ast.Import) and any(x.name=='mpmath' for x in n.names) for n in nodes); print(f'ast_source_audit=PASS assert_nodes={a} float_literals={f} ringmin_imports={r} top_level_mpmath_imports={tm} lazy_mpmath_imports={lm}'); raise SystemExit((a,f,r,tm,lm)!=(0,0,0,0,1))"
```

The mutation harness loaded the checker in memory, changed the first `n=29`
stored upper margin to `margin+1`, and required the `upper margin failed`
`AuditFailure`; after restoration it changed the first `n=30` lower bound to
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

- A direct reuse of the earlier `<3<pi` bridge is impossible at `n=29`:
  the diagnostic half-closure at `R=211/2` is approximately `3.139402`.
- Floating-point roots and deficits were used only to diagnose the candidate;
  they are not premises of the exact conclusion.
- No counterexample to the proposed endpoint inequalities was found in three
  independent reconstructions.
- The first direct whitespace audit used a faulty PowerShell regex and
  falsely marked blank lines. A corrected last-character check passed all
  eight files; the false positive changed no file.
- One ignored `__pycache__` directory created by an independent checker review
  was found by the explicit task-directory audit and removed. It contained
  only the regenerable checker bytecode and was never part of the intended
  delta.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths, comprising three tracked modifications and five untracked additions;
- complete `git diff` inspected: yes, including the final status synchronization;
- untracked additions inspected directly: all five read in full; the proof and
  checker also received separate adversarial reviews;
- direct format check: all eight paths are strict UTF-8 without BOM, LF-only,
  have exactly one final LF, and contain no trailing whitespace;
- `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none under `src/`, `tests/`,
  `results/`, `verify.py`, `paper_assets/`, or the imported theorem;
- generated files unexpectedly changed: none; the detected review-time
  `__pycache__` was removed and the task directory has exactly four files.

## Residual uncertainty

The exact theorem intentionally depends on
`research/FIXED_K_SUPNICK_SEAM.md`; the task-local checker does not reprove
that source. A positive formal seam deficit is not full feasibility, and a
negative one says nothing about a replacement chain or global optimum.
Hosted CI, `verify.py`, certificate frontiers, and paper builds are unrelated
to this delta and were not run.
