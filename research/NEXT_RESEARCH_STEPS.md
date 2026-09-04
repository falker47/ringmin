# Ringmin — Next Research Steps

## Role of this file

This is the sole ranked research roadmap. It records priorities and success criteria, not proofs, task chronology, or current task state.

The public arXiv-v1 paper already supplies:

- the angular reformulation;
- the anti-Monge/Supnick solution of the chain-ordering problem;
- a full all-pairs STN formulation;
- finite global certificates for `3 <= n <= 14`;
- explicit conjectures on seam failures, the floating cascade, and asymptotics.

The first ten precise transitions, the general fixed-radius persistence
mechanism, the uniform window `4k+1<=s_k<=4k+14`, and the eventual identity
`s_k=4k+6` have now been converted into exact theorems. The sequence theorem
in `research/SUPNICK_SEAM_SEQUENCES.md` proves this identity for every `k>=6`,
completing all formal seam onsets without expanding global certification.

## Resolved Priority 1 — First all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_n*` be the chain-optimal Supnick cyclic order on `{1,...,n}`, and let

```text
R_n = R_chain(sigma_n*).
```

The theorem now proved is:

```text
theta_{R_n}(n,1) + theta_{R_n}(1,n-1)
    < theta_{R_n}(n,n-1)
```

for every integer `n >= 8`.

The reverse strict inequality holds for `3<=n<=7`, so the exact onset is `n=8`. The proof is in `research/RADIUS1_SEAM_OBSTRUCTION.md`. It compares strictly increasing chain roots with strictly decreasing explicit Descartes thresholds and closes `n=7,8` by rational inequalities. The raw angular deficit itself is not monotone.

This result concerns only the formal Supnick seam; it does not establish a global optimum or universal floating behavior.

## Resolved Priority 1 — Radius-2 all-`n` seam obstruction

**Status:** proved after arXiv v1.

Let `sigma_{2,n}*` be the chain-optimal Supnick cyclic order on `{2,...,n}`
and let

```text
R_{2,n} = R_chain(sigma_{2,n}*).
```

The theorem now proved is

```text
theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    > theta_{R_{2,n}}(n,n-1)       for 4 <= n <= 12,

theta_{R_{2,n}}(n,2) + theta_{R_{2,n}}(2,n-1)
    < theta_{R_{2,n}}(n,n-1)       for every n >= 13.
```

The proof is in `research/RADIUS2_SEAM_THRESHOLD.md`. It derives the shifted
Supnick convention and closure sums, proves that the implicit roots increase,
identifies the exact radius-2 threshold domain `n>=9`, proves that the
threshold decreases, and closes `n=12,13` by rational inequalities. The raw
angular deficit is not monotone.

This result concerns only the formal shifted Supnick seam; it does not
establish a global optimum or floating behavior.

## Resolved Priority 1 — General fixed-radius seam persistence

**Status:** proved after arXiv v1.

For every fixed integer `k>=1`, the canonical chain-minimizing Supnick order
on `{k,...,n}` has `n-1,n` as the neighbors of `k`. Its chain root
`R_{k,n}` strictly increases to infinity. The seam comparison has an exact
positive Descartes-threshold domain `n>=4k+1`, with

```text
kappa_{k,n}
  = 1/k + 1/n + 1/(n-1)
    - 2 sqrt((2n+k-1)/(k n(n-1))),
T_{k,n} = 1/kappa_{k,n}.
```

The thresholds strictly decrease to `k`, so `R_{k,n}-T_{k,n}` strictly
increases to infinity. Therefore every fixed radius has a finite first strict
seam obstruction, the obstruction persists thereafter, and equality can
occur at most once. The theorem by itself does not determine an exact onset
and makes no global-optimum or floating-circle claim.

The proof is in `research/FIXED_K_SUPNICK_SEAM.md`. The exact
`k=1,2,3,4,5,6,7,8,9,10` onsets follow by combining it with the endpoint bridges in
the ten specialized proof notes.

## Resolved Priority 1 — Uniform fixed-radius onset window

**Status:** proved after arXiv v1.

For the first strict-obstruction index of the formal fixed-radius Supnick
seam, the exact uniform bound is

```text
4k+1 <= s_k <= 4k+14              for every integer k>=1.
```

The lower bound is the general theorem's no-threshold range. For the upper
bound, the proof in `research/UNIFORM_SUPNICK_SEAM_INDEX_BOUND.md` uses only
the symbolic index `n=4k+14` and separator `S_k=k(21k+83)/22`: a strict chain
lower bound gives `R_{k,n}>S_k`, while a positive pre-square gate and an exact
coefficient-positive quadratic difference give `T_{k,n}<S_k`. The general
fixed-`k` sign criterion then supplies the strict obstruction. No finite scan
is used.

This theorem limits the search window for each formal onset but does not
identify the open exact onsets, prove full feasibility, or make a global or
floating-circle claim.

## Resolved Priority 1 — Effective fixed-radius onset formula and cutoff

**Status:** proved after arXiv v1.

For every integer `k>=4325`,

```text
s_k = 4k+6.
```

