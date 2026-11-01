# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What does overlap preserve?

A. Provider authentication.
B. A database transaction.
C. A permanent cloud deployment.
D. Shared context between adjacent chunks.

**Answer: D.** Inspect the implementation and explanation for B16. Shared context between adjacent chunks.

- A is incorrect: it proposes “Provider authentication.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A database transaction.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A permanent cloud deployment.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Why record start_index?

A. To choose a cloud region.
B. To authorize tool execution.
C. To relate a chunk to its original source position.
D. To count API key bytes.

**Answer: C.** Inspect the implementation and explanation for B16. To relate a chunk to its original source position.

- A is incorrect: it proposes “To choose a cloud region.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “To authorize tool execution.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “To count API key bytes.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Which overlap is invalid?

A. A source metadata field.
B. Overlap greater than or equal to chunk size.
C. Overlap zero.
D. Overlap below chunk size.

**Answer: B.** Inspect the implementation and explanation for B16. Overlap greater than or equal to chunk size.

- A is incorrect: it proposes “A source metadata field.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Overlap zero.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Overlap below chunk size.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "short text", "size": 20, "overlap": 2}, which fields match the documented result?

A. {"count": 1, "max_length": 10}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "abcdefghijklmnopqrst", "size": 10, "overlap": 0}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"count": 2, "max_length": 10}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
