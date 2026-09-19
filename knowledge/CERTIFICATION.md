# Certification

This thematic ledger owns the stable finite-certification scope, reported
finite regimes, evidence-chain requirements, and certification-specific
non-implications. It does not independently certify an artifact; the recorded
artifact chain and independent verifier remain controlling.

## Computer-certified finite results

**Status:** computer-certified finite results reported by the paper and artifact chain, and independently reproduced by the full verifier in this bootstrap checkout; not all-`n` theorems.

The repository reports global optima for every `n` in `3 <= n <= 14`, with claimed global absolute tolerance `1e-10` in `R`, local bracket scale `eta=1e-12`, and high-precision reconstruction/checking at 50 decimal digits.

Reported finite regimes:

- `3 <= n <= 7`: full Supnick necklace is realizable; no floating circle.
- `n = 8,9`: circle `1` floats, and the reduced necklace must be distorted to open a sufficient pocket.
- `n = 10,11,12`: circle `1` fits freely in a pocket of the Supnick necklace on `{2,...,n}`.
- `n = 13`: circle `1` floats, while the reduced Supnick necklace encounters a second seam obstruction involving circle `2`.
- `n = 14`: circles `1` and `2` float in a reported certified optimum.

Evidence chain:

- `results/nNN/optimum.json` and companion text artifacts;
- tracked `results/frontiers/nNN_frontier.json` artifacts and their coverage metadata;
- exact historical `results/checkpoints/progress_nNN_lb3.log` files referenced by those frontier artifacts, restored from tracked hash-checked archives as described in [IMPLEMENTATION.md](IMPLEMENTATION.md#full-verifier-evidence-restoration);
- standalone `verify.py`, which does not import `src/ringmin`;
- source and generation metadata embedded in artifacts, including generation commit `fea000523a1ec4193d8ba9c4637563fd65e86d1a`;
- public paper tables and appendix.

A `certified` field is not sufficient by itself. The full verifier mode must include frontier verification. The bootstrap did not regenerate any artifact or prove that the current source tree is identical to the recorded generation commit.

The research-completion goal reproduced the complete `3..14` audit from a clean source export after restoring the tracked archives. This preserves the certified scope and historical generation provenance; it is not a rerun of exhaustive generation. See the [recorded clean run](../ops/TASK-20260911__portable_frontier_evidence/CLEAN_RUN.txt).

## Independent exact-arithmetic global brackets

**Status:** computer-certified finite brackets from the supplied 2026-09-17
payload, reproduced locally by the integrated verifier; independent review of
the integration commit remains separate. This is not exact decimal equality.

For every n=3,...,14 the separate preserved certificate supports
L_n < R*(n) <= U_n with exact U_n-L_n=10^-11. The endpoints, necessary-cycle
argument, strictness for the infimum, complete skeleton/insertion partition,
rational Cartesian existence witnesses and provenance limits are owned in
detail by [GLOBAL_BRACKET_CERTIFICATE.md](../research/GLOBAL_BRACKET_CERTIFICATE.md).
The [selected original evidence](../reproducibility/global_brackets/README.md)
retains its bytes. Run `python -I -S verify_global_brackets.py` to verify all
twelve cases and the pinned input binding without production imports,
checkpoint logs, historical Top-K evidence or a generator replay.

This route does not validate historical float64 pruning or expand the finite
scope. Its 47 feasible upper witnesses do not classify exact optimal orders
or imply universal contact/floating properties. The fixed-order seam theorem
and journal readiness remain separate. Current command evidence belongs in
the [integration dossier](../ops/TASK-20260919__global_bracket_verifier/EVIDENCE.md).

## Non-implications owned by this module

- Local `R* +/- eta` behavior is not a global certificate.
- `--skip-frontier` does not verify global pruning.
- A best-known heuristic is not certified.
- Certified cases through `n=14` do not prove the cascade or asymptotics.
- One recovered contact graph does not establish uniqueness or a universal contact graph for all optima.
