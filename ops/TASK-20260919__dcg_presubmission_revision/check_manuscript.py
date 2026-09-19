"""Revision-local transcription/scope audit, adapted from the accepted manuscript checker.
Not a mathematical verifier or independent acceptance decision."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper_assets/journal_dcg"
BASE = "bfc2caff2ae6b1d1f149eb52cac4dc220dcf85d6"

def need(test, message):
    if not test:
        raise ValueError(message)

def clean_math(s):
    s = re.sub(r"\\tag\{[^}]*\}|\\label\{[^}]*\}", "", s)
    return re.sub(r"\s+", "", s)

def manifest_revision_baseline():
    return json.loads((PAPER/"BUILD_MANIFEST.json").read_text())["revision_baseline_commit"]


def main():
    source = (ROOT / "research/JOURNAL_FIXED_ORDER_SEAM_THEOREM.md").read_text(encoding="utf-8")
    source = source.split("## 1.", 1)[1].split("## 7.", 1)[0]
    seam = (PAPER / "seam_appendix.tex").read_text(encoding="utf-8")
    original = re.findall(r"\$\$(.*?)\$\$", source, re.S)
    output = re.findall(r"\\\[(.*?)\\\]", seam, re.S)
    old = Counter(map(clean_math, original))
    new = Counter(map(clean_math, output))
    need(not old-new, "changed or missing displayed seam mathematics")
    need(len(re.findall(r"\\tag\{A\.\d+\}", seam)) == 21, "21 seam equation tags")
    vectors = re.findall(r"\|\s*(\d+(?:,\d+|, \d+){5,})\s*\|", source)
    need(len(vectors) == 6, "six source rational vectors")
    for vector in vectors:
        need(vector in seam, "rational edge vector missing")
    need("P_n(0)<c" in seam and "eq:seam0" not in seam, "threshold evaluation transcription")
    cases = json.loads((ROOT / "reproducibility/global_brackets/originals/source/ringmin_global_interval_candidate.json").read_text())["certificate"]["cases"]
    report=json.loads((Path(__file__).parent/"global_brackets_verified.json").read_text())
    need(report["status"]=="PASS_GLOBAL_BRACKETS" and report["pinned_input_verification"]=="PASS", "complete reproduction report")
    need(len(report["cases"])==12, "report case count")
    for case, result in zip(cases, report["cases"]):
        need(result["n"]==case["n"] and Fraction(result["L"])==Fraction(case["L"])
             and Fraction(result["U"])==Fraction(case["U"]), "report endpoints")
        need(result["geometry"]["witnesses"]==len(case["upper_witnesses"]), "report witness count")
        need(all(Fraction(x)>0 for x in result["geometry"]["minimum_squared_gap_per_witness"]), "positive recorded geometry margins")
        need(0<Fraction(result["strict_lower_radius_buffer"])<Fraction(1,10**11), "positive recorded strictness buffer")
        for key,value in case["lower_bound"].items():
            if key not in ("status","method","skeleton_vertices"):
                need(result["lower"][key]==value, "report lower evidence: "+key)
    for key in ("witnesses","central_tangencies","outer_pairs","angular_inequalities"):
        need(report[key]==sum(r["geometry"][key] for r in report["cases"]), "report aggregate: "+key)
    table = (PAPER / "bracket_rows.tex").read_text()
    rows = re.findall(r"^(\d+) & ([0-9.]+) & ([0-9.]+) & (\d+)", table, re.M)
    need(len(rows) == 12, "twelve endpoint rows")
    for (n, lo, hi, count), case in zip(rows, cases):
        need(int(n) == case["n"] and Fraction(lo) == Fraction(case["L"])
             and Fraction(hi) == Fraction(case["U"]) and int(count) == len(case["upper_witnesses"]), "endpoint/witness transcription")
        need(Fraction(hi)-Fraction(lo) == Fraction(1,10**11), "exact bracket width")
    coverage = (PAPER / "coverage_rows.tex").read_text()
    rows = re.findall(r"^(\d+) & ([\d,]+) & ([\d,]+) & ([\d,]+|--)", coverage, re.M)
    need(len(rows) == 12, "twelve coverage rows")
    for (n,total,explicit,kept),case in zip(rows,cases):
        low=case["lower_bound"]
        need(int(n)==case["n"] and int(total.replace(",",""))==low["canonical_orders_covered"]
             and int(explicit.replace(",",""))==low["explicit_full_orders_checked"], "coverage transcription")
        if int(n)>=10:
            need(int(kept.replace(",",""))==low["canonical_skeletons_expanded"], "skeleton transcription")
    manuscript = (PAPER / "ringmin_dcg.tex").read_text(encoding="utf-8")
    abstract = manuscript.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0]
    need(150 <= len(abstract.split()) <= 250, "abstract word count")
    for forbidden in ["SUPNICK_FULL_FEASIBILITY", "SUPNICK_SEAM_SEQUENCES", "4k+6", "Corrective v2"]:
        need(forbidden not in manuscript+seam, "out-of-scope manuscript dependency: "+forbidden)
    alltex="\n".join(p.read_text(encoding="utf-8") for p in PAPER.glob("*.tex"))
    labels = re.findall(r"\\label\{([^}]+)\}",alltex)
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",alltex)
    need(len(labels)==len(set(labels)) and set(refs)<=set(labels), "unique resolved source labels")
    need("|---" not in seam, "unconverted Markdown table")
    git=["git","-c","safe.directory="+ROOT.as_posix()]
    changed=subprocess.check_output(git+["diff",BASE,"--name-only"],cwd=ROOT,text=True).splitlines()
    allowed={"CURRENT_STATUS.md","research/NEXT_RESEARCH_STEPS.md"}
    prefixes=("paper_assets/journal_dcg/","ops/TASK-20260919__dcg_presubmission_revision/")
    need(all(p in allowed or p.startswith(prefixes) for p in changed), "protected tracked paths changed: "+repr(changed))
    protected_local = {"paper_assets/journal_dcg/"+name for name in
                       ("bracket_rows.tex", "coverage_rows.tex", "export_tables.py", ".gitattributes")}
    need(not protected_local.intersection(changed), "protected publication inputs changed")
    baseline_main = subprocess.check_output(git+["show", BASE+":paper_assets/journal_dcg/ringmin_dcg.tex"], text=True)
    baseline_seam = subprocess.check_output(git+["show", BASE+":paper_assets/journal_dcg/seam_appendix.tex"], text=True)
    start = r"\section{Geometric angular reformulation}"
    end = r"\section{Reproducibility statement}"
    need(manuscript.split(start)[1].split(end)[0] == baseline_main.split(start)[1].split(end)[0],
         "mathematical body, finite counts or floating quantifiers changed")
    need(manuscript.split(r"\section{Outward integer cosine arithmetic}")[1].split(r"\begin{thebibliography}")[0]
         == baseline_main.split(r"\section{Outward integer cosine arithmetic}")[1].split(r"\begin{thebibliography}")[0],
         "arithmetic appendix changed")
    prefix = "$(1/\\sqrt n+1/\\sqrt{n-1})^2$, strictly decreasing in $n$."
    suffix = "$R>0$ when $k+2\\le n\\le4k$; a unique positive crossing"
    need(seam.split(prefix)[0] == baseline_seam.split(prefix)[0]
         and seam.split(suffix)[1] == baseline_seam.split(suffix)[1], "seam edits outside A.5 boundary proof")
    baseline_displays = re.findall(r"\\\[(.*?)\\\]", baseline_seam, re.S)
    need(len(output) == len(baseline_displays)+2, "exactly two explanatory displays added")
    need("a fixed minimizing cyclic order" in abstract and "a single minimizing" not in abstract,
         "abstract uniqueness ambiguity")
    citations = re.findall(r"\\cite\{([^}]+)\}", manuscript)
    bibkeys = re.findall(r"\\bibitem\{([^}]+)\}", manuscript)
    need(len(bibkeys)==5 and set(citations)<=set(bibkeys), "five resolved bibliography entries")
    need(manuscript.count("pinned, content-addressed") == 2 and "not an archival repository" in manuscript,
         "Git versus archival wording")
    need(manifest_revision_baseline() == BASE, "revision baseline metadata")
    untracked=subprocess.check_output(git+["ls-files","--others","--exclude-standard"],cwd=ROOT,text=True).splitlines()
    exempt="paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
    need(all(p==exempt or p.startswith(("paper_assets/journal_dcg/","ops/TASK-20260919__dcg_presubmission_revision/")) for p in untracked),"unrelated new paths")
    need(hashlib.sha256((ROOT/exempt).read_bytes()).hexdigest()=="e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db", "exempt ZIP bytes changed")
    files=[ROOT/p for p in changed+untracked if p!=exempt and not p.endswith(".pdf")]
    for p in files:
        s=p.read_text(encoding="utf-8")
        need(s.endswith("\n"),"missing final newline: "+p.name)
        need(all(line==line.rstrip() for line in s.splitlines()),"trailing whitespace: "+p.name)
    manifest=json.loads((PAPER/"BUILD_MANIFEST.json").read_text())
    for group in ("inputs_sha256","protected_mathematical_inputs_sha256","output_sha256"):
        for path,sha in manifest[group].items():
            data=(ROOT/path).read_bytes()
            if group=="protected_mathematical_inputs_sha256" and "/originals/" not in path:
                data=data.replace(b"\r\n",b"\n")
            need(hashlib.sha256(data).hexdigest()==sha,"stale build: "+path)
    need(manifest["unresolved_references"]==[] and manifest["overfull_boxes"]==[],"build quality gate")
    print(f"PASS: {len(original)} seam displays preserved, 21 tags, six vectors, 12 endpoint and coverage rows.")
    print(f"PASS: abstract {len(abstract.split())} whitespace words; scope, source references, artifact hashes, UTF-8/whitespace.")
    print("PASS: protected tracked paths unchanged; exempt ZIP unchanged; only allowed task paths.")
    print("PASS: complete stored reproduction report bound to all twelve certificate rows and positive recorded margins.")
    print("PASS: mathematical body, arithmetic appendix, floating quantifiers and seam outside A.5 unchanged from revision baseline.")
    print("PASS: two explanatory displays, five resolved bibliography entries, revision provenance and Git wording.")
    print("LIMIT: transcription and scope audit, not independent mathematical review or hosted CI.")

if __name__=="__main__":
    main()
