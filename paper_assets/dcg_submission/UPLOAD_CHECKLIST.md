# DCG upload checklist

Package prepared from accepted commit
`6749d6b165f982136117481be322c8beaec223ce` on 2026-09-28.
The four TeX files and PDF are byte-identical to that commit. The package
requires independent review before human upload. No submission has been made.

## Files and upload roles

| File | Role |
|---|---|
| `ringmin_dcg.tex` | Main editable manuscript |
| `seam_appendix.tex` | Required manuscript input |
| `bracket_rows.tex` | Required table input |
| `coverage_rows.tex` | Required table input |
| `ringmin_dcg.pdf` | Compiled manuscript, 19 pages |
| `ringmin_dcg_sources.zip` | Convenient source upload: exactly the four TeX files at ZIP root |
| `cover_letter.txt` | Paste into the cover-letter field, or upload if the portal accepts text |
| `SUBMISSION_MANIFEST.json`, `SHA256SUMS` | Local integrity and review records |
| `UPLOAD_CHECKLIST.md`, `.gitattributes` | Local instructions and byte-preservation settings |

All manuscript inputs belong together in one directory. There are no custom
style/class files, external figures or bibliography databases. Standard TeX
distribution dependencies are listed in the manifest. Choose the portal's
source-upload route (ZIP or individual TeX files); do not upload both copies.
The last four local support files are not journal supplementary material.
Do not upload the repository's scientific code or certificates: the manuscript
already cites their [Zenodo archive](https://doi.org/10.5281/zenodo.22849826).

## Human upload sequence

1. Obtain independent acceptance of this exact package and its manifest hashes.
2. Open [DCG Editorial Manager](https://www.editorialmanager.com/dcge/)
   through the journal's submission link. The retrieved public landing page on
   2026-09-28 displayed "Site under development. Do not use for live manuscript
   submission." Check that this warning no longer applies before uploading;
   if it persists, use the journal's contact route to confirm the live portal.
3. Enter the title and corresponding author exactly as on the PDF. Transfer the
   accepted abstract, six keywords and MSC codes from page 1; confirm the
   declarations and data-availability answers against the manuscript.
4. Supply the source files and PDF in their manuscript roles. Paste the complete
   cover letter. Identify arXiv:2607.28654v2 and the separate arXiv:2609.13630
   sequel in any related-publication fields.
5. Complete the private metadata and author attestations below. Check the
   portal-generated PDF, file ordering and resolved references before the
   human author approves submission.

## Human-only fields and decisions

- Full postal address, telephone and fax if requested by the live form: enter
  privately in Editorial Manager. No home address or number is stored here.
- Confirm current affiliation, corresponding-author email, and account details.
- Suggest one current Co-Editor-in-Chief using the portal's current choices.
  The [editorial board](https://link.springer.com/journal/454/editorial-board)
  lists Kenneth L. Clarkson, János Pach and Csaba D. Tóth. The guidelines list
  only Pach and Clarkson; reconcile the live form before choosing. No editor
  has been selected by this task.
- ORCID only if the author has one and supplies it; none has been inferred.
- Personally confirm originality, related-work disclosure, absence of
  simultaneous journal consideration, author approval and any permissions,
  funding/conflict questions or other attestations presented by the form.
  The cover letter makes no unverified exclusive-submission assertion.

## Guidelines rechecked on 2026-09-28

The live [DCG submission guidelines](https://link.springer.com/journal/454/submission-guidelines)
retain Editorial Manager submission, complete editable LaTeX and compiled PDF,
a 150-250-word abstract, 4-6 keywords, MSC, corresponding-author details,
Statements and Declarations, data availability and substantive LLM disclosure.
The Springer template remains recommended, not mandatory; the accepted
`article` format is retained. No change to these requirements was found relative
to the accepted preparation record. The editor-list discrepancy and portal
warning above are current observations, not a confirmed change of journal policy.

## Integrity and independent compilation

`SUBMISSION_MANIFEST.json` hashes every payload file, identifies accepted
source paths and records deterministic build settings. `SHA256SUMS` also hashes
the manifest; it excludes only itself. Its own hash is recorded in the task
evidence. Neither file claims external mathematical acceptance of this package.

For an independent build, extract the source ZIP into an empty directory with
a standard TeX installation. Set `SOURCE_DATE_EPOCH=1789776000` and
`FORCE_SOURCE_DATE=1`, then run this command twice from that directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder ringmin_dcg.tex
```

The package was tested with pdfTeX 1.40.28 (TeX Live 2025). Other TeX/font
versions may produce different PDF bytes. The accepted manuscript's dated
provenance wording is preserved verbatim; current internal acceptance is
identified by this package's manifest. The source-to-claim map remains
[available at the accepted commit](https://github.com/falker47/ringmin/blob/6749d6b165f982136117481be322c8beaec223ce/paper_assets/journal_dcg/SOURCE_MAP.md).
