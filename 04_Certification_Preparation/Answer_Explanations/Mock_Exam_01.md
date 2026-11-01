# Mock Exam 01 — explanations

## M1-01: C — Agent selection
- **A**: Incorrect: this proposes “Use a parser as the agent control loop.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.
- **B**: Incorrect: this proposes “Execute arbitrary Python from the prompt.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.
- **C**: create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed.
- **D**: Incorrect: this proposes “Always use Deep Agents for every prompt.” create_agent provides the basic agent loop; Deep Agents adds planning, files, and delegation when those capabilities are needed. The supported action is: Start with create_agent and a small allowlisted toolset.

Revisit: 02_Intermediate/I01_Create_Agent. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-02: B — Deep Agents
- **A**: Incorrect: this proposes “Disable all tool schemas.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.
- **B**: Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code.
- **C**: Incorrect: this proposes “Assume a virtual file is a durable host file.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.
- **D**: Incorrect: this proposes “Claim a tool name alone supplies OS isolation.” Planning and virtual files are distinct from durable host storage and from a sandbox for arbitrary code. The supported action is: Use Deep Agents planning and a state-backed filesystem.

Revisit: 03_Advanced/A01_Deep_Agents_Workflows. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-03: A — Middleware
- **A**: Enforcement belongs at the execution boundary, before the call or side effect it protects.
- **B**: Incorrect: this proposes “Reject it only after executing its tool.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.
- **C**: Incorrect: this proposes “Put the API key in the rejection message.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.
- **D**: Incorrect: this proposes “Trust a friendly UI warning as enforcement.” Enforcement belongs at the execution boundary, before the call or side effect it protects. The supported action is: Validate it in a before-model guard.

Revisit: 02_Intermediate/I03_Agent_Middleware. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-04: D — Context engineering
- **A**: Incorrect: this proposes “Promote the user message to system instructions.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.
- **B**: Incorrect: this proposes “Append the entire database to the prompt.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.
- **C**: Incorrect: this proposes “Treat a token budget as authorization.” Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns. The supported action is: Keep trusted runtime policy separate from untrusted user content.
- **D**: Trusted policy and user content need separate provenance; prompt size and data authorization are different concerns.

Revisit: 02_Intermediate/I05_Context_Engineering. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-05: C — Instruction files
- **A**: Incorrect: this proposes “Treat uploaded document instructions as developer policy.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.
- **B**: Incorrect: this proposes “Run a shell command mentioned in untrusted text.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.
- **C**: Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism.
- **D**: Incorrect: this proposes “Assume every SDK automatically discovers every file.” Instruction discovery is framework-specific; files and skill metadata must be loaded through the intended mechanism. The supported action is: Load repository guidance and explicitly select the relevant skill.

Revisit: 02_Intermediate/I14_AGENTS_And_SKILL_Files. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-06: B — Restricted execution
- **A**: Incorrect: this proposes “Describe resource limits as a complete OS sandbox.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.
- **B**: Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python.
- **C**: Incorrect: this proposes “Use eval because a timeout makes it safe.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.
- **D**: Incorrect: this proposes “Call shell=True with the generated text.” Allowlisted arithmetic and resource limits are useful boundaries but do not provide isolation for arbitrary Python. The supported action is: Reject it; the lesson accepts only an arithmetic AST allowlist.

Revisit: 03_Advanced/A04_Sandboxed_Execution. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-07: A — Tool protocol
- **A**: Tool-call IDs tie results to requests; tool allowlists and argument validation still apply.
- **B**: Incorrect: this proposes “Match by display position only.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.
- **C**: Incorrect: this proposes “Discard the call IDs.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.
- **D**: Incorrect: this proposes “Trust tool names to authorize arbitrary arguments.” Tool-call IDs tie results to requests; tool allowlists and argument validation still apply. The supported action is: Correlate each result with its tool_call_id.

Revisit: 01_Beginner/B13_Tool_Calling. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-08: D — Structured output
- **A**: Incorrect: this proposes “Silently convert every malformed response to success.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.
- **B**: Incorrect: this proposes “Treat JSON syntax as complete schema validation.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.
- **C**: Incorrect: this proposes “Store the provider key in the contact record.” Valid JSON can still violate types, bounds, and allowed fields. The supported action is: Reject it using the explicit validation schema.
- **D**: Valid JSON can still violate types, bounds, and allowed fields.

