# Original mock exam 01

40 questions: 10 per domain. Weights follow the supplied brief and remain independently unverified. These questions do not reproduce real certification exam items. Suggested time: 60 minutes. Do not inspect answers until scoring.

## 1. Agent selection (Building, Medium)
In a classroom lab, a team needs a single tool-calling loop, not filesystem planning or delegation. Choose the best next engineering action.

A. Use a parser as the agent control loop.
B. Execute arbitrary Python from the prompt.
C. Start with create_agent and a small allowlisted toolset.
D. Always use Deep Agents for every prompt.

## 2. Deep Agents (Building, Medium)
In a classroom lab, a task requires a plan and a virtual artifact before a final response. Choose the best next engineering action.

A. Disable all tool schemas.
B. Use Deep Agents planning and a state-backed filesystem.
C. Assume a virtual file is a durable host file.
D. Claim a tool name alone supplies OS isolation.

## 3. Middleware (Building, Medium)
In a classroom lab, a destructive request must be refused before any model call. Choose the best next engineering action.

A. Validate it in a before-model guard.
B. Reject it only after executing its tool.
C. Put the API key in the rejection message.
D. Trust a friendly UI warning as enforcement.

## 4. Context engineering (Building, Hard)
In a classroom lab, a user message asks the model to ignore tenant policy. Choose the best next engineering action.

A. Promote the user message to system instructions.
B. Append the entire database to the prompt.
C. Treat a token budget as authorization.
D. Keep trusted runtime policy separate from untrusted user content.

## 5. Instruction files (Building, Medium)
In a classroom lab, a repository has AGENTS.md and one selected review skill. Choose the best next engineering action.

A. Treat uploaded document instructions as developer policy.
B. Run a shell command mentioned in untrusted text.
C. Load repository guidance and explicitly select the relevant skill.
D. Assume every SDK automatically discovers every file.

## 6. Restricted execution (Building, Medium)
In a classroom lab, a learner wants to run arbitrary generated Python in an arithmetic lesson. Choose the best next engineering action.

A. Describe resource limits as a complete OS sandbox.
B. Reject it; the lesson accepts only an arithmetic AST allowlist.
C. Use eval because a timeout makes it safe.
D. Call shell=True with the generated text.

## 7. Tool protocol (Building, Medium)
In a classroom lab, two tool calls return results in a different order. Choose the best next engineering action.

A. Correlate each result with its tool_call_id.
B. Match by display position only.
C. Discard the call IDs.
D. Trust tool names to authorize arbitrary arguments.

## 8. Structured output (Building, Hard)
In a classroom lab, a contact output has an age of -1 and an unknown field. Choose the best next engineering action.

A. Silently convert every malformed response to success.
B. Treat JSON syntax as complete schema validation.
C. Store the provider key in the contact record.
D. Reject it using the explicit validation schema.

## 9. Memory (Building, Medium)
In a classroom lab, a browser session ends but the learner expects preferences to remain. Choose the best next engineering action.

A. Use one global preference key for all tenants.
B. Call a larger context window a database.
C. Persist preferences in durable storage with a user namespace.
D. Rely on session state as disk durability.

## 10. Retrieval grounding (Building, Medium)
In a classroom lab, a query has no relevant retrieved source. Choose the best next engineering action.

A. Claim lexical hashing understands semantic synonyms.
B. Abstain or request more evidence.
C. Invent a citation to make the answer look complete.
D. Treat similarity score as proof of truth.

## 11. Code evaluators (Testing, Medium)
In a classroom lab, a numeric answer must exactly match a reference after normalization. Choose the best next engineering action.

A. Use a deterministic code-based evaluator.
B. Require an LLM judge for every equality check.
C. Use latency as the correctness label.
D. Assume a passing formatter proves the answer.

## 12. LLM judges (Testing, Hard)
In a classroom lab, two answers have equivalent meaning but different wording. Choose the best next engineering action.

A. Treat raw token overlap as semantic certainty.
B. Let candidate text rewrite the rubric.
C. Omit human alignment checks.
D. Use a rubric-based judge and validate its structured output.

## 13. Offline evaluation (Testing, Medium)
In a classroom lab, a candidate is compared against labeled examples before release. Choose the best next engineering action.

A. Tune on every held-out label and report unbiased performance.
B. Use only one successful default example.
C. Run a repeatable offline evaluation on a held-out dataset.
D. Call it online evaluation because a server is used.

