# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What happens to extra contact fields?

A. They become secret model instructions.
B. They overwrite .env.
C. They disable validation.
D. They are rejected by the schema.

**Answer: D.** Inspect the implementation and explanation for B08. They are rejected by the schema.

- A is incorrect: it proposes “They become secret model instructions.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “They overwrite .env.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “They disable validation.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. Does a JSON age string pass the strict integer field?

A. Only if the email is uppercase.
B. Only in dark mode.
C. No, the schema requires an integer.
D. Yes, all strings are integers.

**Answer: C.** Inspect the implementation and explanation for B08. No, the schema requires an integer.

- A is incorrect: it proposes “Only if the email is uppercase.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “Only in dark mode.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Yes, all strings are integers.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What is structured extraction distinct from?

A. Validating required fields.
B. Merely checking that text is valid JSON.
C. Defining field bounds.
D. Rejecting negative ages.

**Answer: B.** Inspect the implementation and explanation for B08. Merely checking that text is valid JSON.

- A is incorrect: it proposes “Validating required fields.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Defining field bounds.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Rejecting negative ages.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "{\"name\":\"Ada\",\"email\":\"ada@example.com\",\"age\":28}"}, which fields match the documented result?

A. {"contact": {"name": "Ada", "email": "ada@example.com", "age": 28}}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "{\"name\":\"Lin\",\"email\":\"lin@example.org\",\"age\":0}"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"schema_fields": ["age", "email", "name"]}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
