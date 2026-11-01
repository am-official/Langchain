# Agent Atelier · LangChain Agent Engineer Mastery

A hands-on learning repository with **65 self-contained Streamlit applications**: 20 beginner lessons, 20 intermediate lessons, 20 advanced engineering demonstrations, and five capstones. Each studio includes source, dependencies, environment examples, sample inputs, tests, instructions, explanations, exercises, and practice questions.

The interfaces use a consistent midnight, violet, and mint design with responsive layouts, labeled inputs, progress feedback, actionable errors, and downloadable results.

**Verification scope:** local application behavior is tested. Optional paid-service paths and real cloud deployments are not live-verified. Several advanced projects intentionally simulate cloud concepts and say so explicitly. Official syllabus access was blocked by network policy, so the certification topic map is provisional and no exam score or complete official coverage is guaranteed.

## Open the learning portal

From the repository root, install the complete tested environment:

Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
.venv\Scripts\python.exe -m streamlit run portal.py
```

macOS/Linux:
```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock.txt
.venv/bin/python -m streamlit run portal.py
```

The portal provides searchable studios and three original 40-question mock exams with domain scores, explanations, weak-topic feedback, and downloadable scoring evidence. The mocks follow the supplied four-domain weighting of 25% each; this weighting has not been independently verified against the current official guide.

## Run a project independently

Copy or open any project folder. It does not import source from another project.

```sh
cd 01_Beginner/B14_Calculator_Agent
python -m venv .venv
# Windows: .venv\Scripts\python.exe -m pip install -r requirements.txt
# Windows: .venv\Scripts\python.exe -m streamlit run app.py
# macOS/Linux:
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

Local mode needs no API credentials. Configure only the optional services you use by copying the project's `.env.example` to `.env` and replacing placeholders. Never commit `.env`. Existing process variables take precedence. Live OpenAI requests may incur charges; LangSmith cloud operations require your own account and permissions.

## Validate

```sh
python scripts/validate_repository.py
python -m pytest tests 01_Beginner 02_Intermediate 03_Advanced 05_Capstone_Projects -q
python -m pip check
```

In this managed environment, use `.venv/bin/python` for Python commands and `UV_CACHE_DIR=/workspace/.cache/uv uv pip check --python .venv/bin/python` for the dependency check. Its uv-created environment has no pip module. The real MCP integration requires unrestricted local child-process stdio; it timed out in the restricted command sandbox and passed outside that boundary.

See [validation evidence](docs/VALIDATION.md), [progress and limitations](docs/PROGRESS.md), and the machine-readable [project inventory](docs/PROJECT_STATUS.json).

## Learning path

| Stage | Projects | Main skills |
|---|---:|---|
| [Beginner](01_Beginner) | B01–B20 | Prompts, chat, schemas, streaming, tools, documents, vectors, RAG, tracing |
| [Intermediate](02_Intermediate) | I01–I20 | Agents, middleware, context, memory, graph routing, approvals, MCP, Deep Agents, evaluation |
| [Advanced](03_Advanced) | A01–A20 | Delegation, checkpoints, execution boundaries, retries, deployment concepts, authorization, durability, monitoring |
| [Capstones](05_Capstone_Projects) | C01–C05 | Research, tenant-scoped RAG, parallel teams, reviewed support, lifecycle dashboard |
| [Certification preparation](04_Certification_Preparation) | 120 original mock questions | Four-domain practice, explanations, scoring, practical assessment |
| [Reference guides](06_Reference_Guides) | 8 guides | Cheatsheets, glossary, troubleshooting, compatibility, study plan |

Follow each project's `INSTRUCTIONS.md` before extending it. Compare deterministic fixtures with optional live execution; never mistake local success for cloud verification. The advanced arithmetic worker is a restricted interpreter demonstration, not a general sandbox for arbitrary generated code.

## Certification preparation

- [Official source status](04_Certification_Preparation/Official_Exam_Objectives/SOURCE_STATUS.md)
- [Provisional topic-to-project matrix](04_Certification_Preparation/Objective_To_Project_Mapping/COVERAGE.md)
- [Original mock 1](04_Certification_Preparation/Mock_Exam_01/README.md), [mock 2](04_Certification_Preparation/Mock_Exam_02/README.md), [mock 3](04_Certification_Preparation/Mock_Exam_03/README.md)
- [Answer explanations](04_Certification_Preparation/Answer_Explanations)
- [LangSmith practical assessment](04_Certification_Preparation/LangSmith_UI_Practice/ASSESSMENT.md)
- [Readiness checklist](04_Certification_Preparation/Readiness_Checklist/README.md)
- [Eight-week study plan](06_Reference_Guides/Certification_Study_Plan.md)

A repeated 90% practice score is a study target, not a certification guarantee. Obtain the latest official study guide before relying on the provisional map.

