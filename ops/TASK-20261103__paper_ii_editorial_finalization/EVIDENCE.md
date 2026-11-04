# Evidence for the 3 November 2026 Editorial Finalization

## Revision and Scope

Base and live starting PR #4 head:
`d925f85c8aee2b26bca460bf33618eb65fb996b8`.
The checkout was clean. No later remote changes were observed at startup.
This is STRICT editorial and packaging work, not a new general mathematical
audit or acceptance of the candidate. The containing commit identifies the
final revision; exact-commit hosted results follow push in the draft PR handoff.

The scientific delta is only the explicit total definition of J, including
its fixed complement, main's a_0=0, and manuscript dates. Both abstracts,
results, constants and mathematical checkers are unchanged. check_scope.py
compares the complete sources against an exact substitution allowlist and
checks 804 protected baseline files byte for byte, including all 13 S1 files,
public manuscripts, proof notes, certificates and earlier dossiers.

## Environment

Actual Python/package versions are in environment.json. Local validation used
Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0, Matplotlib 3.10.8
and pytest 9.0.2. These are not the historical pinned environment.
The TeX engine is pdfTeX 1.40.25 / TeX Live 2023 (Debian). BUILD_REPORT.json
records actual system-input hashes, three passes and the fixed deterministic
epoch. Missing pytest and mpmath were installed locally; repository dependency
declarations were not changed.

## Fresh Commands and Outcomes

All commands below ran from repository root unless the extracted archive is
explicitly named. PASS denotes only the stated property.

| Command / check | Observed result | Property and limit |
|---|---|---|
| python -I -S paper_assets/paper_ii_journal/build.py | exit 0; 9/13/14 pages; zero unresolved-reference, missing-character or box warnings | Three no-shell-escape passes per standalone document; actual source/input hashes recorded |
| python -I paper_assets/paper_ii_journal/verify_math.py --with-lp | exit 0; aggregate replay PASS | S1 verifier/integrity, line recovery, five original upper checkers and six exact LP cases; 1,119 inequalities and 18 corrupt LP certificates rejected; bounded, not an all-n proof |
| python -u -m pytest -vv -o addopts= --junitxml=ops/TASK-20261103__paper_ii_editorial_finalization/pytest-results.xml | exit 0; 68 tests and 4 subtests passed in 74.39 s | Complete suite, including nine preservation regressions; JUnit has no failures/errors/skips |
| python verify.py --start 3 --stop 8 --skip-frontier | exit 0, smoke PASS | Existing incumbent/local checks only; global frontier deliberately skipped |
| python -I -S verify_global_brackets.py | exit 0, PASS_GLOBAL_BRACKETS and pinned input binding PASS | Existing finite n=3..14 certificate reproduced, not extended; digest 6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0 |
| python -I -S paper_assets/paper_ii_journal/check_reproducibility.py | exit 0; two identical fresh builds of each document | Main/S2 match delivered PDFs; S1 check builds agree with each other but differ from the preserved delivery |
| python -I -S ops/TASK-20261103__paper_ii_editorial_finalization/check_reproduction_controls.py | exit 0 | Extracted archive outside repository verifies, repeats builds, preserves delivered files, rejects seven corruption/missing-file/external-input controls; also confirms strict delivered replay rejects S1 mismatch |
| python -I verify_math.py --with-lp in separately extracted archive | exit 0 | Full bounded mathematics executable without repository/ops dependencies |
| python -I -S paper_assets/paper_ii_journal/build.py --export, twice | both exit 0; ZIP and outer manifest byte-identical | Deterministic final export after documentation freeze; 39 ZIP members, 38 inner and 26 outer payload hashes |
| python -I -S paper_assets/paper_ii_journal/verify_package.py and extracted counterpart | exit 0 | Final sources, delivered PDFs, current scripts, manifests and unchanged S1 agree |
| python -I -S ops/TASK-20261103__paper_ii_editorial_finalization/check_scope.py | exit 0 | Exact TeX substitutions, unchanged abstracts, 804 protected files and authored-text whitespace; final --staged gate binds Git blobs to inspected bytes |
| PDF structure and visual inspection | PASS in stated scope | Main 9 and S2 13 pages inspected visually, including J on main p.5 and S2 p.4; all main/S2 fonts embedded; no unresolved markers or invalid internal destinations in all three delivered PDFs |

