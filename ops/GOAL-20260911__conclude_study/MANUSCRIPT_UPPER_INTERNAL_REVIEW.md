# Internal manuscript review: reflected blocks and U_4

    reviewed_on=2026-09-11
    scope=paper_assets/v2/ringmin_v2.tex, explicit upper constructions
    reviewer=fresh subagent, internal to the authorized research goal
    external_acceptance=not performed or implied
    outcome=INTERNALLY_VALIDATED; both requested presentation corrections resolved

The reviewer checked the manuscript's reflected-block theorem, construction,
implicit parameters, quantitative constants, U_4 comparison, and related
abstract/review qualifications against the proof sources already audited in
[the general-block review](../TASK-20260911__general_block_transfer/INTERNAL_REVIEW.md)
and [the upper-input audit](UPPER_INTERNAL_AUDIT.md). No manuscript file was
edited by this reviewer. The global-limit and balanced-word results are
outside this review; replacing the earlier limsup by C_* uses those separately
reviewed results.

## 1. Corrections requested from the manuscript author

The initial inspected manuscript had SHA-256
`1a6997ad0b50037fa108bc1200390bd3c3aaadaf4d11d79aa470fe46ab712c93`.
Line numbers below identify that version.

1. **Rank-gap wording, lines 302-303.** The integer gate gives
   `r-z>=2`, with final block endpoint `z=a_k` and `r=m-s`. Its exit
   cell `z+1` is guaranteed strictly before r, but can be only one rank
   before it. The prose said the exit was at least two ranks before the
   wrap. State the exact inequality, or distinguish the block endpoint
   from the exit cell. This removes an off-by-one ambiguity in the
   description; the underlying construction and proof bound are correct.
2. **Explicit cost notation, lines 367-371.** Define `C_3(d)` and
   `C_4(eta)` before using them in the saving identity. Specifically they
   are the complete costs for lengths `(lambda,epsilon_b,d)` and
   `(lambda,epsilon_b,Delta_*,eta)`, with the other inputs fixed. Then
   `U_4=C_4(1/20000)`. This makes the comparison self-contained and
   distinguishes it from the historical unqualified C_3 at width 1/1000.

An exact example confirms the first distinction while satisfying even the
manuscript's quantitative threshold: `alpha=0`, `ell_1=1023/1024`,
`m=2048`. Then `M=2048`, `r=2048`, `z=2046`, and the exit is 2047.
Thus `r-z=2`, while `r-(z+1)=1`.

## 2. Material-claim comparison

| Manuscript statement | Reviewed source | Finding |
|---|---|---|
| Slab measure, shifted diagonal tail, separate uniform high marginals | General transfer Sections 1 and 5 | Same construction; the strict total-length condition is retained. |
| Genuine alternating-half permutations, exact floors and parity reversals | General transfer Section 2 | Same bijection, including zero blocks, length-two identities and cyclic predecessor. Initial rank-gap wording corrected; see Section 5. |
| At most k+3 exceptional cells; 4/m and (4k-1)/m coordinate errors | General transfer Sections 2-3 | Constants and sources agree; all actual seam and wrap cells are retained in the full supplement. |
| Complete max is 4-Lipschitz and belongs to [1,3) | General transfer Section 3 | Correct for the declared compact coordinate domain. |
| Moment error (6k^2+28k+36)/m | General transfer equation (6) | Coefficient agrees exactly. |
| Full-cell criterion, unique root and both-path geometric placement | Arbitrary-high theorem, Sections 1-6; general transfer Section 4 | Correct all-pairs criterion, not a chain-root substitution. |
| Root error ((6k^2+28k+1060)/m+16384/(3m^2))/(4*pi) | General transfer equation (2) | Constants and normalizations agree. The manuscript threshold is at least 2048 and includes the geometric floor gate. |
| Odd upper bound by deletion | General transfer Section 4 | Correct; it does not assert a limit for the odd fixed-order minimum. |
| Countable slabs with total below 1-alpha | General transfer Section 5 | Tail error and diagonal finite recovery agree; the strict total-length condition is not dropped. |
| x_* and alpha_hat | Upper-input audit Sections 2-3 and linked sources | Literal integrals, domains, uniqueness and rational isolations agree. The two alpha optimizers are not conflated. |
| epsilon_b and Delta_* | Upper-input audit Section 4 and linked sources | Both are fixed-start minima over their stated intervals, with the full mixed branch retained. |
| Fourth centered integral and 1/4608000000000000 saving | Fourth-block proof Sections 1-5 | Sign, integral denominator, normalization and exact saving agree. Explicit C_3/C_4 definitions were added; see Section 5. |
| Cubic decrement and signed fourth-order remainder | Fourth-block equation (3) | The coefficient -1/(96*pi*B) and remainder upper coefficient 1/(192*pi*B^2) agree. |

