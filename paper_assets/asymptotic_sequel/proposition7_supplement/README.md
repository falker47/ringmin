# Proposition 7: standalone journal supplement

This directory is the complete review package for the explicit lower endpoint
in Paper II, arXiv:2609.13630. Begin with **supplement.pdf**; its complete
proof is in **supplement.tex**. DEPENDENCIES.md maps L1–L8 to hypotheses,
proofs and provenance. No repository history or old task dossier is needed.

The exact claim is

```text
C_* >= C_term + eta_width
0.14056946887766098063257 < C_term + eta_width
                        < 0.14056946887766098063392.
```

The package reconstructs an existing theorem for independent review. It does
not claim that the bound is sharp for full geometry or that a journal has
accepted it. Published Paper I and Paper II sources remain unchanged.

## Verify without the repository

Requirements: Python >=3.11, standard library only. Copy this directory to
any location and run from it:

```sh
python -I -S verify.py
```

Expected final line:
`PASS supplement checks; analytic proof supplies universal quantifiers`.
Assertions must remain enabled; `-O` is rejected. The verifier regenerates
all rational enclosures in memory, compares certificate.json exactly,
checks the literal endpoint inequalities, checks 144 directed-rational
deletion fixtures and replays the exact shared-crossing checker. It then
checks every packaged file against MANIFEST.json. If run in the repository,
it also checks available source-input hashes after CRLF-to-LF normalization.
The local .gitattributes preserves the exact packaged bytes on checkout. Without the repository zero
source-input checks is expected: source provenance is recorded, while all
analytic proofs and arithmetic inputs needed to verify the claim are local.

The preserved checkers can also be run separately:

```sh
python -I -S check_width_optimum.py
python -I -S check_finite_crossing.py
python -I -S check_integrity_controls.py
```

Those scripts contain a few extra historical diagnostic outputs; their
`x_star` name is the supplement's lower-bound `z_*`, never the upper-bound
parameter. certificate.json uses the unambiguous `z_star` name.
An authoring-only certificate regeneration is available with
`python -I -S verify.py --write-certificate --skip-manifest`.
The `--skip-manifest` mode does not establish package integrity.

## Compile

Use pdfLaTeX with standard packages amsmath, amssymb, amsthm, geometry, lmodern, booktabs and hyperref.
No bibliography program, shell escape or external figure is required.
To keep build products outside the hashed directory:

```sh
mkdir build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build supplement.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build supplement.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build supplement.tex
```

Three passes stabilize the table of contents and references from a fresh directory.
Open build/supplement.pdf and inspect the final log for unresolved references
and overfull boxes. The checked PDF in this package is supplement.pdf.
Different TeX versions or PDF timestamps may change rebuilt PDF bytes;
MANIFEST.json authenticates the delivered PDF, not an arbitrary rebuild.
The input source and arithmetic certificate are deterministic. The technical
report gives the actual build environment and observed reproducibility.

## Files and authority

- supplement.tex / supplement.pdf: complete mathematical exposition.
- check_width_optimum.py / check_finite_crossing.py: exact original checkers.
- verify.py: exact endpoint/certificate checks, new finite deletion scorer,
  and package integrity verification.
- check_integrity_controls.py: isolated standalone replay and negative controls
  for a changed certificate, changed document and disabled assertions.
- certificate.json: essential rational intervals, signs and multipliers.
- DEPENDENCIES.md: claim/hypothesis/proof/check map and source closure.
- VERIFICATION.md: actual checks, independent review scope and residual limits.
- arithmetic.log: complete output of the delivered arithmetic verification.
- .gitattributes: preserves authenticated output bytes across Git platforms.
- MANIFEST.json: source provenance and SHA-256 of every other package file;
  it explicitly excludes its own hash to avoid a circular manifest.

Neither a manifest nor a script's PASS label proves the analytic arguments.
The referee must assess the written proofs. Review State Registry, journal
submission, arXiv updates and finite global enumeration are outside this task.
