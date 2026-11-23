"""Compare the JOGO typesetting with the reviewed integrated Paper I."""

import hashlib
import re
import runpy
import shutil
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile

import pytest

ASSETS = Path(__file__).resolve().parents[1] / "paper_assets"
REVIEWED = ASSETS / "journal_p1_v5"
JOGO = ASSETS / "journal_p1_jogo"
FIGURES = ("01_kernel", "02_necklace", "03_seam", "04_witness", "05_ratios", "06_deficits")
BUILD = runpy.run_path(str(JOGO / "build.py"))


def tex(folder, name="main.tex"):
    return (folder / name).read_text(encoding="utf-8")


def normalize_figure(match):
    # Keep every caption, label and graphic in order. Discard only the float
    # placement, two-column panel layout and image sizing from these six figures.
    block = re.sub(r"\\begin\{figure\}\[[!htbp]+\]|\\end\{figure\}", " ", match[0])
    block = block.replace(r"\begin{minipage}[t]{.48\linewidth}", " ")
    block = block.replace(r"\end{minipage}", " ").replace(r"\hfill", " ")
    block = block.replace(r"\centering", " ")
    for index, name in enumerate(FIGURES, 1):
        block = block.replace(f"figures/{name}.pdf", f"Fig{index}.pdf")
    return re.sub(r"\\includegraphics\[width=(?:\.80)?\\linewidth\]", r"\\includegraphics", block)


def scientific_text(folder):
    source = tex(folder)
    start = source.index(r"\section{The packing problem")
    end = source.index(r"\section{Data and code availability}")
    appendices = source.split("\\appendix\n", 1)[1].split(r"\end{document}", 1)[0]
    body = source[start:end] + "\n" + appendices
    body = re.sub(r"\\input\{([\w.-]+\.tex)\}", lambda m: tex(folder, m[1]).rstrip(), body)
    body = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", normalize_figure, body, flags=re.S)
    body = re.sub(r"^\\clearpage\s*$", "", body, flags=re.M)
    return " ".join(body.split())


# Editorial changes to the reviewed scientific text, in whitespace-collapsed
# form. Each reviewed phrase must occur exactly once. The radii 1^2,...,n^2
# are called square radii, as in the revised Paper II.
EDITORIAL = (
    ("For the quadratic family it gives", "For square radii it gives"),
    ("For quadratic radii it proves", "For square radii it proves"),
    (r"\section{Quadratic radii}", r"\section{Square radii}"),
    ("At quadratic $n=14$", "For square radii and $n=14$"),
    ("Certified global brackets for quadratic radii.", "Certified global brackets for square radii."),
    ("Normalized linear and quadratic brackets.", "Normalized brackets for linear and square radii."),
    # Cite the lower bound on C_2 from revised Paper II. Figure 5 still draws
    # only the upper bound, so the sentence about the figure names both.
    (
        r"constant $C_2<\CtwoUpper$. Figure~\ref{fig:ratios} places these bounds on the "
        r"limiting constants alongside the finite brackets.",
        r"constant $C_2$ with $\CtwoLower\le C_2<\CtwoUpper$. Figure~\ref{fig:ratios} places "
        r"the bounds on $C_*$ and the upper bound on $C_2$ alongside the finite brackets.",
    ),
)


def edited(text):
    for old, new in EDITORIAL:
        assert text.count(old) == 1, old
        text = text.replace(old, new)
    return text


def test_every_scientific_section_and_appendix_matches_the_reviewed_source():
    reviewed = scientific_text(REVIEWED)
    assert hashlib.sha256(reviewed.encode()).hexdigest() == "2d6c96dd7319ea76b820c9968746c4a3a60284c343761631fd6eb2829569cd7a"
    assert scientific_text(JOGO) == edited(reviewed)
    theorem = r"\\newtheorem[^\n]+"
    assert re.findall(theorem, tex(JOGO)) == re.findall(theorem, tex(REVIEWED))
    macros = r"\\newcommand\{\\(?:Rchain|Rfull|Rstar|snapshot)\}[^\n]+"
    assert re.findall(macros, tex(JOGO)) == re.findall(macros, tex(REVIEWED))


def test_six_original_artworks_and_two_official_style_files():
    source = tex(JOGO)
    paths = re.findall(r"\\includegraphics\[[^\]]+\]\{([^{}]+)\}", source)
    assert paths == [f"Fig{i}.pdf" for i in range(1, 7)]
    for path, original in zip(paths, FIGURES, strict=True):
        assert (JOGO / path).read_bytes() == (REVIEWED / "figures" / f"{original}.pdf").read_bytes()
    for name, digest in {
        "sn-jnl.cls": "36d0c3273a59d48dc6a9c7b080dfa1ec50dc10229d8751568d1f2e490ffa5ecc",
        "sn-mathphys-num.bst": "b3a7c7fbcc1e7f9619de634fcea2f5bb7a245818a5942bc576e40ea001633332",
    }.items():
        assert hashlib.sha256((JOGO / name).read_bytes()).hexdigest() == digest
    assert r"\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}" in source


