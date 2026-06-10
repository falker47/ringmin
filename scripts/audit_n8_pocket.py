from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ringmin.evaluator import full_radius


def pocket_radius(R: float, a: float, b: float) -> float:
    curvature = (
        1.0 / R
        + 1.0 / a
        + 1.0 / b
        + 2.0 * math.sqrt(1.0 / (R * a) + 1.0 / (a * b) + 1.0 / (R * b))
    )
    return 1.0 / curvature


def main() -> int:
    result = full_radius((8, 1, 6, 4, 5, 3, 7, 2))
    print(f"R_full={result.R_full:.17g}")
    print(f"pocket_8_6_at_full_R={pocket_radius(result.R_full, 8, 6):.17g}")
    print(f"pocket_8_1_at_full_R={pocket_radius(result.R_full, 8, 1):.17g}")
    print(f"pocket_1_6_at_full_R={pocket_radius(result.R_full, 1, 6):.17g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
