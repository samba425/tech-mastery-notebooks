# Part II — Vedic Mathematics Core Techniques

This part introduces the **16 sutras** in the order used by Bharati Krishna Tirthaji, followed by the **13 sub-sutras**. For each sutra you get the traditional name, a plain-English meaning, the mathematics behind it, and its best uses. The most important sutras (1–4, 10 and 14) are developed in full lessons here and practised heavily in Parts III–VII. The more specialised ones are explained with worked examples and honest notes about their limits.

## The 16 Sutras at a Glance

:::history How to read the sutra names
Each sutra is a short Sanskrit phrase. The English meanings below are the ones commonly given in Tirthaji's book and in later teaching. Several sutras are applied in more than one way, and different teachers sometimes link the same technique to different sutras. Where that happens, this book says so rather than presenting one interpretation as the only correct one.
:::

| # | Sutra | Common English meaning | Main uses in this book |
|---|---|---|---|
| 1 | Ekadhikena Purvena | By one more than the previous one | Squares ending in 5; 1/19, 1/29 … as decimals |
| 2 | Nikhilam Navatashcaramam Dashatah | All from 9 and the last from 10 | Subtraction from 10ⁿ; multiplication and division near a base |
| 3 | Urdhva-Tiryagbhyam | Vertically and crosswise | General multiplication; algebra |
| 4 | Paravartya Yojayet | Transpose and adjust | Division by 12, 112 …; solving equations |
| 5 | Shunyam Saamyasamuccaye | When the total is the same, that total is zero | Special equations solved by inspection |
| 6 | (Anurupye) Shunyamanyat | If one is in ratio, the other is zero | Special simultaneous equations |
| 7 | Sankalana-Vyavakalanabhyam | By addition and by subtraction | Equations with swapped coefficients |
| 8 | Puranapuranabhyam | By completion or non-completion | Completing the square / cube |
| 9 | Chalana-Kalanabhyam | Differences and similarities (sequential motion) | Quadratic equations via 2x + b |
| 10 | Yavadunam | Whatever the extent of its deficiency | Squaring numbers near a base |
| 11 | Vyashtisamanstih | Part and whole | Using an average or a split to simplify |
| 12 | Shesanyankena Charamena | The remainders by the last digit | Decimals of 1/7, 1/13, 1/17 … |
| 13 | Sopantyadvayamantyam | The ultimate and twice the penultimate | A special family of fraction equations |
| 14 | Ekanyunena Purvena | By one less than the previous one | Multiplying by 9, 99, 999 … |
| 15 | Gunitasamuccayah | The product of the sum is equal to the sum of the product | Checking products and factorisations |
| 16 | Gunakasamuccayah | The factors of the sum is equal to the sum of the factors | Checking factorisations; derivatives |

### Two ideas used throughout

**1. Base and deviation.** Many methods compare a number with a convenient **base** (10, 100, 1,000) and work with the **deviation** (how far above or below the base it is). 97 is 100 − 3; 104 is 100 + 4.

**2. Digit sums (Beejank).** Add the digits of a number repeatedly until one digit remains (treat 9 as 0). This is the remainder on division by 9. If a calculation is correct, the digit sums obey the same calculation. See Sutra 15.

## Sutra 1: Ekadhikena Purvena — "By One More than the Previous One"

:::objective
Square any number ending in 5 in one step; multiply pairs such as 43 × 47; write 1/19 (and similar fractions) as recurring decimals without long division.
:::

**Simple explanation.** *Ekadhika* means "one more". The sutra tells you to take the digit (or number) that comes before, and use **one more than it**.

**Prerequisites:** multiplication tables, place value.

### 1A. Squaring numbers ending in 5

:::formula The rule
For a number ending in 5, write it as (a)5. Then **(a)5² = a × (a + 1) | 25**.
:::

[[diagram:square_end5 65]]

:::why Why it works
A number ending in 5 is 10a + 5. Its square is (10a + 5)² = 100a² + 100a + 25 = 100 × a(a + 1) + 25. So the hundreds part is a × (a + 1) and the last two digits are always 25.
:::

**Step-by-step algorithm**

1. Remove the final 5. Call what is left *a*.
2. Multiply *a* by the next number, *a* + 1.
3. Write 25 after the result.

