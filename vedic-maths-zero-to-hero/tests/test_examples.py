"""Checks on hand-written worked examples in content/*.md."""
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_examples as VE  # noqa: E402

CONTENT = sorted((ROOT / "content").rglob("*.md"))


def tables(md):
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(VE.split_row(lines[i]))
                i += 1
            yield block
        else:
            i += 1


def n(s):
    return int(re.sub(r"[^\d−-]", "", s.split("→")[0]).replace("−", "-"))


def test_inline_and_table_arithmetic():
    errors, counts = [], {"inline": 0, "table": 0, "generated": 0}
    for p in CONTENT:
        md = p.read_text(encoding="utf-8")
        for k, line in enumerate(md.splitlines(), 1):
            VE.check_text(line.replace("**", ""), f"{p.name}:{k}", errors, counts)
        VE.check_tables(md, p.name, errors, counts)
    assert not errors, "\n".join(errors)
    assert counts["inline"] > 150 and counts["table"] > 100


def test_urdhva_two_digit_step_columns():
    """Tables with Right (v) | Cross (x) | Left (v) columns."""
    checked = 0
    for p in CONTENT:
        for block in tables(p.read_text(encoding="utf-8")):
            h = [c.lower() for c in block[0]]
            if not any("cross" in c for c in h):
                continue
            for row in block[2:]:
                a, b = [int(x) for x in re.findall(r"\d+", row[1])[:2]]
                da, db = divmod(a, 10), divmod(b, 10)
                right = da[1] * db[1]
                cross = da[0] * db[1] + da[1] * db[0]
                left = da[0] * db[0]
                assert n(row[2]) == right, row
                assert int(row[3].split("=")[-1]) == cross, row
                assert n(row[4]) == left, row
                assert left * 100 + cross * 10 + right == a * b
                checked += 1
    assert checked >= 8


def test_urdhva_three_digit_step_values():
    checked = 0
    for p in CONTENT:
        for block in tables(p.read_text(encoding="utf-8")):
            h = [c.lower() for c in block[0]]
            if not any("step values" in c for c in h):
                continue
            for row in block[2:]:
                a, b = [int(x) for x in re.findall(r"\d+", row[1])[:2]]
                x, y = [int(c) for c in str(a)], [int(c) for c in str(b)]
                expected = [x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[0] * y[2] + x[1] * y[1] + x[2] * y[0],
                            x[1] * y[2] + x[2] * y[1], x[2] * y[2]]
                got = [int(v) for v in row[2].split(",")]
                assert got == expected, (row, expected)
                checked += 1
    assert checked >= 3


def test_nikhilam_tables():
    """Rows with Left and Right columns must reproduce the product."""
    checked = 0
    for p in CONTENT:
        for block in tables(p.read_text(encoding="utf-8")):
            h = [c.lower() for c in block[0]]
            if "left" not in h or "right" not in h or "deviations" not in h:
                continue
            for row in block[2:]:
                a, b = [int(x.replace(",", "")) for x in re.findall(r"[\d,]+", row[1].replace(" ", ""))[:2]]
                ans = int(row[-1].replace(",", ""))
                assert a * b == ans, row
                checked += 1
    assert checked >= 9


def test_sutra_equation_examples():
    """Equation examples from Part II, substituted exactly."""
    F = Fraction
    x = F(-13, 3)
    assert 1 / ((x + 2) * (x + 3)) + 1 / ((x + 2) * (x + 4)) == 1 / ((x + 2) * (x + 5)) + 1 / ((x + 3) * (x + 4))
    x = F(5)
    assert 1 / (x - 4) + 1 / (x - 6) == 1 / (x - 2) + 1 / (x - 8)
    x = F(-2)
    assert (2 * x + 3) / (2 * x + 5) == (2 * x + 5) / (2 * x + 3)
    assert 3 * 0 + 7 * F(2, 7) == 2 and 4 * 0 + 14 * F(2, 7) == 4
    assert 45 * 2 - 23 * (-1) == 113 and 23 * 2 - 45 * (-1) == 91
    assert all(t ** 3 + 6 * t * t + 11 * t + 6 == 0 for t in (-1, -2, -3))
    assert all(2 * t * t + 3 * t - 9 == 0 for t in (F(3, 2), -3))
    assert (7 * 9) == (3 * 21)


def test_recurring_decimals_text():
    from booklib import vedic as V
    assert V.recurring_1_over_x9(19)[0] == "052631578947368421"
    assert V.shesanyankena(7)[0] == "142857" and V.shesanyankena(13)[0] == "076923"
    assert int("052631578") + int("947368421") == 999999999
