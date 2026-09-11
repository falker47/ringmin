# Conservative correction of the finite paper: source and claim audit

Mode: `STRICT`. Internal authoring audit by the `endpoint_finite_referee`
subagent; independent cross-review by the scientific-claim subagent remains a
separate check. This is not external mathematical acceptance or submission
approval. Base reviewed commit: `227d09d480c2d88d09d3450c9015fc9737440c17`.

## Scope and ownership

The new objective was read in full before work. The applicable `AGENTS.md`,
compact knowledge index, current status, current roadmap entry, relevant
ledger headings/sections and their controlling sources were inspected. The
startup working tree was clean. Later shared-tree changes belong to the
coordinated publication-architecture task.

This subagent created only
`paper_assets/v1_correction/ringmin_finite_v2.tex` and this audit. The root
owns copied historical assets, compilation, PDF/bundle checks, publication
metadata, status/ledger/handoff updates and Git integration. Ownership and
expected claim corrections were reported before editing. The root subsequently
took over layout-only edits to the frozen correction source.

The historical `paper_assets/ringmin_paper.tex`, its PDF, appendix, figures,
results, production code and verifier are protected. The former replacement
under `paper_assets/v2/` was not edited by this subagent. No result generation,
new mathematical research, Git mutation or external submission was performed.

The corrective paper retains the original title and finite scientific
identity. It cites **Minimum central circles: an effective characterization
of the global asymptotic constant** as the separate sequel. Its visible
`AWAITING_STANDALONE_ARXIV_ID` status and bibliography token
`PENDING_STANDALONE_ARXIV_ID` are deliberate. It is a review copy awaiting a
real permanent identifier, not an upload-ready correction.

## Source coverage and epistemic classification

The historical manuscript was read completely, including all three proof
bodies, main and heuristic tables, appendix comparison, bibliography, and
external appendix. The complete correction was read and compared against it.
Line references to the historical source below identify the immutable
`paper_assets/ringmin_paper.tex`; correction references use labels/sections so
the root's later layout fixes do not invalidate the mapping.

| Original material | Controlling source/evidence inspected | Corrective disposition |
|---|---|---|
| Angular reformulation, lines 95–104 | Original exact cosine-law proof; `verify.py:25` and its independently implemented all-pairs STN | Historical-paper core. Lemma and proof retained. |
| Chain closure and optimal-order theorem, lines 107–158 | Original supermodularity/Supnick proof; `knowledge/FIXED_ORDER_THEORY.md:11`; relevant original references | Exact theorem retained, with the missing `n>=3` positive-radius domain explicit. All three original proof bodies unchanged. |
| Fixed-order full radius/STN, line 170 | Original two directed angular constraints and shortest-path formulation; `verify.py:91` | Historical-paper core retained, including distinction between chain and full radius. |
| Canonical finite search and induced lower bound, lines 172–176 | `verify.py:80`, `:285`, `:289`, `:324`; `knowledge/CERTIFICATION.md:8` | Original algorithm retained. Omit undefined chain terms with fewer than three survivors; deletion keeps original radii. |
| Main certified range, lines 181–206 | `knowledge/CERTIFICATION.md:8`; saved optimum/frontier evidence; root's fresh full-verifier run | Computer-certified finite results for 3–14 with inherited global radius guard `1e-10`; high-precision reconstructions and local bracket do not expand that guarantee. All table numbers/orders/floating labels retained. |
| Essential/floating semantics, lines 112, 118, 178, 183 | `verify.py:228`–`:258`, constants `:12`–`:22`; original pocket formula | Exact existential definition retained. Pocket equality means two boundary tangencies, not strict floating. Actual numerical joint incident-constraint check described. |
| Finite regimes, lines 67–75, 208–228 | `knowledge/CERTIFICATION.md:14`; `results/supnick_validity.json`; producer `scripts/supnick_validity.py`; main certificate witnesses | Historical-paper core retained as reported finite solutions. Pocket/diagnostic decimals are numerical evidence; no universal optimal contact graph is inferred. |
| All-integer fixed-order seam continuation, lines 211, 230–232 | `research/SUPNICK_FULL_FEASIBILITY.md:347`–`:400`; `research/SUPNICK_SEAM_SEQUENCES.md:10`–`:52`, section 6 and linked finite bridges | Cross-reference only to the later exact fixed-order result. First three thresholds 8,13,17 retained; neither arbitrary-order global optimum nor global floating follows. No seam-proof duplication. |
| Complementary Supnick tour, lines 164–166, 285–295 | `knowledge/FIXED_ORDER_THEORY.md:25`; original chain-extremum argument; numerical generating comparison in `scripts/m2_summary.py` | Exact maximum **chain** theorem preserved. Reported realizability/values remain finite fixed-order numerical evidence, with no certificate for maximizing `R_full` over all cyclic orders. |
| Heuristic 15–18 table, lines 234–248 | Original table and saved heuristic scope in ledgers | Historical numerical upper bounds retained. No expansion of global certification beyond 14. |
| Small-angle/square-root chain calculation, lines 252–258 | Original chain argument, valid exact ordering theorem; `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md:431` | Valid chain-relaxation calculation retained. Its missing all-pairs upper-bound transfer is stated explicitly. |
| False global `1/8` and deficit conjectures | `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md:431`–`:441`: `C_term>3/22>1/8`; current global theorem owner `knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md:10` | Both explicitly disproved. This concerns global asymptotics, not the finite certificates. |
| New `C_*` limit/effective characterization | `research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md:8`–`:96` and current theorem owner/source links | Standalone-core material is cross-reference only: consequence `R*=C_* n^2+o(n^2)`, `C_*>1/8` and effective characterization. No LP, recovery, quantitative endpoint, or new proof imported into the correction. |
| Original appendix/figures | Entire `paper_assets/appendix_tables.tex`; original local image references | Original data and images retained by exact copying under root ownership. Inputs are unconditional and local; no silent omission fallback. Captions/prelude correct inherited labels. |

