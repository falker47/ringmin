"""Small exhaustive oracles and negative controls for distinct-radii certificates."""
import copy
import importlib.util
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "paper_assets/general_radii"
CERTS = ASSETS / "certificates"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ASSETS / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gen = load("certify_radii")
ind = load("verify_radii_certificate")


def canonical(order):
    rotations = [order[j:] + order[:j] for j in range(len(order))]
    return min(rotations + [r[::-1] for r in rotations])


def cycle(order, weights):
    return sum(weights[a][b] for a, b in zip(order, order[1:] + order[:1]))


def cost_matrix(n):
    return [[0 if i == j else 1+((i+j+1)*(abs(i-j)+3) % 13)
             for j in range(n)] for i in range(n)]


@pytest.mark.parametrize("n", [3, 4, 5, 6, 7])
def test_deletion_and_insertion_are_exact_inverses_mod_dihedral(n):
    W = cost_matrix(n)
    universe = {canonical(p) for p in itertools.permutations(range(n))}
    for d in range(n-2):
        core = tuple(range(d, n))
        thresholds = sorted({cycle((core[-1],) + r, W)
                             for r in itertools.permutations(core[:-1])})
        for T in {thresholds[0]-1, thresholds[len(thresholds)//2], thresholds[-1]}:
            expected = {word for word in universe if cycle(tuple(i for i in word if i >= d), W) <= T}
            counts = dict(pruned_oriented=0, retained_cores=0, reverse_leaves=0)
            by_slots = []
            by_insertion = []
            for retained in gen.skeletons(core, W, T, counts):
                by_slots.extend(map(canonical, ind.full_orders(retained, d)))
                by_insertion.extend(map(canonical, gen.insertions(retained, d)))
            assert set(by_slots) == set(by_insertion) == expected
            assert len(by_slots) == len(by_insertion) == len(expected)
            assert counts["reverse_leaves"] == counts["retained_cores"]
            assert counts["pruned_oriented"] + 2*counts["retained_cores"] == math.factorial(n-d-1)


@pytest.mark.parametrize("m", [2, 3, 4, 5, 6])
def test_bellman_completion_matches_permutations_for_every_state(m):
    W = cost_matrix(m+1)
    vertices = tuple(range(m))
    suffix = gen.completion_dp(vertices + (m,), W)
    forward = ind.forward_table(vertices, m, W)
    for j in vertices:
        for mask in range(1 << m):
            if mask & (1 << j):
                continue
            remaining = [v for v in vertices if mask >> v & 1]
            costs = []
            for p in itertools.permutations(remaining):
                path = (j,) + p + (m,)
                costs.append(sum(W[a][b] for a, b in zip(path, path[1:])))
            assert min(costs) == suffix(j, mask) == forward[mask | (1 << j), j]


@pytest.mark.parametrize("mutation", ["angle", "period", "radii", "duplicate", "depth",
                                       "position", "order", "upper", "strictness", "coverage", "truncated"])
def test_mutations_fail_closed(mutation):
    data = json.loads((CERTS / "quadratic_07.json").read_bytes())
    original = copy.deepcopy(data)
    if mutation == "angle":
        data["angle_lower"][0] = 3 << data["bits"]
    elif mutation == "period":
        data["tau_upper"] = 6 << data["bits"]
    elif mutation == "radii":
        data["radii"][0] = True
    elif mutation == "duplicate":
        data["radii"][0] = data["radii"][1]
    elif mutation == "depth":
        data["deleted"] = len(data["radii"])-2
    elif mutation == "position":
        data["stereographic"][1] = data["stereographic"][0]
    elif mutation == "order":
        data["order"][0] = data["order"][1]
    elif mutation == "upper":
        data["upper"] = data["lower"]
    elif mutation == "strictness":
        data["strict_buffer"] = "1"
    elif mutation == "coverage":
        data["coverage"]["explicit"] += 1
    else:
        data["angle_lower"].pop()
    assert json.dumps(original) != json.dumps(data)
    with pytest.raises(ValueError):
        ind.verify(data)


def test_positive_cycle_outside_prefix_family():
    # Ascending noncontiguous triangle (0, 2, 4) has cost 12 > 10; all
    # full and prefix-deletion cycles have cost <= 10.
    W = [[0 if i == j else 1 for j in range(5)] for i in range(5)]
    for i, j in [(0, 2), (2, 4), (0, 4)]:
        W[i][j] = W[j][i] = 4
    order = tuple(range(5))
    assert not gen.positive_prefix_cycle(order, W, 10)
    assert gen.potentials(order, W, 10) is None
    assert ind.classify_order(order, W, 10) == "graph_exclusions"


def test_uncertified_relaxed_order_is_rejected():
    W = [[0 if a == b else 1 for a in range(4)] for b in range(4)]
    with pytest.raises(ValueError, match="unresolved order"):
        ind.classify_order(tuple(range(4)), W, 8)


def test_custom_radii_and_scaling():
    custom = (2, 5, 17, 38)
    a = gen.make_certificate(custom, 1, bits=104, digits=6)
    ind.verify(a)
    bounds = (3*Fraction(a["lower"]), 3*Fraction(a["upper"]))
    b = gen.make_certificate(tuple(3*r for r in custom), 0, bits=104,
                             endpoints=bounds, proposal=tuple(custom.index(x) for x in a["order"]))
    ind.verify(b)
    assert Fraction(b["upper"]) == 3*Fraction(a["upper"])


def test_exact_grid_optimum_gets_strict_upper_witness():
    # Scaling (1,2,3) by 23 makes its Descartes central radius exactly 6.
    cert = gen.make_certificate((23, 46, 69), 0, digits=5)
    ind.verify(cert)
    assert Fraction(cert["lower"]) < 6 < Fraction(cert["upper"])


def test_quadratic_external_brackets_and_published_regression():
    source = ROOT / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
    cases = json.loads(source.read_bytes())["certificate"]["cases"]
    assert {r["n"] for r in cases} == set(range(3, 15))
    for row in cases:
        n = row["n"]
        data = json.loads((CERTS / f"linear_{n:02}.json").read_bytes())
        assert data["radii"] == list(range(1, n+1))
        assert (Fraction(data["lower"]), Fraction(data["upper"])) == (Fraction(row["L"]), Fraction(row["U"]))
    for n in range(3, 15):
        data = json.loads((CERTS / f"quadratic_{n:02}.json").read_bytes())
        assert data["radii"] == [j*j for j in range(1, n+1)]
        assert Fraction(data["upper"])-Fraction(data["lower"]) == Fraction(1, 10**11)
    old = [(3, "0.3832870361", "0.3834870362"), (4, "1.4955284118", "1.4957284119"),
           (5, "3.9342277171", "3.9344277172"), (6, "8.4678350760", "8.4680350761")]
    for n, lower, upper in old:
        data = json.loads((CERTS / f"quadratic_{n:02}.json").read_bytes())
        assert Fraction(lower) < Fraction(data["lower"]) < Fraction(data["upper"]) < Fraction(upper)


def test_isolated_cli_rejects_truncated_json(tmp_path):
    bad = tmp_path / "truncated.json"
    bad.write_bytes((CERTS / "quadratic_03.json").read_bytes()[:-5])
    result = subprocess.run([sys.executable, "-I", "-S", str(ASSETS / "verify_radii_certificate.py"),
                             str(bad)], cwd=tmp_path, stdin=subprocess.DEVNULL, capture_output=True, text=True, check=False)
    assert result.returncode == 1 and "FAIL" in result.stderr


def test_linear_generator_reproduces_tracked_certificate_from_a_clean_checkout(tmp_path):
    output = tmp_path / "linear_03.json"
    subprocess.run([sys.executable, str(ASSETS / "certify_radii.py"), "--linear", "3",
                    "--output", str(output)], cwd=tmp_path, stdin=subprocess.DEVNULL, check=True)
    assert json.loads(output.read_bytes()) == json.loads((CERTS / output.name).read_bytes())
