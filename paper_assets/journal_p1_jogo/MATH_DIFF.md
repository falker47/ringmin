# Mathematical comparison with the integrated draft

The mathematical text, table contents, figure captions and plotted data agree with the integrated Paper I at commit `040d301e600acc12430f76333ec3243268dd3d3e`. The comparison covers all nine scientific sections and all three appendices, including ordinary prose between displays. [Reviewed source](https://github.com/falker47/ringmin/tree/040d301e600acc12430f76333ec3243268dd3d3e/paper_assets/journal_p1_v5) · [Executable comparison](../../tests/test_journal_p1_jogo.py)

## Normalized source comparison

The regression expands the reviewed table and appendix inputs in their original positions. It discards float placement, panel wrappers, image sizing and the page break before §9, maps the six graphic filenames, and collapses whitespace. It retains the captions, labels, mathematical delimiters, signs, tolerances, indices, row entries and proof text. Both normalized strings contain 54,787 characters and have the same UTF-8 SHA-256.

~~~text
reviewed  2d6c96dd7319ea76b820c9968746c4a3a60284c343761631fd6eb2829569cd7a
JOGO      2d6c96dd7319ea76b820c9968746c4a3a60284c343761631fd6eb2829569cd7a
~~~

| Material compared | Result |
| --- | --- |
| Formal statements and proofs | Three theorem environments, two lemmas, one corollary and five proof environments agree. The restated seam theorem, Lemmas A.1 and A.2 and their proofs in Appendix A are included in the full-text comparison. The shared theorem counters and the mathematical macros agree separately. |
| Equations and inequalities | All 13 equation environments, one numbered align environment, two unnumbered align environments, 37 bracket-delimited displays and the inline mathematics agree. All 21 explicit Appendix A equation tags are retained. |
| Tables | All eight tables agree in order, captions, labels, cell contents and source precision. This includes both 12-row finite-bracket tables and all three appendix tables. |
| Figures | All six original vector PDFs have identical bytes in the new directory. Their captions, cross-reference labels and reading order agree. Each illustration now occupies its own single-column float. |
| Material outside the scientific body | The abstract retains the complete results passage beginning with “For radii”. The numerical macros and the revised Paper II comment are identical to the base. The declaration text, including the AI paragraph, agrees verbatim. All 16 cited keys retain their DOI bindings. |

## Figure files

The reviewed filenames are relative to the integrated draft's figures directory. The JOGO package places them beside the manuscript as requested by the journal.

| Reviewed file | JOGO file | SHA-256 of both files |
| --- | --- | --- |
| 01_kernel.pdf | Fig1.pdf | 56bd1bf168c41bb958bdc5f5eecc32c1cc11eb55439c06b9e940c076f7d884a4 |
| 02_necklace.pdf | Fig2.pdf | 2c62cde67ae94c0934a393c196c6126466ccb9637d3993b9ffa7ba85fac562c3 |
| 03_seam.pdf | Fig3.pdf | cf32ba005067f8298ecf99ee29f5ccc0026cc8d12f66309b72958f802e951e9a |
| 04_witness.pdf | Fig4.pdf | 9318ed70e5a46f150e29a770aa2683f7bc86c7366bc0d149bac9b0c8e701d15f |
| 05_ratios.pdf | Fig5.pdf | 10818bdee83bd9edc7f8f8f5929dad0bd609ce14120f37711d442de2db4e8c18 |
| 06_deficits.pdf | Fig6.pdf | 98299cd045545272a8627e2b14a0eef9f8649ed1fe202cb8adb1c9fc2c373035 |

## Editorial and typesetting changes

The Springer Nature class supplies the author block, keywords, MSCs, theorem styles, captions, and numerical bibliography in citation order. The manuscript date is printed on the title page. The abstract names the input domain explicitly and then gives the two computed families. Data and code availability displays the requested commit marker. The author reminder beside the AI declaration is a TeX comment. The bibliography supplies publisher locations for the two chapters and the book. These changes leave the evidence and epistemic status of every claim as recorded in the [integrated claim map](../journal_p1_v5/CLAIMS_DIFF.md).

Run the comparisons from the repository root.

~~~console
python -m pytest tests/test_journal_p1_jogo.py
~~~
