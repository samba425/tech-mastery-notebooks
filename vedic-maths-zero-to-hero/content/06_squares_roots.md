# Part VI — Squares, Cubes and Roots

Squares and roots appear in geometry, simplification, compound interest and data interpretation. Knowing the squares up to 50 by heart — and being able to *produce* any square up to 100 in a few seconds — is one of the most valuable skills for competitive exams.

## Chapter 16: Squares

### 16.1 Memorisation chart: squares 1 to 50

[[table:squares 1 50 5]]

### 16.2 Important squares from 51 to 100

[[table:squares 51 100 5]]

:::tip You do not need to memorise 51–100
Every square from 51 to 100 can be produced in seconds:
- **51–59:** near 50 → (25 + d) | d². For 57², 25 + 7 is 32 and 7² is 49, giving 3,249.
- **61–89:** split by the nearest ten, or use (a ± b)². 68² = 70² − 2 × 70 × 2 + 4 = 4,900 − 280 + 4 = 4,624.
- **90–99:** near 100 → (n − d) | d². For 93², 93 − 7 is 86 and 7² is 49, giving 8,649.
- **Ending in 5:** a(a + 1) | 25.
:::

### 16.3 Square patterns

:::formula Five patterns worth knowing
1. **Consecutive squares differ by the sum of the numbers:** 41² = 40² + 40 + 41 = 1,681.
2. **Difference of squares:** a² − b² = (a + b)(a − b). 26² − 24² = 50 × 2 = 100.
3. **Squares of numbers ending in 1:** 71² = 70² + 2 × 70 + 1 = 4,900 + 141 = 5,041.
4. **Squares of numbers ending in 9:** 79² = 80² − 2 × 80 + 1 = 6,400 − 159 = 6,241.
5. **Squares of 25 + d and 25 − d end in the same two digits:** 23² = 529 and 27² = 729.
:::

### 16.4 Squaring numbers ending in 5

(a)5² = a(a + 1) | 25. Practised in Parts II and IV.

### 16.5 Squaring numbers near 100 and 1,000

(Yavadunam) n² = (n + d) | d² with the right part having 2 digits (base 100) or 3 digits (base 1,000).

| # | Problem | Left n + d | Right d² | Answer |
|---|---|---|---|---|
| 1 | 92² | 84 | 64 | 8,464 |
| 2 | 107² | 114 | 49 | 11,449 |
| 3 | 985² | 970 | 225 | 9,70,225 |
| 4 | 1,032² | 1,064 | 1,024 → carry 1 | 10,65,024 |

### 16.6 Squaring two-digit and three-digit numbers

:::formula The (a + b)² split
(a + b)² = a² + 2ab + b². Choose a as a round number.
:::

[[diagram:area_square 60 7]]

:::example 67² by the split
(60 + 7)² = 3,600 + 2 × 60 × 7 + 49 = 3,600 + 840 + 49 = **4,489**.
:::

:::example 3-digit: 304² and 347²
304² = (300 + 4)² = 90,000 + 2,400 + 16 = **92,416**.
347² by the duplex method (Part IV): column values 9 | 24 | 58 | 56 | 49 → **1,20,409**.
:::

## Chapter 17: Cubes

### 17.1 Cubes 1 to 30

[[table:cubes 1 30 3]]

### 17.2 Useful cube patterns

[[table:roots_endings]]

:::formula Cubes near a base (Yavadunam for cubes)
(B + d)³ = (n + 2d) | 3d² | d³, where each right-hand part has as many digits as the base has zeros.
103³: 103 + 6 = 109 | 3 × 9 = 27 | 27 → **10,92,727**.
98³: 98 − 4 = 94 | 3 × 4 = 12 | −8 → 9,41,200 − 8 = **9,41,192**.
:::

:::why Why it works
(B + d)³ = B³ + 3B²d + 3Bd² + d³ = B²(B + 3d) + B(3d²) + d³. The left part B + 3d is n + 2d.
:::

:::formula Algebraic cube identities
(a + b)³ = a³ + 3a²b + 3ab² + b³ · (a − b)³ = a³ − 3a²b + 3ab² − b³
a³ + b³ = (a + b)(a² − ab + b²) · a³ − b³ = (a − b)(a² + ab + b²)
:::

## Chapter 18: Square Roots and Cube Roots

### 18.1 Square roots of perfect squares (up to 4 digits) by observation

[[flow: Look at the last digit → two choices | Look at the first pair → tens digit | Compare with the square of (tens)5 | Choose the right ending]]

:::example √7,744
- Last digit 4 → root ends in **2 or 8**.
- First pair 77 lies between 8² = 64 and 9² = 81 → tens digit **8**.
- 85² = 7,225 < 7,744, so the root is above 85 → **88**.
:::

:::example √5,329
Last digit 9 → 3 or 7. 53 lies between 49 and 64 → 7_. 75² = 5,625 > 5,329 → below 75 → **73**.
:::

:::example √11,449 (5 digits)
Last digit 9 → 3 or 7. Leading part 114 lies between 10² = 100 and 11² = 121 → 10_. 105² = 11,025 < 11,449 → **107**.
:::

:::warn This only works for perfect squares
For 7,750 the method gives nonsense. If the question does not promise a perfect square, use estimation or long division.
:::

### 18.2 The long-division method for square roots

