## Sutras 5–9: Equations by Inspection

Sutras 5 to 9 are mainly about **solving equations quickly** when they have a special structure. They are clever and worth knowing, but remember: each one only applies to its special case. The ordinary algebra in Part VII always works.

### Sutra 5: Shunyam Saamyasamuccaye — "When the Total is the Same, that Total is Zero"

*Samuccaya* means a "combination" or "total" that appears on both sides of an equation. The sutra says: when the same samuccaya occurs throughout, it must equal **zero**. Tirthaji applies this in several situations; four common ones are below.

:::formula Case 1 — a common factor
If the same expression is a factor of every term, it can be zero. 12x + 3x = 4x + 5x gives 15x = 9x, which forces **x = 0**.
:::

:::formula Case 2 — equal independent terms
(x + a)(x + b) = (x + c)(x + d) with **ab = cd** gives **x = 0**.
Example: (x + 7)(x + 9) = (x + 3)(x + 21). Since 7 × 9 = 63 = 3 × 21, **x = 0**.
In general (ab ≠ cd): x = (cd − ab) ÷ (a + b − c − d).
:::

:::formula Case 3 — equal numerators, equal sums of denominators
1/(x − 4) + 1/(x − 6) = 1/(x − 2) + 1/(x − 8). The denominators on each side add to the same total, 2x − 10. Set it to zero: 2x − 10 = 0, **x = 5**.
Check: 1/1 + 1/(−1) = 0 and 1/3 + 1/(−3) = 0 ✓.
:::

:::formula Case 4 — sum of numerators equals sum of denominators
(2x + 3)/(2x + 5) = (2x + 5)/(2x + 3). Here N₁ + N₂ = 4x + 8 and D₁ + D₂ = 4x + 8 — the same. Set 4x + 8 = 0: **x = −2**.
Check: (−1)/1 = 1/(−1) ✓.
:::

:::warn Use the exact pattern only
These rules are **pattern-matching**. If the pattern does not match exactly, the rule gives a wrong answer. Always substitute your answer back into the original equation to check, and watch for values that make a denominator zero.
:::

### Sutra 6: (Anurupye) Shunyamanyat — "If One is in Ratio, the Other is Zero"

For simultaneous equations, if the coefficients of one variable are in the **same ratio** as the constants, then the **other** variable is zero.

:::example 3x + 7y = 2 and 4x + 14y = 4
The y-coefficients 7 : 14 = 1 : 2 and the constants 2 : 4 = 1 : 2 — the same ratio. So **x = 0**. Then 7y = 2, giving **y = 2/7**.
Check: 4(0) + 14(2/7) = 4 ✓.
:::

:::when
Look for this before starting elimination. It saves time in exam questions that are designed with this pattern, but it applies **only** when the ratios match exactly.
:::

### Sutra 7: Sankalana-Vyavakalanabhyam — "By Addition and by Subtraction"

When the coefficients of x and y are **swapped** between two equations, add the equations and subtract them.

:::example 45x − 23y = 113 and 23x − 45y = 91
**Add:** 68x − 68y = 204 → x − y = 3.
**Subtract:** 22x + 22y = 22 → x + y = 1.
So x = (3 + 1)/2 = **2** and y = (1 − 3)/2 = **−1**.
Check: 45(2) − 23(−1) = 90 + 23 = 113 ✓; 23(2) − 45(−1) = 46 + 45 = 91 ✓.
:::

:::why Why it works
For ax + by = p and bx + ay = q, adding gives (a + b)(x + y) = p + q and subtracting gives (a − b)(x − y) = p − q. Two easy equations replace two awkward ones.
:::

### Sutra 8: Puranapuranabhyam — "By Completion or Non-completion"

This sutra means **completing** an expression into a perfect square or cube. Completing the square is a standard school technique; Tirthaji extends it to cubes.

:::example x³ + 6x² + 11x + 6 = 0
(x + 2)³ = x³ + 6x² + 12x + 8. Our cubic is (x + 2)³ − (x + 2), because subtracting x + 2 takes 12x to 11x and 8 to 6.
Let y = x + 2: y³ − y = 0 → y(y − 1)(y + 1) = 0 → y = 0, 1, −1 → **x = −2, −1, −3**.
:::

