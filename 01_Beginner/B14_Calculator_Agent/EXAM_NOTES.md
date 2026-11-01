# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. Which mechanism parses arithmetic?

A. Unrestricted Python eval.
B. A shell subprocess with user commands.
C. A web browser console.
D. A restricted AST visitor without eval/exec.

**Answer: D.** Inspect the implementation and explanation for B14. A restricted AST visitor without eval/exec.

- A is incorrect: it proposes “Unrestricted Python eval.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A shell subprocess with user commands.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A web browser console.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Why is exponentiation rejected?

A. It requires a LangSmith account.
B. It is a CSS property.
C. It is outside the arithmetic allowlist.
D. It is always a tool authorization token.

**Answer: C.** Inspect the implementation and explanation for B14. It is outside the arithmetic allowlist.

- A is incorrect: it proposes “It requires a LangSmith account.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “It is a CSS property.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “It is always a tool authorization token.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Which framework runs the tool loop?

A. The theme config.
B. create_agent.
C. StrOutputParser alone.
D. The file loader alone.

**Answer: B.** Inspect the implementation and explanation for B14. create_agent.

- A is incorrect: it proposes “The theme config.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “StrOutputParser alone.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The file loader alone.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"expression": "2 + 3 * 4"}, which fields match the documented result?

A. {"answer": "14", "numeric_result": "14", "tool_calls": 1}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"expression": "(10 - 4) / 2"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"answer": "3.0"}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
