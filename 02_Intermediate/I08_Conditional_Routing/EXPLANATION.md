# How Choose the next node works

Route support messages through conditional graph edges and expose which branch ran.

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
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message:str
    route:str
    answer:str

def build_graph():
    graph=StateGraph(State)
    graph.add_node('classify',lambda s:{'route':'billing' if any(w in s['message'].lower() for w in ('refund','invoice','payment')) else 'technical'})
    graph.add_node('billing',lambda s:{'answer':'Billing queue: verify the order before any financial action.'})
    graph.add_node('technical',lambda s:{'answer':'Technical queue: collect reproduction steps.'})
    graph.add_edge(START,'classify');graph.add_conditional_edges('classify',lambda s:s['route'],{'billing':'billing','technical':'technical'})
    graph.add_edge('billing',END);graph.add_edge('technical',END)
    return graph.compile()

def run(data,live=False,model=None):
    return dict(build_graph().invoke({'message':require_text(data['message'],4000)}))
```

## Important lines
- `def build_graph():` — defines a callable stage and its input contract.
- `return graph.compile()` — returns the observable result consumed by tests and the evidence canvas.
- `def run(data,live=False,model=None):` — defines a callable stage and its input contract.
- `return dict(build_graph().invoke({'message':require_text(data['message'],4000)}))` — returns the observable result consumed by tests and the evidence canvas.

## Interface and reliability
The form submits related inputs together. Session state retains the last result; reset clears it. A spinner provides loading feedback. Input errors are shown in context; unknown provider errors are sanitized. Static HTML styles contain no user text. Every output carries explicit local/live labeling. The timer is not a provider latency benchmark. Local tests do not establish live provider correctness, visual browser quality, or production deployment.
