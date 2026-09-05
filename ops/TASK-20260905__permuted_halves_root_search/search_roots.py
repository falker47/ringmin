"""Bounded exhaustive high-permutation root experiment; numerical only.

No production/verifier/prior-checker imports. Always starts at m=2 and
stops at the first robust counterexample size, with the hard ceiling m=8.
Run from the repository root. Writes only this dossier's numerical JSON.
"""

import hashlib
import itertools
import json
import math
from pathlib import Path
import platform

import mpmath as mp


DPS = 80
STEPS = 240
GUARD = '1e-60'
BASE_HEAD = '1636bf23cfadac46fb785bf6b1afda7e2787a466'


def score(radius, order):
    def theta(a, b):
        return 2*mp.asin(mp.sqrt(a*b/((radius+a)*(radius+b))))

    return mp.fsum(max(theta(i, order[i-2])+theta(i, order[i-1]),
                       theta(order[i-2], order[i-1]))
                   for i in range(1, len(order)+1))


def root(order):
    lo, hi = mp.mpf('0.01'), mp.mpf(4*len(order)**2)
    target = 2*mp.pi
    assert score(lo, order) > target > score(hi, order)
    for _ in range(STEPS):
        mid = (lo+hi)/2
        if score(mid, order) > target:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main():
    mp.mp.dps = DPS
    guard = mp.mpf(GUARD)
    data = dict(schema='ringmin.permuted-halves-roots.v1',
                classification='numerical observation; non-rigorous brackets',
                base_head=BASE_HEAD, python=platform.python_version(),
                mpmath=mp.__version__, dps=DPS, bisections=STEPS,
                comparison_guard=GUARD, requested_m=[2, 8],
                enumeration='itertools.permutations; no quotient or pruning',
                seed=None, source_sha256=hashlib.sha256(
                    Path(__file__).read_bytes()).hexdigest(), sizes=[])
    for m in range(2, 9):
        rows = []
        for order in itertools.permutations(range(m+1, 2*m+1)):
            lo, hi = root(order)
            rows.append(dict(order=list(order), lo=mp.nstr(lo, 78),
                             hi=mp.nstr(hi, 78)))
        assert len(rows) == math.factorial(m)
        assert len({tuple(row['order']) for row in rows}) == len(rows)
        shifts = {tuple(m+1+(i+s) % m for i in range(m)) for s in range(m)}
        mid = lambda row: (mp.mpf(row['lo'])+mp.mpf(row['hi']))/2
        best = min(map(mid, rows))
        best_shift = min(mid(row) for row in rows if tuple(row['order']) in shifts)
        gap = best_shift-best
        entry = dict(m=m, permutations=len(rows), shifts=len(shifts),
                     best_orders=[r['order'] for r in rows if abs(mid(r)-best) < guard],
                     best_shift_orders=[r['order'] for r in rows
                                        if tuple(r['order']) in shifts
                                        and abs(mid(r)-best_shift) < guard],
                     best_root=mp.nstr(best, 65),
                     best_shift_root=mp.nstr(best_shift, 65),
                     shift_minus_arbitrary=mp.nstr(gap, 65), rows=rows)
        data['sizes'].append(entry)
        print(f"m={m} permutations={len(rows)} best={mp.nstr(best, 32)} "
              f"shift={mp.nstr(best_shift, 32)} gap={mp.nstr(gap, 12)}", flush=True)
        print('  best_orders=', entry['best_orders'],
              'best_shift_orders=', entry['best_shift_orders'], flush=True)
        data['stop_reason'] = ('first robust numerical counterexample'
                               if gap > guard else 'hard ceiling m=8' if m == 8
                               else 'in progress')
        Path(__file__).with_name('roots.json').write_text(
            json.dumps(data, indent=2)+'\n', encoding='utf-8')
        if gap > guard:
            break
    print('STOP:', data['stop_reason'], 'at m=', m, flush=True)


if __name__ == '__main__':
    main()
