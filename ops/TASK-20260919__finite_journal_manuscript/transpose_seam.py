"""Mechanical first-pass TeX transposition of the accepted, protected proof.

The delivered appendix is reviewed as TeX. This script is task provenance,
not a mathematical premise or a build dependency.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
source = (ROOT / "research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md").read_text(encoding="utf-8")
source = source.split("## 1. Definitions and statement\n", 1)[1].split("## 7.", 1)[0]
source = "## 1. Definitions and statement\n" + source
source = re.sub(r"   \| Smallest radius.*?   \| \$k=3\$.*?\n", "   " + r"\[\begin{array}{c|c|c}k & \Delta_{k,n}>0 & \Delta_{k,n}<0\\1&3\le n\le7&n\ge8\\2&4\le n\le12&n\ge13\\3&5\le n\le16&n\ge17\end{array}\]".replace("\\", "\\\\") + "\n", source, flags=re.S)

def inline(text):
    text = text.replace("Lemma 1", "Lemma A.1").replace("Lemma 2", "Lemma A.2")
    text = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\emph{\1}", text)
    parts = re.split(r"(\$[^$]*\$)", text)
    text = "".join(p if p.startswith("$") else re.sub(r"\((\d+)\)", r"\\eqref{eq:seam\1}", p) for p in parts)
    text = re.sub(r"(?i)sections? (\d)(?:\.(\d))?", lambda m: "Appendix~A." + m[1] + ("." + m[2] if m[2] else ""), text)
    return text.replace("$\\square$", r"\hfill$\square$")

out = ["% Transposed from accepted baseline 6c16af4; proof is included in full.",
       r"\section{Self-contained seam theorem and proof}\label{app:seam}"]
lines = source.splitlines()
i = 0
table = 1
while i < len(lines):
    line = lines[i]
    if line.strip() == "$$":
        block = []
        i += 1
        while i < len(lines) and lines[i].strip() != "$$":
            block.append(lines[i])
            i += 1
        math = "\n".join(block)
        math = re.sub(r"\\tag\{(\d+)\}", r"\\tag{A.\1}\\label{eq:seam\1}", math)
        out.extend([r"\[", math, r"\]"])
    elif line.startswith("### ") or line.startswith("## "):
        level = "subsubsection" if line.startswith("### ") else "subsection"
        heading = re.sub(r"^#+ \d+(?:\.\d+)?\.? ", "", line)
        out.append("\\" + level + "{" + inline(heading) + "}")
    elif line.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", c) for c in row):
                rows.append(row)
            i += 1
        i -= 1
        table += 1
        specs = ["lXX", "lrrrll", "lrllX", "lXl"]
        captions = [
            "The three complete strict classifications in the seam theorem.",
            "Exact threshold comparisons; all displayed square margins are positive.",
            "Rational edge bounds, in the order of \\eqref{eq:seam5}.",
            "Exact chain comparisons for the six endpoint bridges.",
        ]
        out.extend([r"\begin{table}[htbp]\centering\small", "\\caption{" + captions[table-1] + "}",
                    "\\label{tab:seam"+str(table)+"}", r"\setlength{\tabcolsep}{5pt}"])
        env = "tabularx" if "X" in specs[table-1] else "tabular"
        out.append("\\begin{"+env+"}" + (r"{\textwidth}" if env == "tabularx" else "") + "{"+specs[table-1]+"}")
        out.append(r"\toprule")
        for j, row in enumerate(rows):
            out.append(" & ".join(inline(c) for c in row) + r" \\")
            if j == 0:
                out.append(r"\midrule")
        out.extend([r"\bottomrule", "\\end{"+env+"}", r"\end{table}"])
    elif re.match(r"^(?:- |\d+\. )", line):
        ordered = not line.startswith("- ")
        env = "enumerate" if ordered else "itemize"
        out.append("\\begin{"+env+"}")
        while i < len(lines):
            line = lines[i]
            if re.match(r"^(?:- |\d+\. )", line):
                out.append(r"\item " + inline(re.sub(r"^(?:- |\d+\. )", "", line)))
            elif line.startswith("  "):
                out.append(inline(line.lstrip()))
            elif not line.strip() and i+1 < len(lines) and re.match(r"^(?:- |\d+\. |  )", lines[i+1]):
                out.append("")
            else:
                break
            i += 1
        i -= 1
        out.append("\\end{"+env+"}")
    else:
        out.append(inline(line))
    i += 1
target = ROOT / "paper_assets/journal_dcg/seam_appendix.tex"
target.parent.mkdir(parents=True, exist_ok=True)
tex = "\n".join(out).rstrip()+"\n"
tex = tex.replace("\\item For $k=1,2,3$, the complete classifications are:",
                  "\\item For $k=1,2,3$, the complete classifications are:\\nopagebreak[4]")
tex = tex.replace("The indicated margins are strictly", "The margins in Table~\\ref{tab:seam2} are strictly")
tex = tex.replace("In the table below, the displayed integer", "In Table~\\ref{tab:seam3}, the displayed integer")
tex = tex.replace("Thus every closure comparison has the following exact rational bound:",
                  "Table~\\ref{tab:seam4} gives an exact rational bound for every closure comparison.")
tex = tex.replace("Appendix~A.6.1 and 6.2", "Appendices~A.6.1 and A.6.2")
target.write_text(tex, encoding="utf-8", newline="\n")
print("Transposed sections 1-6, 21 tagged equations, one classification array and three rational tables.")
