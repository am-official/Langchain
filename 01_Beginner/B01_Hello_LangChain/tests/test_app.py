import importlib.util
from pathlib import Path
import pytest
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableLambda
from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parents[1] / 'app.py'
spec = importlib.util.spec_from_file_location('hello_lab', APP)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

@pytest.mark.parametrize('language,word', [('English','Hello'),('Spanish','Hola'),('French','Bonjour')])
def test_demo(language, word):
    assert app.greet(' Ada ', language) == f'{word}, Ada! Welcome to your first LangChain lab.'

@pytest.mark.parametrize('name', ['', '  ', 'x'*81, 'Ada\nEnglish'])
def test_invalid_names(name):
    with pytest.raises(ValueError): app.greet(name)

def test_invalid_selection():
    with pytest.raises(ValueError): app.greet('Ada', language='Unknown')
    with pytest.raises(ValueError): app.greet('Ada', tone='Unknown')
    with pytest.raises(ValueError): app.greet('Ada', mode='Unknown')

@pytest.mark.parametrize('key', ['', 'YOUR_OPENAI_API_KEY_HERE'])
def test_live_requires_key(monkeypatch, key):
    monkeypatch.setenv('OPENAI_API_KEY',key)
    with pytest.raises(ValueError, match='OPENAI_API_KEY'): app.greet('Ada', mode='Live OpenAI')

def test_mock_model_receives_prompt_and_parser_handles_message():
    def respond(prompt):
        assert prompt.to_messages()[-1].content == 'Ada\nFrench\nProfessional'
        return AIMessage(content='Bonjour Ada.')
    assert app.greet('Ada','French','Professional','Live OpenAI',RunnableLambda(respond)) == 'Bonjour Ada.'

def test_ui_success_and_error():
    ui=AppTest.from_file(str(APP)).run()
    assert not ui.exception
    ui.button[0].click().run()
    assert not ui.exception
    assert 'Success:' in ui.success[0].value
    assert any('Hello, Ada!' in item.value for item in ui.markdown)
    ui.text_input[0].set_value('').run()
    ui.button[0].click().run()
    assert ui.error and not ui.success

def test_ui_missing_credentials(monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY','')
    ui=AppTest.from_file(str(APP)).run()
    ui.radio[0].set_value('Live OpenAI').run()
    ui.button[0].click().run()
    assert 'OPENAI_API_KEY' in ui.error[0].value
    assert not ui.exception
