"""Reference tables computed in code (never typed by hand)."""
from __future__ import annotations

import math
from fractions import Fraction

from .vedic import fmt


def squares(start="1", end="50", cols="5"):
    a, b, c = int(start), int(end), int(cols)
    nums = list(range(a, b + 1))
    per = math.ceil(len(nums) / c)
    rows = [["n", "n²"] * c]
    for r in range(per):
        row = []
        for k in range(c):
            i = r + k * per
            row += [str(nums[i]), fmt(nums[i] ** 2)] if i < len(nums) else ["", ""]
        rows.append(row)
    return rows


def cubes(start="1", end="30", cols="3"):
    a, b, c = int(start), int(end), int(cols)
    nums = list(range(a, b + 1))
    per = math.ceil(len(nums) / c)
    rows = [["n", "n³"] * c]
    for r in range(per):
        row = []
        for k in range(c):
            i = r + k * per
            row += [str(nums[i]), fmt(nums[i] ** 3)] if i < len(nums) else ["", ""]
        rows.append(row)
    return rows


def times(start="2", end="10", upto="10"):
    a, b, n = int(start), int(end), int(upto)
    rows = [["×"] + [str(k) for k in range(a, b + 1)]]
    for i in range(1, n + 1):
        rows.append([str(i)] + [str(i * k) for k in range(a, b + 1)])
    return rows


def fraction_percent():
    fr = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5), (1, 6), (5, 6), (1, 7), (1, 8), (3, 8), (5, 8), (7, 8),
          (1, 9), (1, 10), (1, 11), (1, 12), (1, 15), (1, 16), (1, 20), (1, 25), (1, 40), (1, 50)]
    rows = [["Fraction", "Percentage", "Decimal"]]
    for n, d in fr:
        p = Fraction(n * 100, d)
        if p.denominator == 1:
            ps = f"{p.numerator}%"
        else:
            w, r = divmod(p.numerator, p.denominator)
            ps = f"{w} {r}/{p.denominator}%"
        dec = n / d
        dec_s = f"{dec:.4f}".rstrip("0").rstrip(".")
        if d in (3, 6, 7, 9, 11, 12, 15):
            dec_s += "… (recurring)"
        rows.append([f"{n}/{d}", ps, dec_s])
    return rows


def powers2():
    rows = [["n", "2ⁿ", "3ⁿ", "5ⁿ"]]
    for n in range(1, 13):
        rows.append([str(n), fmt(2 ** n), fmt(3 ** n) if n <= 10 else "", fmt(5 ** n) if n <= 8 else ""])
    return rows


def cyclicity():
    rows = [["Unit digit", "Last digits of powers 1, 2, 3, 4 …", "Cycle length"]]
    for b in range(10):
        cyc, x = [], b
        while x not in cyc:
            cyc.append(x)
            x = (x * b) % 10
        rows.append([str(b), ", ".join(map(str, cyc)), str(len(cyc))])
    return rows


def roots_endings():
    rows = [["Number ends in", "Square ends in", "Cube ends in"]]
    for d in range(10):
        rows.append([str(d), str(d * d % 10), str(d ** 3 % 10)])
    return rows


def primes(limit="100"):
    n = int(limit)
    ps = [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    rows = [["Primes up to " + str(n)] + [""] * 9]
    for i in range(0, len(ps), 10):
        chunk = [str(p) for p in ps[i:i + 10]]
        rows.append(chunk + [""] * (10 - len(chunk)))
    return rows


def divisibility():
    return [["Divisor", "Rule", "Example"],
            ["2", "Last digit even (0, 2, 4, 6, 8)", "3,574 ✓"],
            ["3", "Digit sum divisible by 3", "4,512 → 12 ✓"],
            ["4", "Last two digits divisible by 4", "7,316 → 16 ✓"],
            ["5", "Last digit 0 or 5", "8,435 ✓"],
            ["6", "Divisible by 2 and by 3", "2,154 ✓"],
            ["7", "Double the last digit, subtract from the rest; repeat", "203 → 20 − 6 = 14 ✓"],
            ["8", "Last three digits divisible by 8", "51,128 → 128 ✓"],
            ["9", "Digit sum divisible by 9", "6,723 → 18 ✓"],
            ["10", "Last digit 0", "4,560 ✓"],
            ["11", "Alternating digit sum divisible by 11", "9,537 → (9+3) − (5+7) = 0 ✓"],
            ["12", "Divisible by 3 and by 4", "1,524 ✓"],
            ["13", "Add 4 × last digit to the rest; repeat", "247 → 24 + 28 = 52 ✓"],
            ["25", "Last two digits 00, 25, 50, 75", "3,475 ✓"]]


def multiples(n="7", upto="20"):
    n, u = int(n), int(upto)
    rows = [[f"{n} ×", "="] * 4]
    per = math.ceil(u / 4)
    for r in range(per):
        row = []
        for k in range(4):
            i = r + k * per + 1
            row += [str(i), fmt(n * i)] if i <= u else ["", ""]
        rows.append(row)
    return rows


REG = {k: v for k, v in globals().items() if callable(v) and not k.startswith("_") and k not in ("fmt", "Fraction")}


def build(name, *args):
    return REG[name](*args)
