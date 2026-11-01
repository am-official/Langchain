# B01 · Hello LangChain
A greeting studio that teaches prompt templates, runnable composition, and text parsing. The midnight, violet, and mint interface includes a result canvas, mode labels, progress feedback, download, and actionable errors.

Start with [INSTRUCTIONS](INSTRUCTIONS.md), then [EXPLANATION](EXPLANATION.md). Demo mode runs a real LangChain pipeline with a deterministic local runnable. It is not a language model. Live OpenAI mode uses `ChatOpenAI` and is not verified against the provider.

**Success:** Ada + English + Warm produces `Hello, Ada! Welcome to your first LangChain lab.` and a success message in demo mode. Spanish/French demo options translate only the greeting word.

This is a foundation chain, not an autonomous agent. LangChain is useful here for composing interchangeable prompt, model, and parser stages; a plain greeting alone does not require it. No LangSmith account or key is needed.

See [sample inputs](sample_data/examples.json), [exercises](EXERCISES.md), [original questions](EXAM_NOTES.md), and [troubleshooting](TROUBLESHOOTING.md). Official objective alignment remains provisional because official sources were blocked during development.
