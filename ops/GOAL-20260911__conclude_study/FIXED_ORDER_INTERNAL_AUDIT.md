# Internal dependency audit of Supnick fixed-order full feasibility

Date: 2026-09-11. Mode: STRICT. Review type: separate internal adversarial
subagent audit for the final publication candidate, not external acceptance.
The parent goal continued authorized work concurrently. Its HEAD advanced
from `372f96c0a9f14d968e7ecb3b1a039e7867340005` to
`13ddb41180b3911940f4fe5cf7d61c0545f9f834` during this review; the four
principal proof/publication sources below have no diff against the latter
HEAD. This audit changes only this file.

## Result and sufficient final-paper formulation

**INTERNALLY VALIDATED:** the complete fixed-order classification, using
the minimal proof dependencies audited below. No gap or counterexample
was found. The following formulation is supported for the final paper.

For integers `k>=1` and `n>=k+2`, let `sigma*_(k,n)` be the canonical
Supnick cycle on `{k,...,n}`, with every radius retained and every circle
externally tangent to the central circle. Write `R_(k,n)` for this cycle's
unique chain-closure radius and

```text
Delta_(k,n) = theta_R(n,k)+theta_R(k,n-1)-theta_R(n,n-1),
R=R_(k,n).
```

The cumulative-angle placement at this radius satisfies all pairwise
non-overlap constraints **if and only if** `Delta_(k,n)>=0`. Equivalently,
some full feasible placement in that same cyclic order exists at this
radius if and only if that inequality holds. The integer classification is:

| k | Feasible at the chain radius | Infeasible at the chain radius in this fixed order |
| --- | --- | --- |
| 1 | `3<=n<=7` | `n>=8` |
| 2 | `4<=n<=12` | `n>=13` |
| 3 | `5<=n<=16` | `n>=17` |
| 4 | `6<=n<=20` | `n>=21` |
| 5 | `7<=n<=24` | `n>=25` |
| Every `k>=6` | `k+2<=n<=4k+5` | `n>=4k+6` |

The seam signs are strict, so no integer equality case occurs. In the
feasible column `R_full(sigma*)=R_chain(sigma*)`. If the manuscript
mentions slack, the correct statement is: for at least four outer circles,
the minimum slack over nonadjacent **directed paths** is exactly Delta,
attained only by the two-edge seam up to reversal. Adjacent one-edge paths
instead have zero slack. The theorem makes no floating-circle assertion,
does not classify the larger optimal radius in the infeasible column,
and does not determine the global problem on `{1,...,n}` after deleting
the radii below k.

The published chain theorem may be retained with its original generality:
for arbitrary strictly increasing positive radii, **one** canonical
Supnick tour minimizes the fixed-R angular sum for every R, hence also
minimizes the chain root. Its root is a lower bound for the full problem
on those same radii; equality follows when that tour is fully feasible.
Do not infer uniqueness of the minimizing tour merely from the strict
anti-Monge inequalities, or confuse that conditional equality with a
feasibility theorem after the seam obstruction.

## Minimal dependency graph and review coverage

The owning ledger is `knowledge/FIXED_ORDER_THEORY.md`, entries
"Anti-Monge/Supnick chain order", "General fixed-radius Supnick seam
persistence", "Exact sequence monotonicity and complete formal seam
onsets", and "Complete exact Supnick fixed-order feasibility
classification". The general construction and all-pairs proof were
audited independently of their later seam-sign imports.

