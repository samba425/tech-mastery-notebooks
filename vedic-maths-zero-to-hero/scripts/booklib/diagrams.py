"""Vector diagrams drawn with reportlab.graphics, in a light hand-drawn style.

Each public function returns a reportlab Drawing (a platypus Flowable).
In Markdown use:  [[diagram:name arg1 arg2 ...]]
"""
from __future__ import annotations

import math
import random

from reportlab.graphics.shapes import Circle, Drawing, Line, PolyLine, Polygon, Rect, String
from reportlab.lib import colors

from . import theme as T
from .vedic import MINUS, fmt

W = T.FRAME_W


def _font(bold=True):
    return T.FONT["Hand"] if bold else T.FONT["Body"]


def _wobble(x1, y1, x2, y2, rng, amp=0.9, steps=8):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        j = 0 if i in (0, steps) else rng.uniform(-amp, amp)
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        pts += [x1 + dx * t + nx * j, y1 + dy * t + ny * j]
    return pts


def hline(d, x1, y1, x2, y2, color=T.INK, width=1.4, seed=1, arrow=False):
    rng = random.Random(seed + int(x1 * 7 + y1 * 13 + x2 * 3))
    d.add(PolyLine(_wobble(x1, y1, x2, y2, rng), strokeColor=color, strokeWidth=width, strokeLineCap=1, strokeLineJoin=1))
    if arrow:
        ang = math.atan2(y2 - y1, x2 - x1)
        for s in (-1, 1):
            a = ang + math.pi + s * 0.45
            d.add(Line(x2, y2, x2 + 6 * math.cos(a), y2 + 6 * math.sin(a), strokeColor=color, strokeWidth=width, strokeLineCap=1))


def hbox(d, x, y, w, h, stroke=T.INK, fill=None, width=1.3, seed=3):
    if fill is not None:
        d.add(Rect(x, y, w, h, fillColor=fill, strokeColor=None, rx=3, ry=3))
    hline(d, x, y, x + w, y, stroke, width, seed)
    hline(d, x + w, y, x + w, y + h, stroke, width, seed + 1)
    hline(d, x + w, y + h, x, y + h, stroke, width, seed + 2)
    hline(d, x, y + h, x, y, stroke, width, seed + 3)


def text(d, x, y, s, size=12, color=T.INK, anchor="middle", bold=True):
    s = str(s)
    font = _font(bold)
    if any(ord(c) > 127 and ord(c) not in T.CMAP.get(font, set()) for c in s):
        font = T.FONT["Body"]
    d.add(String(x, y, s, fontName=font, fontSize=size, fillColor=color, textAnchor=anchor))


def caption(d, s):
    text(d, d.width / 2, 4, s, 9.5, T.GREY, bold=False)


# ------------------------------------------------------------------ diagrams

def number_line(start="-5", end="5", *jumps):
    """number_line START END [from>to ...]  e.g. number_line 30 70 37>57 57>62"""
    a, b = int(start), int(end)
    d = Drawing(W, 92)
    x0, x1, y = 20, W - 20, 34
    hline(d, x0 - 8, y, x1 + 8, y, T.INK, 1.5, arrow=True)
    hline(d, x0 + 8, y, x0 - 8, y, T.INK, 1.5, arrow=True)
    span = b - a
    step = 1 if span <= 20 else (5 if span <= 100 else 10 ** (len(str(span)) - 1))
    sx = lambda v: x0 + (v - a) / span * (x1 - x0)
    v = a
    while v <= b:
        d.add(Line(sx(v), y - 4, sx(v), y + 4, strokeColor=T.INK, strokeWidth=1))
        text(d, sx(v), y - 16, fmt(v), 9, T.RED if v < 0 else T.INK, bold=False)
        v += step
    colors_cycle = [T.ORANGE, T.GREEN, T.PURPLE, T.BLUE]
    for i, j in enumerate(jumps):
        f, t = [int(z) for z in j.split(">")]
        c = colors_cycle[i % 4]
        xa, xb = sx(f), sx(t)
        mid = (xa + xb) / 2
        h = 18 + 6 * (i % 2)
        pts = []
        for k in range(17):
            u = k / 16
            pts += [xa + (xb - xa) * u, y + 4 + h * math.sin(math.pi * u)]
        d.add(PolyLine(pts, strokeColor=c, strokeWidth=1.6))
        hline(d, pts[-4], pts[-3], xb, y + 4, c, 1.6, arrow=True)
        diff = t - f
        text(d, mid, y + h + 9, (f"+{diff}" if diff > 0 else f"{MINUS}{abs(diff)}"), 10, c)
        d.add(Circle(xa, y, 3, fillColor=c, strokeColor=None))
        d.add(Circle(xb, y, 3, fillColor=c, strokeColor=None))
    return d


