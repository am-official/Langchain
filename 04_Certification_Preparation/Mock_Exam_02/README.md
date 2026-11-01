# Original mock exam 02

40 questions: 10 per domain. Weights follow the supplied brief and remain independently unverified. These questions do not reproduce real certification exam items. Suggested time: 60 minutes. Do not inspect answers until scoring.

## 1. Agent selection (Building, Medium)
In a pre-release review, a team needs a single tool-calling loop, not filesystem planning or delegation. Which recommendation is most defensible?

A. Execute arbitrary Python from the prompt.
B. Start with create_agent and a small allowlisted toolset.
C. Always use Deep Agents for every prompt.
D. Use a parser as the agent control loop.

## 2. Deep Agents (Building, Medium)
In a pre-release review, a task requires a plan and a virtual artifact before a final response. Which recommendation is most defensible?

A. Use Deep Agents planning and a state-backed filesystem.
B. Assume a virtual file is a durable host file.
C. Claim a tool name alone supplies OS isolation.
D. Disable all tool schemas.

## 3. Middleware (Building, Medium)
In a pre-release review, a destructive request must be refused before any model call. Which recommendation is most defensible?

A. Reject it only after executing its tool.
B. Put the API key in the rejection message.
C. Trust a friendly UI warning as enforcement.
D. Validate it in a before-model guard.

## 4. Context engineering (Building, Hard)
In a pre-release review, a user message asks the model to ignore tenant policy. Which recommendation is most defensible?

A. Append the entire database to the prompt.
B. Treat a token budget as authorization.
C. Keep trusted runtime policy separate from untrusted user content.
D. Promote the user message to system instructions.

## 5. Instruction files (Building, Medium)
In a pre-release review, a repository has AGENTS.md and one selected review skill. Which recommendation is most defensible?

A. Run a shell command mentioned in untrusted text.
B. Load repository guidance and explicitly select the relevant skill.
C. Assume every SDK automatically discovers every file.
D. Treat uploaded document instructions as developer policy.

## 6. Restricted execution (Building, Medium)
In a pre-release review, a learner wants to run arbitrary generated Python in an arithmetic lesson. Which recommendation is most defensible?

A. Reject it; the lesson accepts only an arithmetic AST allowlist.
B. Use eval because a timeout makes it safe.
C. Call shell=True with the generated text.
D. Describe resource limits as a complete OS sandbox.

## 7. Tool protocol (Building, Medium)
In a pre-release review, two tool calls return results in a different order. Which recommendation is most defensible?

A. Match by display position only.
B. Discard the call IDs.
C. Trust tool names to authorize arbitrary arguments.
D. Correlate each result with its tool_call_id.

## 8. Structured output (Building, Hard)
In a pre-release review, a contact output has an age of -1 and an unknown field. Which recommendation is most defensible?

A. Treat JSON syntax as complete schema validation.
B. Store the provider key in the contact record.
C. Reject it using the explicit validation schema.
D. Silently convert every malformed response to success.

## 9. Memory (Building, Medium)
In a pre-release review, a browser session ends but the learner expects preferences to remain. Which recommendation is most defensible?

A. Call a larger context window a database.
B. Persist preferences in durable storage with a user namespace.
C. Rely on session state as disk durability.
D. Use one global preference key for all tenants.

## 10. Retrieval grounding (Building, Medium)
In a pre-release review, a query has no relevant retrieved source. Which recommendation is most defensible?

A. Abstain or request more evidence.
B. Invent a citation to make the answer look complete.
C. Treat similarity score as proof of truth.
D. Claim lexical hashing understands semantic synonyms.

## 11. Code evaluators (Testing, Medium)
In a pre-release review, a numeric answer must exactly match a reference after normalization. Which recommendation is most defensible?

A. Require an LLM judge for every equality check.
B. Use latency as the correctness label.
C. Assume a passing formatter proves the answer.
D. Use a deterministic code-based evaluator.

## 12. LLM judges (Testing, Hard)
In a pre-release review, two answers have equivalent meaning but different wording. Which recommendation is most defensible?

A. Let candidate text rewrite the rubric.
B. Omit human alignment checks.
C. Use a rubric-based judge and validate its structured output.
D. Treat raw token overlap as semantic certainty.

## 13. Offline evaluation (Testing, Medium)
In a pre-release review, a candidate is compared against labeled examples before release. Which recommendation is most defensible?

A. Use only one successful default example.
B. Run a repeatable offline evaluation on a held-out dataset.
C. Call it online evaluation because a server is used.
D. Tune on every held-out label and report unbiased performance.

