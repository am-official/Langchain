# Troubleshooting
- Missing module: run pip with the same virtual-environment interpreter used to launch Streamlit.
- Missing requirements.txt: change into this project directory before installing.
- Port already used: pass `--server.port 8502` to Streamlit.
- Missing key: copy .env.example to .env beside app.py and replace the placeholder. Restart after changes. An existing process variable takes precedence.
- Provider request failed: check provider account quota, selected model access, key validity, and outbound HTTPS access. Do not paste keys or raw request logs into issues. Live mode remains unverified until a real request succeeds.
- Unexpected demo translation: only Hello/Hola/Bonjour changes language; closing sentences are intentionally English.
- Test invocation finds no tests: use `python -m pytest -q` inside this folder and confirm tests/test_app.py exists.
- Layout concerns: desktop/mobile visual review remains separate from functional AppTest validation. Report viewport dimensions and reproduction steps.
