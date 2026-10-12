"""Vedic algorithms checked against ordinary Python arithmetic."""
import math
import random
import sys
from datetime import date
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from booklib import tables, vedic as V  # noqa: E402
from booklib.questions import GENERATORS, make  # noqa: E402


def test_fmt_indian():
    assert V.fmt(1234567) == "12,34,567"
    assert V.fmt(100000) == "1,00,000"
    assert V.fmt(999) == "999"
    assert V.fmt(-45061) == "\u221245,061"
    assert V.fmt_intl(1234567) == "1,234,567"


def test_nikhilam_multiply():
    for base in (10, 100, 1000):
        for a in range(base - 15, base + 16):
            for b in range(base - 15, base + 16, 3):
                if a > 0 and b > 0:
                    assert V.nikhilam_multiply(a, b, base)[0] == a * b
    for base in (50, 200, 300, 500):
        for a in range(base - 9, base + 10):
            assert V.nikhilam_multiply(a, base + 7, base)[0] == a * (base + 7)


def test_urdhva_multiply():
    r = random.Random(1)
    for _ in range(3000):
        a, b = r.randint(1, 99999), r.randint(1, 99999)
        assert V.urdhva_multiply(a, b)[0] == a * b


def test_squares():
    for n in range(5, 2000, 10):
        assert V.square_ending_5(n)[0] == n * n
    for n in range(1, 3000):
        assert V.duplex_square(n)[0] == n * n
    for n in range(85, 116):
        assert V.yavadunam_square(n, 100)[0] == n * n
    for n in range(950, 1051):
        assert V.yavadunam_square(n, 1000)[0] == n * n
    for n in range(40, 61):
        assert V.square_near_50(n)[0] == n * n


def test_special_products():
    for p in range(1, 30):
        for u in range(1, 10):
            a, b = 10 * p + u, 10 * p + 10 - u
            assert V.same_prefix_units_ten(a, b)[0] == a * b
    for n in range(1, 100000, 37):
        assert V.times_11(n)[0] == 11 * n
    for k in (1, 2, 3, 4):
        for n in range(1, 10 ** k, max(1, 10 ** k // 300)):
            assert V.ekanyunena(n, k)[0] == n * (10 ** k - 1)


def test_divisions():
    for n in range(1, 50000, 7):
        assert V.nikhilam_divide_by_9(n)[0] == divmod(n, 9)
    for d in (7, 8, 9, 88, 89, 97, 98, 996, 997, 998, 9988):
        for n in range(d, 200 * d, max(1, d // 3)):
            assert V.nikhilam_divide(n, d)[0] == divmod(n, d), (n, d)
    for d in (11, 12, 13, 14, 111, 112, 113, 121, 1012, 1123):
        for n in range(d, 300 * d, max(1, d // 4)):
            assert V.paravartya_divide(n, d)[0] == divmod(n, d), (n, d)


def test_recurring_and_vinculum():
    for den in (19, 29, 39, 49, 59, 69, 79, 89, 99):
        s, _ = V.recurring_1_over_x9(den)
        assert Fraction(int(s), 10 ** len(s) - 1) == Fraction(1, den)
    for den in (7, 13, 17, 23):
        s, _ = V.shesanyankena(den)
        assert Fraction(int(s), 10 ** len(s) - 1) == Fraction(1, den)
    for n in range(1, 20000):
        assert V.vinculum_value(n) == n


def test_digital_root():
    for n in range(1, 10000):
        assert V.digit_sum_root(n) == (9 if n % 9 == 0 else n % 9)


def test_reference_tables():
    for row in tables.squares("1", "50", "5")[1:]:
        for i in range(0, len(row), 2):
            if row[i]:
                assert int(row[i + 1].replace(",", "")) == int(row[i]) ** 2
    for row in tables.cubes("1", "30", "3")[1:]:
        for i in range(0, len(row), 2):
            if row[i]:
                assert int(row[i + 1].replace(",", "")) == int(row[i]) ** 3
    for row in tables.divisibility()[1:]:
        d = int(row[0])
        num = int(row[2].split()[0].replace(",", ""))
        assert num % d == 0, row
    t = tables.times("2", "10", "10")
    for r in t[1:]:
        for j, v in enumerate(r[1:]):
            assert int(v) == int(r[0]) * int(t[0][j + 1])


def test_every_generator_independently():
    total = 0
    for key in GENERATORS:
        for s in range(300):
            q = make(key, random.Random(f"pytest|{key}|{s}"))
            assert eval(q.check, {"math": math, "Fraction": Fraction, "date": date}), (key, q.text, q.answer)
            assert q.answer.strip(), key
            total += 1
    assert total >= 90 * 300


def test_book_has_enough_original_questions():
    import json
    rep = ROOT / "output" / "build_report.json"
    if not rep.exists():
        return
    data = json.loads(rep.read_text())
    if "book" in data:
        assert data["book"]["questions"] >= 500
