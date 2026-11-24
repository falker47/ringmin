# Mathematical comparison with the integrated draft

The mathematical text, table contents, figure captions and plotted data agree with the integrated Paper I at commit `040d301e600acc12430f76333ec3243268dd3d3e`, apart from the wording changes listed under [Editorial and typesetting changes](#editorial-and-typesetting-changes). The comparison covers all nine scientific sections and all three appendices, including ordinary prose between displays. [Reviewed source](https://github.com/falker47/ringmin/tree/040d301e600acc12430f76333ec3243268dd3d3e/paper_assets/journal_p1_v5) · [Executable comparison](../../tests/test_journal_p1_jogo.py)

## Normalized source comparison

The regression expands the reviewed table and appendix inputs in their original positions. It discards float placement, panel wrappers, image sizing and the page break before §9, maps the six graphic filenames, and collapses whitespace. It retains the captions, labels, mathematical delimiters, signs, tolerances, indices, row entries and proof text. The reviewed string contains 54,787 characters. Applying the listed wording changes to it yields the JOGO string exactly, with 54,877 characters. The UTF-8 SHA-256 digests are:

~~~text
reviewed  2d6c96dd7319ea76b820c9968746c4a3a60284c343761631fd6eb2829569cd7a
JOGO      39b3de31ea27b2b964624341068be7dbbe2cfb118ff14bfae2ce21eb3458bd36
~~~

| Material compared | Result |
| --- | --- |
| Formal statements and proofs | Three theorem environments, two lemmas, one corollary and five proof environments agree. The restated seam theorem, Lemmas A.1 and A.2 and their proofs in Appendix A are included in the full-text comparison. The shared theorem counters and the mathematical macros agree separately. |
| Equations and inequalities | All 13 equation environments, one numbered align environment, two unnumbered align environments, 37 bracket-delimited displays and the inline mathematics agree. All 21 explicit Appendix A equation tags are retained. |
| Tables | All eight tables agree in order, labels, cell contents and source precision. Their captions agree apart from the square-radius wording in Table 5. This includes both 12-row finite-bracket tables and all three appendix tables. |
| Figures | All six original vector PDFs have identical bytes in the new directory. Their cross-reference labels and reading order agree. Their captions agree apart from the square-radius wording in Figure 5. Each illustration now occupies its own single-column float. |
| Material outside the scientific body | The abstract retains the complete results passage beginning with “For radii”. The numerical macros and the revised Paper II comment are identical to the base, apart from the added macro `\CtwoLower` for the cited lower bound on $C_2$. The declaration text, including the AI paragraph, agrees verbatim. All 16 cited keys retain their DOI bindings. |

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

The Springer Nature class supplies the author block, keywords, MSCs, theorem styles, captions, and numerical bibliography in citation order. The manuscript date is printed on the title page. The abstract names the input domain explicitly and then gives the two computed families. Data and code availability displays the requested commit marker. The author reminder beside the AI declaration is a TeX comment. The bibliography supplies publisher locations for the two chapters and the book.

The radii $1^2,\ldots,n^2$ are called square radii, as in the revised Paper II. The regression applies these six replacements to the reviewed text. Each reviewed phrase occurs exactly once. Labels, file names and the TeX comment above Table 5 keep the word “quadratic”.

| Location | Reviewed | JOGO |
| --- | --- | --- |
| §1, method overview | For the quadratic family it gives | For square radii it gives |
| §1, companion results | For quadratic radii it proves | For square radii it proves |
| §9 heading | Quadratic radii | Square radii |
| §9, deletion example | At quadratic $n=14$ | For square radii and $n=14$ |
| Table 5 caption | Certified global brackets for quadratic radii. | Certified global brackets for square radii. |
| Figure 5 caption | Normalized linear and quadratic brackets. | Normalized brackets for linear and square radii. |

The companion summary in §1 also cites the lower bound $(434+4\sqrt2)/(1587\pi)\le C_2$ from the revised Paper II, whose abstract states it and whose supplement proves it. Figure 5 still draws only the upper bound on $C_2$, since the lower bound lies about 0.0004 below it. The sentence that introduces the figure therefore names the bounds on $C_*$ and the upper bound on $C_2$. The regression applies this seventh replacement after the six above.

Further wording changes follow the November 2026 proof check, whose [report](../../docs/referee/proofcheck-2026-11.md) found no error and no gap. The regression applies them after the seven replacements above. Each reviewed phrase occurs exactly once.

| Location | Reviewed | JOGO |
| --- | --- | --- |
| §5, outline of Appendix A | A fan decomposition bounds every triangle defect below by $\delta_R=\theta_R(n,k)+\theta_R(k,n-1)-\theta_R(n,n-1)$. | Every triangle defect is bounded below by $\delta_R=\theta_R(n,k)+\theta_R(k,n-1)-\theta_R(n,n-1)$, and a fan decomposition writes each path slack as a sum of such defects. |

These changes leave the evidence and epistemic status of every claim as recorded in the [integrated claim map](../journal_p1_v5/CLAIMS_DIFF.md).

Run the comparisons from the repository root.

~~~console
python -m pytest tests/test_journal_p1_jogo.py
~~~
