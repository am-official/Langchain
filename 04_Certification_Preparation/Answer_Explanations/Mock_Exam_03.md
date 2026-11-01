# Mock Exam 03 — explanations

## M3-01: A — Agent selection
- **A**: create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed.
- **B**: Incorrect: this proposes “Always use Deep Agents for every prompt.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.
- **C**: Incorrect: this proposes “Use a parser as the agent control loop.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.
- **D**: Incorrect: this proposes “Execute arbitrary Python from the prompt.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.

Revisit: 02_Intermediate/I01_Create_Agent. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-02: D — Deep Agents
- **A**: Incorrect: this proposes “Assume a virtual file is a durable host file.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.
- **B**: Incorrect: this proposes “Claim a tool name alone supplies OS isolation.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.
- **C**: Incorrect: this proposes “Disable all tool schemas.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.
- **D**: Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code.

Revisit: 03_Advanced/A01_Deep_Agents_Workflows. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-03: C — Middleware
- **A**: Incorrect: this proposes “Put the API key in the rejection message.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.
- **B**: Incorrect: this proposes “Trust a friendly UI warning as enforcement.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.
- **C**: Enforcement belongs at the execution boundary, before the call or side effect it protects.
- **D**: Incorrect: this proposes “Reject it only after executing its tool.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.

Revisit: 02_Intermediate/I03_Agent_Middleware. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-04: B — Context engineering
- **A**: Incorrect: this proposes “Treat a token budget as authorization.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.
- **B**: Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns.
- **C**: Incorrect: this proposes “Promote the user message to system instructions.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.
- **D**: Incorrect: this proposes “Append the entire database to the prompt.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.

Revisit: 02_Intermediate/I05_Context_Engineering. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-05: A — Instruction files
- **A**: Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism.
- **B**: Incorrect: this proposes “Assume every SDK automatically discovers every file.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.
- **C**: Incorrect: this proposes “Treat uploaded document instructions as developer policy.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.
- **D**: Incorrect: this proposes “Run a shell command mentioned in untrusted text.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.

Revisit: 02_Intermediate/I14_AGENTS_And_SKILL_Files. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-06: D — Restricted execution
- **A**: Incorrect: this proposes “Use eval because a timeout makes it safe.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.
- **B**: Incorrect: this proposes “Call shell=True with the generated text.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.
- **C**: Incorrect: this proposes “Describe resource limits as a complete OS sandbox.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.
- **D**: Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python.

Revisit: 03_Advanced/A04_Sandboxed_Execution. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-07: C — Tool protocol
- **A**: Incorrect: this proposes “Discard the call IDs.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.
- **B**: Incorrect: this proposes “Trust tool names to authorize arbitrary arguments.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.
- **C**: Tool-call IDs tie results to requests; tool allowlists and argument validation still apply.
- **D**: Incorrect: this proposes “Match by display position only.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.

Revisit: 01_Beginner/B13_Tool_Calling. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-08: B — Structured output
- **A**: Incorrect: this proposes “Store the provider key in the contact record.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.
- **B**: Valid JSON can still violate types, bounds, and allowed fields.
- **C**: Incorrect: this proposes “Silently convert every malformed response to success.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.
- **D**: Incorrect: this proposes “Treat JSON syntax as complete schema validation.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.

Revisit: 01_Beginner/B08_Structured_Output. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-09: A — Memory
- **A**: Prompt context, browser state, and durable long-term storage have different lifetimes.
- **B**: Incorrect: this proposes “Rely on session state as disk durability.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.
- **C**: Incorrect: this proposes “Use one global preference key for all tenants.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.
- **D**: Incorrect: this proposes “Call a larger context window a database.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.

Revisit: 02_Intermediate/I06_Persistent_Memory. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-10: D — Retrieval grounding
- **A**: Incorrect: this proposes “Invent a citation to make the answer look complete.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.
- **B**: Incorrect: this proposes “Treat similarity score as proof of truth.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.
- **C**: Incorrect: this proposes “Claim lexical hashing understands semantic synonyms.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.
- **D**: Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims.

