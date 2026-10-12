"""Fonts, colours, paragraph styles and the notebook page template."""
from __future__ import annotations

import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
PAGE_W, PAGE_H = A4
MARGIN_L, MARGIN_R, MARGIN_T, MARGIN_B = 24 * mm, 16 * mm, 20 * mm, 18 * mm
FRAME_W = PAGE_W - MARGIN_L - MARGIN_R

# ------------------------------------------------------------------ colours
INK = colors.HexColor("#1F2A44")
BLUE = colors.HexColor("#1E5AA8")
TEAL = colors.HexColor("#0F7C7A")
GREEN = colors.HexColor("#2E7D32")
ORANGE = colors.HexColor("#D9730D")
RED = colors.HexColor("#C62828")
PURPLE = colors.HexColor("#6A3FA0")
PINK = colors.HexColor("#C2185B")
GREY = colors.HexColor("#6B7280")
RULE = colors.HexColor("#E3ECF7")
MARGIN_RED = colors.HexColor("#F3B6B6")
PAPER = colors.HexColor("#FFFEFA")

BOX = {
    # kind: (title, accent, background)
    "tip": ("Tip", GREEN, colors.HexColor("#EAF6EC")),
    "warn": ("Common mistake", RED, colors.HexColor("#FDECEC")),
    "formula": ("Formula", BLUE, colors.HexColor("#E8F0FB")),
    "example": ("Worked example", ORANGE, colors.HexColor("#FFF4E5")),
    "recap": ("Quick revision", PURPLE, colors.HexColor("#F2ECFA")),
    "memory": ("Memory trick", PINK, colors.HexColor("#FCE9F1")),
    "note": ("Note", TEAL, colors.HexColor("#E6F5F4")),
    "history": ("History & accuracy", GREY, colors.HexColor("#F1F2F4")),
    "why": ("Why it works", BLUE, colors.HexColor("#EEF3FC")),
    "when": ("When to use / when not to use", TEAL, colors.HexColor("#E9F7F6")),
    "objective": ("Learning objective", GREEN, colors.HexColor("#F0F8EC")),
    "selftest": ("Short self-test", ORANGE, colors.HexColor("#FFF7EC")),
    "parent": ("For parents & teachers", PURPLE, colors.HexColor("#F5F0FB")),
    "exam": ("Exam strategy", RED, colors.HexColor("#FFF0F0")),
    "approx": ("Approximate method", ORANGE, colors.HexColor("#FFF8E6")),
}

