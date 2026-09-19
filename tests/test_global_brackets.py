"""Independent small oracles and rehashed falsifications of the complete verifier.

No production solver or original generator is imported. Archived invalid inputs
are only fixtures; the false n=4 bracket is independently excluded at its U.
"""

from __future__ import annotations

import copy
import importlib.util
import inspect
import itertools
import json
import math
from pathlib import Path
import random
import subprocess
import sys
from fractions import Fraction as F

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "global_brackets", ROOT / "verify_global_brackets.py"
)
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)
ORIGINALS = ROOT / "reproducibility/global_brackets/originals"


@pytest.fixture(scope="module")
def original():
    return v.read(ORIGINALS / "source/ringmin_global_interval_candidate.json")


@pytest.fixture(scope="module")
def checked(original):
    return v.verify(original)


def rehash(report):
    report["certificate_sha256"] = v.sha(v.canonical(report["certificate"]))
    return report


def mutate(original, change):
    report = copy.deepcopy(original)
    change(report["certificate"])
    return rehash(report)


def row_weights(row, endpoint="L"):
    n = row["n"]
    weights = [[0] * (n + 1) for _ in range(n + 1)]
    for e in row["angle_intervals_scaled"]:
        a, b = e["a"], e["b"]
        weights[a][b] = weights[b][a] = int(e[endpoint + "_lower"])
    return weights


def test_complete_original_and_pins(original, checked):
    v.verify_pinned_inputs(original)
    assert v.verify_archive() == 13
    cases = original["certificate"]["cases"]
    assert checked["all_order_classes_covered"] == sum(
        math.factorial(n - 1) // 2 for n in range(3, 15)
    )
    assert checked["angles_verified_by_cosine"] == 2 * sum(
        math.comb(n, 2) for n in range(3, 15)
    )
    assert checked["witnesses"] == sum(len(r["upper_witnesses"]) for r in cases)
    for result in checked["cases"]:
        assert (
            0
            < F(result["strict_lower_radius_buffer"])
            < F(result["U"]) - F(result["L"])
        )
        assert result["geometry"]["witnesses"] >= 1
    # All source-derived proof metadata is compared; historical runtime is not.
    w = v.read(
        ORIGINALS / "source/global_interval_replay_20260917T101809Z_3399172f.json"
    )
    assert w["certificate"] == original["certificate"]


@pytest.mark.parametrize(
    "name,total",
    [
        ("FALSE_n4_bracket_empty_witness", 46),
        ("FALSE_n4_bracket_47_total_witnesses", 47),
    ],
)
def test_false_bracket_with_correct_rehashed_lower_evidence(name, total):
    report = v.read(
        ORIGINALS / "tests/adversarial_run" / name / "DELIBERATELY_INVALID_windows.json"
    )
    assert rehash(copy.deepcopy(report)) == report
    c = report["certificate"]
    assert sum(len(r["upper_witnesses"]) for r in c["cases"]) == total
    row = c["cases"][1]
    assert F(row["L"]) == F(1, 2) and F(row["U"]) == F("0.50000000001")
    for e in row["angle_intervals_scaled"]:
        for end in ("L", "U"):
            q = F(e["a"] * e["b"]) / ((F(row[end]) + e["a"]) * (F(row[end]) + e["b"]))
            v.verify_angle(q, int(e[end + "_lower"]), int(e[end + "_upper"]))
    v.verify_lower_metadata(
        row, v.audit_lower(4, row_weights(row), int(c["tau_upper_scaled"]))
    )
    # Independent direct three-cycle oracle at the FALSE upper bound.
    W = row_weights(row, "U")
    cycles = [(4,) + p for p in itertools.permutations((1, 2, 3)) if p < p[::-1]]
    assert len(cycles) == 3
    assert all(
        sum(W[s[i]][s[(i + 1) % 4]] for i in range(4)) > int(c["tau_upper_scaled"])
        for s in cycles
    )
    with pytest.raises(ValueError, match="MISSING existential upper witness n=4"):
        v.verify(report)  # No historic digest or endpoint pin is involved.


def test_missing_witness_rehashed(original):
    bad = mutate(original, lambda c: c["cases"][1].update(upper_witnesses=[]))
    with pytest.raises(ValueError, match="MISSING existential"):
        v.verify(bad)