Revisit: 01_Beginner/B19_Simple_RAG. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M3-11: C — Code evaluators
- **A**: Incorrect: this proposes “Use latency as the correctness label.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.
- **B**: Incorrect: this proposes “Assume a passing formatter proves the answer.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.
- **C**: Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge.
- **D**: Incorrect: this proposes “Require an LLM judge for every equality check.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.

Revisit: 02_Intermediate/I15_Code_Based_Evaluators. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-12: B — LLM judges
- **A**: Incorrect: this proposes “Omit human alignment checks.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.
- **B**: A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration.
- **C**: Incorrect: this proposes “Treat raw token overlap as semantic certainty.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.
- **D**: Incorrect: this proposes “Let candidate text rewrite the rubric.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.

Revisit: 02_Intermediate/I16_LLM_As_Judge. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-13: A — Offline evaluation
- **A**: Offline describes the evaluation workflow on a dataset, not whether networking exists.
- **B**: Incorrect: this proposes “Call it online evaluation because a server is used.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.
- **C**: Incorrect: this proposes “Tune on every held-out label and report unbiased performance.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.
- **D**: Incorrect: this proposes “Use only one successful default example.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-14: D — Online evaluation
- **A**: Incorrect: this proposes “Report exact-match accuracy without a reference.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.
- **B**: Incorrect: this proposes “Assume low latency means factual correctness.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.
- **C**: Incorrect: this proposes “Treat a single sentiment signal as complete quality.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.
- **D**: Online checks can measure properties without references; the chosen metric determines what is actually evidenced.

Revisit: 02_Intermediate/I19_Offline_Online_Evaluations. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-15: C — Datasets
- **A**: Incorrect: this proposes “Overwrite examples without recording changes.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.
- **B**: Incorrect: this proposes “Call an assistant configuration an evaluation dataset.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.
- **C**: Stable examples and references support repeatable comparisons and error analysis.
- **D**: Incorrect: this proposes “Use only the latest production response as every reference.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.

Revisit: 02_Intermediate/I17_LangSmith_Datasets. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-16: B — Experiments
- **A**: Incorrect: this proposes “Ignore per-example failures when means improve.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.
- **B**: Controlled experiment inputs are necessary to interpret version differences.
- **C**: Incorrect: this proposes “Attribute the difference entirely to the model.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.
- **D**: Incorrect: this proposes “Compare only the number of green badges.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-17: A — Evaluator alignment
- **A**: Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs.
- **B**: Incorrect: this proposes “Report agreement without the confusion matrix.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.
- **C**: Incorrect: this proposes “Replace undefined precision with 100%.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.
- **D**: Incorrect: this proposes “Remove disagreeing examples from every report.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.

Revisit: 02_Intermediate/I20_Evaluator_Alignment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-18: D — Dataset leakage
- **A**: Incorrect: this proposes “Report the tuned benchmark as unbiased generalization.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.
- **B**: Incorrect: this proposes “Put reference answers into every candidate prompt.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.
- **C**: Incorrect: this proposes “Delete hard examples to improve the score.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.
- **D**: Tuning on evaluation labels leaks information and overstates generalization.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-19: C — Boundary tests
- **A**: Incorrect: this proposes “Catch every error and return a fabricated valid result.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.
- **B**: Incorrect: this proposes “Disable failing assertions.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.
- **C**: Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states.
- **D**: Incorrect: this proposes “Assume default UI success covers failure behavior.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.

Revisit: 01_Beginner/B14_Calculator_Agent. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-20: B — Release gates
- **A**: Incorrect: this proposes “Call every passing local fixture a deployed service.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
- **B**: A metric validates only its defined property; retrieval relevance and answer correctness are separate.
- **C**: Incorrect: this proposes “Claim production answer correctness is certified.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
- **D**: Incorrect: this proposes “Treat citation presence as factual support.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.

Revisit: 05_Capstone_Projects/C05_Complete_Agent_Engineering_Platform. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-21: A — Graph export
- **A**: A graph declaration is a deployment input, not evidence that a remote deployment exists or works.
- **B**: Incorrect: this proposes “Claim the JSON manifest proves deployment.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.
- **C**: Incorrect: this proposes “Assume a local PID proves endpoint behavior.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.
- **D**: Incorrect: this proposes “Expose an unauthenticated tutorial server publicly.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.

