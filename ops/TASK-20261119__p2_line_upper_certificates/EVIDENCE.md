# Evidence

## Environment and authenticated inputs

Local Windows 11 build 26300, CPython 3.14.3, Node v22.16.0, pytest 9.0.2, python-flint 0.9.0, pdfTeX 1.40.28 (TeX Live 2025), pdfinfo 26.07.0. The branch base is 7d257221d9034ca5f895f062e45e782d8e77b6c2. The paper definitions and parameter gates come from the official source archives.

| Input | SHA-256 or Git commit |
|---|---|
| arXiv:2607.28654v4 e-print, 22445 bytes | `e5d499657a47cea462fcaedae78f2dab1eb69f594315cd91aa9a61c71b5081ab` |
| arXiv:2609.13630v3 e-print, 787569 bytes | `c65bfabb23d8764e46da3c03723573b5386a404a32e6a4082bb95e6b23e3d5b1` |
| falker47/ringmin-squared, shallow reference clone | `1d0a5dea10cd09783a9c0e2d54ede79b790cce2b` |

## Claim ledger

| Claim | Classification | Evidence and limitation |
|---|---|---|
| Twenty rational line placements are feasible and have the claimed strict normalized ceilings | Computer-certified finite results, independently reproduced | All pairs checked in exact integers by the isolated verifier. The claim concerns displayed placements. |
| C* < 0.140958576058 | Proved corollary | n=3200 linear placement and Paper II v3 limit theorem. |
| Rational four-block interval and enclosure of the implicit U4 | Computer-certified evaluations with explicit analytic bounds | Outward Arb primitives and independent integer quadrature give the tight rational result. The additional Lipschitz proof gives the coarser implicit range. |
| Quadratic finite radii admit n²(S+1)/π | Proved corollary | Both-arc closing construction in the note and exact quadratic certificates. The limiting interpretation is conditional on the profile theorem. |
| Estimated limiting line span near 0.44265 | Numerical observation | Regression on searched feasible spans. Model sensitivity and an external rigorous range are reported in the note. |

## Commands and checks

All outcomes below are local. Temporary input/output directory arguments are displayed by role as ORDERS, TEMP and INPUTS.

| Command/check | Exit and material output | Property and scope |
|---|---|---|
| `node paper_assets/line_upper/search.cjs ORDERS` | 0, both powers at ten sizes and two seeds | Exploration, including improvement history. Binary64 controls only candidate selection. |
| `node paper_assets/line_upper/search.cjs --interleaved-reference` | 0, 0.1414455073191551 and 0.14146746207639196 | Two 12000-swap reference runs on the plain interleaving. |
| `python -B paper_assets/line_upper/generate.py ORDERS paper_assets/line_upper/certificates` | 0, 20 files | Exact outward reconstruction of the selected words. |
| `python -I -S paper_assets/line_upper/verify_line_certificate.py <all 20 certificate paths>` | 0, 20 PASS lines and 13634050 pairs | Independent of search, generator, Arb and production modules. |
| `python -B paper_assets/line_upper/block_antiderivatives.py` | 0, RATIONAL_BLOCK_ARB 0.14191330499527 0.14191330499528; LITERAL_U4_LIPSCHITZ 0.141895293745 0.141931316245 | Rigorous primitive evaluation and analytic range perturbation. |
| `python -I -S paper_assets/line_upper/verify_block_subdivision.py` | 0, RATIONAL_BLOCK_INTEGER 0.1419133048777 0.1419133051216, uncertain_panels=7 | Independent integer midpoint enclosures on 196608 panels. Both integral programs also reproduced the diagonal comparison. |
| `python -B paper_assets/line_upper/report.py --inputs .codex_inputs` | 0, 9 reference inequalities, 20 hashes and 6 regressions | Exact finite consistency comparisons and explicitly numerical fits. |
| Search and generation rerun into a new temporary directory, byte comparison | 0, REPLAY_BYTE_IDENTICAL 20 | Reproduction on this runtime, including seed histories. |
| `python -m pytest` | 0, 82 passed, 4 subtests passed in 59.06s | Includes moved coordinates/labels, size, ceiling, truncation, nonadjacent overlap, repeated keys and independent small exhaustive oracles. |
| `python -I -S -B verify_global_brackets.py` | 0, PASS_GLOBAL_BRACKETS, 908 angle enclosures, 47 witnesses, 3374988556 covered classes | Existing exact certificate regression. The pinned certificate SHA-256 is 6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0. |
| `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=TEMP preview.tex`, three passes, then `pdfinfo` | 0/0/0, one page, zero undefined references, undefined citations or overfull boxes | Standalone section in its document class. |
| Exact macro cross-check | 0, MACROS_MATCH | Printed line ceiling equals the rational certificate B, block macro the rounded Arb upper endpoint. |

## Artifact provenance