def test_one_grid_unit_false_interval_with_recomputed_lower():
    report = v.read(
        ORIGINALS
        / "tests/adversarial_run/one_ulp_false_L_angle_rehashed/DELIBERATELY_INVALID_windows.json"
    )
    assert rehash(copy.deepcopy(report)) == report
    row = report["certificate"]["cases"][0]
    v.verify_lower_metadata(
        row,
        v.audit_lower(
            3, row_weights(row), int(report["certificate"]["tau_upper_scaled"])
        ),
    )
    with pytest.raises(ValueError, match="false angular LOWER endpoint"):
        v.verify(report)


@pytest.mark.parametrize(
    "change,reason",
    [
        (
            lambda c: c["cases"][1]["angle_intervals_scaled"][0].update(
                U_lower="0", U_upper="1"
            ),
            "angle interval",
        ),
        (
            lambda c: c["cases"][1]["upper_witnesses"][0]["exact_cartesian_check"][
                "stereographic_parameters"
            ].__setitem__(1, {"numerator": "0", "denominator": "1"}),
            "Cartesian polar order",
        ),
        (lambda c: c["cases"].pop(), "case coverage"),
        (
            lambda c: c["cases"].__setitem__(1, copy.deepcopy(c["cases"][0])),
            "case coverage",
        ),
        (
            lambda c: c["cases"][1]["lower_bound"].update(canonical_orders_covered=0),
            "lower metadata",
        ),
        (
            lambda c: c["cases"][0]["lower_bound"].update(
                canonical_orders_covered=True
            ),
            "lower metadata",
        ),
        (
            lambda c: c["cases"][1]["angle_intervals_scaled"].pop(),
            "pair table completeness",
        ),
        (
            lambda c: c["cases"][0]["upper_witnesses"].append(
                copy.deepcopy(c["cases"][0]["upper_witnesses"][0])
            ),
            "duplicate witness",
        ),
        (
            lambda c: c["cases"][0]["upper_witnesses"][0]["order"].__setitem__(1, 3),
            "witness radius set",
        ),
        (
            lambda c: c["cases"][0]["upper_witnesses"][0][
                "positions_scaled_integers"
            ].__setitem__(1, "1"),
            "angular slack",
        ),
        (lambda c: c.update(model="adjacency only"), "model/version"),
        (lambda c: c.update(version="0.2.0"), "model/version"),
        (
            lambda c: c.update(
                tau_lower_scaled=c["tau_upper_scaled"],
                tau_upper_scaled=str(int(c["tau_upper_scaled"]) + 1),
            ),
            "tau upper|tau lower|tau location",
        ),
        (lambda c: c["cases"][0].update(L=0.25), "decimal"),
        (lambda c: c["cases"][0].update(n=True), "case n domain"),
        (
            lambda c: c["cases"][0]["upper_witnesses"][0]["exact_cartesian_check"][
                "stereographic_parameters"
            ][0].update(denominator="0"),
            "parameter denominator",
        ),
    ],
)
def test_rehashed_content_mutations(original, change, reason):
    with pytest.raises(ValueError, match=reason):
        v.verify(mutate(original, change))


@pytest.mark.parametrize(
    "key",
    ["dp_table_sha256", "pruning_and_skeleton_stream_sha256", "skeleton_vertices"],
)
def test_p2_derived_metadata_rehashed(original, checked, key):
    row = copy.deepcopy(original["certificate"]["cases"][-1])
    row["lower_bound"][key] = [] if key == "skeleton_vertices" else "0" * 64
    # Use the independently recomputed n=14 table/stream, not historical pins.
    with pytest.raises(ValueError, match="lower metadata"):
        v.verify_lower_metadata(row, checked["cases"][-1]["lower"])


def test_p2_dp_and_pruning_rehashed_end_to_end(original):
    bad = mutate(
        original,
        lambda c: c["cases"][-1]["lower_bound"].update(
            dp_table_sha256="0" * 64, pruning_and_skeleton_stream_sha256="0" * 64
        ),
    )
    with pytest.raises(ValueError, match="lower metadata n=14"):
        v.verify(bad)


def test_input_binding_is_separate_from_mathematics(original):
    bad = mutate(original, lambda c: c.update(input_cases_sha256="0" * 64))
    assert v.verify(bad)["status"] == "PASS_GLOBAL_BRACKETS"
    with pytest.raises(ValueError, match="CASES input digest binding"):
        v.verify_pinned_inputs(bad)


