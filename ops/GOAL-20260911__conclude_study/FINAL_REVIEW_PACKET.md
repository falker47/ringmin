# Ringmin final external review packet

    goal=GOAL-20260911__conclude_study
    mode=STRICT
    terminal_state=SCIENTIFICALLY_COMPLETE
    repository_task_state=READY_FOR_REVIEW
    independent_external_acceptance=PENDING

## Review identity and integration

- Repository: falker47/ringmin, existing branch main.
- Starting HEAD: `372f96c0a9f14d968e7ecb3b1a039e7867340005`.
- External accepted baseline, read without mutation from the Review State
  Registry: `c45162f7df1b1b482b9dbecea7b619ecdaa02227`.
- Initial unaccepted fourth-continuous-block checkpoint: starting HEAD above.
- New mathematical checkpoint:
  `13ddb41180b3911940f4fe5cf7d61c0545f9f834`.
- Exact frontier-reproduction checkpoint:
  `df9c4f8fd3f27dad8b774feffed3d5102ef02994`.
- Final integration: the commit containing this packet and the v2 source/PDF
  manifest. Its immutable identity is obtained with
  `git log -1 --format=%H -- ops/GOAL-20260911__conclude_study/FINAL_REVIEW_PACKET.md`.
  At handoff this is HEAD and origin/main. The commit cannot contain its own
  literal hash; the final user report supplies it explicitly.

Review the complete delta from the accepted baseline, not just the final
packaging commit. The user's explicit goal permits internally reviewed
checkpoint commits and autonomous continuation; it does not authorize the
builder or its subagents to mark the external registry accepted. No such
write, submission, release, tag or history rewrite occurred.

## Scientific result and terminal-state basis

The central asymptotic problem is closed at the effective variational level
explicitly permitted by the goal:

```text
R*(n)=C_* n^2+o(n^2),
C_*=(1/pi) inf_(n>=2) (b_n+1)/n,
(lambda_(k,r)-1/k)/pi <= C_* <= (lambda_(k,r)+1/r)/pi,
k>=1, r>=2.
```

Here b_n is the minimum all-pair line span for marks 1/n,...,1. For every
word w of length r over {1/k,...,1}, its span ell(w) is computed by the
all-predecessor longest-path recurrence. The finite LP minimizes
`sum p_w ell(w)/r` with mass one and expected count r/k of each mark type.
The displayed width is `(1/k+1/r)/pi`, plus a controlled directed arithmetic
error. Rational endpoint LPs and certificates give a terminating procedure
for arbitrary requested precision. This characterizes a unique real value;
it is stronger than an unspecified limit or an unquantified continuum relaxation.
It is not a newly computed high-precision decimal or an elementary formula.

The [main proof](../../research/GLOBAL_ASYMPTOTIC_VARIATIONAL_LIMIT.md) is
self-contained from the exact angular model. The lower construction uses
every pair constraint; the upper recovery uses actual points and labels,
unit boundary gaps and complete geometric closure. Both parities and every
large integer size are covered. Neither the old explicit lower method nor
the reflected-block family is assumed optimal.

The strongest retained explicit endpoint interval is

```text
L = C_term + eta_width <= C_* <= U_4 = C_4(1/20000),
0.14056946887766098063257 < L < 0.14056946887766098063392,
U_4 < C_3(Delta_*) - 1/4608000000000000.
```

All symbols have exact definitions in the [owning global ledger](../../knowledge/GLOBAL_BOUNDS_ASYMPTOTICS.md)
and manuscript Sections 5-6. C_term uses tau=cos(tau),
q=(1-sin(tau))/(1+sin(tau)), and tau(1+q)/(2*pi). eta_width is the exact
closed three-cutoff width maximum, not a rounded width. U_4 uses the exact
isolated x_*, alpha_hat, epsilon_b and Delta_* and the rational fourth length.
The exact explicit gap is `C_4(1/20000)-C_term-eta_width`; neither endpoint
is claimed sharp. The effective LP bounds, rather than these two explicit
constructions, are the matching lower/upper characterization.

The second principal theorem gives genuine permutations, literal full-max
cost recovery and full-feasible roots for every fixed finite reflected slab
partition, with an explicit O(k^2/m) error and threshold. Countable partitions
with total length strictly below 1-alpha recover by truncation and a diagonal
sequence. This pays the fourth-block transfer debt and replaces an indefinite
sequence of bespoke additional-block tasks.

