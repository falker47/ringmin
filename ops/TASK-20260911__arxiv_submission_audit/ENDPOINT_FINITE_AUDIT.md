# Endpoint, fixed-order and finite-evidence submission audit

    reviewed_on=2026-09-11
    mode=STRICT
    reviewed_head=3beb8d70c5b3748d370a92855847bdf574e5a14f
    review_kind=independent subagent pass internal to this submission audit
    external_acceptance=not performed or implied
    outcome=one IMPORTANT evidence-scope clarification, corrected; no unresolved finding in this scope

## Scope and conclusion

The complete initial 565-line manuscript was read once for coherence.
This pass independently compared the exact upper input definitions, lower
endpoint and limit quantifiers, fixed-order table and finite-certificate
paragraph against their actual linked supplement sources. The global
variational proof and general recovery theorem receive their own separate
scientific review; this file does not substitute for it. Bibliographic
metadata, clean TeX compilation and PDF inspection are separate parent gates.

The manuscript preserves the distinction between exact theorem, explicit
upper construction, numerical finite certificate and heuristic candidate.
No wrong endpoint digit, reversed inequality, confused optimizer,
chain/full/global substitution, new finite optimum, floating-cascade
theorem, efficient algorithm or external acceptance assertion was found.
The supplementary outline is verifiable by the linked sources; no additional
endpoint or fixed-order exposition expansion is required.

Only this audit file's content was changed by this subagent. No proof, checker,
production code, finite artifact, historical v1 file, review registry or Git
state was changed by this subagent. No new scientific conclusion is introduced.

## Finding and resolution

**EF-1 — IMPORTANT, corrected: disclose the inherited numerical-guard scope.**

At reviewed HEAD, manuscript lines 486-493 reported the original finite
certificates, their local tolerances and the full saved-frontier verifier run.
Those facts agree with the recorded evidence. The phrase “audits the complete
saved pruning frontiers and their provenance” benefits from an explicit
boundary: this is a check of saved frontier and coverage evidence, with
the original float64 error guards, rather than an independent interval
evaluation of every excluded order.

Source evidence:

- Historical `paper_assets/ringmin_paper.tex:176` describes bisection,
  an `O(n epsilon64)` error budget and random-order calibration. It does
  not provide directed interval evaluation of every excluded order.
- `scripts/extract_frontiers.py:199` records the float64 bound guard as
  `1e-11`; lines 188-212 save threshold, heap and completion summaries.
- `verify.py:341` onward compares expected totals, completion fields,
  prefix-complete log counts and the saved top-excluded guard.
  Lines 384-407 recompute the lower bounds of the retained list at high
  precision and compare their observed overestimates with the guard.
- The `n=14` retained list has 11 orders; its coverage total is
  `13!/2=3113510400`. Those two counts describe different objects.

**This is a clarification of a historical computational limitation, not a
counterexample or invalidation of a finite result.** No wrong optimum,
corrupt evidence, observed over-pruning or changed certificate was found.
An unproved fully directed error bound is not itself evidence that the
recorded numerical guard fails.

The parent inserted and this reviewer re-read the following at revised
manuscript lines 500-502:

> These numerical certificates retain the original floating-point error guards;
> verification checks the saved frontier and coverage summaries, not every
> excluded order with directed interval arithmetic.

This is the minimal requested qualification. It preserves the historical
scope and all numerical values. The revised source checked here has SHA-256
`d17809a5e2ed3a7a26d30b0cc19d7cd3a457d901bdd971bd4270b40bf495b5bf`;
later parent-only publication edits may change that hash. No BLOCKER or
OPTIONAL finding is raised by this pass.

## Claim/source coverage

Line references in this table are to the initial manuscript at reviewed HEAD;
proof notes were not modified during this pass.