The seven package negative controls reject modified delivered main via both
rebuild equality and manifest, a missing checker, and undeclared external
.tex/.aux/.out/.toc inputs. Nine unit regressions separately reject forged
preservation hashes, changed S1 source/PDF, inconsistent match flags and
attempts to apply lower-only preservation semantics to main/S2.

## S1 Preservation and the Stronger Reproduction Limit

All S1 files agree byte for byte with both the reviewed `75a2f448` package
and starting `d925f85`. Source SHA-256:
`ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4`.

Its preserved delivered PDF SHA-256 is
`a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568`.
The fresh current-environment check build is
`338848bc5d9b92193ce5db565a83e32dcfa8af2752383d9d1401788aa3dff302`.

The previous builder already preserved S1, but its validator assumed every
fresh-build digest equalled a delivered digest. The minimal fix records
`delivery_policy=preserved-baseline`, both hashes and the correct false
comparison flag. The delivered source/PDF remain bound to the original S1
manifest. Main/S2 validation stays strict. This does not assert semantic
equivalence of arbitrary PDFs across TeX versions.

The unchanged optional `--require-delivered` flag fails on S1 in this
environment. Its failure was observed and handled as an explicit limit, not
silenced, renamed PASS or solved by replacing S1. S1's original 14-page visual
review is inherited; current byte identity, structural checks and repeated
check builds are fresh evidence.

## Final Delivered Artifact Identities

| Artifact | SHA-256 |
|---|---|
| main.pdf | ae9b816c7825122c40bfbf6beed9866ba4308780ada88dd7827a93508a44f1ce |
| upper_supplement.pdf | 3e63ad0132d9a328c7f35f3af100f20c6473e74624ef5220278ca88cca91e11a |
| source_bundle.zip | 99365502198e79003565adf3201dcbff5289ffd5a7713a690093db81788f5b9e |
| MANIFEST.json | e0bc3e4ae45747b15c2500a309223e3bf9c707e5a07fd4232af76b30d6b2060f |

final_export.json records byte sizes and export identity. The last re-export
only updated the readiness documentation relative to the fully exercised
portable archive; all TeX, PDFs and executable verification payloads stayed
identical. The final archive inventory and manifests were verified anew.

## Independent Internal Review

A separate assistant context reviewed J, build/validator changes, nine tests,
coverage and author worksheet. It found no blocking issue and independently
verified all 13 S1 files and the nine focused tests. A wording correction from
'computational checker' to 'mathematical checker' was applied. Another context
inspected every S2 page and page 4 separately. The main reviewer inspected all
nine main pages. These are internal checks, not external peer review or author
attestations. REVIEW_COVERAGE.md owns the inherited reports' scope and limits.

## Failures and Evidence Hygiene

The first documentation patch was rejected atomically because it used two
operations for one path. Readback showed no document changes; the corrected
update succeeded. The original terse pytest attempt logged only 17 dots and
no summary; cause remains unknown and it is not counted as a completed suite.
The complete verbose run supplies the test result.

The initial scope whitespace pass rejected terminal padding in generated
pytest stdout. Generated logs now preserve that padding; authored files still
receive explicit whitespace checks. The original failed log is retained.
Transient checkout paths and the runtime hostname were normalized in committed
evidence; log_normalization.json records the raw hashes. Outcomes are unchanged.

## Editorial and Operational Boundaries

The four supplied reviews and dated dossier were read; current official
DMTCS/EJC/SIAM instructions were checked. No venue was selected. The existing
AI acknowledgment is unchanged; historical tool identities, affected portions,
personal scientific review and submission metadata remain for the author.
No merge, Registry change, arXiv update, submission or editor message occurred.

The existing Paper II Todoist task is the sole mission to reconcile after the
commit/delivery. Its author-review work remains actionable, so it stays open.
A bounded Calendar search for Ringmin from 3 November to 4 December found no
correlated event; no timed action was requested, so no event is created.

At content freeze hosted CI and external delivery occur after commit/push.
Their exact SHA, run/job URLs and verified delivery links belong in the final
draft PR/task/chat handoff, not in a guessed self-referential source commit.
