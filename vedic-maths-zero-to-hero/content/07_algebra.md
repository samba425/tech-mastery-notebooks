# Part VII — Factorisation and Algebra

Algebra is arithmetic with letters. Every Vedic multiplication method you have learned works for algebraic expressions too — in fact, the algebra is *why* the methods work. This part builds algebra from the beginning and connects each idea back to mental arithmetic.

## Chapter 20: Expressions, Variables and Equations

### 20.1 Variables, constants and expressions

- A **variable** is a letter that stands for a number that can change (x, y, n).
- A **constant** is a fixed number (5, −3, ½).
- A **term** is a number, a variable, or their product: 7x, −3y², 12.
- An **expression** is terms joined by + or −: 3x² − 5x + 2.
- **Like terms** have the same variables with the same powers: 4x and −9x are like terms; 4x and 4x² are not.

:::example Simplifying expressions
- 5x + 3y − 2x + 7y = (5 − 2)x + (3 + 7)y = **3x + 10y**
- 4(2a − 3) − (a + 5) = 8a − 12 − a − 5 = **7a − 17**
- Evaluate 3x² − 5x + 2 at x = 4: 3(16) − 20 + 2 = **30**
:::

:::warn A minus sign outside brackets
−(a + 5) = −a − 5. The minus applies to **every** term inside. Forgetting this is the most common algebra error.
:::

### 20.2 Linear equations in one variable

An **equation** says two expressions are equal. To solve, do the same operation to both sides — or, equivalently, **transpose** (Paravartya): move a term across the equals sign and change its sign.

[[flow: Expand brackets | Collect x-terms on one side | Collect numbers on the other | Divide by the coefficient | Check by substituting]]

:::example Five linear equations
1. 4x − 7 = 21 → 4x = 28 → **x = 7**
2. 3(x + 2) = 2x + 11 → 3x + 6 = 2x + 11 → **x = 5**
3. 5x − 3 = 2x + 15 → 3x = 18 → **x = 6**
4. x/3 + x/4 = 14 → (4x + 3x)/12 = 14 → 7x = 168 → **x = 24**
5. 0.6x − 1.5 = 0.2x + 0.5 → 0.4x = 2 → **x = 5**
:::

:::formula Paravartya formula
ax + b = cx + d ⇒ **x = (d − b)/(a − c)**. Example 3: x = (15 − (−3))/(5 − 2) = 18/3 = 6.
:::

### 20.3 Word problems into equations

:::example "A number doubled and increased by 7 gives 31."
2x + 7 = 31 → 2x = 24 → x = **12**.
:::

:::example Ages
A mother is 26 years older than her daughter. In 4 years she will be three times as old as the daughter. Let the daughter's age be d.
d + 26 + 4 = 3(d + 4) → d + 30 = 3d + 12 → 18 = 2d → **d = 9**, mother **35**. Check: in 4 years, 39 = 3 × 13 ✓.
:::

## Chapter 21: Algebraic Identities

An **identity** is true for **every** value of the variables. These five are used constantly.

:::formula The essential identities
1. (a + b)² = a² + 2ab + b²
2. (a − b)² = a² − 2ab + b²
3. (a + b)(a − b) = a² − b²
4. (x + a)(x + b) = x² + (a + b)x + ab
5. (a + b)³ = a³ + 3a²b + 3ab² + b³, and (a − b)³ = a³ − 3a²b + 3ab² − b³
:::

### 21.1 (a + b)² — seen as area

[[diagram:area_square a b]]

A square of side (a + b) splits into a square a², a square b², and **two** rectangles ab. That is why there is a **2ab** term — the most commonly forgotten part.

:::warn (a + b)² is not a² + b²
(3 + 4)² = 49, but 3² + 4² = 25. The missing 24 is 2 × 3 × 4.
:::

### 21.2 Difference of two squares — seen as cut-and-move

[[diagram:diff_squares a b]]

