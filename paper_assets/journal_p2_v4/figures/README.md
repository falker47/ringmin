# Figure provenance

The two vector PDFs use embedded DejaVu fonts and omit creation and
modification dates. They were generated with CPython 3.14.3 and
Matplotlib 3.10.9.

| File | Inputs and construction |
|---|---|
| `line_geometry.pdf` (Figure 1) | Model radii 1 and 4/9 give centers (0,1) and (4/3,4/9). Their horizontal separation is twice the geometric mean at shelf contact. This is the PR #10 diagram. |
| `finite_brackets.pdf` (Figure 2, originally F3) | The twelve Paper I v4 intervals in `bracket_rows.tex` are checked by table digest and exact rational width, then normalized by n². The markers show midpoints with half-width error bars. Both panels draw the interval between the exact decimal macros `CstarLower` and `CstarUpper` in `numbers.tex`. The right panel magnifies it and labels both endpoints. |

The SHA-256 of the bracket table with LF endings is
`58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1`.
Plotting coordinates are converted to floating point after the input checks.

Run `python paper_assets/journal_p2_v4/make_figures.py` from the repository
root. Use `--output` with a fresh directory for a separate replay. Use
`--brackets .codex_inputs/arxiv/p1_v4/bracket_rows.tex` to replay from
the extracted official table. [Paper I v4](https://arxiv.org/abs/2607.28654v4) · [Paper II v3](https://arxiv.org/abs/2609.13630v3)
