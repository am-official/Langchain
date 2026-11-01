# Glossary
| Term | Meaning in this curriculum |
|---|---|
| Runnable | A composable stage supporting invocation and, where implemented, streaming |
| Tool | An allowlisted callable with an input schema and execution boundary |
| Agent | A control loop that can use models and tools, rather than a prompt alone |
| Middleware | Hooks around agent execution stages such as model calls |
| Context engineering | Selecting and structuring relevant trusted policy and untrusted data |
| Checkpoint | Persisted execution state associated with a thread/configuration |
| Interrupt | A pause requiring a later decision or continuation |
| Dataset | Versionable examples for evaluation with inputs and appropriate references |
| Experiment | Candidate executions and evaluator results over a dataset |
| Alignment | Agreement and disagreement between evaluator and human judgments |
| Graph | Declared computation with state, nodes, and edges |
| Deployment | Running service that hosts graph code and runtime configuration |
| Revision | Version of deployed code/configuration; local hashes are only a limited analogy |
| Assistant | Graph-specific configuration, distinct from deployed code and a user identity |
| Thread | Continuing conversation/execution state across runs |
| Run | An execution record; traces contain nested run relationships |
| Authentication | Verification of an asserted identity |
| Authorization | Permission checks for an authenticated actor and resource |
| Durability | Survival of data under a stated failure model |
| Online evaluation | Evaluation of selected live/recorded production runs |
| Insights | Aggregate exploratory pattern analysis, distinct from per-run scoring |
