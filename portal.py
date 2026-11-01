"""Learning catalog and original mock-exam runner. streamlit run portal.py"""
from pathlib import Path
import json
from collections import defaultdict
import streamlit as st
ROOT=Path(__file__).resolve().parent


def load_exam(number):
    if number not in (1,2,3):raise ValueError('Choose exam 1, 2, or 3.')
    rows=json.loads((ROOT/f'04_Certification_Preparation/Mock_Exam_{number:02}/exam.json').read_text())
    counts={domain:sum(q['domain']==domain for q in rows) for domain in ('Building','Testing','Deploying','Monitoring')}
    if len(rows)!=40 or any(n!=10 for n in counts.values()):raise ValueError('Exam must contain exactly 10 questions per domain.')
    if len({q['id'] for q in rows})!=40:raise ValueError('Duplicate question IDs.')
    return rows


def grade_exam(questions,answers):
    if set(answers)!={q['id'] for q in questions} or any(not isinstance(v,str) or v not in 'ABCD' or len(v)!=1 for v in answers.values()):
        raise ValueError('Answer all questions with one choice A–D.')
    domains=defaultdict(lambda:{'correct':0,'total':0});topics=defaultdict(lambda:{'correct':0,'total':0});missed=[]
    for q in questions:
        correct=answers[q['id']]==q['answer']
        for group,key in ((domains,q['domain']),(topics,q['topic'])):
            group[key]['correct']+=int(correct);group[key]['total']+=1
        if not correct:missed.append({'id':q['id'],'topic':q['topic'],'project':q['project'],'answer':q['answer']})
    correct=sum(v['correct'] for v in domains.values())
    return {'correct':correct,'total':len(questions),'percent':100*correct/len(questions),'domains':dict(domains),'topics':dict(topics),'missed':missed,'study_target_met':correct/len(questions)>=.9}


