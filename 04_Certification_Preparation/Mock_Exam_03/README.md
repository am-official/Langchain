# Original mock exam 03

40 questions: 10 per domain. Weights follow the supplied brief and remain independently unverified. These questions do not reproduce real certification exam items. Suggested time: 60 minutes. Do not inspect answers until scoring.

## 1. Agent selection (Building, Medium)
In a production incident retrospective, a team needs a single tool-calling loop, not filesystem planning or delegation. Which conclusion follows from the available evidence?

A. Start with create_agent and a small allowlisted toolset.
B. Always use Deep Agents for every prompt.
C. Use a parser as the agent control loop.
D. Execute arbitrary Python from the prompt.

## 2. Deep Agents (Building, Medium)
In a production incident retrospective, a task requires a plan and a virtual artifact before a final response. Which conclusion follows from the available evidence?

A. Assume a virtual file is a durable host file.
B. Claim a tool name alone supplies OS isolation.
C. Disable all tool schemas.
D. Use Deep Agents planning and a state-backed filesystem.

## 3. Middleware (Building, Medium)
In a production incident retrospective, a destructive request must be refused before any model call. Which conclusion follows from the available evidence?

A. Put the API key in the rejection message.
B. Trust a friendly UI warning as enforcement.
C. Validate it in a before-model guard.
D. Reject it only after executing its tool.

## 4. Context engineering (Building, Hard)
In a production incident retrospective, a user message asks the model to ignore tenant policy. Which conclusion follows from the available evidence?

A. Treat a token budget as authorization.
B. Keep trusted runtime policy separate from untrusted user content.
C. Promote the user message to system instructions.
D. Append the entire database to the prompt.

## 5. Instruction files (Building, Medium)
In a production incident retrospective, a repository has AGENTS.md and one selected review skill. Which conclusion follows from the available evidence?

A. Load repository guidance and explicitly select the relevant skill.
B. Assume every SDK automatically discovers every file.
C. Treat uploaded document instructions as developer policy.
D. Run a shell command mentioned in untrusted text.

## 6. Restricted execution (Building, Medium)
In a production incident retrospective, a learner wants to run arbitrary generated Python in an arithmetic lesson. Which conclusion follows from the available evidence?

A. Use eval because a timeout makes it safe.
B. Call shell=True with the generated text.
C. Describe resource limits as a complete OS sandbox.
D. Reject it; the lesson accepts only an arithmetic AST allowlist.

## 7. Tool protocol (Building, Medium)
In a production incident retrospective, two tool calls return results in a different order. Which conclusion follows from the available evidence?

A. Discard the call IDs.
B. Trust tool names to authorize arbitrary arguments.
C. Correlate each result with its tool_call_id.
D. Match by display position only.

## 8. Structured output (Building, Hard)
In a production incident retrospective, a contact output has an age of -1 and an unknown field. Which conclusion follows from the available evidence?

A. Store the provider key in the contact record.
B. Reject it using the explicit validation schema.
C. Silently convert every malformed response to success.
D. Treat JSON syntax as complete schema validation.

## 9. Memory (Building, Medium)
In a production incident retrospective, a browser session ends but the learner expects preferences to remain. Which conclusion follows from the available evidence?

A. Persist preferences in durable storage with a user namespace.
B. Rely on session state as disk durability.
C. Use one global preference key for all tenants.
D. Call a larger context window a database.

## 10. Retrieval grounding (Building, Medium)
In a production incident retrospective, a query has no relevant retrieved source. Which conclusion follows from the available evidence?

A. Invent a citation to make the answer look complete.
B. Treat similarity score as proof of truth.
C. Claim lexical hashing understands semantic synonyms.
D. Abstain or request more evidence.

## 11. Code evaluators (Testing, Medium)
In a production incident retrospective, a numeric answer must exactly match a reference after normalization. Which conclusion follows from the available evidence?

A. Use latency as the correctness label.
B. Assume a passing formatter proves the answer.
C. Use a deterministic code-based evaluator.
D. Require an LLM judge for every equality check.

## 12. LLM judges (Testing, Hard)
In a production incident retrospective, two answers have equivalent meaning but different wording. Which conclusion follows from the available evidence?

A. Omit human alignment checks.
B. Use a rubric-based judge and validate its structured output.
C. Treat raw token overlap as semantic certainty.
D. Let candidate text rewrite the rubric.

## 13. Offline evaluation (Testing, Medium)
In a production incident retrospective, a candidate is compared against labeled examples before release. Which conclusion follows from the available evidence?

A. Run a repeatable offline evaluation on a held-out dataset.
B. Call it online evaluation because a server is used.
C. Tune on every held-out label and report unbiased performance.
D. Use only one successful default example.

