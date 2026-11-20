"""Reproduction, claim fidelity and presentation checks for Paper II."""
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest

PACKAGE = Path(__file__).resolve().parents[1]/"paper_assets/journal_p2_v4"
FIGURES = ["line_geometry.pdf", "finite_brackets.pdf"]
TEX_AVAILABLE = shutil.which("pdflatex") and shutil.which("pdfinfo")


def text(name):
    return (PACKAGE/name).read_text(encoding="utf-8")


def digest(s):
    return sha256(s.encode("utf-8")).hexdigest()


def run(script, *args, cwd=PACKAGE):
    return subprocess.run([sys.executable, str(cwd/script), *map(str,args)],
                          capture_output=True, text=True)


def test_abstract_numbers_and_targets():
    source = text("main.tex")
    abstract = source.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
    title = "The minimum central circle for prescribed radius profiles"
    assert rf"\title{{{title}}}" in source and f"pdftitle={{{title}}}" in source
    assert r"\CstarLower<\CC<\CstarUpper" in abstract
    assert r"\CtwoUpper" in abstract and "pending" not in abstract.lower()
    assert len(abstract.split()) <= 200
    # Decimal claims come from the display macros. A literal algebraic square is fine.
    assert not re.search(r"\d", re.sub(r"\^(?:2|\{2\})", "", abstract))
    numbers = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{(\d+\.\d+)\}", text("numbers.tex")))
    assert numbers == {"CstarLower": "0.1405694688", "CstarUpper": "0.140958576058",
                       "CtwoUpper": "0.088581212993"}
    certs = PACKAGE.parent / "line_upper" / "certificates"
    for p, macro in [(1, "CstarUpper"), (2, "CtwoUpper")]:
        cert = json.loads((certs / f"p{p}_n03200.json").read_bytes())
        assert cert["n"] == 3200 and cert["power"] == p
        assert Fraction(numbers[macro]) == Fraction(*cert["B"])
    assert Fraction(numbers["CstarLower"]) < Fraction("0.14056946887766098063257")


def test_verified_references_match_citations():
    source = text("main.tex")
    cited = {k for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",source)
             for k in group.split(",")}
    listed = set(re.findall(r"\\bibitem\{([^}]+)\}",source))
    registry = json.loads(text("refs_verification.json"))["references"]
    assert len(registry) == len({r["doi"].lower() for r in registry}) >= 12
    assert cited == listed == {r["key"] for r in registry}
    for ref in registry:
        assert ref["status"] == "VERIFIED"
        assert ref["verification_url"].startswith(("https://api.crossref.org/","https://doi.org/"))
        assert all(ref[k] for k in ("title","authors","year","venue"))
        assert f"https://doi.org/{ref['doi']}" in source


def test_surviving_v3_statements_and_displays():
    source = text("main.tex")
    uniform = source.split(r"\section{Exact Angular Comparison}")[1].split(
        r"\section{Prescribed radius profiles}")[0]
    lower = source.split(r"\section{An Explicit Global Lower Endpoint}")[1].split(
        r"\section{Finite values and open questions}")[0]
    body = uniform + lower
    numbered = re.findall(r"\\begin\{equation\}[\s\S]*?\\end\{equation\}", body)
    displays = re.findall(r"\\\[[\s\S]*?\\\]", body)
    # Independently extracted from the surviving sections of official arXiv v3.
    assert len(numbered) == 9
    assert digest("\n".join(numbered)) == "9726abef3e12d18330eba0fe772f3b6dbfa5da6af6408588729bebfb59a6b924"
    assert len(displays) == 7
    assert digest("\n".join(displays)) == "684b49c2e3e60575e237d057d6e6b8c83a05df2483cbdd7f1dfff1b3efa3e289"
    expected = ["107a704c1f0e56100cc2542d335d79776b45c56c4a3b3f0308227cf4138e6e64",
                "30b9212ce9cfe5ce1bb64fafe1d9bede7f50effadbd04e0d44d96b0f6a2034dd",
                "30aa77d4c7add73709dc795bd6dc0586c4fb6d107392af88e4a07d819b213885",
                "adbcdf06eb9bdafa79d2f573225091eccf1906bc0a5f165b4d6c079d9d123b0d",
                "4b1cf2d80db95939ba25099552d6f94dd7d2c45bdfdd9157b842884fea2cd875",
                "82f6b59fdbf2c21fc53712b242a4dff0467ba520973573774fe6463189594c3e"]
    statements = re.findall(
        r"\\begin\{(definition|lemma|theorem|proposition)\}([\s\S]*?)\\end\{\1\}",body)
    assert len(statements) == len(expected)
    claim_map = text("CLAIMS_DIFF.md")
    for num, (kind, statement), known in zip((1, 2, 3, 4, 5, 7), statements, expected, strict=True):
        math = re.findall(r"\$(?:\\.|[^$])*\$|\\\[[\s\S]*?\\\]|"
                          r"\\begin\{equation\}[\s\S]*?\\end\{equation\}",statement)
        assert digest("\n".join(math)) == known
        assert f"{kind.capitalize()} {num}" in claim_map
    for eq in numbered:
        assert re.search(r"\\label\{([^}]+)\}",eq)[1] in claim_map
    ack = source.split(r"\section*{Acknowledgment}")[1].split(r"\begin{thebibliography}")[0]
    assert digest(ack) == "0898445cec77c80937004523c9f27af1b91ae903e048c41c0199eb5645cce104"


