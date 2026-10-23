# Evidence

## Environment

```text
repository_head=6167e36cf6f80a6a7a7a6b41518a6b3f7155295d
scientific_snapshot=3beb8d70c5b3748d370a92855847bdf574e5a14f
platform=Windows
task_mode=STRICT
dependency_source=existing Python, TinyTeX, bundled Poppler
```

## Claim ledger

The package `DEPENDENCIES.md` maps each exact theorem/proved corollary L1--L8
to hypotheses, the complete proof and the applicable checks. Rational
enclosures are exact arithmetic results; finite fixtures corroborate only
their bounded cases. No hosted CI or independent external review is asserted.

## Commands and checks

- Original `git status --short`: exactly the user-identified ZIP; branch main;
  `git rev-parse HEAD`: 6167e36cf6f80a6a7a7a6b41518a6b3f7155295d.
- `git cat-file -t 3beb8d70c5b3748d370a92855847bdf574e5a14f`: commit.
- Isolated elevated `git status --short`: empty, exit 0.
- `git diff 3beb8d70c5b3748d370a92855847bdf574e5a14f HEAD --` the four
  requested research notes: empty, exit 0.
- Original ZIP SHA-256:
  `e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.

## Artifact and provenance checks

Package manifest and exact arithmetic certificate completed; see the command matrix below. All existing tracked
paths except CURRENT_STATUS.md were hashed before edits; final comparison
is recorded below. The published Paper II is the target, never the older v2
manuscript. No publication assets are regenerated incidentally.

## Failed checks and negative evidence

Sandboxed Git in the newly created worktree reported `this operation must be
run in a work tree` and then `cannot come back to cwd: Permission denied`.
Read-only diagnosis found valid worktree metadata; elevated access resolved
the environmental failure without changing repository configuration.

## Final diff inspection

Completed author/source review and scoped checks are recorded below; the final staged inspection immediately precedes the authorized commit.

## Residual uncertainty

External mathematical review remains required. Exact arithmetic checks do
not replace the analytic universal quantifiers. This task makes no claim of
sharpness of the geometric lower endpoint.


## Completed verification evidence

The package [technical report](../../paper_assets/asymptotic_sequel/proposition7_supplement/VERIFICATION.md)
records the complete command/result matrix and analytic limitations. All
commands in this section were run locally in this task; they are not copied
historical submission gates or hosted CI evidence.

| Exact command (package cwd unless stated) | Exit/result | Property and limit |
|---|---|---|
| `python -I -S verify.py --write-certificate --skip-manifest` | 0 | Generated exact certificate after strict target endpoint and bounded deletion checks. Does not check manifest. |
| `python -I -S check_width_optimum.py` | 0; all gates PASS | Fresh exact arithmetic from preserved scientific Git blob; analytic quantifiers remain in the proof. |
| `python -I -S verify.py` | 0; 144 deletion fixtures, inherited crossing controls, certificate equality, 12 output hashes, 7 normalized repository input hashes PASS | Exact arithmetic and package identity; production-independent, partially coupled to preserved checker formulas. |
| `python -I -S check_integrity_controls.py` | 0; standalone copy PASS, altered certificate rejected, altered README rejected, Python -O rejected | Integrity controls modify temporary copies only; no all-n proof implication. |
| `pdflatex -interaction=nonstopmode -halt-on-error -recorder -output-directory=build supplement.tex` (3 fresh outside-repository passes) | 0 / 0 / 0 | 14 pages; final warnings=0, undefined refs=0, overfull=0, underfull=0; no repository recorder input; PDF bytes reproduced. |
| `pdftoppm -scale-to 1400 -png supplement.pdf page` | 0 | All 14 rendered pages inspected; latest contents layout checked separately; no clipping/overlap found. |
| Internal reviewer: `python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/verify.py --skip-manifest` | 0; no actionable mathematical/verifier findings after complete source review | Separate internal agent review; excludes PDF/manifest packaging and is not external acceptance. |
| `python -I -S ops/TASK-20261023__proposition7_supplement/make_manifest.py` (repository cwd) | 0; 7 immutable inputs, 12 output hashes | Input Git-blob and checkout hashes, normalized equality, copied-checker byte identity; manifest intentionally excludes itself. |
| `git check-attr text --` package source and manifest | `text: unset` for both | Package-local preservation of exact output bytes. |
| `git check-ignore` package PDF and arithmetic log | 1, no matches | Expected: both are stageable and not ignored. |
| `git ls-remote --heads origin main` | 0; 6167e36cf6f80a6a7a7a6b41518a6b3f7155295d | Read-only pre-integration remote check, not final push evidence. |

Final PDF SHA-256:
`a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568`.
The manifest contains the remaining exact output hashes. New generation
sources are pinned by those hashes over the stated base; the commit carrying
the package is its immutable revision. No nondeterminism in arithmetic;
same-engine PDF byte reproducibility observed, cross-engine bytes not claimed.

## Additional failed authoring checks

- Built-in LaTeX compiler: unavailable, Windows sandbox setup incomplete.
- Initial shell TeX command: exit 1 because PowerShell passed a literal
  output-directory variable. Quoting the full argument fixed it.
- Subsequent TeX attempt: exit 1, unused mathtools absent; then optional
  microtype absent. Removed unused/optional packages, installed nothing.
- First successful draft had overfull lines and a rerun warning. Line breaks,
  path formatting, contents spacing and extra passes eliminated them.

## Final scope inspection

All 759 pre-existing tracked paths except CURRENT_STATUS.md matched the
preflight SHA-256 snapshot. The final authored text and scripts were read in
full, including the independent review of core proof/checkers. The manifest
and certificate were parsed in full and compared with fresh exact outputs.
The original ZIP hash and original working-tree status are checked again
before integration. No stable claim was duplicated into a knowledge ledger.
The scoped diff and explicit whitespace scan include untracked additions;
staged diff/whitespace and stored Git-blob bytes are checked before commit.

## Integration record convention

The final chat handoff records the exact commit SHA, normal push outcome and
post-push remote/worktree status. A file cannot embed its own containing
commit hash without changing that hash. The package revision is therefore
the commit carrying these files, not a self-referential guessed identifier.
No hosted CI success is claimed. Exactly one next atomic task: independent
review of that exact committed supplement.