def place_value():
    labels = [("Crores", "TC", "C"), ("Lakhs", "TL", "L"), ("Thousands", "TTh", "Th"), ("Ones", "H", "T", "O")]
    cols = ["TC", "C", "TL", "L", "TTh", "Th", "H", "T", "O"]
    vals = ["10,00,00,000", "1,00,00,000", "10,00,000", "1,00,000", "10,000", "1,000", "100", "10", "1"]
    fills = [T.BOX["warn"][2]] * 2 + [T.BOX["tip"][2]] * 2 + [T.BOX["formula"][2]] * 2 + [T.BOX["example"][2]] * 3
    d = Drawing(W, 120)
    cw = (W - 10) / 9
    groups = [(0, 2, "Crores"), (2, 4, "Lakhs"), (4, 6, "Thousands"), (6, 9, "Ones")]
    for s, e, name in groups:
        hbox(d, 5 + s * cw, 88, (e - s) * cw, 22, T.INK, fills[s], seed=s)
        text(d, 5 + (s + e) / 2 * cw, 94, name, 11)
    for i, c in enumerate(cols):
        hbox(d, 5 + i * cw, 58, cw, 28, T.INK, fills[i], seed=10 + i)
        text(d, 5 + (i + 0.5) * cw, 67, c, 12)
        text(d, 5 + (i + 0.5) * cw, 42, vals[i], 7.5, T.GREY, bold=False)
    digits = "345608712"
    for i, ch in enumerate(digits):
        text(d, 5 + (i + 0.5) * cw, 22, ch, 15, T.BLUE)
    caption(d, "34,56,08,712 = thirty-four crore fifty-six lakh eight thousand seven hundred twelve")
    return d


def nikhilam(a="97", b="96", base="100"):
    a, b, base = int(a), int(b), int(base)
    da, db = a - base, b - base
    digits = len(str(base)) - 1
    left, right = a + db, da * db
    d = Drawing(W, 130)
    cx = W / 2
    sd = lambda v: (f"+{v}" if v >= 0 else f"{MINUS}{abs(v)}")
    text(d, cx - 70, 110, f"Base {fmt(base)}", 11, T.GREY, bold=False)
    for row, (n, dv) in enumerate([(a, da), (b, db)]):
        y = 82 - row * 30
        hbox(d, cx - 95, y - 6, 80, 24, T.BLUE, T.BOX["formula"][2], seed=row)
        text(d, cx - 55, y, n, 15, T.BLUE)
        hbox(d, cx + 15, y - 6, 80, 24, T.ORANGE, T.BOX["example"][2], seed=row + 5)
        text(d, cx + 55, y, sd(dv), 15, T.ORANGE)
    hline(d, cx - 15, 82, cx + 15, 52 + 8, T.GREEN, 1.4, arrow=True)
    hline(d, cx - 15, 52 + 8, cx + 15, 82, T.GREEN, 1.4, arrow=True)
    hline(d, cx - 110, 42, cx + 110, 42, T.INK, 1.6)
    text(d, cx - 55, 22, fmt(left), 16, T.GREEN)
    right_s = str(abs(right)).zfill(digits) if 0 <= right < base else sd(right)
    text(d, cx + 55, 22, right_s, 16, T.PURPLE)
    text(d, cx, 22, "|", 16, T.INK)
    text(d, cx - 55, 8, "cross: a + dev(b)", 8.5, T.GREY, bold=False)
    text(d, cx + 55, 8, "vertical: dev × dev", 8.5, T.GREY, bold=False)
    text(d, cx + 170, 22, f"= {fmt(a * b)}", 15, T.RED)
    return d