| Manuscript claim | Actual source read and comparison |
|---|---|
| Abstract and introduction, lines 27-76; conclusions, 519-527 | Read in full. Arbitrary-order asymptotic characterization remains separate from explicit endpoints and finite evidence. Lower/upper endpoint statements are weak bounds, not equality with the global constant. Internal checks and pending external acceptance are distinguished. |
| Exact normalized `E(x)`, `x_*`, `K(alpha)`, `alpha_hat`, 348-358 | `research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md:77` onward defines the same literal two-max integral. `research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md:20` onward restates the exact complete input chain. The normalized optimizer is not the historical shift optimizer; the scale factor `lambda=(1+alpha_hat)x_*` is correct. Prior full parameter derivation is identified in `UPPER_INTERNAL_AUDIT.md` Sections 2-3. |
| Second and third widths and exact brackets, 359-373 | Boundary-minimum note Sections 1-2 defines the separate second reflection, full integral and unique mixed minimum on the closed extension. `research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md:14` onward defines its fixed-start third reflection and full derivative; Section 5 supplies the rational bracket. The manuscript retains `[0,A/3-u]`, full maxima and exact inputs. The stronger `epsilon_b<7/160` follows from the inherited distance bound, freshly checked. |
| Four-block endpoint and strict saving, 375-394 | `research/PERMUTED_HALVES_FOURTH_ADJACENT_BLOCK.md:14` through Section 4 supplies exactly the same fixed parameters, separate slabs, normalized integral, centered denominator, `eta=1/20000`, saving denominator and signed remainder. The explicit cost is not asserted optimal. General finite/full transfer is supplied separately by the general-block theorem, not by the earlier continuous-only note. |
| Lower definitions and rational endpoints, 398-429 | `research/THREE_LEVEL_COMMON_CHAIN.md:485` onward defines the shared-order minimax, same integrals and constants; lines 818-1044 define the closed width region, cubic and global quotient optimum. All three cutoffs, `a,b`, `16+432 sum h_i`, the two 23-place endpoints and weak global inequality agree. The manuscript's `z_*` correctly avoids conflating this cubic root with the upper input `x_*`. |
| Shared-energy lower proof outline, 431-443 | Directly checked `COMMON_CHAIN_QUANTITATIVE_STABILITY.md` Sections 2-3 and 11.1-11.3, then `THREE_LEVEL_COMMON_CHAIN.md` Sections 7 and 9. Degree-two reflected dual gives `E<=8e`; isolated/run deletion plus marginal cancellation gives `54E+2K_i`; separated crossings spend the same energy once; minimax yields the exact denominator. Global transfer uses deletion from an arbitrary full feasible arrangement, preserving original labels and both directed arcs. |
| Closed maximum and limit passage, 444-454 | `THREE_LEVEL_COMMON_CHAIN.md:827-913` gives `G'<0`, positive multipliers and the strict cubic remainder. Lines 981-1039 first fix `0<t<1`, then take `n->infinity`, then `t->1`. Both finite floor separations fail at `n=50000k+1` for unchanged boundary widths. The manuscript states the correct order and limitation; it does not claim an eventual unscaled finite gate. |
| Supnick choice, 459-463 | Historical angular/Supnick statement, actual kernel derivatives in `SUPNICK_FULL_FEASIBILITY.md:98-146`, and the classical-import section of `FIXED_ORDER_INTERNAL_AUDIT.md`. Positive mixed derivative and the maximum-tour theorem applied to the negative cost give one chain minimizer. No uniqueness or full feasibility after obstruction is inferred. Primary bibliography checking is handled separately. |
| Fixed-order iff and six-row table, 465-484 | Read `SUPNICK_FULL_FEASIBILITY.md` Sections 1-4 and 6 directly: the minimum triangle defect, fan telescoping for both arcs, forced adjacent gaps, `N=3,4` and weak equality are all covered. `SUPNICK_SEAM_SEQUENCES.md` initial statement and Section 6 identify the strict all-`k>=6` signs and radius-6 bridge. The exact `k>=1,n>=k+2` domain and every table endpoint match. The prior fixed audit identifies all 12 bridge checks and the minimal persistence/sequence dependencies. This pass did not repeat all 12 transcendental bridges or re-prove the entire threshold derivative argument. |
| Finite scope and verifier run, 486-495 | Read `verify.py` completely, original `n=14` frontier and optimum fields, relevant extraction/search code and `CLEAN_RUN.txt:25-40`. The historical clean-source record has all 12 incumbent/local/frontier PASS lines, including the exact `n=14` count. Fresh artifact integrity checks below agree. This pass did not rerun full geometry or exhaustive generation. EF-1 records the numerical assumption boundary. |
| Reproducibility and limitations, 497-527 | Smoke mode is explicitly distinguished from full-frontier checking; local checks do not imply hosted CI or external acceptance. No optimum beyond 14, all-`n` floating cascade, closed form or efficient evaluation is asserted. Supplement citations point to actual existing proof/audit files; the parent separately pins the final supplement identity. |

