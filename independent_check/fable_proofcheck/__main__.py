"""Run every proof check and negative control found in this directory.

    python -I -B independent_check/fable_proofcheck [PREFIX ...]

Modules ``p1_*.py`` (Paper I) and ``p2_*.py`` (Paper II) are discovered by
name, so the same runner serves either branch and a tree containing both.
Optional PREFIX arguments restrict the run to identifiers starting with one
of them (for example ``P1-B`` or ``P2-L4``).  The exit status is nonzero if
any check fails or any negative control is not rejected.

This file is identical on the Paper I and Paper II proof-check branches.
"""

from __future__ import annotations

import importlib
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def load():
    import fable_common as common

    with common.working_precision():
        for path in sorted(HERE.glob("p[12]_*.py")):
            importlib.import_module(path.stem)

    def natural(item):
        return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", item[0])]

    return sorted(common.CHECKS, key=natural), sorted(common.CONTROLS, key=natural)


def main(argv) -> int:
    checks, controls = load()
    prefixes = tuple(argv) or ("",)
    failures = 0
    ran = 0
    for ident, kind, claim, function in checks:
        if not ident.startswith(prefixes):
            continue
        ran += 1
        start = time.perf_counter()
        try:
            detail = function()
            status = "PASS"
        except AssertionError as error:
            detail, status = "ASSERTION: %s" % error, "FAIL"
            failures += 1
        except Exception as error:  # an unexpected error is a failure, not a skip
            detail, status = "%s: %s" % (type(error).__name__, error), "FAIL"
            failures += 1
        print("%s %-7s %-8s %s\n      -> %s  [%.1fs]" % (status, ident, kind, claim, detail, time.perf_counter() - start), flush=True)
    for ident, description, function in controls:
        if not ident.startswith(prefixes):
            continue
        ran += 1
        try:
            function()
            status = "FAIL"
            failures += 1
        except AssertionError:
            status = "PASS"
        print("%s %-7s control  rejected as required: %s" % (status, ident, description), flush=True)
    print("\n%d items, %d failures" % (ran, failures))
    return 1 if failures or not ran else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
