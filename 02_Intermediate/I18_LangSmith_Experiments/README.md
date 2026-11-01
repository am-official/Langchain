# I18 · Compare experiments

Evaluate two deterministic candidate versions on one dataset and inspect per-example scores and aggregate results.

Start with [INSTRUCTIONS](INSTRUCTIONS.md), then [EXPLANATION](EXPLANATION.md). Each project is self-contained; no imports from another lesson are required.

## What you will learn
- Same dataset across versions
- Per-example evaluator results
- Aggregate experiment comparison

## Success criterion
Run each sample in [sample_data/examples.json](sample_data/examples.json). Each expected field must match. The UI must show a success message and downloadable evidence. Local mode is an educational deterministic implementation. Live integrations, when offered, are unverified until credentials and an actual request are tested.

## Practice
[Exercises](EXERCISES.md) · [Original questions](EXAM_NOTES.md) · [Troubleshooting](TROUBLESHOOTING.md)

Official syllabus verification is blocked by network policy; certification alignment is provisional.

## Optional live LangSmith workflow
Live mode evaluates the existing LANGSMITH_DATASET (default agent-basics), ignoring the local JSON field. Create it with I17 first. Examples must have inputs.question and outputs.answer. Two deterministic candidate versions are uploaded as experiments with a code evaluator. No OpenAI key is needed. Configure LANGSMITH_API_KEY in .env. Live writes require your account and remain unverified here; SDK boundaries are tested with injected clients. Do not upload sensitive data.
