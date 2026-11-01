# Troubleshooting
## First establish the boundary
Reproduce with the project's sample input in local mode. If that fails, inspect validation and dependency installation. If only live mode fails, inspect account access, model availability, credentials, and network policy. Never disable TLS verification as a workaround.

## Interpreter mismatch
Use `python -m pip` and `python -m streamlit` from the same virtual environment. On Windows, call `.venv\Scripts\python.exe` directly. The managed cloud environment uses uv and an environment without pip; use `UV_CACHE_DIR=/workspace/.cache/uv uv pip ... --python .venv/bin/python` there.

## Stdio restrictions
The real MCP integration needs supported child-process pipes. It passed outside the cloud command sandbox; constrained sandbox execution timed out. Do not substitute mocked discovery and claim a transport pass.

## Persistent examples
I09, A03, A13, and C04 intentionally retain state. A pending thread must be resumed, and optimistic concurrency requires the latest version. Use a new job/thread/key for a fresh demonstration. Tests isolate databases and do not erase user data. To reset your own teaching database, stop the app and back up its ignored .local directory first.

## PDF limitations
I10 extracts text from unencrypted PDFs; scanned documents require OCR. The teaching limits are 5 MB and 50 pages. Keep page text within retrieval limits; split larger documents before indexing.

## UI and browser
Run from the project folder to load its theme. Native widgets preserve keyboard behavior. B19 and the portal have representative browser checks; all project form paths have AppTest coverage. This is not a claim that every live integration or every browser was visually audited.
