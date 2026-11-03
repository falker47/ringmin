# Paper II Component Review Coverage

Consolidated on 3 November 2026 for the editorial revision based on
`d925f85c8aee2b26bca460bf33618eb65fb996b8`. This document records the supplied
reviews and their limits. It is not a new mathematical audit, external peer
review, acceptance of the entire PR or promotion of the Review State Registry.
The proofs remain in main, S1 and S2; this note is not a proof premise.

## Reports and Revisions

| Report | Inspected revision | Covered argument and recorded outcome | Limits retained |
|---|---|---|---|
| [S1 / Proposition 7, 23 October](https://chatgpt.com/library?file_id=libfile_addf9f57c0088191b927ebdeffa3b310&account_id=personal) | `75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae` | `TECHNICAL_REVIEW_PASS_WITH_LIMITATIONS`. Analytic reading and independent reconstruction of the entire L1--L8 chain: geometric deletion, terminal assignment/shared energy, signed deletion, one crossing budget, minimax, global width optimum, ordered limits and existence. Separate exact arithmetic confirms the endpoint enclosure; all 14 PDF pages inspected. | This was an analytic review as well as arithmetic checking. The original package scripts were not personally rerun in that review, and its historical CI did not exercise all standalone S1/TeX/integrity gates. It did not accept the whole PR or certify the original Windows checkout. |
| [Theorem 5, 30 October](https://drive.google.com/file/d/1hMIqCMnbx5bQqwdbCtq6msvoEVDkpHQu/view) | `d925f85c8aee2b26bca460bf33618eb65fb996b8` | No invalidating gap identified in Theorem 5, type quantization in section 4.1 or computability in section 4.3. Separate `1/k` and `1/r` errors, remainder counts, rational frequencies and genuine all-pairs recovery examined. Original LP replay: six cases, 1,119 inequalities and 18 altered certificates rejected. Independent implementation: 13 cases and 70,248 rational comparisons. | Theorem 4 was a dependency, not re-audited there. No new S1/S2, whole-PR or CI verdict. Finite tests support the analytic argument; computability does not imply efficiency. |
| [Theorem 6 / S2, 30 October](https://drive.google.com/file/d/1LSp8erwtGSclHWL3-UKvKePIXybhHuf9/view) | `d925f85c8aee2b26bca460bf33618eb65fb996b8` | No invalidating mathematical gap identified. Full-cell all-pairs criterion, authentic permutations, rounding and seams, even/odd and countable transfer, implicit minimizers, independent rational gates and strict fourth-block saving examined. Separate bounded geometric/LP tests and six exact rational sign checks were recorded. | The five original upstream checkers were read but not executed in that session because of GitHub DNS access. Floating tests used stated tolerances. No global four-block optimality, equality `C*=U4`, author attestation or whole-PR acceptance follows. |
| [Theorem 4, Lemmas 2--3 and S2 connection, 3 November](https://drive.google.com/file/d/19QtHFDBCcA8YXUORlizWlTw5J4aYwd6d/view) | `d925f85c8aee2b26bca460bf33618eb65fb996b8` | Positive scoped judgment on angular branches/both arcs, unit closing gap, both squeeze inequalities, concatenation/scaling, bijective authentic-label reassignment, every large size and remainder, limit/infimum identity and `C* <= U4`. Recorded 1,612 exact rank cases and 87,110 comparisons with negative controls. The specific reservation about existence of the global limit was removed. | No fresh complete S2, LP or lower-endpoint audit, whole-suite rerun or CI acceptance. The finite-size estimate has an error term; the audit does not assert `R*(n)/n^2 <= U4` at every finite n. |

The original reports remain unaltered. Their closing requests are dated history:
the subsequent S2 review supplies the review requested after Theorem 5, and
the 3 November report discharges the specific Theorem 4 dependency reservation.
These limits do not, by themselves, identify a reason for another general audit.

## Binding the Evidence to This Revision

The reviewed candidate sources at `d925f85` have SHA-256 digests:

| File | SHA-256 at the reviewed candidate |
|---|---|
| main.tex | `14cc73a3e3c1bb1c4f4fc3476ed3035fc6699e02f06f64cef178cf3516e7982f` |
| upper_supplement.tex | `0030d533cef944ca1cd5b73c01e2f85f117952e52170c9345405b9e506a95bbd` |
| S1 supplement.tex | `ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4` |
| S1 supplement.pdf | `a18eb1ed78155f5c8d8476a35e2f62c95d445c03b65ebeadf522d79ccaaa5568` |

S1's source was compared directly at `75a2f448`, `d925f85` and this revision:
the bytes agree. All S1 files, including its PDF, certificate, checkers and
manifest, are preserved. Its analytic review therefore applies to the same
source text, rather than being inferred from a title or date.

The complete main/S2 delta is limited to the displayed revision date and the
explicit total definition of J. Both texts now state `J(i)=i` outside the
inversion blocks; the main also spells out `a_0=0`. The S2 report already
described the intended permutation as fixing the complement, and the Theorem 4
report retained this clarification as expository. No result, constant,
abstract, proof dependency or mathematical checker is changed. The task's
scope checker verifies the exact substitutions against `d925f85` and protects
every other scientific file.

The new source/PDF digests are in MANIFEST.json and BUILD_REPORT.json. Their
containing Git commit identifies this editorial candidate without circular
self-hashing. Inherited review applies to the unchanged arguments; fresh
engineering checks apply to the changed files and generated package.

## Fresh Verification Is a Separate Evidence Class

[READINESS.md](READINESS.md) and the new task dossier record fresh arithmetic,
build, visual, reference, preservation and package checks. In particular, the
current aggregate replay executes the five original upper checkers and S1's
original verifier/integrity controls. This supplies current execution evidence
without retroactively changing what the October reviews did.

Universal claims still rely on written proofs. Internal AI-assisted reviews,
hash equality, finite fixtures and green CI do not establish external
scientific acceptance or the author's personal understanding. None supplies
missing historical AI tool details, author affiliations or submission consent.
