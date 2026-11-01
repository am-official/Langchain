# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. Which parser validates the task schema?

A. A CSS formatter.
B. A vector store.
C. A token issuer.
D. PydanticOutputParser.

**Answer: D.** Inspect the implementation and explanation for B10. PydanticOutputParser.

- A is incorrect: it proposes “A CSS formatter.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A vector store.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A token issuer.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What type is the done field?

A. A cloud thread.
B. A PDF page.
C. A strict boolean.
D. An arbitrary prompt.

**Answer: C.** Inspect the implementation and explanation for B10. A strict boolean.

- A is incorrect: it proposes “A cloud thread.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A PDF page.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “An arbitrary prompt.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. How are parse failures exposed?

A. As a new deployment.
B. As an actionable input error.
C. As fabricated successful output.
D. As a source rewrite.

**Answer: B.** Inspect the implementation and explanation for B10. As an actionable input error.

- A is incorrect: it proposes “As a new deployment.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “As fabricated successful output.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “As a source rewrite.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "{\"task\":\"Review\",\"priority\":2,\"done\":false}"}, which fields match the documented result?

A. {"task": {"task": "Review", "priority": 2, "done": false}}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "{\"task\":\"Run\",\"priority\":1,\"done\":true}"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"task": {"task": "Run", "priority": 1, "done": true}}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
