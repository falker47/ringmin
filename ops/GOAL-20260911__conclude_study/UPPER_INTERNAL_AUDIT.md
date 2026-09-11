# Internal dependency audit of the exact four-block upper endpoint

    classification=internal adversarial mathematical validation
    reviewed_on=2026-09-11
    scope=x_*; alpha_hat; epsilon_b; Delta_*; exact definition of U_4
    outcome=INTERNALLY_VALIDATED
    external_acceptance=not performed or implied
    environment=Windows; CPython 3.14.3; stdlib exact-checker modes

The fresh reviewer subagent re-derived the retained parameter claims from
their literal max-integrals and inspected the linked exact checkers. No
error or unpaid mathematical dependency was found in this parameter chain.
The review does not externally accept the work, certify a finite optimum,
or endorse every historical claim printed by a broader legacy checker.

The preceding
[fourth-block and general-transfer review](../TASK-20260911__general_block_transfer/INTERNAL_REVIEW.md)
already covers the fourth increment, its rational saving, arbitrary finite
and countable block recovery, and full geometry. This audit pays its stated
remaining debt concerning existence, uniqueness and localization of the
four implicit input parameters.

## 1. Minimal retained dependency graph

```text
Literal normalized E and its block/diagonal switches
  -> unique x_* on [0,1], rational bracket, e=E(x_*)
Literal shifted diagonal K on alpha in [0,1/2]
  -> D=K', including the wrap jump, and K''
(e,D) -> unique alpha_hat, rational bracket
A=1+alpha_hat; lambda=A*x_*
Generic independent-block max increment at start u=lambda
  -> unique epsilon_b, rational bracket and entry-distance bound
v=lambda+epsilon_b
Same generic increment at start u=v
  -> unique Delta_*, rational bracket
w=v+Delta_*; eta=1/20000
  -> exact four-slab probability measure and its literal integral U_4
Fourth-block saving + general-block full transfer (previous audit)
  -> global upper endpoint U_4 with the stated strict improvement
```

The historical shift optimizer `alpha_*` is different from `alpha_hat`.
Its optimization and coefficient comparisons are not required by this
graph: the normalized function E is defined directly and is independent of
alpha. Similarly, old one-, two- and three-block finite transfer proofs are
not required once the new general-block transfer has been established.
The joint-prefix and start-domain optimization corollaries are not needed
to define or recover the explicit four-block endpoint.

## 2. Normalized minimizer x_*

**Source audited:**
[`PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md`](../../research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md),
Sections 2-7, for E, its unique minimum and its bracket. Historical fixed
alpha optimization and old transfer consequences are outside this retained
claim scope.

The reviewer re-derived the following checks:

- The ratio `sqrt(u/(1+u))+sqrt(u/(1+x-u))` is strictly increasing in u.
  Its endpoint gives exactly one block-entry width `tau` in `(1/4,1/3)`.
  The independent removed-diagonal switch is `u=1/3`.
- The unsquared interior switch has the stated positive derivative. Its
  expression through `r=sqrt(z/(1+z))` is algebraically identical to the
  implicit derivative, with positive denominators.
- The derivative Phi retains both the endpoint and the interior chain
  integral. Cost equality cancels the moving switch term in the first
  derivative, but the second derivative retains the positive Q term.
- The all-chord derivative is negative. On `(tau,1/3)`,
  `Phi'>41/72`; the exact `z(1/3)>2/7` gate implies `Phi(1/3)>0`.
  Thus exactly one zero lies in this interval.
- On `(1/3,1)`, the bounds `Q<1/21` and `M>1/20` give
  `Phi'<-1/420`. The factorization of M and both cases at
  `sqrt(1+x)=4/3` were checked, including the rational square signs.
- The exact gate `E(1)>3/250`, strict concavity of the final segment,
  and strict middle-regime increase after the first zero exclude a second
  global minimum. Thus the claimed x_* is the unique global minimizer on
  the auxiliary `[0,1]`, without using a wrap-crossing construction.
- The two exact derivative gates locate it at
  `719/2500 < x_* < 2877/10000` and explicitly verify the mixed regime.

The interval checker was inspected for outward arithmetic, sign-safe
division, square roots, 100-step unsquared switch isolation, and the
64-term atan/log remainders. The circular and hyperbolic primitives were
differentiated independently. The signs at both max switches and the
principal inverse-trigonometric branches are correct. Its exact interval
arithmetic oracle and invalid-domain controls passed during the run.

## 3. Exact alpha_hat and the coefficient normalization