def urdhva2(a="23", b="41"):
    da, db = str(a).zfill(2), str(b).zfill(2)
    d = Drawing(W, 120)
    panel_w = W / 3
    titles = ["1. Vertical (right)", "2. Crosswise", "3. Vertical (left)"]
    for p in range(3):
        ox = p * panel_w + panel_w / 2
        hbox(d, ox - panel_w / 2 + 8, 14, panel_w - 16, 96, T.GREY, None, 0.8, seed=p)
        text(d, ox, 96, titles[p], 10, T.TEAL)
        xs = [ox - 22, ox + 22]
        for i in range(2):
            col = T.INK
            text(d, xs[i], 70, da[i], 18, col)
            text(d, xs[i], 32, db[i], 18, col)
        c = [T.ORANGE, T.GREEN, T.PURPLE][p]
        if p == 0:
            hline(d, xs[1], 64, xs[1], 50, c, 2)
        elif p == 2:
            hline(d, xs[0], 64, xs[0], 50, c, 2)
        else:
            hline(d, xs[0] + 6, 64, xs[1] - 6, 50, c, 2)
            hline(d, xs[1] - 6, 64, xs[0] + 6, 50, c, 2)
        expr = [f"{da[1]}×{db[1]}", f"{da[0]}×{db[1]} + {da[1]}×{db[0]}", f"{da[0]}×{db[0]}"][p]
        val = [int(da[1]) * int(db[1]), int(da[0]) * int(db[1]) + int(da[1]) * int(db[0]), int(da[0]) * int(db[0])][p]
        text(d, ox, 18, f"{expr} = {val}", 10, c, bold=False)
    return d


def urdhva3():
    """Five-step pattern for 3-digit × 3-digit."""
    d = Drawing(W, 110)
    pw = W / 5
    steps = [[(2, 2)], [(1, 2), (2, 1)], [(0, 2), (2, 0), (1, 1)], [(0, 1), (1, 0)], [(0, 0)]]
    cols = [T.ORANGE, T.GREEN, T.RED, T.PURPLE, T.BLUE]
    for i, pairs in enumerate(steps):
        ox = i * pw + 10
        text(d, ox + pw / 2 - 10, 96, f"Step {i + 1}", 10, cols[i])
        xs = [ox + 14 + k * 26 for k in range(3)]
        for k in range(3):
            d.add(Circle(xs[k], 70, 5, fillColor=T.BOX["formula"][2], strokeColor=T.INK, strokeWidth=0.8))
            d.add(Circle(xs[k], 30, 5, fillColor=T.BOX["example"][2], strokeColor=T.INK, strokeWidth=0.8))
        for top, bot in pairs:
            hline(d, xs[top], 64, xs[bot], 36, cols[i], 1.6, seed=i * 10 + top)
        text(d, ox + pw / 2 - 10, 10, ["units", "tens", "hundreds", "thousands", "ten-thou."][i], 8.5, T.GREY, bold=False)
    return d


def area_square(a="a", b="b"):
    d = Drawing(W, 170)
    ox, oy, A, B = W / 2 - 90, 14, 100, 50
    blocks = [(ox, oy + B, A, A, T.BOX["formula"][2], f"{a}²"), (ox + A, oy + B, B, A, T.BOX["tip"][2], f"{a}{b}"),
              (ox, oy, A, B, T.BOX["tip"][2], f"{a}{b}"), (ox + A, oy, B, B, T.BOX["example"][2], f"{b}²")]
    for i, (x, y, w, h, f, lab) in enumerate(blocks):
        hbox(d, x, y, w, h, T.INK, f, seed=i)
        text(d, x + w / 2, y + h / 2 - 5, lab, 16, T.BLUE)
    text(d, ox + A / 2, oy + A + B + 6, a, 13, T.ORANGE)
    text(d, ox + A + B / 2, oy + A + B + 6, b, 13, T.ORANGE)
    text(d, ox + A + B + 120, oy + 70, f"({a} + {b})² = {a}² + 2{a}{b} + {b}²", 13, T.RED)
    return d