The generation sources and outputs are carried in the same tree. The containing commit identifies that version without a self-referential hash inside the certificates. These are the SHA-256 hashes of the generating and audit programs.

```text
search.cjs 816d21c17d08bb19fd0007b8283500c75f0103845ef61639457c7e57f166bb2c
generate.py fa4ae680b63ebcb463c10059489658a72ef07aeb9ed4b4a2b263be98f2bb696a
verify_line_certificate.py 42015b4fc74083868767092d71bfc97891db26e99bac434d53ec5594aa9083ab
block_antiderivatives.py 6970986872ef4c3893e50518d0d9570dd8e74339d9c4661ed735a279432c961e
verify_block_subdivision.py 63ca9bc05aa676f560d9f7dd2179418fc3f0e6091417527d5429d1d636038289
report.py 37c7a05095642e14feaead68acfeb00cdaed875515809a8d50533b0a25bfc408
```

| Certificate | Bytes | SHA-256 |
|---|---:|---|
| p1_n00003.json | 384 | `4e363d9193c6ed9c7c4cd4f81855ad9d4a0ec86620dd4db8353f1f3fc6130a9a` |
| p1_n00004.json | 400 | `50d67f8809582ea0d75b4f9e57bfe344eb944e60b695ee86e0e3113f34f972a0` |
| p1_n00005.json | 416 | `0493653025f714ad72367ee855da1048bbc69982e4b2991839fdff18586a7855` |
| p1_n00006.json | 433 | `b286af8f5d7d15d8c843aa110acf897bee52ffd3c958fc7429c8c74f0de664fd` |
| p1_n00014.json | 580 | `0a065f9d8b0efb90d7b58f1c4542431fd68dcdca4b601e44bc280b534fd6a8d8` |
| p1_n00200.json | 4854 | `c2dd3427be73dd75206ddbb887e693415daded93d5acd04928df3e720dbb8f93` |
| p1_n00400.json | 9341 | `554ef2bf80da6cc78552e25023d5a0cfe406b0157f2af825b005673fe23b9892` |
| p1_n00800.json | 18635 | `dd9ddfdc3534d3ef414b2f9a6033339fdd5d8e94cb83a632803d0e346115a1e4` |
| p1_n01600.json | 38057 | `63e6ff755c5effaca1a1b201b4dc98fc7a914d259633d72588df97b0ba500f42` |
| p1_n03200.json | 78721 | `e48c671bad569202c13dbcdcd86487b35e75f141190c4082136a2602fd1dcdfb` |
| p2_n00003.json | 336 | `7b9747cd4fce37c135876faf6b4561429dc62180a0d3706eabf14f69254bb7d0` |
| p2_n00004.json | 341 | `26094127c0b45e7a0ec26ca2b84417485b5e4518c872ed94d4d92dce40af5b85` |
| p2_n00005.json | 348 | `f99a2d900698dd9cb0cbb2a8f6d2a6a065cd3280abb5520b8c160f3125b25e6d` |
| p2_n00006.json | 354 | `6b0267b3ae4e571ba60fbc32876c8ce27c6789c407da8410046c2e1bc817fb99` |
| p2_n00014.json | 414 | `caa37818f17c150c113e20723857defd6d56aabc0b2d94686cf0067d1196e581` |
| p2_n00200.json | 2899 | `02d643c27a3387a7ddb6233111f06a1288c6c022472e1085bb4b6962f1f1d167` |
| p2_n00400.json | 5528 | `a30cd6addb58368838c9e63cf9861c8bbe40ddf996b30587079ddaa59fb3e052` |
| p2_n00800.json | 11137 | `7cbed93735bfa8a2e9b8ee0fcf0ca4d7da1af6c3596027eeedc5907c9f1b4ba8` |
| p2_n01600.json | 23570 | `dc2e268d2e2df636f5d6b6df9f6c3f9a23ca6fcf7b58b63805edffdaa57ee8c0` |
| p2_n03200.json | 50407 | `10282bd9c8e7d36ef038436d37cea364f13218556228ca1266a93ade9cd15807` |

## Failed checks and residual uncertainty

The initial sandbox DNS probe failed. The permitted read-only HTTPS retry fetched both authenticated archives. The initial search cap, escaped table spacing and first preview line overflow are recorded with the subsequent corrections in the append-only log. Each published number has its own scope. The limit estimate and the floating search have no optimality guarantee. Hosted CI and external mathematical acceptance are pending.

## Final diff inspection

The original tracked files have no content changes. The complete added source, proof, dossier and test text were reviewed, and each JSON was parsed in full, independently verified and replayed byte for byte. An explicit enumeration found 35 allowed additions: 20 JSON, 6 Python, 5 Markdown, 3 TeX and one JavaScript file. Every added file passed the final-newline, trailing-whitespace and UTF-8 checks. The final handoff records the staged and commit checks.