For k=4 the general numerator becomes 1268, consistently with the four-block
source. The manuscript does not replace an implicitly defined parameter
by a rational surrogate or decimal estimate. In particular its terminating
decimal bracket endpoints are exactly the rational endpoints used in the
audited inputs, and epsilon_b<7/160 is the proved sharper weakening.

The centered formula is restricted to `0<eta<=1/20000`; the manuscript
does not extrapolate the chord branch through its later switch. The
construction is explicitly an upper bound and is not declared optimal
over finite or infinite partitions. Its literal complete cost is used
through finite recovery and full geometry.

## 3. Publication and evidence qualifications

The manuscript identifies itself as a versioned v2/journal candidate, not
a replacement of the historical v1 snapshot. It states that internal
adversarial checks are distinct from pending external acceptance, and it
does not claim a submission, tag, release or hosted-CI result.

The abstract's retained upper endpoint U_4 is consistent with the later
definition and theorem. The supplement citations point to the exact
mathematical checkpoint and the relevant audited source chain. Read-only
Git inspection confirmed that the cited upper-input audit exists at
`13ddb41180b3911940f4fe5cf7d61c0545f9f834`.

This review is a source-to-manuscript mathematical comparison. It does not
replace the prior deterministic checker executions, validate the complete
typeset layout, inspect finite certificate artifacts, or review mathematical
sections outside the stated upper-construction scope.

## 4. Local exact diagnostic

The following stdlib diagnostic was run locally with Python 3.14.3,
assertions unnecessary, and exited 0:

```powershell
python -I -S -c @'
from fractions import Fraction as Q
from math import ceil
m=2048; alpha=Q(0); length=Q(1023,1024)
s=(alpha*m).__floor__();z=2*(length*m/2).__floor__();r=m-s
M=ceil(2/(1-alpha-length))
if not(m>=max(2048,M) and r-z==2 and r-(z+1)==1):raise ValueError('counterexample')
print('EXACT seam wording example: m=2048, alpha=0, ell_1=1023/1024; M=2048, r=2048, z=2046, exit=2047')
print('PASS theorem hypotheses; r-z=2 while r-(z+1)=1')
'@
```

Exact output:

```text
EXACT seam wording example: m=2048, alpha=0, ell_1=1023/1024; M=2048, r=2048, z=2046, exit=2047
PASS theorem hypotheses; r-z=2 while r-(z+1)=1
```

## 5. Follow-up inspection and resolution

The reviewer inspected the revised upper section after the manuscript author
made both corrections. The inspected manuscript SHA-256 was
`39ab28b60ef73cf5999465f59c769f753a4864d59f8e5734c8c7d30d988aecb4`.

- Lines 306-308 now distinguish the final block endpoint, which is at
  least two ranks before the high wrap, from its exit, which is strictly
  before the wrap. This agrees with `r-z>=2` and resolves the first item.
- Lines 372-375 now define C_3(d), C_4(eta), and U_4 using their exact
  slab lengths before their first use in the comparison. This resolves
  the second item and preserves the intended fixed exact inputs.

The subsequent literal integral, strict saving, cubic/remainder coefficients
and non-optimality qualifications were re-read and remain correct. Both
requested corrections are closed. The upper-construction section is
**INTERNALLY VALIDATED**, with no remaining correction requested within
this review's scope. External acceptance and review of the other manuscript
sections remain separate.