# ------------------------------------------------------------------ fonts
FONT_SPECS = {
    # name: list of (path, subfont index) candidates
    "Body": [("/System/Library/Fonts/HelveticaNeue.ttc", 0)],
    "Body-Bold": [("/System/Library/Fonts/HelveticaNeue.ttc", 1)],
    "Body-Italic": [("/System/Library/Fonts/HelveticaNeue.ttc", 2)],
    "Body-BoldItalic": [("/System/Library/Fonts/HelveticaNeue.ttc", 3)],
    "Hand": [("/System/Library/Fonts/Noteworthy.ttc", 1), (str(ROOT / "assets/fonts/Hand.ttf"), 0)],
    "HandLight": [("/System/Library/Fonts/Noteworthy.ttc", 0)],
    "Mono": [("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 0)],
    "Fallback": [("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 0)],
}
BUILTIN = {"Body": "Helvetica", "Body-Bold": "Helvetica-Bold", "Body-Italic": "Helvetica-Oblique",
           "Body-BoldItalic": "Helvetica-BoldOblique", "Hand": "Helvetica-Bold", "HandLight": "Helvetica",
           "Mono": "Courier-Bold", "Fallback": "Helvetica"}
FONT = {}
CMAP: dict[str, set] = {}


def register_fonts():
    if FONT:
        return
    for name, cands in FONT_SPECS.items():
        for path, idx in cands:
            if os.path.exists(path):
                try:
                    f = TTFont(f"VM-{name}", path, subfontIndex=idx)
                    pdfmetrics.registerFont(f)
                    FONT[name] = f"VM-{name}"
                    CMAP[FONT[name]] = set(f.face.charToGlyph.keys())
                    break
                except Exception:
                    continue
        if name not in FONT:
            FONT[name] = BUILTIN[name]
            CMAP[FONT[name]] = set(range(32, 127))
    from reportlab.lib.fonts import addMapping
    if FONT["Body"].startswith("VM-"):
        addMapping(FONT["Body"], 0, 0, FONT["Body"])
        addMapping(FONT["Body"], 1, 0, FONT["Body-Bold"])
        addMapping(FONT["Body"], 0, 1, FONT["Body-Italic"])
        addMapping(FONT["Body"], 1, 1, FONT["Body-BoldItalic"])


def covered_everywhere(ch: str) -> bool:
    o = ord(ch)
    return all(o in CMAP[FONT[k]] for k in ("Body", "Body-Bold", "Body-Italic", "Mono", "Hand"))


def fallback_font_for(ch: str) -> str:
    o = ord(ch)
    for k in ("Body", "Fallback", "Mono", "Hand"):
        if o in CMAP[FONT[k]]:
            return FONT[k]
    return FONT["Body"]


def with_fallback(escaped_text: str) -> str:
    """Wrap characters that some book fonts lack in an explicit <font> tag.

    Operates on already-escaped text; tags in the input are left untouched.
    """
    out = []
    in_tag = False
    for ch in escaped_text:
        if ch == "<":
            in_tag = True
        if in_tag or ord(ch) < 128 or covered_everywhere(ch):
            out.append(ch)
        else:
            out.append(f'<font name="{fallback_font_for(ch)}">{ch}</font>')
        if ch == ">":
            in_tag = False
    return "".join(out)


# ------------------------------------------------------------------ styles
def styles(scale: float = 1.0):
    register_fonts()
    s = {}
    base = dict(fontName=FONT["Body"], textColor=INK, leading=15.5 * scale, fontSize=10.6 * scale)
    s["body"] = ParagraphStyle("body", **base, spaceAfter=5)
    s["small"] = ParagraphStyle("small", **{**base, "fontSize": 9 * scale, "leading": 12 * scale}, spaceAfter=2)
    s["cell"] = ParagraphStyle("cell", **{**base, "fontSize": 9.4 * scale, "leading": 12.4 * scale})
    s["cellhead"] = ParagraphStyle("cellhead", parent=s["cell"], fontName=FONT["Body-Bold"], textColor=colors.white)
    s["bullet"] = ParagraphStyle("bullet", parent=s["body"], leftIndent=16, bulletIndent=4, spaceAfter=2.5)
    s["mono"] = ParagraphStyle("mono", fontName=FONT["Mono"], fontSize=10.5 * scale, leading=14 * scale, textColor=colors.HexColor("#102A5C"))
    s["part"] = ParagraphStyle("part", fontName=FONT["Hand"], fontSize=30, leading=38, textColor=colors.white, alignment=TA_LEFT)
    s["partsub"] = ParagraphStyle("partsub", fontName=FONT["HandLight"], fontSize=15, leading=21, textColor=colors.white)
    s["h1"] = ParagraphStyle("h1", fontName=FONT["Hand"], fontSize=21, leading=27, textColor=BLUE, spaceBefore=4, spaceAfter=8)
    s["h2"] = ParagraphStyle("h2", fontName=FONT["Hand"], fontSize=15.5, leading=21, textColor=TEAL, spaceBefore=10, spaceAfter=4)
    s["h3"] = ParagraphStyle("h3", fontName=FONT["Hand"], fontSize=12.8, leading=17, textColor=ORANGE, spaceBefore=7, spaceAfter=3)
    s["boxtitle"] = ParagraphStyle("boxtitle", fontName=FONT["Hand"], fontSize=11.5, leading=15, textColor=INK)
    s["title"] = ParagraphStyle("title", fontName=FONT["Hand"], fontSize=38, leading=46, textColor=BLUE, alignment=TA_CENTER)
    s["subtitle"] = ParagraphStyle("subtitle", fontName=FONT["HandLight"], fontSize=16, leading=22, textColor=TEAL, alignment=TA_CENTER)
    s["center"] = ParagraphStyle("center", parent=s["body"], alignment=TA_CENTER)
    s["toc0"] = ParagraphStyle("toc0", fontName=FONT["Body-Bold"], fontSize=11, leading=15, textColor=BLUE, leftIndent=0, spaceBefore=6)
    s["toc1"] = ParagraphStyle("toc1", fontName=FONT["Body"], fontSize=9.8, leading=13, textColor=INK, leftIndent=14)
    s["toc2"] = ParagraphStyle("toc2", fontName=FONT["Body"], fontSize=8.8, leading=11.5, textColor=GREY, leftIndent=28)
    s["q"] = ParagraphStyle("q", parent=s["body"], leftIndent=22, firstLineIndent=-22, spaceAfter=3)
    s["ans"] = ParagraphStyle("ans", parent=s["small"], leftIndent=22, firstLineIndent=-22, spaceAfter=3.5)
    return s


# ------------------------------------------------------------------ page decoration
def notebook_page(canvas, doc, header: str = "Vedic Maths — Zero to Hero"):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    y = PAGE_H - MARGIN_T + 2
    while y > MARGIN_B - 4:
        canvas.line(10 * mm, y, PAGE_W - 8 * mm, y)
        y -= 7.6 * mm
    canvas.setStrokeColor(MARGIN_RED)
    canvas.setLineWidth(0.9)
    canvas.line(MARGIN_L - 5 * mm, 0, MARGIN_L - 5 * mm, PAGE_H)
    # hole punches
    canvas.setFillColor(colors.HexColor("#EEF1F5"))
    for hy in (PAGE_H * 0.2, PAGE_H * 0.5, PAGE_H * 0.8):
        canvas.circle(8 * mm, hy, 2.6 * mm, stroke=0, fill=1)
    canvas.restoreState()


def notebook_header(canvas, doc, header: str = "Vedic Maths — Zero to Hero"):
    canvas.saveState()
    canvas.setFont(FONT["HandLight"], 9)
    canvas.setFillColor(GREY)
    chap = getattr(doc, "current_chapter", "")
    canvas.drawString(MARGIN_L, PAGE_H - 12 * mm, header)
    if chap:
        canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 12 * mm, chap[:70])
    canvas.setFont(FONT["Hand"], 11)
    canvas.setFillColor(BLUE)
    canvas.drawCentredString(PAGE_W / 2, 9 * mm, f"— {doc.page} —")
    canvas.restoreState()


def plain_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()
