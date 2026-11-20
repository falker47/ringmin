# Evidence

## Environment and references

~~~text
repository=falker47/ringmin
base=7d257221d9034ca5f895f062e45e782d8e77b6c2
base_ref=origin/codex/paper-ii-journal-candidate
branch=codex/p2-profile-generalization
platform=Windows x64
python=CPython 3.14.3
pytest=9.0.2
tex=pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
task_mode=STRICT
~~~

The shared setup matched the arXiv e-print SHA-256 digests and the reference project commit. The local worktree contains an ignored input junction used solely for reads. T3 directly compared all 16 bracket pairs with these sources.

| Input | Version or SHA-256 |
| --- | --- |
| Paper I e-print | 2607.28654v4, `e5d499657a47cea462fcaedae78f2dab1eb69f594315cd91aa9a61c71b5081ab` |
| Paper I bracket table | `58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1` |
| Paper II e-print | 2609.13630v3, `c65bfabb23d8764e46da3c03723573b5386a404a32e6a4082bb95e6b23e3d5b1` |
| Paper II main source | `792473ac5b2f0b39bcfb93a741490576c70aa42bc55c941bc914e4eb8354e98e4` |
| Ringmin-squared | `1d0a5dea10cd09783a9c0e2d54ede79b790cce2b`, `examples/small_n_interval_certificate_n{3,4,5,6}.json`, original interval-backend semantics |

The integer checker and numerical search use the Python standard library. The capability check imported python-flint 0.9.0, NumPy 2.4.3 and pytest 9.0.2, and located the requested TeX packages. The document builds use the local TeX Live installation.

## Claim ledger

| Claim | Classification | Evidence and scope |
| --- | --- | --- |
| Finite squeeze, rank reassignment and compact-law limit | Exact theorem, written proof, independent review pending | [Proof, §§1–3](../../research/PROFILE_GENERALIZATION.md). The proof quantifies all pairs, both directed arcs and every size. |
| Finite word bounds and power specialization | Exact theorem and proved corollary, written proof, independent review pending | [Proof, §§4–5](../../research/PROFILE_GENERALIZATION.md). Coefficient values remain implicit. |
| Measurability alone does not ensure convergence based on the uniform sampling law | Proved corollary by explicit counterexamples | [Counterexamples](../../paper_assets/paper_ii_profiles/ADVERSARIAL_REVIEW.md), including two subsequences with different limits. |
| Matching, finite copy inequalities, stability, two-type linear programs and squeeze comparisons | Independently reproduced finite result | [Integer verifier](../../paper_assets/paper_ii_profiles/checks/verify_finite.py), exhaustive within its stated finite ranges. It uses recorded bracket endpoints as inputs. |
| Five finite scores at $n=512$ | Numerical observation of locally searched orders | [Search](../../paper_assets/paper_ii_profiles/checks/observe.py) and independent directed integer verification of nearest decimals. |
| Standalone and insertion builds | Engineering fact | Six standalone passes over two builds, three integrated passes, PDFs and logs inspected locally. |

## Commands and outputs

All checks below ran locally. Temporary path names in the commands are represented by `TMP`. The two article source files, checkers and scripts are in `paper_assets/paper_ii_profiles`.

| Command or check | Exit and material output | Property |
| --- | --- | --- |
| `git status --short --branch` before starting, native host | 0, `## HEAD (no branch)` | Isolated clean starting tree |
| `git switch -c codex/p2-profile-generalization 7d257221d9034ca5f895f062e45e782d8e77b6c2` | 0, switched to new branch | Exact requested base |
| `python -I -S -B paper_assets/paper_ii_profiles/checks/observe.py --output TMP/orders.json` | 0, five scores at $n=512$ | Seeded local search with 16,000 attempted swaps per nonconstant profile |
| `python -I -S -B paper_assets/paper_ii_profiles/checks/verify_finite.py --sources .codex_inputs --observations TMP/orders.json` | 0, `matching=754 copies=70 placements=480 squeeze=16 stability=225 word_lp=12`, `source_brackets=16`, `independent_word_scores=5`, `PASS_PROFILE_FINITE` | Exact rational arithmetic or outward integer radical intervals. No imports from the generator. |
| `python -m pytest tests/test_profile_generalization.py` | 0, `14 passed in 1.06s` | Finite profile regression and adversarial inputs |
| `python -m pytest` with worktree `src` first, bytecode and disk cache disabled | 0, `82 passed, 4 subtests passed in 55.52s` | All collected tests on the branch |
| `pdflatex -interaction=nonstopmode -halt-on-error -jobname=profiles_note -output-directory=TMP standalone.tex` from the package directory | 0 on all six final passes, two independent temporary directories. Both final logs had zero warnings, overfull or underfull boxes and unresolved references. | Standalone typesetting and same-environment reproducibility |
| `pdfinfo paper_assets/paper_ii_profiles/profiles_note.pdf` and `pdftoppm -png -scale-to 950 ...` | 0, three letter-size pages, 182100 bytes, three rendered pages inspected | Final pagination and visual layout |
| `pdflatex -interaction=nonstopmode -halt-on-error main.tex` in the temporary v3 insertion test | 0 on each of three passes, `main.pdf (12 pages, 351784 bytes)`, final log with zero warnings or multiply defined or undefined references | Actual compatibility after §4, with the quadratic bibliography entry |

