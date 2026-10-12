# Part IV — Multiplication from Basic to Advanced

Multiplication is where Vedic methods shine most. This part moves from tables and patterns, through special multipliers (5, 9, 11, 25, 99, 125 …), to the base methods and the universal vertically-and-crosswise method. Every method shows the **standard** working beside the **shortcut**, the **carry** process, and a box headed **"When this trick does not apply directly"**.

## Chapter 8: Tables, Patterns and Special Multipliers

### 8.1 Multiplication tables and number patterns

[[table:times 11 20 10]]

:::tip Building the teens tables from what you know
13 × 7 = 10 × 7 + 3 × 7 = 70 + 21 = 91. Any "teen × single digit" is (10 × digit) + (units × digit). With practice the 11–20 tables become as easy as 1–10.
:::

:::tip Patterns worth noticing
- The units digits of the 4-table repeat 4, 8, 2, 6, 0.
- Multiples of 9 have digit sums of 9 (or a multiple of 9).
- n × (n + 1) is always even; n² − 1 = (n − 1)(n + 1).
:::

### 8.2 Multiplying by 10, 100, 1,000 and powers of 10

:::formula Shifting place value
× 10 → every digit moves **one place left** (write one zero, or move the decimal point one place right).
× 100 → two places; × 1,000 → three places; × 10ⁿ → n places.
:::

:::example Solved examples
1. 47 × 10 = 470
2. 3.6 × 100 = 360
3. 0.052 × 1,000 = 52
4. 245 × 10,000 = 24,50,000
5. 4.7 × 10⁵ = 4,70,000
:::

:::warn Not "add a zero" for decimals
2.5 × 10 is 25, not 2.50. Think of moving the **digits** (or the point), not of adding zeros.
:::

### 8.3 Multiplying by 5, 25, 50 and 125

:::formula Divide instead of multiply
5 = 10 ÷ 2 · 25 = 100 ÷ 4 · 50 = 100 ÷ 2 · 125 = 1,000 ÷ 8
:::

:::compare Standard method ||| Shortcut
**68 × 25**
```calc
    68
  × 25
  ----
   340
  1360
  ----
  1700
```
|||
**68 × 25**
68 × 100 = 6,800
6,800 ÷ 4 = **1,700**
(or: 68 ÷ 4 = 17, then × 100)
:::

| # | Problem | Shortcut working | Answer |
|---|---|---|---|
| 1 | 486 × 5 | 4,860 ÷ 2 | 2,430 |
| 2 | 37 × 5 | 370 ÷ 2 | 185 |
| 3 | 84 × 25 | 84 ÷ 4 = 21, × 100 | 2,100 |
| 4 | 37 × 25 | 3,700 ÷ 4 | 925 |
| 5 | 68 × 50 | 6,800 ÷ 2 | 3,400 |
| 6 | 64 × 125 | 64 ÷ 8 = 8, × 1,000 | 8,000 |
| 7 | 36 × 125 | 36,000 ÷ 8 | 4,500 |
| 8 | 4.8 × 25 | 480 ÷ 4 | 120 |
| 9 | 125 × 72 | 72 ÷ 8 = 9, × 1,000 | 9,000 |
| 10 | 25 × 25 | 2,500 ÷ 4 | 625 |

:::when When this trick does not apply directly
It always gives the right answer, but it is only *faster* when the other number divides easily by 2, 4 or 8. For 37 × 125, 37,000 ÷ 8 = 4,625 needs a careful division — still fine, but not instant.
:::

### 8.4 Multiplying by 9, 99, 999 (Ekanyunena Purvena)

:::formula Same number of digits as the nines
n × 99…9 = (n − 1) | (complement of n). The right part has as many digits as there are nines.
:::

| # | Problem | Left: n − 1 | Right: 99… − left | Answer |
|---|---|---|---|---|
| 11 | 8 × 9 | 7 | 2 | 72 |
| 12 | 57 × 99 | 56 | 43 | 5,643 |
| 13 | 23 × 99 | 22 | 77 | 2,277 |
| 14 | 846 × 999 | 845 | 154 | 8,45,154 |
| 15 | 98 × 99 | 97 | 02 | 9,702 |

