"""Let the agent calculate — self-contained learning application."""
from pathlib import Path
import os
import json
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
load_dotenv(Path(__file__).with_name('.env'), override=False)

def require_text(value, limit=20000):
    if not isinstance(value, str) or not value.strip() or len(value)>limit:
        raise ValueError(f'Enter nonempty text up to {limit} characters.')
    return value.strip()

def openai_model():
    key=os.getenv('OPENAI_API_KEY','').strip()
    if not key or key=='YOUR_OPENAI_API_KEY_HERE':
        raise ValueError('Set OPENAI_API_KEY in the project .env before live execution.')
    return ChatOpenAI(model='gpt-4.1-mini',api_key=key,timeout=30,max_retries=1,temperature=0)

def ask(system,text,model=None):
    chain=ChatPromptTemplate.from_messages([('system',system),('human','{text}')]) | (model if model is not None else openai_model()) | StrOutputParser()
    return chain.invoke({'text':text})
CODE = 'B14'
TITLE = 'Let the agent calculate'
DESCRIPTION = 'Run a real create_agent tool loop using restricted arithmetic and inspect every tool transition.'
FIELDS = {'expression': {'label': 'Arithmetic expression', 'default': '2 + 3 * 4', 'kind': 'text'}}
LIVE = True
CONCEPTS = ['create_agent control loop', 'Restricted arithmetic tool', 'Tool result inspection']
LOCAL_NOTE = 'Local mode is a deterministic teaching experiment, not a live language model or cloud deployment.'
SUCCESS = 'Success: the experiment completed. Inspect the evidence against the sample expectations.'

import ast
import operator
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.messages import ToolMessage

@tool
def calculate(expression:str)->str:
    """Evaluate bounded arithmetic using +, -, *, /, and parentheses. No Python execution."""
    require_text(expression,200)
    tree=ast.parse(expression,mode='eval')
    if len(list(ast.walk(tree)))>50: raise ValueError('Expression too complex.')
    ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
    def visit(node):
        if isinstance(node,ast.Expression): return visit(node.body)
        if isinstance(node,ast.Constant) and type(node.value) in (int,float): value=node.value
        elif isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)): value=visit(node.operand)*(1 if isinstance(node.op,ast.UAdd) else -1)
        elif isinstance(node,ast.BinOp) and type(node.op) in ops:
            try: value=ops[type(node.op)](visit(node.left),visit(node.right))
            except ZeroDivisionError as exc: raise ValueError('Cannot divide by zero.') from exc
        else: raise ValueError('Only bounded arithmetic is permitted.')
        if not -1e12<=value<=1e12: raise ValueError('Magnitude exceeds safe lesson limit.')
        return value
    return str(visit(tree))

class LocalToolModel(BaseChatModel):
    expression:str
    @property
    def _llm_type(self): return 'deterministic-calculator-teaching-model'
    def bind_tools(self,tools,**kwargs): return self
    def _generate(self,messages,stop=None,run_manager=None,**kwargs):
        result=next((m for m in reversed(messages) if isinstance(m,ToolMessage)),None)
        msg=AIMessage(content=str(result.content)) if result else AIMessage(content='',tool_calls=[{'name':'calculate','args':{'expression':self.expression},'id':'arithmetic-1','type':'tool_call'}])
        return ChatResult(generations=[ChatGeneration(message=msg)])

def run(data,live=False,model=None):
    expression=require_text(data['expression'],200)
    # Validate before any model request, and never evaluate Python source.
    expected=calculate.invoke({'expression':expression})
    agent=create_agent(model=model if model is not None else openai_model() if live else LocalToolModel(expression=expression),tools=[calculate],system_prompt='Use calculate to evaluate the exact arithmetic expression. Return its result.')
    state=agent.invoke({'messages':[HumanMessage(content=expression)]},config={'recursion_limit':8})
    tools=[m for m in state['messages'] if isinstance(m,ToolMessage)]
    if not tools: raise ValueError('No calculator tool was executed.')
    return {'answer':state['messages'][-1].content,'numeric_result':expected,'tool_calls':len(tools),'messages':[{'role':m.type,'content':m.content} for m in state['messages']]}

