# LangSmith cheatsheet
- A trace is a hierarchy of runs/spans. Inspect parent IDs, inputs, outputs, errors, and durations. Redact sensitive material before export.
- `@traceable` instruments a function. `tracing_context(enabled=False)` keeps tests from exporting. Requesting export does not establish delivery; verify the run in the configured project.
- A dataset contains evaluation examples with inputs, reference outputs when needed, stable IDs, and provenance. Dataset changes affect experiment interpretation.
- An experiment compares candidate behavior against a dataset under explicit evaluators. Keep candidate versions, dataset version, evaluator settings, and per-example errors.
- Code evaluators handle deterministic properties. LLM judges use a rubric for less easily coded properties but require calibration, injection resistance, and human review.
- Online evaluators score selected production runs. Reference-free metrics do not magically establish factual correctness. Insights-style analysis explores aggregate patterns; a local topic counter is not the managed Insights product.

I17 includes optional `Client.read_dataset/create_dataset/create_example`; I18 uses the SDK `evaluate`; I19 attaches client-side feedback with `read_run/create_feedback`. Their boundaries are tested using injected clients. Actual live cloud calls were not made. B20 supports optional redacted trace export.

Model/provider credentials and LangSmith credentials serve different purposes. Configure only keys needed by the selected live workflow. Never paste them into issues or commit .env.
