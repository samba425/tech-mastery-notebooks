"""Original practice-question generators.

Each generator takes a seeded random.Random and returns a Question.
- answer:   the string printed in the answer key
- solution: worked steps
- check:    a Python expression evaluated independently by the tests; it must
            evaluate to True. It is written from first principles (plain
            arithmetic), not by re-using the generator's own algorithm.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from datetime import date
from fractions import Fraction

from . import vedic as V
from .vedic import MINUS, fmt

M = MINUS


@dataclass
class Question:
    topic: str
    text: str
    answer: str
    solution: str = ""
    check: str = "True"
    exact: bool = True
    level: str = "beginner"
    tags: list = field(default_factory=list)


GENERATORS: dict[str, tuple] = {}


def gen(key: str, level: str, title: str):
    def wrap(fn):
        GENERATORS[key] = (fn, level, title)
        return fn
    return wrap


def make(topic_key: str, rng: random.Random) -> Question:
    fn, level, _ = GENERATORS[topic_key]
    q = fn(rng)
    q.topic = topic_key
    q.level = level
    return q


def Q(text, answer, solution="", check="True", exact=True):
    return Question("", text, str(answer), solution, check, exact)


def frac_str(f: Fraction) -> str:
    f = Fraction(f)
    if f.denominator == 1:
        return fmt(f.numerator)
    whole = abs(f.numerator) // f.denominator
    if whole and abs(f.numerator) > f.denominator:
        rem = abs(f.numerator) % f.denominator
        sign = M if f < 0 else ""
        return f"{sign}{whole} {rem}/{f.denominator}"
    return fmt(f)


def money(x) -> str:
    x = Fraction(x)
    if x.denominator == 1:
        return "₹" + fmt(x.numerator)
    return "₹" + fmt(float(round(x, 2)))


# ============================================================ PART I foundations

@gen("place_value", "beginner", "Place value (Indian system)")
def _(r):
    n = r.randint(10 ** 6, 10 ** 8 - 1)
    s = str(n)
    names = ["units", "tens", "hundreds", "thousands", "ten thousands", "lakhs", "ten lakhs", "crores"]
    pos = r.randint(1, len(s) - 1)
    digit = int(s[-1 - pos])
    if digit == 0:
        pos = 0
        digit = int(s[-1])
    val = digit * 10 ** pos
    return Q(f"In {fmt(n)}, what is the place value of the digit in the {names[pos]} place?",
             fmt(val), f"The digit is {digit}; {names[pos]} = {fmt(10 ** pos)}; {digit} × {fmt(10 ** pos)} = {fmt(val)}.",
             f"int(str({n})[-1-{pos}]) * 10**{pos} == {val}")


@gen("indian_to_intl", "beginner", "Indian ↔ international commas")
def _(r):
    n = r.randint(10 ** 6, 10 ** 9 - 1)
    return Q(f"Rewrite {fmt(n)} using international commas (millions).", V.fmt_intl(n),
             "International grouping uses threes from the right: thousand, million, billion.",
             f"int('{V.fmt_intl(n)}'.replace(',', '')) == {n}")


@gen("prime_check", "beginner", "Prime or composite?")
def _(r):
    n = r.choice([n for n in range(51, 400) if n % 2 and n % 5])
    is_p = all(n % p for p in range(2, int(n ** 0.5) + 1))
    lim = int(n ** 0.5)
    if is_p:
        sol = f"√{n} ≈ {lim}. No prime up to {lim} divides {n}, so it is prime."
    else:
        p = next(p for p in range(2, lim + 1) if n % p == 0)
        sol = f"{n} = {p} × {n // p}, so it is composite."
    return Q(f"Is {n} prime or composite?", "Prime" if is_p else "Composite", sol,
             f"(all({n} % k for k in range(2, {n}))) == {is_p}")


@gen("divisibility", "beginner", "Divisibility tests")
def _(r):
    d = r.choice([3, 4, 6, 8, 9, 11])
    n = r.randint(1000, 99999)
    if r.random() < 0.5:
        n -= n % d
    rule = {3: "digit sum divisible by 3", 4: "last two digits divisible by 4", 6: "divisible by both 2 and 3",
            8: "last three digits divisible by 8", 9: "digit sum divisible by 9",
            11: "(sum of odd-place digits − sum of even-place digits) divisible by 11"}[d]
    yes = n % d == 0
    return Q(f"Is {fmt(n)} divisible by {d}? Use the divisibility rule.", "Yes" if yes else "No",
             f"Rule for {d}: {rule}. {fmt(n)} ÷ {d} leaves remainder {n % d}.", f"({n} % {d} == 0) == {yes}")


@gen("integers", "beginner", "Positive and negative numbers")
def _(r):
    a, b, c = r.randint(-30, 30), r.randint(-30, 30), r.randint(-30, 30)
    res = a - b + c
    t = lambda x: f"({fmt(x)})" if x < 0 else str(x)
    return Q(f"Calculate {t(a)} {M} {t(b)} + {t(c)}.", fmt(res),
             f"Subtracting {t(b)} is the same as adding {fmt(-b)}. {fmt(a)} + {fmt(-b)} + {fmt(c)} = {fmt(res)}.",
             f"{a} - ({b}) + ({c}) == {res}")


@gen("factors", "beginner", "Factors and multiples")
def _(r):
    n = r.choice([24, 36, 48, 60, 72, 84, 90, 96, 100, 120, 144, 180])
    fs = [k for k in range(1, n + 1) if n % k == 0]
    return Q(f"How many factors does {n} have? List them.", f"{len(fs)}: {', '.join(map(str, fs))}",
             "Pair factors from the outside in: " + ", ".join(f"{k}×{n // k}" for k in fs if k * k <= n) + ".",
             f"len([k for k in range(1, {n}+1) if {n} % k == 0]) == {len(fs)}")


# ============================================================ PART II/III arithmetic

@gen("add_ltr", "beginner", "Left-to-right addition")
def _(r):
    a, b = r.randint(100, 999), r.randint(100, 999)
    h = (a // 100 + b // 100) * 100
    t = (a // 10 % 10 + b // 10 % 10) * 10
    u = a % 10 + b % 10
    return Q(f"Add mentally from left to right: {a} + {b}", fmt(a + b),
             f"Hundreds {h}, tens {t}, units {u}: {h} + {t} + {u} = {a + b}.", f"{a}+{b} == {a + b}")


@gen("add_comp", "beginner", "Adding 9, 99, 199 … by compensation")
def _(r):
    a = r.randint(120, 9800)
    b = r.choice([9, 19, 29, 39, 99, 199, 299, 999, 98, 197])
    up = -b % 10 if b % 100 not in (99, 98, 97) else (100 - b % 100)
    rounded = b + up
    return Q(f"{fmt(a)} + {b}", fmt(a + b),
             f"{b} = {rounded} {M} {up}. {fmt(a)} + {rounded} = {fmt(a + rounded)}, then {M} {up} = {fmt(a + b)}.",
             f"{a}+{b} == {a + b}")


@gen("sub_power10", "beginner", "Subtracting from 100, 1000, 10000 (All from 9, last from 10)")
def _(r):
    k = r.choice([2, 3, 4, 5])
    n = r.randint(10 ** (k - 1) + 1, 10 ** k - 1)
    while n % 10 == 0:
        n += 1
    res = 10 ** k - n
    ds = str(n).zfill(k)
    work = " ".join(f"9−{c}={9 - int(c)}" for c in ds[:-1]) + f", 10−{ds[-1]}={10 - int(ds[-1])}"
    return Q(f"{fmt(10 ** k)} {M} {fmt(n)}", fmt(res), f"All from 9, last from 10: {work} → {str(res).zfill(k)}.",
             f"10**{k} - {n} == {res}")


@gen("sub_comp", "beginner", "Subtraction by compensation")
def _(r):
    a = r.randint(500, 9999)
    b = r.randint(100, a - 50)
    b = b - b % 10 + r.choice([7, 8, 9])
    up = 10 - b % 10
    return Q(f"{fmt(a)} {M} {fmt(b)}", fmt(a - b),
             f"Subtract {fmt(b + up)} instead: {fmt(a)} {M} {fmt(b + up)} = {fmt(a - b - up)}; add back {up} → {fmt(a - b)}.",
             f"{a}-{b} == {a - b}")


@gen("add_column", "intermediate", "Adding a column of numbers")
def _(r):
    nums = [r.randint(100, 9999) for _ in range(r.randint(4, 6))]
    s = sum(nums)
    return Q("Add: " + " + ".join(fmt(x) for x in nums), fmt(s),
             f"Group friendly pairs, or add column-wise with running totals. Digit-sum check: digital roots give {V.digit_sum_root(s)}.",
             f"sum({nums}) == {s}")


@gen("estimate_product", "intermediate", "Estimating a product (approximate)")
def _(r):
    a, b = r.randint(21, 98), r.randint(210, 980)
    ra, rb = round(a, -1), round(b, -1 if b < 500 else -2)
    est = ra * rb
    return Q(f"Estimate {a} × {b} by rounding (approximate answer).", f"≈ {fmt(est)} (exact {fmt(a * b)})",
             f"{a} ≈ {ra}, {b} ≈ {rb}; {ra} × {rb} = {fmt(est)}. This is an estimate, not the exact product.",
             f"abs({est} - {a}*{b}) / ({a}*{b}) < 0.25", exact=False)


# ============================================================ fractions / percentages

@gen("simplify_fraction", "beginner", "Simplifying fractions")
def _(r):
    g = r.randint(2, 12)
    n, d = r.randint(1, 15), r.randint(2, 19)
    while math.gcd(n, d) != 1 or n == d:
        n, d = r.randint(1, 15), r.randint(2, 19)
    N, D = n * g, d * g
    hcf = math.gcd(N, D)
    return Q(f"Simplify {N}/{D}.", f"{n}/{d}", f"HCF of {N} and {D} is {hcf}. Divide both by {hcf}.",
             f"Fraction({N},{D}) == Fraction({n},{d})")


@gen("add_fractions", "intermediate", "Adding and subtracting fractions")
def _(r):
    a, b = Fraction(r.randint(1, 9), r.randint(2, 12)), Fraction(r.randint(1, 9), r.randint(2, 12))
    op = r.choice(["+", M])
    res = a + b if op == "+" else a - b
    lcm = a.denominator * b.denominator // math.gcd(a.denominator, b.denominator)
    return Q(f"{a} {op} {b}", frac_str(res),
             f"LCM of denominators = {lcm}. Convert, then {'add' if op == '+' else 'subtract'} numerators and simplify: {fmt(res)}.",
             f"Fraction('{a}') {'+' if op == '+' else '-'} Fraction('{b}') == Fraction({res.numerator},{res.denominator})")


@gen("frac_to_pct", "beginner", "Fraction → percentage")
def _(r):
    f = r.choice([Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(1, 4), Fraction(3, 4), Fraction(1, 5), Fraction(2, 5),
                  Fraction(1, 6), Fraction(5, 6), Fraction(1, 8), Fraction(3, 8), Fraction(5, 8), Fraction(7, 8), Fraction(1, 9),
                  Fraction(1, 11), Fraction(1, 12), Fraction(1, 16), Fraction(1, 20), Fraction(1, 25), Fraction(1, 7)])
    p = f * 100
    ps = frac_str(p) + "%"
    return Q(f"Write {f} as a percentage.", ps, f"{f} × 100 = {frac_str(p)}%.", f"Fraction('{f}')*100 == Fraction({p.numerator},{p.denominator})")


@gen("pct_of", "beginner", "Percentage of a quantity")
def _(r):
    p = r.choice([5, 10, 12.5, 15, 20, 25, 30, 35, 40, 45, 60, 75, 120, 150])
    base = r.choice([40, 80, 120, 160, 240, 320, 480, 640, 800, 1200, 2400, 3600, 4800, 7200])
    res = Fraction(str(p)) * base / 100
    return Q(f"Find {p}% of {fmt(base)}.", frac_str(res),
             f"Split {p}% into easy parts (10%, 5%, 1% …) or use fractions: {p}% = {Fraction(str(p)) / 100}. Result {frac_str(res)}.",
             f"Fraction('{p}')*{base}/100 == Fraction({res.numerator},{res.denominator})")


@gen("pct_change", "intermediate", "Percentage increase or decrease")
def _(r):
    old = r.choice([200, 250, 400, 500, 800, 1250, 1600, 2000, 2500, 4000])
    p = r.choice([q for q in [5, 8, 10, 12, 15, 20, 25, 30, 40] if old * q % 100 == 0])
    up = r.random() < 0.5
    new = old * (100 + p) // 100 if up else old * (100 - p) // 100
    return Q(f"A price changes from ₹{fmt(old)} to ₹{fmt(new)}. Find the percentage {'increase' if up else 'decrease'}.",
             f"{p}%", f"Change = {fmt(abs(new - old))}. % change = change ÷ original × 100 = {abs(new - old)}/{old} × 100 = {p}%.",
             f"abs({new}-{old})*100 == {p}*{old}")


@gen("decimal_mult", "intermediate", "Multiplying decimals")
def _(r):
    ia, ib = r.randint(11, 99), r.randint(11, 99)
    pb = r.choice([1, 2])
    while ia % 10 == 0:
        ia += 1
    while ib % 10 == 0:
        ib += 1
    sa, sb = f"{ia / 10:.1f}", f"{ib / 10 ** pb:.{pb}f}"
    res = Fraction(ia * ib, 10 ** (1 + pb))
    sr = f"{float(res):.{1 + pb}f}".rstrip("0").rstrip(".")
    return Q(f"{sa} × {sb}", sr,
             f"Multiply without points: {ia} × {ib} = {ia * ib}. Decimal places: 1 + {pb} = {1 + pb}, so the answer is {sr}.",
             f"Fraction('{sa}')*Fraction('{sb}') == Fraction('{sr}')")


# ============================================================ powers / roots / numbers

@gen("square", "beginner", "Squares")
def _(r):
    n = r.randint(11, 60)
    return Q(f"{n}²", fmt(n * n), f"{n} × {n} = {n * n}.", f"{n}**2 == {n * n}")


@gen("cube", "intermediate", "Cubes")
def _(r):
    n = r.randint(2, 25)
    return Q(f"{n}³", fmt(n ** 3), f"{n} × {n} × {n} = {fmt(n ** 3)}.", f"{n}**3 == {n ** 3}")


@gen("sqrt_perfect", "intermediate", "Square roots of perfect squares")
def _(r):
    n = r.randint(21, 99)
    sq = n * n
    last = sq % 10
    cand = {0: "0", 1: "1 or 9", 4: "2 or 8", 5: "5", 6: "4 or 6", 9: "3 or 7"}[last]
    lead = sq // 100
    t = int(math.isqrt(lead))
    return Q(f"√{fmt(sq)}", str(n),
             f"Last digit {last} → root ends in {cand}. Leading part {lead} lies between {t}² and {t + 1}², so tens digit is {t}. Check {t}5² = {(10 * t + 5) ** 2} to choose → {n}.",
             f"{n}*{n} == {sq}")


@gen("cbrt_perfect", "intermediate", "Cube roots of perfect cubes")
def _(r):
    n = r.randint(11, 99)
    c = n ** 3
    lead = c // 1000
    t = round(lead ** (1 / 3))
    while t ** 3 > lead:
        t -= 1
    while (t + 1) ** 3 <= lead:
        t += 1
    u = n % 10
    return Q(f"∛{fmt(c)}", str(n),
             f"Last digit {c % 10} → cube root ends in {u} (cube endings: 1→1, 8→2, 7→3, 4→4, 5→5, 6→6, 3→7, 2→8, 9→9). Thousands part {fmt(lead)} lies between {t}³ and {t + 1}³ → tens digit {t}.",
             f"{n}**3 == {c}")


@gen("lcm_hcf", "intermediate", "HCF and LCM")
def _(r):
    g = r.randint(2, 15)
    a, b = g * r.randint(2, 12), g * r.randint(2, 12)
    while a == b:
        b = g * r.randint(2, 12)
    h, l = math.gcd(a, b), a * b // math.gcd(a, b)
    return Q(f"Find the HCF and LCM of {a} and {b}.", f"HCF {h}, LCM {l}", f"HCF × LCM = product: {h} × {l} = {a * b} = {a} × {b}.",
             f"math.gcd({a},{b}) == {h} and {a}*{b}//math.gcd({a},{b}) == {l}")


@gen("prime_factorise", "intermediate", "Prime factorisation")
def _(r):
    n = r.choice([84, 90, 126, 180, 210, 252, 360, 420, 504, 630, 720, 924, 1001, 1260, 1716, 2310])
    f, m, p = {}, n, 2
    while m > 1:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1
    sup = {1: "", 2: "²", 3: "³", 4: "⁴", 5: "⁵"}
    s = " × ".join(f"{p}{sup[e]}" for p, e in f.items())
    prod = " * ".join(f"{p}**{e}" for p, e in f.items())
    return Q(f"Write {fmt(n)} as a product of primes.", s, "Divide repeatedly by the smallest prime that works (factor tree).", f"{prod} == {n}")


@gen("exponents", "intermediate", "Laws of exponents")
def _(r):
    b = r.choice([2, 3, 5, 10])
    m, n = r.randint(2, 6), r.randint(1, 5)
    kind = r.choice(["mul", "div", "pow", "neg"])
    if kind == "mul":
        return Q(f"{b}^{{{m}}} × {b}^{{{n}}} (give the value)", fmt(b ** (m + n)), f"Add exponents: {b}^{{{m + n}}} = {fmt(b ** (m + n))}.", f"{b}**{m}*{b}**{n} == {b ** (m + n)}")
    if kind == "div":
        m += n
        return Q(f"{b}^{{{m}}} ÷ {b}^{{{n}}}", fmt(b ** (m - n)), f"Subtract exponents: {b}^{{{m - n}}}.", f"{b}**{m}//{b}**{n} == {b ** (m - n)}")
    if kind == "pow":
        m, n = r.randint(1, 3), r.randint(2, 3)
        return Q(f"({b}^{{{m}}})^{{{n}}}", fmt(b ** (m * n)), f"Multiply exponents: {b}^{{{m * n}}}.", f"({b}**{m})**{n} == {b ** (m * n)}")
    v = Fraction(1, b ** n)
    return Q(f"{b}^{{{M}{n}}} as a fraction", f"1/{fmt(b ** n)}", f"A negative exponent means reciprocal: 1/{b}^{{{n}}}.", f"Fraction(1, {b}**{n}) == Fraction({v.numerator},{v.denominator})")


@gen("remainder", "intermediate", "Remainders")
def _(r):
    d = r.choice([7, 9, 11, 13])
    n = r.randint(1000, 99999)
    return Q(f"Find the remainder when {fmt(n)} is divided by {d}.", str(n % d),
             f"{fmt(n)} = {d} × {fmt(n // d)} + {n % d}." + (" Shortcut: digit sum mod 9." if d == 9 else ""), f"{n} % {d} == {n % d}")


@gen("sqrt_estimate", "advanced", "Estimating square roots (approximate)")
def _(r):
    n = r.choice([k for k in range(20, 400) if math.isqrt(k) ** 2 != k])
    s = math.isqrt(n)
    near = s if n - s * s < (s + 1) ** 2 - n else s + 1
    est = near + (n - near * near) / (2 * near)
    return Q(f"Estimate √{n} to 2 decimal places (approximate).", f"≈ {est:.2f} (true value {math.sqrt(n):.3f})",
             f"Nearest perfect square {near * near} = {near}². √n ≈ {near} + ({n} {M} {near * near}) ÷ (2 × {near}) = {est:.3f}.",
             f"abs({est} - {n}**0.5) < 0.06", exact=False)


# ============================================================ multiplication (Part IV)

@gen("mult_11", "beginner", "Multiplying by 11")
def _(r):
    n = r.randint(12, 9999)
    res, steps = V.times_11(n)
    return Q(f"{fmt(n)} × 11", fmt(res), " ".join(steps), f"{n}*11 == {res}")


@gen("mult_5_25", "beginner", "Multiplying by 5, 25, 50, 125")
def _(r):
    k = r.choice([5, 25, 50, 125])
    n = r.randint(12, 999)
    rule = {5: "× 10 ÷ 2", 25: "× 100 ÷ 4", 50: "× 100 ÷ 2", 125: "× 1000 ÷ 8"}[k]
    return Q(f"{n} × {k}", fmt(n * k), f"{k} = {rule.replace('×', '').replace('÷', '/')} → {n} {rule} = {fmt(n * k)}.", f"{n}*{k} == {n * k}")


@gen("mult_9s", "beginner", "Multiplying by 9, 99, 999 (Ekanyunena Purvena)")
def _(r):
    nines = r.choice([2, 2, 3, 3, 4])
    n = r.randint(10 ** (nines - 1), 10 ** nines - 1)
    res, steps = V.ekanyunena(n, nines)
    m = 10 ** nines - 1
    return Q(f"{fmt(n)} × {fmt(m)}", fmt(res), " ".join(steps), f"{n}*{m} == {res}")


@gen("mult_101", "intermediate", "Multiplying by 101, 1001")
def _(r):
    k = r.choice([101, 1001])
    n = r.randint(10, 99) if k == 101 else r.randint(100, 999)
    return Q(f"{n} × {fmt(k)}", fmt(n * k), f"{k} = {k - 1} + 1, so write {n} twice (padded): {n} × {k} = {fmt(n * k)}.", f"{n}*{k} == {n * k}")


@gen("nikhilam_below", "intermediate", "Nikhilam: both numbers below a base")
def _(r):
    base = r.choice([100, 100, 1000])
    a, b = base - r.randint(1, 12 if base == 100 else 40), base - r.randint(1, 12 if base == 100 else 40)
    res, steps = V.nikhilam_multiply(a, b, base)
    return Q(f"{a} × {b} (Nikhilam, base {fmt(base)})", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("nikhilam_above", "intermediate", "Nikhilam: both numbers above a base")
def _(r):
    base = r.choice([100, 100, 1000])
    a, b = base + r.randint(1, 15 if base == 100 else 60), base + r.randint(1, 15 if base == 100 else 60)
    res, steps = V.nikhilam_multiply(a, b, base)
    return Q(f"{fmt(a)} × {fmt(b)} (base {fmt(base)})", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("nikhilam_mixed", "advanced", "Nikhilam: one above, one below")
def _(r):
    a, b = 100 + r.randint(2, 12), 100 - r.randint(2, 12)
    res, steps = V.nikhilam_multiply(a, b, 100)
    return Q(f"{a} × {b}", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("nikhilam_working_base", "advanced", "Nikhilam with a working base (50, 200, 300 …)")
def _(r):
    base = r.choice([50, 200, 300, 400, 500])
    a, b = base + r.randint(-9, 9), base + r.randint(-9, 9)
    p = 10 ** (len(str(base)) - 1)
    m = base // p
    da, db = a - base, b - base
    left = (a + db) * m
    right = da * db
    res = a * b
    sol = f"Working base {base} = {m} × {p}. Deviations {da:+d}, {db:+d}. Left: ({a} {db:+d}) × {m} = {left}. Right: {da} × {db} = {right}. {left} × {p} + {right} = {fmt(res)}."
    return Q(f"{a} × {b} (working base {base})", fmt(res), sol.replace("-", M), f"{a}*{b} == {res}")


@gen("urdhva_2x2", "intermediate", "Vertically and crosswise: 2-digit × 2-digit")
def _(r):
    a, b = r.randint(12, 99), r.randint(12, 99)
    res, steps = V.urdhva_multiply(a, b)
    return Q(f"{a} × {b} (vertically and crosswise)", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("urdhva_3x3", "advanced", "Vertically and crosswise: 3-digit × 3-digit")
def _(r):
    a, b = r.randint(101, 999), r.randint(101, 999)
    res, steps = V.urdhva_multiply(a, b)
    return Q(f"{a} × {b}", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("units_sum_10", "intermediate", "Same tens digit, units adding to 10")
def _(r):
    p = r.randint(1, 15)
    u = r.randint(1, 9)
    a, b = p * 10 + u, p * 10 + 10 - u
    res, steps = V.same_prefix_units_ten(a, b)
    return Q(f"{a} × {b}", fmt(res), " ".join(steps), f"{a}*{b} == {res}")


@gen("square_end5", "beginner", "Squaring numbers ending in 5")
def _(r):
    n = r.randint(1, 19) * 10 + 5
    res, steps = V.square_ending_5(n)
    return Q(f"{n}²", fmt(res), " ".join(steps), f"{n}**2 == {res}")


@gen("square_near_base", "intermediate", "Squaring near 100 or 1000 (Yavadunam)")
def _(r):
    base = r.choice([100, 100, 1000])
    d = r.randint(-15, 15) if base == 100 else r.randint(-40, 40)
    d = d or 3
    n = base + d
    res, steps = V.yavadunam_square(n, base)
    return Q(f"{fmt(n)}²", fmt(res), " ".join(steps), f"{n}**2 == {res}")


@gen("square_near_50", "intermediate", "Squaring numbers near 50")
def _(r):
    n = 50 + r.choice([x for x in range(-9, 10) if x])
    res, steps = V.square_near_50(n)
    return Q(f"{n}²", fmt(res), " ".join(steps), f"{n}**2 == {res}")


@gen("square_duplex", "advanced", "Squaring with the duplex method")
def _(r):
    n = r.randint(21, 999)
    res, steps = V.duplex_square(n)
    return Q(f"{n}² (duplex method)", fmt(res), " ".join(steps), f"{n}**2 == {res}")


@gen("mult_decompose", "beginner", "Multiplication by breaking numbers (distributive)")
def _(r):
    a, b = r.randint(12, 99), r.randint(3, 9)
    t, u = a - a % 10, a % 10
    return Q(f"{a} × {b}", fmt(a * b), f"({t} + {u}) × {b} = {t * b} + {u * b} = {a * b}.", f"{a}*{b} == {a * b}")


@gen("mult_negative", "intermediate", "Multiplying with negative numbers")
def _(r):
    a, b = r.randint(2, 30) * r.choice([1, -1]), r.randint(2, 30) * r.choice([1, -1])
    t = lambda x: f"({fmt(x)})" if x < 0 else str(x)
    return Q(f"{t(a)} × {t(b)}", fmt(a * b), "Same signs → positive; different signs → negative. " + f"{abs(a)} × {abs(b)} = {abs(a * b)}.", f"({a})*({b}) == {a * b}")


# ============================================================ division (Part V)

@gen("div_by_9", "beginner", "Dividing by 9 (Nikhilam)")
def _(r):
    n = r.randint(100, 99999)
    (q, rem), steps = V.nikhilam_divide_by_9(n)
    return Q(f"{fmt(n)} ÷ 9 (quotient and remainder)", f"Q = {fmt(q)}, R = {rem}", " ".join(steps), f"divmod({n}, 9) == ({q}, {rem})")


@gen("div_nikhilam", "advanced", "Nikhilam division by 8, 88, 97, 98, 997")
def _(r):
    d = r.choice([8, 7, 89, 88, 97, 98, 996, 997, 998])
    n = r.randint(10 * d, 99 * d + d - 1) if d < 10 else r.randint(10 * d, 50 * d)
    (q, rem), steps = V.nikhilam_divide(n, d)
    return Q(f"{fmt(n)} ÷ {d}", f"Q = {fmt(q)}, R = {rem}", " ".join(steps), f"divmod({n}, {d}) == ({q}, {rem})")


@gen("div_paravartya", "advanced", "Paravartya division by 12, 13, 112, 1012")
def _(r):
    d = r.choice([11, 12, 13, 14, 111, 112, 113, 121, 1012])
    n = r.randint(20 * d, 90 * d)
    (q, rem), steps = V.paravartya_divide(n, d)
    return Q(f"{fmt(n)} ÷ {d}", f"Q = {fmt(q)}, R = {rem}", " ".join(steps), f"divmod({n}, {d}) == ({q}, {rem})")


@gen("div_5_25_125", "beginner", "Dividing by 5, 25, 50, 125")
def _(r):
    d = r.choice([5, 25, 50, 125])
    n = r.randint(11, 9999)
    k = {5: 2, 25: 4, 50: 2, 125: 8}[d]
    p = {5: 10, 25: 100, 50: 100, 125: 1000}[d]
    res = Fraction(n, d)
    return Q(f"{fmt(n)} ÷ {d} (as a decimal)", fmt(float(res)), f"÷ {d} = × {k} ÷ {p}: {fmt(n)} × {k} = {fmt(n * k)}, ÷ {p} = {fmt(float(res))}.",
             f"Fraction({n},{d}) == Fraction('{float(res)}')")


@gen("long_division", "beginner", "Long division with remainder")
def _(r):
    d = r.randint(3, 29)
    n = r.randint(100, 9999)
    q, rem = divmod(n, d)
    return Q(f"{fmt(n)} ÷ {d}", f"Q = {fmt(q)}, R = {rem}", f"Check: {d} × {fmt(q)} + {rem} = {fmt(d * q + rem)}.", f"divmod({n},{d}) == ({q},{rem})")


@gen("recurring_19", "advanced", "Recurring decimals: 1/19, 1/29 (Ekadhikena)")
def _(r):
    den = r.choice([19, 29, 39, 49, 59])
    s, steps = V.recurring_1_over_x9(den)
    shown = s if len(s) <= 24 else s[:24] + "…"
    return Q(f"Find the recurring block of 1/{den}.", f"0.({shown})", " ".join(steps).replace(s, shown),
             f"int('{s}') * {den} == 10**{len(s)} - 1")


# ============================================================ algebra (Part VII)

@gen("linear_eq", "beginner", "Linear equations (Paravartya: transpose and adjust)")
def _(r):
    x = r.randint(-12, 15)
    a, b = r.randint(2, 9), r.randint(-20, 20)
    c = a * x + b
    sb = f"+ {b}" if b >= 0 else f"{M} {abs(b)}"
    return Q(f"Solve {a}x {sb} = {fmt(c)}", f"x = {fmt(x)}",
             f"Transpose {fmt(b)} (change sign): {a}x = {fmt(c)} {'−' if b >= 0 else '+'} {abs(b)} = {fmt(c - b)}; divide by {a}: x = {fmt(x)}.",
             f"{a}*({x}) + ({b}) == {c}")


@gen("linear_two_sides", "intermediate", "Equations with x on both sides")
def _(r):
    x = r.randint(-10, 12)
    a, c = r.randint(3, 12), r.randint(1, 9)
    while a == c:
        c = r.randint(1, 9)
    b, d = r.randint(-15, 15), None
    d = a * x + b - c * x
    sg = lambda v: f"+ {v}" if v >= 0 else f"{M} {abs(v)}"
    return Q(f"Solve {a}x {sg(b)} = {c}x {sg(d)}", f"x = {fmt(x)}",
             f"Paravartya formula for ax + b = cx + d: x = (d − b)/(a − c) = ({fmt(d)} − {fmt(b)})/({a} − {c}) = {fmt(d - b)}/{a - c} = {fmt(x)}.",
             f"{a}*({x})+({b}) == {c}*({x})+({d})")


@gen("simultaneous", "intermediate", "Simultaneous equations (cross-multiplication)")
def _(r):
    x, y = r.randint(-6, 9), r.randint(-6, 9)
    a1, b1, a2, b2 = r.randint(1, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9)
    while a1 * b2 - a2 * b1 == 0:
        b2 = r.randint(1, 9)
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    D = a1 * b2 - a2 * b1
    return Q(f"Solve: {a1}x + {b1}y = {fmt(c1)},  {a2}x + {b2}y = {fmt(c2)}", f"x = {fmt(x)}, y = {fmt(y)}",
             f"x = (c₁b₂ − c₂b₁)/(a₁b₂ − a₂b₁) = ({fmt(c1 * b2)} − {fmt(c2 * b1)})/{fmt(D)} = {fmt(x)}; y = (a₁c₂ − a₂c₁)/(a₁b₂ − a₂b₁) = ({fmt(a1 * c2)} − {fmt(a2 * c1)})/{fmt(D)} = {fmt(y)}.",
             f"{a1}*({x})+{b1}*({y}) == {c1} and {a2}*({x})+{b2}*({y}) == {c2}")


@gen("sankalana", "advanced", "Sankalana-Vyavakalanabhyam (swapped coefficients)")
def _(r):
    x, y = r.randint(-5, 9), r.randint(-5, 9)
    a, b = r.randint(10, 60), r.randint(10, 60)
    while a == b:
        b = r.randint(10, 60)
    p, q = a * x + b * y, b * x + a * y
    return Q(f"Solve: {a}x + {b}y = {fmt(p)},  {b}x + {a}y = {fmt(q)}", f"x = {fmt(x)}, y = {fmt(y)}",
             f"Add: {a + b}(x + y) = {fmt(p + q)} → x + y = {fmt(x + y)}. Subtract: {a - b}(x − y) = {fmt(p - q)} → x − y = {fmt(x - y)}. Solve: x = {fmt(x)}, y = {fmt(y)}.",
             f"{a}*({x})+{b}*({y}) == {p} and {b}*({x})+{a}*({y}) == {q}")


@gen("shunyam", "advanced", "Shunyam Saamyasamuccaye")
def _(r):
    a, b = r.randint(1, 12), r.randint(1, 12)
    c, d = r.randint(1, 12), r.randint(1, 12)
    # (x+a)(x+b) = (x+c)(x+d) with ab = cd -> x = 0 ; otherwise x = (cd-ab)/(a+b-c-d)
    while a + b == c + d:
        d = r.randint(1, 12)
    x = Fraction(c * d - a * b, a + b - c - d)
    rule = "Independent terms are equal (ab = cd), so x = 0." if a * b == c * d else f"x = (cd − ab)/(a + b − c − d) = ({c * d} − {a * b})/({a + b} − {c + d})."
    return Q(f"Solve (x + {a})(x + {b}) = (x + {c})(x + {d})", f"x = {frac_str(x)}", rule,
             f"(Fraction({x.numerator},{x.denominator})+{a})*(Fraction({x.numerator},{x.denominator})+{b}) == (Fraction({x.numerator},{x.denominator})+{c})*(Fraction({x.numerator},{x.denominator})+{d})")


@gen("expand_binomials", "beginner", "Multiplying binomials (vertically and crosswise)")
def _(r):
    a, b = r.choice([x for x in range(-9, 10) if x]), r.choice([x for x in range(-9, 10) if x])
    p, q = r.randint(1, 4), r.randint(1, 3)
    A, B, C = p * q, p * b + q * a, a * b
    sg = lambda v: f"+ {v}" if v >= 0 else f"{M} {abs(v)}"
    term = lambda k, s: ("" if k == 1 else str(k)) + s
    lhs = f"({term(p, 'x')} {sg(a)})({term(q, 'x')} {sg(b)})"
    rhs = f"{term(A, 'x²')} {sg(B)}x {sg(C)}".replace(" + 0x", "").replace(f" {M} 0x", "")
    return Q(f"Expand {lhs}", rhs, f"Vertical (left): {p} × {q} = {A}. Crosswise: {p} × ({fmt(b)}) + {q} × ({fmt(a)}) = {fmt(B)}. Vertical (right): ({fmt(a)}) × ({fmt(b)}) = {fmt(C)}.",
             f"all(({p}*t+{a})*({q}*t+{b}) == {A}*t*t+{B}*t+{C} for t in range(-3,4))")


@gen("factor_quadratic", "intermediate", "Factorising x² + bx + c")
def _(r):
    m, n = r.choice([x for x in range(-9, 10) if x]), r.choice([x for x in range(-9, 10) if x])
    b, c = m + n, m * n
    sg = lambda v: f"+ {v}" if v >= 0 else f"{M} {abs(v)}"
    poly = f"x² {sg(b)}x {sg(c)}".replace(" + 0x", "").replace(f" {M} 0x", "")
    if b in (1, -1):
        poly = poly.replace(f"{sg(b)}x", ("+ x" if b == 1 else f"{M} x"))
    return Q(f"Factorise {poly}", f"(x {sg(m)})(x {sg(n)})",
             f"Find two numbers with product {fmt(c)} and sum {fmt(b)}: {fmt(m)} and {fmt(n)}. Check with Gunita-samuccaya (put x = 1): (1 {sg(m)})(1 {sg(n)}) = {fmt((1 + m) * (1 + n))} and 1 {sg(b)} {sg(c)} = {fmt(1 + b + c)}.",
             f"{m}+{n} == {b} and {m}*{n} == {c}")


@gen("diff_squares", "intermediate", "Difference of squares (numeric)")
def _(r):
    a, b = r.randint(30, 99), r.randint(5, 29)
    return Q(f"{a}² {M} {b}²", fmt(a * a - b * b), f"a² − b² = (a + b)(a − b) = {a + b} × {a - b} = {fmt(a * a - b * b)}.", f"{a}**2-{b}**2 == {a * a - b * b}")


@gen("identity_square", "intermediate", "(a ± b)² for quick squares")
def _(r):
    base = r.choice([20, 30, 40, 60, 70, 80, 90, 100, 200, 300])
    d = r.choice([1, 2, 3, -1, -2, -3])
    n = base + d
    return Q(f"Use (a ± b)² to find {n}²", fmt(n * n), f"({base} {'+' if d > 0 else '−'} {abs(d)})² = {base * base} {'+' if d > 0 else '−'} 2×{base}×{abs(d)} + {d * d} = {fmt(n * n)}.", f"{n}**2 == {n * n}")


@gen("puranapurana", "advanced", "Puranapuranabhyam (completing the cube)")
def _(r):
    k = r.randint(1, 5)
    # (x+k)^3 - (x+k) = 0 -> x = -k, -k-1, -k+1
    a2, a1, a0 = 3 * k, 3 * k * k - 1, k ** 3 - k
    sg = lambda v: f"+ {v}" if v >= 0 else f"{M} {abs(v)}"
    roots = sorted([-k - 1, -k, -k + 1])
    return Q(f"Solve x³ + {a2}x² {sg(a1)}x {sg(a0)} = 0 by completing the cube", "x = " + ", ".join(fmt(t) for t in roots),
             f"(x + {k})³ = x³ + {a2}x² + {3 * k * k}x + {k ** 3}. The given cubic = (x + {k})³ − (x + {k}). Let y = x + {k}: y³ − y = 0 → y = 0, ±1.",
             f"all(t**3 + {a2}*t*t + {a1}*t + {a0} == 0 for t in {roots})")


@gen("chalana_quadratic", "advanced", "Chalana-Kalanabhyam (roots of a quadratic)")
def _(r):
    m, n = r.randint(-8, 8), r.randint(-8, 8)
    while m == n:
        n = r.randint(-8, 8)
    b, c = -(m + n), m * n
    disc = b * b - 4 * c
    sg = lambda v: f"+ {v}" if v >= 0 else f"{M} {abs(v)}"
    return Q(f"Solve x² {sg(b)}x {sg(c)} = 0 using 2x + b = ±√(b² − 4c)", f"x = {fmt(max(m, n))} or {fmt(min(m, n))}",
             f"Differential: 2x {sg(b)}. Discriminant = {b * b} − {4 * c} = {disc}, √ = {math.isqrt(disc)}. 2x {sg(b)} = ±{math.isqrt(disc)}.",
             f"all(t*t + ({b})*t + ({c}) == 0 for t in ({m},{n}))")


# ============================================================ aptitude (Part VIII)

@gen("ratio_share", "beginner", "Dividing in a ratio")
def _(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    while math.gcd(a, b) != 1:
        b = r.randint(1, 9)
    unit = r.randint(50, 900)
    total = (a + b) * unit
    return Q(f"Divide ₹{fmt(total)} between A and B in the ratio {a} : {b}.", f"A ₹{fmt(a * unit)}, B ₹{fmt(b * unit)}",
             f"Total parts {a + b}; one part = {fmt(total)} ÷ {a + b} = {unit}.", f"{a * unit}+{b * unit} == {total} and {a * unit}*{b} == {b * unit}*{a}")


@gen("average", "beginner", "Averages (deviation method)")
def _(r):
    base = r.randint(40, 80)
    devs = [r.randint(-9, 9) for _ in range(r.randint(5, 7))]
    devs[-1] -= sum(devs) % len(devs)
    nums = [base + d for d in devs]
    avg = Fraction(sum(nums), len(nums))
    return Q("Find the average of " + ", ".join(map(str, nums)) + ".", frac_str(avg),
             f"Assume {base}. Deviations: {', '.join(f'{d:+d}' for d in devs)}; total {sum(devs):+d}; ÷ {len(nums)} = {Fraction(sum(devs), len(nums))}. Average = {frac_str(avg)}.".replace("-", M),
             f"Fraction(sum({nums}), {len(nums)}) == Fraction({avg.numerator},{avg.denominator})")


@gen("weighted_average", "intermediate", "Weighted averages")
def _(r):
    n1, n2 = r.randint(10, 40), r.randint(10, 40)
    a1, a2 = r.randint(40, 70), r.randint(55, 90)
    avg = Fraction(n1 * a1 + n2 * a2, n1 + n2)
    return Q(f"Section A has {n1} students with average {a1}; section B has {n2} students with average {a2}. Find the combined average.",
             frac_str(avg) if avg.denominator == 1 else f"{float(avg):.2f}", f"({n1}×{a1} + {n2}×{a2}) ÷ {n1 + n2} = {n1 * a1 + n2 * a2} ÷ {n1 + n2}.",
             f"abs(({n1}*{a1}+{n2}*{a2})/({n1}+{n2}) - {float(avg)}) < 0.005")


@gen("profit_loss", "intermediate", "Profit and loss")
def _(r):
    cp = r.choice([200, 250, 400, 500, 600, 800, 1200, 1500, 2400])
    p = r.choice([q for q in [-25, -20, -12, -10, -5, 5, 8, 10, 12, 15, 20, 25, 40] if cp * q % 100 == 0])
    sp = cp * (100 + p) // 100
    word = "profit" if p > 0 else "loss"
    return Q(f"An item costing ₹{fmt(cp)} is sold for ₹{fmt(sp)}. Find the {word} percentage.", f"{abs(p)}% {word}",
             f"{word.title()} = {abs(sp - cp)}. % = {abs(sp - cp)}/{cp} × 100 = {abs(p)}%.", f"({sp}-{cp})*100 == {p}*{cp}")


@gen("discount", "intermediate", "Successive discounts")
def _(r):
    d1, d2 = r.choice([10, 20, 25, 30]), r.choice([5, 10, 15, 20])
    eff = Fraction(d1 + d2) - Fraction(d1 * d2, 100)
    return Q(f"Find the single discount equal to successive discounts of {d1}% and {d2}%.", f"{frac_str(eff)}%",
             f"Net = a + b − ab/100 = {d1} + {d2} − {d1 * d2}/100 = {frac_str(eff)}%.",
             f"Fraction(100 - {d1}) * (100 - {d2}) / 100 == 100 - Fraction({eff.numerator},{eff.denominator})")


@gen("simple_interest", "beginner", "Simple interest")
def _(r):
    p = r.choice([5000, 8000, 10000, 12000, 15000, 25000, 40000])
    rate, t = r.choice([4, 5, 6, 8, 10, 12]), r.randint(2, 6)
    si = p * rate * t // 100
    return Q(f"Find the simple interest on ₹{fmt(p)} at {rate}% per annum for {t} years.", f"₹{fmt(si)}", f"SI = PRT/100 = {fmt(p)} × {rate} × {t} / 100 = {fmt(si)}.",
             f"{p}*{rate}*{t} == {si}*100")


@gen("compound_interest", "intermediate", "Compound interest")
def _(r):
    p = r.choice([10000, 20000, 40000, 50000, 80000])
    rate = r.choice([5, 10, 20])
    t = r.choice([2, 3])
    amt = Fraction(p) * Fraction(100 + rate, 100) ** t
    ci = amt - p
    return Q(f"Find the compound interest on ₹{fmt(p)} at {rate}% per annum, compounded yearly, for {t} years.", money(ci),
             f"A = P(1 + R/100)ⁿ = {fmt(p)} × ({100 + rate}/100)^{{{t}}} = {money(amt)}. CI = A − P = {money(ci)}.",
             f"abs({p}*(1+{rate}/100)**{t} - {p} - {float(ci)}) < 0.01")


@gen("time_work", "intermediate", "Time and work")
def _(r):
    a, b = r.choice([(10, 15), (12, 24), (20, 30), (6, 12), (8, 24), (15, 10), (18, 9), (12, 36), (20, 5)])
    t = Fraction(a * b, a + b)
    lcm = a * b // math.gcd(a, b)
    return Q(f"A can finish a job in {a} days and B in {b} days. How long will they take together?", f"{frac_str(t)} days",
             f"Total work = LCM({a},{b}) = {lcm} units. A does {lcm // a}/day, B does {lcm // b}/day; together {lcm // a + lcm // b}/day. Time = {lcm}/{lcm // a + lcm // b} = {frac_str(t)} days.",
             f"Fraction(1,{a}) + Fraction(1,{b}) == 1 / Fraction({t.numerator},{t.denominator})")


@gen("pipes", "intermediate", "Pipes and cisterns")
def _(r):
    f, e = r.choice([(6, 12), (10, 15), (8, 24), (12, 20), (5, 20), (4, 6)])
    t = Fraction(1, Fraction(1, f) - Fraction(1, e))
    return Q(f"Pipe A fills a tank in {f} hours; pipe B empties it in {e} hours. If both are open, how long to fill the empty tank?", f"{frac_str(t)} hours",
             f"Net rate = 1/{f} − 1/{e} = {Fraction(1, f) - Fraction(1, e)} tank/hour, so time = {frac_str(t)} hours.",
             f"Fraction(1,{f}) - Fraction(1,{e}) == 1 / Fraction({t.numerator},{t.denominator})")


@gen("speed", "beginner", "Speed, distance, time")
def _(r):
    s = r.choice([36, 45, 54, 60, 72, 90])
    t = r.choice([Fraction(1, 2), Fraction(3, 4), Fraction(3, 2), 2, Fraction(5, 2), 3])
    d = s * Fraction(t)
    ms = Fraction(s * 5, 18)
    return Q(f"A car travels at {s} km/h for {frac_str(Fraction(t))} hours. Find the distance, and the speed in m/s.", f"{frac_str(d)} km; {frac_str(ms)} m/s",
             f"D = S × T = {s} × {frac_str(Fraction(t))} = {frac_str(d)} km. km/h → m/s: × 5/18 → {frac_str(ms)} m/s.",
             f"{s}*Fraction('{Fraction(t)}') == Fraction({d.numerator},{d.denominator}) and Fraction({s}*1000, 3600) == Fraction({ms.numerator},{ms.denominator})")


@gen("trains", "intermediate", "Trains")
def _(r):
    L1, L2 = r.choice([100, 120, 150, 180, 200, 240]), r.choice([80, 100, 130, 160, 200])
    s1, s2 = r.choice([54, 72, 90]), r.choice([36, 45, 54, 63])
    opp = r.random() < 0.5 or s1 == s2
    rel = s1 + s2 if opp else s1 - s2
    if rel <= 0:
        s1, s2 = s2, s1
        rel = s1 - s2
    t = Fraction((L1 + L2) * 18, rel * 5)
    return Q(f"Two trains {L1} m and {L2} m long run at {s1} km/h and {s2} km/h in {'opposite directions' if opp else 'the same direction'}. How long do they take to cross each other?",
             f"{frac_str(t)} s", f"Relative speed = {rel} km/h = {frac_str(Fraction(rel * 5, 18))} m/s. Distance = {L1} + {L2} = {L1 + L2} m. Time = {frac_str(t)} s.",
             f"Fraction({L1}+{L2}) / Fraction({rel}*5, 18) == Fraction({t.numerator},{t.denominator})")


@gen("boats", "intermediate", "Boats and streams")
def _(r):
    b, s = r.randint(8, 20), r.randint(1, 6)
    while s >= b:
        s = r.randint(1, 6)
    return Q(f"A boat goes downstream at {b + s} km/h and upstream at {b - s} km/h. Find the speed of the boat in still water and of the stream.", f"Boat {b} km/h, stream {s} km/h",
             f"Boat = (down + up)/2 = ({b + s} + {b - s})/2 = {b}. Stream = (down − up)/2 = {s}.", f"({b+s}+{b-s})//2 == {b} and ({b+s}-{b-s})//2 == {s}")


@gen("alligation", "advanced", "Mixtures and alligation")
def _(r):
    c1, c2 = r.choice([20, 30, 40, 50]), r.choice([60, 70, 80, 90])
    m = r.randint(c1 + 2, c2 - 2)
    a, b = c2 - m, m - c1
    g = math.gcd(a, b)
    return Q(f"In what ratio should rice at ₹{c1}/kg be mixed with rice at ₹{c2}/kg to get a mixture worth ₹{m}/kg?", f"{a // g} : {b // g}",
             f"Alligation cross: ({c2} − {m}) : ({m} − {c1}) = {a} : {b} = {a // g} : {b // g}.",
             f"Fraction({c1}*{a // g} + {c2}*{b // g}, {a // g + b // g}) == {m}")


@gen("partnership", "intermediate", "Partnership")
def _(r):
    i1, i2 = r.choice([20000, 30000, 40000, 50000]), r.choice([25000, 35000, 45000, 60000])
    m1, m2 = 12, r.choice([6, 8, 9, 10, 12])
    w1, w2 = i1 * m1, i2 * m2
    g = math.gcd(w1, w2)
    k = (w1 + w2) // g
    profit = k * r.randint(500, 3000)
    s1 = profit * w1 // (w1 + w2)
    return Q(f"A invests ₹{fmt(i1)} for {m1} months and B invests ₹{fmt(i2)} for {m2} months. Profit is ₹{fmt(profit)}. Find A's share.", f"₹{fmt(s1)}",
             f"Ratio = {fmt(i1)}×{m1} : {fmt(i2)}×{m2} = {w1 // g} : {w2 // g}. A's share = {w1 // g}/{k} × {fmt(profit)} = {fmt(s1)}.",
             f"{s1}*({w1}+{w2}) == {profit}*{w1}")


@gen("ages", "intermediate", "Problems on ages")
def _(r):
    son = r.randint(5, 20)
    k = r.choice([2, 3, 4])
    father = k * son
    y = r.randint(2, 10)
    return Q(f"A father is {k} times as old as his son. In {y} years the sum of their ages will be {father + son + 2 * y}. Find their present ages.", f"Son {son}, father {father}",
             f"Let son = x, father = {k}x. ({k}x + {y}) + (x + {y}) = {father + son + 2 * y} → {k + 1}x = {father + son} → x = {son}.",
             f"{k}*{son} == {father} and ({father}+{y})+({son}+{y}) == {father + son + 2 * y}")


@gen("cyclicity", "intermediate", "Last digit using cyclicity")
def _(r):
    b = r.choice([2, 3, 4, 7, 8, 9, 13, 17, 22, 27, 33, 38])
    e = r.randint(20, 999)
    cyc = []
    x = b % 10
    while x not in cyc:
        cyc.append(x)
        x = (x * b) % 10
    last = pow(b, e, 10)
    return Q(f"Find the last digit of {b}^{{{e}}}.", str(last),
             f"Last digits of powers of {b % 10} repeat: {', '.join(map(str, cyc))} (cycle {len(cyc)}). {e} mod {len(cyc)} = {e % len(cyc) or len(cyc)} → {last}.",
             f"pow({b}, {e}, 10) == {last}")


@gen("ncr", "intermediate", "Combinations and permutations")
def _(r):
    n, k = r.randint(5, 12), r.randint(2, 4)
    if r.random() < 0.5:
        return Q(f"In how many ways can a committee of {k} be chosen from {n} people?", fmt(math.comb(n, k)),
                 f"Order does not matter: ⁿCᵣ = {n}!/({k}!·{n - k}!) = {fmt(math.comb(n, k))}.", f"math.comb({n},{k}) == {math.comb(n, k)}")
    return Q(f"In how many ways can {k} prizes (1st, 2nd, …) be given to {n} students, one prize each?", fmt(math.perm(n, k)),
             f"Order matters: ⁿPᵣ = {n} × {n - 1} × … ({k} factors) = {fmt(math.perm(n, k))}.", f"math.perm({n},{k}) == {math.perm(n, k)}")


@gen("probability", "intermediate", "Basic probability")
def _(r):
    kind = r.choice(["dice_sum", "cards", "coins", "balls"])
    if kind == "dice_sum":
        s = r.randint(3, 11)
        fav = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == s)
        p = Fraction(fav, 36)
        return Q(f"Two dice are thrown. What is the probability that the sum is {s}?", str(p), f"{fav} favourable outcomes out of 36 → {fav}/36 = {p}.",
                 f"Fraction(sum(1 for a in range(1,7) for b in range(1,7) if a+b=={s}), 36) == Fraction('{p}')")
    if kind == "cards":
        what, fav = r.choice([("a king", 4), ("a heart", 13), ("a red card", 26), ("a face card (J, Q, K)", 12), ("a red king", 2)])
        p = Fraction(fav, 52)
        return Q(f"A card is drawn from a well-shuffled deck of 52. Probability of {what}?", str(p), f"{fav}/52 = {p}.", f"Fraction({fav},52) == Fraction('{p}')")
    if kind == "coins":
        n = r.choice([2, 3, 4])
        k = r.randint(1, n)
        p = Fraction(math.comb(n, k), 2 ** n)
        return Q(f"{n} fair coins are tossed. Probability of exactly {k} heads?", str(p), f"C(n, k)/2ⁿ = {math.comb(n, k)}/{2 ** n} = {p}.", f"Fraction(math.comb({n},{k}), 2**{n}) == Fraction('{p}')")
    rb, bb = r.randint(2, 8), r.randint(2, 8)
    p = Fraction(math.comb(rb, 2), math.comb(rb + bb, 2))
    return Q(f"A bag has {rb} red and {bb} blue balls. Two are drawn at random. Probability both are red?", str(p), f"C(red, 2)/C(total, 2) = {math.comb(rb, 2)}/{math.comb(rb + bb, 2)} = {p}.",
             f"Fraction(math.comb({rb},2), math.comb({rb + bb},2)) == Fraction('{p}')")


@gen("mensuration", "intermediate", "Mensuration (π = 22/7)")
def _(r):
    kind = r.choice(["circle", "cylinder", "rect", "cone", "sphere"])
    rad = 7 * r.randint(1, 4)
    if kind == "circle":
        a = Fraction(22, 7) * rad * rad
        c = Fraction(44, 7) * rad
        return Q(f"Find the area and circumference of a circle of radius {rad} cm (π = 22/7).", f"Area {frac_str(a)} cm², circumference {frac_str(c)} cm",
                 f"A = πr² = 22/7 × {rad}² = {frac_str(a)}; C = 2πr = {frac_str(c)}.", f"Fraction(22,7)*{rad}**2 == {a} and Fraction(44,7)*{rad} == {c}")
    if kind == "cylinder":
        h = r.randint(5, 20)
        v = Fraction(22, 7) * rad * rad * h
        return Q(f"Volume of a cylinder with radius {rad} cm and height {h} cm (π = 22/7)?", f"{frac_str(v)} cm³", f"V = πr²h = 22/7 × {rad * rad} × {h} = {frac_str(v)}.", f"Fraction(22,7)*{rad}**2*{h} == {v}")
    if kind == "cone":
        h = r.choice([6, 9, 12, 15])
        v = Fraction(1, 3) * Fraction(22, 7) * rad * rad * h
        return Q(f"Volume of a cone with radius {rad} cm and height {h} cm (π = 22/7)?", f"{frac_str(v)} cm³", f"V = ⅓πr²h = {frac_str(v)}.", f"Fraction(22,21)*{rad}**2*{h} == Fraction({v.numerator},{v.denominator})")
    if kind == "sphere":
        v = Fraction(4, 3) * Fraction(22, 7) * rad ** 3
        return Q(f"Volume of a sphere of radius {rad} cm (π = 22/7)?", f"{frac_str(v)} cm³", f"V = 4/3 πr³ = {frac_str(v)}.", f"Fraction(88,21)*{rad}**3 == Fraction({v.numerator},{v.denominator})")
    l, w = r.randint(12, 60), r.randint(5, 40)
    return Q(f"A rectangular field is {l} m by {w} m. Find its area and perimeter.", f"Area {fmt(l * w)} m², perimeter {2 * (l + w)} m", f"A = l × w; P = 2(l + w).", f"{l}*{w} == {l * w}")


@gen("calendar", "advanced", "Day of the week")
def _(r):
    y = r.randint(1950, 2030)
    m = r.randint(1, 12)
    d = r.randint(1, 28)
    day = date(y, m, d).strftime("%A")
    return Q(f"What day of the week was/is {d} {date(y, m, d).strftime('%B')} {y}?", day,
             "Use odd days: count year codes, month codes and leap years (see Part IX), then take the total mod 7.",
             f"date({y},{m},{d}).strftime('%A') == '{day}'")


@gen("pct_fraction_trick", "beginner", "Percentages via fractions")
def _(r):
    p, f = r.choice([(12.5, Fraction(1, 8)), (25, Fraction(1, 4)), (Fraction(100, 3), Fraction(1, 3)), (20, Fraction(1, 5)), (Fraction(50, 3), Fraction(1, 6)),
                     (Fraction(25, 2) * 3, Fraction(3, 8)), (75, Fraction(3, 4)), (Fraction(200, 3), Fraction(2, 3)), (Fraction(100, 9), Fraction(1, 9)), (Fraction(100, 11), Fraction(1, 11))])
    n = f.denominator * r.randint(12, 150)
    res = f * n
    ps = frac_str(Fraction(p)) if not isinstance(p, float) else f"{p:g}"
    return Q(f"Find {ps}% of {fmt(n)} using a fraction.", fmt(res), f"{ps}% = {f}. {f} × {fmt(n)} = {fmt(res)}.", f"Fraction({f.numerator},{f.denominator})*{n} == {res}")


# ============================================================ children (Part X)

@gen("number_bond", "beginner", "Number bonds")
def _(r):
    total = r.choice([10, 10, 20, 100])
    a = r.randint(1, total - 1)
    return Q(f"{a} + ☐ = {total}", str(total - a), f"Count on from {a} to {total}, or think: which number makes {total} with {a}?", f"{a} + {total - a} == {total}")


@gen("kids_add", "beginner", "Adding small numbers (objects)")
def _(r):
    item = r.choice(["mangoes", "toy cars", "balloons", "pencils", "laddoos", "marbles"])
    a, b = r.randint(2, 12), r.randint(2, 12)
    return Q(f"Riya has {a} {item}. Her friend gives her {b} more. How many {item} does she have now?", str(a + b), f"Start at {a} and count on {b}: {a} + {b} = {a + b}.", f"{a}+{b} == {a + b}")


@gen("kids_sub", "beginner", "Taking away (number line)")
def _(r):
    a = r.randint(8, 30)
    b = r.randint(2, a - 1)
    item = r.choice(["birds on a tree", "coins in a box", "apples in a basket", "blocks in a tower"])
    return Q(f"There are {a} {item}. {b} are taken away. How many are left?", str(a - b), f"On a number line, start at {a} and jump back {b}: {a} − {b} = {a - b}.", f"{a}-{b} == {a - b}")


@gen("missing_number", "beginner", "Missing-number puzzles")
def _(r):
    start, step = r.randint(1, 20), r.choice([2, 3, 4, 5, 10])
    seq = [start + i * step for i in range(6)]
    hole = r.randint(1, 4)
    shown = ", ".join("☐" if i == hole else str(v) for i, v in enumerate(seq))
    return Q(f"Find the missing number: {shown}", str(seq[hole]), f"The numbers go up by {step} each time.", f"{seq[hole - 1]} + {step} == {seq[hole]}")


@gen("doubles_halves", "beginner", "Doubles and halves")
def _(r):
    n = r.randint(6, 60) * 2
    if r.random() < 0.5:
        return Q(f"Double {n // 2}", str(n), f"Double = add the number to itself: {n // 2} + {n // 2} = {n}.", f"2*{n // 2} == {n}")
    return Q(f"Half of {n}", str(n // 2), f"Split {n} into two equal groups.", f"{n}//2*2 == {n}")


@gen("times_table", "beginner", "Times-table facts")
def _(r):
    a, b = r.randint(2, 12), r.randint(2, 12)
    return Q(f"{a} × {b}", str(a * b), f"{a} groups of {b} = {a * b}.", f"{a}*{b} == {a * b}")


@gen("kids_money", "intermediate", "Shopping with coins and notes")
def _(r):
    price = r.choice([12, 18, 25, 35, 42, 48, 65, 78, 85])
    paid = 100 if price > 50 else r.choice([50, 100])
    return Q(f"A toy costs ₹{price}. You pay with a ₹{paid} note. How much change do you get?", f"₹{paid - price}",
             f"Count up from {price} to {paid}: {paid - price}.", f"{paid}-{price} == {paid - price}")


@gen("kids_share", "intermediate", "Sharing equally")
def _(r):
    kids = r.randint(2, 8)
    each = r.randint(2, 9)
    left = r.randint(0, kids - 1)
    total = kids * each + left
    return Q(f"{total} sweets are shared equally among {kids} children. How many does each child get, and how many are left over?", f"{each} each, {left} left over",
             f"{kids} × {each} = {kids * each}; {total} − {kids * each} = {left}.", f"divmod({total},{kids}) == ({each},{left})")


# ============================================================ exam simplification

@gen("bodmas", "intermediate", "BODMAS simplification")
def _(r):
    a, b, c, d = r.randint(2, 20), r.randint(2, 12), r.randint(2, 9), r.randint(1, 30)
    e = b * c
    res = a + e // c * b - d if False else a + (e // c) * b - d
    text = f"{a} + {e} ÷ {c} × {b} {M} {d}"
    return Q(f"Simplify: {text}", fmt(res), f"Division and multiplication left to right first: {e} ÷ {c} = {e // c}; × {b} = {e // c * b}. Then {a} + {e // c * b} − {d} = {fmt(res)}.",
             f"{a} + {e} / {c} * {b} - {d} == {res}")


@gen("approx_simplify", "advanced", "Approximation for options (approximate)")
def _(r):
    a = r.randint(200, 999) + r.choice([0.98, 1.02, 0.97, 0.03])
    b = r.randint(11, 49) + r.choice([0.02, 0.98, 0.01])
    c = r.randint(100, 900) + r.choice([0.1, 0.9])
    ra, rb, rc = round(a), round(b), round(c)
    est = ra * rb / 10 + rc
    true = a * b / 10 + c
    return Q(f"Approximate: {a:.2f} × {b:.2f} ÷ 10 + {c:.1f}", f"≈ {est:.0f} (exact {true:.2f})", f"Round each number: {ra} × {rb} ÷ 10 + {rc} ≈ {est:.1f}.",
             f"abs({est} - {true}) / {true} < 0.05", exact=False)
