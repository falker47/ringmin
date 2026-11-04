# Independent package review

Reviewer: independent package-review subagent. Mode: STRICT.
Scope: build/export/manifest closure, package portability, CI wiring,
article-versus-public-source editorial delta, protected-paper and reused-lower
identity. This is an internal review; it does not advance Review State.
Base: `75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae`.

## Final review outcome

The requested local engineering/editorial review is complete. All demonstrated
packaging failures were corrected and independently retested, including the
additional external auxiliary-input bypass and CRLF normalization issue found
during final review. The corrected builder still reproduces all three PDFs
byte for byte. No unresolved actionable packaging finding remains within the
reviewed scope. The historical checkpoints below retain failed attempts and
pending-at-the-time gates; the final replay sections supersede those statuses.

This outcome does not declare mathematical acceptance, final journal readiness,
or exact-commit CI success. Final documentary re-export, staged byte comparison,
commit and hosted CI are parent-owned gates after this report.

## Preliminary checkpoint (retained history)

Preliminary review of the in-progress candidate on 2026-10-23. The upper
supplement and documentary maps were still being authored during this pass.
Final package verification, full outside-repository build, delivered archive
inventory, all-page visual review, and exact-commit hosted CI are PENDING.
The reviewer does not infer those gates from local checks or author reports.

## Actionable findings and disposition

1. **External TeX inputs passed the claimed recorder closure.** The first
   `compile_document` implementation rejected an external `.tex` only if it
   had the main source's basename. A different external `.tex` was silently
   recorded under `system_inputs`. A temporary article containing an absolute
   input of a harmless temporary `outside.tex` returned a PDF and recorded
   `outside.tex` as a system input. This undermined the claim that an isolated
   build established source closure. The author changed the implementation to
   require every external input to belong to declared TeX roots. Final
   regression replay is pending.
2. **A source edit could be exported with its stale PDF and build record.**
   On a temporary package copy, changing `Our main result` to
   `Our modified main result`, without building, then running `build.py --export`
   and `verify_package.py` returned exit 0 for both. The actual source hash
   disagreed with `BUILD_REPORT.json`. The author added source/PDF hash binding
   to the build report at export and verification. Final regression replay
   is pending.
3. **A package missing its main source could be accepted.** Deleting
   `main.tex` from the same temporary copy and regenerating the export returned
   exit 0 from export and package verification. The original manifest checked
   consistency of whatever files happened to remain, without a mandatory
   inventory. The author added a mandatory inventory and complete three-document
   build-record check. Final regression replay is pending.
4. **Authenticated bytes need a local Git text rule.** The worktree has
   `core.autocrlf=true`; the root attributes do not cover this new package.
   A package-local `.gitattributes` preserving hashed bytes is necessary before
   final export and commit. The author has included this in the new required
   inventory; actual checkout-equivalent bytes remain to be checked.

The three demonstrated failures were reported to the author immediately.
The first negative-control run exited 0 and printed:

```text
RECORDER_EXTERNAL_INPUT_ACCEPTED True 12596
STALE_PDF_SOURCE_HASH_MATCH False
STALE_PDF_EXPORT_EXIT 0
STALE_PDF_VERIFY_EXIT 0
MISSING_MAIN_EXPORT_EXIT 0
MISSING_MAIN_VERIFY_EXIT 0
```

These are tests of the earlier implementation, not findings against an
unseen final revision. They were run using Python 3.14 and external temporary
copies; no delivered source, protected artifact or certificate was modified.

A subsequent attempt to test changed lower-supplement bytes and deterministic
export encountered the newly added required-inventory check while the candidate
was incomplete. No archive was written; the test harness then failed reading
that absent archive. This attempt proves neither deterministic export nor final
lower tamper rejection. The updated code now checks all lower-manifest output
hashes in `validate_build_report`, which is a useful correction, but it still
requires a final operational test.

## Checks independently run

All commands were run locally in the managed candidate worktree, using
Python 3.14. Exit codes and material output below were observed by this
reviewer, not copied from a previous dossier.

| Command | Exit | Observed scope/result |
| --- | --- | --- |
| `git status --short` | 0 | Only the CI edit and this task's two new directories appeared. |
| `git diff -- .github/workflows/ci.yml` | 0 | Exactly two Proposition 7 verifier commands added to the existing job. |
| `git diff --name-only 75a2f448 -- paper_assets/ringmin_paper.tex paper_assets/ringmin_paper.pdf paper_assets/asymptotic_sequel paper_assets/journal_dcg research knowledge src results verify.py` | 0 | Empty output: no tracked protected-path content delta at this check. |
| `git config --get core.autocrlf` | 0 | `true`. |
| `python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/verify.py` | 0 | Exact certificate recomputation; 144 rational deletion fixtures; 48 prescribed measures; 16 tour/cutoff cases; 12 output hashes and 7 available source-input hashes. |
| `python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/check_integrity_controls.py` | 0 | Standalone copy passes; altered certificate, altered document and Python `-O` rejected; no delivered file modified. |
| `python -I -S paper_assets/paper_ii_journal/checks/check_line_recovery.py` | 0 | 1089 rational words, 13995 independent paths, 13941 pair/closure checks, 1089 all-pair concatenations, 94620 genuine-label quantiles; 4 negative controls rejected. |
| `python -I paper_assets/paper_ii_journal/checks/check_word_lp.py` | 0 | Six bounded LP cases; 1119 complete word inequalities; 18 corrupt certificates rejected. |
| `git diff --no-index -- paper_assets/asymptotic_sequel/ringmin_asymptotic.tex paper_assets/paper_ii_journal/main.tex` | 1 | Expected no-index difference exit; complete displayed editorial/source diff inspected. |