Revisit: 01_Beginner/B08_Structured_Output. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-09: C — Memory
- **A**: Incorrect: this proposes “Use one global preference key for all tenants.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.
- **B**: Incorrect: this proposes “Call a larger context window a database.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.
- **C**: Prompt context, browser state, and durable long-term storage have different lifetimes.
- **D**: Incorrect: this proposes “Rely on session state as disk durability.” Prompt context, browser state, and durable long-term storage have different lifetimes. The supported action is: Persist preferences in durable storage with a user namespace.

Revisit: 02_Intermediate/I06_Persistent_Memory. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-10: B — Retrieval grounding
- **A**: Incorrect: this proposes “Claim lexical hashing understands semantic synonyms.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.
- **B**: Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims.
- **C**: Incorrect: this proposes “Invent a citation to make the answer look complete.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.
- **D**: Incorrect: this proposes “Treat similarity score as proof of truth.” Retrieval can fail; a transparent no-evidence path is preferable to unsupported claims. The supported action is: Abstain or request more evidence.

Revisit: 01_Beginner/B19_Simple_RAG. Reference target: https://docs.langchain.com/oss/python/langchain/ (current verification blocked).

## M1-11: A — Code evaluators
- **A**: Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge.
- **B**: Incorrect: this proposes “Require an LLM judge for every equality check.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.
- **C**: Incorrect: this proposes “Use latency as the correctness label.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.
- **D**: Incorrect: this proposes “Assume a passing formatter proves the answer.” Deterministic properties should be measured directly rather than delegated unnecessarily to a probabilistic judge. The supported action is: Use a deterministic code-based evaluator.

Revisit: 02_Intermediate/I15_Code_Based_Evaluators. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-12: D — LLM judges
- **A**: Incorrect: this proposes “Treat raw token overlap as semantic certainty.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.
- **B**: Incorrect: this proposes “Let candidate text rewrite the rubric.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.
- **C**: Incorrect: this proposes “Omit human alignment checks.” A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration. The supported action is: Use a rubric-based judge and validate its structured output.
- **D**: A judge can assess semantic criteria but requires a rubric, input boundaries, and calibration.

Revisit: 02_Intermediate/I16_LLM_As_Judge. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-13: C — Offline evaluation
- **A**: Incorrect: this proposes “Tune on every held-out label and report unbiased performance.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.
- **B**: Incorrect: this proposes “Use only one successful default example.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.
- **C**: Offline describes the evaluation workflow on a dataset, not whether networking exists.
- **D**: Incorrect: this proposes “Call it online evaluation because a server is used.” Offline describes the evaluation workflow on a dataset, not whether networking exists. The supported action is: Run a repeatable offline evaluation on a held-out dataset.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-14: B — Online evaluation
- **A**: Incorrect: this proposes “Treat a single sentiment signal as complete quality.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.
- **B**: Online checks can measure properties without references; the chosen metric determines what is actually evidenced.
- **C**: Incorrect: this proposes “Report exact-match accuracy without a reference.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.
- **D**: Incorrect: this proposes “Assume low latency means factual correctness.” Online checks can measure properties without references; the chosen metric determines what is actually evidenced. The supported action is: Apply suitable reference-free evaluators and record their limitations.

Revisit: 02_Intermediate/I19_Offline_Online_Evaluations. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-15: A — Datasets
- **A**: Stable examples and references support repeatable comparisons and error analysis.
- **B**: Incorrect: this proposes “Use only the latest production response as every reference.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.
- **C**: Incorrect: this proposes “Overwrite examples without recording changes.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.
- **D**: Incorrect: this proposes “Call an assistant configuration an evaluation dataset.” Stable examples and references support repeatable comparisons and error analysis. The supported action is: Add reference outputs and stable example identifiers where the evaluator needs them.

Revisit: 02_Intermediate/I17_LangSmith_Datasets. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-16: D — Experiments
- **A**: Incorrect: this proposes “Attribute the difference entirely to the model.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.
- **B**: Incorrect: this proposes “Compare only the number of green badges.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.
- **C**: Incorrect: this proposes “Ignore per-example failures when means improve.” Controlled experiment inputs are necessary to interpret version differences. The supported action is: Compare both candidates on the same versioned examples and evaluator settings.
- **D**: Controlled experiment inputs are necessary to interpret version differences.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-17: C — Evaluator alignment
- **A**: Incorrect: this proposes “Replace undefined precision with 100%.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.
- **B**: Incorrect: this proposes “Remove disagreeing examples from every report.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.
- **C**: Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs.
- **D**: Incorrect: this proposes “Report agreement without the confusion matrix.” Agreement alone can hide systematic acceptance errors; false positives and false negatives have distinct operational costs. The supported action is: Inspect false positives and revise or calibrate the rubric using labeled review data.

