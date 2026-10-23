# Core analytic audit: angular comparison, existence, and word LP

    audited_on=2026-10-23
    mode=STRICT
    baseline=75a2f448038d627b2661ea7c9d6fd0fcdb6d33ae
    review_kind=independent internal analytic audit by delegated reviewer
    conclusion=no invalidating gap found in audited scope
    external_acceptance=not performed or implied

## Scope and protected material

Read the applicable AGENTS.md, canonical index/status, relevant global-ledger
entry and current asymptotic roadmap entry. Reconstructed the arguments in
`paper_assets/asymptotic_sequel/ringmin_asymptotic.tex`, Sections 2--4, and
`research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md`, Sections 1--6. Compared
only the duplicate global-existence argument in
`paper_assets/asymptotic_sequel/proposition7_supplement/supplement.tex`,
under the heading "Existence of the global limit". Read the two bounded checkers in
`ops/TASK-20260911__global_variational_limit/` and its specifically relevant
historical internal review/evidence. The historical outputs were not treated
as current execution evidence.

Only this audit record was written by this reviewer. No public source,
research note, result artifact, production code, certificate, or Review State
Registry was edited. The parent owns the candidate package and final diff.
Plain `git status --short` in this managed checkout reported that it must be
run in a work tree; an explicit work-tree attempt reported a cwd permission
error. Therefore this subreview does not assert checkout cleanliness.
`git rev-parse HEAD` returned the baseline recorded above.

## Analytic findings

No correction is required to the audited theorem statements or proofs.
The following are analytic checks, not conclusions inferred from finite tests.

1. **Ordered recurrence, including zero marks.** All weights are nonnegative,
   so the predecessor maximum preserves nondecreasing coordinates even when
   marks vanish. It enforces every earlier-pair inequality. Componentwise
   induction proves minimality after translation to x_1=0. Every increasing
   path from first to last has at most N-1 edges. A zero between positive
   marks cannot defeat their nonadjacent constraint.
2. **Both angular arcs.** The atan identity follows from
   (R+u)(R+v)-uv=R(R+u+v). The asin lower and atan upper inequalities have the
   required directions for every R>0. Closing a line with gap one controls
   its complementary arcs; scaling controls every original pair. The squeeze
   has the correct normalization and lower error -1/n, and its stated domain
   n>=3 avoids the degenerate two-circle infimum issue.
3. **Genuine-label existence.** For q=ceil(N/n), the sorted retained copied
   marks are ceil(i/q)/n. Scaling by nq/N dominates each target i/N and
   assigns every target label once to a retained point. Mark reduction keeps
   all constraints. Intermediate marks above one cause no issue because
   positions and marks are scaled homogeneously. Dividing the displayed span
   bound by N yields the asserted limsup bound for every large integer N.
   A liminf subsequence closes existence, and the infimum formula follows.
4. **Quantization.** Subadditivity applies separately to upper and lower
   finite-type systems. Zero marks cost no span. Removing zeros and appending
   q unit marks costs at most q, including the join; k=1 gives the same bound
   directly. Sorted uniform marks lie between the two type arrays. Thus the
   one-sided error is exactly the claimed bound 1/k.
5. **LP lower bound.** With m=floor(kq/r) disjoint blocks, total span is at
   least the sum of their spans. After division by kq, m/(kq) tends to 1/r.
   The fewer-than-r discarded vertices cause vanishing count error, so any
   convergent empirical frequency subsequence has the required type means.
6. **Rational vertex and upper recovery.** The feasible polytope is nonempty
   and compact with rational vertices. A linear objective with real algebraic
   costs still attains a minimum at a vertex. Clearing its denominators gives
   integral word multiplicities and equal integral type counts Dr/k. Unit
   gaps control all cross-word pairs. Repeated batches, together with the
   already proved finite-type limit, give the error 1/r without requiring
   arbitrary local marginals to form a cycle.
7. **Computability.** Directed rational edge intervals of width epsilon give
   word-span interval width at most (r-1)epsilon and normalized LP width at
   most (r-1)epsilon/r. Rational endpoint LPs have a terminating exact vertex
   enumeration algorithm; algebraic equality need not be decided by interval
   refinement. Controlling k, r, radical precision and a rational pi enclosure
   establishes arbitrary-precision computability in principle. It gives no
   efficient precision algorithm or explicit optimizer.