def test_figure_reproduction(tmp_path):
    first, second = tmp_path/"first", tmp_path/"second"
    for folder in (first, second):
        result = run("make_figures.py", "--output", folder)
        assert result.returncode == 0, result.stderr
        assert sorted(p.name for p in folder.iterdir()) == sorted(FIGURES)
    assert all((first/name).read_bytes() == (second/name).read_bytes() for name in FIGURES)


def test_figure_band_tracks_both_macros(tmp_path):
    spec = importlib.util.spec_from_file_location("journal_figures", PACKAGE/"make_figures.py")
    figures = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(figures)
    table = PACKAGE/"figures/bracket_rows.tex"
    numbers = tmp_path/"numbers.tex"
    for lo, hi in [("0.1405694688", "0.140958576058"), ("0.134", "0.145")]:
        numbers.write_text(rf"\newcommand{{\CstarLower}}{{{lo}}}" + "\n" +
                           rf"\newcommand{{\CstarUpper}}{{{hi}}}", encoding="utf-8")
        fig = figures.finite_brackets(table, numbers)
        try:
            assert len(fig.axes) == 2
            for ax in fig.axes:
                band, = ax.patches
                # Axes fractions in x, data coordinates in y for axhspan.
                vertices = band.get_path().transformed(band.get_patch_transform()).vertices
                assert (min(vertices[:, 1]), max(vertices[:, 1])) == pytest.approx((float(lo), float(hi)))
            assert [label.get_text() for label in fig.axes[1].get_yticklabels()] == [lo, hi]
        finally:
            figures.plt.close(fig)


@pytest.mark.skipif(not TEX_AVAILABLE, reason="requires pdflatex and pdfinfo")
def test_build_and_fail_closed(tmp_path):
    output = tmp_path/"draft.pdf"
    result = run("build.py","--output",output)
    assert result.returncode == 0, result.stderr
    match = re.search(r"BUILD_PASS pages=(\d+) main_pages=(\d+) passes=3 unresolved=0",result.stdout)
    assert match and 0 < int(match[2]) <= min(14, int(match[1]))
    assert output.read_bytes().startswith(b"%PDF")
    scratch = tmp_path/"broken"
    scratch.mkdir()
    for name in ("main.tex","numbers.tex","build.py"):
        shutil.copyfile(PACKAGE/name,scratch/name)
    shutil.copytree(PACKAGE/"figures",scratch/"figures")
    bad = scratch/"main.tex"
    bad.write_text(text("main.tex").replace(r"\begin{document}",
        r"\begin{document}Missing~\ref{absent} and~\cite{absent}."),encoding="utf-8")
    failure = run("build.py","--output",scratch/"broken.pdf",cwd=scratch)
    assert failure.returncode and "unresolved final TeX log" in failure.stderr
    assert not (scratch/"broken.pdf").exists()
    (scratch/"figures"/FIGURES[0]).unlink()
    missing = run("build.py","--output",scratch/"broken.pdf",cwd=scratch)
    assert missing.returncode and FIGURES[0] in missing.stderr


@pytest.mark.skipif(not TEX_AVAILABLE, reason="requires pdflatex and pdfinfo")
@pytest.mark.parametrize("main_pages", [14, 15])
def test_page_limit_excludes_bibliography(tmp_path, main_pages):
    shutil.copyfile(PACKAGE/"build.py", tmp_path/"build.py")
    (tmp_path/"numbers.tex").write_text("", encoding="utf-8")
    source = (r"\documentclass{article}\begin{document}" + "\n" +
              "Body.\\newpage\n" * (main_pages - 1) +
              r"Last paragraph.\label{page:main-end}\newpage References.\end{document}")
    (tmp_path/"main.tex").write_text(source, encoding="utf-8")
    output = tmp_path/"result.pdf"
    result = run("build.py", "--output", output, cwd=tmp_path)
    if main_pages == 14:
        assert result.returncode == 0 and "pages=15 main_pages=14" in result.stdout
    else:
        assert result.returncode and "15 main-text pages" in result.stderr
        assert not output.exists()
