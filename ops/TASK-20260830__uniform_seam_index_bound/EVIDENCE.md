# Evidence

## Environment

```text
repository_head=a5ae1d56039ff443f2b78f6100ae3524da408d43
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing workspace environment
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| `R_{k,4k+14}>S_k` for every integer `k>=1` | exact theorem (uniform chain lemma) | imported chain bound, strict `sin(x)<x`, exact integral witness `pi<22/7`, and symbolic identity | independent derivation and proof review | adjacent-chain root only |
| `T_{k,4k+14}<S_k` for every integer `k>=1` | exact theorem (uniform threshold lemma) | explicit pre-square positivity gate and coefficient-positive quadratic difference | independent convolution, checker, and proof review | formal Descartes threshold only |
| `4k+1<=s_k<=4k+14` for every integer `k>=1` | exact theorem, post-arXiv-v1 | fixed-`k` no-threshold/sign theorem plus the two uniform lemmas | two read-only adversarial reviews; checker corroboration | formal seam `(n,k,n-1)` only; no full/global claim |
| Checker is stdlib/`Fraction`-only and scan-free | engineering fact | normal/optimized runs, AST audit, import-side-effect audit, and mutation rejection | independent engineering review | checker corroborates new algebra; it does not reprove the imported theorem |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `git status --short` | exit `0`; no paths | clean startup tree | mathematical correctness |
| `python --version` | exit `0`; `Python 3.14.3` | active interpreter | dependency completeness |
| independent symbolic expansions | exact formulas for `P`, `P^2`, the subtrahend, `F`, and the `pi` witness agreed | derivation before implementation | the imported fixed-`k` theorem |
| `python -B ops/TASK-20260830__uniform_seam_index_bound/check_uniform_bound.py` | exit `0`; `53` explicit gates; `parameter_scans=NONE` | exact substitutions, polynomial identities, denominators, domains, signs, and strictness gates | the imported fixed-`k` theorem itself |
| `python -B -O -S ops/TASK-20260830__uniform_seam_index_bound/check_uniform_bound.py` | exit `0`; identical `53` gates and output | optimized/no-site safety and stdlib-only exact execution | hosted environments |
| AST/source/import audit | exit `0`; zero `assert`, float, third-party/production imports, parameter loops, or import effects | source discipline and scan/dependency separation | mathematical proof by itself |
| independent proof and checker reviews | `PASS`; all formulas, gates, directions, quantifiers, convolutions, and exclusions checked | adversarial mathematical and engineering scrutiny | hosted CI |
| optimized in-memory `F`-coefficient mutation | rejected with `positive quadratic numerator F(k) failed` | intended exact gate catches corrupted algebra | every possible mutation |
| `python -B -m pytest -p no:cacheprovider` | exit `0`; `12 passed in 32.69s` | repository regression suite | the new theorem or certificate frontiers |
| direct eight-file format audit | exit `0`; strict UTF-8/no BOM, LF-only, one final LF, zero trailing whitespace | tracked and untracked text integrity | mathematical correctness |
| `git -c safe.directory=... diff --check` | exit `0`; no output | whitespace errors in the tracked diff | untracked additions, covered directly |
| protected-path status and task-directory audit | exit `0`; no protected paths; exactly four task files | scope containment and absence of generated cache | hosted state |

## Artifact and provenance checks

- artifact path: not applicable; no result or certificate artifact is changed;
- generating source/command: not applicable;
- input/version: `research/FIXED_K_SUPNICK_SEAM.md` at task-base `HEAD`;
- generation commit: not applicable;
- schema/hash: not applicable;
- independent verifier: task-local symbolic stdlib/`Fraction` checker rerun in
  normal and optimized/no-site modes, with separate adversarial reviews;
- reproducibility limitation: the checker audits the new algebra and imports
  the fixed-`k` theorem as a trusted proved source rather than reproving it.

## Failed checks and negative evidence

- A read-only `git rev-parse HEAD` without a scoped `safe.directory` option
  was rejected by Git's sandbox ownership check. The per-invocation scoped
  rerun returned the task-base hash; no Git configuration was changed.
- A development-only SymPy expansion agreed with an independent integer
  convolution. SymPy is not imported by the checker and is not a premise of
  the proof.
- The first checker version passed in both modes, but adversarial review found
  that its intended `N>=18` gate checked only
  `(3k+15)-(3k+18)=-3`, and that it omitted the explicit threshold-domain
  gate. The proof itself was unaffected. The checker now verifies
  `N-18=3(k-1)>=0` for `k>=1` and `n_0-(4k+1)=13>0`; all post-fix runs are
  recorded separately below rather than erasing this failed coverage audit.
- The first compact direct-format audit command had a Python parenthesis
  syntax error and exited `1` before reading any file. A simpler multiline
  read-only audit then checked all eight files and exited `0`.
- The first optimized invocation without `-B` created a regenerable
  task-local `__pycache__`. Its resolved path was verified inside the new
  dossier and removed; the final task-directory audit contains four files and
  no directory.
- A combined delete/add `apply_patch` operation for `CURRENT_STATUS.md` was
  refused atomically by the patch tool. Separate patch operations then
  replaced the authorized file successfully without an intermediate user or
  Git-visible handoff.
- No finite parameter scan is used or planned for this theorem.

## Final diff inspection

- `git status --short --untracked-files=all`: exactly the eight authorized
  paths, comprising three tracked modifications and five untracked additions;
- complete tracked `git diff` inspected: yes, all three modified files;
- untracked additions inspected directly: yes, all five read in full after
  substantive edits;
- direct whitespace/encoding check: all eight paths passed strict UTF-8,
  no-BOM, LF-only, exactly-one-final-LF, and trailing-whitespace gates;
- `git diff --check`: exit `0`, no output;
- protected paths unexpectedly changed: none under the imported theorem,
  prior notes/dossiers, `src/`, `tests/`, `scripts/`, `results/`, `verify.py`,
  `paper_assets/`, public summaries, or build/config paths;
- generated files unexpectedly changed: none; the task directory contains
  exactly four intended files and no cache.

## Residual uncertainty

The checker intentionally corroborates only the new symbolic algebra and does
not reprove `research/FIXED_K_SUPNICK_SEAM.md`. Hosted CI, certificate
frontiers, `verify.py`, and paper builds are unrelated and were not run. The
new interval does not identify any exact onset for `k>=8`, and the theorem has
no full-feasibility, global-optimum, contact-graph, floating-circle, or global
asymptotic implication.
