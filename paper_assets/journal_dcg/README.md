# Ringmin finite journal manuscript for DCG

The revised standalone **working submission manuscript** for Discrete
& Computational Geometry is separate from the public finite arXiv v2 and the
asymptotic sequel. It has not been submitted, peer reviewed, or declared
publication-ready by this task.

The [19-page PDF](ringmin_dcg.pdf) is built from [ringmin_dcg.tex](ringmin_dcg.tex),
[seam_appendix.tex](seam_appendix.tex), and two generated table inputs.
There are no external figures, private style files or bibliography databases.
Standard `article` formatting is used for this working version; the Springer
template is encouraged, not required, by the
[DCG instructions](https://link.springer.com/journal/454/submission-guidelines)
checked on 2026-09-19.

## Scope

The exact finite claim is `L_n < R*(n) <= U_n` for n=3,...,14, of rational
width exactly `10^-11`. The seam package proves the general fixed-order
criterion, eventual persistent failure for every fixed k, and the complete
k=1,2,3 classifications with onsets 8,13,17. It includes no explicit all-k
onset formula. Appendix A contains every required proof and rational bridge;
no repository proof note is an essential paper reference.

Historical float64 Stage-A/Top-K pruning is not a finite-proof premise.
Historical floating regimes remain numerical interpretation, not exact
classifications of optimizing orders or contact graphs. Strict slack at U
is distinguished from strict slack at the infimum. No new global result for
n>14 or asymptotic result is asserted.

## Build and reproduce

From the repository root, with Python >=3.11 and `pdflatex` on PATH:

```text
python paper_assets/journal_dcg/build.py
```

This runs pdflatex twice with `-no-shell-escape`, fixes SOURCE_DATE_EPOCH,
suppresses PDF date/path identifiers, and writes the PDF and
[BUILD_MANIFEST.json](BUILD_MANIFEST.json). Logs and renders stay in ignored
`reproducibility/.work/journal_dcg/`. The manifest records compiler version,
source and protected-input hashes, and PDF hash. Local Git attributes preserve
LF source endings; protected text hashes normalize CRLF to LF, while archived
originals retain byte hashes. Two final local builds gave
identical PDF bytes; other TeX/font versions may change bytes or pagination.

The table exporter reads the preserved certificate without modifying it:

```text
python paper_assets/journal_dcg/export_tables.py
```

It generates [bracket_rows.tex](bracket_rows.tex) and
[coverage_rows.tex](coverage_rows.tex). Do not hand-edit the derived tables.

The complete finite check needs only Python's standard library:

```text
python -I -S verify_global_brackets.py
```

It verifies all twelve cases, original-input binding, exact lower coverage
and existential upper witnesses, without replaying the historical search.
The paper retains the mathematical/computational code/data pin
`6c16af422d1cb38641c62d43b6e0e547921b9ba9`; the manuscript is identified by
the task commit containing this directory. Source hashes are not execution
attestation. The frozen pre-submission snapshot is release
`v1.1.0-dcg-presubmission`, commit
`80919666c3c54f8ce20cf66c456d413f6a2c075f`, archived under version DOI
[10.5281/zenodo.22849826](https://doi.org/10.5281/zenodo.22849826).
The accepted repository baseline read live on 2026-09-28 is
`b1480803749e08197bce37442f0953c550e2a5e4`. It postdates the release and
is outside that deposit, as is this editorial patch. The accepted exact
finite certification and integrated fixed-order seam theorem retain their scope.

## Review package and metadata

The [source map](SOURCE_MAP.md) records dependencies and editorial decisions.
The [historical revision evidence](../../ops/TASK-20260919__dcg_presubmission_revision/EVIDENCE.md)
retains its preparation-time context. The
[current compliance evidence](../../ops/TASK-20260928__dcg_submission_compliance/EVIDENCE.md)
records fresh local checks separately from inherited acceptance. The current
editorial baseline is `b1480803749e08197bce37442f0953c550e2a5e4`;
the mathematical code/data pin remains unchanged. The software citation uses
[CITATION.cff](../../CITATION.cff) and the
[persisted Zenodo metadata](../../ops/TASK-20260926__archive_evidence_integration/evidence/zenodo_record.json).

The paper has a 184-word abstract by whitespace count, six keywords, MSC,
the author's already-public affiliation/contact details, declarations and
disclosure of substantive AI assistance. The author confirmed no specific
funding and no relevant conflicts during initial preparation. No ORCID was supplied or
inferred. Actual submission requires author approval and portal metadata.
This patch is not automatically accepted and does not update the Registry.
The sole next atomic task is independent review of the exact
submission-compliance commit; if accepted, prepare the final DCG submission
package and cover letter.