Revisit: 02_Intermediate/I20_Evaluator_Alignment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-18: B — Dataset leakage
- **A**: Incorrect: this proposes “Delete hard examples to improve the score.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.
- **B**: Tuning on evaluation labels leaks information and overstates generalization.
- **C**: Incorrect: this proposes “Report the tuned benchmark as unbiased generalization.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.
- **D**: Incorrect: this proposes “Put reference answers into every candidate prompt.” Tuning on evaluation labels leaks information and overstates generalization. The supported action is: Reserve a separate held-out set for the final assessment.

Revisit: 02_Intermediate/I18_LangSmith_Experiments. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-19: A — Boundary tests
- **A**: Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states.
- **B**: Incorrect: this proposes “Assume default UI success covers failure behavior.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.
- **C**: Incorrect: this proposes “Catch every error and return a fabricated valid result.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.
- **D**: Incorrect: this proposes “Disable failing assertions.” Failure-path tests establish validation behavior and can reveal unsafe execution or stale UI states. The supported action is: Add malformed, empty, oversized, and unsupported-input cases.

Revisit: 01_Beginner/B14_Calculator_Agent. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-20: D — Release gates
- **A**: Incorrect: this proposes “Claim production answer correctness is certified.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
- **B**: Incorrect: this proposes “Treat citation presence as factual support.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
- **C**: Incorrect: this proposes “Call every passing local fixture a deployed service.” A metric validates only its defined property; retrieval relevance and answer correctness are separate. The supported action is: Describe the gate as evidence quality only and add answer-quality checks before claiming broader readiness.
- **D**: A metric validates only its defined property; retrieval relevance and answer correctness are separate.

Revisit: 05_Capstone_Projects/C05_Complete_Agent_Engineering_Platform. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-21: C — Graph export
- **A**: Incorrect: this proposes “Assume a local PID proves endpoint behavior.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.
- **B**: Incorrect: this proposes “Expose an unauthenticated tutorial server publicly.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.
- **C**: A graph declaration is a deployment input, not evidence that a remote deployment exists or works.
- **D**: Incorrect: this proposes “Claim the JSON manifest proves deployment.” A graph declaration is a deployment input, not evidence that a remote deployment exists or works. The supported action is: Validate imports and invocation, then separately deploy and verify the managed service.

Revisit: 03_Advanced/A08_Graph_Deployment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-22: B — Deployment revision
- **A**: Incorrect: this proposes “Overwrite revision history whenever configuration changes.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.
- **B**: Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy.
- **C**: Incorrect: this proposes “Use a conversation thread ID as the code revision.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.
- **D**: Incorrect: this proposes “Assume an assistant name identifies immutable code.” Managed revisions version deployed code/configuration; local content hashes in the lesson are a limited versioning analogy. The supported action is: Track the deployment revision and verify the active version.

Revisit: 03_Advanced/A09_Revisions_And_Assistants. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-23: A — Assistants
- **A**: Assistants configure graph behavior; deployments, threads, and identities have different responsibilities.
- **B**: Incorrect: this proposes “Clone a conversation thread as a substitute for configuration.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.
- **C**: Incorrect: this proposes “Treat assistants as user authentication tokens.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.
- **D**: Incorrect: this proposes “Assume every assistant configuration is a new deployment.” Assistants configure graph behavior; deployments, threads, and identities have different responsibilities. The supported action is: Use distinct assistant configurations for that graph where supported.

Revisit: 03_Advanced/A09_Revisions_And_Assistants. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-24: D — Threads
- **A**: Incorrect: this proposes “Create a new deployment for each message.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.
- **B**: Incorrect: this proposes “Use one thread across all tenants.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.
- **C**: Incorrect: this proposes “Treat a run as a durable identity provider.” Threads organize continuing state; runs represent executions within or against that state. The supported action is: Keep a thread for conversation state and record each execution as a run.
- **D**: Threads organize continuing state; runs represent executions within or against that state.