def main():
    st.set_page_config(page_title=TITLE+' · Agent Atelier',page_icon='✦',layout='wide')
    st.markdown("""<style>
    .stApp {background:radial-gradient(ellipse at top left,#262044 0%,#0e1220 65%);}
    .block-container {max-width:1180px;padding-top:3rem;padding-bottom:3rem;}
    h1 {font-size:clamp(2.4rem,5vw,4rem)!important;letter-spacing:-.045em;line-height:1.1!important;}
    h2,h3 {letter-spacing:-.025em;}
    .eyebrow {color:#a9eddb;letter-spacing:.2em;font-size:.75rem;font-weight:700;}
    .intro {color:#bdc6dd;line-height:1.7;font-size:1.1rem;max-width:760px;}
    button {border-radius:12px!important;min-height:44px;}
    </style>""",unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">AGENT ATELIER / '+CODE+' / HANDS-ON LAB</div>',unsafe_allow_html=True)
    st.title(TITLE)
    st.markdown('<p class="intro">'+DESCRIPTION+'</p>',unsafe_allow_html=True)
    st.caption('01 / Explore the input     →     02 / Run the experiment     →     03 / Inspect the evidence')
    left,right=st.columns([1,1.15],gap='large')
    with left:
        st.subheader('Experiment studio')
        live=st.toggle('Live service execution',value=False) if LIVE else False
        st.caption('Live mode sends data to the configured service and may incur charges.' if live else LOCAL_NOTE)
        if st.button('Reset workspace'):
            st.session_state.clear()
            st.rerun()
        with st.form('experiment'):
            payload={}
            for key,field in FIELDS.items():
                kind=field.get('kind','text')
                if kind=='choice': value=st.selectbox(field['label'],field['choices'])
                elif kind=='number': value=st.number_input(field['label'],value=field['default'],min_value=field.get('min',1),max_value=field.get('max',100))
                else: value=st.text_area(field['label'],value=field['default'],height=120 if kind=='text' else 200)
                payload[key]=value
            if CODE in ('B02','B12'): payload['history']=st.session_state.get('history',[])
            submitted=st.form_submit_button('Run experiment ↗',type='primary',use_container_width=True)
        if submitted:
            st.session_state.pop('result',None)
            try:
                start=time.perf_counter()
                with st.spinner('Working through the pipeline…'):
                    result=run(payload,live=live)
                    if CODE=='B11':
                        st.write_stream(iter(result['chunks']))
                if CODE in ('B02','B12'): st.session_state.history=result['history']
                st.session_state.result=dict(data=result,elapsed=time.perf_counter()-start,live=live)
            except (ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
                st.error('Check the input: '+str(exc))
            except Exception:
                st.error('Execution failed. Check the configuration and service availability; use local mode to continue. See TROUBLESHOOTING.md.')
    with right:
        st.subheader('Evidence canvas')
        with st.container(border=True):
            saved=st.session_state.get('result')
            if saved:
                st.caption('LIVE SERVICE RESULT' if saved['live'] else 'LOCAL / DETERMINISTIC RESULT')
                result=saved['data']
                if 'answer' in result: st.write(result['answer'])
                st.json(result,expanded=True)
                st.success(SUCCESS)
                st.caption(f"Pipeline duration: {saved['elapsed']:.3f}s · Includes local processing")
                st.download_button('Download result ↓',json.dumps(result,indent=2,ensure_ascii=False),'result.json','application/json')
            else:
                st.markdown('### A little input. A useful discovery.')
                st.write('Start with the prepared example. Change one variable, run again, and compare the evidence.')
                st.caption('No API key required for the local experiment.')
        with st.expander('What to look for',expanded=True):
            for item in CONCEPTS: st.write('• '+item)
    st.divider()
    st.caption('LEARN BY BUILDING · Local results are not live cloud verification · Exam objective alignment provisional')

if __name__=='__main__': main()
