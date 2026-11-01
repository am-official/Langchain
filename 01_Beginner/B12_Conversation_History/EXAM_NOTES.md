# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What is the difference between stored and prompt history?

A. They always have identical length.
B. Stored history is automatically multi-region.
C. The prompt stores database backups.
D. The prompt can retain fewer recent messages.

**Answer: D.** Inspect the implementation and explanation for B12. The prompt can retain fewer recent messages.

- A is incorrect: it proposes “They always have identical length.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Stored history is automatically multi-region.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The prompt stores database backups.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What does start_on human protect here?

A. It authorizes a user.
B. It exports traces.
C. It avoids beginning retained context with an orphan assistant turn.
D. It guarantees factual correctness.

**Answer: C.** Inspect the implementation and explanation for B12. It avoids beginning retained context with an orphan assistant turn.

- A is incorrect: it proposes “It authorizes a user.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “It exports traces.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “It guarantees factual correctness.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Can trimming remove an earlier name?

A. Only after cloud deployment.
B. Yes; information outside the retained context can be lost.
C. No; the model permanently remembers everything.
D. Only if the name is English.

**Answer: B.** Inspect the implementation and explanation for B12. Yes; information outside the retained context can be lost.

- A is incorrect: it proposes “Only after cloud deployment.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “No; the model permanently remembers everything.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Only if the name is English.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"message": "My name is Ada.", "max_messages": 4}, which fields match the documented result?

A. {"answer": "Local memory: Ada", "prompt_messages": 1}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"message": "Who am I?", "max_messages": 4, "history": [{"role": "user", "content": "My name is Lin"}, {"role": "assistant", "content": "Hi Lin"}]}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"answer": "Local memory: Lin", "prompt_messages": 3}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