:::example Completing the square: x² + 6x − 7 = 0
x² + 6x = 7 → x² + 6x + 9 = 16 → (x + 3)² = 16 → x + 3 = ±4 → **x = 1 or x = −7**.
:::

### Sutra 9: Chalana-Kalanabhyam — "Differences and Similarities"

Tirthaji uses this sutra for ideas from calculus. Its most practical use is a quick way to solve quadratic equations.

:::formula For ax² + bx + c = 0
The "first differential" 2ax + b equals **±√(b² − 4ac)**.
This is the quadratic formula rearranged: x = (−b ± √(b² − 4ac)) ÷ 2a.
:::

:::example x² − 5x + 6 = 0
2x − 5 = ±√(25 − 24) = ±1 → 2x = 6 or 4 → **x = 3 or 2**.
:::

:::example 2x² + 3x − 9 = 0
4x + 3 = ±√(9 + 72) = ±9 → 4x = 6 or −12 → **x = 3/2 or −3**.
:::

:::note Interpretations vary
Some teaching sources describe Chalana-Kalanabhyam differently (for example, as finding factors by comparing differences). The quadratic method above is the application given in Tirthaji's book and is mathematically identical to the quadratic formula.
:::

## Sutras 10–16: Squares, Decimals, Nines and Checking

### Sutra 10: Yavadunam — "Whatever the Extent of its Deficiency"

*Yavadunam* (with the sub-sutra *Yavadunam Tavadunikritya Varganca Yojayet*: "lessen by the deficiency and set up the square of the deficiency") squares numbers close to a base.

:::formula Squaring near a base
n² = (n + deviation) | (deviation)², where the right part has as many digits as the base has zeros.
:::

:::example Solved examples
1. **97²** (base 100, deficiency 3): 97 − 3 = 94 | 3² = 09 → **9,409**
2. **108²** (excess 8): 108 + 8 = 116 | 64 → **11,664**
3. **88²** (deficiency 12): 88 − 12 = 76 | 144 → carry 1 → **7,744**
4. **994²** (base 1,000, −6): 988 | 036 → **9,88,036**
5. **1,025²** (+25): 1,050 | 625 → **10,50,625**
:::

:::why Why it works
This is Nikhilam multiplication with both numbers equal: (B + d)² = B(B + 2d) + d² = B × (n + d) + d².
:::

### Sutra 11: Vyashtisamanstih — "Part and Whole"

The idea is to treat a quantity either as a **whole** or as **parts**, whichever is easier. Teaching sources apply this in different ways; two widely taught uses are:

:::example Multiplication by the average (product of numbers equidistant from a middle value)
47 × 53: the whole (average) is 50; each part differs by 3. So 47 × 53 = 50² − 3² = 2,500 − 9 = **2,491**.
68 × 72 = 70² − 2² = 4,900 − 4 = **4,896**.
:::

:::example Averages by deviations
Average of 62, 67, 58, 71, 64: take 60 as the "whole" and average only the deviations (2, 7, −2, 11, 4 → total 22 → 22/5 = 4.4). Average = **64.4**.
:::

:::note Interpretations vary
Tirthaji's own uses of this sutra include factorising expressions by splitting them into parts. The two methods above are the most common in modern teaching. Both are standard algebra (a + b)(a − b) = a² − b² and the "assumed mean" method.
:::

### Sutra 12: Shesanyankena Charamena — "The Remainders by the Last Digit"

This sutra converts fractions such as 1/7, 1/13 and 1/17 into recurring decimals.

:::example 1/7
Successive remainders when 10, 100, 1,000 … are divided by 7 are **3, 2, 6, 4, 5, 1** (then they repeat).
Multiply each remainder by the last digit of 7 (which is 7) and keep only the units digit:
3×7 = 21 → 1; 2×7 = 14 → 4; 6×7 = 42 → 2; 4×7 = 28 → 8; 5×7 = 35 → 5; 1×7 = 7 → 7.
**1/7 = 0.142857 142857…**
:::

