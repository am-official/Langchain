"""A dataset with provenance — self-contained learning application."""
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
CODE = 'I17'
TITLE = 'A dataset with provenance'
DESCRIPTION = 'Create and list versionable local evaluation examples, with optional explicit LangSmith upload code documented separately.'
FIELDS = {'dataset': {'label': 'Dataset name', 'default': 'agent-basics', 'kind': 'text'}, 'question': {'label': 'Example input', 'default': 'What do agents use?', 'kind': 'text'}, 'reference': {'label': 'Reference', 'default': 'tools', 'kind': 'text'}}
LIVE = True
CONCEPTS = ['Evaluation example inputs and references', 'Stable example IDs', 'Local dataset versus LangSmith dataset']
LOCAL_NOTE = 'Local mode is a deterministic teaching experiment, not a live language model or cloud deployment.'
SUCCESS = 'Success: the experiment completed. Inspect the evidence against the sample expectations.'

import sqlite3
import uuid
DATA_DIR=Path(__file__).with_name('.local')
def dataset_db():
    DATA_DIR.mkdir(exist_ok=True,parents=True)
    db=sqlite3.connect(DATA_DIR/'datasets.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS examples(id TEXT PRIMARY KEY, dataset TEXT NOT NULL, input TEXT NOT NULL, reference TEXT NOT NULL)')
    return db

from langsmith import Client

def langsmith_client():
    key=os.getenv('LANGSMITH_API_KEY','').strip()
    if not key or key=='YOUR_LANGSMITH_API_KEY_HERE':raise ValueError('Set LANGSMITH_API_KEY in .env for live LangSmith operations.')
    return Client(api_key=key)

def run_local(data,live=False,model=None):
    name=require_text(data['dataset'],80);question=require_text(data['question'],2000);reference=require_text(data['reference'],4000)
    identifier=str(uuid.uuid4())
    with dataset_db() as db:
        db.execute('INSERT INTO examples VALUES (?,?,?,?)',(identifier,name,question,reference))
        rows=db.execute('SELECT id,input,reference FROM examples WHERE dataset=? ORDER BY rowid',(name,)).fetchall()
    return {'dataset':name,'created':{'id':identifier,'input':question,'reference':reference},'examples':[{'id':i,'input':q,'reference':r} for i,q,r in rows],'storage':'local SQLite; not a LangSmith cloud dataset'}


def run(data,live=False,model=None):
    if not live:return run_local(data)
    from langsmith.utils import LangSmithNotFoundError
    name=require_text(data['dataset'],80);question=require_text(data['question'],2000);reference=require_text(data['reference'],4000)
    client=model if model is not None else langsmith_client()
    try:dataset=client.read_dataset(dataset_name=name)
    except LangSmithNotFoundError:dataset=client.create_dataset(dataset_name=name,description='Agent engineering learning examples; no sensitive data.')
    example=client.create_example(inputs={'question':question},outputs={'answer':reference},dataset_id=dataset.id)
    return {'dataset':name,'dataset_id':str(dataset.id),'example_id':str(example.id),'service':'LangSmith cloud write acknowledged; inspect the dataset in your account'}

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
        st.caption('Live mode writes to your LangSmith account. Use a disposable learning project and non-sensitive examples.' if live else LOCAL_NOTE)
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
