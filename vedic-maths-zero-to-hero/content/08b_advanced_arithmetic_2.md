## Chapter 30: Speed, Distance and Time

### 30.1 The basic relation

[[diagram:dst_triangle]]

:::formula
Distance = Speed × Time. To convert km/h to m/s multiply by **5/18**; m/s to km/h multiply by **18/5**.
72 km/h = 72 × 5/18 = **20 m/s**. 15 m/s = 15 × 18/5 = **54 km/h**.
:::

### 30.2 Average speed

:::formula Equal distances at speeds a and b
Average speed = **2ab/(a + b)** — not (a + b)/2.
Going at 40 km/h and returning at 60 km/h: 2 × 40 × 60/100 = **48 km/h**.
:::

:::warn Average speed is total distance ÷ total time
Never average the speeds directly unless the **times** are equal.
:::

### 30.3 Relative speed

Same direction: subtract the speeds. Opposite directions: add them.

### 30.4 Trains

:::formula
A train crossing a pole or a person: distance = length of the train.
Crossing a platform, bridge or another train: distance = sum of the lengths.
:::

:::example Trains
1. A 240 m train at 54 km/h (15 m/s) passes a pole in 240 ÷ 15 = **16 s**.
2. The same train crosses a 360 m platform in (240 + 360) ÷ 15 = **40 s**.
3. Trains of 150 m and 100 m run in opposite directions at 50 and 40 km/h. Relative speed 90 km/h = 25 m/s; time = 250 ÷ 25 = **10 s**.
4. Same trains in the same direction: relative speed 10 km/h = 25/9 m/s; time = 250 ÷ (25/9) = **90 s**.
:::

### 30.5 Boats and streams

:::formula
Downstream speed = boat + stream. Upstream speed = boat − stream.
Boat = (down + up)/2. Stream = (down − up)/2.
:::

:::example
Downstream 18 km/h, upstream 12 km/h → boat **15 km/h**, stream **3 km/h**.
Time to go 30 km downstream and come back: 30/18 + 30/12 = 5/3 + 5/2 = 25/6 hours = **4 h 10 min**.
:::

## Chapter 31: Mixtures, Alligation and Partnership

### 31.1 Alligation

[[diagram:alligation 180 240 200]]

:::formula Rule of alligation
Cheaper : Dearer = (Dearer − Mean) : (Mean − Cheaper)
Tea at ₹180/kg and ₹240/kg mixed to give ₹200/kg: (240 − 200) : (200 − 180) = 40 : 20 = **2 : 1**.
:::

:::tip Alligation works for any "average of two groups"
Speeds, marks, prices, percentages of concentration — whenever two groups combine into one average, the cross diagram gives the ratio of the groups.
:::

### 31.2 Replacement

:::formula Repeated replacement
A container holds x litres of liquid. Each time y litres are removed and replaced with water. After n operations, liquid left = x(1 − y/x)ⁿ.
40 L milk, 8 L replaced twice: 40 × (32/40)² = 40 × 0.64 = **25.6 L** of milk.
:::

### 31.3 Partnership

:::formula
Profit is shared in the ratio of (capital × time).
:::

:::example
A invests ₹50,000 for 12 months; B invests ₹75,000 for 8 months. Ratio 6,00,000 : 6,00,000 = 1 : 1. A profit of ₹24,000 is shared **₹12,000 each**.
:::

## Chapter 32: Problems on Ages

:::tip Let the present ages be the unknowns
Write "n years ago" as (age − n) and "n years hence" as (age + n). The **difference** of two people's ages never changes.
:::

:::example
The sum of a father's and son's ages is 50. Five years ago the father was 7 times as old as the son. Let the son be s: father = 50 − s. 50 − s − 5 = 7(s − 5) → 45 − s = 7s − 35 → 8s = 80 → **s = 10**, father **40**.
Check: 5 years ago 35 = 7 × 5 ✓.
:::

## Chapter 33: Number Systems, Remainders and Cyclicity

### 33.1 Types of numbers (review)

Natural ⊂ whole ⊂ integers ⊂ rational ⊂ real. Rational numbers can be written p/q; irrational numbers (√2, π) cannot. Every recurring decimal is rational: 0.333… = 1/3.

### 33.2 Remainders

:::formula Remainder theorem for numbers
Remainder of (a × b) = remainder of (remainder of a × remainder of b). Same for sums and powers.
(17 × 23 × 29) ÷ 5 → remainders 2, 3, 4 → 2 × 3 × 4 = 24 → remainder **4**.
:::

:::example Remainder of a power
2¹⁰⁰ ÷ 7: since 2³ = 8 leaves remainder 1, 2⁹⁹ = (2³)³³ leaves remainder 1, so 2¹⁰⁰ leaves remainder **2**.
:::

### 33.3 Cyclicity of unit digits

