# How Parse with confidence works

Turn JSON model-style output into a typed task; reject invalid output rather than silently repairing it.

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
from pydantic import BaseModel, Field, ConfigDict
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException
class Task(BaseModel):
    model_config=ConfigDict(extra='forbid')
    task:str=Field(min_length=1)
    priority:int=Field(ge=1,le=3,strict=True)
    done:bool=Field(strict=True)

def run(data,live=False,model=None):
    text=require_text(data['text'],4000);parser=PydanticOutputParser(pydantic_object=Task)
    try: result=parser.invoke(text)
    except OutputParserException as exc: raise ValueError('Output must be a JSON task with priority 1–3 and boolean done.') from exc
    return {'task':result.model_dump(),'format_instructions':parser.get_format_instructions()}
```

## Important lines
- `def run(data,live=False,model=None):` — defines a callable stage and its input contract.
- `try: result=parser.invoke(text)` — executes the composed pipeline with the prepared input.
- `return {'task':result.model_dump(),'format_instructions':parser.get_format_instructions()}` — returns the observable result consumed by tests and the evidence canvas.

## Interface and reliability
The form submits related inputs together. Session state retains the last result; reset clears it. A spinner provides loading feedback. Input errors are shown in context; unknown provider errors are sanitized. Static HTML styles contain no user text. Every output carries explicit local/live labeling. The timer is not a provider latency benchmark. Local tests do not establish live provider correctness, visual browser quality, or production deployment.