def main():
    st.set_page_config(page_title='Agent Atelier · Learning Studio',page_icon='✦',layout='wide')
    st.markdown('''<style>
    .stApp {background:radial-gradient(ellipse at 5% 0%,#30234f 0%,#0e1220 60%);color:#edf0fc;}
    .block-container {max-width:1200px;padding-top:3.5rem;}
    h1 {font-size:clamp(2.7rem,6vw,5rem)!important;letter-spacing:-.05em;line-height:1.05!important;}
    h2,h3 {letter-spacing:-.025em;}
    .kicker {color:#9ee6d0;letter-spacing:.22em;font-size:.75rem;font-weight:700;}
    .lead {font-size:1.15rem;line-height:1.7;color:#bec6dd;max-width:720px;}
    button {border-radius:12px!important;min-height:44px;}
    </style>''',unsafe_allow_html=True)
    st.markdown('<div class="kicker">AGENT ATELIER / LEARN · BUILD · EXAMINE</div>',unsafe_allow_html=True)
    st.title('Build understanding.\nThen build agents.')
    st.markdown('<p class="lead">Sixty-five hands-on studios. One deliberate path from your first prompt to observable, tested agent systems.</p>',unsafe_allow_html=True)
    items=json.loads((ROOT/'docs/PROJECT_STATUS.json').read_text())
    st.html("""<style>
    .metric-grid {display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:2rem 0;}
    .metric-card {padding:18px 20px;border:1px solid #35334e;border-radius:16px;background:#15182a;}
    .metric-label {font-size:.7rem;letter-spacing:.12em;color:#bec6dd;}
    .metric-value {font-size:2rem;line-height:1.3;color:#a9eddb;margin-top:6px;}
    @media(max-width:600px){.metric-grid{grid-template-columns:repeat(2,1fr);gap:10px}.metric-card{padding:14px}}
    </style><div class="metric-grid" role="group" aria-label="Curriculum project counts">
    <div class="metric-card"><div class="metric-label">BEGINNER</div><div class="metric-value">20</div></div>
    <div class="metric-card"><div class="metric-label">INTERMEDIATE</div><div class="metric-value">20</div></div>
    <div class="metric-card"><div class="metric-label">ADVANCED</div><div class="metric-value">20</div></div>
    <div class="metric-card"><div class="metric-label">CAPSTONES</div><div class="metric-value">5</div></div>
    </div>""")
    catalog,assessment=st.tabs(['Explore the studios','Test your understanding'])
    with catalog:
        st.subheader('Choose your next discovery')
        st.caption('Local teaching applications. Cloud features and official certification alignment have separate verification limits.')
        left,right=st.columns([1,2])
        level=left.selectbox('Learning stage',['All','Beginner','Intermediate','Advanced','Capstone'])
        query=right.text_input('Search by topic or project ID',placeholder='Try retrieval, middleware, or B14')
        prefixes={'Beginner':'01_','Intermediate':'02_','Advanced':'03_','Capstone':'05_'}
        visible=[x for x in items if (level=='All' or x['path'].startswith(prefixes[level])) and query.casefold() in x['path'].casefold()]
        st.caption('1 studio matches your interests' if len(visible)==1 else f'{len(visible)} studios match your interests')
        for index,item in enumerate(visible):
            p=Path(item['path']);code=p.name.split('_')[0];name=' '.join(p.name.split('_')[1:])
            with st.container(border=True):
                st.caption(code+' / '+p.parent.name.split('_',1)[1].replace('_',' ').upper())
                st.markdown('### '+name)
                st.caption(item['status'].replace('_',' '))
                command=f'cd "{item["path"]}"\npython -m streamlit run app.py'
                with st.expander('Open this studio'):
                    st.write('After installing dependencies in your active environment, run these commands from the repository root:')
                    st.code(command,language='sh')
                    st.write('Project guide: '+item['path']+'/INSTRUCTIONS.md')
                    st.write('Local tests: python -m pytest "'+item['path']+'/tests" -q')
        if not visible:st.info('Try another topic or choose All learning stages.')
    with assessment:
        st.subheader('Practice with evidence')
        st.write('Three original 40-question mocks, with ten questions per domain. The 90% target is a study goal, not a certification guarantee.')
        st.warning('Official syllabus verification is blocked by network policy. These are original practice materials based on the supplied topic brief.')
        number=st.selectbox('Mock exam',[1,2,3])
        questions=load_exam(number)
        with st.form(f'exam-{number}'):
            answers={}
            for i,q in enumerate(questions,1):
                st.markdown(f'**{i:02} / {q["domain"]} · {q["topic"]}**')
                answers[q['id']]=st.radio(q['question'],list('ABCD'),format_func=lambda value,q=q:value+'. '+q['options']['ABCD'.index(value)],index=None,key=q['id'])
            submitted=st.form_submit_button('Score my attempt ↗',type='primary')
        if submitted:
            if any(v is None for v in answers.values()):st.error('Answer all 40 questions before scoring.')
            else:
                report=grade_exam(questions,answers)
                st.metric('Your practice score',f"{report['percent']:.0f}%",f"{report['correct']} / 40 correct",delta_color='off')
                st.success('Study target met. Repeat after a study interval and complete the practical assessment.' if report['study_target_met'] else 'Review the missed topics, revisit their studios, then try again.')
                st.json(report['domains'])
                st.download_button('Download scoring evidence',json.dumps(report,indent=2),'practice-score.json','application/json')
                for q in questions:
                    with st.expander(q['id']+' · '+q['topic']+' · '+('Correct' if answers[q['id']]==q['answer'] else 'Review')):
                        st.write('Correct answer: '+q['answer'])
                        for letter,reason in q['explanations'].items():st.write(letter+'. '+reason)
                        st.write('Revisit: '+q['project'])
    st.divider()
    st.caption('LEARNING IS A PRACTICE · No paid account needed for local studios · Never commit API keys')

if __name__=='__main__':main()
