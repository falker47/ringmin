"""Exact finite-grid audit of terminal quantile dominance.

This is corroborative: it exhausts unions of rational grid cells, but the
continuum proof is the measure-capacity argument in the authoritative note.
"""

from fractions import Fraction


def main() -> None:
    set_count = 0
    rank_cell_count = 0
    equality_count = 0

    for denominator in range(1, 13):
        for mask in range(1, 1 << denominator):
            cells = [
                index for index in range(denominator) if mask & (1 << index)
            ]
            retained = len(cells)
            terminal = list(range(denominator - retained, denominator))
            all_ranks_equal = True

            for rank, cell in enumerate(cells):
                # On this retained rank cell, t=(rank+u)/denominator and
                # Q_A(t)=(cell+u)/denominator.  The variable u cancels.
                slack = Fraction(denominator - retained + rank - cell,
                                 denominator)
                if slack < 0:
                    raise AssertionError(
                        f"negative quantile slack: m={denominator}, "
                        f"cells={cells}, rank={rank}"
                    )
                all_ranks_equal &= slack == 0
                rank_cell_count += 1

            is_terminal = cells == terminal
            if all_ranks_equal != is_terminal:
                raise AssertionError(
                    f"equality mismatch: m={denominator}, cells={cells}"
                )
            equality_count += int(all_ranks_equal)
            set_count += 1

    expected_equalities = 12 * 13 // 2
    if equality_count != expected_equalities:
        raise AssertionError(
            f"expected {expected_equalities} terminal masks, "
            f"found {equality_count}"
        )

    print(
        "finite_grid_quantile_dominance=PASS "
        f"sets={set_count} rank_cells={rank_cell_count}"
    )
    print(
        "equality_classification=PASS "
        f"terminal_masks={equality_count} denominators=1..12"
    )
    print("arithmetic=fractions.Fraction imports_ringmin=NO")
    print("classification=EXACT_FINITE_GRID_AUDIT_ONLY")


if __name__ == "__main__":
    main()