The proof in `research/EVENTUAL_SUPNICK_SEAM_ONSET.md` treats only
`n=4k+c`, `c=5,6`. Both parity-explicit Supnick sums converge uniformly after
the `k^2` scaling:

```text
R_{k,4k+c}/k^2 -> rho,
rho = (2/pi) integral_1^(5/2) sqrt(x(5-x)) dx.
```

An exact conjugate calculation gives
`T_{k,4k+c}/k^2->24/(2c-1)`, while signed integral remainders certify
`24/11<rho<8/3`. The effective bridge uses the stronger rational separators
`11/5<20/9<rho<41/16<13/5`, the existing closure error, and the exact
threshold error `4193/(256k)`. The critical cutoff margin is
`256*4325-264*4193=248>0`. Thus the formal seam is unobstructed at `4k+5`
and obstructed at `4k+6` throughout the stated tail; fixed-`k` persistence
gives the formula. No finite scan is used.

The cutoff remains valid. This earlier theorem does not alone classify
smaller indices; the sequence theorem below completes them. Neither theorem
makes a full-feasibility, global-optimum, contact-graph, or floating-circle claim.

## Resolved Priority 1 — Radius-3 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{3,...,n}`, with
`R_{3,n}=R_chain(sigma*_{3,n})`, the exact classification is

```text
theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    > theta_{R_{3,n}}(n,n-1)       for 5 <= n <= 16,

theta_{R_{3,n}}(n,3) + theta_{R_{3,n}}(3,n-1)
    < theta_{R_{3,n}}(n,n-1)       for every n >= 17.
```

Thus `s_3=17`. The proof in `research/RADIUS3_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{3,16} < 32 < T_{3,16},
T_{3,17} < 32 < R_{3,17}.
```

The threshold inequalities are rational square comparisons. The chain
inequalities use rational termwise bounds on every arcsine argument and
elementary strict bounds with exact margins. Finite high-precision roots are
diagnostic only. The result concerns one formal seam and makes no claim about
`R*(n)`, full feasibility, or floating circles in global optima.

## Resolved Priority 1 — Radius-4 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{4,...,n}`, with
`R_{4,n}=R_chain(sigma*_{4,n})`, the exact classification is

```text
theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    > theta_{R_{4,n}}(n,n-1)       for 6 <= n <= 20,

theta_{R_{4,n}}(n,4) + theta_{R_{4,n}}(4,n-1)
    < theta_{R_{4,n}}(n,n-1)       for every n >= 21.
```

Thus `s_4=21`. The proof in `research/RADIUS4_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{4,20} < 50 < T_{4,20},
T_{4,21} < 50 < R_{4,21}.
```

The threshold inequalities are rational square comparisons. The chain
inequalities audit all `17` and `18` adjacent edges with rational termwise
bounds and exact elementary bounds for `pi`. Finite high-precision roots are
diagnostic only. The result concerns one formal seam and makes no claim about
`R*(n)`, full feasibility, or floating circles in global optima.

## Resolved Priority 1 — Radius-5 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{5,...,n}`, with
`R_{5,n}=R_chain(sigma*_{5,n})`, the exact classification is

```text
theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    > theta_{R_{5,n}}(n,n-1)       for 7 <= n <= 24,

theta_{R_{5,n}}(n,5) + theta_{R_{5,n}}(5,n-1)
    < theta_{R_{5,n}}(n,n-1)       for every n >= 25.
```

Thus `s_5=25`. The proof in `research/RADIUS5_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{5,24} < 75 < T_{5,24},
T_{5,25} < 75 < R_{5,25}.
```

The threshold inequalities use explicit sign gates and rational square
margins. The chain inequalities audit all `20` and `21` adjacent edges with
rational termwise arcsine bounds and exact polynomial/integral comparisons
with `pi`. Finite high-precision roots are diagnostic only. The result
concerns one formal seam and makes no claim about `R*(n)`, full feasibility,
or floating circles in global optima.

## Resolved Priority 1 — Radius-6 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{6,...,n}`, with
`R_{6,n}=R_chain(sigma*_{6,n})`, the exact classification is

```text
theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    > theta_{R_{6,n}}(n,n-1)       for 8 <= n <= 29,

theta_{R_{6,n}}(n,6) + theta_{R_{6,n}}(6,n-1)
    < theta_{R_{6,n}}(n,n-1)       for every n >= 30.
```

Thus `s_6=30`. The proof in `research/RADIUS6_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{6,29} < 211/2 < T_{6,29},
T_{6,30} < 211/2 < R_{6,30}.
```

The threshold inequalities use exact rational square comparisons. The chain
inequalities audit all `24` and `25` adjacent edges with strict rational
termwise arcsine bounds and exact comparisons with `pi`. Finite
high-precision roots are diagnostic only. The result concerns one formal
seam and makes no claim about `R*(n)`, full feasibility, or floating circles
in global optima.

## Resolved Priority 1 — Radius-7 all-`n` seam obstruction

**Status:** proved after arXiv v1.

For the chain-optimal Supnick cycle on `{7,...,n}`, with
`R_{7,n}=R_chain(sigma*_{7,n})`, the exact classification is