:::example 1/13
Remainders: 10, 9, 12, 3, 4, 1. Multiply by 3 and keep units: 0, 7, 6, 9, 2, 3.
**1/13 = 0.076923 076923…**
:::

:::tip Multiples of 1/7 are rotations
2/7 = 0.285714…, 3/7 = 0.428571…, 6/7 = 0.857142… — always the same six digits 1, 4, 2, 8, 5, 7, starting at a different place.
:::

### Sutra 13: Sopantyadvayamantyam — "The Ultimate and Twice the Penultimate"

This sutra solves a special family of equations: when the four factors in the denominators form an **arithmetic progression** (like x + 2, x + 3, x + 4, x + 5) and are arranged as
1/(AB) + 1/(AC) = 1/(AD) + 1/(BC),
then **ultimate + 2 × penultimate = 0**, i.e. D + 2C = 0.

:::example 1/((x+2)(x+3)) + 1/((x+2)(x+4)) = 1/((x+2)(x+5)) + 1/((x+3)(x+4))
Factors x + 2, x + 3, x + 4, x + 5 (an arithmetic progression). Ultimate D = x + 5, penultimate C = x + 4.
(x + 5) + 2(x + 4) = 0 → 3x + 13 = 0 → **x = −13/3**.
(Verified by substitution with exact fractions.)
:::

:::warn Very special case
This only works for exactly this arrangement. It is included for completeness; you will rarely need it outside Vedic Maths competitions.
:::

### Sutra 14: Ekanyunena Purvena — "By One Less than the Previous One"

This is the partner of Sutra 1. Use it to multiply by **9, 99, 999 …** when the other number has the **same number of digits** as the nines (or fewer).

:::formula n × 99…9 (same number of digits)
Left part: n − 1. Right part: the nines minus the left part (i.e. "all from 9 and last from 10" applied to n).
:::

:::example Solved examples
1. 7 × 9 → 6 | 3 → **63**
2. 43 × 99 → 42 | 57 → **4,257**
3. 768 × 999 → 767 | 232 → **7,67,232**
4. 46 × 999 (fewer digits): think 046 → 045 | 954 → **45,954**
5. 1,234 × 9,999 → 1,233 | 8,766 → **1,23,38,766**
:::

:::when
**Not directly** when the multiplicand has *more* digits than the nines (e.g. 456 × 99). Then use 456 × 100 − 456 = 45,600 − 456 = **45,144**, which is always valid.
:::

### Sutra 15: Gunitasamuccayah — "The Product of the Sum is the Sum of the Product"

In algebra: the sum of the coefficients of a product equals the product of the sums of the coefficients of its factors. This gives a quick **check** for multiplication and factorisation.

:::example Checking (x + 2)(x + 3) = x² + 5x + 6
Coefficient sums of the factors: (1 + 2) = 3 and (1 + 3) = 4 → 3 × 4 = 12.
Coefficient sum of the product: 1 + 5 + 6 = 12 ✓.
:::

The same idea works for numbers using **digit sums** (Beejank). This is often called *casting out nines*.

:::formula The digit-sum check
Find the digit sum (repeat until one digit; 9 counts as 0) of each number. Do the same operation on the digit sums. The result must match the digit sum of your answer.
:::

:::example Checking 467 × 38 = 17,746
467 → 4 + 6 + 7 = 17 → 8. 38 → 11 → 2. 8 × 2 = 16 → 7.
17,746 → 1 + 7 + 7 + 4 + 6 = 25 → 7 ✓.
:::

:::warn What the check cannot catch
If two digits are swapped (17,746 written as 17,476) the digit sum is unchanged, so the check passes even though the answer is wrong. The digit-sum check catches most errors, not all. Combine it with an estimate.
:::

### Sutra 16: Gunakasamuccayah — "The Factors of the Sum is Equal to the Sum of the Factors"

Tirthaji uses this sutra in connection with derivatives of factorised expressions: if a quadratic factorises as (x + a)(x + b), its first differential 2x + (a + b) equals the **sum of the factors** (x + a) + (x + b).

