# Proposed Paper II integration

These are draft edits for an author-selected revision after independent mathematical review. The uniform case and its explicit lower and upper coefficients retain their hypotheses. The new [section](profiles_section.tex) uses the original article's theorem environments and its existing bibliography key for the shelf-packing paper.

## Title

Replace the title with *Minimum central circles for prescribed radius profiles and a finite-word characterization of their asymptotic constants*.

## Abstract

Replace the opening description of the model and its normalized limit with the following passage.

> For outer radii $N_na_{n,i}$ with uniformly bounded nonnegative marks whose empirical laws converge to $\mu$, we prove that the minimum central radius divided by $N_n n$ tends to a constant $E(\mu)/\pi$. For integer radii $1,\ldots,n$ this gives $R^*(n)=C_*n^2+o(n^2)$, with $C_{\rm term}+\eta_{\rm width}\le C_*\le U_4$. For powers $i^p$, $p>0$, the minimum is $C_p n^{p+1}+o(n^{p+1})$, including a single cubic leading coefficient for square radii.

After the description of the line reduction, add the following sentence.

> With marks bounded by $M$, balanced finite words on $k$ quantile types of length $r$ give a bracket for the limiting ring coefficient of width $M(1/k+1/r)/\pi$, before numerical evaluation of the type costs.

Keep the explicit reflected-block and lower-bound constructions identified as results for the uniform linear profile. If the concurrent journal draft is adopted, retain its verified numeric macros in the uniform-profile sentence.

## Introduction and placement

After the linear problem and definition of the global radius, add the following paragraph.

> We also consider prescribed arrays of radii whose normalized sizes have a bounded limiting distribution. The leading coefficient depends only on that distribution. This covers continuous and more generally bounded Riemann-integrable profiles sampled on the uniform grid. In particular, it proves convergence for the quadratic family and identifies each power-profile constant through finite programs.

In the summary of results, add the distributional limit, its square-root stability estimate and the quadratic corollary as one item. Qualify the existing numerical bracket by “for the linear profile.” Add the section immediately after the existing finite-word section (§4 of v3), before the explicit geometric upper constructions. Add the single bibliography entry with key $\texttt{sqprofile}$ from [standalone.tex](standalone.tex). Original shelf reference $\texttt{shelf}$ already supplies its citation. The standalone-only closing reference to Paper II belongs to the wrapper.

## Build the standalone section

From the package directory, run the following command three times with an existing temporary output directory in place of $\texttt{TMPDIR}$. The result is $\texttt{profiles_note.pdf}$. The checked-in PDF has three letter-size pages.

~~~sh
pdflatex -interaction=nonstopmode -halt-on-error -jobname=profiles_note -output-directory=TMPDIR standalone.tex
~~~