def diff_squares(a="a", b="b"):
    d = Drawing(W, 150)
    ox, oy, A, B = 30, 14, 110, 45
    hbox(d, ox, oy, A, A, T.INK, T.BOX["formula"][2], seed=1)
    d.add(Rect(ox + A - B, oy + A - B, B, B, fillColor=colors.white, strokeColor=T.RED, strokeDashArray=[3, 2]))
    text(d, ox + A - B / 2, oy + A - B / 2 - 4, f"{b}²", 12, T.RED)
    text(d, ox + A / 2, oy + A + 6, a, 12, T.ORANGE)
    text(d, ox + A + 70, oy + 50, "cut & move", 11, T.GREY)
    hline(d, ox + A + 30, oy + 40, ox + A + 110, oy + 40, T.GREY, 1.2, arrow=True)
    rx = ox + A + 130
    hbox(d, rx, oy + 20, A + (A - B), A - B, T.INK, T.BOX["tip"][2], seed=7)
    text(d, rx + (2 * A - B) / 2, oy + 20 + (A - B) / 2 - 5, f"({a} + {b}) × ({a} {MINUS} {b})", 12, T.BLUE)
    text(d, W / 2 + 60, oy + A + 10, f"{a}² {MINUS} {b}² = ({a} + {b})({a} {MINUS} {b})", 13, T.RED)
    return d


def fraction_bar(n="3", den="4"):
    n, den = int(n), int(den)
    d = Drawing(W, 70)
    x0, w = 30, W - 160
    cw = w / den
    for i in range(den):
        hbox(d, x0 + i * cw, 24, cw, 26, T.INK, T.BOX["example"][2] if i < n else colors.white, seed=i)
    text(d, x0 + w + 60, 30, f"{n}/{den} = {n / den * 100:g}%", 15, T.BLUE)
    caption(d, f"{n} of {den} equal parts are shaded")
    return d


def percent_grid(p="35"):
    p = int(p)
    d = Drawing(W, 140)
    s = 11.5
    ox = W / 2 - 150
    for i in range(100):
        r, c = divmod(i, 10)
        d.add(Rect(ox + c * s, 122 - (r + 1) * s, s - 1.2, s - 1.2, fillColor=(T.TEAL if i < p else colors.HexColor("#EEF2F6")), strokeColor=None))
    text(d, ox + 230, 70, f"{p} out of 100", 15, T.TEAL)
    text(d, ox + 230, 50, f"= {p}% = {p / 100:g}", 15, T.BLUE)
    return d


def alligation(c1="20", c2="60", m="35"):
    c1, c2, m = int(c1), int(c2), int(m)
    d = Drawing(W, 140)
    cx = W / 2
    text(d, cx - 90, 115, f"Cheaper: {c1}", 13, T.BLUE)
    text(d, cx + 90, 115, f"Dearer: {c2}", 13, T.RED)
    text(d, cx, 70, f"Mean: {m}", 14, T.PURPLE)
    hline(d, cx - 80, 108, cx + 70, 32, T.GREY, 1.2)
    hline(d, cx + 80, 108, cx - 70, 32, T.GREY, 1.2)
    text(d, cx - 90, 18, f"{c2} {MINUS} {m} = {c2 - m}", 13, T.BLUE)
    text(d, cx + 90, 18, f"{m} {MINUS} {c1} = {m - c1}", 13, T.RED)
    g = math.gcd(c2 - m, m - c1)
    caption_y = 2
    text(d, cx, caption_y, f"Ratio cheaper : dearer = {(c2 - m) // g} : {(m - c1) // g}", 10, T.GREY, bold=False)
    return d