| Final claim | Source and precise scope read | Dependencies actually needed | Internal check and remaining scope |
| --- | --- | --- | --- |
| Angular and chain theorem | `paper_assets/ringmin_paper.tex`, model and Supnick theorem; `research/FIXED_K_SUPNICK_SEAM.md` Sections 1-2 | Elementary kernel calculus; classical Supnick maximum-tour theorem applied to negative angular cost | Kernel and root-transfer arguments rederived; imported theorem's hypotheses/orientation checked against the cited published survey |
| Exact cycle and seam neighbors | Fixed-k note Section 1, both parity formulas | Explicit rank arms, shift by k-1 | Rank partition and every edge family checked analytically; independent bounded counters include central and closing edges |
| All-pairs feasibility iff Delta>=0 | `research/SUPNICK_FULL_FEASIBILITY.md` Sections 1-5 in full | Positive first/mixed derivatives; minimum triangle defect; path fan; chain closure | Complete analytic rederivation; exact symbolic/index checker and separate numerical falsification checker rerun |
| General persistence and physical threshold | `research/FIXED_K_SUPNICK_SEAM.md` Sections 2-5 | Chain minimality, deletion of maximum radius, bounded Descartes pocket or equivalent angular tangency identity | Domains, unsquared signs, discarded algebraic root, monotonicity and limits rederived |
| Unified signs for every k>=6 | `research/SUPNICK_SEAM_SEQUENCES.md` Sections 1-6 in full | Exact rationalization from `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` Section 5, only equations (20)-(25); k=6 endpoint bridge | Analytic estimates rederived; all ten exact polynomial certificates and separate symbolic derivatives rerun |
| Initial bridges k=1,...,6 | Endpoint statements from `RADIUS1_SEAM_OBSTRUCTION.md`, `RADIUS2_SEAM_THRESHOLD.md`, `RADIUS3_SEAM_ONSET.md`, `RADIUS4_SEAM_ONSET.md`, `RADIUS5_SEAM_ONSET.md`, `RADIUS6_SEAM_ONSET.md` | Twelve specific rational-radius comparisons | Linked exact checks rerun; all twelve bridges also newly certified by a separate generic rational sqrt/atan implementation reproduced below |
| Complete table and no equality | Full-feasibility note Section 6 | Iff criterion, general persistence, unified k>=6 signs and six finite initial bridges | All prerequisites above suffice; no finite scan proves the infinite table |

This path does not depend on the older uniform onset window, effective
cutoff `4325`, asymptotic threshold estimates, or separate k=7,...,10
proofs. Those were not audited as independent claims. Nor was the
published worst-tour geometric claim audited. The separately constructed
finite endpoint certificates below avoid treating historical radius-by-
radius notes as unexplained proof assumptions: only their listed endpoint
data are used and are independently checked.

## Analytic adversarial review

### Published chain theorem and the classical import

Differentiating `theta_R(a,b)=2asin sqrt(ab/((R+a)(R+b)))` gives

```text
theta_1 = sqrt(R*b/a)/((R+a)*sqrt(R+a+b)),
theta_12 = sqrt(R)/(2sqrt(ab)*(R+a+b)^(3/2)).
```

Both are positive on the complete positive domain. Integrating the mixed
derivative over a rectangle proves strict anti-Monge. Consequently
`-theta_R` is symmetric Monge, and hence Supnick. Applying the classical
**maximum**-tour result to that matrix minimizes the original angular
sum. The tour depends on ranks rather than R. If nonnegative costs are
desired, adding a constant to every entry preserves both Monge
inequalities and all tour comparisons.

