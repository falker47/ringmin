# Internal adversarial dependency audit of the explicit lower endpoint

Date: 2026-09-11. Mode: STRICT. Scope: the proof of
`liminf R*(n)/n^2 >= L = C_term + eta_width` at the three cutoffs in
`research/THREE_LEVEL_COMMON_CHAIN.md`, Section 12. This is a separate
internal subagent audit, not external acceptance or a finite certificate.

Audited tracked source HEAD: `372f96c0a9f14d968e7ecb3b1a039e7867340005`.
The parent goal's authorized work was already present in the working tree.
This audit changes only this file; no source, ledger, published asset,
certificate, review registry, Git state or external state was mutated.

## Conclusion and exact scope

**INTERNALLY VALIDATED within the dependency path below.** No proof gap or
counterexample was found in the current lower endpoint. The exact rational
checker independently rerun in this audit reproduces

```text
0.14056946887766098063257 < L < 0.14056946887766098063392.
```

This is an enclosure of a theorem's explicit constant, not a numerical
estimate of the true optimum. The lower-bound theorem is non-strict at
`L`. Its global transfer starts from arbitrary full feasible configurations,
and does not infer full feasibility from a chain root.

The entire minimal analytic dependency path for this lower endpoint was
read and rederived as recorded below. This does **not** audit every result
in the much larger source notes. In particular it does not audit all
historical terminal-subset optimality claims, the sharpness constructions,
earlier two-/three-level gains, the Section 13 method ceiling, any upper
construction, or any finite optimum certificate. Those results are not
premises of this endpoint when the direct proof path below is used.

## Minimal dependency graph and claim matrix

All source paths are repository relative. Every row is an analytic theorem
or elementary identity; the checkers provide the more limited evidence
specified in the final column. All rows were internally rederived in this
audit. No external acceptance status is created by this document.

| Claim used by L | Exact scope and proof source | Immediate dependencies | Computational support and limit |
| --- | --- | --- | --- |
| Angular kernel; full-feasible deletion implies each induced chain root is at most R | `knowledge/DEFINITIONS.md`; elementary center-distance identity; `research/THREE_LEVEL_COMMON_CHAIN.md` Section 9 final paragraph | Outer circles tangent to the central circle; all pair constraints; original radii retained; at least three survivors | Analytic derivation below, no finite-certificate premise |
| `W/pi-1/n <= R_chain/n^2 <= W/pi` | `research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md` Section 2, every cyclic order of at least three radii in `{1,...,n}` | Elementary asin/atan bounds and chain monotonicity | Analytic and order uniform |
| Reflected reference `J_n`, excess `e>=0`, energy `E<=8e` | Same note Section 3 through equation (6); Section 11.1 | Explicit dual potential, degree two, grid reflection | Signed-deletion checker: exact marginals and symbolic/direct-cost diagnostics |
| `|W_i-W_0-D_(i,n)|<=54E+2K_i` | Same note Sections 11.2 and beginning of 11.3 through equation (38), with Section 4 run accounting; generalized only over the domain in three-level Section 9 | `a>1/6`, `a<1/5`, cutoff at a grid midpoint, all deleted labels below `23n/100`, three survivors | Signed-deletion checker plus 120 fresh three-cutoff direct-cost diagnostics; analytic proof supplies uniformity |
| `|J_n-J|<=5/n`, `|D_(i,n)-D_i|<=19/(2n)` | Same note Section 5 | Explicit derivative bounds, floor errors less than `1/n` | Analytic estimates, no evaluated transcendental floor required |
| One common shared-crossing budget | `research/THREE_LEVEL_COMMON_CHAIN.md` Section 7 | First-marginal strip bound and adjacent width separation; one outer measure | `check_finite_crossing.py`: exact bounded measures, cycles and negative controls |
| Finite common-order minimax and global lower transfer | Same note Section 9 | All previous rows at every cutoff, scalar minimum over `e>=0`, same nested restrictions | Exact scalar/floor checks; universal all-order/all-n statement is analytic |
| Exact `q`, `J=pi*C_term`, `D_i` | Definitions in the same note and `research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md` Sections 5-6 | `tau=cos(tau)` and elementary integral substitution; rational Taylor/binomial enclosures | `check_width_optimum.py` independently evaluates constants with rational arithmetic |
| Unique optimum over the closed width region | `research/THREE_LEVEL_COMMON_CHAIN.md` Sections 12.1-12.3 | Cubic monotonicity/root signs, positive multipliers, exact remainder identity | Width checker: rational signs and formal polynomial identities; global inequality rederived analytically |
| `liminf R*(n)/n^2>=C_term+eta_width` | Same note Section 12.4 | Fixed scaling of optimal widths, eventual finite gates, continuity | Exact floor residue negative control; no exchange of an n-limit with tours |

