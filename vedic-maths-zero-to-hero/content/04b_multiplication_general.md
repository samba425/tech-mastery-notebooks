## Chapter 10: Vertically and Crosswise for Any Numbers

### 10.1 Two-digit by two-digit

:::objective
Multiply any two 2-digit numbers mentally, carrying correctly.
:::

[[diagram:urdhva2 47 36]]

:::compare Standard method ||| Vertically and crosswise
**47 × 36**
```calc
     47
   × 36
   ----
    282
   141
   ----
   1692
```
|||
**47 × 36**
Units: 7 × 6 = 42 → 2, carry 4
Cross: 4×6 + 7×3 = 45, +4 = 49 → 9, carry 4
Left: 4 × 3 = 12, +4 = 16
**1,692**
:::

**The carry process.** Work from right to left. Each step produces a number; keep its **units digit** and carry the rest to the next step. The final step is written in full.

| # | Problem | Right (v) | Cross (x) | Left (v) | Answer |
|---|---|---|---|---|---|
| 1 | 21 × 13 | 3 | 1+6 = 7 | 2 | 273 |
| 2 | 32 × 24 | 8 | 12+4 = 16 | 6 | 768 |
| 3 | 54 × 23 | 12 | 15+8 = 23 | 10 | 1,242 |
| 4 | 67 × 89 | 63 | 54+56 = 110 | 48 | 5,963 |
| 5 | 78 × 46 | 48 | 32+42 = 74 | 28 | 3,588 |
| 6 | 95 × 37 | 35 | 63+15 = 78 | 27 | 3,515 |
| 7 | 83 × 83 | 9 | 24+24 = 48 | 64 | 6,889 |
| 8 | 19 × 91 | 9 | 1+81 = 82 | 9 | 1,729 |

:::tip Combine the step values without fuss
A quick way to finish: answer = left × 100 + cross × 10 + right. For 67 × 89: 4,800 + 1,100 + 63 = 5,963.
:::

### 10.2 Three-digit by three-digit

[[diagram:urdhva3]]

:::formula Five steps for (abc) × (def)
1: c·f  2: b·f + c·e  3: a·f + b·e + c·d  4: a·e + b·d  5: a·d
:::

:::example 234 × 512
```calc
Step 1:  4×2                 =  8          → 8, carry 0
Step 2:  3×2 + 4×1           = 10          → 0, carry 1
Step 3:  2×2 + 3×1 + 4×5     = 27, +1 = 28 → 8, carry 2
Step 4:  2×1 + 3×5           = 17, +2 = 19 → 9, carry 1
Step 5:  2×5                 = 10, +1 = 11
Answer: 1,19,808
```
Check by digit sums: 234 → 9 → 0, so the product's digit sum must be 0 (i.e. 9). 1,19,808 → 27 → 9 ✓.
:::

| # | Problem | Step values (5 → 1) | Answer |
|---|---|---|---|
| 9 | 123 × 321 | 3, 8, 14, 8, 3 | 39,483 |
| 10 | 405 × 213 | 8, 4, 22, 5, 15 | 86,265 |
| 11 | 672 × 348 | 18, 45, 82, 64, 16 | 2,33,856 |

:::warn Middle step has three products
The commonest error is forgetting one of a·f, b·e, c·d in step 3. Say them aloud: "outer pair, then middle pair, then… the other outer pair."
:::

:::when When this trick does not apply directly
It always applies — that is its strength. But it is not always the *fastest*: 998 × 997 is quicker with Nikhilam, and 248 × 125 is quicker as 248 × 1,000 ÷ 8 = 31,000. Look at the numbers before choosing.
:::

### 10.3 Different numbers of digits

Pad the shorter number with leading zeros: 243 × 56 = 243 × 056.

:::example 243 × 56
Steps: 3×6 = 18 → 8 c1; 4×6 + 3×5 = 39 +1 = 40 → 0 c4; 2×6 + 4×5 + 3×0 = 32 +4 = 36 → 6 c3; 2×5 + 4×0 = 10 +3 = 13 → 3 c1; 2×0 + 1 = 1 → **13,608**.
:::

