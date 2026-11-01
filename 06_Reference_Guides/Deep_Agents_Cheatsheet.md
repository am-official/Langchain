# Deep Agents cheatsheet
`create_deep_agent` supplies planning and virtual filesystem tooling with optional subagents. I13 runs write_todos through the actual installed API. A01 writes and reads a virtual file; A02 delegates through the task tool to a named analyst.

The local scripted model emits predefined tool requests. It exercises the real framework but does not perform autonomous research. Live model behavior needs separate evaluation.

The default state-backed filesystem stores virtual artifacts in graph state. It is not the host filesystem and is not automatically durable without persistence. Selecting a host filesystem backend changes the trust boundary. Virtual file paths do not prove OS sandboxing.

Skills and AGENTS.md require the framework's supported loading mechanism. I14 explicitly loads and previews instruction files; it does not claim automatic Deep Agents discovery. Treat retrieved documents and user content as data rather than privileged instructions.

Do not expose execute-like tools for arbitrary generated code without a suitable verified isolation service. A04's arithmetic worker intentionally accepts a much narrower language and explicitly disclaims arbitrary-code isolation.
