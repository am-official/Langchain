# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What local input format is required?

A. Arbitrary binary bytes.
B. Only cloud run UUIDs.
C. A shell command.
D. One term: explanation per line.

**Answer: D.** Inspect the implementation and explanation for B07. One term: explanation per line.

- A is incorrect: it proposes “Arbitrary binary bytes.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only cloud run UUIDs.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A shell command.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What is the local quiz style?

A. An automatic deployment test.
B. A sentiment classifier.
C. Grounded term-definition recall.
D. A psychometrically validated certification exam.

**Answer: C.** Inspect the implementation and explanation for B07. Grounded term-definition recall.

- A is incorrect: it proposes “An automatic deployment test.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A sentiment classifier.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “A psychometrically validated certification exam.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. How many local fact lines are supported?

A. At least one million.
B. One to ten.
C. Exactly zero.
D. An unlimited number.

**Answer: B.** Inspect the implementation and explanation for B07. One to ten.

- A is incorrect: it proposes “At least one million.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Exactly zero.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “An unlimited number.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"facts": "A: first"}, which fields match the documented result?

A. {"questions": [{"question": "What is A?", "answer": "first"}], "count": 1}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"facts": "A: first\nB: second"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"count": 2}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
