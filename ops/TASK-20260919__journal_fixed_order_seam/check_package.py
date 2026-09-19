"""Read-only package, link, whitespace and protected-path audit."""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import re
import runpy
import subprocess


ROOT = Path(__file__).resolve().parents[2]
TASK = "ops/TASK-20260919__journal_fixed_order_seam"
PROOF = "research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md"
BASE = "2169bd429e25682777175ed31248b76feea8fabd"
ZIP = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
ZIP_HASH = "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db"
ALLOWED = {
    PROOF, "CURRENT_STATUS.md", "knowledge/FIXED_ORDER_THEORY.md",
    "research/NEXT_RESEARCH_STEPS.md",
    *(f"{TASK}/{name}" for name in
      ("TASK_STATUS.md", "TASK_LOG.md", "EVIDENCE.md", "check_exact.py", "check_package.py")),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", *args],
        cwd=ROOT, text=True, encoding="utf-8"
    )


changed = set(git("diff", "--name-only", BASE).splitlines())
untracked = set(git("ls-files", "--others", "--exclude-standard").splitlines())
require((changed | untracked) - ALLOWED == {ZIP}, "out-of-scope changes or missing ZIP")
require(ZIP not in git("diff", "--cached", "--name-only").splitlines(), "ZIP staged")
require(sha256((ROOT / ZIP).read_bytes()).hexdigest() == ZIP_HASH, "ZIP changed")
require(not (ROOT / "paper_assets/journal_dcg").exists(), "journal directory created")
print("scope: PASS; only nine allowed task paths differ/add; protected tracked paths unchanged; exempt ZIP hash unchanged and unstaged")

links = 0
for name in sorted(ALLOWED):
    path = ROOT / name
    data = path.read_bytes()
    content = data.decode("utf-8")
    require(not content.startswith("\ufeff"), f"BOM: {name}")
    require(content.endswith("\n") and not content.endswith("\n\n"), f"final newline: {name}")
    for number, line in enumerate(content.splitlines(), 1):
        require(line == line.rstrip(), f"trailing whitespace: {name}:{number}")
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#")[0]
            require((path.parent / target).exists(), f"missing link: {name}: {target}")
            links += 1
print(f"files: PASS; nine complete files inspected for whitespace/UTF-8; {links} local link targets exist")

text = (ROOT / PROOF).read_text(encoding="utf-8")
require(text.count("$$") % 2 == 0, "display delimiter balance")
require(text.replace("$$", "").count("$") % 2 == 0, "inline delimiter balance")
require([int(x) for x in re.findall(r"\\tag\{(\d+)\}", text)] == list(range(1, 22)), "equation numbering")
namespace = runpy.run_path(str(ROOT / TASK / "check_exact.py"))
section = text.split("Numerators of $(q_e)$, in order |", 1)[1].split("For example,", 1)[0]
table_rows = [line for line in section.splitlines() if line.startswith("| $(")]
require(len(table_rows) == 6, "six bridge vector rows")
for line, (k, n, radius, den, nums, direction, _) in zip(table_rows, namespace["ROWS"]):
    cells = [cell.strip() for cell in line.split("|")[1:-1]]
    require(cells[0] == f"$({k},{n})$", "table index")
    require(Fraction(cells[1].strip("$")) == radius, "table radius")
    require(cells[2] == direction and int(cells[3]) == den, "table direction/denominator")
    require([int(x) for x in cells[4].split(",")] == nums, "table vector drift")
minimum_block = text.split("respectively,", 1)[1].split(r"\tag{19}", 1)[0]
minima = [Fraction(int(a), int(b)) for a, b in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", minimum_block)]
expected = [Fraction(43, 30000), Fraction(4333, 26270000), Fraction(32, 359375), Fraction(3, 32500), Fraction(23, 70000), Fraction(1, 5625)]
require(minima == expected, "proof minimum margins drift")
status = (ROOT / "CURRENT_STATUS.md").read_text(encoding="utf-8")
require(status.count("## Exactly one next atomic task") == 1, "next task heading")
require(status.split("## Exactly one next atomic task")[1].strip() ==
        "Independent STRICT review of the theorem package\n`research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md` and its task-local evidence.", "next task scope")
print("publication transcription: PASS; 21 equation labels, six rational vectors (67 edges), six minimum margins, exactly one next task")
for name in (PROOF, f"{TASK}/check_exact.py"):
    print(f"SHA256 {name} {sha256((ROOT / name).read_bytes()).hexdigest()}")
print("PASS: package and protected-path audit; no mathematical acceptance or hosted-CI assertion")
