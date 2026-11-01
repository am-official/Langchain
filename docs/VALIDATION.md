# Validation evidence — 2026-11-01

## Automated results
- Full suite: **393 passed**, 0 failed, 0 errors, 0 skipped. Latest run: 11.81 seconds, CPython 3.12.14 on the managed Linux environment.
- Command: `.venv/bin/python -m pytest tests 01_Beginner 02_Intermediate 03_Advanced 05_Capstone_Projects -q --junitxml=docs/test-results.xml`.
- [JUnit evidence](test-results.xml) is from the current full run. Every project test file was collected.
- File-contract validator: 65 projects, 133 project Python files parsed, 120 original practice questions checked for domain balance and project references.
- Dependency check: all 110 installed packages compatible. Root requirements.lock.txt captures the tested set.
- Root assessment tests verify all three exam weightings, score totals, missed-topic mapping, and incomplete-answer rejection.

The suite uses actual installed framework APIs. Scripted local models test tool protocols and graph behavior without claiming model intelligence. Failure tests cover unsafe arithmetic, malformed schemas, missing evidence, checkpoint resume, tenant filtering, token tampering/expiry, optimistic locking, alert deduplication, trace provenance, and PDF page numbering.

## Real local integrations
- MCP: real stdio server discovery and tool invocation passed, including returned content. The restricted command sandbox caused initialization timeouts. The same integration passed outside that boundary. SDK warning about a Pydantic settings forward reference remains non-fatal; no warning was disabled.
- Graph serving: launched A08 with the documented uvicorn command; POST `/invoke` with `{"text":"hello deployment"}` returned `{"text":"hello deployment","answer":"Graph response: hello deployment"}`.
- Standalone install: copied B14 outside the repository to `/tmp/mastery-standalone-project`, created a fresh environment using its own requirements plus tested version constraints, and ran **11 passing tests**. No parent project imports were available.

The final portal-only regression after the static metric-card rendering refinement also passed all 5 tests.

## Browser evidence
Chromium was run against local Streamlit processes. B19 form submission produced a successful cited result. The portal search selected B14, incomplete exams displayed an error, and the shared layout had no horizontal page overflow at 390px. Screenshots were visually inspected; native controls retain labels and keyboard semantics. This is representative browser evidence, not a 65-project visual audit or a full accessibility certification.

- [B19 desktop](screenshots/B19-desktop.png)
- [B19 mobile](screenshots/B19-mobile.png)
- [Portal desktop](screenshots/portal-desktop.png)
- [Portal mobile](screenshots/portal-mobile.png)

## Unverified boundaries
No live paid OpenAI calls, OpenAI embedding calls, LangSmith cloud writes, cloud trace delivery, managed deployment, region provisioning, production identity integration, or alert notifications were performed. Optional SDK call contracts use injected clients/models in tests. Local multi-region routing and deployment-object ledgers explicitly remain demonstrations.

Official Academy/docs URLs returned proxy 403 during attempted retrieval. Current official objective wording and full syllabus coverage remain unverified. The source record and coverage matrix state this; the supplied brief is not presented as independently verified official evidence.

Windows/macOS commands are documented but not executed on those operating systems. Fresh independent dependency installation was demonstrated for B14; all project manifests were checked in the common resolved environment, not individually installed into 65 separate environments.

## GitHub
These checks were completed locally before the subsequent GitHub upload request. GitHub publication is tracked by repository commit history and does not establish cloud deployment.
