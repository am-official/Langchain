# How Compose the pipeline works

Run parallel text analyses through LCEL, then combine their results into one evidence object.

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
import re
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def run(data,live=False,model=None):
    text=require_text(data['text'],5000)
    pipeline=RunnableParallel(original=RunnablePassthrough(),words=RunnableLambda(lambda s:len(re.findall(r'\b\w+\b',s))),uppercase=RunnableLambda(str.upper)) | RunnableLambda(lambda result:{**result,'answer':str(result['words'])+' words analyzed'})
    return pipeline.invoke(text)
```

## Important lines
- `def run(data,live=False,model=None):` — defines a callable stage and its input contract.
- `return pipeline.invoke(text)` — returns the observable result consumed by tests and the evidence canvas.

## Interface and reliability
The form submits related inputs together. Session state retains the last result; reset clears it. A spinner provides loading feedback. Input errors are shown in context; unknown provider errors are sanitized. Static HTML styles contain no user text. Every output carries explicit local/live labeling. The timer is not a provider latency benchmark. Local tests do not establish live provider correctness, visual browser quality, or production deployment.
