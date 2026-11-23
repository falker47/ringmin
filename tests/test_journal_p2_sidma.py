"""Guard the SIDMA revision, its protected source material, and the frozen supplement."""
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


def test_protected_article_text():
    old = reviewed("main")
    new = read(SIDMA / "main.tex")
    assert sha256(old.encode()).hexdigest() == "18f810d43aecb651c9c529583d9aabba796d093cac0e73be050dfef587d42c40"

    # SIAM front matter uses the expanded form of the reviewed decimal macros.
    expected = abstract(old)
    for macro, value in re.findall(r"\\newcommand\{(\\\w+)\}\{([^{}]+)\}", read(V4 / "numbers.tex")):
        expected = expected.replace(macro, value)
    expected = expected.replace(r"\CC", r"C_\ast").replace(
        "with leading coefficient less than\n$0.088581212993$",
        "with leading coefficient\n" + r"$(434+4\sqrt2)/(1587\pi)\le C_2<0.088581212993$",
    )
    assert abstract(new) == expected

    commands = r"^\\(?:newcommand|DeclareMathOperator)\{.*$"
    assert re.findall(commands, new, re.M) == re.findall(commands, old, re.M)
    assert r"\ref{s1-thm:square-lower}" in new
    assert r"\frac{434+4\sqrt2}{1587\pi}\ \le\ C_2\ <\ \CtwoUpper" in new

    for label in ("prop:cert-upper", "prop:lower"):
        pattern = rf"\\label\{{{label}\}}(.*?)\\end\{{proposition\}}"
        assert re.search(pattern, new, re.S)[1] == re.search(pattern, old, re.S)[1]

    old_note = old.split(r"\section*{Acknowledgment}", 1)[1].split(r"\begin{thebibliography}", 1)[0].strip()
    new_note = new.split(r"\section*{Acknowledgment}", 1)[1].split(AUTHOR_NOTE, 1)[0].strip()
    assert new_note == old_note


def test_supplement_mathematical_text():
    old = reviewed("supplement")
    new = read(SIDMA / "supplement.tex")
    assert sha256(old.encode()).hexdigest() == "ce376ae3521b172379c2a37f7a0905f8eff8b9591d44f423192c54acd56616b4"
    commands = r"^\\(?:newcommand|DeclareMathOperator)\{.*$"
    assert re.findall(commands, new, re.M) == re.findall(commands, old, re.M)
    assert abstract(new) == abstract(old) + (
        "\nAn additional argument for square radii gives the lower bound\n"
        + r"$(434+4\sqrt2)/(1587\pi)$ for their cubic growth coefficient."
    )
    expected = scientific_body(old).replace(r"\texttt{check\_width\_optimum.py}", r"\path{check_width_optimum.py}", 1)
    expected = expected.replace("These supporting files are included alongside\nthis source and PDF;",
                                "The companion " + r"\href{s1_support.zip}{\texttt{s1\_support.zip}}"
                                + " contains these\nsupporting files with the original source and PDF;")
    assert scientific_body(new) == expected + "\n\n" + r"\input{sections/square_lower}"
    square = read(SIDMA / "sections/square_lower.tex")
    assert r"\begin{theorem}\label{thm:square-lower}" in square
    assert r"\ \ge\ \frac{434+4\sqrt2}{1587\pi}" in square
    assert r"\cite[(22)--(23)]{squared}" in square


def test_law_and_specializations_are_included():
    main = read(SIDMA / "main.tex")
    law = read(SIDMA / "sections/law.tex")
    words = read(SIDMA / "sections/words.tex")
    section_inputs = r"^\\input\{sections/([^}]+)\}\s*$"
    assert re.findall(section_inputs, main, re.M) == ["law", "words"]
    assert re.findall(section_inputs, words, re.M) == ["worked_lp_example"]
    assert (SIDMA / "sections/worked_lp_example.tex").is_file()
    assert law.index(r"\label{thm:profile-law}") < law.index(r"\label{eq:limit}")
    assert words.index(r"\label{thm:profile-words}") < words.index(r"\label{thm:lp}")


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
    assert r"\ref{article-prop:lower}" in supplement
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
        keys = re.findall(r"\\bibitem\{([^}]+)\}", source)
        keys.append("squared")
        assert "1d0a5dea10cd09783a9c0e2d54ede79b790cce2b" in entries
        assert sorted(keys) == sorted(re.findall(r"@\w+\{([^,]+),", entries))
        assert sorted(re.findall(r"\\href\{https://doi.org/([^}]+)\}", source)) == sorted(re.findall(r"doi = \{([^}]+)\}", entries))


RELEASE_TAG = "paper-ii-sidma-r1"


def test_repository_links_use_the_release_tag():
    # Squash merges keep branch commits off main, so a link pinned to one of them
    # can stop resolving. Each repository link names the release tag that will be
    # created on the merged commit, and each linked path must exist in this tree.
    link = r"https://github\.com/falker47/ringmin/(?:raw|tree|blob)/([^/}]+)/([^}]+)\}"
    links = [found for name in ("main.tex", "supplement.tex") for found in re.findall(link, read(SIDMA / name))]
    assert len(links) == 3
    for ref, path in links:
        assert ref == RELEASE_TAG
        assert (ASSETS.parent / path).exists(), path


def test_final_log_gate():
    check = runpy.run_path(str(SIDMA / "build.py"))["check_log"]
    clean = "Output written on main.pdf (10 pages, 300000 bytes).\n"
    assert check("main", clean + r"Overfull \hbox (1.0pt too wide)") == 10
    for diagnostic in (r"Overfull \hbox (1.001pt too wide)", r"Overfull \vbox (1.01pt too high)",
                       "LaTeX Warning: Citation 'paper' undefined", "There were undefined references.",
                       "Label(s) may have changed.", "Package xr Warning: No file supplement.aux"):
        with pytest.raises(RuntimeError):
            check("main", clean + diagnostic)
