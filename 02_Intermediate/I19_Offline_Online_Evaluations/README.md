# I19 · Evaluate before and after release

Run reference-based offline checks or reference-free production-run checks with deterministic sampling.

Start with [INSTRUCTIONS](INSTRUCTIONS.md), then [EXPLANATION](EXPLANATION.md). Each project is self-contained; no imports from another lesson are required.

## What you will learn
- Offline reference evaluation
- Online reference-free signals
- Latency does not establish correctness

## Success criterion
Run each sample in [sample_data/examples.json](sample_data/examples.json). Each expected field must match. The UI must show a success message and downloadable evidence. Local mode is an educational deterministic implementation. Live integrations, when offered, are unverified until credentials and an actual request are tested.

## Practice
[Exercises](EXERCISES.md) · [Original questions](EXAM_NOTES.md) · [Troubleshooting](TROUBLESHOOTING.md)

Official syllabus verification is blocked by network policy; certification alignment is provisional.

## Optional live LangSmith workflow
Live mode requires online mode and existing real run UUIDs in the records JSON. It reads the actual completed runs and attaches client-side feedback, ignoring submitted prediction/latency fields. This does not configure a persistent server-side online evaluator. No OpenAI key is needed. Configure LANGSMITH_API_KEY in .env. Live writes require your account and remain unverified here; SDK boundaries are tested with injected clients. Do not upload sensitive data.
