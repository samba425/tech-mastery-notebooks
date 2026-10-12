# Part V — Division and Remainders

Division is the operation learners fear most, but it is simply multiplication in reverse. This part starts with long division (which always works), then shows the special divisors where shortcuts genuinely help — and clearly says where they do not.

## Chapter 13: Division Fundamentals

### 13.1 Long division, step by step

:::objective
Divide any whole number by a one- or two-digit divisor, and state the quotient and remainder correctly.
:::

[[flow: Divide: how many times? | Multiply: divisor × that digit | Subtract | Bring down the next digit | Repeat until no digits remain]]

:::example 7,385 ÷ 23
```calc
        3 2 1
     -------
 23 ) 7 3 8 5
      6 9          23 × 3 = 69
      ---
        4 8        73 − 69 = 4, bring down 8
        4 6        23 × 2 = 46
        ---
          2 5      48 − 46 = 2, bring down 5
          2 3      23 × 1 = 23
          ---
            2      remainder
```
**Quotient 321, remainder 2.** Check: 23 × 321 + 2 = 7,383 + 2 = 7,385 ✓.
:::

:::formula Division check
Dividend = Divisor × Quotient + Remainder, with 0 ≤ Remainder < Divisor.
:::

:::warn Common long-division mistakes
- **Missing zero in the quotient.** 6,024 ÷ 6 = 1,004, not 14. When the divisor does not go into the current number, write 0 in the quotient before bringing down the next digit.
- **Remainder bigger than the divisor.** If it happens, the quotient digit was too small.
:::

### 13.2 Quotient, remainder and decimals

When a division does not come out exactly, you can either state a remainder or continue into decimals by adding zeros after the decimal point.

:::example 47 ÷ 8
As quotient and remainder: 47 = 8 × 5 + 7 → **5 remainder 7**.
As a decimal: 47 ÷ 8 = 5.875 (because 7/8 = 0.875).
As a mixed number: **5 7/8**.
:::

### 13.3 Decimal division

:::formula Make the divisor a whole number
Move the decimal point in the divisor to the end, and move the dividend's point the **same number of places**.
2.56 ÷ 0.16 → 256 ÷ 16 = 16.  4.5 ÷ 0.009 → 4,500 ÷ 9 = 500.
:::

| # | Problem | Rewrite | Answer |
|---|---|---|---|
| 1 | 7.2 ÷ 0.8 | 72 ÷ 8 | 9 |
| 2 | 0.144 ÷ 1.2 | 1.44 ÷ 12 | 0.12 |
| 3 | 15 ÷ 0.25 | 1,500 ÷ 25 | 60 |
| 4 | 3.6 ÷ 0.04 | 360 ÷ 4 | 90 |

## Chapter 14: Shortcuts for Special Divisors

### 14.1 Dividing by 5, 25, 50 and 125

:::formula Multiply instead of divide
÷ 5 = × 2 ÷ 10 · ÷ 25 = × 4 ÷ 100 · ÷ 50 = × 2 ÷ 100 · ÷ 125 = × 8 ÷ 1,000
:::

:::compare Standard method ||| Shortcut
**1,350 ÷ 25**
Long division: 25 into 135 goes 5 times (125), remainder 10; bring down 0 → 100; 25 into 100 goes 4 → **54**.
|||
**1,350 ÷ 25**
1,350 × 4 = 5,400
5,400 ÷ 100 = **54**
:::

| # | Problem | Shortcut | Answer |
|---|---|---|---|
| 5 | 347 ÷ 5 | 694 ÷ 10 | 69.4 |
| 6 | 2,375 ÷ 25 | 9,500 ÷ 100 | 95 |
| 7 | 735 ÷ 50 | 1,470 ÷ 100 | 14.7 |
| 8 | 3,000 ÷ 125 | 24,000 ÷ 1,000 | 24 |
| 9 | 1,234 ÷ 125 | 9,872 ÷ 1,000 | 9.872 |

### 14.2 Dividing by 9 (Nikhilam)

:::formula Running totals
For a dividend with digits d₁ d₂ … d_{n}: the quotient digits are the running totals d₁, d₁+d₂, …; the remainder is the total of **all** digits. Then resolve carries and reduce the remainder below 9.
:::

:::example 2,341 ÷ 9
```calc
  9 | 2   3   4 | 1
    |     2   5 | 9        running totals: 2, 2+3 = 5, 5+4 = 9; remainder 9+1 = 10
    |-----------|---
      2   5   9 | 10
```
Quotient 259, remainder 10. Since 10 ≥ 9: quotient **260**, remainder **1**. Check: 9 × 260 + 1 = 2,341 ✓.
:::

:::tip The remainder alone
The remainder when dividing by 9 is just the digit sum (reduced). 2,341 → 2 + 3 + 4 + 1 = 10 → 1. This is the fastest remainder trick in all of mathematics.
:::

### 14.3 Dividing by 11

Use Paravartya: 11 = 10 + 1, so the flag is **−1**. Each new column = next digit − previous column value.

:::example 7,546 ÷ 11
Columns: 7; 5 − 7 = −2; 4 − (−2) = 6; remainder column 6 − 6 = 0.
Quotient columns 7, −2, 6 → 700 − 20 + 6 = **686**, remainder **0**. Check: 11 × 686 = 7,546 ✓.
:::

:::tip Remainder on division by 11
Alternate sum of digits from the right: for 7,546 → 6 − 4 + 5 − 7 = 0 → remainder 0. If the result is negative, add 11.
:::

### 14.4 Dividing by numbers just below a power of 10 (8, 89, 98, 997 …)

Use Nikhilam division with the complement (see Sutra 2D for full detail).

