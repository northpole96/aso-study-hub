# Maths PYQ analysis: Quadratic Equations and Statistics (2018, 2021, 2025)

Source: the three Maths transcripts in `pyq/` and the family tags in `.claude/skills/aso-mock/data/maths.py`. Keys are ours (no official key). Made 23 Nov 2026.

## 1. How many questions

| Section | 2018 | 2021 | 2025 |
|---|---|---|---|
| Quadratic equations | 2 (Q64, Q72) | 2 (Q64, Q72) | 1 (Q62, solved from options) |
| Statistics (average, GM, median, mode, spread) | 7 (Q94–Q100) | 7 (Q94–Q100) | 0 (but Q68 is a weighted average) |
| Probability (same booklet block as statistics) | 10 | 9 | 0 |

- 2018 Q65 is missing from the OCR. An unplaced option block "2(1 − √3), 2(1 + √3), 1 + √3, 1 − √3" sits beside it; it may be a third quadratic (roots with surds). **CHECK** against the scan.
- The block is fixed. In both 2018 and 2021, **Q94–Q100 is statistics** and **Q79–Q81, Q84–85, Q89–93 is probability**. Q64 and Q72 are the quadratics. Only the numbers change.
- 2025 was a different paper (R. S. Aggarwal arithmetic). The 2027 ASO paper is more likely to follow the 2018 and 2021 template, but that is a guess. **CHECK**.

## 2. Quadratic equations: 3 families

### A. Form the equation from α + β and α − β (slot Q64, both years)
- 2018 Q64: α + β = 24, α − β = 8. Roots 16 and 8. Answer **x² − 24x + 128 = 0**.
- 2021 Q64: α + β = 12, α − β = 4. Roots 8 and 4. Answer **x² − 12x + 32 = 0**.
- Rule: add the two statements to get 2α, subtract to get 2β. Then the equation is x² − (sum)x + (product) = 0.
- Trap: the options differ only in signs. Wrong signs give x² + 12x + 32 or x² − 12x − 32.
- Likely next: α + β = 10, α − β = 2 (roots 6 and 4, x² − 10x + 24); the sum and product given directly; roots given as numbers; α² + β², or 1/α + 1/β, of a given equation; roots that are reciprocals.

### B. Discriminant (slot Q72, both years)
- 2018 Q72: 2x² − 4x + 3 → 16 − 24 = **−8**.
- 2021 Q72: 3x² − 5x + 3 → 25 − 36 = **−11**.
- Rule: D = b² − 4ac. The trap is the sign of b (it is squared, so b = −4 gives +16) and a negative answer among the options.
- Likely next: the same with a positive D (for example x² − 5x + 6 → 1); "nature of the roots" (D < 0 means no real roots, D = 0 equal roots, D > 0 two real roots); the k that makes the roots equal (D = 0), for example kx² − 4x + 1 = 0 gives k = 4.

### C. A word problem that turns into a quadratic (2025 Q62)
- Split 50 into two parts whose reciprocals add to 1/12. The equation is x² − 50x + 600 = 0, so the parts are **30 and 20**. The key is found fastest by testing the options: only (30, 20) adds to 50.
- Likely next: two numbers with a given sum and product; consecutive integers whose product is 56 or 90; a rectangle with given area and perimeter. In 2021 Q93 (consecutive even numbers whose squares differ by 84) the equation was linear, so it is not counted here.

## 3. Statistics: 6 families

| Family | 2018 | 2021 | 2025 |
|---|---|---|---|
| Combined or missing average | Q95: 100 students, 70 boys at 75, class at 72 → girls **65** | Q95: 30 numbers avg 12; first 20 avg 11, next 9 avg 10 → last **50**. Q96: pair averages 20, 19, 21 → A = **22** | Q68: 16 boys at 50.25 and 8 at 45.15 → **48.55** |
| Mean with a missing item | Q96: mean of 7 is 12, six known → 7th is **16** | Q98: mean of first 5 multiples of 7 → **21** | – |
| Geometric mean | Q94: GM of 3, 3², …, 3ⁿ → **3^((n+1)/2)** | Q94: GM of 4 and 16 → **8** | – |
| Deviations from the mean | – | Q97 and Q99: the sum is always **0** | – |
| Median and mode (grouped) | Q97 median, Q98 mode (tables lost in OCR) | Q100: median of a grouped table → **27.22** | – |
| Spread | Q99: variance of first n natural numbers → **(n² − 1)/12**. Q100: lower quartile of 9, 11, 15, 19, 17, 13, 7 → **9** | – (Q97, Q99 above) | – |

- **Combined average is the one family in all three years.** It is the surest statistics question. The rule: total = average × count, add the groups, subtract what is known.
- The 2018 key for Q97 and Q98 is not recoverable; check the scan before using them as practice.
- 2018 Q100's quartile uses the method where the lower half excludes the middle (7, 9, 11 → 9). **CHECK** whether the exam key agrees.
- Likely next (not yet asked): grouped mean, mode by the formula, and the relation mode = 3 × median − 2 × mean; standard deviation of the first n numbers (√((n² − 1)/12)); mean after every item is increased or multiplied; mean of first n natural, even or odd numbers (n + 1)/2, n + 1, n; a mean that changes when one item is replaced or removed; range and mean deviation; coefficient of variation; harmonic mean of two numbers (2ab/(a + b)); the weighted average in 2025 style (marks, prices, ages).

## 4. Near-repeats worth knowing
- Probability twins: 2018 Q90 (independent events, P(A) = 0.3, P(A ∪ B) = 0.8 → P(B) = 5/7) and 2021 Q91 (P(A ∪ B′) = 0.8 → P(B) = 2/7). Same method, a new twist.
- GM of two numbers (2021 Q94) is a gift if it comes again: choose numbers whose product is a perfect square.

## 5. What to do first (by chance of appearing)
1. Q64-type and Q72-type quadratics (about 5 minutes of study; they came in both years).
2. Combined average and missing-item average (all three years).
3. Deviations sum to zero, GM, variance of first n numbers (formulas only).
4. Grouped median, mode, mean (needs the formulas and 15 minutes of practice).