:::example √53,824
Pair the digits from the right: 5 | 38 | 24.
```calc
           2   3   2
        ------------
   2  )  5 | 38 | 24
         4                 2² = 4
        ---
  43  )  1   38            double 2 → 4_; 43 × 3 = 129
         1   29
        --------
  462 )        9   24      double 23 → 46_; 462 × 2 = 924
               9   24
              -------
                   0
```
**√53,824 = 232.** Check: 232² = 53,824 ✓.
:::

:::formula Algorithm
1. Pair digits from the decimal point outwards.
2. Find the largest square ≤ the first pair; write its root as the first digit.
3. Subtract, bring down the next pair.
4. Double the root found so far, write it with a blank: (2r)_. Find the largest digit x with (2r)x × x ≤ current number.
5. Repeat. For decimals, bring down pairs of zeros.
:::

:::example √2 to three decimal places
Pairs 2 | 00 | 00 | 00. Digits found: 1, then 24 × 4 = 96 ≤ 100, then 281 × 1 = 281 ≤ 400, then 2824 × 4 = 11,296 ≤ 11,900. So √2 ≈ **1.414** (more precisely 1.41421…).
:::

### 18.3 Estimating square roots

:::approx The tangent-line estimate
√n ≈ a + (n − a²) ÷ (2a), where a² is the nearest perfect square.
√300: a = 17 (289). √300 ≈ 17 + 11/34 ≈ 17.32 (true 17.3205…).
√70: a = 8 (64). √70 ≈ 8 + 6/16 = 8.375 (true 8.3666…). The estimate is always slightly **too big**.
:::

:::tip Useful values to remember
√2 ≈ 1.414 · √3 ≈ 1.732 · √5 ≈ 2.236 · √6 ≈ 2.449 · √7 ≈ 2.646 · √10 ≈ 3.162
:::

### 18.4 Cube roots of perfect cubes

:::formula Two-step method for perfect cubes up to 6 digits
1. **Last digit** of the cube → last digit of the root (from the cube-endings table: 2↔8, 3↔7, others unchanged).
2. **Thousands part** (drop the last three digits) → find the largest cube ≤ it → that is the tens digit.
:::

| # | Problem | Last digit → | Thousands part → | Answer |
|---|---|---|---|---|
| 1 | ∛2,74,625 | 5 → 5 | 274: 6³ = 216 ≤ 274 < 343 | 65 |
| 2 | ∛4,93,039 | 9 → 9 | 493: 7³ = 343 ≤ 493 < 512 | 79 |
| 3 | ∛1,03,823 | 3 → 7 | 103: 4³ = 64 ≤ 103 < 125 | 47 |
| 4 | ∛6,81,472 | 2 → 8 | 681: 8³ = 512 ≤ 681 < 729 | 88 |
| 5 | ∛12,167 | 7 → 3 | 12: 2³ = 8 ≤ 12 < 27 | 23 |

:::warn Only for perfect cubes
The question must guarantee a perfect cube. Otherwise, estimate: ∛100 ≈ 4.64 because 4.6³ ≈ 97 and 4.7³ ≈ 104.
:::

### 18.5 Approximation and verification

Always verify a root by squaring or cubing back, at least roughly: 88² ends in 4 ✓ and is close to 90² = 8,100 ✓.

## Chapter 19: Daily Drills for Squares and Roots

:::tip A 10-minute daily routine
- **Minutes 1–3:** recite squares 11–30 aloud (forward, then backward).
- **Minutes 4–6:** produce five random squares 31–99 using the near-50 / near-100 / ending-in-5 methods.
- **Minutes 7–8:** three perfect-square roots and two perfect-cube roots.
- **Minutes 9–10:** two estimates of non-perfect square roots, checked with a calculator afterwards.
:::

| Day | Squares to recite | Roots to find |
|---|---|---|
| Monday | 11–20 | √1,849, √3,481, ∛9,261 |
| Tuesday | 21–30 | √6,241, √2,209, ∛32,768 |
| Wednesday | 31–40 | √9,409, √1,369, ∛1,57,464 |
| Thursday | 41–50 | √5,776, √8,281, ∛2,16,000 |
| Friday | 51–60 (near 50) | √7,056, √4,356, ∛3,89,017 |
| Saturday | 90–100 (near 100) | √9,801, √9,025, ∛7,04,969 |
| Sunday | mixed revision | any five |

*Answers to the drill roots:* Mon 43, 59, 21 · Tue 79, 47, 32 · Wed 97, 37, 54 · Thu 76, 91, 60 · Fri 84, 66, 73 · Sat 99, 95, 89.

:::recap Part VI summary
- Know squares 1–50; produce 51–100 with near-50, near-100, ending-in-5 or (a ± b)².
- Cubes near a base: (n + 2d) | 3d² | d³.
- Perfect square roots: last digit → two choices; first pair → tens; compare with (tens)5².
- Perfect cube roots: last digit (2↔8, 3↔7) and the thousands part.
- Non-perfect roots: long division (exact digits) or √n ≈ a + (n − a²)/2a (approximate).
:::

[[practice:square,square_near_50,square_near_base,identity_square,square_duplex,cube,sqrt_perfect,cbrt_perfect,sqrt_estimate|24|Part VI practice]]

[[answerkey:Part VI answer key]]
