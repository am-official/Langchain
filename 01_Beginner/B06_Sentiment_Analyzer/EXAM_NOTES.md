# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What drives the local sentiment score?

A. Provider token usage.
B. The length of the API key.
C. A verified human rating.
D. Positive-term count minus negative-term count.

**Answer: D.** Inspect the implementation and explanation for B06. Positive-term count minus negative-term count.

- A is incorrect: it proposes “Provider token usage.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The length of the API key.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A verified human rating.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. How is not good handled by the local baseline?

A. It performs translation first.
B. It rejects every word good.
C. It may be positive because negation is unsupported.
D. It always understands negation perfectly.

**Answer: C.** Inspect the implementation and explanation for B06. It may be positive because negation is unsupported.

- A is incorrect: it proposes “It performs translation first.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “It rejects every word good.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “It always understands negation perfectly.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What does the live classifier validate?

A. A PDF page number.
B. A label and reason through a Pydantic schema.
C. A database migration.
D. A tool authorization token.

**Answer: B.** Inspect the implementation and explanation for B06. A label and reason through a Pydantic schema.

- A is incorrect: it proposes “A PDF page number.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A database migration.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “A tool authorization token.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "great helpful"}, which fields match the documented result?

A. {"answer": "positive", "score": 2}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "bad broken"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"answer": "negative", "score": -2}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
