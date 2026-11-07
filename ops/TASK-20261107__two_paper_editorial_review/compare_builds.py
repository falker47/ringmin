from pathlib import Path
import json,re
root=Path.cwd()
d=root/"ops/TASK-20261107__two_paper_editorial_review"
w=root/"reproducibility/.work/editorial_20261107"
result={}
for paper,stem in (("paper_i","ringmin_dcg"),("paper_ii","main")):
    base=json.loads((d/f"build_baseline_{paper}.json").read_text())
    rev=json.loads((d/f"build_revised_{paper}.json").read_text())
    repeat=json.loads((d/f"build_repeat_{paper}.json").read_text())
    assert not base["warnings"] and not rev["warnings"] and not repeat["warnings"]
    assert rev["pdf_sha256"]==repeat["pdf_sha256"]
    ba=(w/"baseline"/paper/(stem+".aux")).read_text()
    ra=(w/"revised"/paper/(stem+".aux")).read_text()
    labels=lambda t:re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}",t)
    cites=lambda t:re.findall(r"\\bibcite\{([^}]+)\}\{([^}]*)\}",t)
    assert labels(ba)==labels(ra)
    assert cites(ba)==cites(ra)
    result[paper]={"baseline_pages":base["pages"],"revised_pages":rev["pages"],"new_warnings":[],
        "identical_repeat_pdf":True,"unchanged_label_numbers":len(labels(ra)),
        "unchanged_bibliography_numbers":len(cites(ra)),"pdf_sha256":rev["pdf_sha256"]}
(d/"build_comparison.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
