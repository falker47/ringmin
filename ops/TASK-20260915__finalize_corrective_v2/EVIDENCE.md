# Evidence

## Environment

```text
repository_head_before_final_commit=b297d21
platform=Windows / PowerShell
python=not separately queried; builder invoked with Python
dependency_source=existing checkout; no installation planned
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independent? | Limitation |
|---|---|---|---|---|
| The standalone sequel is identified as arXiv:2609.13630 | supplied external publication metadata, corroborated by the official arXiv record | official arXiv abstract page read at startup | read-only external source | This task does not submit, moderate or accept the sequel. |
| Corrective source preserves the audited mathematical content and numerical inputs | engineering preservation fact | current-task stdlib-only preservation check; exact source/table/figure hashes; existing correction audit | independent of production builder/checker | Does not re-prove the mathematics or recertify finite optima. |
| Corrective PDF is rebuilt without source/build warnings | author-supplied builder result, corroborated by current manifest and clean-build files | `PASS correction: 3 clean passes; stable aux/out; zero warnings`; PDF SHA256 and 12-page inspection | builder is production-coupled; no arXiv server build is claimed | Local TeX Live is not arXiv's server environment. |
| Corrective package audit passes with finalized identifier and inputs | independently reproduced package-audit result | checker pass against the actual builder clean directory; 4 inputs, 12 exact pages, metadata/PDF match | checker is independent of the builder's orchestration but uses the candidate artifact | The mistyped path fails before comparison; arXiv's server build remains untested. |
| Corrective package is a copy-ready replacement candidate | locally copy-ready engineering/provenance conclusion | source/data preservation, builder artifact, author-supplied independent direct compile, checker, tests and PDF inspection pass | checker and preservation checks are independent of builder orchestration; TeX compile is author-supplied | It is not an arXiv submission or external acceptance. |

## Commands and checks

| Command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python paper_assets/build_publications.py correction` | author-supplied exit 0: `PASS correction: 3 clean passes; stable aux/out; zero warnings`; PDF SHA256 `64e3889dca456173cfcb7d30d3f407e7d73bb15d28b3f8dc70ed12a7420002bf` | Four-input clean builder, stable references, warnings, PDF/manifest hashes | Author-run result; the independent direct compile is recorded separately |
| checker with `...publication-correction-cb650a4f8a1144d28846f13ff0e894e2` | exit 0: `PASS correction: 4 inputs; 20 labels; 8 references; 12 exact pages; 20 embedded scalable fonts; 130 system-only dependencies; no active content; metadata consistent` | Source inventory, hygiene, references, metadata, PDF objects and exact clean/candidate agreement | Does not re-prove mathematics |
| checker with author clean build `...independent-correction-local` | current-task exit 0: `PASS correction: 4 inputs; 20 labels; 8 references; 12 exact pages; 20 embedded scalable fonts; 130 system-only dependencies; no active content; metadata consistent` | Source inventory, hygiene, references, metadata, PDF objects and exact independent-clean/candidate agreement | Does not re-prove mathematics or independently reproduce the author's compilation |
| checker with the supplied `...publication-correction-cb650a4f8a1144d28846f13ff0e891e2` | exit 1: `FileNotFoundError` for the absent directory, before comparison | Reproduces the reported discrepancy and identifies the one-character path mismatch | Does not indicate missing files in the actual builder output |
| author-supplied independent source-bundle compile | supplied exit 0; four-file source bundle compiled independently with `SOURCE_DATE_EPOCH=1789084800` and `FORCE_SOURCE_DATE=1`; clean PDF is 12 pages and SHA256 matches the candidate | Direct source-only compilation under the builder's deterministic environment | The compilation itself is author-supplied; arXiv's server environment is not tested |
| source/table/figure preservation comparison | exit 0: all three proof bodies/tables unchanged; source/bundle equality; historical inputs byte-identical; references, identifier and whitespace pass | No mathematical/data drift and frozen standalone source/data | Does not re-prove the mathematics |
| `python verify.py --start 3 --stop 14` | exit 0; `n=03` through `n=14` all `incumbent=PASS local=PASS frontier=PASS`, with `eta=1.0e-12` | Saved finite certificate artifacts, local brackets and retained frontiers | Rechecks saved evidence; does not rerun exhaustive generation or add new science |
| `python -m pytest -q -rA` | exit 0, 15 passed | Repository regression tests, including frontier archive safeguards and geometry checks | Not a publication PDF or arXiv-service check |
| `pdfinfo`, `pdftoppm` plus visual page inspection | exit 0; 12 letter pages, no encryption/forms/JavaScript; all 12 pages inspected | PDF structure, rendering, fonts/figures/tables and layout | Does not reproduce arXiv's server rendering |
| reparse-point audit over candidate, source bundle and actual clean tree | exit 0: `REPARSE_POINTS=none` for all three | Rules out symlink/junction/path redirection | Does not test another host's filesystem |
| active standalone-ID marker audit | exit 1 with no matches for pending/draft identifier markers in current status, publication navigation, corrective package or standalone README | Confirms no active obsolete standalone-ID marker remains | Historical dossiers and checker guard strings retain their archival/validation roles |
| `git diff --check` and complete working-tree diff inspection | current-task final pass exit 0; complete scoped diff reviewed | Repository whitespace and scoped file integration | Remote review decision |

