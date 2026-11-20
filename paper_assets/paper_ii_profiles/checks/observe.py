"""Deterministic local-search observations for fixed power-profile line words."""

import argparse
import json
import math
import random
from pathlib import Path


def span(order, roots):
    coordinates = [0.0]
    for i in range(1, len(order)):
        s = roots[order[i]]
        best = coordinates[-1] + s * roots[order[i - 1]]
        j = i - 2
        while j >= 0 and coordinates[j] + s >= best:
            best = max(best, coordinates[j] + s * roots[order[j]])
            j -= 1
        coordinates.append(best)
    return coordinates[-1]


def search(n, power, moves, seed):
    rng = random.Random(seed)
    roots = [(i / n) ** (power / 2) for i in range(n + 1)]
    half = n // 2
    best_score = math.inf
    for offset in range(0, half, max(1, half // 64)):
        highs = list(range(half + 1 + offset, n + 1)) + list(range(half + 1, half + 1 + offset))
        word = [label for pair in zip(range(1, half + 1), highs) for label in pair]
        score = span(word, roots)
        if score < best_score:
            best_score, best = score, word
    if power:
        for step in range(moves):
            i = rng.randrange(n)
            if step % 4:
                j = (i + 2 * rng.randint(-max(2, half // 8), max(2, half // 8))) % n
            else:
                j = rng.randrange(n)
            if i == j:
                continue
            best[i], best[j] = best[j], best[i]
            score = span(best, roots)
            if score < best_score:
                best_score = score
            else:
                best[i], best[j] = best[j], best[i]
    return {"power": str(power), "n": n, "seed": seed, "moves": moves,
            "score": (best_score + 1) / (math.pi * n), "order": best}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=512)
    parser.add_argument("--moves", type=int, default=16000)
    parser.add_argument("--seed", type=int, default=20261119)
    parser.add_argument("--output", type=Path, help="write orders for the independent integer check")
    args = parser.parse_args()
    if args.n < 4 or args.n % 2 or args.moves < 0:
        parser.error("n must be even and at least four, and moves must be nonnegative")
    results = []
    for i, power in enumerate((0, 0.5, 1, 2, 3)):
        row = search(args.n, power, args.moves, args.seed + i)
        results.append(row)
        print(f"p={power} n={args.n} seed={row['seed']} score={row['score']:.10f}", flush=True)
    if args.output:
        args.output.write_text(json.dumps(results, separators=(",", ":")) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