:::example Using a² − b² for arithmetic
- 53 × 47 = (50 + 3)(50 − 3) = 2,500 − 9 = **2,491**
- 102 × 98 = 10,000 − 4 = **9,996**
- 87² − 13² = (87 + 13)(87 − 13) = 100 × 74 = **7,400**
- 1,005 × 995 = 10,00,000 − 25 = **9,99,975**
- 6.2 × 5.8 = 36 − 0.04 = **35.96**
:::

### 21.3 Perfect-square identities for mental squaring

:::example
- 103² = 10,000 + 600 + 9 = **10,609**
- 97² = 10,000 − 600 + 9 = **9,409**
- 4.1² = 16 + 0.8 + 0.01 = **16.81**
- (x + 5)² = x² + 10x + 25
- (2y − 3)² = 4y² − 12y + 9
:::

### 21.4 Using identities to evaluate expressions

:::example If a + b = 10 and ab = 21, find a² + b².
a² + b² = (a + b)² − 2ab = 100 − 42 = **58**. (Check: a = 7, b = 3 gives 49 + 9 = 58 ✓.)
:::

:::example If x + 1/x = 5, find x² + 1/x².
Square both sides: x² + 2 + 1/x² = 25 → x² + 1/x² = **23**. A favourite exam pattern.
:::

## Chapter 22: Multiplying Polynomials (Vertically and Crosswise)

The Urdhva pattern multiplies polynomials just as it multiplies numbers — the "digits" are the coefficients, and there is **no carrying**.

:::compare Standard method (FOIL) ||| Vertically and crosswise
**(3x + 2)(4x − 5)**
First: 12x²
Outer: −15x
Inner: 8x
Last: −10
Sum: 12x² − 7x − 10
|||
**(3x + 2)(4x − 5)**
Vertical (left): 3 × 4 = **12x²**
Crosswise: 3(−5) + 2(4) = **−7x**
Vertical (right): 2(−5) = **−10**
:::

:::example Three-term by three-term: (x² + 2x + 3)(2x² − x + 4)
Coefficients (1, 2, 3) and (2, −1, 4):
x⁴: 1·2 = 2 · x³: 1(−1) + 2·2 = 3 · x²: 1·4 + 2(−1) + 3·2 = 8 · x: 2·4 + 3(−1) = 5 · constant: 3·4 = 12
**= 2x⁴ + 3x³ + 8x² + 5x + 12.**
Check (Gunitasamuccaya, x = 1): (1 + 2 + 3)(2 − 1 + 4) = 6 × 5 = 30, and 2 + 3 + 8 + 5 + 12 = 30 ✓.
:::

:::tip The x = 1 check works for every product
Put x = 1 in each factor and in your answer; the numbers must agree. Putting x = −1 gives a second, independent check.
:::

## Chapter 23: Factorisation

**Factorising** is multiplying in reverse: writing an expression as a product.

### 23.1 Common factors

6x² + 9x = 3x(2x + 3). Always take out the highest common factor first.

### 23.2 Quadratics x² + bx + c

:::formula Find two numbers
x² + bx + c = (x + m)(x + n) where **m + n = b** and **m × n = c**.
:::

| # | Expression | m, n (sum b, product c) | Factorised |
|---|---|---|---|
| 1 | x² + 7x + 12 | 3, 4 | (x + 3)(x + 4) |
| 2 | x² − 9x + 20 | −4, −5 | (x − 4)(x − 5) |
| 3 | x² + 2x − 15 | 5, −3 | (x + 5)(x − 3) |
| 4 | x² − 4x − 21 | −7, 3 | (x − 7)(x + 3) |
| 5 | x² − 49 | 7, −7 | (x + 7)(x − 7) |

### 23.3 Quadratics ax² + bx + c (Adyamadyena method)

*Adyamadyenantyamantyena* — "the first by the first and the last by the last". Split the middle term so that the **first** coefficient splits as the product of the first terms and the **last** as the product of the last terms.