**Sources audited:**
[`PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md`](../../research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md),
Sections 1-4; and
[`SHIFTED_ALTERNATING_HALVES.md`](../../research/SHIFTED_ALTERNATING_HALVES.md),
the `[0,1/2]` formulas in Sections 5-6.

Splitting the literal shifted diagonal integral at `a=(1+alpha)/3` and
`b=1-alpha` re-derives K and D. In particular the moving wrap contributes
`-(sqrt(2)-1)*sqrt(b)` to D. Differentiating again gives the stated K'';
the constant `1/12` includes the moving diagonal-switch contribution.
The endpoint regimes `alpha=0,1/2` cause zero-length integrals, not omitted
positive-mass branches.

The analytic two-sided bound `-1/324<e<-1/1728` is valid. Together with
`K''>7/60`, it gives
`F''=K''+e>46/405>1/9`, where
`F=K+(1+alpha)^2*e/2`. The elementary endpoint signs of F' are negative
at zero and positive at one half. Hence alpha_hat is uniquely defined on
this whole interval before the numerical localization is used.

The rational midpoint `x0=5753/20000`, the independently re-derived bound
`0<E''<3` throughout the relevant mixed interval, and stationarity give
`E(x0)-3/800000000<e<=E(x0)`. The checker encloses E(x0) using concave
trapezoid/midpoint bounds on separate chord and chain intervals, with an
explicit enclosure of the omitted switch interval. This is a different
integration method from the lambda checker's exact primitives. Its D
quadratures retain the negative wrap product in the correct direction.
The resulting opposite F' signs prove
`1093/10000<alpha_hat<10931/100000`.

The literal reflected-prefix measure was checked against the definition
in the joint-prefix source, Section 3. Symmetry and scaling give exactly
`integral g dmu_prefix = 2*K(alpha)+(1+alpha)^2*E(x)`. Thus the coefficient
normalization is `1/(4*pi)`, and both the integrand and the change of
variable supply a factor `1+alpha` in the prefix increment.

The historical comparisons to `C_107` or its decimal enclosure are not
required for U_4's definition or transfer. They were not substituted for
the literal integral when closing this dependency.

## 4. The second and third mixed stationary widths

**Sources audited:**
[`PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md`](../../research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md),
the parameter-existence and localization claims of Sections 1-4 and 6;
[`PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md`](../../research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md),
Sections 1-5; and the literal measure/max definitions in
[`PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md`](../../research/PERMUTED_HALVES_THIRD_BLOCK_WIDTH.md),
Sections 1-3.

The two stationary-width proofs are instances of the same re-derived
calculation, with fixed start `A/4<u<A/3`, `B=A+u`,
`h=A/3-u`, and width `d` in `[0,h]`. The removed diagonal remains chord,
with its only tie at the upper endpoint of the cutoff slab. The inserted
ratio is strictly increasing in the cell coordinate and remains chord at
the midpoint. Its endpoint increases through exactly one entry width.
This proves the complete chord/mixed branch classification needed here.

In the mixed regime, differentiating the literal cost gives
`Psi=p-(B+d)+(I_c+I_k)/2`, retaining the moving upper endpoint and both
integrals. Differentiating again retains the positive moving-boundary Q
term. The bounds `p'>17/8` and `0<J<2/15` give
`Psi'>131/120>1`. At entry,
`-tau^2/(8*B)<Psi(tau)<0`; at the cutoff,
`Psi(h)>11*h/280>0`. Continuity and these strict signs prove a unique
stationary minimum, with
`0<d_*-tau<tau^2/(8*B)`. The all-chord derivative has no additional zero.
The first-derivative matching at entry is justified by a zero-measure tie
and bounded difference quotients, not an unexamined branch choice.

For the second block, `u=lambda` satisfies the generic hypotheses. The
two directed rational endpoint gates yield
`43/1000<tau_b<87/2000`, and the distance estimate yields
`43/1000<epsilon_b<11/250`. Its sharper inherited weakening is
`epsilon_b<7/160`, with exact slack `431/32000000` after replacing tau_b
by `87/2000` and B by the conservative bound 1.

For the third block, `u=v=lambda+epsilon_b` remains strictly between
`A/4` and `A/3`. The generic proof therefore applies again without an
assumed analogy. The endpoint function decreases in A and increases in v
at the tested widths; the positive pre-square residuals justify both
squared sign comparisons. The two gates and distance estimate give
`29/5000<Delta_*<27/4000<A/3-v`. Thus all four parameters are exact
uniquely specified objects with the coarse rational bounds used by the
fourth-block theorem. No root was defined by a decimal or bracket midpoint.

## 5. Definition of the retained endpoint and remaining scope