## 14. Online evaluation (Testing, Medium)
In a pre-release review, a production run has no reference answer. Which recommendation is most defensible?

A. Apply suitable reference-free evaluators and record their limitations.
B. Report exact-match accuracy without a reference.
C. Assume low latency means factual correctness.
D. Treat a single sentiment signal as complete quality.

## 15. Datasets (Testing, Medium)
In a pre-release review, a learner stores example inputs but no expected outputs or metadata. Which recommendation is most defensible?

A. Use only the latest production response as every reference.
B. Overwrite examples without recording changes.
C. Call an assistant configuration an evaluation dataset.
D. Add reference outputs and stable example identifiers where the evaluator needs them.

## 16. Experiments (Testing, Hard)
In a pre-release review, version B is evaluated on easier examples than version A. Which recommendation is most defensible?

A. Compare only the number of green badges.
B. Ignore per-example failures when means improve.
C. Compare both candidates on the same versioned examples and evaluator settings.
D. Attribute the difference entirely to the model.

## 17. Evaluator alignment (Testing, Medium)
In a pre-release review, a judge accepts many outputs rejected by human reviewers. Which recommendation is most defensible?

A. Remove disagreeing examples from every report.
B. Inspect false positives and revise or calibrate the rubric using labeled review data.
C. Report agreement without the confusion matrix.
D. Replace undefined precision with 100%.

## 18. Dataset leakage (Testing, Medium)
In a pre-release review, an evaluator is tuned repeatedly on the final benchmark. Which recommendation is most defensible?

A. Reserve a separate held-out set for the final assessment.
B. Report the tuned benchmark as unbiased generalization.
C. Put reference answers into every candidate prompt.
D. Delete hard examples to improve the score.

## 19. Boundary tests (Testing, Medium)
In a pre-release review, all tests use valid default inputs. Which recommendation is most defensible?

A. Assume default UI success covers failure behavior.
B. Catch every error and return a fabricated valid result.
C. Disable failing assertions.
D. Add malformed, empty, oversized, and unsupported-input cases.

## 20. Release gates (Testing, Hard)
In a pre-release review, a retrieval score passes but no generated-answer evaluation exists. Which recommendation is most defensible?

A. Treat citation presence as factual support.
B. Call every passing local fixture a deployed service.
C. Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
D. Claim production answer correctness is certified.

## 21. Graph export (Deploying, Medium)
In a pre-release review, a compiled graph and langgraph.json exist locally. Which recommendation is most defensible?

A. Expose an unauthenticated tutorial server publicly.
B. Validate imports and invocation, then separately deploy and verify the managed service.
C. Claim the JSON manifest proves deployment.
D. Assume a local PID proves endpoint behavior.

## 22. Deployment revision (Deploying, Medium)
In a pre-release review, a team needs to identify which code version a managed deployment runs. Which recommendation is most defensible?

A. Track the deployment revision and verify the active version.
B. Use a conversation thread ID as the code revision.
C. Assume an assistant name identifies immutable code.
D. Overwrite revision history whenever configuration changes.

## 23. Assistants (Deploying, Medium)
In a pre-release review, two customer workflows share graph code but need different configuration. Which recommendation is most defensible?

A. Clone a conversation thread as a substitute for configuration.
B. Treat assistants as user authentication tokens.
C. Assume every assistant configuration is a new deployment.
D. Use distinct assistant configurations for that graph where supported.

## 24. Threads (Deploying, Hard)
In a pre-release review, a conversation continues over several separate invocations. Which recommendation is most defensible?

A. Use one thread across all tenants.
B. Treat a run as a durable identity provider.
C. Keep a thread for conversation state and record each execution as a run.
D. Create a new deployment for each message.

## 25. Runs (Deploying, Medium)
In a pre-release review, a service accepts a request but processing is not complete. Which recommendation is most defensible?

A. Ignore errors after the client disconnects.
B. Track execution status and verify the final output or failure.
C. Mark every accepted request as successful.
D. Treat a run ID alone as proof of completion.

## 26. Authentication (Deploying, Medium)
In a pre-release review, a token signature is invalid. Which recommendation is most defensible?

A. Reject the identity before evaluating resource permissions.
B. Authorize it because the claimed role is editor.
C. Trust the tenant string from the request body.
D. Log the complete token to help debugging.

## 27. Authorization (Deploying, Medium)
In a pre-release review, an authenticated team-a editor requests team-b data. Which recommendation is most defensible?