The initial attempted read of a file named `VERIFICATION_RECORD.md` found
no such file; the actual packet explicitly names `VERIFICATION.md`, which
was read and used. No evidence claim depends on the nonexistent filename.

## Fresh local executable checks

Environment: Windows PowerShell, CPython 3.14.3. The fixed-feasibility checker
reports SymPy 1.14.0. All runs below are new executions in this submission
audit, not relabeled historical outputs. They import no production Ringmin
code and provide bounded exact arithmetic corroboration; the proofs supply
infinite quantifiers. Legacy assertion-based checkers ran with assertions
enabled. Historical extra comparisons printed by a checker are not adopted
as additional reviewed claims.


### `width`

Command: `python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py`. Exit 0.

```text
PASS formal polynomial identities: global cubic remainder and scaling loss
PASS alternating rational Taylor gates: tau, q, pi
PASS exact cubic identities; G'<0 on [0,a]; isolated root signs
PASS positive F and KKT multipliers; unique-global proof applies
PASS accepted witness is not local: positive first-coordinate derivative
0.00136820131190299900276 < D_1 < 0.00136820131190299900279
0.00196196296152142894680 < D_2 < 0.00196196296152142894683
0.00241410289623904895464 < D_3 < 0.00241410289623904895467
0.00451910758124825999999 < x_star < 0.00451910758124827000001
0.00452089241875172999999 < h_star_1 < 0.00452089241875174000001
0.00451910758124825999999 < h_star_2 < 0.00451910758124827000001
0.00734089241875172999999 < h_star_3 < 0.00734089241875174000001
0.00035105290142936543670 < lambda_1 < 0.00035105290142936940356
0.00059414888796317986218 < lambda_2 < 0.00059414888796318518264
0.00000038803240421408705 < eta_width < 0.00000038803240421408841
0.00000038785322987836585 < eta_4 < 0.00000038785322987836588
0.00000000017917433572119 < eta_width-eta_4 < 0.00000000017917433572254
0.04619642739017392470216 < relative_gain_percent < 0.04619642739051527365913
0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392
0.00000000004864271653624 < strict_rational_witness_gain < 0.00000000004864271653627
PASS boundary floor failure for n=50000k+1; no eventual unchanged gate
PASS strict scaling: t=9999/10000, N=1106195; loss < 5e-11
PASS improved rational witness: both margins 1/100000, N=100000
PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers
```

### `fourth`

Command: `python -I -S ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py`. Exit 0.

```text
EXACT A-3w > 354539/1000000000 > 0
EXACT A-3w-4eta_0 > 154539/1000000000 > 0
EXACT a-w-eta_0 > 204539/3000000000 > 0
EXACT b-w-eta_0 > 520991513/1000000000 > 0
EXACT 3/2-M > 21016513/1000000000 > 0
PASS 16 corner partitions, 448 reflection moments, 48 branch probes, 6 sign/tie controls
EXACT 16-panel raw full-max increment <= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
PASS bounded exact support; analytic proof supplies interval and cubic term
NOTE no root solving, width scan, finite recovery, transfer or output files
```

### `fixed`

Command: `python -I -S ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py`. Exit 0.

