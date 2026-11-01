# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What does traceable instrumentation describe?

A. User authorization roles.
B. Vector similarity rankings.
C. A deployment manifest.
D. Nested named execution spans.

**Answer: D.** Inspect the implementation and explanation for B20. Nested named execution spans.

- A is incorrect: it proposes “User authorization roles.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Vector similarity rankings.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “A deployment manifest.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Does a local operation ID prove cloud delivery?

A. Only if printed in green.
B. Only with a large prompt.
C. No; verify the actual exported run.
D. Yes; every UUID is a cloud trace.

**Answer: C.** Inspect the implementation and explanation for B20. No; verify the actual exported run.

- A is incorrect: it proposes “Only if printed in green.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only with a large prompt.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes; every UUID is a cloud trace.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What protects trace input text?

A. Adding untrusted text to system policy.
B. Explicit redaction before export.
C. Committing a key.
D. Disabling TLS.

**Answer: B.** Inspect the implementation and explanation for B20. Explicit redaction before export.

- A is incorrect: it proposes “Adding untrusted text to system policy.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Committing a key.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Disabling TLS.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "one two"}, which fields match the documented result?

A. {"words": 2, "characters": 7, "export_requested": false}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": " one   two "}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"words": 2, "characters": 7}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
