"""Extract final PDF text and create contact sheets from Poppler page renders.

Requires pypdf and Pillow (bundled workspace Python). Visual review is manual.
"""
from pathlib import Path
from PIL import Image
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
work=ROOT/"reproducibility/.work/journal_dcg"
reader=PdfReader(ROOT/"paper_assets/journal_dcg/ringmin_dcg.pdf")
pages=sorted(work.glob("page-*.png"))
if len(pages)!=len(reader.pages):
    raise ValueError("render count differs from PDF")
texts=[p.extract_text() for p in reader.pages]
if any("??" in s or "\ufffd" in s for s in texts):
    raise ValueError("unresolved or invalid extracted text")
(work/"manuscript.txt").write_text("\n\n".join(f"PAGE {i+1}\n{s}" for i,s in enumerate(texts)),encoding="utf-8")
size=(703,994)
for base in range(0,len(pages),6):
    sheet=Image.new("RGB",(size[0]*3,size[1]*2),"#bbbbbb")
    for j,p in enumerate(pages[base:base+6]):
        im=Image.open(p).convert("RGB")
        im.thumbnail(size)
        sheet.paste(im,((j%3)*size[0],(j//3)*size[1]))
    sheet.save(work/f"sheet-{base//6+1}.png")
print(f"PASS: {len(pages)} Poppler pages, extracted text without unresolved references/replacement characters.")
print("Contact sheets created for manual inspection; text extraction alone is not a layout check.")
