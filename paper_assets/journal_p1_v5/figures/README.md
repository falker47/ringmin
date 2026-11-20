# Figure provenance

Run `python paper_assets/journal_p1_v5/make_figures.py` at the repository root. To reproduce in an empty location, pass `--output-dir DIRECTORY`. The generator uses Matplotlib's PDF backend through Agg, a fixed DejaVu Sans font, a monochrome palette and explicit PDF metadata with creation and modification dates suppressed. It uses no random numbers. The two numerical chain illustrations and seam plot use mpmath at 65 decimal places.

| File | Construction and interpretation |
| --- | --- |
| `01_kernel.pdf` | The radii are R = 3, a = 1, b = 2. The scalar angle is computed from equation (2). The disk centers lie at distance R plus the corresponding radius from the origin. Schematic. |
| `02_necklace.pdf` | V4's rank rule gives (1, 6, 3, 4, 5, 2, 7). Solve the adjacent-angle sum equal to two pi, and accumulate the resulting angles. Theorem 3.2 and Corollary 5.2 establish optimality. The drawn coordinates are numerical. |
| `03_seam.pdf` | Apply the same rule and root solve at n = 8. Shading identifies the overlapping nonadjacent disks 7 and 8, which straddle disk 1. The non-overlap failure is proved in Theorem 5.1. |
| `04_witness.pdf` | Read the first supplied Cartesian witness for n = 14 from the protected certificate JSON. Reconstruct all centers from its rational stereographic parameters. Independently check 14 rational central equalities and all 91 strict outer inequalities before converting to rendering coordinates. Gray fill and callouts identify disks 1 and 2 from the historical reconstruction. The plotted witness has strict slack in every outer pair. |
| `05_ratios.pdf` | Parse the twelve linear rows of `bracket_rows.tex` and the twelve quadratic rows of `quadratic_brackets.tex` as fractions. Divide the endpoints by n² and n³, respectively. Draw each interval with its midpoint as a marker. Filled circles denote the linear family and open triangles the quadratic family. The band gives both bounds on the linear limit and the dotted line gives the quadratic limiting upper bound from revised Paper II. All three constants are read from `numbers.tex`. |
| `06_deficits.pdf` | For k = 1, 2, 3 and each n from k+2 through 21, solve the published chain equation and evaluate the three angles in (8). Rings identify the first negative value of each series. The plotted values are numerical illustrations of the exact seam theorem. |

The certificate source is [the tracked global bracket artifact](../../../reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json). Its complete file SHA-256 in the source checkout is `cfb95a8354c9ea0529f5ece85118712a3e94c36aed1e14a43b6f32c6e98549db`. The canonical certificate-field digest is `6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0`. Full lower coverage can be reproduced with `python -I -S verify_global_brackets.py`.

The quadratic table is reproduced directly from the [general-radii source table](../../general_radii/quadratic_brackets.tex). The plot regression compares both series and their end-to-end normalizations with the exact endpoints in the [24 certificates](../../general_radii/certificates/).

The checked renderer used Python 3.14.3, mpmath 1.3.0 and Matplotlib 3.10.9. A second run in a fresh directory reproduced all six vector files byte for byte. Different font or renderer versions can change PDF serialization. The automated test compares independent interpreter runs with different hash seeds.
