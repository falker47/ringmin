# Evidence

## Environment and source identity

```text
task_mode=STRICT
base_origin_main=c26400b328c2f8fa338b588e61abb98266a265f9
generator_and_verifier_commit=8cd9f3d0a794260d5d40cd2acf7be9ce35754eee
platform=Windows 11 10.0.26300, x86-64
python=CPython 3.14.3 (MSC v.1944)
mpmath=1.3.0
pytest=9.0.2
generator_sha256=b5c76c424ef1b5bc8fed996434ea4119425dce89a2ade4e3607a0365978fb8f6
independent_verifier_sha256=f13e3a4ba3f69e900a5e3e2f861c93f1026b5c185e3d0ed7a6f9c9ffaa32a5a5
```

Parent setup fetched the versioned Paper I and Paper II e-print archives and checked SHA-256 `e5d499657a47cea462fcaedae78f2dab1eb69f594315cd91aa9a61c71b5081ab` and `c65bfabb23d8764e46da3c03723573b5386a404a32e6a4082bb95e6b23e3d5b1`. Input Ringmin-squared was pinned at `1d0a5dea10cd09783a9c0e2d54ede79b790cce2b`. T4 directly read the extracted Paper I v4 table, §§2–6, the protected original JSON, and the four older quadratic interval endpoints. The original generator, verified inputs and independent Paper I replay remain separate from the new certificate schema.

## Claim ledger