:::example x² + 7x + 12 = (x + 3)(x + 4)
Differential: 2x + 7. Sum of factors: (x + 3) + (x + 4) = 2x + 7 ✓. This confirms the factorisation.
:::

:::note Interpretations vary
This sutra has fewer standard school applications than the others. Treat it as a checking idea.
:::

## The 13 Sub-sutras

| # | Sub-sutra | Common English meaning | Typical application |
|---|---|---|---|
| 1 | Anurupyena | Proportionately | Working bases (50, 200 …) — scale the left part |
| 2 | Sisyate Sesasamjnah | The remainder remains constant | Remainders in division |
| 3 | Adyamadyenantyamantyena | The first by the first and the last by the last | Factorising quadratics: first terms and last terms |
| 4 | Kevalaih Saptakam Gunyat | For 7, the multiplier is 143 | 7 × 143 = 1,001, used for division by 7 and divisibility |
| 5 | Vestanam | By osculation | Divisibility tests for 7, 13, 17, 19 … |
| 6 | Yavadunam Tavadunam | Lessen by the deficiency | Squares and cubes near a base |
| 7 | Yavadunam Tavadunikritya Varganca Yojayet | Lessen by the deficiency and set up the square | Squaring near a base (Sutra 10) |
| 8 | Antyayordasake'pi | Last digits totalling 10 | 43 × 47 type products (Sutra 1B) |
| 9 | Antyayoreva | Only the last terms | Some fraction equations |
| 10 | Samuccayagunitah | The sum of the coefficients in the product | Checking products (with Sutra 15) |
| 11 | Lopanasthapanabhyam | By alternate elimination and retention | Factorising expressions in several variables |
| 12 | Vilokanam | By mere observation | Solving equations by inspection |
| 13 | Gunitasamuccayah Samuccayagunitah | The product of the sum is the sum of the product | Checking factorisations |

:::example Sub-sutra 4: why 143 helps with 7
7 × 143 = 1,001, and 1,001 = 7 × 11 × 13. So a number like abc,abc (e.g. 365,365) is divisible by 7, 11 and 13: 365,365 = 365 × 1,001.
:::

:::example Sub-sutra 5: osculation test for 7
For 7, the "osculator" is 2 (subtract twice the last digit from the rest). Is 343 divisible by 7? 34 − 2 × 3 = 28, and 28 = 7 × 4 ✓. Is 1,001 divisible by 7? 100 − 2 = 98 → 9 − 16 = −7 ✓.
:::

:::example Sub-sutra 3: first by first and last by last
Factorise 6x² + 11x + 3. Split the first term 6x² = 2x × 3x and the last 3 = 3 × 1, then arrange so that the crosswise products add to the middle term: (2x + 3)(3x + 1) → 2x + 9x = 11x ✓.
:::

:::history A note on the sub-sutras
Lists of sub-sutras in different books vary slightly in spelling and order, and some applications are attributed differently. The meanings above follow the commonly reproduced list from Tirthaji's book.
:::

:::recap Part II quick revision
- **Ekadhikena:** (a)5² = a(a + 1) | 25. Same tens, units add to 10: a(a + 1) | u×v.
- **Nikhilam:** all from 9, last from 10. Near a base: cross-add | multiply deviations.
- **Urdhva:** vertical – cross – vertical (2 digits); 1–2–3–2–1 products (3 digits).
- **Paravartya:** above the base → negative flags; x = (d − b)/(a − c).
- **Yavadunam:** n² = (n + d) | d².
- **Ekanyunena:** n × 99…9 = (n − 1) | complement.
- **Gunitasamuccayah:** digit-sum and coefficient-sum checks.
- Sutras 5–9, 11–13, 16: special patterns — check by substitution.
:::

[[practice:shunyam,sankalana,puranapurana,chalana_quadratic,square_near_base,mult_9s,factor_quadratic,recurring_19|16|Practice: Sutras 5–16]]

[[answerkey:Sutras 5–16 answer key]]