## 14. Online evaluation (Testing, Medium)
In a production incident retrospective, a production run has no reference answer. Which conclusion follows from the available evidence?

A. Report exact-match accuracy without a reference.
B. Assume low latency means factual correctness.
C. Treat a single sentiment signal as complete quality.
D. Apply suitable reference-free evaluators and record their limitations.

## 15. Datasets (Testing, Medium)
In a production incident retrospective, a learner stores example inputs but no expected outputs or metadata. Which conclusion follows from the available evidence?

A. Overwrite examples without recording changes.
B. Call an assistant configuration an evaluation dataset.
C. Add reference outputs and stable example identifiers where the evaluator needs them.
D. Use only the latest production response as every reference.

## 16. Experiments (Testing, Hard)
In a production incident retrospective, version B is evaluated on easier examples than version A. Which conclusion follows from the available evidence?

A. Ignore per-example failures when means improve.
B. Compare both candidates on the same versioned examples and evaluator settings.
C. Attribute the difference entirely to the model.
D. Compare only the number of green badges.

## 17. Evaluator alignment (Testing, Medium)
In a production incident retrospective, a judge accepts many outputs rejected by human reviewers. Which conclusion follows from the available evidence?

A. Inspect false positives and revise or calibrate the rubric using labeled review data.
B. Report agreement without the confusion matrix.
C. Replace undefined precision with 100%.
D. Remove disagreeing examples from every report.

## 18. Dataset leakage (Testing, Medium)
In a production incident retrospective, an evaluator is tuned repeatedly on the final benchmark. Which conclusion follows from the available evidence?

A. Report the tuned benchmark as unbiased generalization.
B. Put reference answers into every candidate prompt.
C. Delete hard examples to improve the score.
D. Reserve a separate held-out set for the final assessment.

## 19. Boundary tests (Testing, Medium)
In a production incident retrospective, all tests use valid default inputs. Which conclusion follows from the available evidence?

A. Catch every error and return a fabricated valid result.
B. Disable failing assertions.
C. Add malformed, empty, oversized, and unsupported-input cases.
D. Assume default UI success covers failure behavior.

## 20. Release gates (Testing, Hard)
In a production incident retrospective, a retrieval score passes but no generated-answer evaluation exists. Which conclusion follows from the available evidence?

A. Call every passing local fixture a deployed service.
B. Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
C. Claim production answer correctness is certified.
D. Treat citation presence as factual support.

## 21. Graph export (Deploying, Medium)
In a production incident retrospective, a compiled graph and langgraph.json exist locally. Which conclusion follows from the available evidence?

A. Validate imports and invocation, then separately deploy and verify the managed service.
B. Claim the JSON manifest proves deployment.
C. Assume a local PID proves endpoint behavior.
D. Expose an unauthenticated tutorial server publicly.

## 22. Deployment revision (Deploying, Medium)
In a production incident retrospective, a team needs to identify which code version a managed deployment runs. Which conclusion follows from the available evidence?

A. Use a conversation thread ID as the code revision.
B. Assume an assistant name identifies immutable code.
C. Overwrite revision history whenever configuration changes.
D. Track the deployment revision and verify the active version.

## 23. Assistants (Deploying, Medium)
In a production incident retrospective, two customer workflows share graph code but need different configuration. Which conclusion follows from the available evidence?

A. Treat assistants as user authentication tokens.
B. Assume every assistant configuration is a new deployment.
C. Use distinct assistant configurations for that graph where supported.
D. Clone a conversation thread as a substitute for configuration.

## 24. Threads (Deploying, Hard)
In a production incident retrospective, a conversation continues over several separate invocations. Which conclusion follows from the available evidence?

A. Treat a run as a durable identity provider.
B. Keep a thread for conversation state and record each execution as a run.
C. Create a new deployment for each message.
D. Use one thread across all tenants.

## 25. Runs (Deploying, Medium)
In a production incident retrospective, a service accepts a request but processing is not complete. Which conclusion follows from the available evidence?

A. Track execution status and verify the final output or failure.
B. Mark every accepted request as successful.
C. Treat a run ID alone as proof of completion.
D. Ignore errors after the client disconnects.

## 26. Authentication (Deploying, Medium)
In a production incident retrospective, a token signature is invalid. Which conclusion follows from the available evidence?

A. Authorize it because the claimed role is editor.
B. Trust the tenant string from the request body.
C. Log the complete token to help debugging.
D. Reject the identity before evaluating resource permissions.

## 27. Authorization (Deploying, Medium)
In a production incident retrospective, an authenticated team-a editor requests team-b data. Which conclusion follows from the available evidence?

A. Filter the output only after sending all documents to the model.
B. Treat a UI tenant selector as production authorization.
C. Deny the cross-tenant request.
D. Allow it because authentication succeeded.