Do not report a command as executed until its current-task output is appended
here with the exact exit result.

## Artifact and provenance checks

- artifact path: `paper_assets/v1_correction/ringmin_finite_v2.pdf`;
- generating source/command: `paper_assets/v1_correction/ringmin_finite_v2.tex`,
  `python paper_assets/build_publications.py correction`;
- input/version: corrective source bundle plus byte-preserved appendix/figures,
  fixed `SOURCE_DATE_EPOCH=1789084800`;
- generation commit: final commit produced by this task; see git log;
- schema/hash: `BUILD_MANIFEST.json`, `REVIEW_METADATA.json`, package report and
  PDF checks agree; actual clean-build directory is
  `reproducibility/.work/publication-correction-cb650a4f8a1144d28846f13ff0e894e2`;
- independent verifier: existing publication checker plus author-supplied direct clean compile;
- reproducibility limitation: local TeX Live 2025 package/font snapshot may
  differ from arXiv's server environment.

## Failed checks and negative evidence

The exact mistyped clean-directory path from the reported checker invocation
does not exist; the actual builder path differs by one character and contains
both expected figure inputs. The mistyped invocation reproduces a
`FileNotFoundError` before comparison, while the checker passes against the
actual path. An initial preservation probe also failed on an overstrict
assertion that expected one identifier occurrence; source inspection showed
the correct two occurrences, and the corrected preservation check passed. The
earlier sandbox AppData path-resolution failure is retained as historical
negative evidence; the author subsequently supplied a completed independent
source-only build, and no indirect workaround was used.

## Final diff inspection

- `git status --short`: 14 expected tracked task files modified and the new
  untracked three-file dossier; no unrelated path is present. Git emitted only
  the sandbox's pre-existing `C:\\Users\\Falker/.config/git/ignore`
  permission warning.
- complete tracked text diff, binary PDF status, and the complete untracked
  dossier were inspected directly;
- direct untracked dossier inventory/whitespace check: exit 0, exactly
  `TASK_STATUS.md`, `TASK_LOG.md` and `EVIDENCE.md`, with no trailing
  whitespace;
- `git diff --check`: exit 0; the final scoped diff was reviewed before the
  attempted stage;
- protected-path diff: exit 0 for the frozen standalone source/bundle,
  manuscript, PDF and mathematical content, historical paper, tables/figures,
  former replacement, results, verifier, production code, citation metadata
  and workflows; the standalone README change is navigation-only;
- generated changes are limited to the expected corrective PDF, manifest,
  review metadata and package report; no incidental generated scientific
  asset changed;
- scoped `git add` was not completed: the sandbox denied creation of
  `.git/index.lock`, and the escalated retry was rejected by the exhausted
  host usage limit. No commit or push exists.

## Residual uncertainty

The correction remains unsubmitted. Its builder PDF/manifest/metadata,
package audit and author-supplied independent direct source-only compile are
current, but the authorized commit/push is blocked by host permissions.
ArXiv's replacement workflow, server PDF, moderation and external mathematical
review are not performed here. The scientific claims remain at the
classifications and evidence chain established by the prior audited
correction task; this task adds no scientific evidence.