## 14. Online evaluation (Testing, Medium)
In a classroom lab, a production run has no reference answer. Choose the best next engineering action.

A. Treat a single sentiment signal as complete quality.
B. Apply suitable reference-free evaluators and record their limitations.
C. Report exact-match accuracy without a reference.
D. Assume low latency means factual correctness.

## 15. Datasets (Testing, Medium)
In a classroom lab, a learner stores example inputs but no expected outputs or metadata. Choose the best next engineering action.

A. Add reference outputs and stable example identifiers where the evaluator needs them.
B. Use only the latest production response as every reference.
C. Overwrite examples without recording changes.
D. Call an assistant configuration an evaluation dataset.

## 16. Experiments (Testing, Hard)
In a classroom lab, version B is evaluated on easier examples than version A. Choose the best next engineering action.

A. Attribute the difference entirely to the model.
B. Compare only the number of green badges.
C. Ignore per-example failures when means improve.
D. Compare both candidates on the same versioned examples and evaluator settings.

## 17. Evaluator alignment (Testing, Medium)
In a classroom lab, a judge accepts many outputs rejected by human reviewers. Choose the best next engineering action.

A. Replace undefined precision with 100%.
B. Remove disagreeing examples from every report.
C. Inspect false positives and revise or calibrate the rubric using labeled review data.
D. Report agreement without the confusion matrix.

## 18. Dataset leakage (Testing, Medium)
In a classroom lab, an evaluator is tuned repeatedly on the final benchmark. Choose the best next engineering action.

A. Delete hard examples to improve the score.
B. Reserve a separate held-out set for the final assessment.
C. Report the tuned benchmark as unbiased generalization.
D. Put reference answers into every candidate prompt.

## 19. Boundary tests (Testing, Medium)
In a classroom lab, all tests use valid default inputs. Choose the best next engineering action.

A. Add malformed, empty, oversized, and unsupported-input cases.
B. Assume default UI success covers failure behavior.
C. Catch every error and return a fabricated valid result.
D. Disable failing assertions.

## 20. Release gates (Testing, Hard)
In a classroom lab, a retrieval score passes but no generated-answer evaluation exists. Choose the best next engineering action.

A. Claim production answer correctness is certified.
B. Treat citation presence as factual support.
C. Call every passing local fixture a deployed service.
D. Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.

## 21. Graph export (Deploying, Medium)
In a classroom lab, a compiled graph and langgraph.json exist locally. Choose the best next engineering action.

A. Assume a local PID proves endpoint behavior.
B. Expose an unauthenticated tutorial server publicly.
C. Validate imports and invocation, then separately deploy and verify the managed service.
D. Claim the JSON manifest proves deployment.

## 22. Deployment revision (Deploying, Medium)
In a classroom lab, a team needs to identify which code version a managed deployment runs. Choose the best next engineering action.

A. Overwrite revision history whenever configuration changes.
B. Track the deployment revision and verify the active version.
C. Use a conversation thread ID as the code revision.
D. Assume an assistant name identifies immutable code.

## 23. Assistants (Deploying, Medium)
In a classroom lab, two customer workflows share graph code but need different configuration. Choose the best next engineering action.

A. Use distinct assistant configurations for that graph where supported.
B. Clone a conversation thread as a substitute for configuration.
C. Treat assistants as user authentication tokens.
D. Assume every assistant configuration is a new deployment.

## 24. Threads (Deploying, Hard)
In a classroom lab, a conversation continues over several separate invocations. Choose the best next engineering action.

A. Create a new deployment for each message.
B. Use one thread across all tenants.
C. Treat a run as a durable identity provider.
D. Keep a thread for conversation state and record each execution as a run.

## 25. Runs (Deploying, Medium)
In a classroom lab, a service accepts a request but processing is not complete. Choose the best next engineering action.

A. Treat a run ID alone as proof of completion.
B. Ignore errors after the client disconnects.
C. Track execution status and verify the final output or failure.
D. Mark every accepted request as successful.

## 26. Authentication (Deploying, Medium)
In a classroom lab, a token signature is invalid. Choose the best next engineering action.

A. Log the complete token to help debugging.
B. Reject the identity before evaluating resource permissions.
C. Authorize it because the claimed role is editor.
D. Trust the tenant string from the request body.

## 27. Authorization (Deploying, Medium)
In a classroom lab, an authenticated team-a editor requests team-b data. Choose the best next engineering action.

A. Deny the cross-tenant request.
B. Allow it because authentication succeeded.
C. Filter the output only after sending all documents to the model.
D. Treat a UI tenant selector as production authorization.