```text
derivative_upper_c5_at_6=-205349/72000 margin_below_minus_8over3=13349/72000
derivative_lower_c6_at_6=1398247/363000 margin_above_8over3=430247/363000
parity_constructions=4 cyclic_edges=104 central_correction=PASS
c=5 gate=radical_coefficient degree=8 positive_coefficients=9 origin_zero=False endpoint_1over6=PASS
c=5 gate=lower_presquare degree=10 positive_coefficients=11 origin_zero=False endpoint_1over6=PASS
c=5 gate=lower_margin degree=20 positive_coefficients=20 origin_zero=True endpoint_1over6=PASS
c=5 gate=upper_presquare degree=10 positive_coefficients=11 origin_zero=False endpoint_1over6=PASS
c=5 gate=upper_margin degree=20 positive_coefficients=20 origin_zero=True endpoint_1over6=PASS
c=6 gate=radical_coefficient degree=8 positive_coefficients=9 origin_zero=False endpoint_1over6=PASS
c=6 gate=lower_presquare degree=10 positive_coefficients=11 origin_zero=False endpoint_1over6=PASS
c=6 gate=lower_margin degree=20 positive_coefficients=20 origin_zero=True endpoint_1over6=PASS
c=6 gate=upper_presquare degree=10 positive_coefficients=11 origin_zero=False endpoint_1over6=PASS
c=6 gate=upper_margin degree=20 positive_coefficients=20 origin_zero=True endpoint_1over6=PASS
targeted_rejections=6 PASS
exact_sequence_gates=PASS arithmetic=stdlib/Fraction optimized_safe=YES
production_imports=0 diagnostic_imports=0 root_evaluations=0 k_scan=NONE
```

### `lambda`

Command: `python -I -S ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only`. Exit 0.

```text
PASS interval arithmetic: 2835 point and 297 box Fraction oracle checks; square and domain gates
PASS analytic square gates: z(1/3)>2/7; Phi'>41/72 in the middle; Phi'<-1/420 in the tail
EXACT D(53/500) in (-3/10000,-1/5000); enclosure=[-291784193,-291784192]/1000000000000
EXACT D(107/1000) in (7/100000,9/100000); enclosure=[80028360,80028361]/1000000000000
EXACT Phi(719/2500) in (-1/20000,-1/25000); enclosure=[-45419090,-45419089]/1000000000000
EXACT Phi(2877/10000) in (1/10000,11/100000); enclosure=[102023574,102023575]/1000000000000
EXACT Phi(4/5) in (-1/500,-1/1000); enclosure=[-1828639838,-1828639837]/1000000000000
EXACT E(1) in (3/250,13/1000); enclosure=[12494451212,12494451213]/1000000000000
EXACT alpha_* in (10678476019/100000000000,10678476021/100000000000); lambda_* in (159/500,319/1000)
EXACT descending counterexample interval: [89/100,891/1000] lies after x=4/5 and before the wrap
EXACT C_ref(159/500) in (14191368/100000000,14191369/100000000); enclosure=[141913685638,141913685659]/1000000000000
EXACT C_30 in (14192459/100000000,14192460/100000000); enclosure=[141924592047,141924592066]/1000000000000
PASS exact gates: C_rp<C_ref(159/500)<C_30-1/100000; C_rp<14191369/100000000
```

### `alpha`

Command: `python -I -S ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py --exact-only`. Exit 0.

```text
PASS analytic rational gates: wrap gap>1/15; Fsecond>46/405>1/9; Fprime(0)<-29/1245; Fprime(1/2)>13/108; Esecond<3
EXACT E(5753/20000) in [-844268665,-844268070]/1000000000000
EXACT E(x_*) in [-844272415,-844268070]/1000000000000
EXACT D(1093/10000) in [935124205,935201790]/1000000000000
EXACT Fprime(1093/10000) in [-1427184,-1344781]/1000000000000
EXACT D(10931/100000) in [938842182,938919761]/1000000000000
EXACT Fprime(10931/100000) in [2282349,2364747]/1000000000000
PASS isolation/comparison: 1093/10000<alpha_hat<10931/100000; C_107-C_hat>1/22000000; C_hat<14191364/100000000
PASS recovery: 120 exact cases, m=2..16; endpoint shifts, coincident seams, cyclic predecessors and 3/m errors
```

### `boundary`

Command: `python -I -S ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py`. Exit 0.

