# Referee notes for the JOGO draft

| Question | Evidence and editorial action |
| --- | --- |
| Does the lower bound cover every cyclic order, including ties at the proposed endpoint? | Section 6 and Appendix C use a strict rational buffer at the lower endpoint. The isolated verifier replays all 24 cases with linear and square radii. At the upper endpoint, it checks explicit rational placements. The tables display intervals of width $10^{-11}$. |
| Does choosing a Supnick tour already solve the packing problem? | Section 3 attributes the classical tour result to Supnick and applies it to the adjacent-chain relaxation. The full geometric claim through seven linear radii uses a separate all-pairs feasibility argument. Appendix A proves the first three seam onsets with six exact bridges. |
| Does the reported floating set describe every optimizer? | Table 4 and its scope paragraph identify the reported configurations as individual numerical reconstructions for $n \ge 8$. The strict separation of a witness at the upper endpoint establishes feasibility there. Contact structure at the actual optimum remains open. |
| Can a reader regenerate the published certificates in a fresh checkout? | The linear command formerly tried to read a local arXiv download. It now uses the endpoints and witness order in the tracked original certificate. This is a regression with supplied endpoints. The square-radius search starts from the radius family. Both routes feed the independent rational checker. |
| Which companion result can be checked in the cited public version? | The arXiv v3 preprint gives the linear limit and lower bound. The bibliography now links separately to the immutable revised manuscript for the square-radius limit and its lower bound, and for the sharper upper bounds used in Figure 5. Before journal submission, align the citation with the public revision that contains those results. [Public preprint](https://arxiv.org/abs/2609.13630v3) · [Revision](https://github.com/falker47/ringmin/blob/6157a64f7628e327b390d9ddd21dd3507d6035a2/paper_assets/journal_p2_sidma/main.pdf) |
| Which snapshot will remain retrievable after integration? | The availability section supplies the original certificate digest and archived release DOI. The general-radii revision marker awaits the integration commit. Before submission, the author can insert that SHA and confirm the disclosure of assistance used. [Data and declarations](main.tex) |

## Reproducing the tables, figures and checks

From the repository root, supply writable output directories to the exporters.

~~~console
python paper_assets/journal_p1_jogo/export_tables.py --output-dir build/jogo-tables
python paper_assets/journal_p1_v5/make_figures.py --output-dir build/jogo-figures
python -I -S paper_assets/general_radii/verify_radii_certificate.py --all
python -I -S verify_global_brackets.py
python -m pytest tests/test_general_radii.py tests/test_journal_p1_v5.py tests/test_journal_p1_jogo.py
python paper_assets/journal_p1_jogo/build.py --output build/jogo.pdf --submission-zip build/jogo.zip
~~~

The table exporter computes the two endpoint tables and the coverage table from the original certificate records. It typesets the five theorem, proof and interpretation tables from the reviewed integrated manuscript. The regression compares all eight bodies with the journal source. The figure generator reconstructs all six plots from its tracked inputs. The [general-radii commands](../general_radii/README.md) regenerate the certificate JSON files for individual cases.
