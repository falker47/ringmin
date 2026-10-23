# Paper II: JoCG Submission Package

This separate journal manuscript of arXiv:2609.13630 is prepared for submission
to the Journal of Computational Geometry (JoCG), the destination approved by
the author on 2026-10-24. Independent review of this revision remains required.
No submission, arXiv replacement or external scientific acceptance is implied.

Read [main.pdf](main.pdf), then the supplements needed for the claims under
review. [CLAIM_PROOF_MAP.md](CLAIM_PROOF_MAP.md) maps the complete chain;
[UPPER_DEPENDENCIES.md](UPPER_DEPENDENCIES.md) details the upper endpoint.
[READINESS.md](READINESS.md) records gates and limits; [PRIOR_ART.md](PRIOR_ART.md)
records the scoped comparison.

## Package Index

| Item | Role |
|---|---|
| main.tex / main.pdf | Model, complete global-limit and finite-word LP proofs, endpoint theorems |
| S1: Proposition 7 supplement | Unchanged complete lower-endpoint proof L1--L8, rational certificate and checkers |
| upper_supplement.tex / upper_supplement.pdf (S2) | Reflected-block transfer, implicit parameters and fourth-block saving |
| checks/ | Bounded verification; no test replaces an all-n proof |
| build.py / BUILD_REPORT.json | External-directory builds and actual TeX input hashes |
| verify_package.py / MANIFEST.json | File integrity and package/source identity |
| source_bundle.zip | Portable review sources, PDFs, checkers and unchanged S1; internal manifest |

In a repository checkout S1 is
[the existing package](../asymptotic_sequel/proposition7_supplement/README.md),
pinned to baseline `75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae`.
In the ZIP it is copied byte for byte into `lower_supplement/`.
No old ops dossier is needed to read or execute the package.

## Reproduce

Python >=3.11 and pdfLaTeX with standard packages (including lineno) suffice
for the builds and endpoint checks. SciPy is required only by the optional
word-LP discovery/checker; it is already a project dependency.

From this directory, or an extracted source_bundle.zip:

```sh
python -I -S verify_package.py
python -I -S check_reproducibility.py --require-delivered
python -I verify_math.py --with-lp
```

The aggregate `verify_math.py` already runs S1 verification and integrity
controls once. Those scripts can also be run separately inside S1.
Upper rational commands are indexed in UPPER_DEPENDENCIES.md.
The builder copies only each standalone TeX input to a fresh external temporary
directory, uses three no-shell-escape passes, rejects reference and box warnings,
and rebuilds S1 without replacing its preserved PDF. It records actual output
hashes and system input hashes. Other TeX versions may change bytes/pagination.
The non-mutating `check_reproducibility.py` compiles every document twice in
separate temporary directories and requires identical bytes within the current
TeX environment. `--require-delivered` additionally requires the delivered PDF
hashes; use it with the recorded environment. CI runs package integrity and
`verify_math.py --with-lp` in its existing Python job. A separate push-only
LaTeX workflow runs on package/S1/workflow changes, without duplicate PR builds
or uploaded artifacts. Its TeX version may differ from the delivered build.
For standard-library-only arithmetic replay, omit `--with-lp` and use `-I -S`.
To author a new revision, run `python build.py`, then `python build.py --export`
after all package documentation is final. Ordinary verification never exports
or replaces the delivered PDFs or manifest.

## Scientific Scope

The package reconstructs existing exact theorems and their finite arithmetic
support. Neither explicit endpoint is sharp by this work. It gives no new
finite global optimum, efficient high-precision algorithm or global contact
classification. Internal adversarial review is separate from journal review.