## Project index
- [B01 Hello LangChain](01_Beginner/B01_Hello_LangChain/README.md)
- [B02 Simple AI Chatbot](01_Beginner/B02_Simple_AI_Chatbot/README.md)
- [B03 Prompt Templates](01_Beginner/B03_Prompt_Templates/README.md)
- [B04 Language Translator](01_Beginner/B04_Language_Translator/README.md)
- [B05 Text Summarizer](01_Beginner/B05_Text_Summarizer/README.md)
- [B06 Sentiment Analyzer](01_Beginner/B06_Sentiment_Analyzer/README.md)
- [B07 Quiz Generator](01_Beginner/B07_Quiz_Generator/README.md)
- [B08 Structured Output](01_Beginner/B08_Structured_Output/README.md)
- [B09 LCEL Chains](01_Beginner/B09_LCEL_Chains/README.md)
- [B10 Output Parsers](01_Beginner/B10_Output_Parsers/README.md)
- [B11 Streaming Chatbot](01_Beginner/B11_Streaming_Chatbot/README.md)
- [B12 Conversation History](01_Beginner/B12_Conversation_History/README.md)
- [B13 Tool Calling](01_Beginner/B13_Tool_Calling/README.md)
- [B14 Calculator Agent](01_Beginner/B14_Calculator_Agent/README.md)
- [B15 Document Loader](01_Beginner/B15_Document_Loader/README.md)
- [B16 Text Splitting](01_Beginner/B16_Text_Splitting/README.md)
- [B17 Embeddings](01_Beginner/B17_Embeddings/README.md)
- [B18 Vector Search](01_Beginner/B18_Vector_Search/README.md)
- [B19 Simple RAG](01_Beginner/B19_Simple_RAG/README.md)
- [B20 LangSmith Tracing](01_Beginner/B20_LangSmith_Tracing/README.md)
- [I01 Create Agent](02_Intermediate/I01_Create_Agent/README.md)
- [I02 Multiple Tools](02_Intermediate/I02_Multiple_Tools/README.md)
- [I03 Agent Middleware](02_Intermediate/I03_Agent_Middleware/README.md)
- [I04 Dynamic Model Selection](02_Intermediate/I04_Dynamic_Model_Selection/README.md)
- [I05 Context Engineering](02_Intermediate/I05_Context_Engineering/README.md)
- [I06 Persistent Memory](02_Intermediate/I06_Persistent_Memory/README.md)
- [I07 LangGraph State](02_Intermediate/I07_LangGraph_State/README.md)
- [I08 Conditional Routing](02_Intermediate/I08_Conditional_Routing/README.md)
- [I09 Human In The Loop](02_Intermediate/I09_Human_In_The_Loop/README.md)
- [I10 PDF RAG Assistant](02_Intermediate/I10_PDF_RAG_Assistant/README.md)
- [I11 Advanced Retrieval](02_Intermediate/I11_Advanced_Retrieval/README.md)
- [I12 MCP Tool Integration](02_Intermediate/I12_MCP_Tool_Integration/README.md)
- [I13 Deep Agents Basics](02_Intermediate/I13_Deep_Agents_Basics/README.md)
- [I14 AGENTS And SKILL Files](02_Intermediate/I14_AGENTS_And_SKILL_Files/README.md)
- [I15 Code Based Evaluators](02_Intermediate/I15_Code_Based_Evaluators/README.md)
- [I16 LLM As Judge](02_Intermediate/I16_LLM_As_Judge/README.md)
- [I17 LangSmith Datasets](02_Intermediate/I17_LangSmith_Datasets/README.md)
- [I18 LangSmith Experiments](02_Intermediate/I18_LangSmith_Experiments/README.md)
- [I19 Offline Online Evaluations](02_Intermediate/I19_Offline_Online_Evaluations/README.md)
- [I20 Evaluator Alignment](02_Intermediate/I20_Evaluator_Alignment/README.md)
- [A01 Deep Agents Workflows](03_Advanced/A01_Deep_Agents_Workflows/README.md)
- [A02 Subagents And Delegation](03_Advanced/A02_Subagents_And_Delegation/README.md)
- [A03 Long Running Agents](03_Advanced/A03_Long_Running_Agents/README.md)
- [A04 Sandboxed Execution](03_Advanced/A04_Sandboxed_Execution/README.md)
- [A05 Production Context Management](03_Advanced/A05_Production_Context_Management/README.md)
- [A06 Multi Agent Orchestration](03_Advanced/A06_Multi_Agent_Orchestration/README.md)
- [A07 Fault Tolerant Agents](03_Advanced/A07_Fault_Tolerant_Agents/README.md)
- [A08 Graph Deployment](03_Advanced/A08_Graph_Deployment/README.md)
- [A09 Revisions And Assistants](03_Advanced/A09_Revisions_And_Assistants/README.md)
- [A10 Threads And Runs](03_Advanced/A10_Threads_And_Runs/README.md)
- [A11 Authentication Authorization](03_Advanced/A11_Authentication_Authorization/README.md)
- [A12 Secrets Management](03_Advanced/A12_Secrets_Management/README.md)
- [A13 Persistent Storage](03_Advanced/A13_Persistent_Storage/README.md)
- [A14 Multi Region Deployment](03_Advanced/A14_Multi_Region_Deployment/README.md)
- [A15 Trace Analysis](03_Advanced/A15_Trace_Analysis/README.md)
- [A16 Thread Analysis](03_Advanced/A16_Thread_Analysis/README.md)
- [A17 Cost Latency Monitoring](03_Advanced/A17_Cost_Latency_Monitoring/README.md)
- [A18 Sentiment And Insights](03_Advanced/A18_Sentiment_And_Insights/README.md)
- [A19 Production Alerts](03_Advanced/A19_Production_Alerts/README.md)
- [A20 End To End Agent Lifecycle](03_Advanced/A20_End_To_End_Agent_Lifecycle/README.md)
- [C01 Research Assistant](05_Capstone_Projects/C01_Research_Assistant/README.md)
- [C02 Enterprise RAG Agent](05_Capstone_Projects/C02_Enterprise_RAG_Agent/README.md)
- [C03 Multi Agent Research System](05_Capstone_Projects/C03_Multi_Agent_Research_System/README.md)
- [C04 Production Customer Support](05_Capstone_Projects/C04_Production_Customer_Support/README.md)
- [C05 Complete Agent Engineering Platform](05_Capstone_Projects/C05_Complete_Agent_Engineering_Platform/README.md)
