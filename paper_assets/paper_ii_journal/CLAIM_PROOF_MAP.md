# Claim  ->  Lemma  ->  Hypotheses  ->  Proof  ->  Verification

Every entry concerns existing Paper II science. The main article keeps
Proposition 7 numbering. S1 is the unchanged lower supplement; S2 is the
new autonomous upper supplement. No ops chronology is a premise.

| Claim / classification | Lemmas and hypotheses | Complete proof location | Verification and boundary |
|---|---|---|---|
| Exact angular model / definition and theorem | Positive central/outer radii; both directed arcs for every pair | Main section 2, cosine law and two inverse-trigonometric formulas | Analytic; no adjacent-only replacement |
| Line recurrence and closing / exact theorem | Finite marks in [0,1]; zero marks may coincide; all predecessors | Main section 2, recurrence and Lemma 2 | checks/check_line_recovery.py: independent path oracle and missing-pair/closing controls; bounded |
| Exact geometric squeeze / exact theorem | Original labels 1..n, n>=3; linear-circle closing cost <=1 | Main Lemma 3 | Analytic monotone inequalities; no Taylor/asymptotic order assumption |
| Global limit / exact theorem | Fixed template n, q=ceil(N/n); scale nq/N and monotone genuine-label reassignment | Main Theorem 4 and proof; independent duplicate in S1 section 11 | Rational quantile and all-pair concatenation checks. Proof covers all N, both parities |
| Type quantization / proved lemma | k>=1; q copies of each upper/lower type; q->infinity first | Main section 4.1 | Analytic subadditivity, shared types and unit-mark insertion cost |
| Effective LP bracket / exact theorem | k>=1,r>=2, all k^r words, balanced expected counts | Main Theorem 5; block lower relaxation, rational vertex and unit-gap recovery | checks/check_word_lp.py checks all inequalities for six declared cases; SciPy discovers, Fraction verifies |
| Arbitrary-precision computability / proved corollary | Directed radical and pi enclosures, finite rational endpoint LPs | Main section 4.3 | Exact vertex enumeration argument is analytic; packaged sparse discovery is not claimed to implement it for all k,r |
| All-pairs alternating-half feasibility / exact theorem | m>=2, every high occurs once in [m+1,2m], every low smaller | S2: high-shell inequality and three pair types, both directions | S2 proof covers seams and m=2; no marginal-only recovery |
| General finite/countable block transfer / exact theorem | alpha in [0,1), nonnegative adjacent widths, sum <1-alpha; m gate in theorem | Main Theorem 6 statement; S2 full cell inventory, rounding/moment/angle estimates, odd deletion and tail | Quantified analytic error; alpha checker corroborates 120 bounded single-prefix recovery cases, not the general theorem |
| Exact U4 and strict saving / proved corollary | Exact x*, alpha_hat, epsilon_b, Delta*, fourth width 1/20000 | S2 parameter proofs/gates and fourth-block integral; UPPER_DEPENDENCIES.md | Directed rational sign gates isolate implicit parameters. Not global partition optimality |
| Proposition 7 lower endpoint / exact theorem plus finite rational enclosure | Fixed rational cutoffs, one common order/energy, t*u then n->infinity then t->1 | S1 L1--L8, sections 2--11; S1 DEPENDENCIES.md details every hypothesis | S1 verify.py recomputes certificate and 144 deletion fixtures; analytic proof supplies universal quantifiers |
| Candidate integrity / engineering fact | Delivered files and baseline-bound source provenance | MANIFEST.json, BUILD_REPORT.json and source archive | Hash/compile/negative controls do not establish mathematical truth |

## Acyclic Dependency Structure

Angular model  ->  line/closing  ->  squeeze  ->  global existence  ->  type quantization
 ->  balanced LP bracket  ->  computability.

Angular model  ->  high-shell cell theorem  ->  genuine finite block recovery
 ->  geometric limit; parameter isolations  ->  fourth saving  ->  U4 bound.

Angular model  ->  terminal assignment dual  ->  common-order signed deletion and
shared crossing  ->  finite minimax  ->  scaled width optimum  ->  liminf lower bound.
Global existence identifies that liminf with C*. The lower proof does not
depend on the upper construction or LP theorem. The LP proof uses neither
explicit endpoint. S1 and the main duplicate existence only to remain autonomous.

## Source Authority

Research notes at scientific snapshot
`3beb8d70c5b3748d370a92855847bdf574e5a14f` remain the repository authorities.
S1 at `75a2f448` is reused unchanged. S2 translates the needed upper closure,
with source identities in UPPER_DEPENDENCIES.md. This map is navigation,
not a new thematic claim ledger or external acceptance record.
