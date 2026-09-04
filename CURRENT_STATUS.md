# Current Status

## Repository snapshot

```text
repository=falker47/ringmin
task_base_head=ca3d0ee2d705a1528fce08a50ff33d321b4b22b3
observed_on=2026-09-04
phase=post-arXiv-v1 active research
```

## Current task

```text
task=TASK-20260904__increasing_order_full_asymptotics
mode=STRICT
state=READY_FOR_REVIEW
```

### Objective and current result

Prove or refute the all-`n` candidate

```text
limsup R*(n)/n^2<=1/(2*pi)
```

through the full all-pairs problem for the increasing cyclic order, after
first proving its chain-root asymptotic.

The proof establishes, for `inc_n=(1,2,...,n)`,

```text
R_chain(inc_n)=n^2/(2*pi)+O(n),
R_full(inc_n)/n^2->1/(2*pi).
```

At the explicit radius `Rhat_n=n^2/(2*pi)+n^(3/2)`, every internal adjacent
gap is tight and all closure slack is assigned to `(n,1)`. Internal paths
satisfy an ordered-radius triangle inequality. Every complementary path
crosses the enlarged seam, whose added slack is uniformly larger than every
pair angle, including when one endpoint is fixed or `o(n)`.

Chain closure alone is not feasible: at the chain root the pair `(n,2)` has
scaled two-edge seam deficit tending to `4*pi*(1-sqrt(2))<0`.

Therefore the only global conclusions are

```text
C_term<=liminf R*(n)/n^2<=limsup R*(n)/n^2<=1/(2*pi),
R*(n)=Theta(n^2).
```

Authoritative proof:
`research/INCREASING_ORDER_FULL_ASYMPTOTICS.md`.

### Allowed delta

The new proof note; this file, `PROJECT_KNOWLEDGE.md`, the roadmap, and
`ops/TASK-20260904__increasing_order_full_asymptotics/`.

### Verification gates

- Exact uniform angular and chain-root proof: complete.
- Full two-directed-path gap proof: complete.
- Fixed-endpoint seam obstruction and non-implications: complete.
- Independent 70-digit all-pairs/Cartesian diagnostic: pass after retaining
  one failed over-tight convergence assertion in the task log.
- Complete three-modification/five-addition diff, strict text/whitespace,
  empty index, and protected-path checks: pass.

### Blockers and limitations

No mathematical blocker identified. The construction deliberately uses a
coarse `n^(3/2)` additive radius and does not determine the sharp subleading
scale. It proves neither existence of the normalized global limit nor
optimality of the increasing order or either coefficient endpoint.

The arXiv-v1 paper/assets, production code, search, tests, `verify.py`,
results, finite certificates, and unrelated proof notes/dossiers are
protected. The recorded finite global certification scope remains
`3<=n<=14`.

## Exactly one next atomic task after acceptance

Independently review the uniform angular error, increasing edge-weight/root
transfer, fixed-endpoint seam obstruction, explicit two-directed-path gap
proof, and limited global deductions; record acceptance or precise
corrections without optimizing subleading terms.
