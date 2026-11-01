# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. When are template variables substituted?

A. Only after a cloud deployment.
B. When pip installs Streamlit.
C. By changing the API key.
D. When the prompt is invoked with named inputs.

**Answer: D.** Inspect the implementation and explanation for B03. When the prompt is invoked with named inputs.

- A is incorrect: it proposes “Only after a cloud deployment.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “When pip installs Streamlit.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “By changing the API key.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Does formatting the prompt require a model call?

A. Only if the topic contains braces.
B. Only on Windows.
C. No, formatting is a local operation.
D. Yes, every format call consumes tokens.

**Answer: C.** Inspect the implementation and explanation for B03. No, formatting is a local operation.

- A is incorrect: it proposes “Only if the topic contains braces.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only on Windows.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes, every format call consumes tokens.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. How are system and human content represented?

A. As embedding dimensions.
B. As separate role-based messages.
C. As database tables.
D. As tool permissions.

**Answer: B.** Inspect the implementation and explanation for B03. As separate role-based messages.

- A is incorrect: it proposes “As embedding dimensions.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “As database tables.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “As tool permissions.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"topic": "retrieval", "audience": "a beginner", "style": "Analogy"}, which fields match the documented result?

A. {"variables": ["audience", "style", "topic"]}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"topic": "a {literal}", "audience": "engineer", "style": "Checklist"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"variables": ["audience", "style", "topic"]}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
