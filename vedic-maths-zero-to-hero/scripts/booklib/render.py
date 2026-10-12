"""Markdown (with a few book directives) → ReportLab flowables.

Syntax summary (see README.md for the full list):
  # Part title            new part (coloured banner page)
  ## Chapter              chapter heading (starts a new page)
  ### Section / #### Sub  section headings
  :::tip Optional title   callout box (tip, warn, formula, example, recap, memory,
  ...                     note, history, why, when, objective, selftest, parent,
  :::                     exam, approx)
  :::compare              two-column comparison; separate columns with a line '|||'
  ```calc                 worked calculation in a monospaced box
  | a | b |               table (first row = header)
  [[diagram:name args]]   vector diagram (see diagrams.py)
  [[flow:A | B | C]]      flow chart
  [[practice:keys|count|title]]   generated practice; answers go to next [[answerkey]]
  [[answerkey]]           print pending answers with worked solutions
  [[table:name args]]     generated reference table (squares, cubes, tables …)
  [[lines:N]]             N ruled writing lines
  [[pagebreak]]
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass, field

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (CondPageBreak, Flowable, KeepTogether, PageBreak, Paragraph, Spacer, Table,
                                TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

from . import diagrams, tables
from . import theme as T
from .questions import GENERATORS, make

def split_row(line: str) -> list[str]:
    r"""Split a Markdown table row on unescaped '|'; '\|' stays a literal pipe inside a cell."""
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [c.strip().replace("\\|", "|") for c in cells]


INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<b>\1</b>"),
    (re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])"), r"<i>\1</i>"),
    (re.compile(r"`([^`]+)`"), r'<font name="{mono}" color="#102A5C">\1</font>'),
    (re.compile(r"\^\{([^}]+)\}"), r"<super>\1</super>"),
    (re.compile(r"_\{([^}]+)\}"), r"<sub>\1</sub>"),
    (re.compile(r"==(.+?)=="), r'<font backColor="#FFF3A3">\1</font>'),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s: str) -> str:
    s = esc(s)
    for pat, rep in INLINE:
        s = pat.sub(rep.replace("{mono}", T.FONT["Mono"]), s)
    return T.with_fallback(s)


class Heading(Paragraph):
    """Paragraph that registers itself in the TOC and PDF outline."""

    def __init__(self, text, style, level, key, toc_text=None):
        super().__init__(inline(text), style)
        self.level = level
        self.key = key
        self.toc_text = toc_text or re.sub(r"[*`]", "", text)


class SetChapter(Flowable):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.width = self.height = 0

    def draw(self):
        self.canv._doctemplate.current_chapter = self.title


class PartBanner(Flowable):
    def __init__(self, title, subtitle, color, key):
        super().__init__()
        self.title, self.subtitle, self.color, self.key = title, subtitle, color, key
        self.level = 0
        self.toc_text = f"{title} — {subtitle}" if subtitle else title
        self.width, self.height = T.FRAME_W, 230

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(self.color)
        c.roundRect(0, 0, self.width, self.height, 14, stroke=0, fill=1)
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.12))
        for i in range(6):
            c.circle(self.width - 40 - i * 34, self.height - 30 - (i % 2) * 20, 22 + i * 3, stroke=0, fill=1)
        st = T.styles()
        p = Paragraph(inline(self.title), st["part"])
        w, h = p.wrap(self.width - 40, 200)
        p.drawOn(c, 20, self.height - 30 - h)
        if self.subtitle:
            q = Paragraph(inline(self.subtitle), st["partsub"])
            w2, h2 = q.wrap(self.width - 40, 120)
            q.drawOn(c, 20, 24)
        c.restoreState()


PART_COLORS = [T.BLUE, T.TEAL, T.ORANGE, T.PURPLE, T.GREEN, T.PINK, T.RED, colors.HexColor("#3949AB"),
               colors.HexColor("#00897B"), colors.HexColor("#F4511E"), colors.HexColor("#8E24AA"), colors.HexColor("#43A047"),
               colors.HexColor("#1E88E5"), colors.HexColor("#6D4C41"), colors.HexColor("#5E35B1")]


@dataclass
class Ctx:
    seed: str = "book"
    pending: list = field(default_factory=list)
    qcount: int = 0
    heading_n: int = 0
    part_n: int = 0
    used_texts: set = field(default_factory=set)
    workbook_mode: bool = False
    writing_lines: int = 2
    stats: dict = field(default_factory=dict)


def writing_lines(n: int, width=T.FRAME_W):
    rows = [[""] for _ in range(n)]
    t = Table(rows, colWidths=[width], rowHeights=[8.5 * mm] * n)
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#B9C7DA"))]))
    return t


def callout(kind: str, title: str, flows: list, st):
    default_title, accent, bg = T.BOX.get(kind, T.BOX["note"])
    title = title or default_title
    rows = [[Paragraph(inline(title), ParagraphStyle_color(st["boxtitle"], accent))]] + [[f] for f in flows]
    t = Table(rows, colWidths=[T.FRAME_W - 4])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 5)]


_color_cache = {}


def ParagraphStyle_color(style, color):
    key = (style.name, str(color))
    if key not in _color_cache:
        from reportlab.lib.styles import ParagraphStyle
        _color_cache[key] = ParagraphStyle(style.name + str(len(_color_cache)), parent=style, textColor=color)
    return _color_cache[key]


def calc_block(lines: list[str], st):
    rows = []
    for ln in lines or [" "]:
        s = esc(ln).replace(" ", "&nbsp;") or "&nbsp;"
        rows.append([Paragraph(T.with_fallback(s), st["mono"])])
    t = Table(rows, colWidths=[T.FRAME_W - 30])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F5F9FF")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#9DB7DE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 5),
    ]))
    t.hAlign = "CENTER"
    return [Spacer(1, 2), t, Spacer(1, 6)]


def md_table(rows: list[list[str]], st, width=T.FRAME_W):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    data = [[Paragraph(inline(c), st["cellhead"] if i == 0 else st["cell"]) for c in r] for i, r in enumerate(rows)]
    # column widths proportional to content length, bounded
    lens = [max(len(r[j]) for r in rows) + 4 for j in range(ncol)]
    tot = sum(lens)
    widths = [max(width * 0.08, width * l / tot) for l in lens]
    k = width / sum(widths)
    widths = [w * k for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), T.TEAL),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B8C4D6")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F2F7FB")))
        else:
            style.append(("BACKGROUND", (0, i), (-1, i), colors.white))
    t.setStyle(TableStyle(style))
    return [Spacer(1, 3), t, Spacer(1, 7)]


def unique_questions(keys, count, ctx: Ctx, label):
    out = []
    i = 0
    tries = 0
    while len(out) < count and tries < count * 40:
        key = keys[i % len(keys)]
        rng = random.Random(f"{ctx.seed}|{label}|{key}|{tries}")
        q = make(key, rng)
        tries += 1
        i += 1
        if q.text in ctx.used_texts:
            continue
        ctx.used_texts.add(q.text)
        out.append(q)
    if len(out) < count:
        print(f"  warning: '{label}' has {len(out)}/{count} unique questions")
    return out


def practice_block(spec: str, ctx: Ctx, st, space_lines=0):
    parts = [p.strip() for p in spec.split("|")]
    keys = [k.strip() for k in parts[0].split(",")]
    for k in keys:
        if k not in GENERATORS:
            raise KeyError(f"Unknown question generator: {k}")
    count = int(parts[1]) if len(parts) > 1 else 6
    title = parts[2] if len(parts) > 2 else "Practice questions"
    qs = unique_questions(keys, count, ctx, title)
    flows = [CondPageBreak(60 * mm), Paragraph(inline("✎ " + title), st["h3"])]
    start = ctx.qcount
    for q in qs:
        ctx.qcount += 1
        tag = "" if q.exact else "  <i>(approximate)</i>"
        flows.append(Paragraph(f"<b>{ctx.qcount}.</b>&nbsp;&nbsp;" + inline(q.text) + tag, st["q"]))
        if space_lines:
            flows.append(writing_lines(space_lines))
        ctx.pending.append((ctx.qcount, q))
        ctx.stats[q.topic] = ctx.stats.get(q.topic, 0) + 1
    flows.append(Paragraph(inline(f"*Answers: see the answer key (questions {start + 1}–{ctx.qcount}).*"), st["small"]))
    return flows


def answer_key(ctx: Ctx, st, title="Answer key with worked solutions"):
    if not ctx.pending:
        return []
    flows = [CondPageBreak(50 * mm), Paragraph(inline(title), st["h2"])]
    for n, q in ctx.pending:
        sol = f" — {inline(q.solution)}" if q.solution else ""
        flows.append(Paragraph(f'<b>{n}.</b>&nbsp;&nbsp;<font color="#2E7D32"><b>{inline(q.answer)}</b></font>{sol}', st["ans"]))
    ctx.pending.clear()
    return flows


TABLE_LINE = re.compile(r"^\s*\|.*\|\s*$")
SEP_LINE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def parse(md: str, ctx: Ctx, st) -> list:
    lines = md.splitlines()
    flows: list = []
    para: list[str] = []
    i = 0

    def flush_para(target):
        if para:
            target.append(Paragraph(inline(" ".join(para)), st["body"]))
            para.clear()

    def parse_block(block_lines):
        sub = []
        j = 0
        buf: list[str] = []

        def fl():
            if buf:
                sub.append(Paragraph(inline(" ".join(buf)), st["body"]))
                buf.clear()

        while j < len(block_lines):
            ln = block_lines[j]
            s = ln.strip()
            if s.startswith("```"):
                fl()
                j += 1
                code = []
                while j < len(block_lines) and not block_lines[j].strip().startswith("```"):
                    code.append(block_lines[j].rstrip())
                    j += 1
                sub.extend(calc_block(code, st))
            elif TABLE_LINE.match(ln):
                fl()
                rows = []
                while j < len(block_lines) and TABLE_LINE.match(block_lines[j]):
                    if not SEP_LINE.match(block_lines[j]):
                        rows.append(split_row(block_lines[j]))
                    j += 1
                sub.extend(md_table(rows, st, T.FRAME_W - 30))
                continue
            elif re.match(r"^\s*([-*]|\d+\.)\s+", ln):
                fl()
                m = re.match(r"^\s*([-*]|\d+\.)\s+(.*)$", ln)
                bullet = "•" if m.group(1) in "-*" else m.group(1)
                sub.append(Paragraph(inline(m.group(2)), st["bullet"], bulletText=bullet))
            elif s.startswith("[[") and s.endswith("]]"):
                fl()
                sub.extend(directive(s[2:-2], ctx, st))
            elif not s:
                fl()
            else:
                buf.append(s)
            j += 1
        fl()
        return sub

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith(":::") and len(s) > 3:
            flush_para(flows)
            head = s[3:].strip()
            kind, _, title = head.partition(" ")
            j = i + 1
            block = []
            while j < len(lines) and lines[j].strip() != ":::":
                block.append(lines[j])
                j += 1
            if kind == "compare":
                cols = "\n".join(block).split("|||")
                flows.extend(compare(cols, title, ctx, st, parse_block))
            else:
                flows.extend(callout(kind, title, parse_block(block), st))
            i = j + 1
            continue
        if s.startswith("```"):
            flush_para(flows)
            j = i + 1
            code = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                code.append(lines[j].rstrip())
                j += 1
            flows.extend(calc_block(code, st))
            i = j + 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush_para(flows)
            level = len(m.group(1))
            title = m.group(2).strip()
            ctx.heading_n += 1
            key = f"h{ctx.heading_n}"
            if level == 1:
                main, _, subtitle = title.partition(" — ")
                color = PART_COLORS[ctx.part_n % len(PART_COLORS)]
                ctx.part_n += 1
                flows += [PageBreak(), SetChapter(main), Spacer(1, 40 * mm), PartBanner(main, subtitle, color, key), Spacer(1, 10 * mm)]
            elif level == 2:
                flows += [PageBreak(), SetChapter(title), Heading(title, st["h1"], 1, key)]
            elif level == 3:
                flows += [CondPageBreak(45 * mm), Heading(title, st["h2"], 2, key)]
            else:
                flows += [CondPageBreak(30 * mm), Paragraph(inline(title), st["h3"])]
            i += 1
            continue
        if TABLE_LINE.match(ln):
            flush_para(flows)
            rows = []
            while i < len(lines) and TABLE_LINE.match(lines[i]):
                if not SEP_LINE.match(lines[i]):
                    rows.append(split_row(lines[i]))
                i += 1
            flows.extend(md_table(rows, st))
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            flush_para(flows)
            mm_ = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
            indent = len(mm_.group(1))
            bullet = "•" if mm_.group(2) in "-*" else mm_.group(2)
            style = st["bullet"]
            if indent >= 2:
                from reportlab.lib.styles import ParagraphStyle
                style = ParagraphStyle("b2", parent=st["bullet"], leftIndent=32, bulletIndent=20)
                bullet = "◦" if bullet == "•" else bullet
            flows.append(Paragraph(inline(mm_.group(3)), style, bulletText=bullet))
            i += 1
            continue
        if s == "---":
            flush_para(flows)
            flows.append(diagrams_divider())
            i += 1
            continue
        if s.startswith("[[") and s.endswith("]]"):
            flush_para(flows)
            flows.extend(directive(s[2:-2], ctx, st))
            i += 1
            continue
        if not s:
            flush_para(flows)
        else:
            para.append(s)
        i += 1
    flush_para(flows)
    return flows


def diagrams_divider():
    from reportlab.graphics.shapes import Drawing
    d = Drawing(T.FRAME_W, 14)
    diagrams.hline(d, T.FRAME_W * 0.3, 7, T.FRAME_W * 0.7, 7, colors.HexColor("#9DB7DE"), 1.2, seed=99)
    return d


def compare(cols, title, ctx, st, parse_block):
    left = parse_block(cols[0].strip("\n").splitlines())
    right = parse_block(cols[1].strip("\n").splitlines()) if len(cols) > 1 else []
    titles = (title or "Standard method ||| Shortcut method").split("|||")
    lt = titles[0].strip()
    rt = titles[1].strip() if len(titles) > 1 else "Shortcut method"
    hw = (T.FRAME_W - 8) / 2
    # Shrink nested tables to the column width
    def fit(fl):
        out = []
        for f in fl:
            if isinstance(f, Table):
                f._argW = [w * (hw - 16) / sum(f._argW) for w in f._argW]
            out.append(f)
        return out
    data = [[Paragraph(inline(lt), ParagraphStyle_color(st["boxtitle"], T.BLUE)), Paragraph(inline(rt), ParagraphStyle_color(st["boxtitle"], T.GREEN))],
            [fit(left), fit(right)]]
    t = Table(data, colWidths=[hw, hw])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), T.BOX["formula"][2]),
        ("BACKGROUND", (1, 0), (1, -1), T.BOX["tip"][2]),
        ("LINEABOVE", (0, 0), (0, 0), 3, T.BLUE),
        ("LINEABOVE", (1, 0), (1, 0), 3, T.GREEN),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 6)]


def directive(body: str, ctx: Ctx, st):
    name, _, arg = body.partition(":")
    name = name.strip()
    if name == "pagebreak":
        return [PageBreak()]
    if name == "lines":
        return [writing_lines(int(arg or 4))]
    if name == "space":
        return [Spacer(1, int(arg) * mm)]
    if name == "diagram":
        d = diagrams.build(arg.strip())
        return [Spacer(1, 2), KeepTogether([d]), Spacer(1, 6)]
    if name == "flow":
        return [Spacer(1, 2), diagrams.flow(arg), Spacer(1, 6)]
    if name == "practice":
        return practice_block(arg, ctx, st, ctx.writing_lines if ctx.workbook_mode else 0)
    if name == "answerkey":
        return answer_key(ctx, st, arg.strip() or "Answer key with worked solutions")
    if name == "table":
        parts = arg.split()
        rows = tables.build(parts[0], *parts[1:])
        return md_table(rows, st)
    if name == "generated":
        from . import generated
        return generated.build(arg.strip(), ctx, st)
    raise KeyError(f"Unknown directive [[{body}]]")


class TOC(TableOfContents):
    pass


def make_toc(st):
    toc = TOC()
    toc.levelStyles = [st["toc0"], st["toc1"], st["toc2"]]
    toc.dotsMinLevel = 0
    return toc
