# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What is a citation linked to here?

A. A model API key.
B. A CSS theme.
C. An unrelated example ID.
D. A retrieved source identifier.

**Answer: D.** Inspect the implementation and explanation for B19. A retrieved source identifier.

- A is incorrect: it proposes “A model API key.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A CSS theme.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “An unrelated example ID.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What is the no-evidence response?

A. A silent paid request.
B. A destructive tool call.
C. An explicit abstention.
D. An invented source.

**Answer: C.** Inspect the implementation and explanation for B19. An explicit abstention.

- A is incorrect: it proposes “A silent paid request.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A destructive tool call.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “An invented source.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Does similarity establish source truth?

A. Only in live mode.
B. No; relevance and truth are different.
C. Yes; every high score is a fact.
D. Only if the vector has 64 dimensions.

**Answer: B.** Inspect the implementation and explanation for B19. No; relevance and truth are different.

- A is incorrect: it proposes “Only in live mode.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Yes; every high score is a fact.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Only if the vector has 64 dimensions.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"question": "tools", "documents": ["Agents call tools."]}, which fields match the documented result?

A. {"answer": "[doc-1] Agents call tools.", "sources": ["doc-1"]}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"question": "state", "documents": ["Graphs maintain state."]}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"sources": ["doc-1"]}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