```text
EXACT lower residual = 10516971471577279/21018800219582721
EXACT lower signed square = -342531413518344092144807428477/441789962670730640526171361763841 < 0
EXACT upper residual = 251647560246539/503426690473461
EXACT upper signed square = 51974394530491111127115563/253438432681061908372345318521 > 0
EXACT location slack = 8431/32000000 > 0
PASS imported bracket order and two directed endpoint sign gates
PASS analytic distance-bound implication: 43/1000 < epsilon_b < 11/250
NOTE: continuum proof and imported minima are separate; no numerical root or integral is certified here
```

### `mixed`

Command: `python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py`. Exit 0.

```text
EXACT inherited epsilon slack = 431/32000000
EXACT lower residual = 1088173975683910831/2175907136349689169
EXACT lower signed square = -963745517404602389188679409068317/4734571866017504812540302482915910561 < 0
EXACT upper residual = 226493965596937/453065245150063
EXACT upper signed square = 34763358497298510706339907/205268116362886684743388903969 > 0
EXACT stationary upper slack = 35511/800000000
EXACT diagonal cutoff slack = 354539/3000000000
EXACT cost denominator slack = 24416513/1000000000
EXACT cost difference bracket = -2187/2048000000000 , -24389/72000000000000
EXACT saving over 1/250 > 12389/72000000000000
PASS two directed rational sign gates and positive pre-square residuals
PASS inherited bounds and analytic location/cost implications
NOTE: continuous proof supplies uniqueness; no finite recovery or geometric transfer
```

### `fixed_feasibility`

Command: `python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py`. Exit 0.

```text
EXACT IDENTITY AUDIT; SymPy=1.14.0; no numeric roots
PASS: 9 general identities; N=3/N=4 closure and all paths; rational N=3 root 6/23; 2 wrong-sign rejections
PASS: 32 rank/parity constructions, 276 edges; all rotations/reflections; both central-correction cases
PASS: 1482 unordered pairs, 2964 directed paths; formal telescoping and complementary coverage
PASS: 82 rejection gates total
LIMIT: finite audits guard transcription; the note supplies the all-k proof
```

### Fail-closed negative control

Command:
`python -I -S -O ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py`.
Exit **1**, intentionally, with exact material diagnostic:

```text
RuntimeError: This checker requires enabled assertions; omit -O.
```

This is successful rejection of an invalid execution mode, not a passing
ordinary run. No claim that every older checker is optimization-safe follows.

## Independent saved-evidence integrity check

A separate stdlib-only inline Python command was executed with
`python -I -S -c` and a PowerShell single-quoted here-string. It did not
import `verify.py`, the production package or the archive utility. Its
operations were:

1. Read the ordered 12-entry tracked archive manifest.
2. Recompute every archive SHA-256, decompress every archive in memory,
   and independently recompute each decoded log SHA-256 and length.
3. Recompute every frontier JSON canonical content hash.
4. Check every coverage total against `(n-1)!/2`, every prefix set against
   `{1,...,n-1}`, and every individual prefix count against
   `(n-1-prefix)*(n-3)!`.
5. Find the corresponding exact positive-count prefix completion line in
   each independently decoded log; compare every saved top-excluded
   prefix guard against threshold plus the recorded float64 guard using
   exact `Fraction` arithmetic.
6. Check every retained order is a complete permutation, fixed-largest
   and reflection canonical, distinct within its frontier, and marked
   Stage-B evaluated; check each incumbent has all labels and positions.
7. Check each original incumbent's 50-digit radius equals its frontier's
   linked radius exactly, and every generation hash is
   `fea000523a1ec4193d8ba9c4637563fd65e86d1a`.
8. Parse `verify.py` with `ast` and confirm its static imports contain
   no production `ringmin` package.

Exact command (assertions enabled):