def test_pinned_orders_and_row_counts(original):
    # Same total but different row counts and orders is not original reproduction.
    bad = mutate(
        original, lambda c: c["cases"][0]["upper_witnesses"][0]["order"].reverse()
    )
    with pytest.raises(ValueError, match="CASES endpoints/orders binding"):
        v.verify_pinned_inputs(bad)
    bad = copy.deepcopy(original)
    moved = bad["certificate"]["cases"][9]["upper_witnesses"].pop()
    bad["certificate"]["cases"][10]["upper_witnesses"].append(moved)
    rehash(bad)
    with pytest.raises(ValueError, match="CASES endpoints/orders binding"):
        v.verify_pinned_inputs(bad)


def test_complete_minimum_witness_contract(original):
    # One witness per row suffices mathematically; all 47 are required for pins.
    bad = copy.deepcopy(original)
    for row in bad["certificate"]["cases"]:
        row["upper_witnesses"] = row["upper_witnesses"][:1]
    rehash(bad)
    assert v.verify(bad)["witnesses"] == 12
    with pytest.raises(ValueError, match="CASES endpoints/orders binding"):
        v.verify_pinned_inputs(bad)


@pytest.mark.parametrize("text", ['{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'])
def test_strict_json(tmp_path, text):
    p = tmp_path / "bad.json"
    p.write_text(text)
    with pytest.raises(ValueError):
        v.read(p)


def test_forward_dp_against_all_small_directed_paths():
    rng = random.Random(20260919)
    for m in range(1, 7):
        vertices = tuple(range(1, m + 1))
        for rep in range(6):
            W = [[0] * (m + 1) for _ in range(m + 1)]
            for a, b in itertools.combinations(range(m + 1), 2):
                W[a][b] = rng.randrange(1, 100)
                W[b][a] = W[a][b] if rep < 3 else rng.randrange(1, 100)
            D, root = v.forward_dp(vertices, 0, W)
            for mask in range(1, 1 << m):
                members = [j for j in range(m) if mask >> j & 1]
                for j in members:
                    remaining = [vertices[k] for k in members if k != j]
                    costs = []
                    for p in itertools.permutations(remaining):
                        seq = (0,) + p + (vertices[j],)
                        costs.append(sum(W[a][b] for a, b in zip(seq, seq[1:])))
                    assert D[mask, j] == min(costs)
            assert root == min(
                sum(W[a][b] for a, b in zip((0,) + p, p + (0,)))
                for p in itertools.permutations(vertices)
            )


def canonical_oracle(seq):
    # Lexicographically smallest among ALL rotations and both orientations;
    # this deliberately does not use the verifier's max-anchor normalization.
    s = tuple(seq)
    r = s[::-1]
    return min(
        [s[i:] + s[:i] for i in range(len(s))] + [r[i:] + r[:i] for i in range(len(r))]
    )


def small_coverage_oracle(n, W, T, walk=v.skeleton_cover):
    observed = []
    result = walk(n, W, T, lambda seq: observed.append(canonical_oracle(seq)))
    expected = set()
    for p in itertools.permutations(range(1, n)):
        if p > p[::-1]:
            continue
        full = (n,) + p
        skel = tuple(x for x in full if x != 1)
        cost = sum(W[skel[i]][skel[(i + 1) % len(skel)]] for i in range(len(skel)))
        if cost <= T:
            expected.add(canonical_oracle(full))
    assert len(observed) == len(set(observed))
    assert set(observed) == expected
    assert result["explicit_full_orders_checked"] == len(expected)