The Python checks are independent of the production Ringmin implementation;
word LP candidate discovery uses SciPy, followed by rational checks. They
corroborate bounded arithmetic and engineering properties, not the universal
analytic results. The original lower supplement's manifest and protected-path
Git diff jointly support unchanged reuse at this preliminary checkpoint.

## Editorial and CI assessment

The main article retains the public Paper II limit and finite-word proofs
and explicit endpoint formulas. Its reviewed changes identify the separate
journal candidate, cite corrective Paper I v2 for the current finite account,
retain v1 for historical disproof, disclose overlap with the published Paper II
preprint, and replace history-dependent endpoint references with S1/S2.
No new finite optimum or globally sharp endpoint is claimed. The finite range
is explicitly not an asymptotic premise. No substantive change to the main
limit/LP theorem formulas was found in this source comparison.

The current workflow has both `push` and `pull_request` triggers with no path
filter. The added commands target the preserved lower supplement, use the
standard library under `-I -S`, and run its integrity controls. Existing
checkout and Python/dependency/test stages remain intact. This establishes
workflow wiring only. Hosted CI must be inspected for the exact later SHA.

## Boundaries recorded at the preliminary checkpoint

- Final package/upper-supplement authoring and manifest export must finish.
- Re-run each demonstrated negative control against the final scripts.
- Independently inspect archive members and inner/outer manifest closure;
  verify complete byte-identical S1 inclusion and repeatable export.
- Replay package verification after extraction outside the repository;
  perform the documented build without task-history files.
- Check complete final Git delta and byte preservation after staging.
- Main article prose comparison is not an independent mathematical proof
  acceptance, an exhaustive priority search, or a journal acceptance decision.


## Final standalone replay, 2026-10-23

The complete package was reviewed outside the repository using Python
3.14.3, SciPy 1.17.1 and pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025,
kpathsea 6.4.1). All files used for mutations, compilation and re-export were
in a fresh external TemporaryDirectory. No package source or output was
modified by this reviewer. Only this report is a reviewer edit.

The archive reviewed at this checkpoint had SHA-256
`fb0d63c610ca5951b9b8d324dea9019e5faaef260a8bef468323ff6c1b038f65`.
It contained exactly 36 unique files (35 payload files and its manifest).
Independent byte comparison confirmed all 13 files in `lower_supplement/`
exactly match the preserved repository supplement, with identical inventory.
The repository's outer manifest checked 23 payload hashes; extraction checked
35 payload hashes. Re-export from the standalone tree checked 36 payload
hashes including the newly generated source archive.

| Exact command, in extracted directory unless stated | Exit/result |
| --- | --- |
| `python -I -S verify_package.py` | 0, complete inner manifest and lower provenance |
| `python -I -S build.py` | 0, three isolated passes per document; main 9 pages, S2 13 pages, S1 14 pages; zero reference/box warnings |
| `python -I -S verify_package.py` after rebuild | 0; source/PDF/build-report bindings and delivered hashes still agree |
| `python -I -S verify_math.py --with-lp` | 0, complete bounded replay including all five upper checkers, lower verifier/integrity controls, line checker and rational word LP |
| `python -I -S -O verify_math.py` | 1, expected `FAIL: assertions must remain enabled; do not use -O` |
| `python -I -S build.py --export` twice | Both 0; both source ZIPs byte-identical to each other and the reviewed delivered ZIP |
| `python -I -S verify_package.py` after export | 0; exact archive/current inventory and all byte identities |

All three rebuilt PDF hashes matched their delivered originals:

| Document | SHA-256 |
| --- | --- |
| main.pdf | `0001c5c4b5ae26d106715d4a25f452b2a0386b24308213262465f7bd14c5994a` |
| upper_supplement.pdf | `bb6b2704151ced2464e76cf6272072d1185258ff2655b7baea5ed468285ba56b` |
| lower_supplement/supplement.pdf | `a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568` |

The bounded mathematical replay independently reproduced the lower certificate,
144 rational deletion fixtures, 48 prescribed measures, 16 tour/cutoff cases,
1089 rational line words, 94620 label quantiles, 2835 point plus 297 interval
arithmetic oracles, 120 alpha recovery cases, all directed upper sign gates,
16 fourth-block corner partitions, 448 reflection moments, 48 branch probes,
and 1119 complete LP word inequalities. It rejected all built-in negative
controls, including 18 corrupt LP certificates. The fourth-block raw bound was
`-701561353/200000000000000000000000`, giving the stated normalized strict
saving using pi<4. These are bounded arithmetic results, not analytic proof
acceptance. Historical diagnostic comparisons printed by copied checkers remain
outside the supplement's stated premises as explained in UPPER_DEPENDENCIES.md.

