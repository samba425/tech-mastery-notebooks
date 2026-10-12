# Part IX — Mental Maths Tricks

This part collects everyday mental tricks. Each trick is labelled either **Exact**, meaning it always gives the true answer, or **Approximate**, meaning it gives a quick estimate that you must not present as exact.

:::warn Exact vs approximate
Mixing these up is the biggest danger with "tricks". Exam options are often designed so that a careless estimate falls on a wrong option. Estimate to **eliminate** options, then compute exactly if two options are close.
:::

## Chapter 36: Estimation and Approximation

### 36.1 Rounding to friendly numbers — *Approximate*

:::approx Rounding products
4,987 × 31 ≈ 5,000 × 31 = 1,55,000 (exact: 1,54,597; error about 0.3%).
39.98 × 25.03 ≈ 40 × 25 = 1,000 (exact 1,000.6994).
:::

:::tip Compensate when you round both numbers
If you round one number **up** and the other **down**, errors partly cancel. Rounding both in the same direction doubles the error.
:::

### 36.2 Estimating quotients and roots — *Approximate*

- 7,215 ÷ 59 ≈ 7,200 ÷ 60 = 120 (exact 122.28…).
- √500 lies between 22 (484) and 23 (529), much closer to 22 → about 22.4 (true value ≈ 22.36).
- ∛1,000 is exactly 10, so ∛1,100 is a little more than 10 → about 10.3.

### 36.3 Order-of-magnitude check — *Approximate*

Before writing any answer, ask: "Roughly how big should this be?" 312 × 48 must be near 300 × 50 = 15,000, so 1,497.6 or 1,49,760 are clearly wrong. (The exact answer is 14,976.)

## Chapter 37: Doubling, Halving and Re-grouping

### 37.1 Double and halve — *Exact*

:::formula
a × b = (a ÷ 2) × (b × 2). Halve one factor and double the other until one becomes easy.
:::

:::example
- 16 × 25 = 8 × 50 = 4 × 100 = **400**
- 35 × 14 = 70 × 7 = **490**
- 48 × 125 = 24 × 250 = 12 × 500 = 6 × 1,000 = **6,000**
- 4.5 × 18 = 9 × 9 = **81**
:::

### 37.2 Factor re-grouping — *Exact*

- 25 × 36 × 4 = (25 × 4) × 36 = **3,600**
- 15 × 28 = 15 × 2 × 14 = 30 × 14 = **420**
- 125 × 64 = 125 × 8 × 8 = 1,000 × 8 = **8,000**

### 37.3 Multiplying by 4, 8, 16 — *Exact*

Double repeatedly: 37 × 8 → 74 → 148 → **296**.

## Chapter 38: Percentage Tricks

### 38.1 The swap rule — *Exact*

:::formula
**x% of y = y% of x.**
8% of 25 = 25% of 8 = **2**. 16% of 50 = 50% of 16 = **8**.
:::

### 38.2 Build from 10%, 5% and 1% — *Exact*

18% of 250 = 10% (25) + 5% (12.5) + 3 × 1% (7.5) = **45**.

### 38.3 Fraction equivalents — *Exact*

| Percentage | Fraction | Example |
|---|---|---|
| 12.5% | 1/8 | 12.5% of 640 = 80 |
| 16.67% | 1/6 (approx. %) | 1/6 of 360 = 60 |
| 33.33% | 1/3 (approx. %) | 1/3 of 2,700 = 900 |
| 37.5% | 3/8 | 3/8 of 960 = 360 |
| 62.5% | 5/8 | 5/8 of 480 = 300 |
| 87.5% | 7/8 | 7/8 of 800 = 700 |

:::note About 16.67% and 33.33%
16.67% is a rounded form of 16 2/3 %. Using the fraction 1/6 is **exact**; multiplying by 0.1667 is **approximate**.
:::

### 38.4 Approximate percentages — *Approximate*

23.8% of 4,012 ≈ 24% of 4,000 = 960 (exact ≈ 954.9). Use only for elimination.

## Chapter 39: Calendar Calculations — *Exact*

### 39.1 Odd days