def test_exported_table_bodies_match_every_printed_table(tmp_path):
    exporter = runpy.run_path(str(JOGO / "export_tables.py"))
    exporter["export"](tmp_path)
    blocks = re.findall(r"\\begin\{table\}.*?\\end\{table\}", tex(JOGO), re.S)
    assert len(blocks) == len(list(tmp_path.glob("*.tex"))) == 8
    for block in blocks:
        name = re.search(r"\\label\{tab:(\w+)\}", block)[1]
        body = re.search(r"\\begin\{tabularx?\}.*?\\end\{tabularx?\}", block, re.S)[0]
        assert tex(tmp_path, f"{name}.tex").strip() == body


def test_editorial_fixes_declarations_and_front_matter():
    old, new = tex(REVIEWED), tex(JOGO)
    abstract = new.split(r"\abstract{", 1)[1].split("}\n\n" + r"\keywords", 1)[0]
    assert 150 <= len(abstract.split()) <= 250
    assert "any finite list of at least three distinct positive integer radii" in " ".join(abstract.split())
    start = r"For radii $1,\ldots,n$"
    assert abstract.split(start)[1] == old.split(start, 1)[1].split(r"\end{abstract}", 1)[0].rstrip()
    assert r"\date{September 19, 2026}" in new
    assert r"\pacs[Mathematics Subject Classification (2020)]{52C26,52C15,05C85,90C27}" in new
    upper = "\\newcommand{\\CtwoUpper}"
    lower = "\\newcommand{\\CtwoLower}{(434+4\\sqrt{2})/(1587\\pi)}\n"
    assert tex(REVIEWED, "numbers.tex").count(upper) == 1
    assert tex(JOGO, "numbers.tex") == tex(REVIEWED, "numbers.tex").replace(upper, lower + upper) + (
        "\\newcommand{\\GeneralRadiiCommit}{[commit after merge]}\n"
    )
    marker = r"\section{Data and code availability}"
    expected = old.split(marker)[1].split(r"\section*{Statements and Declarations}")[0]
    expected = expected.replace("the linked revision", r"revision \GeneralRadiiCommit")
    assert new.split(marker)[1].split(r"\backmatter")[0] == expected
    heading = r"\section*{Statements and Declarations}"
    declarations = old.split(heading)[1].split(r"\input{references.tex}")[0].strip()
    note = "% author: add Claude (Anthropic) to this statement"
    assert new.split(heading)[1].split(r"\bibliography{references}")[0].strip() == declarations + "\n" + note


def test_bibliography_keeps_all_cited_keys_and_dois():
    original = dict(re.findall(
        r"\\bibitem\{([^}]+)\}\s*\\href\{https://doi\.org/([^}]+)\}", tex(REVIEWED, "references.tex")
    ))
    records = re.findall(r"^@\w+\{([^,]+),(.*?)^}", tex(JOGO, "references.bib"), re.M | re.S)
    actual = {key: re.search(r"\bdoi\s*=\s*\{([^}]+)\}", fields)[1] for key, fields in records}
    assert len(records) == len(original) == 16
    assert actual == original
    assert set(re.findall(r"\\cite\{([^}]+)\}", tex(JOGO))) == set(original)


def test_build_rejects_unresolved_citations_and_boxes_over_one_point():
    check_log = BUILD["check_log"]
    assert check_log(r"Overfull \hbox (1.0pt too wide) in paragraph") == 1.0
    with pytest.raises(ValueError, match="above 1 pt"):
        check_log(r"Overfull \vbox (1.001pt too high) has occurred while output is active")
    with pytest.raises(ValueError, match="Unresolved"):
        check_log("Package natbib Warning: Citation 'example' on page 1 undefined.")


@pytest.mark.skipif(
    not all(shutil.which(name) for name in ("pdflatex", "bibtex", "pdfinfo")),
    reason="the JOGO PDF build needs pdflatex, bibtex and pdfinfo",
)
def test_three_pass_build_and_single_source_upload(tmp_path):
    output, package = tmp_path / "review.pdf", tmp_path / "upload.zip"
    result = subprocess.run(
        [sys.executable, str(JOGO / "build.py"), "--output", str(output), "--submission-zip", str(package)],
        check=True, stdin=subprocess.DEVNULL, capture_output=True, text=True,
    )
    assert "pdflatex_passes=3 bibtex_runs=1 unresolved=0" in result.stdout
    assert "overfull_above_1pt=0" in result.stdout
    with ZipFile(package) as archive:
        assert sorted(n for n in archive.namelist() if n.endswith(".tex")) == ["main.tex"]
        assert all("/" not in n for n in archive.namelist())
        assert archive.read("main.pdf") == output.read_bytes()
        assert archive.read("main.tex").decode() == tex(JOGO).replace(
            r"\input{numbers.tex}", tex(JOGO, "numbers.tex").rstrip()
        )
        for filename in BUILD["INPUTS"]:
            expected = (JOGO / filename).read_bytes()
            if filename == "references.bib":
                expected = expected.replace(b"\r\n", b"\n")
            assert archive.read(filename) == expected
        bibliography = archive.read("main.bbl")
        assert len(re.findall(rb"\\bibitem(?:\[|\{)", bibliography)) == 16
        assert b"???" not in bibliography
        assert b"arXiv:2609.13630v3" in bibliography
        assert b"6157a64f7628e327b390d9ddd21dd3507d6035a2" in bibliography
