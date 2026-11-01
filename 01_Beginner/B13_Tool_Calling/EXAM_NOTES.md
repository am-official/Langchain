# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What links a tool result to its request?

A. Its UI position alone.
B. The browser color.
C. Its token price.
D. The tool_call_id.

**Answer: D.** Inspect the implementation and explanation for B13. The tool_call_id.

- A is incorrect: it proposes “Its UI position alone.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The browser color.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Its token price.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What blocks an unexpected tool name?

A. The number of documents.
B. The output CSS.
C. An explicit allowlist check.
D. The greeting template.

**Answer: C.** Inspect the implementation and explanation for B13. An explicit allowlist check.

- A is incorrect: it proposes “The number of documents.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The output CSS.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The greeting template.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What is the local tool-call producer?

A. A cloud dataset.
B. A deterministic AIMessage fixture.
C. A verified live model.
D. An untrusted shell.

**Answer: B.** Inspect the implementation and explanation for B13. A deterministic AIMessage fixture.

- A is incorrect: it proposes “A cloud dataset.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A verified live model.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “An untrusted shell.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "one two"}, which fields match the documented result?

A. {"word_count": 2}
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
D. {"word_count": 1}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
