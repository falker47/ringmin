# Claim, hypothesis, proof and verification matrix

All analytic arguments are present in `supplement.tex` / `supplement.pdf`.
Source paths below are provenance only, relative to falker47/ringmin at
scientific commit `3beb8d70c5b3748d370a92855847bdf574e5a14f`.
No prior dossier is an analytic premise. No Supnick optimality or finite
certificate enumeration is required transitively: the explicit assignment
dual proves the reference inequality directly.

| Claim | Exact hypotheses | Complete proof in supplement | Source provenance | Verification and limitation |
|---|---|---|---|---|
| L1: chain root sandwich and full-feasible deletion | At least 3 original positive radii in 1..n; all pairs feasible before deletion | Section 2: cosine law, asin/atan bounds, monotone root, directed closing gaps | COMMON_CHAIN_QUANTITATIVE_STABILITY.md §2; THREE_LEVEL_COMMON_CHAIN.md §9 | Analytic reconstruction; all-pairs direction inspected. No chain-to-full inference. |
| L2: tau, q, C_term, beta_i, D_i | tau in (0,1), fixed rational cutoffs | Section 3 and §9.1: unique root, terminal integral substitution, derivative sign and endpoint limits | INDUCED_SUBSET_ASYMPTOTIC_LOWER_BOUND.md §§5–7 | Exact alternating rational Taylor signs, pi branch identity and interval gates. Decimal guesses are not premises. |
| L3: e>=0, E<=8e | One genuine cyclic order on the reflected finite grid; n>=102 | Section 4: explicit potential and integrated Hessian-free slack; exact degree-two identity and two marginals | COMMON_CHAIN_QUANTITATIVE_STABILITY.md §3, §11.1 | Directed rational checks of 48 oriented fixture tours; J_n is an assignment reference, not assumed a tour. |
| L4: signed discrepancy <=54E+2K_i | n>=102, ell_i/n>q, ell_i<=n-2, beta_i<=23/100 | Section 5: isolated Taylor 3E; bad runs 40E; primitive cancellation 11E+2K; floor error 5/n and 19/(2n) | COMMON_CHAIN_QUANTITATIVE_STABILITY.md §§4–5, 11.1–11.3 | New integer-square-root interval scorer checks 144 tour/cutoff fixtures, rotations, reversal, seam, isolated and consecutive runs, four parity pairs. Bounded corroboration only. |
| L5: sum h_i K_i <=4 sum h_i^3+E | One nonnegative measure; strip mass <=4h_i; adjacent separation; h_i>0 | Section 6: crossed consecutive block and pointwise total long cost <=d^2 | THREE_LEVEL_COMMON_CHAIN.md §7 | Byte-preserved exact checker: 48 prescribed measures; up to 8 crossings; equality and unseparated negative controls. Universal quantifier is analytic. |
| L6: order-uniform finite minimax and R*(n)>=M_(n,4) | All explicit finite gates in equation (finitegates); same outer order for all three restrictions | Section 7: weighted inequality, both scalar branches including F_n<=0; separate full-feasible deletion | THREE_LEVEL_COMMON_CHAIN.md §9 | Exact scalar sign/error checks and inherited floor counterexamples. No minimizing tour or scalar equality realization asserted. |
| L7: unique width optimum over whole polyhedron and rational enclosure | Fixed three cutoffs; nonnegative widths; two weak separation inequalities | Sections 8–9: monotone G, rational endpoint signs, positive multipliers, exact cubic remainder | THREE_LEVEL_COMMON_CHAIN.md §§11.2, 12.1–12.3 | Fresh rational recomputation and essential certificate; literal target endpoints asserted, not merely printed. All faces, zero widths and F<=0 covered analytically. |
| L8: liminf bound and identification with existing C* | Fixed 0<t<1 first, n->infinity next, t->1 last | Section 10: finite gates for t*u and common liminf; Section 11: all-pairs line comparison and labeled concatenation | THREE_LEVEL_COMMON_CHAIN.md §12.4; GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md §§1–3 | Exact boundary floor failure and scaled threshold; no min/limit exchange. Line limit existence is fully reproduced, not delegated to computational checks. |

Every source above is under `research/`. The target manuscript is
`paper_assets/asymptotic_sequel/ringmin_asymptotic.tex`, Proposition 7.
The package contains two byte-identical checkers from the fixed scientific
snapshot, under short local names. Their original paths and SHA-256 values
are recorded in MANIFEST.json; old task text is not needed to run them.

## Transitive dependency closure

Elementary calculus (IVT, differentiation, Taylor with integral remainder,
uniform convergence on a compact interval), the cosine law, finite graph
degree counting, monotonicity, and the elementary alternating-series and
binomial-series theorems are the only general mathematical prerequisites.
The sqrt-product dual bypasses finite Supnick optimality. The line comparison
and explicit labeled-copy recovery supply global limit existence; finite-word
LPs, reflected upper-bound blocks, continuum optimizers, finite global
certificates and geometric contact classifications are not dependencies.

## Epistemic classification

The analytic results are reconstructed exact theorems / proved corollaries.
The endpoint/sign enclosures are exact finite rational computations, freshly
reproduced. The new tour scorer is independently implemented from the two
copied checkers, but uses their freshly certified q interval as a parameter
input. It is not independent of the mathematical formulas being checked.
All scripts are independent of production Ringmin modules and saved results.
No script establishes all-order/all-n quantifiers by testing finite fixtures.
No external scientific acceptance or expanded finite optimum certification
is implied.
