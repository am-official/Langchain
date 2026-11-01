# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. Where does source provenance live?

A. Inside the API key.
B. In a CSS class.
C. In a tool retry count.
D. Document.metadata.

**Answer: D.** Inspect the implementation and explanation for B15. Document.metadata.

- A is incorrect: it proposes “Inside the API key.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “In a CSS class.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “In a tool retry count.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What does page_content contain?

A. An embedding dimension.
B. A provider invoice.
C. The loaded text.
D. The tenant role.

**Answer: C.** Inspect the implementation and explanation for B15. The loaded text.

- A is incorrect: it proposes “An embedding dimension.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A provider invoice.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The tenant role.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. Does loading untrusted text execute it?

A. Only if uploaded as Markdown.
B. No; the loader stores it as data.
C. Yes, every document is Python.
D. Only if it contains imports.

**Answer: B.** Inspect the implementation and explanation for B15. No; the loader stores it as data.

- A is incorrect: it proposes “Only if uploaded as Markdown.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Yes, every document is Python.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Only if it contains imports.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "Hello", "source": "a.txt"}, which fields match the documented result?

A. {"characters": 5, "count": 1}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "Bonjour", "source": "b.txt"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"documents": [{"page_content": "Bonjour", "metadata": {"source": "b.txt", "encoding": "UTF-8"}}]}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
