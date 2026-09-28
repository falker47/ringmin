"""Submission-compliance audit adapted from the preserved 2026-09-19 revision checker.
Not a mathematical verifier or independent acceptance decision."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper_assets/journal_dcg"
BASE = "b1480803749e08197bce37442f0953c550e2a5e4"
PIN = "6c16af422d1cb38641c62d43b6e0e547921b9ba9"
ARCHIVE = "80919666c3c54f8ce20cf66c456d413f6a2c075f"
TAG = "v1.1.0-dcg-presubmission"
DOI = "10.5281/zenodo.22849826"
DOSSIER = "ops/TASK-20260928__dcg_submission_compliance/"
ALLOWED = {
    "CURRENT_STATUS.md", "research/NEXT_RESEARCH_STEPS.md",
    "knowledge/PUBLICATION_HISTORY.md",
    *("paper_assets/journal_dcg/"+name for name in (
        "ringmin_dcg.tex", "ringmin_dcg.pdf", "BUILD_MANIFEST.json",
        "build.py", "README.md", "SOURCE_MAP.md")),
}

def need(test, message):
    if not test:
        raise ValueError(message)

def clean_math(s):
    s = re.sub(r"\\tag\{[^}]*\}|\\label\{[^}]*\}", "", s)
    return re.sub(r"\s+", "", s)

def manifest_revision_baseline():
    return json.loads((PAPER/"BUILD_MANIFEST.json").read_text())["revision_baseline_commit"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight-hashes", type=Path,
                        help="optional raw-byte snapshot captured before editing")
    args = parser.parse_args()
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
    changed = subprocess.check_output(git+["diff", BASE, "--name-only"], text=True).splitlines()
    need(all(p in ALLOWED or p.startswith(DOSSIER) for p in changed),
         "protected tracked paths changed: "+repr(changed))
    baseline = subprocess.check_output(git+["show", BASE+":paper_assets/journal_dcg/ringmin_dcg.tex"], text=True)
    baseline_seam = subprocess.check_output(git+["show", BASE+":paper_assets/journal_dcg/seam_appendix.tex"], text=True)
    need(seam == baseline_seam, "entire seam appendix changed")
    # Removing only the three authorized editorial blocks must recover all TeX.
    insertion_start = "\nThe frozen pre-submission software"
    insertion_end = "\nThe data file is"
    need(manuscript.count(insertion_start) == 1, "one archival provenance block")
    start_pos = manuscript.index(insertion_start)
    end_pos = manuscript.index(insertion_end, start_pos)
    restored = manuscript[:start_pos]+manuscript[end_pos:]
    availability_start = r"\paragraph{Data and code availability.}"
    availability_end = r"\paragraph{Use of artificial intelligence.}"
    old_availability = baseline.split(availability_start)[1].split(availability_end)[0]
    availability = manuscript.split(availability_start)[1].split(availability_end)[0]
    restored = restored.replace(availability, old_availability, 1)
    archive_bib = r"\bibitem{ringmin-archive}"
    entry = manuscript.split(archive_bib)[1].split(r"\end{thebibliography}")[0]
    restored = restored.replace(archive_bib+entry, "", 1)
    need(restored == baseline, "changes outside three authorized TeX blocks")
    need(len(abstract.split()) == 184, "original abstract word count")
    keywords = manuscript.split(r"\textbf{Keywords:}")[1].split(r"\medskip")[0]
    need(len(keywords.split(";")) == 6, "six original keywords")
    for declaration in ("Funding", "Competing interests", "Author contribution",
                        "Data and code availability", "Use of artificial intelligence"):
        need(r"\paragraph{"+declaration+".}" in manuscript, "missing declaration: "+declaration)
    citations = {key for group in re.findall(r"\\cite\{([^}]+)\}", manuscript)
                 for key in group.split(",")}
    bibkeys = re.findall(r"\\bibitem\{([^}]+)\}", manuscript)
    need(len(bibkeys) == len(set(bibkeys)) == 6 and citations <= set(bibkeys),
         "six unique resolved bibliography entries")
    need(r"\cite{ringmin-archive}" in availability, "availability archive citation")
    repro = manuscript.split(r"\section{Reproducibility statement}")[1].split(
        r"\section*{Statements and Declarations}")[0]
    need(r"\cite{ringmin-archive}" in repro, "reproduction archive citation")
    for identity in (PIN, ARCHIVE, BASE, TAG, DOI):
        need(identity in repro, "missing reproduction identity: "+identity)
    need("not contained in the\nZenodo deposit" in repro
         and "requires separate review" in repro, "archival and acceptance boundaries")
    need("not an archival repository" not in manuscript, "stale availability")
    cff = (ROOT/"CITATION.cff").read_text(encoding="utf-8")
    record = json.loads((ROOT/"ops/TASK-20260926__archive_evidence_integration/evidence/zenodo_record.json").read_text())
    meta = record["metadata"]
    need(meta["doi"] == record["doi"] == DOI and 'doi: "'+DOI+'"' in cff,
         "CFF / Zenodo DOI match")
    need(meta["version"] == TAG and 'version: "'+TAG[1:]+'"' in cff,
         "literal CFF and Zenodo versions")
    need(meta["creators"][0]["name"] == "Falconi, Maurizio"
         and 'family-names: "Falconi"' in cff and 'given-names: "Maurizio"' in cff,
         "author metadata")
    need(meta["title"] in " ".join(entry.split()) and 'title: "'+meta["title"]+'"' in cff,
         "software title metadata")
    need(meta["publication_date"] == "2026-09-19" and "Zenodo (2026)" in entry
         and "Falconi, M.:" in entry and TAG in entry
         and "https://doi.org/"+DOI in entry, "deposited bibliography fields")
    for older, newer in ((PIN, ARCHIVE), (ARCHIVE, BASE)):
        need(older != newer, "distinct identities")
        subprocess.run(git+["merge-base", "--is-ancestor", older, newer], check=True)
    untracked = subprocess.check_output(git+["ls-files", "--others", "--exclude-standard"], text=True).splitlines()
    exempt = "paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip"
    need(all(p == exempt or p.startswith(DOSSIER) for p in untracked), "unrelated new paths")
    need(hashlib.sha256((ROOT/exempt).read_bytes()).hexdigest() ==
         "e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db", "exempt ZIP bytes changed")
    if args.preflight_hashes:
        snapshot = json.loads(args.preflight_hashes.read_text(encoding="utf-8"))
        protected = {p: sha for p, sha in snapshot.items() if p not in ALLOWED}
        for path, sha in protected.items():
            need(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha,
                 "raw protected bytes changed: "+path)
        print(f"PASS: {len(protected)} preflight protected files byte-identical (including exempt ZIP).")
    for path in sorted(set(changed+untracked)-{exempt}):
        if path.endswith(".pdf"):
            continue
        text = (ROOT/path).read_text(encoding="utf-8")
        need(text.endswith("\n") and all(line == line.rstrip() for line in text.splitlines()),
             "UTF-8/whitespace: "+path)
    manifest = json.loads((PAPER/"BUILD_MANIFEST.json").read_text())
    for group in ("inputs_sha256", "protected_mathematical_inputs_sha256", "output_sha256"):
        for path, sha in manifest[group].items():
            data = (ROOT/path).read_bytes()
            if group == "protected_mathematical_inputs_sha256" and "/originals/" not in path:
                data = data.replace(b"\r\n", b"\n")
            need(hashlib.sha256(data).hexdigest() == sha, "stale build: "+path)
    need(manifest_revision_baseline() == BASE and manifest["mathematical_source_commit"] == PIN
         and manifest["archival_snapshot"]["commit"] == ARCHIVE
         and manifest["archival_snapshot"]["tag"] == TAG
         and manifest["archival_snapshot"]["doi"] == DOI, "three manifest identities")
    need(report["verifier_sha256"] == hashlib.sha256((ROOT/"verify_global_brackets.py").read_bytes()).hexdigest(),
         "fresh report verifier hash")
    need(report["preserved_original_files"] == 13, "all preserved original files")
    need(manifest["unresolved_references"] == [] and manifest["overfull_boxes"] == [], "build quality gate")
    print(f"PASS: {len(original)} seam displays preserved, 21 tags, six vectors, 12 endpoint and coverage rows.")
    print(f"PASS: abstract {len(abstract.split())} whitespace words; six keywords; all declarations; resolved source references.")
    print("PASS: complete baseline TeX recovered outside three editorial blocks; entire seam appendix unchanged.")
    print("PASS: six resolved bibliography entries; CFF/Zenodo citation; three distinct provenance identities and ancestry.")
    print("PASS: fresh full report bound to twelve certificate rows and positive margins; verifier and artifact hashes.")
    print("PASS: protected tracked paths and exempt ZIP unchanged; only allowed task paths; all text UTF-8/whitespace.")
    print("LIMIT: transcription and scope audit, not independent mathematical review or hosted CI.")

if __name__ == "__main__":
    main()