Revisit: 03_Advanced/A08_Graph_Deployment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-22: D — Deployment revision
- **A**: Incorrect: this proposes “Use a conversation thread ID as the code revision.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.
- **B**: Incorrect: this proposes “Assume an assistant name identifies immutable code.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.
- **C**: Incorrect: this proposes “Overwrite revision history whenever configuration changes.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.
- **D**: Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy.

Revisit: 03_Advanced/A09_Revisions_And_Assistants. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-23: C — Assistants
- **A**: Incorrect: this proposes “Treat assistants as user authentication tokens.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.
- **B**: Incorrect: this proposes “Assume every assistant configuration is a new deployment.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.
- **C**: Assistants configure graph behavior; deployments, threads, and identities have different responsibilities.
- **D**: Incorrect: this proposes “Clone a conversation thread as a substitute for configuration.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.

Revisit: 03_Advanced/A09_Revisions_And_Assistants. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-24: B — Threads
- **A**: Incorrect: this proposes “Treat a run as a durable identity provider.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.
- **B**: Threads organize continuing state; runs represent executions within or against that state.
- **C**: Incorrect: this proposes “Create a new deployment for each message.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.
- **D**: Incorrect: this proposes “Use one thread across all tenants.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.

Revisit: 03_Advanced/A10_Threads_And_Runs. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-25: A — Runs
- **A**: Acceptance and execution completion are different states and need separate evidence.
- **B**: Incorrect: this proposes “Mark every accepted request as successful.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.
- **C**: Incorrect: this proposes “Treat a run ID alone as proof of completion.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.
- **D**: Incorrect: this proposes “Ignore errors after the client disconnects.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.

Revisit: 03_Advanced/A10_Threads_And_Runs. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-26: D — Authentication
- **A**: Incorrect: this proposes “Authorize it because the claimed role is editor.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.
- **B**: Incorrect: this proposes “Trust the tenant string from the request body.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.
- **C**: Incorrect: this proposes “Log the complete token to help debugging.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.
- **D**: Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims.

Revisit: 03_Advanced/A11_Authentication_Authorization. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-27: C — Authorization
- **A**: Incorrect: this proposes “Filter the output only after sending all documents to the model.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.
- **B**: Incorrect: this proposes “Treat a UI tenant selector as production authorization.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.
- **C**: Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure.
- **D**: Incorrect: this proposes “Allow it because authentication succeeded.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.

Revisit: 05_Capstone_Projects/C02_Enterprise_RAG_Agent. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-28: B — Secrets
- **A**: Incorrect: this proposes “Disable TLS verification to bypass access problems.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.
- **B**: Secrets belong in secure configuration; transport verification and least-privilege access remain necessary.
- **C**: Incorrect: this proposes “Commit it to app.py for convenience.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.
- **D**: Incorrect: this proposes “Put it in downloaded evidence.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.

Revisit: 03_Advanced/A12_Secrets_Management. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-29: A — Durability
- **A**: Durability guarantees depend on the storage and failure model; a local database is not multi-region replication.
- **B**: Incorrect: this proposes “Claim region-failure tolerance from local SQLite alone.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.
- **C**: Incorrect: this proposes “Treat an in-memory store as a backup.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.
- **D**: Incorrect: this proposes “Ignore concurrency when multiple writers update state.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.

Revisit: 03_Advanced/A13_Persistent_Storage. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-30: D — Regional failover
- **A**: Incorrect: this proposes “Assume health implies current data.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.
- **B**: Incorrect: this proposes “Claim a local routing simulation created cloud regions.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.
- **C**: Incorrect: this proposes “Silently report the stale replica as current.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.
- **D**: Health, revision freshness, and availability are separate inputs to failover policy.