## Chapter 11: Special Pairs and Squares

### 11.1 Same leading digits, last digits adding to 10

| # | Problem | Left: a(a + 1) | Right: u × v (2 digits) | Answer |
|---|---|---|---|---|
| 1 | 34 × 36 | 3 × 4 = 12 | 24 | 1,224 |
| 2 | 57 × 53 | 5 × 6 = 30 | 21 | 3,021 |
| 3 | 91 × 99 | 9 × 10 = 90 | 09 | 9,009 |
| 4 | 128 × 122 | 12 × 13 = 156 | 16 | 15,616 |

:::when When this trick does not apply directly
34 × 46 (different tens digits, even though units add to 10) — **does not apply**. Use 40² − 6² = 1,600 − 36 = 1,564 (numbers equidistant from 40), or Urdhva.
A related pattern **does** work: tens digits adding to 10 and **equal** units, e.g. 37 × 77 → left (3 × 7 + 7) is 28, right (7 × 7) is 49, giving **2,849**.
:::

### 11.2 Squaring numbers ending in 5

(a)5² = a(a + 1) | 25. See Sutra 1. Extended examples:

| # | Problem | a × (a + 1) | Answer |
|---|---|---|---|
| 5 | 35² | 3 × 4 = 12 | 1,225 |
| 6 | 85² | 8 × 9 = 72 | 7,225 |
| 7 | 105² | 10 × 11 = 110 | 11,025 |
| 8 | 135² | 13 × 14 = 182 | 18,225 |
| 9 | 0.65² | 6 × 7 = 42 → 4,225 → 4 decimal places | 0.4225 |

### 11.3 Squaring numbers near 50

:::formula (50 + d)² = (25 + d) | d²  (right part: 2 digits)
:::

:::why Why it works
(50 + d)² = 2,500 + 100d + d² = 100(25 + d) + d².
:::

| # | Problem | d | 25 + d | d² | Answer |
|---|---|---|---|---|---|
| 10 | 53² | +3 | 28 | 09 | 2,809 |
| 11 | 58² | +8 | 33 | 64 | 3,364 |
| 12 | 47² | −3 | 22 | 09 | 2,209 |
| 13 | 41² | −9 | 16 | 81 | 1,681 |

### 11.4 Squaring numbers near 100 and 1,000 (Yavadunam)

| # | Problem | n ± d | d² | Answer |
|---|---|---|---|---|
| 14 | 96² | 92 | 16 | 9,216 |
| 15 | 113² | 126 | 169 → carry 1 | 12,769 |
| 16 | 989² | 978 | 121 → 121 | 9,78,121 |
| 17 | 1,016² | 1,032 | 256 | 10,32,256 |

### 11.5 Squaring any number: the duplex method

The **duplex** D of a group of digits is: for one digit, its square; for two digits ab, 2ab; for three digits abc, 2ac + b²; for four digits abcd, 2ad + 2bc.

:::example 347²
Duplexes from the left: D(3) = 9, D(34) = 24, D(347) = 2·3·7 + 4² = 58, D(47) = 56, D(7) = 49.
```calc
column values:  9 | 24 | 58 | 56 | 49
from the right: 49 → 9 c4;  56+4 = 60 → 0 c6;  58+6 = 64 → 4 c6;
                24+6 = 30 → 0 c3;  9+3 = 12
answer: 1,20,409
```
:::

:::when When to use the duplex method
It is a general method for squares and is efficient for 3- and 4-digit numbers once practised. For numbers near a base, Yavadunam is faster; for numbers ending in 5, Ekadhikena is fastest.
:::

## Chapter 12: Decomposition, Decimals, Negatives and Checking

### 12.1 Distributive decomposition

