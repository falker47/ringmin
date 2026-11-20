"""Check the v4 claim inventory, journal build, and numerical illustrations."""

import copy
import hashlib
import importlib.util
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import pytest

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "paper_assets" / "journal_p1_v5"


@pytest.fixture(scope="module")
def graphics():
    spec = importlib.util.spec_from_file_location(
        "journal_p1_figures", DRAFT / "make_figures.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def blocks(text, names):
    parts = re.findall(r"\\begin\{(" + names + r")\}(.+?)\\end\{\1\}", text, re.S)
    return "\n".join(name + "\n" + body for name, body in parts)


def test_v4_statements_equations_table_values_and_declarations():
    # Hashes were computed directly from the published v4 source archive.
    # Universal newlines allow Git to check out CRLF on Windows.
    main = (DRAFT / "main.tex").read_text(encoding="utf-8")
    expected = {
        "lemma|theorem|corollary|proposition|definition": "e3372d00d5d1b130df8798d91c2fce73cd0790504cd099351fd85d53788d978b",
        "equation|align": "b96faad635579535f5e8eb6a8a508e3e56ec21d6772430540cfefac7f70657a8",
        "tabularx?": "03ee39a4a901b516eaa03ceb417cfd9ee67a43901535b64f8d8de9cdbf188158",
    }
    for names, digest in expected.items():
        assert sha(blocks(main, names)) == digest
    start = main.index(r"\section*{Statements and Declarations}")
    end = main.index(r"\input{references.tex}", start)
    assert (
        sha(main[start:end].strip())
        == "05875fc3ed0487ec73296386bf97f1f3f8298451fe586d98e64664a52436bef8"
    )
    inputs = {
        "bracket_rows.tex": "58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1",
        "coverage_rows.tex": "4f4bf81b65c68fcd68d337b36ca43c1582f495ca6bf41ad71ccf3b90afceb87a",
        "seam_appendix.tex": "5d518283d993967489968ced9804d1476a41a49bad1596808862d1cffd66515d",
    }
    for name, digest in inputs.items():
        assert sha((DRAFT / name).read_text(encoding="utf-8")) == digest


def test_verified_bibliography_matches_the_cited_entries():
    entries = json.loads((DRAFT / "refs_verification.json").read_bytes())["references"]
    by_key = {entry["key"]: entry for entry in entries}
    src = (DRAFT / "main.tex").read_text(encoding="utf-8")
    group = re.findall(r"\\cite\{([^}]+)\}", src)
    cited = {key for text in group for key in text.split(",")}
    bib = (DRAFT / "references.tex").read_text(encoding="utf-8")
    assert len(cited) >= 15
    assert len(entries) == len(by_key)
    assert set(by_key) == cited == set(re.findall(r"\\bibitem\{([^}]+)\}", bib))
    for entry in entries:
        assert entry["status"] == "VERIFIED"
        assert entry["verification_url"].startswith(
            ("https://doi.org/", "https://api.crossref.org/")
        )
        assert entry["title"] and entry["authors"] and entry["venue"] and entry["year"]
        assert "https://doi.org/" + entry["doi"] in bib
    abstract = src.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
    assert len(abstract.split()) <= 200


def test_exact_witness_and_collapsed_direction(graphics):
    data = json.loads(graphics.CERTIFICATE.read_bytes())["certificate"]
    row = next(case for case in data["cases"] if case["n"] == 14)
    radius, centers = graphics.witness14(row)
    assert radius == Fraction("21.66539518222")
    assert set(centers) == set(range(1, 15))
    margins = []
    for a, b in itertools.combinations(centers, 2):
        (x, y), (u, v) = centers[a], centers[b]
        margins.append((x - u) ** 2 + (y - v) ** 2 - (a + b) ** 2)
    assert len(margins) == 91 and min(margins) > 0
    invalid = copy.deepcopy(row)
    params = invalid["upper_witnesses"][0]["exact_cartesian_check"][
        "stereographic_parameters"
    ]
    params[1] = params[0]
    with pytest.raises(ValueError, match="strict separation"):
        graphics.witness14(invalid)


def test_published_tables_and_normalized_plot_match_all_certificates(graphics):
    archive = ROOT / "paper_assets" / "general_radii"
    quadratic = "quadratic_brackets.tex"
    assert (DRAFT / quadratic).read_text(encoding="utf-8") == (
        archive / quadratic
    ).read_text(encoding="utf-8")

    fig, ax = graphics.plt.subplots()
    try:
        graphics.ratio_plot(ax)
        series = {line.get_label(): line for line in ax.lines}
        families = (
            ("linear", 1, "bracket_rows.tex", r"$R^*(n)/n^2$"),
            ("quadratic", 2, quadratic, r"$R_2^*(n)/n^3$"),
        )
        for intervals, (family, power, filename, label) in zip(
            ax.collections, families, strict=True
        ):
            rows = graphics.bracket_rows(filename)
            assert list(series[label].get_xdata()) == list(range(3, 15))
            for n, point, segment in zip(
                range(3, 15), series[label].get_ydata(), intervals.get_segments(), strict=True
            ):
                cert = json.loads((archive / "certificates" / f"{family}_{n:02}.json").read_bytes())
                assert cert["radii"] == [i**power for i in range(1, n + 1)]
                lo, hi = Fraction(cert["lower"]), Fraction(cert["upper"])
                assert rows[n] == (lo, hi) and hi - lo == Fraction(1, 10**11)
                scale = n ** (power + 1)
                assert segment.tolist() == [[n, float(lo / scale)], [n, float(hi / scale)]]
                assert point == float((lo + hi) / (2 * scale))
        (band,) = ax.patches
        bounds = band.get_window_extent().transformed(ax.transData.inverted())
        assert (bounds.ymin, bounds.ymax) == pytest.approx(
            (0.1405694688, 0.140958576058), rel=0, abs=1e-14
        )
        (upper_line,) = (line for line in ax.lines if line.get_linestyle() == ":")
        assert list(upper_line.get_ydata()) == [0.088581212993] * 2
    finally:
        graphics.plt.close(fig)


def test_chain_diagrams_and_three_sign_changes(graphics):
    with mp.workdps(50):
        r, centers, _ = graphics.chain(1, 7)
        order = [1, 6, 3, 4, 5, 2, 7]
        assert list(centers) == order
        tolerance = mp.mpf("1e-42")
        for a, b in itertools.combinations(order, 2):
            x, y = centers[a]
            u, v = centers[b]
            assert (x - u) ** 2 + (y - v) ** 2 >= (a + b) ** 2 - tolerance
        for a, b in zip(order, order[1:] + order[:1]):
            x, y = centers[a]
            u, v = centers[b]
            assert abs((x - u) ** 2 + (y - v) ** 2 - (a + b) ** 2) < tolerance
        _, centers, _ = graphics.chain(1, 8)
        x, y = centers[7]
        u, v = centers[8]
        assert (x - u) ** 2 + (y - v) ** 2 < 15**2
        for k, n in ((1, 8), (2, 13), (3, 17)):
            assert graphics.chain(k, n - 1)[2] > 0 > graphics.chain(k, n)[2]


def test_figures_repeat_across_interpreter_runs(tmp_path, graphics):
    for run, seed in (("first", "12"), ("second", "47")):
        subprocess.run(
            [
                sys.executable,
                str(DRAFT / "make_figures.py"),
                "--output-dir",
                str(tmp_path / run),
            ],
            cwd=ROOT,
            env=dict(os.environ, PYTHONHASHSEED=seed),
            check=True,
            stdin=subprocess.DEVNULL,
            capture_output=True,
        )
    for stem in graphics.FIGURES:
        first = (tmp_path / "first" / (stem + ".pdf")).read_bytes()
        assert first.startswith(b"%PDF-") and b"/Subtype /Image" not in first
        assert first == (tmp_path / "second" / (stem + ".pdf")).read_bytes()


@pytest.mark.skipif(
    not shutil.which("pdflatex") or not shutil.which("pdfinfo"),
    reason="the journal PDF smoke test needs pdflatex and pdfinfo",
)
def test_three_pass_build(tmp_path):
    output = tmp_path / "proof.pdf"
    output.write_bytes(b"previous build")
    run = subprocess.run(
        [sys.executable, str(DRAFT / "build.py"), "--output", str(output)],
        check=True,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
    )
    assert "pdflatex_passes=3 unresolved=0" in run.stdout
    assert int(re.search(r"before_appendices=(\d+)", run.stdout)[1]) <= 13
    assert output.read_bytes().startswith(b"%PDF-")
