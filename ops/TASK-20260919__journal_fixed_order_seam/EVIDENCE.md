# Evidence

## Environment

```text
repository_head=2169bd429e25682777175ed31248b76feea8fabd
platform=Windows / PowerShell
python=3.14.3
dependency_source=existing local Python; stdlib Fraction; SymPy 1.14.0
task_mode=STRICT
```

## Claim ledger

| Claim | Classification | Evidence | Independence | Limitation |
|---|---|---|---|---|
| All-k criterion and fixed-k persistence | Exact theorem | New package, analytic proof | Direct edge matching and tangent re-derivation | Independent review pending |
| k=1,2,3 full classifications | Proved corollary | Analytic persistence and six exact bridges | Separate arctangent interval audit passed | No global/floating consequence |
| Existing complete all-k onset table | Prior theorem outside chosen scope | Dependency map below | Not re-certified here | Not a premise of the new package |

## A versus B: dependency and editorial decision

Option A would require the general equivalence and persistence proof, then
the endpoint bridges for k=1,...,6. For k=4,5,6 the separators are respectively
50 at n=20,21; 75 at n=24,25; and 211/2 at n=29,30. The infinite k>=6 row
additionally requires `SUPNICK_SEAM_SEQUENCES.md`: the parity-corrected edge
sum, midpoint estimates, implicit-root enclosure, rationalized threshold
derivative (ten polynomial positivity gates), integral derivative estimates,
and the k=6 bridge. Its rationalization is imported from section 5 of
`EVENTUAL_SUPNICK_SEAM_ONSET.md`; the effective k>=4325 cutoff is not needed.
This reconstructs where each row would come from; the ledger alone does not
prove any row, and the omitted endpoint/gate arithmetic was not rerun here.

Option B retains the general equivalence (including its equality case),
strict chain-root growth, threshold domain and sign criterion, eventual
persistence for every fixed k, and the three complete classifications
explicitly used in the finite paper. It requires six endpoint comparisons
instead of twelve and none of the uniform-in-k integral or polynomial gates.
Direct parity matching also removes Supnick optimality as a dependency;
the exact angular pocket identity is re-derived algebraically.

Choose B because the extra onset formula does not support an additional
explicit finite-paper claim. The new source supplies a general fixed-order
classification *criterion* and three explicit classifications. A future
journal transposition should say this precisely rather than suggest that
the omitted all-k explicit table has been proved in that appendix. The public
v2 has no explicit k>=4 onset table and remains unchanged. Old notes and the
existing ledger table remain provenance; the new package does not retract
or supersede their stronger scope.

## Commands and checks

All checks below were run locally in this task. No hosted CI or independent
reviewer result is implied. Commands are from the repository root; Git calls
use the command-local option `-c safe.directory=<repository-root>` because of
the sandbox ownership mismatch. No persistent Git configuration was changed.

| Exact command/check | Exit/result | What it checks | What it does not check |
|---|---|---|---|
| `python --version` | 0; `Python 3.14.3` | Runtime identity | Dependencies of other project tools |
| `python -c "import sys, sympy; print(sys.executable); print('sympy',sympy.__version__)"` | 0; local Python installation; `sympy 1.14.0` | Existing optional symbolic dependency | No environment installation performed |
| `python ops/TASK-20260919__journal_fixed_order_seam/check_exact.py --symbolic` | 0; all checks passed | Exact bridges, bounded cycles/paths, independent interval roots and symbolic identities | Not an all-k proof or independent reviewer decision |
| `python -O ops/TASK-20260919__journal_fixed_order_seam/check_exact.py --symbolic` | 0; same counts, with explicit minimum-margin gates added | Final mathematical checker, including gates under optimization | Same limitations |
| `python ops/TASK-20260919__journal_fixed_order_seam/check_package.py` | First run rejected a display delimiter; corrected separate rerun 0, output below | Transcription, links, whitespace, file allowlist, ZIP hash, one next task | Not mathematical acceptance or hosted CI |
| `git diff --check` | 0; no output | Whitespace of tracked changes | Untracked additions are covered by `check_package.py` |
| `git diff -- CURRENT_STATUS.md knowledge/FIXED_ORDER_THEORY.md research/NEXT_RESEARCH_STEPS.md` | 0; complete tracked diff read | Scope and current-state/source-navigation deltas | New files were inspected directly in full |

