import importlib.util
import sys
from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest
APP=Path(__file__).resolve().parents[1]/'app.py'
spec=importlib.util.spec_from_file_location('lesson_'+APP.parent.name,APP)
app=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=app
spec.loader.exec_module(app)
import json
CASES=json.loads((APP.parent/'sample_data/examples.json').read_text())
@pytest.mark.parametrize('case',CASES)
def test_sample_contract(case,monkeypatch,tmp_path):
    if hasattr(app,"DATA_DIR"): monkeypatch.setattr(app,"DATA_DIR",tmp_path)
    result=app.run(case['input'])
    for key,value in case['expected'].items():
        assert result[key]==value

def test_empty_input_rejected():
    with pytest.raises((ValueError,KeyError,TypeError)): app.run({})

def test_ui_submission(tmp_path):
    import shutil
    isolated=tmp_path/APP.parent.name
    shutil.copytree(APP.parent,isolated,ignore=shutil.ignore_patterns(".local","__pycache__",".pytest_cache",".venv"))
    ui=AppTest.from_file(str(isolated/"app.py")).run(timeout=30)
    assert not ui.exception
    ui.button[-1].click().run(timeout=30)
    assert not ui.exception
    assert ui.success and not ui.error
    ui.button[0].click().run(timeout=30)
    assert not ui.exception and not ui.success

def test_cloud_experiment_contract_without_network():
    from types import SimpleNamespace
    seen=[]
    class Result(list):experiment_name='test-experiment'
    def runner(target,**kwargs):
        assert kwargs['max_concurrency']==1
        assert target({'question':'tools'})['answer'] in ('tools','answer tools')
        score=kwargs['evaluators'][0](SimpleNamespace(outputs={'answer':'tools'}),SimpleNamespace(outputs={'answer':'tools'}))
        assert score['score'] is True
        seen.append(kwargs['experiment_prefix'])
        return Result([{'evaluation_results':{'results':[SimpleNamespace(score=1)]}}])
    result=app.run_cloud_experiments(object(),runner=runner)
    assert seen==['echo-v1','prefix-v2'] and len(result['experiments'])==2
