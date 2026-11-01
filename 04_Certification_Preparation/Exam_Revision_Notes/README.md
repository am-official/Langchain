# Revision notes

## Agent selection
create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed.

Revisit I01.

## Deep Agents
Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code.

Revisit A01.

## Middleware
Enforcement belongs at the execution boundary, before the call or side effect it protects.

Revisit I03.

## Context engineering
Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns.

Revisit I05.

## Instruction files
Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism.

Revisit I14.

## Restricted execution
Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python.

Revisit A04.

## Tool protocol
Tool-call IDs tie results to requests; tool allowlists and argument validation still apply.

Revisit B13.

## Structured output
Valid JSON can still violate types, bounds, and allowed fields.

Revisit B08.

## Memory
Prompt context, browser state, and durable long-term storage have different lifetimes.

Revisit I06.

## Retrieval grounding
Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims.

Revisit B19.

## Code evaluators
Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge.

Revisit I15.

## LLM judges
A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration.

Revisit I16.

## Offline evaluation
Offline describes the evaluation workflow on a dataset, not whether networking exists.

Revisit I18.

## Online evaluation
Online checks can measure properties without references; the chosen metric determines what is actually evidenced.

Revisit I19.

## Datasets
Stable examples and references support repeatable comparisons and error analysis.

Revisit I17.

## Experiments
Controlled experiment inputs are necessary to interpret version differences.

Revisit I18.

## Evaluator alignment
Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs.

Revisit I20.

## Dataset leakage
Tuning on evaluation labels leaks information and overstates generalization.

Revisit I18.

## Boundary tests
Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states.

Revisit B14.

## Release gates
A metric validates only its defined property; retrieval relevance and answer correctness are separate.

Revisit C05.

## Graph export
A graph declaration is a deployment input, not evidence that a remote deployment exists or works.

Revisit A08.

## Deployment revision
Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy.

Revisit A09.

## Assistants
Assistants configure graph behavior; deployments, threads, and identities have different responsibilities.

Revisit A09.

## Threads
Threads organize continuing state; runs represent executions within or against that state.

Revisit A10.

## Runs
Acceptance and execution completion are different states and need separate evidence.

Revisit A10.

## Authentication
Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims.

Revisit A11.

## Authorization
Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure.

Revisit C02.

## Secrets
Secrets belong in secure configuration; transport verification and least-privilege access remain necessary.

Revisit A12.

## Durability
Durability guarantees depend on the storage and failure model; a local database is not multi-region replication.

Revisit A13.

## Regional failover
Health, revision freshness, and availability are separate inputs to failover policy.

Revisit A14.

## Trace structure
Nested and parallel work can overlap; tree structure and timing semantics matter.

Revisit A15.

## Thread analysis
Conversation-level cost and reliability require aggregation across constituent runs.

Revisit A16.

## Latency percentiles
Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles.

Revisit A17.

## Cost attribution
Cost evidence needs known token usage, pricing, and provenance before billing claims are justified.

Revisit A17.

## User sentiment
Feedback can reveal problems while still being biased and incomplete.

Revisit A18.

## Online evaluations and Insights
Per-run evaluation and exploratory aggregation answer related but different questions.

Revisit A18.

## Alerts
Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate.

Revisit A19.

## Deduplication
Deduplication reduces noise but does not establish delivery or incident resolution.

Revisit A19.

## Sampling
Sampling reduces cost but creates coverage limits that must remain visible.

Revisit I19.

## Trace privacy
Privacy controls and delivery verification are separate; local IDs are not cloud evidence.

Revisit B20.
