"""Independent numerical scorer and exact rational finite root certificate.

Does not import search_roots, production code, verify.py, or prior checkers.
Independent recursive enumeration; atan roots at 110 digits. The exact
certificate uses only integers/Fraction/isqrt, not the numerical artifact.
"""

from fractions import Fraction as Q
from functools import lru_cache
import contextlib
import copy
import hashlib
import io
import json
from math import factorial, isqrt
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent


def arrangements(values):
    if not values:
        yield ()
    for index, value in enumerate(values):
        for tail in arrangements(values[:index]+values[index+1:]):
            yield (value,)+tail


def numerical_score(radius, p):
    def angle(a, b):
        return 2*mp.atan2(mp.sqrt(a*b), mp.sqrt(radius*(radius+a+b)))

    # Traverse the explicit 2m-cycle and read the neighbors of each low.
    cycle = [v for low, high in enumerate(p, 1) for v in (low, high)]
    total = mp.mpf(0)
    for j in range(0, len(cycle), 2):
        low, left, right = cycle[j], cycle[j-1], cycle[j+1]
        adjacent = angle(left, low)+angle(low, right)
        chord = angle(left, right)
        total += adjacent if adjacent >= chord else chord
    return total


def independent_numeric(data):
    mp.mp.dps = 110
    assert data['source_sha256'] == hashlib.sha256(
        (HERE/'search_roots.py').read_bytes()).hexdigest()
    assert [e['m'] for e in data['sizes']] == [2, 3, 4]
    assert data['stop_reason'] == 'first robust numerical counterexample'
    maximum_error = mp.mpf(0)
    count = 0
    for entry in data['sizes']:
        m = entry['m']
        rows = {tuple(r['order']): r for r in entry['rows']}
        independent = list(arrangements(tuple(range(m+1, 2*m+1))))
        assert len(rows) == len(entry['rows']) == len(independent) == factorial(m)
        assert set(rows) == set(independent)
        values = {}
        for p in independent:
            lo, hi = mp.mpf(1)/128, mp.mpf(1024)
            assert numerical_score(lo, p) > 2*mp.pi > numerical_score(hi, p)
            for _ in range(320):
                middle = (lo+hi)/2
                if numerical_score(middle, p) < 2*mp.pi:
                    hi = middle
                else:
                    lo = middle
            value = (lo+hi)/2
            saved_lo, saved_hi = mp.mpf(rows[p]['lo']), mp.mpf(rows[p]['hi'])
            assert 0 < saved_hi-saved_lo < mp.mpf('1e-68')
            assert saved_lo < value < saved_hi
            error = abs(value-(saved_lo+saved_hi)/2)
            assert error < mp.mpf('1e-68')
            maximum_error = max(maximum_error, error)
            values[p] = value
            count += 1
        highs = tuple(range(m+1, 2*m+1))
        shifts = [highs[s:]+highs[:s] for s in range(m)]
        best, shift_best = min(values.values()), min(values[s] for s in shifts)
        guard = mp.mpf('1e-90')
        winners = sorted(p for p in values if abs(values[p]-best) < guard)
        shift_winners = sorted(p for p in shifts if abs(values[p]-shift_best) < guard)
        assert winners == sorted(map(tuple, entry['best_orders']))
        assert shift_winners == sorted(map(tuple, entry['best_shift_orders']))
        assert abs(best-mp.mpf(entry['best_root'])) < mp.mpf('1e-63')
        assert abs(shift_best-mp.mpf(entry['best_shift_root'])) < mp.mpf('1e-63')
        assert abs(shift_best-best-mp.mpf(entry['shift_minus_arbitrary'])) < mp.mpf('1e-63')
        assert entry['permutations'] == factorial(m) and entry['shifts'] == m
        print(f'PASS independent atan: m={m}, orders={len(values)}, '
              f'best={winners}, shifts={shift_winners}')
    print(f'PASS numerical roots={count}; maximum midpoint error='
          f'{mp.nstr(maximum_error, 12)}')


