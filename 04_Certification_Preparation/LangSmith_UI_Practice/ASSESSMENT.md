# LangSmith practical assessment
Local apps cannot establish cloud UI proficiency. Use your own LangSmith account and a disposable project; do not upload sensitive data. The following live checks remain unverified in this repository.

1. **Traces:** enable B20 export with your own key. Locate the configured project, open a root run, identify normalize/analyze child spans, and verify redaction. Evidence: run ID, parent-child structure, duration, and a redacted screenshot. A local operation ID is insufficient.
2. **Datasets:** create three input/reference examples, retain stable IDs, and record a dataset change. Evidence: dataset ID and example IDs, without keys.
3. **Experiments:** compare two candidate versions on that dataset using exact match and a reviewed rubric judge where appropriate. Evidence: per-example scores, aggregate results, and at least one error analysis.
4. **Deployment objects:** identify a graph, deployment, active revision, assistant configuration, thread, and run in an account with deployment access. Explain which objects hold code, configuration, state, and execution status. Do not claim deployment from a local manifest.
5. **Monitoring:** inspect p95 latency, observed cost, errors, and explicit user feedback. Configure a supported online evaluator and describe how aggregate Insights differs. Explain sampling and alert delivery limits.

Score each task 0 (not demonstrated), 1 (partial), or 2 (verified with evidence). Target 9/10 with no zero on privacy or deployment terminology. Local-only work must be labeled as practice rather than cloud verification. Ask an instructor to review evidence independently.
