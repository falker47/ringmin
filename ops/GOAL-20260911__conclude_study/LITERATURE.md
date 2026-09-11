# Bounded literature check

Checked 2026-09-11, after independently deriving the line-packing reduction.
Queries concerned disks tangent to a line and minimum span; no external
theorem is needed by the new proof.

The primary journal record is Alt, Buchin, Chaplick, Cheong, Kindermann,
Knauer and Stehn, **Placing your coins on a shelf**, Journal of Computational
Geometry 9(1), 312-327 (2018),
[DOI and article](https://doi.org/10.20382/jocg.v9i1a10),
[primary PDF](https://jocg.org/index.php/jocg/article/download/3056/2781/8108).
It studies minimum horizontal span of disks tangent to a line, with general
hardness and approximation results. This is relevant context, not a newly
discovered model or an imported proof of the uniform-mark asymptotic theorem.

Our own exact identification is elementary: a disk of radius a_i with center
(2*x_i,a_i) is nonoverlapping with the disk at (2*x_j,a_j) precisely when
|x_i-x_j|>=sqrt(a_i*a_j). For marks at most one, horizontal disk-envelope
span differs from twice the center-span objective by between zero and two.
Thus the model is the shelf problem up to a bounded endpoint correction.

The new contribution asserted here is the original-circle asymptotic reduction,
genuine uniform-label concatenation, and effective balanced-word primal/dual
characterization with explicit vanishing errors. This bounded check is not
an exhaustive novelty search and does not establish priority over all literature.
No claim from a secondary search result is used as a mathematical premise.