:::compare Standard method ||| Ekadhikena
**75²**
```calc
     75
   × 75
   ----
    375
   525
   ----
   5625
```
|||
**75²**
a = 7, one more = 8
7 × 8 = 56
attach 25 → **5,625**
:::

:::example Five solved examples (increasing difficulty)
1. 25² → 2 × 3 = 6 → **625**
2. 45² → 4 × 5 = 20 → **2,025**
3. 95² → 9 × 10 = 90 → **9,025**
4. 115² → 11 × 12 = 132 → **13,225**
5. 7.5² → 75² = 5,625; one decimal place in 7.5, so two in the square → **56.25**
:::

**Real-life use.** Area of a 35 m × 35 m plot = 35² = 3 × 4 | 25 = 1,225 m².

:::warn Common mistakes
- Writing a × a instead of a × (a + 1): 65² is **not** 3,625. It is 6 × 7 = 42 → 4,225.
- Forgetting that a can have two digits: 125² → 12 × 13 = 156 → 15,625.
:::

### 1B. Same leading digits, last digits adding to 10

The same idea works for products like 43 × 47: the tens digits are equal (4) and the units add to 10 (3 + 7). This is the sub-sutra **Antyayordasake'pi** ("when the last digits total 10"), used together with Ekadhikena.

:::formula The rule
If two numbers have the same leading part *a* and their last digits *u* and *v* satisfy u + v = 10, then the product is **a × (a + 1) | u × v**, where u × v is written as **two digits**.
:::

:::example Solved examples
1. 43 × 47 → 4 × 5 = 20 | 3 × 7 = 21 → **2,021**
2. 62 × 68 → 6 × 7 = 42 | 2 × 8 = 16 → **4,216**
3. 81 × 89 → 8 × 9 = 72 | 1 × 9 = 09 → **7,209** (note the 0)
4. 104 × 106 → 10 × 11 = 110 | 4 × 6 = 24 → **11,024**
5. 7.3 × 7.7 → for 73 × 77 write 7 × 8 | 3 × 7, i.e. 56 | 21 → 5,621 → **56.21**
:::

:::why Why it works
(10a + u)(10a + v) = 100a² + 10a(u + v) + uv. When u + v = 10 this is 100a² + 100a + uv = 100 · a(a + 1) + uv.
:::

:::when
**Use it** only when *both* conditions hold: the same leading part, and last digits adding to 10. **Do not** use it for 43 × 57 (different tens digits) or 46 × 47 (units add to 13). Then use vertically and crosswise (Sutra 3).
:::

### 1C. Recurring decimals for 1/19, 1/29, 1/39 …

For a denominator ending in 9, the *ekadhika* is one more than the digits before the 9: for 19 it is **2**, for 29 it is **3**, for 49 it is **5**.

**Method for 1/19 (multiply from the right by 2):** start with 1 as the last digit and keep doubling, writing each new digit to the **left** and carrying any tens.

```calc
digits written right to left:  1, 2, 4, 8, 6 (16, carry 1), 3 (12+1=13, carry 1),
7 (6+1), 4 (14, carry 1), 9 (8+1), 8 (18, carry 1), 7 (16+1=17, carry 1), 5 (14+1=15, carry 1),
1 (10+1=11, carry 1), 3 (2+1), 6, 2 (12, carry 1), 5 (4+1), 0 (10, carry 1) … stop after 18 digits

1/19 = 0.052631578947368421 052631…   (18-digit recurring block)
```

:::tip How many digits?
For 1/19 the block has 18 digits (one less than 19). You can stop at 9 digits and use a beautiful shortcut: the second half is the **nines-complement** of the first half. 052631578 + 947368421 = 999999999.
:::

:::memory Ekadhikena
"**Five squares: one more, then 25.**"
:::

## Sutra 2: Nikhilam Navatashcaramam Dashatah — "All from 9 and the Last from 10"

:::objective
Subtract any number from 100, 1,000, 10,000 … instantly; multiply numbers close to a base in one line; divide by 9, 8, 89, 98, 997 and similar divisors.
:::