The complete fixed-order Supnick classification is retained after a full
minimal-dependency audit. It applies to that order at its chain root, not
the global floating structure. Finite global certification remains exactly
3<=n<=14 at the recorded tolerance, independently reproduced by the full
verifier; no larger-n exhaustive search was performed.

## Evidence and material-claim scope

The [claim matrix](CLAIM_MATRIX.md) identifies each final statement's class,
domain, source, dependencies, checker, internal review and external status.
The [final source manifest](FINAL_SOURCE_MANIFEST.json) hashes the complete
tracked source supplement and final additions, with its stated EOL convention.
The [command index](VERIFICATION.md) supplies all principal executable commands
and links exact outputs and the additional embedded independent controls.
The [dependency map](DEPENDENCIES.md) is navigation; proof notes remain the
authority and knowledge modules retain single ownership of stable claims.

Final gates:

- Fourth continuous argument and exact parameter chain: internally validated.
- General finite/countable transfer and all-pair geometry: internally validated.
- Global limit and effective primal/dual characterization: internally validated.
- Explicit L and complete fixed-order theorem: minimal surviving dependencies
  internally rederived and independently checked.
- New checkers: normal/-O success and deliberate corrupt-certificate rejection.
- Clean source gate: 15 tests passed; smoke 3..8 and full 3..14 passed after
  restoration of 12 original logs from tracked archives; every new checker
  passed again there. No ignored source input is required.
- Manuscript source: three separate bounded mathematical reviews complete;
  requested corrections resolved. Nine-page PDF built and visually inspected.
- Canonical index/ledgers, README, publication history, status and roadmap
  synchronized. REPORT remains an unchanged generated finite-result mirror.

All success above is local/internal. Exact-SHA hosted CI was not inspected.
The clean source gate used the pinned installed Windows environment, without
a separate package reinstall. POSIX execution is unclaimed. Original search
generation is not rerun; byte-preserved logs and the independent frontier
verifier reproduce its existing certificate chain, with original provenance.

## Publication candidate and protected record

The [versioned candidate PDF](../../paper_assets/v2/ringmin_v2.pdf),
[LaTeX source](../../paper_assets/v2/ringmin_v2.tex),
[build manifest](../../paper_assets/v2/BUILD_MANIFEST.json) and
[build/supplement instructions](../../paper_assets/v2/README.md) form the new
unsubmitted candidate. The complete repository at the reviewed SHA is its
proof and checker supplement. The principal new theorem is fully proved in
the manuscript; explicit endpoints and fixed-order proof details are supplied
through the precisely linked supplement.

Historical arXiv-v1 TeX/PDF, appendix tables, figures, mirrored CSVs, citation
metadata, original certificate artifacts and production src are compared
against the starting HEAD and remain unchanged. AGENTS.md and the external
review protocol remain unchanged. The only verifier delta normalizes and
confines progress-log paths; no frontier predicate is weakened.

The bounded [literature check](LITERATURE.md) identifies the shelf-packing
model and classical Supnick import. It makes no exhaustive novelty or priority
claim. AI assistance and internal/external review distinctions are disclosed
in the candidate. Author approval and journal/arXiv submission remain external
publication actions, not completion gates silently performed by this goal.

## Closed directions, limitations and remaining science

The old coefficient 1/8 and stronger deficit conjecture are disproved.
Correct marginals without recovery are insufficient. Repeated isolated
block-transfer tasks are superseded by the general theorem. The previously
optimized terminal/common-chain directions and their scoped limitations stay
in the roadmap; none is used as an unreviewed premise of the new global proof.

Practical high-precision evaluation, an elementary expression for C_*, sharp
explicit optimizers, microscopic structure, subleading terms and global
floating-circle quantifiers remain open. These are secondary to the solved
effective leading-order characterization. The word count k^r is exponential;
this study does not claim an efficient algorithm.

There are no known unpaid global-construction transfers or unchecked material
dependencies supporting this final study after internal review. The terminal
state SCIENTIFICALLY_COMPLETE describes the goal's permitted mathematical
level of closure, not external acceptance or an assertion that every related
research question is solved.

## Exactly one next atomic task

Perform one independent external review of the full delta from
c45162f7df1b1b482b9dbecea7b619ecdaa02227 to the final containing commit under
RINGMIN_REVIEW_PROTOCOL.md, including the proof matrix, exact checkers,
clean-source certificate evidence and versioned manuscript. The builder stops
after normal integration and leaves that acceptance decision to the reviewer.