:::why Why it works
n × 99 = n × 100 − n = 100(n − 1) + (100 − n). The left part is n − 1; the right part is 100 − n, which equals 99 − (n − 1).
:::

:::when When this trick does not apply directly
If the number has **more digits** than the nines (e.g. 345 × 99), the left/right split does not hold. Use **n × 100 − n**: 34,500 − 345 = **34,155**. If it has **fewer** digits (7 × 99), pad with zeros: 07 × 99 → 06 | 93 → **693**.
:::

### 8.5 Multiplying by 11

:::formula The "neighbour sum" rule
Write the first digit, then the sum of each pair of neighbouring digits, then the last digit. Carry when a sum is 10 or more.
:::

:::compare Standard method ||| Shortcut
**352 × 11**
```calc
    352
  ×  11
  -----
    352
   3520
  -----
   3872
```
|||
**352 × 11**
3 | 3+5 | 5+2 | 2
3 | 8 | 7 | 2 = **3,872**
:::

**The carry process (789 × 11):** write 7 | 7+8 | 8+9 | 9 = 7 | 15 | 17 | 9. From the right: 9; 17 → write 7, carry 1; 15 + 1 = 16 → write 6, carry 1; 7 + 1 = 8. **789 × 11 = 8,679.**

| # | Problem | Neighbour sums | Answer |
|---|---|---|---|
| 16 | 43 × 11 | 4 \| 7 \| 3 | 473 |
| 17 | 75 × 11 | 7 \| 12 \| 5 → carry | 825 |
| 18 | 99 × 11 | 9 \| 18 \| 9 → carry | 1,089 |
| 19 | 2,314 × 11 | 2 \| 5 \| 4 \| 5 \| 4 | 25,454 |
| 20 | 6,789 × 11 | 6 \| 13 \| 15 \| 17 \| 9 → carries | 74,679 |

:::tip Multiplying by 111 and 22
**× 111:** add digits in groups of three. 32 × 111 → 3 | 3+2 | 3+2 | 2 → 3,552.
**× 22:** multiply by 11, then double. 34 × 22 = 374 × 2 = 748.
:::

:::when When this trick does not apply directly
The rule is for **11** exactly. For 12 or 13, use Paravartya ideas or distribution: 47 × 12 = 470 + 94 = 564.
:::

### 8.6 Multiplying by 101, 1,001 and similar

:::formula
n × 101 = n × 100 + n. For a two-digit n, just write it twice: 47 × 101 = 4,747.
n × 1,001 = n × 1,000 + n. For a three-digit n, write it twice: 365 × 1,001 = 3,65,365.
:::

| # | Problem | Working | Answer |
|---|---|---|---|
| 21 | 47 × 101 | 4,700 + 47 | 4,747 |
| 22 | 236 × 101 | 23,600 + 236 | 23,836 |
| 23 | 8 × 101 | 800 + 8 | 808 |
| 24 | 365 × 1,001 | 3,65,000 + 365 | 3,65,365 |

:::warn Writing twice only works when the digits fit
236 × 101 is **not** 236236. A three-digit number times 101 overlaps: 23,600 + 236 = 23,836.
:::

## Chapter 9: Numbers Close to 10, 100 and 1,000 (Nikhilam)

### 9.1 The method

:::objective
Multiply two numbers that are both near the same base, in one line.
:::

[[diagram:nikhilam 104 97 100]]

[[flow: Choose the base | Write each deviation (+ or −) | Right = deviation × deviation | Left = number + other deviation | Fix digits and carries]]

:::compare Standard method ||| Nikhilam
**98 × 97**
```calc
     98
   × 97
   ----
    686
   882
   ----
   9506
```
|||
**98 × 97** (base 100)
Deviations −2, −3
Right: (−2)(−3) = 06
Left: 98 − 3 = 95
**9,506**
:::

### 9.2 Both numbers below the base