def flow(*steps):
    steps = " ".join(steps).split("|")
    steps = [s.strip() for s in steps if s.strip()]
    n = len(steps)
    per_row = min(n, 4)
    rows = math.ceil(n / per_row)
    bw = (W - 20 - (per_row - 1) * 22) / per_row
    bh = 46
    d = Drawing(W, rows * (bh + 22) + 6)
    palette = [T.BOX[k] for k in ("formula", "example", "tip", "recap", "memory", "note")]
    for i, s in enumerate(steps):
        r, c = divmod(i, per_row)
        x = 10 + c * (bw + 22)
        y = d.height - (r + 1) * (bh + 22) + 14
        _, accent, bg = palette[i % len(palette)]
        hbox(d, x, y, bw, bh, accent, bg, seed=i)
        words = s.split()
        lines, cur = [], ""
        maxch = max(10, int(bw / 5.6))
        for wd in words:
            if len(cur) + len(wd) + 1 > maxch:
                lines.append(cur)
                cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        lines = lines[:3]
        for k, ln in enumerate(lines):
            text(d, x + bw / 2, y + bh / 2 + (len(lines) - 1) * 6 - k * 12 - 3, ln, 9.5, T.INK, bold=False)
        if i < n - 1:
            if c < per_row - 1:
                hline(d, x + bw + 3, y + bh / 2, x + bw + 19, y + bh / 2, accent, 1.5, arrow=True)
            else:
                hline(d, x + bw / 2, y - 3, x + bw / 2, y - 16, accent, 1.5, arrow=True)
    return d


def ten_frame(n="7"):
    n = int(n)
    d = Drawing(W, 80)
    s = 30
    ox = W / 2 - 2.5 * s - 60
    for i in range(10):
        r, c = divmod(i, 5)
        hbox(d, ox + c * s, 44 - r * s, s, s, T.INK, None, 1, seed=i)
        if i < n:
            d.add(Circle(ox + c * s + s / 2, 44 - r * s + s / 2, 10, fillColor=T.RED if i < 5 else T.ORANGE, strokeColor=None))
    text(d, ox + 5 * s + 80, 36, f"{n} + {10 - n} = 10", 16, T.BLUE)
    return d


def array(rows="3", cols="4"):
    r, c = int(rows), int(cols)
    s = 20
    d = Drawing(W, r * s + 30)
    ox = W / 2 - c * s / 2 - 70
    for i in range(r):
        for j in range(c):
            d.add(Circle(ox + j * s + s / 2, d.height - 14 - i * s, 7, fillColor=[T.GREEN, T.ORANGE, T.BLUE, T.PINK][i % 4], strokeColor=None))
    text(d, ox + c * s + 90, d.height / 2 - 6, f"{r} rows × {c} = {r * c}", 15, T.BLUE)
    return d


def magic_square():
    sq = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    d = Drawing(W, 120)
    s = 34
    ox = W / 2 - 1.5 * s - 80
    for i in range(3):
        for j in range(3):
            hbox(d, ox + j * s, 100 - (i + 1) * s, s, s, T.INK, T.BOX["recap"][2] if (i + j) % 2 == 0 else T.BOX["tip"][2], seed=i * 3 + j)
            text(d, ox + j * s + s / 2, 100 - (i + 1) * s + s / 2 - 6, sq[i][j], 16, T.PURPLE)
    text(d, ox + 3 * s + 110, 55, "Every row, column and", 12, T.INK, bold=False)
    text(d, ox + 3 * s + 110, 38, "diagonal adds to 15", 12, T.INK, bold=False)
    return d


def factor_tree(n="360"):
    n = int(n)
    d = Drawing(W, 40)
    nodes = []
    m, p, level = n, 2, 0
    while m > 1:
        while m % p:
            p += 1
        nodes.append((m, p))
        m //= p
    depth = len(nodes)
    d = Drawing(W, depth * 30 + 30)
    x = W / 2 - 40
    y = d.height - 18
    for i, (m, p) in enumerate(nodes):
        text(d, x, y, fmt(m), 13, T.BLUE)
        if m == p:
            break
        hline(d, x - 4, y - 4, x - 30, y - 22, T.GREY, 1)
        hline(d, x + 4, y - 4, x + 30, y - 22, T.GREY, 1)
        d.add(Circle(x - 34, y - 30, 9, fillColor=T.BOX["tip"][2], strokeColor=T.GREEN))
        text(d, x - 34, y - 34, p, 11, T.GREEN)
        x += 30
        y -= 30
    return d


def bar_model(a="3", b="2", total=""):
    a, b = int(a), int(b)
    d = Drawing(W, 80)
    unit = (W - 140) / (a + b)
    for i in range(a + b):
        hbox(d, 30 + i * unit, 30, unit, 26, T.INK, T.BOX["formula"][2] if i < a else T.BOX["example"][2], seed=i)
    text(d, 30 + a * unit / 2, 62, f"A: {a} parts", 11, T.BLUE)
    text(d, 30 + a * unit + b * unit / 2, 62, f"B: {b} parts", 11, T.ORANGE)
    if total:
        text(d, W - 50, 38, total, 13, T.RED)
        hline(d, 30, 22, 30 + (a + b) * unit, 22, T.RED, 1)
    caption(d, f"{a + b} equal parts in all")
    return d


