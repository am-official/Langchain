# Five original practice questions

These are original project checks, not actual certification items. Official objective alignment remains provisional.

## 1. What does the local translator support?

A. Arbitrary multilingual paragraphs.
B. PDF OCR.
C. Automatic language-model training.
D. A three-phrase English phrasebook into Spanish/French.

**Answer: D.** Inspect the implementation and explanation for B04. A three-phrase English phrasebook into Spanish/French.

- A is incorrect: it proposes “Arbitrary multilingual paragraphs.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “PDF OCR.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “Automatic language-model training.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 2. What happens for an unknown local phrase?

A. It writes a key into source code.
B. It silently sends a paid API request.
C. A validation error explains the supported phrases.
D. It invents a fluent translation.

**Answer: C.** Inspect the implementation and explanation for B04. A validation error explains the supported phrases.

- A is incorrect: it proposes “It writes a key into source code.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “It silently sends a paid API request.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “It invents a fluent translation.”; this conflicts with the implementation described above.

Difficulty: Easy. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 3. How is live translation configured?

A. By disabling TLS.
B. Through OPENAI_API_KEY in environment/.env.
C. By editing every Python import.
D. Through a LangSmith key alone.

**Answer: B.** Inspect the implementation and explanation for B04. Through OPENAI_API_KEY in environment/.env.

- A is incorrect: it proposes “By disabling TLS.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “By editing every Python import.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “Through a LangSmith key alone.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 4. For local input {"text": "Hello", "language": "Spanish"}, which fields match the documented result?

A. {"answer": "Hola"}
B. A live API key is mandatory for this local contract.
C. The application must silently execute arbitrary source code.
D. The sample is intentionally undefined and has no expected result.

**Answer: A.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- B is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- D is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

## 5. For local input {"text": "Thank you", "language": "French"}, which fields match the documented result?

A. A live API key is mandatory for this local contract.
B. The application must silently execute arbitrary source code.
C. The sample is intentionally undefined and has no expected result.
D. {"answer": "Merci"}

**Answer: D.** The deterministic sample contract specifies these fields; other fields may also be present. No provider call or arbitrary source execution is required.

- A is incorrect: it proposes “A live API key is mandatory for this local contract.”; this conflicts with the implementation described above.
- B is incorrect: it proposes “The application must silently execute arbitrary source code.”; this conflicts with the implementation described above.
- C is incorrect: it proposes “The sample is intentionally undefined and has no expected result.”; this conflicts with the implementation described above.

Difficulty: Medium. Reference: app.py, EXPLANATION.md, and sample_data/examples.json.

Score one point each. Revisit the corresponding implementation for any missed question.