:::example 6x² + 13x + 6
Find two numbers with product a × c = 36 and sum 13: **4 and 9**.
6x² + 4x + 9x + 6 = 2x(3x + 2) + 3(3x + 2) = **(2x + 3)(3x + 2)**.
Check crosswise: 2·2 + 3·3 = 13 ✓.
:::

:::example 3x² − 10x − 8
a × c = −24, sum −10: **−12 and 2**. 3x² − 12x + 2x − 8 = 3x(x − 4) + 2(x − 4) = **(3x + 2)(x − 4)**.
:::

### 23.4 Difference of squares and perfect squares

- 4x² − 25 = (2x + 5)(2x − 5)
- 9y² − 12y + 4 = (3y − 2)²
- x⁴ − 16 = (x² + 4)(x² − 4) = (x² + 4)(x + 2)(x − 2)

## Chapter 24: Simultaneous Linear Equations

### 24.1 Elimination and substitution

:::example 2x + 3y = 13 and 5x − 2y = 4
Multiply the first by 2 and the second by 3: 4x + 6y = 26 and 15x − 6y = 12. Add: 19x = 38 → **x = 2**. Then 3y = 13 − 4 = 9 → **y = 3**.
:::

### 24.2 Cross-multiplication (a Vedic-style formula)

:::formula For a₁x + b₁y = c₁ and a₂x + b₂y = c₂
x = (c₁b₂ − c₂b₁) ÷ (a₁b₂ − a₂b₁)    y = (a₁c₂ − a₂c₁) ÷ (a₁b₂ − a₂b₁)
Same example: x = (13·(−2) − 4·3)/(2·(−2) − 5·3) = (−26 − 12)/(−4 − 15) = −38/−19 = 2; y = (2·4 − 5·13)/(−19) = (8 − 65)/(−19) = 3.
:::

This is the method Tirthaji presents using Paravartya ideas; it is identical to Cramer's rule taught in higher classes.

### 24.3 Special patterns (from Part II)

| Pattern | Sutra | Example | Solution |
|---|---|---|---|
| Coefficients swapped | Sankalana-Vyavakalanabhyam | 37x + 23y = 97, 23x + 37y = 83 | add: x + y = 3; subtract: x − y = 1 → x = 2, y = 1 |
| One pair in ratio with constants | Anurupye Shunyamanyat | 6x + 5y = 10, 12x + 9y = 18 | x-coeff 6:12 = constants 10:18? No (1:2 vs 5:9) — pattern fails; solve normally |
| y-coeffs and constants in ratio | Anurupye Shunyamanyat | 2x + 3y = 6, 7x + 9y = 18 | 3:9 = 6:18 → x = 0, y = 2 |

:::warn Check the pattern first
The second row shows that a pattern **can fail**. Always check the exact condition before applying a special sutra.
:::

### 24.4 Conventional algebra versus shortcuts

:::when
Shortcut sutras are fast for the patterns they fit. Elimination and cross-multiplication **always** work. In exams: spend two seconds looking for a pattern; if none jumps out, solve conventionally.
:::

:::recap Part VII summary
- Collect like terms; a minus outside a bracket changes every sign inside.
- ax + b = cx + d ⇒ x = (d − b)/(a − c).
- (a ± b)² = a² ± 2ab + b²; a² − b² = (a + b)(a − b).
- Multiply polynomials vertically and crosswise; check with x = 1.
- x² + bx + c: find m, n with sum b and product c. ax² + bx + c: split using a × c.
- Simultaneous equations: elimination, or cross-multiplication formula; look for swapped coefficients.
:::

[[practice:linear_eq,linear_two_sides,expand_binomials,factor_quadratic,diff_squares,identity_square,simultaneous,sankalana,shunyam,chalana_quadratic|26|Part VII practice]]

[[answerkey:Part VII answer key]]