The four-level witness in Section 11 supplies the cutoffs and convenient
reproducible parameter enclosures. Its comparison against the old
three-level value is not logically necessary for L. Section 12's standalone
checker rederives the constants rather than importing its checker.

The assignment dual in the third row is sufficient: the lower-bound proof
does not require that `J_n` itself be the cost of a Hamiltonian tour or that
the Supnick tour attain it. Hence the Supnick parity/seam theorem, a
prescribed-order macroscopic discriminator, the older optimized scalar
split and its sharpness families are not hidden prerequisites of L.

## Analytic rederivation and attempted failure modes

### Geometry, angular reduction and C_term

For center radii `R+u,R+v`, the distance between two centers at smaller
angular separation `delta` has square
`(u-v)^2+4(R+u)(R+v)sin(delta/2)^2`. Comparing with `(u+v)^2` gives the
stated kernel. It is strictly decreasing in `R>0`, tends from `pi` to zero,
and a cycle of at least three edges consequently has exactly one positive
closure root.

For each edge, `asin z>=z` and `(R+u)(R+v)<=(R+n)^2` give the angular
lower bound `2sqrt(uv)/(R+n)`. The half-angle atan form and `atan z<=z`
give the upper bound `2sqrt(uv)/R`. Summing at the closure root gives
the sandwich with precisely the stated directions. No asymptotic scale
or order-dependent error was assumed.

Deletion from a full feasible arrangement preserves all surviving pair
constraints. Each directed gap, including a gap exceeding pi and the
closing gap, is at least its pair's minimum angle because its smaller
angular separation is. The directed gaps still sum to `2pi`. Every
restricted chain root is therefore at most R. All restrictions arise
from the same outer order. Minimization over that outer order and then
infimum over full configurations proves `R*(n)>=B_n^(4)`.

The identity linking the reference integral to C_term can be checked
without the terminal Supnick theorem. Put `s=1+q` and
`z=(1-q)/(1+q)=sin(tau)`. Direct substitution gives
`J=s^2[asin(z)+z*sqrt(1-z^2)]/4`. Since `0<tau<1<pi/2` and
`cos(tau)=tau`, the bracket is `tau*(1+z)`, giving
`J=tau*(1+q)/2=pi*C_term`. This also avoids confusing the cutoff q
with the different variable called q in the older terminal optimization
note. Its Sections 5-6 calculus was checked, but the global optimality of
the older terminal construction is not needed to prove this identity.

### Assignment energy and signed deletion

The dual potential derivative is `h'(x)=sqrt((s-x)/x)/2`. Differentiating
`sqrt(xy)-h(x)-h(y)` in y and rationalizing gives exactly the Section 3
derivative, whose denominator lies in `[4a,4]`. Integrating from `s-x`
gives slack at least `(x+y-s)^2/8` on either side; reversing the path
also reverses the numerator sign. Reflection permutes the grid and the
degree-two sum of h is precisely the reference J_n. The factors `1/n`
and `1/(2n)` consequently give `e>=E/8` and exactly equal marginals,
including odd cardinality. No probability normalization is introduced.

The isolated-deletion cost is `sqrt(yz)-sqrt(xy)-sqrt(xz)`. Its two
first derivatives at `y=z=s-x` equal p(x). The displayed Hessian entries
were rederived; row sums are below 6 when `a>1/6`, giving a remainder
at most `3[(y-t)^2+(z-t)^2]`. An edge cannot serve two isolated deleted
vertices, since those would be adjacent deleted vertices. Thus these
errors sum to at most `3E`.

For each nonisolated run, the replacement and removed edges account for
the restricted tour exactly, including wrap after rotation to a survivor.
The run discrepancy is at most four times its length; the bad-vertex
count is at most twice the number of LL edges. The omitted first
variation is at most one per bad vertex because `0<p<1/2` there and
each defect has absolute value below one. Hence the combined bad-run
error is at most `10M_LL/n`. All deleted x,y obey
`s-x-y>53/75>1/2`, so `M_LL/n<=4E`, yielding `43E`.