| Claim | Classification | Evidence | Independence and limit |
|---|---|---|---|
| The fixed multiplicity of insertion above each core and strictness buffer | Exact theorem and proved corollary | [Method note](../../paper_assets/general_radii/METHOD_NOTE.md) | Direct argument plus small exact oracles, independent human review pending |
| All 12 published linear endpoints reproduced | Independently reproduced finite result | [Certificates](../../paper_assets/general_radii/certificates/) | Fresh coverage, angular bounds, witness reconstruction and independent arithmetic replay, sharing the original method |
| Twelve quadratic open/closed brackets of width $10^{-11}$ | Computer-certified finite result | [Interval table](../../paper_assets/general_radii/README.md#exact-endpoints) | Exhaustive integer lower replay and rational upper existence, for $3\le n\le14$ |
| Four earlier quadratic brackets contain the new intervals | Independently reproduced finite comparison | [Comparison](../../paper_assets/general_radii/RESULTS.md) | Exact rational comparison against the pinned older table |
| Byte-identical generation and isolation | Engineering fact | Checks below | This environment and the 24 listed instances |

## Commands and checks

All rows describe local runs. For pytest, `PYTHONPATH` was set to the worktree's own `src` directory and `PYTHONDONTWRITEBYTECODE=1`; the final suite used `PYTEST_ADDOPTS=-p no:cacheprovider`. The editable install on the machine otherwise resolves to another checkout.

| Command or check | Exit and material output | Property checked |
|---|---|---|
| `python -B paper_assets/general_radii/certify_radii.py --linear N --output FILE`, each $N=3,\ldots,14$ | 0 for all 12, `CANDIDATE` for each file | Generation from v4 rational endpoints and the protected first upper word |
| `python -B paper_assets/general_radii/certify_radii.py --quadratic N --output FILE`, each $N=3,\ldots,14$ | 0 for all 12, including `CANDIDATE n=14 (17372227944147/100000000000, 4343056986037/25000000000]` | Search and integer/rational candidate construction, no global proof from this run alone |
| `python -I -S paper_assets/general_radii/verify_radii_certificate.py --all` | 0, 24 PASS lines, including `PASS quadratic_14.json n=14 classes=3113510400` | Independent Machin/cosine, forward DP, gap assignments, strictness and strict Cartesian distances. Imports only standard library |
| `python -I -S verify_global_brackets.py` | 0, `PASS_GLOBAL_BRACKETS`, 908 angular enclosures, 47 witnesses, 3,374,988,556 classes, 13 preserved original files | Exact original linear-family regression |
| `python -m pytest -p no:cacheprovider tests/test_general_radii.py` | 0, `27 passed in 0.56s` | Exhaustive DP and gap-set oracles, all deletion depths through $n=7$, mixed radii and scaling, grid-aligned optimum, negative controls, published and squared comparisons |
| `python -m pytest` | 0, `86 passed in 56.18s` | Whole repository suite on this worktree and runtime |
| Fresh per-file CLI regeneration in a temporary directory followed by byte equality | 0, `BYTE_IDENTICAL 24 fa43f4bbec2abe88fee977c3c1824d17ca88e0176f0ce5de7347d3105c0d8245` | Digest of sorted UTF-8 filename, NUL byte and raw file content, concatenated for all 24 JSON files; repeated at the generation commit |
| Exact Fraction comparison of every LaTeX row and one-pass minimal article compilation with `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error test.tex` | 0, `TABLE_MATCH 12 LATEX_PASS` | Table matches the JSON and compiles with booktabs |

Regeneration requires the configured inputs for the linear family. The quadratic search is self-contained. Linear code and results share published input endpoints. Independent replay requires none of the generation inputs or third-party packages. No hosted CI or external review result is asserted.

## Failed checks and negative evidence

- The first focused run exposed a test precondition comparing Python objects with `True == 1`. JSON serialization distinguishes the mutations. One isolated child-process test also inherited an invalid Windows stdin handle; giving that command `DEVNULL` made the launch reproducible. Initial runs recorded 2 failures among 26 focused tests and 1 among 85 full-suite tests. The revised focused suite passed, and the final regression suite also covers exact grid optima.
- A fixed deletion depth of two generated $n=11$ in 21.487 s and left the $n=12$ exploratory search in progress. That run was interrupted before any $n=12$ output. A second search used a deeper core and pruned infeasible partial words only during exploratory bisection. Full insertion replay at $L$ remained exhaustive. The two searches agreed on the $n=11$ endpoints, and the independent verifier accepted every final row through $n=14$.
- No recorded explicit lower exclusion needed a graph witness beyond a rank-threshold induced cycle. A synthetic matrix is checked separately to exercise that fallback.

## Final diff and provenance

The two source files were inspected in full in the staged patch and passed `git diff --cached --check` before the source commit. Further additions are the 24 JSON files, table, two results/method documents plus README, dedicated tests, and the four task-dossier files. All JSON data were parsed in full by the independent verifier and reproduced byte for byte. Text additions were read before staging. Final checks include the explicit untracked whitespace audit, scoped full staged patch inspection, `git diff --check`, and the staged whitespace check. Task-specific changes are confined to the three allowed paths. The protected published papers, shared state and ledgers, originals, existing verification code, results, package configuration, and CI require no edits.

## Residual uncertainty

Independent mathematical review and repository integration are pending. Finite brackets do not identify exact optimal radii or contact graphs. Runtime and space beyond the tested instances depend on the core and remaining insertions.

## Second internal attempt

The second attempt checked the generic coverage and strictness proof at `6fb2af8d506d7efd5f27b4f9f473a9510fcb8a4f`. Fix an oriented core and its anchor. Choose $k-1$ places among the other $n-1$ full-word slots for the surviving labels in their prescribed order, then permute the $d$ deleted labels in the remaining slots. This gives $\binom{n-1}{k-1}d!=(n-1)!/(k-1)!$ extensions. Reversal of the core accounts for the other oriented representatives. For a positive directed simple cycle, including one with several windings, the strict integer excess is at least one grid unit. Over $[L,L+\varepsilon]$ the derivative bound consumes at most half that margin.

The [finite replay](second_attempt.py) enumerates ordered integer positions at integer periods. This is a complete feasibility oracle for these experimental integer inequalities since flooring all coordinates preserves every difference inequality with integer right side. A five-vertex example uses weight one on the polygon edges and three on the diagonals. Every induced cyclic sum is at most seven. The star cycle requires 15 across two turns of period seven. The graph test excludes that case, while period eight permits a placement. On authentic size-eight and size-nine matrices the replay projects complete words onto their cores using the smallest remaining anchor and compares all fibres with the production-independent verifier's traversal.

`python -I -S -B ops/TASK-20261119__p1_general_radii_certification/second_attempt.py` returned 0 and printed:

~~~text
DISCRETE_CIRCLE_ORACLE 5584 {'feasible': 2847, 'prefix_exclusions': 2255, 'graph_exclusions': 482}
PENTAGRAM 16 induced subsets, period 7 excluded, period 8 feasible
AUTHENTIC_CORE_FIBRES 16 181440 148008
~~~

In an additional finite check the generator and standalone verifier produced and accepted 11-decimal brackets for the triples $(1,2,3),(1,4,9),(2,3,7),(3,4,5),(1,11,97),(7,30,45),(1,100,10000),(71,113,157)$. At three disks the tangency configuration is given by the positive inner Soddy radius. Put $K=\sum 1/r_i$, $H=4\sum_{i<j}1/(r_ir_j)$. Its reciprocal is $K+\sqrt H$. Exact rational comparisons proved $1/L-K>0$ and $(1/L-K)^2>H$ in all eight cases. At $U$ each satisfied $1/U-K\le0$ or $(1/U-K)^2\le H$. This comparison uses Descartes' circle theorem independently of the angular bounds. The original 24-file verifier replay also passed again. The external research review remains pending.