| # | Problem | Decomposition | Answer |
|---|---|---|---|
| 1 | 7 × 64 | 7 × 60 + 7 × 4 = 420 + 28 | 448 |
| 2 | 18 × 35 | 18 × 35 = 9 × 70 (halve and double) | 630 |
| 3 | 49 × 16 | 50 × 16 − 16 | 784 |
| 4 | 125 × 36 | 125 × 4 × 9 = 500 × 9 | 4,500 |
| 5 | 302 × 47 | 300 × 47 + 2 × 47 = 14,100 + 94 | 14,194 |
| 6 | 1.5 × 46 | 46 + 23 | 69 |

### 12.2 Multiplying decimals

:::formula Decimal places add
Ignore the points, multiply the whole numbers, then put in as many decimal places as the two numbers have together.
:::

| # | Problem | Whole-number product | Decimal places | Answer |
|---|---|---|---|---|
| 7 | 0.7 × 0.8 | 56 | 2 | 0.56 |
| 8 | 1.2 × 1.3 | 156 | 2 | 1.56 |
| 9 | 9.8 × 9.7 | 9,506 (Nikhilam) | 2 | 95.06 |
| 10 | 0.25 × 0.48 | 1,200 | 4 | 0.12 |
| 11 | 3.5 × 3.5 | 1,225 | 2 | 12.25 |

:::approx Check decimals by estimation
9.8 × 9.7 ≈ 10 × 10 = 100, so 95.06 is sensible; 9.506 or 950.6 would not be.
:::

### 12.3 Multiplication involving negative numbers

:::formula Sign rules
(+)(+) = + · (−)(−) = + · (+)(−) = − · (−)(+) = −. With several factors: an **even** number of negatives gives +, an **odd** number gives −.
:::

| # | Problem | Sign | Size | Answer |
|---|---|---|---|---|
| 12 | (−6) × 7 | − | 42 | −42 |
| 13 | (−12) × (−11) | + | 132 | 132 |
| 14 | (−2) × (−3) × (−5) | − (three negatives) | 30 | −30 |
| 15 | 25 × (−16) | − | 400 | −400 |

The vinculum (bar-digit) idea uses negatives on purpose: 9 = 1 1̅ (ten minus one), so 39 × 7 = (40 − 1) × 7 = 280 − 7 = **273**.

### 12.4 Checking multiplication

:::formula Four independent checks
1. **Estimate:** round both numbers. 672 × 348 ≈ 700 × 350 = 2,45,000 (actual 2,33,856 ✓ close).
2. **Last digit:** 672 × 348 must end in 6 because 2 × 8 = 16 ✓.
3. **Digit sum (casting out nines):** 672 → 15 → 6; 348 → 15 → 6; 6 × 6 = 36 → 9. 2,33,856 → 27 → 9 ✓.
4. **Casting out elevens:** alternating digit sums from the right also multiply — this catches swapped digits that the nines-check misses.
:::

:::example Catching an error with digit sums
Someone claims that 467 × 38 is 17,646. Digit sums: 8 × 2 = 16 → 7. But 17,646 → 24 → 6 ✗. So the answer is wrong. (Correct: 17,746.)
:::

:::recap Part IV — choose your method
| Numbers look like… | Best method |
|---|---|
| × 5, 25, 50, 125 | Multiply by 10/100/1,000 and divide by 2/4/8 |
| × 9, 99, 999 | Ekanyunena: (n − 1) \| complement |
| × 11 | Neighbour sums |
| Both near 10/100/1,000 | Nikhilam |
| Near 50, 200, 300 | Nikhilam with a working base |
| Same tens, units add to 10 | a(a + 1) \| u·v |
| Ends in 5, squared | a(a + 1) \| 25 |
| Anything else | Vertically and crosswise, or decomposition |
:::

[[practice:urdhva_2x2,urdhva_3x3,units_sum_10,square_end5,square_near_50,square_near_base,square_duplex,mult_decompose,decimal_mult,mult_negative|26|Chapters 10–12 practice]]

:::selftest Part IV mastery checklist
☐ 2-digit × 2-digit in under 15 seconds, mentally ☐ 3-digit × 3-digit on paper in one line ☐ any square from 1 to 100 in under 10 seconds ☐ × 11, × 25, × 99 instantly ☐ check every product with digit sums.
:::

[[answerkey:Chapters 10–12 answer key]]
