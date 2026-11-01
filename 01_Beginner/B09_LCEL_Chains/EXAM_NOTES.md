# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What does RunnableParallel do here?

A. Persists a conversation database.
B. Authorizes tenant access.
C. Exports cloud traces automatically.
D. Runs named analyses on the same input.

**Answer: D.** Inspect the implementation and explanation for B09. Runs named analyses on the same input.

- A is incorrect: it proposes “Persists a conversation database.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Authorizes tenant access.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Exports cloud traces automatically.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Why use RunnablePassthrough?

A. To execute Python from text.
B. To generate an API key.
C. To retain the original input in the evidence.
D. To hide every failure.

**Answer: C.** Inspect the implementation and explanation for B09. To retain the original input in the evidence.

- A is incorrect: it proposes “To execute Python from text.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “To generate an API key.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “To hide every failure.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What does the pipe operator compose?

A. Provider invoices.
B. Runnable stages.
C. Filesystem permissions.
D. Cloud regions.

**Answer: B.** Inspect the implementation and explanation for B09. Runnable stages.

- A is incorrect: it proposes “Provider invoices.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Filesystem permissions.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Cloud regions.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "Hello world"}, which fields match the documented result?

A. {"words": 2, "uppercase": "HELLO WORLD", "original": "Hello world"}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "one"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"words": 1}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
