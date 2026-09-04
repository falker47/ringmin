# Evidence

## Environment

```text
repository_head=0d2eef8702d19fd93982a495bc1aeea50f29a79a
platform=Windows PowerShell sandbox
python=3.14.3
dependency_source=existing interpreter; stdlib fractions; mpmath 1.3.0 for sanity only
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| Restriction to any retained set preserves feasibility | exact theorem | unchanged centers, central tangencies and all surviving distance constraints; proof section 2 | analytic argument independent of production | requires an actual feasible configuration, not a formal chain |
| R*(n)>=R*({k,...,n})>=R_{k,n} | proved corollary | deletion, cyclic-gap sum and published arbitrary-radii Supnick theorem | independent of search and verifier | generic theorem does not validate new floating-point pruning code |
| R_{k,4k+5}/k^2->rho | existing exact theorem, rederived for this task | proof section 3 checks both parities, Riemann sums, uniform per-edge errors and root bracketing | separate local analytic rederivation; historical checker rerun | Supnick ordering is imported; no formal proof assistant |
| liminf R*(n)/n^2>=rho/16>3/22>1/8 | exact theorem / proved corollary | proof sections 4-5; exact rational margins; floor interpolation | analytic derivation and stdlib arithmetic independent of production | lower bound only; no normalized-limit or equality claim |
| n^2/8 leading term and O(sqrt(n)) deficit | disproved claims | eventual deficit <-n^2/88 in proof section 6 | analytic consequence | no explicit eventual threshold |
| rho/16 approximately 0.13969590237005975546 | numerical observation | 80-digit quadrature and closed form | mpmath, independent of production | sanity only, absent from the proof premises |

The full-feasibility note was read, including its triangle/path argument,
small cycles, weak inequality and strict-sign classification. Its feasible
boundary family implies equality for the reduced-set optimum when combined
with Supnick's theorem. This optional observation is not used to prove the
new global lower bound. No independent acceptance of that prior note is
claimed in this task.

## Commands and checks

All commands below were run locally in this task unless explicitly marked
pending. No hosted result is inferred. Repository-relative commands run
from the repository root. Git commands use the per-invocation option
`-c safe.directory=<resolved repository root>`; the resolved root was
supplied as a literal argument. This does not modify configuration.

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; Python 3.14.3 | interpreter | proof correctness |
| `git status --short --untracked-files=all` with scoped option | 0; no changed paths at startup; global-ignore permission warnings | clean working tree before edits | ignored artifacts or mathematics |
| `git rev-parse HEAD` with scoped option | 0; base SHA above | starting source identity | acceptance of prior claims |
| `python -B -O -S ops/TASK-20260830__eventual_supnick_seam_onset/check_asymptotic_onset.py` | 0; 68 explicit gates, 4 parity subsequences, no parameter scans | existing parity/endpoints, rational errors and rho bounds | imported ordering theorem or mechanized convergence |
| `python -B -I -S ops/TASK-20260904__induced_subset_asymptotic_bound/check_exact_arithmetic.py` | 0; exact output below | signed polynomial remainders, rational constant separation and all 4 symbolic residue cases | deletion geometry and analytic limits |
| 80-digit constant-only sanity command below | 0; exact output below | independent numerical agreement of integral and closed form | any finite optimum, global certificate or proof |
| Direct `python -B -` scope/format/hash audit | 0; tracked=4, new=5, total=9; UTF8/no BOM=9, complete new-file whitespace=5; HEAD/index/protected tracked paths unchanged | exact changed-file set, every untracked text file and source hashes | proof correctness or ignored historical outputs |
| `git diff --check` with scoped option | 0; no output | whitespace in tracked additions | untracked files, audited directly |

Existing asymptotic audit output:

```text
independent_of_production=PASS (stdlib fractions only)
parity_endpoint_audit=PASS c_cases=2 parity_subsequences=4 parameter_scans=NONE
threshold_conjugate_factorization=PASS c=5,6
uniform_threshold_denominator_bounds=PASS error_lt_17/k
exact_rho_interval=PASS 24/11<rho<8/3
exact_symbolic_audit=PASS explicit_gates=68 optimized_safe=YES
classification=EXACT_STDLIB_FRACTION_SYMBOLIC_AUDIT; checker is corroborative and does not mechanize analytic convergence or the imported fixed-k theorem
```

Task-local exact audit output:

```text
signed_remainder_identities=PASS identities=2 pi_quotient=22/7
atan_lower=365721/573440 rho_cross_margin=650463/114688
constant_separation=PASS (24/11)/16=3/22 gap_to_1/8=1/88
all_integer_interpolation=PASS symbolic_residues=4 parameter_scans=NONE
classification=EXACT_RATIONAL_AUDIT; geometry and limits require analytic proof
```

The constant-only sanity command was the following PowerShell here-string
piped to `python -B -`:

```powershell
@'
import mpmath as mp
mp.mp.dps = 80
integral = mp.quad(lambda x: mp.sqrt(x*(5-x)), [1, mp.mpf(5)/2])
rho_integral = 2*integral/mp.pi
rho_closed = (12+25*mp.atan(mp.mpf(3)/4))/(4*mp.pi)
print('mpmath=' + mp.__version__ + ' dps=80')
print('rho=' + mp.nstr(rho_closed, 32))
print('rho/16=' + mp.nstr(rho_closed/16, 32))
print('quadrature_closed_form_abs_difference=' + mp.nstr(abs(rho_integral-rho_closed), 5))
if abs(rho_integral-rho_closed) >= mp.mpf('1e-70'):
    raise RuntimeError('sanity check mismatch')