The final optimized exact/symbolic run reported:

```text
bridge k=1 n=7: PASS; min square margin=43/30000; sum=741/250; threshold margin=4/147; independent atan PASS
bridge k=1 n=8: PASS; min square margin=4333/26270000; sum=327/100; threshold margin=47737/8156736; independent atan PASS
bridge k=2 n=12: PASS; min square margin=32/359375; sum=1457520693/500000000; threshold margin=239/5035536; independent atan PASS
bridge k=2 n=13: PASS; min square margin=3/32500; sum=373/100; threshold margin=673/1192464; independent atan PASS
bridge k=3 n=16: PASS; min square margin=23/70000; sum=14885133/5000000; threshold margin=671/230400; independent atan PASS
bridge k=3 n=17: PASS; min square margin=1/5625; sum=63/20; threshold margin=7465/2663424; independent atan PASS
combinatorics: PASS; 128 cycles, 128 parity-growth matches, 30976 directed fan identities (all starts, both orientations)
threshold domain: PASS; 512 exact boundary comparisons (k=1..256)
independent interval roots: PASS; 12 cases, 670 positive directed slacks, 3 negative seams
symbolic: PASS; SymPy 1.14.0; original-kernel derivatives, 3 pocket identities, threshold, arcsin and pi integral
PASS: all requested bounded checks; analytic proof and independent review remain separate
```

The 12 root cases are (k,n)=(1,3),(1,4),(1,7),(1,8),
(2,4),(2,5),(2,12),(2,13),(3,5),(3,6),(3,16),(3,17).
Each of the nine feasible cases checks all multi-edge directed paths,
including adjacent complements; each onset checks a strictly negative seam.
Single-edge slacks are identically zero, not subjected to a strict test.

The corrected package audit reported:

```text
scope: PASS; only nine allowed task paths differ/add; protected tracked paths unchanged; exempt ZIP hash unchanged and unstaged
files: PASS; nine complete files inspected for whitespace/UTF-8; 26 local link targets exist
publication transcription: PASS; 21 equation labels, six rational vectors (67 edges), six minimum margins, exactly one next task
PASS: package and protected-path audit; no mathematical acceptance or hosted-CI assertion
```

### Independence and exact interval method

The checker imports no production module, saved result, prior checker or
research note. It reconstructs the rank cycle and compares its actual cyclic
edges with the separate parity formula. It uses symbolic coefficients of
individual unordered edges for the fan cancellation, including both
orientations and every starting vertex for k=1..8, N=3..18. The new direct
growth matching is checked across both parity transitions in all 128 cases.
These bounded tests cannot replace the general combinatorial argument.

For an independent analytic representation of finite roots, it uses
`theta/2 = atan(sqrt(ab/(R(R+a+b))))`, not the arcsine table inequalities.
Integer square roots bracket each radical on a 2^-65 grid. For
`S_m(z)=sum_{j=0}^{m-1}(-1)^j z^(2j+1)/(2j+1)`, integration of the finite
geometric identity gives `S_30(z)<=atan(z)<=S_31(z)` for `0<=z<1`;
negative arguments use oddness and reverse the bounds. Arguments above 1/2
are reduced by `atan z=pi/4+atan((z-1)/(z+1))`, with the reduced magnitude
explicitly bounded below 3/4. No binary floating-point arithmetic is used.

The pi interval uses
`16*S_10(1/5)-4*S_3(1/239)` and
`16*S_11(1/5)-4*S_2(1/239)`. Machin's identity follows from
`tan(2 atan(1/5))=5/12`, `tan(4 atan(1/5))=120/119`, and subtraction
of `atan(1/239)` giving tangent 1 on the positive branch below pi/2.
Thirty-eight rational bisections from [k/8,n^2], whose closure signs are
checked, enclose each selected root. Pair-angle bounds at the two endpoints
then enclose the root's directed path slacks; an inconclusive sign raises an
error. This corroborates finite cases independently of the triangle lemma
and the onset propagation; it is not a global certificate or an all-n scan.

