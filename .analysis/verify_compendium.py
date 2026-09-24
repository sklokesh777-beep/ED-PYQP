from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "Entrepreneurship_Development_PYQ_Compendium_and_2026_Prediction.pdf"
PREVIEW = ROOT / ".analysis" / "output" / "compendium-verification-preview.jpg"

papers = [
    ("2018 Regular", "ENTREPRENEURSHIP DEVELOPMENT.pdf", 17, 3),
    ("2018 IAF", "ENTREPRENEURSHIP DEVELOPMENT (1).pdf", 21, 2),
    ("2019 Regular", "ENTREPRENEURSHIPDEVELOPMENT (1).pdf", 24, 2),
    ("2019 IAF", "1696409125525_EntrepreneurshipDevelopment.pdf", 27, 2),
    ("2022 IAF", "EntrepreneurshipDevelopment.pdf", 30, 3),
    ("2023 Regular", "1703135622672_EntrepreneurshipDevelopment.pdf", 34, 3),
    ("2023 Strategic Finance", "1703135984171_Entrepreneurship.pdf", 38, 2),
]

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


doc = fitz.open(PDF)
assert len(doc) == 40, f"Expected 40 pages, found {len(doc)}"
assert PDF.stat().st_size > 500_000
assert all(abs(page.rect.width - 595.276) < 1 and abs(page.rect.height - 841.89) < 1 for page in doc), "Non-A4 page found"

text_by_page = [page.get_text("text", sort=True) for page in doc]
full_text = "\n".join(text_by_page)
checks = {
    "cover": "Previous-Year Question Paper Compendium" in text_by_page[0],
    "methodology": "How the counts work" in full_text and "Exact versus near-repeat wording" in full_text,
    "exact_repeat_count": "Mechanically exact top-level wording groups" in full_text and "ER05" in full_text,
    "frequency_tables": "MSME and entrepreneurship-support institutions" in full_text and "International-market entry modes" in full_text,
    "model_status": "UNOFFICIAL PREDICTION / MODEL PAPER" in full_text,
    "model_sections": all(f"SECTION {s}" in full_text for s in "ABCD"),
    "model_total": "10 + 18 + 30 + 12 = 70" in full_text,
    "model_case": "Circular Harvest Foods" in full_text,
    "all_originals_heading": "ORIGINAL QUESTION PAPERS" in full_text,
    "corpus_counts": all(value in full_text for value in ["154", "168", "7/7"]),
    "no_replacement_char": "�" not in full_text,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

# Verify each divider and every original source page in exact chronological placement.
source_page_count = 0
for label, filename, divider_page, expected_pages in papers:
    assert "ORIGINAL QUESTION PAPER" in text_by_page[divider_page - 1], f"Missing divider at {divider_page}"
    assert label.split()[0] in text_by_page[divider_page - 1], f"Wrong divider at {divider_page}"
    src = fitz.open(ROOT / filename)
    assert len(src) == expected_pages
    for i, src_page in enumerate(src):
        final_page_no = divider_page + 1 + i
        final_text = norm(text_by_page[final_page_no - 1])
        source_text = norm(src_page.get_text("text", sort=True))
        assert source_text in final_text, f"Source text mismatch: {filename} page {i + 1}, final page {final_page_no}"
        assert f"Source page {i + 1}/{expected_pages}" in final_text
        source_page_count += 1
    src.close()
assert source_page_count == 17

# Historical pattern and prediction structure checks against analysis source.
assert full_text.count("Answer any TEN questions") >= 8  # model + seven originals
assert full_text.count("Answer any THREE questions") >= 8
assert full_text.count("Answer any TWO questions") >= 8
assert full_text.count("Case Study") >= 8

links = sum(len(page.get_links()) for page in doc)
toc = doc.get_toc(simple=True)
assert links >= 25, f"Too few clickable links: {links}"
assert len(toc) >= 40, f"Too few bookmarks: {len(toc)}"
for label, _, divider_page, _ in papers:
    assert any(page == divider_page and title.startswith(label.split()[0]) for _, title, page in toc), f"Missing bookmark for {label}"

# The only intentionally almost-empty source artifact is final page 3 of the 2023 Regular source.
low_text_pages = [i + 1 for i, text in enumerate(text_by_page) if len(text.split()) < 25]
assert low_text_pages == [37], f"Unexpected low-text pages: {low_text_pages}"
assert "Source page 3/3" in text_by_page[36] and "Page 3 of 2" in text_by_page[36]

# Build a visual audit sheet: cover, key analysis pages, prediction, every divider,
# every first original page, the intentional footer-only page, and final page.
def find_page(needle: str, start: int = 0) -> int:
    for i in range(start, len(doc)):
        if needle in text_by_page[i]:
            return i
    raise AssertionError(f"Text not found: {needle}")

selected = [
    0,
    1,
    find_page("Quick result: what repeated most?", 2),
    find_page("Mechanically exact top-level wording groups", 2),
    find_page("Specific-topic frequency", 2),
    find_page("2026 PREDICTED / MODEL PAPER", 2),
    find_page("SECTION A", 2),
    find_page("Circular Harvest Foods"),
    find_page("ORIGINAL QUESTION PAPERS"),
]
for _, _, divider, _ in papers:
    selected.extend([divider - 1, divider])
selected.extend([36, 39])
selected = list(dict.fromkeys(selected))

cols = 4
cell_w, cell_h = 350, 500
rows = (len(selected) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "#dce6e8")
draw = ImageDraw.Draw(sheet)
for slot, page_index in enumerate(selected):
    page = doc[page_index]
    scale = 325 / page.rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    x, y = (slot % cols) * cell_w, (slot // cols) * cell_h
    sheet.paste(image, (x + 10, y + 28))
    draw.text((x + 10, y + 7), f"Compendium page {page_index + 1}", fill="#163d4b")
sheet.save(PREVIEW, quality=90, optimize=True)

report = {
    "file": PDF.name,
    "sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
    "bytes": PDF.stat().st_size,
    "pages": len(doc),
    "page_size": "A4",
    "analysis_and_prediction_pages": 16,
    "divider_pages": 7,
    "original_source_pages": source_page_count,
    "original_papers": 7,
    "links": links,
    "bookmarks": len(toc),
    "extracted_words": len(full_text.split()),
    "intentional_low_text_pages": low_text_pages,
    "checks": checks,
    "preview": str(PREVIEW.relative_to(ROOT)),
}
print(json.dumps(report, indent=2))
