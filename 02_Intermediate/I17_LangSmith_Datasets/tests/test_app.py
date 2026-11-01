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

# Additional behavior and failure contracts
def test_dataset_entries_have_unique_ids(monkeypatch,tmp_path):
    monkeypatch.setattr(app,'DATA_DIR',tmp_path)
    data={'dataset':'examples','question':'q','reference':'a'}
    first=app.run(data);second=app.run(data)
    assert first['created']['id']!=second['created']['id']
    assert len(second['examples'])==2

def test_cloud_dataset_uses_correct_schema_without_real_request():
    from types import SimpleNamespace
    class Client:
        def read_dataset(self,**kwargs):
            assert kwargs=={'dataset_name':'d'};return SimpleNamespace(id='dataset-id')
        def create_example(self,**kwargs):
            assert kwargs=={'inputs':{'question':'q'},'outputs':{'answer':'a'},'dataset_id':'dataset-id'}
            return SimpleNamespace(id='example-id')
    result=app.run({'dataset':'d','question':'q','reference':'a'},live=True,model=Client())
    assert result['example_id']=='example-id'