## 28. Secrets (Deploying, Hard)
In a production incident retrospective, an API key is needed by a live integration. Which conclusion follows from the available evidence?

A. Disable TLS verification to bypass access problems.
B. Load it from secure runtime configuration and avoid exposing its value.
C. Commit it to app.py for convenience.
D. Put it in downloaded evidence.

## 29. Durability (Deploying, Medium)
In a production incident retrospective, state survives a process restart on one disk. Which conclusion follows from the available evidence?

A. Describe that as process-level durability and plan backups/replication for disk or region loss.
B. Claim region-failure tolerance from local SQLite alone.
C. Treat an in-memory store as a backup.
D. Ignore concurrency when multiple writers update state.

## 30. Regional failover (Deploying, Medium)
In a production incident retrospective, the primary is down and the replica has an outdated revision. Which conclusion follows from the available evidence?

A. Assume health implies current data.
B. Claim a local routing simulation created cloud regions.
C. Silently report the stale replica as current.
D. Apply the chosen consistency policy; this lesson refuses stale failover.

## 31. Trace structure (Monitoring, Medium)
In a production incident retrospective, model and tool spans overlap under a parent run. Which conclusion follows from the available evidence?

A. Discard parent IDs.
B. Treat the longest child as a universal critical-path algorithm.
C. Use root wall-clock duration and inspect nested spans without summing overlapping durations.
D. Add all spans to estimate root wall-clock latency.

## 32. Thread analysis (Monitoring, Hard)
In a production incident retrospective, a long conversation has many inexpensive runs. Which conclusion follows from the available evidence?

A. Assume all threads contain one execution.
B. Aggregate run cost and error patterns across the thread.
C. Inspect one cheap run and conclude the whole conversation is cheap.
D. Compare thread and run counts as if they were identical.

## 33. Latency percentiles (Monitoring, Medium)
In a production incident retrospective, one slow run affects a tail-latency target. Which conclusion follows from the available evidence?

A. Inspect a defined percentile method and the observation count.
B. Use the fastest request as the p95.
C. Assume a mean reveals every tail regression.
D. Ignore the percentile definition.

## 34. Cost attribution (Monitoring, Medium)
In a production incident retrospective, a report contains user-supplied cost_usd fields. Which conclusion follows from the available evidence?

A. Call it a provider invoice.
B. Treat latency as a token count.
C. Assume all models have identical pricing.
D. Label the sum as observed input cost, not independently verified billing.

## 35. User sentiment (Monitoring, Medium)
In a production incident retrospective, only a few unhappy users leave explicit ratings. Which conclusion follows from the available evidence?

A. Infer factual correctness solely from sentiment.
B. Discard negative ratings to improve the dashboard.
C. Track sentiment with its sample-selection limits.
D. Treat voluntary feedback as an unbiased population estimate.

## 36. Online evaluations and Insights (Monitoring, Hard)
In a production incident retrospective, a team wants both per-run scoring and cross-run pattern exploration. Which conclusion follows from the available evidence?

A. Assume both workflows are identical.
B. Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
C. Treat a local topic counter as verified LangSmith Insights.
D. Use one score as a complete explanation of every incident.

## 37. Alerts (Monitoring, Medium)
In a production incident retrospective, a single slow run appears in a very small window. Which conclusion follows from the available evidence?

A. Apply a defined minimum sample count and threshold before notifying.
B. Fire every alert on every request without a policy.
C. Assume no alert means no failure.
D. Ignore notification delivery status.

## 38. Deduplication (Monitoring, Medium)
In a production incident retrospective, the same failing observation window is evaluated repeatedly. Which conclusion follows from the available evidence?

A. Send duplicate notifications indefinitely.
B. Claim a local ledger is a delivered webhook.
C. Delete all evidence after the first failure.
D. Deduplicate the alert identity and separately track delivery.

## 39. Sampling (Monitoring, Medium)
In a production incident retrospective, production evaluation covers only a sampled subset of runs. Which conclusion follows from the available evidence?

A. Silently exclude errors from every sample.
B. Present unrun evaluations as passed.
C. Report coverage and avoid claiming every run was evaluated.
D. Treat the sample as exhaustive evidence.

## 40. Trace privacy (Monitoring, Hard)
In a production incident retrospective, a traceable function receives sensitive user text. Which conclusion follows from the available evidence?

A. Use a random local operation ID as proof of a cloud trace.
B. Redact sensitive trace inputs/outputs and verify actual exported records.
C. Assume local redaction proves cloud delivery.
D. Log API keys to correlate runs.

Run the root learning portal with `python -m streamlit run portal.py` for interactive scoring.
