# LangGraph cheatsheet
```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
class State(TypedDict):
    value: str
    result: str
builder = StateGraph(State)
builder.add_node('work', lambda state: {'result': state['value'].upper()})
builder.add_edge(START, 'work')
builder.add_edge('work', END)
graph = builder.compile()
assert graph.invoke({'value': 'tools'})['result'] == 'TOOLS'
```
Nodes return state updates. Concurrent branches updating the same field require an appropriate reducer, such as `Annotated[list, operator.add]`; avoid accidental duplicate accumulation on resume.

`add_conditional_edges` makes branch policy explicit. `RetryPolicy` retries selected transient failures; idempotency is still necessary when a node performs side effects. A recursion limit bounds graph steps, not all resource consumption.

Checkpointing requires a checkpointer and a stable `configurable.thread_id`. A browser session is not a checkpoint database. `interrupt(...)` pauses dynamic execution; `Command(resume=...)` supplies a decision on the same thread. Nodes may replay on resume, so perform protected side effects after approval and make replay-safe operations. A03 demonstrates static step checkpoints; I09 demonstrates dynamic review.

SQLite illustrates process-restart durability on one disk. Backup, replication, concurrent writers, disaster recovery, authorization, and retention need separate design decisions.