:::example 10,512 ÷ 97
Complement 03. Split 105 | 12.
```calc
  97 | 1   0   5 |  1   2
  03 |     0   3 |              ← column 1 value (1) × 03
     |         0 |  0           ← column 2 value (0) × 03
     |           |  0  24       ← column 3 value (8) × 03
     |-----------|--------
       1   0   8 |  1  26
```
Track the **column totals** from left to right:
Column 1 = 1. Column 2 = 0 + 1×0 = 0. Column 3 = 5 + 1×3 + 0×0 = 8. Column 4 = 1 + 0×3 + 8×0 = 1. Column 5 = 2 + 8×3 = 26.
Quotient part 1, 0, 8 → **108**; remainder part 1, 26 → 10 + 26 = **36**. Check: 97 × 108 + 36 = 10,476 + 36 = 10,512 ✓.
:::

:::warn Keep track of columns
Each quotient column's value is multiplied by **every** complement digit, which is added to the columns that follow. Writing the column totals in a row (as above) is far less error-prone than writing many small products.
:::

### 14.5 Dividing by 99 and 101

:::formula ÷ 99 for a four-digit number abcd
Quotient = ab; remainder = ab + cd. If the remainder ≥ 99, add 1 to the quotient and subtract 99 from the remainder.
4,567 ÷ 99 → quotient 45, remainder 45 + 67 = 112 → quotient **46**, remainder **13**.
:::

:::formula ÷ 101 for a four-digit number abcd
Quotient = ab; remainder = cd − ab. If negative, subtract 1 from the quotient and add 101.
5,353 ÷ 101 → quotient 53, remainder 53 − 53 = 0 → **53**.
6,120 ÷ 101 → quotient 61, remainder 20 − 61 = −41 → quotient **60**, remainder **60**. Check: 101 × 60 + 60 = 6,120 ✓.
:::

### 14.6 Dividing by numbers just above a power of 10 (12, 13, 112 …)

See Paravartya (Sutra 4). Example: 1,452 ÷ 12 = 121; 13,789 ÷ 112 = 123 remainder 13.

:::when When the shortcuts do not apply directly
- Divisors like **17, 23, 47, 73** are not close to a base. Use ordinary long division — it is clearer and just as fast.
- Paravartya with large flags (e.g. ÷ 18 = 10 + 8, flag −8) creates big negative columns. Use long division or Nikhilam with base 20 only if you are experienced.
- **Do not force a shortcut** when ordinary division is clearer.
:::

## Chapter 15: Divisibility, Checking and Exam Tricks

### 15.1 Divisibility rules (complete table)

[[table:divisibility]]

:::example Osculation test for 7 (sub-sutra Vestanam)
Is 2,149 divisible by 7? 214 − 2 × 9 = 196 → 19 − 2 × 6 = 7 ✓. So 2,149 = 7 × 307.
:::

:::example Test for 13 (add 4 × last digit)
Is 1,183 divisible by 13? 118 + 4 × 3 = 130 → 13 + 0 = 13 ✓. So 1,183 = 13 × 91.
:::

### 15.2 Checking division with multiplication

Every division gives you a free check: **divisor × quotient + remainder = dividend.** In an exam, check by estimating: 7,385 ÷ 23 ≈ 7,000 ÷ 20 = 350 — so 321 is reasonable, but 32 or 3,210 are not.

### 15.3 Exam-oriented division tricks

| Divide by | Instead | Example |
|---|---|---|
| 0.5 | multiply by 2 | 37 ÷ 0.5 = 74 |
| 0.25 | multiply by 4 | 18 ÷ 0.25 = 72 |
| 1.25 | multiply by 0.8 | 60 ÷ 1.25 = 48 |
| 12.5 | multiply by 0.08 | 450 ÷ 12.5 = 36 |
| 1.5 | multiply by 2/3 | 27 ÷ 1.5 = 18 |
| 2.5 | multiply by 0.4 | 35 ÷ 2.5 = 14 |
| 33 1/3 | multiply by 3, ÷ 100 | 250 ÷ 33 1/3 = 7.5 |

:::tip Cancelling before dividing
In fraction-style questions like (84 × 45) ÷ (35 × 36), cancel common factors first: 84/35 = 12/5 and 45/36 = 5/4, so the answer is 12/5 × 5/4 = 3. No large multiplication needed.
:::

:::approx Estimating quotients for options
(4,987 ÷ 24.9) ≈ 5,000 ÷ 25 = 200. If the options are 150, 200, 250, 300, choose 200 without dividing exactly. Use this **only** when the options are well separated.
:::

### 15.4 Common errors and how to correct them

| Error | Example | Fix |
|---|---|---|
| Missing zero in quotient | 3,612 ÷ 12 written as 31 | Each "does not go" step gives a 0: answer 301 |
| Moving decimal points unequally | 4.8 ÷ 0.12 treated as 48 ÷ 12 | Move both points 2 places: 480 ÷ 12 = 40 |
| Remainder too large | 50 ÷ 7 = 6 remainder 8 | Remainder must be < 7: 7 remainder 1 |
| Confusing a ÷ b with b ÷ a | "share 5 among 20" | Read carefully: 5 ÷ 20 = 0.25 each |

:::recap Part V summary
- Dividend = divisor × quotient + remainder.
- ÷ 5, 25, 50, 125 → × 2, 4, 2, 8 and shift the point.
- ÷ 9: running digit totals; remainder = digit sum.
- ÷ 11: flag −1; remainder from the alternating digit sum.
- Near-base divisors: Nikhilam (below) or Paravartya (above).
- Otherwise: plain long division — and always check by multiplying back.
:::

[[practice:long_division,div_5_25_125,div_by_9,div_nikhilam,div_paravartya,divisibility,remainder,recurring_19|24|Part V practice]]

[[answerkey:Part V answer key]]
