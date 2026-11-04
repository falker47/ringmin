# Independent Upper-Bound Review

    reviewed_on=2026-10-23
    mode=STRICT
    baseline=75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae
    review_kind=delegated adversarial internal analytic review
    conclusion=no invalidating gap found in audited scope
    external_acceptance=not performed or implied

## Exact Scope

This follow-up does not repeat the core limit/word-LP audit recorded in
`CORE_AUDIT.md`. It independently reviews the assembled main article's upper
section and the complete new standalone upper supplement, including analytic
dependency closure, every implicit parameter, rational isolation gates, finite
recovery and the strict fourth-block saving.

Final inspected SHA-256 values:

```text
5dec1a8b5a246940288142c92d44817b1f4bb271bb46be5d90adee65e3c1d4c6  paper_assets/paper_ii_journal/upper_supplement.tex
2e74ed7ca0385523d98d8573ce0a0b20b3fbe51a6e9c8adda29550b70df69b06  paper_assets/paper_ii_journal/main.tex
e3397e0cb1238103ccb6848730d09e885ec61ba0a58c4bdf090716e0b48220dd  paper_assets/paper_ii_journal/UPPER_DEPENDENCIES.md
```

The full mathematical text was first read at S2 hash `c34de78d5047483c95348d23b85527c25f9cd129364b6218f3666d1353cff7d2`.
The author's subsequent removal of unused packages, equation line breaks,
explicit common countable gate and remainder-bound sentence were inspected
at the final hash above. The author confirmed source completion before this
conclusion. The main upper section was reread at its listed final snapshot.

The current source proof of general transfer and the fourth-block research
note were consulted where needed; the standalone supplement itself provides
the required mathematical arguments. All five included checkers were read.
The dependency table's twelve local hashes and all five original/copy byte
identities were independently verified. Frozen-commit Git blob identity was
reported by the author, but was not independently rerun by this reviewer.

Only this review file was written during this follow-up. No mathematical
source, historical paper, production file, result artifact, Review State
Registry or Git history was edited. Build/PDF layout inspection belongs to
other task gates; no independent PDF or hosted-CI conclusion is made here.

## Analytic Audit

No source correction is requested. The following conclusions result from
reconstructed reasoning, not from the finite tests below.

1. **All pairs and both arcs.** The high-shell inequality has the correct
   trigonometric branch split and strict direction, including the endpoint
   ratio v=2u. The path contraction includes the one-edge case. Every directed
   high/high, low/high and low/low path is covered by a whole high path or a
   strictly sufficient incident high gap. The m=2 case and cyclic predecessor
   are included. Cell constraints plus closure therefore suffice, not just
   adjacency. The continuous strictly decreasing score has its unique positive
   root before being identified with the actual full fixed-order minimum.
2. **Genuine permutations and complete cells.** Each rounded start is even;
   reversing even slots is a disjoint involution, including zero and two-rank
   blocks. The high cyclic shift is a bijection. The gate r-z>=2 puts every
   block exit before the wrap. Interior cells, shared exits/entries, cell 1
   and the two wrap cells form the stated complete disjoint inventory.
3. **Recovery and seam errors.** The two orientations are allocated to
   half-masses on double panels and include nonsymmetric tests. All exceptional
   cells remain in the empirical measure. Floor displacement bounds are
   summed conservatively even with overlapping bad intervals and zero slabs.
   The constants in the modulus bound yield exactly
   (6k^2+28k+36)/m for the full maximum, using its global 4-Lipschitz bound.
   The low-mark square-root singularity is excluded by chord dominance below
   t=1/4; no unjustified global derivative bound is used there.
4. **Root scale and geometry.** The angle error follows from a valid
   denominator bound and arcsine remainder for m>=32 and c>=1/32. The scalar
   maximum does not require branch agreement. At m>=2048, the proof brackets
   the actual normalized root in (1/32,1/2) before substituting it. The final
   coefficient 1060 is 36+1024, and the k=4 coefficient is 1268. Deleting only
   label 2m gives the odd limsup without claiming the odd fixed-order optimum.
