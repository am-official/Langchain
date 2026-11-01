# Plan with Deep Agents — hands-on instructions
## Step 1: Prerequisites
Python 3.11–3.13 and a browser on Windows, macOS, or Linux. Internet is needed for package installation. No account or key is needed for local mode. Live mode requires an OpenAI account with credits and model access.
## Step 2: Installation
Open a terminal in `02_Intermediate/I13_Deep_Agents_Basics`.
Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```
macOS/Linux:
```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```
## Step 3: Environment configuration
Local mode needs no key. Windows: `Copy-Item .env.example .env`. macOS/Linux: `cp .env.example .env`. Replace the OpenAI placeholder in .env to use live mode; do not edit Python source. Never commit .env. Existing process values take precedence.
## Step 4: Running
Windows: `.venv\Scripts\python.exe -m streamlit run app.py`

macOS/Linux: `.venv/bin/python -m streamlit run app.py`

Use the browser address printed by Streamlit. Stop with Ctrl+C. Run from this project folder to load its theme configuration.
## Step 5: Hands-on demonstration
Use these three contracts (JSON-valued fields are pasted as JSON in the UI):
1. Input `{"task": "Study tools"}` → expected fields `{"todo_count": 1}`.
2. Input `{"task": "Study traces"}` → expected fields `{"todos": [{"content": "Study traces", "status": "in_progress"}]}`.
3. Input `{"task": "Study graphs"}` → expected fields `{"todo_count": 1}`.
## Step 6: Understanding the output
The evidence canvas exposes the returned fields instead of hiding intermediate results. Compare expected fields above, change one setting, and rerun. A green success message confirms completion, not answer quality or cloud deployment. Results retain their submitted mode until the next run.
## Step 7: Modify the application
1. Add a boundary input to sample_data/examples.json and define an expected result before changing code.
2. Extend the result with a useful intermediate value and assert its meaning in a test.
3. Change a UI default and confirm form submission and reset still work.
## Step 8: Troubleshooting
Read TROUBLESHOOTING.md. Check JSON syntax, input limits, interpreter selection, and project working directory before debugging providers.
## Step 9: Testing
Windows: `.venv\Scripts\python.exe -m pytest -q`; `.venv\Scripts\python.exe -m pip check`.

macOS/Linux: `.venv/bin/python -m pytest -q`; `.venv/bin/python -m pip check`.

Expected: all sample contracts and UI tests pass without provider calls. Cloud API and cross-platform launch checks remain unverified.
## Step 10: Certification connection
Provisional domain: Building Agents. Lesson skills: create_deep_agent, Built-in write_todos, State-backed backend. No independently verified official objective is claimed; see the root official-source status.
