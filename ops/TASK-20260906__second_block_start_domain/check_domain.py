"""Only the rational baseline-admissibility gates for the domain theorem.

Run with python -S. No floats, roots, quadrature, scans, optimizers,
production/previous-checker imports or file writes. The universal sign,
switch matching and boundary reduction are analytic, not sampled here.
The exact baseline minimizers/brackets are imported from the joint note.
"""

from fractions import Fraction as Q


def main():
    alpha_low, alpha_high = Q(1093, 10000), Q(10931, 100000)
    x_low, x_high = Q(719, 2500), Q(2877, 10000)
    assert 0 < alpha_low < alpha_high < Q(1, 2)
    assert 0 < x_low < x_high < Q(1, 3)
    # Monotone endpoint choices enclose the same exact implicit baseline.
    margins = {
        'lambda': (1+alpha_low)*x_low,
        'a-lambda': (1+alpha_low)*(Q(1, 3)-x_high),
        'b-a': (2-4*alpha_high)/3,
    }
    for name, lower in margins.items():
        assert lower > 0
        print(f'EXACT {name} > {lower} > 0')
    print('PASS imported bracket order and three baseline-admissibility margins')
    print('NOTE: no radical/root gates remain; continuum sign, switches and infimum reduction are proved analytically')


if __name__ == '__main__':
    main()