```powershell
python -I -S -c @'
from pathlib import Path
from math import factorial
import hashlib,json,gzip,ast,sys
from fractions import Fraction as Q
root=Path('.')
manifest=json.loads((root/'reproducibility/frontier_logs/manifest.json').read_text())
assert [r['n'] for r in manifest['logs']]==list(range(3,15))
count=frontiers=0
for row in manifest['logs']:
 n=row['n']; raw=(root/'reproducibility/frontier_logs'/row['archive']).read_bytes(); log=gzip.decompress(raw)
 assert hashlib.sha256(raw).hexdigest()==row['archive_sha256']
 assert hashlib.sha256(log).hexdigest()==row['sha256'] and len(log)==row['bytes']
 count+=len(log)
 f=json.loads((root/f'results/frontiers/n{n:02d}_frontier.json').read_text())
 clone=dict(f);clone['content_sha256_excluding_hash']=None
 assert hashlib.sha256(json.dumps(clone,sort_keys=True,separators=(',',':')).encode()).hexdigest()==f['content_sha256_excluding_hash']
 assert f['total_canonical_orders']==f['expected_total_canonical_orders']==factorial(n-1)//2
 assert sum(p['count'] for p in f['prefix_coverage'])==factorial(n-1)//2
 assert {p['prefix'] for p in f['prefix_coverage']}==set(range(1,n))
 for p in f['prefix_coverage']:
  assert p['count']==(n-1-p['prefix'])*factorial(n-3)
  if p['count']:
   assert any('stage=stage_a' in line and 'prefix complete' in line and f"prefix={p['prefix']}\t" in line and f"done={p['count']}\t" in line for line in log.decode().splitlines())
  if p['top_excluded_guard_float64']:
   assert Q(p['top_excluded_guard_float64'])-Q(f['float64_lb_error_guard'])>=Q(str(f['threshold_float64']))
 assert f['frontier_size']==len(f['orders'])
 orders=[]
 for e in f['orders']:
  o=tuple(e['order']);assert sorted(o)==list(range(1,n+1)) and o[0]==n and o[1]<o[-1] and e['stage_b_evaluated'];orders.append(o)
 assert len(set(orders))==len(orders);frontiers+=len(orders)
 o=json.loads((root/f'results/n{n:02d}/optimum.json').read_text())
 assert sorted(o['ordering'])==list(range(1,n+1)) and len(o['positions'])==n and o['n']==n
 assert o['generation_commit_hash']==f['generation_commit_hash']=='fea000523a1ec4193d8ba9c4637563fd65e86d1a'
 assert Q(o['R_mpmath_full'])==Q(f['incumbent_R_mpmath'])
 print(f'PASS n={n:02d}: original/archive hashes, {len(orders)} valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance')
mod=ast.parse((root/'verify.py').read_text())
imports=[x.names[0].name for x in ast.walk(mod) if isinstance(x,ast.Import)] + [x.module for x in ast.walk(mod) if isinstance(x,ast.ImportFrom)]
assert all(x and not(x=='ringmin' or x.startswith('ringmin.')) for x in imports)
print(f'PASS {len(manifest["logs"])} archive/log hash pairs, {count} decoded bytes, {frontiers} frontier orders; 13!/2={factorial(13)//2}; verifier has no production Ringmin import')
print('Scope: saved evidence integrity and consistency only; no excluded-order regeneration, directed all-order floating error proof, geometry rerun, or external acceptance')
print('Python '+sys.version.split()[0])
'@
```

Exit **0**. Exact material output:

```text
PASS n=03: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=04: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=05: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=06: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=07: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=08: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=09: original/archive hashes, 1 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=10: original/archive hashes, 4 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=11: original/archive hashes, 6 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=12: original/archive hashes, 9 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=13: original/archive hashes, 10 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS n=14: original/archive hashes, 11 valid distinct canonical frontier orders, prefix counts and guard summaries, linked incumbent provenance
PASS 12 archive/log hash pairs, 9649682 decoded bytes, 47 frontier orders; 13!/2=3113510400; verifier has no production Ringmin import
Scope: saved evidence integrity and consistency only; no excluded-order regeneration, directed all-order floating error proof, geometry rerun, or external acceptance
Python 3.14.3
```

Integrity and internal consistency do not themselves prove the historical
search correct. They establish no stronger numerical certification than the
original stated guard assumptions. The recorded historical full-verifier
PASS output was inspected; it was not freshly executed by this subagent.

## Protected paths and handoff

Read-only diff command:

```text
git -c safe.directory=<repository-root> diff --name-only -- results verify.py src scripts research knowledge paper_assets/ringmin_paper.tex
```

Only the safe.directory argument above is display-normalized to
`<repository-root>`; all other command tokens are exact.

