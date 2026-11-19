"""Produce three deterministic vector figures for the Paper II journal draft."""
import argparse
from fractions import Fraction
import hashlib
from math import sqrt
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

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


def reflected_cells():
    fig,(cell,perm) = plt.subplots(1,2,figsize=(6.3,1.85),
                                    gridspec_kw={"width_ratios":[1.35,1]})
    cell.axis("off")
    cell.set(xlim=(-0.35,4.35),ylim=(-0.53,1.03))
    xs = list(range(5))
    cell.plot(xs,[0]*5,color="0.3",lw=1.4,zorder=1)
    labels = [r"$P_{i-1}$",r"$i$",r"$P_i$",r"$i+1$",r"$P_{i+1}$"]
    for x,label in zip(xs,labels):
        cell.plot(x,0,"o",mec="0.12",mfc="white" if x%2 else "0.23",ms=6)
        cell.text(x,-0.13,label,ha="center",va="top")
    for x in (0,2):
        cell.add_patch(FancyArrowPatch((x,0.07),(x+2,0.07),
                       connectionstyle="arc3,rad=-0.48",arrowstyle="-",
                       linestyle="--",lw=1,color="0.35"))
    cell.text(2,0.91,"Alternating cells",ha="center")
    ranks = range(1,9)
    images = [1,6,3,4,5,2,7,8]
    perm.set(xlim=(0.45,8.55),ylim=(0.35,8.65),xticks=[1,2,4,6,8],yticks=[1,2,4,6,8],
             xlabel=r"rank $i$",ylabel=r"$J(i)$")
    perm.axvspan(0.55,6.45,facecolor="0.94")
    perm.plot([1,8],[1,8],":",color="0.48",lw=0.9)
    for i,j in zip(ranks,images):
        perm.plot(i,j,"o",mec="0.13",mfc="0.18" if i!=j else "white",ms=4.4)
    perm.set_title("Even-rank reversal",fontsize=9,pad=3)
    perm.tick_params(labelsize=7,length=2)
    fig.subplots_adjust(left=0.025,right=0.98,bottom=0.24,top=0.90,wspace=0.33)
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
    text = numbers.read_text(encoding="utf-8")
    def macro(key):
        match = re.search(r"\\newcommand\{\\"+key+r"\}\{([0-9]+\.[0-9]+)\}",text)
        return Fraction(match[1]) if match else None
    lower,upper = macro("CstarLower"),macro("CstarUpper")
    if lower is None or (upper is None and
            r"\newcommand{\CstarUpper}{\textbf{[certified upper bound pending]}}" not in text):
        raise ValueError("unrecognized bound macro")
    if upper is not None and upper <= lower:
        raise ValueError("the numeric upper endpoint must exceed the lower one")
    fig,ax = plt.subplots(figsize=(5.45,2.2))
    n = [i for i,_,_ in bounds]
    middle = [float((l+u)/(2*i*i)) for i,l,u in bounds]
    ax.errorbar(n,middle,yerr=[[float((u-l)/(2*i*i)) for i,l,u in bounds]]*2,
                fmt="o",color="0.14",ms=3.8,lw=1,capsize=2,
                label=r"Finite bracket for $R^*(n)/n^2$")
    ax.axhline(float(lower),color="0.28",ls="--",lw=1.0,
               label=r"Lower bound for $C_*$")
    if upper is not None:
        ax.axhline(float(upper),color="0.1",ls=":",lw=1.2,label=r"Upper bound for $C_*$")
    ax.set(xlim=(2.55,14.45),xticks=n,xlabel=r"Number of outer circles $n$",
           ylabel=r"Normalized radius",ylim=(0.015,max(0.155,float(upper or 0)+0.012)))
    ax.grid(axis="y",alpha=0.27,ls=":",lw=0.7)
    ax.legend(frameon=False,fontsize=7.8,loc="lower right")
    fig.subplots_adjust(left=0.13,right=0.98,top=0.96,bottom=0.22)
    return fig


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--output", type=Path, default=HERE/"figures")
    args.add_argument("--brackets", type=Path, default=HERE/"figures/bracket_rows.tex")
    args.add_argument("--numbers", type=Path, default=HERE/"numbers.tex")
    options = args.parse_args()
    options.output.mkdir(parents=True,exist_ok=True)
    with plt.rc_context(MAT_STYLE):
        plots = [("line_geometry",line_model()),("reflected_cells",reflected_cells()),
                 ("finite_brackets",finite_brackets(options.brackets,options.numbers))]
        for name,fig in plots:
            path = options.output/(name+".pdf")
            fig.savefig(path,format="pdf",metadata=META)
            plt.close(fig)
            print(name,hashlib.sha256(path.read_bytes()).hexdigest())


if __name__=="__main__":
    main()