The older induced-subset note's subsequently superseded list of open questions
about existence of the limit was not copied. The current theorem owner and
its linked proof control that question.

## Complete obsolete-conjecture and `1/8` occurrence inventory

Every historical occurrence of `n^2/8`, `1/8`, `frac{n^2}{8}` or the
square-root integral coefficient was inspected. The following covers all
matching source lines, including the three formulas on original line 263.

| Historical line(s) | Original use | Correction |
|---|---|---|
| 32 | Abstract presents global `n^2/8(1+o(1))` as live conjecture | Abstract calls it disproved and cites sequel; continuation of global floating remains conjectural. |
| 81 | Quantitative summary advertises `R*~n^2/8` | Replaced by pointer to the correction section. |
| 256 | `pi*n^2/8` square-root chain integral | Retained: valid chain-relaxation coefficient, not a feasible global construction. |
| 258 | Self-consistency at `R~n^2/8`, negligible-floater assumption and proposed transfer | Unsupported transfer removed; explicit explanation that chain calculation does not establish global `R*~n^2/8`. |
| 260 | Figure caption labels `n^2/8` the asymptote | Historical image retained; caption explicitly calls it the disproved v1 conjectural reference, distinguishes heuristic points and complementary-chain curve. |
| 262–264 | Leading conjecture, finite deficit `n^2/8-R`, and stronger `O(sqrt(n))` conjecture | Replaced by a remark declaring both asymptotic claims false. All nine finite deficit numbers retained as observations; heuristic deficit direction remains conditional on feasible upper bounds. |
| 266 | Supposed feasible Supnick upper bound could establish leading order | Removed; cites separate all-pairs sequel result. |

The correction's further scalar `C_*>1/8` occurrences are the refuting
consequence, not a reinstatement of the coefficient. The exact lower bound
`3/22>1/8` already suffices to refute both old conjectures: an order-`n^2`
separation cannot be `O(sqrt(n))`. No assumption about the number of floating
circles is used.

Other obsolete or mixed-status conjecture references were checked separately:

| Historical line(s) | Disposition |
|---|---|
| 84 | Epistemic ledger now distinguishes disproved coefficient/deficit, exact fixed-order continuation, and unresolved global continuation. |
| 211 | The all-`n>=8` canonical seam failure is no longer an open conjecture; cite exact fixed-order supplement. |
| 227 | Finite appearances 8,14,18 do not determine every optimum or a global growth law. The unestablished use of Dan's proposed `n/4` bound was removed. |
| 230–232 | Split the cascade into proved eventual canonical fixed-order seam failure, unresolved existential global floating, the stronger unresolved every-optimum assertion, and unresolved indefinite paid/free repetition. |
| 270 | Replace obsolete all-`n` seam/open asymptotic prompts with global finite optima beyond 14 and explicitly quantified global floating questions; arbitrary-radii and 3D questions retained. |
| 30,43,48,57,273 | Historical attribution of Dan's pyramid conjecture retained; it is not one of the disproved asymptotic conjectures. The theorem's realizability qualification remains explicit. |
| 12 | Unused LaTeX conjecture-environment declaration is harmless infrastructure, not a scientific claim. |

