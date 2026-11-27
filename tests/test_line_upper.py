"""Independent controls for the Paper II finite line certificates."""
from copy import deepcopy
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations
import json
from math import isqrt
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1] / "paper_assets" / "line_upper"


def module(name):
    spec = spec_from_file_location(name, ROOT / f"{name}.py")
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cli(path):
    return subprocess.run([sys.executable, "-I", "-S",
                           str(ROOT / "verify_line_certificate.py"), str(path)],
                          stdin=subprocess.DEVNULL, capture_output=True, text=True)


@pytest.mark.parametrize("case", ["position", "labels", "size", "bound", "truncated",
                                  "short_pair", "span", "bool", "duplicate"])
def test_rejects_tampering(case, tmp_path):
    data = json.loads((ROOT / "certificates" / "p1_n00006.json").read_text())
    assert cli(ROOT / "certificates" / "p1_n00006.json").returncode == 0
    positions, order = data["positions"], data["order"]
    if case == "position":
        positions[order[1]-1] = positions[order[0]-1]
    elif case == "labels":
        order[1], order[2] = order[2], order[1]
    elif case == "size":
        data["n"] += 1
    elif case == "bound":
        data["B"] = [1, 1000]
    elif case == "short_pair":
        # Preserve order and extrema; make the first interior separation tiny.
        positions[order[1]-1] = positions[order[0]-1]+1
    elif case == "span":
        data["span_numerator"] += 1
    elif case == "bool":
        data["power"] = True
    payload = json.dumps(data)
    if case == "truncated":
        payload = payload[:-3]
    elif case == "duplicate":
        payload = '{"power":1,' + payload[1:]
    sample = tmp_path / "altered.json"
    sample.write_text(payload, encoding="utf-8")
    result = cli(sample)
    assert result.returncode != 0 and "FAIL" in result.stderr


@pytest.mark.parametrize("n", [3, 4])
def test_exact_recurrence_against_all_grid_placements(n):
    generate = module("generate")
    # For quadratic marks use coordinates in units of 1/n^2. Increasing
    # integer placements suffice since the longest-path edge weights are integers.
    for order in permutations(range(1, n+1)):
        positions, d = generate.positions_for(order, 2)
        assert d == n*n
        got = max(positions)
        # Enumerate every shorter span and every interior placement on the grid.
        for span in range(n-1, got+1):
            feasible = any(all(x[j]-x[i] >= order[i]*order[j]
                               for i, j in combinations(range(n), 2))
                           for mid in combinations(range(1, span), n-2)
                           for x in [(0, *mid, span)])
            if feasible:
                break
        assert feasible and span == got


def test_linear_recurrence_against_all_increasing_paths():
    generate = module("generate")
    for order in permutations(range(1, 6)):
        coordinates, d = generate.positions_for(order, 1)
        scale = d // 5
        def gap(a, b):
            v = a*b*scale**2
            root = isqrt(v)
            return root if root*root == v else root+1
        longest = max(sum(gap(order[a], order[b]) for a, b in zip(path, path[1:]))
                      for k in range(4)
                      for middle in combinations(range(1, 4), k)
                      for path in [(0, *middle, 4)])
        assert max(coordinates) == longest


def test_all_pairs_includes_nonadjacent_constraint():
    verify = module("verify_line_certificate")
    # For labels 2,1,3 two adjacent quadratic gaps equal 2 and 3.
    # The omitted 2,3 separation needs 6 units.
    bad = {"schema":"ringmin-line-v1", "n":3, "power":2, "D":9,
           "order":[2,1,3], "positions":[2,0,5], "span_numerator":5, "B":[1,1]}
    with pytest.raises(ValueError, match="2,3"):
        verify.verify(bad)
    good = deepcopy(bad)
    good.update(positions=[2,0,6], span_numerator=6)
    verify.verify(good)


def test_block_enclosures_overlap_and_meet_target():
    pytest.importorskip("flint", reason="Arb is needed for the antiderivative cross-check")
    analytic = module("block_antiderivatives")
    independent = module("verify_block_subdivision")
    l, u = analytic.endpoints(analytic.cost(), 14)
    lo, hi, _ = independent.enclose()
    a, b = Fraction(l, 10**14), Fraction(u, 10**14)
    assert max(a, lo) <= min(b, hi)
    assert 0 < hi-lo <= Fraction(1, 10**9)
    assert 0 < b-a <= Fraction(1, 10**9)
