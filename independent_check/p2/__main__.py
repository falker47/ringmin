"""Run with python -I -B independent_check/p2 from a checkout of Paper II."""

import re
import sys
from pathlib import Path

import comparison
import figure
import lower
import upper


def main():
    root = Path(__file__).resolve().parents[2]
    passed = 0
    failed = 0

    def report(label, ok):
        nonlocal passed, failed
        print(f"{'PASS' if ok else 'FAIL'} {label}", flush=True)
        if ok:
            passed += 1
        else:
            failed += 1

    numbers = (root / "paper_assets/journal_p2_sidma/numbers.tex").read_text(
        encoding="utf-8"
    )
    names = re.findall(r"\\newcommand\{\\(\w+)\}", numbers)
    report(
        "numbers.tex inventory",
        sorted(names) == ["CstarLower", "CstarUpper", "CtwoUpper"],
    )
    for module in (upper, lower, comparison, figure):
        try:
            for label, ok in module.run(root):
                report(label, ok)
        except (
            ArithmeticError,
            OSError,
            ValueError,
            KeyError,
            IndexError,
            TypeError,
        ) as exc:
            report(f"{module.__name__}: {exc}", False)
    print(f"{passed} passed, {failed} failed")
    return int(bool(failed))


if __name__ == "__main__":
    sys.exit(main())