An **odd day** is a day left over after complete weeks. Day numbers: Sunday 0, Monday 1, … Saturday 6.

:::formula Odd-day facts
- Ordinary year = 365 days = 52 weeks + **1** odd day; leap year = **2** odd days.
- 100 years = **5** odd days; 200 years = **3**; 300 years = **1**; 400 years = **0**.
- Month odd days: Jan 3, Feb 0 (1 in a leap year), Mar 3, Apr 2, May 3, Jun 2, Jul 3, Aug 3, Sep 2, Oct 3, Nov 2, Dec 3.
- Leap year: divisible by 4, but century years only if divisible by 400 (1900 no, 2000 yes).
:::

:::example What day was 15 August 1947?
- 1600 years: 0 odd days.
- Years 1601–1900 (300 years): 1.
- Years 1901–1946 (46 years, 11 leap years): 46 + 11 = 57, and 57 leaves remainder 1 after dividing by 7. So 1.
- 1947 up to 15 August: 3 + 0 + 3 + 2 + 3 + 2 + 3 + 15, which is 31, leaving remainder 3. So 3.
- Total 0 + 1 + 1 + 3 = 5 → **Friday**.
:::

:::example Same date, later year
26 January 2025 was a Sunday. 26 January 2026 is 365 days later → 1 odd day → **Monday**. (2026 is not a leap year, and no 29 February lies between them.)
:::

## Chapter 40: Divisibility and Last-Digit Tricks

### 40.1 Divisibility by 7 and 13 with an osculator — *Exact*

:::formula Ekadhika osculator
Find a multiple of the divisor ending in 9: 7 × 7 = 49 and 13 × 3 = 39. "One more than" the digits before the 9 gives the **osculator**: 5 for 7, and 4 for 13.
Repeatedly: (number without last digit) + (last digit × osculator). If the result is divisible, so is the original number.
:::

:::example
- Is 2,401 divisible by 7? 240 + 1 × 5 = 245 → 24 + 5 × 5 = 49 → yes. (2,401 = 7⁴.)
- Is 1,001 divisible by 13? 100 + 1 × 4 = 104 → 10 + 4 × 4 = 26 → yes.
:::

### 40.2 Last digit of a power — *Exact*

:::example Last digit of 3⁴⁷
Powers of 3 end in 3, 9, 7, 1 (cycle 4). 47 leaves remainder 3 after dividing by 4 → third in cycle → **7**.
:::

:::tip Digits that never change
Any power of a number ending in 0, 1, 5 or 6 ends in the same digit. Numbers ending in 76 keep ending in 76 when raised to any power.
:::

### 40.3 Perfect-square screening — *Exact (as a rejection test)*

A perfect square never ends in 2, 3, 7 or 8, and its digital root is always 1, 4, 7 or 9. So 3,528 cannot be a perfect square. **Passing** the test does not prove a number is a square.

## Chapter 41: Comparing Fractions and Quick Checks

### 41.1 Cross-multiplication comparison — *Exact*

To compare 7/9 and 11/14: compare 7 × 14 = 98 with 9 × 11 = 99. 98 < 99, so **11/14 is larger**.

### 41.2 Digit-sum check — *Exact as a rejection test*

If the digit-sum check fails, the answer is definitely wrong. If it passes, the answer is *probably* right (swapped digits are not detected). See Chapter 12.

### 41.3 Units-digit check — *Exact as a rejection test*

The units digit of 47 × 83 must be the units digit of 7 × 3 = 21 → 1. An option ending in 3 is wrong.

:::recap Part IX summary
- Label every trick Exact or Approximate.
- Approximate: rounding, estimates for elimination only.
- Exact: double and halve, re-grouping, x% of y = y% of x, fraction equivalents, odd-days calendar, osculator divisibility, power cycles.
- Rejection tests (digit sums, units digits, square endings) can prove an answer wrong but not right.
:::

[[practice:estimate_product,pct_of,frac_to_pct,calendar,cyclicity,divisibility,approx_simplify,mult_decompose|20|Part IX practice]]

[[answerkey:Part IX answer key]]
