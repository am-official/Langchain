from fastapi import FastAPI
from pydantic import BaseModel,Field
from app import graph
app=FastAPI(title='Local graph serving lab')
class Input(BaseModel):
    text:str=Field(min_length=1,max_length=2000)
@app.post('/invoke')
def invoke(value:Input):return graph.invoke({'text':value.text})
@app.get('/health')
def health():return {'ready':True}