A bounded literature check inspected the publisher's version of the
repository's cited survey: Burkard, Deineko, van Dal, van der Veen and
Woeginger, *Well-solvable special cases of the Traveling Salesman Problem:
a survey*, SIAM Review 40(3), 496-546 (1998). Its Section 2.3, printed
p. 507, states the maximum Supnick tour used here; Proposition 2.13 on
p. 508 gives symmetric Monge implies Supnick. Theorem 2.5 on p. 502 is
the different minimum-tour statement. Thus the manuscript's sign
convention is correct. This verifies an imported classical theorem and
its applicability, rather than claiming to reprove Supnick's original
1957 theorem. Source: [published survey PDF](https://pure.tue.nl/ws/portalfiles/portal/2373438/Metis148543.pdf),
[DOI](https://doi.org/10.1137/S0036144596297514).

Every edge angle decreases continuously from pi to zero as R increases
from zero to infinity, so a cycle of at least three edges has a unique
positive closure root. At an arbitrary competing tour's root, the
canonical tour has angular sum at most `2pi`. Strict decrease therefore
places the canonical root at or below the competing root. The argument
has the claimed direction and does not require a feasible placement.

### Exact rank construction and triangle minimum

The two low-rank arms partition the ranks through `ceil(N/2)` by parity;
their high partners partition the remaining ranks below N. Appending N
therefore forms a cycle with all radii used once. For N>=4 the first edge
is `(k,n-1)` and the final closing edge is `(n,k)`; N=3 has the same
seam neighbors directly. The two parity edge formulas contain exactly N
edges. For even N the one extra middle edge has consecutive endpoints;
replacing it by an averaged pair of diagonal terms would be an error.

For distinct radii a,b,c, order the endpoints as a<c. Lowering the middle
radius b to k strictly lowers the triangle defect unless b=k. For
`H(x,z)=theta(x,k)+theta(k,z)-theta(x,z)`, the two derivatives are
nonpositive by positive mixed derivative, with the strictness given in
the source. Increasing endpoints to `(n-1,n)` thus lowers H. The two
nonnegative rectangle-integral remainders are strict unless both endpoints
already have those values. This proves that the unique minimizing triple
is middle k, endpoints n-1 and n, including cases in which a=k during
the intermediate comparison; the analytic diagonal value is legitimate
there and is not asserted to be a self-pair constraint.

The fan telescoping identity has exactly m-1 triangle terms for a simple
m-edge path, all with three distinct vertices. It gives
`path slack >= (m-1)delta_R` for every R>0, with no sign assumption. At
Delta=0 an m>=3 fan has at least two different middle vertices, so at
least one term is strict. This supplies the stated equality cases.

### Both arcs, forced gaps and small cycles

At the chain root, the two cyclic path sums for any endpoints add to
`2pi`. Applying the fan bound to both independently proves that each is
at least its required pair angle when Delta>=0. Thus the smaller angular
separation is sufficient, regardless of which path is shorter. Adjacent
complements have exact slack `2pi-2theta>0`; the one-edge direction is
tight. Converting these inequalities by the elementary center-distance
identity gives full Cartesian non-overlap.

Conversely any feasible placement in that fixed order at the chain root
has positive directed gaps `g_i>=theta_i` and
`sum(g_i-theta_i)=0`. Every adjacent gap is therefore forced tight,
including closure. A negative Delta makes the two-edge seam too short;
the complementary path simultaneously violates the upper angular bound.
There is no freedom to repair the seam at this radius.

For N=3 all pairs are adjacent, the seam is a two-edge complement with
positive slack, and there is no nonadjacent slack minimum. For N=4 the
two nonadjacent pairs have four two-edge paths; only the seam realizes
the minimum triangle defect. The weak Delta=0 feasibility argument is
valid before the separate integer sign theorem excludes equality.

### Fixed-k persistence and threshold branches

Deleting the maximum radius n+1 from a minimizing fixed-R tour strictly
reduces cost: already `theta(a,n+1)>theta(a,b)` for its neighbors a,b.
The resulting tour has cost at least the minimum on the smaller set.
Hence the minimal angular sum and its implicit root strictly increase
with n. This does not assume deletion preserves the canonical tour.

For curvature x=1/R, the bounded pocket curvature is
`P_n(x)=x+alpha+2sqrt(alpha*x+beta)`,
`alpha=1/n+1/(n-1)`, `beta=1/(n(n-1))`. The plus branch is the bounded
interstice of three externally tangent circles; its tangent inserted
radius is the unique angular-defect zero because both adjacent angles
strictly increase with the inserted radius. Thus the defect sign is
`sign(P_n(1/R)-1/k)`. The external Descartes formula is used only in
this standard three-circle setting, with positive curvatures and the
bounded branch specified.

At x=0, `P_n(0)=(1/sqrt(n)+1/sqrt(n-1))^2`, strictly above 1/k at
n=4k and strictly below it at n=4k+1. The unique positive threshold
therefore exists exactly for n>=4k+1. Solving its unsquared equation
gives the displayed minus root kappa. The positive quantity
`q=sqrt(alpha/k+beta)>alpha` fixes the square-root sign; the other
algebraic root violates `1/k-alpha-x>=0`. Rationalizing shows kappa
is positive on exactly the physical threshold domain. Consequently
`sign(Delta)=-sign(R_chain-T)` there; before it Delta is strictly positive.

At fixed x, P_n decreases with n, so kappa increases and T decreases.
The chain root increases, making `R_chain-T` strictly increasing. The
root diverges by `R_chain>=k(csc(pi/N)-1)` while T tends to k. These
facts prove persistence and eventual strict obstruction, but do not by
themselves specify the onset. The following two ingredients do.

### Unified k>=6 onset proof

The complete sequence proof was read and rederived. The principal gates
are as follows; all intervals and derivative inequalities include k=6.

1. The exact symmetrized square-root edge sum is the midpoint sum of
   the averages `g_x(-1/2),g_x(1/2)`, plus the seam weight, and minus
   `(L-sqrt(L^2-1))/2` in the even case. Counting the diagonal terms
   confirms the sign and size of this correction when k changes parity.
2. Midpoint concavity gives error at most `3/16`. The second derivative
   of g gives error below `1/4`; the even correction is below `1/60`.
   Thus `F-4/15<S<F+3/16`, with the correct strict directions.
3. From the actual asin closure, `R>S/pi-L/2-1/2`. For the upper
   comparison, the positive coefficient polynomial in Section 3 gives
   `12S/pi+9>(L-1)^2` and positivity of the trial radius
   `R_0=S/pi+2-L/2`. The atan closure at R_0 is strictly below `2pi`,
   so `R<R_0`. This is an actual-root comparison, not an approximation
   at a presumed asymptotic scale.
4. Combining these bounds places `D_c(k)-V_c(k)` in one common interval
   of width `5/2+109/(240pi)<8/3`, independent of parity.
5. The threshold rationalization uses only the exact conjugate identity
   `U^2-4Z=tH`, with all radicals and denominators positive, for `t=1/k`.
   Differentiation gives the source numerator with one radical. Its
   coefficient and both pre-square sides are positive. The two squared
   margin signs therefore really imply the upper/lower derivative bounds;
   squaring has not silently discarded a branch.
6. The coefficient transformation
   `(1+y)^m p(y/[6(1+y)])` has exactly the printed coefficients.
   Their positivity proves every required polynomial sign on the entire
   open interval, while the leading coefficient explicitly covers
   t=1/6. The zero constant of each squared margin excludes t=0 only,
   which is not an actual finite k. All ten certificates were independently
   regenerated by standard-library and SymPy implementations.
7. Leibniz differentiation of F and the signed remainder estimates for
   A_0 and B_0 give the uniform remainder below `3/320`. Rational atan
   sums certify the pi and coefficient enclosures. The resulting affine
   upper bound for `V_5'` has negative slope and value
   `-205349/72000<-8/3` at 6; the lower bound for `V_6'` has positive
   slope and value `1398247/363000>8/3` there.
8. Integrating over a unit step overcomes the entire common error width,
   so `D_5(k+1)<D_5(k)` and `D_6(k+1)>D_6(k)` for all integer k>=6.
   The exact k=6 bridge then fixes their opposite signs for the entire
   family. Fixed-k persistence extends the conclusion to every n.

No differentiable interpolation of a parity-dependent chain root, finite
scan over k, or effective asymptotic cutoff was used.

### Exact initial bridges independently reconstructed

The only finite bridges required are:

| k | Strict positive-seam-side bridge | Strict negative-seam-side bridge |
| --- | --- | --- |
| 1 | `R_(1,7)<6<T_(1,7)` | `T_(1,8)<51/10<R_(1,8)` |
| 2 | `R_(2,12)<17<T_(2,12)` | `T_(2,13)<14<R_(2,13)` |
| 3 | `R_(3,16)<32<T_(3,16)` | `T_(3,17)<32<R_(3,17)` |
| 4 | `R_(4,20)<50<T_(4,20)` | `T_(4,21)<50<R_(4,21)` |
| 5 | `R_(5,24)<75<T_(5,24)` | `T_(5,25)<75<R_(5,25)` |
| 6 | `R_(6,29)<211/2<T_(6,29)` | `T_(6,30)<211/2<R_(6,30)` |

All linked exact bridge functions/checkers passed. In addition, the fresh
script below proves all twelve rows using **different enclosures**:
integer-square-root rational intervals, then alternating atan sums for
the half-angle form `atan sqrt(ab/(R(R+a+b)))`. It reconstructs the
cycle and evaluates every actual edge, including closure. It tests the
threshold using P_n directly, avoiding cancellation in kappa. No source
table of angular/radical bounds is copied or imported.

For a nonnegative rational q, `isqrt(floor(q*M^2))/M` is a lower bound
for sqrt(q), with upper bound larger by 1/M. The explicit squared check
certifies that interval. Alternating atan partial sums of 32 and 33 terms
give lower and upper bounds for arguments in (0,1); monotonicity permits
using the opposite radical endpoints. Every argument is checked in that
domain. Machin's identity uses the same unambiguous branch justified
above. Thus this is exact rational finite evidence, not floating-point
agreement. The smallest printed pocket-sign margin is still positive
(`6614173/500000000000` for k=5,n=25).

## Fresh commands and results

Environment: local Windows PowerShell; Python 3.14.3, SymPy 1.14.0,
mpmath 1.3.0. No packages were installed. There is no hosted CI or external
acceptance claim. Scripts import neither production Ringmin code nor
global certificates. Read-only web access was confined to the cited
classical theorem; no repository or external publication action occurred.

| Exact command | Exit and material result | Evidence classification and limitations |
| --- | --- | --- |
| `python -I ops/TASK-20260904__supnick_feasibility_classification/check_exact.py` | 0; 9 identities, N=3/N=4, rational N=3 root `6/23`; 32 cycles/276 edges; 1482 pairs/2964 directed paths; 82 rejection gates PASS | Exact symbolic and finite indexing checks; analytic proof supplies all-k/all-n quantifiers |
| `python -I ops/TASK-20260904__supnick_feasibility_classification/diagnose.py` | 0; `cases=106 feasible=82 infeasible=24 triangles=445470 directed_paths=29608`; no counterexample | Separate acos/Cartesian numerical falsification only, 80 dps and guard `1e-55`; not interval root certification |
| `python -I -S ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py` | 0; all ten positive-polynomial gates and endpoints PASS; margins `13349/72000`, `430247/363000`; 6 negative controls PASS | Exact finite algebraic certificates for continuum parameter domain, no numerical roots or k scan |
| `python -I ops/TASK-20260904__seam_sequence_monotonicity/check_symbolic.py` | 0; both threshold derivatives/conjugates/five gates and F,A,B,w,g derivatives PASS | Separate symbolic differentiation and coefficient implementation |
| `python -I -O ops/TASK-20260904__supnick_feasibility_classification/check_exact.py` | 0; same identities, counts and 82 rejection gates PASS | Existing explicit guards remain active with optimized Python |
| `python -I -S -O ops/TASK-20260904__seam_sequence_monotonicity/check_exact.py` | 0; same ten polynomial certificates and 6 rejection controls PASS | Existing explicit guards remain active with optimized Python |
| k=1,2 runpy invocation below, piped to `python -I -` | 0; exact bridge/order checks pass through n=8 and n=13 | Calls only existing exact finite functions; avoids their unrelated diagnostic scans |
| `python -I -S ops/TASK-20260804__radius3_seam_onset/check_seam.py --order-stop 17` | 0; 383 gates; threshold/chain bridges at R=32 PASS | Exact finite bridge, bounded construction cross-check |
| `python -I -S ops/TASK-20260804__radius4_seam_onset/check_seam.py --order-stop 21` | 0; 1278 gates; threshold/chain bridges at R=50 PASS | Same scope |
| `python -I -S ops/TASK-20260804__radius5_seam_onset/check_seam.py --order-stop 25` | 0; 1683 gates; threshold/chain bridges at R=75 PASS | Same scope |
| `python -I -S ops/TASK-20260805__radius6_seam_onset/check_seam.py --order-stop 30` | 0; 2312 gates; threshold/chain bridges at R=211/2 PASS | Required seed for the infinite sequence proof |
| Fresh generic bridge script below, piped to `python -I -S -` | 0; `PASS 12 fresh exact endpoint bridges; rational sqrt/atan enclosures; no checker or production imports` | Independent exact finite endpoint enclosure, not an enumeration argument for the infinite theorem |

The exact code for the targeted historical function calls is:

```python
import runpy
for directory,stop in [('radius1_seam_obstruction',8),
                       ('radius2_seam_threshold',13)]:
    ns=runpy.run_path('ops/TASK-20260804__'+directory+'/check_seam.py')
    ns['check_order_convention'](stop)
    ns['check_exact_bridges']()
    print('PASS exact imported bridge and order checks:',directory,'through',stop)
```

## Reproducible independent finite bridge certificate

The following block was freshly executed locally and is sufficient to
reproduce all twelve endpoint inequalities. Each printed `chain_side=-1`
means `R_chain<R_trial<T`; `chain_side=+1` means
`T<R_trial<R_chain`. The displayed margins are rational lower bounds
rounded down, while the assertions use unrounded exact rationals.

```python
from fractions import Fraction as F
from math import isqrt
scale=10**20

def root(q):
    lo=F(isqrt(q.numerator*scale*scale//q.denominator),scale)
    hi=lo+F(1,scale)
    assert lo*lo<=q<hi*hi
    return lo,hi

def atan_sum(x,count):
    assert 0<x<1
    return sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                for j in range(count)),F(0))

pi_lo=16*atan_sum(F(1,5),32)-4*atan_sum(F(1,239),33)
pi_hi=16*atan_sum(F(1,5),33)-4*atan_sum(F(1,239),32)
assert 3<pi_lo<pi_hi<F(22,7)
fixtures=((1,7,F(6),-1),(1,8,F(51,10),1),
          (2,12,F(17),-1),(2,13,F(14),1),
          (3,16,F(32),-1),(3,17,F(32),1),
          (4,20,F(50),-1),(4,21,F(50),1),
          (5,24,F(75),-1),(5,25,F(75),1),
          (6,29,F(211,2),-1),(6,30,F(211,2),1))
for k,n,r,sign in fixtures:
    size=n-k+1
    half=(size+1)//2
    arms=[]
    for parity in (1,2):
        arm=[]
        for low in range(parity,half+1,2):
            arm.append(k+low-1)
            high=size-low
            if high>half: arm.append(k+high-1)
        arms.append(arm)
    tour=arms[0]+arms[1][::-1]+[n]
    assert sorted(tour)==list(range(k,n+1))
    assert {tour[1],tour[-1]}=={n-1,n}
    low=high=F(0)
    for a,b in zip(tour,tour[1:]+tour[:1]):
        s0,s1=root(F(a*b)/(r*(r+a+b)))
        low+=atan_sum(s0,32)
        high+=atan_sum(s1,33)
    alpha=F(1,n)+F(1,n-1)
    beta=F(1,n*(n-1))
    p0,p1=root(alpha/r+beta)
    pocket_lo=1/r+alpha+2*p0-F(1,k)
    pocket_hi=1/r+alpha+2*p1-F(1,k)
    closure_margin=low-pi_hi if sign>0 else pi_lo-high
    threshold_margin=-pocket_hi if sign>0 else pocket_lo
    assert closure_margin>0 and threshold_margin>0
    assert low<high
    print('PASS k=%d n=%d R=%s chain_side=%+d '
          'closure_margin>=%s threshold_margin>=%s' % (
              k,n,r,sign,
              F((closure_margin*10**12).__floor__(),10**12),
              F((threshold_margin*10**12).__floor__(),10**12)))
print('PASS 12 fresh exact endpoint bridges; rational sqrt/atan enclosures; '
      'no checker or production imports')
```

This diagnostic uses Python assertions: run without `-O`. It is an embedded
review certificate with its analytic enclosure justification above, not a
replacement production verifier.

The full written audit was reviewed. An explicit whitespace check passed,
and both embedded Python blocks were extracted from this written Markdown
and rerun successfully with the stated interpreters (exit 0). This checks
the actual untracked addition rather than relying on ordinary `git diff`,
which omits it. The principal source notes and historical TeX had an empty
path-scoped diff against the observed checkpoint HEAD.

## Residual review obligations and protected scope

No unresolved premise was found for the stated fixed-order table along
the audited path. Classical Supnick and the standard bounded Descartes
pocket formula remain explicitly named imported theorems with their
hypotheses checked, rather than being called novel self-contained proofs.
External independent review of the repository theorem remains outstanding.

No global finite verifier, certificate, upper construction, asymptotic
theorem, floating quantifier, or historical worst-arrangement claim was
certified by this review. The original v1 manuscript was inspected only
for model/theorem/citation scope and was not changed. No changes were made
to `AGENTS.md`, the external review protocol/state, production code,
results or publication assets. This file supplies a precise review scope
for the final paper; it does not promote the whole historical corpus to
an audited status.