Exit 0, empty output at this subagent's closing inspection. These scientific,
finite-result and historical-v1 paths had no working diff. The parent is
responsible for final complete/staged diff and all publication package checks.

EF-1 is closed by a source re-read; no unresolved correction remains from
this pass. The endpoint and fixed-order claims agree with the actual proof
sources within the coverage stated above. No external acceptance decision,
submission, release, tag, history mutation or additional task was performed.

## Second bounded check: source packaging and clean-build evidence

The parent requested this engineering review within the same submission
task after the mathematical pass. The complete `check_bundle.py` and
`clean_compile.ps1`, final `BUNDLE_CHECK.json`, candidate
`BUILD_MANIFEST.json`, complete actual `.fls`, and relevant actual
`.log` and pass transcripts were inspected. The clean directory was
`reproducibility/.work/arxiv-clean-1523dfe3b87845d59bb0b7160993dade`.

**Result: no new BLOCKER, IMPORTANT or OPTIONAL finding.** The scripts and
actual evidence establish the stated local package checks within their
scope. This is a review of the known manuscript and its generated PDF, not
a general-purpose hostile TeX/PDF security certification.

### Source isolation, paths and reference stability

- The PowerShell script requires the public directory to contain exactly
  the one regular source file, compares its hash with the candidate, creates
  a new GUID-named directory and checks that it contains only the copied
  source before launching TeX. It neither deletes nor moves any tree.
- Compilation is from that directory with `-no-shell-escape`,
  `-halt-on-error`, `-file-line-error` and `-recorder`.
  `TEXINPUTS=.;` preserves the normal distribution fallback while removing
  an inherited explicit source search path. Environment values and working
  directory are restored in `finally`.
- Source inspection blocks the explicit external-input primitives and
  machine paths used by this source; the actual recorder evidence gives
  the stronger artifact-specific check. Its only local inputs are the
  copied `.tex` and generated `.aux/.out`. Every external input inspected
  here belongs to the installed TinyTeX distribution; no other repository
  file is used for compilation.
- The dependency classifier accepts paths under TeX-tree names; it is not a
  cryptographic allowlist of an arXiv distribution. The actual 108 unique
  system inputs and their hashes are recorded. This is local TinyTeX/TeX
  Live 2025 evidence, not an arXiv-hosted compilation claim.
- Reference convergence is tested on exact `.aux` and `.out` hashes,
  with at least three and at most four passes. The actual first transcript
  reports no initial `.aux`; passes 2 and 3 are byte-identical and free
  of warnings. The complete final log independently passes the stated
  citation/reference, duplicate-label/destination, glyph, box and package
  warning pattern. The final log also reports unchanged bookmark output.

The script implements source-only startup; the final directory naturally
contains generated build files and the parent's later page-render PNGs.
Those later outputs are neither submission source files nor recorder inputs.

### PDF checks and exact byte difference

The Python checker uses an explicit `require` function which raises
`RuntimeError`; it has no correctness dependency on Python assertions.
Its root-object traversal rejects the listed active actions, attachments
and form features; it verifies scalable font descriptors with embedded
font streams and checks the HTTPS URI inventory. For the present generated
artifact this traverses the relevant font, page and annotation objects.

The candidate and clean PDF agree in all nine page texts, decoded painting
streams, dimensions, metadata, all 16 embedded font streams and external
URI sets. The parent separately performs page-by-page visual inspection;
these mechanical comparisons do not replace that judgment.

A separate byte-level check is stronger for these two actual artifacts:
both PDFs have length **333577** and each contains exactly one literal
trailer `/ID` array. Replacing only that array with the same marker makes
the complete files byte-identical. Thus their different SHA-256 values
are fully explained by their trailer IDs, with no other byte difference.
This does not assert byte reproducibility across different TeX environments.

### Fresh commands and exact results

Environment: CPython 3.14.3, pypdf 6.14.2, Windows PowerShell. The optimized
checker was freshly executed:

```text
python -O ops/TASK-20260911__arxiv_submission_audit/check_bundle.py reproducibility/.work/arxiv-clean-1523dfe3b87845d59bb0b7160993dade
```