8. **Duplicate proof.** The Proposition 7 supplement's existence proof agrees
   with this argument, including the scaling factor, every-integer-N recovery,
   all-pairs squeeze and infimum. No inconsistent duplicate claim was found.

## Fresh bounded checks

Environment: local Windows PowerShell; Python 3.14.3; SciPy 1.17.1.
All commands below were independently run during this audit and exited 0:

```text
python -I -B ops/TASK-20260911__global_variational_limit/check_line_recovery.py
python -I -B -O ops/TASK-20260911__global_variational_limit/check_line_recovery.py
python -I -B ops/TASK-20260911__global_variational_limit/check_word_lp.py
python -I -B -O ops/TASK-20260911__global_variational_limit/check_word_lp.py
```

The two line runs had identical complete output:

```text
PASS: 1089 rational words; 13995 independent paths; 13941 pair/closure checks; 1089 all-pair concatenations; 94620 genuine-label quantiles; 4 negative controls rejected.
```

The two LP runs had identical complete output:

```text
PASS k=1 r=2: 1 words; 1 primal blocks; lambda in [0.500000000,0.500000000]; all rational primal/dual gates
PASS k=1 r=5: 1 words; 1 primal blocks; lambda in [0.800000000,0.800000000]; all rational primal/dual gates
PASS k=2 r=2: 4 words; 1 primal blocks; lambda in [0.353553390,0.353553391]; all rational primal/dual gates
PASS k=2 r=3: 8 words; 2 primal blocks; lambda in [0.436886723,0.436886724]; all rational primal/dual gates
PASS k=3 r=4: 81 words; 2 primal blocks; lambda in [0.409906398,0.409906399]; all rational primal/dual gates
PASS k=4 r=5: 1024 words; 3 primal blocks; lambda in [0.396136075,0.396136076]; all rational primal/dual gates
PASS 1119 complete word inequalities; 18 corrupt certificates rejected
Scope: bounded exact LP certificates; no finite Ringmin optimum, simple closed form, or asymptotic proof by computation.
```

An additional `python -I -B -` inline probe loaded the LP checker with
runpy, enumerated every increasing-index path for both rational endpoints
of every word in those six cases, and compared the independent maxima with
`span`. It also required rejection of a negative radicand, dependent support,
inconsistent support, and altered type margin preserving mass/nonnegativity.
It exited 0 with:

```text
PASS: 17090 independent endpoint-path evaluations; 4 additional negative controls rejected.
```

The exact inline Python program passed to `python -I -B -` was:

```python
from fractions import Fraction as Q
from itertools import product
import runpy
ns = runpy.run_path('ops/TASK-20260911__global_variational_limit/check_word_lp.py')
ns['rejects'](ns['sqrt_interval'], Q(-1))
ns['rejects'](ns['solve_columns'], [[Q(1), Q(1)], [Q(2), Q(2)]], [Q(1), Q(2)])
ns['rejects'](ns['solve_columns'], [[Q(1)], [Q(1)]], [Q(1), Q(2)])
counts = [(2, 0), (0, 2)]
ns['check_primal']([Q(1, 2), Q(1, 2)], counts, 2, 2)
ns['rejects'](ns['check_primal'], [Q(3, 4), Q(1, 4)], counts, 2, 2)
checks = 0
for k, r in [(1, 2), (1, 5), (2, 2), (2, 3), (3, 4), (4, 5)]:
    roots = {(i, j): ns['sqrt_interval'](Q(i*j, k*k)) for i in range(1, k+1) for j in range(1, k+1)}
    for word in product(range(1, k+1), repeat=r):
        for endpoint in (0, 1):
            best = Q(0)
            for bits in product((0, 1), repeat=r-2):
                indices = [0] + [j+1 for j, bit in enumerate(bits) if bit] + [r-1]
                value = sum((roots[word[i], word[j]][endpoint] for i, j in zip(indices, indices[1:])), Q(0))
                best = max(best, value)
                checks += 1
            if best != ns['span'](word, roots, endpoint):
                raise RuntimeError('independent endpoint path oracle failed')
print(f'PASS: {checks} independent endpoint-path evaluations; 4 additional negative controls rejected.')
```

These are independently reproduced finite arithmetic results. They do not
prove the infinite quantifiers, certify a new finite Ringmin optimum, run
frontier verification, or establish hosted CI status. The theorem audit is
independent mathematical reasoning within the same research task, not an
external acceptance decision.

