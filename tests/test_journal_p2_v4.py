"""Reproduction, claim fidelity and presentation checks for Paper II."""
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest

PACKAGE = Path(__file__).resolve().parents[1]/"paper_assets/journal_p2_v4"
FIGURES = ["line_geometry.pdf", "reflected_cells.pdf", "finite_brackets.pdf"]
TEX_AVAILABLE = shutil.which("pdflatex") and shutil.which("pdfinfo")


def text(name):
    return (PACKAGE/name).read_text(encoding="utf-8")


def digest(s):
    return sha256(s.encode("utf-8")).hexdigest()


def run(script, *args, cwd=PACKAGE):
    return subprocess.run([sys.executable, str(cwd/script), *map(str,args)],
                          capture_output=True, text=True)


def test_abstract_numbers_and_targets():
    abstract = text("main.tex").split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
    sentences = re.split(r"\.\s+", " ".join(abstract.split()))
    assert r"\Rstar(n)=\CC n^{\QuadraticExponent}+o(n^{\QuadraticExponent})" in sentences[0]
    assert r"\CstarLower<\CC<\CstarUpper" in sentences[1]
    assert len(abstract.split()) <= 200
    assert not re.findall(r"[0-9]+(?:\.[0-9]+)?", abstract)
    numbers = text("numbers.tex")
    assert r"\newcommand{\CstarLower}{0.1405694688}" in numbers
    assert r"\newcommand{\QuadraticExponent}{2}" in numbers
    assert r"\newcommand{\CstarUpper}{\textbf{[certified upper bound pending]}}" in numbers


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


def test_all_v3_statements_and_displays():
    source = text("main.tex")
    body = source.split(r"\section{Exact Angular Comparison}")[1].split(
        r"\section{Finite values and open questions}")[0]
    numbered = re.findall(r"\\begin\{equation\}[\s\S]*?\\end\{equation\}",body)
    displays = re.findall(r"\\\[[\s\S]*?\\\]", body)
    # Independently extracted from the official arXiv v3 source after LF normalization.
    assert len(numbered) == 11
    assert digest("\n".join(numbered)) == "295a40cb6d950bdd8698588b93284426c63d65649607ff1a0c1f30fee2820d08"
    assert len(displays) == 14
    assert digest("\n".join(displays)) == "d56d5bfba821ad531c9bfc2f4de92a38d9033133797c490d9a5c897b59e97fe2"
    expected = ["107a704c1f0e56100cc2542d335d79776b45c56c4a3b3f0308227cf4138e6e64",
                "30b9212ce9cfe5ce1bb64fafe1d9bede7f50effadbd04e0d44d96b0f6a2034dd",
                "30aa77d4c7add73709dc795bd6dc0586c4fb6d107392af88e4a07d819b213885",
                "adbcdf06eb9bdafa79d2f573225091eccf1906bc0a5f165b4d6c079d9d123b0d",
                "4b1cf2d80db95939ba25099552d6f94dd7d2c45bdfdd9157b842884fea2cd875",
                "f812da6ca9ac0fbf1de92c21c48f0914fe5ed5e1f3cab4c0bb108fc7197f4b00",
                "82f6b59fdbf2c21fc53712b242a4dff0467ba520973573774fe6463189594c3e"]
    statements = re.findall(
        r"\\begin\{(definition|lemma|theorem|proposition)\}([\s\S]*?)\\end\{\1\}",body)
    assert len(statements) == len(expected)
    claim_map = text("CLAIMS_DIFF.md")
    for num,((kind,statement),known) in enumerate(zip(statements,expected),1):
        math = re.findall(r"\$(?:\\.|[^$])*\$|\\\[[\s\S]*?\\\]|"
                          r"\\begin\{equation\}[\s\S]*?\\end\{equation\}",statement)
        assert digest("\n".join(math)) == known
        assert f"{kind.capitalize()} {num}" in claim_map
    for eq in numbered:
        assert re.search(r"\\label\{([^}]+)\}",eq)[1] in claim_map
    ack = source.split(r"\section*{Acknowledgment}")[1].split(r"\begin{thebibliography}")[0]
    assert digest(ack) == "0898445cec77c80937004523c9f27af1b91ae903e048c41c0199eb5645cce104"


def test_figure_determinism_and_optional_endpoint(tmp_path):
    first, second = tmp_path/"first",tmp_path/"second"
    for folder in (first,second):
        result = run("make_figures.py","--output",folder)
        assert result.returncode == 0, result.stderr
        assert sorted(p.name for p in folder.iterdir()) == sorted(FIGURES)
    assert all((first/name).read_bytes()==(second/name).read_bytes() for name in FIGURES)
    # Synthetic display value exercises the optional drawing path only.
    numbers = tmp_path/"numbers.tex"
    numbers.write_text(text("numbers.tex").replace(
        r"\textbf{[certified upper bound pending]}", "0.15"),encoding="utf-8")
    other = run("make_figures.py","--output",second,"--numbers",numbers)
    assert other.returncode==0, other.stderr
    assert (first/FIGURES[2]).read_bytes() != (second/FIGURES[2]).read_bytes()
    assert all((first/name).read_bytes()==(second/name).read_bytes() for name in FIGURES[:2])


@pytest.mark.skipif(not TEX_AVAILABLE, reason="requires pdflatex and pdfinfo")
def test_build_and_fail_closed(tmp_path):
    output = tmp_path/"draft.pdf"
    result = run("build.py","--output",output)
    assert result.returncode == 0, result.stderr
    match = re.search(r"BUILD_PASS pages=(\d+) passes=3 unresolved=0",result.stdout)
    assert match and 0 < int(match[1]) <= 12 and output.read_bytes().startswith(b"%PDF")
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