print('classification=NUMERICAL_SANITY_ONLY; no finite root or global optimum computed')
'@ | python -B -
```

Output:

```text
mpmath=1.3.0 dps=80
rho=2.2351344379209560874207891274258
rho/16=0.13969590237005975546379932046411
quadrature_closed_form_abs_difference=0.0
classification=NUMERICAL_SANITY_ONLY; no finite root or global optimum computed
```

## Artifact and provenance checks

Result/certificate regeneration, generation commit, result schema and
global verifier: not applicable. No result artifact is changed or used as
a premise. All theorem dependencies are tracked at the base SHA above.
The production evaluator, induced-order lower bounds in search and
standalone verify.py, and related tests were inspected only to confirm
the model and scope. The new checker imports only fractions.

No pytest, global verifier, paper build or hosted CI was run: this is an
analytic proof/documentation delta with no production or artifact changes.
The recorded global certificate scope remains 3<=n<=14.

## Failed checks and negative evidence

- Initial unscoped read-only Git calls failed ownership protection; the
  per-command safe.directory remedy succeeded, without a config write.
- A NUL global-exclude override failed with `cannot use NUL as an exclude
  file`; it was abandoned. Ordinary scoped status was rerun successfully.
- An apply_patch request with delete/add operations on CURRENT_STATUS.md
  was rejected before application for duplicate targets. The patch was
  split and the status file rewritten in place within the authorized scope.
- Some combined source reads were truncated; relevant mathematical
  premises were reread separately. Final file inspection is recorded below.
- No counterexample or false step in the requested argument was found.
  Discarded shortcuts: deleting from formal closure alone, assuming a
  triangle inequality, assuming normalized monotonicity, rounding up the
  subsequence index, and using reduced-set feasibility as a full-set upper
  bound. Their exact failure modes are preserved in the proof note.

## Final diff inspection

- Complete four-file tracked diff read in full, with no output truncation.
- All five additions read in full: proof note, checker and three dossier
  documents. The final handoff-only edits were inspected afterward.
- Direct UTF-8/no-BOM audit covers all nine files; complete LF, exactly-one-
  final-newline and trailing-whitespace checks cover all five additions.
  Existing README formatting outside the diff was preserved.
- `git diff --check`: exit 0, no output.
- Exact scope: four tracked modifications (CURRENT_STATUS.md,
  PROJECT_KNOWLEDGE.md, README.md, research/NEXT_RESEARCH_STEPS.md) and five
  new files (the proof note and the four files in this dossier).
- All tracked paths outside that four-file set match the index; the index
  matches the base HEAD. This includes AGENTS.md, paper_assets/, results/,
  verify.py, src/, tests/, scripts/, all existing research notes except
  the roadmap, all prior dossiers, REPORT.md and publication/build metadata.
  No generated file or Git history/index change was made.

The direct audit used Python's subprocess with the scoped Git option to
compare `git diff --name-only` and `git ls-files --others --exclude-standard`
against the exact path sets above, `git rev-parse HEAD` against the base
SHA, and `git diff --cached --name-only` against empty output. It decoded
each file as strict UTF-8, rejected BOMs, and for every new file rejected
CR bytes, missing/repeated final LF, and lines with `line.rstrip()!=line`.
No production module was imported. Output:

```text
scope=PASS tracked=4 new=5 total=9
text=PASS UTF8_no_BOM=9 new_files_LF_final_newline_whitespace=5
HEAD_and_index=UNCHANGED protected_tracked_paths=UNCHANGED
```

SHA-256 of the final mathematical sources:

```text
research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md
414ba2734f2527d3aad29e71148229527c30c6586190efcc145364e5a52cb9c8
ops/TASK-20260904__induced_subset_asymptotic_bound/check_exact_arithmetic.py
50db8a59148440ae458830f443d9a8fe838d4c2ad090970b4b2a5246a0565840
```

## Residual uncertainty

Independent human mathematical review and manual integration are pending.
This task does not establish a sharp coefficient, matching upper bound,
existence of the normalized limit, an explicit eventual threshold,
floating behavior or a new finite certificate. The arithmetic checker
corroborates exact algebra and is not a formal proof assistant. Hosted CI
has not been inspected. The public arXiv-v1 record is preserved verbatim.
