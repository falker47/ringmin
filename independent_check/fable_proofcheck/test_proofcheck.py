"""pytest entry point: every registered check must pass, every control must be rejected.

    python -m pytest independent_check/fable_proofcheck -q

This file is identical on the Paper I and Paper II proof-check branches.
"""

import importlib
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import fable_common  # noqa: E402

for _path in sorted(HERE.glob("p[12]_*.py")):
    importlib.import_module(_path.stem)


@pytest.mark.parametrize("item", fable_common.CHECKS, ids=[c[0] for c in fable_common.CHECKS])
def test_check(item):
    _ident, _kind, _claim, function = item
    assert isinstance(function(), str)


@pytest.mark.parametrize("item", fable_common.CONTROLS, ids=[c[0] for c in fable_common.CONTROLS])
def test_control_is_rejected(item):
    _ident, _description, function = item
    with pytest.raises(AssertionError):
        function()


def test_registry_is_not_empty():
    assert fable_common.CHECKS and fable_common.CONTROLS
    idents = [c[0] for c in fable_common.CHECKS] + [c[0] for c in fable_common.CONTROLS]
    assert len(idents) == len(set(idents))
