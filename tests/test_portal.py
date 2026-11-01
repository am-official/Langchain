import importlib.util,sys
from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('portal',ROOT/'portal.py')
portal=importlib.util.module_from_spec(spec);spec.loader.exec_module(portal)
@pytest.mark.parametrize('number',[1,2,3])
def test_exam_weighting_and_scoring(number):
    questions=portal.load_exam(number)
    answers={q['id']:q['answer'] for q in questions}
    report=portal.grade_exam(questions,answers)
    assert report['correct']==40 and report['percent']==100
    assert all(value=={'correct':10,'total':10} for value in report['domains'].values())
    first=questions[0];answers[first['id']]=next(a for a in 'ABCD' if a!=first['answer'])
    report=portal.grade_exam(questions,answers)
    assert report['correct']==39 and len(report['missed'])==1
    assert report['missed'][0]['project']==first['project']

def test_missing_answers_rejected():
    with pytest.raises(ValueError):portal.grade_exam(portal.load_exam(1),{})

def test_catalog_filter_and_exam_empty_submission():
    ui=AppTest.from_file(str(ROOT/'portal.py')).run(timeout=30)
    assert not ui.exception
    ui.text_input[0].set_value('B14').run()
    assert any('1 studio matches' in x.value for x in ui.caption)
    ui.button[-1].click().run()
    assert ui.error and 'all 40' in ui.error[0].value
    assert not ui.exception
