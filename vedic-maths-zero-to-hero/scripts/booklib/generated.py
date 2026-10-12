"""Large generated sections: the Part XII exercise bank and Part XIII practice sets."""
from __future__ import annotations

from reportlab.platypus import CondPageBreak, PageBreak, Paragraph, Spacer

from .questions import GENERATORS

LEVEL_ORDER = {"beginner": 0, "intermediate": 1, "advanced": 2}

BANK = [
    ("A. Numbers and foundations", ["place_value", "indian_to_intl", "prime_check", "divisibility", "integers", "factors"], [8, 8, 4]),
    ("B. Mental addition and subtraction", ["add_ltr", "add_comp", "sub_power10", "sub_comp", "add_column", "estimate_product"], [10, 8, 4]),
    ("C. Fractions, decimals and percentages", ["simplify_fraction", "frac_to_pct", "pct_of", "add_fractions", "pct_change", "decimal_mult", "pct_fraction_trick"], [10, 10, 4]),
    ("D. Powers, roots and number properties", ["square", "cube", "sqrt_perfect", "cbrt_perfect", "lcm_hcf", "prime_factorise", "exponents", "remainder", "sqrt_estimate"], [10, 12, 6]),
    ("E. Multiplication", ["mult_11", "mult_5_25", "mult_9s", "mult_decompose", "mult_101", "nikhilam_below", "nikhilam_above", "urdhva_2x2", "units_sum_10",
                           "square_end5", "mult_negative", "nikhilam_mixed", "nikhilam_working_base", "urdhva_3x3", "square_near_base", "square_near_50", "square_duplex"], [16, 22, 14]),
    ("F. Division and remainders", ["long_division", "div_by_9", "div_5_25_125", "div_nikhilam", "div_paravartya", "recurring_19"], [10, 6, 10]),
    ("G. Algebra", ["linear_eq", "expand_binomials", "linear_two_sides", "simultaneous", "factor_quadratic", "diff_squares", "identity_square", "sankalana", "shunyam",
                    "puranapurana", "chalana_quadratic"], [8, 16, 12]),
    ("H. Arithmetic aptitude", ["ratio_share", "average", "simple_interest", "speed", "weighted_average", "profit_loss", "discount", "compound_interest", "time_work", "pipes",
                                "trains", "boats", "partnership", "ages", "cyclicity", "ncr", "probability", "mensuration", "alligation", "calendar"], [12, 34, 10]),
]

TIMED = ["mult_11", "square_end5", "sub_power10", "add_comp", "mult_5_25", "units_sum_10", "nikhilam_below", "pct_of", "times_table", "div_5_25_125",
         "square", "mult_9s", "pct_fraction_trick", "add_ltr", "diff_squares"]

SET_CATEGORIES = [
    ("Foundational arithmetic", ["add_ltr", "add_comp", "sub_power10", "sub_comp", "integers", "simplify_fraction", "pct_of", "divisibility", "add_column",
                                 "add_fractions", "decimal_mult", "lcm_hcf", "estimate_product", "remainder", "exponents"]),
    ("Multiplication and division", ["mult_11", "mult_5_25", "mult_9s", "long_division", "div_5_25_125", "div_by_9", "nikhilam_below", "nikhilam_above", "urdhva_2x2",
                                     "units_sum_10", "mult_101", "nikhilam_mixed", "urdhva_3x3", "div_nikhilam", "div_paravartya", "nikhilam_working_base"]),
    ("Squares, cubes and roots", ["square", "square_end5", "cube", "square_near_base", "square_near_50", "sqrt_perfect", "cbrt_perfect", "identity_square",
                                  "square_duplex", "sqrt_estimate"]),
    ("Algebra and factorisation", ["linear_eq", "expand_binomials", "linear_two_sides", "simultaneous", "factor_quadratic", "diff_squares", "identity_square",
                                   "sankalana", "shunyam", "puranapurana", "chalana_quadratic"]),
    ("Percentages, ratios and averages", ["pct_of", "frac_to_pct", "pct_fraction_trick", "ratio_share", "average", "pct_change", "weighted_average", "profit_loss",
                                          "discount", "partnership", "alligation"]),
    ("Government-exam mixed aptitude", ["bodmas", "simple_interest", "speed", "ratio_share", "pct_change", "profit_loss", "compound_interest", "time_work", "pipes",
                                        "trains", "boats", "ages", "mensuration", "probability", "ncr", "cyclicity", "remainder", "approx_simplify", "alligation"]),
    ("Advanced mental-math challenge", ["urdhva_3x3", "square_duplex", "div_paravartya", "div_nikhilam", "recurring_19", "nikhilam_working_base", "calendar",
                                        "cyclicity", "sankalana", "puranapurana", "square_near_base", "sqrt_estimate", "chalana_quadratic"]),
]

