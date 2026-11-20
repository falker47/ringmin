"""Standalone exact all-pairs verifier for a rational Ringmin line placement."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def pi_lower():
    # Odd partial sums of atan(1/q) end positive (upper bounds); even sums
    # end negative (lower bounds). Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    def partial(q, terms):
        return sum(Fraction((-1)**j, (2*j + 1) * q**(2*j + 1))
                   for j in range(terms))
    return 16 * partial(5, 32) - 4 * partial(239, 11)


def integers(values, length, name):
    require(type(values) is list and len(values) == length,
            f"{name} must have {length} entries")
    require(all(type(x) is int for x in values), f"noninteger in {name}")
    return values


def verify(data):
    require(type(data) is dict and data.get("schema") == "ringmin-line-v1",
            "unknown certificate schema")
    n, power, denominator = (data.get(k) for k in ("n", "power", "D"))
    require(type(n) is int and n >= 2, "invalid n")
    require(type(power) is int and power in (1, 2), "invalid power")
    require(type(denominator) is int and denominator > 0, "invalid denominator")
    order = integers(data.get("order"), n, "order")
    require(sorted(order) == list(range(1, n+1)), "order is not a permutation")
    coordinates = integers(data.get("positions"), n, "positions")
    ordered = [coordinates[k-1] for k in order]
    require(ordered[0] == 0 and all(x < y for x, y in zip(ordered, ordered[1:])),
            "origin or order disagrees with label-indexed positions")
    span = max(coordinates) - min(coordinates)
    require(type(data.get("span_numerator")) is int and data["span_numerator"] == span,
            "incorrect span")
    numerator, divisor = integers(data.get("B"), 2, "B")
    require(numerator > 0 and divisor > 0, "bound must be positive")

    n2, d2 = n*n, denominator*denominator
    for i, xi in enumerate(coordinates, start=1):
        for j in range(i+1, n+1):
            difference = abs(xi - coordinates[j-1])
            if power == 1:
                valid = n2 * difference**2 >= i*j*d2
            else:
                valid = n2 * difference >= i*j*denominator
            if not valid:
                raise ValueError(f"short separation for labels {i},{j}")
    lower = pi_lower()
    require((span+denominator) * divisor * lower.denominator
            < denominator * n * numerator * lower.numerator, "B is too small")
    return n, power, span, denominator, numerator, divisor


def unique_object(entries):
    obj = {}
    for key, value in entries:
        require(key not in obj, f"duplicate key {key}")
        obj[key] = value
    return obj


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for filename in args.files:
        try:
            data = json.loads(filename.read_text(encoding="utf-8"),
                              object_pairs_hook=unique_object)
            n, power, span, denominator, numerator, divisor = verify(data)
        except (ValueError, OSError, OverflowError) as error:
            print(f"FAIL {filename.name}: {error}", file=sys.stderr)
            failed = True
        else:
            print(f"PASS {filename.name} n={n} p={power} pairs={n*(n-1)//2}"
                  f" span={span}/{denominator} B={numerator}/{divisor}")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