### Twelve requested proof gates and v2 claim coverage

| Required logical gate | Self-contained location |
|---|---|
| Root existence/uniqueness | Section 2, endpoint limits and strict decrease |
| Neighbors of k, both parities | Rank definition, (5), and section 2 |
| Triangle defect and equality cases | Lemma 2, (8)-(9) |
| All-pairs fan argument | (10) and section 4 |
| Both cyclic directions | Explicit P_+, P_- in section 4 |
| Closing gap | (5), (11), adjacent-complement calculation |
| N=3 and N=4 | Separate cases in section 4 |
| Three-way equivalence | Section 4, with Cartesian criterion (2) |
| Negative seam cannot be repaired | Nonnegative gap excesses sum to zero in (11) |
| Exact onset signs | Six bridges (18), rational tables, and (17) |
| No integer equality where claimed | Section 6.3 for k=1,2,3; no universal exclusion asserted |
| Parity and quantifiers | (5), both growth matches, fixed-k comparison domain n>=4k+1 |

The public v2's `fixedseams` uses at source lines 229, 253 and 292,
and the onset statement at line 249, are covered respectively by the
k=1 classification, fixed-k persistence, general criterion/selected
classifications, and k=1,2,3 strict bridges. In a future journal version
the generic classification reference should be narrowed as prescribed in
package section 8. Decimal slacks, numerical pocket sizes, saved optimizer
descriptions and floating statements retain their separate numerical/global
sources; none is promoted to a consequence of this theorem.

No solver tests, global verifier replay or TeX build was run: these paths
and their mathematical claims are unchanged. No hosted CI was inspected or
claimed green. The requested independent STRICT review has not been started.

## Artifact and provenance checks

No numerical or publication artifact is regenerated. Initial exempt ZIP SHA-256:
`e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db`.

Final proof SHA-256:
`dadcb9584ce58fbd0fbbd693a55f8651e6866f1035e3321e68468f0f38b6a1b7`.
Final mathematical checker SHA-256:
`07025d86664172402031f96a074e3913cf7ef6c9e6357af26f962f8d4491733f`.
Provenance is the supplied accepted baseline plus this task commit; no
nondeterministic experiment, external dataset or generated certificate is used.

## Failed checks and negative evidence

Plain Git startup commands failed with dubious ownership. The command-local
safe-directory option succeeded. Git also warns that the sandbox cannot read
the user's global ignore file; the explicitly observed ZIP is still checked.
The first scoped staging command failed with `.git/index.lock: Permission
denied` (exit 1); the same nine-path command succeeded after tool-enforced
escalation (exit 0), under the standing commit/push authorization.

The first output-to-draft comparison corrected two minimum-margin annotations
(all individual bounds were already strict). The package audit then caught
one Markdown conversion error in an array-spacing command. Both corrections
and the rejected duplicate-path apply_patch call are retained in TASK_LOG.md.

## Final diff inspection

The three tracked diffs and every new file have been read in full. Only the
nine allowlisted task paths change; all other tracked files compare unchanged
against the accepted baseline. The sole pre-existing untracked ZIP has the
same SHA-256 and is explicitly excluded from staging. Direct UTF-8/whitespace
inspection includes untracked additions; ordinary `git diff --check` passed.
Links and theorem-table transcription passed. No additional knowledge owner
or global claim ledger was created: only a scoped source pointer was added
to the existing fixed-order owner.

The completion sequence is to set READY_FOR_REVIEW, recheck the final package,
stage only these paths, inspect the full staged diff, run
`git diff --cached --check`, commit and perform a normal push to the existing
origin/main, then verify the remote SHA and remaining status. Those integration
results are reported in the final task handoff; this evidence snapshot cannot
contain its own commit hash. Commit/push does not confer mathematical acceptance.

## Residual uncertainty

Independent STRICT proof review remains the sole proposed next task. Neither
the full all-k onset formula nor global optima, floating structure, hosted CI,
or overall journal readiness is newly certified by this work.
