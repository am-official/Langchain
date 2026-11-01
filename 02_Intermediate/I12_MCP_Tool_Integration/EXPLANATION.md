# How A tool over MCP works

Start an allowlisted local MCP server, discover its tools, and call one through the LangChain adapter.

## Why LangChain
LangChain supplies composable messages, prompts, model adapters, documents, or retrieval contracts. Pure local processing may be simpler without it; the lesson isolates the named engineering concept before introducing external services.

## Imports
`Path` resolves local configuration; `os` reads variable names; `json` encodes evidence; `time` measures local duration; `streamlit` renders the interface; `load_dotenv` loads optional configuration without replacing injected values. `ChatPromptTemplate` structures messages; `StrOutputParser` extracts text; `RunnableLambda` wraps Python functions; message classes represent chat roles; `ChatOpenAI` is used only by offered live paths. Additional concept-specific imports appear in the source below.

## Data flow
```mermaid
flowchart LR
  Input[Form input] --> Validate[Validate and normalize]
  Validate --> Experiment[Lesson pipeline]
  Experiment --> Evidence[Structured evidence]
  Evidence --> Result[Result canvas and download]
```

## Concept-specific implementation, annotated by source
Read this complete runnable core alongside app.py. Validation precedes processing; the returned dictionary defines what the UI displays.

```python
import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

async def inspect_mcp(text):
    server=StdioServerParameters(command=sys.executable,args=[str(Path(__file__).with_name('server.py'))])
    async with asyncio.timeout(15):
        async with stdio_client(server) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize()
                tools=await load_mcp_tools(session)
                selected=next(t for t in tools if t.name=='count_words')
                result=await selected.ainvoke({'text':text})
                # Adapter returns a list of content blocks; retain protocol evidence.
                return {'tools':[t.name for t in tools],'result':result,'expected_words':len(text.split()),'transport':'local stdio; fixed server command'}

def run(data,live=False,model=None):
    return asyncio.run(inspect_mcp(require_text(data['text'],2000)))
```

## Important lines
- `return {'tools':[t.name for t in tools],'result':result,'expected_words':len(text.split()),'transport':'local stdio; fixed server command'}` — returns the observable result consumed by tests and the evidence canvas.
- `def run(data,live=False,model=None):` — defines a callable stage and its input contract.
- `return asyncio.run(inspect_mcp(require_text(data['text'],2000)))` — returns the observable result consumed by tests and the evidence canvas.

## Interface and reliability
The form submits related inputs together. Session state retains the last result; reset clears it. A spinner provides loading feedback. Input errors are shown in context; unknown provider errors are sanitized. Static HTML styles contain no user text. Every output carries explicit local/live labeling. The timer is not a provider latency benchmark. Local tests do not establish live provider correctness, visual browser quality, or production deployment.