DIFF = ["Beginner"] * 3 + ["Intermediate"] * 4 + ["Advanced"] * 3
SECONDS = {"Beginner": 45, "Intermediate": 75, "Advanced": 120}


def _by_level(keys, level):
    want = LEVEL_ORDER[level]
    exact = [k for k in keys if LEVEL_ORDER[GENERATORS[k][1]] == want]
    near = [k for k in keys if abs(LEVEL_ORDER[GENERATORS[k][1]] - want) == 1]
    return exact or near or keys


def build(name, ctx, st):
    from .render import answer_key, inline, practice_block
    out = []
    sp = ctx.writing_lines if ctx.workbook_mode else 0
    if name == "exercise_bank":
        for title, keys, counts in BANK:
            out += [CondPageBreak(80), Paragraph(inline(title), st["h2"])]
            for level, n in zip(("beginner", "intermediate", "advanced"), counts):
                ks = _by_level(keys, level)
                out += practice_block(f"{','.join(ks)}|{n}|{title.split('. ', 1)[1]} — {level.title()}", ctx, st, sp)
        out += [CondPageBreak(80), Paragraph(inline("I. Mixed-topic drills"), st["h2"])]
        all_keys = [k for _, ks, _ in BANK for k in ks]
        for d in range(4):
            mix = all_keys[d::4]
            out += practice_block(f"{','.join(mix)}|12|Mixed drill {d + 1}", ctx, st, sp)
        out += [CondPageBreak(80), Paragraph(inline("J. Timed mental-math tests (target: 20 questions in 8 minutes; write only the answer)"), st["h2"])]
        for d in range(4):
            out += practice_block(f"{','.join(TIMED[d:] + TIMED[:d])}|20|Timed test {d + 1}", ctx, st, 0)
        out += [CondPageBreak(80), Paragraph(inline("K. Challenge questions"), st["h2"])]
        adv = [k for k in all_keys if GENERATORS[k][1] == "advanced"]
        out += practice_block(f"{','.join(adv)}|20|Challenge set", ctx, st, sp)
        out += [PageBreak()] + answer_key(ctx, st, "Part XII answer key with worked solutions")
        return out
    if name == "practice_sets":
        set_no = 0
        for cat, keys in SET_CATEGORIES:
            out += [PageBreak(), Paragraph(inline(f"{cat} — 10 sets"), st["h2"])]
            for i in range(10):
                set_no += 1
                diff = DIFF[i]
                ks = _by_level(keys, diff.lower())
                rot = ks[i % len(ks):] + ks[:i % len(ks)]
                n = 8
                minutes = max(4, round(n * SECONDS[diff] / 60))
                out += practice_block(f"{','.join(rot)}|{n}|Set {set_no}: {cat} · {diff} · suggested time {minutes} min", ctx, st, sp)
            out += [PageBreak()] + answer_key(ctx, st, f"Answers and explanations — {cat}")
        return out
    raise KeyError(name)
