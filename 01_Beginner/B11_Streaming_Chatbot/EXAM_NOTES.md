# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. Which model method supports incremental delivery?

A. freeze.
B. export_key.
C. drop_database.
D. stream.

**Answer: D.** Inspect the implementation and explanation for B11. stream.

- A is incorrect: it proposes “freeze.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “export_key.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “drop_database.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Does consuming the entire iterator before display preserve live delivery?

A. Only if the key is longer.
B. Only with a vector store.
C. No, it buffers delivery until completion.
D. Yes, buffering always improves interactivity.

**Answer: C.** Inspect the implementation and explanation for B11. No, it buffers delivery until completion.

- A is incorrect: it proposes “Only if the key is longer.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only with a vector store.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes, buffering always improves interactivity.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. How is the final text reconstructed?

A. By multiplying token counts.
B. By concatenating chunks in order.
C. By sorting chunks alphabetically.
D. By keeping only the last chunk.

**Answer: B.** Inspect the implementation and explanation for B11. By concatenating chunks in order.

- A is incorrect: it proposes “By multiplying token counts.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “By sorting chunks alphabetically.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “By keeping only the last chunk.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"message": "Hello"}, which fields match the documented result?

A. {"answer": "Local streaming example: Hello ", "chunk_count": 4}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"message": "Two words"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"chunk_count": 5}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
