"""Pause before the action — self-contained learning application."""
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
CODE = 'I09'
TITLE = 'Pause before the action'
DESCRIPTION = 'Persist a graph interrupt and resume the same thread only after an explicit approval decision.'
FIELDS = {'thread': {'label': 'Thread identifier', 'default': 'approval-demo', 'kind': 'text'}, 'action': {'label': 'Decision', 'default': 'pause', 'kind': 'choice', 'choices': ['pause', 'approve', 'reject']}, 'request': {'label': 'Proposed action', 'default': 'Send a draft response', 'kind': 'text'}}
LIVE = False
CONCEPTS = ['interrupt and Command resume', 'Durable checkpoint thread', 'Approval before side effects']
LOCAL_NOTE = 'Local mode is a deterministic teaching experiment, not a live language model or cloud deployment.'
SUCCESS = 'Success: the experiment completed. Inspect the evidence against the sample expectations.'

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

from langgraph.types import interrupt, Command
from langgraph.checkpoint.sqlite import SqliteSaver
DATA_DIR=Path(__file__).with_name('.local')
class ApprovalState(TypedDict):
    request:str
    decision:str
    executed:bool

def review(state):
    decision=interrupt({'proposed_action':state['request'],'message':'Approve or reject this local demonstration.'})
    return {'decision':decision,'executed':decision=='approve'}

def run(data,live=False,model=None):
    thread=require_text(data['thread'],80);action=data['action'];request=require_text(data['request'],2000)
    if action not in ('pause','approve','reject'): raise ValueError('Invalid approval action.')
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    with SqliteSaver.from_conn_string(str(DATA_DIR/'checkpoints.sqlite')) as saver:
        graph=StateGraph(ApprovalState);graph.add_node('review',review);graph.add_edge(START,'review');graph.add_edge('review',END)
        compiled=graph.compile(checkpointer=saver);config={'configurable':{'thread_id':thread}}
        snapshot=compiled.get_state(config)
        if action=='pause':
            if snapshot.next: raise ValueError('This thread is already waiting. Approve/reject it, or choose a new thread ID.')
            result=compiled.invoke({'request':request,'decision':'pending','executed':False},config)
        else:
            if not snapshot.next: raise ValueError('Pause a request on this thread before resuming.')
            result=compiled.invoke(Command(resume=action),config)
        return {'thread':thread,'pending':bool(result.get('__interrupt__')),'decision':result['decision'],'executed':result['executed'],'request':result['request'],'effect':'local state transition only; no external message sent'}

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