**Simple explanation.** *Nikhilam* means "all". To find how far a number is from the next power of 10, subtract **every digit from 9** and the **last digit from 10**.

### 2A. Subtracting from a power of 10

:::example Solved examples
1. 100 − 37: 9 − 3 = 6, 10 − 7 = 3 → **63**
2. 1,000 − 468: 9−4, 9−6, 10−8 → **532**
3. 10,000 − 2,791 → 7,2,0,9 → **7,209**
4. 1,000 − 46: think of 46 as 046 → 9−0, 9−4, 10−6 → **954**
5. 10,000 − 3,580: the last digit is 0, so apply the rule to 358 (from 1,000) → 642 and keep the 0 → **6,420**
:::

:::why Why it works
1,000 = 999 + 1. Subtracting from 999 never needs borrowing (each digit is subtracted from 9), and the extra 1 is added to the last digit, which is the same as subtracting that digit from 10.
:::

:::warn Trailing zeros
If the number ends in zero, the "last digit" is the last **non-zero** digit. 1,000 − 470: apply the rule to 47 (from 100) to get 53, then attach the 0 → 530.
:::

### 2B. Multiplying numbers near a base

[[diagram:nikhilam 97 96 100]]

:::formula Nikhilam multiplication
Write each number with its deviation from the base.
**Right part** = product of the deviations (it must have as many digits as the base has zeros).
**Left part** = either number plus the *other* number's deviation (cross addition).
:::

**Step-by-step (97 × 96, base 100):**

1. Deviations: 97 = 100 − 3, 96 = 100 − 4.
2. Right part: (−3) × (−4) = 12 → two digits: 12.
3. Left part: 97 − 4 = 93 (or 96 − 3 = 93 — the same!).
4. Answer: 93 | 12 = **9,312**.

:::why Why it works
Let the numbers be B + a and B + b, where B is the base. Their product is B² + Ba + Bb + ab = B × (B + a + b) + ab. The left part (B + a + b) is "one number plus the other's deviation"; it is multiplied by B, which is why the right part ab must fill exactly the number of zeros in B.
:::

:::example Five solved examples
1. **88 × 94** (base 100; −12, −6): right = 72; left = 88 − 6 = 82 → **8,272**
2. **103 × 107** (+3, +7): right = 21; left = 103 + 7 = 110 → **11,021**
3. **112 × 95** (+12, −5): right = −60; left = 112 − 5 = 107 → 107 | −60 = 10,700 − 60 = **10,640**
4. **996 × 988** (base 1,000; −4, −12): right = 048 (three digits); left = 996 − 12 = 984 → **9,84,048**
5. **1,012 × 1,003** (+12, +3): right = 036; left = 1,015 → **10,15,036**
:::

:::warn Common mistakes
- **Too few digits in the right part.** With base 1,000 the right part needs three digits: 4 × 12 = 48 must be written 048.
- **Too many digits.** For 88 × 88 (base 100, −12 each), right = 144 — that is three digits. Carry the 1: left 76 + 1 → 77 | 44 = **7,744**.
- **Negative right part.** When one deviation is positive and the other negative, subtract: 107 | −60 means 10,700 − 60.
:::

### 2C. Working bases (numbers near 50, 200, 300 …)

When numbers are near 50 or 300, use a **working base** = (a convenient multiple) × (a power of 10).

:::example Working base 50 = 100 ÷ 2
**48 × 47** (deviations −2, −3 from 50): right = 6; left = 48 − 3 = 45. Because 50 = 100 ÷ 2, halve the left part: 45 ÷ 2 = 22.5. The .5 means "50 into the right part", so the right part becomes 56 and the answer is 22 | 56 = **2,256**.
Alternatively use 50 = 5 × 10: left 45 × 5 = 225, right 6 → 225 | 6 = **2,256**.
:::

:::example Working base 200 = 2 × 100
**212 × 207** (+12, +7): right = 84; left = 212 + 7 = 219 → × 2 = 438 → **43,884**.
:::

### 2D. Nikhilam division (divisors just below a base)

To divide by 9, 8, 89, 98, 997 …, use the **complement** of the divisor (base − divisor), and repeatedly multiply and add.

