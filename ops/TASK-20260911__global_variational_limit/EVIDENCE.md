# Evidence

## Environment and scope

Python 3.14.3, NumPy 2.4.3, SciPy 1.17.1, mpmath 1.3.0, pytest 9.0.2;
Windows PowerShell, local execution. Starting HEAD 372f96c. STRICT.
The proof is analytic; finite checks do not prove its asymptotic quantifiers.

## Checks

The [internal review](INTERNAL_REVIEW.md) records independently reconstructed
proof obligations and the two corrected scope issues. The stdlib line checker
passes normally and with -O; exact counts are in that review.

Parent ran `python -I ops/TASK-20260911__global_variational_limit/check_word_lp.py`
and the same command with `-O`: exit 0, identical output. All 1119 complete
word inequalities and 18 corrupt-certificate controls pass. Six (k,r) cases:
(1,2), (1,5), (2,2), (2,3), (3,4), (4,5). Directed lambda brackets include
[0.409906398,0.409906399] at (3,4) and [0.396136075,0.396136076] at (4,5).
These coarse finite LP values are not new best global coefficients. SciPy
discovers candidates; every primal equality and dual inequality is checked
with Fraction against directed rational costs, independently of solver status.

Parent also ran `python -m pytest`: exit 0, `12 passed in 33.64s`;
`python verify.py --start 3 --stop 8 --skip-frontier`: exit 0, all six
incumbent/local PASS, frontier SKIP; and `python verify.py --start 3 --stop 14`:
exit 0, all twelve incumbent/local/frontier PASS, including total canonical
counts 239500800 at n=13 and 3113510400 at n=14. These full runs use the
locally present ignored progress logs, so they do not yet resolve portability.
No hosted CI run inspected. No finite optimum or artifact regenerated.

## Final diff and residual uncertainty

All 23 staged task files match fully inspected content; explicit UTF-8,
newline, whitespace and 37 local-link checks pass. Staged diff has no protected
or incidental generated files. Practical high-precision computation and a simple closed form are
not claimed by a terminating arbitrary-precision characterization.
