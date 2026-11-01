# How Durability is a design choice works

Write versioned user state transactionally, enforce optimistic concurrency, and verify it after reopening the database.

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
import sqlite3
import uuid
import hashlib
DATA_DIR=Path(__file__).with_name('.local')
from contextlib import contextmanager
@contextmanager
def connect():
    DATA_DIR.mkdir(exist_ok=True,parents=True)
    db=sqlite3.connect(DATA_DIR/'platform.sqlite')
    try:
        with db:yield db
    finally:db.close()

def run(data,live=False,model=None):
    key=require_text(data['key'],80);value=require_text(data['value'],2000);expected=int(data['expected_version'])
    if expected<0:raise ValueError('Expected version cannot be negative.')
    with connect() as db:
        db.execute('CREATE TABLE IF NOT EXISTS records(key TEXT PRIMARY KEY,value TEXT,version INTEGER NOT NULL)')
        db.execute('BEGIN IMMEDIATE')
        current=db.execute('SELECT version FROM records WHERE key=?',(key,)).fetchone()
        version=current[0] if current else 0
        if version!=expected:raise ValueError(f'Version conflict: current version is {version}. Reload before saving.')
        db.execute('INSERT INTO records VALUES (?,?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,version=excluded.version',(key,value,version+1))
    with connect() as db: saved=db.execute('SELECT value,version FROM records WHERE key=?',(key,)).fetchone()
    return {'key':key,'value':saved[0],'version':saved[1],'storage':'local SQLite; durable across process restarts, not disk loss or region failure'}
```

## Important lines
- `def connect():` — defines a callable stage and its input contract.
- `return sqlite3.connect(DATA_DIR/'platform.sqlite')` — returns the observable result consumed by tests and the evidence canvas.
- `def run(data,live=False,model=None):` — defines a callable stage and its input contract.
- `return {'key':key,'value':saved[0],'version':saved[1],'storage':'local SQLite; durable across process restarts, not disk loss or region failure'}` — returns the observable result consumed by tests and the evidence canvas.

## Interface and reliability
The form submits related inputs together. Session state retains the last result; reset clears it. A spinner provides loading feedback. Input errors are shown in context; unknown provider errors are sanitized. Static HTML styles contain no user text. Every output carries explicit local/live labeling. The timer is not a provider latency benchmark. Local tests do not establish live provider correctness, visual browser quality, or production deployment.