:::example 1,235 ÷ 88
Base 100, complement 100 − 88 = **12**. Split the dividend: the right part has as many digits as the base has zeros.
```calc
  88 | 1  2 |  3   5
  12 |    1 |  2          ← 1 × 12
     |      |  3   6      ← (2 + 1) = 3, and 3 × 12 = 36
     |------|--------
       1  3 |  8  11      → quotient 13, remainder 8×10 + 11 = 91
```
91 is bigger than 88, so take one more 88 out: quotient **14**, remainder 91 − 88 = **3**. Check: 88 × 14 + 3 = 1,235 ✓.
:::

**Division by 9** is especially easy because the complement is 1: each quotient digit is the running total of the dividend's digits.

:::example 12,345 ÷ 9
Running totals: 1, 1+2 = 3, 3+3 = 6, 6+4 = 10 → quotient columns 1 | 3 | 6 | 10; remainder column 10 + 5 = 15.
Resolve: 1,3,6,10 → 1,370 (carry the 1 from 10). Remainder 15 = 9 + 6 → add 1 to the quotient.
**Quotient 1,371, remainder 6.** Check: 9 × 1,371 + 6 = 12,345 ✓.
:::

:::when
**Use Nikhilam** when the numbers are within about 10–15 % of a base (88–112 for base 100). **Do not use it** for 67 × 58: the deviations (−33, −42) are larger than the numbers' distance to other bases, and the right part 1,386 overflows badly. Use vertically and crosswise instead.
:::

:::memory Nikhilam
"**Cross-add on the left, multiply deviations on the right, fill the zeros.**"
:::

## Sutra 3: Urdhva-Tiryagbhyam — "Vertically and Crosswise"

:::objective
Multiply any two numbers — of any size — in a single line, from right to left; multiply algebraic expressions with the same pattern.
:::

**Simple explanation.** Instead of writing several partial products and adding them, you calculate each **column** of the answer directly: multiply vertically, then crosswise, then vertically again, adding as you go.

[[diagram:urdhva2 23 41]]

:::formula 2-digit × 2-digit: (ab) × (cd)
Units: b × d. Tens: a × d + b × c (crosswise). Hundreds: a × c. Carry from right to left.
:::

:::example 23 × 41
Step 1 (vertical right): 3 × 1 = 3 → write 3.
Step 2 (crosswise): 2 × 1 + 3 × 4 = 2 + 12 = 14 → write 4, carry 1.
Step 3 (vertical left): 2 × 4 = 8, + 1 = 9.
**23 × 41 = 943.**
:::

:::why Why it works
(10a + b)(10c + d) = 100ac + 10(ad + bc) + bd. The three steps are exactly the coefficients of 100, 10 and 1. It is the distributive property, organised by place value.
:::

:::example Solved examples (increasing difficulty)
1. **32 × 21:** 2×1 = 2; 3×1 + 2×2 = 7; 3×2 = 6 → **672**
2. **46 × 37:** 6×7 = 42 → 2 carry 4; 4×7 + 6×3 = 46, +4 = 50 → 0 carry 5; 4×3 = 12, +5 = 17 → **1,702**
3. **89 × 76:** 9×6 = 54 → 4 c5; 8×6 + 9×7 = 111, +5 = 116 → 6 c11; 8×7 = 56, +11 = 67 → **6,764**
4. **123 × 456** (five steps, see below) → **56,088**
5. **(2x + 3)(4x + 5):** 2·4 = 8x²; 2·5 + 3·4 = 22x; 3·5 = 15 → **8x² + 22x + 15**
:::

### 3-digit × 3-digit

[[diagram:urdhva3]]

```calc
  1 2 3
× 4 5 6
Step 1: 3×6                 = 18  → write 8, carry 1
Step 2: 2×6 + 3×5           = 27  +1 = 28 → write 8, carry 2
Step 3: 1×6 + 3×4 + 2×5     = 28  +2 = 30 → write 0, carry 3
Step 4: 1×5 + 2×4           = 13  +3 = 16 → write 6, carry 1
Step 5: 1×4                 =  4  +1 =  5
Answer: 56,088
```