## Checker portability and minimum package verification

- `check_line_recovery.py` uses only the standard library and no Ringmin
  imports. It tests rational square marks, all-pairs/closing/concatenation,
  path-oracle equality, genuine-label quantiles, and explicit negative controls.
- `check_word_lp.py` has no Ringmin/prior-checker import, but requires SciPy.
  SciPy discovers a support and dual. Fraction arithmetic reconstructs primal
  weights, checks all type equations, repairs the dual by an exact maximum
  violation, and checks every complete-word inequality. Its absent final-type
  dual coefficient is implicitly zero. Discovery can fail on a different
  solver version, but such failure cannot certify an invalid candidate.
- Keep this distinction explicit in package dependencies and verification
  scope. The bounded SciPy generator/checker is not the general terminating
  exact vertex-enumeration algorithm asserted by the computability proof.
- Minimum useful package gate: run copied checkers in isolated normal and -O
  modes outside repository import paths, record Python/SciPy versions and
  output, and preserve source hashes. Retain the extra endpoint path oracle
  and malformed-candidate probes in reproducible package verification where
  convenient. No full finite-optimum frontier run is needed solely to validate
  unchanged analytic-core packaging.

## Source fingerprints observed

SHA-256, recorded before this audit file was written:

```text
5248445a3a1b92c494466fdfe266555023bbc13606f93ffc07ec229538b886e6  paper_assets/asymptotic_sequel/ringmin_asymptotic.tex
4648e053f89b3ca110ee4615f87c1171f750469a5b81a593bbb678f809614bdd  research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md
b8aa60b3584e2f512154923c6ec53396ef57f778cf4cca06aa2bb9b631761664  ops/TASK-20260911__global_variational_limit/check_line_recovery.py
ad1edc08732932cad4f4ef8410057ac642933e3fc8631205f7f27185bb061cda  ops/TASK-20260911__global_variational_limit/check_word_lp.py
ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4  paper_assets/asymptotic_sequel/proposition7_supplement/supplement.tex
```

Next atomic review step: audit the assembled journal candidate and its exact
package verification against these analytic obligations. No next task was
begun, and this reviewer performed no commit or push.

## Final Journal-Candidate Binding (2026-10-23)

The reviewer reread the complete current `paper_assets/paper_ii_journal/main.tex`
core, from section 2 (Exact Angular Comparison) through section 4.3 (Exact
Certificates and Computational Meaning), and the candidate's complete
`CLAIM_PROOF_MAP.md`. This binds the preceding analytic findings directly to
the journal candidate, not merely to its public-preprint source.

Final inspected SHA-256 values:

```text
2e74ed7ca0385523d98d8573ce0a0b20b3fbe51a6e9c8adda29550b70df69b06  paper_assets/paper_ii_journal/main.tex
59544e854a7c5b3472b2e5d0e0cec9142c4458076612934751b7aa1362223d58  paper_assets/paper_ii_journal/CLAIM_PROOF_MAP.md
```

### Delta and Analytic Conclusion

An inspected unified diff against the previously audited public core contains
exactly six section/subsection title-capitalization changes. Removing those
titles gives identical text. No theorem, formula, hypothesis, proof step,
quantifier, numerical bound or computational claim changed in sections 2--4.
In particular the final candidate preserves:

- both-arc angular control and the n>=3 squeeze;
- the all-predecessor recurrence, including zero marks;
- actual point/label reassignment with scale nq/N, every sufficiently large
  integer target size and both parities;
- the fixed-k finite-type limit before quantization;
- the two-sided LP bracket for every k>=1 and r>=2, retaining all k^r words;
- compact rational-polytope recovery even with algebraic objective entries;
- the separately paid 1/k and 1/r errors;
- rational endpoint LPs for terminating in-principle computability, without
  an indefinite algebraic-equality interval oracle or an efficiency claim.

The claim/proof map has no stronger mathematical or evidentiary promise than
the candidate proof. Its numbering agrees with the candidate: closing Lemma 2,
squeeze Lemma 3, existence Theorem 4 and finite-word Theorem 5. The map states
that six bounded word-LP cases are checked, that SciPy only discovers
candidates, and that the packaged solver is not the general exact
vertex-enumeration algorithm. It keeps lower/upper endpoint proofs independent
of the LP theorem and treats hash/build checks as engineering evidence.

