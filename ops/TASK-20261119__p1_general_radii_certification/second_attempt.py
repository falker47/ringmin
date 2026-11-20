"""Independent finite oracles for the general-radii coverage and graph checks."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
import json
from math import factorial
from pathlib import Path
from random import Random
from runpy import run_path

PACKAGE = Path(__file__).resolve().parents[2] / "paper_assets" / "general_radii"


def outcome(classify, order, weights, period):
    try:
        return classify(order, weights, period)
    except ValueError as exc:
        if "unresolved order" not in str(exc):
            raise
        return "feasible"


def matrix(n, pairs, values):
    weights = [[0] * n for _ in range(n)]
    for (i, j), value in zip(pairs, values, strict=True):
        weights[i][j] = weights[j][i] = value
    return weights


def integer_circle(classify):
    # Integer right-hand sides make rounding all feasible potentials down safe.
    rng = Random(20261120)
    counts = Counter()
    for n in range(3, 7):
        order = tuple(range(n))
        pairs = list(combinations(order, 2))
        for period in range(4, 8):
            signatures = []
            for tail in combinations_with_replacement(range(period+1), n-1):
                x = (0, *tail)
                signatures.append(tuple(min(x[j]-x[i], period-x[j]+x[i]) for i, j in pairs))
            if n <= 4:
                trials = product(range(3), repeat=len(pairs))
            else:
                trials = (tuple(rng.randrange(1+period//2) for _ in pairs) for _ in range(320))
            for values in trials:
                possible = any(all(a <= b for a, b in zip(values, actual))
                               for actual in signatures)
                result = outcome(classify, order, matrix(n, pairs, values), period)
                assert possible == (result == "feasible")
                counts[result] += 1
    return counts


def pentagram(classify):
    pairs = list(combinations(range(5), 2))
    weights = matrix(5, pairs, [1 if (i-j) % 5 in (1, 4) else 3 for i, j in pairs])
    costs = []
    for size in range(3, 6):
        for cycle in combinations(range(5), size):
            costs.append(sum(weights[i][j] for i, j in zip(cycle, cycle[1:] + cycle[:1])))
    assert len(costs) == 16 and max(costs) == 7
    assert outcome(classify, tuple(range(5)), weights, 7) == "graph_exclusions"
    assert outcome(classify, tuple(range(5)), weights, 8) == "feasible"


def canonical_core(word, dropped):
    core = tuple(x for x in word if x >= dropped)
    pivot = core.index(min(core))
    rotated = core[pivot:] + core[:pivot]
    return min(rotated, (rotated[0], *reversed(rotated[1:])))


def fibres(audit):
    instances = projections = surviving = 0
    for n in (8, 9):
        pairs = [(i, j) for i in range(n) for j in range(i)]
        words = [(0, *p) for p in permutations(range(1, n)) if p[0] < p[-1]]
        for family in ("linear", "quadratic"):
            file = PACKAGE / "certificates" / f"{family}_{n:02}.json"
            data = json.loads(file.read_text(encoding="utf-8"))
            weights = matrix(n, pairs, data["angle_lower"])
            period = data["tau_upper"]
            for dropped in (2, 3, 4, n-3):
                k = n-dropped
                multiplicity = factorial(n-1)//factorial(k-1)
                cores = Counter(canonical_core(word, dropped) for word in words)
                assert len(cores) == factorial(k-1)//2
                assert set(cores.values()) == {multiplicity}
                kept = sum(count for core, count in cores.items()
                           if sum(weights[i][j] for i, j in zip(core, core[1:]+core[:1])) <= period)
                got = audit(weights, period, dropped)
                assert got["explicit"] == kept and got["full_classes"] == len(words)
                assert got["pruned_oriented"]*multiplicity == 2*(len(words)-kept)
                instances += 1
                projections += len(words)
                surviving += kept
    return instances, projections, surviving


if __name__ == "__main__":
    target = run_path(str(PACKAGE / "verify_radii_certificate.py"), run_name="comparison")
    result = integer_circle(target["classify_order"])
    print("DISCRETE_CIRCLE_ORACLE", result.total(), dict(result))
    pentagram(target["classify_order"])
    print("PENTAGRAM 16 induced subsets, period 7 excluded, period 8 feasible")
    print("AUTHENTIC_CORE_FIBRES", *fibres(target["lower_audit"]))
