"""Convert searched orders to exact, portable certificates."""
import argparse
import json
from math import isqrt
from pathlib import Path


def positions_for(order, power):
    n = len(order)
    if sorted(order) != list(range(1, n + 1)) or power not in (1, 2):
        raise ValueError("expected a permutation and power 1 or 2")
    scale = 10**12
    denominator = n * scale if power == 1 else n**2
    points = []
    for i, label in enumerate(order):
        best = 0
        for j in range(i - 1, -1, -1):
            if points[j] + denominator <= best:
                break
            product = label * order[j]
            if power == 1:
                # ceil(sqrt(product)*scale), including the perfect-square case.
                gap = 1 + isqrt(product * scale**2 - 1)
            else:
                gap = product
            best = max(best, points[j] + gap)
        points.append(best)
    by_label = [0] * n
    for label, position in zip(order, points):
        by_label[label - 1] = position
    return by_label, denominator


def certificate(order, power, provenance):
    n = len(order)
    positions, denominator = positions_for(order, power)
    span = max(positions) - min(positions)
    # A provisional strict decimal ceiling. The verifier proves its own pi bound.
    pi_digits = 314159265358979323846
    places = 10**12
    upper = ((span + denominator) * places * 10**20
             // (n * denominator * pi_digits) + 1)
    return {
        "schema": "ringmin-line-v1", "power": power, "n": n,
        "order": order, "D": denominator, "positions": positions,
        "span_numerator": span, "B": [upper, places], "search": provenance,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("search_dir", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    inputs = sorted(args.search_dir.glob("p*_n*.json"))
    if not inputs:
        parser.error("no search orders found")
    args.destination.mkdir(parents=True, exist_ok=True)
    for source in inputs:
        run = json.loads(source.read_text(encoding="utf-8"))
        provenance = {key: run[key] for key in ("chosen", "attempts")}
        if len(run["order"]) != run["n"]:
            raise ValueError(f"size mismatch in {source.name}")
        data = certificate(run["order"], run["power"], provenance)
        dest = args.destination / source.name
        dest.write_text(json.dumps(data, separators=(",", ":")) + "\n",
                        encoding="utf-8", newline="\n")
        print(source.name, data["B"][0], "/", data["B"][1])


if __name__ == "__main__":
    main()