## Every floating/contact quantifier and numerical overclaim

1. Original lines 48 and 62 implied global floating from `n>=8` and seam
   failure. The correction says reported certified 8–14 optima admit such
   placements, separately from the all-`n` fixed-order obstruction.
2. Regime-table headers, the n14 caption, main-table caption and the structural
   summary now describe reported solutions/existence. A displayed witness need
   not itself realize all available strict slack; no uniqueness follows.
3. The original existential definition at line 112 is preserved exactly.
   At line 118, `rho<=pocket` only guarantees fitting against the two pocket
   boundaries; equality is not strict slack. Other pair constraints must also
   be checked.
4. Original line 178's operational equivalence was too compressed for the
   finite perturbation actually used. `verify.py:239` tests individual essential
   pairs with `+1e-9`; `:256` separately tests **all** incident constraints for
   one circle with `+1e-9`. The correction states both. It does not claim that
   absence of individually reported essential pairs alone proves the same
   simultaneous numerical margin. Nor does it allege that the abstract
   infinitesimal convex-feasibility equivalence is false.
5. Original line 206's "the optimal cycle" was narrowed to a reported optimal
   cycle. Original line 227's single-backbone assertion and first-floater
   thresholds no longer quantify over every global optimum.
6. Original free/paid Proposition, lines 215–217: the initial correction still
   preserved an unqualified exact equality for 10–12. Independent scientific
   cross-review identified the missing exact full-insertion proof. The final
   scientific text uses approximate pocket/cost decimals, separate all-pairs
   checks, and agreement of reported full radii with the reduced-chain value
   within the stated certificate tolerance. No exact insertion theorem was
   invented. The main numerical data and finite-regime interpretation remain.
7. Original second-breakdown line 223 now describes the reported optimum;
   later circle-2/circle-3 appearances are correspondingly finite or heuristic.
8. Original universal floating conjecture remains unresolved, explicitly
   separated from the weaker existential question and exact canonical seams.
9. The 50-digit-verifier references now distinguish arithmetic precision,
   incumbent reconstruction, local bracketing and the original `1e-10` global
   guard. The unchanged appendix's 30 digits receive the same qualification.
10. Original `Worst arrangement` and its summary/figure/appendix wording now
    distinguish maximum chain radius from maximizing full fixed-order radii.
    This is a scope correction; no counterexample to the exact chain theorem
    or wrong finite optimum was found.

## Numerical certificate scope and unchanged evidence

The correction retains the original finite certificates and their error
guard assumptions. The historical calibration is recorded in
`results/float64_calibration.csv:2`–`:8`: 100,000 sampled orders at each
8–14, maximum observed absolute deviation
`1.75137506176142662e-14` and overestimate `1.4259157329620128e-14`.
The paper's rounded `1.8e-14`/`1.5e-14` values remain conservative.
The comparison to `1e-10` is corrected from "four orders" to "more than
three orders".

`verify.py:324`–`:417` checks saved content hashes, exact expected canonical
counts, progress-prefix coverage summaries, retained frontier bounds and
Stage-B flags at high precision, and top-excluded guard metadata. This is not
a new directed-interval reevaluation of every excluded order. No incorrect
optimum, numerical guard counterexample, over-pruning instance or damaged
certificate was discovered in this task. The limitation is inherited
certification scope, not evidence that all finite claims are invalid.

The root reported a fresh full `python verify.py --start 3 --stop 14` success
for all incumbent/local/frontier checks, after restoring 12 byte-preserved
historical logs totaling 9,649,682 bytes. That execution is root-run evidence,
not a verifier run by this subagent. Its exact output and hashes belong in
the root's [EVIDENCE.md](EVIDENCE.md). It reproduces saved evidence without
rerunning exhaustive generation and does not imply hosted CI or external
acceptance.

## Local verification performed by this subagent

Environment: Windows PowerShell, Python 3.14.3; the symbolic checker reports
SymPy 1.14.0. All runs local. Only the `safe.directory` argument below is
display-normalized to `<repository-root>`; other displayed command arguments
are the actual ones used.

1. `git -c safe.directory=<repository-root> rev-parse HEAD`: exit 0,
   `227d09d480c2d88d09d3450c9015fc9737440c17`.
