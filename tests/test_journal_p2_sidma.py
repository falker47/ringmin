"""Compare the SIDMA documents with the two reviewed sources independently of TeX."""
from hashlib import sha256
from pathlib import Path
import re
import runpy
from zipfile import ZipFile

import pytest


ASSETS = Path(__file__).resolve().parents[1] / "paper_assets"
V4 = ASSETS / "journal_p2_v4"
SIDMA = ASSETS / "journal_p2_sidma"
FROZEN = ASSETS / "paper_ii_journal" / "source_bundle.zip"
S1 = "lower_supplement/supplement.tex"
AUTHOR_NOTE = "% author: add Claude (Anthropic) to this statement"


def read(path):
    return path.read_text(encoding="utf-8")


def reviewed(name):
    if name == "main":
        return read(V4 / "main.tex")
    with ZipFile(FROZEN) as archive:
        return archive.read(S1).decode("utf-8")


def abstract(tex):
    return tex.split(r"\begin{abstract}", 1)[1].split(r"\end{abstract}", 1)[0].strip()


def scientific_body(tex):
    # Include every section, both figures and captions, both data tables and all
    # material following the last proof. Only front matter and bibliography differ.
    body = tex[tex.index(r"\section{"):]
    return re.split(r"\\(?:begin\{thebibliography\}|bibliographystyle\{|nocite\{)", body, maxsplit=1)[0].strip()


@pytest.mark.parametrize(("name", "digest"), [
    ("main", "18f810d43aecb651c9c529583d9aabba796d093cac0e73be050dfef587d42c40"),
    ("supplement", "ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4"),
])
def test_mathematical_text(name, digest):
    old = reviewed(name)
    new = read(SIDMA / f"{name}.tex")
    assert sha256(old.encode()).hexdigest() == digest
    commands = r"^\\(?:newcommand|DeclareMathOperator)\{.*$"
    assert re.findall(commands, old, re.M) == re.findall(commands, new, re.M)

    expected_abstract = abstract(old)
    expected = scientific_body(old)
    actual = scientific_body(new)
    if name == "main":
        # Front-matter metadata must stand on its own without document-local macros.
        for macro, value in re.findall(r"\\newcommand\{(\\\w+)\}\{([^{}]+)\}", read(V4 / "numbers.tex")):
            expected_abstract = expected_abstract.replace(macro, value)
        expected_abstract = expected_abstract.replace(r"\CC", r"C_\ast")
        for title in ("Main results", "Related work"):
            expected = expected.replace(r"\paragraph{" + title + ".}", r"\paragraph*{" + title + "}")
        expected = expected.replace("Supplement S1 gives the complete proof",
                                    r"Supplement S1 (Theorem~\ref{s1-thm:main}) gives the complete proof")
        expected = expected.replace("0.14191330499527,0.14191330499528",
                                    r"0.14191330499527,\allowbreak 0.14191330499528")
        expected += "\n" + AUTHOR_NOTE + "\n\n" + r"\clearpage"
    else:
        expected = expected.replace(r"\texttt{check\_width\_optimum.py}", r"\path{check_width_optimum.py}", 1)
        expected = expected.replace("These supporting files are included alongside\nthis source and PDF;",
                                    "The companion " + r"\href{s1_support.zip}{\texttt{s1\_support.zip}}"
                                    + " contains these\nsupporting files with the original source and PDF;")
    assert abstract(new) == expected_abstract
    assert actual == expected


def test_figures_decimal_inputs_and_companion():
    assert read(SIDMA / "numbers.tex") == read(V4 / "numbers.tex")
    figures = sorted(p.name for p in (V4 / "figures").glob("*.pdf"))
    assert figures == ["finite_brackets.pdf", "line_geometry.pdf"]
    assert sorted(p.name for p in (SIDMA / "figures").iterdir()) == figures
    for name in figures:
        assert (SIDMA / "figures" / name).read_bytes() == (V4 / "figures" / name).read_bytes()
    with ZipFile(FROZEN) as original, ZipFile(SIDMA / "s1_support.zip") as companion:
        members = [n for n in original.namelist() if n.startswith("lower_supplement/")]
        assert len(members) == 13
        assert sorted(companion.namelist()) == sorted(members)
        for name in members:
            assert companion.read(name) == original.read(name)


def test_submission_metadata_and_bibliographies():
    main = read(SIDMA / "main.tex")
    supplement = read(SIDMA / "supplement.tex")
    shared = read(SIDMA / "shared.tex")
    assert r"\externaldocument[s1-][nocite]{supplement}" in main
    assert r"\externaldocument[article-][nocite]{main}" in supplement
    assert r"Proposition~\ref{article-prop:lower}" in supplement
    assert r"\newsiamremark{remark}{Remark}" in shared
    for text in (main, supplement):
        assert r"\input{shared}" in text
        assert r"\bibliographystyle{siamplain}" in text
    assert r"\begin{keywords}" in main and r"\begin{MSCcodes}" in main
    assert "52C15, 52C26, 90C05" in main
    assert "\n\n" not in abstract(main)
    assert len(abstract(main).split()) <= 250
    assert main.count(AUTHOR_NOTE) == 1
    for name, bib in (("main", "references.bib"), ("supplement", "supplement-references.bib")):
        source = reviewed(name)
        entries = read(SIDMA / bib)
        assert sorted(re.findall(r"\\bibitem\{([^}]+)\}", source)) == sorted(re.findall(r"@\w+\{([^,]+),", entries))
        assert sorted(re.findall(r"\\href\{https://doi.org/([^}]+)\}", source)) == sorted(re.findall(r"doi = \{([^}]+)\}", entries))


def test_final_log_gate():
    check = runpy.run_path(str(SIDMA / "build.py"))["check_log"]
    clean = "Output written on main.pdf (10 pages, 300000 bytes).\n"
    assert check("main", clean + r"Overfull \hbox (1.0pt too wide)") == 10
    for diagnostic in (r"Overfull \hbox (1.001pt too wide)", r"Overfull \vbox (1.01pt too high)",
                       "LaTeX Warning: Citation 'paper' undefined", "There were undefined references.",
                       "Label(s) may have changed.", "Package xr Warning: No file supplement.aux"):
        with pytest.raises(RuntimeError):
            check("main", clean + diagnostic)