The derivative `p'=-s/[4sqrt(x)(s-x)^(3/2)]` has absolute value below 11
on the entire grid interval. The primitive comparison has smooth error
`11d^2/2` and jump error at most d for a crossed threshold. Integrating
with the equal marginals and restoring the factor two gives
`|first variation|<=11E+2K`, hence the required `54E+2K` bound. This
argument uses the same outer measure separately at all three cutoffs;
it makes no claim about independent cutoff measures.

The uniform derivative/floor estimates were checked directly. The J_n
error is `(3/2+1+1+3/2)/n=5/n`; the D error is
`(7/2+2+2+2)/n=19/(2n)`. No sign of an uncontrolled floor error is used.

### Shared crossing, minimax and quantifiers

At a midpoint the strip is empty below half a grid spacing; otherwise
its normalized count is at most `2h+1/n<=4h`. For a pair crossing more
than one cutoff, the crossed indices form one consecutive block.
Summing adjacent width separations shows the sum of its crossed widths
is less than its endpoint distance d. Thus every such crossing is long,
and its entire weighted charge is at most `d^2`. One-crossing pairs
obey the same long bound; short crossings contribute at most `4h_i^3`.
Equality cases `d=h_i`, adjacent separation equality, a cutoff endpoint,
and a pair crossing all three thresholds leave no uncharged term.

Combining the deletion estimates spends this energy once and gives
`sum h_i W_i >= H(J_n+e)+F_n-(54H+2)E`.
The inequality `E<=8e` produces `L(h)=16+432H`, with no extra copies
of 16. The outer branch and inner weighted average give
`max W_i >= J_n+max(e,F_n/H-(L/H-1)e)`.
Its minimum for e>=0 is `max(F_n,0)/L(h)`: positive F_n uses the branch
intersection, while nonpositive F_n uses e=0. The positive-part map is
monotone and 1-Lipschitz, so all finite error inequalities have the right
direction even when a finite numerator changes sign.

The domain checks work uniformly: `n>=102` gives `a>1/6`, all three
cutoffs lie below `23/100<s/2`, and the stated finite gate supplies
nonempty deletions, at least three survivors and actual midpoint
separation. It is not enough to check macroscopic separation alone.

### Width optimum and finite floors

Expanding the cubic at `(a-x,x,b-x)` reproduces N and its derivative.
The derivative of the quotient numerator is
`G'=48(x-a-b)(16+432(a+b-x))<0` for every `0<=x<=a`.
The checker certifies the strict root signs and positive multipliers.
At the root, the stationary identity gives gradient
`(lambda_1,lambda_1+lambda_2,lambda_2)` for `F-rho*L`.
The cubic Taylor remainder is exactly
`-8 sum (h_i-u_i)^2(h_i+2u_i)`. Both constraint terms are nonpositive
on the full closed region. Since every u_i is positive, equality occurs
only at u, including boundary faces with a zero coordinate. If F<=0,
the positive-part quotient is zero and cannot tie. This proves global
uniqueness on the whole region, without assuming both constraints active.

For each *fixed* `0<t<1`, widths tu are strictly separated and obey the
finite corollary for all `n>=ceil(1/((1-t)a))`. The sufficient gate also
implies `n>=102` and nonempty deletion because `beta_1-q>a` and
`1/a>102`. The quantity B_n^(4) depends only on the cutoffs, not the
auxiliary widths. Taking liminf at fixed t and then the supremum as
t increases to one is therefore legitimate and yields the weak bound L.
No uniformity in a moving t or exchange with minimizing tours is claimed.

The unchanged optimal widths do fail both finite separations at every
`n=50000k+1`: the floors are exactly `(10455k,10907k,11500k)`.
This invalidates an eventual all-n gate at those unchanged widths,
but not the scaled-width argument. The exact scaling-loss identity,
its positive sign from uniqueness, and the upper bound
`eta_width-eta(tu)<(1-t)/2000000` were also checked. Strict-domain
supremum and closed-domain maximum remain distinct.

### Exact arithmetic review

The width checker was read in full. Its interval arithmetic rounds outwards;
all divisions have positive denominator gates; nonnegative powers are
used only where their inputs are nonnegative. Its decimal display expands
both endpoints and is not used as a hidden proof input.

