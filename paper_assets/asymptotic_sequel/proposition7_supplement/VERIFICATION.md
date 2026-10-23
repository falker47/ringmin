# Technical verification report

Date: 2026-10-23. Mode: STRICT. Target: Proposition 7 of Paper II,
arXiv:2609.13630. Authoring baseline:
`6167e36cf6f80a6a7a7a6b41518a6b3f7155295d`. Scientific inputs:
`3beb8d70c5b3748d370a92855847bdf574e5a14f`.

## Mathematical reconstruction

The 14-page supplement contains the complete L1–L8 dependency chain and
the required global-limit existence argument. DEPENDENCIES.md specifies
each hypothesis and source section. No analytic dependency is delegated to
an operational dossier, a PASS label or a finite enumeration.

The main safeguards explicitly proved are: all-pairs deletion with original
radii; exact cyclic closure; reflected assignment rather than presumed tour
realization; arbitrary consecutive deletion runs and the seam; constants
3+40+11=54; one common energy for all crossings; both scalar minimax branches;
global cubic optimality including all boundary faces and F<=0; and fixed
t, then n->infinity, then t->1. The lower-bound root is named z_* throughout.

A separate internal reviewer read the entire mathematical source, dependency
matrix, verifier and both original checkers and reported no actionable
mathematical or verifier finding. The reviewer independently ran
`python -I -S paper_assets/asymptotic_sequel/proposition7_supplement/verify.py --skip-manifest`
with exit 0. This review excluded unfinished PDF/manifest packaging. The
subsequent source edits were typographic (line breaking, contents layout and
PDF metadata), not changes to mathematical statements or coefficients.
This is an internal agent review, not peer review, external acceptance or a
formal proof-assistant certificate.

## Exact arithmetic and finite checks actually run

Environment: Windows; Python 3.14.3; standard library only, no new dependency.
Commands below use the package directory as working directory unless a
repository-relative path is shown.

| Command | Exit and material result | Scope and independence |
|---|---|---|
| `python -I -S verify.py --write-certificate --skip-manifest` | 0; certificate generated; literal strict endpoint comparisons passed | Fresh rational parameter arithmetic, positive KKT gates and exact certificate. Coupled to the preserved arithmetic checker; independent of production modules/results. This invocation does not check hashes. |
| `python -I -S verify.py --skip-manifest` | 0; certificate exactly matched; full output saved in arithmetic.log | 144 directed-rational deletion fixtures at n=102,103,104,105; rotations/reversal, runs, seam and all four outer/inner parity pairs. New integer-square-root scorer independent of inherited interval helpers; uses their freshly certified q bounds. |
| `python -I -S check_width_optimum.py` | 0; `PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers` | Original checker, exact scientific Git blob. Rational Taylor/binomial intervals, polynomial identities, signs, KKT gates and floor negative controls. |
| `python -I -S check_finite_crossing.py` (also invoked by verify.py) | 0; 48 prescribed measures and 16 tour/cutoff cases passed | Original exact checker; shared energy up to 8 crossings, equality boundaries, F_n signs, malformed parameters and negative controls. No general tour enumeration. |

The exact enclosure is asserted against these literal rational endpoints:

```text
0.14056946887766098063257 < C_term+eta_width
                        < 0.14056946887766098063392.
```

certificate.json records the essential rational intervals for tau, q, pi,
D_i, z_*, all four G sign gates, F(u), L(u), rho, both multipliers and the
full coefficient. Every endpoint is a fraction, not a floating approximation.
For example the multiplier enclosures printed by the original checker are

```text
0.00035105290142936543670 < lambda_1 < 0.00035105290142936940356
0.00059414888796317986218 < lambda_2 < 0.00059414888796318518264.
```

The old checker's printed `x_star` means this supplement's lower-bound z_*.
Its outward formatting widens the displayed root interval by one decimal
unit; the strict signs at the original exact z_- and z_+ are checked directly.

## Compilation, PDF and portability

Existing engine: pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025), kpathsea
6.4.1, LaTeX2e 2025-11-01 / L3 2026-01-19. Poppler supplied pdfinfo,
pdftoppm and PDF rendering. No package installation occurred.

The final build used:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -recorder -output-directory=build supplement.tex
```

An independent fresh-directory build outside the repository ran that command
three times: exits **0, 0, 0**. Its final log has **0 warnings, 0 undefined
references/citations, 0 overfull and 0 underfull boxes**. The recorder contains
no repository input path. It reproduced the delivered PDF byte for byte.
Date, trailer ID and optional PTEX metadata are suppressed in the source.
The delivered PDF is A4, 14 pages, unencrypted, with no JavaScript or forms.
All 14 pages were rendered at 1400-pixel maximum dimension and visually
inspected. After the contents-page refinement, the changed pages were
rechecked and the remaining rendered pages retained their bytes. Equations,
symbols, headings, page numbers, reference list and source paths are readable
and remain inside the margins.

Delivered PDF SHA-256:
`a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568`.

Earlier authoring failures were retained in the task evidence: PowerShell
initially passed a literal output-directory variable; correcting argument
quoting fixed it. Unused mathtools and optional microtype were unavailable;
they were removed instead of installed. Initial overfull lines and a
reference-rerun warning were resolved by line breaking and additional passes.
The app's built-in compiler was unavailable because Windows sandbox setup
was incomplete; the installed local engine produced the verified PDF.

## Provenance and protected resources

MANIFEST.json records seven immutable source inputs, their Git-blob and
checkout SHA-256 values, and every packaged output except itself. Checkout
CRLF versus Git LF is recorded explicitly; normalized input content must
match the pinned commit. Both delivered original checkers are byte-identical
to their scientific Git blobs. New source/checker hashes identify the exact
authoring additions over the base commit; the Git commit carrying the
manifest identifies the delivered package revision.

A preflight SHA-256 snapshot of **759 existing tracked files**, excluding
only the authorized CURRENT_STATUS.md update, matched after construction.
This includes published papers and generated assets, source research notes,
knowledge ledgers, production code, results and independent verifier.
The original untracked ZIP was preserved in the original checkout and never
copied into or staged from the isolated worktree. No Review State Registry
write, PR, merge, tag, release, workflow dispatch or submission was performed.

## Residual limits

No material proof gap was identified by reconstruction or the internal review.
Independent external mathematical review remains necessary. Finite fixtures
do not prove all-order or all-n statements. The bound is not asserted sharp
for full geometry or the common-chain minimax; only the stated fixed-cutoff
width functional is globally optimized. No upper-bound claim is introduced.
No finite global optimum certificate was regenerated. The production test
suite and full frontier verifier were not run: their protected code/artifacts
were not changed and they do not verify this asymptotic proof.

Same-engine PDF reproducibility was observed; other TeX versions may produce
different bytes. The package manifest detects alterations, not adversarial
replacement of both files and manifest; Git provenance supplies that anchor.
Hosted CI for the final commit is not asserted or used as mathematical evidence.

## Final package integrity controls

`python -I -S verify.py` passed with exit 0, checking every output hash
and seven repository input hashes. Repository input verification normalizes
CRLF to LF, while retaining both raw hashes for provenance. The package-local
.gitattributes disables Git newline conversion so authenticated output bytes
survive fresh checkouts on different platforms.

`python -I -S check_integrity_controls.py` passed with exit 0. A separate
temporary standalone copy passed the full verifier with zero repository
inputs. Altered certificate content and altered README bytes were rejected;
Python -O was rejected explicitly. Only the temporary copies were changed.
These are integrity and portability checks, not analytic proofs.