```text
theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    > theta_{R_{7,n}}(n,n-1)       for 9 <= n <= 33,

theta_{R_{7,n}}(n,7) + theta_{R_{7,n}}(7,n-1)
    < theta_{R_{7,n}}(n,n-1)       for every n >= 34.
```

Thus `s_7=34`. The proof in `research/RADIUS7_SEAM_ONSET.md` reuses the
general fixed-`k` theorem and closes both endpoints with the exact rational
separator

```text
R_{7,33} < 140 < T_{7,33},
T_{7,34} < 140 < R_{7,34}.
```

The threshold inequalities use explicit sign gates and exact rational square
comparisons. The chain inequalities audit all `27` and `28` adjacent edges
with strict rational termwise arcsine bounds and exact comparisons with
`pi`. Finite high-precision roots are diagnostic only. The result concerns
one formal seam and makes no claim about `R*(n)`, full feasibility, contact
graphs, or floating circles in global optima.

## Resolved Priority 1 — Radius-8 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS8_SEAM_ONSET.md` proves

```text
R_{8,37} < 176 < T_{8,37},
T_{8,38} < 176 < R_{8,38}.
```

Exact threshold sign/square gates and complete rational chain bounds for
all 30/31 edges, with exact comparisons to `pi`, close the bridge. The
fixed-`k` theorem then gives `Delta_{8,n}>0` for `10<=n<=37` and
`Delta_{8,n}<0` for every `n>=38`, hence `s_8=38`.
The prior numerical diagnostic is not a proof premise. This concerns one
formal seam and does not expand the global certification scope.

## Resolved Priority 1 — Radius-9 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS9_SEAM_ONSET.md` proves

```text
R_{9,41} < 220 < T_{9,41},
T_{9,42} < 220 < R_{9,42}.
```

All 33/34 edges, threshold positivity/pre-square signs, directed square
margins and strict rational arcsine/pi bounds close all four gates. The
fixed-k theorem gives positive deficit on `11<=n<=41` and negative deficit
for every `n>=42`, hence `s_9=42`. Only the two endpoints enter the exact
arithmetic; no numerical scan is a premise and no global claim is changed.

## Resolved Priority 1 — Radius-10 all-`n` seam obstruction

**Status:** proved after arXiv v1.

The dedicated endpoint note `research/RADIUS10_SEAM_ONSET.md` proves

```text
R_{10,45} < 270 < T_{10,45},
T_{10,46} < 270 < R_{10,46}.
```

Both full cycle representations, all 36/37 rational edge witnesses,
threshold positivity/pre-square signs and exact arcsine/pi bounds close
all four gates. The fixed-k theorem yields positive deficit for
`12<=n<=45` and negative deficit for every `n>=46`, hence `s_10=46`.
No numerical scan, floating root or preliminary reviewer value is a
premise. This concerns the formal seam exclusively.

## Resolved Priority 1 — Sequence monotonicity and all formal seam onsets

**Status:** proved after arXiv v1.

The proof in `research/SUPNICK_SEAM_SEQUENCES.md` establishes
`D_5(k+1)<D_5(k)` and `D_6(k+1)>D_6(k)` for every integer `k>=6`, where
`D_c(k)=R_{k,4k+c}-T_{k,4k+c}`. It treats the parity change through the
exact central-edge correction, compares implicit roots with an error
smaller than the consecutive-step margin, and checks all finite algebraic
gates exactly. No effective asymptotic bound or numerical scan is a premise.

The prior k=6 bridge and fixed-k persistence then give `s_k=4k+6` for
every `k>=6`. Together with the first five specialized onsets, all formal
seam indices are classified. Separate radius-11 and later endpoint bridges
are no longer needed to classify these onsets.

## Priority 1 — All-pairs feasibility just before the formal seam onset

Exactly one next atomic task: prove or refute that the formal Supnick
placement on `{k,...,4k+5}`, at its adjacent-chain root, satisfies every
pairwise non-overlap constraint for every integer `k>=6`. Retain cyclic
closure and both angular paths; use diagnostics only to guide or falsify
the statement and certify any counterexample. The positive formal seam
deficit is known, but sufficiency for all-pairs feasibility is unresolved.
No global-optimum or floating consequence is assumed. This task has not begun.

## Deferred priority 3 — Rigorous leading asymptotics

Prove unconditional two-sided bounds sufficient to establish or refute

```text
R*(n) = n^2/8 * (1 + o(1)).
```

This requires controlling the full geometric problem, not only the chain sum, and must not assume the floating set is `o(n)` unless separately proved.

## Deferred priority 4 — Certification architecture beyond `n=14`

Only after a precise mathematical discriminator or stronger lower bound is available, investigate whether certification for `n=15` is computationally credible. A task must estimate canonical search size, pruning strength, verifier artifact size, runtime, storage, and failure modes before starting a long run.

## Lower-priority extensions

- radii `k^alpha` or general sequences;
- uniqueness/contact-graph classification of finite optima;
- three-dimensional sphere analogue;
- journal-version preparation after substantive new mathematics or external feedback.
