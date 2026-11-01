# LangChain cheatsheet
## Compose a small chain
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages([('system', 'Be concise.'), ('human', '{question}')])
chain = prompt | model | StrOutputParser()
answer = chain.invoke({'question': 'What is a tool?'})
```
`model` must be a compatible runnable supplied by the application. B03 and B09 show executable examples. Use `.stream` when incremental delivery matters; assembling all chunks before rendering defeats streaming.

## Choose the control flow
Use a simple chain for fixed steps. Use `create_agent(model=..., tools=[...])` for a model/tool loop. Use LangGraph for explicit state transitions, branches, interrupts, or custom orchestration. Use Deep Agents when planning, virtual files, or delegated tasks are required. More machinery does not imply higher answer quality.

## Validate boundaries
Tools require schemas, allowlists, argument validation, bounded execution, and appropriate authorization. Pydantic structured output validates types and bounds; valid JSON alone does not establish schema validity. A fake model verifies protocol behavior, not the live model's reasoning.

## Modern versus legacy patterns
This repository uses runnable composition and create_agent rather than legacy LLMChain or initialize_agent patterns. Role-based messages keep system policy distinct from user text. Current official API status could not be independently retrieved; installed package API imports and local behavior were tested instead.
