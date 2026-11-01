# Compare experiments — hands-on instructions
## Step 1: Prerequisites
Python 3.11–3.13 and a browser on Windows, macOS, or Linux. Internet is needed for package installation. No account or key is needed for local mode. This lesson performs its experiment locally.
## Step 2: Installation
Open a terminal in `02_Intermediate/I18_LangSmith_Experiments`.
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
Local mode needs no key. Windows: `Copy-Item .env.example .env`. macOS/Linux: `cp .env.example .env`. No secrets are required or requested. Never commit .env. Existing process values take precedence.
## Step 4: Running
Windows: `.venv\Scripts\python.exe -m streamlit run app.py`

macOS/Linux: `.venv/bin/python -m streamlit run app.py`

Use the browser address printed by Streamlit. Stop with Ctrl+C. Run from this project folder to load its theme configuration.
## Step 5: Hands-on demonstration
Use these three contracts (JSON-valued fields are pasted as JSON in the UI):
1. Input `{"examples": [{"input": "tools", "reference": "tools"}]}` → expected fields `{"scores": {"echo-v1": 1.0, "prefix-v2": 0.0}, "examples": 1}`.
2. Input `{"examples": [{"input": "x", "reference": "answer x"}]}` → expected fields `{"scores": {"echo-v1": 0.0, "prefix-v2": 1.0}}`.
3. Input `{"examples": [{"input": "a", "reference": "b"}]}` → expected fields `{"scores": {"echo-v1": 0.0, "prefix-v2": 0.0}}`.
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
Provisional domain: Testing Agents. Lesson skills: Same dataset across versions, Per-example evaluator results, Aggregate experiment comparison. No independently verified official objective is claimed; see the root official-source status.

## Optional live LangSmith workflow
Live mode evaluates the existing LANGSMITH_DATASET (default agent-basics), ignoring the local JSON field. Create it with I17 first. Examples must have inputs.question and outputs.answer. Two deterministic candidate versions are uploaded as experiments with a code evaluator. No OpenAI key is needed. Configure LANGSMITH_API_KEY in .env. Live writes require your account and remain unverified here; SDK boundaries are tested with injected clients. Do not upload sensitive data.
