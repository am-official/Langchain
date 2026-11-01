# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. How does the local summary select content?

A. It uses an undisclosed LLM.
B. It ranks by billed token cost.
C. It translates the document.
D. It takes the requested leading sentences.

**Answer: D.** Inspect the implementation and explanation for B05. It takes the requested leading sentences.

- A is incorrect: it proposes “It uses an undisclosed LLM.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “It ranks by billed token cost.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “It translates the document.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What range of summary lengths is accepted?

A. Exactly zero sentences.
B. Exactly 100 sentences.
C. One to five sentences.
D. Any negative number.

**Answer: C.** Inspect the implementation and explanation for B05. One to five sentences.

- A is incorrect: it proposes “Exactly zero sentences.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Exactly 100 sentences.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Any negative number.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Does the local extractor prove abstractive quality?

A. Only when the UI is green.
B. No; it demonstrates extractive processing.
C. Yes; it verifies semantic coverage.
D. Yes; it trains a summarization model.

**Answer: B.** Inspect the implementation and explanation for B05. No; it demonstrates extractive processing.

- A is incorrect: it proposes “Only when the UI is green.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Yes; it verifies semantic coverage.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes; it trains a summarization model.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "One. Two. Three.", "sentences": 2}, which fields match the documented result?

A. {"answer": "One. Two.", "source_sentences": 3}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "Only one sentence.", "sentences": 3}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"answer": "Only one sentence.", "source_sentences": 1}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