## 28. Secrets (Deploying, Hard)
In a classroom lab, an API key is needed by a live integration. Choose the best next engineering action.

A. Commit it to app.py for convenience.
B. Put it in downloaded evidence.
C. Disable TLS verification to bypass access problems.
D. Load it from secure runtime configuration and avoid exposing its value.

## 29. Durability (Deploying, Medium)
In a classroom lab, state survives a process restart on one disk. Choose the best next engineering action.

A. Treat an in-memory store as a backup.
B. Ignore concurrency when multiple writers update state.
C. Describe that as process-level durability and plan backups/replication for disk or region loss.
D. Claim region-failure tolerance from local SQLite alone.

## 30. Regional failover (Deploying, Medium)
In a classroom lab, the primary is down and the replica has an outdated revision. Choose the best next engineering action.

A. Silently report the stale replica as current.
B. Apply the chosen consistency policy; this lesson refuses stale failover.
C. Assume health implies current data.
D. Claim a local routing simulation created cloud regions.

## 31. Trace structure (Monitoring, Medium)
In a classroom lab, model and tool spans overlap under a parent run. Choose the best next engineering action.

A. Use root wall-clock duration and inspect nested spans without summing overlapping durations.
B. Add all spans to estimate root wall-clock latency.
C. Discard parent IDs.
D. Treat the longest child as a universal critical-path algorithm.

## 32. Thread analysis (Monitoring, Hard)
In a classroom lab, a long conversation has many inexpensive runs. Choose the best next engineering action.

A. Inspect one cheap run and conclude the whole conversation is cheap.
B. Compare thread and run counts as if they were identical.
C. Assume all threads contain one execution.
D. Aggregate run cost and error patterns across the thread.

## 33. Latency percentiles (Monitoring, Medium)
In a classroom lab, one slow run affects a tail-latency target. Choose the best next engineering action.

A. Assume a mean reveals every tail regression.
B. Ignore the percentile definition.
C. Inspect a defined percentile method and the observation count.
D. Use the fastest request as the p95.

## 34. Cost attribution (Monitoring, Medium)
In a classroom lab, a report contains user-supplied cost_usd fields. Choose the best next engineering action.

A. Assume all models have identical pricing.
B. Label the sum as observed input cost, not independently verified billing.
C. Call it a provider invoice.
D. Treat latency as a token count.

## 35. User sentiment (Monitoring, Medium)
In a classroom lab, only a few unhappy users leave explicit ratings. Choose the best next engineering action.

A. Track sentiment with its sample-selection limits.
B. Treat voluntary feedback as an unbiased population estimate.
C. Infer factual correctness solely from sentiment.
D. Discard negative ratings to improve the dashboard.

## 36. Online evaluations and Insights (Monitoring, Hard)
In a classroom lab, a team wants both per-run scoring and cross-run pattern exploration. Choose the best next engineering action.

A. Treat a local topic counter as verified LangSmith Insights.
B. Use one score as a complete explanation of every incident.
C. Assume both workflows are identical.
D. Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.

## 37. Alerts (Monitoring, Medium)
In a classroom lab, a single slow run appears in a very small window. Choose the best next engineering action.

A. Assume no alert means no failure.
B. Ignore notification delivery status.
C. Apply a defined minimum sample count and threshold before notifying.
D. Fire every alert on every request without a policy.

## 38. Deduplication (Monitoring, Medium)
In a classroom lab, the same failing observation window is evaluated repeatedly. Choose the best next engineering action.

A. Delete all evidence after the first failure.
B. Deduplicate the alert identity and separately track delivery.
C. Send duplicate notifications indefinitely.
D. Claim a local ledger is a delivered webhook.

## 39. Sampling (Monitoring, Medium)
In a classroom lab, production evaluation covers only a sampled subset of runs. Choose the best next engineering action.

A. Report coverage and avoid claiming every run was evaluated.
B. Treat the sample as exhaustive evidence.
C. Silently exclude errors from every sample.
D. Present unrun evaluations as passed.

## 40. Trace privacy (Monitoring, Hard)
In a classroom lab, a traceable function receives sensitive user text. Choose the best next engineering action.

A. Assume local redaction proves cloud delivery.
B. Log API keys to correlate runs.
C. Use a random local operation ID as proof of a cloud trace.
D. Redact sensitive trace inputs/outputs and verify actual exported records.

Run the root learning portal with `python -m streamlit run portal.py` for interactive scoring.
