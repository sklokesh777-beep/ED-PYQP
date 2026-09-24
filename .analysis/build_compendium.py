from __future__ import annotations

import html
import re
from pathlib import Path

import fitz
import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / ".analysis" / "output"
FRONT_MD = ANALYSIS / "compendium-front.md"
FRONT_HTML = ANALYSIS / "compendium-front.html"
FRONT_PDF = ANALYSIS / "compendium-front.pdf"
FINAL_PDF = ROOT / "Entrepreneurship_Development_PYQ_Compendium_and_2026_Prediction.pdf"

PAPERS = [
    {
        "label": "2018 - BCom Regular",
        "short": "2018 Regular",
        "session": "March/April 2018",
        "programme": "BCom Regular",
        "course": "C1 15 MC 603",
        "file": "ENTREPRENEURSHIP DEVELOPMENT.pdf",
        "pages": 3,
        "note": "Complete three-page source paper.",
    },
    {
        "label": "2018 - BCom International Accounting & Finance",
        "short": "2018 IAF",
        "session": "March/April 2018",
        "programme": "BCom International Accounting & Finance",
        "course": "C4 15 MC 603",
        "file": "ENTREPRENEURSHIP DEVELOPMENT (1).pdf",
        "pages": 2,
        "note": "Complete two-page source paper.",
    },
    {
        "label": "2019 - BCom Regular",
        "short": "2019 Regular",
        "session": "March/April 2019",
        "programme": "BCom Regular",
        "course": "C1 15 MC 603",
        "file": "ENTREPRENEURSHIPDEVELOPMENT (1).pdf",
        "pages": 2,
        "note": "Complete two-page source paper.",
    },
    {
        "label": "2019 - BCom International Accounting & Finance",
        "short": "2019 IAF",
        "session": "March/April 2019",
        "programme": "BCom International Accounting & Finance",
        "course": "C4 15 MC 603",
        "file": "1696409125525_EntrepreneurshipDevelopment.pdf",
        "pages": 2,
        "note": "Complete two-page source paper.",
    },
    {
        "label": "2022 - BCom International Accounting & Finance",
        "short": "2022 IAF",
        "session": "June 2022",
        "programme": "BCom International Accounting & Finance",
        "course": "C4 15 MC 603",
        "file": "EntrepreneurshipDevelopment.pdf",
        "pages": 3,
        "note": "Complete three-page source paper.",
    },
    {
        "label": "2023 - BCom Regular",
        "short": "2023 Regular",
        "session": "May 2023",
        "programme": "BCom Regular",
        "course": "C1 15 MC 603",
        "file": "1703135622672_EntrepreneurshipDevelopment.pdf",
        "pages": 3,
        "note": "The source PDF has two content pages plus a third page containing only the contradictory footer 'Page 3 of 2'. It is retained for exact source completeness.",
    },
    {
        "label": "2023 - BCom Strategic Finance",
        "short": "2023 Strategic Finance",
        "session": "May 2023",
        "programme": "BCom Strategic Finance",
        "course": "C6 20 MC 602",
        "file": "1703135984171_Entrepreneurship.pdf",
        "pages": 2,
        "note": "Complete two-page source paper.",
    },
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


frequency = read(ANALYSIS / "frequency_report.md")
prediction = read(ANALYSIS / "prediction_2026.md")
# Avoid two competing document titles while preserving all report content.
frequency = re.sub(r"^# ", "## ", frequency, count=1)
prediction = re.sub(r"^# ", "## ", prediction, count=1)


def build_markdown(paper_starts: list[int] | None = None) -> str:
    rows = []
    for index, paper in enumerate(PAPERS):
        start = str(paper_starts[index]) if paper_starts else "calculated in final edition"
        rows.append(
            f"| {paper['session']} | {paper['programme']} | `{paper['course']}` | {paper['pages']} | {start} |"
        )
    corpus_table = "\n".join(rows)
    return f"""
# How to use this compendium

This book puts **all seven supplied previous-year Entrepreneurship Development papers into one PDF**, followed by no missing source paper. Before the originals, it gives a transparent recurrence analysis and one **clearly unofficial 2026 predicted/model paper**.

> **Important:** Prediction is not certainty. The corpus covers seven programme variants across only four exam years (2018, 2019, 2022 and 2023). Same-year variants may share setters or syllabus emphasis. Use the prediction to practise; revise the full current syllabus.

## What is included

1. Corpus and pattern audit.
2. Exact and near-repeat question groups.
3. Broad-theme and specific-topic appearance counts.
4. Evidence labels showing the exact paper and question number.
5. A balanced 70-mark 2026 predicted/model paper aligned to current Modules 1-6.
6. The seven original papers, in chronological order, reproduced as source pages.

## Quick result: what repeated most?

| Priority | Normalised topic | Separate assessed prompts | Distinct papers |
|---:|---|---:|---:|
| 1 | MSME and entrepreneurship-support institutions | 12 | 7/7 |
| 2 | Business-plan purpose, components, formulation and evaluation | 12 | 7/7 |
| 3 | International-market entry modes | 9 | 6/7 |
| 4 | Entrepreneurial process, enterprise establishment and venture life cycle | 6 | 6/7 |
| 5 | Business models, BMC and value proposition | 10 | 5/7 |
| 6 | Seed, angel, venture-capital and equity finance | 7 | 5/7 |
| 7 | Entrepreneurial traits, competencies, mindset and resilience | 6 | 5/7 |
| 8 | Government policy, incentives, tax holidays and Startup India | 6 | 5/7 |
| 9 | Intellectual property and protection | 6 | 5/7 |
| 10 | Entrepreneur types and profiles | 5 | 5/7 |

**Highest near-repeat:** international-market entry methods appeared in **6 of 7 papers** as substantially the same long-answer task. The entrepreneurial process/steps of establishing a venture appeared as a near-repeat in **5 of 7 papers**.

## How the counts work

- A **paper count** answers: “In how many of the seven papers did this topic appear at least once?”
- A **prompt count** answers: “How many separately assessed prompts tested this topic?”
- A topic is counted at most once within one top-level numbered question.
- Explicit case subquestions and genuine OR alternatives count separately when they independently test a topic.
- Exact repeats, near repeats and broader thematic recurrence are reported separately; they must not be added together.
- Offered-question mark exposure is not the same as marks a student had to answer because Sections A-C include choices.

## Source-paper index

| Session | Programme | Course code | Source pages | Compendium start page* |
|---|---|---|---:|---:|
{corpus_table}

\*The listed page is the divider immediately before the reproduced original paper. PDF bookmarks also take you directly to each paper.

## Historical paper pattern: unchanged in 7/7 papers

| Section | Offered | Answer rule | Marks each | Required marks |
|---|---:|---:|---:|---:|
| A | 12 | Any 10 | 1 | 10 |
| B | 5 | Any 3 | 6 | 18 |
| C | 4 | Any 2 | 15 | 30 |
| D | 1 case | Compulsory | 12 | 12 |
| **Total** | **22 slots** | **16 numbered answers** | - | **70** |

<div class="section-break"></div>

{frequency}

<div class="section-break prediction-break"></div>

{prediction}

<div class="section-break"></div>

# ORIGINAL QUESTION PAPERS

The pages after this point reproduce all seven repository PDFs in chronological order. Each paper has a divider and PDF bookmark. The source wording, formatting and errors are preserved. The 2023 Regular file's extra footer-only third page is intentionally retained and is not a missing-content error.
""".strip() + "\n"


CSS = r"""
@page {
  size: A4;
  margin: 16mm 13mm 18mm 13mm;
  @top-left { content: "ENTREPRENEURSHIP DEVELOPMENT - PYQ COMPENDIUM"; color: #466776; font-size: 7pt; letter-spacing: .06em; }
  @top-right { content: string(chapter); color: #5e7782; font-size: 7pt; }
  @bottom-left { content: "Frequency Analysis + 2026 Model Paper + Originals"; color: #607985; font-size: 7pt; }
  @bottom-right { content: "Page " counter(page); color: #254f62; font-size: 7.5pt; font-weight: 600; }
}
@page cover {
  margin: 0;
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}
* { box-sizing: border-box; }
html { font-family: "Noto Sans", sans-serif; color: #182830; font-size: 9.3pt; line-height: 1.38; }
body { margin: 0; }
.cover {
  page: cover; height: 297mm; padding: 27mm 22mm 22mm; color: white;
  background: linear-gradient(150deg, #17324a 0%, #155c72 49%, #0b8a80 100%);
  page-break-after: always; position: relative;
}
.cover .eyebrow { margin-top: 5mm; color: #cafff1; font-size: 9.5pt; letter-spacing: .16em; text-transform: uppercase; }
.cover h1 { margin: 19mm 0 7mm; color: white; font-size: 30pt; line-height: 1.08; border: 0; letter-spacing: -.02em; }
.cover h2 { margin: 0 0 12mm; color: #e0fff8; font-size: 15pt; font-weight: 500; }
.cover .warning { max-width: 150mm; padding: 5mm; border-left: 4px solid #ffd166; background: rgba(0,0,0,.12); font-size: 10.5pt; line-height: 1.48; }
.cover strong { color: white; }
.cover .stats { position: absolute; left: 22mm; right: 22mm; bottom: 22mm; display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,.42); padding-top: 6mm; }
.cover .stat { width: 23%; }
.cover .num { display: block; color: #ffd166; font-size: 19pt; font-weight: 700; }
.cover .label { color: #e7fffa; font-size: 8pt; }
.contents { page-break-after: always; }
.contents h1 { page-break-before: auto; }
.contents ul { list-style: none; padding-left: 0; }
.contents ul ul { padding-left: 5mm; }
.contents li { margin: 1mm 0; }
.contents a { color: #20556b; text-decoration: none; }
.contents a::after { content: leader(".") target-counter(attr(href), page); color: #6d858f; }
.section-break { page-break-before: always; height: 0; }
.prediction-break + h2, .prediction-break ~ h2:first-of-type { color: #7b3f00; }
h1, h2, h3, h4 { color: #0f566c; line-height: 1.2; break-after: avoid; }
h1 { font-size: 21pt; margin: 3mm 0 6mm; padding-bottom: 3mm; border-bottom: 2.5px solid #18a194; string-set: chapter content(); }
h2 { font-size: 14.5pt; margin: 7mm 0 3mm; border-left: 4px solid #18a194; padding-left: 3mm; string-set: chapter content(); }
h3 { font-size: 11.3pt; margin: 5mm 0 2mm; color: #315f72; }
h4 { font-size: 10pt; margin: 4mm 0 1.5mm; }
p { margin: 0 0 2.7mm; orphans: 3; widows: 3; }
ul, ol { margin: 1.5mm 0 3mm; padding-left: 6mm; }
li { margin: .8mm 0; }
strong { color: #153f50; }
blockquote { margin: 3.5mm 0; padding: 3mm 4mm; border-left: 4px solid #e9a23b; background: #fff7e5; color: #3d4750; break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm; font-size: 7.15pt; line-height: 1.24; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: #155f70; color: white; text-align: left; padding: 1.8mm 1.5mm; border: .45pt solid #d1e1e5; vertical-align: top; }
td { padding: 1.45mm 1.5mm; border: .45pt solid #c9d9de; vertical-align: top; overflow-wrap: anywhere; }
tbody tr:nth-child(even) { background: #f2f8f8; }
code { font-family: "Noto Sans Mono", monospace; font-size: .88em; background: #eef4f5; padding: 0 .5mm; overflow-wrap: anywhere; }
a { color: #087f78; overflow-wrap: anywhere; }
hr { border: 0; border-top: 1px solid #a8c4cc; margin: 6mm 0; }
"""

COVER = """
<section class="cover">
  <div class="eyebrow">Seven original papers • audited recurrence counts</div>
  <h1>Entrepreneurship Development</h1>
  <h2>Previous-Year Question Paper Compendium<br>with 2026 Predicted / Model Paper</h2>
  <div class="warning"><strong>One PDF for focused exam preparation.</strong><br><br>Exact and near-repeat analysis, topic appearance counts, evidence labels, a syllabus-balanced 2026 model paper, and every original source paper in chronological order.<br><br><strong>The prediction is unofficial and not guaranteed.</strong></div>
  <div class="stats">
    <div class="stat"><span class="num">7</span><span class="label">Original papers</span></div>
    <div class="stat"><span class="num">154</span><span class="label">Official Q1-Q22 slots</span></div>
    <div class="stat"><span class="num">168</span><span class="label">Assessed prompt units</span></div>
    <div class="stat"><span class="num">70</span><span class="label">Marks per paper</span></div>
  </div>
</section>
"""


def render_front(markdown_text: str) -> fitz.Document:
    FRONT_MD.write_text(markdown_text, encoding="utf-8")
    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "1-3"}},
        output_format="html5",
    )
    body = md.convert(markdown_text)
    html_doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Entrepreneurship Development PYQ Compendium and 2026 Prediction</title><style>{CSS}</style></head><body>{COVER}<section class="contents"><h1>Contents</h1><p>Entries below are clickable. Original papers also have PDF bookmarks and an index with final page numbers.</p>{md.toc}</section>{body}</body></html>"""
    FRONT_HTML.write_text(html_doc, encoding="utf-8")
    HTML(string=html_doc, base_url=str(ROOT)).write_pdf(FRONT_PDF)
    return fitz.open(FRONT_PDF)


# Two-pass layout: calculate the exact starts of original-paper divider pages,
# then print those page numbers in the source-paper index.
front = render_front(build_markdown())
for _ in range(3):
    page_cursor = len(front) + 1
    starts = []
    for paper in PAPERS:
        starts.append(page_cursor)
        page_cursor += 1 + paper["pages"]
    front.close()
    new_front = render_front(build_markdown(starts))
    if len(new_front) + 1 == starts[0]:
        front = new_front
        break
    front = new_front
else:
    raise RuntimeError("Front-matter pagination did not stabilise")

out = fitz.open()
# WeasyPrint emits named internal destinations. PyMuPDF does not retain these
# through insert_pdf reliably, so capture their resolved page/point and rebuild
# them as ordinary internal GoTo links after the complete document is assembled.
front_links = []
for source_page_index, source_page in enumerate(front):
    for link in source_page.get_links():
        if link.get("page", -1) >= 0 and link.get("to") is not None:
            front_links.append({
                "source_page": source_page_index,
                "from": fitz.Rect(link["from"]),
                "page": int(link["page"]),
                "to": fitz.Point(link["to"]),
                "zoom": float(link.get("zoom", 0.0)),
            })
out.insert_pdf(front, links=False, annots=True)
front_toc = front.get_toc(simple=True)
front_pages = len(front)
front.close()

toc = [entry[:] for entry in front_toc]
A4 = fitz.paper_rect("a4")
header_y = 20
content_rect = fitz.Rect(24, 31, A4.width - 24, A4.height - 34)

for paper_index, paper in enumerate(PAPERS, start=1):
    divider_page_no = len(out) + 1
    page = out.new_page(width=A4.width, height=A4.height)
    page.draw_rect(page.rect, color=None, fill=(0.055, 0.28, 0.37))
    page.draw_rect(fitz.Rect(0, 0, 16, A4.height), color=None, fill=(0.08, 0.68, 0.59))
    page.insert_text((42, 90), "ORIGINAL QUESTION PAPER", fontsize=10, fontname="helv", color=(0.68, 0.95, 0.90))
    page.insert_textbox(fitz.Rect(42, 125, A4.width - 42, 240), paper["label"], fontsize=24, fontname="hebo", color=(1, 1, 1), lineheight=1.15)
    page.insert_text((42, 282), f"Session: {paper['session']}", fontsize=11, fontname="helv", color=(0.90, 0.98, 0.98))
    page.insert_text((42, 306), f"Programme: {paper['programme']}", fontsize=11, fontname="helv", color=(0.90, 0.98, 0.98))
    page.insert_text((42, 330), f"Course code: {paper['course']}", fontsize=11, fontname="helv", color=(0.90, 0.98, 0.98))
    page.insert_text((42, 354), f"Source pages retained: {paper['pages']}", fontsize=11, fontname="helv", color=(0.90, 0.98, 0.98))
    note = paper["note"].replace("’", "'").replace("‘", "'")
    page.insert_textbox(fitz.Rect(42, 410, A4.width - 42, 525), note, fontsize=9.5, fontname="helv", color=(0.82, 0.93, 0.94), lineheight=1.35)
    page.insert_textbox(fitz.Rect(42, 690, A4.width - 42, 755), "The original paper begins on the next page. Source wording, formatting and typographical errors are preserved.", fontsize=9.5, fontname="helv", color=(0.82, 0.93, 0.94), lineheight=1.35)
    page.insert_text((A4.width - 112, A4.height - 20), f"Page {divider_page_no}", fontsize=7.5, fontname="helv", color=(0.72, 0.89, 0.90))
    toc.append([1, paper["label"], divider_page_no])

    src = fitz.open(ROOT / paper["file"])
    if len(src) != paper["pages"]:
        raise ValueError(f"Page-count mismatch for {paper['file']}: {len(src)} != {paper['pages']}")
    for source_index in range(len(src)):
        output_page_no = len(out) + 1
        target = out.new_page(width=A4.width, height=A4.height)
        target.insert_text((24, header_y), f"ORIGINAL PAPER | {paper['short']} | Source page {source_index + 1}/{len(src)}", fontsize=7.2, fontname="hebo", color=(0.20, 0.38, 0.46))
        target.show_pdf_page(content_rect, src, source_index, keep_proportion=True)
        target.insert_text((24, A4.height - 14), f"Source file: {paper['file']}", fontsize=6.6, fontname="helv", color=(0.38, 0.49, 0.54))
        target.insert_text((A4.width - 88, A4.height - 14), f"Page {output_page_no}", fontsize=7.2, fontname="hebo", color=(0.20, 0.38, 0.46))
        toc.append([2, f"Source page {source_index + 1} of {len(src)}", output_page_no])
    src.close()

# Restore the clickable contents links captured from the front matter.
for link in front_links:
    out[link["source_page"]].insert_link({
        "kind": fitz.LINK_GOTO,
        "from": link["from"],
        "page": link["page"],
        "to": link["to"],
        "zoom": link["zoom"],
    })

out.set_toc(toc)
metadata = out.metadata
metadata.update({
    "title": "Entrepreneurship Development PYQ Compendium and 2026 Predicted Paper",
    "author": "Prepared from the supplied SJCC previous-year question papers",
    "subject": "Frequency analysis, unofficial 2026 model paper, and seven original papers",
    "keywords": "Entrepreneurship Development, PYQ, previous year question papers, 2026 prediction, BCom",
})
out.set_metadata(metadata)
out.save(FINAL_PDF, garbage=4, deflate=True, clean=True)
out.close()

final = fitz.open(FINAL_PDF)
print(f"Front-matter pages: {front_pages}")
print(f"Original divider pages: {len(PAPERS)}")
print(f"Original source pages: {sum(p['pages'] for p in PAPERS)}")
print(f"Final pages: {len(final)}")
print(f"Final bytes: {FINAL_PDF.stat().st_size}")
print(f"Bookmarks: {len(final.get_toc())}")
print(f"Text words: {sum(len(page.get_text().split()) for page in final)}")
