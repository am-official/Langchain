# API compatibility and verification
The tested managed environment uses CPython 3.12.14. Direct package pins live in pyproject.toml and per-project requirements.txt; requirements.lock.txt at the root records the complete tested environment. Use that lock for the full curriculum; standalone folders use their own requirements.

Verified through execution: create_agent, agent before_model/wrap_model_call/dynamic_prompt middleware, ModelRequest.override, LangGraph StateGraph/conditional edges/interrupt/Command/RetryPolicy, SQLite checkpointing, Deep Agents planning/files/subagents, LangChain MCP adapter with a real local server, text splitters, document/vector-store contracts, and Streamlit forms. LangSmith client/evaluator call shapes have injected-boundary tests; live cloud account behavior remains unverified.

The MCP project pins AnyIO 4.12.1. It was investigated during stdio diagnosis; the successful integration also required an unrestricted local subprocess execution boundary, so the timeout should not be attributed solely to a package version.

Official documentation hosts were blocked by network policy. These tests verify the installed APIs and documented local behavior; they do not independently verify the latest official exam syllabus. Legacy LLMChain and initialize_agent patterns are not used.

Live OpenAI model IDs default to gpt-4.1-mini; I04 has configurable SMALL_MODEL/LARGE_MODEL. Account/model access and future model availability must be tested by the learner. Semantic embeddings use text-embedding-3-small only in B17 live mode. Retrieval lessons intentionally use local lexical hashing and state its limitations.