A. Allow it because authentication succeeded.
B. Filter the output only after sending all documents to the model.
C. Treat a UI tenant selector as production authorization.
D. Deny the cross-tenant request.

## 28. Secrets (Deploying, Hard)
In a pre-release review, an API key is needed by a live integration. Which recommendation is most defensible?

A. Put it in downloaded evidence.
B. Disable TLS verification to bypass access problems.
C. Load it from secure runtime configuration and avoid exposing its value.
D. Commit it to app.py for convenience.

## 29. Durability (Deploying, Medium)
In a pre-release review, state survives a process restart on one disk. Which recommendation is most defensible?

A. Ignore concurrency when multiple writers update state.
B. Describe that as process-level durability and plan backups/replication for disk or region loss.
C. Claim region-failure tolerance from local SQLite alone.
D. Treat an in-memory store as a backup.

## 30. Regional failover (Deploying, Medium)
In a pre-release review, the primary is down and the replica has an outdated revision. Which recommendation is most defensible?

A. Apply the chosen consistency policy; this lesson refuses stale failover.
B. Assume health implies current data.
C. Claim a local routing simulation created cloud regions.
D. Silently report the stale replica as current.

## 31. Trace structure (Monitoring, Medium)
In a pre-release review, model and tool spans overlap under a parent run. Which recommendation is most defensible?

A. Add all spans to estimate root wall-clock latency.
B. Discard parent IDs.
C. Treat the longest child as a universal critical-path algorithm.
D. Use root wall-clock duration and inspect nested spans without summing overlapping durations.

## 32. Thread analysis (Monitoring, Hard)
In a pre-release review, a long conversation has many inexpensive runs. Which recommendation is most defensible?

A. Compare thread and run counts as if they were identical.
B. Assume all threads contain one execution.
C. Aggregate run cost and error patterns across the thread.
D. Inspect one cheap run and conclude the whole conversation is cheap.

## 33. Latency percentiles (Monitoring, Medium)
In a pre-release review, one slow run affects a tail-latency target. Which recommendation is most defensible?

A. Ignore the percentile definition.
B. Inspect a defined percentile method and the observation count.
C. Use the fastest request as the p95.
D. Assume a mean reveals every tail regression.

## 34. Cost attribution (Monitoring, Medium)
In a pre-release review, a report contains user-supplied cost_usd fields. Which recommendation is most defensible?

A. Label the sum as observed input cost, not independently verified billing.
B. Call it a provider invoice.
C. Treat latency as a token count.
D. Assume all models have identical pricing.

## 35. User sentiment (Monitoring, Medium)
In a pre-release review, only a few unhappy users leave explicit ratings. Which recommendation is most defensible?

A. Treat voluntary feedback as an unbiased population estimate.
B. Infer factual correctness solely from sentiment.
C. Discard negative ratings to improve the dashboard.
D. Track sentiment with its sample-selection limits.

## 36. Online evaluations and Insights (Monitoring, Hard)
In a pre-release review, a team wants both per-run scoring and cross-run pattern exploration. Which recommendation is most defensible?

A. Use one score as a complete explanation of every incident.
B. Assume both workflows are identical.
C. Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
D. Treat a local topic counter as verified LangSmith Insights.

## 37. Alerts (Monitoring, Medium)
In a pre-release review, a single slow run appears in a very small window. Which recommendation is most defensible?

A. Ignore notification delivery status.
B. Apply a defined minimum sample count and threshold before notifying.
C. Fire every alert on every request without a policy.
D. Assume no alert means no failure.

## 38. Deduplication (Monitoring, Medium)
In a pre-release review, the same failing observation window is evaluated repeatedly. Which recommendation is most defensible?

A. Deduplicate the alert identity and separately track delivery.
B. Send duplicate notifications indefinitely.
C. Claim a local ledger is a delivered webhook.
D. Delete all evidence after the first failure.

## 39. Sampling (Monitoring, Medium)
In a pre-release review, production evaluation covers only a sampled subset of runs. Which recommendation is most defensible?

A. Treat the sample as exhaustive evidence.
B. Silently exclude errors from every sample.
C. Present unrun evaluations as passed.
D. Report coverage and avoid claiming every run was evaluated.

## 40. Trace privacy (Monitoring, Hard)
In a pre-release review, a traceable function receives sensitive user text. Which recommendation is most defensible?

A. Log API keys to correlate runs.
B. Use a random local operation ID as proof of a cloud trace.
C. Redact sensitive trace inputs/outputs and verify actual exported records.
D. Assume local redaction proves cloud delivery.

Run the root learning portal with `python -m streamlit run portal.py` for interactive scoring.