The separately enclosed word scores multiplied by $10^{10}$ and rounded are 3183098862, 1999947376, 1413183229, 889945783 and 651515025, respectively. The generated temporary orders on this Windows host had SHA-256 `78080ea27a8447774ff704df4d2e8d8d6295c4e66504973595db163444c234ad`. Their file digest depends on newline convention and can also depend on floating-point search ties. The independent checker verifies the rounded scores directly from the supplied orders.

## Artifact provenance

The tracked standalone PDF was generated from the two TeX sources in this same change. Its SHA-256 is `2cc515314001d9600e1ee6aed30938c15cb12f3c3b6d55c080e05b14cac64920` in each of the two final builds. The only production artifact generated is the requested PDF. Cross-environment bitwise reproducibility was not tested.

## Failed checks and limits

The [log](TASK_LOG.md) records the Windows Git sandbox issue, a rejected overlength shell invocation and the initial TeX overfull box, with the narrower successful checks. The mathematical counterexamples in the adversarial review rule out unqualified distributional transfer for arbitrary measurable functions and the unqualified infimum formula for nonmonotone representatives.

A finite checker cannot certify the general written proof. The original quadratic brackets retain their guarded interval assumptions. Their source verifier and the unrelated global-brackets verifier were outside this analytic task. Hosted CI and external peer review are pending.

## Diff and protected paths

The acceptance boundary comprises one proof file, the new profile package, one new test module and the four dossier files. The worktree scope and whitespace inspections cover every untracked textual addition, then the staged content. The PDF is checked separately by hash and rendered pages. The task requests a local commit and reserves publication for the author.

Before staging, Git listed exactly 13 allowed additions. The direct file audit checked all 12 UTF-8 texts for final LF, trailing spaces, conflict markers, host paths and local Markdown targets. It checked the PDF SHA-256 and reported “13 files audited (12 UTF-8 texts and 1 verified PDF)”. The tracked base, including source manuscripts, status, ledgers, roadmap, existing tests, production code, results, configuration and certificate verifiers, had an empty diff and passed the unstaged whitespace check.

The full staged diff contained only the 13 additions. Both staged and unstaged whitespace checks returned 0, the unstaged diff was empty, and a byte-for-byte readback of each index blob matched the inspected file. This handoff uses a local branch and commit, as requested.

## Second internal attempt

A fresh derivation at commit `cc87fb039465606d33c5f222c7dd18210722ef52` checked the line squeeze, genuine-label reassignment, stability under sorted square-root matching, normalization for $i^p$, and the finite-word bounds. For the lower LP bound one can choose the replication count $q$ divisible by the word length $r$. Cutting a minimizing $kq$-word into whole $r$-words then satisfies every balance constraint exactly at that finite size. This subsequence has the same limit.

For the binary law with mass $t$ at zero and the rest at $M$, the energy is $M(1-t)$. A word with $h$ positive letters costs $M\max(h-1,0)$. With $K=k-\lfloor kt\rfloor$ positive types in the upper quantile sample, convexity gives a lower LP value of at least $M\max(K/k-1/r,0)$. Mixing the two adjacent integer counts of positive letters attains it. Within each count, sample uniformly among the indexed types of each sign to obtain the required balance, including the constant endpoint cases.

The standard-library [replay](second_attempt.py) enumerates all word paths on square-root alphabets, checks the binary LP estimates and tests the donor-rank inequality over the recorded ranges. It imports no profile implementation. The command `python -I -S -B ops/TASK-20261119__p2_profile_generalization/second_attempt.py` returned 0 and printed:

~~~text
EXHAUSTIVE_ROOT_ARRAYS 205 STABILITY 11917 REVERSE_PAIR 205
BINARY_ATOMIC_LP 30240
TOP_DONOR_COMPARISONS 38744
~~~

The binary count includes repeated rational values of $t$ represented by different denominators. These are independently reproduced finite controls. External mathematical review of the general theorem remains pending.