def dst_triangle():
    d = Drawing(W, 130)
    cx = W / 2 - 60
    d.add(Polygon([cx - 70, 16, cx + 70, 16, cx, 116], fillColor=T.BOX["note"][2], strokeColor=None))
    hline(d, cx - 70, 16, cx + 70, 16, T.TEAL, 1.6)
    hline(d, cx + 70, 16, cx, 116, T.TEAL, 1.6)
    hline(d, cx, 116, cx - 70, 16, T.TEAL, 1.6)
    hline(d, cx - 40, 58, cx + 40, 58, T.TEAL, 1.2)
    text(d, cx, 75, "D", 20, T.RED)
    text(d, cx - 22, 30, "S", 20, T.BLUE)
    text(d, cx + 22, 30, "T", 20, T.GREEN)
    text(d, cx, 30, "×", 14, T.INK)
    for i, s in enumerate(["D = S × T", "S = D ÷ T", "T = D ÷ S", "km/h × 5/18 = m/s"]):
        text(d, cx + 180, 90 - i * 20, s, 12, T.INK, bold=False)
    return d


def objects(groups="3", per="4", kind="apple"):
    g, p = int(groups), int(per)
    col = {"apple": T.RED, "orange": T.ORANGE, "ball": T.BLUE, "leaf": T.GREEN}.get(kind, T.PINK)
    gw = p * 18 + 16
    d = Drawing(W, 70)
    ox = max(10, W / 2 - g * (gw + 10) / 2 - 50)
    for i in range(g):
        x = ox + i * (gw + 10)
        hbox(d, x, 18, gw, 38, T.GREY, None, 0.9, seed=i)
        for j in range(p):
            d.add(Circle(x + 14 + j * 18, 37, 7, fillColor=col, strokeColor=None))
            if kind == "apple":
                d.add(Line(x + 14 + j * 18, 44, x + 16 + j * 18, 49, strokeColor=T.GREEN, strokeWidth=1.4))
    text(d, ox + g * (gw + 10) + 60, 32, f"{g} × {p} = {g * p}", 15, T.BLUE)
    return d


def square_end5(n="35"):
    n = int(n)
    a = n // 10
    return flow(f"{n}²", f"take {a}", f"{a} × {a + 1} = {a * (a + 1)}", f"attach 25", f"{fmt(n * n)}")


def compare_bars(*pairs):
    """compare_bars label=value ... simple bar chart for data interpretation."""
    items = [(p.split("=")[0].replace("_", " "), float(p.split("=")[1])) for p in pairs]
    d = Drawing(W, 150)
    mx = max(v for _, v in items) or 1
    bw = (W - 60) / len(items)
    for i, (lab, v) in enumerate(items):
        h = v / mx * 100
        x = 40 + i * bw
        hbox(d, x + 6, 26, bw - 12, h, [T.BLUE, T.ORANGE, T.GREEN, T.PURPLE, T.TEAL, T.PINK][i % 6], T.BOX[["formula", "example", "tip", "recap", "note", "memory"][i % 6]][2], seed=i)
        text(d, x + bw / 2, 30 + h, f"{v:g}", 10, T.INK)
        text(d, x + bw / 2, 12, lab, 9.5, T.GREY, bold=False)
    hline(d, 36, 26, W - 16, 26, T.INK, 1.2)
    return d


REGISTRY = {name: fn for name, fn in globals().items() if callable(fn) and not name.startswith("_") and name not in
            ("hline", "hbox", "text", "caption", "Drawing", "Circle", "Line", "PolyLine", "Polygon", "Rect", "String", "fmt")}


def build(spec: str):
    parts = spec.split()
    name, args = parts[0], parts[1:]
    if name not in REGISTRY:
        raise KeyError(f"Unknown diagram '{name}'")
    return REGISTRY[name](*args)