:::warn Common mistakes
- Forgetting one of the crosswise pairs in the middle step (there are **three** products in step 3 for 3-digit numbers).
- Adding the carry to the wrong column. Always carry to the **next column on the left**.
- Mixing up the number of digits: pad the shorter number with zeros (23 × 405 → 023 × 405).
:::

:::when
**Use it** for any multiplication — it is the universal method. It shines for 2-digit × 2-digit products done mentally. For numbers near a base, Nikhilam is usually faster; for multiplying by 11, 25 or 99, the special rules in Part IV are faster still.
:::

:::memory Urdhva
"**Vertical, cross, vertical.** For 3 digits: 1 – 2 – 3 – 2 – 1 products in the five steps."
:::

## Sutra 4: Paravartya Yojayet — "Transpose and Adjust"

:::objective
Divide by numbers slightly **above** a base (11, 12, 13, 112, 1,012 …); solve linear equations by transposing terms; understand the idea of "change the sign and apply".
:::

**Simple explanation.** *Paravartya* means "transpose" (move across and change sign). When a divisor is a little more than a base, write its excess digits with **minus signs** and use them as multipliers.

### 4A. Paravartya division

:::example 1,452 ÷ 12
Base 10, excess +2 → transposed flag **−2**. The right part has one digit (base 10 has one zero).
```calc
  12 | 1    4    5 | 2
  −2 |     −2   −4 | −2
     |-------------|----
       1    2    1 | 0     → quotient 121, remainder 0
```
Bring down 1. 1 × (−2) = −2 → 4 − 2 = 2. 2 × (−2) = −4 → 5 − 4 = 1. 1 × (−2) = −2 → 2 − 2 = 0.
**1,452 ÷ 12 = 121.** Check: 12 × 121 = 1,452 ✓.
:::

:::example 13,789 ÷ 112
Base 100, excess 12 → flags **−1, −2**. Right part: 2 digits.
```calc
  112 | 1   3   7 |  8   9
  −1−2|    −1  −2 |
      |        −2 | −4          (2 × −1, 2 × −2)
      |           | −3  −6      (3 × −1, 3 × −2)
      |-----------|--------
        1   2   3 |  1   3      → quotient 123, remainder 13
```
**Quotient 123, remainder 13.** Check: 112 × 123 + 13 = 13,789 ✓.
:::

:::warn Negative remainder
Sometimes the remainder comes out negative (e.g. 2,489 ÷ 13 gives column values 2, −2, 14 | −33). Resolve the columns into an ordinary number, then **borrow one divisor** from the quotient until the remainder is between 0 and the divisor. 2,489 ÷ 13 → quotient 191, remainder 6.
:::

### 4B. Solving linear equations by transposition

"Transpose and adjust" is exactly what you do when you move a term across the equals sign and change its sign.

:::formula ax + b = cx + d
Transpose: x = (d − b) ÷ (a − c).
:::

:::example Solved examples
1. 5x + 3 = 28 → 5x = 25 → **x = 5**
2. 7x − 4 = 3x + 20 → x = (20 + 4)/(7 − 3) = 24/4 = **6**
3. 2x + 9 = 5x − 6 → x = (−6 − 9)/(2 − 5) = −15/−3 = **5**
4. (x + 3)/4 = (x − 2)/3 → 3(x + 3) = 4(x − 2) → 3x + 9 = 4x − 8 → **x = 17**
5. 0.5x + 1.2 = 0.2x + 3 → x = (3 − 1.2)/(0.5 − 0.2) = 1.8/0.3 = **6**
:::

:::when
**Paravartya division** is neat for divisors like 11, 12, 13, 102, 112, 1,012. For other divisors (e.g. 47, 73) use ordinary long division, or the more advanced "flag" (*dhvajanka*) method found in specialist books. **Do not force it**: dividing by 19 with Paravartya creates large negative columns and is slower than long division.
:::

:::memory Paravartya
"**Above the base? Flip the sign of the excess and multiply along.**"
:::

[[practice:square_end5,units_sum_10,sub_power10,nikhilam_below,nikhilam_above,nikhilam_mixed,urdhva_2x2,urdhva_3x3,div_by_9,div_nikhilam,div_paravartya,linear_two_sides,recurring_19|26|Practice: Sutras 1–4]]

[[answerkey:Sutras 1–4 answer key]]
