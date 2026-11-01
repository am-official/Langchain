# Run the greeting studio
## Step 1: Prerequisites
Python 3.11–3.13, a terminal, and a browser on Windows, macOS, or Linux. Internet is needed to install dependencies. Demo needs no account. Optional live mode requires an OpenAI account, available credits, and access to gpt-4.1-mini.
## Step 2: Installation
Open a terminal in this project folder.

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
Demo requires no configuration. For live mode:
```powershell
Copy-Item .env.example .env
notepad .env
```
```sh
cp .env.example .env
# Open .env in your editor and replace the placeholder with your own key.
```
Existing process variables take precedence. Never commit or share your key.
## Step 4: Running
```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```
```sh
.venv/bin/python -m streamlit run app.py
```
Use the browser address printed by Streamlit. Keep the terminal open; Ctrl+C stops the app. No background service or database is required.
## Step 5: Hands-on demonstration
Select Demo. Submit each interaction:
1. Ada / English / Warm → Hello, Ada! Welcome to your first LangChain lab.
2. Lin / Spanish / Professional → Hola, Lin! Your learning session is ready.
3. Sam / French / Playful → Bonjour, Sam! Let the learning adventure begin!
## Step 6: Understanding the output
The result records the mode, language, tone, and elapsed chain time. A success message confirms all three pipeline stages completed. Demo output is fixed, not AI-generated. Previously submitted results retain their original settings until another submission.
## Step 7: Modify the application
1. Change the warm closing sentence and update its expected test output.
2. Add a fourth tone in both TONES and the demo dictionary.
3. Extend the prompt to request two sentences in live mode, then test with a mock message.
## Step 8: Troubleshooting
See TROUBLESHOOTING.md. Check your interpreter and working directory first. Provider failures do not prevent Demo mode.
## Step 9: Testing
```powershell
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m pip check
```
```sh
.venv/bin/python -m pytest -q
.venv/bin/python -m pip check
```
Expect all tests to pass. Tests exercise demo outputs, input validation, prompt composition, parsing, key handling, and Streamlit form interaction without network calls.
## Step 10: Certification connection
Provisional domain: Building Agents. Foundation: structured model input and runnable execution. This is not a verified official objective mapping; consult the repository's official-source status before using it as exam coverage evidence.