[[table:cyclicity]]

:::example Unit digit of 7⁹⁵
Powers of 7 end in 7, 9, 3, 1 (cycle of 4). 95 = 4 × 23 + 3 → third in the cycle → **3**.
:::

:::example Trailing zeros of 100!
Count factors of 5: 100/5 = 20, 100/25 = 4 → **24 zeros**.
:::

### 33.4 Number of factors, sum of factors

For n = 2³ × 3² × 5: number of factors = 4 × 3 × 2 = 24. Sum of factors = (1 + 2 + 4 + 8)(1 + 3 + 9)(1 + 5) = 15 × 13 × 6 = **1,170**.

## Chapter 34: Permutations, Combinations and Probability

### 34.1 Counting principles

:::formula
**Multiplication principle:** m ways then n ways → m × n ways.
**Permutations** (order matters): ⁿPᵣ = n!/(n − r)!
**Combinations** (order does not matter): ⁿCᵣ = n!/(r!(n − r)!)
:::

:::example Counting
1. Arrangements of the letters of INDIA (I repeats twice): 5!/2! = **60**.
2. Committee of 3 men from 6 and 2 women from 5: ⁶C₃ × ⁵C₂ = 20 × 10 = **200**.
3. Handshakes among 10 people: ¹⁰C₂ = **45**.
4. 4-digit PINs with no repeated digit: 10 × 9 × 8 × 7 = **5,040**.
:::

### 34.2 Basic probability

:::formula
P(event) = favourable outcomes ÷ total equally likely outcomes. 0 ≤ P ≤ 1. P(not A) = 1 − P(A).
:::

:::example Probability
1. Two dice, sum 7: favourable (1,6) (2,5) (3,4) (4,3) (5,2) (6,1) = 6 of 36 → **1/6**.
2. At least one head in 3 tosses: 1 − P(no heads) = 1 − 1/8 = **7/8**.
3. A king or a heart from 52 cards: (4 + 13 − 1)/52 = 16/52 = **4/13** (the king of hearts is counted once).
:::

:::warn "Or" means add, but subtract the overlap
P(A or B) = P(A) + P(B) − P(A and B).
:::

## Chapter 35: Geometry and Mensuration

### 35.1 Formula sheet

| Shape | Area / Volume | Perimeter / Surface area |
|---|---|---|
| Rectangle l × b | lb | 2(l + b) |
| Square side a | a² | 4a; diagonal a√2 |
| Triangle | ½ × base × height; Heron: √(s(s−a)(s−b)(s−c)) | a + b + c |
| Circle radius r | πr² | 2πr |
| Cuboid l × b × h | lbh | 2(lb + bh + hl) |
| Cube side a | a³ | 6a² |
| Cylinder r, h | πr²h | curved 2πrh; total 2πr(r + h) |
| Cone r, h, slant l | ⅓πr²h | curved πrl; l = √(r² + h²) |
| Sphere r | 4/3 πr³ | 4πr² |

### 35.2 Worked examples (π = 22/7 where needed)

:::example Mensuration
1. Rectangle 24 m × 15 m: area **360 m²**, perimeter **78 m**.
2. Circle of radius 14 cm: area 22/7 × 196 = **616 cm²**; circumference 2 × 22/7 × 14 = **88 cm**.
3. Triangle with sides 13, 14, 15: s = 21; area = √(21 × 8 × 7 × 6) = √7,056 = **84**.
4. Cylinder r = 7, h = 10: volume 22/7 × 49 × 10 = **1,540 cm³**; curved surface 2 × 22/7 × 7 × 10 = **440 cm²**.
5. Sphere r = 21: volume 4/3 × 22/7 × 9,261 = **38,808 cm³**.
6. Right triangle with legs 9 and 12: hypotenuse √(81 + 144) = √225 = **15**.
:::

:::tip Pythagorean triples to memorise
(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29) — and their multiples, such as (9, 12, 15) and (6, 8, 10).
:::

:::tip Choose π = 22/7 when the radius is a multiple of 7
The 7 cancels, and the arithmetic stays exact.
:::

:::recap Chapters 30–35
- D = S × T; km/h × 5/18 = m/s; average speed for equal distances = 2ab/(a + b).
- Trains: add lengths when crossing a long object; relative speed adds (opposite) or subtracts (same).
- Alligation: (dearer − mean) : (mean − cheaper).
- Partnership: capital × time.
- Remainders multiply; unit digits cycle with period 1, 2 or 4.
- ⁿPᵣ for arrangements, ⁿCᵣ for selections; P(not A) = 1 − P(A).
:::

[[practice:speed,trains,boats,alligation,partnership,ages,cyclicity,ncr,probability,mensuration|24|Chapters 30–35 practice]]

[[answerkey:Chapters 30–35 answer key]]
