# Figure provenance

The PDFs use vector paths, embedded DejaVu fonts and grayscale fills, outlines and line styles. Creation and modification dates are omitted. The committed files were produced with CPython 3.14.3 and Matplotlib 3.10.9.

| Figure | Inputs and construction |
|---|---|
| `line_geometry.pdf` | Two model radii, 1 and 4/9. Disk centers are (0,1) and (4/3,4/9). The horizontal center separation equals twice the geometric mean, so the disks touch on the common shelf. Rendering uses floating-point coordinates. |
| `reflected_cells.pdf` | Symbolic alternating low/high cells and an eight-rank example of Theorem 6. A slab on ranks 1 through 6 maps 2 to 6 and 6 to 2, with all other ranks fixed. The dashed cell arc denotes the direct high-pair constraint. |
| `finite_brackets.pdf` | Twelve pairs of original bracket endpoints for n=3 through 14, copied verbatim from Paper I v4 into `bracket_rows.tex`. The generator checks the table digest and rational widths before dividing by n². Midpoints and half-widths are converted to plotting coordinates after normalization. The asymptotic lower line reads `numbers.tex`. A numeric upper macro adds the upper line. |

The SHA-256 of the source bracket table in LF form is `58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1`.

Run `python paper_assets/journal_p2_v4/make_figures.py` from the repository root. To replay from the official extracted file, pass `--brackets .codex_inputs/arxiv/p1_v4/bracket_rows.tex`. Pass `--output` and a fresh directory to compare the replay with the committed figures.

[Paper I v4 source](https://arxiv.org/src/2607.28654v4) · [Paper II v3 source and supplements](https://arxiv.org/src/2609.13630v3)
