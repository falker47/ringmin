"""Standalone exact verification of the Proposition 7 supplement.

Python >=3.11, standard library only; run with -I -S, without -O.
The inherited checker supplies parameter interval arithmetic. New directed
integer-square-root fixtures independently score actual cyclic deletions.
Analytic universal claims belong to supplement.tex, not to these fixtures.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import runpy
import subprocess
import sys

if not __debug__:
    raise RuntimeError('Enabled assertions are required; omit -O.')

HERE = Path(__file__).resolve().parent


def parameters():
    w = runpy.run_path(str(HERE/'check_width_optimum.py'))
    w['transcendental_gates']()
    ds = tuple(w['deletion'](beta) for beta in w['BETA'])
    w['symbolic_identity_gates']()
    w['polynomial_gates'](ds)
    w['floor_gates']()
    h = w['widths'](w['X'])
    numerator = w['numerator'](h, ds)
    denominator = w['denominator'](h)
    rho = w['div'](numerator, denominator)
    eta = w['div'](rho, w['PI'])
    c = w['div'](w['mul'](w['TAU'], w['add'](w['point'](1), w['Q'])),
                 w['scale'](2, w['PI']))
    full = w['add'](c, eta)
    target = (F('0.14056946887766098063257'),
              F('0.14056946887766098063392'))
    assert target[0] < full[0] <= full[1] < target[1]
    assert F('0.00000038803240421408705') < eta[0]
    assert eta[1] < F('0.00000038803240421408841')
    multipliers = [w['sub'](w['sub'](ds[i], w['scale'](24, w['power'](h[i], 2))),
                            w['scale'](432, rho)) for i in (0, 2)]
    assert numerator[0] > 0 and multipliers[0][0] > F('0.00035')
    assert multipliers[1][0] > F('0.00059')
    signs = {name: w['stationary'](w['point'](z), ds)
             for name, z in [('zero', F(0)), ('a', w['A']),
                             ('z_minus', w['X'][0]), ('z_plus', w['X'][1])]}
    assert signs['zero'][0] > 0 > signs['a'][1]
    assert signs['z_minus'][0] > 0 > signs['z_plus'][1]
    for di, lower, upper in zip(ds,
            ['0.00136820131190299900276', '0.00196196296152142894680',
             '0.00241410289623904895464'],
            ['0.00136820131190299900279', '0.00196196296152142894683',
             '0.00241410289623904895467']):
        assert F(lower) < di[0] <= di[1] < F(upper)

    def pair(value):
        return [str(v) for v in value]

    cert = {
        'schema': 'ringmin-proposition7-rational-v1',
        'scientific_commit': '3beb8d70c5b3748d370a92855847bdf574e5a14f',
        'semantics': 'closed rational enclosures; target enclosure is strict',
        'tau': pair(w['TAU']), 'q': pair(w['Q']), 'pi': pair(w['PI']),
        'beta': [str(v) for v in w['BETA']],
        'D': [pair(v) for v in ds], 'z_star': pair(w['X']),
        'widths': [pair(v) for v in h], 'G_signs': {k: pair(v) for k, v in signs.items()},
        'F_at_u': pair(numerator), 'L_at_u': pair(denominator),
        'rho': pair(rho), 'multipliers': [pair(v) for v in multipliers],
        'C_term': pair(c), 'eta_width': pair(eta), 'lower_coefficient': pair(full),
        'strict_target': pair(target),
    }
    print('PASS literal Proposition 7 endpoints, D_i enclosures and positive KKT gates')
    return w, cert


# Independent interval primitives for the finite geometry/deletion fixtures.
# No interval helper or tour constructor is imported from the inherited checker.
SCALE = 10**60


def sqrt_interval(v):
    v = F(v)
    if v < 0:
        raise ValueError('Square root domain is nonnegative')
    k = isqrt(v.numerator*SCALE*SCALE//v.denominator)
    lo = F(k, SCALE)
    hi = lo if k*k*v.denominator == v.numerator*SCALE*SCALE else F(k+1, SCALE)
    assert lo*lo <= v <= hi*hi
    return lo, hi


def plus(*values):
    return sum(v[0] for v in values), sum(v[1] for v in values)


def minus(u, v):
    return u[0]-v[1], u[1]-v[0]


def times(c, v):
    return min(c*v[0], c*v[1]), max(c*v[0], c*v[1])


def abs_bound(v):
    return max(abs(v[0]), abs(v[1]))


def edges(tour):
    return list(zip(tour, tour[1:]+tour[:1]))


def edge_count(tour):
    return Counter(tuple(sorted(e)) for e in edges(tour))


def cost(tour, n):
    return times(F(1, n*n), plus(*(sqrt_interval(x*y) for x, y in edges(tour))))


def signed_fixtures(q_bounds, beta):
    tested = 0
    parities, lengths = set(), set()
    saw_wrap = False
    for n in (102, 103, 104, 105):
        k = (q_bounds[0]*n).__floor__()
        assert k == (q_bounds[1]*n).__floor__()
        natural = list(range(k, n+1))
        middle = len(natural)//2
        alternating = []
        for low, high in zip(natural[:middle], reversed(natural[-middle:])):
            alternating.extend((low, high))
        if len(natural) % 2:
            alternating.append(natural[middle])
        tours = [natural, natural[::2]+natural[1::2], alternating,
                 alternating[:middle][::-1]+alternating[middle:]]
        for tour in tours:
            assert sorted(tour) == natural and len(set(tour)) == len(tour)
            for order in (tour, tour[1:]+tour[:1], tour[::-1]):
                assert edge_count(order) == edge_count(tour)
                outer_edges = edges(order)
                s_int = n+k
                energy = sum(F((x+y-s_int)**2, n**3) for x, y in outer_edges)
                w0 = cost(order, n)
                jn = times(F(1, n*n), plus(*(sqrt_interval(x*(s_int-x)) for x in natural)))
                excess = minus(w0, jn)
                assert excess[0] >= 0 and energy <= 8*excess[0]
                # Exact two marginals of the reflected oriented measure.
                first, second = Counter(), Counter()
                for x, y in outer_edges:
                    first[x] += 1
                    first[y] += 1
                    second[s_int-y] += 1
                    second[s_int-x] += 1
                assert first == second == Counter({v: 2 for v in natural})
                for cut in beta:
                    ell = (cut*n).__floor__()
                    assert F(ell, n) > q_bounds[1] and ell <= n-2
                    keep = [x for x in order if x >= ell]
                    parities.add((len(order) % 2, len(keep) % 2))
                    w1 = cost(keep, n)
                    dn = times(F(1, n*n), plus(*(
                        minus((F(s_int-x),)*2, times(2, sqrt_interval(x*(s_int-x))))
                        for x in range(k, ell))))
                    # D_n = sum[(n+k-j)/n - 2 sqrt(j(n+k-j))/n]/n.
                    delta = minus(minus(w1, w0), dn)
                    first_variations = []
                    crossing = F(0)
                    midpoint = F(2*ell-1, 2)
                    for x, y in outer_edges:
                        for x1, y1 in ((x, y), (y, x)):
                            z = s_int-y1
                            if (x1-midpoint)*(z-midpoint) < 0:
                                crossing += F(abs(x1-z), 2*n*n)
                            if x1 < ell:
                                p = times(F(1, 2), minus((F(1), F(1)),
                                                       sqrt_interval(F(x1, s_int-x1))))
                                first_variations.append(times(F(x1+y1-s_int, n*n), p))
                    variation = plus(*first_variations)
                    assert abs_bound(minus(delta, variation)) <= 43*energy
                    assert abs_bound(variation) <= 11*energy+2*crossing
                    assert abs_bound(delta) <= 54*energy+2*crossing
                    # Recover every run independently from cyclic survivor indices.
                    positions = [i for i, x in enumerate(order) if x >= ell]
                    removed, inserted = Counter(), Counter()
                    bad_vertices = 0
                    for left, right in zip(positions, positions[1:]+[positions[0]+len(order)]):
                        if right == left+1:
                            continue
                        path = [order[i % len(order)] for i in range(left, right+1)]
                        m = len(path)-2
                        lengths.add(m)
                        saw_wrap |= right >= len(order)
                        if m >= 2:
                            bad_vertices += m
                        removed.update(tuple(sorted(e)) for e in zip(path, path[1:]))
                        inserted[tuple(sorted((path[0], path[-1])))] += 1
                    assert edge_count(order)+inserted == edge_count(keep)+removed
                    ll = sum(x < ell and y < ell for x, y in outer_edges)
                    assert bad_vertices <= 2*ll and F(ll, n) <= 4*energy
                    tested += 1
    assert tested == 144 and len(parities) == 4 and saw_wrap
    assert 1 in lengths and any(m >= 2 for m in lengths)
    print('PASS 144 directed-rational deletion fixtures: 43E, 11E+2K, 54E+2K, runs, seam, all parity pairs')


def check_manifest():
    manifest = json.loads((HERE/'MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['schema'] == 'ringmin-proposition7-manifest-v1'
    assert manifest['excluded_from_self_hash'] == ['MANIFEST.json']
    for name, digest in manifest['outputs'].items():
        path = HERE/name
        assert path.parent == HERE and path.is_file(), name
        assert sha256(path.read_bytes()).hexdigest() == digest, name
    actual = {p.name for p in HERE.iterdir() if p.is_file() and p.name != 'MANIFEST.json'}
    assert actual == set(manifest['outputs']), (actual, set(manifest['outputs']))
    # The standalone package verifies without any repository. If embedded at
    # the declared location, additionally verify every available source input.
    root = HERE.parents[2]
    checked = 0
    if (root/'AGENTS.md').is_file():
        for item in manifest['inputs']:
            path = root/item['path']
            assert sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest() == item['lf_normalized_sha256'], item['path']
            checked += 1
    print(f'PASS manifest: {len(actual)} output hashes; {checked} repository input hashes (LF-normalized inputs; 0 is valid standalone)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-certificate', action='store_true',
                        help='Regenerate certificate.json after all mathematical checks')
    parser.add_argument('--skip-manifest', action='store_true',
                        help='For authoring only: do not assert package integrity')
    args = parser.parse_args()
    w, certificate = parameters()
    signed_fixtures(w['Q'], w['BETA'])
    result = subprocess.run([sys.executable, '-I', '-S', str(HERE/'check_finite_crossing.py')],
                            capture_output=True, text=True, check=True)
    print(result.stdout, end='')
    path = HERE/'certificate.json'
    if args.write_certificate:
        path.write_text(json.dumps(certificate, indent=2, sort_keys=True)+'\n',
                        encoding='utf-8', newline='\n')
        print('WROTE certificate.json from exact rational computations')
    assert json.loads(path.read_text(encoding='utf-8')) == certificate
    print('PASS certificate equals fresh rational recomputation')
    if not args.skip_manifest:
        check_manifest()
    print('PASS supplement checks; analytic proof supplies universal quantifiers')


if __name__ == '__main__':
    main()