Revisit: 03_Advanced/A14_Multi_Region_Deployment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-31: C — Trace structure
- **A**: Incorrect: this proposes “Discard parent IDs.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.
- **B**: Incorrect: this proposes “Treat the longest child as a universal critical-path algorithm.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.
- **C**: Nested and parallel work can overlap; tree structure and timing semantics matter.
- **D**: Incorrect: this proposes “Add all spans to estimate root wall-clock latency.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.

Revisit: 03_Advanced/A15_Trace_Analysis. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-32: B — Thread analysis
- **A**: Incorrect: this proposes “Assume all threads contain one execution.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.
- **B**: Conversation-level cost and reliability require aggregation across constituent runs.
- **C**: Incorrect: this proposes “Inspect one cheap run and conclude the whole conversation is cheap.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.
- **D**: Incorrect: this proposes “Compare thread and run counts as if they were identical.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.

Revisit: 03_Advanced/A16_Thread_Analysis. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-33: A — Latency percentiles
- **A**: Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles.
- **B**: Incorrect: this proposes “Use the fastest request as the p95.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.
- **C**: Incorrect: this proposes “Assume a mean reveals every tail regression.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.
- **D**: Incorrect: this proposes “Ignore the percentile definition.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.

Revisit: 03_Advanced/A17_Cost_Latency_Monitoring. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-34: D — Cost attribution
- **A**: Incorrect: this proposes “Call it a provider invoice.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.
- **B**: Incorrect: this proposes “Treat latency as a token count.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.
- **C**: Incorrect: this proposes “Assume all models have identical pricing.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.
- **D**: Cost evidence needs known token usage, pricing, and provenance before billing claims are justified.

Revisit: 03_Advanced/A17_Cost_Latency_Monitoring. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-35: C — User sentiment
- **A**: Incorrect: this proposes “Infer factual correctness solely from sentiment.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.
- **B**: Incorrect: this proposes “Discard negative ratings to improve the dashboard.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.
- **C**: Feedback can reveal problems while still being biased and incomplete.
- **D**: Incorrect: this proposes “Treat voluntary feedback as an unbiased population estimate.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.

Revisit: 03_Advanced/A18_Sentiment_And_Insights. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-36: B — Online evaluations and Insights
- **A**: Incorrect: this proposes “Assume both workflows are identical.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
- **B**: Per-run evaluation and exploratory aggregation answer related but different questions.
- **C**: Incorrect: this proposes “Treat a local topic counter as verified LangSmith Insights.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
- **D**: Incorrect: this proposes “Use one score as a complete explanation of every incident.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.

Revisit: 03_Advanced/A18_Sentiment_And_Insights. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-37: A — Alerts
- **A**: Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate.
- **B**: Incorrect: this proposes “Fire every alert on every request without a policy.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.
- **C**: Incorrect: this proposes “Assume no alert means no failure.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.
- **D**: Incorrect: this proposes “Ignore notification delivery status.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.

Revisit: 03_Advanced/A19_Production_Alerts. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-38: D — Deduplication
- **A**: Incorrect: this proposes “Send duplicate notifications indefinitely.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.
- **B**: Incorrect: this proposes “Claim a local ledger is a delivered webhook.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.
- **C**: Incorrect: this proposes “Delete all evidence after the first failure.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.
- **D**: Deduplication reduces noise but does not establish delivery or incident resolution.

Revisit: 03_Advanced/A19_Production_Alerts. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-39: C — Sampling
- **A**: Incorrect: this proposes “Silently exclude errors from every sample.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.
- **B**: Incorrect: this proposes “Present unrun evaluations as passed.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.
- **C**: Sampling reduces cost but creates coverage limits that must remain visible.
- **D**: Incorrect: this proposes “Treat the sample as exhaustive evidence.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.

Revisit: 02_Intermediate/I19_Offline_Online_Evaluations. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M3-40: B — Trace privacy
- **A**: Incorrect: this proposes “Use a random local operation ID as proof of a cloud trace.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.
- **B**: Privacy controls and delivery verification are separate; local IDs are not cloud evidence.
- **C**: Incorrect: this proposes “Assume local redaction proves cloud delivery.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.
- **D**: Incorrect: this proposes “Log API keys to correlate runs.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.

Revisit: 01_Beginner/B20_LangSmith_Tracing. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).
