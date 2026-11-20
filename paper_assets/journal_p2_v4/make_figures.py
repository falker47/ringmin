"""Produce the two journal figures for the Paper II journal draft."""
import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
from math import sqrt
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
TABLE_SHA = "58666265324e0cf9c3ad7cf811107f795893ccf0e43954fec2ce65d32d93a5d1"
MAT_STYLE = {"font.family": "DejaVu Sans", "font.size": 9,
             "pdf.fonttype": 42, "axes.spines.top": False,
             "axes.spines.right": False, "axes.labelcolor": "0.1",
             "xtick.color": "0.2", "ytick.color": "0.2"}
META = {"Title": None, "CreationDate": None, "ModDate": None,
        "Creator": "Ringmin Paper II figures", "Author": "Maurizio Falconi"}


def line_model():
    fig, ax = plt.subplots(figsize=(4.7, 2.05))
    ax.set_aspect("equal")
    ax.axis("off")
    # These choices make the horizontal center separation exactly 4/3.
    a, b = 1, 4/9
    xi, xj = 0, sqrt(a*b)
    ax.plot([-1.25, 2.18], [0, 0], color="0.15", lw=1)
    for x, r, shade, label, horizontal in [(xi,a,"0.93","i",-0.14),
                                           (xj,b,"white","j",0.15)]:
        xy = (2*x,r)
        ax.add_patch(Circle(xy,r,facecolor=shade,edgecolor="0.18",lw=1.25))
        ax.plot([2*x,2*x],[0,r],ls="--",color="0.4",lw=0.85)
        ax.plot(*xy,"o",ms=3.5,color="0.13")
        ax.text(2*x+horizontal,r/2,f"$a_{label}$",ha="center",va="center")
        ax.text(2*x,r+0.12,f"$(2x_{label},a_{label})$",ha="center",va="bottom")
    ax.annotate("",(2*xj,-0.20),(2*xi,-0.20),
                arrowprops={"arrowstyle":"<->","lw":1,"color":"0.2"})
    ax.text(xj,-0.25,r"$2(x_j-x_i)=2\sqrt{a_i a_j}$",ha="center",va="top")
    ax.set(xlim=(-1.25,2.25),ylim=(-0.57,2.09))
    fig.subplots_adjust(left=0.01,right=0.99,top=0.97,bottom=0.01)
    return fig


def finite_brackets(table, numbers):
    raw = table.read_bytes()
    if hashlib.sha256(raw.replace(b"\r\n",b"\n")).hexdigest() != TABLE_SHA:
        raise ValueError("unexpected contents in the Paper I bracket table")
    matches = re.findall(rb"(?m)^(\d+)\s*&\s*([\d.]+)\s*&\s*([\d.]+)\s*&", raw)
    bounds = [(int(n),Fraction(l.decode()),Fraction(u.decode())) for n,l,u in matches]
    if [n for n,_,_ in bounds] != list(range(3,15)) or any(
            u-l != Fraction(1,10**11) for _,l,u in bounds):
        raise ValueError("expected the twelve displayed Paper I enclosures")
    definitions = numbers.read_text(encoding="utf-8")

    def endpoint(key):
        match = re.search(r"\\newcommand\{\\" + key + r"\}\{(\d+\.\d+)\}", definitions)
        if match is None:
            raise ValueError(f"expected a decimal value for {key}")
        return Decimal(match[1])

    lower, upper = endpoint("CstarLower"), endpoint("CstarUpper")
    if upper <= lower:
        raise ValueError("the upper endpoint must exceed the lower endpoint")

    fig, (ax, detail) = plt.subplots(
        1, 2, figsize=(6.3, 2.4), gridspec_kw={"width_ratios": [4, 1]})
    n = [i for i, _, _ in bounds]
    middle = [float((l+u)/(2*i*i)) for i, l, u in bounds]
    half_width = [float((u-l)/(2*i*i)) for i, l, u in bounds]
    ax.errorbar(n, middle, yerr=half_width, fmt="o", color="0.14",
                ms=3.8, lw=1, capsize=2, label=r"Finite $R^*(n)/n^2$")
    lo, hi = float(lower), float(upper)
    for panel in (ax, detail):
        panel.axhspan(lo, hi, facecolor="0.76", label=r"Band for $C_*$")
        panel.axhline(lo, color="0.25", lw=0.65)
        panel.axhline(hi, color="0.25", lw=0.65)
    ax.set(xlim=(2.55, 14.45), xticks=n, xlabel=r"Number of outer circles $n$",
           ylabel="Normalized radius", ylim=(0.015, max(0.155, hi+0.012)))
    ax.grid(axis="y", alpha=0.27, ls=":", lw=0.7)
    ax.legend(frameon=False, fontsize=8, loc="lower right")

    margin = (hi-lo)*0.65
    detail.set(xticks=[], ylim=(lo-margin, hi+margin), yticks=[lo, hi],
               yticklabels=[str(lower), str(upper)], title=r"$C_*$ band")
    detail.yaxis.tick_right()
    detail.tick_params(axis="y", labelsize=8, length=0, pad=4)
    for spine in detail.spines.values():
        spine.set_visible(False)
    fig.subplots_adjust(left=0.11, right=0.83, bottom=0.22, top=0.87, wspace=0.22)
    return fig


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--output", type=Path, default=HERE/"figures")
    args.add_argument("--brackets", type=Path, default=HERE/"figures/bracket_rows.tex")
    args.add_argument("--numbers", type=Path, default=HERE/"numbers.tex")
    options = args.parse_args()
    options.output.mkdir(parents=True,exist_ok=True)
    with plt.rc_context(MAT_STYLE):
        plots = [("line_geometry", line_model()),
                 ("finite_brackets", finite_brackets(options.brackets, options.numbers))]
        for name,fig in plots:
            path = options.output/(name+".pdf")
            fig.savefig(path,format="pdf",metadata=META)
            plt.close(fig)
            print(name,hashlib.sha256(path.read_bytes()).hexdigest())


if __name__=="__main__":
    main()
