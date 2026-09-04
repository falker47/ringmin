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
- locally present, Git-ignored `results/checkpoints/progress_nNN_lb3.log` files referenced by those frontier artifacts;
- standalone `verify.py`, which does not import `src/ringmin`;
- source and generation metadata embedded in artifacts, including generation commit `fea000523a1ec4193d8ba9c4637563fd65e86d1a`;
- public paper tables and appendix.

A `certified` field is not sufficient by itself. The full verifier mode must include frontier verification. The bootstrap did not regenerate any artifact or prove that the current source tree is identical to the recorded generation commit.

## Non-implications owned by this module

- Local `R* +/- eta` behavior is not a global certificate.
- `--skip-frontier` does not verify global pruning.
- A best-known heuristic is not certified.
- Certified cases through `n=14` do not prove the cascade or asymptotics.
- One recovered contact graph does not establish uniqueness or a universal contact graph for all optima.

