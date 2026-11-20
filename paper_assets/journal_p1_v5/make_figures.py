"""Reproduce the six editable vector figures from the finite-paper inputs."""

import argparse
import json
import re
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import degrees
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CERTIFICATE = (
    REPO
    / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json"
)
META = {"Creator": "Ringmin journal figures", "CreationDate": None, "ModDate": None}
FIGURES = (
    "01_kernel",
    "02_necklace",
    "03_seam",
    "04_witness",
    "05_ratios",
    "06_deficits",
)


def rank_cycle(k, n):
    count = n - k + 1
    half = (count + 1) // 2

    def arm(low, high):
        result = []
        while low <= half or high > half:
            if low <= half:
                result.append(low)
            if high > half:
                result.append(high)
            low += 2
            high -= 2
        return result

    ranks = arm(1, count - 1) + arm(2, count - 2)[::-1] + [count]
    return [rank + k - 1 for rank in ranks]


def angle(radius, a, b):
    return 2 * mp.asin(mp.sqrt(mp.mpf(a) * b / ((radius + a) * (radius + b))))


@lru_cache(maxsize=None)
def chain(k, n):
    with mp.workdps(65):
        order = rank_cycle(k, n)
        edge = list(zip(order, order[1:] + order[:1]))

        def residual(r):
            return mp.fsum(angle(r, a, b) for a, b in edge) - 2 * mp.pi

        lo, hi = mp.mpf(0), mp.mpf(n * n)
        while residual(hi) > 0:
            hi *= 2
        r = mp.findroot(residual, (lo, hi), solver="anderson")
        if r <= 0 or abs(residual(r)) > mp.mpf("1e-55"):
            raise ValueError("chain root did not converge")
        phi = mp.mpf(0)
        centers = {}
        for a, b in edge:
            centers[a] = ((r + a) * mp.cos(phi), (r + a) * mp.sin(phi))
            phi += angle(r, a, b)
        deficit = angle(r, n, k) + angle(r, k, n - 1) - angle(r, n, n - 1)
        return r, centers, deficit


def bracket_rows(filename="bracket_rows.tex"):
    rows = {}
    pattern = r"^\s*(\d+)\s*&\s*([\d.]+)\s*&\s*([\d.]+)\s*&\s*(\d+)"
    for row in (HERE / filename).read_text(encoding="utf-8").splitlines():
        hit = re.match(pattern, row)
        if hit:
            n, lower, upper, _ = hit.groups()
            rows[int(n)] = Fraction(lower), Fraction(upper)
    if tuple(rows) != tuple(range(3, 15)) or any(
        b - a != Fraction(1, 10**11) for a, b in rows.values()
    ):
        raise ValueError("incomplete or inconsistent bracket table")
    return rows


def witness14(case):
    """Reconstruct each center from the first witness and verify every pair."""
    if case["n"] != 14 or set(case["upper_witnesses"][0]["order"]) != set(range(1, 15)):
        raise ValueError("invalid witness labels")
    radius = Fraction(case["U"])
    if radius != bracket_rows()[14][1]:
        raise ValueError("witness radius does not equal the manuscript endpoint")
    w = case["upper_witnesses"][0]
    params = w["exact_cartesian_check"]["stereographic_parameters"]
    centers = {}
    for a, entry in zip(w["order"], params, strict=True):
        t = Fraction(int(entry["numerator"]), int(entry["denominator"]))
        if a in centers:
            raise ValueError("repeated witness label")
        mul = (radius + a) / (1 + t * t)
        x, y = mul * (1 - t * t), mul * 2 * t
        if x * x + y * y != (radius + a) ** 2:
            raise ValueError(f"central tangency failed for {a}")
        centers[a] = x, y
    for a, b in combinations(centers, 2):
        x, y = centers[a]
        u, v = centers[b]
        if (x - u) ** 2 + (y - v) ** 2 <= (a + b) ** 2:
            raise ValueError(f"strict separation failed for {a},{b}")
    return radius, centers


def geometry(ax, radius, centers, highlight=(), callouts=(), label_center="R"):
    r = float(radius)
    ax.add_patch(Circle((0, 0), r, facecolor="0.94", edgecolor="0.25", lw=1.0))
    ax.text(0, -0.07 * r, label_center, ha="center", va="center", fontsize=9)
    limits = [-r, r, -r, r]
    for a, (xx, yy) in centers.items():
        x, y = float(xx), float(yy)
        dark = a in highlight
        ax.add_patch(
            Circle(
                (x, y),
                a,
                facecolor="0.78" if dark else "white",
                edgecolor="0.13",
                linewidth=1.4 if dark else 0.85,
            )
        )
        if a in callouts:
            ax.annotate(
                str(a),
                (x, y),
                xytext=(1.55 * x, 0.58 * y),
                ha="center",
                va="center",
                fontsize=8.5,
                arrowprops={"arrowstyle": "-", "lw": 0.8, "color": "0.15"},
            )
        else:
            ax.text(x, y, str(a), ha="center", va="center", fontsize=7.4)
        limits = [
            min(limits[0], x - a),
            max(limits[1], x + a),
            min(limits[2], y - a),
            max(limits[3], y + a),
        ]
    pad = 0.04 * max(limits[1] - limits[0], limits[3] - limits[2])
    ax.set(
        xlim=(limits[0] - pad, limits[1] + pad),
        ylim=(limits[2] - pad, limits[3] + pad),
        aspect="equal",
    )
    ax.set_axis_off()