2. `git -c safe.directory=<repository-root> diff --no-index -- paper_assets/ringmin_paper.tex paper_assets/v1_correction/ringmin_finite_v2.tex`:
   exit 1 as expected for different files. Complete source also directly read;
   differences confined to explained corrective text and packaging/font setup.
3. `python -I -S ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py`:
   exit 0. `exact_sequence_gates=PASS arithmetic=stdlib/Fraction optimized_safe=YES`;
   4 parity constructions, 104 cyclic edges, both central corrections, 10
   polynomial coefficient/endpoint gates and 6 targeted rejections pass;
   `production_imports=0 diagnostic_imports=0 root_evaluations=0 k_scan=NONE`.
4. `python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py`:
   exit 0. Nine general identities, N=3/N=4 closure and all paths, rational
   N=3 root `6/23`, 32 rank/parity constructions and 276 edges, 1,482 unordered
   pairs/2,964 directed paths, and 82 rejection gates pass. Its finite
   transcription checks do not replace the all-`k` analytic proof.
5. A read-only standard-library preservation check was executed as a PowerShell
   here-string piped to `python -I -S -`. It extracted each manuscript title,
   all `proof` environments, and the complete `tabular` bodies following labels
   `tab:main`, `tab:heur`, `tab:worst`, requiring equality; counted 12,4,2 rows;
   required the three local inputs, absence of `IfFileExists`, exactly one of
   each pending-status token, resolved reference/citation labels, and no trailing
   whitespace. Initial run: exit 1 solely for an inherited trailing space in
   the open-problems paragraph, after all substantive equality checks passed.
   The correction-only whitespace was removed. Repeated identical check:
   exit 0, output below. No production imports or result generation.
6. `git -c safe.directory=<repository-root> diff --exit-code -- paper_assets/ringmin_paper.tex paper_assets/ringmin_paper.pdf paper_assets/appendix_tables.tex paper_assets/figures results verify.py src/ringmin`:
   exit 0 with no output. Protected original scientific/code/artifact paths
   remain unchanged.

```text
tab:main complete tabular unchanged; rows=12
tab:heur complete tabular unchanged; rows=4
tab:worst complete tabular unchanged; rows=2
PASS title, all3 proof bodies, all3 complete numeric tabulars, required local assets, placeholders, internal references/citations, whitespace
Python 3.14.3; stdlib-only; no production imports; no result generation
```

Source hashes at the scientific freeze, **before root layout adjustments**:

| Path | Bytes | SHA256 |
|---|---:|---|
| `paper_assets/ringmin_paper.tex` | 29184 | `5042d01b0f0f54ed3badeaa494cd24411aa58a2aa2c865b3f02abb27fcbcc60a` |
| `paper_assets/appendix_tables.tex` | 2178 | `b79e4deaffbdb6a9b8864210337b492b8ae96bdcc7f44d432c577cf2c4730056` |
| `paper_assets/v1_correction/ringmin_finite_v2.tex` | 34408 | `c714fa3d4f19bff2b9fa1bd33a1327c3fa10a164b16020f89815602df830ec6f` |

The root owns final source hashes/build evidence; these hashes identify the
scientific review snapshot and must not be mistaken for post-layout hashes.

## Handoff and limitations

The correction retains the valid finite scientific core and moves new
asymptotic theory to the standalone paper. Relevant overlap classifications
and primary bibliography checks are recorded separately in
[POLICY_AND_OVERLAP.md](POLICY_AND_OVERLAP.md). The survey title/DOI and Hifi
article metadata were corrected in the new source from that agent's primary
checks. Historical acknowledgments of the Henigman comment were retained;
its hidden comment was not independently retrieved during this task.

The root must finish layout/PDF checks, source-only bundle checks and final
asset/hash reconciliation. The pending standalone identifier remains an
intentional submission gate. No permanent identifier was invented, no arXiv
upload was attempted, and this internal audit neither accepts the mathematics
externally nor changes the certified range.

## Final post-layout preservation check

The root completed layout edits (small regime table; displayed pocket values;
small ragged-right bibliography; narrower table padding; disabled unused EPS
conversion). The final scientific text was inspected around each affected
region. The root reports a three-pass, zero-warning, 12-page clean PDF build;
that build is root evidence, not a PDF build performed by this subagent.

This subagent repeated the preservation check against the post-layout source,
then additionally compared every copied input byte-for-byte with its historical
original. The exact final PowerShell command was:

```powershell
@'
import hashlib, pathlib, re, sys
root=pathlib.Path('.')
old=(root/'paper_assets/ringmin_paper.tex').read_text(encoding='utf-8')
new=(root/'paper_assets/v1_correction/ringmin_finite_v2.tex').read_text(encoding='utf-8')
assert re.search(r'\\title\{(.*?)\n\\author',old,re.S).group(1)==re.search(r'\\title\{(.*?)\n\\author',new,re.S).group(1)
proof=lambda s:re.findall(r'\\begin\{proof\}(.*?)\\end\{proof\}',s,re.S)
assert len(proof(old))==3 and proof(old)==proof(new)
for label, rows in [('tab:main',12),('tab:heur',4),('tab:worst',2)]:
    get=lambda s: re.search(r'\\begin\{tabular\}(.*?)\\end\{tabular\}',s.split('\\label{'+label+'}',1)[1],re.S).group(1)
    assert get(old)==get(new), label
    body=get(new).split('\\midrule')[-1].split('\\bottomrule')[0]
    assert len([l for l in body.splitlines() if '&' in l])==rows, label
    print(label+' complete tabular unchanged; rows='+str(rows))
assert '\\IfFileExists' not in new
assert re.findall(r'\\input\{([^}]+)\}',new)==['appendix_tables.tex']
assert re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',new)==['figures/n14.png','figures/radii_vs_n.png']
for marker in ['AWAITING_STANDALONE_ARXIV_ID','PENDING_STANDALONE_ARXIV_ID']:
    assert new.count(marker)==1
refs=set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',new))
labels=set(re.findall(r'\\label\{([^}]+)\}',new))
assert refs<=labels
cites=set(re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',new))
bibs=set(re.findall(r'\\bibitem\{([^}]+)\}',new))
assert cites<=bibs
for name in ['paper_assets/ringmin_paper.tex','paper_assets/v1_correction/ringmin_finite_v2.tex','paper_assets/appendix_tables.tex']:
    data=(root/name).read_bytes()
    print(name+' bytes='+str(len(data))+' sha256='+hashlib.sha256(data).hexdigest())
assert not any(l.rstrip()!=l for l in new.splitlines() if l.strip()), 'trailing whitespace'
print('PASS title, all3 proof bodies, all3 complete numeric tabulars, required local assets, placeholders, internal references/citations, whitespace')
print('Python '+sys.version.split()[0]+'; stdlib-only; no production imports; no result generation')
for asset in ['appendix_tables.tex','figures/n14.png','figures/radii_vs_n.png']:
    a=(root/'paper_assets'/asset).read_bytes()
    b=(root/'paper_assets/v1_correction'/asset).read_bytes()
    assert a==b, asset
    print(asset+' historical copy byte-identical sha256='+hashlib.sha256(a).hexdigest())
'@ | python -I -S -
```

Exit 0, exact output:

```text
tab:main complete tabular unchanged; rows=12
tab:heur complete tabular unchanged; rows=4
tab:worst complete tabular unchanged; rows=2
paper_assets/ringmin_paper.tex bytes=29184 sha256=5042d01b0f0f54ed3badeaa494cd24411aa58a2aa2c865b3f02abb27fcbcc60a
paper_assets/v1_correction/ringmin_finite_v2.tex bytes=34550 sha256=4724d3d6f222e22293a61b5bbed70685550c8a341f4a070f535ebd6fbfc7d2af
paper_assets/appendix_tables.tex bytes=2178 sha256=b79e4deaffbdb6a9b8864210337b492b8ae96bdcc7f44d432c577cf2c4730056
PASS title, all3 proof bodies, all3 complete numeric tabulars, required local assets, placeholders, internal references/citations, whitespace
Python 3.14.3; stdlib-only; no production imports; no result generation
appendix_tables.tex historical copy byte-identical sha256=b79e4deaffbdb6a9b8864210337b492b8ae96bdcc7f44d432c577cf2c4730056
figures/n14.png historical copy byte-identical sha256=6c5719cb6089437e4f03baeb1b42ff34155dfcbfc41a5de0b3402da87b1cdcea
figures/radii_vs_n.png historical copy byte-identical sha256=f4d3b900bbec1c3e0555d9e9f38d97df68d5ea4fda3ba6f314324b6eb085a9eb
```

The final source hash agrees with the root's clean-build input. These checks
establish source/data preservation and explicit local inputs, not rendered
page quality, exact-arXiv-service compilation, or external review acceptance.
