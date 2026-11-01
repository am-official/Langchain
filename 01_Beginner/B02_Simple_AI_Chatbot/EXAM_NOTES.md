# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. How many chat messages does one completed turn append?

A. One system message only.
B. No messages.
C. One tool message only.
D. Two: user and assistant.

**Answer: D.** Inspect the implementation and explanation for B02. Two: user and assistant.

- A is incorrect: it proposes “One system message only.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “No messages.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “One tool message only.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What is the local reply mechanism?

A. A semantic retrieval model.
B. A background cloud deployment.
C. A deterministic response template.
D. A live OpenAI request.

**Answer: C.** Inspect the implementation and explanation for B02. A deterministic response template.

- A is incorrect: it proposes “A semantic retrieval model.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A background cloud deployment.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “A live OpenAI request.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Where does UI conversation history live?

A. Inside the OpenAI API key.
B. In the current Streamlit browser session.
C. In a replicated cloud database.
D. In the committed Python source.

**Answer: B.** Inspect the implementation and explanation for B02. In the current Streamlit browser session.

- A is incorrect: it proposes “Inside the OpenAI API key.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “In a replicated cloud database.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “In the committed Python source.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"message": "Hello"}, which fields match the documented result?

A. {"turns": 1}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"message": "Tools?"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"turns": 1}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
