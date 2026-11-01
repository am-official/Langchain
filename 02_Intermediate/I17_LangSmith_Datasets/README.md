# I17 · A dataset with provenance

Create and list versionable local evaluation examples, with optional explicit LangSmith upload code documented separately.

Start with [INSTRUCTIONS](INSTRUCTIONS.md), then [EXPLANATION](EXPLANATION.md). Each project is self-contained; no imports from another lesson are required.

## What you will learn
- Evaluation example inputs and references
- Stable example IDs
- Local dataset versus LangSmith dataset

## Success criterion
Run each sample in [sample_data/examples.json](sample_data/examples.json). Each expected field must match. The UI must show a success message and downloadable evidence. Local mode is an educational deterministic implementation. Live integrations, when offered, are unverified until credentials and an actual request are tested.

## Practice
[Exercises](EXERCISES.md) · [Original questions](EXAM_NOTES.md) · [Troubleshooting](TROUBLESHOOTING.md)

Official syllabus verification is blocked by network policy; certification alignment is provisional.

## Optional live LangSmith workflow
Live mode reads or creates the named dataset and appends a real example using LangSmith Client. Rerunning adds another example; use a disposable dataset. Inputs use question and reference outputs use answer. No OpenAI key is needed. Configure LANGSMITH_API_KEY in .env. Live writes require your account and remain unverified here; SDK boundaries are tested with injected clients. Do not upload sensitive data.
