# ringmin

Given *n* unit discs packed tangentially in a ring, what is the smallest central disc that fits?
**ringmin** certifies the global optimum for n = 3–13 by exhaustive enumeration of cyclic orderings, with each bound verified to 50 significant digits via `mpmath`.
See [MSE #4619480](https://math.stackexchange.com/q/4619480) for the original problem statement.

## Certified Results

| n  | R\*                               | optimal cycle                                        | floaters |
|----|-----------------------------------|------------------------------------------------------|----------|
|  3 | 0.260869565217391304347826086957  | [3, 1, 2]                                            | —        |
|  4 | 0.844453589560855604347528524674  | [4, 1, 3, 2]                                         | —        |
|  5 | 1.69549408120271081351328017371   | [5, 1, 4, 3, 2]                                      | —        |
|  6 | 2.79491951889692485617024406797   | [6, 1, 5, 3, 4, 2]                                   | —        |
|  7 | 4.15318955374381246513863858202   | [7, 1, 6, 3, 4, 5, 2]                                | —        |
|  8 | 5.7677942845896143026361805725    | [8, 1, 6, 4, 5, 3, 7, 2]                             | {1}      |
|  9 | 7.72672655261128921886246177604   | [9, 2, 8, 1, 5, 6, 4, 7, 3]                          | {1}      |
| 10 | 9.97990738586347760966552641468   | [10, 2, 9, 4, 7, 1, 6, 5, 8, 3]                      | {1}      |
| 11 | 12.4887204871876588517468786264   | [11, 2, 10, 4, 8, 6, 7, 1, 5, 9, 3]                  | {1}      |
| 12 | 15.2588704304484933617250043503   | [12, 2, 11, 4, 9, 6, 7, 8, 5, 1, 10, 3]              | {1}      |
| 13 | 18.3175630472173206282821941532   | [13, 3, 1, 12, 2, 10, 6, 8, 7, 9, 5, 11, 4]          | {1}      |

*floaters*: unit-disc radii that touch only the central circle in every optimal placement;
"—" means every disc touches at least one neighbour.
Certified: global optimality up to absolute tolerance 1 × 10⁻¹⁰ in R; bisection relative
tolerance 10⁻¹²; binding structure verified to 50 digits.

## Reproduce

**Requirements:** Python ≥ 3.11, pip.

**Install:**

```bash
pip install -e ".[test]"
```

**Run the test suite:**

```bash
pytest
```

All tests should pass in under 60 seconds on any modern laptop.

**Evaluate a fixed ordering** (instant):

```bash
ringmin solve --order "10,2,9,4,7,1,6,5,8,3"
```

**Certify the optimum for n = 10** (exhaustive sweep, ~5 min):

```bash
ringmin sweep --n 10
```

For larger n, parallelism helps:

```bash
ringmin sweep --n 13 --workers 8   # several hours
```

Results are written to `results/n13/` and checkpoints to `results/checkpoints/`.

## Results and Paper Assets

- [`results/`](results/) — per-n subdirectories, each containing `optimum.json`,
  high-precision R\* values, and binding-structure data.
- [`paper_assets/`](paper_assets/) — figures, CSV tables, and appendix LaTeX tables for
  the companion paper.

Checkpoint `.pkl` files (`results/checkpoints/`) are listed in `.gitignore`; they are
regenerated automatically when running `ringmin sweep --resume`.

## License

MIT — see [LICENSE](LICENSE).