### Final requested integrity regressions

The regression harness was run as `python -I -S -`; subprocess commands were
exactly `python -I -S verify_package.py` and `python -I -S build.py --export`.
Every mutation was confined to a new copy of the extracted package. To test
semantic validation rather than merely old hashes, each mutated source/file's
outer manifest entry was updated to its new hash, or removed when the file
was deleted. For ZIP-only omissions, the inner manifest was consistently
updated and the outer ZIP hash recomputed. The remaining candidate files and
build report stayed unmodified.

| Negative control | Observed result |
| --- | --- |
| Absolute input of external `outside.tex` in a temporary article | RuntimeError: input outside isolated build and declared TeX roots |
| Changed main.tex, old PDF/build record, updated payload hash | Both commands exit 1: `stale build source: main` |
| Changed main.pdf, old build record, updated payload hash | Both commands exit 1: `stale build PDF: main` |
| Deleted main.tex and its manifest entry | Verifier exit 1: required manifest payload missing; exporter exit 1: required candidate payload missing |
| Deleted checks/upper_lambda.py and its manifest entry | Same required-payload rejection by both commands |
| Deleted lower_supplement/check_finite_crossing.py and outer entry | Both commands exit 1 on missing lower-manifest payload |
| Omitted upper checker from ZIP, with consistent inner/outer manifests | Verifier exit 1: required manifest payload missing |
| Omitted lower checker from ZIP, with consistent inner/outer manifests | Verifier exit 1: archive inventory differs from complete current package |

The harness completed with exit 0 and `PASS FINAL PACKAGE REVIEW REGRESSIONS`.
This discharges the original stale-output, absent-source and incomplete-archive
findings for the reviewed implementation. The auxiliary-input variant below
was discovered during the subsequent final path audit.

### Byte portability finding and correction

The five unchanged upper checker copies contain CRLF line endings. The initial
package-wide `* text eol=lf` would normalize them in Git, invalidating both
manifest hashes and the claimed byte-copy identity. Read-only commands proved
this for upper_lambda.py: `git hash-object --no-filters -- <path>` returned
`61fe27460ca8eac079d88cb2814cf1e8f3ac0036`, whereas
`git hash-object --path=<path> -- <path>` returned
`68e7e1e5c4a1ce70a6d9275ece3b45252143e99a`.

The author added `checks/upper_*.py -text`. This reviewer independently reran
`git check-attr text eol -- <path>`: text is now unset. Both hash-object
commands now return `61fe27460ca8eac079d88cb2814cf1e8f3ac0036`. This resolves the
normalization mechanism. The parent will additionally compare every staged
package blob with the actual working bytes before commit. Manifest/export must
be regenerated after the attribute/document changes.

### Additional external auxiliary-input regression

A later adversarial variant renamed the harmless external input to
`outside.aux`. The build accepted it and did not record it, because the suffix
exception preceded path validation. The exact observed output was
`EXTERNAL_AUX_ACCEPTED 12596 RECORDED False`. This was reported immediately.
The required correction is to exempt only generated auxiliary artifacts inside
the isolated build directory, applying the external-root check to every
external input irrespective of suffix. The author implemented this correction. A fresh
`python -I -S -` regression replay rejected external `.tex`, `.aux`, `.out`
and `.toc` inputs. The corrected `compile_document` then rebuilt all three
complete documents in fresh temporary directories; every PDF matched the
already recorded delivered hash, with 9/13/14 pages and no reference/box
warnings. The harness exited 0 with `PASS FINAL RECORDER CORRECTION`.
The corrected build.py SHA-256 is
`1b659df1077bf1a1d327db635a0c14fc17c6046d3f0cf6cee904b815ecf2ead3`.

### Final scope limits

This review independently establishes the reported local build, packaging,
bounded arithmetic and mutation-check outcomes. It does not claim to have
re-proved the upper supplement's analytic lemmas, accepted universal
quantifiers, performed every-page visual inspection, or exhausted novelty
literature. Those remain distinct analytic/editorial review layers. No current
mathematical result was inferred solely from PASS output or a manifest hash.

The parent's forthcoming READINESS/dossier update and re-export change the
archive hash. The final package hash must be recorded and its verifier rerun;
the final staged blob comparison and exact-SHA hosted CI remain parent-owned
completion gates. No commit, push, submission or Review State change was
performed by this reviewer.


## Final byte-filter check

After the author added the upper-checker exception, a Python harness ran
`git hash-object --no-filters -- <path>` and
`git hash-object --path=<path> -- <path>` for every current package file.
All 24 file pairs agreed; the harness exited 0 with
`PASS current Git clean filters preserve all 24 candidate files`.
This checks the configured clean filters without staging or changing files.
The actual staged-blob comparison remains the parent's final independent gate.
The final Markdown scan found no remaining previously reported mojibake tokens.