The cosine/sine alternating sums have the correct lower/upper parity.
The root of `cos(t)-t` is unique by its negative derivative. The tangent
identity for Machin's pi formula is exact; its angle is in `(0,pi/2)`
since `atan(1/5)>=5/26`, `atan(1/239)<=1/239`, and the upper angle
is below `4/5<pi/2`. Thus the algebraic tangent value one selects pi/4.
The integrated square-root binomial coefficients are positive and
decreasing, with ratio `(2j-1)/(2j+2)`. Bounding the omitted integrand
by `c_81*v^162/(1-v^2)` gives the printed tail and correct enclosure
direction for D. The moving-q widening is justified by endpoint bound
two plus integrand-derivative bound two over length at most one.

The polynomial helper corroborates two exact identities, but is not
misrepresented as an automated proof of the KKT global inequality. The
analytic sign/constraint argument above is required. Two intentionally
false root intervals were rejected without changing the checker source.

## Commands freshly run and evidence classification

Environment: local Windows PowerShell, Python 3.14.3, mpmath 1.3.0,
SymPy 1.14.0. No network, hosted CI, production module or saved result
was used. The standard-library checkers were run with isolated Python
and site initialization disabled. Read commands used targeted headings
and linked ranges; the initial singular `knowledge/DEFINITION.md` lookup
failed because the actual canonical file is `knowledge/DEFINITIONS.md`,
which was subsequently read. A plain initial Git status encountered the
ownership guard; subsequent read-only Git used a command-local
a per-invocation `safe.directory` option, without
changing Git configuration.