Exit **0**. Its normal output file is rewritten by that authorized command;
a before/after SHA-256 check confirms `BUNDLE_CHECK.json` remained
byte-identical. No report-content or script edit was made by this reviewer.

```text
PASS one source; 20 unique labels; 9 bibliography keys; 108 TeX-system inputs only
PASS 9 pages identical in text, painting instructions, dimensions and metadata; 16 embedded scalable fonts; no active content
PASS source hygiene; exact HTTPS link inventory; evidence BUNDLE_CHECK.json
PASS optimized checker evidence unchanged SHA256=d3a9b24df7381b0b0b4206849ba1c5d025a0f5e42c64f461b7b78c18fbc5fea8
```

The following independent inline command was then executed, exit **0**:

```powershell
python -I -c @'
from pathlib import Path
import json,hashlib,re
from pypdf import PdfReader
root=Path('.')
c=root/'paper_assets/v2'
b=root/'reproducibility/.work/arxiv-clean-1523dfe3b87845d59bb0b7160993dade'
m=json.loads((c/'BUILD_MANIFEST.json').read_text())
for name,wanted in m['files'].items():
 actual=hashlib.sha256((c/name).read_bytes()).hexdigest()
 if actual!=wanted: raise RuntimeError('Manifest hash mismatch: '+name)
 print('PASS BUILD_MANIFEST '+name+' '+actual)
x=(c/'ringmin_v2.pdf').read_bytes();y=(b/'ringmin_v2.pdf').read_bytes()
pat=rb'/ID\s*\[\s*<[0-9A-Fa-f]+>\s*<[0-9A-Fa-f]+>\s*\]'
if len(re.findall(pat,x))!=1 or len(re.findall(pat,y))!=1: raise RuntimeError('Unexpected PDF ID representation')
if re.sub(pat,b'/ID [NORMALIZED]',x)!=re.sub(pat,b'/ID [NORMALIZED]',y):raise RuntimeError('PDF difference beyond trailer ID')
print('PASS PDFs byte-identical after normalizing their sole trailer /ID array; original lengths '+str((len(x),len(y))))
for name in ('pass-2.txt','pass-3.txt'):
 txt=(b/name).read_text();
 if 'Warning' in txt or 'Overfull' in txt or 'Underfull' in txt or 'undefined' in txt:raise RuntimeError('Late pass warning')
if (b/'pass-2.txt').read_bytes()!=(b/'pass-3.txt').read_bytes():raise RuntimeError('Final pass transcripts differ')
if 'No file ringmin_v2.aux.' not in (b/'pass-1.txt').read_text():raise RuntimeError('First-pass source-only evidence missing')
print('PASS first transcript begins without aux; pass-2 and pass-3 transcripts are identical and warning-free')
log=(b/'ringmin_v2.log').read_text()
if re.search(r'Overfull |Underfull |Missing character|undefined|multiply defined|Rerun to get|Label\(s\) may have changed|Package .* Warning|LaTeX Warning|destination with the same identifier',log):raise RuntimeError('Final log warning')
print('PASS final actual log has no reference/citation/glyph/box/package warning')
'@
```

Exact material output:

```text
PASS BUILD_MANIFEST ringmin_v2.tex 189232a42ab4e8d2a77d1fd3535f08ab8e0aa9c22cbdcee1427a472f152ee39a
PASS BUILD_MANIFEST build.py cdf525ee1fd9ac5da88f6030bf94ef361910e19315d834f70f88e19dc023980a
PASS BUILD_MANIFEST ringmin_v2.pdf c3fc42c1f8796d86938260dc7764277458982306315668d244a94686bc9f3ef9
PASS PDFs byte-identical after normalizing their sole trailer /ID array; original lengths (333577, 333577)
PASS first transcript begins without aux; pass-2 and pass-3 transcripts are identical and warning-free
PASS final actual log has no reference/citation/glyph/box/package warning
```

The clean PDF hash remains
`2d3deef7df68e4ef69353fed17d8c4e15577402c88eebed5a93b6fd3ebc23b3b`.
The source hash is the same for the candidate, minimal bundle and clean copy.
All three actual candidate files match their build-manifest hashes.
This second review does not run another compilation or claim arXiv's own
PDF has been generated or visually approved.