def test_small_pruning_and_every_cyclic_insertion_gap():
    rng = random.Random(20260919)
    for n in range(4, 10):
        W = [[0] * (n + 1) for _ in range(n + 1)]
        for a, b in itertools.combinations(range(1, n + 1), 2):
            W[a][b] = W[b][a] = rng.randrange(1, 100)
        costs = []
        for p in itertools.permutations(range(2, n)):
            s = (n,) + p
            costs.append(sum(W[s[i]][s[(i + 1) % len(s)]] for i in range(len(s))))
        costs.sort()
        for T in set([costs[0] - 1, costs[0], costs[len(costs) // 2], costs[-1]]):
            small_coverage_oracle(n, W, T)


def mutated_walk(old, new):
    source = inspect.getsource(v.skeleton_cover)
    assert source.count(old) == 1
    namespace = dict(vars(v))
    exec(compile(source.replace(old, new), "<test-only-mutant>", "exec"), namespace)
    return namespace["skeleton_cover"]


def test_equality_overpruning_mutant_fails_set_oracle():
    n = 6
    W = [[int(a != b) for b in range(n + 1)] for a in range(n + 1)]
    small_coverage_oracle(n, W, n - 1)
    bad = mutated_walk("if bound > T:", "if bound >= T:")
    # The wrong branch can still satisfy factorial counts, so require the set.
    with pytest.raises(AssertionError):
        small_coverage_oracle(n, W, n - 1, bad)


def test_missing_final_insertion_gap_mutant_is_rejected():
    n = 6
    W = [[int(a != b) for b in range(n + 1)] for a in range(n + 1)]
    bad = mutated_walk("range(len(seq))", "range(len(seq) - 1)")
    with pytest.raises(ValueError, match="insertion count"):
        small_coverage_oracle(n, W, n - 1, bad)


def test_skeleton_refuses_asymmetric_reverse_completion():
    W = [[int(a != b) for b in range(6)] for a in range(6)]
    W[2][3] = 10
    with pytest.raises(ValueError, match="symmetric"):
        v.skeleton_cover(5, W, 100, lambda seq: None)


def exact_cos_bounds(x, terms=160):
    # Exact Fraction sum and signed tail, no fixed-point recurrence.
    partial = sum(
        (-1) ** k * x ** (2 * k) / math.factorial(2 * k) for k in range(terms)
    )
    next_term = x ** (2 * terms) / math.factorial(2 * terms)
    return (
        (partial, partial + next_term)
        if terms % 2 == 0
        else (partial - next_term, partial)
    )


def test_cosine_against_exact_rational_oracle():
    rng = random.Random(20260919)
    xs = [F(0), F(1, 7), F(1), F(3, 2), F(2), F(3), F(4)]
    xs += [F(rng.randrange(1, 4001), 1000) for _ in range(15)]
    for x in xs:
        lo, hi = exact_cos_bounds(x)
        for terms in (112, 113):
            a, b = v.cos_bounds(x, terms)
            assert F(a, v.B) <= lo <= hi <= F(b, v.B)


@pytest.mark.parametrize("q", [F(-1), F(0), F(9, 10), F(1), F(2)])
def test_invalid_angle_domains(q):
    with pytest.raises(ValueError, match="q domain"):
        v.verify_angle(q, 1, 2)


def test_isolated_stdlib_cli_has_no_generator_or_production_dependency(tmp_path):
    p = tmp_path / "verify_global_brackets.py"
    p.write_bytes((ROOT / "verify_global_brackets.py").read_bytes())
    run = subprocess.run(
        [
            sys.executable,
            "-I",
            "-S",
            str(p),
            "--mathematical-only",
            "--certificate",
            str(ORIGINALS / "source/ringmin_global_interval_candidate.json"),
        ],
        cwd=tmp_path,
        stdin=subprocess.DEVNULL,
        text=True,
        capture_output=True,
        timeout=90,
    )
    assert run.returncode == 0, run.stderr
    result = json.loads(run.stdout)
    assert result["pinned_input_verification"] == "NOT_CHECKED"
    assert result["witnesses"] == 47
    assert not (tmp_path / "reproducibility").exists()


def test_cli_failure_is_nonzero_without_pass_output(tmp_path, original):
    path = tmp_path / "invalid.json"
    path.write_text(
        json.dumps(mutate(original, lambda c: c["cases"][1].update(upper_witnesses=[])))
    )
    run = subprocess.run(
        [
            sys.executable,
            "-I",
            "-S",
            str(ROOT / "verify_global_brackets.py"),
            "--mathematical-only",
            "--certificate",
            str(path),
        ],
        text=True,
        capture_output=True,
        timeout=20,
        stdin=subprocess.DEVNULL,
    )
    assert run.returncode == 1
    assert "MISSING existential upper witness n=4" in run.stderr
    assert "PASS_GLOBAL_BRACKETS" not in run.stdout