Revisit: 03_Advanced/A10_Threads_And_Runs. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-25: C — Runs
- **A**: Incorrect: this proposes “Treat a run ID alone as proof of completion.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.
- **B**: Incorrect: this proposes “Ignore errors after the client disconnects.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.
- **C**: Acceptance and execution completion are different states and need separate evidence.
- **D**: Incorrect: this proposes “Mark every accepted request as successful.” Acceptance and execution completion are different states and need separate evidence. The supported action is: Track execution status and verify the final output or failure.

Revisit: 03_Advanced/A10_Threads_And_Runs. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-26: B — Authentication
- **A**: Incorrect: this proposes “Log the complete token to help debugging.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.
- **B**: Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims.
- **C**: Incorrect: this proposes “Authorize it because the claimed role is editor.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.
- **D**: Incorrect: this proposes “Trust the tenant string from the request body.” Authentication verifies the asserted identity; authorization cannot safely rely on unverified claims. The supported action is: Reject the identity before evaluating resource permissions.

Revisit: 03_Advanced/A11_Authentication_Authorization. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-27: A — Authorization
- **A**: Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure.
- **B**: Incorrect: this proposes “Allow it because authentication succeeded.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.
- **C**: Incorrect: this proposes “Filter the output only after sending all documents to the model.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.
- **D**: Incorrect: this proposes “Treat a UI tenant selector as production authorization.” Authenticated identity does not imply access to every tenant; filter authorized data before retrieval and model exposure. The supported action is: Deny the cross-tenant request.

Revisit: 05_Capstone_Projects/C02_Enterprise_RAG_Agent. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-28: D — Secrets
- **A**: Incorrect: this proposes “Commit it to app.py for convenience.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.
- **B**: Incorrect: this proposes “Put it in downloaded evidence.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.
- **C**: Incorrect: this proposes “Disable TLS verification to bypass access problems.” Secrets belong in secure configuration; transport verification and least-privilege access remain necessary. The supported action is: Load it from secure runtime configuration and avoid exposing its value.
- **D**: Secrets belong in secure configuration; transport verification and least-privilege access remain necessary.

Revisit: 03_Advanced/A12_Secrets_Management. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-29: C — Durability
- **A**: Incorrect: this proposes “Treat an in-memory store as a backup.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.
- **B**: Incorrect: this proposes “Ignore concurrency when multiple writers update state.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.
- **C**: Durability guarantees depend on the storage and failure model; a local database is not multi-region replication.
- **D**: Incorrect: this proposes “Claim region-failure tolerance from local SQLite alone.” Durability guarantees depend on the storage and failure model; a local database is not multi-region replication. The supported action is: Describe that as process-level durability and plan backups/replication for disk or region loss.

Revisit: 03_Advanced/A13_Persistent_Storage. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-30: B — Regional failover
- **A**: Incorrect: this proposes “Silently report the stale replica as current.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.
- **B**: Health, revision freshness, and availability are separate inputs to failover policy.
- **C**: Incorrect: this proposes “Assume health implies current data.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.
- **D**: Incorrect: this proposes “Claim a local routing simulation created cloud regions.” Health, revision freshness, and availability are separate inputs to failover policy. The supported action is: Apply the chosen consistency policy; this lesson refuses stale failover.

Revisit: 03_Advanced/A14_Multi_Region_Deployment. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-31: A — Trace structure
- **A**: Nested and parallel work can overlap; tree structure and timing semantics matter.
- **B**: Incorrect: this proposes “Add all spans to estimate root wall-clock latency.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.
- **C**: Incorrect: this proposes “Discard parent IDs.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.
- **D**: Incorrect: this proposes “Treat the longest child as a universal critical-path algorithm.” Nested and parallel work can overlap; tree structure and timing semantics matter. The supported action is: Use root wall-clock duration and inspect nested spans without summing overlapping durations.

Revisit: 03_Advanced/A15_Trace_Analysis. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-32: D — Thread analysis
- **A**: Incorrect: this proposes “Inspect one cheap run and conclude the whole conversation is cheap.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.
- **B**: Incorrect: this proposes “Compare thread and run counts as if they were identical.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.
- **C**: Incorrect: this proposes “Assume all threads contain one execution.” Conversation-level cost and reliability require aggregation across constituent runs. The supported action is: Aggregate run cost and error patterns across the thread.
- **D**: Conversation-level cost and reliability require aggregation across constituent runs.