5. **Countably many blocks.** Each finite truncation has the common geometric
   gate because its total is bounded by T<1-alpha. Tail integral error is at
   most 2||F|| times the omitted length. Increasing thresholds faster than k^3
   make the finite modulus/error bounds vanish; a density argument then covers
   continuous tests. This establishes recovery, not an optimal partition.
6. **Exact normalized prefix minimum.** The unsquared switch is unique and
   increasing. First-derivative moving terms cancel by cost equality, while
   the positive second-derivative switch term is retained. The middle interval
   has Phi'>41/72, isolating one zero. The separate tail proof gives
   Phi'<-1/420, and E(1)>0 together with endpoint concavity excludes a lower
   tail minimum. It does not extrapolate middle convexity. The two rational
   signs isolate the unique global x* without substituting a decimal value.
7. **Exact shift minimum.** The split K integral treats the moving wrap.
   Its second derivative and the bound on e=E(x*) imply
   F''>46/405>1/9 on the stated interval. Endpoint signs guarantee exactly one
   zero. The Taylor enclosure about the stationary x* has the correct
   displacement 3/800000000. Directed concavity quadrature and a reversed
   negative-wrap enclosure give the displayed rational endpoint signs.
8. **Second and third width minima.** The common lemma applies first at
   lambda and then at v, with both starts strictly in (A/4,A/3). The ratio
   is increasing in the slab coordinate; the mixed switch lies after the
   midpoint. The formula for z' is positive and below 1/2. The nonzero Q
   term in Psi' is retained; Psi'>131/120>1 and the positive cutoff derivative
   establish a unique mixed stationary minimum. The bound on distance from
   entry follows by integrating Psi'>1. The entry-sign corners have valid
   monotonicity directions and positive pre-square residuals. The sharper
   epsilon<7/160 follows from the explicit slack; it is not silently imported
   from the weaker 11/250 output in the older boundary checker.
9. **Rational algorithms.** The grid interval arithmetic encloses every
   operation, excludes zero denominators, and uses valid convergent atan/log
   tails. Switch bisections require separated unsquared signs. The primitive
   derivatives match the actual split integrals. The independent shift gates
   use concave trapezoid/midpoint bounds and pay for the omitted switch
   interval. Tables and signed fractions in S2 match fresh checker outputs.
10. **Fourth independent block.** The exact preceding minima remain fixed.
    Only the new diagonal slab changes, so earlier mixed branches cancel with
    their full costs. Separate reflection preserves both high marginals and
    introduces no positive-mass seam. The enclosing corners keep both changed
    maxima strictly chord on the entire closed slab at every
    0<eta<=1/20000. Rationalization gives the negative integral with the
    correct factor 1/(4 pi). Denominator bounds prove the signed cubic
    remainder and strict finite saving; no sign is inferred from a formal
    asymptotic expansion alone. The saving is exactly greater than
    1/4608000000000000 at the specified rational width.
11. **Final transfer and main consistency.** All four lengths satisfy the
    general theorem's strict pre-wrap hypothesis. Therefore the literal
    full-cost U4 transfers to feasible even and odd placements. Main.tex
    retains the same exact implicit definitions, intervals, error constants,
    cubic remainder and strict inequality. No four-block or finite global
    optimality is asserted.
12. **Dependencies and evidence scope.** The standalone proof closes the
    historical fourth-block note's deliberately deferred transfer through
    the general theorem. Historical alpha-star/C30/C107 comparison outputs
    of reused scripts are explicitly excluded as premises. The documented
    120 recovery cases belong only to the inherited single-prefix checker;
    the universal multiple-block theorem remains analytic.

The initial packaging caution was that four inherited checkers use Python
assertions. The final supplement/dependency document explicitly requires
ordinary execution; the package runner also rejects -O. The reviewer checked
that rejection directly. No unresolved actionable issue remains in this scope.

## Fresh Local Verification

Environment: Windows PowerShell; Python 3.14.3, standard library only for the
upper checks. From `paper_assets/paper_ii_journal`, all five commands exited 0:

```text
python -I -S -B checks/upper_lambda.py --exact-only
python -I -S -B checks/upper_alpha_minimum.py --exact-only
python -I -S -B checks/upper_boundary.py
python -I -S -B checks/upper_mixed_width.py
python -I -S -B checks/upper_fourth_block.py
```

