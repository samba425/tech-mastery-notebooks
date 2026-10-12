#!/usr/bin/env python3
"""Build the textbook, practice workbook and formula-sheet PDFs from content/*.md.

Usage:
    python3 scripts/generate_book.py            # all three PDFs
    python3 scripts/generate_book.py --only book
    python3 scripts/generate_book.py --parts 01,04   # quick preview of selected files
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))

from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, NextPageTemplate, PageBreak, PageTemplate, Paragraph, Spacer

from booklib import render, theme as T
from booklib.render import Ctx, Heading, PartBanner

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
OUT = ROOT / "output"

BOOK_FILES = sorted(p.name for p in CONTENT.glob("[0-9][0-9]*.md"))
WORKBOOK_FILES = ["12_exercises.md", "13_practice_sets.md"]
FORMULA_FILES = ["15_revision.md"]
WORKSHEET_FILES = ["worksheets/childrens_worksheets.md"]
TARGETS = ["book", "workbook", "formulas", "worksheets"]


class BookDoc(BaseDocTemplate):
    def __init__(self, filename, header, **kw):
        super().__init__(filename, pagesize=T.A4 if hasattr(T, "A4") else None, leftMargin=T.MARGIN_L, rightMargin=T.MARGIN_R,
                         topMargin=T.MARGIN_T, bottomMargin=T.MARGIN_B, **kw)
        self.header = header
        self.current_chapter = ""
        frame = Frame(T.MARGIN_L, T.MARGIN_B, T.FRAME_W, T.PAGE_H - T.MARGIN_T - T.MARGIN_B, id="f", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate("cover", [frame], onPage=self.draw_cover),
            PageTemplate("page", [frame], onPage=lambda c, d: T.notebook_page(c, d, self.header),
                         onPageEnd=lambda c, d: T.notebook_header(c, d, self.header)),
        ])
        self.cover = None

    def handle_documentBegin(self):
        self.current_chapter = ""
        super().handle_documentBegin()

    def draw_cover(self, c, doc):
        T.plain_page(c, doc)
        if self.cover:
            self.cover(c, doc)

    def afterFlowable(self, f):
        if isinstance(f, (Heading, PartBanner)):
            text = f.toc_text
            self.notify("TOCEntry", (f.level, T.with_fallback(escape(text)), self.page, f.key))
            self.canv.bookmarkPage(f.key)
            self.canv.addOutlineEntry(text, f.key, level=f.level, closed=f.level > 0)


def cover_painter(title, subtitle, tagline):
    from reportlab.lib import colors

    def paint(c, doc):
        W, H = T.PAGE_W, T.PAGE_H
        c.saveState()
        c.setFillColor(colors.HexColor("#FFF8EC"))
        c.rect(0, 0, W, H, stroke=0, fill=1)
        palette = [T.BLUE, T.ORANGE, T.GREEN, T.PURPLE, T.PINK, T.TEAL]
        for i in range(14):
            c.setFillColor(colors.Color(*palette[i % 6].rgb(), alpha=0.10))
            c.circle((i * 97) % W, H - 60 - (i * 151) % (H - 120), 30 + (i * 13) % 60, stroke=0, fill=1)
        c.setFillColor(T.BLUE)
        c.setFont(T.FONT["Hand"], 44)
        c.drawCentredString(W / 2, H * 0.68, title)
        c.setFont(T.FONT["HandLight"], 20)
        c.setFillColor(T.TEAL)
        c.drawCentredString(W / 2, H * 0.68 - 40, subtitle)
        c.setFont(T.FONT["Body"], 12)
        c.setFillColor(T.INK)
        for k, line in enumerate(tagline):
            c.drawCentredString(W / 2, H * 0.50 - k * 18, line)
        c.setFont(T.FONT["Mono"], 22)
        c.setFillColor(T.ORANGE)
        c.drawCentredString(W / 2, H * 0.30, "97 × 96 = 93|12      35² = 12|25")
        c.setFillColor(T.GREEN)
        c.drawCentredString(W / 2, H * 0.30 - 32, "1000 − 357 = 643      43 × 11 = 473")
        c.setFont(T.FONT["Body"], 9.5)
        c.setFillColor(T.GREY)
        c.drawCentredString(W / 2, 40, "Original practice material. Exam names are used only to describe the syllabus; no question is an official previous-year question.")
        c.restoreState()
    return paint


def build_pdf(files, out_path, header, title, subtitle, tagline, workbook=False, seed="book", scale=1.0, lines=2):
    st = T.styles(scale)
    doc = BookDoc(str(out_path), header, title=f"{title} — {subtitle}", author="Vedic Maths Zero to Hero project")
    doc.cover = cover_painter(title, subtitle, tagline)
    ctx = Ctx(seed=seed, workbook_mode=workbook, writing_lines=lines)
    story = [NextPageTemplate("page"), PageBreak()]
    story += [Paragraph("Table of Contents", st["h1"]), render.make_toc(st)]
    for name in files:
        md = (CONTENT / name).read_text(encoding="utf-8")
        story += render.parse(md, ctx, st)
    if ctx.pending:
        story += render.answer_key(ctx, st)
    t0 = time.time()
    doc.multiBuild(story, maxPasses=6)
    return {"file": out_path.name, "pages": doc.page, "questions": ctx.qcount, "seconds": round(time.time() - t0, 1), "topics": ctx.stats}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=TARGETS, action="append")
    ap.add_argument("--parts", help="comma-separated file prefixes for a quick preview build")
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    report = {}
    tag = ["From counting to competitive exams — a colourful self-study textbook",
           "Foundations · 16 Sutras & 13 Sub-sutras · Mental maths · Children's course",
           "Government-exam aptitude · 1,000+ verified practice questions with solutions"]
    if a.parts:
        pre = a.parts.split(",")
        files = [f for f in BOOK_FILES if any(f.startswith(p) for p in pre)]
        report["preview"] = build_pdf(files, OUT / "preview.pdf", "Preview", "Vedic Maths", "Preview build", tag)
    else:
        todo = a.only or TARGETS
        if "book" in todo:
            report["book"] = build_pdf(BOOK_FILES, OUT / "Vedic_Maths_Zero_to_Hero.pdf", "Vedic Maths — Zero to Hero", "Vedic Maths", "Zero to Hero", tag)
        if "workbook" in todo:
            report["workbook"] = build_pdf(WORKBOOK_FILES, OUT / "Vedic_Maths_Practice_Workbook.pdf", "Vedic Maths — Practice Workbook",
                                           "Vedic Maths", "Practice Workbook", ["Write your working in the ruled space under each question.",
                                                                                "Answer keys follow each section — attempt first, then check."],
                                           workbook=True, seed="workbook")
        if "formulas" in todo:
            report["formulas"] = build_pdf(FORMULA_FILES, OUT / "Vedic_Maths_Formula_Sheets.pdf", "Vedic Maths — Formula & Shortcut Sheets",
                                           "Vedic Maths", "Formula & Shortcut Sheets", ["Sutra chart · tables · identities · aptitude formulas",
                                                                                        "Common mistakes · exam-day strategy · revision checklists"], seed="formulas")
        if "worksheets" in todo:
            report["worksheets"] = build_pdf(WORKSHEET_FILES, OUT / "Vedic_Maths_Childrens_Worksheets.pdf", "Vedic Maths — Children's Worksheets",
                                             "Maths Fun", "Children's Worksheets (Ages 5–12)",
                                             ["24 printable worksheets in three levels, with pictures and writing space.",
                                              "Answer keys at the end of each level. For parents and teachers to use with children."],
                                             workbook=True, seed="worksheets", scale=1.15, lines=1)
        if (OUT / "build_report.json").exists():
            report = {**json.loads((OUT / "build_report.json").read_text()), **report}
    for k, v in report.items():
        print(f"{k:9s} {v['file']:40s} pages={v['pages']:4d} questions={v['questions']:5d} ({v['seconds']}s)")
    (OUT / "build_report.json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