Revisit: 03_Advanced/A16_Thread_Analysis. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-33: C — Latency percentiles
- **A**: Incorrect: this proposes “Assume a mean reveals every tail regression.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.
- **B**: Incorrect: this proposes “Ignore the percentile definition.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.
- **C**: Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles.
- **D**: Incorrect: this proposes “Use the fastest request as the p95.” Tail latency depends on the sample and method; the lesson uses nearest-rank percentiles. The supported action is: Inspect a defined percentile method and the observation count.

Revisit: 03_Advanced/A17_Cost_Latency_Monitoring. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-34: B — Cost attribution
- **A**: Incorrect: this proposes “Assume all models have identical pricing.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.
- **B**: Cost evidence needs known token usage, pricing, and provenance before billing claims are justified.
- **C**: Incorrect: this proposes “Call it a provider invoice.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.
- **D**: Incorrect: this proposes “Treat latency as a token count.” Cost evidence needs known token usage, pricing, and provenance before billing claims are justified. The supported action is: Label the sum as observed input cost, not independently verified billing.

Revisit: 03_Advanced/A17_Cost_Latency_Monitoring. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-35: A — User sentiment
- **A**: Feedback can reveal problems while still being biased and incomplete.
- **B**: Incorrect: this proposes “Treat voluntary feedback as an unbiased population estimate.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.
- **C**: Incorrect: this proposes “Infer factual correctness solely from sentiment.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.
- **D**: Incorrect: this proposes “Discard negative ratings to improve the dashboard.” Feedback can reveal problems while still being biased and incomplete. The supported action is: Track sentiment with its sample-selection limits.

Revisit: 03_Advanced/A18_Sentiment_And_Insights. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-36: D — Online evaluations and Insights
- **A**: Incorrect: this proposes “Treat a local topic counter as verified LangSmith Insights.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
- **B**: Incorrect: this proposes “Use one score as a complete explanation of every incident.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
- **C**: Incorrect: this proposes “Assume both workflows are identical.” Per-run evaluation and exploratory aggregation answer related but different questions. The supported action is: Use online evaluators for selected-run scores and Insights-style analysis for aggregate patterns.
- **D**: Per-run evaluation and exploratory aggregation answer related but different questions.

Revisit: 03_Advanced/A18_Sentiment_And_Insights. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-37: C — Alerts
- **A**: Incorrect: this proposes “Assume no alert means no failure.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.
- **B**: Incorrect: this proposes “Ignore notification delivery status.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.
- **C**: Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate.
- **D**: Incorrect: this proposes “Fire every alert on every request without a policy.” Window size and thresholds shape alert reliability; trigger evaluation and delivery are separate. The supported action is: Apply a defined minimum sample count and threshold before notifying.

Revisit: 03_Advanced/A19_Production_Alerts. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-38: B — Deduplication
- **A**: Incorrect: this proposes “Delete all evidence after the first failure.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.
- **B**: Deduplication reduces noise but does not establish delivery or incident resolution.
- **C**: Incorrect: this proposes “Send duplicate notifications indefinitely.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.
- **D**: Incorrect: this proposes “Claim a local ledger is a delivered webhook.” Deduplication reduces noise but does not establish delivery or incident resolution. The supported action is: Deduplicate the alert identity and separately track delivery.

Revisit: 03_Advanced/A19_Production_Alerts. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-39: A — Sampling
- **A**: Sampling reduces cost but creates coverage limits that must remain visible.
- **B**: Incorrect: this proposes “Treat the sample as exhaustive evidence.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.
- **C**: Incorrect: this proposes “Silently exclude errors from every sample.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.
- **D**: Incorrect: this proposes “Present unrun evaluations as passed.” Sampling reduces cost but creates coverage limits that must remain visible. The supported action is: Report coverage and avoid claiming every run was evaluated.

Revisit: 02_Intermediate/I19_Offline_Online_Evaluations. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).

## M1-40: D — Trace privacy
- **A**: Incorrect: this proposes “Assume local redaction proves cloud delivery.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.
- **B**: Incorrect: this proposes “Log API keys to correlate runs.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.
- **C**: Incorrect: this proposes “Use a random local operation ID as proof of a cloud trace.” Privacy controls and delivery verification are separate; local IDs are not cloud evidence. The supported action is: Redact sensitive trace inputs/outputs and verify actual exported records.
- **D**: Privacy controls and delivery verification are separate; local IDs are not cloud evidence.

Revisit: 01_Beginner/B20_LangSmith_Tracing. Reference target: https://docs.langchain.com/langsmith/ (current verification blocked).