Material outputs independently reproduced:

```text
PASS interval arithmetic: 2835 point and 297 box Fraction oracle checks; square and domain gates
Phi(719/2500): [-45419090,-45419089]/10^12, strictly inside (-1/20000,-1/25000)
Phi(2877/10000): [102023574,102023575]/10^12, strictly inside (1/10000,11/100000)
Phi(4/5): [-1828639838,-1828639837]/10^12, strictly inside (-1/500,-1/1000)
E(1): [12494451212,12494451213]/10^12, strictly inside (3/250,13/1000)
E(5753/20000): [-844268665,-844268070]/10^12
E(x_*): [-844272415,-844268070]/10^12
D(1093/10000): [935124205,935201790]/10^12
Fprime(1093/10000): [-1427184,-1344781]/10^12
D(10931/100000): [938842182,938919761]/10^12
Fprime(10931/100000): [2282349,2364747]/10^12
PASS recovery: 120 exact cases, m=2..16; endpoint shifts, coincident seams, cyclic predecessors and 3/m errors
second lower signed square: -342531413518344092144807428477/441789962670730640526171361763841
second upper signed square: 51974394530491111127115563/253438432681061908372345318521
inherited epsilon slack: 431/32000000
third lower signed square: -963745517404602389188679409068317/4734571866017504812540302482915910561
third upper signed square: 34763358497298510706339907/205268116362886684743388903969
stationary upper slack: 35511/800000000
diagonal cutoff slack: 354539/3000000000
PASS 16 corner partitions, 448 reflection moments, 48 branch probes, 6 sign/tie controls
EXACT 16-panel raw full-max increment <= -701561353/200000000000000000000000
PASS raw enclosure < -1/288000000000000
EXACT normalized saving > 1/4608000000000000 using pi<4
PASS cutoff chain-excess/diagonal-tie control; 3 invalid chord gates rejected
```

The boundary checker separately prints its older epsilon<11/250 conclusion;
S2 uses its two exact entry signs and the sharper slack checked in the mixed
width script. Historical comparison outputs were observed but are not used
as newly validated claims in this review.

The command `python -I -S -B -O verify_math.py` exited 1 as required, with:

```text
FAIL: assertions must remain enabled; do not use -O
```

A standard-library hash probe checked all twelve listed source-table hashes
and compared the five included scripts byte-for-byte with their specifically
linked original files. It exited 0 with:

```text
PASS 12 source-table hashes; 5 byte-identical checker copies.
```

The exact hash-probe program, piped to `python -I -S -B -` from the repository
root, was:

```python
from pathlib import Path
from hashlib import sha256
import re
root=Path.cwd()
pkg=root/'paper_assets/paper_ii_journal'
text=(pkg/'UPPER_DEPENDENCIES.md').read_text(encoding='utf-8')
checked=0
for path, wanted in re.findall(r'\| ([^|]+?) \| `([0-9a-f]{64})` \|',text):
    source=(pkg/path) if path.startswith('checks/') else (root/path)
    actual=sha256(source.read_bytes()).hexdigest()
    if actual != wanted:
        raise RuntimeError(('source hash',path,actual,wanted))
    checked+=1
pairs=[('upper_lambda.py','ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py'),('upper_alpha_minimum.py','ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py'),('upper_boundary.py','ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py'),('upper_mixed_width.py','ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py'),('upper_fourth_block.py','ops/TASK-20260911__fourth_adjacent_block/check_fourth_block.py')]
for copy, original in pairs:
    if (pkg/'checks'/copy).read_bytes() != (root/original).read_bytes():
        raise RuntimeError(('checker differs',copy))
print(f'PASS {checked} source-table hashes; {len(pairs)} byte-identical checker copies.')
```

## Independent Finite Cell-Inventory Probe

This additional bounded check imports neither production code nor existing
checkers. It constructs shifted high lists and reverses slices independently
of the displayed J formula, then compares every actual cyclic cell with the
written inventory. Since target coordinates on a panel are affine, checking
both endpoints verifies its stated coordinate bound on that panel in each
finite fixture. The exact command was the following program piped to
`python -I -S -B -` from the journal-package directory:

```python
from fractions import Fraction as Q
from math import ceil
profiles = cases = cells = panel_endpoints = 0
for alpha in (Q(0), Q(1,7), Q(1,2), Q(9,10)):
    room = 1-alpha
    lengths_sets = [(Q(0),), (2*room/5,), (room/8, Q(0), room/6, Q(0)), (Q(0), room/100, room/2, Q(0)), (room/16,)*4]
    for lengths in lengths_sets:
        profiles += 1
        minimum = max(2, ceil(2/(1-alpha-sum(lengths))))
        for m in range(minimum, 97):
            s = (alpha*m)//1
            ls = [2*((length*m/2)//1) for length in lengths]
            starts = [0]
            for length in ls:
                starts.append(starts[-1]+length)
            r = m-s
            p = list(range(m+s+1, 2*m+1))+list(range(m+1, m+s+1))
            for a, length in zip(starts, ls):
                p[a+1:a+length:2] = reversed(p[a+1:a+length:2])
            if sorted(p) != list(range(m+1, 2*m+1)) or r-starts[-1] < 2:
                raise RuntimeError('permutation or wrap gate')
            def H(u):
                return m+1+((u+s-1) % m)
            exceptional = {1:(H(m),H(1)), r:(2*m-1,2*m)}
            if r+1 <= m:
                exceptional[r+1]=(2*m,m+1)
            interior = {}
            for a, length in zip(starts, ls):
                if length:
                    exceptional[a+length+1]=(H(a+2),H(a+length+1))
                for i in range(a+2,a+length+1):
                    if i in interior or i in exceptional:
                        raise RuntimeError('classification overlap')
                    interior[i]=(a,length)
            if len(exceptional) > len(lengths)+3:
                raise RuntimeError('exceptional count')
            for i in range(1,m+1):
                actual=(p[(i-2)%m],p[i-1])
                if i in interior:
                    a,length=interior[i]
                    expected=(m+s+i-1,m+s+2*a+length+2-i) if i%2 == 0 else (m+s+2*a+length+3-i,m+s+i)
                    edges=(Q(i-2,m),Q(i,m)) if i%2 == 0 else (Q(i-1,m),Q(i+1,m))
                    for t in edges:
                        plus=(t,1+Q(s,m)+t,1+Q(s+2*a+length,m)-t)
                        target=plus if i%2 == 0 else (plus[0],plus[2],plus[1])
                        point=(Q(i,m),Q(actual[0],m),Q(actual[1],m))
                        if max(abs(x-y) for x,y in zip(point,target)) > Q(4,m):
                            raise RuntimeError('interior panel error')
                        panel_endpoints += 1
                elif i in exceptional:
                    expected=exceptional[i]
                else:
                    expected=(H(i-1),H(i))
                if actual != expected:
                    raise RuntimeError((alpha,lengths,m,i,actual,expected))
                cells += 1
            cases += 1
print(f'PASS {profiles} fixed rational profiles; {cases} genuine permutations; {cells} exact cells; {panel_endpoints} affine panel endpoints; zero/two-length blocks and both wrap directions covered.')
```

It exited 0 with:

```text
PASS 20 fixed rational profiles; 1720 genuine permutations; 90645 exact cells; 24472 affine panel endpoints; zero/two-length blocks and both wrap directions covered.
```

These fixtures corroborate the inventory and finite panel arithmetic only.
They do not establish the universal transfer theorem, the angular criterion,
implicit-minimum uniqueness, or a new finite Ringmin optimum.

## Handoff and Limits

The source statements are classified as exact theorems and proved corollaries;
the fresh script outputs are independently reproduced bounded finite results.
This review found no invalidating mathematical or proof-dependency gap in the
upper endpoint at the stated snapshots. It does not constitute external
acceptance, verify unrelated lower-supplement mathematics, certify a finite
optimum, review all PDF pages, or establish a hosted CI result. No commit or
push was performed by this reviewer.

Next atomic review gate: review the final exact journal package, including
PDF presentation, manifest/standalone verification and the committed SHA.