| # | Problem | Deviations | Left | Right | Answer |
|---|---|---|---|---|---|
| 1 | 9 × 8 | −1, −2 | 7 | 2 | 72 |
| 2 | 96 × 93 | −4, −7 | 89 | 28 | 8,928 |
| 3 | 89 × 91 | −11, −9 | 80 | 99 | 8,099 |
| 4 | 86 × 87 | −14, −13 | 73 | 182 → carry 1 | 7,482 |
| 5 | 993 × 989 | −7, −11 | 982 | 077 | 9,82,077 |

### 9.3 Both numbers above the base

| # | Problem | Deviations | Left | Right | Answer |
|---|---|---|---|---|---|
| 6 | 12 × 13 | +2, +3 | 15 | 6 | 156 |
| 7 | 104 × 108 | +4, +8 | 112 | 32 | 11,232 |
| 8 | 111 × 112 | +11, +12 | 123 | 132 → carry 1 | 12,432 |
| 9 | 1,007 × 1,015 | +7, +15 | 1,022 | 105 | 10,22,105 |

### 9.4 One above, one below

The right part is **negative**. Subtract it from (left × base).

:::example 104 × 97
Deviations +4 and −3. Right = −12. Left = 104 − 3 = 101.
Answer = 101 × 100 − 12 = 10,100 − 12 = **10,088**.
:::

| # | Problem | Left | Right | Calculation | Answer |
|---|---|---|---|---|---|
| 10 | 108 × 95 | 103 | −40 | 10,300 − 40 | 10,260 |
| 11 | 112 × 93 | 105 | −84 | 10,500 − 84 | 10,416 |
| 12 | 1,004 × 998 | 1,002 | −8 | 10,02,000 − 8 | 10,01,992 |

### 9.5 Numbers near 10 (the finger-friendly version)

For single digits near 10: 7 × 8 → deviations −3, −2 → left 7 − 2 = 5, right 6 → **56**. This is a lovely way for children to check tables above 5 × 5.

### 9.6 Working bases: near 50, 200, 300, 500

:::formula Working base = multiplier × power of 10
Find the left part as usual, then **multiply** it by the multiplier (for bases like 200 = 2 × 100) or **divide** it (for 50 = 100 ÷ 2), and attach the right part with the correct number of digits.
:::

| # | Problem | Base | Left | × or ÷ | Right | Answer |
|---|---|---|---|---|---|---|
| 13 | 52 × 54 | 50 = 5 × 10 | 56 | × 5 = 280 | 8 → 280 \| 8 | 2,808 |
| 14 | 46 × 43 | 50 = 5 × 10 | 39 | × 5 = 195 | 28 → carry 2 | 1,978 |
| 15 | 212 × 207 | 200 = 2 × 100 | 219 | × 2 = 438 | 84 | 43,884 |
| 16 | 304 × 296 | 300 = 3 × 100 | 300 | × 3 = 900 | −16 | 89,984 |

:::why Why it works
With base B = m × 10ᵏ: (B + a)(B + b) = B(B + a + b) + ab = m × (B + a + b) × 10ᵏ + ab. So the left part is multiplied by m and the right part fills k digits.
:::

:::warn Common mistakes with working bases
- Forgetting to multiply (or divide) the left part.
- Using the wrong number of digits on the right: for base 50 = 5 × 10, the right part has **one** digit; for 200 = 2 × 100 it has **two**.
:::

:::when When this trick does not apply directly
- Numbers on **different bases**: 12 × 97 — no shared base helps. Use vertically and crosswise or distribution (12 × 97 = 1,200 − 36 = 1,164).
- Deviations **too large**: 63 × 78 on base 100 gives right = 37 × 22 = 814, a big carry; and on base 50 left = 91 × 5 = 455, right = 13 × 28 = 364 → still a heavy carry. Use Urdhva.
- A rough guide: Nikhilam is ideal when both deviations are single digits or small two-digit numbers.
:::

[[practice:mult_5_25,mult_9s,mult_11,mult_101,nikhilam_below,nikhilam_above,nikhilam_mixed,nikhilam_working_base|24|Chapters 8–9 practice]]

[[answerkey:Chapters 8–9 answer key]]