def additional_checks(data):
    corruptions = []
    missing = copy.deepcopy(data)
    missing['sizes'][0]['rows'].pop()
    corruptions.append(missing)
    duplicate = copy.deepcopy(data)
    duplicate['sizes'][0]['rows'][1] = duplicate['sizes'][0]['rows'][0]
    corruptions.append(duplicate)
    bracket = copy.deepcopy(data)
    bracket['sizes'][0]['rows'][0]['lo'] = '1'
    corruptions.append(bracket)
    winner = copy.deepcopy(data)
    winner['sizes'][0]['best_shift_orders'] = [[3, 4]]
    corruptions.append(winner)
    source = copy.deepcopy(data)
    source['source_sha256'] = '0'*64
    corruptions.append(source)
    for bad in corruptions:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                independent_numeric(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError('corrupted artifact accepted')
    print('PASS rejection checks: omitted/duplicate order, invalid bracket, '
          'incomplete shift ties, source hash')

    # Numerical check of both directed paths and Cartesian non-overlap;
    # this corroborates, but does not replace, the imported exact theorem.
    radius = mp.mpf(577)/100
    p = (8, 7, 5, 6)
    cycle = [v for i, high in enumerate(p, 1) for v in (i, high)]
    angle = lambda a, b: 2*mp.atan2(mp.sqrt(a*b), mp.sqrt(radius*(radius+a+b)))
    gaps = [mp.mpf(0)]*8
    for i, right in enumerate(p):
        low, left = i+1, p[i-1]
        x, y, chord = angle(left, low), angle(low, right), angle(left, right)
        gaps[(2*i-1) % 8] = x
        gaps[2*i] = max(y, chord-x)
    excess = 2*mp.pi-sum(gaps)
    assert excess > 0
    gaps[-1] += excess
    positions = [mp.mpf(0)]
    for gap in gaps[:-1]:
        positions.append(positions[-1]+gap)
    guard = mp.mpf('1e-100')
    pairs = 0
    for a in range(8):
        for b in range(a+1, 8):
            arc = positions[b]-positions[a]
            required = angle(cycle[a], cycle[b])
            assert min(arc, 2*mp.pi-arc)-required > -guard
            xa = (radius+cycle[a])*mp.cos(positions[a])
            ya = (radius+cycle[a])*mp.sin(positions[a])
            xb = (radius+cycle[b])*mp.cos(positions[b])
            yb = (radius+cycle[b])*mp.sin(positions[b])
            distance_squared = (xa-xb)**2+(ya-yb)**2
            assert distance_squared-(cycle[a]+cycle[b])**2 > -guard
            pairs += 1
    print(f'PASS 110-digit witness at R=577/100: {pairs} Cartesian pairs, '
          f'{2*pairs} directed paths; guard=1e-100')


def plus(x, y):
    return x[0]+y[0], x[1]+y[1]


def minus(x, y):
    return x[0]-y[1], x[1]-y[0]


def atan_bounds(x, terms=80):
    """Alternating Taylor partial sum and its signed next-term bound."""
    assert Q(0) < x < Q(1)
    partial = sum(((-1)**k*x**(2*k+1)/Q(2*k+1)
                   for k in range(terms)), Q(0))
    next_term = (-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(partial, partial+next_term), max(partial, partial+next_term)


def tau_bounds():
    # Machin identity: 2*pi = 32 atan(1/5) - 8 atan(1/239).
    a, b = atan_bounds(Q(1, 5)), atan_bounds(Q(1, 239))
    return 32*a[0]-8*b[1], 32*a[1]-8*b[0]


@lru_cache(None)
def angle_bounds(radius, a, b):
    radius = Q(radius)
    q = Q(a*b)/((radius+a)*(radius+b))
    assert 0 < q < 1
    scale = 10**40
    integer = isqrt(q.numerator*scale**2//q.denominator)
    low, high = Q(integer, scale), Q(integer+1, scale)
    assert low*low <= q < high*high
    coefficient, power, partial = Q(1), Q(1), Q(0)
    terms = 240
    for k in range(terms):
        partial += coefficient*power
        power *= q
        coefficient *= Q((2*k+1)**2, 2*(k+1)*(2*k+3))
    result = 2*low*partial, 2*high*(partial+power/(1-q))
    assert result[1]-result[0] < Q(1, 10**30)
    return result


def exact_cells(radius, p):
    cells = []
    for j, right in enumerate(p):
        left, low = p[j-1], j+1
        chain = plus(angle_bounds(radius, left, low),
                     angle_bounds(radius, low, right))
        chord = angle_bounds(radius, left, right)
        cells.append((max(chain[0], chord[0]), max(chain[1], chord[1])))
    return cells


def exact_score(radius, p):
    cells = exact_cells(radius, p)
    return sum(c[0] for c in cells), sum(c[1] for c in cells)


def branch(radius, low, a, b):
    """Exact sign(chain-chord), including the pre-square sign gate."""
    A, c, d = 1/Q(radius), 1/Q(a), 1/Q(b)
    e = 1/Q(low)-A-c-d
    if e <= 0:
        return 'C'
    value = 4*(A*c+A*d+c*d)-e*e
    return 'C' if value > 0 else 'H' if value < 0 else '='


def outward(interval):
    """Coarse outward decimal grid, encoded as exact rational strings."""
    scale = 10**12
    lo, hi = interval[0]*scale, interval[1]*scale
    return [str(Q(lo.numerator//lo.denominator, scale)),
            str(Q(-(-hi.numerator//hi.denominator), scale))]


def certificate():
    tau = tau_bounds()
    records = []
    # Winner below each separator, every other candidate above it.
    # The final row establishes the shift-family winner separately.
    cases = [(3, Q(559, 200), (6, 4, 5), 'all'),
             (4, Q(577, 100), (8, 7, 5, 6), 'all'),
             (4, Q(723, 125), (7, 8, 5, 6), 'shifts')]
    print('PASS exact m=2: both permutations are cyclic shifts; cells invariant')
    for m, radius, winner, domain in cases:
        highs = tuple(range(m+1, 2*m+1))
        candidates = (list(arrangements(highs)) if domain == 'all' else
                      [highs[s:]+highs[:s] for s in range(m)])
        bounds = []
        for p in candidates:
            difference = minus(exact_score(radius, p), tau)
            if p == winner:
                assert difference[1] < 0
            else:
                assert difference[0] > 0
            bounds.append(dict(order=list(p), S_minus_tau=outward(difference)))
        records.append(dict(m=m, R=str(radius), domain=domain,
                            winner=list(winner), bounds=bounds))
        other_margin = min(Q(b['S_minus_tau'][0]) for b in bounds
                           if tuple(b['order']) != winner)
        winner_bound = next(b['S_minus_tau'] for b in bounds
                            if tuple(b['order']) == winner)
        print(f'PASS exact m={m} domain={domain} R={radius}: '
              f'winner S-2pi in {winner_bound}; others > {other_margin}')

    # Independently certify useful short root brackets, not rounded floats.
    brackets = [(2, (3, 4), Q(8444535895, 10**10), Q(8444535896, 10**10)),
                (3, (6, 4, 5), Q(27949195188, 10**10), Q(27949195190, 10**10)),
                (4, (8, 7, 5, 6), Q(57677942845, 10**10), Q(57677942846, 10**10)),
                (4, (7, 8, 5, 6), Q(57835600858, 10**10), Q(57835600859, 10**10))]
    for m, p, lo, hi in brackets:
        assert minus(exact_score(lo, p), tau)[0] > 0
        assert minus(exact_score(hi, p), tau)[1] < 0
        print(f'PASS rational root bracket m={m} P={p}: {lo} < rho < {hi}')

    # Connect the observed witness to the local swap at the SHIFT ROOT.
    # Left increment is mixed, right increment chain throughout this band.
    before, after = (7, 8, 5, 6), (8, 7, 5, 6)
    for radius in (Q(577, 100), Q(723, 125)):
        assert branch(radius, 1, 6, 7) == 'C'
        assert branch(radius, 1, 6, 8) == 'H'
        for moving in (7, 8):
            assert branch(radius, 3, 5, moving) == 'C'
    delta = minus(exact_score(Q(577, 100), after),
                  exact_score(Q(577, 100), before))
    old, new = exact_cells(Q(577, 100), before), exact_cells(Q(577, 100), after)
    assert old[1] == new[1] and old[3] == new[3]
    local = plus(minus(new[0], old[0]), minus(new[2], old[2]))
    assert local[1] < 0 and delta[1] < 0
    # Bound the explicit mixed/chain increment throughout a rational band
    # containing the shift root. Every individual angle decreases in R.
    lo, hi = brackets[-1][2:]
    positive = [(6, 8), (3, 7)]
    negative = [(1, 6), (1, 7), (3, 8)]
    root_delta = (
        sum(angle_bounds(hi, a, b)[0] for a, b in positive)
        - sum(angle_bounds(lo, a, b)[1] for a, b in negative),
        sum(angle_bounds(lo, a, b)[1] for a, b in positive)
        - sum(angle_bounds(hi, a, b)[0] for a, b in negative))
    assert root_delta[1] < 0
    print('PASS exact local swap j=1: mixed/chain increments; '
          f'Delta at shift root in {outward(root_delta)}')

    artifact = dict(schema='ringmin.permuted-halves-root-certificate.v1',
                    classification='exact rational finite certificate',
                    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    angle_terms=240, sqrt_denominator='10^40', atan_terms=80,
                    separators=records,
                    root_brackets=[dict(m=m, order=list(p), lo=str(lo), hi=str(hi))
                                   for m, p, lo, hi in brackets],
                    local_swap_delta_at_577_over_100=outward(delta),
                    local_swap_delta_at_shift_root=outward(root_delta))
    (HERE/'certificate.json').write_text(json.dumps(artifact, indent=2)+'\n',
                                       encoding='utf-8')


if __name__ == '__main__':
    data = json.loads((HERE/'roots.json').read_text(encoding='utf-8'))
    independent_numeric(data)
    additional_checks(data)
    certificate()