def kernel_plot(ax):
    r, a, b = 3, 1, 2
    t = float(angle(r, a, b))
    x, y = (r + b) * mp.cos(t), (r + b) * mp.sin(t)
    ax.add_patch(Circle((0, 0), r, facecolor="0.93", edgecolor="0.25", lw=1))
    ax.add_patch(Circle((r + a, 0), a, facecolor="white", edgecolor="black"))
    ax.add_patch(Circle((float(x), float(y)), b, facecolor="white", edgecolor="black"))
    ax.plot([r + a, 0, float(x)], [0, 0, float(y)], color="0.3", lw=0.9)
    ax.plot([0, r + a, float(x)], [0, 0, float(y)], "k.", ms=3)
    ax.add_patch(Arc((0, 0), 2.8, 2.8, theta1=0, theta2=degrees(t), lw=1))
    ax.text(1.6, 0.22, r"$\theta$", size=9, ha="left")
    ax.text(-1.45, -1.35, r"$R$", size=10)
    ax.text(r + a + 0.12, -0.48, r"$a$", size=10)
    ax.text(float(x) + 0.17, float(y) + 0.48, r"$b$", size=10)
    ax.set(xlim=(-3.4, 7), ylim=(-3.3, 5.3), aspect="equal")
    ax.set_axis_off()


def number(name):
    pat = r"^\\newcommand\{\\" + name + r"\}\{(\d+\.\d+)\}$"
    content = (HERE / "numbers.tex").read_text(encoding="utf-8")
    match = re.search(pat, content, re.MULTILINE)
    if not match:
        raise ValueError(f"missing numeric Paper II bound: {name}")
    return Fraction(match[1])


def ratio_plot(ax):
    linear_lo = float(number("CstarLower"))
    linear_hi = float(number("CstarUpper"))
    quadratic_hi = float(number("CtwoUpper"))
    ax.axhspan(linear_lo, linear_hi, color="0.55", zorder=0)
    ax.axhline(quadratic_hi, ls=":", lw=1, color="0.25")
    ax.text(3, linear_hi + 0.002, r"$C_*$ bounds", va="bottom")
    ax.text(3, quadratic_hi + 0.002, r"$C_2$ upper bound", va="bottom")
    series = (
        ("bracket_rows.tex", 2, "o", "black", r"$R^*(n)/n^2$"),
        ("quadratic_brackets.tex", 3, "^", "white", r"$R_2^*(n)/n^3$"),
    )
    for filename, exponent, marker, face, label in series:
        rows = bracket_rows(filename)
        ns = list(rows)
        lower = [lo / n**exponent for n, (lo, _) in rows.items()]
        upper = [hi / n**exponent for n, (_, hi) in rows.items()]
        mid = [float((lo + hi) / 2) for lo, hi in zip(lower, upper, strict=True)]
        ax.vlines(ns, list(map(float, lower)), list(map(float, upper)), colors="black")
        ax.plot(ns, mid, ls="none", marker=marker, ms=3.6, color="black",
                markerfacecolor=face, label=label)
    ax.set(
        xlabel=r"Number of outer circles $n$",
        ylabel="Normalized central radius",
        xticks=[3, 5, 7, 9, 11, 14],
        xlim=(2.5, 14.5),
        ylim=(0, 0.165),
    )
    ax.legend(frameon=False, fontsize=8, loc="lower right", handlelength=1)


def deficits_plot(ax):
    for k, style, marker in ((1, "-", "o"), (2, "--", "s"), (3, ":", "^")):
        ns = range(k + 2, 22)
        ax.plot(
            ns,
            [float(chain(k, n)[2]) for n in ns],
            linestyle=style,
            marker=marker,
            lw=1,
            ms=2.7,
            color="0.12",
            label=f"$k={k}$",
        )
    ax.axhline(0, lw=0.65, color="0.44")
    for k, n in ((1, 8), (2, 13), (3, 17)):
        ax.plot(n, float(chain(k, n)[2]), "o", ms=6, mfc="none", mec="0.1", mew=0.8)
    ax.set(
        xlabel=r"Largest radius $n$",
        ylabel=r"Seam deficit $\Delta_{k,n}$ (rad)",
        xticks=[3, 8, 13, 17, 21],
        xlim=(2.5, 21.5),
    )
    ax.legend(frameon=False, fontsize=7, ncol=3)


def make_figures(out):
    out.mkdir(parents=True, exist_ok=True)
    cert = json.loads(CERTIFICATE.read_bytes())["certificate"]
    case = next(c for c in cert["cases"] if c["n"] == 14)
    witness_radius, witness_centers = witness14(case)
    print("PASS_WITNESS_14 central=14 strict_outer_pairs=91")
    style = {
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "pdf.fonttype": 42,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.65,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
    }
    with plt.rc_context(style):
        for i, name in enumerate(FIGURES):
            fig, ax = plt.subplots(figsize=(3.12, 2.35))
            if i == 0:
                kernel_plot(ax)
            elif i in (1, 2):
                n = 6 + i
                radius, centers, _ = chain(1, n)
                geometry(ax, radius, centers, highlight=(7, 8) if n == 8 else ())
                if n == 8:
                    a, b = centers[7], centers[8]
                    ax.plot(
                        [float(a[0]), float(b[0])],
                        [float(a[1]), float(b[1])],
                        ls="--",
                        color="0.35",
                        lw=0.65,
                        zorder=1,
                    )
            elif i == 3:
                geometry(
                    ax,
                    witness_radius,
                    witness_centers,
                    highlight=(1, 2),
                    callouts=(1, 2),
                )
            elif i == 4:
                ratio_plot(ax)
            else:
                deficits_plot(ax)
            fig.tight_layout(pad=0.45)
            fig.savefig(out / (name + ".pdf"), format="pdf", metadata=META)
            plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE / "figures")
    make_figures(parser.parse_args().output_dir)
