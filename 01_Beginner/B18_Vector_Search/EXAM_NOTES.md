# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What does the vector store rank?

A. Users by authorization level.
B. Cloud costs by invoice ID.
C. Python imports by file size.
D. Documents by similarity to the query vector.

**Answer: D.** Inspect the implementation and explanation for B18. Documents by similarity to the query vector.

- A is incorrect: it proposes “Users by authorization level.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Cloud costs by invoice ID.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Python imports by file size.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Does this local index survive a process restart?

A. Yes; embeddings are backups.
B. Only if the query is English.
C. No; it is in memory.
D. Yes; it is automatically replicated.

**Answer: C.** Inspect the implementation and explanation for B18. No; it is in memory.

- A is incorrect: it proposes “Yes; embeddings are backups.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only if the query is English.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes; it is automatically replicated.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What happens for a zero query vector?

A. It creates a deployment.
B. The explicit no-match path returns no evidence.
C. It invents a top source.
D. It executes every document.

**Answer: B.** Inspect the implementation and explanation for B18. The explicit no-match path returns no evidence.

- A is incorrect: it proposes “It creates a deployment.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “It invents a top source.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “It executes every document.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"question": "tools", "documents": ["Agents call tools.", "Graphs maintain state."]}, which fields match the documented result?

A. {"top_source": "doc-1"}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"question": "state", "documents": ["Tools execute.", "Graphs maintain state."]}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"top_source": "doc-2"}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
