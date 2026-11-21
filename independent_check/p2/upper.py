"""Independent rational replay of the line witnesses in the upper-bound proposition of Paper II.

The feasibility test uses only the geometric-mean separation in the line problem.
Heuristic search histories do not enter any comparison.
"""

import json
import re
from fractions import Fraction
from itertools import combinations
from pathlib import Path


SIZES = (3, 4, 5, 6, 14, 200, 400, 800, 1600, 3200)
MACROS = {1: "CstarUpper", 2: "CtwoUpper"}


def atan_bounds(reciprocal, pairs):
    """The alternating arctangent series at 1/q, ending on either side."""
    x = Fraction(1, reciprocal)
    lower = sum((-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(2 * pairs))
    return lower, lower + x ** (4 * pairs + 1) / (4 * pairs + 1)


# Machin's identity: pi/4 = 4 atan(1/5) - atan(1/239).
a_lo, a_hi = atan_bounds(5, 10)
b_lo, b_hi = atan_bounds(239, 4)
PI_LO, PI_HI = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def unique_fields(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON field {key}")
        obj[key] = value
    return obj


def check_placement(data, p, n):
    """Return (coordinate denominator, actual span numerator, ceiling)."""
    if data["schema"] != "ringmin-line-v1":
        raise ValueError("unknown certificate schema")
    if (
        type(data["n"]) is not int
        or data["n"] != n
        or type(data["power"]) is not int
        or data["power"] != p
    ):
        raise ValueError("filename and (n, power) disagree")
    if p not in MACROS or n < 2:
        raise ValueError("unsupported witness family or size")

    coords, order = data["positions"], data["order"]
    if (
        type(coords) is not list
        or len(coords) != n
        or any(type(x) is not int for x in coords)
    ):
        raise ValueError("expected one integer coordinate per label")
    if (
        type(order) is not list
        or any(type(i) is not int for i in order)
        or sorted(order) != list(range(1, n + 1))
    ):
        raise ValueError("order is not a permutation")
    if any(coords[i - 1] >= coords[j - 1] for i, j in zip(order, order[1:])):
        raise ValueError("order disagrees with coordinates")
    d = data["D"]
    if type(d) is not int or d <= 0:
        raise ValueError("invalid coordinate denominator")
    h = max(coords) - min(coords)
    if type(data["span_numerator"]) is not int or data["span_numerator"] != h:
        raise ValueError("span mismatch")

    # With mark i**p/n**p, multiplying the distance by n**p turns
    # the squared required distance into i**p * j**p. Clear D once.
    scale = Fraction(n**p, d)
    points = [
        (i, x * scale.numerator, i**p * scale.denominator)
        for i, x in enumerate(coords, 1)
    ]
    for (i, x, wi), (j, y, wj) in combinations(points, 2):
        if (x - y) ** 2 < wi * wj:
            raise ValueError(f"insufficient separation of labels {i} and {j}")

    ratio = data["B"]
    if (
        type(ratio) is not list
        or len(ratio) != 2
        or any(type(v) is not int or v <= 0 for v in ratio)
    ):
        raise ValueError("invalid ceiling numerator or denominator")
    ceiling = Fraction(*ratio)
    per_mark = Fraction(h + d, n * d)
    if per_mark >= ceiling * PI_LO:
        raise ValueError("cannot certify the strict ring ceiling")
    if (ceiling * 10**12).denominator != 1 or (
        ceiling - Fraction(1, 10**12)
    ) * PI_HI >= per_mark:
        raise ValueError("ceiling exceeds 12-place outward rounding")
    return d, h, ceiling


def published_values(main, numbers, p, checked):
    d, h, ceiling = checked
    name = MACROS[p]
    decimals = re.findall(r"\\newcommand\{\\" + name + r"\}\{(\d+\.\d+)\}", numbers)
    if len(decimals) != 1:
        raise ValueError(f"missing or ambiguous {name}")
    value = Fraction(decimals[0])
    unit = Fraction(1, 10 ** len(decimals[0].split(".")[1]))
    per_mark = Fraction(h + d, 3200 * d)
    yield (
        f"numbers.tex {name} strict witness ceiling",
        value == ceiling and per_mark < value * PI_LO,
    )
    yield (
        f"numbers.tex {name} outward rounding by <1 final unit",
        (value - unit) * PI_HI < per_mark,
    )

    # The abstract repeats the decimals. Bind each to its own coefficient.
    abstract = main.split(r"\begin{abstract}", 1)[1].split(r"\end{abstract}", 1)[0]
    pattern = (
        r"C_\s*\\ast\s*<\s*(\d+\.\d+)" if p == 1 else r"less than\s*\$(\d+\.\d+)\$"
    )
    advertised = re.findall(pattern, abstract)
    yield (
        f"abstract p={p} printed ceiling",
        len(advertised) == 1 and Fraction(advertised[0]) == value,
    )

    # Match the proposition's m, D, H and reference to this macro against
    # the evaluated witness, including H as printed (with TeX thin spaces).
    section = main.split(r"\label{prop:cert-upper}", 1)[1].split(r"\end{proof}", 1)[0]
    section = section.replace(r"\,", "")
    rows = re.findall(
        rf"^\s*{p}\s*&\s*([^&\n]+?)\s*&\s*(\d+)\s*&\s*\\(\w+)",
        section,
        re.MULTILINE,
    )
    good = False
    if len(rows) == 1 and re.search(r"Take\s+\$m=3200\$", section):
        formula, span, printed_macro = rows[0]
        denominator = {r"m10^{12}": 3200 * 10**12, "m^2": 3200**2}.get(formula)
        good = (d, h, name) == (denominator, int(span), printed_macro)
    yield f"upper proposition p={p} printed witness", good


def run(root):
    """Yield a verdict for each expected witness and each published upper value."""
    assets = Path(root) / "paper_assets"
    paper = assets / "journal_p2_sidma"
    directory = assets / "line_upper" / "certificates"
    main = (paper / "main.tex").read_text(encoding="utf-8")
    numbers = (paper / "numbers.tex").read_text(encoding="utf-8")
    names = {f"p{p}_n{n:05d}.json" for p in MACROS for n in SIZES}
    names.update(path.name for path in directory.glob("*.json"))
    for name in sorted(names):
        try:
            match = re.fullmatch(r"p([12])_n(\d{5})\.json", name)
            if not match:
                raise ValueError("unknown witness filename")
            p, n = map(int, match.groups())
            data = json.loads(
                (directory / name).read_text(encoding="utf-8"),
                object_pairs_hook=unique_fields,
            )
            witness = check_placement(data, p, n)
            yield f"{name} {n * (n - 1) // 2} pairs, strict B={witness[2]}", True
            if n == 3200:
                yield from published_values(main, numbers, p, witness)
        except (ValueError, TypeError, OSError, KeyError, IndexError) as exc:
            yield f"{name} {exc}", False
