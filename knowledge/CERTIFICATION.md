# Certification

This thematic ledger owns the stable finite-certification scope, reported
finite regimes, evidence-chain requirements, and certification-specific
non-implications. It does not independently certify an artifact; the recorded
artifact chain and independent verifier remain controlling.

## Computer-certified finite results

**Status:** historical computer-certified finite results reported by the paper
and artifact chain, independently reproduced by the full historical verifier
under that route's numerical guards; not all-`n` theorems. The accepted exact
global bracket claim has the separate evidence chain below.

The repository reports global optima for every `n` in `3 <= n <= 14`, with claimed global absolute tolerance `1e-10` in `R`, local bracket scale `eta=1e-12`, and high-precision reconstruction/checking at 50 decimal digits.

Reported finite regimes:

- `3 <= n <= 7`: full Supnick necklace is realizable; no floating circle.
- `n = 8,9`: circle `1` floats, and the reduced necklace must be distorted to open a sufficient pocket.
- `n = 10,11,12`: circle `1` fits freely in a pocket of the Supnick necklace on `{2,...,n}`.
- `n = 13`: circle `1` floats, while the reduced Supnick necklace encounters a second seam obstruction involving circle `2`.
- `n = 14`: circles `1` and `2` float in a reported certified optimum.

Historical evidence chain:

- `results/nNN/optimum.json` and companion text artifacts;
- tracked `results/frontiers/nNN_frontier.json` artifacts and their coverage metadata;
- exact historical `results/checkpoints/progress_nNN_lb3.log` files referenced by those frontier artifacts, restored from tracked hash-checked archives as described in [IMPLEMENTATION.md](IMPLEMENTATION.md#full-verifier-evidence-restoration);
- standalone `verify.py`, which does not import `src/ringmin`;
- source and generation metadata embedded in artifacts, including generation commit `fea000523a1ec4193d8ba9c4637563fd65e86d1a`;
- public paper tables and appendix.

A `certified` field is not sufficient by itself. For this historical route,
the full verifier mode must include frontier verification. The bootstrap did
not regenerate any artifact or prove that the current source tree is identical
to the recorded generation commit.

This route's float64 Stage-A/Top-K/frontier comparisons retain their historical
worst-case error and frontier-completeness limitations. High-precision checking
of saved orders does not retroactively prove every excluded-order comparison.
The [2026-09-16 audit](../ops/TASK-20260916__journal_readiness/CERTIFICATION_UPGRADE_PLAN.md)
records that boundary; it is historical provenance, not a prerequisite for the
separate exact bracket result below.

The research-completion goal reproduced the complete `3..14` audit from a clean source export after restoring the tracked archives. This preserves the certified scope and historical generation provenance; it is not a rerun of exhaustive generation. See the [recorded clean run](../ops/TASK-20260911__portable_frontier_evidence/CLEAN_RUN.txt).

## Independent exact-arithmetic global brackets

**Status:** computer-certified finite result, independently reviewed and
accepted for `n=3,...,14` at baseline
`f6f22e95af495a4b0385322a5b6add5966cd7296`. The user supplied the completed
STRICT review and accepted Review State Registry baseline on 2026-09-19;
the [reconciliation evidence](../ops/TASK-20260919__journal_readiness_reconciliation/EVIDENCE.md#accepted-review-provenance)
records that attribution. Acceptance applies to that reviewed baseline;
later commits require separate review. This is not exact decimal equality.

For every integer `n=3,...,14`, the accepted claim is
`L_n < R*(n) <= U_n` with exact `U_n - L_n = 10^-11`. The global chain combines
outward-checked angular intervals, exact integer DP/pruning and complete
canonical skeleton/insertion coverage for the lower bound, with at least one
exact rational Cartesian existence witness for each n for the upper bound.
The endpoints, necessary-cycle argument, strictness for the infimum,
complete skeleton/insertion partition,
rational Cartesian existence witnesses and provenance limits are owned in
detail by [GLOBAL_BRACKET_CERTIFICATE.md](../research/GLOBAL_BRACKET_CERTIFICATE.md).
The [selected original evidence](../reproducibility/global_brackets/README.md)
retains its bytes. Run `python -I -S verify_global_brackets.py` to verify all
twelve cases and the pinned input binding without production imports,
checkpoint logs, historical Top-K evidence or a generator replay.

The former numerical-certification journal blocker is closed for this finite
claim through the accepted exact global-bracket route: the historical
Stage-A/Top-K/frontier float64 path is no longer a necessary dependency of its
proof. This does not retroactively certify historical float64 pruning.

The scope remains n=3,...,14. Its 47 feasible upper witnesses do not classify
exact optimal orders or imply universal contact/floating properties. Neither
results for n>14, asymptotics, the publication-quality fixed-order seam theorem,
peer review nor overall journal readiness were accepted by this review.
The [implementation](../ops/TASK-20260919__global_bracket_verifier/EVIDENCE.md)
and [merge](../ops/TASK-20260919__merge_global_bracket_verifier/EVIDENCE.md)
dossiers retain their original local-command and then-pending-review context;
the proof note retains its derivation and verifier-specific provenance limits.

## Non-implications owned by this module

- Local `R* +/- eta` behavior is not a global certificate.
- `--skip-frontier` does not verify global pruning.
- A best-known heuristic is not certified.
- Certified cases through `n=14` do not prove the cascade or asymptotics.
- One recovered contact graph does not establish uniqueness or a universal contact graph for all optima.
