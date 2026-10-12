#!/usr/bin/env python3
"""Independently verify arithmetic written by hand in content/*.md.

Checks performed
1. Inline equations such as "46 × 37 = 1,702", "97² = 9,409", "1,000 − 468 = 532",
   "35% of 640 = 224", "√144 = 12" anywhere in the text (including calc blocks).
   Chained forms "a op b op c = d" are evaluated left-to-right only when every
   operator is + or − (so no precedence ambiguity).
2. Table rows whose "Problem" cell is a pure arithmetic expression and whose
   last cell is a number.
3. Every question generator: answers re-checked against independent expressions.

Exit status is non-zero if anything fails.
"""
from __future__ import annotations

import math
import random
import re
import sys
from datetime import date
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from booklib.render import split_row  # noqa: E402

NUM = r"\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\d+(?:\.\d+)?"
OPS = {"×": "*", "x": "*", "÷": "/", "+": "+", "−": "-", "-": "-"}
SUP = {"²": 2, "³": 3}

eq_binary = re.compile(
    rf"(?<![\w.,/^×÷+−\-*(|])(?<![×÷+−\-]\s)({NUM})\s*([×÷+−])\s*({NUM})\s*=\s*(−?(?:{NUM}))(?![\d,]*\s*[×÷+−/\w%])(?!\.\d)")
eq_power = re.compile(rf"(?<![\w.,×+−÷(])(?<![×÷+−\-]\s)({NUM})([²³])\s*=\s*(−?(?:{NUM}))(?![\d,]*\s*[×÷+−/\w%])(?!\.\d)")
eq_pct = re.compile(rf"(?<![\w.])({NUM})%\s+of\s+(?:₹)?({NUM})\s*=\s*(?:₹)?({NUM})(?![\d,%]|\s*[(%×+])")
eq_sqrt = re.compile(rf"([√∛])({NUM})\s*=\s*({NUM})(?![\d,.])")
chain = re.compile(rf"(?<![\w.,×÷(])((?:{NUM})(?:\s*[+−]\s*(?:{NUM})){{2,}})\s*=\s*(−?(?:{NUM}))(?![\d,]*\s*[×÷+−/\w%])")


def val(s: str) -> Fraction:
    s = s.replace(",", "").replace("−", "-")
    return Fraction(s)


def check_text(text: str, where: str, errors: list, counts: dict):
    for m in eq_binary.finditer(text):
        a, op, b, c = m.groups()
        A, B, C = val(a), val(b), val(c)
        if op == "÷" and B == 0:
            continue
        r = {"×": A * B, "÷": A / B if B else None, "+": A + B, "−": A - B}[op]
        counts["inline"] += 1
        if r != C:
            errors.append(f"{where}: {m.group(0)!r} → expected {float(r):g}")
    for m in eq_power.finditer(text):
        a, p, c = m.groups()
        counts["inline"] += 1
        if val(a) ** SUP[p] != val(c):
            errors.append(f"{where}: {m.group(0)!r} → expected {val(a) ** SUP[p]}")
    for m in eq_pct.finditer(text):
        p, b, c = m.groups()
        counts["inline"] += 1
        if val(p) * val(b) / 100 != val(c):
            errors.append(f"{where}: {m.group(0)!r} → expected {float(val(p) * val(b) / 100):g}")
    for m in eq_sqrt.finditer(text):
        s, a, c = m.groups()
        counts["inline"] += 1
        k = 2 if s == "√" else 3
        if val(c) ** k != val(a):
            errors.append(f"{where}: {m.group(0)!r} → {c}^{k} != {a}")
    for m in chain.finditer(text):
        expr, c = m.groups()
        toks = re.findall(rf"{NUM}|[+−]", expr)
        total = val(toks[0])
        for op, n in zip(toks[1::2], toks[2::2]):
            total = total + val(n) if op == "+" else total - val(n)
        counts["inline"] += 1
        if total != val(c):
            errors.append(f"{where}: {m.group(0)!r} → expected {float(total):g}")


PURE = re.compile(r"^[\d,.\s+−×÷()\-]+$")


def eval_pure(expr: str):
    e = expr.replace(",", "").replace("−", "-").replace("×", "*").replace("÷", "/")
    e = re.sub(r"(\d+(?:\.\d+)?)", r"Fraction('\1')", e)
    return eval(e, {"Fraction": Fraction})


def check_tables(md: str, where: str, errors: list, counts: dict):
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(split_row(lines[i]))
                i += 1
            header = [h.lower() for h in block[0]]
            if "problem" in header and ("answer" in header[-1]):
                pi = header.index("problem")
                for row in block[2:]:
                    if len(row) != len(header):
                        continue
                    prob, ans = row[pi], row[-1].replace("**", "")
                    if PURE.match(prob) and re.fullmatch(rf"−?(?:{NUM})", ans):
                        counts["table"] += 1
                        got = eval_pure(prob)
                        if got != val(ans):
                            errors.append(f"{where}: table row {row[0]} '{prob}' = {ans}, expected {float(got):g}")
            continue
        i += 1


def check_generators(errors: list, counts: dict, per_topic=200):
    from booklib.questions import GENERATORS, make
    for key in GENERATORS:
        for s in range(per_topic):
            q = make(key, random.Random(f"verify|{key}|{s}"))
            counts["generated"] += 1
            if not eval(q.check, {"math": math, "Fraction": Fraction, "date": date}):
                errors.append(f"generator {key}: {q.text} → {q.answer}")
                break


def main():
    errors, counts = [], {"inline": 0, "table": 0, "generated": 0}
    for path in sorted((ROOT / "content").rglob("*.md")):
        md = path.read_text(encoding="utf-8")
        for n, line in enumerate(md.splitlines(), 1):
            check_text(line.replace("**", ""), f"{path.name}:{n}", errors, counts)
        check_tables(md, path.name, errors, counts)
    check_generators(errors, counts)
    print(f"Checked {counts['inline']} inline equations, {counts['table']} table rows, {counts['generated']} generated questions.")
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  ✗", e)
        sys.exit(1)
    print("✓ All checks passed.")


if __name__ == "__main__":
    main()
