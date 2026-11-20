# Editorial changes from Paper II v3

The journal manuscript is titled *The minimum central circle for prescribed
radius profiles*. Its main example uses consecutive integer radii. The
abstract and introduction give the general distributional limit, the
finite-word approximation and the interval
0.1405694688 < C* < 0.140958576058 for the uniform profile.

| Part of the manuscript | Change |
|---|---|
| Uniform case, §§2–4 | Retains the angular comparison, finite-template infimum and word program. The program at k = r = 64 still illustrates the cost of direct enumeration. |
| Prescribed profiles, §5 | Adapts PR #8 after the finite-word section. Includes the bounded-mark squeeze, quantile replication, weak-limit proof, indexed word program, adjacent-pair estimate and power corollary. The quadratic case uses the lower bound 1/(6π) proved here. |
| Certified upper bound, §6 | Applies the finite-template infima to two rational placements at n = 3200 from PR #6. The second certificate gives C₂ < 0.088581212993 for square radii. The exact value of each limiting coefficient is open. |
| Reflected blocks | A short historical remark replaces v3 §5. It gives the certified cost interval for the specified rational parameters and refers to v3 and S2 for full geometric recovery. The earlier reflected-cell schematic leaves the journal package with that section. |
| Lower endpoint, §7 | Preserves the lower-bound proposition, its directed enclosure and its proof outline. The original lower supplement S1 is the sole journal supplement. Its proof of v3 Proposition 7 applies to Proposition 14 here. |
| Figures and references | PR #10's shelf diagram and verified bibliography carry over. Its finite-bracket plot (F3, now Figure 2) shows the strict asymptotic band at scale and in a magnified panel. |
| Data and code | Points to S1 and the pinned integer witnesses. Gives both standard-library verifier commands. |
| Author record | The byline, affiliation as supplied, date and AI acknowledgment follow PR #10 verbatim. |

## Review record

On 20 November 2026 the author reported an independent check outside Codex
of both n = 3200 certificates. A separate implementation checked all
5,118,400 pairs per certificate and used an Arb lower bound for π. The
author also reported a line-by-line reading of the profile proof note
that found no error. External human mathematical review of the profile
theorem is pending. The integration dossier records the local replays
separately. [Claim map](CLAIMS_DIFF.md) · [Integration evidence](../../ops/TASK-20261120__p2_integrated_draft/EVIDENCE.md)