| Exact verification command | Exit and material output | What it establishes / does not establish |
| --- | --- | --- |
| `python --version` | 0; `Python 3.14.3` | Local interpreter |
| `python -I -S ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | 0; all gates pass; `PASS fixed-cutoff width optimum; analytic proof supplies global quantifiers` | Exact rational parameter, integral, root, multiplier, coefficient and floor gates; formal polynomial identities. Analytic global proof remains necessary |
| `python -I -S ops/TASK-20260911__four_level_rational_witness/check_four_level.py` | 0; all gates pass; `PASS fixed four-level witness; universal quantifiers use the proved corollary` | Exact fixed witness and finite gates; comparison with old value is not needed by L |
| `python -I -S ops/TASK-20260911__finite_shared_crossing/check_finite_crossing.py` | 0; 48 prescribed measures, 16 tour/cutoff cases, exact unseparated excess `1/1250`, all negative controls pass | Bounded exact corroboration of one shared energy, marginals, wrap, parity, signs and floors; not arbitrary-tour enumeration |
| `python -I -S ops/TASK-20260911__three_level_common_chain/check_three_level.py` | 0; 12 prescribed grid couplings and all gates pass; `PASS all three-level checks; analytic proof supplies all-order quantifiers` | Additional dependency corroboration, not a needed premise for the new scalar optimum |
| `python ops/TASK-20260910__deletion_exponent_sharpness/check_sharpness.py` | 0; 12 exact floors, 60 tours, 180 orientations, 360 strip checks, 8 symbolic identities, 60 direct-cost cases at each of 70/100 dps all pass | Exact combinatorial identities, symbolic local identities and separately classified numerical diagnostics for the signed-deletion dependency; no finite optimum or universal proof by sampling |
| `python -I -S -O ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py` | Expected 1; `RuntimeError: This checker requires enabled assertions; omit -O.` | Fails closed if assertions are disabled; intentional negative test |
| Fresh direct-cost diagnostic below, piped to `python -` | 0; `PASS 120 fresh direct-cost diagnostics at all three current cutoffs, 80 dps; exact q floors and integer E/K; no production or prior checker imports` | Independent bounded falsification attempt at all current cutoffs; numerical evidence only for radical inequalities |
| Root/import control below, piped to `python -I -S -` | 0; `PASS two false root intervals rejected; standalone imports fractions, math only` | Negative sign controls and import separation; does not replace source review |

The width checker additionally reproduced these exact outward enclosures:

```text
0.00035105290142936543670 < lambda_1 < 0.00035105290142936940356
0.00059414888796317986218 < lambda_2 < 0.00059414888796318518264
0.00000038803240421408705 < eta_width < 0.00000038803240421408841
0.00000000017917433572119 < eta_width-eta_4 < 0.00000000017917433572254
0.14056946887766098063257 < C_term+eta_width < 0.14056946887766098063392
```

The source-only SHA256 values at audit time were:

```text
research/THREE_LEVEL_COMMON_CHAIN.md
d0035afdd6f2b7f004159928f8babe9830dce073198f63b2b9a9419e2be3723c
research/COMMON_CHAIN_QUANTITATIVE_STABILITY.md
97ef6456c646db0d9c1c2b43fecc041561408d573485b8c61bf23e951fdfe4e0
research/INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md
42f2fc55d8d7740ab9bf1c14e4f2191339c647db147aecc1ac9907a48d645360
ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py
048261ae2e552cf99311eee4202ea407c3cae1ff1a500774a0d64fb5d351e16f
```

Final file checks: the entire new audit was inspected, an explicit Python
whitespace check passed, and both Python blocks extracted from the written
Markdown reran successfully (exit 0). All four source hashes above were
compared again and remained unchanged (exit 0). The ordinary path-scoped
`git diff --check` also exited 0, but it omits this untracked addition;
the explicit whitespace check is the applicable new-file evidence.

## Reproducible fresh controls

Run each Python block from the repository root by piping a PowerShell
single-quoted here-string to the interpreter specified above. No local
file other than this audit is created.

```python
from fractions import Fraction as F
from itertools import chain
import mpmath as mp
mp.mp.dps=80
qlo=F('0.1950200913506069300798071259134151019366')
qhi=F('0.1950200913506069300798071259134151019367')
betas=(F(2091,10000),F(10907,50000),F(23,100))
cases=0
for n in (102,103,104,105,106,107,1000,1001,2048,2049):
    k=(qlo*n).__floor__()
    assert k==(qhi*n).__floor__()
    ordered=list(range(k,n+1))
    alternate=list(chain.from_iterable(zip(
        ordered[:len(ordered)//2],ordered[::-1][:len(ordered)//2])))
    if len(ordered)%2: alternate.append(ordered[len(ordered)//2])
    walks=(ordered, alternate, ordered[::2]+ordered[1::2],
           alternate[len(alternate)//3:]+alternate[:len(alternate)//3])
    nn=mp.mpf(n)
    def edges(w): return zip(w,w[1:]+w[:1])
    def cost(w): return mp.fsum(mp.sqrt(u*v) for u,v in edges(w))/nn**2
    ref=mp.fsum(mp.sqrt(i*(n+k-i)) for i in ordered)/nn**2
    for w in walks:
        assert sorted(w)==ordered
        e=cost(w)-ref
        es=sum((u+v-n-k)**2 for u,v in edges(w))
        energy=mp.mpf(es)/nn**3
        assert 0<e and energy<=8*e+mp.mpf('1e-70')
        for beta in betas:
            ell=(beta*n).__floor__()
            assert F(ell,n)>qhi and n-ell>=2
            w1=[i for i in w if i>=ell]
            ideal=mp.fsum(n+k-i-2*mp.sqrt(i*(n+k-i))
                         for i in range(k,ell))/nn**2
            delta=cost(w1)-cost(w)-ideal
            oriented=[(u,n+k-v) for u,v in edges(w)]
            oriented += [(v,n+k-u) for u,v in edges(w)]
            kr=sum(abs(x-z) for x,z in oriented if (x<ell)!=(z<ell))
            cross=mp.mpf(kr)/(2*nn**2)
            assert abs(delta)<=54*energy+2*cross+mp.mpf('1e-70')
            cases+=1
assert cases==120
print('PASS 120 fresh direct-cost diagnostics at all three current cutoffs, '
      '80 dps; exact q floors and integer E/K; '
      'no production or prior checker imports')
```

```python
import ast, runpy
from fractions import Fraction as F
from pathlib import Path
path=Path('ops/TASK-20260911__four_level_width_optimum/check_width_optimum.py')
ns=runpy.run_path(str(path))
ds=tuple(ns['deletion'](b) for b in ns['BETA'])
for lo,hi in [('0.00451','0.004515'),('0.004525','0.00453')]:
    left=ns['stationary'](ns['point'](F(lo)),ds)
    right=ns['stationary'](ns['point'](F(hi)),ds)
    assert not (left[0]>0 and right[1]<0)
imports=sorted(n.module for n in ast.walk(ast.parse(path.read_text()))
               if isinstance(n,ast.ImportFrom))
assert imports==['fractions','math']
print('PASS two false root intervals rejected; '
      'standalone imports fractions, math only')
```

## Residual obligations

No unresolved mathematical dependency was found in the minimal lower-endpoint
path above. External review remains outstanding and must assess the analytic
proof as well as the exact arithmetic; an internal subagent review cannot
mark the external registry accepted. If the final paper presents obsolete
or independent results excluded above, they need their own audit rather
than inheriting this conclusion. In particular a method-ceiling statement
from Section 13 would require a separate review. This audit proves neither
that L is the true normalized constant nor that the lower/upper gap closes.