Keep `alpha=alpha_hat`, `A=1+alpha`, and the four consecutive lengths
`lambda=A*x_*`, `epsilon_b`, `Delta_*`, `eta=1/20000`. The shifted
diagonal mass on each of these slabs is replaced by that slab's own
symmetrized reflection. Each high marginal is preserved separately;
shared endpoints have zero mass. The previous internal review checks the
rational domain margins and establishes genuine finite recovery and full
all-pairs feasibility through the general-block theorem.

Equivalently, with the unnormalized increments defined by their literal
max-integrals in the source proofs,

```text
4*pi*U_4 = 2*K(alpha_hat)+A^2*E(x_*)
           +D_b(epsilon_b)+F_3(Delta_*)+F_4(1/20000).
```

This identity specifies the same integral as the four-slab measure; it
does not use the old unqualified `C_3` at width `1/1000`. Here the actual
comparison is with `C_3(Delta_*)`. Combined with the preceding audit,
the retained endpoint and the strict fourth-block saving have no remaining
unchecked internal parameter dependency or unpaid transfer debt.

This statement concerns the explicit upper construction. It does not prove
optimality of its parameters among all partitions, among all high
permutations, or in global geometry. The separate global-limit theorem is
not reviewed in this file. External acceptance of the final packet remains
outstanding. Historical optimization/transfer claims outside the retained
graph remain outside this audit even when a checker prints them.

## 6. Independently executed commands and exact output

All four checker runs below exited **0** locally under CPython 3.14.3.
The legacy checkers contain Python assertions: these runs used assertions
enabled, without `-O`; an optimized run would not be equivalent evidence.
No production code or finite certificate verifier is imported. Optional
mpmath diagnostics were not run or used as premises. No hosted CI was
inspected by this reviewer.

```text
python -I -S ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py --exact-only
```

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

```text
python -I -S ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py --exact-only
```

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

```text
python -I -S ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py
```

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

```text
python -I -S ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py
```

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

Additional invalid-gate checks were run with this exact PowerShell command,
also exiting **0**:

```powershell
python -I -S -c @'
import runpy
if not __debug__: raise RuntimeError('assertions required')
b=runpy.run_path('ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py')
t=runpy.run_path('ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py')
checks=[(lambda:b['endpoint_gate'](0,b['XL'],b['EL']),AssertionError),(lambda:t['endpoint_gate'](1,0,t['TL']),ValueError)]
for call,kind in checks:
 try:call()
 except kind:pass
 else:raise RuntimeError('invalid gate accepted')
print('PASS assertions enabled; 2 independent invalid endpoint-gate controls rejected')
'@
```

```text
PASS assertions enabled; 2 independent invalid endpoint-gate controls rejected
```

## 7. Reviewed source identity

SHA-256 values of the principal proofs and checkers at review:

```text
research/PERMUTED_HALVES_REFLECTED_PREFIX_LAMBDA.md
407b39bcd5206dec134389613353ecbcef50bef83f094460fa2d70ba4205cfc3
research/PERMUTED_HALVES_REFLECTED_PREFIX_ALPHA_MINIMUM.md
ad166ea8ccfdc1a60073e5ff2f005a4299b678416f0f1358ca096a58571c6751
research/PERMUTED_HALVES_SECOND_BLOCK_BOUNDARY_MINIMUM.md
b5fb608178709fd29e3c535d7ddc9b337bec008e9bee7142a9f794b53778ad62
research/PERMUTED_HALVES_THIRD_BLOCK_MIXED_WIDTH.md
7e98610b45e029646ec7858a413e1cb7fce0dd1403f06a98bb22bfb90c4bd200
research/SHIFTED_ALTERNATING_HALVES.md
baae791231b841de4393f8690e06a8393dfcb0ec3a8315dae81290e33a21b5db
ops/TASK-20260905__reflected_prefix_lambda/check_lambda.py
439ac0ead71a03788bcefe72f4296a787a1e830140747192495ab8c9caa8c8d0
ops/TASK-20260905__reflected_prefix_alpha_minimum/check_alpha_minimum.py
19ed6ee315d22c5cfe525778cf032bfac8d89a803d23826ed5bd5f2bf9850521
ops/TASK-20260906__second_block_boundary_minimum/check_boundary.py
c3c475e9a9df25242b4225f993e26f99ef55914287ba6f8df32b5c2aba396b8c
ops/TASK-20260908__third_block_mixed_width/check_mixed_width.py
fd742d2586f64891b21648eceec45d714e3cd26d183f3353a4d07307b669600e
```

Only this audit file was edited for this assignment. Principal proofs,
legacy checkers, canonical ledgers, finite artifacts, publication assets,
and external review state were left untouched by this reviewer.
