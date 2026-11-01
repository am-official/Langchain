# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What do local hash vectors represent?

A. Verified semantic meanings for all synonyms.
B. User permissions.
C. Cloud invoice items.
D. Lexical token buckets, not semantic understanding.

**Answer: D.** Inspect the implementation and explanation for B17. Lexical token buckets, not semantic understanding.

- A is incorrect: it proposes “Verified semantic meanings for all synonyms.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “User permissions.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Cloud invoice items.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What is cosine similarity of identical nonzero vectors?

A. A tenant ID.
B. A JSON schema.
C. One.
D. Negative infinity.

**Answer: C.** Inspect the implementation and explanation for B17. One.

- A is incorrect: it proposes “A tenant ID.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “A JSON schema.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Negative infinity.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. What is a hash-collision limitation?

A. Every hash stores a raw key.
B. Different words can share a bucket.
C. Every vector is a cloud deployment.
D. All synonyms are guaranteed to match.

**Answer: B.** Inspect the implementation and explanation for B17. Different words can share a bucket.

- A is incorrect: it proposes “Every hash stores a raw key.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Every vector is a cloud deployment.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “All synonyms are guaranteed to match.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "agent", "other": "agent"}, which fields match the documented result?

A. {"dimensions": 64, "cosine_similarity": 1.0}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "tool", "other": "tool"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"cosine_similarity": 1.0}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