The map initially read at SHA-256
`728a5697813feecb324d4be91dc9281086c96e58e1133ad408ecedfbd28028d9`
had the editorial duplication `section section 2--11` in the unrelated
Proposition 7 row. The parent corrected it to `sections 2--11`. Replacing
that corrected phrase by the original one in memory reproduces the initial
hash exactly, independently confirming that this was the sole map change.
The final map hash is recorded above. No mathematical correction was needed.

Conclusion: **no invalidating gap found in the final candidate's audited
core or its claim/proof map at these exact snapshots**. This is an internal
analytic review conclusion, not external acceptance or a new finite-optimum
certificate. No mathematical source was edited by this reviewer.

### Exact Comparison Evidence

All comparison checks were local standard-library checks under Python 3.14.3.
The initial extra probe required the packaged core checkers to match original
bytes exactly. It exited 1 at `check_line_recovery.py` with
`RuntimeError: ('checker copy differs', 'check_line_recovery.py')`.
The subsequent text diffs were empty for both files. Inspection established
that their only changes are CRLF-to-LF normalization. This failed binary
assertion is retained here; byte identity is not claimed.

The following complete comparison program was piped to `python -I -S -B -`
from the repository root and exited 0:

```python
from pathlib import Path
from hashlib import sha256
import re
public=Path('paper_assets/asymptotic_sequel/ringmin_asymptotic.tex').read_text(encoding='utf-8')
main_path=Path('paper_assets/paper_ii_journal/main.tex')
main=main_path.read_text(encoding='utf-8')
base_core=public[public.index(r'\section{Exact angular comparison}'):public.index(r'\section{Explicit geometric upper constructions}')]
candidate_core=main[main.index(r'\section{Exact Angular Comparison}'):main.index(r'\section{Explicit Geometric Upper Constructions}')]
without_headings=lambda text: re.sub(r'\\(?:sub)?section\{[^}]*\}', '', text)
if without_headings(base_core) != without_headings(candidate_core):
    raise RuntimeError('non-heading mathematical core difference')
print('PASS main sections 2--4 identical after removing section/subsection titles; inspected unified diff contains only six heading-capitalization changes.')
for name in ('check_line_recovery.py','check_word_lp.py'):
    original=(Path('ops/TASK-20260911__global_variational_limit')/name).read_bytes()
    candidate=(Path('paper_assets/paper_ii_journal/checks')/name).read_bytes()
    if original.replace(b'\r\n',b'\n') != candidate:
        raise RuntimeError(('checker has non-newline difference',name))
    print('PASS',name,': CRLF-to-LF only;',len(original),'->',len(candidate),'bytes')
for path in (main_path,Path('paper_assets/paper_ii_journal/CLAIM_PROOF_MAP.md')):
    print(sha256(path.read_bytes()).hexdigest(),path.as_posix())
```

Material output before the map's typo correction:

```text
PASS main sections 2--4 identical after removing section/subsection titles; inspected unified diff contains only six heading-capitalization changes.
PASS check_line_recovery.py : CRLF-to-LF only; 5447 -> 5300 bytes
PASS check_word_lp.py : CRLF-to-LF only; 7185 -> 7007 bytes
2e74ed7ca0385523d98d8573ce0a0b20b3fbe51a6e9c8adda29550b70df69b06 paper_assets/paper_ii_journal/main.tex
728a5697813feecb324d4be91dc9281086c96e58e1133ad408ecedfbd28028d9 paper_assets/paper_ii_journal/CLAIM_PROOF_MAP.md
```

The final map-only delta was verified with this exact command (exit 0):

```text
python -I -S -B -c "from pathlib import Path; from hashlib import sha256; p=Path('paper_assets/paper_ii_journal/CLAIM_PROOF_MAP.md'); b=p.read_bytes(); old=b.replace(b'sections 2--11',b'section section 2--11'); h=sha256(old).hexdigest(); print('Reconstructed pre-correction map SHA-256:',h); assert h=='728a5697813feecb324d4be91dc9281086c96e58e1133ad408ecedfbd28028d9'; print('PASS map changed only the reported section-reference typo.')"
```

It printed the exact initial map hash and
`PASS map changed only the reported section-reference typo.`

The previously recorded independent checker executions apply to unchanged
Python logic; the package copies differ only in line endings. No redundant
checker rerun was used as a substitute for reading the final proof. The
parent's package-wide executions remain separately recorded task evidence.
