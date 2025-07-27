"""
PyPDF2 outline extractor using text heuristics only.
- line length
- all-caps / title-case
- position on page
"""
from PyPDF2 import PdfReader
from typing import Dict, List

def extract_outline(pdf_path: str) -> Dict:
    reader = PdfReader(pdf_path)
    lines = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text:
            continue
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            lines.append({
                "text": line,
                "len": len(line),
                "upper": line == line.upper(),
                "page": page_num
            })

    if not lines:
        return {"title": "No text", "outline": []}

    # thresholds
    max_len = max(l["len"] for l in lines)
    h1_len = max_len * 0.25
    h2_len = max_len * 0.5
    h3_len = max_len * 0.75

    outline = []
    seen = set()
    for l in lines:
        lvl = None
        if l["upper"] and l["len"] <= h1_len:
            lvl = "H1"
        elif l["upper"] and l["len"] <= h2_len:
            lvl = "H2"
        elif l["len"] <= h3_len:
            lvl = "H3"
        if lvl and l["text"] not in seen:
            outline.append({"level": lvl, "text": l["text"], "page": l["page"]})
            seen.add(l["text"])

    # title = first non-empty line on page 1
    title = next((l["text"] for l in lines if l["page"] == 1), "Untitled")

    # sort by page, then level
    outline = sorted(outline, key=lambda x: (x["page"], {"H1": 1, "H2": 2, "H3": 3}[x["level"]]))
    return {"title": title, "outline": outline}